---
name: cognitive-router
description: >-
  Use when Ilya's request is mixed, expensive, strategic, project-related, or
  could trigger premature writing: "давай подумаем", "пойми", "найди",
  "собери язык", "зафиксируй", "запомни", "внедри", "прогони через
  когнитивный роутер", "не потерять", "для клиента", "визуализируй",
  "какие операции". Classify the request into THINK, SCAN, CANON, REVIEW,
  MAKE, WRITE, RUN, MEMORY, TASK, MEDITATE, REPLICATE, PROCESS, VISUAL, CLIENT, or
  EXTERNAL-CONTEXT; choose the next allowed route and the best next skill;
  decide whether to stop, ask, or delegate; prevent premature Vault writes;
  and produce a concise operational brief, project closeout, or next-step gate.
---

# Cognitive Router

Use this skill to turn a live, layered request into the next correct cognitive operation. The goal is to separate thinking, scanning, canon-building, artifact-making, writing, and execution so Codex does not search, write, or build too early.

## Quick Protocol

1. Classify the user's current message by operation class.
2. If the request is mixed, identify the route between classes, not only the first class.
3. Apply the relevant gate before moving to the next class.
4. Execute only the next allowed step.
5. In expensive, broad, project, or write-risk tasks, show a short brief before acting.
6. If the user says "пока обсуждаем", "беседуй в чате", or equivalent, do not write files.
7. If the user says "запиши", "зафиксируй", "обнови", "внедри", or equivalent, classify the artifact first, then write to the right contour.
8. After routing, choose a post-route action mode: `route-only`, `route+ask`, or `route+delegate`.

## Operation Classes

| Class | Meaning | Triggers | Allowed | Forbidden | Output |
|---|---|---|---|---|---|
| THINK | Develop thinking | "давай подумаем", "обсуди", "пока рассуждаем" | hypotheses, distinctions, strong questions | writing to Vault, fixing rules | hypotheses, tensions, options |
| SCAN | Diagnose and search | "пойми", "изучи", "найди", "где лежит" | read sources by circles, map structure | immediate rewrites | findings, locations, links |
| CANON | Ontologize language | "собери язык", "синтаксис", "канон", "правила" | types, relations, prohibitions, examples | implementation without acceptance | language/rule specification |
| REVIEW | Review or repair | "это не то", "вернись к логике", "замечания" | parse keep/remove/replace/consequence | defending the old version | correction list |
| MAKE | Build artifact | "собери карту", "дай бриф", "таблицей", "сделай КП" | choose template and assemble result | long methodology without need | draft or artifact |
| WRITE | Institutionalize | "запомни", "в rules", "зафиксируй", "как скилл" | route and write to the proper contour | writing everywhere at once | path and changes |
| RUN | Execute | "внедри", "погнали", "всё выполняется" | execute accepted plan and verify | re-architecting | changes plus verification |
| MEMORY | Operational memory | "не потерять", "в Daily", "статус проекта" | capture in Daily/project/INBOX | leaving only in chat | short routed note |
| TASK | Executable task routing | "задачи", "заведи задачу", "что в трекер", "ускорь проект", "owner next action" | produce candidate/task_delta and route to the active project tracker; for РГ1 use bundled Google Spreadsheet РГ1 ingest with `PP/Codex ingest` reconciliation mark | using TaskOS as the primary task home; routing РГ1 tasks through Airtable bridge | task_delta candidates and sync route |
| MEDITATE | Extract rules | "/meditate", "проведи meditate" | process reflection and rule candidates | content summary as a substitute | active/staged/rejected |
| REPLICATE | Reproduce system | "на другой машине", "перенести", "воспроизвести" | bootstrap, dependencies, instructions | undocumented local hacks | reproduction package |
| PROCESS | Process engineering | "автоматизации", "хуки", "процесс", "операции" | split rule/hook/automation/skill | making everything a rule | decision table |
| VISUAL | Visual modeling | "визуализируй", "mermaid", "картинка" | readable diagram and viewing notes | unreadable wall of text | diagram |
| PRESENTATION | Paper Planes deck production | "презентация", "дека", "слайды", "слайдумент", "HTML-прототип", "PP Pages", "PPTX", "PowerPoint", КП со слайдами | mandatory PP Presentation Kit preflight -> production MD -> domain subskill -> critics -> presentation QA -> export | direct HTML/PPTX, partial kit, specialist bypass | kit receipt + artifact status |
| CLIENT | Client packaging | "для клиента", "КП", "отправить" | client-facing language | leaking internal draft terms | polished client text |
| EXTERNAL-CONTEXT | External enrichment | "рынок", "конкуренты", "свежие данные", "best practices" | bring sourced outside context | replacing internal Vault without reason | integrated external package |

## BPM Metaoperations

For project and BPM requests, also choose one metaoperation:

| Code | Metaoperation | Thinking type | Typical route |
|---|---|---|---|
| OP-A | Sense fixation | frame, scope, goal, constraints | THINK / SCAN -> SENSEMAKE -> CANON |
| OP-B | Information gathering | facts vs opinions | SCAN -> MAKE |
| OP-C | Structuring | raw material into form | SCAN -> MAKE |
| OP-D | Logical conclusions | traceable conclusions from data | SENSEMAKE -> CANON/MAKE |
| OP-E | Project assembly | integrated project artifact | MAKE -> REVIEW -> MAKE |
| OP-F | Management decision | choose direction and reasons | REVIEW / CANON -> MAKE |

If the metaoperation is unclear, first make a sense pass: are we framing, collecting, structuring, concluding, assembling, or deciding?

## Gates

- THINK -> CANON only after stable distinctions appear.
- CANON -> MAKE only when the output format is clear.
- MAKE -> WRITE only after explicit "запиши", "фиксируй", "внедри", or equivalent.
- WRITE -> RUN only when there is a repeatable scenario and verification.
- SCAN -> MAKE only after enough sources are found or a source limit is explicit.
- SCAN/CANON -> EXTERNAL-CONTEXT when internal facts are insufficient or the answer depends on current market, competitors, public cases, or external methodology.
- EXTERNAL-CONTEXT -> CANON/MAKE only after saying what the outside context confirms, changes, weakens, or adds to the internal map.
- TASK -> WRITE/RUN through the active project tracker. For РГ1 projects: bundle related task_delta into compact management packages and write / prepare them for Google Spreadsheet РГ1 with `PP/Codex ingest / needs RG1 reconciliation`; do not route РГ1 tasks through Airtable bridge. For non-РГ1 projects, use the project-specific task route if defined. Do not route new executable tasks to TaskOS as the primary home.

## Post-route Action Modes

`cognitive-router` should keep helping with the logic of the work after classification. It is not limited to a static route card. Its job is to decide the next safest and most useful move.

Use one of three modes:

| Mode | When to use | What router does | Stop-point |
|---|---|---|---|
| `route-only` | request is broad, high-risk, external, governance-related, or user is still discussing | outputs route card, likely next skill(s), write/external risk, and stop-point | stops after route card |
| `route+ask` | intent is plausible but missing data, durable-write risk, sensitive context, or ambiguous target exists | asks the smallest necessary question and names what depends on the answer | stops after question |
| `route+delegate` | intent is clear, risk is low or already approved, and a specific skill should do the work | names the primary skill, supporting skills if useful, and then continues with that skill's workflow | stops at that skill's own gate |

Router may recommend skill chains, for example:

- `summary -> tunnel` when a chat summary produces knowledge candidates;
- `client-info -> commercial-proposal-generator -> multi-perspective-review` for a serious КП path;
- `deepresearch -> local return packet -> skill-eval-harness` for external review of the skill system;
- `rail -> cordos` when project drift reveals task candidates;
- `admin -> cordos` when project acceleration tasks should become Task Inbox candidates;
- `skill-system-governance -> skill-eval-harness` when skill patches need regression coverage;
- `trails-generator -> expert-article-writer -> multi-perspective-review -> text-deai-editor` for content rail work.

Router must not perform another skill's core work by itself. It should not write a КП, run deep research, mutate Vault, create tasks, or rewrite rules just because it identified the route. It can execute the next step only when the action mode is `route+delegate` and the selected skill's own gates allow it.

Default examples:

```yaml
route_only:
  route: "EXTERNAL-CONTEXT -> REVIEW"
  next_skill: "deepresearch"
  write_risk: "medium"
  stop_point: "prepare sanitized outbound packet; approval before sending sensitive context"

route_ask:
  route: "CANON -> WRITE"
  next_skill: "ingest"
  write_risk: "high"
  question: "Писать в Vault сейчас или подготовить candidate/preview?"

route_delegate:
  route: "SUMMARY"
  next_skill: "summary"
  write_risk: "none"
  action: "run summary now; no durable write"
```

## Common Routes

| Route | Use when | Guardrail |
|---|---|---|
| THINK -> CANON | a new language is emerging from discussion | do not write the raw sketch |
| THINK -> CANON -> MAKE | hypotheses, frameworks, maps | stabilize language before artifact |
| SCAN -> MAKE | find facts and assemble a brief/table/map | limit source expansion |
| SCAN -> CANON | study Vault/system structure | extract patterns, not only summary |
| SCAN -> SENSEMAKE -> CANON/MAKE | documents/interviews/screens need sensemaking | reality-map-first |
| SCAN/CANON -> EXTERNAL-CONTEXT -> CANON/MAKE | internal context needs market/methodology benchmark | integrate, do not dump sources |
| REVIEW -> CANON | critique reveals a language flaw | parse review into keep/remove/replace |
| CANON -> WRITE | "запомним как скилл/rule" | route artifact before writing |
| MAKE -> REVIEW -> MAKE | iterative artifact revision | change only affected nodes |
| MAKE -> CLIENT | internal draft becomes client text | client-language gate |
| MEMORY -> RUN | "не потерять" becomes action | capture before execution |
| TASK -> CORDOS/ADMIN | executable work, owner-next-action, tracker delta, acceleration task | active tracker first; for РГ1, bundled Google Spreadsheet ingest with reconciliation mark |
| PROCESS -> WRITE -> RUN | rules/hooks/automation design | split rule/hook/automation/skill |
| MEDITATE -> WRITE | process reflection creates rules | fact -> damage -> cause -> countermeasure |

## Reuse / Method-Derivative Routing

When a project request touches donors, reuse, BPM-to-BPM transfer, consumer clustering, dashboard representation, SI variability, or method derivatives, route it as `PROCESS -> SCAN -> REVIEW` or `Rail / BPM Exchange`, not as a normal scope refresh.

First build a family query from the project signal, even when nobody names a concrete donor. Then route to curated source homes before broad search. If the user, a teammate, or a project source names a concrete donor candidate, alias, acronym, old project name, or source nickname, route immediately to exact-name source-check as an additional step. A named donor such as `Окское Подворье / СПСЖ` is not just a hint; it is evidence that the family/source or alias expansion may have failed.

Run a reuse / method-derivative pass only on:

- explicit Ilya request;
- Rail / BPM Exchange run;
- pre-defense or client-defense preparation;
- 3-4 significant ingests with at least one `BPM-1`, `BPM-2`, or `BPM-3` signal;
- major BPM source completion;
- project gate change.

Do not trigger it from every subpassport/scope update, ordinary task status, or minor administrative edit. If the evidence is weak, return `weak_evidence` and do not surface a reuse proposal. If reuse is confirmed, stop proposing the same BPM/theme route. If rejected, preserve the reason and retry conditions. If the observer says methodological innovation is not needed, mark `not_needed` until gate change, substantial new data, or explicit review.

Before returning `no strong donor` or a top-K donor list, require `family/source expansion`: family terms, business model, channel, analysis object, anti-patterns, 8ka knowledge units, 5ka tunnel batches, 2ka cases, 4ka archive passports, 1ka training units, and source PDF names. If a human later names a missed donor, classify the defect as `missed_family_source_expansion` or `missed_alias_source_expansion` and patch the route.

Short routing verdict:

```yaml
reuse_router:
  trigger: explicit | rail | pre_defense | ingest_packet | major_bpm_source | gate_change | none
  named_donor_present: yes | no
  family_source_expansion_done: yes | no
  alias_source_expansion_done: yes | no
  should_run: yes | no
  reason:
  reuse_state: open | confirmed | rejected | weak_evidence | not_needed | not_applicable
  miss_cause: missed_family_source_expansion | missed_alias_source_expansion | semantic_query_too_broad | semantic_query_too_narrow | source_unavailable | none
  next_skill: rail | bpm-exchange-reconciliation | admin | none
```

## SENSEMAKE Mode

Use `SENSEMAKE` inside `SCAN -> CANON` and `SCAN -> MAKE` when Ilya brings facts not for summary, but to improve the working map of reality.

Triggers:
- "пойми, что в документах"
- "проведи те же операции"
- "как это связано с интервью / ПВЦЗ / проектом"
- "что это меняет"
- "покажи управленческий смысл"
- uploaded client files, screenshots, interviews, or data without a direct artifact command

Rules:
- Discuss in chat first.
- Extract management meaning instead of retelling the source.
- Stitch layers: document -> interview -> PVTsZ/project logic -> possible action.
- Name the divergence type: strategic, financial, operational, terminological, organizational.
- Expand internal terms when they become reasoning anchors.
- If a strong phrase is selected or repeated, develop it as a model.
- Write to Vault, PVTsZ, deck, or canon only after explicit WRITE signal.

Short verdict format:

```text
router_class:
route:
primary_mode:
post_route_action:
next_skill:
supporting_skills:
метаоперация BPM:
что делаю сейчас:
что не делаю сейчас:
пишу в Vault:
стоп:
```

## Brief Formats

For expensive, broad, mixed, or write-risk requests, show:

```text
Понял так:
классы:
route:
primary_mode:
post_route_action:
next_skill:
supporting_skills:
источники:
результат:
пишу в Vault:
стоп:
```

For project work, use:

```text
Понял так:
проект / контур:
входной симптом или задача:
router class:
route:
primary mode:
post_route_action:
next_skill:
supporting_skills:
метаоперация BPM:
что делаю сейчас:
что не делаю сейчас:
ожидаемый артефакт:
пишу в Vault:
```

## Project Closeout

After a meaningful project step, end with a compact operational block when useful:

```text
Сдвиг:
Фаза / подфаза:
Оценка траектории:
Next step:
Что пока рано:
Сигнал перехода:
Knowledge check:
Knowledge / learning signal:
```

Use `Knowledge / learning signal` to route reusable insights to the knowledge factory, quality/process contour, learning contour, content contour, or back to the project.

## Phase Awareness

Track the phase of joint thinking:

| Phase | What happens | Next move |
|---|---|---|
| Socratic | distinguish terms, tensions, options | THINK -> CANON |
| Engineering | language becomes schema, skill, rule, map, process, template | CANON -> MAKE/WRITE |
| Production | search, assemble, update, verify, integrate | SCAN/MAKE/WRITE/RUN |
| Reflective | system studies failures, repeats, strong moves | REVIEW/MEDITATE -> WRITE |

Signals:
- stable language appears: propose canon, do not write without acceptance;
- three or more edits hit one artifact: collect deltas and patch affected logic;
- long discussion but applied task: offer a minimal example/map/table;
- "не потерять" or "в Daily": route to MEMORY;
- repeated failure three times: propose MEDITATE/rule candidate;
- market/competitor/current-methodology question: use EXTERNAL-CONTEXT;
- repeatable working move appears: propose skill/rule/template after acceptance.

## New Delivery Checks

For `New Delivery` projects, keep a hidden diagnostic layer:

- cadence map: daily, weekly, monthly, quarterly, annual/strategic;
- role map: curator, architect, implementer, trainer, temporary functional substitution;
- internal owner per active track;
- transfer/de-escalation signs;
- project -> tracks -> track-months;
- track statuses: active, paused, completed, cancelled, reframed, new;
- subtracks, weekly mechanics, and client-result vs methodology-harvest split.

If a layer is missing, diagnose the defect as `ingest-gap`, `description-gap`, or `management-gap`.

## Project State Reconcile

For a hot project, answer six questions:

1. Did new facts appear from Notion, Vault, or chat?
2. Do they change any BPM hypothesis?
3. Do they change any BPA block or slide intent?
4. Do they change next step, stage gate, or assembly type?
5. Do they require updating project card, admin scale, plan, or Daily?
6. Is this local or a reusable pattern / knowledge-check candidate?

If all six are "no", do not deeply rebuild the project that day.

## Operating Rule

The main rule: classify the expensive request by route between operations, then perform only the next allowed step.

## Writeback / Approval Gate

This skill is high-risk because it can route the work toward durable writes, rule changes, task creation, external context, or canonical decisions.

Before any durable action, stop and confirm with Ilya unless he gave explicit same-turn permission for that exact action. Durable actions include: creating or editing Vault files, changing frontmatter/status fields, updating registries, registering task deltas in Codex Project Task Inbox, changing rules or skills, importing sources into Reader/Readwise, sending or preparing external-facing text as final, and canonizing external-model output.

If the route is ambiguous, output a route card and ask for confirmation. Do not treat route selection as permission to execute the write.
