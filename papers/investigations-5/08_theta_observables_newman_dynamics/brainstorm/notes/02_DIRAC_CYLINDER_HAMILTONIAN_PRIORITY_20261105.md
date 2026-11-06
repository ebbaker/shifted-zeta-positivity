# Dirac cylinder Hamiltonian as the starting model

**Planning update, 5 November 2026:** the author has now requested the [research plan](../../research-overview/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_DRAFT_OVERVIEW_20261105.md#research-plan) and [sole progress register](../../research-progress/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_RESEARCH_PROGRESS_20261105.md). The physical priorities below remain in force; its deferred-planning and B00-next instructions are historical. [Decision03](03_ANALYTICAL_RESEARCH_PLAN_DECISIONS_20261105.md) records the analytical/general-index planning return, prepared for Edward Baker with substantial LLM assistance, gpt-6-astra/max.

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in this turn's metadata. Investigation08 chat0001, thread `01a1ae2a-64b9-7882-8942-9c56f3d136e6`.

**Author clarifications within TND-B00.** Investigation08 should adapt MC11's full angular–radial Dirac-square model to the theta geometry and de Bruijn–Newman framework of `05_radial_theta_collision_geometry`. Understanding the Hamiltonian as naturally as possible is a leading priority. The starting object is the spinor model on a spherical cylinder, with its radial degree of freedom and geometric differential operator. The author also proposes investigating the Newman flow through radial eigenfunction expansions of its cosine kernel, while keeping a natural auxiliary flow open as another avenue.

This sharpens [Proposal01][proposal]: a preparation protocol or classical ensemble is not the selected organizing principle. The observation that two readouts depend only on a position distribution remains true, but does not replace the physical model the author wants to understand. Preparation and measurement will be studied in that model's context.

| Next discussion | Type | Recommended model | Readiness | Useful outcome |
| --- | --- | --- | --- | --- |
| TND-B00 — interpret the cylinder Hamiltonian and its Newman role | B — brainstorm | Astra; the Hamiltonian interpretation and choice between direct spectral Newman representation and a useful auxiliary flow remain conceptual | Ready from the existing operator and radial sources | A natural Hamiltonian interpretation and a comparison of the two flow avenues, with unresolved choices retained |

## The physical model meant by MC11

In [MC11 Section 2][mc], let D be the self-adjoint Dirac operator on the unit round sphere and Gamma its chirality. The complete cylinder and its operators are

\[
C=\mathbb R_v\times S^2,\qquad
g_C=dv^2+\tfrac14g_{S^2},\qquad
\mathcal D_C=-i\Gamma\partial_v+2D,\qquad
L_0=\mathcal D_C^2=-\partial_v^2+4D^2.
\]

The Hilbert space is the L2 space of spinors on this cylinder, with the paper's constant volume normalization. The sphere has radius 1/2. The free product model combines the radial and angular degrees of freedom while remaining separable; an additional interaction would be a further model choice. The angular channel D²=n² has multiplicity 4n, and the squared operator has channel dispersion k²+4n². Its self-adjoint realization and full-line Green kernel are among MC11's accepted operator results, within their internal-assessment scope.

L0 is the geometric positive kinetic operator whose Hamiltonian interpretation is to be developed. Its first-order Dirac factor, its use as a second-order Hamiltonian, and its heat or resolvent realizations have distinct physical roles. The initial discussion should explain those roles from the geometry and spinor structure, including units, rather than choose a new potential to prescribe a theta state.

## What the earlier phrase energy response referred to

The precise object is the **angularly damped radial Green response of L0**. If K0 is the kernel of L0 inverse, then

\[
K_0(v,v)=(4|D|)^{-1},\qquad
Q_s(\beta)=\operatorname{Tr}_{S^2}
\bigl[B_s e^{-\beta D^2}K_0(v,v)\bigr],
\quad B_s=P_1+s(I-P_1).
\]

For s=1 this is the complete sum of exp(-beta n²). Each radial Green diagonal contributes 1/(4n), cancelling the angular multiplicity 4n. Thus the response arises from the full cylinder operator, including all radial momenta. It is an observation of that operator, rather than the definition of the physical model. The angular damping beta is a separate control, and the response is not a full-cylinder thermal partition function.

The later conditional angular ensemble and energy-moment formulas offer measurement interpretations of this response. They do not replace the cylinder theory. Their separate observable assessment remains pending, as recorded in [Note13][observables].

## The direct connection to Investigation05

The [radial companion][radial] already uses the same product metric, with logarithmic radial coordinate u. Its field G is scalar, however, and its elliptic operator is

\[
\mathcal L_{\mathrm{sc}}=1-\Delta_C
=1-\partial_u^2-4\Delta_{S^2}.
\]

For its canonical radial family,

\[
\mathcal L_{\mathrm{sc}}G_\lambda=8e^{\lambda u^2}\Phi(u),
\qquad
\partial_\lambda G_\lambda
=\mathcal L_{\mathrm{sc}}^{-1}u^2\mathcal L_{\mathrm{sc}}G_\lambda,
\]

where the inverse is the decaying inverse in that radial sector. These are the companion's existing formulas, with lambda replacing its Newman-time symbol t. They retain the companion's same-assistant checking status.

The shared geometry makes this a concrete comparison between a spinor Dirac-square model and a scalar generating-field theory. Their field spaces and angular spectra differ, so an identification of their operators needs an actual construction. Likewise the source coordinate u in the angular-response scan has not yet been derived as the physical cylinder position v. The existing source map specifies beta=pi exp(4u) externally. Those connections are central questions for the Hamiltonian interpretation.

## Two flow avenues to keep open

**Represent Newman flow through radial spectral modes.** On the complete free cylinder, the radial spectrum is continuous. In the even radial sector the cosine waves are already generalized eigenfunctions. For D² chi_n=n² chi_n and real k,

\[
L_0[\cos(kv)\chi_n]=(k^2+4n^2)\cos(kv)\chi_n,
\qquad -\partial_k^2\cos(kv)=v^2\cos(kv).
\]

These elementary identities follow directly from the stated operator and kernel; the modes are not normalizable discrete eigenstates. Investigation05 already treats u as a logarithmic radial coordinate. Once the relation of that coordinate and source field to the MC11 spinor model is explicit, the identities give a natural point of entry for the author's suggestion: describe Newman evolution in radial spectral variables and ask what operator or deformation of the physical model realizes it. Complex z is then handled by the appropriate analytic continuation, not as a real self-adjoint spectral label.

At the scalar source level, multiplication by u² becomes minus the second derivative in the Fourier variable. This is the existing backward-heat identity. The new research question is its Hamiltonian interpretation in the coupled angular–radial model, including the source/readout map. Ordinary evolution by the radial kinetic operator is diagonal in its spectral variable and is a different operation. A change of spectral representation alone therefore does not settle the dynamical interpretation.

**Use a natural auxiliary flow from the same model.** Alternatively, seek an evolution suggested by the cylinder Hamiltonian, its geometry or a justified extension, and understand its effect on the scalar field and the observed H. This may be useful even when it is not Newman time itself. Its purpose could be explanatory, diagnostic or analytical; a claim about the original zeros would require an explicit comparison, recovery map or invariant. The ordinary cylinder-heat and linear-combination examples in Investigation05 provide benchmarks with their existing scopes, not a prohibition on other auxiliary dynamics.

Neither avenue is selected by this clarification. The physical interpretation and the information each flow makes accessible should guide the eventual choice. No finite box, radial confinement, changed boundary condition or new numerical survey is implied by considering an eigenfunction expansion.

## Revised first priority

**Develop the natural Hamiltonian interpretation of the angular–radial Dirac model on the spherical cylinder, and determine how that model can realize or extend Investigation05's theta generating field and de Bruijn–Newman evolution.**

Three questions organize the next discussion:

1. What physical theory does the geometric Dirac square describe, and what explains its kinetic terms, spinor structure and radial–angular separation?
2. How do its Green response and source observation produce the scalar theta field used in Investigation05, and which coordinate or observation choices still require explanation?
3. Does radial spectral analysis give a natural representation of Newman deformation within this theory, or does a natural auxiliary flow offer the more useful connection to Investigation05?

The geometry and Hamiltonian come first in this ordering. State preparation, measurement and any proposed additional interactions follow from the interpretation being considered. No Hamiltonian evolution is identified with Newman time merely from the presence of an exponential, and no new interaction or evolution law is settled here.

The [result index][results] and [patterns index][avoid] still apply, particularly [Newman reductions][newman], [controls][controls], [coordinate realizations][a03] and [scoped exclusions][a07]. This clarification selects a physical starting model and research emphasis; it proposes no excluding inequality or new theorem. The existing control screen in Proposal01 remains applicable to later mathematical claims. Formal planning and execution remain deferred while TND-B00 continues.

[proposal]: 01_HIGH_LEVEL_RESEARCH_PROPOSAL_20261105.md
[mc]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/manuscript/main.tex
[observables]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md
[radial]: ../../../05_radial_theta_collision_geometry/book/main.tex
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[newman]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
