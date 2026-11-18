# B07 r1 — Regional gap statistics and a backward three-gap comparison

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable in the
registered chat0002 metadata; advisory helpers inherited settings.
Type **B**, recommended **Astra**. [Frozen request][request].

**Status: proved in-note conditional local comparisons; statistical source
acquisition open.** A separate internal assessment is requested before
quantitative reuse. No new bound on the de Bruijn–Newman constant is claimed.
The gain here is an explicit finite-data safety margin: two neighboring
exterior zeros improve the elementary backward gap comparison. Regional
minimum evolution and a rare-event consumer identify how statistics could
use that margin, without assuming independence or a random-matrix law.

Read-first routing: [result summaries][results], especially [cluster18][cluster]
and [collision controls12][controls]; [avoid index][avoid], especially
[classification01][classification], [premise screen02][premises] and
[scope07][scope]. Under classification01 this is a **quantitative local
milestone**, not an RH-equivalent reformulation: a sufficient positive
margin below is explicitly computable from initial gaps and can fail.
Its numerical constants are proved; no uniform canonical margin is acquired.

## 1. A statistical minimum is a legitimate observable

Work on the inherited physical slab 0<=t*-Delta<=t*<=1/2, where the
canonical strip, count and product inputs used below are paid. Start at a
known **all-real, simple** canonical time t*, using H_t=-H_zz. Set u=t*-t,
with no height-dependent rescaling. Extension outside this slab requires
its own verification of those source and complete-product inputs.
Choose K finite buffered blocks and freeze their finite, nonempty sets of
eligible consecutive-pair labels J_k at u=0. Include boundary-crossing
pairs in a covering application. Let the random index X be uniform on
{1,...,K}; all zeros remain deterministic. Continuous random centers are
also possible, but require measurable labels and integrable domination;
the finite formulation below needs neither extra assertion.

For each eligible pair write x_j<x_{j+1}, c_j=(x_j+x_{j+1})/2,
D_j=(x_{j+1}-x_j)^2/4, and define the complete exterior quantities
\[
 Q_{j,\rho}=(\rho-c_j)^2-D_j,
 \quad M_j=\sum_{\rho\ne x_j,x_{j+1}}Q_{j,\rho}^{-1},
 \quad S_{j,n}=\sum_{\rho\ne x_j,x_{j+1}}Q_{j,\rho}^{-n}.
 \tag{1}
\]
Every occurrence is counted. Work on a stopped interval on which the
complete divisor is real and simple and these branches continue. A local
window alone does not protect exterior reality. On every compact
subinterval before the stop all required pairs have strict isolation.
The infinite tails in (1) are absolute, as in the accepted canonical
product/count input. Then
\[
 D_{j,u}=-2+4D_jM_j,\qquad
 M_{j,u}=-2M_j^2+12S_{j,2}+16D_jS_{j,3}.
 \tag{2}
\]
Since the pair is adjacent and the complete exterior is real, every
Q_{j,rho}>0. Thus M_j,S_{j,2},S_{j,3} are nonnegative.

**Strict-isolation extension of the identity.** The accepted [GT Note41][riccati]
and [CM Note09][hierarchy] state (2), with forward time sign reversed here,
on a stronger quantitative collar. Generic consecutive real zeros need
not satisfy that collar. At any simple time choose
\[
 \sqrt{D_j}<R<\min_{\rho\ne x_j,x_{j+1}}|\rho-c_j|.
 \tag{3}
\]
Local finiteness and adjacency make the strict interval nonempty. The
circle contains exactly the pair. At this frozen time, truncate the
canonical product in complete opposite/conjugate groups, retaining the
pair, and evolve each polynomial by its exact heat equation. Products and
all fixed spatial jets converge uniformly on the circle. The identities
\(\partial_t(H_z/H)=-H_{zzz}/H+H_zH_{zz}/H^2\) and the contour formulas
for c,D,M and their time derivatives therefore pass to the limit exactly
as in Note41 §2, using its §1 product setup. Finite nearby denominators are separated by (3), and the
remaining inverse-square tails converge absolutely. The finite polynomial
algebra for (2) uses no factor-four radius ratio. This proves (2) at the
chosen time; compact pre-collision intervals admit finitely many such
charts. No strong collar, uniform clearance at a multiple event, or
common-time convergence of truncated polynomial evolutions is asserted.
This extension is about identities; old quantitative collar estimates
are not imported to the larger class.

Set q_k(u)=min_{j in J_k} D_j(u). On each compact pre-stop interval it is
locally Lipschitz. Almost everywhere its derivative equals that of an
active minimizer j_k(u); derivatives of tied active branches agree at
almost every tie time. For a C^1 test phi on the bounded range,
\[
 \frac{d}{du}\mathbb E\phi(q_X)
 =\mathbb E\{\phi'(q_X)[-2+4q_X M_{j_X}]\} \quad\text{a.e.}
 \tag{4}
\]
Switching is harmless for this envelope law; it does not create one
persistent closest-pair trajectory or transfer a previous pair's anchors.
The minimum marginal does not close (4): it needs the joint law with the
active pair's complete exterior interaction. This is the relevant BBGKY
analogy. No independent-pair closure is supplied.

Positivity immediately gives q_k(u)>=q_k(0)-2u, hence
\[
 \mathbb P(q_X(u)\le r)\le\mathbb P(q_X(0)\le r+2u),\qquad r\ge0,
 \tag{5}
\]
throughout the common protected interval. A first covered collision by
Delta requires an initial gap-square D<=2Delta somewhere in its block.
After an earlier unprotected exterior collision these statements cannot
be continued using positivity.

## 2. The hierarchy improves the elementary safety time

Fix one eligible pair. Suppose 0<d_0<=D(0), and a paid initial lower bound
0<=b_0<=M(0) is available. Define b(u)=b_0/(1+2b_0u). By (2),
\[
 M_u\ge-2M^2,\qquad
 (M-b)_u+2(M+b)(M-b)\ge0.
\]
An integrating factor on each compact pre-stop interval gives M>=b.
Writing a(u)=1+2b_0u and using D>=0 before collision,
\[
 (a^{-2}D)_u=a^{-2}(D_u-4bD)\ge-2a^{-2}.
\]
The integral equals u/a(u), including b_0=0 by continuity. Consequently
\[
 \boxed{D(u)\ge a(u)[d_0a(u)-2u].} \tag{6}
\]
The bracket is affine and positive at u=0. Thus
\[
 \boxed{d_0(1+2b_0\Delta)>2\Delta} \tag{7}
\]
keeps the lower bound strictly positive for all 0<=u<=Delta. In a
first-collision argument it excludes this pair at that event, by continuity
of D. It does not assert exterior reality beyond a different earlier
collision. If b_0d_0<1 the permitted duration is
\[
 \Delta<\frac{d_0}{2(1-b_0d_0)}. \tag{8}
\]
If b_0d_0>=1 the scalar comparison has no finite cap; its regime and
coverage hypotheses still do, so this is not infinite backward descent.

For comparison with the original transport consumer, if
A(u)=integral_0^u M(v)dv, the exact equation gives
\[
 D(u)=e^{4A(u)}\left[D(0)-2\int_0^u e^{-4A(v)}\,dv\right],\qquad
 2\int_0^u e^{-4A(v)}\,dv\le\frac{2u}{1+2b_0u}.
 \tag{9}
\]
The lower environment envelope is derived from initial data and the real
hierarchy; it is not an assumed full-time bound.

Let g=x_{j+1}-x_j, h_L=x_j-x_{j-1}, h_R=x_{j+2}-x_{j+1} initially.
The two adjacent exterior occurrences alone supply
\[
 d_0=g^2/4,\qquad
 b_0=\frac1{h_L(h_L+g)}+\frac1{h_R(h_R+g)}\le M(0).
 \tag{10}
\]
Omit an unavailable side, or any term not certified; omitted exterior
terms are positive. Certified lower/upper gap enclosures must be propagated
with the appropriate monotonicities, rather than substituted arbitrarily.
The statistical observable with a concrete consumer is therefore the joint
law of **three consecutive initial gaps**, or the lower tail of
\[
 R_j(\Delta)=\frac{g_j^2}{4}(1+2b_{0,j}\Delta)-2\Delta. \tag{11}
\]
For three equal initial gaps g, (10) gives b_0=1/g^2, so (8) allows
Delta<g^2/6, compared with g^2/8 when b_0=0. This is an illustrative
conditional improvement, not canonical gap data or a new universal step.
A regional minimizer selected initially need not remain the worst score:
apply (11) to every eligible pair and take the minimum of those margins.

## 3. Pair counts and exact exclusion are different statistical tasks

For a finite initial real-zero window, let C_k(r) count unordered distinct
label pairs at distance <=r. Include all pairs in the comparison set;
then a closest pair is consecutive, and
\[
 \mathbb P(\hbox{minimum gap in block }X\le r)
 =\mathbb P(C_X(r)\ge1)\le\mathbb E C_X(r). \tag{12}
\]
Exact minimum laws require void/higher-order information, as the earlier
[OC pair-marginal discussion][ocdiscussion] explains. A useful one-sided
upper bound can nevertheless come from a two-point majorant. For (11),
neighbor-conditioned or higher-order information is needed. A full
four-point configuration describes three gaps; the condition that no
intermediate zeros occur is an additional nearest-neighbor/void condition.
Consecutive-gap data cannot be silently identified with an unrestricted
four-point marginal.

The [OC full marked-pair proof][ocproof], accepted in [OC assessment14][ocaudit],
provides time moduli at fixed positive blur, with multiplicity and exterior
tails retained. It does not acquire an initial profile or a sharp near-zero
gap tail. A nonnegative smooth majorant for (12) could use that interface
only after paying resolution, blur, edge and height errors. Its constants
grow as resolution shrinks; passing to a sharp event is not free. Distinct
labels at a repeated point count; subtracting the multiplicity diagonal
would remove the event being investigated.

Define the conservative bad-block count
\[
 B_\Delta=\#\{k:\min_{j\in J_k}R_j(\Delta)\le0\}.
\]
It is an integer and P(block X is bad)=B_Delta/K. A proved bound strictly
below 1/K forces B_Delta=0, so every covered margin is positive. A small
but larger probability allows exceptional blocks. An actual whole-interval
collision count admits the same integer logic if its upper bound is
acquired; an average over observation times alone can miss an isolated
event. Continuous random centers instead require a positive lower measure
contributed by any event, including at window boundaries.

To turn these statements into Lambda<=t*-Delta one still needs: (i) a
known simple all-real start, (ii) coverage of every possibly failing pair,
including block boundaries, (iii) a common first-loss argument for the
whole interval, and (iv) a paid uniform high-height theorem or tail bound
which prevents failure escaping to infinity. For example, an independent
real/simple high-height result uniform on the entire slab reduces the
remaining collision problem to a buffered compact region. Pointwise
high-height cutoffs at each time do not automatically give such a uniform
statement. No such all-height input or sufficient statistical margin is
proved here. Density one or probability tending to one alone is inadequate.

## 4. Sources, controls and disposition

The checked primary [Rodgers–Tao paper][rt], introduction, §4 Theorem 4.16
and §9 around (93), supplies a genuine precedent for averaged gap dynamics.
Their nearly equal spacing consequence is obtained under Lambda<0 and
contradicts a positive proportion of small gaps, proving the **lower**
bound Lambda>=0. Their §4 time interval Lambda<t<=0 is not imported as a
positive-time theorem here; (2) was justified locally from our contour
input. The proposed application here would lower an established **upper**
bound, by proving all-real continuation from t* to t*-Delta. No statement
about the current best numerical upper bound is needed or made. The paper
was already cataloged in the parent [source receipt][rtreceipt]; this pass
checked its cited primary HTML passages and downloaded no new PDF.

Analytical control replay uses [controls12][controls] and the explicit
family-by-family [Note13 premise table][controltable]. Euler-factor,
weighted-square, finite-source, finite-prime and canonical-score changes
fail unchanged theta/full reflected arithmetic in their specified classes;
reflected super-Gaussians fail the canonical arithmetic/order input;
smooth primitive controls have unpaid canonical strip/count transfer;
atomic/finite-profile controls lack the complete canonical population;
RH-conditional mergers retain RH and changed arithmetic; changed kernels
fail the physical readout; fractional relaxations lack integer realization;
static surgery lacks a common canonical heat evolution. Those failures do
not establish a favorable statistical law for theta. The generic local
comparison itself can hold for noncanonical real-rooted heat fields.

In particular H(t,z)=z^2-2(t-t_c) has D=2(t-t_c), M=0. At t*>t_c,
(7) is exactly Delta<t*-t_c. Equality permits the actual collision.
Thus strictness and the missing margin are essential; real initial roots
and heat evolution do not by themselves allow an arbitrary descent.
This finite control fails the canonical population premise, but tests
(2), (6) and their endpoint interpretation exactly. No random simulation
or numerical evidence is used for a proof claim.

**Decision:** retain the regional statistical direction and select the
three-gap score (11), together with integer exclusion and complete height
coverage, as its concrete consumer. The minimum law (4) exposes the joint
hierarchy; (6) supplies an explicit positive-environment comparison.
Next conceptual question: can the canonical source supply a quantitative
lower-tail estimate for min R_j(Delta) with a uniform high-height payment,
strong enough for zero exceptions? No source-acquisition execution packet
is issued without a distinct proof mechanism. The independent finite-divisor
benchmark [E16][e16] remains ready and unchanged. The present work is not a
completion of E16, a finite BBGKY closure, or an improvement of Lambda.

[request]: ../research-progress/handoffs/VCD-GT-CM-B07-r1.md
[riccati]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[hierarchy]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[controltable]: 13_VCD_GT_CM_B03_JOINT_TRANSPORT_AND_SUPERZETA_20261118.md
[e16]: ../research-progress/handoffs/VCD-GT-CM-E16-r1.md
[ocdiscussion]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/brainstorm/notes/06_TND_OC_PAIR_MARGINAL_AND_RODGERS_TAO_SPACING_20261108.md
[ocproof]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md
[ocaudit]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/reviews/14_TND_OC_E12_R1_FULL_MARKED_PAIR_CLAIM_ASSESSMENT_20261108.md
[rtreceipt]: ../../../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md
[rt]: https://arxiv.org/html/1801.05914v5
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
