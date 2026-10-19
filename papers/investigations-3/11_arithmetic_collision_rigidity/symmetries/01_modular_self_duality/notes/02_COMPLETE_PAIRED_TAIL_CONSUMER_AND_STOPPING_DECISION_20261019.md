# S01-T1: complete paired-tail consumer and bounded stopping decision

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, verified from the root session metadata. Derivation, implementation and delegated same-model review are internal LLM work; no specialist human review.

**Outcome.** The paired omitted-mode bound is now exposed through a reusable, domain-checked interface and consumed by the unchanged complete physical signed test on B. Fresh 192/256-bit runs confirm the inherited complete-error decrease, but all 40 final signed intervals, the minimum paid signed margin, and all 116 adaptive calls are unchanged within each precision. **S01-T1 is complete as an implementation integration and regression validation. Its primary additional-margin objective is not achieved.** Retain the interface and stop optimizing this omitted tail on B. This is a measured limitation of this fixed evaluator and pilot, not an obstruction to modular methods or an assertion that the exact analytic error has no benefit.

## 1. Scope and frozen comparison

The [comparison contract](../../notes/01_S01_COMPLETE_CONSUMER_COMPARISON_CONTRACT_20261019.md) selects the primary metric before execution. We interpret the user's first track as the first numbered program, S01; this does not launch the overview's separate S03 arithmetic residual branch.

The actual consumer tests

\[
 M=\frac{\mathcal L_0-E/100}{G_c^2}
  =V_1^2-V_0V_2-\frac{V_0^2+V_1^2}{100}>0,
 \quad V=(H,H_x,H_{xx})/G_c,
\]

on the entire closed B=[1/100,1/5] x [999,1001]. Here Gc=1000^(7/4) exp(-125 pi) is a fixed positive scale, never differentiated. The code calls the original `signed_cell` and `run_signed_consumer`; it does not regroup the acceptance expression to obtain a different interval result.

Keep the original d=pi/8-4 log(1000)/1000, modes 1–11, U=2, midpoint (21/200,1000), degrees (24,12), midpoint jets 0–50, order-52 majorant, source tail, all quadrature radii and all Taylor payments. Each precision uses one fresh setup shared by the old and paired runs. Both pay the same acquisition. The complete consumer is real-only. The paired theorem's complex-neighborhood scope is retained but no new complex wall is evaluated; in particular its t>=1/100 damping must not be applied to the older wall's t=0 boundary.

The [opening paired-endpoint theorem](01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md) is inherited, not re-proved here. It combines the signed source-zero endpoints before absolute estimation, with no dropped vertical segment for a non-even source. The exact same shifted retained polynomial is used on both sides of this integration comparison.

## 2. Reusable interface and complete payment

The new [integration checker](../numerics/integrate_paired_tail_consumer.py) exports `install_paired_tail(ev, paired)`. It checks the fixed B rectangle/midpoint, precision, source cutoff, integer modes, contour, normalization and polynomial degrees. It invokes the opening theorem's admissibility and infinite-series checks, and replaces only `ev.uniform_tails[0]`, the order-0–2 omitted-mode vector. It returns the previous vector for restoration. The source tail, midpoint data/radii, finite-integral majorant, high-order tails and full-H moment remain identical; their exact dyadics are fingerprinted before and after integration. High-order derivative-tail estimates are not replaced by an order-2 allowance.

For each whole-cell added component error the unchanged evaluator pays

\[
 \epsilon_j=\epsilon_{j,\mathrm{quad}}+
 \epsilon_{j,\mathrm{Taylor}}+\epsilon_{j,\mathrm{source}}+
 \epsilon_{j,\mathrm{mode}}.
\]

The shared polynomial image already includes its outward arithmetic rounding. It is retained, then enlarged by this complete added error. No improved endpoint is differentiated by itself. All cutoffs and the analytic representation remain fixed through physical differentiation.

The fresh [record](../numerics/S01_COMPLETE_CONSUMER_20261019.json) includes separate whole-box error components at both precisions, all final cell margins, admissibility constants, the infinite n>=24 payment, common-data fingerprint, source pins, setup work and consumer counts. The following are conservative upward roundings of the 192-bit complete errors in fixed Gc units:

| Physical derivative | Original complete added error | Paired complete added error | Paired/original, rounded upward |
| --- | ---: | ---: | ---: |
| H | 4.620515e-12 | 3.934535e-12 | 0.851536 |
| Hx | 3.469201e-12 | 3.218759e-12 | 0.927810 |
| Hxx | 3.055846e-12 | 2.964413e-12 | 0.970080 |

The common whole-box Taylor allowance is about 2.164837e-12; quadrature contributes about 6.44e-13 to 6.74e-13; retained-source tails are below 1.2e-435. Thus further omitted-mode tuning cannot remove the unchanged Taylor and quadrature floors. The reductions in this table repeat the opening milestone, now checked in its actual signed consumer.

## 3. Actual physical effect

| Precision | Final accepted closed cells, each method | Calls including failed initial geometry, each method | Certified minimum M, each method | Identical final signed intervals |
| --- | ---: | ---: | ---: | ---: |
| 192 bits | 40 | 116 | >8.26087722768e-5 | 40/40 |
| 256 bits | 40 | 116 | >8.26087722864e-5 | 40/40 |

At each precision the old and paired minimum interval strings are identical; every final three-component jet enclosure is also identical. The higher-precision setup changes the reported minimum slightly, but that change occurs on both sides and is not credited to pairing. The weakest final cell is t in [1/100,23/400], x in [8007/8,1001]. The original whole-time geometry reaches its depth limit; the original four equal time slabs repair it. Both methods make 40 initial calls and 76 repair calls; each has 36 repair split choices. Closed seams and exact rational coverage are checked by the original consumer, and the entire adaptive geometry is compared for equality.

The existing interval image widths are many orders above the approximately 1e-13 tail savings. The equality of the actual returned intervals, rather than this heuristic alone, establishes the reported absence of a resolved paid-margin gain. It does not show that the exact underlying analytic allowance cannot improve a differently designed or more accurate consumer. We do not introduce another margin functional to manufacture a success after the declared test is decisive.

No matched-cost experiment is selected. Setup times and counts are recorded for audit only. The unchanged 116 calls provide no work-count advantage; no speed ratio is claimed. There is no new covered cell, real bridge improvement, complex exterior theorem or Newman bound.

## 4. Stronger comparison references

The [existing real-source comparator](../../../numerics/high_height_consumer/REAL_COMPARISON.json), discussed in [Note 12](../../../notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md), has largest complete component error below 2.165e-12 Gc using 768-bit real-source quadrature and the same physical domain, degrees, source cutoff and signed target. Its midpoint coefficients come from a different finite-integral representation; it is not the exact same shifted retained polynomial. It remains stronger in physical added-error accuracy than this paired shifted representation. It is not rerun here and no superiority over it is claimed.

The transport Notes 20–22 frozen-exponential/correlated correction and the S03 complete source-informed direct radius >1.336516 also remain separate applicable reference representations. No mixed-normalization ranking is made. Their matched correction comparison is S02-T1, not a hidden part of S01. The contract gives the full Q/phase/physical conversion matrices, including normalizer derivatives. The earlier analytic-only/source-informed S03 allowances are unchanged.

## 5. Controls and separate internal review

The portable [control checker](../numerics/check_paired_consumer_controls.py) freshly executes the repository's source-specific event certifiers into an external work directory. It then returns those source-specific jet balls through a stub to the **unchanged** physical `signed_cell`. All five surrounding event boxes fail strict acceptance, and the Euler p=41 negative-Laguerre witness has a strictly negative excess near -5.300001e-6 in its native scale. Decimal display balls are conservatively re-enclosed; no exact-dyadic transfer is claimed. No theta tail allowance is inserted into a control.

The [control record](../numerics/S01_CONSUMER_CONTROLS_20261019.json) also rejects zero/edge contour shifts, a stationary omitted mode, excessive spectral height and excessive imaginary width. The non-even analytic fixture verifies the full vertical-segment identity through derivative orders 0–2 and rejects omission at all three orders. The integration interface separately rejects a changed spatial domain.

Analytic premise screens remain necessary: finite-prime and finite weighted-square families lack complete normalized reflection; reflected super-Gaussian and smooth positive-primitive families lack the exact normalized theta integer-square expansion; Euler-factor controls lack unchanged level-one coefficient/source data. Heat-polynomial/counter-kernel events share generic heat/rotation identities without the theta source and justified theta tail constants. Finite-prime and smooth-primitive existence constructions do not supply effective event boxes for this replay. The smooth-density/two-channel controls lack the claimed quantitative coupling to the signed physical observable; no such new coupling is proposed here. These facts do not require a control to fail a valid local test on every collision-free box.

[Review 02](../reviews/02_COMPLETE_CONSUMER_INTEGRATION_INTERNAL_REVIEW_20261019.md) records a separate internal reader and decisive replay. VAL-01 and VAL-02 close on this bounded continuation instance; later changed estimates must reopen or append validation. The result is an interval-checked implementation integration and regression validation, with the primary additional-margin objective unachieved. It is neither a new analytic theorem nor a universal no-go theorem.

## 6. Decision and next action

Keep the paired-tail interface for compatible fixed-domain consumers. **Stop further S01 omitted-tail tuning on B under this comparison contract.** S01's retained signed-core estimate remains open. No extension gate is activated by the unchanged margin. S02-T1 can now begin by declaring its matched disk comparison against the strongest frozen-exponential/correlated correction; S03-T1 retains its independent analytic residual contract. Neither task has been executed by this result.

This continuation follows the [result-summary index](../../../../../../result-summaries/README.md) and [avoid index](../../../../../../avoid/README.md), especially [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), [target reformulations](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [preserving cancellation](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The global real bridge 1001<|x|<exp(2000) on the stated time slab and global complex exterior remain open.
