# Notes 35–37: assessment and remaining joins

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6-astra (Codex), actual effort xhigh**, verified from session metadata. Chat 0012, thread 01a170f9-948a-7083-9c79-2eeccb5ab856.

**Scope:** separate-chat, cross-model LLM assessment of the Sol notes and selected code/evidence. No numerical rerun, interval certificate, full endpoint-proof audit, specialist review or HDA-20 completion.

## Assessment and evidence

Notes 35–37 make substantive quantitative progress: a failed finite-source method becomes a plausible candidate for certification, with fixed physical targets and retained failures. I found no blocking issue in the local analytic steps inspected. They do not supply an accepted finite core or a global approximation.

Read [AN01](../research-progress/handoffs/HDA-17-AN01.md), Notes [35](../notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md), [36](../notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md), [37](../notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md), Reviews 18–20, the current overview/register and Note 34's joining contract. Inspected the Hermite source, main diagnostic and directional covariance code. The three code hashes recorded in the main Hermite result match current files; the supplement's inherited r1 hash matches. Its recorded maximum is 0.6887484812283295 for Delta Q at y=0, allowance 0.005509987849826636 against total target 0.01. These are record-consistency checks, not accuracy verification.

Interpretation follows the [result index](../../../../result-summaries/README.md), [heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), and cautions on [target reformulations](../../../../avoid/01_restating_the_target.md), [evidence status](../../../../avoid/06_status_stronger_than_the_evidence.md) and [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## What the three notes establish

**Note 35 chooses a method.** Weak transfer helps selected rows but does not dominate the local method for covariance and signed source. Interpolation dominates the failed budget; more theta modes or a larger source cutoff do not address that error. The largest weak source ratio across the original three times is 1.97354e11. Failed sufficient allowances are not lower bounds on actual errors.

**Note 36 improves bounds and identifies a better representation.** Signed-polynomial curvature caps and convex secant weights retain continuous inequalities. The adaptive linear mesh improves order-zero interpolation by 24.37 times against the old uniform768 baseline. Delta Q still exceeds its source allocation by 2056.73 at the worse point. The signed radial source coefficient and derivative extrema check out. Curvature/time formulas retain their exact-heat premises and residual terms. Composite integration helps at a documented extra cost; refinement agreement remains diagnostic.

**Note 37 changes feasibility.** The complete-source fourth derivative, Hermite factor 1/24, integrated factor h^5/720, absolute slope cardinals and Bernstein positivity argument are consistent. The linear fallback correctly uses a second-order remainder. Exact nonnegative dyadic coefficients prove positivity of the chosen source, while its proximity to canonical nodal data remains a separate question. The ideal-Gauss proof bounds both the integral and rule remainders; rounded Gaussian data remain unpaid.

| Method at t=64,x=4,y=0 | Delta Q source allowance | Ratio to 0.008 source allocation |
| --- | ---: | ---: |
| Note 36 adaptive768 linear | 16.4538 | 2056.73 |
| Note 37 Hermite, original caps | 0.00884058 | 1.10507 |
| Same source, directional caps | 0.00550999 | 0.688748 |

The directional cap is legitimate: each direction uses the minimum of two bounds valid for both fields. Total errors freeze caps before categories are mapped. Filtered mean products are formed after full-support integration. The approximately 1963-fold same-mesh interpolation gain uses doubled nodal data; the comparable-storage Hermite384 failure correctly prevents a cost-neutral claim.

## Remaining obstacles

1. **Certification at one point:** enclose nodal values/slopes, source-cap/chord arithmetic, finite-field evaluation and continuous filter integration. Both observable and positive error-envelope integrals need payment. Absolute values and minimum switches create curves not resolved by axis splits. The remaining 31% of source allocation is useful slack, not a guarantee.
2. **Continuous space/time coverage:** the improved result is only at t=64,x=4,y=0 or 1/2. At t=64 spatial regulator terms and curvature corrections vanish. Those observations do not validate the t>64 adaptive system, full rectangle or transition slab. Note 35's older t=96,128 failures have not been overturned by new computations there.
3. **Effective endpoint overlap:** the recorded endpoint/outer theorems have eventual constants/onsets. Their useful overlaps must be instantiated. Regulator definition times 64 and 128 are not certified theorem onsets.
4. **Paid time joins:** F=(1-theta)F1+theta F2 has residual containing theta'(F2-F1). Note 34 gives a valid compact bound, but needs field errors and component residuals, not just averaged observable errors. A wider overlap changes its constants and domain.
5. **Compatible spatial assembly:** an ordinary cutoff gives partial_bar_z F=(partial_bar_z lambda)(P_*-H_f), generally breaking holomorphy. Blending observables also has nonlinear covariance and differential compatibility costs. This structural question survives a successful finite-core certificate; corrected constructions and other joins are not excluded.

Note 25's outer-potential obstruction is scoped to its piecewise-linear, strictly positive-endpoint source and off-axis buffered strips. It must not be asserted as an already proved exclusion of every Hermite/tapered source. Conversely, Note 37 gives no all-height outer-potential theorem for its source with zero coefficients.

## Project position and continuation

There are endpoint/outer formulas with recorded in-note proofs, exact regulated identities, a compact transfer/time-join theorem and now a promising finite approximation. One compatible global construction with informative errors everywhere remains missing. HDA-17 stays Partial; HDA-18 stays Gated. The maintained manuscript is through Note 31; this assessment does not alter it.

The author's phase-transition suggestion is examined in [Note 38](../notes/38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md). Notes 27–28 already contain a regulator-induced high-height crossover; that can guide uniform approximation but does not by itself resolve spatial compatibility.

The [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) remain compatible with generic local identities and positivity. Changed-source controls lack the unchanged canonical theta data; atomic controls lack the smooth-density premise. No RH, simplicity, collision exclusion or regulator-removal inference follows.

**Next: Analysis and numerics — Sol.** Certify the frozen Note 37 worst observation before expanding numerical coverage. The separate analytical scoping in Note 38 can proceed without that certificate. Reserve Astra for a specifically resistant spatial-compatibility or uniform differentiated-layer estimate.
