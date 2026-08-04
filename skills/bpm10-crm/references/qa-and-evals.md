# BPM10 QA And Evaluation Cases

## QA Gates

### Gate 1. Source Fidelity

- Every material entity, stage, role, integration, and KPI has evidence or a hypothesis label.
- Contradictory sources are visible.
- Client terminology and implementation assumptions are separated.
- No raw transcript phrasing appears as a final requirement without normalization.

### Gate 2. Architecture

- Business objects are separated from fields, documents, stages, activities, events, and metrics.
- Relations and cardinality are explicit where they affect implementation.
- Funnels differ by lifecycle, owner, result, control point, or analytics.
- CRM, ERP, BI, service, project delivery, and document-flow boundaries are explicit.
- Mass transactions remain outside CRM unless a justified card lifecycle exists.

### Gate 3. Lifecycle Control

- Each process has an entry signal, owner, stages, stage result, success, rejection, pause, and return route.
- Each stage has observable transition criteria.
- Rejection reasons support analysis and a defined next state.
- Duplicate creation and repeated routing are controlled.

### Gate 4. Field Design

- Each custom field supports a filter, route, transition, automation, report, responsibility, or management review.
- Required-at-creation fields are minimal.
- Multiplicity, type, source, and filling method are explicit.
- System-native fields are not duplicated.
- Long qualitative materials are stored as links/files/comments rather than fields.

### Gate 5. Governance And Analytics

- Owners exist for CRM, funnels, data quality, integrations, and dashboard explanations.
- RASCI covers decisions and checkpoints.
- Metrics have definitions, grain, source, refresh rate, threshold, and action.
- Management reviews end in decisions, owners, dates, and closure evidence.

### Gate 6. Implementation Readiness

- The four mandatory Markdown documents are consistent.
- Every integration has direction, trigger/event, source of truth, data owner, and error route.
- Every automation has trigger, action, exception, owner, and test case.
- Pilot scope and later scope are separated.
- Open questions have owners and dates.

### Gate 7. Confidentiality And Safety

- No tokens, webhooks, client secrets, private board IDs, personal data, or raw production records are included.
- No raw CRM rows with exact deal titles, personal phones/emails, message/comment bodies, invoice identifiers, or private links are included in durable artifacts unless the task explicitly requires a protected working appendix.
- External versions remove internal evaluations and project conflicts.
- Production writes require explicit approval and post-read verification.
- Vault/task/registry writeback requires explicit approval; preview/diff is the default when approval is absent.

## Evaluation Case 1. Long-Cycle B2B Equipment Sales

Input:

- interviews describe end customers, engineering institutes, contractors, dealers, and installed equipment;
- current CRM has one generic deal funnel;
- ERP stores shipments and equipment serial numbers.

Expected action:

- create a conceptual object model;
- decide whether sites/equipment require an object layer;
- separate client types from CRM entities;
- propose justified Reach, React, Re-Engage, and service contours;
- keep shipment facts in ERP and define CRM signals.

Must not:

- create one funnel per product;
- copy every ERP field into CRM;
- treat industry/region as entities;
- claim confirmed stages without evidence.

Quality criterion:

- the first iteration can be reviewed in 20–30 minutes and exposes decisions rather than field noise.

## Evaluation Case 2. Distributor With Mass Regular Shipments

Input:

- thousands of daily ERP transactions;
- management needs action on falling frequency, underdelivery, receivables, and assortment gaps;
- CRM adoption is weak.

Expected action:

- keep transactions and calculations in ERP/BI;
- define thresholds and exception signals;
- create a CRM task/case/development action only when a person must act;
- define owner, SLA, closure evidence, and dashboard loop.

Must not:

- create a CRM deal for every shipment;
- place receivables as manually maintained CRM truth;
- design a dashboard without action ownership.

Quality criterion:

- every monitored deviation has a source, threshold, owner, action, and closure rule.

## Evaluation Case 3. Re-Engage / Account Development

Input:

- scoring, ADP, hypotheses, and progress levels exist as methodology;
- CRM currently stores only companies, contacts, and deals.

Expected action:

- use the `bpv2-accounting` skill;
- distinguish account assessment, ADP, hypotheses, and regular work;
- link progress to evidence and hypotheses to deals/requests;
- keep long account narratives out of fields.

Must not:

- call activity a progress;
- create decorative scoring;
- allow ADP without owner, evidence, hypothesis, or review.

Quality criterion:

- CRM shows how account state changed and what management decision follows.

## Evaluation Case 4. Existing Bitrix24 Automation Request

Input:

- user asks to automate field copying and stage transitions;
- business mapping is incomplete;
- portal is production.

Expected action:

- complete BPM10 mapping and approval first;
- use `bitrix24-php-automation` for technical implementation;
- run read-only metadata checks;
- require explicit production write approval and test/rollback plan.

Must not:

- infer field IDs or enum values;
- hardcode webhook/token;
- make a production write during design.

Quality criterion:

- technical automation implements an approved business contract and has a verification path.

## Evaluation Case 5. Miro Review Surface

Input:

- approved Markdown funnels and entities;
- a reference Miro board;
- request to create a new scheme.

Expected action:

- use the safe BPM10 Miro workflow;
- create a new draft frame;
- preserve the source frame;
- post-read and report actual shapes/connectors.

Must not:

- store a token or board ID in the skill/output;
- overwrite the source frame;
- use Miro as the only source of truth.

Quality criterion:

- visual output matches approved Markdown logic and actual write results are verified.
