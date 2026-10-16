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

- [External review 12 of project 17](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) §3: "both are foregone conclusions"; [addendum 13](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md) §3: Note 20 "certifies a sign already known".
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §9: 21's \(|x|\le112\) region and 22's box lie inside the region where Polymath 15 and Platt–Trudgian already guarantee real simple zeros; rule R5 of the [brainstorm](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md) (as corrected in the [cross-assessment](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md) §3.1) says where that region ends.
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-09: an old script "whose printed failures never became a nonzero exit status"; its replacement was tested by injection ("an injected 0.001 error produces 4 FAILs and exit 1").
- [Formal replay scope review](../papers/investigations-2/formal_replay_crosswalk/reviews/FIRST_MILESTONE_SCOPE_REVIEW_20261012.md): a record with fabricated `reported_axioms` "returned success"; the [cross-family review](../papers/investigations-2/formal_replay_crosswalk/reviews/CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013.md): "An off-path `sorry` would compile with only a warning."
- [19's verification review](../papers/investigations-2/active/19_euler_factor_controls/reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md): interval negation "was not outward-rounded", so although the signs were never in doubt (raw margins at least \(5\cdot10^{-6}\)), "the certificates were not rigorous"; the Newman comparator "returns True" for \([-1,1]\) against \([0.5,2.5]\) (overlap, not containment).
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-18: "the experiment it unlocks cannot fail".

## What it cost

Certified cells and manuscript propositions that add no collision
coverage; regenerated certificates in 19; Newman records that must be
refreshed before reuse; a crosswalk whose labels were revised.

## Instead

Before certifying a region, check the published coverage and say in the
record whether the cell is inside it ([21's README table](../papers/investigations-2/active/21_quaternion_theta_geometry/README.md) is asked to say so); write every checker so that an injected error fails it, and record the injection; use containment tests and outward rounding; and present machinery tests as machinery tests, which is how 22's notes present theirs.
