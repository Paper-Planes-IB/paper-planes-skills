---
name: "consulting-slides-creator"
description: "Use when designing dense Paper Planes consulting sliduments and choosing slide structures: SCQA, action titles, MECE layouts, tables, charts, matrices, roadmaps, RASCI, stage-gates, and QA rules. This skill designs composition and hands production to pp-slidument in the user's requested format; it does not create an intermediate PPTX for PDF."
metadata:
  version: "0.1.1"
  contribution_trace:
    originator: "Илья Балахнин"
    increment: "2026-10-25; requested-format precedence and no intermediate PPTX for PDF; E77-E83; universal method only; internal; effect unmeasured; no financial effect claimed"
---

# Consulting Slides Creator (Paper Planes)

## Mandatory Paper Planes handoff

**Связь с DM.06 — 23.10.2026:** если в проекте уже есть разрешённый мастер DM.06 или пользователь прямо запросил этот формат, `pp-slidument` проверяет достаточность BPM и работает в его границах. Для текущей PDF-деки не создавать отдельный Slides-мастер: конструкцию передавать в существующий согласованный исходник и выпускать PDF. Локальный макет не разрешает итоговую сборку и не заменяет DP03/DP04. См. [владельца выпуска](../pp-slidument/SKILL.md).

Для клиентской презентации Paper Planes этот скилл передаёт сборку в `pp-slidument`: PP Presentation Kit с обновлением 21.07.2026, производственный Markdown, типология, визуальный стандарт, два критика и правила экспорта. Если пользователь явно запросил редактируемый PowerPoint, применяются `pp-slidument/references/native-pptx-production-guide.md` и локальные уточнения режима. Макеты этого скилла — варианты конструкции; комплект не содержит готового `src.generator`. При отсутствии передачи в `pp-slidument` материал не готов к клиентскому выпуску. След принятия пакета и проверки — `contribution_trace` в `pp-slidument/SKILL.md`, 26.09.2026.

Для каждого handoff фиксируй в ответе/существующей спецификации квитанцию: `parent_run_id | child_skill=pp-slidument | slide_ids_or_scope | input_spec_version | handed_off_artifact | handoff_status | next_gate`. Статус `handed_off` допустим только при существующем production MD или ином принятом входном артефакте с версией/путём. Этот скилл отвечает за обоснование конструкции, но не заявляет запуск текстовой редакции, критиков, PDF-экспорта или итогового QA: их квитанции возвращает `pp-slidument`.

Скилл отвечает за выбор конструкции и визуальной логики. Выпуск передаёт в `pp-slidument`, сохраняя прямо выбранный Ильёй формат. Для текущего Paper Planes рабочего маршрута PDF не создавать промежуточный PPTX; редактируемый PPTX допустим только по прямому запросу.

## Производственный маршрут

В установленном пакете есть методические инструкции и ссылки на примеры; рабочего `src.generator` в нём нет. Не запускай старую команду генерации и не создавай PPTX ради промежуточного PDF. Передай композицию в `pp-slidument`; он собирает и проверяет формат, запрошенный пользователем. Регрессионный сценарий E77 проверяет этот маршрут.

## Каталог типов

| Задача | Типы |
|--------|------|
| Графики, KPI | chart, data, waterfall |
| Стратегия | sankey, treemap, matrix, funnel, swot |
| SCQA | scqa |
| Процессы | chevron_process, flow_blocks, mermaid |
| Списки | numbered_list |
| Комбо | chart_table, multi_table, table_sidebar |
| RASCI | rasci |
| Roadmap | roadmap_swimlane |
| Stage-gate | stage_gate |
| Do/Don't | do_dont |
| Сегменты | segment_matrix |
| KPI-строки | goals_rows |
| Brand pyramid | brand_pyramid |
| Mechanism | mechanism_card |
| Титульный | title_dark |
| Executive summary | exec_summary |
| Next steps | next_steps |
| AS IS → TO BE | from_to |
| Сравнение | comparison |
| Issue tree | issue_tree |
| Цитата | quote |
| Пирамида Минто | pyramid |
| Процесс | process_detail |

> ⛔ `divider` ЗАПРЕЩЁН (обучение Балахнина 21.03.2026)

## Критические правила

### Плотность контента
Слайдументы ≠ презентации. Плотные аналитические документы, читаются без спикера.
- Таблицы: 15-30 строк, 4-8 буллетов в ячейке, шрифт 8-10pt
- Боковые блоки (facts): заполнение 80%+ высоты
- Если не помещается — [1/2], [2/2] в заголовке, не обрезать

### Цвета Paper Planes
- **#FF5850** (коралловый) — акцент
- **#000000** — основной текст
- **#374151 / #6B7280 / #E5E7EB** — вторичный, фоны
- Светофор (зелёный/жёлтый/красный) — ТОЛЬКО для RAG-статусов, приоритетов, стрелок динамики

### Action Titles
Каждый слайд — вывод, не описание. «Выручка выросла на 15% за счёт B2B» — не «Динамика выручки».

### Установка зависимостей
```bash
cd ~/.codex/skills/consulting-slides-creator && uv pip install -r requirements.txt
```

## References (Load при необходимости)

| Файл | Содержание |
|------|-----------|
| `references/json_examples_analytical.md` | JSON-примеры для всех 18 аналитических типов |
| `references/json_examples_structural.md` | JSON-примеры для 20 структурных типов |
| `references/content_formatting.md` | Правила форматирования текста, таблиц, фактов |
| `references/slide_type_algorithm.md` | Алгоритм выбора типа слайда |
| `references/visual_diversity.md` | Принцип визуального разнообразия |
| `references/data_extraction.md` | Извлечение данных для графиков |
| `references/quality_checklist.md` | QA checklist + предотвращение ошибок |
| `references/workflow.md` | Workflow для Claude: от контента к PPTX |
| `references/consulting_principles.md` | Консалтинговые элементы и принципы |
| `references/self_learning_log.md` | Лог ошибок из реальных проектов |
| `references/structural_layouts.md` | Детальные спецификации структурных layout'ов |

## Workflow (краткий)

1. **Анализ контента** → определить тип слайда (Load: `references/slide_type_algorithm.md`)
2. **Составить JSON** → по примерам (Load: `references/json_examples_analytical.md` или `references/json_examples_structural.md`)
3. **Передача в производство** → `pp-slidument`, формат следует прямому запросу пользователя.
4. **QA** → проверить заголовок-вывод, плотность, цвета и передачу в `presentation-qa` по выбранному формату.
5. **Итерация** → исправить согласованный исходник и повторно проверить затронутый рендер.

Для клиентской деки Paper Planes добавляй `handoff_receipt` в существующую спецификацию/ответ и передавай его в `pp-slidument`: родительский запуск, версия `pp-slidument`, выбранные ID/типы слайдов, версия входа, переданный артефакт, ожидаемый выход `pp-slidument` и статус передачи. Не утверждай, что запускались редактор, критики, экспорт PDF или итоговый аудит, пока `pp-slidument` не вернул квитанции, связанные с конкретной версией.

## Модульная структура кода

```
src/
├── core/           — constants, shapes, text_blocks, charts, typography, grid, qa, styles
├── layouts/
│   ├── __init__.py — реестр layout'ов + auto-discovery + build_slide()
│   ├── analytical/ — 18 модулей
│   └── structural/ — 20 модулей
└── generator.py    — единый CLI entry point
```

## MANUAL MIGRATION REQUIRED

Review unsupported Claude skill fields manually: `**Paper Planes Consulting Slides Generator**`.

## Регрессия формата

`E77` in `../mece-prezy/evals/scenarios.json`: when the user asks to continue an existing PDF, this skill supplies layout reasoning to `pp-slidument`; it must not invoke the absent PPTX generator or create an intermediate deck. If the user explicitly asks for editable PPTX, that requested format takes precedence and the supported route must be verified.

## Structured Analytical Artifact Gate

Every SCQA, issue tree, classification, matrix, analytical Mermaid, storyline, storyboard, metric tree, or dimension architecture used in a slide inherits the global contract in `~/.codex/AGENTS.md`. Layout type does not create methodological validity: `mermaid`, `matrix`, `table`, or `issue_tree` passes only after its semantic model, source trace, MECE or alternative completeness gate, and client-evidence rights pass. Frappe/Quartz are optional mirrors, not production blockers. This skill still owns layout only; `pp-slidument` owns the final PP deck route.
