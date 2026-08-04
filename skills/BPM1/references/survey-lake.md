# Survey Lake

Use this reference when BPM1 needs durable reuse from old surveys or needs to return a new survey into reusable knowledge.

Survey Lake is a structured memory layer for BPM-1. It is not a folder of raw CSV files. Raw files are only the first layer; reusable value comes from registry, question, metric, JTBD, and slide-pattern records.

Default local storage for this skill, when present:

```text
/Users/iliabalahnin/.codex/skills/BPM1/survey_lake
```

## Layers

1. `raw_files`: original files without edits.
2. `surveys`: one row per survey.
3. `questions`: one row per normalized question.
4. `metrics`: one row per reusable number/benchmark.
5. `factors_jtbd`: factor clusters, segment hypotheses, JTBD candidates.
6. `slide_patterns`: how results became slides, SI, Storyline-Storyboard, or decisions.
7. `recovery_issues`: parsing/schema/matrix/UUID/quality caveats.

## Minimal Schemas

### surveys

```yaml
survey:
  survey_id: ""
  project: ""
  survey_type: "B2C Choice | EVP Employer | Internal Employee | Event Conference | B2B2C | unknown"
  category: ""
  geography: ""
  field_date: ""
  sample_n: 0
  platform: "Tally | Anketolog | Yandex | Google Sheets | XLSX | CSV | unknown"
  raw_file: ""
  recovery_status: "verified | partly_reconstructed | unreliable"
  reuse_value: "high | medium | low | no_reuse"
  notes: ""
```

### questions

```yaml
question:
  question_id: ""
  survey_id: ""
  family: "screening | behavior | frequency | scenario | factor | barrier | switching | channel | trust | WTP | awareness | consideration | NPS | open | matrix | demographics"
  normalized_text: ""
  answer_type: "single | multi | likert | matrix | numeric | open | ranking | unknown"
  options_summary: ""
  recovery_status: "verified | reconstructed | unreliable"
  reuse_status: "ready | adapt | source_check | do_not_reuse"
  adapt_for: []
  caveat: ""
```

### metrics

```yaml
metric:
  metric_id: ""
  survey_id: ""
  category: ""
  survey_type: ""
  metric: ""
  value: ""
  percent: null
  base_n: 0
  segment: ""
  source_question_id: ""
  confidence: "HIGH | MEDIUM | LOW | NO DATA"
  reuse_scope: ""
  caveat: ""
```

### factors_jtbd

```yaml
factor_jtbd:
  item_id: ""
  survey_id: ""
  category: ""
  factor_or_cluster: ""
  jtbd_hypothesis: ""
  evidence: ""
  confidence: "HIGH | MEDIUM | LOW"
  reuse_scope: ""
```

### slide_patterns

```yaml
slide_pattern:
  pattern_id: ""
  survey_id: ""
  input_signal: "factor ranking | barrier | brand funnel | WTP | cluster | JTBD | open answers | prior_vs_fact"
  slide_type: "factor hierarchy | brand funnel | JTBD map | cluster map | barrier map | QFD | CJM | price ladder | evidence gate"
  example_title: ""
  reuse_condition: ""
```

## Search Logic

For a new project:

1. Classify survey type.
2. Extract category, geography, audience, decision, and likely slide needs.
3. Search `surveys` for same type first.
4. Rank analogs by:
   - survey type match;
   - category proximity;
   - audience proximity;
   - geography;
   - recency;
   - field/sample quality;
   - recovery status;
   - question-family overlap.
5. Pull:
   - reusable questions;
   - reusable metrics;
   - prior ranges;
   - likely factors/JTBD;
   - slide patterns.
6. Mark each reuse item as `direct`, `adjacent`, `weak_proxy`, or `context`.

Never pull an attractive metric without its base, category, and source caveat.

## Ingest Logic

For attached files:

1. Preserve raw file reference.
2. Identify survey platform and file type.
3. Count rows, completed rows, columns/questions.
4. Classify survey type.
5. Build `surveys` registry draft.
6. Extract reusable question rows.
7. Extract metric candidates only when labels/base are reliable.
8. Extract factor/JTBD candidates only after matrix validity checks.
9. Produce recovery issues.

If Tally matrix UUID labels cannot be mapped, questions can enter the lake as `source_check`, but metrics/clusters should not enter as reliable benchmarks.

## Update Logic After Fieldwork

Post-field output must include:

```yaml
survey_lake_update:
  surveys:
    - survey_id: ""
  questions:
    - question_id: ""
  metrics:
    - metric_id: ""
  factors_jtbd:
    - item_id: ""
  slide_patterns:
    - pattern_id: ""
  recovery_issues: []
  no_write_reason: ""
```

Classify every update:

- `new`: new reusable knowledge.
- `strengthens`: confirms prior or old benchmark.
- `weakens`: contradicts or narrows old benchmark.
- `replaces`: newer/better source supersedes old source.
- `no_reuse`: project-specific or low-quality.

## Storage

If no physical Survey Lake storage exists yet, do not invent that it exists. Say:

```text
Survey Lake storage is not defined yet. I can produce a lake-ready packet in chat, or, with permission, create/update the chosen storage.
```

Good starting storage options:

- a folder with raw files plus CSV/Markdown registry files;
- a Google Sheet / Airtable-like table with the schemas above;
- a lightweight SQLite database if automated querying is needed;
- a Vault folder only if local rules allow file creation.
