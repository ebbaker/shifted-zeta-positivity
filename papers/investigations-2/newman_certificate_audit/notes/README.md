# Newman certificate audit research notes

12 October 2026. Folder prepared for Edward Baker using GPT-6-astra (Codex;
`gpt-6-astra`), reasoning effort **ultra**; notes 1–2 added the same day
with Claude Fable 5.1 (`claude-fable-5-1`) and notes 3–5 with Claude Opus 5.5
(`claude-opus-5-5`, reasoning effort max; note 5 on 13 October), with
substantial LLM assistance.

Save dated incremental arguments here. Identify hypotheses, proved steps,
source dependencies, the remaining estimate, and a concrete next decision.
Each note must record its own model and reasoning effort. Follow the
[project scope](../README.md) and [portfolio conventions](../../README.md).

## Notes

1. [Pinned public certificate and dependency ledger](1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md):
   pins the Gomila package at commit `a74738de…`, verifies its 443-file
   seal, states the exact row and Polymath Theorem 1.2 hypotheses, and
   tabulates for each lane the domain, the lower-bound mechanism, the
   approximation error paid and the certified margin. Identifies the first
   finite rows as the only cells where the error is a material fraction of
   the margin, and explains why the uniform finite lane cannot consume the
   corrected interface at all.
2. [Finite-lane replay and corrected-budget benchmark](2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md):
   reproduces the stored floors at the first row of every producer run,
   measures `∂L/∂(y^2) = 9.53` and `∂L/∂t = 19.06` at the weakest row,
   recomputes the `C`-dropped and `C`-retained budgets, and bounds the
   conceivable gain from the corrected interface by `ΔΛ ≈ 1.2·10^{−8}`.
   Records, separately from the benchmark, that the package's own
   unused "sharp" (Polymath §8.5 improved-triangle) weight would move the
   lane's boundary by `ΔΛ ≈ 0.004–0.006`. Decision: stop the
   corrected-interface campaign for this certificate class; remaining
   obligations are audit-only.
3. [Certified row replay and finite-lane reductions](3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md):
   - checks the native binding and the window freeze by hand;
   - certifies 32 stored rows independently with standard-library
     interval arithmetic, including the weakest row,
     `L_690988 ≥ 7.9136674559412·10^{−7}`; all twelve singleton-time
     first-of-run floors reproduce to 12 decimals;
   - re-verifies the Dini `y`-transfer gate with certified supremum
     `≤ 3/4` (`[0.7107, 3/4]` in the largest leg), and shows that the
     package's `0.99999860767` is a stopping-rule artifact;
   - records the sharp-weight option at `t0 ≈ 0.157`, for which
     hypotheses (i) and (iii) are reusable.

   Remaining: the barrier majorants, the tail gates and the uniform
   error budget.
4. [Tail lemma and uniform error budget](4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md):
   - checks the exact convolution partition (4.3), and shows that `OV` is
     redundant padding. The tail's real contraction is
     `D' = 0.960478`, with reserve `0.0395`.
   - checks the endpoint caps, the all-`N`, `y` and `t` reductions, and
     the error terms with the `10.50` weld.
   - records one thin gate, `1.29·10⁻⁶`, which fixes the head
     `M = 153814` and is avoidable by reversing two reductions.
   - checks U1–U5 of the uniform budget,
     `E_max ≤ 2.33494905212·10⁻⁷`, and gives proof-to-code maps for both
     Arb programs.
   - records two Polymath displays that do not follow from their written
     proofs, both true and unused by the tail and `E_max` (note 5 §4.1
     corrects a broader remark); proves `B_t ≠ 0`; and updates the
     tolerance table.

   Remaining: the barrier (Lemma 8.4 majorants, prism gate, `t → 0`)
   and the producer's amortized rows.
5. [Barrier certificate](5_BARRIER_CERTIFICATE_AUDIT_20261013.md):
   - checks Lemma 8.4, one intermediate display of whose proof does not
     follow by its stated step, and its extension to the box and to
     `t = 0`;
   - records that Polymath's gate (91) divides the time term by `2n`,
     which the package does not inherit;
   - checks the head-plus-integral bound (one thin but structural gate,
     margin `2.24·10⁻⁷`, equivalent to `N² < X/4π`), the prism gate and
     its homotopy, the stored-sum identity, the Taylor tail, the uniform
     budget and `t → 0`;
   - recomputes all 883 prism gates of both transcripts and the direct
     majorant sums at five prisms, replays the four Arb programs, and
     corroborates the stored-sum values by direct summation;
   - corrects note 4: the finite lane and the barrier use (21) as
     displayed, which is true.

   Remaining: the producer's amortized rows (B3), then consolidation
   (B4).
