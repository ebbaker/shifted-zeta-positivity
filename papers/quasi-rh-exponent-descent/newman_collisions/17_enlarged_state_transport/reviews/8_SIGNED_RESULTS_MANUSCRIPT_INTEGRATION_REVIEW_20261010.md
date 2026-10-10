# Signed-result manuscript integration review

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6-astra (Codex), reasoning effort ultra, recorded integration-turn
configuration. This is an internal separate-agent LLM audit, not independent
mathematical validation or a priority assessment.

## Scope and source checks

This review covers integration of investigation 17 Notes 12–15 into
enlarged_state_transport_and_heat_flow.tex, with the necessary matched
contour and Mellin context from Notes 9–10. The numerical source and retained
record are numerics/check_high_stationary_s1_cell.py and
numerics/HIGH_STATIONARY_S1_CELL_RECORD_20261010.json.

The checker source SHA-256 is
d5f2ab504352b71c02625e4ef3332411ba3d8768a8df9d2ab83643b8d1b76c27,
matching the retained record. The record reports PASS. No fresh numerical
replay is needed for this manuscript-only integration because the checker,
parameters, and numerical claims have not changed. This review checked the
reported outward intervals and their mathematical use, rather than treating
a matching hash as a proof.

## Mathematical audit

1. **Exact carrier defect.** Conjugating the real second-order operator by
   the physical normalizer gives the stated normalized operator. The
   individual defect retains both the linear and quadratic terms in
   log n, and the n=1 term vanishes exactly. Differentiation followed
   by elimination on the genuine physical set Hxx=0 gives
   L1 = B Hx² − Hx Rcal with B=b−a′+ab′/b. The derivation never divides
   by Hx. The third-order error expansion, complete Cauchy payment, and
   sign-oriented finite criterion have the correct signs and coefficients.
   The explicit nonzero conditions on Omega and b are necessary.

2. **Cutoff-edge absolute masses.** The natural-cutoff normalization is
   N w_N = exp((4−kappa)L/16)(1+o(1)); the limiting edge measure is
   exp(−y/2)dy. The limiting physical derivative coefficient is
   −pi/8−iy/2, and the defect divided by its leading positive coefficient
   has the same limit. The stated integrable tail bound proves the
   required uniform Riemann-sum limit. The conclusion excludes an
   absolute fixed relative reserve and a first-carrier absolute
   perturbation argument. It neither decides the signed physical
   correlation nor excludes a reserve tending to zero.

3. **Complex currents and degeneracies.** For the complete complex channel,
   |Cxx|² L1 = 4 I1 I2 is exact on Hxx=0. A zero of the complex
   second derivative is a real exception to the sign inference; analyticity
   alone does not remove it. The strict first relative cone forces the
   first complex derivative to vanish at that exception. The second
   cone may be nonstrict. The resulting lower bound therefore covers
   the exceptional set without division by a potentially vanishing
   physical derivative. Absolute current payments have the required
   cross-error term.

4. **Positive-spectrum obstruction.** Direct differentiation of the two
   positive cosine terms gives the displayed strict stationary violation.
   The positive-frequency complex second derivative is nonzero there.
   Smoothing by a Gaussian gives a positive even spectral density and
   preserves a nearby violation by the ordinary implicit function theorem.
   This is a generic spectral control, not a counterexample for the
   genuine theta source, and compact bandwidth is not claimed after
   smoothing.

5. **Matched contours and fixed-product asymptotics.** The full even
   kernel is formed before its negative contour is reflected and the
   positive-half-line product series is truncated. The incomplete
   Mellin–Bessel formula retains both endpoints and the mixed derivative
   in the J1 readout. The exact gamma-channel polynomial has coefficients
   1,−1,5,2,−1,−2 in the displayed order; the third logarithmic
   derivative cancels. The leading constants 4096 and 32768, and
   the phase −pi/4, check against the gamma asymptotics.
   A fixed-product negative-half-line endpoint estimate transfers the
   auxiliary gamma oscillation to the legitimate matched channel.
   The statement is restricted to time zero and fixed product, imposes
   no physical stationarity, and is not a uniform positive-time sign
   theorem. Positive-time raw all-line absolute integrability fails;
   the complete glued source remains integrable.

6. **Nonempty high-height stationary branch.** The retained outward
   record separates Hx/A below zero and Hxxx/A above zero on the
   entire stated rectangle. Opposite endpoint signs of Hxx/A imply a
   unique zero of the physical Hxx for each time. Monotonicity is
   asserted for Hxx, not for its normalized ratio. The stationary
   point lies in the candidate band [87.400,87.425], where the
   recorded product upper endpoint is −13941.9506022330639...,
   supporting the rounded strict bound <−13941.95. That sharper
   product bound is attached only to the candidate band. The complete
   disk approximation is assumed at every physical center; its third-jet
   error is fully paid. Since Hx is already separated from zero, this
   branch provides a calibration, no additional collision exclusion and
   no predecessor neighborhood below the rectangle.

## Integration requirements

The manuscript must distinguish the real finite approximant from the new
complete complex channel, and the logarithmic Stirling exponent from the
theta source. Physical derivatives hold time and cutoff fixed; derivatives
of the Mellin channel hold its separate parameters fixed. The abstract and
conclusion must recognize the successful bounded high-height calibration
while retaining the uniform-sign, vanishing-slope, predecessor-coverage,
and RH limitations.

The existing author field, “Drafted for Edward Baker”, is appropriate.
The preparation record should add this integration's verified model and
effort without retroactively filling unavailable effort fields in the
earlier notes. Notes and retained checkers remain internal project sources;
classical Bessel and gamma identities require their primary-source citations.

## Conditional arithmetic synopsis

The manuscript's separate summary of Note 11 preserves its assumed
fixed-modulus prime-counting input. The exponents 23/24+beta/12,
1/2+beta/2, and 87/41−2beta, and the comparison threshold beta<8/41,
agree with the note. The synopsis explicitly concerns a selected-column
filter and leaves cancellation by the remaining actual response possible.
It does not promote the external quasi-RH premise to a proved input or
infer a complete short-family moment.

## Final integrated-source check

The complete staged source was inspected after integration. It has 136
distinct labels and 107 cross-reference uses, with no duplicate labels or
unresolved references. All 20 bibliography entries are cited, and every
citation resolves. Begin/end environment counts agree.

The source now uses a separate complex-channel symbol, a separate theta
source symbol, a distinct Mellin variable, and a superscripted single-product
channel distinct from the finite product partial sum. The new stationary
proposition retains physical normalization, the entire third-jet payment,
existence and uniqueness, and its lack of added collision coverage.
The program identifies signed relative control near a vanishing slope
and growing-product positive-time endpoint control as open.

The final abstract clarifications were applied: the high-height rectangle
is explicitly conditional on the complete disk, and fixed-product
oscillation is restricted to the second Laguerre expression. The new
proposition explicitly assumes the disk input at every physical center
of the rectangle.

The author and preparation record preserve the older unavailable effort
metadata and separately record the verified integration-turn configuration.
No mathematical blocker was found. The final saved standalone source
compiled successfully with the desktop editor's native compiler, after
repairing a missing grouping brace introduced by the theta-source
notation change. The final scope clarifications were included in the
successful build. The built-in source/PDF preview remains the delivery
surface; no separate PDF export or terminal TeX installation was used.
Compilation confirms a successful build, not mathematical validity.

Final compiled source SHA-256:

```text
c5f0c1b72cef849bbadef6049b62775ffc3146e8297458fbf287c1ebab1c0e95
```
