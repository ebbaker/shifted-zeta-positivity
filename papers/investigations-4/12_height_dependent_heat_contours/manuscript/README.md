# Complex zero-field book and retained heat manuscripts

24 October 2026. Drafted for **Edward Baker** with substantial LLM assistance. Original complex-field book revision: **gpt-6-astra (Codex), actual reasoning effort max**. Complex-current notation revision: **gpt-6.1-sol (Codex), actual reasoning effort xhigh**. Complex-potential presentation revision: **gpt-6-astra (Codex), actual reasoning effort max**.

The maintained [book.tex](book.tex), *Complex zero fields and conserved heat evolution*, centers on the smooth complex zero field, its density and phase, complex-potential/DS-II evolution, analytic conservation laws, normalization and multiplicity observables. Wirtinger derivatives and W=2 partial_z^2 log D now lead the setup and field theorem; the equivalent real Schrödinger–Poisson equation retains its `eq:SP` label. [Note 20](../notes/20_COMPLEX_POTENTIAL_AND_WIRTINGER_FORMULATION_20261024.md) and [Review 18](../reviews/18_COMPLEX_POTENTIAL_PRESENTATION_REVIEW_20261024.md) record this author-requested presentation revision. The author explicitly requested this rewrite and preservation of the preceding book as a new dated draft. The full derivations are in the book; [Note 23](../brainstorm/notes/23_COMPLEX_FIELD_BOOK_AND_CONSERVATION_LAWS_20261024.md) records the selection and new calculations, and [Self-review 13](../brainstorm/reviews/13_COMPLEX_FIELD_BOOK_SELF_REVIEW_20261024.md) records the same-assistant audit.

With the specified potential and integrability, the conserved quantities are mass, two momenta, a Hamiltonian, and explicit first-moment/virial combinations. The holomorphic lift has additional weighted target laws. The global mass is the degree for polynomials and infinite for transcendental entire functions, including theta. Polynomial fields have zero momenta and zero Hamiltonian even through collisions. The multiplicity observable is not conserved; its analytic transport and resolution errors are retained. No new theta-specific upper bound or simplicity result is claimed.

## Retained book drafts

The three existing dated standalone TeX drafts are collected in [drafts/](drafts/README.md) at the author's request. This organization pass creates no additional manuscript version.

| Version | File | Role |
| --- | --- | --- |
| Earlier relative-flux book | [Draft 01](drafts/book_draft_20261023_01_relative_flux.tex) | Preserved earlier exposition and complete reference/source budgets |
| Fixed-offset theorem checkpoint | [Draft 02](drafts/book_draft_20261023_02_fixed_offset.tex) | Exact source at the 23 October theorem-centered milestone |
| Immediately before the complex-field rewrite | [Draft 03](drafts/book_draft_20261024_03_conserved_contours.tex) | Byte-identical copy of the current contour-centered book before this rewrite; use for its theorem and section numbers |
| Maintained complex-field book | [book.tex](book.tex) | Continue editing this source |

The [relocation receipt](drafts/DRAFT_RELOCATION_20261024.json) maps the historical paths to the new folder and records byte identity and documentation-link changes. Drafts 02 and 03 have identical contents and distinct milestone provenance. [Continuation 24](../brainstorm/notes/24_CONTINUATION_COMPLEX_ZERO_FIELD_20261024.md) gives the next analytic pass.

The [preservation receipt](BOOK_PRE_FIELD_DRAFT_RECEIPT_20261024.json) verifies draft 03. The [current build receipt](BOOK_COMPLEX_POTENTIAL_BUILD_RECORD_20261024.json) identifies the revised source and reading copy, with fourteen exact algebra checks of the complex equations, proof identities, current, cutoff and residual conventions. The [preceding complex-current receipt](BOOK_COMPLEX_CURRENT_BUILD_RECORD_20261024.json) and [original field receipt](BOOK_COMPLEX_FIELD_BUILD_RECORD_20261024.json) retain earlier build provenance. The current book has **16 pages**, no unresolved references or box warnings, and all pages received visual inspection. Mathematical review is same-assistant only. No new manuscript snapshot, commit or tag was created. [Milestone history](../DRAFT_HISTORY.md).

## Reading copy and rebuild

The current [reading copy](../../../../output/pdf/height-dependent-heat-contours/book.pdf) is generated outside the manuscript folder in the repository's ignored PDF output directory. Open book.tex in the desktop LaTeX editor and select it as the main document; this folder also contains main.tex, while the preserved standalone drafts are in drafts/.

From this manuscript directory:

```sh
mkdir -p /tmp/hdc-book-build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/hdc-book-build book.tex
mkdir -p ../../../../output/pdf/height-dependent-heat-contours
cp /tmp/hdc-book-build/book.pdf ../../../../output/pdf/height-dependent-heat-contours/book.pdf
```

The earlier [contour build receipt](BOOK_CONTOUR_BUILD_RECORD_20261023.json) and [relative-flux receipt](BOOK_BUILD_RECORD_20261023.json) remain historical records. They do not identify the current reading copy. Compilation checks typesetting, not the validity of a proof.

## Retained broader working draft

24 October 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), ultra**.

The [working research draft](main.tex) retains the spectral, coefficient, contour and numerical background. At the author's explicit request, it now includes the complete [near-axis cluster comparison](near_axis_cluster.tex), its Gaussian polynomial lemma and full-tail proof, the scoped curvature-omission control, and the all-multiple positive-source control. Section 9 distinguishes the initial cluster from a complete transported population; its error is measured against the absolute Gaussian model integral, with no model floor or new simplicity conclusion. The missing nonvanishing condition in the coefficient comparison and the stale fixed-offset status prose were corrected.

The current [reading copy](../../../../output/pdf/height-dependent-heat-contours/main.pdf) has **35 pages**, with no unresolved references, citation warnings or box warnings. All pages received visual checks; the new section received separate same-model proof review. See [Review 17](../reviews/17_MAIN_NEAR_AXIS_INTEGRATION_REVIEW_20261024.md) and the [build receipt](NEAR_AXIS_BUILD_RECORD_20261024.json). The [27-page conservation build](CONSERVATION_BUILD_RECORD_20261023.json) remains a historical record. Use the same rebuild commands with main.tex and main.pdf. The book and retained standalone book drafts were unchanged; no Git commit or tag was made.

The contour program is tracked in the [SCF overview](../brainstorm/research-overview/03_CONSERVED_SPATIAL_CONTOURS_ANALYTIC_PROGRAM_20261023.md) and [progress register](../brainstorm/research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md). [Continuation 19](../brainstorm/notes/19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md) and the new revision note identify the remaining arithmetic obligation. Numerics support analytical questions; document compilation does not validate a mathematical proof.
