---
name: bpm4-b2b-dashboard-industrial-distribution
description: "Use when working with BPM-4 commercial-network dashboards across separate subtypes: B2B/industrial distribution, HoReCa/Retail point networks, or distribution-like SKU dashboards. Covers Formula Profit, point/store economics, cheque analytics, loyalty-client cohorts, client/dealer segmentation, shipment cohorts, SKU affinity, OoS, cross-filtered BI/DataLens/HTML views, SI/SIF extraction, and Storyline-Storyboard routing."
metadata:
  version: "0.3.53"
  status: active
  line: BPM-4 / commercial network dashboard
  owner: Ilya
  supports_bpm:
    primary: [BPM-4]
    required_secondary: [BPM-10, BPM-11]
    optional_secondary: [BPM-2, BPM-3, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9]
  can_consume: [sales / shipment / order-line datasets, retail cheque datasets, loyalty-program datasets, point/store registry, cashier / seller slices, Formula Profit inputs, CRM / ERP / BI exports, project BPM Storyline-Storyboard, Матрица BPM — SI, flat B2B transaction base, hierarchical 1C Excel exports, client-region dictionaries, manager dictionaries, regional deep-dive slices, packaged external methodology/specs]
  can_produce: [BPM-4 dashboard view spec, DataLens-ready implementation handoff, standalone HTML dashboard, Formula Profit decomposition, point/store performance tree, loyalty-client RFM / cohort / cluster views, segment / SKU / cohort hypotheses, SI / SIF candidates, Storyline-Storyboard writeback proposal, base-analysis packet, annotatable report with compact chart screenshots, client / category / SKU / manager / point breaks, region-segment matrices, account-based segmentation families, growth candidates, executive summary structure, no-op reason]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-09-03: Added retail point-opening plan rule: when a target revenue plan requires new locations, split growth into current-network run-rate, existing-point optimization ceiling, and new-point residual; calculate format portfolio with stated minimum mix such as 80/20 in favor of tonars, but allocate formats by city/territory archetype instead of applying the mix uniformly to every city."
      - "2026-09-03: Reframed MG atlas chart families as an improvement / extension idea bank, not a required dashboard template. The skill should remember which graph ideas can strengthen a HoReCa/Retail BPM-4 analysis and propose/apply them when they sharpen a decision, expose a hidden mechanism, close a caveat, or enrich BPM-SI."
      - "2026-09-03: Added analytical atlas package rule: if an HTML atlas arrives with chart map CSV, chart-ready data folder, artifact manifest, QA.json and preview, treat it as a reusable BPM-4 dashboard package. Inspect chart count, sections, map schema, data files, QA/render status and limitations; use chart-ready CSV for immediate posthoc checks; distinguish chart-level reproducibility from raw-to-chart pipeline reproducibility; QA render is not metric proof."
      - "2026-09-01: Added dashboard construction log rule: graph-building logs are lineage / metric-contract evidence. Extract chart -> JSON view -> physical source -> formula -> filter semantics -> derived QA/payload dependencies -> network/point isolation -> visual-only encodings; update source coverage and named recovery gaps before treating an HTML dashboard as reproducible."
      - "2026-09-01: Added POS/address candidate dictionary rule: point/POS candidate tables close package-recovery gaps but do not become approved point masters; inspect source split, raw aliases, POS IDs, address parsability, date ranges, amount coverage, duplicates and cross-system mapping before point/address conclusions."
      - "2026-09-01: Added candidate-dictionary guardrail: `dim_*_candidates` tables are mapping/normalization evidence, not approved master data; inspect source split, duplicate keys, category conflicts, nulls, metric coverage, and approval status before using them for SKU/point conclusions."
      - "2026-09-01: Added package-manifest lineage rule: manifest files are source-class evidence for package completeness, expected tables, QA artifacts, processed/QA directories, and recovery gaps; they do not by themselves prove metric values unless the referenced physical tables/QA files are present."
      - "2026-09-01: Added change-delta heuristic audit rule: after updates, additions, expansions, cancellations, replacements, or status changes, evaluate every delta against the active heuristic set and record whether it strengthens, weakens, narrows, supersedes, or leaves unchanged the report's conclusions and data gaps."
      - "2026-09-01: Added post-ingest caveat retirement rule: every new raw/mart/source layer must trigger a posthoc pass over the original dashboard conclusions, replacing stale data gaps with `закрыто / сужено / остается открытым / заменено более точным gap`, and the skill itself must be updated when the iteration creates a reusable rule."
      - "2026-09-01: Added annotation sweep closure rule: after a dense set of dashboard annotations, produce a visible closure ledger showing which new heuristics were absorbed into in-place conclusions, issue tree, hypothesis/data-gap registers, roadmap/data requests, and skill rules; unresolved items must be named as gaps, not left implicit."
      - "2026-09-01: Added dashboard issue-tree rule: bottom analytical registers must include a fact/hypothesis/data-gap issue tree up to four levels when dashboard conclusions drive roadmap decisions; hypothesis tables alone are insufficient."
      - "2026-09-01: Strengthened peer-set registry rule: peer sets must be built in the document for every action-bearing slice, not only points; formats, cities, SKU/categories, RFM/clusters, sellers and cohorts need explicit comparison groups when used for management action."
      - "2026-09-01: Added loyalty-join-date cohort guardrail: cohort validity requires requesting loyalty-program join date alongside true first purchase/registration date; visible cohorts must separate loyalty join, first visible purchase, and true first purchase."
      - "2026-09-01: Added segment kinship / transition matrix rule: RFM, cluster, format-route and similar segment migration upside must estimate plausible conversion through behavioral adjacency before calculating movement to better segments."
      - "2026-09-01: Added divergence regression/factor matrix rule: when success grows while quality/capture/coverage/manageability worsens, the report must build an outcome-factor-control-verdict-missing-bridge matrix and run correlations/regression/feature-importance when raw grain is available."
      - "2026-09-01: Strengthened bidirectional BPM enrichment rule: cross-BPM gates must first reuse completed BPM evidence and, when another BPM is ongoing or pending, enrich that BPM's program with exact questions, fields, checks, or hypotheses instead of leaving a generic `verify via BPM` note."
      - "2026-09-01: Добавлен mandatory profit-layer data-gap rule: every profit/payback/unit-economics dependent finding must create or update an explicit data-gap row when margin/COGS/write-offs/fixed costs/bonus/contact cost are absent; initiatives remain revenue/proxy until the gap is closed."
      - "2026-09-01: Добавлен full replay consistency rule: после новых эвристик вроде BPM reuse-first или open-data proxy агент обязан перепройти весь отчет, обновить in-place выводы, нижние hypothesis/data-gap registers и coverage ledger, а не только дописать локальный фрагмент."
      - "2026-09-01: Добавлен BPM reuse-before-request rule: cross-BPM gates сначала используют уже собранные BPM-данные и возвращают enrichment обратно; новые evidence requests создаются только на конкретные gaps зерна, смысла или прав доказательности."
      - "2026-09-01: Добавлен geo/retail enrichment rule для high-ticket low-flow точек: если есть адреса, bottleneck card должна проверять адресный потенциал через открытые данные как отдельный proxy-слой, не подменяя им BPM-4, BPM-3 и маржинальные доказательства."
      - "2026-09-01: Added best-practice formula extraction rule: when the report says to capture a transferable formula from a city/point/format, immediately build a factor-analysis packet with proved factors, hypothesized mechanisms, transferability, non-transferable context, first test peers, and KPIs."
      - "2026-09-01: Added syndicated-idea proof rule: cross-chart ideas such as format machines, route roles, or segment mechanisms must be backed by syndicated figures from all relevant charts/cuts when the dashboard contains them."
      - "2026-09-01: Added cluster-to-scenario embodiment rule: when consumer clusters exist, immediately produce cluster -> product scenario -> CRM/loyalty trigger -> NPD/assortment hypothesis -> BPM-1A/BPM-3 validation questions instead of merely recommending that scenarios be assigned."
      - "2026-09-01: Added multi-point contribution rule: when repeat_store_count or repeat_format_combo layers exist, calculate the revenue/client/frequency/LTV contribution of multi-point and cross-format clients before asking for a deeper client route bridge."
      - "2026-09-01: Added embodiment rule for analytical meta-statements: claims like 'this should be a dispatcher of causes' must be converted into the actual dispatcher/router/table in the report when the data or typology is available."
      - "2026-09-01: Added execute-the-recommended-analytical-artifact rule: if the report says to build bottleneck cards, entity shortlists, version checks, or diagnostic tables and the dashboard/raw data contains the grain, build them immediately instead of leaving a generic recommendation."
      - "2026-09-01: Added consumer-occasion evidence boundary: BPM-4 cheque/SKU analytics can surface monetization patterns, but visit occasions, purchase missions, and custdev-checkable motives must be sourced from BPM-1A, BPM-3, observation, mystery shopping, or explicitly marked as hypotheses."
      - "2026-09-01: Added anomaly-to-driver rule for point growth opportunities: when a point or segment looks unusual, especially low-flow/high-ticket, decompose what creates the anomaly before recommending a growth lever."
      - "2026-09-01: Added chart screenshot evidence rule for annotatable BPM-4 reports: when conclusions reference dashboard graphs, include compact screenshots/crops of the relevant graph in the DOCX/PDF near the interpretation, unless source access makes this impossible and the gap is stated."
      - "2026-09-01: Reclassified HoReCa/Retail network analytics as a separate BPM-4 commercial-network subtype, not as industrial distribution; the current skill filename is legacy compatibility, while subtype selection must preserve distinct retail logics."
      - "2026-09-01: Added hard validation for annotatable DOCX/PDF output: after generation or repair, inspect package/style XML or rendered output to ensure inline analytical fields have no residual monospace font references, non-black colors, or size overrides."
      - "2026-09-01: Strengthened annotatable-document typography guardrail: embedded analytical fields must not change font family or point size either; no monospace/code styling for metric keys, SKU names, formulas, or bridge fields in annotatable reports unless explicitly requested."
      - "2026-09-01: Added annotatable-document typography guardrail: BPM-4 dashboard DOCX/PDF reports must keep body text, inline fields, code-like metric keys, SKU names, and bridge formulas in black unless Ilya explicitly requests color coding; do not use blue/light inline-code styling in annotatable analytical reports."
      - "2026-09-01: Strengthened posthoc heuristic replay: when a heuristic changes or clarifies a conclusion, edit the affected report sections in place, then add the bottom coverage matrix; the matrix cannot substitute for updating stale local conclusions."
      - "2026-09-01: Added full heuristic replay pass: after annotation-derived analytical syllogisms accumulate, rerun the whole dashboard/report through the heuristic set, update the main analysis with a cross-heuristic audit, and create a separate annotatable cognitive-strategy document when requested."
      - "2026-09-01: Strengthened NBA rule: lists of repeat/loyalty mechanics such as frequency product, booster, bundle, threshold, NPD test, or personal recommendation must be converted into an NBA table when repeat and SKU/category layers exist."
      - "2026-09-01: Added Next Best Action calculation rule: repeat/RFM/loyalty recommendations such as related product, bundle, threshold, or personal recommendation must be converted into NBA candidates using equilibrium gap, SKU/category monetization, cooccurrence, segment/RFM, margin, and control-group gates."
      - "2026-09-01: Added repeat-economics equilibrium rule: when repeat, RFM migration, retention, or cohort tactics increase frequency while cheque, margin, basket depth, or premium mix degrades, calculate the equilibrium point before recommending scale."
      - "2026-09-01: Added cross-format client route rule: when point/store formats differ materially, compare mono-format and cross-format clients by frequency, average cheque, basket depth, LTV, RFM, SKU/category mix, and intervals; route missing client-level paths to BI/CRM data gaps."
      - "2026-09-01: Added RFM heteroskedasticity guardrail: RFM factor claims must not be written as one homogeneous law; check dispersion and interaction effects by format, territory, point size, identification quality, season, and basket economics."
      - "2026-09-01: Added cross-BPM SI upgrade rule for SKU/scenario recommendations: monetization findings such as seasonal bundles, display, add-ons, loyalty triggers, or NPD routes must be checked against available BPM-1A, BPM-3/mystery, BPM-7B, BPM-10/11 evidence before becoming actions."
      - "2026-09-01: Added entity-search execution rule: phrases like find/check/compare points, sellers, SKUs, categories, cohorts, or counterexamples must immediately produce named entities when the dashboard or raw base contains the relevant grain."
      - "2026-09-01: Added mandatory bottom hypothesis/data-gap register: every dashboard hypothesis, possible mechanism, or unresolved data deficit surfaced in local chart analysis must be collected near the end with ID, source, status, strengthening/weakening signals, next test, and decision impact."
      - "2026-09-01: Added hypothetical modality execution rule: phrases like could/might/мог/возможно must immediately become checked version tables when dashboard cuts exist."
      - "2026-09-01: Added SKU focus hypothesis test: statements like fewer/more SKU is better must be tested across point scale, cheque quality, SKU-per-flow normalization, and client basket variability before becoming a product-tunnel conclusion."
      - "2026-09-01: Added format average-cheque causal decomposition rule: every format/point average-cheque comparison must be decomposed into basket depth, item price, category/SKU mix, city/location, RFM/client layer, and explicit missing causal fields."
      - "2026-09-01: Added loyalty margin/SKU bridge rule: when loyalty upside is bounded by revenue and SKU/category data exists, check verified margin fields first; if absent, compute monetization proxy candidates and name the exact SKU-margin-ID bridge."
      - "2026-09-01: Added client-base incompleteness self-check: claims that RFM/LTV/cohorts may miss valuable scenarios must be quantified from identified/unidentified layers when available."
      - "2026-09-01: Added hypothesis verification-design rule: every assumption phrased as could/might/possible must state how it will be checked, what confirms it, and what weakens it."
      - "2026-09-01: Added mechanism-proof boundary rule: mechanism claims such as speed conflict, queue pressure, cashier discipline, or interface failure must state whether they are directly measured, indirectly supported, cross-BPM supported, or only a hypothesis with required evidence."
      - "2026-09-01: Added concrete shortlist rule: when recommending a pilot on points, sellers, SKUs, clients, segments, or regions, name the starting entities from available data instead of only giving selection criteria."
      - "2026-09-01: Added conditional-branch execution rule: analytical branches beginning with if/если must be checked immediately when relevant cuts exist, and rendered as version-check-verdict rows."
      - "2026-09-01: Added executed-cross-check block requirement: if the analysis says cuts must be stitched, the report must immediately show which cuts were actually checked and their verdicts."
      - "2026-09-01: Major 0.3.0 shift: BPM-4 dashboard analysis must populate hypothesis / BPM-SI / evidence-request logic, not only produce chart interpretations; strong client questions become SI candidates with downstream slide/roadmap impact."
      - "2026-09-01: Added intuition-baseline rule: when a metric direction looks intuitive or counterintuitive, state the management model relative to which that judgment is made."
      - "2026-09-01: Added dilemma-discrimination rule: when an interpretation has competing hypotheses, use available charts/cuts to raise or lower their likelihood instead of leaving versions equal."
      - "2026-09-01: Added base-normalization guardrail: large absolute contributions by format/category/point/segment must be normalized by base size before being treated as process deterioration or opportunity."
      - "2026-09-01: Added share-vs-absolute guardrail: interpretations must distinguish relative share signals from absolute count/value signals and state which level drives the management conclusion."
      - "2026-09-01: Added raw-base bridge derivation rule: when raw cheque/order grain is available, missing dashboard bridges such as cohort x point/SKU/seller must be built by the agent before being treated as data gaps."
      - "2026-09-01: Added interpretation-expansion requirement: compact diagnostic phrases like format load, peak pressure, cashier capture, or operational bottleneck must be unpacked into concrete mechanisms, tests, and client questions."
      - "2026-09-01: Added bottom-up Formula Profit ledger: significant recalculation metrics from all dashboard charts must be collected at the bottom with formula, value, management implication, and proof boundary."
      - "2026-09-01: Added immediate loyalty economics calculation: when identified/unidentified cheques and revenue are available, compute average-cheque gap, conversion scenarios, and breakeven thresholds instead of only recommending the calculation."
      - "2026-09-01: Generalized anomaly interpretation across the full dashboard: every graph anomaly must search explanatory signals in all available neighboring cuts, while missing bridges such as cohort x point/SKU must be explicit data gaps."
      - "2026-09-01: Added cross-chart anomaly stitching: if one chart creates competing mechanisms and neighboring dashboard cuts share keys, the agent must test those cuts directly and move unavailable cuts to data gaps."
      - "2026-09-01: Added point bottleneck heuristic: point-level charts 1.14-1.18 style must translate peer deviations into Formula Profit bottlenecks by SKU/category mix, basket depth, item price, RFM/customer composition, seller behavior, and identity capture."
      - "2026-09-01: Added point peer-diagnostic heuristic: point comparison charts must produce point-specific growth levers through similar/different peer sets, not only rankings."
      - "2026-09-01: Added cohort left-censoring and cohort anomaly heuristics: visible first cohorts must not be treated as true acquisition cohorts, and revenue retention drops must be checked by cohort age."
      - "2026-09-01: Added RFM factor-model expansion: context/flow findings must be decomposed into operational mechanisms such as flow habit, territory density, identity capture, format scenario, high-ticket low-frequency, and peak unidentified flow."
      - "2026-09-01: Added migration-upside-with-quality-decay heuristic: segment migration economics must test whether repeat/frequency gains are offset by average-cheque, margin, basket-depth, or quality degradation."
      - "2026-09-01: Added RFM retail tactic contract: segments must map to differentiated actions, economic gates, control groups, and predictor checks rather than audience labels."
      - "2026-09-01: Added annotation-loop contract: when Ilya comments on a generated dashboard document, update the source artifact and annotatable DOCX/PDF, not only the chat answer."
      - "2026-09-01: Added disproportionate-contribution syllogism for charts that compare result share with occurrence/check/share frequency: quadrants determine distinct management actions instead of top-revenue ranking."
      - "2026-09-01: Reframed Ilya-style dashboard reasoning as reusable syllogistic models, not universal metric-specific rules: divergence under growth, inverse movement, hidden mechanism branching, and causal caution."
      - "2026-08-28: Added visual reference parity guardrail: reference dashboards require matching layout grammar and product surface, not only matching section inventory."
      - "2026-09-01: Reframed HoReCa/Retail network dashboard as a BPM-4 subtype, not a loose mode: point/store economics, cheque identification, loyalty RFM/cohorts/clusters, SKU/category monetization, store-factor tree, and explicit source-gap placeholders."
      - "2026-08-28: Added Natalia reference parity rule: when a reference dashboard is supplied, BPM-4 output must match its dashboard-class interaction and section density, with explicit unavailable blocks instead of silently downgrading to readiness output."
      - "2026-08-28: Added automatic revenue-vs-gross-profit divergence diagnostics: visible gross-margin ratio, volume × margin bridge, transactional factor decomposition, and causal-language guardrail."
      - "2026-08-28: Clarified owner decision: SL is not a standalone canon; it is an Ipatovo-specific SPL fallback used only when payment-discipline data was unavailable and requires explicit owner acceptance elsewhere."
      - "2026-08-03: Added Ipatovo extension for flat B2B base analysis: revenue-only guardrail, hierarchical 1C ingestion, DSL/KML/BNT/SPL/PSC segmentation families, standard breaks, region matrices, growth extraction, and executive summary packaging."
      - "2026-05-28: Added handoff to bpm4-datalens-dashboard for Yandex DataLens implementation and QA."
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# Skill BPM 4 Commercial Network Dashboard

## Purpose

Use this skill to handle BPM-4 commercial-network dashboard work across several **separate** business logics: industrial / B2B distribution, HoReCa/Retail point networks, and distribution-like SKU contexts. Retail / HoReCa is not a subtype of industrial distribution: it has its own consumer, cheque, point-format, loyalty, RFM, basket, cashier, and store-economics logic. The skill is scoped to dealer / partner / client / SKU / warehouse / shipment / order-line analysis for B2B distribution, and to point / store / cheque / loyalty-client / cashier / SKU analysis when a project has owned retail, partner retail, foodservice points, dark stores, tonars, counters, or store-like outlets.

Do not apply the template mechanically to pure SaaS, professional services, or custom project sales. For mixed projects, explicitly separate the regular SKU layer from project/custom-production layers.

The skill owns **BPM-4 commercial-network dashboard subtypes**. The filename keeps the original B2B/industrial lineage for compatibility only; it must not be read as a claim that retail analytics inherits industrial-distribution logic:

| Подвид BPM-4 | Когда применять | Основной объект анализа |
|---|---|---|
| `B2B / industrial distribution dashboard` | дилеры, B2B-клиенты, склады, отгрузки, регулярные поставки, промышленная дистрибуция | клиент / контрагент / SKU / склад / регион |
| `HoReCa/Retail network dashboard` | точки, магазины, тонары, чеки, программа лояльности, продавцы, форматы точек | точка / чек / клиент лояльности / корзина / SKU |

Each subtype can run in two operating modes:

1. **Dashboard / BI mode** — semantics, Formula Profit, cross-filters, SI/SIF extraction, DataLens handoff.
2. **Base analysis mode** — one-shot dissection of a transaction base into segmentations, breaks, matrices, growth candidates, and executive summary artifacts.

If Natalia or another project operator supplies a reference dashboard, treat it as a mandatory dashboard-class parity benchmark, not as a loose visual example. The output may adapt business semantics to the selected subtype, but it must not silently downgrade to a source-readiness report, static chart packet, or thin Formula Profit proof-of-concept. In HoReCa/Retail, preserve retail-native logic instead of translating findings into industrial-distribution categories.

The canonical Vault home is:

`Vault/10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPM — Майнинг/OPM/EXEC/BPM-4/INS-OPM-4.07-B2B-дашборд-шаблон.md`

## When To Use

Use when the task mentions:

- BPM-4, numeric database analysis, Formula Profit, dashboard, Metabase, BI, Power BI, Plotly, DataLens, Yandex DataLens;
- industrial distribution, дилеры, дистрибуция, склады, SKU, отгрузки, регулярные поставки;
- HoReCa / Retail, собственная розница, партнёрская розница, точки, магазины, тонары, кассовые чеки, программа лояльности, продавцы / кассиры, средний чек, глубина чека, LTV, RFM, когорты, повторные покупки, кластеризация покупателей;
- OoS, lost demand, fulfillment gap, RFM dealers, GPC/RFS, client/product/warehouse segmentation;
- устойчивые регрессии / associations between client type and product group / nomenclature type;
- сочетанность, связность, co-occurrence, affinity, basket analysis, cross-sell, attach rate between SKUs / product groups / nomenclature;
- dashboard views that should feed SI / SIF or BPM Storyline-Storyboard.
- `разбери базу`, `брейки`, `матрица регион × категория`, `матрица регион × сегмент`, `сегментация клиентов`, `топ SKU`, `точки роста`, `недопроданный ассортимент`, `книги продаж`, `иерархическая выгрузка 1С`;
- account-based segmentation for B2B distribution: `DSL`, `KML`, `BNT`, `SPL`, `PSC`, `SL`, `контрагент-категория`, `категории внутри точки`, `кому продавать`, `что продавать`, `как продавать`.

## Ipatovo Extension: Source Priority

When a methodology pack contains both:

- image-native segment descriptions / slide language from a real project; and
- external textual reconstruction / adaptation,

use this priority:

1. **Real project visuals / slides / formulas** — primary lineage for naming and business meaning.
2. **Text spec** — computational adaptation and implementation guidance.
3. **Agent inference** — only for gaps, marked explicitly as inference.

For the Ipatovo lineage this means:

- `DSL`, `KML`, `BNT`, `SPL`, `PSC` are treated as the canonical family names if the slides use them.
- If a text spec introduces a slightly different decoding of the same abbreviation, do not silently overwrite the slide-native meaning.
- In outputs, explicitly mark whether the segment definition is `slide-native`, `text-adapted`, or `agent-inferred`.

## Workflow

1. Confirm scope.
   Check that the project is industrial B2B distribution or regular shipments. If it is project sales, custom manufacturing, SaaS, or professional services, do not apply the template directly.
   If the project is mixed, set scope as `distribution-like SKU layer + exceptions`: regular SKU/order-line analytics are allowed, while project/custom layers require separate cohort, TTV, and reconciliation gates.

1a. Choose BPM-4 subtype.
   - `B2B distribution dashboard` if the business object is account/dealer/distributor shipment economics.
   - `HoReCa/Retail network dashboard` if the business object is point/store/cheque/loyalty-client economics.
   - If both layers exist, explicitly separate them and do not merge end-consumer RFM with B2B account segmentation.

2. Choose operating mode inside the selected subtype.
   - `dashboard_mode` if the user needs BI semantics, interactive views, filter logic, Formula Profit, or Storyline/BI handoff.
   - `base_analysis_mode` if the user gives a transaction file / 1C export / flat sales base and asks for segmentation, breaks, matrices, growth points, or executive summary artifacts.
   - `hybrid_mode` if both are required: first normalize and segment the base, then route the agreed semantic layer into BI/dashboard views.
   - If the user or Natalia provides a dashboard reference, choose `dashboard_mode` or `hybrid_mode` unless the user explicitly asks for analysis-only output.

2a. Preserve reference-dashboard parity.
   When a reference dashboard is supplied, first extract a parity checklist:
   - global filters and scope tabs;
   - KPI/control top;
   - Formula Profit / revenue cascade;
   - monthly economics and year-over-year or period-over-period trend blocks;
   - breakdown tables by channel, client/account, region, manager, category, SKU, point/store when available;
   - RFM / repeat / cohort / cluster / affinity blocks where the source has client-period, document, or basket grain;
   - forecast, gap plan, or scenario blocks where enough history exists;
   - data-quality, reconciliation, source-files, and unavailable-data blocks.

   Implement the reference class of interaction and density: sidebar or visible filter panel, reset/preset controls, scoped views, chart + table pairs, and drill-down tables. If the current source cannot support a reference section, keep the section as `не рассчитано / требуется источник` with the missing fields, rather than removing the section. Do not justify the absence of these sections by saying the artifact was only built for readiness unless the user explicitly requested a readiness-only pass.

2b. Preserve visual reference parity.
   Section parity is insufficient if the product surface still feels like a generic analytical artifact. When Natalia's reference or a similar accepted dashboard is the benchmark, mirror the visual grammar:
   - a persistent left filter rail with select controls, reset, and compact section navigation;
   - one long vertical dashboard surface by default, not a hidden-tab report packet, unless the reference itself is tab-first;
   - a compact KPI/control top before charts;
   - numbered business sections such as `1.1`, `1.2`, `2`, `3`, `4–5`, matching the reference's reading rhythm;
   - chart + table or chart + source-status pairs in the same viewport band;
   - visible chips / badges for active perimeter, data status, and unavailable source blocks;
   - dense but calm BI typography: few framed cards, no decorative consultant slide styling, no oversized empty panels.

   If the output cannot visually resemble the reference because of renderer constraints, say so and provide the closest fallback. Do not call a dashboard parity-complete when only the metrics and section names match.

2c. Use HoReCa/Retail network dashboard variant when the source has points, cheques, loyalty clients, SKU/category lines, sellers/cashiers, or owned/partner retail formats.
   This is still BPM-4: the object of analysis becomes a commercial point/store and its retail basket, not only a B2B account. Do not force dealer segmentation names onto end-consumer behaviour.

   Minimum HoReCa/Retail dashboard blocks:
   - `периметр и источники`: period, points/stores, formats, cheque rows, loyalty-client rows, financial reconciliation status, source gaps;
   - `сеть`: revenue, cheques, identified-client cheque share, identified revenue share, average cheque, active points, month dynamics;
   - `точки`: point/store ranking, city/format breaks, top/bottom points, seller/cashier productivity where source supports it;
   - `формула точки`: revenue = cheques × average cheque; loyalty revenue = identified clients × LTV; average cheque = item price × basket depth;
   - `клиентская база`: identified / unidentified cheques, RFM, repeat funnel, cohort retention, clients by number of purchases;
   - `корзина`: category and SKU breaks, basket depth, SKU/category monetization, ABC/XYZ or equivalent turnover/stability view;
   - `сочетанность`: SKU/category co-occurrence with support, confidence, lift, basket count, and management action when basket grain exists;
   - `кластеры`: consumer-behaviour clusters with clear source variables, size, frequency, average cheque, LTV, and best-RFM share;
   - `дерево рычагов роста`: point-level branches separating client base, LTV, average cheque, frequency, item price, and basket depth;
   - `план действий`: local action register, test status, owner and effect, or an explicit `реестр действий не найден / требуется источник`.

   Minimum source gaps that must stay visible when absent:
   - verified gross margin / COGS, write-offs, rent or place cost, payroll, logistics, opening date, point status, opening hours, traffic, local actions/tests, promotion calendar, assortment introduction/removal dates;
   - approved point registry and format dictionary;
   - loyalty identity coverage limits: cheques without client ID must remain in revenue and average-cheque blocks but must not be used as repeat/LTV proof.

   Required management interpretation:
   - distinguish `high revenue because of flow`, `high revenue because of cheque`, `high revenue because of identified client base`, and `high revenue because of LTV`;
   - preserve Ilya-style dashboard reasoning as syllogistic models, not as universal metric-specific rules. Pattern A: if an aggregate success metric grows while a structurally related quality / capture / coverage metric worsens, do not produce a direct improvement recommendation; branch the hidden mechanism into operational failure, mix shift, new-flow composition, measurement/coverage change, and seasonal/contextual effect, then test by available dimensions before choosing an action. The branching must be materialized as a regression / factor matrix: `outcome -> candidate factors -> controls -> current evidence -> strengthened/weakened version -> missing bridge`. If raw grain exists, run correlations, stratified checks, regression, regularized model, tree-based feature importance, or another suitable directional model; if raw grain is absent, build the factor ledger from available dashboard cuts and put the missing raw-base bridge in data gaps. In the Мясной Гурман case this appears as revenue/cheque growth with falling identified-cheque share, but the reusable object is the divergence-under-growth syllogism, not the exact loyalty metric;
   - do not leave average-cheque decomposition as a methodological recommendation; translate `cheques × average cheque`, `item price × basket depth`, and category mix into segment-specific management regimes such as flow-protection, basket-expansion, traffic-growth, format/location diagnosis, and margin-gated premiumization;
   - Pattern B: if an input/breadth metric decreases while an outcome/intensity metric improves, do not assume the input should be restored; test whether reduction/focus increased attention, choice readability, conversion, bundle clarity, or concentration on strong positions. In the Mясной Гурман case this appears as falling unique SKU count with rising basket depth, but the reusable object is the inverse-movement syllogism, not the exact SKU/depth pair;
   - Pattern C: when a chart compares an entity's share of result with its share of occurrence / checks / customers / visits, read the ratio as disproportionate contribution, not as a plain ranking. A high ratio means the entity is more monetary / consequential than its frequency; a low ratio means it is frequent but less monetary per occurrence. Use quadrants: high result + high ratio = protect and scale; low result + high ratio = develop visibility and penetration; high result + low ratio = move right through premiumization, bundles, occasion design, or mix shift; low result + low ratio = clean, redesign, or keep only with a proven service role. In the Mясной Гурман case this appears as category/SKU revenue share versus cheque share, but the reusable object is the contribution-disproportionality syllogism;
   - Pattern D: when a chart shows customer segments, do not leave the segment as an audience label; translate each segment into management role, tactic, economic gate, control group, and stop condition. Strong segments may need protection, habit reinforcement, premium/bundle expansion, or NPD participation rather than discounts; weak or lost segments may need cheap reactivation tests rather than expensive universal win-back. In RFM this means segment-specific action, not generic campaign naming;
   - Pattern E: when segment migration promises economic upside, test whether another economic-quality parameter degrades during the migration. Do not estimate upside only as `customers × target-segment LTV delta`; compare at least two scenarios: migration with quality preserved versus migration with observed decay in average cheque, margin, basket depth, premium mix, or other money-bearing quality. In RFM/repeat contexts, if later purchases have lower average cheque, the CRM tactic must include a cheque/basket protection mechanism, an equilibrium point, and a stop rule;
   - Pattern E1: before calculating migration upside in RFM, clusters, format routes, customer profiles, or similar segmentations, build a segment kinship / transition matrix. Do not assume any segment can be converted directly into the best segment. Estimate adjacency by recency/frequency/monetary distance, basket/category similarity, purchase occasion, format/channel route, interval, LTV, offer responsiveness, and cost/contact fit. Output `segment A -> nearest segment B -> behavioral gap -> NBA/offer to close the gap -> plausible conversion proxy -> cheque/margin degradation risk -> data/profit gap`. If client-level segment history exists, calculate transition rates; if only aggregates exist, label the matrix as proxy and route `segment_t -> segment_t+1` bridge to data gaps;
   - Pattern E2: when repeat, RFM migration, retention, or cohort tactics increase frequency while cheque, margin, basket depth, premium mix, or SKU quality degrades, calculate the equilibrium point before recommending scale. Minimum revenue-only equilibrium: `baseline cheque / observed next-purchase cheque - 1` as required frequency uplift; `baseline cheque - observed next-purchase cheque` as quality gap; `baseline cumulative average target -> required next cheque` as recovery floor. If margin, bonus cost, discount, communication cost, or operational cost is available, also calculate profit-equilibrium and stop-loss. If those fields are absent, state `revenue-only equilibrium` and route `profit-equilibrium` to data gaps;
   - Pattern E3: when the recommendation says `related product`, `bundle`, `threshold`, `personal recommendation`, `next-best-product`, or similar, calculate Next Best Action candidates instead of leaving a generic mechanism. The same applies to lists of `проверяемые механики` in repeat/RFM/loyalty contexts: frequency product, monetary booster, bundle, margin-safe threshold, NPD test, or category recommendation must become an NBA table when repeat and SKU/category layers exist. Minimum NBA proxy: `target segment / RFM -> current or previous purchase signal -> equilibrium gap -> candidate SKU/category -> monetization index / average cheque contribution -> cooccurrence or affinity support -> margin / cost gate -> control-group KPI -> stop rule`. If `client_id × purchase_number × previous SKU/category × next SKU/category × margin × offer` is absent, label the result `proxy-NBA` and route the missing bridge to BI/CRM data gaps;
   - Pattern F: when a chart shows cohorts but loyalty-program join date, registration date, or first-purchase history before the extraction window is unknown, treat the first visible cohort as left-censored. Do not read it as true new-customer acquisition; label it `visible cohort / видимая когорта` until full first-event dates are restored. For loyalty programs, always request and separate three dates where available: `дата присоединения к ПЛ`, `первая видимая покупка в выгрузке`, and `настоящая первая покупка в полной истории`;
   - Pattern G: when a chart shows cohort revenue retention, search for cohort-age anomalies: excessive revenue drop from month 0 to month 1, unusually weak retention versus same-age cohorts, or sudden later-month decay. Each anomaly must produce a mechanism branch: first-purchase novelty not repeated, promotion cohort, point/format mix, seasonal category, identity/coverage issue, or CRM follow-up gap;
   - Pattern H: when a chart compares points/stores/branches, do not stop at ranking. Build peer sets by format, city/territory, flow, average cheque, basket depth, identity capture, repeat/RFM quality, maturity, and category mix where available. For each point, name the closest peer benchmark, the material difference, the growth hypothesis, the action, and the metric. A point's growth lever is found in its deviation from comparable points, not from the total network average alone. Peer sets must be materialized in the report as a registry/table, not left as prose;
   - Pattern H2: peer-set logic applies to every action-bearing slice, not only points. If a conclusion uses format, city/territory, seller/cashier, SKU/category, RFM segment, consumer cluster, cohort, channel, or campaign as a basis for action, build the relevant peer-set registry: `slice -> comparison unit -> similarity criteria -> peer members or peer definition -> benchmark -> deviation -> action -> missing bridge`. If source grain is absent, record the exact peer-set bridge gap;
   - Pattern I: when point-level charts unfold from comparison into average cheque, LTV, depth, SKU/category mix, RFM, customer clusters, and sellers, convert each peer deviation into a Formula Profit bottleneck. Do not treat low average cheque, low LTV, or low repeat as self-explanatory. Test whether the symptom is driven by cheap SKU dominance, low basket depth, low item price, customer/RFM composition, weak premium occasion, unidentified flow, seller/cashier behavior, or format/location constraints. Output `symptom -> possible mechanism -> drill-down slice -> controllable lever -> experiment KPI`;
   - Pattern J: when one chart produces an anomaly or competing explanations and neighboring dashboard cuts share join keys, run the cross-chart check in the same pass. Do not leave `check by point / seller / category / cohort / segment` as a recommendation if those fields are already available. Output `anomaly -> mechanism candidates -> available join keys -> checked cuts -> strengthened explanations -> weakened explanations -> missing fields`. If the needed cut is absent from the ready dashboard, first check whether raw cheque/order grain is available. In raw-base mode, build the missing bridge yourself before calling it a data gap: for example `cohort x point`, `cohort x category/SKU`, `cohort x seller`, `cohort x first purchase category`, or `segment x point/SKU`. This applies to all graph classes: cohort anomalies must search the whole dashboard and, when raw base exists, derived raw-base cuts for monthly, point, format, category/SKU, seller, RFM, client-stage, channel, and promotion signals; SKU anomalies must be read through cheque, depth, repeat, point and category cuts; RFM anomalies must be read through point, format, cashier, SKU and calendar cuts. Do not infer a bridge that is absent and not derivable;
   - Pattern K: when a loyalty / CRM recommendation can be economically bounded from the current dataset, calculate it immediately. If identified and unidentified cheque counts and revenue are present, compute identified average cheque, unidentified average cheque, observed gap, unidentified cheque base, conversion scenarios, and breakeven cost thresholds. Do not write only `calculate loyalty economics` unless the required fields are absent. Keep causal caution visible: the observed gap is an upper-bound / directional benchmark unless controlled uplift or margin data proves economic incrementality;
   - Pattern L: collect every significant bottom-up recalculation of Formula Profit indicators into a final ledger. This includes upper-bound potential, breakeven thresholds, metric-to-money conversions, RFM migration upside, quality-decay cost, repeat-economics equilibrium, point bottleneck economics, category/SKU monetization indices, and cohort revenue gaps. Each row must show source chart(s), metric, formula/value, management implication, and proof boundary. Do not leave useful recalculation metrics scattered only inside graph comments;
   - Pattern L2: collect every active dashboard hypothesis, possible mechanism, and unresolved data deficit into a final hypothesis / data-gap register near the end of the report. Local chart commentary may introduce a hypothesis, but the report is incomplete unless the bottom register gives it an ID, source chart(s), current status, what strengthens it, what weakens it, next test or missing bridge, and the decision it can change. Separate hypotheses from data deficits: hypotheses are testable versions about mechanisms; data deficits are missing keys, grains, lineage, or source rights blocking the test. Do not leave phrases like `рабочая гипотеза`, `требует проверки`, `данных не хватает`, `bridge gap`, or `остается недоказанным` only inside graph prose;
   - Pattern L3: when dashboard findings drive CRM, loyalty, NPD, point-governance, BI-roadmap, or profit decisions, build a fact/hypothesis issue tree near the bottom of the report before or alongside the hypothesis register. The tree must go up to four levels where the material can support it: `management question -> cause / lever zone -> mechanism -> testable node`. Each node must carry proof status `факт`, `гипотеза`, `расчет / proxy`, or `дефицит данных`, plus evidence and management consequence. The purpose is to show how facts and hypotheses connect, not merely to list hypotheses. If a visual map materially improves reading, include it in the annotatable report as an embedded figure and keep the text/table version as the auditable source;
   - Pattern M: do not leave compact interpretation phrases unexplained. If the output says `flow format`, `peak load`, `cashier capture`, `operational bottleneck`, `format effect`, `seller discipline`, `assortment readability`, or similar, immediately unpack it into concrete mechanisms, observable tests, required cuts, owner-facing questions, and the first manageable pilot action. The reader should not have to infer what the phrase means operationally;
   - Pattern N: never confuse relative shares with absolute counts or values. If a chart uses a share/percentage, state the share movement as the primary signal and then separately state the absolute movement if it matters. Shares usually indicate process quality, capture, mix, or proportional contribution; absolutes indicate scale and economic weight. The management conclusion must say which level drives it and how the other level supports or weakens it;
   - Pattern O: when a segment, format, category, city, or point has the largest absolute contribution, normalize by its base before interpreting deterioration or opportunity. Check at least one relevant denominator: number of points, total cheques, revenue base, client base, store count, category exposure, or format share. Output `absolute contribution -> base size -> relative rate/change -> conclusion preserved or weakened`. A large format may dominate absolute growth only because it dominates the network;
   - Pattern P: when a conclusion contains a dilemma or competing explanations, do not leave them as equal possibilities if the dashboard or raw base can distinguish them. Search for discriminating evidence: cross-sectional slices, within-entity dynamics, base normalization, counterexamples, adjacent metrics, and plausible third factors. Output `versions -> discriminating signal -> check -> strengthened version -> weakened version -> remaining uncertainty`. If evidence is insufficient, say why and record the needed cut;
   - Pattern Q: when a correlation sign or chart direction is described as intuitive, counterintuitive, strange, or logical, name the baseline management model. Output `simple expected model -> observed direction -> why counterintuitive under that model -> alternative model that makes it logical -> required check`. Do not treat intuition as universal; it is always relative to a model of how the business mechanism should work;
   - Pattern R: every strong analytical question to the client must be promoted into hypothesis / BPM-SI / evidence-request logic. Do not leave useful questions only as interview prompts. Output `hypothesis or SI candidate -> client fact to request -> what slide, roadmap decision, BPM route, CRM architecture, loyalty economics, or BI control changes if confirmed / weakened`. This is the 0.3.x behavior: dashboard analysis actively grows the project SI layer;
   - Pattern R2: SKU/scenario recommendations are not allowed to jump from BPM-4 monetization to action without cross-BPM SI checking. If a chart suggests `develop SKU`, `seasonality`, `bundle`, `display`, `add-on`, `sauce/grill companion`, `loyalty trigger`, or `NPD route`, convert it into a syllogism and evidence gate: `BPM-4 monetization -> BPM-1A consumer occasion -> BPM-3 or mystery-shopper experience -> BPM-7B product route -> BPM-10/11 CRM/BI trigger`. State which layers are already supported, which are missing, and how the SI / slide-intent changes. If only BPM-4 supports the signal, call it a monetization hypothesis, not a ready commercial action. Do not write `create more visit occasions`, `family purchase mission`, `weekend stock-up`, `premium occasion`, or similar custdev-checkable motives as proven from cheque/SKU data alone; BPM-4 may name candidate occasions only as hypotheses to be confirmed through BPM-1A, BPM-3, observation, mystery shopping, or customer intercepts;
   - Pattern S: if the report states `check / stitch / cross-check by available cuts`, it must immediately include an executed-check block, not only an instruction. Output `checked cut -> result -> strengthened mechanism -> weakened mechanism -> remaining bridge gap`. If a cut cannot be checked from the ready dashboard, first attempt raw-base derivation where source grain allows it; otherwise record the exact missing key;
   - Pattern T: analytical `if / если` branches are not allowed to remain conditional when the relevant dashboard cuts or raw-base keys exist. Convert them into checked branch rows: `version / condition -> how checked -> verdict -> remaining data gap`. Keep `if` only for genuinely future data, explicit scenario modeling, or missing-key cases;
   - Pattern U: when the report recommends choosing pilot entities, do not stop at criteria such as `choose 6-8 points` or `choose 8-10 sellers`. If the data contains entity-level rows, immediately output a starting shortlist with `entity -> why selected -> absolute signal -> relative signal or denominator -> what to test -> pilot metric`. If the entity-level cut is absent, record the exact missing key rather than leaving the team to operationalize the recommendation manually;
   - Pattern U2: phrases such as `найти точки`, `найти контрпримеры`, `сравнить группы`, `проверить категории`, `выбрать SKU`, `посмотреть продавцов`, or their English equivalents are execution triggers, not recommendations, whenever entity-level grain exists. The same paragraph must show the named entities found, the selection rule, absolute and relative metrics where relevant, and the resulting verdict. If the entity list cannot be produced, state the missing field or source access gap. In assortment-focus cases, always compare both supporting entities and counterexamples before preserving a focus hypothesis;
   - Pattern V: mechanism claims require a proof boundary. If the output says `speed conflict`, `queue pressure`, `cashier discipline`, `interface failure`, `motivation conflict`, `technical failure`, `new customer flow`, or similar, state the evidence class: `directly measured`, `indirectly supported by BPM-4`, `supported by cross-BPM evidence`, `weakened`, or `hypothesis only`. When direct numeric proof is absent, cite the BPM/source group that supports the hypothesis and list the exact fields needed to prove or reject it. Do not write mechanism language as fact when only the symptom is measured;
   - Pattern W: assumptions phrased as `could`, `might`, `possible`, `могло`, `могла`, `возможно`, `может быть`, or similar must include a verification design in the same row or paragraph: `source to request / available cut -> test -> confirming signal -> weakening signal -> decision that changes`. A bare list of questions is insufficient when the assumption affects CRM roadmap, loyalty economics, point governance, seller KPI, SKU decisions, or BPV routing;
   - Pattern X: if the report says the client base, RFM, LTV, cohorts, loyalty layer, or identified-client analytics may be incomplete, quantify the blind zone immediately when identified/unidentified layers exist. Minimum check: identified cheque share, unidentified cheque share, identified revenue share, unidentified revenue share, average cheque by identity status, peak-period split, and top point/format/category scenarios where unidentified revenue or average cheque is materially high. Only fields not present after this check become data gaps;
   - Pattern Y: when a loyalty / CRM upside is expressed as a revenue upper bound and SKU/category data exists, immediately test whether a margin bridge is available. First verify field semantics: do not treat `gross`, discount, list price, or pre-discount amount as валовая прибыль unless COGS/margin lineage proves it. If verified margin is absent, compute a monetization-proxy shortlist of categories/SKUs using revenue share, cheque/share frequency, revenue per cheque, materiality, and seasonality; then state the required bridge `check_id -> ID status -> SKU/category -> margin/markup/COGS -> promo/discount -> point/format`. The output must say which candidates could raise or lower loyalty profit economics and which source owns the missing margin;
   - Pattern Z: when comparing average cheque between formats, cities, point types, channels, or store groups, never leave the statement as `A has higher average cheque than B`. Decompose immediately into `cheques/flow`, `basket depth`, `average item price`, `category/SKU mix`, `identified-client share`, `RFM/client layer`, `city/territory/location`, `seasonality`, and `data gaps for customer type / visit mission / traffic / competition`. Output what is proven numerically, what is only a likely mechanism, and what must be checked through BPM-3/observation/customer intercept or raw cheque bridges. If the item price is similar but basket depth differs, say that the mechanism is a fuller basket/visit mission rather than expensive unit price;
   - Pattern AA: when interpreting ассортиментная фокусировка, never equate focus with universal SKU reduction. If the report suggests that fewer or more SKU may be better, test at least four levels: `unique SKU -> revenue/cheques scale`, `unique SKU -> average cheque/depth/item price`, `SKU per flow denominator such as SKU per 1,000 cheques`, and `identified-client basket variability -> frequency/LTV/RFM quality` where available. A valid conclusion must separate point assortment breadth, relative breadth per flow, customer basket breadth, and occasion-specific narrow baskets. If `client_id x check_id x SKU` is absent, use cluster/product-group proxy only as partial evidence and name the missing bridge;
   - Pattern AB: hypothetical modality is an execution trigger. If a report says `could`, `might`, `may`, `мог`, `могла`, `возможно`, `вероятно`, `может быть`, `не исключено`, or names several possible mechanisms, immediately convert the phrase into a version-check table when any relevant dashboard cut exists. Minimum output: `version / hypothesis -> available cut used -> result -> verdict strengthened/weakened/untestable -> exact missing bridge`. Do this before finalizing the paragraph; do not leave hypothetical prose when the data can test at least part of it. If only partial checks are possible, write `проверено частично` and name the fields that block causal proof;
   - Pattern AC: after several annotation-derived analytical syllogisms have accumulated, or when Ilya asks to `перепройти весь массив / документ`, run a full heuristic replay pass instead of only patching the latest local paragraph. First edit the affected report sections in place whenever a heuristic changes, narrows, strengthens, weakens, or clarifies a conclusion; then add a cross-heuristic audit near the bottom. The bottom matrix is coverage evidence, not a substitute for correcting stale local conclusions. Output `section -> heuristic -> changed conclusion -> checked evidence -> proof boundary / bridge gap -> roadmap consequence`. If requested as a document, create a separate annotatable DOCX/PDF with the reusable cognitive strategies, not just the client-specific findings. Keep the strategies framed as syllogistic starting models, not universal laws;
   - Pattern AD: for annotatable BPM-4 dashboard DOCX/PDF reports, keep all body text and embedded analytical fields visually black by default and in the same font family / point size as the surrounding paragraph or table cell. Inline metric keys, SKU/category names, bridge formulas, English source-field names, code-like fragments, and hyperlinks must not be styled as pale blue, link-like, monospace, smaller, larger, or otherwise typographically separate text unless Ilya explicitly asks for color coding or code styling. Headings and table fills may use restrained structure only if they do not make field values look like secondary/light text; when in doubt, plain black surrounding typography wins. When generating from Markdown, do not let backticks or inline-code markup become Word code styling in the annotatable report; either render those fragments as plain text or normalize their runs after export. When repairing an existing DOCX, inspect visible runs and underlying `word/*.xml` for residual `Courier`, `Courier New`, `Consolas`, `Menlo`, `Monaco`, non-black `w:color`, and field-level `w:sz` overrides that make fragments smaller/larger than the surrounding paragraph. The completion check is `no residual monospace references + no non-black body/field colors + rendered DOCX visually shows inline fields as ordinary text`;
   - Pattern AE: annotatable BPM-4 dashboard reports must include compact screenshots or cropped images of the graphs being interpreted. If a section says `график 1.1`, `по графику`, `на дашборде видно`, or uses chart evidence for a management conclusion, place a small readable screenshot/crop of that graph near the interpretation or at the start of the graph subsection. Screenshots are evidence anchors, not decorative images: crop to the relevant plot and legend, keep captions short, preserve graph numbering, and avoid full-page dashboard dumps when a focused crop is enough. If the source is an HTML/BI dashboard, use browser/export/screenshot tooling; if it is PDF/PPT, extract or render the relevant page/region; if the graph cannot be captured, write `скриншот графика недоступен` with the source-access reason and keep the chart ID in the evidence trace. A text-only annotatable report is incomplete when graph screenshots are technically available;
   - Pattern AF: when a chart surfaces an unusual growth opportunity, interpret what creates the anomaly before naming the lever. For low-flow/high-ticket points, do not stop at `низкий поток + высокий чек`: decompose into at least `basket depth`, `average item price`, `category/SKU mix`, `identified-client share`, `repeat/RFM`, `format/city`, and `base-size reliability`. Separate mechanisms such as `fuller basket`, `premium/SKU price mix`, `loyalty-visible mission`, `seasonal product spike`, and `small-base artifact`. Output `unusual point/segment -> measured anomaly -> likely driver -> proof status -> growth lever -> missing data`. If the high cheque is driven by depth, scale the purchase mission or bundle; if by item price/category mix, build premium add-on and recommendation logic; if by weak base, do not promote it as a growth point until stability is checked;
   - Pattern AG: recommendations to build analytical artifacts must execute immediately when the data grain exists. If the prose says `build bottleneck card`, `make shortlist`, `check versions`, `compare sellers/points/SKU`, `construct peer-set`, or `form diagnostic table`, do not leave it as a task unless the necessary fields are absent. Build the artifact in-place with named entities and measured values, then list remaining data gaps. For point bottleneck cards, output `point -> symptom -> peer deviation -> checked slices -> likely bottleneck -> lever -> experiment KPI -> missing data`;
   - Pattern AH: analytical meta-statements must be embodied. If the report says `this block should be a dispatcher`, `this should route causes`, `this must be a decision matrix`, `not a list but a mechanism`, or similar, immediately convert the statement into the actual router/table/matrix with rows, conditions, proof checks, actions, KPI, and missing data. Do not leave methodological self-description as a substitute for the artifact it names;
   - Pattern AI: multi-point and cross-format client layers must be quantified when available. If the dashboard contains `repeat_store_count`, `repeat_format_combo`, store-count buckets, format-combo buckets, or similar fields, calculate at least `client share`, `revenue share`, `frequency`, `average cheque`, `basket depth`, and `LTV` for mono-point, 2+ point, 3+ point, and relevant cross-format segments. Do not leave only `need client_id -> point -> format bridge`: first state what the aggregate already proves, then name the deeper bridge needed to distinguish network-infrastructure behavior, local migration, and distinct purchase missions;
   - Pattern AJ: consumer clusters must be embodied as scenario/action rows when the cluster layer exists. If the prose says `give each cluster a product scenario`, `CRM trigger`, `NPD hypothesis`, `loyalty action`, or similar, immediately build a table: `cluster -> measured profile -> product scenario -> CRM/loyalty trigger -> next best action -> NPD/assortment hypothesis -> BPM-1A/BPM-3 validation question -> proof boundary`. If cluster client counts overlap or exceed total identified clients, mark clusters as overlapping behavioural profiles, not MECE segments;
   - Pattern AK: syndicated cross-chart ideas must carry syndicated proof. If the report claims `two commercial machines`, `format roles`, `route-to-store mechanism`, `segment engine`, `network infrastructure behaviour`, or another idea built from multiple graphs, attach the numerical support from every relevant available cut: share of revenue/checks/clients, median point metrics, aggregate format metrics, ID share, repeat/frequency, average cheque, depth, LTV, and cross-format / multi-point contribution. Separate what is numerically proved from consumer motives that require BPM-1A/BPM-3;
   - Pattern AL: best-practice formula extraction must happen immediately. If the prose says `capture formula`, `снять формулу`, `transferable package`, `donor practice`, `эталон`, or similar for a city, point, format, seller group, SKU/category, or segment, build a factor-analysis packet in the report: `candidate donor -> proved factors -> hypothesized mechanisms -> transferable elements -> non-transferable context -> first peer tests -> KPI -> missing evidence`. Do not leave `снять формулу` as a recommendation when the dashboard already contains point/format/category/seller/client cuts;
   - Pattern AM: for HoReCa/Retail high-ticket low-flow points, bottleneck cards must include a geo/retail enrichment layer when point addresses are available. The diagnostic sequence is `internal BPM-4 check -> address/open-data proxy -> BPM-3/field/customer check -> verdict`. Internal BPM-4 checks: cheque stability by month, basket depth, item price, SKU/category mix, identified-client share, repeat/RFM, seasonality, format/city peer-set, and base-size reliability. Address/open-data checks: geocode, residential/office density, pedestrian and car access, public transport, traffic anchors, nearby food/meat/grocery competitors, map rating/reviews, street visibility, parking, and route convenience. BPM-3/field checks: signage visibility, entrance clarity, shelf/display, seller explanation, service speed, local visit occasion, and reasons for non-repeat. Open data must be treated as `proxy локального потенциала`, not proof of profit, real footfall, customer mission, seller quality, or margin. If addresses are missing, record the exact field gap and keep location explanations as hypotheses;
   - Pattern AN: cross-BPM recommendations must use `reuse first, program enrichment second, request third`. If a BPM-4 finding says it needs BPM-1A, BPM-3, BPM-7B, BPM-10/11, BPV-01, or another adjacent BPM, first inspect or cite already collected project evidence from that BPM when available. If the BPM is ongoing, pending, or planned, enrich its program with exact questions, variables, observations, cuts, or hypotheses generated by the BPM-4 finding. Output `decision -> existing BPM evidence used -> what it proves -> what BPM program is enriched -> exact question/field/check added -> what enrichment returns to the source BPM -> remaining gap -> new evidence request only if needed`. Do not create a generic new survey, interview, mystery shop, CRM task, or product gate when existing BPM evidence already answers the decision. If the adjacent BPM source is inaccessible, record `existing BPM source access gap`, not a new fact gap;
   - Pattern AO: when a new annotation introduces or changes a reusable heuristic, run a full replay consistency pass over the whole report. Update affected local conclusions in-place, then update the heuristic list, bottom-up ledger if money/metric implications exist, hypothesis register, data-gap register, cross-section matrix, and coverage ledger. The bottom matrix cannot repair contradictions left in earlier graph sections. The pass must explicitly mark `changed / strengthened / weakened / no-op` for major sections touched by the heuristic;
   - Pattern AQ: after a dense annotation set, close the set with an explicit annotation-sweep ledger in the report or working document. Minimum columns: `annotation theme -> absorbed into local conclusion? -> absorbed into bottom issue tree / hypothesis / data-gap register? -> absorbed into roadmap / data request? -> absorbed into skill rule? -> remaining gap / no-op reason`. This ledger is required when the user says `весь последний сет правок`, `все неучтенное`, `учти последний пакет`, or equivalent. Do not claim the set is handled only because individual paragraphs were edited; the closure ledger is the audit trail that the latest heuristics did not get lost;
   - Pattern AP: any profit-dependent conclusion must create a data-gap row when the source is revenue/proxy-only. If the report recommends or evaluates loyalty economics, NBA, RFM migration, NPD, point scaling, point closure, promotion, unit economics, payback, or margin-safe action, check for gross margin, contribution margin, COGS, markup, write-offs, discounts, loyalty bonuses, contact/communication cost, IT/operational cost, payroll, rent/place cost, logistics, opening date and point status. If any fields needed for the stated profit claim are absent, the report must add/update a bottom data-gap row `profit layer / profit bridge`, state which profit conclusion is blocked, and label the current result `выручка / proxy`, `monetization proxy`, or `revenue-only equilibrium`, not `прибыль`;
   - Pattern AR: every new raw, mart, BI export, table dump, source coverage file, or client source that arrives after a dashboard narrative must trigger post-ingest caveat retirement. The agent must update the original conclusions / growth-points artifact in-place and reconcile every active data gap against the new source: `закрыто источником`, `сужено`, `заменено более точным gap`, `остается открытым`, or `не применимо`. Do not keep old phrases like `нет сырой базы`, `нет RFM`, `нет bridge`, or `dashboard-only` if a new parquet/mart/source now supports the calculation. Replace them with exact source rights such as `computed bridge high confidence`, `matched-only layer`, `point-month aggregate`, `partial item layer`, `native key gap`, or `profit layer absent`. When the new source opens a calculation, run it immediately or state the exact blocker; when it closes a caveat, remove or rewrite the caveat both near the local conclusion and in the bottom data-gap register. If the iteration produces a reusable analytical or production rule, update this skill in the same pass;
   - Pattern AS: after a report, dashboard, source ledger, skill, hypothesis register, issue tree, or data-gap register receives multiple updates, additions, expansions, cancellations, replacements, or status changes, run a change-delta heuristic audit. Classify each material delta as `обновление`, `дополнение`, `расширение`, `отмена`, `смена статуса`, `замена`, `сужение gap`, `закрытие gap`, or `no-op`. For each delta, state which heuristics it activates, what conclusion it strengthens or weakens, what old statement it supersedes, what new exact gap remains, and whether the roadmap/data request changes. Do not treat a delta ledger as bookkeeping only: it is a consistency check that prevents old caveats, old hypotheses, and old recommendations from surviving after the evidence base changes;
   - Pattern AT: package manifests, file manifests, processing inventories, and export manifests are first-class lineage evidence, but not first-class metric evidence. When a manifest arrives, register it as `package manifest / lineage ledger`, copy it to project sources, compare expected files with physically present files, and update source coverage / data-gap registers. A manifest can prove that a processed package expected certain parquet, CSV, QA markdown, dictionary templates, processed directories, and QA directories; it cannot prove the metric content of a referenced file until that physical file is read. Output `expected -> present / missing -> source class -> what conclusion or gap changes -> recovery action`. Use manifest deltas to avoid silent missing QA packs, missing dictionaries, and false confidence in source coverage;
   - Pattern AU: `dim_*_candidates`, mapping candidates, dictionary candidates, and template-like dimension exports are not approved master data by default. Treat them as candidate normalization evidence and QA objects. Before using them in SKU/point/format conclusions, inspect `source`, raw names, raw codes, category fields, metric fields, nulls, duplicate keys, source-row counts, conflicting categories, and whether a human-approved mapping exists. Output `candidate dimension -> source split -> coverage -> duplicate/conflict risk -> what it enables -> what it does not prove -> approval/recovery action`. For SKU dictionaries, candidate rows can support source vocabulary, top SKU/entity lists, source reconciliation, and NPD/NBA shortlist hygiene; they do not prove final 1C↔loyalty SKU equivalence, margin, category truth, or product role until mapping is approved;
   - Pattern AV: POS/point candidate dictionaries are a special case of candidate dimensions. They can close a manifest/package missing-file gap and support point vocabulary, raw alias inventory, address parsing, peer-set hygiene, source coverage, and geo/open-data enrichment prep. They do not prove approved point master, Штрих ↔ mLoyalty point equivalence, real address, coordinates, format, ownership, opening status, or point profitability until aliases are normalized and approved. Inspect at least `source`, `pos_name_raw`, `pos_id_raw`, first/last dates, row counts, net amount, duplicate POS IDs, missing IDs, city/address parsability, format hints, and cross-source overlap. Output `POS candidate dictionary -> source split -> ID/null coverage -> address/alias risk -> what it enables -> what it does not prove -> approval/enrichment action`;
   - Pattern AW: dashboard construction logs, graph-build logs, embedded-source maps, and similar build notes are lineage / metric-contract evidence, not direct business metric evidence. When such a log arrives, persist it as a project source and extract a chart passport: `graph/block -> JSON view/table -> physical source file -> formula -> filters/scope -> visual encoding semantics -> derived QA/payload dependency -> reproducibility status -> missing artifact`. Mandatory checks: separate network-level filters from selected-point filters; distinguish visual-only normalized table bars from metrics; mark rows like `не раскрыто до SKU` as coverage/exposure rows; identify which charts are directly recomputable from parquet and which require QA CSV, payload, embedded source JSON, metric dictionary, or build script. If a chart depends on missing derived files such as RFM score CSV, cluster CSV, cooccurrence CSV, match-coverage CSV, or payload JSON, name those files in the data-gap register and do not claim full reproducibility from parquet alone;
   - Pattern AX: analytical atlas packages are source bundles, not loose attachments. Trigger when a BPM-4 HTML/PDF/BI artifact is accompanied by a chart map CSV, chart-ready `data/` files, artifact manifest, QA file and preview. Persist the whole bundle to project sources, then register it as `аналитический атлас-пакет / chart-ready dashboard bundle`. Minimum inspection: artifact name/date, chart count, section taxonomy, chart-map columns, per-chart data file presence, row/column shape, QA status, render errors, source periods, source perimeters, `external_writeback`, and explicit limitations. Use chart-ready CSV immediately for posthoc checks, entity shortlists, regressions/correlations and caveat retirement. Treat chart-map rows with `поддерживаемый_вывод / управленческое_применение / оговорка` as a mini claim ledger feeding the report and Storyline-Storyboard. Never equate chart-ready replay with full raw-to-chart reproducibility: build script, source JSON, metric dictionary, preprocessing QA, approval mappings and profit layer remain separate gaps unless physically present and inspected. QA/render success proves display integrity, not business metric truth;
   - Pattern AY: HoReCa/Retail chart families from the MG atlas are an improvement / extension idea bank, not a mandatory dashboard template. Remember them as candidate additions that may strengthen a BPM-4 analysis when they reveal a hidden mechanism, create a better management comparison, close a stale caveat, support BPM-SI, or connect BPM-4 to CRM/NPD/loyalty decisions. Do not mark a dashboard incomplete merely because one family is absent. Use only the families that fit the decision and data grain; if a missing family blocks a specific decision, record that exact data gap. Useful idea families:
     `growth-quality divergence`: revenue/cheques growth combined with average cheque, depth, discount load and item value to see whether growth improves or degrades управляемость;
     `identity blind zone`: identified vs unidentified revenue/cheques, match coverage and source coverage to quantify what RFM/LTV/cohorts cannot see;
     `value-volume-price/mix bridge`: ERP/1C growth decomposition into physical volume and price/mix so assortment strategy is not confused with simple demand growth;
     `sell-in / sell-out SKU bridge`: SKU overlap between ERP and loyalty/retail item layers to connect production/channel portfolio with consumer basket evidence;
     `point archetype map`: traffic vs average cheque / revenue bubble / point Pareto to separate flow machines, high-ticket points, underperformers and hidden growth pockets;
     `format-city-peer decomposition`: format comparison and city portfolio to avoid mistaking format effects for geography, maturity, location or base-size effects;
     `ID opportunity by point/seller/time`: point and cashier/seller scatter plus weekday quality to move from "improve loyalty" to named operational bottlenecks;
     `point stability / heatmap`: point growth-stability and point-month heatmap to distinguish scalable leaders, volatile spikes, recovery candidates and seasonal/local anomalies;
     `repeat economics`: repeat funnel, survival to many purchases and cheque/depth dynamics by purchase number to calculate retention upside and quality decay;
     `cohort value diagnostics`: retention plus revenue per retained client, with left-censoring / true-cohort guardrail, to find acquisition-quality or first-to-second-purchase breaks;
     `route-to-store`: multi-store and cross-format customer routes to detect high-value network users, local migration, and format-specific purchase missions;
     `RFM governance`: RFM composition, cube, scatter, bonus flow and client stages to turn segments into actions, boundaries, drifts and campaign gates;
     `basket cluster scenarios`: cluster portfolio/value, product heatmap, RFM/format overlays, geometry and LTV dispersion to convert clusters into CRM triggers, NPD hypotheses and BPM-1A/BPM-3 questions;
     `purchase repertoire`: product-group освоение by purchase number and basket breadth vs frequency/LTV/best-RFM share to shift CRM from one-off add-ons to repertoire expansion;
     `basket affinity`: SKU/category pairs, group co-occurrence and format-pair differences to design bundles, shelves, NBA and format-specific offers with support/confidence/lift where possible;
     `service / exclusive category role`: service-group and exclusive-category monetization to distinguish traffic builders, basket boosters, premiumizers and brand-proof categories;
     `method boundary diagnostics`: cluster-K and RFM-boundary charts to show that segmentation choices are управленческие суждения with stability checks, not decorative math.
     Output rule: when using any idea, state `idea -> decision it improves -> evidence needed / available -> proof boundary -> whether to add now, request data, or no-op`;
   - Pattern AZ: HoReCa/Retail point-opening plans must separate `текущая сеть`, `потолок оптимизации существующих точек`, and `остаток на новые точки`. When the target is a multi-year revenue plan, calculate the required CAGR/root from current fact to target year, then build yearly residuals: `target revenue -> existing network after run-rate and optimization ramp -> new-point revenue gap -> required points`. If the user or strategy sets a format mix such as `не менее 80/20 в пользу тонаров`, treat it as a portfolio constraint, not a city-level universal rule. First classify current and candidate cities by city-format archetype: `моноформат тонаров`, `сбалансированный микс`, `районная мясная / high-ticket low-flow`, `формально микс, но коммерчески моноформат`, `недостаточно наблюдений`. Use city-format evidence: points by format, revenue share, revenue per point, cheques/flow, average cheque, depth, ID share, revenue per capita, points per 10k residents, maturity/opening status and address/open-data proxy when available. Output `city -> observed archetype -> recommended format mix -> current-city capacity -> new-city need -> proof boundary / data gap`. Do not model all future locations as average tonars unless the user explicitly asks for a tonar-only scenario;
   - do not call a point profitable unless margin, write-offs, rent/place cost, payroll and logistics are present or the limitation is explicitly accepted;
   - separate point-format effects from city/territory effects and from maturity/opening-date effects;
   - state which action changes: assortment, seller script, loyalty capture, local promotion, point relocation/closure, SKU removal, SKU expansion, or product-tunnel hypothesis.

3. Anchor the dashboard or analysis in Formula Profit / revenue logic.
   The first block must be the tree cascade of Formula Profit. Other views are diagnostic branches, not independent charts.
   If the raw base does **not** contain reliable себестоимость / COGS, lock the analysis to `revenue_only_mode` and do not claim profit potential. In that case all growth and initiative potentials must be expressed as `delta выручки`, not `delta прибыли`.

4. In `base_analysis_mode`, normalize the source structure first.
   The skill must handle:
   - flat transaction logs (`manager`, `region`, `client`, `category`, `sku`, `month`, `quantity`, `volume`, `revenue`);
   - multi-level 1C Excel exports with hierarchy like `manager -> region -> client -> category -> sku -> months`.
   Minimum normalized grain is:
   `one row = one shipment / realization / one SKU for one client in one month`.
   Add derived fields where possible:
   `year`, `month_num`, `pack`, `active_months`, `avg_price`, `n_categories`, `n_skus`.

5. Require cross-filtering.
   Dashboard views must react to filters across period, warehouse/channel, manager, region, segment, SKU/product line, client/dealer and price type where available.

6. Map every view to a management action.
   Each chart/table must have: user, owner, process, data source, refresh frequency, reaction threshold, decision, and place to fix the next step.

7. Extract SI/SIF.
   Treat each view class as a possible SI/SIF source:
   - Formula Profit cascade -> profit-lever / factor-tree / управляемый рычаг.
   - KPI cards -> executive-control / red-zone / threshold.
   - Time series -> trend-break / seasonality / cadence.
   - Bubble/scatter GPC/RFS -> segment-policy / portfolio-priority / migration-rule.
   - Heatmaps -> territory-warehouse-bottleneck / fulfillment-gap.
   - Breakdown tables -> action-queue / accountable-owner / next-step.
   - RFM/cluster tables -> rule-per-segment / transition-criterion.
   - Cross tables -> governance-gap / handoff-gap.
   - OoS block -> lost-demand / availability-leakage / service-promise.
   - Slicers/cross-filter -> robustness-check / semantic-layer.
   - Client-type/product association -> ICP-product-fit / segment-policy / sales-playbook.
   - SKU affinity / nomenclature co-occurrence -> bundle-rule / attach-rate / cross-sell / product-architecture.
   - Regression or model feature importance -> hypothesis, not causality, unless design and data support causal reading.

7a. Diagnose revenue / gross-profit divergence automatically.
   - On the first monthly economics view, never leave revenue and gross profit as two visually correlated lines without a visible ratio. Show gross margin directly through a third percentage series, gap labels/connectors, or an immediately aligned ratio panel. Exact margin must also be available in the cross-series tooltip.
   - Trigger a diagnostic drill-down when revenue and gross profit move materially out of proportion, gross margin changes sharply, or a derived metric has an unusual fluctuation. Do not wait for a separate user request.
   - Minimum drill-down: reconcile source coverage; quantify the focal-period movement; build an exact `volume effect + margin effect = gross-profit delta` bridge; test mix shift versus within-group economics for channel, category, client, and SKU; expose the largest transaction-level entrants, exits, and margin changes tied to the dates.
   - Prefer an exact symmetric Kitagawa/Oaxaca-style decomposition for two-period rate changes. Treat channel, category, client, SKU, region, and manager as alternative overlapping lenses; never add their contributions across dimensions.
   - When the source supports it, add a multivariate or regularized explanatory model with stated grain, controls, validation window, fit, and residual. A factor decomposition is sufficient when it reconciles the movement more transparently than regression.
   - Regression coefficients, feature importance, and timing-linked transaction shifts are explanations or hypotheses, not causal proof. Mark missing price, discount, return, COGS-composition, payment, and inventory events as evidence gaps.

8. Run association and affinity diagnostics when requested or when SKU/client fit is unclear.
   Treat these as Formula Profit support views, not standalone analytics.

   **Client type -> nomenclature / product group**
   - Unit of analysis: order, shipment, realization document, customer-period, or deal. State the unit before modeling.
   - Inputs: client type / segment, region, channel, manager, cohort, order size, product group, SKU, amount, margin if available.
   - Outputs: association table, lift / odds ratio, confidence / sample-size flags, and management implication.
   - Acceptable methods: cross-tabs with lift, chi-square / Cramer's V, logistic or multinomial regression, tree-based feature importance, regularized models for sparse data.
   - Required controls where available: period/cohort, channel, region, manager, order size, old-tail vs new-flow, and product group.
   - Do not call a relation "устойчивая" unless it persists across at least two time windows, has enough sample size, and remains directionally stable after basic controls.

   **Nomenclature affinity / сочетанность**
   - Unit of basket: cheque/order, shipment document, realization document, deal, or client-period. Pick one and name it.
   - Use product group first; SKU-level analysis is allowed only after cleaning low-volume codes.
   - Minimum metrics: support, confidence A->B, confidence B->A, lift, co-occurrence count, distinct basket count.
   - The common quick metric `both / either` is allowed as "сочетанность", but never alone; high frequency categories can inflate it.
   - Filter out weak pairs by minimum baskets, minimum co-occurrence, and business relevance.
   - For old datasets, split new flow and old tail; otherwise project bundles from old cohorts can masquerade as current cross-sell.

9. Apply account-based segmentation families when the source base supports them.
   There are three layers of segmentation work:

   **A. Segmenting clients / accounts**
   - `KML` — competition / monopolization / LTV family for the question `кому продавать`.
   - `BNT` — average check / systemness / cycle family for the question `кому продавать`.
   - `SPL` — shipment regularity / payment discipline / LTV family for the question `как продавать`, when logistics and payment behavior are critical.
   - `SL` is not a standalone canonical family. It was first used in the Ipatovo lineage only as a project-specific fallback for `SPL` when payment-discipline data (`P`) was unavailable. Do not calculate or publish pure `SL` in place of `SPL` unless the owner explicitly accepts that fallback for the current project.

   **B. Segmenting categories inside an account**
   - `DSL` — category penetration / spread / LTV family for the question `что продавать`.
   - `PSC` — price / systemness / slots family for the question `как продавать` or `как устроено транзакционное поведение внутри категории`.

   **C. Mapping combinations into verbal archetypes**
   - Build named cells such as top-priority / high-yield / stable / open-small / hard-competitive / unpredictable only if the business rules are explicit.
   - Never invent a category label without showing the underlying combination rules.

   Minimum contract for any segmentation family:
   - define each letter;
   - state whether thresholds are fixed or percentile-based;
   - show the grain (`client`, `client-category`, `client-period`, `basket`, `shipment`);
   - show sample exclusions;
   - show management use.

10. In `base_analysis_mode`, produce the standard analysis packet.
    Minimum output families:
   - `break_clients`
   - `break_categories`
   - `break_skus`
   - `break_managers`
   - `matrix_region_category`
   - `matrix_region_segment`
   - `region x DSL / KML / BNT / PSC / SL` where relevant
   - `growth candidates / недопроданный ассортимент`
   - `data quality exceptions` for region / manager / client dictionaries
   - `4-6 stories from data`

    Stories should follow reusable templates:
   - concentration risk;
   - one category grows while the rest decline;
   - manager dependency on 1-2 accounts;
   - model region with better segment mix;
   - SKU dependence on one client;
   - mismatch between formal business identity and actual revenue structure.

10a. In reference-parity dashboard mode, produce the standard interactive dashboard packet.
    Minimum output families:
   - `filters_and_scope`: period, channel, region, manager, client/account, segment, category, SKU, warehouse/point where fields exist;
   - `management_top`: KPI cards, reconciliation status, data period, source limitations;
   - `formula_profit`: revenue, discount, COGS, gross profit, gross margin, coverage caveats;
   - `monthly_economics`: revenue, gross profit, gross margin, checks/documents/realizations, clients, average document value, quantity, discount;
   - `breaks`: channel, region, manager, warehouse, client/account, category, SKU, contract;
   - `client_behavior`: RFM-like account table, repeat shipments, cohorts by first realization, retained / lost / reactivated accounts where source grain supports it;
   - `segment_families`: BNT, DSL, PSC, KML/SPL only when required source fields exist, with explicit missing-source rows otherwise;
   - `product_behavior`: SKU/category affinity, client-type/product association, concentration and long-tail diagnostics;
   - `diagnostics`: revenue-vs-gross-profit divergence, mix/economics decomposition, transaction events, data-quality exceptions;
   - `planning`: forecast / gap plan / scenario only when history and business target are available; otherwise an explicit no-data placeholder;
   - `source_and_lineage`: source files, grain, excluded rows, formula coverage, refresh and join gaps.

    The B2B version should mirror the reference's product quality and interaction pattern, not its retail-specific semantics. Retail-only blocks such as phone/Roistat transfers, cashier employees, and store-hour heatmaps become B2B analogues only when the source has matching identifiers and operational meaning.

10b. In HoReCa/Retail dashboard mode, produce the standard point-analysis packet.
    Minimum output families:
   - `filters_and_scope`: period, point/store, city, format, category, SKU, identified-client mode, first-purchase cohort where fields exist;
   - `network_top`: revenue, cheques, average cheque, identified cheque share, identified revenue share, active points, source reconciliation;
   - `network_dynamics`: monthly revenue, cheques, average cheque, active points, identified / unidentified split;
   - `point_breaks`: top/bottom points, city, format, seller/cashier, point maturity/status if available;
   - `point_formula_tree`: point revenue drivers by cheques, average cheque, identified clients, LTV, frequency, item price, basket depth;
   - `loyalty_behavior`: RFM, repeat funnel, cohort retention, clients by purchase number, multi-point clients;
   - `basket_and_sku`: category/SKU contribution, SKU/category monetization map, ABC/XYZ, basket depth, co-occurrence/affinity;
   - `consumer_clusters`: clusters only if variables, sample size, and source limitations are shown;
   - `action_register`: local tests/actions with status and effect, or an explicit missing-source block;
   - `source_and_lineage`: source files, grain, period, excluded rows, join logic, dictionary gaps, and unavailable economics.

    RFM retail tactic contract:
   - Collapse raw RFM cells into a manageable number of action segments; do not create a separate campaign for every RFM score unless the operator can execute and measure it.
   - For each segment state: management role, target behavior, tactic, expected lift, cost of contact/bonus, margin dependency, control group, measurement window, and stop-loss.
   - RFM migration economics must include both incremental frequency/retention and potential average-cheque or basket-quality decay; if repeated purchases become cheaper, calculate the equilibrium point and prescribe a countermeasure such as bundle, threshold, premium add-on, high-monetization category trigger, or next-best-product recommendation.
   - Related-product / bundle / threshold / personal-recommendation outputs must include an NBA table or proxy-NBA paragraph. Required fields: target segment, prior signal, equilibrium gap, candidate action, proof source, expected cheque/basket effect, margin/cost gate, control-group KPI, and data gap if personalization keys are absent.
   - Repeat / retention / RFM migration outputs must state whether the equilibrium is `revenue-only` or `profit-level`. Profit-level equilibrium requires margin, bonus/discount cost, communication cost, and operational cost; absent fields become explicit data gaps.
   - For `best / champions / лучшие`, prefer habit protection, assortment/basket expansion, premium or bundle scenarios, early access, and NPD feedback; do not default to discounting customers who already buy.
   - For `normal / potential / promising`, focus on the next repeat purchase and movement into regularity.
   - For `sleeping / at-risk`, act quickly with a specific return occasion and last-category trigger.
   - For `lost / churn`, use low-cost win-back first and suppress expensive campaigns unless prior value justifies them.
   - For `new`, optimize second-purchase conversion and preference capture before assigning mature LTV meaning.
   - If the user asks what predicts segment membership, separate tautological predictors (recency, frequency, monetary, repeat, avg cheque when used in RFM definition) from operational predictors (point, format, city, seller/cashier, category, identity capture, season, promo, assortment breadth/depth). Use regression or controlled stratification only as directional evidence unless causal design exists.
   - When reporting that RFM quality is associated with `flow` or `point context`, expand it into explicit factor models: flow habit / потоковая привычка, territorial density / территориальная плотность, identity capture quality / качество поглощения в базу, format scenario / форматный сценарий, high-ticket low-frequency behavior / дорогой но нерегулярный чек, and peak unidentified flow / пиковый неопознанный поток. Do not leave `context` as an opaque explanation.
   - RFM factor claims must pass a heteroskedasticity / неодинаковый-разброс check before becoming management conclusions. Do not write `strong RFM base emerges where X` as a homogeneous law unless dispersion is stable across formats, territories, point sizes, seasons, and identification levels. Check at least: `format × flow`, `city/territory × format`, `ID share × flow`, `average cheque × frequency`, `basket depth × SKU/category mix`, and `month × format`. If dispersion differs materially, make the variance itself the conclusion: name stable factories, volatile point classes, outliers, and the different operating models they imply.
   - When formats differ materially, run a mono-format / cross-format client route check. This applies to explicit store formats and hidden format differences such as center vs residential salons, mall vs street points, premium vs convenience points, own vs partner retail, or counter vs delivery. Compare `mono-format clients` and `cross-format clients` by client count, revenue, frequency, average cheque, basket depth, LTV, RFM mix, SKU/category mix, purchase intervals, and seasonality. If the dashboard has only aggregate format-combo rows, use them as a first signal and register the missing `client_id -> format -> point -> SKU/category -> interval` bridge as a BI/CRM data gap. Treat strong cross-format behavior as possible SI: the client may be using the network as a system, not merely choosing one point.
   - For cohort blocks, always state whether the cohort is based on true first event, loyalty-program join date, registration date, or first visible event in the extract. If true first event or loyalty-join date is unavailable, disclose left-censoring and build a cohort anomaly table by cohort month, activity month, month-since, revenue drop versus previous month, retention versus month 0, comparison with same-age cohort median, and required drill-down.
   - For point comparison blocks, produce a peer-diagnostic table rather than only a top/bottom list: point, peer-set definition, underperforming factor, outperforming factor, nearest benchmark point(s), growth lever, test action, metric, and data gap. Typical point models: high-flow low-identity, high-ticket low-flow, high-flow low-monetization, strong-repeat low-cheque, high-cheque low-RFM, and chronic weak point.
   - For point bottleneck blocks, produce a point card that decomposes the symptom through Formula Profit: `point -> symptom -> peer deviation -> cheque / LTV / RFM / SKU decomposition -> likely mechanism -> lever -> experiment KPI -> missing data`. Mandatory checks: category/SKU mix, basket depth, item price, identity capture, RFM structure, seller/cashier variance, and point maturity. Use customer clusters only when the source has a reliable `point x customer cluster` bridge; otherwise mark it as a data gap.
   - For anomaly blocks, perform cross-chart stitching whenever the source contains compatible keys. Minimum useful joins: time, point/store, format, city/territory, seller/cashier, category, SKU, client stage, RFM segment, cohort, channel, and promotion where available. The report must say which mechanisms became stronger, which became weaker, and which remained untestable because fields were missing. For cohort anomalies specifically, produce `cohort / month -> anomaly -> synchronous network context -> client stages -> category/SKU context -> point/format context -> strengthened explanation -> weakened explanation -> bridge status`. In dashboard-only mode, bridge status may be `нет в готовом дашборде`; in raw-base mode, bridge status must be `построено агентом`, `ключей нет в сырой базе`, or `доступ к сырой базе отсутствует`.
   - For loyalty economics blocks, produce `identified cheque base -> unidentified cheque base -> identified average cheque -> unidentified average cheque -> observed gap -> conversion scenarios -> margin/breakeven threshold -> missing fields`. If margin, bonus cost, discount cost, communication cost, IT cost, and cashier execution cost are absent, label the output as `верхняя граница выручки / не прогноз прибыли`.
   - For final executive writeups, include a bottom-up Formula Profit ledger near the end before data gaps: `source chart(s) -> bottom-up metric -> formula/value -> management reading -> proof boundary`. A row is valid only if it says what can be recalculated, how much it is worth or how it bounds the decision, what management action changes, and why it is or is not profit.
  - For final executive writeups, include a bottom issue tree plus hypothesis / data-gap register after the bottom-up ledger when roadmap decisions depend on dashboard findings. Required issue-tree columns: `Уровень 1`, `Уровень 2`, `Уровень 3`, `Уровень 4`, `Тип узла`, `Evidence / что уже видно`, `Управленческое следствие`. Required hypothesis columns: `ID`, `гипотеза / версия`, `откуда возникла`, `статус`, `что усиливает`, `что ослабляет`, `следующий тест / решение`. Required data-gap columns: `ID`, `дефицит данных`, `почему важен управленчески`, `что должен дать источник`, `куда влияет`. A report is incomplete if active facts, hypotheses, or data gaps appear only in the body and are absent from this bottom layer.
   - For interpretation-heavy claims, add an unpacking block: `phrase -> concrete meaning -> observable signs -> what to ask client -> pilot action -> metric`. This is mandatory when the phrase names a mechanism rather than a directly measured value.
   - For share/count charts, add a guardrail sentence: `главный сигнал — доля / абсолют; второй показатель — масштаб / контекст`. Do not write a conclusion from `identified cheques`, `revenue share`, `category share`, `client share`, or similar without naming whether the metric is relative or absolute.
   - For large-contribution claims, add a base-normalization sentence: `это не только / только эффект размера базы, потому что ...`. If the conclusion disappears after normalization, downgrade it to scale effect.
   - For dilemma claims, add a discrimination sentence: `версия A усилилась / версия B ослабла / обе остаются равными`, with the checked evidence named. Do not write only `возможны две версии` unless no distinguishing cut exists.
   - For surprising-direction claims, add an intuition-baseline sentence: `это контринтуитивно для модели X, но логично для модели Y`; then state whether the data proves Y or only raises it as a hypothesis.
   - For client-question blocks, add a BPM-SI routing table: `гипотеза / SI-кандидат -> что запросить у клиента -> что изменится в выводе / слайде / roadmap / BPM-route`. If the project has a `BPM Storyline-Storyboard` or equivalent SI ledger, update it or record a no-op reason.
   - For SKU/category scenario claims, run cross-BPM SI upgrade before recommending action: BPM-4 can prove monetization and point flow; BPM-1A proves consumer occasion; BPM-3 or mystery-shopper proves shelf/choice/seller experience; BPM-7B proves product route and NPD fit; BPM-10/11 proves CRM/BI triggerability. Missing layers must go to the bottom hypothesis/data-gap register.
   - For cross-check instructions, add a performed-check table or paragraph in the same section: `разрез проверен -> что найдено -> относительный/абсолютный статус -> вердикт -> недостающий bridge`. The response is incomplete if it only says the team should check.
   - For sentences beginning with `если`, ask whether the condition can be checked now. If yes, replace with `проверено: ...`; if partly, write `проверено частично`; if no, write the missing key. Prefer `версия -> проверка -> вердикт` tables over long conditional prose.
   - For pilot/action recommendations, include a concrete starting shortlist whenever source data supports it: named points, sellers/cashiers, SKUs, clients, regions, categories, or segments; selection reason; absolute value; relative rate/share; denominator/base; and first diagnostic action.
   - For any instruction-like phrase inside the analysis such as `найти`, `проверить`, `сравнить`, or `выбрать`, first test whether the report source already contains the grain needed to execute it. If yes, replace the instruction with an executed entity list and verdict. Keep the instruction only for missing-source cases and route that missing source to the bottom data-gap register.
   - For mechanism-heavy claims, add a proof-boundary block: `measured symptom -> inferred mechanism -> supporting BPM/source traces -> what this proves -> what this does not prove -> evidence needed to upgrade to fact`.
   - For hypothesis rows, do not write only `what to ask client`; write `how to verify`: source, calculation or cross-check, confirming pattern, weakening pattern, and management consequence.
   - For RFM/LTV/cohort caveats, compute the measurable blind zone first: `unidentified checks/revenue/avg cheque -> peak period -> top entities -> what RFM misses -> missing bridge`.

    A standalone HTML dashboard is acceptable when DataLens is not the target, but it must be self-contained, filterable, and machine-inspectable: source JSON or tables must remain extractable, section headings must be visible, and data gaps must be rendered inside the artifact.

11. Route to BPM Storyline-Storyboard.
   If a dashboard view creates a hypothesis, storyline move, slide candidate, knowledge deficit, data task, SI/SIF candidate, or BPV action, update the project BPM Storyline-Storyboard or explicitly record a no-op reason.

11a. Preserve the annotation loop.
   When Ilya comments on a generated BPM-4 dashboard document or annotatable artifact, the response is incomplete until the artifact itself is updated. Apply the comment to the canonical editable source first, regenerate the annotatable DOCX/PDF if it exists, and verify both. Treat the chat answer as a summary of the writeback, not as the primary destination of the correction.

12. Hand off DataLens implementation when needed.
   If the target is Yandex DataLens, keep this skill responsible for distribution semantics, Formula Profit, SKU/client grain, OoS, association logic, and management meaning. Use `bpm4-datalens-dashboard` for SQL-view/dataset execution, chart layout, click-to-filter, scatter stabilization, save/publish cycle, browser QA, and post-publish delta.

   Before handoff, provide:
   - agreed Formula Profit and reporting unit rules;
   - fact grain: order line, shipment line, realization document, client-period, or other;
   - client / dealer / product / warehouse keys and known dictionary gaps;
   - control slice for year, currency, business direction, and key totals;
   - list of required diagnostic views and their management actions.

13. If the deliverable is a board / director packet, structure the executive output explicitly.
   Default executive structure for a flat-base B2B review:
   - cover + key KPIs + 5 strongest findings;
   - geography + categories;
   - four segmentation families in compact form;
   - core clients + region/segment matrices;
   - top SKU + 3 strongest SKU stories;
   - managers + concentration observations;
   - quick wins;
   - mid-term initiatives;
   - long-term initiatives;
   - first 30 days / priority stack.

   Initiatives must be written as:
   `verb + target cohort + expected delta + owner + metric`.
   No generic nouns like `pilot`, `optimization`, `improvement` without object and metric.

14. Decide downstream route.
   - BPV if the dashboard becomes a client management rhythm, operating meeting, sales action queue, or analytics factory.
   - 1-ка if the dashboard yields a training exercise, rubric, or gate.
   - 2-ка if it yields a product-vitrine thesis, case, or content candidate.
   - 5-ка if the BPM/BPV standard needs correction.
   - 8-ка if it yields reusable knowledge or a SI/METH candidate.

## Segment Family Contract (Ipatovo-aware)

Use this contract whenever DSL/KML/BNT/SPL/PSC/SL appear.

### DSL

- Primary role: `что продавать` inside the account / category penetration logic.
- Prefer slide-native meaning first:
  - `D` = глубина погружения в ассортимент;
  - `S` = распределение / spread ассортимента по категориям;
  - `L` = LTV.
- If a text spec proposes an alternative decoding, preserve it only as `text-adapted interpretation`, not as a silent replacement.

### KML

- Primary role: `кому продавать` via account attractiveness and competitive position.
- Typical letters:
  - `K` = уровень конкуренции;
  - `M` = уровень монополизации / concentration of supplier shares;
  - `L` = LTV.

### BNT

- Primary role: `кому продавать` via transaction attractiveness.
- Typical letters:
  - `B` = средний чек;
  - `N` = системность заказов;
  - `T` = цикл закупок / time between purchases.

### SPL

- Primary role: `как продавать` when shipment rhythm and payment discipline matter.
- Typical letters:
  - `S` = системность отгрузок;
  - `P` = платёжная дисциплина;
  - `L` = LTV.

### PSC

- Primary role: transaction-behavior segmentation / `как продавать`.
- Prefer slide-native meaning first:
  - `P` = средняя стоимость позиции;
  - `S` = системность заказов;
  - `C` = slots / объём потребления / depth × repeat behavior.

### SL

- Not a standalone canonical segmentation family.
- Ipatovo lineage: project-specific `SPL` fallback with the unavailable payment-discipline dimension removed.
- Default rule outside that accepted exception: do not build pure `SL`; show `SPL — не рассчитано` and the missing payment-discipline source instead.
- If an owner explicitly authorizes the fallback, label it `project-specific SPL fallback`, preserve `S` and `L` definitions, and never present it as a universal BPM-4 canon.

## Base Analysis Guardrails

- Do not infer `маржинальность`, `валовая прибыль`, `unit economics`, or `profit pool` from a base that only contains revenue/volume/quantity.
- If cost data is absent, all segment attractiveness and growth estimates stay in revenue terms.
- Exclude very weak tails from top-lists or mark them as `длинный хвост`, not as strategic priorities.
- Region and manager fields are not trusted blindly; missing or technical values must go to a data-quality block before client-facing conclusions.
- If thresholds are percentile-based, say so. If thresholds are fixed, justify them.
- If a segment family is adapted from a specific project lineage, label it `project-specific reusable pattern`, not `universal BPM-4 canon`.
- Do not substitute `SL` for unavailable `SPL` by default. Missing payment events are a source gap, not permission to canonize a two-dimensional fallback.

## Output Family Contract (validated on Ipatovo artifact set)

When the user asks to `разбери базу`, the skill should not default to one monolithic PDF.
Prefer a **packet of specialized outputs**. For the Ipatovo lineage, the validated output family is:

1. `otchet_prodazhi_*`
   - Role: general sales / revenue / volume / pricing / concentration review.
   - Typical size: A4 portrait.
   - Typical length: 10-15 pages.
   - Must include:
     - cover page with 5-7 top KPIs;
     - director summary with strongest pain points;
     - dynamic trend pages;
     - concentration / lost clients / price / category stories;
     - prioritized actions.

2. `otchet_segmentaciya_*`
   - Role: account-based segmentation methodology + segment interpretation.
   - Typical size: A4 portrait.
   - Typical length: 8-15 pages.
   - Must include:
     - methodology caveat page;
     - table of segment families and their managerial role;
     - top segment tables with revenue/client shares;
     - interpretation blocks written in management language;
     - explicit note on unavailable segment families (for example, no KML if competitor-wallet data is absent).

3. `otchet_geografia_*`
   - Role: geography x category / geography data quality / known vs unknown region analysis.
   - Typical size: A3 landscape when large matrices are central.
   - Must include:
     - region coverage caveat;
     - known-region share vs unknown-region share;
     - at least one region x category matrix;
     - at least one structural interpretation page;
     - explicit statement of what cannot be concluded due to missing geo dictionary.

4. `otchet_geo_x_segments_*`
   - Role: region x segment overlays.
   - Typical size: A4 landscape or dense A4 packet.
   - Must include:
     - one intro page with methodology and strongest geo-segment stories;
     - separate intersections for key segment families;
     - column/row reading guidance;
     - explicit warning against over-reading the `Неизвестно` region bucket.

5. `otchet_brejki_*`
   - Role: standardized break packet for clients / categories / SKU.
   - Typical size: A3 landscape when wide tables with many metrics are used.
   - Must include:
     - metric legend with formula meaning;
     - one page per analytical unit family;
     - bars/heat inside cells only as reading support, not as substitute for values;
     - full-list artifact references if the PDF shows only top-N.

The exact filenames may differ, but the skill should preserve the **family idea**:
`sales review`, `segmentation review`, `geography review`, `geo x segments review`, `break packet`.

## PDF and Layout Expectations

- Use **A4 portrait** for narrative reports and methodology-heavy packets.
- Use **A3 landscape** for wide break tables and large region/category matrices.
- Put the project name, report role, period, and preparation provenance in the header.
- The first page of each PDF must explain:
  - what this packet answers;
  - what time window is used;
  - how many clients / rows / revenue are in scope;
  - which data limitations remain active.
- If a report is table-heavy, include a metric legend before the first dense table.
- If a report is matrix-heavy, include reading instructions like `читается по строкам` / `читается по столбцам`.

## Reporting Style Contract

- Report titles should be **findings-first** where possible, not neutral placeholders.
- Under each major table or matrix, provide short narrative interpretation:
  - what is structurally important;
  - what is risky;
  - what is actionable;
  - what still needs source clarification.
- Use Russian management language, no emoji, no decorative jargon.
- Distinguish rigorously between:
  - observed fact,
  - plausible explanation,
  - hypothesis,
  - unavailable conclusion.
- If a conclusion depends on incomplete dictionaries (region, manager, competitor wallet, payment discipline), state that limitation in the page itself, not only once in an appendix.

## Data-Limitation Disclosure Rules

These PDFs show that limitation disclosure is not optional; it is part of the output grammar.

Always disclose explicitly when:

- geography is partially inferred from legal names;
- a large `Неизвестно` bucket exists;
- KML cannot be built due to no competitor sales / wallet data;
- SPL is reduced to `S·L` due to no payment-discipline data;
- profitability / margin analysis is omitted because COGS is not verified;
- top-N pages are excerpts from fuller CSV artifacts.

## Mandatory Story Blocks

In artifact packets similar to Ipatovo, the skill should attempt to generate short story blocks such as:

- `что видно уже сейчас`;
- `ключевое`;
- `интерпретация`;
- `что делать в первую очередь`;
- `практическое применение`;
- `оговорка по данным`.

These are not decorative sections; they are required translation layers from data to management use.

## Artifact Bundle Contract

For mature `base_analysis_mode`, the output should be treated as a bundle, not a single table dump:

- normalized base (`sales_flat` or equivalent);
- segmentation table by client;
- breaks;
- matrices;
- growth candidates;
- thematic PDF packet family;
- optional executive summary packet.

If only part of the bundle is produced, the skill must state which layer is missing:
`no_pdf_packet`, `no_growth_packet`, `no_region_matrix`, `no_segment_overlay`, `no_executive_bundle`.

## Completion Checks

- Scope lock is explicit: B2B distribution / regular shipments.
- Operating mode is explicit: `dashboard_mode`, `base_analysis_mode`, or `hybrid_mode`.
- If a reference dashboard from Natalia/project operators exists, parity checklist is explicit and every reference block is either implemented, adapted to B2B semantics, or shown as `не рассчитано / требуется источник` with concrete missing fields.
- If a reference dashboard from Natalia/project operators exists, visual grammar is checked separately from metric coverage: left rail, vertical BI reading flow, KPI top, numbered sections, chart/table density, and visible unavailable blocks.
- A reference-dashboard request is not completed by a readiness-only artifact unless the user explicitly asked for readiness-only output.
- HoReCa/Retail sources trigger the point-analysis variant when point/store, cheque, loyalty, SKU/category, seller/cashier, or format fields exist.
- HoReCa/Retail dashboards include network top, point breaks, point Formula Profit tree, loyalty behaviour, basket/SKU blocks, consumer clusters where supportable, action register or explicit missing-source block, and source/lineage.
- Cheques without client identity are included in revenue/average-cheque calculations but excluded from repeat, LTV, RFM and cohort claims unless a documented identity bridge exists.
- Point profitability is not claimed unless margin, write-offs, rent/place cost, payroll and logistics are present or the limitation is visible.
- Standalone HTML dashboards preserve extractable data and visible data-gap blocks; screenshot-only or textless artifacts are not treated as reusable dashboard evidence.
- Analytical atlas packages are inspected as bundles: manifest, chart map, chart-ready data files, QA/render status, preview, sections, source periods, source perimeters and limitations are registered before conclusions. Chart-level replay, raw-to-chart pipeline reproducibility and metric proof are stated separately.
- HoReCa/Retail point-opening plans split target growth into current-network run-rate, existing-point optimization ceiling, and residual new-point revenue; required CAGR is calculated; format mix constraints such as `80/20 в пользу тонаров` are applied at portfolio level and then adapted by city/territory archetype rather than pasted uniformly onto every city.
- Formula Profit cascade is first.
- The first revenue / gross-profit trend exposes gross margin directly; material divergence triggers a reconciled volume × margin bridge and transaction-backed factor drill-down.
- `revenue_only_mode` is declared when COGS/margin data is absent.
- Cross-filtering is specified or implemented.
- OoS is handled where distribution data supports it.
- Client-type/product association is modeled with stated unit of analysis, controls, sample thresholds, and "correlation not causation" guardrail.
- SKU/nomenclature affinity includes support, confidence, lift, and a management action; `both/either` alone is not enough.
- New flow vs old tail is separated when order and realization dates differ materially.
- Missing product/client dictionary codes are flagged before client-facing segmentation claims.
- Segment families are labeled with their source status: `slide-native`, `text-adapted`, or `agent-inferred`.
- For DSL/KML/BNT/SPL/PSC, each letter is decoded and management use is stated. If an owner-authorized Ipatovo-style `SL` fallback is present, its exception status and missing `P` source are visible.
- In `base_analysis_mode`, standard breaks and region/segment matrices are produced or explicitly waived with a no-op reason.
- Growth candidates / недопроданный ассортимент logic is stated, not implied.
- Executive-summary structure is explicit when the ask is board-ready.
- Output family is explicit: sales / segmentation / geography / geo x segments / breaks, or an explicit reduced subset with reasons.
- PDF page format is chosen intentionally: A4 portrait for narrative, A3 landscape for wide tables/matrices.
- Every PDF has a visible data-limitation block where relevant.
- Table-heavy packets include a metric legend; matrix-heavy packets include reading instructions.
- Every view has a management action and owner.
- If DataLens is the target, `bpm4-datalens-dashboard` is applied or an explicit no-op reason is recorded.
- SI/SIF candidates are named or rejected with a no-op reason.
- BPM Storyline-Storyboard route is updated or no-op is recorded.
- Active hypotheses and data deficits surfaced in chart prose are collected in a bottom register with IDs, source charts, status, strengthening/weakening signals, next test, and decision impact.
- Any body-text instruction to find/check/compare named analytical entities is executed immediately when the source has the grain; otherwise the exact missing key is recorded as a data gap.
- Any recommendation to build bottleneck cards, entity shortlists, version-check tables, peer-sets, or diagnostic matrices is executed immediately when source grain exists; otherwise the exact missing fields are recorded near the recommendation and in the bottom data-gap register.
- Analytical meta-statements such as `диспетчер причин`, `матрица решения`, `роутер причин`, or `не перечень, а механизм` are embodied as the actual table/router/matrix in the report when the typology and available data allow it.
- Multi-point / cross-format client layers are quantified before being routed to data gaps: client share, revenue share, frequency, average cheque, depth, LTV, and the remaining client-route bridge are visible.
- Consumer cluster layers are converted into explicit scenario/action matrices when available: measured profile, product scenario, CRM/loyalty trigger, NBA or offer logic, NPD/assortment hypothesis, BPM-1A/BPM-3 validation, and proof boundary.
- Syndicated cross-chart ideas are backed by syndicated figures from the available cuts, and the report separates numerically proven mechanisms from consumer motives requiring BPM-1A/BPM-3 validation.
- Transferable formulas / donor practices named in the report are extracted as factor-analysis packets with proved factors, hypothesized mechanisms, transferable/non-transferable elements, first peer tests, KPIs, and missing evidence.
- SKU/category development recommendations are checked through cross-BPM SI evidence gates before becoming actions; unsupported layers are registered as hypotheses or data gaps.
- Consumer occasions, visit missions, motives, and other custdev-checkable explanations are not inferred as facts from BPM-4 alone; they are either supported by BPM-1A/BPM-3/observation/mystery evidence or explicitly labeled as hypotheses with the required check.
- Annotatable DOCX/PDF reports that interpret dashboard charts include compact screenshots/crops of the relevant graphs near the corresponding conclusions, or an explicit `скриншот графика недоступен` source-access reason.
- Unusual point/segment opportunities, including low-flow/high-ticket cases, are decomposed into concrete drivers before action: depth, item price, category/SKU mix, ID share, repeat/RFM, format/city, and base-size reliability.
- For HoReCa/Retail high-ticket low-flow points with known addresses, the report includes an address/open-data proxy layer: density, access, transport, traffic anchors, competitors, map reviews/rating, visibility, parking and route convenience. The report states which conclusions are proven by internal BPM-4 data, which are only geo/open-data proxies, and which require BPM-3, field observation, customer evidence, or margin data.
- Cross-BPM gates use existing BPM evidence before creating new requests; outputs state what was reused, which ongoing/pending BPM program was enriched with exact questions/fields/checks, what was enriched back into BPM, and which exact source/field gap remains.
- New annotation-derived heuristics trigger a full replay consistency pass across local conclusions, heuristic list, hypothesis/data-gap registers, cross-section matrix and coverage ledger.
- New raw/mart/source ingests trigger caveat retirement: update the original conclusions artifact, run newly enabled checks, and rewrite each old data gap as `закрыто / сужено / заменено / остается открытым` with exact source rights.
- Multi-delta updates include a change-delta heuristic audit: every material update/addition/expansion/cancellation/replacement/status change is classified and checked against the active heuristic set, with strengthened/weakened/superseded conclusions and remaining exact gaps.
- Package manifests are registered as lineage evidence and reconciled against physical files; missing expected tables, dictionaries, QA markdown, and CSV QA artifacts become explicit recovery gaps, not silent assumptions.
- Candidate dimension tables are inspected as mapping/normalization evidence, not master data; duplicate raw codes, category conflicts, nulls, and approval gaps are visible before SKU/point conclusions.
- POS/point candidate dictionaries are inspected as raw alias/address/ID evidence, not as approved point masters; missing cross-system mapping, coordinates, address normalization, opening status and approval remain explicit gaps.
- Dashboard construction logs produce a visible chart-to-source passport and named recovery gaps: every material chart block is mapped to JSON view/source file/formula/filter semantics/derived asset, and missing QA CSV, payload, source JSON, metric dictionary or build script is listed before claiming dashboard reproducibility.
- Profit-dependent findings without verified margin, COGS, write-offs, fixed costs, bonus/discount/contact cost, payroll, rent/place cost and logistics are recorded in the bottom data-gap register as `profit layer / profit bridge`; the report labels related initiatives as `выручка / proxy`, not profit.
- Divergence-under-growth findings include a regression / factor matrix with outcome, candidate factors, controls, current evidence, strengthened/weakened versions and missing bridge; raw-base mode runs the model, dashboard-only mode records the missing regression bridge as a data gap.
- Segment migration upside includes a kinship / transition matrix before economics: likely adjacent moves, unlikely/directly-too-expensive moves, NBA/offer, plausible conversion proxy, cheque/margin degradation risk, and missing `segment_t -> segment_t+1` bridge.
- Every action-bearing slice has a visible peer-set registry/table in the report, or a named missing bridge; this applies to points, formats, territories, sellers, SKU/categories, RFM/clusters, cohorts, channels and campaigns.
- Dense annotation sets end with a visible closure ledger: what changed in-place, what entered issue tree / hypothesis / data gaps, what changed roadmap / data request, what changed the skill, and what remains unresolved.

## Eval Cases

Use these regression cases after material edits to this skill.

| Case ID | Prompt | Expected route | Forbidden behavior | Pass condition |
|---|---|---|---|---|
| `retail-good-trigger-2026-09-01` | `Собери управленческий дашборд по точкам собственной розницы: чеки, клиенты лояльности, SKU, продавцы, форматы` | This skill, `HoReCa/Retail dashboard mode` | Route to generic charting only; use B2B dealer segmentation as-is; omit loyalty identity caveat | Output includes network top, point breaks, point formula tree, RFM/cohorts/repeat, basket/SKU blocks, source gaps, and management actions |
| `retail-profitability-gap-2026-09-01` | `Назови прибыльные и убыточные магазины по кассовым чекам и программе лояльности` | This skill with profitability limitation | Claim profit from revenue-only or cheque-only source | Response says profitability requires margin/COGS, write-offs, rent/place cost, payroll and logistics; provides revenue/client diagnostics instead |
| `b2b-adjacent-guard-2026-09-01` | `Разбери отгрузки B2B-дилеров по регионам, складам, клиентам и SKU` | This skill, B2B distribution mode | Force retail point/RFM consumer blocks where no retail identity exists | Output keeps dealer/client segmentation, shipment cohorts, SKU affinity and Formula Profit semantics |
| `datalens-handoff-2026-09-01` | `Перенеси утвержденный HoReCa/Retail BPM-4 дашборд в Yandex DataLens` | This skill for semantic handoff, then `bpm4-datalens-dashboard` for implementation | Let DataLens skill define business Formula Profit alone | Handoff names grain, point/client/SKU keys, metrics, filters, source gaps and required chart families before implementation |

## Quick Diagnostic Scripts

When adapting a user's pairwise "сочетанность" script, preserve the intent but harden the method:

```python
# Required columns after renaming:
# basket_id = cheque/order/document/deal/client-period
# item = SKU or product group
base = df.dropna(subset=["basket_id", "item"]).drop_duplicates(["basket_id", "item"])
baskets = base.groupby("basket_id")["item"].apply(set)
item_baskets = base.groupby("item")["basket_id"].nunique()

# For each pair A,B calculate:
# support_count = baskets containing A and B
# support = support_count / total_baskets
# confidence_a_to_b = support_count / baskets_with_A
# confidence_b_to_a = support_count / baskets_with_B
# lift = support / (share_A * share_B)
# jaccard / sochetannost = support_count / baskets_with_A_or_B
```

For client-type/product association, start with a cross-tab and only then model:

```text
client_type x product_group:
count_orders, amount, margin, share_in_client_type, share_in_product_group,
lift_vs_total, odds_ratio_or_model_effect, sample_flag, management_action
```

## Structured Analytical Artifact Gate

Client/product/region segmentations, association matrices, metric trees, dashboard dimensions, evidence/claim tables, analytical visuals, and Storyline-Storyboard deltas inherit the global contract in `~/.codex/AGENTS.md`. State unit of analysis, universe, grain, dimension dictionary, numerator/denominator, filter semantics, multi-label boundary, residual/unclassified rows, physical source, and management decision. Do not label overlapping commercial cuts as strictly MECE. Frappe is nonblocking; the calculation/data source and Formula Profit canon govern.
