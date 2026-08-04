# Archive proof-story routing

## Contents

1. Source order
2. Donor selection
3. Evidence rights
4. Mini-case format
5. Failure modes

## 1. Source order

Search the current Vault and connected workspaces in this order:

1. active project `реюз-из-архива` and `BPM Storyline-Storyboard` files;
2. approved client cases and current product-vitrine case cards;
3. archive project passports and their source artifacts;
4. knowledge-unit batches and training units as donor indexes;
5. archive of commercial proposals for offer patterns only;
6. Notion meetings, project pages and approved case material;
7. public sources for externally verifiable facts.

Use `rg --files` and `rg` for local discovery. Prefer existing donor/reuse mappings over starting from names remembered from prior conversations.

## 2. Donor selection

Score candidates on:

- same problem mechanism;
- same target lever or lever bundle;
- same research method;
- same created artifact;
- same implementation/transfer mechanism;
- comparable business model, scale or growth transition;
- industry similarity;
- evidence completeness;
- client-facing permission and confidentiality safety.

Problem, artifact and implementation fit outweigh industry similarity.

For each selected donor record:

```yaml
proof_candidate:
  donor: ""
  source_artifacts: []
  problem_fit: ""
  mechanism_fit: ""
  artifact_fit: ""
  implementation_fit: ""
  transferable_lesson: ""
  non_transferable_context: ""
  confirmed_outcome: ""
  evidence_rights: ""
  client_naming_rights: ""
  claim_reviewer: ""
```

## 3. Evidence rights

Use one status:

- `client_ready_named`: named use and claims are approved and sourced.
- `client_ready_anonymized`: mechanism and outcome may be used without the client name.
- `approach_analogy_only`: source proves the method or proposed artifact, not delivery or outcome.
- `internal_donor_only`: useful for design, prohibited in client text.
- `needs_source_check`: plausible but missing direct source or approval.
- `do_not_use`: sensitive, contradicted, weak or unsupported.

Evidence rules:

- an archived commercial proposal proves only what Paper Planes offered;
- a final deliverable can prove work performed, but not business outcome by itself;
- a project passport or knowledge unit can route to evidence, but may remain source-limited;
- an outcome claim needs an explicit result source and safe wording;
- a logo, client name or remembered anecdote is not evidence;
- never invent metrics, timing, scope, implementation depth or causality;
- if naming rights are unclear, anonymize or keep the story internal;
- distinguish “we designed”, “we helped launch”, “the client implemented”, and “the result changed”.

## 4. Mini-case format

Write a proof story primarily as a compact decision-support inset inside the page containing the supported claim:

1. **Situation:** a short, client-relevant analogous transition.
2. **Management problem:** the causal mechanism, not a generic pain.
3. **Paper Planes move:** research, design or implementation action.
4. **Concrete artifact/practice:** what existed after the work.
5. **Confirmed effect:** only what the evidence supports.
6. **Why it matters here:** the transferable lesson for the current client.
7. **Boundary:** what does not transfer and still needs verification.

Use a conclusion headline. Prefer a compact diagram, before/after mechanism, artifact fragment or decision chain over a decorative testimonial.

Create a dedicated case page only if all conditions are true:

- the story has client-facing usage rights;
- the source proves more than a proposed approach;
- the story contains enough concrete mechanism and artifact detail to stand alone;
- the case is central to the buyer's decision rather than generic credentials;
- removing the page would materially weaken the argument.

The case must support a nearby proposal claim. If removing the case changes no reader belief or decision, omit it.

## 5. Failure modes

Reject or revise when:

- donor choice is based only on industry;
- the story is a logo wall or generic credentials block;
- proposal scope is described as delivered work;
- a final presentation is treated as proof of financial result;
- unapproved client details are exposed;
- the case contains more history than transferable mechanism;
- a mini-case appears far from the claim it proves;
- a source-limited analogy is inflated into a separate page;
- several weak cases replace one properly sourced story;
- an analogy is written as a promise that the current client will obtain the same result.
