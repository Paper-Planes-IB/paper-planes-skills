#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
from pathlib import Path


START = "<!-- PAPER_PLANES_SKILL_ROUTING_START -->"
END = "<!-- PAPER_PLANES_SKILL_ROUTING_END -->"


def build_routing_index(repo: Path) -> str:
    manifest = json.loads((repo / "registry" / "manifest.json").read_text(encoding="utf-8"))
    catalog = json.loads((repo / "registry" / "catalog.json").read_text(encoding="utf-8"))
    catalog_by_name = {item["skill"].casefold(): item for item in catalog}
    active = [item for item in manifest["skills"] if item["lifecycle"] == "active"]
    legacy = [item for item in manifest["skills"] if item["lifecycle"] == "legacy"]
    groups: dict[str, list[dict]] = {}
    for record in active:
        item = catalog_by_name.get(record["name"].casefold(), {})
        group = item.get("type") or "Общее / без среза"
        groups.setdefault(group, []).append(
            {
                "name": record["name"],
                "description": item.get("description") or "Описание уточняется.",
            }
        )

    lines = [
        "# Маршрутизация по скиллам Paper Planes",
        "",
        "Канон: `https://github.com/Paper-Planes-IB/paper-planes-skills`.",
        f"Активных пакетов: **{len(active)}**. Архивных пакетов: **{len(legacy)}**.",
        "",
        "## Правило обращения",
        "",
        "1. Если пользователь назвал скилл, прочитать его `SKILL.md` полностью и применить в текущем запросе.",
        "2. Если название не указано, выбрать минимальный набор по описанию задачи и прочитать инструкции до действий.",
        "3. При пересечении нескольких скиллов выбрать основной и подключать остальные только для отдельной функции.",
        "4. Неясный или рискованный маршрут сначала вести через чтение и диагностику; запись требует разрешения, предусмотренного задачей и скиллом.",
        "5. Архивный пакет вызывается только по прямому запросу. Его наличие не разрешает автоматически удалять или заменять материалы.",
        "",
    ]
    for group in sorted(groups, key=str.casefold):
        lines.extend([f"## {group}", ""])
        for item in sorted(groups[group], key=lambda value: value["name"].casefold()):
            lines.append(
                f"- **{item['name']}** — {item['description']} "
                f"Файл: `~/.codex/skills/{item['name']}/SKILL.md`."
            )
        lines.append("")
    lines.extend(["## Архив", ""])
    lines.append(
        ", ".join(f"`{item['name']}`" for item in sorted(legacy, key=lambda value: value["name"].casefold()))
        + "."
    )
    lines.append("")
    return "\n".join(lines)


def managed_block(index_path: Path) -> str:
    return "\n".join(
        [
            START,
            "## Маршрутизация по скиллам Paper Planes",
            "",
            f"Подробная карта установлена в `{index_path}`.",
            "Для задач Paper Planes сначала сопоставь запрос с этой картой, затем полностью прочитай `SKILL.md` выбранного пакета.",
            "Прямое название скилла является явным триггером. Без названия выбирай минимальный набор по описанию задачи.",
            "При неоднозначности используй безопасный режим чтения или задай уточняющий вопрос до записи.",
            "Архивные скиллы вызываются только по прямому запросу.",
            "Выбор скилла сам по себе не разрешает публикацию, отправку сообщений, изменение прав, удаление или другую внешнюю запись.",
            END,
        ]
    )


def upsert_block(existing: str, block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if pattern.search(existing):
        return pattern.sub(block, existing, count=1).rstrip() + "\n"
    prefix = existing.rstrip()
    return (prefix + "\n\n" if prefix else "") + block + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Установить память маршрутизации Paper Planes")
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    codex_home = args.codex_home.expanduser()
    codex_home.mkdir(parents=True, exist_ok=True)
    index_path = codex_home / "paper-planes-skill-routing.md"
    agents_path = codex_home / "AGENTS.md"
    routing = build_routing_index(repo)
    index_path.write_text(routing, encoding="utf-8")

    existing = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    updated = upsert_block(existing, managed_block(index_path))
    changed = updated != existing
    backup_path = None
    if changed and agents_path.exists():
        backup_dir = codex_home / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / f"AGENTS.md.{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        shutil.copy2(agents_path, backup_path)
        os.chmod(backup_path, 0o600)
    if changed:
        agents_path.write_text(updated, encoding="utf-8")
    os.chmod(index_path, 0o600)

    print(
        json.dumps(
            {
                "routing_index": str(index_path),
                "agents_file": str(agents_path),
                "agents_changed": changed,
                "backup": str(backup_path) if backup_path else None,
                "active_skills": routing.count("Файл: `~/.codex/skills/"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
