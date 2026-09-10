# The log 7 to log 8 extension

Read [the analysis](extension_analysis.md) for definitions, proofs, limits, and the continuation-residual target.

Results in the working v0.3 normalization:

- Full-operator new-slab bound: for length log(8/7), the gamma transfer has norm at most exp(-0.06 omega) for every 0 < omega <= 1/2. This also applies to every shorter slab.
- Full central coupling lower bound: its square exceeds 1 - 1.84e-17. This limits the available slack; it does not prove full positivity.
- Finite-input cumulative positivity: all inputs in the 128-old-mode plus 32-new-mode space pass at shift 1e-11, with full output and an analytic remainder bound. This space contains the earlier negative-generator witness.
- Shorter first steps have larger proved finite central slack: at least 1e-7 for a quarter-step, 1e-11 for a half-step, and 1e-17 for the full step, on the same 128+32 input dimensions.
- The omitted old and new input spaces are not controlled. There is no unrestricted log 8 extension certificate here.

| Files | Role |
|---|---|
| `extension_storage.py`, `extension_*.json` | Piecewise polynomial input, full-output cumulative storage and finite-input positivity certificates |
| `central_geometry.py`, `central_*.json` | Central cross form, component cancellation, finite-input positivity, full-coupling lower witnesses |
| `new_slab_bound.py`, `new_slab_bound.json` | Uniform full-operator bound on the new gamma slab |
| `step_size_diagnostics.py`, `step_size_diagnostics.json` | Central diagnostics and proved finite-input relative slack for shorter first steps |
| `cross_checks.py`, `cross_checks.json` | Independent kernel integration and full-output quadrature checks |

The scripts import the two preceding research packets by relative paths. Their numerical dependencies are python-flint 0.9.0 and mpmath 1.4.1. The reference manuscript and its source routine remain unchanged.

From this directory, the main runs are:

```sh
python new_slab_bound.py
python central_geometry.py --old 128 --new 32 --degree 320 --bits 4096 --output central_128_32.json
python central_geometry.py --old 128 --new 32 --degree 340 --bits 4608 --output central_128_32_replay.json
python extension_storage.py --old 128 --new 32 --shift 1e-11 --degree 280 --bits 6144 --output extension_128_32_1em11.json
python step_size_diagnostics.py
python cross_checks.py
```

The largest full-output run took about ten minutes in this environment. Analytic deductions and the error proofs still require independent review; no result here audits the normalization.
