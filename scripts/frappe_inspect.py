import json
import frappe


def main():
    standalone = not getattr(frappe.local, "site", None)
    if standalone:
        frappe.init(
            site="lms.178.130.50.200.sslip.io",
            sites_path="/home/frappe/frappe-bench/sites",
        )
        frappe.connect()
    try:
        meta = frappe.get_meta("Wiki Document")
        fields = [
            {"fieldname": field.fieldname, "fieldtype": field.fieldtype}
            for field in meta.fields
        ]
        docs = frappe.get_all(
            "Wiki Document",
            filters=[
                ["Wiki Document", "route", "in", [
                    "knowledge/bolshoy-reestr-skillov",
                    "knowledge/3-я-консультант-реестр-скиллов-и-промптов",
                ]]
            ],
            fields=["name", "title", "route", "slug", "is_published", "parent_wiki_document", "wiki_space"],
        )
        print(json.dumps({"fields": fields, "documents": docs}, ensure_ascii=False))
    finally:
        if standalone:
            frappe.destroy()


if __name__ == "__main__":
    main()
