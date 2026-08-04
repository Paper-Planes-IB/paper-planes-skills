---
name: whitepaper-proposal-generator
description: Generate personalized Paper Planes semi-whitepaper, semi-commercial proposals for Gamma when the offer concerns corporate, commercial, operational, organizational, HR/culture, automation/data, or hybrid strategy and transformation. Use when Ilya asks for a whitepaper-like КП, a strategic memorandum with commercial terms, a subject-adaptive proposal based on the 9 levers, or proof-rich Gamma pages using archived Paper Planes projects and mini-cases.
metadata:
  version: "0.1.1"
  supports_bpm:
    primary: [commercial_trace, proposal_route, whitepaper_proposal, client_facing_claims]
    required_secondary: [BPM-2, BPM-5, BPM-10, BPM-11]
    optional_secondary: [BPM-1, BPM-3, BPM-4, BPM-6, BPM-7A, BPM-7B, BPM-8, BPM-9]
  can_consume:
    - commercial origin trace
    - client meeting notes / transcripts / files
    - product vitrine and 9-lever canon
    - BPM / BPO / BPV models
    - project Storyline-Storyboard and Matrix BPM-SI donor candidates
    - archive proof stories and approved cases
    - public sources after source gate
  can_produce:
    - whitepaper proposal packet
    - subject route and client fingerprint
    - proposal claim gate
    - BPM question pack for lived-reality checks
    - commercial donor signal for BPM Exchange
    - task_delta candidates after acceptance
  preflight_required: true
  return_contract:
    version: "v0.1"
    changelog:
      - "2026-07-13: Added BPM Exchange capability metadata and commercial whitepaper as BPM question emitter contract."
---

# Whitepaper Proposal Generator

Create a useful strategic document that also sells the recommended Paper Planes route. Standardize the reasoning architecture, not the client-facing text.

## Mandatory parent and production dependencies

1. Read and apply `../commercial-proposal-generator/SKILL.md` completely unless it is already loaded for the current turn. It owns source, claim, artifact, approval, MEDDPICC, JOLT, commercial trace, pricing, case, implementation and externalization gates. Do not recursively re-trigger either skill once both are active.
2. When producing slides, HTML, PP Pages or PPTX, use the current PP Presentation Kit and `pp-slidument` required by the parent skill. This skill owns subject routing and narrative, not visual production.
3. Keep internal codes such as BPM, BPO, BPV, SI, MEDDPICC and RDB out of client-facing pages. Translate them into questions, works, decisions, artifacts, rhythms and business effects.

## Required references

Read all three before drafting:

- `references/subject-routing.md` — determine the strategic subject, target levers and analytical depth.
- `references/whitepaper-gamma-narrative.md` — build the hybrid whitepaper/commercial narrative and page contract.
- `references/archive-proof-stories.md` — find, validate and write project mini-cases.

Also read only the relevant parent references for tone, Gamma production, pricing, templates and QA.

## Core product logic

Use the invariant three-stage route:

1. **Understand requirements.** Study enough of the 9-lever system to derive conceptual requirements for the target lever or lever bundle.
2. **Design the target system.** Expand target levers through sublevers, mechanisms, models, roles, rules, artifacts, data, metrics and management rhythms.
3. **Make the system reproducible.** Launch real cycles, correct deviations, train by joint work, transfer ownership and test independent reproduction.

Internal routing is `BPM -> BPO design -> BPV implementation`. The client sees `understand -> design -> embed`.

Apply the depth rule:

> The lower the target lever, the more preceding levers usually enter the analysis; each preceding lever is studied only to the depth needed to issue reliable design requirements.

Do not treat the nine levers as a fixed menu. Select a client-specific configuration and show what is in scope, what is checked only as context, what is deferred, and why.

## Workflow

### 1. Build the source pack

Collect, in priority order:

- client meeting notes, transcripts, files, existing proposal and explicit statements from Ilya;
- current commercial trace, decision context and known deal constraints;
- current product vitrine and 9-lever canon;
- relevant BPM/BPO/BPV models and product cards;
- active project storyline/reuse documents;
- archived project passports, source artifacts and approved cases;
- public sources only when current facts or external evidence are needed.

Classify every material claim as `client_fact`, `approved_internal`, `public_verified`, `hypothesis`, `inference`, `internal_only`, `needs_source_check` or `do_not_use`.

Never convert a meeting hypothesis into a client fact. Use formulations such as “мы услышали”, “наша рабочая гипотеза”, and “это предстоит проверить” where appropriate.

Apply an evidence-precision gate to every number, share, range, money amount, timeline, comparison and `X -> Y` arrow, including action titles, accent numerals, diagrams and captions. Each needs an exact source object and locator. If the source is absent, remove the precision and write a concrete qualitative mechanism; never invent a plausible metric. A phrase such as “company grew quickly” must not become `4 -> 6 projects` or any other numeric target without evidence.

### 2. Create the client fingerprint

Before outlining pages, capture:

- business transition and strategic bets;
- owners, decision roles and personal success criteria;
- known metrics and economic constraints;
- stated pains, contradictions and no-decision risks;
- customer requirements and expectations;
- company promises and commercial model;
- contractual obligations, kept separate from expectations and promises;
- operating bottlenecks, systems, data and existing management practices;
- organizational capacity, key competencies, overload and change readiness;
- decision criteria, decision process, paper process, champion and alternatives;
- what the client explicitly does not want.

If a critical field is unknown, mark it as an evidence gap and continue with a bounded working hypothesis unless the missing choice changes price, scope or an external commitment.

### 3. Classify the subject

Use `references/subject-routing.md` to assign one primary type and optional secondary type:

- integrated/corporate strategy;
- commercial strategy;
- operational strategy;
- organizational and management-system transformation;
- people and culture strategy;
- automation, data and IT strategy;
- hybrid transformation.

Produce an internal `subject_route` before drafting:

```yaml
subject_route:
  primary_subject: ""
  secondary_subject: ""
  client_job_to_be_done: ""
  business_transition: ""
  target_levers: []
  upstream_requirement_levers: []
  cross_cutting_levers: []
  deferred_levers: []
  analytical_depth_by_lever: {}
  design_depth_by_lever: {}
  implementation_enablers: []
  recommended_route: ""
  alternative_routes_rejected: []
  route_confidence: high|medium|low
  evidence_gaps: []
```

If several subjects are plausible, select one recommended route and retain at most two alternatives in internal QA. Do not give the client an unranked service menu.

### 4. Form the point of view

Write one governing thesis that connects:

`client transition -> causal mechanism -> risk of a partial intervention -> recommended route -> expected management capability`.

The document must teach the client something useful about their situation. It must also take a position. Avoid neutral textbook exposition.

For every theory block, answer:

1. Why does this mechanism matter here?
2. Which client evidence activates it?
3. What project decision follows from it?

Delete theory that does not change the proposed route, scope, sequence, decision or artifact.

### 5. Build the commercial narrative

Apply ABCD as the visible movement of the document:

- **Attention:** the client recognizes their own transition, tension and consequence.
- **Benefits:** the client sees the capability and business change they will gain, not a list of consultant actions.
- **Credentials:** methods and proof stories explain why the route is credible.
- **Destination:** the client can picture the three stages, involvement, decisions, terms and next step.

Apply MEDDPICC as internal sales scaffolding and JOLT as decision-risk control. Do not expose framework names unless Ilya explicitly asks.

Interleave client diagnosis, theory, route and proof. Do not place a generic company profile or a long theory chapter before the client recognizes themselves.

### 6. Select proof stories

Follow `references/archive-proof-stories.md`.

Use two independent fit tests:

- **problem/mechanism fit:** the donor faced a similar causal problem;
- **artifact/implementation fit:** Paper Planes created or embedded something relevant to the proposed route.

Industry similarity is useful but never sufficient by itself.

Every visible mini-case needs an evidence-rights status and a direct answer to “what this proves here”. By default, place it as a compact proof inset beside the thesis it supports, not as a separate page. Use a full case page only when the story is approved, independently strong and materially advances the decision. Prefer two to four strong stories over a logo wall or many weak mentions.

### 7. Draft Gamma-ready pages

Use the page contract and adaptive sequence from `references/whitepaper-gamma-narrative.md`.

Each page must contain:

- a conclusion headline, not a topic label;
- one main message;
- concrete client, theory, method or proof content;
- a recommended visual form;
- a transition to the next argument;
- internal source/claim trace that stays outside the client layer.

Personalization must continue throughout. Three consecutive substantive pages without client-specific evidence, application or implication is a QA failure.

Treat involvement, mini-cases, commercial caveats, methodology and implementation support as content roles, not mandatory standalone pages. For each role choose `inset`, `sidebar`, `footer`, `integrated block`, `standalone page` or `appendix`. Use a standalone page only when it materially advances the client's decision; otherwise integrate it into the page whose claim it supports.

### 8. Show the three stages at the right resolution

For Stage 1, name research questions, methods, respondents/data and the design requirements produced. The stage must end with explicit requirements for business processes, structure, roles, decision rights, data, metrics and tools that the target operating system must support.

For Stage 2, expand the target levers into tangible artifacts plus their owners and rhythms. Include `as is` and `to be` descriptions of core and supporting processes, process owners, RACI/role contracts, job instructions, business calendar, meeting agendas and formats, decision rules, target structure and interfaces among profit centres, service centres and competence centres, metrics and dashboards. Never stop at “describe processes”, “develop structure” or “prepare recommendations”.

For Stage 3, show launch cycles, Paper Planes and client roles, temporary functional substitution where appropriate, shadowing/co-running, targeted hiring or role replacement when an evidence-backed gap exists, first operating cycles, acceptance gates, gradual role transfer and a test that the company reproduces the required standards independently. Optional post-project support is separate from the base project's acceptance.

Show Ilya's personal involvement in shareholder/leadership sessions, intermediate meetings on findings, key design forks and implementation reviews when it is part of the intended offer. Do not imply unlimited personal delivery capacity.

Treat overload and burnout as a working hypothesis and implementation constraint, not a diagnosis. State what signal will be checked, how workload will be protected and what operating rhythm may need adjustment.

### 9. Run proposal QA

In addition to all parent-skill gates, verify:

- subject is explicit and the structure changes because of it;
- target and upstream levers are distinguishable;
- every upstream analysis ends in a design requirement;
- every detailed lever ends in artifacts plus operating rhythms;
- theory changes a project decision;
- client facts, hypotheses and inferences are not mixed;
- proof stories have source and usage rights;
- proposal archives are not misused as delivery/outcome evidence;
- the offer recommends one route and bounds alternatives;
- the document remains useful even before the pricing pages;
- the document still functions commercially after the intellectual layer;
- implementation and transfer are concrete;
- Gamma text is production-ready and not merely an outline.
- every source notation is decoded through a project notation dictionary and is not reinterpreted by visual similarity;
- accepted client wording is used consistently across the whole document; expectations, promises and obligations are not substituted for one another;
- generic labels such as `design`, `launch`, `contour`, `gate` or `system` name their object, composition and function;
- no numeric or directional precision appears without locator-level evidence;
- large page regions are semantically filled by decision-relevant content, not by isolated generic phrases.

Use this verdict:

```yaml
whitepaper_proposal_qa:
  subject_adaptation: passed|needs_revision
  nine_lever_logic: passed|needs_revision
  personalization_density: passed|needs_revision
  theory_to_decision_trace: passed|needs_revision
  proof_story_rights: passed|needs_revision
  abcd_movement: passed|needs_revision
  meddpicc_content: passed|needs_revision
  jolt_decision_support: passed|needs_revision
  three_stage_delivery: passed|needs_revision
  terminology_precision: passed|needs_revision
  evidence_precision: passed|needs_revision
  semantic_density: passed|needs_revision
  gamma_readiness: passed|needs_revision
  parent_gates: passed|needs_revision|blocked
  overall: passed|needs_revision|blocked
```

Do not call the result final while any required row is `needs_revision` or `blocked`.

## Eval hooks

When this skill changes, `skill-eval-harness` must test at least:

- rapid growth described qualitatively does not become an invented `X -> Y` metric;
- `1/3 + 1/3 + 1/3` explicitly identified as payment order stays payment order and is not interpreted as project phasing;
- customer expectations, company promises and contractual obligations remain separate semantic roles;
- an operational-strategy proposal ends analytics with requirements for business processes and expands Stage 2 into concrete processes, owners, roles, calendars, meetings, structure, metrics and dashboards;
- Ilya's involvement is shown as named sessions and decision points, not generic “personal participation”;
- support, involvement and proof stories become insets by default unless a standalone page advances a decision;
- overload or burnout appears only as an evidence-bounded hypothesis and implementation constraint.

## Output contract

For a substantial request, prepare internally:

1. `source_pack` and claim gate;
2. `client_fingerprint`;
3. `subject_route`;
4. governing thesis and rejected alternatives;
5. evidence-rights table for mini-cases;
6. Gamma-ready page narrative;
7. commercial terms and approval gaps;
8. `whitepaper_proposal_qa`;
9. commercial trace delta when a new commercial fact appears.

Expose only the client-appropriate layer plus material blockers and approvals. Do not dump internal routing into the presentation.
