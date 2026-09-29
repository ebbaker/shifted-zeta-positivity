# Review of the CCM ground-selection continuation

Date: 28 September 2026.

Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured reasoning-effort level are not exposed to the lead reviewer. The main synthesis received separate analytic and numerical readings by parallel agents using the same model context. This is not independent human refereeing or formal verification.

## Disposition

The [main note](../notes/CCM_GROUND_SELECTION_TARGET_20260928.md) supports a change from an absolute residual target to a quantitative ground-selection target. Its new estimates and implications survived the mathematical checks below. It does **not** prove an overlap lower bound, RH, or the conjectured CCM determinant limit.

The important substantive improvement over round 5 is that the reference profile now has an unconditional, quantitatively tiny residual, while the ambiguity in interpreting that residual is demonstrated within the actual arithmetic form. The weaker overlap criterion is a sufficient RH target; it must not be reported as a solved estimate or as equivalent to the original prolate comparison.

## Analytic checks

1. **Unconditional identity and test class.** The polarized explicit formula uses \(\overline{\widehat f(\bar z_\rho)}\widehat g(z_\rho)\), including complex spectral parameters. The Xi factor makes the expression vanish without assuming real zeros. This is a statement about a distribution/form on appropriate weighted tests, not the kernel of a presumed positive self-adjoint operator on whole-line L2. Hard cutoffs and their tails have uniformly bounded weighted variation; paired transforms decay quadratically on the zero strip. The zero-side series and the regularized arithmetic expression admit the stated approximation argument.

2. **Hard-cutoff operator domain.** The Fourier decay O(1/|t|) makes the squared logarithmic multiplier integrable. Compressing its action, and adding bounded finite-window pole and prime operators, puts the hard restriction in the localized operator domain. H1 regularity of its zero extension is neither needed nor claimed. The logarithmic endpoint singularity is included in the residual bound.

3. **Explicit residual constants.** The archimedean off-support kernel, pole factor, and both prime directions have consistent normalization. The integral \(\int_0^\infty(e^tE_1(t))^2dt=\pi^2/4\) follows by a positive integral representation; a separate high-precision integration matched this identity. The proof itself is analytic. For prime shifts up to X, \(a=\pi X\) and \(|\log n-\log m|\ge|n-m|/X\) give the packet Gram bound with row sum \(\coth(\pi/2)\). The contribution above X is separately bounded, rather than omitted.

4. **Quadratic energy improvement.** The identity \(Q(f_b,f_b)=Q(k-f_b,k-f_b)\) follows by polarization of the annihilator relation. Both equal-sign and opposite-sign tail correlations are retained. The latter occur only beyond shift 2b. Bounds on absolute component energies yield an absolute Rayleigh estimate, not its sign. The improvement is a consequence of exact cancellation before estimates are taken.

5. **Near-zero cluster.** On the weighted space \(H^1\cap L^2(e^{2a|x|}dx)\), a>1/2, the full prime form is bounded using \(\sum\Lambda(n)n^{-a-1/2}<\infty\). Fixed finite families of translated Xi profiles have nonsingular limiting Gram matrices. Small operator norm on their cutoff span forces a spectral subspace near zero of at least the same dimension. This proves actual near-zero eigenvalues, not merely a min–max upper bound compatible with distant negative spectrum. Only under RH can these eigenvalues be identified with the bottom fixed-index levels. No uniform estimate in growing cluster dimension is asserted.

6. **Escaping moments.** The translated positive profiles have unchanged mean and half second moment \(\tau_k+a^2/2\). Choosing a=b/2 and cutting off near ±b gives residual tending to zero but moment \(\tau_k+b^2/8+o(1)\). Their norms remain nonzero. They are approximate null vectors; no actual-ground or finite-positive-mechanics assertion is made. This distinction is necessary for the counterexample's scope.

7. **Even negative witness.** Removing a hypothetical off-axis zero quartet with its full multiplicities produces a real even entire transform taking i and −i at conjugate selected zeros and zero at the others. Its inverse transform belongs to all the weighted spaces used. The explicit-formula energy is strictly negative, and compact cutoffs preserve it. Nontrivial purely imaginary Xi zeros would correspond to real zeta zeros in (0,1), which are excluded by the alternating-series identity. Thus an off-axis failure of RH is covered by the quartet argument.

8. **Overlap criterion.** For the bottom-even spectral projection E_b, \(|\varepsilon_b^+|\|E_bv_b\|\le\|W_bv_b\|\) follows directly from the spectral theorem. A cofinal ratio tending to zero forces the unshifted bottom energies toward zero. Domain monotonicity or the preceding negative witness then gives RH. This uses neither simplicity nor an odd gap nor that the even bottom is the full bottom. Applying the statement to a chosen cluster near zero instead of the bottom would be invalid. No converse from RH to the proposed overlap bound is supplied.

9. **Limits and discretization.** The continuum residual estimates do not establish finite Fourier residuals at the previously proposed polynomial schedule. L2 projection accuracy and accuracy in the operator graph norm differ. The finite data are not substituted into the infinite-dimensional criterion. The determinant conclusion still requires normalization and concentration beyond overlap.

10. **Effective low-space comparison.** The block elimination identity is exact where the complement resolvent exists. No lower bound for that complement or relative estimate for its correction is proved. The tail matrix gives an explicit trial form but is not by itself the effective form. A fixed-rank low space cannot be presumed to capture the growing near-zero cluster. These remain proposed research tasks.

## Numerical checks and corrections made

The [diagnostic review](CCM_XI_GROUND_DIAGNOSTIC_20260928.md) verifies that the proxy is the restricted analytic Xi kernel, rather than the finite prolate sum. It records small-block defining-form checks, normalization controls, and the targeted precision repeats. The ordinary residual is dominated by tiny components outside the first four finite even modes, whereas the angular error is dominated by the first excited mode. The raw second-even separation test fails in all selected cases.

The final synthesis explicitly distinguishes the centered finite residual \(\|(A-\rho)\widehat v\|\) from the uncentered continuum residual \(\|W_bv_b\|\). Table rounding was corrected, and the sharper packet-overlap residual replaced the earlier weaker triangle bound. The original numerical run versions are preserved for source-hash verification; portable entry points change dependency discovery and metadata without changing the mathematical routines.

Repeated precisions share formulas and are not interval certificates. A 32-to-64 cutoff comparison at X=13 changes the profile and moment, so no monotone improvement or cutoff convergence is inferred. The finite complement in the eigenbasis table is not the infinite Fourier tail.

## What remains missing

The core missing estimate is a lower bound on the true bottom-space overlap which dominates the known residual, or a stronger comparison that also controls the normalized transform and moment. The approximate-null family provides no such bound. Neither the positive profile of k nor the smallness of its boundary tail implies positivity or localization of the true ground eigenfunction.

A next substantive advance would control the orientation of an independently described low arithmetic space under its effective operator, with a proved complement estimate, or establish a direct quantitative localization/overlap theorem. Larger fixed-support matrices would be useful only as a test of one of those specified estimates. Sonin-residual work was not undertaken in this continuation.
