# Heat contour research manuscripts

23 October 2026. Drafted for **Edward Baker** with substantial LLM assistance. Current selective version: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

The maintained [selective analytic manuscript](book.tex), *Heat collisions and relative zero flux*, develops the author's requested “from the book” direction around one argument: the exact nonreal balance, a boundary defined by a reference heat field, and arithmetic theta/xi estimates of its relative flux. The [selection note](../notes/18_RELATIVE_FLUX_AND_ANALYTIC_MANUSCRIPT_SELECTION_20261023.md) explains the theorem crosswalk and the [internal review](../reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md) records checks and limitations. “From the book” is the editorial objective; no optimal global arithmetic estimate is claimed.

The [first research draft](main.tex) and its five included section files preserve the broader spectral, coefficient, contour and numerical work. Its [original review](../reviews/14_MANUSCRIPT_AND_RESEARCH_RESET_REVIEW_20261023.md), [build record](BUILD_RECORD_20261023.json), and [research reset](../notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md) remain valid records of that version. The current revision does not alter those sources. Their prior expository update was prepared by **gpt-6.1-sol (Codex), effort xhigh**.

Generated PDFs belong in repository-root `output/pdf/height-dependent-heat-contours/`, ignored by Git. Open `book.tex` in the desktop LaTeX editor; when selecting a main file for this directory, choose `book.tex` for the selective paper or `main.tex` for the first research draft.

From this directory, rebuild the selective reading copy with:

```sh
mkdir -p /tmp/hdc-book-build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/hdc-book-build book.tex
mkdir -p ../../../../output/pdf/height-dependent-heat-contours
cp /tmp/hdc-book-build/book.pdf ../../../../output/pdf/height-dependent-heat-contours/book.pdf
```

The [selective build record](BOOK_BUILD_RECORD_20261023.json) stores hashes and validation. PDF metadata may vary across builds. Intermediate files and generated reading copies are not manuscript sources. Milestones are indexed in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md); no snapshot folder, Git commit or tag was created for this revision.

The finite balance and multiplicity constants are exact and sharp; the source-ordering estimate improves a named absolute comparator. Useful high-height size and earlier nonreal discrimination remain open. Neither version proves RH or a new global simplicity proportion.
