#!/bin/zsh
set -euo pipefail

REPO="${PP_SKILLS_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
STATE_DIR="${HOME}/.local/state/paper-planes-codex"
mkdir -p "$STATE_DIR"

cd "$REPO"
git pull --ff-only origin main
python3 scripts/link_active_skills.py --repo "$REPO"
python3 scripts/install_skill_routing_memory.py --repo "$REPO"
printf '%s обновление завершено\n' "$(date '+%F %T')" >> "$STATE_DIR/update.log"
