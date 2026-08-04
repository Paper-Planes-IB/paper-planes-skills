# Related Skills

The handoff archive contains three installable skill folders.

| Skill | Role | Use it when | Boundary |
|---|---|---|---|
| `bpm10-crm` | Core CRM analysis and design | Audit, target architecture, entities, funnels, cards, functional requirements, governance, system map, QA | Owns business architecture, not production implementation |
| `bpv2-accounting` | Re-Engage and current-client development | Scoring, ADP, progress, hypotheses, KAM process, regular work | Owns account-development methodology; BPM10 projects it into CRM |
| `bitrix24-php-automation` | Bitrix24 technical automation | PHP Bizproc, local modules, field sync, REST/webhook diagnostics | Use only after BPM10 decisions are approved |

## Other Existing Vault Modules

These are related references but not packaged as separate native skills because the core package already contains the necessary boundary logic:

- BPM11 target data model: enterprise objects, events, semantics, systems of record, data ownership;
- BPM4 database/profit analysis: commercial signals, segments, thresholds, deviations;
- BPM8 process analysis: end-to-end work, decisions, roles, inputs, outputs;
- Business Analysis: generic strategy/process/CRM analysis;
- B2B expert-sales prompt library: Lean CRM, manager decision packet, weekly review, full-cycle QA.

The BPM10 Miro module is packaged as `references/miro-integration.md`. It is part of the BPM10 output workflow, not a separate BPM10 skill.

Install a related skill only if its trigger is expected. Avoid loading all skills into one task by default.
