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

- [LESSONS_LEARNED](../papers/weil-positivity/shifted-zeta/storage-depth/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md) §5: "the one recurring process failure was letting the numerical work run ahead of the structural question it was meant to answer."
- [Sonin option-1 outcome](../papers/investigations/sonin-critical-boundary/notes/OPTION1_AND_CONSTRAINED_SIGN_OUTCOME_20261003.md): trial dimension went 160→1280 and "None exceeds the inherited arithmetic upper endpoint 1.047808594."; the [arithmetic-storage assessment](../papers/investigations/program-meta-analysis/reviews/ARITHMETIC_STORAGE_PROGRAM_ASSESSMENT_20260929.md): the fixed trial space "provably misses most of the relevant trace".
- [Matched 01/18 results](../papers/investigations-2/brainstorm/reviews/MATCHED_01_18_AND_19_RESULTS_CODEX_20261014.md): "Each cell reaches exactly one million counted primitive evaluations … The validated nested integration returns no usable finite integral before this cap."; the absolute fallback \(|\mathcal L_0|<4.70\cdot10^{-52}\) against a true value near \(10^{-64}\), while the [baseline](../papers/investigations-2/brainstorm/notes/MATCHED_STATIONARY_BASELINE_20261014.md) used 24,000 callbacks.
- [Priority response review](../papers/investigations-2/brainstorm/reviews/PRIORITY_RESPONSE_REVIEW_CODEX_20261012.md): the amplification lane's best tuned limit lost to Liu by \(1.3\cdot10^{-7}\).
- [Program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md) §3, §10: "stop routine depth extension as an RH strategy"; "pause automatic growth of support windows, Fourier cutoffs, physical hierarchies and isospectral realizations."
- [CCM bounded audit](../papers/investigations/ccm-operator-realizations/notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md): the 4096-mode Schur certificate would need a cutoff \(\ge L\exp(c\,e^{L/2})\); the scalar test had already failed.

- [Effective arithmetic-tail continuation, Note 11](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md),
  18 October 2026: “These are measured finite costs, not a complexity law or
  a matched speed comparison.” The omitted-mode estimate improves
  analytically, while retained quadrature dominates the two bounded point
  cases. [Review 10](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md) keeps that distinction;
  reducing an already subdominant tail does not supply the global physical
  margin. Added for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**, same-model internal review.

- **BW12 boundary-only data comparison (21 October 2026).**
  [Note 03](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md)
  records: “This thin-box implementation does not establish a boundary
  advantage.” A full-source charge certificate succeeds, but every
  direct tensor-cell vertex is already on the outer boundary. Direct
  exclusion reuses the same data, has a stronger paid margin and needs
  fewer consumer operations. Boundary-only acquisition does not by
  itself establish a saving; compare actual data reuse before enlarging
  a mesh. The stop is scoped to that declared implementation.
  [Same-assistant review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/03_TWO_ZERO_THETA_COMPARISON_REVIEW_20261021.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no independent validation.

## What it cost

Computation time, and a sequence of records that had to be re-read as
"tests of the machinery"; the depth program was frozen; CCM's fixed-\(L\)
enlargement was suspended.

## Instead

"Pair every numerical campaign with a written statement of which
structural question it decides and what answer would stop it"
(LESSONS_LEARNED §5); write the four things the meta-analysis §10 asks for
before starting; attach a kill criterion with a number, as the
[11 October brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md) does for every proposal and [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md) §1 does for the frontier lane. When a direct evaluation is cheaper than the method under test, the method's result is the cost comparison, and it is recorded as such.

## Explicit outer constants still need a feasible bridge

18 October 2026, for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Investigation 3/11, Note 14](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md)
sharpens exp(64/epsilon) to exp(20/epsilon), but says: “The narrowed gap
is not a reason to launch a height scan”. Its present explicit-mode rule
still requires >10^433 retained modes at exp(2000). This is a scoped
resource obstruction for that enumeration, not a lower bound for other
assembly or oscillatory methods. [Review 12](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md)
retains the missing physical margin and global bridge.

20 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**. [Actual-profile Note 06](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/06_ACTUAL_PROFILE_OBSERVATIONS_AND_RELAXED_DUAL_FAILURE_20261020.md) acquires actual theta values before assessing the selected count dual and proves its objective is at least one even with zero observation error. “more precision cannot repair this fixed relaxation.” This stops only the specified three-observation positive-measure class, not all finite profiles or integer-sensitive estimators. [Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/reviews/03_FOURTH_ORDER_AND_ACTUAL_PROFILE_ROUND_REVIEW_20261020.md).
