# Numerical campaigns and budgets running ahead of the structural question

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A computation is extended (more horizon, more modes, a larger trial
space, more evaluations, a finer tuning) because it can be, without a
written statement of which structural question it decides and what
answer would stop it. The computation returns the same answer at higher
cost, or hits its budget, and the question is then settled analytically in
a paragraph.

## What it looks like here

Depth extension as an RH strategy; trial dimension 160 to 1280 with no
change; a signed cubature that spent its \(10^6\)-evaluation cap and
returned nothing usable where a direct evaluation took 24,000 callbacks;
amplification tuned to a limit that a published result beat anyway.

## Evidence

- [LESSONS_LEARNED](../notes/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md) §5: "the one recurring process failure was letting the numerical work run ahead of the structural question it was meant to answer."
- [Sonin option-1 outcome](../papers/investigations/sonin-critical-boundary/notes/OPTION1_AND_CONSTRAINED_SIGN_OUTCOME_20261003.md): trial dimension went 160→1280 and "None exceeds the inherited arithmetic upper endpoint 1.047808594."; the [arithmetic-storage assessment](../papers/investigations/program-meta-analysis/reviews/ARITHMETIC_STORAGE_PROGRAM_ASSESSMENT_20260929.md): the fixed trial space "provably misses most of the relevant trace".
- [Matched 01/18 results](../papers/investigations-2/brainstorm/reviews/MATCHED_01_18_AND_19_RESULTS_CODEX_20261014.md): "Each cell reaches exactly one million counted primitive evaluations … The validated nested integration returns no usable finite integral before this cap."; the absolute fallback \(|\mathcal L_0|<4.70\cdot10^{-52}\) against a true value near \(10^{-64}\), while the [baseline](../papers/investigations-2/brainstorm/notes/MATCHED_STATIONARY_BASELINE_20261014.md) used 24,000 callbacks.
- [Priority response review](../papers/investigations-2/brainstorm/reviews/PRIORITY_RESPONSE_REVIEW_CODEX_20261012.md): the amplification lane's best tuned limit lost to Liu by \(1.3\cdot10^{-7}\).
- [Program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md) §3, §10: "stop routine depth extension as an RH strategy"; "pause automatic growth of support windows, Fourier cutoffs, physical hierarchies and isospectral realizations."
- [CCM bounded audit](../papers/investigations/ccm-operator-realizations/notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md): the 4096-mode Schur certificate would need a cutoff \(\ge L\exp(c\,e^{L/2})\); the scalar test had already failed.

## What it cost

Computation time, and a sequence of records that had to be re-read as
"tests of the machinery"; the depth program was frozen; CCM's fixed-\(L\)
enlargement was suspended.

## Instead

"Pair every numerical campaign with a written statement of which
structural question it decides and what answer would stop it"
(LESSONS_LEARNED §5); write the four things the meta-analysis §10 asks for
before starting; attach a kill criterion with a number, as the
[11 October brainstorm](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md) does for every proposal and [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md) §1 does for the frontier lane. When a direct evaluation is cheaper than the method under test, the method's result is the cost comparison, and it is recorded as such.
