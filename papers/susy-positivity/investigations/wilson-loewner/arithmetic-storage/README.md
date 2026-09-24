# Arithmetic storage: cumulative positivity and the first prime

**Second session (Claude, 24 September 2026; not committed).** The [review](reviews/review_claude_first_prime_session_20260924.md) finds the first session's numbers correct. The [research note](notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md) shows that every append hypothesis is joined-window central positivity (Lemma A). It closes the first-prime join with the unchanged weil-depth pipeline: Q(0,3/4) ≥ 4.92e-4, κ₀ ≤ 0.99980, normalized coupling < 0.99982 at ω = 10⁻³. It proves that joins of fixed length cannot keep a uniform margin, and certifies that positivity on (0, log 3) pins the prime-2 weight to [−8.2e-5, +3.2e-6] relative. Finite-append certificates should stop. See the [continuation](notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md).

The [first research session](notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md) certifies the local metrics for the first-prime append, proves that the prime repairs a negative gamma/pole witness, and exhibits a rigorous obstruction to the inherited 128-mode energy proxy. Complete-form finite-input tests are favorable, but the all-input mixed bound remains open. See the [continuation handoff](notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_INPUTS_20260924.md) and [numerics](numerics/README.md).

This Wilson–Loewner subprogram studies how the complete arithmetic response
could acquire a positive state norm, and how that norm could survive spatial
extension and the arrival of prime delays. It joins the existing cumulative
continuation method to the unresolved semilocal Sonin comparison, with a
focused canonical-system comparison as a supporting direction.

Start with the [program and goals](notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md).
The [notes index](notes/README.md) records the current starting point.

The first normalized append is **already completed internally** in the
[critical-path certificate](../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md):
its all-input relative bound is below 0.951. Specialist review is outstanding.
The new task is to identify what survives beyond that prime-free example,
especially at the first prime. No first-prime storage theorem, all-depth
continuation, or physical realization is claimed here.

This folder belongs within Wilson–Loewner because it develops the parent's
cumulative-storage and arithmetic-response target. Existing proof files remain
in [critical-path](../../critical-path/README.md); WZW and N4SYM retain their
physical investigations. This package coordinates the new comparison and
extension work without duplicating those records.

New research belongs in `notes/`, future numerical work in `numerics/`, and
future reviews in `reviews/`; create the latter folders when they contain work.
Follow the repository [large-files policy](../../../../../LARGE_FILES.md).
Use commits or tags for future manuscript milestones, not new draft snapshots.

Prepared for Edward Baker, 24 September 2026, with substantial LLM assistance.
Model: GPT-6 (Codex; developer-provided identity). Reasoning effort: not exposed;
not inferred. This opening package is a research plan, not a new certificate.
