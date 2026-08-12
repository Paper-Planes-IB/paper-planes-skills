#!/usr/bin/env python3
"""Incrementally archive generated Granola notes into the synced Drive folder."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

API = "https://public-api.granola.ai/v1"
ARCHIVE = Path(os.environ.get(
    "GRANOLA_ARCHIVE_DIR",
    "/Users/natalie/Library/CloudStorage/GoogleDrive-tokaeva@paper-planes.ru/Shared drives/Paper Planes/4. Производство/Встречи",
))
MANIFEST = ARCHIVE / "manifest.json"
STATE = ARCHIVE / ".granola-api-state.json"


def keychain_token() -> str:
    return subprocess.check_output([
        "/usr/bin/security", "find-generic-password", "-a", "paper-planes",
        "-s", "granola-archive-api", "-w",
    ], text=True).strip()


def api(path: str) -> dict:
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {keychain_token()}",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name, dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def safe_name(value: str) -> str:
    value = re.sub(r"[/:]", " — ", value or "Без названия")
    value = re.sub(r"[\\?%*|\"<>]", "_", value)
    return re.sub(r"\s+", " ", value).strip(" .")[:120]


def public_folders() -> dict[str, dict]:
    result, cursor = {}, None
    while True:
        params = {"page_size": 30}
        if cursor:
            params["cursor"] = cursor
        page = api("/folders?" + urllib.parse.urlencode(params))
        for folder in page.get("folders", []):
            if folder.get("name") != "Проекты":
                result[folder["id"]] = folder
        if not page.get("hasMore"):
            return result
        cursor = page.get("cursor")
        if not cursor:
            return result


def canonical_id(note: dict) -> str:
    match = re.search(r"/([0-9a-f]{8}-[0-9a-f-]{27,36})(?:$|[?#])", note.get("web_url", ""), re.I)
    return match.group(1) if match else note["id"]


def choose_project(note: dict, allowed: dict[str, dict]) -> tuple[Optional[str], list[str]]:
    folders = [f for f in note.get("folder_membership", []) if f.get("id") in allowed]
    ids = [f.get("id") for f in folders if f.get("id")]
    if not folders:
        return None, ids
    parent_ids = {f.get("parent_folder_id") for f in folders if f.get("parent_folder_id")}
    leaves = [f for f in folders if f.get("id") not in parent_ids] or folders
    existing = {p.name: p.name for p in ARCHIVE.iterdir() if p.is_dir()}
    candidates = sorted((safe_name(f.get("name", "")), f) for f in leaves)
    for name, _ in candidates:
        if name in existing:
            return name, ids
    return candidates[0][0] or "_Неразобранное", ids


def transcript_text(note: dict) -> str:
    chunks = note.get("transcript")
    if chunks is None:
        payload = api(f"/notes/{note['id']}/transcript")
        chunks = payload.get("transcript", payload.get("items", []))
    lines = []
    for chunk in chunks or []:
        speaker = chunk.get("speaker") or {}
        label = speaker.get("diarization_label") or speaker.get("attribution")
        if not label:
            label = "Me" if speaker.get("source") == "microphone" else "Them"
        label = {"me": "Me", "them": "Them"}.get(str(label).lower(), str(label))
        lines.append(f"{label}: {chunk.get('text', '').strip()}")
    return "\n\n".join(line for line in lines if line.strip())


def render(note: dict, meeting_id: str, project: str, folder_ids: list[str]) -> str:
    event = note.get("calendar_event") or {}
    date = event.get("scheduled_start_time") or note.get("created_at") or dt.datetime.now(dt.timezone.utc).isoformat()
    title = note.get("title") or event.get("event_title") or "Без названия"
    ids = "\n".join(f'  - "{x}"' for x in folder_ids)
    exported = dt.datetime.now(dt.timezone.utc).isoformat()
    return (
        "---\n"
        f'meeting_id: "{meeting_id}"\n'
        f'granola_note_id: "{note["id"]}"\n'
        f'title: {json.dumps(title, ensure_ascii=False)}\n'
        f'date: "{date}"\n'
        f'project: {json.dumps(project, ensure_ascii=False)}\n'
        f"granola_folder_ids:\n{ids if ids else '  []'}\n"
        f'source: "{note.get("web_url", "")}"\n'
        f'exported_at: "{exported}"\n'
        "---\n\n"
        f"# {title}\n\n## Транскрипт\n\n{transcript_text(note)}\n"
    )


def list_recent() -> list[dict]:
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    since = state.get("cursor_time")
    if not since:
        since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=2)).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    notes, cursor = [], None
    while True:
        params = {"created_after": since}
        if cursor:
            params["cursor"] = cursor
        page = api("/notes?" + urllib.parse.urlencode(params))
        notes.extend(page.get("notes", []))
        if not page.get("hasMore"):
            break
        cursor = page.get("cursor")
        if not cursor:
            break
    return notes


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    meetings = manifest.setdefault("meetings", [])
    known = {m.get("meeting_id") for m in meetings if m.get("status") == "exported"}
    known_notes = {m.get("granola_note_id") for m in meetings if m.get("granola_note_id")}
    allowed = public_folders()
    added = 0
    latest = None
    for stub in sorted(list_recent(), key=lambda n: n.get("created_at", "")):
        latest = max(latest or "", stub.get("created_at", ""))
        if stub["id"] in known_notes:
            continue
        try:
            note = api(f"/notes/{stub['id']}?include=transcript")
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 413):
                continue
            raise
        meeting_id = canonical_id(note)
        if meeting_id in known:
            continue
        project, folder_ids = choose_project(note, allowed)
        if project is None:
            continue
        date_value = ((note.get("calendar_event") or {}).get("scheduled_start_time") or note.get("created_at", ""))
        date = dt.datetime.fromisoformat(date_value.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d__%H-%M")
        title = safe_name(note.get("title") or "Без названия")
        rel = Path(project) / f"{date}__{title}__{meeting_id}.md"
        target = ARCHIVE / rel
        if target.exists() and target.stat().st_size:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        content = render(note, meeting_id, project, folder_ids)
        if not transcript_text(note).strip():
            continue
        target.write_text(content, encoding="utf-8")
        meetings.append({
            "meeting_id": meeting_id, "granola_note_id": note["id"],
            "title": note.get("title"), "date": date_value, "project": project,
            "granola_folder_ids": folder_ids, "path": str(rel),
            "source": note.get("web_url", ""), "status": "exported",
            "exported_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "conflict": None, "error": None,
        })
        known.add(meeting_id)
        known_notes.add(note["id"])
        added += 1
    manifest["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    summary = manifest.setdefault("summary", {})
    summary["found"] = len(meetings)
    summary["exported"] = sum(m.get("status") == "exported" for m in meetings)
    summary["unassigned"] = sum(m.get("project") == "_Неразобранное" for m in meetings)
    summary["errors"] = sum(m.get("status") == "error" for m in meetings)
    atomic_json(MANIFEST, manifest)
    if latest:
        # Five-minute overlap protects against delayed visibility and equal timestamps.
        cursor = dt.datetime.fromisoformat(latest.replace("Z", "+00:00")) - dt.timedelta(minutes=5)
        cursor_text = cursor.replace(microsecond=0).isoformat().replace("+00:00", "Z")
        atomic_json(STATE, {"cursor_time": cursor_text, "last_run": manifest["updated_at"], "added": added})
    print(json.dumps({"added": added, "exported": manifest["summary"]["exported"]}))


if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        # macOS background access is retried after Full Disk Access is granted.
        pass
