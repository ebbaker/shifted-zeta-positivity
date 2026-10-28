# Radial deformations and zero dynamics research overview

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**.

**This is the primary research program for Investigation05.** At Edward Baker's request, it supersedes both the [RTC overview][rtc] and the [RLC overview][rlc] for research priority, together with their earlier next-session instructions. Their proofs, controls and historical progress remain intact. The new [proposal][proposal] defines the work packages, the new [progress register][progress] records what is actually established, and the [continuation note][handoff] specifies the next session.

The priority is to understand radial deformations and their zero dynamics **before deciding how to use them against theta forcing**. A clearer structural theory can be worthwhile before it supplies a sharper theta estimate. The longer-term motivation is an alternative view of the system that could contribute to a contradiction under a hypothetical positive de Bruijn-Newman threshold. That application remains open.

## The starting result

The [working manuscript][manuscript] consolidates the initial results, with the editable source in this investigation's base folder. It contains the canonical radial source and flux, the selected forced response, the exact Darboux family, a conserved integral, physical and auxiliary evolution laws, the complete energy comparison, and a colliding control. [Note17][n17] supplies the original family; [Note18][n18] records the elementary zero-motion corollaries. [Review11][review] states the verification and manuscript scope.

With x=log r, lambda=a^2/4>0 and g_t(x)=4 exp(t x^2/4) Phi(x/2), retain

\[
Y_{xx}+\lambda Y=g_t,\qquad B=Y_x(0)=-8H(t,a).
\]

For kappa>=0, define

\[
w_\kappa=\kappa\tanh(\kappa x),\quad
U_\kappa=(\partial_x-w_\kappa)Y,\quad
h_\kappa=(\partial_x-w_\kappa)g_t.
\]

Then

\[
U_{\kappa,xx}+[\lambda+2\kappa^2\operatorname{sech}^2(\kappa x)]U_\kappa=h_\kappa,
\qquad U_\kappa(t,0;\lambda)=B(t,\lambda).
\]

The physical observation and its finite multiplicities are exactly unchanged. An explicit integral also retains -8H. In r, the system uses the usual three-dimensional radial Laplacian with an additional radial potential. Its forcing and inversion parity change in a specified way. The complete energy identity transports the old forcing cancellation; that fact limits that identity, not the entire deformation perspective.

## The central distinction between zero sets

| Object | What varies | What is currently known |
| --- | --- | --- |
| Physical zeros H(t,a)=0 | Observation frequency a and physical time t | Their locations and multiplicities are independent of kappa in the exact family |
| Interior response zeros U_kappa(t,x;lambda)=0 | Spatial coordinate x under t, lambda and kappa | A local simple-node velocity is available; bifurcations and complete zero transport remain to be studied |
| Physical multiple events | U_kappa(0)=partial_lambda U_kappa(0)=0 | These are spectral boundary conditions, not interior double nodes in x |
| Homogeneous characteristic zeros | A specified operator, domain and boundary problem | No characteristic determinant equal to H has been constructed |

The fact that physical zeros stay fixed under kappa does not make the auxiliary dynamics uninteresting. It makes any geometric information about the family available at the same physical event. A bridge from interior geometry to the boundary observation is a separate theorem. The explicit control already has no interior U zeros while retaining a multiple boundary zero, so that bridge cannot be an unqualified nodal-absence assertion.

## Three phases of work

**Phase I: understand the deformation systems.** Study their regular parameterization, inverses, selected tails, coupled evolution, interior nodal sets, boundary crossings, composition and invariant pairings. Start with the cosh seed and broaden only after its behavior is understood. Generic source results and exact controls are useful outputs of this phase. Immediate theta separation is not its completion test.

**Phase II: locate additional information.** Determine which structural quantities can use the actual theta source, or which deformations make an otherwise difficult constraint accessible. Distinguish identities forced by exact equivalence from an additional estimate or compatibility relation. The earlier source, flux and nonlinear theta equations remain available inputs, without dictating the first task.

**Phase III: connect the structure to the positive-threshold problem.** A later result must be transferred to the physical first jet with its full parameter coverage and multiplicity scope. A contradiction under Lambda>0 would require the existing finite-event reduction and a new reason its canonical event cannot occur. Alternative mechanisms may involve zero transport, compatibility, a global quantity with complete boundaries, or a valid characteristic realization; no one mechanism is selected in advance.

## Work packages

| ID | Subject | Intended output |
| --- | --- | --- |
| RDZ-01 | Geometry and regularity of the explicit family | Precise parameter domains, inverse maps, endpoint behavior, radial interpretation and admissible limits |
| RDZ-02 | Physical, spectral and deformation evolution | Complete coupled laws and compatibility, with source, boundary and tail terms retained |
| RDZ-03 | Interior zeros and their relation to physical zeros | Local event classification and complete transport on a stated domain; a proved boundary correspondence or its exact limitations |
| RDZ-04 | Wider deformation classes and composition | One explicit admissible extension or classification, including its physical observation map and exceptional parameters |
| RDZ-05 | Invariant pairings and structural constraints | A conservation or comparison theorem beyond merely reprinting the transported energy identity |
| RDZ-06 | Canonical theta specialization | A demonstrated theta-dependent structural or quantitative distinction, after the relevant deformation theory is understood |
| RDZ-07 | Positive-threshold transfer | A fully scoped implication toward excluding a hypothetical positive threshold, or an exact record of the remaining obstruction |
| RDZ-08 | Verification, literature and records | Accurate proofs, control tests, provenance and reproducible supporting computations throughout |

The [proposal][proposal] gives the full contracts. The first bounded package joins RDZ-01 through RDZ-03: interior nodal geometry of the existing family, including regularization by mu=kappa^2, local degeneracies and spatial boundary accounting. Re-deriving the conserved integral is a setup check, not the entire return.

## How earlier work is used

- The [radial foundation][n01], flux formulas and canonical tail bounds remain common input.
- [Note16][n16]'s fourth-moment exclusion and exact estimator comparison remain valid at their stated scopes. Optimizing that radius is no longer the default next task.
- [Note17][n17]'s final suggestion to seek an immediate forcing estimate is superseded by the structure-first order here.
- The Gaussian deformation's moving-event and boundary costs remain a comparison case. The present exact family keeps events fixed at every finite kappa; a singular infinite-parameter limit still needs its own analysis.
- The tested scalar multiplier and separate absolute flux losses remain scoped results. They do not establish a prohibition on studying other systems or stronger arguments in equivalent representations.
- Lattice and quaternionic constructions are background; no additional dimension or lattice is required by this program.

## Standards and status

Use the [result index][results] and [avoid index][avoid], especially [collision controls][controls], [local geometry][geometry], [geometric realizations][realizations], [target classification][a01], [scope][a07] and [coupled estimates][a12]. A structural theorem can complete a declared Phase I task without excluding theta collisions. Its content must be stated precisely: a new classification, correspondence, law, invariant, or scoped obstruction. A plan or repeated formula is not a completed theorem.

The unchanged-theta all-positive-time collision exclusion remains the previously recorded final-strength target. It is not a newly established criterion. A finite-domain result is assessed on that domain; a generic law is checked against controls rather than required to exclude them. When theta separation is claimed, identify and prove the effect of the canonical premise used.

Analytic work leads. Supporting computation may check algebra, illustrate a proved local model, or certify a constant required by a written theorem. Sampling does not decide bifurcation completeness, all-height behavior or threshold transfer. New proofs go in notes/, assessments in reviews/, and computations with small records in numerics/. Keep one active manuscript and the concise DRAFT_HISTORY entry; create no manuscript snapshots.

[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[proposal]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[handoff]: ../notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
[review]: ../reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md
[rtc]: 01_RADIAL_THETA_COLLISION_RESEARCH_OVERVIEW_20261027.md
[rlc]: 02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_OVERVIEW_20261027.md
[n01]: ../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n16]: ../notes/16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[n17]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[n18]: ../notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[realizations]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
