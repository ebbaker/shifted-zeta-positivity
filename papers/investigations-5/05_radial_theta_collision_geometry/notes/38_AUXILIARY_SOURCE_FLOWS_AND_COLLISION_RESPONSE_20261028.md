# Auxiliary source flows and collision response

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Investigation05, chat0017, *Assess auxiliary flow strategy*.

**Status: exploratory assessment with direct local calculations.** Designing
an auxiliary flow is a plausible reusable direction from [Note37][n37].
The bounded cosine perturbation below gives a nonzero unfolding direction
at every marked nondegenerate real collision of a positive continuous
source. It supplies neither a theta collision exclusion nor a demonstrated
improvement over the original heat response. No flow is selected for a
research campaign, and the CTF register and manuscripts are unchanged.

This follows the [result index][results], especially [collision
controls][controls] and [geometric realizations][geometry], and the
[avoid index][avoid], especially [target reformulations][a01],
[shared control premises][a02], [coordinate changes][a03] and
[scoped conclusions][a07]. The proposed milestone is a useful diagnostic
or estimate with a measured comparison, not another equivalent global
regularity condition.

## 1 What the earlier auxiliary flow achieved

[Note28][n28] makes a marked collision produce finite auxiliary-time
breakdown of a conservative feedback flow. That is a real amplification
construction. Its regularity equivalence is not an independent exclusion.
[Note29][n29] obtains regularity estimates from an already available lower
bound on the original value/derivative pair; it does not obtain that bound.
A different auxiliary evolution remains open. Its benefit need not depend
on dimension three or on retaining that particular feedback.

Two useful objectives are distinguishable: an observable with a clearer
or cheaper collision response, and an independently controllable quantity
whose bound would constrain collisions. A successful diagnostic may be
generic; an exclusion must use a premise that actually separates the
canonical source from the admitted colliding controls.

## 2 Screen simple additions before choosing a flow

Use the established normalization
\[
H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
\qquad H_t=-H_{zz}.
\]
The primary normalization check is recorded in [Reference14][ref14].
At a nondegenerate double event, write
\[
H(T,a)=H_z(T,a)=0,\qquad A=H_{zz}(T,a)\ne0.
\]
For a proposed regular equation
\[
F_\tau=-F_{zz}+b(\tau,z)F_z+c(\tau,z)F,
\]
the added terms vanish at a double event. Its leading local splitting
still satisfies \((z-a)^2\sim2(\tau-\tau_*)\). This is only a statement
about the leading local law: nonconstant coefficients can change global
motion, higher terms and energy estimates.

For constant b,c the reduction is stronger and exact:
\[
F(\tau,z)=e^{c\tau}H\bigl(\sigma(\tau),e^{b\tau}z\bigr),
\qquad \sigma'=e^{2b\tau},\quad\sigma(0)=0.
\]
These terms rescale amplitude, position and time. Likewise, the particular
quadratic-potential combination already solved in [Brainstorm08,
Section7][b08] transports the old zeros by an explicit Gaussian factor and
rescaling. Neither calculation excludes other drift, potential or coupled
equations. A smooth nonlinear addition N(F,F_z) with N(0,0)=0 also vanishes
at the event; singular feedback requires its own independent bounds.

## 3 Keep the new parameter separate from Newman time

For a prescribed real even weight q, define
\[
F(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+s q(u)}\cos(zu)\,du.
\tag{1}
\]
For bounded q this is entire in t,s,z for the canonical theta source,
by uniform domination on compact parameter sets. It remains even in z
and real on the real axis for real t,s. The physical slice is exactly
F(t,0,z)=H(t,z), and F_t=-F_{zz}. Positivity of the source survives for
real s; the all-real-zero monotonicity of Newman time is not thereby
established in s.

Let
\[
R_q(t,z)=F_s(t,0,z)
=\int_0^\infty q(u)\Phi(u)e^{tu^2}\cos(zu)\,du.
\]
At a simple zero x(s), differentiation gives
\[
x'(0)=-R_q(t,x(0))/H_z(t,x(0)).
\tag{2}
\]
Near a double event, with \(\tau=t-T\), \(\eta=z-a\), the leading
expansion is
\[
F(t,s,z)=\tfrac A2\eta^2-A\tau+sR_q(T,a)
+O\bigl(|\eta|^3+|\eta|(|\tau|+|s|)+(|\tau|+|s|)^2\bigr).
\tag{3}
\]
The analytic squared gap D of the two nearby zeros therefore has
\[
D(t,s)=8\tau-8\frac{R_q(T,a)}A s
+O\bigl((|\tau|+|s|)^2\bigr).
\tag{4}
\]
One can justify D through the local degree-two Weierstrass factor, so
the formula does not require individually differentiable roots at the
event. The implicit function theorem also gives a local curve of real
double events \((T(s),a(s))\), since the Jacobian of (F,F_z) in (t,z)
has determinant \(-A^2\). Its derivatives are
\[
T'(0)=\frac{R_q}A,\qquad
a'(0)=\frac{H_{zzz}R_q}{A^2}-\frac{\partial_zR_q}A,
\tag{5}
\]
with all terms evaluated at (T,a). These are response identities, not
bounds on the response. The case q=1 only changes amplitude; q=u^2
only replaces t by t+s and gives T'(0)=-1.

## 4 A bounded perturbation with guaranteed response at the mark

Fix a real mark a>0, independently of s and of the running spectral
variable z, and take
\[
q_a(u)=\cos(au),\qquad |q_a|\le1.
\]
The cosine product identity gives the exact auxiliary equation
\[
F_s(t,s,z)=\tfrac12\{F(t,s,z+a)+F(t,s,z-a)\}.
\tag{6}
\]
At the mark its initial response is
\[
P_a(t):=R_{q_a}(t,a)
=\int_0^\infty\Phi(u)e^{tu^2}\cos^2(au)\,du
=\tfrac12\{H(t,0)+H(t,2a)\}>0.
\tag{7}
\]
Strict positivity uses the positive continuous theta density, not merely
nonnegativity of an arbitrary measure. Also \(P_a(t)\le H(t,0)\).
The bounded source tilt costs at most a factor e^{|s|} in absolute
source majorants; the factor for the source difference is at most
e^{|s|}-1. Thus the perturbation has a fixed normalization and controlled
source growth, without dividing its generator by H or H_z.

At a nondegenerate collision (T,a), equations(3)–(4) now give a definite
square-root splitting under s:
\[
(z_+(s)-z_-(s))^2=-8\frac{P_a(T)}A s+O(s^2).
\tag{8}
\]
This demonstrates an actual response. Positive P_a is not itself a
collision detector: it is positive away from collisions as well. Newman
time already has square-root splitting, D_t=8, so no better exponent or
signal-to-error ratio is established. The ratio P_a/A still needs control.
Different marks generally require different auxiliary flows; there is no
claim of one simultaneously adapted flow at every height.

If a single modified time equation is desired, the path s=epsilon*t
through(1) obeys
\[
\widetilde F_t=-\widetilde F_{zz}
+\tfrac\epsilon2\{\widetilde F(t,z+a)+\widetilde F(t,z-a)\},
\qquad \widetilde F(0,z)=H(0,z).
\tag{9}
\]
This is a nonlocal addition to backward heat. Keeping t,s separate first
makes the connection to the original family easier to track.

For a strictly local alternative, q=u^4 gives F_s=F_{zzzz} and the
single-path equation \(\widetilde F_t=-\widetilde F_{zz}
+\epsilon\widetilde F_{zzzz}\). Theta's double-exponential tail makes
this source integral entire in the parameters too. But R_q=H_{zzzz}
need not be nonzero at a double event: the quadratic heat model
z^2-2t has zero fourth derivative. Higher derivative order alone provides
no guaranteed enhancement. The same quartic exponential is not a
two-sided deformation of a Gaussian-tail control, whose integral diverges
for s>0. The bounded cosine tilt avoids that domain mismatch.

## 5 Collision controls and the bounded next question

The response identities apply to every analytic source family satisfying
their stated integrability and nondegeneracy conditions. They should
respond to controls, rather than falsely exclude them.

For a direct exact check, use Note29's positive control with Tc=1/4:
\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\quad
H_*(T_c,z)=C(z^2/4-6)^2e^{-z^2/16},\quad C=\sqrt\pi/16.
\]
At \(a=2\sqrt6\), its curvature is
\(A=12Ce^{-3/2}\), while the cosine-tilt response is
\(P_a=C(18+162e^{-6})>0\). Hence its collision curve has
\[
T'(0)=\tfrac32e^{3/2}+\tfrac{27}2e^{-9/2}>0.
\]
The bounded tilt is analytic around that event on t<4+Tc. This control
lacks canonical square arithmetic and the theta tail, but fails no
premise of the proposed diagnostic.

| Control family | Response calculation and distinguishing premise |
| --- | --- |
| Euler-factor controls | The bounded tilt preserves admissibility; at any nondegenerate real event(7) is positive. Canonical Euler factors/conductor fail, not a diagnostic premise. |
| Weighted-square and finite-prime controls | Their admitted smooth source integrals obey the same formulas. Complete canonical coefficients or full reflection fail; neither is used to sign(7). Their lack of an all-real time is irrelevant to this local calculation. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Positivity and local analytic integrability give the same response. Canonical square arithmetic fails; the detector does not use it as a separator. |
| Atomic controls | The shift identity holds on the moment domain; strict positivity needs a separate support check. At a marked zero of a source having positive mass at u=0, the cos-squared integral is positive. No blanket density argument is applied to all measures. |
| Quadratic heat model | Admits the PDE/local calculation, but is outside the positive integrable theta-source class; it screens the claim that a fourth derivative must detect a double event. |

The family screen is analytical; previous certified witnesses are not
recomputed. The Gaussian control is evaluated exactly above. No control
fails an acquired theta-specific response estimate, since none is yet
proposed.

The next useful question is whether a fixed, normalized auxiliary
direction supplies a sharper or cheaper *controlled* response than the
original heat direction or direct (H,H_z) evaluation, or yields an
independent estimate from the complete theta source. The comparison must
include source/error growth and the cost of any curvature denominator.
Geometry becomes useful if it supplies that estimate. This gives a small
testable starting point without selecting a dimension or reopening the
old feedback-regularity criterion.

All displayed new calculations were checked by the same assistant;
no independent specialist review or novelty claim is made.

[n37]: 37_GEOMETRY_DISCUSSION_AND_RETURN_CONTINUATION_20261028.md
[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[b08]: ../brainstorm/08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md
[ref14]: ../references/14_NEWMAN_FLOW_AND_SOURCE_PERTURBATION_REFERENCES_20261028.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
