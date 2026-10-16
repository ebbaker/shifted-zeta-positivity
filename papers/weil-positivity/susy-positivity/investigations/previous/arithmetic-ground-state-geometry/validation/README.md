# Package validation

Package validation checks source hashes, file sizes, local links, current and archived manuscript build records, dated snapshot hashes, and the integrity of small recorded computations. It does not verify analytical proofs. The package manifest records current deliverables; historical source fingerprints in `archive/provenance/` identify the inherited survey without making it a live dependency of a future manuscript.

From this investigation directory run:

```sh
python3 validation/check_package.py --replay
```

The replay runs ten small exact programs without writing output and compares their JSON with the retained records: nine supercharge checks, two fixed-quartic period checks, three shape-period checks, four rank-three Jacobi/residue checks, four boundary reflection/normalization checks, five coherent-delay checks, seven prime-return checks, five collective-feedback checks, ten joint-response/comparison checks, and ten arithmetic-sign/boundary-response checks. These fifty-nine labelled checks use integer or rational arithmetic. The validation program and checkers require only Python 3's standard library. A staged copy may use `--external-root /path/to/the/intended/investigation` to resolve links to the shared background and preceding survey.

The manifest intentionally excludes itself and ignored working-output/cache directories. A changed source requires an explicit manifest refresh after review; silently treating a stale manifest as current is not valid. No third-party paper or large derived dataset is part of this package.

After reviewed changes, [refresh_manifest.py](refresh_manifest.py) explicitly refreshes the current file hashes. Build intermediates under `build/` are excluded. The [manuscript build guide](../BUILD.md) distinguishes PDF rendering review from analytical and algebraic validation.
