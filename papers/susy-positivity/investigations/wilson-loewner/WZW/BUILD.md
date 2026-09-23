# Build the thermal orbit-weight manuscript

The live standalone manuscript uses local TeX inputs and does not import the parent manuscript. It now focuses on the Bost–Connes orbit-weight investigation, with earlier tests summarized near the end. A TeX Live installation with latexmk, pdfLaTeX, Latin Modern, AMS packages, microtype, hyperref, fancyhdr and tabularx is sufficient.

From `WZW`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
```

The delivered [PDF](manuscript.pdf) has 12 pages. [BUILD_RECORD.json](BUILD_RECORD.json) records its identity, active sources, research inputs, numerical provenance and visual review. Rebuilding can alter PDF metadata bytes without altering the mathematics. After substantive changes, inspect the new PDF and refresh the record rather than preserving a stale review claim.

The active sections are `01_scope`, `02_arithmetic_target`, `03_thermal_weights`, `04_norms_and_limits`, `05_physical_interface`, `06_previous_tests` and `a_validation`, together with the entry point, preamble and references. Seven older section fragments remain in the folder but are not compiled; the record identifies them separately.

Render every page for review:

```sh
pdftoppm -r 110 -png build/manuscript.pdf build/page
```

Resolve undefined references or citations, overflow and layout defects before recording a delivery. Keep intermediate logs and images in the ignored `build/` directory or outside the repository. Check relative links to the research notes from the delivered PDF's directory. Each committed file must remain under the repository's size limit; do not add third-party PDFs.

## Recorded numerical controls

The current argument uses the unchanged 87-case orbit-weight record: 17 exact integer and 70 floating controls. From `WZW`, with Python 3 and mpmath installed:

```sh
python3 -B numerics/check_arithmetic_orbit_weights.py --output /tmp/arithmetic-orbit-weights-replay.json
```

The manuscript revision is an editorial integration of the completed research and adds no numerical cases. The program and record hashes were checked; the suite was not rerun merely to rewrite the manuscript. Earlier controls remain separate: WZW pilot 72, arithmetic source 60, bounded collar 60, Brownian readout 51, modular scattering 65, fractional cusp 80. See [numerics/README.md](numerics/README.md) and the linked notes for replay commands and limitations. These controls do not establish a causal completed physical realization or RH.

## Milestones and package identity

Use [DRAFT_HISTOR.md](DRAFT_HISTOR.md) for concise milestones, pointing to the containing commit or tag when available and the detailed note and review. Do not create dated manuscript snapshots.

The parent `PACKAGE_RECORD.json` inventories this folder. Refresh its file identities after edits while preserving all unrelated numerical records and custom research metadata. Then run `python3 -B validation/check_package.py check` from the parent Wilson–Loewner directory. The validator's `refresh` command also reruns and rewrites older diagnostics, so it should not be used for a purely editorial update.
