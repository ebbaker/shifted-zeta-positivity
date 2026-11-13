# B10 signed Mellin estimate — same-assistant assessment

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0007, thread
`01a1d19b-462e-7722-a6be-3d1555a82423`. Actual model and reasoning effort
are unavailable in the recorded configurations. This assessment is by
the proof's authoring assistant; it is not a separate-agent, different-model
or independent specialist review.

**Disposition: retain Note29 as proved in-note from the named published
and inherited inputs, with same-assistant checking.** A fresh proof audit
is recommended before manuscript integration. The quantitative conclusion
is the shorter averaged range ell≥U^(17/81+ρ), with unchanged logarithmic
residual/Green rates. There is no every-center or zero-exclusion result.

The [proof](../notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md)
and [return](../notes/30_GNP_RS_B10_RETURN_AND_MODEL_CHANGE_20261112.md)
follow the [result index](../../../../../result-summaries/README.md),
[heat-flow cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
and [avoid index](../../../../../avoid/README.md). This is a numerical
exponent gain in an averaged theorem under
[avoid01](../../../../../avoid/01_restating_the_target.md), not a new
criterion equivalent to the desired pointwise conclusion.

## 1. Exact consumer and source import

The identity Q=4 sum w_n²+2 Re S is exact with B07's Fourier convention.
The conjugate pair in the square is essential: the proof bounds Re S,
not the modulus of each complex, one-sided m-block. The tail consumer
needs the former. After splitting at Z, |low+high|²≤2|low|²+2|high|²
pays all cross terms without postulating their cancellation. No change
to the original field or coefficient cutoff is made.

The source input is Bourgain–Watt v1 **Theorem 4**, whose statement on
printed page 1 was checked in both extracted text and the rendered PDF.
It is a cumulative error estimate. Its use in a local interval retains
the complete R^θ error at both endpoints. It is not Theorem 3's
short-interval statement or Theorem 2 used outside its shift range.
The explicit source slack 19/60-1515/4816=151/72240 and the fixed
ε_src=151/144480 are correct. Negative frequencies and intervals
crossing zero are covered by conjugation and splitting. The complete
published proof was not re-audited.

## 2. Mellin cutoff and error audit

The cutoff in (B10.5) equals the required weight at every integer:
for Z+1≤n≤B both smooth factors equal one; at all other positive
integers one factor is zero. Thus smoothing between integers costs no
coefficient error. The upper extension by 3/4 is included in the weight
and derivative bounds. The normalization b(n)n^(-1/2+iτ)=w_n n^(iτ)
is correct.

On this support a(x)=sqrt(x)w_x has maximum O(U^(-1/18)). Its total
variation is O of the same scale. Boundary transition widths in the
logarithmic variable are 1/Z and 1/B. Therefore their first-derivative
L1 cost is O(A), second-derivative cost O(AB), not O(A) for every
order. This distinction is retained in the kernel B/v² tail. The
kernel's L1 norm is O(A log U), not a claimed constant.

The contour identity includes the ζ pole at z=1-s with positive
residue tilde b(1-s). The residue is bounded by O(A sqrt B/U), hence
its square costs O(A²U^(-3/2)). It is not silently omitted. Smooth
compact support supplies higher-order decay for contour convergence;
the uniform quantitative integral uses the explicitly bounded first
two derivatives.

The tail |v|>U contributes at most O(AB U^(θ-1)) to the weighted
kernel moment. Since B≤sqrt U and θ<1, it is dominated by
O(AU^θ). This is the decisive check preventing projection from
silently expanding the local averaging interval. Cauchy–Schwarz and
Tonelli are applied with the positive measure |k(v)|dv. The u-to-zeta
frequency map has derivative -1/2, giving only a fixed Jacobian factor.

These checks support (B10.11) and its signed real-part consequence.
They do not supply an estimate for the imaginary part or for arbitrary
independent coefficients; the exact ζ/Mellin identification is used.

## 3. Low modes, complete norm and residual ledger

B08's phase class and its N²/(Uh) remainder remain intact. Only the
amplitude envelope is sharpened to the actual w_N². For N between
Y/2 and Z, the exponent quadratic is convex. Its endpoint main powers
are 377/1400 and 17/63, with positive difference 1/1800. Floors and
fixed dyadic factors cost bounded multiplicative factors, because the
error in the logarithm is O(1). Summation over all dyadic blocks is
explicitly paid by log U.

Large shifts and noncomparable pairs retain their U^(3/8)ell^(-4)
payment. The low/high split is at the coefficient level. Complete
floor crossings and the small phase drift retain B07's full-support
freezing cost. The finite-head norm is checked independently by the
diagonal and the decaying Y^(11/4)/ell² Fourier allowance, so A0
controls both the entire arm and its head, as required.

All terms of B08 (B08.14) reappear in (B10.20). Retuning M,Y from
U^(1/9) to U^(1/10) is necessary for the shorter range. The exact
source, low/high, head, reflected, large-shift and clock exponents
are checked in the [small record](../numerics/17_GNP_RS_B10_INPUTS_AND_CHECKS_20261112.json).
In particular the high norm-square margin is 7/1620; the retained
head margin is 4/405; the frequency gate exponent is 1/2<7/8.
Taking square roots and then reserving half the margin for product
and logarithm absorption gives min(7/6480,9ρ/28), as stated.
The ell≥sqrt U overlap follows from B08 with its fixed ρ8=19/72.

At the handoff's test point δ=1/144, ell=U^(11/48), the new low
and high costs have negative powers -25/1008 and -17/720, whereas
the old leading allowance has power 1/112. This is a strict instance
of the requested gain, not a numerical experiment.

## 4. Scope, controls and unresolved work

The earlier internal-parameter obstruction in (B10.23) follows from
(7.3), using R≥2 to compare (R-1)² and R², and the two inequalities
H/R²≤B1 and H/N_BW≤B1. It excludes only extensions retaining
those constraints; it is not a lower bound on the actual sum or a
universal failure of the Bombieri–Iwaniec method.

The [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
are screened against the full canonical arithmetic and physical readout
in Note29's table. The generic mean-square inequality may have analogues
for colliding fields. The source/arm identification is what fails for
the named controls, and no averaged estimate here contradicts an
isolated collision. This preserves
[premise02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [separate-bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

The inherited complete-field provider retains its earlier internal
review level. No independent provider audit, numerical onset,
every-center value, maximal/persistence theorem, full-c extension,
varying-cutoff result, shrinking-depth theorem or positive-threshold
exclusion is supplied. The proof and this self-check have shared
premises and should be assessed accordingly.
