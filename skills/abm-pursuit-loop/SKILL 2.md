---
name: abm-pursuit-loop
description: Use when discovering B2B consumers of an ingredient or designing, running, auditing, or improving a Russian Paper Planes ABM pursuit loop for target accounts, pursuit units, contact research, entry strategy, short sales materials, meeting handoff, CRM-boundary packaging, or ABM knowledge-base hygiene.
metadata:
  status: experimental
  line: BPV-03.8 / доказательная ABM-петля
  owner: Ilya
  originator: Илья Балахнин
  donor:
    author: Дийор
    package: Универсальный комплект ABM 1.1
    received: 2026-09-03
    latest_reviewed_package: Универсальный комплект ABM 1.3
    latest_reviewed: 2026-09-09
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
    - author: Константин Вогулкин
      participants:
        - Илья Балахнин
        - Codex
      artifact: Промт для построения реестра потребителей сырья — методика VASTECO
      project: поиск B2B-потребителей ингредиентики для продуктового Туннеля ВАСТЭКО
      factory: BPV-03.8
      change_type: практическая обратная связь по двум поисковым прогонам
      reuse: усилены проверка существования спроса, контрактные производители, журнал отрицательных результатов, верификация юридического лица и осторожная трактовка тендеров
      quality_check: добавлены регрессионные сценарии в references/eval-pack.md
      effect: машина различает прямую закупку сырья, продуктовый след, фасовку, импорт, контрактное производство и технически недоступный источник
      mode: internal
      finance_note: финансовые последствия авторского вклада не определены источниками
    - author: Дийор
      participants:
        - Илья Балахнин
        - Codex
      artifact: Универсальный комплект ABM 1.3
      project: поиск B2B-потребителей ингредиентики для продуктового Туннеля ВАСТЭКО
      factory: BPV-03.8
      change_type: расширение алгоритма влево до обнаружения неизвестных потребителей
      reuse: добавлен режим `ingredient-consumer-discovery` перед классической адресной проработкой
      quality_check: отдельные позитивный и негативный сценарии добавлены в references/eval-pack.md
      effect: единицей поиска стала связка компания, площадка, применение и спецификация ингредиента; привлекательность, достоверность и готовность к контакту разделены
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
- discover unknown B2B consumers of a raw material or ingredient before target accounts are selected;
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

Reason / activity objects sit across ABM, account management and CRM. Historical aliases include `инфоповод` in Ракада Мед, `активность / банк прогрессов и акций` in Мясной Гурман, and `reason_to_connect` in ABM. In ABM, the skill owns discovery and preparation of the reason: why this account, why now, what material / argument, which role, what expected next step, and what evidence will prove the touch was worth making. Execution, CRM writeback, progress status and repeated client development belong to `BPV-04` / `BPV-05.1` unless explicitly approved.

Never let this skill send outreach, create CRM records, change CRM fields, update tasks, or mutate external systems without a separate exact instruction, deduplication, readback, and log.

## Donor Modes

| Mode | Donor source | Russian meaning | Use for | Output | Handoff |
|---|---|---|---|---|---|
| `ingredient-consumer-discovery` | `Универсальный комплект ABM 1.3` | обнаружение потребителей ингредиента | ingredient, geography, applications, candidate generation, entity resolution, use evidence, prioritization | verified consumer-candidate register | approved targets continue in `contact-intelligence` |
| `operating-system` | `abm-operating-system` | операционная модель ABM | business context, pursuit unit, evidence spine, criteria, score, owner decision | ABM operating packet | stays in `BPV-03.8` |
| `contact-intelligence` | `abm-contact-intelligence` | контактная разведка | entity resolution, people/roles/channels, access graph, source status | contact-ready research packet | `BPV-03.8`; sales may use after approval |
| `entry-strategy` | `abm-entry-strategy` | стратегия входа | one pursuit unit, role/contact, entry route, emails, call scripts | manager-ready entry strategy | execution goes to `BPV-04` |
| `sales-materials` | `abm-sales-materials` | материалы поддержки касания | 3-5 slides, one-pager, checklist, pre-read, manager note | short role-specific material + internal note | broader reusable material goes to `BPV-03.7` |
| `meeting-handoff` | `abm-meeting-to-crm` | встреча в CRM-контуре | transcript/notes to concise protocol, decisions, risks, next steps | CRM-ready handoff package | external write only through `BPV-05.1` after approval |
| `knowledge-audit` | `abm-knowledge-audit` | аудит базы знаний ABM | structure, links, source-to-conclusion trace, duplicates, stale rules | audit findings and repair candidates | generic knowledge hygiene goes to `BPV-05.7` |

## Core Workflow

1. Resolve the request into a mode. If the user asks for the whole ABM contour, start with `operating-system`.
2. Identify the pursuit unit before scoring. In `ingredient-consumer-discovery`, use `account × legal entity or production site × ingredient application × ingredient specification`; in other modes use account, legal entity, object, site, procurement unit, function, event route, channel partner, or another explicitly defined object.
3. Separate facts, interpretations, hypotheses, unknowns, and human decisions.
4. Build or read the current source manifest. Search snippets and AI summaries are discovery leads, not evidence.
5. Decide the next managerial decision: research, prioritize, find a role, prepare a touch, hand off, observe, pause, or stop.
6. For every proposed touch, write the `повод / активность` explicitly: source signal, target account and role, reason to connect, supporting material, expected progress, owner of execution, expected evidence, stop/retry rule.
7. Produce only the artifact needed for that decision.
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

### `ingredient-consumer-discovery`

Use this mode when the market of potential consumers is not yet known. It precedes contact research and does not require an existing ABM card.

#### Inputs

- normalized ingredient name, aliases, grades, derivatives and excluded substitutes;
- target geography and period;
- supplied specification, pack, certifications, minimum lot and known restrictions;
- known applications and candidate segments, explicitly marked as seed hypotheses;
- existing consumer list, if any, used as a comparison baseline rather than hidden truth;
- public demand traces for the ingredient in the target geography: registered products, finished-product compositions, wholesale offers, imports or other direct category evidence;
- managerial decision that the search must support.

#### Algorithm

1. **Normalize the ingredient.** Build positive and negative search dictionaries of Russian, English, trade, regulatory and technical names. The negative dictionary must cover derivatives, blends, fractions, substitutes, flavours and finished products that mention the ingredient but do not prove consumption of the supplied material. Do not merge a raw material, derivative, blend, fraction, substitute or finished product without an explicit equivalence rule.
2. **Confirm that a demand trace exists.** Before expanding company names, verify that the ingredient or a clearly linked material is present in the target geography through registered products, official compositions, direct procurement, disclosed industrial use, wholesale demand or another opened source. This proves only that a market trace exists; it does not prove the size of the market or any named company's current purchase. If no direct trace is found, preserve the negative result and search limitations instead of fabricating a market.
3. **Build the application map.** For every candidate application record the finished product, ingredient function, probable grade, technological condition, buyer type, exclusion rule and observable market traces. Create a distinct route for contract manufacturers because they may consolidate the demand of many brands. Keep brand owners, contract manufacturers, importers, packers, distributors and final industrial consumers as different roles. The map may be multi-label; do not call it strictly MECE unless one division criterion and a visible residual are established.
4. **Generate candidates by parallel evidence routes.** Run two primary routes in parallel: direct raw-material procurement and product/manufacturing evidence. Industrial ingredients may be bought through direct contracts and leave no public tender, while a tender for a finished product proves only an indirect demand trace. Search official product and company materials, declarations and certificates, patents and technical documents; use exhibitions, associations, catalogues, marketplaces, vacancies, media and search results as radars that lead to stronger evidence. Run application-specific queries with the negative dictionary, then inspect excluded derivative results separately in case they reveal a valid upstream raw-material route. Expand through exact product, manufacturer, plant, brand, tender and document names, not only through a broad ingredient query.
5. **Maintain a source-route ledger.** For each required source family record the exact query or route, date, result, direct locator and one terminal Russian status: `найдено-и-проверено`, `проверено-без-результата`, `источник-недоступен`, `не-применимо`, `маршрут-не-завершён`, or `требует-проверки`. A blocked source must stay visible; it does not authorize filling gaps from general knowledge.
6. **Resolve the entity and prove existence.** Separate brand, account, legal entity, production site, purchasing centre and contractual party. Confirm existence through an official register, working corporate site or product register. If a tender names an unfamiliar legal entity, test its relationship to a known plant or group before creating a new consumer record. A group-level fact does not prove consumption at a specific site. An importer or packer with no local processing has zero direct raw-material consumption for that pursuit unit, even if it sells a finished product. Deduplicate by stable identifiers and preserve aliases.
7. **Verify the use.** Assign one Russian status: `прямо подтверждено`, `сильно предполагается`, `слабый сигнал`, `опровергнуто`, `маршрут проверки не завершён`. Record source, locator, period, ingredient specification, relationship level, limitation and next check. Product composition or a group statement does not by itself prove the current supplier, purchasing volume or purchasing legal entity. Keep suppliers, distributors, unresolved brands and finished-product tenders in a separate market-marker queue until the production link is proven.
8. **Estimate consumption separately.** Preserve `published`, `tender-derived`, `calculated`, `expert`, or `unknown` as distinct internal calculation states and show them to the user in Russian. A calculated range must expose formula, production base, dosage/share assumption, period and sensitivity. Use an opened public wholesale-price range only as a plausibility and commercial-context check, not as proof of purchase volume. Never score an estimate as a confirmed fact.
9. **Apply hard gates.** Exclude or pause candidates when there is no relevant activity in the target geography, the application conflicts with the supplied grade or certification, the entity cannot be resolved, the evidence is stale beyond the decision horizon, an importer or packer has no proven processing, or an explicit commercial/legal restriction blocks work. Missing public data alone is not a hard gate.
10. **Evaluate three independent layers.** Commercial attractiveness covers probable volume, repeatability, margin potential, logistics and product fit. Evidence confidence covers source strength, recency, entity linkage and agreement of sources. Contact readiness covers current purchasing signal, role route and permitted channel. Never collapse these into one opaque score and never let confidence increase attractiveness.
11. **Recommend a route.** Use `передать в адресную проработку`, `допроверить`, `наблюдать`, `исключить`, or `объединить с другой записью`. A human confirms the route. Only approved targets proceed to `contact-intelligence`; only after that may `entry-strategy` prepare a call or message. Do not use a fixed candidate count as a quality threshold.
12. **Learn from outcomes.** Return call results, false positives, inaccessible routes, new terminology, actual applications, requirements and volumes to the application map, source registry and criteria version. Do not rewrite historical evidence.

#### Search stop

Stop when all applicable source families have terminal statuses and two targeted expansion passes over newly found product, manufacturer, plant, tender, document and brand names add no new verified candidate. A time or cost ceiling may stop the run earlier, but the output must show unfinished routes. A requested count such as 25 companies per segment is a coverage ambition, not permission to add unverified rows.

#### Required output

Return:

- scope and normalized ingredient dictionary;
- application map with inclusion and exclusion rules;
- source-route manifest and terminal statuses;
- candidate register at the `company × site × application × specification` level;
- separate market-marker register for suppliers, distributors, unresolved brands, importers, packers and indirect finished-product demand;
- evidence ledger and unresolved contradictions;
- negative-result and inaccessible-source ledger with exact search routes;
- consumption estimate status, range, method and sensitivity;
- separate commercial attractiveness, evidence confidence and contact readiness;
- human decision field, next evidence check and proposed handoff;
- comparison with an existing list by overlap, unique verified additions, false positives, direct-evidence share, entity-resolution quality, application coverage, source freshness and manager usability.

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
- ingredient discovery does not begin with contact search or require a pre-existing ABM card;
- pursuit unit is explicit or ambiguity is stated;
- `BPV-03.8`/`BPV-04`/`BPV-05.1` boundary is respected;
- facts, hypotheses, and decisions are separated;
- source statuses are terminal or gaps are visible;
- external write and outreach gates are not bypassed;
- user-facing language is Russian;
- eval coverage exists for any material skill update.

For eval design and regression cases, read [eval-pack.md](references/eval-pack.md).
