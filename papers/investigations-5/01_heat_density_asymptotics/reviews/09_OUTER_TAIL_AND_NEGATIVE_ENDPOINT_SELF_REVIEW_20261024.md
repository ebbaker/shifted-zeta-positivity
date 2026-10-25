# Outer tails and negative endpoint: same-assistant analytical review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's metadata. The reviewer is the same
assistant that derived and wrote [Note 25][n25] and [Note 26][n26].
This is not independent specialist review and does not complete HDA-20.
No numerical checks, machine-symbolic execution or interval certificate
were used or claimed. File/link checks are housekeeping, not mathematical
validation.

**Disposition:** retain both notes as proved-in-note results with the
following exact scopes. HDA-19 becomes partial: the time-only-regulator
outer tail is controlled, and a particular compact-source potential
comparison is excluded after the spatial switch. HDA-16 becomes partial:
the negative endpoint now has all-height evolution and actual covariance
budgets; its positive part remains unfinished. HDA-17 has no newly
accepted representation and HDA-18 remains gated.

## 1. Complete-source contour and observable bounds

I rederived the Fourier normalization as one half of the full-line
transform. After the contour shift, reflection supplies two equal
half-line upper bounds and cancels that half. The field exponent is
`exp(-a|x|)`, not a bound on the density itself. The source series is
normally convergent in `|Im u|<pi/8`; fixing `a<=pi/16` gives the positive
cosine factor and a geometric mode envelope. Even reflection, analytically
continued from the real axis, is essential for the negative half-line.
The vertical ends vanish with a superexponential bound; there is no
unpaid endpoint at zero or a finite source cutoff.

OH2 retains `exp(-t_a a^2)` and uses `s=max(t_b,0)` for the real source
coordinate. Its elementary tail split is conservative but finite for
any compact time interval. The derivative weights `(v+a)^j` majorize
`|v+ia|^j`; all fixed jet orders can be treated before observable
comparison. No asymptotic remainder was differentiated.

For the observables, the regulator floor is used only on slabs ending
at 64. The full horizontal filter width changes the exponent to
`E=exp(-a max(|x|-ell,0))`; the full transverse width enters OH2.
Products of field jets give `E^2` for density/current and `E^4` for the
squared potential gradients in covariance. The Laplacian covariance
constant comes from `2L_2+4(L_2+L_x^2+L_y^2)`. Actual covariance is kept;
it has not been inferred from the potential equation. The time-derivative
formula retains the regulator term and both physical field terms.

The zero-field background is a valid algebraic regulated model on these
slabs. Its density is zero and its potential is `log q`. No holomorphic
zero measure is attributed to the identically zero field. The tail theorem
therefore says nothing about the number of canonical zeros. The explicit
height threshold may be large; no numerical size or finite onset was
estimated. It is nevertheless an error bound holding beyond that threshold
to infinity, with arbitrary prescribed absolute tolerance.

## 2. The cutoff obstruction and what it does not establish

For the finite field, the first integration by parts contributes
`g(U_s) sin(U_s z)/z`; continuity of `g` cancels interior terms at that
stage. The second integration is cellwise and pays every jump in `g'`,
both end derivatives and the remaining `g''` integrals. Omitting these
terms would invalidate the comparison. Positive endpoint source values
give `g(U_s)>0` at every fixed finite time.

The lower bound uses a buffered region with distance `d_y>0` from the
real axis, where `|sin(U_s z)|>=sinh(U_s d_y)`. It is not a real-axis
lower bound. The true potential only needs the complete-field upper
bound; no unsupported theta lower estimate enters. At each fixed
`t>64`, `q=E_0^2 exp(-beta x^2)` is eventually below the contour
exponential. Thus OH17 compares a logarithmically decaying finite-field
potential with a true potential bounded above by a negative linear
function of height. Its lower bound diverges for all sufficiently large
heights, after the complete averaging buffer is paid.

The exclusion concerns source-anchored averaged potential for finite
piecewise-linear sources with nonzero positive endpoint and the given
Gaussian-in-height regulator, on the stated off-axis observations. It
is not a density-only exclusion, does not assert a statement at `y=0`,
and does not cover smooth zero-endpoint tapers, moving cutoffs or other
noncompact representations. It is stronger than failure of a numerical
error allowance, but far narrower than impossibility of an adaptive
outer approximation. In particular, exact heat evolution of the finite
field does not repair the demonstrated source-tail mismatch.

## 3. Negative endpoint and covariance cancellation

The same source Taylor estimate was integrated with jet weights through
order four. With the exact common `epsilon_b(-T)`, the dimensionless
bounds are `u_j=O(T^(-j/2))`, `v_j=O(T^(-j/2-1))`. The time-only
normalization is used only to bound rational maps at one time. The
observable time derivatives are derived from the physical heat equation,
so no derivative of the normalizer is lost. In particular
`r_t=T/(1+T^2)>0` because the heat variable is `t=-T`.

The Gaussian satisfies that same backward heat equation, and direct
multiplication of `G_zz` with `conjugate(G_z)` gives both terms and the
sign in NE4's current. The direct budgets have errors `T^-2` for density,
`T^-5/2` for current, and `T^-3` for the density time derivative.
Potential and potential-time errors have orders `T^-1` and `T^-2`.

For the real derivative tensors, NE15 counts partitions with singleton
and pair blocks. Dividing every derivative block of `1+|a|^2` by that
quantity bounds its first derivative by one and second derivative by two.
The log-composition coefficient is `(k-1)!`; the reciprocal coefficient
is `k!`. This verifies the stated tensor constants and the differentiated
forcing bound. Holomorphy converts each spatial directional jet to the
corresponding complex derivative without dimension-dependent component
losses. Telescoping the composition products pays the field argument and
every derivative factor. Fourth potential derivatives require field jets
through order four and the fifth derivative bound for the scalar map;
these are both supplied.

The two-point covariance identity pays the kernel variance, not the sum
of two unrelated squared-gradient bounds. On the convex buffer it gives
NE21 with coefficient four. Differentiating the actual covariance first
gives NE22. The two spatial directions and two signed components give
coefficients 16 and 8 in NE23. This uses third and fourth potential
derivative errors, not a derivative of an existing static allowance.
It yields `O(T^-3)` for `Q-Q_G` and `O(T^-4)` for its Laplacian,
respectively one power smaller than their upper physical scales.

The physical averaging widths are fixed. The transverse scale specifies
where the supremum is taken; partial-time derivatives remain at fixed
physical coordinates. All convolution points and straight segments
between them fit in NE1's declared buffer. No moving-filter commutator
or moving-domain flux statement is being silently used.

## 4. Controls, external input and continuation

The notes identify the failed premises for atomic/polynomial,
Euler-factor, weighted-square/finite-prime, reflected and primitive
controls. The generic analytic estimates are compatible with smooth
colliding sources with their own constants. There is no simplicity
claim. The negative Gaussian result does not provide regulator removal
or a zero-count approximation.

Polymath's version-pinned paper was consulted as an outer-representation
lead. The inspected Theorem 1.5 is for `0<t<=1/2`; it was not imported
into the `t>64` adaptive regime. Its recorded comments about other bounded
parameters are not a substitute for doing that extension. The new proofs
use the canonical source and elementary estimates and do not depend on
an unverified high-height theorem. Existing PDF provenance is linked
from the reference catalog; no new download or numerical run was needed.

There is no proved spatial overlap between a new adaptive exterior and
the positive inner clock, since such an exterior has not yet been
constructed. The next analytical step is a noncompact outer pair with
paid relative holomorphic error and weak regulator transfer on a compact
slab above 64. No Sol packet is issued before a numerical question is
identified. The maintained manuscript's existing build remains the
Note 23 integration; these results are recorded in research notes and
status pointers pending its next substantive revision.

[n25]: ../notes/25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[n26]: ../notes/26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
