# Newman certificate audit research notes

12 October 2026. Folder prepared for Edward Baker using GPT-6-astra (Codex;
`gpt-6-astra`), reasoning effort **ultra**; notes 1–2 added the same day
with Claude Fable 5.1 (`claude-fable-5-1`) and note 3 with Claude Opus 5.5
(`claude-opus-5-5`, reasoning effort max), with substantial LLM assistance.

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
