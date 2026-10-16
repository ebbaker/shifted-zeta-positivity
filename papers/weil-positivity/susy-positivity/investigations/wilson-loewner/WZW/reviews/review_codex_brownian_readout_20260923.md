# Same-assistant audit: Brownian bridge readout test

**Numerical correction, later on 23 September 2026:** the transformed prime-free kernel correction integral in the diagnostic used `exp(-2*v)` instead of `exp(-(3-2*omega)*v)`. The written convolution formula was correct. The implementation and record have been corrected and the complete suite replayed successfully. See the [modular-scattering note, Section 8](../notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) for the derivation, independent regressions and scope; the analytical exclusions are unchanged.


23 September 2026. Prepared for Edward Baker with LLM assistance.

Model: GPT-6 (Codex; developer-provided identity). Effort: not exposed; not inferred.

Reviewed artifact: [Brownian bridge readout test](../notes/BROWNIAN_BRIDGE_READOUT_TEST_20260923.md), with its [program](../numerics/check_brownian_readout.py) and [record](../numerics/records/brownian-readout-20260923.json).

This is a same-assistant claim and formula audit, not an independent specialist review.

## Findings

The test has a concrete stochastic system, signal preparation, mean readout, propagation coordinate and ordinary norm. It does not infer an input/output operator from a moment ratio alone. The main negative result is supported by incompatible local kernels and an independent boundary-modulus argument. The note also preserves the genuine positive result: completed xi is still a natural scalar moment observable.

The following distinctions are essential to the conclusions and are retained in the note:

1. **Distribution versus paths.** The pair of BES(3) exit times, with the pi/2 normalization, has the law of the squared normalized bridge range. This does not identify their physical clocks or construct a pathwise transformation.
2. **Mellin versus Laplace.** E[D^(s/2)] yields xi; E[exp(-p D)] is the actual causal delay transfer. The numerical comparison calculates each separately.
3. **Radius versus arithmetic shift.** Lambda is the radius squared. The displayed numerical comparison lambda = omega is a control. The local analytic exclusion applies to every fixed positive radius, so the conclusion does not rely on that guessed clock.
4. **Mean signal versus quantum amplitude.** The positive delay averaging is an explicit classical readout. The wider exclusion does not apply to arbitrary coherent scattering amplitudes or matrix-valued channels.
5. **Whole-line versus finite-window norms.** The Brownian mean balance has only fluctuations and future output. A compression of the logarithmic phase unitary can also discard earlier-than-zero output. Its norm bound therefore does not certify the desired causal Volterra norm.
6. **Unbounded inverse versus bounded quotient.** The logarithmic smoothing operator has no bounded inverse, but its adjoint quotient has a bounded unitary extension. The latter is proved through equal norms on a dense range. Unbounded inversion is not used to reject that extension.
7. **Boundary phase versus causality.** The exact unit-modulus boundary multiplier follows from the functional equation without RH. Causality of the full positive-shift family is the missing RH-equivalent assertion; no contour shift through potential poles is silently made.

## Formula audit

The radial generator is (1/2) d^2/dx^2 + (1/x) d/dx for standard three-dimensional Brownian motion. The regular solution of its exit-time equation gives r sqrt(2p)/sinh(r sqrt(2p)) at the center. Two independent waits and the factor pi/2 give (sqrt(pi lambda p)/sinh(sqrt(pi lambda p)))^2. Its first moment pi lambda/3 and variance pi^2 lambda^2/45 agree with the completed-xi moments.

Differentiating the two range-distribution expansions gives the two stated densities of D. The small-d branch yields the coefficient 4 pi^2 lambda^(5/2) in the exponentially flat kernel. The completed arithmetic kernel has leading coefficient (2 pi)^omega/Gamma(omega), and the first delayed coefficient is c_2(omega) times that coefficient. The numerical record retains the gamma/rational prime-free kernel, rather than comparing only an Euler-product term.

For the logarithmic construction, the Jacobian d = exp(2x) and the central weight Y^(1/2) give 2 exp(5x/2) g(exp(2x))/E[Y^(1/2)]. The transform of exp(-omega x) q(x) is M(p+omega) under the exp(-p x) convention, by evenness of M. This fixes the order of the ratio and avoids inadvertently taking the inverse of K.

The positive-delay proposition uses modulus one at all frequencies (or almost everywhere plus continuity), not at one frequency. A discrete lattice delay may have modulus one at selected frequencies; it does not evade the proposition. The Bessel density has support on every positive interval, so strict attenuation holds at every nonzero frequency.

## Numerical scope

All 51 recorded cases pass. They are floating diagnostics at 45 decimal digits; the oscillatory phase integrals use 15 guard digits, and one complex moment also has a 60-digit refinement. The phase comparison integrates the physical density before comparison with the independently evaluated xi quotient. The theta truncation uses 12 terms and rapidly decaying small/large branches. No enclosure arithmetic or Monte Carlo uncertainty claim is made. The finite-window norm control uses a unit constant waveform and independently compares a density integral with the range-distribution formula; the general L2 identity is proved analytically.

The program records its own SHA-256 and parameters. The record's passing status includes confirmation of mismatches; it is not a positive arithmetic-realization result. Previous 60-case and 72-case records are neither rerun nor merged into this suite.

## Residual research question

A coherent physical operation could in principle realize the phase extension without implementing an unbounded inverse as a separate step. This test has not constructed such an operation or proved its causality. That is the appropriate next Brownian question if the branch is pursued. The present result excludes ordinary positive delay readouts, not every physical use of Brownian paths.
