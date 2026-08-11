---
name: paper-planes-artifact-methodology
description: Use whenever the user asks to create, plan, structure, review, or prepare any Paper Planes artifact or project deliverable, including presentations, sliduments, commercial proposals, HTML mockups, reports, research, tables, Mermaid diagrams, dashboards, instructions, project documents, client-facing materials, or artifact templates. Also use when the user mentions Paper Planes methodology, MECE, SCQA, ABCD, RDB, JTBD, PDCA/PDSA, SOSTAC, KPI, Formula of Profit, CJM, issue trees, hypothesis trees, unit economics, segmentation, positioning, customer research, growth, experiments, strategy, implementation, or asks which methodology should apply. Requires discussing the task first, naming applicable methodologies, explicitly confirming MECE for segmentation/tables/Mermaid/structures, and using the Paper Planes methodology router, Frappe knowledge base, and MD-instruction workflow.
---

# Paper Planes Artifact Methodology

## Purpose

Apply Paper Planes methodology rules before creating or planning artifacts. This skill is a router and workflow guardrail: it decides which methodology to invoke, when to read the Paper Planes Frappe knowledge base for detail, when to hand work to a specialized Paper Planes skill, and when to create or update a project MD instruction.

Do not treat this skill as an encyclopedia. Keep detailed methodology content in the Paper Planes Frappe knowledge base. Keep reference files only as routing guidance and local workflow rules.

Canonical knowledge base:

- Entry point: `https://lms.paper-planes.ru/knowledge/glavnaya`
- Canonical surface: Frappe LMS Wiki / Paper Planes knowledge base.
- Verification standard: when methodology detail matters, open and verify the relevant live Frappe Wiki page through an authenticated browser/session instead of relying on memory, Notion, or local notes.
- Access note: if the entry point redirects to login for a guest session, treat the knowledge base as available but authentication-required. Do not downgrade it to a public source gap.

## Required First Response Pattern

Before creating any artifact, first discuss the task in text. Then explicitly state:

- which methodologies will be used;
- why each methodology applies;
- where each methodology will appear in the artifact;
- whether MECE is required;
- what sources or instructions are canonical;
- whether the Frappe knowledge base must be checked before writing;
- what open questions remain.

If the task includes segmentation, categorization, tables, Mermaid diagrams, issue trees, hypothesis trees, or hierarchical structures, explicitly say that MECE will be used.

## Workflow

1. Classify the artifact type and task intent.
2. Read `references/methodology-router.md` to select applicable methodologies.
3. Read `references/adjacent-skill-router.md` when the task overlaps with specialized Paper Planes skills.
4. Read `references/model-catalog.md` when the task needs a more precise model than the router table provides.
5. Read `references/output-contract.md` before returning a methodology preflight or artifact brief.
6. If the task involves a new or reusable artifact instruction, read `references/md-instruction-workflow.md`.
7. Check for local project files under `instructions/` when working in a project folder.
8. Discuss the task and methodology choice with the user before creating files or artifacts.
9. Create or update an MD instruction only after explicit user confirmation.
10. Read the canonical Frappe knowledge base when methodology detail is needed, sources conflict, or the user asks for verification.
11. If Frappe requires authentication and no authenticated session/tool is available, report the access limit, use the best available project/source material as provisional input, and mark the methodology detail as not live-verified.
12. If a referenced methodology page is missing from Frappe, report the gap, use the best available project/source material as provisional input, and mark the methodology detail as unverified.

## Operating Rules

- Use MECE as the default standard for all segmentation, categorization, table structures, Mermaid diagrams, issue trees, hypothesis trees, and hierarchy design.
- Use ABCD for commercial proposals, landing pages, selling websites, marketing kits, POS materials, and other sales-oriented communications.
- Use SCQA for management argumentation, storylines, analytical notes, presentation logic, hypotheses, and executive materials.
- Use RDB and JTBD for positioning, value propositions, benefits, key messages, product cards, and sales enablement.
- Use SOSTAC for strategic presentations and executive strategy narratives.
- Use PDCA/PDSA for process improvement, implementation cycles, quality, and continuous improvement.
- Use Problem Map, Ishikawa, Issue Tree, or Hypothesis Tree for diagnostics, interviews, contradictions, and root-cause work.
- Use Formula of Profit, KPI methodology, metric trees, and owners when the artifact involves economics, dashboards, growth levers, or management metrics.
- Use CJM, service blueprint, jobs map, experience map, and touchpoint inventory when the artifact involves customer path, service gaps, onboarding, support, retention, or handoff between channels.
- Use customer segmentation, RFM, cohort logic, ABC/XYZ, need-state segmentation, and ICP when the artifact involves audience groups, client base structure, product assortment, sales focus, or prioritization.
- Use unit economics, LTV, CAC, payback, contribution margin, pocket price waterfall, and price corridor logic when the artifact involves monetization, pricing, profitability, channels, or commercial terms.
- Use OKR, KPI tree, metric hierarchy, North Star Metric, leading/lagging indicators, and owner/control rhythm when the artifact involves management dashboards, operating reviews, or accountability.
- Use ICE, RICE, impact/effort, confidence scoring, experiment design, and hypothesis cards when the artifact involves growth, prioritization, product tests, marketing tests, or implementation backlog.
- Use TAM/SAM/SOM/PAM, market map, competitor matrix, 5 forces, PESTEL, and demand/supply fit when the artifact involves markets, external environment, competitors, or commercial opportunity.
- Use STP, brand ladder, value proposition canvas, messaging house, offer ladder, and benefit-proof-reason structure when the artifact involves positioning, communication, product packaging, or sales scripts.
- Use BCG, GE/McKinsey, Ansoff, portfolio map, product lifecycle, NPD funnel, and stage-gate logic when the artifact involves portfolio, product strategy, launches, or roadmap decisions.
- Use operating model, RACI/RAPID/DACI, SIPOC, value stream map, process map, control points, and governance cadence when the artifact involves roles, process design, implementation, or organizational change.
- Use risk matrix, dependency map, assumptions log, decision log, and issue/risk/action/owner registers when the artifact involves project management, implementation risk, or client governance.
- Use Pyramid Principle, storyline-storyboard, action titles, evidence ledger, claim ledger, and source gap log when the artifact must become a presentation, slidument, report, or executive memo.

## Source Policy

Use local project instructions for project-specific constraints. Use this skill for global methodology routing. Use the Frappe knowledge base for canonical methodology detail.

If sources conflict, apply this hierarchy:

1. Latest direct user instruction.
2. Global Paper Planes methodology rules from this skill.
3. Local project instruction in `instructions/`.
4. Canonical Frappe Wiki methodology pages.
5. Client materials and approved project artifacts.
6. External best practices.
7. Agent assumptions.

Stop and ask the user when a conflict affects meaning, methodology, client promise, structure, or acceptance criteria.

Do not use Notion as the default methodology source. Use Notion only when the user explicitly points to a Notion page, when a project still has a confirmed Notion-only source, or when Frappe has a documented gap. In those cases, mark the Notion material as a source or fallback, not as the global canon.

## Output Contract

For methodology preflight, return:

- task classification;
- selected methodology stack;
- methodology placement in the artifact;
- MECE decision;
- canonical sources and live-verification status;
- adjacent specialized skills to use or avoid;
- open questions or assumptions;
- next action.

For artifact creation, this skill prepares methodology and routing. The final artifact itself should be produced by the relevant production skill when one exists.

## Writeback Rules

- Do not publish, overwrite, move, or delete project artifacts by default.
- Do not create or update reusable MD instructions without explicit user confirmation.
- Do not treat external best practices, ChatGPT/Perplexity output, memory, or Notion as canonical methodology when Frappe can be checked.
- If Frappe cannot be checked, label the methodology detail as not live-verified.

## References

- `references/methodology-router.md` - methodology routing table and Frappe knowledge-base source links.
- `references/model-catalog.md` - expanded model catalog with triggers and artifact usage.
- `references/adjacent-skill-router.md` - rules for combining this router with specialized Paper Planes skills.
- `references/output-contract.md` - response structure, quality gates, and dry-run checklist.
- `references/md-instruction-workflow.md` - rules for creating project MD instructions.
- `references/eval-cases.md` - regression cases for testing trigger, routing, source, and writeback behavior.
- `references/fake-task-run.md` - fake task dry run results for install-readiness checks.
