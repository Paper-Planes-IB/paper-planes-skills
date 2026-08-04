# Source Inventory

## Coverage

- Coverage level: Directional.
- Sources checked: portable HTML dashboard for Dинастия-С, project registry and project card, reusable dentistry case draft, archived medical-methodology batch, existing BPM-4 healthcare clinic economics skill.
- Missing high-value lanes: live MIS/CRM or warehouse connector, treatment plan table, appointment status history, chair or cabinet id, appointment duration, doctor schedule, margin/cost data, marketing spend by source, stable cross-system id contract.
- Rejected or lower-confidence candidates: broad Vault search results not opened; raw patient rows with personal data; FIO-based attendance comparisons as financial proof.

## Sources

| Source | Type | Locator | Connector Or Tool | Permission Status | Last Checked | Supports | Gaps Or Caveats | Automation Eligible | Update Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dинастия-С portable dashboard v0.9 | HTML dashboard / embedded datasets | `/var/folders/y7/z20t7xkd2w7_cy1_ksrzxwxh0000gn/T/СКИБ_Дашборд_анализа_базы_v0_9_portable.html` | Local file read | User supplied in current thread | 2026-06-11 | Monthly, branch, department, patient type, RFM, source, doctor, appointment, Markov transition, service-line, attendance-comparison aggregates | Temporary local path; source extract may expire; includes personal patient fields, so only aggregate semantics should be persisted | No | Manual refresh from updated dashboard export |
| Dинастия С project registry | Vault registry | `Vault/__Проекты.md` | Local workspace files | Available | 2026-06-11 | Project identity, aliases, industry, РГ2 status, active project context | Project status may change; verify before project-management claims | Yes | Draft update proposal only |
| Dинастия С project card | Project card | `Vault/10-отделы/04-производство/Проекты/Династия С/00-Карточка проекта.md` | Local workspace files | Available | 2026-06-11 | Scope, BPM status, data-quality risks, deliverables, dashboard reconcile context | Operational BPM progress requires team confirmation | Yes | Draft update proposal only |
| Dинастия / НИЦ / НоваДент dentistry case draft | Product-vitrine case draft | `Vault/10-отделы/02-продажи-маркетинг/04 — Коммерческие функции/04.4 — Витрина продуктов агентства/2026-04-29-Династия-НИЦ-и-НоваДент-почему-стоматологии-теряют-деньги-не-в-маркетинге-а-между-консультацией-и-лечением.md` | Local workspace files | Available | 2026-06-11 | Reusable dentistry logic: revenue lost between consultation, treatment plan, repeat appointment, and specialist handoff | Case draft is interpretive, not a numeric source | Yes | Draft update proposal only |
| Post-archive medical methodology batch | Methodology batch | `Vault/10-отделы/05-качество-БП/АТС-рефлексия/Линии/Post-archive tunnel — batch Сантерра Сайвер СадкоПарк Рыбинсккомплекс РусАгроПром Румяный Каравай Роял Медик Ростовский девелопер Роллинг-Мото 10-05-2026.md` | Local workspace files | Available | 2026-06-11 | Medical LTV / PJM / CRM / retention operating-system patterns and anti-patterns | Generalized reusable donor, not client-specific data | Yes | Draft update proposal only |
| BPM-4 healthcare clinic economics skill | Local skill | `/Users/iliabalahnin/.codex/skills/bpm4-healthcare-clinic-economics/SKILL.md` | Local skill file | Available | 2026-06-11 | Medical Formula Profit, SI classes, graph classes, output caveats, source requirements | Domain guidance, not a source of current client facts | Yes | Manual skill maintenance only |

