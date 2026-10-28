# Deformations preserving the radial integrand and localizing a collision

27 October 2026, America/New_York. Idea proposed by **Edward Baker**; organized and developed for him with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007, **Explore collision-localizing deforms**, thread `01a18047-0177-7ad2-878f-19ed2eaa1a37`.

**Status: brainstorm and elementary construction examples.** The proposed search permits general changes to the equations and higher-dimensional realization, subject to one invariant: the complete radial integrand remains unchanged at every radial coordinate. The objective is to represent a hypothetical positive-time collision in a form where its local geometry, dynamics or integral balance becomes easier to estimate. No collision exclusion or new theta estimate is established here.

## Edward Baker's proposal and clarifications

> Before proceeding, I'd like to mention a new idea that I was thinking about regarding the possible contradiction. I'm wondering if one approach to the problem is the following. Assume there is a collision at positive time. Can we find a deformation of the equations that leads to some form of dynamics that is clearly not possible? Perhaps there is a way to find a deformation that "localizes" that collision in some way and exposes the most salient features of it, which could potentially lead to more powerful tools for studying it (maybe estimating certain integrals in three dimensions instead of one, with more natural boundaries).

He then broadened the admissible class:

> Perhaps there are more general deformations than those considered in the manuscript, the only requirement is to preserve the radial distribution in order to maintain H(t,z)

The intended meaning of radial distribution is explicit:

> It means preserve the integrand over r or u depending on the variable, which is essentially a radial coordinate

> That is really the only invariant, and the Laplacian machinery probably gives some guidance on what types of deformations can naturally preserve the desired radial distribution

The invariant is therefore the complete one-dimensional density, not merely its integral or total source mass. The intermediate fields need not preserve radial symmetry, a particular potential, a spectrum, positivity, an energy identity, or the Darboux factorization. These may be useful properties of a chosen construction, but they are not additional requirements imposed on the search.

## The invariant in the manuscript's coordinates

Use the [manuscript][manuscript] and [continuation note19][handoff]. With r=exp(2u),

\[
H(t,z)=\int_0^\infty \mathcal I_u(t,z;u)\,du
      =\int_1^\infty \mathcal I_r(t,z;r)\,dr,
\]
\[
\mathcal I_u=e^{tu^2}\Phi(u)\cos(zu),\qquad
\mathcal I_r=\frac18r^{3/2}e^{t\log^2r/4}Q(r)
                 \cos\!\left(\frac z2\log r\right).
\]

The densities satisfy \(\mathcal I_r\,dr=\mathcal I_u\,du\); the Jacobian must accompany a change of radial coordinate. Fixing either complete density in its own coordinate fixes H and its spectral derivatives wherever differentiation under the integral is justified.

For a three-dimensional realization, let dν=dΩ/(4π) be normalized spherical measure. The defining requirement can be written

\[
\boxed{\int_{S^2}\mathcal J_s(t,z;r,\omega)\,d\nu(\omega)
       =\mathcal I_r(t,z;r)\quad\text{for every }r\ge1.}
\tag{1}
\]

Here s is the auxiliary deformation parameter. Equation (1) fixes the reduced integrand pointwise in r, while allowing the full field and equations to change. More general angular measures or geometries can be used if their measures and Jacobians are included in this equality. Ordinary regularity and convergence are needed to make the equations meaningful; they are not extra conserved quantities.

One convenient sufficient construction changes the source field. Write

\[
\mathcal P F(r)=\int_{S^2}F(r,\omega)\,d\nu(\omega),\qquad
\mathcal P F_s=Q.
\tag{2}
\]

Then choose

\[
\mathcal J_s=\frac18r^{3/2}e^{t\log^2r/4}F_s(r,\omega)
              \cos\!\left(\frac z2\log r\right).
\]

This preserves (1) for every t,z in the convergence domain. In ordinary Euclidean volume measure the identical observation is

\[
H(t,z)=\frac1{32\pi}\int_{|X|\ge1}
 |X|^{-1/2}e^{t\log^2|X|/4}F_s(X)
 \cos\!\left(\frac z2\log|X|\right)\,d^3X.
\tag{3}
\]

The coefficient in (3) follows from d³X=r²dr dΩ. Preserving Q through (2) is a useful example of (1), not a requirement that every admissible deformation retain a source/test-factor decomposition of this form.

## Why the Laplacian supplies natural deformations

For a smooth field on a spherical shell,

\[
\Delta=\partial_r^2+\frac2r\partial_r+\frac1{r^2}\Delta_{S^2}.
\]

The sphere has no boundary, so the integral of its angular Laplacian vanishes. Consequently

\[
\boxed{\mathcal P\Delta F
 =\left(\partial_r^2+\frac2r\partial_r\right)\mathcal P F.}
\tag{4}
\]

In particular, the full Laplacian takes fields with zero spherical average to fields with zero spherical average. Starting with Q=ΔΘ, any smooth potential perturbation Ψ_s with \(\mathcal P\Psi_s=0\) gives

\[
\widetilde\Theta_s=\Theta+\Psi_s,\qquad
F_s=\Delta\widetilde\Theta_s=Q+\Delta\Psi_s,
\qquad\mathcal P F_s=Q.
\tag{5}
\]

This changes the potential and the three-dimensional source while preserving the radial integrand exactly. Keeping the potential's spherical average fixed is a sufficient way to build this family, not another invariant required of every possible family.

A concrete example uses a smooth bump χ supported in an annulus strictly inside r>1 and a unit vector n:

\[
\Psi_s(r,\omega)=s\chi(r)(\omega\cdot n),
\]
\[
F_s(r,\omega)=Q(r)+s\left(\chi''+\frac2r\chi'
                              -\frac2{r^2}\chi\right)(\omega\cdot n).
\tag{6}
\]

The angular factor has mean zero and angular Laplacian −2 times itself, proving (6) and its preservation directly. The change is spatially confined to the annulus; all exterior radial tails remain those of Q. No sign restriction on F_s is needed for preservation. Small amplitudes can retain positivity if a particular argument benefits from it, because Q is strictly positive on the compact support.

At physical time t, take \(F_{s,t}=e^{t\log^2r/4}F_s\). Its average is exactly Q_t. This is not an assertion that \(F_{s,t}=\Delta(e^{t\log^2r/4}\widetilde\Theta_s)\); that expression has additional radial derivative terms.

Angular conservation laws give another natural class:

\[
\partial_s F_s=-\operatorname{div}_{S^2}J_s
\quad\Longrightarrow\quad
\partial_s\mathcal P F_s=0.
\tag{7}
\]

For example, J_s=F_s v_s gives angular transport, and J_s=−∇_{S²}F_s gives angular diffusion. Pure angular diffusion leaves an initially radial field stationary. Nontrivial angular transport can begin from Q when the velocity has nonzero angular divergence; a rigid rotation of a radial field does nothing. An angular change of variables, with its density Jacobian and the transformed differential operator, is another realization of the same preservation principle. The resulting operator may have anisotropic or mixed coefficients: there is no reason to insist on the manuscript's scalar radial potential form.

## Angular concentration as an explicit example

For η≥0, define

\[
A_\eta(\omega)=\frac{\eta e^{\eta\omega\cdot n}}{\sinh\eta},
\qquad A_0=1,\qquad F_\eta(r,\omega)=Q(r)A_\eta(\omega).
\tag{8}
\]

Direct integration gives

\[
\int_{S^2}e^{\eta\omega\cdot n}\,d\nu
 =\frac12\int_{-1}^{1}e^{\eta v}\,dv
 =\frac{\sinh\eta}{\eta}.
\]

Thus (8) is an explicit smooth positive family preserving every radial contribution. Increasing η concentrates the angular distribution near n, while every finite η retains the canonical radial decay and the complete H. This gives a concrete instance of geometric localization compatible with the proposed invariant. It does not yet localize a spectral collision or provide an advantageous PDE estimate. A singular limit would require separate control of angular derivatives and boundary terms.

The fixed radial density also clarifies what cannot be removed by a bare cutoff: a nonzero radial contribution cannot disappear outside a finite radial interval. Its contribution must remain represented at those radii. A localized perturbation such as (6), angular concentration such as (8), or a localized estimate with the complementary contribution retained are all compatible with that fact. These examples do not exhaust the allowable deformations.

## Relation to the existing Darboux family

The manuscript supplies an exact integrated observation but need not preserve its displayed integrand pointwise. In its notation,

\[
h_\kappa=g'-w_\kappa g,\qquad
p_\kappa'+w_\kappa p_\kappa=\cos(\sqrt\lambda x),
\]
so

\[
p_\kappa h_\kappa
 =-g\cos(\sqrt\lambda x)+(p_\kappa g)'.
\tag{9}
\]

The derivative integrates to zero under its selected boundary conditions. The new requirement therefore broadens the permissible equations while asking for a stronger, pointwise preservation statement about their reduced density. The Darboux pairing fits that requirement only if its derivative correction is included in the local density. Its cosh seed and fixed radial form do not define the new search space. The [existing reference annotation][darbouxref] records the classical factorization source; no homogeneous spectral theorem is being imported into the broader proposal.

## How localization might contribute to a contradiction

Assume a physical event H(T,a)=H_z(T,a)=0 with T>0 and real a>0. Because (1) preserves H, retaining this event is automatic. It is not a second invariant to impose. The freedom lies in choosing fields, operators and domains that make the fixed radial data easier to analyze.

For an ordinary double event, put C=H_zz(T,a)≠0. Taylor expansion and H_t=−H_zz give the local rescaling

\[
\frac{H(T+\varepsilon^2\tau,a+\varepsilon\xi)}
      {(C/2)\varepsilon^2}
 =\xi^2-2\tau+O(\varepsilon)
\tag{10}
\]

on compact rescaled sets. This is the familiar allowed double-event model, including its orientation in Newman time. It identifies the local geometry but supplies no impossible dynamics by itself. Higher multiplicities require their own models. See the [local collision summary][geometry] for the stronger inherited results and their scope.

The three-dimensional proposal has a different possible use: choose an allowed realization so that an integration-by-parts identity, a monotonicity law, or a comparison estimate exposes the source cancellation at the event. Spherical shells and angular boundaries are natural candidates because (4) distinguishes the retained radial part from the freely varying angular part.

Two details belong to that calculation. First, a physical collision fixes the reduced observation; in a general nonradial response it need not make a field vanish pointwise on the whole inner sphere. Any such boundary condition must follow from the chosen construction. Second, localizing a field changes its equation:

\[
\Delta(\chi F)=\chi\Delta F
                 +2\nabla\chi\cdot\nabla F+(\Delta\chi)F.
\tag{11}
\]

The transition terms and all boundary fluxes must enter the resulting identity. These are consequences of the chosen equations, not additional invariants. A useful deformation would make the complete identity easier to control using the fixed theta marginal. The deformed fields themselves need not retain theta's square expansion or Kelvin symmetry.

## Collision controls and the first structural question

The [control register][controls] and [premise-screening rule][a02] distinguish generic identities from an actual theta estimate. Equations (1)–(8) apply to many radial marginals. Their validity cannot by itself rule out a collision.

| Control | What the proposed preservation constructions retain | Canonical input the control lacks |
| --- | --- | --- |
| Manuscript's Gaussian-polynomial example | Its exact double event survives (5), (6) and (8), on its heat convergence domain | The fixed theta marginal and canonical tails |
| Euler-factor controls | Their own complete observation and collisions, for each allowed prime and parameter | The unchanged canonical theta marginal; the arithmetic and conductor data are modified |
| Weighted-square and finite-prime controls | Their own marginal and all measurements derived from it | Unchanged complete theta coefficients and full source reflection |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Their own reflected or positive marginal and collision | The complete canonical square-source marginal |
| Finite-profile and atomic threshold controls | The angular mass construction still makes sense for measures; the smooth potential calculation needs an appropriate formulation | The full theta marginal and the full profile/eventual-simplicity inputs identified in the register |
| RH-conditional endpoint controls | Their own perturbed observation, with their conditional and endpoint scope retained | Ordinary theta Dirichlet-series arithmetic and the exact canonical marginal |

For the first row this is an exact substitution, not a numerical test: at the manuscript's event, g_*=(16x⁴+24)e^(−x²), whose cosine transform is (√π/2)(λ−6)²e^(−λ/4). Setting Q_*(r)=r^(−5/2)g_*(log r) at that time and applying (5), (6), or (8) leaves that transform exactly unchanged. The same projection calculation covers the smooth registered controls within their actual convergence domains. Atomic examples are not silently treated as smooth potentials. Earlier numerical certificates are not rerun here.

Failing equality with theta's marginal does not mean that a control fails an as-yet-unproved inequality. A future separating estimate must demonstrate that distinction quantitatively. This does not add an invariant: the theta data are already present in the density that the user has asked to keep fixed.

**First structural question:** choose one explicit deformation generated by the Laplacian's zero-average angular sector, derive its complete equations and reduced observation, and determine whether a localized integral or dynamics becomes simpler in a mathematically useful way. The compact annular family (6) is a bounded starting example; angular transport or concentration offers a different one. Compare the resulting identity with its one-dimensional reduction and the exact colliding control before selecting a larger construction.

A new structural correspondence or a scoped limitation would be a legitimate return. A sharper theta inequality would be a further result. Simply recovering H or writing a three-dimensional integral is setup. This is a proposed extension of the [RDZ program][program], especially its broader deformations and pairings questions; no RDZ task is marked complete by this brainstorm. The all-positive-time contradiction remains the existing final target, classified according to [avoid01][a01], rather than a new criterion supported by examples.

## Sources and scope

The repository [result index][results] and [avoid index][avoid] govern interpretation, especially [collision controls][controls], [local collision geometry][geometry], [coordinate realizations][a03] and [scoped exclusions][a07]. [Note04][gaussian] already shows why a deformation to a positive terminal transform can lose a collision through a boundary; it concerns that specific Gaussian family. It does not exclude the general integrand-preserving search proposed here.

The projection, angular example, normalization, Darboux density comparison and local Taylor calculation above were checked by direct differentiation and integration by the same assistant. They organize a research proposal; no independent specialist review, new numerical certificate, improved Newman bound or completed collision exclusion is claimed. Research chat text is retained in this investigation's [chat0007 archive][chat] through the standing history tool.

[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[handoff]: ../notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
[program]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[gaussian]: ../notes/04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[darbouxref]: ../references/08_DARBOUX_FACTORIZATION_AND_RADIAL_DEFORMATION_20261027.md
[chat]: ../chat-histories/0007_2026-10-28T02-11-39Z_explore-collision-localizing-deforms.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
