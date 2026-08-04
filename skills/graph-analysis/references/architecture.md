# Graph Analysis Architecture Notes

This reference captures the current decision packet for Vault/Graphify graph analysis.

## MVP Position

- Use local JSON + Python inspection first.
- Do not require Neo4j, embeddings, GraphRAG, or external APIs for MVP.
- Graphify's `graph.json` is enough for navigation, validation, path tracing, project God node checks, hub checks, and ego-graph narrowing.
- Microsoft GraphRAG is a useful advanced architecture model, but it requires LLM-based indexing and is not the MVP.

## Target Node Model

Target `node_type` values:

- `project`: named project God node. Label format: `Проект: <Название>`.
- `hub`: cross-project system/theme, for example `1C`, `Bitrix`, `BPM`, `медицина / экономика клиник`.
- `artifact`: file/document/report/deck/spreadsheet/PDF.
- `evidence`: source, interview, contract, external research.
- `task`: task or decision item.
- `concept`: concept, method, storyline, product idea.
- `data`: dataset, registry, spreadsheet, metrics source.

Current graph compatibility:

- `node_role: project_god` approximates `node_type: project`.
- `node_role: cross_project_hub` approximates `node_type: hub`.
- `artifact_kind` and `file_type: document|paper|image` approximate `artifact`.
- `file_type: concept|rationale` approximate `concept`.

## Target Edge Model

Core edge relations:

- `project_contains`: project -> artifact/task/concept.
- `uses_cross_project_hub`: project -> hub.
- `references`: any -> any.
- `implements`: task/artifact -> concept.
- `rationale_for`: artifact/evidence -> decision/task/concept.
- `shares_data_with`: project/artifact -> project/artifact.
- `semantically_similar_to`: weak semantic relation; treat carefully.
- `evidence_for`: evidence -> claim/artifact.
- `depends_on`: task/project -> task/artifact.
- `updates`: newer artifact -> older artifact.
- `no_op_reason`: decision -> context.

## Key Methods

MVP:

- Degree centrality: fast first pass, but can confuse hubs and projects without typing.
- Betweenness centrality: useful for bridges and cross-project hubs; cache on larger graphs.
- Connected components: detect isolated projects and graph islands.
- Ego graph: cheapest useful context for project drill-down.
- Shortest path: explain relation between two projects/nodes.
- Articulation points/bridges: identify critical structural dependencies.
- Louvain/community detection: useful when available, but not required for every answer.
- Fuzzy entity resolution: use name normalization and neighbor overlap before LLM.

Advanced:

- Graph embeddings.
- Microsoft GraphRAG-style summarization.
- Neo4j/GDS.
- Temporal graph diff.
- Automated contradiction detection.
- Interactive dashboards beyond Graphify HTML.

## Approval Gates

Require explicit user approval before:

- Merging a local project graph into a master graph.
- Rebuilding `graph.html`.
- Deleting a node or edge.
- Updating graph attributes.
- Auto-inferring new semantic edges.

Read-only inspection does not require approval.

## Practical Recipes

### Explain A Node

Show:

- role/type
- degree
- hub/project neighbors
- top artifact neighbors
- low-confidence adjacent edges
- source files for important edges

### List Cross-Project Hubs

Filter `node_type == hub` or `node_role == cross_project_hub`. Compute `hub_spread` as count of adjacent project God nodes.

### Find Under-Enriched Projects

Approximate `enrichment_score` when missing:

- Has local `graphify-out/graph.json`: enriched.
- Count semantic nodes where `project == project_name` and not only skeleton artifacts.
- Count `project_contains` edges.
- Count cross-project hubs.

### Avoid Hairball Visualization

For a large portfolio:

- Start with project + hub view.
- Use ego view for one project.
- Hide degree-1 artifacts unless requested.
- Use confidence threshold when possible.

## Known Gaps In Current Graph

- No uniform `node_type` yet.
- No persisted `enrichment_score` yet.
- Some graph nodes use `file_type` where `node_type` should eventually exist.
- `confidence_source` is not consistently present.
- Staleness fields are not consistently present.
