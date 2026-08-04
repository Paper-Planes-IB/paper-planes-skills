# Parent–derivative family contract

Use this reference whenever a parent or derivative loop skill is created, migrated, compared, or promoted.

## Canonical registry entry

```yaml
loop_family_entry:
  family_id:
  parent_skill:
  parent_version:
  governing_bpv:
  governing_bpv_name:
  governing_bpv_ckp:
  bpv_registry_source:
  lifecycle: experimental|review|active|review-critical|deprecated
  business_unit_owner:
  method_owner:
  do_object_class:
  task_class: normative|exploratory|hybrid
  valuable_final_product:
  invariants: []
  mandatory_human_gates: []
  mandatory_evals: []
  source_lineage_contract:
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
  derivatives:
    - derivative_id:
      skill:
      version:
      owner:
      industry_or_context:
      parent_version_inherited:
      declared_deltas: []
      early_gate_deltas: []
      evaluation_deltas: []
      compatibility: compatible|migration_required|blocked|unknown
      evidence_runs: []
      originating_chat_or_context:
      reference_loop_id:
      crystallization_decision:
  unresolved_gaps: []
```

## Derivative creation gate

A child may be created only when:

1. the parent cannot express the need as a parameter or mode without losing clarity;
2. the child has a stable object, receiver, output, owner, and trigger;
3. domain-specific sources or gates materially change execution;
4. the delta is explicit and bounded;
5. parent invariants remain inherited or an authorized override exists;
6. an eval pack covers both child behavior and parent compatibility;
7. the child has a lifecycle and rollback route.
8. a one-off reference loop has passed and its crystallization gate explicitly returns `create_experimental_child`.
9. the governing BPV registration contains code, name, ЦКП, status, and parent; otherwise return `BPV_CKP_GAP`.
10. when the loop derives from a 4ka presentation route, deck artifact/version, approval decision, approved slide IDs, and the reverse BPV link are explicit; an unapproved slide remains a candidate.

Otherwise extend the parent or register a configuration profile instead of creating a new skill.

The first successful run creates only an `experimental` child. Require an unchanged-rule transfer or shadow run for `review`, then the family reproducibility threshold for `active`.

## Parent-to-child propagation

For every material parent change create an impact record:

```yaml
parent_change_impact:
  parent_version_from:
  parent_version_to:
  changed_invariants: []
  changed_gates: []
  changed_schemas: []
  changed_evals: []
  child_impacts:
    - derivative_id:
      status: compatible|migration_required|not_applicable|blocked
      required_change:
      owner:
      due_gate:
      verification:
```

Do not mark the parent change complete while material children remain `unknown`.

## Child-to-parent return

Classify child learning:

- `local_only`: context-specific and non-transferable;
- `sibling_candidate`: useful to a bounded subgroup;
- `parent_candidate`: reusable across the family;
- `new_family_candidate`: violates parent object boundaries and may require a separate parent;
- `no_op`: no method change.

Promotion to the parent requires:

- at least two meaningfully different contexts unless a safety-critical defect justifies immediate correction;
- evidence of improved time, money, quality, safety, or reliability;
- collision check against siblings;
- parent regression pass;
- method-owner acceptance;
- migration impact report.

## Nested derivatives

Allow nested derivatives such as an industry derivative, project derivative, and early-gate subderivative. Keep the shortest valid inheritance chain. A subderivative must never bypass its immediate parent when reporting deltas.

Use project-specific early-gate or evaluation differences as declared deltas, not as universal constants. Promote only after cross-context proof.

## Optional graph layer

Graphify may index parent-child relationships, evidence, and versions. Its absence or staleness is `graph_index_gap`, not a loop blocker. The registry, source files, and audit records are canonical.
