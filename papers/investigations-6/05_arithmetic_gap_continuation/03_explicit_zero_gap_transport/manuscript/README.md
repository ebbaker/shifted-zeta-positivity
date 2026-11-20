# Explicit zero locations in the Newman heat flow

Working manuscript prepared for Edward Baker with OpenAI Codex assistance, 20 November 2026. The opening draft recorded gpt-6.2-astra/max. The desktop chat records gpt-6.2-astra/ultra for this revision.

[Read the manuscript](../../../../../output/pdf/explicit-zero-gap-transport/explicit_zero_gap_transport.pdf) · [Editable LaTeX](main.tex) · [Reference passages and provenance](../references/README.md) · [Build and checks](../numerics/05_ZERO_LOCATIONS_MANUSCRIPT_BUILD_20261120.json)

| Section | Question | Source |
| --- | --- | --- |
| 1 | What constitutes a counted position at one time, and which errors matter for a gap? | [Field and notation](main.tex) |
| 2 | Which roots do the residue, inverse and full-product formulas locate? What finite error can each one certify? | [Formulas and error estimates](anchors.tex) · [One-time truncation check](position_check.tex) |
| 3 | Where can the estimates be compared with Polymath and Platt–Trudgian? | [Published comparisons](comparison.tex) |
| 4 | How do counted positions and the unlocated exterior determine \(S_{k,p,q}\), then \(D_k'\)? | [Mixed hierarchy](exterior.tex) |
| 5 | What position, count and time estimates are still needed? | [Continuation](frontier.tex) |
| A–C | How much of the high-time gap motion can the phase current explain, and what limits its use? | [Phase and its domain](current.tex) · [Large-time transport and direct product evolution](transport.tex) · [Finite comparison](finite.tex) |

The [founding contour calculation](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) and [full-product recovery](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) supply the position formulas. The [mixed-moment derivation](../notes/09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md) and its [internal assessment](../reviews/04_EZ_MIXED_MOMENT_ANCHOR_ASSESSMENT_20261120.md) give the signed anchor estimate. The [research handoff](../notes/10_EZ_ZERO_LOCATIONS_CONTINUATION_20261120.md) identifies the first open position comparison.

Run the following command from this directory with Python 3, latexmk, pdfLaTeX and BibTeX installed.

~~~sh
python3 build.py
~~~

The [builder](build.py) uses the branch and parent bibliographies and replaces the reading copy on success. The [original production record](../numerics/02_DRAFT_BUILD_AND_CHECK_20261120.json) identifies the opening draft. The [finite arithmetic records](../numerics/README.md) document the numerical checks separately. [Large-file policy](../../../../../LARGE_FILES.md)
