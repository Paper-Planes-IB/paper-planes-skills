---
name: rail
description: >-
  Use when Ilya invokes Rail, /rail, "проверь рельсу", "инспектируй ход
  проекта", "проверь проект по рельсе", "восстанови рельсу", "что с проектом",
  or asks to inspect a 4th-department production project across its chats,
  project artifacts, BPM/BPP scope, statuses, stages, deadlines, tasks, owners,
  and methodology compliance. Rail is only for projects in
  Vault/10-отделы/04-производство/Проекты by default and may run only from a
  main project chat: Штаб проекта or Внутренний PP / проектная сборка. It
  reconstructs the actual project rail from evidence, compares it with the
  current 4ka BPM/BPP methodology, and proposes a repair plan without editing
  until explicit accept. Rail is the project-rail-drift mode of the wider
  fix-rules / rail drift-audit family; use fix-rules instead for local
  chat-rule-drift.
metadata:
  version: "0.3.42"
  status: active
  line: project-rail-drift / 4ka delivery governance
  owner: Ilya
  supports_bpm:
    primary: [BPP, Rail]
    required_secondary: [BPM-1A, BPM-1B, BPM-2, BPM-4, BPM-8, BPM-9, BPM-10, BPM-11]
    optional_secondary: [BPM-3, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-12]
  can_consume: [project cards, chat maps and subpassports, task trackers, BPM registers, BPM Storyline-Storyboard, problem maps / ЦВЗ-slices, BPM-12 Minority Report, rail/status reports]
  can_produce: [rail drift packet, repair proposal, task_delta candidates, project-source no-op reason, dynamic rail reference candidates, problem-map / ЦВЗ repair candidates, cross-BPM next-check responsibility matrix, post-mining source closure, consolidated problem model, Estuarine map and visual, actant-action portfolio, BPM-12 AI/RAG attribution gate, assembly BPA pass]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-28: Added K1-to-K3 depth boundary in 0.3.42: BPM/K1 output is sufficient when it gives source-backed linear BPM slides, slide-intents, evidence rights, and BPM-addressed source debt; synthetic re-interpretation, controlled-wave comparison, OSINT refresh before client render, RDB finalization, and client-ready proof orchestration belong to K3 in BPA.04-BPA.05/BPA.08 unless explicitly assigned earlier by owner."
      - "2026-08-28: Added BPM-addressed technical-debt routing in 0.3.41: checks like CRM win/loss, tenders, КП, SLA, tickets, installed base, contract terms, and controlled mystery are not left as generic storyline/RDB notes; they become technical-debt backlog rows in the responsible BPM with evidence, owner contour, return route, and strengthen/weaken criteria."
      - "2026-08-28: Added RDB assembly placement in 0.3.40: mining collects RDB ingredients only; synthetic RDB is formed in BPA.04-BPA.05 after BPM-SI / Storyline-Storyboard and an accepted client Answer, then checked as proof / quality gate before deliverable materialization."
      - "2026-08-28: Added analytical-node subject requirement in 0.3.39: problem nodes, claims, SI, slide-intents, tasks, and other managerial analytical formulations must show the actor / function / system / owner behind an action predicate; if the subject is not evidenced, write `субъект не установлен / requires source check` instead of hiding it in passive wording."
      - "2026-08-28: Added cross-BPM next-check responsibility matrix in 0.3.38: any material next-check raised by any BPM can create a BPM-addressed required check, optional enrichment, watch item, or no-op for another BPM; this does not auto-include or auto-execute the target BPM, but it creates an explicit evidence responsibility and return route to the originating problem node, SI, storyboard, BPV route, or scope decision."
      - "2026-08-28: Added the BPM-2/BPM-3 full-transcript recovery default in 0.3.37: unless Ilya explicitly authorizes summary-only ingest, Rail must first try to retrieve and process the full transcript from the available physical recorder or Granola fallback; summaries are temporary fallbacks and require `full_transcript_recovery_required` when colleagues report that full transcripts exist."
      - "2026-08-28: Added the Natasha cron / Frappe export synchronization rule in 0.3.36: material Rail version changes, new source-class contracts, or downstream-relevant guardrails must update the single partner-safe operating-architecture fragment consumed by `meltpot-natalia-3h-update-pack`, replacing stale excerpts instead of appending parallel summaries."
      - "2026-08-28: Added BPM-12 / Minority Report AI/RAG attribution gate: every BPM-12 AI/RAG-readiness pass must attribute methodology to CORD-PDCA, skill `cord-pdca`, and domain 6 AI-course standards, separating evidence, inference, source gaps, answerability gaps, management delta, and owner stop/go."
      - "2026-08-28: Split the BPM-1 survey family into BPM-1A consumer surveys and BPM-1B employee surveys; BPM-1B defaults to Checkup, domain 6, with Dmitry Shipulin as responsible owner."
      - "2026-05-26: Added BPM Exchange capability metadata."
      - "2026-06-06: Added economical reuse / method-derivative check without heartbeat dependency."
      - "2026-06-06: Added mandatory donor family/source/alias expansion after MГ Окское Подворье miss."
      - "2026-06-06: Made 4ka archive index the mandatory reuse visibility scaffold."
      - "2026-07-08: Added Problem Map / ЦВЗ-slice as a legitimate rail artifact for non-classical projects without an explicit mining phase."
      - "2026-07-08: Added deleted-track guardrail: historical sources must not resurrect removed projects/tracks."
      - "2026-07-08: Added assembly-mode gate: when a project is clearly in presentation assembly or Ilya confirms assembly, Rail must use the full 10-step BPA assembly process stack."
      - "2026-07-08: Added assembly progress navigator: every Rail assembly pass must show current step N/10, previous passed steps, next step, and a short in-chat summary."
      - "2026-07-08: Added universal assembly challenge subagents for method-heavy deliverables before calculation, slide claims, or client-facing deck assembly."
      - "2026-07-11: Added problem -> Cynefin -> actants -> action -> SI/slide-intent -> BPV route order for assembly and BPV dry-run checks."
      - "2026-07-11: Added Old Delivery project-chat auto-trigger for short rail commands and BPM ingest triage; New Delivery explicitly excluded."
      - "2026-07-11: Added mandatory BPM-addressed multi-source evidence trace for every new BPM ingest and downstream action/SI/BPV outputs."
      - "2026-07-11: Added mandatory Old Delivery project document set for BPM evidence corpus."
      - "2026-07-11: Added macro-idea evidence map, polymorphic actant map, and mandatory 9-action matrix for Old Delivery dry-runs."
      - "2026-07-11: Clarified that Old Delivery dry-runs create/update evidence documents unless explicitly run chat-only."
      - "2026-07-11: Added regression guards for BPM scope ledger, problem-node names/status history, actant type validation, concrete action cells, and concrete donor reuse-check."
      - "2026-07-11: Recorded Ilya's official standing permission to create Old Delivery evidence document-set files and required code+name in actant problem roles."
      - "2026-07-11: Clarified that the 9-action matrix is cumulative across all active problem nodes, not limited to the latest ingest."
      - "2026-07-11: Added mandatory Old Delivery coverage check across problem history, actant map, 9-action matrix, SI/BPV trace, and document writeback paths."
      - "2026-07-11: Added Old Delivery interview prep tracker and appointed-interview brief handoff; Rail must not appoint or manage interview queue."
      - "2026-07-11: Added interview brief -> actual interview -> question coverage audit -> next-question backlog trace; coverage cannot be complete when SI/BPV gaps are only implied."
      - "2026-07-11: Added pre-final 0.1.18 self-audit checklist: exact table schemas, BPM-addressed source trace, visible SI/BPV rows for all P-nodes, and no complete verdict while any regression remains."
      - "2026-07-11: Added node-by-node coverage ledger; grouped rows, ranges, bare P-codes, and self-reported pass are invalid unless each active P-node is visibly covered in every required view."
      - "2026-07-11: Forbid pseudo-ledgers: Actant map and 9-action matrix must be separate checks; delta tables cannot claim cumulative coverage; writeback requires paths/links."
      - "2026-07-11: Promoted Rail to unified 0.2.01: retains all 0.1.x guardrails and adds tabular-source ingest contract for Excel/XLS/XLSX/CSV/table exports; external references are conditional, not mandatory, and tabular audit replaces interview question audit when applicable."
      - "2026-07-11: Promoted unified Rail to 0.2.02 with batch_interview_ingest contract: per-source rights, source isolation, batch synthesis rights, per-source question audits, and delta-only/cumulative coverage separation."
      - "2026-07-11: Hardened unified Rail to 0.2.03: mandatory batch regression guards for per-source rights table, decomposed BPM labels, no collapsed no-signal rows, exact macro/actant/action/question schemas, batch synthesis table, writeback paths, and no generic passed verdict."
      - "2026-07-11: Hardened unified Rail to 0.2.04: exact-schema gate for batch ingest; table presence no longer counts as pass, forbidden verdict aliases are blocked, and source gaps must use allowed batch verdicts."
      - "2026-07-11: Hardened unified Rail to 0.2.05: recovery_plus_new_batch contract; recovered sources and new sources must be separated, recovery rights must be audited, mandatory analytical layers cannot be skipped, and strategic fork findings do not substitute for Rail tables."
      - "2026-07-11: Hardened unified Rail to 0.2.06: single-source follow-up contract for financial/follow-up/dedup ingests after the second source; delta-only still requires exact schemas, source-rights, no collapsed nodes, writeback paths, and allowed single-source verdicts."
      - "2026-07-11: Hardened unified Rail to 0.2.07: mixed_contract_ingest contract for passes combining BPP events, BPM-SI synthesis, BPM Exchange/reuse, reference-source gaps, and no-op market ingest; each class needs rights matrix before conclusions."
      - "2026-07-11: Hardened unified Rail to 0.2.08: BPP event, BPM-SI synthesis, BPM Exchange/reuse, reference gap, and market no-op are standalone source-class contracts as well as possible participants in mixed_contract_ingest."
      - "2026-07-11: Promoted unified Rail to 0.3.01: preserves all 0.1.x and 0.2.x ingest contracts and adds the mandatory post-mining transition: source closure, problem-model consolidation, Cynefin recheck, Estuarine mapping and visualization, 9-action portfolio, SI/BPV routing, and BPA readiness gate."
      - "2026-07-11: Hardened post-mining Rail to 0.3.02: every launch is run-to-blocker; passed gates automatically start the next gate in the same invocation, open forks/nonblocking gaps are not blockers, visuals require an actual attempt plus fallback, and partial returns need blocker evidence and exact failure labels."
      - "2026-07-12: Hardened Gate 2 to 0.3.03: every active P-node and every evidence-supported relevant actant must be visibly represented; full problem-actant coverage and actant inventory ledgers are mandatory, while compressed macro-mechanism views are executive derivatives only."
      - "2026-07-12: Corrected Gate 2 in 0.3.04: the time × energy visual plots actant × change-unit points only; every active P-node remains mandatory in a separate macro-tension-grouped problem-actant coverage ledger with full code, name, linked actants, and relationship mechanism."
      - "2026-07-12: Hardened assembly continuation in 0.3.05: `deferred_by_owner` requires an explicit owner pause; C4/partner review is a downstream review gate, not a reopened BPA.01 gap; superseded historical blocks are non-operational and cannot override later authoritative verdicts."
      - "2026-07-12: Hardened BPA.06 production routing in 0.3.06: physical PPTX creation must hand off to the system Presentations skill using its artifact-tool, render, overflow, montage, and visual-QA contract; PP slidument and consulting-slide skills are mandatory overlays, not substitute generators. Accepted reuse donors must also receive explicit transfer/no-transfer/adaptation and slide routes before materialization."
      - "2026-07-12: Expanded presentation reuse in 0.3.07: distinguish mechanism reuse, specific slide-format reuse, deck-architecture reuse, and visual-template reuse. Slide/deck reuse requires a physical defended reference, version/status and slide IDs; one primary visual reference must be selected before the Presentations skill starts authoring."
      - "2026-07-12: Consolidated the assembly integrity contract in 0.3.08: nine-action absence is a mandatory completeness diagnostic across BPA.03/04/05/07/08/09; presentation reuse and the system Presentations production handoff are hard BPA.05→BPA.06 gates rather than optional guidance."
      - "2026-07-12: Installed the PP Presentation Kit contract in 0.3.09: HTML-first PP visual prototype, global logo, editable/raster decision, text-deAI and Balakhnin voice, system Presentations materialization, PP Pages/local browser inspection, pp-text-critic, pp-slide-critic, and presentation-qa are mandatory; consulting-slides-creator is fallback/reference only."
      - "2026-07-12: Hardened the PP HTML acceptance gate in 0.3.10: browser render and zero overflow prove only technical integrity. PP visual likeness, density, concrete exhibits, Russian audience copy, real global logo, silhouette diversity, and pre-materialization text/voice review are mandatory before editable PPTX permission."
      - "2026-07-12: Closed PP visual-gate loopholes in 0.3.11: CSS skin changes do not prove composition repair; visible copy must be edited at source rather than replaced at runtime; logo and fonts require asset/render verification; PP critic and montage evidence are mandatory before visual-likeness pass."
      - "2026-07-12: Hardened slide reasoning in 0.3.12: every substantive slide must carry a complete Situation -> Complication -> Answer chain, preserve every accepted deliverable objective, use the answer as its action title, and provide a claim-specific exhibit; sparse fact-card listings cannot pass BPA.05, HTML review, PP critics, or presentation QA."
      - "2026-07-12: Added the PP Pages shell contract in 0.3.13: separate slide grammar from the viewing shell; a PP Pages prototype needs governed 16:9 slide screens, a collapsible slide navigator with thumbnails and active-state navigation, stable header/deck context, and functional rather than decorative color semantics. A long scrolling HTML document is not an equivalent PP Pages prototype."
      - "2026-07-12: Restored the canonical Markdown-first assembly contract in 0.3.14 from Notion BPA/SOSTAC and archive evidence: the authoritative pre-render artifact is a production-grade MD deck specification, while HTML, PP Pages and PPTX are downstream render targets. Every slide is dual-classified by SOSTAC information role and structural slide class, traced to SI/GS/library references, and carries SCA, evidence, content, exhibit, assembly and QA fields before rendering."
      - "2026-07-12: Added provenance isolation and full-scope disposition in 0.3.15 after the Elevel dry-run audit: chat/thread claims must be bound to exact thread ID and cwd; BPA.01 must disposition every active macro-tension/objective as core, appendix, separate deliverable, deferred, removed_by_owner or no-op. Later scope additions/revivals automatically reopen every upstream BPA artifact back to the first divergence; mere downstream presence cannot count as scope preservation."
      - "2026-07-12: Canonicalized the Notion BPA/SOSTAC slide classification in 0.3.16: SOSTAC is a multi-value information-role axis; structural classes are technical, normative, reference, consulting and encyclopedic. SI routes to repeatable normative/reference constructions, while consulting slides require a documented normative-proof gap and can become GS/normative only after review and a new SI."
      - "2026-07-12: Added machine-verifiable pre-client presentation gates in 0.3.17 from Natasha Tokaeva's external audit: type rationale before render, exact source labels, consecutive-layout limit, first-five SCQA check, full-deck contact sheet, overflow/whitespace geometry, strict 16:9 screen/print/export tests and golden HTML/reference coverage per main slide type."
      - "2026-07-12: Made Natasha Tokaeva's full production audit binding in 0.3.18: management thought determines the renderer, universal card construction cannot substitute for consulting assembly, every material claim needs a locator-level evidence ledger, source copy must be clean before render, and color semantics must be governed."
      - "2026-07-12: Integrated PP Presentation Kit 2026-07-12 as a mandatory dependency in 0.3.19: canonical MD template, slide taxonomy, visual-style guide, white/ink/coral palette, two-critic workflow and single-source render discipline supersede the previous Elevel paper palette and any optional-kit interpretation."
      - "2026-07-12: Closed routing bypasses in 0.3.20: every process, agent, subagent, skill or subskill that creates, edits, reviews, exports or publishes a Paper Planes deck must enter the same PP Presentation Kit preflight and return a durable kit receipt."
      - "2026-07-12: Registered the now-public GitHub repository as canonical PP Presentation Kit upstream in 0.3.21; installed ZIPs are snapshots and every future kit update must record upstream URL, commit and drift status."
      - "2026-07-19: Added the technological-vs-organizational applicability gate in 0.3.22. An owner-classified technological project must not be forced through Cynefin, Estuarine actants, the 9-action matrix, or organizational BPV routes; it follows a technology rail built around process/data/model/architecture/test/technical-readiness gates."
      - "2026-07-20: Added the New Delivery administrative-foundation preflight in 0.3.23: Rail must check the common project passport, explicit project charter, and all nine administrative-scale components; missing or stale foundations route through the canonical admin skill, and an explicit same-turn passport creation/writeback permission must not be ignored."
      - "2026-08-03: Added explicit Cynefin opt-in in 0.3.24: Rail must not generate Cynefin, Estuarine, actant maps, energy/time visuals, or 9-action matrices unless Ilya explicitly enables Cynefin for that specific project or pass. Without opt-in, use problem/evidence/process/data/SI/BPV routing and mark the disabled layers not_applicable_by_owner."
      - "2026-08-03: Hardened duplicate handling in 0.3.25: physical or byte-level duplication only blocks a new copy and independent-source count. It never permits skipping semantic ingest when the canonical parent content has not yet been read and written into evidence, problem nodes, SI/BPV, project-passport structure, and downstream project documents."
      - "2026-08-03: Added Evidence Separation Ledger / Evidence trace separation contract in 0.3.26: evidence class, verification, cross-source status and use rights must not be collapsed into one status; trace contains only material downstream routes, and absent project passports must remain explicitly unmaterialized."
      - "2026-08-24: Added mandatory ClickUp project-container attribution in 0.3.27: every 4ka Rail preflight must find or re-verify the native project container, record its exact hierarchy and URL, and remain read-only unless Ilya separately approves an exact ClickUp change set."
      - "2026-08-28: Added the BPM-3 client-source exclusion gate in 0.3.28: Cynefin, Estuarine, actant maps, energy/time and 9-action operations apply only to BPM-2 internal organizational evidence. BPM-3 client interviews bypass applicability and opt-in checks entirely and use a client-evidence schema without no-op placeholders."
      - "2026-08-28: Added the interview-registration source contract in 0.3.29: new interviews use the native ClickUp call recorder as primary evidence registration and Granola only as a documented fallback when ClickUp cannot be used; Notion is historical-only and is excluded from current registration and recurring completeness checks."
      - "2026-08-28: Added the BPM-2/BPM-3 interview deviation monitor in 0.3.30: planned person/role/segment coverage is reconciled with ClickUp recordings, documented Granola fallbacks, BPM source registration and evidence writeback; only new or materially changed deviations are escalated to Ilya in the project штаб and to Natalia Tokaeva through an assigned ClickUp comment without mutating project fields."
      - "2026-08-28: Standardized BPM-2/BPM-3 heartbeat topology in 0.3.32: one mandatory heartbeat per physical chat aggregating either or both interview BPMs, never per respondent/source/BPM; a single temporary штаб fallback is allowed only when no physical interview chat exists, and duplicate штаб plus subject-chat monitors are forbidden."
      - "2026-08-28: Added atomic problem-node guardrail in 0.3.33: one problem node represents one independently testable mechanism; macro-tensions may group nodes but cannot replace them with a synthetic multi-mechanism problem."
      - "2026-08-28: Added administrative transformation trace in 0.3.34: material ПЦВЗ/problem/SI/slide/BPV changes must update the Admin Scale journal between Programs and Tasks and carry verified ClickUp attribution without auto-creating hypotheses or tasks."
---

# Rail

## Purpose

Rail inspects a 4th-department production project as an operating system: chats, штаб, working contours, scope, BPM/BPP movement, tasks, deadlines, owners, next actions, and methodology fit.

The goal is not to summarize the project. The goal is to answer:

- what rail the project is supposed to follow;
- what rail it is actually following;
- where the project, chats, BPM/BPP artifacts, tasks, or штаб handoff lag behind;
- what should be repaired, escalated, or explicitly left as-is.

## Relationship To Fix Rules

Rail is not a bigger `fix-rules` pass. It is the `project-rail-drift` mode of the same drift-audit family. In user-facing behavior, treat this as one skill family with two modes: `chat-rule-drift` and `project-rail-drift`.

Use Rail when the unit of analysis is the project operating system:

- project status or phase;
- project chat map and штаб route;
- BPM/BPP movement;
- owners, deadlines, tasks, stage gates;
- cross-chat handoffs;
- methodology fit for a 4th-department project.

Use `fix-rules` instead when the unit of analysis is a local rule violation:

- current chat artifact;
- subpassport or chat map row for this chat;
- local rule compliance;
- skill / automation / hook behavior directly referenced by this chat;
- agent process drift.

If a Rail pass discovers a simple local rule violation, mention it as a local fix candidate. If the user asks to repair it immediately and it is unambiguous, use the `fix-rules` fix mode. If a `fix-rules` pass discovers that the whole project rail is stale, stop the local audit at the boundary and recommend Rail from an allowed main project chat.

If the user's request is ambiguous, ask one short routing question before inspecting broadly: `Это скорее про текущий чат/локальные правила или про рельсу всего проекта?`

Any project status passer or closeout that sees stale status, missing owner, unclear next step, broken handoff, or stage-gate drift should suggest running this `project-rail-drift` mode.

Any project status passer, closeout, deepresearch return-packet, competitor-research return-packet, storyboard review, content/commercial rail pass, or BPM-candidate-source pass that sees candidate slides, SI/SIEF proof groups, BPM-6/7A/7B visuals, battlecards, КП arguments, content angles, or reusable knowledge patterns should also check whether a dynamic rail reference is needed. This is not a new skill. It is a live-reference maintenance function inside existing rail / BPM-SI / Storyline-Storyboard governance.

## Natasha Cron / Frappe Export Synchronization

When Rail receives a material version update, a new source-class contract, a new guardrail that affects partner-visible delivery quality, or a downstream-relevant operating-architecture change, update the single partner-safe fragment consumed by the Natasha cron `meltpot-natalia-3h-update-pack`.

This is a replace-and-refresh rule, not an append-only bulletin:

- identify the canonical Rail changelog item and the smallest partner-safe operational implication;
- update the existing cron prompt fragment or its existing source handoff so the current rule supersedes stale snippets;
- route only delivery-relevant information to the partner exchange / Frappe mirror layer: project launch, delivery quality, economics, speed, risk, reusable assets, BPM/BPA/BPP rail, Storyline-Storyboard, fullkit or QA standards;
- do not expose closed 5-ka / 8-ka internals, client-confidential evidence, raw PЦВЗ, hypotheses, SI rows, or project facts that lack release rights;
- do not create a second mirror, duplicate cron, parallel Frappe text, or one-off summary when an existing fragment can be overwritten;
- if the cron is inactive or Frappe publication is only a mirror, still update the upstream fragment and record `Frappe: зеркало / не источник методологии`;
- if the Rail change is technical-only or irrelevant to partners, record a concise `без партнёрской дельты` no-op in the relevant rule/update trail instead of pushing noise downstream.

## Non-Negotiables

- Scope is 4ka projects only by default: `Vault/10-отделы/04-производство/Проекты/<project>`.
- Every 4ka Rail pass must attribute the local project to its native ClickUp container before broad inspection. Use `clickup-mcp-router` in read-only mode and resolve the exact chain `workspace -> space -> folder -> list -> Project task` plus stable URLs and IDs where those levels exist. Search by the exact project/client name and known aliases; do not infer the container from a nearby sales card, similarly named client, interview task, document, or chat.
- If a ClickUp container is already recorded in the project card, chat map, administrative scale, or another current project-control artifact, re-read and verify that it still exists and that its physical hierarchy matches the recorded project. If no local attribution exists but the native container is found, update an existing canonical project artifact when the current request permits local writeback; otherwise report `local_staging / clickup_container_found` and show the verified hierarchy and URL. If the container cannot be found after exact-name and alias search, report `clickup_sync_gap` and request the project/list/task link; do not create a surrogate container or treat local Markdown trackers as synchronized ClickUp state.
- ClickUp attribution is read-only project identification, not mutation authority. Commands such as `найди проект`, `соатрибутируйся`, `сверься с ClickUp`, `обнови карту`, `протащи по рельсе`, or a generic Rail launch do not authorize changing ClickUp statuses, owners, dates, priorities, fields, descriptions, task types, parents, views, lists, folders, documents, or tasks. Before any ClickUp mutation, show the exact change set `object / URL -> field -> current value -> proposed value -> physical evidence` and obtain a separate explicit approval for that change set; afterwards re-read every changed object.
- Rail may run only in main project chats: `Штаб проекта` or `Внутренний PP / проектная сборка`.
- Do not run Rail from auxiliary/service chats such as data/MIS/economics, interviews/HR, patient path, market/strategy, or other subject working contours.
- If Ilya invokes Rail from an auxiliary/service chat, do not inspect there. Identify the current chat role from the chat map and say the request must be moved or escalated to `Штаб проекта` or `Внутренний PP / проектная сборка`.
- Do not inspect the whole Vault, all departments, or all runtime automations unless Ilya explicitly expands scope.
- Do not create new files unless Ilya explicitly asks for file output or a new artifact. Exception: Ilya has officially granted standing permission for Old Delivery Rail/BPM evidence document-set creation in an existing project folder; this includes `Реестр BPM-источников.md`, `BPM scope ledger`, `Карта проблем.md` / `Карта проблем и Cynefin.md` only when Cynefin is explicitly enabled, `Карта актантов.md` only when Cynefin is explicitly enabled, `Evidence trace — source-to-node matrix.md`, `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md`, `BPV route map.md`, `Interview roster / interview prep tracker.md`, and `Interview briefs.md` / equivalent.
- For every New Delivery project, check the administrative foundation before declaring `new_delivery_logic_required`: one common project passport/project card, an explicit project charter, and all nine administrative-scale components `Цель / Замысел / Политика / Планы / Программы / Задачи / ЦКП / Идеальная картина / Статистики`. The canonical method owner is the `admin` skill; use its `gate-check + conditional normalize` logic rather than treating the administrative scale as a passive source.
- If Ilya explicitly authorizes creation, normalization, or writeback of the project passport / charter / administrative scale in the current request, consume that permission in the same pass: update the existing canonical passport first, or create one canonical root passport only when none exists. Do not stop at `artifact-gap`, ask for the same permission again, or create parallel passport/scale files. A short Rail command without this explicit permission still does not authorize a new New Delivery file.
- Do not edit project artifacts, rules, AGENTS files, BPM/BPP canon, or trackers until after an explicit accept of the repair plan.
- Do not answer from memory when checking methodology. Read the current 4ka BPM/BPP sources and the project's current artifacts.
- Before selecting, designing or interpreting any BPM, keep four layers separate: `цель и решение владельца`, `фактическая онтология`, `границы доказательств источников`, `дизайн исследования`. The mandatory trace is `цель владельца -> решение -> дефицит знания -> требуемое доказательство -> BPM -> дизайн -> допустимый вывод -> обновление решения`. A BPM method, questionnaire item, city, segment, future expansion or source mention is never sufficient on its own to define the main field. If the owner goal or decision is absent, allow only exploratory work and do not finalize quotas, field geography, sample or instrument. BPM-2 may provide early organizational ontology, but it never silently becomes the source of the owner's telos.
- Do not require subpassports for main chats. `Штаб проекта` and `Внутренний PP / проектная сборка` are governed by the chat map and штаб handoff rules; separate subpassport files are required only for track/service working contours.
- Do not demand C2/C4 accept inside chats. Acceptants, StageGate, task trackers, and other BPP artifacts are standard process requirements to check and report as artifact gaps, but Rail must not treat their absence as a chat-local blocker or try to obtain process accept in a service chat.
- Treat agent reports, old chat summaries, and compressed handoffs as snapshots. Before final output, reconcile them with current project files.
- Separate project facts from methodology requirements, interpretation, and proposed repair.
- Before applying the default Old Delivery chain, classify the project task as `technological / organizational / mixed / unknown` from the contract, deliverable, source corpus, and explicit owner instruction. The owner's explicit classification overrides folder naming and generic Rail defaults.
- Cynefin is explicit opt-in for every project and pass. Unless Ilya directly says that Cynefin is used on the named project or in the named analytical pass, do not generate or require Cynefin domains, Estuarine, actant maps, problem-actant coverage, energy/time visuals, or 9-action matrices. Mark those layers `not_applicable_by_owner: cynefin_not_enabled`, not as evidence gaps or Rail failures. This rule supersedes every unconditional Cynefin/Estuarine/actant/action requirement later in this skill. Permission is local to the named project/pass and must not propagate to other projects.
- For a task explicitly classified by Ilya as `technological`, do not require or generate Cynefin domains, Estuarine actants, energy/time maps, the 9-action matrix, organizational problem-actant coverage, or organizational BPV routes. Mark those layers `not_applicable_by_owner: technological_task`, not as missing evidence or Rail failure.
- A technological Rail uses the chain `source rights -> technical objective / decision -> process and data inventory -> data quality and lineage -> calculation/model specification -> architecture and interfaces -> test design / dry run -> technical readiness, risks and acceptance criteria -> implementation roadmap / technical BPV route when genuinely applicable`. Organizational observations may be retained only as delivery constraints (owner, access, decision gate, SLA), not expanded into a Cynefin/Estuarine analysis unless Ilya reclassifies the task as `mixed` or `organizational`.
- For `mixed` tasks, separate the technological and organizational workstreams before synthesis. Without explicit Cynefin opt-in, both streams use problem/evidence/process/data/SI/BPV routing without Cynefin or actants. With explicit opt-in, apply Cynefin/Estuarine/9-actions only to the organizational or adaptive-change part, never to the technical model, data pipeline, calculation, integration, or software architecture itself.
- If Ilya or a current project artifact marks a project, initiative, track, task, or contour as deleted / removed / cancelled, do not resurrect it from older sources, meeting titles, old trackers, synced rows, or storyboard deltas. Preserve old materials only as `historical source`, `former track`, or `economic / evidence layer` inside live contours, and explicitly mark any stale tracker/spreadsheet row as needing correction.

## Default Operation

Use `REVIEW -> PROCESS -> MAKE`.

Default mode is `inspect` unless Ilya asks to reconstruct, repair, or update.

### Old Delivery Auto-Trigger

In a 4ka project chat that is identified by the chat map, passport, project card, or current context as `Old Delivery`, short commands such as `тащи по рельсе`, `протащи по рельсе`, `по рельсе`, `запусти рельсу`, and any explicit BPM ingest automatically invoke the Old Delivery BPM/BPA triage mode. Do not ask Ilya to paste the full starter prompt again.

The default Old Delivery triage order without explicit Cynefin opt-in is:

```text
source / BPM-candidate source
-> problem_node / ПЦВЗ / SCQA
-> evidence / causal and process trace
-> data / lineage / role / decision gates when applicable
-> SI / САИ / slide-intent / storyboard node
-> initiative hypothesis / movement suggestion
-> BPV / sub-BPV / derivative / gate route
```

Only after explicit Cynefin opt-in may Rail insert `Cynefin domain -> Estuarine actants -> problem-actant links -> actant action classes` between the problem and SI layers.

This opt-in can apply only to `BPM-2 — internal employee / organizational interviews` and organizational synthesis grounded in BPM-2. `BPM-3 — client interviews` is excluded by source class regardless of project-level or pass-level opt-in. For BPM-3, Rail must not run an applicability check, assign or recheck a Cynefin domain, build or populate an Estuarine / actant layer, score energy/time, generate a 9-action matrix, or create no-op placeholder rows for any of those layers. The BPM-3 route is `client source rights -> jobs / value / pain / experience / switching / service evidence -> problem / claim delta -> client or operational evidence request -> SI / storyboard / BPV hypothesis when supported`. Its macro-idea table omits the `Cynefin / domain` column. Record the exclusion once in source rights as `excluded_by_source_class: BPM-3_client_interview`; do not materialize it in `Карта актантов.md`.

This 0.3.28 source-class gate overrides every earlier 0.1.x / 0.2.x exact-schema or cumulative-coverage requirement that would otherwise demand Cynefin, polymorphic actant, energy/time, or 9-action sections for a BPM-3 source. Their omission is a correct source-class route, not `not_applicable`, a coverage gap, or a schema failure. Batch, follow-up, recovery, mixed-contract, and post-mining passes must branch on source class before applying those schemas.

In a mixed BPM-2 + BPM-3 corpus, BPM-3 may confirm, weaken, or contradict a client consequence of a BPM-2 organizational problem, but it cannot be an input to Cynefin classification, actant typing or positioning, energy/time scoring, or 9-action design. Those layers require BPM-2-addressed evidence of the internal organizational mechanism.

This auto-trigger is not valid for the analytical/BPM layer of `New Delivery`. Do not inherit the Old Delivery BPM/BPA chain. However, the New Delivery administrative-foundation preflight is mandatory and must run first. Mark `new_delivery_logic_required` only for the missing analytical/delivery logic after checking and, when explicitly authorized, normalizing the passport, charter, and nine-component administrative scale.

If Ilya or the project evidence says `майнинг завершён`, `забор значимых источников завершён`, `закрываем evidence-корпус`, `источников достаточно`, `остановить дальнейший инжест`, or equivalent, do not continue ordinary ingest and do not jump directly to a deck, org structure, target operating model, initiative list, or pilot selection. Automatically switch the same unified Rail to `post_mining_transition` under Rail 0.3.15 and run it continuously to the first real blocker. This transition inherits every source-rights, trace, exact-schema, cumulative-coverage, writeback, and no-overclaim guard from 0.1.x and 0.2.x.

### Multi-Source Interview Trace

When Rail processes a second or later interview / BPM source in a project, it must not output a flat synthesis where later sections hide whether a node came from one source, several sources, a contradiction, or agent inference.

Before downstream sections such as possible actions, SI / slide-intents, initiatives, or BPV routes, build a source register:

```text
bpm_source_id:
BPM:
respondent / role:
date:
source_type:
status: primary / secondary / processed / ai-summary
```

Use human-readable BPM-addressed source labels in every `source_trace`, not only generic IDs. Acceptable labels include `BPM-2 / интервью Речкалова`, `BPM-2 / интервью Афанасьева`, `BPM-4 / расчёт экономики`, `BPM-10 / CRM-срез`, `BPM-6 / desk research return`.

Every problem, Cynefin domain, actant, action class, SI / slide-intent, initiative hypothesis, and BPV / sub-BPV route must carry:

- `source_trace`: BPM-addressed source IDs / labels that support it;
- `cross_source_status`: `single-source / confirmed / extended / contradicted / refined / inferred / needs_source_check`;
- `derived_from`: upstream problem / actant / action / SI node when the item is not directly stated in a source;
- `confidence`: `low / medium / high`;
- `next_evidence_need` when status is not safely confirmed.

Every new ingest of every BPM updates this source register and must be checked against existing nodes. Do not compare only interviews to interviews. A BPM-4 calculation, BPM-10 CRM slice, BPM-6 market return, or BPM-8 process observation can confirm, weaken, contradict, or reclassify a node first raised by BPM-2 interviews.

### Cross-BPM Next-Check Responsibility Matrix 0.3.38

A `next-check` is not just a free-text evidence note. When a problem node, claim, SI, storyboard line, BPV route, or scope gap names or logically implies another BPM as the right verification layer, Rail must materialize a cross-BPM responsibility row.

Minimum schema:

| Origin object | Origin BPM / source trace | Next-check formulation | Target BPM | Responsibility class | Evidence required | Strengthens if | Weakens / contradicts if | Return route | Scope effect | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Rules:

- `Origin object` must be a visible project object: `P-код + название`, claim ID, SI / САИ, storyboard line, BPV route, or BPM scope row.
- `Target BPM` can be any relevant BPM, not only BPM-SI / lake routes. BPM-2 can raise a BPM-4 or BPM-10 check; BPM-3 can raise a BPM-10 / BPM-11 / BPM-4 check; BPM-4 can raise BPM-6 / BPM-7A / BPM-7B checks; BPM-6 can raise BPM-3 / BPM-5A / BPM-7B / BPM-10 checks, when the evidence dependency is explicit.
- `Responsibility class` uses `обязательная проверка / опциональное обогащение / наблюдать / no-op / запрещено по классу источника`.
- A next-check never automatically includes, executes, or canonizes the target BPM. If the target BPM is already included in `BPM scope ledger`, the row becomes execution backlog for that BPM. If the target BPM is deferred, recommended, or absent, the row becomes a scope-decision candidate. If Ilya excluded the BPM, the row may only record `no-op / excluded_by_owner` unless a new strong evidence reason is visible.
- Checks that name concrete technical evidence such as `CRM win/loss`, tender registry, КП / commercial proposals, SLA, tickets, installed base, contract terms, price lists, service records, data lineage, scoring protocol, or controlled mystery wave must not remain as generic Storyline / RDB / slide caveats. Route each item as `technical debt backlog` in the responsible BPM: usually BPM-10 for CRM/funnel/win-loss exports, BPM-11 for entity keys/integrations/lineage, BPM-4 for account economics, contracts, prices and margin, BPM-8 for SLA/tickets/service/process execution, BPM-5A/5C for controlled mystery/prototype checks, BPM-6 for competitor/public-claim refresh. The originating Storyline/RDB row keeps only the return dependency and status.
- This routing does not raise the expected depth of K1 BPM work. K1 / factory BPM output is acceptable when it delivers source-backed linear BPM slides, slide-intents, source rights, caveats, and BPM-addressed source debt. Tasks that require synthetic re-interpretation across BPMs, comparison with a future controlled wave, refreshing OSINT specifically before client render, final RDB/CVP assembly, or client-ready proof orchestration belong to K3 in BPA.04/BPA.05/BPA.08 unless the owner explicitly assigns that synthesis to the BPM phase.
- The row must state what would strengthen, weaken, or contradict the originating object. Do not write generic checks like `проверить рынок` without the decision that will change.
- `Return route` must say where the result writes back: problem node / ПЦВЗ / SCQA, Evidence trace, BPM Storyline-Storyboard, BPV route map, Admin Scale transformation journal, or BPM scope ledger.
- For BPM-3, the Cynefin / Estuarine / 9-action prohibition still applies. A client source may raise cross-BPM evidence checks, but cannot create those organizational layers by itself.
- This matrix generalizes the `interview-brief-by-analogs` carryover logic: old evidence can inject questions into a later interview; likewise any prior BPM can inject checks into a later calculation, market audit, CRM audit, process observation, competitor review, or data lineage audit.

Failure labels:

- `next_check_unrouted` — material next-check exists but has no target BPM and return route;
- `next_check_auto_bpm_overreach` — next-check was treated as automatic target-BPM execution or canonization;
- `next_check_missing_strengthen_weaken_logic` — row lacks explicit strengthen / weaken / contradict criteria;
- `next_check_scope_gate_missing` — target BPM is not included but no scope-decision status is shown;
- `next_check_forbidden_layer_fail` — BPM-3 next-check wrongly creates Cynefin / Estuarine / 9-action work.
- `next_check_technical_debt_unrouted` — concrete CRM / SLA / tenders / КП / ticket / contract / mystery / lineage check remains only as a generic note instead of a BPM-addressed technical-debt backlog row.
- `k1_bpm_depth_overreach` — K1/BPM output is judged incomplete because it lacks K3-level synthetic rethinking, controlled-wave comparison, OSINT refresh before client render, final RDB/CVP, or client-ready proof orchestration, despite having sufficient source-backed linear BPM slides / slide-intents and evidence debt.

### Evidence Separation Ledger / Evidence Trace Separation Contract 0.3.26

`Evidence Separation Ledger` and `Evidence trace` are different evidence-governance artifacts and must not become duplicate tables with different names.

The Evidence Separation Ledger is claim-level. One row is one atomic assertion. Its minimum schema is:

| Claim ID | Atomic claim | Source and locator | Evidence class | Verification status | Cross-source status | Allowed use | Forbidden use | Downstream candidate route | Confidence | Original / superseded status |
|---|---|---|---|---|---|---|---|---|---|---|

Rules:

- `Evidence class` describes what kind of basis exists: signed document, client material, interview statement, external benchmark, analytical synthesis, hypothesis, source gap, governance decision, or another named class.
- `Verification status` describes what was actually checked, independently of the class.
- `Cross-source status` distinguishes single-source, multi-source confirmation, contradiction, refinement, inference, and source-check need.
- `Allowed use` and `Forbidden use` are mandatory claim-rights fields. A downstream route does not itself grant permission to make the claim.
- `Source and locator` must identify the source object and the best available locator: date, respondent/claim ID, page/section, sheet/range/row, meeting block, slide ID, or other stable address. They may share one column only when both remain explicit and parseable.
- A single generic `Status` column that mixes source type, verification, confidence and use restriction is `evidence_separation_status_conflation` and cannot be treated as a normalized Ledger.
- Preserve source-native legacy status only as a compatibility/audit field; it must not govern decisions after normalization.

Evidence trace is route-level. It answers where a material output came from and what it affects. Its minimum routed row is:

| Problem node / output | Claim IDs | BPM-addressed source trace | Cross-source status | What is supported | What is not supported | SI / passport / BPV route | Materialization status | Next evidence / gate |
|---|---|---|---|---|---|---|---|---|

Rules:

- Do not copy every Ledger row into Evidence trace. Include a claim only when it visibly supports a problem node, SI, passport, BPV route, decision, deliverable claim, or explicit evidence gap.
- Claims without a material downstream route remain in the Ledger and their appropriate administrative, contractual, source-register, or assembly home.
- If an SI or passport route is designed but no separate passport artifact exists, write `route_defined / passport_not_materialized` or a Russian-readable equivalent. Never present the route as a completed passport.
- A recommendation, slide object, client Top-5 entry, historic pilot label, or score is not a project passport and does not authorize implementation.
- The trace must preserve negative rights from the Ledger. A route cannot upgrade an interview statement, benchmark, synthesis or hypothesis into a client fact.
- Link Ledger and trace through stable Claim IDs / evidence IDs and BPM-addressed source labels; do not duplicate full claim wording when IDs and a concise support statement suffice.

Failure labels:

- `evidence_separation_status_conflation` — class, verification, cross-source state and use rights remain collapsed in one status field;
- `evidence_trace_ledger_copy` — trace mechanically copies claims without a material downstream route;
- `evidence_trace_rights_upgrade` — a downstream route increases claim strength beyond Ledger rights;
- `passport_route_materialization_overclaim` — a candidate SI/passport route is presented as an existing completed passport;
- `evidence_claim_locator_missing` — a material claim lacks a source object and usable locator.

In `Old Delivery` projects, this evidence corpus must be materialized as project documents, not only summarized in chat. Ilya has officially granted direct standing permission to create the minimal missing document set in the existing project folder. This permission overrides the generic no-new-files guard for this specific Old Delivery evidence set:

- `Реестр BPM-источников.md` — BPM-addressed source register;
- `BPM scope ledger` — included / excluded / deferred / recommended BPM scope;
- `Карта проблем и Cynefin.md` — problem nodes, SCQA / ПЦВЗ links, Cynefin status and status history;
- `Карта актантов.md` — Estuarine actants, problem links, zone / changeability, energy/time drivers;
- `Evidence trace — source-to-node matrix.md` — source-to-problem / source-to-actant / source-to-SI / source-to-BPV matrix;
- `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md` — if not already present under the project analysis contour;
- `BPV route map.md` — BPV / sub-BPV route candidates, source traces, confidence, and next evidence needs.
- `Interview roster / interview prep tracker.md` — known / appointed respondents, role, function, BPM, status, coverage target, brief status;
- `Interview briefs.md` or equivalent — role-specific question briefs produced by `interview-brief-by-analogs`.

If an equivalent existing file already exists, update it instead of creating a duplicate. If the project folder or allowed landing cannot be found, do not create files elsewhere; report `sync gap: Old Delivery document set not created`. Do not cite the generic no-new-files rule as a reason to skip this Old Delivery evidence set. This standing permission does not apply to `New Delivery`.

`Dry-run` does not suppress this writeback in Old Delivery. Treat `драйран`, `прогон`, `протащи по рельсе`, and `тащи по рельсе` as a methodological test with a real project document trace. Skip file creation/update only when Ilya explicitly says `только в чате`, `без файлов`, `симуляция без записи`, or `не создавать документы`, or when the project folder / allowed landing cannot be found.

Every Old Delivery Rail pass that processes a BPM ingest must end with:

```text
document writeback status:
created:
updated:
not_created:
sync_gap:
```

For every created or updated document, include the project contour and path / link, not only the file name. A writeback status without paths is incomplete because it cannot be verified quickly.

Do not write `writeback not performed` merely because the pass is called a dry-run. If writeback did not happen, the status must name the explicit reason.

Before the first substantive Old Delivery Rail/BPM pass, and whenever scope is absent or stale, create or update a BPM scope ledger. Rail must not silently decide which BPM will or will not happen.

Minimum BPM scope ledger:

| BPM | Status | Why in / why out | Source / decision | Owner decision | Next trigger |
|---|---|---|---|---|---|

Allowed statuses: `included / excluded_by_owner / deferred / recommended / candidate / not_applicable / blocked / unknown`. If Rail recommends a BPM, it must be explicit that Ilya can reject it. If Ilya says `этого BPM не будет` or equivalent, mark `excluded_by_owner` and stop recommending it until a new strong evidence trigger appears.

### Old Delivery Interview Prep Tracker

At Old Delivery project initiation, Rail may treat org structure, interview table, стартовый пакет, and respondent lists as interview-prep context, not only as background. It may create or update an interview roster / interview prep tracker in the project folder, but it must not appoint the next interviewee or manage the interview queue as an autonomous owner.

Minimum table:

| Respondent | Role / function / location | Interview BPM | Status | Coverage target | Brief status | Notes |
|---|---|---|---|---|---|---|

Allowed respondent statuses: `known / appointed / scheduled / completed / skipped / replaced / needs_owner_decision / unknown`.

For all new interviews, meeting registration and physical source identity follow this source contract:

1. Primary registrar: the native ClickUp call recorder inside the attributed project container.
2. Fallback registrar: Granola only when ClickUp cannot be used for that meeting. The roster/source row must record the concrete fallback reason.
3. Notion is historical-only. Existing Notion interview pages may be ingested as legacy evidence, but Notion must not register new interviews, define their current completion state, supply the stable identity key, or participate in recurring completeness reconciliation.
4. The stable planned-interview key is `ClickUp project/list ID + respondent key + interview intent`. The physical event key is the ClickUp call/recording ID; for an approved fallback it is the Granola meeting UUID linked back to the ClickUp project and planned respondent.
5. Never register the same physical meeting independently in both systems. If ClickUp and Granola both contain it, choose the primary physical source and record the other as an auxiliary mirror / duplicate trace.

#### BPM-2 / BPM-3 Full Transcript Recovery Default

For BPM-2 and BPM-3 ingest, the default evidence target is the full transcript of the physical meeting, not the shortest available summary. Unless Ilya explicitly says `summary-only`, `только summary`, `не поднимать полный транскрипт`, or gives an equivalent limitation, Rail must first try to retrieve and process the full transcript from the available physical recorder: ClickUp call recorder for new interviews, or a documented Granola fallback / legacy Granola source when that is the accessible recorder.

Granola notes, AI summaries, structured summaries, Notion pages, and short sync notes are temporary fallback evidence, not a completed transcript-level ingest, when a full transcript may exist. If colleagues say that most interviews are in Granola and full transcripts are accessible there, Rail must treat every summary-only BPM-2/BPM-3 row as `full_transcript_recovery_required` until the full transcript is retrieved, access is denied, the transcript is absent, or Ilya explicitly accepts summary-only processing for that source.

Source rows and batch rights tables must distinguish:

| Source status | Meaning | Required next action |
|---|---|---|
| `primary transcript` | full transcript read from the physical recorder | proceed with transcript-level ingest |
| `primary transcript via Granola fallback` | full Granola transcript read because Granola is the available / approved recorder | proceed with transcript-level ingest and keep fallback reason |
| `summary fallback — transcript not yet checked` | only summary/notes are available in the local corpus, and full transcript access has not been tested | set `full_transcript_recovery_required` |
| `summary fallback — transcript inaccessible` | full transcript was attempted but access is denied / missing / technically unavailable | preserve limitation and source-check evidence |
| `summary-only by owner` | Ilya explicitly authorized summary-only use for this source | preserve owner limitation and do not reopen automatically |

Minimum registration fields in the existing interview roster / source register:

| Проектный контейнер ClickUp | Респондент / роль | BPM | Плановый слот / intent | Регистратор | ID физической записи | Причина Granola fallback | Факт встречи | BPM source ID | Время ingest | Статус сверки |
|---|---|---|---|---|---|---|---|---|---|---|

Recurring interview completeness checks compare `planned ClickUp respondent/intent -> ClickUp recording or documented Granola fallback -> BPM source ID -> evidence writeback`. They do not query Notion for current-state registration. A separate one-time legacy recovery pass may inspect Notion, but its results must be migrated into the current register and must not keep Notion as a runtime dependency.

#### BPM-2 / BPM-3 Interview Deviation Monitor

While the interview gate is open, Rail must reconcile both event completeness and planned coverage by person, role, client, and segment. A total interview count never substitutes for the named/role-based BPM-2 plan or the client/segment BPM-3 plan. During the first seven calendar days after project initiation, the reconciliation runs every working day; afterwards it continues every working day until the interview gate is explicitly closed, paused, or superseded by the owner.

Heartbeat creation is a standard project gate, not an ad hoc follow-up request. When BPM-2 or BPM-3 first becomes `included` in an Old Delivery scope, Rail must inspect the project chat map and create or verify exactly one active interview-deviation heartbeat in every physical chat whose subpassport aggregates BPM-2 and/or BPM-3. One chat that aggregates both BPMs receives one combined heartbeat. If the BPMs live in two physical chats, each chat receives one heartbeat for its own scope. Never create a heartbeat per BPM, respondent, client, slot, recording, or source.

If the interview contour exists only logically and no physical subject chat exists, create one temporary combined heartbeat in the main project штаб. Mark it as `штабной fallback: физический интервью-чат отсутствует`. When a physical interview chat is later created, migrate the monitor by creating it there and pausing or deleting the штаб fallback after verifying the new heartbeat; the same scope must never be monitored concurrently from both штаб and subject chat. If a project has no physical chat ID available, record `runtime-missing: target thread not resolved` and resolve it through the chat registry before claiming the gate is complete.

BPM-2 deviation codes:

| Код отклонения | Условие обнаружения | Порог |
|---|---|---|
| `ОТКЛ-БПМ2-01 — Плановый респондент без зарегистрированного слота` | В утверждённом BPM-2 roster есть человек/роль, но в ClickUp нет intent/слота | 3 календарных дня после включения в план, а в первые 7 дней проекта — при каждой дневной сверке |
| `ОТКЛ-БПМ2-02 — Слот прошёл, физическая запись не найдена` | Плановый слот завершён, но нет ClickUp recording ID и нет документированного Granola fallback | более 6 часов |
| `ОТКЛ-БПМ2-03 — Запись есть, BPM source ID отсутствует` | Физическая запись найдена, но не зарегистрирована как BPM-2 source | более 24 часов |
| `ОТКЛ-БПМ2-04 — Evidence writeback отсутствует` | BPM-2 source ID существует, но нет записи результата в evidence-корпусе | более 48 часов |
| `ОТКЛ-БПМ2-05 — Плановая роль или фамилия не покрыта` | Общий числовой план формально достигнут дополнительными интервью, но плановый человек/роль не опрошены | сразу при сверке |
| `ОТКЛ-БПМ2-06 — Fallback не обоснован` | Granola использована без причины невозможности ClickUp или без связи с ClickUp-проектом и плановым респондентом | сразу при обнаружении |
| `ОТКЛ-БПМ2-07 — Один созвон посчитан дважды` | Один physical event независимо учтён как ClickUp- и Granola-источник | сразу при обнаружении |

BPM-3 deviation codes:

| Код отклонения | Условие обнаружения | Порог |
|---|---|---|
| `ОТКЛ-БПМ3-01 — Плановый клиент или сегмент без зарегистрированного слота` | В утверждённом BPM-3 плане есть клиент/сегмент, но в ClickUp нет intent/слота | 3 календарных дня после включения в план, а в первые 7 дней проекта — при каждой дневной сверке |
| `ОТКЛ-БПМ3-02 — Слот прошёл, физическая запись не найдена` | Плановый клиентский слот завершён, но нет ClickUp recording ID и нет документированного Granola fallback | более 6 часов |
| `ОТКЛ-БПМ3-03 — Запись есть, BPM source ID отсутствует` | Физическая запись найдена, но не зарегистрирована как BPM-3 source | более 24 часов |
| `ОТКЛ-БПМ3-04 — Evidence writeback отсутствует` | BPM-3 source ID существует, но jobs/value/pain/experience/switching/service evidence не записан | более 48 часов |
| `ОТКЛ-БПМ3-05 — Заметки подменили число интервью` | Несколько заметок/транскриптов одного physical event посчитаны как несколько клиентских интервью | сразу при сверке |
| `ОТКЛ-БПМ3-06 — Квота клиента или сегмента не покрыта` | Общий числовой план достигнут, но утверждённая клиентская/сегментная квота не закрыта | сразу при сверке |
| `ОТКЛ-БПМ3-07 — Fallback или дубль не нормализован` | Granola fallback не обоснован/не связан с ClickUp либо один physical event посчитан дважды | сразу при обнаружении |

Each alert packet uses the exact schema:

| Код отклонения | Проект | BPM | Респондент / роль или клиент / сегмент | Ожидаемое состояние | Фактическое состояние | Возраст отклонения | Физический источник | BPM source ID | Требуемое действие | Ответственный контур | Дедлайн устранения |
|---|---|---|---|---|---|---|---|---|---|---|---|

Notify only a new deviation or a material change in code, stage, age band, source status, required action, owner contour, or deadline. Use the deduplication fingerprint `СВЕРКА-ИНТЕРВЬЮ:<ClickUp project/list ID>:<BPM>:<respondent/client key>:<deviation code>` and check recent project comments before posting. An unchanged deviation and a clean check produce no external ClickUp comment.

The recurring project monitor reports the packet to Ilya in the project штаб thread. For a real deviation it also creates one assigned ClickUp comment for Natalia Tokaeva in the attributed project root, with `notify_all=false`; this comment-only permission does not authorize changes to status, assignee, deadline, priority, task type, parent, description, custom fields, lists, docs, or any other project entity. Notion is excluded from this runtime monitor.

`Coverage target` names the problem nodes, macro-tensions, BPM scope gaps, actants, SI gaps, or BPV-route uncertainties the respondent can test. If an interview brief is needed but the appointed respondent is not clear, Rail asks Ilya one short question: `к кому готовим следующее интервью?`

When Ilya names an appointed / upcoming respondent, Rail runs or hands off to `interview-brief-by-analogs` before the interview. The brief must draw from:

- current evidence corpus and source-to-node matrix;
- BPM scope ledger and excluded/deferred BPMs;
- macro-idea / tension map;
- active problem-node coverage gaps;
- BPM-SI / Storyline-Storyboard gaps;
- relevant archive analogs and known failure modes.

The brief should be written into `Interview briefs.md` or an equivalent existing project file unless Ilya explicitly requests `только в чате`, `без файлов`, or `симуляция без записи`. This Old Delivery handoff is an exception to the default writeback caution of `interview-brief-by-analogs`; it remains internal and must be marked as an interview brief, not canon.

Minimum next-interview handoff:

| Appointed respondent | Why this interview matters | BPM | Problem nodes / macro-tensions to test | Required injected questions | Archive analogs | Writeback target |
|---|---|---|---|---|---|---|

### Old Delivery Question Coverage Audit

When an interview was prepared from an `Interview briefs.md` / question brief / question block, Rail must run a question coverage audit after ingesting the actual interview. This audit is required even when the interview itself is strong.

Required chain:

```text
interview brief
-> actual interview / transcript / secondary sync
-> question coverage audit
-> next-question backlog
-> next interview brief
```

Before marking interview coverage as complete, Rail must compare the prepared questions with the actual source. Assign stable `question_id` values to the original question intents where possible.

Minimum table:

| question_id | question / intent | target respondent | asked status | answer status | evidence gained | linked P-node / SI | remaining gap | best next respondent | prompt improvement |
|---|---|---|---|---|---|---|---|---|---|

Allowed `asked status`: `asked / not_asked / source_missing / not_applicable`.

Allowed `answer status`: `answered / partial / unanswered / no_answer_expected / source_missing`.

Do not collapse `not_asked` and `unanswered`:

- `not_asked` means the available transcript / secondary source does not show that the question was asked.
- `unanswered` means the question was asked, but the answer did not produce sufficient evidence.
- `source_missing` means the source layer is too weak to determine whether the question was asked or answered.

Each gained answer must link to problem nodes, SI / slide-intents, BPV routes, or explicit evidence gaps. If an unclosed question should move forward, put it into a `next-question backlog` and, when a future respondent is already appointed, suggest that respondent as `best next respondent`. Rail must not appoint a respondent merely to close the backlog.

The audit should be materialized in `Evidence trace — source-to-node matrix.md` or another existing evidence document. If a separate backlog file is not created, record where the backlog rows were written. If no writeback happens, explain the explicit blocker in `document writeback status`.

If there was no prepared brief for the current respondent but a carryover backlog exists from previous interviews, still render the same table. Set `target respondent` to the current respondent or `carryover`, set `asked status` to `not_asked / source_missing / not_applicable` where appropriate, and do not use a two-column `Вопрос / Статус` shortcut. A carryover backlog without `question_id`, `asked status`, `answer status`, `linked P-node / SI`, `remaining gap`, and `prompt improvement` is incomplete.

For human-facing output after multiple interviews, include a compact trace table before or inside sections 6+:

| Node | Layer | Source trace | Cross-source status | Derived from | Confidence | Next evidence |
|---|---|---|---|---|---|---|

If a point is based only on the latest interview, mark `single-source: latest`. If it generalizes across interviews, mark `confirmed` or `extended`. If interviews disagree, mark `contradicted` and keep the contradiction visible rather than averaging it. If Rail proposes an action, SI, initiative, or BPV route as its own synthesis, mark `inferred` and show the upstream nodes it came from.

Problem nodes must always be displayed as `code + name`, e.g. `P10 — Транзакционная модель теряет конкурентоспособность`. Bare codes (`P10`) are not sufficient in human-facing tables, including macro-idea maps, polymorphic actant maps, 9-action matrices, SI tables, and BPV route tables.

Problem node names, claims, SI / slide-intents, task names, and managerial analytical formulations must include a visible subject when the predicate describes action, ownership, transfer, decision, management, measurement, or change. Do not write passive / subjectless forms such as `выполняются`, `управляется`, `согласуется`, `считается`, `теряется`, or `не каскадируется` without answering `кем / чем / у кого`. Use the most precise evidenced subject available: person, role, function, team, process owner, customer, supplier, system, source-of-truth, or explicitly `субъект не установлен / requires source check`. A subjectless node cannot pass problem-map or SI/BPV quality gates unless it is a direct source quote marked as such.

Each problem node must be atomic: one independently testable mechanism with its own actor/process/context, evidence trace, next check and downstream fate. A formulation that joins independent gaps in goals, budget, prioritization, roles, measurement or another mechanism through `и` must be split unless the source proves one shared causal mechanism. Keep the broader synthesis in the macro-tension / SCQA / storyline layer, not as a substitute problem node. When an existing composite node is corrected, preserve it only in status history as `split / deprecated`, route each child separately, and remove the composite node from active SI/BPV paths.

Every ingest that materially changes ПЦВЗ, the problem-node structure or causal mechanism, BPM-SI / САИ, slide-intent, BPV route, or a fundamental hypothesis status must also update the project's existing Admin Scale `Журнал сущностных трансформаций` on the transition `5. Программы -> 6. Задачи`. The row must show `source ingest -> before -> after -> affected code+name nodes / SI / slide intents -> evidence trace -> administrative consequence -> program/task route -> verified ClickUp container/target -> sync status and next decision`. Wording-only edits, formatting, counters, or evidence strengthening without structural change are `без структурной дельты` and do not create a new row. A transformation never auto-creates a task or hypothesis; a native ClickUp `Гипотеза` remains dominant only when the transformed claim is genuinely falsifiable and the exact ClickUp writeback has been approved.

After every new BPM ingest, include problem-node status history:

| Problem node | Previous status | New status | Change type | Source trace | What changed / stayed | Next check |
|---|---|---|---|---|---|---|

Allowed change types: `new / unchanged / confirmed / extended / refined / contradicted / merged / split / deprecated / no_signal`. New problem nodes must not hide what happened to earlier nodes.

Do not collapse this table to `Problem node / current effect`. Do not combine `New status` and `Change type` into values such as `confirmed/refined`; use separate fields. `Source trace` must be BPM-addressed, e.g. `BPM-2 / интервью Ремнёвой`, not only `SRC-08b`, `Ремнёва`, or surname-only labels.

For Old Delivery passes after the second ingest, the problem-node history must include every active problem node accumulated so far. If a node is not affected by the current ingest, show `no_signal` or `unchanged`, not omission.

Modes:

- `inspect`: current rail status and blockers.
- `reconstruct`: reverse-engineer the actual project rail from all project chats and artifacts.
- `methodology-check`: compare actual movement with current 4ka BPM/BPP methodology.
- `repair-plan`: propose exact fixes, but do not edit before accept.
- `post-mining-transition`: after mining closure, run source closure, problem consolidation, Cynefin recheck, Estuarine map/visual, action/SI/BPV trace, and BPA readiness.
- `after-accept`: patch existing files only within the accepted scope and verify.

Standard 4ka artifact checks:

- common project passport / project card as the single headquarters source of truth;
- explicit project charter covering purpose, boundaries, governance, decision routing, and operating principles;
- complete administrative scale: `Цель / Замысел / Политика / Планы / Программы / Задачи / ЦКП / Идеальная картина / Статистики`; for New Delivery, route missing/stale components through `admin` and report its gate result;
- `Админ-шкала/Карта-чатов.md` after chat-map confirmation;
- track/service chat subpassports after track chat creation;
- project task tracker / backlog after chat-map confirmation and chat creation;
- explicit project team clarification: PP roles, client-side штаб / owners, and current responsible people;
- `Админ-шкала/Реестр-BPM.md`;
- `Анализ/BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md` для mining / INIT / PLAN проектов, где уже есть BPM-scope и первый значимый BPM-источник или BPM-candidate source / raw-pack / интервью / орг-встреча / база / reuse / диагональный документ, способные породить будущий слайд;
- `Карта проблем` / ЦВЗ-срез для особых 4ka-проектов без явного mining-этапа, где фактура приходит через инициативы, треки, оргинтервью, статусные созвоны, внешние research-пакеты или клиентские документы. Такая карта является частным видом ЦВЗ: она собирает проблемно-вызовный слой по трекам и должна быть связана с целями, решениями, метриками, владельцами и Storyline/Storyboard, но не обязана порождать задачи сама по себе;
- `Админ-шкала/StageGate-INIT.md`;
- start fact / BPM-impact review where applicable.
- reuse / method-derivative leakage check when the project has enough new evidence, an explicit Rail request, or a pre-defense gate. This check is stateful and economical; it is not a per-update obligation.
- assembly BPA pass when the project is clearly in presentation / deck / slidument / storyline / storyboard / defense assembly, or when Rail asks whether the current work is assembly and Ilya confirms it.
- post-mining transition when mining / meaningful source collection is declared complete: source closure, consolidated problem model, Cynefin recheck, Estuarine table and visual, action portfolio, SI/sub-BPV trace, and BPA readiness gate.

These are process artifacts. Missing items are reported as `artifact-gap` or `process-gap`, not as "chat failed" unless the current chat itself is the required artifact's home.

Team clarification is mandatory in every Rail pass. If the project team is absent, partial, or stale, report it even when all other artifacts look fine.

## Assembly Mode / BPA Pass

When the current project is obviously in assembly, Rail must not stay at generic project-status inspection. Assembly means the work is currently moving a client-facing or internal decision deliverable forward: presentation, deck, slidument, storyboard, storyline, slide brief, appendix, defense package, client meeting deck, or pre-defense materials.

If assembly is likely but not certain, Rail asks one short routing question: `Это сейчас сборка презентации / deliverable через BPA-ассемблинг?` If Ilya confirms, set `assembly_mode: yes` and run the BPA pass.

If assembly mode is active, Rail must use the current BPA assembly canon as the operating rail. Primary source home:

`Vault/10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPA — Ассемблинг/`

Use the current files in that folder as source of truth. If the folder cannot be found, say `BPA source gap` and use this fallback order without inventing a different process:

| BPA | Process | Rail check |
|---|---|---|
| `BPA.01` | фиксация deliverable-пакета | What exactly is being assembled, for whom, for what decision, by what date, with what output package. |
| `BPA.02` | BPM-SI Storyline Control Card | Whether the accepted SI / storyline control card exists and governs the deck. |
| `BPA.03` | BPM Storyline-Storyboard | Whether sources, BPM increments, slide hypotheses, evidence gaps, and no-op reasons are maintained. |
| `BPA.04` | смысловая сборка клиентского ответа | Whether the argument logic, ПЦВЗ / SCQA analogue, claims, proof groups, and narrative spine are coherent. |
| `BPA.05` | слайдовый бриф перед сборкой | Whether the pre-assembly slide brief exists: method axis, coding membrane, evidence rights, organizational filter, КПО / service-blueprint links when relevant. |
| `BPA.06` | сборка основного deliverable | Whether the main deck / slidument exists, is current, and follows the accepted storyline. |
| `BPA.07` | сборка appendix и support-пакета | Whether backup evidence, calculations, interview traces, method notes, and optional slides are assembled. |
| `BPA.08` | multi-perspective review | Whether partner / expert / reader / presentation-QA review has been run or explicitly scheduled. |
| `BPA.09` | защита и фиксация клиентского решения | Whether the defense meeting, decision logic, objections, acceptance criteria, and next client action are prepared. |
| `BPA.10` | harvest методологической единицы | Whether reusable knowledge, method derivative, slide intent, or project learning is harvested after assembly. |

### RDB assembly placement

RDB / CVP / communication formula is not a required final output of mining and must not be produced directly from one BPM source. In mining, Rail records `RDB-ингредиенты`: client jobs / pains / value language, competitive alternatives, peer groups, proof candidates, win/loss, SLA, unit economics, operating feasibility, data lineage and falsifiers.

Synthetic RDB is formed only during assembly, after the project has BPM-SI / project SI, BPM Storyline-Storyboard and an accepted client Answer:

```text
BPM evidence
-> BPM-SI / project SI
-> BPM Storyline-Storyboard
-> BPA.04 смысловая сборка клиентского ответа
-> RDB as proof / quality gate
-> BPA.05 слайдовый бриф перед сборкой
-> BPA.06 основной deliverable
```

Minimum source logic:

| RDB block | Main BPM inputs | Evidence role |
|---|---|---|
| Resonance | BPM-3, BPM-2, BPM-7B | client jobs, value language, channel scenarios, management tension |
| Differentiation | BPM-6, BPM-5A, BPM-7B, BPM-4 | alternatives, peer groups, observed differences, competitive pressure, economic defendability |
| Belief | BPM-4, BPM-8, BPM-10/11, BPM-3 | numbers, operating feasibility, data lineage, SLA/service proof, client confirmation |

If a mining artifact says `собрать RDB`, Rail rewrites the route as `собрать RDB-ингредиенты и передать в BPA.04-BPA.05`. A fast RDB draft is allowed only after explicit owner instruction and must be marked `draft / not client-ready`.

### K1 / K3 depth boundary for BPM-to-BPA transition

Do not make K1 staff or BPM-factory outputs satisfy K3 assembly expectations. BPM phase output is sufficient for handoff when it contains:

- source-backed observations / calculations / interview signals;
- linear BPM slides or slide-intents that state what the source can and cannot prove;
- evidence-rights and caveats;
- BPM-addressed source debt / next-check rows;
- clear return routes to P-node, SI, Storyline-Storyboard, BPM scope ledger, or BPA.

K1 does not need to produce synthetic client-ready interpretation, final RDB/CVP, cross-BPM proof orchestration, controlled-wave comparison, OSINT refresh timed to client rendering, or final deck logic. Those are K3 responsibilities in early assembly:

| Operation | Owner level | BPA home |
|---|---|---|
| decide whether controlled BPM-5A must be rerun before client render | K3 / C3 with C4-partner gate | BPA.04 / BPA.05 / BPA.08 |
| compare BPM-6 claims against a later controlled wave | K3 | BPA.04 / BPA.05 |
| refresh OSINT because the deck is approaching client-ready status | K3 / assembly owner | BPA.05 / BPA.08 |
| finalize RDB / CVP / positioning proof | K3 | BPA.04 -> BPA.05 |
| turn linear BPM slides into narrative spine and production deck spec | K3 | BPA.04 -> BPA.05 -> BPA.06 |

K1 may flag these as `BPA synthesis dependency` or `K3 assembly gate candidate`, but Rail must not mark the BPM phase as incomplete merely because those K3 operations have not yet happened.

For each active assembly pass, output a compact status table:

```text
BPA assembly navigator:
current step: BPA.N / 10 — name
why this is the current step:
already passed:
- BPA.01 — status / one-line summary
- ...
next step: BPA.N+1 — name / what unlocks it
short assembly summary:

BPA assembly pass:
| BPA | status: done / partial / missing / no-op | evidence artifact | gap | next action |
```

The `BPA assembly navigator` is mandatory in every Rail answer where `assembly_mode: yes`, even if the user did not ask for a table. Its purpose is orientation inside the chat: a human reader must immediately understand which of the 10 assembly steps the project is on, how many steps exist in total, which steps are already passed, what the next step is, and what the current assembly state means in plain Russian. Keep the navigator short: 3-7 lines plus the passed-step bullets when useful.

When the current step is uncertain, do not omit the navigator. Write `current step: uncertain, likely BPA.N / 10` and explain what evidence is missing to locate the project precisely.

Rail must distinguish three levels of action:

- `inspect`: diagnose the BPA assembly stack and show gaps.
- `repair-plan`: propose exact file/artifact updates, task deltas, or owner/date corrections.
- `after-accept`: update existing project artifacts and trackers within the accepted scope.

When Ilya says `протащи`, `добей`, `разнеси`, `собери`, `ускорь сборку`, `перед защитой`, or similar in an assembly context, Rail should treat the request as assembly acceleration: use all 10 BPA processes to move the presentation forward, not merely to describe the project state. The approval gate still applies for edits: do not change files until Ilya has accepted the change set, unless the current request itself is an explicit edit/update command.

Assembly continuation guards:

- `deferred_by_owner`, `paused_by_owner`, `later_by_owner_instruction`, or equivalent is allowed only when Ilya or another named decision owner explicitly instructed Rail to pause or defer that BPA step. Silence, an ordinary status check, or the absence of a fresh command is not an owner deferral.
- When the current BPA step has usable input and no real evidence, method, permission, or human-decision blocker, Rail must start the next operation in the same run and report `in_progress`, not manufacture a pause.
- C4 / partner / senior review belongs to the stated downstream review or pre-assembly gate, normally BPA.05 or BPA.08. Its absence must not reopen a completed BPA.01 or appear as a BPA.01 blocker.
- Historical failed or superseded sections may remain for audit trail only when marked `historical_superseded`, `non_operational`, and linked to the later authoritative replacement. A historical verdict, repair request, or failure label must never be read as current project state after the replacement passes.

### BPA.06 presentation-production handoff

When the main deliverable is a PowerPoint or a local slide deck, Rail governs readiness but must not author the PPTX through an improvised script or generic file-writing path.

#### PP Presentation Kit source of truth

The mandatory Paper Planes production contract is derived from `PP_presentation_kit_2026-07-05.zip`, SHA-256 `04554669901a3718fe2db06fa8a4bf3fcf8d8378b05d15f0cefa2eeeb887a91d`. The temporary ZIP path is provenance only. Operational references are the installed durable files:

- `/Users/iliabalahnin/.codex/skills/pp-slidument/SKILL.md`;
- `/Users/iliabalahnin/.codex/skills/pp-slidument/references/pp_pptx_builder_rule.md`;
- `/Users/iliabalahnin/.codex/skills/pp-slidument/agents/pp-text-critic.md`;
- `/Users/iliabalahnin/.codex/skills/pp-slidument/agents/pp-slide-critic.md`;
- `/Users/iliabalahnin/.codex/skills/text-deai-editor/SKILL.md`;
- `/Users/iliabalahnin/.codex/skills/balakhnin-voice/SKILL.md`;
- `/Users/iliabalahnin/.codex/skills/presentation-qa/SKILL.md`;
- `/Users/iliabalahnin/.codex/skills/consulting-slides-creator/SKILL.md` as fallback/reference only.

#### Mandatory PP presentation pipeline

After explicit permission to create the new presentation file, the required sequence is:

1. `pp-slidument` establishes deck mode, action titles, analytical density, left-to-right reading and required functional visuals.
2. Prepare audience-visible Russian copy and run `text-deai-editor` plus `balakhnin-voice` before an HTML prototype may be called PP-ready. Internal codes, production notes, avoidable English terms and anti-AI constructions must not remain in the visible layer.
3. Build an HTML-first prototype from the canonical PP Presentation Kit 2026-07-12: white slide `#FFFFFF`, ink `#181D27`, coral `#FF5850` as the main accent, governed soft status colors, functional tables/charts/matrices/process schemes, consistent 16:9 grid, PT Sans unless an accepted project reference specifies another installed family, and the real Paper Planes logo as a global asset. The former Elevel/PAPER background `#EFEBE7` is superseded. Plain text `PAPER PLANES` is not a logo check.
4. Run the PP visual-likeness and density gate described below. A technically valid generic card grid is not a PP slidument.
5. Inspect the repaired HTML visually. Publish/update through PP Pages when the service and authorization are available; otherwise record `pp_pages_unavailable` and perform an equivalent local browser/render inspection. Silent omission is forbidden.

#### PP Pages shell contract 0.3.13

The HTML prototype has two governed layers that must be audited separately:

1. `PP slide grammar`: the 16:9 slide itself, including title, SCA logic, exhibits, sources, logo and functional visual coding.
2. `PP Pages shell`: the presentation-viewing interface around the slides.

A PP Pages-equivalent shell requires:

- discrete governed 16:9 slide screens rather than one undifferentiated long-scroll document;
- a collapsible slide navigator / sidebar containing the complete ordered slide list and visual thumbnails;
- a visible active-slide state and reliable click/keyboard navigation;
- stable deck title/context in a governed header without duplicating slide titles;
- a focused single-slide viewing mode at normal desktop viewport, while overview/scroll remains secondary;
- responsive behavior that keeps slide, sidebar and controls usable without horizontal overflow;
- shell controls visually separated from slide content so they are never exported into PPTX.

Reference evidence: PP Pages example supplied by Ilya on 2026-07-12, `https://pages.72-56-234-191.sslip.io/xnv72U7y8WAo/`. It demonstrates a sticky deck header, collapsible `Слайды` navigator, ordered thumbnail rail, discrete slide frames and stable Paper Planes mark placement. The example is a shell and composition reference, not permission to copy client content or treat every observed color as canonical.

Color is functional only when it has a named semantic role and remains stable across slides: role, contour, scenario, evidence status, risk, decision state or another explicit class. Unexplained multi-color cards, decorative rainbow accents and per-slide color invention fail. Project/reference-specific palettes must be recorded separately from universal PP shell rules.

#### Canonical Markdown deck-spec contract 0.3.14

PP Pages is a viewing shell, not an assembly method. HTML is a render prototype, not the authoritative content source. Before any HTML, PP Pages or PPTX materialization, BPA.05/BPA.06 must produce or update one existing project Markdown artifact as the canonical `production_md_deck_spec`.

Canonical evidence:

- Notion `BPA. Ассемблинг | Assembling (по SOSTAC)`: SOSTAC information roles, technical/normative/reference/consulting/encyclopedic slide classes, SI/GS and library logic;
- Notion `Обучение по работе с презентациями и слайдами`: deductive/inductive assembly, Minto and three-level slide logic;
- archive `БП модули. Storyboard SCA после QA инвестиционной презентации.md`: action title, slide-level SCA, support numbers and exact sources before Gamma;
- archive `PP Presentation.md`: storyboard fields, visual type and source/risk gates;
- archive presentation repositories and defended decks for GS/library references.

The same MD remains the source of truth through review. Runtime HTML dictionaries, later visual copy edits and PPTX-only content changes are forbidden unless written back to the MD first.

Mandatory deck header:

```yaml
deck_job:
audience:
decision_question:
accepted_objectives:
governing_thought:
deck_scqa:
sostac_sequence:
source_corpus:
confidentiality_boundary:
primary_reference_deck:
slide_library_roots:
render_targets: [html, pp_pages, editable_pptx]
```

Mandatory slide scaffold:

```markdown
## Slide <ID> — <action title>

- objective_route:
- deck_role:
- sostac_roles: [situation_analysis, objectives, strategy, tactics, action_plan, control]
- structural_class: technical|normative|reference|consulting|encyclopedic
- slide_intent_id:
- normative_proof_status: sufficient|insufficient|not_applicable
- consulting_slide_reason:
- GS_reference:
- library_address:
- donor_slide_and_transfer_gate:
- slide_job:
- audience_decision_implication:
- SCA_status:

### SCA
| Situation | Complication | Answer |
|---|---|---|

### Content
- key blocks:
- support numbers / quotes:
- definitions:

### Evidence
- source trace:
- evidence rights:
- caveat / gap:

### Exhibit specification
- visual pattern:
- reading order:
- functional color semantics:
- labels / legend:

### Assembly operations
- Line:
- Grid:
- Master:
- Style:
- Component:
- Proofread:
- Export:

### QA and handoff
- text-deAI / voice:
- PP slide critic:
- presentation QA:
- unresolved issue:
- appendix / next-slide transition:
```

Classification is multi-axis. `SOSTAC` describes one or more information roles in the deck; `structural_class` describes how standardized the slide is; `visual_pattern` describes the exhibit; `SI` describes a repeatable intent; `GS/library_address` points to reusable construction evidence. None substitutes for another.

Canonical source: Notion [`BPA. Ассемблинг | Assembling (по SOSTAC)`](https://app.notion.com/p/2e2b21994da780d49f8ec052063d39dd).

| Structural class | Meaning | Default route | Required gate |
|---|---|---|---|
| `technical` | status, navigation, service/closing and other highly standardized pages | governed technical template | deck need + no empty-slide violation |
| `normative` | standardized method/model slide such as EST, CJM or action plan | SI -> GS/library template -> project evidence | SI/GS/library address |
| `reference` | evidence-heavy Situation Analysis / appendix / source page | reference template + project evidence | source/evidence-rights trace |
| `consulting` | unique proof construction because the Question cannot be demonstrated by available normative slides | custom reasoning/exhibit | `normative_proof_status=insufficient` + reason + senior review |
| `encyclopedic` | explanatory/teaching page with a broader body of knowledge | governed knowledge structure | explicit teaching/definition role |

SOSTAC is multi-value: one slide may combine Situation Analysis and Objectives or another justified set. Mark every role actually present and a dominant role for ordering when needed.

SI does not directly generate a consulting slide. If a Question cannot be proved by normative/GS constructions, create a consulting slide with an explicit proof gap. After successful defense/reuse, it may enter GS, become normative and receive a newly written SI. GS therefore contains non-consulting slides and former consulting slides that passed normalization.

#### Machine-verifiable pre-client gates 0.3.17

The required order is fixed:

`slide type rationale in production MD -> HTML render -> true-size 16:9 check -> pp-text-critic -> pp-slide-critic -> repairs written back to MD -> rerender -> contact sheet + presentation-qa -> publish -> PPTX`.

Mandatory machine/audit checks:

| Gate | Pass condition |
|---|---|
| critic receipts | durable outputs from both `pp-text-critic` and `pp-slide-critic`; self-report is invalid |
| type rationale | every slide has SOSTAC roles, structural class, visual pattern, library/custom rationale before HTML |
| consecutive layout | no visual pattern/silhouette repeats on more than 2 consecutive substantive slides unless production MD gives a named sequence reason and reviewer accepts it |
| source specificity | no generic labels such as `интервью и документы`; material claims name source object and available locator: respondent/document, date/version, page/section/sheet/range/row or evidence-node ID |
| source language | anglicism/anti-AI checks run against production MD source copy before render, not runtime output |
| opening SCQA | slides 1-5 collectively establish deck Situation, Complication, Question/decision and Answer/direction; slide-level SCA remains separate |
| contact sheet | one screenshot montage/contact sheet contains every slide in order with readable IDs; omissions fail |
| overflow | zero clipping/overlap/scroll overflow at true 16:9 render |
| empty-space geometry | automated bounding-box/canvas audit flags any unexplained empty region >=25% of a substantive slide or substantive-content occupancy below 55%; accepted full-bleed/chart/diagram/cover exceptions require slide-level reason |
| strict aspect | HTML slide viewport, screenshot, print-to-PDF and PPTX export all preserve 16:9 within rendering tolerance; browser shell is excluded from slide bounds |
| golden example coverage | each main visual pattern/structural class used by the deck points to an approved HTML/GS/donor example; consulting slides point to custom rationale and reviewer instead |

Any failed gate returns `hold_before_client`; publication and PPTX are blocked. CSS acceptance comments, runtime replacements and raw counts cannot satisfy these gates.

#### Natasha Tokaeva production contract 0.3.18

Technical compliance is not presentation acceptance. Correct size, palette, font, logo, numbering and footer strips are necessary but cannot compensate for an unassembled argument.

The management thought determines the renderer before HTML:

| Management thought | Required visual family |
|---|---|
| causality / mechanism | causal chain, system map, dependency flow, driver tree |
| comparison / choice | common-row matrix, option profile, comparable table |
| route / transition | pathway, stage-gate, conditional roadmap |
| organization / responsibility | org view, role-interface map, RASCI, decision-rights view |
| decision / condition | decision table, decision tree, conditional recommendation map |
| evidence / diagnosis | chart, analytical table, heatmap, issue tree, evidence map |

A generic card grid is not a neutral renderer. Repeating it across different thoughts is `universal_card_renderer_overuse`. A five-step mechanism such as W06 must be one readable causal construction; five equal cards with arrows fail as `causal_chain_rendered_as_cards`.

Every material claim must have a claim-level evidence row before render:

| Claim ID | Slide ID | Exact claim | Source object | Locator | Evidence right | Caveat | Client wording status |
|---|---|---|---|---|---|---|---|

`Source object` names the interview/respondent, document, model or dataset. `Locator` gives the best available date + quote/timecode, page/section, sheet/range/row or evidence-node ID. Labels such as `интервью и документы`, source ranges without claim allocation, and `источники в приложении` are invalid. A methodology appendix cannot substitute for the claim ledger.

Visible text is corrected in production MD before render. Runtime JavaScript dictionaries, CSS replacement layers and post-render substitutions never count as de-AI, voice or language acceptance. The text critic runs on production MD and again on the final rendered copy.

Every non-neutral color needs a stable color dictionary: `token -> meaning -> allowed objects -> forbidden use`. Decorative multicolor bars or changing semantics across slides fail.

Failure labels: `management_thought_renderer_mismatch`, `universal_card_renderer_overuse`, `causal_chain_rendered_as_cards`, `claim_level_evidence_missing`, `evidence_methodology_substituted_for_ledger`, `source_copy_runtime_cleanup_fail`, `color_dictionary_missing`. Any one of them means `hold_before_client`.

#### Mandatory PP Presentation Kit dependency 0.3.19

Every presentation-producing Rail route must load the installed kit canon before BPA.05/BPA.06 work:

- `pp-slidument/references/kit-2026-07-12-README.md`;
- `pp-slidument/references/deck-content-template.md`;
- `pp-slidument/references/slide_types.md`;
- `pp-slidument/references/visual-style-guide.md`;
- `pp-slidument/references/kit-2026-07-12-pptx-builder-rule.md`;
- both PP critics.

The kit is a mandatory dependency, not an optional reference. Project styles may override the canon only through an explicit owner-approved project visual reference recorded in production MD. Silent fallback to the old Elevel light palette, a generic template, direct PPTX authoring or a partial subset of the kit fails as `pp_kit_dependency_missing` / `pp_kit_version_drift` / `pp_palette_legacy_drift`.

#### No-bypass routing contract 0.3.20

Triggers `презентация`, `дека`, `слайд`, `слайдумент`, `HTML-прототип`, `PP Pages`, `PPTX`, `PowerPoint`, КП со слайдами, deck appendix, slide review/export/publication route through the kit regardless of the entry process or skill.

Required route: `entry process/skill -> pp-slidument kit preflight -> production MD -> domain subskill -> pp-text-critic -> renderer/materialization -> pp-slide-critic -> presentation-qa -> publish/export`.

Domain subskills may add interview, survey, dashboard, MPP/КП, BPV, BPM Exchange or consulting logic but cannot replace, weaken or reorder the kit gates. Every agent/subagent returns a durable receipt: `kit_version | production_md_path | template_loaded | slide_types_loaded | visual_guide_loaded | builder_rule_loaded | text_critic_report | slide_critic_report | presentation_qa_verdict | export_status`.

Missing receipt, direct artifact generation, specialist independence from `pp-slidument`, or a one-critic route is `pp_kit_route_bypass`; status remains `hold_before_client`.

#### Public upstream contract 0.3.21

Canonical upstream: `https://github.com/ntokaeva/paper-planes-presentation-kit`, public repository, default branch `main`. Verified HEAD on 2026-07-12: `c9aa8b46f1a306f9037d36957bb778ebe990a2cc`.

The installed ZIP remains an installation snapshot with its own SHA-256. Before future kit changes or presentation production after a declared kit update, compare the installed references with upstream and record `upstream_url | upstream_commit | installed_snapshot | drift_status` in the kit receipt. Repository accessibility failure is a source-sync gap, not proof that the repository is private.

Until Ilya supplies the historical full slide classification, unknown leaf types must be marked `classification_pending_owner_ingest`; do not force them into the current provisional list. The scaffold may be extended without changing its stable axes.

#### Audit provenance isolation and scope-disposition contract 0.3.15

When Ilya asks to inspect another chat, dry-run, task or working directory, Rail must bind the audit before reading conclusions:

| Field | Required value |
|---|---|
| audit target | exact Codex thread/task ID |
| working directory | exact cwd supplied by Ilya or recorded in thread metadata |
| session source | matching session file(s) / thread history |
| allowed evidence | messages, files and writebacks generated by that target |
| excluded evidence | same-client project chats, ambient browser tabs, similarly named folders and later summaries unless explicitly requested |

No claim may be attributed to the audited chat without a matching target trace. Same client/project name is not sufficient. If evidence from another chat is useful, label it `external_comparison` and keep it outside the causal audit. Failure: `audit_thread_provenance_mixed`.

Before BPA.01 is accepted, create a cumulative scope-disposition ledger from the complete post-mining problem model:

| Macro-tension / accepted objective | Source / owner | Role before BPA.01 | BPA disposition | Deliverable / section | Governing-question role | Reason / owner decision | Revisit trigger |
|---|---|---|---|---|---|---|---|

Allowed dispositions: `core_primary`, `core_secondary`, `appendix`, `separate_deliverable`, `deferred_with_trigger`, `removed_by_owner`, `justified_no_op`. Silence, omission and `represented by evidence` are invalid.

A narrow decision-deck instruction selects a primary decision but does not silently replace the complete problem scope. Any narrowing must state whether it is `add`, `refine` or `replace`. `replace` requires explicit owner confirmation and row-level disposition of displaced objectives.

Every accepted objective receives an objective-role trace:

`BPA.01 disposition -> BPA.02 governing-question role -> BPA.04 Answer/SCQA -> narrative spine -> production MD -> W01/W02 or named later route -> appendix/separate deliverable`.

Presence in a late slide is not equivalent to preserved role. A `core_primary` or `core_secondary` objective must appear with the agreed prominence in the governing frame, Answer/SCQA and opening deck architecture. Otherwise use `objective_role_degraded`.

If Ilya later adds, revives, promotes, demotes or reframes an objective, Rail performs an upstream divergence audit. Reopen BPA.01–BPA.05 from the earliest artifact whose objective-role trace is no longer correct. Do not preserve a passed status merely because a downstream block was appended. All dependent C4, content-review and render permissions are invalidated until regeneration.
6. Choose output mode explicitly: `editable` is default; `raster` is allowed for rapid show/review when non-editability is stated. Record the choice and reason.
7. The current Codex runtime's system `Presentations` skill remains the production owner for PPTX materialization. Follow its visual-route, `@oai/artifact-tool`, scratch/final-output, render, montage, overflow/overlap and iterative repair contract. The PP HTML prototype and builder rule govern brand/layout behavior; they do not authorize bypassing the runtime's mandatory materialization tool.
8. `consulting-slides-creator` may supply slide-type ideas, layout references and QA prompts only. It is not the final generator and must not determine the visible style by itself.
9. Render every slide and inspect both individual renders and a montage. Fix text wrapping, overlap, clipping, inconsistent logo placement, density imbalance and visual regressions.
10. Run both PP critics before delivery: `pp-text-critic` for language/anti-AI/voice and `pp-slide-critic` for action titles, density, sources, fonts, shadows and style consistency.
11. Run `presentation-qa` as the independent strategic/source/storyline/client-readiness judge. It complements the PP critics and does not replace them.

#### PP visual-likeness and density gate

`overflow 0/N`, valid HTML, successful screenshots and a readable title are technical checks only. Before the HTML can unlock PPTX, inspect every slide against the installed PP builder rule and approved PP slide image:

| Check | Pass condition |
|---|---|
| paper / brand | approved PAPER field, restrained PP accents, no generic white SaaS/card-dashboard appearance |
| global logo | actual logo asset in one governed slot with consistent size; not a typed brand name |
| typography | accepted PP family; Cyrillic editable default PT Sans; no arbitrary web-font substitution |
| action title | concrete conclusion that advances the decision; descriptive topic labels fail |
| analytical density | the canvas is substantively occupied by evidence, comparison, mechanism, table/chart or decision logic; large unused areas and three short cards fail |
| exhibit specificity | each slide has a functional exhibit tied to its claim; decorative cards/chips alone do not count |
| concrete content | named object, mechanism, evidence status, decision implication and source/caveat where material |
| silhouette diversity | deck uses varied but coherent tables, comparison profiles, decision trees, flows, matrices, org views and evidence exhibits; repeated card grids across the deck fail |
| audience language | visible copy is Russian professional language; avoidable anglicisms, internal production vocabulary, agent codes and untranslated labels fail |
| anti-AI language | no formulaic `не X, а Y`, rhetorical framing, anthropomorphism, power words, repetitive synthetic cadence or arrow-heavy pseudo-logic |
| sources | material numbers and factual claims have visible source/caveat treatment |
| no decoration-only UI | pills, rounded cards and badges are used only when they encode meaning, not as the default composition |

#### Substantive-slide SCA gate 0.3.12

Every substantive slide in the main deck and decision-relevant appendix must have a visible analytical chain:

`Situation -> Complication -> Answer`.

- `Situation` states the relevant evidence, current condition or accepted premise.
- `Complication` explains why that situation obstructs the client's stated objectives, creates a decision tension, or changes the economics/risk of the choice.
- `Answer` provides the resulting model, implication, decision rule, recommendation, hypothesis or next evidence gate.
- The action title expresses the slide's `Answer`, not its topic and not a summary of the `Situation`.
- The exhibit must make the transition from evidence to implication inspectable. Three short fact cards are not an analytical chain.

SCA is a reasoning contract, not a mandatory three-column template. A slide may use a causal bridge, matrix, tree, flow, comparison, decomposition, chart or other functional exhibit. Cover, section divider, protocol/decision wording and purely technical appendix pages may be marked `SCA_not_applicable` with a reason.

Before BPA.06, BPA.05 must contain a slide-level ledger:

| Slide ID | Deliverable objective | Situation | Complication for client objective | Answer / action title | Exhibit / model | Evidence / caveat | SCA status |
|---|---|---|---|---|---|---|---|

The ledger must also reconcile all accepted objectives from BPA.01/BPA.02/BPA.04. Compression into one governing question must not erase a parallel objective such as improvement of the current operating model while another strategic choice is assessed.

Mandatory result: `PP_visual_likeness_passed / failed`, slide-level defects, repaired slide IDs, and a montage-based final verdict. The agent must compare the deck with at least one approved PP reference image/deck or the installed builder rule. Self-attestation based only on CSS tokens is invalid.

Acceptance anti-loophole rules:

- `source-copy integrity`: audience-visible text must be corrected in the source slide data/content. JavaScript replacement dictionaries, CSS pseudo-content, post-render substitutions or hidden duplicate text cannot substitute for text-deAI/voice editing. Runtime replacement may support a migration pass, but the gate remains failed until the source copy itself is clean.
- `composition repair`: changing colors, borders, radii, accent bars or background variables while retaining the same repeated card-grid renderer is a skin repair, not a slide-format repair. The report must name which slide IDs changed silhouette and how.
- `logo provenance`: the global mark must use an official/local approved logo asset or a verified exact export. A hand-drawn/reconstructed SVG does not pass merely because it is visually similar. Record asset path/hash or approved source URL and rendered consistency.
- `font realization`: declaring a font family in CSS is insufficient. Verify the rendered/computed font on representative slides or embed/load the approved font. Fallback to Arial or another family must be reported.
- `critic evidence`: `PP_visual_likeness_passed` requires attached/recorded outputs from `pp-slide-critic` and `pp-text-critic`, plus montage review and slide-level repaired IDs. Counts such as `logo 23/23` or `overflow 0/23` cannot replace critic evidence.
- `owner-edit hold`: when Ilya says he will provide further artifact edits, update standards/statuses but do not modify the physical HTML/PPTX until those edits arrive. Mark `artifact_owner_edits_pending` and preserve the current artifact.

The handoff must record: `pp_kit_version`, `production_owner_skill`, `html_prototype`, `pp_pages_or_local_review`, `visual_route`, `primary_reference`, `global_logo_check`, `output_mode`, `final_pptx_path`, `render_path`, `overflow_test`, `montage_review`, `text_deai_status`, `balakhnin_voice_status`, `pp_text_critic_status`, `pp_slide_critic_status`, `presentation_qa_status`, and unresolved defects.

Failure labels:

- `presentation_production_skill_bypass` — PPTX created outside the mandatory system Presentations materialization route;
- `pp_html_first_missing` — PP deck materialized without the HTML-first visual prototype;
- `pp_brand_layer_missing` — light PP system / global logo / consistent grid absent or unverified;
- `pp_visual_likeness_fail` — technically valid HTML does not resemble an approved PP slidument in density, specificity, composition or visual language;
- `pp_generic_card_grid_fail` — repeated generic card/pill layouts substitute for analytical exhibits;
- `pp_logo_asset_missing` — typed brand name or absent mark substituted for the governed logo asset;
- `pp_visible_language_fail` — avoidable English/internal/AI-pattern language remains in the visible slide layer;
- `pp_density_specificity_fail` — slide is sparse, generic or lacks a claim-specific exhibit;
- `pp_css_skin_only_fail` — palette/borders changed but slide silhouettes and exhibit logic remained generic;
- `pp_runtime_copy_replacement_fail` — visible text appears corrected only through runtime substitutions while source copy remains unedited;
- `pp_logo_provenance_fail` — logo is reconstructed/unverified or lacks durable asset provenance;
- `pp_font_realization_unverified` — approved font declared but not loaded/computed/render-verified;
- `pp_critic_evidence_missing` — visual pass claimed without both PP critic outputs, montage verdict and repaired slide IDs;
- `pp_pages_or_browser_review_missing` — no PP Pages attempt and no equivalent local visual inspection;
- `pp_pages_shell_missing` — HTML is a long-scroll slide stack without the governed PP Pages viewing shell;
- `pp_slide_navigator_incomplete` — sidebar/thumbnail navigator does not include all slides, active state or reliable navigation;
- `pp_shell_slide_layer_mixed` — shell controls are embedded into slide content or would leak into PPTX;
- `pp_color_semantics_undefined` — multiple colors are used without stable named meaning or legend;
- `production_md_deck_spec_missing` — HTML/PPTX work starts without an authoritative intermediate Markdown specification;
- `production_md_not_source_of_truth` — visible render content differs from MD or was edited only downstream;
- `slide_dual_classification_missing` — SOSTAC role or structural class is absent;
- `slide_library_address_missing` — a normative/reference slide lacks SI/GS/library/donor routing or justified custom-consulting status;
- `slide_spec_incomplete` — slide lacks SCA, content, evidence, exhibit, assembly or QA fields;
- `render_started_before_md_gate` — HTML, PP Pages or PPTX materialization started before the MD deck spec passed;
- `audit_thread_provenance_mixed` — causal audit combines the requested dry-run/chat with another project chat or directory;
- `scope_disposition_ledger_missing` — BPA.01 narrows the deliverable without row-level fate for every macro-tension/objective;
- `scope_change_mode_undefined` — add/refine/replace was not stated;
- `scope_replacement_without_owner_confirmation` — prior objective was displaced without explicit owner decision;
- `objective_role_degraded` — objective exists downstream but lost its agreed prominence in governing question, Answer/SCQA or opening deck;
- `upstream_reopen_missing` — a later scope correction was appended downstream without reopening dependent BPA stages;
- `stale_gate_after_scope_change` — C4/content/render pass remains active after an upstream objective change;
- `sostac_single_label_forced` — a mixed-information slide was forced into one SOSTAC role and lost content logic;
- `consulting_slide_without_normative_gap` — custom consulting construction was chosen without proving normative slides insufficient;
- `SI_direct_to_consulting_fail` — an SI was treated as a direct consulting-slide generator;
- `GS_normalization_without_review` — a consulting slide was promoted to GS/normative without review evidence and a new SI;
- `slide_type_rationale_missing` — slide type/pattern was chosen after render or without management-thought rationale;
- `consecutive_layout_repeat_fail` — one layout repeats more than twice without accepted sequence reason;
- `generic_source_label_fail` — source note is generic and not traceable to a named object/locator;
- `opening_SCQA_fail` — first five slides do not establish the deck-level reasoning and decision;
- `contact_sheet_incomplete` — montage/contact sheet omits or misorders slides;
- `empty_space_geometry_fail` — substantive slide has unexplained large empty area or low occupancy;
- `strict_16x9_export_fail` — screen, print/PDF or PPTX dimensions do not preserve 16:9;
- `golden_example_coverage_missing` — a main slide type/pattern has no approved reference or custom-consulting rationale;
- `pp_text_pipeline_missing` — text-deAI or Balakhnin voice pass absent;
- `pp_critic_stack_missing` — pp-text-critic or pp-slide-critic absent;
- `pptx_render_qa_missing` — deck returned without complete render/montage/overflow review;
- `presentation_visual_route_undefined` — layout started without a selected visual route/reference;
- `consulting_slides_creator_used_as_final` — fallback/reference generator incorrectly used as final PP production path.
- `slide_situation_only_fail` — slide lists facts or circumstances but does not explain the complication and resulting answer;
- `slide_complication_missing` — the relevance of evidence to the client's objectives or decision is absent;
- `slide_answer_unsupported` — answer/action title is not supported by the stated situation and complication;
- `slide_objective_scope_loss` — an accepted deliverable objective disappeared during governing-question, storyline or slide-brief compression;
- `intro_card_underdeveloped` — a large introductory block uses generic labels without diagnostic questions, known state, decision need or expected output;
- `slide_exhibit_reasoning_gap` — exhibit decorates or lists content but does not expose the evidence-to-implication transition.

If BPA.05 / BPM Exchange / Rail selected reuse donors, distinguish four reuse classes before authoring:

- `mechanism reuse`: causal logic, governance pattern, calculation, process, pilot or BPV mechanism;
- `slide-format reuse`: composition of a specific successful slide or exhibit;
- `deck-architecture reuse`: sequence, section rhythm, decision framing, appendix logic or defense choreography of a successful deck;
- `visual-template reuse`: typography, grid, palette, master-like composition and visual system. Exactly one primary visual reference is allowed for the system Presentations route unless the user explicitly authorizes a mixed custom design.

Mechanism selection does not automatically select the same project's deck as a presentation reference. Slide/deck reuse requires a physical PPTX/PDF, known version, defense/review status, inspectable pages, and specific slide IDs or deck sections.

BPA.06 must consume a presentation-reuse ledger before authoring:

| Reuse class | Donor project / deck | Physical file + version | Defense / acceptance status | Donor slide IDs / sections | Why successful / relevant | Transfer | Do not transfer | Target Elevel slide / role | Primary visual reference? | Adaptation / source-right gate |
|---|---|---|---|---|---|---|---|---|---|---|

Every accepted donor must have a visible fate. A mechanism donor may feed a normal slide or appendix proof. A slide/deck donor may feed a specific layout, exhibit, narrative sequence, or dedicated reuse/analog slide when comparison itself helps the client decide. A donor-name list without physical deck inspection and slide-level analysis is invalid. Client content, numbers, logos and claims are never copied as Elevel evidence. Missing routing is `reuse_to_slide_route_missing`; missing physical/defense/slide-ID trace is `reference_deck_source_gap`; multiple ungoverned visual references are `presentation_visual_reference_conflict`; a donor slide presented as a current-client fact is `reuse_claim_overreach`.

### Nine-action assembly completeness contract

The nine Estuarine action classes are not merely a Gate 3 analytical table. Their coverage must be checked through assembly because missing classes can reveal missing evidence, solution bias, an omitted external scan, ignored authority dependencies, or loss of an important slide route.

Required BPA placement:

| BPA | Mandatory nine-action operation |
|---|---|
| `BPA.03` | register which action classes generated accepted SI and storyboard hypotheses |
| `BPA.04` | run the primary completeness diagnostic against active P-nodes, Cynefin domains, Estuarine zones and actants |
| `BPA.05` | verify that analytically significant classes have a visible core/appendix/no-op slide fate and were not lost during slide-brief compression |
| `BPA.07` | preserve the full matrix, evidence gates and justified no-signal reasons in appendix/support material |
| `BPA.08` | rerun an independent action-portfolio completeness review before client-ready status |
| `BPA.09` | ensure `Conditional`, `Trigger`, and `Request` are reflected in resolution wording, decision gates, monitoring signals and authority/resource requests where applicable |

Mandatory ledger:

| Action class | Candidate count | Linked P-nodes + actants | Cynefin / Estuarine basis | Storyboard / slide route | Coverage status | Absence explanation | Remediation / evidence gate |
|---|---:|---|---|---|---|---|---|

Allowed coverage statuses: `covered`, `justified_no_signal`, `data_gap_candidate`, `analytical_omission`, `storyboard_omission`, `method_mismatch`.

Absence is not automatically an error, but every zero class requires a visible explanation or remediation. Hard anomaly checks:

- volatile actants without `Stabilise` -> `stabilise_coverage_gap`;
- liminal actants without `Request` -> `request_authority_gap`;
- complex/aporetic problems without `Conditional` -> `conditionality_gap`;
- counterfactual/external conditions without `Monitor` or `Trigger` -> `external_signal_gap`;
- cross-functional conflicts without `Interaction` -> `interaction_design_gap`;
- action portfolio dominated by `Create` -> `solution_creation_bias`;
- no `Destroy` anywhere -> `initiative_pruning_gap_candidate`;
- no `Shift` where time/energy barriers are material -> `changeability_shift_gap`.

Not every class must appear in the core deck. Every class must be checked, and its fate must be `core`, `appendix`, `justified_no_signal`, or a named return to evidence/BPA.03/BPA.04. BPA.05 cannot pass and BPA.06 cannot start when a zero class remains unexplained or an analytically significant class has no slide route.

### BPA.05 to BPA.06 hard-gate summary

BPA.06 physical deck authoring is allowed only when all are true:

1. slide brief and method challenge passed;
1a. the slide-level SCA ledger passed for every substantive slide and all accepted deliverable objectives remain visibly routed;
1b. one authoritative production MD deck specification passed, including deck header, dual slide classification, SI/GS/library routing, SCA, evidence, exhibit, assembly and QA fields;
1c. the full scope-disposition ledger and objective-role trace passed; no objective is silently omitted, degraded or changed without upstream regeneration;
2. nine-action completeness ledger passed with every class explained;
3. accepted mechanism donors have transfer/no-transfer/adaptation and slide routes;
4. slide/deck reuse has physical file, version, defense status and donor slide IDs, or an explicit justified no-reference decision;
5. one primary visual reference/route is selected;
6. explicit new-file permission exists;
7. the complete PP Presentation Kit pipeline is active: pp-slidument -> audience-visible text-deAI + Balakhnin voice -> HTML-first PP prototype + global logo -> PP visual-likeness/density gate -> PP Pages/local browser inspection -> system Presentations materialization -> render/montage/overflow -> pp-text-critic + pp-slide-critic -> presentation-qa.

Failure of any item must name the exact blocker. Rail must not silently fall back to improvised PPTX generation.

Evidence-rights guard for assembly:

- Do not turn BPM-2 organizational material into BPM-3 client jobs unless the respondent explicitly reports customer-side evidence.
- If there is no BPM-3, mark CJM / КПО / buyer-language material as reconstructed from BPM-2 / BPM-6 / BPM-7B / best-practice evidence, not as proven client jobs.
- Treat coding membranes like BTK document `10` as mandatory when BPM-3 is transformed into slide jobs, PCA / Bain x Kano logic, CJM / КПО, or acceptance-barrier slides.
- Treat organizational validation as an operating filter: it checks executability, data, SLA, roles, documents, CRM, last mile, owner, and result responsibility; it does not prove the client job by itself.
- When a deck uses the BTK slide-2 / slide-7 pattern or a similar B2B-service pattern, recognize the separate BPM-SI route `BPM-2 x BPM-3 three-level operating validation`: `BPM-3 job / value -> BPM-2 validation strip: CEO/shareholder filter -> non-operational back -> operations filter -> КПО / service blueprint row -> BPA.05`.
- Do not call the middle subfilter `concept` as canon. Use `non-operational back` / `неоперационный бэк`: marketing, product, digital, service solutions, B2B, commercial support and other functions that support the promise but are not the final operational execution layer.
- Do not classify functions into `non-operational back` and `operations` by department name alone. Require an org-structure classification preflight: value-chain role, client-promise role, decision rights, execution rights, last-mile responsibility, SLA/data ownership, and industry-specific operating model. In some companies, such as TD Комплект-type structures, the same named service or commercial function can be back, operations, or hybrid until the org map and actual work are inspected.

Problem / Cynefin / Estuarine / BPV route guard for assembly and dry-runs:

- Do not route a source directly to BPV / sub-BPV before extracting the problem node and causal-regime / Cynefin domain.
- Do not start with actants as if they were the problem. Actants explain what holds or changes a problem after the problem is named.
- Required order: `source -> problem_node / ПЦВЗ / SCQA -> Cynefin domain -> Estuarine actants -> problem-actant links -> possible actant_action_class -> SI / САИ / slide-intent -> initiative hypothesis -> BPV / sub-BPV / derivative / gate route -> sub-BPV x actant-action score`.
- In Old Delivery dry-runs with more than one source, do not use a respondent-by-respondent contradiction table as the main view. First group evidence into macro-ideas / strategic tensions, then attach respondents and BPM sources to those macro-ideas. The view must scale when more interviews arrive.
- Actants are polymorphic. A single actant may play several roles (`actor`, `constraint`, `constructor`) across different problems. Do not force one primary class if the evidence shows multiple roles; show class-per-problem or class-per-mechanism.
- Validate actant type before output. Use `actor` only for an entity with agency: person, role, team, function, governance body, customer, supplier, contractor, state actor, partner, or another decision-capable side. Abstract mechanisms and conditions such as `отсрочка`, `склад`, `KPI`, `план`, `бонус`, `договор`, `ликвидность`, or `цифровая воронка` are normally `constraint`, `constructor`, `resource`, or `evidence carrier`, not `actor`, unless the output names the owner who acts through them.
- Possible actions must be shown as a 9-action matrix for every significant problem-actant pair or macro-idea: `Stabilise / Destroy / Shift / Create / Monitor / Conditional / Trigger / Request / Interaction`. If an action type is irrelevant, mark `no_signal` or `low_fit`, not silence.
- 9-action cells must be concrete. Each non-empty cell should name the actant, intervention mechanism, and evidence/gate needed. Generic cells such as `пересмотреть`, `мониторить`, `создать правила`, `наладить взаимодействие`, or `запросить данные` without object and mechanism are `action_cell_too_generic`.
- The 9-action matrix is cumulative across the project evidence corpus. It must cover all active problem nodes accumulated from all ingests so far, not only the problem nodes affected by the latest source. The latest ingest can add rows, revise cells, change confidence, or mark `no_change_from_current_ingest`; it must not hide older active P-nodes.
- If problem is missing, mark `problem_map_missing`; if Cynefin domain is missing, mark `causal_regime_missing`; if actants are missing, mark `actant_map_missing`; if action is not linked to SI / slide-intent, mark `SI_slide_intent_missing`; if BPV appears too early, mark `premature_BPV_route`.
- In human-facing Rail output, write BPV as `code + name`, for example `BPV-08 — Система управления -> BPV-08.6 — Разработка и внедрение организационной структуры`. Bare BPV codes are not sufficient.

Mandatory human-facing tables for Old Delivery multi-source dry-runs:

1. `Macro-idea evidence map`, replacing a wide surname table:

| Macro-idea / tension | Problem nodes | Cynefin | Supporting sources | Divergent sources | Cross-source status | What must be checked next |
|---|---|---|---|---|---|---|

Use this to group positions by similarity and disagreement. If a new respondent arrives, add them to `supporting` or `divergent`, not as a new column unless their role itself is the unit of analysis.

A macro-idea map that omits `Supporting sources`, `Divergent sources`, `Cross-source status`, or `What must be checked next` is incomplete. Do not replace these with a single latest-source delta column.

The exact required columns are `Macro-idea / tension`, `Problem nodes`, `Cynefin`, `Supporting sources`, `Divergent sources`, `Cross-source status`, and `What must be checked next`. A table with `Delta of current source` and `Status` but without the multi-source columns is not compliant with Rail 0.1.18.

2. `Polymorphic actant map`:

| Actant | Roles by problem | Linked problems | Mechanism | Source trace | Growth driver | Energy/time barrier | Zone / changeability | Open check |
|---|---|---|---|---|---|---|---|---|

`Roles by problem` must include code + problem name, not bare codes. Use forms like `P12 — Проектный контур собирается вручную: actor; P14 — CRM и проектная таблица расходятся: constructor`. `Linked problems` is mandatory and also uses code + name; an actant without a problem link remains `actant_source_check`.

The `Polymorphic actant map` must keep `Roles by problem` and `Linked problems` as separate columns. `Roles by problem` says what role the actant plays per problem; `Linked problems` lists all connected problem nodes as code + name. Omitting `Linked problems` is a coverage failure.

Omitting `Source trace`, `Growth driver`, `Energy/time barrier`, or `Zone / changeability` is also an incomplete Estuarine map. If evidence is absent, write `source_gap / no_signal`, not a blank cell.

Do not merge `Roles by problem` and `Linked problems` into one column such as `Роли и связанные проблемы`. Do not write linked problems as bare codes (`P5, P20, P22`); use code + name. Avoid non-canonical actant types such as `system gap` as the type. If something is a gap, name the underlying actant or mechanism and mark the gap in `Open check` / `Energy/time barrier`.

3. `9-action matrix`:

| Problem / macro-idea | Actant | Stabilise | Destroy | Shift | Create | Monitor | Conditional | Trigger | Request | Interaction | Best next action | SI / slide-intent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Cells may use `high / medium / low / no_signal` or `1-5` when a score is useful. The matrix is required even when the answer later selects only 2-3 practical actions.

For cumulative output, add a column `Current ingest effect` when useful:

| Problem / macro-idea | Actant | Current ingest effect | Stabilise | Destroy | Shift | Create | Monitor | Conditional | Trigger | Request | Interaction | Best next action | SI / slide-intent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Allowed effects: `new / revised / confirmed / weakened / no_change_from_current_ingest / deprecated`.

`Problem / macro-idea` must name covered problem nodes as code + name, not only `P5 + P9 + P11` or ranges such as `P12-P15`. Grouped rows are allowed only when all included problem nodes are explicitly named and the evidence/gate for each covered node is visible. A catch-all row such as `commercial / CRM / CFO / evidence gaps remain` is incomplete.

### Old Delivery Coverage Check

Every Old Delivery Rail/BPM pass after the second ingest must run a coverage check before finalizing. The pass is incomplete if any active problem node is missing from required cumulative views.

```text
coverage check:
active problem nodes total:
shown in problem history:
shown in macro-idea map:
shown in polymorphic actant map:
shown in 9-action matrix:
shown in SI/BPV trace:
missing:
verdict: complete / incomplete
```

Rules:

- `problem history` must include all active nodes with `code + name`.
- `polymorphic actant map` must include all active nodes either through an actant link or an explicit `no actant signal / source_check` row.
- `9-action matrix` must include all active nodes or a justified grouped macro-row that names all covered problem nodes.
- `SI/BPV trace` must be tabular, not a plain bullet list, and include `Output / route`, `Derived from`, `Source trace`, `Status`, `Confidence`, and `Next evidence / gate`.
- `SI/BPV trace` must show every active problem node either directly through an output/route or explicitly as `evidence_gap / no current SI / no current BPV route`. Writing that remaining nodes are "represented as evidence gaps" without rows for those nodes is a coverage failure.
- `verdict: complete` is allowed only when every required view has visible rows or justified grouped rows for every active problem node. If any mandatory row is only implied, use `verdict: incomplete` or fix the table before finalizing.
- If `missing` is non-empty, fix the output before final answer or mark the run `incomplete` with the exact missing nodes.

For Rail 0.1.20 and later, the final coverage check must be backed by a node-by-node coverage ledger. Do not infer coverage from counts alone.

Minimum ledger:

| Problem node | Problem history | Macro-idea map | Actant map | 9-action matrix | SI/BPV trace | Missing / fix |
|---|---|---|---|---|---|---|

Each row must use the full problem node name, e.g. `P13 — Нет общего финансового словаря`. Each required view cell must be `pass` only when that exact node is visible in that view as `code + name` or in a grouped row that explicitly lists `code + name` for that node. If a view shows only a range (`P11-P13`), compact cluster (`P6/P10/P18`), or bare code (`P13`), the cell is `fail: bare_or_ranged_code`. If a node is absent from the actant map, add an actant-map row with `no actant signal / source_check`; otherwise the ledger cell is `fail: missing_actant_row`.

The counts in `coverage check` must be computed from this ledger, not from a narrative claim. A self-audit row saying `pass — 22/22` is invalid if the ledger would fail any node.

The ledger schema is exact. Do not merge columns. A column named `Actant/action trace`, `Actant + action`, `Actants/actions`, or any equivalent combined field is invalid and must be marked `node_coverage_ledger_schema_fail`. `Actant map` and `9-action matrix` are separate gates because a node can appear in one and be absent from the other.

Delta tables do not satisfy cumulative coverage. A table titled `Polymorphic actant map — delta`, `SI / slide-intent delta`, or similar can be useful as a current-source delta, but it cannot be used to mark all active nodes as covered. To mark `pass` in the ledger, the cumulative actant map and cumulative SI/BPV trace must visibly contain the node, or the row must explicitly state `no actant signal / source_check` or `no current SI/BPV route / evidence_gap` for that exact node.

Question coverage audit uses an exact schema: `question_id`, `question / intent`, `target respondent`, `asked status`, `answer status`, `evidence gained`, `linked P-node / SI`, `remaining gap`, `best next respondent`, `prompt improvement`. Shorter headings such as `Asked`, `Answer`, or `Linked node / SI` are not compliant. `linked P-node / SI` must use code + name, not bare codes.

The source register must decompose stacked BPM labels when several BPM rights are claimed. A compact label such as `BPM-2/4/8/9 — интервью Самакаева` is not enough for downstream trace. Use separate rows or explicit labels such as `BPM-2 / интервью Самакаева`, `BPM-4 / channel economics from интервью Самакаева`, `BPM-8 / process evidence from интервью Самакаева`, `BPM-9 / HR/capacity evidence from интервью Самакаева`.

Document writeback status is incomplete unless each updated/created file has a path or link. A list of file names without paths/links is `writeback_trace_fail`, even when sync gaps are listed.

### Old Delivery Tabular / Excel / Workbook Ingest

Rail 0.2.01 is the unified current Rail, not a parallel branch. It inherits all 0.1.x Old Delivery guardrails: problem -> Cynefin -> actants -> actions -> SI/BPV order, cumulative evidence documents, code+name nodes, node-by-node coverage ledger, exact self-audit schemas, writeback path requirements, and no pseudo-ledgers. The tabular-source contract below is an added source-class contract inside the same Rail.

Use `tabular_source_ingest` when the source is an Excel / XLS / XLSX workbook, CSV export, Google Sheet export, table dump, BI table export, or another structured table-like source. Do not call the class only `workbook ingest` when the source may be a single sheet, CSV, XLS, XLSX, exported range, or table package. Use `tabular_source_ingest` as the generic class and a more specific `source_container` where known.

Required chain:

```text
tabular source
-> source persistence / temporary-source status
-> source manifest
-> sheet/table/range register
-> formula / calculation / lineage audit when applicable
-> quantitative claim trace
-> BPM-addressed source decomposition
-> problem-node delta
-> SI/BPV trace or explicit delta-only verdict
-> data-quality verdict
-> node-by-node coverage ledger when cumulative coverage is claimed
```

Minimum source manifest:

| Field | Requirement |
|---|---|
| `source_id` | stable ID such as `SRC-12` |
| `source_container` | `xlsx / xls / csv / google_sheet_export / table_export / unknown` |
| `file_name / table_name` | human-readable source name |
| `project_path / temp_path` | project path if persisted; temp path only as `source_persist_gap` |
| `sheet/table count` | number of visible sheets/tables when applicable |
| `used ranges / row-count` | sheet ranges or table row/column counts when inspectable |
| `period / grain` | analytical period and grain if present |
| `key dimensions` | business, region, product, channel, etc. |
| `key measures` | revenue, ВНП1, маржа, plan/fact, etc. |
| `source status` | `persisted / temp_only_dryrun / temp_only_blocker / external_object / partial` |

Formula and external-reference audit is conditional:

- If formulas exist, report formula count, formula areas / sheets, cached-value availability, and formula-error status.
- If external references exist or are claimed, list them, their count, whether cached values exist, and whether autonomous recalculation is possible.
- If no external references are present, write `external references: none_detected`; do not create a gap.
- If external source workbooks are not included in a dry-run, this is `data_lineage_gap / autonomous_recalculation_not_possible`, not automatically a fatal Rail failure. It blocks full auditability and client-facing quantitative canonization until resolved.

Question coverage audit is `not_applicable` only when replaced by a tabular-source audit. The replacement audit must explicitly cover: `source manifest`, `sheet/table/range register`, `formula/calculation audit when applicable`, `external reference audit when applicable`, `quantitative claim trace`, `data-quality verdict`, and `source persistence status`.

Quantitative claims must be traceable to sheet/table/range, formula/value status, and caveat. A claim based on cached external values must say so. Do not write `formula errors: 0` as full validation when external references are missing; write `cached formula errors: 0; autonomous recalculation: not possible without external sources`.

BPM-addressed source decomposition for tabular sources should reflect evidence rights, not force every BPM. Examples:

- `BPM-4 / quantitative economics from SRC-12`;
- `BPM-10 / data-lineage and CRM/table consistency from SRC-12`;
- `BPM-11 / reporting artifact from SRC-12`, only if the file is actually a reporting/management artifact;
- `BPM-8 / process evidence from SRC-12`, only if the file shows process handoff, ownership, or operating practice.

Do not require external-source addressing when the file has no external references and no claim depends on absent source parameters. Do require it when formulas, linked values, named ranges, or claims depend on external source files.

Verdicts for tabular sources:

| Verdict | Meaning |
|---|---|
| `passed_with_tabular_delta` | useful quantitative delta extracted, no cumulative coverage claimed |
| `passed_with_data_lineage_gap` | useful but external references / lineage prevent full recalculation |
| `passed_with_source_persist_gap` | dry-run source remains temporary; analysis can stand, durable canonization waits |
| `incomplete_tabular_contract` | manifest / table register / claim trace missing |
| `incomplete_quant_audit` | formulas, cached values, or claim trace insufficient for stated quantitative claims |

If the pass does not claim cumulative coverage across all active P-nodes, do not output ordinary Old Delivery `coverage check: complete`; output `delta-only verdict` plus affected P-nodes. If cumulative coverage is claimed, all Rail 0.2.01 node-by-node ledger rules still apply.

### Old Delivery Batch Interview Ingest

Rail 0.2.02 is the unified current Rail. It inherits all 0.2.01 and 0.1.x guardrails and adds a source-class contract for `batch_interview_ingest`. Use this when two or more interviews / interview-like sources are processed in one pass.

Batch processing does not merge sources. Every source in the batch must keep its own source rights, limitations, question audit, problem-node delta, and downstream trace. Cross-source synthesis is allowed only after per-source deltas are visible and must be marked as `batch_synthesis`.

Minimum batch preflight:

| Field | Requirement |
|---|---|
| `batch_id` | stable batch ID |
| `batch_size` | number of sources |
| `ordered_sources` | ordered source IDs and respondents |
| `source_isolation` | must be `required / preserved`; otherwise incomplete |
| `cross_source_synthesis` | `allowed_with_trace / not_allowed / blocked` |
| `partial_batch_success` | whether partial success is allowed |
| `rail_version` | current unified Rail version |

Minimum per-source rights table:

| batch item | source_id | respondent / role | source type | source status | BPM-addressed rights | processed layers | limitations | contribution | batch synthesis rights |
|---|---|---|---|---|---|---|---|---|---|

Rules:

- `source status` must distinguish `primary transcript`, `primary_sync_truncated`, `secondary summary`, `AI summary`, `structured summary`, `raw missing`, and other evidence levels.
- `BPM-addressed rights` must decompose compact labels. Do not write only `BPM-1/2/8/9`; first resolve `BPM-1A` versus `BPM-1B`, then use explicit labels like `BPM-1B / employee survey evidence from SRC-13`, `BPM-2 / interview evidence from SRC-13`, `BPM-8 / process evidence from SRC-13`.
- `processed layers` must state which layers were actually processed: problem, Cynefin, actants, actions, SI/BPV, question audit.
- `limitations` must preserve source weaknesses such as truncated transcript or secondary summary.
- `batch synthesis rights` must say what may be synthesized from this source and what must remain source-limited.

Minimum batch output order:

```text
batch preflight
-> per-source rights table
-> source A delta
-> source B delta
-> per-source question audits
-> batch synthesis table
-> cumulative problem-node history or explicit delta-only verdict
-> macro-idea map
-> actant map
-> 9-action matrix
-> SI/BPV trace
-> node-by-node coverage ledger when cumulative coverage is claimed
-> document writeback status with paths/links
```

Question audit in batch mode:

- run per source, not only at batch level;
- use exact question audit schema from Rail 0.1.x / 0.2.x;
- add a carryover backlog table only after per-source audits;
- if a source is a secondary summary and question asking cannot be verified, use `source_missing / not_asked`, not `unanswered`.

Verdicts for batch interview ingest:

| Verdict | Meaning |
|---|---|
| `passed_with_batch_delta` | per-source deltas and batch synthesis are useful, cumulative coverage not claimed |
| `passed_with_partial_source_limits` | batch useful, but one or more sources have truncated/secondary limitations |
| `incomplete_batch_contract` | per-source rights, source isolation, or per-source audits missing |
| `incomplete_batch_coverage` | cumulative coverage is claimed but node-by-node ledger / required views fail |

Batch delta does not close cumulative coverage. A table titled `9-action matrix — batch delta`, `actants — batch delta`, or `new SI` cannot be used to mark all active P-nodes as covered. If cumulative coverage is not explicitly rendered through node-by-node ledger, output `delta-only verdict` rather than `coverage check: complete` or `batch ingest: passed`.

#### Batch Regression Guards 0.2.03

Rail 0.2.03 hardens `batch_interview_ingest`. These checks are blockers, not style preferences. If any required item is missing, the batch cannot receive `passed_with_batch_delta`; use `incomplete_batch_contract` or `incomplete_batch_coverage`.

| Guard | Required behavior | Failure label |
|---|---|---|
| Per-source rights table | Always render the full per-source rights table before synthesis | `batch_rights_table_missing` |
| BPM rights labels | Decompose compact labels such as `BPM-1/2/4/8/9`; route surveys to `BPM-1A` or `BPM-1B`, then assign BPM-addressed rights per source | `batch_bpm_rights_compact_fail` |
| Problem-node history | Do not collapse unaffected nodes into `Остальные N узлов`; either render every active P-node or label the section `problem_history_delta_only` | `batch_problem_history_collapsed_fail` |
| Macro-idea map | Use exact macro-idea schema even in batch; problem nodes are always `code + name`, with Cynefin, cross-source status, and next check | `batch_macro_map_schema_fail` |
| Actant map | Use exact polymorphic actant schema; include roles by problem, source trace, growth driver, energy/time barrier, zone/changeability; absent signal gets `no actant signal / source_check` | `batch_actant_map_schema_fail` |
| 9-action matrix | Use exact 9-action schema with `code + name`; no bare P-codes, slash clusters, catch-all rows, or generic cells | `batch_action_matrix_schema_fail` |
| Question audit | Run exact question-audit schema per source before any carryover backlog; source summaries use `source_missing / not_asked` when asking cannot be verified | `batch_question_audit_schema_fail` |
| Batch synthesis | If any cross-source conclusion is made, render a separate batch synthesis table | `batch_synthesis_table_missing` |
| Writeback status | Include paths/links for every created or updated evidence file; file names alone are not enough | `batch_writeback_paths_missing` |
| Verdict | Never write generic `batch ingest: passed`; choose the precise batch verdict, and downgrade to incomplete when contract rows are missing | `batch_generic_pass_fail` |

Minimum batch synthesis table:

| Batch synthesis | Source ingredients | Source-specific limits | Synthesis rights | Linked P-node / SI | Confidence | Next evidence |
|---|---|---|---|---|---|---|

Use this table only after per-source deltas are visible. If the table contains claims that were not supported by source-specific rows, mark them `inferred / needs_source_check` rather than confirmed.

#### Batch Exact-Schema Gate 0.2.04

Rail 0.2.04 closes the `table present but schema wrong` loophole. In batch mode, never mark a section as `present`, `passed`, or `completed` only because a table or heading exists. A section passes only when it uses the exact required columns, row-level `code + name` addressing, BPM-addressed source trace, and allowed statuses. If a table is useful but off-schema, write `schema_fail` and downgrade the batch to `incomplete_batch_contract`.

Required exact schemas:

| Section | Exact columns |
|---|---|
| Per-source rights | `batch item | source_id | respondent / role | source type | source status | BPM-addressed rights | processed layers | limitations | contribution | batch synthesis rights` |
| Problem-node history | `Problem node | Previous status | New status | Change type | Source trace | What changed | Next check` |
| Macro-idea evidence map | `Macro-idea / tension | Problem nodes | Cynefin / domain | Supporting sources | Divergent sources | Cross-source status | What must be checked next` |
| Polymorphic actant map | `Actant | Actant type | Roles by problem | Linked problems | Mechanism | Source trace | Growth driver | Energy/time barrier | Zone / changeability | Open check` |
| 9-action matrix | `Problem node | Actant | Source trace | Stabilise | Destroy | Shift | Create | Monitor | Conditional | Trigger | Request | Interaction | Best next action | Linked SI | Current ingest effect` |
| Batch synthesis | `Batch synthesis | Source ingredients | Source-specific limits | Synthesis rights | Linked P-node / SI | Confidence | Next evidence` |
| Question audit | `source_id | question_id | prepared question / intent | linked P-node / SI | asked status | answer status | evidence / answer summary | source trace | carryover / backlog` |
| Document writeback status | `action | file path / link | document role | change recorded | sync status | gap / fix` |

Row-level rules:

- `Problem node`, `Problem nodes`, `Roles by problem`, `Linked problems`, `Linked P-node / SI`, and `linked P-node / SI` must use `code + name`, not bare `P18`, slash clusters such as `P8/P14/P28`, or range groups.
- Combined statuses such as `confirmed/extended` are forbidden. Use one primary status in `New status` and explain nuance in `What changed`.
- `source-governance gap`, `Evidence gap`, or another meta-gap cannot stand in for a problem node unless it has an explicit P-code and name or is placed in a separate source-governance section.
- Delta tables still obey exact schemas. A heading such as `9-action matrix — delta` does not relax `code + name`, source trace, linked SI, or current-ingest-effect requirements.
- `present`, `recorded`, `completed`, `false confirmation prevented`, and similar self-reported labels do not count as validation. Validation must say `exact_schema_pass` or `schema_fail:<failure label>`.

Allowed batch verdicts are only:

| Verdict | When allowed |
|---|---|
| `passed_with_batch_delta` | exact schemas pass, useful per-source deltas exist, batch synthesis is valid, cumulative coverage is not claimed |
| `passed_with_partial_source_limits` | exact schemas pass and the only blocker is source limitation such as truncated / secondary / missing source |
| `incomplete_batch_contract` | any required table, exact schema, per-source audit, writeback path/link, BPM-addressed right, or allowed verdict is missing |
| `incomplete_batch_coverage` | cumulative coverage is claimed but node-by-node ledger or required cumulative views fail |

Forbidden verdict aliases: `batch processing status: completed_with_source_gaps`, `completed_with_source_gaps`, `completed_with_gaps`, `batch ingest: passed`, `passed`, `complete`, `coverage complete`, `false confirmation prevented: yes` as a substitute for verdict. If source gaps remain but exact schemas pass, use `passed_with_partial_source_limits`; if exact schemas fail, use `incomplete_batch_contract`.

#### Recovery Plus New Batch Gate 0.2.05

Rail 0.2.05 adds a hard contract for `recovery_plus_new_batch`: any pass that both recovers previously missing/truncated sources and ingests new sources in the same run. This mode is still a batch ingest and must satisfy all 0.2.04 exact-schema gates.

Minimum order:

```text
rail version check
-> recovery manifest
-> new-source manifest
-> per-source rights table for all sources
-> recovery-rights delta table
-> per-source deltas
-> exact problem-node history across all active nodes
-> macro-idea evidence map
-> polymorphic actant map
-> 9-action matrix
-> SI/BPV trace
-> per-source question audit
-> batch synthesis table
-> document writeback status with paths/links
-> allowed verdict
```

Required recovery-rights delta table:

| source_id | respondent / role | previous source status | recovered source status | evidence upgraded | old limitations superseded | remaining limitations | allowed BPM-addressed rights | invalidated prior gaps / claims | required re-check |
|---|---|---|---|---|---|---|---|---|---|

Rules:

- Recovered sources and new sources must be visibly separated before synthesis. A narrative block titled `что исправил source recovery` is not enough.
- `source rights upgraded without new IDs` is not a validation result. It must be backed by the recovery-rights delta table.
- A recovered source may close a previous source gap only for the exact claims and BPM-addressed rights shown in the table; old gaps remain open otherwise.
- New strategic findings, donor candidates, country models, forks, or strong SI do not substitute for macro-idea map, actant map, 9-action matrix, question audit, BPV trace, or writeback paths.
- If the pass creates new problem nodes, it must still render the full problem-node history exact schema for all active nodes, not only `new nodes` and `substantial changes`.
- `recovery_plus_new_batch` cannot use a custom success verdict such as `completed_with_new_strategic_fork`. If exact schemas pass and cumulative coverage is not claimed, use `passed_with_batch_delta`; if recovery/new-source limits remain, use `passed_with_partial_source_limits`; if any required layer is absent, use `incomplete_batch_contract`.
- If the output states an older Rail version than the current local skill version, it must mark `rail_version_drift` and cannot be accepted as a valid Rail pass.

Failure labels:

| Failure | Meaning |
|---|---|
| `recovery_manifest_missing` | recovered and new sources are not separated before synthesis |
| `recovery_rights_delta_missing` | recovered-source rights are not audited row by row |
| `recovery_claim_overreach` | a recovered source is used beyond its shown BPM-addressed rights |
| `new_source_rights_missing` | new sources lack the exact per-source rights table |
| `strategic_fork_substituted_for_rail_tables` | strategic conclusions replace required Rail tables |
| `recovery_plus_batch_verdict_alias_fail` | custom verdict used instead of allowed batch verdict |

#### Single-Source Follow-Up Gate 0.2.06

Rail 0.2.06 adds a hard contract for post-second single-source ingests, including `financial_follow_up_ingest`, `follow_up_ingest`, `duplicate_dedup_ingest`, `supplemental_source_ingest`, and other non-batch sources that update an existing Old Delivery evidence corpus. These are not batch passes, but they still must satisfy Old Delivery exact-schema requirements.

Minimum order:

```text
rail version check
-> single-source rights table
-> duplicate / parent-source handling when applicable
-> source delta summary
-> exact problem-node history or explicit problem_history_delta_only
-> macro-idea evidence map
-> polymorphic actant map
-> 9-action matrix or exact not_applicable matrix with reason
-> SI/BPV trace
-> question audit / source-request audit
-> document writeback status with paths/links
-> allowed single-source verdict
```

Required single-source rights table:

| source_id | parent_source | respondent / role | source type | source status | BPM-addressed rights | processed layers | duplicate handling | limitations | contribution | downstream evidence gates |
|---|---|---|---|---|---|---|---|---|---|---|

Required follow-up exact schemas:

| Section | Exact columns |
|---|---|
| Problem-node history delta | `Problem node | Previous status | New status | Change type | Source trace | What changed | Next check` |
| Macro-idea evidence map | `Macro-idea / tension | Problem nodes | Cynefin / domain | Supporting sources | Divergent sources | Cross-source status | What must be checked next` |
| Polymorphic actant map | `Actant | Actant type | Roles by problem | Linked problems | Mechanism | Source trace | Growth driver | Energy/time barrier | Zone / changeability | Open check` |
| 9-action matrix | `Problem node | Actant | Source trace | Stabilise | Destroy | Shift | Create | Monitor | Conditional | Trigger | Request | Interaction | Best next action | Linked SI | Current ingest effect` |
| SI/BPV trace | `Output / route | Linked P-node | Linked SI | Derived from | Source trace | Status | Confidence | Next evidence / gate` |
| Question / request audit | `source_id | question_id / request_id | prepared question / request intent | linked P-node / SI | asked/requested status | answer/delivery status | evidence / answer summary | source trace | carryover / backlog` |
| Document writeback status | `action | file path / link | document role | change recorded | sync status | gap / fix` |

Rules:

- `delta_only` does not permit collapsed rows such as `Остальные 23 узла`. Either show exact problem-node rows for affected nodes and label the section `problem_history_delta_only`, or render the cumulative node-by-node ledger.
- Every mentioned P-node must be `code + name`; bare lists such as `P3, P13, P15` and clusters such as `P1/P23` fail.
- Combined statuses such as `partially closed/refined` or `confirmed/refined` fail. Use one primary `New status` and put nuance in `What changed`.
- If a financial/source follow-up produces actions such as data dictionary, bridge, allocation policy, request, audit, or model check, the 9-action matrix is required. If truly not applicable, render an exact not-applicable matrix with source-traced reasons.
- A question audit for follow-up sources may be a request audit when the source is about promised packets, screenshots, audit package, balance, FinRED, or other downstream evidence. It must still use the exact schema.
- Duplicate Notion/page handling must state whether the duplicate is `not_registered`, `merged_into_parent`, or `registered_as_child`, and what evidence was or was not added.
- Physical, byte-level, archive-container, or near-identical duplication only governs storage and independent-source counting. Before returning a dedup verdict, Rail must separately verify `semantic_ingest_status`: whether the canonical parent content has already been read and materially routed into per-source rights, problem/evidence layers, SI/BPV, project-passport structure, and required downstream documents. If not, merge the duplicate into the parent and complete the semantic ingest from the canonical copy in the same pass; `merged_into_parent` is not a no-op verdict by itself.
- Document writeback by file name alone fails.

Allowed single-source verdicts:

| Verdict | When allowed |
|---|---|
| `passed_with_single_source_delta` | exact schemas pass, useful source delta exists, cumulative coverage is not claimed |
| `passed_with_follow_up_evidence_gap` | exact schemas pass, but named downstream evidence remains pending |
| `incomplete_single_source_contract` | source rights, exact schemas, question/request audit, writeback paths, or allowed verdict are missing |
| `incomplete_single_source_coverage` | cumulative coverage is claimed but node-by-node ledger / required cumulative views fail |

Forbidden single-source verdict aliases: `completed_with_pending_financial_evidence`, `completed_with_follow_up_gap`, `financial vocabulary: verified` as a verdict substitute, `quantitative cross-check: passed` as a Rail verdict, `duplicate source prevented: yes` as a verdict substitute, `passed`, `complete`, `coverage complete`. If the output states an older Rail version than the current local skill version, mark `rail_version_drift` and use `incomplete_single_source_contract`.

Failure labels:

| Failure | Meaning |
|---|---|
| `single_source_rights_missing` | required source-rights table is absent or off-schema |
| `single_source_exact_schema_fail` | one or more follow-up exact schemas are missing or off-schema |
| `single_source_collapsed_nodes_fail` | delta/cumulative problem history collapses unaffected nodes |
| `single_source_verdict_alias_fail` | custom or surrogate verdict used |
| `follow_up_request_audit_missing` | promised evidence / request audit is absent or off-schema |
| `duplicate_handling_trace_missing` | duplicate handling lacks parent/merge/evidence trace |

#### Mixed Contract Ingest Gate 0.2.07

Rail 0.2.07 adds a hard contract for `mixed_contract_ingest`: any pass that combines different source contracts in one run, such as `BPP governance event`, `BPP initiation/status event`, `BPM-SI convergence artifact`, `BPM Exchange / reuse synthesis`, `BPM-6 reference`, `reference-source gap`, `market ingest no-op`, or another non-homogeneous source class. The pass is valid only if it first separates the classes and rights before producing conclusions.

Minimum order:

```text
rail version check
-> mixed-contract preflight
-> source-contract rights matrix
-> BPP event ledger when BPP events exist
-> BPM-SI synthesis rights table when synthesis artifacts exist
-> BPM Exchange / reuse rights table when donor/reuse artifacts exist
-> reference/no-op ledger when reference gaps or no-op market ingests exist
-> source-class-specific deltas
-> exact problem-node history or explicit delta-only history
-> macro-idea evidence map
-> polymorphic actant map
-> 9-action matrix or exact not_applicable matrix
-> SI/BPV trace
-> document writeback status with full paths/links or explicit path_abbreviated_for_chat
-> allowed mixed-contract verdict
```

Required source-contract rights matrix:

| item_id | source class | object / source | registered as | allowed use | not allowed | BPM/BPP route | evidence strength | linked claims / nodes | required downstream check |
|---|---|---|---|---|---|---|---|---|---|

Required BPP event ledger:

| event_id | event type | date | role in project | allowed use | not allowed | linked decision / constraint | evidence requests generated | handoff / owner |
|---|---|---|---|---|---|---|---|---|

Required BPM-SI synthesis rights table:

| source_id | artifact | primary BPM | secondary / reference BPM | synthesis rights | fact-confirmation rights | claim status | linked P-node / SI | acceptance gate | next evidence |
|---|---|---|---|---|---|---|---|---|---|

Required BPM Exchange / reuse rights table:

| source_id | donor / pattern | reusable BPM pattern | transfer hypothesis | what transfers | what does not transfer | fact-confirmation rights for client | linked P-node / BPV | adaptation gate | next evidence |
|---|---|---|---|---|---|---|---|---|---|

Required reference/no-op ledger:

| item_id | class | pointer / location | status | allowed use | not allowed | gap reason | recovery action | impact on current pass |
|---|---|---|---|---|---|---|---|---|

Rules:

- BPP events do not receive `SRC-ID` and cannot create client factual proof by themselves. They may create project intent, constraints, decisions, handoff, and evidence requests only.
- `BPM-SI convergence artifact` may generate hypotheses, SI, BPV routes, decision criteria, and synthesis claims. It cannot confirm upstream client facts unless those upstream sources are traced separately.
- `BPM Exchange / reuse synthesis` may generate donor hypotheses, transfer logic, archetypes, and adaptation gates. It cannot confirm facts about the current client.
- `BPM-6 reference`, `Fuji reference`, `gdoc pointer`, empty market index, and similar objects must be marked as reference / source-check / no-op when direct source or market package is absent.
- A mixed pass cannot write `reuse donor check: completed` as a Rail verdict. Reuse completion is a section status, not the pass verdict.
- Problem-node deltas from synthesis/reuse must mark `claim status` as `hypothesis / synthesis / reuse_candidate / needs_client_evidence`, not `confirmed`, unless client evidence is separately traced.
- `Document writeback status` with abbreviated paths is allowed only if explicitly marked `path_abbreviated_for_chat`; otherwise full path/link is required.

Allowed mixed-contract verdicts:

| Verdict | When allowed |
|---|---|
| `passed_with_mixed_contract_delta` | all class-rights tables and exact downstream schemas pass, useful delta exists, cumulative coverage not claimed |
| `passed_with_mixed_contract_no_op` | class-rights tables pass and one or more source classes are valid no-op / reference gap |
| `incomplete_mixed_contract_ingest` | any class-rights table, exact downstream schema, writeback path/link, or allowed verdict is missing |
| `incomplete_mixed_contract_coverage` | cumulative coverage is claimed but node-by-node ledger / cumulative views fail |

Forbidden mixed-contract verdict aliases: `reuse donor check: completed`, `engineering synthesis classified: yes`, `market ingest: no-op` as whole-pass verdict, `processing status: completed`, `completed`, `passed`, `complete`. If the output states that no rule update is needed while a new source class is present without an existing contract, mark `mixed_contract_rule_gap`.

Failure labels:

| Failure | Meaning |
|---|---|
| `mixed_contract_rights_matrix_missing` | source classes are not separated before conclusions |
| `bpp_event_ledger_missing` | BPP events are described narratively without event ledger |
| `bpm_si_rights_missing` | synthesis artifact lacks synthesis/fact-confirmation rights |
| `bpm_exchange_rights_missing` | donor/reuse source lacks transfer and no-transfer rights |
| `reference_noop_ledger_missing` | reference gaps / no-op market sources lack ledger |
| `mixed_contract_claim_overreach` | BPP/SI/reuse/reference source is used as client fact evidence beyond rights |
| `mixed_contract_verdict_alias_fail` | custom or section-level status used as pass verdict |
| `mixed_contract_rule_gap` | pass introduces a new source class but claims no rule update is needed |

#### Standalone Source-Class Contracts 0.2.08

Rail 0.2.08 clarifies that `BPP event`, `BPM-SI convergence artifact`, `BPM Exchange / reuse synthesis`, `reference-source gap`, and `market ingest no-op` are standalone source-class contracts. They may appear alone in a private/specialized pass or together inside `mixed_contract_ingest`. `mixed_contract_ingest` does not define these classes; it only combines several standalone contracts in one run.

Standalone BPP event contract:

| event_id | event type | date | role in project | allowed use | not allowed | linked decision / constraint | evidence requests generated | handoff / owner | writeback path / link |
|---|---|---|---|---|---|---|---|---|---|

Allowed verdicts: `passed_with_bpp_event_delta`, `incomplete_bpp_event_contract`. Failure labels: `bpp_event_ledger_missing`, `bpp_event_claim_overreach`, `bpp_event_writeback_missing`.

Standalone BPM-SI synthesis contract:

| source_id | artifact | primary BPM | secondary / reference BPM | synthesis rights | fact-confirmation rights | claim status | linked P-node / SI | acceptance gate | next evidence | writeback path / link |
|---|---|---|---|---|---|---|---|---|---|---|

Allowed verdicts: `passed_with_bpm_si_synthesis_delta`, `incomplete_bpm_si_synthesis_contract`. Failure labels: `bpm_si_rights_missing`, `bpm_si_claim_overreach`, `bpm_si_acceptance_gate_missing`.

Standalone BPM Exchange / reuse contract:

| source_id | donor / pattern | reusable BPM pattern | transfer hypothesis | what transfers | what does not transfer | fact-confirmation rights for client | linked P-node / BPV | adaptation gate | next evidence | writeback path / link |
|---|---|---|---|---|---|---|---|---|---|---|

Allowed verdicts: `passed_with_bpm_exchange_delta`, `incomplete_bpm_exchange_contract`. Failure labels: `bpm_exchange_rights_missing`, `bpm_exchange_claim_overreach`, `bpm_exchange_adaptation_gate_missing`.

Standalone reference-source gap / market no-op contract:

| item_id | class | pointer / location | status | allowed use | not allowed | gap reason | recovery action | impact on current pass | writeback path / link |
|---|---|---|---|---|---|---|---|---|---|

Allowed verdicts: `passed_with_reference_gap`, `passed_with_market_no_op`, `incomplete_reference_noop_contract`. Failure labels: `reference_noop_ledger_missing`, `reference_claim_overreach`, `market_noop_reason_missing`.

Rules:

- A standalone class pass still runs Old Delivery downstream triage if it changes problem nodes, SI, BPV routes, actants, actions, evidence gaps, or project decisions.
- BPP events alone may be valid without SRC-ID. They still require event ledger and writeback path/link.
- BPM-SI synthesis alone may create SI/BPV hypotheses but cannot confirm client facts without upstream trace.
- BPM Exchange / reuse alone may create donor hypotheses and adaptation gates but cannot confirm client facts.
- Reference gap / market no-op alone may validly end as no-op, but must say what cannot be used, why, and what recovery action exists.
- If a pass contains exactly one of these classes, use the standalone verdicts above, not `passed_with_mixed_contract_delta`.
- If a pass contains two or more different source-class contracts, use `mixed_contract_ingest` and include each relevant standalone ledger inside it.

### Post-Mining Transition 0.3.21

Rail 0.3.21 is the current third family of the same unified Rail. It retains all prior rules and registers the public GitHub repository as canonical PP Presentation Kit upstream.

Trigger `post_mining_transition` when Ilya or an accepted project artifact states that mining, the meaningful-source collection, or the evidence corpus is complete / sufficient. The trigger is valid only for `Old Delivery` unless a separate New Delivery rule explicitly adopts it.

#### Run-To-Blocker Execution Contract 0.3.02

One post-mining launch is one continuous execution. Rail must start Gate 0 and continue automatically through every gate whose predecessor passed. A gate verdict is a transition event, not a stopping event.

Mandatory behavior:

- after Gate 0 receives `source_corpus_sufficient_for_synthesis` or `source_corpus_sufficient_with_nonblocking_gaps`, start Gate 1 in the same invocation;
- after Gate 1 receives `problem_model_consolidated` or `problem_model_consolidated_with_open_forks`, start Gate 2 in the same invocation;
- Gate 2 must attempt both the exact Estuarine table and the visual before any return;
- after a usable Gate 2 map exists, start the cumulative 9-action portfolio and SI/sub-BPV trace in the same invocation;
- after Gate 3, continue to Gate 4; stopping at Gate 4 is legitimate when audience / client decision / deliverable requires Ilya or another named owner;
- if execution was interrupted, the next Rail launch resumes from the first unattempted or failed gate using existing writeback state. It does not repeat passed gates unless evidence changed.

The following are not blockers:

- `nonblocking gaps`;
- `open forks`;
- proposed rather than owner-confirmed energy / time scores;
- some actants being `unplaced / source_gap`;
- lack of a specialized visualization tool when Mermaid / equivalent fallback is available;
- a large actant corpus, long table, or response-length pressure;
- the fact that the agent calls the output a `first pass`, `next pass`, or `next gate`.

Open forks must be represented as parallel change units, alternative actant positions, or conditional action routes. They are not silently resolved and do not stop mapping.

Response-length pressure is handled by writing the full tables into the existing project documents and returning a compact navigator in chat. It is never a methodological blocker.

Allowed real blockers:

- an upstream gate has an allowed `incomplete_*` / `reopen_mining_*` verdict and the missing evidence prevents the next layer from being constructed even provisionally;
- the project folder / required source cannot be accessed and the analysis cannot be reconstructed from available evidence;
- a visualization capability was actually attempted, failed technically, and the declared fallback also failed;
- Ilya explicitly says to stop after a named gate or run chat-only without continuing;
- Gate 4 requires a named human decision about audience, deliverable, or strategic fork before BPA readiness can be asserted.

Before any partial final return, render this exact table:

| Gate | Attempted | Status | Blocker evidence | Failure label | Writeback path / link | Resume action |
|---|---|---|---|---|---|---|

Rules for partial return:

- every predecessor marked `passed` must be followed by the next gate marked `attempted`; `pending` without an attempt is invalid;
- `next gate: X` is not a valid final state when X can be started;
- a generic `pending`, `next`, `not yet run`, `first pass complete`, or `continue later` is not blocker evidence;
- the partial return must use one exact failure label and show the source / tool / decision evidence behind it;
- if the blocker can be represented provisionally through `proposed_from_evidence`, `expert_estimate`, `unplaced`, conditional routes, or fallback visualization, continue rather than stop.

Failure labels:

| Failure | Meaning |
|---|---|
| `post_mining_gate_not_attempted` | a predecessor passed but the next gate was left pending without an attempt |
| `post_mining_self_split_fail` | the agent invented separate passes / runs without user instruction or a real blocker |
| `post_mining_false_blocker` | nonblocking gap, open fork, provisional score, corpus size, or response length was used to stop |
| `post_mining_partial_return_schema_fail` | partial return lacks the exact blocker table, evidence, failure label, writeback, or resume action |
| `post_mining_visual_not_attempted` | Gate 2 returned without attempting a proper visual and available fallback |
| `post_mining_resume_state_missing` | resumed execution repeated / skipped gates because prior writeback state was not inspected |

Required transition order:

```text
mining-complete signal
-> source closure audit
-> source-corpus sufficiency gate
-> cumulative problem-node consolidation
-> root / symptom / consequence separation
-> 5-8 macro-tensions when evidence supports that compression
-> Cynefin recheck on the consolidated problem model
-> Estuarine actant map
-> energy / time / zone placement and visual map
-> cumulative 9-action portfolio
-> selected action -> SI / САИ / storyline / storyboard link
-> sub-BPV / BPV route and 1-5 relationship score
-> client-decision and deliverable definition
-> BPA.01 readiness gate
```

Do not skip from `mining complete` to initiatives, pilots, target org structure, storyline, slides, or BPV. If any intermediate layer is absent, mark the exact failure and stop the downstream claim at that layer.

#### Gate 0: Source Closure

Run a final source audit before changing the project stage. Update the existing source register / evidence trace; do not create a parallel closure register when the project already has an equivalent document.

Minimum source-closure table:

| Source / source group | BPM-addressed rights | Accepted evidence | Limitations | Duplicate / superseded by | Blocking gap | Non-blocking gap | Closure decision |
|---|---|---|---|---|---|---|---|

Rules:

- `blocking gap` means the missing evidence could materially change a macro-tension, root-cause relation, Cynefin domain, strategic fork, or client decision.
- `non-blocking gap` may change confidence, appendix depth, or future enrichment but does not prevent synthesis.
- Duplicates are excluded with parent / supersession trace; they are not silently deleted.
- A source limitation remains visible after closure. `Corpus sufficient` never upgrades secondary or incomplete evidence into primary proof.
- Mining may be reopened only for a named blocking gap or a later material ingest; reopening does not erase the closure history.

Allowed source-closure verdicts:

- `source_corpus_sufficient_for_synthesis`;
- `source_corpus_sufficient_with_nonblocking_gaps`;
- `reopen_mining_for_named_blocking_gaps`;
- `incomplete_source_closure_contract`.

#### Gate 1: Consolidated Problem Model

Use all active problem nodes and their history. Do not consolidate only the latest source delta.

Minimum consolidation table:

| Macro-tension | Included problem nodes | Root / symptom / consequence | Causal links | Current Cynefin domain | Previous domain / change | Supporting sources | Divergent sources | Confidence | Strategic fork / next check |
|---|---|---|---|---|---|---|---|---|---|

Rules:

- Every problem node is written as `code + name`.
- Every merged, split, deprecated, or subordinated node keeps a visible history and destination.
- The target of `5-8 macro-tensions` is a usability heuristic, not permission to force unrelated problems together. Use a different count when evidence requires it and state why.
- Separate root mechanisms, symptoms, consequences, and unresolved competing explanations. A strategic fork is not silently resolved by the agent.
- Recheck Cynefin only after consolidation because new cross-source evidence may move a problem between `Clear / Complicated / Complex / Chaotic / Aporetic / mixed / unknown`.
- Cynefin is assigned to the problem or macro-tension, not to an actant in isolation. An actant may participate in problems from different domains.

Allowed problem-model verdicts:

- `problem_model_consolidated`;
- `problem_model_consolidated_with_open_forks`;
- `incomplete_problem_model_consolidation`.

#### Gate 2: Estuarine Actant Map

Build the Estuarine map from the accepted consolidated problem model. Actants explain what shapes the problem landscape; they do not replace problem nodes.

Core actant classes and subtypes:

| Core class | Valid subtypes / examples |
|---|---|
| `actor` | person; role; team; distributed group; professional community; coalition; collective identity; governance body; client; supplier; contractor; state / regulator; external decision-capable side |
| `constraint` | formal rule; decision-right boundary; budget / capacity limit; KPI / incentive; professional standard; norm / taboo; contract / regulation; access or information condition; reputation rule |
| `constructor` | recurring process; routine; ritual; governance mechanism; learning mechanism; coordination mechanism; platform / system; algorithm / model; recurring lead or decision handoff |

`resource` and `evidence carrier` may remain auxiliary roles in the evidence table, but they do not replace the three core Estuarine classes. When one label appears to be several classes, decompose it. Example: `founder` may be an `actor`; unilateral veto is a `constraint`; a weekly founder-led decision routine is a `constructor`. Do not spend the mapping session arguing for one permanent class.

Minimum post-mining actant table:

| Actant ID | Actant | Core class / subtype | Roles by problem | Linked problems | Mechanism | Change unit / intended shift | Source trace | Financial cost 1-5 | Authority 1-5 | Competence / attention 1-5 | Conflict 1-5 | Energy position 1-5 | Time 1-5 | Time basis | Influence 1-5 | Zone | Score status | Candidate actions | Open check |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Scoring rules:

- Scores apply to the named `Change unit / intended shift`, not to changing the whole person, organization, market, system, or abstract actant. If one actant contains several materially different shifts, split it into several map rows.
- `Financial cost`: 1 = no new budget / absorbed by current work; 2 = small local operating expense; 3 = cross-functional budget or meaningful procurement; 4 = major program / investment decision; 5 = capital-scale or externally financed change.
- `Authority`: 1 = local owner can decide; 2 = functional head; 3 = several functions / executive sponsor; 4 = CEO / board-level authority; 5 = shareholder, regulator, external center of power, or equivalent veto.
- `Competence / attention`: 1 = capability and attention are available; 2 = ordinary training / allocation; 3 = scarce cross-functional skill or leadership attention; 4 = new role / external expert / difficult capability build; 5 = capability is fundamentally absent or unavailable in the current market / horizon.
- `Conflict`: 1 = little resistance or loss; 2 = local friction; 3 = KPI, budget, or decision-right redistribution; 4 = coalition / status / identity loss; 5 = existential conflict, hard veto, or severe reputational / political risk.
- `Energy position` defaults to the maximum of the four energy components so one hard veto is not hidden by averaging. A different weighting is allowed only when stated explicitly.
- `Time` is time to a stable observable shift, not merely time to sign a decision. Record the basis as `authorization lead time / implementation time / stabilization-observation time`; the coordinate defaults to the longest of the three.
- `Time`: 1 = up to 2 weeks; 2 = roughly 2-6 weeks; 3 = roughly 1-3 months; 4 = roughly 3-12 months; 5 = beyond 12 months or outside the current project horizon. Adjust the calendar bands only by stating the project-specific horizon.
- `Influence`: 1 = local / weak system effect; 5 = system-wide or decisive effect.
- `Score status`: `proposed_from_evidence / expert_estimate / owner_confirmed / calculated / source_gap`.

Zone classification uses this precedence:

1. `counterfactual`: above the practical changeability boundary for the stated horizon, resources, and authority. This means `treat as landscape now`, not `impossible forever`.
2. `liminal`: change is possible, but not by the people constructing the map without permission, authority, budget, or external resource. Typical routes are `Request`, `Conditional`, and explicit escalation.
3. `volatile`: low time and energy but high influence / instability / reversibility. Stabilise before experimenting when uncontrolled movement can damage the system.
4. `workable`: changeable within the current horizon, authority, and resource envelope; eligible for action design and BPV / pilot consideration.
5. `unplaced`: evidence is insufficient to score; it cannot be treated as workable by default.

The practical changeability boundary is contextual. Every map must state the assumed project horizon, available authority, budget/resource envelope, and who confirmed or proposed the line.

#### Complete P-Node And Actant Population Contract 0.3.04

Gate 2 is a population map, not a twelve-point summary of macro-tensions. It must preserve two complete universes:

1. every active problem node from the accepted consolidated problem model;
2. every evidence-supported actant relevant to at least one active problem node.

`Every actant` does not mean every noun in the corpus. Include an entity when evidence supports that it shapes, reproduces, stabilizes, constrains, or can materially change at least one active P-node. Exclude pure source metadata, incidental mentions, and evidence carriers with no system mechanism, but record the exclusion reason.

Problems and actants remain different layers:

- energy/time coordinates belong to `actant × change unit`, not to the P-node;
- every active P-node must be visibly present as `code + full name` in the problem-actant coverage ledger and linked to one or more actant/change-unit points;
- P-nodes are not scatter points and must not be assigned time/energy coordinates; the visual plots actants only;
- if a P-node has no supported actant, record it in the coverage ledger as `no actant signal / source_check`; do not hide it inside a macro-tension;
- one actant may appear in several P-node facets when its role or change unit differs;
- do not turn a proposed solution into a current actant. Represent the current actor/constraint/constructor or the absence of a constructor; route creation of the future mechanism to Gate 3 `Create`.

Mandatory actant inventory ledger:

| Actant ID | Actant code + name | Evidence status | Core class / subtype | Linked P-nodes code + name | Change-unit IDs | Included in master table | Included in visual | Aggregated under | Exclusion / gap reason |
|---|---|---|---|---|---|---|---|---|---|

Mandatory problem-actant coverage ledger:

| Macro-tension | Problem node code + full name | Linked actant IDs + names | Relationship mechanism | Change-unit IDs | Coverage status | Gap / next check |
|---|---|---|---|---|---|---|

Rules:

- all active P-nodes require separate ledger rows; ranges and bare-code clusters fail;
- all included actants require separate inventory rows; a macro-mechanism cannot silently absorb child actants;
- `30/30` or another count is valid only when computed from the problem-actant coverage ledger;
- a compressed set of macro-mechanisms may be produced only as `executive Estuarine view` after the full master map passes;
- every executive macro-point must list member actant IDs and linked P-node IDs; it cannot replace child scores or links;
- group the coverage ledger by macro-tension so the complete P population remains readable without turning problems into map points;
- if the actant scatter is too dense, use labels, collision handling, or actant-only facets; do not omit actants or add P-nodes to the coordinate field;
- the authoritative output is the master actant table + complete actant inventory + macro-tension-grouped problem-actant coverage ledger + actant-only visual; executive view is derivative.

Failure labels:

| Failure | Meaning |
|---|---|
| `post_mining_problem_coverage_ledger_missing` | one or more active P-nodes are absent from the macro-tension-grouped problem-actant coverage ledger |
| `post_mining_actant_population_compressed` | evidence-supported actants were replaced by a smaller macro-mechanism set without inventory trace |
| `post_mining_macro_view_substituted_for_master` | executive view is presented as the authoritative Estuarine map |
| `post_mining_problem_as_actant` | a problem was assigned energy/time coordinates as if it were an actant |
| `post_mining_solution_as_actant` | a proposed future mechanism was used as a current actant instead of a Gate 3 action |
| `post_mining_actant_inventory_ledger_missing` | full actant inclusion/exclusion ledger is absent |
| `post_mining_problem_actant_link_missing` | an active P-node lacks linked actants or explicit source-check status |

#### Mandatory Visual Standard

Post-mining Estuarine mapping must produce both the exact table and a visual map. The visual does not replace the table.

Visual requirements:

- x-axis: `time to change`, 1-5, left to right;
- y-axis: `energy to change`, 1-5, bottom to top;
- show the practical counterfactual / changeability boundary;
- show or clearly label `volatile`, `workable`, `liminal`, and `counterfactual` zones;
- distinguish core classes by shape: `actor = circle`, `constraint = square`, `constructor = triangle`;
- distinguish zones by color and include a legend; do not use color as the only class encoding;
- label every point with `Actant ID + short name`; the full name and trace remain in the table;
- show polymorphic actants as split points / linked facets or decompose them into typed components; do not assign an arbitrary single shape;
- use opacity or border style for confidence / score status when the rendering tool supports it;
- visually inspect the output for unreadable labels, overlap, missing points, and mismatch with the table.
- plot only `actant × change unit` points; never plot P-nodes as if they had time/energy coordinates;
- keep all P-nodes, their full names, macro-tension grouping, linked actants, and relationship mechanisms in the adjacent problem-actant coverage ledger;
- when one canvas becomes unreadable, use collision handling or actant-only small multiples; do not remove actants to make the chart tidy;

Use an available visualization capability for a proper scatter map when possible. Gate 2 must record the attempt. If the runtime cannot render different point shapes, immediately use an embedded Mermaid quadrant / equivalent as a declared fallback with class prefixes and a legend; report `visual_encoding_limited` and keep the exact table authoritative. Do not return merely because the preferred visual tool is absent. A prose-only map is `estuarine_visual_missing`; no proper-tool attempt and no fallback attempt is `post_mining_visual_not_attempted`.

#### Gate 3: Actions, SI, and BPV Route

Only after actants are placed, build the cumulative 9-action portfolio. Preserve all existing 0.1.x / 0.2.x exact-schema and cumulative-coverage rules.

For each selected action, preserve this trace:

```text
macro-tension / problem
-> actant + map position + zone
-> action class
-> concrete intervention mechanism + evidence / gate
-> SI / САИ / storyline / storyboard node
-> initiative hypothesis
-> sub-BPV route
-> BPV route when the sub-BPV genuinely rolls up to a BPV
```

At this stage, prefer sub-BPV specificity. Do not create a new top-level BPV when the mechanism is a subtype, operation, or implementation route of an existing BPV.

Minimum sub-BPV x action score:

| Sub-BPV / BPV code + name | Linked action class | Linked actant | Linked problem / macro-tension | Relationship score 1-5 | Why | Source / method basis | Re-evaluation trigger |
|---|---|---|---|---|---|---|---|

Score meaning: `1 = incidental`, `2 = weak`, `3 = plausible`, `4 = strong`, `5 = defining / core mechanism`. This is a starting methodological estimate, not permanent canon. Re-evaluate after new ingests, pilot evidence, method changes, or the appearance of new sub-BPV / BPV entries.

#### Gate 4: Handoff To BPA

Post-mining does not become assembly-ready until the intended client decision and deliverable are defined. Record:

- audience / decision owner;
- decision the client must make;
- deliverable type;
- accepted SI for core story;
- appendix-only SI;
- mandatory calculations / organizational views;
- unresolved forks that must remain options rather than asserted decisions.

Allowed final post-mining verdicts:

- `ready_for_BPA.01`;
- `ready_for_BPA.01_with_open_forks`;
- `hold_before_BPA_source_closure`;
- `hold_before_BPA_problem_model`;
- `hold_before_BPA_estuarine_map`;
- `hold_before_BPA_client_decision`.

`hold_before_BPA_*` is not permission to stop before attempting the named upstream gate. It is valid only after the gate was attempted and the exact partial-return blocker table proves why provisional scoring, conditional routes, `unplaced`, or visualization fallback could not continue. `hold_before_BPA_client_decision` may validly stop after Gates 0-3 are complete when the remaining input is a named human decision.

Every 0.3.11 post-mining response must include a compact navigator:

```text
Post-mining navigator:
Rail version: 0.3.32
source closure:
problem model:
Cynefin recheck:
Estuarine table:
Estuarine visual:
9-action portfolio:
SI / sub-BPV trace:
client decision:
BPA readiness:
next gate:
```

Writeback uses the existing Old Delivery evidence set: source closure in `Реестр BPM-источников.md` / evidence trace; consolidation and Cynefin in `Карта проблем и Cynefin.md`; the table and embedded / linked visual in `Карта актантов.md`; selected actions and SI in Storyline-Storyboard; sub-BPV / BPV scores in `BPV route map.md`. Create no parallel files when an equivalent exists. Existing Old Delivery standing permission covers missing members of this evidence set; project path / link is still mandatory in `document writeback status`.

Post-mining failure labels:

| Failure | Meaning |
|---|---|
| `post_mining_source_closure_missing` | mining was declared complete without final source audit and sufficiency verdict |
| `post_mining_problem_consolidation_missing` | active P-nodes were not consolidated with history, root/symptom logic, and macro-tensions |
| `post_mining_cynefin_recheck_missing` | domains were copied from incremental mining without full-corpus recheck |
| `post_mining_actant_map_incomplete` | actants lack core type, problem links, energy profile, time, zone, source trace, or open check |
| `estuarine_boundary_context_missing` | counterfactual line lacks horizon / authority / resource assumptions |
| `estuarine_visual_missing` | table exists but no visual map or declared visualization blocker exists |
| `estuarine_visual_mismatch` | visual points, classes, labels, zones, or scores do not match the table |
| `post_mining_action_before_map` | actions / initiatives were selected before problem consolidation and actant placement |
| `post_mining_si_trace_missing` | selected action lacks SI / storyline / storyboard link |
| `post_mining_bpv_route_premature` | BPV / sub-BPV is proposed before problem-actant-action-SI trace |
| `post_mining_bpa_premature` | deck, org structure, target model, or pilot package starts before the post-mining gates pass |

### Old Delivery Pre-Final Self-Audit

Before outputting `verdict: complete` in any Old Delivery Rail/BPM pass after the second ingest, run this self-audit. If any item is `fail`, the verdict must be `incomplete` or `passed_with_fixes`, and the output must either be fixed before finalizing or list the exact failed items.

| Check | Pass condition | Failure label |
|---|---|---|
| Rail version | current output follows the latest local Rail version, not an older stated version | `rail_version_drift` |
| Source register | source register exists and uses BPM-addressed labels | `source_register_missing` |
| Node-by-node coverage ledger | every active P-node is checked separately across problem history, macro-map, actant map, 9-action matrix, and SI/BPV trace, with exact separate columns | `node_coverage_ledger_missing / node_coverage_ledger_schema_fail` |
| Macro-idea map | exact required columns including Cynefin, supporting/divergent sources, cross-source status, next check; every listed problem appears as code + name, never range-only | `macro_map_schema_fail` |
| Problem history | exact required columns: previous status, new status, change type, source trace, what changed, next check; no combined statuses like `confirmed/extended` | `problem_history_schema_fail` |
| Actant map | exact polymorphic schema, code+name problem links, source trace, growth driver, energy/time barrier, zone/changeability; absent nodes get explicit `no actant signal / source_check` rows | `actant_map_schema_fail` |
| Actant typing | people/roles/functions/mechanisms are not merged or assigned non-canonical types without explanation | `actant_type_fail` |
| 9-action matrix | active nodes are covered with code+name, concrete cells, no unexplained ranges, no bare-code clusters, no catch-all rows | `action_matrix_schema_fail` |
| Question audit | prepared brief or carryover backlog uses the exact full question audit schema, code+name linked nodes, and separates `not_asked` from `unanswered` | `question_audit_schema_fail` |
| SI/BPV trace | every active P-node has a cumulative visible row/grouped row with code+name, BPM-addressed source trace, and explicit route/gap; delta-only tables do not count | `si_bpv_trace_coverage_fail` |
| Writeback | document writeback status includes paths/links for every created/updated file and sync gaps | `writeback_trace_fail` |
| Batch ingest contract | batch mode includes per-source rights, decomposed BPM labels, per-source question audits, batch synthesis table when synthesis exists, writeback paths, and precise verdict | `batch_rights_table_missing / batch_bpm_rights_compact_fail / batch_synthesis_table_missing / batch_question_audit_schema_fail / batch_generic_pass_fail` |
| Batch exact-schema gate | every batch table uses exact required columns, code+name rows, allowed statuses, and allowed verdict only; table presence alone is not pass | `batch_exact_schema_gate_fail / batch_verdict_alias_fail` |
| Recovery plus new batch | recovered and new sources are separated, recovery-rights delta is rendered, old gaps are explicitly superseded or left open, and strategic findings do not replace required Rail tables | `recovery_manifest_missing / recovery_rights_delta_missing / recovery_claim_overreach / strategic_fork_substituted_for_rail_tables / recovery_plus_batch_verdict_alias_fail` |
| Single-source follow-up | post-second follow-up / financial / duplicate-dedup source has source rights, exact delta schemas, no collapsed nodes, request audit, writeback paths, and allowed verdict | `single_source_rights_missing / single_source_exact_schema_fail / single_source_collapsed_nodes_fail / follow_up_request_audit_missing / single_source_verdict_alias_fail` |
| Mixed contract ingest | heterogeneous source classes are separated in rights matrix, BPP/SI/reuse/reference/no-op ledgers exist where applicable, and no class is used beyond rights | `mixed_contract_rights_matrix_missing / bpp_event_ledger_missing / bpm_si_rights_missing / bpm_exchange_rights_missing / reference_noop_ledger_missing / mixed_contract_claim_overreach / mixed_contract_verdict_alias_fail` |
| Standalone source-class contracts | BPP event, BPM-SI synthesis, BPM Exchange/reuse, reference gap, and market no-op can run alone with their own ledger, rights, writeback, and verdict | `bpp_event_ledger_missing / bpm_si_rights_missing / bpm_exchange_rights_missing / reference_noop_ledger_missing / source_class_standalone_contract_missing` |
| Post-mining transition | a mining-complete signal runs continuously to the first real blocker: source closure, cumulative problem consolidation, full-corpus Cynefin recheck, complete active-P and relevant-actant population ledgers, exact Estuarine table + attempted actant-only visual/fallback, cumulative 9-action portfolio, SI/sub-BPV trace, client-decision gate, and post-mining navigator; passed gates automatically start successors | `post_mining_source_closure_missing / post_mining_problem_consolidation_missing / post_mining_cynefin_recheck_missing / post_mining_actant_map_incomplete / post_mining_problem_coverage_ledger_missing / post_mining_actant_population_compressed / post_mining_macro_view_substituted_for_master / post_mining_solution_as_actant / post_mining_actant_inventory_ledger_missing / post_mining_problem_actant_link_missing / estuarine_visual_missing / post_mining_gate_not_attempted / post_mining_self_split_fail / post_mining_false_blocker / post_mining_partial_return_schema_fail / post_mining_visual_not_attempted / post_mining_bpa_premature` |

This self-audit should be shown compactly when useful, and must be used internally even when not shown. A final line such as `shown in SI/BPV trace: all material deltas; unchanged nodes explicitly gated` is not sufficient unless the actual SI/BPV table visibly contains those nodes or grouped rows.

Never mark a self-audit item as `pass` from the existence of a table alone. The pass condition is row-level compliance. A table that exists but uses bare codes, ranges, merged status fields, or catch-all groups must be marked `fail` with the relevant failure label.

When classifying actants, do not assign `constructor` to a person merely because they create or sponsor a system. A person or role such as CFO, CEO, manager, or project owner remains `actor / decision-owner`; the `constructor` is the system, routine, policy, model, report, or process they create or operate.

### Reuse-Check After Third Ingest

After the third significant BPM ingest, Rail must run a compact reuse-check with both archetypes and concrete donors. Archetype-only reuse is incomplete.

Minimum table:

| Archetype / route | Concrete donor project / unit | Why donor | Transferable asset | What does not transfer | Evidence needed | Status |
|---|---|---|---|---|---|---|

Use concrete projects, archive passports, knowledge units, cases, method derivatives, or source-limited donor candidates where possible. If no concrete donor can be named, mark `concrete donor source gap` and state which archive / 8ka / 5ka / 2ka / 1ka source home must be searched. Do not present a donor as applicable without explaining why it is a donor and what cannot be transferred.

### Universal Assembly Challenge Subagents

When assembly uses a coding membrane, factor model, segmentation, clustering, market sizing, JTBD, CJM / КПО, service blueprint, entity map, process map, unit economics, or any other method axis that converts raw evidence into slide claims, Rail must require a universal challenge pass before treating the output as ready for `BPA.06` core deck assembly.

This is not BTK-specific. BTK is only the first strong source-case for the pattern:

```text
framework / coding dictionary
-> acceptance or readiness layer
-> subagent challenge
-> calculation / report
-> slide claims + appendix trace
```

Mandatory subagent roles:

| Subagent | Genre | Checks | Return format |
|---|---|---|---|
| `method-architecture critic` | methodological challenge | Does the method axis actually fit the project archetype, source type, and decision question? Are the layers separated correctly? | `verdict`, `critical risks`, `required method changes`, `accepted logic` |
| `statistical / model-validity critic` | quant / model QA | Is the sample, scale, feature count, aggregation, PCA / clustering / sizing / scoring logic defensible? What must not be claimed statistically? | `run / do-not-run`, `model caveats`, `minimum fixes`, `appendix needs` |
| `coding-protocol / MCE critic` | coding discipline | Are coding rules explicit, mutually distinguishable, source-grounded, and repeatable? Are no-signal, weak signal, secondary layer, and mandatory barrier separated? | `codebook gaps`, `classification risks`, `required fields`, `examples needed` |
| `evidence-chain critic` | source-rights QA | Can every claim trace back to source, quote / fact, code, inference, and allowed slide role? Are source rights overstated? | `claim -> evidence status`, `unsupported claims`, `caveats`, `appendix trace` |
| `operational applicability critic` | execution / adoption QA | Does the slide claim survive an operating filter: owner, data, SLA, process, system, last mile, responsibility, decision gate? | `execution gaps`, `owner/data/SLA risks`, `BPV/BPO implications`, `no-overpromise notes` |
| `client-decision readability critic` | executive readability | Can a client understand what decision is being asked, what choices exist, what risks remain, and what happens next? | `decision clarity`, `reader friction`, `rewrite priorities`, `core vs appendix split` |
| `red-team / alternative-explanations critic` | critical challenge | What else could explain the pattern? What did the team ignore? What source or SI may be missing? | `alternative explanations`, `missing SI/source`, `stress-test questions`, `stop/go` |

If multi-agent tools are available, launch these as distinct subagents or equivalent named reviewers. If they are not available, Rail must still run the same named perspectives sequentially and label the result as `simulated subagent challenge`. Do not skip the challenge merely because the runtime lacks a subagent tool.

Minimum challenge packet in Rail output:

```text
Assembly challenge:
status: not_started / running / passed / passed_with_fixes / blocked
subagents:
| role | verdict | critical issue | required fix before BPA.06 | appendix / caveat need |
overall decision:
```

Rail must block or downgrade assembly readiness when any mandatory subagent returns a critical issue that affects evidence rights, method validity, client decision clarity, or execution feasibility.

### Universal BPV-QA routing

Whenever Rail produces, receives, or reviews an implementation result routed to `BPV-xx` / `BPV-xx.x`, it must invoke `multi-perspective-review` in `bpv_qa` mode before marking the BPV result accepted, reusable, adopted, or case-proven.

Required order:

```text
exact BPV-xx.x route
-> common BPV invariants
-> canonical QA profile from 5-ka
-> linked instructions / paired cases / transfer rules from 8-ka
-> artifact-specific QA skill when applicable
-> CKP / artifact / handoff / adoption / paired-case verdict
-> repair and repeat QA
```

Do not create or require a separate QA skill per BPV by default. The universal router loads declarative profiles. Specialist QA skills are reserved for genuinely different artifact mechanics such as presentations, commercial proposals, calculations, workbooks, dashboards, CRM/data specifications, org models, and AI/RAG systems.

If Rail can identify only the upper family and not the exact sub-BPV, return `route_ambiguous` and keep the BPV result on hold. A broad `BPV-04 — Управление продажами` review cannot accept `BPV-04.4 — Подготовка КП и ТКП`. The Rail receipt must name the exact code and title, QA profile version, loaded knowledge units, specialist QA verdict, adoption evidence status, paired-case status, defects, and repair route.

## Reuse / Method-Derivative Check

Rail must be able to notice when project evidence may reuse data, model logic, slide logic, field questions, dashboard schema, or a method derivative from another project. This is a leakage check inside Rail and BPM Exchange, not a separate heartbeat requirement.

Run the check only when one of these triggers exists:

- Ilya explicitly asks Rail / donors / reuse / method derivative questions;
- project enters pre-defense or client-defense preparation;
- 3-4 significant ingests have accumulated and at least one touches `BPM-1A`, `BPM-1B`, `BPM-2`, or `BPM-3`;
- a major BPM source is completed: processed survey, interview block, raw-pack, dashboard, export, data request, or client document with management meaning;
- a status signal changes the project gate.

Do not run the check for every subpassport update, minor scope edit, ordinary task status change, single small note without BPM meaning, or administrative sync. Avoid using project heartbeats as the primary trigger: a project may already have another meaningful heartbeat, and heartbeat failure must not block reuse governance.

Significant ingest means:

- new meeting or interview;
- processed survey;
- raw-pack;
- client document with management meaning;
- dashboard / export / data request;
- status signal changing the project gate.

Use this machine operation:

```text
family/source expansion -> alias expansion -> match -> applicability -> transferable operation / method derivative -> data sufficiency -> verdict
```

`family/source expansion` is mandatory before a negative or top-K donor verdict. The agent must find plausible donors even when no one names the exact project. Do not run one broad noisy Vault search and stop. First translate the current project signal into a compact family query, then search curated reuse homes.

For example, a project signal such as `МГ: собственная розница, мясо/колбасная категория, правильная корзинка, чек, повтор, loyalty, SKU, конечный потребитель` must produce family queries such as:

- `food retail / branded retail / фирменная розница`;
- `loyalty / программа лояльности / карта лояльности`;
- `basket / корзина / структура чека / глубина чека`;
- `LTV / повтор / отток / check economics`;
- `колбасная / мясная / замороженная продукция`;
- anti-patterns such as `розница без корзины`, `traffic-without-basket-economics`.

Search these family queries in high-signal source homes before scanning the whole Vault:

- `04-производство/Архивные проекты/00-Индекс архивных проектов.md` as the reuse visibility scaffold;
- 4ka archive passports linked from the index, including `source_limited` and derivative cases unless explicitly excluded;
- 8ka knowledge units and knowledge-check batches;
- 5ka post-archive tunnel / method batches and antipat­tern tables;
- 2ka case derivatives and content case folders;
- 1ka training units when they preserve reusable exercises.

The archive index is not merely a navigation file. It is the first source of truth for whether an archived project is visible for reuse. If a project is not fully classified but is not explicitly excluded, Rail must keep it in the candidate universe as `reuse_visible / needs_classification` or `reuse_visible / source_limited` rather than silently dropping it.

Only after family/source expansion, expand exact aliases:

- exact names and likely aliases mentioned by people, e.g. client names, abbreviations, old brand names, source PDF names;
- archive project index and passports;
- 2ka case derivatives and content cases;
- 8ka knowledge units;
- 5ka post-archive tunnel / method batches;
- 1ka training units when they preserve a reusable exercise name;
- source terms in Russian and English: category, business model, channel, object of analysis, method name, antipat­tern.

If a person names a donor candidate after the first pass, treat that as evidence of a failed family/source or alias expansion, not as a new unrelated idea. Re-run the donor check on both family terms and exact names, then record the miss cause in the project Rail/status or reuse packet when relevant.

C1/C2 do not own deep donor evaluation. They may confirm parsed facts such as project, BPM, channel, data type, object of analysis, gate, SKU depth, buyer id, repeat purchase, channel, and margin/proxy availability. The machine runs the donor check; C3/C4/Ilya decide whether the route is accepted.

Track reuse state by `BPM / theme / route`:

| State | Meaning | Rail behavior |
|---|---|---|
| `open` | enough evidence to evaluate, not decided yet | run compact check and propose verdict |
| `confirmed` | reuse route accepted | stop proposing the same route; only update on substantial new data or gate change |
| `rejected` | reuse route declined | record refusal reason and retry conditions |
| `weak_evidence` | signal exists but is below proposal threshold | do not propose; observe until stronger evidence appears |
| `not_needed` | observer says methodological innovation / reuse is unnecessary | freeze until gate change, new substantial data, or explicit review |

Output in Russian-readable YAML or table form. English machine tags may remain as optional technical layer, but Russian fields are mandatory.

Separate:

- `data reuse`: old source data can be reused or compared;
- `model reuse`: analytical model / clustering / scoring logic can be adapted;
- `method derivative`: a derivative form of an existing BPM / method / SI that changes how raw BPM material is organized, represented, and shown to the team or client.

A method derivative is not `method_candidate`. Record at minimum: project source, project of application, source BPM, related BPMs, what transfers, what does not transfer, first repeated application / confirmation project, status, and current reuse state.

## Preflight

Before reading broadly, state:

```text
rail preflight:
project:
mode:
scope:
current chat:
current chat role:
rail allowed here: yes/no
ClickUp attribution: verified / candidate / clickup_sync_gap
ClickUp container: workspace / space / folder / list / Project task / URL
ClickUp mode: read-only / exact change set separately approved
expected sources:
methodology sources:
allowed actions:
forbidden actions:
will edit files: no / after accept only
```

If the current directory is inside a 4ka project, use that project. If not, ask which 4ka project to inspect unless it is named in the request.

Before continuing, determine the current chat role from `Карта-чатов.md`, реестр чатов, карта коммуникаций, or the nearest project chat control artifact.

Allowed current chat roles:

- `main штаб-проекта`;
- `main internal-pp-сборка`.

Forbidden current chat roles:

- `auxiliary субпроектный чат`;
- `service/subject working chat`;
- `unknown`.

If the role is forbidden or unknown, stop after preflight and output:

```text
Rail is not allowed from this chat.
current chat role:
allowed launch points:
- Штаб проекта
- Внутренний PP / проектная сборка
what to do:
```

Do not run the inspection until the request is made in one of the allowed main chats or Ilya explicitly changes this rule.

## Source Order

Read only what is needed, but in this order.

### 1. Project Control Sources

Find and inspect:

- native ClickUp project container through `clickup-mcp-router`: exact workspace / space / folder / list / `Project` task, IDs and URLs; compare it with any attribution already stored in the project card, chat map, or administrative scale;
- `Админ-шкала/Карта-чатов.md`, `Карта-чатов.md`, реестр чатов, карта коммуникаций;
- project card / `00-Карточка проекта.md`;
- admin scale files;
- project tracker, task tracker, status notes, daily/project logs if directly used by the project;
- штаб artifacts or sections;
- subpassports and start messages for track/service working contours only.

### 2. BPM/BPP Project Sources

Find the project's BPM/BPP scope and movement:

- BPM registry or status block;
- BPP / administrative BPM files;
- scope table;
- stage gates, C2 acceptant, owner, status, inputs, outputs, next action, deadline fields;
- history/changelog sections related to BPM/BPP updates.

### 3. Current 4ka Methodology Sources

Before claiming methodology compliance, locate current 4ka methodology sources. Prefer project-linked references first, then nearby 4ka canonical files.

Search narrowly for:

- `_Каталог-BPM`;
- `BPM`;
- `BPP`;
- `Административные`;
- `Шаблон-блока-BPM-статус`;
- `fullkit`;
- `readiness`;
- `C2`;
- `акцептант`;
- methodology history / changelog / update notes.

If sources are not found, say `methodology source gap` and do not invent the canon.

### 4. Chat Evidence

Use the project chat map to inspect all chats/contours in the project, not just the current chat:

- `main штаб-проекта`;
- `main internal-pp-сборка`;
- auxiliary subject chats such as data/MIS/economics, interviews/HR, patient path, market/strategy;
- any extra chats that appeared in project artifacts.

This all-chat inspection is allowed only after Rail has been launched from an allowed main chat. Auxiliary/service chats may be inspected as evidence, but they are not valid launch points.

For each chat, determine:

- status;
- role;
- linked BPM/scope;
- intended inputs/outputs;
- actual current work;
- decisions that must return to штаб;
- stale status;
- missing subpassport only for auxiliary/service track chats, never for `Штаб проекта` or `Внутренний PP / проектная сборка`;
- tasks, blockers, owners, dates, next actions.

## Rail Reconstruction

When reconstructing, build two rails side by side:

- `intended rail`: what the project artifacts and 4ka methodology say should happen;
- `actual rail`: what the current artifacts, chat map, tasks, and evidence show is happening.

Classify drift:

- `status-drift`: status in artifacts lags behind actual work.
- `clickup-attribution-gap`: the active 4ka project has no verified native ClickUp container attribution in the Rail preflight.
- `clickup-container-drift`: the recorded ClickUp space/folder/list/Project-task route no longer matches the physical native hierarchy or resolves to a different project.
- `stage-drift`: project phase/subphase is unclear or stale.
- `scope-drift`: work has entered or left scope without штаб decision.
- `bpm-drift`: BPM exists in scope but lacks movement, owner, inputs, outputs, or next action.
- `storyline-storyboard-gap`: active mining / INIT / PLAN project already has BPM-scope plus a first significant BPM source or BPM-candidate source / raw-pack / interview / org meeting / database / reuse / cross-contour document that can produce a future slide, but lacks a live BPM Storyline-Storyboard or it does not grow from each BPM.
- `problem-map-cvz-gap`: active non-classical 4ka project without an explicit mining phase has enough track / initiative / meeting evidence to synthesize root problems, but lacks a `Карта проблем` / ЦВЗ-slice or the existing map is not connected to decisions, metrics, owners, Storyline/Storyboard, and no-op/task handoff rules.
- `bpm-candidate-source-gap`: a source has clear BPM meaning, but the project did not classify it as official BPM or BPM-candidate source and did not run possible BPM increments -> SI -> Storyline-Storyboard update/no-op.
- `diagonal-ingest-gap`: a source arrived through another contour, department, reuse lane, archive, or strategic document and may feed a 4ka project, but no routing question or ingest/no-op decision was recorded.
- `dynamic-rail-reference-gap`: a dynamic output from another skill or rail, such as a slide hypothesis, SI/SIEF proof group, visual exhibit, battlecard, commercial argument, content angle, benchmark pattern, or knowledge candidate, should refer to a live rail/database/artifact but has no target rail, no target artifact, no BPM-SI router handoff, and no explicit no-op reason.
- `stale-dynamic-reference`: a skill, packet, storyboard, rail note, or project artifact points to an outdated rail/database/artifact name, stale BPM/SI route, removed skill, renamed artifact, or superseded project home.
- `bpp-drift`: administrative/process rail does not match current methodology.
- `new_delivery_admin_preflight_missing`: New Delivery was classified or stopped without checking the passport, charter, and all nine administrative-scale components.
- `admin_scale_checked_as_source_only`: the administrative scale was read but not gate-checked or routed through the canonical `admin` logic when normalization was needed.
- `explicit_passport_create_permission_ignored`: Ilya explicitly authorized passport/charter/scale creation or writeback, but the pass stopped at an artifact gap, asked again, or created no canonical landing.
- `chat-drift`: chat role/status/handoff is missing or stale, or an auxiliary/service track chat lacks its required subpassport. Main chats do not require subpassports.
- `task-drift`: task lacks owner, date, next action, or implementation reason.
- `handoff-drift`: decision stayed in a working chat instead of returning to штаб.
- `methodology-source-gap`: current methodology source was not found.
- `no-op`: checked and no change is needed.

## Methodology Compliance

For each material issue, use this evidence pattern:

```text
project fact:
methodology requirement:
drift:
management consequence:
proposed repair:
needs accept:
```

Check at minimum:

- current stage/substage vs 4ka project rail;
- BPM in scope vs active BPM movement;
- status vocabulary and gates;
- C2 / acceptant requirements as process metadata, not as chat-local blockers;
- owner / date / next action completeness;
- inputs and outputs per BPM;
- readiness/fullkit requirements if applicable;
- штаб vs working contour separation;
- whether factual project practice suggests the rail itself should be redesigned.

## BPM-12 / AI-RAG Attribution Gate

When a 4ka project activates `BPM-12`, `Minority Report`, AI/RAG-readiness, RAG stop/go, corpus preparation, prototype assessment, or pilot assessment, Rail must check a separate methodology attribution gate before accepting the pass as ready for штаб decision.

Required attribution:

- `CORD-PDCA` as the governing management cycle;
- local skill `cord-pdca` as the operational contract;
- domain 6 AI-course standards as the training and knowledge reference;
- relevant PP precedent when known, such as ИРИДИ, as an analogy source, not as client evidence.

Required BPM-12 output separation:

- `подтверждённое evidence`;
- `вывод агента`;
- `source gap`;
- `answerability gap`;
- `AI/RAG hallucination or overreach risk`;
- `management delta`;
- `owner stop/go required`.

If a BPM-12 pass evaluates AI/RAG feasibility without this attribution and separation, mark `bpm12_methodology_attribution_gap` and do not treat the pass as sufficient for corpus, prototype, pilot, vendor, or project-wide status decisions. Activation of BPM-12 never authorizes an RAG pilot by itself.

## Output Format

Keep output compact unless Ilya asks for detail.

```text
rail preflight:
project:
mode:
scope:
chat map:
ClickUp attribution:
ClickUp container:
ClickUp mode:
methodology sources checked:
project sources checked:
not doing:

BPA assembly navigator: # only when assembly_mode: yes
current step:
already passed:
next step:
short assembly summary:

BPA assembly pass: # only when assembly_mode: yes
| BPA | status | evidence artifact | gap | next action |

Assembly challenge: # required for method-heavy assembly
status:
| role | verdict | critical issue | required fix before BPA.06 / defense | appendix / caveat need |
overall decision:

Project rail:
| layer | intended rail | actual rail | drift | next action |

Chat contours:
| chat | role | status | scope | current work | штаб handoff |

BPM/BPP movement:
| item | expected | actual | blocker/drift | next action |

Dynamic rail references:
| item | source skill/packet | candidate rail | target artifact/database | current status | drift/no-op | next action |

Tasks:
| task | owner | date | source | status | missing |

Methodology compliance:
| area | project fact | current requirement | drift | repair |

Repair plan:
must fix now:
good to fix:
leave as-is:

Accept gate:
```

If nothing is stale:

```text
Rail: отставаний по рельсе не найдено.
Checked:
Residual risk:
```

## After Accept

Patch only accepted files and explicitly accepted missing canonical artifacts. Prefer existing project homes and update an existing project passport before creating anything. If the accepted scope includes a missing passport / charter / administrative scale, create at most one canonical passport at the project root and keep the charter and all nine administrative-scale components in that same artifact unless the project already has an established canonical split:

- chat map;
- project card;
- admin scale;
- BPM/BPP status blocks;
- task tracker;
- штаб notes.
- project `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md`;
- project `Карта проблем` / ЦВЗ-срез or the nearest existing Storyline / project-card block when the project has no separate problem-map file;
- `Матрица BPM — SI` or other existing BPM-SI rail/database artifact, when the accepted repair is about dynamic SI/SIF/slide reference maintenance.

After editing:

- verify YAML/frontmatter with Ruby safe YAML when relevant;
- verify Obsidian-safe Markdown when editing Vault `.md`: no local absolute markdown links, `file://`, URL-encoded `%20` paths, or `#`-tags in frontmatter; internal Vault navigation should use `[[wikilink]]` / `[[wikilink|alias]]` in body text;
- re-read changed sections;
- report changed files and what was verified.

Use Ruby frontmatter check:

```bash
ruby -e 'require "date"; require "yaml"; p = ARGV[0]; s = File.read(p); fm = s[/\A---\n(.*?)\n---\n/m, 1]; YAML.safe_load(fm, permitted_classes: [Date, Time, Symbol], aliases: true) if fm; puts "frontmatter ok"' path/to/file.md
```

## Guardrails

- Do not turn Rail into a content plan, client-facing report, or methodology rewrite unless Ilya asks.
- Do not launch Rail from service/auxiliary chats. Use them as evidence only when Rail is launched from штаб or internal PP assembly.
- Do not silently change the project rail. First show drift and repair plan.
- Do not treat absence of evidence as failure. Mark it as a source gap.
- Do not collapse archive/Old Delivery, current delivery, and monthly delivery into one project layer unless Ilya explicitly says they are one continuous project.
- Do not mechanically route every signal to every department. Rail is a 4ka operating inspection skill.
- Do not automatically update dynamic rail references just because another skill suggested them. Show the reference candidate, target rail, target artifact/database, source evidence, and no-op alternative; update only after Ilya accepts.

## Writeback / Approval Gate

Rail is high-risk because it can change project status, owners, next steps, stage gates, trackers, project cards, Daily Notes, and downstream 1/2/5/8 signals.

Default output is drift + repair plan. Do not change a project rail, status, owner, deadline, scope, tracker, project card, or departmental landing without explicit approval from Ilya for the exact change set. If the evidence is partial, mark source gaps and ask instead of repairing silently.

## Global Structural Artifact Contract

Rail inherits the cross-cutting contract in `~/.codex/AGENTS.md` for every Problem Map, issue/hypothesis tree, Evidence Separation Ledger, Evidence trace, source-to-node matrix, Mermaid analytical visual, Storyline-Storyboard, metric tree, and dimension architecture. Existing Rail exact schemas remain stricter and win where they add fields. Frappe/Quartz are nonblocking mirrors; the applicable BPP/BPA file and physical project evidence govern the row. A new ingest must land as a visible delta before any full map/storyline rewrite, and methodology claims must never fill a missing client source.
