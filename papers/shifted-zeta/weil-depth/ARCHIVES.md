# Ball-matrix archives — tracked guide to the unversioned data

The large derived data of this paper are kept outside git: the saved Arb ball matrices behind
each certificate (about 13 MB per horizon), the independent implementation's saved matrices
for the two leading horizons, and the original v0.1 review package (whose only large content
is the 9/5 matrices). This file is the tracked description of that folder. The folder itself
may live anywhere — the current local copy is
`/Users/Shared/szp-archive/weil-depth/numerics-archives/`, with a copy of this guide as
its `README.md` — and `papers/shifted-zeta/weil-depth/.gitignore` excludes `numerics-archives/` and every
`*.json.gz` under `numerics/output/` so that a copy placed inside the repository is not
committed by accident. The repository-wide convention and the step-by-step procedure for
adding or moving such files are in `LARGE_FILES.md` at the repository root; this file is the
per-paper instance of that convention.

The repository is complete and verifiable without the folder. Every certificate records the
SHA-256 of the archive it was computed from (`matrix_archive_sha256`) and a content hash of
the matrices themselves (`matrices_content_sha256`, canonical JSON of the four ball matrices
and the run parameters, independent of timestamps and runtime metadata), and every archive is
deterministic output of `numerics/certify_arb.py` or `numerics/independent_arb.py` for the
parameters recorded in the certificate — about one minute per horizon at `N = 128`.

The continuation paper is [storage-depth](https://github.com/ebbaker/shifted-zeta-positivity/tree/main/papers/shifted-zeta/storage-depth);
its data use the separate `szp-archive/storage-depth/numerics-archives/` folder
and `STORAGE_DEPTH_ARCHIVES` variable.

## Expected layout

The folder mirrors `numerics/`. When a file is missing from `numerics/output/`, the scripts
look for the same relative path under the directory named by the environment variable
`WEIL_ARCHIVES` (`certify_arb.locate`).

```
WEIL_ARCHIVES/
├── SHA256SUMS.txt
├── output/
│   ├── log2_N128/central_matrices.json.gz
│   ├── log3_N128/central_matrices.json.gz
│   ├── log4_N128/central_matrices.json.gz
│   ├── log5_N128/central_matrices.json.gz
│   ├── log6_N128/central_matrices.json.gz
│   ├── length_1p8_N128/central_matrices.json.gz
│   ├── log7_N128/central_matrices.json.gz
│   ├── independent_1p8/independent_matrices.json.gz
│   └── independent_log7/independent_matrices.json.gz
└── drafts/v0.1_2026-09-09/FINITE_HORIZON_WEIL_REVIEW_PACKAGE_20260909.zip
```

| File (relative to `WEIL_ARCHIVES`) | Belongs at | Size | SHA-256 |
|---|---|---:|---|
| `output/log2_N128/central_matrices.json.gz` | `numerics/output/log2_N128/` | 13 MB | `f07817c12004adde9ff21e1775982ea09561c948a64577331f40a2a0e8d560de` |
| `output/log3_N128/central_matrices.json.gz` | `numerics/output/log3_N128/` | 13 MB | `00bb842f7a8c357b754b7ff00f5953f2b4c6ab8f91d0da4fcfa2296bb76eb799` |
| `output/log4_N128/central_matrices.json.gz` | `numerics/output/log4_N128/` | 13 MB | `b3452b4529a1bdb38514b04c8313657fed43a4e1c80f528825f7bc3a075cbcc5` |
| `output/log5_N128/central_matrices.json.gz` | `numerics/output/log5_N128/` | 13 MB | `9b9285bdedd4a164a496ecdd030a13599b7cc121904247beab60e53836312456` |
| `output/log6_N128/central_matrices.json.gz` | `numerics/output/log6_N128/` | 13 MB | `1afc68d147396e9a2220abe3f0950179cc337c80dc6ce0e00e6d43117218308b` |
| `output/length_1p8_N128/central_matrices.json.gz` | `numerics/output/length_1p8_N128/` | 11 MB | `cf5cdf2f17a5a69fc6c9c1f4ec734c8cb18ceda842cd53925fa0a67b5c1ded14` |
| `output/log7_N128/central_matrices.json.gz` | `numerics/output/log7_N128/` | 13 MB | `2460486c3de953009b85a40601a4968043ad265d1394998068364aaa8294d6a5` |
| `output/independent_1p8/independent_matrices.json.gz` | `numerics/output/independent_1p8/` | 12 MB | `c0fe16b099d0fd1e1917aca558202f952983deea57324f64896f9002cd106d00` |
| `output/independent_log7/independent_matrices.json.gz` | `numerics/output/independent_log7/` | 14 MB | `55e6bc41b74f1e12a67f36dea2958103a6d3c397bdfc37eff975eafd3075c62a` |
| `drafts/v0.1_2026-09-09/FINITE_HORIZON_WEIL_REVIEW_PACKAGE_20260909.zip` | `archive/drafts/v0.1_2026-09-09/` (small contents extracted there under `package/`) | 12 MB | `e0b66ad36a1e403bc702e452623f96ed44ba52882e059cd18530cb548d684c07` |

The same archive hashes appear as `matrix_archive_sha256` in the corresponding
`numerics/output/*/central_certificate.json` and `enclosure.json`, as `matrix_sha256` in
`numerics/output/independent_*/certificate.json`, and in `BUILD_RECORD.json`; the ZIP hash is
the `baseline_zip_sha256` of the archived v0.2 build record. Total size about 122 MB.

## Obtaining the files

Either regenerate them or ask for them.

* **Regenerate.** From `numerics/`, with python-flint 0.9.0 / FLINT 3.6.0 installed
  (`requirements.txt`) and assertions enabled:

  ```bash
  python certify_arb.py --N 128 --M 220 --bits 1792 --log-horizon 7 --floor 1.37e-28 --output output/log7_N128
  python certify_arb.py --N 128 --M 180 --bits 1536 --horizon 9/5   --floor 3.38e-23 --output output/length_1p8_N128
  python independent_arb.py --N 128 --M 220 --bits 1792 --log-horizon 7 --floor 1.37e-28 --output output/independent_log7
  ```

  and `--log-horizon n` with `--M 220 --bits 1792` for `log2 … log6` (floors in
  `numerics/output/enclosure_summary.json`). Each construction takes 30–90 s. Compare the
  resulting `matrices_content_sha256` with the value in the committed certificate.
* **Request.** Reviewers who want the exact saved files rather than a rebuild can request the
  folder from the author. Verify it first with `sha256sum -c SHA256SUMS.txt` from inside the
  folder; the expected content of that manifest is the table above.

## Using the files

Either copy the `output/` tree back into `numerics/output/` (`rsync -a WEIL_ARCHIVES/output/ numerics/output/`),
or leave the folder where it is and point the scripts at it:

```bash
export WEIL_ARCHIVES=/path/to/numerics-archives
cd papers/shifted-zeta/weil-depth/numerics
python certify_arb.py --reuse --bits 1792 --floor 1.37e-28 --output output/log7_N128
python enclose_certificate.py output/log7_N128
python analyze_certificate.py output/log7_N128 --shift 4e-15 --decay 6e-29 --generator-bound 14
python compare_implementations.py
```

`certify_arb.py --reuse`, `enclose_certificate.py`, `analyze_certificate.py` and
`compare_implementations.py` all fall back to `WEIL_ARCHIVES` for any archive missing from
`numerics/output/`; `analyze_certificate.py` refuses an archive whose hash differs from the
one recorded in the certificate it is asked to replay.

## What the hashes do and do not establish

`matrix_archive_sha256` identifies one exact `.gz` file; `matrices_content_sha256`
identifies the matrices and parameters inside it independently of packaging. In the
environments that were tested — Python 3.10.0, 3.11.15 and 3.12.14, each with python-flint
0.9.0 and FLINT 3.6.0 — rebuilds of the 9/5 and `log 7` archives reproduced the content hash
exactly, with identical pivots. That is an identity check for the saved data in those
environments. It is not a claim that every machine, or every Arb/FLINT release, produces
bit-for-bit identical balls: a different arithmetic implementation may legitimately produce
different (still valid) enclosures with a different content hash. The sign decisions never
depend on a hash; they are made by ball LDL on whatever matrices are present, and a rebuild
that passes the certificate is a certificate for its own matrices.
