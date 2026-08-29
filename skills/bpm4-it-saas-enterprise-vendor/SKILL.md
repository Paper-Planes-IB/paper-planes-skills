---
name: bpm4-it-saas-enterprise-vendor
description: Use when working with BPM-4 Formula Profit for IT, SaaS, cybersecurity, enterprise software vendors, CRM opportunity slices, renewals, support, licenses, subscriptions, implementation services, product anchors, variable pricing basis, protected-scope economics, or DataLens-ready dashboard handoff.
metadata:
  version: "0.1.0"
  status: active
  line: BPM-4 / IT SaaS enterprise vendor
  owner: Ilya
  supports_bpm:
    primary: [BPM-4]
    required_secondary: [BPM-10, BPM-11]
    optional_secondary: [BPM-2, BPM-3, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9]
  can_consume: [CRM opportunity exports, license / renewal / support / subscription data, partner / source / win-loss signals, BPM Storyline-Storyboard, Матрица BPM — SI]
  can_produce: [revenue stream normalizer, protected-scope economics map, Formula Profit decomposition, DataLens-ready implementation handoff, commercial data-gap packet, SI / SIF candidates, Storyline-Storyboard writeback proposal]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-05-28: Added handoff to bpm4-datalens-dashboard after IT/SaaS stream normalization."
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# Skill BPM 4 IT SaaS Enterprise Vendor

## Purpose

Use this skill to handle BPM-4 work for IT / SaaS / enterprise software vendors, especially when revenue is a mix of new licenses, renewals, support, subscriptions, professional services, partner-led deals, pilots, and product anchors.

This skill does not replace the BPM-4 canon. It is an industry / business-model layer for cases where classic ARPU is too narrow because pricing may be per seat, per machine, per server, per certificate, per account, per system, or flat fee.

Canonical Vault home:

`Vault/10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPM — Майнинг/OPM/EXEC/BPM-4/README.md`

## Scope Lock

Use for:

- enterprise IT / SaaS / cybersecurity vendors;
- B2B software with long sales cycles, pilots, budgeting, procurement, channel partners, implementation, support, and renewals;
- CRM / opportunity exports that show account, deal title, stage, owner, industry, product hints, renewal/support hints, or partner/source hints;
- Formula Profit design where the first job is to normalize incomplete commercial data before calculating.

Do not use as-is for:

- self-serve PLG SaaS where user-level ARPU / trial conversion is the main economic engine;
- industrial B2B distribution / SKU / warehouse / shipment dashboards; use `bpm4-b2b-dashboard-industrial-distribution`;
- generic financial reporting without commercial decomposition.

## Core Principle

Do not force everything into ARPU.

For enterprise IT / cybersecurity, the main economic unit is often not a user. Normalize pricing to a protected or deployed scope:

`contract value -> protected scope -> normalized license set value`

ARPU may remain a reference metric, but the working BPM-4 measure is usually:

`average protected set value = contract value / normalized protected scope`

## Revenue Streams

Split streams through plus, then calculate each stream with its own driver logic:

| Stream | Meaning | Common missing fields |
|---|---|---|
| New sale / new license | first sale, new module, new account, or new protected scope | amount, close date, product, scope, discount, source |
| Renewal | renewal of installed base, updates, annual contract continuation | installed base, renewal value, churn/loss reason, term |
| Support / maintenance | support attached to license or installed base | support revenue, attach rate, support cost |
| Subscription / cloud / service | recurring SaaS or managed service | ARR/MRR, term, start/end dates, churn, hosting COGS |
| Implementation / professional services | deployment, integration, migration, customization, training | effort, internal/partner cost, margin, capacity |
| Expansion | upsell, cross-sell, added module, larger protected scope | source anchor, expansion product, expansion value |

## Normalized License Set

When pricing basis varies, create a normalizer instead of treating price names as truth.

| Pricing basis | Normalize to |
|---|---|
| Per seat / user | protected users or accounts |
| Per machine / server | protected machines, hosts, servers, target systems |
| Per certificate / token / key | protected technical identities or credential objects |
| Per connector / integration | protected systems or data sources |
| Flat fee | protected scope covered by the contract |
| Bundle / platform | license set by product anchors and protected scope |

For each opportunity, try to capture:

- account;
- revenue stream;
- product anchor;
- pricing basis;
- protected scope quantity;
- contract value;
- discount / partner adjustment;
- implementation and support components;
- term and renewal date.

If the source lacks quantities, mark it as `BPM-4 partial input` and produce a missing-field request rather than delaying the analysis.

## Product Anchor Logic

Treat product anchors as commercial entry points, not just SKUs.

Examples:

- PAM-first;
- AM / MFA-first;
- CM / PKI-first;
- ITDR-first;
- BearPass / secrets-first;
- IdM / governance-first;
- platform / bundle.

For every anchor, ask:

1. What protected scope does it cover?
2. What pricing basis is used?
3. What adjacent products can expand it?
4. Is expansion visible in CRM, invoices, support data, or only hypothesized?
5. Does the deal prove platform synergy, or only a bundle?

## Formula Profit Skeleton

Use this as the first-pass commercial skeleton:

```text
Revenue =
  New license / new protected sets
+ Renewal of installed protected sets
+ Support / maintenance attached to installed sets
+ Subscription / cloud / managed service
+ Implementation / professional services
+ Expansion into adjacent products or added protected scope
```

Driver view:

```text
Stream value =
  # accounts or opportunities
× conversion / renewal / expansion rate
× average protected scope
× average protected set value
× discount / partner / procurement adjustment
```

Cost view:

```text
Economic contribution =
  stream value
- implementation / delivery cost
- support cost
- hosting / infrastructure COGS where applicable
- partner margin / discount leakage
- CAC / presale / pilot cost where available
```

## Data Triage Workflow

1. Identify source type.
   CRM opportunity, invoice, contract, P&L, support registry, product usage, partner lead, pilot report, implementation estimate, or mixed source.

2. Split revenue streams.
   Never mix new sale, renewal, support, subscription, implementation, and expansion in one undifferentiated average.

3. Normalize pricing basis.
   Convert per-seat, per-machine, per-certificate, per-system, and flat-fee deals into protected scope and average protected set value where possible.

4. Map product anchors.
   Extract product family from explicit fields first, then from title text only as a marked inference.

5. Separate license from services.
   If the deal bundles license, implementation, support, customization, or partner services, mark the mixed bundle and request decomposition.

6. Build missing-field backlog.
   Required fields usually include amount, dates, probability, product field, pricing basis, protected scope quantity, discount, partner/source, support revenue, implementation cost, margin, win/loss reason, and renewal date.

7. Route downstream.
   BPM-4 owns numeric baseline and Formula Profit logic. BPM-10 / BPM-11 own CRM/data-model gaps. BPM-8 owns stage/process interpretation. Storyline-Storyboard receives storyline, slide, and evidence implications.

8. Hand off DataLens implementation when needed.
   If the target output is a Yandex DataLens dashboard, keep this skill responsible for IT/SaaS semantics: stream separation, protected-scope normalizer, product anchors, license/service/support split, partner/discount interpretation, and missing-field backlog. Use `bpm4-datalens-dashboard` for SQL-view/dataset execution, chart layout, controls, click-to-filter, scatter stabilization, save/publish cycle, browser QA, and post-publish delta.

   Before handoff, provide:
   - agreed Formula Profit by revenue streams;
   - account/opportunity/contract grain and date basis;
   - stream fields: new sale, renewal, support, subscription, implementation, expansion;
   - product anchor and pricing-basis fields or marked inference rules;
   - control slice for period, currency, product family / stream, and key totals;
   - explicit fields that are missing and must not be inferred into client-facing claims.

## Completion Checks

- Scope lock says IT / SaaS / enterprise vendor, not generic SaaS or distribution.
- Revenue streams are separated through plus.
- ARPU is not used as the only primary metric unless the business is truly user-subscription based.
- Variable pricing basis is normalized to protected scope / license set.
- Product anchors are treated as entry points and expansion paths.
- Implementation, support, partner margin, discount, and hosting COGS are not silently folded into license value.
- Missing fields are named explicitly when the source is partial.
- If DataLens is the target, `bpm4-datalens-dashboard` is applied only after stream and protected-scope normalization, or an explicit no-op reason is recorded.
- BPM Storyline-Storyboard is updated or a no-op reason is recorded when the source changes project hypotheses.

## Structured Analytical Artifact Gate

Revenue-stream classifications, product-anchor maps, protected-scope metric trees, dashboard dimensions, evidence tables, analytical visuals, and Storyline-Storyboard deltas inherit the global contract in `~/.codex/AGENTS.md`. State scope, grain, recurring/non-recurring rule, multi-label boundary, residual, Formula Profit source, physical CRM/finance evidence, and decision. Do not call overlapping license/service/support streams strictly MECE, and do not use Frappe or methodology pages to repair missing client data.
