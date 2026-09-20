# Dated manuscript drafts

The [current working manuscript](../manuscript.pdf) and its
[TeX source](../manuscript.tex) live at the investigation root. This folder
preserves complete, buildable versions with their PDFs and hash records.

| Version | Date | Contents and status |
|---|---|---|
| [0.5](2026-09-15-v05/README.md) | 15 September 2026 | Characterises the output states one magnetic insertion can reach (Section 6.5) --- exactly the functions analytic past the unit circle --- and realizes the mirror prime reference by one dressing at the same fixed $q$ (Corollary 7.10), settling the open question of Remark 7.10 of version 0.4; adds Section 7.6, presenting the target as a compression of the gamma energy with both sides positive term by term and an explicit source on the dominating side, so that the prime-free inequality is no longer a prerequisite; withdraws the claim of version 0.4 that a realization of the pole term must contain a null pair in an indefinite-metric sector, and restates Problem 8.3 as the single compression; adds `check_mirror_dressing.py` and `check_gamma_compression.py`. |
| [0.4](2026-09-15-v04/README.md) | 15 September 2026 | Adds Section 2.5: the pole form as the hyperbolic pairing of the evaluations at $s=0$ and $s=1$, and the unitary involution every source carries, identified with $\rho\mapsto1-\rho$ for a compatible realization; settles the prime-free inequality outside the window $\log 2<L<\log 7$ (Yoshida below, Proposition 8.1 above) and qualifies the Connes-Consani mechanism; adds `check_prime_free_archimedean.py`, an author field and a preparation note. |
| [0.3](2026-09-15-v03/README.md) | 15 September 2026 | Adds Section 7.5: the mirror prime reference, the prime-free subtraction form of the target, and the criterion as a domination or compression; revises the outlook around the prime-free archimedean inequality and adds Problem 8.2. |
| [0.2](2026-09-15-v02/README.md) | 15 September 2026 | Adds the spectral form of the target, the interference bound, and Theorem 7.5 excluding the archimedean/prime two-channel source with explicit certificates at $L=1$ and $L=5/4$ and for large $L$; adds the explicit-formula and channel-bound checks and the spectral-realization literature. |
| [0.1](2026-09-14-v01/README.md) | 14 September 2026 | First working manuscript: self-contained Weil normalization, sphere and Schur calculations, dressed prime norm, magnetic-domain and gluing restrictions, and earlier exact source tests. The complete Weil match remains open. |

Save each subsequent reviewed version in a new date-and-version directory.
Never replace files inside an earlier snapshot. The [build guide](../BUILD.md)
describes the save and verification commands. To rebuild an older version,
first copy its directory to a separate working location.
