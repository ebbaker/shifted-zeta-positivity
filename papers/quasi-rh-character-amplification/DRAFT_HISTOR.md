# Manuscript history

Keep one editable [manuscript.tex](manuscript.tex); no draft snapshot folders.
Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

| Date | Investigation | Snapshot path or commit/tag | Why this version matters | Evidence |
| --- | --- | --- | --- | --- |
| 2026-10-08 | Conductor localization of the mixed inverse/plain moment | [Working-tree manuscript](manuscript.tex); no commit, tag, or snapshot created | First manuscript: explicit analytic inputs, proof of the ideal-pair estimate, three-block reduction, and conditional count payoff; the final signed estimate remains open | [Manuscript review](reviews/MANUSCRIPT_REVIEW_20261008.md), [combined derivation](notes/MIXED_MOMENT_REDUCTION_20261008.md), [payoff](notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md) |

The same working-tree source now also contains the
[selector feasibility calculation](notes/SELECTOR_FEASIBILITY_20261008.md)
and the [live-divisor refinement](notes/LIVE_DIVISOR_TRANSFORM_20261008.md),
including a proved mean-zero principal-layer subcase. The
[selector review](reviews/SELECTOR_FEASIBILITY_REVIEW_20261008.md) and
[input review](reviews/CONTINUATION_INPUT_REVIEW_20261008.md) record the
scoped checks. These are in-place continuation edits, not a new commit,
tag, or snapshot milestone; the full mixed estimate remains open.

The next in-place continuation adds the
[two-conductor refinement](notes/SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md),
the [selector-preserving mixed subcases](notes/SELECTOR_PRESERVING_SUBCASES_20261008.md),
and the [narrower sufficient application domain](notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md).
The [new review](reviews/SELECTOR_PRESERVING_REVIEW_20261008.md) records
their hypotheses and exact checks. The mixed saving inside the remaining
buffered triangle is still unproved; no boundary or commit milestone has
been advanced.

The current source compiles with the built-in LaTeX compiler. Detailed
research and verification history stays in the linked notes and reviews.
Future milestones should reference commits or tags rather than new snapshots.
