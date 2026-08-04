# Ingest Layer

Use this reference when attached survey files must be read, normalized, or assessed for reuse.

## Supported Inputs

- Tally CSV/XLSX exports.
- Anketolog / Yandex / other platform XLSX.
- Google Sheets / CSV.
- Aggregated result tables.
- Questionnaire text, PDF, DOCX, or pasted form.
- Field result exports with respondent rows.

## Normalized Question Schema

```yaml
question:
  source_file: ""
  survey_name: ""
  raw_column: ""
  normalized_text: ""
  survey_type: "B2C Choice | EVP Employer | Internal Employee | Event Conference | B2B2C | unknown"
  family: "screening | behavior | frequency | scenario | factor | barrier | switching | channel | trust | WTP | awareness | consideration | NPS | open | matrix | demographics"
  answer_type: "single | multi | likert | matrix | numeric | open | ranking | unknown"
  base_n: 0
  recovery_status: "verified | reconstructed | unreliable"
  reuse_status: "ready | adapt | source_check | do_not_reuse"
  notes: ""
```

## Tally / Matrix Handling

Treat Tally as a core input format, not a legacy exception.

Common issues:

- JSON-in-cell matrix answers.
- UUID row/option ids instead of readable labels.
- HTML entities in answer text.
- hidden fields or technical columns.
- duplicated "Other" fields.
- exported form lacks schema with row labels.

Procedure:

1. Detect delimiter and encoding.
2. Separate metadata columns (`submittedAt`, `respondentId`, `isCompleted`) from questions.
3. For each cell, detect whether value is plain text, multi-select text, JSON, or broken JSON.
4. Parse JSON answers and collect option values.
5. Try to recover matrix row labels only if they are present in the export or form schema.
6. Assign recovery status:
   - `verified`: question text, row labels, option labels are readable.
   - `reconstructed`: answer values are readable but row/option mapping is inferred.
   - `unreliable`: UUIDs cannot be mapped to labels or the matrix structure is ambiguous.
7. Exclude `unreliable` fields from clustering and benchmarks unless the user accepts a low-confidence exploratory read.

## Data Health Checks

Always report:

- number of rows and completed responses;
- number of columns/questions;
- missingness and suspicious empty columns;
- base size per branch;
- fields with JSON/UUID recovery issues;
- fields unsafe for clustering;
- open-answer language and encoding issues.

## Reuse Classification

Mark each question:

- `ready`: reusable almost as-is;
- `adapt`: reusable family, rewrite wording/category labels;
- `source_check`: useful but needs schema/source confirmation;
- `do_not_reuse`: broken, too project-specific, leading, or low-quality.
