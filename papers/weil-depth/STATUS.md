# Verification status — Weil depth v0.4

10 September 2026. Working draft; not externally reviewed by a human, not formally verified.

| Claim or component | Status | Evidence and limits |
|---|---|---|
| Central normalization and prime-power generator (eq. 2.6, Prop. 3.1) | Analytically reviewed twice; confirmed numerically against zeta zeros | v0.2 review checked Suzuki's coefficient formulas; v0.3 review rederived the gamma symbol and kernels and confirmed $Q_{0,9/5}[f]=\sum_\rho\lvert\hat f_c(\gamma_\rho)\rvert^2$ for a smooth test to relative $6\times10^{-10}$ (`numerics/review_claude/check_fourier_side.py`) |
| Polynomial form core (Lemma 2.2) | Analytically reviewed | Dilation, mollification, $C^1$ polynomial approximation, boundedness of the finite-rank projection checked |
| Shift perturbation and continuation (Lemmas 3.2–3.3, Prop. 3.4) | Analytically reviewed; proof written out in v0.3; one local step corrected in v0.4 | Weighted Laplace-line realization, norm differentiability for positive shift, Sobolev restriction below 1/2, form identity for the smoothed vector, Gronwall, strong zero-shift limit; the $C_L$ bound carries a harmless spare factor 2. The v0.3 proof of Lemma 3.3 asserted $\lvert p\pm\alpha\rvert,\lvert p\pm\beta\rvert\ge\eta-1/2$, false for $p-\beta$ (which does not occur in the denominator); v0.4 states the bounds actually used, $\lvert p-\alpha\rvert\ge\eta-1/2$ and $\lvert p+\beta\rvert\ge\eta+1/2$. The lemma is unaffected |
| Fractional infinite-tail estimate (Lemma 4.1, Prop. 4.3) | Analytically reviewed; sharpness quantified | Jacobi identity and weighted norm checked; exact single-mode value via Weber–Schafheitlin shows the floor is sharp to within $\log 2$ on single modes (Remark 4.2); closure step made explicit |
| Profile remainder (Lemma 4.4) | Analytically reviewed | Cauchy majorant 256 verified and shown to be loose by an order of magnitude |
| Full-output parity leakage and Schur test (Lemma 5.1, Prop. 5.2) | Analytically reviewed and recomputed | Both exact full Grams retained; Gram entries confirmed by direct quadrature to 20+ digits (`check_grams_and_floor.py`); head diagonal confirmed from the Fourier side to $10^{-11}$ (`check_head_exact.py`) |
| Lower bounds at $\log2,\ldots,\log6,\ 9/5,\ \log7$ (Theorem 6.1) | Full builds PASS; independent implementation PASS at all seven; replay PASS | `numerics/output/*_N128/central_certificate.json`, `enclosure.json`; `numerics/review/crosscheck_*.json`; floors are the largest three-significant-figure rationals passing the sector tests |
| Upper bounds (Prop. 6.2) and even ground state | Ball Rayleigh quotients PASS; even upper bound below odd floor in every row | `enclosure.json` per horizon; the ground-state vectors themselves are diagnostics |
| Small-shift, reflection and storage bounds at all horizons | Analytic consequence; exact rational checks PASS | `analysis.json` per horizon (`analyze_certificate.py` with the constants of Table 1); shift bounds are sufficient, not optimal |
| Outward ball serialization and replay | Reviewed; PASS | Dyadic reconstruction containment; hash binding (archive hash and matrices content hash); analytic bounds, trace and leakage rechecked on replay |
| Displayed rounding in Table 3 (certificate data) | Corrected in v0.4 | v0.3 printed nearest- or floor-rounded midpoints (e.g. tail floor `0.6075` at `log 7`, above the certified `0.60748…`; error `3.73e-37` and radius `4.6e-295`, below their certified upper values). `make_tables.py` now rounds lower endpoints down and upper endpoints up from the full ball, radius included (`0.6074`, `3.74e-37`, `4.7e-295`), and `paper_numbers.json` records endpoints rather than midpoints. Presentation only: the sign tests always used the stored balls |
| Reproducibility without the archives | Verified in the tested environments | Archives are unversioned (layout and hashes in `ARCHIVES.md`); rebuilds under Python 3.10/3.11/3.12 with python-flint 0.9.0 / FLINT 3.6.0 give identical `matrices_content_sha256` at 9/5 and `log7`. Not a claim of bit-for-bit portability to other arithmetic libraries; the sign tests do not depend on the hash |
| Moment formulas | 45 independent numerical integrals PASS | `numerics/review/review_checks.json`; diagnostic quadrature, not interval certification |
| Sharper leakage error (Remark 5.3) | Proved | Not used in any reported certificate |
| Storage update and nested Schur identities (Appendix B) | Algebraically proved | Bookkeeping only; no arithmetic preservation theorem |
| `log 8` and horizons above `log 7` | Not certified | Scalar tail floor at $N=128$ is negative there; keeping it near 0.6 needs $N\approx310$ or more (Section 7.2). These are resource projections for the present implementation: at fixed $L<3$ the scalar floor $a_{N,L}\to+\infty$ as $N\to\infty$, so it is cost, not an obstruction, that grows |
| Decay of the enclosures with $L$ | Observed, not proved | $-\log_{10}\mu_j$ rises by about 11 per unit horizon between `log 2` and `log 3` and about 33 between 9/5 and `log 7`; finite differences on seven horizons, consistent with Zhu's empirical Landau–Widom law. No decay law at unbounded depth is claimed |
| All-depth sequence / RH | Not proved | The diagonal implication does not construct the required sequence |
| Novelty / literature | Limited check | Yoshida and Connes–Consani cover $L\le\log2$ for test functions whose Fourier transform vanishes at the poles (pole term removed); the `log 2` row here concerns the full form without that condition, and the two normalizations have not been matched term by term. Zhu's certified window (total length 1.6) has the same active primes as the `log 5` row and its floor is consistent with ours (compatible lower bounds by different methods, not a cross-check); no exhaustive search |

Review and code were produced with language-model assistance under the author's direction
(OpenAI models for v0.1–v0.2; Anthropic's Claude for the v0.2 review and the v0.3
revisions; an OpenAI model for the v0.3 review, without recomputation; Claude for the v0.4
revisions, which changed no certificate). The two implementations, the Fourier-side checks and the enclosures all share
the analytic reduction; their agreement is not a separate proof of that reduction.

Known robustness fix in v0.3: `independent_arb.py` used `sum()` over an empty generator at
the prime-free horizon `log 2`, which returned a Python integer instead of an Arb ball and
made the bounds record fail; it now starts the sums at `arb(0)`. No certificate was
affected.
