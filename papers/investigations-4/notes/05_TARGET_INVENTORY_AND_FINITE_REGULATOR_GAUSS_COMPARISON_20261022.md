# Target inventory and a complete finite-regulator Gauss-area comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded authoring model
**gpt-6.1-sol (Codex), reasoning effort ultra**, verified from this chat's
active turn metadata. Contributing-agent checks are internal LLM checks;
there is no specialist review or formal analytic verification.

**Status: proved in-note, in the specified parameterized scope.** The
regularized spatial Green formula gives an explicit bias allowance without
an interior jet floor. On Note 03's sufficient ordinary-double window,
Note 04's global inverse-Schur certificate is worse than the direct Green
certificate for **every finite regulator**, by an explicit factor exceeding
707. This completes one bounded CHB-07 comparison as a scoped failure.
The inequality compares upper-bound certificates, not the actual integrals.
No theta acquisition, improved arithmetic bound or exclusion is supplied.

Read the [result index][results] and [avoid index][avoid], specifically
[local heat geometry][geometry], [collision controls][controls],
[classification][a01], [matched premises][a02], [scope][a07],
[coupled estimates][a12] and [complete targets][a13]. This is a quantitative
estimator comparison, not an RH-equivalent criterion. [Note 03][n3] owns
the complete physical window; [Note 04][n4] owns the positive mass. The
[overview][overview] and [existing register][plan] retain task ownership.

## 1. Short inventory of actual consumers

Use H_tau=-H_zz, G=(H,H_z), E=|H|²+|H_z|², and the fixed physical frame.
The following targets have different dimensions and denominators. No
identity between them is assumed.

| Consumer and exact source formula | Dimension, domain and weight | Direction, consequence and direct baseline |
| --- | --- | --- |
| **Spatial Gauss area**, [BW10 GA1–GA6][gauss]: A_t(Omega)=integral_Omega g_2 dA_z, g_2=|HH_zz-H_z²|²/E². We use A_t/pi and its complex-time average below. | A spatial disk at fixed t has real dimension 2; averaging over complex heat rectangle D gives dimension 4. Positive density; denominator is the complex jet energy E². | A smaller upper certificate would be an estimating gain. Finiteness alone cannot exclude an endpoint: GA6 retains the atom pi(m-1). GA3's spatial Green formula is the direct baseline. **Primary candidate here.** |
| **Physical tube / phase cap**, [BW10 MT7–MT10, MT21][tube]: I_eta=integral_a^b [partial_v |H(t,x+i eta)|²]/[2 eta E_R(t,x)] dx=pi+R_eta, with E_R=H(t,x)²+H_x(t,x)². | At fixed real time, the original spatial product tube has four real dimensions, normalized by 8 eta U V. The nontrivial transverse average has two dimensions; MT10 reduces it to a real interval. Its weight remains 1/E_R at the physical point. | MT8 retains B_eta-W_eta; MT21 gives the complete signed two-source R_eta. Under the stated RH/all-real product hypotheses, 0<=R_eta<=g eta² D_0/6. The equally informed direct comparator already has the exact cap pi and this trace allowance; the complex-energy Gauss density does not replace its denominator, transverse faces or signs. |
| **Critical-wall amplitude**, [ICW Note 02 (8)–(10)][icw-note]: log(B(T)/B(epsilon))=integral_epsilon^T q(t,c(t)) dt; on H_x=0, q=-H_xx/H=C_2/C_0 and S_1=0. | A one-dimensional moving real-time curve. The quotient divides by the signed critical value C_0, not E. On the c=0 phase wall, B=|H(t,c(t))|. | An upper budget controls endpoint amplitude; the ordinary-double exclusion budget with logarithmic coefficient less than one is already classified in ICW, not a new estimate here. A pointwise signed upper q<=k requires sigma(C_2-k C_0)<=0 with sigma=sign C_0. Same-source direct amplitude/critical-value evaluation is the baseline. |
| **Complete endpoint response**, [BW12 Note 15 (8)–(10)][covariance]: Delta_H=Delta_F+L_F(E_res)+B_F(E_res,E_res)+R_3, |R_3|<=C_3(rho). Its complete lower certificate is Delta_F+C_J-epsilon_J-C_3(rho), before acquisition error. | A response built from one- and two-source integrals, followed by oriented one-dimensional spatial-contour functionals; not an unsigned four-dimensional density. Note 15 compactifies the canonical law on [0,1], retaining its atom and contour denominators. | A stricter complete signed interval can be useful while it still contains zero. Exclusion requires a strictly positive full lower endpoint. The canonical covariance baseline retains L_F(e_2)+2B_F(bar E_res,e_2), the residual quadratic payment, cubic remainder, wall ratio and proper two-root geometry. No bridge from the present mass to that complete expression has been proved. |

The complete signed topological expression itself is [BW12 Note 18 (11)][transport],
I_late-I_early+I_side=sum q_p. Note 03 has already evaluated that full sum
as wind V. Its positive bulk replacement retains all imaginary-time faces
and the spatial wall; estimating an individual face by the total positive
mass needs an additional comparison. RH's full Weil form is a later
possible consumer only after an actual transform identity or inequality.

For the endpoint row, the exact contour operators are
I[f]=(2pi i)^(-1)oint_Gamma f dz,
L_F(V)=-4I[(z-c)V/F], and
B_F(V,W)=2I[(z-c)VW/F²]-I[V/F]I[W/F], with c the reference centroid.
Their denominators are F and F² on the paid external contour, not an
internal separation or the Gauss denominator. For the tube row, R_eta is
exactly MT21's two-source oscillatory integral with physical weight 1/E_R;
the identity I_eta=B_eta-W_eta and its equivalent MT10 evaluate the same
observation, including the weight derivative and transverse faces.

## 2. Direct regularized spatial Green formula and target bias

Take exactly Note 03's W=D times Omega, with
D=[-T,T]+i[-Y,Y], Omega={|z-a|<=R}, and T=Y=d/2. Retain its constants
h=|H_zz(0,a)|>0, D_2, epsilon_1, m_*=5hR/8, and

\[
 M_0=D_2(d+R^2/2),\qquad
 |H|\le M_0,\quad |H_z|\le\epsilon_1,\quad |H_{zz}|\le D_2,
 \quad E\ge m_*^2\quad\hbox{on the spatial wall}.          \tag{1}
\]

Put x=delta²>0 and D_z=HH_zz-H_z². The spatial Hessian identity gives

\[
 \gamma_\delta={|D_z|^2+x(|H_z|^2+|H_{zz}|^2)
                         \over\pi(E+x)^2}
       ={1\over4\pi}\Delta_z\log(E+x).
\]

The regulator makes this smooth on every fiber, including tau=0. Green's
formula therefore gives the exact identity

\[
 A_\delta(\tau):=\int_\Omega\gamma_\delta\,dA_z
   ={1\over4\pi}\int_{\partial\Omega}
                         \partial_n\log(E+x)\,ds.        \tag{2}
\]

For a real unit normal n in the spatial plane,
|partial_n E|<=2 epsilon_1(M_0+D_2). The circumference is 2pi R and
Area(D)=4TY. Positivity and (1)–(2) prove

\[
 0\le A_\delta(\tau)\le
 {R\epsilon_1(M_0+D_2)\over m_*^2+x},\qquad
 \mathcal G_\delta:=\int_D A_\delta\,dA_\tau
 \le F_\delta:={4TYR\epsilon_1(M_0+D_2)\over m_*^2+x}.    \tag{3}
\]

This pays the exact mixed-free *spatial* boundary derivative, not a
dropped mixed entry of the four-dimensional Hessian. No interior floor
for E has been used. In particular, the same bound is already available
on each fixed-time spatial disk before any complex-time averaging.

Define A_0^bd(tau) by the boundary expression (2) with x=0. On every
non-event fiber, A_0^bd=integral g_2/pi. At the event it includes GA6's
defect mass, whereas the canceled pointwise Gauss map alone does not.
The unique event fiber is null for heat-area integration. Write
mathcal G_0=integral_D A_0^bd dA_tau. Subtract the two *boundary*
expressions, where E has its paid floor:

\[
 A_\delta-A_0^{\rm bd}
 =-{x\over4\pi}\int_{\partial\Omega}
                        {\partial_n E\over E(E+x)}\,ds,
\]
\[
 |A_\delta-A_0^{\rm bd}|
 \le {R\epsilon_1(M_0+D_2)x\over m_*^2(m_*^2+x)},\qquad
 |\mathcal G_\delta-\mathcal G_0|
 \le Z_\delta:={x\over m_*^2+x}F_0.                     \tag{4}
\]

There is no asserted sign of this bias. The direct upper certificate is
uniform as delta tends to zero, and paying its bias returns exactly

\[
 \boxed{F_\delta+Z_\delta=F_0.}                          \tag{5}
\]

This is an explicit regularization allowance for the named consumer, not
a new small-area margin. At an ordinary double the normalized spatial
concentration remains one, in addition to its regular background.

## 3. Every finite regulator loses for the existing global Schur certificate

Retain Note 04's exact interface dmu_delta=(2/pi)s_delta gamma_delta dV,
including its mixed curvature. Its existing *global constant* certificate,
on Note 03's sufficient ordinary-double window, is

\[
 \begin{gathered}
 U=M_0^2+\epsilon_1^2,\quad
 A=M_0D_2+\epsilon_1^2,\quad B=\epsilon_1^2+D_2^2,
 \quad j_0=37h^2/64,\\
 c_\delta={xj_0^2\over(U+x)(A^2+xB)},\qquad
 \mathcal G_\delta\le
 T_\delta:={\pi\over2c_\delta}(1+B_\delta),\quad B_\delta\ge0.
                                                               \tag{6}
 \end{gathered}
\]

Here Q=1 follows from the conditional event/window theorem. B_delta is
the **mass** regulator error from Note 03, distinct from the **area** bias
Z_delta. No value of Q is selected to obtain a preferred estimate.

**Proposition.** For all delta>0 under precisely that sufficient-window
contract,

\[
 \boxed{T_\delta\ge K\left({D_2\over h}\right)^4F_0,
 \qquad K={5242880\pi\over23273}>707.}                   \tag{7}
\]

**Proof.** The contract gives d<=hR²/(32D_2), d<=alpha R,
alpha=min(1,h/(4(D_3+PD_2))), and D_2>=h. Consequently

\[
 D_2R\le\epsilon_1=D_2R+D_3d\le{5D_2R\over4},\quad
 {D_2R^2\over2}\le M_0\le{17D_2R^2\over32}.            \tag{8}
\]

Since 4TY=d², substitution in F_0 yields

\[
 F_0={d^2R\epsilon_1(M_0+D_2)\over25h^2R^2/64}
      \le {R^4\over320}(1+17R^2/32).                    \tag{9}
\]

For every x>0, (U+x)(A²+xB)/x>=UB. Thus (6), including even the
optimistic choice of discarding the nonnegative B_delta, gives

\[
 T_\delta\ge{\pi UB\over2j_0^2}
 \ge {2048\pi\over1369}\left({D_2\over h}\right)^4
             R^2(1+R^2/4)(1+R^2).                       \tag{10}
\]

For r=R²>0,

\[
 { (1+r/4)(1+r)\over r(1+17r/32)}>{8\over17},\qquad
 (1+r/4)(1+r)-{8\over17}r(1+17r/32)
                           =1+{53r\over68}>0.          \tag{11}
\]

Dividing (10) by the upper envelope in (9) proves (7). In particular,
the result holds without optimizing delta, without taking delta to zero,
and even before the mass error enlarges the certificate. All quantities
divided by are positive. This proves the claimed comparison. □

For the regularized target F_delta<=F_0, so (7) is stronger than the
comparison T_delta>707 F_delta. Recovering the unregularized target by
(4) gives T_delta+Z_delta, which is also worse than F_0. The strongest
direct method is granted the same geometry and source information and
may use the actual signed boundary expression (2); that can only improve
upon the direct certificate compared here.

**Scope of the failure.** This rules out an improvement by choosing a
finite regulator in the specific chain (6), with Note 03's sufficient
window and Note 04's global c_delta. It is not a lower bound on the true
Gauss area, an optimal constant, or a claim about every Schur comparison.
It does not cover other windows, localized/weighted estimates, sharper
actual curvature information, source-specific cancellations, or a positive
mass used to pay one error term of a complete signed expression. The
bounded-mass and bounded-weight results of Note 04 remain intact.

## 4. Critical-wall connection retained, with its actual missing payments

On H!=0 let p=H_z/H. Direct differentiation gives

\[
 g_2={|p_z|^2\over(1+|p|^2)^2}.
\]

For a real heat solution on its real critical wall H_x=0, H!=0, p=0 and
q=-H_xx/H=-p_z are real. Hence **g_2=q²** there. In the declared
RH/all-real paired-product regime, the separate product theorem gives
q>0 in a simple gap; the square by itself does not determine that sign.
No RH or all-real premise was used in §§2–3.

There are three separate unpaid comparisons for this amplitude consumer:
recovery of a moving real-curve trace from the complex-spacetime measure;
control of the quotient/signed C_2-k C_0 using the *same* source and S_1=0;
and an endpoint allowance strong enough for ICW's named integral budget.
A fixed-window boundary floor pays none of those by itself. Use home 02's
[unchanged-source ledger][source], with simultaneous value/jet matching,
full reflection, complete mode/ray tails, wall errors and rounding. No new
source model or critical-value floor is introduced here.

The quadratic supplies an exact scale check. For H=z²-2tau, c(t)=0,

\[
 q(t,0)=1/t,\quad g_2(t,0)=1/t^2,\quad
 \pi\gamma_\delta(t,0)={4\over4t^2+\delta^2},\quad
 q(t,0)^2=\left(1+{\delta^2\over4t^2}\right)
                         \pi\gamma_\delta(t,0).          \tag{12}
\]

Thus a finite regulator's apparently bounded wall density loses the
singular target unless its trace bias is paid. On [epsilon,T] this
multiplier costs up to 1+delta²/(4epsilon²); fixed delta does not pay the
endpoint limit. Yet its spatial area tends to
pi+pi R²/(R²+4) by GA8–GA9 and its complete mass tends to one. This exact
control disproves a uniform finite upper bound for the integrated q budget
or its q² trace derived solely from these bounded masses and generic local
jet upper bounds. It does not rule out paid endpoint-dependent trace
estimates or an additional theta-specific signed inequality.

## 5. Controls, review and disposition

The controls are applied by the scope of each statement, not by combining
their distinct preservation lists. The inequalities (2)–(7) use only local
holomorphic heat data and the stated paid contract. At a matching analytic
ordinary double they are supposed to retain the collision.

| Control family from [the register][controls] | Response and premise distinction |
| --- | --- |
| H=z | Positive spatial Gauss density but J=0 and zero bulk mass. It fails the ordinary-double/J floor premise of (6); it rules out generic unweighted domination, not (7). |
| Quadratic/Hermite and Note 03's neighboring-root quartic | The quadratic has Q=1 and (12); the quartic retains a separating spatial contour and total count two through a double. Their own sufficient local windows obey the comparison. They fail the unchanged canonical theta source/arithmetic; no collision exclusion is predicted. |
| Euler-factor sources | The generic local identities apply at matching finite analytic events, with their own bounds. The original Euler coefficients/completion are changed; no canonical theta source estimate is imported. |
| Weighted-square and finite-prime controls | Apply only at their established matching analytic events. Full normalized reflection/unchanged coefficients fail. Nontrivial finite-source perturbations have no all-real heat slice; the RH product sign is not assigned to them. |
| Reflected super-Gaussian and smooth positive-primitive controls | Their established analytic collisions retain the local mass/area laws. They fail the unchanged normalized integer-square theta expansion; strong reflection, positivity or primitive normalization alone does not separate them. |
| Earlier counter-kernels | The local identities apply at verified matching finite holomorphic events with their own window contract; this note acquires no new event or global real-root property for them. The complete canonical reflected theta coefficients are absent. |
| Smooth-density and two-channel controls | These screen a proposed transfer to the full Weil form in their own stated classes. They are not assigned a physical heat-jet event here. An exact transform/inequality bridge to that complete signed form is absent from the present Gauss comparison. |
| RH-conditional close normalized endpoint controls | They retain the stated all-real positive-time regime and can have an endpoint double. Ordinary Dirichlet-series arithmetic fails. Their critical-wall singularity remains compatible with bounded spatial area and bulk mass. |

[Review 06][review] records contributing-agent internal checks and the
[small exact-algebra receipt][receipt] binds its script and this note.
Finite checks support constants and control formulas; the written argument
proves the analytic comparison. No theta scan or numerical campaign is
needed to decide this candidate.

**Task disposition:** CHB-07 remains active, with its first bounded target
comparison complete as the scoped failure (7). Stop regulator optimization
within (6). CHB-04 stays complete in its conditional local scope;
CHB-05's actual acquisition is unperformed; CHB-06 and inherited BW10/BW12
exclusion gates are unchanged. The next unpaid work is a localized or
source-dependent comparison for a specified signed/error consumer, or the
critical-wall trace and coupled signed moment payment above. Selecting such
an inequality is not evidence for its truth. The present gain is deciding
the complete all-finite-regulator comparison and paying the named target's
regularization bias, independently of noncollision.

[n3]: 03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n4]: 04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[overview]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[source]: ../02_theta_source_constraints/README.md
[icw-note]: ../03_heat_transport_and_charges/notes/02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/06_FINITE_REGULATOR_GAUSS_COMPARISON_REVIEW_20261022.md
[receipt]: ../03_heat_transport_and_charges/numerics/CHB_GAUSS_COMPARISON_CHECKS_20261022.json
[results]: ../../../result-summaries/README.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md
[gauss]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[tube]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[covariance]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/15_CANONICAL_COVARIANCE_SIGNED_ENCLOSURE_20261021.md
[transport]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
