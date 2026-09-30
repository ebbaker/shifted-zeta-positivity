# Internal critical review of the consolidated Sonin notes

29 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and reasoning effort are not exposed. This is a separate same-model internal review, not independent human refereeing.

Reviewed the [canonical comparison audit](../notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md) and [place-addition/error-control analysis](../notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md), concentrating on the new formulas and scope claims. A second same-model reader checked the source convention, strong trace proof, source family, scalar tail program, and total error budget. The lead agent integrated the findings.

**Conclusion:** No substantive mathematical error found in the reviewed additions. No computed actual-Sonin sign or trace is being certified by this review.

1. **Galerkin residual, (A16).** With `R_N=(I−A Q_N A_N^{-1}Q_N*)W`, expanding its squared Hilbert–Schmidt norm gives exactly the displayed scalar and three finite matrices. In particular `J_N=Q_N* H A Q_N` has the correct order; cyclicity yields the real cross term `−2 Re tr(A_N^{-1}J_N)`. The quadratic term is correctly `tr(A_N^{-1}K_N A_N^{-1}H_N)`. No unseen tail has been deleted: it remains in `h_0` and the full-integral entries.

2. **Calibration for `h_0`.** The kernel `D_S F` is correct, since `C_F D_S=C_{D_S F}` for the specified translations. Its shifted support causes no obstacle to the compact-smooth trace identity. This step does not invoke the short-support dominance theorem. The auxiliary kernel need not satisfy the original moment constraints, because the calibration itself does not require them.

3. **Signed covariance and residual laws.** Equations (A4)–(A6) are valid: the signed spectral measure is dominated by the positive one through `−W≤H_F≤W`, and the integral sign matches (A3). The complete residual at fixed support changes only by minus the positive-pairing increment. The additional arithmetic prime term belongs only to the partial residual (A10). Both bookkeeping conventions are distinguished correctly. The compressed double-commutator identity (A8) has the correct sign and factor.

4. **Small-cutoff obstruction.** The dilation/geometric expansion (A20), Hilbert–Schmidt scalar products (A21), and off-diagonal summability prove the stated contradiction. Each fixed `Y_N` is trace class, so pairing it with the operator-norm limit is legitimate. The proof establishes non-Hilbert–Schmidt regularity of that exact unsmoothed cutoff, without contradicting the smoothed trace results.

5. **Numerical gate and remaining obligation.** The notes accurately say that no certified actual-Sonin trial matrix, full residual norm, or return moment has been computed. The scalar Chebyshev improvement is an error-budget component, not an arithmetic sign result. The proposed finite-matrix reduction is concrete, but its matrix entries and infinite spatial tails still need enclosures. The stated approximants converge to `B_S`, with no unsupported claim that they converge to `Q`.

The calibration sign, normalization, pole separation, compact-smooth trace proof, and all-support restricted criterion also remain consistent with the earlier audit. The explicit smooth cutoff extension of the Hankel kernel correctly supplies the trace-class argument used there.

## Evidence classification and decision

| Claim | Evidence and limit |
|---|---|
| Correct comparison on the smooth core | Primary-source normalization checks plus explicit internal derivation; not a new positivity theorem |
| Pole-neutral RH criterion | Published restricted criterion with an explicit coordinate map and all-support quantifiers |
| Signed place-addition law | Exact operator and spectral-measure identities; the sign-bearing covariance remains uncontrolled |
| Chebyshev tail improvement | Analytic norm bound plus standard-library exact rational certification of the scalar majorants |
| One-sided trace approximation | Exact Galerkin identity and fixed-test convergence; no numerical residual enclosure yet |
| First-prime residual sign on new sources | Not computed or established |
| Arbitrary-support positivity | Not established; finite-place condition numbers and positive traces do not supply it |

The scalar program was run and checked against the resolvent expansion.
At relative targets `10^-6`, `10^-8`, and `10^-10`, the certified sufficient
degrees are 50, 63, 76 for Chebyshev, versus 293, 372, 450 for Neumann.
These are degrees of analytic majorants, not observed errors of actual
Sonin traces. The generated record identifies the exact program by hash.

Two error-budget clarifications were incorporated: quadrature of the final
error-kernel integral needs its own enclosure, and nonneutral numerical
source replacements need their pole contribution or a source-error bound.
The exact two-source family is neutral analytically.

**Decision.** The evidence supports an exact signed place-addition relation
and a concrete approximation lemma. It does not yet support a one-sided
bound for the arithmetic residual. The next single task is to enclose the
full actual-Sonin Hilbert–Schmidt residual through (A16), including spatial
tails, for the sources in (A17). The [continuation handoff](../notes/SONIN_CONTINUATION_AFTER_TRACE_AUDIT_20260929.md)
preserves that limited target. If successful it enables a diagnostic;
the Sonin-specific signed covariance estimate remains the all-support
research obligation.
