---
name: presentation-qa
description: Use when reviewing strategic presentations, slide decks, section-slide drafts, storyboards, or client-facing deck iterations for source fidelity, storyline integrity, MECE structure, claim calibration, client readiness, regression across versions, and slide-level QA. Especially useful for Paper Planes strategy decks, BPM/4th department projects, consulting presentations, and cases where facts must not be lost while simplifying the narrative.
metadata:
  version: "0.1.3"
  status: draft
  line: strategic-presentation-quality
  owner: Ilya
  supports_bpm:
    primary: [BPM-SI, Storyline-Storyboard]
    required_secondary: [BPM-2, BPM-4, BPM-6, BPM-7A, BPM-7B, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-3, BPM-5, BPM-8, BPM-9]
  can_consume: [presentation / deck / storyboard versions, prior QA packet, BPM Storyline-Storyboard, Матрица BPM — SI, actant map, sub-BPV actant-action profiles, source indexes and claim ledgers]
  can_produce: [QA packet, claim-risk ledger, weak-evidence / trace-gap events, actant-action coverage counter, sub-BPV action score map, bridge-slide candidates, reusable QA learning]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-07-13: Added annotation regression ledger, semantic underfill, semantic-role substitution, terminology precision and target-PDF-renderer receipts."
      - "2026-07-11: Added SI/slide-intent bridge between actant-action and BPV-route checks."
      - "2026-07-11: Added Estuarine-first order and code+name readability requirement for BPV-route checks."
      - "2026-07-11: Added sub-BPV x actant-action score checks and fixed output section numbering."
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# Presentation QA

## Purpose

Use this skill to run a rubric-based QA review of a strategic presentation or slide/storyline layer.

The skill is a QA judge, not a deck author. It checks whether the current presentation version can be used for the current stage without losing project logic, distorting sources, overclaiming, or creating client-facing risk.

## Governance contract

This skill sits on a client-facing artifact boundary. Before calling a deck `client-ready`, it must explicitly check:

1. `source_class`: what kind of evidence supports each material claim;
2. `claim_usability`: whether each claim is client-ready, internal-only, source-check, appendix-only, or do-not-use;
3. `exhibit_readiness`: whether slide titles, exhibit titles, visuals, caveats, and source notes support the intended management decision;
4. `dlp_readiness`: whether internal methods, client-sensitive facts, delivery risks, pricing logic, or unapproved cases are exposed;
5. `writeback_boundary`: whether the user asked only for QA or also for file edits, deck edits, task_delta, or external-facing text.

For Paper Planes decks assembled through Rail/BPA, `client-ready` additionally requires:

- confirmed use of PP Presentation Kit 2026-07-12: canonical deck-content template, slide taxonomy, visual-style guide, PPTX builder rule and both critics;
- `PP_visual_likeness_passed` from the HTML/render stage;
- a completed `pp-text-critic` report;
- a completed `pp-slide-critic` report;
- confirmation that `text-deai-editor` client-deliverable mode was applied to audience-visible copy; `balakhnin-voice` is required only when Ilya explicitly requested authorial stylization;
- real global logo, accepted PP typography/brand field, montage review and zero unresolved overflow/overlap;
- no use of `consulting-slides-creator` as the final production generator.

If any item is missing, return `PP_production_QA_incomplete`; do not substitute this skill's general verdict for the missing specialist critic or visual-likeness gate.

The canonical palette is white `#FFFFFF`, ink `#181D27`, coral `#FF5850`, with governed soft status colors from the installed visual-style guide. Treat legacy Elevel/PAPER `#EFEBE7` without an explicit approved project override as `pp_palette_legacy_drift`.

Reject a PP visual pass when it is supported only by CSS palette changes, runtime text replacements, an unverified reconstructed logo, a declared-but-unverified font, overflow counts, or self-reported logo counts. Require source-copy cleanup, real silhouette changes by slide ID, durable asset provenance, rendered-font verification, both PP critic reports and montage evidence.

Apply Natasha Tokaeva's production contract as a hard gate. For each substantive slide, verify that the management thought selects the renderer; reject universal card grids used for causality, comparison, routes, organization, decisions or evidence. Verify a locator-level claim evidence ledger, production-MD source-copy cleanup before render, and a stable color dictionary. A methodology appendix, generic source footer or CSS acceptance layer cannot substitute for these controls. Any failure returns `hold_before_client`.

Do not turn QA findings into file edits, new slides, task registrations, or client-final text unless Ilya explicitly asks and the relevant writeback/preflight gate is satisfied.

## Non-goals

Do not:

- rewrite the whole presentation;
- invent a new storyline;
- improve content "from yourself" without source basis;
- replace project strategy with an alternative consultant opinion;
- treat external benchmarks as proof of applicability;
- turn hypotheses, proxy sizing, or proposed thresholds into verified conclusions;
- create or edit files unless explicitly asked.

## Trigger Conditions

Use this skill when the user asks to:

- review a presentation, deck, slides, storyboard, storyline, section slides, or HTML slide draft;
- compare a new version of slides with a prior review;
- check MECE, consistency, source fidelity, storyline, claim risk, or client readiness;
- QA a strategic presentation before client discussion;
- identify lost facts, risky claims, missing bridge slides, or weak proof-layer;
- build feedback for a deck team without rewriting the deck.

Typical triggers:

- "проверь презентацию";
- "оцени слайды";
- "проведи QA";
- "сравни новую версию";
- "что стало лучше/хуже";
- "проверь на MECE";
- "проверь claims";
- "не потеряли ли фактуру";
- "готово ли клиенту";
- "section-slide / storyline layer".

## Required Inputs

Minimum:

- current presentation / slide text / HTML / PPT / storyboard;
- target gate or intended use, if known.

Strongly preferred:

- prior review packet, if this is a later version;
- previous presentation version, if delta-review requires factual change comparison;
- project storyline / storyboard;
- accepted decisions;
- source materials or source index;
- BPM -> SI matrix for BPM projects;
- supporting interview summaries, raw transcripts, dashboards, benchmark packets, competitor packets, or research packets;
- known must-preserve facts and must-not-overclaim zones.
- project-specific regression checklist;
- internal-only terms list.

If inputs are missing, do not invent them. Mark as `нет в пакете`.

## Input Contract

Treat inputs as an explicit review packet:

```yaml
input_contract:
  new_deck_version: "required"
  target_stage_or_gate: "strongly_preferred"
  previous_review_packet: "optional_but_required_for_delta"
  previous_deck_version: "optional"
  source_pack: "optional"
  project_regression_pack: "optional"
  project_storyline_or_storyboard: "optional"
  client_context: "optional"
  internal_only_terms: "optional"
```

Fallback rules:

- If `previous_review_packet` is absent, run `first_pass_review`; do not claim delta-review.
- If `source_pack` is absent, set maximum claim status to `interpretive but plausible` or `not assessable`.
- If `project_regression_pack` is absent, build a temporary one from `project_logic_map`, accepted decisions, and prior QA; mark it as `temporary`.
- If `target_stage_or_gate` is absent, infer it and mark the inference as an assumption.

## Missing Materials Rule

Before doing substantive QA, identify what is actually present.

- If prior review packet is missing, do not perform true delta-review. Write `delta-review not possible`, run baseline QA on the current version, and list what is needed for delta-review.
- If previous deck version is missing but prior review packet exists, run delta-review against the prior issues only. Do not claim specific slides changed. Use `appears fixed`, `appears still risky`, or `not assessable`.
- If evidence pack is missing, do not mark claims as `verified`. Use at most `interpretive but plausible`; claims needing proof become `not assessable from provided materials`.
- If target gate is missing, infer the most likely gate from artifact stage, mark it as an assumption, and do not apply client-ready standards to a skeleton.
- If internal-only terms list is missing, use the default client-language red flags and mark the list as `нет в пакете`.

## Operating Mode

Work as a QA judge.

Compare:

1. current deck;
2. project storyline / storyboard;
3. source materials;
4. prior QA, if available;
5. known project principles and constraints.

Do not substitute your own strategy for project logic. If another structure looks better but the current structure is coherent, recommend only local fixes.

## Reviewability Gate

Before scoring, return a short reviewability gate.

| Check | pass / fail / weak | Comment |
|---|---|---|
| Current deck/version is available |  |  |
| Artifact stage is understandable |  |  |
| Target gate is explicit or safely inferred |  |  |
| Prior QA exists for delta-review |  |  |
| Previous deck version exists if factual comparison is needed |  |  |
| Evidence pack exists or absence is explicit |  |  |
| Material claims can be checked |  |  |
| Internal-only terms are known or default list applies |  |  |

If reviewability gate has a critical `fail`, do not pretend to run a full review. Return limited QA plus missing materials.

## Project Pattern Ingestion

This skill must work across different project chats and client projects. Do not treat Rosma-derived concepts or any prior project's concepts as universal QA objects.

Before running project-specific QA, ingest the project's own logic from available sources and build a compact `project_logic_map`.

Primary sources for project logic:

- current deck / storyboard / storyline;
- BPM Storyline-Storyboard, if present;
- BPM -> SI matrix, if present;
- project passport, subpassports, track notes, and stage-gate notes;
- source index, interview summaries, transcripts, dashboards, research packets, competitor packets, and accepted prior QA;
- explicit user statements in the current chat.

Extract these project-specific entities:

```yaml
project_logic_map:
  strategic_frame: ""
  core_mechanisms: []
  operating_model_blocks: []
  commercial_or_economic_logic: []
  channel_or_route_logic: []
  service_or_customer_experience_logic: []
  digital_or_tooling_logic: []
  marketing_or_demand_logic: []
  data_and_evidence_contract: []
  future_bets_or_hypotheses: []
  client_language_constraints: []
  must_preserve_facts: []
  must_not_overclaim_zones: []
```

Use this map as the project's QA reference. If a prior project used concepts like `zonal defense`, `revenue management`, `dealer protection`, `personal account`, `OEM`, or similar, treat them only as examples of possible logic slots. For a new project, replace them with the concrete statements and categories extracted from that project's own sources.

If the project logic map cannot be built from the supplied packet, mark missing fields as `нет в пакете` and QA only against available evidence.

## Project Logic Trace Layer

The `project_logic_map` must be visible and traceable, not only inferred in the assistant's reasoning.

For every meaningful item in `project_logic_map`, maintain a trace row:

```yaml
project_logic_trace:
  logic_item: ""
  logic_slot: "strategic_frame|core_mechanism|operating_model|commercial_economic_logic|channel_route_logic|service_cx_logic|digital_tooling_logic|marketing_demand_logic|data_evidence_contract|future_bet|must_preserve_fact|must_not_overclaim_zone"
  source_artifact: ""
  source_status: "confirmed|partial|hypothesis|missing|contradicted"
  used_in:
    - slide_or_block: ""
      claim: ""
      role: "main_storyline|proof_layer|appendix|hypothesis|data_request|parking_lot"
  qa_status: "ok|risk|needs_source|overclaim|lost|misplaced"
  action: "keep|downgrade|move|source_check|rewrite|drop|request_data"
```

Trace direction must be two-way:

- from source / statement / project artifact to deck block, slide, claim, or storyboard item;
- from deck block, slide, claim, or QA finding back to the source / statement / project artifact that supports it.

This is a lightweight project-document trace, not a full Vault tunnel. Use `tunnel` only when a knowledge item must be routed into durable Vault architecture. For presentation QA, the required default is visible traceability inside the project documents and QA output.

If a project document lacks trace fields, flag this as `trace_gap` and recommend adding a trace block before client-ready review.

## Project Regression Pack

Project-specific checks must be separated from universal deck QA.

Do not hardcode a prior project's vocabulary as universal checks. Build or read a `project_regression_pack` for the current project:

```yaml
project_regression_pack:
  project: ""
  version: ""
  status: "provided|temporary|missing"
  checks:
    - id: "REG-001"
      check: ""
      why_it_matters: ""
      fail_signal: ""
      expected_fix: ""
      source_or_prior_issue: ""
```

Sources for the pack:

- previous review packet;
- accepted user decisions;
- project storyline / storyboard;
- project-specific risks from `project_logic_map`;
- prior regressions noticed in earlier deck versions.

If no pack is provided, use only universal checks plus temporary checks extracted from current project sources. Mark every temporary check as non-canonical.

## Previous Review Packet

When prior QA exists, expect or reconstruct this shape:

```yaml
previous_review_packet:
  deck_version: ""
  review_date: ""
  stage: ""
  issues:
    - issue_type: "claim_overreach|storyline_gap|missing_bridge|evidence_gap|language_risk|density_risk|regression"
      severity: "blocker|major|minor|watch|editorial"
      issue: ""
      location: ""
      required_fix: ""
      status_at_review: "open|partially_fixed|closed|watch"
```

## Stage Calibration

Before scoring, classify the artifact stage:

- `section-slide skeleton`;
- `storyline layer`;
- `intermediate content deck`;
- `client discussion draft`;
- `client-ready deck`.

Evaluate by the standard of that stage and by the next target gate.

Return:

| Current stage | Next stage | What blocks transition |
|---|---|---|

### Stage Strictness

| Stage | Check strictly | Do not require too early |
|---|---|---|
| `section-slide skeleton` | block logic, conclusion presence, crude regressions, missing bridges, obvious claim overreach | final proof-layer, polished language, finished visual design |
| `storyline layer` | causal transitions, claims vs hypotheses, bridge slides, route logic | full evidence base for every supporting claim |
| `intermediate content deck` | evidence coverage, density, client language, proof-layer structure | final client-ready polish |
| `client discussion draft` | management conclusions, risks, language, unsupported claims, readiness for discussion | absolute perfection of client-ready deck |
| `client-ready deck` | all blocker/major issues, language, evidence, visuals, route, no internal language | draft assumptions without caveat |

Rule: do not over-QA a skeleton. For `section-slide skeleton`, review storyline direction, stage legitimacy, missing bridges, obvious claim overreach, and regression risks.

### Slidument Density Calibration

For Paper Planes strategic B2B decks, defense decks, methodology decks, and consulting documents, dense slidument-style slides are not a defect by default. The preferred artifact may intentionally carry a full reasoning layer on the slide: claim, method, evidence, caveats, implications, and decision logic.

Do not recommend reducing a dense slidument to 7-8 lighter core slides or moving material to appendix merely because the slide is text-heavy. Dense layers are acceptable and often preferred when they:

- preserve the reasoning chain needed for C3/C4, client defense, or methodology review;
- let the reader reconstruct the argument without oral explanation;
- keep source logic, caveats, definitions, and decision implications visible;
- function as a client-facing working document, not a marketing pitch deck.

Flag density only when it creates a real QA problem:

- the management conclusion is buried or contradicted;
- hierarchy is unclear;
- the slide mixes incompatible logic levels without labels;
- the reader cannot tell what decision the slide supports;
- text physically overlaps, is unreadable, or defeats the exhibit's purpose;
- sensitive internal evidence is exposed in a client-facing layer.
- a large card or panel contains only a generic label and leaves the diagnostic question, known state, decision need and expected output implicit;
- a substantive slide presents Situation but omits the Complication for the client's objective or an evidence-supported Answer;
- geometry is formally balanced but a large region, table row or cell contains only a noun label, generic phrase or unexplained whitespace: flag `semantic_underfill` separately from overflow and occupancy;

For every substantive slide, audit `Situation -> Complication -> Answer` as a reasoning chain. The action title must state the Answer, while the exhibit must expose how the evidence leads to the implication. Do not require a literal three-column layout. Flag `slide_situation_only_fail`, `slide_complication_missing`, `slide_answer_unsupported`, `slide_exhibit_reasoning_gap`, `intro_card_underdeveloped`, or `slide_objective_scope_loss` when an accepted deliverable objective disappears during compression.

For HTML/PP Pages artifacts, score the viewing shell separately from slide content. Require discrete 16:9 slide screens, a complete collapsible thumbnail navigator, visible active state, reliable navigation, focused slide viewing and clean separation between shell controls and exportable slide content. Flag `pp_pages_shell_missing`, `pp_slide_navigator_incomplete` or `pp_shell_slide_layer_mixed`. Audit color as information architecture: every recurring color needs a stable named semantic role; decorative or shifting multi-color coding is `pp_color_semantics_undefined`.

Treat the production Markdown deck specification as the authoritative pre-render artifact. Before client-ready HTML/PPTX, verify deck-level objective/SCQA/SOSTAC sequence and slide-level SOSTAC role, structural class, SI/GS/library route, SCA, evidence, exhibit and assembly instructions. Compare visible render copy and claims to MD. Use `production_md_deck_spec_missing`, `production_md_not_source_of_truth`, `slide_dual_classification_missing`, `slide_library_address_missing` or `slide_spec_incomplete` when the contract fails.

Treat SOSTAC as a multi-value information-role axis: do not force a slide containing several roles into one label. Apply the canonical structural classes `technical / normative / reference / consulting / encyclopedic`. A consulting slide must document why normative/GS slides cannot prove the Question; SI cannot directly generate it. Promotion into GS/normative requires successful review/reuse evidence and a new SI.

Require machine-verifiable receipts before client-ready status: type rationale before render; no unapproved layout repeated over two consecutive substantive slides; exact source labels; first-five deck SCQA; complete ordered contact sheet; overflow/overlap, empty-space geometry and semantic-fill results; strict 16:9 screen/print/PDF/PPTX tests; golden example coverage; both PP critic reports after final rerender; and a final-page check in the target PDF renderer for pages with photos, overlays or prior color defects. Any missing receipt returns `hold_before_client`.

Audit objective prominence, not only presence. Reconcile every active macro-tension/accepted objective against the BPA.01 scope-disposition ledger and trace it through governing question, Answer/SCQA, narrative spine, production MD and opening slides. A core objective that appears only in a late slide is `objective_role_degraded`. Any owner scope correction after a pass requires upstream regeneration; otherwise flag `upstream_reopen_missing` and `stale_gate_after_scope_change`.

When density is useful, recommend improving hierarchy, headings, callouts, source labels, and reading order rather than splitting into lighter slides. Use appendix only for evidence that is not needed in the main reasoning chain.

## Core Rubric

Score each axis from 0 to 4:

- `0 = fail`
- `1 = weak`
- `2 = acceptable draft`
- `3 = strong intermediate`
- `4 = client-ready for current stage`

Axes:

1. `source fidelity` - does the deck match sources?
2. `storyline integrity` - does causal logic hold?
3. `structural MECE` - are logic levels separated?
4. `content sufficiency` - is each block developed enough for its role?
5. `claim calibration` - are hypotheses, facts, and claims correctly marked?
6. `client readiness` - is the language and confidence level safe for client use?
7. `actant-action coverage` - if the deck contains initiatives, roadmap, org changes, BPV/BPO-route, or business-model moves, are hypotheses classified by how they act on actants: `Stabilise`, `Destroy`, `Shift`, `Create`, `Monitor`, `Conditional`, `Trigger`, `Request`, `Interaction`?

For `actant-action coverage`, do not reward a deck for having many initiatives. Check whether the initiative mix is appropriate for the actant map and causal-regime status. Flag overuse of `Create`, missing `Interaction`, and `Monitor / Conditional / Trigger / Request` items presented as ready-to-launch implementation. If a strategy deck depends on external market, technology, regulation, or competitor moves but has very few `Trigger` hypotheses, flag a likely external-scenario gap.

If the deck claims a BPV/BPO-route, do not stop at the upper `BPV-XX` class. For BPV-route, identify the relevant `sub-BPV`, derivative, gate, or implementation mechanism and check its expected `sub-BPV x actant-action` scores on a `1-5` scale. Scores `4-5` mean the actant-action mechanism should be explicit in the initiative, gate, skill, or loop. Scores `1-2` require a project-specific explanation or a route reconsideration. Treat these scores as revisable methodology, not as permanent truth.

BPV-route checks must be problem/Cynefin-first, then Estuarine, then SI/slide-intent: before accepting the route, verify that the deck or QA packet shows `problem -> causal-regime domain -> actant -> type/subtype -> problem link -> zone/changeability -> possible action class -> SI / САИ / slide-intent -> initiative hypothesis`. If the route starts with actants before problems and Cynefin domain, mark `problem_map_missing / causal_regime_missing`. If action class is not linked to SI / slide-intent, mark `SI_slide_intent_missing`. If the route jumps straight to BPV codes, mark `premature_BPV_route`.

In human-facing QA output, never show a BPV or sub-BPV as code only. Use `BPV-08 — Система управления -> BPV-08.6 — Разработка и внедрение организационной структуры`. A bare `BPV-08 -> BPV-08.6` is a readability defect unless the names are shown in the same row.

## Severity Model

For every finding use one severity:

- `blocker` - cannot pass the next gate: breaks main storyline, contradicts sources, lacks evidence for a central claim, misses a critical bridge, or creates high client misunderstanding risk;
- `major` - serious logic, structure, content, claim, or client-confusion risk; should be fixed before C3/C4 review or client discussion;
- `minor` - local weakness that does not break the deck;
- `watch` - not an error yet, but may become a regression or gate risk in the next version;
- `editorial` - style or wording issue without material risk.

Do not mark cosmetics, personal taste, or ordinary wording polish as `blocker`. A blocker must be tied to next-gate risk.

## Fact / Claim Status

For every material claim use one status:

- `verified`;
- `partially verified`;
- `interpretive but plausible`;
- `hypothesis`;
- `unsupported`;
- `contradicted by source`;
- `dangerous as client claim`.

Do not confuse:

- fact;
- interpretation;
- hypothesis;
- recommendation;
- proposed metric;
- client-facing claim.

## Evidence Hierarchy

Use this hierarchy when calibrating claim strength:

1. Client-confirmed data / cleaned project dataset.
2. Raw interview transcript.
3. Processed interview summary.
4. Internal PP strategic synthesis.
5. External benchmark with source.
6. External proxy sizing.
7. Inference / consultant hypothesis.

If a claim relies mainly on levels 5-7, it cannot be `verified`; at most use `partially verified` or `interpretive but plausible`.

## Claim Ledger Contract

Material claims must be traceable. Use a claim ledger rather than loose comments.

```yaml
claim_ledger:
  - claim: ""
    deck_location: ""
    source: ""
    source_class: "client_confirmed_data|raw_transcript|processed_summary|accepted_internal_synthesis|public_source|external_research|benchmark|inference|missing"
    evidence_level: 1
    verification_status: "verified|partially verified|interpretive but plausible|unsupported|overstated|contradicted|not assessable"
    claim_usability: "client_ready|internal_only|needs_source_check|appendix_only|do_not_use"
    risk: ""
    required_action: "keep|downgrade|add_source|add_disclaimer|move_to_appendix|mark_as_hypothesis|request_data"
```

Rules:

- No source means no verification.
- `verified` is allowed only when evidence level 1-3 supports the exact wording.
- Level 4 can support `partially verified` or `interpretive but plausible`.
- Levels 5-7 cannot support `verified`.
- Benchmark supports analogy, option, or hypothesis; it does not prove applicability.

Client-facing usability rules:

- `client_ready` requires source class, safe wording, and no unresolved DLP issue.
- `internal_only` applies to delivery-risk, private methodology labels, pricing logic, unapproved client analogs, weak strategic hypotheses, and sensitive project facts.
- `needs_source_check` applies when the claim may be true but lacks a traceable source or exact wording support.
- `appendix_only` applies to useful evidence that should not drive the main storyline yet.
- `do_not_use` applies to contradicted, stale, overclaimed, sensitive, or unapproved claims.
- External research, NotebookLM, Perplexity, ChatGPT Pro, public benchmarks, and competitor packets cannot become `client_ready` unless reconciled with project/client evidence or explicitly accepted by Ilya for that use.

## Exhibit Readiness Gate

For client-facing or C3/C4-facing decks, check not only whether a slide has content, but whether the exhibit can carry a decision.

```yaml
exhibit_readiness:
  - slide_or_block: ""
    exhibit_title: ""
    action_title: ""
    visual_type: "table|matrix|heatmap|2x2|timeline|waterfall|map|battlecard|diagram|text_only|other"
    decision_role: "frame|evidence|choice|tradeoff|roadmap|risk|appendix|bridge"
    claim_usability: "client_ready|internal_only|needs_source_check|appendix_only|do_not_use"
    source_note_present: true|false
    caveat_present_if_needed: true|false
    readiness: "slide_ready|needs_title_fix|needs_visual_fix|needs_source|appendix_only|do_not_use"
    fix: ""
```

Rules:

- A slide title must state a management conclusion or clear decision role, not only a topic label, unless the artifact stage is only a skeleton.
- A visual that looks polished but carries a weak or unsupported claim is not slide-ready.
- A strong claim buried in a weak title should be flagged as `needs_title_fix`.
- A visual with no source/caveat for material numbers or rankings should be flagged as `needs_source`.
- If the slide is useful only as evidence, benchmark, or hypothesis, move it to appendix/support rather than main storyline.

## Required Tests

### 1. Source Fidelity Test

Check:

- whether every material claim matches sources;
- whether the deck strengthens a claim beyond the source;
- whether qualifiers and caveats were lost;
- whether benchmark is used as analogy, not proof;
- whether hypotheses are presented as confirmed.

Return disputed items as:

| Claim | Status | Source / missing source | Risk | Fix |
|---|---|---|---|---|

### 2. Storyline Integrity Test

Check:

- whether section titles / action titles form a continuous management story;
- whether the story can be reconstructed without oral explanation;
- whether each block creates the need for the next;
- whether upstream and downstream blocks are in the right order;
- whether proof-layer is not mistaken for main narrative;
- whether appendix / future bets entered the main storyline too early.

Return:

| Break | Severity | Why it matters | Fix |
|---|---|---|---|

### 3. Structural MECE Test

Check that these levels are not mixed:

- main narrative;
- strategic mechanism;
- operating model;
- channel rule;
- service / CX layer;
- supporting proof;
- benchmark;
- appendix;
- future bet.

Also check whether the project's own extracted entities are confused with each other. Use `project_logic_map`, not Rosma-specific defaults.

Common slots to check, filled from the current project sources:

- strategic frame vs tactical initiatives;
- core mechanism vs supporting proof;
- commercial/economic logic vs discount or pricing mechanics;
- marketing/demand logic vs traffic mechanics;
- channel/route logic vs sales activity;
- service/customer-experience logic vs digital tool;
- digital/tooling logic vs standalone IT feature list;
- data/evidence contract vs unverified claim;
- future bet vs current recommendation;
- operating model / roles / KPIs vs storyline evidence.

Return:

| Mixed items | Logic levels | Why it is bad | How to separate |
|---|---|---|---|

### 4. Content Sufficiency Test

For each block, assess:

- whether it has management meaning;
- whether it has a thesis, not only a topic;
- whether it needs proof-layer now;
- whether it is too empty for current stage;
- whether it is too detailed too early.

Classify each block:

- `section slide`;
- `intermediate content slide`;
- `underdeveloped`;
- `over-decomposed`;
- `misplaced`;
- `should move to appendix`.

### 5. Claim Calibration Test

Check:

- overconfident wording;
- vague claims that need sharpening;
- unsupported absolutes;
- numbers, thresholds, sizing, leader claims without source;
- accent numerals, `X -> Y` arrows, comparison labels, diagram captions and action-title precision without exact source object and locator;
- hypotheses needing labels;
- proposed rules that belong in appendix before validation.

Flag especially:

- counts of initiatives / tactics / options that look precise but are not sourced;
- thresholds, rules, prioritization logic, or gating criteria without evidence;
- competitive imitability / defensibility claims without proof;
- market sizing / proxy sizing;
- digital tools, dashboards, portals, personal accounts, CRM, AI, or automation claims treated as strategy without management function;
- direct sales / partner / channel / route claims without project evidence;
- product/category expansion, OEM, segment entry, or new-offer conclusions without source support;
- CRM / dashboard / dataset readiness.

### 6. Lost Fact Test

Find confirmed or important project facts that are:

- absent;
- too weak;
- misplaced;
- meaningfully distorted;
- wrongly moved to appendix;
- wrongly elevated into main narrative.

For each, assign a destination:

- `main narrative`;
- `proof-layer`;
- `appendix`;
- `data request`;
- `parking lot`;
- `drop for this deck`.

Return:

| Fact | Loss status | Correct layer | Why it matters | How to include without overload |
|---|---|---|---|---|

### 7. Client Readiness Test

Check:

- internal words not safe for client;
- unnecessary anglicisms;
- methodology instead of management conclusions;
- topic headings instead of conclusion headings;
- places needing more evidence;
- places needing lower confidence;
- whether the deck can be shown without oral translation.

Client-language red flags:

- internal words: `raw`, `processed`, `BPM`, `SI`, `storyline`, `MD-файл`, unless already disclosed;
- unnecessary anglicisms or imported project slang when a precise Russian management term exists;
- prior-project vocabulary carried into a new project without source support;
- words such as `самый`, `обязательный`, `единственный`, `доказано` without strong evidence.
- vague consulting containers such as `контур`, `архитектура`, `дизайн`, `система`, `гейт`, `скафолд` unless the slide names the managed object, composition and function;
- semantic-role substitution: client `requirements/expectations` rewritten as company `promises` or contractual `obligations`, or vice versa;
- generic object names such as `portfolio` when the accepted object is `project portfolio`, or `design` when the accepted stage is `design of structure`.

For each language risk, assign one action:

- `заменить` - use a client-facing Russian management term;
- `раскрыть при первом использовании` - keep the term but explain it once;
- `допустимо, если определено` - term is allowed if the project/client already uses it;
- `оставить только для внутреннего слоя` - do not expose in client-facing deck.

### 8. Bridge-Slide Detector

Find where a bridge slide is needed.

Common transition types, filled from `project_logic_map`:

- market/category context -> strategic frame;
- strategic frame -> core mechanisms;
- core mechanism -> commercial/economic logic;
- commercial/economic logic -> channel / route / sales model;
- channel / route / sales model -> service / CX / digital/tooling logic;
- service / CX / digital/tooling logic -> data, KPIs, roles, or operating model;
- hypotheses -> validation plan / roadmap.

Return:

| Between blocks | Why bridge is needed | What it must explain |
|---|---|---|

### 9. Block Density and Slide Density

Assess density on the right level and against the artifact's intended genre. In Paper Planes B2B consulting work, dense sliduments can be the target format.

If only outline / storyline / section-slide skeleton exists, slide-level judgment is `not assessable`; review block-level density only.

For each block, assess:

- does the density preserve or obscure the reasoning chain?
- is this intended as a slidument / working defense layer or as a presentation-only slide?
- would splitting lose necessary source logic, caveats, or decision trace?
- one clear main takeaway?
- visual form matches the thought?
- too many classifications on one screen?
- is every large region semantically occupied by a claim, mechanism, evidence, decision, owner, criterion or explicit evidence gap?

If actual slides exist, also assess each slide:

- title vs visual consistency;
- one-screen cognitive load;
- whether the chart/table supports the action title;
- whether source notes and caveats fit without clutter;
- whether multiple classifications compete on the same slide.

Use:

- `ok`;
- `dense_but_valid`;
- `dense_needs_hierarchy`;
- `too_dense_for_decision`;
- `visually unclear`;
- `not assessable`.

### 10. Delta Review Mode

If there is a prior review or previous version, compare against it.

Return:

| Prior issue | Current status | Improvement / regression | Residual risk |
|---|---|---|---|

For annotated revisions, also maintain a regression ledger:

| Annotation | Exact accepted replacement | Production-MD changed | Rejected form swept globally | Same error class checked | Affected pages rerendered | Final artifact reopened |
|---|---|---|---|---|---|---|

A local patch to HTML/PDF without the production-MD change does not qualify as `fixed`. Any user annotation invalidates prior text, render and export receipts for the affected artifact until this ledger is complete.

Statuses:

- `fixed`;
- `improved but still risky`;
- `unchanged`;
- `regressed`;
- `new risk introduced`;
- `not assessable`;
- `appears fixed`;
- `appears still risky`.

Do not evaluate later versions in isolation when prior QA exists.

### 11. Regression Checklist

Check whether previously found errors returned.

Default checklist:

- project-specific strategic frame not replaced by an arbitrary initiative list;
- extracted project mechanisms not replaced by prior-project vocabulary;
- hypotheses not converted into norms;
- benchmark not used as applicability proof;
- future bets not elevated into main storyline;
- digital/tooling object not reduced to feature list when its role is an operating mechanism;
- commercial/economic logic not reduced to discounts or pricing mechanics;
- data contract not dropped before data-heavy claims;
- contact / influence / route / sale distinctions not collapsed;
- proxy sizing not presented as market fact.

Return `pass / fail / weak` for each relevant item.

### 12. Trace-to-Action

Every `blocker` and `major` must become a concrete action.

Return:

| Problem | Action type | Where to fix | What should change | Gate |
|---|---|---|---|---|

Action types:

- `rewrite title`;
- `add bridge slide`;
- `move to appendix`;
- `add disclaimer`;
- `downgrade claim`;
- `add proof-layer`;
- `request data`;
- `split block`;
- `merge block`;
- `remove internal language`;
- `clarify route`;
- `restore evidence link`;
- `mark as hypothesis`.

`rewrite title` means direction or example only, not final authoring. Prefer actions such as `turn topic into conclusion`, `downgrade overclaim`, or `replace method label with management claim`. Do not write the deck for the author.

Each action must be local. Do not rebuild the whole deck if the current project structure is workable.

## Final Route Decision

End with one recommended route:

| Route | Meaning |
|---|---|
| `continue assembly` | current version is safe enough to keep building |
| `revise before C3/C4` | fix material issues before senior review |
| `hold before client` | do not show to client yet |
| `return to evidence` | source clarification, data, or proof-layer is needed first |
| `storyline escalation` | C3/C4/partner decision is needed; this is not just editing |

Return:

| Recommended route | Why | Minimal conditions to move forward |
|---|---|---|

## Anti-Authoring Boundary

If you see a better alternative structure, but the current project structure is workable, do not rebuild the deck.

Allowed:

- diagnostics;
- claim calibration;
- gap finding;
- local move recommendations;
- recommendation outline.

Forbidden:

- writing a new deck;
- changing the strategic frame;
- adding hypotheses without source;
- replacing the project storyline with your own.

## Senior Load Budget

Senior-facing QA must be compact. This limit applies to the QA answer, not to the deck being reviewed. Do not infer that the underlying deck should be made lighter, split into fewer core slides, or reduced to a pitch-deck format.

Default limits:

- no more than 5 material findings in the main answer;
- no more than 3 blockers;
- no more than 5 trace-to-action rows;
- exactly 1 final route decision;
- secondary notes go into appendix / secondary notes only if useful.

If there are more issues, group them into risk classes instead of forcing C3/C4 to read a raw QA dump.

## Output Contract

Return the review in this structure unless the user asks for a shorter version.

### 1. Reviewability Gate

| Check | pass / fail / weak | Comment |
|---|---|---|

If limited QA only is possible, say so here.

### 2. Stage Calibration

| Current stage | Next stage / target gate | What blocks transition |
|---|---|---|

### 3. Project Logic Map

Before scoring, show the ingested project-specific QA reference.

| Slot | Extracted project logic | Source / status |
|---|---|---|
| Strategic frame |  |  |
| Core mechanisms |  |  |
| Operating model blocks |  |  |
| Commercial / economic logic |  |  |
| Channel / route logic |  |  |
| Service / customer experience logic |  |  |
| Digital / tooling logic |  |  |
| Marketing / demand logic |  |  |
| Data / evidence contract |  |  |
| Future bets / hypotheses |  |  |
| Client language constraints |  |  |
| Must-preserve facts |  |  |
| Must-not-overclaim zones |  |  |

If a slot is unavailable, write `нет в пакете`.

### 4. Project Logic Trace

Show trace rows for the main project logic items used in QA.

| Logic item | Slot | Source artifact / status | Used in slide/block/claim | QA status | Action |
|---|---|---|---|---|---|

If trace is unavailable, write `trace_gap` and explain what document or source field is missing.

### 5. Delta Review

If prior review exists:

| Prior issue | Current status | Improvement / regression | Residual risk |
|---|---|---|---|

If prior review is missing, write `delta-review not possible`.

### 6. Regression Checklist

Separate universal checks and project-specific checks extracted from `project_logic_map` or `project_regression_pack`.

| Check | pass / fail / weak | Comment |
|---|---|---|

### 7. Actant-Action Coverage

If the deck contains initiatives, roadmap, org changes, BPV/BPO-route, commercial moves, or business-model moves, show the counter. If not applicable, write `not applicable` and why.

| Action class | Count of hypotheses / initiatives | Slide/block | QA risk |
|---|---:|---|---|
| `Stabilise` |  |  |  |
| `Destroy` |  |  |  |
| `Shift` |  |  |  |
| `Create` |  |  |  |
| `Monitor` |  |  |  |
| `Conditional` |  |  |  |
| `Trigger` |  |  |  |
| `Request` |  |  |  |
| `Interaction` |  |  |  |

Then add one short verdict: balanced / over-indexed / missing class / not assessable.

If a BPV-route is present, also show the sub-BPV score check:

| BPV-route code + name | sub-BPV / derivative / gate code + name | Action class used | Expected score 1-5 | Profile status | QA verdict |
|---|---|---|---:|---|---|

If the route names only an upper `BPV-XX`, mark `sub-BPV missing` and recommend decomposition before treating the route as implementation-ready.

If the route is not preceded by a problem/Cynefin and Estuarine table, add:

| Problem | Cynefin domain | Actant | Type / subtype | Zone / changeability | Possible actions | SI / САИ / slide-intent | Initiative hypothesis | BPV route |
|---|---|---|---|---|---|---|---|---|

Heuristics:
- `Stabilise`: client base, key employees, data access, critical budget, fragile operating rhythm.
- `Destroy`: stop doing something, close a harmful initiative, remove a fake process / report / channel.
- `Shift`: reduce the cost, conflict, energy, or time of change, for example PLM making new product launches easier.
- `Create`: create a department, role, expert-sales process, rule, owner, or routine.
- `Monitor`: watch a possible strategic bet such as ASU-EO until a signal is strong enough.
- `Conditional`: one change opens another, for example PLM enables a product contour.
- `Trigger`: predefine action after an external event such as market shift, regulation, competitor move, or technology signal.
- `Request`: ask for external permission, resources, designers, state support, contractor, or external expertise.
- `Interaction`: change org links, RASCI, handoff, SLA, decision rights, data flow, or meeting rhythm.

### 8. Top Blockers and Majors

| # | Severity | Break | Why critical | Fix |
|---|---|---|---|---|

### 9. Trace-to-Action

| Problem | Severity | Action type | Where to fix | What should change | Gate |
|---|---|---|---|---|---|

### 10. Bridge Slides Needed

| Between blocks | Why needed | What it must explain |
|---|---|---|

### 11. Claim Ledger

| Claim | Deck location | Source class | Source | Evidence level | Verification status | Claim usability | Required action |
|---|---|---|---|---:|---|---|---|

### 12. Exhibit Readiness

| Slide / block | Exhibit title | Visual type | Decision role | Readiness | Fix |
|---|---|---|---|---|---|

### 13. Client-Language Red Flags

| Language risk | Where | Why risky | Action | Suggested direction |
|---|---|---|---|---|

Actions: `заменить`, `раскрыть при первом использовании`, `допустимо, если определено`, `оставить только для внутреннего слоя`.

### 14. Block Density

Use when the artifact is outline / storyline / section-slide skeleton.

| Block | Density status | Main takeaway clear? | Visual readiness | Fix |
|---|---|---|---|---|

### 15. Slide Density / Visual Readiness

Use only when actual slide draft exists. If not, write `slide-level density not assessable`.

| Slide | Density status | Title/visual fit | Visual issue | Fix |
|---|---|---|---|---|

### 16. Preserve vs Simplify

| Fact / element | Current problem | Correct layer | Why |
|---|---|---|---|

### 17. Final Route Decision

| Recommended route | Why | Minimal conditions to move forward |
|---|---|---|

### 18. Final Management Summary

Answer in exactly 5 lines:

1. Can the team continue building on this version?
2. What must be fixed before the next showing?
3. What can remain internal draft?
4. What is the most dangerous claim?
5. What is the strongest element?

### 19. Secondary Notes / Appendix

Use only if needed and keep out of the senior-facing core.

#### Rubric Score

| Axis | Score 0-4 | Comment |
|---|---:|---|

#### MECE and Logic-Level Mixing

| # | Severity | Mixed items | Logic levels | Why bad | How to separate |
|---|---|---|---|---|---|

#### Fact and Claim Check

| # | Claim | Status | Source | Risk | Fix |
|---|---|---|---|---|---|

#### Lost or Underused Facts

| # | Fact | Loss status | Correct layer | Why important | How to include |
|---|---|---|---|---|---|

#### Block-by-Block Review

| Block / slide / section | Role | Block type | Assessment | Problem | Recommended fix |
|---|---|---|---|---|---|

#### Claims Under Risk

| Claim | Severity | Why risky | Needed source / softening |
|---|---|---|---|

#### Priority Fixes

Group fixes:

- `fix before any client discussion`;
- `fix before content fill`;
- `can stay for internal intermediate version`;
- `move to appendix or mark as future bet`.

#### Recommended Edit Structure

Only outline:

- what to raise;
- what to merge;
- what to subordinate;
- what to move to appendix;
- where to add bridge slides;
- where to add explicit disclaimer / data contract.

Do not write a new storyline.

#### Reusable QA Logic

If useful, list checks that should become reusable QA logic:

- mandatory checks;
- BPM / 4th department checks;
- source fidelity checks;
- logic checks;
- content sufficiency checks;
- client language checks;
- risky claim checks.

## QA Self-Check

Before finalizing, verify:

- I did not rewrite the deck instead of reviewing it.
- I did not replace project storyline with my own.
- I did not mark evidence levels 5-7 as `verified`.
- I did not treat benchmark as proof of applicability.
- I did not create too many blockers.
- Every blocker/major has an action.
- Senior-facing part is not overloaded.
- I explicitly said when delta-review is impossible.
- I separated current stage from client-ready standard.
- I did not expose sensitive data.
- I assigned source class and client-facing usability for material claims.
- I checked whether polished exhibits actually support the decision they appear to support.

## Writeback / Externalization Boundary

Presentation QA is read-only by default.

Allowed without additional approval:

- QA packet in chat;
- issue list;
- claim ledger;
- exhibit readiness table;
- recommended fixes as directions.

Requires explicit Ilya approval:

- editing the deck file;
- creating a new QA file;
- creating or updating Storyline-Storyboard, BPM matrix, source index, task tracker, or Vault documents;
- preparing final client-facing wording;
- sending or exporting material externally;
- registering task_delta candidates.

Before any durable action, use:

```yaml
presentation_qa_preflight:
  action_type: qa_only|edit_deck|create_file|update_storyboard|update_bpm_matrix|task_delta|externalize
  target:
  explicit_request_received: true|false
  source_class_check_done: true|false
  claim_usability_check_done: true|false
  exhibit_readiness_check_done: true|false
  dlp_status: public|internal|client_sensitive|restricted
  approval_required: true|false
  approval_received: true|false
```

If QA produces executable tasks, route them as `candidate` / `task_delta` to Codex Project Task Inbox after Ilya accepts the concrete list. Do not use CORD Task OS as the primary task home and do not write directly to Airtable without the Inbox handoff.

## BPM / 4th Department Add-on

When reviewing Paper Planes BPM / 4th department project decks, also check:

- each slide ties to a BPM/SI source or is marked as hypothesis;
- each material SI change is classified as `appeared|strengthened|weakened|unchanged` against the project Storyline-Storyboard when that artifact exists;
- if the deck contains initiatives, roadmap, BPV/BPO-route, org changes, or business-model moves, each material initiative / hypothesis has an `actant_action_class` and the QA packet includes an action-class counter: `Stabilise`, `Destroy`, `Shift`, `Create`, `Monitor`, `Conditional`, `Trigger`, `Request`, `Interaction`;
- if the deck contains a BPV-route, it is decomposed below the upper `BPV-XX` level into sub-BPV / derivative / gate, and its `sub-BPV x actant-action` scores are checked on the `1-5` scale; low-score deviations are explained or routed to profile review;
- BPV-route is checked only after problems, Cynefin domains, Estuarine actants, problem links, zones / changeability, possible actions, SI / slide-intents, and initiative hypotheses are visible; otherwise mark `problem_map_missing / causal_regime_missing / SI_slide_intent_missing / premature_BPV_route`;
- BPV / sub-BPV are written as `code + name`, not as bare codes;
- high-impact SI hypotheses with real interpretive forks have an answer-gate / `шлюз ответа по SI` proposal, but do not require answer-gates for every SI;
- external research has not replaced local project evidence;
- interviews are not summarized without raw transcript support when claims are strong;
- project facts are routed into `main narrative / proof-layer / appendix / data request`;
- storyboard and BPM -> SI matrix are used as the source of sequence;
- data-heavy claims have a data contract / dataset readiness caveat;
- client-facing conclusions do not expose internal process language;
- external competitor or market claims for a real client project are marked as public evidence only unless `client_reality_reconciliation_gate` has been completed through BPM-2 / BPM-3 and internal evidence;
- competitor names from transcripts, voice notes, OCR, auto-summary, or informal speech are not treated as confirmed competitors unless a normalization table or trusted confirmation exists.
- competitor ranking is not based on public visibility alone when BPM-2/BPM-3/client-side/CRM/win-loss evidence exists; require `field_pressure_reconciliation` before presenting priority competitors.

For unreconciled external research, maximum claim status is `public evidence only / not client-confirmed`. Do not allow a slide to present such claims as the client's lived market map, current installed base, active competitor threat ranking, or final commercial reality.

For transcript-derived competitor names, require:

| raw_name | likely_normalized_name | confidence | why | needs_confirmation_from |
|---|---|---|---|---|

Until confirmed, the slide / deck note must say `normalized_candidate`, not `confirmed_competitor`.

For priority competitor slides, require a field-pressure split:

```yaml
field_pressure_reconciliation:
  public_visibility: ""
  client_reported_pressure: ""
  historical_pressure: ""
  latent_threat: ""
  benchmark_only: true|false
  channel_or_partner: true|false
```

If this split is missing, downgrade the slide claim to `competitor map hypothesis` or `public visibility map`, not `priority threat ranking`.

If a client/expert/dealer/sales call happened after external research, require a `client_correction_packet` before accepting changed competitor priorities, battlecard emphasis, or client-facing competitor rankings:

| external finding | client correction | effect on priority | evidence needed | action |
|---|---|---|---|---|

Allowed categories: `confirmed`, `strengthened`, `weakened`, `contradicted`, `renamed / normalized`, `added by client`, `moved to historical`, `moved to partner/channel`, `moved to benchmark`, `requires CRM/win-loss`. If the correction affects data, implementation rhythm, CRM, or ownership, the QA output must route it to BPM-4, BPM-9, BPM-10, or BPM-11 instead of treating the slide as final.

For competitor battlecards or slides explaining why a competitor wins, check commercial mechanics before accepting the claim:

- VAT / no VAT / IP or similar tax structure;
- procurement volume;
- cost base / COGS;
- insurance or risk buffer;
- discount rules;
- effect of price on sales motivation;
- service and warranty cost;
- implementation effort;
- integration effort and opportunity cost.

If these are not checked, mark the battlecard or slide as `commercially incomplete` and route evidence needs to BPM-4 / BPM-5 / BPM-9 / BPM-10 / BPM-11.

## Done Definition

The review is complete when:

- reviewability gate is shown before substantive QA;
- missing materials are named and limited QA is declared when full review is impossible;
- actant-action coverage is checked or explicitly marked `not applicable` when the deck has no initiatives / roadmap / BPV-BPO route / org changes;
- BPV-routes are checked below the upper BPV level through sub-BPV / derivative / gate and `sub-BPV x actant-action` scores, or marked `sub-BPV missing`;
- BPV-route checks include a problem/Cynefin-first, Estuarine, and SI/slide-intent table or explicitly mark `problem_map_missing / causal_regime_missing / actant_map_missing / SI_slide_intent_missing / premature_BPV_route`;
- BPV and sub-BPV codes in the output include names;
- `input_contract` is respected and missing sources are not invented;
- `project_logic_map` is built from the current project's sources or missing slots are marked as `нет в пакете`;
- `project_logic_trace` is shown for main logic items, or missing trace is explicitly marked as `trace_gap`;
- project-specific checks are handled through `project_regression_pack`, not hardcoded from another project;
- QA checks use current-project extracted logic rather than Rosma-specific or prior-project defaults;
- the current artifact stage is named;
- target gate is explicit or safely inferred as an assumption;
- rubric scores are assigned;
- severity includes `watch` when something is not yet a defect but can regress later;
- claim ledger includes deck location, source, evidence level, verification status, and required action for material claims;
- claim ledger includes source class and client-facing usability for material claims;
- no claim without source is marked as `verified`;
- exhibit readiness checks slide/action titles, visual type, decision role, caveats, and source notes when slides or storyboard exhibits exist;
- blocker and major issues have trace-to-action fixes;
- risky claims are classified;
- lost facts are assigned to the right layer;
- prior-review regressions are checked if applicable;
- block density and slide density are separated; slide-level density is `not assessable` when there are no slides;
- `rewrite title` is treated as direction/example only, not final deck authoring;
- final route decision is one of `continue assembly`, `revise before C3/C4`, `hold before client`, `return to evidence`, or `storyline escalation`;
- senior-facing output is compact: no more than 5 material findings, 3 blockers, and 5 trace-to-action rows unless Ilya explicitly asks for full detail;
- the final management summary tells the team whether to continue building on the version;
- QA self-check passes before final answer.

## Eval hooks

When this skill is improved or audited through `skill-system-governance`, `skill-eval-harness` must test at least:

- a deck with no source pack cannot mark material claims as verified;
- a polished slide with unsupported ranking is flagged as `needs_source` or `do_not_use`;
- external research claims remain `public evidence only / not client-confirmed` until reconciled;
- client-facing deck review catches internal terms and DLP-sensitive facts;
- QA-only request does not edit files or create new deck artifacts;
- accepted follow-up tasks route to Codex Project Task Inbox as task_delta candidates, not to TaskOS as primary home;
- skeleton/storyline review does not over-QA visual polish as if it were client-ready.
- an unsupported `4 -> 6` accent claim is rejected even when the surrounding implication is plausible;
- `expectations`, `promises` and `obligations` are detected as distinct semantic roles;
- vague `contour`, `design`, `system` and `gate` labels fail unless their object, composition and function are named;
- a visually clean slide with a large empty region and one generic phrase fails `semantic_underfill`;
- an annotation marked “fixed” fails delta QA if the old wording remains elsewhere or production MD was not changed;
- a previously pink/tinted PDF cover requires target-renderer proof after export, not only a browser screenshot.
