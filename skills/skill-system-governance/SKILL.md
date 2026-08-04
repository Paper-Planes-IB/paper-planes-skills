---
name: skill-system-governance
description: Use when Ilya asks to inspect, improve, select, create, deprecate, or route local Codex skills as a system; when external researcher feedback returns about skills; when deciding whether a pattern should become a skill, section, rule, eval, or no-op; or when running the inspect, improve, external prompt, return packet, accepted patch loop.
metadata:
  status: active
  line: APQ-23 / skill system governance
  owner: Ilya
  originator: Илья Балахнин
  created: 2026-05-30
---

# Skill System Governance

## Purpose

Own the system-level loop for Codex skills: inspect the current skill base, extract universal improvements from reflections, prevent skill sprawl, prepare external researcher prompts, receive external decision packets, apply accepted patches, and require eval coverage for every material change.

This skill is a governor, not a domain worker. It should not do the primary work of `deepresearch`, `competitor-research`, `ingest`, `admin`, `cordos`, or another operating skill. It decides what should change in the skill system and routes the change through approval, eval, and verification.

## Non-goals

Do not:

- patch skills directly from external feedback before Ilya accepts the change;
- create a new skill when a section, mode, gate, output contract, or eval case inside an existing skill would solve the problem;
- treat project-specific, client-specific, or industry-specific feedback as a universal skill rule without cleanup;
- create Vault files, task records, automations, or rules unless Ilya explicitly asks and the relevant skill gate allows it;
- use CORD Task OS as the primary home for new executable tasks.

## Trigger Conditions

Use this skill when Ilya asks to:

- inspect the skill system or "чат inspect skills";
- choose the next skill to improve;
- prepare a prompt for an external researcher to improve a skill or the skill system;
- process an external review of skills;
- decide whether to create a new skill or extend an existing skill;
- accept, change, defer, reject, deprecate, or remove skill changes;
- add evals, regression cases, lifecycle states, or cross-cutting standards to skills.

Do not use this skill for a normal domain task merely because a skill is involved. Use the domain skill directly, and call governance only when the skill system itself is being changed or evaluated.

## Governance Loop

Run the loop in this order:

1. `inspect`: identify target skill(s), adjacent skills, current status, and likely risk.
2. `cleanup`: if the input is reflection or external feedback, remove client, project, industry, geography, competitor, product, and one-off facts unless they reveal a reusable failure mode.
3. `route`: decide whether each improvement belongs in an existing skill, a new skill, a cross-cutting standard, a global rule, Vault knowledge, Codex Project Task Inbox, or no-op.
4. `anti-sprawl`: default to extending an existing skill unless a standalone repeated job-to-be-done, trigger, output contract, and eval set exist.
5. `eval-first`: require eval cases before accepting a material patch.
6. `proposal`: return a patch backlog with accepted / change / defer / reject disposition.
7. `writeback`: apply only the accepted scope after Ilya's approval.
8. `verify`: validate edited skills and report the delta.

## Modes

| Mode | Trigger | Output |
|---|---|---|
| `system-inspect` | broad review of skill system | skill map, gaps, next skill candidate |
| `skill-reflection-ingest` | self-reflection / improvement notes returned | universal improvement list after specificity cleanup |
| `external-return-router` | external researcher returned advisory packet | accepted/change/defer/reject decision packet |
| `anti-sprawl-review` | proposed new skill or duplicate behavior | create / extend-existing / no-op decision |
| `patch-planning` | Ilya asks to implement accepted changes | scoped patch plan + eval requirements |
| `lifecycle-review` | deprecate, delete, revive, or scaffold skill | lifecycle decision + reproducibility checklist |
| `cross-standard-review` | repeated contract across skills | proposed reusable standard and target skills |

## Cross-Cutting Standards

Prefer reusable contracts over copy-pasted local variants.

```yaml
preflight:
  action_type: write|externalize|create_file|canonize|rule_change|skill_patch|task_delta
  target: vault_path|external_model|skill_file|task_inbox|reader|automation
  sensitivity: public|internal|client_sensitive|restricted
  approval_required: true
  dlp_check: passed|failed|not_applicable
  no_op_if: ""

external_return_packet:
  source: chatgpt_pro|perplexity|notebooklm|external_researcher|other
  status: advisory
  accepted: []
  change: []
  defer: []
  reject: []
  data_gaps: []
  risk_gaps: []
  writeback_targets: []
  next_action: ""

self_reflection_intake:
  raw_notes: ""
  specificity_cleanup_done: true
  universal_improvements: []
  project_specific_routes: []
  disposition: accepted|change|defer|reject|pending

skill_improvement_suggestion:
  skill: ""
  failure_mode: ""
  improvement: ""
  type: metadata|workflow|preflight|output|eval|guard|lifecycle|description
  expected_effect: ""
  eval_case_ref: ""
  disposition: accepted|change|defer|reject|pending

task_delta:
  candidate_task: ""
  owner_next_action: ""
  route: codex_project_task_inbox
  status: candidate
  airtable_sync: pending_heartbeat
```

## Anti-Sprawl Decision

Before creating a new skill, answer:

```yaml
anti_sprawl_decision:
  proposed_new_skill: ""
  decision: do_not_create|extend_existing|create_after_approval
  existing_skill_to_extend: ""
  standalone_jtbd: true|false
  distinct_triggers: true|false
  distinct_output_contract: true|false
  adjacent_collision_risk: low|medium|high
  eval_cases_ready: true|false
  why: ""
```

Default decision: `extend_existing`. Create a new skill only when the behavior is repeated, bounded, evaluable, and not naturally owned by an existing skill.

## Eval Requirement

Every material skill improvement must include eval coverage through `skill-eval-harness`.

Minimum eval case pack:

- good trigger;
- bad trigger / adjacent confusion;
- ambiguous trigger;
- writeback or externalization gate if relevant;
- regression case tied to the failure that caused the patch.

Do not mark a skill patch complete if it lacks an eval case or an explicit no-op reason for eval.

## Local Skill Kit Installation

When installing a local archive or zip that contains multiple skills:

- inspect the archive manifest before writing anything;
- compare archive skill names with existing `~/.codex/skills/<skill>/SKILL.md`;
- create a timestamped backup of every existing conflicting skill before copying;
- do not blindly overwrite a living local `SKILL.md` that has newer project rules, changelog entries, or local governance; prefer preserving the current `SKILL.md` and merging missing `references/`, `assets/`, or scripts from the archive;
- if the archive contains malformed metadata, old paths such as `~/.claude`, or references to generator code that is not bundled, patch the installed `SKILL.md` to state the real Codex path and the actual runnable/non-runnable status;
- place kit-level critics, rules, or shared references inside the most relevant installed skill when there is no native global home for them, and report that placement;
- remove `.DS_Store`, `__pycache__`, and other packaging noise from the installed copy;
- verify after installation that every installed skill has a readable `SKILL.md` frontmatter with non-empty `name` and `description`.

## Lifecycle Model

Use these states:

| State | Meaning | Exit criterion |
|---|---|---|
| `experimental` | new or unstable behavior | basic eval pass |
| `review` | under structured validation | pass eval and adjacent collision checks |
| `active` | normal operating skill | stable use |
| `review-critical` | important but currently risky | redesign and eval pass |
| `temporary_scaffold` | temporary helper while behavior migrates to parent skill | reproducibility threshold met |
| `deprecated` | superseded or no longer preferred | ready for removal after rollback note |
| `removed` | deleted after approval | rollback note exists |

Temporary scaffold deletion checklist:

```yaml
deprecation:
  skill: ""
  reason: scaffold_migrated|superseded|unused|duplicate
  behavior_migrated_to: ""
  reproducibility_runs_required: 3
  reproducibility_runs_passed: 0
  unresolved_scaffold_only_behavior: []
  state: temporary_scaffold|deprecated|removed
  rollback_note: ""
  ilya_approval_required: true
```

## Task Routing Correction

Executable tasks, owner-next-actions, and tracker deltas produced by skills should route as `candidate` / `task_delta` to Codex Project Task Inbox. CORD Task OS is not the primary task home. Airtable sync is a downstream heartbeat after accepted task candidates.

Governance must flag and patch any skill that still says:

- create new tasks directly in TaskOS as the home;
- push tasks to Airtable without the Task Inbox handoff;
- report only task IDs without task substance.

## DLP / Externalization Check

Before sending prompts or packets to external models or reviewers, require:

```yaml
dlp_check:
  contains_raw_private: true|false
  contains_client_internal: true|false
  contains_project_status: true|false
  approved_to_externalize: true|false
  redaction_applied: []
  block_if: "contains_raw_private_or_client_internal_without_approval"
```

Default: if uncertain, treat the packet as `client_sensitive` and sanitize.

## Output Contract

```yaml
skill_governance_packet:
  mode: system-inspect|skill-reflection-ingest|external-return-router|anti-sprawl-review|patch-planning|lifecycle-review|cross-standard-review
  source: user|external_researcher|self_reflection|local_inspection|eval
  specificity_cleanup:
    done: true|false
    stripped_project_specifics: []
    reusable_patterns: []
  accepted: []
  change: []
  defer: []
  reject: []
  patch_backlog:
    - priority: P0|P1|P2
      target_skill: ""
      change_type: metadata|workflow|preflight|output|eval|guard|lifecycle|description
      change_summary: ""
      eval_required: true
  anti_sprawl_decisions: []
  lifecycle_decisions: []
  task_inbox_routing_checks: []
  dlp_notes: []
  next_action: ""
```

## Done Definition

Done when:

- project/industry-specific reflection is cleaned before skill-level use;
- each improvement is routed to skill / section / standard / rule / Vault / Task Inbox / no-op;
- new-skill creation passes anti-sprawl review;
- material patches have eval cases;
- accepted changes are scoped and verified;
- final answer reports what changed, what was deliberately not changed, and which files were validated.

Not done if:

- it patches from external feedback without Ilya approval;
- it creates a new skill for a section-sized behavior;
- it leaves old TaskOS-as-home assumptions in a skill;
- it accepts a skill improvement without eval coverage;
- it stores project-specific strategy as a universal skill rule.
