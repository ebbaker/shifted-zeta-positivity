# Height adapted zero detection and nonuniform zero free regions

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: investigation opened; detector lemmas and fixed-probe reductions
are available, but no new zero-free region or uniform arithmetic bound is
proved. Internal same-model analysis is not independent specialist review.

This investigation asks whether the signed arithmetic covariance work can
yield a height-dependent or finite-window zero-free result. Its immediate
purpose is to establish the quantitative link between a prepared prime sum
and the exclusion of a zero in a stated box, before choosing target heights
or decay constants.

The main technical starting point is the
[research assessment](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md).
It remains in its original folder as the record of the deductions that
motivated this investigation. This overview summarizes those results and
identifies the missing theorems. The
[research directions](RESEARCH_DIRECTIONS_20261004.md) describe the main
approaches, related programs, primary sources, and stopping criteria.
The opening [detector lemmas](DETECTOR_LEMMAS_20261004.md) give uniform
decay away from the carrier and a lower bound on a whole unit-height box.

The [Gaussian localization investigation](gaussian_localization/README.md)
now develops exact pole subtraction, a uniform weighted inverse-kernel
norm, and a conditional finite-box detector with linked Gaussian parameters.
The [explicit-constants continuation](gaussian_localization/EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md)
now evaluates the inverse, physical-tail, pole, and zero-count constants,
giving the smaller log-prime-scale cover [24(N+1),208N] and an explicit
sufficient arithmetic inequality. The
[finite Gaussian Möbius reduction](gaussian_localization/FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md)
now removes small divisors and caps the product sum at an effective error,
giving a narrower signed arithmetic target. The
[height-uniform Vaughan comparison](gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
provides explicit derivative and cutoff costs for the original scalar
route. Both retained cancellation inequalities remain open.

## Aim and scope

The intended outcome is an unconditional inequality for a complete prepared
arithmetic observable, with a quantitative converse that gives a zero-free
box or a height-dependent region. The converse must specify a continuous
prime-scale interval and numerical error allowances; a few small values of
the observable do not suffice.

The motivating question is narrower than a fixed positive global power
saving. The existing fixed-power scalar criterion implies a fixed strip
for all zeta zeros, whereas a new nonuniform region could improve exclusion
only on selected height ranges or by a shrinking amount.

A result counts as new zero exclusion only if it goes beyond what the
known zero-free regions or verified zeros used in its proof already imply.
A sharper smoothed bound obtained from those same inputs is a useful
calibration theorem, with a different claim.

## Current understanding

The [assessment, section 1](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md)
derives a stronger classical baseline for the original fixed probe.
Let

\[
F(X)=\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}}.
\]

Existing asymptotic Korobov--Vinogradov and classical density inputs give
every constant below 0.4352925886 for the normalized response envelope,
below 0.4629776100 for the scalar envelope, and below 0.8705851772 for the
variance envelope:

\[
|V_g(X)|\ll X e^{-cF(X)},\quad
|\lambda_V(X)|\ll e^{-dF(X)},\quad
\mathcal V_g(X)\ll X^3e^{-2cF(X)}.
\]

Here c and d must be strictly below their respective thresholds. The
constants and starting ranges have not been made numerical. This improves
the manuscript's asymptotic comparison, not the input zero-free region.
It is a fixed-probe theorem; its constants cannot be assumed uniform in
a growing modulation parameter.

The [assessment, section 2](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md)
also proves that the fixed-probe arithmetic reduction accepts a general
subpower envelope r(X)=exp[-Phi(log X)], with Phi tending to infinity and
Phi=o(log X). Suitable cutoffs give

\[
\lambda_V(X)=\mathcal C_\Omega(X)+O_g(r(X)),\qquad
\mathcal I_{\rm retained}(X)=-q\mathcal C_\Omega(X)+O_g(r(X)).
\]

This preserves the full signed integral, continuum, product caps, prime
powers, and spectral tail. It transfers an envelope between arithmetic
forms. It is not a curved-region converse, an energy estimate from a scalar
estimate, or a height-uniform theorem for the new probe family.

Finally, [assessment sections 4 and 5](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md)
quantify the detector and construct a family adapted to height. The fixed
detector has coefficient of order |gamma|^(-7) on closed right substrips.
The new family removes that attenuation at its central height.

## The prepared family

Retain the polynomial h(v)=(1-16v^2)^8 on |v|<1/4, extended by zero.
Write H(z)=integral h(v)e^(zv)dv. For a real carrier height t0, set

\[
h_{t_0}(v)=e^{it_0v}h(v),\quad
N_{t_0}=\|-h_{t_0}'''+\tfrac14h_{t_0}'\|_2,\quad
g_{t_0}=(-h_{t_0}'''+\tfrac14h_{t_0}')/N_{t_0}.
\]

Then

\[
G_{t_0}(z)=\frac{z(z^2-1/4)H(z+it_0)}{N_{t_0}},\qquad
w_{t_0}(u)=u^{-1/2}g_{t_0}(-\log u).
\]

Define the prime response and matching shell scalar by

\[
V_{t_0}(x)=\sum_n\Lambda(n)w_{t_0}(n/x),\qquad
\lambda_{t_0}(X)=\frac1{qX^{3-it_0}}
\int_X^{2X}x^{1-it_0}V_{t_0}(x)\,dx,\quad q=7/3.
\]

The zero coefficient is

\[
D_{t_0}(s)=\frac{G_{t_0}(1/2-s)}q
\frac{2^{s+2-it_0}-1}{s+2-it_0}.
\]

Preparation still removes the pole at one. The exact normalization is
given in assessment equation (17), and its rational proof yields

\[
|D_{t_0}(\beta+it_0)|>0.36
\quad(3/4\le\beta\le1,\ |t_0|\ge100).
\]

This is a coefficient lower bound, not a lower bound for the sum over all
zeros. Other zeros can interfere. The observable is complex, so a modulus
bound or a justified pair of real observables is needed.

The opening detector note strengthens this to
|D_t0(beta+i gamma)|>1/4 when 3/4<=beta<=1,
|gamma-t0|<=1 and |t0|>=100, with an exact proof. It also gives a uniform
upper envelope in the distance from the carrier. These are local
coefficient lemmas; no zero box is excluded by them alone.

The cost is explicit growth in derivative bounds:

\[
\|D^6w_{t_0}\|_{\rm TV}\ll(1+|t_0|)^6,\qquad
\|D^7\ell_{t_0}\|_{\rm TV}\ll(1+|t_0|)^7,
\quad
\ell_{t_0}(u)=\int_1^2y^{1-it_0}w_{t_0}(u/y)\,dy.
\]

The continuum also survives. With K(s)=(2^(s+2)-1)/(s+2),

\[
c_{t_0}=-\frac{H(-1/2+it_0)}{2N_{t_0}}\ne0,\qquad
\int\ell_{t_0}(u)\log u\,du=c_{t_0}K(1-it_0).
\]

All cutoff and centering formulas must use this coefficient. Extending
every fixed-probe arithmetic reduction uniformly to this family remains
work to do.

## The missing implication

The central proposed deliverable is a theorem of the following form.
For a candidate box

\[
\mathcal B(b,t_0,\Delta)=
\{\beta+i\gamma:b\le\beta\le1,\ |\gamma-t_0|\le\Delta\},
\]

the existence of a zero in the box should force a quantitative lower
bound for a prepared observable somewhere in a computable interval
J of log X. For example, a possible formulation to investigate is

\[
\sup_{y\in J}e^{(1-b)y}
|\lambda_{t_0}(e^y)|\ge
A(b,t_0,\Delta,J)-E_{\rm remote}.
\]

This is a target shape, not a theorem. The observable, interval, lower
constant, and remote-zero allowance must be justified together. A cluster
may require several carriers, extra moments, or a power-sum argument.
Multiplicity and the finite initial cap must be retained.
If an exposed-zero argument changes the height, the theorem must also
specify a covered guard interval; a narrow band cannot silently inherit
a replacement zero outside it.

A new independent arithmetic bound smaller than this lower threshold
throughout J would then exclude the box. Without the detection theorem,
an order-one central coefficient alone supplies no certificate.

The existing one-sided Landau proof concerns a real scalar and a fixed
power envelope. It gives neither this finite detection interval nor a
nonuniform converse for the complex family. An eventual subpower estimate
with an unspecified threshold cannot exclude an individual fixed zero,
whose contribution is itself eventually power-small.

## Parameters and sequencing

Keep distinct the prime scale X, carrier height t0, candidate-box width
Delta, arithmetic factor length, and integration-frequency cap Omega.
Moving a short frequency window to a large carrier height does not enlarge
the window or create additional separated samples.

The recommended order is:

1. Prove a quantitative box-detection lemma and a parameter-dependent
   classical comparison for the new family.
2. Extend the full arithmetic reduction with uniform derivative,
   continuum, endpoint, and tail budgets.
3. Formulate the exact signed arithmetic inequality on the interval
   required by the detector.
4. Use small diagnostics to reject false inequalities, then seek rigorous
   continuous-parameter bounds.
5. Select target heights or regional improvements only after the first
   three steps determine the resource budget.

This ordering is a research judgment, not evidence that a new region is
already attainable. Near-term results may be detector or transfer lemmas
of independent interest; their broader novelty needs a literature audit.

## Relationship to the earlier programs

The signed product covariance in
[program 01](../programs/01_signed_arithmetic_covariance/README.md) remains
the arithmetic foundation. It is not automatically the prime-pair ratio
correlation used in the recent 67.25 percent results. Their asymptotic
proportions tolerate finite exceptions. A bridge to those results would
need a new observable and transfer theorem; see assessment section 6.

The useful neighboring branches are
[large values and single-zero detection](../programs/09_large_values_zero_detection/PRELIMINARY_INVESTIGATION_20261004.md),
[short-interval reconstruction](../programs/04_short_interval_multiscale/PRELIMINARY_INVESTIGATION_20261004.md),
[arithmetic approximation](../programs/06_arithmetic_approximation/PRELIMINARY_INVESTIGATION_20261004.md),
and [finite certificate support](../programs/10_finite_certificates_support/PRELIMINARY_INVESTIGATION_20261004.md).
Their roles and limitations are described in the companion directions note.

## Records and claims

Save dated research notes in this folder. Place future numerical sources
and small records under the prime-variance project's
numerics/height_adapted_zero_detection folder, and reviews under
reviews/height_adapted_zero_detection. Create those folders when there is
work to save. Follow the repository's [large-file policy](../../../../LARGE_FILES.md);
cite third-party papers rather than copying their PDFs.

Label each statement as a proved project deduction, an application of an
existing theorem, a conditional estimate, or a proposed investigation.
Record all hypothesis and parameter ranges. Floating diagnostics are not
outward certificates; a finite certificate must include every unsampled
tail and continuous-parameter error.
