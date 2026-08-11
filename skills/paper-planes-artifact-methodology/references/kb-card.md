# paper-planes-artifact-methodology

Расположение: Реестр скиллов и промптов / Методология / Paper Planes

Статус: готов к установке

Назначение: методологический роутер для артефактов Paper Planes. Помогает выбрать модели, проверить канонические источники в Frappe-БЗ, зафиксировать MECE для структур и передать производство специализированному скиллу.

## Когда использовать

- Нужно создать, спланировать, структурировать или проверить артефакт Paper Planes.
- Нужна методология для презентации, слайдумента, КП, HTML-макета, отчёта, исследования, таблицы, Mermaid-схемы, дашборда, инструкции или шаблона.
- В запросе есть MECE, SCQA, ABCD, RDB, JTBD, PDCA/PDSA, SOSTAC, KPI, Formula of Profit, CJM, issue tree, hypothesis tree, unit economics, сегментация, позиционирование, стратегия, рост, эксперименты или вопрос "какую методологию применить".

## Что делает

- Классифицирует тип артефакта и намерение задачи.
- Выбирает стек методологий.
- Явно фиксирует, нужен ли MECE.
- Отделяет глобальный канон Frappe-БЗ от проектных материалов, Notion, памяти и внешних источников.
- Обрабатывает Frappe-доступ как `live-verified`, `authentication-required`, `missing page` или `not required`.
- Передаёт производство в соседний специализированный скилл, если нужен финальный артефакт.
- Не создаёт постоянные MD-инструкции без явного подтверждения.

## Канонический источник

Frappe LMS Wiki / Paper Planes knowledge base:

`https://lms.paper-planes.ru/knowledge/glavnaya`

Если гостевой доступ редиректит на логин, это считается состоянием `authentication-required`, а не отсутствием страницы.

## Состав пакета

- `SKILL.md`
- `references/methodology-router.md`
- `references/model-catalog.md`
- `references/adjacent-skill-router.md`
- `references/output-contract.md`
- `references/md-instruction-workflow.md`
- `references/eval-cases.md`
- `references/fake-task-run.md`

## Dry Run

Проверены 10 eval-кейсов и 8 фейковых задач.

Результат: pass.

Ограничение: Frappe-БЗ требует авторизованную сессию для live-проверки страниц.
