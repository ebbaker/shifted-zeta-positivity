# Independent numerical checks for the Claude review of 1 October 2026

Model: Claude Fable 5.1 (Anthropic), run through Claude Cowork in a cloud sandbox
(Python 3, mpmath 1.4.1, numpy 2.4.4, scipy 1.17.1, sympy). These scripts support the
[manuscript review](../../reviews/MANUSCRIPT_REVIEW_CLAUDE_20261001.md). They are
floating-point diagnostics, not certificates, and they are not used by the manuscript.
Manuscript state checked: commit `7034f88`, `manuscript.tex`
SHA-256 `b81bdbdb91541e7fae0f5da781792fb23ab09b1f7a09b34e4b9cffa69c446404`.

| Script | Output | What it checks |
|---|---|---|
| `check1_conventions.py` | `check1_output.txt` | (1) \(v_{1/2}\equiv1\) with the manuscript's Gamma and \(\pi^{-it}\) factors; (2) the phase-derivative formula (eq. phase-deriv) against finite differences of \(\arg v_\sigma\); (3) \(\mathcal E(B_{d,\gamma})=4\pi^2\) for several \(d\) of both signs; (4) the critical explicit formula (eq. critical-explicit) for a Gaussian source with \(s=0.3\). |
| `check2_crossings.py` | `check2_output.txt` | (4b) eq. critical-explicit with \(s=0.15\), where the critical-zero sum is a visible \(3\times10^{-3}\) contribution; (5) eq. crossing-formula at \(\sigma=0.75\) (pole crossed), \(\sigma=1\) (removable pole line, half residue \(a(0)\)), \(\sigma=1.5\) (no crossing); (6) \(c_0=\lVert C_\infty\rVert\) by a Gauss–Legendre Nyström discretization of the finite cosine transform on \((0,1)\), and the resulting gap constants \(g_\sigma\); (7) Lemma phase-limit for a Gaussian test at \(\gamma_1\). |
| `check3_operator.py` | `check3_output_X150.txt`, `check3_output_X220.txt` | End-to-end discretization of \(\chi V_\sigma P\), \(PV_\sigma\chi\), \(C_\sigma T_\sigma\) for the actual zeta phase on a periodic box, testing eq. L-trace term by term and the trend of \(\operatorname{Tr}(bL_\sigma b^*)\) toward \(\lvert b(\gamma_1)\rvert^2\) for \(\sigma=0.8,0.7,0.6,0.55\). Traces are localized to the interface \(x=0\) because on a circle the indicator \(P\) has a second (mirror-image) interface at the seam and \(\operatorname{Tr}(a(D)(V^*PV-P))\) vanishes identically in finite dimensions. Arguments: `X dx [sigma list]`. |

Headline results: all identities hold to the precision of the method (checks 1–5 and 7 to
\(10^{-10}\) or better; the operator identity to \(10^{-4}\), limited by the box and grid, with
the \(\sigma=0.55\) residual falling from \(1.1\times10^{-3}\) to \(8\times10^{-5}\) when the box
is enlarged from \(X=150\) to \(X=220\)). The archimedean gap is
\(1-c_0^2\approx5.72\times10^{-5}\) (Slepian's asymptotic gives \(6.2\times10^{-5}\)). Run times
are a few seconds for checks 1–2 and one to three minutes for each operator run on two cores.
