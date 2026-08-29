# Operating contract

## Intervention ladder

Always reason through the complete ladder so the plan has a credible route to completion.

| Level | Meaning | Default authority |
|---|---|---|
| A0 | Observe and record | autonomous |
| A1 | Recommend or clarify context | autonomous |
| A2 | Request evidence or apply a reversible task-local repair | autonomous with effect check |
| A3 | Pause, replan or materially change scope | human decision before execution |
| A4 | Change task state, artifact policy, shared skill, rule, validator or eval | human review; local project exceptions require explicit standing policy |
| A5 | External, irreversible, destructive, financial, permission or publication action | explicit human approval immediately before action |

The MVP runtime action cap may be lower than the designed ladder. State both the recommended level and the currently executable level.

## Correction routing

- `revise_current_iteration`: a current acceptance criterion failed. Repair and repeat its verification.
- `advance_with_comment`: the current criterion remains satisfied and the comment belongs to a later quality layer.
- `replan_from_current_state`: objective, audience, artifact purpose or source of truth changed. Preserve useful work and replace the remaining plan.
- `clarify_route`: overall confidence is below 0.95 and the options lead to materially different results.

## Improvement carrier

Choose from observable work:

1. local decision;
2. reference example;
3. method module;
4. workflow skill;
5. domain overlay;
6. validator;
7. eval fixture;
8. orchestration recipe;
9. independent reviewer;
10. policy;
11. no durable write.

A separate method needs stable inputs, outputs, trigger and quality criteria. A reviewer needs a different evidence set or blocking right and must improve material-error detection or time to verified result. Project, industry and task-family scope are hypotheses until supported by varied cases and counterexamples.

## Effect proof

Use the lifecycle:

`created -> delivered -> acknowledged -> applied -> effect_verified`

Only `effect_verified` closes an improvement. Require a fresh state, valid evidence reference, unexpired recommendation and an observable delta in outcome, error, time, cost or review burden.

## Incident compilation

After a material failure is confirmed, compile the bounded Codex trajectory
into a redacted IR and regression fixture. Detection alone cannot establish the
failure: the incident needs human, validator or independent-review confirmation.
The critical step is the earliest material violation that explains the confirmed
correction. A compiler fallback stays scoped to the explicit defect class in the
descriptor. Review task-family, shared-skill, cross-project and global promotion
before changing their carrier.

### Protected-invariant sweep after repair

Every repair rechecks the properties that must remain stable while the target defect changes:

1. Job Story, audience and decision to enable;
2. source of truth and evidence relevance;
3. accepted artifact lineage, editability and representation;
4. accepted storyline, visual grammar and client vocabulary;
5. project boundary, owner route and client stage;
6. previously passed gates that the repair could invalidate.

If the original editable source is missing, use `source_gap`. A reconstruction may be useful working material, but it stays outside accepted lineage until its method is disclosed and independently compared with the accepted artifact. A screenshot, PDF page or raster background embedded into HTML is a representation substitution and must never be reported as restored editable HTML.

Production begins after the required meaning gate passes. Examples include an accepted storyline for a proposal, a source-backed decision structure for a client document, and an accepted metric definition for a dashboard. Formal QA cannot promote an artifact while business relevance remains unchecked.

## Work-quality admission

Run `loopctl work-quality-gate --input <packet.json>` before a material
production action or readiness promotion. The packet contains structural fields
and evidence references. Keep client text outside shared telemetry unless the
validator runs task-locally.

1. **Current criterion.** Every required criterion of the current iteration has
   a receipt before production begins. Later gates cannot compensate for a
   failed current criterion.
   If the session itself declares a Human Gate before the action, record the
   passing decision and its evidence reference. The user's existing instruction
   can satisfy the gate when it already authorizes that exact action.
2. **User-provided source.** Attempt the exact URL or file first. After failure,
   attempt the declared connector, browser, export or authenticated fallback.
   `source_gap` becomes valid after both attempts have receipts.
3. **Existing artifact.** Record expected unit count, allowed unit IDs, protected
   manual edits, purpose and rollback. Any extra slide, page, file or hidden unit
   blocks the change.
4. **Client language.** Before `client_ready`, resolve internal codes, unexplained
   abbreviations, undefined metrics, service statuses and claims that require an
   oral explanation to become intelligible.
5. **Skill release.** Compare local and cloud versions, dependency closure and
   absolute paths. Require security scan, generated package, smoke test and
   red-team test. Show the diff and evidence to Sergey before upload. The existing
   `hudi-agent-system` package generator remains the delivery mechanism.
6. **Completion claim.** Before saying that a scope is all, complete, ready,
   installed, checked or verified, record its expected count, proved count,
   unknown count and evidence references. `checked` and `verified` require
   per-item evidence. Keep discovered, indexed, prepared, installed and verified
   states separate. Use a quantified partial statement when coverage is partial.

## Loop budget

Set bounds for iterations, time, tokens, concurrent processes, transient artifacts and attempts without a durable delta. Stop or clean up after two iterations without new evidence or a durable result unless the user explicitly extends the budget.
