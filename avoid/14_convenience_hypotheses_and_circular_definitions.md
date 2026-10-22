# Convenience hypotheses that exclude the matching case; definitions that assume the conclusion

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A hypothesis is added to make a Cauchy–Schwarz step or a tangent
expansion go through, and it excludes precisely the case that matters; or
a constant is defined as the unproved positive minimum of the quantity it
is meant to bound; or a lemma is proposed as a test of a strip it already
assumes; or an expression is divided by a physical function at its
unknown zeros. The argument then proves its premise.

## What it looks like here

A retracted manuscript section; a tangent prediction with the wrong sign
at finite coupling; a "decisive diagnostic" that would have been circular;
a target divided by the unknown jet.

## Evidence

- [Wilson-lines continuation, session 3](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/CONTINUATION_20260917_SESSION3.md) §3: "Hypotheses added for the convenience of a Cauchy–Schwarz step are where the physics went."; "each restrictive hypothesis … excluded precisely the amplitude that matches" (manuscript §11.6 retracted).
- [Topological-bulk evaluation](../papers/weil-positivity/susy-positivity/investigations/previous/topological-susy-bulk/archive/reviews/EVALUATION.md): "The exact change and tangent prediction have opposite signs on this input." (the scalar coherent deformation was retired).
- [Codex brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md): the proposed test of Lemma 18.1 at \(\kappa=3/4\) "already assumes β*≤(1+κ)/2=7/8. It is not an independent test"; the [amplification ledger](../papers/quasi-rh/quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md): "a zeta-only seven-eighths assumption does not satisfy the positive-slot hypothesis".
- [02's continuation brief](../papers/investigations-2/active/02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md): "Defining `epsilon_R` as the unproved positive minimum of its left side would be circular."; [20's note](../papers/investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md): "dividing by a physical function at its unknown zeros would be circular."
- [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), scalar cones: "Using the unknown quotient \(V/W\) to prescribe coefficients would remain circular."; [coordination Note 11](../papers/investigations-2/active/22_theta_manifold_geometry/notes/00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md) adopted the rule rejecting proposals that only rewrite the trace or divide by the unknown jet.

- [S07-T1 Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md),
  19 October: “This rigid parent class cannot accommodate a nontrivial cutoff error.”
  The complete fourth source is not holomorphic; its profile-cutoff residual
  leaves the finite jet space and needs its actual complement. Restricting
  a reproducing-kernel estimate to the parent theta line would omit the
  object being estimated. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/03_CONSTRAINED_THETA_SPACE_INTERNAL_REVIEW_20261019.md).
  Added for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

- **BW12 analytic charge hypothesis audit (21 October 2026).**
  [Note 05](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md)
  proves a real-cap reduction but records: “The half-plane bound is on
  the derivative Psi'=mu. It implies injectivity and charge at most one,
  **not** charge zero.” The quadratic collision passes the phase bound;
  spatial-wall lower bounds and the missing cap sign remain inputs to
  prove, not quantities made positive by definition. [Self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/05_TWO_ROOT_DISCRIMINANT_AND_CAP_REVIEW_20261021.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no independent review.

  The subsequent [BW12 Note 06](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md)
  pays those inputs for one complete-theta window, with source-derived
  walls, counts and cap signs. Its matching event control still passes
  the wall and phase consumer. The [self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/06_COMPLETE_THETA_REAL_CAP_APPLICATION_REVIEW_20261021.md)
  records: “A useful phase bound does not itself supply the missing
  near-event sign.” The finite gap >12 does not resolve a degenerating
  endpoint. Added 21 October 2026 for Edward Baker with substantial LLM
  assistance, **gpt-6-astra, actual effort max**.

## What it cost

A retracted manuscript section; a retired deformation; a planned
diagnostic that would have tested nothing; 02 "blocked at the
source-dependent cancellation inequality".

## Instead

For every added hypothesis, check that the actual theta object satisfies
it (the matching amplitude, the matching source) before using it; for every
defined constant, say what proves it positive; for every proposed test,
state the hypothesis it assumes and confirm the test can fail. The
[investigations-2 README](../papers/investigations-2/README.md) rule 3 ("Model tests must preserve the hypotheses they challenge") and Note 11's rejection rule are the standing versions.

**A paid local window still admits the event, 21 October 2026.** Prepared
for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**.
[BW12 Note 07](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md) now pays the hypothetical-double
geometry from complete moments; its correctly retained charge is one.
For higher multiplicity, [Note 09](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md) proves:
“Even same positive cap signs permit a charge-six endpoint.” The missing
variable polynomial forcing cannot be omitted from the many-root
evolution. This screens the direct extension of that particular cap
consumer, not other theta-specific estimates. [Review 08](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md)
checks the complete roots, source dependence and scoped conclusion;
all review is internal to the same model configuration.

**Manuscript checkpoint, 21 October 2026.** The [BW12 manuscript](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/manuscript/main.tex)
retains the distinction between a strict matched-envelope improvement
and an actual sign: “A strict improvement over another enclosure can
still leave zero inside the resulting interval.” Its windows and
higher-root controls do not close the source-sign obligation.
[Same-model integration review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/09_MANUSCRIPT_INTEGRATION_REVIEW_20261021.md);
prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. No broader impossibility claim.
