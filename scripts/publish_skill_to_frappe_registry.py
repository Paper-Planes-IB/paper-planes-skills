#!/usr/bin/env python3
import json
import os
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

from pp_lms import LMSClient


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV = Path.home() / ".config" / "paper-planes" / "lms.env"
ROUTE = os.environ.get("FRAPPE_WIKI_ROUTE", "knowledge/bolshoy-reestr-skillov")
CARD_PATH = Path(os.environ.get(
    "SKILL_KB_CARD",
    str(ROOT / "skills" / "paper-planes-artifact-methodology" / "references" / "kb-card.md"),
))
BACKUP_DIR = Path(os.environ.get(
    "FRAPPE_BACKUP_DIR",
    str(ROOT / "tmp" / "frappe-backups"),
))

MARKER = "<!-- skill:paper-planes-artifact-methodology -->"


def load_lms_env():
    values = {}
    env_path = Path(os.environ.get("PP_LMS_ENV", DEFAULT_ENV)).expanduser()
    if env_path.exists():
        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    for key in ("PP_LMS_URL", "PP_LMS_API_KEY", "PP_LMS_API_SECRET"):
        if os.environ.get(key):
            values[key] = os.environ[key]
    return values


def client():
    return LMSClient(Path(os.environ.get("PP_LMS_ENV", DEFAULT_ENV)).expanduser())


def api_request(method, path, payload=None):
    try:
        return client().request(method, path, payload)
    except RuntimeError as error:
        raise SystemExit(str(error)) from None


def get_registry_doc_name():
    filters = json.dumps([["route", "=", ROUTE]], ensure_ascii=False)
    fields = json.dumps(["name", "title", "route"], ensure_ascii=False)
    query = urllib.parse.urlencode({"filters": filters, "fields": fields})
    result = api_request("GET", f"/api/resource/Wiki%20Document?{query}")
    rows = result.get("data") or []
    if not rows:
        raise SystemExit(f"No Wiki Document found for route={ROUTE!r}")
    return rows[0]["name"]


def choose_content_field(doc):
    candidates = ["content", "body", "description"]
    for field in candidates:
        if field in doc and isinstance(doc.get(field), str):
            return field
    visible = ", ".join(sorted(doc.keys()))
    raise SystemExit(f"Could not find editable text field. Available fields: {visible}")


def append_to_plain_text(current, addition):
    if MARKER in current:
        return current, False
    block = f"\n\n---\n\n{MARKER}\n\n{addition.strip()}\n"
    return current.rstrip() + block, True


def append_to_editorjs(raw, addition):
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return append_to_plain_text(raw, addition)

    blocks = data.get("blocks")
    if not isinstance(blocks, list):
        return append_to_plain_text(raw, addition)

    serialized = json.dumps(data, ensure_ascii=False)
    if MARKER in serialized:
        return raw, False

    data.setdefault("time", int(datetime.now().timestamp() * 1000))
    blocks.extend([
        {"type": "delimiter", "data": {}},
        {"type": "paragraph", "data": {"text": MARKER}},
        {"type": "paragraph", "data": {"text": addition.strip().replace("\n", "<br>")}},
    ])
    return json.dumps(data, ensure_ascii=False), True


def main():
    addition = CARD_PATH.read_text(encoding="utf-8")
    doc_name = get_registry_doc_name()
    encoded_name = urllib.parse.quote(doc_name, safe="")
    doc = api_request("GET", f"/api/resource/Wiki%20Document/{encoded_name}").get("data") or {}

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUP_DIR / f"wiki-document-{doc_name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    backup_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")

    field = choose_content_field(doc)
    current = doc.get(field) or ""
    if current.lstrip().startswith("{"):
        updated, changed = append_to_editorjs(current, addition)
    else:
        updated, changed = append_to_plain_text(current, addition)

    if not changed:
        print(json.dumps({"status": "already_present", "doc": doc_name, "field": field, "backup": str(backup_path)}, ensure_ascii=False))
        return

    result = api_request("PUT", f"/api/resource/Wiki%20Document/{encoded_name}", {field: updated})
    print(json.dumps({
        "status": "updated",
        "doc": doc_name,
        "field": field,
        "route": ROUTE,
        "backup": str(backup_path),
        "response_keys": sorted((result.get("data") or result).keys()),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
