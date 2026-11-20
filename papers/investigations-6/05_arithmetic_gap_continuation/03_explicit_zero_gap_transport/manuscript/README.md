# Explicit zero locations in the Newman heat flow

**Counted positions, high ranks, and backward gap curvature.** Analytical working manuscript drafted for Edward Baker, 20 November 2026, with OpenAI Codex assistance. The opening manuscript recorded gpt-6.2-astra/max. The current revision records gpt-6.2-astra/ultra and gpt-6.2-sol/ultra. The project assessments are internal.

[Read the PDF](../../../../../output/pdf/explicit-zero-gap-transport/explicit_zero_gap_transport.pdf) · [Editable manuscript](main.tex) · [Build record](../numerics/06_INTEGRATED_MANUSCRIPT_BUILD_20261120.json) · [Sources and passage provenance](../references/README.md)

| Section | Development | Source |
| --- | --- | --- |
| 1 | Physical field and time, positive rank, and squared half-gap | [Field and notation](main.tex) |
| 2 | Contour displacement, one inverse for consecutive positions, growing count, and the error after differencing | [Contour and inverse](anchors.tex) · [Growing window and finite input bounds](window.tex) |
| 3 | High ranks at fixed positive all-real time, sufficient moment budgets, circle counts, and absolute calibration of Polymath's clock at one-half | [Fixed-time reconstruction and clock proof](comparison.tex) · [Individual factor reconstruction](factors.tex) |
| 4 | Exact gap velocity, complete exterior traces, and the signed residual after lattice cancellation | [Exterior interaction and full product evolution](exterior.tex) |
| 5 | A common time and space estimate at one upper anchor, its positive gap curvature, and the finite precision for initial data | [Backward curvature](curvature.tex) |
| 6 | A second derivation of gap velocity on a counted phase interval, its domain, and its mean-spacing correction | [Current](current.tex) · [Time-dependent estimates](transport.tex) |
| 7 | Supporting enclosures of individual positions and the first gap | [Position table](position_check.tex) · [Finite descent](finite.tex) |
| 8 | Effective overlap at one specified time, acquisition of moments and longer descent | [Outstanding challenges](frontier.tex) · [Research handoff](../notes/16_EZ_ASSESSED_ANCHOR_CONTINUATION_20261120.md) |

The research notes give the original statements, status and separate internal assessments. [Growing inverse](../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md) · [High-rank factors](../notes/12_EZ_FINITE_PRODUCT_AT_HIGH_RANK_20261120.md) · [Absolute clock rank](../notes/13_EZ_CLOCK_RANK_20261120.md) · [Direct moments](../notes/14_EZ_DIRECT_MOMENTS_AT_HIGH_RANK_20261120.md) · [Single-anchor curvature](../notes/15_EZ_SINGLE_ANCHOR_GAP_CURVATURE_20261120.md)

Run the following command in this directory with Python 3, latexmk, pdfLaTeX and BibTeX installed.

~~~sh
python3 build.py
~~~

The [builder](build.py) replaces the reading copy in the ignored output directory on success. The [earlier production record](../numerics/05_ZERO_LOCATIONS_MANUSCRIPT_BUILD_20261120.json) identifies the preceding revision. [Numerical evidence](../numerics/README.md) · [Large-file policy](../../../../../LARGE_FILES.md)
