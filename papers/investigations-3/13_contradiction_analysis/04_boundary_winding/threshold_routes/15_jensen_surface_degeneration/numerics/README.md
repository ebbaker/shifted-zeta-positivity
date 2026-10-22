# Local Jensen-resolution numerics

21 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6-astra (Codex)**, effort **max**.

The [contract](01_RESOLUTION_COMPARISON_CONTRACT_20261021.md) fixes the
window, resolution and benefit target and records bounded amendments.
[check_local_jensen_resolution.py](check_local_jensen_resolution.py)
uses python-flint 0.9.0 (the recorded FLINT is 3.6.0), with consumer
precisions 192 and 256 and 832 additional central-series working bits.

From this directory, with that dependency installed:

```sh
python3 check_local_jensen_resolution.py --output /tmp/JSD_RESOLUTION_REPLAY.json
```

The script fails on any unresolved required interval comparison. It
checks the complete approximation/tail budgets, root-count margins,
exact quadratic identities and the infinite-product double control.
The small [record](JSD_RESOLUTION_COMPARISON_20261021.json) binds the
script bytes and records both precision runs. Timing and platform fields
are observational and will vary; a byte-identical JSON is not expected.
Mathematical comparisons must pass on the replay's actual balls.

All per-method coefficients and moments are freshly acquired inside its
timer. Common process startup/imports and separate control executions are
excluded. No large coefficient array or surface is materialized. The
[research note](../notes/01_LOCAL_RESOLUTION_AND_COMPLETE_COST_COMPARISON_20261021.md)
gives the proof and interpretation; the [self-review](../reviews/01_LOCAL_RESOLUTION_SELF_REVIEW_20261021.md)
is same-assistant only. No manuscript build or global simplicity claim.
