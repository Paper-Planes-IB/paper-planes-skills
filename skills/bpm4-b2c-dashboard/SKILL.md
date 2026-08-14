---
name: bpm4-b2c-dashboard
description: "Use when designing, adapting, reviewing, or packaging a BPM-4 B2C dashboard: transaction data contract, profit formula, repeat purchases, RFM, cohorts, customer clusters, anonymization, and acceptance checks."
metadata:
  version: "0.1.0"
  status: active
  line: BPM-4 / B2C dashboard package
  owner: Paper Planes
  supports_bpm:
    primary: [BPM-4]
    optional_secondary: [BPM-2, BPM-3, BPM-7A, BPM-10]
  can_consume: [transaction exports, customer exports, order line exports, retail or service dashboard brief, anonymized sample data, existing BPM-4 package]
  can_produce: [B2C dashboard requirements, data contract, metric dictionary, anonymization rules, RFM and repeat-purchase logic, QA checklist, dashboard blueprint]
  references:
    - references/README.md
    - references/requirements_audit.md
    - references/b2c_data_contract.md
    - references/sample_schema.csv
    - references/b2c_dashboard_blueprint.md
    - references/metric_dictionary.md
    - references/segmentation_and_rfm.md
    - references/anonymization_rules.md
    - references/acceptance_checklist.md
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-14: Created anonymized B2C dashboard package from the ABIS BPM-4 package audit."
---

# BPM-4 B2C Dashboard

## Purpose

Use this skill to build or check a reusable B2C dashboard package based on BPM-4. It covers the data contract, Formula Profit, repeat purchases, RFM, cohorts, customer clustering, anonymization, and acceptance checks.

The skill is intended for B2C transaction models: retail, e-commerce, services, HoReCa, and other businesses where the core grain is a purchase, order, visit, ticket, or receipt.

## When To Use

Use this skill when the task mentions:

- B2C dashboard, retail dashboard, customer-base dashboard, Formula Profit for B2C;
- repeat purchases, retention, frequency, days to second purchase;
- RFM, customer segmentation, customer clusters, cohorts;
- anonymized dashboard package or reusable dashboard template;
- transaction exports with orders, order lines, products, stores, channels, and customers;
- adapting a client-specific BPM-4 dashboard package into a generic B2C package.

Do not use this skill as the primary path for:

- B2B dealer or partner dashboards;
- medical clinic economics where patient-flow semantics are primary;
- SaaS renewal dashboards;
- DataLens implementation after the semantic layer is already agreed.

Use the adjacent specialist skill for those cases, then return here only for reusable B2C package logic if needed.

## Required References

Before designing or reviewing a B2C dashboard package, read:

1. `references/b2c_data_contract.md`
2. `references/metric_dictionary.md`
3. `references/segmentation_and_rfm.md`
4. `references/anonymization_rules.md`
5. `references/acceptance_checklist.md`

If the task is an audit of an existing package, also read `references/requirements_audit.md`.

If the task is a dashboard blueprint, also read `references/b2c_dashboard_blueprint.md`.

## Preflight

Before producing recommendations or files, state:

```yaml
bpm4_b2c_dashboard_preflight:
  source_package: string|null
  business_model: retail | ecommerce | services | horeca | mixed | unknown
  source_data_status: real_data | sample_data | no_data | unknown
  anonymization_status: verified | partial | missing | unknown
  customer_key_status: stable | unstable | missing | unknown
  partner_registry_status: verified | partial | missing | not_applicable | unknown
  data_grain:
    orders: available | missing | unknown
    order_items: available | missing | unknown
    customers: available | missing | unknown
    stores_or_channels: available | missing | unknown
  required_outputs: []
  blockers: []
```

Rules:

- Do not build RFM before resolving `customer_key_status` and partner/B2B exclusion.
- Do not treat legal entities as a clean B2C audience automatically.
- Do not expose personal fields in examples, screenshots, schemas, or package names.
- Do not call a dashboard package complete until the acceptance checklist has a pass/fail status.

## Build Order

1. Inventory source exports and identify fact grain.
2. Normalize IDs: orders, customers, stores, products, order lines.
3. Remove or flag internal, test, employee, B2B, and partner transactions.
4. Verify the B2C audience with a partner registry before RFM.
5. Check totals: revenue, checks, order lines, customers, discounts, returns, gross profit.
6. Build Formula Profit.
7. Build repeat-purchase metrics.
8. Build RFM and customer-base states.
9. Build cohorts.
10. Run clustering only if data volume and quality are sufficient.
11. Build product, category, brand, channel, and store views.
12. Add a data-quality view.
13. Run the acceptance checklist.
14. Package outputs as text-first reusable materials.

## Core Dashboard Structure

The recommended B2C dashboard sequence is:

```text
1. Business overview
2. Revenue and Formula Profit
3. Customer base
4. Repeat purchases
5. RFM and clusters
6. Cohorts
7. Products, categories, brands
8. Channels and stores
9. Data quality
```

Use `references/b2c_dashboard_blueprint.md` for the detailed block list.

## Data Contract Rules

Minimum tables:

- `orders`;
- `order_items`;
- `customers`;
- `stores`;
- `partner_registry`.

Use `references/b2c_data_contract.md` and `references/sample_schema.csv` as the default request structure.

Mandatory flags:

- `is_internal`;
- `is_test`;
- `is_b2b_or_partner`;
- `is_partner`;
- `is_employee`;
- `exclude_from_b2c_rfm`.

## Metrics

Use `references/metric_dictionary.md` as the source of metric definitions.

Do not redefine core metrics casually. If the client uses a different accounting rule, write the difference explicitly and keep both the source rule and dashboard rule visible.

## Repeat Purchases

Minimum repeat-purchase outputs:

- customers with 2+ purchases;
- repeat rate;
- purchase count distribution;
- days to second purchase;
- repeat by first-purchase category;
- repeat by acquisition channel;
- repeat in 30, 60, and 90 days where the period supports it.

## RFM And Clusters

RFM is calculated only for identified B2C customers after exclusions.

Customer clustering is optional and should run only when:

- there are at least 1,000 identified customers;
- history covers at least 3 months;
- partner/B2B contamination is removed;
- RFM or behavioral fields are sufficiently variable.

Cluster names must describe business behavior rather than model numbers.

## Anonymization

Use `references/anonymization_rules.md`.

Never include:

- names;
- phones;
- emails;
- exact addresses;
- exact birth dates;
- free text fields that can contain personal data.

Use stable hashed IDs and aggregated demographics.

## Acceptance

Use `references/acceptance_checklist.md` before calling the package complete.

At minimum, verify:

- source totals;
- B2C exclusion logic;
- repeat-purchase calculations;
- RFM inputs and thresholds;
- cohort logic;
- anonymization;
- dashboard block completeness.

## Output Format

For an audit, return:

- status by requirement;
- gaps;
- risks;
- what to add.

For a reusable package, return:

- a ZIP or folder path;
- included files;
- what the package supports;
- known limits;
- validation performed.
