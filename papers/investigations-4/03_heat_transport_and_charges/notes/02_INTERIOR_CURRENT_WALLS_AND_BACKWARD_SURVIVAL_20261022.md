# Interior current walls: what backward survival would prove

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn’s metadata.

**Status: conditional transport lemmas and analytic control screen;
no new theta estimate or collision exclusion.** This follows the user’s
suggestion to start between zeros and move with a current. It extends
[I4-H00’s root-wall screen][previous]. Read the [result index][results],
[avoid index][avoid], [control register][controls] and [target-classification
rule][a01]. The conditional criteria below specify the missing work; they
are not themselves estimating progress. See the [review][review].

## 1. Choose the observable before choosing the current

Use H_t=-H_xx, with H real on the real axis and sufficiently smooth.
This is the standard [de Bruijn–Newman convention][rt]; ordinary diffusion
runs toward decreasing t. Set
\[
 p=H_x/H,\qquad Q=H_x^2-HH_{xx},\qquad q=Q/H^2=-p_x
\]
where H is nonzero. Three different wall velocities arise:

| Observable | Cancelling velocity w' | Domain |
| --- | --- | --- |
| Scalar energy density H² | v_0=2H_x/H=2p | H nonzero |
| Jet energy density H²+H_x² | v_J=2H_x(H+H_xx)/(H²+H_x²) | Nonzero first jet |
| Phase of H+iH_x | v_theta=Q_x/Q | Q nonzero and nonzero first jet |

For scalar energy, the exact balance is
\[
 \partial_t(H^2)+\partial_x(2HH_x)=2H_x^2.
\]
The contribution of a moving endpoint is H²(w'-2p), so v_0 cancels it.
For two such endpoints,
\[
 \frac d{dt}\int_{w_-}^{w_+}H^2dx=2\int_{w_-}^{w_+}H_x^2dx.       \tag{1}
\]
This is a balance with a source term, not conserved scalar mass. Its
forward positivity does not imply a positive limit toward earlier time.
The jet-energy formula follows by adding the corresponding H_x² balance.
The phase current Q_x/Q is **inherited** from [BW09 Note 06 §3][phase].
These velocities generally differ: one cannot transfer their cancellations
or their continuation properties from one observable to another.

## 2. Two surviving scalar-current paths give a gap lower bound

Suppose a(t)<b(t) are consecutive simple real zeros for 0<t<=T, with
H nonzero between them. Assume Q>=0 throughout that gap. This hypothesis
holds under the established real-root product assumptions, since
\[
 q(t,x)=\sum_r\frac1{(x-r(t))^2}>0.                         \tag{2}
\]
The sum and its convergence are those of [BW10 CP1][product]; no such
sign is asserted for arbitrary real heat solutions or unknown nonreal
regimes. For an RH-conditional simplicity application the all-real regime
is an explicit hypothesis, not a proof of RH.

**Conditional two-path lemma.** If two distinct scalar-current solutions
w_-(t)<w_+(t) exist throughout 0<t<=T and remain strictly inside this same
gap, then
\[
 \boxed{b(t)-a(t)>w_+(t)-w_-(t)\ge w_+(T)-w_-(T)>0.}        \tag{3}
\]
Indeed v_0,x=2p_x=-2q<=0, so
\[
 \frac d{dt}(w_+-w_-)
 =v_0(t,w_+)-v_0(t,w_-)\le0.
\]
Separation is therefore nondecreasing as t decreases. A finite endpoint
collision of these roots is impossible. Strict interior inequalities at
positive times suffice; a positive distance from each root need not be
assumed in (3).

Thus proving backward survival for an interval of starting positions,
or merely two distinct positions, would give a substantive noncollision
argument. Proving survival of **one** path would not. The hard input is
existence inside the gap all the way down to zero: v_0 is singular at
root boundaries, and ordinary local ODE uniqueness does not provide it.
The theorem gives no new theta survival estimate by itself.

For a general velocity v, two trapped paths instead satisfy d'=A(t)d,
where A is the average of v_x over their joining segment. An upper bound
v_x<=k(t), with k_+ integrable down to zero, gives
\[
 d(t)\ge d(T)\exp\left(-\int_t^T k_+(s)ds\right)>0.          \tag{4}
\]
Only an upper bound is needed. Scalar current already has k=0 under (2);
other currents may have nonintegrable backward compression.

## 3. Exact control: scalar-current paths can hit a root before zero

Take H=x²-2t, with roots ±sqrt(2t). The central path w=0 is a
scalar-current solution for every t>0. It remains strictly between the
roots even though they collide at t=0. It also stays at the same positive
fraction of the gap from both endpoints; relative interiority is not an
absolute gap floor.

For an initial point 0<x_T<sqrt(2T), scalar current is
\[
 x'=\frac{4x}{x^2-2t}.
\]
On its backward branch, inversion gives
\[
 \frac{dt}{dx}+\frac{t}{2x}=\frac x4,
 \qquad t=\frac{x^2}{10}+\frac C{\sqrt x},\quad
 C=\sqrt{x_T}\left(T-\frac{x_T^2}{10}\right)>0.              \tag{5}
\]
As time decreases, x increases until it hits the right root at
\[
 x_*=(5C/2)^{2/5},\qquad t_*=x_*^2/2>0.
\]
The initial interior condition gives x_T<x_*; t(x) decreases to t_*.
Reflection treats negative initial points. Hence **only the central
scalar-current path survives to zero in this control**. This identifies
precisely why the two-path premise fails, despite Q>0 and exact energy
flux cancellation. Forward trapping cannot be substituted for the
backward survival needed in (3).

## 4. Phase paths can all stay between the zeros and still collapse

Under (2), p decreases from +infinity to -infinity across a simple gap.
For every fixed real c there is exactly one interior p=c wall. Implicit
differentiation gives
\[
 w_c'=Q_x/Q=2c+p_{xx}/p_x.
\]
It cancels real-jet wall phase and continues over any compact regular
simple-gap interval. This is distinct from scalar current, which would
require w'=2c on the same path.

For H=x²-2t these walls are explicit:
\[
 w_c(t)=\frac{-2ct}{1+\sqrt{1+2c^2t}},\quad w_0=0,
 \qquad w_c'=-\frac c{\sqrt{1+2c^2t}}.                     \tag{6}
\]
They all remain between the roots and have bounded speeds, but collapse
together at t=0. Their amplitudes are
\[
 H(t,w_c)=-\frac{4t}{1+\sqrt{1+2c^2t}}\longrightarrow0.
\]
Two distinct labels have separation of order t; phase velocity has
v_theta,x(t,0)=1/t. Thus the integrability condition in (4) fails.
Bounded velocity is not bounded distortion of a family of trajectories.

This is universal locally at an **ordinary double of a real-analytic
heat field**. If H=H_x=0 and
H_xx=h_2!=0 at (0,a), set h_3=H_xxx(0,a). The equation
F_c=H_x-cH=0 has F_c,x=h_2, so the analytic implicit-function theorem
provides a regular wall through the event. Uniformly for bounded c,
\[
 w_c(t)=a+(h_3/h_2-c)t+O(t^2),\quad
 H(t,w_c)=-h_2t+O(t^2),\quad \partial_cw_c=-t+O(t^2).        \tag{7}
\]
The born roots lie a±sqrt(2t)+O(t), so these phase walls are interior for
small t>0. Also q(t,w_c)=1/t+O(1). Smooth wall continuation is therefore
compatible with the event itself; the first jet and the separation of
wall labels vanish. Higher multiplicities are not covered by (7).

## 5. A source estimate that could bolster the construction

The strongest immediate version of the user’s scalar-current idea is to
prove (3)’s backward survival for **two paths**, using unchanged theta
data without assuming an unknown positive H floor or root gap. A second,
related approach is to preserve the amplitude on an interior phase wall.
For p=c define
\[
 B_c(t)=e^{-cw_c(t)+c^2t}|H(t,w_c(t))|.
\]
A direct chain rule gives
\[
 (\log B_c)'=q(t,w_c),\qquad
 B_c(\varepsilon)=B_c(T)
       \exp\left(-\int_\varepsilon^Tq(t,w_c(t))dt\right).   \tag{8}
\]
A finite uniform bound on this integral, with bounded w_c, would preserve
positive endpoint amplitude and prevent collapse of the enclosing pair.
For an ordinary double, even the weaker estimate
\[
 \int_\varepsilon^T q(t,w_c(t))dt
 \le\kappa\log(T/\varepsilon)+C,\qquad \kappa<1,             \tag{9}
\]
would contradict (7). Both conditions fail for the quadratic. Equation
(8) is exactly a normalized amplitude ratio, so restating it is not a
new estimate. No theta bound of type (8) or (9) is obtained here.

The simplest source-facing pilot is c=0, the unique critical point in a
real-root gap. Its motion and V'=-H_xx were already recorded in
[BW09 Note 05 §4][critical]. With the complete cosine source write
\[
 C_j(t,x)=\int_0^\infty u^j e^{tu^2}\Phi(u)\cos(xu)du,
 \qquad S_1(t,x)=\int_0^\infty u e^{tu^2}\Phi(u)\sin(xu)du.
\]
Then H=C_0, H_x=-S_1, H_xx=-C_2; on the critical wall S_1=0 and
q=C_2/C_0. A signed bound q<=k(t), with the sign sigma=sign C_0 fixed,
is equivalent to the **coupled** bound
\[
 \sigma\{C_2-k(t)C_0\}\le0\quad\text{subject to }S_1=0.     \tag{10}
\]
Any useful proof must keep the same theta coefficients, complete reflection,
full tails, wall uncertainty and any event matching. Separately bounding
C_2 and dividing by an assumed lower bound for C_0 would assume the missing
amplitude. The direct same-information comparator is (8), or direct
endpoint/gap evaluation; no advantage is yet established.

**Next task:** use the I4-S01 source work to seek one explicit, complete
backward-survival or coupled amplitude estimate, with a declared wall,
time window and matched direct comparator. Screen it analytically before
starting a numerical tracking campaign. Two-path survival is the desired
extra input, not a consequence of vanishing flux. I4-H01’s full complex
boundary/charge estimate remains gated.

The quadratic lacks theta arithmetic. The existing atomic threshold family
also has a central interior critical/phase path with vanishing amplitude,
while failing unchanged canonical theta data. Euler-factor controls alter
canonical arithmetic; weighted-square/finite-prime controls lack full
normalized reflection; reflected/primitive controls lack canonical square
coefficients. No new event locations or wall continuations are assigned
to those families. The [scope rule][a07] and [coupled-estimate rule][a12]
apply; this is a bounded refinement of I4-H00, not a universal obstruction
to moving-boundary arguments or a new RH-equivalent criterion claimed as progress.

[previous]: 01_ZERO_FOLLOWING_BOUNDARIES_AND_REMAINING_FLUX_20261021.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[phase]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[critical]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[product]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md
[rt]: https://arxiv.org/html/1801.05914
[review]: ../reviews/02_INTERIOR_CURRENT_WALL_REVIEW_20261022.md
