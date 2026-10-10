# Theta moments exclude two spin families and screen a third

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Numerical and algebraic checks are internal.

This scout of [program 15](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
tests explicit elementary spin realizations before invoking their zero
geometry. The main bounded result is an outward interval enclosure that
rules out two simple finite families at time zero. A coupled ten-spin
fit survives two moments but fails a third in exploratory arithmetic.

## 1. Genuine partition function and time dictionary

Let Phi_e be the even extension of the manuscript's full theta kernel.
Define

\[
Z_t(h)=\int_{\mathbb R}e^{tu^2+hu}\Phi_e(u)du,\qquad
H_t(z)=Z_t(iz)/2.
\tag{1}
\]

Every finite complex t,h derivative converges locally uniformly. Thus
partial_t Z=partial_h^2 Z and partial_t H=-partial_z^2 H. The normalized
probability law is mu_t=e^{tu^2}Phi_e/Z_t(0); its generator is
(u^2-E_tu^2)mu_t. For t>=0 a standard Gaussian G yields
Z_t(h)=E Z_0(h+sqrt(2t)G). These exact identities retain complex readout
cancellation and prove no Lee–Yang property.

The needed external hypothesis is explicit: positive pair couplings and
elementary single-spin Laplace transforms nonvanishing in the appropriate
half-plane. See [Fröhlich–Rodriguez, Theorems 1–2](https://arxiv.org/pdf/1205.6643).
Assigning that single-spin property to the unknown genuine theta measure
at t=0 would assume RH. We instead screen spin laws whose elementary
factors have their own known zero geometry.

## 2. Exact inverse constraints for independent equal spins

For S=a sum_{i=1}^N sigma_i with independent sigma_i=plus/minus 1,

\[
E S^2=Na^2,\quad E S^4=(3N^2-2N)a^4,\quad
\frac{E S^4}{(E S^2)^2}=3-\frac2N.
\tag{2}
\]

Writing genuine even moments m_j=I_j/I_0, the necessary effective spin
count is N_eff=2/(3-m_4/m_2^2). The amplitude is then fixed by
a^2=m_2/N. It is not legitimate to round N_eff to an integer and call
the moments matched.

The independent outward enclosure described below gives

\[
2.79098616 < m_4/m_2^2 < 2.79121956,
\qquad 9.56874<N_{\rm eff}<9.57945.
\tag{3}
\]

There is no integer N in this interval. No independent equal-weight
Rademacher family, finite or a moment-convergent sequence of such families,
can reproduce the theta second and fourth moments at time zero. For a
convergent sequence, either N eventually stabilizes at an integer or
N tends to infinity along a subsequence and its kurtosis tends to three.
This does not exclude unequal amplitudes, interactions, or different
elementary single-spin measures.

A second exact screen concerns two equal spins with ferromagnetic
coupling J>=0. Their S=a(sigma_1+sigma_2) law has mass p/2 at each of
plus/minus 2a and mass 1-p at zero, with
p=(1+tanh J)/2>=1/2. Its kurtosis is 1/p<=2, incompatible with (3).
This rules out that two-spin family for every amplitude and positive coupling.

## 3. Outward theta-moment enclosure

The [checker](../numerics/screen_theta_spins.py) uses the standard library
only. With `--enclose`, it encloses I_0,I_2,I_4 by an independent Decimal
calculation at 42 digits. There are 2,048 dyadic cells in [0,2] and theta
terms n=1,2,3. Each addition, multiplication, division and exponential
is widened by one adjacent representable Decimal value. Decimal's
correctly rounded exponential is enclosed on both sides. The pi interval
comes from exact rational alternating arctangent sums in Machin's formula
pi=16 atan(1/5)-4 atan(1/239), with 70 terms in each sum.

For c=pi n^2, the summand and two derivatives are

\[
\phi_n=(2c^2e^{9u}-3ce^{5u})e^{-ce^{4u}},
\]
\[
\phi_n'=(30c^2e^{9u}-15ce^{5u}-8c^3e^{13u})e^{-ce^{4u}},
\]
\[
\phi_n''=(330c^2e^{9u}-75ce^{5u}-224c^3e^{13u}
+32c^4e^{17u})e^{-ce^{4u}}.
\tag{4}
\]

The midpoint value of f_j=u^j sum_{n<=3}phi_n is enclosed separately
from its second derivative over the whole cell. If the cell length is h,
the integral error is at most h^3 sup|f_j''|/24. All product terms in
f_j'' are included. Summing these enclosures does not rely on a
quadrature refinement estimate.

For the omitted theta terms, n^4<=256*3^{n-4} and
n^2>=16+9(n-4) for n>=4 imply

\[
\sum_{n\ge4}\phi_n(u)
\le C e^{-(64\pi-9)u-128\pi u^2},\qquad
C=\frac{512\pi^2e^{-16\pi}}{1-3e^{-9\pi}}.
\tag{5}
\]

The Gaussian integrals of u^j e^{-128pi u^2} are less than one for
j=0,2,4, so the missing full-line positive moments are each below C.
For u>2, the full-kernel envelope
Phi<=4pi^2 e^{-pi}e^{-(4pi-9)u-8pi u^2} and u^j<=100e^{u^2}
give a remaining moment below 10^{-39}. Both positive omitted contributions
are added to the upper interval endpoint, and the lower endpoint uses
positivity. The [source-bound record](../numerics/theta_spin_screen_record_20261010.json)
contains the complete outward intervals; conservative summaries are

\[
0.01155234249<m_2<0.01155265063,\qquad
0.00037249544<m_4<0.00037250673.
\tag{6}
\]

Equations (3) and (6) are a low-moment certificate for the named families.
They are not a zero certificate or a Lee–Yang proof for theta.

## 4. A ten-spin ferromagnetic fit and its heat evolution

Choose N=10, M=sum sigma_i, and probability weights proportional to
exp(J M^2/2). The constant diagonal contribution can be removed, leaving
pair coupling J between every distinct pair, hence a ferromagnet for J>=0.
For S=aM define exact finite moments

\[
B_r(J)=\frac{\sum_{k=0}^{10}\binom{10}{k}(2k-10)^r
e^{J(2k-10)^2/2}}{\sum_{k=0}^{10}\binom{10}{k}e^{J(2k-10)^2/2}}.
\tag{7}
\]

The inverse equations are B_4/B_2^2=m_4/m_2^2 and a^2=m_2/B_2.
Standard-library Simpson evaluations with 4,096 and 8,192 cells in [0,3],
eight theta terms, and a bracketed finite-model solve produce

\[
J\approx0.00240658580120,\qquad a\approx0.0336197722058.
\]

The model predicts m_6 approximately 1.85735319354*10^{-5}, compared
with the theta evaluation 1.88364670648*10^{-5}, a relative mismatch of
about -0.0139588. These sixth-moment evaluations and the fitted parameters
are floating-point screening evidence, not interval-certified claims.
Agreement between quadrature resolutions does not certify their errors.
The exact two-family exclusions in section 2 use the separate outward
enclosure, not this fit.

The genuine heat deformation of this finite spin family is exactly

\[
Z^{\rm spin}_t(h)=
\frac{\sum_k\binom{10}{k}
e^{(J+2ta^2)(2k-10)^2/2+ha(2k-10)}}
{\sum_k\binom{10}{k}e^{J(2k-10)^2/2}}.
\tag{8}
\]

Thus J(t)=J+2ta^2 and a is fixed. It obeys partial_t Z=partial_h^2 Z.
Refitting a and J independently at each time would generally violate this
dictionary. This finite comparison is a known spin model, not an exact
theta realization. Matching moments at zero field supplies no uniform
complex-field approximation at the candidate heights.

## 5. Scoped conclusion and next bounded task

The elementary equal independent-spin and two-spin ferromagnetic models
are rigorously screened out. A ten-spin coupled model can approximate
the first two moments, but an additional shape parameter is needed even
in the exploratory sixth-moment screen. General spin realizations remain
open. Positivity of moment Hankel matrices does not imply the needed
half-plane nonvanishing.

If this direction is continued, specify an admissible elementary spin
family with enough independent parameters, and enclose the inverse moment
conditions through degree eight while preserving J(t) in (8). Before
claiming any zero consequence, prove uniform convergence in complex fields
and differentiated readouts with the normalizer and quadratic payments of
Note 13. A constructive realization at time zero would have RH-strength
content, so finite fits must remain screening results.
