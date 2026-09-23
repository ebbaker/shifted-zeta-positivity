# Build the WZW manuscript

This is a live standalone manuscript, with local TeX inputs and no imports from the parent manuscript. A TeX Live installation with latexmk, pdfLaTeX, Latin Modern, AMS packages, microtype, hyperref, fancyhdr and tabularx is sufficient.

From `WZW`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
```

The delivered PDF is [manuscript.pdf](manuscript.pdf). Rebuilding can change its metadata bytes without changing its mathematics. [BUILD_RECORD.json](BUILD_RECORD.json) records the source and PDF hashes, page count, inherited research inputs, and the completed visual review for this delivery. After substantive changes, inspect the new PDF and refresh that record; do not preserve a stale review claim.

For visual review, render every page into the ignored build directory:

```sh
pdftoppm -r 110 -png build/manuscript.pdf build/page
```

Resolve undefined citations or references, overflow, and layout defects before recording a new delivery. Keep intermediate logs and images in `build/`, outside the tracked source inventory. Each committed file stays under the repository's size limit. Do not add third-party PDFs.

## Existing numerical controls

The manuscript documents the unchanged 22 September records. From `WZW`, with NumPy and mpmath installed, replay them separately if the underlying mathematics or programs change:

```sh
python3 -B ../numerics/check_wzw_loewner_pilot.py --output /tmp/wzw-loewner-replay.json
python3 -B ../numerics/check_arithmetic_loewner_source.py --output /tmp/arithmetic-loewner-source-replay.json
```

The first has 72 cases and the second 60. They are separate from the parent manuscript's 299-case suite. A replay checks the program's recorded identities and inequalities; it does not prove the BCFT input, physical sewing, unweighted arithmetic contraction, or RH.

## Milestones and the parent package

Use [DRAFT_HISTOR.md](DRAFT_HISTOR.md) for a short milestone entry with a commit or tag when available, plus the reason and links to the detailed note and review. Do not create dated manuscript snapshot folders.

The parent `PACKAGE_RECORD.json` inventories this folder as well. After adding or changing files, refresh its identity inventory while preserving unrelated recorded diagnostics, and run `python3 -B validation/check_package.py check` from the parent Wilson--Loewner directory. The existing `refresh` command also reruns and rewrites the old numerical records, so it should not be used merely to register an editorial change.
