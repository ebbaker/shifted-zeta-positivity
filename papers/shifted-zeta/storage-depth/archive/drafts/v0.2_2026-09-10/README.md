# Storage depth: current working manuscript

Version 0.2 develops the old-energy comparison, explicit conditional induction,
and a partition-based second quarter-step experiment. The immutable version
0.1 manuscript and all five original research packets remain in
archive/drafts/v0.1_2026-09-10/.

Read manuscript/storage_depth.pdf, STATUS.md, and ARCHIVES.md.
The second-step old-energy comparison passes; the second-step residual
and absolute positivity sufficient tests do not. No new full-operator
horizon beyond the inherited 1.98 certificate is claimed.
The original normalization and independent mathematical review obligations
remain open. A numerical certificate means its stated analytic reduction
plus guarded interval sign tests in the working Weil-depth normalization.

## Reproduce the new work

Use Python 3.10, python-flint 0.9.0 / FLINT 3.6.0, and mpmath 1.4.1.
Keep assertions enabled. From this paper directory:

~~~bash
export STORAGE_DEPTH_ARCHIVES=/absolute/path/to/shifted-zeta-positivity-archive/storage-depth/numerics-archives

python -B numerics/recursion/check_spatial.py \
  --output /your/scratch/spatial-consistency.json

python -B numerics/metric_comparison.py \
  --paper archive/drafts/v0.1_2026-09-10 \
  --archives "$STORAGE_DEPTH_ARCHIVES" --bits 2048 --mu 1e-7 \
  --output /your/scratch/metric-comparison.json

python -B numerics/recursion/build_step.py \
  --archive-dir "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-rebuild" \
  --archive-relative output/second-quarter-rebuild/central_matrices.json.gz \
  --record /your/scratch/second-quarter-rebuild.json

python -B numerics/recursion/certify_step.py \
  --record numerics/records/second-quarter-build.json \
  --bits 2048 --output /your/scratch/second-quarter-replay.json
~~~

The second-step builder preserves the original 256-plus-32 spatial head and
appends 32 modes on a second quarter slab. It verifies the first-step archive
before use. It recomputes the new output and cross Grams, translated windows,
and analytic complement. All current Taylor calculations enforce total
length below three. The proof and source explain the inherited Gram error.

For a replay with the recorded rational continuation, add:

~~~bash
--continuation numerics/records/second-quarter-continuation.json
~~~

The certificate script also tries full-old energy and residual inequalities.
A failed sufficient test is recorded as a failure to certify, not as
operator negativity. Successful finite computations alone do not establish
indefinite continuation or prevent finite-depth accumulation.

The exact v0.1 sign replays and a fresh first-step rebuild are provided by
archive/drafts/v0.1_2026-09-10/numerics/replay.py; its archived guide gives
the commands. Large derived files belong in the sibling archive, never Git.

## Build the manuscript

Run make with pdflatex and latexmk installed. Temporary LaTeX files go
under /tmp/storage-depth-tex by default. The source contains the complete
current mathematical argument; the archived source is unchanged.
