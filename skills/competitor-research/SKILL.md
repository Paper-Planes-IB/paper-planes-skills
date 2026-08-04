---
name: competitor-research
description: "Use when Ilya asks to prepare an external ChatGPT Pro / Perplexity / other research-machine prompt for deep competitor analysis, especially BPM-6 competitor research, or to process a returned competitor research packet: known competitor list, market, proposal, product strategy, positioning, marketing mix, sales approach, client/industry evidence, public news, reports, websites, SEO/search visibility, or competitor monitoring"
metadata:
  version: "0.1.0"
  status: experimental
  line: research / commercial / 2-ka / market intelligence
  owner: Ilya
  originator: Илья Балахнин
  source: "extracted from deepresearch; informed by Paper Planes Notion/Drive competitor-analysis materials"
  supports_bpm:
    primary: [BPM-6]
    required_secondary: [BPM-2, BPM-3, BPM-4, BPM-7A, BPM-7B, BPM-10]
    optional_secondary: [BPM-8, BPM-9, BPM-11]
  can_consume: [BPM Storyline-Storyboard, Матрица BPM — SI, competitor maps, CRM / win-loss / field-pressure signals, external research return packets]
  can_produce: [outbound competitor research prompt, BPM-6 return packet, client reality reconciliation questions, field pressure reconciliation, battlecard / competitor-map candidates, storyline_delta]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-05-26: Added BPM Exchange capability metadata."
      - "2026-06-21: Added mandatory field-pressure table before any real-client competitor ranking."
---

# Competitor Research

## Purpose

Generate a high-quality outbound research prompt / task packet for ChatGPT Pro, Perplexity, or another external research machine to build a detailed competitor intelligence packet for a known company / market / category when Ilya already has or can provide a competitor list.

This skill is a specialized extraction from `deepresearch`. It inherits `deepresearch` source discipline, source separation, claim ledger, DLP gate, and decision-packet logic, but focuses on competitor surfaces: websites, reports, public news, positioning, product lines, sales motions, key clients, industries, channels, promotion, pricing clues, and marketing mix.

For Paper Planes BPM work, this skill is the default external-prompt and return-packet rail for `BPM-6` competitor / desk research. It must treat competitor research as part of the BPM exchange, not as an isolated web-research task.

## Primary Codex Behavior

By default, Codex must not execute the full competitor research itself. Codex's primary job is to:

1. run internal preflight and collect safe context;
2. identify competitor names that require Ilya confirmation;
3. ask Ilya for confirmation when direct competitors are unclear;
4. generate a precise outbound prompt for ChatGPT Pro 5.5, Perplexity, or another external research machine;
5. require the external machine to return a structured competitor research packet with sources, questions, uncertainties, and benchmark best practices;
6. process the returned packet later through `return-packet` mode.

Codex may execute the research inside Codex only if Ilya explicitly says something like `делай здесь`, `исполни сам в Codex`, `не отправляем наружу`, or gives an equivalent direct instruction.

If Ilya says `dry run`, `префлайт`, `сгенерируй запрос`, `запрос для GPT Pro`, `запрос для Perplexity`, or similar, the output is an outbound prompt, not a completed competitor analysis.

### BPM-6 / BPM Exchange Gate

When Ilya invokes competitor research for a real Paper Planes project, especially with `BPM-6`, `конкуренты`, `карта конкурентов`, `battlecards`, `сравнить ресерч`, or `внешний инжест`, Codex must treat the run as `BPM-6` unless Ilya explicitly assigns another BPM.

The prompt or return-packet review must be fed by the top relevant BPM exchange signals that already exist before the run starts. These can include:

- `BPM-2` / `BPM-3`: client, NCL, sales, buyer-role, JTBD, TCO, field-pressure, and interview signals;
- `BPM-4`: sales base, revenue concentration, segment/product mix, margin / GP gaps, repeatability and account evidence;
- `BPM-7A/B`: market sizing, segment attractiveness, region/product priorities, procurement and CAPEX hypotheses;
- `BPM-10`: CRM, win/loss, competitor-in-deal, source, funnel, segment, and data-field gaps;
- existing `BPM Storyline-Storyboard`, `Матрица BPM — SI`, competitor maps, project cards, trackers, and accepted reconciliation notes.

Do not replace public competitor research with internal BPM signals. Use the BPM signals to shape what the external machine must test, falsify, normalize, downgrade, or route back as `needs_field_reconciliation`.

For every BPM-6 outbound prompt and return packet, include or extract:

- `bpm6_primary_classification`: direct competitor / integrator / distributor / component supplier / service-spares / EPC-specifier / hidden-low-visibility / benchmark-only / unknown;
- `bpm_exchange_inputs_used`: the 3-5 most relevant prior BPM signals included in the run;
- `conflict_with_prior_bpm`: where public evidence contradicts or reframes BPM-2/BPM-3/BPM-4/BPM-7/BPM-10;
- `field_reconciliation_needed`: what must be checked through client reality, CRM, win/loss, tender traces, project institutes, or follow-up interviews;
- `storyline_delta`: appeared / strengthened / weakened / needs_check;
- `rail_destination`: BPM Storyline-Storyboard / competitor map / BPM-SI / project rail / appendix-only / no-op.

If a returned packet changes competitor priority, battlecard readiness, segment threat, or slide hypotheses, Codex must update the existing `BPM Storyline-Storyboard` or record a no-op reason in the nearest project artifact after Ilya approves or clearly requests ingestion. Public visibility alone must never decide final competitor priority.

## Anti-sprawl Decision

```yaml
anti_sprawl_decision:
  proposed_new_skill: "competitor-research"
  decision: "create_after_approval"
  existing_skill_to_extend: "deepresearch"
  reason: "Competitor analysis has a standalone repeated trigger, distinct data schema, and recurring matrix outputs; keeping it inside deepresearch would make deepresearch too broad."
  approval_required: true
  approval_status: "approved by Ilya in chat"
```

## Non-goals

This skill must not:

- replace `deepresearch` for general market/company research;
- silently execute a full competitor research run inside Codex when the user expects an external-machine prompt;
- pretend that public positioning equals actual strategy;
- infer private clients, revenue, prices, contracts, or sales processes without evidence;
- scrape closed platforms, private accounts, paywalled sources, or personal data without an approved entry path;
- copy competitor content at length;
- write to Vault, CORD, Reader, Notion, or external decks without Ilya's approval;
- publish, send, or externalize findings without DLP review.

## Trigger Conditions

Use this skill when Ilya says:

- `проанализируй конкурентов`;
- `список конкурентов`;
- `competitor research`;
- `конкурентная разведка`;
- `позиционирование конкурентов`;
- `маркетинговый микс конкурентов`;
- `зайди на сайты конкурентов`;
- `почитай отчёты / новости / клиентов / продукты`;
- `сравни игроков рынка`;
- `собери карту конкурентного поля`;
- `что видно по продажам / продуктам / клиентам / отраслям конкурентов`.

Do not use this skill for:

- one-company brief without competitor comparison: use `client-info` or `deepresearch`;
- generic external second opinion: use `deepresearch`;
- product/service matrix for Paper Planes: use `sector-service-matrix-builder`;
- writing a commercial proposal: use `commercial-proposal-generator`;
- content drafting from findings: use content rail skills after this research produces an accepted packet.

## Required Inputs

Minimum:

- target company / product / market being compared;
- competitor list, even if rough;
- geography and industry/category;
- decision use: КП, strategy, positioning, product vitrine, sales argument, market entry, content, monitoring, other;
- depth: `lean`, `full`, or `monitor`.

Useful optional inputs:

- known client hypothesis / ICP;
- target segments;
- relevant products/services;
- whether the target entities are competitors, partners, integrators, distributors, resellers, channel multipliers, or a mixed list;
- for partner intelligence: partner/channel list, partner type, role in lead generation, and whether the task is about enablement, lead quality, channel conflict, GTM scale, or partner policy;
- available CRM / win-loss / support / deal notes / SKU or segment data, if already collected;
- for partner intelligence: available partner performance data, lead source data, deal registration, lead-to-meeting / lead-to-pilot / lead-to-contract conversion, revenue by partner, discount/margin signals, implementation outcomes, and partner-owned vs direct-owned deal notes;
- time horizon for news and reports;
- languages / regions. Default output language is Russian only unless Ilya explicitly requests another language;
- preferred visualization format: tables, PPT-ready chart descriptions, словесные схемы / block schemes, positioning maps, scorecards;
- BPM / SI visual intent if relevant: BPM-6 competitor/context, BPM-7A market sizing, BPM-7B product/industry/region prioritization, SI / SIF / storyline-storyboard hypotheses;
- preferred source priority by sector: official product pages, partner cards, industry media, professional blogs, documentation, conferences, public talks, reviews, databases;
- desired source granularity: homepage only, product pages, partner pages, docs/support, landing copy, case pages, pricing pages, event pages;
- whether direct marketing-language quotes from landing pages are needed;
- whether battlecard bullets are needed: where they win, where we win, when to concede, where not to fight, typical landmine, counter-argumentation;
- whether the research must test `platform value` vs `bundle / product set` vs `synergy`;
- target positioning territory to test, if any;
- hypotheses to verify or falsify;
- focus competitors for mini-battlecards, if different from the full confirmed direct competitor list;
- sales-play requirements: buyers, trigger events, entry product, expansion path, proof metrics, likely objections;
- playbook segmentation requirements: core segments, adjacent segments, defensive segments, research-only segments, or segment-specific sales motions;
- storyline synthesis requirements: strategic frame, tactical blocks, operating levers, weak-evidence slides to move down, and domain-specific Russian terminology;
- known source pack, Google Drive folder, Notion pages, prior matrices, storyline/storyboard, project passport, subpassports, tracks, trackers, or adjacent project artifacts;
- what not to analyze;
- confidentiality / DLP constraints.

If competitor list is missing or may be incomplete, first search the current project context for competitor mentions and propose candidate competitors. Do not treat any mentioned company as a confirmed competitor until Ilya approves it.

## Source Priority

Always separate internal, external, and inference.

Internal sources:

- Vault / Google Drive files supplied or discoverable through connectors;
- Notion pages or connected Google Drive materials about competitor analysis;
- prior Paper Planes matrices, КП, project artifacts, content, and research packets;
- project storyline/storyboard documents;
- project passport, project card, стартовое сообщение, or project README;
- chat subpassports and track/subtrack passports;
- project tracks, trackers, scope maps, task rails, stage-gate notes, interview briefs, client context, and stykovye/adjacent artifacts that explain why competitor research is needed;
- Readwise / Reader documents and highlights when relevant.

External public sources:

- competitor official sites, product pages, pricing pages, blogs, case studies, FAQ, help center, webinars, landing pages;
- partner cards, marketplace listings, distributor/reseller pages, integration catalogs;
- annual reports, investor decks, sustainability reports, public filings, tenders, procurement pages, procurement portals, RFP/specification traces, and contract award records;
- public news, industry media, analyst/review sites, interviews, press releases, conference talks, podcasts;
- public client logos, cases, partner pages, integrations;
- search results, SEO clues, ad libraries, social/public content, review platforms;
- documentation portals, support portals, changelogs, release notes, API/integration documentation;
- professional blogs, public technical posts, conference agendas, webinars, event pages, speaker decks;
- job postings and team pages as weak evidence for priorities and capabilities;
- public registries, classifiers, certificates, licenses, accreditation records, and industry directories;
- exhibition catalogs, speaker/sponsor lists, association member directories, partner directories, and public supplier catalogs.

Forbidden or restricted:

- closed groups, private chats, personal data, account automation, bypassing access controls;
- long copyrighted excerpts;
- non-public client evidence unless Ilya explicitly supplies and approves use;
- sensitive internal Paper Planes / client context in external prompts without DLP approval.

## Notion / Drive Reference Patterns

When available, use Notion and connected Google Drive as a source of existing Paper Planes process language and templates.

Known useful patterns found in Notion/Drive search:

- published PP article: `Анализ конкурентов: как провести, методы` in Notion / Media PP;
- competitor assessment parameters from PP decks: products/services, pricing policy, target clients, sales and service processes, positioning, promo tools, channels;
- positioning spreadsheets: vectors such as assortment, premium/quality, innovation/technology, expertise/training, financial terms, logistics/availability, reputation;
- 6P-style matrices: Product, Price, Place, Promotion, People, Positioning;
- medical / sector templates that capture quotes, visual artifacts, positioning territory, USP, categories, customer segments.

Do not assume Notion or Drive is canonical by itself. Use it as an internal source pattern and cite it as `internal_source`.

## Execution Priorities And Success Definition

For complex competitor research, force the external machine to work by priority levels instead of treating all sections equally.

Default priority ladder:

- `P0`: the main strategic question that changes positioning, category framing, platform/synergy logic, or sales direction;
- `P1`: confirmed direct competitors approved by Ilya;
- `P2`: auxiliary, adjacent, substitute, or local-market competitors;
- `P3`: global / international benchmarks used for best practices, not as direct competitors.

The exact P0 wording must be adapted to the project. Examples:

- choose the strongest positioning territory;
- prove whether the offer is `platform value`, `bundle`, `suite`, `workflow`, or `synergy`;
- explain the category shift;
- identify the sales plays that should change КП / defense / product strategy.

Definition of success must be explicit in the outbound prompt. A good packet should make it possible to:

- choose one primary positioning territory or state that evidence is insufficient;
- explain platform / bundle / synergy distinction when relevant;
- prepare 3-5 sales plays;
- produce mini-battlecards for the most important confirmed competitors;
- separate safe claims, risky claims, and claims to avoid;
- produce a hypothesis verdict table: hypothesis, verdict, evidence, confidence, implication.

## Platform / Bundle / Synergy Proof Standard

If the research compares `platform`, `suite`, `bundle`, `ecosystem`, `identity loop`, `workflow`, `operating system`, or similar platform-like claims, do not accept the label only because a player has several products.

Platform or synergy value can be counted only when public or accepted internal evidence supports at least some of:

- cross-product workflows;
- unified identity / customer / entity / object model;
- shared policy, risk, scoring, reporting, or governance logic;
- event integration across products;
- unified audit evidence or compliance trace;
- shared data layer, integrations, API, or orchestration logic;
- measurable customer outcome that emerges from combined use, not from one module alone.

When evidence is weak, label the claim as `bundle`, `suite`, `possible synergy`, or `platform claim not proven` instead of accepting the vendor's category language.

## Threat, Positioning, And Internal Data Discipline

Public competitor research can map visible market structure early, before BPM-4 / CRM / win-loss / support data exists. It must not pretend that public visibility is the same as real deal threat.

Separate these layers:

| Layer | Meaning | Allowed conclusion |
|---|---|---|
| `public_visibility` | how visible / loud / well-positioned the player is in public sources | useful for positioning, awareness, category language, and public proof |
| `positioning_claim` | what the competitor says or implies about itself | valid input to positioning analysis, not proof of actual adoption or superiority |
| `deal_level_threat` | whether the competitor appears in real deals, losses, objections, CRM, support, or win-loss data | requires internal / client-side evidence |
| `unknown_until_internal_data` | public sources are not enough to rank practical threat | must be marked as uncertain |

If CRM / win-loss / support / SKU / segment data is unavailable, still run the external market-context research, but require caveats:

- threat ranking is based on public visibility and evidence strength, not proven sales threat;
- segment economics and real win/loss patterns remain unverified;
- practical prioritization should be revisited after BPM-4 / CRM evidence appears.

When BPM-4 is clearly completed in a project, Codex should remind Ilya that competitor conclusions can be upgraded with CRM / win-loss / support / SKU / segment data. This is not a blocker for early BPM-6 research; it is a later improvement opportunity.

### Mandatory Field-Pressure Table Before Ranking

For any real-client public competitor map, do not produce a final competitor ranking, battlecard priority list, or sales-play priority until a compact field-pressure table is present. If field evidence is unavailable, the table must still exist and mark the relevant columns as `unknown`; the output can rank only public visibility / evidence quality, not real deal threat.

Minimum table:

| player | role_type | public_visibility | client_reported_pressure | CRM_or_win_loss_evidence | historical_or_latent_pressure | ranking_allowed_now | next_evidence_needed |
|---|---|---|---|---|---|---|---|

Rules:

- `ranking_allowed_now=yes` only when client / sales / CRM / win-loss / tender / implementation evidence supports the practical threat.
- High public visibility with unknown or weak field pressure becomes `benchmark_only`, `latent_threat`, `watch`, or `public_visibility_rank_only`.
- Low public visibility with strong field pressure becomes `hidden_or_low_visibility_competitor` and must be routed to BPM-2 / BPM-3 / BPM-10 before client-facing use.
- If this table would be mostly `unknown`, classify the packet as `public evidence map / needs_field_reconciliation`, not as battlecard-ready.

## Hidden / Low-Visibility Competitors

External web search often misses competitors that matter in deals but are weakly visible online.

Require the external machine to look for and separately report:

- local dealers, distributors, integrators, agencies, installers, and implementation partners;
- white-label / private-label / OEM offers;
- regional suppliers or niche players;
- project-based providers who sell a solution rather than a named product;
- substitutes that solve the same customer job through another category;
- marketplaces, tender mentions, partner catalogs, and industry directories that reveal players absent from search results.

These players must be marked as `hidden_or_low_visibility_candidate` until stronger evidence or Ilya confirmation exists. They can inform market structure, but they must not enter client-facing battlecards without source-check.

Hidden-competitor search must not stop at ordinary web search. When the raw list contains weak names, regional players, channel players, suppliers, or unclear entities, require a separate hidden-source pass:

- tender / procurement traces;
- job postings and team capability signals;
- public registries, classifiers, certificates, licenses, and accreditation records;
- exhibition catalogs, association directories, partner directories, and supplier catalogs;
- reseller, dealer, white-label, OEM, implementation, and project/specification channels.

If these sources are not checked, label hidden competition as a `question map`, not a final threat map.

## Role Taxonomy And Weak-Name Normalization

Do not put every found organization into one competitor bucket. Before ranking or battlecarding, classify each player by role:

| role_type | meaning |
|---|---|
| `manufacturer` | makes or owns the product / platform / core offer |
| `integrator` | implements, configures, customizes, or assembles solutions around others' products |
| `supplier` | supplies goods / components / licenses without owning the full solution logic |
| `distributor_or_dealer` | channel player, reseller, regional access point, or sales intermediary |
| `service_provider` | provides service, support, operations, maintenance, outsourcing, or recurring delivery |
| `project_institute_or_specifier` | shapes specs, requirements, designs, standards, or procurement logic without necessarily selling the final product |
| `white_label_or_oem` | sells under another brand or enables another player invisibly |
| `substitute` | solves the same customer job through another category |
| `benchmark_only` | useful best-practice comparator, not a live competitor |
| `unknown` | role unclear; must not enter the main battlecard layer |

For weakly visible names, OCR/transcript names, raw-list names, and entities found only once, require a normalization pass before analysis:

| raw_name | normalized_name | role_type | confirmation_status | evidence_used | client_facing_use |
|---|---|---|---|---|---|
| as found | canonical or best guess | role taxonomy | confirmed / normalized_candidate / duplicate / exclude / unknown | registry / tender / site / catalog / job / source list | no / source-check only / yes |

Use `normalized_candidate` until the name is supported by at least one primary public source, registry/tender/catalog trace, or Ilya/internal confirmation. A normalized candidate may appear in hidden candidates, confirmation questions, or appendix, but not in the main threat ranking or client-facing battlecards.

## Forbidden Market Shortcuts

For positioning analysis, competitor self-claims are important. Preserve them as `positioning_claim` or `official_self_claim`.

But do not convert these shortcuts into market facts:

- marketplace volume or number of listings as market size;
- public presence, SEO visibility, or media activity as market share;
- partner / integration / marketplace listing as proof of active implementations;
- channel presence as proof of sales effectiveness;
- case logo as proof of current scale or satisfaction;
- broad category language such as `рынок большой`, `лидер`, `платформа`, `экосистема`, `enterprise-ready` as fact without direct evidence.

Use these signals for positioning and hypothesis generation, then mark what evidence would be needed to use them as client-facing claims.

## Next Evidence Layer / BPM-5 Candidate

Some competitor questions cannot be resolved by public research alone. When the public packet exposes unresolved practical threats, recommend the next evidence layer instead of overclaiming.

Possible next evidence sources:

- real КП / proposals / commercial offers;
- product specifications, tender requirements, technical tasks, RFPs;
- approved mystery-shopping or funnel walk, without impersonation or access bypass;
- demo / pricing request traces, if ethically and legally obtained;
- win-loss interviews;
- customer / integrator / partner interviews;
- support / service / implementation pain data;
- CRM / deal-stage / objection data after BPM-4.

Treat this as a `BPM-5 candidate` for future discussion, not as a mandatory part of every competitor-research run. Do not create a new BPM-5 skill automatically.

## BPM Exchange Governance

For real-client competitor work, use the full BPM exchange architecture, but prevent noisy routing and public-visibility overreach.

Before producing or accepting a competitor research packet, add a compact governance layer:

```yaml
bpm_exchange_governance:
  relevance_score: 0.0
  route_class: "required_check|optional_enrichment|watch|no_op"
  preflight_summary: "" # 200 tokens max
  required_checks: []
  optional_enrichment: []
  conflict_resolution:
    conflict_detected: true|false
    conflicting_signal_or_source: ""
    contradiction_type: "hard|soft|no_op|unknown"
    resolution_strategy: "human_arbitration|evidence_weight|archetype_precedent|park"
    resolution_status: "pending|resolved|parked|not_needed"
  signal_lifecycle:
    decay_status: "fresh|aging|stale|timeless"
    ttl_days: 90
    ttl_override: false
  work_log_check:
    duplicate_check_done: true
    similar_recent_work: []
    action: "reuse|extend|rerun|new_work"
  metrics:
    derivatives_generated: 0
    derivatives_landed: 0
    derivatives_no_op: 0
    false_positive_risk: "low|medium|high|unknown"
```

Distinguish BPM routes:

- `required_check`: the BPM can change competitor priority, block a client-facing battlecard, validate a weak ranking, resolve a contradiction, or define commercial/data requirements. Examples: BPM-2/BPM-3 for client reality, BPM-4/BPM-5 for deal pressure/economics, BPM-10/BPM-11 for ownership/data model.
- `optional_enrichment`: the BPM can improve context or proof but does not block using the current packet as hypothesis. Examples: extra BPM-7B sector framing or benchmark enrichment when no client claim depends on it.
- `watch`: keep the player/signature visible without generating tasks.
- `no_op`: record why this competitor route is irrelevant.

Use top-K filtering: include only the 3-5 most relevant active exchange signals or archive analogs in the outbound prompt / local packet. Do not dump every mention of every competitor.

If internal/client evidence contradicts public research, create a conflict record instead of letting public visibility decide the ranking.

## Client Reality Reconciliation Gate / BPM-2

For real client projects, competitor research is only a public evidence map until reconciled through the client's lived reality. This reconciliation is primarily a `BPM-2` derivative: external competitor claims must generate client / owner / expert questions that can confirm, correct, contradict, add, or downgrade the public map. If the relevant voice is dealer, partner, integrator, sales, support, implementation, or internal expert evidence, route the same check through `BPM-3`.

The outbound prompt and returned packet must explicitly say:

`This is a public evidence map, not the client's lived market map, until reconciled with internal/client evidence.`

Require this block when the research concerns a real client project:

```yaml
client_reality_reconciliation_gate:
  external_visibility_claims:
    - claim: ""
      source_type: "official_self_claim|partner_or_channel_claim|third_party_claim|marketplace_signal|tender_signal|inference"
      evidence_grade: "A|B|C|D|X"
      public_visibility_only: true
  client_reality_questions:
    - question: ""
      target_role: "owner|CEO|sales|regional_manager|dealer|expert|procurement|technical_team|support|implementation"
      tests_claim: ""
      expected_correction_type: "confirm|correct|contradict|add|downgrade"
  likely_misread_or_misnamed_entities: []
  historical_vs_current_status: []
  business_model_factors_to_check:
    - "pricing"
    - "VAT/tax structure"
    - "procurement volume"
    - "service burden"
    - "margin"
    - "implementation effort"
    - "partner economics"
    - "support load"
  reconciliation_output_template:
    confirmed_by_client: []
    corrected_by_client: []
    contradicted_by_client: []
    added_by_client: []
    downgraded_after_client_input: []
    needs_CRM_win_loss_source_check: []
```

Do not let public visibility, PMS listings, marketplaces, tender mentions, partner catalogs, or case pages become client-lived-market claims until this reconciliation is done.

## Partner Intelligence Mode

Use this branch when the entities are partners, integrators, distributors, resellers, implementation providers, lead sources, channel multipliers, or when Ilya asks for `partner intelligence`, partner-channel research, partner policy, partner enablement, or analysis of partner help / hinder dynamics.

Important: do not turn partners into competitors. A partner becomes a direct competitor only if there is public evidence that it sells a direct substituting product or platform. Otherwise, mark tensions as `possible_channel_conflict`, `implementation_conflict`, `vendor_portfolio_conflict`, `margin_pressure_hypothesis`, or `lead_quality_gap`, not as direct competition.

Partner research must separate these layers:

| Layer | Meaning | Allowed conclusion |
|---|---|---|
| `public_visibility` | how visible the partner is in public sources | awareness, public category language, public proof surface |
| `public_readiness` | how ready the partner appears to discuss the category based on visible expertise, cases, events, content, and vendor portfolio | hypothesis for enablement priority, not proof of deal performance |
| `visible_identity_relevance` | public proximity to IAM / PAM / MFA / IdM / PKI / SOC / compliance / adjacent topics | hypothesis about fit for the category conversation |
| `possible_channel_conflict` | visible competing vendors, own services, adjacent products, or commercial incentives | risk hypothesis that requires client/internal verification |
| `lived_partner_map` | how the client actually experiences the partner in deals | requires Konakov / sales / CRM / win-loss / partner performance evidence |
| `actual_lead_quality` | real quality of leads submitted by the partner | requires CRM / lead brief / conversion / interview evidence |
| `actual_revenue_contribution` | real contribution to revenue / pipeline | requires CRM / finance / partner performance evidence |
| `actual_margin_pressure` | real discount or margin pressure caused by the partner | requires commercial data, not public inference |

Allowed without field correction:

- rank `public_readiness`, `public_visibility`, `visible_identity_relevance`, and `enablement_priority_hypothesis`;
- propose partner segments and sales-play hypotheses;
- mark likely help / hinder patterns as inference;
- identify what must be checked in CRM, win-loss, partner interviews, and commercial interviews.

Forbidden without field correction:

- ranking `best partners for the client` as a final claim;
- claiming highest lead quality, best conversion, highest revenue contribution, real margin pressure, real tendency to hide the client, or real deal-level conflict;
- turning a public vendor portfolio into proof that the partner actively pushes a competitor in deals;
- using public partner status as proof of implementation quality or sales effectiveness.

Partner intelligence packets must include this sentence verbatim:

`This is a public evidence map, not the client's lived partner map, until reconciled with internal/client evidence.`

### partner_intelligence_self_reflection_gate

If an external researcher writes that CRM, win-loss, partner performance, real lead quality, margin pressure, conversion data, closed partner portals, or filled lead briefs are missing, convert that from a generic disclaimer into a concrete data-gap table:

| public_claim | missing_client_data | interview_owner | CRM_or_source_field | deck_usability | action |
|---|---|---|---|---|---|
| visible claim or ranking from public research | exact internal evidence needed | Konakov / Ekaterina / CRM analyst / sales / presales / marketing / support | existing or proposed CRM / source field | client-ready / internal-only / appendix-only / do-not-use | accepted_gap / already_covered / new_task_candidate / ignore / skill_improvement_candidate |

For partner research, self-reflection must not remain only a prose caveat. It must become a `partner_data_gap_packet` with:

- `accepted_gap`;
- `already_covered`;
- `new_task_candidate`;
- `ignore`;
- `skill_improvement_candidate`.

### Weak-Signal Layer For Partners

Partner packets should collect weak signals, but label them explicitly as `weak_signal`, not as proof of real deals.

Allowed weak signals:

- vacancies and role requirements;
- Habr / professional blogs / technical posts;
- conference talks, agendas, speaker profiles, and webinars;
- tenders and procurement traces;
- partner pages, vendor catalogs, marketplace listings, and integration catalogs;
- certified specialists, badges, partner statuses, and training pages;
- public case pages, event pages, whitepapers, and demo-lab mentions.

Weak signals can support `public_readiness` and `visible_identity_relevance`. They cannot support final claims about actual lead quality, revenue, conversion, margin pressure, customer ownership, or deal-level conflict.

### Under-Cover / Mystery-Shopping Quarantine

Do not recommend or run under-cover research, fake leads, mystery-shopping, impersonation, or funnel walks by default. In B2B enterprise channels, this is often ethically risky, legally sensitive, and weak as evidence because the real cycle is long and relationship-driven.

Such work is allowed only after all of:

- separate explicit approval from Ilya;
- ethical and legal check;
- narrow written scenario;
- no impersonation of a real person;
- no access bypass, closed-portal scraping, or private-data collection;
- clear statement of what decision the exercise can and cannot support.

Default safer substitutes: Konakov / Ekaterina / sales interviews, CRM and win-loss analysis, partner performance review, filled lead brief audit, and partner enablement workshop.

## Field Pressure Reconciliation

After `Client Reality Reconciliation Gate` produces client-side, sales-side, CRM, win/loss, dealer, partner, or expert evidence, reconcile each competitor by field pressure. Do not rank competitors by public visibility alone when client-side interviews or CRM are available.

For every meaningful competitor or candidate, separate:

```yaml
field_pressure_reconciliation:
  competitor: ""
  public_visibility: "strong|medium|weak|unknown"
  client_reported_pressure: "strong|medium|weak|none|unknown"
  historical_pressure: "active_now|used_to_matter|legacy_installed_base|obsolete|unknown"
  latent_threat: "high|medium|low|unknown"
  benchmark_only: true|false
  channel_or_partner: true|false
  direct_competitor_status: "confirmed|likely|candidate|not_direct|unknown"
  evidence_sources:
    public: []
    client_or_sales_voice: []
    CRM_or_win_loss: []
    partner_or_channel: []
  ranking_implication: ""
  action: "prioritize_battlecard|monitor|interview_more|CRM_check|benchmark_only|downgrade|exclude"
```

Definitions:

- `public_visibility`: strong web/source presence.
- `client_reported_pressure`: mentioned by client / sales / ROP / dealer / expert as appearing in deals.
- `historical_pressure`: used to matter, now less visible in deals, or present as legacy installed base.
- `latent_threat`: capable player that could matter but is not currently frequent.
- `benchmark_only`: useful comparison, not a live competitor.
- `channel_or_partner`: may bring deals or block deals, but is not a direct competitor.

If public visibility is high but field pressure is low, mark the player as `benchmark_only`, `latent_threat`, `historical_pressure`, or `monitor`, not as a priority direct battlecard. If field pressure is high but public visibility is weak, flag `hidden_or_low_visibility_competitor` and route to BPM-2/BPM-3/BPM-5/BPM-10 checks before client-facing use.

## Client Correction Packet

When a client, owner, expert, dealer, partner, sales, support, or implementation call becomes available after external competitor research, produce a correction packet. This is the operational output of client reconciliation: it says which external findings were confirmed, corrected, weakened, renamed, moved, or need CRM/win-loss.

Required table:

| external finding | client correction | effect on priority | evidence needed | action |
|---|---|---|---|---|

Use categories:

- `confirmed`;
- `strengthened`;
- `weakened`;
- `contradicted`;
- `renamed / normalized`;
- `added by client`;
- `moved to historical`;
- `moved to partner/channel`;
- `moved to benchmark`;
- `requires CRM/win-loss`.

Required schema:

```yaml
client_correction_packet:
  source_external_packet: ""
  source_voice_evidence: "BPM-2|BPM-3|mixed"
  corrections:
    - external_finding: ""
      client_correction: ""
      category: "confirmed|strengthened|weakened|contradicted|renamed_normalized|added_by_client|moved_to_historical|moved_to_partner_channel|moved_to_benchmark|requires_CRM_win_loss"
      effect_on_priority: "raise|keep|lower|remove|monitor|split_segment|needs_more_evidence"
      evidence_needed: []
      action: ""
      downstream_bpm:
        - "BPM-4"
        - "BPM-9"
        - "BPM-10"
  bpm_routes:
    BPM-4: "data/dashboard/CRM fields to verify competitor pressure and economics"
    BPM-5: "proposal/win-loss/commercial traces to verify"
    BPM-9: "implementation rhythm or operating decision affected"
    BPM-10: "CRM/lead-source/pipeline/ownership fields to check"
    BPM-11: "data entities/statuses to adjust or inspect"
```

Use this packet before changing battlecard priorities, competitor heatmaps, sales plays, Storyline-Storyboard claims, or client-facing competitor rankings.

## CRM / Win-Loss Transfer Fields

Competitor research should improve the next CRM / win-loss / sales-motion cycle, not only the deck. When the decision use includes sales, КП, positioning, product strategy, or market entry, convert findings into fields that can be checked later:

| field | meaning |
|---|---|
| `competitor_in_deal` | player actually seen in a deal / tender / objection, not merely visible online |
| `competitor_role_type` | manufacturer / integrator / supplier / distributor / service provider / specifier / white-label / substitute / benchmark |
| `segment_or_use_case` | where this competitor appears or might appear |
| `trigger_event` | what causes the buyer to compare alternatives |
| `source_type` | CRM / win-loss / tender / interview / public source / inference |
| `loss_or_risk_reason` | price, trust, availability, channel, product fit, implementation burden, incumbent, regulation, other |
| `price_or_commercial_objection` | specific commercial pressure, if evidenced |
| `implementation_or_service_objection` | delivery, support, integration, operations, or service risk |
| `proof_needed_before_battlecard` | what evidence upgrades the claim to client-facing use |

If these fields cannot be filled, mark sales-motion conclusions as `public_hypothesis`, not as deal-level mechanics.

## Commercial Mechanics As Competitive Factor

A battlecard is incomplete if it compares only products, features, public claims, or positioning while ignoring commercial mechanics. For real client projects, competitor pressure may be explained by economics and operating burden more than by product superiority.

For each priority competitor, sales play, or segment battlecard, check:

```yaml
commercial_mechanics_check:
  competitor: ""
  VAT_or_tax_model: "with_VAT|without_VAT|IP_or_sole_prop|mixed|unknown"
  procurement_volume: "large|medium|small|unknown"
  cost_base_or_COGS_signal: "known|inferred|unknown"
  insurance_or_risk_buffer: "present|absent|unknown"
  discount_rules: "transparent|individual|dealer_based|tender_based|unknown"
  price_effect_on_sales_motivation: "raises|neutral|lowers|unknown"
  service_and_warranty_cost: "high|medium|low|unknown"
  implementation_effort: "high|medium|low|unknown"
  integration_effort: "high|medium|low|unknown"
  opportunity_cost: "high|medium|low|unknown"
  evidence_needed: []
  battlecard_implication: ""
```

Required factors:

- VAT / no VAT / sole proprietor or similar tax structure;
- procurement volume;
- cost base / COGS;
- insurance or risk buffer;
- discount rules;
- effect of price on sales motivation;
- service and warranty cost;
- implementation effort;
- integration effort and opportunity cost.

If these mechanics are unknown, mark the battlecard as `commercially incomplete` and route missing evidence to BPM-4, BPM-5, BPM-9, BPM-10, or BPM-11 as appropriate. Do not explain a competitor win by product features alone when tax, procurement, discount, service, implementation, or integration economics may explain it better.

## Naming Normalization / Transcript Safety

When competitor names come from transcripts, voice notes, client calls, OCR, auto-summary, or informal speech, do not create new competitor entities immediately.

Return a normalization table:

| raw_name | likely_normalized_name | confidence | why | needs_confirmation_from |
|---|---|---|---|---|

Examples of risks:

- phonetic transcription;
- Cyrillic/Latin variants;
- brand vs product vs platform name;
- local nickname;
- former company name;
- distributor name confused with vendor;
- competitor merged with technology standard.

Until confirmed, use `normalized_candidate`, not `confirmed_competitor`. A `normalized_candidate` may appear in `competitor_mentions_for_confirmation` or hidden/low-visibility candidates, but not in the main confirmed competitor matrix or client-facing battlecards.

## Segment Playbook Logic

Do not collapse a heterogeneous market into one generic competitor strategy.

If the target market has distinct jobs, buying contexts, segments, routes, or implementation models, require segment-specific playbooks.

Each playbook should include:

- segment / buying context;
- primary job-to-be-done;
- confirmed / likely competitors;
- hidden or low-visibility competitors to check;
- positioning territory;
- where public evidence is strong;
- what CRM / BPM-4 / win-loss / support data would change;
- sales play;
- battlecard implications;
- client-facing claims to use / avoid.

Default playbook statuses:

- `core`: main current strategic battlefield;
- `adjacent`: related opportunity, but needs proof;
- `defensive`: must understand to avoid being surprised or attacked;
- `research_only`: keep watching; do not prioritize commercially yet.

## Storyline Synthesis Layer

When competitor research feeds a deck, BPM Storyline-Storyboard, SI/SIF cluster, commercial defense, or strategy narrative, require a storyline synthesis layer in Markdown.

This layer must generalize from evidence into a usable storyline without canonizing project-specific claims.

Rules:

- answer in Markdown, not as raw YAML only;
- keep the executive decision packet first, then analytical tables, then claim ledger, then appendix with sources;
- separate strategic frame from tactics, tools, evidence, and appendices;
- identify 5-8 storyline landing blocks where new facts should be placed instead of rewriting the whole structure;
- when an existing storyline exists, treat new research as an increment first: land facts into existing blocks, show deltas, and rewrite the whole storyline only if evidence forces a structural change;
- if a tool or digital interface appears, classify it by management function, not as a standalone IT block by default;
- if marketing appears, describe its role in supporting channels, sales, category creation, proof, and partner/dealer enablement, not only traffic;
- if pricing, discounts, routes, conditions, or channel effort appear, translate them into revenue / margin management language;
- move slides about market base, shares, regions, market sizing, or quantitative claims lower into evidence/appendix when proof is not strong enough;
- use professional Russian and minimize unnecessary English terms;
- if sector language exists, use the sector's accepted Russian vocabulary before importing English labels.

Generic storyline landing blocks may include, depending on the project:

- strategic frame / defense logic / category logic;
- availability / service / operational reliability;
- channel, dealers, partners, direct sales, or route-to-market;
- revenue and margin management;
- digital interface / portal / account as operating infrastructure;
- marketing as sales/channel/category support;
- new categories, OEM, application bundles, or product expansion;
- data, dashboards, roles, governance, and pilot roadmap.

If a returned external answer proposes a project-specific storyline, Codex should treat it as a candidate. In return-packet mode, extract:

- which generic storyline blocks are useful;
- which are project-specific and should not become global skill rules;
- which require Ilya confirmation;
- which should be added to BPM-SI / Storyline-Storyboard as candidates after approval.

## Storyline Increment Rule

If Ilya brings additional research, a new external answer, or a new source pack after a storyline already exists, do not ask the external machine to rewrite the whole storyline by default.

Require an increment-style answer:

- keep the current strategic frame unless the new evidence directly weakens it;
- place each new fact into one of the existing storyline blocks or propose a new block only if none fits;
- show deltas in four groups: `appeared`, `strengthened`, `weakened`, `needs_check`;
- mark weakly sourced additions as `evidence_pending`, not as accepted storyline;
- propose slide changes as `add`, `strengthen`, `move_down`, `merge`, `remove`, or `no_change`;
- preserve Russian management language and avoid unnecessary English terms;
- if the answer proposes a full storyline rewrite, it must explain what evidence made incremental landing insufficient.

## BPM / SI Visual Layer

Competitor research often feeds `BPM-6`, `BPM-7A`, and `BPM-7B` in Paper Planes project logic.

Use canonical naming:

- `BPM-6` = desk research / competitor analysis;
- `BPM-7A` = market sizing: PAM / TAM / SAM / SOM;
- `BPM-7B` = product / industry / region market analysis, Porter-like;
- use `SI`, `SIF`, and `SIF cluster` for slide-intent / evidence-factor logic;
- do not introduce `SIEF` as a canonical term. If Ilya says `SIEF`, treat it as a practical request for SI/SIF-oriented visual evidence, but write `SI / SIF visual layer` in the prompt.

When the research may feed storyline/storyboard, the external machine must propose not only findings, but also slide-useful visuals and the SI / SIF function of each visual.

### Visual-First Transfer Packet

When the returned answer contains a lot of prose, Codex must convert the useful parts into a visual-first transfer packet before treating it as storyboard-ready.

Minimum visual packet for serious competitor work:

- competitor heatmap by priority level (`P1`-`P5` or the project's priority scale), evidence depth, and sales relevance;
- role / arena map separating manufacturers, integrators, suppliers, distributors, service providers, specifiers, white-label/OEM players, substitutes, and benchmarks;
- segment attractiveness x right-to-win matrix;
- manufacturer-vs-integrator / owner-vs-channel map when roles are mixed;
- battlecard sheet for the top priority players, including confidence and proof gaps;
- top-5 one-slide battlecards when the result will feed КП, storyboard, or sales defense;
- exhibit titles and slide headlines for each proposed visual;
- color-coded confidence / usability labels: `client-ready`, `internal-only`, `needs_source_check`, `do_not_use`.

If the external answer is analytically useful but not slide-ready, return it as `analysis_ready_but_not_storyboard_ready` and list the missing exhibits.

### Useful Visuals By BPM

For `BPM-6` competitor / desk-research stories, ask for:

- competitor positioning map: axes, player placement, white spaces, interpretation;
- competitor pyramid / arena map: direct competitors, auxiliary players, substitutes, international benchmarks;
- product-domain coverage matrix: players x product/service domains, feature depth, evidence grade;
- category maturity / market reframing diagram: old frame -> emerging frame -> desired category claim;
- benchmark pattern map: practice, source, applicability, what to adapt, what not to copy;
- claim-source map: self-claim vs partner/channel claim vs third-party claim vs documentation evidence;
- battlecard matrix: strengths, weaknesses, landmines, counter-arguments, concede cases;
- substitute / adjacent-services map when the category boundary is unstable.

For `BPM-7A` market-sizing stories, ask for:

- PAM / TAM / SAM / SOM waterfall or nested funnel;
- segment-size table with assumptions, source quality, confidence range, and what would change the estimate;
- opportunity pool map: size x accessibility x strategic relevance;
- capacity vs potential chart: market opportunity vs realistic sales / delivery / channel capacity;
- growth drivers / restraints timeline when market timing matters;
- sensitivity table: optimistic / base / conservative assumptions;
- evidence-gap table for market-sizing claims that lack reliable sources.

For `BPM-7B` product / industry / region prioritization stories, ask for:

- product x industry x region heatmap: attractiveness, fit, competition intensity, evidence grade;
- Porter-like forces map: buyers, suppliers, substitutes, rivalry, entrants, regulation/platform dependence if relevant;
- value-chain / ecosystem map: roles, channels, influencers, partners, bottlenecks;
- BCG-style or attractiveness x right-to-win matrix;
- GTM-priority matrix: segment/region/product x sales motion / channel / proof required;
- regional/product opportunity map with caveats and source confidence;
- risk/opportunity portfolio: where to enter, defend, test, avoid.

### SI / SIF Visual Annotation

Every recommended visual should include:

```yaml
visual_si_annotation:
  visual_name: ""
  bpm_source: "BPM-6|BPM-7A|BPM-7B|bundle"
  storyline_role: "Situation|Complication|Question|Answer|evidence block|appendix|battlecard|support"
  si_or_sif_function: ""
  what_it_proves: ""
  what_it_does_not_prove: ""
  evidence_needed: []
  slide_readiness: "ready|needs_source_check|appendix_only|do_not_use"
```

Do not let the external machine treat every visual as slide-ready. It must distinguish:

- `ready`: enough evidence for main storyline;
- `needs_source_check`: useful hypothesis, needs stronger source;
- `appendix_only`: useful support, not main storyline;
- `do_not_use`: visually tempting but unsupported or misleading.

## Internal Context Preflight

Before researching competitors externally, build an internal context pack for the executing model. The goal is to prevent generic competitor analysis and make the machine understand the project situation.

If the task is attached to a real project, client, КП, product route, or market-entry question, first look for existing internal context in this order:

1. `storyline` / `storyboard` documents, especially BPM Storyline-Storyboard or proposal/storyline files;
2. project passport, project card, стартовое сообщение, README, or project overview;
3. chat subpassports, track/subtrack passports, and chat map rows;
4. active project tracks, scope maps, trackers, task rails, stage gates, and delivery/status notes;
5. prior КП, sector/service matrices, client-info briefs, interview briefs, analog briefs, and research packets;
6. stykovye / adjacent artifacts: product vitrine, content candidates, 2-ka/5-ka/8-ka links, methodology notes, accepted decisions, or constraints that change competitor interpretation.

The internal context pack should answer:

- what project / client / market question this competitor research serves;
- what decision the research should inform;
- what products/services/segments are in scope;
- what competitors are already known, where they were mentioned, and why they might matter;
- what hypotheses, constraints, promises, or open questions already exist;
- what language / positioning / sales argument should be tested against competitors;
- what must not be sent externally because of DLP.

## Competitor Mention Discovery

When the skill is launched inside a project context, search internal project artifacts for competitor mentions before external research.

Check:

- storyline/storyboard;
- project passport/card/README/start message;
- subpassports, tracks, trackers, scope maps, task rails;
- prior КП, matrices, client-info, interview briefs, analog briefs;
- meeting notes, research packets, content candidates, product-vitrine links, accepted decisions;
- Notion/Drive project context if available through connectors.

Classify mentions:

- `confirmed_by_ilya`: explicitly named by Ilya as competitor;
- `project_candidate`: mentioned in project artifacts as competitor / аналог / альтернатива / игрок рынка;
- `weak_signal`: appears in passing, source list, news, case, or benchmark;
- `not_competitor`: mentioned but not relevant as competitor.

Admission rules:

- direct / main competitors enter the main competitor matrix only after explicit confirmation from Ilya;
- internal project mentions, external model suggestions, search results, and source-list co-occurrence can create only `project_candidate` or `weak_signal` entries until Ilya confirms them;
- auxiliary / secondary competitors may be kept as candidates when they help interpret the field, but must be separated from confirmed direct competitors;
- international benchmarks are not direct competitors by default. Treat them as a best-practice layer for patterns worth studying, adapting, or rejecting;
- international benchmark lists may be enriched through public search even when the names were not in Ilya's initial competitor list, as long as they remain marked as `international_benchmark` / `best_practice`, not as direct competitors.

Before researching discovered names, ask Ilya to confirm:

```yaml
competitor_mentions_for_confirmation:
  - name: ""
    mention_source: ""
    mention_context: ""
    proposed_type: "direct|indirect|potential|benchmark|unknown"
    confidence: "low|medium|high"
    why_it_may_matter: ""
    needs_ilya_confirmation: true
```

Do not include `project_candidate` or `weak_signal` names in the main competitor matrix until Ilya approves them. If Ilya is unavailable and a quick scan is still useful, keep them in a separate `unconfirmed_mentions` section.

If internal artifacts are unavailable, say so explicitly:

```yaml
internal_context_preflight:
  status: "found|partial|not_found"
  checked_sources:
    - "storyline/storyboard"
    - "project passport/card"
    - "subpassports/tracks"
    - "trackers/stage gates"
    - "prior КП/matrices/briefs"
    - "adjacent artifacts"
  usable_context: []
  missing_context: []
  dlp_constraints: []
```

Do not block the research if no internal context exists, but mark the run as `external-heavy` and lower confidence for project-specific recommendations.

## PP Competitor Analysis Canon

When using the Notion / Drive PP materials as reference, preserve these ideas.

### Strategic Uses

Competitor analysis should answer what business decision changes, not just what competitors do.

Use it for:

- market attractiveness and barrier assessment;
- unique value proposition and white-space search;
- price and perceived-value strategy;
- marketing investment allocation;
- growth opportunities and weak-signal detection;
- strategic risk reduction before competitors move;
- sales and proposal argumentation;
- product/showcase positioning.

Always classify implications into three decision levels:

| Level | Meaning | Examples |
|---|---|---|
| tactical quick wins | actions possible quickly with limited resources | adjust message, strengthen proof, add missing FAQ, test underused channel |
| operational optimization | changes across marketing/sales/product/service | CRM/process change, loyalty/onboarding, site UX, sales scripts, service model |
| strategic initiatives | longer-term direction shifts | new product, new segment/geography, repositioning, platform investment, partnerships |

### Competitor Types

Do not stop at obvious direct competitors.

- `direct`: same audience, comparable offer, similar price/value band.
- `auxiliary`: secondary local or adjacent competitor that helps map the field but is not yet a confirmed main comparator.
- `indirect`: solves the same client problem through another model or category.
- `potential`: adjacent or large player that can enter the niche.
- `benchmark`: aspirational player whose practices may be useful even if not a direct threat.
- `international_benchmark`: foreign / global best-practice case used to enrich the analysis with stronger patterns, not to define the direct competitive field.

Deep analysis usually focuses on 3-10 priority competitors. Use prioritization when the list is larger.

Direct competitors require Ilya confirmation. International benchmarks can be proposed and enriched by the research itself, but their output must answer: what practice is worth studying, what should not be copied, why the pattern applies or does not apply, and what local caveats matter.

### Prioritization Logic

Use adapted BANT to decide which competitors deserve deeper work:

- `Budget`: visible resources, marketing/R&D/product investment, capacity to attack.
- `Authority`: ability to shape market standards, thought leadership, brand power.
- `Need`: how directly the competitor solves the same client job.
- `Timeline`: growth speed, launches, expansion, hiring, strategic movement.

### Methods To Include When Useful

- `SWOT`: strengths, weaknesses, opportunities, threats by competitor or cluster.
- `JTBD / substitute analysis`: what job the client hires the solution to do and what alternatives solve it.
- `positioning map`: 2-axis or multi-vector map, with explicit axis rationale.
- `6P / marketing mix`: Product, Price, Place, Promotion, People, Positioning.
- `mystery-shopper / funnel walk`: only when ethical, public, and approved; do not impersonate or bypass access.
- `review mining`: repeat themes from client feedback, with source and sample-size caution.

### Data Collection Logic

Collect through a combination of:

- official/public sources: site, blog, cases, product pages, reports, press releases;
- partner/distributor sources: partner cards, marketplace listings, integration catalogs, reseller descriptions;
- market/public sources: media, industry reviews, analyst/review sites, interviews, events, public databases, reviews;
- documentation sources: docs/support portals, release notes, changelogs, FAQ, API/integration pages;
- professional-community sources: public technical blogs, webinars, conference talks, speaker decks, podcasts;
- internal PP sources: Notion/Drive templates, previous matrices, КП, project evidence;
- analytics clues: SEO, traffic/search visibility, ads libraries, social content, newsletters, job posts;
- primary research if approved: interviews, customer surveys, mystery-shopper style checks.

Do not confuse channel activity with channel effectiveness. If a competitor is active somewhere, mark this as observed activity, not proof of ROI.

### Source Priority Template

Every outbound prompt should include a sector-adapted source priority list. If Ilya does not specify one, use this default and let the external machine adapt names to the sector:

1. official company site, product pages, pricing/packaging pages, cases, documentation/support portals;
2. partner cards, marketplace listings, distributor/reseller descriptions, integration catalogs;
3. profile/industry media, analyst/review sites, databases, public rankings, procurement/tender pages;
4. professional blogs, technical posts, public talks, conferences, webinars, podcasts;
5. public reviews, forums, social/public content, newsletters, job postings as weak signals.

For each key claim, ask the external machine to label the source type:

- `official_self_claim`: the competitor says this about itself;
- `partner_or_channel_claim`: partner/distributor/integrator describes the competitor;
- `third_party_claim`: media/analyst/review/database says this;
- `documentation_evidence`: docs/support/release notes show actual functional depth;
- `inference`: reasoned conclusion from signals, not a direct fact.

Do not infer market share, revenue, client scale, financial strength, implementation quality, or adoption level unless direct sources support it.

### Analysis Criteria

At minimum, check:

- product/service line depth and breadth;
- functionality, quality, innovation, packaging;
- pricing, discounts, loyalty, payment terms, price/value perception;
- target clients, ICP, segments, industries, geography;
- sales channels, partner network, direct/indirect distribution, marketplace presence;
- sales process clues: lead magnets, CTAs, demos, consultations, onboarding, objection handling;
- service/customer experience: support channels, speed promises, self-service, reviews;
- marketing and promotion: channels, content formats, social cadence, SEO, email/newsletter, ad messaging;
- positioning and message: category claim, USP, proof, tone, visual artifacts;
- digital presence: UX/UI, mobile, speed clues, personal account/app/integrations;
- reputation and media: mentions, executives, events, awards, negative themes;
- operational/technology clues: automation, AI, integrations, team/hiring signals.

### Output Forms

Choose the output form by decision use:

- summary comparison table for fast overview;
- detailed report for specialists;
- executive deck for top management;
- positioning map for strategy and messaging;
- dashboard/watchlist for recurring monitoring;
- КП input block for commercial proposal work;
- content/product-showcase implications for 2-ka.

For consulting / strategy / КП / battlecard use, the output must be PPT-ready:

- concise slide bullets;
- tables that can be moved directly into PPT;
- text descriptions of charts and diagrams;
- clear axes, dimensions, and interpretation;
- source labels compact enough to survive slide compression.

### Common Mistakes To Prevent

- copying competitor tactics instead of adapting principles;
- analyzing without a decision question;
- focusing only on direct competitors;
- treating one-off analysis as stable truth;
- ignoring qualitative signals from reviews/interviews/comments;
- presenting hypotheses as facts;
- recommending actions that exceed internal resources;
- generating too many recommendations without impact/effort priority;
- excluding sales/product/service teams from interpretation when their context matters.

### Cadence

Use cadence by risk:

- monthly: critical metrics, launches, visible website/positioning/pricing changes;
- quarterly: full analysis of key competitors;
- annually: strategic competitive-landscape review.

For recurring work, hand off to `monitor` mode and require update threshold: report only changes that alter decision, risk, opportunity, timing, evidence confidence, or next action.

## Mode Router

| Mode | Trigger | Output |
|---|---|---|
| `outbound-prompt` | default mode; Ilya wants GPT Pro / Perplexity / external machine / dry run / preflight | external research prompt + context pack + output schema |
| `source-plan` | competitor list exists but research scope is unclear | competitor research brief + source plan for outbound prompt |
| `lean-competitor-scan` | fast comparison, 3-5 competitors, limited time | outbound prompt for compact matrix + first conclusions |
| `full-competitor-map` | strategic work, КП, positioning, product strategy, market entry | outbound prompt for detailed competitor intelligence packet |
| `website-positioning-audit` | focus on sites, messaging, UX, product pages, SEO/search clues | outbound prompt for positioning and sales-surface report |
| `marketing-mix-comparison` | focus on 6P / channels / promotion / pricing / sales clues | outbound prompt for marketing mix matrix |
| `partner-intelligence` | target entities are partners, integrators, distributors, resellers, channel multipliers, or lead sources | outbound prompt / return-packet with public readiness, lived partner map gaps, channel conflict hypotheses, and partner enablement requirements |
| `monitor` | recurring competitor watch | outbound prompt for watchlist, change log, alerts, significance threshold |
| `local-execution` | only when Ilya explicitly asks Codex to execute the research itself | completed local competitor packet |
| `return-packet` | Ilya brings external/Notion/Perplexity output back | accepted/change/defer/reject packet |

## Workflow

Default workflow for Codex is prompt construction, not full research execution.

1. Frame the decision use: why we analyze competitors and what decision will change.
2. Run Internal Context Preflight:
   - collect storyline/storyboard, project passport, subpassports, tracks, trackers, prior КП/matrices/briefs, and adjacent artifacts when available;
   - build a compact context pack for the external executing model;
   - separate usable internal context, missing context, and DLP constraints.
3. Normalize competitor list:
   - confirmed direct / main competitors, only after Ilya confirmation;
   - auxiliary or secondary competitors, separately marked;
   - indirect substitutes;
   - potential entrants;
   - international benchmark / aspirational players as a best-practice layer, with optional enrichment through public search.
   - if the list contains partners / integrators / distributors / resellers / channel multipliers, switch those entities into `partner-intelligence` semantics and do not treat them as competitors unless direct substitution is separately evidenced.
4. If direct competitors are not explicitly confirmed, stop and ask Ilya which names are direct/main competitors before creating the final outbound prompt. If a draft prompt is still useful, mark all unconfirmed names as candidate-only.
5. Build source plan for the external machine:
   - official site pages;
   - reports / presentations / filings;
   - news and interviews;
   - search and positioning surfaces;
   - products and pricing clues;
   - clients, sectors, cases, partners;
   - channels, promotion, content, events;
   - public reviews and reputation;
   - job postings / team signals if useful.
6. Generate an outbound prompt that tells ChatGPT Pro / Perplexity / other machines to collect evidence with source links and dates.
7. Require the external machine to fill the competitor matrix by comparable criteria.
8. Require the external machine to build claim ledger: claim, source, evidence grade, confidence, implication.
9. Require source separation:
   - what competitors explicitly say;
   - what can be observed;
   - what is inferred;
   - what is unknown.
10. Require synthesis:
   - competitor archetypes;
   - positioning map;
   - white spaces;
   - threats;
   - copy/do-not-copy patterns;
   - implications for product, КП, sales, content, and strategy.
   - an executive summary first: 5-7 management conclusions before detailed schema;
   - SI-ready synthesis: what concrete slide intents / storyline moves emerge from the combined evidence, not from isolated facts.
11. Require evidence discipline for threat and positioning:
   - public visibility vs real deal threat;
   - positioning claims vs verified facts;
   - hidden / low-visibility competitors;
   - weakly sourced players that must not enter client-facing battlecards;
   - forbidden market shortcuts;
   - what later CRM / BPM-4 / win-loss / support data would improve.
   - for partner intelligence: public visibility vs lived partner map, public readiness vs actual lead quality, possible channel conflict vs proven deal conflict, and final ranking ban until field correction.
12. Require segment playbooks when the category contains different jobs, segments, routes, or buying contexts.
13. Require visual and analytical artifacts, not only text:
   - comparison tables;
   - competitor heatmap;
   - positioning maps;
   - bundle vs synergy / platform proof diagram when relevant;
   - 2x2 or multi-axis matrices;
   - radar / scorecard tables when useful;
   - claim confidence matrix;
   - funnel or sales-motion схемы;
   - sales play table;
   - benchmark best-practice map;
   - timeline of important launches/news when useful.
   - a slide-ready exhibit pack: 6-8 exhibit candidates with title, visual type, claim, source strength, SI/SIF function, readiness, and missing evidence.
14. Require a battlecard layer when decision use includes КП, sales argument, competitive defense, or positioning:
   - where they win: situations, segments, proof, or product scope where the competitor is genuinely strong;
   - where we win: situations where our offer / logic / proof is stronger;
   - when to concede: cases where the competitor may be a better fit and we should not force the fight;
   - where not to fight: weak comparison angles, unprovable attacks, or categories where evidence is insufficient;
   - typical competitor claims / landmines;
   - calm counter-argumentation;
   - safe client-facing wording.
15. Forbid crude negative battlecard frames:
   - do not use `у них нет платформы`, `they are not a platform`, `у них нет X`, or similar as the main battlecard logic;
   - if platform scope is relevant, replace the crude frame with a fair comparison: what the competitor actually has, where it works, where its public proof/scope is narrower, where we win, and when to concede;
   - do not create strawman battlecards. A strong battlecard must make the competitor look real before it explains our advantage.
16. Require the external machine to return unclear questions, missing context, and assumptions separately.
17. Require main body / appendix separation:
   - main body: executive summary, top decisions, slide-ready exhibits, top claim usability, battlecards, next actions;
   - appendix: full claim ledger, long competitor matrices, source tables, raw detail.
18. Require top claims by usability:
   - client-ready;
   - internal-only;
   - needs source-check;
   - do-not-use / risky.
19. Require a sales-play table when decision use includes КП, sales argument, battlecards, product strategy, or market entry:
   - trigger event;
   - buyer;
   - entry product / entry claim;
   - expansion path;
   - proof metric;
   - likely competitor;
   - partner role;
   - objection;
   - recommended response.
20. Require a hypothesis verdict table when the task includes hypotheses or a positioning/platform question:
   - hypothesis;
   - verdict: supported / partially supported / weak / contradicted / not enough evidence;
   - evidence;
   - confidence;
   - implication.
21. Require dynamic rail references when the packet produces slide hypotheses, SI/SIF clusters, BPM-6/7A/7B visuals, or storyboard-ready exhibits:
   - link each candidate to the relevant dynamic rail: BPM-SI / Storyline-Storyboard / project rail / content or commercial rail if relevant;
   - mark whether it is `rail_update_candidate`, `needs_bmsi_router`, `appendix_only`, or `no_rail_update`;
   - do not treat the slide proposal as complete until it has a proposed rail destination or a no-op reason.
22. Return the outbound prompt to Ilya. Do not run the research unless Ilya explicitly instructs local execution.
23. When Ilya brings back the external answer, use `return-packet` mode to classify accepted/change/defer/reject and propose writeback candidates only after approval.

## Return-Packet Self-Reflection Governance

When Ilya brings back an external `competitor-research` result, treat the `self_reflection` block as a suggestion backlog for improving skill operation.

Rules:

- self-reflection items are not accepted automatically;
- do not patch this skill, `deepresearch`, `SKILLS.md`, APQ, rules, prompts, or automations directly from self-reflection suggestions;
- before extracting suggestions for skill improvement, run industry/project specificity cleanup: remove or ignore concrete sector names, competitor names, client names, product names, geography, regulations, technologies, and one-off project facts unless they reveal a reusable research failure mode;
- convert self-reflection into general patterns only: source-class gaps, evidence gates, hidden-player discovery, role-taxonomy confusion, weak-name normalization, output-contract gaps, visual/storyboard transfer gaps, CRM/win-loss transfer gaps, client-facing claim risks, prompt-scope problems, or DLP/writeback problems;
- route project-specific facts separately through the project return packet, `tunnel`, BPM Storyline-Storyboard, claim ledger, or no-op; do not canonize them as skill rules;
- first extract the suggestions into a short `skill_improvement_suggestions` list;
- if the suggestion changes this skill, `deepresearch`, BPM routing, client-facing battlecard policy, or reusable research standards, route it through `skill-system-governance` and require `skill-eval-harness` regression coverage before treating the patch as complete;
- for partner-intelligence packets, also extract every data limitation from self-reflection into `partner_data_gap_packet`, especially missing CRM, win-loss, partner performance, lead quality, conversion, margin, closed portal, or filled lead brief evidence;
- discuss the suggestions with Ilya and ask what to accept, change, defer, or reject;
- after Ilya accepts a suggestion, apply it through the normal skill-edit / writeback gate;
- if the external answer lacks self-reflection, mark `self_reflection_missing: true` and ask whether to rerun or proceed without that improvement signal.

Required `partner_data_gap_packet` classification:

| item | meaning |
|---|---|
| `accepted_gap` | real data gap that should constrain conclusions or become a field question |
| `already_covered` | already present in client/internal data or project artifacts |
| `new_task_candidate` | should become a task, interview question, CRM check, lead brief change, or analysis request |
| `ignore` | not useful, not ethical, too expensive, or outside project scope |
| `skill_improvement_candidate` | should improve this skill or an adjacent skill after Ilya accepts it |

For partner-intelligence packets, convert the self-reflection into this table before concluding:

| public_claim | missing_client_data | interview_owner | CRM_or_source_field | deck_usability | action |
|---|---|---|---|---|---|

## Outbound Prompt Contract

When generating a request for ChatGPT Pro 5.5, Perplexity, or another external research machine, output a ready-to-paste prompt with this structure:

Single-copy rule:

- the final outbound prompt shown to Ilya must be one copyable block;
- do not split the prompt into separate code blocks for schema, self-reflection, evidence grades, or appendices;
- if wrapping the whole prompt in a fenced block, use one outer `text` fence and do not use nested triple backticks inside it;
- put `self_reflection` inside the main required output schema, not as a separate copyable block after the schema;
- after the final outbound prompt block, do not add additional prompt text that Ilya would also need to copy.

```markdown
# Competitor Research Request

## Role
You are an external competitor-intelligence researcher. Your task is to build a source-backed competitor research packet. Do not treat your output as canonical; it will be reviewed by Codex and Ilya.

## Language
Answer only in Russian unless Ilya explicitly asks for another language. Keep source names and direct source titles in their original language when needed, but all analysis, conclusions, tables, and questions must be in Russian.

## Format
Return the answer in Markdown. Do not return only raw YAML or a database-like dump. YAML-like structures are allowed only inside clearly titled Markdown sections when they make the packet easier to transfer into Codex.

## Context Pack
- Target company / product / market:
- Geography:
- Industry/category:
- Decision use:
- Depth:
- Preferred source priority:
- Preferred visual format:
- BPM / SI visual intent:
- Need direct marketing-language quotes: yes/no
- Need battlecard layer: yes/no
- Internal context that can be used:
- Sensitive context that must not be repeated or exposed:

## Competitor Admission Rules
- Direct / main competitors are only the names explicitly confirmed by Ilya.
- Project mentions and your own discoveries are candidates only until confirmed.
- Auxiliary competitors must be separated from direct competitors.
- International benchmarks are a best-practice layer, not direct competitors.
- You may enrich international benchmarks through your own public search, but keep them marked as benchmark / best-practice.

## Confirmed Direct Competitors
- ...

## Candidate / Auxiliary / Unconfirmed Competitors
- ...

## International Benchmarks To Consider Or Enrich
- ...

## Execution Priorities
Use this priority ladder unless Ilya supplies a different one:

- P0: the main strategic / positioning question, especially platform value vs bundle/suite/synergy when relevant.
- P1: confirmed direct competitors approved by Ilya.
- P2: auxiliary / adjacent / substitute / local competitors.
- P3: international benchmarks used as best-practice references, not as direct competitors.

## Definition Of Success
The result must allow Ilya/Codex to:

- choose one primary positioning territory or state that evidence is insufficient;
- explain whether the target offer is platform value, bundle, suite, workflow, or synergy;
- prepare 3-5 sales plays;
- split recommendations into segment playbooks when the market has different jobs, buying contexts, or routes;
- produce mini-battlecards for the most important confirmed competitors;
- separate safe claims, risky claims, and claims to avoid;
- produce a hypothesis verdict table with evidence and confidence.

## Platform / Bundle / Synergy Proof Standard
Do not call any player a platform only because it has several products. Count platform or synergy value only when evidence supports cross-product workflows, unified identity/entity/customer model, shared policy/risk/reporting logic, event integration, unified audit evidence, shared data/orchestration layer, or measurable customer outcome from combined use.

If evidence is weak, label the claim as bundle, suite, possible synergy, or platform claim not proven.

## Public Visibility, Positioning Claims, And Real Threat
Do not treat public visibility as real sales threat.

Separate:

- `public_visibility`: search/media/site visibility and public proof;
- `positioning_claim`: what the competitor says about itself;
- `deal_level_threat`: requires CRM, win-loss, support, objections, deal notes, or other internal evidence;
- `unknown_until_internal_data`: cannot be ranked confidently without client-side data.

Competitor positioning claims are important for messaging analysis. Preserve them as positioning evidence, but do not turn them into market share, adoption, implementation quality, or customer success claims.

If CRM / win-loss / support / SKU / segment data is not available, say clearly that threat ranking is based on public visibility and evidence quality only. Also state what BPM-4 / CRM data would improve the conclusion later.

## Hidden / Low-Visibility Competitors
Search for players that may be commercially relevant but weakly visible online:

- local dealers, distributors, integrators, installers, and implementation partners;
- white-label / private-label / OEM offers;
- regional suppliers and niche providers;
- project-based providers that sell a solution rather than a named product;
- substitutes that solve the same client job through another category;
- marketplaces, tender mentions, partner catalogs, and industry directories.

Keep them separate as `hidden_or_low_visibility_candidate` unless there is strong evidence or Ilya confirmation.

Hidden-source pass:

- tender / procurement traces, RFP/specification pages, and award records;
- job postings and team pages as weak capability signals;
- public registries, classifiers, certificates, licenses, and accreditation records;
- exhibition catalogs, association directories, sponsor/speaker lists, partner directories, and supplier catalogs;
- reseller, dealer, white-label, OEM, implementation, service, and specification channels.

If these sources are not checked, call the hidden-competitor block a question map, not a final threat map.

## Role Taxonomy And Weak-Name Normalization
Do not put all found organizations into one competitor bucket.

Classify every meaningful player as one of:

- manufacturer;
- integrator;
- supplier;
- distributor_or_dealer;
- service_provider;
- project_institute_or_specifier;
- white_label_or_oem;
- substitute;
- benchmark_only;
- unknown.

For raw-list names, weakly visible names, OCR/transcript names, and one-source names, build a normalization table:

| raw_name | normalized_name | role_type | confirmation_status | evidence_used | client_facing_use |
|---|---|---|---|---|---|

Use `normalized_candidate` until the name is supported by a primary public source, registry/tender/catalog trace, or Ilya/internal confirmation. Normalized candidates may appear in hidden candidates, confirmation questions, or appendix, but not in main threat ranking or client-facing battlecards.

## Forbidden Market Shortcuts
Do not use the following as facts without direct evidence:

- marketplace volume or listing count as market size;
- SEO/media/public presence as market share;
- partner, marketplace, or integration listing as proof of active implementations;
- channel presence as proof of sales effectiveness;
- public case/logo as proof of current scale or satisfaction;
- broad claims such as `leader`, `platform`, `ecosystem`, `enterprise-ready`, or `market is large` without evidence.

These signals may be used for positioning analysis and hypotheses, but they must be labelled as such.

## Segment Playbooks
If the category contains different jobs, buying contexts, routes, or implementation models, do not return one generic strategy.

Create playbooks by segment:

- segment / buying context;
- client job-to-be-done;
- confirmed / likely competitors;
- hidden competitors to check;
- positioning territory;
- sales play;
- where we win / where they win / when to concede;
- what public evidence supports;
- what BPM-4 / CRM / win-loss / support data would change;
- client-facing claims to use or avoid.

Use statuses: `core`, `adjacent`, `defensive`, `research_only`.

## Next Evidence Layer / BPM-5 Candidate
If public research cannot resolve practical competitor threat, recommend a next evidence layer instead of overclaiming.

Possible sources: real КП, specifications, tender requirements, RFPs, approved mystery-shopping / funnel walk, demo or pricing request traces, win-loss interviews, customer / integrator / partner interviews, support / implementation pain data.

Mark this as a `BPM-5 candidate` for Codex/Ilya discussion, not as mandatory work inside this run.

## Research Tasks
1. Analyze official sites, product pages, cases, reports, public news, search visibility, channels, promotion, sales clues, clients/sectors, pricing clues, and reputation.
2. Use source priority in this order unless the sector requires adaptation: official product pages and docs; partner/marketplace cards; industry media and analyst/review sites; professional blogs and public talks; reviews/forums/social/job postings as weak signals.
3. Build a comparable competitor matrix.
4. Build a separate benchmark best-practices section: what to adapt, what not to copy, applicability, caveats.
5. Separate public facts, internal/contextual facts, and inferences.
6. Label key claims by source type: official self-claim, partner/channel claim, third-party claim, documentation evidence, or inference.
7. Provide source links and dates for every important claim. When useful, point to the exact page type: product page, partner page, documentation, case, pricing, event, media article.
8. Do not infer market share, financial figures, adoption level, or implementation quality without direct sources.
9. Start with an executive summary: 5-7 management conclusions before the detailed packet.
10. Build SI-ready synthesis: explain what concrete slide intents, storyline moves, evidence blocks, and decision points emerge from the combination of competitor data, claims, visuals, benchmarks, and battlecards.
11. Test platform / bundle / synergy claims if relevant, using the proof standard above.
12. Build 3-5 sales plays if the decision use touches КП, sales, positioning, market entry, or product strategy.
13. End with a hypothesis verdict table if hypotheses were supplied or emerged.
14. Build a storyline synthesis layer if the packet may feed a deck, BPM Storyline-Storyboard, SI/SIF cluster, commercial defense, or strategy narrative.
15. Separate public visibility, positioning claims, and real deal threat.
16. Report hidden / low-visibility competitor candidates separately.
17. Flag weakly sourced players that must not be used in client-facing battlecards.
18. Identify forbidden market shortcuts and downgrade them to hypotheses where needed.
19. Produce segment playbooks when the market is not one homogeneous battlefield.
20. Return contradictions, missing evidence, uncertainty, and questions back to Ilya/Codex.
21. Normalize weak names and classify every meaningful entity by role taxonomy before ranking.
22. Convert sales-motion findings into CRM / win-loss transfer fields where possible.
23. If the raw competitor list is long or weakly normalized, recommend a narrower rerun on 8-10 priority players plus separate procurement/hidden-competitor runs instead of pretending one pass is final.

## Storyline Synthesis Layer
If the output may feed slides, strategy, КП, BPM Storyline-Storyboard, or SI/SIF, add a Markdown section called `Storyline Synthesis`.

It must include:

1. Upper strategic frame: the main logic of the story in 3-5 sentences.
2. Tactical blocks under the frame: 5-8 blocks where evidence should land.
3. Management language: how to describe decisions about route, channel, pricing, margin, service, availability, effort, proof, and direct/partner sales.
4. Tool/interface interpretation: if there is a portal, account, dashboard, CRM, app, or platform-like object, explain its management function, not only IT features.
5. Marketing interpretation: explain how marketing supports sales, channels, partners/dealers, category creation, proof, and conversion, not only traffic.
6. Evidence hierarchy: which slides/claims are main-storyline ready, which should move down to evidence/appendix because proof is weak.
7. Landing map: where new facts should be placed without rewriting the whole storyline.
8. Increment logic: if a previous storyline exists, show what appeared, strengthened, weakened, and needs checking instead of rewriting the entire storyline.

If you recommend changing the whole storyline, explain why incremental landing is insufficient and cite the evidence that forces the change.

Use mostly Russian terminology. Avoid unnecessary English terms when a precise Russian term exists.

## Main Body / Appendix Split
Do not return only a raw schema or long YAML-like database. Separate:

Main body:
1. Executive summary: 5-7 management conclusions.
2. What this changes for positioning / product strategy / sales / storyline.
3. Storyline synthesis if relevant.
4. Slide-ready exhibit pack: 6-8 proposed exhibits.
5. Top claims by usability: client-ready / internal-only / needs source-check / do-not-use.
6. Sales plays: 3-5 if relevant.
7. Battlecard summary.
8. Hypothesis verdict table.
9. Recommended next actions.

Appendix:
1. Full competitor matrix.
2. Full claim ledger.
3. Full source table.
4. Detailed benchmark notes.
5. Raw visual artifacts and long tables.

## Mandatory Visual / Analytical Artifacts
Do not return only prose. Include visualizable artifacts in Markdown:

1. Summary comparison table.
2. Competitor matrix by products, positioning, clients, sales motion, channels, proof, reputation, and evidence grade.
3. Competitor heatmap: competitors x product domains / segments / proof depth / sales relevance.
4. Positioning map: describe axes and place each player on the axes in a table. If possible, add a simple ASCII / Markdown map.
5. Bundle vs synergy / platform-proof diagram when platform-like claims matter.
6. Claim confidence matrix: claim x evidence grade x usability x risk x source type.
7. Sales play table: trigger event, buyer, entry product/claim, expansion path, proof metric, likely competitor, partner role, objection, recommended response.
8. 2x2 or multi-axis matrix for the most important strategic contrast.
9. Radar / scorecard table with criteria and 1-5 scores, with a note that scores are evidence-based estimates.
10. Sales-motion / funnel comparison table or схема.
11. Benchmark best-practices map: practice, benchmark source, why it works, what to adapt, what not to copy, caveats.
12. Timeline of important launches/news/signals if the time dimension changes interpretation.
13. BPM/SI visual layer: recommend which visuals belong to BPM-6, BPM-7A, BPM-7B, what SI/SIF function each visual serves, and whether it is main-storyline ready or only appendix/support.
14. Slide-hypothesis list: for every useful visual, state the possible slide title, storyline role, what it proves, what it does not prove, and missing evidence.
15. Slide-ready exhibit pack: 6-8 concrete slide candidates, each with exhibit title, exhibit type, key claim, source strength, SI/SIF function, storyline role, slide readiness, and what evidence is missing.

For serious competitor work, include a visual-first transfer packet:

- competitor heatmap by priority level (`P1`-`P5` or the provided priority scale), evidence depth, and sales relevance;
- role / arena map separating manufacturers, integrators, suppliers, distributors, service providers, specifiers, white-label/OEM players, substitutes, and benchmarks;
- segment attractiveness x right-to-win matrix;
- manufacturer-vs-integrator / owner-vs-channel map when roles are mixed;
- battlecard sheet and top-5 one-slide battlecards if the output feeds КП, storyboard, or sales defense;
- exhibit titles and slide headlines for every proposed visual;
- color-coded confidence / usability labels: `client-ready`, `internal-only`, `needs_source_check`, `do_not_use`.

## SI-Ready Synthesis
Do not leave the result as separate matrices and observations. After the visual and evidence sections, synthesize the synergy:

- what new storyline becomes possible from the combined evidence;
- what SI / SIF cluster this research can feed;
- which 3-5 slides should be assembled first;
- which evidence blocks belong together on the same slide;
- which claims should remain appendix-only;
- which gaps prevent a slide from becoming main-storyline ready.

## Dynamic Rail References
If a finding creates or changes a candidate slide, SI/SIF cluster, storyline move, battlecard, content angle, КП argument, or project decision, do not leave it isolated in this packet.

For each such item, propose a dynamic rail reference:

- `bpm_si_rail`: BPM-SI / SI/SIF / Storyline-Storyboard linkage;
- `project_rail`: project status, owner, next action, stage-gate, project artifact;
- `content_rail_2ka`: content / article / case / product-showcase derivative;
- `commercial_rail_2ka`: КП / sales argument / battlecard / proposal defense;
- `knowledge_rail_8ka`: reusable knowledge unit / method pattern / source pack;
- `no_rail_update`: useful inside this packet, but no durable rail update should happen now.

The external model should not update any rail. It should return candidates for Codex/Ilya review:

```yaml
dynamic_rail_references:
  - item: ""
    item_type: "slide_hypothesis|si_sif_cluster|battlecard|claim|visual|benchmark|content_angle|commercial_argument|knowledge_candidate"
    suggested_rail: "bpm_si_rail|project_rail|content_rail_2ka|commercial_rail_2ka|knowledge_rail_8ka|no_rail_update"
    target_artifact_or_database: "BPM Storyline-Storyboard|Матрица BPM — SI|project rail|content backlog|commercial proposal packet|knowledge unit|unknown"
    why_this_rail: ""
    update_type: "add_candidate|strengthen_existing|source_check|appendix_only|no_op"
    needs_bmsi_router: true|false
    approval_required: true
```

## Partner Intelligence Addendum
If the task analyzes partners, integrators, distributors, resellers, lead sources, or channel multipliers, add a dedicated partner section before battlecards.

Required partner-intelligence outputs:

- explicit statement: `This is a public evidence map, not the client's lived partner map, until reconciled with internal/client evidence.`;
- normalized partner list and role matrix;
- public readiness scorecard, clearly labeled as public-only;
- help / hinder hypotheses;
- possible channel conflict map, without calling partners competitors unless they sell direct substitutes;
- weak-signal table with evidence class and caveats;
- `partner_intelligence_self_reflection_gate` table;
- `partner_data_gap_packet`;
- questions for Konakov / Ekaterina / CRM / sales / presales / marketing / support;
- lead brief implications;
- enablement hypotheses that require field correction before becoming final recommendations.

Do not produce a final ranking of `best partners for the client` without field correction. It is acceptable to rank `public_readiness`, `visible_identity_relevance`, and `enablement_priority_hypothesis`.

## Battlecard Layer
If decision use includes КП, sales, positioning, competitive defense, or product strategy, add slide-ready bullets:

- Where they win: situations, segments, proof points, integrations, buying contexts, or product scopes where this competitor is genuinely strong.
- Where we win: situations where our offer, logic, implementation path, evidence, or category framing is stronger.
- When to concede: scenarios where the competitor may be a better fit and we should not force the comparison.
- Where not to fight: weak angles, unprovable claims, unfair comparisons, or topics where evidence is insufficient.
- Strengths: what the competitor actually has and can credibly claim.
- Weaknesses: where the public evidence shows gaps, narrower coverage, or weaker proof.
- Typical landmine: how this competitor may attack us / frame the category.
- Counter-argumentation: calm professional response.
- Proof needed: what evidence is still missing before using this in a client-facing battlecard.

Forbidden rough battlecard frames:

- Do not use `у них нет платформы`, `they are not a platform`, `у них нет X`, or similar as the main argument.
- If platform breadth or suite scope matters, describe it fairly: what they actually have, where it works, where public evidence shows narrower scope/proof, where we win, and when to concede.
- Do not build strawman battlecards. The comparison must be fair enough that it would survive a knowledgeable buyer or the competitor reading it.

Client-facing battlecard exclusions:

- do not use claims about concrete losses to a competitor without CRM / win-loss / tender / primary evidence;
- do not claim price superiority or infer discount strategy from weak public clues;
- do not call a competitor a real deal-level threat only from official self-claims, media visibility, SEO, catalogs, or partner listings;
- do not use weak raw-list names, normalized candidates, or hidden candidates in client-facing battlecards before source-check;
- use safer wording: `publicly visible claim`, `hypothesis to verify`, `requires win-loss/source check`, or `appendix-only signal`.

## Professional Russian Language
Use Russian professional consulting language. Avoid literal кальки from English if they sound unnatural. If the category has accepted English terms, keep the term but explain it in Russian. Prefer precise category language over marketing fog.

## Self-Reflection / Improvement Notes
After the main report, add a short self-reflection block. Answer in first person, 1-3 sentences per question. Use it as quality control for the current answer and as improvement input for the next run.

Required questions:

1. What was missing from my answer to make the competitor analysis more useful?
2. Where did I provide too much prose and not enough tables, diagrams, or slide-ready artifacts?
3. Which visualizations, charts, matrices, or slide hypotheses should be added next?
4. Which competitors, substitutes, auxiliary players, or benchmarks may be missing?
5. Which sources or source classes were underused?
6. Which weak names, raw-list entities, OCR/transcript names, or one-source players require normalization before ranking?
7. Where did I fail to separate manufacturer, integrator, supplier, distributor, service provider, specifier, white-label/OEM, substitute, and benchmark roles?
8. Where did I rely too much on official self-claims instead of partner, third-party, documentation, tender/procurement, registry/certificate, or evidence-based signals?
9. Which claims are weakest or most at risk of being overinterpreted?
10. What should not be used in client-facing battlecards until stronger evidence appears, including concrete loss claims, price-superiority claims, and real deal-strength claims?
11. Which assumptions should be confirmed with Ilya or Codex before the next iteration?
12. Which CRM / win-loss / tender / interview fields would change the sales-motion conclusions?
13. Which BPM-6 / BPM-7A / BPM-7B or SI/SIF visual angles did I not cover well enough?
14. What would make this packet more transferable into PPT / storyboard / КП / battlecards: heatmap, arena map, role map, attractiveness x right-to-win, battlecard sheet, slide headlines, exhibit titles, top-5 one-slide battlecards, or confidence coloring?
15. Should the next run be narrowed to 8-10 priority players, split into procurement/tender trace, or split into regional/hidden-competitor scan?
16. What would I change in the prompt before rerunning the research?
17. What are the 3 highest-leverage next improvements to this output?

For partner-intelligence packets, also answer:

18. Which partner conclusions are only public readiness, not lived partner quality?
19. Which claims require Konakov / Ekaterina / CRM / win-loss / partner performance correction before deck use?
20. Which weak signals were used, and how could they distort the picture?
21. Did I accidentally rank partners as best/worst for the client without internal evidence?
22. Did I suggest under-cover / mystery-shopping, and if so did I quarantine it behind explicit approval, ethical/legal check, and a narrow scenario?

Return this block inside the main `competitor_research_packet.self_reflection` schema. Do not output it as a separate code block.

## Required Output Schema
Return the answer using the `competitor_research_packet` schema below.
```

Then include the `Output Contract` YAML schema from this skill inside the same outbound prompt. When showing the prompt to Ilya, preserve the single-copy rule above.

## Output Contract

```yaml
competitor_research_packet:
  target_company: ""
  market_or_category: ""
  geography: ""
  output_language: "ru"
  output_format: "markdown"
  execution_mode: "outbound_prompt|local_execution|return_packet"
  external_machine_target: "chatgpt_pro_5_5|perplexity|other|not_applicable"
  decision_use: "proposal|strategy|positioning|product|market_entry|content|monitoring|other"
  depth: "lean|full|monitor"
  execution_priorities:
    p0_main_strategic_question: ""
    p1_confirmed_direct_competitors: []
    p2_auxiliary_or_adjacent_competitors: []
    p3_global_benchmarks: []
  internal_data_availability:
    crm_or_bpm4_data_available: false
    win_loss_data_available: false
    support_or_service_data_available: false
    sku_or_segment_data_available: false
    partner_performance_data_available: false
    partner_lead_quality_data_available: false
    partner_margin_or_discount_data_available: false
    consequence_for_confidence: ""
    improvement_when_bpm4_complete: ""
    improvement_when_partner_field_correction_complete: ""
  partner_intelligence_gate:
    applies: false
    required_statement: "This is a public evidence map, not the client's lived partner map, until reconciled with internal/client evidence."
    partner_entities_are_not_competitors_by_default: true
    allowed_public_rankings:
      - "public_readiness"
      - "public_visibility"
      - "visible_identity_relevance"
      - "enablement_priority_hypothesis"
    forbidden_without_field_correction:
      - "best_partner_for_client"
      - "highest_actual_lead_quality"
      - "highest_actual_revenue_contribution"
      - "actual_margin_pressure"
      - "actual_deal_conflict"
      - "partner_hides_client"
      - "real_conversion_ranking"
    weak_signal_sources:
      - "vacancies"
      - "Habr_or_professional_blogs"
      - "conference_talks"
      - "tender_or_procurement_traces"
      - "partner_pages"
      - "certified_specialists_or_badges"
      - "webinars"
      - "vendor_or_marketplace_catalogs"
    under_cover_quarantine:
      default_allowed: false
      requires:
        - "explicit_Ilya_approval"
        - "ethical_legal_check"
        - "narrow_written_scenario"
        - "no_impersonation"
        - "no_access_bypass"
        - "no_private_data_collection"
  partner_intelligence_self_reflection_gate:
    - public_claim: ""
      missing_client_data: ""
      interview_owner: "Konakov|Ekaterina|CRM_analyst|sales|presales|marketing|support|unknown"
      CRM_or_source_field: ""
      deck_usability: "client-ready|internal-only|appendix-only|do-not-use"
      action: "accepted_gap|already_covered|new_task_candidate|ignore|skill_improvement_candidate"
  definition_of_success:
    primary_positioning_territory_required: true
    platform_bundle_synergy_explanation_required: true
    sales_plays_required: true
    mini_battlecards_required_for: []
    claim_risk_separation_required: true
    hypothesis_verdict_required: true
  threat_and_positioning_discipline:
    public_visibility_vs_real_threat_caveat: ""
    positioning_claims_to_analyze:
      - claim: ""
        competitor: ""
        why_it_matters_for_positioning: ""
        not_proven_as: []
    deal_level_threat_evidence:
      available: false
      sources: []
      missing_data_needed: []
    weakly_sourced_players:
      - player: ""
        why_weak: ""
        allowed_use: "internal_hypothesis|source_check_only|do_not_use_client_facing"
    forbidden_market_shortcuts_found:
      - shortcut: ""
        where_it_appeared: ""
        safer_interpretation: ""
        needed_evidence: ""
  platform_bundle_synergy_proof:
    platform_claim: ""
    verdict: "platform_value|bundle|suite|workflow|possible_synergy|platform_claim_not_proven|not_applicable"
    evidence:
      cross_product_workflows: []
      unified_identity_or_entity_model: []
      shared_policy_risk_reporting_logic: []
      event_integration: []
      unified_audit_evidence: []
      shared_data_or_orchestration_layer: []
      measurable_customer_outcomes: []
    confidence: "low|medium|high"
    implication: ""
  executive_summary:
    - conclusion: ""
      why_it_matters: ""
      evidence_strength: "low|medium|high"
      decision_impact: ""
  main_body:
    positioning_implications: []
    product_strategy_implications: []
    sales_argument_implications: []
    storyline_implications: []
    first_slides_to_build: []
  storyline_synthesis:
    upper_strategic_frame: ""
    tactical_blocks:
      - block_name: ""
        role_in_storyline: ""
        evidence_to_land_here: []
        caveats: []
    management_language:
      revenue_margin_management: []
      channel_or_route_management: []
      service_availability_proof: []
      direct_vs_partner_sales: []
    tool_or_interface_interpretation:
      object: ""
      management_function: ""
      not_only_it_block: true
    marketing_interpretation:
      role_beyond_traffic: []
      channel_sales_support: []
      proof_or_category_support: []
    evidence_hierarchy:
      main_storyline_ready: []
      move_down_to_evidence_or_appendix: []
      needs_more_proof: []
    landing_map:
      - new_fact_or_signal: ""
        target_storyline_block: ""
        reason: ""
        rewrite_whole_storyline: false
    storyline_increment:
      appeared: []
      strengthened: []
      weakened: []
      needs_check: []
      proposed_slide_changes:
        - slide_or_block: ""
          change_type: "add|strengthen|move_down|merge|remove|no_change"
          reason: ""
          evidence_status: "ready|evidence_pending|weak|contradicted"
      full_rewrite_needed: false
      why_increment_is_not_enough: ""
  appendix_map:
    full_competitor_matrix: "included|omitted|not_applicable"
    full_claim_ledger: "included|omitted|not_applicable"
    full_source_table: "included|omitted|not_applicable"
    detailed_benchmark_notes: "included|omitted|not_applicable"
    raw_visual_artifacts: "included|omitted|not_applicable"
  internal_context_preflight:
    status: "found|partial|not_found"
    checked_sources:
      - "storyline/storyboard"
      - "project passport/card"
      - "subpassports/tracks"
      - "trackers/stage gates"
      - "prior КП/matrices/briefs"
      - "adjacent artifacts"
    usable_context: []
    missing_context: []
    dlp_constraints: []
  competitor_mentions_for_confirmation:
    - name: ""
      mention_source: ""
      mention_context: ""
      proposed_type: "direct|indirect|potential|benchmark|unknown"
      confidence: "low|medium|high"
      why_it_may_matter: ""
      needs_ilya_confirmation: true
  confirmed_competitor_list:
    - ""
  competitor_admission:
    direct_competitors_confirmed_by_ilya: []
    auxiliary_competitor_candidates: []
    indirect_or_potential_candidates: []
    international_benchmarks:
      - name: ""
        source: "ilya|internal_context|external_search|external_model"
        best_practice_focus: []
        why_relevant: ""
        not_a_direct_competitor: true
  unconfirmed_mentions:
    - ""
  hidden_or_low_visibility_candidates:
    - name: ""
      candidate_type: "local_dealer|integrator|white_label|regional_supplier|project_provider|substitute|marketplace_or_tender_signal|specifier|service_provider|other"
      source_or_signal: ""
      why_it_may_matter: ""
      evidence_strength: "low|medium|high"
      client_facing_use: "no|only_after_source_check|yes"
  weak_name_normalization:
    - raw_name: ""
      normalized_name: ""
      role_type: "manufacturer|integrator|supplier|distributor_or_dealer|service_provider|project_institute_or_specifier|white_label_or_oem|substitute|benchmark_only|unknown"
      confirmation_status: "confirmed|normalized_candidate|duplicate|exclude|unknown"
      evidence_used:
        - "official_site"
        - "registry"
        - "tender_or_procurement"
        - "certificate_or_license"
        - "exhibition_or_association_catalog"
        - "job_posting"
        - "internal_confirmation"
      client_facing_use: "no|source_check_only|yes"
  role_taxonomy_map:
    - player: ""
      normalized_name: ""
      role_type: "manufacturer|integrator|supplier|distributor_or_dealer|service_provider|project_institute_or_specifier|white_label_or_oem|substitute|benchmark_only|unknown"
      role_evidence: []
      may_enter_main_matrix: false
      may_enter_client_battlecard: false
  competitors:
    - name: ""
      type: "direct|auxiliary|indirect|potential|benchmark|international_benchmark"
      website: ""
      priority: "P0|P1|P2|P3"
  source_plan:
    official_sites: []
    documentation_support_release_notes: []
    partner_marketplace_distributor_cards: []
    reports_and_filings: []
    tender_procurement_rfp_award_traces: []
    public_registries_classifiers_certificates_licenses: []
    exhibition_association_partner_supplier_catalogs: []
    job_postings_and_team_pages: []
    industry_media_analyst_reviews: []
    professional_blogs_conferences_webinars: []
    search_and_seo: []
    product_pricing_pages: []
    clients_cases_partners: []
    social_content_ads_events: []
    reviews_reputation: []
    internal_sources: []
  competitor_matrix:
    - competitor: ""
      products_services: ""
      pricing_policy: ""
      target_clients: ""
      industries: ""
      positioning: ""
      sales_motion_clues: ""
      channels: ""
      promotion_content: ""
      service_customer_experience: ""
      proof_clients_cases: ""
      technology_operations: ""
      reputation_news: ""
      source_links: []
      evidence_grade: "A|B|C|D|X"
  marketing_mix:
    product: ""
    price: ""
    place: ""
    promotion: ""
    people: ""
    positioning: ""
  positioning_map:
    axes:
      - ""
      - ""
    player_positions: []
    white_spaces: []
  claim_ledger:
    - claim: ""
      competitor: ""
      source_family: "internal|external|mixed|inference"
      sources: []
      evidence_grade: "A|B|C|D|X"
      confidence: "low|medium|high"
      contradiction: ""
      implication: ""
      source_type: "official_self_claim|partner_or_channel_claim|third_party_claim|documentation_evidence|internal|inference"
      page_type: "homepage|product|pricing|case|partner|documentation|support|release_note|event|media|blog|review|database|other"
  strategic_implications:
    quick_wins: []
    operational_changes: []
    strategic_options: []
    risks: []
    no_go_or_do_not_copy: []
  segment_playbooks:
    - playbook_name: ""
      status: "core|adjacent|defensive|research_only"
      segment_or_buying_context: ""
      customer_job_to_be_done: ""
      confirmed_or_likely_competitors: []
      hidden_competitors_to_check: []
      positioning_territory: ""
      sales_play: ""
      where_we_win: []
      where_they_win: []
      when_to_concede: []
      public_evidence: []
      bpm4_crm_win_loss_support_data_that_would_change_this: []
      client_facing_claims_to_use: []
      claims_to_avoid: []
  next_evidence_layer:
    bpm5_candidate: true
    why_needed: ""
    evidence_sources_to_collect:
      - "real_proposals"
      - "specifications"
      - "tender_requirements"
      - "approved_mystery_shopping_or_funnel_walk"
      - "demo_or_pricing_request_trace"
      - "win_loss_interviews"
      - "customer_integrator_partner_interviews"
      - "support_or_implementation_pain_data"
    not_mandatory_for_this_run: true
  top_claims_by_usability:
    client_ready:
      - claim: ""
        why_safe: ""
        source_strength: "A|B|C|D|X"
        suggested_wording: ""
    internal_only:
      - claim: ""
        why_internal_only: ""
        source_strength: "A|B|C|D|X"
    needs_source_check:
      - claim: ""
        missing_evidence: []
        next_source_to_check: ""
    do_not_use_or_risky:
      - claim: ""
        risk: ""
        safer_alternative: ""
  benchmark_best_practices:
    - benchmark: ""
      practice_or_pattern: ""
      source_links: []
      what_to_adapt: ""
      what_not_to_copy: ""
      applicability: "low|medium|high"
      caveats: ""
      not_a_direct_competitor: true
  output_forms:
    summary_table: true
    detailed_report: false
    executive_deck: false
    positioning_map: true
    ppt_ready_tables: true
    chart_descriptions_for_ppt: true
    battlecard_layer: false
    two_by_two_or_multi_axis_matrix: true
    radar_or_scorecard: true
    sales_motion_scheme: true
    benchmark_best_practice_map: true
    timeline_if_relevant: true
    bpm_si_visual_layer: true
    slide_hypotheses: true
    slide_ready_exhibit_pack: true
    executive_summary_first: true
    main_body_appendix_split: true
    claim_usability_rating: true
    competitor_heatmap: true
    bundle_vs_synergy_diagram: true
    sales_play_table: true
    claim_confidence_matrix: true
    hypothesis_verdict_table: true
    monitoring_dashboard: false
    proposal_input_block: false
  visual_artifacts:
    summary_comparison_table: []
    competitor_heatmap: []
    priority_heatmap_p1_p5: []
    product_domain_coverage_matrix: []
    role_or_arena_map:
      role_groups:
        manufacturer: []
        integrator: []
        supplier: []
        distributor_or_dealer: []
        service_provider: []
        project_institute_or_specifier: []
        white_label_or_oem: []
        substitute: []
        benchmark_only: []
        unknown: []
      interpretation: ""
    manufacturer_vs_integrator_or_owner_vs_channel_map: []
    segment_attractiveness_right_to_win_matrix: []
    battlecard_sheet_top_players: []
    top_5_one_slide_battlecards: []
    positioning_map:
      axes: []
      player_positions: []
      ascii_or_markdown_map: ""
    bundle_vs_synergy_or_platform_proof_diagram:
      diagram_description: ""
      bundle_signals: []
      synergy_signals: []
      platform_proof_signals: []
      what_is_not_proven: []
    claim_confidence_matrix:
      - claim: ""
        evidence_grade: "A|B|C|D|X"
        usability: "client-ready|internal-only|needs_source_check|do-not-use"
        risk: "low|medium|high"
        source_type: "official_self_claim|partner_channel_claim|third_party_claim|documentation_evidence|internal_source|inference"
        implication: ""
    strategic_2x2_or_matrix:
      axes_or_dimensions: []
      player_positions: []
      interpretation: ""
    radar_or_scorecard:
      criteria: []
      scores: []
      scoring_caveat: "Scores are evidence-based estimates, not measured truth."
    sales_motion_scheme:
      stages: []
      competitor_patterns: []
      implications: []
    sales_play_table:
      - play_name: ""
        trigger_event: ""
        buyer: ""
        entry_product_or_claim: ""
        expansion_path: ""
        proof_metric: ""
        likely_competitor: ""
        partner_role: ""
        objection: ""
        recommended_response: ""
        confidence: "low|medium|high"
    benchmark_best_practice_map: []
    signal_timeline:
      - date: ""
        competitor_or_benchmark: ""
        signal: ""
        source: ""
        implication: ""
    bpm_si_visual_layer:
      bpm_6_competitor_context:
        competitor_positioning_map: ""
        competitor_pyramid_or_arena_map: ""
        product_domain_coverage_matrix: []
        category_reframing_diagram: ""
        claim_source_map: []
        substitute_or_adjacent_services_map: ""
      bpm_7a_market_sizing:
        pam_tam_sam_som_waterfall_or_funnel: ""
        segment_size_assumptions_table: []
        opportunity_pool_map: ""
        capacity_vs_potential_chart: ""
        growth_drivers_restraints_timeline: []
        sensitivity_table: []
        market_sizing_evidence_gaps: []
      bpm_7b_product_industry_region:
        product_industry_region_heatmap: []
        porter_like_forces_map: ""
        value_chain_or_ecosystem_map: ""
        attractiveness_right_to_win_matrix: ""
        gtm_priority_matrix: []
        regional_product_opportunity_map: ""
        risk_opportunity_portfolio: []
    slide_hypotheses:
      - visual_name: ""
        bpm_source: "BPM-6|BPM-7A|BPM-7B|bundle"
        possible_slide_title: ""
        storyline_role: "Situation|Complication|Question|Answer|evidence block|appendix|battlecard|support"
        si_or_sif_function: ""
        what_it_proves: ""
        what_it_does_not_prove: ""
        evidence_needed: []
        slide_readiness: "ready|needs_source_check|appendix_only|do_not_use"
    slide_ready_exhibit_pack:
      - exhibit_title: ""
        exhibit_type: "table|2x2|positioning_map|heatmap|timeline|battlecard|loop_diagram|claim_map|scorecard|other"
        key_claim: ""
        source_strength: "A|B|C|D|X"
        storyline_role: "Situation|Complication|Question|Answer|evidence block|appendix|battlecard|support"
        si_or_sif_function: ""
        source_blocks_to_combine: []
        what_it_proves: ""
        what_it_does_not_prove: ""
        missing_evidence: []
        slide_readiness: "ready|needs_source_check|appendix_only|do_not_use"
        why_this_slide_matters: ""
  si_ready_synthesis:
    emergent_storyline: ""
    si_or_sif_clusters:
      - name: ""
        source_blocks_to_combine: []
        possible_slide_sequence: []
        evidence_gaps: []
    first_3_to_5_slides_to_assemble:
      - slide_title: ""
        exhibit_source: ""
        reason_to_build_first: ""
        readiness: "ready|needs_source_check|appendix_only|do_not_use"
    appendix_only_claims: []
    main_storyline_blockers: []
  dynamic_rail_references:
    - item: ""
      item_type: "slide_hypothesis|si_sif_cluster|battlecard|claim|visual|benchmark|content_angle|commercial_argument|knowledge_candidate"
      suggested_rail: "bpm_si_rail|project_rail|content_rail_2ka|commercial_rail_2ka|knowledge_rail_8ka|no_rail_update"
      target_artifact_or_database: "BPM Storyline-Storyboard|Матрица BPM — SI|project rail|content backlog|commercial proposal packet|knowledge unit|unknown"
      why_this_rail: ""
      update_type: "add_candidate|strengthen_existing|source_check|appendix_only|no_op"
      needs_bmsi_router: true
      approval_required: true
  battlecards:
    - competitor: ""
      where_they_win: []
      where_we_win: []
      when_to_concede: []
      where_not_to_fight: []
      strengths: []
      weaknesses: []
      typical_landmines: []
      counter_argumentation: []
      forbidden_rough_frames:
        - "у них нет платформы"
        - "they are not a platform"
        - "у них нет X"
      fair_comparison_frame: ""
      safe_client_wording: ""
      proof_needed_before_client_use: []
  hypothesis_verdict:
    - hypothesis: ""
      verdict: "supported|partially_supported|weak|contradicted|not_enough_evidence"
      evidence: ""
      confidence: "low|medium|high"
      implication: ""
  source_granularity:
    direct_marketing_quotes_needed: false
    exact_page_type_required: true
    direct_quotes:
      - competitor: ""
        quote: ""
        source_url: ""
        page_type: ""
        why_it_matters: ""
  forbidden_inferences:
    - "market_share_without_direct_source"
    - "financials_without_direct_source"
    - "implementation_quality_without_direct_source"
    - "adoption_level_without_direct_source"
  prioritization:
    impact_effort_matrix: []
    first_actions: []
    do_later: []
    do_not_do: []
  common_mistakes_checked:
    - "copying_without_adaptation"
    - "no_decision_question"
    - "direct_competitors_only"
    - "hypothesis_as_fact"
    - "no_resource_reality_check"
  open_questions: []
  recommended_next_actions: []
  writeback_candidates: []
  skill_improvement_suggestions:
    - suggestion: ""
      source: "self_reflection|codex_return_review"
      why_it_may_help: ""
      proposed_action: ""
      status: "suggestion_needs_ilya_review"
  self_reflection:
    what_was_missing: ""
    too_much_prose_not_enough_visuals: ""
    visualizations_to_add_next: []
    missing_players_or_benchmarks: []
    underused_sources: []
    weak_names_to_normalize_next: []
    role_taxonomy_confusions: []
    official_self_claims_overused: []
    tender_procurement_registry_job_catalog_sources_underused: []
    missing_internal_data_that_would_change_threat_ranking: []
    hidden_or_low_visibility_competitors_to_check_next: []
    forbidden_market_shortcuts_to_avoid: []
    segment_playbooks_to_split_or_refine: []
    crm_win_loss_sales_motion_fields_to_add: []
    bpm5_next_evidence_layer_candidates: []
    overreliance_on_self_claims: ""
    weakest_claims: []
    not_ready_for_client_battlecards: []
    assumptions_to_confirm_with_ilya_or_codex: []
    bpm_si_visual_gaps: []
    ppt_storyboard_battlecard_improvements: []
    rerun_scope_recommendation:
      narrow_to_8_10_priority_players: false
      separate_tender_procurement_run: false
      separate_hidden_or_regional_scan: false
      reason: ""
    prompt_changes_before_rerun: []
    top_3_next_improvements: []
  approval_required_before_writeback: true
```

## Evidence Grades

- `A`: competitor official source, public filing/report, primary public evidence, or accepted internal source.
- `B`: reliable media / several independent public confirmations / strong internal template match.
- `C`: plausible inference from weak or partial evidence.
- `D`: unsupported claim or single weak source.
- `X`: contradicted by available evidence.

## DLP / Externalization Gate

This skill can create client-facing or strategy-sensitive material. Treat outputs as internal by default.

Before externalizing to a client, partner, public channel, ChatGPT Pro, Perplexity, Notion page shared externally, or a deck:

- remove sensitive client/project context;
- separate public competitor facts from Paper Planes internal interpretation;
- do not reveal internal hypotheses, client economics, delivery risks, or confidential source packs;
- anonymize internal analogs unless Ilya explicitly approves disclosure;
- keep quotes short and source-linked;
- mark uncertain claims as inference.

If unsure, stop and ask Ilya for DLP approval.

## Writeback / HITL Gate

Codex may:

- read public sources;
- search Notion/Drive/Readwise if connectors are available and relevant;
- produce outbound prompts, matrices, packets, and candidate ledgers;
- suggest Vault / Reader / content / КП writeback targets.

Codex must ask Ilya before:

- executing the full competitor research locally instead of generating an external prompt, unless Ilya explicitly asked for local execution;
- creating or editing Vault files;
- updating `SKILLS.md`, APQ, product vitrine, КП, content plan, or project artifacts;
- importing sources into Reader;
- sending findings externally;
- turning competitor claims into accepted strategy or client-facing copy.

## Boundaries With Adjacent Skills

| Adjacent skill | Difference |
|---|---|
| `deepresearch` | general research and external review OS; this skill is a specialized competitor intelligence workflow |
| `client-info` | prepares one client/company brief; this skill compares several competitor players |
| `sector-service-matrix-builder` | builds PP service/product matrices; this skill researches competitor market surfaces |
| `commercial-proposal-generator` | writes КП; this skill supplies competitor evidence and positioning implications |
| `trails-generator` | finds knowledge/content trails in Vault; this skill maps competitor evidence from public/internal sources |

## Done Definition

This skill is done when:

- if external execution is intended, a ready-to-paste outbound prompt is produced instead of a completed local research report;
- outbound prompt is delivered as one copyable block, with no required second copy/paste block;
- outbound prompt requires the external answer in Markdown, not raw YAML only;
- outbound prompt requires Russian-only analytical output unless Ilya says otherwise;
- outbound prompt requires executive summary first, before detailed schema or appendix;
- outbound prompt requires visual / analytical artifacts, not only prose;
- outbound prompt requires main body / appendix separation;
- outbound prompt requires execution priorities: P0 strategic question, P1 confirmed direct competitors, P2 auxiliary competitors, P3 global benchmarks;
- outbound prompt includes source-priority, source-type labels, and page-type granularity;
- outbound prompt separates public visibility, positioning claims, and real deal threat;
- outbound prompt preserves competitor self-claims for positioning analysis but does not treat them as market share, adoption, implementation quality, or sales effectiveness;
- outbound prompt requires hidden / low-visibility competitor candidates: local dealers, integrators, white-label/OEM, regional suppliers, project providers, substitutes, marketplaces, tenders, partner catalogs;
- outbound prompt requires a hidden-source pass beyond ordinary web search: procurement/tender traces, job postings, public registries/classifiers/certificates/licenses, exhibition catalogs, association/partner/supplier directories;
- outbound prompt states that hidden competitors are only a `question map` if those sources were not checked;
- outbound prompt requires role taxonomy before ranking: manufacturer, integrator, supplier, distributor/dealer, service provider, project institute/specifier, white-label/OEM, substitute, benchmark, unknown;
- outbound prompt requires weak-name normalization for raw-list, OCR/transcript, one-source, and weakly visible entities before any main-matrix or client-facing use;
- outbound prompt marks weakly sourced players as internal hypothesis / source-check only / not client-facing;
- outbound prompt forbids market shortcuts: listing volume as market size, public presence as market share, integration listing as active deployment proof, channel presence as sales effectiveness proof;
- for partner intelligence, outbound prompt separates public visibility / public readiness from lived partner map / actual lead quality / actual revenue contribution / actual margin pressure;
- for partner intelligence, outbound prompt forbids final best-partner ranking without field correction through Konakov / Ekaterina / CRM / win-loss / partner performance data;
- for partner intelligence, outbound prompt requires weak-signal sources to be labeled as weak evidence and not proof of real deals;
- for partner intelligence, outbound prompt quarantines under-cover / mystery-shopping behind explicit approval, ethical/legal check, and a narrow scenario;
- outbound prompt states what CRM / BPM-4 / win-loss / support / SKU / segment data would improve once available, without blocking early external research;
- outbound prompt recommends a `BPM-5 candidate` next evidence layer when public research cannot resolve practical competitor threat;
- outbound prompt requires segment playbooks when the category contains different jobs, segments, routes, or buying contexts;
- outbound prompt requires claim usability rating: client-ready / internal-only / needs source-check / do-not-use;
- outbound prompt requires claim confidence matrix;
- outbound prompt asks for PPT-ready tables / chart descriptions when output will be used for КП, strategy, sales, or battlecards;
- outbound prompt asks for a slide-ready exhibit pack, not only raw visual artifacts;
- outbound prompt asks for a visual-first transfer packet when the output may feed storyboard, КП, or battlecards: priority heatmap, role/arena map, manufacturer-vs-integrator or owner-vs-channel map, segment attractiveness x right-to-win, battlecard sheet, top-5 one-slide battlecards, exhibit titles, slide headlines, and color-coded confidence;
- outbound prompt requires competitor heatmap and bundle vs synergy / platform-proof diagram when relevant;
- outbound prompt requires 3-5 sales plays when the decision use touches КП, sales, positioning, product strategy, or market entry;
- outbound prompt requires hypothesis verdict table when hypotheses or platform/positioning questions exist;
- outbound prompt requires storyline synthesis when the output may feed slides, BPM Storyline-Storyboard, SI/SIF, КП, or strategy narrative;
- outbound prompt separates strategic frame, tactical blocks, management language, tool/interface role, marketing role, and evidence hierarchy;
- outbound prompt uses storyline increment logic when a previous storyline exists: appeared / strengthened / weakened / needs_check before any full rewrite;
- outbound prompt uses platform proof standard and does not accept `platform` merely because a player has several products;
- outbound prompt asks for SI-ready synthesis: what slide intents and storyline moves emerge from the evidence synergy;
- outbound prompt asks for dynamic rail references for slide/SI/SIF/battlecard/content/commercial candidates, including whether the BPM-SI router should process them;
- outbound prompt asks for BPM-6 / BPM-7A / BPM-7B visual candidates and SI/SIF annotations when the research may feed storyline/storyboard;
- outbound prompt converts sales-motion findings into CRM / win-loss transfer fields when relevant: competitor_in_deal, competitor_role_type, segment/use case, trigger_event, source_type, loss/risk reason, commercial objection, implementation/service objection, and proof needed before battlecard;
- outbound prompt recommends narrowing a rerun to 8-10 priority players or splitting procurement/hidden-competitor runs when the raw list is long or weakly normalized;
- outbound prompt avoids treating `SIEF` as a canonical term and uses `SI / SIF visual layer` instead;
- battlecards use a fair `where they win / where we win / when to concede / where not to fight` structure instead of crude negative framing;
- battlecards explicitly forbid `у них нет платформы`, `they are not a platform`, `у них нет X`, and similar lazy frames as the main argument;
- competitor list is normalized;
- direct competitors are separated from auxiliary competitors and international benchmarks;
- direct / main competitors are marked as confirmed by Ilya, or kept out of the main matrix;
- international benchmarks are framed as best-practice sources, with adapt / do-not-copy / caveats;
- source plan is explicit;
- competitor matrix is filled with evidence grades;
- internal/external/inference sources are separated;
- claim ledger exists;
- public visibility and real sales threat are not collapsed;
- positioning claims are preserved as positioning evidence but downgraded when used as proof of adoption, share, implementation quality, or customer success;
- hidden / low-visibility candidates are listed separately from confirmed direct competitors;
- segment playbooks are produced when one generic strategy would hide important segment differences;
- positioning and marketing mix implications are clear;
- open questions and next actions are listed;
- outbound prompt requires a first-person self-reflection / improvement block after the main report;
- return-packet mode treats self-reflection as suggestions for Ilya review, not as automatic skill changes;
- return-packet mode first cleans self-reflection from industry/project specifics and extracts only reusable skill patterns unless Ilya explicitly asks for a project-specific regression pack;
- return-packet mode routes accepted reusable skill-system improvements through `skill-system-governance` and requires `skill-eval-harness` cases for weak/self-claim exclusion, hidden-player normalization, client-facing battlecard safety, and visual-first artifact output;
- return-packet mode converts partner self-reflection gaps into `partner_data_gap_packet` with `public claim -> client data needed -> interview owner -> CRM/source field -> deck usability -> action`;
- writeback / externalization approval needs are explicit.

Not done if:

- it starts doing the full research in Codex when Ilya needed a prompt for ChatGPT Pro / Perplexity;
- it splits the outbound prompt into several copyable blocks that Ilya must copy separately;
- it lets the external machine answer in English or an unspecified language when Ilya did not request it;
- it returns only YAML / raw schema / database-like output instead of Markdown with readable sections;
- it accepts a prose-only output without tables, matrices, maps, or visualizable artifacts;
- it accepts a raw schema/database output without executive summary and main-body synthesis;
- it produces many visual artifacts but does not synthesize them into concrete SI/slide candidates;
- it produces slide/SI/SIF candidates without dynamic rail references or no-op reasons;
- it lacks claim usability ratings for client-ready vs internal-only vs source-check vs do-not-use;
- it lacks P0-P3 prioritization for complex competitor research;
- it accepts platform/synergy language without proof of cross-product workflows, shared model, shared policy/risk/reporting logic, event integration, audit evidence, shared data/orchestration, or measurable combined outcomes;
- it does not provide sales plays when the research is meant for КП, sales, positioning, product strategy, or market entry;
- it skips hypothesis verdicts when hypotheses were supplied or emerged;
- it skips storyline synthesis when the packet is meant to feed slides, BPM Storyline-Storyboard, SI/SIF, КП, or strategy narrative;
- it rewrites an existing storyline from scratch without first attempting incremental landing into existing blocks;
- it fails to show `appeared / strengthened / weakened / needs_check` deltas when processing new research against an existing storyline;
- it treats a portal, personal account, dashboard, CRM, or similar tool as a standalone IT block when its role is actually service, availability, proof, rules, channel protection, or sales support;
- in partner intelligence, it calls partners competitors without direct substitute evidence;
- in partner intelligence, it ranks `best partners for the client`, actual lead quality, actual revenue contribution, actual margin pressure, or real channel conflict from public sources only;
- in partner intelligence, it treats vacancies, Habr, conferences, tenders, partner pages, certified specialists, webinars, marketplace/vendor catalogs, or public statuses as proof of real deal performance;
- in partner intelligence, it leaves missing CRM / win-loss / partner performance evidence as a prose disclaimer instead of creating a data-gap table;
- in partner intelligence, it recommends under-cover / mystery-shopping without quarantine, explicit approval, ethical/legal check, and a narrow scenario;
- it treats marketing only as traffic when the context requires channel, dealer/partner, sales, proof, or category support;
- it leaves weakly sourced market base/share/region/sizing slides in the main storyline instead of moving them down to evidence/appendix;
- it fails to ask for source type labels and exact page types when source quality matters;
- it asks for visuals but does not require SI/SIF function, storyline role, slide readiness, and missing evidence;
- it canonizes `SIEF` as a methodology term instead of translating the request into SI/SIF visual requirements;
- it uses `у них нет платформы`, `they are not a platform`, `у них нет X`, or similar as the core battlecard frame instead of fair comparison;
- it produces battlecards without `where they win`, `where we win`, and `when to concede`;
- it lets the external machine infer market share, financials, adoption, or implementation quality without direct sources;
- it treats public visibility as proof of real deal threat;
- it treats competitor positioning claims as market facts instead of positioning evidence;
- it ignores hidden / low-visibility competitor candidates when the category likely contains dealers, integrators, white-label/OEM, regional suppliers, project providers, or substitutes;
- it ranks practical threat confidently while CRM / BPM-4 / win-loss / support data is unavailable;
- it collapses several segments or buying contexts into one generic competitor strategy when playbooks are needed;
- it fails to propose a BPM-5 candidate next evidence layer when public research cannot resolve practical threat;
- it only summarizes competitor websites;
- it copies slogans without interpreting positioning;
- it treats inferred sales motion as fact;
- it lacks source links and dates;
- it mixes internal PP interpretation with public facts;
- it produces recommendations without decision use.
- it lacks self-reflection on what was missing, what to improve, and how to change the next prompt.
- it applies self-reflection suggestions as skill changes without discussing them with Ilya first.

## Eval Cases

Good triggers:

- "Вот список конкурентов клиента, собери запрос для GPT Pro / Perplexity по продуктам, позиционированию, клиентам и маркетинговому миксу."
- "Нужно понять, как конкуренты продают услугу X и чем нам отличаться в КП."
- "Сравни сайты конкурентов, отчёты, новости и публичные кейсы по отрасли."
- "Сделай dry run / preflight и подготовь запрос для внешней машины."
- "Нужен CI-пакет для battlecards, чтобы потом быстро перенести выводы в слайды."

Bad triggers:

- "Сделай deep research по рынку без списка конкурентов" -> prefer `deepresearch`.
- "Подготовь brief по клиенту перед встречей" -> prefer `client-info`.
- "Напиши КП с учётом конкурентов" -> competitor research may support, but primary skill is `commercial-proposal-generator`.

Ambiguous:

- "Посмотри конкурентов в целом" -> ask for decision use, geography, and competitor list or permission for discovery pre-pass.
- "Собери анализ конкурентов" -> unless Ilya says to execute locally, produce outbound prompt for external research machine.
- "Сделай анализ по конкурентам и положи в Vault" -> prepare preview; ask before writeback.
- "Добавь международные примеры лучших практик" -> enrich benchmark layer through public search, but do not promote them to direct competitors without Ilya confirmation.
- "В проекте встретились ещё пять игроков" -> show them as candidates for confirmation, not as confirmed direct competitors.
- "Perplexity ответил не по-русски / без графиков" -> patch outbound prompt to require Russian-only output and mandatory visualizable artifacts.
- "Перплексити дал слишком текстовый ответ без battlecards / источников / page types" -> add source priority, page-type granularity, PPT-ready visuals, and battlecard layer to outbound prompt.
- "Это похоже на BPM-6 / BPM-7A / BPM-7B и нужно для SIEF" -> interpret as SI/SIF visual layer; require BPM-specific visuals, slide hypotheses, storyline role, and evidence gaps.
- "Сделай battlecard: у них нет платформы" -> reject the crude frame; require fair comparison with `where they win`, `where we win`, `when to concede`, and evidence-backed platform/scope differences.
- "Нужно доказать, что это платформа, а не набор продуктов" -> require platform / bundle / synergy proof standard, claim confidence matrix, bundle-vs-synergy diagram, and hypothesis verdict.
- "Нужны sales plays по результатам конкурентного анализа" -> require 3-5 plays with trigger event, buyer, entry product/claim, expansion path, proof metric, likely competitor, partner role, objection, and recommended response.
- "Внешняя машина вернула обновленный storyline после конкурентного анализа" -> do not canonize the project-specific storyline; extract reusable storyline-synthesis patterns, weak-evidence demotions, and BPM-SI candidates for Ilya review.
- "Нужно, чтобы ответ был в МД" -> require Markdown output as the default external answer format, with YAML-like schema only inside readable Markdown sections if useful.
- "Пришли новые данные к уже собранному storyline" -> require storyline increment: land facts into existing blocks, show appeared / strengthened / weakened / needs_check, and avoid full rewrite unless evidence forces it.
- "Конкурент хорошо виден в поиске / медиа / маркетплейсе" -> treat as public visibility and positioning signal, not as proof of real deal threat or market share.
- "Нужно понять, кто реально мешает продажам" -> ask for CRM / win-loss / support / deal evidence if available; if unavailable, mark threat ranking as public-evidence-based and lower confidence.
- "В категории могут быть локальные дилеры / интеграторы / white-label" -> require hidden / low-visibility competitor candidates and keep them outside confirmed direct competitors until checked.
- "Публичный research не отвечает, кто реально выигрывает сделки" -> propose BPM-5 candidate next evidence layer: КП, specs, tenders, approved mystery-shopping, win-loss, customer/integrator interviews.
- "Рынок распадается на разные сегменты" -> produce segment playbooks instead of one generic competitor strategy.
