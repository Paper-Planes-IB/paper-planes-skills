# Weekly session meditate

## Purpose

Turn one week of real Codex work into a small set of verified process
improvements. The review covers varied task families and judges value by errors
prevented, time to verified result, repeated corrections, review burden, cost,
and useful silence.

## Sample

Use recent active and completed tasks. Include several task families when they
exist: client production, research, data or models, project management,
knowledge work, software, personal operations, and automation.

Prefer tasks containing:

- a material Sergey correction;
- a failed or reopened gate;
- a long run or repeated action without a durable delta;
- sibling tasks sharing one artifact or source of truth;
- an external write or publication;
- a useful `no_op`;
- an open-source adoption attempt.

Record structural evidence and task references. Keep raw client content and
emotional wording outside shared telemetry.

## Classification

For each incident choose one primary defect and one carrier:

- local correction;
- reference example;
- method module;
- workflow skill;
- domain overlay;
- validator;
- eval fixture;
- orchestration recipe;
- independent reviewer;
- policy;
- no durable write.

Treat the following as separate regression classes:

1. `iteration_advanced_before_human_gate`;
2. `multiple_user_visible_owners_for_one_work_item`;
3. `technical_status_without_human_decision_surface`;
4. `external_components_adopted_without_individual_trials`;
5. `formal_qa_without_business_relevance`;
6. `repair_without_invariant_sweep`;
7. `repeated_action_without_durable_delta`;
8. `source_of_truth_or_lineage_drift`.

## Value-first priority gate

Rank problems before investigating or repairing them. Keep four values separate:

1. user importance and observable loss;
2. evidence confidence;
3. expected effect;
4. tractability.

Ease of repair cannot raise importance. Sergey's explicit 0-10 importance rating
overrides the machine score. A problem below 7/10 receives local cleanup at most;
it cannot consume a systemic improvement cycle.

The machine score uses six 0-10 dimensions: result-quality loss 30%, weekly time
loss 25%, cognitive burden 15%, recurrence and reach 15%, safety or irreversibility
10%, and resource degradation 5%. Report the underlying dimensions and the
expected weekly loss. Never turn the weighted number into false precision.

Before starting work, check ownership. When another task already owns the same
experiment, send it new evidence and stop. Parallel work requires a distinct
untested hypothesis, independent evidence or a real permission boundary.

System work at 7/10 or higher still needs an effect metric. Evidence confidence
below 0.70 routes to evidence collection. Tractability remains visible for
planning and never changes problem importance. Use
`hudi_loop_engineering.problem_priority.evaluate_problem_priority` for the
deterministic route.

## Improvement depth gate

Do not equate a new instruction, skill, validator, unit test, dashboard or
decision-queue entry with an improvement in Sergey's work. Grade every repair
by the strongest sequential proof it has actually reached:

| Depth | Required proof | Allowed claim |
|---|---|---|
| L0 | durable carrier exists | documented |
| L1 | historical regression passes offline | tested offline |
| L2 | the control is on the mandatory runtime path | connected |
| L3 | a live task was detected or blocked before the defect reached Sergey | live effect proved locally |
| L4 | a later independent session avoided the same defect and the result was checked | systemic improvement proved |
| L5 | at least five independent live cases, false positives at or below 15%, and rollback proved | stable system change |

The levels are sequential. A later receipt cannot compensate for a missing
runtime connection. Report the current depth, the next missing proof and the
human burden that remains. Use
`hudi_loop_engineering.improvement_depth.evaluate_improvement_depth` for the
deterministic decision.

For weekly root-cause selection, prioritize production families before
administrative workflow polish:

1. repeated defects in client-facing meaning, writing or visual output;
2. repeated loss of accepted artifact purpose, evidence or manual edits;
3. artifact and file proliferation that damages the project workspace;
4. recurring user rework and supervision burden;
5. administrative inconvenience and interface noise.

An easier repair does not outrank a harder problem. User importance overrides
the machine score.

## Continuous production-quality program

Start with four standing directions and keep their evidence separate:

1. copywriting;
2. slides;
3. artifact hygiene;
4. the improvement loop itself.

Use `policies/continuous-quality-program.yaml` for outcomes, release gates,
promotion thresholds and the terminal condition. The build phase ends when all
four directions reach L5. The steady state continues as bounded Kaizen: silent
daily observation, local reversible repair, cross-session effect checks and
weekly promotion or retirement of controls. Feature growth is not a goal.

These directions are initial swimlanes, not a closed taxonomy. A materially
different repeated defect can open a new swimlane after deduplication, a named
outcome metric and a distinct release gate. Use one Kanban:

`intake -> evidence -> ready -> implementation -> shadow -> canary -> effect_check -> stable`.

Verified controls leave active work. Every 30 days they return through
`review_due` for retain, recalibrate, rollback or retire. Failed controls use
`rollback`; rejected or obsolete controls use `retired`. Keep the existing
Improvement Queue as the source of truth and project it with
`hudi_loop_engineering.quality_kanban`; do not create another backlog.

Kanban movement is a control receipt, not the improvement outcome. Every active
candidate must name the carrier actually changed: documentation, YAML policy,
skill, validator, eval, hook, automation prompt, artifact rule or other
executable behavior. Promotion to effect check requires that changed carrier and
a fresh task observation.

Any new or materially changed automation follows
`policies/automation-commissioning.yaml`: two reviewed manual runs with a repair
between them, accepted canary, rollback proof, owner task and outcome metric.
Keep it paused until all gates pass. A schedule is deployment, not verification.

## Action policy

Apply a reversible task-local or project-local repair when evidence, rollback,
and an effect check exist. Shared skill, validator, eval, permission, schedule,
or global policy changes require the user's explicit request or review.

Every external component receives its own exact-revision intake, real Job Story,
locked metric, rollback, and accept/reject verdict. A batch comparison can
shortlist components. Adoption remains sequential so the measured effect is
attributable.

## Human surface

Return:

1. the week's main conclusion;
2. repeated defects and affected task families;
3. improvements already applied and their verification;
4. the open-source radar with `adopt_safe`, `adapt_with_cuts`, `quarantine`, or
   `reject`;
5. at most one critical decision for Sergey;
6. the next bounded effect check.

Technical receipts and paths appear last. A clean review may return `no_op`.
