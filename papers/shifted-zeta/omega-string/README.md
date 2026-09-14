# The shifted zeta string ("Paper 2")

Working draft of *The shifted zeta string: an unconditional inverse-spectral family and its
RH endpoint* — see `STATUS.md` for stage, verification record, and what blocks release.
**This is not a released manuscript**; cite nothing from this folder without checking
`STATUS.md`.

## Contents

| File | What it is |
|---|---|
| `omega_string.tex` | LaTeX source, v5 (frozen 28 Aug 2026) |
| `omega_string.pdf` | Compiled v5 (pdflatex, TeX Live; 13 pp.) |
| `fig_density.png` | Figure 1: the Poisson-smoothed zero spectral measure |
| `fig_density.py` | Generates `fig_density.png` (mpmath + numpy + matplotlib; ~2 min) |
| `v1_identities.py` | Verification, part 1: residue lemma (Lemma 3.1), Fourier block, constants (ξ′/ξ)(1), ρ_∞ |
| `v2_thmE_kasahara.py` | Verification, part 2: Thm 1.6(i)–(ii) convergence tables, the Kasahara dual-curve table (Rem 5.1), endpoint length L_ξ = B(0) (Rem 6.3) |

To rebuild: `python3 fig_density.py && pdflatex omega_string.tex` (twice). The verification
scripts are standalone; their expected outputs are quoted in the paper's Section 7 and in the
round records. The Herglotz-peeling reconstruction code (Section 7.1) is not yet in the
repository; see `STATUS.md`.

[Shifted-zeta program](../README.md) · [All manuscripts](../../README.md)
