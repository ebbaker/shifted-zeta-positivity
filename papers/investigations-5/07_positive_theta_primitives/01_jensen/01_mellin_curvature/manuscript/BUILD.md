# Signed Mellin curvature background manuscript

2 November 2026, America/New_York. Drafted for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6-astra (Codex)**, effort **max**.

The editable manuscript is [main.tex](main.tex). It explains the source,
coefficient/Jensen destination, signed-average baseline, curvature and
factorial comparison, eight physical subinvestigations, and the remaining
localization and arbitrary-order obligations. This is exposition of the
existing research; the Gaussian curvature bound remains unproved.

Run from this directory with a current TeX installation containing
`latexmk`, pdfLaTeX, BibTeX, Python 3, `plainurl.bst`, and the standard packages in the preamble:

```sh
sh build.sh
```

The PDF and auxiliary build files go to the repository-root ignored
`output/pdf/mellin-curvature/` folder. To build elsewhere, pass an output
directory as the first argument. The PDF is named
`signed_mellin_curvature_background.pdf`.

The bibliography reads the existing canonical
[shared sources.bib](../../../references/sources.bib). The build creates a disposable print bibliography beside the PDF, omitting
research-inspection notes while preserving citation metadata and links. No
duplicate canonical bibliography or third-party PDF is stored here. Mathematical-source and
version details are in [Integration10](../notes/10_BACKGROUND_MANUSCRIPT_INTEGRATION_20261102.md);
the manuscript's own check is [Review02](../reviews/02_BACKGROUND_MANUSCRIPT_SELF_CHECK_20261102.md).
The small [build record](BUILD_RECORD.json) identifies this draft's inputs
and reading-copy hash; hashes establish artifact identity, not mathematical validity.

Keep one evolving manuscript source. Milestones belong in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md), with future version milestones
pointing to commits or tags. Do not create manuscript snapshot folders
or commit generated working PDFs.
