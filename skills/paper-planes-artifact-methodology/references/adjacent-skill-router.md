# Adjacent Skill Router

This skill chooses methodology and source policy. It should hand execution to specialized Paper Planes skills when the user asks for a concrete production artifact.

## Prefer Specialized Skill For Production

| User intent | Prefer | Role of this skill |
|---|---|---|
| Dense presentation, slidument, HTML presentation, one-pager | `pp-slidument`, `consulting-slides-creator`, Presentation Kit rules | Select methodology stack, source hierarchy, MECE rules, and evidence gates |
| Commercial proposal or paid offer | `commercial-proposal-generator`, `bpv-04-mpp-commercial-proposal` | Select ABCD/RDB/JTBD/economics stack and Frappe checks |
| Client case | `pp-case-writer`, `case-narrative` | Select evidence ledger, SCQA, before/after logic, claim boundaries |
| Expert article or longread | `expert-article-writer`, `pp-longread-leverage`, `balakhnin-voice` | Select argument structure, source policy, methodology grounding |
| Customer or market research | `deepresearch`, `competitor-research`, `client-info`, `demand-supply-match-intelligence` | Select research model, source confidence, segmentation and comparison logic |
| Interview guide or interview synthesis | `interview-brief-by-analogs`, `pp-interview-slides`, `BPM1` | Select JTBD/CJM/issue-tree/segmentation logic |
| Dashboard, metrics, or financial model | `bpm4-datalens-dashboard`, domain BPM4 skills, spreadsheets skills | Select Formula of Profit, KPI tree, owner cadence, source hierarchy |
| Process, roles, implementation, governance | `rail`, `admin`, `cord-pdca`, relevant BPM/BPV skill | Select PDCA/SIPOC/RACI/risk/governance logic |
| Skill quality or regression test | `skill-eval-harness` | Provide target behavior and methodology-specific eval cases |

## Collision Rules

- If the user asks "which methodology", stay in this skill.
- If the user asks to create the final artifact, use this skill for preflight and then use the specialized production skill.
- If the user names a specialized skill directly, read that skill and use this skill only for methodology routing.
- If the task is a Paper Planes client project in production, project gates and local instructions override generic artifact preferences.
- If two specialized skills overlap, choose the one that owns the final artifact format, then add the other only for a narrow function.

## Avoid

- Do not let this skill replace production skills.
- Do not turn every artifact into a new reusable instruction.
- Do not silently write to Drive, Frappe, ClickUp, GitHub, Notion, or project folders unless the user request and the selected skill allow it.
