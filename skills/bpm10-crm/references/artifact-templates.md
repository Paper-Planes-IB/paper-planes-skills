# BPM10 Artifact Templates

Use these templates as working contracts. Remove unused columns only when the reason is explicit.

## 1. Source Register

| ID | Source | Date | Owner / speaker | Scope | Reliability | What it proves | Conflicts | Link |
|---|---|---|---|---|---|---|---|---|

## 2. Evidence And Decision Ledger

| ID | Claim / design decision | Status | Evidence | Source ID | Confidence | Owner of confirmation | Due date |
|---|---|---|---|---|---|---|---|

Statuses: `confirmed`, `hypothesis`, `rejected`, `requires confirmation`.

## 3. Problem Map

| ID | Management contour | Problem / growth point | Observable fact | Consequence / risk | Proposed change | BPM10 criterion | Source | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|

## 4. Conceptual Entity List

Target file: `Client. CRM. Entity list.md`.

| ID | Business entity | Definition | Management purpose | Processes / funnels | Owner | Key relations | Cardinality | CRM implementation | System of record | Status / question |
|---|---|---|---|---|---|---|---|---|---|---|

Add a separate exclusion table:

| Candidate | Final type | Why it is not a separate entity | Where it lives instead |
|---|---|---|---|

Final types: field, classifier, file, document, stage, activity, event, metric, external-system object.

## 5. Funnels And Smart Processes

Target file: `Client. CRM. Funnels and smart processes.md`.

| ID | Funnel / smart process | Purpose | 4R class | Entity | Owner | Entry signal | Main stages | Success output | Rejection / pause output | Inputs | Outputs | System | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 6. Entity × Process Matrix

| Entity / client type | Reach inbound | Reach outbound | React | Refresh | Re-Engage | Marketing | Service | CRM conclusion |
|---|---|---|---|---|---|---|---|---|

Write `not used` instead of leaving an empty cell. Mark disputed mappings as `requires confirmation`.

## 7. Entity Cards

Target file: `Client. CRM. Entity cards.md`.

| № | Business entity | Card section | Field name | Required at creation | Multiple | CRM field type | Description / values | Source | Filling | Used for | Comment / approval |
|---:|---|---|---|---|---|---|---|---|---|---|---|

`Used for` must name at least one operational purpose: filter, routing, stage control, automation, report, responsibility, or management review.

Do not add system-native fields such as funnel, stage, created date, or system owner as custom fields.

## 8. Functional Requirements

Target file: `Client. CRM. Functional requirements for funnels and smart processes.md`.

| № | Funnel / smart process | Stage | Stage meaning | Responsible role | User actions | Required evidence / fields | External integrations | Automation | Transition criteria | SLA / checkpoint | Rejection / return rule |
|---:|---|---|---|---|---|---|---|---|---|---|---|

Write user actions, evidence/fields, integrations, and automations as bullet lists inside cells. Describe automations as `trigger + action + exception/owner`.

## 9. System Carrier Map

| Process / fact | User action lives in | Confirmed fact lives in | Calculation / analytics lives in | Document of record | Signal to CRM | CRM action | System owner | Integration | Risk |
|---|---|---|---|---|---|---|---|---|---|

## 10. Process Transition Register

| From | Event / condition | To | Object created / updated | Required evidence | Owner | Automation | Failure route |
|---|---|---|---|---|---|---|---|

## 11. RASCI And Governance

| Object / decision | Responsible | Accountable | Support | Consulted | Informed | Evidence | Review cadence | Change authority |
|---|---|---|---|---|---|---|---|---|

Cover at least: funnel ownership, data creation, data quality, stage decision, rejection, integration error, dashboard explanation, and methodology change.

## 12. Management Dashboard Contract

| Metric / signal | Definition | Grain | Source | Refresh rate | Target / threshold | Deviation logic | Owner | Required action | CRM object / task | Escalation |
|---|---|---|---|---|---|---|---|---|---|---|

## 13. Duplicate Protection

| Duplicate risk | Matching key | Detection point | Prevention rule | Merge authority | Audit trail | Exception |
|---|---|---|---|---|---|---|

## 14. Decision Register

| ID | Decision | Status | Rationale | Evidence | Owner | Decision date | Review date | Impacted artifacts |
|---|---|---|---|---|---|---|---|---|

## 15. Open Questions

| ID | Question | Why it matters | Options | Required source / participant | Owner | Due date | Default if unanswered |
|---|---|---|---|---|---|---|---|

## 16. Handoff Checklist

- [ ] Scope and target platform are explicit.
- [ ] Four mandatory CRM documents are attached.
- [ ] All entities have definitions, owners, relations, and system mappings.
- [ ] Every funnel has entry, success, rejection, pause, and return rules.
- [ ] Every stage has an observable result and transition criteria.
- [ ] Custom fields have an operational purpose.
- [ ] ERP, BI, service, document flow, and CRM boundaries are explicit.
- [ ] Integrations describe direction, event, payload owner, and error route.
- [ ] Automations describe trigger, action, exception, and owner.
- [ ] Data quality and duplicate rules are explicit.
- [ ] Governance and change authority are explicit.
- [ ] Open decisions have owners and dates.
- [ ] Client data, private links, credentials, and tokens are removed from external versions.
