# OrtoLight CRM/BPV Standard

This reference captures the reusable part of the OrtoLight CRM package. Use it as a donor pattern, not as a client-fact source for other projects.

## Transferable Pattern

The reusable sequence is:

`interviews -> management requirements -> conceptual data model -> entity cards -> funnels -> automations -> integrations -> normalization / deduplication -> migration gate -> marketing pilot -> sales pilot -> full launch`.

## Core Insight

A CRM implementation package is not ready because it contains many fields and process names. It is ready only when it connects management decisions, user roles, system boundaries, data quality, automations, integrations, and launch acceptance.

## Medical / B2B Distribution Checks

Always separate:

- doctor as demand creator and practitioner;
- clinic / workplace as operating context;
- legal counterparty / payer as accounting object;
- order contact as operational contact;
- dealer as channel intermediary;
- manager as commercial owner;
- marketing / academy as signal source;
- customer service as service and recovery role.

Weak duplicate signals are not enough to merge objects: same name, shared phone, shared email, same clinic, same date, similar product name, same amount, or recurring event name.

## Loyalty And Progress

Keep manager actions, confirmed customer results, loyalty points, and segment status separate. A completed task does not automatically prove customer progress. Loyalty currency and ordinary discounts require separate analytics even when technically represented as discount in an order system.

## Pilot Acceptance

A plan must state who pilots, what scenarios are tested, what data must already be migrated, which integrations must work, what failures stop the rollout, and who signs off the next stage.

## Skill Delta Candidates

- `bpm10-crm`: link to package QA, entity-role collision gate, CRM/BPV routing, data-quality and pilot acceptance gates.
- BPM-4 skills: add doctor/clinic potential, loyalty ledger, segment engine, lost demand gaps only after a data-backed example.
- Dedicated `crm-implementation-qa`: use when the package contains multiple implementation layers and needs a pre-handoff verdict.
