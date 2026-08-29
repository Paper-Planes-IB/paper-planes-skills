---
name: interview-brief-by-analogs
description: Use when preparing questions, agendas, hypotheses, or briefing notes for project interviews, client interviews, expert interviews, content interviews, case interviews, respondent calls, role-specific interviews, sector-specific interviews, or requests like "какие вопросы задать", "подготовь к интервью", "бриф интервью", "вопросы респонденту".
---

# Interview Brief By Analogs

## Core Idea

Prepare interview questions from three evidence layers:

1. Current project context: project card, administrative scale, meeting notes, hypotheses, deliverables.
2. Vault analogs: past projects, interviews, cases, published materials, and tagged fragments with similar role, sector, problem, project type, stage, or source.
3. Open-world context: current sector context, market structure, role-specific concerns, benchmarks, regulation, public company facts, and outside language.

Never blend these layers silently. Label what comes from Vault, what comes from external sources, and what is an inference.

## Trigger Interpretation

When the user asks for interview questions, first classify the mode:

- **Project interview:** diagnosis, implementation, administrative scale, BPM, org design, strategy, client operations.
- **Content interview:** article, case, longread, expert commentary, publication, narrative harvesting.
- **Hybrid interview:** both project extraction and content extraction matter. Use both output blocks, but avoid duplicating questions.

If the user gives only a project or respondent name, infer mode from folder/project context. If still unclear, produce a hybrid brief.

## Required Context Pass

Before drafting questions:

1. Read CORD/session context required by the local project rules if not already loaded.
2. Read the five root registries before classification: `Vault/__Глоссарий.md`, `Vault/__Персоналии.md`, `Vault/__Проекты.md`, `Vault/__География.md`, `Vault/__Теги.md`.
3. Locate the current project/material context:
   - project card;
   - administrative scale / analysis / products;
   - recent meetings, interviews, processed notes;
   - existing weekly/content/draft context if content mode.
4. Extract query coordinates:
   - respondent role or должность;
   - sector / отрасль;
   - project type;
   - stage;
   - known problems;
   - target deliverable.

If a coordinate is missing, infer it from nearby files and mark the inference.

## BPM Exchange / Client Reality Preflight

When the interview is part of a 4th-department BPM project, run a BPM exchange preflight before drafting questions.

Look for active or candidate signals from:

- BPM-SI matrix and Storyline-Storyboard gaps;
- deepresearch / competitor-research return packets;
- presentation QA weak-evidence or overclaim notes;
- prior BPM-1 / BPM-2 / BPM-3 voice findings;
- BPM-4 dashboard/data requests;
- BPM-5 commercial trace or win/loss candidates.

Do not dump all matching context into the interview prompt. Build a compact `preflight_summary` first:

```yaml
preflight_summary:
  project: ""
  interview_bpm: "BPM-1|BPM-2|BPM-3"
  top_signals:
    - signal_id: ""
      relevance_score: 0.0
      route_class: "required_check|optional_enrichment|watch|no_op"
      why_this_matters: ""
      question_to_inject: ""
  archive_analogs_used: []
  conflicts_to_test: []
```

Use top-K filtering: by default inject no more than 3-5 exchange signals and 3 archive analogs. If more are relevant, group them into a single synthesis question instead of creating a long list.

Classify routes:

- `required_check`: the interview can confirm, falsify, or materially change a project claim, competitor priority, commercial decision, storyline, or data requirement.
- `optional_enrichment`: the interview can add examples or language but does not block the current hypothesis.
- `watch`: useful to keep in mind, but do not ask unless the respondent naturally opens the topic.
- `no_op`: not relevant for this respondent or stage.

If an external research packet has a `client_reality_reconciliation_gate`, treat it as a BPM-2/BPM-3 question source. Convert public claims into falsification and correction questions, not confirmation-only prompts.

If the interview happens after external research, design the brief so the resulting notes can produce a `client_correction_packet`:

| external finding | client correction | effect on priority | evidence needed | action |
|---|---|---|---|---|

Use correction categories: `confirmed`, `strengthened`, `weakened`, `contradicted`, `renamed / normalized`, `added by client`, `moved to historical`, `moved to partner/channel`, `moved to benchmark`, `requires CRM/win-loss`. When a correction affects economics, CRM, ownership, implementation rhythm, or data fields, route follow-up to BPM-4, BPM-5, BPM-9, BPM-10, or BPM-11.

When competitor, partner, vendor, product, platform, or technology names come from transcripts, voice notes, client calls, OCR, auto-summary, or informal speech, do not treat them as confirmed entities. Add a normalization table:

| raw_name | likely_normalized_name | confidence | why | needs_confirmation_from |
|---|---|---|---|---|

Use `normalized_candidate` until the respondent, Ilya, CRM, source-check, or a trusted project artifact confirms the entity. Ask disambiguation questions when needed:

- "Как это название пишется?"
- "Это производитель, дилер, продукт, платформа или стандарт?"
- "Это актуальный игрок сейчас или историческое название?"
- "Это юридическое лицо, бренд или локальное прозвище?"

Injected questions must show their source:

```yaml
injected_question:
  source_signal: ""
  source_bpm: "BPM-2|BPM-3|BPM-4|BPM-5|BPM-6|BPM-7A|BPM-7B|BPM-8|BPM-9|BPM-10|BPM-11"
  question: ""
  why: ""
  return_to:
    - "BPM-SI"
    - "Storyline-Storyboard"
    - "client_reality_reconciliation_gate"
```

## Vault Analog Search

Search tagged and untagged evidence. Do not rely on one tag only.

Strong coordinates:

- `#роль/*`, `#респондент/*`, должность in frontmatter/body;
- `#отрасль/*`, `#товарная-категория/*`, `#ценовой-сегмент/*`;
- `#проблематика/*`, `#ситуация/*`, `#ключевой-вопрос/*`, `#ответ/*`;
- `#тип-проекта/*`, `#BPM/*`, `#инструмент/*`, `#модель/*`;
- `#статус-проекта/завершён`, `#статус-материала/завершён`, `#статус-материала/опубликован`;
- folders: `Проекты`, `Кейсы реализованных проектов`, `Встречи`, `Интервью`, `Анализ`, `Продукты`, `Лонгриды`.

Use both:

- tag search: exact tags and category searches;
- text search: role names, sector words, problem phrases, artifact names, project names.

Prefer evidence in this order:

1. Processed project analysis and administrative-scale files.
2. Finished project cards and realized cases.
3. Processed interview extracts.
4. Published or final content.
5. Raw transcripts only when no processed source exists.

## Archive Analog Scoring

When archive analogs are used, rank them explicitly. Do not use a project as an analog only because one tag matches.

```yaml
archive_analog_match:
  analog_project: ""
  similarity_score: 0.0
  similarity_breakdown:
    project_archetype: 0.0
    SCQA_or_problem: 0.0
    industry_or_business_model: 0.0
    BPM_scope: 0.0
    respondent_role: 0.0
    stage: 0.0
  match_threshold: 0.75
  reusable_questions: []
  known_failure_modes: []
  confidence: "high|medium|low"
```

Default retrieval: top-3 to top-5 with diversity. If several analogs are nearly identical, use the strongest one and mention the rest as supporting, not as separate question sources. If the score is below threshold, keep the analog as `watch` or `no_op`, not as a question driver.

## Similarity Scoring

Rank analogs by usefulness, not by textual similarity alone.

Default weights:

| Coordinate | Weight |
|---|---:|
| Same respondent role / decision level | 3 |
| Same sector or business model | 3 |
| Same problem / SCQA complication | 4 |
| Same project type / BPM / intervention type | 2 |
| Same stage of work | 2 |
| Completed or published source | 2 |
| Same company/project only by name | 1 |

Rules:

- Do not use sector-only overlap as enough evidence.
- Require either one very strong match (problem + role) or two medium matches.
- Prefer 3-7 high-quality analogs over a long list.
- If analogs conflict, surface the conflict as an interview hypothesis.
- If the current project has an administrative scale, use analogs to sharpen it, not replace it.

## Open-World Context

Use external research when:

- the sector is underrepresented in Vault;
- the role is specialized;
- market/regulation/product context may have changed;
- the interview depends on current facts, public company context, benchmarks, or recent events.

When using external research:

1. Browse current primary or high-quality sources.
2. Cite links in the answer.
3. Separate external facts from Vault evidence.
4. Convert external facts into interview probes, not generic background.
5. Do not let open-world context override direct project evidence unless there is a clear reason.

Avoid broad market summaries unless they change the questions.

## Output: Project Interview

Use this structure:

1. **BLUF:** what this interview must clarify.
2. **What we already know:** 3-5 bullets from current project context.
3. **Analog signals from Vault:** 3-7 analogs with why they matter.
4. **External context:** only if used; cite sources.
5. **Hypotheses to test:** 5-7 pointed hypotheses.
6. **Question blocks:** 12-18 questions grouped by logic, not by abstract theme.
7. **Probing questions:** follow-ups that reveal mechanics, tradeoffs, and exceptions.
8. **Risks / traps:** questions likely to produce generic answers and better replacements.
9. **Evidence links:** Vault links and source links.

Project question blocks usually include:

- role and decision rights;
- current process and actual practice;
- bottlenecks and workarounds;
- economics / metrics / data;
- conflicts between functions;
- implementation constraints;
- success criteria.

## Output: Content Interview

Use this structure:

1. **BLUF:** what story, thesis, or proof the interview must unlock.
2. **Likely angle:** article/case/content hypothesis.
3. **Analog signals from Vault:** past cases, published pieces, recurring problems.
4. **External context:** only if it sharpens the angle; cite sources.
5. **Narrative hypotheses:** 3-5 possible angles.
6. **Question blocks:** 10-15 questions.
7. **Scene/case probes:** questions that elicit concrete episodes, numbers, tensions, before/after.
8. **Quote zones:** where to ask for vivid language, client phrasing, objections.
9. **Evidence links:** Vault links and source links.

Content questions must extract:

- concrete scenes;
- numbers and constraints;
- before/after contrast;
- decision moments;
- objections and failed alternatives;
- language the audience actually uses.

## Output Discipline

Keep the brief usable in a live conversation:

- Start with the conclusion.
- Put the best questions first.
- Avoid generic consultant prompts.
- Mark source type: `Vault`, `external`, `inference`.
- Use Russian professional language.
- Do not explain Vault, wikilinks, SCQA, MECE, or administrative scale to Ilya.
- If evidence is thin, say so and give a thinner brief with clear unknowns.

## Common Mistakes

- Asking only from the administrative scale and ignoring past analogs.
- Treating same sector as same problem.
- Mixing project discovery questions with content-harvesting questions without separating intent.
- Using raw transcripts before processed analysis.
- Adding open-world research as decoration instead of turning it into probes.
- Hiding uncertainty about inferred role, sector, or stage.

## Writeback / Approval Gate

This skill is risky when interview briefs use client/project analogs, transcripts, external sources, or inferred sensitive context that may affect a meeting, proposal, research memo, or client-facing plan.

Default output is an internal interview brief. Do not write the brief into Vault, update project/client cards, send externally, turn inferred analogs into canon, or create tasks/questions as accepted commitments without Ilya's explicit approval. Mark `Vault`, `external`, and `inference` separately.

Exception: in an Old Delivery Rail/BPM project, Ilya has granted standing permission for internal evidence-set files. When Ilya names an appointed / upcoming respondent, or Rail asks `к кому готовим следующее интервью?` and receives the respondent, this skill may write the internal question brief to `Interview briefs.md` or an equivalent existing project interview-prep file in the project folder, as part of the Old Delivery evidence-set. Rail and this skill must not appoint interviewees or manage the interview queue autonomously. This does not permit external sending, canonization of hypotheses, task creation, or client-facing use without separate approval. If Ilya says `только в чате`, `без файлов`, `симуляция без записи`, or the project folder is not found, do not write and record the sync gap.

## Externalization / DLP Gate

Interview briefs may contain sensitive analogs, client/project facts, inferred roles, sector assumptions, and private interview context. Before sending externally or using with a client, sanitize the packet and confirm with Ilya.

Do not reveal source clients, raw transcript details, private analogs, personal data, internal doubts, or unapproved hypotheses. Convert sensitive analogs into generalized probes unless explicit disclosure is approved.

## Structured Analytical Artifact Gate

When a brief is organized as an Issue Tree or Hypothesis Tree, or when it updates a Problem Map/evidence trace/storyline gap, apply the global contract in `~/.codex/AGENTS.md`. Every hypothesis probe must name mechanism, expected signal, source/answer sought, falsifier, and decision affected. Analog methodology and Frappe do not count as respondent evidence. Interview questions may test a problem node or claim, but they do not confirm it until the physical interview source is processed.
