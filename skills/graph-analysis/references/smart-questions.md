# Smart Questions For Project Graphs

Use these questions when a user wants insight beyond a neighbor list. Start with deterministic graph metrics, then read files only after graph narrowing.

## MVP Questions

### 1. Which portfolio areas live in parallel worlds?

Command: `components`.

Return connected components, project God nodes inside each component, and major hubs/artifacts. Interpret multi-project components as islands.

### 2. If we remove central hubs, who becomes important?

Command: `vip`.

Exclude cross-project hubs and rank non-hub nodes by bridge-like score. In MVP, approximate with degree after removing hubs; when NetworkX is available, use betweenness.

### 3. Where are structural holes?

Approximation: compare project pairs that share hub themes but have no short path except through generic hubs. Report as candidates, not facts.

### 4. Which projects are under-enriched but query-important?

Command: `enrich-next`.

Rank project God nodes by low semantic enrichment and high hub connections. Recommend the next projects to enrich for token savings.

### 5. Where are monocultures?

Command: `monoculture`.

Find projects whose cross-project links mostly go through one hub. Treat this as dependency risk, not error.

### 6. Which edges need source-check?

Use `validate --min-confidence 0.5` and inspect low-confidence edges. Prioritize edges that cross project/community boundaries.

### 7. Which nodes look anomalous?

Compare degree with inferred type. Suspicious patterns:

- artifact with very high degree;
- project God with very low `project_contains`;
- hub with `hub_spread < 2`;
- concept that acts like a hub but lacks hub role.

### 8. What should we read to answer cheaply?

Use `ego <project> --depth 2`, then read only source files attached to artifact, evidence, rationale, or task-like nodes surfaced by the ego graph.

## Advanced Questions

These require snapshots, stronger typing, or LLM/GraphRAG:

- Which nodes grew sharply in centrality over the last N days?
- Which decisions are hanging: evidence exists, but no implementation edge?
- Which successful-looking projects lack evidence density?
- Which methodology concepts dominate 5-ka but are absent in 4-ka projects?
- Which old central nodes lost influence without replacement?

## Answer Format

For each smart question, answer with:

- finding;
- metric used;
- top nodes/projects;
- confidence caveat;
- what files to read next, if any;
- whether the graph needs enrichment before trusting the answer.
