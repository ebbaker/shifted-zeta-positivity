# Relative Discriminant Charges and Signed Source Response in Theta Heat Flow

21 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Actual manuscript session: **gpt-6-astra, reasoning effort ultra**.

[Read the manuscript](main.pdf) or edit [the LaTeX source](main.tex).
The 34-page manuscript is self-contained for the local analytic results;
the classical xi Fourier normalization and real-zero threshold theorem
are stated as external inputs with references. It consolidates the
finite-cluster charge, two-root cap theorem, explicit endpoint windows,
signed source response and event continuation, canonical-tail refinement,
finite-moment control, and many-root identities and counterexamples.
Existing numerical certificates are supporting evidence in Section 9.

The unchanged-theta signed margin, all-height signed coverage and
higher-multiplicity exclusion remain open. No endpoint-exclusion or
RH-conditional simplicity theorem is claimed. Review is internal to the
same model configuration, without independent specialist validation.

## Source organization

- `introduction.tex`: source normalization, RH context, charge interpretation.
- `foundations.tex`: cluster preparation, charge, two-root theorem and windows.
- `source.tex`: signed response, event continuation, moment control and theta tail.
- `many.tex`: full-cluster dynamics, cubic monotonicity and exact controls.
- `support.tex`: numerical support, outstanding obligations and acknowledgement.
- `appendix.tex`: holomorphic reference transfer and boundary interpolation.
- `references.tex`: public literature and linked supporting research records.

## Build and review

From this folder, with a standard LaTeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/bw12-manuscript-build main.tex
```

The rebuilt PDF is `/tmp/bw12-manuscript-build/main.pdf`. The saved
`main.pdf` is the reviewed delivery copy. Standard packages include
amsmath, amsthm, mathtools, lmodern, microtype, geometry and hyperref.
No Python dependency or numerical acquisition is needed to compile it.
The Codex built-in LaTeX editor also compiles the complete project.

The [integration review](../reviews/09_MANUSCRIPT_INTEGRATION_REVIEW_20261021.md)
records mathematical checks, link verification, compilation and page
inspection. The [progress register](../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md)
retains the existing research statuses, and [DRAFT_HISTORY](../DRAFT_HISTORY.md)
indexes this working-tree milestone. Numerical replay instructions remain
in the [numerics guide](../numerics/README.md). No snapshot folder or commit
was created.
