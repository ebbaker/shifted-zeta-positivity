# Gap chains, the dipole response and a local analytic factor

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual recorded model and effort unavailable;
none is inferred. Status: **explanatory discussion and manuscript emphasis
clarification, with same-assistant algebra and production checking**.
No new theorem, source certificate, quantitative improvement or research
task disposition is claimed.

Edward accepts integer p,q as the natural hierarchy variables, asks that
this be foregrounded, and interprets the gaps as a chain whose cumulative
lengths determine M. He suggests a dipole interpretation and asks how an
analytic nonvanishing factor can be invisible to a fixed-time pair
readout but influence subsequent motion. This note develops those points,
following [Discussion07][previous].

The [result index][results] and [avoid index][avoid] remain the routing
sources; relevant entries are [Cluster18][cluster],
[Controls12][controls], [classification01][classification],
[premises02][premises] and [scope07][scope]. The chain formula and field
identities below are already in the manuscript. Their interpretation and
elementary examples are identities, not a new collision-prevention
criterion or an improvement to an existing estimate.

## Integer p,q as the main hierarchy coordinates

The author's requested emphasis is now explicit in the manuscript
abstract and [§1 introduction][framework]. The nonnegative integer
exponents attach separately to the poles \(c\pm\sqrt D\). Rational
partial fractions and finite divided-difference identities make this
the natural setting for the proved recurrence. Its equivalent even/odd
S/T coordinates are regular through mergers.

The later complex-power construction extends the exponent of the
combined quadratic denominator. It is not a proved hierarchy with two
independently complex split-pole indices. This is an editorial
clarification of the existing statements; the title, theorems and
scientific task statuses are unchanged. The build and selected-page
inspection are recorded [here][build].

## The chain formula already established in §4

On an interval where the complete divisor is real and simple, write its
ordered zeros as \(x_n\), and put
\[
 g_n=x_{n+1}-x_n,\qquad
 L_{n,m}=\sum_{j=1}^{m}g_{n-j},\qquad
 R_{n,m}=\sum_{j=1}^{m}g_{n+j}.
\]
Thus L is the distance from the left target to the m-th exterior zero
on its left; R is the analogous distance from the right target.
The [all-gap proposition in §4][lattice] states exactly
\[
 M_n=\sum_{m\ge1}
 \left[
 \frac1{L_{n,m}(L_{n,m}+g_n)}
 +\frac1{R_{n,m}(R_{n,m}+g_n)}
 \right],
 \qquad
 g_n'=\frac4{g_n}-2g_nM_n.
\]
Each exterior distance is a sum of consecutive gaps. An individual gap
therefore enters many other rows. The chain describes relative motion
and does not need the absolute translation coordinate.

These assertions use the complete real ordered divisor. If only a
finite real block is known, its terms can be written this way, but the
remaining exterior must be retained, including any nonreal zeros.
Positive real-gap denominators cannot be assigned to that unknown
exterior. The manuscript explicitly makes this distinction.

The uniform chain gives a helpful exact normalization check. If every
gap is g, then L=R=mg, so
\[
 M=\frac2{g^2}\sum_{m\ge1}\frac1{m(m+1)}
   =\frac2{g^2},\qquad g'=0.
\]
This is the stationary cosine control already used in §4. Its mutual
pair repulsion and complete exterior compression balance. It is not a
canonical theta model or a claim that general chains remain uniform.

**19 November clarification of emphasis:** the author correctly requested
the logarithmic height dependence even in the basic picture. The uniform
example above is only a normalization control.
[Discussion09](09_VCD_GT_CM_HEIGHT_DENSITY_AND_GAP_FLUCTUATIONS_20261119.md)
foregrounds the manuscript's actual height-dependent clock, local gap
fluctuations and complete tail, with a canonical certificate readout.

## The dipole and higher-order interpretation

Let a and b=a+g be the target zeros and let rho be exterior. The exact
identity
\[
 \frac1{(\rho-b)(\rho-a)}
 =\frac1g\left[\frac1{\rho-b}-\frac1{\rho-a}\right]
\]
identifies one contribution to M as the difference of two reciprocal
distance fields, divided by the target separation. At distance
\(w=\rho-(a+b)/2\), the difference is
\[
 \frac{g}{w^2-g^2/4}
 =\frac{g}{w^2}\left(1+O(g^2/w^2)\right)
 \quad\text{as }|w|/g\longrightarrow\infty.
\]
Thus the dipole analogy is precise for this reciprocal-distance
kernel: taking the difference removes the leading common response.
M is the complete sum of these responses per unit separation, not
an average normalized by the number of exterior zeros. Combine the
two first-power terms before summing; the difference is absolutely
summable under the manuscript's hypotheses even when the two
first-power sums separately are not.

For the diagonal moments \(S_r=\sum_\rho(w_\rho^2-D)^{-r}\),
a distant term has magnitude of order \(|w|^{-2r}\).
Increasing r strengthens the relative weight of small denominators.
For two real exterior denominators \(Q_1<Q_2\), the ratio of their
contributions is \((Q_2/Q_1)^r\). This compares terms within an order;
it does not compare dimensionful values of different moments directly.
Increasing p in P_{p,q} emphasizes proximity to b; increasing q
emphasizes proximity to a. Off-diagonal and odd moments can have
signs, and nonreal contributions can have phases, so magnitude
concentration alone is not positivity of the complete moment.

A useful equivalent formulation already in §4 removes the target poles
from the common logarithmic derivative:
\[
 R(z)=\frac{H_z(z)}{H(z)}-\frac1{z-a}-\frac1{z-b},
 \qquad
 M=-\frac{R(b)-R(a)}{g}
   =-\frac1g\int_a^b R'(x)\,dx.
\]
Here R is analytic near the closed target segment; the integral is
along that segment. The last equality is the fundamental theorem of
calculus. M measures the spatial variation of the exterior field
across the pair. A common exterior velocity cancels from the gap.

This sharpens the earlier preference for estimating the gap observable:
one may estimate a compatible portion of the gap chain and its
complete exterior, retaining correlations among all cumulative
distances. D_n is then a readout of that common state. The proposal
never requires treating one gap as an independent dynamical system.
Whether a particular chain estimate improves a complete budget remains
an open quantitative question, not a consequence of the rewriting.

## Why the local factor matters to motion

At a fixed time factor
\[
 H(z)=Q(z)A(z),\qquad Q(z)=(z-a)(z-b),
\]
with A analytic and nonzero throughout the counted disk. Then
\[
 \frac{H_z}{H}=\frac1{z-a}+\frac1{z-b}+\frac{A_z}{A}.
\]
The last term is analytic inside the contour. For each nonnegative
integer k its polynomial-weighted integral
\(\oint z^k(A_z/A)\,dz\) is zero. Hence the pair power sums, center
and D read out the zeros of Q alone.

This does not say that A_z/A is zero. A nonconstant analytic factor
is invisible to these particular contour integrals, rather than
cancelling pointwise from H_z/H. Rational weights with poles at the
targets can detect it; these are precisely the weights used for the
exterior moments.

Motion uses the heat equation \(H_t=-H_{zz}\). At a simple zero x(t),
differentiating H(t,x(t))=0 gives
\[
 x'=\frac{H_{zz}}{H_z}\bigg|_x
    =\frac{Q_{zz}}{Q_z}\bigg|_x+2\frac{A_z}{A}\bigg|_x.
\]
The product rule
\[
 (QA)_{zz}=Q_{zz}A+2Q_zA_z+QA_{zz}
\]
shows the source of the second term. Q does not in general evolve by
the heat equation on its own. With \(R=A_z/A\), the two velocities give
\[
 g'=\frac4g+2[R(b)-R(a)]=\frac4g-2gM.
\]
Only the difference of the exterior velocities affects the gap. A
constant R would move both roots equally at that instant. A constant
nonzero scalar A has R=0 and, by linearity of the heat equation,
never changes the zero motion at all.

For a direct finite example, compare initial fields
\[
 Q(0,z)=z^2-1,\qquad
 H(0,z)=(z^2-1)(z^2-25).
\]
On the circle |z|=2 both enclose exactly the same pair, -1 and 1;
the additional factor is nonzero on and inside that circle.
Their initial D is 1. Evolving each full field by the same heat
equation gives
\[
 D_Q'(0)=2,\qquad
 M_H(0)=\frac2{25-1}=\frac1{12},\qquad
 D_H'(0)=2-\frac4{12}=\frac53.
\]
The pair has the same current positions and different velocities.
The local analytic factor retains the influence of exterior zeros.
The [exact arithmetic record][checks] checks this example directly
from polynomial derivatives as well as the gap law.

## Scope and collision screen

The complete [Discussion06 premise screen][screen] remains applicable.
For the identities used here:

- Quadratic and strong-collar quartic heat controls satisfy the generic
  local algebra and can reach a double event. They fail literal theta
  source identity, not the pair-velocity law. The quadratic
  \(H(t,z)=z^2-2(t-T)\) gives D=2(t-T), M=0 and D'=2,
  including at D=0. No positive margin follows merely from the identity.
- The Euler-factor controls have a locally nonvanishing multiplier
  at real zeros at the initial slice. Their full normalized theta
  source identity fails, and their extra nonreal divisor cannot be
  discarded when computing future motion.
- The weighted-square and finite-source perturbations in Controls12
  do not provide a complete all-real divisor; the documented subclasses
  have nonreal zeros at every real time. Their real zeros therefore
  cannot supply the complete positive gap-chain representation.
  The local analytic factor and complex exterior identities still apply.
- The remaining reflected, shape, finite-prime, kernel and relaxed-state
  controls retain the exact failed premises listed in Discussion06;
  nothing here upgrades finite data, source shape or a static divisor
  into the unchanged complete canonical heat path.

This is an analytical premise screen and a finite algebra check, not
a replay of the external controls' certificates. It does not exclude
chain-based estimates or localization. It records why these identities
alone do not exclude the controls.

[previous]: 07_VCD_GT_CM_SPLIT_POLES_OBSERVABLES_AND_LOCALIZATION_20261118.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[framework]: ../../manuscript/sections/01_framework.tex
[lattice]: ../../manuscript/sections/14_coupled_lattice.tex
[screen]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
[checks]: ../numerics/02_GAP_CHAIN_FACTOR_EXACT_CHECKS_20261118.json
[build]: ../numerics/03_INTEGER_PQ_EDITORIAL_BUILD_20261118.json
