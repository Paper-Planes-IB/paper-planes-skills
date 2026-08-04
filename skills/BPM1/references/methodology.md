# Methodology

Use this reference when the task requires an explicit prior, evidence weighting, confidence, or post-field comparison.

## Prior Construction

Prefer transparent ranges over complex math unless the user asks for a quantitative model.

Minimum prior record:

```yaml
prior_parameter:
  metric: ""
  expected_range: ""
  central_estimate: ""
  evidence:
    - source: ""
      grade: "direct | adjacent | weak_proxy | context"
      sample_or_base: ""
      date: ""
      similarity: 0.0
  confidence: "HIGH | MEDIUM | LOW | NO DATA"
  field_need: "confirm | falsify | explore | not_needed"
  caveat: ""
```

## Similarity Weighting

Score each source on:

- category similarity;
- audience similarity;
- geography;
- time/recency;
- methodology;
- question wording similarity;
- sample/base size.

Default interpretation:

- `0.75-1.00`: strong analogue;
- `0.50-0.74`: usable adjacent analogue;
- `0.25-0.49`: weak proxy;
- `<0.25`: context only or exclude.

Apply recency decay more strongly in fast-changing categories such as tech, finance, platforms, employment markets, and events. Use slower decay for stable food/FMCG habits.

## Confidence

- `HIGH`: multiple direct/strong analogues, stable pattern, sufficient base. Still not field fact.
- `MEDIUM`: at least one direct source or several adjacent sources; field confirmation required.
- `LOW`: weak proxy, old source, cross-market transfer, small base, or unclear category match.
- `NO DATA`: no acceptable source; add exploratory field question.

Never write "fact" for a prior. Use "likely", "expected", "prior", "benchmark candidate", or "pre-field hypothesis".

## Stated vs Derived Importance

Stated importance:

- respondent says factor is important.
- useful for language and declared priorities.
- often inflated by social desirability and flat rating.

Derived importance:

- factor predicts choice, satisfaction, NPS, consideration, repeat use, or purchase behavior.
- requires suitable dependent variable and sample.

If derived importance cannot be calculated, say so. Do not imply behavior from stated importance.

## K-Means and JTBD

Use k-means only if:

- factor matrix labels are verified or safely reconstructed;
- enough respondents for stable clusters;
- missingness is manageable;
- scale direction is consistent;
- factor questions are not all flat-rated.

Translate clusters into JTBD using:

- high-ranking factors;
- scenarios/occasions;
- barriers;
- open answers;
- behavior/frequency;
- price/channel patterns.

Avoid naming clusters only by demographics. Demographics can describe a cluster but should not be its job logic.

## Prior vs Fact

After fieldwork, compare:

```markdown
| Parameter | Prior | Fact | Delta | Interpretation | Action |
|---|---:|---:|---:|---|---|
```

Classify differences:

- `confirmed`: fact inside prior interval;
- `strengthened`: fact exceeds expectation in strategically useful direction;
- `weakened`: fact lower than expected but still relevant;
- `surprise`: fact outside interval and changes decision;
- `no_read`: field result unreliable or base too small.

## Value of Information

Field questions are most valuable when:

- the answer can change a decision;
- uncertainty is high;
- external/internal prior is weak;
- the metric controls segmentation, offer, pricing, channel, or storyline evidence.

Questions are low-value when:

- answer is already stable across direct sources;
- metric is not decision-relevant;
- wording duplicates another stronger question;
- answer will not be usable in slides, JTBD, segmentation, or operational decision.
