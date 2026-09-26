# Building the YM manuscript

26 September 2026. Drafted for Edward Baker with substantial LLM assistance. Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.

The maintained manuscript is [manuscript.tex](manuscript.tex), with its [preamble](preamble.tex), [sections](sections/), and [references](references.tex). The readable deliverable is [manuscript.pdf](manuscript.pdf). This live draft includes the continuation after the review exchange, resumed at the author's request. It is maintained in place, without dated snapshot folders.

From this YM directory, with a standard TeX Live installation providing latexmk and pdflatex:

    LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
    cp build/manuscript.pdf manuscript.pdf

The source uses standard LaTeX mathematics, Latin Modern fonts, microtype, hyperref, and table packages. No shell escape, external dataset, bibliography service, or network access is needed to build it. The bibliography is supplied as LaTeX in references.tex.

The exact current tool versions and page count are in BUILD_RECORD.json. The resulting PDF remains below the repository's approximately 1 MB per-file target. BUILD_RECORD.json identifies the exact output, source files, and research records used. A rebuilt PDF may differ byte for byte because of PDF metadata, timestamps, or TeX versions; hashes identify files, not proof correctness.

The 26 September continuation adds full-electric point-source and strict-half-slab preparation obstructions, with their actual positive pairings, source domains and a [substantive self-audit](reviews/FULL_ELECTRIC_AND_BUFFERED_SOURCE_AUDIT_20260926.md). These analytical results use no numerical input. Existing uncommitted research and numerical records are preserved; the earlier diagnostic controls were not needlessly rerun.

The build was checked for unresolved references/citations, duplicated labels, and overfull boxes. All pages were rendered and visually inspected, with separate full-page inspection of the title, principal formulas, and tables. The temporary PNGs and build intermediates are not repository deliverables. To render a local review copy with Poppler:

    pdftoppm -r 120 -png manuscript.pdf /tmp/ym-manuscript-page

For the continuation, the zero-list checker's certification labels and NumPy compatibility were corrected and all 30 floating controls replayed into a separate record. A new standard-library exact-rational control verifies the analytic post-6063 remainder bound; the full floating comparison remains diagnostic. The existing [numerics index](numerics/README.md) gives reproduction commands and explains which controls use prescribed weights and which experiment samples the interacting Wilson action. The [consolidation audit](reviews/MANUSCRIPT_CONSOLIDATION_AUDIT_20260925.md) records the scientific scope, editorial correction, and verification limits. The [draft history](DRAFT_HISTOR.md) points to this live milestone without creating a snapshot directory.

The parent PACKAGE_RECORD.json is a historical package inventory, not refreshed by this continuation. The earlier consolidation recorded 92 discrepancies outside YM. Unrelated entries are preserved; BUILD_RECORD.json is the current standalone YM fingerprint record.
