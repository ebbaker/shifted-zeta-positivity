# A bounded diagnostic of the Xi proxy and the actual even Weil ground

28 September 2026. Prepared for Edward Baker with LLM assistance.

Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort are
not exposed and are not inferred. Status: multiprecision floating diagnostic,
not an interval certificate or an infinite-support theorem. The original run
metadata used an unverified Astra label; that metadata has been corrected in
the active records, and the original bytes remain in `../numerics/ground-selection-20260928/run-sources/`.

## Result

The simple residual/second-even-separation estimate is unavailable in every
tested case, despite ground overlaps close to one. The normalized candidate's
Rayleigh value lies *above* the second even eigenvalue. The computation also
separates two distinct effects: the candidate's Fourier approximation can be
extremely accurate while its difference from the actual finite ground remains
visible; and almost all of the ordinary residual norm can come from tiny
components outside the lowest even spectral cluster.

This supports a cluster-resolved or energy-weighted comparison as a more
informative next target. It does not prove that such a comparison can be
closed, that the finite grounds converge, or that the original prolate
candidate fails.

## Exact object tested

The bounded audit defines the Xi kernel by

\[
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2},\qquad
k(x)=e^{x/2}\sum_{n\ge1}h(ne^x).
\]

The kernel is even. For stable numerical evaluation the program uses the same
positive-side series at \(|x|\). It tests the unit-norm restriction

\[
w_L=\frac{\mathbf1_{[-L/2,L/2]}k}{\|\mathbf1_{[-L/2,L/2]}k\|_2}.
\]

**This is an analytic Xi proxy, not the finite prolate sum \(q_L\) or its
normalized version \(v_L\).** The audit proves that these candidates approach
the same limiting kernel, but they are different finite-support test vectors.
In particular the truncation of k can leave endpoint defects not shared by a
prolate construction. No conclusion below is an exclusion of the original
prolate comparison.

The Fourier basis is
\(e_0=L^{-1/2}\),
\(e_n=\sqrt{2/L}\cos(2\pi n(x+L/2)/L)\), \(n\ge1\).
For \(L=\log X\), the actual even block \(A=W_{+,L,N}\) is built from the
repository's closed gamma, pole, and prime-power formulas. The fast existing
builder is hard-coded to X=13. The workspace program generalizes its length,
exponential tail and prime list; the block-assembly routine is imported
unchanged. Both parity blocks at N=3 are compared with the existing defining
distribution/quadrature builder at every tested X. At X=13 the generalized
coefficients are also checked against the inherited fast coefficients.

Let \(\widehat w=P_Nw_L/\|P_Nw_L\|\), \(u\) be the unit finite even ground
with sign chosen toward \(\widehat w\), and let
\(\epsilon_0<\epsilon_1\le\cdots\) be the finite even eigenvalues. The
recorded quantities are

\[
\rho=\langle\widehat w,A\widehat w\rangle,\quad
r=\|(A-\rho)\widehat w\|,\quad
\sigma=\epsilon_1-\rho.
\]

The index 1 refers to the **second even eigenvalue**, not the least odd level.
The residual implementation in the audit requires \(\sigma>0\). We record a
null residual/separation ratio when this condition fails, rather than using
the absolute value of a negative denominator.

No zeta zeros enter the builder or candidate. A separate check compares
normalized Fourier integrals of k at real arguments 1, 5 and 10 with the
analytic completed zeta expression, not with a zero list.

## Bounded observations

The initial run used 90 decimal digits. Only X=13,N=32 and X=29,N=32 were
repeated at 130 digits, together with one additional X=13,N=64 cutoff.

| X | N | Candidate Rayleigh rho | Second even epsilon_1 | Residual r | Full candidate-ground L2 distance | Ground half-second-moment |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 8 | 1.20877e-8 | 5.56333e-10 | 9.72373e-5 | .0530991 | .0195364 |
| 5 | 16 | 9.26433e-9 | 9.78005e-12 | 1.05121e-4 | .0646235 | .0188443 |
| 13 | 8 | 1.91245e-10 | 9.62368e-18 | 1.12620e-5 | .100891 | .0310630 |
| 13 | 16 | 1.08539e-22 | 4.34408e-29 | 5.13609e-12 | .0193508 | .0244875 |
| 13 | 32 | 7.85968e-29 | 1.01007e-42 | 7.76813e-15 | .0150644 | .0220459 |
| 13 | 64 | 6.05698e-29 | 2.58785e-51 | 8.71993e-15 | .0225145 | .0215400 |
| 29 | 16 | 6.86367e-17 | 1.08424e-37 | 8.38201e-9 | .104961 | .0316369 |
| 29 | 32 | 1.59037e-35 | 2.60182e-61 | 3.36141e-18 | .0334808 | .0255912 |

The candidate's full limiting half-second-moment is
\(0.0231049931154189707889\ldots\). Here a ground “moment” means the
signed ratio \(\frac12\int x^2u/\int u\), not a probability variance.
The exact Fourier-coefficient formula from the audit is used. The least even
level is below the least odd level in all these finite observations; no
infinite-dimensional ground-ordering theorem follows.

At X=13,N=32 the candidate Fourier projection tail is only 1.891e-15, against
a profile distance .01506. At N=64 the tail decreases to 8.863e-16 while the
profile distance increases to .02251. At X=29,N=32 the tail is 3.919e-18 while
the profile distance is .03348. Thus simply resolving this particular
candidate more accurately is not what limits these comparisons.

The X=13 moment first moves toward the Xi moment, then crosses below it, and
continues downward between N=32 and N=64. Neither apparent earlier agreement
nor the later drift establishes a limit. These supports and cutoffs were
selected to test the comparison mechanism, not to fit an asymptotic law.

## Why the ordinary residual is misleading here

Expand \(\widehat w=\sum_j c_ju_j\) in the actual finite even eigenbasis.
The programs retain the first four weights \(p_j=|c_j|^2\) and reconstruct

\[
r^2=\sum_j(\epsilon_j-\rho)^2p_j,\qquad
\rho=\sum_j\epsilon_jp_j.
\]

| X,N | Ground weight p_0 | Second-even weight p_1 | Weight outside first four | Fraction of r² from first four |
|---|---:|---:|---:|---:|
| 13,32 | .9997730774 | .0002268383 | 1.11045e-13 | 1.02371e-28 |
| 13,64 | .9994931625 | .0005065312 | 6.15744e-13 | 4.82489e-29 |
| 29,32 | .9988793469 | .0011190998 | 1.18275e-11 | 2.23848e-35 |

The first four modes contain almost the entire vector, yet essentially none
of its ordinary residual squared. At X=13,N=32 those modes contribute only
1.16034e-13 of the Rayleigh value. Small coefficients in the other retained
even modes dominate the residual and Rayleigh value. The actual angular
error is instead predominantly a rotation toward the second even mode.

The “remainder” in this table is the rest of the **finite even matrix**,
j=4,...,N. It is not the uncomputed infinite Fourier complement. The records
separately give coupling norms to the next N Fourier rows; those are finite
diagnostics and not infinite-tail upper bounds.

This is a direct reason not to infer an eigenvector estimate from a small
absolute residual. It also explains why the blunt norm divided by the
second-even separation can be much less informative than the observed
overlap. A useful next calculation would eliminate or control a suitable
complement while retaining an explicit effective matrix on the weak even
cluster. The remaining task is then to prove its orientation toward the
candidate, not merely that it is a low-energy cluster. Choosing that cluster
from already known exact eigenvectors would be diagnostic only; a proof
needs an independently described trial space and a controlled remainder.

## Verification and limitations

1. The closed block formulas agree with defining-distribution quadrature for
   the selected small blocks, and the X=13 specialization agrees with the
   existing coefficients. All source identities are retained in the records.
2. The repeated observables and first four even eigenvalues agree to at least
   20 relative decimal digits. The worst relative difference is 1.603e-24 in
   the extremely small X=29,N=32 ground eigenvalue. The gate signs agree.
   Agreement of two precisions sharing formulas is not interval certification.
3. Independent candidate controls check the direct arithmetic series at
   positive and negative x. Evenness and the normalized Fourier/Xi values
   agree to about 1e-71. The integral half-second-moment and analytic Xi
   derivative agree to 2.35e-71. These quadratures and their very small
   superexponential tails are not interval-enclosed.
4. Matrices existed only in memory. The repository was read-only; bytecode
   generation was disabled. Only scripts, compact JSON and this note were
   written to the task workspace.
5. No positive form approximation, continuum spectral gap, simple-even
   all-support theorem, prolate comparison, or RH conclusion is established.

## Files and reproduction

- `../numerics/ground-selection-20260928/check_xi_ground_comparison.py`: portable generator; requires
  mpmath and the existing CCM builders.
- `../numerics/ground-selection-20260928/check_xi_candidate_normalization.py`: independent normalization
  controls using the analytic Xi formula.
- `../numerics/ground-selection-20260928/summarize_xi_ground_comparison.py`: verifies original source
  hashes and reports relative precision agreement and eigenbasis splits.
- `../numerics/ground-selection-20260928/xi-ground-comparison-90.json` and
  `../numerics/ground-selection-20260928/xi-ground-comparison-130.json`: compact observations.
- `../numerics/ground-selection-20260928/xi-ground-comparison-summary.json`: eigenbasis and precision
  summary.
- `../numerics/ground-selection-20260928/xi-candidate-normalization.json`: candidate controls.
- `../numerics/ground-selection-20260928/portable-source-verification.json`: unchanged mathematical
  function syntax between the original generator and portable revision.
- `../numerics/ground-selection-20260928/run-sources/`: exact historical generator, dependency sources
  and original record bytes. These preserve the original hashes; they are not
  the current replay entry points.

The current generator defaults to finding `check_mass_stiffness.py` and
`check_odd_blocks.py` beside itself. While staged separately, use
`--repo-numerics /path/to/repository/papers/investigations/ccm-operator-realizations/numerics`.
Install mpmath normally or expose its installation through PYTHONPATH; the
portable scripts contain no machine-specific dependency path.

Example replay, from this investigation’s `numerics/ground-selection-20260928/` directory (the existing builders are one directory above):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B check_xi_ground_comparison.py --repo-numerics .. --digits 90 --case 5,8 --case 5,16 --case 13,8 --case 13,16 --case 13,32 --case 29,16 --case 29,32 --output fresh-90.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_xi_ground_comparison.py --repo-numerics .. --digits 130 --case 13,32 --case 13,64 --case 29,32 --output fresh-130.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_xi_candidate_normalization.py --repo-numerics .. fresh-normalization.json
```

The portable revision changes dependency discovery, CLI options and model
metadata, not coefficients, candidate integrals, eigenproblem, or observations.
Its help path and candidate normalization control were replayed after the
revision. The expensive eigenvalue diagnostics remain bound to their
preserved original run version; no unchanged eigensolve was repeated solely
because packaging changed.
