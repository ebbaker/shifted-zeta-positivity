# Finite precision, signed kernels and endpoint energy: internal review

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
**gpt-6-astra (Codex), reasoning effort ultra**, verified session metadata.
Separate delegated checks and root integration review, all using the same
model; no specialist review, cross-model review or novelty assessment.

**Verdict.** [Note 12](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) and [Note 13](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md) pass the stated bounded comparisons after the corrections recorded below. No all-height signed inequality, original multiple-zero exclusion, strict cap surplus, or simplicity proof has been obtained. The positive gate RHS-02 remains open.

The [result index](../../../../../../../result-summaries/README.md),
[control catalogue](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../../../avoid/README.md) govern this review.
In particular, [same-model checks](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[complete payment](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [checked imports](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
remain explicit limitations.

## 1. Corrected value algorithm and matched extraction

**Verdict: pass.** I checked [Note 12 §1](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) against the primary approximation and independently recalculated its alias, division, and matched-comparator bounds.

[O'Sullivan, *A generalization of the Riemann--Siegel formula*, Theorem1.3, equation(1.8)](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/Riemann-Siegel-2nd-revision.pdf) gives error `O(t^(-N/6-sigma/2))`, with the constant depending only on the fixed real-part interval and `N`. Its fractional-part parameter includes the entire interval `[0,1)`. Therefore `N=6` gives the stated `O(t^(-1-sigma/2))`, uniformly across cutoff transitions. The finite correction indices and the two square-root-length sums are correctly distinguished.

For each width, the Cauchy coefficient estimate uses the exact holomorphic function zeta on the radius-`a` disc. The sampled radius is `a/2`; root-of-unity averaging keeps precisely coefficients `b_(1+qJ)`. After multiplication by `a`, the complete alias tail is at most `M 2^(-J)/(1-2^(-J))`. The coarse bound `M<<gamma^(1/2)` is valid uniformly on the declared fixed strip, so `J=ceil(3log_2 gamma)` gives the claimed `O(gamma^(-5/2))`. The Riemann--Siegel approximation is only evaluated pointwise. Its truncation is never differentiated, and different floors at sample points cause no gap in the proof.

The value error and normalized derivative error are both `O(gamma^(-5/4))`. Division retains the reciprocal factor and the normalized exact logarithmic derivative. With the geometric smallest width, the resulting error is `gamma^(-3/4+o(1))`; the coefficient norm less than two prevents any additional factor from the number of widths.

For the matched one-width comparator `a` of order `L^(-3/2)`, the checked Balazard--de Roton formula has leading logarithm `log(1/a)=3ell/2+O(1)` multiplied by `V~L/(2ell)`. Its reciprocal exponent is therefore `3/4+o(1)`, as stated. The same approximation gives normalized division error `gamma^(-1/2+o(1))`. Both schemes consequently have sufficient leading summand exponent `1/2`; the geometric scheme retains its leakage cancellation and stability but no algorithm-independent exponent advantage follows.

The independent noncentral gap, center accuracy, all-zero leakage, arbitrary multiplicity, and control behavior remain unchanged. The count is explicitly for exact-arithmetic Dirichlet summands; neither roundoff, special-function implementation, bit complexity, optimality, nor a finite-height onset is asserted. No simplicity or strict surplus is obtained.

I also checked [Note 12 §2](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md): the uniform-height reciprocal payment, full vertical-kernel integration, horizontal-strip control, and exact double-zero residue are consistent. Its stated mollifier allowance is a sufficient absolute-error payment, not a lower bound on the actual error or a universal mollifier-length obstruction.

## 2. Separate reciprocal-contour check

**Mathematical verdict: passes within its stated scope.** The beta/Mellin identity, displacement to `Re w=-b`, and residue at zero are correct. No reciprocal-zeta poles are crossed because `Re(s+w)>=1/2+h`. The bound on `K_k` has only a logarithmic local integral and integrable tails for fixed `k>=2`. The sufficient cutoff `log Y=K(log gamma)^2`, `K>1/(2c)`, follows, whereas polynomial length merely fails to make this particular upper allowance small.

The primary Balazard--de Roton PDF was independently rechecked: Proposition 1 covers all `1/2<sigma<=2`, and Proposition 18 supplies the displayed typicality choice. The high-, intermediate-, small-, and compact-height splits in (M2) are valid. For horizontal contour segments, state explicitly that the same bound is uniform for shifts at least `h`: its small-shift bound improves with the shift, and its large-shift bound is `O_theta(V)`. The entire traversed strip has `sigma<2` for large gamma.

The double-zero Laurent coefficients and residue (M4) are exact. Other zero residues and the remaining contour cannot be dropped. The note does not assert that its sufficient mollifier length is necessary, nor import simplicity through a derivative moment.

**Repairs verified:** the author restored literal `O(1)` and `o(1)` expressions corrupted by equation-label substitution, and explicitly stated the uniform shift range used for horizontal segments. The current staged bytes contain these repairs. No actionable mathematical correction remains.

## 3. Separate polynomial-kernel and energy check

The review corrected one wording issue: symmetric rational energies are meromorphic in time, while the log-gap energy becomes analytic only after removing its explicit logarithmic singularity. All displayed energy constants are unchanged.

### Heat constants, exterior sign and domain

- With τ=√(2t), the backward heat equation gives the Hermite expansion in H3 with exactly Lτ He_{m+1} and (L²−S)τ²He_{m+2}/2. Expanding at a simple Hermite root gives the common drift Lτ² and the next term −Sλ_iτ³/2.
- The Hermite identity Σ_{j≠i}(λ_i−λ_j)^{−1}=λ_i/2, together with the cancellation of triple cross terms and Σ_iλ_i²=m(m−1)=2M, gives Σ_{i<j}(λ_i−λ_j)^{−2}=M/4. This verifies both finite terms in H4. Integer-power remainders follow from the discriminant and symmetric rational functions of the analytic cluster polynomial; the logarithmic singularity is separated first.
- The exact velocity identity gives U′=−4E−Σ_{i<j}(b_j−b_i)/(x_j−x_i). The exterior quotient sum tends to −2MS, so the finite part is +MS, as H4 requires. Dropping that term reverses the relevant finite bookkeeping. Squaring the H3 velocities gives the independently checked kinetic constant 4mL²−6MS.
- H7 is the exact conversion from the first nonzero endpoint derivative to g′/g and −(log|g|)″. The full exterior inverse-square sum converges under the zero count; the mirror zero contributes m/(4a²). No lower bound for |h_m| or upper bound for S follows from separate moment upper bounds.
- All expansions concern sufficiently small positive t in a fixed isolated-cluster disk. Weierstrass preparation and the scaled Hermite implicit-function theorem justify that local domain; they do not provide a pre-zero all-real interval. The primary [Rodgers–Tao paper](https://arxiv.org/html/1801.05914v2) explicitly develops its regularization under Λ<0 on a negative-time interval. That input is unavailable from RH alone at the endpoint.

### Signed-kernel constants and uniformity

- The odd positive polynomial roots pair as stated; removing their sign-changing intervals produces a globally nonnegative companion with no larger value outside the certified gap. Every exterior zero remains in S5. Equal degree preserves strip decay and the same declared Fourier-support bound. This does not transfer a gamma or pole budget.
- The sixfold interval convolution gives B_6(0)=11/20, B_6″(0)=−1 and B_6⁽⁴⁾(0)=6. These yield the three moments in S8, the exact threshold δg>√(3/2)/π, and the minimum 23/(60δ) in S10.
- On the final Fourier segment, differentiating s⁵/(120δ⁶) yields precisely the positive coefficients s³/(24π²δ⁶) and s/(16π⁴δ⁶) in S13. The change of variables x=e^{2π(3δ−s)} gives the S14 constant 2r!/π^{r+1}. The lower endpoint term in Stieltjes integration is exponentially smaller than the main integral, so the PNT error is relative o(1).
- Combining the three positive endpoint contributions gives exactly 2e^{3πδ}/(π⁶δ⁶)·(1+1/(4c²))(1+1/(4g²)). The interior/main ratio is O(δ⁵e^{−πδ}) uniformly over all 0<c≤g, including arbitrarily varying parameters.
- S15 is valid even when c/g→1: factoring c^{−2}−g^{−2} before estimating retains the positive endpoint main term, and the interior difference has relative error O(δ³e^{−πδ}). It is not an unjustified subtraction of two relative asymptotics.
- S16's bandwidth and cutoff constants follow directly from the mass-reduction threshold; minimizing 3πδ−6logδ on that range verifies the stated exponential prime-cost lower growth. The comparison remains confined to the declared acquisition schemes, with no optimal-complexity or full-envelope dominance claim.

No original multiple zero is excluded by either calculation. Their stated scopes and unproved endpoint/arithmetic inputs remain visible.

## 4. Controls, comparison and integration decision

Root independently rechecked the Riemann–Siegel strip and correction count, the discrete coefficient selector, the exact division estimate, the polynomial root replacement, the final B-spline segment, the factor two in the prime integral, and the double-zero Laurent residue. The heat-energy finite parts retain exterior forcing. The signed kernel's mass can decrease; no complete gamma/pole-envelope ordering is asserted.

The all-real endpoint controls still satisfy the zero-side extraction and polynomial comparison. At a double zero the central mass is two, and the heat energy has the same divergence. The exact zeta value algorithm and Möbius coefficients are not transferred to a changed control that fails their ordinary-Dirichlet premise. Conversely, the arithmetic finite-data control fails exact reflection and full-tail completion. Their preservation lists remain separate. Certified noncentral gaps and location accuracy are independent inputs, not outputs of RH or finite-wall continuation.

The main numerical improvement is a classical algorithm applied with its complete errors: both matched extraction schemes now have the same sufficient leading summand exponent. This does not establish a new algorithm, optimal complexity, bit cost, finite-height onset, executed interval certificate, or advantage over matched direct first-jet exclusion. The Riesz length is sufficient for this allowance and not necessary for the actual error. The polynomial lemma concerns one factorized kernel class, not every sign-changing test.

The endpoint-energy assessment does not activate BW09 HFCE-07. Rodgers–Tao's pre-zero all-real interval is a premise of that contradiction argument, not a consequence of RH alone. The original BW09 manuscript and its task registers remain unchanged.

The notes, their indexes, the current overview and progress register, and concise repository pointers are updated together. Note 09 now explicitly records the later matched-algorithm comparison without deleting its correct earlier Euler-sum calculation. No numerical source or fixture changed; the existing 265 exact-rational checks are not evidence for these new analytic estimates and were not rerun. No sign scan or new numerical campaign was performed. No manuscript snapshot was created.
