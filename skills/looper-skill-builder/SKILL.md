---
name: looper-skill-builder
description: Guide Ilya and a senior owner through an interactive brief in the current subject chat, identify the governing BPV from the existing registry, assemble and test a one-off reference loop, and crystallize a successful result into an experimental derivative BPV looper skill with lineage, evals, and family governance. Use when Ilya asks to launch the материнский луперизатор, turn a discussed business process into a reusable loop, create a child BPV looper after a guided CORD/PDSA pass, or design and evolve a parent/derivative loop-skill family. Do not use merely to execute an already-defined loop or summarize a process.
---

# Looper Skill Builder

Current lifecycle: `experimental`. Promote to `review` and then `active` only through the eval and reproducibility gates below.

## Purpose

Guide the user from a live business-process discussion to a tested reference loop and then, only after a crystallization gate, generate and govern an experimental derivative BPV looper without hardcoding temporary outputs.

Treat the product as a managed system:

`Preflight -> Do -> Plan -> Collect -> Organize -> Review -> Do2 -> Check -> Act -> Meta-check`.

The parent skill defines the guided brief, invariants, contracts, gates, evals, lineage, versioning, and bidirectional learning. A derivative skill crystallizes a proven reference loop for a specific BPV class, object, input system, output artifact, and business-unit owner.

This skill designs loop skills. It does not replace `cord-pdca`, which executes a management cycle around a live object, or `skill-creator`, which supplies the packaging mechanics.

## Required resources

Read [references/family-contract.md](references/family-contract.md) when creating or changing a parent/child family, inheritance rules, registries, or versioning.

Read [references/evals.md](references/evals.md) before declaring a new parent or derivative skill ready for review or production.

## Non-negotiables

- Define the valuable final product before inputs, tools, prompts, or automation.
- Preserve semantic equivalence of rules; never optimize for formula resemblance alone.
- Never hardcode target figures, accepted examples, employee lists, coefficients, or expected outputs merely to make a test pass.
- Separate current execution mode from target execution mode.
- Keep humans at explicitly named gates; never hide judgment inside a variable or fallback.
- Treat Graphify as a desirable index, never as a mandatory execution gate or normative source.
- Keep primary sources and decisions traceable even when the graph is absent.
- Make missing normative basis visible; do not silently interpolate policy.
- Do not create a derivative skill until its parent, owner, delta, and eval obligations are explicit.
- Do not promote a child practice into the parent from one successful project.
- Do not start by drafting a child skill. First complete the guided brief and execute the reference loop.
- A single successful reference run may create an `experimental` child, but can never make it `review`, `active`, or production-ready.

## Primary operating mode: guided brief to child looper

When invoked in a subject chat, treat that chat and its linked sources as the working evidence surface. Reuse facts already established in the conversation; do not make the user repeat them.

Run five consecutive phases:

```text
1. Context and BPV routing
-> 2. Interactive eight-step brief
-> 3. One-off reference loop
-> 4. Crystallization gate
-> 5. Experimental child-looper generation
```

### Brief interaction protocol

- Ask only questions that cannot be answered from the current chat or linked sources.
- Move one logical brief block at a time; do not dump the full questionnaire at once.
- After each block, show a compact provisional record and state what it unlocks.
- Return to an earlier block when later evidence changes its contract.
- Separate facts, accepted policies, hypotheses, temporary parameters, and unresolved gaps.
- Require senior-owner confirmation of Do, Collect completeness, conceptual rules, Review criteria, and the crystallization decision.
- Continue safe source inspection and model preparation while non-blocking answers are pending.

### Phase 1. Context and BPV routing

Locate the existing canonical BPV registry and classify the work against it before inventing a new class. Record:

- governing upper BPV;
- governing BPV name and ЦКП;
- possible sub-BPV or existing derivative;
- business-unit/factory owner or ownership gap;
- why the process belongs there;
- adjacent BPV boundaries;
- upstream `source/project -> BPM -> SI -> Storyline slide_id -> deck artifact/version -> approval event/decision -> BPV` lineage and reverse BPV link when applicable.

If no existing BPV fits, return `BPV_CLASSIFICATION_GAP` and a candidate route. Do not create a new upper BPV inside this skill.

If a BPV code or name exists but its ЦКП is absent or cannot be stated as a concrete transferable result, return `BPV_CKP_GAP`. Do not proceed to crystallization or child generation until code, name, ЦКП, status, and parent are explicit.

## Preflight

Run this before designing the loop. Stop only on a material ambiguity that changes the loop class, product, authority, or safety boundary.

```yaml
looper_preflight:
  request:
  current_chat_object:
  bpv_registry_source:
  governing_bpv:
  governing_bpv_name:
  governing_bpv_ckp:
  bpv_status: upper_bpv|sub_bpv|derivative|needs_classification
  business_unit_owner:
  do_object:
  valuable_final_product:
  product_form:
  product_receiver:
  value_proof: time|money|quality|combined
  task_class: normative|exploratory|hybrid
  parent_system:
  upstream_lineage:
    source_project:
    source_artifacts: []
    source_bpm: []
    si_ids: []
    storyline_slide_ids: []
    deck_artifact:
    deck_version:
    approval_event_or_decision:
    approved_slide_ids: []
    approved_decisions: []
    bpv_reverse_link: written|proposed|missing|not_applicable
    trace_status: complete|candidate|gap|not_applicable
  current_execution: human|machine_supported|machine_operated
  target_execution: human|machine_supported|machine_operated
  human_owner:
  human_gates: []
  write_authority: read_only|candidate_only|approved_write
  sensitivity: public|internal|client_sensitive|restricted
  dlp_status: passed|blocked|needs_redaction
  source_readiness: complete|partial|contradicted|missing
  graph_index: available|stale|unavailable|not_applicable
  loop_scope:
  excluded_scope:
  expected_derivative_family:
  stop_conditions: []
```

### Preflight gates

1. **Product gate:** the output is concrete, transferable to an operator, and usable without redesign.
2. **Value gate:** the expected improvement in time, money, quality, or their combination is testable.
3. **Authority gate:** durable writes, external actions, policy changes, and production releases have explicit authority.
4. **Lineage gate:** upstream evidence and decisions are named. For 4ka BPV-derived loops preserve: `source/project -> BPM / mining -> SI -> Storyline/BPA slide class and ID -> deck artifact/version -> defense/approval event -> approved slide/decision -> BPV -> Plan loop`, plus the reverse BPV link to BPM, SI, slide, and approved decision. An unapproved slide can create only a BPV candidate and cannot pass crystallization as accepted lineage.
5. **Data gate:** required sources, identifiers, grain, periods, ownership, freshness, and exceptions are known or visibly missing.
6. **Human gate:** judgment, override, release, and exception ownership are explicit.
7. **Safety gate:** DLP, access, legal, people-impact, and externalization boundaries are explicit.
8. **Evaluation gate:** success, regression, stop, and rollback criteria can be tested.

If Collect later reveals an unplanned variable, source, or policy, return to Do through a controlled feedback loop. Classify it as `Do incomplete`, `source unnecessary`, or `unauthorized rule`; never absorb it silently.

## The eight-step operating loop

### 1. Do — define the valuable final product

Write a one-sentence main question and a MECE description of what the loop must produce.

Specify:

- object and receiver;
- exact artifact form;
- formula or conceptual result contract;
- value proof;
- acceptance criteria;
- exclusions and non-goals.

Do is invalid when it names only activity, analysis, automation, or an abstract capability.

### 2. Plan — define strategies and policies

List the upper-level policies that govern Do:

- strategic intent and parent goals;
- thresholds, deadlines, floors, ceilings, and priorities;
- connected processes and systems;
- applicable approved decisions;
- human decision rights;
- change-control policy.

Do not convert a one-month parameter into a permanent policy without evidence. Mark uncertain constants as hypotheses with period and owner.

### 3. Collect — register raw inputs

Create a complete source register with links or physical locations, grain, stable identifiers, period, freshness, owner, allowed use, and known defects.

The senior owner must confirm whether Collect covers Do. If a newly found input changes the product or rule system, trigger `Collect -> Do` feedback before continuing.

Classify every input as:

- normative source;
- primary evidence;
- operational data;
- historical evidence;
- comparison baseline;
- diagnostic object;
- non-authoritative aid.

Previous automation may be a diagnostic object, not a source of truth.

### 4. Organize — build the unambiguous conceptual model

Translate sources into semantic rules:

- variables and their origin;
- conditions and branches;
- precedence and mutual exclusions;
- thresholds and periods of validity;
- exception routes;
- joins and identity resolution;
- missing-data behavior;
- human overrides;
- output components and reconciliation logic.

Compare meaning, not syntactic complexity. Two formulas are equivalent only when they produce the same decisions across the valid input domain, not merely one observed dataset.

### 5. Review — define readiness before execution

Review data quality, model completeness, source rights, safety, operability, observability, and success criteria before dry run.

Set:

- input quality thresholds;
- allowable variance;
- component-level reconciliation;
- exception limits;
- reviewer and release owner;
- rollback and fallback;
- golden/shadow/blind or synthetic test design.

Never use a single fitted month as proof of generality. A golden case may use the same month or another month, but it must test the accepted rule system; a shadow case tests transfer without changing rules to match outputs.

### 6. Do2 — run the controlled dry run

Execute the model on an approved test pack. Preserve:

- input snapshot;
- rule and skill versions;
- decisions and overrides;
- component outputs;
- errors and warnings;
- timing and cost;
- complete audit trail.

Do2 may be golden, shadow, blind, synthetic, replay, or controlled pilot. It is not production.

### 7. Check — compare result with the correct truth mechanism

First choose the evaluation logic:

- **Normative:** compare every material component, decision, exception, and total against the accepted rule/evidence corpus.
- **Exploratory:** compare external effects, retain stronger variants, reject weaker ones, and preserve experiment validity.
- **Hybrid:** use hard safety/normative gates plus empirical optimization inside the allowed space.

Run eight universal passes:

1. source fidelity;
2. semantic rule equivalence;
3. calculation/data integrity;
4. branch, exception, and boundary coverage;
5. DLP, authority, and human-gate compliance;
6. operator usability and final-product completeness;
7. regression and transfer across cases;
8. lineage, auditability, and parent/child compatibility.

Ignore inherited QA labels and status fields unless independently evidenced. Register each mismatch at component level with source rule, implemented rule, observed result, root cause, and required correction.

### 8. Act — change the model or Plan

Classify each correction:

- rule/model correction;
- source/data-contract correction;
- Plan/policy correction;
- human-gate correction;
- interface/operability correction;
- parent-skill candidate;
- derivative-only correction;
- no-op.

Act starts a new versioned cycle. Never patch target outputs directly. Preserve rollback and explain why the correction belongs to the model, Plan, parent, or derivative.

## One-off reference loop

After the brief is accepted, run the eight-step model once as a controlled reference loop in the current task context. Do not create the child skill yet.

The reference-loop packet must contain:

```yaml
reference_loop:
  governing_bpv:
  upstream_lineage: {}
  brief_version:
  input_snapshot:
  rule_model_version:
  execution_mode:
  dry_run_case:
  component_results: []
  exceptions: []
  human_decisions: []
  eight_pass_check: []
  deviations: []
  corrections: []
  rerun_result:
  value_effect:
  audit_trail:
```

For normative work, prove component and decision equivalence, not only the final total. For exploratory work, prove experiment validity and external effect. A corrected rerun must use changed rules or data contracts, never patched target outputs.

## Crystallization gate

Run this gate only after the reference loop reaches an accepted result.

```yaml
crystallization_gate:
  do_achieved: true|false
  governing_bpv_confirmed: true|false
  reference_loop_reproducible: true|false
  semantic_rules_explicit: true|false
  no_target_hardcoding: true|false
  sources_traceable: true|false
  approved_decision_trace_complete: true|false|not_applicable
  reverse_bpv_link_ready: true|false|not_applicable
  human_gates_explicit: true|false
  operating_boundaries_known: true|false
  parent_invariants_identified: true|false
  derivative_deltas_declared: true|false
  eval_pack_ready: true|false
  creation_authority: approved|needs_confirmation|not_approved
  decision: create_experimental_child|repeat_reference_loop|return_to_brief|stop
```

Use `create_experimental_child` only when every substantive gate passes. One reference run proves that a child can be crystallized; it does not prove generality or production readiness.

If the original invocation explicitly requested both the guided pass and child creation, treat it as creation authority for the accepted scope. Ask again only when the proposed child name, BPV parent, location, permissions, or scope materially differs from what was agreed.

## Experimental child-looper generation

After `create_experimental_child`, invoke `skill-creator` and create a derivative skill package. Never copy the entire parent blindly.

The child must include:

- explicit reference to `looper-skill-builder` and the governing BPV;
- concrete Do and valuable final product;
- specialized brief fields and source/data contracts;
- inherited parent invariants;
- declared domain, industry, project, early-gate, and evaluation deltas;
- executable loop sequence and human gates;
- reference-loop evidence without client-sensitive payload;
- eval and regression cases;
- stop, fallback, rollback, audit, and DLP rules;
- family-registry entry and parent version;
- lifecycle `experimental`.

Do not mark the child `review` until it passes a transfer or shadow case without changing rules to match the result. Do not mark it `active` until the family lifecycle criteria are met.

## Parent and derivative governance

The parent owns invariants, schemas, mandatory gates, evaluation method, lifecycle, and family registry. The derivative owns domain sources, local rules, output artifact, business-unit owner, and explicitly declared deltas.

Use this inheritance test:

```text
parent invariant
-> inherited unchanged?
-> specialized by declared parameter?
-> overridden with authority and evidence?
-> tested against parent regression pack?
-> registered in family map?
```

Child-to-parent promotion requires repeatability, cross-context relevance, evidence, no collision with siblings, and parent-owner review. Parent changes must produce an impact report for every child: `compatible`, `migration_required`, `not_applicable`, or `blocked`.

Graphify may help traverse the family, but the canonical family registry and file lineage remain sufficient for execution.

## Meta-check

Run after a full loop, a broken loop, or a shortened automatic return such as `Collect -> Do`.

Evaluate the parent skill itself:

- Did it select the correct task class?
- Did it ask only decision-relevant questions?
- Did it prevent silent policy invention and hardcoding?
- Did it route human judgment correctly?
- Did it generate a usable child contract?
- Did the child inherit and report deltas correctly?
- Did Check expose real failures?
- Did Act improve the object or only the test case?
- Are parent changes propagating to children?
- Are general child learnings returning to the parent?

Classify the meta-result as `parent_ok`, `parent_patch_candidate`, `child_patch_only`, `eval_gap`, `governance_gap`, or `no_op`. Skill changes require `skill-system-governance` and eval coverage before writeback.

## Machine and human execution

Do not use one flat automation label. Record current and target modes and the actual division of labor.

For each operation state:

- machine action;
- human action;
- decision owner;
- evidence produced;
- stop condition;
- fallback.

`machine_operated` never means human-free. Humans retain named ownership of policy, exceptional judgment, release, and consequences.

## Output contract

Maintain a compact state packet throughout the guided brief and before creating or changing a derivative skill:

```yaml
looper_design_packet:
  phase: bpv_routing|brief|reference_loop|crystallization|child_generation|meta_check
  preflight: {}
  bpv_route: {}
  approved_decision_lineage: {}
  brief_progress:
    current_block:
    accepted_blocks: []
    unresolved_questions: []
  do_contract: {}
  plan_policies: []
  collect_registry: []
  conceptual_model: {}
  review_gates: []
  dry_run_design: {}
  check_method:
  act_routes: []
  execution_model: {}
  parent_contract: {}
  derivative_contract: {}
  family_registry_delta: {}
  eval_pack: []
  reference_loop: {}
  crystallization_gate: {}
  child_skill:
    name:
    path:
    lifecycle: experimental
    validation_status:
  meta_check: {}
  lifecycle: experimental|review|active|review-critical|deprecated
  unresolved_gaps: []
  writeback_scope: []
```

## Writeback and externalization

- Preview the design and exact file scope before durable changes unless the user explicitly commanded creation or editing.
- Route executable task deltas to the established project tracker; never invent a parallel task home.
- Treat external research and model output as advisory until reviewed.
- Redact or block client-sensitive inputs before externalization without approval.
- Do not create production automations, integrations, or external objects merely because the loop design mentions them.

## Done definition

The parent looper skill is ready for `review` only when:

- Do and valuable final product are concrete;
- normative/exploratory class is explicit;
- all eight stages have inputs, outputs, owners, and return routes;
- current and target execution modes are separated;
- DLP, human gates, audit, fallback, and rollback are specified;
- parent/child contracts and family registry exist;
- forward and backward trace rules exist;
- required eval pack passes;
- meta-check and lifecycle are defined;
- no test depends on hardcoded expected output.

It is not ready when a single successful dry run is the only evidence, a missing rule is hidden by fallback, or the derivative cannot explain its lineage and deltas.

A guided invocation is complete only when it ends in one explicit state:

- `experimental_child_created`;
- `reference_loop_passed_child_deferred`;
- `repeat_reference_loop_required`;
- `returned_to_brief`;
- `blocked_by_normative_or_authority_gap`.
