# Output Contract

Use this contract for the first response and for dry-run checks.

## Methodology Preflight Template

```text
Task classification:
- Artifact type:
- Task intent:
- Client/project context:

Methodology stack:
- [Model]: why it applies; where it appears in the artifact; Frappe status.

MECE:
- Required: yes/no.
- Where:

Canonical sources:
- Latest user instruction:
- Local project instructions:
- Frappe knowledge base:
- Client/project artifacts:
- Fallbacks:

Adjacent skills:
- Use:
- Avoid:

Open questions / assumptions:
- ...

Next action:
- ...
```

## Quality Gates

- The selected models match the actual artifact, not just keywords in the prompt.
- MECE is explicitly stated for segmentation, tables, Mermaid, trees, hierarchies, dashboards, and templates.
- Frappe verification status is explicit: live-verified, authentication-required, missing page, or not required for this step.
- Notion, memory, and external sources are never labeled as global canon.
- Adjacent specialized skills are named when production work is requested.
- Writeback rules are clear before creating reusable MD instructions or touching project files.

## Dry-Run Checklist

Before calling the skill ready:

1. `SKILL.md` can be read from start to finish.
2. All referenced files exist.
3. Router covers presentations, commercial proposals, dashboards, research, diagrams, process work, economics, and reusable instructions.
4. Source hierarchy points to Frappe as canon.
5. Authentication-required Frappe access is handled as an access state, not a source gap.
6. Eval cases include good trigger, bad trigger, ambiguous trigger, writeback risk, Frappe access, and adjacent-skill collision.
