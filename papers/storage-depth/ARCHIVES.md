# External storage-depth matrices

This is the current tracked guide under the repository LARGE_FILES.md policy (v0.3, closeout 11 September 2026; includes the two R18 archives added after v0.2).
Sources, PDFs, exact continuation coefficients, and small certificate records
stay in Git. All regenerable matrix archives stay in the external
szp-archive/storage-depth/numerics-archives/ directory.
No new archive is committed, no Git LFS is used, and no download service is
required. The current local root is `/Users/Shared/szp-archive`.
See the repository's [storage-depth closeout](https://github.com/ebbaker/shifted-zeta-positivity/blob/main/papers/storage-depth/CLOSEOUT.md)
for the latest archive-availability audit.

## Closeout availability (11 September 2026)

The local audit found four of the six recorded matrices, all matching their
stored-file hashes and sizes. The two R18 matrices below are absent; their
small records, exact continuation and regeneration instructions are present.
The author accepted this availability state for closing the writing project.
Additional large Fourier-analysis outputs from Claude were intentionally
not retained because of size; the author confirmed that omission is acceptable.
The small R17 diagnostics remain in the repository. No omitted computation
was rerun for this housekeeping audit.

## Layout and lookup

Set STORAGE_DEPTH_ARCHIVES to the absolute path of your numerics-archives copy.
The new loader first checks the requested relative path under this paper's
numerics/ directory, then that same relative path under STORAGE_DEPTH_ARCHIVES.
A corrupt in-tree copy fails verification; it is not silently bypassed.
The unchanged v0.1 loader uses its archived numerics/ directory as its normal
location, with the same external root and relative paths.

~~~text
numerics-archives/
  README.md
  SHA256SUMS.txt
  ARCHIVE_RECORDS.json
  history/quarter-step-closure-20260910/
    closure_256_32.matrices.json.gz
    old_128_320_6144.json.gz
    old_256_320_6144.json.gz
  history/first-step-96-20260911/            (v0.3, R18; regenerate locally)
    closure_256_96.matrices.json.gz
    closure_256_96.json
    ARCHIVE_RECORDS.json
  output/second-quarter/
    central_matrices.json.gz
    build_record.json
  output/second-quarter-96/                  (v0.3, R18; regenerate locally)
    central_matrices.json.gz
    build_record.json
    second-quarter-96-continuation.json
~~~

The second-step archive contains a 320-by-320 head and three complete output
Grams, at lengths (log(7), log(8/7)/4, log(8/7)/4), with retained dimensions
(256,32,32), degree 320, and 6144-bit arithmetic. It inherits the hash-verified
first-step head and old/old Gram blocks. It includes the inherited-model error;
it is not a second independent reconstruction of the first step.

## Archive inventory

Paths are relative to numerics/ or STORAGE_DEPTH_ARCHIVES. The catalog is
numerics/ARCHIVE_RECORDS.json. Each file has a stored-file hash and a canonical
matrix-content hash; both are checked before the matrices are used.

### history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz

Size: 160584016 bytes.

Stored-file SHA-256:

    4e421883b6b918a5dd751430a73d115ce22398262ecb28773eaebf6005c7d75d

Canonical matrix-content SHA-256:

    ceccde610b1d8fad050444bee8d4d587a7a552e2b8a022002df64f9c9fe6170d

### history/quarter-step-closure-20260910/old_128_320_6144.json.gz

Size: 43429046 bytes.

Stored-file SHA-256:

    fc6a0d1af3e9db51b48f52139749798ef0600824be43fd1e54c3d78f087bff72

Canonical matrix-content SHA-256:

    f920def55bfc99ab4cffcf140f9c00db4347505f61c22555e457776fb08ba36a

### history/quarter-step-closure-20260910/old_256_320_6144.json.gz

Size: 173696589 bytes.

Stored-file SHA-256:

    a3fdcfd0731095cd5fb89d7a1e079dd3894d26d647f196cdf94bdc72b1b80d3c

Canonical matrix-content SHA-256:

    c69695ce5531561fd511083cd3a02086a69d99ed561777a19699ed3f2a195584

### output/second-quarter/central_matrices.json.gz

Size: 297151691 bytes.

Stored-file SHA-256:

    abce193c5bbc74b5089b193c82edfad4802b433e6daade35587e3719e5f940ee

Canonical matrix-content SHA-256:

    62c4f708f7d6b26d7d76d09f3fe0d4a5ba8d18af5a496fead2aef89fe456775d

The absolute and residual sufficient tests are unsuccessful at the recorded
parameters; the full-old candidate-energy comparison succeeds at mu=1e-8.
The archive preserves the complete matrices needed for stronger tests.

### history/first-step-96-20260911/closure_256_96.matrices.json.gz (v0.3, R18)

Size: 265734856 bytes. Built 11 September 2026 in a cloud container (Python
3.11.15, python-flint 0.9.0, FLINT 3.6.0) by the unchanged v0.1 builder
close_complement.py with --old 256 --new 96 --bits 6144 --floor 1e-30 and the
old_256_320_6144 cache present. Two-interval complement floor 1.109.

Stored-file SHA-256:

    a64e5539915e861b71603ecfee7a78d30c84cee0b888372ca2fe71d2e02da742

Canonical matrix-content SHA-256:

    14bce4f625313ccaa7cdf8af3eb09c41cd344353c05861067635ec925a1aebac

Small records: numerics/records/closure_256_96.json (build record) and
numerics/records/closure_256_96_catalog.json (its one-entry catalog, path
relative to the seed folder). This archive is the seed of the next one.

### output/second-quarter-96/central_matrices.json.gz (v0.3, R18)

Size: 632719410 bytes; 448-by-448 head and three complete output Grams at
lengths (log 7, log(8/7)/4, log(8/7)/4), retained dimensions (256, 96, 96),
degree 320, 6144-bit arithmetic; built by build_from_seed_v2.py /
build_step_seed.py from the 96-mode seed in 5125 seconds. Three-interval
complement floor 0.76828; the absolute test at 1e-30 passes at build time.

Stored-file SHA-256:

    2a7791e1acfa7fd0f9dda2c76a379eec521b5bc7ce2a6e7f72bd9ee507739282

Canonical matrix-content SHA-256:

    5ebedbe6c4f0fee175dd49c14b480e1d7a07f8506db020b442077876894feb87

Beside it, outside git: second-quarter-96-continuation.json (3018378 bytes,
the exact rational Galerkin continuation, 96 by 352, 80 decimal digits),
SHA-256 fd78c8652ac441e26e3f9598610974d791e98c637e7abddda4134fdb5ba9693e.
Small records: numerics/records/second-quarter-96-build.json,
floor-bisection-second96-2048.json, rayleigh-upper-second96-2048.json.

These two archives were not produced on the maintainer's machine. Regenerate
them with the R18 commands in README.md (about 40 and 85 minutes at 6144 bits
on one core) and compare the canonical content hashes; a rebuilt gzip has its
own file hash, and the loaders check the file hash of the record you pass them,
so use the build record your own run writes.


## Regeneration and replay

Use the pinned Python dependencies in numerics/requirements.txt. Keep
assertions enabled. All commands below run from this paper directory.

To regenerate the first step from source without a matrix cache:

~~~bash
python -B archive/drafts/v0.1_2026-09-10/numerics/replay.py rebuild \
  --output-dir /absolute/path/to/new-first-step-build
~~~

The first-step runner writes a new catalog with both hashes. It can also
rebuild the optional failed 128-plus-32 attempt with rebuild-initial. See the
archived ARCHIVES.md for its complete instructions and the unchanged records.

To regenerate the second step from the verified first-step archive:

~~~bash
export STORAGE_DEPTH_ARCHIVES=/absolute/path/to/szp-archive/storage-depth/numerics-archives
python -B numerics/recursion/build_step.py \
  --archive-dir "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-rebuild" \
  --archive-relative output/second-quarter-rebuild/central_matrices.json.gz \
  --record /your/scratch/second-quarter-rebuild.json
~~~

This writes the large archive externally and a small build record both beside
the data and at the specified record path. Parameters default to the recorded
values. A rebuilt gzip has its own file hash; compare the content hash to
recognize identical serialized matrices. To use a freshly rebuilt first-step
catalog without changing the immutable v0.1 records, use
numerics/recursion/build_from_seed.py, which verifies both data hashes and the
seed generating-source hashes before construction. Keep and review the new
catalog and sign records. Never bypass a mismatch merely to make a replay run.

### Streaming loader and archive-based replays (v0.3)

The recorded archives decompress to 344 MB and 635 MB, and json.load of the
larger one needs more than 3 GB of memory. numerics/recursion/stream_io.py
parses an archive incrementally, converts entries to Arb balls as they are
read, and recomputes the canonical matrix-content hash while streaming, so the
same size, file-hash, content-hash and builder-source checks as archive.py and
the v0.1 archive_io.verify are performed in a few gigabytes. A mismatch raises.

numerics/recursion/replay_floor.py re-runs the absolute, relative and
comparison tests from the hash-verified archives with a chosen floor, residual
factor or comparison threshold, or bisects for the largest passing
three-significant-figure value; it writes the trace of every guarded test.
numerics/recursion/rayleigh_upper.py computes ball Rayleigh upper bounds for
the lowest eigenvalue from the head alone. The commands that produced records
R14-R16 are listed in README.md. An --oracle-tail-floor run replaces the
certified analytic complement floor by a stated number; it is a diagnostic of
the finite matrices and is recorded as such, never as a certificate.

The recorded validators certify_step.py and weighted_residual.py remain as
they were; they replay at two working precisions:

~~~bash
python -B numerics/recursion/certify_step.py \
  --record numerics/records/second-quarter-build.json --bits 2048 \
  --continuation numerics/records/second-quarter-continuation.json \
  --output /your/scratch/second-quarter-2048.json
~~~

A source-only reviewer may regenerate the data or request the six recorded matrix
files from the repository maintainer, quoting the names and hashes above.
There is no public download URL or dataset DOI for these regenerable files.

## Integrity and repository hygiene

From the external folder, run shasum -a 256 -c SHA256SUMS.txt. The Python
loaders additionally verify canonical matrix contents. Canonical serialization
is compact UTF-8 JSON of data["matrices"], with sorted dictionary keys,
unchanged list ordering and Arb entries, ensure_ascii=True, and allow_nan=False.
Other metadata, gzip headers, and compression are excluded from the content
hash. Hashes identify data; analytic enclosures and arithmetic sign tests
establish the stated certificate. Cross-version bitwise portability is not
claimed.

The paper's .gitignore excludes compressed matrices, array caches, sweep
outputs, and review ZIPs. The current BUILD_RECORD.json and SHA256SUMS.txt list
only small source-package deliverables, never external matrices. Before any
commit, run the staged/tree/history size checks in the root LARGE_FILES.md.
All current small deliverables must remain below 1 MiB. The old Weil topic
branch history is a separate repository-maintenance matter; no history is
rewritten by this storage-depth work.

## Separate-tail residual replay (v0.2, historical)

The refined tests still do not certify the second-step residual inequality.
For the fixed higher-precision replay of the recorded weight triple:

~~~bash
python -B numerics/recursion/weighted_residual.py \
  --record numerics/records/second-quarter-build.json \
  --comparison numerics/records/second-quarter-4096.json \
  --continuation numerics/records/second-quarter-continuation.json \
  --bits 2048 --theta 0.9999 \
  --weights 1 0.6335965029937086 0.3895577505597481 --attempts 1 \
  --output /your/scratch/second-quarter-weighted-2048.json
~~~

The two ten-proposal experiments use 1024 bits, theta=0.99 with initial
weights (1,0.6,0.38), and theta=0.9999 with initial weights (1,0.63,0.39).
Their small records preserve all proposed weights and failed guards.
No negative-operator claim is inferred from these outcomes.
