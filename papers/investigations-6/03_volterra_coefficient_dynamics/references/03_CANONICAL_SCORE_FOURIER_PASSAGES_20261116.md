# Complete-score Fourier comparison: checked sources

16 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Lead actual model/effort unavailable; E18 source checks dispatched gpt-6.1-sol/ultra, separately from backend attestation. Passage inspections, not full-paper reviews.

- **NIST DLMF §§25.2 and 25.4:** [Dirichlet series 25.2.1, continuation, Euler product 25.2.11](https://dlmf.nist.gov/25.2), [xi completion and reflection 25.4.3–4](https://dlmf.nist.gov/25.4). Checked 16 November 2026. Euler absolute estimates used only for Re s>1; no zero claim inside the critical strip. E18 derives its two-sided exterior bounds from these formulas.
- **NIST DLMF Gamma:** [no zeros §5.2(i)](https://dlmf.nist.gov/5.2#i), [recurrence 5.5.1](https://dlmf.nist.gov/5.5.E1), [sector Stirling 5.11.1, vertical magnitude 5.11.9 and remainder paragraph §5.11(ii)](https://dlmf.nist.gov/5.11). Checked by E18; lead checked the vertical formula and sector-error statement. Arguments stay in a fixed right-half-plane sector and their real parts in a compact interval, so the stated uniform vertical estimates apply. These classical formulas are not new arithmetic estimates.
- **NIST DLMF Euler summation:** [25.2.8](https://dlmf.nist.gov/25.2.E8), Re s>0, finite Dirichlet sum plus pole term and fractional-part integral. Lead inspected the formula and its domain on 16 November 2026. E19 generalizes the directly derived partial-summation calculation to the coefficients of zeta(s)/zeta(s+2); no universality or large-values theorem is imported.
- **Bernhard Riemann**, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, Monatsberichte der Berliner Akademie (November 1859), pp. 671–680. [Wilkins edition index](https://www.maths.tcd.ie/EMIS/classics/Riemann/index.html) confirms bibliography; inspected [English translation by David R. Wilkins, preliminary version December 1998](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf), printed pp.1–4 (PDF pp.2–5): Euler product, completed reflection, Fourier representation and exterior logarithmic product. Source normalization is converted explicitly in the VCD manuscript and E18. Direct download to `/private/tmp/szp-vcd-b05-references-20261116/Riemann1859-Wilkins.pdf` failed with DNS resolution error; web PDF passage inspection succeeded, no local byte/hash record is claimed.
- **Brad Rodgers and Terence Tao**, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5, 3 July 2021; Forum of Mathematics, Pi 8 (2020), e6, DOI [10.1017/fmp.2020.6](https://doi.org/10.1017/fmp.2020.6). E18 inspected authors' [v5 §1, equations (1)–(3) and following evenness](https://arxiv.org/pdf/1801.05914v5) as a normalization cross-check only; no theorem is imported here. Existing Rodgers–Tao investigation retains broader ownership. Direct download of this version to the same external temporary directory failed with DNS error; web inspection succeeded, no local copy/hash is claimed.

The new finite positive trigonometric-weight argument is proved directly, using prime factorization, elementary prime-reciprocal divergence and partial summation. It is a classical type of arithmetic weighting argument; no novelty claim is made for the method or zeta value-distribution facts. Only its stated canonical remainder/consumer conclusion is used here. All third-party PDFs remain outside the repository; none was stored successfully by the attempted direct downloads.

## Fixed-cluster discussion supplement, 16 November 2026, chat0004

For Edward Baker with Codex assistance; actual model/effort unavailable.
Rodgers–Tao v5 was rechecked for the backward-heat convention in §1,
equation (4), and §4's individual-zero dynamics, **PDF Theorem 11,
equation (56), printed p.27**. The experimental HTML labels the same
theorem 4.16. Its principal-value ODE is stated for Λ<t≤0 and the simple
real-zero regime used there; it is background, not an imported theorem
about passage through collisions or Jacobi degree truncation.

The existing external reading copy was reused and its identity verified:
`/Users/Shared/szp-archive/height-dependent-heat-contours/references/1801.05914v5.pdf`,
503405 bytes, SHA-256
`376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91`.
The earlier failed VCD downloads above remain historical failures.
The [Rodgers–Tao investigation's catalog](../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/references/README.md)
retains broader ownership. Online [v5 §4](https://arxiv.org/html/1801.05914v5#S4)
and the existing PDF passage were inspected; no full-paper verification
or new download is claimed. Manuscript §10.4 derives its local contour
moment and collision-resolution statements directly; see
[discussion27](../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md).
