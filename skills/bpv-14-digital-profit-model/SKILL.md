---
name: bpv-12-digital-profit-model
description: "Use when running the Digital Profit Model derivative of BPV-12 Управление синхронизацией: priority and sequencing systems for multi-project, multi-team, multi-order or high-SKU environments; DNA pitch, TCO/business-value alignment, capacity allocation, APS/solver/AI triage, override learning, pilots, and handoff to BPV-05 data/automation readiness."
metadata:
  status: experimental
  owner: Ilya
  line: BPV-12 / Управление синхронизацией / Digital Profit Model derivative
  created: 2026-06-11
  primary_bpv: BPV-12 Управление синхронизацией
  covered_sub_bpv:
    - BPV-12.1 Приоритизация объектов исполнения
    - BPV-12.2 Оптимизация pitch / sequence
    - BPV-12.3 Планирование мощности и распределение исполнения
    - BPV-12.4 Override и обучение модели
  registry_status: canonical BPV derivative
  legacy_directory_alias: bpv-14-digital-profit-model
  legacy_skill_aliases:
    - bpv-14-digital-profit-model
  adjacent_bpv:
    - BPV-02 Финансовый менеджмент
    - BPV-04 Управление продажами
    - BPV-05 Подготовка к автоматизации
    - BPV-07 Операционная эффективность
    - BPV-08 Система управления
    - BPV-10 Аналитическая фабрика
    - BPV-11 ИИ-зация бизнес-процессов и RAG
    - BPV-14 Корпоративное обучение и развитие способностей
---

# BPV-12 Digital Profit Model

## Purpose

Use this skill to run the BPV side of Digital Profit Model work: convert a request like "we need to align priorities, choose the optimal execution order / DNA pitch, allocate teams or capacity, or use APS / AI / solver" into a working decision system:

```text
data -> recommendation -> decision -> acceptance / override -> execution -> fact -> rule review
```

Digital Profit Model is an experimental operating derivative inside canonical `BPV-12 Управление синхронизацией`; it spans BPV-12.1–12.4 and is not a separate upper BPV.

## Trigger

Use this skill when the user or source material mentions any of:

- Digital Profit Model, Gross Profit model, управляемая валовая прибыль;
- multi-project, multi-team, multi-order or high-SKU environments, backlog prioritization and execution sequencing;
- DNA pitch, optimal work order, TCO / business-value comparison and capacity allocation;
- APS, solver, AI, digital twin, optimization, recommendation engine, if the real question is decision-making;
- raw material constraints, supplier constraints, capacity constraints, setup matrix, due-date trade-offs;
- Customer Strategic Score, Pricing Potential, pricing floor, override policy;
- "что производить, для кого, когда, из какого сырья, по какой цене".

Do not use it as the primary skill for:

- product hypothesis lifecycle, product tunnel, SEVA, or DPM as a product concept: use `bpv-01-npd-lifecycle-os` unless Gross Profit decision operations are central;
- pure dashboard / semantic layer / BI work: use `BPV-10 Аналитическая фабрика` or a dashboard skill unless decision rules, owner, override, and pilot are in scope;
- pure IT architecture, data readiness, or vendor selection: use `BPV-05 Подготовка к автоматизации` after this skill defines why APS / solver / AI is needed;
- generic finance analysis without a recurring decision loop: route to `BPV-02 Финансовый менеджмент` / BPM4 finance domain.

## Source Order

Before writing or routing BPV-12 / DPM work, prefer live Vault context over memory:

1. canonical BPV registry entry `BPV-12 Управление синхронизацией` and its current affected file;
2. `Digital Profit Model — модель управляемой валовой прибыли`;
3. `Knowledge unit — Digital Profit Model high-SKU manufacturing`;
4. relevant client sources such as Kronus reengage / discovery notes;
5. adjacent BPV files: BPV-02, BPV-04, BPV-05, BPV-07, BPV-08, BPV-10, BPV-11, BPV-14.

If sources are unavailable, say which layer was not checked and keep conclusions provisional.

## Workflow

### 1. Preflight

Classify the request:

```yaml
bpv_12_dpm_mode: triage|framing|constraint_map|data_readiness|decision_model|pilot|prototype|tech_handoff|handoff|routing
client_context: ""
decision_system_present: true|false|unclear
requested_artifact: ""
adjacent_bpv_risk: []
registry_effect: no_registry_change|candidate_derivative|candidate_sub_bpv
```

If the user asks to "закрепить" DPM as a separate upper BPV, keep it under canonical BPV-12 and return its current derivative status unless Ilya explicitly changes the registry.

### 2. Triage The Request

Separate four different jobs:

| Request form | What to do |
|---|---|
| "Need BI / dashboard" | Ask what recurring decision changes. If none, route to BPV-10. |
| "Need APS / AI / solver" | Define decision object, owner, baseline, constraints, and pilot before any vendor / tech claim. |
| "Need Gross Profit model" | Build economic and decision model, not just margin reporting. |
| "Sales / production / procurement argue" | Map the decision conflict and convert it into rules, override policy, and rhythm. |

Minimum triage gate:

- decision to change;
- owner of the decision;
- metric and loss baseline;
- repeatability of the problem;
- constraints that bind the decision.

### 3. Frame The Decision System

Describe the decision in concrete operational language:

```text
what objects compete for execution
-> which should be executed first
-> in which sequence / DNA pitch
-> by which team or capacity
-> with which dependencies and deadlines
-> at what total cost and business value
-> what to move, stop, accept, expedite, or rebuild
```

If this chain cannot be filled, stay in framing.

### 4. Build The Constraint Map

Include at least:

- production capacity, work centers, routings, operation sequence;
- setup / changeover matrix by SKU group or family;
- raw material availability, price curves, MOQ, alternatives;
- supplier lead time, single-source risk, substitution rules;
- firm backlog, promised due dates, OTIF, claims;
- customer priority and Customer Strategic Score;
- pricing floor, discount authority, premium triggers;
- cost-to-serve, working capital, cash proxy.

Do not hide TCO, business value, dependencies, capacity, deadlines or switching losses inside a generic penalty score. Pricing, suppliers and raw material are case-specific constraints, not universal sub-processes of BPV-12.

### 5. Run Data-Readiness

Separate three levels:

| Level | Meaning |
|---|---|
| Must-have for pilot | SKU group, BOM, routings, capacity calendar, setup matrix, backlog, due dates, variable margin, raw material availability, cost-to-serve drivers, payment terms / inventory impact. |
| Must-define before pilot | Customer Strategic Score rubric, pricing rules, override policy, score weights, critical raw material / single-source list. |
| Start collecting day 1 | sales override log, actual operation times, yield / scrap, OTIF / claims, forecast confidence, price realization. |

If must-have data is absent, write a proxy plan and state which promises are not allowed yet.

### 6. Design The Decision Model

Use this canvas:

```yaml
decision_model_canvas:
  decision: ""
  metric: ""
  economics:
    revenue: ""
    variable_cost: ""
    contribution: ""
    setup_cost: ""
    raw_material_opportunity_cost: ""
    cost_to_serve: ""
    working_capital_cash_proxy: ""
  owner: ""
  constraints: []
  data_fields: []
  rule: ""
  override_policy: ""
  pilot_scope: ""
  evidence_standard: ""
  tech_implication: ""
```

Keep Customer Strategic Score stable enough for governance. Sales can supply evidence and exceptions, but should not freely rewrite strategic score for each deal.

### 7. Pilot And Prototype

Limit the pilot to a tractable scope: one product family, one production route, one customer segment, top-N orders, or a constrained backlog slice.

Before pilot, require:

- problem statement and non-goals;
- decision map;
- constraint map;
- data-readiness heatmap;
- full economic model or explicit proxies;
- baseline and success metric;
- override log design;
- operating rhythm where recommendations will be reviewed.

Acceptable pilot tools include spreadsheet, BI prototype, notebook, Python model, low-code tool, or manual scoring table. Do not treat tool choice as the main result.

### 8. Technical Handoff

Only after the pilot shows applicability, prepare requirements for APS, solver, AI, integrator, data model, or architecture.

The handoff must include:

- decisions the system should recommend;
- master data and source systems;
- integration points;
- RFP / POC criteria;
- evidence from pilot;
- owner of daily / weekly operation;
- audit trail and override requirements.

### 9. Institutionalize

BPV-12 / DPM is successful when the client has an operating contour:

- owner;
- decision meeting / IBP / S&OP rhythm;
- accepted rule set;
- override governance;
- training and role clarity, mirrored to the applicable `BPV-14.4/14.6/14.8/14.9` route and `BPV-14.R`, or an explicit no-op;
- fact review and rule revision;
- reduced dependence on Paper Planes daily holding.

## Approved Decision Lineage

When DPM is derived from a project Storyline or defended presentation, do not jump from a slide hypothesis directly to BPV. Preserve the full trace and write the reverse link from BPV-12 back to the approved decision:

```yaml
approved_decision_lineage:
  source_project: ""
  source_bpm: []
  si_ids: []
  storyline_slide_ids: []
  deck_artifact: ""
  deck_version: ""
  approval_event_or_decision: ""
  approved_slide_ids: []
  approved_decisions: []
  bpv_route:
    primary: "BPV-12 Управление синхронизацией"
    covered_sub_bpv: []
    adjacent_bpv: []
  reverse_bpv_link_written: true|false
  unresolved_trace_gaps: []
```

An unapproved slide remains a `BPV candidate`; it cannot be reported as an implemented or accepted BPV route.

## Output Contracts

Choose the smallest output that fits the request.

| Output | Use when |
|---|---|
| DPM intake note | Early request, unclear whether this is BI, IT, APS, AI, or BPV. |
| Problem statement | The problem and non-goals need executive agreement. |
| Constraint map | The client has operational trade-offs but they are not explicit. |
| Data-readiness heatmap | The pilot might be blocked by missing data or master-data quality. |
| Decision model canvas | The recurring decision, economics, rules, and override need design. |
| Pilot brief | A limited scope must be launched and measured. |
| Technical requirements | A pilot has shown the need for APS / solver / AI / data / integration. |
| BPV routing note | DPM is a BPV-12 derivative and may need propagation across BPV-02/04/05/07/08/10/11/14. |

## Routing To Adjacent BPV

Always identify downstream routes:

- BPV-02 Финансовый менеджмент: Gross Profit, costing, margin basis, pricing floor;
- BPV-04 Управление продажами: sales backlog, customer priority, order acceptance, commercial implications;
- BPV-05 Подготовка к автоматизации: master data, source systems, architecture, IT readiness, pilot acceptance;
- BPV-07 Операционная эффективность: capacity, setup, waste, operation time, cost drivers;
- BPV-08 Система управления: IBP / S&OP rhythm, KPI, decision meetings;
- BPV-10 Аналитическая фабрика: dashboards, semantic layer, regular analytics review;
- BPV-11 ИИ-зация бизнес-процессов и RAG: AI/RAG execution only when the DPM route actually uses it;
- BPV-14 Корпоративное обучение и развитие способностей: role training mirror and educational-product registry.

When DPM is only a sub-effect of the BPV-01 product tunnel, say so explicitly and route product-lifecycle work to BPV-01 while keeping the Gross Profit synchronization decision system in BPV-12.

## Anti-Patterns

Avoid:

- starting with APS / AI / BI vendor before decision model;
- treating gross margin as enough for product mix;
- letting sales rewrite strategic score for a single deal;
- compressing all constraints into one opaque penalty score;
- making a dashboard without a decision owner;
- piloting too broadly;
- promising margin uplift without baseline and pilot evidence;
- claiming implementation is done after prototype handoff.

## Eval Cases

Use these cases when editing or validating the skill.

| Case | Prompt | Expected routing |
|---|---|---|
| good trigger | "Клиент хочет APS / AI для high-SKU производства, чтобы управлять Gross Profit и выбирать, какие заказы брать." | Activate BPV-12 / DPM, start triage and decision-system framing. |
| dashboard confusion | "Сделай дашборд валовой прибыли по SKU." | Route to BPV-10 unless recurring decision rules / owner / override / pilot are requested. |
| BPV-01 adjacency | "Разбери новую продуктовую гипотезу и туннель вывода продукта." | Use BPV-01; mention BPV-12 only if product mix / Gross Profit synchronization is central. |
| vendor-first risk | "Нужно выбрать APS-вендора." | Run BPV-12 / DPM triage first; route architecture and readiness to BPV-05. |
| legacy-code regression | "Проведи BPV-14 Digital Profit Model." | Normalize the legacy alias to BPV-12 / DPM; never treat DPM as corporate training and never overwrite canonical BPV-14. |
| registry guard | "Закрепи DPM как отдельный верхний BPV." | Keep it as a BPV-12 derivative unless Ilya explicitly changes the canonical registry. |
| approved-lineage guard | "Слайд про оптимальную очередь выглядит сильным — создавай BPV." | Keep as candidate until deck/version and approval decision are known; then write the reverse BPV-12 link. |
| evidence guard | "AI даст плюс 7 процентов маржи, напиши это клиенту." | Refuse as claim without baseline and pilot evidence; replace with testable hypothesis. |
