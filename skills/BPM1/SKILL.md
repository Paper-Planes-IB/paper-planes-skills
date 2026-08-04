---
name: BPM1
description: Use when Ilya asks to prepare a BPM-1 survey, reuse old surveys, build a questionnaire, process survey results, forecast likely survey results before fieldwork, compare prior vs fact, extract JTBD/clusters from quantitative survey factors, or route survey evidence into BPM-SI, Storyline-Storyboard, slides, reusable question banks, or survey benchmarks.
---

# BPM1

## Core Principle

`BPM1` is a survey reuse and prior-building skill. It helps design smarter questionnaires, reuse Paper Planes survey archives / Survey Lake, pull external benchmarks, build a probabilistic prior before fieldwork, process field results, compare `prior vs fact`, and return the new evidence into reusable knowledge.

Never present prior as field fact. A prior is a structured hypothesis with evidence, confidence, interval, and field-validation need.

## Mandatory Preflight

Before drafting or analysing a survey, state:

```yaml
preflight:
  project_or_category: ""
  survey_type: "B2C Choice | EVP Employer | Internal Employee | Event Conference | B2B2C | unknown"
  delivery_stage: "questionnaire | pre-field prior | post-field analysis | reuse extraction | BPM-SI routing"
  survey_lake_mode: "search | ingest | update | not_needed | unknown"
  evidence_available:
    internal_archive: "found | attached | missing | unknown"
    external_benchmarks: "needed | not_needed | already_given"
    field_results: "attached | missing | not_yet"
  allowed_writeback: "chat_only | existing_files_only | explicit_file_creation_allowed"
  forbidden_actions:
    - "do not treat prior as fact"
    - "do not mix B2C, EVP, internal employee, event, and B2B2C priors"
    - "do not use unreliable reconstructed matrix fields without low-confidence marking"
```

If the user only gives files, inspect them and classify their reusable value. Do not create files unless explicitly asked.

## BPM Guard

- In B2C, baseline is almost always `BPM-1`: quantitative survey, factor ratings, frequency, open answers, k-means by choice factors, scenarios, barriers, channels, price sensitivity.
- `BPM-3` is almost never a standard B2C block. Use it in B2C only as rare qualitative deepening: high-consideration/high-risk choice, unclear clusters, claims language source-check, or explicit interview scope.
- In B2B / B2B2C / dealer / partner markets, `BPM-3` can be a functional analogue of `BPM-1`: interviews may provide the primary map of choice factors, barriers, buying roles, service requirements, documents, timing, channel, and commercial policy.

## Workflow

### 1. Classify Survey Type

Choose one primary type before building a prior. If uncertain, say what evidence would disambiguate.

- `B2C Choice`: buying, consumption, category, brand, frequency, price, WTP, NPS, barriers, choice factors.
- `EVP Employer`: employer choice, offer, employer brand awareness, job search channels, consideration, refusal reasons.
- `Internal Employee`: leadership, rules, engagement, culture, benefits, tenure, eNPS, internal service.
- `Event Conference`: attendance, non-attendance, speakers, tickets, online/offline, event NPS, return intent.
- `B2B2C`: channel + end customer, dealer/distributor + consumer, service and product priors must be separated.

Read `references/survey-types.md` when questionnaire families, slide types, or type-specific anti-patterns matter.

### 2. Discover and Ingest Evidence

Use attached files first, then local/Vault search if relevant, then external sources if current source-check is needed.

Supported formats:

- Tally CSV/XLSX exports;
- Anketolog/Yandex/other survey XLSX;
- Google Sheets / CSV;
- aggregated tables;
- questionnaire text/PDF;
- field result exports.

For Tally and matrix/rating exports, treat JSON-in-cell and UUID fields as a first-class case. Parse what can be parsed, but assign each question/field a recovery status:

- `verified`: labels and answer mapping are clear;
- `reconstructed`: structure is inferred and plausible;
- `unreliable`: UUID/row labels/form schema are missing or contradictory.

Do not use `unreliable` fields in priors, clusters, or reusable banks without explicit low-confidence marking.

Read `references/ingest-layer.md` for normalization schema and Tally handling.

### 3. Survey Lake Mode

Use Survey Lake Mode when the user asks about reuse, old surveys, survey corpus, "озеро опросов", benchmarks, prior, reusable questions, or when a new survey file should become future reusable knowledge.

Default local Survey Lake storage for this skill:

```text
/Users/iliabalahnin/.codex/skills/BPM1/survey_lake
```

If this folder exists, consult it before broad archive search. If it is missing or stale, say so and fall back to attached files / local search.

Survey Lake is not just raw files. It has six layers:

1. `raw_files`: original CSV/XLSX/PDF/DOCX/exports without alteration.
2. `surveys`: registry rows, one row per survey.
3. `questions`: normalized reusable question bank.
4. `metrics`: reusable benchmark rows with base, value, context, and confidence.
5. `factors_jtbd`: factor, cluster, and JTBD candidates.
6. `slide_patterns`: how survey findings become BPM-SI, Storyline-Storyboard, and slides.

Modes:

- `search`: find similar surveys, questions, metrics, factors, and slide patterns for a new project.
- `ingest`: classify attached survey files and produce lake-ready records.
- `update`: after fieldwork, convert results into reusable questions, metrics, JTBD, clusters, and slide patterns.

In chat-only mode, produce a lake packet but do not write it. If the user explicitly asks to create/update the lake, use existing storage if defined; if storage is not defined, ask for or propose a storage location.

Read `references/survey-lake.md` for schemas, search logic, and update packets.

### 4. Build or Improve the Questionnaire

A BPM-1 questionnaire should usually include:

- screening and quota logic;
- behavior / frequency;
- scenarios and occasions;
- choice factors;
- barriers and refusal reasons;
- switching / churn / competitor consideration;
- trust and channels;
- price / WTP;
- open answers for language;
- factor block suitable for k-means;
- JTBD bridge questions.

For EVP, internal employee, event, or B2B2C surveys, use the relevant families from `references/survey-types.md`.

Every proposed question should have a role:

```yaml
question_role:
  question: ""
  source: "new | reused_internal | adapted_internal | external_benchmark | field_validation"
  tests: "factor | barrier | segment | JTBD | WTP | channel | trust | awareness | behavior"
  why_needed: ""
  can_remove_if_space_limited: true
```

### 5. Build Pre-Field Prior

Before fieldwork, produce a prior forecast with ranges, not false precision:

```markdown
| Parameter | Expected prior | Interval | Evidence | Confidence | Field decision |
|---|---:|---:|---|---|---|
```

Confidence labels:

- `HIGH`: strong prior / stable benchmark, still not field fact;
- `MEDIUM`: likely scenario, needs field confirmation;
- `LOW`: hypothesis, must be checked in field;
- `NO DATA`: exploratory question required.

Read `references/source-map.md` for external sources and `references/methodology.md` for weighting, similarity, recency, confidence, and VOI logic.

### 6. Create Field Validation Plan

Show how the future field result will be interpreted:

```yaml
field_validation_plan:
  must_test:
    - parameter: ""
      why_decision_relevant: ""
      expected_prior: ""
      what_would_change_strategy: ""
  low_value_questions_to_cut: []
  exploratory_questions_to_add: []
```

Prioritize high-impact/high-uncertainty questions. Remove questions whose answers are already stable and not decision-relevant.

### 7. Post-Field Analysis

When field results arrive:

1. Parse and normalize results.
2. Count base sizes, completions, missingness, quotas, and reliability gaps.
3. Calculate frequencies, top-2-box, means, rankings, WTP ranges, awareness/consideration, barriers.
4. Separate stated importance from derived importance when data allows.
5. Build factor clusters with k-means only when the factor matrix is valid enough.
6. Translate clusters into likely JTBD, not by naming demographics alone.
7. Compare `prior vs fact`.
8. Identify surprises and explain likely causes.
9. Produce slide implications.
10. Produce reusable update packet.

Do not run k-means on broken matrix exports, tiny bases, or fields with unknown labels. If clustering is unsafe, say so and use descriptive segmentation instead.

### 8. Route Results to BPM-SI and Storyline

Survey results usually become slides and SI, not just tables. Route findings into:

- factors of choice / drivers and barriers;
- segment and cluster map;
- JTBD and occasions;
- QFD / voice-to-product translation;
- CJM / service blueprint implications;
- offer / product / format decisions;
- loyalty / CRM / retention hypotheses;
- price/WTP implications;
- storyline claims and evidence gates.

If working in a project with existing `BPM Storyline-Storyboard` or `BPM-SI` files, do not write to them unless the user explicitly allows. In chat, show the delta as:

```markdown
Появились:
Усилились:
Ослабли:
```

### 9. Update Reusable Knowledge / Survey Lake

At the end of post-field work, produce a reusable update packet:

```yaml
reusable_update:
  survey_type: ""
  category: ""
  reusable_questions:
    - question: ""
      reuse_condition: ""
  benchmark_candidates:
    - metric: ""
      observed_value: ""
      confidence: ""
      reuse_scope: ""
  jtbd_candidates: []
  cluster_archetypes: []
  slide_patterns: []
  caveats: []
```

Also produce a Survey Lake update packet when the result should become future reuse:

```yaml
survey_lake_update:
  surveys: []
  questions: []
  metrics: []
  factors_jtbd: []
  slide_patterns: []
  recovery_issues: []
  writeback_target: "chat_only | existing_file | database | spreadsheet | unknown"
```

Only write this into files when the user explicitly asks or existing local rules allow the specific writeback.

## Output Contract

For questionnaire work:

1. Executive summary.
2. Survey type and BPM guard.
3. Reused question map.
4. Proposed questionnaire.
5. Prior forecast table.
6. Field validation plan.
7. Risks and missing evidence.
8. Survey Lake update/search packet, if relevant.

For post-field analysis:

1. Data health note.
2. Main numbers.
3. Factors / barriers / WTP / channels.
4. Clusters and JTBD.
5. Prior vs fact.
6. Surprises.
7. Slide implications.
8. Reusable update packet.
9. Survey Lake update packet.

## Hard Guardrails

- Prior is never a fact.
- Never silently mix survey types.
- Never treat B2C `BPM-3` as a standard companion to `BPM-1`.
- Never use external sources without labeling them as direct, adjacent, weak proxy, context, or not useful.
- Never hide base sizes.
- Never overinterpret open answers as representative frequencies.
- Never run factor clustering without checking matrix validity.
- Never treat Tally UUID fields as labels.
- Never put `unreliable` recovered fields into the benchmark bank without low-confidence marking.
- Never leave new useful survey evidence only in chat if the user explicitly asks to register/reuse it.
