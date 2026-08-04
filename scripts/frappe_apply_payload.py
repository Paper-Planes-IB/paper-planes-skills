import json
import re
import frappe


REGISTRY_NAME = "gcj3niu80m"
WIKI_SPACE = "dvmhriukp4"


def normalized_title(value):
    value = value or ""
    value = re.sub(r"^(agents|codex)__", "", value, flags=re.I)
    return value.casefold().strip()


def main(payload_path="/tmp/skills_publish_payload.json"):
    with open(payload_path, encoding="utf-8") as handle:
        payload = json.load(handle)

    registry = frappe.get_doc("Wiki Document", REGISTRY_NAME)
    registry.content = payload["registry_content"]
    registry.is_published = 1
    registry.save(ignore_permissions=True)
    frappe.db.commit()

    existing = frappe.get_all(
        "Wiki Document",
        filters={"parent_wiki_document": REGISTRY_NAME},
        fields=["name", "title", "route"],
        limit_page_length=1000,
    )
    by_title = {normalized_title(item["title"]): item for item in existing}
    by_route = {item["route"]: item for item in existing if item.get("route")}
    created = []
    updated = []

    for index, item in enumerate(payload["pages"], start=1):
        match = by_title.get(item["name"].casefold()) or by_route.get(item["route"])
        if match:
            doc = frappe.get_doc("Wiki Document", match["name"])
            updated.append(doc.name)
        else:
            doc = frappe.new_doc("Wiki Document")
            doc.parent_wiki_document = REGISTRY_NAME
            doc.wiki_space = WIKI_SPACE
            doc.route = item["route"]
            doc.slug = item["route"].split("/")[-1]
            doc.doc_key = f"github:paper-planes-skills:{item['name']}"
            doc.is_group = 0
            doc.is_external_link = 0
            created.append(item["name"])

        doc.title = item["name"]
        doc.content = item["content"]
        doc.meta_title = item["name"]
        doc.meta_description = item["description"]
        doc.is_published = 1
        doc.source_path = f"github:Paper-Planes-IB/paper-planes-skills/skills/{item['name']}/SKILL.md"
        doc.save(ignore_permissions=True)
        if index % 10 == 0:
            frappe.db.commit()

    frappe.db.commit()
    frappe.clear_cache()
    result = {"registry": REGISTRY_NAME, "created": created, "updated": updated}
    print(json.dumps(result, ensure_ascii=False))
    return result

