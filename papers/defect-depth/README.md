# Detection depth of spectral defects ("Paper 3")

Working draft of *Detection depth of spectral defects in shifted zeta strings* — see
`STATUS.md` for stage, verification record, and what blocks release. **This is not a released
manuscript**; cite nothing from this folder without checking `STATUS.md`.

## Contents

| File | What it is |
|---|---|
| `defect_depth.tex` | LaTeX source, v1 (29 Aug 2026) |
| `defect_depth.pdf` | Compiled v1 (pdflatex, TeX Live; 15 pp.; figures are placeholders) |
| `code/lab_ihara_core.py` | The Ihara laboratory core: graph constructors, exact charpolys (Faddeev–LeVerrier + Yun squarefree), Ihara/Bass zeta data, Weyl functions q, h_ω, q_ω, Ψ, Stieltjes-string round trips, Pick counts |
| `code/lab_ihara_experiments.py` | The laboratory record through round 5, concatenated; split on the `### FILE:` markers to re-run individually (validation, cubic census, Kesten–McKay universality, defect anatomy, ω-flow, covers, full Ihara structure, Hankel depth scans, real-ζ background, GM-pair search, W1 compactified depth law) |
| `code/README.md` | Which script backs which part of the paper, and run notes |
| `code/requirements.txt` | Pinned environment (mpmath, numpy) |

To rebuild the PDF: `pdflatex defect_depth.tex` (twice). The scripts print to stdout; their
expected outputs are the numbers quoted in the paper's tables and in the laboratory round
records (`LAB_ihara_round1`–`round5`, `ROUND6_closeout` in the project notes). The round-6
inline verification runs (time-normalization certificate, s₀ scan, unscaled real-ζ suite,
envelope bracketing) are not yet committed as standalone scripts — see `STATUS.md`, blocking
item 5.
