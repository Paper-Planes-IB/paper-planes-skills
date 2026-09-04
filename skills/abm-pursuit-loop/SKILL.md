---
name: abm-pursuit-loop
description: Use when designing, running, auditing, or improving a Russian Paper Planes ABM pursuit loop for B2B target accounts, pursuit units, contact research, entry strategy, short sales materials, meeting handoff, CRM-boundary packaging, or ABM knowledge-base hygiene.
metadata:
  status: experimental
  line: BPV-03.8 / доказательная ABM-петля
  owner: Ilya
  originator: Илья Балахнин
  donor:
    author: Дийор
    package: Универсальный комплект ABM 1.1
    received: 2026-09-03
  contribution_trace:
    - author: Дийор
      participants:
        - Илья Балахнин
        - Codex
      artifact: Универсальный комплект ABM 1.1
      project: универсальная ABM-методика для hard-nosed / внедренческих сред
      factory: BPV-03.8
      change_type: методический донорский инкремент
      reuse: перенесено как единый skill `abm-pursuit-loop`; исходные шесть скиллов свернуты в режимы
      quality_check: eval-набор в references/eval-pack.md
      effect: ABM перестает быть списком контактов и становится доказательной петлей выбора, разведки, касания, передачи и обучения
      mode: internal
      finance_note: финансовые последствия авторского вклада не определены источниками
---

# ABM Pursuit Loop

## Purpose

Run ABM as a managed pursuit loop: choose the unit of pursuit, gather evidence, form a role/access hypothesis, prepare a human-approved touch, package CRM handoff, and feed observed outcomes back into the next hypothesis.

This skill is the Paper Planes adaptation of Diyor's `Универсальный комплект ABM 1.1`. The donor package contained six separate skills; in this corpus they are modes of one skill because they share one lifecycle, one evidence spine, and one BPV home: `BPV-03.8`.

## Use When

Use this skill when Ilya asks to:

- set up or improve ABM for a project, segment, list of accounts, distributor channel, partner channel, object, procurement route, or other configurable pursuit unit;
- research a selected B2B account, company, site, object, buyer role, decision maker, influence route, or access route for ABM;
- design an entry strategy, first touch, second touch, call scenario, or manager-ready outreach logic;
- create a short ABM material tied to a verified role, trigger, TCO factor, S/P hypothesis, and next step;
- convert a meeting into an ABM handoff package for CRM without automatic external write;
- audit ABM knowledge base, source trace, master base, or learning loop;
- decide whether an imported ABM artifact belongs to `BPV-03.8`, `BPV-04`, `BPV-05.1`, or another adjacent contour.

Do not use this skill for generic market research, ordinary proposal writing, CRM administration, meeting minutes, or content creation unless the requested work is part of an ABM pursuit loop.

## BPV Boundary

`BPV-03.8` owns:

- unit-of-pursuit model;
- ABM source registry and evidence rules;
- target selection and prioritization logic;
- role/access hypotheses;
- personalization logic and short ABM materials;
- touch strategy before execution;
- learning loop from responses and outcomes.

Adjacent contours own:

- `BPV-04`: sales execution, actual contact, deal development, seller feedback, commercial next actions;
- `BPV-05.1`: CRM entities, fields, statuses, deduplication, write permissions, operational data contract;
- `BPV-03.7`: reusable sales-support materials when the material is broader than one pursuit unit;
- `BPV-05.7`: corporate knowledge-base hygiene when the issue is not ABM-specific.

Never let this skill send outreach, create CRM records, change CRM fields, update tasks, or mutate external systems without a separate exact instruction, deduplication, readback, and log.

## Donor Modes

| Mode | Donor source | Russian meaning | Use for | Output | Handoff |
|---|---|---|---|---|---|
| `operating-system` | `abm-operating-system` | операционная модель ABM | business context, pursuit unit, evidence spine, criteria, score, owner decision | ABM operating packet | stays in `BPV-03.8` |
| `contact-intelligence` | `abm-contact-intelligence` | контактная разведка | entity resolution, people/roles/channels, access graph, source status | contact-ready research packet | `BPV-03.8`; sales may use after approval |
| `entry-strategy` | `abm-entry-strategy` | стратегия входа | one pursuit unit, role/contact, entry route, emails, call scripts | manager-ready entry strategy | execution goes to `BPV-04` |
| `sales-materials` | `abm-sales-materials` | материалы поддержки касания | 3-5 slides, one-pager, checklist, pre-read, manager note | short role-specific material + internal note | broader reusable material goes to `BPV-03.7` |
| `meeting-handoff` | `abm-meeting-to-crm` | встреча в CRM-контуре | transcript/notes to concise protocol, decisions, risks, next steps | CRM-ready handoff package | external write only through `BPV-05.1` after approval |
| `knowledge-audit` | `abm-knowledge-audit` | аудит базы знаний ABM | structure, links, source-to-conclusion trace, duplicates, stale rules | audit findings and repair candidates | generic knowledge hygiene goes to `BPV-05.7` |

## Core Workflow

1. Resolve the request into a mode. If the user asks for the whole ABM contour, start with `operating-system`.
2. Identify the pursuit unit before scoring: account, legal entity, object, site, procurement unit, function, event route, channel partner, or another explicitly defined object.
3. Separate facts, interpretations, hypotheses, unknowns, and human decisions.
4. Build or read the current source manifest. Search snippets and AI summaries are discovery leads, not evidence.
5. Decide the next managerial decision: research, prioritize, find a role, prepare a touch, hand off, observe, pause, or stop.
6. Produce only the artifact needed for that decision.
7. Show source gaps and confidence boundaries.
8. If a write, external touch, CRM update, or task mutation is requested, stop for exact target confirmation unless Ilya has already provided the exact change set in the current turn.

## Evidence Rules

For every material conclusion capture:

- entity and pursuit-unit linkage;
- fact, period, source, direct locator, date checked, currentness, limitation;
- whether the source proves the fact or only suggests a hypothesis;
- relationship level: company, group, branch, site, object, function, person, project, procurement route;
- next evidence check.

Do not invent people, roles, reporting lines, needs, projects, budgets, criteria, weights, thresholds, owners, dates, emails, phones, or CRM status.

Use Russian user-facing statuses. English labels are allowed only as internal immutable mode IDs. Preferred Russian source statuses:

- `найдено-и-проверено`;
- `проверено-без-результата`;
- `источник-недоступен`;
- `не-применимо`;
- `маршрут-не-завершён`;
- `требует-проверки`.

Missing data does not equal zero score. It changes confidence, route, or next-check.

## Mode Output Contracts

### `operating-system`

Return:

- pursuit-unit definition and scope;
- source registry shape;
- criteria and hard gates;
- scoring model status: draft, owner-approved, or not-ready;
- buyer-role / access model;
- CRM/data contract dependencies;
- rhythm of learning loop;
- first pilot conditions.

### `contact-intelligence`

Return:

- resolved identity and ambiguity notes;
- applicable source manifest with terminal Russian statuses;
- verified contacts and relationship level;
- routing contacts and bridges separated from decision-maker contacts;
- conflicts and excluded leads;
- up to three next-depth options.

### `entry-strategy`

Return:

- account and pursuit unit;
- current events and relationship history;
- contacts or route to role;
- one primary and up to two reserve entry ideas;
- first email, second email, first call scenario, second call scenario;
- manager note with S/P hypotheses, objections, forbidden claims, and desired outcome.

First touch opens a conversation. It confirms the role, shows a relevant situation/task hypothesis, asks permission, and fixes a next channel. It must not ask whether the client has a need, ask who the current supplier is, push a catalog, or move to price/proposal before the task is confirmed.

### `sales-materials`

Return:

- short answer-first material tied to one role, one trigger, one task, one TCO factor, and one next step;
- internal sources and unresolved gaps;
- separate manager note.

Create presentation, document, or spreadsheet files only when the user explicitly asks for a file format.

### `meeting-handoff`

Return:

- meeting source, participants if known, decisions, next steps, risks, open questions, and CRM-ready summary;
- exact target CRM entity if supplied;
- writeback status: `preview-only`, `approved-write-pending`, `written-and-read-back`, or `manual-action-required`.

Do not update CRM from this skill unless exact CRM entity, field, write content, and approval are all present.

### `knowledge-audit`

Return:

- observed structure, entry points, source-to-conclusion trace, stale/duplicate canon, technical contamination, and repair candidates;
- no file creation or externalization unless explicitly requested;
- reversible local edits only when already permitted by the active workspace rules.

## Quality Gates

Before final delivery, check:

- the request is truly ABM-loop work;
- pursuit unit is explicit or ambiguity is stated;
- `BPV-03.8`/`BPV-04`/`BPV-05.1` boundary is respected;
- facts, hypotheses, and decisions are separated;
- source statuses are terminal or gaps are visible;
- external write and outreach gates are not bypassed;
- user-facing language is Russian;
- eval coverage exists for any material skill update.

For eval design and regression cases, read [eval-pack.md](references/eval-pack.md).
