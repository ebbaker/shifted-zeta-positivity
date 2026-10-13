# Numerics Lab — Results (Aug 17, 2026)

Code: `lab/xi_lib.py` (library), `lab/run_experiments.py` (experiments), figure `lab_results.png`.
Stack: numpy / mpmath / scipy. Everything below reproduces in ~3 minutes.

## Validation

* $\Xi(x) = 4\int_0^\infty \Phi(u)\cos(xu)\,du$ (Pólya's $\Phi>0$, 6 theta terms, trapezoid $du=5\cdot10^{-5}$)
  matches $\xi(\tfrac12+ix)$ computed independently via mpmath ($\Gamma$, $\zeta$) to ~10 digits at
  $x=0,5,20,30$, and vanishes at the first zero ordinate $x=14.134725\ldots$ ($|\Xi|\sim10^{-18}$).
* Davenport–Heilbronn: $\Xi_{DH}(z)=\Lambda_{DH}(\tfrac12+iz)$, built from the odd character mod 5
  ($\chi(2)=i$) via Hurwitz zeta, with $\kappa=(\sqrt{10-2\sqrt5}-2)/(\sqrt5-1)$. Verified real and even
  in $z$ to $10^{-21}$. Newton iteration recovers the classical **off-line zeros** (zero spheres, in
  rotated coordinates $(a; y_0)$ = center; radius):

  | $s$ (critical strip) | sphere center $a$ | sphere radius $y_0$ |
  |---|---|---|
  | $0.808517182 + 85.699348485\,i$ | 85.699348 | 0.308517 |
  | $0.650830081 + 114.163342686\,i$ | 114.163343 | 0.150830 |
  | $0.574356050 + 166.479305\,i$ | 166.479306 | 0.074356 |

## Experiment 1 — Laguerre positivity for $\Xi$ (function data only)

$L_1[\Xi](x) = \Xi'(x)^2 - \Xi(x)\Xi''(x)$, all three functions from the (positive) cosine transform.
Result: **relative $L_1 \ge 0.173$ on $[0,52]$** (normalized by $\Xi'^2+|\Xi\Xi''|$); beyond $x\approx55$
the float64 quadrature floor ($|\Xi'|\sim10^{-18}$, $L_1\sim10^{-34}$) is reached — no verdict there
without high-precision quadrature, which mpmath can supply if ever needed. As expected for the real
Riemann $\Xi$: no dips.

## Experiment 2 — the zero spheres of DH are visible from the axis

$L_1[\Xi_{DH}]$ computed on grids around the first two spheres (after the sign-preserving exponential
rescaling $F \mapsto e^{\pi x/4}F$, which leaves $\mathrm{sign}\,L_1$ invariant since $L_1[e^{cx}]\equiv0$):

* Sphere $(a,y_0)=(85.699,\,0.3085)$: $L_1<0$ exactly on $[85.417,\,85.982]$ — predicted window
  $|x-a|<y_0$ is $[85.391,\,86.008]$. Observed window sits just inside the prediction, as theory
  requires (the negative pair term $2\,\mathrm{Re}(x-z_0)^{-2}$ is exactly negative on $|x-a|<y_0$; the
  positive contributions of all other zeros shave the edges).
* Sphere $(114.163,\,0.1508)$: $L_1<0$ on $[114.025,114.302]$, predicted $[114.013,114.314]$. Same
  agreement.
* Control stretch $[78,82]$ (only on-line zeros nearby): $L_1 > 0$ throughout (min $\approx 7\cdot10^2$
  in rescaled units).

**Interpretation.** The acnode/crunode (σ-swapped vs σ-fixed ruling) dichotomy of the twistor picture
has an axis-visible certificate, and it is *quantitative*: a zero sphere of radius $y_0$ forces
$L_1<0$ on an interval of length $\approx 2y_0$ centered at its projection. This is the $\ell$-lowest
member of the graded hierarchy, computed purely from boundary (axis) data — no knowledge of zero
locations used.

## Experiment 3 — sector energies scale as $y_0^{2\ell}$

Zero set: first 20 Riemann ordinates (real) + one implanted sphere at $a=28$, radius $y_0$ swept over
$[10^{-3}, 10^{-0.5}]$. Sector energies
$\mathcal{E}_\ell=\int_0^2\big|\sum_\rho j_\ell(\lambda y_\rho)e^{i\lambda a_\rho}\big|^2 e^{-\lambda^2}d\lambda$:

* Real zeros contribute **exactly zero** to every $\ell\ge1$ sector ($j_\ell(0)=0$): measured
  $\mathcal{E}_1(\text{20 real zeros only})=0$ to machine precision.
* Log–log slopes of $\mathcal{E}_\ell$ vs $y_0$: **2.000, 4.000, 6.000** for $\ell=1,2,3$ — the predicted
  $y_0^{2\ell}$ law from $j_\ell(\lambda y_0)\sim(\lambda y_0)^\ell/(2\ell+1)!!$.
* On real data: DH's three spheres give per-sphere $\mathcal{E}_1 = 4.36\cdot10^{-3},\ 1.06\cdot10^{-3},\
  2.59\cdot10^{-4}$ — ratios 4.11 and 4.10 vs the $(y_0/y_0')^2$ predictions 4.18 and 4.11. ✓

**Interpretation.** The $\ell$-grading works exactly as designed: sector $\ell$ detects spheres with
sensitivity $y_0^{2\ell}$, real zeros are invisible in all $\ell\ge1$ sectors, and the $\ell=1$ level has the
same $y_0^2$ scaling as the axis Laguerre dip depth — consistent with the identification of Laguerre
positivity as the bottom of the graded family. The polynomial (not exponential) decay in $y_0$ is the
quantitative face of "RH is barely true" ($\Lambda\ge0$): near-axis spheres emit an arbitrarily weak
but *never zero* signal, so a successful positivity proof must control these functionals to all orders
— which is exactly where the arithmetic (explicit formula / $\Phi>0$ / Euler product) must enter, since
DH shows symmetry alone permits the signal to be present.

## What is established vs. what is a heuristic

Established numerically here: the detector pipeline end-to-end; the window law $|x-a|<y_0$ on real DH
data; the $y_0^{2\ell}$ grading; the vanishing of $\ell\ge1$ sectors on real zeros (this last is exact by
construction, not an experiment). Heuristic, promoted to the top of the research queue: an
*independent* expression for the $\ell\ge1$ sector energies in terms of $\Xi$/prime data (explicit
formula), so that their vanishing can be attacked rather than merely observed.
