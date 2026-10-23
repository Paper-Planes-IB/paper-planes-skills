---
name: ingest
description: "Use when Ilya asks to ingest, add, remember, route, classify, or place new material into the Vault / knowledge system. Handles intake, classification, routing, proposal, no-op, and writeback-after-approval for facts, hypotheses, rules, external research, content candidates, tasks, commercial facts, contradictions, and source packets."
metadata:
  version: "0.3.11"
  status: active
  line: Vault ingest / knowledge routing
  owner: Ilya
  originator: Илья Балахнин
  supports_bpm:
    primary: [ingest]
    required_secondary: [BPM-2, BPM-4, BPM-6, BPM-7A, BPM-7B, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-3, BPM-5, BPM-8, BPM-9]
  can_consume: [new source packets, external research returns, NotebookLM outputs, commercial facts, task signals, project artifacts]
  can_produce: [intake classification, route proposal, no-op reason, writeback proposal, task_delta packet, source-check queue item, post-mining Rail handoff]
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-08-29: Made Озеро BPM — SI — Slides — BPV a P0 freshness-controlled writeback target: bounded upstream changes must update the lake or record a no-op within 24 hours; one existing automation maintains the contour without promoting route maps or decks to accepted BPV."
      - "2026-08-28: Added interview-corpus statistics deduplication: count unique respondent/role interview events rather than files and report organizations, primary transcripts, derived duplicates, and excluded non-client sources separately."
      - "2026-08-03: Added post-upload uniqueness check for client source batches: relist the target folder, verify one intended file per name/size, and remove only connector-created exact duplicates before publishing links."
      - "2026-08-03: Added recalculated-report version-coherence guard: compare new and prior text plus rendered tables/charts, assign primary rights claim-by-claim, and never let stale captions or unchanged narrative inherit the recalculated status of nearby visuals."
      - "2026-08-03: Added compound-validity guard: a cross-tab or analytical intersection inherits the weakest evidence rights of its axes, join keys, grain compatibility, and denominator; visual persuasiveness cannot upgrade source rights."
      - "2026-07-25: Added Granola shared-link recovery: if connector lookup cannot find a shared note, try the public URL / redirected document page and parse readable Next/HTML content before declaring a source gap."
      - "2026-07-12: Hardened unified Ingest/Rail to 0.3.03: Gate 2 must visibly cover every active P-node and every evidence-supported relevant actant; compressed macro views cannot replace the full/faceted master map."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.3.02: post-mining handoff is run-to-blocker; a passed gate cannot return with the next gate merely pending, and nonblocking gaps/open forks/provisional scores do not stop execution."
      - "2026-07-11: Promoted unified Ingest/Rail to 0.3.01: mining-complete signals stop ordinary ingest and hand off to Rail post-mining transition for source closure, problem consolidation, Cynefin recheck, Estuarine mapping/visualization, action/SI/BPV routing, and BPA readiness."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.08: BPP event, BPM-SI synthesis, BPM Exchange/reuse, reference gap, and market no-op are standalone source-class contracts as well as mixed-contract participants."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.07 with mixed_contract_ingest contract for heterogeneous passes combining BPP events, BPM-SI synthesis, BPM Exchange/reuse, reference gaps, and market no-ops."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.06 with single-source follow-up contract for financial/follow-up/dedup ingests after the second source: exact schemas, source-rights, request audit, no collapsed nodes, writeback paths, and allowed verdicts."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.05 with recovery_plus_new_batch contract: recovered and new sources must be separated, recovery-rights delta must be audited, mandatory analytical layers cannot be skipped, and strategic fork findings do not substitute for Rail tables."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.04 with exact-schema gate for batch ingest: table presence is not pass, required columns are enumerated, forbidden verdict aliases are blocked, and source gaps must use allowed batch verdicts."
      - "2026-07-11: Hardened unified Ingest/Rail to 0.2.03 with batch regression guards: mandatory per-source rights table, decomposed BPM labels, no collapsed no-signal rows, exact macro/actant/action/question schemas, batch synthesis table, writeback paths, and no generic passed verdict."
      - "2026-07-11: Promoted unified Ingest/Rail to 0.2.02 with batch_interview_ingest contract: per-source rights, source isolation, batch synthesis rights, and delta-only/cumulative coverage separation."
      - "2026-07-11: Promoted Ingest/Rail handling to unified 0.2.01: preserves 0.1.x guardrails and adds tabular-source ingest class for Excel/XLS/XLSX/CSV/table exports; external references are conditional and question audit is replaced by tabular audit when applicable."
      - "2026-07-11: Mirrored Rail 0.1.20 pseudo-ledger, delta-table, source-register, question-audit, and writeback guards."
      - "2026-07-11: Added Old Delivery node-by-node coverage ledger guard from Rail 0.1.19."
      - "2026-07-11: Added Old Delivery pre-final self-audit blocker mirroring Rail 0.1.18."
      - "2026-07-11: Added Old Delivery question coverage audit and stricter coverage-complete guards for SI/BPV evidence gaps."
      - "2026-07-11: Added Old Delivery interview prep tracker and appointed-interview brief writeback exception; Rail must not appoint interviewees."
      - "2026-07-11: Added mandatory Old Delivery coverage check and SI/BPV trace table requirements."
      - "2026-07-11: Clarified that the Old Delivery 9-action matrix is cumulative across all active problem nodes, not latest-ingest-only."
      - "2026-07-11: Recorded Ilya's official standing permission to create Old Delivery evidence document-set files and required code+name in actant problem roles."
      - "2026-07-11: Added Old Delivery regression guards for BPM scope ledger, problem-node names/status history, actant type validation, concrete action cells, and concrete donor reuse-check."
      - "2026-07-11: Clarified that Old Delivery dry-runs create/update evidence documents unless explicitly run chat-only."
      - "2026-07-11: Added Old Delivery macro-idea evidence map, polymorphic actant map, and 9-action matrix requirements."
      - "2026-07-11: Added mandatory Old Delivery project document set creation/update for BPM evidence corpus."
      - "2026-07-11: Added BPM-addressed multi-source evidence trace requirement for every new BPM ingest and downstream triage outputs."
      - "2026-07-11: Added Old Delivery project-chat auto-trigger for BPM ingest triage; New Delivery explicitly excluded."
      - "2026-07-11: Added mandatory BPM ingest triage chain: problem -> Cynefin -> actants -> action -> SI/slide-intent -> BPV-route."
      - "2026-05-26: Added BPM Exchange capability metadata."
---

# Ingest

## Постоянный синтез DP03 / DP04 — 23.10.2026

При пополнении аналитического корпуса прочитать полный раздел «Постоянный синтез и пополнение DP03 / DP04 — стандарт 23.10.2026» в `<PP>/Vault/10-отделы/05-качество-БП/Бизнес-процессы/04-производство/_Архитектура-проектов.md`. Он уточняет прежние упоминания совмещённого файла и действует в пределах scope/прав текущей задачи.

Единица изменения — утверждение в реестре выводов DM.03, не номер страницы. Отдельный файл матрицы для новых записей не создавать: анализ и трассировка находятся в одном досье; старые проекты мигрировать только по отдельному разрешению. Проверить качество материала, пересмотреть утверждение, оценить влияние на DP03/DP04 и детализацию DM.02 в программе DP01. Различать состояние знания, готовность страницы и согласование версии; учитывать неожиданные вопросы и обоснованное отсутствие влияния. Противоречие записывать сразу; существенный пересмотр ответа/согласованной версии — после разбора ролью DP01. Списки гипотез и заголовков получать из существующих записей, не создавать параллельные журналы. Ритм задаёт DP01; процент переписанных заголовков не является критерием качества. Полный шаблон изменения и приёмка передачи — в указанном разделе.

## Purpose

`ingest` is the controlled entrypoint for new material entering the Vault / knowledge system.

It does not mean "write everything somewhere." A successful ingest may end as:

- a writeback proposal;
- a no-op with reason;
- a source-check queue item;
- a task-route candidate;
- a content-route candidate;
- a project/context preflight;
- an approved writeback to an existing file.

Default posture: classify and route before writing. Do not create new files unless Ilya explicitly asked for a file / document / artifact. Exception: Ilya has officially granted standing permission to create the mandatory Old Delivery BPM/Rail evidence document set in the existing project folder.

Terminology guard: the canonical name for the BPM-to-SI route is `BPM-SI` in Latin script. `BPM-SI lake`, `BPM-SI contour`, and Russian explanatory synonyms `BPM-SI озеро` / `BPM-SI контур` are allowed only as contextual synonyms. Do not make the Cyrillic `БПМ-СИ` spelling the primary form, and do not use or reproduce fused miss-heard forms such as `BPMSA` / `БПМСА`.

## BPM-SI Lake Freshness Contract

`Озеро BPM — SI — Slides — BPV.md` in the existing BPA / Ассемблинг contour is a P0 reference index for project lineage, reusable ideas and reverse search from BPV to source evidence. It is not an optional tagging layer.

When a material ingest changes any bounded upstream — project BPM source register, `BPM Storyline-Storyboard`, `BPV route map`, slide/deck artifact, BPA.09 defense or client-decision record, `Матрица BPM — SI`, or canonical BPV registry — the same pass must update the existing lake or add an explicit dated no-op reason. Maximum permitted lag is 24 hours. If the lake is older than the newest bounded upstream by more than 24 hours, mark `freshness breach`, name the newest upstream and perform all available writeback before presenting the lake as current.

The lake writeback must preserve evidence rights. Storyline presence, route-map presence, file mtime, HTML/PDF/PPTX, pre-defense or shown deck do not prove accepted BPV. A complete route requires BPM evidence, SI, slide/deck identity, defense, recorded client decision, approved priority project and canonical BPV. Otherwise retain `partial_upstream`, `partial_downstream`, `donor-only`, `missing`, `contradicted` or `no-op` with a Russian explanation.

Maintain one existing automation for this contour. Prefer updating and reactivating it over creating a duplicate. Every automated run checks physical links, full-reconciliation date, unique receiver/storyline counts, BPV route-map inventory and reverse lineage `BPV -> client decision -> deck -> SI -> BPM`.

## When To Use

Use this skill when Ilya says or implies:

- `ingest`;
- `добавь в Vault`;
- `проглоти`;
- `заинжесть`;
- `запомни`;
- `добавь в знание`;
- `сохрани в правила`;
- `занеси`;
- brings new material that should enter a durable knowledge, project, content, task, rule, or commercial trace.

## Source Preflight

Before classification, check the relevant existing roots / registries when available:

- `ПКМ/01-устав.md`;
- `Vault/__Глоссарий.md`;
- `Vault/__Персоналии.md`;
- `Vault/__Проекты.md`;
- `Vault/__География.md`;
- `Vault/__Теги.md`;
- project chat maps, trackers, passports, README files, and local `AGENTS.md` when the input looks project-bound;
- existing content backlogs / weekly-docs when the input is content-like;
- existing commercial trace / task inbox when the input is commercial or task-like.

If a registry cannot be found, say that explicitly and continue as `partial_context`, not as certainty.

When assigning a new project source ID, do not rely only on the primary source register. First run a bounded project-local check for the candidate ID and nearby IDs across the existing project card, source register, evidence trace, Storyline-Storyboard, BPV route map, BPM scope ledger, task tracker, and other known source-bearing ledgers. If any downstream artifact already uses the candidate ID for a different physical source, preserve that existing ID and assign the next free source ID to the new source. Record the correction briefly in the working update if a conflict was found.

Уточнение 03.10.2026: ту же проверку выполнять для идентификаторов утверждений и замыслов слайдов, повторно непосредственно перед записью и после неё. Первоначальный свободный номер не гарантирует уникальность при параллельной правке проектного корпуса. При обнаружении пересечения перенумеровывать только строки своего текущего прохода и все их ссылки; соседние изменения сохранять. Проверять уникальность по точным строкам определений, а не по числу упоминаний идентификатора в тексте.

## BPM Ingest Triage

When new material is an official BPM input, BPM-candidate source, or can feed any BPM, every ingest must run the BPM downstream triage chain before finalizing. Material includes links, databases, exports, conclusions, voice notes, transcripts, meetings, external research returns, CRM signals, dashboard insights, reuse packets, files, or any explicit BPM-candidate source:

In 4ka project chats identified as `Old Delivery`, this triage is automatic for short rail commands (`тащи по рельсе`, `протащи по рельсе`, `по рельсе`, `запусти рельсу`) and for any explicit BPM ingest. Do not require a long starter prompt from Ilya. `New Delivery` is explicitly excluded from this default: do not reuse Old Delivery triage as New Delivery logic unless Ilya separately defines that logic.

```text
source / BPM ingest
-> problem_node / ПЦВЗ / SCQA
-> causal_regime_hint / Cynefin domain
-> Estuarine actants
-> possible actant_action_class
-> SI_candidate / САИ / slide-intent
-> movement_suggestion / initiative hypothesis
-> BPV / sub-BPV / derivative / gate route
```

This triage always runs. It does not mean every ingest must produce every downstream artifact. If a layer has no signal, record an explicit no-op: `no problem signal`, `domain unchanged`, `no actant signal`, `no action signal`, `no SI / slide-intent signal`, `no BPV-route signal`.

If the material jumps directly to actants without a problem and Cynefin domain, mark `problem_map_missing / causal_regime_missing`. If an action is not linked to `SI / САИ / slide-intent`, mark `SI_slide_intent_missing`. If a BPV route appears before the chain, mark `premature_BPV_route`.

When the ingest is a second or subsequent interview / BPM source for the same project, add a multi-source evidence trace. Do not let downstream sections hide whether a point comes from one interview, several interviews, another BPM source, contradiction, or agent inference. For every `problem_node`, `Cynefin domain`, `actant`, `action`, `SI / slide-intent`, `initiative`, and `BPV / sub-BPV route`, record:

| field | value |
|---|---|
| `bpm_source_id` | canonical source label such as `BPM-2 / интервью Речкалова`, `BPM-4 / расчёт экономики`, `BPM-10 / CRM-срез` |
| `source_trace` | BPM-addressed source IDs / respondent-date labels supporting the point |
| `cross_source_status` | `single-source / confirmed / extended / contradicted / refined / inferred / needs_source_check` |
| `derived_from` | upstream node IDs when the item is synthesized rather than directly stated |
| `confidence` | `low / medium / high` |
| `next_evidence_need` | what should be checked next if not confirmed |

Every new ingest of any BPM must be reconciled with the accumulated evidence corpus for the project. A new `BPM-4`, `BPM-6`, `BPM-8`, or `BPM-10` source may confirm, weaken, contradict, refine, or reclassify nodes first raised in `BPM-2` interviews; record that explicitly instead of treating each BPM stream as isolated.

For `Old Delivery` projects, this accumulated corpus must be written into a project document set, not only kept in the chat answer. Ilya has officially granted direct standing permission for this class of files: if the existing project folder is known and no equivalent document exists, create the minimal missing file(s); otherwise update the existing files. Do not cite the generic no-new-files rule as a reason to skip this document set.

Required Old Delivery document set:

| document | purpose |
|---|---|
| `Реестр BPM-источников.md` | every BPM-addressed ingest with respondent/object/date/status |
| `BPM scope ledger` | explicit included / excluded / deferred / recommended BPM scope |
| `Карта проблем и Cynefin.md` | problem nodes, ПЦВЗ / SCQA, domain status, domain changes |
| `Карта актантов.md` | Estuarine actants and links to problems |
| `аналитическое досье с реестром выводов и трассировкой` | source-to-node comparison across BPMs |
| `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md` | SI / САИ / slide-intents and knowledge gaps |
| `BPV route map.md` | BPV / sub-BPV route hypotheses with source trace |
| `Interview roster / interview prep tracker.md` | known / appointed respondents, role/function, BPM, status, coverage target, brief status |
| `Interview briefs.md` | internal question briefs produced by `interview-brief-by-analogs` |

If the project folder is unknown, record `sync gap: Old Delivery document set not created` and keep the writeback proposal in chat. Do not apply this standing permission to `New Delivery`.

In Old Delivery, `dry-run` / `драйран` is not a reason to skip document creation or update. It means the rail is being tested on a real project corpus and must leave a real document trace unless Ilya explicitly says `только в чате`, `без файлов`, `симуляция без записи`, or `не создавать документы`.

This Old Delivery document-set rule overrides the generic ingest approval gate for this specific class of files. The standing permission is already granted by the Old Delivery rail rule; still prefer updating equivalent existing files over creating duplicates.

### Mining-Complete Handoff 0.3.03

If Ilya or an accepted project artifact states `майнинг завершён`, `значимые источники собраны`, `закрываем evidence-корпус`, `источников достаточно`, `останавливаем инжест`, or equivalent in an `Old Delivery` project, stop ordinary ingest accumulation and hand off to the unified Rail `post_mining_transition` in run-to-blocker mode.

Required handoff:

```text
source closure audit
-> source-corpus sufficiency verdict
-> cumulative problem-model consolidation
-> full-corpus Cynefin recheck
-> Estuarine table + visual map
-> cumulative 9-action portfolio
-> selected action -> SI / storyline / storyboard
-> sub-BPV / BPV route with 1-5 relationship score
-> client-decision definition
-> BPA.01 readiness gate
```

Do not treat a mining-complete signal as permission to start a presentation, org structure, target model, pilot package, or fresh BPV list. A later material source may reopen mining only with a named reason and preserved closure history. Do not return after a passed gate with the next gate merely `pending / next`: continue in the same invocation until a real blocker. Nonblocking gaps, open forks, provisional scores, `unplaced` actants, response length, and lack of a preferred visual tool are not blockers. Gate 2 must preserve every active P-node and every evidence-supported actant linked to an active P-node; a small set of macro-mechanisms is executive-only and cannot replace the master table, complete ledgers, or full/faceted visual. The authoritative schemas, scoring scales, population rules, zone logic, visual encoding, run-to-blocker contract, verdicts, and failure labels live in the current `rail` skill under `Post-Mining Transition 0.3.03` and must not be re-invented locally.

Post-mining writeback continues to use existing Old Delivery evidence documents: source closure in the source register / evidence trace; consolidated problems and Cynefin in `Карта проблем и Cynefin.md`; Estuarine table and embedded / linked visual in `Карта актантов.md`; actions and SI in Storyline-Storyboard; sub-BPV / BPV scoring in `BPV route map.md`. Do not create parallel post-mining files when these equivalents exist.

Every Old Delivery BPM ingest final response must include:

```text
document writeback status:
created:
updated:
not_created:
sync_gap:
```

For Old Delivery multi-source ingests, the output must include three analytical views before downstream initiative / BPV routing:

- `Macro-idea evidence map`: group respondent positions into macro-ideas / tensions, with supporting sources, divergent sources, cross-source status, and next check. Do not keep adding respondent surname columns as the primary contradiction table.
- `Polymorphic actant map`: show each actant's possible roles across problems (`actor / constraint / constructor / mixed`), mandatory linked problems, mechanism, source trace, and energy/time barriers.
- `9-action matrix`: test all nine actant-action classes for significant problem-actant pairs: `Stabilise / Destroy / Shift / Create / Monitor / Conditional / Trigger / Request / Interaction`; use `no_signal` or `low_fit` explicitly when a class does not apply.

Additional Old Delivery regression guards:

- Problem nodes must be rendered as `code + name` everywhere, not only as `P3` / `P10`.
- Actant `Roles by problem` and `Linked problems` must also use `code + name`, e.g. `P12 — Проектный контур собирается вручную: actor`.
- `Polymorphic actant map` must keep separate columns for `Roles by problem` and `Linked problems`; omitting linked problems is invalid.
- People and roles remain `actor / decision-owner`; classify the system, report, process, model, policy, or routine as `constructor`, not the person who sponsors it.
- Problem-node history must include all active problem nodes after every post-second ingest; unaffected nodes get `unchanged / no_signal`, not omission.
- Every new BPM ingest must update old problem-node statuses: `new / unchanged / confirmed / extended / refined / contradicted / merged / split / deprecated / no_signal`.
- If BPM scope is absent, stale, or only implied, create/update a BPM scope ledger with statuses `included / excluded_by_owner / deferred / recommended / candidate / not_applicable / blocked / unknown`. Recommendations must be rejectable by Ilya.
- Validate actant type: only agency-bearing entities are `actor`; mechanisms like `отсрочка`, `склад`, `KPI`, `план`, `бонус`, `договор` are normally `constraint / constructor / resource / evidence carrier`.
- 9-action matrix cells must name the concrete actant, mechanism, and required evidence/gate. Otherwise mark `action_cell_too_generic`.
- 9-action matrix is cumulative: include all active problem nodes accumulated across previous ingests, not only nodes affected by the current ingest. Use `Current ingest effect` with `new / revised / confirmed / weakened / no_change_from_current_ingest / deprecated` where needed.
- After the third significant BPM ingest, reuse-check must include concrete donor projects / knowledge units plus why they are donors, what transfers, what does not transfer, and remaining source gaps. Archetype-only reuse is incomplete.
- SI/BPV output must be a trace table with `Output / route`, `Derived from`, `Source trace`, `Status`, `Confidence`, and `Next evidence / gate`; bullet lists are incomplete for Old Delivery cumulative runs.
- SI/BPV trace must include every active problem node as a visible row or justified grouped row: direct route, `evidence_gap`, `no current SI`, or `no current BPV route`. A phrase such as `remaining nodes represented as evidence gaps` without rows is a coverage failure.
- Macro-idea evidence map is incomplete without `Supporting sources`, `Divergent sources`, `Cross-source status`, and `What must be checked next`; Polymorphic actant map is incomplete without `Source trace`, `Growth driver`, `Energy/time barrier`, and `Zone / changeability`.
- Final response must include `coverage check` across active problem nodes and `document writeback status` with project contour/path for created or updated files. Do not write `verdict: complete` when required coverage is only implied.
- At Old Delivery project initiation, org structure / interview table / respondent list may create or update an interview prep tracker. Rail does not appoint interviewees or manage the queue. When Ilya names the appointed / upcoming respondent, run or hand off to `interview-brief-by-analogs`; write the internal brief to `Interview briefs.md` / equivalent unless Ilya explicitly says chat-only.
- After ingesting an interview that had a prepared brief / question block, run `question coverage audit`: assign `question_id`, compare prepared questions to actual transcript / secondary source, separate `asked status` (`asked / not_asked / source_missing / not_applicable`) from `answer status` (`answered / partial / unanswered / no_answer_expected / source_missing`), and write unresolved questions into `аналитическое досье с реестром выводов и трассировкой` or another existing evidence document as `next-question backlog`. `not_asked` must not be reported as `unanswered`.
- Before claiming `coverage check: complete`, run the Old Delivery pre-final self-audit. Fail the run as `incomplete / passed_with_fixes` if any of these are missing or only implied: BPM-addressed source register; exact macro-idea map columns; exact problem-history columns; exact polymorphic actant columns; canonical actant typing; 9-action rows with code+name and no catch-all ranges; full question audit schema for prepared brief or carryover backlog; SI/BPV visible rows for every active P-node; writeback paths/links. Do not hide this behind `all material deltas` or `unchanged nodes gated`.
- For Rail 0.1.20+ behavior, the final coverage check must be backed by an exact node-by-node ledger: `Problem node | Problem history | Macro-idea map | Actant map | 9-action matrix | SI/BPV trace | Missing / fix`. Each active P-node must be checked separately. Counts such as `22/22` are invalid unless derived from this ledger. Ranges (`P11-P13`), clusters (`P6/P10/P18`), bare P-codes, and catch-all rows fail coverage unless the same row explicitly lists every included node as `code + name` and shows the evidence/gate for each. Missing actants require explicit `no actant signal / source_check` rows. A combined column such as `Actant/action trace` is invalid: actant coverage and 9-action coverage are separate gates. Delta tables (`actant map — delta`, `SI delta`) cannot prove cumulative coverage. Stacked source labels such as `BPM-2/4/8/9` must be decomposed into BPM-addressed source rows. Question audit must use the exact full schema and code+name links. Document writeback must include paths/links for every created/updated file, not only file names.

Rail/Ingest 0.2.01 is the unified current ingest rail, not a parallel branch. It preserves the 0.1.x Old Delivery guardrails and adds `tabular_source_ingest` as a source-class contract. For tabular sources, classify Excel / XLS / XLSX / CSV / Google Sheet export / BI table export / table dump as `tabular_source_ingest`, not automatically as an interview-like source. `question coverage audit` is `not_applicable` only if replaced by a tabular audit: source manifest, sheet/table/range register, formula/calculation audit when applicable, external-reference audit when applicable, quantitative claim trace, data-quality verdict, and source persistence status. External references are conditional: if no external references are present, write `external references: none_detected`; if external references exist but source files are absent, write `data_lineage_gap / autonomous_recalculation_not_possible`, not a generic failure. In dry-runs, a temp-only source is `source_persist_gap`; it blocks durable canonization/full auditability but does not automatically invalidate the analytical delta. Use `passed_with_tabular_delta`, `passed_with_data_lineage_gap`, `passed_with_source_persist_gap`, `incomplete_tabular_contract`, or `incomplete_quant_audit` as appropriate.

Rail/Ingest 0.2.02 is the unified current ingest rail and adds `batch_interview_ingest` for two or more interview / interview-like sources processed in one pass. Batch processing does not merge sources. Require a per-source rights table: `batch item | source_id | respondent / role | source type | source status | BPM-addressed rights | processed layers | limitations | contribution | batch synthesis rights`. Source rights must distinguish primary transcript, truncated sync, secondary summary, AI summary, structured summary, and raw-missing states. Compact BPM labels such as `BPM-1/2/8/9` must be decomposed. Run question audit per source, then carryover backlog. Batch synthesis is allowed only after per-source deltas are visible and must be marked `batch_synthesis`. If cumulative coverage is not rendered through node-by-node ledger, use `passed_with_batch_delta` or `passed_with_partial_source_limits`, not `coverage complete` / `batch ingest: passed`. Use `incomplete_batch_contract` when per-source rights/source isolation/audits are missing, and `incomplete_batch_coverage` when cumulative coverage is claimed but ledger/views fail.

When reporting interview-corpus statistics, count unique interview events at the respondent/role level, not files. A derived summary, cleaned copy, duplicate card, alternate export, or archive duplicate does not increase the interview count. Always separate at least: physical files, unique interviews, unique organizations, interviews with a primary transcript, secondary/derived-only sources, and explicitly excluded non-client or out-of-scope interviews. If one organization has several genuinely separate interviews with different respondents/roles or dates, count them as separate interviews while keeping one organization in the organization count. Preserve the deduplication basis in the project interview register or nearest existing source registry.

Rail/Ingest 0.2.03 makes the batch contract fail-fast. A batch pass is incomplete when it lacks the per-source rights table, uses compact BPM labels, collapses unaffected problem nodes as `Остальные N узлов`, uses non-exact macro-idea / polymorphic actant / 9-action / question-audit schemas, makes cross-source conclusions without the table `Batch synthesis | Source ingredients | Source-specific limits | Synthesis rights | Linked P-node / SI | Confidence | Next evidence`, reports writeback by file name without paths/links, or writes generic `batch ingest: passed`. Use failure labels: `batch_rights_table_missing`, `batch_bpm_rights_compact_fail`, `batch_problem_history_collapsed_fail`, `batch_macro_map_schema_fail`, `batch_actant_map_schema_fail`, `batch_action_matrix_schema_fail`, `batch_question_audit_schema_fail`, `batch_synthesis_table_missing`, `batch_writeback_paths_missing`, `batch_generic_pass_fail`.

Rail/Ingest 0.2.04 closes the `table present but schema wrong` loophole for batch ingest. Never mark `per-source rights table: present`, `batch synthesis table: present`, `question audit: present`, `document writeback: recorded`, or similar unless the table uses the exact required columns and row-level `code + name` / BPM-addressed trace. Exact schemas are mandatory for per-source rights, problem-node history, macro-idea evidence map, polymorphic actant map, 9-action matrix, batch synthesis, question audit, and document writeback status. Bare P-codes, slash clusters like `P8/P14/P28`, combined statuses like `confirmed/extended`, and meta-gaps standing in for P-nodes are `batch_exact_schema_gate_fail`. Allowed batch verdicts are only `passed_with_batch_delta`, `passed_with_partial_source_limits`, `incomplete_batch_contract`, and `incomplete_batch_coverage`; forbidden aliases include `completed_with_source_gaps`, `completed_with_gaps`, `batch ingest: passed`, `passed`, `complete`, `coverage complete`, and `false confirmation prevented: yes` as a verdict substitute. If source gaps remain but exact schemas pass, use `passed_with_partial_source_limits`; if any exact schema fails, use `incomplete_batch_contract`.

Rail/Ingest 0.2.05 adds a required contract for `recovery_plus_new_batch`, where previously missing/truncated sources are recovered and new sources are ingested in one pass. Recovered sources and new sources must be separated before synthesis through a recovery manifest and a new-source manifest. Recovered sources require the exact recovery-rights delta table: `source_id | respondent / role | previous source status | recovered source status | evidence upgraded | old limitations superseded | remaining limitations | allowed BPM-addressed rights | invalidated prior gaps / claims | required re-check`. A recovered source closes only the exact prior gaps shown there. Strategic forks, donor candidates, country models, or strong SI do not replace required Rail tables: full problem-node history, macro-idea evidence map, polymorphic actant map, 9-action matrix, SI/BPV trace, per-source question audit, batch synthesis, and writeback paths/links remain mandatory. If the output uses an older Rail version than the current skill, mark `rail_version_drift`. Custom verdicts such as `completed_with_new_strategic_fork` are forbidden; use only the allowed batch verdicts. Failure labels: `recovery_manifest_missing`, `recovery_rights_delta_missing`, `recovery_claim_overreach`, `new_source_rights_missing`, `strategic_fork_substituted_for_rail_tables`, `recovery_plus_batch_verdict_alias_fail`.

Rail/Ingest 0.2.06 adds a required contract for post-second single-source follow-ups: `financial_follow_up_ingest`, `follow_up_ingest`, `duplicate_dedup_ingest`, `supplemental_source_ingest`, and other non-batch sources that update an existing Old Delivery corpus. They require a single-source rights table `source_id | parent_source | respondent / role | source type | source status | BPM-addressed rights | processed layers | duplicate handling | limitations | contribution | downstream evidence gates`, exact delta schemas for problem history, macro-idea evidence map, polymorphic actant map, 9-action matrix or exact not-applicable matrix, SI/BPV trace, question/request audit, and writeback status with paths/links. `delta_only` does not allow `Остальные N узлов`; every mentioned P-node must be `code + name`; combined statuses like `partially closed/refined` fail. Allowed verdicts are only `passed_with_single_source_delta`, `passed_with_follow_up_evidence_gap`, `incomplete_single_source_contract`, and `incomplete_single_source_coverage`. Forbidden aliases include `completed_with_pending_financial_evidence`, `completed_with_follow_up_gap`, `financial vocabulary: verified`, `quantitative cross-check: passed`, `duplicate source prevented: yes`, `passed`, `complete`, and `coverage complete`. Failure labels: `single_source_rights_missing`, `single_source_exact_schema_fail`, `single_source_collapsed_nodes_fail`, `single_source_verdict_alias_fail`, `follow_up_request_audit_missing`, `duplicate_handling_trace_missing`.

Rail/Ingest 0.2.07 adds `mixed_contract_ingest` for passes combining heterogeneous source classes: `BPP governance/initiation/status event`, `BPM-SI convergence artifact`, `BPM Exchange / reuse synthesis`, `BPM-6 reference`, reference-source gap, market no-op, and similar. Such passes must first render a source-contract rights matrix `item_id | source class | object / source | registered as | allowed use | not allowed | BPM/BPP route | evidence strength | linked claims / nodes | required downstream check`. BPP events require an event ledger and cannot receive SRC-ID or confirm client facts. BPM-SI artifacts require synthesis/fact-confirmation rights and claim status. BPM Exchange/reuse requires transfer / no-transfer / adaptation gates and cannot confirm client facts. Reference gaps and market no-ops require a reference/no-op ledger. Allowed verdicts are only `passed_with_mixed_contract_delta`, `passed_with_mixed_contract_no_op`, `incomplete_mixed_contract_ingest`, and `incomplete_mixed_contract_coverage`. Forbidden aliases include `reuse donor check: completed`, `engineering synthesis classified: yes`, `market ingest: no-op` as whole-pass verdict, `processing status: completed`, `completed`, `passed`, and `complete`. Failure labels: `mixed_contract_rights_matrix_missing`, `bpp_event_ledger_missing`, `bpm_si_rights_missing`, `bpm_exchange_rights_missing`, `reference_noop_ledger_missing`, `mixed_contract_claim_overreach`, `mixed_contract_verdict_alias_fail`, `mixed_contract_rule_gap`.

Rail/Ingest 0.2.08 clarifies standalone source-class contracts. `BPP event`, `BPM-SI convergence artifact`, `BPM Exchange / reuse synthesis`, `reference-source gap`, and `market ingest no-op` may appear alone in private/specialized passes or together in `mixed_contract_ingest`. Standalone BPP uses event ledger and verdict `passed_with_bpp_event_delta` / `incomplete_bpp_event_contract`; standalone BPM-SI uses synthesis rights and verdict `passed_with_bpm_si_synthesis_delta` / `incomplete_bpm_si_synthesis_contract`; standalone BPM Exchange/reuse uses transfer/no-transfer/adaptation gates and verdict `passed_with_bpm_exchange_delta` / `incomplete_bpm_exchange_contract`; standalone reference/market no-op uses reference/no-op ledger and verdict `passed_with_reference_gap`, `passed_with_market_no_op`, or `incomplete_reference_noop_contract`. If exactly one of these classes is processed, use standalone verdicts, not mixed-contract verdicts. If two or more different source-class contracts are processed, use `mixed_contract_ingest` and include each relevant standalone ledger. Failure label for missing standalone contract: `source_class_standalone_contract_missing`.

## Client Source Persist Gate

When the input is a client / project source file, or when a file is used as evidence for analysis, it must not remain only in a temporary application folder such as `/var/folders`, `/tmp`, Downloads, or another transient local path.

Before finalizing the ingest, do one of the following:

- save the meaningful source into the existing project source landing, usually `Источники` / source-pack, without creating a new file route unless explicitly required;
- update the existing source / artifact registry when one exists;
- if the file is not saved, state an explicit no-op reason: duplicate, irrelevant, sensitive, no project folder found, Drive/Vault unavailable, or manual transfer expected.

Final responses after file-based ingest should include one of: `source saved`, `duplicate skipped`, `source persist no-op`, or `sync gap`.

### Технические наблюдения Google Drive / Sheets — 04.10.2026

- Ярлык Drive (`application/vnd.google-apps.shortcut`) не является исходным содержимым. Если metadata-wrapper не возвращает `shortcutDetails.targetId`, фиксировать ограничение и разрешать цель через интерфейс или точное название с независимой ссылкой из физического источника. Единственное совпадение названия без прямого target ID остаётся ограниченной атрибуцией; ошибку скачивания ярлыка нельзя выдавать за отсутствие доступа к исходному документу.
- При проверке XLSX-экспорта Google Sheets отдельно проверять живую формулу, формулу снимка и кэш значения. `__xludf.DUMMYFUNCTION` в снимке означает необходимость проверки переносимости, а не доказанную поломку облачного оригинала. Наличие кэша не доказывает автономный пересчёт; тест новых вводных нужен для уже действующего гейта автоматизации. Не исправлять оригинал без поручения владельца.
- Дополнение 13.10.2026: видимые имена и размеры файлов Google Drive File Provider не доказывают доступность содержимого. При `Operation timed out` проверить фактическую загрузку; на macOS флаг `SF_DATALESS` (`0x40000000`) помогает отделить облачные placeholders от полученных байтов. Применять штатную команду «Загрузить сейчас» к точно выбранному источнику/папке и затем повторно читать физический файл. Начавшаяся загрузка и исчезновение ошибки не заменяют чтения; в writeback сохранять непрочитанный остаток.
- Для загрузки через Finder не использовать `Cmd+A` вместе с общим меню «Действие»: там есть создание папки с выбранными объектами. Выбирать точный объект, читать свежее контекстное меню и нажимать только явно показанную «Загрузить сейчас». После операции проверять исходный путь и состав. При ошибочном перемещении остановить операцию, выполнить штатную отмену и проверить восстановление структуры; не продолжать чтение из случайно созданной папки.

Это техническая реализация действующих правил атрибуции, сохранения и табличного аудита; порядок Rail и партнёрский стандарт delivery не меняются.

## Notion External Object Recovery

When ingesting a Notion meeting/source page, if `fetch` shows an embedded table, file, or attachment only as `external_object_instance` / `unknown` and opening the block anchor returns the parent page again, do not treat the source as empty or fully processed.

Before finalizing:

- fetch the page with transcript enabled and identify phrases around the promised table / link / attachment;
- run Notion / connected-source search using those phrases, especially field names and distinctive business terms;
- check Google Drive / Sheets results that match the meeting date, project, or table fields;
- if the embedded object still cannot be read, record an explicit `source gap` naming the hidden block and the expected content;
- if a related Drive/Sheets file is found, ingest it as a separate source with its own ID and do not conflate it with the unread embedded object.

## Granola Shared-Link Recovery

When ingesting a Granola note or transcript link, do not stop at connector search failure.

Before declaring `source gap`:

- extract the canonical document UUID from `/t/<slug>` links, recognizing that copied links may append a share suffix after the UUID;
- try Granola connector search / meeting retrieval by likely title, date, and UUID;
- if the connector cannot see the note, open the shared URL directly and follow its redirect to `/d/<uuid>`;
- Уточнение 22.09.2026: UUID в ссылке `/t/` может быть идентификатором общего доступа и отличаться от UUID встречи в фактическом адресе `/d/`. После наблюдаемого перенаправления повторно вызвать `get_meetings` и `get_meeting_transcript` с UUID из `/d/` до вывода о недоступности коннектора или перехода к одной AI-выжимке. Сохранять связь исходной ссылки и фактического UUID; это один физический созвон. Большой ответ транскрипта сначала сохранить в рабочей памяти инструмента, вывести размер и метаданные, затем читать ограниченными фрагментами вместо полного дампа.
- Уточнение 22.09.2026 по встречам у доски: реплики «вот эта работа — два месяца», «эта — месяц» без изображения / однозначного текстового указателя подтверждают произнесённые оценки, но не их привязку к этапам. Не наследовать такую привязку из AI-выжимки и не суммировать длительности параллельных работ как последовательные. В коммерческом следе отдельно сохранять общий ориентир, однозначно названные сроки конкретных этапов, условие «если договоримся» и неустановленную привязку остальных оценок.
- inspect the returned page for readable `original_content`, `generated_lines`, transcript links, or embedded Next/HTML data;
- if the page is readable, classify the source as `meeting_note / transcript-page-readable` and record the connector limitation as `connector-access gap`, not as missing evidence;
- if neither connector nor public page exposes content, record a precise `source gap` with the note URL, expected content, and likely access owner.

This matters because a Granola note created or shared by another PP teammate may be invisible to the authenticated connector while still readable via the copied share URL.

## Modes

| mode | use when | output |
|---|---|---|
| `intake` | material is present but not yet understood | short input summary and missing context |
| `classify` | material can be typed and statused | `material_type` + `canonical_status` |
| `route` | likely existing landing places can be checked | target existing files / contours |
| `proposal` | writeback may be useful but needs approval | `ingest_proposal` |
| `writeback` | Ilya explicitly approved this specific writeback | edits to existing files, then `post_writeback_delta` |
| `no-op` | material should not be durably written | `no_op_reason` |
| `return-packet` | external output needs review, not canonization | accepted / change / defer / reject / source-check |

Mode transitions:

1. `intake -> classify`: only after source and material boundaries are clear enough.
2. `classify -> route`: only after material type and canonical status are assigned.
3. `route -> proposal`: when an existing landing place exists but writeback is not yet approved.
4. `proposal -> writeback`: only after explicit approval from Ilya for this writeback.
5. Any mode may end in `no-op` if durable landing would create noise, duplicate, or false canon.

## Intake Types

Use the smallest type that fits.

| type | meaning | default status | default handling |
|---|---|---|---|
| `fact` | verifiable statement | `candidate` | needs source / landing check |
| `hypothesis` | plausible but unverified idea | `raw` | do not canonize without check |
| `user_decision` | explicit decision by Ilya | `accepted` | route to existing decision / project / rule trace |
| `rule` | operating rule, policy, or "always do X" | `proposal` | rules writeback gate unless already explicitly accepted |
| `external_research` | ChatGPT / Perplexity / NotebookLM / analyst output | `raw + requires_source_check` | review as source, not fact |
| `content_candidate` | possible post, article, case, weekly slot, or idea | `raw` | route through content maturity, not canon |
| `task` | work item / commitment / next action | `candidate` | route to task tracker / inbox, not knowledge note |
| `commercial_fact` | lead, КП, win/loss, price, deal, partner, referral, event | `candidate` | route to commercial trace / metrics source |
| `contradiction` | conflicts with existing canon or source | `flagged` | stop and show conflict |
| `do_not_ingest` | noise, duplicate, unsafe, or not useful | `no-op` | return no-op reason |

Route hints are not primary types: `glossary_term`, `persona`, `project_ref`, and `source_pack` are route hints that still need one of the material types above.

## Canonical Statuses

| status | meaning | allowed actions |
|---|---|---|
| `raw` | received but not accepted as knowledge | summarize, classify, keep in chat/proposal |
| `candidate` | classified and may be useful | propose landing, ask / wait for approval |
| `proposal` | writeback proposal is formed | show to Ilya; no durable write yet |
| `accepted` | explicitly accepted by Ilya or already canonical | writeback allowed if target is clear |
| `source-check` | needs verification before use | do not canonize as fact |
| `internal-only` | usable inside Vault, not client-facing | keep DLP caveats |
| `client-facing` | safe for external wording | still preserve source and date |
| `do-not-use` | false, unsafe, obsolete, or misleading | do not cite or write as active knowledge |
| `archival` | historical / read-only | do not overwrite active canon |
| `no-op` | no durable action needed | explain why |
| `flagged` | conflict / ambiguity / risk | stop and show conflict |

`raw` does not imply creating a staging file. If no existing staging place is known and no file was requested, keep the material in chat/proposal until a route is accepted.

## Preflight Template

Before any writeback, produce or internally satisfy this preflight. If fields are materially unknown, stop in `proposal`.

```yaml
ingest_preflight:
  source: "user|external_ai|notebooklm|file|email|meeting|crm|other"
  material_type: "fact|hypothesis|user_decision|rule|external_research|content_candidate|task|commercial_fact|contradiction|do_not_ingest"
  canonical_status: "raw|candidate|proposal|accepted|source-check|internal-only|client-facing|do-not-use|archival|no-op|flagged"
  target_existing_files: []
  source_persist_check:
    source_path: ""
    project_folder_found: null
    target_source_landing: ""
    duplicate_status: "unknown|duplicate|new|not_applicable"
    registry_update: "done|not_needed|sync_gap|blocked"
    no_op_reason: null
  proposed_action: "append_to_existing_file|update_existing_section|update_frontmatter|add_registry_entry|task_route|commercial_trace|no_op"
  allowed_actions: []
  forbidden_actions:
    - "create_new_file_without_explicit_user_command"
    - "create_new_registry_without_explicit_user_command"
    - "leave_client_project_source_only_in_temp_folder_without_no_op_reason"
    - "canonize_hypothesis_or_external_research_as_fact"
    - "overwrite_existing_canon_without_conflict_review"
  open_questions: []
  requires_approval: true
  approval_received: false
```

## Output Contracts

Use compact Markdown by default. YAML-like blocks are useful when the user needs to approve routing or writeback.

```yaml
ingest_proposal:
  preflight: {}
  summary: ""
  diff_preview:
    add: []
    modify: []
    delete: []
  confidence: "low|medium|high"
  blocker: null
```

```yaml
writeback_plan:
  approved_by: "Ilya"
  approval_timestamp: ""
  steps:
    - action: "append|update_existing_section|update_frontmatter|add_registry_entry"
      file: ""
      content_summary: ""
  rollback_note: ""
```

Use `rollback_note` for frontmatter, registries, rules, canonical files, and risky edits. It is optional for small append-only updates.

```yaml
no_op_reason:
  input_summary: ""
  reason: "duplicate|noise|external_unverified|already_canonical|out_of_scope|unsafe|not_worth_durable_write"
  recommendation: null
```

```yaml
post_writeback_delta:
  files_modified: []
  entries_added: []
  registries_updated: []
  status_changes: []
  timestamp: ""
```

## External AI Input Policy

Outputs from ChatGPT Pro, Perplexity, NotebookLM, external analysts, or similar systems are not canon by default.

Default handling:

- material_type: `external_research`;
- canonical_status: `raw + requires_source_check`;
- split into `usable`, `needs_source_check`, `internal_only`, `do_not_use`, and `project_specific`;
- do not write market claims, client claims, legal/regulatory claims, competitor claims, or numeric claims as facts without source/source-date/evidence status;
- if the external output materially affects a project storyline, rail, task, or decision, route it as a return packet and show accepted / changed / deferred / rejected items before durable writeback.

## Compound-Validity Guard

When an analytical artifact crosses two or more derived dimensions, models, segmentations, mappings, scores, or taxonomies, do not validate only the final matrix or visualization. Audit every parent axis, the join key, grain compatibility, and denominator separately.

Use the default rights rule:

```text
cross_rights = min(axis_1_rights, axis_2_rights, join_key_rights, grain_compatibility, denominator_rights)
```

- If any parent axis is `raw`, `source-check`, `flagged`, or semantically contradicted, the cross-output cannot become an accepted fact or action-ready model merely because totals reconcile or the heatmap looks coherent.
- Preserve the valid arithmetic layer separately from business interpretation.
- Show how conclusions change under the strongest available canonical or operational axis when one exists.
- Block downstream quotas, targeting, KPI, pricing, cash, investment, or organizational prescriptions until the weakest required parent layer passes its evidence gate.
- Record duplicate parent defects once, but state explicitly that crossing them compounds rather than repairs the limitations.

## Recalculated-Report Version-Coherence Guard

When a user supplies a report described as updated, recalculated, corrected, final, or primary, do not infer that every page, caption, legend, narrative paragraph, recommendation, and managerial label was regenerated from the new data.

Required checks when a predecessor exists:

1. Compare binary identity, extracted text, and rendered pages separately. A changed PDF hash with identical text and rendered pages is a `logical_duplicate`, not new evidence.
2. Build a page/object delta: `changed table/chart`, `unchanged narrative`, `changed caption`, `stale caption`, `new claim`, `removed claim`.
3. Reconcile changed numerical objects to the strongest upstream row-level sources and transformation rights.
4. Assign `primary` status claim-by-claim or object-by-object. Do not make the whole file primary if only its charts changed.
5. Mark surviving old values next to a new figure as `superseded_by_recalculated_table`; do not average, blend, or silently choose between them.
6. If a report contains conflicting periods, entity counts, regions, owners, or totals, preserve the valid numerical layer and block the conflicting interpretation until the generator or source owner resolves it.
7. For client-facing reuse, require a version manifest and automated claim test linking `claim_id → value → period → formula → source hash → allowed meaning`. Charts, legends and prose must resolve from the same claim object.
8. If a meeting transcript contains a financial or quantitative scenario whose spoken coefficients, arithmetic result, or causal bridge do not reconcile, preserve the managerial direction as a hypothesis but do not canonize the number. Reconstruct the formula and inputs, show the arithmetic discrepancy explicitly, and require a source-owner or model check before client-facing reuse.

Use `passed_with_data_lineage_gap` when the recalculated numerical layer is valid but generator code, version manifest, or caption coherence is missing. Use `incomplete_quant_audit` when the changed numerical layer itself cannot be reconciled.

## Гейт идентичности SI до маршрутизации

До создания/дополнения SI или переноса source delta в Storyline-Storyboard применять гейт идентичности из `~/.codex/AGENTS.md` и канона SI-карточек: сверить каталог, карточку и точную пару `код + каноническое название`, смысл/модель и входы. `SI-<число>` не назначается по свободному номеру/max+1 в проекте. Проектный ID, каноническая ссылка и клиентский заголовок раздельны; коллизия старой строки не наследуется новым ingest. Нет подтверждённого соответствия — маркированный проектный кандидат/ближайшие аналоги, без автоматической канонизации и массового переименования. Визуальный референс проверять отдельно; gate повторить перед writeback. Действует и при работе только в чате. Решение Ильи 14.10.2026, уточнение существующего правила от 29.08.2026.

## BPM-3 Evidence-Rights Guard

When ingesting client interviews, non-client interviews, external client sources, or project materials that may become `BPM-3`, do not let org interviews or internal opinions become direct proof of client jobs.

Required routing:

- `BPM-3` / external client evidence may prove client jobs, pains, value criteria, choice / non-choice factors, service expectations, and acceptance barriers.
- `BPM-2` / org interviews may validate execution risks, owners, handoffs, data, systems, SLA, CJM / service-blueprint requirements, and whether the proposed job is operationally plausible.
- A job / barrier slide candidate must keep this chain visible: `BPM-3 evidence -> job / acceptance barrier -> BPM-2 validation -> CJM / storyboard requirement -> SI / presentation assembly`.
- If a client job is derived only from `BPM-2`, mark it as `internal hypothesis / needs BPM-3 evidence`, not as an accepted client job.

## No-Op Path

No-op is a valid successful outcome.

Use `no-op` when:

- the material is duplicate;
- the material is noise or too weak;
- it is an unverified external claim with no immediate route;
- the existing canon already covers it;
- the material is outside current scope;
- writing it would create a parallel registry or low-value note;
- the user has not asked for a file and no existing landing place is appropriate.

Always explain the reason and, when useful, suggest the next better action.

## Anti-Sprawl Rules

### Безопасность массовых правок метаданных

- Перед однотипной правкой нескольких существующих файлов сохранять доступный для восстановления точный исходный текст или проверенную физическую версию каждого файла. Наличие синхронизации само по себе не доказывает, что нужная версия сохранена.
- Короткое поле frontmatter менять в пределах одной конкретной строки и первого блока YAML. Предпочитать построчную замену с проверкой старого значения; не применять к полному документу регулярное выражение, которое может захватить перевод строки. Перед записью проверить предполагаемую дельту: изменилось ровно разрешённое поле, заголовки, тело и остальные метаданные совпадают с исходным текстом.
- После записи каждого файла повторно проверить целевое значение, точную сохранность остального текста и валидность YAML. При несовпадении остановить пакет, восстановить точную версию и проверить совпадение полного текста; не восстанавливать потерянное содержимое по пересказу. При сравнении длин между JavaScript и Python учитывать различие UTF-16 и числа символов Unicode; длина не заменяет проверку содержимого.

- Search existing landing places before proposing a new file.
- Do not create new files unless Ilya explicitly requested a file/artifact or existing rules treat the wording as explicit file creation.
- Do not create new registries when an existing registry, tracker, backlog, or project file can receive the signal.
- Do not treat "useful" as "must be written."
- Do not mix fact and hypothesis in the same status.
- Do not let external AI output become accepted canon without source-check.
- Do not overwrite contradictory canon silently; stop with `flagged`.
- Do not route tasks into knowledge notes when a task tracker / inbox is the correct home.
- Do not leave commercial facts only in chat if a commercial trace route exists.
- Do not leave client / project source files only in temporary paths after using them as evidence; save them into the existing project source landing or record an explicit no-op / sync gap.
- After uploading a client source batch, relist the exact destination folder before publishing links. Verify one intended copy per canonical name and size. If the current connector operation created exact duplicates, keep the instance referenced by the registry and remove only the redundant newly created copies; never delete a pre-existing non-identical version on name alone.

## Eval Cases

| # | input | expected behavior | forbidden behavior |
|---|---|---|---|
| 1 | `добавь в Vault` without material or destination | ask for material / purpose; no write | write to a random file |
| 2 | external research packet | classify as `external_research`, `source-check`; return-packet/proposal | canonize as fact |
| 3 | commercial deal fact | route to commercial trace with source/status | create a new commercial file without command |
| 4 | new content idea | classify as `content_candidate`; route through content maturity | write as evergreen canon |
| 5 | new rule / "always do X" | treat as `rule`; use rules approval/writeback gate | silently edit rules without accepted scope |
| 6 | short phrase that may be a project/chat/contour name | check registries before answering substantively | treat as ordinary topic immediately |
| 7 | `запомни` without clear object | clarify or propose target/status | create a vague memory note |
| 8 | contradiction with existing canon | mark `flagged`, show conflict | overwrite existing canon |
| 9 | explicit `создай файл X` | confirm route/content if needed, then create appropriate file | create empty / misplaced file |
| 10 | weak rumor or unsupported claim | no-op or source-check | write with "maybe" as durable knowledge |
| 11 | NotebookLM summary | source-check / proposal; do not canonize | treat summary as primary source |
| 12 | org interview says "clients need X" | register as BPM-2 internal hypothesis / execution signal; request or link BPM-3 evidence before SI | promote it directly to client job / presentation claim |
| 12 | duplicate existing entry | no-op with link/target | create parallel entry |
| 13 | client PDF/HTML/MD/XLSX source in `/var/folders` or Downloads | save meaningful source to existing project `Источники` / source-pack and update registry, or state duplicate/no-op/sync gap | use source for analysis and leave it only in temp |

## Done Definition

The skill is done when:

- material is classified by type and canonical status;
- existing landing places were checked or absence was stated;
- no writeback happens without explicit approval unless the user directly requested a file and the action is unambiguous, or the action is the mandatory Old Delivery BPM evidence document set described above;
- external AI output is not canonized as fact;
- no-op is used when durable writeback would add noise;
- writeback, when approved, ends with `post_writeback_delta`;
- risky conflicts are flagged instead of silently overwritten.

## Structured Analytical Artifact Ingest Gate

If the incoming material creates or changes a Problem Map, issue/hypothesis tree, MECE partition, evidence/claim/source-to-node matrix, analytical Mermaid, storyline-storyboard, metric tree, or dimension architecture, apply the global contract in `~/.codex/AGENTS.md`. Classify methodology source, physical evidence source, processing rights, model contract, completeness gate, mirror state, and target existing artifact separately. Do not create a parallel methodology skill/file, do not let Frappe block ingestion, and land the source as a visible delta before any full rewrite or canonization.


## Подключаемые нормы из AGENTS — 14.10.2026

Темы: `источники`, `метаданные`. Полные исходные формулировки перенесены без пересказа; номера и исходные разделы нужны для проверки. Это не новое разрешение на запись. Последняя прямая команда и действующее ядро имеют приоритет перед старыми примерами. РГ1/РГ2, Task Inbox и снятые маршруты не восстанавливаются по историческому тексту; ClickUp по умолчанию только для чтения. Подключать применимые нормы с условиями и исключениями, не весь файл и не все режимы подряд. Дословный исторический текст хранится для трассировки, а не отменяет более позднее решение. Указатель / проверка: `scripts/model_router.py --instruction-contract "<тема>"` / `--check-instructions` из корня PP.

### Г-122. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-122:start -->
- Если пользователь приносит результат ChatGPT Pro / Perplexity / deepresearch / NotebookLM / внешнего аналитического пакета по проекту 4-го отдела, а в проекте есть или должен быть `BPM Storyline-Storyboard`, считать такой материал `BPM-candidate source`, если он касается рынка, категории, конкурентов, positioning, моделей продаж, buyer roles, канала, reuse, доказательности или будущей деки.
<!-- agents-norm:Г-122:end -->

### Г-123. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-123:start -->
- `proposal-review` и `deepresearch Return Packet` не считаются завершёнными, пока агент не обновил существующий `BPM Storyline-Storyboard — гипотезы, слайды и дефициты знания.md` или не записал в нём / ближайшем проектном артефакте явную no-op причину.
<!-- agents-norm:Г-123:end -->

### Г-124. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-124:start -->
- Обязательная цепочка: `external output -> local return packet -> possible BPM increments -> SI / SIM / slide hypotheses -> lack of knowledge / field questions`.
<!-- agents-norm:Г-124:end -->

### Г-125. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-125:start -->
- Если Илья прямо назначает BPM для инжеста, например `приравняй к BPM7a`, этот BPM становится primary classification; вторичные BPM-инкременты всё равно фиксируются, если материал также касается конкурентов, buyer roles, sales process, канала, CRM или продуктовой матрицы.
<!-- agents-norm:Г-125:end -->

### Г-126. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-126:start -->
- Нельзя завершать ответ только устной оценкой внешнего исследования, если оно материально меняет будущие storyboard-гипотезы, evidence gates или дефициты знания проекта.
<!-- agents-norm:Г-126:end -->

### Г-127. External research ingest и Storyline-Storyboard

<!-- agents-norm:Г-127:start -->
- После каждого обновления проектного `BPM Storyline-Storyboard` финальный ответ обязан показывать дельту выводов в трёх группах: `появились`, `усилились`, `ослабли`. Если в группе нет значимой дельты, писать `нет существенной дельты`. Нельзя ограничиваться только перечнем изменённых файлов.
<!-- agents-norm:Г-127:end -->

### Г-193. Клиентские регламенты и регулярные форматы

<!-- agents-norm:Г-193:start -->
- Для каждого нового артефакта сразу определять, где он живёт: источник, processed, карточка проекта, daily, договорный контур или другой релевантный контур проекта.
<!-- agents-norm:Г-193:end -->

### Г-194. Клиентские регламенты и регулярные форматы

<!-- agents-norm:Г-194:start -->
- При клиентском инжесте локальные вложения и файлы-источники не оставлять только во временной папке приложения. По умолчанию складывать релевантные клиентские источники в Google Drive-папку проекта, в подпапку `Источники`. Локальную рабочую папку Codex использовать только как временный рабочий слой или fallback, если Google Drive-папка проекта не найдена; в таком случае явно сказать про sync gap. Дубли и явно нерелевантные файлы не копировать, а в ответе коротко фиксировать, что пропущено.
<!-- agents-norm:Г-194:end -->

### С-135. Жёсткие принципы (из устава, дублирую для агента)

<!-- agents-norm:С-135:start -->
10. **Metadata minimum.** Для новых и активно трогаемых Vault-сущностей по возможности фиксировать минимум: `тип`, `статус`, `owner`, `контур`, `источник`/`источники`, `обновлён`, `связи`. Если `тип` уже занят legacy-классификацией документа, добавлять `тип-сущности` как canonical entity type. Старые файлы не мигрировать массово; дополнять только при естественном касании.
   Дополнение по задачам: если агент регистрирует, добавляет или обновляет задачи в трекере / task-list / реестре задач и сообщает об этом пользователю, в финальном ответе нужно показывать не только ID задач (`T3-34`, `T5-23` и т.п.), но и содержание каждой новой или существенно изменённой задачи: ID, краткое действие, владелец / контур, срок, выход и зачем это нужно. Если задач много, использовать компактную таблицу или сгруппированный список. Запрещено оставлять пользователю только перечень ID без расшифровки. Любой вывод списка задач, блокеров, candidate-вех или backlog-строк для обсуждения / triage / bulk editing должен иметь устойчивую сквозную нумерацию или колонку `#`, чтобы Илья мог ссылаться на пункты диапазонами и пачками. Каждый нумерованный пункт задачи CORD Task OS / CoreTask OS / Task OS должен показывать не только номер и ID, но и название / краткое действие задачи; голые ID или диапазоны ID без названий допустимы только если пользователь прямо попросил машинный список идентификаторов. В таких списках по умолчанию не выводить задачи со статусом `готово` / `выполнено` / `снято`, если Илья прямо не попросил показать закрытые / готовые задачи.
   Дополнение по source-check задачам: задачи вида `разобрать raw/source и вынуть task-delta`, созданные только чтобы не потерять сигнал из встречи / Soroka / Notion digest, нельзя держать активными после успешной сверки. Если дельта уже покрыта существующими задачами / субтреками / субпаспортами, закрывать такую строку в MD source of truth как `готово / no-op` с evidence, какие задачи покрывают сигнал и что новых задач нет.
   Актуализация 18.08.2026 по РГ: `РГ1` / `РГ2` больше не являются текущими операционными контурами. Следующие legacy-дополнения про Google Spreadsheet РГ1, `needs RG1 reconciliation`, Basecamp РГ1 и отдельные РГ-паспорта не применять без свежей прямой команды Ильи именно на исторический РГ-объект. По умолчанию task-route ищется в актуальном проектном контуре 4-го отдела; если он не подтверждён, статус `local_staging / требуется актуальный task-route`.
   Дополнение по проектам РГ1: для проектов РГ1 primary tracker задач — таблица РГ1 в Google Docs / Google Drive, если Илья не задал явное исключение для конкретного проекта. Алиасы `Гугл спредшит РГ1`, `Гугл спрашатай Г1`, `Г1`, `таблица группы 1`, `Google Spreadsheet РГ1`, `RG1 Project Planning System` считать прямой ссылкой на таблицу `RG1 Project Planning System`, а не поводом начинать с локального поиска по Vault. Известный spreadsheet ID: `1R-T2dwK9zl4_aUwJ0QoFQPrPIzGSynO-QjyjeQtaeIs`; если ID не срабатывает, сначала использовать Google Drive search по `RG1 Project Planning System` / `РГ1`, и только потом локальный `rg` как fallback. Локальные `Трекер-задач.md`, `24_Трекер...md`, субпаспорта и MD-реестры в Vault являются только человекочитаемым следом, historical ledger или подготовительным слоем task-delta; они не считаются завершённой регистрацией задачи и не являются source of truth по статусам. Перед записью в РГ1 агент обязан редуцировать поток задач: не плодить специализированные микростроки, а бандлить близкие task-delta в компактные управленческие пакеты с владельцем / контуром, сроком или событием, ожидаемым выходом, причиной и source-trace. При добавлении, изменении или закрытии задач в проекте РГ1 агент обязан сначала пытаться работать с таблицей РГ1 через доступный Google Drive / Docs / Sheets контур. Если таблица РГ1 недоступна или ссылка на неё не установлена, в ответе и локальном следе явно фиксировать `sync gap: требуется перенос в таблицу РГ1`, а не писать `pending_airtable` и не считать MD-трекер достаточным. Это правило имеет приоритет над общими правилами про Airtable / Codex Project Task Inbox для проектов 4-го отдела.
   Дополнение по writeback задач для РГ1: задачи РГ1 больше не трассируются через мост в Airtable как основной маршрут. Когда в обсуждении, проходчике, Soroka, Daily, `/cordos`, `/summary`, `/tunnel` или проектном reconcile появляется явная постановка, изменение, закрытие или снятие задачи по проекту РГ1, маршрут такой: `task signal -> bundled candidate / task_delta -> явный акцепт Ильи или прямая команда -> Google Spreadsheet РГ1 -> planning / reconciliation группы РГ1`. В строке РГ1 нужна пометка `PP/Codex ingest` или эквивалентная: это первичный инжест Paper Planes / Codex, а не финальная плановая истина группы. РГ1 может принять строку, объединить её с другой, переименовать, снять, разнести по другой задаче или вернуть на уточнение. Нельзя писать такие задачи напрямую в Task OS, `chat_manual`, SQLite, Airtable или MD-трекер как primary route для РГ1.
   Дополнение по пилоту Basecamp-задач: пока Илья явно держит Airtable-решение отложенным и просит внедрять Basecamp, прямые команды `в Basecamp`, `поставь в Basecamp`, `добавь в Basecamp`, `зафиксируй todo в Basecamp`, `из этого чата отправь задачу в Basecamp` и близкие формулировки являются акцептом на маршрут `chat/task signal -> task-delta -> Codex/Vault preflight проекта и контура -> Basecamp project/todolist -> Basecamp todo`. Этот маршрут не проходит через `Codex Project Task Inbox` и не создаёт Airtable writeback. Для 4-ки сохранять MD/Vault-трекер как человекочитаемый trace, если проектный контур требует следа, но операционная задача пилота живёт в Basecamp. Если проект или контур не распознан, не терять задачу: использовать Basecamp fallback-list `Inbox / Требует раскладки` в распознанном Basecamp-проекте; если проект не распознан, остановиться и запросить/зафиксировать routing gap. Airtable вернётся отдельным решением Ильи и не должен автоматически перехватывать Basecamp-команды.
   Дополнение по иерархии Basecamp РГ1: в папке / пространстве `РГ1` отдельные Basecamp-проекты первого уровня (`РОСМА`, `Аконит`, `Индид`, `OrtoLight`, `Вастэко` и близкие) считать каноническими рабочими проектами для детального машинного чтения, задач, артефактов, владельцев, сроков и статусов конкретного проекта. Проект / папку `ЧЕТВЕРКА - РГ1` считать портфельным обзором и верхнеуровневым контролем по РГ1: она может содержать дубли конкретных проектов, заведённые ошибочно, но полезна как срез портфеля. При запросе по конкретному проекту сначала идти в отдельный Basecamp-проект; при запросе общего обзора ситуации по РГ1 сначала идти в `ЧЕТВЕРКА - РГ1` и затем, при необходимости, проваливаться в отдельные проекты.
   Дополнение по двухмаршрутному обогащению Basecamp РГ1: если Илья просит завести, обогатить или обновить проект РГ1 в Basecamp из паспорта, карты треков, source-home, портфолио или проектного реестра, агент должен различать два слоя и при необходимости наполнять оба. Первый слой: `ЧЕТВЕРКА - РГ1 -> todoset проекта` как портфельная карточка / обзор, где создаются или обновляются to-do lists по трекам / П1-П14, лёгкие задачи и связи для видимости на портфеле. Второй слой: отдельный Basecamp-проект `<проект>` как рабочий контур, где нужно включить `To-dos` и `Docs & Files`, создать to-do lists по трекам с сохранением нумерации, добавить паспортные задачи `N.0` с описанием, ИКР и взаимосвязями, перенести важные пункты плана работ, загрузить ключевые файлы и создать навигационный документ / source-home. При обогащении отдельного Basecamp-проекта не сводить всё к задачам и файлам: выбирать нативный тип сущности по управленческой функции материала. `Schedule / Calendar` использовать для встреч, комитетов, дедлайнов и контрольных дат; `Message Board / сообщения` — для решений, протоколов, смысловых апдейтов, проектных объявлений и handoff-заметок; `Docs & Files` — для паспортов, source-home, документов и тематических окон; `To-dos` — только для исполнимых действий с владельцем, сроком и выходом; `Campfire / Chat` и `Check-ins` — для коротких статусов, регулярных вопросов и операционного ритма, если это уместно в проекте. Если Илья просит `перенеси в Basecamp`, `создай в Basecamp`, `вгрузи в Basecamp`, `разложи в Basecamp`, `обогати Basecamp` или близко, это означает полный корпус Basecamp-переноса, а не частичную загрузку: проверить / создать проект и портфельный слой, включить и упорядочить dock, разнести задачи, файлы / документы, сообщения, календарь, chat / check-ins, и обновить локальный Vault-trace. Для каждой нативной сущности либо внести содержимое, либо явно зафиксировать no-op / routing gap: нет подтвержденных будущих дат, нет регулярного вопроса, нет материала для сообщения, нет файлов для окна, нет исполнимых задач. Портфельный слой не заменяет полноценный проект, а полноценный проект не отменяет портфельный обзор. Если один слой отсутствует, создать его или явно зафиксировать routing gap; если есть оба, не считать это дублем.
   Дополнение по проектным трекерам 4-ки и Airtable: для проектов 4-го отдела вне РГ1 проектный MD-трекер остаётся человекочитаемым следом, но не достаточным writeback; Airtable / Inbox-маршрут применяется только если он явно задан текущими правилами конкретного проекта. Для проектов РГ1 это дополнение не применяется: там используется Google Spreadsheet РГ1 с бандлованием и пометкой `PP/Codex ingest / needs RG1 reconciliation`.
   Дополнение по отключению Airtable и Codex Project Task Inbox: с 05.07.2026 Airtable writeback и `Codex Project Task Inbox` отключены как рабочие функции по умолчанию. Агент не должен создавать, обновлять, предлагать к записи или использовать эти контуры как primary / downstream route для новых task_delta, radar-routing, partners-ingest, `/cordos`, `/summary`, `/tunnel`, project reconcile или ручных задач. Для РГ1 используется `RG1 Project Planning System` с пометкой `PP/Codex ingest / needs RG1 reconciliation`; для явных Basecamp-команд используется Basecamp; для остальных контуров без утверждённого живого трекера — proposal-only + существующий локальный trace / sync gap. Старые упоминания `Codex Project Task Inbox -> Airtable`, `pending_airtable`, `Airtable bridge`, `Airtable sync gap` считать legacy/historical, а не инструкцией к действию. Вернуть Airtable или Project Task Inbox можно только отдельным прямым решением Ильи.
   Дополнение по текущему task-route 13.07.2026: YouGile отменён как рабочий downstream. Актуальный route для проектов вне РГ1 — ClickUp через локальный `clickup-mcp-router`, если конкретный проект / контур имеет там живой контейнер или Илья прямо просит этот маршрут. По умолчанию ClickUp используется только для чтения: сканировать, искать, атрибутировать workspace / space / folder / list / project task, читать существующие задачи / документы / статусы и проверять контейнеры. Проходчики, heartbeat, Soroka, `/cordos`, `/summary`, `/tunnel` и ручной ingest не должны принудительно писать задачи в ClickUp из чата без отдельной прямой команды Ильи на запись. Без такой команды достаточно помнить / показать task_delta / оставить локальный trace в существующей посадке и фиксировать `local_staging / clickup_container_found` или `clickup_sync_gap`. В пользовательских ответах больше не нужно перечислять старый выключенный стек (`YouGile`, `Airtable`, `Task OS`, `chat_manual`, `SQLite`, `Codex Project Task Inbox`) как disclaimer или `sync_status`; эти контуры считать внутренним legacy-контекстом для антидубля только если Илья специально спрашивает.
   Дополнение по статусу миграции 19.07.2026: перенос инвариантов Delivery OS из YouGile в ClickUp считается завершённым. ClickUp является ключевой системой проектной работы Paper Planes; нельзя описывать перенос в ClickUp как будущую инициативу, незавершённую миграцию или открытый стратегический gap без нового конкретного evidence. YouGile остаётся только историческим источником и архивным reference-слоем. Для РГ1 `RG1 Project Planning System` по-прежнему является первичным task-tracker, а ClickUp сохраняет роль ключевой проектной системы; это явное маршрутное исключение, а не отмена статуса ClickUp.
   Дополнение по проектным гипотезам 26.07.2026: в активных проектах `04 Производство` фундаментальные проверяемые утверждения вести в ClickUp как нативный тип `Гипотеза`, отдельно от обычного канбана исполнения. Гипотеза отличается от задачи, темы, открытого вопроса, P-узла и слайд-интента: она должна быть фальсифицируемым утверждением, иметь источник / evidence, способ проверки и решение, которое изменится. Общая схема полей: `Состояние`, `Класс`, `Уверенность`, `Источник / evidence`, `Способ проверки`, `Какое решение изменится`, `Дата пересмотра`; жизненный цикл: `сигнал -> сформулирована -> проверяется -> подтверждена / опровергнута / отложена`. После каждого значимого интервью, датасета, встречи или аналитического источника агент обязан сверять живой набор гипотез через `new / strengthened / weakened / contradicted / no_change`, обновляя смысловой дубль вместо создания новой карточки. Каноническая связка: `источник -> гипотеза -> проверка / запрос evidence -> решение -> явно одобренная задача исполнения`; подтверждение гипотезы не порождает задачу автоматически. Владельцев и даты не придумывать. ClickUp хранит операционную карточку и состояние зрелости, а Storyline/Storyboard, субпаспорта, интервью и evidence-матрицы остаются слоями источников и синтеза и не образуют параллельный реестр статусов. Запись в ClickUp требует отдельной прямой команды Ильи; после массовой записи обязательны проверка реального `task_type`, содержимого, отсутствия дублей и счётчиков проектной / портфельной доски. Полная техническая схема, шаблон и UI-ограничения живут в `clickup-mcp-router`.
<!-- agents-norm:С-135:end -->

### С-197. Tool selection rules

<!-- agents-norm:С-197:start -->
- **Notion:** два равноправных канала — прямой REST-API (`https://api.notion.com/v1/*` с токеном) и MCP-коннектор (`mcp__*__notion-*`). Выбор — по задаче (workspace-search чаще быстрее через MCP, сложные database-запросы — через прямой API).
<!-- agents-norm:С-197:end -->

### С-198. Tool selection rules

<!-- agents-norm:С-198:start -->
- **Google Drive:** прямой доступ через смонтированную папку `~/Library/CloudStorage/GoogleDrive-balahnin@paper-planes.ru/Мой диск/`. MCP Drive — только для поиска по Drive-API, если локального зеркала нет.
<!-- agents-norm:С-198:end -->

### С-199. Tool selection rules

<!-- agents-norm:С-199:start -->
- **4ка / общий production shared drive:** если в локальном Vault-контуре проекта 4-го отдела не найдены данные, документы или rail-опоры, которых не хватает для выполнения процедуры, project push, Rail, source-check, stage-gate, BPM/BPP-сверки, инжеста, возврата проекта на рельсу или создания контентно-насыщенных проектных файлов, общий shared drive `~/Library/CloudStorage/GoogleDrive-balahnin@paper-planes.ru/Общие диски/Paper Planes/4. Производство/` является обязательным маршрутом source-recovery. При fallback / фиаско локального Vault-поиска агент заранее и принудительно проверяет общий shared drive 4 производства, ищет релевантную папку проекта не только по точному имени, но и по широкому семантическому схождению названия, клиента, алиасов, РГ, партнёра и темы. В найденной папке нужно инвентаризировать доступные файлы проекта: карту чатов, админ-шкалу, stage-gate, BPM/BPP-артефакты, дорожные карты, уставные / стартовые документы, источники, встречи, интервью, КП, деки, таблицы и другие рабочие материалы. Затем через source-check / ingest протянуть в текущий Vault-контур те файлы и выводы, которые нужны для дообогащения текущего этапа, чтобы не пропустить значимые уставные документы проекта на старте. Нельзя останавливаться на выводе `в локальном Vault нет` или собирать бедный проектный артефакт только из локального Vault, пока не проверен этот более широкий контур или явно не сказано, что он недоступен.
<!-- agents-norm:С-199:end -->

### С-200. Tool selection rules

<!-- agents-norm:С-200:start -->
- **Client source persist gate:** любой клиентский / проектный source-файл, принесённый в чат или использованный агентом как основание анализа, не должен оставаться только во временной папке приложения, Downloads, `/var/folders`, `/tmp` или другом transient-контуре. До финализации работы агент обязан сохранить значимый source в существующую папку проекта `Источники` / source-pack и обновить существующий реестр источников / артефактов; если файл не переносится, явно зафиксировать no-op причину: дубль, нерелевантность, чувствительность, отсутствие проектной папки, недоступность Drive/Vault или ожидаемый ручной перенос. В финальном ответе показывать статус `source saved`, `duplicate skipped` или `sync gap`.
<!-- agents-norm:С-200:end -->

### С-203. Tool selection rules

<!-- agents-norm:С-203:start -->
- **Mattermost:** через bot-токен (после согласования с Натальей). Голосовые пересказы Ильи — отдельный канал инжеста.
<!-- agents-norm:С-203:end -->

### С-205. Tool selection rules

<!-- agents-norm:С-205:start -->
- **Voice Notes:** через транзитную папку `Vault/20-сырьё/voice-notes/`. Это временный landing zone, не постоянный архив: после разбора записи маршрутизируются по смысловым домам (`50-нормативные-документы/03-стратегия-2026/Личное`, `90-лекции`, проекты 4-ки, нормативный контур, контент, база знаний / Фабрика знаний, Daily Notes / Дарья). Разбор — по классам (см. `ПКМ/05-voice-notes-инжест.md`).
<!-- agents-norm:С-205:end -->
