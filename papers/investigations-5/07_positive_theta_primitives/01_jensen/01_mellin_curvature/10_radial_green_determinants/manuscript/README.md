# Boundary-preserving comparisons for theta Toeplitz determinants

First consolidated working draft, 4 November 2026. Intended author: **Edward Baker**.
Substantial LLM assistance; consolidation **gpt-6-astra / ultra**, chat0007,
task **RGD-E01 r3** (E — execution; recommended Sol; actual current session retained).

The paper consolidates finite certificates, exact comparison identities,
positive reference constructions and precisely scoped growing-dimension
limitations. It proves no new canonical positivity range and no RH conclusion.
The pair-reference/diagonal-control section incorporates the completed
Sol E04 r7 assessment: twelve obligations accepted within scope without
mathematical correction. This is internal LLM review with shared premises,
not independent specialist review.

- [Canonical TeX source](radial_green_determinants.tex)
- [Claim-to-source map](CLAIM_MAP.md)
- [Input versions](INPUT_SOURCES.json)
- [Build record](BUILD_RECORD.json)
- [Milestone history](../DRAFT_HISTORY.md)

## Build

Run `python3 build.py` from this directory using a TeX installation with
`latexmk`, `pdflatex` and BibTeX. The script locates the repository root and
builds the reading copy at `output/pdf/radial-green-determinants/radial_green_determinants.pdf`.
The PDF and TeX intermediates are generated and ignored; they do not belong
in this manuscript directory. The small build record retains source and PDF
hashes, and flags overfull boxes or unresolved citations/references.
Visual inspection is recorded in the integration check, not inferred from compilation.

This is one canonical editable draft. No snapshot folder, commit, tag,
submission or publication is created by consolidation. Frozen assessment
packets and numerical records are unchanged.
