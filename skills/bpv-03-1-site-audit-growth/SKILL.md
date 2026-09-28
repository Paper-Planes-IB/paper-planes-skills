---
name: bpv-03-1-site-audit-growth
description: "Deprecated bridge. Prefer bpm6-website-positioning-audit when a company website audit is a BPM-6/BPM-7B evidence and positioning diagnostic; use this only for legacy BPV handoff from a completed BPM site audit."
metadata:
  status: "deprecated"
  owner: Ilya
  line: "deprecated BPV bridge / site audit"
  primary_bpv: "BPV-03.1 — GTM и архитектура выхода на рынок"
  adjacent_bpv:
    - "BPV-03.2 — Позиционирование и claims/evidence system"
    - "BPV-03.5 — Контентная фабрика"
    - "BPV-03.7 — Материалы поддержки продаж"
    - "BPV-10.1 — аналитико-управленческий контур"
  preferred_skill: "bpm6-website-positioning-audit"
  deprecation_reason: "Поправка Ильи 13/09/2026: site-audit по специфике сначала относится к семейству BPM, а не BPV."
  source_archives:
    - "company-site-audit-doc.zip"
  created: 2026-09-13
---

# Deprecated Bridge: BPV-03.1 Site Audit Growth

## Назначение

Этот skill оставлен как совместимый мост для уже созданной классификации. По умолчанию аудит сайта нужно вести через `bpm6-website-positioning-audit`: сайт является BPM-источником по публичному позиционированию, продуктовой матрице, доказательствам, digital-входу и search architecture.

Использовать этот BPV-мост только если BPM-аудит уже завершён и из него явно выделен внедренческий объект: структура сайта, landing architecture, proof-pack, материалы поддержки продаж, tracking / CRM поля или клиентский документ.

## Core Rules

- Сначала определить официальный URL. Если сайт неоднозначен, задать вопрос.
- Если задача про диагностику, evidence, позиционирование или сверку сайта с продуктовой матрицей, немедленно route to `bpm6-website-positioning-audit`.
- Не создавать Google Doc, screenshots pack или внешний артефакт без явной команды.
- Скриншоты, SEO-данные, конкурентные выводы и клиентские проблемы проходят DLP.
- Не показывать методические ярлыки клиенту, если нужен клиентский документ; переводить в язык покупателя и следующего действия.
- Если аудит связан с продуктовой матрицей / презентациями / КП, сначала создать BPM evidence trace, затем связать downstream с `BPV-03.7` и `BPV-04.4`.

## Workflow

1. Инвентаризируй сайт: главная, услуги, кейсы, о компании, лицензии, эксперты, статьи, формы, контакты, footer.
2. Для каждой страницы зафиксируй: роль в покупке, H1 / первый экран, proof, CTA, missing elements, source URL.
3. Отдели search architecture от tracking architecture.
4. Для landing pages группируй спрос по клиентской ситуации, а не по внутреннему каталогу услуг.
5. Если нужен документ, держи структуру: summary, page/block analysis, screenshot after analyzed block, search architecture, landing architecture, CRM/tracking fields.
6. Перед клиентским выводом провести anti-slop / de-AI pass через `text-deai-editor`, если доступен.

## Output Packet

```yaml
site_audit_growth_packet:
  режим: "legacy_bpv_handoff|route_to_bpm6|qa_only"
  сайт: ""
  preferred_skill: "bpm6-website-positioning-audit"
  bpm_precheck_done: "да|нет"
  bpv_route:
    primary: "BPV-03.1 — GTM и архитектура выхода на рынок"
    adjacent: []
  site_inventory:
    pages: []
    missing_pages: []
    broken_or_empty_sections: []
  audit:
    что_работает: []
    что_слабо: []
    что_изменить: []
    proof_needed: []
  search_architecture:
    demand_clusters: []
    current_pages: []
    landing_candidates: []
  tracking:
    required_fields: []
  output:
    google_doc_requested: "да|нет"
    screenshots_requested: "да|нет"
    client_ready: "да|нет|после_редактуры"
  dlp:
    чувствительность: "public|internal|client_sensitive|restricted"
    redaction_needed: []
```

## Eval / DLP

- хороший триггер: “аудит сайта”, “посмотри структуру сайта”, “сделай документ по сайту”;
- плохой триггер: BPM-диагностика сайта, сверка с позиционированием, продуктовой матрицей или публичными claims — route to `bpm6-website-positioning-audit`;
- legacy trigger: завершённый BPM-аудит сайта породил конкретный BPV-handoff;
- writeback-risk: Google Doc, screenshots, publication, client delivery;
- DLP: internal recommendations, competitor comparisons, screenshots with private widgets, CRM/tracking assumptions.
