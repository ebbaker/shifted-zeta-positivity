# Complete cutoff reflection numerics

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol` (Codex); reasoning effort **ultra**.

No calculations have been run for this initialization. Future computations
should implement the declared bounded task in the
[research program](../notes/INITIAL_RESEARCH_PROGRAM_20261013.md), preserve
complete-source error payments, and distinguish diagnostics from certificates.
Keep reproducible code and small records here. Follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md) for external generated data.

## Completed first calculation

13 October 2026. Prepared for Edward Baker with substantial LLM assistance;
recorded model `gpt-6-astra`, effort **ultra**.

The [reflected-block checker](check_complete_reflected_block.py) and
[retained record](COMPLETE_REFLECTED_BLOCK_RECORD_20261013.json) compare
four small reciprocal centers, both first jets and two quadrature orders.
Replay from the repository root with:

```sh
python3 papers/investigations-2/active/01_complete_cutoff_reflection/numerics/check_complete_reflected_block.py --record /tmp/reflected-block.json
```

This requires NumPy and uses binary64 diagnostics, not outward arithmetic.
The [research note](../notes/COMPLETE_REFLECTED_BLOCK_AND_ENDPOINT_OBSTRUCTION_20261013.md)
separately proves the shared-endpoint obstruction and records all physical
reconstruction payments. No genuine-theta joint-zero certificate is claimed.

## Matched complete-remainder screen, 14 October 2026

Prepared for Edward Baker with substantial LLM assistance; recorded model
`gpt-6-astra` (Codex), reasoning effort **ultra**.

The [checker](check_matched_remainder_01.py),
[record](MATCHED_REMAINDER_01_RECORD_20261014.json), and
[derivation](../notes/2_MATCHED_STATIONARY_REMAINDER_ALLOWANCE_SCREEN_20261014.md)
test the complete retained A+B−C estimate against the shared direct-source
baseline at `t=1/20`, on genuine Hx and Hxx stationary cells near 204.088
and 205.557. All finite-model derivatives, the leading correction, and the
complete disk/Cauchy error ledger are retained. Neither conditional sign
is certified by the four tested radii. For the Hxx stationary target, an
analytic lower bound on the **error allowance** proves that both separate
conditional jet boxes contain zero at every permitted radius `0<r<=1`.
This is not a lower bound on the true approximation error.

No new signed contour remainder was derived. Small signed residuals
reconstructed from the already certified baseline are identified as such;
they do not constitute a cheaper independent remainder calculation.
The checker requires `python-flint 0.9.0`, uses 256-bit outward balls, and
hash-checks the shared baseline record. Replay instructions are in the note.

## Path-only update, 16 October 2026

Prepared for Edward Baker with LLM assistance; Claude Opus 5.5
(`claude-opus-5-5`), Claude Cowork, reasoning effort max.

The quasi-RH exponent-descent folder moved to
`papers/quasi-rh/quasi-rh-exponent-descent/`, so the note paths that
`check_complete_reflected_block.py` and `check_matched_remainder_01.py` read
and hash were updated, and nothing else. The retained records keep the earlier
paths and checker hashes; two of the hashed notes in this investigation also
changed (link repairs only). Fresh replays before and after the change agree
in every numerical field; only source hashes, the recorded input paths and
runtimes differ (see the [relocation
record](../../../../REORGANIZATION_20261016.md)).
