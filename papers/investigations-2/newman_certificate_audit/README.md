# Newman certificate audit and corrected-interface benchmark

12 October 2026. Prepared for Edward Baker. Scope: GPT-6-astra (Codex);
reasoning effort: ultra, verified from the session configuration. First
audit session the same day: Claude Fable 5.1 (`claude-fable-5-1`), Cowork.
Second session the same day (review of the first, finite-lane audit):
Claude Opus 5.5 (`claude-opus-5-5`), Cowork, reasoning effort max.
Prepared with substantial LLM assistance. Internal checks are not
independent mathematical validation.

[Investigation portfolio](../README.md)

## Objective and status

Independently replay a public de Bruijn–Newman upper-bound certificate, then measure whether the repository's corrected heat approximation improves its margins, admissible parameters, or certification cost. A reproducible audit or a useful evaluator improvement is a successful outcome even without a new bound. No public claim is validated by creating this project.

**Status: first bounded task completed on 12 October 2026, with a
negative benchmark result.** The Gomila package
(`judegomila/dbn-lambda-01787854-candidate-audit`, commit `a74738de…`,
claim `Λ ≤ 0.1787854`, self-labelled not peer reviewed) was pinned, its
443-file seal verified, its four hypothesis lanes mapped with their error
budgets and margins, and its weakest finite rows reproduced by an
independent floating implementation to the stored digits. At the only
cells where the approximation error matters (the first finite windows,
`T_N ≈ 7.9·10^{−7}` against `E_max = 2.33·10^{−7}`), the corrected
interface's smaller budget (`e_C/e_{C,0} = 3.7·10^{−6}`) cannot be used at
all, because the lane is uniform in `x`; and even if it could, the row's
measured sensitivities bound the gain by `ΔΛ ≈ 1.2·10^{−8}`. The barrier
has margins `400×` its approximation allowance, the tail `10^{4}×`. The
README's stop condition for a record-bound campaign is met. See the
[benchmark note](notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md)
and the [dependency ledger](notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md).

A side observation (not pursued): the package's own producer has an unused
"sharp" weight, the Polymath §8.5 improved triangle inequality, which at
the certified row gives a lower bound `0.077` instead of `7.9·10^{−7}` and
would move the lane's boundary by about `0.004–0.006` in `Λ` at the same
verification height, subject to re-proving the package's `y`-transfer for
that weight. The lever in this certificate class is the finite-lane
lower-bound lemma, not the Riemann–Siegel error term.

**Second session (12 October): review and finite-lane audit.** A
cross-model [review](reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md)
confirmed notes 1–2; it found no error that changes a conclusion and
recorded refinements. [Note 3](notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md)
then audited every link of the finite lane except the uniform error
budget:

- the native binding and window freeze, checked by hand;
- an independent standard-library certificate of 32 stored rows, which
  gives `L_690988 ∈ [7.9136674559412, 7.9136674559419]·10^{−7}`, reproduces
  all twelve singleton-time first-of-run floors to 12 decimals, and leaves
  `L_690988 − E_max ≥ 5.58·10^{−7}`;
- an independent re-verification of the Dini `y`-transfer gate with
  supremum `≤ 3/4`. The package's reported worst ratio `0.99999860767` is
  an artifact of its bisection stopping rule, not a `10^{−6}` margin.

No defect was found. The review also shows that the improved
inequality's bound is monotone in the `γ`-bound. At the same `X` and
`y0`, a sharp-weight lane at `t0 ≈ 0.157` (`Λ ≈ 0.1745`) would therefore
reuse hypotheses (i) and (iii) unchanged. It is recorded as an option,
not pursued. The largest unaudited piece is now the barrier's Lemma 8.4
derivative majorants, which require the Polymath PDF in the session.

This combines certificate review and interface benchmarking in one investigation. It reuses project 17's approximation work rather than reopening its unsuccessful collision-exclusion program. The ordering of public packages is provisional: inspect current source availability, exact claims, dependencies, and replay requirements before selecting one and pinning its revision.

## Records of the audit sessions

- [Dependency ledger](notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md): pin, seal, row, hypotheses, lanes, contracts, remaining obligations.
- [Replay and benchmark](notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md): stored-row reproduction, sensitivities, budgets, decision.
- [Certified replay and finite-lane reductions](notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md): native binding, window freeze, certified replay of 32 stored rows, Dini gate re-verified with margin, sharp-lane option (second session).
- [Numerics](numerics/README.md):
  - standard-library error-budget replay;
  - numpy row replay (benchmark tool);
  - standard-library certified row replay and Dini gate re-verification;
  - numpy Dini-gate landscape (exploration).

  Each has a retained record.
- [Cross-model review of notes 1–2](reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md) (Claude Opus 5.5).
- [Chat histories](chat-histories/README.md):
  - The second session's conversation is chat 1. It was converted from the Cowork session transcript and registered with `record_chat.py --import-json`.
  - The first session's conversation was not captured.

## First bounded task

Select 20–50 difficult cells from one pinned barrier or final-time certificate. Reproduce their original certificates before changing the evaluator. On the same cells and precision, compare the original approximation, the pointwise corrected expression, and the holomorphic corrected interface where a common analytic disk is required.

For each cell record the finite-sum margin, displacement caused by the correction, source remainder, interval overestimation, derivative allowance, cutoff payment, runtime, precision, and exact domain. State separately what the sample establishes and which obligations remain for the entire certificate.

*Outcome (12 October):* the pinned certificate has no cells on which the
three evaluators could differ materially. Its barrier cells are evaluated
pointwise but have margins `0.52–1.89` against an allowance `0.00125`; its
final-time cells are not pointwise at all. Ten representative finite rows
(the five weakest and the first row of each prime leg and the last row)
and the barrier transcript were replayed instead, and the comparison was
carried out analytically at the weakest row. The per-cell ledger asked for
above therefore collapses to the two tables in the notes.

## Deliverables

- A dependency and domain ledger for the selected bound, including the verified initial region, intermediate-time barrier, final-time nonvanishing, and unbounded analytic tail. *Delivered (note 1).*
- A reproducible cell selection and replay procedure, small retained records, and a comparison table with complete error accounting. *Delivered (note 2, numerics).*
- A review locating any discrepancy precisely, or confirming the tested assertions within their stated scope. *Partially. The first session found no discrepancy in the replayed rows, the error-budget transcription or the barrier transcript. The second session audited the finite lane's native binding, window freeze and Dini `y`-transfer and certified 32 stored rows independently, also without discrepancy. The barrier majorants, the tail gates and the uniform error budget remain.*
- A decision on full replay, further evaluator work, or closure before any new bound campaign. *Delivered: no further evaluator work for this class; full replay only as audit.*

## Continue and stop tests

Continue if the corrected interface resolves previously undecidable cells, supports a justified parameter improvement, or materially reduces cost. Expand from the sample to a complete audit only after all analytic dependencies and coverage obligations are identified. Stop a record-bound campaign if finite-sum cancellation or the tail dominates and the correction changes neither feasibility nor cost. If the package cannot be replayed from available source, report the exact reproducibility gap; that is not a disproof of its mathematical claim.

*Applied:* finite-sum cancellation dominates; the correction changes neither feasibility nor cost. The record-bound campaign is stopped. The package replays from source at the levels attempted (seal, stored transcripts, independent recomputation of rows and budgets).

## Scope constraints and inherited work

Optimize the actual criterion $t_0+y_0^2/2$, with every hypothesis paid. The improved residual belongs to the corrected center, not the old finite sum. Physical derivatives require the correct normalization and holomorphic surrogate. Adjacent natural cutoffs have a matching theorem; arbitrary frozen cutoffs still require add/remove costs. Existing interfaces state $0<t\le1/2$; $t=0$ and foreign complex domains need explicit justification. A bounded scan never proves the infinite tail.

Start from the [benchmark proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md), [public-certificate audit proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md), [project 17 status](../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/README.md), and [cutoff-matching review](../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/11_THETA_CUTOFF_MATCHING_REVIEW_20261011.md). The approximation theorem remains an imported input.

## Records

Place research in `notes/`, computations and small records in `numerics/`, reviews in `reviews/`, and conversation provenance in `chat-histories/`. Follow the [large-file policy](../../../LARGE_FILES.md). At notable milestones update `DRAFT_HISTORY.md` with concise commit/tag references and links; do not create manuscript snapshot directories.
