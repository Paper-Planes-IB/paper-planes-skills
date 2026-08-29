# Verified throughput control

Use for repeatable production, migration, retrieval and knowledge-processing
loops. The control prevents long exploratory turns from being mistaken for
progress.

## Before the first action

Declare:

1. one useful unit;
2. the expected unit denominator;
3. the unchanged quality contract and per-item evidence;
4. a first-delta time budget;
5. the source register or exact-set that discovery will populate.

Run `loopctl throughput-gate --input <receipt.json>`. Production is not admitted
when the contract is missing.

## First-delta rule

The first bounded pass must produce either one verified useful unit or an exact
blocker. Tool calls, generated drafts, sent messages and created files are not a
delta until their required QA/effect evidence exists.

- After two routes without a verified delta, stop and use
  `replan_from_current_state`.
- Any context compaction before the first verified delta is a throughput
  incident and also routes to `replan_from_current_state`.
- Discovery results go into the declared source register. Production consumes
  that register; it does not repeat the same searches after recovery.

## Closeout receipt

Record:

```text
useful_unit
expected_units
verified_units
quality_contract
per_item_evidence_count
first_verified_delta_sec
end_to_end_sec
steady_state_sec
sergey_interventions
actions_without_delta
routes_without_delta
context_compactions_before_first_delta
```

Report both end-to-end and steady-state rates when setup or recovery is
material. Never compare rates across different work classes or weaker quality
contracts.

Promotion from `canary` to `effect_check` must carry the validated receipt as a
typed `receipt://throughput/...` evidence reference. The lifecycle transition
rejects promotion without it.
