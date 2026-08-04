---
name: deepresearch
description: >-
  Use when Ilya asks for deep research, external ChatGPT Pro / Perplexity review,
  a strong prompt for external research, a controlled second opinion, or a
  decision packet from multi-source evidence. Supports Lean and Full Deep modes,
  recurring monitoring prompts, Vault/Google-Drive-first context, optional
  Notion / Readwise / Drive connector instructions, web/academic/fact source planning,
  monitoring-stack routing, cross-synthesis, 4th-department BPM-7A/B prompt
  generation through BPM exchange, and Codex/Vault write-back routing.
metadata:
  version: "0.1.0"
  status: active
  line: external-deep-research
  source: "adapted from Sergey Khudovekov review loop and Research OS v3 for Ilya's Codex/Vault workflow"
  supports_bpm:
    primary: [BPM-7A, BPM-7B]
    required_secondary: [BPM-2, BPM-3, BPM-4, BPM-6, BPM-10]
    optional_secondary: [BPM-5, BPM-8, BPM-9, BPM-11]
  can_consume: [Vault / Drive / Notion context packs, BPM Storyline-Storyboard, Матрица BPM — SI, public evidence maps, external model outputs]
  can_produce: [outbound deepresearch prompt, decision packet, local return packet, claim ledger, data request checklist, BPM Exchange reconciliation candidates]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# deepresearch

## Purpose

Run a controlled research / external-review loop for expensive reasoning.

`deepresearch` has three jobs:

1. prepare a strong paste-ready prompt for ChatGPT Pro / Perplexity;
2. structure a Lean or Full Deep research cycle through named artifacts;
3. when Ilya brings the external answer back, convert it into a Codex/Vault decision packet.

External models are not source of truth and not execution engines. They provide external evidence and second opinions. Codex still owns source checking, decision routing, and write-back into Vault.

## Principles

- **Vendor-agnostic:** describe roles and outputs, not a specific model dependency.
- **Artifact-first:** each step must produce a named artifact. No artifact means the step did not happen.
- **Vault-first:** use known Vault/project context first, then external sources for gaps and current facts.
- **Source separation:** always distinguish internal Vault/Drive/Notion/Readwise evidence from external web/academic/community evidence and from inference.
- **Two modes:** `Lean` for fast decision support; `Full Deep` for strategic or expensive questions.
- **Roles over tools:** tools are optional execution surfaces; roles are the workflow.
- **Human-in-the-loop:** external output is advisory and durable write-back requires the active Vault rules and Ilya's instruction.

## When To Use

Use when a reasoning error is costly:

- architecture and complex plans;
- disputed strategic choices;
- client materials before finalization;
- methodology, research arguments, risk review;
- market, company, competitor, product, or category research;
- commercial proposals, cases, product-showcase logic, content or strategy artifacts where strong external critique is useful;
- any request like `составь промпт для ChatGPT Pro`, `дай промпт в Perplexity`, `усиль промпт`, `отдадим в Pro`, `нужен внешний второй взгляд`, `сделай deep research`.
- 4th-department project requests for `BPM-7A`, `BPM-7B`, `BPM7AB`, `семь АБ`, market-sizing, market map, market-by-products/industries/regions, category sizing, competitor landscape, buyer-role map, procurement/tender map, or a prompt for those outputs.

Use it even when Ilya asks only for a prompt. In that case produce the external prompt / research bundle and stop.

## Do Not Use

Do not use for:

- routine edits;
- simple summaries;
- ordinary local execution;
- questions Codex can answer directly from available local sources;
- automatic browser/API submission to ChatGPT Pro / Perplexity;
- dumping large raw Vault folders into an external model;
- unapproved community-source extraction, private/community data collection, or closed-platform collection without an accepted entry path.

## Roles

One assistant can perform several roles, but prompts should name the roles when useful.

| Role | Job | Typical surface |
|---|---|---|
| Brief Refiner | Turn raw request into structured research brief | Codex / ChatGPT / Perplexity |
| Vault Context Packager | Summarize internal context and safety constraints | Codex |
| Web Researcher | Live web/media search and current public facts | Perplexity Pro / ChatGPT browsing |
| Academic Miner | Academic and research databases | ChatGPT / Perplexity / direct URLs |
| Data Harvester | Structured public data and APIs | Direct URLs / model browsing |
| Connector Researcher | Narrow Notion / Readwise / Drive connector search when available | ChatGPT / Perplexity / MCP connectors |
| Community Entry Mapper | Finds approved entry paths into community signals without assuming a collection tool | Public search, connectors, exports, RSS, APIs, manual source packs |
| Cross-Synthesizer | Find consensus, conflicts, blind spots, signal quality | ChatGPT / Perplexity |
| Decision Packager | Convert findings into decision packet | Codex |

Community signals are not a default executable layer. First define a lawful and practical entry path: public web indexing, official/public pages, platform search, export, connector, RSS/newsletter, API, or a manual source pack supplied by Ilya.

## Monitoring Stack Architecture

Use this section when Ilya asks to move from one-off research into recurring monitoring, source ingestion, alerts, digests, or source-adapter design.

Default architecture:

```text
source adapters -> normalized event store -> topic rules -> scoring/ranking -> digest/alerts -> Codex/Vault return
```

### MVP Stack

Prefer a Readwise/Reader-first RSS stack. For Ilya's workflow, RSS should first land in Readwise Reader and then enter Codex through the official Readwise MCP. This keeps saved articles, newsletters, feeds, highlights, and reading history in one research-memory layer.

| Layer | Preferred tools | Use now? | Why |
|---|---|---:|---|
| Personal RSS / reading memory | Readwise Reader + official Readwise MCP | yes | primary intake for RSS, newsletters, saved articles, highlights, and Reader documents |
| Orchestration | Readwise saved searches/tags first; Huginn or n8n later | conditional | only add external orchestration if Reader/MCP cannot cover cadence, alerts, or digest routing |
| RSS/API generation | RSSHub, RSS-Bridge | fallback | use only when Reader cannot subscribe to or parse a public source cleanly |
| Feed store/reader | Readwise Reader primary; FreshRSS or Miniflux only if needed | fallback | avoid parallel RSS stores unless Readwise lacks history/API behavior needed for a monitor |
| Hacker News | Official Firebase API + Algolia HN API | yes | avoid HTML collection; query by topic, tag, author, date |
| Substack | native RSS first; Substack2Markdown / sbstck-dl / substack-api only if needed | conditional | prefer RSS; use downloaders only for user-approved public/exportable material |
| Telegram/public channels | local `public_telegram_scraper.py` only if present and explicitly approved; otherwise entry-path discovery | conditional | public preview only; no private chats, no member collection, no account automation |
| Telegram alternatives | streaming_overseer, TeleGraphite, TGDataset, rtgstat | research only | evaluate as entry paths, not default dependencies |
| X.com | twikit, twscrape, Scweet, XActions | quarantine | high breakage risk, cookie/account risk, and Terms-of-Service risk |

### Connection Decision

Use this decision order:

1. **Connect by default:** official Readwise MCP, Readwise Reader RSS/newsletter intake, HN Firebase/Algolia, public RSS/API sources that can land in Reader.
2. **Use as fallback:** RSSHub / RSS-Bridge when a public source needs RSS generation before landing in Reader.
3. **Connect after check:** Huginn/n8n or FreshRSS/Miniflux only if Readwise Reader + MCP cannot provide enough cadence, history, alerting, or API access.
4. **Use only with explicit scope:** Substack downloaders, local Telegram public-preview adapter, third-party Telegram datasets/services.
5. **Do not connect for MVP:** X.com unofficial clients unless Ilya explicitly accepts instability, account/cookie risk, and likely maintenance churn.

### Reader Source Acquisition Packet

When asking ChatGPT Pro / Perplexity to improve research coverage, monitoring, or the skill system, require a separate source-acquisition output. The external model must return what should be added to Readwise Reader, not add it itself.

External models must provide:

```yaml
reader_source_acquisition_packet:
  purpose: ""
  candidate_sources:
    - title: ""
      source_type: "rss|newsletter|substack|book|paper|pdf|website|database|service|youtube|podcast|other"
      url: ""
      rss_or_import_url: ""
      author_or_org: ""
      why_relevant: ""
      job_to_be_done: ""
      expected_signal: ""
      target_use: "research|monitoring|article|proposal|client_context|methodology|market_watch|content_rail|other"
      priority: "P0|P1|P2|P3"
      route_decision: "subscribe|save_to_reader|shortlist|read_now|evidence|watch|skip|needs_review"
      suggested_tags: []
      risks_or_limits: ""
      access_notes: "public|paywalled|requires_login|book_to_buy|file_to_upload|unknown"
  books_to_consider:
    - title: ""
      author: ""
      link: ""
      why_this_book: ""
      priority: "P0|P1|P2|P3"
  services_or_databases_to_consider:
    - name: ""
      url: ""
      what_it_provides: ""
      how_it_feeds_reader_or_research: ""
      priority: "P0|P1|P2|P3"
  do_not_add:
    - source: ""
      reason: ""
```

Rules:

- no `url` or import path means the candidate is incomplete;
- no `why_relevant` or `job_to_be_done` means the candidate is not ready for Reader;
- prefer fewer high-signal sources over broad lists;
- separate RSS/newsletter subscriptions, one-off documents, books, and services/databases;
- mark paywalls, login requirements, copyright limits, and weak evidence clearly;
- do not instruct external models to mutate Readwise/Reader directly.

After Ilya pastes the external answer back into Codex, convert this packet into a local candidate ledger. Only after discussion and explicit approval may Codex add sources/documents to Readwise Reader through the Readwise MCP or another approved import route.

### Adapter Contract

Every source adapter must output normalized events, not raw dumps.

```yaml
event:
  source_id: ""
  source_type: "rss|api|hn|substack|telegram_public_preview|forum|connector|manual_pack"
  source_url: ""
  title: ""
  author: ""
  published_at: ""
  collected_at: ""
  url: ""
  text_excerpt: ""
  tags: []
  matched_rules: []
  score: 0
  rights_and_safety: ""
  raw_ref: ""
```

No adapter should write directly into Vault. The adapter produces events; the research workflow turns them into digest, alert, source table, or decision packet; Codex routes accepted outputs back into existing Vault artifacts.

## Modes

### Mode A: Prompt Only

Use when Ilya asks for a prompt to send to ChatGPT Pro / Perplexity.

Output: paste-ready prompt with structured brief, operating context, source plan if relevant, and expected output.

### Mode B: Lean Research

Use for operational questions, fast checks, first-pass research, and monitoring.

Expected time: about 30 minutes externally.

Artifacts:

1. `Structured Brief`
2. `Source Plan`
3. `Run A`: Perplexity / web-heavy research
4. `Run B`: ChatGPT / files / structured context research
5. `Cross-Synthesis`
6. `Decision Packet`

### Mode C: Full Deep Research

Use for strategic decisions, expensive hypotheses, competitive intelligence, product research, or high-risk client materials.

Expected time: 2-3 hours externally.

Artifacts:

1. `Structured Brief`
2. `Source Plan`
3. `Run A`: Perplexity Deep Research / web + media + facts
4. `Run B`: ChatGPT Pro / files + reasoning + internal context
5. `Run C`: academic / structured database pass where relevant
6. `Run D`: Notion / Readwise / Drive connector pass where relevant and available
7. `Cross-Synthesis`
8. `Grand Synthesis`
9. `Decision Packet`

No community-source run until an approved entry path exists.

### Mode D: Return Packet

Use when Ilya pastes a ChatGPT Pro / Perplexity answer back into Codex.

Output: local decision packet and proposed write-back route.

#### 4ka BPM / Rail Return Gate

When the returned external answer concerns a 4th-department production project and includes market, category, competitor, positioning, sales-model, buyer-role, channel, product, CRM/data, benchmark, reuse, or future deliverable material, treat it as a `BPM-candidate source` until checked.

Before calling the Return Packet complete, run this gate:

```text
external output
-> local return packet
-> massive-ingest check
-> possible BPM increments
-> SI / slide hypotheses
-> lack of knowledge / field questions
-> project Storyline-Storyboard update/no-op
```

For the local return packet, classify the material before proposing any write-back:

```yaml
return_packet_classification:
  input_type: "source|evidence|claim|hypothesis|SI_candidate|rule_candidate|knowledge_unit|task_candidate|mixed"
  source_family: "internal|external|mixed|inference"
  bpm_candidate_source: true|false
  target_artifact: "project_storyline_storyboard|bpm_si_matrix|methodology_file|knowledge_unit|task_inbox|no_op|unknown"
  target_reason: ""
  task_vs_knowledge: "task|knowledge_update|both|neither"
  no_op_reason: ""
```

Do not create a new ingest log by default. Prefer existing project Storyline-Storyboard, project journal, `Матрица BPM — SI`, methodology files, or `ПКМ/картотека-лог.md` only when the signal changes rules or methodology.

For active BPA / All Delivery projects with a deliverable or slide/storyline trajectory, update `Анализ/BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md` when it exists. If the file does not exist but the project already has BPM-scope plus a significant BPM-candidate source, create it when an active rule requires that exact artifact or record the explicit no-op reason if creation is not allowed. If there is no physical project Storyline-Storyboard target yet, write the no-op / routing reason into the nearest existing project artifact and open a task to resolve the gap.

For market/category/competitor/channel research, assume at least `BPM-6`, `BPM-7A`, and `BPM-7B` relevance until checked. If the research also touches client data, CRM, source of deals, SKU, margin, integrations, product modules, roles, quality, or implementation, check secondary increments for `BPM-3`, `BPM-4`, `BPM-8`, `BPM-9`, `BPM-10`, and `BPM-11`.

#### BPM Exchange Governance

For 4th-department real-client return packets, run the full BPM exchange logic, but protect the system from prompt bloat, false-positive routing, duplicate work, and silent contradictions.

Every material signal should carry:

```yaml
bpm_exchange_governance:
  relevance_score: 0.0
  relevance_reason: ""
  route_class: "required_check|optional_enrichment|watch|no_op"
  preflight_summary: "" # 200 tokens max
  conflict_resolution:
    conflict_detected: true|false
    conflicting_signal_or_source: ""
    contradiction_type: "hard|soft|no_op|unknown"
    resolution_strategy: "human_arbitration|evidence_weight|archetype_precedent|park"
    resolution_status: "pending|resolved|parked|not_needed"
  signal_lifecycle:
    created_date: ""
    last_validated_date: ""
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

Routing rules:

- `required_check`: the target BPM can change the answer, block client-facing use, validate a weak claim, or is explicitly required by a human / project gate.
- `optional_enrichment`: the target BPM can enrich language, add proof, or improve prioritization, but the current output can proceed as a hypothesis without it.
- `watch`: keep the signal visible, but do not create tasks or rewrite storyline.
- `no_op`: record why no route is needed.

Use calibrated top-K filtering. Do not inject all available signals into a skill prompt. Prefer the smallest set that is enough for the query class and summarize each selected signal in `preflight_summary`, with raw sources available only if needed. If the corpus has no measured retrieval calibration yet, state that the K choice is heuristic. If a derivative has low relevance or weak evidence, do not create a human task unless it affects a client-facing claim, a commercial decision, or a writeback gate.

Conflicts are not failures. If BPM-2 confirms a problem and BPM-5 or BPM-4 contradicts its economic importance, mark a conflict and route to human arbitration or evidence weighting instead of silently choosing one side.

Signal lifecycle is project-relative. Even when a project lasts about 3 months, weak public evidence, competitor status, CRM snippets, and archive analogs can become stale inside the project. Default TTL is 90 days for project signals; shorter TTL may be used for market/competitor facts, and `ttl_override: true` may mark timeless methodology.

#### Client Reality Reconciliation Gate / BPM-2

When an external return packet concerns a real client project, the external answer is a public evidence map, not the client's lived market map, until reconciled through BPM-2 / BPM-3 voice evidence and internal commercial data.

This gate is downstream of `BPM-2` by default: any real-client market, category, competitor, channel, buyer-role, pricing, procurement, service, implementation, or business-model claim must generate BPM-2 client / owner / expert questions before becoming client-ready. If the voice evidence is from dealers, partners, integrators, employees, or implementation teams, route the same check through BPM-3 as well.

The local return packet must include:

```yaml
client_reality_reconciliation_gate:
  required: true
  source_relation: "external_research -> BPM-2/BPM-3 reconciliation"
  external_visibility_claims: []
  client_reality_questions: []
  likely_misread_or_misnamed_entities: []
  historical_vs_current_status: []
  business_model_factors_to_check:
    - "pricing"
    - "VAT/tax structure"
    - "procurement volume"
    - "service burden"
    - "margin"
    - "implementation effort"
  reconciliation_output_template:
    confirmed_by_client: []
    corrected_by_client: []
    contradicted_by_client: []
    added_by_client: []
    downgraded_after_client_input: []
    needs_CRM_win_loss_source_check: []
```

External prompts for real client projects must explicitly require this statement:

`This is a public evidence map, not the client's lived market map, until reconciled with internal/client evidence.`

If future client, owner, dealer, partner, expert, or support interviews are planned, require the external machine to generate an interview guide designed to falsify or correct the external findings, not only confirm them.

#### Field Pressure Reconciliation

After client reality evidence appears, reconcile public research against field pressure before ranking competitors, market players, partners, or substitutes.

For each meaningful player, separate:

```yaml
field_pressure_reconciliation:
  player: ""
  public_visibility: "strong|medium|weak|unknown"
  client_reported_pressure: "strong|medium|weak|none|unknown"
  historical_pressure: "active_now|used_to_matter|legacy_installed_base|obsolete|unknown"
  latent_threat: "high|medium|low|unknown"
  benchmark_only: true|false
  channel_or_partner: true|false
  evidence_sources:
    public: []
    client_or_sales_voice: []
    CRM_or_win_loss: []
    partner_or_channel: []
  ranking_implication: ""
  action: "prioritize|monitor|interview_more|CRM_check|benchmark_only|downgrade|exclude"
```

Never rank competitors only by public visibility when the project has access to client-side interviews, ROP/sales voice, CRM, win/loss, dealer, partner, or support evidence. A highly visible public player may be only a benchmark or latent threat; a weakly visible player may be a high-pressure deal competitor if the client-side evidence says so.

#### Client Correction Packet

When a client, owner, expert, dealer, partner, sales, support, or implementation call is available after external research, produce a `client_correction_packet`. This packet turns BPM-2/BPM-3 reconciliation into specific changes for BPM-4, BPM-5, BPM-6, BPM-9, BPM-10, BPM-11, BPM-SI, and Storyline-Storyboard.

Required table:

| external finding | client correction | effect on priority | evidence needed | action |
|---|---|---|---|---|

Allowed correction categories:

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

Route effects explicitly:

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
    BPM-4: "what data/dashboard/CRM fields must verify"
    BPM-5: "what proposals/win-loss/commercial traces must verify"
    BPM-9: "what implementation rhythm or operating decision changes"
    BPM-10: "what CRM/lead-source/pipeline/ownership fields must change or be checked"
    BPM-11: "what entities/statuses require data model changes"
  storyline_delta:
    appeared: []
    strengthened: []
    weakened: []
```

Do not treat a correction packet as durable canon by itself. It is a routed update proposal until the relevant BPM/data/storyline targets are accepted or no-op reasons are recorded.

#### Naming Normalization / Transcript Safety

When competitor, partner, vendor, product, platform, standard, or buyer names come from transcripts, voice notes, client calls, OCR, auto-summary, or informal speech, do not create new competitor or market entities immediately.

Return a normalization table and keep the entity as `normalized_candidate` until confirmed:

| raw_name | likely_normalized_name | confidence | why | needs_confirmation_from |
|---|---|---|---|---|

Risk patterns:

- phonetic transcription;
- Cyrillic/Latin variants;
- brand vs product vs platform name;
- local nickname;
- former company name;
- distributor name confused with vendor;
- competitor merged with technology standard.

Only after confirmation may the entity move from `normalized_candidate` to `confirmed_competitor`, `confirmed_partner`, `confirmed_vendor`, or another project-specific confirmed status.

The user-facing final answer after a project Storyline-Storyboard update must include the required delta:

- `появились`;
- `усилились`;
- `ослабли`.

If there is no meaningful delta in a group, say `нет существенной дельты`. Do not finish with only a prose summary or a file-change list.

### Mode E: Recurring Monitor

Use when Ilya explicitly wants the same research question monitored on a schedule, such as weekly, biweekly, monthly, or before a recurring meeting.

Do not silently switch a one-time research request into recurring monitoring. If Ilya says `регулярно`, `каждую неделю`, `мониторь`, `следи`, `подсасывай апдейты`, `раз в N дней`, or similar, stop and ask for transition approval unless the current message already clearly approves it.

Required transition gate:

```text
Похоже, это не разовый deepresearch, а recurring monitor.
Перевожу в режим `Recurring Monitor`?

Нужно подтвердить:
1. частота: weekly / biweekly / monthly / custom;
2. горизонт обновлений: за последнюю неделю / месяц / с прошлого запуска;
3. источники: web / academic / Notion connector / Readwise MCP / Drive connector / structured data / approved community entry paths;
4. update threshold: что считать значимым изменением;
5. output format: short update / decision packet / risk alert / table;
6. return route: в этот чат / в существующий Vault-файл / только draft в чат;
7. safety: что нельзя искать или цитировать наружу.
```

Recurring Monitor artifacts:

1. `Recurring Brief`
2. `Watchlist`
3. `Source Plan`
4. `Update Criteria`
5. `Run Log`
6. `Delta Synthesis`
7. `Update Packet`

If Ilya asks Codex itself to run the monitor on schedule, use the app automation system after confirmation. If the request is only for ChatGPT Pro / Perplexity, produce a prompt that tells the external tool how to perform the recurring check in its own environment, but do not claim Codex has scheduled it.

## Structured Brief

Every research or Pro-review prompt starts with a structured brief.

```text
RESEARCH BRIEF
──────────────────────────────────────────
ТЕМА: [one clear formulation]
КЛЮЧЕВЫЕ ВОПРОСЫ:
  1. ...
  2. ...
  3. ...
ГОРИЗОНТ: [time range for sources]
ГЛУБИНА: lean / full
РЕГУЛЯРНОСТЬ: one-time / recurring
КЛАССЫ ИСТОЧНИКОВ: [A/B/C/D/E/F, only relevant classes]
ВНУТРЕННИЕ ИСТОЧНИКИ: [Vault via Google Drive / uploaded files / Notion / Readwise / prior packets / none]
ВНЕШНИЕ ИСТОЧНИКИ: [web / academic / databases / public sources / community entry paths / none]
ОЖИДАЕМЫЙ ВЫХОД: [decision packet / research memo / review / table / prompt]
КОНТЕКСТ/ОГРАНИЧЕНИЯ: [business, Vault, safety, known constraints]
ЧУВСТВИТЕЛЬНЫЕ ДАННЫЕ: [что нельзя отправлять наружу или надо анонимизировать]
КЛИЕНТСКИЕ ОПЕРАЦИОННЫЕ ДАННЫЕ: [CRM / SKU / support / margin / win-loss / service desk / roadmap / КП / lost deals / none / unavailable]
ЧТО НЕЛЬЗЯ УТВЕРЖДАТЬ БЕЗ ЭТИХ ДАННЫХ: [claims to avoid or mark as weak]
──────────────────────────────────────────
```

If the brief is weak, rewrite it before producing the external prompt.

## Market Boundary / Derivative Market Guard

When researching a market, category, product, service model, or commercialization route, do not collapse the specific question into the broad parent market.

Most useful market research should separate:

1. `parent_market`: the broad market that explains scale, demand drivers, regulation, customer base, and category language;
2. `derivative_market`: the specific business model, service layer, rental/subscription/managed-service layer, implementation layer, maintenance layer, platform layer, or other narrower segment that the decision actually concerns.

Examples:

- product market vs service/rental market;
- software category vs implementation/managed-service market;
- equipment market vs maintenance/aftermarket market;
- broad industry spend vs specific procurement category;
- total addressable audience vs paying demand for a premium/outsourced/subscription model.

Rules:

- parent-market data can support context, scale, and demand drivers;
- parent-market data cannot prove penetration, adoption, economics, margins, or competitive position in the derivative market;
- derivative-market evidence is required for claims about specific business-model traction, willingness to pay, contract economics, usage, penetration, adoption, and supplier ranking;
- if derivative-market evidence is missing, mark the relevant claims as `needs_derivative_market_evidence`;
- if both parent and derivative evidence exist, show how they relate instead of choosing only one.

Required output when relevant:

```yaml
market_boundary_check:
  parent_market:
    definition: ""
    what_it_can_support: []
    evidence_used: []
  derivative_market:
    definition: ""
    what_it_must_prove: []
    evidence_used: []
    evidence_gap: []
  invalid_shortcuts:
    - shortcut: "parent market data used as derivative-market proof"
      affected_claim: ""
      required_fix: ""
```

## Market Data Freshness Rule

For market size, growth, share, penetration, adoption, pricing, margin, competitive position, and customer-readiness claims, treat recency as part of evidence quality.

Default rule for current market decisions:

- prefer sources from the last 2-3 years;
- if several sources use the same or comparable data for the same geography, industry, sub-industry, and definition, prefer the newest source;
- older sources may be used for historical trend, baseline, CAGR context, market evolution, or to show how the category changed, but not as the best current estimate when a newer comparable source exists;
- if the source is older than 3 years and the market is dynamic, mark it as `aging` or `stale_for_current_claim`;
- if a timeless methodological source is used, mark it as methodology, not current market evidence.

Required output when relevant:

```yaml
market_data_freshness:
  current_estimates_used:
    - claim: ""
      source: ""
      year: ""
      geography: ""
      industry_scope: ""
      why_current_best_available: ""
  older_sources_used_as_context:
    - source: ""
      year: ""
      used_for: "trend|baseline|CAGR_context|category_history|methodology"
      not_used_for: ""
  stale_or_weak_sources:
    - source: ""
      year: ""
      affected_claim: ""
      downgrade: ""
```

## Research Brief / Folded Research Logic

The former standalone research skill is folded into `deepresearch`. Do not call it as a separate skill. Use this section when the task is research on a company, market, category, competitor, methodology, client context, or strategic hypothesis.

Research starts Vault/Drive-first when external ChatGPT Pro / Perplexity can access Ilya's Google Drive or uploaded Vault files. The external prompt should explicitly say:

- search the provided Vault / Google Drive / file context narrowly first;
- treat Vault/Drive facts as internal evidence, not public truth;
- then identify external evidence gaps;
- then use web/academic/structured sources only where they change confidence, decision, risk, or next action;
- keep internal and external sources separated in the output.

Recommended research modes:

| Mode | Trigger | Output |
|---|---|---|
| `company-research` | company, client, competitor, partner | company brief, signals, risks, open questions |
| `market-research` | market, segment, category, industry | market map, drivers, players, uncertainty map |
| `benchmark-scan` | analogs, practices, frameworks | benchmark table, copy / do-not-copy, applicability |
| `diligence-lite` | check a claim, opportunity, or risk | evidence memo, red flags, recommendation |
| `research-for-content` | article, longread, case, matrix | source pack, angles, disputed claims |
| `research-for-proposal` | КП or client decision support | client context, market pain, proof points, objections |

## Client-Side Data Gap Standard

When research tries to choose a segment, ICP, route-to-market, platform value, margin logic, win/loss explanation, or strategic priority, external public sources are usually not enough.

The prompt should force the external researcher to state which client-side data would be needed for a stronger answer and what cannot be claimed without it.

Important boundary:

- do not block early market / category / competitor research just because BPM-4, CRM, SKU, margin, support, or win/loss data does not exist yet;
- early `market-research`, `company-research`, `benchmark-scan`, and competitor/context ingestion may run before BPM-4;
- in that early stage, the goal is market context, segment hypotheses, competitor landscape, buyer-role hypotheses, source map, risks, and data-request design;
- BPM-4 / CRM / SKU / support / margin / win-loss data is the next validation layer for economics, ICP precision, route prioritization, service burden, and revenue/margin decisions;
- therefore the output should distinguish `market_context_ready`, `hypothesis_ready`, `needs_bpm4_validation`, and `not_ready_for_durable_economic_claim`.

Common high-value client-side data:

- anonymized CRM rows: segment, source, stage, deal size, win/loss, cycle length, buyer, geography;
- SKU / product group data: revenue, margin, attach rate, returns, service burden, stock/availability;
- support / service desk data: incidents, repair, complaints, onboarding friction, SLA, implementation load;
- win/loss and lost-deal notes: reasons, competitors, objections, price pressure, buying criteria;
- proposal / КП archive: promised value, scope, price logic, objections, proof used;
- product roadmap / PLM / firmware / integration data where product capability matters;
- interviews with current customers, lost customers, competitor customers, partners, integrators, field sales, support, and implementation teams.

If these data are missing, the external answer must not pretend precision. It must:

- still produce the market/context packet if the task is early-stage market ingestion;
- label segment attractiveness, ICP, TAM/SAM/SOM, margin, win-rate, service burden, adoption, implementation quality, and buyer-readiness claims as `hypothesis`, `weak`, `inference`, `needs_bpm4_validation`, or `needs_client_data`;
- separate `strategic zone` from precise ICP;
- produce a `Data Request Checklist`;
- produce `Interview Scripts` or interview question blocks when qualitative confirmation is needed;
- list the weakest claims and what data would strengthen or kill them;
- name what is not ready for client-facing, public, or durable Vault use.

Useful repeatable artifact for such cases:

```yaml
client_side_data_request:
  crm_fields_needed: []
  sku_or_product_fields_needed: []
  support_or_service_fields_needed: []
  win_loss_fields_needed: []
  proposal_or_lost_deal_files_needed: []
  roadmap_or_product_data_needed: []
  interviews_needed:
    - audience: "current_customer|lost_customer|competitor_customer|integrator|partner|sales|support|implementation|product"
      questions: []
      why_needed: ""
  claims_blocked_without_data: []
```

When a visual is requested, prefer a decision-useful matrix such as:

- `segment attractiveness x accessibility`;
- bubble size by revenue, margin, win-rate, or service burden when client data exists;
- confidence overlay when the data is missing or mixed.

## Procurement / Tender Evidence Layer

Use this layer when the market is B2B, B2G, enterprise, industrial, regulated, procurement-heavy, service-contract-heavy, or where tenders/RFPs/specifications can reveal real buyer language.

Tender evidence is not required for every research run. It is required or strongly recommended when:

- public market reports are too generic;
- the specific derivative market is weakly covered by public analysis;
- service / rental / outsourcing / maintenance / implementation contracts are the real object of research;
- buyer criteria, contract scope, pricing structure, geography, supplier names, or procurement volume matter;
- claims about demand, competition, or regional suppliers would otherwise rely only on inference.

Source families may include:

- official public procurement portals;
- corporate procurement portals;
- tender aggregators;
- RFP / RFQ / specification archives;
- public contract registries;
- industry-specific procurement databases;
- commercial-offer packs supplied by Ilya or client-approved sources.

For Russian research, consider whether 44-ФЗ, 223-ФЗ, ЕИС / zakupki.gov.ru, B2B-Center, СберА, Фабрикант, RosTender-like aggregators, or sectoral procurement portals are relevant. Do not include them mechanically if the market does not buy through tenders.

Required output when tender evidence matters:

```yaml
tender_research_plan:
  relevance: "required|recommended|optional|not_relevant"
  why:
  portals_or_databases: []
  query_terms: []
  classification_codes:
    okpd_or_local_codes: []
    cpv_or_international_codes: []
    other_codes: []
  include_terms: []
  exclude_terms: []
  period: "last_2_3_years_preferred"
  geography:
  fields_to_extract:
    - buyer
    - supplier
    - contract_subject
    - contract_value
    - date
    - region
    - scope
    - required_service_level
    - selection_criteria
    - incumbent_or_winner
  relevance_rule:
  known_limits:
  what_this_can_prove:
  what_this_cannot_prove:
```

Tender evidence limits:

- tenders can show public/procurement demand, buyer language, contract structure, and visible suppliers;
- tenders do not automatically prove total market size, margin, win-rate, service quality, private-market demand, or actual implementation success;
- tender samples must be checked for duplicates, framework contracts, cancellations, lots with mixed scope, and generic wording.

## Visibility Bias / Hidden Player Guard

Do not equate public visibility with market pressure.

This matters especially for:

- regional suppliers;
- white-label / OEM / private-label players;
- integrators and service contractors;
- incumbent vendors with weak websites but strong procurement presence;
- implementation partners;
- local distributors;
- aftersales/service companies;
- small B2B players that win through relationships, geography, or price rather than content visibility.

Required output when ranking players, channels, or suppliers:

```yaml
visibility_bias_check:
  public_visibility_risk: "low|medium|high|unknown"
  likely_hidden_players:
    - player_type: ""
      why_may_be_hidden: ""
      how_to_find: "tenders|CRM|win_loss|interviews|regional_search|dealer_partner_search|service_records|field_sales"
  claims_to_downgrade:
    - claim: ""
      reason: "public visibility is not enough"
      required_evidence: []
```

## Digital Readiness / Advanced-Tech Claim Guard

Claims about digital readiness, AI readiness, predictive analytics, EHS/ERP/CRM/BI integration, platform adoption, automation maturity, or data-driven operating maturity must be treated as inference unless backed by direct evidence.

Direct evidence may include:

- customer interviews;
- implementation case studies;
- CRM / support / integration data;
- product usage data;
- tender requirements for digital functionality;
- public implementation references;
- field sales / support / implementation evidence;
- credible sector surveys with matching geography and segment.

If evidence is indirect, label the claim as:

- `digital_readiness_inference`;
- `needs_interview_validation`;
- `needs_usage_or_implementation_evidence`;
- `not_client_facing_as_fact`.

## Service / Recurring-Model Economics Gate

Use this gate when the opportunity concerns service, rental, subscription, managed service, maintenance, outsourcing, implementation, platform-enabled service, or other recurring / operational models.

Do not infer attractiveness from product-market size alone. Check operating economics and delivery burden.

Required output when relevant:

```yaml
service_economics_gate:
  model_type: "service|rental|subscription|managed_service|maintenance|outsourcing|implementation|platform_enabled_service|other"
  revenue_logic:
  cost_drivers:
    - labor
    - logistics
    - inventory_or_asset_base
    - onboarding
    - support
    - SLA
    - repairs_or_replacements
    - churn_or_renewal
    - financing_or_working_capital
    - compliance
  margin_unknowns: []
  operational_burden_unknowns: []
  contract_economics_evidence: []
  claims_not_allowed_without_economics: []
  next_data_needed:
    - CRM_contracts
    - PnL_by_contract_type
    - service_logs
    - support_or_incident_data
    - renewal_churn_data
    - tender_awards_and_values
    - interviews_with_buyers_or_operators
```

If economics data is missing, the output may still describe market context, but must not present margin attractiveness, scalable profitability, or segment priority as proven.

Minimum output:

```yaml
research_packet:
  research_question: ""
  decision_context: ""
  mode: "company-research|market-research|benchmark-scan|diligence-lite|research-for-content|research-for-proposal"
  answer_short: ""
  confidence: "low|medium|high"
  internal_sources_used:
    - source: ""
      type: "Vault|Google Drive|Notion|Readwise|uploaded file|prior decision packet"
      what_it_supports: ""
  external_sources_used:
    - source: ""
      type: "web|academic|database|public media|community approved path|other"
      what_it_supports: ""
  key_findings:
    - finding: ""
      evidence_grade: "A|B|C|D|X"
      source_family: "internal|external|mixed|inference"
      implication: ""
  contradictions: []
  open_questions: []
  client_side_data_request:
    crm_fields_needed: []
    sku_or_product_fields_needed: []
    support_or_service_fields_needed: []
    win_loss_fields_needed: []
    proposal_or_lost_deal_files_needed: []
    roadmap_or_product_data_needed: []
    interviews_needed: []
    claims_blocked_without_data: []
  market_context_status: "market_context_ready|hypothesis_ready|needs_bpm4_validation|not_ready_for_durable_economic_claim"
  not_ready_for_client_public_or_durable_use: []
  useful_next_visuals_or_matrices: []
  risks: []
  market_boundary_check:
    parent_market:
    derivative_market:
    invalid_shortcuts: []
  market_data_freshness:
    current_estimates_used: []
    older_sources_used_as_context: []
    stale_or_weak_sources: []
  tender_research_plan:
    relevance:
    portals_or_databases: []
    query_terms: []
    classification_codes: []
  visibility_bias_check:
    public_visibility_risk:
    likely_hidden_players: []
  service_economics_gate:
    model_type:
    margin_unknowns: []
    operational_burden_unknowns: []
  recommended_next_action: ""
  vault_candidates: []
  do_not_write_without_approval: true
```

Evidence grades:

- `A`: primary/internal accepted source or strong primary external source;
- `B`: strong external source or several independent confirmations;
- `C`: plausible expert inference from partial evidence;
- `D`: unsupported or weakly supported;
- `X`: contradicted by available evidence.

## Client-Facing Claim Exclusion Standard

For client-facing, public, proposal, deck, or durable Vault use, do not present the following as facts unless the source, year, geography, scope, and methodology are explicit and current enough:

- market size;
- market growth;
- market share;
- player ranking / "leader" claims;
- penetration or adoption of a specific business model;
- margins or profitability;
- win-rate / buyer preference;
- digital readiness;
- service-model economics;
- regional competitive strength;
- implementation success.

If a newer source covers the same geography, industry, sub-industry, and metric with a comparable or better definition, prefer the newer source. Use older numbers as historical context, trend baseline, or CAGR context, not as the main current claim.

Each sensitive claim should be placed in one of:

- `client_facing_safe`;
- `internal_hypothesis`;
- `source_check_needed`;
- `needs_bpm4_validation`;
- `do_not_use`.

## Research Claim Ledger

Do not create a separate `research-claim-ledger` skill. Integrate claim tracking into every serious `deepresearch` run.

```yaml
claim_ledger:
  - claim: ""
    source_family: "internal|external|mixed|inference"
    sources:
      - ""
    evidence_grade: "A|B|C|D|X"
    confidence: "low|medium|high"
    contradiction: ""
    source_year: ""
    geography_scope: ""
    market_scope: "parent_market|derivative_market|unclear"
    freshness_status: "fresh|acceptable|aging|stale|timeless_methodology|unknown"
    client_facing_usability: "client_facing_safe|internal_hypothesis|source_check_needed|needs_bpm4_validation|do_not_use"
    implication: ""
    can_enter_vault: "yes|candidate|no"
```

Rules:

- no claim without source family;
- no external source becomes canon by itself;
- internal Vault/Drive evidence and external evidence must be visibly separated;
- inference must be named as inference;
- parent-market evidence must not be used as proof for derivative-market claims;
- freshness must be checked for current market claims;
- contradictions must survive into the Decision Packet.

## Source Classes

Use only relevant classes. Do not include a source class just because it exists.

### Class A: Live web and media

Use for current market, company, news, events, public discussion, trends.

Useful methods:

- Perplexity / ChatGPT web search;
- Readwise / Reader MCP as the primary personal RSS, newsletter, saved-article, highlight, and Reader-document source;
- RSSHub / RSS-Bridge only as a fallback for public sites without clean feeds, ideally landing the resulting feed into Readwise Reader;
- FreshRSS / Miniflux only if a monitor needs a separate feed store outside Readwise;
- GDELT: `https://api.gdeltproject.org/api/v2/doc/doc?query=TOPIC&mode=artlist&maxrecords=25&format=json`;
- Hacker News for tech through Firebase and Algolia APIs:
  - `https://hacker-news.firebaseio.com/v0/newstories.json`
  - `https://hacker-news.firebaseio.com/v0/item/ITEM_ID.json`
  - `https://hn.algolia.com/api/v1/search?query=TOPIC&hitsPerPage=20`;
- Internet Archive for history: `https://web.archive.org/web/*/URL`.

### Class B: Academic and research bases

Use for scientific, technical, medical, social-science, management, or methodology questions.

Useful methods:

- OpenAlex: `https://api.openalex.org/works?search=TOPIC&per_page=10&sort=cited_by_count:desc`;
- arXiv: `https://export.arxiv.org/api/query?search_query=all:TOPIC&max_results=10`;
- Semantic Scholar: `https://api.semanticscholar.org/graph/v1/paper/search?query=TOPIC&limit=10&fields=title,year,citationCount,abstract`;
- PubMed when medical/biological relevance exists;
- SSRN via web search for economics, law, social science.

### Class C: Community signal

Current status: entry-path discovery only.

Allowed now:

- Reddit via Perplexity / web search, or narrow URL patterns;
- Stack Exchange / Stack Overflow for technical questions;
- public forums, communities, and official pages that the external model can access normally;
- newsletters, RSS feeds, public archives, and manually supplied source packs;
- Notion / Readwise / Drive connector materials when they contain already-saved community signals.
- public Telegram-channel previews only through an approved entry path, such as an existing local `public_telegram_scraper.py`, public preview pages, public archives, rtgstat-like analytics pages, or a manually supplied source pack.

Do not assume any platform-specific extractor. Do not propose account automation, private collection, member collection, bypassing access controls, or bulk copying of closed community content.

For Telegram-like sources:

- first check whether an approved adapter/source path exists;
- prefer public preview, public analytics pages, public archives, or manual packs;
- keep excerpts short and source-linked;
- do not collect members, private messages, closed groups, or personal data;
- do not send messages, join communities, bypass access controls, or automate account behavior.

If community signal matters, first produce a Community Entry Path Plan:

```text
COMMUNITY ENTRY PATH PLAN
source_family: [community / forum / social / newsletter / public archive / connector]
candidate_sources: [...]
entry_path: [public web search / official page / RSS / export / connector / manual source pack / API]
permission_status: [public / connector-authorized / user-supplied / unknown / not-allowed]
scope: [topic, date window, geography, language, communities]
query_terms: [...]
expected_artifact: [source table / excerpts / summaries / links / no-op]
safety_notes: [what not to collect, quote, store, or send externally]
decision: [use now / ask Ilya / exclude from this run]
```

If no approved entry path exists, mark Class C as `excluded: no approved entry path` and continue with web, academic, connector, and structured-data sources.

### Class D: Structured facts

Use for encyclopedic, statistical, and structured data checks.

Useful sources:

- Wikipedia summary;
- Wikidata;
- Our World in Data;
- World Bank Open Data;
- DBpedia where semantic data matters.

### Class E: Domain/local databases

Use only when relevant:

- Rosstat / EMISS for Russian official statistics;
- Kaggle / HuggingFace datasets;
- Scopus / WoS / CrunchBase / PitchBook if the external tool has access.

### Class F: Monitoring infrastructure

Use only when the task is recurring monitoring or monitor design, not for ordinary one-off research.

Allowed components:

- official Readwise MCP for Reader documents, RSS/newsletter intake, highlights, saved articles, and research-memory search;
- Huginn / n8n for orchestration, schedules, rules, alerts, and digest delivery only if Readwise cannot cover the workflow;
- RSSHub / RSS-Bridge for public feed generation only when a source cannot be added cleanly to Reader;
- FreshRSS / Miniflux for separate feed storage only when Readwise is insufficient;
- small custom adapters for sources with stable public APIs;
- normalized event store for deduplication, scoring, and replay.

Do not add a component because it is fashionable. Add it only when it owns one clear job in the pipeline.

## Source Plan

Before external research, generate a source plan.

```text
SOURCE PLAN
──────────────────────────────────────────
INTERNAL FIRST:             [ ] Vault via Google Drive  [ ] uploaded Vault files  [ ] Notion  [ ] Readwise/Reader  [ ] prior decision packets
CLASS A (web/media):       [ ] web search  [ ] Readwise/Reader RSS  [ ] RSSHub/RSS-Bridge fallback  [ ] GDELT  [ ] HN Firebase/Algolia  [ ] Archive
CLASS B (academic):        [ ] OpenAlex  [ ] arXiv  [ ] Semantic Scholar  [ ] PubMed
CLASS C (community):       [ ] Reddit/web  [ ] Stack Exchange  [ ] forums  [ ] newsletters/RSS  [ ] Telegram public preview via approved path  [ ] other approved entry path
CLASS D (facts/data):      [ ] Wikipedia  [ ] Wikidata  [ ] OWID  [ ] World Bank
CLASS E (domain/local):    [ ] Rosstat  [ ] EMISS  [ ] Kaggle  [ ] HF  [ ] other
PROCUREMENT / TENDERS:     [ ] public procurement portals  [ ] corporate procurement portals  [ ] tender aggregators  [ ] contract registries  [ ] RFP/specification archives
CLASS F (monitoring infra): [ ] Readwise MCP  [ ] Reader tags/saved searches  [ ] Huginn/n8n if needed  [ ] FreshRSS/Miniflux fallback  [ ] normalized event store  [ ] alerts/digest
CONNECTORS:                [ ] Notion  [ ] Readwise/Reader MCP  [ ] Google Drive  [ ] OneDrive  [ ] none
RATIONALE: [why these classes are relevant]
EXCLUSIONS: [what not to search and why]
SAFETY: [what must be anonymized or summarized]
SOURCE SEPARATION: [how internal / external / inference will be separated]
MARKET BOUNDARY: [parent market vs derivative/specific market; what each source can and cannot prove]
FRESHNESS RULE: [prefer last 2-3 years for current market claims; older sources only for trend/baseline/CAGR/methodology unless no newer comparable data exists]
MVP STACK DECISION: [connect now / conditional / quarantine / exclude]
──────────────────────────────────────────
```

## Recurring Monitor Prompt

When producing an external recurring-monitor prompt, include this block.

```text
Recurring Monitor:

Cadence:
- Run this research update [weekly / biweekly / monthly / custom] if your environment supports scheduled or recurring tasks.
- If your environment cannot schedule tasks automatically, treat this as a reusable monitoring prompt and say what I need to do to rerun it.

Update horizon:
- Compare new evidence since [last run date / last 7 days / last month].
- Do not repeat old background unless it changes the interpretation.

Watchlist:
- [companies / topics / competitors / terms / sources / questions]

Sources:
- Use the selected source classes from the Source Plan.
- If you have Notion / Readwise / Drive connectors, search narrowly for recent pages, saved documents, highlights, or updates relevant to the watchlist.
- Use community sources only through approved entry paths; if none exist, list the missing entry paths instead of collecting community data.
- For recurring monitors, prefer Readwise Reader RSS/newsletter intake + Readwise MCP before any separate RSS store or custom source collection.

Significance threshold:
- Report only updates that change the decision, risk, opportunity, timing, evidence confidence, or next action.
- Separate major changes, minor signals, and noise.

Output:
1. What changed since the previous run.
2. New evidence by source class.
3. What this changes in the decision / risk / opportunity.
4. What remains unchanged.
5. Recommended next action.
6. Whether this should return to Codex/Vault as a decision packet, task candidate, or no-op.
```

If asked to design the recurring pipeline itself, add:

```text
Monitoring implementation:
1. Recommended MVP stack and why.
2. Source adapters to connect now.
3. Conditional adapters that need approval/checks.
4. Excluded/quarantined adapters and why.
5. Normalized event schema.
6. Topic rules and scoring.
7. Digest/alert format.
8. Operational risks: ToS, account risk, secrets, rate limits, maintenance burden.
```

## Vault Context Packaging

Use Vault context carefully. Include enough for reasoning, not everything nearby.

Preferred context order:

1. current user decision / question;
2. structured brief;
3. operating context for the external model;
4. optional external connector instructions, such as Notion or Readwise, when useful;
5. relevant artifact excerpt or summary;
6. known constraints, rules, accepted decisions;
7. source plan;
8. open questions and risks;
9. requested output format.

For Vault files:

- use summaries or excerpts by default;
- include exact file names only if they help orientation;
- do not include secrets, credentials, private raw logs, full contracts, financial primary documents, or large raw transcripts without explicit approval;
- separate confirmed facts from assumptions.

## External Connector Context

ChatGPT Pro or Perplexity may have connectors that Codex does not use inside the current local session. The most useful cases are Notion, Readwise/Reader, and Drive.

When the task would benefit from context that may live in Notion, include an explicit connector instruction in the external prompt. Do this especially for:

- client/project context that may have meeting notes, CRM-like pages, briefs, or status updates in Notion;
- product, content, or commercial materials that may have drafts, decisions, or references in Notion;
- questions where Vault context is known to be incomplete or stale;
- external review of a plan where Notion may contain accepted decisions, owner/status data, or recent meeting records.

Do not tell the external model to search Notion broadly. Give it a narrow target:

- what to search for;
- which entities, project names, clients, topics, or dates matter;
- what kinds of Notion pages are useful;
- what to ignore;
- how to report what it found.

Default Notion connector instruction:

```text
If you have access to my Notion connector, use it only as an additional context source. Search narrowly for pages related to: [project/client/topic/date/entities].

Look specifically for:
- accepted decisions;
- meeting notes or protocols;
- project/client context;
- owners, deadlines, statuses;
- product, content, commercial, or research drafts;
- facts that change the answer.

Do not treat Notion as automatically canonical. Distinguish:
- Notion facts you found;
- Vault/context facts provided in this prompt;
- your own inference;
- unresolved contradictions.

Do not expose or quote sensitive Notion content unnecessarily. Summarize when possible. If you find sensitive client/economic/personal data, report that such context exists and explain what kind of decision it affects, without reproducing the sensitive details unless explicitly needed.

In your answer, include a short `Notion connector findings` block:
- searched_for;
- useful_pages_or_context_found;
- what changed in your recommendation;
- remaining gaps;
- whether the recommendation depends on Notion evidence.
```

If the task is about skills architecture only, Notion is optional. Tell the external model to use Notion only if it can find existing skill/process docs, project methodology, content production notes, or accepted decisions that materially change the recommendation.

### Readwise / Reader Connector

Readwise has an official MCP server for Readwise highlights and Reader documents. If Ilya has connected it in the external tool or in Codex, it can be used as an additional research-memory layer.

Use Readwise / Reader when the task may benefit from:

- saved articles, PDFs, newsletters, or documents Ilya has already collected;
- highlights and notes from books/articles;
- prior reading on a market, company, concept, methodology, product, or technology;
- source discovery before web research;
- source acquisition recommendations from ChatGPT Pro / Perplexity;
- recurring monitoring of saved documents or newly highlighted material.

Do not use Readwise broadly. Give it a narrow target:

- topic / entity / project / client / concept;
- relevant tags if known;
- date or recency window if relevant;
- whether to search Reader documents, Readwise highlights, or both;
- what to ignore.

Default Readwise connector instruction:

```text
If you have access to my Readwise / Reader connector or Readwise MCP, use it only as an additional context source.

Search narrowly for:
- Reader documents and Readwise highlights related to: [topic/entities/tags/date window];
- saved articles, PDFs, newsletters, books, or notes that materially affect the research question;
- prior highlights that contain frameworks, evidence, examples, objections, or source leads.

Do not treat Readwise as canonical. Distinguish:
- Readwise / Reader evidence you found;
- Vault or prompt context;
- external web/academic evidence;
- your own inference.

Do not quote long copyrighted passages. Summarize highlights and cite document titles/authors/URLs when available.

In your answer, include a short `Readwise connector findings` block:
- searched_for;
- useful_documents_or_highlights_found;
- strongest signals;
- what changed in your recommendation;
- remaining gaps;
- whether the recommendation depends on Readwise evidence.

If the task includes finding new sources, include a separate `Reader Source Acquisition Packet` with RSS/import URLs, books, services/databases, route decisions, priorities, and why each source should enter Reader. Do not add anything to Reader yourself.
```

If Readwise MCP is not connected, do not block the research. State that Readwise was not available and continue with Vault context, web/academic sources, and other connectors.

## Mandatory External Context Block

External models do not know Ilya's Vault architecture. For prompts about skills, Vault, Codex process, departments, content rails, project rails, commercial artifacts, or task systems, include a compact `Operating Context` block before the material.

Do not wait for Pro / Perplexity to ask these questions. Answer them proactively when relevant.

Default context:

```text
Operating Context for External Model:

- `2-ка`, `4-ка`, `5-ка`, `8-ка` are internal Paper Planes / Vault department contours, not maturity levels.
- `2-ка` = sales/marketing/content/product-showcase contour: commercial proposals, cases, content rail, product vitrine, external packaging.
- `4-ка` = production / client delivery projects: project rails, штабы, project chats, BPM/BPP movement, owners, deadlines, delivery artifacts.
- `5-ка` = business-process quality and methodology: BPM/BPA/BPO/BPI/BPP, standards, readiness, fullkit, process methodology.
- `8-ка` = knowledge factory: reusable knowledge units, SECI/Nonaka logic, knowledge checks, knowledge reuse and fate of knowledge signals.
- Vault = local knowledge/project/document system. Codex can read existing files, summarize, update existing files, edit frontmatter/YAML carefully, create links, update registries, and create files only when Ilya explicitly asks or when an active rule requires a precise artifact.
- Codex Project Task Inbox = primary task-delta intake for new executable commitments. Knowledge belongs in Vault when it changes understanding, canon, methodology, product, content, case, project context, or evidence. A task belongs in the Inbox when there is an owner/contour, action, deadline or next step, expected output, and implementation reason. Legacy CORD Task OS may be used only as historical context or duplicate-check source, not as the primary home for new tasks.
- External ChatGPT Pro / Perplexity output is advisory. It must return to Codex/Vault as a decision packet: accepted / change / defer / reject / data gaps / risk gaps / writeback targets / next action.
- By default, only Ilya accepts durable writes to Vault, rule changes, task creation, canonicalization, and externalization. Other roles such as partner, PM, editor, or client may be stakeholders, but not assumed acceptors unless explicitly stated.
- Do not assume external tools can access Vault files. Treat all context below as the full context available to you, except when explicit connector instructions are given.
```

## External Model FAQ

For skill-system modernization prompts, include this FAQ unless it would make the prompt too long. If space is limited, include the answers most relevant to the prompt.

```text
External Model FAQ / Assumptions:

1. What are `2-ка`, `4-ка`, `5-ка`, `8-ка`?
They are internal Paper Planes / Vault department contours, not levels. `2-ка` is sales/marketing/content/product-showcase; `4-ка` is client delivery / production projects; `5-ка` is business-process quality and methodology; `8-ка` is the knowledge factory.

2. What can Codex do with Vault?
Codex can read files, search, summarize, update existing files, carefully edit frontmatter/YAML, add links, update registries, create tasks candidates, and create files only when Ilya explicitly asks or a live rule requires a precise artifact. Codex must report what changed.

3. Where is the boundary between Vault and Codex Project Task Inbox?
Vault stores knowledge, canon, project context, evidence, content, methodology, product/showcase logic, and reusable artifacts. Codex Project Task Inbox stores candidate executable commitments and task deltas: owner/contour, action, due date or next step, expected output, and implementation reason. Airtable sync happens downstream after accepted task candidates. Legacy CORD Task OS is not the primary home for new tasks.

4. What data should not be sent to external ChatGPT Pro / Perplexity?
Do not send secrets, credentials, tokens, private keys, `.env`, raw financial ledgers, full contracts, private logs, personal data, sensitive client primary evidence, or commercially sensitive terms unless Ilya explicitly approves.

5. What should `commercial-proposal-generator` produce?
It should produce a full Paper Planes proposal packet / Gamma-ready commercial proposal draft when asked, not just a skeleton. It should still mark assumptions, source gaps, pricing gaps, delivery-readiness gaps, and manual assembly needs.

6. Should research inside `deepresearch` be web-only?
No. Research should be Vault/Google-Drive-first and external-web-aware: first inspect internal context that is available through uploaded files, Google Drive / Vault, Notion, Readwise, or prior packets; then identify external evidence gaps; then use current external research where it matters; then return a decision packet / research memo / Vault candidates with internal and external sources separated.

7. What real artifacts can test modernized skills?
Good pressure-test artifacts: a commercial proposal / КП, an expert article or longread, a research memo, a project rail inspection, and a client brief.

8. Should skills have lifecycle statuses?
Yes. Preferred lifecycle: `experimental -> review -> active -> deprecated -> removed`. `review-critical` may be used for high-priority skills that remain usable but need deep redesign.

9. Should skills be compatible with Perplexity Skills format?
No strong requirement. These are local Codex skills first. External models may recommend portable patterns, but the primary standard should serve Codex/Vault routing, write-back, safety, and live-chat execution.

10. Who can approve durable writes or task creation?
By default, Ilya approves durable Vault writes, rule changes, canonicalization, task creation, and externalization. Other roles can be stakeholders or reviewers, but do not assume they are final acceptors unless stated.

11. What counts as writing to Vault?
Creating a new file, modifying an existing file, adding a durable block, changing frontmatter/YAML, updating a registry, creating links that change navigation, and changing status fields all count as Vault write operations. Chat-only suggestions and candidate lists are not writes.

12. What is the default file-creation policy?
Do not create new files unless Ilya explicitly asks for file output or an active rule requires that exact artifact. Prefer existing files and existing contours first.

13. What does external Pro output become when it returns?
It becomes advisory input, not canon. Codex should convert it into a decision packet: accepted / change / defer / reject / client questions / data gaps / risk gaps / writeback targets / next action.

14. What is the purpose of skills?
Skills are operational routing documents for live Codex work. They should tell Codex when to act, when not to act, what sources to read, what output to produce, when to ask for approval, and how to avoid adjacent-skill confusion.

15. Should external ChatGPT Pro / Perplexity use Notion connectors?
Sometimes. If the external model has a Notion connector, it may use Notion as an additional context source for meeting notes, accepted decisions, project/client context, statuses, drafts, and recent updates. It must search narrowly, summarize safely, distinguish Notion facts from Vault facts and inference, and not treat Notion as automatically canonical.

16. Should external ChatGPT Pro / Perplexity use Readwise / Reader?
Sometimes. If Readwise MCP or a Readwise/Reader connector is available, it may search Ilya's saved Reader documents and Readwise highlights as a personal research-memory layer. It should search narrowly by topic/tags/entities, summarize safely, avoid long copyrighted quotes, and distinguish Readwise evidence from Vault facts, web sources, and inference.

17. What should external models optimize for when reviewing the skill system?
Optimize for fewer wrong-mode activations, fewer premature Vault writes, clearer handoffs, stronger evidence discipline, better reusable outputs, faster execution, safer human-in-the-loop gates, and easier regression testing through eval scenarios.
```

## Cross-Synthesis

When multiple runs or source classes are used, include a cross-synthesis step.

```text
You are the Cross-Synthesizer. You have [N] independent research runs on: [TOPIC].

Tasks:
1. CONSENSUS: what do sources confirm together?
2. CONFLICTS: where do sources disagree, and why?
3. BLIND SPOTS: what important question remains uncovered?
4. SIGNAL QUALITY: which source/run produced the strongest and weakest signal?
5. WEIGHTED POSITION: final synthesis with source weights and uncertainty.

Output: structured markdown with the sections above.
```

## Decision Packet

Final output should be a decision packet, not a loose answer.

```markdown
# DECISION PACKET: [TOPIC]
**Date:** YYYY-MM-DD
**Mode:** Lean / Full Deep / Prompt Only / Return Packet
**Source classes:** A / B / C / D / E / F / connectors
**Internal sources:** Vault / Google Drive / Notion / Readwise / uploaded files
**External sources:** web / academic / databases / public media / approved community entry paths

## Key Findings
1. ...
2. ...
3. ...

## Source Consensus
...

## Conflicts and Uncertainty
...

## Blind Spots
...

## Claim Ledger
| Claim | Source family | Evidence grade | Confidence | Contradiction | Implication |
|---|---|---|---|---|---|
| ... | internal / external / mixed / inference | A/B/C/D/X | low/medium/high | ... | ... |

## Recommended Actions
- [ ] ...
- [ ] ...

## Reader Source Acquisition Packet
Include when the research reveals sources, books, RSS/newsletters, files, services, or databases that should be considered for Readwise Reader.

- sources_to_add:
- books_to_consider:
- services_or_databases_to_consider:
- do_not_add:
- priority_order:
- approval_needed_before_import: true

## Data Request Checklist
Include when the answer depends on missing client-side data.

- CRM fields needed:
- SKU / product group fields needed:
- support / service desk fields needed:
- margin / economics fields needed:
- win/loss or lost-deal notes needed:
- proposal / КП archive needed:
- roadmap / product / integration data needed:
- interviews needed:
- claims blocked until data is supplied:

## Interview Scripts
Include when interviews would materially improve ICP, segment attractiveness, buyer logic, implementation reality, or win/loss understanding.

- current customers:
- lost customers:
- competitor customers:
- partners / integrators:
- sales / account owners:
- support / implementation:
- product / roadmap owners:

## Sources by Class
**Internal / Vault / Drive:** ...
**Class A:** ...
**Class B:** ...
**Class C:** ...
**Class D:** ...
**Class E:** ...
**Class F:** ...
**Connectors:** ...

## Codex/Vault Return
- accepted:
- change:
- defer:
- reject:
- client_questions:
- data_gaps:
- risk_gaps:
- writeback_targets:
- next_action:

## Self-Reflection / Improvement Notes
Answer briefly in first person after the main packet. Use this as quality control for the current answer and as improvement input for the next prompt/run.

| Question | My answer |
|---|---|
| What was missing from my answer? |  |
| Where did I answer too generally? |  |
| Where did I rely too much on inference instead of evidence? |  |
| Which sources or source classes were underused? |  |
| Which connector contexts might have improved the answer? |  |
| Which claims are weakest or most uncertain? |  |
| What should not be used in client-facing or durable materials yet? |  |
| What contradictions or blind spots remain unresolved? |  |
| Which assumptions should be confirmed with Ilya or Codex? |  |
| What visual/table/structured artifact would make this more useful? |  |
| What would make this easier to route into Vault / CORD / Reader? |  |
| What would I change in the prompt before rerunning? |  |
| What are the 3 highest-leverage next improvements? |  |
```

## Prompt Standard

Every serious external prompt should include:

- Russian language instruction;
- role: strong external reviewer/researcher, not agreeable assistant;
- structured brief;
- operating context;
- connector instructions if useful;
- source plan if research is needed;
- material/context;
- what to check;
- what not to do;
- output format;
- quality criteria.
- client-side data gap standard when the question involves segment choice, ICP, economics, margin, win/loss, service burden, platform value, or route-to-market.
- market boundary check when the question may confuse a parent market with a derivative/specific market.
- freshness rule for current market figures: prefer last 2-3 years, and use older comparable data mainly as trend / baseline / CAGR context.
- procurement / tender plan when the market is B2B/B2G, procurement-heavy, service-contract-heavy, or weakly covered by public reports.

Default prompt skeleton:

Single-copy rule for prompt-only outputs:

- when giving Ilya a paste-ready prompt, make it one copyable block;
- do not split the prompt into separate code blocks for schemas, self-reflection, evidence grades, or appendices;
- if wrapping the whole prompt in a fenced block, use one outer `text` fence and do not use nested triple backticks inside it;
- include `Self-Reflection / Improvement Notes` inside the same requested output format, not as a separate copyable block after the main prompt;
- after the final prompt block, do not add additional prompt text that Ilya also needs to copy.

```text
Ответь строго на русском языке, кроме названий файлов, команд, моделей, API и неизбежных терминов.

Ты выступаешь как сильный внешний эксперт, исследователь и критик. Твоя задача — не соглашаться автоматически, а проверить решение, собрать релевантные источники, найти слабые места, расхождения и слепые зоны, а затем вернуть decision packet.

RESEARCH BRIEF:
[structured brief]

Operating Context:
[mandatory context block when the request concerns Vault/Codex/skills/departments/contours]

External connectors:
[optional narrow instruction for Notion / Readwise / Drive / Perplexity connector if it can provide useful context]

SOURCE PLAN:
[source classes and rationale]

Материал / вводные:
[summary, excerpt, file context, assumptions]

Проверь:
1. [main question]
2. [risks and weak points]
3. [alternatives]
4. [blind spots]
5. [missing data]
6. Если вопрос касается сегментов, ICP, экономики, маржи, win/loss, сервиса, SKU, платформенной ценности или маршрутов продаж, отдельно проверь, какие client-side данные нужны для честного вывода.
7. Если вопрос касается рынка, отдели родительский рынок от конкретного деривативного рынка / модели: продуктовый рынок, сервисная модель, аренда, подписка, managed service, внедрение, обслуживание, platform layer и т.п. Покажи, что данные родительского рынка могут доказывать, а что не могут.
8. Если речь о текущих рыночных цифрах, долях, росте, penetration, adoption, марже, ценах или конкуренции, приоритетно используй источники за последние 2-3 года. Более старые источники используй как исторический контекст, baseline или CAGR/trend context, если есть более свежие сопоставимые данные по той же географии, отрасли и подотрасли.
9. Если рынок B2B/B2G, procurement-heavy или сервисно-контрактный, проверь, нужен ли тендерный / procurement слой. Если нужен, верни tender research plan: порталы, ключевые слова, коды классификаторов, исключения, период, география, поля для выгрузки и ограничения.

Ограничения:
- Не давай generic-рекомендации.
- Не выдумывай факты, цифры, источники, кейсы или намерения участников.
- Разделяй факты, гипотезы, интерпретации и рекомендации.
- Если данных недостаточно, прямо скажи, каких данных не хватает.
- Не блокируй ранний market / category / competitor ingest из-за отсутствия BPM-4, CRM, SKU, margin, support или win/loss данных. Ранний рыночный контекст нужен до BPM-4.
- Если BPM-4 / CRM / SKU данных ещё нет, всё равно собери market context, segment hypotheses, competitor landscape, buyer-role hypotheses, source map, risks и data request design.
- Не превращай стратегические зоны в точные ICP без CRM / SKU / support / margin / win-loss / интервью / спецификаций.
- Не утверждай TAM/SAM/SOM, сегментную привлекательность, маржинальность, win-rate, service burden, adoption, implementation quality или buyer-readiness как доказанный факт без прямых данных; маркируй такие claims как `hypothesis`, `weak`, `inference`, `needs_bpm4_validation`, `needs_client_data` или `do_not_use`.
- Не используй данные родительского рынка как доказательство проникновения, экономики, adoption, supplier ranking или конкурентной позиции в деривативном рынке.
- Не приравнивай публичную видимость игрока к реальному давлению в сделках; отдельно отметь возможных скрытых региональных, white-label, интеграторских, сервисных или procurement-only игроков.
- Не подавай digital readiness, AI/PdM/analytics readiness, EHS/ERP/CRM/BI integration maturity или platform adoption как факт без интервью, внедрений, usage-data, тендерных требований или других прямых доказательств.
- Для сервисных, арендных, подписочных, managed-service, implementation или maintenance моделей отдельно проверь экономику сервиса: cost drivers, SLA, логистику, support burden, churn/renewal, working capital, contract economics и margin unknowns.
- Если не хватает client-side данных, верни `Data Request Checklist` и `Interview Scripts`, а не только общий disclaimer.
- Приоритизируй замечания по управленческим последствиям, а не по косметике.
- Не используй неутверждённые community sources: сначала предложи entry path, границы и ограничения, затем жди акцепта или исключай этот слой.

Формат ответа:
1. Structured research/review result.
2. Cross-synthesis if several source classes were used.
3. Decision Packet.
4. Notion / Readwise connector findings, if a connector was used.
5. Reader Source Acquisition Packet: separate list of sources/books/RSS/newsletters/files/services/databases to add or consider for Readwise Reader, with URLs/import paths, priorities, route decisions, and reasons.
6. Data Request Checklist and Interview Scripts if missing client-side data blocks a strong conclusion.
7. Market Boundary Check: parent market vs derivative/specific market, evidence limits, invalid shortcuts.
8. Market Data Freshness: newest usable current estimates, older sources used only as trend/baseline/CAGR/methodology where appropriate, stale sources and downgrades.
9. Tender / Procurement Research Plan, if relevant.
10. Visibility Bias / Hidden Player Check.
11. Service Economics Gate, if the model is service / rental / subscription / managed service / implementation / maintenance.
12. Market Context Status: `market_context_ready`, `hypothesis_ready`, `needs_bpm4_validation`, or `not_ready_for_durable_economic_claim`.
13. Recommended visualization or matrix, especially `segment attractiveness x accessibility` with bubble size by revenue / margin / win-rate / service burden if data exists, or confidence overlay if BPM-4 data is not available yet.
14. Self-Reflection / Improvement Notes: answer the self-check questions briefly, in first person, after the main answer. Use them to say what was missing, what should be improved, and how the next prompt/run should change.
```

## Self-Reflection Module

Every serious external prompt should ask the external model to add a short self-reflection block after the main answer. This block is not a replacement for the answer; it is a quality-control appendix for Codex and Ilya.

Instruction to include:

```text
После основного ответа добавь блок `Self-Reflection / Improvement Notes`.

Ответь кратко, от первого лица, по 1-3 предложения на каждый вопрос:

1. Чего не хватало в моём ответе?
2. Где я ответил слишком общо?
3. Где я слишком сильно опирался на интерпретацию, а не на evidence?
4. Какие источники или классы источников я использовал недостаточно?
5. Какие connector-контексты, например Notion / Readwise / Drive, могли бы улучшить ответ?
6. Какие claims самые слабые или неопределённые?
7. Что пока нельзя использовать в клиентских, публичных или durable-материалах?
8. Какие противоречия или blind spots остались?
9. Какие assumptions нужно подтвердить с Ильёй или Codex?
10. Какая таблица, визуализация, график, матрица или структурный артефакт сделал бы ответ полезнее?
11. Что упростило бы возврат ответа в Vault / CORD / Reader?
12. Что я бы изменил в prompt перед повторным прогоном?
13. Какие 3 улучшения следующего прогона дадут максимальный эффект?
14. Где я мог смешать родительский рынок и деривативный / специфический рынок?
15. Какие рыночные цифры устарели, старше 2-3 лет или должны использоваться только как исторический контекст / CAGR / baseline?
16. Нужен ли отдельный тендерный / procurement анализ, и если да, какие запросы, коды и базы надо использовать?
17. Где я мог спутать публичную видимость игрока с реальным рыночным давлением?
18. Какие claims про digital readiness / AI / аналитику / интеграции являются inference, а не fact?
19. Какие сервисные economics / margin / SLA / support burden вопросы остались не закрыты?
```

For structured outputs, request this schema:

Put these fields inside the same main output schema, not in a separate code block:

- `self_reflection.what_was_missing`
- `self_reflection.too_generic`
- `self_reflection.inference_over_evidence`
- `self_reflection.underused_sources_or_classes`
- `self_reflection.connector_contexts_that_could_help`
- `self_reflection.weakest_or_uncertain_claims`
- `self_reflection.not_ready_for_client_public_or_durable_use`
- `self_reflection.contradictions_or_blind_spots`
- `self_reflection.assumptions_to_confirm_with_ilya_or_codex`
- `self_reflection.useful_tables_visuals_or_structured_artifacts`
- `self_reflection.vault_cord_reader_return_improvements`
- `self_reflection.prompt_changes_before_rerun`
- `self_reflection.top_3_next_improvements`
- `self_reflection.parent_vs_derivative_market_risk`
- `self_reflection.market_data_freshness_risks`
- `self_reflection.tender_or_procurement_next_step`
- `self_reflection.public_visibility_bias_risk`
- `self_reflection.digital_readiness_inference_risk`
- `self_reflection.service_economics_unknowns`

## Self-Reflection Upgrade Signals

When a returned self-reflection says the answer lacked CRM, SKU, support, margin, win/loss, product-roadmap, service-desk, proposal archive, lost-deal, interview data, derivative-market evidence, tender/procurement analysis, recent market figures, hidden-player checks, digital-readiness proof, or service-economics data, treat that as a valid prompt-improvement signal by default.

Do not automatically change Vault or project canon from it. Instead, in return-packet mode:

- turn it into `data_gaps`, `client_questions`, and `next_run_requirements`;
- mark blocked claims as `not_ready_for_client_public_or_durable_use`;
- separate parent-market context from derivative-market proof;
- check whether stale market figures must be replaced by newer 2-3 year sources or downgraded to trend / baseline / CAGR context;
- if tender/procurement analysis is recommended, extract the query terms, classification codes, portals, fields, time window, and relevance rules needed for the next run;
- if hidden players are suspected, add a visibility-bias check and field/CRM/interview routes to find them;
- ask whether Ilya wants the next prompt to include anonymized client-side rows, lost deals, SKU groups, geography, service pain, integrations, and strategic objective;
- if source recommendations are included, route them through Reader Source Acquisition Packet / Reader candidate ledger;
- if interviews are recommended, extract audience-specific interview scripts.

Common next-run requirements:

```yaml
next_run_requirements:
  anonymized_crm_rows: "needed|optional|not_needed"
  sku_groups: "needed|optional|not_needed"
  margin_or_economics: "needed|optional|not_needed"
  support_or_service_data: "needed|optional|not_needed"
  win_loss_or_lost_deals: "needed|optional|not_needed"
  integrations_or_product_specs: "needed|optional|not_needed"
  derivative_market_sources: "needed|optional|not_needed"
  tender_or_procurement_export: "needed|optional|not_needed"
  recent_market_figures_last_2_3_years: "needed|optional|not_needed"
  service_contract_economics: "needed|optional|not_needed"
  hidden_player_discovery: "needed|optional|not_needed"
  digital_readiness_evidence: "needed|optional|not_needed"
  geography: "needed|optional|not_needed"
  strategic_objective: "revenue_growth|margin_growth|platform_value|segment_choice|other|unknown"
  interviews:
    - audience: ""
      count_or_depth: ""
      key_questions: []
  competitor_teardown_inputs:
    competitor_list: []
    desired_artifacts: "commercial proposals|specifications|demos|public pages|partner pages|other"
```

## Return Loop

When Ilya brings the external answer back, do not accept it blindly.

Convert it into a local decision packet:

- `accepted`: what we accept and why;
- `change`: what should change in the artifact, plan, prompt, project, КП, content, rule, or skill;
- `defer`: useful but not now;
- `reject`: what Pro / Perplexity got wrong or overreached;
- `client_questions`: what should be asked externally;
- `data_gaps`: what data is missing;
- `risk_gaps`: what remains risky;
- `next_run_requirements`: client-side data, interviews, connectors, or teardown inputs needed before a stronger rerun;
- `not_ready_for_client_public_or_durable_use`: claims that must not leave the advisory layer yet;
- `writeback_targets`: existing Vault/workspace files or contours that may need update;
- `next_action`: the smallest useful next move.

If the external answer includes `Self-Reflection / Improvement Notes`, treat that block as a suggestion backlog for improving future use of `deepresearch` or adjacent skills.

Rules:

- self-reflection items are suggestions, not accepted changes;
- do not patch `deepresearch`, another skill, `SKILLS.md`, APQ, rules, prompts, automations, Vault files, CORD, or Reader directly from self-reflection suggestions;
- if the returned packet is about the skill system, route it through `skill-system-governance` and require `skill-eval-harness` coverage before material patches are considered complete;
- before turning any self-reflection into a skill improvement, strip project, client, industry, geography, competitor, product, and one-off factual specifics unless they expose a reusable research failure mode;
- extract them into `skill_improvement_suggestions`;
- discuss them with Ilya as `accepted / change / defer / reject`;
- only after Ilya accepts a suggestion may Codex apply a skill/rule/prompt/writeback change through the normal approval gate;
- if self-reflection is missing, mark `self_reflection_missing: true` in the local return packet and decide whether to rerun or proceed.
- when a real-client return packet produces many related data requests, interview scripts, source checks, and validation needs, do not create many microtasks by default. Bundle them into one `reconciliation sprint` task with owner/contour, time box, expected output, source trace, and validation purpose. For RG1 projects, sync that bundled task to the RG1 Google Spreadsheet as the primary tracker and keep local Vault task rows as trace.

Suggested local structure:

```yaml
skill_improvement_suggestions:
  - suggestion: ""
    source: "self_reflection|codex_return_review"
    affected_skill_or_process: "deepresearch|competitor-research|other"
    specificity_cleanup_done: true
    why_it_may_help: ""
    proposed_action: ""
    eval_required: true
    status: "suggestion_needs_ilya_review"
self_reflection_missing: false
```

For skill-system reviews, use this additional local packet before patching:

```yaml
skill_system_return_packet:
  source: "external_researcher|chatgpt_pro|perplexity|codex_return_review"
  status: "advisory_not_canon"
  accepted: []
  change: []
  defer: []
  reject: []
  affected_skills: []
  anti_sprawl_decisions: []
  patch_backlog: []
  eval_requirements: []
  dlp_notes: []
  next_action: ""
```

If the external answer includes source recommendations, build a local Reader candidate ledger before importing anything:

- source / book / service / file;
- URL or import path;
- why relevant;
- job-to-be-done;
- target use;
- priority;
- route decision;
- tags;
- risks/limits;
- recommendation: add now / discuss / skip.

Do not add sources to Readwise Reader just because Pro / Perplexity recommended them. First discuss the ledger with Ilya. Import to Reader only after explicit approval, using the Readwise MCP when available.

For NotebookLM-like or external-model outputs, treat the answer as `proposal-review` unless Ilya explicitly says to canonicalize or write back.

For 4th-department projects with an existing or required `BPM Storyline-Storyboard`, `proposal-review` is not enough by itself. If the external answer materially concerns market/category/competitors/positioning/sales model/buyer roles/channel/reuse/BPM evidence, classify it as a BPM-candidate source, produce the local return packet, and then update the existing Storyline-Storyboard or record an explicit no-op reason there before finalizing. The required chain is:

`external output -> local return packet -> possible BPM increments -> SI / slide hypotheses -> lack of knowledge / field questions`.

If Ilya assigns the external output to a BPM such as `BPM-7A`, treat that BPM as primary and still record secondary BPM increments when the output also touches competitors, buyer roles, sales process, channel, CRM, or product matrix.

#### BPM-7A/B Prompt Generation Gate

When Ilya asks to compose a research prompt for `BPM-7A`, `BPM-7B`, `BPM7AB`, `семь АБ`, market-sizing, market-by-products/industries/regions, competitor-market mapping, or asks to make a strong external prompt for a 4th-department project market analysis, keep the normal `deepresearch` discipline and additionally treat the output as a `BPM-7A/B` external research prompt. The prompt must be fed by accumulated SI / slide hypotheses / data gaps from other BPMs that already route signal into `BPM-7A/B`.

Primary interpretation:

- `BPM-7A` = market analysis / market-sizing: TAM/SAM/SOM, demand pools, growth/decline, segment attractiveness, investment cycles, geography, customer industries, procurement patterns, and data quality.
- `BPM-7B` = market analysis by products / industries / regions: product-category map, customer-industry map, regional map, player roles, channel structure, buyer roles, substitutes, procurement/tender layer, and segment prioritization.
- `BPM7AB` / `семь АБ` = combined `BPM-7A + BPM-7B` packet unless Ilya explicitly narrows it.

Before producing the prompt, perform a local BPM-exchange preflight from existing project artifacts. Use calibrated top-K filtering, not all available context. Include only the strongest signals that have already produced SI, slide hypotheses, data gaps, or routing relevance into `BPM-7A/B`; if no project-specific calibration exists, state that the K choice is heuristic.

Eligible feeder BPMs include any BPM that already generated a signal relevant to market/category analysis:

- `BPM-2` / interviews: client voice, owner framing, buyer roles, target industries, perceived competitors, procurement realities, field pressure, segment pain.
- `BPM-3`: current/lost/customer/partner/integrator voice, if available.
- `BPM-4`: revenue, margin, product, CRM, win/loss, SKU, funnel, geography, or client-portfolio facts that shape market priority.
- `BPM-5`: mystery-shopper / commercial-offer evidence, competitor selling behavior, visible go-to-market.
- `BPM-6`: desk research, competitor map, category map, public claims, source leads.
- `BPM-8`: process / delivery constraints that affect market accessibility or service burden.
- `BPM-9`: competence / role gaps that affect addressable market execution.
- `BPM-10`: CRM / pipeline / lead-source / conversion signals.
- `BPM-11`: target data model / entity definitions needed to avoid confused categories.
- `BPP/BPA/Storyline-Storyboard`: accepted storyline, SI, slide hypotheses, lack-of-knowledge, evidence gates.

The generated external prompt must explicitly say:

`This is a public evidence map, not the client's lived market map, until reconciled with BPM-2/BPM-3 client evidence, BPM-4 economics, BPM-10 CRM/pipeline data, and the project Storyline-Storyboard.`

The prompt must request outputs that are usable as BPM-return material:

```yaml
bpm7ab_research_packet:
  primary_bpm: "BPM-7A/B"
  feeder_bpm_signals:
    - bpm: ""
      signal: ""
      why_it_matters_for_BPM7AB: ""
      source_family: "internal|external|mixed|inference"
      confidence: "low|medium|high"
  market_boundary:
    parent_market: ""
    specific_market_or_segments: []
    exclusions: []
  market_sizing:
    TAM: ""
    SAM: ""
    SOM_or_accessible_pool: ""
    confidence: ""
    evidence_limits: []
  segment_map:
    - segment: ""
      demand_driver: ""
      current_pressure: ""
      accessibility: ""
      fit_with_project_hypotheses: ""
      data_needed_from_client: []
  competitor_market_map:
    - player: ""
      role: "direct_competitor|EPC_integrator|distributor|OEM|regional_hidden_player|substitute|partner_channel|benchmark|unknown"
      public_visibility: "strong|medium|weak|unknown"
      likely_client_reported_pressure: "strong|medium|weak|none|unknown"
      evidence: []
      action: "prioritize|monitor|interview_more|CRM_check|benchmark_only|downgrade|exclude"
  procurement_tender_layer:
    relevance: "required|recommended|optional|not_relevant"
    portals: []
    query_terms: []
    okpd_or_other_codes: []
    fields_to_extract: []
  data_request_to_validate:
    BPM-2_or_BPM-3_questions: []
    BPM-4_fields: []
    BPM-10_fields: []
    BPM-11_entities: []
  storyline_delta_candidates:
    appeared: []
    strengthened: []
    weakened: []
```

For prompt-only mode, do not write BPM-7A/B results into Vault. The external prompt should return a packet that Codex can later convert into local Return Packet, Storyline-Storyboard deltas, BPM increments, data requests, and no-op reasons.

## Write-Back Rules

Follow the active Vault rules:

- use existing files first;
- do not create new files unless Ilya explicitly asks for file output or the current rules allow the exact artifact;
- do not write external output directly into canon without local review;
- mark source as `external deepresearch / ChatGPT Pro / Perplexity review` if the idea enters a durable artifact;
- if the output affects commercial facts, project trace, content plan, BPM/SI, or rules, route it through the appropriate existing contour before editing.

## Done Definition

For prompt-only:

- prompt is paste-ready;
- prompt is delivered as one copyable block, with no required second copy/paste block;
- structured brief, operating context, source plan, constraints, output format, and safety are explicit;
- if the question involves segment choice, ICP, economics, margin, win/loss, service burden, platform value, SKU/product groups, or route-to-market, client-side data gaps and blocked claims are explicit;
- prompt asks for Data Request Checklist / Interview Scripts when client-side data is missing;
- prompt asks the external model to include `Self-Reflection / Improvement Notes` after the main answer;
- if source acquisition is in scope, Reader Source Acquisition Packet is explicitly requested;
- sensitive context is filtered or summarized;
- no unapproved community extraction is included.

For recurring monitor:

- Ilya explicitly approved transition to recurring mode;
- cadence, horizon, watchlist, source plan, significance threshold, output format, and return route are defined;
- prompt does not claim external scheduling unless the external tool supports it;
- Codex automation is created only after explicit confirmation;
- community entry paths are either explicitly approved and scoped, or excluded;
- monitoring stack decision is explicit: connect now, conditional, quarantine, or exclude;
- Reader source candidates are returned as a candidate ledger and not imported until Ilya approves;
- adapters produce normalized events and do not write directly into Vault.

For full research / review loop:

- structured brief exists;
- source plan exists;
- selected external runs are clearly separated;
- cross-synthesis is requested when there are multiple runs;
- external answer returns as decision packet;
- early market/category/competitor ingest is allowed and expected before BPM-4 exists;
- external answer returns useful market context, segment hypotheses, competitor landscape, buyer-role hypotheses, source map, risks, and data-request design even when CRM/SKU/support/margin/win-loss data is missing;
- external answer separates strategic zones from precise ICP when client-side evidence is missing;
- external answer marks TAM/SAM/SOM, segment attractiveness, margin, win-rate, service burden, adoption, implementation quality, and buyer-readiness claims as hypothesis/weak/inference/needs-bpm4-validation/needs-client-data unless direct data supports them;
- external answer includes `market_context_status` so Codex can distinguish market context readiness from economic/ICP validation readiness;
- external answer includes Data Request Checklist, Interview Scripts, and next-run requirements when stronger conclusions depend on client-side evidence;
- external answer includes self-reflection / improvement notes, or Codex marks that block as missing in the return packet;
- self-reflection suggestions are routed to Ilya for review before any skill/rule/prompt/writeback change;
- Codex creates local return packet;
- source recommendations become Reader candidates, not immediate imports;
- accepted changes are routed to correct existing artifacts or explicitly left as no-op.
- if community sources were used, entry path, source limits, safety constraints, and resulting artifacts are recorded.

Not done if:

- the external prompt refuses or delays early market/category/competitor ingest merely because BPM-4, CRM, SKU, margin, support, or win/loss data does not exist yet;
- the external prompt asks for a precise ICP, segment priority, margin strategy, platform value, or route-to-market recommendation without distinguishing early hypotheses from claims that need BPM-4/client-side validation;
- the answer presents external web inference as enough to decide segment economics, win-rate, service burden, buyer readiness, adoption, or implementation quality;
- missing CRM / SKU / support / margin / win-loss / interview data is mentioned only in self-reflection but not converted into Data Request Checklist, client questions, or next-run requirements;
- client-facing, public, or durable claims are not separated from weak advisory claims;
- the answer recommends interviews but does not specify audiences and question blocks;
- the answer recommends sources/services/databases but does not route them through Reader/source acquisition review.

## Writeback / Approval Gate

This skill is high-risk because it can send context to external ChatGPT Pro / Perplexity, request connector searches, return advisory outputs, propose Vault/CORD/rule/skill changes, and import source candidates into Readwise Reader.

Before sending sensitive or internal context externally, ask Ilya if the packet includes client names, economics, commercial terms, internal methodology, project statuses, private Notion/Vault content, or other non-public material. Before durable writeback, show the return packet, `accepted/change/defer/reject`, writeback targets, source sensitivity, and exact proposed action.

External answers are advisory, not canon. Do not write them into Vault, rules, skills, CORD, Reader/Readwise, or external communications without explicit approval from Ilya.

## Externalization / DLP Gate

Treat any transfer to ChatGPT Pro, Perplexity, client, partner, public channel, connector, or external reviewer as a DLP-controlled action.

Before externalization, classify the packet:

- `public`: safe public context;
- `internal`: Paper Planes internal methodology, process, statuses, or artifacts;
- `client-sensitive`: client names, project facts, economics, contracts, prices, delivery risks, people, or statuses;
- `restricted`: material that must not leave the local Codex/Vault contour without a separate explicit approval.

Default: if unsure, treat as `client-sensitive`. Sanitize or abstract client names, economics, commercial terms, internal methodology, private Notion/Vault excerpts, personal data, and project statuses. External prompts should receive the minimum context needed for the question, with internal/external/inference labels preserved.
