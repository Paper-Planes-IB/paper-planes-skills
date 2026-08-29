---
name: bpv-03-7-mpp-sales-support
description: Use when preparing BPV-03.7 sales-support materials (МПП), sales enablement logic, or a proposal-adjacent support pack; keep BPV-04.4 as the adjacent КП/ТКП process and preserve CRM, analytics, and training mirrors without modifying the main commercial-proposal-generator skill.
metadata:
  status: experimental
  owner: Ilya
  line: BPV-03.7 / MPP / sales support
  primary_bpv: BPV-03.7 Материалы поддержки продаж
  adjacent_bpv:
    - BPV-04.4 Подготовка КП и ТКП
    - BPV-05.1 Проектирование и внедрение CRM
    - BPV-10 Аналитическая фабрика
    - BPV-14.3 Обучение продажам и коммерческим практикам
  legacy_directory_alias: bpv-04-mpp-commercial-proposal
  legacy_skill_aliases:
    - bpv-04-mpp-commercial-proposal
  parent_skill: commercial-proposal-generator
  created: 2026-06-11
  rg1_sources:
    - sales-support-skills-package-2026-06-11
    - Deafon content factory / sales MPP factory
    - STS presentation generator
---

# BPV-03.7 MPP Sales Support

## Purpose

Build the BPV side of MPP: not a client-facing КП draft, but a commercial support pack that explains how materials of sales support become an implemented sales capability.

This skill is adjacent to `commercial-proposal-generator`. Do not patch, override, or replace that skill. Use the main proposal skill when the requested artifact is the КП itself. Use this skill when the task is to build the BPV / MPP operating layer around a commercial proposal, sales kit, TKP, proof base, training, adoption, or sales enablement route.

When any output becomes slides, HTML, PP Pages or PPTX, route it through the full PP Presentation Kit 2026-07-12 and `pp-slidument`. This skill contributes MPP/BPV logic only and cannot materialize or accept the deck independently.

## Trigger

Use this skill for requests like:

- `собери БПВ-МПП`;
- `сделай skill вокруг МПП`;
- `разложи КП как МПП / sales enablement`;
- `подготовь support pack для продаж`;
- `что нужно внедрить, чтобы МПП работали`;
- `КП / ТКП / speed-to-TKP как BPV`;
- `связь КП, МПП, CRM, обучение, PST, adoption`.

Do not use it for:

- drafting the full client proposal text;
- archiving sent КП;
- changing pricing / scope / legal conditions;
- creating client-facing claims without the commercial proposal claim gate.

## Parent Objects

Canonical parent and adjacent proposal process in the BPV registry:

```text
BPV-03.7 Материалы поддержки продаж
-> adjacent BPV-04.4 Подготовка КП и ТКП
-> КП / ТКП support layer
-> CRM / SLA / training / adoption evidence
```

Neighbouring BPV parents:

| Signal | Route |
|---|---|
| CRM fields, statuses, SLA, reasons for delay | `BPV-05.1 Проектирование и внедрение CRM` |
| data readiness, solution base, source fields | `BPV-05.3` / `BPV-05.4` / `BPV-05.7` |
| TCO / ROI and commercial economics | `BPV-02 Финансовый менеджмент` |
| dashboard of proposal speed / deviation reasons | `BPV-08 Система управления` / `BPV-10 Аналитическая фабрика` |
| onboarding | `BPV-09 Управление человеческим капиталом` + `BPV-14.1` / `BPV-14.R` |
| PST, sales-role training, skill gate | subject trace in `BPV-03.7` / `BPV-04`, mirror in `BPV-14.3` / `BPV-14.R`, plus 1-ка |
| proposal archive, proof base, cases, one-pagers | 2-ка МПП / commercial functions |

## Workflow

1. **Preflight.** Identify whether the user needs a КП, an MPP support pack, a BPV implementation route, or a routing proposal. If the output is the КП itself, hand off to `commercial-proposal-generator`.
2. **Source map.** Check available sources: client request, proposal draft, archive КП, product showcase, cases, proof base, CRM trace, sales objections, RG-1/RG-2 materials when supplied.
3. **Sales job.** Select the MPP by the sales job, not by the asset name: objection, funnel stage, decision participant, proof gap, next action, or re-engage scenario.
4. **MPP object.** Define what kind of MPP is needed: one-pager, sales script, case block, FAQ, TKP template, TCO block, objection map, proof library, sales room asset, training unit, white paper, client-sendable memo, or manager prep note.
5. **Source gaps and reviewers.** Mark unsupported product, price, medical, legal, implementation, ROI, timeline, or case claims as `source_gap`; name who must review them.
6. **BPV route.** Keep `BPV-03.7` as the MPP parent, `BPV-04.4` as the adjacent proposal process, and translate the MPP into implementation logic: owner, rhythm, CRM fields, usage gate, training, adoption evidence.
7. **Commercial support packet.** Produce the packet below.
8. **Downstream.** Route strong patterns to the BPV registry, including the `BPV-14` training mirror when applicable, 2-ка MPP, 1-ка training, 8-ка knowledge unit, Storyline/BPM-SI, or no-op.

## RG-1 Heuristics Accepted Into This Skill

From the RG-1 packs, adopt these rules as BPV-MPP heuristics:

| RG-1 pattern | BPV-MPP use |
|---|---|
| Material is chosen by sales task, not title | start from objection / funnel stage / buyer role / next action |
| Sales-MPP registry | keep reusable MPP types with `send_when`, `manager_goal`, `barrier`, `reviewer` |
| BNT / BAND logic | classify barrier as budget, need, time, authority, technical fit, service / re-engage |
| `brief -> outline -> draft -> source-ledger -> QA` | every serious MPP has source trace and quality gate, not only client copy |
| Client artifact separated from working pack | client-sendable asset must not contain internal notes, prompt remnants, or production labels |
| Source gap discipline | do not invent product facts, cases, prices, terms, metrics, or sensitive claims |
| Reviewer discipline | name business / product / legal / medical / sales reviewer when needed |
| No pressure language | MPP helps the buyer decide; it does not "push" the buyer |
| Manager prep can be separate | for ABM / B2B presentations, keep sales preparation apart from client-facing Gamma / PDF |

Do not copy RG-1 client-specific wording into generic BPV-MPP. Extract only the operating pattern.

## Output Packet

```yaml
bpv_mpp_packet:
  mode: discovery|support_pack|skill_update_candidate|routing_only
  client_or_context: ""
  source_pack:
    proposal: ""
    archive_kp: []
    product_route: ""
    cases_or_proof: []
    rg_sources: []
    missing_sources: []
  mpp_object:
    type: one_pager|case_block|faq|tkp_template|tco_block|objection_map|proof_library|sales_room|training_unit|other
    user: sales|rop|presale|partner|client_owner|other
    job_to_be_done: ""
    funnel_stage: ""
    bnt_band_factor: budget|need|time|authority|technical_fit|service_reengage|other
    client_barrier: ""
    send_when: ""
    manager_goal: ""
    do_not_claim_without_source: []
    reviewer: ""
  bpv_route:
    parent_bpv: "BPV-03.7 Материалы поддержки продаж"
    adjacent_proposal_bpv: "BPV-04.4 Подготовка КП и ТКП"
    neighboring_bpv: []
    owner_client: ""
    owner_pp: ""
    rhythm: ""
    crm_fields: []
    sla_or_gate: []
    adoption_evidence: []
    training_mirror:
      subject_bpv: "BPV-03.7"
      bpv_14_routes: ["BPV-14.3"]
      educational_registry_14r: update|proposal|no_op
  approved_lineage:
    source_bpm: []
    si_ids: []
    storyline_slide_ids: []
    approved_deck_artifact: ""
    approved_deck_version: ""
    approval_event_or_decision: ""
    approved_slide_ids: []
    reverse_bpv_link_written: true|false|not_applicable
  rg1_quality:
    client_artifact_separated: true|false
    source_ledger_required: true|false
    qa_required: true|false
    source_gaps: []
    pressure_language_risk: low|medium|high
    reviewer_needed: []
  proposal_link:
    use_commercial_proposal_generator: true|false
    reason: ""
    do_not_patch_main_skill: true
  downstream:
    bpv_registry: update|proposal|no_op
    bpv_14_training_mirror: update|proposal|no_op
    bpv_14r_educational_registry: update|proposal|no_op
    mpp_2ka: update|proposal|no_op
    training_1ka: update|proposal|no_op
    knowledge_8ka: update|proposal|no_op
    storyline_bpm_si: update|proposal|no_op
```

For small requests, do not print the whole YAML. Use it as a checklist and return a compact table.

## Gates

### Duplicate Guard

`МПП` already exists as `BPV-03.7 Материалы поддержки продаж`; `BPV-04.4` owns the adjacent КП/ТКП process. Do not propose a new top-level BPV named MPP and do not move MPP back under BPV-04. Add value as a gate, proof metric, skill heuristic, or support packet.

### Claim Gate

If anything may become client-facing, inherit the claim discipline from `commercial-proposal-generator`: classify claims as client-ready, internal-only, needs source-check, or do-not-use.

### RG Input Gate

When RG-1 or RG-2 sends additional MPP heuristics:

1. Extract reusable MPP / BPV value.
2. Classify as `accepted / discuss / defer / reject`.
3. Do not patch `commercial-proposal-generator` directly.
4. If the heuristic improves this skill, propose the patch to Ilya first unless he explicitly accepts immediate writeback.

### BPV Sequence Gate

Every support pack should state how the MPP changes sales behavior:

```text
artifact -> user -> usage rhythm -> CRM / evidence -> review -> next action
```

If the artifact is useful but has no usage rhythm, call it `MPP asset`, not `BPV-ready MPP`.

When the MPP originates in a Storyline or presentation, an unapproved slide remains a candidate. A BPV-ready route requires the source BPM/SI, slide ID, approved deck artifact/version, approval decision, and a reverse link from BPV-03.7 to that decision.

### RG-1 Source-Ledger Gate

For BPV-MPP outputs that may be reused by sales, include or mentally reconstruct a source ledger:

| Field | Meaning |
|---|---|
| `source_used` | proposal, case, CRM, call note, product file, price list, expert note, benchmark |
| `claim_supported` | what the source actually proves |
| `source_gap` | what the material wants to say but cannot yet prove |
| `reviewer` | who must approve the claim before client use |
| `client_visibility` | client-ready / internal-only / needs source-check / do-not-use |

If the MPP includes prices, commercial terms, product specs, legal / medical / regulatory claims, ROI, timelines, case outcomes, or technology claims, do not mark it client-ready without a reviewer or source.

### Sales-Use Gate

A BPV-MPP packet must answer:

- what sales situation triggers this material;
- which buyer role or decision participant receives it;
- what objection or hesitation it addresses;
- what the manager should do before sending it;
- what CRM field / note / status should record usage;
- what next action the material is supposed to create.

Without this, the output is content, not sales-support BPV.

### Application-Format Gate

When reviewing or improving an existing MPP artifact, do not propose generic technical attributes unless they are required by the artifact's concrete application format.

Technical recommendations such as saving, export, versioning, author attribution, editable fields, dashboards, integrations, analytics, or delivery mechanics are allowed only when the sales-use case requires them: for example, a reusable internal MPP panel, CRM-embedded material, governed template factory, manager workspace, or measured adoption flow.

For a single client-sendable one-pager, КП page, PDF-like HTML sheet, or lightweight sales memo, exclude technical-attribute recommendations that do not change the buyer decision, manager action, review gate, or usage rhythm. This exclusion includes HTML implementation details, missing local asset folders, self-contained packaging, print-size concerns, responsive engineering, file transfer mechanics, and other execution-layer issues unless the user explicitly asks for technical QA or the artifact's approved application format depends on them.

Print preparation, prepress requirements, page-size standards, PDF production constraints, bleed / margin / crop logic, and handoff-to-print issues are not BPV-MPP work. Ignore and exclude them from BPV-MPP review unless the user explicitly requests print-production QA; if such QA is requested, route it to the presentation / print-production owner instead of treating it as MPP sales-support logic.

In this case, keep QA focused on sales situation, buyer role, objection / hesitation, clarity of offer, claim sensitivity, next step, and client-facing readability.

## Good Output Shape

For a BPV-MPP request, return:

| Layer | Decision |
|---|---|
| Parent BPV | `BPV-03.7 Материалы поддержки продаж` |
| Adjacent proposal BPV | `BPV-04.4 Подготовка КП и ТКП` |
| MPP object | concrete asset or bundle |
| Sales use | who uses it and when |
| Proof | what evidence supports it |
| Source gaps | what cannot be claimed yet |
| Reviewer | who must approve sensitive claims |
| CRM / data | what must be recorded |
| Training | what sales / presale must practice |
| Training mirror | `BPV-14.3` and `BPV-14.R`, or explicit no-op |
| Adoption | what shows it works |
| Downstream | BPV / 2-ка / 1-ка / 8-ка / Storyline no-op or update |

## Relationship To Main Proposal Skill

Use `commercial-proposal-generator` for:

- writing the КП;
- Gamma-ready proposal text;
- pricing / scope / claim gates;
- archive КП;
- proposal defense prep.

Use this skill for:

- turning КП logic into MPP;
- turning MPP into BPV implementation;
- mapping sales enablement to CRM / SLA / training / adoption;
- preparing a patch candidate from RG-1 / RG-2 MPP practices.

## Regression Evals

| Case | Prompt | Expected | Forbidden |
|---|---|---|---|
| canonical parent | `Собери МПП для снятия возражений после КП` | primary `BPV-03.7`, adjacent `BPV-04.4` | parent `BPV-04` |
| CRM route | `Нужно фиксировать использование МПП в CRM` | route CRM mechanics to `BPV-05.1` | call BPV-05 a top-level CRM BPV |
| training mirror | `Добавь PST и тренировку менеджеров` | subject trace in BPV-03.7/04, mirror `BPV-14.3` and `BPV-14.R` | route only to 1-ка or old BPV-10 HR |
| approved lineage | `Сильный слайд про objection map — сразу делай BPV` | keep candidate until approved deck/version/decision and reverse link exist | promote an unapproved slide to BPV |
| legacy alias | `Use bpv-04-mpp-commercial-proposal` | accept legacy alias but normalize output to `bpv-03-7-mpp-sales-support` / BPV-03.7 | preserve legacy BPV-04 parent |
