# Whitepaper-like Gamma proposal narrative

## Contents

1. Genre contract
2. Adaptive page families
3. Recommended sequence
4. Page specification
5. Personalization and style QA

## 1. Genre contract

The document must work simultaneously as:

- an executive point of view that improves the client's understanding;
- a personalized diagnosis of the client's transition;
- a reasoned recommendation, not a neutral menu;
- a commercial offer with scope, delivery, terms and next decision;
- an internal-defense document that a champion can forward to other decision makers.

The reusable theory is a minority layer. Personalization should dominate the argument and remain visible from beginning to end.

Use an external title built around the client's transition, not the service name:

`How <client> can move from <current management condition> to <target capability>`

Optional subtitle:

`A personalized strategic memorandum and proposal for joint work`.

## 2. Adaptive page families

Use only families that advance the decision:

1. **Recognition page:** sourced client facts, transition and tension.
2. **Causal diagnosis page:** mechanism linking symptoms to root problem.
3. **Theory lens page:** one transferable idea immediately applied to the client.
4. **Nine-lever page:** target, upstream, cross-cutting and deferred levers.
5. **Decision page:** why this route, what alternatives were rejected and why.
6. **Research page:** question, evidence, method and requirement produced.
7. **Design page:** target artifact, owner, rhythm, metric and use.
8. **Implementation page:** live cycles, roles, transfer and acceptance.
9. **Proof inset:** one donor, one mechanism and one transfer lesson embedded in a diagnosis, design or implementation page. Promote it to a separate page only when the case is approved, independently strong and central to the decision.
10. **Commercial page:** involvement, timing, price, payment, assumptions and next step.

Do not create filler pages such as generic trend lists, unsourced market statistics, a logo wall, or “about us” before the client problem is established.

## 3. Recommended sequence

Adapt length to the decision, but preserve this movement:

1. Title with the client's transition.
2. Executive thesis: what changed, why the old system no longer fits, what route is recommended.
3. What we heard: sourced facts, goals, contradictions and constraints.
4. The hidden causal mechanism.
5. Why a partial intervention is insufficient.
6. The relevant theory of the subject, immediately applied.
7. The 9-lever configuration: analyze, design, implement, defer.
8. Why this scope and sequence are sufficient.
9. Stage 1 logic: questions, methods and design requirements.
10. Stage 1 concrete modules tailored to the subject.
11. Stage 2 target system.
12. Stage 2 artifacts grouped by target lever.
13. Example of how one artifact works in daily management.
14. Stage 3 implementation and transfer ladder.
15. Governance: owners, client team, Paper Planes team and Ilya's role.
16. Add proof inset 1 to the closest causal-mechanism page.
17. Add proof inset 2 to the closest artifact or implementation page.
18. Expected management and business effects with metric logic.
19. Risks, assumptions, boundaries and what is consciously not proposed.
20. Timing, decision gates and first working cycle.
21. Commercial terms and payment order.
22. Recommended next decision.

This is a page library, not a mandatory 22-page quota. Merge adjacent pages when the decision is simple; split dense design pages when useful content would become unreadable.

Place proof stories next to the claim they support rather than collecting all cases at the end. Treat the list above as insertion instructions: proof insets do not create pages 16 and 17 by default and do not increase the page count.

## 4. Page specification

Draft every Gamma page with:

```yaml
page:
  id: ""
  family: recognition|diagnosis|theory|lever_map|decision|research|design|implementation|proof|commercial
  headline_conclusion: ""
  main_message: ""
  client_specific_content: []
  theory_or_method_content: []
  proof_or_source_content: []
  visual_form: diagram|table|process|timeline|matrix|cards|quote|metric_tree|other
  transition: ""
  internal_trace:
    sources: []
    claim_status: []
    approval_needed: []
```

The client-facing page receives all fields except `internal_trace`.

For an embedded case use:

```yaml
proof_inset:
  supports_page: ""
  takeaway_headline: ""
  situation: ""
  move_and_artifact: ""
  confirmed_effect_or_boundary: ""
  relevance_here: ""
  internal_source_and_rights: ""
```

Use conclusion headlines such as:

- “Growth increased the number of interfaces faster than the management system could formalize them.”
- “Bitrix24 can support the new model only after process ownership and target data are defined.”

Avoid topic headlines such as “Business processes”, “Automation”, or “Our approach”.

## 5. Personalization and style QA

Pass all checks:

- the first substantive page makes the client recognize themselves;
- the governing thesis could not be sent unchanged to another company;
- no three consecutive substantive pages lack a client fact, application or implication;
- names, roles, systems, geography, product logic and strategic bets appear only when sourced and relevant;
- client language is reused without reproducing transcription noise;
- every theory page changes a proposed choice;
- every method page says what decision its evidence enables;
- Benefits describe changed management capability and business effect, not consultant activity;
- Credentials prove the specific route, not generic prestige;
- Destination shows what happens after agreement;
- the document helps the internal champion explain the project;
- terms do not arrive as an unrelated price appendix.

Maintain a calm, precise and executive tone. Avoid consulting bird language, exaggerated certainty, decorative theory, bright but unsupported contrasts, and repeated “not X but Y” rhetoric.
