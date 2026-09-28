---
name: bpv-04-4-commercial-proposal-tkp
description: "Use when a commercial proposal / КП / ТКП must be treated as BPV-04.4 implementation work: source-backed proposal production, claim gates, pricing/scope trace, proposal handoff, adoption evidence, and linkage to MPP, CRM, analytics, and training. Co-use commercial-proposal-generator for the proposal text itself."
metadata:
  status: "экспериментальный"
  owner: Ilya
  line: "BPV-04.4 / КП и ТКП / commercial proposal twin"
  primary_bpv: "BPV-04.4 — Подготовка КП и ТКП"
  parent_skill: "commercial-proposal-generator"
  adjacent_bpv:
    - "BPV-03.7 — Материалы поддержки продаж"
    - "BPV-04.1 — Постановка процесса продаж по выбранной методологии"
    - "BPV-04.2 — Предпродажная квалификация"
    - "BPV-05.1 — Проектирование и внедрение CRM"
    - "BPV-10.1 — Автоматизированный аналитико-управленческий контур"
    - "BPV-14.3 — Обучение продажам и коммерческим практикам"
  created: 2026-09-13
  contribution_trace:
    - "Создан как BPV-близнец commercial-proposal-generator по решению Ильи 13/09/2026; источник: НЭП / пакет скиллов Влада Полевого и canonical BPV registry."
---

# BPV-04.4 Commercial Proposal / TKP Twin

## Назначение

Этот skill не заменяет `commercial-proposal-generator`. Он добавляет BPV-слой к КП / ТКП: делает коммерческое предложение не разовым текстом, а воспроизводимым внедряемым контуром с источниками, ролями, критериями приёмки, CRM-следом, handoff и adoption evidence.

Используй его, когда пользователь говорит не только `сделай КП`, но и просит:

- превратить КП / ТКП в BPV / внедренческий контур;
- проверить КП как BPV-04.4;
- связать КП с МПП, CRM, обучением, аналитикой, sales enablement;
- создать альтернативный BPV-route для существующего `commercial-proposal-generator`;
- подготовить QA / eval / DLP для proposal-generating skill.

Если нужно просто написать текст КП, сначала используй `commercial-proposal-generator`, а этот skill держи как BPV-надстройку.

## BPV Route

Канонический адрес:

```text
BPV-04 — Управление продажами
-> BPV-04.4 — Подготовка КП и ТКП
```

Соседние маршруты:

| Сигнал | Route |
|---|---|
| МПП, one-pager, proof-pack, sales kit | `BPV-03.7 — Материалы поддержки продаж` |
| выбор услуги и квалификация | `BPV-04.2 — Предпродажная квалификация` |
| CRM-поля, статусы, причины задержек, история сделки | `BPV-05.1 — CRM` |
| скорость КП, конверсия, причины проигрыша | `BPV-10.1 — аналитико-управленческий контур` |
| обучение менеджеров работе с КП | `BPV-14.3 — обучение продажам` |

## Workflow

1. Определи, что именно нужно: клиентский текст КП, BPV-аудит КП, внедренческий контур КП, skill-twin, QA-only или route-only.
2. Если есть клиентский текст, запусти `commercial-proposal-generator` как parent skill и сохрани его claim/source gates.
3. Построй BPV-04.4 packet: источник запроса, выбранная услуга, владелец, цена / scope, evidence, следующий шаг, CRM-след, handoff, adoption.
4. Проверь, не является ли часть запроса МПП: тогда соседний route — `BPV-03.7`, а не новое КП.
5. Если КП существует как HTML/PDF/PNG-шаблон или его нужно сделать редактируемым, разрешён optional-call к derivative subskill `html-proposal-template-editor` из `~/.codex/derivative-subskills/html-proposal-template-editor/`; он отвечает только за техническую реконструкцию / block-map / template validation, а не за содержание КП.
6. Не создавай задачи, CRM-записи, Google Docs, КП-файл или внешний follow-up без явной команды и конкретного change set.
7. Если появляется повторяемый паттерн, отправь его в skill-governance как patch candidate для parent skill, а не переписывай parent без акцепта.

## Output Packet

```yaml
bpv_04_4_proposal_packet:
  режим: "черновик|клиентская_версия|bpv_qa|route_only|skill_patch_candidate"
  клиент: ""
  объект_предложения: ""
  parent_skill_used: "commercial-proposal-generator"
  proposal_status: "черновик|готово_к_проверке|нужны_источники|нужен_акцепт|не_готово"
  bpv_route:
    primary: "BPV-04.4 — Подготовка КП и ТКП"
    adjacent: []
  source_gate:
    источники_доступны: []
    источники_не_доступны: []
    client_ready_claims: []
    internal_only_claims: []
    needs_source_check: []
  handoff:
    владелец_клиента: ""
    владелец_PP: ""
    CRM_след: ""
    следующий_шаг: ""
    adoption_evidence: []
  production_subskill:
    html_proposal_template_editor: "not_needed|candidate|used|blocked"
    причина: ""
    граница: "только editable HTML/PDF/PNG template layer; не содержание КП"
  eval:
    good_trigger: ""
    bad_trigger: ""
    ambiguous_trigger: ""
    writeback_risk: ""
  dlp:
    чувствительность: "internal|client_sensitive|restricted"
    можно_наружу: "да|нет|после_редактуры|требует_акцепта"
```

## Eval / DLP Gates

- `good trigger`: пользователь просит КП как BPV, proposal QA, route, handoff или внедрение proposal process.
- `bad trigger`: пользователь просит обычный сайт-аудит, cold email, презентацию без КП или аналитический dashboard; выбирай другой skill.
- `ambiguous trigger`: пользователь просит `материалы для продаж`; сначала различи КП / ТКП и МПП.
- `writeback-risk`: любые файлы, CRM, Bitrix, Google Docs, архив КП и task_delta требуют явного акцепта.
- `DLP`: клиентские цифры, цены, маржа, кейсы, имена, внутренние проблемы и proposal reasoning по умолчанию `client_sensitive`.
