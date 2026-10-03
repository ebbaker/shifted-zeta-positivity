# Manuscript integration of the single probe results

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed in this session and are not inferred. The mathematical
cross-checks were performed by separate agents of the same model; they
are not independent specialist refereeing.

## Revised manuscript

The current [manuscript](../manuscript.tex) now contains Section 10,
“Prepared-source criteria and finite translate certificates.” It integrates
the [single-probe theorem](../notes/SINGLE_PROBE_GROWTH_THEOREM_20261003.md),
[centered negative-index bound](../notes/CENTERED_NEGATIVE_INDEX_SHARPENING_20261003.md),
and [seven-source certificate](../numerics/single_probe_joint_20261003/README.md).
The [preceding research review](ALL_WINDOW_OUTCOME_REVIEW_AND_CONTINUATION_20261003.md)
records the original mathematical and numerical assessment.

The new section supplies the source domain and moment conventions,
polynomial probe, elementary transform zero-location proof, exact
covariance and Laplace identities, seven equivalent all-window criteria,
and quantitative consequences of a hypothetical off-critical zero.
It also proves the explicit centered negative-index and correction-rank
bounds, and states the seven-source Gram comparison as a computer-assisted
proposition with its full error treatment and reproducibility references.

The abstract, introduction, scope, bibliography, and LLM acknowledgement
were revised to match. The earlier claim that every result is analytic
was replaced with an explicit distinction between analytic theorems and
the numerical certificates. The old statement about a fixed source family
was narrowed to a fixed finite list or fixed support window: one profile
with unbounded translations still retains the all-support quantifier.

The obsolete mean-only correction proposal was removed from the open
questions and replaced with the current signed comparison and weighted
growth target. The scope cites the later first-prime obstruction, without
reproducing that separate proof or treating positive correction as a
negative Weil form. The earlier local relative-comparison certificates
remain in their existing research notes.

## Checks completed

The two new mathematical fragments received separate same-model cross
checks and primary-agent review before integration. The checks covered
Fourier and sesquilinear conventions; compact-support form approximation;
the transform parameter 19/2 and weighted ODE; the uncanceled zero residue;
all seven implications; the Dirichlet/concavity argument and strict ceiling
index; and the factors in the diagonal and off-diagonal covariance formulas.

All seven displayed pivot lower bounds were compared with the exact rational
endpoints at both recorded precisions. The scalar root bracket and its
displayed density endpoints were also checked against the exact record.
The manuscript distinguishes pivot bounds from eigenvalue bounds, and
states that the verified comparison covers only the seven-dimensional
span, including arbitrary complex coefficients. The earlier numerical
package and its independent rational interval audit were not changed.

The assembled source has 165 distinct labels and 181 reference uses, with
no duplicate labels, unresolved source references, missing bibliography
keys, or unbalanced LaTeX environments. The built-in desktop LaTeX compiler
reported **success** for the revised current manuscript on 3 October 2026.
This records compilation of the saved source, not merely a request to open
the editor. No source-repair cycle was needed.

The author field remains “Drafted for Edward Baker,” and the acknowledgement
now includes assistance with numerical implementation and auditing. The
existing [draft history](../DRAFT_HISTORY.md) and [investigation index](../README.md)
were updated. No manuscript snapshot folder or separate draft was added.

## Source binding and remaining scope

Repository baseline: `ea0ec42c0d14270497525286dace08bc0df476dd`.

Previous manuscript SHA-256:

    f48309c50261d01b46023c6255c10ad8e784f8f92329c1357b91e11f9e293fc8

Integrated manuscript SHA-256:

    5fe7539ce73baa2bbb852a620426c2d5b4e63e236785cd3e26731611422122c6

This is an uncommitted working-tree revision. The source hash identifies
the version compiled and reviewed here; it is not mathematical evidence.
All added and edited files are below the repository's small-file limit.
The global signed growth estimate, all-window positivity, and RH remain
unproved. The manuscript claims the equivalence and the stated finite
certificate, not a proof of their unresolved global hypothesis.
