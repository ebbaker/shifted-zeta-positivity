# Manuscript and continuation package

The manuscript-and-code ZIP contains a repository-ready overlay with the
17-page draft PDF, editable LaTeX, all five original research packets, exact
coefficients, certificate records, reproducibility tools, and continuation notes.

The external-data ZIP contains the separate matrix archive folder. Extract both
ZIPs into the same directory to obtain the intended sibling layout. Do not put
either ZIP or the external matrix tree into git.

Start with shifted-zeta-positivity/papers/storage-depth/README.md and
CONTINUATION.md. ARCHIVES.md gives both hashes, the environment-variable lookup,
and regeneration instructions. The first two replay actions of interest are
spatial-sign and relative; the latter reproduces the full old-domain factor .9.
The normalizations remain subject to the author's independent verification.

The data bundle includes three gzip files. Only the spatial matrix file is
required for direct sign replays; the two old-depth caches are optional
acceleration for rebuilding and the failed historical attempt.

DELIVERY_RECORD.json lists all file sizes and delivery hashes. The top-level
SHA256SUMS.txt checks the ZIPs. Each extracted tree has its own checksum manifest.
