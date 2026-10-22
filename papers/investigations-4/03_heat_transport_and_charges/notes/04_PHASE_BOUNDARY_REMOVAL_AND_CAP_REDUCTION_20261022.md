# Removing phase-boundary integrals and retaining the cap terms

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active root turn metadata.

**Status: exact finite real-phase boundary reduction, built on the inherited
phase-current identity; no theta exclusion or measured acquisition gain.**
Edward Baker clarified that simplifying integrals related to topology by
removing their boundary terms is an objective independently of noncollision.
The [overview][program] and [progress register][progress] now explicitly
include this as ICW-07, independent of ICW-03's endpoint-survival gate.

Read the [result index][results], [avoid index][avoid], [controls][controls],
[scope rule][scope] and [re-realization rule][coordinates]. The original
phase current and its wall cancellation are in [BW09 Note 06 §3][bw09]
and [home Note 02][previous]. We do not relabel those as a new discovery.
The contribution here is the explicit cap reduction and the residual left
when one instead uses scalar-current walls. [Review][review] records scope.

## 1. Identify the integral whose side term is to vanish

Write J=H+iH_x, E=H²+H_x², p=H_x/H, Q=H_x²-HH_xx and q=Q/H².
The real-jet phase one-form is, wherever E>0,
\[
 \omega=d\arg J={Q_x\,dt-Q\,dx\over E}.                    \tag{1}
\]
Indeed H_t=-H_xx and H_xt=-H_xxx give the time numerator
H_x H_xx-H H_xxx=Q_x. The phase need not have a single-valued global
argument; (1) is the well-defined differential on the nonzero-jet set.
On an admissible closed contour, (2pi)^(-1) integral omega is the winding
number. A nonzero-jet boundary is mandatory even if zeros lie inside.

For a wall x=w(t), the side integrand is
\[
 \omega(\partial_t+w'\partial_x)={Q_x-w'Q\over E}.          \tag{2}
\]
Thus v_theta=Q_x/Q removes this **topological phase** side term when Q!=0.
Where H!=0 this is equivalently a constant-p wall p=c. By contrast,
\[
 \partial_t(H^2)+\partial_x(2HH_x)=2H_x^2
\]
has moving-wall term H²(w'-2p), removed by v_0=2p. These are different
integrals. The jet-energy current also remains a separate observable.

For a scalar-current wall, the exact phase residual is
\[
 {Q_x-2pQ\over E}={q_x\over1+p^2}.                         \tag{3}
\]
For a phase wall, its scalar-energy residual is
\[
 H^2(v_\theta-2p)=H^2q_x/q.                               \tag{4}
\]
Consequently simultaneous cancellation requires q_x=0 along a common
wall (where H,Q!=0). It is possible for special symmetry walls; it is
not automatic between two zeros. Equations (3)–(4) identify exactly which
remaining integral must be paid if the other current is chosen.

A concrete canonical common wall is x=0: evenness gives S_1=S_3=0,
while source positivity gives C_0,C_2>0 and Q=C_0C_2>0. Both currents
vanish there. Combining this endpoint with any regular scalar wall gives

d/dt integral_0^{w(t)} H² dx = 2 integral_0^{w(t)} H_x² dx.

This exact boundary simplification needs no noncollision conclusion. It
does not remove the other scalar wall's phase residual (3).

## 2. Exact reduction to caps, with orientation

Let a finite strip epsilon<=t<=T be bounded by two C¹ phase walls w_L<w_R.
Assume J!=0 on the entire boundary and Q!=0 on its sides. Orient by dt wedge dx,
so the upper cap runs left to right and the lower cap right to left. Then
\[
 2\pi W_J(\partial\Omega)
 =\int_{w_L(T)}^{w_R(T)} {-Q(T,x)\over E(T,x)}\,dx
  -\int_{w_L(\varepsilon)}^{w_R(\varepsilon)}
                     {-Q(\varepsilon,x)\over E(\varepsilon,x)}\,dx. \tag{5}
\]
Both side integrals are exactly absent. This is a valid simplification even
when it provides no new estimate for the cap integrals or the integer W.
It leaves the event information in the caps and their lifted phase branches.

For the particularly simple regular same-gap case, assume H!=0 throughout
the strip, q>0, and fixed finite labels p(w_L)=c_L>c_R=p(w_R).
Each cap lies in one H-sign half-plane, and therefore
\[
 \int_{w_L(t)}^{w_R(t)}\omega
       =\arctan c_R-\arctan c_L.                          \tag{6}
\]
No spatial quadrature is needed once label and branch validity are paid.
The cap identity needs only H!=0 and actual constant-p graph walls; q>0
is used here for uniqueness and the stated ordering, not for the identity.
Both caps agree and W=0. The zero degree is consistent with the first jet
having no zero in this strip; it is not new evidence for noncollision.
For caps crossing H=0, principal arctangents alone are insufficient:
retain the continuous phase lift and all branch corrections. The integer
winding number belongs to the full closed contour.

At an ordinary double, fixed-label walls obey the inherited expansions
w_c(t)=a+(h_3/h_2-c)t+O(t²), H(t,w_c)=-h_2 t+O(t²).
Hence the cap width is (c_L-c_R)t+O(t²), but its phase integral (6) is a
**nonzero constant**. A shrinking cap cannot be dropped on length grounds.
At t=0 the first jet vanishes, so the contour ending there is inadmissible.
Use a positive cutoff and retain its cap, or add a justified connector and
local index. Smooth wall geometry does not remove that payment.

The quadratic provides an exact control: all these phase walls are regular
for t>0, both side terms vanish, and (6) holds, while the double event persists.
The generic reduction is supposed to remain compatible with this event.
It has no arithmetic premise that rejects the collision.

## 3. Complete-source implementation and open comparison

With C_j=integral u^j e^{tu²}Phi cos(xu) and
S_j=integral u^j e^{tu²}Phi sin(xu),
\[
 H=C_0,\quad H_x=-S_1,\quad H_{xx}=-C_2,\quad H_{xxx}=S_3,
 \quad Q=S_1^2+C_0C_2,\quad Q_x=S_1C_2-C_0S_3.
\]
A constant-p wall satisfies S_1+cC_0=0. Its implicit velocity is
\[
 w_c'=-{S_3+cC_2\over C_2+c^2C_0},                       \tag{7}
\]
provided the denominator is nonzero. This is equivalent to Q_x/Q on its
regular nonzero-H portion. The implicit wall equation may continue through
an ordinary event, but the phase one-form remains undefined at J=0 there.
For c=0, w'=-S_3/C_2; this is generally not the scalar velocity, which equals
zero at an H_x=0 point. Under q>0 a gap contains only one c=0 wall, so two
distinct labels are needed to bound this interior strip.

If scalar walls are used instead, (3) becomes the complete signed expression
\[
 {2S_1^3+3C_0S_1C_2-C_0^2S_3\over C_0(C_0^2+S_1^2)}.      \tag{8}
\]
These moments come from one unchanged source. Use the common-source
residual set and all-tail payments of [Note 03 §2][contract], now through
j=3, or higher moments where parameter-cell propagation requires them.
Do not separately fit S_3 or discard its mixed contribution.

| Remaining obligation | Exact scope |
| --- | --- |
| Wall existence and labels | Certified roots of S_1+cC_0=0, uniqueness/continuation on [epsilon,T], and paid wall uncertainty. |
| Side cancellation | Exact for the true phase wall; an approximate wall leaves (Q_x-w'Q)/E, including evaluator and path errors. |
| Boundary admissibility | Nonzero first jet on the actual boundary; Q!=0 on sides for the velocity coordinate. |
| Caps | Complete signed Q/E integration and branch tracking, or the justified same-gap label formula (6). |
| Endpoint or event | Retain the small cap or a paid connector/index; no automatic epsilon->0 deletion. |
| Source | Unchanged coefficients, complete reflection and tails, joint moments and simultaneous event matching if an event is posited. |
| Complex topology | A separate form and all oriented boundary faces are required for the complex Hopf/Chern problem; (5) does not pay I4-H01. |

The direct comparator gets the same wall locations, complete source data
and phase labels. With these labels it can also use (6). Thus the **exact
integral reduction** is established, while an advantage in acquisition cost,
error size or certified coverage remains unmeasured. That latter comparison
must count the cost of locating and certifying the phase walls; eliminating
a displayed integral does not make those inputs free.

**Next bounded simplification task:** select one existing topological integral
and a compact regular window, then compare its full boundary evaluation with
(5) using the same observations. Prove a reduced acquisition/error obligation,
or record an exact reduction without a cost claim. For a complex charge,
first identify its actual boundary form and the complete set of faces;
a real-jet phase cancellation cannot be substituted. This task is allowed
to proceed without proving endpoint noncollision.

## 4. Direct BW10/BW12 ancestry and the next complex face

This work continues **BW10 `10_rh_implies_simple_zeros`** and **BW12
`12_relative_chern_hopf_charges`**. The precise real-phase ancestor is
[BW10 Note 21, MT3–MT5][bw10-tubes]: rho=Q/E, j=Q_x/E and
rho_t+j_x=0. Equation (2) is exactly its moving-wall flux j-w' rho.
Interior walls do not replace the full adjacent-root cap for free. Under
the usual simple-gap product assumptions,
\[
 \int_a^{w_L}\rho\,dx=\pi/2-\arctan c_L,\quad
 \int_{w_L}^{w_R}\rho\,dx=\arctan c_L-\arctan c_R,\quad
 \int_{w_R}^b\rho\,dx=\pi/2+\arctan c_R.
\]
The three pieces still total pi. Thus the same-data cap-simplification is
explicit, with both omitted edge pieces paid, but it supplies no surplus
for BW10's RH-conditional simplicity argument.

BW10 Note 21 MT7–MT10 already reduces a different, fixed-time weighted
spatial tube to a transverse-derivative integral by a primitive/weight
cancellation. Its transverse faces and trace error are not canceled by
(2). Reuse that result and [Note 23's exact finite-time quadratic baseline][bw10-baseline]
for HMC-05, rather than restarting the completed HMC-04 reduction.

The genuinely complex target is [BW10 Note 25, MC6/MC9][bw10-chern], developed
in [BW12 Notes 17][bw12-connection] and [18, equation (11)][bw12-transport].
With G=(H,H_z), g=G/||G|| and A=-ig*dg, its three-form is
C=A wedge dA/(4pi²), and the complete face formula is
\[
 I_{\rm late}-I_{\rm early}+I_{\rm side}
             =\sum_p\binom{m_p}{2}.
\]
I_side includes both imaginary-heat faces and the complex-spatial outer
wall. These are three-dimensional faces, with compatible orientations and
corner data. The real-phase form (1) differs from A: indeed BW12 proves
A restricted to the physical real plane is zero while (1) need not be.

A concrete next simplification contract is a genuine three-dimensional
side whose projective image [H:H_z] lies in a fixed smooth real curve in
CP^1. The Hopf curvature is a two-form on CP^1, so its pullback to that
side vanishes; hence C also vanishes there. This elementary implication
is an available conditional cancellation mechanism, not a constructed
admissible theta boundary. Finding such a proper side, closing the domain,
keeping G nonzero and accounting for every other face remain open. A
nontrivial holomorphic equation H_z=cH has real codimension two at regular
points and cannot alone supply a three-dimensional side.

This is the specific bridge to I4-H01. Boundary-simplification analysis may
begin independently of noncollision; completing its quantitative theta
conclusion still requires the entire boundary estimate. [BW10's register][bw10-progress]
and [BW12's register][bw12-progress] keep HMC-05 open, HMC-06 gated and
FTSR-06/07 gated. No parent task is silently upgraded.

[program]: ../../research-overview/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRAM_20261022.md
[progress]: ../../research-progress/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRESS_20261022.md
[previous]: 02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[contract]: 03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md
[review]: ../reviews/03_SOURCE_CONTRACT_SURVIVOR_AND_BOUNDARY_REVIEW_20261022.md
[bw09]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coordinates]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md

[bw10-tubes]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[bw10-baseline]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md
[bw10-chern]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[bw10-progress]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[bw12-connection]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/17_PARALLEL_TRANSPORT_CONNECTIONS_AND_COLLISION_CONTROLS_20261021.md
[bw12-transport]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[bw12-progress]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md
