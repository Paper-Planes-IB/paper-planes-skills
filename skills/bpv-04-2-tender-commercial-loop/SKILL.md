---
name: bpv-04-2-tender-commercial-loop
description: "Use when NEP/Vlad-style tender skills should be run as one BPV commercial loop: tender ingestion, prioritization, document intake, evidence retrieval, and bid workspace preparation without auto-submit, auto-price, or unsupported claims."
metadata:
  status: "экспериментальный"
  owner: Ilya
  line: "BPV-04.2 / tender qualification and bid preparation"
  primary_bpv: "BPV-04.2 — Предпродажная квалификация"
  adjacent_bpv:
    - "BPV-04.4 — Подготовка КП и ТКП"
    - "BPV-05.1 — CRM"
    - "BPV-05.7 — Управление корпоративными знаниями"
    - "BPV-08.3 — Процесс управленческих решений"
    - "BPV-10.1 — Автоматизированный аналитико-управленческий контур"
  source_archives:
    - "skill_pack_2026-08-28.zip"
  created: 2026-09-13
---

# BPV-04.2 Tender Commercial Loop

## Назначение

Этот skill интегрирует тендерные скиллы Влада как один коммерческий operating loop:

```text
сбор закупочных сигналов -> приоритизация -> разбор документации -> evidence pack -> workspace заявки -> human decision
```

Он не подаёт заявки, не подписывает документы, не назначает цену, не заявляет лицензии / СРО / экспертов / опыт без актуального evidence.

## Source Skills From Vlad Package

| Source skill | Роль | Route |
|---|---|---|
| `nep-tender-ingestion` | сбор и нормализация закупочных сигналов | `BPV-10.1`, `BPV-04.2` |
| `nep-tender-prioritization` | P1/P2/P3 и Tier 0/1/2 | `BPV-04.2`, `BPV-08.3` |
| `nep-tender-doc-intake` | требования, риски, stop-factors | `BPV-04.4`, `BPV-05.3` |
| `nep-tender-knowledge-base` | source pack и reusable evidence | `BPV-05.7`, `BPV-03.7` |
| `nep-tender-bid-assistant` | workspace заявки и checklist | `BPV-04.4`, `BPV-07.7` |

## Operating Rules

- Стартуй от продуктовой матрицы, а не от общих ключевых слов.
- Всегда проверяй дату письма / сигнала против срока подачи в извещении.
- Дедупликация идёт по номеру извещения / процедуры, а не только по заказчику или теме.
- `P1/P2/P3` и `Tier 0/1/2` допустимы как technical labels, но в человекочитаемом выводе рядом давай русское значение.
- Любой найденный тендер сначала `кандидат`; участие требует human decision.
- Если источник найден через агрегатор, но первичная карточка не открыта, статус — `требует проверки`.

## Workflow

1. Определи режим: ingestion, prioritization, light doc intake, full doc intake, evidence pack, bid workspace, route-only.
2. Сверь тендер с продуктовой матрицей и исключениями.
3. Проверь номер процедуры, срок, площадку, НМЦК, заказчика, регион, предмет, закон / процедуру.
4. Раздели решение: прямое участие, партнёр, наблюдение, отказ, требуется РП / юрист / финансы.
5. Для заявки собери requirement-to-evidence matrix и вопросы владельцам.
6. Не создавай рабочую папку, Google Sheet, CRM-задачу или внешнюю запись без явной команды.

## Output Packet

```yaml
tender_commercial_packet:
  режим: "ingestion|prioritization|light_intake|full_intake|evidence_pack|bid_workspace|route_only"
  процедура:
    номер: ""
    площадка: ""
    заказчик: ""
    срок_подачи: ""
    сигнал_получен: ""
    deadline_check: "актуально|просроченный_сигнал|требует_проверки"
  fit:
    продуктовая_матрица: ""
    статус: "core_fit|adjacent_fit|weak_fit|reject|needs_review"
    основание: ""
  приоритет:
    technical_label: "P1|P2|P3|Tier 0|Tier 1|Tier 2|Reject|not_assigned"
    русское_значение: ""
    следующий_шаг: ""
  evidence:
    confirmed: []
    candidate: []
    missing: []
    expired_or_unknown: []
  owner_questions:
    РП: []
    юристы: []
    финансы: []
    продажи: []
  ограничения:
    не_подавать_автоматически: true
    не_назначать_цену_автоматически: true
    не_заявлять_право_без_evidence: true
```

## Eval / DLP

- хороший триггер: “разбери тендер”, “приоритизируй закупку”, “собери пакет заявки”;
- плохой триггер: обычное КП без закупочной процедуры — route to proposal skill;
- writeback-risk: создание workspace, CRM-задач, Google Sheet, отправка заявки;
- DLP: закупочные документы могут быть публичными, но внутренний decision, цена, capability gaps, legal risk и вопросы РП — internal/client-sensitive.
