---
name: admin-scale
description: >-
  Use only as a temporary scaffold or fallback when the user explicitly invokes
  admin-scale or the parent admin skill is unavailable. The canonical
  administrative-scale behavior belongs in admin: goal, purpose, policy, plans,
  programs, tasks, valuable final product, ideal scene, and statistics.
metadata:
  status: temporary_scaffold
  lifecycle: scaffold_migrating_to_admin
  parent_skill: admin
---

# Admin Scale

Use this skill when the user explicitly invokes `admin-scale`, or when the parent `admin` skill is unavailable and the user wants a project, workstream, or initiative described through the logic of the administrative scale.

Prefer `admin` for real project admin passes. `admin` owns the canonical behavior: creating, checking, updating, and refreshing the administrative scale on every relevant admin call.

## Temporary scaffold status

This skill is a scaffold while the parent `admin` skill internalizes the administrative-scale behavior.

Deletion / deprecation criteria:

```yaml
admin_scale_scaffold_deletion:
  behavior_migrated_to: admin
  reproducibility_runs_required: 3
  reproducibility_runs_passed: 0
  parent_must_reproduce:
    - create_admin_scale
    - check_admin_scale
    - update_admin_scale
    - refresh_admin_scale_on_every_admin_pass
    - preserve_9_components
  unresolved_scaffold_only_behavior: []
  may_deprecate_after_ilya_approval: true
  may_remove_after_rollback_note: true
```

Do not delete this skill automatically. When the parent `admin` skill has reproduced the behavior enough times, propose deprecation/removal through `skill-system-governance`.

## Core model

Administrative scale has 9 components:

1. Goal — what must be achieved.
2. Purpose — why this should exist and whose benefit it maximizes.
3. Policy — boundaries, rules, and operating principles.
4. Plans — timing, scope, cadence, sequence.
5. Programs — the change mechanisms or transformation streams.
6. Tasks — concrete actions, owners, and near-term execution.
7. Valuable final product — what is created for whom and with what value.
8. Ideal scene — how success looks in observable terms.
9. Statistics — leading and lagging indicators.

## How to use it

When building an administrative scale:

1. Separate state from intervention.
2. Distinguish project packages from raw hypotheses.
3. Treat each package as a manageable change unit, not as a loose idea.
4. Write in operational language, not abstract theory.
5. Make every component decision-relevant.

## Recommended workflow

1. Identify the negative state or target state.
2. Define the project package that responds to it.
3. Fill the 9 components in order.
4. Keep `Programs` and `Tasks` distinct:
   `Programs` = change mechanisms.
   `Tasks` = immediate actions.
5. Make `Ideal scene` observable.
6. For `Statistics`, include both leading and lagging indicators.

## Special rule for hypothesis maps

If the source is a hypothesis map:

- branches may mean causality;
- branches may also mean a valid management response;
- blue or explicitly separated right-side blocks should be treated as project packages if the user frames them that way.

In that case:

1. first read the map as `state -> drivers/responses -> project packages`;
2. then write one administrative-scale entry per project package.

## Output preference

Default output per package:

- Goal
- Purpose
- Policy
- Plans
- Programs
- Tasks
- Valuable final product
- Ideal scene
- Statistics

If the user wants a shorter version, compress to:

- Goal
- Purpose
- Main mechanism
- First actions
- Success criteria
