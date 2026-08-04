# Medical Clinic Economics Semantic Layer

## Quick Reference

- Area: medical clinic and dentistry economics, especially patient-base, route, retention, capacity, source, and doctor economics.
- Intended users: Data Analytics runs for Paper Planes medical projects and dentistry dashboards.
- Coverage level: Directional.
- Source inventory: `references/source-inventory.md`.
- Last synthesized: 2026-06-11.
- Freshness expectations: always re-read the latest client dashboard, MIS/CRM export, or project source pack before client-facing numeric claims.
- Default date and time zone rules: use the date fields from the source export; for Russian client projects, assume local project time only when the source does not specify a timezone.

## Entity Clarification

| Entity | Means | Does Not Mean | Primary IDs | Grain Notes | Sources |
| --- | --- | --- | --- | --- | --- |
| Patient | Person receiving care in MIS/CRM or dashboard export | Unique FIO string across all systems | `ID_Пациента` when available | Patient grain should drive LTV, RFM, repeat, reactivation, and source analysis | Dинастия-С dashboard |
| Appointment | Scheduled visit or booking event | Performed treatment or payment | Appointment row id if available; otherwise appointment datetime + patient + doctor | Appointment grain supports lead time, show-up, no-show, status, and schedule funnel | Dинастия-С dashboard `appointment_rows`, `appointments` |
| Visit | Performed transactional encounter with revenue or manipulations | Appointment, attendance row, or treatment plan | `ID_Посещения` | Visit grain supports revenue, average check, departments, doctors, patient type | Dинастия-С dashboard `visit_rows` |
| Transaction line | Performed service or manipulation line | Whole visit or patient | `ID_Услуги` plus visit id when available | Service portfolio and procedure mix should use line grain, but patient and visit metrics need deduplication | Dинастия-С dashboard `transaction_lines` |
| Attendance | Attendance export or observed show-up row | Financial realization, payment, or revenue | Stable patient id if available; FIO only as fallback | FIO-based attendance comparison is directional and cannot prove financial leakage by itself | Dинастия-С dashboard `attendance_comparison` |
| Doctor | Clinician or provider in source export | Comparable performance unit without case-mix normalization | `ID_Врача` | Doctor analysis must account for specialty, role, case mix, branch, patient type, downstream transfers | Dинастия-С dashboard `doctors`, `doctor_ltv`, `appointment_by_doctor` |
| Branch | Clinic site or filial | Comparable market role by default | Branch name | Branch analysis must separate scale, maturity, territory, service mix, and patient source | Dинастия-С dashboard `branch_month`, project card |
| Department | Clinical direction such as therapy, hygiene, surgery, orthopedics, orthodontics | Product offer by itself | Department name | Use departments for service portfolio and journey transitions, but translate into patient routes before recommendations | Dинастия-С dashboard `department_month`, `markov_transitions` |
| Chair or room capacity | Physical capacity denominator for dental economics | Revenue proxy | Chair, room, cabinet, schedule id | Utilization requires chair or room id, duration, status, and doctor schedule; otherwise it is normative only | BPM-4 healthcare skill, Dинастия-С dashboard `chair_capacity` |

## Key Metrics

| Metric | Definition | Numerator | Denominator | Time Grain | Canonical Source | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | Sum of realized revenue in the selected source grain | `Выручка` | Not applicable | Date, month, visit, service line | Latest transactional export or dashboard aggregate | Confirm whether date is visit, payment, realization, or posting date |
| Transaction visits | Count of distinct performed visits with transaction evidence | Distinct `ID_Посещения` | Not applicable | Visit or month | `visit_rows`, `monthly` | Do not mix with scheduled appointments or attendance rows without reconciliation |
| Patients with revenue | Count of distinct patients with revenue in period | Distinct `ID_Пациента` with revenue | Not applicable | Period | `meta.totals`, patient-level export | Yearly patient counts can double-count patients across years |
| Average visit check | Revenue per transactional visit | Revenue | Transaction visits | Month, branch, department, doctor | `monthly`, `branch_month`, `department_month`, `doctors` | Sensitive to visit definition and department allocation |
| Revenue per patient | Revenue per patient with revenue | Revenue | Distinct patients with revenue | Period or cohort | Patient-level export, RFM | Avoid using summed monthly patients as unique patient denominator |
| Patient type revenue | Revenue by approximate patient type | Revenue by patient type | Revenue | Month | `patient_type_month`, `visit_cube` | Primary/repeat/reactivation definitions must be verified against patient history window |
| RFM segment revenue | Revenue by recency, frequency, monetary segment | Segment revenue | Total revenue or segment patients | Period | `rfm_segments`, `rfm_matrix` | Segment labels are model output; verify thresholds before using operationally |
| LTV | Historical revenue per patient or patient cohort in the export window | Patient revenue | Patient count | Cohort or period | `doctor_ltv`, `cohorts`, patient-level table | This is export-window LTV unless full lifetime history is confirmed |
| Source quality | Patients, patients with revenue, revenue, and revenue per patient by acquisition source | Source-level revenue and patients | Source patients or total revenue | Period | `sources` | Requires source completeness and marketing spend for CAC/ROI claims |
| Show-up rate | Approximate arrived appointments / scheduled appointments | `Дошли` | `Записи` | Appointment month, doctor, lead bucket | `appointments`, `appointment_by_doctor`, `appointment_lead_buckets` | Approximate unless status definitions and day-matching rules are verified |
| Attendance-finance coverage | Weighted share of attendance rows matched to invoice/payment/realization stage | Matched attendance rows | Attendance rows | Export period | `attendance_comparison` | FIO-based matching is directional; not a loss amount |
| Chair utilization | Performed or scheduled time / available chair time | Occupied chair minutes or hours | Available chair minutes or hours | Day, week, month | Schedule + chair id + duration | Do not claim as fact without chair id, duration, status, and schedule |

## Standard Filters And Dimensions

| Filter Or Dimension | Default Logic | Override When | Applies To | Sources |
| --- | --- | --- | --- | --- |
| Period | Use the dashboard or export period explicitly | Comparing YTD, cohorts, or source-specific windows | All metrics | Dashboard `meta`, monthly aggregates |
| Branch | Keep filial/site separate before network average | The question is explicitly network-level only | Revenue, visits, patients, doctors, departments | `branch_month`, `visit_cube` |
| Department | Use clinical direction as route node | Service names are needed for product offer or procedure mix | Revenue, visits, patient transitions | `department_month`, `markov_transitions`, `transaction_lines` |
| Patient type | Separate primary, repeat, and reactivation | Definitions are missing or source history is too short | Revenue, route, CRM, reactivation | `patient_type_month`, `visit_cube` |
| Source | Include source completeness and patients with revenue | Source field is sparse or attribution rules changed | Marketing and acquisition analysis | `sources` |
| Doctor | Analyze by doctor role and case mix | User asks for raw ranking, but caveat heavily | Doctor economics, appointment show-up, LTV | `doctors`, `doctor_ltv`, `appointment_by_doctor` |
| RFM segment | Use segments for retention and reactivation prioritization | Thresholds are unknown and decision requires exact trigger rules | CRM, retention, high-value base | `rfm_segments`, `rfm_matrix` |

## Query Patterns

- Pattern: Medical Formula Profit decomposition
  - Use when: explaining what drives revenue or growth reserve.
  - Key tables: `monthly`, `patient_type_month`, `branch_month`, `department_month`, `rfm_segments`, `sources`.
  - Required filters: period, branch, department, patient type.
  - Common joins: avoid row-level joins unless stable ids are present; reconcile aggregates first.
  - Example skeleton: revenue = patients with revenue * visits per patient * average visit check, then segment by branch, department, patient type, source, and RFM.

- Pattern: Patient journey and leakage map
  - Use when: the question concerns where patients fail to reach treatment or repeat.
  - Key tables: `appointment_rows`, `appointments`, `visit_rows`, `markov_transitions`, `attendance_comparison`.
  - Required filters: appointment month, visit date, doctor, department, branch.
  - Common joins: appointment to visit by stable patient id and date or explicit appointment id; FIO matching is directional only.
  - Example skeleton: appointment -> show-up -> transactional visit -> department transition -> repeat visit -> revenue.

- Pattern: High-value retention and reactivation
  - Use when: sizing CRM opportunity or identifying patient-base priorities.
  - Key tables: `rfm_segments`, `rfm_matrix`, `rfm_top_patients`, patient-level table when safe.
  - Required filters: segment, recency band, monetary band, last visit date.
  - Common joins: patient id to last doctor, last department, source, and last treatment route.
  - Example skeleton: segment revenue and patient count, then estimate scenario only as directional unless future conversion rates are known.

- Pattern: Branch business-model comparison
  - Use when: comparing clinic sites or deciding branch strategy.
  - Key tables: `branch_month`, `visit_cube`, `department_month`, `sources`, `doctor_ltv`.
  - Required filters: branch, period, department, source, patient type.
  - Common joins: branch x department x patient type, branch x source if source is branch-attributed.
  - Example skeleton: compare revenue share, visit share, average check, department mix, source mix, doctor mix, and maturity window.

- Pattern: Doctor role analysis
  - Use when: assessing clinician economics, conversion, or staffing.
  - Key tables: `doctors`, `doctor_ltv`, `appointment_by_doctor`, `predictor_effects`.
  - Required filters: doctor, department, branch, patient type, first doctor vs visited doctor.
  - Common joins: doctor id to department, patient id to downstream departments and patient LTV.
  - Example skeleton: classify doctors by role, not rank: entry, route, high-ticket, retention, complex-treatment, downstream-transfer.

- Pattern: Source and reputation economics
  - Use when: assessing marketing channels and acquisition quality.
  - Key tables: `sources`, monthly/source export if available, marketing spend if available.
  - Required filters: source, period, branch, first visit type.
  - Common joins: source to patient revenue, patient type, RFM, department path.
  - Example skeleton: source patients, patients with revenue, revenue, revenue per patient, coverage, then add CAC only if spend is present.

- Pattern: Capacity and chair economics
  - Use when: discussing chairs, rooms, doctor schedules, or utilization.
  - Key tables: schedule export, chair or room id table, appointment duration, visit rows, revenue by doctor and department.
  - Required filters: branch, chair, date, doctor, status, duration.
  - Common joins: scheduled slot to chair id and visit id; doctor schedule to performed visit.
  - Example skeleton: available chair hours -> scheduled hours -> performed hours -> revenue per chair hour -> no-show/cancelled gap.

## Gotchas

- Gotcha: Repeat patients can dominate revenue.
  - Impact: a marketing-only diagnosis may miss the main growth reserve.
  - How to avoid: always compute patient type revenue and RFM concentration before recommending lead generation.
  - Source: Dинастия-С dashboard, dentistry case draft.

- Gotcha: Top patient concentration can make averages misleading.
  - Impact: average revenue per patient hides high-value retention and reactivation opportunities.
  - How to avoid: inspect RFM segments, RFM matrix, and top-N concentration.
  - Source: Dинастия-С dashboard.

- Gotcha: Department direct revenue is not the same as journey contribution.
  - Impact: hygiene, therapy, diagnostics, or pediatric visits may be undervalued.
  - How to avoid: use Markov transitions and downstream revenue logic before de-prioritizing low-check departments.
  - Source: Dинастия-С dashboard, dentistry case draft.

- Gotcha: Doctor ranking without case mix is unsafe.
  - Impact: teams can overcorrect behavior or incentives based on misleading raw rankings.
  - How to avoid: segment by doctor role, specialty, patient type, first doctor vs visited doctor, and downstream LTV.
  - Source: BPM-4 healthcare skill, Dинастия-С dashboard.

- Gotcha: FIO-based matching can create false leakage claims.
  - Impact: attendance vs finance gaps may be overstated or understated.
  - How to avoid: label FIO-based comparisons directional and request stable ids.
  - Source: Dинастия-С dashboard `attendance_comparison`.

- Gotcha: Chair economics is often normative before it is factual.
  - Impact: capacity decisions can be made on insufficient denominators.
  - How to avoid: require chair id, duration, schedule, and status before utilization claims.
  - Source: BPM-4 healthcare skill, Dинастия-С dashboard `chair_capacity`.

## Related Dashboards And Docs

| Source | Use It For | Caveats |
| --- | --- | --- |
| Dинастия-С portable dashboard v0.9 | Current aggregate benchmark for patient base, RFM, departments, sources, doctors, visits, appointments | Temporary local file; re-read latest export before reuse |
| Dинастия С project card | Project scope, BPM status, source pack, data-quality risks | Operational progress requires confirmation |
| Dинастия / НИЦ / НоваДент case draft | Reusable dentistry insight: money lost between consultation and treatment | Narrative source, not numeric proof |
| BPM-4 healthcare clinic economics skill | Medical Formula Profit, SI classes, graph classes, caveat rules | Domain layer, not client fact source |

## Open Questions

- Question: What is the stable cross-system patient id from appointment, MIS, finance, and attendance exports?
  - Why it matters: needed to quantify funnel leakage and avoid FIO-based overclaiming.
  - Best owner or source to check next: client IT / MIS export owner.

- Question: Which dates define revenue, visits, payments, realization, and appointment status?
  - Why it matters: monthly trends and conversion bridges can change depending on date basis.
  - Best owner or source to check next: dashboard reconcile notes, MIS/finance export definitions.

- Question: Are treatment plans, prescriptions, or recommended procedures available as a table?
  - Why it matters: the core dentistry hypothesis is conversion from consultation and plan to performed treatment.
  - Best owner or source to check next: CRM/MIS owner, doctor-plan workflow owner.

- Question: Are chair id, room id, appointment duration, doctor schedule, cancellations, and no-shows available?
  - Why it matters: factual chair utilization and revenue per chair hour require those denominators.
  - Best owner or source to check next: schedule export owner.

- Question: Is marketing spend available by source, month, branch, and campaign?
  - Why it matters: source revenue can be analyzed now, but CAC/ROI cannot be claimed without spend.
  - Best owner or source to check next: marketing team / finance export.

