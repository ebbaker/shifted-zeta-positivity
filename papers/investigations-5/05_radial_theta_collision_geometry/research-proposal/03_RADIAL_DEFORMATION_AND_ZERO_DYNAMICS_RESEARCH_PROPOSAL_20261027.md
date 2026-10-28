# Research proposal for radial deformations and zero dynamics

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**.

**Priority.** This proposal and the new [overview][overview] supersede the earlier RTC and RLC research plans for selecting future work. Edward Baker requested a thorough study of the deformations before deciding how they help with theta forcing. The earlier plans and their results remain historical inputs. The new [progress register][progress] alone owns RDZ task states; no RTC or RLC completion is counted again.

The initial [manuscript][manuscript] supplies an exact family of radial systems with unchanged physical H. This proposal asks what can be learned from that family as a dynamical and geometric object. The eventual positive-Lambda contradiction is a motivation, not an assumption about the intermediate results.

**27 October scope extension, chat0007.** Edward Baker specified preservation of the complete radial integrand as the sole invariant and requested auxiliary dynamics for localization. [Note20](../notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md) now supplies a normalized angular flow, transport flow, exact deformed operator and boundary map, cap costs and a steered first-moment representation. [Brainstorm02](../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md) proposes further tube and projected-Laplacian work. The Darboux-specific contracts below apply to that branch; they do not restrict all admissible realizations. Broad RDZ tasks remain open. Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra, actual effort max.

## Common mathematical contract

Use the complete selected response Y, its source g_t, and the definitions in [Notes17][n17] and [18][n18]. Physical time t, spectral parameter lambda=a^2/4, spatial coordinate x=log r, and deformation parameter kappa are distinct. For the first tasks choose symbolic compact sets 0<=t<=T, 0<lambda_-<=lambda<=lambda_+, 0<=kappa<=K, and 0<=x<=X as needed. Localizing in x does not replace the selected tail or silently impose a new endpoint condition.

The initial identities include U=(partial_x-w)Y, h=(partial_x-w)g, w=kappa tanh(kappa x), U(0)=B=-8H, V=U_lambda, and the exact inverse with denominator lambda+kappa^2. At kappa=0, U=Y'; the family is regular in mu=kappa^2 on compact x sets. Its physical-time source law contains both x^2h/4 and xg/2. Its energy identity includes both lower boundary terms away from an event.

Broader constructions must specify the operator, forcing, observation, function class, selected tails, parameter domain and inverse or loss of invertibility. An observation preserved up to a factor requires that factor to be proved nonzero on the stated domain. Its spectral derivative and boundary terms must also be retained.

## RDZ-01 Understand the explicit deformation family

Study the geometry of the cosh-seed family, its radial potential, its source transformation and its admissible parameters. Distinguish the differentiated realization at kappa=0 from an identity on Y. Describe the utility and limitations of mu=kappa^2. Determine what remains uniform on bounded sets and what additional hypotheses would be needed for large deformation, large radius or small spectral parameter.

**Deliverable:** a precise description of the selected family and one new endpoint, domain or geometric result. An uncontrolled limit kappa->infinity cannot be used as a simpler terminal system. No spectral semigroup or operator equivalence on an unspecified space is assumed.

## RDZ-02 Understand the coupled dynamics

Derive and compare evolution in t, lambda and kappa for the responses, forcing and observation. Check compatibility of the explicit equations, including derivatives of the inverse denominator and source terms. Determine whether a useful finite subsystem exists for a declared purpose, or characterize the residual hierarchy it leaves. Ordinary commutation of smooth parameter derivatives is an audit, not by itself evidence of an integrable structure.

**Deliverable:** a complete coupled evolution statement with its domain and boundary map, plus a structural consequence or a scoped closure obstruction. The original physical heat equation must be recovered at x=0. This task need not produce a theta estimate.

## RDZ-03 Study interior nodal geometry and physical zero motion

Start from the simple-node velocity in Note18, then study where it ceases to apply. Classify a declared class of interior events U=U_x=0 using the actual local derivatives in x and the auxiliary parameter. Keep these distinct from physical events U(0)=U_lambda(0)=0. Account for nodes entering or leaving through x=0 and x=X before making a finite-domain count statement. Higher-order degeneracies require their own scope; a generic double-node calculation is not an all-multiplicity theorem.

Investigate whether an orientation, a comparison principle, or a quantity attached to interior nodal sets has a useful relation to the unchanged boundary observation. The Gaussian-polynomial control shows that interior nodal absence alone is insufficient. A valuable outcome may be a precise correspondence, an obstruction to one proposed correspondence, or a new local model that clarifies the dynamics.

**Deliverable:** a proved local classification or complete transport law for a stated class, with an explicit boundary interpretation and a control check. No claim about a physical collision follows solely from the existence of an auxiliary fold.

## RDZ-04 Extend and compose admissible deformations

After the basic family is understood, select one extension: a different nonvanishing seed, a finite composition, or a justified integral intertwiner. Derive its complete forced equation and observation map. Keep spectral dependence of seeds, coefficients and boundaries if introduced. Determine the exceptional parameters and whether a composition retains radial form and the original selected response.

**Deliverable:** one explicit extension with a proved observation and multiplicity map, or a classification/obstruction for a clearly declared class. A general literature result about homogeneous equations does not automatically supply the forced theta boundary map. Broad searches over unconstructed operators are not the default first step.

## RDZ-05 Identify invariant pairings and additional constraints

Study conserved integrals, bilinear pairings, currents and variation identities available in the deformed equations. Distinguish a transported identity from an additional independent constraint. Note17 already establishes the exact transformation of the ordinary norm-plus-forcing identity, including its boundaries. Reprinting that equality for more parameter values does not add event information.

**Deliverable:** a new conservation, comparison or independence statement with all boundary terms, or a scoped proof that a selected candidate contains only the known boundary residual. This may be a structural result with no sign assertion. A positive homogeneous operator cannot replace the actual forced system without a proved map.

## RDZ-06 Bring in the complete theta source

Begin a focused canonical application only after the relevant structural question has been resolved well enough to identify what theta information it could use. Possible inputs include the simpler positive flux, complete square-mode tails, source derivative relations, or the canonical nonlinear theta equations. Choose the input because the developed deformation theory needs it.

**Deliverable:** one actual theta-dependent distinction or complete estimate, with its domain, comparison and control premise. This phase may reveal that an earlier structural result is useful in a way not anticipated here. It is not restricted in advance to bounding the forcing integral by its absolute value.

## RDZ-07 Assess a contradiction under positive Lambda

Read the existing [positive-threshold analysis][threshold] and its underlying finite-event reduction before importing it. Under a hypothetical Lambda=T>0, the reduction needs exterior localization uniform near T and gives a finite real event of multiplicity at least two. A later deformation result could rule out that event through a compatibility condition, a global quantity with complete boundaries, a valid characteristic realization, or another proved implication.

**Deliverable:** the exact logical bridge from an acquired RDZ result to the canonical event, or a specific list of the missing steps. Cover the required heights, times and multiplicities; distinguish a fixed positive slab from all positive times and from simplicity at time zero. Real ordered-zero methods cannot be used below an unproved all-real threshold. A final-strength collision criterion is stated once as an application requirement, not counted as supporting evidence for RH.

## RDZ-08 Verification and records

Use direct proofs first. When needed, an exact algebra replay may check the parameter and boundary bookkeeping; a controlled numerical illustration may show a proven local model; a rigorous enclosure may evaluate a constant required by a theorem. Each computation must state its analytic consumer and errors. Do not begin a numerical campaign to decide a global deformation or collision assertion by sampling.

Test the explicit colliding source first, then the relevant [registered control families][controls] at their actual premises and convergence domains. Generic Phase I laws should remain compatible with their events. A canonical separating claim must identify the additional premise and prove its quantitative effect. Keep same-assistant review, separate-model review and specialist review distinct.

## First bounded work package

**Selected question:** how do simple interior zeros and their first degeneracies behave in the existing radial family, and what can their transport say about the fixed boundary observation?

1. Fix a symbolic compact domain and the source class. Start with the full canonical response and the exact Gaussian-polynomial control; clearly label any broader smooth-source theorem.
2. Use mu=kappa^2 near zero and derive the required first and second local jets from the exact forced and deformation equations. Verify mixed derivatives with the full source law.
3. Analyze a stated nondegenerate interior multiple-node class. Determine its local orientation if the hypotheses decide one; otherwise exhibit the unresolved sign or a counterexample. Do not presume monotonicity.
4. Include spatial boundary crossings before proposing a zero-count law. Keep physical spectral multiplicity separate from spatial node multiplicity.
5. Compare the auxiliary behavior with the unchanged H,H_a observation. State precisely what new information the result supplies and what relation remains unproved.
6. Save one focused proof note and an assessment. Update the new progress register. Choose any computation only after its role in this analytic question is clear.

A complete local classification or a precise failed correspondence can satisfy this package without a theta-specific exclusion. Merely restating the already recorded simple-node velocity cannot. The next task is selected from what this study actually reveals, rather than automatically returning to the previous flux optimization.

## Records and continuity

Follow the [result index][results] and [avoid index][avoid], especially [local collision geometry][geometry], [controls][controls], [target classification][a01], [scoped exclusions][a07] and [coupled estimates][a12]. Respect the [large-file policy][largefiles], [reference workflow][references] and [chat-history workflow][history]. Notes, numerics and reviews remain in their established folders. Edit the single base-folder manuscript in place and record concise milestones in DRAFT_HISTORY.md; no snapshot folders are created.

The first session follows the [continuation note][handoff]. Current results and proposed work are separated in the [progress register][progress]. The creation of this proposal is not completion of its research tasks.

[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[handoff]: ../notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[n17]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[n18]: ../notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[largefiles]: ../../../../LARGE_FILES.md
[references]: ../../../../REFERENCE_WORKFLOW.md
[history]: ../../../../tools/CHAT_HISTORY.md
