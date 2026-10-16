# Internal review of the Poisson refinement and signed Gaussian criteria

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is parallel same-model internal analysis and cross-review, not
independent specialist refereeing or formal proof verification.

The [Poisson continuation](../../../notes/height_adapted_zero_detection/gaussian_localization/POISSON_SMALL_DIVISOR_REFINEMENT_20261004.md)
proves an unconditional improvement of the removable divisor cutoff from
\(e^{15k}\) to \(e^{77k/5}\), with deletion error below \(\eta_N/16\)
on all saved detector samples. The signed notes give conditional arithmetic
criteria. Neither the
[basic dyadic criterion](../../../notes/height_adapted_zero_detection/gaussian_localization/SIGNED_DYADIC_ATTEMPT_20261004.md)
nor the
[cofactor-aware criterion](../../../notes/height_adapted_zero_detection/gaussian_localization/COFACTOR_AWARE_SIGNED_CRITERION_20261004.md)
proves the required bound on actual Möbius sums. No new zero-free box follows.

## Poisson deletion checks

Separate calculations checked the Fourier convention and rotated-ray
sign \(-\operatorname{sgn}(m)/T\). The Fourier exponential decays on
that ray for either frequency sign. The carrier factor may grow on one
ray, but its growth is explicitly bounded by \(e^{T/T}\); it is not
silently discarded. The logarithmic Gaussian controls both joining
arcs, and the principal logarithm branch is preserved.

Summing the positive Fourier majorants geometrically pays for every
nonzero mode. The bound \(u^{5/2}/(e^u-1)<2\) then uses one fractional
Gaussian moment. No extra zeta factor belongs in this geometric-sum
calculation. The exact exponent is \(-639k/16\) before summing divisors,
and \(-23k/16\) after \(D=e^{77k/5}\). The coefficient \(847/900<1\),
least-sample monotonicity, and all-\(N\) base budget were checked.

The weak product cap, strict divisor cutoff, and strict active cofactor
ceiling are retained. The new cofactor ceiling is \(e^{53k/5}\).
The inherited full-divisor coefficient bounds still pay the upper
product and optional frequency tails. The continuum coefficient is
updated with the new cutoff, using \(254k^2\), rather than the old
coefficient 241. Its Gaussian pole damping remains affordable.

The numerical ceiling near 15.41994 is explicitly a scale diagnostic
for this absolute contour envelope. It is not an optimality claim about
all contours, arithmetic signs, or zero detection methods. The literature
link supplies context for logarithmic-Gaussian contour methods, while
the actual twisted bound is proved directly in the note.

## Signed arithmetic checks

The basic signed calculation retains the exact upper partial-summation
term at \(B/r\). Its integral estimate and Gaussian moment bounds
include all cofactors, and lead to the stated full-target bound from an
assumed finite twisted-prefix estimate. The dyadic prefix condition is
required for every real partial endpoint, rather than only completed
blocks. Its conclusion is an explicit sufficient zero-exclusion criterion,
with the arithmetic hypothesis left open.

The ordinary absolute envelope does not reach that criterion. The
mean-square control is correctly kept as an average; no exceptional
carrier is removed without a separate estimate. A synthetic coherent
coefficient control demonstrates why bounds using only coefficient
moduli and phase factorization cannot prove the desired prefix saving.
It is not asserted to describe actual Möbius coefficients.

One elementary exponential lower bound in the basic criterion's opening
draft was corrected during internal review: \((5/2)^{17}\) is too small
for that particular certificate. The final exact base proof uses
\(e>8/3\) and \((8/3)^{17}>7935000\). The claimed budget itself was
not changed. The replay checks the corrected proof seed.

The cofactor-aware continuation derives an amplitude derivative bound
after factoring out the carrier. It introduces a secondary cutoff and
compares two finite signed targets by an exact identity. The continuum
difference cancels through that identity, and the secondary product
tail is separately paid. Its weaker \(Y^{13/20}\) arithmetic input
also remains unproved. Bounds on an infinite untwisted Mertens function
are not inserted as if they were available unconditional arithmetic.

A separate internal cross-review found no blocking issue in the final
cofactor derivative identity, rotated amplitude moments, secondary
cutoff, all-sample budgets, terminal caps, or the comparison identity's
signs. Its continuum bound uses \(334k^2\), and the two conditional
signed errors are each below \(\eta_N/1000\). This supports the
conditional transfer, without supplying its arithmetic hypothesis.

## Replay scope and remaining work

The [replay guide](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
links the new standalone standard-library checker and small record.
It checks formal-log coefficient identities, complex rational cap
identities, fractional-moment and derivative constants, elementary
exponential budget seeds, and synthetic partial summation. Source hashes
identify the inputs; they do not prove analytic statements.

The final replay passed 4,096 formal prime-log coefficient identities,
76 complex-component cap cases, 23,636 retained-pair cutoff checks,
16 rational geometric-mode identities, and 264 exact polynomial
partial-summation cases, together with the constant and budget
certificates. These counts describe finite verification coverage.

Exact algebra and rational inequalities do not constitute formal
verification of contour deformation, Poisson summation, or analytic
all-parameter estimates. No giant prime or Möbius enumeration, actual
zeta-zero computation, or continuous-carrier certificate is performed.
The analytic proofs supply those transfer statements, with the required
arithmetic cancellation still an independent hypothesis.

The next substantive question is whether the finite twisted-Möbius input
in the cofactor-aware criterion can be established using arithmetic
structure, or whether a different joint estimate can bypass that sufficient
input. Additional optimization of the absolute Poisson cutoff would bring
a much smaller logarithmic gain. No manuscript snapshot, commit, or
unrelated working-tree edit is part of this continuation.
