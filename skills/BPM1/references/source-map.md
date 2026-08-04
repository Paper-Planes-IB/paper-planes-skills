# Source Map

Use this reference when external benchmarks are needed for a BPM-1 prior. Source availability and legal/access status can change; verify important sources before relying on them in client-facing work.

## Evidence Grades

- `direct`: same or very close behavior/category/audience/geography; can inform ranges.
- `adjacent`: related behavior or audience; use with adaptation and caveats.
- `weak_proxy`: only a loose signal; never use as a direct percentage.
- `context`: macro/cultural/category context only.
- `not_useful`: closed, legally risky, unavailable, or irrelevant for the decision.

## Russia

| Source | Default grade | Use |
|---|---|---|
| HSE household / consumer behavior studies, RLMS-HSE | `direct` or `adjacent` | Household behavior, consumption, socio-demographic transfer, long-term patterns. |
| Rosstat household budgets, consumer expectations, EMISS/fedstat | `adjacent` or `context` | Macro calibration, income/region/consumption structure, confidence and spending context. |
| FOM | `adjacent` | Social attitudes and everyday practices; often aggregated. |
| VCIOM Navigator / datasets | `adjacent` or `weak_proxy` | Public opinion and some social behavior; check whether topic is consumer-relevant and whether microdata exists. |
| NAFI | `adjacent` | Finance, digital behavior, consumer literacy, lifestyle reports; often aggregated. |
| RANEPA monitoring | `adjacent` or `context` | Social-economic monitoring and household context. |
| openICPSR / Zenodo Russian datasets | `adjacent` or `weak_proxy` | Use only after topic/data dictionary check. |
| Romir, Mediascope, Ipsos/GfK/Comcon public reports | `context` or `not_useful` | Useful public snippets, but full panels are often closed or paid. |

## Kazakhstan / CIS

| Source | Default grade | Use |
|---|---|---|
| Bureau of National Statistics RK | `direct` or `context` | Household spending, living standards, regional context. |
| National Bank of Kazakhstan inflation expectations | `direct` or `context` | Monthly confidence/inflation expectations, spending mood. |
| Freedom Finance Global / Kursiv consumer confidence | `direct` or `adjacent` | Consumer confidence and regional mood, when source-check confirms method. |
| World Values Survey | `adjacent` | Cultural/value calibration, not direct category behavior. |
| Gallup Findex / World Poll public datasets | `adjacent` | Financial behavior and broad attitudes. |
| CIS-STAT, Central Asia Barometer, World Bank Listening to Central Asia | `adjacent` or `context` | Regional/cultural transfer; avoid absolute percent transfer. |

## Transfer Rules

- Transfer relative patterns more readily than absolute percentages.
- Penalize cross-country, old, political, or unrelated-category sources.
- Mark legal/access risk explicitly.
- Do not use political/social mood surveys as consumer behavior facts.
- If direct category data is absent, say `NO DATA` and design an exploratory field question.
