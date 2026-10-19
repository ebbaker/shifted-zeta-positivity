# Second transverse completion and current feasibility

19 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Analytic derivation and scoped counterexamples, with exact
algebra checks and a separate same-model internal review. No specialist
human review.

## Decision and observation contract

**S06-T1 is complete as a scoped closure of the second transverse-current
sign and physical-energy magnitude-payment attempt. Its feasibility gate
for S06-T2 is not passed.** The next transverse order has a unique complete
source in the declared one-parameter correction class. Its observation
contains a second physical derivative, and its centered current contains
both a derivative of the Laguerre expression and the next Laguerre
expression. At a nondegenerate physical collision the observation is
nonzero and the centered current is strictly positive. Thus these favorable
auxiliary signs do not exclude the events they were intended to detect.

This is a finite-order feasibility result, rather than an RH-equivalent
criterion or a new theta sign estimate. Interpret it using the
[result summaries][summaries] and [patterns to avoid][avoid], particularly
[collision controls][controls], [geometric realizations][geometry],
[reformulations][a1], [shared control premises][a2],
[scope of negative results][a7], and [separate-bound losses][a12].

| Contract item | Fixed choice |
| --- | --- |
| Additional input | Second base-p insertion in the existing source extension, multiplied by q squared, with one full primitive correction |
| Completion class | q squared times the second insertion plus c(D-1)psi, with constant real c |
| Physical map | One half of the full-line transform with the original exp(tu squared) heat weight |
| Candidate consumers | Completed current positivity, including a lower bound by delta E; a finite local magnitude payment by E |
| Exact target | H, Hx, E=H squared+Hx squared; retain higher derivatives explicitly |
| Domain | Every t>0 and real x; the old pilot B is a reference, not a new computation domain |
| Boundary and product rules | Recombine the source before integration; preserve all four product terms, primitive lower edges and corner |
| Gate | A new independently estimable arithmetic term or a scoped closure of this attempt |

The [previous S06 note][previous] gave C1=(9-D)Phi/4 and
J1c=(9t/8)L0. The present calculation uses C2, rather than renaming that
known identity. No source quadrature, finite spectral cutoff or new
physical certification is needed for this feasibility decision.

## Exact source completion and its convergence

Use the same marked extension as [Note 01][opening]:

\[
 q=e^{4u},\quad D=\partial_u,\quad
 \psi(u,p)=e^u\sum_{n\ge1}e^{-\pi n^2(q-ip)},\quad
 \mathcal S=\tfrac18(D^2-1)\psi,\quad \mathcal S(u,0)=\Phi(u).
\]

Write psi(u)=psi(u,0), and define the second real insertion
\(g_2=(-i\partial_p)^2\mathcal S|_{p=0}\). The existing general base-p
formula, including its shifted D coefficients, gives

\[
 A_2:=q^2g_2=\frac{P_4(D)}{128}\psi,\qquad
 P_4(D)=(D-1)(D-5)(D-7)(D-9).
 \tag{1}
\]

Theta reflection is exactly
\(\psi(-u)=\psi(u)+\sinh u\). Hence at the negative cusp

\[
 \psi(u)=\tfrac12e^{-u}-\tfrac12e^u+
 \text{a remainder with doubly exponential decay in }-u.
 \tag{2}
\]

Every fixed derivative of that remainder has the same decay type.
Since P4(1)=0 and P4(-1)=960, A2 has leading term
\((15/4)e^{-u}\). In the correction c(D-1)psi the corresponding term is
\(-c e^{-u}\). Thus positive-time full-line absolute integrability forces
c=15/4 in this class. The exact factorization is

\[
 P_4(D)+480(D-1)=(D^2-1)(D^2-22D+165).
\]

The completed source therefore is

\[
 \boxed{C_2=A_2+B_2
 =q^2g_2+\tfrac{15}{4}(D-1)\psi
 =\tfrac1{16}(D^2-22D+165)\Phi,}
 \quad B_2=\tfrac{15}{4}(D-1)\psi.
 \tag{3}
\]

C2 and its fixed derivatives decay doubly exponentially at both cusps,
locally uniformly after multiplication by the heat weight, a fixed
polynomial and a spectral exponential. All subsequent completed transforms,
derivatives and product integrals are consequently absolutely convergent.
The separate transforms of A2 and B2 diverge at the negative cusp for
t>0. Equation (3) must be formed before integration.

A useful scope lemma makes the cancellation precise. For any finite
constant-coefficient polynomial Q, the full-line transform of Q(D)psi
is absolutely integrable at a positive time if and only if
Q(-1)=Q(1)=0. Necessity follows from the two exponential terms in (2):
neither survives multiplication by exp(tu squared) at the negative cusp.
Sufficiency follows by divisibility:

\[
 Q(D)=(D^2-1)R(D),\qquad Q(D)\psi=8R(D)\Phi.
 \tag{4}
\]

This lemma requires no definite-parity hypothesis. It concerns finite
polynomials after the declared q weights are applied; it does not address
variable coefficients, nonlocal source operators or a new coupled kernel.
At zero or negative heat time its necessity statement is not asserted.

## Physical observation, full product and boundary bookkeeping

Define

\[
 W(t,x)=\tfrac12\int_{\mathbb R}e^{tu^2}C_2(u)e^{ixu}\,du,
 \qquad H=\tfrac12\int_{\mathbb R}e^{tu^2}\Phi(u)e^{ixu}\,du.
\]

Integration by parts has zero upper and lower currents for the completed
physical source. In particular,

\[
 \mathscr F_t(D\Phi)=-i(xH-2tH_x),\quad
 \mathscr F_t(D^2\Phi)=(2t-x^2)H+4txH_x-4t^2H_{xx}.
\]

Thus the exact observation is

\[
 \boxed{W=\tfrac1{16}\left[
 (165+2t-x^2)H+4txH_x-4t^2H_{xx}
 +22i(xH-2tH_x)\right].}
 \tag{5}
\]

The negative sign of the Hxx term is required. This is a finite physical
jet, rather than a new independently known source value.

For comparison, a one-sided transform has actual lower boundaries. Set
F=integral from zero to infinity of exp(tu squared)Phi(u)exp(ixu). Then

\[
 \int_0^\infty e^{tu^2}C_2(u)e^{ixu}\,du
 =\tfrac1{16}\left[
 (165+2t-x^2)F+4txF_x-4t^2F_{xx}
 +22i(xF-2tF_x)+(22+ix)\Phi(0)-\Phi'(0)\right].
 \tag{6}
\]

For theta, Phi'(0)=0, but Phi(0) is retained. F also has a sine component.
Neither a doubled one-sided cosine nor deletion of the displayed boundary
reproduces W.

For the real completed source, the full current has a coupled formula

\[
 J_2:=\operatorname{Im}(\overline W W_x)
 =\tfrac18\iint_{\mathbb R^2}(u+v)e^{t(u^2+v^2)}
 C_2(u)C_2(v)\cos(x(u-v))\,du\,dv.
 \tag{7}
\]

The coefficient 1/8 includes the two factors 1/2 in W and symmetrization
in u,v. Pointwise, its source product is

\[
 C_2(u)C_2(v)=A_2(u)A_2(v)+A_2(u)B_2(v)
                  +B_2(u)A_2(v)+B_2(u)B_2(v).
 \tag{8}
\]

At the negative corner the leading coefficients have signs +,-,-,+ and
cancel in their sum. None of the four separated weighted transforms is an
absolutely convergent source product for t>0. Triangle estimates of these
pieces are therefore unavailable. Equation (7) is applied to the
recombined product, where Fubini is justified by completed decay.

## Complete current and the new residual

Put hj=partial_x^j H, L0=h1 squared-H h2,
L1=h2 squared-h1 h3 and L0_x=h1 h2-H h3. Expanding (5) before estimating
gives

\[
 \boxed{J_2=\tfrac{11}{128}\left[
 (165+2t)H^2+(xH-2th_1)^2
 +2t(165+4t+x^2)\mathcal L_0
 -4t^2x\partial_x\mathcal L_0+8t^3\mathcal L_1\right].}
 \tag{9}
\]

In particular the H h3 and h1 h2 mixed terms remain in the derivative
term. Centering removes only the displayed first-jet quadratic form:

\[
 \boxed{J_{2c}:=J_2-\tfrac{11}{128}
 \{(165+2t)H^2+(xH-2th_1)^2\}
 =\tfrac{11t}{64}\left[
 (165+4t+x^2)\mathcal L_0
 -2tx\partial_x\mathcal L_0+4t^2\mathcal L_1\right].}
 \tag{10}
\]

This goes beyond J1c: it explicitly introduces L1 and a signed derivative
of L0. Neither is independently estimated by source completion or Hodge
positivity.

The [complete primitive bridge][bridge] also identifies every half-line
lower edge and corner in this expression. Use 8hj=Ij+(1/2)delta_j0 and
kappa=I0+1/2. Then J2=(11/8192)N, where

\[
\begin{aligned}
 N={}&(165+2t)\kappa^2+(x\kappa-2tI_1)^2\\
 &+2t(165+4t+x^2)(I_1^2-\kappa I_2)
 -4t^2x(I_1I_2-\kappa I_3)+8t^3(I_2^2-I_1I_3).
\end{aligned}
 \tag{11}
\]

If Nbulk is the same polynomial with kappa replaced by I0, the entire
primitive edge/corner contribution is

\[
 N-N_{\rm bulk}=(165+2t+x^2)(I_0+\tfrac14)
 -2txI_1-t(165+4t+x^2)I_2+2t^2xI_3.
 \tag{12}
\]

The 1/4 corner and all signed lower-edge terms are part of the physical
observation. Equations (8) and (12) rule out obtaining a favorable
remainder by deleting cross terms or boundaries.

## Collision screen and the scope of the closure

At any nondegenerate event with t>0,
H=h1=0 and h2 nonzero. Equations (5), (9) and (10) yield

\[
 \boxed{E=0,\quad W=-\tfrac{t^2}{4}h_2\ne0,\quad
 J_2=J_{2c}=\tfrac{11t^3}{16}h_2^2>0.}
 \tag{13}
\]

Consequently:

1. J2c>0, or even J2c>delta E for a prescribed finite delta, accepts
   a nondegenerate event. By continuity the latter inequality holds on a
   sufficiently small neighborhood of that event. It is not a physical
   noncollision test.
2. A finite locally bounded payment |W| squared<=M E fails at that event.
   Such a source-uniform payment cannot follow from completion, reflection
   and generic heat/current algebra on a class containing that source.

An exact heat-polynomial check is H=x squared-2(t-T), T>0. It solves
H_t=-H_xx and at (T,0) has W=-T squared/2,
|W| squared=T to the fourth/4 and J2c=11T cubed/4, while E=0.
This checks algebra, but it is not itself an integrable source example.

The [reflected super-Gaussian control][reflected] supplies the actual
convergent source example. At T=1/4 it has

\[
 H_*(T,x)=cF(x)(1+\cos4x),\quad c>0,\quad
 F(x)\ge M_0(1-x^2/4)>0\quad(|x|<2).
\]

At x*=pi/4 its H and Hx vanish and Hxx=16cF(x*)>0. All fixed derivatives
of its source decay faster than a Gaussian, so the differential completion
C2*=(D squared-22D+165)Phi*/16 and its full transform converge. Applying
(13) uses this control's own Hxx and its own source; it imports no theta
tail or error constant. The control has positivity, full even reflection,
convergence and the completed differential observation. It fails the
canonical integer-square arithmetic identity. This is the premise by
which a future theta-specific estimate may distinguish it.

Weighted-square controls share the raw local transverse algebra and have
certified nondegenerate events, but fail full theta reflection. Inserting
the theta coefficient 15/4 into their raw primitive completion is not
justified; no convergent raw A2+B2 transform is asserted for them.
Their own event jets still test the generic differential current (5).
The Euler-factor control retains positive even decay and has a separate
negative-Laguerre witness; it fails the canonical theta coefficient and
modular data. Smooth shape and positive-primitive controls retain the
stated generic premises while failing the arithmetic square expansion.
They screen any claimed generic sign implication, rather than challenging
an arithmetic hypothesis they do not possess. Fresh inherited control
replays and the exact reflected event calculation are recorded in the
[numerics guide][numerics].

Subtracting the favorable L1 term in (10) is a possible further proposed
remainder, but the result is exactly

\[
 J_{2c}-\tfrac{11t^3}{16}\mathcal L_1
 =\tfrac{11t}{64}\{(165+4t+x^2)\mathcal L_0
                      -2tx\partial_x\mathcal L_0\}.
 \tag{14}
\]

This is not a positive multiple of L0, and no equivalence of their signs
is claimed. It is an exposed signed derivative target with no independent
arithmetic bound supplied here. Identity (14) alone does not pass T1's
feasibility gate or authorize a bounded T2 campaign.

The closure concerns this second-completion current-positivity test and
generic first-jet energy magnitude payment. It does not rule out a
theta-specific bound on the old collision-free pilot, a paid estimate
using higher physical jets, a genuinely coupled arithmetic remainder,
or variable-coefficient/nonlocal completion. No theta approximation
error, cost, margin, coverage, Newman bound or complex exterior claim
changes. S06-T2 remains Waiting until a different independently estimable
term is selected. See the [internal review][review].

[opening]: 01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[previous]: 02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a2]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[bridge]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[reflected]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md
[numerics]: ../numerics/README.md
[review]: ../reviews/04_SECOND_TRANSVERSE_COMPLETION_INTERNAL_REVIEW_20261019.md
