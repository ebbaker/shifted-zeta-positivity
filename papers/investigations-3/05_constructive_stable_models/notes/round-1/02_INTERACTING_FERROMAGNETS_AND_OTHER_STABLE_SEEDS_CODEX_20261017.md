# Round 1 continuation: interacting ferromagnets and other stable seeds

17 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
Same-model subagents checked the constructions, imports and finite arithmetic.
This is continued research within round one, **before formal round review**.

**Disposition:** the independent-spin exclusion in [Note 01](01_INDEPENDENT_SPIN_HEAT_FAMILY_AND_ODD_DILATION_OBSTRUCTION_CODEX_20261017.md)
does not close interacting ferromagnets. Two further bounded screens reject
single quartic laws and a natural fixed Bessel base with positive even
multipliers. An explicit, initially interacting two-quartic-block model
lies outside the independence hypothesis and the
nonnegative-potential-coefficient cone. Its stability and heat law are justified; a theta
approximation has not been constructed. Retain the interacting block
architecture for the round review, without starting a larger fitting run.

## 1. Scope, sources and decision questions

This continuation follows the user's request to examine alternatives before
the review. It applies the [initial proposal](../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md),
the [result index](../../../../../result-summaries/README.md), and the
[avoid index](../../../../../avoid/README.md), particularly
[summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid 01](../../../../../avoid/01_restating_the_target.md),
[avoid 07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[avoid 13](../../../../../avoid/13_a_factor_is_not_the_target.md), and
[avoid 16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The inherited theta normalization and moment conventions are those of
Note 01. A real-zero approximation to the complete theta transform at
time zero remains an RH-strength objective. The present outputs are
specified construction checks and bounded obstructions, not evidence
from finite fits for that objective.

| Alternative | Result of this round's examination |
| --- | --- |
| General initially interacting Ising spins | Admissible and exactly heat compatible; Note 01's odd-dilation argument does not apply. No theta approximation theorem obtained. |
| One interacting pair, with arbitrary positive amplitudes | Can break odd dilation, but its kurtosis is at most 2, excluding theta moment matching. |
| A single quartic continuous spin, including critical Curie–Weiss limits | Independently stable; four source values exclude theta approximation, including weak limits with varying quartic parameters. |
| Pure potentials with nonnegative coefficients from degree six onward | Same four values exclude pointwise source approximation at those nodes. No general weak-limit claim for a growing-degree class is made. |
| Fixed natural Bessel base times arbitrary nonnegative even-coefficient multipliers | Five values exclude source approximation and, by compactness, weak source or transform approximation. This contains the even universal-prefactor route. |
| Coupled quartic blocks | Concrete stable interacting family with paid finite-block convergence; a certified negative sixth potential coefficient puts an explicit example outside the preceding potential cone. Theta approximation is unresolved. |

## 2. Interactions change the zero geometry

For unit signs with a **fixed initial interaction**, define
\[
Z_N(t,h)=\frac{\sum_\sigma
\exp\{\sum_{i<j}J^0_{ij}\sigma_i\sigma_j+tS_N^2+hS_N\}}
{\sum_\sigma\exp\{\sum_{i<j}J^0_{ij}\sigma_i\sigma_j\}},
\quad S_N=\sum_i b_i\sigma_i,
\quad J^0_{ij}\ge0,\ b_i>0.
\tag{1}
\]
The denominator is fixed at time zero. The exact heat dictionary is
\[
J_{ij}(t)=J^0_{ij}+2tb_ib_j,\qquad
\partial_tZ_N=\partial_h^2Z_N.
\tag{2}
\]
The same single-spin and field hypotheses checked in Note 01 apply to
[Fröhlich–Rodriguez, Theorem 1](https://arxiv.org/pdf/1205.6643#page=3):
unit Bernoulli measures are even and compactly supported, their transforms
are zero-free in the positive half-plane, the fields are \(b_ih\), and
the couplings (2) are nonnegative for real \(t\ge0\). Thus
\(Z_N(t,iz)\) has only real zeros. No theta stability is assumed.

For an explicit change in zero geometry, take two equal amplitudes \(b\)
and \(J^0=\tfrac12\log3\). Then
\[
Z_2(0,iz)=\frac{\cos(2bz)+1/3}{1+1/3}.
\]
At \(2br=\arccos(-1/3)\), this vanishes, but
\(\cos(6br)=23/27\), so its value at \(3r\) is nonzero.
There is consequently no odd-dilation invariant for general interacting
ferromagnets.

One pair is still too restrictive. For arbitrary amplitudes \(a,b>0\),
the squared readout takes the values \((a+b)^2\) and \((a-b)^2\) with
probabilities \(p=(1+\tanh J^0)/2\ge1/2\) and \(1-p\). On setting
\(r=(a-b)^2/(a+b)^2\in[0,1)\), its kurtosis is
\[
\frac{p+(1-p)r^2}{[p+(1-p)r]^2}\le\frac1p\le2.
\tag{3}
\]
The derivative of the middle expression in \(r\) is
\(2p(1-p)(r-1)/[p+(1-p)r]^3\le0\). The inherited outward theta
kurtosis exceeds 2.79098. Equation (3) therefore excludes every single
ferromagnetic pair, rather than all interacting systems.

## 3. Quartic seeds: valid stability, failed source compatibility

The continuous law
\[
\rho_{\alpha,\beta}(u)=C_{\alpha,\beta}
e^{-\alpha u^4-\beta u^2},\qquad \alpha>0,\ \beta\in\mathbb R,
\tag{4}
\]
is an independently admissible Lee–Yang seed. The primary source is
[Simon–Griffiths, Theorems 1 and 3, pp. 148 and 151–152](https://math.caltech.edu/SimonPapers/47.pdf).
It constructs quartic laws as limits of ferromagnetic Ising systems and
proves the half-plane zero theorem for their ferromagnetic couplings.
The quadratic coefficient may have either sign. Heat weighting simply
replaces \(\beta\) by \(\beta-t\); there is no independent refit.

For any positive source, set
\[
W(x)=-\log\rho(\sqrt x),\qquad
\Delta_h^3W(0)=W(3h)-3W(2h)+3W(h)-W(0).
\]
Every law (4) has \(\Delta_h^3W(0)=0\), since \(W\) is quadratic in
\(x\). More generally, this difference is nonnegative if
\[
-\log\rho(u)=c+\beta u^2+\alpha u^4+\sum_{k\ge3}v_ku^{2k},
\qquad v_k\ge0,
\tag{5}
\]
with convergence at the tested nodes. Constants, quadratic heat factors,
and quartic terms cancel. For \(k\ge3\), \(\Delta_h^3 x^k|_{x=0}>0\).

The [source certificate](../../numerics/round-1/SOURCE_ALTERNATIVE_OBSTRUCTIONS.json)
evaluates the complete theta source and gives
\[
\boxed{\quad
\Delta_{1/100}^3[-\log\Phi(\sqrt x)]_{x=0}
\in(-0.000434999,-0.000434997).
\quad}
\tag{6}
\]
Thus (5) cannot converge to theta even at the four source nodes
\(u=0,\sqrt{.01},\sqrt{.02},\sqrt{.03}\). Multiplying sources by arbitrary
positive normalizing constants does not change this test.

This tests a familiar sufficient construction as well. In
[de Bruijn, Theorem 1, p. 198](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da),
an even nonconstant nonnegative entire potential gives a real-zero Fourier
transform if its derivative is a complex-compact limit of polynomials
with imaginary roots. For an even potential this derivative hypothesis
forces nonnegative even Taylor coefficients. Indeed, rotating its odd
derivative gives a real odd Laguerre–Pólya function. Its canonical product,
rotated back, is a real constant times
\(u^{2m+1}e^{au^2}\prod_j(1+u^2/r_j^2)\), with \(a\ge0\).
The constant must be positive, since otherwise the even potential would
decrease to minus infinity on the real half-line. Integrating this
positive-coefficient product proves the assertion. Such potentials, and
their permitted quadratic heat deformations, satisfy (5). The simple
potential route fails the actual theta test (6). We are not claiming
that every polynomial with nonnegative coefficients has the required
derivative-root property.

For the **single quartic family**, the exclusion also covers weak source
limits, and hence convergence of normalized Fourier transforms. Here is
the extra compactness argument; it is not presumed for the full class (5).
Suppose (4) converges weakly to theta's normalized positive density. If
\(r_n=\|(\alpha_n,\beta_n)\|\to\infty\), pass to a subsequence with
normalized potentials tending on compact sets to a nonconstant polynomial
\(p(u)=au^4+bu^2\). Choose bounded intervals \(A,B\) with
\(\inf_Ap>\sup_Bp+2\eta\). Then eventually
\[
\mu_n(A)\le (|A|/|B|)e^{-r_n\eta}\mu_n(B)\longrightarrow0,
\]
contradicting the positive theta mass of \(A\). The parameters are
therefore bounded. Extract their limits and determine the normalizing
constant from any compact interval of positive limiting mass. Local
density convergence then identifies the limit as another quartic or a
Gaussian, both incompatible with (6). This does not exclude multi-block
quartic systems.

## 4. Bessel seeds and universal multipliers

The natural double-exponential seed is
\[
B(u)=e^{-2\pi\cosh4u},\qquad
\int_0^\infty B(u)\cos(zu)\,du=\tfrac14K_{iz/4}(2\pi).
\tag{7}
\]
Its real-zero property is independent of theta. For example, a zero of
\(K_{iz}(a)\) gives the decaying Dirichlet solution
\(y(x)=K_{iz}(ae^x)\) of
\(-y''+a^2e^{2x}y=z^2y\). Its energy identity forces \(z^2>0\).
The imported differential equation and decay are
[DLMF 10.25.1](https://dlmf.nist.gov/10.25#E1) and
[10.40.2](https://dlmf.nist.gov/10.40#E2); see also
[Gasper, equations (1.5)–(1.7) and sections 2–3](https://arxiv.org/pdf/0801.2996).

An even universal multiplier \(U\) has \(U(iz)\) in the
Laguerre–Pólya class. Pólya's preservation theorem, stated with hypotheses
in [Cardon, Proposition 1](https://mathdept.byu.edu/cardon/papers/FourierRealZeros.pdf),
applies to (7): the source is even, integrable and decays faster than
\(e^{-|u|^b}\) for some \(b>2\). Hence \(BU\), and subsequently
\(e^{tu^2}BU\) for real \(t\ge0\), have real-zero transforms. For a
nonnegative, nonzero even multiplier, the canonical product is
\[
U(u)=Cu^{2m}e^{au^2}\prod_j(1+u^2/r_j^2),\qquad C>0,\ a\ge0.
\tag{8}
\]
Every even coefficient is nonnegative. This includes products of cosh
factors and polynomial universal factors.

In fact the following test applies to **every** entire multiplier with
nonnegative even coefficients, whether or not it is universal. For
\(R(x)=\Phi(\sqrt x)e^{2\pi\cosh(4\sqrt x)}\), the same certificate gives
\[
\boxed{\quad\Delta_{1/1000}^4R(0)
\in(-5.232\cdot10^{-7},-5.230\cdot10^{-7}).\quad}
\tag{9}
\]
Each admissible \(U(\sqrt x)\) has nonnegative fourth forward differences.
Consequently no such fixed-base source \(BU_n\) can converge to theta
at the five nodes \(u=\sqrt{k/1000}\), \(0\le k\le4\).

This exclusion also reaches weak source limits. Bounded masses imply,
for every \(R\ge0\),
\[
U_n(R)\int_R^{R+1}B(u)\,du\le\int_0^\infty B(u)U_n(u)\,du\le M.
\tag{10}
\]
Nonnegative coefficients give \(|U_n(z)|\le U_n(|z|)\), so the multipliers
form an entire normal family. Any subsequential compact limit gives local
uniform density convergence to \(BU\). If the measures converge weakly
to theta, this identifies \(BU=\Phi\), contradicting (9). Normalizing
the masses and applying Lévy's continuity theorem therefore also excludes
pointwise real-frequency, and hence complex-compact, Fourier convergence
to \(H_0\). This argument needs no assumed inversion of derivative data.

The universal-prefactor obstruction is **already discussed by de Bruijn
on p. 221**, using analytic continuation. Equation (9) supplies a concrete
finite diagnostic and states the larger nonnegative-coefficient class it
checks; it is not a novelty claim for that classical exclusion. The test
is tied to the fixed base (7). Arbitrarily varying or degenerating Bessel
bases and nonuniversal multipliers outside this coefficient cone are not
excluded here.

Even matching two tail terms does not automatically preserve stability.
For \(U_c=4\pi^2(\cosh9u+c\cosh5u)\), matching the theta coefficients
of \(e^{9u}\) and \(e^{5u}\), after removal of \(e^{-\pi e^{4u}}\),
requires \(c=\pi-3/(2\pi)>2\). But
\(U_c(iz)/(4\pi^2)=T_9(\cos z)+cT_5(\cos z)\). Dividing the polynomial
by its root at zero and putting \(y=x^2\) gives
\[
p_c(y)=256y^4-576y^3+(432+16c)y^2-(120+20c)y+9+5c.
\]
Its discriminant is \(2^{24}D(c)\), with
\[
D(2+s)=-575-1004s-736s^2-472s^3-136s^4-20s^5<0\quad(s\ge0).
\]
Thus the required prefactor has nonreal zeros and is not universal.
This fails that sufficient preservation route; it does not prove that
the Fourier transform of the particular product \(BU_c\) is unstable.

## 5. A concrete initially interacting seed that survives these exclusions

Consider the zero-field two-variable law
\[
d\nu(x,y)=C\exp\{-x^4-y^4+\tfrac72(x^2+y^2)+xy\}\,dx\,dy,
\qquad S=x+y.
\tag{11}
\]
Both sites are admissible quartic measures and the cross coupling is
**positive at the initial time**. The continuous-spin theorem cited in
section 3 gives a real-zero transform for \(S\). It has the fixed heat law
\[
\beta(t)=-\tfrac72-t,\quad K(t)=1+2t,\qquad
Z(t,h)=\mathbb E_\nu e^{tS^2+hS},\quad\partial_tZ=\partial_h^2Z.
\tag{12}
\]

This is also a specified limit of elementary Ising ferromagnets. Take two
blocks of even size \(N\), block magnetizations \(M_1,M_2\), and
\[
c_N=(12N^3)^{-1/4},\quad
J_{\mathrm{within}}=1/N+7c_N^2,\quad
J_{\mathrm{between}}=c_N^2,\quad S_N=c_N(M_1+M_2).
\tag{13}
\]
Use \(J\) as the coefficient of each unordered pair. The centered-binomial
expansion cancels \(M_j^2/(2N)\), leaving quartic coefficient one for
\(x_j=c_NM_j\), quadratic coefficient \(7/2\), and cross term \(x_1x_2\).
Under heat, add \(2tc_N^2\) to every pair and retain the diagonal scalar
\(e^{2tNc_N^2}\) with the initial normalizer fixed. Thus (13) has exactly
the parameter evolution (12), before taking a limit.

The associated piecewise-constant block histograms have a uniform quartic
envelope. One direct check writes \(M=2r\) for even \(N\) and uses
\[
\log\frac{\binom N{(N+M)/2}}{\binom N{N/2}}
\le-\frac{M^2}{2(N+1)}-\frac{M^2(M^2-2)}{12(N+1)^3}.
\]
This follows from the exact central ratio and
\(\log[(1-u)/(1+u)]\le-2u-2u^3/3\). After applying (13), the central
ratio is bounded by \(e^{-x^4/8+(7/2+\sqrt{12})x^2}\), where
\(x=c_NM\). Replacing \(x\) by any point of its shrinking histogram cell
preserves a uniform quartic envelope with slightly weaker constants.
For any fixed compact complex \((t,h)\) set, choose \(q\) large enough
to absorb the cross quadratic, \(tS^2\), the linear readout and each fixed
derivative, using that a quartic envelope is bounded by
\(D_qe^{-qx^2}\) for every fixed \(q\). The histogram mesh tends to zero;
the lattice readout differs from its associated continuous histogram
variable by at most half that mesh. Dominated convergence then gives
complex-compact convergence and differentiated convergence of (13) to
(11)–(12). This justifies the
finite-block construction; it is not a convergence theorem to theta or
a bound uniform in an increasing number of blocks.

There is a discriminating coefficient check on this seed. Put
\(s=x+y\), \(v=(x-y)/2\). Its marginal density is proportional to
\[
e^{-s^4/8+2s^2}\int_{\mathbb R}
e^{-2v^4+6v^2-3s^2v^2}\,dv.
\]
If \(W=V^2\), where \(V\) has density proportional to
\(e^{-2(V^2-3/2)^2}\), its potential is
\[
-\log\rho_S(s)=C+s^4/8-2s^2-\log\mathbb E e^{-3s^2W}.
\]
In particular,
\[
[s^6](-\log\rho_S)=\tfrac92\kappa_3(W).
\tag{14}
\]
Four rigorous integrals, in the
[two-block certificate](../../numerics/round-1/TWO_QUARTIC_SEED_CERTIFICATE.json), give
\[
\kappa_3(W)\approx-0.005059254092,\qquad
[s^6](-\log\rho_S)\approx-0.022766643414,
\]
with outward interval radii below \(10^{-38}\) for both displayed
quantities before decimal shortening. Hence (11) lies outside the
nonnegative-higher-potential-coefficient class (5). This is an explicit
reason the source test (6) cannot exclude all interacting block models.
The sign does not establish theta moment matching or theta convergence.

The general architecture has sites \(\alpha_j>0,\beta_j\in\mathbb R\),
couplings \(K_{ij}\ge0\), and positive readout weights \(b_j\):
\[
\rho(\mathbf x)\propto
\exp\{-\sum_j\alpha_jx_j^4-\sum_j\beta_jx_j^2+
\sum_{i<j}K_{ij}x_ix_j\},\qquad S=\sum_jb_jx_j.
\]
Heat uses \(\beta_j(t)=\beta_j-tb_j^2\) and
\(K_{ij}(t)=K_{ij}+2tb_ib_j\). Every fixed finite model is admissible.
For a theta construction, what is missing is a rule selecting a sequence
of blocks and parameters with a proved source or complex-transform error
tending to zero and a uniform heat-tail budget. No such rule follows from
the finite-block limit (13), and a finite moment fit would not provide it.

## 6. Computation contract, controls and pre-review decision

The [replay guide](../../numerics/round-1/ALTERNATIVES_REPLAY.md) records
the bounded runs. The source tests used 160-bit Arb arithmetic, eight
theta terms and an analytic complete tail, nine evaluations, a 30-second
limit, and requested finite-difference width below \(10^{-7}\).
Their final radii are much smaller. The two-block test used four rigorous
Acb integrals on \([0,4]\), 160 bits, fixed tolerance and evaluation caps,
and a proved tail at most \(e^{-128}/32\) for each integral. Initial scouts
are distinguished from the retained runs. No parameter grid was run.

The controls from summary 12 still apply to any proposed theta implication.
In each case, the premise that would fail is **convergence to that control
from the claimed real-zero approximants on the necessary time slices**:

| Control | Contrary slice |
| --- | --- |
| Euler-factor \(0<c<1\) | The factor \(1+c\cos(az)\) has nonreal zeros already at time zero. |
| Weighted-square collision controls | A sufficiently close positive time before their nondegenerate collision has a nonreal pair. |
| Reflected super-Gaussian control | Its pre-collision nonreal pair likewise prevents such convergence. |
| Smooth/positive-primitive positive-threshold controls | Some positive time below their threshold has a nonreal zero. |

Hurwitz forbids that convergence at the named slice. A real double zero
at the collision itself is compatible with Lee–Yang. We have not assigned
an uncomputed forward-difference sign to a control: (6) and (9) test the
actual theta source. Shape, reflection and auxiliary positivity do not
supply the missing admissible approximation of any target.

**Recommendation before review:** retain the scoped exclusions from Notes
01–02, and keep the interacting quartic-block architecture open as an
explicit alternative. The initially interacting example and its negative
potential coefficient prevent extending those exclusions to all
ferromagnets. The round review should assess whether there is a concrete
source-approximation strategy for growing blocks; it should not infer one
from a stable seed, tail resemblance or low-moment fitting. No broader
closure or manuscript milestone is proposed here.

**Continuation, 17 October 2026:** [Note 03](03_FIELD_GROWTH_AND_QUARTIC_NETWORK_OBSTRUCTIONS_CODEX_20261017.md) proves a further obstruction: no fixed diffuse quartic readout site may persist in a theta-approximating ferromagnetic sequence. The explicit seed above remains a valid construction but cannot serve as a fixed component to which more sites are merely appended. Infinitesimal interacting and degenerating-site regimes remain open. The new independent pure-quartic-array exclusion is proved analytically and extends to weak source limits.
