#!/usr/bin/env python3
"""Merge repository skills into the existing Frappe catalog."""

from __future__ import annotations

import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "registry" / "catalog.json"
MANIFEST = ROOT / "registry" / "manifest.json"
OVERRIDES = ROOT / "registry" / "overrides.json"
WIKI_ROUTES = ROOT / "registry" / "wiki_routes.json"
BASE_URL = "https://lms.paper-planes.ru"
GITHUB_BASE = "https://github.com/Paper-Planes-IB/paper-planes-skills/tree/main/skills"
ALIASES = {"consulting-slides": "consulting-slides-creator"}


def slugify(value: str) -> str:
    value = value.casefold().replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-zа-яё0-9-]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def classify(name: str, text: str) -> str:
    hay = f"{name} {text}".casefold()
    if name.casefold() == "text-deai-editor":
        return "AI Text Editor"
    groups = [
        ("BPM / методология", ("bpm", "bpv", "market", "economics", "survey-dashboard", "datalens", "sector-service", "demand-supply")),
        ("Управление проектами", ("project", "clickup", "basecamp", "meeting", "handoff", "admin", "rail", "cord", "commercial-proposal", "rsvp")),
        ("Контент и редактура", ("content", "editor", "article", "longread", "slide", "presentation", "print", "case", "whitepaper", "cover", "voice")),
        ("Внутренние процессы", ("skill", "vault", "ingest", "governance", "graph", "rules", "router", "sync", "research", "heptabase", "tunnel")),
    ]
    for label, markers in groups:
        if any(marker in hay for marker in markers):
            return label
    return "Общее / без среза"


def frontmatter_description(skill_md: pathlib.Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^description:\s*[\"']?(.*?)[\"']?\s*$", text, re.M)
    return match.group(1).strip() if match else ""


def russian_fallback(name: str, source_description: str) -> str:
    readable = name.replace("-", " ").replace("_", " ")
    return (
        f"Скилл помогает выполнить задачу «{readable}» по заданному рабочему процессу. "
        "Он задаёт порядок действий, требования к результату и проверку качества."
    )


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8")) if CATALOG.exists() else []
    catalog = [item for item in catalog if item["skill"].casefold() not in ALIASES]
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    wiki_routes = json.loads(WIKI_ROUTES.read_text(encoding="utf-8")) if WIKI_ROUTES.exists() else {}
    for item in catalog:
        override = overrides.get(item["skill"], {})
        for field in ("type", "description", "slices"):
            if override.get(field):
                item[field] = override[field]
    by_name = {item["skill"].casefold(): item for item in catalog}

    for record in manifest["skills"]:
        name = record["name"]
        skill_md = ROOT / "skills" / name / "SKILL.md"
        source_description = frontmatter_description(skill_md) if skill_md.exists() else ""
        existing = by_name.get(name.casefold(), {})
        override = overrides.get(name, {})
        description = override.get("description") or existing.get("description")
        if not description or not re.search(r"[А-Яа-яЁё]", description):
            description = russian_fallback(name, source_description)
        item = {
            "skill": name,
            "type": override.get("type") or existing.get("type") or classify(name, source_description),
            "description": description.strip(),
            "source": "Илья / GitHub",
            "github": f"{GITHUB_BASE}/{name}",
            "page": existing.get("page") or wiki_routes.get(name.casefold()) or f"{BASE_URL}/knowledge/skill-{slugify(name)}",
            "slices": override.get("slices") or existing.get("slices") or "Без среза",
            "lifecycle": record["lifecycle"],
        }
        by_name[name.casefold()] = item

    merged = sorted(by_name.values(), key=lambda item: (item["type"], item["skill"].casefold()))
    CATALOG.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"catalog": len(merged), "repository_skills": len(manifest["skills"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
