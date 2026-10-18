# Overview 02: summary of the entire research round

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model: **GPT-6.1 Sol (`gpt-6.1-sol`)**;
the initial bounded execution recorded **max**, and the subsequent analytic
and finite-wall continuations recorded **ultra**. Reviews are internal
same-model work; no independent specialist review is claimed.

This is the requested summary of the **entire overview 02 round**, from
manuscript pinning and Notes 07–10 through Notes 11–14. It supplements the
[final research note][final], which contains the latest derivations, and
the continuing [progress tracker][progress]. It does not replace either.
The [result-summary index][summaries] and [patterns-to-avoid index][avoid]
govern the status language, especially [finite versus global scope][scope],
[collision controls][controls] and [numerics following the question][numerics].

**Outcome:** the round produced a complete finite evaluator, certified
finite signed and wall consumers, stronger effective approximation
estimates, and a smaller explicit outer exclusion threshold. The bounded
continuation and its auxiliary replay are complete. **The overall research
plan is not complete: Stage 4's global bridge remains open, and no new
Newman bound is established.**

## What the round established

| Work | Result and evidence |
| --- | --- |
| Manuscript baseline, Stage 0 | The strengthened eight-file source set was pinned and its scalar contracts replayed; compilation passed. The original manuscript pin remains unchanged. [Review 06][review06]. |
| Complete evaluator, Stage 1 | Shifted complete reflection is retained before truncation. Mode tail, retained-integral cutoff, quadrature, rounding and whole-cell propagation are paid. Real and complex diagnostics passed on the declared finite domains. [Note 07][note07]. |
| Matched comparison and adversaries, Stage 2 | The baseline and adjoining tests were replayed. Applicable control-event boxes reject strict exclusion, and the Euler-factor witness is separately classified. Both timing rounds failed the required factor-two advantage. The latest complete comparison was approximately 7.590 s shifted versus 11.236 s real, a ratio of 1.480. No computational superiority or larger scan is justified. [Notes 08][note08] and [12][note12]. |
| Finite signed inequalities, Stage 3 | The strict inequality L0=(Hx)^2-H Hxx > (H^2+(Hx)^2)/100 is interval-certified on [1/100,1/5] × [25,45] (314 strips) and [1/100,1/5] × [999,1001] (40 cells). These are compact results, not a uniform global sign law. [Notes 09][note09] and [12][note12]. |
| Effective arithmetic tail | Integration by parts in omitted nonstationary square modes gains log(x)/x over the earlier absolute tail along the logarithmic contour rule. Explicit constants give errors below 2e-9 G0 for the first three derivatives at every x>=1000 on the stated time/complex strip. Bounded point tests at 1000 and 10000 paid all errors and measured retained-integral cost. [Note 11][note11]. |
| Finite wall and propagation | Seven closed cells certify the full wall at Re z=1000, 0<=t<=1/5, |Im z|<=1. Published initial verification, strip preservation and local Hermite splitting then imply E=H^2+(Hx)^2>0 for 0<t<=1/5, |x|<=1000. Union with the signed box closes [1/100,1/5] × [-1001,1001]. Initial simplicity and a zero-velocity estimate are unnecessary. [Note 13][note13]. |
| Final analytic continuation | The explicit eventual first-jet exclusion is sharpened from exp(64/epsilon) to exp(20/epsilon), uniformly for epsilon<=t<=1/2. A constant-distance contour d=pi/8-A/x supplies a new explicit O(x^(-1/4)) omitted-mode bound without the logarithmic contour retreat. A remote polynomial heat control isolates the limitation of the finite-wall premises. [Final research note][final] and [Review 12][review12]. |
| Replay and claim control, Stage 5 | The finite consumers passed fresh 256-bit shifted and independent real-source replay, exact closed coverage checks, hash/parameter checks and adversarial injections. The final analytic constants and remote control have separate outward/exact replay records. These checks close the auxiliary claims and do not supply missing global coverage. [Reviews 09][review09], [11][review11] and [12][review12]. |

## What remains

At tau=1/100 the current coverage is:

| Region, for 1/100<=t<=1/5 | Status |
| --- | --- |
| abs(x)<=1001 | Closed by finite propagation plus the signed overlap. |
| 1001<abs(x)<exp(2000) | **Open finite bridge.** |
| abs(x)>=exp(2000) | Covered by the final research note's proved eventual exclusion. |

The smaller outer constant is an earned analytic improvement, but the
remaining bridge is still enormous. At its outer endpoint, the explicit
b*=1/8 finite-mode rule requires more than 10^433 retained modes for one
height. This is a resource statement about that enumeration scheme, not
an impossibility theorem for faster representations or other modular
methods. Better omitted-mode accuracy alone does not establish a lower
bound for the physical field or its first jet.

The next substantive research step must provide a cancellation-sensitive
estimate or a genuinely feasible complete outer/bridge consumer. A canopy
alternative still needs all its actual initial-verification, exterior,
barrier, parameter and endpoint hypotheses. After a route closes, its full
package needs global replay and final manuscript/claim integration. The
new Notes 11–14 remain outside the pinned manuscript source set.

**Completion notice:** the recorded research round and its bounded final
continuation are complete at this documented stopping point. The global
research objective remains unfinished.

[final]: ../notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md
[progress]: 02_UPDATED_RESEARCH_PLAN_PROGRESS_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[numerics]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[note07]: ../notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
[note08]: ../notes/02_updated_research_plan/08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md
[note09]: ../notes/02_updated_research_plan/09_COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.md
[note11]: ../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md
[note12]: ../notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md
[note13]: ../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md
[review06]: ../reviews/06_SOL_STRENGTHENED_MANUSCRIPT_CONTRACT_REVIEW_20261018.md
[review09]: ../reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md
[review11]: ../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md
[review12]: ../reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md
