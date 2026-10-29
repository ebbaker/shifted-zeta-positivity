# Auxiliary flows for collision analysis research overview

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

**Status: initial background overview for further brainstorming.** This
investigation explores modifications of the de Bruijn–Newman flow and
related auxiliary evolutions that could make zero collisions easier to
observe or constrain. The starting material comes from Investigation05's
[geometry discussion][n37] and [auxiliary source-flow assessment][n38].
No candidate flow, research plan, task sequence or numerical campaign has
been selected. The author has explicitly deferred planning until after
further brainstorming.

## Motivation and relationship to the earlier investigation

Investigation05 began with radial theta geometry and developed several
ways to represent or evolve the source while retaining access to its
spectral observation. The present direction takes the freedom to design
an auxiliary evolution as its central idea. A useful flow might turn a
collision into a pronounced response, expose information in a different
combination, or admit an estimate that is difficult to see in the original
formulation.

The dimension, geometry and generator remain open. Three-dimensional
radial structure is available when it contributes a useful relation, but
is not a premise of this investigation. Local differential terms,
nonlocal source perturbations and coupled fields all fit its scope.
The original conservative theta-flow program remains in Investigation05
with its existing task states; this investigation has no task register yet.

Two possible benefits should remain distinct. A better diagnostic could
resolve a collision or near collision more effectively at a stated cost.
An exclusion argument would additionally need independently established
information that prevents the relevant response for the canonical theta
source. Either can motivate research; amplification alone does not supply
the second.

## Canonical field and collision convention

Use the repository normalization
\[
H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
\qquad
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Then
\[
H_t=-H_{zz},\qquad
H(0,z)=\frac18\xi\!\left(\frac{1+iz}{2}\right).
\]
The complete source is positive on the half-line and has
double-exponential decay. The [reference guide][references] routes to the
checked Rodgers–Tao normalization and the Newman–Wu source-weighting
background, retaining their different conventions and inspection scopes.

The local calculations inherited here concern a nondegenerate real double
event
\[
H(T,a)=H_z(T,a)=0,\qquad A=H_{zz}(T,a)\ne0.
\]
Higher multiplicities, uniform height ranges and global threshold
conclusions are not established by these local formulas.

## What the previous auxiliary flows contribute

| Background | What is available | Limit retained here |
| --- | --- | --- |
| [Conserved-density heat, Note25][n25] | A collision removes leading diffusion modes of the marked value and derivative densities | A generic diagnostic under moment assumptions; it works in any dimension and admits colliding controls |
| [Feedback magnifier, Note28][n28] | A conservative feedback flow with a finite breakdown deadline at a marked collision, proved in-note with same-assistant checks | Global regularity reformulates pointwise noncollision; no independent theta bound preventing breakdown |
| [Positive carrier, Note29][n29] | Quantitative regularity from an independently known first-jet margin | The comparison does not acquire that margin or enlarge its already separated theta domain |
| [Linear combined flow, Brainstorm08][b08] | An exact solution of the specified Newman/cylinder-heat combination | Its zeros are the original heat zeros after a nonvanishing factor and coordinate/time rescaling |
| [Source perturbations, Note38][n38] | General local response identities, a bounded cosine perturbation and an exact positive-source control | No demonstrated improvement in sensitivity, cost or collision exclusion |

These findings motivate freedom to change the flow and observable
together. They do not select the earlier feedback construction as the
default continuation or rule out other geometric estimates.

## Two parameters retain a clear connection to the original problem

A convenient source-defined family from Note38 is
\[
F(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+s q(u)}\cos(zu)\,du.
\tag{1}
\]
Here t remains Newman time and s is a new auxiliary parameter. For bounded
real even q, the theta tail makes F entire in t,s,z; F is even in z and
real on the real axis for real t,s. Its physical slice is exactly
F(t,0,z)=H(t,z), and F_t=-F_{zz} throughout the family.

The new source remains positive for real s. This does not transfer
Newman's all-real-zero monotonicity to the s direction. A deformation
that changes zeros needs a justified comparison back to the physical
slice. An evolution that preserves the complete observation, or preserves
zeros through a known nonvanishing factor, has a different role. These
possibilities remain available without being identified with each other.

Define the initial auxiliary response
\[
R_q(t,z)=F_s(t,0,z)
=\int_0^\infty q(u)\Phi(u)e^{tu^2}\cos(zu)\,du.
\]
At a simple zero, its motion under s is
\(z'(0)=-R_q/H_z\). Near the double event, writing
\(\tau=t-T\) and \(\eta=z-a\), the leading expansion is
\[
F(t,s,z)=\frac A2\eta^2-A\tau+sR_q(T,a)+\text{higher terms}.
\tag{2}
\]
More precisely, the squared gap D of the two nearby zeros is analytic and
satisfies
\[
D(t,s)=8\tau-8\frac{R_q(T,a)}A s
+O\bigl((|\tau|+|s|)^2\bigr).
\tag{3}
\]
The nearby curve of double events has T'(0)=R_q(T,a)/A. These inherited
identities describe a response; they do not bound it. The source note
contains the remainder, implicit-function calculation and qualifications.

## Candidate examples already discussed

The following are mathematical examples, not a selected program.

| Source weight q | Auxiliary equation or effect | Interpretation |
| --- | --- | --- |
| 1 | F_s=F | Changes amplitude |
| u^2 | F_s=-F_zz | Replaces t by t+s |
| u^4 | F_s=F_zzzz | A local higher-order direction; its response can vanish at a double event |
| cos(au), with a fixed | F_s=(F(z+a)+F(z-a))/2 | A bounded nonlocal direction with a positive response at the mark |

The quartic case also converges for all complex parameters for the
canonical theta source. Following s=epsilon*t gives
\[
\widetilde F_t=-\widetilde F_{zz}
+\epsilon\widetilde F_{zzzz},\qquad
\widetilde F(0,z)=H(0,z).
\]
This makes a natural local modification concrete. The quadratic heat
model z^2-2t has a double event and zero fourth derivative, so higher
derivative order by itself is not a guaranteed collision signal. In
addition, multiplying a Gaussian-tail control by e^{su^4} is not an
admissible two-sided perturbation at s=0; its integral diverges for s>0.

For regular holomorphic evolutions with terms b(t,z)F_z+c(t,z)F, both
added terms vanish at a double event. They retain the leading local
heat splitting, although nonconstant coefficients can change global
dynamics and higher terms. Constant drift bF_z translates the argument;
linear drift bzF_z dilates it with a time change. With constant b,c,
the two explicit solutions are respectively
\[
e^{c\tau}H(\tau,z+b\tau),\qquad
e^{c\tau}H(\sigma(\tau),e^{b\tau}z),\quad
\sigma'=e^{2b\tau},\quad\sigma(0)=0.
\]
The corresponding distinction has been corrected in Note38. These are
scoped comparisons, not exclusions of general drift, potential, nonlinear
or coupled constructions.

## The bounded cosine response

For q_a(u)=cos(au), fix a>0 independently of s and of the running
spectral variable z. The exact auxiliary equation is
\[
F_s(t,s,z)=\frac12\{F(t,s,z+a)+F(t,s,z-a)\}.
\tag{4}
\]
At the mark, the first response is
\[
P_a(t):=F_s(t,0,a)
=\int_0^\infty\Phi(u)e^{tu^2}\cos^2(au)\,du
=\frac{H(t,0)+H(t,2a)}2>0.
\tag{5}
\]
Strict positivity follows from the positive continuous density; also
\(P_a(t)\le H(t,0)\). Since \(|q_a|\le1\), the source perturbation costs at most
e^{|s|} in absolute majorants, and its difference from the original source
costs at most e^{|s|}-1. The generator contains no inverse zero value or
inverse first derivative.

At a double event, equation(3) gives
\[
(z_+(s)-z_-(s))^2=-8\frac{P_a(T)}A s+O(s^2).
\tag{6}
\]
This gives a definite square-root unfolding. The same exponent already
occurs in Newman time, where D_t=8. Positivity of P_a holds away from
collisions too, so it is not by itself a collision certificate. The
response ratio still contains A, and a different mark generally requires
a different auxiliary flow.

On the single path s=epsilon*t, this example becomes
\[
\widetilde F_t=-\widetilde F_{zz}
+\frac\epsilon2\{\widetilde F(t,z+a)+\widetilde F(t,z-a)\},
\qquad \widetilde F(0,z)=H(0,z).
\tag{7}
\]
Keeping the parameters separate first makes the original slice and the
auxiliary response explicit. Neither form is selected as the eventual
research flow.

## Controls and interpretation

Note38 evaluates the cosine response exactly on the positive control
\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\qquad
T_c=\tfrac14,
\]
whose double event is at \(a=2\sqrt6\). With \(C=\sqrt\pi/16\), its curvature
and response are
\[
A=12Ce^{-3/2},\qquad P_a=C(18+162e^{-6})>0.
\]
This is a successful diagnostic response on an admitted colliding source.
The control lacks canonical square arithmetic and the theta tail, but
fails no premise of the bounded-tilt calculation.

The [control register][controls] and Note38's family screen retain the
other distinctions: Euler-factor controls alter the canonical factors;
weighted-square and finite-prime controls lack complete coefficients or
full reflection; reflected and positive-primitive controls lack canonical
square arithmetic. Their admitted positive continuous sources share the
cosine-response calculation. Atomic measures require a support check for
strict positivity. No separating theta estimate has yet been acquired.

An improved diagnostic would need a quantitative advantage after
normalization, error growth and evaluation cost are accounted for. An
exclusion would require additional information specific to the complete
canonical source. Replacing that missing information by a global
regularity assertion equivalent to noncollision would return to the
earlier reformulation. These distinctions frame the brainstorming without
fixing a target inequality, preferred flow or sequence of tasks.

The [result index][results], particularly [heat flow][heat],
[collision controls][controls] and [geometric realizations][geometry],
and the [avoid index][avoid] are the common background. The specific
guidance on [target classification][a01], [control premises][a02],
[coordinate changes][a03] and [scoped conclusions][a07] applies.
The inherited calculations have the same-assistant checking stated in
their source notes; this overview adds no independent mathematical review.

## Source and conversation continuity

The original notes and reference annotations remain in Investigation05.
This investigation links to them and will hold subsequent work developed
for this direction. Its [folder guide][root] and [reference guide][references]
provide the entry points.

The founding conversation, *Assess auxiliary flow strategy*, retains its
unique Investigation05 chat0017 registration; [the history guide][history]
links to that archive. New dedicated conversations belong here. A research
plan and progress register are intentionally deferred until the author
has continued the brainstorming.

[root]: ../README.md
[history]: ../chat-histories/README.md
[references]: ../references/README.md
[n25]: ../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n28]: ../../05_radial_theta_collision_geometry/notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../../05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n37]: ../../05_radial_theta_collision_geometry/notes/37_GEOMETRY_DISCUSSION_AND_RETURN_CONTINUATION_20261028.md
[n38]: ../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[b08]: ../../05_radial_theta_collision_geometry/brainstorm/08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
