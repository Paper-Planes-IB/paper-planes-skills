#!/bin/zsh
set -u

REPO="${PP_SKILLS_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
FAILURES=0

check() {
  local label="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    printf 'OK   %s\n' "$label"
  else
    printf 'FAIL %s\n' "$label"
    FAILURES=$((FAILURES + 1))
  fi
}

check "GitHub CLI авторизован" gh auth status
check "Репозиторий доступен" gh repo view Paper-Planes-IB/paper-planes-skills
check "Рабочая копия без расхождений" git -C "$REPO" diff --quiet
check "Реестр скиллов валиден" python3 "$REPO/scripts/validate_registry.py"
check "Ссылки Codex актуальны" python3 "$REPO/scripts/link_active_skills.py" --repo "$REPO" --strict
check "Память маршрутизации установлена" test -s "${HOME}/.codex/paper-planes-skill-routing.md"
check "Правило маршрутизации подключено" grep -q "PAPER_PLANES_SKILL_ROUTING_START" "${HOME}/.codex/AGENTS.md"
check "LMS отвечает от имени пользователя" "$REPO/scripts/pp_lms.py" whoami

if (( FAILURES > 0 )); then
  printf '\nПроверка не пройдена: %d\n' "$FAILURES"
  exit 1
fi
printf '\nРельса работает. Перезапустите Codex после первой установки.\n'
