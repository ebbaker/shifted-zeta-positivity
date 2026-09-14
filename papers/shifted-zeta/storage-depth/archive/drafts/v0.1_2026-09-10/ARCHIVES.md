# External matrix archives

This tracked guide is canonical. It implements the repository LARGE_FILES.md
policy retrieved 10 September 2026 (Git blob
df63856efee3f438fc013d5086fbf1bd709ede26).

Git holds sources and small records. Every deliverable intended for the
repository is below 1 MiB; these three regenerable matrix files are external.
Neither delivery ZIP belongs in git. No Git LFS or cloud-drive dependency is used.

## Layout and lookup

The normal in-tree location is papers/storage-depth/numerics/<path below>.
The supported loader checks that location first, then the identical relative
path under STORAGE_DEPTH_ARCHIVES. No other search path or built-in download is
used. The external delivery folder is:

    shifted-zeta-positivity-archive/
      storage-depth/
        numerics-archives/
          README.md
          SHA256SUMS.txt
          ARCHIVE_RECORDS.json
          history/quarter-step-closure-20260910/
            closure_256_32.matrices.json.gz
            old_128_320_6144.json.gz
            old_256_320_6144.json.gz

From the paper directory, point the environment variable to your copy:

    export STORAGE_DEPTH_ARCHIVES=/absolute/path/to/shifted-zeta-positivity-archive/storage-depth/numerics-archives
    python numerics/replay.py verify --archives
    python numerics/replay.py relative --output-dir numerics/replays/relative
    python numerics/replay.py spatial-sign --output-dir numerics/replays/spatial-sign

Use Python with the pinned dependencies. The runner checks both hashes before
staging a verified copy for unchanged historical consumers; it also verifies the
staged bytes. A missing file or mismatch stops the replay with an explanation.
The normal in-tree location takes precedence, including on mismatch; a corrupt
local file is not silently bypassed by an external copy.

From inside numerics-archives, a quick stored-file check is:

    shasum -a 256 -c SHA256SUMS.txt

The complete lookup and dual-hash check is the replay verify --archives action.

## Inventory

Paths below are relative to either numerics/ or the external numerics-archives/.
One MiB is 1,048,576 bytes; MB is decimal.


### closure_256_32.matrices.json.gz

Path: history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz

Size: 160,584,016 bytes; 153.145 MiB; 160.584 MB.

Complete 288-by-288 head and separate old/new full-output Grams, stored as Arb midpoint/radius data. Required for replaying the .9 relative test and the absolute spatial sign without rebuilding.

Stored-file SHA-256:

    4e421883b6b918a5dd751430a73d115ce22398262ecb28773eaebf6005c7d75d

Canonical matrix-content SHA-256:

    ceccde610b1d8fad050444bee8d4d587a7a552e2b8a022002df64f9c9fe6170d

Recorded parameters:

    {"log_series_degree": 100, "new_modes": 32, "old_modes": 256, "precision_bits": 6144, "profile_degree": 320}


### old_128_320_6144.json.gz

Path: history/quarter-step-closure-20260910/old_128_320_6144.json.gz

Size: 43,429,046 bytes; 41.417 MiB; 43.429 MB.

Optional old-depth cache for the unsuccessful 128-plus-32 historical sufficient test. Retained for the complete research history; no negative-form conclusion is drawn from that failed test.

Stored-file SHA-256:

    fc6a0d1af3e9db51b48f52139749798ef0600824be43fd1e54c3d78f087bff72

Canonical matrix-content SHA-256:

    f920def55bfc99ab4cffcf140f9c00db4347505f61c22555e457776fb08ba36a

Recorded parameters:

    {"M": 320, "N": 128, "horizon": null, "log_horizon": 7, "precision_bits": 6144}


### old_256_320_6144.json.gz

Path: history/quarter-step-closure-20260910/old_256_320_6144.json.gz

Size: 173,696,589 bytes; 165.650 MiB; 173.697 MB.

Optional old-depth cache used in rebuilding the successful spatial construction. It contains old-interval matrices only and assumes no new-depth global positivity result.

Stored-file SHA-256:

    a3fdcfd0731095cd5fb89d7a1e079dd3894d26d647f196cdf94bdc72b1b80d3c

Canonical matrix-content SHA-256:

    c69695ce5531561fd511083cd3a02086a69d99ed561777a19699ed3f2a195584

Recorded parameters:

    {"M": 320, "N": 256, "horizon": null, "log_horizon": 7, "precision_bits": 6144}


## Regeneration and recognition

No external data are needed for a fresh build. From the paper directory:

    python numerics/replay.py rebuild --output-dir /absolute/path/to/new-build

This runs the unchanged spatial constructor with old=256, new=32, profile
degree=320, logarithm degree=100, precision=6144 bits, cells=512, and floor=1e-33.
It writes the old 256-mode cache and the spatial archive under the same
history/quarter-step-closure-20260910/ relative path in the new output folder.
The historical full construction took about 21 minutes; runtime varies.

To reconstruct the optional old 128-mode cache and repeat the initial attempt:

    python numerics/replay.py rebuild-initial --output-dir /absolute/path/to/new-initial-build

The initial sign test is expected to fail its sufficient criterion. The original
initial source snapshot is used. Differences in the small record's source-path
metadata are possible because the snapshot now has an archival filename.

To accelerate either build with a historical old cache, add --use-cache.
The cache is located by the same two-location rule and verified before use.
Without --use-cache, no old cache is staged, so a fresh reconstruction occurs.

Every newly generated gzip archive gets its own small ARCHIVE_RECORDS.json,
with both hashes and its parameters, and a SHA256SUMS.txt. Compare its
matrices_content_sha256 to this tracked catalog to recognize equal matrices.
The file hash of a rebuild can change because gzip headers and build elapsed
time change. Do not replace a tracked file hash without reviewing the new data
and the associated arithmetic sign result.

Canonical matrix serialization is defined exactly in numerics/archive_io.py:
compact UTF-8 JSON of data["matrices"], sorted dictionary keys, unchanged list
ordering and Arb entry values, ensure_ascii=True, and allow_nan=False.
All other metadata, gzip time, gzip filename, and compression are excluded.

The content hash identifies the serialized matrices. It does not certify
their derivation, enclosure validity, analytic error budget, or positivity.
Those are decided by the builder, mathematical reductions, and arithmetic sign
tests. Identity has been tested only in the recorded environment; portable
bit-for-bit arithmetic across libraries and versions is not promised.

## Obtaining and maintaining a copy

The accompanying external-data delivery ZIP contains this entire folder.
For a source-only checkout, regenerate using the commands above or request the
storage-depth matrix packet dated 10 September 2026 from the repository
maintainer, quoting the requested filenames and hashes in this guide. No stable
public download URL or dataset DOI has been created for these regenerable files.

The paper's .gitignore excludes numerics/**/*.json.gz and numerics-archives/;
the overlay root adds the latter as a backstop. Before committing, confirm:

    git check-ignore -v papers/storage-depth/numerics/history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz

The paper BUILD_RECORD.json and SHA256SUMS.txt list only small deliverables,
never these external data. Source release completeness comes from the code,
parameters, hashes, and this guide; the raw matrices stay outside the tag tree.
