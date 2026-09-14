# Small algebra checks and retained records

These programs support written calculations in [the notes](../notes/README.md).
They use Python's standard library and print JSON to standard output;
they do not write or overwrite a record. Numerical illustrations are
labelled separately from exact rational algebra.

| Program | Preserved record | Scope |
|---|---|---|
| [check_matching.py](check_matching.py) | [matching-checks.json](records/matching-checks.json) | 153 finite checks of gamma refinement, composition, and the rational-feedback identity. |
| [check_gauge_transfer.py](check_gauge_transfer.py) | [gauge-transfer-checks.json](records/gauge-transfer-checks.json) | 326 finite checks for winding, transfer, branch cusps, and coherent contact; includes a labelled floating-point illustration. |
| [check_sphere_schur.py](check_sphere_schur.py) | [sphere-schur-checks.json](records/sphere-schur-checks.json) | 251 finite checks of rank-one norms, Schur product ratios, common-state interference, and repetition coefficients; includes a labelled overlap illustration. |

Run from the investigation directory:

```sh
python3 numerics/check_matching.py
python3 numerics/check_gauge_transfer.py
python3 numerics/check_sphere_schur.py
```

Counts refer to finite test cases, not independent theorems. In the new
check, truncated products retain their end factors and the truncated
state retains the final shifted coefficient. The infinite identities,
their domains, and the source-selection arguments are discussed in the
[sphere/Schur note](../notes/SPHERE_AND_SCHUR_PAIRINGS.md).

The first two programs and their record contents are unchanged by the
reorganization. Keep any future replay output separate from these
preserved records. The checks do not construct a field theory, verify
an infinite-dimensional proof, or certify Weil positivity. No large data
or positivity sweep is part of this investigation; follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
