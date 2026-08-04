---
name: graph-analysis
description: Inspect, validate, navigate, and maintain Graphify/Vault knowledge graphs. Use when Codex works with graphify-out/graph.json, project God nodes, cross-project hubs, graph.html visualization, Graphify merge/enrichment, link prediction, duplicate candidates, bridge nodes, graph quality, graph-first navigation before reading many Vault files, or questions like "why is this node central?", "which projects use Bitrix?", "trace path between projects", "compare projects", "find under-enriched projects", and "validate graph quality".
---

# Graph Analysis

Use this skill for graph-first work over Vault/Graphify graphs. The graph is a navigation index: inspect it before reading many files, then read only the artifacts selected by the graph.

## Current Graphify Schema

The current Vault graph uses Graphify-style JSON:

- Top-level keys: `nodes`, `links`, optional `hyperedges`, optional `graph.hyperedges`.
- Node identity: `id`, `label`.
- Current role fields: `node_role` (`project_god`, `cross_project_hub`, `project_card`) and `project`.
- Current type fields: `file_type`, `artifact_kind`; target model may add `node_type`.
- Edge fields: `source`, `target`, `relation`, `confidence`, `confidence_score`, `source_file`, `project`.
- Some future graphs may add `as_of`, `evidence`, `node_kind`, `last_seen`, or stricter confidence levels. Use them when present, but do not require them for current Graphify exports.

Treat `node_type` as canonical when present. Otherwise map:

- `node_role: project_god` -> `project`
- `node_role: cross_project_hub` -> `hub`
- `artifact_kind` or `file_type: document|paper|image` -> `artifact`
- `file_type: concept|rationale` -> `concept`

## Hard Rules

- Project God nodes are only named projects: `Проект: <Название>`.
- System components such as `1C`, `Bitrix`, `BPM`, `медицина / экономика клиник` are cross-project hubs, never project God nodes.
- Do graph-first navigation before broad file reading.
- Read files only after an ego graph, path trace, hub query, or project listing identifies relevant artifacts.
- Do not merge, rebuild visualization, delete nodes/edges, infer new edges, or update graph attributes without explicit user approval.
- If graph data is stale or structurally weak, say so before using it.
- Link prediction, duplicate detection, and bridge detection produce candidates only. They are not facts until checked against source artifacts.
- For centrality questions, classify the node role first. A high-degree hub is not a central project.
- Avoid all-node visual interpretation when the graph is large. Prefer portfolio, hub, project ego, or weak-signal views.

## Quick Workflow

1. Locate `graphify-out/graph.json` in the current directory or the user-provided path.
2. Run `scripts/graph_inspector.py inspect <graph.json>`.
3. If answering about a project, run `explain` or `ego` on `Проект: <name>`.
4. If answering about a cross-project system, run `list-hubs` or `explain` on the hub.
5. Read only the artifact files surfaced by the graph.
6. For write-back, ask for approval and show the planned delta first.

## Commands

Run from any directory:

```bash
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py inspect graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py list-gods graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py list-hubs graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py components graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py vip graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py bridges graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py weak-nodes graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py enrich-next graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py link-predict graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py monoculture graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py explain graphify-out/graph.json "Проект: БТК"
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py compare graphify-out/graph.json "Проект: Амиго-Груп" "Проект: БТК"
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py duplicates graphify-out/graph.json
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py ego graphify-out/graph.json "Проект: БТК" --depth 2
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py trace graphify-out/graph.json "Проект: Амиго-Груп" "Проект: БТК"
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py validate graphify-out/graph.json
```

Use `--json` when another script should consume the output.

## Analysis Recipes

### Why Is This Node Central?

Run `explain`. Report node role/type, degree, project neighbors, hub neighbors, top adjacent artifacts, and whether its centrality is structural or semantic.

If the node is a hub, explicitly say: "This is a cross-project hub, not a project God node."

Choose the metric by question:

- Degree: "what is this node connected to?"
- Hub spread: "which projects share this system/topic?"
- Bridges/articulation: "what would disconnect parts of the graph?"
- Jaccard/common neighbors: "which projects are structurally similar?"
- Link prediction: "which candidate connection should we verify next?"

### Which Projects Use A Hub?

Run `list-hubs`, then `ego <hub> --depth 1`. Return project neighbors and confidence/source examples. Do not treat mere low-confidence `references` as strong operational dependency.

### Compare Two Projects

Run `compare`, then `trace` if needed. Compare neighboring hubs, concepts, and optionally artifacts. If the shortest path goes through a generic hub (`BPM`, `1C`), warn that this may be a weak generic bridge and check edge confidence/source files.

### Find Bridges

Run `bridges`. Treat results as structural candidates. A bridge is useful only when it connects project clusters or high-value concepts; a bridge through a generic hub may be a visualization artifact.

### Find Weak Or Isolated Nodes

Run `weak-nodes`. Use it for enrichment planning: dangling artifacts, tiny components, and low-degree project anchors often indicate missing `project_contains`, source evidence, or canonical hub links.

### Find Duplicate Candidates

Run `duplicates` for exact normalized-label candidates. Use `--fuzzy` only for exploratory review. Never merge automatically; show candidates and ask for approval before any alias update or node merge.

### What Should We Read?

Run `ego <project> --depth 2`, filter neighbors to artifacts with relations such as `project_contains`, `rationale_for`, `evidence_for`, `implements`, `references`, then read only those `source_file` paths.

### Which Project To Enrich Next?

Use `list-gods`. Prefer projects with low enrichment (few non-skeleton semantic nodes), high hub connectivity, and active/recent project context. The current graph may not have `enrichment_score`; approximate by project God degree, count of semantic non-artifact neighbors, and local `graphify-out/graph.json` existence.

### Link Prediction Mode

Use `link-predict` when Ilya asks for missing links, reuse candidates, graph development, knowledge graph completion, or whether projects/processes should be connected.

This is a recommendation mode, not an automatic write-back mode:

- Output candidates only: `(source, target, suggested relation, score, why)`.
- Never add predicted edges to `graph.json` without a separate explicit approval.
- Treat generic hubs (`BPM`, `1C`, `Bitrix`) as weak evidence unless the candidate also has specific shared concepts, artifacts, or rare hubs.
- Prefer recommendations that create managerial value: cross-project reuse, duplicate detection, missing evidence, missing hub/process, or a project that needs enrichment.
- For each accepted candidate, read the source artifacts before writing an edge. If evidence is not strong enough, record it as a question or no-op rather than a fact.

Recommended MVP command:

```bash
python ~/.codex/skills/graph-analysis/scripts/graph_inspector.py link-predict graphify-out/graph.json --min-common 2 --limit 20
```

Interpretation:

- `common` = shared neighbors.
- `specific` = shared neighbors after filtering out very broad hubs.
- `jaccard` = overlap share between neighbor sets.
- `score` = structural recommendation score with generic hubs downweighted.
- `why` = the shared neighbors that explain the candidate.

By default, `link-predict` suppresses candidates whose only shared neighbors are broad generic hubs with degree >= 20. Use `--allow-generic-only` only for diagnostics, because those rows usually mean "the graph needs more specific cross-project hubs or canonical concepts" rather than "these projects should be linked now."

Use high-scoring candidates as a graph development queue: links to verify, hubs to create, duplicates to review, and artifacts to read next.

## Quality Checks

Always check:

- God node rule: every project node label starts with `Проект:`.
- Hub isolation: no hub has project role/type.
- Confidence: warn about edges with `confidence_score < 0.5`.
- Freshness readiness: warn when many edges lack `as_of` / `captured_at`; current Graphify exports may not have those fields yet, so treat this as a yellow backfill signal, not a blocker.
- Connectivity: project God nodes should have at least 3 `project_contains` edges, unless intentionally skeleton.
- Schema drift: warn if nodes lack both `node_type` and `node_role`.
- Dangling edges: every edge endpoint must exist as a node.
- Hairball risk: for portfolio visualization, prefer project + hub views or project ego views over all nodes.

## Visualization Guidance

- Portfolio view: project God nodes + cross-project hubs.
- Project drill-down: ego graph around one `Проект: X`.
- Hub map: one cross-project hub and its project neighbors.
- Weak-signal view: low-degree nodes and tiny components.
- Do not rely on an all-node force graph for sensemaking when the graph exceeds roughly 500 visible nodes; use filters or ego views.

Default visual interpretation:

- Node size = degree, but clamp very large hubs mentally.
- Node color = community when available.
- Dashed/low-confidence/stale edges should be treated as candidates, not facts.
- Every visualization should have a one-sentence interpretation, not just a link.

## Advanced Backlog

Do not implement these unless Ilya explicitly asks:

- Neo4j or other graph database layer.
- Node embeddings, GraphSAGE, node2vec, or ML entity resolution.
- LLM community summaries / full GraphRAG global search.
- Automated write-back, cron maintenance, or mutation without approval.
- Contradiction graph or temporal versioned graph.

## References

- For architecture notes and the full research packet, read `references/architecture.md`.
- For non-obvious portfolio questions and how to operationalize them, read `references/smart-questions.md`.
- For deterministic inspection, run `scripts/graph_inspector.py`.
