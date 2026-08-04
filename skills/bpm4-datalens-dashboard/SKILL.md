---
name: bpm4-datalens-dashboard
description: "Use when implementing, reviewing, or fixing a BPM-4 Formula Profit dashboard in Yandex DataLens: SQL views, datasets, charts, controls, click-to-filter, scatter, save/publish cycle, browser QA, and BPM Storyline-Storyboard handoff."
metadata:
  version: "0.1.2"
  status: active
  line: BPM-4 / DataLens dashboard implementation
  owner: Ilya
  supports_bpm:
    primary: [BPM-4]
    required_secondary: [BPM-10, BPM-11]
    optional_secondary: [BPM-2, BPM-3, BPM-5, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9]
  can_consume: [Formula Profit decomposition, domain BPM-4 handoff, SQL views, DataLens datasets, dashboardId / workbookId / revId, BI chart specs, BPM Storyline-Storyboard]
  can_produce: [DataLens build plan, dataset spec, chart spec, dashboard QA packet, post-publish delta, SI / SIF candidates, Storyline-Storyboard writeback proposal, no-op reason]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-05-28: Created DataLens implementation layer for BPM-4 dashboards."
      - "2026-05-30: Added domain handoff support for medical BPM-4 dashboards."
      - "2026-05-30: Added medical dashboard implementation patterns from a Codex-built reference prototype."
---

# Skill BPM 4 DataLens Dashboard

## Purpose

Use this skill when BPM-4 work moves from Formula Profit and data model design into Yandex DataLens implementation. It is the execution and QA layer for SQL views, datasets, charts, controls, click-to-filter, scatter charts, publishing, browser verification, and dashboard-cycle logging.

This skill does not decide the business Formula Profit by itself. If the formula, revenue streams, client/product grain, patient/service grain, payer logic, or industry logic are not agreed, first use the relevant BPM-4 domain skill and return here after the semantic layer is clear.

Known domain handoff sources:

- `bpm4-b2b-dashboard-industrial-distribution`
- `bpm4-it-saas-enterprise-vendor`
- `bpm4-healthcare-clinic-economics`

## When To Use

Use when the task mentions:

- DataLens, Yandex DataLens, datalens API, dashboardId, workbookId, revId;
- BPM-4 dashboard implementation, Formula Profit dashboard, SQL-view, dataset, chart, widget, selector, control;
- moving a BPM-4 dashboard from Power BI to DataLens;
- click-to-filter, chart-to-chart filtering, action params, `enableActionParams`, `state=...`;
- scatter, native scatter, EditorChart, `Request failed with status code 400`;
- save / publish / browser-check / render QA for a DataLens dashboard.

Do not use as the primary skill for:

- defining Formula Profit in an unknown business model;
- Power BI-only implementation;
- generic DataLens dashboards that are not BPM-4 / commercial-performance dashboards.

## Preflight

Before editing or specifying a DataLens dashboard, state:

```yaml
datalens_bpm4_preflight:
  dashboard_mode: current_dashboard | new_dashboard_requested | unknown
  dashboard_id: string|null
  workbook_id: string|null
  current_rev_id: string|null
  formula_profit_status: agreed | partial | missing
  domain_handoff_source: string|null
  domain_mode: string|null
  source_layer: sql_view | dataset | export | unknown
  control_slice:
    year: string|null
    currency: string|null
    business_direction: string|null
    key_totals_checked: true|false
  grain:
    fact_grain: string|null
    client_key: string|null
    product_key: string|null
    patient_key: string|null
    visit_or_episode_key: string|null
    service_or_procedure_key: string|null
    payer_key: string|null
    doctor_key: string|null
    department_key: string|null
    capacity_unit_key: string|null
    date_field: string|null
  units_and_currency_rule: string|null
  api_or_ui_mode: api | ui | mixed | unknown
  blockers: []
```

Rules:

- Do not create a new dashboard if the user asked to work in the current one.
- If `formula_profit_status = missing`, stop dashboard design and request or build the Formula Profit first.
- If currencies or units are mixed without an explicit rule, stop client-facing claims and create a data-quality backlog.
- If `dashboardId`, `workbookId`, or `revId` are needed for an edit and missing, ask for them or locate them before making changes.

## Build Order

Follow this order:

1. Build or locate SQL-view and dataset.
2. Check the control slice: year, currency, business direction, and key sums.
3. Build first screen: Formula Profit and revenue decomposition.
4. Build dynamics.
5. Add breakdowns by clients, products, managers, territories, or other agreed entities.
6. Add scatter charts only after standalone render is stable.
7. Add RFS / DDS / GPC or other agreed segmentations as breakdown tables, not just top filters.
8. Enable click-to-filter for breakdowns and segmentations after structural/API changes are done.
9. Save, publish, read the fresh dashboard, and browser-check the published view.
10. Record post-publish delta, limitations, and backlog.

## Data Model Rules

DataLens BPM-4 dashboards should stand on calculated SQL views or a clean dataset layer, not on heavy chart-level formulas.

Minimum field groups for commercial dashboards:

- period fields: date, year, quarter, month number, month label;
- commercial dimensions: business direction, organization, currency, client / buyer, order, product / nomenclature, product type, channel, region, manager where available;
- metrics: revenue, discount, returns, cost, expenses, extra income, gross profit, gross margin percent, quantity in source unit, quantity in reporting unit;
- segment fields: RFS, DDS, GPC or project-specific equivalents, calculated at client level when relevant.

For medical BPM-4 dashboards, use the medical handoff fields instead of forcing the commercial vocabulary:

- period fields: appointment / visit / procedure / payment / registry date, with one explicit date basis per chart;
- medical dimensions: branch / site, department, doctor, patient cohort, payer stream, service group, procedure, diagnosis / case-mix group where approved, cabinet / bed / equipment where relevant;
- medical facts: patients, appointments, visits, performed services / procedures, prescriptions / orders, payments / charges / registry value, no-shows, cancellations, available time, scheduled time, performed time;
- medical metrics: revenue or registry value, visits per patient, average check or value per patient, service depth, prescription-to-performance conversion, payer mix, capacity utilization, leakage, LTV where cohort logic supports it;
- data-gap fields: missing appointment / request / prescription / payment / payer / capacity / cost entities and their claim status.

Guardrails:

- Do not sum different currencies into one value.
- Do not sum different units into one volume unless a project rule defines a reporting unit.
- Do not calculate segment buckets at chart level if they can be calculated in SQL or dataset.
- Sort months by technical date or month number, not by text label.
- When datasets differ, selectors need compatible fields, aliases, or selected target tabs.
- For medical dashboards, do not treat dictionaries as fact tables, performed procedures as prescriptions, appointments as visits, or payer tariffs as cashflow unless the domain handoff explicitly allows it.

Medical dashboard modules that DataLens may implement after domain approval:

- top KPI strip: revenue / registry value, patients, visits or episodes, average check, LTV or value per patient, visits or episodes per patient, service depth, average service price;
- outpatient / inpatient / diagnostics / rehabilitation tabs when source grain and management action differ;
- plan-fact table with explicit plan source, period allocation rule, and caveat if the plan is illustrative;
- dynamics with grain switch: month by default, quarter/year for management overview, day only for detailed period diagnostics;
- structure tables with click-to-filter: branch, department, doctor, payer stream, age cohort, service group, room / cabinet / bed / equipment where available;
- RFM / cohort matrix with service breakdown by selected segment;
- ABC / concentration table for patient, payer, service, or doctor concentration;
- repeat-visit or repeat-admission funnel with transition cards and service mix by step;
- scatter matrices: doctors and departments by patients x LTV, visits per patient x average check, with average reference lines where supported;
- Sankey transition maps for observable patient flows, clearly separated from verified referrals;
- capacity or load proxy block only when the denominator is explicitly marked as true capacity, schedule capacity, or historical maximum proxy.

## Dashboard Structure

One main BPM-4 dashboard should usually follow this sequence:

```text
0. Formula Profit
0.1. Clients and order economics
0.2. Compact unit economics
1. Dynamics
1.1. Metric dynamics breakdown
2. Clients
3. Products
4. Segmentations
```

Structure rules:

- Keep Formula Profit visible at the start; shrink secondary KPI blocks before removing the formula.
- Do not turn the first screen into a wall of huge KPI cards.
- Use a table/matrix for unit economics when multiple units exist.
- For long dashboards, enable table of contents and keep section names short.
- Use tabs only when the dashboard is too long and dataset links are already stable.

## Chart Rules

For every chart:

- Title explains the slice and metric.
- Tooltip is enabled unless it is a simple KPI card.
- Number format matches metric type: money, percent, quantity, or ratio.
- Sorting follows the management question, not accidental alphabetical order.
- Colors remain stable for the same metrics across blocks.
- Visualization answers the block question rather than merely exposing available fields.

Specific rules:

- KPI cards: compact, no internal scroll, one management metric per card.
- Dynamics: do not stack revenue, cost, profit, percentages, and quantities in one column stack.
- Breakdown tables: top-15 or top-20 in the main dashboard; use pagination, scroll, drilldown, or export for full lists.
- Tables: use data bars / conditional formatting for numeric columns.
- Segmentations: RFS / DDS / GPC should be tables with data bars and click-to-filter, not only top selectors.
- Tooltips should help verify numbers: entity/period, main metric, revenue, gross profit, gross margin percent, and LFL details where relevant.

## Click-To-Filter

Top selectors should stay short: direction, year, quarter/month/date, currency, client, product type, product, and selected metric when needed.

Mandatory click-to-filter candidates:

- metric dynamics breakdown;
- client breakdown;
- product type breakdown;
- product / nomenclature breakdown if performance allows;
- RFS / DDS / GPC segmentation tables.

Workflow:

1. Finish structural and layout changes first.
2. Publish dashboard.
3. Enable chart filtering through UI when DataLens API cannot reliably preserve `enableActionParams`.
4. Save dashboard.
5. Read fresh dashboard and check `enableActionParams`.
6. Test a click in the published dashboard.
7. Confirm `state=...` appears, connected widgets change, and the test state is then cleared from the URL.

If `state=...` appears but widgets do not change, diagnose dataset links, aliases, selected tabs, and incompatible fields before blaming click-to-filter itself.

## Scatter Rules

Scatter is for commercial attractiveness diagnostics of entities: client, product type, product, manager, territory, or another agreed entity.

Default schema:

```text
X = gross margin percent
Y = gross profit
Point = entity
Size = revenue, only if render is stable
Tooltip = entity, revenue, gross profit, gross margin percent, quantity, average price, orders, LTV where relevant
```

Required:

- Build and check the scatter as a standalone chart first.
- Use manual axis titles with filled title values.
- Keep tooltip on.
- Insert into the dashboard only after standalone render works.
- If dashboard render returns `400`, first inspect dashboard controls and dataset compatibility.
- Do not fix scatter `400` by changing only container size.
- Enable click-to-filter on scatter only after stable render; table and segmentation click-to-filter come first.

Native scatter is preferred for basic dots, axes, tooltip, color/size, and diagnostic reading. Use EditorChart only when persistent labels, average lines, custom legend, zoom, or a Power BI-like composition is genuinely required.

## API Workflow

Before any API edit, read a fresh dashboard:

```text
getDashboard -> capture revId, items, layout, controls, chartIds, settings
```

Update sequence:

```text
1. updateDashboard mode=save with current revId
2. capture revId from save response
3. updateDashboard mode=publish with new revId
4. getDashboard again
5. verify published revId and structure
```

Never store tokens, OAuth, IAM, or secrets in markdown, skill files, SQL, or handoff notes.

After publishing, verify:

- revId changed;
- expected item/layout counts are present;
- chartIds were not lost;
- deleted selectors are not still in controls;
- `expandTOC` is as intended;
- `enableActionParams` is true where UI filtering was enabled;
- published browser view renders without `400`;
- test `state=...` is cleared before handing over the URL.

## Output Contracts

Use these packet shapes when useful.

```yaml
datalens_dataset_spec:
  source_views: []
  dataset_ids: []
  grain: string
  required_fields: []
  calculated_fields: []
  control_totals: []
  data_quality_gaps: []
```

```yaml
datalens_dashboard_build_plan:
  dashboard_id: string|null
  build_order: []
  charts_to_create_or_update: []
  controls_to_create_or_update: []
  click_to_filter_targets: []
  scatter_stabilization_needed: []
  browser_check_plan: []
```

```yaml
datalens_chart_spec:
  chart_name: string
  block: Formula Profit|Dynamics|Clients|Products|Segments|Other
  dataset: string
  question_answered: string
  fields:
    dimensions: []
    measures: []
    tooltips: []
    filters: []
  formatting:
    number_format: string
    colors: string
    sorting: string
  interaction:
    click_to_filter: required|optional|off
    control_compatibility: string
```

```yaml
datalens_quality_check:
  data_and_formula: pass|fail|partial
  first_screen: pass|fail|partial
  dynamics: pass|fail|partial
  breakdowns: pass|fail|partial
  scatter: pass|fail|partial|not_used
  segmentations: pass|fail|partial|not_used
  navigation: pass|fail|partial
  api_publish: pass|fail|partial
  browser_render: pass|fail|partial
  limitations: []
```

```yaml
post_publish_delta:
  dashboard_id: string
  workbook_id: string|null
  published_rev_id: string
  changed: []
  verified_by_api: []
  verified_in_browser: []
  remaining_limits: []
  next_backlog: []
```

## Storyline And Downstream Routing

Treat DataLens implementation as BPM evidence, not just visualization.

Route any discovered insight or gap:

- Storyline-Storyboard: slide hypothesis, storyline move, evidence gate, data deficit, or field question.
- BPM-10 / BPM-11: data-model, CRM, ERP, dictionary, join, or grain gaps.
- BPM-8 / BPV: if a chart becomes a management rhythm, action queue, or meeting control.
- 1-ka: if a chart becomes a training exercise or dashboard-reading rubric.
- 2-ka: if a chart supports a case, product-vitrine thesis, or content candidate.
- 5-ka / 8-ka: if the pattern becomes reusable method, SI, SIF, or dashboard standard.

If no route is needed, record a no-op reason instead of silently dropping the finding.

## Completion Checks

- Formula Profit is agreed or the missing formula is named as a blocker.
- Dashboard is updated in the current place unless the user explicitly requested a copy.
- SQL-view / dataset layer is checked before charts are treated as valid.
- Control totals are checked for year, currency, business direction, and core sums.
- Formula Profit appears before diagnostic blocks.
- Currencies and units are not mixed without an explicit rule.
- Main breakdown tables are limited or have pagination / drilldown / export logic.
- Data bars / conditional formatting are present where tables carry numeric decisions.
- Tooltips are enabled for main charts.
- Scatter charts are standalone-checked before dashboard insertion.
- Click-to-filter is enabled and tested for breakdowns and segmentations.
- Save happened before publish, and fresh dashboard state was read after publish.
- Browser render is checked before claiming the dashboard is ready.
- Final answer names dashboardId, revId, what changed, what was checked, and remaining limitations.
