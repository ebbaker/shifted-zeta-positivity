# A certified velocity-residual detector for off-axis zeros ("rh-detector")

Working draft of *A certified velocity-residual detector for off-axis zeros of the Riemann
Ξ-function, and the De Bruijn–Newman flow as a matrix pencil on Calogero–Moser space* — see
`STATUS.md` for stage, provenance, verification record, and what blocks release. **This is
not a released manuscript**; cite nothing from this folder without checking `STATUS.md`.

This manuscript is a separate thread from Papers 1–3 and the first-slab preprint (see the
program map in the repository `README.md`); it carries no companion cross-citations.

## Contents

| File | What it is |
|---|---|
| `rh_detector.tex` | LaTeX source, draft of 25 Aug 2026 (author block empty pending release) |
| `rh_detector.pdf` | Compiled draft (pdflatex, TeX Live; 10 pp.) |
| `code/h1_zeros1000.py` | Regenerates the 1001-ordinate zeta zero cache (`zeros1001.json`, shipped) |
| `code/h3_certified.py` | Table 1 (certified null test at K = 1000) and the §4.2 thresholds |
| `code/d1_synthetic.py` | Table 2 (synthetic injection tests: off-/on-axis recovery and model separation) |
| `code/v1_pencil.py` | §5.1 (pencil identity n = 2…7, rank-one relation, Λ benchmarks, k = 2 thresholds vs root tracking) |
| `code/d4_margin_meter.py` | Table 3 (local De Bruijn–Newman margins via the pencil) |
| `code/h4_beta.py` | §6 (Dirichlet beta null test; uses `beta_zeros.json`, shipped) |
| `code/zeros1001.json` | First 1001 zeta ordinates, 25 digits (regenerated 25 Aug; matches the pre-outage cache digit-for-digit) |
| `code/beta_zeros.json` | First 70 ordinates of the completed Dirichlet beta function |
| `code/README.md` | Which script backs which table/section, and run notes |
| `code/requirements.txt` | Pinned environment (mpmath, numpy, scipy) |

To rebuild the PDF: `pdflatex rh_detector.tex` (twice). Every number in the paper's tables
is printed by one of the scripts above; `code/README.md` maps them. All certificates are
rigorous modulo floating point — the interval-arithmetic port is a blocking item in
`STATUS.md`.
