#!/usr/bin/env python3
"""Idempotently mirror Ilya's published skills from Google Drive.

The sync is additive: folders missing from the upstream snapshot are kept and
marked as legacy in registry/manifest.json. Nothing is deleted automatically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REGISTRY_DIR = ROOT / "registry"
TOKENS_FILE = pathlib.Path(
    os.environ.get("PP_GDRIVE_TOKENS", "/Users/natalie/.config/mcp-gdrive/tokens.json")
)
SOURCE_FOLDER_ID = os.environ.get(
    "ILYA_SKILLS_FOLDER_ID", "1KRuMs74h_cDfVcKiXL33GcaIVuNabNd-"
)
FOLDER_MIME = "application/vnd.google-apps.folder"
KNOWN_LEGACY = {
    "autoresearch",
    "client-intel-agent",
    "client-project-onboarding",
    "daily-notes-processor",
    "hypothesis-map-builder",
    "km",
    "meeting-report",
    "notion-vault-sync",
    "research-agent",
    "three-perspective-review",
}
RETAINED_ACTIVE = {
    "archive-granola-transcripts",
    "paper-planes-presentation-kit",
}


def http_json(url: str, *, headers=None, data=None) -> dict:
    if data is not None:
        command = [
            "curl", "--http1.1", "--fail", "--silent", "--show-error",
            "--connect-timeout", "10", "--max-time", "60", "--retry", "5",
            "--retry-all-errors",
        ]
        for key, value in (headers or {}).items():
            command.extend(["-H", f"{key}: {value}"])
        command.extend(["-X", "POST", "--data-binary", "@-", url])
        result = subprocess.run(command, input=data, capture_output=True, check=True)
        return json.loads(result.stdout)
    command = [
        "curl", "--http1.1", "--fail", "--silent", "--show-error",
        "--connect-timeout", "10", "--max-time", "60", "--retry", "5",
        "--retry-all-errors", "-K", "-", url,
    ]
    config = "".join(
        f'header = "{key}: {value}"\n' for key, value in (headers or {}).items()
    ).encode()
    result = subprocess.run(command, input=config, capture_output=True, check=True)
    return json.loads(result.stdout)


def access_token() -> str:
    with TOKENS_FILE.open(encoding="utf-8") as handle:
        cfg = json.load(handle)
    payload = urllib.parse.urlencode(
        {
            "client_id": cfg["client_id"],
            "client_secret": cfg["client_secret"],
            "refresh_token": cfg["refresh_token"],
            "grant_type": "refresh_token",
        }
    ).encode()
    response = http_json(
        "https://oauth2.googleapis.com/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
    return response["access_token"]


def list_children(token: str, folder_id: str) -> list[dict]:
    items: list[dict] = []
    page_token = None
    while True:
        query = {
            "q": f"'{folder_id}' in parents and trashed=false",
            "fields": "nextPageToken,files(id,name,mimeType,modifiedTime,md5Checksum,size)",
            "pageSize": "1000",
            "supportsAllDrives": "true",
            "includeItemsFromAllDrives": "true",
        }
        if page_token:
            query["pageToken"] = page_token
        url = "https://www.googleapis.com/drive/v3/files?" + urllib.parse.urlencode(query)
        page = http_json(url, headers={"Authorization": f"Bearer {token}"})
        items.extend(page.get("files", []))
        page_token = page.get("nextPageToken")
        if not page_token:
            return sorted(items, key=lambda item: item["name"].casefold())


def safe_name(name: str) -> str:
    clean = name.replace("/", "_").replace("\x00", "").strip()
    if clean in {"", ".", ".."}:
        raise ValueError(f"Unsafe Drive name: {name!r}")
    return clean


def download(token: str, item: dict, target: pathlib.Path) -> None:
    mime = item["mimeType"]
    if mime.startswith("application/vnd.google-apps."):
        export_map = {
            "application/vnd.google-apps.document": ("text/markdown", ".md"),
            "application/vnd.google-apps.spreadsheet": ("text/csv", ".csv"),
            "application/vnd.google-apps.presentation": ("application/pdf", ".pdf"),
        }
        if mime not in export_map:
            return
        export_mime, suffix = export_map[mime]
        if target.suffix == "":
            target = target.with_suffix(suffix)
        url = (
            f"https://www.googleapis.com/drive/v3/files/{item['id']}/export?"
            + urllib.parse.urlencode({"mimeType": export_mime})
        )
    else:
        url = f"https://www.googleapis.com/drive/v3/files/{item['id']}?alt=media"
    target.parent.mkdir(parents=True, exist_ok=True)
    curl_config = f'header = "Authorization: Bearer {token}"\n'.encode()
    subprocess.run(
        [
            "curl",
            "--http1.1",
            "--fail",
            "--silent",
            "--show-error",
            "--connect-timeout", "10",
            "--max-time", "120",
            "--retry", "5",
            "--retry-all-errors",
            "-K", "-",
            "-o",
            str(target),
            url,
        ],
        input=curl_config,
        check=True,
    )


def fetch_tree(token: str, folder_id: str, target: pathlib.Path, inventory: list[dict]) -> None:
    for item in list_children(token, folder_id):
        name = safe_name(item["name"])
        destination = target / name
        if item["mimeType"] == FOLDER_MIME:
            destination.mkdir(parents=True, exist_ok=True)
            fetch_tree(token, item["id"], destination, inventory)
            continue
        download(token, item, destination)
        inventory.append(
            {
                "drive_id": item["id"],
                "path": str(destination.relative_to(target.parents[0])),
                "mime_type": item["mimeType"],
                "modified_time": item.get("modifiedTime"),
                "drive_md5": item.get("md5Checksum"),
            }
        )


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_skill(path: pathlib.Path) -> list[str]:
    problems = []
    skill_md = path / "SKILL.md"
    if not skill_md.is_file():
        problems.append("missing SKILL.md")
        return problems
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        problems.append("missing YAML frontmatter")
    if "name:" not in text[:2000]:
        problems.append("missing frontmatter name")
    if "description:" not in text[:4000]:
        problems.append("missing frontmatter description")
    secret_markers = ("api_key=", "api-secret=", "bearer ey", "password=")
    for candidate in path.rglob("*"):
        if not candidate.is_file() or candidate.stat().st_size > 5 * 1024 * 1024:
            continue
        try:
            lowered = candidate.read_text(encoding="utf-8").lower()
        except (UnicodeDecodeError, OSError):
            continue
        suspicious_lines = [
            line for line in lowered.splitlines()
            if any(marker in line for marker in secret_markers)
            and not any(safe in line for safe in ("your_key", "placeholder", "example", "<token>", "<password>"))
        ]
        if suspicious_lines:
            problems.append(f"possible embedded secret in {candidate.relative_to(path)}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local-only",
        action="store_true",
        help="Rebuild the manifest from the local mirror without contacting Google Drive.",
    )
    args = parser.parse_args()
    SKILLS_DIR.mkdir(exist_ok=True)
    REGISTRY_DIR.mkdir(exist_ok=True)
    manifest_path = REGISTRY_DIR / "manifest.json"
    previous_manifest = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path.exists()
        else None
    )
    if args.local_only:
        upstream_names = {
            record["name"]
            for record in (previous_manifest or {}).get("skills", [])
            if record.get("source") == "ilya-drive"
        }
    else:
        token = access_token()
        upstream_names = {
            safe_name(item["name"])
            for item in list_children(token, SOURCE_FOLDER_ID)
            if item["mimeType"] == FOLDER_MIME
        }
        with tempfile.TemporaryDirectory(prefix="pp-skills-") as temp_dir:
            snapshot = pathlib.Path(temp_dir) / "skills"
            snapshot.mkdir()
            inventory: list[dict] = []
            fetch_tree(token, SOURCE_FOLDER_ID, snapshot, inventory)
            for skill_name in sorted(upstream_names, key=str.casefold):
                source = snapshot / skill_name
                if not source.is_dir():
                    continue
                destination = SKILLS_DIR / skill_name
                if destination.exists():
                    shutil.copytree(source, destination, dirs_exist_ok=True)
                else:
                    shutil.copytree(source, destination)

    all_names = sorted(
        [path.name for path in SKILLS_DIR.iterdir() if path.is_dir()], key=str.casefold
    )
    records = []
    invalid = []
    warnings = []
    for name in all_names:
        folder = SKILLS_DIR / name
        issues = validate_skill(folder)
        if issues:
            blocking = [issue for issue in issues if issue == "missing SKILL.md" or "secret" in issue]
            advisory = [issue for issue in issues if issue not in blocking]
            if blocking:
                invalid.append({"skill": name, "issues": blocking})
            if advisory:
                warnings.append({"skill": name, "issues": advisory})
        files = []
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                files.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "sha256": sha256(path),
                        "size": path.stat().st_size,
                    }
                )
        records.append(
            {
                "name": name,
                "lifecycle": (
                    "legacy"
                    if name in KNOWN_LEGACY or (name not in upstream_names and name not in RETAINED_ACTIVE)
                    else "active"
                ),
                "source": "ilya-drive" if name in upstream_names else "retained-local",
                "files": files,
            }
        )

    manifest = {
        "schema_version": 1,
        "source_folder_id": SOURCE_FOLDER_ID,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "upstream_skill_count": len(upstream_names),
        "repository_skill_count": len(records),
        "legacy_skill_count": sum(item["lifecycle"] == "legacy" for item in records),
        "skills": records,
        "validation_errors": invalid,
        "validation_warnings": warnings,
    }
    if previous_manifest:
        previous_payload = {key: value for key, value in previous_manifest.items() if key != "generated_at"}
        current_payload = {key: value for key, value in manifest.items() if key != "generated_at"}
        if previous_payload == current_payload:
            manifest["generated_at"] = previous_manifest.get("generated_at", manifest["generated_at"])
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "upstream": len(upstream_names),
                "repository": len(records),
                "legacy": manifest["legacy_skill_count"],
                "invalid": len(invalid),
            },
            ensure_ascii=False,
        )
    )
    return 2 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
