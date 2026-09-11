# Storage-depth numerical supplement

Code and small records for the [storage-depth paper](../README.md), working
draft v0.3. Read [STATUS.md](../STATUS.md), [CLAIMS.json](../CLAIMS.json) and
the [closeout record](../CLOSEOUT.md) before interpreting a result.

| Location | Purpose |
|---|---|
| `records/` | Small records for spatial construction, continuation, floor bisections, residual tests, comparisons and Rayleigh upper bounds. Both passing and failed tests are retained. |
| `recursion/replay_floor.py` | Hash-verified streaming replay of absolute, relative and comparison tests; optional bisection. Hypothetical complement floors are diagnostics. |
| `recursion/rayleigh_upper.py` | Ball Rayleigh upper bounds for the original first and second steps. |
| `recursion/build_step.py`, `build_from_seed.py` | Original second-step construction and seeded reconstruction. |
| `recursion/build_step_seed.py`, `build_from_seed_v2.py` | Construction from a seed with arbitrary slab dimension, used for the 96-mode R18 build. |
| `recursion/stream_io.py`, `archive.py` | External archive lookup and integrity checks; the streaming loader reduces peak memory. |
| `recursion/certify_step.py`, `weighted_residual.py`, `check_spatial.py` | Original guarded tests, weighted residual experiments and spatial consistency checks. |
| `metric_comparison.py` | Comparison of the retained old metric and the candidate energy. |
| `tools/` | Archive catalogs, exact Galerkin continuation and upper bounds from a supplied build record. |
| `fourier_side/` | Midpoint zero-sum and sensitivity diagnostics, zero caches and small result records; these are not interval certificates. |
| `ARCHIVE_RECORDS.json` | Six recorded matrix archives, with stored-file and canonical matrix-content hashes. |
| `../archive/drafts/v0.1_2026-09-10/numerics/` | Preserved first-step builders, five research packets and original replay code. |

Use Python 3.10 or 3.11 and `requirements.txt`; assertions must stay enabled.
The recorded environment is python-flint 0.9.0 with FLINT 3.6.0, and mpmath
1.3/1.4 (the requirements file pins 1.4.1).

Large data live outside git. For the maintainer's current copy:

```bash
export STORAGE_DEPTH_ARCHIVES=/Users/Shared/szp-archive/storage-depth/numerics-archives
```

Adjust that path for another machine. [ARCHIVES.md](../ARCHIVES.md) records
availability, hashes and regeneration instructions. The paper
[README](../README.md#reproduce) gives the R14–R18 commands, including the
96-mode rebuild. Write regenerated matrices and continuation data to the
external archive, and scratch replay outputs outside the repository.

Repository packaging checks, which do not rerun mathematical certificates:

```bash
# From the repository root
python3 tools/check_repository_hygiene.py
```

[All manuscripts](../../README.md)
