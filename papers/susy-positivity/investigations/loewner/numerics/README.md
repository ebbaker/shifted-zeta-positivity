# Checks and records

Registered check programmes: standard library only, JSON to standard output, a
preserved record under [`records/`](records/), and registration in the `CHECKS`
dictionary of [`validation/drafts.py`](../validation/drafts.py), so that
`python3 validation/drafts.py check --replay` re-runs each one and requires
byte-identical output.

| Programme | Preserved record | Scope |
|---|---|---|
| [check_contraction_margin.py](check_contraction_margin.py) | [contraction-margin-checks.json](records/contraction-margin-checks.json) | The elementary assembly of the compressed transfer $V_{\omega,L}$ and its contraction data, in double precision. 53 cases in six groups: the Gauss--Jacobi and Gauss--Legendre rules against exact moments and the closed-form sine autocorrelations $S_{jk}$ against quadrature; the kernel by two independent routes and against the **exact Laplace transform** $\pi^\omega\Gamma(\frac{a+p}2)/\Gamma(\frac{b+p}2)\cdot\frac{(p+a)(p-b)}{(p+b)(p-a)}$ ($\Gamma$ alone --- no $\zeta$, no $\xi$, no zeros); the mass $\int_0^Lk_\omega$ at $L=\log3,\log5,\log7$ and its first-order limit against the closed form of the contraction-margin note's Proposition 2.3; contraction $\lVert V\rVert<1$ and $\lambda_{\min}(I-V^{\mathsf T}V)/2\omega=m_L^{(24)}(1+\delta)$ with $\lvert\delta\rvert<1\%$ at $\omega=0.01$, against the localized Weil form assembled in closed form in the same basis; the first-order law on $e_1$ at all three horizons; and the cumulative Cayley coordinate (the congruence, accretivity, and the quadratic gap to the defect). About one second; `python3 numerics/check_contraction_margin.py`. |
| [check_beta_realization.py](check_beta_realization.py) | [beta-realization-checks.json](records/beta-realization-checks.json) | What a radial Loewner chain would have to produce for the archimedean factor, and why it cannot. 43 cases in five groups: the archimedean delay identified pointwise as $\tau=-\frac12\log U$ with $U\sim\mathrm{Beta}(\frac a2,\omega)$, with its zero-delay exponent and the dual power law $\mathbb E[U^q]\sim q^{-\omega}$; the exact factorization $\mathbb E[U^qS^r]=\mathbb E[U^q]\mathbb E[S^r]$ saying the additivity fraction is independent of the total; the chord diffusion of a radial chain and its speed density, whose antipodal exponent is $-\frac12$ for every driving while the swallowing exponent is free; the resulting exclusion of the target parameters on $0<\omega<\frac12$, and the three Bessel dimensions against the SLE range; and the horocycle representation $K^\Gamma_\omega(p)=\int_{\mathbb R^{2\omega}}\lvert t+i\rvert^{-(p+b)}dt$, with the Riesz integral checked by honest quadrature at integer dimension and the kernel prefactor against the area of $S^{2\omega-1}$. Uses $\Gamma$, $\sinh$ and elementary algebra only --- no $\zeta$, no $\xi$, no zeros. Under a second; `python3 numerics/check_beta_realization.py`. |

The first programme is self-contained: complex digamma and trigamma, Gauss--Jacobi
nodes by Golub--Welsch on the closed-form Jacobi recurrence, Gauss--Legendre by
Newton on the Legendre polynomials, a cyclic Jacobi symmetric eigensolver and
Gaussian elimination are all written out. What makes double precision possible
is that the spike $\tau^{\omega-1}$ of the kernel sits in the *quadrature
weight* and never in an evaluated quantity (see
[the note of 18 September](../notes/REGISTERED_ASSEMBLY_AND_THE_HORIZONS_20260918.md),
Proposition 1.1).

What double precision cannot carry is recorded in the programme's own output:
$\lambda_{\min}(D)\approx2\omega m_L$ is $10^{-9}$ at $L=\log3$ and about
$10^{-17}$ and $10^{-22}$ at $\log5$ and $\log7$, so the margin check is made at
$\log3$ only, and the higher horizons are asserted here through the mass and the
first-order law on a fixed vector, both $O(10^{-4})$, with the margin left to
[`exploratory/`](exploratory/README.md) at 40--90 digits.

Counts refer to finite test cases, not independent theorems, and no check here
is a positivity certificate.
