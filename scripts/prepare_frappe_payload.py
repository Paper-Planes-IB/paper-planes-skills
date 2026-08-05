#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re

from pp_lms import upsert_markdown_section


ROOT = pathlib.Path(__file__).resolve().parents[1]


def page_content(item: dict) -> str:
    skill_md = ROOT / "skills" / item["skill"] / "SKILL.md"
    raw = skill_md.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.S)
    status = "Архивный" if item.get("lifecycle") == "legacy" else "Актуальный"
    return f"""# {item['skill']}

Расположение: [3. Я — консультант](/knowledge/3-я-консультант) / [Большой реестр скиллов](/knowledge/bolshoy-reestr-skillov) / {item['skill']}

## Что делает

{item['description']}

**Статус:** {status}  
**Полный пакет:** [открыть в GitHub]({item['github']})

## Инструкция

{raw.strip()}
"""


def main() -> None:
    catalog = json.loads((ROOT / "registry" / "catalog.json").read_text(encoding="utf-8"))
    template = (ROOT / "registry" / "registry_template.md").read_text(encoding="utf-8")
    registry_heading = "# Большой реестр скиллов"
    duplicate_at = template.find(registry_heading, len(registry_heading))
    if duplicate_at != -1:
        template = template[:duplicate_at].rstrip() + "\n"
    install_section_path = ROOT / "onboarding" / "wiki-install-section.md"
    if install_section_path.exists():
        template = upsert_markdown_section(
            template,
            install_section_path.read_text(encoding="utf-8"),
        )
    counts = {}
    for item in catalog:
        counts[item["type"]] = counts.get(item["type"], 0) + 1
    linked = sum(bool(item.get("github")) for item in catalog)
    template = re.sub(
        r"Всего скиллов: \*\*\d+\*\*\. Связано с GitHub: \*\*\d+\*\*\.",
        f"Всего скиллов: **{len(catalog)}**. Связано с GitHub: **{linked}**.",
        template,
    )
    data_json = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    counts_json = json.dumps(counts, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = re.sub(
        r'<script type="application/json" id="sr-data">.*?</script>',
        f'<script type="application/json" id="sr-data">{data_json}</script>',
        template,
        flags=re.S,
    )
    template = re.sub(
        r'<script type="application/json" id="sr-counts">.*?</script>',
        f'<script type="application/json" id="sr-counts">{counts_json}</script>',
        template,
        flags=re.S,
    )
    repository_names = {
        record["name"].casefold()
        for record in json.loads((ROOT / "registry" / "manifest.json").read_text(encoding="utf-8"))["skills"]
    }
    pages = [
        {
            "name": item["skill"],
            "route": item["page"].split("lms.paper-planes.ru/", 1)[-1].lstrip("/"),
            "description": item["description"],
            "github": item["github"],
            "lifecycle": item.get("lifecycle", "active"),
            "content": page_content(item),
        }
        for item in catalog
        if item["skill"].casefold() in repository_names
    ]
    payload = {"registry_content": template, "catalog": catalog, "pages": pages}
    target = ROOT / "registry" / "frappe_payload.json"
    target.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"catalog": len(catalog), "pages": len(pages)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
