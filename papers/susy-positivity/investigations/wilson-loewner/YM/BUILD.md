# Building the YM manuscript

25 September 2026. Drafted for Edward Baker with substantial LLM assistance. Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.

The maintained manuscript is [manuscript.tex](manuscript.tex), with its [preamble](preamble.tex), [sections](sections/), and [references](references.tex). The readable deliverable is [manuscript.pdf](manuscript.pdf). This is a consolidation of the existing investigation, which is paused at the author's request. It is not a new dated snapshot.

From this YM directory, with a standard TeX Live installation providing latexmk and pdflatex:

    LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
    cp build/manuscript.pdf manuscript.pdf

The source uses standard LaTeX mathematics, Latin Modern fonts, microtype, hyperref, and table packages. No shell escape, external dataset, bibliography service, or network access is needed to build it. The bibliography is supplied as LaTeX in references.tex.

The recorded build used TeX Live 2023, pdfTeX 3.141592653-2.6-1.40.25, and latexmk 4.79. The resulting PDF has 35 pages and remains below the repository's approximately 1 MB per-file target. BUILD_RECORD.json identifies the exact output, source files, and research records used. A rebuilt PDF may differ byte for byte because of PDF metadata, timestamps, or TeX versions; hashes identify files, not proof correctness.

The build was checked for unresolved references/citations, duplicated labels, and overfull boxes. All pages were rendered and visually inspected, with separate full-page inspection of the title, principal formulas, and tables. The temporary PNGs and build intermediates are not repository deliverables. To render a local review copy with Poppler:

    pdftoppm -r 120 -png manuscript.pdf /tmp/ym-manuscript-page

No numerical program was changed or rerun for this editorial consolidation. The existing [numerics index](numerics/README.md) gives reproduction commands and explains which controls use prescribed weights and which experiment samples the interacting Wilson action. The [consolidation audit](reviews/MANUSCRIPT_CONSOLIDATION_AUDIT_20260925.md) records the scientific scope, editorial correction, and verification limits. The [draft history](DRAFT_HISTOR.md) points to this live milestone without creating a snapshot directory.

The parent PACKAGE_RECORD.json has only its YM inventory and standalone-manuscript entry updated for this deliverable. It already had 92 inventory discrepancies outside YM before this consolidation; those unrelated entries are preserved, so the parent package-wide check still reports them. This does not prevent a clean standalone manuscript build or validation of its own fingerprints.
