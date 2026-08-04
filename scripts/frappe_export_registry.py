import json
import frappe


def main():
    registry = frappe.get_doc("Wiki Document", "gcj3niu80m").as_dict()
    skill_docs = frappe.get_all(
        "Wiki Document",
        filters=[["Wiki Document", "route", "like", "knowledge/3-я-консультант-реестр-скиллов-и-промптов%"]],
        fields=[
            "name", "title", "route", "slug", "doc_key", "is_published",
            "wiki_space", "is_group", "parent_wiki_document", "sort_order",
            "content", "meta_title", "meta_description", "source_path",
        ],
        order_by="route asc",
        limit_page_length=1000,
    )
    payload = {
        "registry": registry,
        "documents": skill_docs,
        "counts": {"documents": len(skill_docs)},
    }
    print(json.dumps(payload, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
