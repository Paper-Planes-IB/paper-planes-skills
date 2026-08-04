---
name: medical-clinic-economics-semantic-layer
description: Use when answering Data Analytics questions for medical clinic and dentistry economics, including patient base analysis, RFM/LTV, visits, appointments, doctors, departments, branches, treatment journeys, capacity, source quality, and metric caveats.
---

# Medical Clinic Economics Semantic Layer

Use this skill to answer medical clinic, dentistry, and patient-base economics questions with the source-backed context in `references/semantic-layer.md`.

## Start Here

1. Read `references/semantic-layer.md`.
2. Use the listed canonical entities, metrics, grains, filters, caveats, and query patterns.
3. Treat this layer as source-selection and interpretation guidance, not as a substitute for live source reads.
4. Check freshness before answering time-sensitive questions.
5. When sources disagree or coverage is weak, say so and verify against the cited source.

## References

- `references/semantic-layer.md`: metrics, standard dimensions, query patterns, gotchas, and open questions.
- `references/source-inventory.md`: sources checked, coverage level, permissions, gaps, and update boundaries.
- `references/evidence.md`: detailed provenance for key reusable claims and current benchmark figures.

## Answering Rules

- Do not reduce clinic growth to new lead acquisition when repeat patients, LTV, plan execution, or cross-department journey evidence is available.
- Separate transactions, appointments, attendance, invoice/payment/realization, treatment plan, and schedule capacity grains before comparing metrics.
- Do not claim chair utilization as fact without chair or room id, appointment duration, doctor schedule, and status data.
- Do not rank doctors as good or bad from raw revenue, LTV, or show-up rates without case mix, specialty, role in journey, patient type, and downstream transfer context.
- Treat FIO-based matching as directional only; require stable patient ids for financial leakage claims.
- Preserve patient privacy: do not copy row-level patient examples, names, or other personal data into generated outputs unless the user explicitly asks and the output is safe.
