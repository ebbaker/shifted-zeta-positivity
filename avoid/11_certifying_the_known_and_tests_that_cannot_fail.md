# Certifying what known results already force, and tests that cannot fail

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A certificate is produced for a region where published results already
guarantee the conclusion (real simple zeros below the Polymath barrier and
the Platt–Trudgian height), or a checker is written whose failure cannot
reach its exit status, whose comparator passes on overlap rather than
containment, or whose rounding is not outward. The record looks like
evidence and is either a test of the machinery or no test at all.

## What it looks like here

Certified cells at heights \(\le112\) and small heat times; "nonvacuous
bounded calibration" of signs that are foregone conclusions; a script
whose printed failures were never a nonzero exit; a record with fabricated
axioms that "returned success".

## Evidence

- [External review 12 of project 17](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) §3: "both are foregone conclusions"; [addendum 13](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md) §3: Note 20 "certifies a sign already known".
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §9: 21's \(|x|\le112\) region and 22's box lie inside the region where Polymath 15 and Platt–Trudgian already guarantee real simple zeros; rule R5 of the [brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md) (as corrected in the [cross-assessment](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md) §3.1) says where that region ends.
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-09: an old script "whose printed failures never became a nonzero exit status"; its replacement was tested by injection ("an injected 0.001 error produces 4 FAILs and exit 1").
- [Formal replay scope review](../papers/investigations-2/formal_replay_crosswalk/reviews/FIRST_MILESTONE_SCOPE_REVIEW_20261012.md): a record with fabricated `reported_axioms` "returned success"; the [cross-family review](../papers/investigations-2/formal_replay_crosswalk/reviews/CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013.md): "An off-path `sorry` would compile with only a warning."
- [19's verification review](../papers/investigations-2/active/19_euler_factor_controls/reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md): interval negation "was not outward-rounded", so although the signs were never in doubt (raw margins at least \(5\cdot10^{-6}\)), "the certificates were not rigorous"; the Newman comparator "returns True" for \([-1,1]\) against \([0.5,2.5]\) (overlap, not containment).
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-18: "the experiment it unlocks cannot fail".

- [Arithmetic contour finite consumer, Notes 12–13](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md),
  18 October 2026: “The lemma does not follow merely from a published
  canopy”. A complete certified complex wall supplies the missing finite
  boundary input; initial zero verification alone is not positive-time
  coverage. [Review 11](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md) also records the rejected
  finite quadrature enclosures and recomputed margins. Added for Edward
  Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**;
  same-model internal review, no global bound.

## What it cost

Certified cells and manuscript propositions that add no collision
coverage; regenerated certificates in 19; Newman records that must be
refreshed before reuse; a crosswalk whose labels were revised.

## Instead

Before certifying a region, check the published coverage and say in the
record whether the cell is inside it ([21's README table](../papers/investigations-2/active/21_quaternion_theta_geometry/README.md) is asked to say so); write every checker so that an injected error fails it, and record the injection; use containment tests and outward rounding; and present machinery tests as machinery tests, which is how 22's notes present theirs.

## Constructive-stability continuation, 17 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), effort ultra**. The [Project 05 cross-model review, Section 3](../papers/investigations-3/05_constructive_stable_models/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md) observes that the forward collision-control tables “cannot fail”: Hurwitz already excludes a nonreal-zero function as a complex-compact limit of real-zero functions. The [round-two reconciliation](../papers/investigations-3/05_constructive_stable_models/notes/round-2/README.md) replaces that evidentiary reading with a stable Bessel reverse control. A family also excluded for Bessel has an expressiveness limitation; this is not information about theta stability.


## Overview 02 bounded pilot on 18 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort max**. The [matched pilot note](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md)
records: “validation passed; the performance gate did not pass.” A smaller
propagated error and a local signed certificate on already covered territory
are machinery gains, not new collision coverage. The round stops scan
expansion and retains the global gap. Its control interface actually rejects
five surrounding event boxes; [adversarial replay](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md)
checks strict equality, invalid arithmetic, altered input bytes and broken
covers. The comparison is scoped to its measured implementation, not an
obstruction to all contour methods.
