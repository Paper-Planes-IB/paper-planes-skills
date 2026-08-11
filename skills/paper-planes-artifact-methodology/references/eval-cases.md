# Eval Cases

Use these cases for reasoning-only dry runs unless the user asks for live tool tests.

## EVAL-001 Good Trigger: Methodology Choice

Prompt: "Какая методология нужна для структуры КП по новому продукту?"

Expected route: `paper-planes-artifact-methodology`.

Expected behavior:

- Select ABCD, RDB, JTBD, SCQA, evidence/proof logic, and commercial economics if price is involved.
- State whether Frappe verification is needed.
- Do not draft the full commercial proposal unless the user asks for it.

Pass condition: methodology preflight is returned with sources, MECE decision, and next action.

## EVAL-002 Good Trigger: Mermaid Structure

Prompt: "Собери Mermaid-схему гипотез по причинам оттока."

Expected route: `paper-planes-artifact-methodology` plus production by the relevant artifact skill if a deliverable is requested.

Expected behavior:

- MECE is explicitly required.
- Select problem map, issue tree, hypothesis tree, CJM/retention logic.
- State source and Frappe verification status.

Pass condition: no hierarchy is proposed without MECE.

## EVAL-003 Adjacent Skill Collision: Slidument

Prompt: "Сделай плотную HTML-презентацию по результатам исследования."

Expected route: methodology preflight here, production through `pp-slidument` or `consulting-slides-creator`.

Forbidden behavior: this skill claims it alone owns slide production.

Pass condition: specialized production skill is named and this skill scopes itself to methodology/source/routing.

## EVAL-004 Bad Trigger: Pure File Operation

Prompt: "Переименуй файл и положи его в папку проекта."

Expected route: no methodology skill unless the file is an artifact instruction or methodology deliverable.

Forbidden behavior: methodology preflight for a simple file operation.

Pass condition: avoid this skill or mark it not applicable.

## EVAL-005 Frappe Authentication Required

Prompt: "Проверь в БЗ, как у нас описан SCQA, и собери структуру."

Expected behavior:

- Try authenticated/live Frappe access if available.
- If only guest access is available and it redirects to login, report authentication-required.
- Mark SCQA detail as not live-verified if proceeding from fallback material.

Pass condition: no claim that Frappe page is missing purely because guest access redirects to login.

## EVAL-006 Writeback Risk

Prompt: "Запиши эту инструкцию как постоянное правило проекта."

Expected behavior:

- Read `md-instruction-workflow.md`.
- Ask for explicit confirmation if not already given.
- Prefer local `instructions/` only inside a known project folder.

Pass condition: no durable instruction file is created without explicit confirmation and clear placement.

## EVAL-007 Source Conflict

Prompt: "В Notion написано одно, в Frappe другое, а клиент прислал третий вариант. Что берём?"

Expected behavior:

- Apply source hierarchy.
- Stop and ask if the conflict affects meaning, client promise, structure, or acceptance criteria.
- Treat Frappe as global methodology canon and client material as project artifact unless the latest user instruction overrides.

Pass condition: conflict is not silently resolved when it changes meaning.

## EVAL-008 Dashboard Methodology

Prompt: "Нужно спроектировать дашборд для управленческого контроля продаж."

Expected behavior:

- Select Formula of Profit, KPI tree, metric hierarchy, leading/lagging indicators, owner/control rhythm.
- Consider MECE for filters, dimensions, and metric tree.
- Route production to dashboard/spreadsheet/BI skill if implementation is requested.

Pass condition: methodology stack distinguishes metrics, dimensions, owners, and review cadence.

## EVAL-009 Ambiguous Trigger: Artifact Or Methodology

Prompt: "Нужно красиво упаковать структуру проекта."

Expected behavior:

- Do not assume the final format.
- Ask or state a safe assumption: presentation, one-pager, project instruction, dashboard, or project-control document.
- Still name likely methodology candidates: SCQA for logic, MECE for structure, RACI/risk register if this is project governance.

Pass condition: the skill does not jump straight to slide production or durable writeback without clarifying artifact type.

## EVAL-010 Model Precision

Prompt: "Разложи, почему падает повторная покупка, и предложи гипотезы."

Expected behavior:

- Use `model-catalog.md` if router table is too broad.
- Select CJM/JTBD for customer path, cohort/RFM logic for behavior, issue/hypothesis tree for causes, ICE/RICE or experiment design for next tests.
- Mark MECE as required for cause categories and hypothesis tree.

Pass condition: selected models cover diagnosis, customer behavior, and test prioritization separately.
