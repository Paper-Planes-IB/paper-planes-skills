---
name: skill-eval-harness
description: Use when reviewing, pressure-testing, or regression-testing local Codex skills, their descriptions, trigger boundaries, adjacent-skill collisions, lifecycle status, or writeback behavior
metadata:
  status: active
  line: APQ-23 / skill quality / evals
  owner: Ilya
  originator: Илья Балахнин
---

# Skill Eval Harness

## Purpose

Test whether a local Codex skill will be selected, bounded, and executed safely before it becomes or remains a reliable APQ asset.

This skill is a harness, not an executor. It produces eval cases, failure reports, routing observations, and patch backlogs for `SKILLS.md`, `SKILL.md-standard.md`, and individual `~/.codex/skills/*/SKILL.md` files.

## Non-goals

This skill must not:

- rewrite skills automatically without Ilya's explicit approval;
- create new skills just because a boundary is unclear;
- recommend a new skill before checking whether an existing skill, mode, gate, output contract, or eval case can absorb the function;
- replace the weekly APQ-review automation;
- treat external model feedback as canon;
- score people or contribution value directly;
- mutate Vault, rules, CORD, or skills without a writeback gate.

## Trigger Conditions

Use this skill when Ilya asks to:

- test a skill, description, trigger, or boundary;
- check whether two skills collide;
- build eval cases for a skill;
- review high-risk skills before rewriting;
- verify whether a proposed skill patch improves routing;
- evaluate `description` quality, negative triggers, writeback behavior, or lifecycle status;
- perform anti-sprawl review before creating or accepting a new skill;
- run a weekly/APQ skill review with evidence.

Do not use this skill when the user wants the primary work itself: writing a proposal, doing research, summarizing a chat, routing knowledge, or drafting content. In those cases, use the relevant work skill and call this harness only if a skill-quality question appears.

## Inputs

Required:

- target skill or skill group;
- eval purpose: trigger, description, collision, writeback, output, lifecycle, or regression;
- current `SKILL.md` or enough excerpt to inspect;
- adjacent skills if collision is suspected.

Optional:

- real failed prompt / misroute example;
- proposed patch;
- expected correct route;
- risk class from `SKILL.md-standard.md`;
- APQ / contribution-trace context.

If missing:

- ask for the smallest missing input if the eval cannot proceed;
- otherwise create a provisional eval pack and mark assumptions.

## Mode Router

| Mode | Trigger | Output | Adjacent skill |
|---|---|---|---|
| `single-skill-eval` | one skill is under review | eval report + patch backlog | `fix-rules` if current chat rule was violated |
| `description-eval` | trigger surface may be too broad/narrow | description findings + better trigger candidates | `cognitive-router` for routing policy |
| `collision-eval` | two or more skills overlap | collision matrix + decision rules | `cognitive-router` |
| `writeback-eval` | skill may write to Vault/CORD/rules/skills/external | writeback-risk report + gate requirement | future `writeback-governor` |
| `registry-eval` | weekly APQ skill review | registry delta + noncompliance summary | APQ automation / `SKILLS.md` |
| `anti-sprawl-eval` | a new skill is proposed or appears in the corpus | do-not-create / extend-existing / create-after-approval decision | `SKILL.md-standard.md` |
| `patch-regression` | proposed skill patch exists | before/after eval cases + expected behavior | relevant target skill |
| `system-governance-eval` | a skill-system review, external feedback packet, or cross-cutting standard is being accepted | governance eval pack + routing checks | `skill-system-governance` |

## Workflow

1. Identify target skill(s), adjacent skills, and risk class.
2. Read `description` first. Treat it as the trigger surface.
3. Read only the relevant parts of `SKILL.md`: purpose, triggers, non-goals, output, gates, boundaries, eval cases.
4. Build an eval pack before proposing patches.
5. For each eval case, specify expected route, forbidden behavior, and pass/fail criteria.
6. Run a reasoning-only simulation unless the user explicitly asks for live file/tool tests.
7. Return findings as `pass`, `fail`, `weak`, or `not-assessable`.
8. Produce patch backlog, not automatic edits, unless Ilya has explicitly approved changes.

## Output Contract

```yaml
skill_eval_report:
  target_skills: []
  eval_mode: ""
  risk_class: "no-write|candidate-only|durable-write|externalization|governance-change|mixed"
  summary: ""
  findings:
    - status: "pass|fail|weak|not-assessable"
      area: "description|trigger|boundary|writeback|output|lifecycle|evals"
      evidence: ""
      implication: ""
      proposed_fix: ""
  eval_cases:
    - case_id: ""
      prompt: ""
      expected_skill: ""
      expected_mode: ""
      forbidden_behavior: ""
      pass_condition: ""
      notes: ""
  collision_matrix:
    - user_intent: ""
      prefer: ""
      avoid: ""
      reason: ""
  writeback_gate:
    required: true|false
    reason: ""
  dlp_externalization_check:
    required: true|false
    sensitivity: "public|internal|client_sensitive|restricted|not_applicable"
    pass_condition: ""
  task_inbox_routing_check:
    required: true|false
    expected_route: "codex_project_task_inbox|not_applicable"
    forbidden_route: "taskos_as_primary_home|direct_airtable_without_inbox|not_applicable"
  lifecycle_check:
    required: true|false
    expected_state: "experimental|review|active|review-critical|temporary_scaffold|deprecated|removed|not_applicable"
    removal_criteria_present: true|false
  patch_backlog:
    - priority: "P0|P1|P2|P3"
      target: ""
      change_type: "description|boundary|output|gate|eval|lifecycle"
      proposed_change: ""
      requires_ilya_approval: true
```

## Eval Case Types

Every key skill should have at least:

- `good-trigger`: the skill should clearly activate;
- `bad-trigger`: another skill should be preferred;
- `ambiguous-trigger`: router must ask or choose a safer path;
- `description-collision`: description overlaps with another skill;
- `missing-input`: skill should ask, assume explicitly, or return not-assessable;
- `writeback-risk`: skill should stop at candidate/preview/approval.
- `anti-sprawl`: proposed skill should be rejected, folded into an existing skill, or explicitly approved as standalone.
- `task-inbox-routing`: executable tasks should route to Codex Project Task Inbox as candidate/task_delta, not to TaskOS as the primary task home.
- `external-return-router`: external ChatGPT/Perplexity/NotebookLM/researcher output should return as advisory decision packet, not as canon.
- `self-reflection-cleanup`: project/client/industry specifics should be stripped before a reflection becomes a skill-system improvement.
- `lifecycle-scaffold`: temporary scaffold skills should have parent migration and deletion criteria.

High-risk skills also need:

- premature Vault write;
- CORD false positive;
- external sensitive context;
- rule/skill mutation;
- canonicalization from external output;
- route-only vs route-and-act.
- skill-system patch without eval cases.

For any skill that creates or reviews structured analytical artifacts, add the global-contract regression pack:

- `false-broad-trigger`: ordinary proposal, report, research, strategy, KPI task, table, Mermaid request, dashboard build, or file operation must not activate structural methodology unless an in-scope analytical structure is actually created or reviewed;
- `mece-boundary`: MECE is required for a partition claiming coverage and forbidden as a generic label for timelines, registers, process flows, evidence ledgers, or arbitrary diagrams;
- `methodology-evidence-separation`: a method page or framework cannot prove a client fact;
- `frappe-bypass`: unavailable, empty, or generic Frappe cannot block work when the global contract and internal PP source are sufficient;
- `artifact-contract`: Problem Map, Issue/Hypothesis Tree, Storyline, Storyboard, Evidence Trace, Mermaid, and metric/dimension structures satisfy their required fields;
- `existing-artifact`: update the existing canonical/project artifact before creating a parallel file;
- `delta-not-rewrite`: a new source lands as appeared/strengthened/weakened/contradicted/no-change/needs-check before any full structural rewrite.

## Default High-Risk Candidates

This is a review list, not a final policy:

- `cognitive-router`;
- `ingest`;
- `tunnel`;
- `summary`;
- `cordos`;
- `partners-ingest`;
- `fix-rules`;
- `meditate`;
- `deepresearch`;
- `commercial-proposal-generator`;
- `rsvp`;
- `pp-case-writer`.

The final high-risk list should be confirmed with Ilya and then reflected in `SKILLS.md` / APQ review.

## System Governance Eval Pack

When `skill-system-governance` accepts a patch or an external researcher recommends skill changes, produce a compact regression pack before edits are considered complete:

```yaml
governance_eval_pack:
  target_change: ""
  must_include:
    - good_trigger
    - adjacent_confusion_guard
    - ambiguous_or_low_confidence_prompt
    - writeback_or_externalization_gate_if_relevant
    - regression_case_from_observed_failure
  checks:
    specificity_cleanup: pass|fail|not_applicable
    anti_sprawl_decision: pass|fail|not_applicable
    task_inbox_routing: pass|fail|not_applicable
    dlp_externalization: pass|fail|not_applicable
    lifecycle_or_deprecation: pass|fail|not_applicable
  pass_condition: ""
```

If a patch affects task routing, the harness must explicitly test that new executable tasks and owner-next-actions route to `Codex Project Task Inbox` as candidate/task_delta. It must fail any instruction that makes CORD Task OS the primary task home or bypasses the Inbox before Airtable sync.

If a patch affects external research, the harness must test that external output remains advisory and returns through accepted/change/defer/reject before any skill, Vault, rule, Reader, CORD, or automation writeback.

## Anti-sprawl Review

Before recommending or accepting a new skill, produce:

```yaml
anti_sprawl_decision:
  proposed_new_skill: ""
  decision: "do_not_create|extend_existing|create_after_approval"
  existing_skill_to_extend: ""
  why_not_new_skill: ""
  required_change_if_extending:
    - "description"
    - "mode_router"
    - "output_contract"
    - "gate"
    - "eval_case"
    - "registry_note"
  approval_required: true
```

Default decision is `extend_existing` unless the proposed skill has a standalone repeated trigger, distinct output contract, clear boundaries, eval cases, and explicit approval from Ilya.

## Writeback / HITL Gates

Codex may:

- inspect skills and registry files;
- produce eval reports;
- propose patch backlogs;
- classify risk;
- recommend lifecycle changes.

Codex must ask Ilya before:

- editing a target skill;
- changing `SKILLS.md` beyond safe registry sync;
- changing lifecycle status;
- deleting or deprecating a skill;
- creating new eval files or test suites outside the accepted location;
- treating an eval finding as canonical APQ status.

## Boundaries With Adjacent Skills

| Adjacent skill | Difference |
|---|---|
| `cognitive-router` | chooses the work route for a live user request; this harness tests whether routing rules and descriptions are reliable |
| `fix-rules` | audits rule drift in current work; this harness audits skill trigger/output/gate quality |
| `meditate` | extracts process lessons from agent behavior; this harness turns lessons into eval cases and regression checks |
| weekly APQ-review automation | runs scheduled registry review; this harness supplies the eval method used inside that review |
| future `writeback-governor` | controls durable writes; this harness tests whether skills call or respect that gate |

## Done Definition

This skill is done when:

- target skill(s) and adjacent skills are named;
- eval cases are explicit;
- description and trigger risks are assessed;
- writeback behavior is classified;
- patch backlog is prioritized;
- approval requirements are clear.

Not done if:

- it only says "looks good";
- it proposes a rewrite without eval evidence;
- it ignores `description`;
- it does not test adjacent-skill collision;
- it silently edits skills without approval.

## Anti-patterns

- Creating more skills instead of fixing a boundary.
- Treating every useful pattern as a new skill instead of adding a mode/gate/eval to an existing one.
- Treating usage count as proof of quality.
- Testing only happy paths.
- Letting `description` summarize workflow.
- Making evals so abstract that no future agent can decide pass/fail.
- Allowing a high-risk skill to write durable artifacts without preview and approval.
