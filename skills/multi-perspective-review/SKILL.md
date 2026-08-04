---
name: multi-perspective-review
description: Use when a serious document, case, article, proposal, matrix, client-facing artifact, or BPV result needs a multi-perspective readiness gate. In bpv_qa mode it acts as the universal BPV-QA router: detects the exact BPV/sub-BPV, loads the canonical QA profile and linked knowledge units, and delegates artifact-specific checks.
metadata:
  status: active
  department: "cross-functional"
  line: readiness-and-bpv-qa
  replaces: three-perspective-review
---

# multi-perspective-review

## BPV-QA router mode

Use `bpv_qa` mode when the reviewed result claims to implement a `BPV-xx` or `BPV-xx.x`, or when the exact BPV route must be determined before acceptance.

This is the universal QA skill for BPV. Do not create one QA skill per BPV by default. The skill loads a declarative QA profile from the canonical BPV registry and linked Knowledge Factory units. A separate specialist QA skill is justified only when the artifact has a distinct verification mechanism, such as a presentation, commercial proposal, financial model, workbook, dashboard, CRM/data specification, org model, or AI/RAG system.

Required route:

```text
artifact / implementation result
-> exact BPV-xx.x classification
-> common BPV QA invariants
-> canonical BPV-specific QA profile
-> linked Knowledge Factory instructions and paired cases
-> artifact-specific QA skill when applicable
-> CKP / artifact / handoff / adoption / paired-case verdict
-> defects, repair route and repeat QA
```

Never infer acceptance criteria from case wording alone. The 5-ka canonical BPV registry owns the BPV code, CKP, acceptance criteria and verdict vocabulary. The 8-ka Knowledge Factory supplies reusable instructions, examples, paired cases and transfer/no-transfer knowledge; it does not override the canonical profile.

Minimal packet:

```yaml
bpv_qa_packet:
  bpv_route: "BPV-xx.x — name"
  route_confidence: confirmed|candidate|ambiguous|not_applicable
  result_type: artifact|process|system|capability|mixed
  qa_profile_source: "canonical registry section/link"
  knowledge_units: []
  paired_cases: []
  common_invariants:
    ckp_fit: pass|fail|unknown
    source_rights: pass|fail|unknown
    artifact_trace: pass|fail|unknown
    handoff: pass|fail|unknown
    adoption: pass|fail|unknown
    paired_case_support: pass|candidate|fail|not_required
  specialist_qa:
    skill: ""
    verdict: pass|fail|not_run|not_applicable
  verdict: passed|passed_with_gaps|repair_required|hold_for_evidence|route_ambiguous
  defects: []
  repair_route: []
  review_owner: ""
```

If the exact `BPV-xx.x` cannot be determined, return `route_ambiguous`; do not silently test against the upper BPV family. A top-level BPV profile does not prove every child sub-BPV.

For `BPV-04.4 — Подготовка КП и ТКП`, keep a hard boundary: the reviewed object is the concrete commercial or technical-commercial proposal file created for the client to use, not Paper Planes' own presale proposal and not the client's full sales process. Test source-transfer fidelity, ABCD/RDB, technical and economic completeness, claims, next step, file integrity and carrier-specific QA. Do not use qualification quality, CRM completeness, SLA, roles, handoff, adoption, conversion or margin as gates of the file verdict. SPIN, BANT and MEDDPICC are optional input traces: inspect only whether supplied information was transferred correctly. Load the local Vault methodology linked from `QA.BPV-04.4.v0.3` first; Notion links are provenance/fallback only and their unavailability must not block the review.

## Presentation routing gate

If the reviewed artifact is a Paper Planes deck, slide block, HTML prototype, PP Pages page or PPTX, require the PP Presentation Kit 2026-07-12 receipt and specialist reports. Multi-perspective review cannot replace `pp-text-critic`, `pp-slide-critic` or `presentation-qa`; missing receipt means `hold_before_client`.

## Назначение

Gate серьёзного документа перед отправкой, публикацией или переводом в следующий контентный / коммерческий контур.

Этот skill является финальным readiness gate, а не редактором вкуса. Его вердикт должен быть связан с назначением артефакта, адресатом, доказательностью claims, DLP-статусом, источниками и риском использования.

## Когда использовать

- `multi perspective review`
- `multi-perspective`
- `three perspective review`
- `3pr`
- `проверь со всех сторон`
- `готов ли документ к отправке`

## Perspectives

Базовые перспективы:

1. Партнёр: есть ли смысл, ценность и решение задачи.
2. Эксперт: выдержана ли логика, фактура и методология.
3. Читатель: читается ли документ без лишнего трения.

Дополнительные перспективы подключаются по жанру:

- клиент: понятно ли, что именно предлагается и зачем это бизнесу;
- редактор 2-ки: подходит ли материал для контентной рельсы и нужного слота;
- коммерция: усиливает ли материал витрину, кейс, КП или маршрут продажи;
- методолог: не теряется ли связка с Vault, BPM/SI, архетипом или продуктовой карточкой.

Обязательные системные перспективы для клиентских, публичных и коммерческих артефактов:

- `source / claim gate`: какие claims подтверждены, какие являются inference, какие нельзя использовать;
- `DLP / disclosure gate`: что нельзя раскрывать и что нужно анонимизировать;
- `artifact-use gate`: можно ли использовать артефакт именно в заявленном канале: КП, deck, статья, кейс, письмо, клиентский документ, внутренний канон;
- `next-contour gate`: что должно пойти дальше в КП, витрину, презентацию, контент-план, knowledge unit, task_delta или no-op.

## Governance contract

Перед вердиктом собрать компактный review packet:

```yaml
multi_perspective_review_packet:
  artifact:
    type: proposal|case|article|deck|matrix|client_doc|internal_doc|other
    intended_use: internal|client_facing|public|partner_facing|canon_candidate|commercial|content
    target_gate: draft_review|before_send|before_publish|before_canon|before_archive|before_next_contour
  source_status:
    sources_available: []
    missing_sources: []
    source_sufficiency: sufficient|partial|missing|not_needed
  claim_status:
    client_ready: []
    internal_only: []
    needs_source_check: []
    do_not_use: []
  dlp_status:
    disclosure_status: safe|needs_redaction|blocked|not_assessable
    sensitive_items: []
  perspectives:
    partner: ""
    expert: ""
    reader: ""
    client: ""
    commerce: ""
    methodologist: ""
  verdict: ready|almost_ready|not_ready|limited_review_only
  required_before_use: []
  next_contour_candidates: []
  task_delta_candidates: []
```

Rules:

- `ready` is impossible if source sufficiency is missing for material claims, DLP is not assessed for external use, or the intended use is unclear;
- `almost_ready` means the artifact is directionally usable but has specific fixes before the next gate;
- `not_ready` means use would create misunderstanding, weak claim risk, source risk, commercial risk, or DLP risk;
- `limited_review_only` means the input packet is insufficient for a real gate verdict.

## Workflow

1. Сначала проверить документ как deliverable, а не как текст в вакууме.
2. Назвать intended use и target gate.
3. Проверить source/claim/DLP слой до финального verdict.
4. Вердикт должен быть явным: `ready`, `almost_ready`, `not_ready`, `limited_review_only`.
5. Замечания выдавать по силе влияния, а не по косметике.
6. Для материалов 2-ки отдельно отмечать, какие упражнения или проверки стоит разнести в writer-скиллы.
7. Если появляются owner-next-actions, предложить их как task_delta candidates, но не создавать автоматически.

## Output contract

```markdown
## Multi-Perspective Review

### 1. Intended Use / Gate

### 2. Verdict

### 3. Top Findings

| Perspective | Status | Finding | Required fix |
|---|---|---|---|

### 4. Claim / Source Gate

| Claim | Status | Source / missing source | Use decision |
|---|---|---|---|

### 5. DLP / Disclosure Gate

### 6. Required Before Use

### 7. Next Contour / No-op
```

Senior-facing default: no more than 5 top findings, no more than 3 blockers, one final verdict.

## Writeback / Approval Gate

Этот skill считается рискованным не потому, что пишет сам, а потому что его вердикт может стать gate-решением для КП, статьи, кейса, матрицы, презентации или клиентского артефакта.

Review-вердикт не является автоматическим разрешением на публикацию, отправку, запись в канон, изменение статуса или обновление файлов. Если review предлагает durable change, финализацию, external send, canonicalization или lifecycle/status update, нужно показать решение и получить акцепт Ильи.

Перед durable action использовать:

```yaml
multi_perspective_writeback_preflight:
  action_type: qa_only|edit_artifact|create_file|update_status|canonize|externalize|task_delta|archive
  target:
  explicit_request_received: true|false
  source_claim_gate_done: true|false
  dlp_gate_done: true|false
  verdict: ready|almost_ready|not_ready|limited_review_only
  approval_required: true|false
  approval_received: true|false
```

Если review создаёт follow-up tasks, route them as `candidate` / `task_delta` to Codex Project Task Inbox after Ilya accepts the concrete list. Do not use CORD Task OS as the primary task home and do not write directly to Airtable without the Inbox handoff.

## Externalization / DLP Gate

Если review касается клиентского, публичного, партнёрского или внешне отправляемого материала, отдельной перспективой проверить DLP-периметр: что нельзя раскрывать, что надо анонимизировать, какие claims не подтверждены, где внутренний язык вылезает наружу, где внешний адресат может увидеть лишний проектный или коммерческий контекст.

Вердикт `готово` невозможен, если DLP-риск не проверен или disclosure status неизвестен.

## Done definition

Done when:

- intended use and target gate are explicit;
- verdict is one of `ready`, `almost_ready`, `not_ready`, `limited_review_only`;
- source/claim gate is applied to material claims;
- DLP/disclosure gate is applied for external-facing use;
- findings are prioritized by use risk, not taste;
- required fixes before use are explicit;
- next contour candidates or no-op are stated;
- no durable write, externalization, status update, canonization, archive, or task_delta is performed without approval.

Not done if:

- verdict is a vague "нормально";
- review focuses on style while missing unsupported claims;
- client/public artifact is marked ready without DLP check;
- review creates tasks or changes statuses without approval;
- project-specific claims become reusable rules without governance cleanup.

## Eval hooks

When this skill is improved or audited through `skill-system-governance`, `skill-eval-harness` must test at least:

- client-facing artifact with missing sources cannot receive `ready`;
- public article with sensitive internal facts is blocked or marked `needs_redaction`;
- review-only request does not edit files or statuses;
- weak claims are routed to `needs_source_check` or `do_not_use`;
- follow-up tasks route to Codex Project Task Inbox as task_delta candidates, not to TaskOS as primary home;
- insufficient input produces `limited_review_only`, not a fake final verdict.
