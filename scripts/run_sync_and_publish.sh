#!/bin/zsh
set -euo pipefail

REPO="/Users/natalie/paper-planes-skills"
LOG_DIR="/Users/natalie/.local/state/paper-planes-skills"
mkdir -p "$LOG_DIR"
cd "$REPO"

git pull --ff-only origin main
python3 scripts/sync_from_ilya_drive.py
python3 scripts/build_registry.py
python3 scripts/validate_registry.py
python3 scripts/link_active_skills.py --repo "$REPO"

if git diff --quiet && [ -z "$(git status --porcelain)" ]; then
  echo "$(date '+%F %T') изменений нет" >> "$LOG_DIR/sync.log"
  exit 0
fi

git add skills registry
git commit -m "Синхронизировать скиллы Ильи $(date '+%F %H:%M')"
git push origin main

if [ -x scripts/publish_to_frappe.sh ]; then
  scripts/publish_to_frappe.sh
fi

echo "$(date '+%F %T') синхронизация завершена" >> "$LOG_DIR/sync.log"
