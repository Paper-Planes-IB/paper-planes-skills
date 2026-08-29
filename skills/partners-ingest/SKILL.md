---
name: partners-ingest
description: Use when Ilya asks to ingest partner/project updates from shared production sources, common agent/partner exchange folders, Google Drive 4. Производство, or today's project deltas into the Paper Planes Vault routing system.
metadata:
  short-description: Ingest partner/project deltas into Vault
  version: "0.1.0"
  status: draft
  line: 04-production / partner and shared-drive project ingest
  owner: Ilya
  supports_bpm:
    primary: [BPP, ingest, partner_source_radar]
    required_secondary: [BPM-2, BPM-4, BPM-8, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-3, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-9]
  can_consume:
    - project journals, cards, trackers, BPM registries and Storyline-Storyboard files
    - shared production Drive updates and bounded radar outputs
    - MeltPot / partner exchange packets
    - automation memories and daily reports as observability, not primary facts
    - BPM Exchange routing guards and disabled writeback target rules
  can_produce:
    - source-class classification
    - project / partner route proposal
    - no-op, source-check, needs-owner and needs-routing decisions
    - existing-artifact writeback proposal after approval
    - BPM Exchange reconciliation candidates
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-12: Added BPM Exchange capability metadata and explicit consumed/produced route contract."
---

# Partners Ingest

## Purpose

`partners-ingest` turns fresh partner/project signals into routed Vault updates without crawling or over-ingesting unrelated material.

Use it for requests like:

- `partners ingest`
- `ingest от партнеров`
- `забери обновления из общего диска производства`
- `проверь партнёрские / проектные обновления за сегодня`
- `протяни сигналы из 04-производства / MeltPot exchange`

## Time Window

Default manual run window: only files created or modified today in the user's timezone.

Do not scan historical archives unless Ilya explicitly asks for a wider period. If an older file is referenced by today's changed file, read it only as context for the today's delta.

## Source Layers

Check, in this order:

1. Today's changed files in `Vault/10-отделы/04-производство/Проекты`.
2. Today's changed project journals, task trackers, meeting files, raw/processed/source-recovery files, BPM registries, Storyline-Storyboard files, and project cards.
3. Today's changed files under the shared production artifact map: `Общие диски / Paper Planes / 4. Производство`, but only where a Vault project card explicitly maps a project to that Drive folder.
4. Today's changed MeltPot exchange returns and partner update packs when the request touches partner routing.
5. Existing automation memories/logs only to understand what already ran today; do not treat them as canonical project facts by themselves.

## Shared Drive Radar Scope

When Ilya asks for a common agent Google Drive / Shared Drives Paper Planes radar, treat it as a shared-drive observability pass, not a normal Vault project pass.

If `scripts/shared_drive_radar.py` is used, run the required local command first when specified, then verify whether its default roots match the requested drive scope. The script default may only cover `Paper Planes/4. Производство`; when the request names both `Paper Planes` and `PP Shared`, run an additional bounded pass with explicit repeated `--root` arguments for both local mount roots and use that as the scope-completeness check.

For shared-drive radar automations, Daily Note writeback is an observability invariant. Always pass the intended `--daily-note` path unless Ilya explicitly says `только в чате`, `без файлов`, `симуляция без записи`, or `не создавать Daily Note`. If the target Daily Note is missing, create it first from the standard Daily Note skeleton or let `scripts/shared_drive_radar.py` create/update the marked block. Missing Daily Note is a fix-now condition, not a reason to switch to `--no-daily`.

If multiple radar passes write to the same Daily Note, normalize the writeback before finishing: leave one current `## Общий агентский диск — радар обновлений` block that includes the scope-completeness result, and remove duplicate/raw blocks from earlier passes.

When a multi-root bounded run uses `--max-scan-files`, do not assume the rendered result is the union of all requested roots. The scan limit can exhaust on one root and omit meaningful changes from another. If the required scope names both `Paper Planes` and `PP Shared`, keep the mandatory default/local pass, run explicit roots as requested, and, when outputs differ, normalize the Daily Note and final answer as a union with a source-gap note about bounded coverage.

Do not treat `Мой диск/CLAUDE/Vault` as the primary source for this radar. Vault/Daily Note is only the writeback surface unless the user explicitly asks for a Vault pass.

## Association Gate

Ingest a source only when it is clearly associated with a project or partner routing object:

- the path lies inside a known project folder;
- the path is listed in the project card as a Drive/artifact folder;
- the file links to an existing BPM, Storyline-Storyboard, task tracker, meeting, project card, or subpassport;
- the source/frontmatter explicitly names the project, partner, department, or routing package;
- today's automation log says the project file was updated and the file itself confirms the content.

If association is unclear, do not silently ingest. Mark the signal as `needs-routing`, `donor-signal`, `source-check`, or ask Ilya.

## Routing Rules

After reading a valid signal, decide its route:

- `4ka project journal`: project status, project event, source arrival, task movement, blocker, client/project meeting.
- `Storyline-Storyboard`: BPA / All Delivery / Old Delivery signals with `BPM-scope + first meaningful BPM-candidate source`.
- `Матрица BPM — SI`: reusable BPM/SI pattern, SIF cluster, cross-BPM relation, New Delivery donor signal.
- `active project tracker`: owner/action/date/output task or blocker. For РГ1 use `RG1 Project Planning System` with `PP/Codex ingest / needs RG1 reconciliation`; for other contours use only an explicitly active tracker, otherwise keep proposal-only + local trace / sync gap.
- `MeltPot partner update`: significant strategy, 4ka, finance, commercial, or operating architecture signal visible to partners.
- `1/2/5/6/8`: training, content/commercial, process/methodology, code/product, or knowledge-factory downstream.

## Disabled Writeback Targets

As of 2026-07-05, Airtable writeback and `Codex Project Task Inbox` are disabled as working routes for partners-ingest and shared-drive radar.

- Do not create or update Airtable records.
- Do not create or update `Codex Project Task Inbox` rows or packets.
- Do not use `pending_airtable`, `Airtable sync gap`, `Task Inbox packet`, or `Codex Project Task Inbox -> Airtable` as a live route.
- Treat old references to Airtable / Task Inbox in project files, trackers, or memories as historical unless Ilya explicitly re-enables that route in the current task.
- For РГ1 task_delta, write to `RG1 Project Planning System` only after explicit accept, and keep the reconciliation mark.
- For unmatched or non-РГ1 signals without a live tracker, record `proposal-only`, `needs-project-match`, `needs-owner`, or `sync gap: no active tracker`, not Airtable / Task Inbox.

## BPA / New Delivery Rule

For BPA / All Delivery / Old Delivery:

- if `BPM-scope + first meaningful BPM-candidate source` exists, create or update the project `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md`;
- a triggered BPA.08 creation gate is a `missing-required-artifact`, not a proposal waiting for generic file-creation approval.

For New Delivery:

- treat sources as `donor-signal` by default;
- route to `Матрица BPM — SI`, methodology, training, or operating architecture;
- do not create a project BPA Storyline-Storyboard unless a separate BPA / All Delivery slide-based contour is explicitly carved out.

## Output

Report briefly:

1. Today's window checked.
2. Signals found.
3. What was ingested / updated.
4. What was marked `needs-routing`, `donor-signal`, or `source-check`.
5. What partner-visible updates should be sent through MeltPot.

Do not overclaim: if only logs were checked and no source file was updated, say so.

## Writeback / Approval Gate

This skill is high-risk because it can ingest partner/project deltas into Vault, production maps, project cards, BPA/New Delivery artifacts, partner-visible updates, and task candidates.

Before any durable update, show Ilya the source signal, affected project/partner contour, target file(s), proposed diff or update summary, and whether the action is `source-check`, `needs-routing`, `donor-signal`, `candidate`, or accepted writeback. Do not silently create/update project files, BPA artifacts, active trackers, partner messages, or tasks unless Ilya explicitly approved that exact action or an active project rule requires that exact artifact and the scope is unambiguous. Airtable and `Codex Project Task Inbox` are not active trackers unless Ilya separately re-enables them.

## Structured Analytical Artifact Ingest Gate

Partner sources that change a Problem Map, analytical tree, classification, evidence/claim matrix, Mermaid, storyline-storyboard, metric tree, or dimension architecture inherit the global contract in `~/.codex/AGENTS.md`. Preserve partner source, physical locator, rights, methodology source, inference, and receiver artifact as separate fields. The source lands as delta/no-op in the existing artifact; partner wording, Frappe/Quartz, or a donor method cannot become client fact or PP canon without the applicable gate.
