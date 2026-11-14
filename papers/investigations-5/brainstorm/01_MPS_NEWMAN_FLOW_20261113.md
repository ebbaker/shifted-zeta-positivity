# Matrix product states for the Newman flow

13 November 2026, America/New_York. Prepared for **Edward Baker**, who
proposed this direction, with substantial OpenAI Codex LLM assistance.
Actual backend model and reasoning effort are unavailable in this chat's
recorded model configurations; no settings are inferred.

**Status: exploratory representation and approximation analysis, with one
floating compression pilot.** There is a concrete matrix product state
(MPS) formulation: tensorize the binary digits of the source coordinate.
Its imaginary-time generator has a matrix product operator (MPO) of bond
dimension at most three. A constructive increasing-rank hierarchy converges
on every prescribed compact time/height domain. Whether useful ranks and
working precision suffice for the normalized signed Green observation at
growing height remains open. No new zero exclusion, uniform complexity
theorem, specialist review or novelty claim is made.

This follows the [result index](../../../result-summaries/README.md) and
[avoid index](../../../avoid/README.md), especially
[collision controls](../../../result-summaries/12_collision_controls_and_screening.md),
[stable-model scope](../../../result-summaries/17_constructive_stable_model_obstructions.md),
[classification](../../../avoid/01_restating_the_target.md),
[coordinate changes](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions](../../../avoid/07_scoped_exclusions_read_as_universal.md).
The exact tensor identities below are representations; the error bounds
are approximation statements; the pilot is a measured finite compression
diagnostic. None acquires the missing arithmetic sign.

## 1. The inherited wavefunction and the direction of imaginary time

Use Investigation 09's complete normalization:

\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \qquad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
 \tag{1}
\]

Here \(\Phi\) is the positive, even, complete theta source, and
\(H_0(z)=\xi(1/2-iz/2)/8\). The
[source chapter](../09_green_potentials_newman_flow/manuscript/sections/02_source.tex)
supplies the fixed-derivative, exponentially weighted domination.

Fix \(\lambda_0=1/2\) and put \(\tau=\lambda_0-\lambda\). The unnormalized
source wavefunction is

\[
 \psi_\tau(u)=e^{-\tau u^2}W_{\lambda_0}(u),\qquad
 \partial_\tau\psi_\tau=-X^2\psi_\tau,
 \quad (Xf)(u)=uf(u).
 \tag{2}
\]

Thus ordinary contractive imaginary time runs toward **decreasing Newman
time**. The interval \(0\le\lambda\le1/2\) corresponds to
\(0\le\tau\le1/2\). Increasing \(\lambda\) is reverse heat and is
unbounded on ambient \(L^2\), even though the canonical prepared source
has the required decay for every finite real time.

This is exactly compatible with the inherited cylinder realization:
\(K=-\partial_v^2+4(A-I)\), restricted to its prepared first angular
shell, becomes multiplication by \(u^2\). Its radial/angular state is
already a product. Tensorizing those two factors alone adds no compression
mechanism. See the
[operator chapter](../09_green_potentials_newman_flow/manuscript/sections/03_geometry_operator.tex).

One can alternatively use a Born-density formulation:
\(\varphi_\tau=e^{-\tau X^2/2}\sqrt{W_{\lambda_0}}\), for which
\(2H_\lambda(z)=\langle\varphi_\tau,e^{izX}\varphi_\tau\rangle\).
For real \(z\) this is a bounded unitary observable; complex \(z\) needs
the source's weighted domains. This alternative has generator \(X^2/2\).
The linear Fourier readout in (1), applied to \(\psi\), must not be
confused with a Born expectation using \(|\psi|^2\).

## 2. A concrete binary-coordinate MPS

Choose a source cutoff \(U>0\), \(N=2^L\) midpoint samples, and

\[
 h=2U/N,\quad a=-U+h/2,\quad w_k=h2^{L-k},\qquad
 u_{\boldsymbol b}=a+\sum_{k=1}^Lw_kb_k,\quad b_k\in\{0,1\}.
 \tag{3}
\]

The vector

\[
 |\psi^{(L,U)}_\tau\rangle
 =\sqrt h\sum_{\boldsymbol b}
 W_{\lambda_0-\tau}(u_{\boldsymbol b})|b_1\cdots b_L\rangle
 \approx\sum_{\boldsymbol b}
 A_1^{b_1}(\tau)\cdots A_L^{b_L}(\tau)|\boldsymbol b\rangle
 \tag{4}
\]

is a **quantics tensor train (QTT)**. The sites label coarse-to-fine binary
resolution, not physical electrons, primes or zeros. The boundary matrix
dimensions are one; the internal dimensions are the MPS bond dimensions.
Repeated singular-value decomposition gives an exact finite representation
with \(D_k\le2^{\min(k,L-k)}\). Compression asks whether much smaller
dimensions give a specified error in a relevant norm.

This is an established tensor-network construction, with a particularly
close condensed-matter analogue in
[Shinaoka et al., §§II–III](https://arxiv.org/html/2210.12984v3).
[Lindsey, §§3–4](https://arxiv.org/html/2311.12554v3)
relates ranks and constructive interpolation errors to regularity.
Their results motivate analysis of the actual theta source; they do not
provide its height-dependent signed-observation bounds automatically.

## 3. The generator is an exact small MPO

Let \(n_k=|1\rangle\langle1|\) on bit \(k\). On the sampled space,

\[
 \widehat X=aI+\sum_kw_kn_k,\qquad
 \widehat K=\widehat X^2
 =a^2I+\sum_k(2aw_k+w_k^2)n_k
       +2\sum_{j<k}w_jw_kn_jn_k.
 \tag{5}
\]

This is a commuting, all-pairs spin interaction with factorized couplings.
There is an explicit MPO:

\[
 \widehat K=(1,2a,a^2)
 \prod_{k=1}^L
 \begin{pmatrix}
 I&2w_kn_k&w_k^2n_k\\
 0&I&w_kn_k\\
 0&0&I
 \end{pmatrix}
 \begin{pmatrix}0\\0\\I\end{pmatrix}.
 \tag{6}
\]

At each site the three running entries update
\((1,2s,s^2)\) to \((1,2(s+w_kb_k),(s+w_kb_k)^2)\).
This proves (6), including the constant and cross-term factors. The bond
dimension is **at most three**, independently of the grid size.

The exact discrete orbit is \(e^{-\tau\widehat K}|\psi_0\rangle\).
Commutativity makes its factorization into the gates from (5) exact;
there is no Trotter splitting error before compression. The chain is
not a nearest-neighbor physical chain, however, so a nearest-neighbor
ground-state area-law argument has not been supplied.

A second exact network expression follows directly from the Gaussian
Fourier integral, for \(\tau>0\):

\[
 e^{-\tau\widehat X^2}
 =\frac1{\sqrt{4\pi\tau}}\int_{\mathbb R}
 e^{-s^2/(4\tau)}e^{isa}
 \bigotimes_{k=1}^L e^{isw_kn_k}\,ds.
 \tag{7}
\]

A finite quadrature of this auxiliary-field integral is a sum of product
operators and hence an MPO of rank at most its number of nodes. Its
quadrature error still needs a bound. The integrand contains complex
phases; positive Gaussian weights do not make every readout positive.

**Small generator rank is not small exact propagator rank.** At a cut
after bit \(k\), write \(j=pM+q\), \(M=2^{L-k}\), and
\(u=\alpha_p+hq\), \(\alpha_p=a+hMp\). The Gaussian multiplier unfolds as

\[
 e^{-\tau(\alpha_p+hq)^2}
 =e^{-\tau\alpha_p^2}e^{-\tau h^2q^2}
     \bigl(e^{-2\tau h\alpha_p}\bigr)^q.
 \tag{8}
\]

For \(\tau>0\), the nodes in parentheses are distinct positive numbers.
This is a row/column-scaled Vandermonde matrix, with exact rank
\(\min(2^k,2^{L-k})\). This scoped statement concerns the sampled Gaussian
multiplier in this bit ordering. It does not lower-bound its approximate
ranks, or the ranks of the particular evolved theta state.

## 4. The Newman field is a product-state contraction

If the coefficient matrices in (4) approximate \(\sqrt h W_\lambda\),
then the corresponding field is

\[
 \widetilde H_\lambda^{(L,U)}(z)
 =\frac{\sqrt h}{2}e^{iza}
 \prod_{k=1}^L\left(A_k^0(\tau)+e^{izw_k}A_k^1(\tau)\right).
 \tag{9}
\]

The product is a scalar. For exact cores it equals the midpoint rule
\((h/2)\sum_jW_\lambda(u_j)e^{izu_j}\). The oscillatory readout itself
has bond dimension one. Once the cores exist, evaluation costs
\(O(LD^2)\) arithmetic operations for maximum bond dimension \(D\),
excluding precision costs. Construction of the cores is a separate cost.

Fixed spatial jets use the same state with the insertion
\((i\widehat X)^r\). The polynomial construction below gives that diagonal
operator an MPO of bond dimension at most \(r+1\). In particular one state
can supply \(H,H_z,H_{zz}\) with their own weighted error payments. This
does not provide uniform bounds when derivative order also grows.

This is the requested finite MPS expression for a wavefunction undergoing
the correct imaginary-time evolution, with an explicit readout of the
canonical field. Sampling the field in \(z\) and tensorizing that grid is
another possibility, but the source-coordinate version exposes its exact
generator without a derivative discretization.

## 5. An explicit convergent hierarchy, beyond finite-vector factorization

For fixed \(U\), approximate \(W_{\lambda_0}\) uniformly by a polynomial
\(p_d\) of degree \(d\), with error \(\epsilon_d\to0\). An even polynomial
can be chosen because the source is even. For \(0\le\tau\le\tau_*\), use

\[
 q_m(\tau,u)=\sum_{r=0}^m\frac{(-\tau u^2)^r}{r!},\qquad
 |e^{-\tau u^2}-q_m(\tau,u)|
 \le\frac{(\tau_*U^2)^{m+1}}{(m+1)!}=:E_m.
 \tag{10}
\]

Taylor's remainder on the nonnegative real interval gives this bound.
Writing \(M_U=\sup_{|u|\le U}W_{\lambda_0}(u)\), the evolved polynomial
\(r_{d,m,\tau}=p_dq_m\) satisfies

\[
 \sup_{\tau,u}|W_{\lambda_0-\tau}(u)-r_{d,m,\tau}(u)|
 \le\epsilon_d+(M_U+\epsilon_d)E_m.
 \tag{11}
\]

Every degree-\(r\) polynomial has explicit sampled MPS cores of dimension
at most \(r+1\). Indeed, for \(v(x)=(1,x,\ldots,x^r)\), set

\[
 B_r(q)_{ij}=\begin{cases}\binom ji q^{j-i},&j\ge i,\\0,&j<i,\end{cases}
 \quad 0\le i,j\le r.
 \qquad v(x)B_r(q)=v(x+q).
 \tag{12}
\]

If \(c(\tau)\) is the coefficient column of \(r_{d,m,\tau}\), then

\[
 \sqrt h\,r_{d,m,\tau}(u_{\boldsymbol b})
 =\sqrt h\,v(a)\prod_kB_{d+2m}(w_kb_k)c(\tau).
 \tag{13}
\]

Absorb the two boundary vectors into the first and last cores. The bond
dimension is at most \(d+2m+1\), independent of the number of grid points
at fixed \(d,m\). Equations (10)–(13) approximate the exact orbit uniformly
on the compact clock, rather than declaring an arbitrary independently
fitted state to solve the flow.

These monomial formulas establish existence, not numerical conditioning:
large binomial coefficients can make them a poor implementation. Stable
interpolative constructions are preferable; Lindsey's Proposition 13 and
equations (4.1)–(4.3) provide the relevant polynomial-exact construction.
Bounds on its analytic neighborhoods and norms must be supplied for the
chosen interval. The present argument needs only polynomial approximation
on a compact real interval and does not claim a favorable all-height rate.

## 6. Pay the error in the observation norm

Suppose the finite-state Euclidean error is
\(\|\widetilde\psi-\psi^{(L,U)}\|_2\le\varepsilon\). For \(|\Im z|\le b\),
Cauchy–Schwarz gives

\[
 |\widetilde H(z)-H_{\mathrm{grid}}(z)|
 \le\frac{\sqrt h}{2}
       \left(\sum_j e^{-2(\Im z)u_j}\right)^{1/2}\varepsilon
 \le\frac{\sqrt{2U}}2e^{bU}\varepsilon.
 \tag{14}
\]

This is an absolute error, with no division by the field near a zero.
For a fixed derivative order \(r\), the last bound gains the factor
\(U^r\), and the omitted source tail gains \(|u|^r\).
For \(|\Re z|\le T\), define
\(M_2=\sup_{\tau,z,|u|\le U}|\partial_u^2[W_{\lambda_0-\tau}(u)e^{izu}]|\)
on the prescribed compact ranges. The complete source is smooth, so
midpoint quadrature and the source tail give

\[
 |H_{\lambda_0-\tau}(z)-\widetilde H(z)|
 \le \underbrace{\frac12\int_{|u|>U}e^{b|u|}W_{\lambda_0}(u)\,du}_{E_{\rm tail}}
 +\frac{Uh^2M_2}{24}
 +\frac{\sqrt{2U}}2e^{bU}\varepsilon.
 \tag{15}
\]

Arithmetic source truncation, computed-core errors and floating arithmetic
are additional payments when these are used. The derivatives in this
quadrature bound belong to the complete source; reflecting a finite theta
prefix does not automatically preserve its smooth endpoint.

For each finite target box and positive absolute tolerance, first choose
\(U\) for the tail, then \(h\) for quadrature and \(d,m\) for the state
error. Formula (11) gives \(\varepsilon\le\sqrt{2U}\) times its right-hand
side. Diagonal choices over boxes \(T\to\infty\) and tolerances tending
to zero give locally uniform convergence to the entire field. This proves
existence of the proposed limiting family, without any bounded-rank claim
or conclusion about zeros of its approximants.

For numerical evolution, a differentiable approximate state with residual
\(r=\partial_\tau\widetilde\psi+\widehat K\widetilde\psi\) obeys

\[
 \|\widetilde\psi(\tau)-\psi(\tau)\|_2
 \le\|\widetilde\psi(0)-\psi(0)\|_2+
         \int_0^\tau\|r(s)\|_2\,ds.
 \tag{16}
\]

Variation of constants and \(\|e^{-s\widehat K}\|\le1\) prove this.
Whole-step truncation errors likewise accumulate under the contractive
full propagator. Individual gates from (5) need not each be contractions
because some one-site coefficients are negative; gate-level errors require
their intervening amplification factors. A fixed-rank variational evolution
is an approximation whose residual cannot be omitted.

## 7. Height and the Green consumer

In the repository's convention, Newman height \(X\) corresponds to zeta
height \(|X|/2\). At time zero,

\[
 H_0(X)=M(s)\zeta(s),\quad s=\tfrac12-iX/2,\qquad
 M(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/16.
 \tag{17}
\]

The gamma factor has scale
\(|M(s)|\asymp |X|^{7/4}e^{-\pi|X|/8}\) as \(|X|\to\infty\).
This is not a lower bound on \(|H_0|\): zeta can vanish. It explains why
a tiny relative error in the positive source state can be large compared
with the signed Fourier readout. To certify an absolute error in a
gamma-normalized field using only (14), one must pay the corresponding
exponential normalization factor. This is a limitation of that particular
source-norm error allowance, not a lower complexity bound for every
cancellation-aware contraction method.

The existing
[Riemann–Siegel chapter](../09_green_potentials_newman_flow/manuscript/sections/10_riemann_siegel.tex)
already removes that scale analytically and retains both arithmetic arms
and the remainder. Any tensor approach should be compared with that
baseline, or applied to those complete normalized expressions. Multiplying
an inaccurate small Fourier value by a large normalization afterward does
not recover lost digits.

For the current Green program, field accuracy must pass through the
[boundary-log acquisition theorem](../09_green_potentials_newman_flow/manuscript/sections/07_boundary_log.tex)
or the [contour-deflation method](../09_green_potentials_newman_flow/manuscript/sections/09_deflation.tex).
These allow zeros, but require their stated anchors, contours, tails and
denominator payments. A uniform small ordinary state norm is not by itself
a uniform signed-log estimate. In particular, the inherited
[conditioning family](../09_green_potentials_newman_flow/manuscript/sections/11_conditioning.tex)
changes its Green value on a square-root scale under a first-order source
perturbation. Its obstruction concerns that enlarged source family, not
all theta-specific tensor algorithms.

The [current boundary-bootstrap status](../09_green_potentials_newman_flow/02_height_time_boundary_bootstrap/README.md)
includes the acquired width 567/1000 and the accepted E11 packet assessment;
the every-center signed budget and global bridge remain open. Low-rank
representation would help acquire or analyze the retained field, but does
not change those task statuses. Universal \(J_0=0\) is the inherited
RH-equivalent reformulation; checking an MPS approximation is not evidence
for that equivalence's conclusion.

## 8. A bounded floating pilot

The [script](numerics/mps_newman_pilot.py) and
[small execution record](numerics/MPS_NEWMAN_PILOT_20261113.json) use midpoint
grids with 1,024 and 4,096 points on \([-2,2]\), eight positive-half-line theta
terms, and binary64 TT-SVD. Each state is formed by the exact diagonal
grid evolution from \(\lambda_0=1/2\), then compressed independently.
The pilot therefore tests representation, not an adaptive time integrator.

For 4,096 points at \(\lambda=0\):

| Requested relative state tolerance | Maximum bond dimension | Stored real parameters | Measured relative state error | Relative Fourier difference at \(X=80\) |
| --- | --- | --- | --- | --- |
| \(10^{-8}\) |8|538|\(1.71\times10^{-9}\)|3.69%|
| \(10^{-12}\) |10|820|\(2.51\times10^{-13}\)|\(6.90\times10^{-7}\)|

The last column compares the MPS contraction with the same floating dense
grid sum, about \(2.6470\times10^{-12}\). It is not a continuum error
certificate. At the tighter setting the observed absolute difference is
about \(1.83\times10^{-18}\), where floating evaluation also matters.
The \(\lambda=1/2\) slices likewise use maximum ranks 8 and 10 at these
tolerances. The pilot's dense initialization does not demonstrate a faster
end-to-end algorithm; independent source and quadrature errors are unpaid.

These results support small approximate ranks on the specified grid and
expose readout sensitivity. They do not establish a rank law at increasing
height, a nonzero lower field bound, or any new zero information.

## 9. An exact low-rank collision control

Let \(T>0\), and use two bits with source coordinate
\(u=b_1+b_2-1\). Assign amplitudes

\[
 |\Psi_\lambda\rangle
 =e^{\lambda-T}(|00\rangle+|11\rangle)+|01\rangle+|10\rangle.
 \tag{18}
\]

Its Fourier contraction is

\[
 F_\lambda(z)=2+2e^{\lambda-T}\cos z,\qquad
 \partial_\lambda F_\lambda=-\partial_z^2F_\lambda.
 \tag{19}
\]

This is the transform of the positive source
\(2\delta_0+e^{-T}(\delta_{-1}+\delta_1)\) with the Newman heat weight.
All its zeros are real for \(\lambda\ge T\). For \(\lambda<T\), they are
\((2k+1)\pi\pm i\operatorname{arcosh}(e^{T-\lambda})\). At \(\lambda=T\),
\(F=F_z=0\), \(F_{zz}=2\) at every \((2k+1)\pi\).

Yet exactly at the collision,
\(|\Psi_T\rangle=(|0\rangle+|1\rangle)^{\otimes2}\): its bond dimension
is one and its normalized bipartite entanglement is zero. At other times
its bond dimension is at most two. Reversing the clock gives the same
contractive imaginary-time law generated by \((n_1+n_2-I)^2\).

This elementary three-atom example is in the spirit of the catalog's
atomic controls, not a new canonical theta event. It disproves only the
generic inference that positive amplitudes, bounded MPS rank, or a regular
imaginary-time orbit prevent positive-time collisions. It also shows that
a collision need not produce an entanglement spike in this encoding.
It fails the complete theta source, its arithmetic, its full profile and
its eventual threshold simplicity. The polynomial identity
\(qF_T=(q+1)^2\), \(q=e^{iz}\), and the rank-one event amplitude are
checked alongside (6) and (12) by exact rational finite algebra.

## 10. Collision-control premise screen

This is an analytical screen against the actual families in
[cluster 12](../../../result-summaries/12_collision_controls_and_screening.md),
following [avoid 02](../../../avoid/02_shape_only_arguments_and_the_controls.md).
Existing numerical collision witnesses were not rerun. Tensorization and
compact approximation are generic operations, so they are not themselves
distinguishing theta premises. No claim is made that every control has the
same efficient rank bound as theta at a prescribed tolerance.

| Control | Premise absent from the literal theta application |
| --- | --- |
| Euler-factor/translated-source controls | They change the complete source and xi field; the unchanged zeta prime subtraction and canonical normalization cannot be imported. |
| Weighted-square and finite-prefix controls | They do not supply all theta coefficients together with full reflection. Their event times must not be called finite all-real thresholds. |
| Reflected super-Gaussian control | Reflection, positivity and positive Gram forms do not supply the integer-square theta expansion. |
| Smooth shape and positive-primitive controls | Decay, log-concavity, primitive positivity and endpoint/asymptotic matching do not supply the full arithmetic source. |
| Finite-prime-orbit controls | Selected-prime identities and finite measurements leave the full normalized reflection/arithmetic condition unpaid. No uniform growing-prefix premise follows. |
| Atomic and exact finite-profile controls | They lack the full theta profile and arithmetic; the atomic threshold models also lack theta's eventual threshold simplicity. Equation (18) gives an explicit small MPS example. |
| RH-conditional endpoint controls | The ordinary Dirichlet-series arithmetic is absent; their conditional construction is not unconditional evidence about theta. |
| Fixed source with a varied observation kernel | The complete cosine/Fourier readout and its Newman equation are absent. Equation(9) must retain the literal readout. |

Failure of one canonical identity is not proof that a control fails every
future estimate derived from it. A proposed favorable tensor inequality
must identify and verify its own distinguishing quantitative premise.
Accurately representing a colliding control preserves its collision.

## 11. Where the idea could acquire arithmetic content

The most immediately justified use is a multiscale compression and error
analysis of the existing prepared state. The substantive analytical target
would be a bound on the required ranks and precision as functions of
height, complex observation offset, time and desired normalized error,
followed by the existing Green acquisition theorem. The next comparison
should keep the same field, tolerance and tails and include construction
cost, against ordinary interpolation or the complete Riemann–Siegel method.

A more arithmetic network could index prime occupations. Formally,
\(n=\prod_pp^{k_p}\) makes the isolated heat weight
\[
 e^{\lambda(\log n)^2/4}
 =\exp\!\left[\frac\lambda4
           \left(\sum_pk_p\log p\right)^2\right].
 \tag{20}
\]
This is again a collective quadratic coupling, but a finite RS cutoff
imposes \(\sum_pk_p\log p\le\log N\), and the complete gamma factors,
reflection arm and correction remain. At positive \(\lambda\), the
unrestricted series \(\sum_n n^{-s}e^{\lambda(\log n)^2/4}\) does not even
have terms tending to zero. Equation (20) is therefore not a standalone
infinite Gibbs state or a replacement for the complete Newman field.
It is a possible finite arithmetic tensorization, with its cost and
utility unestablished.

A Lee–Yang/stability-preserving tensor family would be a separate, much
stronger proposal. Positive tensor entries alone do not ensure real zeros,
as (18) shows. The existing
[constructive-stable-model exclusions](../../../result-summaries/17_constructive_stable_model_obstructions.md)
apply to their specified families, not every tensor network. No claim of
equivalence between RH and a particular restricted tensor ansatz is made.

The present direction remains a brainstorm: the explicit representation
and compact convergence can be used now; a new arithmetic inequality or
a measured complete acquisition advantage is still required for further
Green/Newman progress. The [same-assistant check](reviews/01_MPS_SELF_CHECK_20261113.md)
and [reference catalog](references/README.md) record the verification scope.
