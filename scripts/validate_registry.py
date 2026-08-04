#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    manifest = json.loads((ROOT / "registry" / "manifest.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "registry" / "catalog.json").read_text(encoding="utf-8"))
    errors = list(manifest.get("validation_errors", []))
    names = set()
    pages = set()
    for item in catalog:
        folded = item["skill"].casefold()
        if folded in names:
            errors.append({"skill": item["skill"], "issues": ["duplicate skill name"]})
        names.add(folded)
        if item["page"] in pages:
            errors.append({"skill": item["skill"], "issues": ["duplicate Wiki page"]})
        pages.add(item["page"])
        description = item.get("description", "")
        sentences = [
            part for part in re.split(r"(?<=[.!?])\s+(?=[А-ЯЁ])", description) if part.strip()
        ]
        if not re.search(r"[А-Яа-яЁё]", description):
            errors.append({"skill": item["skill"], "issues": ["description is not Russian"]})
        if not 2 <= len(sentences) <= 3:
            errors.append({"skill": item["skill"], "issues": ["description must contain 2-3 sentences"]})
    print(json.dumps({"errors": errors, "catalog": len(catalog)}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
