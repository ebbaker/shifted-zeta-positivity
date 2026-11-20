# Jacobi truncation and the motion of a counted zero pair

20 November 2026. Analytical working draft prepared for Edward Baker with OpenAI Codex assistance. The public record does not expose the lead configuration. Bounded drafting and internal review contributors were dispatched as gpt-6.2-sol/ultra.

[PDF reading copy](../../../../../output/pdf/jacobi-integer-hierarchy/jacobi_integer_hierarchy.pdf) · [Editable TeX](main.tex) · [Internal assessment](../reviews/05_AGC_JH_FIRST_MANUSCRIPT_ASSESSMENT_20261120.md) · [Build record](../numerics/07_AGC_JH_MANUSCRIPT_BUILD_20261120.json)

The draft starts with the physical theta tilt, derives the finite-head heat defect and its action on the full integer hierarchy, and follows the two-degree increment into the signed squared half-gap estimate. The compact-source parity theorem identifies a limit on degree monotonicity. The moving-Gram estimates justify uniform physical-time control. Section 8 contains the supporting canonical evidence on the single degree-24 chart. Section 9 states the open problems.

## Rebuild

With Python 3, pdfLaTeX, latexmk and the packages listed in the TeX preamble available, run the following from this directory.

```sh
python3 build.py
```

The [build helper](build.py) compiles in a temporary directory below the ignored PDF output folder and installs the finished reading copy there. Inputs are entirely local. The [large-file workflow](../../../../../LARGE_FILES.md) governs generated PDFs.

## Source map

- The [parent manuscript](../../manuscript/main.tex) supplies the physical normalization, the pair law, the integer hierarchy and the centered log identity. The draft uses the equation numbering of its [19 November PDF](../../../../../output/pdf/arithmetic-gap-continuation/arithmetic_gap_continuation.pdf).
- The [Volterra coefficient manuscript](../../../03_volterra_coefficient_dynamics/manuscript/main.tex) gives the complete quadrature error and Jacobi defect. The [exterior-moment manuscript](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/main.tex) develops the unforced hierarchy.
- The branch proofs and their hypotheses are in [the forced hierarchy](../notes/02_AGC_JH_FORCED_INTEGER_HIERARCHY_20261119.md), [degree and time compatibility](../notes/03_AGC_JH_DEGREE_TIME_INTERFACE_20261119.md), [the signed remainder](../notes/04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md) and [the parity obstruction](../notes/05_AGC_JH_PARITY_OSCILLATION_CONTROL_20261119.md).
- The [time-zero acquisition](../notes/07_AGC_JH_CANONICAL_SIGNED_CONTOUR_20261119.md) and [physical-time certificate](../notes/08_AGC_JH_PHYSICAL_TIME_SLAB_20261119.md) document the matched direct calculations. The [continuation](../notes/01_AGC_JH_CONTINUATION_AND_PROMPT_20261119.md) states the reduced-information question for the next degree step.
