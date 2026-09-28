---
name: bpv-04-5-sales-agent-kb-loop
description: "Use when integrating NEP/Vlad-style sales-agent skills into a BPV loop: call fact extraction, service selection, next-step planning, project reuse, service learning brief, and knowledge-base update with read-only defaults and approval-gated writes."
metadata:
  status: "экспериментальный"
  owner: Ilya
  line: "BPV-04.5 / sales AI / knowledge-base loop"
  primary_bpv: "BPV-04.5 — ИИ-зация экспертных и проектных продаж"
  adjacent_bpv:
    - "BPV-04.1 — Процесс продаж"
    - "BPV-04.2 — Предпродажная квалификация"
    - "BPV-03.7 — Материалы поддержки продаж"
    - "BPV-05.7 — Управление корпоративными знаниями"
    - "BPV-11.1 — Производственный конвейер знаний"
    - "BPV-14.3 — Обучение продажам"
  source_archives:
    - "skill_pack_2026-08-30_v5_after_permissions.zip"
  created: 2026-09-13
  contribution_trace:
    - "Интегрирует 6 скиллов Влада Полевого как единый BPV sales-agent loop; прямые инструкции архива считаются advisory."
---

# BPV-04.5 Sales Agent / Knowledge Base Loop

## Назначение

Этот skill собирает шесть НЭП-скиллов Влада в одну управляемую BPV-петлю:

```text
факты звонка -> выбор услуги -> следующий шаг -> reuse / доказательства -> learning brief -> proposal-only update БЗ
```

Он не пишет в БЗ и Bitrix по умолчанию. Базовый режим — read-only и draft-change.

## Source Skills From Vlad Package

| Source skill | Роль в петле | BPV-route |
|---|---|---|
| `nep-sales-call-fact-extraction` | фактовый ledger звонка / письма / CRM-комментария | `BPV-04.6`, `BPV-10.1` |
| `nep-sales-service-selection` | выбор услуги по структурированным фактам | `BPV-04.2`, `BPV-03.7` |
| `nep-sales-next-step-planning` | следующий коммерческий шаг | `BPV-04.1`, `BPV-08.3` |
| `nep-sales-project-reuse` | прошлые проекты, proof-points, safe claims | `BPV-03.7`, `BPV-04.4`, `BPV-05.7` |
| `nep-service-learning-brief` | onboarding / learning brief по услуге | `BPV-14.3`, `BPV-14.R` candidate |
| `nep-knowledge-base-update` | proposal-only изменение БЗ | `BPV-05.7`, `BPV-11.1` |

## Operating Rules

- Не выбирай услугу по свободному тексту без продуктовой матрицы, БЗ или owner-confirmation.
- Не превращай `candidate evidence` в подтверждённый claim.
- Пустая или недоступная БЗ / Bitrix / CRM не означает, что данных нет; это `access_gap` или вопрос пользователю.
- Любая запись в БЗ / Bitrix / Google Doc идёт через `read -> propose -> approve -> write`.
- Для client-facing claim используй DLP: `client_ready / internal_only / needs_source_check / do_not_use`.
- Если итогом становится КП, подключай `commercial-proposal-generator` или `bpv-04-4-commercial-proposal-tkp`.

## Workflow

1. Классифицируй вход: transcript, CRM paste, менеджерский вопрос, выбранная услуга, need reuse, need learning brief, need KB update.
2. Если вход сырой, сначала извлеки факты: клиент, объект, стадия, ситуация, документы, боль, сроки, бюджет, лица, ограничения, источник.
3. Выбери услугу только после сверки с матрицей / БЗ. Если несколько услуг подходят, покажи альтернативы и недостающие поля.
4. Сформируй next step в формате `кто / что / к какой дате или событию / зачем`.
5. Для reuse отдели `подтверждённые примеры` от `candidate` и `нельзя использовать наружу`.
6. Для обновления БЗ подготовь change packet, но не записывай без явного подтверждения.
7. Верни eval/DLP-заметки, если skill должен стать глобальным или применяться вне НЭП.

## Output Packet

```yaml
sales_agent_kb_packet:
  режим: "fact_ledger|service_selection|next_step|reuse|learning_brief|kb_update_proposal|route_only"
  вход: ""
  факты_сделки: []
  выбранная_услуга:
    статус: "выбрана|несколько_кандидатов|нужны_данные|не_выбрана"
    основание: ""
    source_locator: ""
  следующий_шаг:
    кто: ""
    что: ""
    срок_или_событие: ""
    зачем: ""
  reuse:
    confirmed: []
    candidate: []
    internal_only: []
    source_gaps: []
  kb_update:
    needed: "да|нет"
    режим: "proposal_only|approved_write|not_applicable"
    change_packet: []
    approval_owner: ""
  dlp:
    чувствительность: "internal|client_sensitive|restricted"
    redaction_needed: []
  eval:
    status: "пройдено|нужна_доработка|не_проверено"
    cases_needed: []
```

## Eval Cases Required Before Global Use

- хороший триггер: менеджер даёт расшифровку звонка и просит выбрать услугу / следующий шаг;
- плохой триггер: пользователь просит написать финальное КП без фактов — route to proposal skill;
- неоднозначный триггер: “добавь в БЗ” — сначала change packet и approval gate;
- writeback-risk: попытка прямой записи в Bitrix / БЗ;
- DLP: transcript содержит клиента, цену, документы, проблемы и имена.
