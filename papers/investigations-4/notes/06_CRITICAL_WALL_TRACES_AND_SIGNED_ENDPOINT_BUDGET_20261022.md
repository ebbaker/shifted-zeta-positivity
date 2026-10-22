# Critical-wall traces and the signed endpoint amplitude budget

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded authoring model
**gpt-6.1-sol (Codex), effort ultra**, verified from this turn's metadata.
Contributing-agent internal LLM checks; no specialist review or analytic
formalization.

**Status: proved in-note in the specified local, parameterized scope.**
There is a sharp spatial Gauss-area trace inequality, and a complete
complex-bulk-to-moving-curve comparison with the correct logarithmic
endpoint cost. The latter's specified local-Schur/total-mass certificate
loses to direct critical-value estimation. The coupled moment cancellation
does give an explicit bounded signed residual after subtracting 1/t;
its coefficient one remains compatible with an ordinary double. No
canonical-theta sign or exclusion margin is obtained.

This continues [Note 05][n5] under the existing [overview][overview] and
[CHB register][plan]. Read the [result index][results] and [avoid index][avoid],
particularly [heat geometry][geometry], [controls][controls],
[classification][a01], [matched premises][a02], [scope][a07],
[normalization][a08] and [coupled estimates][a12]. These are quantitative
trace and remainder estimates, not a new RH-equivalent criterion. The
inherited ICW subunit-logarithmic exclusion target is stated once in
[ICW Note 02 (8)–(10)][icw]; no checks here support its truth for theta.

## 1. Contract and actual signed consumer

Use H_tau=-H_zz, real H on the real slice, and the ordinary-double
matching H(0,a)=H_z(0,a)=0, h_2=H_zz(0,a)!=0. Take exactly
[Note 03's sufficient window][n3] and fixed physical jet frame. Write

\[
 h=|h_2|,\quad a_2=h-\epsilon_2\ge7h/8,\quad
 \eta=\epsilon_2+\epsilon_1 C_{\rm geom}/\delta_F\le h/4,
 \quad b=h-\eta\ge3h/4,\quad b_+=h+\eta.                 \tag{1}
\]

Here C_geom denotes Note 03's constant D_3+PD_2; it is not a source
moment. Its construction supplies the holomorphic critical graph c(tau),
|c-a|<=3R/8, |H_zz|>=a_2, |H_{z^j}|<=D_j for j=2,3,4, and

\[
 V(\tau)=H(\tau,c(\tau))=\tau B(\tau),\qquad
 |B+h_2|\le\eta,\quad b\le|B|\le b_+\quad(|\tau|\le d).
                                                               \tag{2}
\]

The proof of Note 03 gives this graph/unit bound on the heat disk of
radius d, before restriction to its rectangle W. For the product traces
below set t_*=d/4, so their auxiliary heat disks lie inside that rectangle.
No unknown positive endpoint value or internal zero separation is assumed.
The event is a conditional matching hypothesis, not an acquired theta event.

On the real critical wall c(t), 0<t<=t_*, define complete-source moments
mathsf C_j=int u^j exp(tu²)Phi(u)cos(c(t)u)du and
mathsf S_j=int u^j exp(tu²)Phi(u)sin(c(t)u)du. Then

\[
 \mathsf S_1=0,\quad V=\mathsf C_0,\quad
 V'=-H_{zz}=\mathsf C_2,\quad q=V'/V,\quad
 \sigma=\operatorname{sign}V=\operatorname{sign}B,
\]
\[
 \boxed{\sigma(\mathsf C_2-k\mathsf C_0)=|V|(q-k).}      \tag{3}
\]

Thus the signed amplitude consumer is an upper bound for q, or its
integral, on this **one-dimensional moving real curve**. Its direct
same-information baseline is

\[
 |q(t)|\le {D_2\over bt},\qquad
 \int_\epsilon^{t_*}|q(t)|dt
              \le {D_2\over b}\log(t_*/\epsilon).        \tag{4}
\]

Neither the trace theorem nor the endpoint estimates below assume RH.
In a different, declared all-real paired-product regime, that separate
theorem supplies q>0 in a simple gap. An unsigned square alone supplies
no such sign. For an upper budget, q<=|q| always remains valid.

## 2. Sharp spatial trace, including its denominator

On a zero-free disk |z-c|<=r at a fixed heat time, put p=H_z/H and
assume c is critical and |p|<=P. Then p(c)=0 and
g_2=|p_z|²/(1+|p|²)². The useful trace inequality is

\[
 \boxed{|q|^2\le{1+P^2\over\pi r^2}
                 \int_{|z-c|<r}g_2\,dA_z.}             \tag{5}
\]

**Proof.** Schwarz's lemma gives |p(c+w)|<=P|w|/r. The circle mean of
|p_z(c+w)|² at every radius s is at least |p_z(c)|²=|q|², by its
holomorphic Taylor series. Hence

\[
 \int g_2\,dA\ge |q|^2\,2\pi\int_0^r
                    {s\,ds\over(1+P^2s^2/r^2)^2}
             ={|q|^2\pi r^2\over1+P^2}.
\]

Equality holds for p(c+w)=alpha w with P=|alpha|r. The single factor
1+P² improves the direct unweighted-submean allowance (1+P²)². This is
a sharp analytic trace statement for the declared disk/range data. It is
not an exclusive advantage over a direct method allowed the same identity.

All denominator assumptions can be paid from the critical value:

\[
 |H(\tau,c+w)|\ge|V(\tau)|-D_2r^2/2>0,\qquad
 |p|\le{D_2r\over|V(\tau)|-D_2r^2/2}.                  \tag{6}
\]

Here H_z(c)=0 and the segment stays inside the paid spatial disk.
For example, r(t)=rho t gives a bounded P and an r^(-2) trace cost.
For r(t)=rho sqrt(t), if rho sqrt(t_*)<=5R/8 and
theta=D_2rho²/(2b)<1, (5)–(6) give, with
a(t)=pi^(-1)int_disk g_2,

\[
 q(t)^2\le a(t)\left\{{1\over\rho^2t}
                  +{D_2^2\over b^2(1-\theta)^2t^2}\right\}.
                                                               \tag{7}
\]

If a(t)<=a_* for all 0<t<=t_*, integration of the square-root bound yields

\[
 \int_\epsilon^{t_*}|q|\le\sqrt{a_*}\left\{
 {2(\sqrt{t_*}-\sqrt\epsilon)\over\rho}
 +{D_2\over b(1-\theta)}\log(t_*/\epsilon)\right\}.     \tag{8}
\]

The sharp trace avoids a spurious power divergence on that spatial scale.
But at a matching ordinary double, a_*>=1. Indeed, on z=c(t)+ty with
|y|<=C, the positive-time Taylor expansion gives
H=-h_2t+O_C(t²), H_z=h_2ty+O_C(t²), and H_zz=h_2+O_C(t).
Consequently g_2 dA_z tends to (1+|y|²)^(-2)dA_y. Every fixed inner
disk of radius Ct eventually lies inside rho sqrt(t); its normalized mass
tends to C²/(1+C²), and then to one as C increases. This proves the
needed positive-time special case directly. Thus the leading coefficient
of this particular uniform-area
certificate cannot improve (4). This is a failure of that comparison class,
not a prohibition of a source-dependent or signed localized estimate.

For H=z²-2tau and r=rho t, the exact limiting values are
a(t)->rho²/(1+rho²), P(t)->rho, and t|q|=1. Formula (5) captures exactly
the unit logarithmic coefficient in this limit. Finite spatial area does
not remove the endpoint budget.

## 3. Complete complex-bulk to moving-curve trace

To price the additional dimension loss, fix alpha=1/2, rho>0 with
rho t_*<=5R/8, and require

\[
 H_-=b(1-\alpha)-D_2\rho^2t_*/2>0.                       \tag{9}
\]

Such a rho exists. Define the shrinking complex tube

\[
 \mathcal U_t=\{|\tau-t|<\alpha t,
                       \ |z-c(\tau)|<\rho t\}\subset W.
\]

Its heat disks avoid tau=0 and fit inside the physical rectangle for
t<=d/4. The holomorphic change z=c(tau)+w has complex determinant one;
there is no omitted moving-wall Jacobian or swept-boundary claim here.
Use Note 04's exact definitions D_z=HH_zz-H_z²,
N_delta=|D_z|²+delta²(|H_z|²+|H_zz|²),
gamma_delta=N_delta/[pi(E+delta²)²], and
s_delta=delta²|J|²/[(E+delta²)N_delta]. They retain the mixed curvature.
Set

\[
 H_+=b_+(1+\alpha)+D_2\rho^2t_*/2,\quad
 P=D_2\rho/H_-,\quad U=H_+^2+D_2^2\rho^2,
\]
\[
 A=D_2H_++D_2^2\rho^2t_*,\quad
 N=A^2+\lambda^2D_2^2(1+\rho^2t_*^2),\quad
 c_*={\lambda^2 j_0^2\over(U+\lambda^2)N},\quad
 j_0=37h^2/64,
\]
\[
 \beta={SL^3\over\pi^2e_0^{5/2}},\qquad \delta=\lambda t,
 \quad\lambda>0.                                       \tag{10}
\]

S,L,e_0 are Note 03's **complete-boundary** constants. On this actual tube,
Taylor's formula and (2) give

\[
 H_-t\le|H|\le H_+t,\quad |H_z|\le D_2\rho t,\quad
 E\le Ut^2,\quad |D_z|\le At,\quad N_\delta\le Nt^2.
\]

Consequently Note 04's exact mixed-curvature Schur complement has
s_delta>=c_*/t². On the zero-free tube also

\[
 g_2\le\pi\left(1+{\lambda^2\over H_-^2}\right)^2\gamma_\delta.
                                                               \tag{11}
\]

Apply (5) on each complex-time spatial disk, and then the heat-disk
submean inequality to the holomorphic q(tau)=V'/V. This gives

\[
 |q(t)|^2\le{1+P^2\over\pi^2\alpha^2\rho^2t^4}
                       \int_{\mathcal U_t}g_2\,dV.
                                                               \tag{12}
\]

This displays the full spatial and heat trace loss, rather than inferring
a real trace from an average. Use (11), dmu_delta=(2/pi)s_delta gamma_delta dV,
and positivity on the **full** fixed window:
mu_delta(U_t)<=mu_delta(W)<=1+beta lambda²t². It follows that

\[
 \boxed{|q(t)|\le{C_{\rm top}\over t},\quad
 C_{\rm top}=\left(1+{\lambda^2\over H_-^2}\right)
 \sqrt{{(1+P^2)(1+\beta\lambda^2t_*^2)
                                  \over2\alpha^2\rho^2c_*}}.}   \tag{13}
\]

This is a proved local trace from the evaluated positive mass, with the
correct logarithmic integral C_top log(t_*/epsilon). The regulator depends
on the target t; each application uses a constant delta=lambda t on W.
No differentiation of that family is used in (13).

**Matched comparison.** In this specified certificate,
N>=lambda²D_2² and U>=D_2²rho² imply
1/c_*>=D_2^4rho²/j_0². Therefore, even discarding all other factors at
least one in (13),

\[
 {C_{\rm top}\over D_2/b}
 \ge {bD_2\over\sqrt2\alpha j_0}
 \ge {48\sqrt2\over37}{D_2\over h}>1.                  \tag{14}
\]

The local scaling has repaired the earlier global inverse-regulator
power loss, but this tube/local-Schur/**total-mass** certificate still
cannot improve the direct same-data bound (4). The comparison is between
certificate coefficients. A sharper acquired mass on U_t, another
weighted/signed observation or additional theta information is outside
this failure. Note 04's bounded mass remains valid independently.

## 4. Finite regularization retains an endpoint cost

On the actual real critical wall, the exact regularized trace is

\[
 \pi\gamma_\delta(t,c(t))={V'(t)^2\over V(t)^2+\delta^2},
 \qquad q^2=\left(1+{\delta^2\over V^2}\right)\pi\gamma_\delta.
                                                               \tag{15}
\]

Recovering q² costs up to 1+delta²/(b²epsilon²) on [epsilon,t_*].
For fixed delta, define the signed q_delta=VV'/(V²+delta²). Direct
integration, retaining the endpoint denominator, gives

\[
 \int_\epsilon^{t_*}(q-q_\delta)dt
 ={1\over2}\log{1+\delta^2/V(\epsilon)^2
                         \over1+\delta^2/V(t_*)^2}.      \tag{16}
\]

At fixed delta this restores the missing log(1/epsilon). If instead
delta(t)=lambda t, differentiating a regularized primitive adds
delta delta'/(V²+delta²). Its leading coefficient at the event is
lambda²/(h²+lambda²) times 1/t. Adaptive regularization must pay that
term or the equivalent bias multiplier in (15). It does not delete the
singular signed budget.

## 5. A bounded signed moment residual, without a hidden endpoint floor

Differentiate the critical graph and critical value using the heat
equation:

\[
 c'={H_{zzz}\over H_{zz}},\qquad
 V'=-H_{zz},\qquad
 V''=H_{zzzz}-{H_{zzz}^2\over H_{zz}},\qquad
 |V''|\le2K_0:=D_4+D_3^2/a_2.                           \tag{17}
\]

The mixed term is retained before taking the displayed fallback modulus.
As V(0)=0, B(t)=int_0^1 V'(st)ds and
B'(t)=int_0^1 sV''(st)ds, so |B'|<=K_0. With K=K_0/b,

\[
 \boxed{q(t)={1\over t}+r(t),\quad r=B'/B,\quad |r|\le K,}
\]
\[
 \boxed{\mathsf C_2-{\mathsf C_0\over t}=tB',\qquad
 \left|\mathsf C_2-{\mathsf C_0\over t}\right|\le K_0t.} \tag{18}
\]

This is an actual jointly cancelled source-moment estimate. It gives

\[
 \sigma\left[\mathsf C_2-\left(t^{-1}+K\right)\mathsf C_0\right]
 \le0,\qquad
 \left|\int_\epsilon^{t_*}q\,dt-\log(t_*/\epsilon)\right|
                         \le K(t_*-\epsilon).           \tag{19}
\]

The exact residual tends to log(|B(t_*)|/h), which is finite. With
a_*=min(eta,K_0t_*), its endpoint enclosure is
log(1-a_*/h)<=log(|B(t_*)|/h)<=log(1+a_*/h). These statements preserve
the coefficient one; they cannot supply ICW's strictly subunit coefficient.
The equally informed direct critical-value method derives (17)–(19)
exactly. Thus the bounded remainder is useful local estimation, but no
topological or new canonical-arithmetic advantage is claimed.

One can retain a signed center instead of paying the whole remainder
symmetrically. Cauchy on a radius-d/2 disk around real t<=t_* gives
|B''|<=8eta/d². Write h_j=H_{z^j}(0,a) for j=3,4 and define

\[
 K_1={8\eta\over bd^2}+K^2,\qquad
 r_0={h_3^2-h_2h_4\over2h_2^2}
 ={\mathsf C_4(0)\over2\mathsf C_2(0)}
        +{\mathsf S_3(0)^2\over2\mathsf C_2(0)^2}.       \tag{20}
\]

The event moments in (20) are evaluated at (0,a), with simultaneous
mathsf C_0=mathsf S_1=0 and mathsf C_2!=0. Then |r'|<=K_1 and

\[
 |r(t)-r_0|\le K_1t,\qquad
 \left|\int_\epsilon^{t_*}q\,dt-\log(t_*/\epsilon)
                      -r_0(t_*-\epsilon)\right|
                    \le {K_1\over2}(t_*^2-\epsilon^2).  \tag{21}
\]

In particular k(t)=t^(-1)+r_0+K_1t is a paid upper barrier in (3).
The sign of r_0 is not inferred from positivity of Phi; its coupled
numerator mathsf C_2 mathsf C_4+mathsf S_3² still needs actual source data.

For the square trace, both singular terms must be retained:

\[
 \boxed{|q(t)^2-t^{-2}-2r_0t^{-1}|\le2K_1+K^2.}          \tag{22}
\]

Subtracting t^(-2) alone can leave a nonintegrable 2r_0/t. The integrated
remainder in (22) has a finite endpoint allowance
(2K_1+K²)(t_*-epsilon). This explicitly identifies what the unsigned
square loses when used for a signed amplitude budget.

## 6. Wall and source acquisition costs

Use the unchanged canonical coefficients, full reflection and complete
mode/ray ledger in [source home 02][source]. No new theta acquisition is
performed here. The conditional value/derivative matching and real wall
are simultaneous inputs; separate head/tail bounds are not a sign proof.

For a real approximate critical location hat c with |hat c-c|<=omega, and
source evaluation errors varepsilon_j^src for mathsf C_j at hat c, Taylor's
formula gives the coupled-budget error allowance

\[
 E_k\le\varepsilon^{\rm src}_2+|k|\varepsilon^{\rm src}_0+D_3\omega
                                    +{|k|D_2\omega^2\over2}.    \tag{23}
\]

The quadratic wall error for C_0 uses H_z(c)=0. This bound presumes the
whole segment is paid by the same source contract; acquisition, tails
and rounding are included in varepsilon_j^src, distinct from (1)'s geometric
epsilon_2. An uncertain k adds its own
error times an upper bound for |C_0|. The sign sigma must be acquired or
supplied by (2), not selected after evaluating an unsigned norm.

For k=1/t+O(1), retaining an O(t) enclosure for the cancelled moment in
(18) is sufficiently paid by varepsilon_2^src=O(t), varepsilon_0^src=O(t²) and
omega=O(t). These are sufficient accuracy scales, not necessary ones,
not a runtime theorem, and not a claim that finite tolerance proves exact
event matching. A fixed absolute C_0 error is amplified by 1/t.

If r_0 is acquired with error e_r, (21)'s signed integral enclosure pays
an additional e_r(t_*-epsilon); the upper barrier uses hat r_0+e_r.
Subtracting an approximate 2r_0/t in the **square** trace instead costs
2e_r log(t_*/epsilon). A fixed positive uncertainty in that coefficient
does not certify a bounded renormalized-square endpoint integral. The
unsubtracted signed residual (18)–(19) does not need r_0 acquisition.

## 7. Controls and research disposition

The sharp trace and conditional local endpoint estimates are intended to
hold on matching collision controls; they supply no separating premise.
In addition to the quadratic, a useful exact heat control is

\[
 H=z^2-2t+\nu(z^4-12tz^2+12t^2),\quad
 c(t)=0,\quad V=-2t+12\nu t^2,
\]
\[
 q={1\over t}-{6\nu\over1-6\nu t},\qquad r_0=-6\nu.    \tag{24}
\]

For either sign of nu it has an ordinary double at zero; take a small
sufficient window to exclude other events. Its local charge is one in
both cases, while the signed center r_0 has opposite signs. The residual
2r_0/t in q² is therefore real information, not removable by positivity
of the bulk. These polynomials lack canonical theta arithmetic; no global
all-real regime is assigned to the quartic.

Apply the [control register][controls] with the same distinctions as
Note 05: H=z fails the ordinary-double/J-floor hypothesis; quadratic and
Hermite events pass the local laws; Euler-factor controls change the
canonical coefficients/completion; weighted-square and finite-prime
controls fail full normalized reflection/unchanged coefficients and are
not assigned an all-real heat slice; reflected super-Gaussian and smooth
positive-primitive controls lack the canonical integer-square theta
expansion. RH-conditional close endpoint controls fail ordinary Dirichlet
arithmetic. Counter-kernel formulas apply only at verified matching analytic
events. Smooth-density/two-channel controls remain screens for their own
full-Weil claims, with no new physical heat-jet bridge assigned here.

[Review 07][review] checks the derivations and scoped comparisons; the
[exact finite-algebra receipt][receipt] supports constants, regularization
and both-sign controls. Neither constitutes specialist validation.

**Disposition.** CHB-07's critical-wall follow-up has paid spatial and
complex-time trace costs, finite/adaptive regulator bias, and the ordinary-
double signed endpoint remainder. The positive-mass certificate (13) has
the right logarithmic scale but is dominated by direct same-data estimation
in (14). Equations (18)–(22) are reusable bounded residual estimates; they
retain the compulsory unit logarithmic coefficient. The next source task
is a genuinely sharper coupled signed enclosure using actual unchanged
theta data, or a localized mass/error estimate that beats its equally
informed direct baseline. No strict event-exclusion margin, higher-
multiplicity theorem, all-height result or theta acquisition is supplied.
CHB-07 remains active; CHB-04, CHB-05 acquisition and all inherited exclusion
gates retain their previous states. ICW's unpaid canonical signed estimate
is not completed by this generic local contract.

[n3]: 03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n4]: 04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[n5]: 05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md
[overview]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[source]: ../02_theta_source_constraints/README.md
[icw]: ../03_heat_transport_and_charges/notes/02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/07_CRITICAL_WALL_TRACE_AND_ENDPOINT_BUDGET_REVIEW_20261022.md
[receipt]: ../03_heat_transport_and_charges/numerics/CHB_CRITICAL_WALL_CHECKS_20261022.json
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
