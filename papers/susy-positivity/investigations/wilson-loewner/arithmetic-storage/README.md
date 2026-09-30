# Arithmetic storage: cumulative positivity and the first prime

**Direct positive approximation, 29 September 2026.** The [updated overview](PROJECT_SUMMARY.md) and [active research plan](notes/SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md) now prioritize independently positive forms and identification of their arithmetic limit. Odd-source domination is an optional diagnostic, not a prerequisite. The first analysis constructs a controlled regularized baseline, proves collapse of the phase-family projection at the critical endpoint, and explains why a nonzero trace limit needs spectral concentration and growing resolution. The arithmetic limit remains open. See the [internal review](reviews/SONIN_DIRECT_LIMIT_REVIEW_20260929.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; exact serving variant and configured reasoning effort not exposed.

**First compressed moment, 29 September 2026.** The [new calculation](notes/SONIN_COMPACT_FIRST_MOMENT_20260929.md) retains the actual Sonin projection and narrows the first-prime trace intervals by about 66% and 63% for the prescribed even and odd sources. Both complete residual signs remain unresolved. The mass-and-mean bounds are sharp for the available spectral information, so the next calculation needs additional compressed information. The [finite Mellin-defect note](notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md) identifies the constrained sign and cross-term estimates a structural theorem would require. See the [updated project summary](PROJECT_SUMMARY.md) and [internal review](reviews/SONIN_FIRST_MOMENT_REVIEW_20260929.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; exact serving variant and configured reasoning effort not exposed.

**Current project summary, 29 September 2026.** Start with [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md), which consolidates the finite-join results, actual Sonin tools, new scalar calculation, and remaining signed arithmetic gap. The [scalar calculation](notes/SONIN_SCALAR_TRACE_CALCULATION_20260929.md) encloses all four prescribed real-place traces to width below `10^-5`; the old two-vector space captures below 1.090% and 2.422% of the first-prime positive trace. The first-prime inverse-metric trace remains only broadly bounded, and no arithmetic residual sign is claimed. See the [review](reviews/SONIN_SCALAR_TRACE_REVIEW_20260929.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; serving variant and reasoning effort not exposed.

**Actual Sonin enclosure test, later 29 September 2026.** The [new analysis](notes/SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md) implements certified actual-Sonin trial matrices and complete projection-tail bounds for the two prescribed smooth sources. An omitted-direction witness proves that the chosen two-vector trace approximation misses more than 0.00373 and 0.00712, so that specific small-error target is rejected. The prolate resolvent and source certificates remain useful; no arithmetic residual sign is claimed. See the [review](reviews/SONIN_ACTUAL_ENCLOSURE_REVIEW_20260929.md) and [current handoff](notes/SONIN_CONTINUATION_AFTER_ENCLOSURE_TEST_20260929.md), which next targets the scalar smoothed trace. Prepared for Edward Baker with GPT-6 (Codex) assistance; serving variant and reasoning effort not exposed.

**Sonin continuation, 29 September 2026.** The [canonical comparison audit](notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md) verifies the normalization, pole-neutral source criterion, actual projection, and trace-class justification. The [new analysis](notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md) derives an exact signed place-addition law, a faster Chebyshev return expansion, and a one-sided actual-trace approximation bound. No actual Sonin residual has yet been numerically enclosed, and no residual sign theorem is claimed. See the [critical review](reviews/SONIN_TRACE_AUDIT_REVIEW_20260929.md) and [current continuation](notes/SONIN_CONTINUATION_AFTER_TRACE_AUDIT_20260929.md). CCM remains temporarily closed; the completed finite Weil certificates are preserved. Prepared for Edward Baker with GPT-6 (Codex) assistance; exact serving variant and reasoning effort not exposed.

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
