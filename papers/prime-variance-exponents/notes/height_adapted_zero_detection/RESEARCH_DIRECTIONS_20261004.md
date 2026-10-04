# Research directions for height adapted zero detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: research map and proposed deliverables; no new zero-free region
or height-uniform arithmetic saving is proved.

Read the [program overview](README.md) first. The technical basis is the
[research assessment](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md),
especially sections 2, 4, and 5. The directions below are proposals unless
a specific existing lemma is identified. They are ordered by their
usefulness to establishing the detector and arithmetic interface, not by
a claimed probability of solving the zero-free problem.

## Quantitative detection on a finite prime-scale interval

The first question is how a zero in a specified height box forces a
measurable response on a computable interval of log X. The order-one
central coefficient is helpful, but phase cancellation between zeros
prevents a single-coefficient argument.

Investigate a localized explicit formula combined with a Turan or
Kolesnik--Straus power-sum argument. It must handle clustered zeros,
multiplicities, an exposed zero or other justified substitute for a
rightmost zero, remote zeros, and the initial transform cap. Record the
dependence of the lower threshold and interval length on the box width
and local zero count.

The [opening detector lemmas](DETECTOR_LEMMAS_20261004.md) give a bounded
local reciprocal of D_t0. Investigate division by -D_t0 in a
localized test to restore positive multiplicity residues. A global inverse
requires separate control of preparation zeros, convolution tails,
and the pole at one. If an exposed-zero replacement changes the height,
specify a computable guard band instead of assuming it stays in the
original candidate box.

The primary model is
[Schlage-Puchta, Theorem 3 and its power-sum proof](https://arxiv.org/html/1912.00853):
one off-line zero forces a large PNT error on a specified finite interval,
with computable constants. That theorem concerns psi minus x, not our
prepared scalar. Adapting the proof is a proposed task; its constants
and first-excursion range cannot simply be imported.

A useful first deliverable is a conditional box-exclusion theorem whose
arithmetic upper-bound hypothesis is completely explicit. It remains a
transfer theorem until that hypothesis is proved independently. Reject a
derivation that assumes zero separation, simplicity, a rightmost zero,
or a truncated zero sum without budgeting the assumption or remainder.

For example, if a converse supplies a response threshold
c exp[-delta u-L_det], with delta=1-b, the complete arithmetic
decomposition must satisfy

\[
R_{\rm arithmetic}(u,t)+R_{\rm comparison}(u,t)
<c e^{-\delta u-\mathcal L_{\rm det}}
\]

throughout the covered continuous windows. The detection loss, guard
band, and interval must be determined before this inequality defines
a useful target. An inverse-test norm that erases the central coefficient
gain is a reason to reconsider the route.

## Uniform arithmetic reduction for the complex family

Redo the scalar Vaughan comparison, density centering, complementary
divisor deletion, and Mellin truncation for ell_t0. The fixed-probe
subpower reduction is already proved; the full uniform complex extension
is not.

Start with the exact continuum identity in assessment equation (22).
Track complex coefficients and conjugation consistently; the original
cross-spectrum is a product, not an absolute square. Preserve all strict
cutoffs and partial terminal blocks. Establish bounds in terms of X,
the carrier height, the candidate-box width, and the integration cap.

The known derivative growth suggests scalar comparison cutoffs of order

\[
U_{\rm V}=V_{\rm V}
\asymp \sqrt X(1+|t_0|)^{-1/2}r(X)^{1/14}.
\]

This charges the scalar comparison term, not every remaining error.
The upper product cap is a separate parameter; it must not be confused
with V_V. Verify the full centering and frequency-tail costs before using
this prescription as a uniform reduction.

The desired output is a single complete signed correlation whose bound
implies the detector hypothesis. Separate bounds for prime discrepancy
and Mertens factors are useful controls, but do not constitute new
correlation cancellation. The
[arithmetic closure audit](../programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
shows that coherent zero modes survive the exact arithmetic identity.

## Classical calibration for a moving carrier

Derive a forward bound for lambda_t0(X) from established zero-free regions
and local zero counts, with explicit dependence on t0 and the frequency
width. The improved constants in assessment section 1 concern the original
fixed probe. Applying them with an unspecified t0-dependent constant
does not calibrate a moving family.

Use the exact detector D_t0 to separate a central height band from its
tails. Establish its decay as gamma moves away from t0, then compare the
arithmetic estimate and zero-side lower bound using the same normalization.
If a proposed gain is already a consequence of this classical comparison,
record it as a calibration result.

[Bellotti's asymptotic region](https://arxiv.org/pdf/2306.10680),
[Chourasiya--Simonic's explicit classical density theorem](https://arxiv.org/html/2507.15184v2),
and [Lee--Leong's explicit Mertens estimates](https://arxiv.org/html/2208.06141v5)
provide source inputs. For finite applications, choose an input with
verified constants and starting heights; the asymptotic constant 48.0718
alone is not a numerical certificate.

For eventual curved regions, use
[Broucke's discussion of the Pintz forward and converse theorems](https://arxiv.org/html/2507.13780v1).
The familiar unsmoothed comparison involves the infimum of
eta(t)log X+log t. A prepared detector has a different height attenuation
and needs its own proved converse. Neither its numerical decay constant
nor the raw PNT dictionary can be transplanted without that proof.

## Several probes and local energy

Explore a finite family of nearby carriers or shell moments as an
alternative to a single complex scalar. Possible observables include a
sum of squared moduli or a height-averaged local energy. Such quantities
could make cancellation harder while retaining a positive arithmetic
interpretation.

The missing lemma would be a lower bound for the response of every
admissible zero cluster to the entire probe family, followed by an upper
bound for the complete arithmetic energy. Repeated zeros require the
corresponding multiplicity treatment. Nearly coincident zeros can make
response matrices ill-conditioned, so a separation assumption cannot be
hidden in a minimum-eigenvalue argument.

First test the exact response of formal zero configurations, with their
coefficient weights and cross terms. These tests can reject an attempted
inequality; they do not certify the actual zeta zero set. An ordinary
positive Gram matrix is not automatically a Weil certificate whose
negative index detects off-line zeros.

## The physical wavelength and short intervals

Height modulation makes the natural oscillation length approximately
X/(1+|t0|). This suggests a connection to
[program 04's complete short-interval reconstruction](../programs/04_short_interval_multiscale/PRELIMINARY_INVESTIGATION_20261004.md).
That program supplies exact multiscale covariance and identifies a
coarse response that survives smoothing-error cancellation.

A candidate uniform extension of its sixth-order reconstruction is

\[
\|R_{6,h,t_0}-V_{t_0}\|_{L^2([X,2X])}
\ll_{\rm probe} (1+|t_0|)^6h^6X^{-9/2}.
\]

The implied constant should depend only on the base probe and explicitly
stated input parameters. This extension is **to be
proved**, including the complex kernel, sieve assumptions, and full caps.
For a response-norm budget X^(3/2)r(X), it would require

\[
h\lesssim\frac{X}{1+|t_0|}r(X)^{1/6}.
\]

An easier first step is to redo the second-order transfer uniformly.
Only then determine whether the existing short-interval arithmetic input
operates at the required length. Reconstruction cancels approximation
moments, not a genuine zero mode. An uncentered short-interval variance
hypothesis may already imply a stronger strip; consult the
[dispersion audit](../programs/01_signed_arithmetic_covariance/SHORT_INTERVAL_DISPERSION_GATE_20261004.md).

## Large values and arithmetic amplification

[Program 09](../programs/09_large_values_zero_detection/PRELIMINARY_INVESTIGATION_20261004.md)
audits how a zero detector can interact with
[Guth--Maynard's large-value theorem](https://arxiv.org/pdf/2405.20552v2).
It provides an explicit warning about polynomial lengths, window lengths,
exceptional zero classes, and singleton detection.

For the new family, determine the actual normalized coefficients and the
frequency-window length before testing any large-value bound. Translating
a short window to a high carrier changes coefficient phases; it does not
make the window long. One zero giving one large value is insufficient
when the theorem still allows a positive number of exceptional samples.

Pursue this branch only if a new amplification mechanism forces enough
separated large values of one common polynomial, or if a new regrouping
gives a useful length range with all caps and remainders paid. Ordinary
density improvements alone permit isolated zeros.

## Hardy approximation as an alternative finite certificate

[Program 06](../programs/06_arithmetic_approximation/PRELIMINARY_INVESTIGATION_20261004.md)
has an exact prepared Mellin identity and a full weighted physical norm,
including its small-x tail. Let e_N be its approximation error and
fix 0<b<beta0<1 and T0>=0. Put

\[
\varepsilon_N(b)=\int_0^1|e_N(x)|^2x^{2b-1}\,dx,\qquad
F_N(s)=\frac{1-\zeta(s)P_N(s)}s,\quad P_N(1)=0.
\]

At a zero rho=beta+i gamma with beta>b, Cauchy--Schwarz gives

\[
\varepsilon_N(b)\ge\frac{2(\beta-b)}{|\rho|^2}.
\]

Consequently a rigorously computed finite norm below
2(beta0-b)/(1+T0^2) excludes beta>=beta0 at |gamma|<=T0.
This sufficient finite inequality requires no convergence as N grows.
It has a demanding height cost, and no such improved certificate has
been obtained here.

A shifted target or more general real dilations may support a more local
certificate. The integer-only dictionary is constant on reciprocal
integer bins, so its approximation of a rapidly oscillating shifted
target must be analyzed first. Do not presume that increasing the number
of integer coefficients removes that restriction. The established general
framework is
[Delaunay--Fricain--Mosaki--Robert](https://arxiv.org/abs/1101.1199).

This branch supplies a useful independent control and possible finite
certificate, rather than a substitute for proving an arithmetic saving.
Raw Mobius coefficients may conceal a power-Mertens obligation, and a
finite optimizer does not prove norm convergence.

## Finite certificates and computational support

[Program 10](../programs/10_finite_certificates_support/PRELIMINARY_INVESTIGATION_20261004.md)
provides a small harness that preserves complete cofactor caps, terminal
blocks, prime powers, continuum, and signed cross terms. Its current
records are floating diagnostics, not new outward certificates.

Adapt this machinery after an explicit inequality and error budget are
available. For complex probes, use the correct Hermitian energy where
appropriate without changing signed product identities into absolute
squares. Prove continuous coverage in X and carrier height, as well as
arithmetic, quadrature, remote-frequency, and interpolation errors.

Record a small counterexample to a proposed inequality when one is found.
Successful samples remain diagnostic until all unsampled regions and
tails are enclosed. Large sweeps, exponent fits, and refinement agreement
do not supply those bounds.

## The separate zero proportion branch

The recent
[Alpoge--Furman](https://arxiv.org/abs/2608.13637) and
[Lamzouri](https://arxiv.org/abs/2609.02882) results motivate studying new
valid complex-zero certificates or prime-pair information beyond known
normalized support. Assessment section 6 explains why our product
correlation is a different observable and why signed-window optimization
alone does not improve their existing quadratic functional.

A useful bounded scout would first derive a precise bridge from a new
height-adapted arithmetic observable to their ratio correlation. Without
that bridge, treat this as a separate branch with its own missing estimate.
Improved proportions can coexist with exceptional off-line zeros, so they
do not themselves certify the local boxes sought here.

## Initial deliverables and decision criteria

The next written milestones should be:

1. A detector lemma specifying the box, observable, continuous interval,
   lower threshold, and all zero-side remainders.
2. A uniform arithmetic reduction and classical comparison with a complete
   parameter budget.
3. One precisely stated arithmetic inequality that would improve exclusion
   relative to those classical inputs.
4. A small reproducible diagnostic or a proved certificate for that
   inequality, with its status clearly identified.

Keep detector improvement, classical calibration, new arithmetic
cancellation, and actual zero exclusion as separate claims. Reconsider a
branch when its hypothesis already contains the desired zero-free region,
when its range does not match the required parameters, or when all
purported gain comes from smoothing and the same input zeros.

No specific target height, fixed saving, desired proportion, or numerical
sweep is selected by this research map.
