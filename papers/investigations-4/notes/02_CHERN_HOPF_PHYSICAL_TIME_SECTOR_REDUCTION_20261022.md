# Local physical-time faces with a cancelling projective side

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn's metadata.

**Status: local analytic face reduction proved in-note, conditional on an
ordinary double. No full event-enclosing physical window or theta exclusion.**
This advances [Note 01][sector] from radial jet caps to actual constant-real-
and constant-imaginary-heat-time faces. It retains the puncture and every
other face. See the [program][program], [plan][plan], [review][review],
[result index][results], [avoid index][avoid] and [scope rule][scope].
The parent is [BW12's full face formula][bw12]; [BW10 MC9][bw10] fixes the
normalization. This is not the real-phase one-form reduction.

## 1. Construct the domain before dropping its side

Translate a real ordinary double to (tau,z)=(0,a), with h_2!=0. Fix a finite
P>0. In a neighborhood of {0} times {|p|<=P}, solve
\[
 H_z(\tau,z)=pH(\tau,z).                                  \tag{1}
\]
The derivative with respect to z at (0,a,p) is h_2, independent of p.
The parameter-dependent analytic implicit-function theorem, or a uniform
contraction on this compact p disk, gives one holomorphic z=z(tau,p)
for sufficiently small |tau| and p in a slightly larger disk. It has
\[
 z(0,p)=a,\qquad H(\tau,z(\tau,p))=\tau B(\tau,p),\qquad
 B(0,p)=-h_2.                                             \tag{2}
\]
Shrink the uniform heat disk so B and H_zz-pH_z remain nonzero there.
B has a holomorphic logarithm on the product disk. Section 3 gives a
quantitative sufficient chart contract. No numerical theta enclosures
have been acquired; its actual source inputs remain unpaid.

For tau!=0,
\[
 z_p={H\over H_{zz}-pH_z}\ne0.
\]
If two p values had the same image z, (1) and H!=0 would force them equal.
Consequently Psi(tau,p)=(tau,z(tau,p)) is injective and holomorphic with
nonzero complex Jacobian on this punctured product, preserving orientation.

Choose a closed complex heat rectangle
D=[-T,T]+i[-Y,Y] inside the uniform disk, T,Y>0, and
0<epsilon<min(T,Y). The domain is
\[
 W_\varepsilon=\Psi\big((D\setminus\{|\tau|<\varepsilon\})
                                  \times\{|p|\le P\}\big). \tag{3}
\]
Its complete boundary consists of four physical heat-edge faces, an inner
heat-circle face, and the projective side |p|=P. Corners inherit their
product orientations. The axis p=0 is not a face. On this compact punctured
domain H!=0, so G!=0; no common zero is enclosed. As epsilon->0 the image
pinches to the event. That event is a boundary apex of this sector, not an
interior event of a full spatial neighborhood. All bounded p values map
to z=a when tau=0.

## 2. All heat-edge integrals reduce to one critical-value trace

Use F=2 dRe p wedge dIm p/(1+|p|²)² and
\[
 \kappa={P^2\over1+P^2},\qquad \int_{|p|\le P}F=2\pi\kappa,
 \qquad
 M(\tau)={1\over4\pi^2}\int_{|p|\le P}\operatorname{Im}\log B(\tau,p)\,F.
                                                               \tag{4}
\]
A different global log branch adds a constant to M and leaves its differences
unchanged. From Note 01's ratio-chart identity and (2),
\[
 \Psi^*\mathcal C={1\over4\pi^2}
             \{d\arg\tau+d\operatorname{Im}\log B\}\wedge F. \tag{5}
\]
For an oriented heat edge e from tau_a to tau_b, with the complex orientation
on its p disk, this gives the exact reduction
\[
 \boxed{\ I_e={\kappa\over2\pi}\int_e d\arg\tau
                       +M(\tau_b)-M(\tau_a).\ }             \tag{6}
\]
Differentiation/integration is legitimate on the compact product; p
derivatives of log B wedge the top p-form to zero. The apparent disk moment
also simplifies exactly. For each tau, Im log B(tau,p) is harmonic in p.
The curvature weight F is radial, so the angular mean on every centered
p circle equals its value at p=0. Integrating those circle means gives
\[
 M(\tau)={\kappa\over2\pi}\operatorname{Im}\log B(\tau,0).
\]
Define the critical-value trace V(tau)=H(tau,z(tau,0)). Since H_z=0 there,
V'=-H_zz. Consequently (6) is the stronger exact identity
\[
 \boxed{\ I_e={\kappa\over2\pi}\Delta_e\arg V
       ={\kappa\over2\pi}\operatorname{Im}\int_e
          {-H_{zz}\over H}(\tau,z(\tau,0))\,d\tau.\ }       \tag{6a}
\]
A continuous phase lift along e is essential; principal endpoint arguments
alone can lose integer turns. This removes both the three-dimensional
face quadrature and the endpoint two-dimensional moment acquisition.
The full p-disk chart still must be certified: values on the critical wall
alone do not prove the surrounding side exists. The radial disk and
holomorphy of log B are essential to this mean-value reduction.

The rectangle has the counterclockwise orientation in the heat plane:
late face t=T goes upward in Im tau, the top imaginary-time face goes left,
the early face t=-T goes downward, and the bottom imaginary-time face goes
right. The inner circle is clockwise. Every face is retained:

| Face | Exact contribution |
| --- | --- |
| Each of four heat edges | Equation (6a): kappa/(2pi) times its oriented critical-value phase change. |
| Their complete outer sum | kappa: angular increments total 2pi and all M corner terms telescope. |
| Inner heat-circle face | -kappa, exactly for every positive epsilon; M returns to its starting value. |
| Projective side | Zero: p is restricted to |p|=P, hence F pulls back to zero. |

The total is zero, consistent with the punctured sector containing no event.
The imaginary-time faces have been simplified, not deleted. The inner cap
cannot be dropped when epsilon shrinks. Individual face values need the
B(tau,0)-dependent phase corrections; the total kappa does not make them
zero. In the symmetric rectangle, the late/early angular increments are
2 arctan(Y/T), and each imaginary-time increment is 2 arctan(T/Y).
Their critical-value phase corrections still need to be included.

The field-dependent corner function has the leading expansion
\[
 B(\tau,p)=-h_2+O_P(\tau),\qquad M(\tau)=M(0)+O_P(|\tau|).
\]
This is a qualitative analytic statement. No uniform high-height constant,
paid small source remainder or advantageous numerical cost is inferred.
An exact signed acquisition of the critical-value phase increments in
(6a), including branch tracking, is the remaining physical-face estimating
question; the disk integrals are no longer acquisition obligations.

## 3. Current, geometry and source payments

Here is an explicit sufficient implicit-chart contract, conditional on an
actual ordinary event. On |tau|<=d, |z-a|<=r, |p|<=P, let h=|h_2|>0,
D_j bound |partial_z^j H|, epsilon_1 bound |H_z|, and epsilon_2 bound
|H_zz-h_2|. Require strict margins in
\[
 \theta={\epsilon_2+P\epsilon_1\over h}<1,\qquad
 d(D_3+PD_2)<(1-\theta)hr,\qquad
 \delta_F=h-\epsilon_2-P\epsilon_1>0,
\]
\[
 \epsilon_2+{\epsilon_1(D_3+PD_2)\over\delta_F}<h.          \tag{6b}
\]
The map z -> z-(H_z-pH)/h_2 is a uniform theta-contraction of the closed
z disk into its interior. Its derivative bound follows from
|H_zz-pH_z-h_2|<=epsilon_2+P epsilon_1; its center displacement is at most
d(D_3+PD_2)/h by heat evolution and exact event matching. Thus it produces
the full holomorphic graph, with
|z_tau|<=(D_3+PD_2)/delta_F. Integrating
\[
 B(\tau,p)=\int_0^1[-H_{zz}+H_z z_\tau](s\tau,z(s\tau,p))\,ds
\]
proves |B+h_2|<=epsilon_2+epsilon_1(D_3+PD_2)/delta_F<h, supplying B!=0
and its log branch. All inequalities can be made strict on a slightly
larger p disk, as needed above. Fallback complete-moment bounds are
\[
 \epsilon_1\le D_2r+D_3d,\qquad
 \epsilon_2\le D_3r+D_4d.
\]
For fixed finite P and h>0 these conditions are feasible by first taking
r small and then d/r small, with D_j bounded on a fixed ambient polydisk.
No computed radius or observed theta event is asserted. Use paid jet
lower bounds, complete-source upper bounds and inward parameter rounding
for a finite implementation; source normalization and all tails are those
of Note 01 §4. This contract does not presume a nonzero H floor at the event.
Write b=h-|B+h_2|_upper>0. On |tau|>=epsilon the compact floors are
\[
 |H|\ge\varepsilon b,\quad
 |Q|=|H|\,|H_{zz}-pH_z|\ge\varepsilon b\delta_F,\quad
 E\ge\varepsilon^2b^2.
\]
They deteriorate as epsilon tends to zero, as the retained cap requires.


On a regular graph, put Q=H_z²-HH_zz. Complexification of the phase current gives
\[
 z_\tau={Q_z\over Q},\qquad
 z_\beta=-{iHH_z\over Q}\quad(p=Pe^{i\beta}).               \tag{7}
\]
These formulas follow by differentiating p=H_z/H. They need Q!=0; a graph
failure at Q=0 need not be a zero of G. Near the chosen event the construction
above avoids that failure on each compact punctured sector. The side is
three-dimensional because tau supplies two real coordinates and beta one.
This is not the scalar-energy current 2H_x/H.

For a boundary implementation the defining function can be
S=|H_z|²-P²|H|². On S=0 and G!=0,
\[
 |\nabla_z S|=2P|Q|.                                     \tag{8}
\]
Thus a certified boundary Q floor supplies spatial regularity. It is a
boundary-chart condition, not an unknown internal root-gap assumption.
Complete-source bounds M_j(T_*,Y_*) give
|z_tau|<=(M_1M_2+M_0M_3)/delta_Q and
|z_beta|<=M_0M_1/delta_Q on a paid compact graph.
Use [Note 01 §4][sector] for the full-tail/rounding interface.

A complete finite acquisition must pay: the uniform implicit chart and
branch; all simultaneous value/derivative observations; B and Q floors on
the chosen compact punctured domain; the same unchanged source and tails
for every moment; critical-value phase tracking and endpoint uncertainty; and any
quadrature/rounding. Merely making |p|-P small in value does not control
a three-form's pullback: approximate walls require tangential derivative
errors or a validated exact level geometry.

The finite-regularization form is k²C, where k=E/(E+delta²). Its side still
vanishes, but (6) is not its formula unless the amplitude correction in
Note 01 (11) is also paid. On a domain with a proved E floor, passing to the
unregularized form is straightforward; no floor uniform in epsilon is
claimed here.

## 4. Comparison, collision control and what remains

The direct evaluator receives the same phase graph, B, critical-value
data, source error and branch information. It can use (6a) too. The achievement
is a structural reduction of a complete family of face integrals, not an
arithmetic distinction or an established speedup.

For H=z²-2tau, choose the analytic local branch
\[
 z(\tau,p)={-2p\tau\over1+\sqrt{1+2p^2\tau}},\qquad
 H={-4\tau\over1+\sqrt{1+2p^2\tau}},\qquad
 B={-4\over1+\sqrt{1+2p^2\tau}},                           \tag{9}
\]
with the limits at p=0. On a sufficiently small product disk this satisfies
(1)–(2) exactly. Here V=-2tau, so every heat-edge contribution is exactly
kappa Delta arg tau/(2pi), although B varies with p. For P=1 and a small
square centered at zero, each outer heat face contributes 1/8, the inner
face -1/2, and the side zero. The ordinary collision survives. A rectangle
wholly in Re tau>0 instead has zero winding. More generally, every analytic ordinary-double control
has this local reduction; the [arithmetic controls][controls] receive no
invented events or new all-real regimes. Unchanged theta coefficients
would be needed for a theta-specific estimate, not for the cancellation.

**Continuation update, 22 October 2026:** [Note 03][complete] now supplies
the local complete-boundary extension described below, with both charts,
all physical faces and explicit parameterized boundary floors. This note's
punctured-sector scope is unchanged; the new construction splits only the
closed boundary of a genuine enclosing product window.

The extension missing from this note was an **event-enclosing physical window** with its
complementary projective chart or sector and every connector accounted for.
A bounded-ratio pinched sector alone does not enclose a full neighborhood
of the event. In addition, practical comparison needs paid values of the
critical-value phase increments, or a useful cancellation across a
larger assembled boundary. Higher multiplicities have H_zz=0 at the event,
so the implicit-function argument used here does not transfer automatically.
No BW10 simplicity or BW12 global-exclusion gate is completed.

[sector]: 01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[program]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/04_CHERN_HOPF_BOUNDARY_OPENING_REVIEW_20261022.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[scope]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[bw10]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[bw12]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md

[complete]: 03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
