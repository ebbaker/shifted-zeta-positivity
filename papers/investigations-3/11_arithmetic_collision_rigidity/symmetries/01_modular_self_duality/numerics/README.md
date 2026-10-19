# Reproduce the S01 paired-endpoint comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol, actual reasoning effort ultra**. Internal
same-model verification; no independent specialist review.

The [derivation](../notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md)
proves the paired-endpoint bound. `check_paired_modular_tail.py` checks its
uniform constants and infinite tail using outward Arb/Acb arithmetic,
then freshly constructs the existing complete height-1000 evaluator.
The two methods share the exact polynomial, quadrature radii, source
cutoff, derivative conventions and propagation payments. Only the
omitted arithmetic-tail payment changes.

Requires Python with python-flint 0.9.0. From the repository root, write
future output to a fresh external location and record actual model/effort:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/numerics/check_paired_modular_tail.py --repo . --output /tmp/S01_PAIRED_TAIL.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/numerics/check_paired_modular_tail.py --repo . --output /tmp/S01_PAIRED_TAIL_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/S01_CONTROL_RECEIPTS --output /tmp/S01_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The primary record `PAIRED_MODULAR_TAIL_20261018.json` contains the 192-bit
complete comparison and the 192/256-bit tail expressions. The separate
`PAIRED_MODULAR_TAIL_REPLAY_256_20261018.json` freshly repeats the complete
comparison at 256 bits and checks tail expressions at 256/320 bits.
All arithmetic modes beyond the twelve finite tail terms use a proved
geometric bound. No numerical infinite-series cutoff is assumed exact.

`S01_MODULAR_CONTROLS_20261018.json` replays the existing five source-specific
event boxes and a separate Euler negative-Laguerre witness. It verifies
the downstream acceptance interface; it does not validate the analytic
tail theorem. The checker separately rejects five inadmissible parameter
sets and verifies a non-even analytic source's compulsory vertical segment
through two spectral derivatives at a complex spectral point.

All component errors use fixed `G0(1000)` normalization. The retained
physical derivatives hold the contour, integer mode cutoff, source cutoff
and normalizer fixed. A smaller error is not a lower bound for the signed
field; no new collision-free region, global exterior or Newman bound is
claimed. Records remain small; regenerated receipts and additional replay
outputs belong outside Git under the repository large-files policy.
