# Certified Hubbard heat trial and its cost limitation

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol** (Codex); reasoning effort **ultra**.
This is an internal derivation and reproducible bounded benchmark. No
literature novelty, scalable computational advantage, or theta consequence
is claimed.

The first quantum gate in the [initial program](INITIAL_RESEARCH_PROGRAM_20261014.md)
can now be decided. A finite-time integral of explicitly declared
one-body heat trajectories gives a genuine correlated trial state in a
small interacting fermion sector. A computable positive-interaction
residual estimate certifies an energy below every sector-preserving
single Slater determinant. The same-family direct Rayleigh calculation is
more accurate and cheaper in the representation used here. Therefore the
certificate is useful, but this implementation does **not** justify a
computational-advantage claim or expansion to larger systems.

## 1. A correction bound that uses the surrogate generator

Work in a finite-dimensional complex Hilbert space with the usual
Hermitian inner product. Let B=B* >= beta I, beta>0, and let
A=B+V, where V=V* >=0. Assume that all nonzero eigenvalues of V are at
least nu>0. Set

\[
 u(t)=e^{-tB}\rho,\quad
 \Psi=\int_0^T u(t)\,dt,\quad
 r(t)=u'(t)+Au(t)=Vu(t),\quad
 R=\int_0^T r(t)\,dt=V\Psi,
\]

and Q0=int_0^T ||u(t)||²dt, Q1=int_0^T t||u(t)||²dt.
This is exact evolution for a declared surrogate B, and approximate
evolution for A. It is a restricted subclass of the arbitrary paths in
[the finite-time seed theorem](RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md).
It does not silently replace a time-dependent mean-field path by a
fixed-generator path.

Define

\[
 \ell=\sqrt{4Q_1}-\frac{\|u(T)\|}{\beta}.
\]

If ell>0, then

\[
 \boxed{
 \inf\sigma(A)\le
 \frac{\langle\Psi,A\Psi\rangle}{\|\Psi\|^2}
 \le \frac{2Q_0+\|R\|^2/\nu}{\ell^2}.}
 \tag{1}
\]

**Proof of the denominator.** Put S=B^{-1}rho. Spectral calculus gives
4int_0^infty t||u(t)||²dt=||S||², so ||S||>=sqrt(4Q1).
The exact terminal identity is Psi=S-B^{-1}u(T). Consequently

\[
 \|\Psi\|\ge\|S\|-\|B^{-1}u(T)\|
 \ge\sqrt{4Q_1}-\|u(T)\|/\beta=\ell.
\]

This step uses only a bound on the inverse, not a many-body inverse solve.
The strict condition ell>0 is necessary before squaring this lower bound.

**Proof of the numerator.** The exact B-flow satisfies

\[
 E_B:=\langle\Psi,B\Psi\rangle
 =2Q_0-2\operatorname{Re}\langle\Psi,u(T)\rangle\le2Q_0.
\]

The last inequality follows from spectral calculus: the endpoint overlap
is a sum/integral of nonnegative weights
(1-e^{-Tlambda})e^{-Tlambda}/lambda.
Also V<=V²/nu by its known positive spectral gap. Thus

\[
 \langle\Psi,V\Psi\rangle\le\|V\Psi\|^2/\nu
 =\|R\|^2/\nu.
\]

A>=B>0, so an upper numerator and positive lower denominator give (1).
For A=H+E_s I, subtract E_s from the quotient and upper bound.
The final relation

\[
 A\Psi=\rho+R-u(T)
\]

retains the endpoint that the uncorrected diagonal approximation loses.

This estimate does not require V to commute with B. It does require a
known gap in the positive spectrum of V. An arbitrary signed interaction
or a continuum positive potential whose spectrum accumulates at zero
does not satisfy the displayed hypothesis. For repulsive finite-lattice
Hubbard interaction V=U sum_i n_{i up}n_{i down}, the nonzero eigenvalues
are integer multiples of U, so nu=U is available. In the dimer sector
below V=UP for a projection P, and the stronger identity

\[
 \langle\Psi,V\Psi\rangle=\|R\|^2/U
 \tag{2}
\]

holds exactly. Equation (2) is elementary projection algebra, not a
novelty claim.

One can replace ||R|| by int||r(t)||dt in (1). This generally loses
cancellation and requires its own rigorous integration. We instead
accumulate the residual vector explicitly and count that work.

## 2. A declared interacting fermion model and trial family

Use a two-site Hubbard model with hopping 1, repulsion U=4, and the fixed
sector N_up=N_down=1, hence N=2. The four-dimensional basis is
(L_up L_down, L_up R_down, R_up L_down, R_up R_down). In this tensor
ordering,

\[
 H_0=\begin{pmatrix}
 0&-1&-1&0\\-1&0&0&-1\\-1&0&0&-1\\0&-1&-1&0
 \end{pmatrix},\quad
 V=\operatorname{diag}(4,0,0,4),\quad H=H_0+V.
\]

Choose the common energy shift E_s=3 and time T=6. Then
B=H0+3I has eigenvalues 1,3,5 (3 has multiplicity two), so beta=1.
A=H+3I>=B>=I. The exact ground energy of H in this sector is

\[
 E_0=2-2\sqrt2=-0.828427124746190\ldots.
\]

The initial family is the unnormalized product Slater state
rho(p,q)=(1,p)_up tensor (1,q)_down. A parameter infinity denotes the
localized orbital (0,1); finite parameters denote (1,p). Overall
normalization cancels in all the quotient comparisons. Every time slice
remains a Slater determinant:

\[
 u(t)=e^{-3t}
 (e^{t\sigma_x}a)_\uparrow\otimes
 (e^{t\sigma_x}b)_\downarrow.
\]

Its time integral Psi generally has Schmidt rank two, which provides the
correlation absent from a single product determinant.

Every compared method uses the same initial family, sector, shift, T,
three surrogate spectral modes, and analytic exponential integrals. The
169 common candidates are all pairs from

\[
 \{0,1/8,1/4,3/8,1/2,3/4,1,4/3,2,8/3,4,8,\infty\}.
\]

The extra direct-variational budget experiment uses additional rational
points in the same continuous family; it does not change the trajectory
or state representation. No grid result is claimed globally optimal
within the integrated family.

## 3. Integration and certification

This small model admits exact exponential moments, so no method uses a
sampled time quadrature. Let P_lambda be the rational spectral projector
of B and v_lambda=P_lambda rho. Then

\[
 \Psi=\sum_\lambda f_\lambda v_\lambda,
 \quad f_\lambda=(1-e^{-\lambda T})/\lambda,
 \quad u(T)=\sum_\lambda e^{-\lambda T}v_\lambda,
 \quad R=\sum_\lambda f_\lambda Vv_\lambda.
\]

Orthogonality gives

\[
 Q_0=\sum_\lambda\|v_\lambda\|^2
 \frac{1-e^{-2\lambda T}}{2\lambda},\qquad
 Q_1=\sum_\lambda\|v_\lambda\|^2
 \frac{1-(1+2\lambda T)e^{-2\lambda T}}{4\lambda^2}.
\]

These are common analytic integrals; there is no discrepancy in time
quadrature between the methods. The selected-state enclosure-width target
is 10^{-25}. The script uses only Python's standard library. Exact
rational alternating-series bounds of degrees 31 and 32 enclose e^{-1};
positive integer powers enclose every required exponential. Exact
rational interval operations and integer square-root enclosures propagate
the bounds outward. The selected Rayleigh and residual-upper enclosures
are narrower than 10^{-25}. The floating-point candidate scan is labeled
numerical; it selects states that are then checked with rational intervals.

The script checks both original finite-time energy/norm identities
and the terminal relation with the interacting residual, and evaluates
the original generic Cauchy estimates using
analytical moments of the vectors u, U and d. Their failure at the two
selected states is rigorous. The diagnostic that every grid denominator
is negative is a floating-point observation, not a whole-grid certificate.
No quadrature truncation, undocumented library precision, or eigenvalue
fit is used in the selected-state certificate.

## 4. Results and variational meaning

All energies in this table have the shift 3 subtracted. Site-reflected
localized states have the same result.

| Criterion on the same 169 candidates | Selected initial state | Reported energy | Actual integrated-state Rayleigh |
| --- | --- | ---: | ---: |
| Uncorrected 2Q0/(4Q1)-3 | p=q=1 | -1.999926263562080 | 0 exactly |
| Direct Rayleigh of Psi | p=infinity, q=0 | -0.507461853237753 | -0.507461853237753 |
| Endpoint and positive-interaction residual upper (1) | p=0, q=infinity | -0.502153976126777 | -0.507461853237753 |
| Generic seed-note Cauchy upper | same localized state | unavailable: denominator <0 | -0.507461853237753 |

The uncorrected criterion is below the exact ground energy. Its optimizer
is a particularly strong failure: the integrated state has energy zero,
although the diagonal criterion approaches the free hopping energy -2.
The rational interval record certifies the bound violation at that state.

For the localized state, the record certifies

\[
 -0.50746185323775255650394405705
 \le E(\Psi)\le
 -0.50746185323775255650394405704,
\]

and an upper endpoint of (1) of

\[
 E(\Psi)\le
 -0.50215397612677637283871231969 < -\tfrac12.
\]

The norm-squared lower bound is 0.3141447445033797; the actual norm
squared is 0.3143177138280889. The generic Cauchy denominator
4Q1-delta_N lies below -1.1322207435500161 at this same state. The
structure of the positive interaction and known surrogate generator
therefore matters: a generic defect estimate need not be usable even
when a more specific residual estimate is useful.

The comparison with all single Slater determinants is analytical, not a
grid inference. For normalized sector-preserving product orbitals, let
z and w be their site polarizations. Optimizing their phases makes their
kinetic contributions -sqrt(1-z²) and -sqrt(1-w²). With U=4,

\[
 E=-\sqrt{1-z^2}-\sqrt{1-w^2}+2(1+zw).
\]

For fixed z, minimizing over w gives 2-s-sqrt(5-4s²), where
s=sqrt(1-z²) is in [0,1]. Since

\[
 (\tfrac52-s)^2-(5-4s^2)=5(s-\tfrac12)^2\ge0,
\]

E>=-1/2. Equality is attained at s=1/2 with opposite polarizations.
Complex phases cannot improve the phase-minimized kinetic contribution.
Thus the certified heat-integrated trial beats every single product
Slater state in the declared fixed-spin sector. Its distance from the
exact correlated ground energy remains large; the small strict
improvement does not establish good many-body accuracy.

## 5. Actual residual and overlap work

The candidate scans instrumented vector/mode multiplication and addition
counts; the selected-state exact rational certification checks are
additional verification work and are not included in this scan metric.
The counts include initial tensor construction, nonzero matrix entries,
vector combinations and dot products. Surrogate projectors and exponential
coefficients are precomputed identically for all methods. The metric
excludes scalar post-processing divisions and square roots; the latter
are separately counted. It is an operation comparison, not a timing
benchmark or a hardware-independent cost model.

| Same 169 candidates | Dot products | Full H actions | V actions | Surrogate projector actions | Vector/mode multiply+add work | Square roots |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Uncorrected diagonal criterion | 507 | 0 | 0 | 507 | 17,407 | 0 |
| Direct integrated-state Rayleigh | 338 | 169 | 0 | 507 | 20,618 | 0 |
| Residual enclosure (1) | 845 | 0 | 507 | 507 | 27,547 | 338 |

A V action is cheaper than a full H action here; they are not assigned
identical prices. Their nonzero scalar operations enter the same counted
metric. The enclosure requires accumulating all three residual modes
Vv_lambda, the terminal vector and their norms. Direct evaluation forms
Psi once, applies H once, and computes two overlaps. Recomputing a
correction is not charged as free residual information.

At the residual method's 27,547-unit budget, direct variational evaluation
uses 27,450 units for 225 initial candidates from the same continuous
Slater/path family. Each direct evaluation costs 122 counted units; the
budget is checked before executing a candidate, so no rejected final
evaluation is hidden outside the budget. It finds the same numerical minimum
-0.507461853237753, with a tighter certified evaluation of the same state.
Ignoring scalar square-root costs favors the residual estimator, so that
omission cannot explain a hidden cost advantage for it. No wall-clock
performance claim follows from this chosen metric.

The compact four-dimensional Fock representation is deliberately common
to all methods. In a determinant-list representation at larger particle
number, forming R=Vsum_i w_i u_i and its squared norm requires residual
cross overlaps. A norm of a sum cannot be replaced by the sum of norms
without changing the estimate. Direct Rayleigh evaluation also has
cross overlaps. This experiment does not establish a reduction from
quadratic overlap work to linear work in either representation. Applying
V to a determinant also need not preserve its single-determinant form.
Those costs must be counted in any attempted extension.

## 6. Bounded decision and deliverables

The quantum initial-program gate passes through a useful certified bound
and a sharp limitation. The interaction-specific estimate (1) gives a
rigorous energy below the full product-Slater optimum. Direct variational
evaluation in the same state family wins the tested work comparison.
Do not expand this implementation merely to reproduce direct Rayleigh
work through residuals. A future quantum-method claim would require an
approximation and representation in which a correction can be certified
at lower total cost, as well as comparison with existing methods.

Reproduction after installation in the investigation:

```bash
python3 numerics/hubbard_heat_benchmark.py
```

Deliverables are the standard-library
[script](../numerics/hubbard_heat_benchmark.py) and its small
[rational certificate and work record](../numerics/HUBBARD_HEAT_BENCHMARK_20261014.json).
The record contains the script SHA-256, exact parameters, selected-state
intervals and arithmetic counts. A matching hash identifies a source
snapshot; the mathematical decisions come from the exact rational
inequalities and do not depend on a hash. All files remain well below the
repository's large-file limit. This is not a manuscript or a new snapshot
folder, and it makes no positivity inference for stationary Laguerre
forms or backward Newman time.
