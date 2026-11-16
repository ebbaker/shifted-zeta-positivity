# Which estimates could control unresolved collisions?

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0004. Actual model and
reasoning effort are unavailable in the recorded configuration.

**Status: route discussion with conditional local calculations;
same-assistant checking only.** No new overview or research plan is
activated. B07 remains unactivated and E25 unissued. No canonical
collision exclusion, numerical campaign, or specialist review is claimed.

Read the [result index](../../../../result-summaries/README.md), especially
[controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
[local geometry13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [approximation18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md);
also the [avoid index](../../../../avoid/README.md), specifically
[01: target reformulations](../../../../avoid/01_restating_the_target.md),
[02: control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07: scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12: signed aggregate estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [15: sibling results](../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## 1. What refinement establishes, and what is still needed

Use the fixed, conjugation-symmetric two-zero cluster of manuscript
§10.4, equations (10.13)–(10.17), as discussed in
[note27](27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md).
Its symmetric coordinates are

\[
c=(z_1+z_2)/2,\qquad D=((z_1-z_2)/2)^2,\qquad
|D_N-D|\le d_N\longrightarrow0.
\tag{1}
\]

Positive D means two distinct real zeros; negative D means a nonreal
conjugate pair. A double zero has D=0. At a fixed real double event T,
the exact heat equation gives D'(T)=2. Thus a genuine collision already
has a shrinking unresolved time window of size O(d_N). Refinement
locates that collision; it does not remove it. Similarly, convergence
of an individual zero does not establish that its limit is real.

The following three routes distinguish an actual useful extra estimate
from the existing approximation theorem. Route A has the strongest
existing analytical foundation. Route B most directly addresses degree
induction. Route C specifies the strength an averaged estimate would
need. These are conditional interfaces, not three new theta theorems.

## 2. Route A: transport a positive separation through heat time

On an isolated two-zero tube factor the actual field as

\[
F_\lambda(z)=((z-c(\lambda))^2-D(\lambda))A_\lambda(z),
\qquad h_\lambda=A_{\lambda,z}/A_\lambda,
\tag{2}
\]

where A is holomorphic and nonzero on the spatial neighborhood. The
factorization remains regular at the double event. Put

\[
K(\lambda)=
\frac{h_\lambda(c+\sqrt D)-h_\lambda(c-\sqrt D)}{2\sqrt D},
\qquad K\big|_{D=0}=h_{\lambda,z}(c).
\tag{3}
\]

This is a divided difference: it measures the variation of the drift
contributed by the remaining factor, rather than the common motion of
the pair. It is real on real heat time and extends analytically through
D=0. No global all-real-zero assumption is used.

The normalized heat equation is F_lambda=-F_zz-m2 F. At a simple root r,
differentiating F_lambda(r(lambda))=0 gives r'=F_zz(r)/F_z(r).
Writing r_±=c±s, s²=D, in (2) therefore gives

\[
r_\pm'=\pm\frac1s+2h_\lambda(r_\pm),\qquad
\boxed{D'=2+4KD.}
\tag{4}
\]

Indeed D'=s(r_+'-r_-'). Analytic continuation supplies the identity
at D=0. This extends the existing local factor/force identity in
[Rodgers–Tao branch note02, §3](../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
to the regular squared-separation coordinate. It is not a new general
zero-dynamics theorem. For literature background,
[Rodgers–Tao, arXiv:1801.05914v5, §4, (56)](https://arxiv.org/html/1801.05914v5#S4)
gives the principal-value root interaction law in its stated simple
all-real regime Lambda<t<=0. That regime is not assumed across a
hypothetical event here.

Fix times u<v in the tube and define the positive integrating factor

\[
W(t)=\exp\!\left(4\int_t^v K(s)\,ds\right).
\]

Since (WD)'=2W, exact integration yields

\[
W(u)D(u)=D(v)-2\int_u^v W(t)\,dt.
\tag{5}
\]

Consequently, a lower bound L_v<=D(v) and an upper bound
B>=2 integral_u^v W with **L_v>B** prove D(t)>0 for every t in [u,v].
The same comparison with equality allowed proves D(u)>=0 and
D(t)>0 for u<t<=v. Thus an endpoint double zero need not be excluded
when the objective is reality at that endpoint.

For example, if K<=M throughout the tube, the sufficient cost is

\[
B_M(\Delta)=
\begin{cases}
(e^{4M\Delta}-1)/(2M),&M\ne0,\\
2\Delta,&M=0,
\end{cases}
\qquad \Delta=v-u.
\tag{6}
\]

This formula is valid also for negative M. An upper bound for the signed
integrals of K in (5) can be much better than replacing K by |K|.
Bounded K alone does not prevent collision: the exact quadratic heat
field (z-a)²-2(lambda-T) has K=0 and D(v)=2(v-T). Its gap budget
reaches zero exactly at u=T and fails for u<T.

**The missing source estimate.** One needs a quantitative relation
between the incoming gap and the complete exterior drift that makes
(5) positive on a specified interval. A sequence of permissible tiny
steps is insufficient if their total length stops at an unknown
positive time. An induction must control the accumulated cost or prove
that the time steps cover the desired interval.

Potential useful information includes a relation between the pair gap
and the variation of the exterior drift, or a bound on its signed time
integral derived from the complete canonical source. Separate estimates
for gap size and exterior magnitude can miss that relation. Approximate
equal spacing illustrates the cancellation one might try to quantify,
but a uniform equally spaced model is not assumed for the actual zeros.

### Why the cluster formulation could help acquire that input

Let Gamma be the fixed enclosing contour. Its Cauchy projection gives

\[
h_\lambda(z)=\frac1{2\pi i}\oint_\Gamma
 \frac{F_{\lambda,z}(\zeta)/F_\lambda(\zeta)}{\zeta-z}\,d\zeta,
\qquad
K=\frac1{2\pi i}\oint_\Gamma
 \frac{F_{\lambda,z}(\zeta)/F_\lambda(\zeta)}{(\zeta-c)^2-D}\,d\zeta.
\tag{7}
\]

The first formula follows by subtracting the interior zero residues
from F_z/F; taking its divided difference gives the second. Both remain
regular when the internal pair merges. An outer contour margin and
buffer are still essential.

More explicitly, remove the two interior zeros from G_N as well and
write h_N for its unit logarithmic derivative. If Gamma has length L,
the inner convex region is at distance at least b>0 from Gamma, and
|log(F/G_N)|<=B_N on a collar of Gamma, integration by parts gives

\[
\sup_{\mathrm{inner}}|h_z-h_{N,z}|
\le\frac{L B_N}{\pi b^3}.
\tag{8}
\]

This is the scalar-log transfer already proved in the sibling note02
§4, with its factor-of-two convention for the exterior drift removed.
It bounds the divided-difference error at the same pair of arguments
without an inverse internal gap. Using the model's own c_N,D_N also
requires the coordinate errors in (1); they are not silently discarded.
Formula (7) provides a regular kernel for paying that dependence.

The practical distinction from the older
[two-root pilot, note03](../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md)
would be a regime without separately resolved roots or slope floors.
That pilot already found negligible approximation error but a large
absolute unit-curvature payment. Improving approximation order alone
cannot repair that loss. The genuinely open question is whether the
canonical signed error/source identities control the signed cost in
(5) more effectively on an unresolved cluster.

## 3. Route B: a contraction of nonreality under degree refinement

At a fixed heat time, define u_N=max(0,-D_N). This measures the square
of the imaginary half-gap for a nonreal model pair, while allowing
finite approximants to have nonreal roots. A useful candidate inequality
would have the form

\[
u_{N+1}\le(1-a_N)u_N+e_N,\qquad
0<a_N\le1,\quad \sum_N a_N=\infty,\quad e_N/a_N\longrightarrow0.
\tag{9}
\]

If established, it forces u_N->0 and hence D>=0 by (1). To see this,
fix epsilon>0 and take e_N<=epsilon a_N beyond some degree. Then
(u_{N+1}-epsilon)_+ <=(1-a_N)(u_N-epsilon)_+; the product of the
factors tends to zero. Now let epsilon decrease to zero.

Equation (9) is an **unproved canonical estimate**, not a consequence
of compact convergence, Jacobi interlacing, or source moment positivity.
The correction must act on nonreality itself. Rapid convergence to a
nonreal limiting pair is fully compatible with all existing local
approximation estimates. Summable changes between degrees do not force
the limit to be real. A proposed contraction with only summable gains
a_N would likewise leave a possible initial defect.

The exact signed error and its parity make a two-degree comparison
N->N+2 worth considering instead of assuming one-step monotonicity.
That is a choice of what to derive, not an established sign. Starting
from contour increments of log(G_(N+1)/G_N), the missing result would
have to give a restoring signed contribution, with the omitted tail
smaller than that contribution. All-degree source identification in
E08 does not yet supply such a quantitative inequality.

This route can prove reality while allowing D=0. To exclude an interior
double collision using it, it would have to apply on both sides in heat
time: a true double event has D<0 on its earlier-time side. Reality at
one endpoint alone does not prove simplicity there.

## 4. Route C: bound accumulation across resolution scales

A positive-time double collision occupies only O(d_N) unresolved time.
That small measure is expected, not contradictory. An averaged estimate
must beat the collision's actual scale dependence.

For positive uniform error bounds d_N->0 on a fixed tube I, consider

\[
Q_N=\int_I\frac{d\lambda}{|D_N(\lambda)|+d_N}.
\tag{10}
\]

Suppose an interior double event occurs at T. On a sufficiently small
interval |lambda-T|<=delta, analyticity gives |D(lambda)|<=C|lambda-T|.
By (1), |D_N|+d_N<=C|lambda-T|+2d_N. Therefore

\[
Q_N\ge\frac2C\log\!\left(1+\frac{C\delta}{2d_N}\right).
\tag{11}
\]

Hence an independently obtained bound
Q_N=o(log(r_0/d_N)), for any fixed positive reference scale r_0,
would exclude such an event. A uniform bound for Q_N would suffice.
Conversely, if D has no zeros on the compact tube then its positive
minimum modulus makes Q_N bounded for all large N. This is a local
noncollision criterion, not an acquired estimate or evidence for RH.
It also permits a pair that stays nonreal throughout I: a real incoming
anchor is necessary to turn noncollision into persistence of reality.

The interpretation is that each finer scale near a genuine collision
contributes a nonvanishing amount to the integral. The number of scales
increases like log(1/d_N). This gives a precise target for a proposed
multiscale energy estimate. The Rodgers–Tao branch already explains why
excellent exterior approximation is compatible with inverse-gap energy
divergence. An estimate that stays bounded only away from a stipulated
event does not meet (11). No bound of the required strength is supplied
by the present VCD results.

## 5. Control screen and scope of the proposal

This is an analytical screen using the established control results;
their numerical certificates were not rerun. In particular, passing
shared local hypotheses is not described as passing an unproved
canonical inequality.

| Control class | What the present proposal actually says |
| --- | --- |
| Exact polynomial/Hermite heat collision | Passes regular factorization, outer isolation and bounded exterior drift. For the double model, (5) loses its margin at T and (11) has logarithmic growth. At a fixed earlier slice, any convergent model with D<0 must fail (9)'s combined gain/error conditions. The model lacks a positive theta source, so the positive-source controls remain necessary. |
| Weighted-square controls | Their isolated certified events share the local heat/cluster hypotheses and disprove exclusion from those alone. The all-real incoming anchor over a global descent is unavailable: these sources have no finite all-real threshold. Full reflection/completion also fails. |
| Reflected super-Gaussian and smooth positive/primitive controls | Their local events share the regular cluster laws. Unchanged integer-square theta arithmetic fails. No signed theta estimate is claimed to have been tested on them. |
| Euler-factor controls | Unchanged ordinary theta/Dirichlet coefficients fail. Their positive thresholds screen a global late-anchor argument: a real late slice alone cannot establish reality earlier. No particular isolated event is inferred merely from a threshold certificate. |
| Atomic and continuous finite-profile threshold controls | Their stated event examples pass positive-source information and selected finite observations, yet collide. Full theta profile/arithmetic and the stated threshold eventual-simplicity hypotheses fail. Finite atomic Jacobi chains also terminate; that fact does not defeat the generic local heat calculation. |
| Finite-prime, finite-head and finite-score controls | Matching the selected finite information does not establish (9) or the signed cost inequality. Full canonical identities fail. Retain each source's local-event/threshold distinction; smooth next-defect freedom is not a proved collision theorem. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic fails. Endpoint double zeros show why D>=0 should not be replaced by strict endpoint simplicity when only reality is sought. Their RH premise remains part of their construction. |
| Changed observation kernels / abstract profile relaxations | Respectively fail the exact physical Fourier/backward-heat premise, or the premise of being an actual physical field. They are not substituted into (4). |

To pass from a two-zero tube to a theorem about all zeros, one must
handle larger clusters, preserve total counts when contours are changed,
and cover increasing heights with adequate control of boundary entries.
A finite first collision cannot simply be assumed to exist globally.
Uniform strict separation at time zero would also demand simplicity,
which is stronger than the desired reality conclusion. These are
separate obligations, not supplied by a local pair calculation.

## 6. Tentative choice for the next discussion

The most grounded question is whether canonical Jacobi information
controls the **signed exterior contribution to squared-separation
transport**, while the cluster is still unresolved. Equations (7)–(8)
provide an existing route for transferring information without dividing
by a vanishing root gap. The real research gain would be a useful signed
estimate in (5), with explicit input cost and a genuine improvement over
an equally informed direct comparison. If the information only improves
the error bar, the earlier pilot already explains why that is inadequate.

Route B is the more ambitious alternative if the central interest is
induction in N. Route C can diagnose the strength needed from an averaged
estimate. These comparisons are saved for the author's choice; no route
is selected as an activated program and no new overview/plan is created.
