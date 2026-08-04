---
name: cord-pdca
description: Use when a project, track, product, goal, skill, decision loop, or knowledge object needs a full management cycle: align with strategy, gather decision-relevant inputs, route them through the right Vault contours, define the real control object, check against plan, review reality feedback, and improve the plan or management technology.
---

# CORD-PDCA

## Purpose

Run a closed double-loop management cycle around a control object.

This skill is not a replacement for `summary`, `tunnel`, `rail`, `cordos`, `deepresearch`, or `meditate`.
It governs the cycle above them:

- define what object is being managed;
- connect it to strategic and parent goals;
- gather only the inputs that matter now;
- route signals to the right project and Vault contours;
- distinguish `system_delta`, `open_loop`, `evidence_only`, and `no_op`;
- check against plan;
- review reality;
- change either the plan or the management technology.

## When to Use

Use when:

- there is a folder, project, track, subpassport, storyboard, product tunnel, skill, goal, or decision loop that needs active management;
- there is a lot of signal and it is unclear what matters;
- there is a `source gap`, `owner gap`, `route gap`, `writeback gap`, or `open loop`;
- a project signal must be connected to BPM-SI, knowledge, content, tasks, or strategy;
- the user needs more than a summary and more than a one-time routing pass;
- the work should improve over repeated cycles.

Do not use when:

- only a compact summary is needed;
- only a task needs to be registered;
- only knowledge routing is needed;
- only an external research prompt is needed;
- only agent reflection is needed.

## Governing Model

`CORD-PDCA` runs around a `Do-object`.

Possible `Do-object` types:

- `project`
- `track`
- `product`
- `goal`
- `skill`
- `decision-loop`
- `task-system`
- `knowledge-object`

Before acting, resolve:

- `object`
- `object_type`
- `goal`
- `parent_object`
- `owners`
- `gates`
- `artifacts`
- `rhythm`
- `success_criteria`

If the object is unclear, stop and resolve it before running the rest of the cycle.

## Cycle

### 1. Plan

Pull the frame the object must serve.

Read only what is relevant:

- `Vault/50-нормативные-документы/` for strategic anchors;
- current folder's own source-of-truth files;
- parent project files;
- accepted commitments, hypotheses, gates, success criteria.

Produce a `plan frame`:

- `primary_object`
- `parent_project`
- `local_goal`
- `parent_goal`
- `strategic_links`
- `active_commitments`
- `active_hypotheses`
- `known_gates`
- `success_criteria`
- `constraints`

### 2. Collect

Collect bounded, decision-relevant inputs around the object.

Search in this order:

1. local object files;
2. parent project files;
3. project-wide operational traces;
4. methodology and BPM/SI traces;
5. task and sync traces;
6. already-ingested external packets;
7. bounded shared-drive signals if relevant.

Filter by:

- `status relevance`
- `hypothesis relevance`
- `decision relevance`
- `gap relevance`

Produce a `typed input map`:

- `status_inputs`
- `hypothesis_inputs`
- `decision_inputs`
- `evidence_inputs`
- `task_sync_inputs`
- `external_inputs`
- `noise_candidates`

### 3. Organize

Route inputs through the structure of the system.

Organize by:

- local elements of the folder;
- tracks and subtracks;
- processes;
- task classes;
- departments and contours;
- related projects;
- signal classes.

For each meaningful signal, produce a routing decision:

- `primary_landing`
- `secondary_landings`
- `blocked_landings`
- `no_op_landings`
- `dependency_route`

The result is a `routing map`, not a narrative.

### 4. Do

Work on the control object itself.

`Do` is not "create a task".
`Do` is:

- the real control object;
- its goal;
- its operating logic;
- the exact management delta being introduced.

State:

- what is being managed;
- what the object is trying to achieve;
- how the object operates;
- what exact delta changes it now.

Typical `Do` outputs:

- project object tightened;
- track logic clarified;
- owner map corrected;
- storyboard updated;
- no-op explicitly fixed;
- knowledge object promoted;
- route shifted to the correct artifact.

### 5. Check

Check whether the current result conforms to the plan.

Check against:

- strategic frame;
- local goal;
- parent goal;
- commitments;
- gates;
- success criteria.

Output:

- `conforms`
- `partially_conforms`
- `diverges`

### 6. Review

Collect feedback from reality, not from theory.

Review:

- `worked / did_not_work / partial / unknown`
- `win / loss / defended / rejected / pending`
- `positive / negative / mixed / no_reaction`
- `process reality`
- `owner reality`
- `artifact reality`
- `evidence reality`
- `system effect`

This is where reality says how the object actually behaves.

### 7. Act

Act does not mean "do another action".
Act changes either:

- the `plan`
- or the `technology of getting the result`
- or both
- or nothing

Output:

- `change_type: plan | technology | both | none`
- `target`
- `current_problem`
- `correction`
- `next_cycle_effect`

## Double Loop

### Inner loop

`Plan -> Collect -> Organize -> Do -> Check -> Review`

Improves the object.

### Outer loop

`Check + Review -> Act -> new plan or new management technology`

Improves the way the object is managed.

Always treat this skill as a self-improving double loop.

## Loop States

Every meaningful signal must be classified as one of:

- `system_delta`
- `closed_loop_candidate`
- `open_loop`
- `evidence_only`
- `no_op`

Meanings:

- `system_delta` — writeback happened and changed the system;
- `closed_loop_candidate` — likely system change, but one more control check is needed;
- `open_loop` — the signal is real, but route, owner, gate, or writeback is not closed;
- `evidence_only` — useful material, but not grounds for operational writeback;
- `no_op` — consciously does not change the object.

## Question / Answer Engine

This skill must actively detect missing answers.

Question types:

- `source_question`
- `owner_question`
- `decision_question`
- `reality_question`
- `improvement_question`

For each missing answer, produce:

- `question_type`
- `exact_question`
- `why_it_matters`
- `blocked_object`
- `best_respondent`
- `best_source`
- `expected_answer_format`
- `needed_by`
- `can_continue_without_it: yes | partially | no`

Prioritize only:

- `must_have_now`
- `useful_soon`
- `next_cycle_check`

Do not spam the user with every possible question.

## Other Skills Invocation Matrix

Use this skill as an orchestrator. Invoke other skills only by deficit.

| Cycle block | Deficit | Use skill |
|---|---|---|
| `Plan` | parent/project map | `graphify` |
| `Plan` | compact state extraction | `summary` |
| `Plan` | concept ambiguity | `concept` |
| `Collect` | ingest source into Vault | `ingest` |
| `Collect` | partner/project update ingest | `partners-ingest` |
| `Collect` | external evidence gap | `deepresearch` |
| `Collect` | market/competitor gap | `competitor-research` |
| `Organize` | knowledge routing | `tunnel` |
| `Organize` | BPM/project routing | `rail` |
| `Organize` | task route | `cordos` |
| `Do` | project writeback | `rail` |
| `Do` | cross-contour landing | `tunnel` |
| `Do` | task registration | `cordos` |
| `Do` | system/admin change | `admin` |
| `Review` | agent/process reflection | `meditate` |
| `Act` | rule correction | `fix-rules` |
| `Act` | skill/system change | `skill-system-governance` |
| `Act` | create or revise a skill | `skill-creator` |

Do not invoke other skills because they seem adjacent.
Invoke only when the cycle exposes a concrete deficit.

## Required Output Shape

For a non-trivial run, return a compact packet with these sections:

1. `Plan Frame`
2. `Typed Input Map`
3. `Routing Map`
4. `Do-Object`
5. `Check`
6. `Review`
7. `Act`

Minimal compact schema:

```md
## Plan Frame
- primary_object:
- parent_project:
- local_goal:
- strategic_links:
- known_gates:

## Typed Input Map
- status_inputs:
- hypothesis_inputs:
- evidence_inputs:
- missing_answers:

## Routing Map
- primary_landing:
- secondary_landings:
- blocked_or_no_op:

## Do-Object
- object:
- goal:
- operating_logic:
- management_delta:

## Check
- status:
- mismatch_if_any:

## Review
- outcome:
- reaction:
- reality_gap:
- what_worked:
- what_failed:

## Act
- change_type:
- correction:
- next_cycle_effect:
```

## 4D Notes

In 4D projects:

- prefer the physical project folder as the main control surface;
- for classical mining/assemble projects, treat `BPM Storyline-Storyboard` as the canonical `Do` carrier when relevant;
- for non-classical / track-led projects without an explicit mining phase, a `Карта проблем` can be treated as a ЦВЗ-slice and interim `Do` carrier: root problems by track must connect to goals, decisions, metrics, owners, Storyline/Storyboard, and no-op/task handoff rules;
- for `New Delivery`, do not force a classical storyboard if the project uses track/subpassport/index logic as its storyboard analog;
- project journals are observability bridges, not decorative digests;
- BPM-SI and knowledge loops are downstream operating contours, not optional ornament.

## Anti-Patterns

Do not:

- turn every signal into a task;
- confuse `Check` with `Review`;
- confuse `Do` with `Act`;
- treat a summary as writeback;
- treat task creation as proof of a closed loop;
- canonize a downstream raw-pack without primary-source discipline;
- vacuum the whole Vault when a bounded collect is enough;
- invoke half the skill library without a concrete deficit;
- leave a meaningful signal without explicit classification.

## Short Canon

`cord-pdca` is a governing orchestration skill for running a self-improving double loop around a control object.

It aligns the object to strategy, gathers only the inputs that matter, routes them through the right contours, defines the real management delta, checks against plan, reviews reality, and changes either the plan or the management technology in the next cycle.
