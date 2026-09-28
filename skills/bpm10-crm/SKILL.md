---
name: bpm10-crm
description: Analyze, design, document, and validate B2B CRM architecture using the Paper Planes BPM10 methodology. Use when Codex needs to audit an existing CRM, turn interviews and sales processes into a target CRM model, define entities and Bitrix24 mappings, design Reach/React/Refresh/Re-Engage funnels, prepare CRM cards and functional requirements, separate CRM from ERP/BI/service systems, build a CRM governance model, or prepare a client/integrator handoff package and Miro scheme.
version: 0.1.5
line: BPM-10 / CRM analysis / target CRM architecture
source: Dior handoff package, hardened for Codex/Vault DLP and writeback rules
supports_bpm:
  primary: [BPM-10]
  required_secondary: [BPM-2, BPM-4, BPM-11]
  optional_secondary: [BPM-3, BPM-5, BPM-6, BPM-8, BPM-9]
can_consume:
  - organizational interviews
  - customer interviews
  - CRM exports and screenshots
  - current funnel/stage maps
  - role model and regulations
  - BPM-4 signals
  - BPM-11 object and SoR logic
  - integrator specifications
can_produce:
  - CRM target architecture
  - entity list
  - funnel and smart-process list
  - entity cards
  - functional requirements
  - system-boundary map
  - CRM governance model
  - CRM commercial-trace check
  - Miro writeback proposal
  - no-op reason
  - CRM implementation package QA
  - BPV route map for CRM implementation
  - data-quality and pilot acceptance gates
preflight_required: true
return_contract:
  version: "v0.1"
  changelog:
    - "2026-08-03: Installed from Dior handoff package with BPM routing metadata."
    - "2026-08-15: Added explicit BPM Exchange preflight_required and return_contract metadata."
    - "2026-09-15: Added CRM implementation package QA routing, BPV route map, data-quality gate, and pilot acceptance gate from OrtoLight package."
    - "2026-09-16: Added funnel multiplication guard: keep adjacent topics as fields/flags unless a separate lifecycle, owner, control point, or analytics loop is source-backed."
    - "2026-09-16: Added visual architecture scheme guard: numbered arrows and dotted proposals require a relation ledger before they count as integration specification."
    - "2026-09-16: Added повод / активность развития as a first-class CRM object for Refresh, Re-Engage, account management, and sales-support banks."
changelog:
  - date: 2026-08-03
    changes:
      - Installed from Dior handoff package.
      - Added Codex metadata for BPM routing.
      - Hardened DLP, external-system, and durable-writeback rules.
      - Added Russian output/field naming and CRM commercial-trace minimum.
  - date: 2026-09-15
    changes:
      - Added routing to CRM implementation package QA for multi-file CRM specs.
      - Added BPV route map, data-quality gate, and pilot acceptance gate as CRM handoff outputs.
  - date: 2026-09-16
    changes:
      - Added rule from Mясной Гурман CRM defense: do not create a separate CRM funnel for every adjacent topic; first prove a distinct managed lifecycle, owner, control point, or analytics loop. Otherwise route the topic as a Russian-labeled field, flag, checklist section, or dashboard dimension inside the primary process.
      - Added rule from Mясной Гурман sales-system architecture v2: a visual scheme with numbered links, arrows and dotted proposals is a discussion / alignment artifact until it has a relation ledger and owner decisions for each material connection.
      - Added cross-project derivative from Ракада Мед / Мясной Гурман / Indit: инфоповоды, активности и банк прогрессов are one methodological family. CRM design must decide whether they are fields, dictionaries, smart-process cards, or linked materials; they cannot remain free-text manager tasks.
---

# BPM10 CRM

## Purpose

Turn evidence about sales, clients, roles, systems, and management routines into a controllable CRM architecture. Design management logic first and technical configuration second.

Do not reduce BPM10 to a list of Bitrix24 fields. The result must explain:

- what the business manages;
- which objects need cards, owners, histories, links, stages, or analytics;
- which processes require separate lifecycles;
- where CRM ends and ERP, BI, document flow, service, or project delivery begins;
- which decisions, signals, and actions the CRM contour must support.

## Source Of Truth And Mode

When the original Vault corpus is available, treat it as the canonical methodological source and this skill as an executable wrapper over that logic. The bundled references are a portable fallback, not a license to overwrite live Vault logic by habit.

Default mode is `review / design / handoff preview`, not `durable writeback`.

## Load References Selectively

- Read `references/core-overview.md` for the canonical BPM10 scope and artifact set.
- Read `references/core-methodology.md` for the full first-iteration workflow and detailed CRM document rules.
- Read `references/artifact-templates.md` before producing BPM10 Markdown deliverables.
- Read `references/methodology-expansion.md` for strategy, problem maps, governance, systems, and dashboard requirements.
- Read `references/bpm-boundaries.md` when BPM4, BPM8, BPM11, BPV2, ERP, BI, or service boundaries are material.
- Read `references/miro-integration.md` only when a Miro output is requested or required for alignment.
- Read `references/qa-and-evals.md` before final handoff or when reviewing an existing CRM design.
- Read `references/lean-crm-prompts.md` only for reusable prompt patterns, manager packets, weekly reviews, or full-cycle QA.
- Read `references/related-skills.md` when the task extends into Re-Engage/accounting or Bitrix24 PHP automation.

## Operating Rules

1. Separate facts, hypotheses, decisions, and open questions.
2. Cite each material design decision to a source: interview, CRM export, current process, strategy, role model, report, or client confirmation.
3. Mark unsupported elements as `требует проверки`. Never invent roles, fields, stages, integrations, formulas, or system capabilities.
4. Use client terminology after it is confirmed. Keep one stable term for one object.
5. Keep CRM lean. Create a field only when it supports filtering, routing, stage control, automation, reporting, responsibility, or management review.
6. Keep long narratives, process maps, PowerMaps, technical inventories, and qualitative interview notes in linked files, boards, or attachments.
7. Treat a funnel as justified only when the lifecycle, owner, result, control points, or analytics differ.
7a. When a meeting proposes adjacent funnels such as tenders, training, visits, claims, promo, or partner support, first decide which process is the evidence-bearing primary lifecycle. Keep adjacent topics as fields, flags, checklist sections, dictionaries, or dashboard dimensions when they do not have a separate owner, stage logic, management review, or decision loop. Mark a separate funnel as `резерв / требуется проверка владельца и жизненного цикла` until the source proves the distinct lifecycle.
7b. Treat visual CRM / sales-system schemes as alignment artifacts until their material arrows are converted into a relation ledger: `номер связи -> источник -> приемник -> объект -> ключ сопоставления -> система-владелец -> частота -> ошибка / повтор -> владелец качества -> критерий приемки`. Dotted lines, proposals, screenshots, and role journeys do not prove integration readiness by themselves.
7c. Model `повод / активность развития` explicitly in Refresh, Re-Engage and account-management CRM. Historical aliases include `инфоповод` in Ракада Мед and `активность / банк прогрессов и акций` in Мясной Гурман. This object is not just a reminder or a free-text task: it must carry source, target client/account/point, reason to act, material or argument, expected client progress, owner, deadline, evidence of execution, result metric, and stop / repeat rule. Decide whether it is a dictionary row, checklist item, smart-process card, linked material, or dashboard dimension.
8. Require rejected/lost states with reasons and an explicit return, pause, or closure rule.
9. Treat Bitrix24 as the target implementation only when the task or sources confirm it. Keep the conceptual model platform-neutral first.
10. Do not write to production CRM, Miro, or other external systems without explicit confirmation of target, operation, and check/rollback plan.
11. All user-facing statuses, defect labels, management states, and field purposes must be written in Russian. English is allowed only for immutable system IDs, API fields, product names, or direct source quotes.
12. Raw CRM exports are not safe by default. Do not paste raw rows with names, phones, emails, exact deal titles, message texts, comment bodies, webhook fragments, private URLs, invoice numbers, or production notes into chat, Vault canon, or client-facing artifacts.
13. Before externalization or cross-project reuse, mask or generalize client names, personal identifiers, secrets, private board IDs, and commercially sensitive combinations of facts. Preserve the management mechanism, not the raw client trace.
14. By default, treat CRM, Bitrix24, Miro, and similar systems as read-only research surfaces until an explicit write target and rollback/check path are approved.
15. Durable writeback into Vault, registries, task trackers, or project cards requires explicit approval. Without that, return a proposal, diff, or preview only.
16. If BPM10 touches lead source, win/loss, ownership, or pipeline logic, check the minimum commercial trace: `lead_origin`, `source_type`, `source_detail`, `partner_channel_candidate`, `stage`, `product_route`, `proposal_status`, `win/loss`, `lost_to` when available, `owner`, `next_action`, and `metric_storage_primary/secondary` when known.

## Workflow

### 1. Define The Decision And Scope

Fix:

- business decision supported by the CRM;
- client, business unit, geography, channel, and product scope;
- current and target systems;
- expected deliverable: audit, first iteration, functional specification, review, Miro scheme, or implementation support;
- decision owner and review participants;
- deadline and price of error.

If scope is ambiguous, proceed with a clearly labeled working boundary that does not create external writes or irreversible changes.

### 2. Build The Evidence Base

Collect only relevant sources:

- project context and strategy;
- organizational and customer interviews;
- current CRM/ERP/BI exports and screens;
- process maps, role descriptions, regulations, and dashboards;
- CRM training or integrator baseline;
- confirmed examples and prior decisions.

Create a source register and an evidence ledger. Record conflicts rather than averaging them away.

Classify sources before using them:

- `интервью сотрудников`;
- `интервью клиентов`;
- `CRM export / screenshot / field dictionary`;
- `current regulation / process map`;
- `integrator spec / implementation note`;
- `dashboard / KPI / BPM-4 derivative`;
- `hypothesis / recommendation / agent inference`.

Keep source rights visible. A client claim, employee workaround, CRM screenshot, and agent synthesis do not have the same evidentiary weight.

### 3. Diagnose The Management Problem

Build a problem map before designing objects when the task is more than a local field change. Connect each problem to:

- observable fact;
- consequence or risk;
- owner or affected role;
- required management decision;
- CRM/process/data/system implication;
- source and confidence.

Use a problem graph when causal relations across strategy, sales, roles, data, and systems matter.

### 4. Set System Boundaries

For each process or fact, decide where the following live:

- action;
- confirmed fact;
- calculation or analytics;
- document of record;
- signal that starts a task, case, or deal;
- owner of data quality.

Do not move accounting, mass transactions, production delivery, or legally significant documents into CRM merely because they relate to a client. CRM should receive the status, signal, link, and next action it needs to manage.

### 5. Design The Conceptual Data Model

Start with business objects. Separate:

- entity;
- attribute or classifier;
- document;
- stage;
- activity;
- integration event;
- analytical metric.

Create an entity only when a separate card, history, owner, links, process, or analytics are required. Define relations and cardinality before platform mapping. Then map entities to standard CRM objects, smart processes, fields, files, or external systems.

### 6. Design Lifecycles And 4R

Classify processes when useful:

- `Reach`: first entry into a relationship, inbound or outbound;
- `React`: active commercial opportunity and sale;
- `Refresh`: warming or returning a relevant company without an active deal;
- `Re-Engage`: managed development of a current or known client.

Do not force all four classes into every CRM. Keep only the processes supported by the business model and confirmed target state.

For each lifecycle define:

- entity;
- owner;
- entry signal;
- reason / activity object: `повод`, `активность`, `инфоповод`, `прогресс`, `акция`, `материал`, or `next best action`;
- stages and stage outcomes;
- mandatory evidence and fields by stage;
- success, rejection, pause, and return routes;
- integrations and automations;
- management metrics and review rhythm.

### 7. Produce The First Iteration

Prepare enough logic for a 20–30 minute client review:

1. conceptual data model;
2. list of funnels and smart processes;
3. entity × process/4R matrix;
4. high-level stages and transitions;
5. system boundaries;
6. decisions and open questions.

Do not detail hundreds of fields before the entities, lifecycles, and system boundaries are confirmed.


### CRM Implementation Package QA

When the source set contains several implementation layers such as entity cards, funnels, automations, integrations, normalization / deduplication rules, migration notes, or rollout plans, treat the work as `CRM implementation package QA`, not as a simple CRM summary.

Use or recommend the dedicated `crm-implementation-qa` skill when available. If you stay inside BPM-10, still check:

- entity / role collisions: doctor, clinic, legal counterparty, payer, order contact, dealer, manager, economic buyer, technical buyer, end user;
- source-of-truth boundaries between CRM, 1C / ERP, BI, service, and channel systems;
- automations for repeated events, late events, errors, missing references, manual review, retry, and deduplication;
- integrations for direction, matching key, sync journal, reconciliation, failure handling, and ownership;
- data-quality gates: normalization, weak duplicate signals, dispute queue, merge journal, original-value preservation;
- pilot acceptance: pilot users, scenarios, entry criteria, stop / rollback criteria, owner sign-off, and full-launch gate.

For BPV routing, map each material source and requirement as:

`source -> BPM -> САИ / claim -> BPV line -> deliverable / skill delta`.

Do not create parallel Vault task rows when a live project task system such as ClickUp is already the downstream. Return a proposed ClickUp change set unless the user explicitly approves writing to ClickUp.

### 8. Produce The Integrator Package

After the first iteration is approved, produce the four mandatory Markdown documents:

1. `Client. CRM. Entity list.md`;
2. `Client. CRM. Funnels and smart processes.md`;
3. `Client. CRM. Entity cards.md`;
4. `Client. CRM. Functional requirements for funnels and smart processes.md`.

Add the entity/process matrix, system map, RASCI, analytics requirements, decision register, and Miro scheme when they reduce implementation risk.

If the task is limited to review or first iteration, do not generate all detailed artifacts mechanically. Produce only the minimum set required for the current gate.

### 9. Define Governance And Analytics

Fix:

- CRM owner and change authority;
- data owner and quality controller;
- RASCI by funnel, data object, decision, checkpoint, and dashboard;
- regular CRM review cadence;
- metric definitions, sources, and owners;
- how an exception becomes an assigned action;
- rules for field, stage, and automation changes.

A dashboard is not complete if it only shows facts. It must show the deviation, location, owner, reason, and next action or the reason no action is required.

### 10. Validate And Handoff

Run the checks from `references/qa-and-evals.md`. At minimum verify:

- source fidelity;
- entity/field separation;
- lifecycle justification;
- stage transition criteria;
- system boundaries;
- rejection and return routes;
- role ownership;
- analytics/action link;
- duplicate protection;
- implementation ambiguity;
- confidentiality and secret removal.

End with a decision register: approved, rejected, deferred, and still open items with owners and dates.

## Human Approval Gates

Stop for explicit approval before:

- fixing a disputed entity, funnel, role, KPI, integration, or scoring formula as final;
- moving from the first iteration to detailed functional requirements when the architecture is not approved;
- writing or updating canonical Vault files, project cards, registries, or task trackers;
- writing to a production CRM or Miro board;
- deleting, merging, or renaming existing CRM objects or fields;
- changing permissions, automations, webhooks, or public API contracts;
- exporting raw client, personal, financial, or production data.

## Output Standard

Lead with the management conclusion. Then provide evidence, design decisions, artifacts, risks, and the next review action.

Every table must have an operational purpose. Every material row must end in one of four states: confirmed, hypothesis, rejected, or requires confirmation.

For a review, report gaps first. For a new design, produce the artifacts first. Never claim validation or successful external writes unless they were actually performed and post-read.

When naming deliverables, statuses, and field purposes for the user:

- keep human-readable labels in Russian;
- keep API/system identifiers as separate exact values;
- explicitly separate `подтверждено`, `гипотеза`, `отклонено`, `требует проверки`;
- mark whether the output is `preview`, `candidate writeback`, or `approved writeback`.

## Anti-Patterns

- Starting with Bitrix24 fields before defining the managed object.
- Creating a funnel for every product, department, or technical substep.
- Creating a separate funnel for an adjacent topic when the source only proves a flag, checklist section, dictionary, or analytics dimension inside the primary managed process.
- Treating a visual architecture map as an integration specification before the numbered links, data owners, keys, failure handling, permissions, and pilot acceptance criteria are written down.
- Leaving `инфоповоды`, promotions, product arguments, client-development actions, or account-management reasons as free text without owner, target account, material, expected progress, execution evidence, and result metric.
- Mixing client status with deal stage.
- Duplicating ERP transactions or project delivery in CRM.
- Treating every meeting note or checklist as a CRM field.
- Omitting rejection reasons, return routes, owners, or transition criteria.
- Designing dashboards without a decision and action loop.
- Copying the current sales chaos into a target CRM because it already exists.
- Using Miro as the source of truth instead of generating it from approved Markdown logic.

## Structured Analytical Artifact Gate

CRM Problem Maps, issue/hypothesis trees, entity classifications, evidence matrices, process Mermaid/Miro views, metric trees, and dimension architecture inherit the global contract in `~/.codex/AGENTS.md`. Build the source-backed problem register before the target entity model; keep client facts, design hypotheses, and methodology separate. Entity or funnel partitions need an explicit scope and MECE verdict when they claim coverage; process diagrams use sequence/ownership/transition completeness instead. Miro and Frappe are mirrors/views, not source of truth.
