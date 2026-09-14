# Draft snapshots and external numerical archives

The governing policy is [LARGE_FILES.md](../../../../LARGE_FILES.md). This investigation currently has no large derived data and no required external numerical input.

## Location and lookup

Large regenerable outputs belong in:

```text
szp-archive/susy-positivity/arithmetic-ground-state-geometry/numerics-archives/
    README.md
    SHA256SUMS.txt
    output/<experiment>/<files>
```

The maintainer's current `szp-archive` root is `/Users/Shared/szp-archive`. Portable scripts must not embed that machine path. Set `ARITHMETIC_GROUND_STATE_ARCHIVES` to the investigation's `numerics-archives` directory. A consumer should first look for the expected relative path under `numerics/`, then the same relative path under that environment-variable root, and fail clearly if neither exists. No other search or automatic download fallback is permitted.

## When an experiment produces large data

Keep the generator and exact run parameters in the repository. Write data outside the repository, retaining the same relative `output/<experiment>/...` layout. The small record must identify the file size, stored-byte SHA-256, and, for structured data, the canonical uncompressed-content SHA-256. Every consumer verifies the recorded hash before using the data.

Add each archive's path, size, hashes, regeneration command, software requirements and availability to this guide. Update the archive's `SHA256SUMS.txt` and copy this canonical guide to its `README.md`. Check the relevant ignore rules. Hash agreement establishes identity of data, not a positivity theorem or portability of floating-point output.

No individual repository file should exceed about 1 MiB. Large sweeps, matrices, zero caches, review bundles and third-party papers do not belong in this package. No archive directory will be created merely as a placeholder for nonexistent data.

## Current archive inventory

None. The theoretical derivations and any small identity diagnostics can be reproduced without external data.

## Manuscript draft inventory

Small manuscript snapshots are separate from the external numerical-data inventory above. [archive/drafts/README.md](archive/drafts/README.md) indexes the previous 25-page draft, the integrated version through note 19, and the exact 48-page live version before note 20's sign analysis. Each dated directory contains a PDF, complete TeX sources, the build record and stored-byte SHA-256 hashes. Individual PDFs remain below 1 MiB. Snapshot files are historical and must not be updated when the live manuscript changes. Note 20 produced only small exact records and requires no external numerical data.
