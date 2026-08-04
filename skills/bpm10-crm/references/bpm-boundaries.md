# BPM10 Boundaries And Handoffs

## Boundary Rule

BPM10 designs the client-commercial control contour in CRM. It consumes evidence and models from adjacent BPMs but must not absorb their full scope.

| Contour | Owns | Gives BPM10 | BPM10 returns |
|---|---|---|---|
| BPM2: employee interviews | Organizational facts, role conflicts, current workarounds | Evidence, roles, problems, current process | Questions, role/data conflicts, design hypotheses |
| BPM3: customer interviews | Buying process, roles, criteria, reasons to win/lose | Customer journey evidence and qualification criteria | CRM capture requirements and validation questions |
| BPM4: database and profit analysis | Revenue, activity, product/client economics, deviations | Segments, signals, thresholds, potential, regular transaction facts | CRM actions, ownership, tasks, and required event feeds |
| BPM6: desk and competitor analysis | Public market and competitor evidence | Account/company attributes, triggers, competitor context | Required CRM classifiers and research return packets |
| BPM8: business processes | End-to-end activities, decisions, roles, inputs, outputs | Approved process logic and ownership | CRM implementation of selected control points, stages, tasks, and signals |
| BPM10: CRM analysis | Client-commercial objects, lifecycles, stages, fields, actions, signals, governance | — | CRM architecture and integrator package |
| BPM11: target data model | Enterprise objects, events, semantics, ownership, quality, systems of record | Canonical objects, relations, events, identifiers, data owners | CRM-specific projection, fields, links, and lifecycle requirements |
| BPV2: accounting / current-client development | Scoring, ADP, progress, hypotheses, portfolio control | Re-Engage rules and evidence requirements | CRM entities, smart processes, fields, transitions, and automation requirements |
| ERP / accounting | Orders, shipments, invoices, debt, prices, cost, legal/accounting facts | Confirmed facts and deviations | Status requests, links, and action signals; not duplicate transactions |
| BI / dashboard | Calculations, aggregations, monitoring | Exceptions, thresholds, slices, root-cause signals | Owner, task/deal/case, next action, and closure evidence |
| Service system | Incidents, SLA, support activities | Service signals and status | Customer context, commercial opportunity, and escalation route |

## BPM8 / BPM10 Test

Keep an element in BPM8 when it describes how work is performed across roles and systems. Move its CRM projection into BPM10 only when CRM must control a card, state, action, owner, communication, or transition.

Do not turn every process step into a CRM stage. A stage must represent a management-relevant state with an observable output.

## BPM11 / BPM10 Test

Keep an element in BPM11 when it defines the enterprise object, event, identifier, semantic rule, system of record, or data quality ownership.

Move it into BPM10 when the CRM user must see, edit, filter, route, automate, link, or report it. CRM may hold a projection rather than the master record.

## BPM4 / BPM10 Test

Keep mass transactions and calculations in ERP/BI. Send an event to CRM only when a person must make a decision or perform a customer-related action.

Examples:

- shipment remains in ERP; missing shipment creates a CRM signal;
- receivables remain in accounting/BI; a threshold breach creates a task or incident;
- product/client potential is calculated in BI; an approved opportunity becomes a deal or ADP hypothesis;
- regular sales history remains in the warehouse; decline in frequency creates a Re-Engage action.

## BPV2 / BPM10 Test

BPV2 owns the method of developing a current client. BPM10 owns how the method becomes controllable in CRM.

Do not store full account narratives, equipment maps, PowerMaps, or long plans as fields. Store management states, owners, evidence links, progress, hypotheses, next decisions, and linked commercial objects.

## Implementation Handoff

Use `bitrix24-php-automation` only after BPM10 has approved objects, field types, mappings, automations, and rollback/check logic. Technical automation must not decide the business architecture.

Use the BPM10 Miro workflow only after approved Markdown logic exists. Miro is a review surface, not the source of truth.
