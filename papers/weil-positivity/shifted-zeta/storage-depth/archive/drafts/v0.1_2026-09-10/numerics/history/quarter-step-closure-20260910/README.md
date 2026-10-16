# Closing the quarter-step complement

Start with the [closure analysis](closure_analysis.md). The full old-input residual factor 0.9 and the spatial full-operator floor 1e-33 both pass. The [analytic reduction](spatial_complement_lemma.md) explains the joint old/new complement bound and the direct residual test. The normalization remains the working Weil-depth v0.3 convention; normalization verification is separate.

This packet reuses the preceding research directories by relative imports. Use Python 3.10 and the versions in [requirements.txt](requirements.txt), with assertions enabled.

```sh
python arithmetic_bound.py --cells 512 --output arithmetic_512.json
python verify_arithmetic_partition.py
python cross_checks.py
python close_complement.py --old 256 --output closure_256_32.json
python relative_closure.py --archive closure_256_32.matrices.json.gz --output relative_256_32.json
python path_corollary.py
```

The spatial construction writes a compressed archive of the complete head matrix and separate old/new full-output Grams. The residual test reads this archive and verifies its recorded source hashes. It does not read or assume the full-operator sign result in `closure_256_32.json`.

Old-depth matrix construction is cached in `old_N_degree_bits.json.gz`. This cache concerns the old interval only; the new-depth global certificate from the previous packet is not used. The full 256-plus-32 construction took about 21 minutes in the recorded environment. The relative test reuses the approximately 153 MiB spatial archive.

`closure_128_32.json` records the initial unsuccessful finite-head/complement test. Its negative test pivot means that this sufficient criterion did not certify the operator; it is not a counterexample to positivity. Its original source is retained as `close_complement_initial.py`, with the source-snapshot mapping recorded in the JSON. That initial version did not save the full spatial matrix archive.

The numerical quadrature comparisons in `cross_checks.json` are independent checks of formulas, not sign certificates. `arithmetic_partition_check.json` independently verifies the continuum arithmetic norm bound using every interval on which the shifted weight is constant.

No file in `sources/` and no repository manuscript was changed.
