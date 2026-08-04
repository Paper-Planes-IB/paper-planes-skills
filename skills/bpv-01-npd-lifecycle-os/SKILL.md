---
name: bpv-01-npd-lifecycle-os
description: "Use when running BPV-01 Продуктовая фабрика and NPD implementation work: product Tunnel, NPD Lifecycle OS, SEVA / SKU portfolio review, product committee preparation, hypothesis cards, gate evidence, PLM / digital thread checks, RAG evidence memory, post-launch review, or product-governance BPV handoff."
metadata:
  version: "0.1.6"
  status: experimental
  updated: 2026-07-28
  owner: Ilya
  line: BPV-01 Продуктовая фабрика / NPD / product tunnel
  created: 2026-06-11
  supports_bpm:
    primary: [BPV-01, NPD Lifecycle OS]
    required_secondary: [BPM-4, BPM-5, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-2, BPM-3, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9, BPV-05, BPV-10, BPV-11, BPV-12, BPV-14]
  can_consume:
    - NPD / product tunnel project sources
    - product committee packets and decision logs
    - hypothesis cards, SEVA, PLM / RAG / BI evidence
    - BPM Exchange / Matrix BPM-SI donor signals
    - BPV registry and affected BPV files
  can_produce:
    - NPD gate review packet
    - product hypothesis card structure
    - product committee pre-read / decision log fields
    - BPV route / gate / proof-metric proposal
    - BPM Exchange donor / no-op classification
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-07-28: Методика разделения обязана завершаться картой потенциальных ветвлений по каждому кандидату действующего реестра с проверкой полного покрытия; общих критериев и отдельных примеров недостаточно."
      - "2026-07-28: Разделение компонентных гипотез больше не является бинарным; допустимы самостоятельный маршрут, технологический профиль, вариант внутри профиля и недостаточность данных. Вывод NotebookLM требует проверки по физическому источнику."
      - "2026-07-28: Визуализация квадранта должна сохранять полную прослеживаемость кандидатов: каждый маршрут подписывается напрямую или через однозначную нумерованную расшифровку; совпадающие точки разводятся визуально без изменения расчетной координаты."
      - "2026-07-28: Added an evidence-maturity versus commercial-investment-attractiveness quadrant; route readiness remains a separate gate condition."
      - "2026-07-28: Split pre-gate evidence maturity, commercial-investment attractiveness, and route readiness; production and distribution now require separate routes."
      - "2026-07-26: Added BPM Exchange capability metadata and automated pre-gate 0 boundary: machine proposal is not committee decision."
  primary_bpv: BPV-01 Продуктовая фабрика
  adjacent_bpv:
    - BPV-05 Подготовка к автоматизации
    - BPV-10 Аналитическая фабрика
    - BPV-11 ИИ-зация бизнес-процессов и RAG
    - BPV-12 Управление синхронизацией
    - BPV-14 Корпоративное обучение и развитие способностей
---

# BPV-01 NPD Lifecycle OS

## Purpose

Run the BPV side of product strategy and NPD: turn product ideas, technology signals, SKU issues, supplier options, market facts, and PLM / data signals into a managed lifecycle of gates, evidence, owners, decisions, and handoff.

This skill does not write a generic product strategy deck. It helps implement the operating system around product decisions:

```text
signal -> hypothesis card -> evidence -> gate -> decision -> owner -> digital / RAG trace -> next review
```

## Trigger

Use this skill for requests like:

- `собери BPV-01 по NPD`;
- `продуктовый Туннель`;
- `NPD Lifecycle OS`;
- `SEVA`;
- `подготовь продуктовый комитет`;
- `разбери продуктовую гипотезу`;
- `сделай gate / go-no-go по продукту`;
- `свяжи NPD с PLM / RAG / аналитической фабрикой`;
- `что делать с SKU / продуктовой линией / технологией / ингредиентом / поставщиком`;
- `scale / hold / stop / redesign`;
- `product committee pre-read / decision log`.

Do not use it for:

- pure marketing positioning without product governance;
- generic article writing;
- dashboards without NPD / portfolio decision;
- RAG implementation that is not tied to product hypotheses;
- digital profit model pilots where the main decision is order / customer / capacity mix rather than product lifecycle. Use the BPV-12 / DPM derivative there.

## Source Hierarchy

Read live Vault sources when available. Do not rely on memory if the user asks for durable writeback.

Primary sources:

- canonical `BPV-01 Продуктовая фабрика` registry entry and its current affected file;
- `BPV — Внедрение/NPD Lifecycle OS — метод жизненного цикла продуктовой гипотезы.md`;
- project evidence from ВАСТЭКО, Альтернатива, product Tunnel, PLM/R&D, product committee, SEVA, and RAG product tunnel packets.

Adjacent sources:

- canonical `BPV-05 Подготовка к автоматизации` entry for PLM, digital thread, master data, architecture, and readiness;
- canonical `BPV-10 Аналитическая фабрика` entry for post-launch BI and portfolio review;
- canonical `BPV-11 ИИ-зация бизнес-процессов и RAG` entry for RAG memory and evidence pipeline;
- canonical `BPV-12 Управление синхронизацией` entry when NPD affects production mix, gross profit, capacity, pricing, or raw materials;
- canonical `BPV-14 Корпоративное обучение и развитие способностей` entry when the product loop creates a training product.

## Workflow

1. **Preflight.** Identify whether the work is product Tunnel, NPD gate, SEVA portfolio review, product committee prep, PLM/data pass, RAG evidence pass, post-launch review, or BPV handoff.
2. **Signal map.** Name the product signal: customer, market, R&D, supplier, production, free capacity, defect, sales, margin, SKU creep, technology, ingredient, owner push, or strategic option. For FMCG / retail / production cases, explicitly distinguish market pull from production-capacity push.
3. **Automated pre-gate 0.** If the project has an automated signal intake, treat it as a source-ingestion, memory, scoring, and queue layer. Its output is a machine proposal, not a canonical hypothesis or committee decision. Require human source-check, route confirmation, applicability map, two separate economics views, restrictions, and next test before the card becomes ready for G0. Never collapse evidence maturity, commercial-investment attractiveness, and route readiness into one score. Score them separately, choose the target geography, and split import / distribution, contract production, and own production into separate routes. An unknown financial corridor is a readiness gap, not zero commercial value.
   When a portfolio view is useful, plot evidence maturity on the horizontal axis and commercial-investment attractiveness on the vertical axis. Use project-approved thresholds to form four analytical queues. Do not encode route readiness into this quadrant: readiness remains a separate gate condition.
   В квадранте должна сохраняться полная прослеживаемость кандидатов. Каждый маршрут подписывается напрямую или через однозначную нумерованную расшифровку. Если несколько маршрутов имеют одинаковые баллы, их метки разводятся вокруг общего центра с явным указанием, что расчетная координата не меняется.
   Разделение компонентной гипотезы не сводится к ответу «разделить / не разделять». Допустимы четыре результата: самостоятельный маршрут, технологический профиль применения внутри материнской гипотезы, вариант внутри профиля и недостаточность данных. Различие поставщика, страны, марки или сырьевого источника не создает отдельный маршрут без изменения испытания, критерия успешности, покупателя, нормативного контура, экономики или решения. Вывод NotebookLM является аналитическим предложением до проверки по физическому источнику.
   Методика разделения считается примененной только после наложения на действующий реестр кандидатов. Для каждого кандидата должна быть видимая строка с потенциальными ветвями, текущим выводом и следующим доказательством; затем выполняется проверка полного покрытия реестра. Общие критерии и несколько показательных примеров не заменяют такую карту.
4. **Hypothesis card.** Create or update the product hypothesis card with portfolio role, owner, current gate, evidence, economics, digital thread, and next decision.
5. **Platform hypothesis check.** If the signal is broader than one SKU or product, model it as a parent hypothesis with child checks / routes, not as one flat card.
6. **Gate routing.** Choose the current gate and required evidence. A market trend is not enough for a launch decision until it is crossed with accessible channel, regional / segment fit, promo budget, production capacity, and opportunity cost.
7. **External research prompt.** If a gate lacks market, supplier, competitor, regulatory, technology, pricing, or channel evidence, prepare a paste-ready prompt for an external researcher before forcing a decision.
8. **Adjacent BPV check.** Decide whether the signal needs BPV-05, BPV-10, BPV-11, BPV-12, or a BPV-14 training mirror.
9. **Roadmap bridge.** If a roadmap or technology plan is in scope, verify that each commitment has an atomic item, source/evidence lineage, gate decision, owner, portfolio role, dependencies, required teams, capacity status, and review/kill date. Preserve roadmap versions as vintages.
10. **Decision output.** Produce a go / hold / stop / redesign / scale / watch / MTO / exit / strategic-exception recommendation with confidence and source gaps. For commercial launch gates, include the sales argument bank: why the product exists, USP / RTB, target segment, whom not to offer, price / earning logic, supporting script or presentation, and BI proof needed after launch.
11. **Governance handoff.** If the decision needs a product committee, prepare pre-read, agenda, decision log fields, owner, due date, and next review. Return the structured decision, reason, scope, restrictions, assigned checks, and results to the pre-gate memory. If the committee diverges from the machine proposal, record the reason; use it to improve rules, never to rewrite the canon automatically.
12. **Downstream.** Route reusable learning to the BPV registry, Storyline/BPM-SI, 8-ка knowledge, 1-ка training, 2-ка product showcase / MPP / content, and mirror any training product to BPV-14.7/14.8/14.9 plus BPV-14.R, or record an explicit no-op.

## Core Packet

For substantial requests, use this packet internally and show the compact version to the user.

```yaml
bpv_01_npd_packet:
  mode: tunnel|hypothesis_card|gate_review|seva_review|product_committee|plm_pass|rag_evidence|post_launch|handoff|routing_only
  context:
    client_or_project: ""
    product_or_sku: ""
    source_signal: customer|market|r&d|supplier|production|free_capacity|defect|sales|margin|technology|ingredient|owner_push|other
    signal_origin_class: market_pull|customer_pull|production_capacity_push|technology_push|supplier_push|portfolio_cleanup|owner_push|mixed|unknown
    source_pack: []
    missing_sources: []
  approved_lineage:
    source_bpm: []
    si_ids: []
    storyline_slide_ids: []
    approved_deck_artifact: ""
    approved_deck_version: ""
    approval_event_or_decision: ""
    approved_slide_ids: []
    reverse_bpv_link_written: true|false|not_applicable
  hypothesis:
    statement: ""
    portfolio_role: growth|defense|replacement|margin|strategic_option|learning|compliance|other
    current_gate: hypothesis|market|supplier_partner|cto_manufacturability|economy_capex|plm_thread|commercial_pilot|transfer_scale|post_launch|portfolio_review
    owner: ""
    evidence_status: fact|partial|inference|missing
    confidence: high|medium|low
  gate_evidence:
    market: []
    market_capacity_fit:
      accessible_channel: ""
      segment_or_region_fit: ""
      promo_budget_or_activation: ""
      production_capacity: ""
      opportunity_cost: ""
      verdict: pass|partial|fail|unknown
    supplier_partner: []
    manufacturability: []
    economics_capex: []
    digital_thread: []
    commercial_pilot: []
    sales_argument_bank:
      why_exists: ""
      usp_rtb: ""
      target_segment: ""
      do_not_offer_to: ""
      price_or_earning_logic: ""
      script_or_presentation_link: ""
      post_launch_bi_proof: []
    post_launch: []
    source_gaps: []
  external_research_prompt:
    needed: true|false
    trigger_gate: market|supplier_partner|economy_capex|competitor|channel|regulation|technology|pricing|not_applicable
    research_question: ""
    context_to_share: ""
    must_find: []
    forbidden_to_share: []
    expected_return_packet:
      facts: []
      source_links: []
      confidence: high|medium|low|unknown
      contradictions: []
      gaps: []
      implications_for_gate: []
    return_packet_status: not_requested|requested|received|source_checked|rejected
  seva:
    applicable: true|false
    financial_contribution: ""
    market_channel_role: ""
    operational_manageability: ""
    strategic_role: ""
    hidden_load: ""
    confidence: high|medium|low
    recommended_portfolio_decision: grow|fix|hold|watch|harvest|mto|exit|strategic_exception|not_applicable
  adjacent_bpv:
    bpv_05_automation_readiness: none|data_readiness|plm_thread|master_data|architecture|pilot_acceptance
    bpv_10_analytics_factory: none|post_launch_bi|portfolio_review|metric_tree
    bpv_11_ai_rag: none|evidence_memory|corpus_registry|human_review|backlog_operations
    bpv_12_synchronization_dpm: none|product_mix|gross_profit|capacity|pricing|raw_material
    bpv_14_training: none|hypotheses_experiments|data_analytics|digital_ai_knowledge
  product_committee:
    needed: true|false
    pre_read_required: true|false
    decision_log_fields: []
    proposed_decision: continue|narrow|stop|redesign|scale|hold|watch|mto|exit|strategic_exception
    owner: ""
    due_date_or_next_gate: ""
  downstream:
    bpv_registry: update|proposal|no_op
    bpv_14_training_mirror: update|proposal|no_op
    bpv_14r_educational_registry: update|proposal|no_op
    storyline_bpm_si: update|proposal|no_op
    knowledge_8ka: update|proposal|no_op
    training_1ka: update|proposal|no_op
    product_showcase_2ka: update|proposal|no_op
```

## Gate Model

| Gate | Main Question | Minimum Evidence | Decision |
|---|---|---|---|
| Hypothesis | Why does this product matter to the portfolio? | signal source, role, owner, expected upside / risk | accept for discovery / reject / park |
| Market | Is there demand and an accessible channel? | buyer/job, segment, channel, competitor signal, field proof, promo / activation budget | continue / narrow / stop |
| Supplier / partner | Can the technology or supply chain work? | due diligence, samples, terms, risks, alternatives | approve / replace / stop |
| CTO / manufacturability | Can we produce / deliver it without crowding out better work? | technical review, OPI, capacity, quality, TCO, production opportunity cost | go to economics / redesign / stop |
| Economy / CAPEX | Does the economics hold? | unit economics, target cost, margin, tooling, CAPEX, payback | invest / hold / redesign |
| PLM / thread | Is there a digital trace? | product project, SKU, BOM, revision, tooling, change, launch status | ready / fix data |
| Commercial / pilot | Is repeatability visible and can sales explain the product? | pilot, first commercialization, feedback, quality, sales proof, sales argument bank | scale / limit / redesign |
| Transfer / scale | Who owns the routine? | owner, process, training, data, cadence | transfer / extend pilot |
| Post-launch | What does the market fact require? | sales, margin, defects, payback, feedback | scale / hold / stop / redesign |

## Platform Hypothesis Mode

Use this when the input is broader than a single SKU, supplier, technology, or product format: ingredient platform, technology family, B2B+B2C option space, component bet, or broad RAG-generated signal.

Model:

```text
parent hypothesis -> child checks / routes -> evidence pack -> return to parent -> next gate / investment committee
```

Stage boundary:

- `G0 / zero card` creates the hypothesis, documents entry rationale, decomposes it, selects promising routes, records data gaps, and decides which checks to launch next.
- `G1 / first-stage stitching` gathers evidence across the selected routes: demand, technology feasibility, suppliers / components, primary economics, regulation, and then consolidates the results for the next gate or investment committee.
- Do not demand G1 evidence from a G0 card; do not let G1 remain a loose set of parallel checks without returning evidence to the parent hypothesis.
- Distinguish the methodological stage-gate tunnel from technical downstream business processes. A Bitrix24 process for raw-material / distribution chain creation can be a downstream process after G1, while product processing, B2B/B2C product development, e-commerce, or own-SKU routes may require separate process specs.

Minimum child-check fields:

- `parent_hypothesis_id`
- `child_check_type`: market / B2B value / technology / supplier / regulation / economics / benchmark
- `check_question`
- `required_output`
- `evidence_pack_link`
- `consolidation_status`

Do not describe each child check as a separate methodology tunnel. If a stakeholder says "several tunnels", translate it as "several cards / routes / child checks inside one stage-gate process" unless the client has explicitly defined separate processes.

### Application Map and Route-Splitting Rule

For ingredient, component, technology, or supplier-led inputs, do not evaluate
the component "in general" and do not create one product route per supplier.
Use:

```text
parent component hypothesis
-> application route =
   application
   x buyer / segment
   x functional job
   x critical process conditions
   x expected result
   x supply scenario
-> variants =
   brand / grade / origin / supplier
```

Before creating a separate route, test whether variants:

1. solve the same functional job;
2. work under comparable process conditions;
3. produce comparable sensory, stability, yield, or shelf-life results;
4. require the same technical / customer test;
5. use the same success criterion;
6. have comparable company-side and customer-side economics;
7. can receive the same gate decision.

Create a separate route only if a difference changes the required test,
success criterion, economics, or possible gate decision. Otherwise keep it as
a variant inside the route. A different supplier alone creates a supplier
opportunity linked to the SKU / route, not a new product hypothesis.

Split B2B and B2C only when buyer job, process, demand evidence, regulation,
economics, or possible decision differs. Channel naming alone is not enough.

### Dual Economics

For every relevant route keep two independent economic views:

- company economics: landed cost, storage, working capital, processing /
  repacking, commercial cost, price, and margin;
- customer / product economics: dosage, yield, auxiliary inputs, operations,
  waste / downtime, storage, switching cost, avoided cost, and net effect.

One positive view does not compensate for a missing or negative second view.
At G0 a transparent range with assumptions is sufficient; later gates require
stronger evidence.

### Standard G1 Check Packages

After G0 assign only the packages needed to close the route's actual gaps:

- B2C demand;
- B2B value;
- component / supplier;
- technology applicability;
- regulation / labeling;
- company economics;
- customer / product economics;
- variant comparison;
- commercial trial.

Every package needs a check question, owner, due date, required output,
acceptance criterion, result link, and return status to the parent route.

`Component platform x industry vertical` may be retained as a methodology
hypothesis for portfolio analysis, but must not become a mandatory classifier,
route-creation rule, or gate priority unless the specific operating model has
adopted and validated it.

## SEVA Mode

Use SEVA when the question is portfolio / SKU / product-line review rather than one new hypothesis.

Minimum factors:

- financial contribution: margin, contribution, cash, frozen capital, ad load;
- market / channel role: category entry, retention, channel, frequency, complementarity;
- operational manageability: supplier, MOQ, lead time, stock, logistics, support, returns;
- strategic role: defense, flagship, trust, technology, client access, market education;
- hidden load: manual work, SKU creep, data complexity, exceptions, dead stock;
- confidence: source, freshness, completeness, disputed assumptions, next test.

If a product is a `strategic_exception`, name the reason, owner, review horizon, success metric, and cost of exception.

## External Research Prompt Mode

Use this mode when an NPD gate cannot be responsibly decided from internal sources and the missing evidence can be gathered externally.

Trigger this mode for gaps in:

- market proof: buyer, job, segment, use case, willingness to pay, channel;
- competitor / substitute proof: alternatives, category norms, differentiation, price corridor;
- supplier / partner proof: supplier options, technology maturity, terms, risks, analogs;
- regulation / certification: required approvals, safety standards, labeling, restrictions;
- technology / ingredient proof: feasibility, claims, performance, risks, IP / patent red flags;
- economics benchmarks: pricing, margin proxy, CAPEX analogs, tooling, payback ranges.

Produce a paste-ready prompt with this structure:

```text
Context:
We are evaluating an NPD / product portfolio hypothesis. The current gate is <gate>. The product / SKU / technology is <object>. Internal evidence is insufficient in these areas: <source gaps>.

Research task:
Find external evidence that helps decide whether the hypothesis should continue, narrow, stop, redesign, or wait.

Must find:
- buyer / job / segment evidence;
- market and channel evidence;
- competitor or substitute evidence;
- supplier / technology / regulatory evidence, if relevant;
- pricing, margin, CAPEX, or payback benchmarks, if available;
- contradictions and reasons the hypothesis may fail.

Return format:
1. Facts with source links.
2. Confidence level for each fact.
3. Contradictions or weak evidence.
4. Remaining gaps.
5. Implications for the NPD gate decision.

Do not:
- invent client-internal facts;
- treat marketing claims as proof without source qualification;
- write a recommendation without naming evidence strength.
```

External return packets are advisory only. Classify them as `fact`, `partial`, `inference`, or `missing`, then run human review / product governance before any gate decision or Vault canon writeback.

## Product Committee Mode

Use product committee mode when a gate decision needs authority, trade-off, or cross-functional owner.

Prepare:

- pre-read: hypothesis card, evidence pack, source gaps, confidence, recommendation;
- agenda: NPD gate decisions and portfolio / SKU sanitation separated;
- decision log: decision, reason, owner, deadline, next gate, data / RAG writeback;
- negative decisions: kill, recycle, hold, redesign are valid decisions, not failure;
- for `G0 / zero-card` committee regulations, make G0 canonical and mark later gates / stages as assumptions unless they were separately approved by Ilya and the client team;
- for rehearsal / implementation committees, always separate two outputs: product decision by hypothesis / route, and system delta to data model, Bitrix / CRM, RAG memory, templates, protocol, roles, or gate rules;
- post-launch review: every launch needs 30/60/90 or project-calibrated review.

Do not let the committee become a discussion club. If there is no decision log, BPV is not implemented.

## RAG Evidence Memory Mode

Use when the product hypothesis depends on documents, supplier proof, specs, protocols, market facts, claims, red flags, or prior decisions.

Minimum chain:

```text
source -> knowledge atom -> hypothesis -> route -> gate -> decision -> next check
```

Required entities:

- source / artifact;
- knowledge atom;
- hypothesis card;
- product / SKU / component / ingredient;
- supplier / partner;
- market cell;
- red flag;
- source gap;
- gate decision.

RAG may propose a hypothesis, but cannot approve it. Human review and product governance decide.

## Early-Signal And Roadmap Bridge Mode

Use when a roadmap, technology plan, equipment family, or historical roadmap version is in scope.

Minimum chain:

```text
source signal -> signal atom -> cluster / watchlist -> human review
-> G0 parent hypothesis -> child checks -> evidence pack -> gate
-> atomic roadmap item -> capacity/dependency check -> outcome feedback
```

Minimum roadmap item fields:

- `roadmap_item_id`;
- `parent_hypothesis_id`;
- `equipment_class / product family`;
- `portfolio_role / current_gate`;
- `source_signal_ids / evidence_pack / decision_id`;
- `owner / start / end / planning_granularity`;
- `dependency_ids / required_teams / capacity_status`;
- `status / review_date / kill_condition`.

Do not infer machine status from rich-text color or one multi-item cell. Atomize initiatives first.

When multiple roadmap versions exist, preserve them as vintages and classify changes as `added / removed / moved / split / merged / accelerated / delayed / scope_changed`.

For retrospective sensing tests, prevent hindsight leakage: choose a cutoff, exclude later sources, hide the future roadmap vintage, generate a blind watchlist, then score recall, precision, false positives, lead time, confidence calibration, and carryover detection. AI may recommend `watch / load evidence / merge / reject`; a human owner decides entry to G0 and the roadmap.

## Route Template / Capacity Mode

Use when a source combines project types, stage checklists, plan/fact, staffing, or resource sufficiency.

Always separate:

- `stage-gate lifecycle`: decision rights and evidence for continued investment;
- `route_template`: applicable standard work packages after a gate;
- `route/project_instance`: current execution state of one project;
- `PLM/digital_thread`: linked versions of requirements, decisions, prototypes, tests, releases, and SKU;
- `capacity_overlay`: skill/team availability by period.

Do not encode these in one project type/status field. Standard effort is a prior until calibrated against completed project facts. Competing checklist tabs require `process_version`, `effective_from`, owner, diff, and migration rule. A resource model with a missing hiring/growth sheet or broken upstream reference is `data_lineage_gap`; do not use its outputs to authorize staffing or roadmap commitments.

## Portfolio Prioritization Mode

Use when the source contains scoring formulas, priority categories, queue ranks, roadmap selection, overrides, or reserved capacity.

Separate these fields and entities:

- `portfolio_score`: relative attractiveness within a comparable reference class;
- `portfolio_role`: growth / margin / defense / platform / replacement / compliance / learning option;
- `priority_category`: operational class of work;
- `urgency_commitment`: deadline, obligation, severity, cost of delay;
- `lifecycle_state`: active / paused / hold / killed / completed;
- `rank_order`: queue position with validity date;
- `capacity_reservation`: team/skill/time allocation;
- `priority_override`: decision event with reason, approver, expiry, and displaced work.

Do not let one numeric code represent all of them. Use contribution-per-effort only inside a comparable reference class and only with source-backed demand, substitution/cannibalization, effort range, evidence confidence, capacity/dependency feasibility, and post-launch recalibration. Treat unanchored multiplicative expert coefficients as `weak_prior`. Reserved capacity requires quota, opportunity cost, WIP limit, period, owner, and exit/review gate.

## Competitive / Pricing Evidence Mode

Use when a source contains competitor models, feature comparison, market prices, target cost, channel prices, pricing rules, or a price committee input.

Apply two distinct gates:

1. competitive/value evidence before BT/OKR or equivalent product scope approval;
2. pricing/channel evidence before commercial launch.

Never collapse `market observation`, `analytical interpretation`, `recommendation`, `approved decision`, and `post-launch fact`. A price observation needs source, captured date, geography, channel, currency/VAT, availability, volume/MOQ, configuration and evidence quality. A comparable-set model needs functional equivalence, segment fit and normalization notes. A price decision needs owner, threshold, rationale, validity period, exception handling and review date.

Use target-costing in both directions:

```text
actual cost -> achievable channel/customer price
market/value price range -> target cost before prototype
prototype actual cost -> repeated price/cost gate
```

Treat binary feature sums, unanchored competitor weights, fixed markups/discounts and `competitor price = automatic ceiling` as `weak_prior` until sensitivity and backtest against realised price, margin, volume, win/loss and elasticity proxy. Route recurring monitoring to BPV-10, cost-driver improvement to BPV-07, competitive research to BPM-6, market context to BPM-7B, and the final product/commercial decision to BPV-01/price governance.

## PLM / Digital Thread Mode

Use when engineering, manufacturing, BOM, revision, tooling, CAPEX, defects, or lifecycle status are relevant.

Check:

- product master and owner;
- engineering definition: CAD/PDM/EBOM/specification/version;
- manufacturing definition: MBOM/BOP/routing/launch data;
- change management: ECR/ECO/ECN or equivalent;
- economics: target cost, actual cost, margin, CAPEX, tooling, payback;
- closed loop: sales / margin / quality returns to portfolio or product committee.

If there is only a forward system flow and no feedback loop, the digital thread is incomplete.

## Output Shapes

For quick diagnosis, return a table:

| Field | Decision |
|---|---|
| Current gate | |
| Portfolio role | |
| Evidence status | |
| Owner | |
| Source gaps | |
| Adjacent BPV needed | |
| Recommended decision | |
| Next gate | |

For committee prep, return:

| Agenda item | Decision needed | Evidence | Source gap | Owner | Deadline |
|---|---|---|---|---|---|

For external research prompt prep, return:

| Field | Content |
|---|---|
| Trigger gate | |
| Source gap | |
| Research question | |
| Context to share | |
| Must find | |
| Forbidden to share | |
| Expected return packet | |

For SEVA, return:

| Product / SKU | Financial | Market role | Ops load | Strategic role | Hidden load | Confidence | Decision |
|---|---|---|---|---|---|---|---|

## Boundaries

- Do not create a new top-level BPV from a product subpattern without explicit decision.
- Do not treat SEVA, product committee, RAG memory, or PLM pass as separate skills by default. They are modes inside this skill.
- Do not call a product hypothesis BPV-ready without owner, evidence, gate, decision, and next review.
- Do not promise launch / scale / financial uplift without baseline and source.
- Do not move to IT implementation before the decision object, owner, data, and feedback loop are clear.
- Do not turn external research or AI-generated notes into canon without source-check and human review.

## Eval Cases

Use these as regression cases when the skill is updated:

| Case | Prompt | Expected | Forbidden |
|---|---|---|---|
| good-trigger | `Разбери продуктовую гипотезу ВАСТЭКО через продуктовый Туннель и SEVA` | activate this skill, produce hypothesis + gate + SEVA packet | generic product strategy essay |
| adjacent-BPV | `Нужно внедрить PLM для новинок` | activate this skill with BPV-05 automation-readiness / PLM pass | route PLM to BPV-11 or treat it as pure AI implementation |
| bad-trigger | `Напиши пост про инновации в продуктах` | use content/article skill, not this one | run full NPD packet |
| RAG-boundary | `RAG сам предложил 12 продуктовых гипотез, занеси в план` | require human review and gate classification | auto-approve hypotheses |
| external-research-gap | `По гипотезе не хватает market proof и supplier proof, подготовь следующий шаг` | produce paste-ready external researcher prompt and expected return packet | make gate decision as if evidence exists |
| DPM-boundary | `Оптимизируй mix заказов по валовой прибыли и сырью` | route to BPV-12 / DPM unless product lifecycle is central | route to BPV-14 or force NPD Lifecycle OS |
| training-mirror | `Собери обучение работе с продуктовыми гипотезами` | keep subject lineage in BPV-01 and mirror the educational product to BPV-14.7 / BPV-14.R | route only to 1-ка without BPV-14 trace |
| approved-lineage | `Слайд с новой продуктовой гипотезой готов — создавай BPV` | keep a candidate until deck/version and approval decision are known; then write the reverse BPV-01 link | treat an unapproved slide as an accepted BPV decision |
| pricing-evidence | `Конкуренты снизили цену; обнови продуктовый gate и предложи новую РРЦ` | separate observation/comparability/scenario/decision, require target-cost and post-launch evidence | copy competitor price or approve price automatically |
| writeback-risk | `Закрепи это как новый BPV` | propose classification and approval gate | create top-level BPV automatically |
