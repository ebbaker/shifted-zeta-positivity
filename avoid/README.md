# Patterns to avoid

15 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max.

## Purpose

This folder records the recurring ways in which this project has lost
time, overstated what it had, or had to retract something, each backed by
specific evidence from the repository. It exists because the same mistakes
have recurred across programs written weeks apart by different models, and
the lessons were recorded in notes that later investigations did not read.
The companion folder [`result-summaries/`](../result-summaries/README.md)
holds what the project established; this one holds how it got in its own
way.

Every pattern here was found by the project's own reviews, often the
model that made the mistake reviewing itself later, and several were made
by the model writing this folder. The anecdotes are quotations with paths,
so a reader can check the context, and they are chosen for what they cost:
a retraction, a withdrawn claim, a broken file, a week of notes with no
gain. None of this is a verdict on the research directions; a closed
branch is not a mistake, and the repository's rule that inactive status
"does not assert mathematical impossibility" applies here too.

## Structure

One file per pattern, numbered roughly from the mathematical to the
procedural. Each file has the sections *The pattern*, *What it looks like
here*, *Evidence* (paths and quotations of at most a sentence), *What it
cost*, and *Instead*, which points at the repository rule that now
addresses it or states one when none exists. Links are relative to this
folder.

| File | Pattern |
| --- | --- |
| [01](01_restating_the_target.md) | Restating the target in new words and counting it as progress (the criterion treadmill) |
| [02](02_shape_only_arguments_and_the_controls.md) | Arguments whose premises the collision controls also satisfy |
| [03](03_lifts_and_re_realizations_in_new_coordinates.md) | Lifting the flow or re-realizing an already positive object in new coordinates |
| [04](04_counts_and_precision_as_evidence.md) | Assertion counts, replay totals and numerical precision read as evidence |
| [05](05_same_model_reviews_and_shared_premises.md) | Same-model reviews and shared-premise checks treated as independent |
| [06](06_status_stronger_than_the_evidence.md) | Status words, headlines and novelty claims stronger than the evidence |
| [07](07_scoped_exclusions_read_as_universal.md) | Scoped exclusions upgraded into universal no-go statements |
| [08](08_normalization_and_constant_slips.md) | Normalization, factor-of-two, endpoint and constant slips |
| [09](09_round_floors_and_fitted_laws.md) | Round targets reported as measurements; finite data turned into laws |
| [10](10_numerics_ahead_of_the_question.md) | Numerical campaigns and budgets running ahead of the structural question |
| [11](11_certifying_the_known_and_tests_that_cannot_fail.md) | Certifying what known results already force, and tests that cannot fail |
| [12](12_term_by_term_matching_and_separate_bounds.md) | Term-by-term matching, separate absolute bounds, separately positive sectors, dropped small terms |
| [13](13_a_factor_is_not_the_target.md) | Realizing one factor, a boundary phase or a positive state space and calling it the target |
| [14](14_convenience_hypotheses_and_circular_definitions.md) | Convenience hypotheses that exclude the matching case; definitions that assume the conclusion |
| [15](15_ignoring_sibling_results_and_unfinished_closures.md) | Not reading sibling results and stop lists; closures recommended but never written |
| [16](16_unchecked_imports_and_novelty_claims.md) | Facts imported from the literature or from PDFs without checking the source |
| [17](17_parallel_writers_and_broken_registries.md) | Two clones writing the same files: conflict markers and duplicate registrations |
| [18](18_snapshots_large_files_and_work_outside_the_tree.md) | Snapshot sprawl, large data in history, and work that exists only outside the tree |
| [19](19_status_files_that_lag_the_findings.md) | Status files, READMEs and manuscripts that lag the findings of audits |
| [20](20_volume_without_a_gain.md) | Manuscripts and notes that grow without a quantitative gain |

## Maintenance

Add a pattern only with evidence: a path and a quotation from a review,
note or status file in the tree, and what it cost. Prefer extending an
existing file to opening a near-duplicate. When a rule is adopted that
addresses a pattern, add it under *Instead* with its path. Do not soften
an entry because the model that made the mistake is the one editing the
folder. Record the model that wrote or revised an entry.
