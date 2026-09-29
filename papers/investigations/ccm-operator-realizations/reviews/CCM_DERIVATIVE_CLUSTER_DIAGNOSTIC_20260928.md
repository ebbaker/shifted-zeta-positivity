# Independently specified Xi derivative spaces and the finite Schur correction

Date: 2026-09-28. Model: GPT-6 (Codex). Exact serving variant and reasoning effort were not exposed. Research diagnostic prepared for Edward Baker with LLM assistance.

**Status:** two bounded multiprecision experiments, each repeated at 130 and 160 decimal digits; no interval certification, no theorem about the infinite Fourier complement or the expanding-support limit. The only support is `X=13`, `L=log(13)`; the only Fourier cutoffs are `N=32,64`. The unchanged actual even Weil-matrix builder is used. No zero data enter the construction.

## Finding

The independently prescribed span of the projected analytic functions `k,k'',k''''` contains an excellent approximation to the observed finite even ground state. But minimizing the uncorrected energy inside that span selects a much poorer direction. Eliminating the *entire finite complement* at energy zero almost perfectly restores the finite ground state, provided the induced mass matrix is included. That result identifies a concrete correction which an analytic argument must control; it does not supply an independent bound for that correction.

The difficulty is visible in the scales: the complement remains very soft, and its correction cancels between about 18 and 28 decimal orders of the trial block's Frobenius norm. The finite inverse used here already contains the whole remaining finite operator. Its successful use is standard finite block elimination, not a resolution of the sign or infinite-tail problem.

## Trial functions and endpoint handling

On `[-b,b]`, `b=L/2`, use the analytic even Xi kernel in the normalization

\[
k(x)=e^{x/2}\sum_{n\ge1}\frac\pi2(ne^x)^2
       \bigl(2\pi(ne^x)^2-3\bigr)e^{-\pi(ne^x)^2},\qquad x\ge0,
\]

extended evenly. An overall nonzero constant has no effect on the trial space. This is the analytic Xi kernel, not a finite prolate candidate. Set `t=pi*n^2*exp(2x)`. Each summand is

\[
(\pi n^2)^{-1/4}t^{5/4}e^{-t}P_0(t),\quad P_0(t)=t-3/2,
\]

and analytic derivatives follow from

\[
P_{m+1}(t)=(5/2-2t)P_m(t)+2tP'_m(t).
\]

Let `P_N` be the projection onto the orthonormal even basis

\[
e_0=L^{-1/2},\qquad e_n=(2/L)^{1/2}\cos(d_n(x+L/2)),\quad d_n=2\pi n/L.
\]

The two prescribed trial spaces are

\[
V_{N,2}=\operatorname{span}\{P_N k,P_N k''\},\quad
V_{N,3}=\operatorname{span}\{P_N k,P_N k'',P_N k''''\}.
\]

Normalize the projected columns separately, then apply QR. No eigenvector is used to build these spaces. Eigenvectors of the actual finite matrix are computed only for reference comparisons, including the best approximation obtainable in the prescribed span.

The derivative coefficients include endpoint terms. For `a_0=1/sqrt(L)`, `a_n=sqrt(2/L)` for `n>=1`, and *unnormalized* coefficients `c_n(f)=<e_n,f>`, integration by parts gives

\[
c_n(k'')=-d_n^2c_n(k)+2a_n k'(b),
\]
\[
c_n(k'''')=d_n^4c_n(k)-2a_nd_n^2k'(b)+2a_n k'''(b).
\]

The implementation divides all these terms by the same preliminary norm of `k`; subsequent separate column normalization leaves the spans unchanged. At this support,

\[
k(b)\simeq5.59150\,10^{-15},\quad k'(b)\simeq-4.31134\,10^{-13},\quad
k'''(b)\simeq-2.35350\,10^{-9}.
\]

Thus simply multiplying the Fourier coefficients by powers of `-d_n^2` would implement a different candidate and omit relevant boundary terms. Direct quadrature of derivative coefficients at modes `0,1,3`, and independent differentiation at `x=0.4`, check the recurrence and these formulas.

## Blocks, Schur correction, and the correct mass

Write `A` for the actual `(N+1)`-dimensional even Weil matrix. For orthonormal trial columns `S` and an orthonormal complement `T`, form

\[
H=S^*AS,\qquad C=T^*AS,\qquad D=T^*AT.
\]

Only after positivity of the finite `D` is observed numerically, solve

\[
Z=D^{-1}C,\quad J=C^*Z,\quad F_0=H-J,
\quad U=S-TZ,\quad K=I+Z^*Z.
\]

The exact finite identities are

\[
U^*AU=F_0,\qquad U^*U=K.
\]

The harmonic-lift Ritz vector reported below solves the **generalized pencil**

\[
F_0p=\theta Kp
\]

for its least eigenvalue, and normalizes `Up`. An ordinary smallest-eigenvalue vector of `F_0` minimizes a different quotient. For transparency, the records contain both choices and their full-space lifts.

## Results

Distances are Euclidean distances between normalized coefficient vectors, with sign aligned to the actual finite even ground state. “Best in span” is the normalized projection of that reference ground state onto `V_{N,m}`; it is a diagnostic lower bound on the distance attainable in the prescribed trial span, not a candidate construction.

| N | dim | Xi proxy distance | H-Ritz distance | Best in span distance | Harmonic-lift Ritz distance |
|---:|---:|---:|---:|---:|---:|
| 32 | 2 | 0.0150644 | 0.0126688 | 2.26867e-4 | 7.25157e-17 |
| 32 | 3 | 0.0150644 | 0.0105590 | 3.49381e-6 | 4.97862e-24 |
| 64 | 2 | 0.0225145 | 0.0201339 | 5.43700e-4 | 1.75612e-18 |
| 64 | 3 | 0.0225145 | 0.0179968 | 1.52151e-5 | 2.44410e-26 |

The trial span's geometric capture is substantially better than the vector chosen by `H`. Going from `N=32` to `N=64` worsens the Xi, plain Ritz, and best-in-span distances at this fixed support; these two cutoffs do not establish a limiting trend. The harmonic lift leaves the prescribed span and uses the full finite complement, so its much smaller distance is not in conflict with the best-in-span bound.

The actual least even eigenvalues are approximately `2.25893119e-49` at `N=32` and `6.32135141e-59` at `N=64`. The complement and cancellation scales are:

| N | dim | observed min(D) | min(H) | ||C||F | ||H||F | ||F0||F | log10(||H||F/||F0||F) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | 2 | 7.05873e-37 | 6.28183e-32 | 3.32372e-12 | 1.36800e-23 | 1.01126e-42 | 19.1312 |
| 32 | 3 | 1.57365e-31 | 1.80448e-34 | 5.96154e-10 | 4.16201e-19 | 7.09613e-37 | 17.7683 |
| 64 | 2 | 1.95358e-44 | 5.26136e-32 | 3.71786e-12 | 1.06703e-23 | 2.59401e-51 | 27.6142 |
| 64 | 3 | 3.89838e-38 | 1.53802e-34 | 6.64164e-10 | 3.29293e-19 | 1.97347e-44 | 25.2224 |

These Frobenius cancellation figures measure the scale of the *whole effective block*, not directly the accuracy needed to certify its smallest eigenvalue. In each row `J` has the same displayed norm as `H`. Certifying the smallest direction can require more accuracy still. Although `D` is tiny, the solved lift norms `||Z||F` are only approximately `0.03434, 0.06416, 0.04877, 0.08826`, respectively. This is a structured coupling fact in these finite calculations; estimating `||Z||` solely by `||C||/min(D)` would discard that structure.

The ordinary-Schur full lifts have distances approximately `1.74118e-12, 7.52765e-16, 6.46812e-13, 7.74164e-16` in the same row order. The mass correction improves these to the generalized harmonic distances in the first table. The reported conclusion therefore uses `K`, not an ordinary eigenproblem silently treated as a Ritz problem.

## A finite algebraic bound and its limitations

For a finite self-adjoint `A>=0` with `D>=delta I>0`, put `lambda=min eig(A)` and let `theta` be the least generalized eigenvalue of `(F0,K)`. If `lambda<delta`, then

\[
\frac{\theta\delta}{\delta+\theta}\le\lambda\le\theta.
\]

The upper bound is Rayleigh–Ritz on the harmonic graph. For an actual eigenvector with nonzero trial head `p`, block elimination gives

\[
p^*F_0p=\lambda\,p^*Kp+
\lambda^2p^*C^*D^{-2}(D-\lambda I)^{-1}Cp.
\]

The last quadratic form is at most `(delta-lambda)^{-1}p^*(K-I)p`, yielding
`theta <= lambda*delta/(delta-lambda)` and the stated lower bound. For `lambda=0`, the same conclusion follows directly from the Schur identity. This is an elementary finite conditional bound; it does not justify its positivity assumptions in an infinite setting.

Using the observed finite minima for `delta`, its relative bracket widths are approximately `3.20019e-13, 1.43547e-18, 3.23577e-15, 1.62153e-21`, respectively. All four observed eigenvalues lie in these conditional brackets. The actual relative errors `theta/lambda-1` are much smaller: about `1.64319e-20, 1.72673e-29, 9.53081e-22, 3.68394e-31`. These values explain why energy-zero elimination is accurate in this finite diagnostic. They supply no eigenvector bound by themselves; the vector distances were directly measured against reference eigenvectors.

The bound presupposes positivity of `A`; equivalently, in a proof using block elimination with `D>0`, one must independently establish `F0>=0`. Here all relevant signs are floating observations. Neither a complement lower bound uniform in cutoff nor an independent lower bound for the effective block was established. The observed `D` minimum decreases by roughly seven orders when doubling `N` in either trial dimension. No fixed positive complement floor should be inferred.

## Consequences for the next analytic target

1. The three-dimensional derivative space is an explicit candidate cluster at this support. Its strong geometric capture is evidence for investigating derivative or translation-generated clusters; it is not evidence that this fixed dimension works on cofinal supports.
2. Any useful cluster reduction must retain the complement correction and induced mass. A theorem about `H` alone would address a visibly different direction in these data.
3. A useful proof target is a structured quadratic-form or matrix comparison for `C^*D^{-1}C` relative to `H`, with enough directional precision to determine the small residual sign and ground orientation. A generic small-coupling norm estimate loses the cancellation, and the computation of the complete finite inverse is not such a comparison.
4. The next step should be an analytic complement estimate, or a rigorously controlled reference inverse with a signed remainder, for an independently defined cluster. Repeating this exact finite elimination at more cutoffs without a remainder estimate would mainly restate the original operator problem in smaller coordinates.
5. There are two distinct limits: the Fourier cutoff at fixed support, and then cofinal support. This experiment addresses neither. Positive finite `D` and `F0` do not settle the missing Fourier tail, much less RH.

## Verification and reproducibility

Files in [../numerics/cluster-selection-20260928/](../numerics/cluster-selection-20260928/README.md):

- `check_derivative_cluster.py`: portable diagnostic, using the unchanged repository builders via `--repo-numerics`.
- `derivative-cluster-130.json`, `derivative-cluster-160.json`: compact records containing the small effective matrices, profiles, endpoint controls, and source hashes. No dense full matrices are archived.
- `summarize_derivative_cluster.py`, `derivative-cluster-summary.json`: source verification, exact comparison of retained output strings, and the conditional finite brackets.

The 130- and 160-digit records match exactly outside the precision field and rounding-error checks, at the serializer's 45 significant-digit output precision. All three source hashes match the current files. At 130 digits, the largest analytic-derivative/coefficient control error is below `8.6e-130`; the largest relative energy-congruence error is below `6.8e-84`; the largest relative generalized-Rayleigh discrepancy is below `3.1e-78`. The 160-digit repeat improves the latter two to below `1.2e-113` and `5.6e-108`. These are floating consistency checks, not interval bounds on integration or rounding errors.

Dependencies: Python and `mpmath` (tested Python 3.10.0, mpmath 1.3.0), plus the existing `check_odd_blocks.py` and `check_mass_stiffness.py` in the investigation's numerics directory. Install dependencies normally or make them available through `PYTHONPATH`; the scripts contain no private dependency path. From `numerics/cluster-selection-20260928/`, set `REPO_NUMERICS=..` (or use the absolute existing builder directory when staged elsewhere), then run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B check_derivative_cluster.py --repo-numerics "$REPO_NUMERICS" --digits 130 --cutoffs 32 64 --output derivative-cluster-130.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_derivative_cluster.py --repo-numerics "$REPO_NUMERICS" --digits 160 --cutoffs 32 64 --output derivative-cluster-160.json
python3 -B summarize_derivative_cluster.py --repo-numerics "$REPO_NUMERICS"
```

The default builder location is the script directory when `--repo-numerics` is omitted. Runtime source hashes are retained in both original records and were not rewritten after the runs.
