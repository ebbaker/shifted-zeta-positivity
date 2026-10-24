# Heat contour research manuscripts

23 October 2026. Drafted for **Edward Baker** with substantial LLM assistance. Current book revision: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

The maintained [book.tex](book.tex), *Conserved heat contours toward simple zeta zeros*, now centers the RH-conditional fixed-offset Gaussian comparison and the actual contours preserving H dz. It includes the full proof, an all-multiple positive-source control, and the exact collision balance linking the acquired wall to the unresolved simplicity estimate. The overarching goal is **RH implies simple zeros**; no new simplicity proportion is claimed. The [revision note](../brainstorm/notes/20_THEOREM_CENTERED_BOOK_REVISION_20261023.md) explains the selection, and the [internal review](../brainstorm/reviews/10_THEOREM_CENTERED_BOOK_REVIEW_20261023.md) records checks and limits.

The acquired zero-free wall removes the upper and lower transition flux. Earlier nonreal population and horizontal-end inward flux remain to be bounded. The manuscript distinguishes the material velocity H_z/H from the root velocity H_zz/H_z and retains complete source errors and the ordered field limits.

## Retained book drafts

At the author's explicit request, substantial book rewrites may now retain dated standalone TeX drafts **in addition to Git history**. This is a book-specific change to the earlier no-draft practice; it does not create snapshot folders or change the handling of other investigations.

| Version | File | Role |
| --- | --- | --- |
| Before the contour theorem rewrite | [book_draft_20261023_01_relative_flux.tex](book_draft_20261023_01_relative_flux.tex) | Exact prior book, *Heat collisions and relative zero flux*, retaining the longer reference/source-ordering budgets |
| Fixed-offset theorem rewrite | [book_draft_20261023_02_fixed_offset.tex](book_draft_20261023_02_fixed_offset.tex) | Exact copy of the reviewed current book at this milestone |
| Maintained source | [book.tex](book.tex) | Continue editing here; retain a new dated draft for a later substantial rewrite |

The [build receipt](BOOK_CONTOUR_BUILD_RECORD_20261023.json) records hashes for all three sources and the reading copy. The final build has **15 pages**, with no unresolved references or box warnings; all pages were visually checked. No commit or tag was created in this revision. Milestones are indexed in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md).

## Reading copy and rebuild

Open book.tex in the desktop LaTeX editor and select it as the main document for the book. The directory also contains main.tex and standalone dated drafts, so automatic main-file discovery may otherwise be ambiguous.

Generated PDFs belong in repository-root `output/pdf/height-dependent-heat-contours/`, ignored by Git. The current reading copy is [book.pdf](../../../../output/pdf/height-dependent-heat-contours/book.pdf). From this manuscript directory, rebuild it with:

```sh
mkdir -p /tmp/hdc-book-build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/hdc-book-build book.tex
mkdir -p ../../../../output/pdf/height-dependent-heat-contours
cp /tmp/hdc-book-build/book.pdf ../../../../output/pdf/height-dependent-heat-contours/book.pdf
```

Intermediate build files and PDFs are not manuscript sources. PDF metadata may vary across builds. The older [BOOK_BUILD_RECORD_20261023.json](BOOK_BUILD_RECORD_20261023.json) remains the historical receipt for the earlier book.

## Broader working draft

The [working research draft](main.tex) retains the spectral, coefficient, contour and numerical background, including the provisional [conserved spatial contour section](conserved_contours.tex). It was not edited during the theorem-centered book rewrite. Its latest recorded build has 27 pages; the [conservation review](../brainstorm/reviews/08_CONSERVED_CONTOURS_MANUSCRIPT_REVIEW_20261023.md) and [build record](CONSERVATION_BUILD_RECORD_20261023.json) describe that version. Use the same rebuild commands with main.tex and main.pdf to regenerate its reading copy.

Current analytical work is tracked in the [SCF overview](../brainstorm/research-overview/03_CONSERVED_SPATIAL_CONTOURS_ANALYTIC_PROGRAM_20261023.md) and [progress register](../brainstorm/research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md). [Continuation 19](../brainstorm/notes/19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md) and the new revision note identify the remaining arithmetic obligation. Numerics support analytical questions; document compilation does not validate a mathematical proof.
