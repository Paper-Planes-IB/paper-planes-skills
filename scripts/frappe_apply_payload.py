import json
import re
from pathlib import Path
from datetime import datetime, timezone
import frappe

REGISTRY_NAME = "gcj3niu80m"
WIKI_SPACE = "dvmhriukp4"

def normalized_title(value):
    return re.sub(r"^(agents|codex)__", "", value or "", flags=re.I).casefold().strip()

def main(payload_path="/tmp/skills_publish_payload.json"):
    payload = json.loads(Path(payload_path).read_text(encoding="utf-8"))
    registry = frappe.get_doc("Wiki Document", REGISTRY_NAME)
    existing = frappe.get_all("Wiki Document", filters={"parent_wiki_document": REGISTRY_NAME}, fields=["*"], limit_page_length=1000)
    def unique(field, value, normalized=False):
        matches = [d for d in existing if (normalized_title(d.get(field)) if normalized else d.get(field)) == value]
        if len(matches) > 1:
            raise ValueError(f"Ambiguous Wiki Document match: {field}={value}")
        return matches[0] if matches else None
    plan = []
    for item in payload["pages"]:
        key = f"github:paper-planes-skills:{item['name']}"
        match = unique("doc_key", key) or unique("title", item["name"].casefold(), True) or unique("route", item["route"])
        plan.append((item, match))
    # Persist a readable snapshot before the first write, including published content.
    space = frappe.get_doc("Wiki Space", WIKI_SPACE)
    keys = [d.get("doc_key") for d in existing] + [registry.doc_key]
    revisions = frappe.get_all("Wiki Revision Item", filters={"revision": space.main_revision, "doc_key": ["in", keys]}, fields=["*"], limit_page_length=1000)
    blob_names = list({r.get("content_blob") for r in revisions if r.get("content_blob")})
    blobs = frappe.get_all("Wiki Content Blob", filters={"name": ["in", blob_names]}, fields=["*"], limit_page_length=1000) if blob_names else []
    snapshot = json.dumps({"registry": registry.as_dict(), "documents": existing, "space": space.as_dict(), "revision_items": revisions, "blobs": blobs}, ensure_ascii=False, indent=2, default=str)
    directory = Path(frappe.get_site_path("private", "backups", "skills-sync"))
    directory.mkdir(parents=True, exist_ok=True)
    backup = directory / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    backup.write_text(snapshot, encoding="utf-8")
    assert backup.read_text(encoding="utf-8") == snapshot
    created, updated, unchanged = [], [], []
    # Wiki supports suppressing per-document revision rebuilds during bulk changes.
    from wiki.api.wiki_space import _sync_main_revision_for_space
    registry_changed = registry.content != payload["registry_content"] or registry.is_published != 1
    previous_guard = frappe.flags.in_reorder_wiki_documents
    frappe.flags.in_reorder_wiki_documents = True
    try:
        for item, match in plan:
            fields = {"title": item["name"], "content": item["content"], "meta_title": item["name"], "meta_description": item["description"], "is_published": 1, "source_path": f"github:Paper-Planes-IB/paper-planes-skills/skills/{item['name']}/SKILL.md"}
            if match:
                doc = frappe.get_doc("Wiki Document", match["name"])
                if all(doc.get(k) == v for k, v in fields.items()):
                    unchanged.append(doc.name)
                    continue
                updated.append(doc.name)
            else:
                doc = frappe.new_doc("Wiki Document")
                doc.update({"parent_wiki_document": REGISTRY_NAME, "wiki_space": WIKI_SPACE, "route": item["route"], "slug": item["route"].split("/")[-1], "doc_key": f"github:paper-planes-skills:{item['name']}", "is_group": 0, "is_external_link": 0})
                created.append(item["name"])
            doc.update(fields)
            doc.save(ignore_permissions=True)
            live = frappe.get_doc("Wiki Document", doc.name)
            assert all(live.get(k) == v for k, v in fields.items()), item["name"]
        if registry_changed:
            registry.content = payload["registry_content"]
            registry.is_published = 1
            registry.save(ignore_permissions=True)
    finally:
        frappe.flags.in_reorder_wiki_documents = previous_guard
    if created or updated or registry_changed:
        _sync_main_revision_for_space(WIKI_SPACE)
    frappe.db.commit()
    frappe.clear_cache()
    result = {"registry": REGISTRY_NAME, "created": created, "updated": updated, "unchanged": unchanged, "backup": str(backup)}
    print(json.dumps(result, ensure_ascii=False))
    return result
