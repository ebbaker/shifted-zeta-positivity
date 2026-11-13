# What the Green observation measures, and lowering its transverse offset

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Same conversation as child
chat0007. Actual backend model and reasoning effort are unavailable in
recorded configurations.

**Status: explanatory brainstorm and elementary geometry/sign calculations,
checked by the same assistant.** The author proposes lowering the imaginary
observation coordinate and investigating the resulting arithmetic and
renormalization problems. No new canonical arithmetic bound, lower-offset
B10 theorem, uniform shrinking-depth result or manuscript change is claimed.
This follows the [persistence discussion][persistence], but changes the
observation geometry rather than asserting broad persistence of its old signal.

Read the [result index][results], [heat-flow cluster11][cluster], and
[avoid index][avoid], especially [target01][a01], [premise02][a02],
[scope07][a07] and [separate-bounds12][a12]. The classification is a
quantitative diagnostic: explicit changes in the single-zero margin and
the regulator correction are established, while the arithmetic comparison
needed to exploit them remains open. The controls screen is in §7.

## 1. Terminology and the quantity being observed

Adopt the author's terminology correction. Write
\[
 z=X+i b,\qquad T=|X|/2,
 \qquad s=\frac{1-iz}{2}=\frac{1+b}{2}-\frac{iX}{2}.        \tag{1}
\]
Here X is the **longitudinal coordinate**, b the **transverse offset**,
T the **zeta height** at time zero, and lambda the **Newman heat time**.
For an upper zero, y denotes its transverse depth. Thus decreasing b
moves toward the zeta critical line; it does not decrease the zeta height.
At nonzero time the field is the deformed H_lambda, not zeta evaluated
at a new s. Earlier descriptions of b as a "height" meant imaginary
coordinate in the H-plane and should be read with this distinction.

At fixed lambda let \(u(z)=\log|H_\lambda(z)|\). The observation uses
both u at an interior point and its boundary values. Write
\(\mathcal P_B^{(b)}u(X)\) for the harmonic prediction at X+ib from
the boundary values on Im z=0 and Im z=B. Then
\[
 J_{\lambda,B}^{(b)}(X)
    =\mathcal P_B^{(b)}u(X)-u(X+ib).                        \tag{2}
\]
If the field is zero-free throughout the strip and has the requisite
growth, u is harmonic and this discrepancy is zero. Zeros introduce
logarithmic singularities, with
\(\Delta u=2\pi\sum_j m_j\delta_{z_j}\). Poisson–Jensen gives
\[
 J_{\lambda,B}^{(b)}(X)
 =\sum_{0<y_j<B}m_j\,G_B^{(b)}(X-x_j,y_j).                \tag{3}
\]
This is a positive, spatially weighted zero count/potential. It is not
simply the amplitude of H at one point, nor a measurement of zero velocity.
A zero-free multiplicative factor whose logarithm has the valid harmonic
representation cancels from (2). A very small nonzero field value alone
therefore need not imply a large Green discrepancy.

The [manuscript's complete identity][green] is B=8, b=4. For fixed
B=8 and any fixed 0<b<8 away from an actual zero, its product-limit
argument extends directly: the boundary kernels below have exponential
tails, the inherited unit-log bound applies on both unchanged boundaries,
and the paired product converges at the nonzero observation point. An
observation coinciding with an interior zero has J=+infinity, understood
as a limit. Boundary zeros still have integrable logarithms and zero
individual Green contribution. This extension is geometry, not B10's
arithmetic estimate at a new b.

## 2. What nonvanishing buys, and what it does not

The statement used previously was that H_lambda is nonzero **at X+4i**
on the declared time range, because all its zeros satisfy |Im z|<=1.
It was not a statement that H_lambda is zero-free everywhere.

Nonvanishing makes the pointwise logarithm finite and locally harmonic.
For a useful uniform approximation estimate one needs more: a quantitative
modulus floor relative to the error. If
\[
 |F-A|\le\varepsilon,\qquad |A|\ge\mu>\varepsilon,
\]
then the reverse triangle inequality and the derivative of log give
\[
 |\log|F|-\log|A||\le\frac{\varepsilon}{\mu-\varepsilon}.
                                                               \tag{4}
\]
Nonzero by itself supplies no useful uniform mu. Indeed the complete
field decays rapidly with X. The [outer comparison][outer] first divides
by a specified zero-free carrier and then obtains a floor for the
**normalized** field from an absolutely convergent arithmetic comparison.
This gives stable control of the subtracted term in (2). To upper-bound
J one needs a lower bound on that logarithm; an upper estimate alone is
in the wrong direction.
Inside a region where zeros are still possible, such a modulus floor is
an additional estimate to prove, not an assumption available for free.

Closer to a zero, a small absolute approximation error can exceed the
true field value. Better complete-field accuracy can help, but its error
must be compared with the local modulus or a separate small-value argument.
The finite existence of a logarithm is not a substitute for that comparison.

## 3. Lowering b while keeping the strip B=8 fixed

Do not silently replace B by 2b. With \(k=\pi/B\), the existing strip
Green formula at a general observation point is
\[
 G_B^{(b)}(u,y)=\frac12\log
 \frac{\cosh(ku)-\cos(k(b+y))}
      {\cosh(ku)-\cos(k(b-y))}.                            \tag{5}
\]
The two boundary densities are now different:
\[
 P_0^{(b)}(u)=\frac{\sin(kb)}{2B[\cosh(ku)-\cos(kb)]},
 \quad
 P_B^{(b)}(u)=\frac{\sin(kb)}{2B[\cosh(ku)+\cos(kb)]}.      \tag{6}
\]
Their masses are 1-b/B and b/B. At B=8, b=4 these reduce to the two
old copies of K, each of mass one half. Thus a change in b changes the
real-boundary averaging kernel and the outer-boundary payment together.
The old residual mean cannot simply be inserted with unchanged weights.

For an aligned upper zero and b>y,
\[
 G_B^{(b)}(0,y)=
 \log\frac{\sin(\pi(b+y)/(2B))}{\sin(\pi(b-y)/(2B))}.       \tag{7}
\]
This increases as b decreases toward y. It diverges logarithmically
when the observation hits the zero. But sending b all the way to zero
with y fixed makes the signal tend to zero again. "Closer to the real
axis" is therefore not a uniform monotonic improvement for every zero.

For the existing class y in [1/2,1], |u|<=1, and fixed 1<b<=4,
the minimum in (5) is at y=1/2 and |u|=1. To check this, put
\(C=\cosh(ku)\) and
\(q=\sin(kb)\sin(ky)/(C-\cos(kb)\cos(ky))\), so G=atanh(q).
It decreases with |u|, and q_y has the sign of
\(C\cos(ky)-\cos(kb)\), which is nonnegative on this domain.
The resulting illustrative values, evaluated from (5), are:

| Transverse offset b | Single-zero minimum G_8^(b)(1,1/2) | Lower boundary mass |
| --- | --- | --- |
| 4 | 0.182972 | 1/2 |
| 2 | 0.375393 | 3/4 |
| 5/4 | 0.461742 | 27/32 |

These decimals are floating illustrations, not interval certificates.
The exact formulas give the analytical comparison. They are sharper
single-zero margins, not replacements for the named conservative m_*
without restating the consumer. Offset 5/4 remains strictly above every
possible canonical zero in the inherited strip.

There is a separate mass tradeoff. Integrating (5) in u gives
\[
 \int_{\mathbb R}G_B^{(b)}(u,y)du
 =\frac{2\pi}{B}\min(b,y)\,[B-\max(b,y)].                 \tag{8}
\]
One proof integrates the Green equation in the horizontal direction:
the result is the one-dimensional Dirichlet Green function with slope
jump -2pi at b=y. For B=8 and y<=1 the old value is pi*y, while the
maximum over all b is 2*pi*y*(1-y/8), less than 2*pi*y. A much higher
pointwise peak does not create unbounded first spatial mass.

For each fixed b>1 below four, the ratio of (5) to G_8^(4) is bounded
above and below uniformly in u and 0<y<=1. This follows by continuous
extension at y=0 and |u|=infinity, since b is separated from the zero
strip. Hence purely geometric comparison transfers B10's existing rates
with b-dependent constants; it does not itself improve the asymptotic
rate. A new arithmetic estimate at that b is not excluded by this fact.
These mass calculations are for fixed-time zero geometry; they do not
freeze the physical time along a moving observation trajectory for free.

## 4. An offset on the scale of a shallow zero can change the signal scale

There is more than a constant gain if the observation offset is allowed
to shrink with a prescribed target depth. For a single upper zero of
depth d, set b=2d and u=d*v, keeping B=8. As d tends to zero,
\[
 G_8^{(2d)}(dv,d)
 \longrightarrow\frac12\log\frac{v^2+9}{v^2+1}.             \tag{9}
\]
The aligned signal tends to log 3; at horizontal distance d it tends
to (log 5)/2. At the old fixed offset four, the aligned signal is
\(G_8^{(4)}(0,d)=\pi d/8+O(d^3)\). Thus the gain in amplitude is
real, but the useful horizontal width is now of order d.

This also changes the cubic geometry: \(\int G_8^{(4)}(u,d)^3du\)
is comparable to d^3, whereas \(\int G_8^{(2d)}(u,d)^3du\) is
comparable to d for small d. For the latter statement, (9) gives a
positive lower bound on |u|<=d. For the upper bound, the strip Green
function is bounded by the upper-half-plane Green function
\(\tfrac12\log[(u^2+9d^2)/(u^2+d^2)]\); its cubed integral is d
times a finite constant. Domain monotonicity here follows from the
maximum principle applied to the difference, whose singularity cancels.
This is a geometric calculation, not an acquired upper bound for the
new cubic Green observable.

A proof cannot choose b using an unknown zero's exact depth without
paying that choice. A prescribed dyadic test is possible geometrically:
for y in [d,2d], choose b=3d and |u|<=d. The small-d minimum tends to
\(\tfrac12\log(17/5)>0\). Other zeros may still lie on or near this
observation line. Uniform arithmetic and logarithmic control, the
shrinking horizontal window, coverage, and heat-time variation are all
new obligations. The original fixed-offset estimates do not pay them.

## 5. Riemann–Siegel is not restricted to the absolute-convergence region

The complete finite two-arm formula, its reflected terms and its remainder
must be distinguished from the infinite ordinary Dirichlet series.
Failure of absolute convergence of the latter does not invalidate the
former. The [existing manuscript discussion][rs] already makes this
distinction. Polymath's [v2 Theorem 1.3][polymath] explicitly approximates
the evolved field for 0<lambda<=1/2, 0<=b<=1 and X>=200, after division
by a specified nonvanishing normalization. Its displayed approximation
has two finite sums and explicit errors. The fixed-positive-time limit
of the normalized field is separately stated to be nonuniform as time
tends to zero; it cannot be silently applied to lambda=1/L_X.

The outer shortcut at b=4 is particularly convenient because ordinary
absolutely convergent sums bound the normalized field away from zero.
Reducing b does not automatically require a new Riemann–Siegel formula;
it requires retaining whichever terms and cancellation the shortcut had
discarded, with a useful error bound for the actual new consumer.

There is a modest first test before entering the zero strip. At fixed
b=5/4 and c=1, the inherited elementary normalized dominant coefficient
has modulus bounded, up to fixed chart constants, by
\[
 n^{-(1+b)/2}\exp\{[(\log n)^2-L_X\log n]/(4L_X)\}
\le n^{-(1+b)/2-1/8}=n^{-5/4},\qquad
 n\le N_X=\lfloor\sqrt{X/(4\pi)}\rfloor.                  \tag{10}
\]
The inequality uses log n<=L_X/2. Even the old coarser reflected-arm
envelope \(O(X^{(1-b)/4})\) decays at this b, as X^(-1/16).
Thus this first smaller offset is not automatically outside the useful
absolute-summation regime. Rechecking the actual chart, correction,
recentered time, arithmetic floor and changed Poisson weights remains
necessary; (10) is a feasibility calculation, not a completed theorem.

For positive heat time an infinite series with weights
exp(lambda*(log n)^2/4) need not even have terms tending to zero. Its
finite cutoff, reflection and remainder are structural. An unspecified
"renormalization" of the divergent infinite series is not interchangeable
with the complete heat-evolved expression.

## 6. Three distinct ways of treating the logarithm

**Remove a known nonzero carrier.** Set V=H/C where C is explicitly
nonzero and its logarithm has the required harmonic representation.
Then J[V]=J[H]. This removes large smooth amplitude variation while
preserving the zeros and their Green signal. The current carrier and
the published normalized approximation already do this. It does not
remove zeros caused by cancellation between the complete arithmetic arms.

**Regularize small values, retaining the correction.** For a normalized
analytic field V put
\[
 u_\delta=\tfrac12\log(|V|^2+\delta^2),\quad
 D_\delta=u_\delta-\log|V|
 =\tfrac12\log(1+\delta^2/|V|^2)\ge0.
\]
With the same boundary prediction operator, define
\(J_\delta=\mathcal P u_\delta-u_\delta(z)\). Then, away from a
zero at z,
\[
 \boxed{J=J_\delta+D_\delta(z)-\mathcal P D_\delta}.        \tag{11}
\]
This sign matters: simply replacing the subtracted center logarithm by
its regularized value can underestimate the true defect. D_delta(z)
is precisely the dangerous term near a zero. Existing [E04][e04] supplies
a one-sided regularized **boundary** transfer; it is not a uniform
small-value estimate for a new interior observation point.

Direct differentiation also gives
\[
 \Delta u_\delta=
 \frac{2\delta^2|V'|^2}{(|V|^2+\delta^2)^2}.                \tag{12}
\]
Thus regularization smooths the zero charges into a positive density.
This may be useful, but the smoothing/limit error must remain in the
consumer; the atom has not been eliminated from the underlying field.

**Deflate a local zero cluster.** If a complete local factorization is
available, H=P_cluster U, treat log|P_cluster| explicitly and estimate
the regular factor U. Add the known zero contribution back into the
Green identity. The [parent deflation section][deflation] already has
conditional divided-difference and contour-floor tools. Its stated
acquisition bounds are for H_0; a uniform evolving implementation needs
its own parameters. A complete local root count, root uncertainty and
a certified or analytically proved factor floor cannot be omitted.
Under a hypothetical collision these may be studied as quantified
conditional data, rather than assumed favorable. Merely dividing by
an approximate zero polynomial leaves spurious poles; the existing
divided-difference construction was designed to avoid that mistake.

## 7. Controls and a useful continuation question

The detector identities and lower-offset gains are generic geometry.
They also hold for noncanonical fields when the stated strip/product
hypotheses hold. The polynomial heat control in the persistence note
survives these identities. Therefore sharper geometry or regularization
alone cannot certify the canonical exclusion.

For any proposed arithmetic mechanism apply [controls12][controls]:
Euler-factor/translated controls change the complete canonical
coefficients; weighted-square and finite-tail controls lack the full
coefficient/reflection conjunction; finite-prime controls lack full
reflection beyond their fixed data; reflected super-Gaussian and
positive-primitive controls lack the canonical square-series arithmetic;
atomic/finite-profile/compact controls lack the complete theta profile
and its global inputs; RH-conditional endpoint controls fail ordinary
Dirichlet-series arithmetic and retain their conditional premise;
variable-readout controls fail the physical cosine/Newman equation;
relaxed measures lack an actual integer zero configuration; RSCT
calibrations lack the full common-height trajectory and complete Green
window. These are failed **canonical application premises**, not claims
that each derived geometric inequality fails for each control.

The useful next question is whether the increased single-zero margin
outweighs the larger kernel and logarithmic acquisition costs. A bounded
first comparison would keep B=8 and test b=2 and b=5/4 against b=4,
rederiving the boundary kernels, outer baseline and complete residual
payments. A deeper continuation would choose a prescribed target depth d,
take b proportional to d, and prove a signed logarithmic estimate with
all errors uniform in that scale. Deflation or a regulator with (11)
could be part of it. Neither investigation is accomplished by the present
geometry calculation, and no new execution task is issued by this discussion.

Same-assistant checks: the general strip formula reduces exactly to the
old atanh kernel at b=B/2; the two Poisson masses sum to one; (8) reduces
to pi*y at b=4, B=8, y<=1; (9) follows by the small-argument sine/sinh
expansions; the comparison log error (4), regulator sign (11) and density
(12) were differentiated/algebraically checked. The [small calculation
record](../../numerics/20_GNP_RS_LOWER_OFFSET_GEOMETRY_CHECKS_20261113.json)
contains illustrative values, not a theta zero experiment.

Primary-source inspection on 13 November 2026: Polymath v2 (4 August
2019), introduction (5), (11), Theorem 1.3 (13)–(24), and the caveat
after (12). Only these passages were rechecked; this is not a new audit
of the published proof. Existing bibliography and external reading-copy
ownership are retained in the [reference catalog][references].

[persistence]: 10_GNP_RS_PERSISTENCE_SCALE_AND_ZERO_MOTION_20261113.md
[green]: ../../../manuscript/sections/05_green.tex
[outer]: ../../../manuscript/sections/10a_transition_green.tex
[rs]: ../../../manuscript/sections/10_riemann_siegel.tex
[deflation]: ../../../manuscript/sections/09_deflation.tex
[e04]: ../../notes/11_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_20261111.md
[references]: ../../references/README.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
