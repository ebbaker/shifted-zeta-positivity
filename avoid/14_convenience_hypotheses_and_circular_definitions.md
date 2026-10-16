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

- [Wilson-lines continuation, session 3](../papers/susy-positivity/investigations/wilson-lines/notes/CONTINUATION_20260917_SESSION3.md) §3: "Hypotheses added for the convenience of a Cauchy–Schwarz step are where the physics went."; "each restrictive hypothesis … excluded precisely the amplitude that matches" (manuscript §11.6 retracted).
- [Topological-bulk evaluation](../papers/susy-positivity/investigations/previous/topological-susy-bulk/archive/reviews/EVALUATION.md): "The exact change and tangent prediction have opposite signs on this input." (the scalar coherent deformation was retired).
- [Codex brainstorm](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md): the proposed test of Lemma 18.1 at \(\kappa=3/4\) "already assumes β*≤(1+κ)/2=7/8. It is not an independent test"; the [amplification ledger](../papers/quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md): "a zeta-only seven-eighths assumption does not satisfy the positive-slot hypothesis".
- [02's continuation brief](../papers/investigations-2/active/02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md): "Defining `epsilon_R` as the unproved positive minimum of its left side would be circular."; [20's note](../papers/investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md): "dividing by a physical function at its unknown zeros would be circular."
- [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), scalar cones: "Using the unknown quotient \(V/W\) to prescribe coefficients would remain circular."; [coordination Note 11](../papers/investigations-2/active/22_theta_manifold_geometry/notes/00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md) adopted the rule rejecting proposals that only rewrite the trace or divide by the unknown jet.

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
