# Version 0.3 status — 11 September 2026

Working draft; not externally reviewed by a human, not formally verified. All
statements are in the working Weil-depth v0.3 normalization (source preserved
under `archive/drafts/v0.1_2026-09-10/reference/weil-depth-v0.3/`); the author's
independent normalization audit is pending. A certified statement means a
recorded guarded Arb sign test plus its stated analytic reduction.

| Claim or component | Status | Evidence and limits |
|---|---|---|
| Residual identity, graph-scaled form, direct-floor lemma (Sec. 3) | Analytic; reviewed | Elementary; the direct-floor lemma is new in v0.3 and replaces the scalar comparison in the conditional theorem |
| Analytic complement floors: weight bound for the arithmetic norm, gamma tails with the variation hypothesis, Carleman and Hilbert–Schmidt cross bounds (Sec. 4.1) | Analytic; reviewed; constants recomputed independently | v0.2 review recomputed `g_{a,256}`, `g_{h,32}`, `f_0`, `beta`, `beta_theta`, `C_{L_q}` to 10–17 digits; the inherited fractional-tail bound is from Weil-depth |
| First step, absolute floor `Q_{0,L_q} >= 2.99e-29` | Certified (R14) | Largest passing three-figure floor by bisection; `3.00e-29` fails; 2048-bit re-evaluation of the 6144-bit archive; reproduces R7 at `1e-33` to every printed digit |
| First step, relative test: `M_0.9 >= 2.90e-29`, `M_0.8 >= 2.67e-29`, residual factor `theta = 0.78` | Certified (R14) | Hence `H_J >= 2.90e-29`, `R*F^{-1}R <= 0.78 H_J`, and `Q_{0,L_q} >= 2.90e-29/tau^2 = 1.13e-29` by the direct-floor lemma; `theta = 0.76` fails |
| First step, comparison `H_J >= 1.13e-7 A` | Certified (R14) | `1.14e-7` fails; generalized eigenvalue `min H_J/A` on 256 modes is `1.22e-7` (diagnostic) |
| Upper bound `lambda_min(Q_{0,L_q}) <= 3.29e-29` | Certified (R16) | Ball Rayleigh quotient of a 60-digit rational vector plus the head error; quotient `3.28379e-29` |
| Shift consequences at `L_q`: `Q_{s,L} >= 1.49e-29` for `s <= 9e-16`; `||V|| <= exp(-1.4e-29 omega)`; `D >= (1 - exp(-2.9e-29 omega)) I` | Analytic consequence | `C_{L_q} < 16.5362`, `C (9e-16)^2 = 1.34e-29 < 1.495e-29`; supersedes the v0.2 interval `5e-18` and the global R6 interval `5e-17` |
| Second step, comparison `H_{J_2} >= 5.01e-8 A_2` | Certified (R15) | `5.02e-8` fails; generalized eigenvalue `6.0e-8` (diagnostic) |
| Upper bound `lambda_min(Q_{0,L_2}) <= 1.89e-30` | Certified (R16) | Quotient `1.88423e-30` |
| Second step with 32-mode slabs, full-operator floor and residual factor | **Not certified** (R11, R12, R15) | Absolute test fails at `1e-36` (pivot 182); residual tests fail at `theta = 0.9, 0.95, 0.99`; twenty weighted variants fail. Failures reproduced at 2048 and 4096 bits |
| Second step with 96-mode slabs (`256+96+96`): `1.69e-30 <= lambda_min(Q_{0,L_2}) <= 1.89e-30`, `M_0.9 >= 1.65e-30`, `theta = 0.8`, `H_{J_2} >= 5.25e-8 A_2`; shift `omega <= 2e-16`, `||V|| <= exp(-8e-31 omega)` | Certified (R18) | Three-interval floor 0.768 as projected; `1.70e-30` fails; built in a cloud container at 6144 bits (archives external, regenerate locally); replays at 2048 bits |
| Diagnosis of the second-step failure | Diagnostic (R16, hypothetical floors) | With the certified three-interval floor replaced by `0.55`, both tests pass; with `0.65`, `theta = 0.8` passes and the largest passing absolute floor is `1.64e-30` (upper bound `1.89e-30`); `0.5` fails. Projection: 96 modes on each short slab supply the needed floor (Table 1 of the paper) |
| Appended-slab recursion | Analytic projection | Comparison-matrix floor decreases roughly linearly in the number of slabs and turns negative after about five 32-mode slabs (Table 2) |
| Conditional continuation theorem | Analytic; hypotheses verified for the first and second steps | Direct-floor version; the `mu` recurrence of v0.2 was dropped because it loses about six orders of magnitude per step against the true decay |
| Verification-dimension estimate | Heuristic with a rigorous lower bound on `rho_L` | `N` grows like `L exp(rho_L)`: about `10^3` modes at `L = 3`, `4e4` at `L = 4` for a positive floor; practical horizon of the method near `L = 3` |
| Fourier-side check (R17) | Diagnostic (midpoints, mpmath) | Zero sums for the lowest eigenvector reach 92% of `lambda_0` with 400 zeros and 97.8% with 2000 (height 2515), the remainder scaling as `1/T`; `f_0` vanishes at the first zeros to `1e-28`–`1e-18`; a displacement of the first zero by `1e-12` would already contradict the certificate, while zeros above height about 70 are invisible |
| Cumulative storage and generator identities (Appendix A) | Analytic; motivational | Not used by any theorem; no positive-shift certificate exists |
| Independent reconstruction of the spatial matrices | **Open** | The validators (not the builders) have a second implementation from the v0.2 review; no second 256+32 or 256+32+32 build |
| Normalization audit; human review; formal verification | **Open** | |

## Project closeout

The storage-depth writing project is closed out on 11 September 2026 as a
working draft. [CLOSEOUT.md](CLOSEOUT.md) records the repository and archive
checks. This changes no certificate or review status in the table above.

## Deferred research and verification (not closeout tasks)

1. Regenerate the two R18 archives locally (commands in ARCHIVES.md) and confirm
   their content hashes; re-run `replay_floor.py --step 2 --record ...` on them.
2. Build the two-interval second step (global basis on `(0, L_q)`) for
   comparison with the three-interval one, and choose the recursion invariant
   (merge periodically, or grow the slabs).
3. Make the Fourier-side check rigorous: more zeros, a tail bound from the
   endpoint values, ball arithmetic for the transforms.
4. Independent reconstruction of the spatial matrices.
5. The normalization audit.

Version 0.2 and its records remain unchanged under `archive/drafts/v0.2_2026-09-10/`;
its numerics records under `numerics/records/` are still current and are
extended, not replaced, by R14–R18.
