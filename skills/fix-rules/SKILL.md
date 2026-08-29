---
name: fix-rules
description: >-
  Use when Ilya asks to "fix rules", "почини правила", "добейся исполнения
  правил", "проверь отставание от правил", "что не соответствует текущим
  правилам", or wants an audit of the current chat and only the documents that
  belong to that chat context against the current Vault/Codex rule layer. By
  default the skill is chat-local, not project-wide, folder-wide, or
  runtime-wide. It performs only one operation class: detect where the current
  chat context and its directly related artifacts lag behind the current rules,
  automatically fix in-scope rule noncompliance, and ask for accept only when
  the fix is ambiguous, out of scope, external, or touches protected rule layers.
  If the request may be either about the current chat or the whole project,
  explicitly choose or ask between two modes: chat-rule-drift and
  project-rail-drift.
---

# Fix Rules

## Purpose

Audit the current chat context against the current rules. Do not audit the whole project, folder, Vault, or runtime layer unless Ilya explicitly asks for that wider scope. Do not do broad refactoring, content rewriting, or silent cleanup. The output is a compact chat-local drift report and a proposed fix set.

## Mode Router

`fix-rules` and `rail` are one drift-audit family. The user-facing logic should feel like one skill with two modes, not two unrelated tools.

Use `chat-rule-drift` mode when the request is about whether the current chat, its direct artifacts, or the agent behavior complies with active rules.

Typical triggers:

- `fix rules`, `почини правила`, `добейся исполнения правил`;
- `что не соответствует правилам`;
- `проверь отставание от правил`;
- a created chat, subpassport, tracker row, local artifact, automation, hook, or skill may violate current rules;
- the user asks about the agent's process, not the whole project operating system.

Use `project-rail-drift` mode when the request is about the state of a 4th-department production project as an operating system. This mode may delegate the detailed project inspection to `rail`, but the routing question remains part of the same drift-audit family.

Typical triggers:

- `/rail`, `проверь рельсу`, `что с проектом`, `инспектируй ход проекта`;
- the question is about project status, project chats, штаб route, BPM/BPP movement, owners, deadlines, task rail, stage gates, or methodology fit;
- the user asks to reconstruct or repair the actual project rail across multiple project artifacts.

If both modes seem relevant:

1. Start with `chat-rule-drift` only if the immediate problem is a local rule violation in the current chat.
2. Escalate to `project-rail-drift` only when the fix requires understanding the whole project rail.
3. If unclear, ask Ilya one short question: `Это скорее про текущий чат/локальные правила или про рельсу всего проекта?`
4. If inside an auxiliary/service project chat, do not run full Rail there; report the allowed launch point and the штаб route.
5. Do not silently run both. Say which mode is active and why.

Project-status passers, closeouts, `rail`, `summary`, and project preflights should recommend this drift-audit family when they see stale status, owner gaps, broken handoff, missing next step, rule drift, or project rail ambiguity.

## Non-Negotiables

- Treat this as `REVIEW -> PROCESS`, not content production.
- Do not create files unless Ilya explicitly asks for a file or the missing file is required by an active in-scope rule with an unambiguous target artifact.
- Fix in-scope noncompliance immediately when the rule, target artifact, and correction are clear.
- Do not edit project artifacts, `AGENTS.md`, `.codex/rules`, automation configs, or the rule cart without explicit accept after the drift report, except for in-scope rule noncompliance in ordinary project/chat artifacts.
- Never auto-edit normative/rule layers (`AGENTS.md`, `.codex/rules`, skill files, automation configs, rule cart) from `fix-rules` unless Ilya's current message explicitly asks to change that rule/process layer.
- Use existing files first, but only those directly belonging to the current chat context.
- Default scope is `chat-local`. Project-wide, folder-wide, workspace-wide, recovery-wide, or runtime-wide checks are forbidden unless Ilya explicitly says "по проекту", "по папке", "по Vault", "по runtime", "по автоматизациям", "по хукам", "широко", or equivalent.
- If a global/runtime rule appears relevant but is not directly tied to this chat context, mention it only as `out of scope`, not as drift.
- If a rule is newer than the chat artifact, distinguish `outdated because rule changed` from `noncompliant even under old rules`.
- Do not reduce "rules" to markdown registries, but check executable layer only when the current chat context directly owns or references a hook, automation, skill, manifest, script, or recovery document.

## Rule Sources

Read only what the chat-local task needs, in this order:

1. Always-loaded rules visible in the current prompt and `~/.codex/AGENTS.md`.
2. Root `CLAUDE/AGENTS.md`, if the workspace is inside the Vault.
3. `.codex/rules/*.md` and/or `CLAUDE/.Codex/rules/*.md` when present.
4. `ПКМ/картотека-правил.yaml`, `ПКМ/картотека-лог.md`, `ПКМ/hot.md` only for rule history, recency, and status.
5. Chat-local control artifacts: chat map row, chat subpassport, chat-specific tracker rows, chat-specific README/brief, and only the relevant slices of broader project artifacts.
6. Runtime/control layer only when the current chat context directly owns or references executable behavior:
   - `~/.codex/automations/*/automation.toml` and memory files;
   - `CLAUDE/Codex/Автоматизации — active.yaml` or similar active manifests;
   - `~/.codex/skills/*/SKILL.md` and skill registries;
   - hook directories such as `.Codex/hooks/`, `.codex/hooks/`, `.claude/hooks/`, `CLAUDE/.Codex/hooks/`;
   - scripts or recovery docs explicitly named by the rule.

Avoid broad scans across the project, Vault, `.codex/cache`, `.codex/sessions`, build outputs, attachments, raw archives, or automation directories unless Ilya explicitly scopes the audit there.

## Scope Discipline

Default mode is `chat-local`.

Allowed in default mode:
- current chat role and row in `Карта-чатов.md` / реестр чатов;
- chat subpassport, if it exists;
- direct source documents named by the chat map for this chat;
- only the relevant rows/sections of broader files, such as BPM rows attached to this chat;
- executable artifacts only if this chat explicitly owns or references them.

Forbidden in default mode:
- auditing all project files;
- auditing `Codex/Автоматизации — active.yaml`;
- comparing all runtime automations;
- scanning hooks globally;
- checking unrelated project skeleton components;
- reporting workspace/recovery drift as if it belonged to the chat.

Escalate scope only if Ilya explicitly asks for a wider pass. Name the escalation in the preflight.

## Workflow

1. **Preflight**
   - Identify the target as the current chat by default.
   - Identify the scope: `chat-local` unless Ilya explicitly requested wider scope.
   - Identify the layer: usually `chat artifact`; use `runtime`, `automation`, `hook`, `skill`, or `recovery` only if directly owned/referenced by the chat or explicitly requested.
   - If inside `Vault/10-отделы/04-производство/Проекты/<project>`, mark the target as a 4th-department project but still keep the audit chat-local.
   - State allowed operations: audit, drift classification, proposed fixes.
   - State forbidden operations: silent edits, new files, broad rewrite, unrelated cleanup, project-wide scan, runtime-wide scan.

2. **Build the Current Rule Set**
   - Extract only rules relevant to the current chat and its directly related artifacts.
   - Mark each rule as `chat-local`, `4ka-chat`, `project-context-needed`, or `out-of-scope`.
   - Mark each in-scope rule by fix mode:
     - `fix-now`: the artifact violates a current rule and the correction is clear inside the current scope. Examples: created project chat lacks a separate chat subpassport; chat map row status contradicts confirmed state; created chat lacks a parent штаб route; touched frontmatter/YAML is invalid.
     - `accept-needed`: the situation may require judgement, changes meaning/scope/owners/deadlines/statuses, affects normative/rule layers, touches external systems, or could create substantial new content.
   - Prefer current always-loaded rules over older summaries.

3. **Inspect the Target**
   - Read chat control artifacts before content artifacts.
   - For project/chat routing, check maps and registries first: `Карта-чатов.md`, реестр чатов, карта коммуникаций, chat subpassports.
   - Read broader project files only by narrow slice: the row/section that names this chat, its BPM/scope rows, or the explicit parent штаб route.
   - For executable drift, compare rule intent with live implementation only if this chat directly owns or references the executable artifact.
   - Record the exact artifact and line or section that appears stale.

4. **Classify Drift**
   Use these statuses:
   - `violates-current-rule`: artifact or workflow contradicts an active rule.
   - `missing-required-artifact`: current rules require an existing artifact/update that is absent.
   - `stale-after-rule-update`: artifact was reasonable before, but a newer rule changed the required behavior.
   - `ambiguous-scope`: rule may apply, but target/project scope is unclear.
   - `runtime-missing`: chat-owned rule requires a hook, automation, skill, manifest, or script, but no executable implementation is found.
   - `runtime-stale`: chat-owned implementation exists but does not match the current rule or active manifest.
   - `chat-context-misclassified`: current chat role is unclear or contradicts the project chat map.
   - `out-of-scope`: possible issue exists but belongs to project-wide/runtime-wide audit, not this chat.
   - `no-op`: checked and no change is needed.

5. **Choose Fix Mode**
   - `fix-now`: default for all in-scope `violates-current-rule`, `missing-required-artifact`, `stale-after-rule-update`, `runtime-missing`, or `runtime-stale` items when the target and correction are unambiguous.
   - `accept-gate`: use for `ambiguous-scope`, `out-of-scope`, any wider-scope change, any normative/rule-layer change unless Ilya explicitly asked to edit that layer, and any change that could alter project meaning, owners, deadlines, status, scope, or external commitments.
   - If a drift item clearly violates a rule but the landing place or intended correction is ambiguous, do not invent a correction. Classify it as `ambiguous-scope` and ask for accept.
   - Fixes must still be reported after the patch with changed files and verification.

## 4th-Department Project Add-On

Run this add-on whenever the current path or target is inside `Vault/10-отделы/04-производство/Проекты/` or the user says the target is a project of the 4th department / production. The add-on is still chat-local by default.

1. **Determine the chat role first**
   - Check `Админ-шкала/Карта-чатов.md`, `Карта-чатов.md`, реестр чатов, project card, trackers, and subpassports.
   - Classify the current chat as exactly one of:
     - `main штаб-проекта`: central management contour; decisions, statuses, deadlines, escalations, scope.
     - `main internal-pp-сборка`: internal PP contour; hypotheses, storyline, storyboard, deliverable review, methodology assembly.
     - `auxiliary субпроектный чат`: subject working contour such as HR/interviews, data/MIS/economics, patient path, market/strategy.
     - `unknown`: no registry evidence found.
   - If the chat is auxiliary, state the parent штаб route and what must be escalated back there.

2. **Check only chat-relevant 4ka rule families**
   - Chat map row and status for this chat.
   - Chat subpassport / стартовое сообщение for this chat, if the chat is created.
   - BPM rows directly linked to this chat.
   - Parent штаб route and escalation rules.
   - Chat-specific tracker rows or tasks, if they already exist.
   - Interview/source handling only if this chat is an interview/source chat.
   - Runtime/hooks/automation only if this exact chat or its row requires them.

   Do not check project skeleton, FullKit, whole admin scale, whole project tracker, whole BPM-status block, or all automations unless Ilya explicitly expands the scope.

2a. **Check BPM-2 / BPM-3 interview-monitor drift when in scope**
   - For an interview/source chat, project штаб, or an explicit interview-control audit, verify that the current Rail monitor reconciles `planned respondent/role/client/segment -> ClickUp Call Recorder or documented Granola fallback -> BPM source ID -> evidence writeback`.
   - Flag as `runtime-missing` or `runtime-stale` when the recurring monitor is absent, paused without an owner decision, still depends on Notion, counts notes instead of physical meetings, checks only total interview count, omits named/role/segment coverage, or sends repeated unchanged alerts.
   - Flag as `violates-current-rule` when Granola is treated as primary without a documented ClickUp impossibility, one meeting is double-counted, BPM-3 is routed through Cynefin/Estuarine/9-actions, or the notification automation mutates ClickUp project fields.
   - The required alert route is: new or materially changed deviations to Ilya in the project штаб heartbeat; real deviations also receive one deduplicated assigned ClickUp comment to Natalia Tokaeva. A green or unchanged check must not create an external comment.
   - Verify the alert schema contains: `Код отклонения | Проект | BPM | Респондент / роль или клиент / сегмент | Ожидаемое состояние | Фактическое состояние | Возраст отклонения | Физический источник | BPM source ID | Требуемое действие | Ответственный контур | Дедлайн устранения`.
   - Keep ClickUp notification authority comment-only with `notify_all=false`. Any status, assignee, deadline, priority, type, parent, description, custom-field, list, doc, or other mutation still requires the normal exact-change-set approval gate.
   - Check topology against the chat map: exactly one heartbeat per physical chat aggregating BPM-2 and/or BPM-3; one combined heartbeat when both BPMs share a chat; never one per respondent, source, slot, or BPM. A temporary штаб fallback is valid only while no physical interview chat exists. Concurrent штаб and subject-chat monitors for the same scope are `runtime-duplicate` and must be consolidated.
   - A newly included BPM-2/BPM-3 scope without a created or verified heartbeat is `missing-required-runtime`, not a future recommendation. If the target thread cannot be resolved, report `runtime-missing: target thread not resolved` and keep the project gate incomplete.

3. **Report 4ka-specific drift separately**
   - Do not mix chat-local drift with global/project/runtime drift.
   - For each drift item, say whether it affects this chat, parent штаб handoff, or a direct chat artifact.

5. **Output in Chat**
   Use this structure:

   ```text
   fix-rules preflight:
   target:
   scope:
   target layer:
   chat role:
   rule sources checked:
   chat sources checked:
   broader sources sliced:
   not doing:

   Chat-local drift:
   | status | artifact | rule | enforcement | what lags | fix / proposed fix | needs accept |

   Fixed now:
   | artifact | fix | verification |

   Out of scope noticed:
   | item | why out of scope | how to request it |

   Recommended next move:
   ```

   Keep the table short. Group minor repeats instead of listing every duplicate line.

6. **Propose Fixes**
   - Propose the smallest useful patch set.
   - Separate `fixed now`, `needs accept`, `good to fix`, and `leave as-is`.
   - Execute `fixed now` items immediately when they are in scope and unambiguous.
   - Ask for or rely on explicit accept before editing `needs accept` and `good to fix` items, unless Ilya already said to fix.

### Structured analytical artifact drift

When the current scope owns a problem map, issue/hypothesis tree, MECE partition, evidence/claim/source-to-node matrix, analytical Mermaid, storyline-storyboard, metric tree, or dimension architecture, check the cross-cutting standard in `~/.codex/AGENTS.md`. Treat missing model fields, false MECE claims, Frappe-as-blocker, methodology used as client evidence, missing source trace, duplicate parallel artifacts, and full rewrites without delta evidence as `violates-current-rule` or `stale-after-rule-update`. Do not expand this into a project-wide audit unless the user explicitly requested that scope.

7. **After Fix Or Accept**
   - Patch only existing files unless Ilya explicitly requested new files.
   - Exception: create a missing artifact when an active rule requires that exact artifact in the current scope, such as a separate subpassport for a created project chat.
   - Verify parsable formats after editing: YAML/frontmatter with Ruby safe YAML where relevant.
   - Report changed files and verification.

## Output Rules

- Be concrete: name files and sections, not just abstract policies.
- Do not overwhelm Ilya with every rule in the system.
- If nothing is stale, say `fix-rules: отставаний не найдено` and list what was checked.
- If the audit was partial, say exactly what was not checked and why.
- When the target is a 4ka project, always state the chat role even if no drift is found.
- When hooks/automations are not chat-owned, say `runtime not checked: out of chat-local scope`.

## Common Failure Modes

- Starting content work instead of rule drift audit.
- Treating a project-local map as optional when a global rule now requires a preflight.
- Updating the rulebook but forgetting project artifacts that now lag behind it.
- Reporting global runtime/recovery drift during chat-local audit.
- Leaving clear in-scope rule noncompliance unfixed while asking for accept.
- Auto-fixing nuanced, semantic, external, or normative changes that require accept.
- Confusing "rule should exist" with "project artifact violates rule"; this skill checks compliance, not new rule design.
- Treating an auxiliary project chat as the штаб or internal PP assembly chat.

## Writeback / Approval Gate

This skill is high-risk because it can touch rule layers, AGENTS.md, local skill behavior, project compliance artifacts, hooks, automations, and normative process language.

The default output is a drift report plus proposed fixes. Do not edit rules, skills, AGENTS.md, hooks, automations, project statuses, owners, deadlines, or meaning-bearing artifacts unless Ilya explicitly approves the exact change set. If the fix is semantic, normative, external-facing, project-wide, runtime-wide, or ambiguous, stop at preview/diff and ask.
