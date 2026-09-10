# Independent verification scripts (Claude review, 9 September 2026)

Companion to `../../archive/reviews/2026-09-09_review-of-v0.2_claude/REVIEW_CLAUDE_20260909.md` (review of v0.2; the scripts still apply to the v0.3 package). Run everything from `numerics/` with the
package's own environment (`python-flint==0.9.0`, `mpmath`, `numpy`); nothing here modifies
the package, and the archives are only read. Set `ARCHIVE_1P8` / `ARCHIVE_LOG7` to point at
other `central_matrices.json.gz` files if needed (defaults: `output/length_1p8_N128/…`,
`output/log7_N128/…`).

| Script | What it checks | Runtime |
|---|---|---|
| `check_constants.py` | Recomputes $a_{N,L}$, $K_L$, $\eta_M$, $\epsilon$, $C_L$, chain norms from the printed formulas (mpmath, 60 digits; $g_j$ by Taylor expansion of $G_0$), the Cauchy majorant, the continuation rationals, and the $\log 8$ tail-floor projections for $N=128\ldots2048$. | ~1 min |
| `check_fourier_side.py` | Evaluates $Q_{0,9/5}[f]$ for $f_c=\cos^6(\pi x/L)$ directly from the Fourier/kernel definition (2.6) and compares with $2\sum_{\gamma>0}\lvert\hat f_c(\gamma)\rvert^2$ over the first 100 zeta zeros. Confirms the normalization to $6\times10^{-10}$. | ~3 min |
| `check_head_exact.py` | Diagonal head entries $Q_{0,L}[\phi_n]$ from the Fourier side: exact log-multiplier part via Weber–Schafheitlin, remainder multiplier by quadrature, pole/delay terms by quadrature; compared with the archived Arb head. Agreement to ~$10^{-11}$. | ~30 s |
| `check_grams_and_floor.py` | Full-output Gram entries $F_{ij}$, $C_{ij}$ by direct quadrature of the outputs $\widetilde U\phi_n$ (unitary coordinate), compared with the archive. Agreement to 20+ digits (quadrature precision). | ~10 min |
| `check_floor.py` | 80-digit head spectra, PSD check of $E_r$, the required-tail-floor diagnostic, and a sweep of the certified floor $m$ with the package's `validate()`. | ~1 min |
| `check_twosided.py` | Bisects the largest floor `validate()` certifies and certifies an upper bound by a ball Rayleigh quotient of the head ground state. Gives $3.34\times10^{-23}\le\lambda_{\min}(9/5)\le4.136\times10^{-23}$ and $1.33\times10^{-28}\le\lambda_{\min}(\log 7)\le6.802\times10^{-28}$. | ~45 s |
| `profile_runs.py` | Builds $\log2,\ldots,\log6$ with the unmodified `certify_arb.py` ($N=128$, $M=220$, 1792 bits) and encloses $\lambda_{\min}$ at each; writes `profile.json` (included). | ~6 min |

Full rebuilds of both certificates (`certify_arb.py`, `independent_arb.py`), the analyzer,
`compare_implementations.py` and `review_checks.py` were also rerun in the reviewing
environment (Python 3.11.15, python-flint 0.9.0, FLINT 3.6.0) and reproduced the archived
pivots, bounds and radii to every displayed digit.
