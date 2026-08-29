---
name: bpm4-b2b-dashboard-industrial-distribution
description: "Use when working with BPM-4 B2B industrial distribution or distribution-like SKU dashboards: Formula Profit, client/dealer segmentation, shipment cohorts, SKU affinity, client-type/product associations, OoS, cross-filtered BI/DataLens views, SI/SIF extraction, and Storyline-Storyboard routing."
metadata:
  version: "0.2.3"
  status: active
  line: BPM-4 / industrial distribution dashboard
  owner: Ilya
  supports_bpm:
    primary: [BPM-4]
    required_secondary: [BPM-10, BPM-11]
    optional_secondary: [BPM-2, BPM-3, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9]
  can_consume: [sales / shipment / order-line datasets, Formula Profit inputs, CRM / ERP / BI exports, project BPM Storyline-Storyboard, Матрица BPM — SI, flat B2B transaction base, hierarchical 1C Excel exports, client-region dictionaries, manager dictionaries, regional deep-dive slices, packaged external methodology/specs]
  can_produce: [BPM-4 dashboard view spec, DataLens-ready implementation handoff, Formula Profit decomposition, segment / SKU / cohort hypotheses, SI / SIF candidates, Storyline-Storyboard writeback proposal, base-analysis packet, client / category / SKU / manager breaks, region-segment matrices, account-based segmentation families, growth candidates, executive summary structure, no-op reason]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-28: Added Natalia reference parity rule: when a reference dashboard is supplied, BPM-4 output must match its dashboard-class interaction and section density, with explicit unavailable blocks instead of silently downgrading to readiness output."
      - "2026-08-28: Added automatic revenue-vs-gross-profit divergence diagnostics: visible gross-margin ratio, volume × margin bridge, transactional factor decomposition, and causal-language guardrail."
      - "2026-08-28: Clarified owner decision: SL is not a standalone canon; it is an Ipatovo-specific SPL fallback used only when payment-discipline data was unavailable and requires explicit owner acceptance elsewhere."
      - "2026-08-03: Added Ipatovo extension for flat B2B base analysis: revenue-only guardrail, hierarchical 1C ingestion, DSL/KML/BNT/SPL/PSC segmentation families, standard breaks, region matrices, growth extraction, and executive summary packaging."
      - "2026-05-28: Added handoff to bpm4-datalens-dashboard for Yandex DataLens implementation and QA."
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# Skill BPM 4 B2B Dashboard Industrial Distribution

## Purpose

Use this skill to handle BPM-4 dashboard work for industrial B2B distribution and distribution-like SKU contexts. The skill is scoped to dealer / partner / client / SKU / warehouse / shipment / order-line analysis, including mixed projects where regular SKU shipments coexist with project sales or light manufacturing.

Do not apply the template mechanically to pure SaaS, professional services, or custom project sales. For mixed projects, explicitly separate the regular SKU layer from project/custom-production layers.

The skill now has **two operating modes**:

1. **Dashboard / BI mode** — semantics, Formula Profit, cross-filters, SI/SIF extraction, DataLens handoff.
2. **Flat base analysis mode** — one-shot dissection of a B2B transaction base into segmentations, breaks, matrices, growth candidates, and executive summary artifacts.

If Natalia or another project operator supplies a reference dashboard, treat it as a mandatory dashboard-class parity benchmark, not as a loose visual example. The output may adapt business semantics to the current B2B distribution source, but it must not silently downgrade to a source-readiness report, static chart packet, or thin Formula Profit proof-of-concept.

The canonical Vault home is:

`Vault/10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPM — Майнинг/OPM/EXEC/BPM-4/INS-OPM-4.07-B2B-дашборд-шаблон.md`

## When To Use

Use when the task mentions:

- BPM-4, numeric database analysis, Formula Profit, dashboard, Metabase, BI, Power BI, Plotly, DataLens, Yandex DataLens;
- industrial distribution, дилеры, дистрибуция, склады, SKU, отгрузки, регулярные поставки;
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

2. Choose operating mode.
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

11. Route to BPM Storyline-Storyboard.
   If a dashboard view creates a hypothesis, storyline move, slide candidate, knowledge deficit, data task, SI/SIF candidate, or BPV action, update the project BPM Storyline-Storyboard or explicitly record a no-op reason.

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
- A reference-dashboard request is not completed by a readiness-only artifact unless the user explicitly asked for readiness-only output.
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
