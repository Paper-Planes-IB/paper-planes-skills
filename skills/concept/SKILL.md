---
name: concept
description: "Use when Ilya invokes /concept or asks to find and explain specific terms/concepts from the current chat/project, especially non-names, non-internal-methodology terms, technical concepts, protocols, standards, market categories, metrics, software features, business processes, or vendor claims; produces an external researcher prompt by default"
metadata:
  status: experimental
  line: research / knowledge / concept intelligence
  owner: Ilya
  originator: Илья Балахнин
---

# Concept

## Purpose

`/concept` turns messy project language into concept research prompts.

Default behavior: scan the current chat and nearby project context, identify specific terms that are not proper names and not already-covered internal methodology, select one or several concepts, and generate a ready-to-send prompt for an external researcher. The prompt should explain the concept, classify it, source-check claims, and show how it may matter for the project.

This skill is a prompt generator by default, not an automatic deep research runner.

## Trigger

Use this skill when Ilya says:

- `/concept`;
- `concept`;
- `concept-deep-dive`, if he means prompt-style explanation rather than Vault scaffold;
- `объясни концепт`;
- `найди термины в чате`;
- `сделай промт на объяснение концепта`;
- `что такое X в нашем контексте`;
- `разбери термин / понятие / концепцию`.

If Ilya asks to write files, create a concept note, or scaffold a Vault card, use the existing `concept-deep-dive` skill or ask which route he wants.

## Modes

| Mode | Trigger | Output |
|---|---|---|
| `scan` | `/concept` without a chosen term | project-wide vacuum of candidate concepts across the current project and all registered project chats / artifacts, then shortlist + ask which to research |
| `prompt` | default when a concept is chosen | one copyable external researcher prompt |
| `local_explain` | only if Ilya says `объясни здесь`, `делай сам`, `без внешнего исследователя` | concise local explanation with source caveats |
| `return_packet` | Ilya brings back an external concept answer | accepted / change / defer / reject + writeback candidates |

## Project-Wide Vacuum Rule

If Ilya invokes `/concept` or says only `concept` without specifying a term, do not limit the scan to the current visible chat.

Run a project-wide concept vacuum:

1. Preflight the current project / chat contour:
   - check `Карта-чатов.md`, chat registry, project card, README, tracker, Storyline-Storyboard, subpassports, daily statuses, source/research packets;
   - if the current chat is marked as project штаб, treat scope as the whole project;
   - if no registry exists, say so and scan the current folder / visible project context only.
2. Scan all registered project chats / subpassports / artifacts that are locally available:
   - project card / passport;
   - BPM Storyline-Storyboard;
   - task tracker;
   - market / product / data / interview / org subpassports;
   - research packets and return packets;
   - source review notes and daily statuses;
   - other artifacts explicitly linked from the chat map.
3. Extract candidate concepts from the whole project, not just the last user message.
4. Deduplicate variants and transliterations.
5. Exclude proper names, brands, people, files, task IDs, and already-covered internal methodology terms.
6. Return a ranked shortlist by project relevance:
   - high = blocks current understanding / battlecards / data request / client conversation;
   - medium = useful for research or interviews;
   - low = background only.
7. Ask Ilya which concept(s) to turn into an external prompt unless one concept is obviously requested by surrounding text.

Do not create concept notes or write to Vault during vacuum mode unless Ilya explicitly asks.

## Concept Detection

When scanning a chat or project-wide corpus, extract terms that are likely to need explanation:

- technical concepts, protocols, standards, materials, metrics;
- software features, API/integration layers, infrastructure terms;
- market categories, business-process terms, operating models;
- vendor claims that may hide different maturity levels;
- abbreviations and transliterated terms.

Exclude by default:

- people, companies, brands, products, URLs, file names;
- project task IDs, BPM numbers, SI/SIF IDs;
- Paper Planes internal methodology terms already covered by local methodology files;
- generic business words with no concept-specific ambiguity.

If a proper name is also a category or standard, keep it only if the user needs the concept behind it. Example: a brand name is excluded; a protocol/standard is included.

## Methodology Coverage Check

Before generating the prompt, quickly check whether the concept is already covered by nearby methodology / knowledge files when available. Use `rg` in the current project and obvious Vault knowledge locations. Do not do a broad noisy search through `.codex/cache`, sessions, or unrelated technical folders.

If coverage exists, mention it in the prompt as internal context. If not, mark `methodology_coverage: not_found`.

## Output Rules

For `scan` mode, return:

| concept | why it is a concept | likely category | context fragment | recommended action |
|---|---|---|---|---|

For `prompt` mode:

- output one copyable `text` block;
- keep it generic unless Ilya asks for a project-specific version;
- include placeholders for project context and chat excerpts;
- require Russian Markdown output from the external researcher;
- require classification before explanation;
- require source map, claim discipline, claim usability, books if relevant, and self-reflection.
- require production evidence, local market sizing relevance, depth-vs-width competitor checks, customer journey trigger events, and regulatory/source-currentness checks when relevant.

## External Prompt Template

Use this template and adapt only the bracketed fields and any project-specific wording Ilya gave.

```text
# Concept Deep Dive Request

## Role

Ты внешний исследователь, объяснитель и source-check reviewer сложных технических, рыночных, управленческих или отраслевых концептов.

Твоя задача — объяснить выбранный концепт так, чтобы консультантская команда могла правильно использовать его в проекте, не путая:

- термин;
- технологию;
- физический объект;
- протокол;
- стандарт;
- API / integration layer;
- software feature;
- бизнес-процесс;
- market category;
- management concept;
- vendor / expert / market claim;
- project-specific hypothesis.

Ты не должен писать академический обзор ради обзора. Ты должен дать прикладное понимание для стратегии, продукта, продаж, конкурентного анализа, клиентских интервью, source-check, battlecards, диагностики и будущих проектных решений.

## Language

Ответ строго на русском языке.

Английский термин можно сохранить, если он является стандартным названием технологии, протокола, продукта, API, стандарта, управленческого метода или рыночной категории.

Пиши профессионально, но понятно для консультанта, который не является узким специалистом в теме.

## Concept

Концепт для разбора: [ВСТАВИТЬ КОНЦЕПТ]

## Project Context

Мы работаем над проектом:

- клиент / отрасль: [ВСТАВИТЬ]
- тип проекта: [стратегия / диагностика / оргразвитие / продуктовая стратегия / конкурентный анализ / внедрение / КП / контент / другое]
- зачем нам нужен этот концепт: [ВСТАВИТЬ]
- какие решения он может повлиять: [ВСТАВИТЬ]

Концепт встретился в контексте:

[ВСТАВИТЬ 2-5 ФРАГМЕНТОВ ИЗ ЧАТА / ДОКУМЕНТОВ, ГДЕ ТЕРМИН УПОМИНАЛСЯ]

## Core Task

Нужно понять не академически, а прикладно:

- что термин реально означает;
- где его значение размыто;
- какие есть разные трактовки у специалистов, вендоров, клиентов, рынка и консультантов;
- где он влияет на проект;
- какие claims можно использовать;
- какие claims требуют source-check;
- какие вопросы задать клиенту, команде, экспертам, пользователям, партнёрам или подрядчикам;
- какие выводы можно использовать в клиентских материалах, а какие оставить internal-only.

## First: Concept Classification

Перед объяснением классифицируй концепт.

Верни таблицу:

| Dimension | Classification | Comment |
|---|---|---|
| Что это прежде всего | technology / device / protocol / standard / API / software feature / integration layer / business process / market category / management concept / metric / vendor claim / expert term / other |  |
| Это точный термин или зонтик для нескольких явлений? | exact term / umbrella / fuzzy category / marketing label / unclear |  |
| Это физическая функция, процесс, модель, рынок или утверждение? |  |  |
| Где применимо | product / sales / operations / finance / HR / marketing / strategy / IT / service / customer experience / other |  |
| На что влияет в проекте | decision / diagnosis / roadmap / battlecard / interview / data request / client materials / background only |  |
| Риск терминологической путаницы | low / medium / high |  |

Если концепт имеет разные значения в разных отраслях или у разных участников рынка, сначала разведи значения.

## What To Explain

### 1. Что это такое

- Дай короткое определение в 2-3 предложениях.
- Объясни простыми словами, без потери точности.
- Если термин имеет несколько значений, разведи:
  - strict meaning;
  - professional usage;
  - vendor / market usage;
  - customer-facing usage;
  - possible misuse.
- Укажи, какие русские переводы или аналоги могут быть неточными.

### 2. Как это работает

Опиши базовый принцип работы.

Если применимо, явно раздели слои:

| Layer | What belongs here | Example / relevance |
|---|---|---|
| Physical object / device |  |  |
| Process / workflow |  |  |
| Technology / protocol |  |  |
| Standard / certification |  |  |
| Data / API / integration |  |  |
| Software / platform layer |  |  |
| Governance / policy layer |  |  |
| Commercial / operating model |  |  |
| Customer-facing value |  |  |

Если какой-то слой не применим, напиши `not applicable`.

### 3. Кто это использует

Опиши:

- какие типы компаний / команд / ролей используют концепт;
- кто является buyer / decision maker;
- кто является user;
- кто является technical or expert evaluator;
- кто является blocker;
- кто платит;
- кто страдает при плохом внедрении;
- какие отрасли наиболее релевантны.

### 4. Зачем это нужно

Объясни:

- какую задачу решает;
- какие боли закрывает;
- какие alternatives / substitutes существуют;
- когда концепт действительно нужен;
- когда он избыточен;
- когда он является hygiene factor, а не преимуществом;
- когда он является модным словом без достаточного содержания.

### 5. Как это полезно в проекте

Раздели:

| Relevance type | Interpretation for this project |
|---|---|
| Diagnostic relevance |  |
| Strategic relevance |  |
| Product / service relevance |  |
| Commercial relevance |  |
| Operational relevance |  |
| Interview use |  |
| Source-check use |  |
| Battlecard / argument use |  |
| Data request implication |  |
| Internal-only hypothesis |  |

Добавь вопросы, которые нужно задать:

- owner / CEO / sponsor;
- sales / commercial team;
- product / operations / delivery;
- finance / analytics;
- support / service;
- partners / contractors;
- customers / users.

### 6. Как это связано с рынком и конкурентами

Объясни:

- как участники рынка могут использовать этот концепт в позиционировании;
- какие claims стоит проверять;
- какие claims нельзя принимать без доказательств;
- как отличить реальную capability от маркетинговой формулировки;
- как проверить, это production capability, demo, pilot, roadmap item, partner function, one-off case или просто language.
- если концепт используется в конкурентном сравнении, сравнивай не ширину портфеля сама по себе, а глубину реальной способности: production depth, интеграции, lifecycle, поддержка, внедрения, доказанные use cases, operating model, references.

Верни таблицу:

| Possible claim | What it may actually mean | Verification question | Evidence needed | Risk of overclaim |
|---|---|---|---|---|

Если есть конкретные конкуренты или альтернативы, верни отдельную матрицу:

| Player / alternative | Portfolio width | Production depth | Proof of real use | Integration / lifecycle depth | Support / operating model | What remains unproven |
|---|---|---|---|---|---|---|

### 7. Market / Trend View

Проверь:

- растёт ли значимость концепта или падает;
- какие драйверы роста / снижения;
- какие технологические, регуляторные, ценовые, организационные или операционные тренды важны;
- что происходит в релевантной стране / отрасли, если есть данные;
- если локальных данных мало, честно скажи: `локальных данных мало`;
- международные данные используй только как benchmark, не как доказательство локального рынка.
- если концепт влияет на sizing, разложи локальный рынок на осмысленные cohorts / regulated segments / customer classes / company classes, а не только на общий TAM;
- если sizing невозможен, укажи какие публичные реестры, регуляторные классификации, отраслевые базы, тендеры, CRM или интервью нужны для оценки.

Разделяй:

- global trend;
- local / regional context;
- sector-specific relevance;
- enterprise / SMB / public sector / B2C differences, если применимо.

Верни sizing relevance table, если концепт связан с рынком:

| Segment / cohort | Why relevant | How to size | Source needed | Can support TAM? | Confidence |
|---|---|---|---|---|---|

### 8. Практические признаки зрелости

Как понять, что компания действительно умеет работать с этим концептом?

Верни таблицу:

| Maturity signal | What to request | Why it matters |
|---|---|---|
| Documentation |  |  |
| Demo / example |  |  |
| Production case |  |  |
| Data / metrics |  |  |
| Process ownership |  |  |
| Tooling / system support |  |  |
| Integration proof |  |  |
| Support / operating model |  |  |
| KPI / SLA |  |  |
| Governance / responsibility |  |  |
| Partner ecosystem |  |  |

Отдельно верни production evidence checklist:

| Evidence type | What to ask for | Who can confirm | Why it matters |
|---|---|---|---|
| Product / presale confirmation |  | product / presale / solution architect | separates real capability from sales language |
| Implementation evidence |  | delivery / implementation / customer success | proves the concept works beyond demo |
| Customer reference / case |  | customer / account team | proves external use |
| Usage / telemetry / adoption data |  | product / analytics / support | proves repeated use |
| Support / incident evidence |  | support / service desk | reveals operating burden |
| Integration / lifecycle proof |  | technical owner / integrator | proves depth, not label |
| Roadmap vs current production split |  | product owner | separates future promise from current fact |

Отдельно укажи weak signals:

- claim есть только в презентации;
- нет production cases;
- есть API / метод / процесс, но нет внедрений;
- всё держится на одном человеке;
- функция доступна только через партнёра;
- нет поддержки после внедрения;
- нет документов для пользователей / интеграторов / команды;
- нет KPI / SLA / owner;
- demo не показывает реальный lifecycle.
- вендор говорит, что capability есть, но не может показать production evidence;
- есть портфельный пункт, но нет глубины внедрения;
- capability находится в roadmap / pilot, но подана как действующая;
- способность обеспечивается партнёром, но продаётся как собственная.

### 8A. Customer Journey / Trigger Events

Если концепт влияет на продажи, cross-sell, adoption, implementation, roadmap или customer success, опиши реальные trigger events.

Не ограничивайся теоретической логикой "после X можно продать Y". Покажи, какие события в жизни клиента реально создают переход.

Верни таблицу:

| Trigger event | Who notices it | What pain appears | What concept-related need follows | Evidence to verify | Cross-sell / adoption risk |
|---|---|---|---|---|---|

Отдельно отметь:

- trigger events that are real and externally observable;
- trigger events that require internal CRM / win-loss / account notes;
- trigger events that are only consultant inference.

### 9. Основные риски и ошибки понимания

Покажи:

- с чем концепт часто путают;
- технические риски;
- коммерческие риски;
- организационные риски;
- внедренческие риски;
- риски для продаж / стратегии / клиентских материалов;
- формулировки, которые нельзя использовать без проверки.

Обязательно отметь, если термин может быть “слишком красивым зонтиком” и скрывать разные уровни зрелости.

### 10. Source Map

Дай список авторитетных источников:

- официальные стандарты / спецификации;
- документация производителей / платформ / методологий;
- отраслевые ассоциации;
- аналитические отчёты;
- качественные статьи / white papers;
- академические источники, если они реально полезны;
- локальные источники, если есть.
- актуальные регуляторные источники, если концепт связан с compliance, безопасностью, лицензированием, персональными данными, отраслевыми требованиями, государственными системами или критической инфраструктурой.

Для каждого источника укажи:

| Source | URL | Source type | What it proves | What it does not prove | Evidence grade |
|---|---|---|---|---|---|

Evidence grade:

- A = official standard / primary documentation / client-confirmed data;
- B = strong vendor documentation or reputable third-party source;
- C = plausible inference from partial evidence;
- D = weak / marketing-only / unverified;
- X = contradicted by available evidence.

### 10A. Regulatory Mapping

Если концепт связан с регулированием, compliance, безопасностью, государственными системами, персональными данными, критической инфраструктурой, лицензированием, сертификацией, отраслевыми нормами или юридическими рисками:

- используй первичные и актуальные нормативные источники, а не пересказы;
- укажи дату / актуальность нормы;
- отдели юридически обязательные требования от best practice, vendor claim и экспертной интерпретации;
- если нужна юридическая проверка, явно напиши `requires legal review`;
- не делай окончательных юридических выводов без профильного review.

Верни таблицу:

| Regulation / standard | Current status / date | What it requires | Who it applies to | Relevance to concept | What needs legal review |
|---|---|---|---|---|---|

### 11. Books

Если книги реально помогают понять концепт глубже, верни отдельный блок.

Раздели:

- must-read;
- useful background;
- not necessary for this project.

Если книг по теме нет или они не нужны для прикладного проекта, честно напиши: `книги не являются обязательным источником для этого концепта`.

## Claim Discipline

Не превращай vendor / expert / market claims в факты.

Всегда отделяй:

| Claim type | Meaning |
|---|---|
| official definition | Подтверждено стандартом, спецификацией или официальной документацией |
| vendor self-claim | Так заявляет производитель / платформа / поставщик |
| expert claim | Так говорит эксперт / консультант / автор |
| documentation evidence | Есть техническая, методологическая или процессная документация |
| production evidence | Есть кейсы, внедрения, references, demo в рабочем контуре |
| production depth evidence | Есть доказательство глубины: lifecycle, integrations, support, usage, owner, repeated deployment, operating model |
| third-party evidence | Подтверждено независимым источником |
| regulatory evidence | Подтверждено актуальным первичным нормативным источником или юридическим review |
| inference | Логичный вывод, но не факт |
| project-specific hypothesis | Гипотеза для текущего проекта, требует проверки |

Если данных не хватает, помечай `needs source-check`.

Если claim основан только на vendor self-claim или expert claim, не называй его доказанным.

## Claim Usability

Для важных claims укажи, где их можно использовать:

| Claim | Evidence status | Can use in client materials? | Can use in internal notes / battlecard? | Required caveat / source-check |
|---|---|---|---|---|

Статусы:

- safe to use;
- use with caveat;
- internal hypothesis only;
- do not use until verified;
- likely marketing noise.

## Output Format

Верни Markdown со следующей структурой:

## 1. Executive Summary

5-7 ключевых выводов.

Обязательно включи:

- что это такое;
- почему важно / не важно для проекта;
- главный риск неправильного понимания;
- что можно использовать в клиентских материалах;
- что требует source-check.

## 2. Concept Classification

Таблица классификации концепта.

## 3. Concept Card

Таблица:

| Field | Value |
|---|---|
| concept |  |
| short definition |  |
| category | technology / protocol / software / business process / market concept / management concept / standard / other |
| strict meaning |  |
| market / professional usage |  |
| who uses it |  |
| why it matters |  |
| relevance to project | high / medium / low |
| confidence | high / medium / low |
| source-check needed | yes / no |

## 4. Explanation

Понятное объяснение концепта.

## 5. How It Works

Разбери слои: object, process, technology, data, software, governance, operating model, customer-facing value.

## 6. Application To The Project

Таблица:

| Use case | Why relevant | Project implication | Argument / decision implication | Data or interview question | Evidence needed |
|---|---|---|---|---|---|

## 7. Market / Trend View

Драйверы, ограничения, тенденции, local context, global benchmark.

## 8. Competitor / Claim Check

Таблица:

| Possible claim | What it may mean | How to verify | What not to overclaim | Source type needed |
|---|---|---|---|---|

Если есть конкуренты / альтернативы, добавь `Production Depth Matrix`:

| Player / alternative | Portfolio width | Production depth | Evidence | Weakness / unknown | Implication |
|---|---|---|---|---|---|

## 9. Interview Questions

Вопросы для:

- owner / CEO / sponsor;
- sales / commercial team;
- product / operations / delivery;
- finance / analytics;
- support / service;
- partners / contractors;
- customers / users.

Обязательно включи вопросы для product / presale / solution architect, если концепт касается продукта, технологии, внедрения, интеграций, платформы, security, API, compliance или vendor capability.

## 10. Practical Maturity Signals And Production Evidence

Таблица mature / weak signals + production evidence checklist.

## 11. Customer Journey / Trigger Events

Реальные trigger events, которые делают концепт нужным клиенту, пользователю, buyer, интегратору, sales или support.

## 12. Regulatory Mapping

Если применимо: актуальные нормы, первичные источники, обязательность, зона применения, что требует legal review.

## 13. Claim Usability

Таблица claims and whether they can be used in client materials, internal notes or only as hypotheses.

## 14. Source Map

Таблица:

| Source | URL | Source type | What it proves | What it does not prove | Evidence grade |
|---|---|---|---|---|---|

## 15. Books

Если релевантно.

## 16. Final Verdict

- Что команде нужно понять прямо сейчас.
- Что можно использовать в клиентских материалах.
- Что только internal-only.
- Что требует source-check.
- Какие следующие 3-5 действий, включая production evidence, sizing, competitor depth, trigger events или regulatory review, если они релевантны.

## 17. Self-Reflection

Коротко ответь:

1. Что осталось непонятным?
2. Какие источники слабые?
3. Какие вопросы надо уточнить у Ильи / Codex?
4. Что стоит добавить в следующий prompt?
5. Каких production evidence не хватило?
6. Где нужна локальная оценка рынка / sizing по cohorts или regulated segments?
7. Где конкурентное сравнение требует depth, а не portfolio width?
8. Какие customer journey trigger events пока являются inference?
9. Какая регуляторика требует первичного источника или legal review?
```

## Return Packet Mode

When Ilya brings back an external concept answer:

1. Classify findings as `accepted / change / defer / reject`.
2. Extract reusable concept-card structure separately from project-specific claims.
3. Mark source-check gaps.
4. Suggest writeback targets, but do not write to Vault unless Ilya explicitly asks.
5. If it affects Storyline-Storyboard, show deltas: `appeared / strengthened / weakened / needs_check`.
6. Extract next-run requirements separately:
   - production evidence to request from product / presale / implementation / support;
   - local market sizing / cohort sizing needed;
   - competitor production-depth matrix needed;
   - real customer journey trigger events to verify;
   - regulatory mapping / legal review needed.

## Done Definition

Done when:

- candidate concepts are separated from names and internal methodology terms;
- the selected concept is placed into a generic external prompt;
- the prompt requires classification before explanation;
- source discipline and claim usability are explicit;
- production evidence and production depth are requested when capability claims matter;
- local sizing / cohort sizing is requested when market potential matters;
- competitor comparison tests depth, not only portfolio width, when competitors are relevant;
- customer journey trigger events are requested when adoption/cross-sell/roadmap matters;
- regulatory mapping and legal review are requested when compliance or legal claims matter;
- books are requested only if useful;
- the output asks for practical project implications and interview questions;
- Codex does not create Vault concept files unless Ilya asks.
