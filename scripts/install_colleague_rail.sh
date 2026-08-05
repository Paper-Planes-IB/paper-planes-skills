#!/bin/zsh
set -euo pipefail

REPO="${PP_SKILLS_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
CONFIG_DIR="${HOME}/.config/paper-planes"
STATE_DIR="${HOME}/.local/state/paper-planes-codex"
PLIST="${HOME}/Library/LaunchAgents/com.paperplanes.codex-skills-update.plist"
LABEL="com.paperplanes.codex-skills-update"

command -v git >/dev/null || { echo "Нужен git" >&2; exit 1; }
command -v gh >/dev/null || { echo "Нужен GitHub CLI: https://cli.github.com" >&2; exit 1; }
command -v python3 >/dev/null || { echo "Нужен Python 3" >&2; exit 1; }
gh auth status >/dev/null
gh repo view Paper-Planes-IB/paper-planes-skills >/dev/null

mkdir -p "$CONFIG_DIR" "$STATE_DIR" "${HOME}/Library/LaunchAgents"
python3 "$REPO/scripts/link_active_skills.py" --repo "$REPO" --adopt-identical || true
python3 "$REPO/scripts/install_skill_routing_memory.py" --repo "$REPO"

ENV_FILE="$CONFIG_DIR/lms.env"
if [[ ! -f "$ENV_FILE" ]]; then
  printf 'LMS API key: '
  read -r LMS_KEY
  printf 'LMS API secret: '
  read -rs LMS_SECRET
  printf '\n'
  umask 077
  {
    printf 'PP_LMS_URL=https://lms.paper-planes.ru\n'
    printf 'PP_LMS_API_KEY=%s\n' "$LMS_KEY"
    printf 'PP_LMS_API_SECRET=%s\n' "$LMS_SECRET"
  } > "$ENV_FILE"
fi
chmod 600 "$ENV_FILE"

cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>${REPO}/scripts/update_colleague_skills.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key><integer>8</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>${STATE_DIR}/launchd.out.log</string>
  <key>StandardErrorPath</key>
  <string>${STATE_DIR}/launchd.err.log</string>
</dict>
</plist>
PLIST
plutil -lint "$PLIST" >/dev/null
launchctl bootout "gui/$(id -u)/${LABEL}" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"

"$REPO/scripts/pp_lms.py" whoami >/dev/null
echo "Готово. Запустите: $REPO/scripts/doctor_colleague_rail.sh"
