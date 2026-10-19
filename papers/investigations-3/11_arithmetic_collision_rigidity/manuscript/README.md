# Positive Arithmetic Packets for the Theta Heat Flow

Updated 19 October 2026, America/New_York. Drafted for Edward Baker with
substantial LLM assistance. Current synthesis and manuscript integration:
**gpt-6-astra, actual effort max**. Earlier contributions retain their
recorded configurations in the acknowledgements and build history.

The [canonical LaTeX project](positive_arithmetic_packets/main.tex) is a
**48-page working draft with twelve sections and thirteen TeX files**.
The original eleven analytic sections retain the complete overview 02
proofs and certificates. New [Section 12](positive_arithmetic_packets/sections/12_symmetry_findings.tex)
summarizes the current symmetry findings with links to detailed notes:
S03's complete arithmetic residual estimate, S04's uniform averaging and
local transfer, the numerical comparisons, and the scoped geometric limits.

The manuscript develops positive arithmetic carriers and the E/64 payment,
preserves complete modular cancellation before truncation, proves effective
tail estimates, states the full finite error contract and derives finite
noncollision and the explicit real exterior from their named inputs.
The symmetry section summarizes separately proved research-note results;
it does not replace their full proofs.

Coverage remains E>0 on [1/100,1/5] x [-1001,1001], and on
epsilon<=t<=1/2, |x|>=exp(20/epsilon). The bridge
**1001<|x|<exp(2000)** and required complex exterior remain open.
The new summary supplies no additional coverage or Newman bound.

- [Local reading-copy PDF](../../../../output/pdf/positive_arithmetic_packets.pdf), generated in the ignored root output folder.
- [Source and build record](positive_arithmetic_packets/BUILD_RECORD.json), with the preceding build record preserved.
- [Current integration review](../reviews/16_SYMMETRY_PROGRAM_AND_MANUSCRIPT_INTEGRATION_REVIEW_20261019.md) and [verification receipt](../numerics/SYMMETRY_PROGRAM_MANUSCRIPT_INTEGRATION_20261019.json).
- [Research accomplishments review](../reviews/15_MANUSCRIPT_AND_SYMMETRY_ACCOMPLISHMENTS_REVIEW_ASTRA_20261019.md) and its [selective fresh numerical replays](../numerics/MANUSCRIPT_SYMMETRY_REVIEW_REPLAY_20261019.json).
- [New research program](../symmetries/research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md) and [progress register](../symmetries/research-progress/02_UNIFORM_ARITHMETIC_RESIDUAL_PROGRESS_20261019.md); new mathematical work has not begun.
- [18 October integration review](../reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md) and [numerical replay](../numerics/MANUSCRIPT_INTEGRATION_REPLAY_20261018.json), retaining their original source-version scope.
- [Draft history](../DRAFT_HISTORY.md), recording milestones without new snapshot folders.

The document links in Section 12 are local file links relative to the reading
copy in `output/pdf/`. Keep that location when following them. The Markdown
summary and manuscript source also identify every target in `symmetries/`.

Open the project in the built-in LaTeX editor for editable source and a live
preview. A terminal rebuild uses an external directory; run until references
stabilize from `manuscript/positive_arithmetic_packets`:

```sh
mkdir -p /tmp/positive-arithmetic-packets-build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
```

The current terminal and desktop builds pass; all 48 pages were rendered and
inspected. The existing eleven analytic sections and selected numerical
inputs match their preceding hashes. Their mathematical certificates were
not rerun merely for the summary addition. Compilation is a document check;
no independent implementation or specialist review is claimed.
