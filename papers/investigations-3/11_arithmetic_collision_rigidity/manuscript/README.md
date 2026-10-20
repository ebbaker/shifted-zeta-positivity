# Positive Arithmetic Packets for the Theta Heat Flow

Updated 19 October 2026, America/New_York. Drafted for Edward Baker with
substantial LLM assistance. Current analytic integration and extensions:
**gpt-6-astra, actual effort max**. Earlier contributions retain their
recorded configurations in the acknowledgements and build history.

The [canonical LaTeX project](positive_arithmetic_packets/main.tex) is a
**52-page working draft with thirteen sections and fourteen TeX files**.
Sections 1–10 retain their preceding source bytes. Section 11 distinguishes
uniform slab coverage from the later small UAR-05 island. Section 12
summarizes S01–S07 and GEO-T1 with links to detailed notes. New
[Section 13](positive_arithmetic_packets/sections/13_uniform_coherent_edge.tex)
emphasizes UAR-03's coherent analytic edge construction and summable cutoff
transitions, UAR-04's complete residual bound, and two new analytic extensions.

The explicit extension gives a residual bound between arbitrary endpoints
inside the original sector, with the decaying envelope evaluated at their
lower height. The qualitative extension proves edge-error and transition
bounds on any fixed compact positive band of t log(x/(4 pi)), for sufficiently
small t. Its new constants and onset have not been numerically fixed. Full
proofs are in [S03 Note 13](../symmetries/03_normalized_jet_rotation/notes/13_REBASED_RESIDUAL_AND_COMPACT_SECTOR_EDGE_EXTENSIONS_20261019.md);
the manuscript gives statements and proof outlines.

Uniform coverage remains E>0 on [1/100,1/5] x [-1001,1001], and on
epsilon<=t<=1/2, |x|>=exp(20/epsilon). UAR-05 adds its precisely stated small
closed box near t=.05, x=4 pi exp(20)+1; UAR-06's matched direct consumer is
stronger there at the same dominant acquisition cost. The intervening
bridge and required complex exterior remain open. The two new analytic
extensions supply no further physical exclusion or Newman bound.

- [Local reading-copy PDF](../../../../output/pdf/positive_arithmetic_packets.pdf), generated in the ignored root output folder.
- [Source and build record](positive_arithmetic_packets/BUILD_RECORD.json), preserving the preceding record.
- [Current integration review 18](../reviews/18_UAR_ANALYTIC_MANUSCRIPT_AND_GENERALIZATION_REVIEW_20261019.md) and [verification receipt](../numerics/UAR_ANALYTIC_MANUSCRIPT_INTEGRATION_20261019.json).
- [Post-UAR accomplishments review 17](../reviews/17_ACCOMPLISHMENTS_AND_POST_UAR_RESEARCH_PRIORITIES_REVIEW_ASTRA_20261019.md), with its source-version-specific assessment.
- [Uniform residual program](../symmetries/research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md), [progress register](../symmetries/research-progress/02_UNIFORM_ARITHMETIC_RESIDUAL_PROGRESS_20261019.md) and [completed-round summary](../symmetries/summary/02_UNIFORM_ARITHMETIC_RESIDUAL_ROUND_SUMMARY_20261019.md).
- [Preceding integration review 16](../reviews/16_SYMMETRY_PROGRAM_AND_MANUSCRIPT_INTEGRATION_REVIEW_20261019.md) and [18 October review 13](../reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md), retaining their original source-version scope.
- [Draft history](../DRAFT_HISTORY.md), recording milestones without new snapshot folders.

The manuscript's document links are local file links relative to the reading
copy in `output/pdf/`. Keep that location when following them. The source
identifies every target in `symmetries/`.

Open the project in the built-in LaTeX editor for editable source and a live
preview. A terminal rebuild uses an external directory; run until references
stabilize from `manuscript/positive_arithmetic_packets`:

```sh
mkdir -p /tmp/positive-arithmetic-packets-build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
```

The terminal build passes without warnings; all 52 pages were rendered and
inspected, with pages 47–52 also reviewed at page scale. Fresh 192/256-bit
UAR-03, UAR-04 and UAR-06 replays pass, including the latter's source-own
controls. The new arbitrary-endpoint checker passes at both precisions.
The build record records the desktop compiler result. Scalar replays
support constants and bookkeeping; the written arguments supply uniformity.
The new derivations have internal self-review, not independent specialist review.
