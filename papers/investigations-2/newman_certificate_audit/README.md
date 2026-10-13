# Newman certificate audit and corrected-interface benchmark

12 October 2026. Prepared for Edward Baker. Scope: GPT-6-astra (Codex);
reasoning effort: ultra, verified from the session configuration. First
audit session the same day: Claude Fable 5.1 (`claude-fable-5-1`), Cowork.
Second session the same day (review of the first, finite-lane audit):
Claude Opus 5.5 (`claude-opus-5-5`), Cowork, reasoning effort max.
Third session, 12–13 October (steps B1, B2 and B5 of the parallel plan:
tail lemma and uniform error budget; barrier; cross-review of the formal
lane): Claude Opus 5.5 (`claude-opus-5-5`; the serving model may differ),
Cowork, reasoning effort max.
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
has margins `400×` its approximation allowance, the tail `10^{4}×`. Those
two figures measure approximation allowances only. Note 4 §6 and note 5
§10 give the derivative and contraction tolerances: the tail's contraction reserve is
`0.0395`, and the barrier's derivative majorants would have to be `×1.497`
too small. The README's stop condition for a record-bound campaign is met. See the
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
not pursued.

**Third session (12 October): tail lemma and uniform error budget.**
[Note 4](notes/4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md)
audits the two remaining analytic suppliers of hypothesis (ii): the tail
lemma for all `N ≥ 3840000`, and the uniform budget `E_max`. No defect was
found.

- The convolution partition (4.3) is exact.
- The term `OV` is redundant padding: its caps lie inside the routed
  caps. Without it, the contraction is `D' = 0.960478`, so the reserve is
  `0.0395`, not `2.8·10⁻⁴`.
- One all-`N` gate is thin, `1.29·10⁻⁶` on the extended `y`-hull, and it
  fixes the head `M = 153814`. It is not load-bearing: with the `y`- and
  `N`-reductions taken in the other order, the gate is needed only on the
  `y`-box, where it is `2.02`.
- The reduction U1–U5 behind `E_max` is correct and uniform in `N`, `y`
  and `t`. `E_max ≤ 2.33494905212·10⁻⁷`, and `L_690988/E_max ≥ 3.389`.
- Two displayed Polymath bounds, (21) and (24), do not follow from their
  written proofs. Both are true. The tail and `E_max` use neither; the
  finite lane and the barrier use (21) as displayed (note 5 §4.1).
- A standard-library recomputation passes all 54 gates and agrees with
  the package's Arb values, which are always the more conservative.
- Both Arb programs, rebuilt here, reproduce the sealed transcripts byte
  for byte.

Polymath's §8 is now read from the paper's TeX source (`km-git-acc/dbn_upper_bound`),
so the remaining barrier audit (Lemma 8.4 majorants, prism gate,
`t → 0`) does not need the PDF. `B_t ≠ 0` is proved in note 4 §3.8.

**Third session, continued (13 October): the barrier.**
[Note 5](notes/5_BARRIER_CERTIFICATE_AUDIT_20261013.md) audits hypothesis
(iii): no zero of `H_t` in `[X, X+1] × [0.1809, 1]` for `0 ≤ t ≤ t0`. No
defect was found.

- Lemma 8.4 is correct. One intermediate display of its proof does not
  follow by its stated step, but it is true and the lemma follows.
- Polymath's own gate (91) divides the time term by `2n`, which its
  argument does not justify. The package's gate has no such division.
- The derivative-box lemma, the head-plus-integral bound, the prism gate
  with its homotopy, the stored-sum identity, the Taylor-tail bound
  (`1.95·10⁻²² < 10⁻²⁰`), the uniform approximation budget
  (`3.57·10⁻⁴ < 0.00125`) and the extension to `t = 0` all check.
- A standard-library checker passes 44 gates. It recomputes all 883
  prism gates of both sealed transcripts (smallest margin
  `0.5198498946`, at prism 882), and its direct sums of the Lemma 8.4
  majorants at five prisms lie below the transcript's ceilings.
- The four Arb programs reproduce their sealed outputs. An independent
  direct-summation evaluator of `f_t` agrees with the stored-sum values
  at 117 mesh points.
- The derivative majorants could be `×1.497` too small, jointly, before
  prism 882 fails.

With notes 1–5, every analytic link of hypotheses (ii) and (iii) has been
checked. What remains is the imported theorems and libraries, and the
producer's 3,148,981 rows that were not recomputed (step B3). The same
session also wrote the cross-family review of the formal-replay lane's
first milestone, which is filed in that lane's
[reviews](../formal_replay_crosswalk/reviews/CROSS_FAMILY_REVIEW_OF_FIRST_MILESTONE_CLAUDE_20261013.md).

This combines certificate review and interface benchmarking in one investigation. It reuses project 17's approximation work rather than reopening its unsuccessful collision-exclusion program. The ordering of public packages is provisional: inspect current source availability, exact claims, dependencies, and replay requirements before selecting one and pinning its revision.

## Records of the audit sessions

- [Dependency ledger](notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md): pin, seal, row, hypotheses, lanes, contracts, remaining obligations.
- [Replay and benchmark](notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md): stored-row reproduction, sensitivities, budgets, decision.
- [Certified replay and finite-lane reductions](notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md): native binding, window freeze, certified replay of 32 stored rows, Dini gate re-verified with margin, sharp-lane option (second session).
- [Tail lemma and uniform error budget](notes/4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md): partition and `OV`, caps and all-`N`, `y`, `t` and error gates, U1–U5, proof-to-code maps, updated tolerances (third session).
- [Barrier certificate](notes/5_BARRIER_CERTIFICATE_AUDIT_20261013.md): Lemma 8.4 and its extension to the box, head plus integral, prism gate and homotopy, stored sums and Taylor tail, uniform budget and `t → 0`, proof-to-code map, tolerances (third session, continued).
- [Numerics](numerics/README.md):
  - standard-library error-budget replay;
  - numpy row replay (benchmark tool);
  - standard-library certified row replay and Dini gate re-verification;
  - numpy Dini-gate landscape (exploration);
  - standard-library recomputation of the tail lemma and of `E_max`, with
    a byte replay of the package's two Arb verifiers;
  - standard-library recomputation of the barrier's suppliers and of all
    883 prism gates;
  - byte replays of the barrier's four Arb programs, and a
    direct-summation Arb corroboration of the stored-sum values.

  Each has a retained record.
- [Cross-model review of notes 1–2](reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md) (Claude Opus 5.5).
- [Chat histories](chat-histories/README.md):
  - The second session's conversation is chat 1. It was converted from the Cowork session transcript and registered with `record_chat.py --import-json`.
  - The first session's conversation was not captured at the time. It was recovered on 13 October as chat 1 of the [Claude registry](chat-histories/claude-cowork/README.md).
  - The third session's conversation is chat 2 of the Claude registry, captured from its transcript on 13 October.

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
- A review locating any discrepancy precisely, or confirming the tested assertions within their stated scope. *Partially. The first session found no discrepancy in the replayed rows, the error-budget transcription or the barrier transcript. The second session audited the finite lane's native binding, window freeze and Dini `y`-transfer and certified 32 stored rows independently, also without discrepancy. The third session audited the tail lemma, the uniform error budget and then the barrier, again without discrepancy. The producer's amortized rows remain.*
- A decision on full replay, further evaluator work, or closure before any new bound campaign. *Delivered: no further evaluator work for this class; full replay only as audit.*

## Continue and stop tests

Continue if the corrected interface resolves previously undecidable cells, supports a justified parameter improvement, or materially reduces cost. Expand from the sample to a complete audit only after all analytic dependencies and coverage obligations are identified. Stop a record-bound campaign if finite-sum cancellation or the tail dominates and the correction changes neither feasibility nor cost. If the package cannot be replayed from available source, report the exact reproducibility gap; that is not a disproof of its mathematical claim.

*Applied:* finite-sum cancellation dominates; the correction changes neither feasibility nor cost. The record-bound campaign is stopped. The package replays from source at the levels attempted (seal, stored transcripts, independent recomputation of rows and budgets).

## Scope constraints and inherited work

Optimize the actual criterion $t_0+y_0^2/2$, with every hypothesis paid. The improved residual belongs to the corrected center, not the old finite sum. Physical derivatives require the correct normalization and holomorphic surrogate. Adjacent natural cutoffs have a matching theorem; arbitrary frozen cutoffs still require add/remove costs. Existing interfaces state $0<t\le1/2$; $t=0$ and foreign complex domains need explicit justification. A bounded scan never proves the infinite tail.

Start from the [benchmark proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md), [public-certificate audit proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md), [project 17 status](../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/README.md), and [cutoff-matching review](../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/11_THETA_CUTOFF_MATCHING_REVIEW_20261011.md). The approximation theorem remains an imported input.

## Records

Place research in `notes/`, computations and small records in `numerics/`, reviews in `reviews/`, and conversation provenance in `chat-histories/`. Follow the [large-file policy](../../../LARGE_FILES.md). At notable milestones update `DRAFT_HISTORY.md` with concise commit/tag references and links; do not create manuscript snapshot directories.
