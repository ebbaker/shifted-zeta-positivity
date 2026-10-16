# Critical path: cumulative positivity and adaptive smoothing

This investigation studies continuation of cumulative positivity as support
length grows and arithmetic shift decreases. No all-depth path is established.

The current result is the [all-input arithmetic EMA anchor](notes/EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md):
the fixed relaxation tower, with its local and pole terms intact, gives
Q(0,1/2) >= I/40 and a certified original-transfer defect
D(0.001,1/2) >= 0.000049998 I. A finite tower supplies a lower operator;
endpoint-aware cosine blocks and rational interval bounds cover all omitted
inputs. This closes the preceding pilot's specified gap. It is a proof-method
result inside previously known positive windows, not a new depth horizon.

The [review](reviews/ADAPTIVE_EMA_REVIEW_20260920.md) confirms the preceding
EMA audit's main conclusions and records one minor correction to its resolution
scaling. The [next-session handoff](notes/RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md)
prioritizes normalized cumulative depth coupling for an append from L=1/2 to
L=11/20. A single-window certificate does not settle that coupling or show that
a sequence of depths can become unbounded.

- [Notes](notes/README.md): current proof and continuation, earlier audit and
  proposal evaluation, each retained as dated research.
- [Review](reviews/README.md): scope, correction, and numerical replay.
- [Numerics](numerics/README.md): rational anchor certificate at 40 and 60 digits,
  independent response checks, the earlier pilot, and 57 inherited controls.
- [Current provenance](numerics/records/ema-review-anchor-provenance-20260920.json).
- [Earlier audit provenance](numerics/records/adaptive-ema-audit-provenance-20260920.json)
  and [original research record](RESEARCH_RECORD.json) preserve their historical
  file identities; their index hashes describe their original sessions.
- [Wilson–Loewner manuscript pair](../wilson-loewner/README.md): version 0.4 remains
  the manuscript baseline; these EMA developments have not been integrated.
- [Shift-flow and cumulative-storage proposal](../wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md).

The audit used GPT-6 (Codex), with Extra High effort reported by the user.
The current review and anchor use OpenAI GPT-6 (Codex); the reviewing session's
effort setting is not exposed. Specialist mathematical review is outstanding.
No physical Wilson realization, localization theorem, or arithmetic Loewner
driver is supplied by the arithmetic certificate.
