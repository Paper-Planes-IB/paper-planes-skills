---
name: bpv-03-7-expert-deck-builder
description: Use when Vlad/NEP-style company, direction, product, or editable HTML decks should be integrated as BPV-03.7 sales-support materials with source-backed claims, product-matrix identity, presentation QA, and commercial proposal boundaries.
metadata:
  status: "экспериментальный"
  owner: Ilya
  line: "BPV-03.7 / expert decks / editable presentation builder"
  primary_bpv: "BPV-03.7 — Материалы поддержки продаж"
  adjacent_bpv:
    - "BPV-03.2 — Позиционирование и claims/evidence system"
    - "BPV-03.9 — Развитие бренда и визуальной концепции"
    - "BPV-04.4 — Подготовка КП и ТКП"
    - "BPV-10.2 — Портфель аналитических продуктов"
  parent_skills:
    - "pp-slidument"
    - "presentation-qa"
    - "consulting-slides-creator"
    - "commercial-proposal-generator"
    - "bpv-03-7-mpp-sales-support"
  source_archives:
    - "NEP-skills-created-together-latest-2026-09-08.zip"
  created: 2026-09-13
---

# BPV-03.7 Expert Deck Builder

## Назначение

Этот skill интегрирует `expert-group-master-deck` и `editable-master-deck-builder` из пакета Влада как BPV-режимы, а не как автономную презентационную систему.

Он применим к:

- презентации экспертной компании;
- презентации направления;
- продуктовой презентации;
- персонализированному multi-position offer;
- editable HTML deck из утверждённого Markdown и визуального донора.

## Boundaries

- Не выбирай продукт, тариф или соседнюю услугу за пользователя.
- Product matrix — identity source; price calculator — price source.
- Если задача является КП / ТКП, подключай `commercial-proposal-generator` или `bpv-04-4-commercial-proposal-tkp`.
- Если задача является QA готовой деки, подключай `presentation-qa`.
- Если задача требует slidument / HTML / PPTX production, используй существующий PP presentation pipeline; этот skill держит BPV-route и source discipline.
- Если задача требует не нового содержания, а реконструкции / ремонта editable HTML deck, PDF proposal deck или PNG/raster slide export, можно вызвать derivative subskill `html-proposal-template-editor` из `~/.codex/derivative-subskills/html-proposal-template-editor/`. Он не является top-level skill корпуса и не заменяет `pp-slidument`, `presentation-qa` или `commercial-proposal-generator`.
- Не переносить locked / approved wording без проверки источника и права использования.

## Modes

| Режим | Когда использовать | Parent skill |
|---|---|---|
| `company_deck` | презентация компании / группы | `pp-slidument`, `presentation-qa` |
| `direction_deck` | презентация направления или практики | `pp-slidument`, `presentation-qa` |
| `product_deck` | презентация выбранного продукта / услуги | `bpv-03-7-mpp-sales-support` |
| `commercial_offer_deck` | персонализированное предложение | `commercial-proposal-generator` |
| `editable_html_build` | approved MD + визуальный донор -> editable HTML | `pp-slidument` / local production pipeline; optional `html-proposal-template-editor` только для template reconstruction |
| `qa_only` | проверка без создания | `presentation-qa` |

## Output Packet

```yaml
expert_deck_bpv_packet:
  режим: "company_deck|direction_deck|product_deck|commercial_offer_deck|editable_html_build|qa_only|route_only"
  артефакт: ""
  bpv_route:
    primary: "BPV-03.7 — Материалы поддержки продаж"
    adjacent: []
  source_identity:
    product_matrix_row: ""
    price_source: ""
    approved_wording: []
    source_gaps: []
  claim_ledger:
    client_ready: []
    internal_only: []
    needs_source_check: []
    do_not_use: []
  production:
    parent_skill: []
    output_format: "chat|md|html|pptx|pdf|qa_only"
    file_creation_explicitly_requested: "да|нет"
    optional_subskill:
      html_proposal_template_editor: "not_needed|candidate|used|blocked"
      reason: ""
  dlp:
    чувствительность: "internal|client_sensitive|restricted"
```

## Eval / DLP

- хороший триггер: “собери company deck / direction deck / product deck”, “сделай editable deck”;
- плохой триггер: обычное редактирование одного слайда — route to presentation tooling / QA;
- ambiguous trigger: “сделай КП в презентации” — сначала определить КП или МПП;
- DLP: презентации экспертной компании часто содержат кейсы, квалификации, цены, источники и внутренние proof gaps.
