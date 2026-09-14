# Reproduction scripts — rh-detector

Regenerated from the round notes on 25 August 2026 after the original session workspace
was lost (see `../STATUS.md`, Provenance); all outputs were re-verified against the
recorded Round 3/4 values on that date, and the quick scripts were smoke-tested again
under the pinned environment on 9 September 2026.

| Script | Backs | Runtime |
|---|---|---|
| `h1_zeros1000.py` | regenerates `zeros1001.json` (first 1001 zeta ordinates, 25 digits) | ~4 min |
| `h3_certified.py` | Table 1 (certified null test, K = 1000, exact S(U), Trudgian band) and the §4.2 thresholds; **needs `zeros1001.json`** (shipped, or rebuild with h1) | ~3 min |
| `d1_synthetic.py` | Table 2 (injection tests; computes its own 80 ordinates) | ~1 min |
| `v1_pencil.py` | §5.1: pencil identity n = 2…7, rank-one relation, Λ(z²+y₀²), unit-variance Hermite benchmark, five k = 2 thresholds vs direct root tracking | seconds |
| `d4_margin_meter.py` | Table 3 (local Λ margins; computes its own 80 ordinates) | ~1 min |
| `h4_beta.py` | §6 (Dirichlet beta null test; uses `beta_zeros.json` if present, else regenerates by sign scanning) | ~1 min cached |

Each script prints to stdout; the expected outputs are the numbers quoted in the paper's
tables. Run from this directory (the JSON caches are resolved relative to the working
directory). Dependencies: `requirements.txt`. The high-precision parts use mpmath at
25–30 significant digits; the injection fits and pencil eigenvalue computations run in
double precision — this is the floating-point caveat recorded in `../STATUS.md`.

[Miscellaneous papers](../../README.md) · [All manuscripts](../../../README.md)
