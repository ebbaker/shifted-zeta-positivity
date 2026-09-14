# Manuscript build and validation

The current working draft is [manuscript.pdf](manuscript.pdf), with [manuscript.tex](manuscript.tex) as its entry point, calculation sources under `sections/`, and external references in [references.tex](references.tex). It is self-contained and does not input the shared background or cite its equation numbers.

A standard TeX distribution with `latexmk` and pdfLaTeX is sufficient. From this investigation directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
```

The ignored `build/` directory holds intermediate files. Check the final log for undefined references, citations and overfull boxes. Render the PDF and inspect the pages, particularly after changing equations or page breaks. [BUILD_RECORD.json](BUILD_RECORD.json) records the reviewed source hashes and compiled PDF; it describes one completed build, not a claim that PDF metadata is byte-reproducible across environments.

After reviewed source or deliverable changes, refresh the package manifest explicitly and replay the small algebra checks:

```sh
python3 validation/refresh_manifest.py
python3 validation/check_package.py --replay
```

A fresh compilation changes the PDF hash and requires a new build record after visual review. Do not update a historical algebra record merely to make a replay pass. The manifest and build record establish file identity; the analytical arguments remain subject to mathematical review.

The current PDF is below the repository size limit. No third-party PDF is included. See [ARCHIVES.md](ARCHIVES.md) before producing large numerical data or review bundles.

## Dated draft snapshots

The [draft archive](archive/drafts/README.md) contains the exact pre-integration version, the integration through note 19, and the live version immediately before note 20. The current manuscript integrates the sign analysis in note 20. Each snapshot can be built using the same command above in a separate working copy so archived sources remain unchanged. The [coverage map](MANUSCRIPT_COVERAGE.md) lists the current results. Package validation also checks the current and archived build-record source hashes and snapshot hashes.
