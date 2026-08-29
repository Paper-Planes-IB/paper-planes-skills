---
name: bpm4-healthcare-clinic-economics
description: Use when working with BPM-4 Formula Profit for healthcare, clinics, hospitals, medical centers, archived medical projects, MIS/EMR exports, patient flow, appointments, visits, procedures, doctors, departments, beds, cabinets, equipment, payer mix, OMC/DMS/commercial revenue, LTV, capacity, SI / SIF impact, and HTML-first medical dashboards.
metadata:
  version: "0.1.6"
  status: active
  line: BPM-4 / healthcare clinic economics
  owner: Ilya
  supports_bpm:
    primary: [BPM-4]
    required_secondary: [BPM-11]
    optional_secondary: [BPM-2, BPM-3, BPM-5B, BPM-5C, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9, BPM-10]
  can_consume: [MIS / EMR exports, appointment / visit / prescription / referral / procedure / payment datasets, P&L, OMC / DMS / commercial registers, doctor schedules, capacity data, service dictionaries, KSG / tariff dictionaries, archived medical project artifacts, Power BI / DataLens / HTML dashboard examples, BPM Storyline-Storyboard, SI / SIF registers]
  can_produce: [medical Formula Profit decomposition, healthcare dashboard view spec, clickable HTML dashboard prototype, patient journey transaction-log map, data-gap ledger, payer / patient / capacity economics map, implementation-neutral dashboard handoff, optional DataLens handoff, SI / SIF impact map, Storyline-Storyboard writeback proposal, no-op reason]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-20: Added external healthcare market signal guard: separate market baseline from client facts, nominal growth from price/volume/mix, and require payer/capacity/cost/geography evidence before project claims."
      - "2026-05-30: Activated medical BPM-4 domain view and added explicit DataLens handoff contract."
      - "2026-05-30: Added reusable dashboard patterns from a Codex-built medical-center prototype."
      - "2026-05-30: Re-anchored healthcare BPM-4 as HTML-first / implementation-neutral, added archived medical project scan and SI impact layer."
      - "2026-05-30: Corrected misheard SAF to SI; APQ is only a downstream artifact route, not the primary reasoning layer."
      - "2026-05-31: Added BPM Exchange matrix for medical BPM-4 hypotheses and graph classes."
---

# Skill BPM 4 Healthcare Clinic Economics

## Purpose

Use this skill for BPM-4 work in medicine: clinic / hospital economics, archived medical project reuse, MIS data, patient flow, medical services, payer mix, capacity, doctors, departments, beds, cabinets, equipment, SI / SIF impact, and management dashboards.

This skill is an industry layer over BPM-4, not a replacement for the BPM-4 canon. It must be applied only to the extent supported by the actual database structure. Missing data is a management finding, not a reason to invent metrics.

## Scope Lock

Use for:

- private clinic, medical center, dentistry, diagnostics, outpatient or inpatient economics;
- state / public hospitals with mixed funding: OMC, DMS, commercial, VMP, budget, research, clinical trials;
- MIS / EMR exports, 1C / finance exports, appointment records, visit logs, procedure facts, service dictionaries, KSG / tariff dictionaries;
- dashboards for patient flow, Formula Profit, LTV, payer mix, doctor / department / branch performance, capacity, utilization, and medical service mix;
- cases where patient journey, data model, and economics must be reconciled.
- deriving SI / SIF candidates and reusable Paper Planes artifacts from medical BPM-4 work: methodology, HTML dashboard scaffold, data model, training unit, product-vitrine module, anonymized case, or operating rhythm.

Do not use as-is for:

- pharmaceutical distribution, SKU warehousing, or medical equipment distribution; use the B2B distribution BPM-4 skill;
- SaaS / healthtech vendor commercial analytics; use the IT / SaaS BPM-4 skill;
- generic BI implementation after the medical formula is already agreed; use this skill only for medical semantics and use `bpm4-datalens-dashboard` only when DataLens is explicitly requested or already chosen;
- clinical quality analysis without economic, flow, or capacity implications.

## External Healthcare Market Signal Guard

External healthcare reports can provide market baseline, trend hypotheses, comparator ranges, regulation context, payer structure, consolidation signals, workforce constraints, and candidate BPM-7A/7B questions. They do not confirm a clinic's patient flow, profitability, capacity, payer mix, geography, service portfolio, data quality, or implementation readiness.

Before converting an external market claim into a project claim, require the following bridge:

```text
external market signal
-> exact segment / geography / payer / period
-> nominal growth split: price / volume / mix
-> client capacity and workforce denominator
-> client cost-side and contribution
-> local demand / referral / competition evidence
-> project decision that would change
```

Rules:

- Never use market CAGR as a proxy for client growth, physical volume, or profit growth.
- Separate price, volume, mix, medical inflation, payroll, equipment, consumables, and service complexity.
- Do not transfer laboratory, dentistry, diagnostics, private-clinic, or state-hospital benchmarks across segments without an explicit analogy caveat.
- For mixed or public medicine, separate OMC / DMS / commercial / VMP / budget / research streams before applying a commercial-market conclusion.
- For regional expansion, add local workforce, referral network, licenses, payer context, CAPEX/OPEX, equipment service, and operating-model reproducibility.
- Route an accepted external signal into the industry reference, BPM-7A/7B hypothesis layer, product-vitrine module, and relevant project Storyline only with visible source rights and a `not client fact` label.

## Preflight

Before making claims, state:

```yaml
healthcare_bpm4_preflight:
  mode: private_clinic_transactional | state_hospital_mixed_funding | mixed | unknown
  organization_type: clinic | hospital | network | diagnostics | dentistry | oncology | other
  formula_profit_status: agreed | partial | missing
  source_systems: [MIS, EMR, CRM, 1C, BI, Excel, OMC_register, DMS_register, schedule, HR, other]
  available_grains:
    patient: true|false
    encounter_or_episode: true|false
    appointment: true|false
    visit: true|false
    prescription_or_order: true|false
    referral_or_transfer: true|false
    performed_service_or_procedure: true|false
    payment_or_charge: true|false
    doctor: true|false
    department: true|false
    branch_or_site: true|false
    room_cabinet_bed_or_equipment: true|false
    schedule_or_capacity: true|false
  payer_fields: [OMC, DMS, commercial, VMP, budget, research, clinical_trials, unknown]
  date_basis: appointment_date | visit_date | procedure_date | payment_date | registry_date | mixed | unknown
  pii_rule: anonymized | personal_data_present | unknown
  data_dependency_decision: apply_full | apply_partial | no_op_until_data
  output_mode: analysis | dashboard_spec | clickable_html_prototype | implementation_handoff | datalens_handoff | si_impact_map | unknown
  implementation_default: html_prototype | datalens | spreadsheet | power_bi | unknown
  archived_medical_project_scan: done | not_needed | missing_access | unknown
  missing_critical_fields: []
```

Rule: if a table or field is absent, do not silently approximate it. Mark the affected block as `apply_partial` or `no_op_until_data` and name the management implication.

Default implementation rule: unless the user explicitly asks for DataLens / Power BI / spreadsheet, assume the first working artifact should be a self-contained clickable HTML prototype. DataLens is an optional production implementation path, not the default output of this skill.

## Archived Medical Project Scan

Before designing a new medical BPM-4 formula, dashboard, or reusable module, check whether archived medical projects or prior medical dashboards contain reusable patterns. Do not copy client-specific facts, names, figures, patient data, or recognizable structures without approval; extract only generalized patterns.

Look for:

- medical Formula Profit variants: private clinic, outpatient, inpatient, diagnostics, rehabilitation, mixed funding;
- source-system patterns: MIS / EMR tables, 1C exports, payment registers, OMC / DMS registers, schedules, service dictionaries;
- data gaps that repeated across projects: missing requests, appointment logs, prescription facts, stable patient IDs, payer markers, doctor schedules, capacity denominators;
- dashboard modules that worked: KPI strip, RFM, repeat funnel, doctor matrices, Sankey transitions, plan-fact, load proxy, inpatient bed-days;
- client-facing caveats and do-not-claim language that prevented overstatement;
- reusable HTML / dashboard scaffold patterns and QA checks;
- downstream artifacts: case, training unit, product-vitrine module, SI / SIF, Storyline-Storyboard hypotheses.

Use this packet when archive reuse matters:

```yaml
archived_medical_project_scan:
  archive_sources_checked: []
  reusable_patterns:
    - pattern: ""
      source_type: dashboard|case|storyline|data_model|proposal|retro|other
      reuse_allowed: yes|no|needs_anonymization|unknown
      destination: formula|html_dashboard|data_gap|training|product_vitrine|case|SI|SIF
  do_not_reuse:
    - item: ""
      reason: client_specific|personal_data|weak_evidence|outdated|unknown_rights
  gaps_to_check_in_current_project: []
```

## Medical BPM-4 -> SI Impact Classes

When medical BPM-4 produces a strong finding, classify which SI / SIF class it affects. Do not leave the result as "just a dashboard insight"; route it into Storyline-Storyboard, SI / SIF candidates, field questions, or no-op.

Use these working SI classes:

| SI class | What BPM-4 can reveal in medicine | Useful graphs / data |
|---|---|---|
| `SI-FP` Formula Profit architecture | what actually drives medical profit: patient flow, payer mix, service depth, capacity, retention, cost, leakage | Formula Profit tree, waterfall, contribution by payer / service / department, revenue bridge |
| `SI-DATA` Data truth / observability | which parts of the medical business are provable and which are invisible in MIS / EMR / finance | source coverage matrix, entity relationship map, data-gap heatmap, claim ledger |
| `SI-JOURNEY` Patient journey and leakage | where demand, appointment, visit, prescription, performed procedure, payment, and follow-up disconnect | funnel, Sankey, time-lag chart, prescription-to-performance conversion, no-show / cancellation bridge |
| `SI-CAPACITY` Medical capacity and bottlenecks | whether revenue / quality is constrained by doctor time, rooms, beds, equipment, OR, diagnostics, or schedule | utilization heatmap, open / available / scheduled / performed time bridge, queue and wait-time dynamics |
| `SI-PAYER` Payer and contract economics | how OMC / DMS / commercial / VMP / budget / research streams behave differently and distort averages | payer mix stack, payer x service margin matrix, tariff vs cashflow bridge, contract waterfall |
| `SI-DOCTOR` Doctor / role / department economics | how doctors, departments, roles, case-mix, repeat behavior, and service depth shape economics | doctor scatter, department scatter, case-mix normalized table, first-line vs realization role filter |
| `SI-PORTFOLIO` Service portfolio and clinical direction strategy | which services / directions create value, repeat, follow-up, cross-flow, or capacity strain | service portfolio matrix, ABC / concentration, service co-occurrence, direction x payer x margin |
| `SI-RETENTION` Repeat, cohort, and LTV mechanics | how patient cohorts return, churn, reactivate, or move across service lines | RFM, cohort retention, repeat-visit funnel, LTV by cohort / service / payer |
| `SI-RHYTHM` Management rhythm / operating system | which dashboard findings need regular owner review, action queue, meeting rhythm, escalation, or process owner | decision table, owner-action heatmap, threshold list, weekly / monthly review panel |
| `SI-PRODUCT` PP product and method packaging | which part can become a product-vitrine module, fullkit, training unit, proposal block, or reusable HTML scaffold | artifact map, product-route table, case anonymization checklist, reuse / quality log |

Minimum SI packet:

```yaml
medical_bpm4_si_packet:
  finding: ""
  si_class: SI-FP|SI-DATA|SI-JOURNEY|SI-CAPACITY|SI-PAYER|SI-DOCTOR|SI-PORTFOLIO|SI-RETENTION|SI-RHYTHM|SI-PRODUCT
  evidence_graph_or_table: ""
  source_tables: []
  claim_status: confirmed_by_data|partial|inference|missing|do_not_claim
  management_implication: ""
  next_evidence_needed: []
  route_to:
    storyline_storyboard: true|false
    field_questions: true|false
    product_vitrine: true|false
    training_unit: true|false
    reusable_scaffold: true|false
    apq_register: true|false
```

APQ / asset routing is downstream only: use it when a medical BPM-4 output becomes a reusable method, HTML scaffold, skill, product module, training unit, dashboard standard, anonymized case, or repeatable operating rhythm. Do not use APQ language as a substitute for the SI classification.

## Medical BPM-4 -> Other BPM Hypotheses

Medical BPM-4 is a donor BPM for other BPMs. An economic graph should usually produce a question for another BPM before it becomes a strategic, process, customer, product, or staffing claim.

Use this exchange packet:

```yaml
medical_bpm4_exchange_packet:
  bpm4_signal: ""
  graph_class: ""
  source_tables: []
  economic_observation: ""
  target_bpm_hypotheses:
    - target_bpm: BPM-1|BPM-2|BPM-3|BPM-5|BPM-6|BPM-7A|BPM-7B|BPM-8|BPM-9|BPM-10|BPM-11
      hypothesis: ""
      evidence_needed: ""
      graph_or_field_check: ""
      claim_status: confirmed_by_data|partial|inference|missing|do_not_claim
  storyline_delta: appeared|strengthened|weakened|no_material_delta
  si_candidate: ""
  no_op_reason: ""
```

Core medical graph classes:

| Graph class to build in HTML prototype | BPM targets | Hypotheses it can produce |
|---|---|---|
| Medical Formula Profit tree / waterfall | BPM-2, BPM-5, BPM-8, BPM-10, BPM-11 | the profit constraint is offer architecture, process ownership, management rhythm, CRM / MIS capture, or data model |
| Payer x service / procedure economics matrix | BPM-2, BPM-6, BPM-7A, BPM-7B | payer strategy and service portfolio should differ by OMC / DMS / commercial / VMP / budget stream |
| Patient source / request -> appointment -> visit funnel | BPM-3, BPM-5B, BPM-5C, BPM-8, BPM-10 | patient entry, anxiety, access, handoff, CRM status, or booking process creates leakage |
| Appointment -> visit -> prescription -> performed procedure bridge | BPM-3, BPM-5, BPM-8, BPM-9, BPM-11 | clinical recommendation is not converting into performed care because of experience, process, role, capacity, or data gap |
| Repeat-visit / repeat-admission funnel | BPM-2, BPM-3, BPM-7B, BPM-8 | retention is driven by patient journey design, follow-up rhythm, service route, or medical program packaging |
| Cohort / RFM / LTV matrix | BPM-2, BPM-3, BPM-7B | patient base contains different growth routes: reactivation, chronic program, diagnostics-to-treatment, rehabilitation, premium payer |
| Doctor scatter: patients x LTV / visits per patient x average check | BPM-8, BPM-9, BPM-1, BPM-5 | doctor roles, workload, competence, motivation, case-mix, or process design explain economic spread |
| Department / direction portfolio matrix | BPM-2, BPM-6, BPM-7A, BPM-7B, BPM-8 | medical directions differ by attractiveness, right-to-win, capacity strain, and cross-flow potential |
| Capacity heatmap / utilization bridge | BPM-5, BPM-8, BPM-9, BPM-11 | bottleneck is schedule, room / bed / equipment, staffing, standards, or missing denominator |
| Wait-time / time-lag chart | BPM-3, BPM-5, BPM-8, BPM-10 | delay between request, appointment, diagnostics, result, next visit, and procedure creates demand loss |
| Sankey patient-flow map | BPM-3, BPM-5, BPM-8, BPM-11 | observed patient path differs from declared pathway; transitions need process and data-model reconstruction |
| No-show / cancellation / refusal bridge | BPM-3, BPM-5C, BPM-8, BPM-10 | lost demand comes from access, experience, communication, price, CRM status, or process owner gap |
| Plan-fact / forecast variance | BPM-5, BPM-9, BPM-10, BPM-11 | management rhythm, owner model, planning assumptions, staffing, or data granularity are insufficient |
| Data observability heatmap | BPM-10, BPM-11, BPM-5 | organization cannot safely manage a claim yet; source capture, entity model, owner, or process discipline is missing |

Default rule: each HTML medical dashboard prototype should include at least one block that explicitly says which BPM hypotheses the current graph creates. If a graph creates no useful cross-BPM hypothesis, record a no-op reason.

## Core Medical Formula

Start with this skeleton and adapt to the case:

```text
Medical Formula Profit =
  patient flow economics
+ payer / contract economics
+ service / procedure / case-mix economics
+ capacity / time economics
+ patient journey transaction-log economics
+ retention / follow-up economics
- direct medical costs
- personnel and capacity costs
- equipment / room / bed / OR constraints
- data leakage and unmeasured losses
```

Do not force a private-clinic formula onto a public hospital. Choose the mode first.

## Mode 1: Private Clinic Transactional

Use when the business is primarily commercial and the database supports patient / visit / service / payment analysis.

Default tree:

```text
Revenue =
  patients
× patient mix: primary / secondary / reactivated
× visits per patient
× average check
× check depth: services or procedures per visit
× average service price
+ programs / packages / consumables / other sales
```

Required views:

- revenue: cashflow and price-list / base-price revenue if both exist;
- patients: primary, secondary, reactivation, cohort definition;
- LTV and repeat behavior;
- visits, appointments, no-shows, cancellations where available;
- average check, service price, check depth;
- branch / clinic / department / doctor breakdowns;
- age group, doctor category, service category if available;
- LFL dynamics only after date basis is stable.

Guardrail: primary / secondary definitions must be explicit. Example: first-ever patient, first in period, or returned after 12+ months are different definitions.

## Mode 2: State Hospital Mixed Funding

Use when the organization has OMC / DMS / commercial / VMP / budget / research streams, or when MIS is regional and does not directly store commercial checks.

Default tree:

```text
Economic baseline =
  medical volumes by patient / case / visit / procedure
× payer stream: OMC / DMS / commercial / VMP / budget / research
× tariff / price / registry value / proxy value
× department / doctor / capacity constraints
× completed vs prescribed / scheduled / missed flow
```

Required distinctions:

- performed procedure is not the same as prescribed procedure;
- visit is not the same as appointment or request;
- registry value / OMC tariff is not the same as cash payment;
- service dictionary / KSG dictionary is not a transaction table;
- budget funding is not the same as patient-attributed revenue;
- clinical research and sponsor drugs require a separate stream if material.

If appointment / request tables are missing, state that conversion from patient demand to visit cannot be reconstructed from MIS alone. Route the gap to BPM-3, BPM-5B/5C, BPM-8, and BPM-11.

## Patient Journey Transaction Logs

When transaction-like traces exist, use them to reconstruct the observable part of patient journey. This does not replace patient interviews or process interviews; it shows what the systems can prove.

Relevant logs:

- request / call / web-form / referral;
- appointment / booking / waitlist;
- visit / encounter / admission / discharge;
- doctor consultation;
- prescription / order / назначение;
- performed procedure / service / manipulation;
- lab / diagnostics order and result;
- referral between doctors, departments, branches, or organizations;
- transfer to inpatient, OR, ICU, rehabilitation, diagnostics, or external provider;
- cancellation, no-show, refusal, non-performed prescription;
- payment / charge / registry submission;
- complaint, appeal, NPS / CSI, callback, follow-up.

Build journey metrics only where the log chain supports them:

| Journey fragment | Needed data | Possible metric | Caveat |
|---|---|---|---|
| request -> appointment | request and appointment linked by patient / episode / lead id | booking conversion, time-to-appointment | impossible if requests are absent |
| appointment -> visit | appointment and visit status | no-show, cancellation, attendance conversion | appointment date and visit date must be separated |
| visit -> prescription | visit and prescription / order | prescription rate by doctor / department / cohort | doctors differ by case mix |
| prescription -> performed procedure | prescription and performed procedure linked | conversion into execution, leakage, delay | do not infer if only performed facts exist |
| doctor A -> doctor B | sequential visits / referrals | cross-doctor pathway, internal referral graph | sequence is not causality without referral marker |
| department A -> department B | sequential visits / transfers | pathway between departments, bottleneck nodes | needs episode window and rules |
| diagnostics order -> result -> next visit | orders, results, next encounters | diagnostic cycle time, result-to-action delay | result availability may be outside MIS |
| outpatient -> inpatient / OR / rehab | encounter type / transfer / admission | escalation or continuation rate | needs shared patient / episode key |
| visit -> payment / registry | visit and charge / registry | monetization / tariff attribution | cashflow, tariff, and registry value differ |
| complaint -> process change | complaint and resolution / process log | quality loop closure | often qualitative, route to BPM-8 |

For cross-intersections by doctors, departments, services, and branches, state the unit:

```text
patient-period | episode | visit sequence | prescription basket | performed-service basket | doctor pair | department pair
```

Allowed diagnostics:

- doctor-to-doctor transition matrix;
- department-to-department transition matrix;
- service / procedure co-occurrence inside visit or episode;
- prescription-to-performance conversion by doctor / department / service group;
- internal referral graph;
- leakage after appointment, prescription, diagnostics, or first visit;
- time lag between steps;
- frequent path patterns by cohort, payer, branch, age group, service line;
- patient journey segments: primary, secondary, reactivated, chronic / long-cycle, surgery / diagnostics / rehabilitation.

Guardrails:

- Do not call a sequence a referral unless a referral / назначивший врач / source marker exists.
- Do not call performed-service co-occurrence a clinical pathway without episode logic.
- Do not compare doctors without case-mix, department, schedule, and patient cohort caveats.
- If only performed procedures exist, say that missed prescriptions, refusals, and unperformed recommendations are invisible.
- If patient IDs are anonymized but stable, journey analysis is possible; if IDs are unstable by system, restrict to aggregate flow.
- If personal data appears, anonymize before externalization or screenshots.

Route findings:

- BPM-4 if the journey fragment changes revenue, LTV, payer mix, check depth, utilization, or leakage;
- BPM-11 if the fragment reveals missing entities, keys, or target data model requirements;
- BPM-3 / BPM-5B / BPM-5C if the fragment cannot explain motivation, anxiety, refusal, no-show, or service experience;
- BPM-8 if the fragment points to process ownership, handoff, or AS-IS / TO-BE reconstruction;
- BPM-9 if the fragment points to role, workload, skill, or staffing constraints.

## Capacity Economics

Always check whether economics are constrained by capacity:

```text
Capacity economics =
  open time
× available time
× scheduled time
× performed visit / procedure time
× conversion from appointment to visit
× revenue or tariff value per hour
```

Possible capacity units:

- doctor;
- department;
- branch / site / building;
- cabinet / room;
- bed;
- operating room;
- diagnostic equipment: CT, MRI, PET/CT, ultrasound, angiography, lab line, other;
- day hospital / inpatient ward;
- nursing or support staff.

Do not calculate utilization if the denominator is not defined. `Open time`, `available time`, `scheduled time`, and `performed time` are different management concepts.

## Payer / Contract Economics

Separate payer streams before averages:

| Stream | Typical metric | Common trap |
|---|---|---|
| OMC | tariff / registry value / KSG | treating tariff as cashflow |
| DMS | insurer contract, visit or service value | mixing insurer rules with commercial price |
| Commercial | paid services, checks, packages | missing informal / off-system payment risk |
| VMP | high-tech care quota / tariff | mixing VMP with ordinary OMC |
| Budget | subsidy or program funding | attributing budget to individual patient without rule |
| Research / clinical trials | trial income, sponsor drugs, study costs | mixing research income with service revenue |

If payer is absent or unreliable, no client-facing payer-mix claim is allowed. Produce a missing-field request.

## Data Dependency Rules

Apply blocks only when the database supports them:

| Available data | Allowed analysis | No-op / caveat |
|---|---|---|
| Patient ID only | repeat, cohort, anonymized flow | no revenue unless linked to payment / tariff |
| Appointment table | demand, no-show, booking conversion | no performed care unless linked to visit |
| Visit table | patient contact and visit frequency | no service mix unless linked to procedures |
| Performed procedure table | service mix and medical volumes | no demand loss or missed prescriptions |
| Prescription / order table | prescribed vs performed gap | no payment unless linked to procedure / charge |
| Payment / charge table | cashflow, check, payer value | no medical pathway unless linked to visit / service |
| Service / KSG dictionary only | normalization and grouping | not a transaction baseline |
| Doctor schedule | capacity denominator | no utilization without visit / performed time |
| Bed / OR / equipment schedule | bottleneck and utilization analysis | no economic effect without volumes / value |

When data is partial, produce a `data-gap ledger` with:

```yaml
data_gap:
  missing_entity: appointment | request | visit | prescription | performed_service | payment | payer | doctor | capacity | cost
  affected_metric: ""
  impact_on_formula_profit: ""
  allowed_partial_analysis: ""
  required_source_or_owner: ""
  route_to_bpm: [BPM-4, BPM-11]
```

## Dashboard View Spec

Recommended sequence:

1. Formula Profit tree: patient flow, payer mix, service mix, capacity.
2. Executive KPI strip: revenue / registry value, patients, visits, procedures, LTV or value per patient, payer mix, utilization.
3. Dynamics: revenue, patients, visits, average check, service price, depth, capacity utilization, LFL where valid.
4. Breakdowns: branch, department, doctor, payer, service group, patient cohort, equipment / bed / OR where relevant.
5. Bottleneck views: appointment-to-visit, prescribed-to-performed, open-to-available-to-performed time, equipment downtime where available.
6. Data-gap ledger: visible limitations and next data requests.

Recommended diagnostic modules when the data supports them:

- outpatient vs inpatient tabs, if the economics, grain, and source systems differ;
- plan-fact top layer, but only with an explicit plan source, seasonality rule, and caveat if the plan is illustrative or transferred from another year;
- RFM / cohort layer for patient base economics: recency, frequency, monetary value, service mix by segment, and click-through from segment to top services;
- ABC / concentration layer for patients, payers, service groups, or doctors where concentration changes management action;
- repeat-visit / repeat-admission funnel: transition 1 -> 2, 2 -> 3, stabilization point, loss between steps, and service mix by visit number;
- interval vs check scatter: days between visits / admissions on X, average check on Y, visit / admission number as label;
- doctor and department matrices: patients x LTV, visits per patient x average check, with average lines and filters by specialty / role when available;
- patient-flow Sankey: branch / department / service group / doctor transitions, separated from true referral unless a referral marker exists;
- capacity proxy block only when true capacity is absent: historical maximum as a temporary denominator, clearly marked as proxy, not operational capacity;
- inpatient block when relevant: episodes, unique patients, bed-days, average length of stay, value per bed-day, admission dynamics, length-of-stay distribution.

Every view must name:

- user / decision-maker;
- management action;
- owner of the process or data;
- source table;
- refresh frequency;
- threshold or reason to react.

## Optional DataLens Handoff

Use DataLens only when the user explicitly asks for DataLens, an existing DataLens workspace/dashboard is already the target, or the project decision says the HTML prototype must be moved into DataLens. This skill keeps the healthcare Formula Profit, medical grain, metric caveats, and data gaps; `bpm4-datalens-dashboard` owns DataLens datasets, charts, controls, save / publish, and browser QA only on that optional branch.

Use this packet shape:

```yaml
medical_datalens_handoff:
  domain_skill: bpm4-healthcare-clinic-economics
  target_skill: bpm4-datalens-dashboard
  formula_profit_status: agreed | partial | missing
  healthcare_mode: private_clinic_transactional | state_hospital_mixed_funding | mixed | unknown
  semantic_grain:
    patient_key: string|null
    episode_or_visit_key: string|null
    service_or_procedure_key: string|null
    payment_or_registry_key: string|null
    doctor_key: string|null
    department_key: string|null
    capacity_unit_key: string|null
    date_basis: appointment_date | visit_date | procedure_date | payment_date | registry_date | mixed | unknown
  required_views:
    - Formula Profit
    - patient flow
    - payer mix
    - service / procedure mix
    - doctor / department performance
    - capacity and utilization
    - data-gap ledger
  protected_claims:
    - claim: ""
      status: confirmed_by_data | partial | missing | do_not_claim
      source_table: ""
      caveat: ""
  data_gaps: []
  pii_rule: anonymized | personal_data_present | unknown
  datalens_build_request: dataset_spec | dashboard_spec | implementation | qa_only
```

Do not let the implementation layer normalize medical entities into generic commercial entities without naming the mapping. For example, `patient` may be the economic subject, `service / procedure` may replace `product`, and `payer stream` may replace `customer segment`; each mapping must be explicit.

## Clickable HTML Prototype Mode

When the user asks to "build", "show", "prototype", "make clickable", "прокликаем", "в HTML", "дашборд-макет", or similar, produce a clickable HTML dashboard prototype unless they explicitly ask for Power BI / DataLens / spreadsheet only.

Purpose of the HTML prototype:

- test management logic before BI implementation;
- make Formula Profit, filters, drilldowns, and broken data areas visible;
- let the team click through patient, payer, service, doctor, department, and capacity views;
- separate agreed metrics from placeholders and data gaps.

Default artifact:

```text
healthcare-bpm4-dashboard-prototype.html
```

Prototype requirements:

- single self-contained HTML file unless the user asks for a larger app;
- no backend requirement for a first prototype;
- use synthetic or aggregated sample data unless the user provides approved data;
- never expose personal medical data or patient identifiers;
- include filters for period, organization / branch, department, payer, patient cohort, doctor category, and service group when supported;
- include tabs for materially different business lines only when their source grain differs, for example outpatient, inpatient, diagnostics, rehabilitation, or mixed funding;
- make dashboard sections clickable: Formula Profit node -> relevant breakdown table / chart / data-gap note;
- make tables and charts cross-filter each other in the prototype where useful: clicking an RFM segment, funnel step, payer row, branch row, doctor row, or department row should reveal the relevant service / procedure mix;
- include visible labels for `confirmed by data`, `partial`, `missing`, and `do not claim`;
- include tabs or segmented controls for:
  - Formula Profit;
  - patient flow;
  - patient journey logs;
  - payer mix;
  - capacity;
  - service mix;
  - repeat behavior / RFM;
  - doctors and departments;
  - patient transitions;
  - data gaps;
- include a "claim / data-gap ledger" panel that changes with selected section;
- every chart/table must have a management action, not only a metric.

Interaction rules:

- clicking a KPI node filters or opens the corresponding explanation panel;
- clicking a row in branch / department / doctor / payer tables updates the detail panel;
- clicking a segment in RFM / ABC / cluster tables updates the service / procedure breakdown;
- clicking a funnel step updates the service / procedure breakdown for that visit / admission number;
- clicking a journey transition, doctor pair, department pair, or prescription-to-performance metric opens its evidence and caveat panel;
- missing data blocks must be clickable and explain what cannot be calculated and which source is needed;
- reset filters must be available;
- if the prototype uses placeholder data, mark it clearly as `synthetic / illustrative`.

Design rules:

- prioritize dense, operational dashboard layout over a marketing page;
- no landing page;
- no decorative hero or card-heavy storytelling page;
- keep the first screen focused on Formula Profit and filters;
- use a sticky top bar with page tabs, active filters, and source/date metadata when the prototype has multiple medical contours;
- use stable dimensions for KPI tiles, charts, tables, and filter controls;
- prefer dense KPI rows, compact tables with in-cell bars, fixed chart heights, and collapsible secondary detail over oversized cards;
- ensure text fits on desktop and mobile;
- use restrained colors and clear status encoding rather than a one-hue palette.

Verification:

- open the HTML locally in a browser or via a lightweight local server;
- click through each tab / filter / drilldown;
- verify that no core panel is blank;
- verify that synthetic / missing-data labels are visible;
- if browser automation is available, capture at least one desktop screenshot and inspect obvious layout overlaps.

## QA Guardrails

Before accepting a dashboard or claim:

- check key totals against source totals;
- check date basis and period filters;
- check currency / payer / tariff rules;
- inspect broken visuals and blank fields;
- flag impossible LFL values or denominator errors;
- verify primary / secondary / reactivation definitions;
- verify that dictionaries are not treated as fact tables;
- verify that mixed payer streams are not averaged into misleading ARPU / LTV;
- verify that no protected personal data is exposed in screenshots or external prompts.
- for clickable HTML prototypes, verify tabs, filters, row clicks, KPI clicks, reset action, and data-gap panels before calling the artifact ready.

## SI / Storyline Routing

Route strong findings to BPM Storyline-Storyboard or record a no-op reason:

- `Patient journey cannot be reconstructed from MIS only`;
- `Observable patient journey comes from transaction logs, not only interviews`;
- `Prescription-to-performance conversion reveals hidden leakage`;
- `Doctor and department transition matrices need episode and case-mix guardrails`;
- `Data-gap as управленческий вывод`;
- `Medical Formula Profit needs patient-flow + capacity + payer mix`;
- `Service dictionary is not transaction evidence`;
- `Capacity bottleneck as revenue and quality constraint`;
- `Payer stream separation before averages`;
- `Dashboard QA before client-facing claims`.

Downstream:

- BPM-11 for target data model, entities, source owners, and dashboard semantic layer;
- BPM-3 / BPM-5B / BPM-5C for missing patient entry, demand, experience, no-show, and journey evidence;
- BPM-8 for process reconstruction and prescribed-vs-performed gaps;
- BPM-9 for doctor / nurse capacity, roles, motivation, and competence constraints;
- BPM-6/7 for market, service portfolio, payer strategy, and priority medical directions.

## Completion Checks

- Scope mode is explicit: private clinic, state hospital, mixed, or unknown.
- Data dependency decision is explicit: full, partial, or no-op until data.
- Formula Profit separates patient flow, payer mix, service mix, capacity, and costs where available.
- Patient journey transaction logs are used when available, with unit of analysis and caveats stated.
- Missing appointment / request / prescription / payment / capacity tables are named, not hidden.
- Payer streams are separated before averages.
- Capacity denominator is defined before utilization claims.
- Dashboard views have owners and management actions.
- If clickable HTML is requested, the prototype is created, opened, clicked through, and verified for nonblank states.
- QA flags broken visuals, denominator issues, LFL anomalies, and dictionary-vs-fact confusion.
- BPM Storyline-Storyboard is updated or a no-op reason is recorded when hypotheses change.

## Structured Analytical Artifact Gate

Patient/payer/service/doctor segmentations, patient-journey maps, claim ledgers, metric trees, dashboard dimensions, analytical visuals, and Storyline-Storyboard deltas inherit the global contract in `~/.codex/AGENTS.md`. Always state clinical/business unit of analysis, event grain, numerator/denominator, dictionary-vs-fact boundary, multi-label membership, data rights, missing events, and management decision. Methodology and Frappe never fill absent MIS/EMR/finance evidence.
