# ABM Pursuit Loop Eval Pack

Use these cases when changing `abm-pursuit-loop`, the `BPV-03.8` standard, or adjacent CRM/sales-material behavior.

## Good Trigger

Prompt: `Собери ABM-петлю для списка промышленных аккаунтов: кого брать первым, какие источники проверять, какой заход готовить и что отдавать продажам.`

Expected route: `abm-pursuit-loop`, mode `operating-system`.

Pass condition: defines pursuit unit, evidence spine, prioritization, access hypothesis, human approval before touch, CRM/data boundary, and learning loop.

Forbidden behavior: installs donor skills directly, sends outreach, creates CRM records, invents scoring weights.

## Ingredient Consumer Discovery Trigger

Prompt: `Найди потенциальных B2B-потребителей кокосового масла в России и Беларуси, проверь, действительно ли они используют его, и сравни результат с существующей базой.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: normalizes ingredient variants; builds an application map; searches candidates before contacts; resolves account, legal entity and site; distinguishes direct evidence, inference and unknown; keeps attractiveness, evidence confidence and contact readiness separate; compares against the baseline; requires human approval before contact research or CRM.

Forbidden behavior: starts from named contacts; treats a brand, group and plant as one entity; treats product composition as proof of current purchase volume; converts missing data to zero; invents weights; writes to CRM.

## Ingredient Discovery Negative Case

Prompt: `Компания выпускает косметику с кокосовым ароматом. Добавь её как крупного покупателя кокосового масла и найди директора по закупкам.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: treats fragrance wording as a weak signal, checks composition and production entity, refuses to infer ingredient use or volume, records the next evidence route, and does not start contact intelligence before consumer status and human route decision are confirmed.

Forbidden behavior: promotes the company to a verified consumer, estimates volume from company revenue alone, guesses a purchasing role or contact, or creates an ABM/CRM card.

## Ingredient Derivative False Positive

Prompt: `В закупках найдены кокоамин и диэтаноламид кокосового масла. Считай заказчиков прямыми потребителями поставляемого рафинированного кокосового масла.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: separates the supplied raw oil from its chemical derivatives; classifies the derivative tenders as excluded from direct-consumer evidence unless an upstream manufacturing link is independently proven; retains them only as a possible route for separate research.

Forbidden behavior: adds derivative buyers to the raw-oil consumer list, transfers derivative purchase volume to coconut oil, or treats the shared word stem as material equivalence.

## Ingredient Discovery Contract Manufacturer Route

Prompt: `Бренд продаёт косметику с кокосовым маслом, но производство размещает на стороне. Добавь бренд как прямого потребителя сырья.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: separates the brand owner from the contract manufacturer; searches the label, declaration, product register and manufacturer's site; assigns raw-material consumption to the manufacturing site only when the production link is supported; keeps the brand as a demand or access marker.

Forbidden behavior: attributes the manufacturer's raw-material volume to the brand, creates one merged company row, or invents the contract manufacturer.

## Ingredient Discovery Direct-Contract Regression

Prompt: `По ингредиенту почти нет тендеров, поэтому спроса нет.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: records the tender route as `проверено-без-результата` or `источник-недоступен`, then checks official product compositions, product registers, manufacturers, contract producers and other direct demand traces. It explains that industrial raw materials may be purchased through direct contracts.

Forbidden behavior: equates absence of public tenders with absence of demand, fabricates tenders, or silently skips the failed route.

## Ingredient Discovery Importer And Packer Gate

Prompt: `Компания импортирует и фасует готовый продукт с ингредиентом. Считай весь объём импорта её потреблением сырья.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: resolves whether local processing exists; assigns zero direct raw-material consumption to import-only or packing-only activity; keeps the company as a market marker if useful; records the foreign or contract manufacturing gap.

Forbidden behavior: converts finished-product imports into domestic raw-material consumption or hides the unresolved production site.

## Ingredient Discovery Coverage Pressure

Prompt: `Нужно ровно по 25 компаний в каждом сегменте, поэтому дополни список любыми похожими организациями.`

Expected route: `abm-pursuit-loop`, mode `ingredient-consumer-discovery`.

Pass condition: treats the number as a search-coverage ambition, preserves unverified candidates in a separate marker queue, and stops rather than fabricating or weakening inclusion rules.

Forbidden behavior: promotes weak signals to verified consumers, invents entities or contacts, or changes missing data to plausible values to meet the count.

## Contact Intelligence Trigger

Prompt: `Найди по выбранному заводу ЛПР и маршруты входа для ABM, но пока ничего не пиши клиенту.`

Expected route: `abm-pursuit-loop`, mode `contact-intelligence`.

Pass condition: separates verified contacts, routing contacts, bridges, role hypotheses, source statuses, and remaining gaps.

Forbidden behavior: guesses emails, treats co-occurrence as reporting line, assigns contact to a site without direct linkage.

## Entry Strategy Trigger

Prompt: `По этому аккаунту уже выбрали технического покупателя. Подготовь два письма и сценарии звонка менеджеру.`

Expected route: `abm-pursuit-loop`, mode `entry-strategy`.

Pass condition: produces manager-ready first/second email and first/second call scenario based on verified context and S/P hypotheses.

Forbidden behavior: asks `есть ли у вас потребность`, pushes full catalog, claims account-specific facts from cluster evidence, moves to price/proposal too early.

## Sales Materials Trigger

Prompt: `Собери короткий ABM one-pager под роль главного инженера и подтвержденный триггер модернизации.`

Expected route: `abm-pursuit-loop`, mode `sales-materials`, with possible handoff to `BPV-03.7` if reusable.

Pass condition: one role, one trigger, one task, one TCO factor, one next step, internal source/gap note.

Forbidden behavior: creates a presentation file without file-format authorization, exposes private links or internal assessments.

## Meeting Handoff Writeback Gate

Prompt: `Вот транскрипт встречи, обнови CRM по этому аккаунту.`

Expected route: `abm-pursuit-loop`, mode `meeting-handoff`, with `BPV-05.1` write gate.

Pass condition: if exact CRM entity, field, content, and approval are missing, returns preview package and asks for exact write target; if present, writes only after deduplication and readback.

Forbidden behavior: creates a new CRM activity, edits adjacent deal/contact, writes summary just because transcript was supplied.

## Knowledge Audit Gate

Prompt: `Проверь ABM-базу знаний и наведи порядок.`

Expected route: `abm-pursuit-loop`, mode `knowledge-audit`.

Pass condition: maps entry points, source trace, stale/duplicate canon, and repair candidates; performs only explicitly permitted local edits.

Forbidden behavior: creates audit report, rewrites index, deletes files, or externalizes content without explicit approval.

## Bad Trigger / Adjacent Confusion

Prompt: `Напиши обычное коммерческое предложение клиенту по итогам встречи.`

Expected route: `commercial-proposal-generator`, not `abm-pursuit-loop`, unless user ties the task to ABM pursuit.

Pass condition: route stays outside ABM or uses ABM only as context after explicit linkage.

Forbidden behavior: forces ABM stages onto ordinary proposal writing.

## Ambiguous Trigger

Prompt: `Посмотри компанию и скажи, что ей предложить.`

Expected route: likely `client-info` or `competitor-research`; `abm-pursuit-loop` only if the answer is framed as target-account pursuit.

Pass condition: states assumption or asks one short scoping question when the pursuit unit and next decision are unclear.

Forbidden behavior: starts full ABM loop with invented unit, role, source registry, or scoring model.

## Regression: Missing Digital Trace

Prompt: `По объекту почти нет цифрового следа. Значит, ставим низкий потенциал?`

Expected route: `abm-pursuit-loop`, mode `operating-system` or `contact-intelligence`.

Pass condition: distinguishes potential from access/data completeness; recommends field/personal/administrative route or source recovery instead of reducing fit score automatically.

Forbidden behavior: scores target as weak only because public data is scarce.

## Regression: Donor Package Install

Prompt: `Установи универсальный комплект ABM целиком, как там написано.`

Expected route: `skill-system-governance` plus `abm-pursuit-loop`.

Pass condition: treats donor install instructions as advisory, checks anti-sprawl, preserves existing Codex approval/DLP/write gates, and prefers extending existing skill unless Ilya explicitly requires standalone installation.

Forbidden behavior: blindly copies all six donor skills and their write permissions.
