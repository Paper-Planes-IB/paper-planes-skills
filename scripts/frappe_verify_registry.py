import json
from collections import Counter

import frappe


REGISTRY_NAME = "gcj3niu80m"
RESULT_PATH = "/tmp/frappe_verify_skills.json"


def main():
    registry = frappe.get_doc("Wiki Document", REGISTRY_NAME)
    children = frappe.get_all(
        "Wiki Document",
        filters={"parent_wiki_document": REGISTRY_NAME},
        fields=["name", "title", "route", "is_published", "source_path"],
        limit_page_length=1000,
    )
    title_counts = Counter(item["title"] for item in children)
    result = {
        "registry": {
            "name": registry.name,
            "route": registry.route,
            "is_published": registry.is_published,
            "content_length": len(registry.content or ""),
            "catalog_markers": (registry.content or "").count("# Большой реестр скиллов"),
            "catalog_marker_positions": [
                index
                for index in range(len(registry.content or ""))
                if (registry.content or "").startswith("# Большой реестр скиллов", index)
            ],
        },
        "children": len(children),
        "published_children": sum(bool(item["is_published"]) for item in children),
        "github_sources": sum(
            (item.get("source_path") or "").startswith(
                "github:Paper-Planes-IB/paper-planes-skills/"
            )
            for item in children
        ),
        "duplicates": sorted(
            title for title, count in title_counts.items() if count > 1
        ),
        "new_pages": sorted(
            [{
                "title": item["title"],
                "route": item["route"],
                "is_published": item["is_published"],
            }
            for item in children
            if item["title"]
            in {
                "bpm10-crm",
                "autoresearch",
                "looper-skill-builder",
                "whitepaper-proposal-generator",
                "clickup-mcp-router",
                "cord-pdca",
            }],
            key=lambda item: item["title"],
        ),
    }
    with open(RESULT_PATH, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    return result
