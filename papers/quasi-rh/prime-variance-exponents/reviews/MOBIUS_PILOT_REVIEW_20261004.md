# Möbius and Vaughan pilot: independent code and mathematics review

4 October 2026. Internal LLM review.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is not independent specialist refereeing or interval certification.

Reviewed [pilot.py](../numerics/mobius_reduction_20261004/pilot.py),
its retained [record](../numerics/mobius_reduction_20261004/record.json),
and the underlying
[arithmetic reduction](../notes/MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).
No substantive implementation or mathematical error was found.
The reviewed script SHA-256, matching the record, is
`a31671f8f2b0afc654151b4c642fcbaf673022b34275ffe43263c910a78a0476`.

## Formula and indexing audit

- Differentiating h=(1-16v²)⁸ gives exactly the factored polynomial used
  in `weight`: −64v(1−16v²)⁵[2688(1−80v²)+(1−16v²)²]. The final
  division by √(νt) has the correct normalization. The support mask
  avoids evaluating log at zero and implements zero endpoint values.
- The sieve correctly retains μ(1)=1, sets μ to zero on squareful
  integers, changes its sign once per distinct prime factor, and assigns
  log p to every power p^j in Λ. Index zero makes no contribution.
- `N=floor(2BX)` retains the entire shell. Divisor low/high slices form
  a complete disjoint split at D. The tighter bound K=N//(D+1) is exact
  for integer d>D; it omits no terminal cofactor or partial support band.
- The pilot's cutoff factor 1/4 is stated in its record. It is a fixed
  multiple of the analytic cutoff, so it preserves the quadratic error
  theorem with changed constants. Flooring the real cutoffs implements
  their integer inequalities exactly.
- For m>U, the constructed coefficient
  −Σ_(d|m,d≤U)μ(d) equals Σ_(d|m,d>U)μ(d); for m≤U the required
  coefficient is zero. The bilinear array is therefore precisely
  Σ_(mn=r,m>U,n>U)A_U(m)Λ(n). The inner Λ includes prime powers.
- The continuum has the correct sign and value c_wΣ_(d≤U)μ(d)/d.
  The centered Type II response adds x times that coefficient.
- Gauss–Legendre nodes x=X(3/2+z/2) and weights Xw_z/2 give the correct
  shell Jacobian. The cofactor Gram uses these same positive weights;
  its trace and full signed sum have the claimed meanings. The pilot
  uses the negative of the note's individual C_k convention, which
  leaves every Gram entry unchanged.
- The linear projection denominator is exactly ∫_X^(2X)x²dx=7X³/3.
  Quadrature with at least two nodes integrates that denominator exactly,
  giving the orthogonal shape/scalar split up to floating rounding.

## Independent calculations performed

An independent trial-division implementation agreed with the μ and Λ
sieves at every integer through 2000. Exact rational evaluations of the
derivative-defined g₀ agreed with the factored formula at nineteen
rational interior points. At an additional real shell X=100.25, direct
divisor enumeration reconstructed the Type II coefficients and cofactor
components independently of the array slices. The response, centered
Type II, shape, scalar mismatch, cofactor energy, and Gram diagonal
agreed to maximum absolute normalized difference 8.9×10^(-16).

For the retained six-shell record, the largest 128-to-256-node change
among the normalized energy columns was 9.64×10^(-7), occurring in a
cofactor diagonal. Maximum coefficient-identity error was 3.20×10^(-14),
response-identity error 4.35×10^(-11), and rank-one splitting error
divided by X² was 5.35×10^(-16). These are floating consistency checks,
not rigorous quadrature error bounds. The published outputs correctly
carry that limitation and do not infer an asymptotic exponent.

## Additional analytic check

Also checked
[higher-order reconstruction](../notes/HIGHER_ORDER_SHORT_INTERVAL_RECONSTRUCTION_20261004.md).
The fourth-order and fifth-order remainder constants, three-scale moment
cancellation, even Peano kernel, its positivity/mass/maximum, and sixth
derivative endpoint-atom signs and scaling are consistent. The endpoint
prime-mass estimate yields the stated O(X) norm error at h=X^(11/12);
the signed three-length covariance includes the correct 40 and 256
normalization factors. The optional relative-average multiplier and its
noncancellation half-plane are also correct.

The source of the sieve estimate was checked by the originating agent;
this review checked its use and exponent accounting rather than
independently reproducing that published proof. Minor presentation
issues in that draft note were reported: stray `qquad`/`quad` text and
inline formula delimiters. For literal finite-range statements, defining
V_h for all h>0 or restricting the three-scale discussion to h≥4 avoids
the earlier displayed h≥1 convention when h/4<1. Its asymptotic claims
already have h/4≥1 eventually and are unaffected.

The analytic sector reductions establish quadratic discarded errors.
The observed signed covariance cancellation is a finite diagnostic;
the remaining global arithmetic estimate is unproved.
