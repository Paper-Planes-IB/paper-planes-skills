#!/usr/bin/env python3
from __future__ import annotations

import argparse
import filecmp
import json
import os
import shutil
import datetime as dt
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Подключить активные скиллы Paper Planes к Codex")
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--include-legacy", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--adopt-identical", action="store_true")
    parser.add_argument(
        "--allow-conflicts-file",
        type=Path,
        default=Path.home() / ".config" / "paper-planes" / "allowed-skill-overrides.txt",
    )
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    manifest = json.loads((repo / "registry" / "manifest.json").read_text(encoding="utf-8"))
    target_root = args.codex_home.expanduser() / "skills"
    target_root.mkdir(parents=True, exist_ok=True)
    managed = []
    linked = []
    unchanged = []
    conflicts = []
    adopted = []
    allowed_overrides = []
    allowed_names = set()
    if args.allow_conflicts_file.expanduser().exists():
        allowed_names = {
            line.strip()
            for line in args.allow_conflicts_file.expanduser().read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
    backup_root = args.codex_home.expanduser() / "skills-backup" / dt.datetime.now().strftime("%Y%m%d_%H%M%S")

    def directories_match(left: Path, right: Path) -> bool:
        comparison = filecmp.dircmp(left, right)
        if comparison.left_only or comparison.right_only or comparison.funny_files:
            return False
        for filename in comparison.common_files:
            if not filecmp.cmp(left / filename, right / filename, shallow=False):
                return False
        return all(directories_match(left / name, right / name) for name in comparison.common_dirs)

    for item in manifest["skills"]:
        if item["lifecycle"] == "legacy" and not args.include_legacy:
            continue
        name = item["name"]
        source = repo / "skills" / name
        target = target_root / name
        managed.append(name)
        if target.is_symlink():
            if target.resolve() == source.resolve():
                unchanged.append(name)
                continue
            conflicts.append({"skill": name, "reason": "ссылка ведёт в другое место", "target": str(target)})
            continue
        if target.exists():
            if args.adopt_identical and target.is_dir() and directories_match(source, target):
                backup_root.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(backup_root / name))
                target.symlink_to(source, target_is_directory=True)
                adopted.append(name)
                continue
            if name in allowed_names:
                allowed_overrides.append(name)
                continue
            conflicts.append({"skill": name, "reason": "папка уже существует", "target": str(target)})
            continue
        target.symlink_to(source, target_is_directory=True)
        linked.append(name)

    config_dir = args.codex_home.expanduser().parent / ".config" / "paper-planes"
    config_dir.mkdir(parents=True, exist_ok=True)
    managed_file = config_dir / "managed-skills.txt"
    managed_file.write_text("\n".join(sorted(managed, key=str.casefold)) + "\n", encoding="utf-8")
    os.chmod(managed_file, 0o600)

    result = {
        "active_selected": len(managed),
        "linked": len(linked),
        "already_linked": len(unchanged),
        "adopted_identical": len(adopted),
        "backup": str(backup_root) if adopted else None,
        "preserved_overrides": sorted(allowed_overrides, key=str.casefold),
        "conflicts": conflicts,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if conflicts and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
