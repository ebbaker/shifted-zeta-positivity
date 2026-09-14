# Cumulative-storage continuation

Start with [the research note](cumulative_storage_path.md). It derives an exact Cayley representation of cumulative storage, proves preservation of spatial relative coupling, and gives a signed Schur inequality for combined depth and shift continuation.

The new numerical result is restricted to one exact degree-126 polynomial: at depth log 7 and shift 1e-11, its full-output contraction defect is positive, although the earlier instantaneous-generator calculation was negative. This packet does not certify an enlarged horizon or a full relative-coupling upper bound.

| File | Purpose |
|---|---|
| `cumulative_storage_path.md` | Deductions, proofs, limits, next depth target |
| `certify_vector_storage.py` | Arb enclosure of one full-output storage quotient, with analytic profile error |
| `storage_log7_1em11.json` | Degree 220, 6144-bit result |
| `storage_log7_1em11_replay.json` | Degree 240, 7168-bit replay |
| `storage_log7_1em13.json` | Smaller-shift comparison on the same input |
| `cross_checks.py`, `cross_checks.json` | Independent beta-integral and quadrature checks; noncommuting block algebra checks |

The input coefficients are read from `../critical-path-20260910/generator_witness_log7.json`, and that record's hash is stored with each new result. The new script is self-contained apart from that vector and python-flint. The quadrature checks additionally use mpmath.

Reproduction, with the packages in `requirements.txt` installed:

```sh
python certify_vector_storage.py --output storage_log7_1em11.json
python certify_vector_storage.py --degree 240 --bits 7168 --output storage_log7_1em11_replay.json
python certify_vector_storage.py --shift 1e-13 --degree 240 --bits 7168 --output storage_log7_1em13.json
python cross_checks.py
```

The working normalization is the Weil-depth v0.3 source at commit `a566944dc1be2899e37fce3d0e857516ced33d8f`. The analytic deductions and error proof await independent review. Synced sources and the repository manuscript were not edited.
