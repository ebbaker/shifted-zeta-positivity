# Numerical checks for the second Claude review (revision of 1 October 2026)

Model: Claude Fable 5.1 (Anthropic), run through Claude Cowork in a cloud sandbox
(Python 3, mpmath 1.4.1, numpy 2.4.4). Supports the
[second review](../../reviews/MANUSCRIPT_REVIEW_ROUND2_CLAUDE_20261001.md) of the revised
manuscript (commit `5a431c1`, `manuscript.tex`
SHA-256 `fe6f997edb5fff06ee9f37aa599b748621b8622bf046a15a306ab05dac6953dc`).
Floating-point diagnostics, not certificates; nothing here is used by the manuscript.
The first-round scripts in [`../review_checks_claude_20261001/`](../review_checks_claude_20261001/README.md)
remain valid for the revision, since none of the identities they test changed.

`check4_revision.py` → `check4_output.txt`:

- **A. Finite Blaschke energy.** \(\mathcal E(\Theta)/4\pi^2\) for Blaschke products with
  \(m=1,2,3\) zeros in one half-plane (unequal widths, and a triple zero) equals \(m\) to five
  digits, confirming the revised Lemma 5.1's identity \(\mathcal E(\Theta)=4\pi^2 m\). Mixed products
  (zeros in both half-planes) give \(1.92\), \(0\), \(2.60\) against the manuscript's bound
  \(2(m_++m_-)=4,4,6\) and against the sharper \(m_++m_-=2,2,3\); the rational-model symbol
  reproduces its rank-one prediction \(2q^2=1.92158\).
- **B. Interpolation bound** \(\mathcal E(f)\le2\pi\lVert f\rVert_2\lVert f'\rVert_2\) (eq. 5.7):
  holds on three test functions; nearly tight for a chirp (ratio \(0.99\)).
- **C. Window energy for the zeta phase.** \(\mathcal E(b_jv_\sigma)\) for the actual \(v_\sigma\),
  \(\sigma=0.6\) and \(0.51\), at heights \(j=10,\dots,30000\), computed as
  \(\int|\xi||\widehat{b_jv_\sigma}|^2d\xi\) by FFT, with the number of critical zeros in the window
  (sign changes of Hardy's \(Z\)) for comparison. \(\mathcal E/4\pi^2\) tracks
  \(0.26+\sum_{\gamma\in\text{window}}b_j(\gamma)^2\) closely; \(\mathcal E/\log(2+j)\) stays within
  \(8\)–\(15\) while \(\mathcal E/\log^2(2+j)\) decreases, as the revised logarithmic bound predicts.

Run time about four minutes on two cores (dominated by `mpmath.zeta` at height \(10^4\)–\(3\cdot10^4\)).
