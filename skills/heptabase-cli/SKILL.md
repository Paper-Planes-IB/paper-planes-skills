---
name: heptabase-cli
description: Interact with Heptabase using the CLI to create, read, and edit notes, journals, tags, cards, list whiteboards and manage cards on whiteboards, and browse AI Tutor goals, courses, and lessons. Use when the user asks to manage their Heptabase knowledge base, search cards, work with journals, tags, or whiteboards, or read AI Tutor content.
allowed-tools: Bash(heptabase *) Bash(jq *)
metadata:
  heptabase-cli-version-range: "0.2.x"
---

## Prerequisites

- CLI installed from the desktop app. The command is `heptabase` on macOS/Linux; Windows installs `heptabase.cmd` for cmd/PowerShell and a `heptabase` shim for POSIX shells.
- Check version compatibility before use with `heptabase --version`. If the installed CLI version is outside this skill's compatibility range (`0.2.x`), you MUST stop and ask the user to update either the Heptabase desktop app or this skill package before continuing.

## Command discovery

Run `heptabase help` to see all available top-level commands. This is always up to date. Each command supports `--help` for detailed usage:

```bash
heptabase help
heptabase note --help
heptabase note create --help
```

## Common recipes

Use these as quick recipes for frequent requests. For less common flags or if a command fails, run `heptabase help` or `<command> --help` to discover the correct syntax.

- **Recent cards:** `heptabase card list --sort createdTime --direction descending --limit 20`
- **Today's journal:** `heptabase journal read $(date +%Y-%m-%d)`
- **Search cards by keyword:** `heptabase card list -q "<keyword>" --limit 20`
- **List cards on a whiteboard:** `heptabase whiteboard cards <whiteboardId>`
- **Add a card to a whiteboard:** `heptabase whiteboard add-card --whiteboard-id <whiteboardId> --card-id <cardIdOrDate>`

## All output is JSON

Every command prints JSON to stdout. You can parse it with `jq` or pipe it to other tools.

## Troubleshooting

- **Desktop app must be running.** The CLI communicates with a local server inside the app. If the app is closed, all commands fail. Run `heptabase start` to launch and wait for readiness.
- **Mutations are serialized.** Write operations (create, save, append, trash, restore, tag add/remove, whiteboard add-card/remove-card) run one at a time to prevent conflicts. Reads are concurrent.
- **Request body size limit.** The server rejects request bodies larger than 1 MB.
- **Request timeout.** The server times out requests that take longer than 10 seconds to send their body.

## Known limitations

- **Auto-enabling local server/CLI install not supported.** If the local CLI server is disabled or CLI wiring is missing, the skill cannot repair it by itself; ask the user to enable Local CLI Server and CLI install from desktop settings first.
- **Binary/media upload workflows not supported.** This skill is for JSON/text operations on notes/journals/tags/cards and AI Tutor reads, not file upload or media-processing APIs.
- **Whiteboard creation/edit/delete not supported yet.** You can list whiteboards and add, list, or remove cards on them, but you can't create, rename, move, or delete whiteboards.
- **File reading not supported yet.** You can't read files (e.g., image, video) with `fileId`.
- **PDF card reading not supported yet.** You can't read pdf card or its parsed content.

## Warnings

- **Use the CLI as the only data access path.** Never directly read, write, or modify Heptabase app data through local database files, app storage, cache files, internal endpoints, or any other non-CLI mechanism. If the CLI does not support the requested operation, stop and report that it is not supported.


## Подключаемые нормы из AGENTS — 14.10.2026

Темы: `Heptabase`. Полные исходные формулировки перенесены без пересказа; номера и исходные разделы нужны для проверки. Это не новое разрешение на запись. Последняя прямая команда и действующее ядро имеют приоритет перед старыми примерами. РГ1/РГ2, Task Inbox и снятые маршруты не восстанавливаются по историческому тексту; ClickUp по умолчанию только для чтения. Подключать применимые нормы с условиями и исключениями, не весь файл и не все режимы подряд. Дословный исторический текст хранится для трассировки, а не отменяет более позднее решение. Указатель / проверка: `scripts/model_router.py --instruction-contract "<тема>"` / `--check-instructions` из корня PP.

### С-141. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-141:start -->
16. **Heptabase как visual synthesis layer.** Heptabase / Hepta использовать как визуально-синтетический слой PP OS: карты связей, доски решений, tension maps, board index, AI-context и маршруты между Vault / NotebookLM / Codex / GitHub. Hepta не является master-хранилищем, каноном, архивом raw или заменой Vault / NotebookLM / Codex. В проектных процедурах, Rail-проверках, разворачивании инфраструктуры проекта, поиске проектных следов и восстановлении статуса проекта искать источники только в Vault / Drive / проектных артефактах; Hepta для таких проверок не использовать, если Илья отдельно не попросил именно Hepta. Рабочая структура v2026 живёт под root `PP OS v2026`; legacy-доски считать архивом до явной миграции. Доступ к самой Hepta по умолчанию есть только у Ильи и Дарьи; остальным участникам не проектировать Hepta-access, а готовить внешние output packs: сводки, ссылки, source-pack, вопросы, draft-файлы, решения и каналы обратного сигнала. При работе через CLI помнить ограничение: можно создавать, читать, дополнять и удалять карточки, а также добавлять их на существующие whiteboards, но нельзя создавать / переименовывать / удалять whiteboards и нельзя раскладывать карточки по секциям или координатам. После каждой CLI-загрузки агент обязан сказать Илье, что карточки лежат на canvas, и дать ручную схему раскладки по секциям. Карточки писать retrieval-friendly: стабильное имя, статус, purpose, keywords, when to use, related cards, source / owner, return path. Зрелые решения, правила, методология и определения проходят Return-to-Vault Gate и возвращаются в Vault / GitHub / Codex; в Hepta остаются визуальные связи, гипотезы и навигация.
<!-- agents-norm:С-141:end -->

### С-142. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-142:start -->
17. **Hepta sections = sub-whiteboards.** Когда агент предлагает "секции" для Hepta-доски, по умолчанию считать это предложением создать дочерние whiteboards / sub-whiteboards, а не визуальные зоны на одном canvas. CLI не создаёт sub-whiteboards, поэтому агент должен давать Даше точные названия sub-whiteboards; если они уже созданы, агент добавляет карточки сразу в соответствующие sub-whiteboards. Ручные зоны на одном canvas использовать только для быстрых временных набросков или если Илья явно просит не плодить sub-whiteboards.
<!-- agents-norm:С-142:end -->

### С-143. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-143:start -->
18. **9 рычагов в Hepta = модель, а не внутренний дом PP.** Доску `02 — 9 рычагов PP` и её дочерние доски трактовать как методологическую модель, структуру базы знаний и внешний / клиентский lens Paper Planes, а не как место хранения внутренних операционных контуров компании. Внутренние стратегические, финансовые, культурные и иные рычаги PP могут отображаться на 9 рычагов через связки, карты применения и return routes, но не должны автоматически жить внутри соответствующего рычага модели. Например, внутренние культура, ценности и этические кейсы PP не складываются по умолчанию в `02 — 9 рычагов PP / 8. Культура`; туда можно класть модель, диагностику, методологию и внешнюю структуру знания про культурный рычаг.
<!-- agents-norm:С-143:end -->

### С-144. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-144:start -->
19. **Таксономия Даши для Internal Levers.** В Hepta принята рабочая таксономия Даши: `01 — Strategy 2026-2029` → `Internal Levers` → 9 дочерних досок `Internal Lever 1-9`. Новые карточки, bridge-карточки, landing routes и клиентские / внутренние производные, относящиеся к применению 9 рычагов к стратегии Paper Planes, вносить внутрь соответствующей доски `Internal Lever ...` внутри `Internal Levers`, а не напрямую в `01` и не в модельную доску `02 — 9 рычагов PP`. `01` держать как стратегическую мать и навигацию; `Internal Levers` — как рабочий контейнер применения 9 рычагов к PP. Внутри каждого `Internal Lever ...` дальше раскладывать карточки по sub-sub-whiteboards, а не держать длинный плоский список. Если sub-sub-whiteboards ещё не созданы, агент даёт Даше точные названия и временно оставляет карточки на родительской доске соответствующего рычага; отдельные служебные карточки-памятки под эту таксономию не создавать без необходимости.
<!-- agents-norm:С-144:end -->

### С-145. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-145:start -->
20. **Hepta sensemaking по клиентским КП.** Архивные КП и клиентские материалы не импортировать в Hepta целиком как архив. Hepta должна видеть из них только смысловые landing-карточки: архетип клиента, управленческую развилку, рычаги, reusable assets, противоречия, open questions и return routes. Статус таких карточек по умолчанию `client signal / non-canonical` или `method candidate / non-canonical`: они не становятся каноном без Return-to-Vault Gate. Сырьё и полный текст КП остаются в Vault / коммерческом или проектном контуре; Hepta хранит карту выводов и маршрутов.
<!-- agents-norm:С-145:end -->
