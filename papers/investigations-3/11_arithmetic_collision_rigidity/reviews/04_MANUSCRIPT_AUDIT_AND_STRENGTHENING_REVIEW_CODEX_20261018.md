# Review of the manuscript and its next quantitative targets

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Reviewing model **gpt-6-astra (Codex)**, reasoning effort
**ultra**, verified from the current turn metadata. This is a separate
review conversation using three parallel same-model agents and primary-agent
rechecking. It is additional internal LLM review, **not cross-model or
independent specialist review**.

## Disposition

**No blocking mathematical defect found in the reviewed proof chain.**
The positive packet estimates, exact finite Euler operations, endpoint
cancellation and scoped collision construction appear supported by their
written proofs and named imports. The manuscript accurately says that
the signed theta residual remains open. Its numerical accuracy is for
an auxiliary arithmetic tail, not for the complete field near a zero.

The most useful new outcome of this review is an actual strengthening:
[Note 05](../notes/05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md)
proves positive real part for positive higher-mode packets in broad
complex strips. It improves the carrier payment from 117 E to E/64 and
gives much sharper relative remainder derivatives. This makes the package
more useful for complex analysis without supplying a collision exclusion.

[Note 06](../notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md)
gives a finite-mode complex-strip approximation with an explicit
exponentially decreasing derivative error, extending the existing
contour idea from investigation 07. It identifies the missing positive
margin and the complete global contracts required for a Newman bound.

## Version and method

The reviewed manuscript is
[Positive Arithmetic Packets for the Theta Heat Flow](../manuscript/positive_arithmetic_packets/main.tex),
seven LaTeX files, whose current bytes match every source hash in
[BUILD_RECORD.json](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json).
The verified source-set SHA-256 is
`9def46d014fb1006ff3a16378f66bcd1b7991ea526739b65e8bbfccaf791962e`.
Notes 01–04, the previous three reviews, and the relevant repository-wide
summaries and controls supplied context. The canonical manuscript was
not edited; its reading-copy PDF was not rebuilt or subjected to a new
layout review.

The [new checker](../numerics/certify_strip_carriers.py) calls the original
exact-rational constant calculation, repeating every original printed
enclosure and headline check. It also checks the new scalar bounds.
[Its record](../numerics/STRIP_CARRIER_CHECKS_20261018.json) fixes the code
identities and exact rational intervals. All checks passed. It reuses
the original interval code and does not constitute a separate numerical
implementation. Earlier oscillatory packet/orbit programs were inspected
through their recorded scope but were not rerun for this review.

## Mathematical audit

1. **Normalization and Euler operations.** Rechecked the primitive
   operator, Mellin normalization \(H_0=\xi((1+iz)/2)/8\), the mixed
   logarithmic heat weights, source translations and the complex shifts.
   The half-line lower interval and the minus sign in its reflected first
   derivative are essential and correctly retained. The rejection of the
   divergent positive-time prime-power series is appropriately scoped.
2. **Positive modes and uniform bounds.** Recomputed the logarithmic
   source derivatives, convexity, sinc estimate, local interval lower
   bound, geometric tail and first two moment identities. The height-uniform
   quotient bounds use both absolute and inverse-square estimates. There
   is no extrapolation from finite numerical samples.
3. **Modular cancellation and event scale.** Checked the signs in the
   repeated endpoint integration, derivative asymptotics obtained from
   differentiated integrals, and the exact all-odd-endpoint cancellation.
   The fixed omitted tail has a nonzero inverse-square asymptotic. The
   normalized heat drift, Laguerre identity, local Taylor error and
   \(-1/s+O(1)\) stationary collision ratio are consistent. In particular,
   finite imaginary packet shifts cannot be substituted into a bounded
   local collision expansion.
4. **Rigidity and controls.** The Gaussian distribution uniqueness
   argument, reflection-defect ODE and normalized primitive endpoint give
   the stated coefficient rigidity. The finite-dimensional orbit
   nullspace construction retains its prescribed prime constraints and
   measurements. It necessarily has a first nonzero odd endpoint; its
   algebraic tail competes with the complete theta field's rapid decay.
   The logarithmic-curvature argument then supplies a nondegenerate
   extremum and hence an exact double event. The imported eventual
   real/simple-zero and strip results are stated with their positive-time
   scope and agree with [Polymath](https://arxiv.org/html/1904.12438v2),
   Theorems 1.5 and 3.2 and §9. The construction does not prescribe an
   effective height or a finite Newman threshold for the controls.
5. **New strip and curvature proof.** Two agents derived the broad-strip
   positive-real-part argument and the Schwarz coefficient bound, and
   the primary agent checked the scaling \(z=x+4m^2\operatorname{artanh}\zeta\).
   This yields \(\beta^2+|\beta_x|\le1/(4m^4)\), not merely a looser
   Cauchy estimate. The real remainder second derivative uses the
   deficits in both logarithmic curvature bounds; the factors are
   \(d_m\) and \(d_m^2\), with \(d_5=29/200\). These inequalities
   remain valid for the positive-coefficient collision controls.
6. **New shifted approximation.** Checked the complete contour shift,
   use of reflection on the negative half, both spectral derivative
   factors, heat equation, source majorant and geometric tail. Full
   reflection is used before truncation. Without it the omitted vertical
   contribution cannot be discarded. The finite approximant is not
   claimed to be even or globally real-rooted. Scalar tail constants
   do not establish a positive field or jet margin.

## What is worth pursuing

The current manuscript already supports a stronger auxiliary paper.
Its cleanest additional statement is the positive-real-part strip theorem,
with the consequences
\[
 |(\log A)_x|\le1/8,\qquad
 |(\log A)_{xx}|\le1/64,
\]
and, for the two-prime remainder,
\[
 |r_x|<1.06\,10^{-25},\qquad |r_{xx}|<1.54\,10^{-26},
 \qquad \sup_{|\Im z|\le1}|r(z)|<8.5\,10^{-25}.
\]
The old 117 bound is valid but unnecessarily loose. Even the old argument
alone gives a one-sided payment below 0.671 E; the strip theorem supplies
the substantially stronger absolute bound. Extending the time interval
to 24 is also possible but has little relevance to improving Lambda.

For collision research, the priority should be a complete signed margin
after modular cancellation, tested first on a bounded domain. The shifted
finite approximation provides an explicit error budget for that test.
It should be compared with the existing complete-source method before
large computations begin. A positive-time slab or the full published
canopy/barrier contract is a coherent consumer; isolated windows are not
a new bound. The reviewed notes separate these proposed tasks from results.

## Limits and control screen

The [result-summary index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md) govern this assessment.
In particular, the finite global joint-zero target is already recorded as
RH-equivalent in [summary 13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md).
No reformulation of it is counted as a gain. The new numerical constants
are auxiliary quantitative gains; the contour identity is an approximation
tool with a proved error, not an exclusion mechanism by itself.

The controls in [summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
are screened explicitly in Note 06. Finite-prime and weighted-square
controls pass positive higher-mode strip geometry but fail normalized
analytic reflection. Reflected smooth controls can pass reflection but
lack the exact theta square-mode data. Euler-factor controls alter those
data. Any finite-domain certificate must actually fail its strict margin
on a domain containing an applicable control's event. These are analytic
premise checks, not newly computed control certificates.

Thus the results are promising as quantitative analytic tools. They do
not yet give a numerical upper bound for Lambda, a theta collision
exclusion, or a demonstrated reduction in the remaining global workload.
The next claim should be judged by a certified margin, error at the
physical scale, effective coverage, or measured consumer improvement.
