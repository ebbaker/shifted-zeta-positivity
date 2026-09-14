# The margin in the shifted screw-function criterion ("Paper 1")

Working draft of *The margin in the shifted screw-function criterion for zero-free half-planes*,
with its shorter companion *Quantitative asymptotics for Suzuki's shifted screw functions*. See
`STATUS.md` for stage, verification record, redaction record, and what blocks release.
**This is not a released manuscript**; cite nothing from this folder without checking `STATUS.md`.

## What the paper does

Suzuki (JLMS 108 (2023), §11) attached to ζ a shifted family Ψ_ω and proved that ζ has no zeros
with Re s > ½+ω iff Ψ_ω(t) ≥ 0 eventually. This paper makes that criterion quantitative: an exact
decomposition `Ψ_ω(t) = (ξ′/ξ)(½+ω) t + (ξ′/ξ)′(½+ω) + R_ω(t)` with an explicit, exponentially
damped remainder, giving (i) a linear **margin** whose slope vanishes at ω = 0 precisely because
(ξ′/ξ)(½) = 0 — the mechanism of RH's marginality; (ii) an explicit onset threshold; (iii) a
sharp **phase transition** at ω_c = Θ−½ (RH ⟺ it is continuous); (iv) exponential sensitivity to
violating zeros; (v) an unconditional positivity **window** from verified zeros plus zero-free
regions, with endpoint law t₊ ≈ 0.72(½−ω)⁻²; and (vi) the same theory for real primitive Dirichlet
L-functions, where the margin grows with the conductor and the criterion is provably blind to
Siegel zeros. The reformulation transports the zero-free-half-plane problem faithfully; it does
not claim to reduce it.

## Contents

| File | What it is |
|---|---|
| `psi_omega_margin.tex` | LaTeX source, full version (21 pp.; fold-in of 27 Aug 2026) |
| `psi_omega_margin.pdf` | Compiled full version (pdflatex, TeX Live) |
| `psi_omega_concise.tex` | LaTeX source, concise companion, "Quantitative asymptotics for Suzuki's shifted screw functions" (9 pp.) |
| `psi_omega_concise.pdf` | Compiled concise companion |
| `code/` | Verification scripts `c1`–`c8` (mpmath + numpy), a README mapping each to a paper result, and `requirements.txt` |
| `supplementary/DERIVATION_AND_VERIFICATION.md` | Where each result comes from, how it was checked, and the two corrections made during the recheck |
| `supplementary/NEXT_STEPS.md` | The four next-step investigations (window / Dirichlet / phase transition / priority), now folded in, plus what remains before a submission-ready draft |

## Which version to read

The **concise** version is the intended submission: the core decomposition, margin, threshold,
critical-shift dichotomy, sensitivity, and one-sided consequences, ~9 pp. The **full** version
adds the discursive introduction, the unconditional window with the zero-free-region endpoint law,
the Dirichlet/Selberg-class section, and all numerical tables. Companion Paper 2
(`../omega-string`) currently cites the concise version.

## To rebuild

```
pdflatex psi_omega_margin.tex   && pdflatex psi_omega_margin.tex      # twice, for the ToC/refs
pdflatex psi_omega_concise.tex  && pdflatex psi_omega_concise.tex
```

Both are self-contained (bibliography is inline `thebibliography`; no `.bib`, no external style).
To re-run the numerics, see `code/README.md`.

## Status and provenance

Working draft; author block filled (Edward B. Baker III) but no ORCID yet; no external human review; not covered by any release or DOI.
Developed August 2026 with substantial language-model assistance under the author's direction,
across referee-style rounds 12–14 with independent numerical recomputation at each. Full record in
`STATUS.md`.

[Shifted-zeta program](../README.md) · [All manuscripts](../../README.md)
