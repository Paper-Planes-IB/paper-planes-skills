---
name: bpm-exchange-reconciliation
description: Use when Ilya asks to run BPM Exchange, взаимное обогащение BPM, BPM-SI, Storyline-Storyboard, approved-presentation-to-BPV lineage, return packs, QA learning, client reality reconciliation, field pressure, or project-level BPM enrichment for 4th-department projects.
metadata:
  version: "0.2.10"
  status: draft
  line: 04-production / BPM Exchange / Storyline-Storyboard governance
  owner: Ilya
  supports_bpm:
    primary: [BPM-Exchange, Storyline-Storyboard, BPM-SI]
    required_secondary: [BPM-2, BPM-3, BPM-4, BPM-6, BPM-7A, BPM-7B, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-5, BPM-8, BPM-9]
  can_consume:
    - AGENTS.md and current rulebook
    - automation memory
    - BPM Storyline-Storyboard
    - Матрица BPM — SI
    - BPV — Внедрение registry and affected BPV files
    - approved presentation artifact/version and defense decision log
    - project BPM registry, tracker, chat map, subpassports
    - deepresearch / competitor-research return packets
    - presentation QA packets
    - client interviews, CRM, win/loss, dashboard, commercial trace
    - participating skill capability metadata
  can_produce:
    - BPM Exchange reconciliation packet
    - Storyline-Storyboard delta proposal
    - BPM-SI donor / candidate / no-op classification
    - BPV downstream / sub-BPV / gate / proof-metric classification
    - BPV-sequence impact proposal
    - BPM / SI / slide / approved decision / BPV lineage packet with reverse links
    - client reality and field pressure reconciliation
    - commercial mechanics evidence needs
    - naming normalization table
    - task_delta packet for Codex Project Task Inbox
    - skill / rule / automation patch candidates
  preflight_required: true
  return_contract:
    version: "v0.2"
    changelog:
      - "2026-05-27: Initial orchestrator skill for BPM Exchange reconciliation."
      - "2026-05-28: Added execution modes, short path, trigger routing, preflight checklist, upstream contracts, and decision footer."
      - "2026-05-31: Added BPM-4 donor hypothesis pattern and graph-class routing for cross-BPM exchange."
      - "2026-06-06: Added stateful reuse / method-derivative governance and economical triggers."
      - "2026-06-06: Added mandatory family/source/alias expansion for donor search after MГ Окское Подворье miss."
      - "2026-06-06: Made 4ka archive index the mandatory reuse visibility scaffold."
      - "2026-06-09: Added accepted guards for already-synced hot project ingest and downstream 2ka raw-pack derivatives."
      - "2026-06-10: Added accepted guards for commercial reengage donors, accepted SI refinements, and 2ka content-draft language donors."
      - "2026-06-11: Added guards for mixed-delivery Storyline receivers, initiative-map BPM-home decisions, and empty/service raw-pack no-ops."
      - "2026-06-11: Added BPV downstream and BPV-sequence checks for Storyline/BPM-SI signals."
      - "2026-06-21: Added public competitor map field-pressure table guard before ranking or battlecard priority."
      - "2026-07-11: Canonized BPV-01...14 routes and added approved-deck/decision lineage with reverse BPV links."
      - "2026-08-03: Added accepted guards for management-delta source-class filtering and New Delivery client-result vs methodology-harvest separation."
      - "2026-08-11: Added commercial trace reality and hold-topic review guards for BPM Exchange writeback."
---

# BPM Exchange Reconciliation

## Presentation boundary

BPM Exchange may create SI, storyline, reuse and donor routes, but any downstream slide, HTML, PP Pages or PPTX must enter PP Presentation Kit 2026-07-12. Donor discovery does not permit direct copying or rendering; the kit preflight and receipt remain mandatory.

## Purpose

Run the current BPM Exchange standard for 4th-department project learning: mutual enrichment between BPM tracks, BPM-SI, project Storyline-Storyboard, external return packs, QA events, client reality, field evidence, commercial mechanics, and skill/rule/automation patches.

This skill is an orchestrator. It does not replace `deepresearch`, `competitor-research`, `presentation-qa`, `rail`, `ingest`, or BPM-4 domain skills. It coordinates their outputs and checks whether a signal should enrich a project Storyline, BPM-SI, BPV/sub-BPV/gate, a task bridge, or no-op.

## Core Principle

The skill is not the source of truth for the standard.

At runtime, reconstruct the current standard from live sources before reasoning:

1. root / local instructions: `AGENTS.md`, `.Codex/rules/*.md`, and relevant `ПКМ` rules;
2. automation memory: `$CODEX_HOME/automations/bpm-exchange-learning-brief/memory.md`, when this is an automation or learning-brief run;
3. project sources: `Карта-чатов.md`, `Реестр-BPM.md`, `Трекер-задач.md`, subpassports, project card;
4. project `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md`;
5. `Матрица BPM — SI.md` governance / donor / no-op blocks;
6. current deck artifact/version, defense protocol, approved slide IDs, and approved decisions when a presentation exists;
7. `BPV — Внедрение/README.md` and affected BPV files when a signal implies implementation;
8. relevant return packs, QA outputs, commercial trace, CRM/win-loss/dashboard/interview evidence;
9. capability metadata of participating skills.

Capability metadata check is conditional. Do not flag a skill merely because it exists in the local skill list. Check `version`, `supports_bpm`, `can_consume`, `can_produce`, `preflight_required`, and `return_contract` only for skills that actually participate in the current BPM Exchange route. Example: `BPM1` needs full capability metadata only when BPM-1 survey evidence, survey priors, survey lake, or BPM-1 -> Storyline routing is active in the pass.

If live sources conflict with this skill, live sources win unless the conflict is itself a rule/skill patch candidate.

## Accepted Over-Routing Guards

These guards are accepted operating rules for BPM Exchange. Apply them before creating any Storyline gap, BPM-SI candidate, SIF cluster, or `task_delta`.

### BPV Downstream Guard

Storyline and BPM-SI signals can imply future implementation, but this does not automatically create a new top-level BPV.

Before proposing BPV writeback, classify:

| Classification | Meaning |
|---|---|
| `upper-BPV-candidate` | possible new top-level BPV; requires separate Ilya decision |
| `sub-BPV-candidate` | specialization inside an existing BPV |
| `BPV-gate` | readiness / quality / adoption check inside BPV |
| `BPV-proof-metric` | metric that proves implementation is working |
| `skill-only` | useful agent workflow, not a client business process |
| `BPV no-op` | checked and does not affect BPV |

Required checks:

1. Read the canonical registry and search `BPV-01...BPV-14` for an existing parent.
2. Route `МПП` to `BPV-03.7 Материалы поддержки продаж`; keep `BPV-04.4 Подготовка КП и ТКП` adjacent.
3. Route CRM to `BPV-05.1`, preparation of data/architecture/automation to `BPV-05`, analytics to `BPV-10`, RAG/AI to `BPV-11`, and Digital Profit Model / sequence decisions to `BPV-12`.
4. Keep product Tunnel / SEVA / NPD in `BPV-01`; use BPV-02/07/08 as adjacent finance, operations, and management routes only when their objects are affected.
5. Mirror every educational product to the applicable `BPV-14.x` and `BPV-14.R` while preserving the subject BPV, or record an explicit no-op.
6. Preserve `source BPM -> SI -> Storyline slide_id -> approved deck/version -> approval decision -> BPV/sub-BPV/gate/proof metric` and write the reverse BPV link. An unapproved slide is only a BPV candidate.
7. Show `BPV-sequence impact`: which future implementation route, owner, rhythm, evidence, and next gate the signal implies.
8. Update Storyline/BPM-SI/BPV only when the receiver is confirmed; otherwise return a proposal or no-op reason.

### Already-Synced Hot Project Ingest

Fresh project-folder activity can be a material signal without being a missing landing gap. When a hot project ingest is already synchronized across the relevant project layer, classify it as `bpm_program_already_synced` and do not create duplicate SI/SIF, Storyline gap, or Task Inbox packet.

Minimum synchronization check:

| Layer | Check |
|---|---|
| `BPM Storyline-Storyboard` | source appears in hypotheses, knowledge gaps, slide/exhibit map, or impact log |
| `Problem-Map` / equivalent project analysis | source problems or increments are represented |
| `Реестр-BPM` / BPM registry | source is logged or affected BPMs are updated |
| `StageGate` / Rail state | current stage, repair pack, or PLAN gate reflects the signal when relevant |
| tracker / `Codex Project Task Inbox` | accepted executable follow-ups already exist or explicit no-op is recorded |

Output required:

```text
facts -> source_detected and landing evidence
inference -> bpm_program_already_synced
accepted/unchanged canon -> project mode and current gate
task_delta -> no_op with matched_existing_task when relevant
next_expected_delta -> actual evidence still needed
```

Do not reopen the same route from later service reports, bpm-progress blocks, matrix-only changes, project journals, or content derivatives unless there is a new primary source, senior edit, source-check result, CRM/dashboard evidence, or explicit human routing.

### Downstream Raw-Pack Guard

Fresh 2ka raw-packs are useful control sources but inherit the status of their upstream source. A raw-pack does not become BPM-SI evidence by itself.

Before using a raw-pack as BPM Exchange input, compare:

1. raw-pack source path and source mtime;
2. upstream project journal / Storyline / tracker mtime;
3. previous BPM-SI or project writeback blocks;
4. whether the raw-pack contains primary evidence, senior edit, source-check result, or only service/empty journal text;
5. receiver mode, especially `New Delivery` vs `BPA / All Delivery`.

Classify as:

| Condition | Classification |
|---|---|
| upstream project state already handled | `downstream_derivative_no_op` / `duplicate_existing_signal` |
| raw-pack built from service or empty journal sections | `service_derivative_no_op` |
| New Delivery raw-pack without explicit BPA routing | `wrong_receiver_guard / donor_signal` |
| raw-pack contains new primary source or explicit human routing | inspect primary source before any writeback |

### Management Delta Source-Class Guard

Daily reports, project journals, raw-packs, service journals, and file mtime radar may mark a project as `moving` or `project_delta`, but that label is not evidence by itself. Before accepting movement, classify the source class and the management delta separately.

Required source-class checks:

1. Is the changed object a primary project source, client-facing evidence, source-check result, CRM / dashboard evidence, accepted senior edit, or explicit owner routing?
2. Or is it a project card, empty project journal, service report, raw-pack, Daily Note derivative, internal governance source, file-only mtime, API-only radar, technical/runtime file, or weak lexical crossmatch?
3. Has the referenced parent source changed materially since the last landing, or is the raw-pack only repeating an already handled source?
4. For `New Delivery`, is the signal a client result, a source-check/prototype, a role/coordination gate, or methodology harvest?

Classify as:

| Condition | Classification |
|---|---|
| empty project journal with only raw-pack links | `no_material_change / service_or_empty_source` |
| project card / service / internal governance source without new client-facing evidence | `no_material_change / derivative-source-flag` |
| file-only or API-only radar without source-read | `source-read candidate / needs_evidence` |
| same-day Shared Drive source-check file for a hot `New Delivery` project | inspect the source-check file before reducing the signal to raw-pack no-op |
| `New Delivery` prototype, workbook, recommender, role map, or track file without owner/client acceptance | `source-check / management_delta candidate`, not client progress |
| accepted role/coordination rule with missing owner or expired coordinator | `management-gap / needs_owner`, not Storyline/BPV/SI evidence |

If source-class checking downgrades many `moving` rows to no-op, return a prompt/rule/automation patch candidate rather than opening Storyline, BPM-SI, BPV, or task routes.

### Commercial Reengage Donor Guard

Commercial reengage can be material BPM-SI evidence without being a project Storyline receiver. If a reengage / existing-client / approach-in-progress source creates a repeatable cross-BPM SI or SIF candidate, route it as `donor_signal` through commercial trace, Matrix BPM-SI, and source-check gates unless a BPA / All Delivery project receiver is explicitly confirmed.

Required checks:

1. commercial trace already records `client_entity`, `lead_origin`, `source_type`, `stage`, `product_route`, `ICP-fit`, and metric storage;
2. the signal has a repeatable BPM bundle, not only a one-client sales note;
3. the next project receiver is named explicitly before any Storyline writeback;
4. executable follow-ups are shown as task_delta packets only when an accepted owner / due / output exists.

Classify as:

| Condition | Classification |
|---|---|
| commercial trace landed, no confirmed BPA receiver | `donor_signal / no project Storyline writeback` |
| repeatable SI/SIF candidate appears | `Matrix proposal / needs_source_check` |
| confirmed project receiver and primary source exist | inspect target project sources before writeback |

### Commercial Trace Reality Guard

Commercial trace rows, proposal drafts, Gamma / deck work, verbal-yes notes, reengage status, partner lead signals, and procurement-ready language are commercial evidence, not proof of delivery, sent status, client acceptance, win/loss, competitor pressure, or BPV readiness by themselves.

Before using a commercial signal as BPM Exchange evidence, split:

1. `commercial fact`: lead, КП, draft, sent, verbal yes, procurement, lost, won, paused, reengage;
2. `source right`: email / CRM / call / proposal / invoice / win-loss / partner / owner statement;
3. `project receiver`: confirmed BPA / New Delivery / support / sales-only / no receiver;
4. `commercial mechanics`: VAT, legal entity, price/margin, COGS, discount, service/warranty, implementation effort, integration, opportunity cost;
5. `client reality`: owner / buyer / partner / dealer / expert / CRM / win-loss confirmation.

Classify as:

| Condition | Classification |
|---|---|
| commercial trace landed, sent / accepted / win-loss unknown | `commercial_reality_gap / needs_status_check` |
| proposal or sales-play contains competitor / battlecard claim without field or CRM evidence | `commercially_incomplete / needs_BPM-4/5/9/10/11` |
| verbal yes or procurement-ready signal exists without invoice / contract / owner confirmation | `commercial_trace_evidence / not_delivery_evidence` |
| project receiver not confirmed | `donor_signal / Matrix proposal / no Storyline writeback` |
| CRM / win-loss / owner confirmation lands | route to the relevant BPM receiver and recheck BPV consequence |

### Accepted SI Refinement Guard

When an already accepted SI route receives a calibration axis such as channel, region, segment, role, product line, customer type, or evidence confidence, do not create a standalone SI by default.

Route the signal as a refinement of the accepted SI when:

1. the base SI is already accepted or canonized;
2. the new signal changes calibration or applicability, not the core logic;
3. there is no repeated BPA / All Delivery evidence or senior review yet;
4. project-specific weights, thresholds, sanctions, and client regulations still require calibration.

Use `Matrix refinement / donor_signal / needs_source_check`; create a new SI only after repeatability, senior review, or explicit Ilya routing.

### 2ka Content-Draft Donor Guard

Drafts from 2ka books, articles, content-harvest, weekly-doc, or narrative batches may contain useful language, QA frames, or product-definition lenses. They are not primary BPM evidence.

Treat them as `language_refinement / QA-frame donor / needs_routing` unless they are tied to a primary project source, senior deck/storyboard edit, accepted methodology update, or explicit human routing. They must not create project Storyline gaps, task_delta, canonical SI, or client-facing claims by themselves.

### Hold Topic Brief Review Guard

Hold / watch topic briefs, content harvest notes, raw topic lists, and weak external/public signals may reveal useful language or future source-check queues, but they are review-layer artifacts until a primary project source, senior edit, accepted methodology update, explicit Ilya routing, or client / CRM / expert confirmation lands.

Classify them as `review_layer / source_check_queue / no durable route` by default. They may be shown in the daily BPM Exchange brief with preflight summary and no-op reason, but must not create Storyline gaps, canonical SI, BPV routes, task_delta, client-facing claims, or skill changes without a stronger receiver.

### Mixed-Delivery Storyline Receiver Guard

Some active 4D projects use a slide/storyline receiver whose filename is not exactly `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md`. If the project card, Rail status, tracker, chat map, or subpassports show that the existing Storyline file is the accepted receiver for hypotheses, slide logic, evidence gaps, and BPM/SI deltas, use that file as the project receiver.

Do not create a duplicate Storyline file and do not reclassify the project into a classic BPA / All Delivery phase merely because the filename or delivery model differs.

Classify as:

| Condition | Classification |
|---|---|
| fresh primary project source is already landed in existing Storyline receiver and Task Inbox | `bpm_program_already_synced / existing_storyline_receiver` |
| fresh primary source produces a reusable BPM-SI route but project mode remains mixed delivery | `Matrix proposal / project_only / needs_source_check` |
| downstream report complains about missing exact filename while accepted receiver exists | `naming_boundary_no_op / no_duplicate_storyline` |

### Initiative-Map BPM Home Guard

When an active 4D project is explicitly managed through an initiative map, штабная рельса, tracks, subpassports, or a mixed old-new delivery model, absence of a classic `Реестр-BPM.md` or `BPM-статус` block is not automatically a project defect.

Before opening a BPM-home gap, check whether the project card or Rail status names a program home such as `карта инициатив П1-П14 -> рабочие контуры -> evidence/storyboard -> штабные решения`.

Classify as:

| Condition | Classification |
|---|---|
| initiative-map program home is explicit and accepted | `explicit_bpm_home_no_op / classic_registry_not_required` |
| initiative-map is implied but not accepted | `needs_bpm_program_home_decision` |
| project is classic BPA / All Delivery and has no accepted alternate home | `missing_bpm_program_home` |

### Empty / Service Raw-Pack No-Op Guard

If a post-cutoff 2ka raw-pack points to an upstream project journal, service report, Daily Note, or content-harvest item whose project delta is empty, service-only, already handled, or below evidence threshold, do not run SI extraction.

Classify as `below_threshold / service_or_empty_source / downstream_derivative_no_op`. Reopen only when the raw-pack contains a fresh primary source, source-check result, senior edit, CRM/dashboard evidence, or explicit Ilya routing.

### Public Competitor Map Field-Pressure Guard

Public competitor maps, SEO/web visibility maps, market maps, partner catalogs, tender scans, and external competitor return packets cannot produce final competitor ranking, battlecard priority, or client-facing sales-play priority until field pressure is separated from public visibility.

For every real-client competitor route, require a compact table before ranking:

| player | role_type | public_visibility | client_reported_pressure | CRM_or_win_loss_evidence | historical_or_latent_pressure | ranking_allowed_now | next_evidence_needed |
|---|---|---|---|---|---|---|---|

Classify:

| Condition | Classification |
|---|---|
| high public visibility, weak/unknown field pressure | `benchmark_only` / `latent_threat` / `watch` / `public_visibility_rank_only` |
| low public visibility, strong field pressure | `hidden_or_low_visibility_competitor` / `required_check` |
| no CRM / win-loss / client / sales evidence | `public evidence map / needs_field_reconciliation` |
| field pressure confirms practical deal threat | ranking or battlecard priority allowed, with source caveat |

Do not treat public visibility as real sales threat. Route missing field evidence to BPM-2 / BPM-3 / BPM-10, and to BPM-4 / BPM-5 / BPM-9 / BPM-11 when commercial mechanics, economics, implementation burden, ownership, or data model can change the ranking.

## Execution Outline

Run in this order:

1. Choose mode: `full_exchange`, `light_reconciliation`, or `qa_fix_only`.
2. Load the current standard from live sources; do not rely on memory alone.
3. Preflight the project / contour / delivery mode / receiver / writeback boundary.
4. Gather only relevant signals for the requested cutoff or scope.
5. Build the signal map with primary BPM, secondary BPM increments, evidence strength, and route class.
6. Run governance checks: relevance, conflict, TTL, work-log, derivatives, false-positive risk.
7. Run reuse / method-derivative check only when trigger and evidence threshold are met.
8. Run client reality / field pressure / commercial mechanics / naming checks only when triggered by the signal.
9. Return Storyline/BPM-SI effect: `появились / усилились / ослабли / нет существенной дельты`.
10. Produce Task Delta packets for executable actions.
11. End with human gates / decision footer for any durable writeback.

## Modes

| Mode | Use when | Required blocks | Optional / skip |
|---|---|---|---|
| `full_exchange` | daily brief, project-wide exchange, multi-source return packet | preflight, signal map, cross-BPM, governance, Storyline/BPM-SI effect, task_delta, human gates | include all triggered client reality / field / commercial / naming blocks |
| `light_reconciliation` | one project, one source, small delta, quick check | preflight, top 3-5 signals, route/no-op, Storyline effect, human gates | skip full tables with no signal; summarize no-op reasons |
| `qa_fix_only` | QA claim-risk / trace-gap / prompt patch only | preflight, QA signal, source BPM needed, route/no-op, patch candidate, human gate | skip competitor/client reality unless QA touches those claims |

Default mode is `light_reconciliation` unless the user asks for daily/full/project-wide exchange or the source set is broad.

## When To Use

Use for:

- `BPM Exchange`, `BPMExchange`, `bpm exchange`;
- взаимное обогащение BPM;
- reconciliation between BPM, BPM-SI, Storyline-Storyboard, return packs, QA, skills;
- daily / periodic learning brief for 4th-department projects;
- project-level question: which BPM should check, answer, enrich, or downgrade a signal;
- external research return that may affect Storyline, BPM-SI, competitor ranking, field questions, or task_delta;
- QA finding that should improve prompts, rails, return contracts, eval cases, or rules.

Do not use for:

- writing the full external research prompt itself: use `deepresearch` or `competitor-research`;
- slide/deck QA itself: use `presentation-qa`;
- project rail repair itself: use `rail`;
- durable writeback without Ilya's explicit accept.

Trigger routing:

| User wording / situation | Use this skill? | Route |
|---|---|---|
| `BPM Exchange`, `взаимное обогащение BPM`, `сверь BPM-SI и Storyline` | yes | `bpm-exchange-reconciliation` |
| external research return affects real project Storyline / SI / field questions | yes, after relevant return skill | this skill coordinates downstream routing |
| `сделай deepresearch prompt` / `дай запрос в Perplexity` | no | `deepresearch` |
| `собери конкурентный prompt / battlecard research` | no for prompt; yes later for return reconciliation | `competitor-research`, then this skill if returned |
| `проверь презентацию / claims / deck` | no for QA itself; yes for QA learning loop | `presentation-qa`, then this skill if QA creates BPM deltas |
| `проверь рельсу проекта` | no | `rail` |
| pure content summary without BPM/SI/Storyline exchange | no | use relevant content/summary route |

If the user does not mention BPM Exchange, BPM-SI, Storyline, mutual enrichment, return-packet routing, or QA learning loop, do not activate this skill for a pure research, deck, or rail task.

## Required Preflight

Before content output, classify:

```text
project / contour -> delivery mode -> current receiver -> allowed writeback -> forbidden writeback -> live sources checked
```

Use this checklist:

| Question | Typical values | If unclear |
|---|---|---|
| What project / contour is active? | project name, 4D folder, штаб, auxiliary chat, automation | read project registry / chat map before output |
| What is delivery mode? | BPA / All Delivery, New Delivery, legacy, commercial intake, report-layer | mark `receiver_unconfirmed` |
| What is the receiver? | Storyline, BPM-SI, tracker, Task Inbox, commercial trace, no-op | default no durable writeback |
| What live sources were checked? | AGENTS/rules, memory, Storyline, BPM-SI, registry, tracker, return pack, QA | say `partial_context` if missing |
| What writeback is allowed? | chat-only, proposal, accepted writeback | require explicit accept unless already accepted |
| What writeback is forbidden? | Storyline/BPM-SI/rules/tasks/Airtable without accept | list in preflight |

For 4th-department projects, distinguish:

| Mode | Storyline behavior |
|---|---|
| BPA / All Delivery receiver | Storyline/BPM-SI enrichment may be required after strong primary source |
| New Delivery | project Storyline gap is no-op by default; extract donor signals only |
| legacy / hybrid / single-contour exception | inspect project rules before creating gaps |
| commercial / signed-doc intake only | confirm signed/payment/owner/delivery mode before BPM obligations |
| report-layer only | no-op until primary source is checked |

Preflight examples:

- `Амиго / штаб -> BPA receiver -> Storyline + tracker checked -> writeback forbidden without accept -> field-pressure reconciliation allowed as proposal`.
- `Вастэко / New Delivery -> wrong receiver for BPA.08 Storyline -> donor-only -> no project Storyline gap`.
- `Ортолайт / signed-doc intake -> receiver unconfirmed -> required_check before BPM obligations`.

## Signal Map

Build a compact map of signals since the relevant cutoff or within the user-specified project scope.

In `light_reconciliation`, keep only top 3-5 signals and one no-op row for the rest.

For each strong signal capture:

| Field | Meaning |
|---|---|
| source | file/event/return pack/interview/QA/CRM/dashboard |
| source_type | primary / external_public / client_interview / CRM / dashboard / report_layer / donor |
| primary_BPM | main BPM that owns the signal |
| secondary_BPM_increments | BPMs that must check or receive consequences |
| evidence_strength | high / medium / weak |
| route_class | required_check / optional_enrichment / watch / no_op |
| receiver | Storyline / BPM-SI / tracker / Task Inbox / commercial trace / no-op |
| human_gate | yes/no and why |
| si_ids | exact SI / SIF identifiers |
| storyline_slide_ids | project slide hypothesis identifiers |
| deck_artifact_version | defended / approved presentation artifact and version |
| approval_event_or_decision | protocol, decision, approver, date/status |
| bpv_route | canonical BPV/sub-BPV/gate/proof metric/candidate/no-op |
| reverse_bpv_link | written / proposed / missing / not_applicable |
| training_mirror | BPV-14.x + BPV-14.R / no-op |

For reuse / donor / method-derivative signals also capture Russian-readable fields:

| Field | Meaning |
|---|---|
| проект_источник | where the reusable data / model / derivative was born |
| проект_применения | current or candidate project where it may be reused |
| тип_реюза | `data reuse` / `model reuse` / `method derivative` / mixed |
| исходный_BPM | BPM that produced the source operation |
| связанные_BPM | BPMs that must receive or check consequences |
| что_переносится | data schema, model logic, dashboard representation, slide logic, field questions, etc. |
| что_не_переносится | boundaries and risks |
| reuse_state | `open` / `confirmed` / `rejected` / `weak_evidence` / `not_needed` |
| причина_отказа | required when rejected |
| условия_повторной_проверки | required when rejected or weak evidence |
| human_gate | who decides: C3 / C4 / Ilya / client owner |

English machine tags may be added, but Russian fields are mandatory.

Do not limit checks to BPM-4/5/6/7. Consider BPM-1, BPM-2, BPM-3, BPM-4, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9, BPM-10, BPM-11 when materially relevant.

## Cross-BPM Exchange

For each material signal, return the exchange route:

```text
source BPM -> question produced -> target BPM -> expected answer -> returned hypothesis -> receiver / no-op
```

Examples:

- BPM-6 public competitor map -> asks BPM-2/3/10 whether pressure is lived -> CRM/win-loss returns field priority -> Storyline competitor ranking updated or downgraded.
- BPM-4 dashboard anomaly -> asks BPM-6/7B whether this is market opportunity or internal mix artifact -> Storyline keeps only validated growth claim.
- QA claim-risk -> asks source BPM for proof -> weak claim becomes no-op, footnote, or evidence need.

## BPM-4 Donor Hypothesis Pattern

BPM-4 often acts as a donor BPM: dashboards, Formula Profit, transaction logs, unit economics, and data gaps produce questions that other BPMs must answer before the finding becomes a strategic claim. Treat BPM-4 findings as `economic evidence`, not as complete strategy by themselves.

For each BPM-4 signal, build:

```yaml
bpm4_donor_hypothesis:
  source_signal: ""
  graph_or_table_class: ""
  economic_observation: ""
  produced_hypotheses:
    - target_bpm: BPM-1|BPM-2|BPM-3|BPM-5|BPM-6|BPM-7A|BPM-7B|BPM-8|BPM-9|BPM-10|BPM-11
      question: ""
      evidence_needed: ""
      expected_return: ""
      route_class: required_check|optional_enrichment|watch|no_op
  claim_guard: confirmed_by_data|partial|inference|do_not_claim
  receiver: Storyline|BPM-SI|field_questions|tracker|Task_Inbox|no_op
```

Common BPM-4 graph classes and exchange routes:

| BPM-4 graph / table class | Produces question for | Typical hypothesis |
|---|---|---|
| Formula Profit tree / waterfall | BPM-2, BPM-5, BPM-8, BPM-10 | revenue or profit is constrained by offer, process, operating rhythm, or CRM / data capture |
| Unit economics / margin matrix | BPM-2, BPM-6, BPM-7A, BPM-7B | product / segment attractiveness differs from public market logic |
| Revenue / profit concentration | BPM-2, BPM-6, BPM-7B | dependence on narrow segment / customer / service creates growth or risk hypothesis |
| Funnel / conversion / leakage | BPM-3, BPM-5, BPM-8, BPM-10 | demand, UX, process handoff, or CRM status causes observable loss |
| Cohort / retention / LTV | BPM-2, BPM-3, BPM-7B, BPM-8 | growth comes from repeat mechanics, journey design, product route, or relationship rhythm |
| Capacity / utilization / bottleneck | BPM-5, BPM-8, BPM-9, BPM-11 | economic upside is blocked by operations, roles, staffing, schedule, equipment, or data model |
| Entity scatter / quadrant map | BPM-2, BPM-6, BPM-7B, BPM-9 | clients / products / doctors / managers / territories split into different strategic arenas |
| Transition / Sankey / pathway | BPM-3, BPM-5, BPM-8, BPM-11 | real journey differs from declared process and requires process or data-model reconstruction |
| Plan-fact / forecast variance | BPM-5, BPM-9, BPM-10, BPM-11 | planning rhythm, owner model, data granularity, or forecast assumptions are wrong |
| Data-gap / observability heatmap | BPM-10, BPM-11, BPM-5 | the organization cannot manage the claim yet; data model or process capture must be repaired |

Do not promote a BPM-4 graph into a market, customer, or process claim until the target BPM evidence is checked or the claim is explicitly marked as inference.

## Reuse / Method-Derivative Governance

`Проверь доноров` is a machine operation, not a manual C1/C2 task:

```text
family/source expansion -> alias expansion -> match -> applicability -> transferable operation / method derivative -> data sufficiency -> verdict
```

C1/C2 may provide or confirm simple parsed facts: industry, business model, channel, active BPM, data type, analysis object, current gate, SKU depth, buyer id, repeat purchase, purchase channel, margin/proxy availability. The skill must do the donor matching and applicability check; C3/C4/Ilya make the semantic decision.

### Family / Source / Alias Expansion

Before saying that no stronger donor exists, or before returning a top-K donor list, expand the search space through family terms and concrete source homes. This is mandatory because reusable units may live under different project names, 2ka case derivatives, 5ka tunnel batches, 8ka knowledge units, or 1ka training exercises rather than the current semantic label.

Do not wait for a human to name the donor. Build a family query from the current project signal.

Example: for `МГ / мясная фирменная розница / правильная корзинка / чек / повтор / loyalty / SKU / конечный потребитель`, the machine should search:

```yaml
family_query:
  industry_family:
    - "food retail"
    - "branded retail"
    - "фирменная розница"
    - "колбасная продукция"
    - "мясная продукция"
    - "замороженная продукция"
  business_model:
    - "own retail"
    - "программа лояльности"
    - "карта лояльности"
    - "LTV"
  analysis_object:
    - "конечный потребитель"
    - "чек"
    - "корзина"
    - "структура чека"
    - "глубина чека"
    - "повтор"
    - "отток"
  antipatterns:
    - "розница без корзины"
    - "traffic-without-basket-economics"
    - "basket-level loyalty analytics"
```

Search these terms in curated reuse homes before broad Vault search:

Minimum expansion:

| Source home | What to search |
|---|---|
| 4ka archive index / passports | start from `04-производство/Архивные проекты/00-Индекс архивных проектов.md` as reuse visibility scaffold; then search linked passports for exact names, aliases, source corpus status, archive tunnel status, family/species terms |
| 2ka cases / content derivatives | client-facing case names, industry descriptions, source PDF names |
| 8ka knowledge units | reusable unit names, archetypes, fate of knowledge, limitations |
| 5ka post-archive tunnel | `METH-*` units, antipat­terns, method names |
| 1ka training units | exercise names that preserve reusable operations |
| BPV-14.R educational-product registry | subject BPV, audience, capability gap, cost/load, reuse, assessment, and transfer-to-work evidence |

The archive index defines the candidate universe for archived-project reuse. If an archived project lacks full family/species classification but is not marked `excluded`, `alias_only`, `aggregate_only`, or `do not tunnel`, keep it visible as `reuse_visible / needs_classification` or `reuse_visible / source_limited` rather than dropping it from the donor pass.
| current project evidence | people-named donors, abbreviations, working names, source terms |

If a human mentions a candidate donor that the first pass missed, reclassify the first pass as `missed_family_source_expansion` or `missed_alias_source_expansion`, not as `weak_evidence`. Then:

1. search family terms, exact names, and aliases;
2. identify the physical source homes found;
3. update the donor verdict;
4. record the miss cause if the project has a Rail/status or reuse packet.

Do not treat a donor as absent merely because a broad category search produced noisy output. If category words like `retail`, `SKU`, `consumer`, `CRM`, `loyalty`, or `clustering` are too broad, constrain them to curated reuse homes and combine them with business model / object / anti-pattern terms.

Run reuse / method-derivative governance only when one of these triggers is present:

- explicit Rail / BPM Exchange / donor / reuse / method-derivative request;
- pre-defense or client-defense preparation;
- 3-4 significant ingests have accumulated and at least one touches `BPM-1`, `BPM-2`, or `BPM-3`;
- major BPM source completed: processed survey, interview block, raw-pack, dashboard, export, data request, or client document with management meaning;
- status signal changes the project gate.

Do not run it on every subpassport/scope update, minor administrative edit, ordinary task status, or single weak note. Do not depend on project heartbeat as the primary trigger.

State machine by `BPM / theme / route`:

| State | Meaning | Behavior |
|---|---|---|
| `open` | enough evidence to evaluate | run compact verdict |
| `confirmed` | reuse accepted | stop proposing same route; update only after substantial new data or gate change |
| `rejected` | reuse declined | record reason and retry conditions; use the reason to improve future matching |
| `weak_evidence` | below threshold | do not propose; observe until stronger evidence appears |
| `not_needed` | observer says methodological innovation / reuse is unnecessary | freeze until gate change, new substantial data, or explicit review |

Separate three entities:

- `data reuse`: source data, survey, transaction, CRM, BI, interview pack, or dashboard can be reused;
- `model reuse`: analytical model, clustering, scoring, segmentation, or calculation logic can be adapted;
- `method derivative`: a derivative form of an existing BPM / method / SI that changes the organization or representation of raw BPM material for the team or client.

Do not call this `method_candidate` by default. A derivative may later become a method candidate only after repeated use, review, and explicit methodological acceptance.

Tunnel derivative candidates by maturity, not mechanically:

| Status | Route |
|---|---|
| `project-only` | current project Storyline / BPM sources only |
| `method-derivative-candidate` | BPM source + BPM-SI matrix / derivative layer as proposal |
| `reuse-confirmed` | confirmed project route + source project reference + conditions |
| `training-ready` | 1ka training only after repeatable reviewer-safe operation |
| `content-ready` | 2ka content only after client-safe abstraction |

Possible receivers: source BPM, BPM-SI matrix, method derivative layer / registry, 8ka knowledge factory, 1ka training, current project Storyline, BPM-10/11 when CRM/BI/data-model fields are required, 2ka content only when mature.

## Governance Checks

For every strong route include:

| Check | Required output |
|---|---|
| relevance_score | 0.0-1.0 with short reason |
| top-K / preflight_summary | short useful subset, not raw dump |
| conflict_resolution | contradiction type, strategy, status, human gate |
| signal_lifecycle / TTL | new / active / stale / duplicate / expired |
| work_log_check | landed / missing / report-only / stale |
| derivatives | generated / landed / no-op |
| false_positive_risk | low / medium / high |

If many low-relevance or no-op routes appear, propose a prompt/rule/automation patch candidate.

## Client Reality Gate

External research is public evidence, not lived reality.

Short output: if no material external-vs-field conflict exists, write one line: `Client Reality: нет существенной дельты / public evidence remains evidence map`.

When external market/category/competitor/channel output touches a real client project, show:

| Block | Include |
|---|---|
| external_visibility_claims | what public evidence claims |
| client_reality_questions | what BPM-2/BPM-3/owner/dealer/partner/client must verify |
| corrected / contradicted / added / downgraded | how field reality changes public map |
| needs_CRM_win_loss_source_check | concrete CRM/tender/support/dashboard fields needed |

## Field Pressure Reconciliation

Do not rank competitors only by public visibility after client reality, CRM, win/loss, support, sales, dealer, or implementation signals appear.

Short output: include only players whose ranking implication changes; omit stable benchmark-only rows.

For each meaningful player separate:

| Field | Meaning |
|---|---|
| public_visibility | high / medium / low |
| client_reported_pressure | high / medium / low / unknown |
| historical_pressure | yes/no |
| latent_threat | yes/no |
| benchmark_only | yes/no |
| channel_or_partner | yes/no |
| direct_competitor_status | direct / substitute / partner / benchmark / unknown |
| ranking_implication | promote / downgrade / split by arena / watch / no-op |

Highlight: high public visibility + low field pressure; low public visibility + high field pressure; historical-only; benchmark-only; channel/partner but not direct competitor.

## Client Correction Packet

If a client/expert/dealer/sales/support/implementation call follows external research, build:

| external finding | client correction | effect on priority | evidence needed | action |
|---|---|---|---|---|

Use categories:

- confirmed;
- strengthened;
- weakened;
- contradicted;
- renamed / normalized;
- added by client;
- moved to historical;
- moved to partner/channel;
- moved to benchmark;
- requires CRM/win-loss.

If correction affects data, commercial experience, implementation rhythm, CRM, ownership, or data model, route explicitly to BPM-4, BPM-5, BPM-9, BPM-10, BPM-11.

Short output: include only changed categories: confirmed, strengthened, weakened, contradicted, renamed, added, moved, or requires CRM/win-loss.

## Commercial Mechanics

For competitor, battlecard, channel, sales-play, or pricing claims, check whether pressure may come from commercial mechanics rather than product superiority:

- VAT / no VAT / individual entrepreneur status;
- purchase volume and procurement terms;
- COGS / margin / stock availability;
- insurance cushion / warranty / service;
- discount rules and agent economics;
- sales motivation effects;
- implementation labor and integration effort;
- opportunity cost and support burden.

If not checked, mark `commercially incomplete` and route evidence needs to BPM-4/BPM-5/BPM-9/BPM-10/BPM-11 as relevant.

Short output: list only unchecked commercial mechanics that could change ranking, priority, or claim safety.

## Naming Normalization / Transcript Safety

Names from voice, OCR, auto-summary, transcript, or informal speech are candidates, not confirmed entities.

Short output: show only names that affect routing, competitor identity, partner identity, source attribution, or task ownership.

Return:

| raw_name | likely_normalized_name | confidence | why | needs_confirmation_from | status |
|---|---|---:|---|---|---|

Status should remain `normalized_candidate` until confirmed by source-check, client confirmation, CRM, document, website, or project owner.

## Storyline / BPM-SI Effect

Always separate:

| Group | Meaning |
|---|---|
| появились | new hypotheses, SI, SIF, tasks, evidence gates |
| усилились | prior hypotheses gained stronger evidence |
| ослабли | prior hypotheses became less safe, downgraded, or narrowed |
| нет существенной дельты | no meaningful change |

For BPM-SI, classify the signal:

- canonical SI candidate;
- donor SIF cluster;
- watch;
- no-op;
- wrong receiver;
- below threshold.

Never promote to canonical SI without repeatability, reviewer gate, or explicit accept when required by current standard.

Minimum output is always required: `появились / усилились / ослабли`. If empty, write `нет существенной дельты`.

After the Storyline delta, show the implementation lineage when applicable:

```yaml
approved_bpv_lineage:
  source_bpm: []
  si_ids: []
  storyline_slide_ids: []
  deck_artifact: ""
  deck_version: ""
  approval_event_or_decision: ""
  approved_slide_ids: []
  bpv_route: []
  reverse_bpv_link: written|proposed|missing|not_applicable
  training_mirror: []
  status: accepted|candidate|trace_gap|no_op
```

## Task Delta Overlay

If an executable task, owner, next action, blocker, project gap, or accepted follow-up appears, produce a Task Inbox packet instead of writing directly to Task OS / tracker / Airtable:

| task_delta | project | delivery_type / RG | owner | due_or_event | expected_output | why | source | target_airtable | matched_existing_task | decision_state | sync_status |
|---|---|---|---|---|---|---|---|---|---|---|

Use:

- `decision_state=accepted` only when Ilya already accepted the action;
- `sync_status=pending_airtable` only when the correct Task Inbox / bridge route exists;
- `decision_state=needs_human` or `proposed` when action is not accepted.
- Default when accept is not explicit: `decision_state=needs_human`, `sync_status=not_sent`.
- Do not use `pending_airtable` unless a correct Task Inbox / bridge target exists.

Show task content, not only IDs.

## Upstream Skill Inputs

Expected minimum fields from upstream outputs:

| Upstream | Minimum fields to consume | If missing |
|---|---|---|
| `deepresearch` | source type, public claims, evidence confidence, BPM-7A/B relevance, client reality questions, data needs | keep as public evidence map; no durable claim |
| `competitor-research` | competitor classification, arena, public visibility, field reconciliation questions, source-check status | do not rank by visibility alone |
| `presentation-qa` | claim-risk, weak evidence, trace gap, missing source, affected slide/storyline claim, deck artifact/version, approval status | ask source BPM; keep BPV as candidate if approval evidence cannot be found |
| `rail` | project mode, launch point, tracker/task drift, receiver gap, accepted/proposed repair | do not convert rail drift into Storyline gap without receiver check |
| BPM-4 skills | dataset/source, formula branch, anomaly/hypothesis, required secondary BPM, data gap | do not call anomaly a market claim until BPM-6/7/10 check |
| `ingest` | material type, canonical status, route proposal, no-op reason, task_delta candidate | preserve decision_state and writeback boundary |

Failure modes per upstream:

| Failure | Handling |
|---|---|
| `deepresearch` gives TAM/share without client data | mark `external_public / needs_BPM4_BPM10_reconciliation` |
| `competitor-research` gives web-visible ranking | split public visibility from field pressure |
| `presentation-qa` gives claim-risk without source | route to source BPM; keep claim weak/no-op until source found |
| `rail` flags missing Storyline from report-layer | inspect receiver mode and primary source before gap |
| BPM-4 skill finds growth lever without margin/source fields | mark `commercially incomplete` |

## Output Shape

Use this structure unless the user asks for a shorter packet:

1. Управленческая картина: what the system learned.
2. Cross-BPM exchange table.
3. Governance: conflicts, TTL/stale, work-log, no-op/false-positive, skill capability gaps.
4. Client Reality Reconciliation.
5. Field Pressure Reconciliation.
6. Client Correction Packet.
7. Commercial Mechanics.
8. Naming Normalization.
9. Storyline-Storyboard / BPM-SI effect: появились / усилились / ослабли.
10. Approved presentation / decision -> BPV lineage and reverse links.
11. Skill / Rule / Automation patch candidates.
12. Task delta packets.
13. Human gates.

Always separate `facts`, `inference`, `proposals`, and `accepted/unchanged canon`.

For short output, use:

1. Управленческая картина.
2. Top signal routes / no-op.
3. Storyline/BPM-SI delta.
4. BPV lineage / no-op.
5. Task_delta / human gates.

Template phrases:

- `Факты:` source-grounded observations only.
- `Инференция:` interpretation from sources.
- `Предложение:` writeback or patch candidate.
- `Канон без изменений:` accepted rule / project state that remains unchanged.

## Writeback Boundary

This skill may read and propose. It must not durably edit:

- `BPM Storyline-Storyboard`;
- `Матрица BPM — SI`;
- rules / AGENTS / `.Codex/rules`;
- skill files;
- project trackers / Task Inbox;
- Airtable / external task systems;
- commercial trace;

unless Ilya explicitly accepts the specific writeback.

Allowed without separate accept:

- update automation memory when the current run is an automation and memory update is required;
- produce a chat-only reconciliation packet.

After any accepted Vault `.md` writeback, verify both layers:

- YAML/frontmatter parses with Ruby safe YAML when frontmatter is present;
- Obsidian-safe Markdown passes targeted search: no local absolute markdown links, `file://`, URL-encoded `%20` paths, or `#`-tags in frontmatter; internal Vault navigation in body text uses `[[wikilink]]` / `[[wikilink|alias]]`.

## Decision Footer

End any non-trivial packet with explicit gates:

| Gate | Proposed action | Target | Decision needed |
|---|---|---|---|

Use concise decision phrases:

- `акцепт на Storyline writeback`;
- `акцепт на BPM-SI donor/candidate update`;
- `акцепт на approved decision -> BPV writeback`;
- `акцепт на Task Inbox packet`;
- `акцепт на rule/skill/automation patch`;
- `no-op confirmed`.

## Regression Evals

| Case | Expected | Forbidden |
|---|---|---|
| MPP | BPV-03.7 primary, BPV-04.4 adjacent | BPV-04 as MPP parent |
| data / analytics / RAG / DPM | BPV-05 / 10 / 11 / 12 | old BPV-11 / 12 / 13 / 14 map |
| training | subject BPV + BPV-14.x + BPV-14.R or no-op | only 1-ка landing |
| unapproved slide | BPV candidate / trace gap | accepted BPV |
| approved deck | exact deck/version/decision and reverse BPV link | one-way BPV note |

## Common Failure Modes

| Failure | Correction |
|---|---|
| Treating public research as lived market reality | Run Client Reality Gate and keep public packet as evidence map |
| Treating journal/raw-pack as primary BPM source | Inspect referenced primary file; default report-layer to no-op |
| Creating Storyline gap for New Delivery | Classify receiver mode first; donor-only unless accepted otherwise |
| Ranking competitors by SEO/web presence | Split public visibility from field pressure |
| Writing tasks directly to tracker/Airtable | Produce Task Inbox packet and decision_state |
| Promoting donor pattern to SI canon too early | Require repeatability / reviewer gate / accept |
| Promoting an unapproved slide directly to BPV | Keep candidate until deck/version and approval decision exist |
| Using pre-canonical BPV numbering | Normalize through the current BPV-01...14 registry before routing |
| Copying the standard into the skill forever | Reload live standard each run |

## Structured Analytical Artifact Exchange Gate

When an exchange candidate is a Problem Map pattern, issue/hypothesis tree, classification, evidence/claim/source-to-node schema, analytical visual, storyline-storyboard pattern, metric tree, or dimension architecture, inherit the live global contract in `~/.codex/AGENTS.md`. Transfer the method contract separately from donor/project evidence; a donor artifact, methodology page, Frappe, or Quartz never proves the receiver project's facts. Require adaptation/no-transfer gates, explicit MECE applicability, source rights, and delta landing into an existing receiver artifact before canonization.
