---
name: demand-supply-match-intelligence
description: "Use when Ilya asks to generate an external ChatGPT Pro / Perplexity / research-machine prompt, or ingest its return packet, for evaluating market opportunity, product-market fit, demand-supply fit, market cell, offer unit, supplier/customer fit, commercialization route, or whether a product, asset, technology, service, method, platform, capability, or client need has a real market match. Useful for BPM-7A/B, BPM-4 follow-up, product strategy, market entry, КП inputs, and opportunity screening."
metadata:
  status: experimental
  line: research / market intelligence / BPM-7B / product-market fit / 4-ka / 5-ka / 2-ka
  owner: Ilya
  originator: Илья Балахнин
  source: "created from external SKILL (1).md and normalized into Ilya's local Codex skill standard"
---

# Demand-Supply Match Intelligence

## Purpose

Use this skill to evaluate whether a concrete offer unit matches a concrete market cell, client job, route to market, and commercialization logic.

Core chain:

```text
offer unit -> market cell -> client job -> required function -> evidence -> value chain -> route -> confidence -> decision gate -> next action
```

Never evaluate an opportunity "in general". One offer unit can be strong in one market cell, weak in another, and irrelevant in a third.

## Primary Codex Behavior

By default, Codex must not execute the full demand-supply research itself.

Codex's primary job is to:

1. run internal preflight and collect DLP-safe context;
2. clarify input side, decision use, market boundaries, and missing inputs;
3. build a precise outbound prompt for ChatGPT Pro, Perplexity, or another external research machine;
4. require the external machine to return a structured demand-supply match packet with sources, confidence, data gaps, and self-reflection;
5. later process the returned answer through `return-packet-ingest` mode.

Codex may execute the analysis locally only if Ilya explicitly says something like `делай здесь`, `исполни сам в Codex`, `не отправляем наружу`, or gives an equivalent direct instruction.

If Ilya says `dry run`, `префлайт`, `сгенерируй запрос`, `запрос для GPT Pro`, `запрос для Perplexity`, or similar, the output is an outbound prompt, not a completed demand-supply analysis.

## Anti-sprawl Decision

```yaml
anti_sprawl_decision:
  proposed_new_skill: "demand-supply-match-intelligence"
  decision: "create_after_approval"
  existing_skill_to_extend: "deepresearch / competitor-research / sector-service-matrix-builder"
  reason: "Demand-supply fit has a standalone repeated trigger, two-sided market-cell schema, confidence gates, and commercialization-route output that would make adjacent skills too broad."
  approval_required: true
  approval_status: "approved by Ilya in chat"
  originator_trace: "Илья Балахнин / мои скиллы / APQ-23"
```

## Non-goals

This skill must not:

- replace `deepresearch` for broad evidence gathering;
- replace `competitor-research` for competitor intelligence;
- replace `bpm4-b2b-dashboard-industrial-distribution` or BPM-4 analysis;
- pretend that public demand signals equal paying demand;
- pretend that an available supply unit creates a business opportunity by itself;
- produce client-facing claims without evidence calibration;
- write to Vault, CORD, Reader, Notion, slides, КП, APQ, rules, or skills without Ilya's approval;
- send sensitive internal/client data to ChatGPT Pro, Perplexity, or another external model without DLP review.

## Trigger Conditions

Use this skill when Ilya asks:

- "есть ли здесь рынок";
- "проверь opportunity";
- "сопоставь спрос и предложение";
- "есть продукт / технология / актив, кому это нужно";
- "есть клиентская боль, чем её закрывать";
- "оценить market fit / product-market fit";
- "понять маршрут коммерциализации";
- "выбрать рыночную ячейку";
- "проверить новый бизнес / направление / продукт";
- "сделать screening гипотез";
- "BPM-7A / BPM-7B / market entry / opportunity map".

Do not use this skill when:

- the task is only a competitor map: use `competitor-research`;
- the task is a general deep research prompt: use `deepresearch`;
- the task is one-client meeting context: use `client-info`;
- the task is writing КП: use `commercial-proposal-generator`, with this skill as evidence input;
- the task is pure strategy lever design without a market-cell check: use `leverage-builder`.

## Inputs

Minimum:

- input signal: offer unit, demand signal, market need, product, asset, supplier, technology, capability, trend, or hypothesis;
- geography / market boundary;
- decision use: strategy, КП, market entry, product, investment, partner route, BPM, content, monitoring;
- known constraints and sensitive data rules.

Useful optional inputs:

- target company / client / segment;
- known offer units;
- known customer jobs / pains;
- known market cells;
- beneficiary strategy context: strategic horizon, growth bets, right-to-win, non-goals, asset model, delivery constraints, target client archetype, route-to-market constraints;
- internal data: CRM, sales, win-loss, support, margins, production, capacity, channels, brand constraints;
- external sources or prior research;
- competitor/benchmark context;
- BPM status: BPM-4, BPM-6, BPM-7A, BPM-7B, BPM-10;
- timebox and required confidence level.

If inputs are missing, do not invent them. Either ask, mark `missing`, or run an early screening with lower confidence.

## Mode Router

| Mode | Trigger | Output |
|---|---|---|
| `supply-led` | Offer unit exists; demand is unclear | market-cell candidates + demand tests |
| `demand-led` | Client job / pain / market need exists; offer is unclear | possible offer units + supply tests |
| `two-sided-fit` | Both offer and demand are known | fit matrix + route recommendation |
| `portfolio-screening` | Many offer units or many market cells | ranked opportunity portfolio |
| `bpm-7b-market-cell` | Product / industry / region prioritization | BPM-7B market-cell analysis |
| `bpm-7a-sizing-support` | Market size matters | sizing assumptions + data gaps, not full sizing if data missing |
| `outbound-prompt` | default mode; Ilya wants ChatGPT Pro / Perplexity / external research machine / dry run / preflight | ready-to-paste external prompt with DLP-safe context |
| `return-packet-ingest` | Ilya brings back an external answer | accepted/change/defer/reject + improvement suggestions + writeback candidates after approval |
| `local-execution` | only when Ilya explicitly asks Codex to execute here | completed local demand-supply packet |

## BPM / Rail Positioning

This skill is usually a bridge between:

- `BPM-4`: internal data, economics, CRM, margins, repeat demand;
- `BPM-6`: competitor / desk research;
- `BPM-7A`: market sizing and opportunity pool;
- `BPM-7B`: product / industry / region market-cell prioritization;
- `BPM-10`: CRM / funnel / route evidence;
- `commercial rail`: КП argument, sales play, partner route;
- `content/product rail`: product showcase, market narrative, case or article;
- `8-ka`: reusable pattern if the opportunity logic becomes methodological.

Early external research is allowed before BPM-4 exists. But confidence must stay limited until local or internal data confirms demand, economics, route, or repeatability.

If BPM-4 later becomes clearly completed, remind Ilya that the demand-supply conclusion can be upgraded with CRM / sales / win-loss / support / margin / SKU data.

## Data Types

Each fact, gap, and conclusion must have a data type.

| Type | Meaning | Decision use |
|---|---|---|
| `direct_public_source` | regulator, report, registry, supplier site, patent, documentation, tender | usable if fresh and applicable |
| `indirect_public_signal` | analogs, reviews, jobs, news, assortments, marketplaces, mentions | early screening only |
| `partially_open_data` | public data answers only part of the question | preliminary proof |
| `internal_data_needed` | sales, CRM, clients, procurement, production, finance, channel, brand, support | decision limited until loaded |
| `external_data_needed` | interviews, commercial offers, expert calls, field checks, paid bases | decision after collection |
| `expert_interpretation` | expert reading over facts | valid only if separated from fact |
| `invalid_general_question` | question too broad; must be reformulated by market cell | no decision |

## Workflow

Default workflow for Codex is prompt construction, not full research execution.

1. **Frame signal and input side**
   - Determine whether the signal starts from demand, supply, both, or an unclear input.
   - Return a short signal card: source, side, initial hypothesis, decision use.

2. **Separate fact / inference / hypothesis**
   - Facts need sources.
   - Inferences need explicit reasoning.
   - Hypotheses need validation path.

3. **Define offer unit**
   - Product, service, method, technology, supplier, asset, team, data, format, platform, process, location, competence, or system.
   - Decompose into functions: price, quality, speed, risk, regulation, margin, access, convenience, new property, platform effect, brand, capacity.

4. **Build market cells**
   - Minimum formula: `segment -> application -> format -> channel -> geography -> customer type`.
   - Never evaluate only at total-market level.

5. **Evaluate demand in four layers**
   - visible end-customer demand;
   - category structure;
   - buyer / producer demand;
   - internal company demand / strategic fit.

6. **Evaluate beneficiary-strategy fit**
   - If a beneficiary organization is named, test whether each market cell strengthens or distracts from that organization's stated strategy.
   - Use only DLP-safe and explicitly provided strategic context in outbound prompts.
   - If strategy context is not provided, ask the external machine to return a `strategy_context_needed` section rather than guessing.
   - Evaluate whether the opportunity creates compounding assets, improves repeatability, strengthens right-to-win, fits delivery capacity, supports target client archetypes, and respects strategic non-goals.
   - Separate market attractiveness from beneficiary fit. A cell can be attractive in the market and still be wrong for the beneficiary.

7. **Score demand**
   - `D0`: no visible signals.
   - `D1`: logic or international analogs.
   - `D2`: local public signals.
   - `D3`: customers, interviews, requests, tenders, purchase signals.
   - `D4`: repeated confirmed demand and clear customer job.

8. **Evaluate supply**
   - availability, form, substitutes, specs, certificates, prices, lead times, minimum order, technical/legal/operating constraints, supplier resilience.

9. **Evaluate market structure**
   - If reliable shares exist, calculate HHI.
   - If shares do not exist, do not invent HHI. Use concentration level `C0-C4`.

10. **Apply 3/4 rule**
   - If 3-4 strong players control a capital-intensive category, selling to them may be better than entering directly.
   - If fragmented and testable, own product or direct route may be possible.
   - If both own product and partner route reinforce each other, consider synergy.
   - If data is weak, keep in observation or assign data loading.

11. **Assess value-chain attractiveness**
   - size/growth, repeatability, margin, implementation cost, switching cost, problem intensity, regulatory necessity, channel access, ability to retain value.

12. **Assess operating and asset consequences**
   - Check delivery burden, senior/expert bottlenecks, implementation complexity, margin risk, sales cycle, rework risk, handoff complexity, and support burden.
   - Identify assets created by the opportunity: case, reference, data, method, reusable process, training unit, productized offer, partner channel, content asset, code/tool, community, or knowledge unit.
   - Name anti-assets or strategic drag: one-off customization, low-margin delivery, reputation risk, hidden support load, channel dependency, unrepeatable founder/expert effort, or dilution of positioning.

13. **Choose commercialization route**
   - sell to large players;
   - own product;
   - partnership;
   - synergy;
   - licensing;
   - service / implementation;
   - observation;
   - archive.

14. **Grade evidence and confidence**
   - Evidence: `A` direct strong proof; `B` good source; `C` indirect signal; `D` unsupported hypothesis; `X` contradicted.
   - Confidence: `0.20`, `0.40`, `0.60`, `0.75`, `0.90`.

15. **Name data gaps and gates**
   - What question is open, why it matters, owner, how it changes decision, what raises confidence.

16. **Generate outbound prompt**
   - Unless Ilya explicitly requested local execution, stop after producing a ready-to-paste prompt for the external research machine.
   - The prompt must require the external machine to return the full output contract below.

17. **Return-packet ingest**
   - When Ilya brings back the external answer, classify accepted/change/defer/reject.
   - Extract candidate writebacks, data gaps, and skill improvement suggestions.
   - Do not write or canonicalize without approval.

18. **Return decision**
   - close, observe, desk check, interview, request terms, technical test, legal check, calculate economics, pilot, sales handoff, own product, partner route.

## Confidence Rules

- Do not raise confidence above `0.60` without local or internal data.
- Do not raise confidence above `0.75` without confirmed demand, confirmed supply, or credible economics.
- Do not recommend a pilot without demand, supply, legal risk, and economics checks.
- Do not use HHI without market shares.
- Do not present public visibility as paying demand.
- Do not present supply availability as profit potential.
- Do not treat a benchmark as proof of applicability.

## Output Contract

Return in Markdown.

Required structure:

1. Executive summary.
2. Signal card: input, side, source, decision use.
3. Fact / inference / hypothesis split.
4. Offer-unit function map.
5. Market-cell map.
6. Demand analysis: four layers and D-score.
7. Supply analysis.
8. Market structure: HHI or C0-C4.
9. 3/4 rule and category-control conclusion.
10. Value-chain attractiveness.
11. Beneficiary-strategy fit, if a beneficiary is named.
12. Operating burden and asset-conversion assessment.
13. Demand-supply fit matrix.
14. Evidence ledger.
15. Confidence index and caveats.
16. Data-gap backlog.
17. Commercialization route.
18. Decision gate and next action.
19. Self-reflection / improvement notes.

### Demand-Supply Fit Matrix

| Offer unit | Market cell | Input side | Customer job | Required function | Evidence | Evidence grade | Confidence | Route | Data gaps | Next step |
|---|---|---|---|---|---|---|---:|---|---|---|

### Beneficiary-Strategy Fit Matrix

Use this table when the opportunity has a named beneficiary organization.

| Market cell | Market attractiveness | Beneficiary fit | Strategic contribution | Strategic drag / non-goal risk | Asset created | Capacity / margin risk | Decision implication |
|---|---|---|---|---|---|---|---|

Do not assume that attractive market cells are good strategic cells for the beneficiary. If no strategy context is provided, mark `strategy_context_needed`.

### Client Archetype / Anti-Archetype

| Archetype | Why it fits | Evidence needed | Anti-archetype | Why to avoid |
|---|---|---|---|---|

### Asset-Conversion Check

| Opportunity | What reusable asset can be created | What makes it repeatable | What would make it one-off / non-scalable | Next asset gate |
|---|---|---|---|---|

### Data-Gap Backlog

| Question | Why it matters | Data type | Owner / route | Decision impact | What raises confidence |
|---|---|---|---|---|---|

### Decision Card

```yaml
decision_card:
  status: "close|observe|desk_check|interview|request_terms|technical_test|legal_check|economics_check|pilot|sales_handoff|own_product|partner_route"
  confidence: 0.60
  strongest_cell: ""
  weakest_assumption: ""
  strategy_context_needed: []
  strategic_fit: "strong|medium|weak|not_assessable"
  strategic_non_goal_risks: []
  asset_conversion_candidates: []
  operating_burden_risks: []
  required_data_before_next_gate: []
  client_facing_safe_claims: []
  internal_only_claims: []
  do_not_use_claims: []
  approval_required_before_writeback: true
```

## Outbound Prompt Mode

When building a prompt for ChatGPT Pro, Perplexity, or another external machine:

- provide only DLP-safe context;
- require Russian output unless Ilya asks otherwise;
- require Markdown, not raw YAML only;
- require source links and dates;
- require fact / inference / hypothesis split;
- require market-cell analysis, not total-market prose;
- require evidence grades and confidence caveats;
- require beneficiary-strategy fit when a beneficiary is named, but only from DLP-safe context supplied in the prompt;
- require the external machine to separate market attractiveness from beneficiary fit;
- require client archetype / anti-archetype and strategic non-goal risks when relevant;
- require operating burden and asset-conversion assessment;
- require self-reflection;
- require returned questions and data gaps;
- state that the external answer is advisory and must return to Codex/Ilya for review.
- produce one copyable prompt block; do not split required schema, self-reflection, or appendix into separate copy blocks.

Do not send:

- client names, economics, CRM data, win-loss, support data, internal strategy, commercial conditions, raw transcripts, or sensitive project context unless Ilya explicitly approves;
- confidential Paper Planes methodology;
- data that would reveal client pipeline, pricing, margins, or delivery risks.

## Return-Packet Ingest Mode

When Ilya brings back an external answer:

1. classify recommendations as `accepted / change / defer / reject`;
2. separate public facts, internal facts, inferences, and unsupported claims;
3. identify which market cells got stronger or weaker;
4. update confidence only if evidence quality improved;
5. extract data gaps and next gates;
6. treat self-reflection as suggestions for Ilya review, not automatic skill changes;
7. propose writeback candidates only after approval.

## Self-Reflection / Improvement Notes

Every full output must end with a short self-reflection:

1. What data was missing?
2. Where was the answer too general and not market-cell-specific?
3. Where did I over-rely on public signals?
4. Which claim is weakest?
5. Which internal data would most improve confidence?
6. What should not be used client-facing?
7. Did I confuse market attractiveness with beneficiary fit?
8. What strategic context was missing?
9. Which opportunity may create strategic drag even if demand exists?
10. What reusable asset, if any, could this opportunity create?
11. What should change in the next prompt or data request?

Self-reflection is an improvement backlog. Do not patch skills, rules, APQ, Vault, or automations from it without Ilya's explicit approval.

## Writeback / HITL Gates

Codex may:

- analyze the current chat and supplied files;
- produce a demand-supply packet;
- produce an external prompt;
- propose Vault / CORD / BPM / КП / content writeback candidates;
- suggest data requests and next gates.

Codex must ask Ilya before:

- creating or editing Vault files;
- updating project artifacts, SKILLS.md, APQ, rules, or other skills;
- creating CORD tasks;
- importing sources into Reader;
- sending prompts or findings externally with sensitive context;
- converting hypotheses into client-facing claims, КП text, deck claims, or strategy canon;
- launching pilots, interviews, mystery-shopping, supplier requests, or commercial outreach.

## DLP / Externalization Gate

Default status of outputs is internal.

Before any external use:

- remove sensitive client/project context;
- separate public market facts from Paper Planes interpretation;
- downgrade claims without evidence;
- anonymize internal examples unless approved;
- keep quotes short and source-linked;
- mark unknowns and assumptions;
- ask Ilya if the material includes client economics, CRM, margins, pipeline, support, delivery risks, or internal methodology.

## Boundaries With Adjacent Skills

| Adjacent skill | Difference |
|---|---|
| `deepresearch` | gathers broad evidence; this skill evaluates demand-supply fit and commercialization route |
| `competitor-research` | maps competitors; this skill maps offer unit x market cell x demand x supply |
| `sector-service-matrix-builder` | builds Paper Planes offer matrix; this skill evaluates external market fit |
| `commercial-proposal-generator` | writes КП; this skill supplies opportunity evidence and safe claims |
| `bpm4-b2b-dashboard-industrial-distribution` | analyzes internal data/economics; this skill consumes BPM-4 results as higher-confidence evidence |
| `presentation-qa` | reviews decks; this skill can feed deck claims but does not QA slide quality |
| `leverage-builder` | builds strategic levers; this skill tests market-cell viability of a lever |

## Done Definition

Done when:

- if external execution is intended, a ready-to-paste outbound prompt is produced instead of a completed local analysis;
- outbound prompt is one copyable block;
- outbound prompt requires the external answer in Markdown, not raw YAML only;
- outbound prompt requires Russian output unless Ilya says otherwise;
- outbound prompt requires input side to be named;
- outbound prompt requires fact / inference / hypothesis separation;
- outbound prompt requires offer unit decomposition into functions;
- outbound prompt requires explicit market cells;
- outbound prompt requires demand scoring by layer;
- outbound prompt requires supply check;
- outbound prompt requires market structure assessment without fake HHI;
- outbound prompt requires beneficiary-strategy fit if a beneficiary is named;
- outbound prompt requires market attractiveness to be separated from beneficiary fit;
- outbound prompt requires operating burden, client archetype / anti-archetype, and asset-conversion checks when relevant;
- outbound prompt requires route recommendation with confidence caveat;
- outbound prompt requires evidence ledger and data-gap backlog;
- outbound prompt requires confidence rules;
- DLP/writeback gates are explicit;
- outbound prompt requires self-reflection;
- return-packet-ingest mode treats external answer as advisory, not canonical;
- next action is local and approval-safe.

Not done if:

- it starts doing the full research in Codex when Ilya needed a prompt for ChatGPT Pro / Perplexity;
- answer evaluates "the market" in general;
- public visibility is treated as demand;
- offer availability is treated as business viability;
- confidence exceeds evidence;
- HHI is invented without shares;
- pilot is recommended without demand/supply/legal/economics gates;
- external output is treated as canon;
- client-facing claims are produced without calibration;
- writeback or externalization happens without Ilya's approval.

## Eval Cases

Good triggers:

- "Есть технология X, кому её продавать и есть ли рынок?"
- "У клиента боль Y, какие offer units могут закрыть её?"
- "Проверь, стоит ли запускать продукт в этом сегменте."
- "Сопоставь спрос и предложение по нескольким рыночным ячейкам."
- "Сделай prompt для Perplexity по demand-supply fit."

Bad triggers:

- "Собери конкурентов" -> use `competitor-research`.
- "Сделай deep research по рынку" -> use `deepresearch`.
- "Напиши КП" -> use `commercial-proposal-generator`.

Ambiguous:

- "Рынок большой?" -> force market-cell framing and evidence limits.
- "Есть много публичных сигналов" -> public visibility only; ask for internal data before high confidence.
- "Можно запускать пилот?" -> require demand, supply, legal, economics gates.

Writeback-risk:

- "Запиши вывод в стратегию" -> prepare candidate and ask approval.
- "Отправь клиенту" -> DLP and client-facing claim gate first.
- "Создай задачи" -> propose CORD candidates only.
