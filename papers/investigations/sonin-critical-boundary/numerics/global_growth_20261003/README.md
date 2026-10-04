# Fixed-probe zero-tail and continuous-range certificate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
were not exposed and are not inferred. Internal checks are not independent
specialist refereeing.

This small package certifies the constants in the [zero-tail proof](../../notes/GLOBAL_GROWTH_ZERO_TAIL_20261003.md):

- `delta_T < 1.058e-116` at the published verified height `T=3e12`;
- `delta_T(1+exp(250)) < 3.961e-8`;
- `b(2) < 0.01237498726501953`;
- `q + delta_T(1+exp(250)) + b(2) < 1.47931505787654 < 1.48`.

The analytic argument extends this last comparison to **every real separation
2 <= r <= 500**. The global subexponential estimate remains open, and this
absolute bound does not imply the sharper pairwise threshold `|C_g|<=q`.

The generator reconstructs the exact prepared polynomial, normalization,
interior sixth-derivative squared norm, and endpoint atoms using rational
arithmetic. It bounds the total variation of the sixth distributional
derivative and uses Arb outward arithmetic for the logarithm and exponentials.
The diagonal is imported only after checking the SHA-256 of
`../all_window_mechanism_20261003/probe_256.json`.

The external mathematical inputs are the complete explicit formula, the
zero-count bound, and [Platt--Trudgian's published finite-height verification](https://doi.org/10.1112/blms.12460).
Those inputs are not independently reverified by this script. No individual
zero ordinates or prime sums near the final separation are enumerated.

Run from this directory with Python and `python-flint` available:

```bash
python3 certify_zero_tail.py --bits 192 --diagonal ../all_window_mechanism_20261003/probe_256.json --output zero_tail_192.json
python3 certify_zero_tail.py --bits 256 --diagonal ../all_window_mechanism_20261003/probe_256.json --output zero_tail_256.json
python3 replay_zero_tail.py --diagonal ../all_window_mechanism_20261003/probe_256.json --output zero_tail_replay.json
```

The stored runs used Python 3.10.0, python-flint 0.9.0, and FLINT 3.6.0.
The replay checks source hashes, precision-independent inputs, exact rational
upper endpoints, and overlap between the two precision enclosures. It is a
record audit, not a separate reconstruction of the analytic proof. Runtime
metadata may vary when regenerating a record, so its file hash may change.

The [preflight](../../notes/GLOBAL_GROWTH_ZERO_TAIL_PREFLIGHT_20261003.md)
limited the work to these two scalar runs. All saved records are small;
there are no large derived data, downloaded papers, or zero caches.
