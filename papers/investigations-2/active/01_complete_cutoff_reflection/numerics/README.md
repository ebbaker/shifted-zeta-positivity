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
