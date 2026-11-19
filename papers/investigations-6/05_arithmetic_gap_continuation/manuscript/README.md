# Analytical manuscript

19 November 2026, America/New_York. Drafted for **Edward Baker**, named as
author, with OpenAI Codex LLM assistance. Founding lead recorded
**gpt-6-astra/max**; bounded derivation and assessment helpers explicitly
dispatched **gpt-6.1-sol/ultra**. Intended future continuation: **ultra**.
Dispatch metadata is not independent serving-backend attestation.

**Arithmetic residuals and backward gap continuation in the Newman heat
flow** is a 32-page self-contained analytical background and research-program
draft. The [PDF](../../../../output/pdf/arithmetic-gap-continuation/arithmetic_gap_continuation.pdf)
and its build products are in the repository-root ignored `output/` folder.
The editable entry point is [main.tex](main.tex); the bibliography has its
[own source and inspection guide](../references/README.md).

| Section | Development |
| --- | --- |
| 1. The source and physical time | Literal theta amplitude, normalization, heat equation, growth and divisor prerequisites |
| 2. Pair coordinates and the gap chain | Regular discriminant, complete exterior force, cumulative gaps, dipole response and logarithmic density |
| 3. Integer and complex hierarchies | Integer split-pole p,q equations, regular moments, separate complex Mellin exponent and its convergence/branch conditions |
| 4. Backward continuation | Signed cumulative drift, initial-only comparison, coupled V/K barrier and the localization already used by high-height acquisition |
| 5. The arithmetic source | Full Riemann–Siegel reference, exact arithmetic terms, published error inputs, Polymath strip criterion, Platt–Trudgian and Gomila |
| 6. Residual transport | Explicit heat defect, forced error equation, conditional propagation, joint contour quotient, center and correction payments |
| 7. Synthesis and challenges | Fixed-time normalization versus motion, common-contour comparison, collision controls and the remaining analytical dependencies |

The pair, chain, hierarchy and transfer formulas used by this program are
derived in the text. The parent manuscript retains ownership of the
broader common-time approximation and refinement results; specialized
proofs and primary-source error constants are cited at their point of use.
The [integration note](../notes/03_AGC_MANUSCRIPT_INTEGRATION_20261119.md)
records the precise scope. Numerics are supporting evidence and no new
numerical research campaign is part of this draft.

## Assessment and production

The [separate internal assessment](../reviews/01_AGC_ANALYTICAL_DRAFT_ASSESSMENT_20261119.md)
accepted the draft within its analytical-background, conditional-interface
and research-setup scope after one correction check. It shares inherited
source premises and is not independent specialist validation. The useful
canonical error estimate, any additional protected interval and global
coverage remain open. The Gomila package's reported status is attributed;
this work has not replayed its complete certificate.

All seven mathematical section files retain their accepted review hashes.
The subsequent changes to `main.tex` only enable URL wrapping and format
the bibliography. The final build has resolved citations and cross-references,
zero LaTeX warnings or overfull/underfull boxes, and all 32 pages were
visually inspected after rendering at 110 dpi. The
[production record](../numerics/02_AGC_MANUSCRIPT_BUILD_AND_SETUP_CHECK_20261119.json)
binds the sources and reading copy. These checks establish production and
document consistency, not a new mathematical result.

From the repository root, rebuild with:

```sh
sh papers/investigations-6/05_arithmetic_gap_continuation/manuscript/build.sh
```

The script requires a LaTeX installation with `latexmk`, `pdflatex` and
BibTeX. It resolves the local bibliography and directs all generated
files to `output/pdf/arithmetic-gap-continuation/`. No manuscript snapshot
folder is created. The [continuation prompt](../notes/01_AGC_CONTINUATION_AND_PROMPT_20261119.md)
and [sole progress register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
identify the first unactivated analytical research task.
