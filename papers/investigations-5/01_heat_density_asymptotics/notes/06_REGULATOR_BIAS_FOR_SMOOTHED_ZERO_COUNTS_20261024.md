# Regulator bias for a smoothed zero-counting function

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.


**Status:** a conditional local error bound is derived in-note, including
multiple zeros. The theta-dependent lower bounds have not been supplied
numerically. This advances HDA-02 to partial; it does not establish that
the pilot regulator is small enough to represent smoothed zero counts.

## 1. An exact bridge at fixed time

Let \(H\) be holomorphic and not identically zero on a neighborhood of
the full spatial averaging buffer. Its zero measure is
\(\nu=\sum_a m_a\delta_a\). For a compactly supported \(C^2\) spatial
kernel \(K\), define
\[
R_\epsilon(z)=\int K(z-w)\rho_\epsilon(w)\,dA_w,
\qquad R_0(z)=\sum_a m_aK(z-a).
\]
These are unnormalized averages. At zeros, the locally integrable
logarithm is interpreted distributionally. The source manuscript's
[density identity and divisor limit][book], equations
`eq:lapdensity` and `eq:divisor`, give
\[
\rho_\epsilon-\nu
 =\frac1{4\pi}\Delta B_\epsilon,\qquad
B_\epsilon=\log\left(1+\frac{\epsilon^2}{|H|^2}\right). \tag{1}
\]
One can also verify the divisor term directly: near a zero,
\(\log|H|^2=2m\log|w-a|+\log|g(w)|^2\), with nonvanishing
holomorphic \(g\); the second term is harmonic and
\(\Delta\log|w-a|=2\pi\delta_a\).

Move the derivatives onto the kernel:
\[
\boxed{R_\epsilon(z)-R_0(z)
=\frac1{4\pi}\int (\Delta K)(z-w)B_\epsilon(w)\,dA_w.} \tag{2}
\]
Compact support removes boundary terms. Unlike a direct comparison of
individual peaks, (2) asks for an integrated logarithmic error. For any
buffer \(D\) containing the shifted kernel support,
\[
|R_\epsilon(z)-R_0(z)|
\le\frac{\|\Delta K\|_\infty}{4\pi}
       \int_D B_\epsilon(w)\,dA_w. \tag{3}
\]
This is often a conservative bound because it discards cancellation in
\(\Delta K\). Its benefit is an explicit route to average-shape error.
For \(K_h(w)=h^{-2}K(w/h)\), the displayed kernel norm scales as
\(h^{-4}\), so shrinking smoothing and removing the regulator together
require a separate error budget.

## 2. Explicit local rates, with all lower-bound inputs exposed

Cover the zeros in \(D\) by disjoint disks of radii \(r_j\), contained
in the holomorphic domain. Suppose throughout disk \(j\),
\[
|H(w)|\ge c_j|w-a_j|^{m_j},\qquad c_j>0,
\]
and on the remaining compact set \(D_{\rm out}\),
\(|H|\ge b>0\). These constants are supplied data, not consequences of
an observed density plot. Put \(a_{\epsilon,j}=(\epsilon/c_j)^{1/m_j}\).
Then
\[
\int_D B_\epsilon\,dA
\le |D_{\rm out}|\frac{\epsilon^2}{b^2}
 +\sum_j I_{m_j}(a_{\epsilon,j},r_j),\quad
I_m(a,r)=2\pi\int_0^r s\log(1+(a/s)^{2m})\,ds. \tag{4}
\]
Disks extending outside \(D\) only enlarge this upper bound.

For a simple zero, direct integration gives
\[
I_1(a,r)=\pi\{r^2\log(1+a^2/r^2)
             +a^2\log(1+r^2/a^2)\}
\le\pi a^2\{1+\log(1+r^2/a^2)\}. \tag{5}
\]
For \(m\ge2\), extend the integral to infinity, split at \(a\), and
use \(\log(1+x)\le x\) outside that radius and
\(\log(1+(a/s)^{2m})\le\log2+2m\log(a/s)\) inside. This yields
\[
I_m(a,r)\le\pi a^2\left(m+\log2+\frac1{m-1}\right). \tag{6}
\]
The elementary bound is adequate here; no optimal constant is claimed.
Equations (3)–(6) prove an \(O(\epsilon^2\log(1/\epsilon))\)
local error at simple zeros and \(O(\epsilon^{2/m})\) at an order-\(m\)
zero, for fixed kernel and fixed lower-bound data. The bound retains
multiplicity and remains compatible with double events. It does not
assume all zeros are simple or real.

## 3. Time averaging and what is still missing

For a nonnegative unit-mass temporal kernel \(g_\tau\), apply (2) at
each sampled time and integrate it. The exact spacetime error bound is
\[
|\mathcal F\rho_\epsilon-\mathcal F\nu|
\le\frac{\|\Delta K\|_\infty}{4\pi}
\int g_\tau(s)\left[\int_D B_\epsilon(t-s,w)\,dA_w\right]ds. \tag{7}
\]
For a uniform power-rate conclusion from (4)–(6), the disk cover,
lower-bound constants and multiplicity description must be controlled
through the time buffer. Simple-zero constants can degenerate as zeros
merge, so a fixed-time rate must not be promoted to a uniform temporal
one. A cluster formulation or direct bound on the integral in (7) is
preferable near changing multiplicity. Pure time averaging with no
smooth spatial kernel is outside (2)–(7).

The negative-time compact limit has no zeros but a nonzero regularized
background, as [Note 05][limits] shows. In that limit \(|H|\) becomes
small, so the lower bound \(b\) is not uniform in \(T\). Removing
\(\epsilon\) first and taking \(T\to\infty\) at fixed \(\epsilon\)
are different asymptotic descriptions. The integral bound may be loose
there because a large nearly constant logarithmic offset is annihilated
by \(\Delta K\).

Next, pay at least one actual theta instance of (3) or (7), preferably
with contour/cluster lower bounds or a direct logarithmic-integral
estimate. A sequence of smaller regulators can diagnose convergence,
but successive differences alone are not a certified tail estimate.
The current 17-case pilot measures the regularized mean only. It has
not established a quantitative error against \(R_0\).

## 4. Scope and controls

This is a generic approximation bound, not an RH-equivalent condition
or a zero-exclusion mechanism. It applies equally to \(H=z^2-2t\)
and to the repository's [collision controls][controls] wherever its
explicit analytic and lower-bound premises hold. A double zero changes
the rate rather than invalidating or being excluded by the bound.
The unchanged theta data are needed to make its constants quantitative
for the intended source; no such constants are inferred from source
shape alone. See [target classification][classification] and
[unchecked-import discipline][imports].

[book]: ../../../investigations-4/12_height_dependent_heat_contours/manuscript/book.tex
[limits]: 05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../avoid/01_restating_the_target.md
[imports]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
