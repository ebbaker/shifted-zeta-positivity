# Auxiliary flows for localizing collision cancellation

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007.

Edward Baker asked for continuous, parameterized deformations driven by an auxiliary differential equation, retaining the complete radial integrand as the sole invariant. The [manuscript][ms] and [Note20][n20] now give explicit examples. This brainstorm considers how to use that freedom. Concentrating a representation is established for the examples below; an estimate that excludes a theta collision remains a research question.

## Three meanings of localization

The physical event (T,a_*) cannot move or disappear while H is fixed. What can change is where the three-dimensional fields carry its two cancellations, which boundary carries a flux, or which part of an integral needs detailed estimation. The proposed study should choose one of those meanings before optimizing a flow. The radial density still contributes at every radius where it is nonzero.

## A controllable concentration parameter

Let P be normalized spherical averaging. The auxiliary equation

\[
\partial_sA=(q-P(qA))A,\qquad A_0=1,
\]

has the explicit solution A_s=e^(sq)/P(e^(sq)). It preserves PA=1 at every radius. Taking F_{s,t}=A_sQ_t keeps the entire radial integrand fixed. The fixed score q can be chosen to favor a desired angular region. For q=ω·n, the mass outside a cap of angle δ is at most e^[−s(1−cosδ)]/(1−e^(−2s)). Thus s is an explicit localization parameter with a quantitative leakage bound.

There is also a transport PDE, ∂_sA+div_S(A∇_Sq)=0. For the same linear angular score, A_s=(cosh s−q sinh s)^(−2), and half its mass lies in the cap q≥tanh s. This gives a geometrical motion along the sphere, rather than an imposed cutoff. The flow and the exponential normalization flow are different.

A diffusion-and-drift variant is

\[
\partial_sA=D\Delta_{S^2}A-\operatorname{div}_{S^2}(A\nabla_{S^2}q),\qquad D>0.
\]

Its angular integral is conserved, and direct substitution shows that the normalized stationary density is e^(q/D)/P(e^(q/D)). Positive diffusion offers a way to retain a finite width. A cooling schedule D(s) would need an actual evolution and convergence analysis; it is not automatically the stationary formula with D replaced by D(s). Diffusion alone from A=1 does not localize anything.

## Aim the flow at the first jet

A common cap axis merely concentrates every radial contribution in the same direction. A more specific choice freezes a_* and aligns the cap at u with

\[
n(u)=\frac{(\cos(a_*u),-bu\sin(a_*u),0)}
 {\sqrt{\cos^2(a_*u)+b^2u^2\sin^2(a_*u)}},\qquad b>0.
\]

The exact weighted angular moment in Note20 equals (coth s−1/s)(H(T,a_*),bH_a(T,a_*),0). Under a hypothetical collision, it vanishes. The auxiliary flow concentrates that vector cancellation near the curve Γ(u)=e^(2u)n(u). This gives a specific geometry for a possible tube or boundary calculation, while keeping the construction independent of the running spectral argument z.

One possible investigation is to follow the signed flux through a finite-width tube around Γ, using the explicit cap leakage as the exterior allowance. Its lateral slope and curvature depend on n′ and n″, and the deformed differential operator contains their full contributions. A useful result would compare the complete signed tube identity with the original radial calculation. The curve's existence and its zero weighted moment are representations of the event, not an exclusion.

## Let a Laplacian flow choose the deformation

The explicit cap families prescribe their destination. A broader possibility is to minimize a chosen localization cost within the space of fields with the correct radial average. This permits deformations beyond multiplication of the original response by a scalar angular factor.

Here is a concrete bounded prototype. Work on a fixed annulus Ω={r_-<|X|<r_+}, with r_->1. Write F=Q+G, require PG=0, and set G=0 on both radial boundaries. Let χ_out(r,ω)≥0 be a smooth weight outside a chosen angular tube, and let ε>0. Define

\[
\mathcal E(G)=\frac12\int_\Omega\chi_{\rm out}(Q+G)^2\,d^3X
             +\frac\varepsilon2\int_\Omega|\nabla G|^2\,d^3X.
\]

The projected gradient equation is

\[
\boxed{\partial_sG=\varepsilon\Delta G
 -(I-P)[\chi_{\rm out}(Q+G)],\qquad G_0=0.}
\]

For smooth solutions with those boundary conditions, PG satisfies the homogeneous radial heat equation with zero initial and boundary data, hence remains zero. Equivalently, the equation stays in the zero-average sector. P is orthogonal for the Euclidean volume inner product because its weight r² is radial. Integration by parts then gives

\[
\frac{d\mathcal E}{ds}=-\int_\Omega|\partial_sG|^2\,d^3X\le0.
\]

These are conditional identities for a smooth solution of this bounded problem. A completed return must specify existence, regularity, and the treatment of radial joins or boundary flux before claiming a global smooth realization. Positivity is not ensured, and is not an invariant required by the user. If desired for a particular application, positivity would call for a different constrained flow.

The objective moves source magnitude away from the selected exterior region while paying a gradient penalty. It is not yet a collision-sensitive objective: a better candidate could be derived from the full forcing and boundary terms of a chosen response equation. That would require deriving the response variation and its adjoint before using the phrase gradient descent for that problem. This prototype gives a concrete auxiliary PDE to develop without pretending that such an adjoint or collision estimate is already available.

## How to judge these possibilities

For a radial f, multiplication by the exponential cap profile increases its ordinary squared norm by s coth s. In the induced measure A_s^(−2)d³X, the complete norm and integration-by-parts identity pull back to the original ones. Thus the full induced energy alone does not improve the collision argument. This scopes one comparison; it does not exclude signed tube estimates, different objectives, or more general nonmultiplicative deformations.

The exact Gaussian-polynomial collision survives all the normalized angular constructions. The [control register][controls] and [Brainstorm01's premise table][b01] apply to the other source classes. A successful theta application must use the fixed canonical marginal in an estimate that actually distinguishes those controls; no extra invariant of the deformed fields is being demanded.

The most useful next calculation appears to be one of two bounded questions: compute the complete boundary current for the steered finite-width tube, or develop the projected annular PDE with a fully specified response-based objective. The former tests whether the new geometry simplifies a signed identity; the latter tests whether the deformation can be selected by a genuine dissipative evolution. Neither requires taking an uncontrolled infinite-concentration limit. Their results should determine the next research choice.

[ms]: ../radial_deformations_and_zero_dynamics.tex
[n20]: ../notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md
[b01]: 01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
