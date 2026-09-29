# Complete prime-power rate from the tail to a fixed core

Date: 2026-09-28. Model: GPT-6 (Codex). Exact serving variant and reasoning effort were not exposed. Prepared for Edward Baker with LLM assistance.

**Status:** bounded multiprecision diagnostic, repeated at 80 and 110 decimal digits. Every prime power required by the eight prescribed central windows is included by an integer sieve. No zero data or finite Weil matrices enter the calculation. Floating evaluations are not interval certificates and do not establish a uniform numerical bound as the tail parameter grows.

## Outcome and normalization

The observed tail-to-core rates agree with the continuum prediction, including its finite-`X` normalization. At `X=10000,T=1`, the complete rate is approximately `0.249974995355834`, and differs from its continuum prediction by only `-3.07889e-11`. However, a bound using the supremum of the finite prime-counting error is approximately `0.0102258` at that same point. The small observed discrepancy is much stronger than this coarse bound; these observations cannot substitute for the signed or localized estimates needed in a sharp weighted inequality.

Use the literal even kernel

\[
k(x)=e^{x/2}\sum_{n\ge1}\frac\pi2(ne^x)^2
       \bigl(2\pi(ne^x)^2-3\bigr)e^{-\pi(ne^x)^2},\qquad x\ge0,
\]

with even extension. Its Fourier transform is `Xi/4`, and

\[
d\mu(x)=k(x)\cosh(x/2)\,dx,\qquad M=\mu(\mathbb R)=1/8.
\]

For `x=log X>T`, define the complete rate into the fixed core `[-T,T]` by

\[
B_T(x)=\frac1{\cosh(x/2)}
\sum_{\substack{n\ge2\\|x-\log n|\le T}}
\frac{\Lambda(n)}{\sqrt n}k(x-\log n).
\tag{1}
\]

“Complete” means every permitted prime power is included; transitions outside this core are not part of `B_T`. There is no fixed prime truncation independent of `X`.

The factor in (1) follows from

\[
\mathcal E_p(u)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int k(s)k(s+\log n)|u(s+\log n)-u(s)|^2\,ds.
\]

At a positive point `x` in the tail, the edge back to `x-log n` contributes outgoing rate `Lambda(n)k(x-log n)/(sqrt(n)cosh(x/2))` relative to `dmu(x)`. There is no extra factor of two in that rate. The factor two appearing in the limit below comes from `sqrt(X)/cosh(log(X)/2)`.

## Stieltjes identity and a finite-envelope bound

Put

\[
a=Xe^{-T},\quad b=Xe^T,\quad
f_X(t)=t^{-1/2}k(\log(X/t)),\quad
\psi(t)=\sum_{n\le t}\Lambda(n),\quad E(t)=\psi(t)-t.
\]

The endpoints in this diagnostic are nonintegers. The exact Stieltjes formulas are

\[
B_T(\log X)=\frac1{\cosh(\log X/2)}\int_a^b f_X(t)\,d\psi(t),
\]

\[
B_T(\log X)-B^{\rm cont}_T(X)=
\frac{f_X(b)E(b)-f_X(a)E(a)-\int_a^b E(t)f_X'(t)\,dt}
{\cosh(\log X/2)},
\tag{2}
\]

where

\[
I_T=\int_{-T}^T e^{-y/2}k(y)\,dy=\mu([-T,T]),\qquad
B^{\rm cont}_T(X)=\frac{2X}{X+1}I_T.
\tag{3}
\]

The equality `I_T=mu([-T,T])` uses evenness. In particular, the expected limits are

\[
B_T(\log X)\longrightarrow2I_T\quad(X\to\infty,\ T\text{ fixed}),
\qquad 2I_T\longrightarrow2M=1/4\quad(T\to\infty).
\tag{4}
\]

For a rigorous envelope `|E(t)|<=eta*t` on `[a,b]`, (2) gives the rigorous conditional bound

\[
|B_T-B_T^{\rm cont}|
\le\eta\frac{2X}{X+1}V_T,
\tag{5}
\]

with, for example,

\[
V_T=2\cosh(T/2)k(T)+
\sqrt{4\sinh(T/2)
\int_{-T}^T e^{-y/2}|k'(y)+k(y)/2|^2\,dy}.
\tag{6}
\]

Indeed, `f_X'(t)=-t^{-3/2}[k'(y)+k(y)/2]`, `y=log(X/t)`. After changing variables, the integral in the total-variation estimate is bounded by weighted Cauchy–Schwarz, producing (6). This avoids estimating roots of the absolute-value integrand numerically.

For each finite interval, the supremum

\[
\eta_{X,T}=\sup_{a\le t\le b}\frac{|\psi(t)-t|}{t}
\]

is attained among its endpoints and one-sided values at the included prime-power jumps. Between jumps, `psi` is constant and `psi(t)/t-1` is monotone, so its absolute value has no strict interior maximum. The program visits all those values. Its logarithms, kernel values, integrals and envelope values are floating approximations; thus the recorded envelope-based bounds are diagnostic evaluations of (5), not certified intervals.

The program also replays (2) from the exact step locations: if `psi_j` is constant on a gap, its integral against `df_X` is `psi_j[f_X(right)-f_X(left)]`. The remaining integral of `t df_X` is recovered by integration by parts from endpoint values and the single smooth integral of `f_X`. This verifies the finite prime-step/Stieltjes bookkeeping without replacing the arithmetic sum by a smoothed density.

## Bounded results

The only tested parameters are `X=20,100,1000,10000`, with `T=0.5,1`. A complete integer sieve through `ceil(10000*e)=27183` covers all required prime powers.

| X | T | Prime powers in window | B_T | B_cont | B_T - B_cont |
|---:|---:|---:|---:|---:|---:|
| 20 | 0.5 | 10 | 0.235998573978082 | 0.233975931511528 | +2.02264e-3 |
| 20 | 1 | 19 | 0.238060954450072 | 0.238095231320144 | -3.42769e-5 |
| 100 | 0.5 | 26 | 0.242996530948278 | 0.243242305036737 | -2.45774e-4 |
| 100 | 1 | 56 | 0.247524464044679 | 0.247524745431833 | -2.81387e-7 |
| 1000 | 0.5 | 156 | 0.245543399174763 | 0.245429298788317 | +1.14100e-4 |
| 1000 | 1 | 339 | 0.249750241316392 | 0.249750242643508 | -1.32712e-9 |
| 10000 | 0.5 | 1138 | 0.245776218315784 | 0.245650163070798 | +1.26055e-4 |
| 10000 | 1 | 2496 | 0.249974995355834 | 0.249974995386613 | -3.07889e-11 |

The fixed-core limiting rates are

\[
2I_{0.5}\simeq0.245674728087105,\qquad
2I_1\simeq0.249999992886151.
\]

Their deficits from `1/4` are approximately `0.00432527` and `7.11385e-9`, respectively. The continuum rate at finite `X` has the additional factor `X/(X+1)`. Comparing the prime rate directly with `1/4` without these two corrections would misidentify the arithmetic error.

At `T=0.5` the signed arithmetic error changes sign across the four values of `X`; these data establish no monotonic approach to the limiting rate. Although the wider window gives much smaller observed arithmetic errors here, the coarse supremum bound gets worse because it samples a larger interval and has a larger variation constant.

| X | T | finite eta | envelope-based error bound | resulting raw lower rate |
|---:|---:|---:|---:|---:|
| 20 | 0.5 | 0.213084 | 0.200810 | 0.0331659 |
| 20 | 1 | 0.287999 | 0.368076 | -0.129981 |
| 100 | 0.5 | 0.0776227 | 0.0760486 | 0.167194 |
| 100 | 1 | 0.118821 | 0.157873 | 0.0896518 |
| 1000 | 0.5 | 0.0212932 | 0.0210489 | 0.224380 |
| 1000 | 1 | 0.0250503 | 0.0335827 | 0.216168 |
| 10000 | 0.5 | 0.00669015 | 0.00661937 | 0.239031 |
| 10000 | 1 | 0.00762087 | 0.0102258 | 0.239749 |

The negative raw lower bound in one row can of course be replaced by the trivial zero bound. The table is intended to expose the precision lost by this envelope argument, not to claim a sharp certificate. At `X=10000,T=1`, the computed bound is about `3.32e8` times the observed absolute error.

## What follows analytically, and what does not

The classical prime number theorem `E(t)/t -> 0`, together with (5), proves the first limit in (4) for each fixed core. This is an analytic consequence of PNT and the explicit finite variation constant; it is not an extrapolation from the table.

There is also a uniform exterior Dirichlet consequence. Let `R>T` and let `u` vanish on `[-R,R]`. Restricting the nonnegative prime energy to edges joining the support of `u` to `[-T,T]` gives

\[
\mathcal E_p(u)\ge
\left(\inf_{|x|>R}B_T(|x|)\right)\|u\|_{L^2(\mu)}^2.
\tag{7}
\]

Set `eta_R=sup_{t>=exp(R-T)} |E(t)|/t`. For arbitrary `x`, discard a possible prime-power atom at the lower window endpoint and use the Stieltjes interval `(a,b]`; this can only decrease the nonnegative rate and makes the same lower estimate valid without an endpoint exception. Equation (5) yields, for `|x|>R`,

\[
B_T(|x|)\ge
\frac{2e^R}{e^R+1}I_T-2\eta_R V_T.
\tag{8}
\]

PNT gives `eta_R -> 0`. Taking `R` large for fixed `T`, then taking `T` large, proves that for every `epsilon>0` there exists `R` such that

\[
\mathcal E_p(u)\ge(1/4-\epsilon)\|u\|_{L^2(\mu)}^2
\quad\text{when }u=0\text{ on }[-R,R].
\tag{9}
\]

These inequalities can first be stated for compact smooth `u` and then extended wherever the closed jump form permits. The reflection of the prime edges gives the same rate in the negative tail. Since the gamma jump energy is nonnegative, adding it preserves (9).

Equation (9) controls functions forced to vanish in the core. It does not control the core–tail cross terms for a general function, exclude subthreshold modes involving the core, or prove the sharp global mean-zero inequality. A pointwise outgoing rate is only one component of the full quadratic form. No essential-spectrum assertion or compactness result is claimed from this diagnostic alone.

This identifies a useful role for the prime sum: retaining all prime powers at the moving scale recovers the threshold in the tails, whereas truncating the primes at a fixed bound would eventually miss every edge into a fixed core. The companion [operator note](../notes/CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md) separately supplies quantitative localization and the essential lower edge. Excluding discrete subthreshold modes uniformly toward 1/4 remains open. Increasing the largest `X` in this table would not address that missing step.

## Records and reproducibility

The [weighted-tail numerical directory](../numerics/weighted-tail-20260928/README.md) contains:

- `check_weighted_prime_tail.py`: standalone portable implementation; only `mpmath` is needed in addition to Python.
- `weighted-prime-tail-80.json` and `weighted-prime-tail-110.json`: small records, including the source hash, all window counts, rates, PNT envelopes and replay checks.
- `summarize_weighted_prime_tail.py` and `weighted-prime-tail-summary.json`: source-hash verification and precision comparison.

All retained observable strings agree at the serializer's 45 significant-digit precision between the two runs; the precision and roundoff-check fields are excluded from that comparison. The current source hash matches both run records. The largest integration-by-parts replay discrepancies are approximately `1.4e-81` and `2.8e-111`, respectively. These checks establish consistency of the floating calculation, not certified arithmetic error bounds. The kernel series is truncated using a precision-dependent rapidly decaying tail rule, and its truncation is not interval enclosed.

Tested with Python 3.10.0 and mpmath 1.3.0. Install mpmath normally or make it available through `PYTHONPATH`; no private dependency path is embedded in the code. From the numerics directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B check_weighted_prime_tail.py --digits 80 --output weighted-prime-tail-80.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_weighted_prime_tail.py --digits 110 --output weighted-prime-tail-110.json
python3 -B summarize_weighted_prime_tail.py
```

No numerical generator source was changed after the recorded runs. No large derived data are saved. The main analytic results and their limits are in the [round-8 synthesis](../notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md).
