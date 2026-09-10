# External storage-depth matrices

This is the current tracked guide under the repository LARGE_FILES.md policy.
Sources, PDFs, exact continuation coefficients, and small certificate records
stay in Git. All regenerable matrix archives stay in the sibling
shifted-zeta-positivity-archive/storage-depth/numerics-archives/ directory.
No new archive is committed, no Git LFS is used, and no download service is
required.

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
  output/second-quarter/
    central_matrices.json.gz
    build_record.json
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
export STORAGE_DEPTH_ARCHIVES=/absolute/path/to/shifted-zeta-positivity-archive/storage-depth/numerics-archives
python -B numerics/recursion/build_step.py \
  --archive-dir "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-rebuild" \
  --archive-relative output/second-quarter-rebuild/central_matrices.json.gz \
  --record /your/scratch/second-quarter-rebuild.json
~~~

This writes the large archive externally and a small build record both beside
the data and at the specified record path. Parameters default to the recorded
values. A rebuilt gzip has its own file hash; compare the content hash to
recognize identical serialized matrices. A freshly rebuilt first step has its own catalog. To use that catalog without
changing the immutable v0.1 records, use the following entry point; it verifies
both data hashes and the seed generating-source hashes before construction.

~~~bash
python -B numerics/recursion/build_from_seed.py \
  --seed-catalog /absolute/path/to/new-first-step-build/ARCHIVE_RECORDS.json \
  --seed-archives /absolute/path/to/new-first-step-build \
  --archive-dir "$STORAGE_DEPTH_ARCHIVES/output/second-quarter-rebuild" \
  --archive-relative output/second-quarter-rebuild/central_matrices.json.gz \
  --record /your/scratch/second-quarter-rebuild.json
~~~

Keep and review the new catalog and sign records. Never bypass a mismatch
merely to make a replay run.

To replay the recorded second step at two working precisions:

~~~bash
python -B numerics/recursion/certify_step.py \
  --record numerics/records/second-quarter-build.json --bits 2048 \
  --continuation numerics/records/second-quarter-continuation.json \
  --output /your/scratch/second-quarter-2048.json
python -B numerics/recursion/certify_step.py \
  --record numerics/records/second-quarter-build.json --bits 4096 \
  --continuation numerics/records/second-quarter-continuation.json \
  --output /your/scratch/second-quarter-4096.json
~~~

A source-only reviewer may regenerate the data or request these four matrix
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

## Separate-tail residual replay

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
