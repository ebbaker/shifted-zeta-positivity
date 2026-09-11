# Storage depth: current working manuscript (v0.3)

`manuscript/storage_depth.pdf` is the current draft, *Residual-controlled depth
extension of finite-horizon Weil positivity* (version 0.3, 10–11 September 2026).
It is a rewrite of version 0.2 as a paper rather than a consolidated laboratory
record, with the certified numbers re-derived by archive-based bisection. The
immutable earlier drafts are under `archive/drafts/` (v0.1 with all five
original research packets and their code; v0.2 with its package files), the
review that motivated v0.3 is under `archive/reviews/`, and the background
packets are under `archive/background/`.

Read `manuscript/storage_depth.pdf`, then `STATUS.md` (what is certified and
what is not), `CLAIMS.json` (record-by-record scope), and `ARCHIVES.md` (the
large matrix archives kept outside git under the repository `LARGE_FILES.md`
policy).

## What changed from v0.2 to v0.3

* The spatial floor at `L_q = (3/4) log 14` is `2.99e-29` (bisected), not the
  inserted `1e-33`; a ball Rayleigh quotient gives the upper bound `3.29e-29`.
  The shift interval widens from `5e-18` to `9e-16`. The residual factor is
  `0.78`, the comparison threshold `1.13e-7`. Records R14 and R16.
* The relative test now carries a floor directly (`M_theta >= m`, Lemma 3.2),
  which replaces the scalar comparison in the conditional continuation theorem.
* At the second step with 32-mode slabs the comparison threshold is `5.01e-8`
  (R15) and the upper bound `1.89e-30` (R16); the failed absolute and residual
  tests are diagnosed as an artifact of the three-interval complement floor
  (hypothetical-floor runs, R16, diagnostic only). A rebuild with 96-mode slabs
  (R18, 11 Sept) then certifies `1.69e-30 <= lambda_min(Q_{0,L_2}) <= 1.89e-30`,
  residual factor `0.8`, `mu = 5.25e-8`, shift interval `2e-16`.
* A Fourier-side computation (R17, diagnostic) compares the lowest eigenvector's
  zero sum with its eigenvalue and measures what the certificate can see.
* New tools: `numerics/recursion/stream_io.py` (streaming dual-hash loader that
  runs in a few GB of memory), `replay_floor.py` (archive-based replays with
  bisection), `rayleigh_upper.py` (ball Rayleigh upper bounds),
  `build_step_seed.py` / `build_from_seed_v2.py` (extend a first-step archive of
  any slab dimension; `build_step.py` is left byte-identical so the recorded
  archives still verify), `numerics/tools/` (continuation, upper bound and
  catalog helpers for R18), and `numerics/fourier_side/` (the R17 scripts).

A numerical certificate means its stated analytic reduction plus guarded
interval sign tests in the working Weil-depth normalization. The normalization
audit and independent mathematical review remain open. Nothing here is a
statement about zeros of zeta.

## Reproduce

Python 3.10 or 3.11, python-flint 0.9.0 (FLINT 3.6.0), mpmath 1.3 or 1.4; keep
assertions enabled. From this paper directory, with the sibling archive present:

~~~bash
export STORAGE_DEPTH_ARCHIVES=/absolute/path/to/shifted-zeta-positivity-archive/storage-depth/numerics-archives
cd numerics/recursion

# R14: first-step bisections (about 14 minutes at 2048 bits on one core)
python -B replay_floor.py --step 1 --bits 2048 \
  --relative 0.85 0.8 0.78 0.76 0.75 \
  --bisect-absolute 1e-33 1e-28 --bisect-relative 0.9:1e-33:1e-28 0.8:1e-33:1e-28 \
  --bisect-mu 1e-7 2e-7 --output /your/scratch/floor-bisection-first-2048.json

# R15: second-step bisection and recorded failures (about 8 minutes)
python -B replay_floor.py --step 2 --bits 2048 --absolute 1e-36 --relative 0.9 0.95 0.99 \
  --bisect-mu 1e-8 1e-7 --output /your/scratch/floor-bisection-second-2048.json

# R16: upper bounds and hypothetical-floor diagnostics
python -B rayleigh_upper.py --step 1 --output /your/scratch/rayleigh-upper-first-2048.json
python -B rayleigh_upper.py --step 2 --output /your/scratch/rayleigh-upper-second-2048.json
python -B replay_floor.py --step 2 --oracle-tail-floor 0.55 --absolute 1e-36 --relative 0.9 \
  --output /your/scratch/oracle-second-0.55.json

# R18: rebuild the first step with 96 slab modes (needs the old_256_320_6144 cache beside the output),
#      extend it, and certify (about 40 + 85 minutes at 6144 bits; see ARCHIVES.md for the paths)
cd ../../archive/drafts/v0.1_2026-09-10/numerics
python -B history/quarter-step-closure-20260910/close_complement.py --old 256 --new 96 --bits 6144 --floor 1e-30 \
  --output "$STORAGE_DEPTH_ARCHIVES/history/first-step-96-20260911/closure_256_96.json"
cd ../../../../numerics
python -B tools/describe_archive.py --archive "$STORAGE_DEPTH_ARCHIVES/history/first-step-96-20260911/closure_256_96.matrices.json.gz" \
  --output "$STORAGE_DEPTH_ARCHIVES/history/first-step-96-20260911/ARCHIVE_RECORDS.json"   # compare content hash with records/closure_256_96_catalog.json
cd recursion
python -B build_from_seed_v2.py --seed-catalog "$STORAGE_DEPTH_ARCHIVES/history/first-step-96-20260911/ARCHIVE_RECORDS.json" \
  --seed-archives "$STORAGE_DEPTH_ARCHIVES/history/first-step-96-20260911" --seed-relative closure_256_96.matrices.json.gz \
  --new 96 --bits 6144 --floor 1e-30 --archive-dir "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-96" \
  --archive-relative output/second-quarter-96/central_matrices.json.gz --record /your/scratch/second-quarter-96-build.json
# a rebuilt gzip has a new file hash: use the record your build wrote, and compare its
# matrices_content_sha256 with records/second-quarter-96-build.json
python -B ../tools/galerkin_continuation.py --record /your/scratch/second-quarter-96-build.json \
  --output "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-96/second-quarter-96-continuation.json"
python -B replay_floor.py --step 2 --record /your/scratch/second-quarter-96-build.json \
  --continuation "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-96/second-quarter-96-continuation.json" \
  --relative 0.9 0.8 --bisect-absolute 1e-30 1e-28 --bisect-relative 0.9:1e-31:1e-28 --bisect-mu 1e-8 1e-7 \
  --output /your/scratch/floor-bisection-second96-2048.json
python -B ../tools/rayleigh_upper_record.py --record /your/scratch/second-quarter-96-build.json --output /your/scratch/rayleigh-upper-second96-2048.json

# R17: Fourier-side diagnostic (export the head, then the zero sums; mpmath only after the export)
cd ../fourier_side
python -B export_head.py /your/scratch/head288_mid.json
python -B zero_sum_check.py /your/scratch/head288_mid.json zeta_zeros_400.json /your/scratch/zero_sum_check_K400.json 400
python -B zero_sensitivity.py ../records/rayleigh-upper-first-2048.json zeta_zeros_400.json /your/scratch/zero_sensitivity_K20.json 20
~~~

The earlier validators (`certify_step.py`, `metric_comparison.py`,
`weighted_residual.py`, `build_step.py`, `check_spatial.py`) are unchanged and
still run; `certify_step.py` and `weighted_residual.py` use `json.load` and
need more than 3 GB of memory for the second-step archive, whereas the new
tools stream. The v0.1 replays and rebuilds are described in
`archive/drafts/v0.1_2026-09-10/ARCHIVES.md`. Large derived files belong in the
sibling archive, never in git.

## Build the manuscript

`make` with pdflatex and latexmk installed (the source needs `lmodern`,
`mathrsfs`, `microtype`, `booktabs`, `enumitem`, `hyperref`). Temporary files go
under `/tmp/storage-depth-tex`.
