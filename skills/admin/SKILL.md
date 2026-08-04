---
name: admin
description: Use when Ilya asks to run, design, test, apply, fix, normalize, or check the admin skill / Admin Rail QA / Admin Rail Controller for Paper Planes 4-ка projects, especially before PRE, INIT, PLAN, EXEC, weekly triage, post-meeting, portfolio checker, or next-gate decisions.
---

# Admin Rail QA

## Purpose

Run a manual QA pass over the administrative rail of a 4-ка project. The skill checks whether the project is administratively manageable before C3/C4 attention is consumed: status, owners, artifacts, storage, chat contours, daily rhythm, blockers, and next actions.

The skill can also run controlled writeback when Ilya explicitly asks it to fix or normalize the admin rail. In writeback mode, it first checks readiness for the next project gate, then fixes only evidence-backed administrative gaps. It must not invent project facts, decide strategy, or create artifacts that require human judgment.

Do not turn this into a generic project review. Stay inside the administrator hat: operational connectedness, rules, tempo, organization, and scaffold.

Triage horizon: Paper Planes project triage is primarily weekly. The admin skill must not treat daily task selection as the main triage decision. Daily selection is a breakdown of the weekly triage / схватка, not a replacement for it.

Administrative scale is part of the admin skill. Do not route administrative-scale requests to a separate skill if this `admin` skill is available. The admin skill must know how to create, check, and update the administrative scale, and must verify it on every admin pass.

`admin-scale` is only a temporary scaffold / fallback. The parent `admin` skill owns the canonical administrative-scale behavior. During admin passes, note whether the admin skill reproduced the needed admin-scale behavior without routing to `admin-scale`; after repeated successful reproduction, the scaffold can be proposed for deprecation/removal through skill governance.

## Canonical Project Control Card

Methodological decision: do not require a separate `context.md` file in every project. The useful object is a compact current headquarters control card, not the filename.

Default canonical home:

1. `00-Карточка проекта.md` at the project root — current headquarters view and primary administrative entry point.
2. `Админ-шкала/README.md` — expanded nine-component administrative scale and its operating logic.
3. Existing tracker/backlog — tasks, weekly route, buffer, owners and execution statuses.
4. `Реестр-артефактов.md` — canonical artifact homes and handoffs.
5. Existing decision log / project journal — historical sequence of material decisions.

In Ilya's personal Vault, `context.md` and `<PROJECT>. context.md` are deinstalled as canonical project artifacts. Consolidate their useful contents into `00-Карточка проекта.md`, `Админ-шкала/README.md`, the tracker, artifact register and decision log, then remove the context file after validating the transfer and inbound links. Do not apply this personal-Vault migration policy to Shared Vault or another separately governed Vault without an explicit instruction for that storage contour.

Outside Ilya's personal Vault, `context.md`, `<PROJECT>. context.md`, `README.md`, a Notion project page or another established file may serve as the canonical project card only when the governed contour already uses it as the single headquarters source of truth. Do not create a parallel `context.md` beside a usable `00-Карточка проекта.md`. During an explicitly authorized migration, consolidate current-state blocks into the target canonical card; do not maintain both as competing current-state files.

### Why the project card is not the administrative scale

The artifacts have different jobs:

| Artifact | Management job | Must contain | Must not become |
|---|---|---|---|
| `00-Карточка проекта.md` / canonical context alias | answer in 2–5 minutes what this project is, where it is, what decision/output is next and what blocks it | current identity, ЦКП, governing question, mandate, scope, stage/gate, readiness, current decisions, near-term rhythm, owners/decision contours, blockers and canonical links | full history, atomic evidence warehouse or duplicate task tracker |
| `Админ-шкала/README.md` | define how the project is organized and governed | Цель, Замысел, Политика, Планы, Программы, Задачи, ЦКП, Идеальная картина, Статистики | short status card or event log |
| tracker / backlog | govern execution | tasks, owners, dates/events, outputs, blockers, status and next action | project charter or evidence ledger |
| artifact register | govern storage and handoffs | artifact, owner/home, status, source of truth, input/output route | narrative project summary |
| decision log / journal | preserve audit history | dated decision, source/owner, downstream effect and supersession | current project status |
| Evidence Separation Ledger / evidence trace | govern rights of analytical claims when the project produces material claims | atomic assertion, source/locator, evidence class, use limits and downstream route | universal administrative file required before evidence exists |

### Minimum project-card contract

The canonical project card must show, or explicitly mark as `требует заполнения`:

| Block | Minimum content | Freshness rule |
|---|---|---|
| Identity | project, client/entity, delivery type, stage, status, owner/decision contour, last material update | date must not lag behind the latest material project decision |
| ЦКП | observable project result and beneficiary | must agree with the current mandate and accepted owner interpretation |
| Governing question | management decision/question the project must unlock | a topic label is insufficient |
| Mandate / contract frame | horizon, deliverables, acceptance, confidentiality, commercial/post-project obligations when relevant | physical source and current interpretation remain visibly separate |
| Scope / boundaries | included, excluded, deferred and owner-decided boundaries | silent scope change is forbidden |
| Stage / next gate | current stage, gate, entry evidence, exit criteria and immediate next gate | stage title alone is insufficient |
| Readiness | component-by-component readiness and next evidence for every partial/missing component | headline and row-level count must agree; `8/8` cannot coexist with `7 из 8` without explanation |
| Current operating state | next 7–14 days, key meeting rhythm, blocker #1, enabler, current decisions and next observable output | history and expired dates must not masquerade as current state |
| People / decisions | PP roles, client-side owners, acceptance/decision route and unresolved owner gaps | do not invent owners |
| Canonical links | contract, admin scale, tracker, chat map, source/evidence home, BPM/BPP, problem/SI/BPV and current deliverable when applicable | duplicate or stale homes are drift |
| Recent material changes | compact latest changes with source/decision and downstream effect | keep only the current audit window; long history belongs in the existing journal/log |

The project card is not an evidence source. A fact summarized in it inherits the rights of the named upstream source. Presence in the card does not turn a client statement, hypothesis, external recommendation or agent synthesis into a confirmed fact.

### Update triggers

Refresh the canonical project card when any of the following changes materially:

- contract/mandate interpretation or project boundary;
- delivery type, stage, next gate or readiness;
- ЦКП or governing question;
- owner, acceptance route or current decision contour;
- blocker #1, seven-day enabler or next observable output;
- working calendar / operating rhythm;
- canonical artifact home;
- material source status that changes a project decision, deliverable or gate.

Ordinary claim-level additions that do not change current project control do not require a new card history entry. Record them in the evidence layer and return `project_card_no_change` in the admin/ingest receipt.

### When a separate `context.md` is justified outside the personal Vault

A separate context file is never a canonical project artifact in Ilya's personal Vault. In another governed contour, a separate context file is acceptable only when at least one condition is true:

- the project already established `context.md` as its canonical root card and no competing project card exists;
- the project lives primarily outside the standard Vault structure and needs one portable machine/human handoff snapshot;
- an external agent/runtime requires a generated context export; the export is marked derivative, names its source-of-truth files and is not edited independently;
- a migration is in progress and the temporary coexistence has an owner, end date and consolidation target.

Otherwise classify a proposed additional context file as `parallel_context_drift` and update the existing canonical project card instead. When normalizing Ilya's personal Vault, classify an existing context file as `personal_vault_context_deinstall_required`; preserve useful data in canonical homes and delete the exact file only after a content and inbound-link audit.

### Evidence Separation Ledger applicability

Do not make an Evidence Separation Ledger a universal Day-0 administrative requirement. It becomes applicable when the project starts producing material analytical, causal, numerical, contractual-interpretation, benchmarking or recommendation claims that will enter a client deliverable, decision, project passport, SI/BPV route or implementation gate.

Admin checks only the administrative applicability and landing:

- whether an evidence-rights layer is required now;
- which existing file is its canonical home;
- whether it is linked from the project card and artifact register;
- whether claim/evidence work is blocking the next gate.

The analytical/evidence methodology owns the row-level claim schema and verdicts. Admin must not duplicate the claim ledger inside the project card or administrative scale.

## Source Order

Use existing project files first, then canonical standards.

1. Project-local files:
   - `00-Карточка проекта.md`
   - established `context.md` / `<PROJECT>. context.md` only outside Ilya's personal Vault and only when it is the governed canonical project-card alias
   - `Админ-шкала/README.md`
   - `Админ-шкала/Карта-чатов.md`
   - `Админ-шкала/Реестр-BPM.md`
   - `Админ-шкала/Реестр-артефактов.md`
   - `Админ-шкала/Реестр-респондентов.md`
   - `Админ-шкала/Реестр-интервью.md`
   - `Админ-шкала/Бэклог-задач.md` or `Трекер-задач.md`
   - `Админ-шкала/Ежедневные-статусы/`
   - `Коммуникации/`
   - `README.md` in the project root
2. Canonical references if project files are incomplete:
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/_Регламент-администратора-группы.md`
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/Стандарт шляпы администратора рабочей группы.md`
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/PRE/README.md`
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/INIT/BPP.05.INIT-настройка-админ-шкалы.md`
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/INIT/BPP.10.INIT-организация-хранилища.md`
   - `10-отделы/05-качество-БП/Бизнес-процессы/04-производство/BPP — Административные/INIT/README.md`

If the user gives only a short project or contour name, first perform the Vault preflight from active rules: check project registers, chat maps, project cards, and nearby README files before treating it as a new topic.

## Manual Workflow

### 0. Determine Mode

Default to `review` unless Ilya explicitly asks for `fix`, `writeback`, `normalize`, `создай`, `поправь`, `исправь`, `доведи до канона`, or equivalent.

| Mode | Meaning | File changes |
|---|---|---|
| `review` | Read-only Admin Rail QA and gate readiness card. | No edits. |
| `gate-check` | Read-only readiness assessment for transition to the next project gate. | No edits. |
| `checker` | Manual portfolio/project checker for admin readiness, weekly triage, buffer, and fixable actions. | No edits unless separately requested. |
| `fix-existing` | Fix evidence-backed admin gaps in existing files only. | Existing files only. |
| `normalize` | Bring the admin rail toward canonical 4-ка structure. | Existing files plus missing admin artifacts when explicitly allowed. |

If the user asks to "fix what can be created and corrected", interpret it as `gate-check + conditional normalize`: first assess next-gate readiness; then create or edit only the administrative artifacts that can be filled from existing evidence. Do not fill unknown facts with guesses.

If the user asks for a "checker", "чекер", "портфельный проход", "пройти все проекты", or similar, use `checker` mode, not cron. A checker is manually invoked and produces a report; it does not schedule itself.

### 1. Identify Scope

Determine:

- project;
- stage: `PRE | INIT | PLAN | EXEC | CLOSE | weekly | post-meeting`;
- triage horizon: normally `weekly`; use `daily` only for distribution inside an already selected weekly triage / схватка;
- object being reviewed: admin scale, storage, chat map, interview schedule, task backlog, daily status, StageGate package, or whole admin rail;
- available project-local sources;
- missing context.
- target gate: `PRE->INIT`, `INIT->PLAN`, `PLAN->EXEC`, `weekly triage`, `weekly review`, `daily execution`, `post-meeting follow-up`, `BPV/BND monthly gate`, or other explicitly named gate.

Do not make a long finding about whether an administrator is assigned. If the admin field is absent, record it as a compact context gap and continue with the rail check.

### 2. Run The Four Administrator Contours

Check the project through the four administrator contours:

| Contour | Check |
|---|---|
| Целостность | Scope, commitments, tasks, artifacts, documents, and next actions are connected. |
| Правила | Gates, buffers, BPP/BPM/BPA/BPV logic, storage, naming, and documentation rules are followed. |
| Темп | Tasks move, statuses are current, blockers have owners, enablers arrive on time. |
| Организация | Meetings, quorum, plan-fact, reports, communication channels, and handoffs are visible. |

### 2A. Check Next-Gate Readiness

For every gate-oriented request, produce a clear readiness decision before any writeback:

| Gate | Admin readiness checks |
|---|---|
| `PRE->INIT` | Base documents, first owner, starting storage, respondent/interview setup, data request, start session. |
| `INIT->PLAN` | Project card, admin scale, BPM scope/registry, storage, chat map, tracker, starting corpus, key blockers and owner routes. |
| `PLAN->EXEC` | Accepted scope, delivery rhythm, interview/data schedules, artifact register, owner map, blocker log, next observable steps. |
| `weekly triage` | Project is eligible for the weekly схватка; buffer color/urgency, FullKit/admin readiness, blockers, enablers for 7 days, owner capacity, segment quota, and next weekly deliverable are visible. |
| `weekly review` | Current statuses, plan/fact, overdue items, blockers, decisions needed, updated artifacts and logs. |
| `daily execution` | The daily task is inside an already selected weekly triage / схватка, has owner, output, blocker/enabler, and does not silently introduce a new project priority. |
| `post-meeting` | Decisions, tasks, owners, deadlines, changed artifacts, client/PP follow-up routes. |
| `BPV/BND monthly gate` | Monthly result, client owner/candidate, PP role, rhythm, evidence of change, transfer/de-escalation signal. |

BPM/action-plan scope rule:

- When building or normalizing a project action plan, first derive target BPMs from the signed scope / КП / application and only then map them to the BPM-SI bundle routes. Do not list all useful BPMs as active scope by default.
- The plan must separate `core`, `conditional gate`, and `no-op / phase-2` BPMs, and the roadmap must show why each active BPM is needed for the promised deliverables.
- For management diagnostics, make process analysis, data / Formula Profit, CRM/request trace, target data model, and client-voice gates explicit when the scope touches operating model, regular management, sales/tariffs, regional model, or sale-readiness.
- If the action plan is delivered as a spreadsheet, apply a consistent table style across all used tabs before handoff: visible borders for every used cell, fixed-width week columns, centered identical week markers, frozen/header rows, and no mixed bordered/unbordered table fragments.
- In client-adjacent action-plan spreadsheets, prefer readable business-process names over internal `BPM-N` numbering in visible columns. Put internal outputs / artifacts after the calendar columns, label them as internal and not for client transfer, and keep optional research blocks as conditional / факультативные notes rather than hard commitments.
- In client-adjacent action-plan spreadsheets, write client participants as roles from the org structure rather than personal names unless the user explicitly asks for named scheduling. Start-week alignment meetings should read as simple meetings / kickoff meetings, not over-formal working sessions, when the user wants a lighter client-facing plan.
- Before handing off a client-adjacent action-plan spreadsheet, run a de-AI / client-language pass: replace internal status words such as `core`, `gate`, `baseline`, `gap`, `data-readiness`, `ядро`, and English method labels with plain Russian work language; keep only business abbreviations that are natural for the client context.
- After raw Google Sheets batch updates to a roadmap or meeting-program table, verify edited rows by visible row identity (`№`, track, meeting name), not only by A1 range, because zero-based API indexes can silently place the right text in the neighboring row.

Post-defense chat-map rule:

- When an analytical defense / stage-gate moves a 4-ка project from diagnostic work to implementation launch, update the project chat map as part of the admin writeback.
- Diagnostic chats must not remain the active working rail by inertia. Move them to archive / reference-source status unless the implementation scope explicitly keeps them active.
- Create or update one separate subpassport for each new implementation chat / stream. Each subpassport must include purpose, scope, boundaries, source task(s), return route to штаб, and first working pass.
- Each active implementation chat must map to owner, output, deadline / event, acceptance criteria, sync status, blocker, and next action. If the project uses YouGile, the chat map must name the YouGile / task-sync route instead of legacy Airtable language.
- Do not delete historical chat traces just because the active rail changed; preserve them as audit trail unless Ilya explicitly asks to delete and the content has been moved or is empty.

Gate route:

- `ready`: all blocking admin prerequisites are present.
- `ready_with_caveats`: no S3/S4 blocker, but S2 gaps must be assigned.
- `not_ready`: one or more S3/S4 blockers exist.
- `needs_human_override`: administrative facts exist, but C3/C4/partner judgment is required to accept risk.

In `fix-existing` or `normalize`, only proceed to writeback after classifying the gate. If the project is `not_ready`, you may still fix administrative hygiene that is clearly evidence-backed, but must not mark the gate as passed.

### 2B. Check Weekly Triage And Buffer Logic

Use this section when the request mentions triage, buffer, weekly selection, схватка, project choice, or portfolio focus.

Core rules:

- triage selects projects for the week / схватка, not just tasks for the day;
- started projects should be visible in triage unless explicitly parked, paused, or excluded with a reason;
- weekly triage must respect segment/quota logic when the source system provides segments;
- buffer status is an urgency signal: red projects require immediate attention, yellow require cause/action, green continue controlled monitoring;
- daily task selection must be traceable to a weekly selected project or an explicit emergency/override;
- FullKit/admin readiness affects whether a project is ready for productive work or only for admin normalization;
- enabler for 7 days and blocker #1 must be visible for every selected project;
- do not recommend adding a project to the week if the next observable output is unclear.

For each project under weekly triage, classify:

```yaml
weekly_triage_status:
  in_weekly_triage: yes | no | unknown
  weekly_route: take_to_sprint | monitor | park | unblock_first | escalate
  buffer_status: red | yellow | green | unknown
  urgency_reason:
  seven_day_enabler:
  blocker_1:
  next_weekly_output:
  fullkit_admin_readiness: ready | caveat | not_ready | unknown
  daily_execution_allowed: yes | no | only_admin_fix | needs_override
```

If buffer/triage data is missing, the finding is usually `S2`. If the project is being worked today without a weekly triage route or emergency override, the finding is usually `S3`.

When writeback is allowed, the admin skill must set the triage and buffer status in the project contour. In read-only `review`, `gate-check`, or `checker` mode, it must output the proposed status without writing it.

Status fields to maintain:

```yaml
admin_status:
  weekly_triage_route: take_to_sprint | monitor | park | unblock_first | escalate | unknown
  buffer_status: red | yellow | green | unknown
  buffer_reason:
  blocker_1:
  seven_day_enabler:
  next_weekly_output:
  daily_execution_allowed: yes | no | only_admin_fix | needs_override
  status_set_at: YYYY-MM-DD
  status_source: admin
```

Preferred writeback location:

1. existing triage/buffer/admin-status block in `Трекер-задач.md`;
2. if absent, create or update a compact `Недельный triage / buffer` block in `Трекер-задач.md`;
3. mirror only the gate-critical summary in `00-Карточка проекта.md` when the project gate changes or remains blocked;
4. do not create a new file just to store triage/buffer unless Ilya explicitly asks for normalization.

Status-setting rules:

- `red`: immediate attention needed; S3/S4 blocker, deadline/buffer breach, or active work is impossible without intervention.
- `yellow`: material risk or S2 weakness; work can continue with caveats and assigned owner.
- `green`: admin-ready for the current weekly route; no S2+ admin blocker visible.
- `unknown`: insufficient evidence to calculate buffer; must include what evidence is missing.

Triage route rules:

- `take_to_sprint`: ready for weekly work with clear output and no S3/S4 blocker.
- `unblock_first`: week should remove blocker before delivery/analysis work.
- `monitor`: project remains visible but does not need active weekly capacity beyond control.
- `park`: explicitly paused / not this week / no useful next action.
- `escalate`: needs C2/C3/C4/partner/client decision before normal work.

### 2C. Portfolio Checker Mode

Use `checker` mode when Ilya asks to pass all projects through the admin standard.

Scope:

- scan active project folders under the requested contour, normally `10-отделы/04-производство/Проекты`;
- use only existing project-local files and nearby reports;
- do not create or edit files;
- do not create cron automations unless Ilya explicitly asks for a schedule/reminder/automation.

For each project, output:

```yaml
project_admin_checker_row:
  project:
  stage:
  next_gate:
  admin_readiness: ready | caveat | not_ready | unknown
  weekly_triage_route: take_to_sprint | monitor | park | unblock_first | escalate | unknown
  buffer_status: red | yellow | green | unknown
  blocker_1:
  seven_day_enabler:
  next_weekly_output:
  daily_execution_allowed: yes | no | only_admin_fix | needs_override
  fixable_actions_count:
  human_or_external_required:
  recommended_manual_command:
```

Portfolio checker report must include:

- `take_to_sprint`: projects ready for weekly work;
- `unblock_first`: projects where the week should remove a blocker before delivery work;
- `red_or_yellow_buffer`: projects needing attention by buffer status;
- `unknown_buffer`: projects where buffer cannot be calculated from current evidence;
- `admin_fix_existing_candidates`: projects with safe file-level admin fixes;
- `human_decision_required`: projects blocked by C2/C3/C4/partner/client input.

### 2D. Suggest 5 Acceleration Tasks From The Project Tracker

Use this section during admin operations when a project tracker or backlog is available, especially in `weekly triage`, `daily execution`, `checker`, `gate-check`, `fix-existing`, or `normalize` mode.

Goal: help the administrator accelerate the project without inventing a new project plan.

Rules:

- suggest exactly up to 5 tasks from the existing project tracker / backlog;
- use only tasks already present in `Админ-шкала/Бэклог-задач.md`, `Трекер-задач.md`, project task lists, or an explicitly supplied tracker;
- do not create new tasks in this block unless Ilya separately asks for task creation;
- if Ilya accepts acceleration tasks for registration, route them as `candidate` / `task_delta` to Codex Project Task Inbox with `sync_status=pending_airtable`; do not use CORD Task OS as the primary task home and do not write directly to Airtable without the Inbox handoff;
- do not replace weekly triage with daily task selection: these tasks must either support the weekly route or be marked as proposed accelerators for C2/C3/C4 choice;
- prefer tasks that unlock several downstream actions, remove blockers, complete missing FullKit/admin readiness, clarify owner/decision, produce a next observable output, or reduce senior/admin load;
- avoid tasks that are large, vague, ownerless, not tied to the next gate, or dependent on unavailable client/external input unless their purpose is to unblock that input;
- if the tracker is missing or too stale, say `tracker_not_assessable` and list what tracker evidence is needed.

Selection criteria:

| Criterion | Why it matters |
|---|---|
| `unblocks_work` | removes a blocker or enables multiple next actions |
| `gate_critical` | improves readiness for the named next gate |
| `seven_day_impact` | can materially move the project in the current weekly horizon |
| `owner_clear` | has a visible owner or obvious owner route |
| `output_clear` | produces an observable artifact, decision, status, source, or handoff |
| `low_coordination_cost` | can be started without heavy scheduling or C3/C4 rescue |
| `senior_load_reduction` | reduces future senior review, rework, or scattered questions |

Output format:

```yaml
tracker_acceleration_tasks:
  source_tracker:
  tracker_status: usable | stale | missing | tracker_not_assessable
  selection_logic:
  tasks:
    - rank: 1
      task_id_or_label:
      task:
      task_inbox_route: candidate_task_delta | not_requested
      why_this_accelerates:
      next_observable_output:
      owner_or_owner_route:
      dependency_or_blocker:
      suggested_timing: today | this_week | after_unblock
      risk_if_ignored:
```

If fewer than 5 useful tasks exist, return fewer and explain why. If more than 5 exist, keep the list to the five highest-leverage tasks.

### 3. Check PRE Readiness When Relevant

For PRE or Day 1 INIT, check only the operational evidence:

- base documents received;
- interview participant registry exists;
- interview table exists;
- slots are agreed or blockers are explicit;
- calendar events are ready or pending with owner;
- data request is prepared/sent;
- setup session/start call is either planned or explicitly not needed.

### 3A. Check The Canonical Project Card

Every whole-project admin pass checks the canonical project-control card before the administrative scale:

- identify the single canonical home: `00-Карточка проекта.md`, or outside Ilya's personal Vault an established context alias / explicit temporary home;
- detect competing current-state files and classify them as `parallel_context_drift` unless a migration/end date is recorded;
- verify the minimum project-card contract above;
- compare frontmatter/update date with the latest material decision or journal entry;
- compare headline readiness with row-level readiness;
- distinguish current state from historical log;
- verify that the card points to, rather than duplicates, the administrative scale, tracker, artifact register and evidence layer;
- verify that mandate facts and owner interpretations remain visibly separate.
- in Ilya's personal Vault, verify that no `context.md` variant remains after migration and that Shared Vault was not changed by the deinstallation pass.

Use this status block:

```yaml
project_card_check:
  canonical_home:
  alias_type: standard_project_card | legacy_context | external_portable_snapshot | temporary_migration | unknown
  status: current | usable_with_gaps | stale | missing | competing_sources
  last_material_update:
  latest_project_decision_seen:
  internal_contradictions: []
  competing_current_state_files: []
  evidence_layer_applicable: yes | no | unknown
  evidence_layer_home:
  proposed_updates: []
  writeback_allowed: yes | no
  writeback_done: yes | no
```

Typical findings:

- `project_card_missing` — no compact headquarters entry point exists;
- `project_card_stale` — current fields lag behind material decisions;
- `project_card_internal_contradiction` — stage, readiness, scope, dates or source-of-truth links conflict inside the card;
- `parallel_context_drift` — a separate context file duplicates a usable canonical card;
- `personal_vault_context_deinstall_required` — a context file remains in Ilya's personal Vault and must be migrated into canonical homes before exact-file deletion;
- `project_card_history_overload` — long chronology obscures current state and should remain in the existing journal/log;
- `project_card_claim_overreach` — the card upgrades a hypothesis, client statement or recommendation beyond upstream evidence rights.

### 4. Check Admin Scale

For `BPP.05.INIT`, check:

- `Админ-шкала/` exists or the project card explicitly holds a temporary admin-scale section;
- `README.md` exists;
- timeline covers INIT;
- team register exists;
- chat map exists;
- artifact register exists;
- respondent and interview registers exist when interviews are in scope;
- task backlog/tracker exists;
- daily statuses exist for active INIT days;
- 9 admin-scale components exist: цель, замысел, политика, планы, программы, задачи, ЦКП, идеальная картина, статистики;
- C2 acceptance is recorded when required.
- if the project may use retail, CRM, BI, transaction, survey, or customer behavior data, a compact data-reuse preflight is captured or explicitly marked `not_applicable`.

Administrative scale has 9 components:

| Component | Meaning | Admin check |
|---|---|---|
| `Цель` | what must be achieved | target state is explicit and project-relevant |
| `Замысел` | why this should exist and whose benefit it maximizes | purpose is not just a task description |
| `Политика` | boundaries, rules, and operating principles | constraints, refusals, and work principles are visible |
| `Планы` | timing, scope, cadence, sequence | horizon, rhythm, and gate sequence are stated |
| `Программы` | change mechanisms or workstreams | mechanisms are separated from immediate tasks |
| `Задачи` | concrete actions, owners, and near-term execution | tasks have owner / next step / output where evidence allows |
| `ЦКП` | valuable final product | final valuable product is observable and tied to beneficiary |
| `Идеальная картина` | how success looks in observable terms | success scene can be checked, not only imagined |
| `Статистики` | leading and lagging indicators | at least minimal progress / result indicators exist or are marked missing |

Data-reuse preflight is not a deep analytics task for C1/C2. It is a short set of factual questions that lets Rail / BPM Exchange later evaluate reuse potential without rediscovering the project from scratch:

```yaml
data_reuse_preflight:
  применимо: да | нет | неизвестно
  объект_анализа: конечный потребитель | клиент_B2B | SKU | канал | регион | другое | неизвестно
  есть_клиентская_база_продаж: да | нет | неизвестно
  есть_SKU_или_товарная_детализация: да | нет | неизвестно
  есть_повторные_покупки: да | нет | неизвестно
  есть_идентификатор_покупателя: да | нет | неизвестно
  есть_канал_покупки: да | нет | неизвестно
  есть_маржа_или_proxy_экономики: да | нет | неизвестно
  связанные_BPM: []
  кто_подтверждает_факты: C1 | C2 | C3 | клиент | неизвестно
```

This block only prepares evidence for later machine checks. Do not turn it into a full donor/reuse verdict during ordinary admin-scale setup unless Ilya explicitly asks or the project is at pre-defense / gate change.

### 4A. Create Or Update Admin Scale

Use this section when Ilya asks to create, update, normalize, fix, or apply an administrative scale, or when the project admin rail has no usable admin scale and writeback is allowed.

Core rules:

- first use existing files and evidence;
- do not create a new admin-scale file unless Ilya has allowed creation or asked for normalization that includes missing canonical admin artifacts;
- if `Админ-шкала/README.md` exists, update it as the preferred admin-scale home;
- if no admin-scale file exists but `00-Карточка проекта.md` has a temporary admin-scale section, update that section;
- if neither exists and creation is not allowed, output `admin_scale_missing` and propose creation instead of creating it;
- unknown facts must be marked as `требует заполнения`, not invented;
- distinguish `Программы` from `Задачи`: programs are work/change mechanisms; tasks are immediate actions;
- make `ЦКП`, `Идеальная картина`, and `Статистики` observable.

When creating or updating an administrative scale, use this structure:

```markdown
## Административная шкала

### Цель

### Замысел

### Политика

### Планы

### Программы

### Задачи

### ЦКП

### Идеальная картина

### Статистики
```

### 4B. Mandatory Admin-Scale Refresh On Every Admin Pass

Every admin pass must include an admin-scale check, even if the user asked about another admin operation.

In read-only modes (`review`, `gate-check`, `checker`):

- report whether the administrative scale is present, complete, stale, or missing;
- identify the most important missing or stale component;
- propose updates, but do not write.

In writeback modes (`fix-existing`, `normalize`):

- update existing administrative-scale fields when evidence is available;
- add `требует заполнения` for required but unknown fields only when editing an existing admin-scale artifact;
- do not mark the admin scale complete unless all 9 components are usable;
- if a project gate changes or weekly route/buffer changes, refresh at least `Планы`, `Задачи`, `Статистики`, and, if needed, `Политика`.

Use this status block:

```yaml
admin_scale_check:
  home:
  status: complete | usable_with_gaps | stale | missing | not_assessable
  missing_or_stale_components: []
  proposed_updates: []
  parent_admin_reproduced_scale_behavior: yes | no | not_assessable
  admin_scale_scaffold_needed: yes | no | not_assessable
  writeback_allowed: yes | no
  writeback_done: yes | no
```

### 5. Check Storage And Source Of Truth

For `BPP.10.INIT`, check:

- root project storage exists;
- README/pasport exists;
- canonical name, owner, stage/status/scope source of truth, project boundary, and layer are explicit;
- first-level structure is present;
- BPM folders match BPM scope, not all possible BPMs mechanically;
- raw sources, working synthesis, and deliverables are separated;
- input documents were moved from PRE holding areas;
- rights/access notes are recorded when visible;
- Problem Map / SCQA and storyline/storyboard are linked if they exist.

### 6. Check Chat Map And Communication Contours

Check:

- `Штаб проекта` is the first and main decision contour;
- `Внутренний PP / проектная сборка` exists as internal assembly contour for mining/analysis where relevant;
- each chat has purpose, status, participants, boundaries, linked BPM/scope, and decision-return route;
- no already active chat remains in status `предложен` or `рекомендован`;
- decisions from working chats have a route back to штаб;
- there is a task to publish or confirm the chat map when required.

### 7. Check Daily Rhythm And Blockers

Check:

- latest daily status / plan-fact exists;
- tasks have owner, deadline or next step;
- blockers have owner and escalation route;
- meetings have protocols or decision logs;
- new artifacts are registered;
- unresolved questions to C3/C4/partner are batched, not scattered;
- overdue or hanging items are visible.

### 8. Route Findings

Use severity:

- `S0`: no issue, hide from senior;
- `S1`: small improvement, keep with admin/author;
- `S2`: material weakness, owner must fix or accept risk;
- `S3`: blocker, do not pass to next gate without fix or explicit override;
- `S4`: stop/governance breach, hold/escalate.

Use route:

- `accept`;
- `accept_with_caveats`;
- `revise`;
- `hold`;
- `reject`;
- `escalate`.

Senior/C3/C4 should see only S2+ and no more than 3-5 findings.

### 8A. Separate Fixable Actions From External Blockers

Every admin pass must explicitly separate:

- `fixable_now`: administrative corrections the agent can make from existing evidence if writeback is allowed;
- `create_if_allowed`: missing admin artifacts the agent can create if the user permits new files;
- `human_or_external_required`: blockers that require client data, C2/C3/C4/partner judgment, scheduling approval, or strategic decision.

This is mandatory even in read-only `review` or `gate-check` mode. In read-only mode, present these as proposed actions, not performed actions.

Fixable actions must be concrete and file-level:

- file to change;
- exact admin defect;
- evidence source;
- proposed edit;
- why it reduces senior/admin load;
- whether it is safe to do without human judgment.

Use this structure:

```yaml
fixable_actions:
  - action:
    target_file:
    defect:
    evidence:
    proposed_fix:
    safe_without_human_judgment: yes | no
    mode_required: fix-existing | normalize
```

Do not end an admin pass with only "hold", "revise", or blockers. Always show what the agent can clean up immediately and what remains genuinely blocked.

### 9. Controlled Writeback Rules

Only run this section in `fix-existing` or `normalize`.

Before editing, state briefly which files will be touched and why.

Allowed in `fix-existing`:

- update statuses in an existing tracker, interview register, artifact register, project journal, project card, or admin-scale file;
- set or update weekly triage route and buffer status in the existing tracker / project card;
- move known blockers from scattered tasks into an existing blocker/status section;
- add missing owner / next action / route when already evident from project files;
- add explicit no-op reasons where active rules require an update but evidence says no change is needed;
- update links between existing admin artifacts.

Allowed in `normalize` when Ilya explicitly permits creation:

- create one missing root `00-Карточка проекта.md` only when no canonical project card/context alias exists and the user authorized normalization with file creation;
- create missing canonical admin artifacts under `Админ-шкала/`:
  - `README.md`;
  - `Карта-чатов.md`;
  - `Реестр-BPM.md`;
  - `Реестр-артефактов.md`;
  - `Реестр-респондентов.md`;
  - `Реестр-интервью.md`;
  - `Ежедневные-статусы/` and the current daily status file;
- create only files whose content can be initialized from existing project evidence;
- if evidence is insufficient, create a sparse scaffold only when the user explicitly requested canonical normalization, and mark unknown fields as `требует заполнения`, never as facts.

Never write:

- strategic decisions, BPM scope acceptance, client commitments, or C3/C4 overrides;
- client communications or meeting schedules without human approval;
- fake completion statuses;
- inferred facts without evidence.

After writeback, return:

- gate readiness route before and after fixes;
- files changed or created;
- remaining S2/S3 blockers;
- what still requires human judgment.

## Output Format

Use this structure by default:

```yaml
admin_rail_review_card:
  project:
  stage:
  reviewed_object:
  mode: review | gate-check | checker | fix-existing | normalize
  triage_horizon: weekly | daily_execution | not_applicable
  target_gate:
  gate_readiness: ready | ready_with_caveats | not_ready | needs_human_override
  weekly_triage_status:
    in_weekly_triage:
    weekly_route:
    buffer_status:
    seven_day_enabler:
    blocker_1:
    next_weekly_output:
    daily_execution_allowed:
  route: accept | accept_with_caveats | revise | hold | reject | escalate
  readiness_summary:
  top_findings:
    - finding:
      severity: S1 | S2 | S3 | S4
      contour: целостность | правила | темп | организация
      evidence:
      owner:
      next_action:
      route_if_not_fixed:
  missing_artifacts:
  ownerless_or_hanging_items:
  fixable_actions:
    - action:
      target_file:
      defect:
      evidence:
      proposed_fix:
      safe_without_human_judgment:
      mode_required:
  create_if_allowed:
    - artifact:
      why_needed:
      source_evidence:
      scaffold_or_full:
  human_or_external_required:
    - blocker:
      owner:
      needed_decision_or_input:
  tracker_acceleration_tasks:
    source_tracker:
    tracker_status:
    selection_logic:
    tasks:
      - rank:
        task_id_or_label:
        task:
        why_this_accelerates:
        next_observable_output:
        owner_or_owner_route:
        dependency_or_blocker:
        suggested_timing:
        risk_if_ignored:
  chat_map_status:
  admin_scale_status:
  project_card_check:
    canonical_home:
    alias_type:
    status:
    last_material_update:
    latest_project_decision_seen:
    internal_contradictions:
    competing_current_state_files:
    evidence_layer_applicable:
    evidence_layer_home:
    proposed_updates:
    writeback_allowed:
    writeback_done:
  admin_scale_check:
    home:
    status:
    missing_or_stale_components:
    proposed_updates:
    writeback_allowed:
    writeback_done:
  storage_status:
  daily_rhythm_status:
  escalation_needed:
  human_judgment_required:
  next_review_trigger:
  writeback_plan:
    will_edit_existing:
    will_create:
    blocked_from_writing:
  writeback_result:
    changed_files:
    created_files:
    remaining_blockers:
```

After the YAML card, add a short human-readable summary in Russian:

- what is ready;
- what blocks movement;
- which 5 tracker tasks most accelerate the project, if a usable tracker exists;
- whether the administrative scale exists, is current, and what must be refreshed;
- what to return to admin/author;
- what the agent can fix immediately if writeback is allowed;
- what C3/C4 must decide, if anything.
- what was fixed or deliberately left unfixed, if the mode included writeback.

## Boundaries

Do:

- inspect existing files before advising;
- check the administrative scale on every admin pass;
- create or update the administrative scale when explicitly allowed and evidence-backed;
- return bad admin input before senior review;
- prepare drafts of messages, tasks, checklists, status cards, and escalation packets;
- propose missing files in read-only mode, and create/update them only when user asks for writeback or normalization;
- evaluate readiness for the next project gate before editing in writeback mode;
- fix existing administrative files when the user explicitly asks to correct what can be corrected;
- keep findings evidence-based and tied to project artifacts.

Do not:

- make strategic decisions;
- decide BPM scope for C3;
- contact the client autonomously;
- schedule or cancel meetings without human approval;
- modify Vault files unless the user asked for writeback, fix, or normalization;
- create a new administrative-scale file unless creation is explicitly allowed by the user or by normalize mode with missing admin artifacts approved;
- evaluate expert quality of analytical conclusions except where admin evidence is missing;
- create a noisy list of nits for C3/C4.

## Skill Improvement Notes

This first version is manually run. Future versions may add scripts for deterministic checks:

- admin-scale structure parser;
- chat-map status checker;
- artifact-register completeness checker;
- daily-status freshness checker;
- storage/source-of-truth checker.
