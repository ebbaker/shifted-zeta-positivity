# Research overview for radial integrand preservation and collision localization

27 October 2026, America/New_York. Rewritten for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007, **Explore collision-localizing deforms**.

**The primary program is to use deformations preserving the complete radial integrand to localize the cancellation at a hypothetical positive-time collision.** The equations, fields and auxiliary dynamics may change. The question is whether this freedom can expose a signed integral, boundary relation or dynamical constraint that is easier to control using the canonical theta data.

This overview and the rewritten [progress register][progress] govern current priorities. They replace the earlier sequence that began with interior nodes of the Darboux family. The existing filenames remain stable. The [earlier proposal][proposal] retains that branch's contracts; its first task is no longer the default continuation. The RTC and RLC programs remain historical foundations.

## The invariant and the available freedom

Write

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du
      =\int_1^\infty\mathcal I(t,z;r)\,dr,
\qquad
\mathcal I(t,z;r)=\frac18r^{3/2}Q_t(r)
                         \cos\!\left(\frac z2\log r\right).
\]

The variables satisfy \(r=e^{2u}\), with \(dr=2r\,du\). For normalized spherical averaging \(P\), the general requirement is

\[
\boxed{P\mathcal J_s(t,z;r,\cdot)=\mathcal I(t,z;r)
       \quad\text{at every radius}.}
\]

Here \(s\) is an auxiliary deformation parameter, separate from physical time \(t\). Preserving only the final integral is weaker than this requirement. In the \(u\) coordinate, the preserved density includes the corresponding Jacobian. A sufficient construction is a source field \(F_{s,t}\) with \(PF_{s,t}=Q_t\), but this factorization does not define the whole admissible class.

Radial symmetry, positivity of the deformed fields, a fixed potential, a fixed spectrum, an unchanged energy and Darboux form are not additional invariants. They may be useful features of a particular construction. Each proposed equation still needs a well-defined solution and observation map, with the regularity, convergence and boundary terms required by its argument. If a deformation depends on the running physical or spectral parameters, those derivatives must be included when recovering the physical jet.

The Laplacian gives a natural way to organize the freedom:

\[
P\Delta F=\Delta_3PF,\qquad
\Delta_3=\partial_r^2+\frac2r\partial_r.
\]

Thus zero-average angular components can evolve while the radial component stays fixed. The compact potential perturbation \(F=Q+\Delta\Psi\), \(P\Psi=0\), in [manuscript Section 9][manuscript] is one example. General preservation of the full density also permits other factorizations and equations.

## What localization is meant to achieve

Assume a candidate event

\[
H(T,a_*)=H_z(T,a_*)=0,\qquad T>0,\quad a_*>0.
\]

An exact deformation preserving \(H\) retains this event. It can change where the higher-dimensional fields carry the cancellation, which boundaries carry its flux, and how the signed contributions are estimated. It cannot erase a nonzero radial contribution by discarding its radius. Radial truncations therefore retain a complementary contribution or a proved tail bound.

The initial goal is a useful localization theorem on a declared finite domain. Possible gains include a signed boundary identity with more tractable terms, a controlled concentration law, or an auxiliary evolution that reduces a cost relevant to the collision equations. The eventual contradiction would require proving that the retained theta data cannot satisfy the localized event conditions. An impossible terminal state cannot simply be stipulated as the destination of the flow.

## Established constructions to build on

[Note20][n20] and [manuscript Sections 9–10][manuscript] give the following finite-parameter results, with [same-assistant assessment][review12].

| Construction | Available result | Consequence for the next calculation |
| --- | --- | --- |
| Normalized angular flow | \(A_s=e^{sq}/P(e^{sq})\), \(\partial_sA_s=(q-P(qA_s))A_s\), \(A_0=1\), \(PA_s=1\) | A continuous auxiliary ODE preserves the radial source exactly |
| Angular transport | \(\partial_sA+\operatorname{div}_{S^2}(A\nabla_{S^2}q)=0\), with an explicit solution for \(q=\omega\cdot n\) | A different driver moves angular mass along each sphere |
| Complete equation realization | \(\psi_s=A_s\psi\), \(L_{\lambda,s}=A_sL_\lambda A_s^{-1}\), with the derived forcing and boundary operator | The averaged boundary observation remains \(-8H\), including its spectral derivatives when \(A_s\) is independent of the running spectral parameter |
| Collision-adapted directions | A radius-dependent axis gives an angular moment proportional to \((H,H_z,0)\) | The two collision cancellations have a concrete three-dimensional geometry |

For a fixed unit axis, \(q=\omega\cdot n\) and \(A_s=s e^{sq}/\sinh s\). For \(s>0\) and cap angle \(0<\delta<\pi\),

\[
P(A_s\mathbf1_{q\le\cos\delta})
\le\frac{e^{-s(1-\cos\delta)}}{1-e^{-2s}},
\qquad P(A_s^2)=s\coth s.
\]

The first formula quantifies angular leakage. The second records the increasing ordinary squared norm of a multiplied radial field. These are different parts of the localization budget.

To align the construction with the event, freeze \(a_*\) and a scale \(b>0\), and set

\[
v(u)=(\cos(a_*u),-bu\sin(a_*u),0),\quad
m(u)=|v(u)|,\quad n(u)=v(u)/m(u).
\]

With \(q(r,\omega)=n(\log r/2)\cdot\omega\) and \(\rho_T=e^{Tu^2}\Phi(u)\),

\[
\int_0^\infty\rho_Tm\,P(\omega A_s)\,du
=(\coth s-1/s)(H(T,a_*),bH_z(T,a_*),0).
\]

This concentrates the vector cancellation near the curve \(\Gamma(u)=e^{2u}n(u)\). The candidate frequency is a fixed construction parameter; it is not differentiated as the running argument of \(H\). The formula covers the first-jet condition at any multiplicity at least two, but supplies no higher-jet classification or all-height uniform estimates.

## A flow that selects the deformation

The prescribed cap families are starting models. [Brainstorm02][b02] proposes a broader Laplacian flow that chooses a zero-average perturbation by decreasing a localization cost.

For a fixed physical time, write \(F=Q_t+G\) on a bounded annulus \(\Omega=\{r_-<|X|<r_+\}\), \(r_->1\). Set \(G=0\) on its radial boundaries and \(G_0=0\). For a smooth exterior weight \(\chi_{\rm out}\ge0\) and \(\varepsilon>0\), the proposed equation is

\[
\partial_sG=\varepsilon\Delta G
 -(I-P)[\chi_{\rm out}(Q_t+G)].
\]

For smooth solutions, \(PG=0\) persists and

\[
\mathcal E(G)=\frac12\int_\Omega\chi_{\rm out}(Q_t+G)^2\,d^3X
 +\frac\varepsilon2\int_\Omega|\nabla G|^2\,d^3X,
\qquad
\frac{d\mathcal E}{ds}=-\int_\Omega|\partial_sG|^2\,d^3X.
\]

These conditional identities do not yet supply a global smooth realization. Existence and regularity, radial joins, the response equation and its boundary observation remain to be developed. The present objective measures source localization; deriving an objective from the actual collision identity would require the response variation and its adjoint. This task can be pursued without restricting the whole program to positive fields or multiplicative conjugation.

## Research questions and completion criteria

The LOC identifiers below track this revised program. They do not rename or mark complete the earlier RDZ tasks; their disposition is recorded in the [progress register][progress].

| ID | Research question | Required return |
| --- | --- | --- |
| LOC-01 | Which auxiliary equations preserve the complete radial density and give usable response maps? | A stated family, parameter domain, observation and derivative map, with full forcing, boundaries and regularity; extend beyond the existing examples only for a defined use |
| LOC-02 | Does localization near the collision-adapted curve improve a signed calculation? | A complete finite-tube identity and quantitative comparison including exterior mass, radial tails, steering derivatives and all boundary terms; or a precise limitation for the tested comparison |
| LOC-03 | Can a projected Laplacian flow choose a useful deformation? | A well-posed bounded evolution and proved dissipation law, followed by a justified response/boundary realization and assessment of the objective's relevance to collision cancellation |
| LOC-04 | Which estimate uses the fixed canonical marginal to distinguish theta? | A proved signed estimate or compatibility relation on a stated domain, with its canonical input and its behavior on colliding controls identified |
| LOC-05 | Can a localized result exclude the event required by a positive threshold? | The logical transfer with the necessary time, height, tail and multiplicity coverage, or an exact statement of the remaining gap |

LOC-02 is the immediate bounded calculation. LOC-03 is an early complementary route if the prescribed concentration families only transport the old difficulty. LOC-01 supports both as needed; a classification of every possible deformation is not a prerequisite. LOC-04 begins when an actual signed quantity or response functional has been identified. LOC-05 depends on a proved result adequate for the [existing finite-event reduction][threshold].

## The next bounded calculation

Fix a finite candidate \((T,a_*)\), a finite deformation range \(0\le s\le S\), a cap angle, and a bounded radial annulus. Use the explicit steered profile and its selected response from Note20. On the angular tube

\[
\Omega_\delta=\{r_-<r<r_+,\ \omega\cdot n(\log r/2)>\cos\delta\},
\]

derive the complete forced Green identity for the response and its spectral derivative. Retain the drift and potential introduced by conjugation, the lateral boundary, both radial faces and the dependence of the axis on radius. A physical event does not impose an unproved zero condition on an arbitrary tube boundary.

Then reconnect this finite calculation to the full observation: account for the complementary angular region and the omitted radial intervals. The cap estimate bounds angular mass; it does not automatically bound every response or boundary term. Determine which parts are exact pullbacks of the radial identity and which signed term has become more tractable. Compare against the one-dimensional calculation using the same source information and error allowances.

Check the exact Gaussian-polynomial collision during the derivation. A complete return is a proved localized identity with a substantive comparison, a new controlled structural consequence, or a scoped obstruction for the chosen estimate. Merely recovering \(H\) again does not complete LOC-02. Save the derivation and assessment before selecting a larger family or a numerical campaign.

## Controls and the standard for progress

The existing [control screen][b01] shows that the normalized constructions retain the Gaussian-polynomial event and the observations of the applicable smooth [registered controls][controls] on their convergence domains. The controls lack the fixed canonical marginal in the specified ways; that alone does not show they fail an unproved separating inequality. Atomic controls require a measure or distribution formulation rather than an assumed smooth PDE.

Structural results may hold for colliding controls. A claimed theta exclusion must identify the canonical input actually used and prove its effect on the proposed estimate. The complete energy in the induced measure \(A_s^{-2}d^3X\) pulls back to the original identity; ordinary full source norms with radial weights do not improve under normalized multiplication. Those comparisons leave other signed local estimates and nonmultiplicative deformations open.

Use the [result index][results] and [avoid index][avoid], especially [geometric realizations][realizations], [target classification][a01], [control screening][a02], [transported identities][a03] and [scoped exclusions][a07]. The all-positive-time collision exclusion remains the existing final-strength target, not a new criterion validated by these constructions. Finite-domain gains and precise structural theorems are assessed at their actual scope.

## Earlier work and records

The Darboux family and local zero-motion formulas in [Notes17][n17] and [18][n18] remain available comparison tools. Its conserved pairing is an integrated observation: pointwise preservation requires the derivative correction displayed in manuscript Section 9. Interior Darboux node classification is an optional supporting branch, not a gate before studying localization. Earlier flux, moment, lattice and Gaussian-deformation results retain their stated scopes.

Keep one active manuscript. Put research derivations in `notes/`, assessments in `reviews/`, and justified computations with small records in `numerics/`. The [progress register][progress] owns current task states, [CURRENT_RESEARCH_PROGRAM.md][current] routes the next session, and [Note19][handoff] carries the updated continuation priority. This rewrite reorganizes the program around the user's invariant; it adds no collision-excluding theorem.

[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[proposal]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[n20]: ../notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md
[review12]: ../reviews/12_RADIAL_INVARIANT_AND_ANGULAR_FLOW_SELF_ASSESSMENT_20261027.md
[b01]: ../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md
[b02]: ../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md
[n17]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[n18]: ../notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[realizations]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[current]: ../CURRENT_RESEARCH_PROGRAM.md
[handoff]: ../notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
