# Chern/Hopf projective sides and local sectors

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn's metadata.

**Status: exact boundary simplification and a parameterized local construction
proved in-note. No theta event exclusion or measured acquisition advantage.**
This shared note connects the BW10 multiplicity-selective observation,
BW12's complete face formula and I4's source/transport homes. The user
explicitly values simplification independently of noncollision. See the
[new program][program], [plan/register][plan] and [internal review][review].

Read the [result index][results], [avoid index][avoid], [control screen][controls],
[reformulation rule][a01], [scope rule][a07] and [coupled-estimate rule][a12].
The charge normalization and full-sphere regularization are inherited from
[BW10 MC6–MC9][mc]; the full spacetime face formula is [BW12 (11)][transport].
The specific local sectors and their face/corner accounting are the present
application. No literature priority claim is made. [Rudolph §1][rudolph]
was checked for Whitehead's integral formula, not for a new theta implication.

## 1. The form, its charts and the exact cancellation

Complex heat time is tau and spectral position is z. Use
\[
 G=(H,H_z),\quad H_\tau=-H_{zz},\quad E=|H|^2+|H_z|^2,
 \quad g=G/\sqrt E,\quad
 \mathcal A=-ig^*dg,\quad \mathcal F=d\mathcal A,\quad
 \mathcal C={\mathcal A\wedge\mathcal F\over4\pi^2}.
\]
All differential forms use real coordinates of C² and its complex
orientation. Use the actual normalized jet frame g throughout. The real
one-form d arg(H+iH_x) on physical spacetime is a different observation;
its side cancellation in [ICW Note 04][icw] does not imply cancellation here.

On H!=0 set p=H_z/H, eta=Im(dH/H), and
\[
 a_p={\operatorname{Im}(\bar p\,dp)\over1+|p|^2},\qquad
 \mathcal A=\eta+a_p,\qquad
 \mathcal F=da_p={2\,d\Re p\wedge d\Im p\over(1+|p|^2)^2}.
                                                               \tag{1}
\]
Eta is globally defined and closed on this chart; a globally single-valued
arg H is not required. If p=rho exp(i beta), then a_p=f d beta with
f=rho²/(1+rho²). Since a_p wedge da_p=0,
\[
 \mathcal C={\eta\wedge da_p\over4\pi^2}=d\mathcal B_H,
 \qquad \mathcal B_H=-{\eta\wedge a_p\over4\pi^2}.           \tag{2}
\]
Thus a cap lying in this chart reduces to its oriented two-dimensional
corner boundary: integral_cap C=integral_boundary(cap) B_H.

**Side lemma.** If a smooth three-face with G!=0 has its projective image
[H:H_z] in one fixed smooth real curve in CP^1, its pulled-back curvature
F and hence C vanish. This follows because F is the pullback of a two-form
from CP^1 and the restricted projective map has rank at most one.
It is a sufficient condition, not a classification of every cancelling side.
In particular, a genuine regular side |p|=P>0 has zero C integral.
A fixed complex equation p=c by itself is real codimension two at regular
points; the real modulus condition supplies the correct dimension.

The second chart H_z!=0, q=H/H_z, has its own primitive B_{H_z}.
On the overlap,
\[
 \mathcal B_{H_z}-\mathcal B_H
 ={d\arg H\wedge d\arg p\over4\pi^2}.                     \tag{3}
\]
The integral on a closed oriented corner surface is an integer: it is the
degree integral of its angular map into the two-torus. Hence reducing caps
to corners retains a possible seam integer. If an entire closed boundary
lies in the H!=0 chart, (2) already forces its total charge to zero.
An enclosing charge-one boundary cannot be handled by silently discarding
its H=0 chart seam.

## 2. An admissible ordinary-double sector with every face included

Assume a holomorphic heat field has an ordinary double at (0,a):
H=H_z=0 and h_2=H_zz!=0. Write h_3=H_zzz there. Then
\[
 DG(0,a)=\begin{pmatrix}-h_2&0\\-h_3&h_2\end{pmatrix},\quad
 \det_{\mathbb C}DG=-h_2^2\ne0.                            \tag{4}
\]
The local holomorphic inverse preserves real complex orientation. Choose
a target ball of radius r_1 compactly inside its image, and fix
0<r_0<r_1 and 0<kappa<1. Define the actual source domain as the inverse image of
\[
 K=\{Z\in\mathbb C^2:r_0\le\|Z\|\le r_1,\quad
       u:=|Z_2|^2/\|Z\|^2\le\kappa\}.                     \tag{5}
\]
A source-paid sufficient radius is given in §4. This is a four-manifold
with corners, with two solid-torus caps, one side [r_0,r_1] times T²,
and two torus corners. There is no additional chart wall because the
closed target ball is contained in the inverse image chart. The locus
u=0 is a polar coordinate degeneration, not a missing boundary face.

Use
\[
 Z_1=r\sqrt{1-u}e^{i\phi_1},\quad Z_2=r\sqrt u e^{i\phi_2}.
\]
Away from the harmless axis u=0,
\[
 \mathcal A=(1-u)d\phi_1+u\,d\phi_2,\quad
 \mathcal A\wedge d\mathcal A=d\phi_1\wedge du\wedge d\phi_2,
 \quad dV_{\mathbb C^2}={r^3\over2}dr\wedge d\phi_1\wedge du\wedge d\phi_2.
                                                               \tag{6}
\]
These formulas extend as smooth forms across that axis. The cap integrals,
with induced outward orientations, are therefore
\[
 \boxed{\ I_{\rm outer}=\kappa,\qquad I_{\rm inner}=-\kappa,
       \qquad I_{\rm projective\ side}=0.\ }               \tag{7}
\]
The side has |p|=sqrt(kappa/(1-kappa)), so the side lemma applies.
The cap primitive (2) gives the same result: the outer corner orientation
is minus dphi_1 wedge dphi_2, a sign essential to obtaining +kappa.
The complete boundary sum is zero, as required because the shell contains
no event. Exact side elimination and cap reduction are the achieved goal.

The inner cap still contributes -kappa as r_0 tends to zero. The resulting
apex is a singular boundary event, not an interior zero with fractional
charge kappa. The complementary sector contributes 1-kappa to a full
outer sphere; together they retain the ordinary event's charge one.
These jet-norm caps are not fixed-real-heat-time faces. [Note 02][time]
constructs a local punctured time sector and reduces every heat face to
one critical-value phase trace.

## 3. Regularization and an explicit limiting allowance

Use the inherited MC9 regularization parameter delta>0, distinct from r_0:
\[
 \mathcal A_\delta={E\over E+\delta^2}\mathcal A=k\mathcal A,
 \qquad \mathcal C_\delta={\mathcal A_\delta\wedge d\mathcal A_\delta\over4\pi^2}
                         =k^2\mathcal C.
\]
Here omega_delta=dA_delta/(2pi), equivalently
(i/(2pi)) partial barpartial log(E+delta²), in the inherited MC9 convention.
The projective side still vanishes exactly. In the radial sector,
\[
 \int_{G^{-1}K}\omega_\delta^2
 =\kappa\left[{r_1^4\over(r_1^2+\delta^2)^2}
              -{r_0^4\over(r_0^2+\delta^2)^2}\right].        \tag{8}
\]
This is MC8's known radial mass localized to a precisely specified angular
sector; the local holomorphic Jacobian is included by change of variables.
For each radial cap,
\[
 |I_{r,\delta}-I_r|\le2\kappa\delta^2/r^2.                 \tag{9}
\]
Indeed 1-(1+x)^(-2)<=2x for x>=0. The total shell mass is between zero
and 2kappa delta²/r_0². Thus delta/r_0->0 pays the unregularized limit
uniformly on these shells. The two iterated limits differ:
\[
 \lim_{r_0\downarrow0}\lim_{\delta\downarrow0}\int\omega_\delta^2=0,
 \qquad
 \lim_{\delta\downarrow0}\lim_{r_0\downarrow0}\int\omega_\delta^2=\kappa.
                                                               \tag{10}
\]
The second limit is the angular share of concentrated regularized mass;
it is not an integer event count on this singular sector.
For nonconstant-E caps, the correct chart reduction is
\[
 \mathcal C_\delta=d(k^2\mathcal B_H)-d(k^2)\wedge\mathcal B_H.
                                                               \tag{11}
\]
The amplitude term cannot be removed merely by using the unregularized
corner formula. It vanishes on the constant-E caps of (5).

## 4. Quantitative inverse chart from complete canonical moments

This lemma makes the radius condition in (5) explicit, conditionally on
ordinary-double event jets; it supplies no actual theta event data.
Take the canonical source normalization of [Rodgers–Tao (1), (3), (4)][rt].
For R_*>0 and a real event location a at heat time zero define
\[
 M_j=\int_0^\infty u^j e^{R_*u^2+R_*u}\Phi(u)\,du,
 \quad K=(M_5^2+3M_4^2+3M_3^2+M_2^2)^{1/2},
 \quad \mu={|h_2|^2\over\sqrt{2|h_2|^2+|h_3|^2}}.          \tag{12}
\]
For paid enclosures |h_2|>=ell_2>0, |h_2|<=u_2, |h_3|<=u_3, one may
replace mu by ell_2²/sqrt(2u_2²+u_3²), and use upper bounds for every M_j
in K. Unknown event-location uncertainty belongs in these enclosures.
For translated real heat time t_0, replace R_* in the quadratic exponential
by t_0+R_* and retain the linear weight R_*u. All coefficients and complete
source reflection remain unchanged; no internal root gap enters.

In the complex Euclidean ball ||(tau,z-a)||<=R_*, mixed derivatives of H
are bounded by the corresponding M_j, using H_tau=-H_zz. The combined
Frobenius norm of the two Hessians of G is bounded by K. Explicitly their
entries have absolute orders (4,3,3,2) and (5,4,4,3), producing (12).
Thus ||DG(X)-DG(0)||<=K||X||. Also mu<=s_min(DG(0)). Choose
\[
 0<R\le\min(R_*,\mu/(2K)),\qquad 0<r_1<\mu R/2.          \tag{13}
\]
For X,Y in the physical ball B_R,
||G(X)-G(Y)||>=(mu/2)||X-Y||. Writing G(X)=AX+N(X),
||N(X)||<=K||X||²/2 and ||DN||<=KR. For ||Z||<=mu R/2,
X->A^{-1}(Z-N(X)) is a 1/2-contraction of the closed B_R into B_{3R/4}.
It has a unique fixed point. This proves the needed inverse chart, target
ball inclusion and inverse Lipschitz bound 2/mu. Holomorphic regularity
follows from the invertible derivative. At a hypothetical canonical event,
h_2 and h_3 are actual complete-source jets, not freely chosen parameters.

**Complete acquisition contract.** Use the [ICW source ledger][source-ledger]
with the same exact finite summands and common omitted source. For weights
e^{T_*u²+Yu}, replace 9 by 9+Y in its omitted-mode b and exterior-ray b_n,
and add YU in the exterior exponential. Require the same positive b,b_n
and T_*<=8lambda_k, T_*<=8lambda_ne^{4U}; increase N,U if necessary.
This covers M_2 through M_5 and the event jets, with finite quadrature and
outward-rounding payments. Keep simultaneous H=H_z=0 matching if an event
is hypothesized. A certified lower |h_2| is needed for a numerical chart;
it is not inferred from a floating value. No acquisition was run here.

## 5. Frame, controls and comparator

The cap values in (7) refer to the fixed physical frame g. For a gauge
with a single-valued real lift chi, C changes by d(chi F)/(4pi²);
paired corner contributions must be retained. A sector alone has nontrivial
first cohomology: the smooth nonliftable gauge exp(i n phi_1) changes its
individual cap values to ±(n+1)kappa. It leaves the full shell sum zero.
Thus the reported individual flux is not an invariant under arbitrary
sector-only gauge changes. This ambiguity is absent once the physical
frame is fixed as in BW12. Corners require their induced orientations,
not an added unmotivated flux term in the original fixed-frame Stokes formula.

For H=(z-a)²-2tau, the inverse chart is exact:
\[
 z=a+Z_2/2,\qquad \tau=Z_2^2/8-Z_1/2.
\]
Equations (7)–(10) hold while its ordinary collision remains. The same
conditional local construction applies to any analytic ordinary-double
control, irrespective of arithmetic. For the catalogue: Euler factors
alter canonical arithmetic; weighted-square/finite-prime sources lack
full reflection; reflected/primitive controls lack canonical square
coefficients; normalized RH-conditional endpoint controls lack ordinary
Dirichlet arithmetic. No event or all-real continuation is assigned where
the source has not supplied one. These arithmetic mismatches are not used
by the cancellation lemma; it correctly remains compatible with events.

The direct comparator gets the same G-coordinate domain, source bounds,
frame and projective information, and can use (2), (7) and (8) itself.
The achieved gain is exact elimination of a three-dimensional side integral
and reduction of the remaining integrals to explicit caps/corners, not an
exclusive arithmetic estimator or measured speedup. Global chart assembly,
fixed physical spatial walls and higher multiplicities remain separate.
For m>2, h_2=0 and (4) is singular; do not extend this inverse-chart proof.

[program]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[time]: 02_CHERN_HOPF_PHYSICAL_TIME_SECTOR_REDUCTION_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/04_CHERN_HOPF_BOUNDARY_OPENING_REVIEW_20261022.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../avoid/01_restating_the_target.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[icw]: ../03_heat_transport_and_charges/notes/04_PHASE_BOUNDARY_REMOVAL_AND_CAP_REDUCTION_20261022.md
[source-ledger]: ../03_heat_transport_and_charges/notes/03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md
[mc]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[transport]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[rt]: https://arxiv.org/html/1801.05914
[rudolph]: https://arxiv.org/pdf/0912.4974
