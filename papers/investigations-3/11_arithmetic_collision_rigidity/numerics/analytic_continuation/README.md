# Replay the final analytic continuation

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. Internal same-model review.

[Note 14](../../notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md)
contains the all-height proofs. These records check their scalar constants
and exact polynomial control; they do not scan heights or close the global
bridge. Requires Python with python-flint 0.9.0.

From the repository root, using the actual model/effort for a future run:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/analytic_continuation/replay_analytic_continuation.py --repo . --output-dir /tmp/inv11-analytic-replay --execution-model gpt-6.1-sol --execution-effort ultra --verify-reference papers/investigations-3/11_arithmetic_collision_rigidity/numerics/analytic_continuation/ANALYTIC_CONTINUATION_REPLAY_20261018.json
```

The wrapper checks pinned reference source identities before replaying,
generates 192-bit outer and constant-distance records, independently
repeats them at 256 bits, checks enclosure intersections and runs the exact
remote polynomial check. It records all process costs, own-source hashes
and five rejected outer-domain parameter cases. Run into a fresh output
directory; do not overwrite the retained reference evidence during a replay.

`OUTER20_EXCLUSION_20261018.json` covers epsilon<=t<=1/2 and
abs(x)>=exp(20/epsilon). `CONSTANT_DISTANCE_TAIL_20261018.json` covers
orders 0–2, all x>=1000, 0<=t<=1/2, |Im z|<=1 for its two frozen rules.
`REMOTE_COLLISION_CONTROL_20261018.json` checks an exact polynomial family
which lacks the theta source and fails the stronger D1 signed premise.
`ANALYTIC_CONTINUATION_REPLAY_20261018.json` binds the source bytes and
bounded replay. The [consumer ledger](GLOBAL_ANALYTIC_CONTINUATION_LEDGER_20261018.json)
supersedes the earlier outer cutoff while preserving its finite inputs.
Hashes identify inputs and outputs; the written arguments establish the
unbounded-range claims. There is no new Newman bound.
