# Critical path: cumulative positivity and adaptive smoothing

This investigation studies continuation of cumulative positivity as support
length grows and arithmetic shift decreases. No all-depth path is established.

The completed [adaptive-EMA audit and L=1/2 pilot](notes/ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md)
is the current starting point. It corrects the energy displays and trace scope,
proves a stronger two-sided input-removal lemma, compares complete output norms,
and identifies the omitted-input estimate that prevents certification at small
shifts. One exact rational all-input bound applies only to a deliberately
over-smoothed operator. No admissible all-depth route is certified. See its
[provenance record](numerics/records/adaptive-ema-audit-provenance-20260920.json).
The audit used GPT-6 (Codex), with Extra High effort reported by the user.

The earlier [EMA smoothing, positivity, and continuation](notes/EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md) is
the 20 September 2026 evaluation of Edward Baker's adaptive-EMA proposal and
the next-session handoff. It distinguishes the inherited arithmetic EMA from
additional boundary and shift-path smoothers, derives their energy and limiting
identities, gives a counterexample to uncontrolled smoothing removal, and
specifies a controlled pilot. The gamma sector also has an exact multiscale
EMA representation. No arithmetic contraction bound was claimed in that handoff.

- [Continuation note](notes/EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md).
- [Numerics](numerics/README.md): the full-output pilot, the scoped rational
  certificate, and the original 57 finite controls.
- [Research record](RESEARCH_RECORD.json): file identities and source provenance.
- [Wilson–Loewner manuscript pair](../wilson-loewner/README.md): version 0.4 remains
  the manuscript baseline; these new results have not been integrated into it.
- [Earlier shift-flow and cumulative-storage proposal](../wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md).

The earlier handoff was prepared with OpenAI GPT-6 (Codex), with effort then
unexposed. The new audit records the subsequently supplied Extra High setting.
Neither research note has received independent mathematical review. The earlier
RESEARCH_RECORD.json preserves that session's file identities; its index hashes
refer to the earlier index state.
