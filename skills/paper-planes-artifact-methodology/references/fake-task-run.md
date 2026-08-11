# Fake Task Run

Date: 2026-08-11

Purpose: test `paper-planes-artifact-methodology` on realistic fake Paper Planes tasks before installation.

## Task 1: Commercial Proposal

Prompt: "Нужно собрать структуру КП для новой услуги по управленческим дашбордам для B2B-дистрибьютора."

Expected behavior:

- Trigger this skill.
- Select ABCD, RDB, JTBD, SCQA, Formula of Profit, KPI tree, evidence ledger.
- MECE required for offer blocks, dashboard sections, and proof structure.
- Frappe check required before final reusable methodology wording.
- Route final КП production to `commercial-proposal-generator`.

Dry-run result: pass.

Reason: router covers commercial proposal, dashboard/economics, and adjacent-skill handoff.

## Task 2: Mermaid Hypothesis Tree

Prompt: "Сделай Mermaid-дерево гипотез, почему у клиента падает маржа по каналам."

Expected behavior:

- Trigger this skill because Mermaid, hierarchy, hypotheses, and economics are present.
- Select MECE, issue tree, hypothesis tree, Formula of Profit, contribution margin, pocket price waterfall.
- MECE required.
- Frappe check useful but not required for a quick draft if methodology detail is not disputed.
- Route production only if the user wants a final diagram artifact.

Dry-run result: pass.

Reason: MECE and tree logic are mandatory in both `SKILL.md` and `methodology-router.md`.

## Task 3: Simple File Operation

Prompt: "Переименуй файл `draft.md` в `final.md`."

Expected behavior:

- Do not trigger this skill.
- No methodology preflight.
- No Frappe check.
- No MECE.

Dry-run result: pass.

Reason: `eval-cases.md` includes pure file operation as a bad trigger.

## Task 4: Project Operating Instruction

Prompt: "Сделай постоянную инструкцию для проекта: как оформлять еженедельный статус."

Expected behavior:

- Trigger this skill only as methodology/source/writeback guard.
- Read `md-instruction-workflow.md`.
- Ask for explicit confirmation before creating a durable instruction if confirmation is not already clear.
- Prefer local `instructions/` only in a known project folder.
- Select SCQA, governance cadence, issue/risk/action/owner register if the status includes risks and next actions.

Dry-run result: pass.

Reason: writeback gate is explicit.

## Task 5: Frappe Knowledge Check

Prompt: "Проверь в БЗ Frappe, как у нас описан CJM, и сделай структуру интервью."

Expected behavior:

- Trigger this skill.
- Try live/authenticated Frappe verification.
- If guest access redirects to login, label status as authentication-required, not missing.
- Select CJM, JTBD, jobs map, issue tree, interview logic.
- Route interview production to `interview-brief-by-analogs` if final interview guide is requested.

Dry-run result: pass with access limitation.

Reason: live guest request to `https://lms.paper-planes.ru/knowledge/glavnaya` redirects to login; current rules cover this as authentication-required.

## Task 6: Ambiguous Packaging

Prompt: "Красиво упакуй структуру проекта для клиента."

Expected behavior:

- Trigger this skill because artifact type is unclear and methodology may affect client-facing output.
- Ask or state a safe assumption about format: presentation, one-pager, project-control document, or instruction.
- Select SCQA and MECE as likely defaults; add RACI/risk register only if this is governance.
- Do not jump directly to slide production or write a durable instruction.

Dry-run result: pass.

Reason: ambiguous-trigger eval requires clarification or safe assumption.

## Task 7: Dashboard Brief

Prompt: "Спроектируй дашборд продаж: какие вкладки, метрики, фильтры, владельцы."

Expected behavior:

- Trigger this skill.
- Select Formula of Profit, KPI tree, metric hierarchy, leading/lagging indicators, owner/control rhythm.
- MECE required for tabs, filters, metric tree, and owner matrix.
- Route implementation to dashboard/spreadsheet/BI skill if the user asks to build it.
- Frappe check required before reusable dashboard methodology or client-facing methodology note.

Dry-run result: pass.

Reason: dashboard route is covered in router, model catalog, and eval cases.

## Task 8: Source Conflict

Prompt: "В клиентском файле структура одна, в Frappe методологии другая, а я сейчас прошу третью. Что брать?"

Expected behavior:

- Apply source hierarchy.
- Latest user instruction wins if explicit and safe.
- Frappe remains global methodology canon.
- Client file remains project-specific artifact.
- Stop and ask if the conflict changes client promise, acceptance criteria, or meaning.

Dry-run result: pass.

Reason: source hierarchy and stop condition are explicit in `SKILL.md`.

## Summary

| Task | Result | Main check |
|---|---|---|
| Commercial Proposal | pass | adjacent skill handoff and methodology stack |
| Mermaid Hypothesis Tree | pass | MECE and economics |
| Simple File Operation | pass | bad trigger avoidance |
| Project Operating Instruction | pass | writeback gate |
| Frappe Knowledge Check | pass with access limitation | authentication-required handling |
| Ambiguous Packaging | pass | no premature artifact assumption |
| Dashboard Brief | pass | metrics, owners, MECE |
| Source Conflict | pass | hierarchy and stop condition |

Overall result: pass.

Installation readiness: ready for manual install after the package is moved into the active skills directory.
