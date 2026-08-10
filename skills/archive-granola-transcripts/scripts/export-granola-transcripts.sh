#!/bin/zsh

set -euo pipefail

SCRIPT_DIR=${0:A:h}
SKILL_DIR=${SCRIPT_DIR:h}
START_DATE=${2:-"2026-01-01"}
END_DATE=${3:-$(date +%F)}

if [[ $# -ge 1 && -n "$1" ]]; then
  ARCHIVE_DIR=$1
else
  candidates=(~/Library/CloudStorage/GoogleDrive-*/Shared\ drives/Paper\ Planes/4.\ Производство/Встречи(N/))
  if (( ${#candidates[@]} != 1 )); then
    print -u2 "Ожидалась одна папка Paper Planes/4. Производство/Встречи, найдено: ${#candidates[@]}"
    exit 2
  fi
  ARCHIVE_DIR=${candidates[1]%/}
fi

if [[ ! -d "$ARCHIVE_DIR" ]]; then
  print -u2 "Папка архива не найдена: $ARCHIVE_DIR"
  exit 2
fi

RUN_DIR="$ARCHIVE_DIR/.runs"
PROMPT_FILE=$(mktemp -t granola-export-prompt.XXXXXX)
LAST_MESSAGE=$(mktemp -t granola-export-result.XXXXXX)

cleanup() {
  rm -f "$PROMPT_FILE" "$LAST_MESSAGE"
}
trap cleanup EXIT

mkdir -p "$RUN_DIR"

GRANOLA_EXPORT_ARCHIVE_DIR="$ARCHIVE_DIR" \
GRANOLA_EXPORT_START_DATE="$START_DATE" \
GRANOLA_EXPORT_END_DATE="$END_DATE" \
perl -pe '
  s/__ARCHIVE_DIR__/$ENV{GRANOLA_EXPORT_ARCHIVE_DIR}/g;
  s/__START_DATE__/$ENV{GRANOLA_EXPORT_START_DATE}/g;
  s/__END_DATE__/$ENV{GRANOLA_EXPORT_END_DATE}/g;
' "$SCRIPT_DIR/export-agent-prompt.md" > "$PROMPT_FILE"

codex exec \
  --skip-git-repo-check \
  --ephemeral \
  --sandbox workspace-write \
  --add-dir "$SKILL_DIR" \
  --cd "$ARCHIVE_DIR" \
  --output-last-message "$LAST_MESSAGE" \
  - < "$PROMPT_FILE"

RUN_STAMP=$(date +%Y%m%d-%H%M%S)
cp "$LAST_MESSAGE" "$RUN_DIR/$RUN_STAMP.txt"
cat "$LAST_MESSAGE"

