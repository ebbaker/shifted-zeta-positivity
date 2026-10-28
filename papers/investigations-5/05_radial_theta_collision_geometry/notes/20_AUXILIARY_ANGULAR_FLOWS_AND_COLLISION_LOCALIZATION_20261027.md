# Auxiliary angular flows preserving the radial integrand

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007, **Explore collision-localizing deforms**.

**Status: elementary finite-parameter constructions proved by direct calculation, with same-assistant checking.** The [manuscript][ms], Sections 9–10, now includes the radial-integrand invariant, a Laplacian construction, two auxiliary flows, a complete deformed equation and boundary map, and a representation of the physical first jet concentrated near a curve. The [new brainstorm][b02] proposes further uses, including a projected Laplacian descent. No theta collision is excluded and no asymptotic operator limit is taken.

The invariant is exactly the one specified by Edward Baker in [Brainstorm01][b01]: the complete one-dimensional integrand remains fixed at every radius. Extra properties of the examples below are consequences of choosing those examples, not additional invariants required of the whole program.

## The explicit auxiliary differential equations

Let P denote normalized spherical averaging. A fixed smooth bounded real score q(r,ω), independent of physical t,z, defines

\[
A_s=\frac{e^{sq}}{P(e^{sq})},\qquad
\bar q_s=P(qA_s),\qquad
\partial_sA_s=(q-\bar q_s)A_s,\quad A_0=1.
\]

Then PA_s=1 and ∂_s\bar q_s=P(A_s(q−\bar q_s)²)≥0. The source F_{s,t}=A_sQ_t has PF_{s,t}=Q_t. The explicit exponential solution establishes smooth finite-s existence for smooth q; bounded q gives domination for every physical derivative used in the observation on compact physical parameter sets. Spatial derivatives require their own bounds; the fixed-axis and steered-axis examples have the required growth.

For q=ω·n with |n|=1,

\[
A_s=\frac{s e^{s\omega\cdot n}}{\sinh s},\quad
P(\omega A_s)=(\coth s-1/s)n,\quad
P(A_s^2)=s\coth s.
\]

All formulas have removable values at s=0. They follow from P(e^{sq})=(1/2)∫_{−1}^1e^{sv}dv=sinh(s)/s. Differentiating its logarithm gives the angular mean; replacing s by 2s gives the square norm. The exact cap complement is

\[
P(A_s1_{q\le\cos\delta})
=\frac{e^{s\cos\delta}-e^{-s}}{e^s-e^{-s}}
\le\frac{e^{-s(1-\cos\delta)}}{1-e^{-2s}}.
\]

The separate angular transport PDE ∂_sA+div_S(A∇_Sq)=0, also starting at A_0=1, has density A_s^tr=(cosh s−q sinh s)^(−2). Indeed dv/ds=1−v², and differentiating the inverse characteristic v_0=(v−tanh s)/(1−v tanh s) gives that density. Its mass in v≥tanh s is exactly one half, since that set is the image of v_0≥0. These two flows are distinct; the exponential density does not solve this unmodified transport equation.

## A complete equation realization

Start with the manuscript's selected response

\[
\psi=r^{-1/2}Y(\log r),\quad
L_\lambda=\Delta+\frac{\lambda+1/4}{r^2},\quad L_\lambda\psi=Q_t.
\]

For any positive normalized A_s independent of t,λ, set ℓ_s=log A_s and ψ_s=A_sψ. Product differentiation gives

\[
L_{\lambda,s}=A_sL_\lambda A_s^{-1}
=\Delta-2\nabla\ell_s\cdot\nabla+
  \frac{\lambda+1/4}{r^2}+|\nabla\ell_s|^2-\Delta\ell_s,
\quad L_{\lambda,s}\psi_s=A_sQ_t.
\]

This is an actual change to the equations, including angular drift. The induced boundary operator is

\[
\mathcal R_s f=[(r\partial_r+1/2-r\partial_r\ell_s)f]_{r=1}.
\]

It obeys R_sψ_s=A_s(1,ω)B, so PR_sψ_s=B=−8H and PR_s∂_λψ_s=B_λ. Differentiation in λ commutes with R_s because A_s is independent of λ. Every finite spectral multiplicity is retained. The inverse and selected solution are explicit at finite s; no new homogeneous eigenvalue problem or unspecified domain equivalence is assumed.

For the exponential flow, a_s=q−\bar q_s gives ∂_sψ_s=a_sψ_s and ∂_sL_{λ,s}=[a_s,L_{λ,s}]. This commutator is a consequence of conjugation. It is not evidence of a separately proved integrable hierarchy. Physical time still satisfies ∂_tF_{s,t}=(log²r/4)F_{s,t}.

## A representation aimed at the collision conditions

Freeze a candidate frequency a_*>0 and b>0. Define

\[
v(u)=(\cos(a_*u),-bu\sin(a_*u),0),\quad
m(u)=|v(u)|,\quad n(u)=v(u)/m(u).
\]

The denominator is positive for every u≥0. On large u it is bounded below by min(1,bu), and on a compact interval positivity supplies a positive minimum. Hence n is smooth, and its finite derivatives grow at most polynomially in u for fixed a_*,b. With r=e^(2u), the resulting spatial derivatives are compatible with the canonical tails. These bounds are not uniform as a_* varies over all heights.

Use q(r,ω)=n(log r/2)·ω. The candidate frequency is a fixed construction parameter, not the running z in H(t,z). For ρ_T=e^(Tu²)Φ(u),

\[
\int_0^\infty\rho_Tm\,P(\omega A_s)\,du
=(\coth s-1/s)(H(T,a_*),bH_a(T,a_*),0).
\]

The first component follows from m n_1=cos(a_*u); the second follows from m n_2=−bu sin(a_*u) and the differentiated cosine transform. Thus a multiple physical zero gives zero weighted angular first moment for all s>0. No assumption that the multiplicity is exactly two is needed for this identity; it does not classify higher jets or higher-order collision geometry.

The angular profiles concentrate near the spatial curve Γ(u)=e^(2u)n(u), with the cap estimate above uniformly in u. Since m≤1+bu and the canonical source has all needed moments, multiplying the cap bound by ∫ρ_Tm gives a finite bound on the omitted weighted mass. The construction concentrates a representation of the cancellation; it does not shrink the radial support or change the physical event.

## Costs and control screen

For a radial field f and a positive radial weight, its ordinary squared norm after multiplication by A_s is multiplied by s coth s. In the induced measure A_s^(−2)d³X, the norm of A_sf equals the original norm exactly. The complete forced Green identity in that induced measure, with the induced boundary operator, also pulls back to the original identity. This scopes the comparison: a global radial-weighted source norm does not improve, and simply transporting the complete energy identity adds no event condition. Local signed quantities and deformations outside this multiplication family remain open.

For the steered score, derivatives with respect to r satisfy

\[
|\nabla\ell_s|^2=s^2[(n'\cdot\omega)^2+(1-q^2)/r^2],
\quad
\Delta\ell_s=s[(n''+2n'/r)\cdot\omega-2q/r^2].
\]

The dependence of n on r must therefore enter a lateral-boundary calculation. No uniform inverse or limiting smooth operator at s=∞ is claimed.

The manuscript's exact Gaussian-polynomial event has H=H_a=0, so the displayed vector moment is exactly zero for every s>0, although its source concentrates into the same kind of tube. This is an analytic substitution using its exact transform, not a numerical experiment. The [control table in Brainstorm01][b01] and the [registered families][controls] extend this screen: smooth Euler-factor, weighted-square, finite-prime, reflected and primitive controls retain their observations on their own convergence domains. They fail the unchanged canonical radial marginal in the ways recorded there. Atomic sources require a measure/distributional formulation for the differential equations. None is claimed to fail an unavailable separating estimate.

## Classification and continuation

These are generic representation and localization statements, not a new RH-equivalent criterion. The proved quantities are the exact boundary map, the explicit cap tail, the norm cost, and the first-moment identity. A useful next return would calculate a complete signed boundary current or assess a specified projected descent functional, as proposed in [Brainstorm02][b02]. It must show what becomes easier to estimate; the existence of a normalized flow alone is not a theta estimate.

Use the [result index][results], [avoid index][avoid], [controls][controls], [target classification][a01], [coordinate-realization caution][a03], and [scope rule][a07]. The [assessment][review] records the mathematical and document checks. Source conventions are checked in the [reference annotation][ref]; the concentration and conjugation formulas are derived directly here and in the manuscript.

[ms]: ../radial_deformations_and_zero_dynamics.tex
[b01]: ../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md
[b02]: ../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md
[review]: ../reviews/12_RADIAL_INVARIANT_AND_ANGULAR_FLOW_SELF_ASSESSMENT_20261027.md
[ref]: ../references/09_SPHERICAL_LAPLACIAN_AND_ANGULAR_FLOW_CONVENTIONS_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
