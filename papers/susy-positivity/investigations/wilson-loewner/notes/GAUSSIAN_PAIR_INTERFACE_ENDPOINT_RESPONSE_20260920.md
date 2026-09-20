# A Gaussian pair interface excites the protected tower with nonuniform weights

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: unavailable; not exposed in this session.
Status: internal analytical calculation, primary-source audit and finite
diagnostics. No independent specialist review or arithmetic positivity result.
The version-0.5 manuscript pair and every dated snapshot are preserved.

## Decision

A stable, flavor-neutral quadratic coupling to the two lowest scalar modes
provides a definite Gaussian boundary preparation. A single charged endpoint
on this state excites infinitely many protected composites. Its normalized
ordinary-adjoint response is

\[
 G_g(u)=(1-q)^2\frac{e^{-u/2}}{(1-qe^{-u})^2}
       =\sum_{k=0}^{\infty}(1-q)^2(k+1)q^k e^{-(k+1/2)u},
 \qquad 0\leq q<1.                                      \tag{1}
\]

The coupling determines \(q\); it is not fitted to arithmetic. The factor
\(k+1\) is the Bose enhancement of the seeded mode, derived below from its
ordinary Fock norm. Thus an infinite composite tower is physically reachable
in this explicitly specified mode interface, but its response is not the
omitted elementary channel. Even granting extra projections solely for
comparison, its weights cannot all become one. Its nonzero singular boundary
limit has a double short-distance pole instead of a simple one.

This is a scoped obstruction to this Gaussian preparation with this charged
endpoint. It does not exclude other interfaces or endpoints. The construction
is admissible as a spatially nonlocal, finite-mode boundary coupling in the
free theory. It is **not** a derived local supersymmetric hemisphere boundary
interaction or a Wilson endpoint. That additional physical realization is
unestablished, and the spectral mismatch already prevents this candidate
from passing the requested component test.

## 1. Starting audit and what is being held fixed

Read the four requested notes, current main Section 5 and SI S12, and the
critical-path cumulative-append handoff. Read `LARGE_FILES.md`; no `AGENTS.md`
was found in the checkout, its applicable ancestor directories, or its
subdirectories. The [separate internal audit](../reviews/review_codex_endpoint_sources_20260920.md)
records source locations and limitations.

The key primary inputs are [D, (2.8), (3.1)--(3.5), (C.7)--(C.13)] and
[G, (78)--(82), (125)--(128)]. In the centered flat frame the protected
scalar is \(O(t)=q_1(t)+tq_2(t)/(2r)\). Applying ordinary dilation to a
fixed insertion, rather than to its changing polarization, gives

\[
 \mathcal Q[D,O(t)]=-\frac{t}{2r}\mathcal Qq_2(t).
                                                               \tag{2}
\]

The free scalar variation has a nonzero fermion on the right at generic
nonzero interior points. This remains a failure on arbitrary closed
representatives. For either individual nilpotent charge, the ordinary
radial Hodge identity instead gives
\(\{\mathcal Q_i^H,(\mathcal Q_i^H)^\dagger\}=8(D-R_H)\)
in the source convention. Its common harmonic states admit restricted
\(e^{-uD}\). An elementary highest-H scalar has Hodge gap \(\ell\),
so only its \(\ell=0\) mode remains. No substantive correction to this
distinction was found. This is an internal check, not specialist approval.

The calculation below takes that common harmonic Hilbert space and its
ordinary radial norm as its starting point. It does not infer a Hilbert
isometry from the localized \(L^2(d^2Y)\) wavefunctions. In particular the
physical annihilators introduced next are not the tilded generators of the
localized Weyl algebra. Boundary Mellin amplitudes are not used to set any
spatial energy or endpoint coefficient.

## 2. Candidate specified before the arithmetic comparison

### Bulk, modes, and ordinary adjoint

Use one free massless three-dimensional N=4 hypermultiplet with the ordinary
positive reality condition and no gauge field. On the unit spatial cylinder
\(\mathbb R\times S^2\), the scalar part of its conformal action is

\[
 S_{\rm sc}=\sum_{I=1}^2\int du\,d\Omega\,
 \left(|\partial_u\phi_I|^2+|\nabla_{S^2}\phi_I|^2
                          +\tfrac14|\phi_I|^2\right).           \tag{3}
\]

The free fermion action is the conformal Dirac action; its modes stay in
their vacuum and do not enter this Gaussian scalar preparation. Equation
(3) is the cylinder version of the ungauged conformal action in [D, (2.10)].
Vacuum energy is subtracted in the propagation generator \(D\).

Let \(a^\dagger,b^\dagger\) create the two independent highest-H,
\(\ell=0\) scalar quanta with flavor charges \(+1,-1\). Their unit
normalization is fixed by canonical quantization of (3), with
\(Y_{00}=1/\sqrt{4\pi}\) and one-particle energy \(1/2\):

\[
 [a,a^\dagger]=[b,b^\dagger]=1,\qquad [a,b]=[a,b^\dagger]=0.
\]

Equivalently these modes are extracted by the positive-frequency
field-and-momentum projection on \(Y_{00}\). This specifies a smooth spatial
smearing and a frequency polarization, rather than a point field at the cut.
On their Fock space,

\[
 D_{\rm eff}=\tfrac12(N_a+N_b),\quad F=N_a-N_b,\quad
 |m,n\rangle=\frac{(a^\dagger)^m(b^\dagger)^n}{\sqrt{m!n!}}|0\rangle.
                                                               \tag{4}
\]

Every such ket is harmonic. All other bulk modes are spectators in their
vacuum. Thus inclusion of this space into the full radial Hilbert space is
isometric by ordinary free-field quantization, and \(D\) restricts to (4).
No identification of a spatial harmonic index with a composite degree is
made: the many-particle energies in (4) are sums of lowest-mode energies.

### Neutral Gaussian boundary preparation

Prepare the incoming boundary state as the ground state of

\[
 H_g=\tfrac12(N_a+N_b+1)-g(a^\dagger b^\dagger+ab),
 \qquad g\in\mathbb R,\quad |g|<\tfrac12.                       \tag{5}
\]

For example, a semi-infinite preparation cylinder with this Hamiltonian and
vacuum spectator modes prepares the state at its end, as the normalized
limit of \(e^{-T H_g}|0\rangle\) when \(T\to\infty\). The coherent-state
Euclidean action on the two selected modes is

\[
 S_{{\rm prep},g}=\int_{-\infty}^{0}d\tau\,
 \left[\bar a\partial_\tau a+\bar b\partial_\tau b
 +\tfrac12(\bar a a+\bar b b+1)-g(\bar a\bar b+ab)\right],       \tag{6}
\]

understood through the canonical time-sliced coherent-state integral.
Here the integration variables \(a,b\) are the oscillator symbols, not the
boundary variables \(Y,\bar Y\) of [G]. At the join, the coupling is switched
off. Propagation between the two endpoints is by the original \(D_{\rm eff}\),
not by \(H_g\). The adjoint preparation is used on the bra side.

This choice has an independent physical rationale. The elementary endpoint
has flavor one. Among quadratic interactions in these two modes, a neutral
pair term is the lowest-degree Hermitian interaction that creates additional
quanta while preserving this flavor sector. Linear sources carry flavor;
number terms alone cannot create pairs from vacuum. We impose no arithmetic
rates, even-degree filter, or coefficients in choosing (5). The phase of a
complex pair coupling can be removed by a mode rotation; its absolute value
gives the same weights. The entire stable interval is tested, so there is no
privileged value to optimize against the target.

Equations (5)--(6) are **nonlocal in angle** when written in bulk fields:
they couple the global lowest-mode canonical coordinates. This is a defined
external boundary preparation, with a finite number of modes and no
ultraviolet ambiguity. It is not asserted to arise from a local deformation
of the original Higgs boundary conditions. The operation preserves the
harmonic subspace, so the prepared kets remain annihilated by both individual
Higgs charges and their ordinary adjoints. We make no claim here of a local
supersymmetric completion of the interface on the full bulk field space.
This distinction is enough to use (4), and avoids extending the Hodge claim
to an unproved boundary module.

### Stability and complete boundary conditions

Write

\[
 \tanh(2\eta)=2g,\quad \lambda=\tanh\eta,\quad q=\lambda^2,
 \quad g=\frac{\lambda}{1+\lambda^2},\quad
 \Omega_g=\frac{1-q}{2(1+q)}=\sqrt{\tfrac14-g^2}>0.              \tag{7}
\]

The real squeeze parameter \(\eta\) is separate from spatial time and the
earlier field-space Mellin exponent. Define

\[
 \alpha=a\cosh\eta-b^\dagger\sinh\eta,\qquad
 \beta=b\cosh\eta-a^\dagger\sinh\eta.
\]

Their commutators are canonical, and direct substitution gives

\[
 H_g=\Omega_g(\alpha^\dagger\alpha+\beta^\dagger\beta+1).         \tag{8}
\]

This proves stability and gives a precise boundary condition:
\(\alpha|\Omega_g\rangle=\beta|\Omega_g\rangle=0\), with every
spectator annihilator also killing the state. These conditions and unit norm
fix it up to a phase. They specify the incoming Gaussian state completely;
they are not the Dirichlet/auxiliary boundary data of the earlier hemisphere.

## 3. Endpoint, response, normalization, and domains

The boundary recurrence from (8) gives

\[
 |\Omega_g\rangle=\sqrt{1-q}\sum_{k\geq0}\lambda^k|k,k\rangle
   =S_\eta|0\rangle,\qquad
 S_\eta=\exp[\eta(a^\dagger b^\dagger-ab)].                            \tag{9}
\]

This is a finite-mode unitary Bogoliubov transformation; its adjoint is
\(S_\eta^\dagger=S_{-\eta}\). Now use the original single charged endpoint
\(a^\dagger\), placed **after** preparation. Its raw ket has squared norm
\(\langle\Omega_g|aa^\dagger|\Omega_g\rangle=(1-q)^{-1}\).
Define the unit-norm endpoint preparation and its ordinary adjoint by

\[
 B_g=\sqrt{1-q}\,a^\dagger S_\eta,\qquad
 B_g^\dagger=\sqrt{1-q}\,S_\eta^\dagger a,
\]
\[
 |\psi_g\rangle=B_g|0\rangle
   =(1-q)\sum_{k\geq0}\sqrt{k+1}\lambda^k|k+1,k\rangle.          \tag{10}
\]

One can also obtain this ket as \(S_\eta|1,0\rangle\). This last equality
holds on the specified seed; it is not the operator identity
\(B_g=S_\eta a^\dagger\) on arbitrary inputs. In particular \(B_g\) is not
asserted to be an identity-normalized transfer on arbitrary boundary data.

The weights can be derived without invoking a squeezed-state formula:
expanding a quadratic pair source gives coefficient \(\lambda^k/k!\)
for \((a^\dagger)^{k+1}(b^\dagger)^k\). Its squared Wick norm is
\((k+1)!k!\). Therefore the resulting spectral weight is proportional to

\[
 \frac{(k+1)!k!}{(k!)^2}\,q^k=(k+1)q^k.                        \tag{11}
\]

The ground-state recurrence fixes the common coefficient in (10).
Since \(\sum_{k\geq0}(k+1)q^k=(1-q)^{-2}\), the normalized response
is exactly

\[
 G_g(u)=\langle0|B_g^\dagger e^{-uD_{\rm eff}}B_g|0\rangle,
\]

as evaluated in (1), with

\[
 E_k=k+\tfrac12,\qquad w_k=(1-q)^2(k+1)q^k,
 \quad \sum_k w_k=1.                                         \tag{12}
\]

Using the raw elementary endpoint instead multiplies (1) by \(1/(1-q)\).
It does not change the relative weights or energies. The vacuum has norm
one here; the earlier hemisphere partition value \(1/2\) is not imported
as an endpoint normalization.

The operators in (4) are self-adjoint number operators on their usual Fock
domains, with finite-particle core. One convenient domain for \(B_g\) is
\(\{\psi:S_\eta\psi\in\operatorname{Dom}(a^\dagger)\}\); its adjoint
has the corresponding ordinary annihilator domain. The vacuum lies in this
domain for \(|g|<1/2\). The ket (10) lies in every power domain of \(D\),
because its coefficient tail is geometric. The closed-form series is
absolutely and locally uniformly convergent for
\(\Re u>\log q\) when \(0<q<1\), in particular for all real \(u\geq0\).
This is the analytic series continuation; the bounded semigroup formula
uses \(u\geq0\).
For \(q=0\) the answer is the single exponential. For real \(u\geq0\),

\[
 0\leq G_g(u)\leq e^{-u/2},\qquad G_g(0)=1,\qquad
 G_g'(0)=-\left(\tfrac12+\frac{2q}{1-q}\right).                \tag{13}
\]

The Laplace transform converges for \(\Re p>-1/2\) and is
\(\sum_k w_k/(p+k+1/2)\). These are positive ordinary norms and an
actual spectral matrix element, not a trace or a Mellin transform. The
energies and weights have now been computed without using the target.

## 4. Arithmetic component comparison

The requested component is

\[
 C_{\rm omit}(u)=\sum_{n\geq1}e^{-(2n+1/2)u}
              =\frac{e^{-5u/2}}{1-e^{-2u}}.                    \tag{14}
\]

For every nonzero stable coupling, (12) has all energies \(k+1/2\),
including \(1/2,3/2,7/2,\ldots\), which (14) does not have. Each target
energy does occur, at \(k=2n\), but its weight is
\((1-q)^2(2n+1)q^{2n}\), rather than one. The candidate therefore
excites the corresponding *composite* energies without restoring the
discarded elementary angular modes or matching their response.

To isolate the weight issue, grant for comparison only the orthogonal
projection

\[
 P_* =\tfrac12(1+(-1)^{N_b})-|1,0\rangle\langle1,0|
 \quad\hbox{on the flavor-one sector}.                         \tag{15}
\]

It keeps even \(k\geq2\). This is an additional filter, not a boundary
condition or symmetry selection derived from (5). Indeed the pair term
changes \(N_b\) by one. Its projected response, without renormalizing, is

\[
 G_{g,*}(u)=(1-q)^2 e^{-u/2}\frac{x(3-x)}{(1-x)^2},
 \qquad x=q^2e^{-2u}.                                         \tag{16}
\]

The success probability is
\(G_{g,*}(0)=q^2(3-q^2)/(1+q)^2\). A conditional normalization
divides (16) by this constant for \(q>0\); it cannot change relative weights.
An arbitrary overall normalization cannot flatten them either: equality of
the \(n=1,2\) weights requires \(q^2=3/5\), while equality of the \(n=2,3\)
weights requires \(q^2=5/7\). Thus even this more permissive comparison has
no solution in the stable family. This is an exact algebraic obstruction,
not an optimization failure at sampled couplings.

At any fixed stable coupling, both (1) and (16) have finite limits at zero,
whereas

\[
 C_{\rm omit}(u)=\frac1{2u}-\frac34+O(u).                       \tag{17}
\]

More generally, the spectral theorem implies
\(\langle\psi,e^{-uD}\psi\rangle\to\|\psi\|^2\) for any fixed
finite-norm state and \(D\geq0\). An exact response (14) must therefore
involve a singular endpoint, an infinite trace, or another non-vector
construction. This general observation does not exclude the regulated
point-field channel from which (14) originally arose.

## 5. Singular limit and regulator: a stronger mismatch

As \(|g|\uparrow1/2\), \(q\uparrow1\), the preparation gap in (7) closes.
The normalized kets (10) have no norm limit: their overlaps with every fixed
finite-particle ket vanish while their norm stays one. They converge weakly
to zero. For each fixed \(u>0\), (1) tends to zero, while (13) remains one
at \(u=0\). This limit is not the desired singular covariance.

Choose the removable pair phase so that \(g\uparrow1/2\). Removing the
vanishing common ket factor \(1-q\) produces instead the generalized ket

\[
 |\chi\rangle=\sum_{k\geq0}\sqrt{k+1}|k+1,k\rangle.             \tag{18}
\]

It is a continuous linear functional on rapidly decreasing Fock sequences,
not a Hilbert vector. A precise regulator is
\(|\chi_\epsilon\rangle=e^{-\epsilon D}|\chi\rangle\),
\(\epsilon>0\). Its response is

\[
 \langle\chi_\epsilon,e^{-uD}\chi_\epsilon\rangle
 =\frac{e^{-(u+2\epsilon)/2}}{(1-e^{-(u+2\epsilon)})^2}.          \tag{19}
\]

For \(q=e^{-2\epsilon}\), this equals
\(e^{-\epsilon}G_g(u)/(1-q)^2\). Hence the regulated singular ket
is tied to the specified stable preparation family, up to the stated common
factor, and is not a new choice of spectral coefficients. Equation (19)
converges pointwise for \(u>0\), uniformly on compact subsets of that interval,
and on finite-particle test vectors as a generalized ket. Its squared norm diverges
as \(1/(4\epsilon^2)\). No finite positive extension at \(u=0\) is claimed.

Even after granting (15), its limiting response is

\[
 \widetilde G_*(u)
 =\frac{e^{-5u/2}(3-e^{-2u})}{(1-e^{-2u})^2},\qquad
 \frac{\widetilde G_*(u)}{C_{\rm omit}(u)}
 =\frac{3-e^{-2u}}{1-e^{-2u}}.                                 \tag{20}
\]

It has leading behavior \(1/(2u^2)\); the full singular response in (19)
has leading behavior \(1/u^2\). Neither has (17)'s simple pole. At large
\(u\), the ratio in (20) tends to three and its short-distance value diverges
like \(1/u\); no overall normalization repairs both regimes.

This also defeats the positive derivative component test:
\(2\int_0^\infty u e^{-pu}C_{\rm omit}(u)du\) is finite for
\(\Re p>-5/2\), while the same integral with \(\widetilde G_*\)
has a logarithmic ultraviolet divergence. A cutoff and signed finite-part
subtraction would define a different object, not turn these endpoint weights
into unit weights. Taking the coupling as a function of the separation would
also change the fixed observable in the question.

Finally, the complete prime-free arithmetic generator has off-diagonal kernel
\(2C_{\rm omit}(u)-2e^{u/2}\), and, in the repository's hard-cutoff
convention, the local coefficient
\(\log\epsilon+\gamma+\log(2\pi)+O(\epsilon)\).
Equivalently its derivative includes the signed term
\(-2/(p-1/2)^2\). A positive endpoint correlator supplies neither this
signed pole nor that fixed local finite part, even if its positive component
were to match. No signed cancellation or auxiliary smoothing loss is counted
as arithmetic positivity.

## 6. Evidence, limits, and consequence

The analytical results are (8)--(20): stable preparation, normalized endpoint
coefficients, response, domains, incompatible weight ratios and regulated
singular limit. Their proofs use canonical oscillator algebra, geometric
series, and the spectral theorem. They do not require numerical extrapolation.

The standard-library program
[check_gaussian_pair_endpoint.py](../numerics/check_gaussian_pair_endpoint.py)
provides four exact rational coupling/normalization checks, 25 factorial
weight checks, and the incompatible rational equal-weight requirements.
As an independent floating diagnostic it integrates the tridiagonal squeeze
evolution of a seeded state at 512 and 1024 steps for three couplings, then
compares the resulting amplitudes and response with (10) and (1). It also
checks 20 response/projection comparisons, four short-distance samples, and
nine heat-regulator identities. The finite ODE truncation is not an interval
certificate. The exact finite identities do not certify external physical
assumptions or arithmetic positivity.

From the investigation directory:

```sh
python3 -B numerics/check_gaussian_pair_endpoint.py \
  --output /tmp/gaussian-pair-endpoint-replay.json
python3 -B numerics/check_spatial_radial_descent.py \
  --output /tmp/spatial-radial-descent-replay.json
python3 -B numerics/check_hodge_radial_channel.py \
  --output /tmp/hodge-radial-channel-replay.json
```

The new small [diagnostic record](../numerics/records/gaussian-pair-endpoint-checks-20260920.json)
and [provenance record](../numerics/records/gaussian-pair-endpoint-provenance-20260920.json)
are separate from the manuscript's existing diagnostics and build record.
The two inherited programs reproduced their saved records in this environment.

The result advances the endpoint question by giving a response, not only a
counting character. Infinite excitation alone is insufficient: canonical
endpoint matrix elements can change both pole order and asymptotic behavior.
This candidate fails before a Wilson or interacting calculation is justified.
It supplies no spatial-to-Mellin dictionary, arithmetic shift interpretation,
physical arithmetic transfer, or arithmetic Loewner driver.

The direct arithmetic continuation remains independent. The EMA anchor is
internally certified and awaits specialist review. At
\(L=1/2,h=1/20,\omega=10^{-3}\), the scalar sufficient estimate fails;
the finite quotient near 0.802 is not an all-input upper bound. The queued
task remains the energy-weighted cumulative-coupling estimate controlling
both omitted input spaces and preserving endpoint and signed-pole memory.
See the [next-session prompt](RESEARCH_CONTINUATION_AFTER_GAUSSIAN_ENDPOINT_20260920.md).

## Primary sources

- [D] Dedushenko, Pufu and Yacoby, *A one-dimensional theory for Higgs branch
  operators*, arXiv:1610.00740v2, [primary full text](https://arxiv.org/html/1610.00740v2).
- [G] Dedushenko, *Gluing II: Boundary Localization and Gluing Formulas*,
  arXiv:1807.04278v3, [primary full text](https://arxiv.org/html/1807.04278v3).

The new Gaussian mode interface, its response and the arithmetic comparison
are calculations in this note, not results attributed to [D] or [G].
