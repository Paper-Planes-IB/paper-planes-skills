# Competitor КП QA Matrix

Use this reference when the task requires a structured packet, several competitor КП, a comparison matrix, slide-ready evidence, or ClickUp/BPM backlog transfer.

## 1. Source Register

| field | meaning |
| --- | --- |
| `source_id` | stable source id, e.g. `TZ-001`, `KP-AVISTA-001` |
| `source_type` | ТЗ / competitor КП / revised КП / email / call note / CRM / SAVA КП |
| `source_owner` | customer / competitor / SAVA / agent inference |
| `date` | document date or received date |
| `scenario` | controlled mystery scenario / real inquiry / tender / other |
| `rights` | internal-only / client-shareable / public / unknown |
| `limitations` | missing pages, oral terms, outdated date, extraction issue, unclear scope |

## 2. ТЗ Baseline

| baseline block | fields to normalize |
| --- | --- |
| Object | name, capacity, floor count, geometry, location, climate, intended use |
| Scope | design, manufacturing, foundation, delivery, installation, commissioning, furniture/equipment, documents |
| Technical | constructive scheme, fire class, load, insulation, engineering systems, standards, certificates, SRO |
| Site responsibilities | what customer provides: power, crane, lift, accommodation, food, storage, waste, security |
| Commercial | requested deadline, warranty, payment assumptions if present, required options |
| Contradictions | outdated dates, conflicting specs, unclear units, impossible terms |

## 3. Scope Completeness Matrix

Statuses:

- `included` — explicitly included in КП.
- `excluded` — explicitly excluded or customer responsibility.
- `optional` — priced or offered as option.
- `unclear` — not mentioned or ambiguous.
- `substituted` — competitor proposes different solution.
- `non_compliant` — contradicts ТЗ.

| requirement | ТЗ baseline | competitor КП status | evidence / quote short | commercial effect | risk |
| --- | --- | --- | --- | --- | --- |
| Working documentation | required sections | included / unclear / etc. | locator | included cost / potential add-on | low/medium/high |
| Foundation | required | status | locator | effect | risk |
| Delivery to site | required | status | locator | effect | risk |
| Installation / PNR | required | status | locator | effect | risk |
| Furniture/equipment | required list | status | locator | effect | risk |
| Certificates / SRO | required | status | locator | effect | risk |

## 4. Delivered-Cost Normalization

Never compare proposal headline prices until this table is filled enough to show comparability.

| component | КП price includes? | if excluded/unclear | normalization action | confidence |
| --- | --- | --- | --- | --- |
| Base building | yes/no/unclear | amount or missing | keep/add/request | A/B/C/D |
| Design / RD | yes/no/unclear | missing | add/request | A/B/C/D |
| Foundation | yes/no/unclear | missing | add/request | A/B/C/D |
| Delivery | yes/no/unclear | location terms | add/request | A/B/C/D |
| Installation | yes/no/unclear | crew resources | add/request | A/B/C/D |
| Customer-provided crane/lift/food/accommodation | yes/no/unclear | rates/assumptions | add/request | A/B/C/D |
| Furniture/equipment | yes/no/unclear | exclusions | add/request | A/B/C/D |
| Warranty/service | yes/no/unclear | risk | add/request | A/B/C/D |

Verdict options:

- `headline_price_comparable`
- `headline_price_misleading`
- `delivered_cost_lower`
- `delivered_cost_higher`
- `delivered_cost_unknown`

## 5. Technical Compliance QA

| requirement class | check | status | evidence | next question |
| --- | --- | --- | --- | --- |
| Fire safety | fire resistance, class, AПС/СОУЭ | compliant / partial / missing / non-compliant | locator | question |
| Climate/load | region loads, heat calculation, insulation | status | locator | question |
| Constructive | module/panel scheme, frame, foundation interface | status | locator | question |
| Engineering | ЭОМ/ВК/ОВ/АПС/ТМ scope | status | locator | question |
| Documentation | passport, calculations, certificates, SRO | status | locator | question |
| Warranty | construct, finishing, networks, installation | status | locator | question |

## 6. Sales Motion QA

| sales behavior | evidence | interpretation | BPM route |
| --- | --- | --- | --- |
| response speed | date/time if known | speed advantage / lag / unknown | BPM-10 |
| qualification questions | list | consultative sale / template sale | BPM-10 |
| engineering involvement | named role / technical annex / calculations | stronger risk reduction | BPM-8/BPM-10 |
| assumptions and exclusions | visible / hidden | buyer risk | BPM-4/BPM-10 |
| next step | call / site survey / revised КП / contract | funnel maturity | BPM-10 |
| follow-up | yes/no | sales discipline | BPM-10 |

## 7. Proposal Quality QA

| lens | strong signal | weak signal |
| --- | --- | --- |
| Task diagnosis | КП restates and interprets ТЗ/job | generic price list |
| Fit explanation | explains why chosen constructive/scope fits | no rationale |
| Risk removal | flags assumptions, site constraints, schedule dependencies | hides exclusions |
| Buyer enablement | helps defend purchase internally with proof, options, documents | forces buyer to infer |
| Evidence | cases, certificates, calculations, photos, production proof | unsupported claims |
| Decision route | clear next steps and required inputs | "call us" only |

## 8. Fair Battlecard

Use only source-backed points.

| player | where they win | where SAVA may win | when to concede | where not to fight | proof needed |
| --- | --- | --- | --- | --- | --- |
| competitor | claim + source | claim + source/gap | condition | condition | evidence needed |

Rules:

- Do not attack a competitor on an inferred weakness.
- Do not claim SAVA wins without SAVA evidence.
- A battlecard bullet without source/gap status stays `draft`.

## 9. BPM Transfer

| finding | source trace | status | target BPM | needed evidence | what strengthens | what weakens | return destination |
| --- | --- | --- | --- | --- | --- | --- | --- |
| delivered cost gap | КП + ТЗ | evidence-debt / strengthened / contradicted | BPM-4 | normalized economics | signal | falsifier | Storyline/BPV/task |
| competitor sales motion | КП/email | field signal | BPM-10 | CRM/funnel/win-loss | signal | falsifier | CRM fields/backlog |
| product/region fit | КП + ТЗ | hypothesis | BPM-7B | product × region data | signal | falsifier | heatmap |
| public claim mismatch | КП vs website | contradiction/needs check | BPM-6 | public/field sources | signal | falsifier | competitor map |

## 10. SAVA КП Improvement Backlog

| improvement | why it matters | source evidence | owner route | status |
| --- | --- | --- | --- | --- |
| Make exclusions explicit | prevents misleading price comparison | competitor КП / ТЗ | КП owner / MPP | candidate |
| Add delivered-cost block | protects from headline-price demпинг | normalized matrix | BPM-4/BPV-03.7 | candidate |
| Add buyer-risk appendix | helps internal defense | competitor stronger signal | BPV-03.7 | candidate |

Do not convert backlog into execution tasks unless Ilya explicitly asks for task creation or writeback.
