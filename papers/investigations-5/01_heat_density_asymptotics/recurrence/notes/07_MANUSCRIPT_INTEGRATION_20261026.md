# Analytical manuscript integration

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Recurrence chat0002, thread `01a176bf-7fd6-7fa2-ad1c-0fe1585f43c6`.

The author requested a systematic analytical manuscript of the current
results, followed by outstanding tasks, and an explicit account of what
the preceding investigation retains at the simplest and higher orders.
The current source is [main.tex](../manuscript/main.tex), titled *Finite
Fluctuation Hierarchies for the Negative-Time Riemann Heat Flow*.
This is a synthesis of the saved results, not a new execution request for
the provider audit. The [input manifest](07_MANUSCRIPT_INPUTS_20261026.json)
identifies the selected versions; the [internal assessment](../reviews/06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md)
and [build record](../manuscript/BUILD_RECORD_20261026.json) distinguish
analytical scope from document-production checks.

## Development and source correspondence

The development starts from the canonical cosine source and derives the
real-initial-value heat convolution. The common logarithmic gamma shape
then yields the weighted finite partition polynomials and their evolved
recurrence. The local remainder is integrated against Gaussian moments
before the growing window is bounded. Matching the full population error
to the real Riemann--Siegel remainder explains K=2p. True and artificial
tails are kept separate. Only after this fixed-order argument are the
factorial constants controlled simultaneously for growing order.

| Manuscript | Principal source and preserved scope |
| --- | --- |
| Sections 1.1 and 4.5 | Ansatz Notes 03--05, 10 and 12: earlier short and first-correction formulas, their domains, and different differentiation conventions. |
| Sections 2--4 and Appendices A--B | Recurrence Notes 02--04: finite recurrence, all-order coefficient envelope, fixed-p comparison, compact-time endpoint costs and all-mode bounds. |
| Section 5 and Appendix A.1 | Note05 and Review04: simultaneous order costs, unabsorbed/refined tails and the chosen outer rate on [1,2]. |
| Sections 6--7 | Note06, Review05 and R05-AN02: exact coefficient identities, complex bounds, quadrature, sensitivity, rounding, geometry and conditional precision. |
| Section 8 and Appendix C | Remaining provider, cost, joint-limit, reconstruction, physical-transfer and independent-validation obligations; classical-input scope. |

## What the approximations retain

The comparison table in Section 1.1 is the main guide. Every row keeps
both arithmetic arms and all n<=N; the integral rows also keep the exact
transfer between the moving natural cutoff and the fixed chart cutoff.
On the common slab 1<=T<=2, the proved natural-scale allowances are:

| Approximation | Arithmetic retained | Riemann--Siegel completion | Error allowance |
| --- | --- | --- | --- |
| Earlier short formula | Complete elementary arithmetic sum | Leading correction with its heat factor | O(X^-3/4) |
| Earlier target-dependent first correction | Exact gamma modes and their quadratic curvature correction | Bounded integral through C1 | O(X^-5/4) |
| Frozen p=1 | U0+U1, including the full quadratic Gaussian moment | Bounded integral through C2 | O(X^-7/4) |
| Frozen p=2 | U0+U1+U2, including cubic and curvature-square terms | Bounded integral through C4 | O(X^-11/4) |
| Frozen fixed p>=1 | Every partition of fluctuation weight at most p | Bounded integral through C_(2p) | O(X^-(p+3/4)) |

The frozen rows also hold on each declared fixed compact positive
T-interval with the displayed endpoint dependence. These are comparisons
of proved allowances, not pointwise monotonicity of actual errors.
Fluctuation weight is not ordinary polynomial degree. The earlier
target-dependent correction agrees with the frozen first arithmetic
correction at the chart center, but its differentiated formula and heat
residual differ; the manuscript derives the distinction explicitly.
No single-cosine replacement of the negative-time arithmetic population
is justified. The preceding ansatz investigation already had a separate
growing-degree outer approximation; the present manuscript does not
claim that outer accuracy first became available with this hierarchy.

## Status and continuation

The source results remain **proved in-note from named inputs**, with the
source notes' **same-model internal assessments**. This manuscript has
an additional **same-session authoring assessment**, not independent
specialist validation. Its evaluation theorem remains a **conditional
accuracy specification**. Concrete certified providers and descriptor
handling are the first unfulfilled evaluation task; broad R05 remains
Partial. R04/R06 and the ansatz/parent statuses are unchanged.

No numerical experiment supplies a proof step. No numerical or symbolic
research campaign was run for this integration. Compilation, reference
resolution and rendered-page inspection are production checks. Future
certified interval checks and measured costs may support the analysis.

Read the [result index](../../../../../result-summaries/README.md),
its [heat-flow cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
the [control screen](../../../../../result-summaries/12_collision_controls_and_screening.md),
the [avoid index](../../../../../avoid/README.md), and the
[separate-error pattern](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
This is an approximation/evaluation result, not an RH criterion or
collision-exclusion mechanism. Section 8 states the canonical premise
that each control lacks; exact heat evolution alone can survive those
controls and is not used to infer a zero-location conclusion.
