# Signed pair kernels and oscillation-preserving transformations: internal review

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. All derivations and cross-audits are
internal LLM work, not independent mathematical validation. No numerical
sweep, atlas extension, or mode sampling was used.

## 1. Outcome and dependencies

This continues the analytical signed primitive-ratio and product priority
identified after Heat Notes 20–21. It develops an actual candidate-paid
diagonal cancellation, a paid near-pair band, and two oscillation-preserving
transformation theorems. Their retained signed main terms are explicit;
their required opposite threshold sign is still unproved.

The saved notes are:

* [Project 09 Note 7](../newman_collisions/09_prime_phase_torus/notes/7_DIAGONAL_ANNIHILATING_PAID_KERNELS_AND_NEAR_PAIR_BOUNDS_20261010.md):
  extended candidate-null kernel, exact diagonal annihilation, and paid
  macroscopic near-pair bounds.
* [Project 09 Note 8](../newman_collisions/09_prime_phase_torus/notes/8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md):
  uniform finite Poisson/Fresnel formula and its globally paid product
  applications.
* [Project 09 Note 9](../newman_collisions/09_prime_phase_torus/notes/9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md):
  coupled primitive frontier, exact Möbius coefficients, and a global
  sublattice Poisson payment.
* [Heat Note 22](../newman_collisions/notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md):
  program synthesis and exact prescribed stationary weight, center, and
  carrier reflection identities.

The physical approximation, normalizer, raw-jet Bell residuals, and paid
candidate coordinates are those of existing Heat Note 8 and project 09
Notes 2–6. The density-strengthened coefficient and its recalculated
physical perturbation payment are imported from Heat Notes 20–21 and
project 09 Note 6. New formulas never turn an auxiliary-index derivative
into a raw spatial derivative or impose independent prime phases.

## 2. Candidate-paid diagonal cancellation

With the actual moments and drift-containing candidate coordinate, define
\[
\mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2,
\qquad Z_1=Y_1+\epsilon X_1.
\]
The extended complete dual is
\[
\mathcal J^\dagger=\mathcal K
+X_0(\Gamma X_4-3X_6+2\epsilon Y_6)-2Z_1Y_5.
\]
Its measured two-sided candidate payment can use
\[
\Pi^\dagger=
a_0|3X_6-\Gamma X_4-2\epsilon Y_6|+2a_1|Y_5|,
\]
where \(a_0,a_1\) are the actual paid bounds for \(X_0,Z_1\).
This is a sufficient payment, not a newly solved sharp one-sided optimizer.
For \(\Gamma=\Gamma_{\rm count}=O(L)\), its complete finite moment
envelope is \(O(L(Nw_N)\eta_N)=O(LN^{-\kappa/4})\).

All four ordered-pair coefficients vanish at equal indices. The cosine
coefficients contain \(h^2\delta^2\), where
\(h=\rho_n+\rho_m\) and \(\delta=\rho_n-\rho_m\).
The two small drift sine terms remain, with their exact orientations.
The degree-six null additions use higher finite features than the earlier
five-feature dual. They do not contradict Note 6's degree obstruction,
which concerned that earlier feature space, and they do not identically
annihilate the complete sixth-degree kernel. They annihilate its diagonal.

The finite \(X_6,Y_5,Y_6\) moments are exactly defined from the prescribed
coefficients. Their weighted moment bounds are sufficient for the null
payment; no genuine fifth or sixth spatial-jet approximation is needed.
The original threshold approximation payment still concerns raw jets
through order four and must use the chosen normalizer coefficient.

On a fixed macroscopic index range, the band \(|n-m|\le H\) has
absolute cosine payment
\[
O((1+|\Gamma|)w_N^2H^3/N),
\]
and drift sine payment at most \(O(|\epsilon|w_N^2H^2)\).
For \(H\asymp\sqrt N\), the cosine payment is
\(O(LN^{-1/2-\kappa/4})\) with the density normalizer; the drift
payment is smaller because \(\epsilon=O(t/N^2)\).
The bound can include the near-boundary mixed block/complement pairs by
working on \([N/4,N]\). It is not a bound for the full complement or
for all separated pairs. Those terms remain in the complete arithmetic sum.

## 3. Uniform product transformation

Note 8 proves a finite interval formula, rather than citing an asymptotic
B-process with unspecified endpoint errors. Integer-endpoint Poisson sums
retain their half-weight corrections. Each literal common-factor interval
is partitioned into disjoint integer dyadic pieces. A finite expanded band
contains every stationary mode and every mode whose stationary point is
near an endpoint.

Two integrations by parts on the excluded, uniformly nonstationary modes
retain their full analytic endpoint coefficients. The first inverse-phase
sum uses symmetric convergence, with its poles removed by the included
band. The second and third sums converge absolutely. No physical height
is excluded because an endpoint phase is close to an integer.

For retained modes, the exact coordinate
\[
\xi=\operatorname{sgn}(v-1)\sqrt{2(v-1-\log v)}
\]
makes the phase quadratic. Two regular quotient identities give incomplete
Fresnel main terms, two endpoint corrections, and a remainder bounded
using four amplitude derivatives. The full Fresnel transition is retained
even when a stationary point crosses an endpoint. A full Gaussian alone
is never substituted there.

The globally summed common-factor error is
\[
|R_{\rm product}^{\rm CF}|
\le C\mathfrak M(Nw_N)^2/T
=O(\mathfrak M N^{-1-\kappa/4}).
\]
The original-index alternative has the stronger bound
\[
|R_{\rm product}^{\rm orig}|
\le C\mathfrak M L^6(Nw_N)/T.
\]
Both retain the actual product sine term, carrier, four physical pair
classes, and literal floors. The same proofs cover the new degree-six
diagonal-annihilating kernels with their explicit coefficient scale.
For \(\mathfrak M=O(L)\), both errors are
\(o(N^{-\kappa/4})\), uniformly for sufficiently small time on
\(1\le\kappa\le3/2\). This compares with an available physical
upper-budget scale, not a lower bound for measured error.

The transformed stationary main terms may be numerous. The theorem is
an analytical representation with a paid remainder, not a claim of a
smaller or faster numerical algorithm or a negative main sum.

## 4. Coupled primitive frontier

For the exact frontier with actual \(\gcd(n,m)\le J\), Note 9 gives
\[
\mathcal F_J=\sum_{q\le N}c_J(q)
(\Re V_q)^TQ(\Re V_q),\qquad
c_J(q)=\sum_{j\mid q,\,j\le J}\mu_{\rm Mob}(q/j).
\]
Each quadratic retains both ratio and product channels. Its block and
complement vectors use \(\lfloor N/q\rfloor\) and
\(\lfloor\lfloor N/2\rfloor/q\rfloor\) exactly.
Although \(c_J(q)=0\) for \(1<q\le J\), the terms with \(q>J\)
must remain. For the primitive sector \(J=1\), the coefficients are
the actual Möbius function. They can be negative.

Half-integer Poisson endpoints retain exactly each sublattice's integer
membership. With \(M\ge4P\), \(P=T/(2\pi)\), all potentially
stationary integrals are among the retained \(|k|\le M\) modes.
Two phase-aware integrations by parts pay the excluded tail, retaining
its alternating endpoint functions. For feature degree at most D,
the complete error is
\[
|\mathcal F_J-\widetilde{\mathcal F}_J|
\le C_D\|Q\|A_v^2
\left\{\frac{(Nw_N)L^D}{M}+\frac{L^{2D}}{M^2}\right\}.
\]
It is uniform for every \(1\le J\le N\). The divisor bound
\(|c_J(q)|\le\tau(q)\) is used only for this positive error envelope;
the signed main coefficients remain exact. The weighted divisor sums
converge uniformly using a fixed weight exponent strictly greater than
one half. Taking \(M=\lceil4P\rceil\) gives an error below the
physical upper-budget scale for any fixed D and polynomial growth of the
matrix and feature scales. The new kernel uses D=6.

The complete candidate constraints apply only to the full moment vector
\(V_1\), not separately to each \(V_q\). Reflected q-sublattices have
shifted weights, centers, carriers, and dual index ranges. Imposing separate
candidate zeros or replacing all reflected sublattices by the q=1 family
would change the arithmetic problem.

## 5. Prescribed stationary reflection

Heat Note 22 derives exact coefficient identities from the actual rational
alpha data and physical carrier. For the q=1 stationary map \(n=P/k\),
the heat weight changes its exponent by
\[
\delta_\sigma=O(tx^{-2}+t^2x^{-1}),
\]
the reflected center has mismatch \(O(x^{-2})\), and the carrier
mismatch modulo \(2\pi\) is \(O(x^{-1})\). Terms nominally of
order \(t/x\) in the center and \(tL\) in the carrier cancel when
the actual centering and thermal frequency are retained.

On a fixed macroscopic dual interval this compares the leading stationary
coefficient with \((-1)^j\overline{q(k)}\rho(k)^j\), at cost
\(O_j(w(k)/x)\). For a fixed moment quadratic its static coefficient
comparison costs \(O(\mathfrak M(Nw_N)^2/x)\). This is not a global
stationary-phase error or a replacement for the endpoint theorem.

The antilinear moment reflection fixes even cosine and odd sine moments,
and hence fixes the base threshold quadratic. Its diagonal-annihilating
extension changes the sign of the small drift coefficient. The stationary
image of \([N/2,N]\) is approximately \([N,2N]\), so the natural
cutoff is not conserved. These facts limit a proof using leading reflection
alone; they do not rule out a useful signed inequality for the complete
coupled Fresnel and boundary terms.

## 6. Cross-audit and scope

The root derivations and separate LLM audits checked the candidate-null
identity and sine orientations, diagonal cancellation, narrow-band powers,
and measured candidate payment. They checked the integer and half-integer
finite Poisson conventions, both integration-by-parts signs, paired tail
functions, expanded stationary band, regular quotient limits, inverse
coordinate derivatives, and global dyadic and divisor summations. The
physical weight exponent used in the original-index refinement was
justified from the exact alpha formula and natural-cutoff floor displacement.
Static reflection identities were checked independently against the
exact center and carrier formulas.

Primary references for the elementary Fourier/Poisson and stationary phase
normalizations are
[NIST Fourier series and Poisson summation](https://dlmf.nist.gov/1.8),
[cotangent partial fractions](https://dlmf.nist.gov/4.22.E3), and
[stationary phase](https://dlmf.nist.gov/2.3#iv). The new paid formulas are
derived in the notes, with their own explicit remainder mechanisms.
No generic stationary-phase citation supplies an unprinted error bound.
No independent specialist or formal proof review has been performed.

All uniform asymptotic statements refer to sufficiently small positive time
on the stated closed parameter interval. Faster growth of the selected
matrix coefficients must stay in the displayed errors and payments. The
genuine density constant remains symbolic. Ordinary-double tests do not
close higher multiplicity or small-curvature branches by themselves.

## 7. Precisely recombine before seeking the sign

One valid split is
\[
\mathcal J^\dagger
=\mathcal F_J^\dagger
+\mathcal D_{>J}^\dagger+\mathcal P_{>J}^\dagger.
\]
Use Note 9 for the coupled frontier, Note 6 for the matching large-common-
factor difference intervals, and Note 8 for their product intervals.
Alternatively use an entire-product transform and retain its matching
primitive difference representation. The two complete product expressions
are alternatives and must not both be counted.

Where the near-pair band is paid separately, its exact contribution must
be removed from the corresponding main expression before adding its
absolute payment. The remaining sum contains the separated actual
primitive pairs and resonant product terms. Its signed upper bound must
beat the new candidate payment, recomputed physical threshold payment,
and the remainders of the chosen representation.

The next bounded analytical task is a candidate-conditioned one-sided
estimate of these **coupled resonant and boundary terms**, keeping the
prescribed coefficients, Möbius factors, shifted centers, and actual common
frequency. A full absolute moment payment or an isolated block sign would
not achieve it. The present continuation supplies new exact cancellations
and vanishing errors, but leaves that main signed inequality open.
