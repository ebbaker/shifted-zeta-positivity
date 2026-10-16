# Structural tests for a positive arithmetic bulk theory

This note derives compatibility tests for choosing a bulk theory. They concern exact operator identities and the physical meaning of observables. They are not numerical positivity estimates, and none establishes positivity of the complete Weil form. The deductions below are supplied for this comparison; no claim of literature priority is made.

## 1. The target and what must be explained

Put \(I_L=(-L/2,L/2)\), let \(E_L\) extend by zero, and use \(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\). Define
\[
a_k=2k+\tfrac12,\qquad
B(s)=\sum_{k\ge0}\frac2{a_k}\frac{s}{s+a_k^2}
=\Re\psi(\tfrac14+i\sqrt{s}/2)-\psi(\tfrac14).
\]
Writing \(T_d=E_L^*U_dE_L\), \(U_dF(x)=F(x-d)\), the required form is
\[
\begin{split}
Q_L[f]={}&\frac1{2\pi}\int B(\tau^2)|\widehat{E_Lf}(\tau)|^2\,d\tau
+w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2\\
&-\sum_{\substack{p\ {\rm prime},\,m\ge1\\m\log p<L}}
(\log p)p^{-m/2}\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle ,
\end{split}
\]
where
\[
w_0=\psi(\tfrac14)-\log\pi,\quad
C(f)=\int f(x)\cosh(x/2)\,dx,\quad
S(f)=\int f(x)\sinh(x/2)\,dx.
\]
The natural finite-interval domain has logarithmically weighted Fourier norm. The form is closed and semibounded there; nonnegativity is the unresolved property. All support lengths, or an unbounded sequence of them, are required for the global program. These conventions agree with the local background and with the additive form of Weil's criterion reviewed by Suzuki.[^suzuki]

An acceptable quantum construction independently specifies a positive physical Hilbert space, a reference state, and a linear state map
\[
\Gamma_L:C_c^\infty(I_L)\longrightarrow\mathscr H_L
\]
and proves \(q_L(g,f)=\langle\Gamma_Lg,\Gamma_Lf\rangle\). A positive Hamiltonian alone does not identify this map. A supertrace, spectral determinant, holomorphic amplitude, or regularized difference of traces is a different object until an additional identity relates it to this ordinary norm.

## 2. Gaussianity is not the principal dividing line

At a finite regulator, every positive covariance matrix \(C\) is the covariance of a Gaussian vector: take \(C^{1/2}X\) with standard Gaussian \(X\). This observation proves no arithmetic positivity, since finding a positive \(C\) equal to the target is the unknown step. It shows that the complexity of a two-point kernel alone cannot establish that an interacting realization is necessary.

Conversely an interacting theory gives a quadratic functional of a *linear smearing*:
\[
\|\mathcal O(f)\Omega\|^2
=\iint\overline{f(x)}f(y)
\langle\Omega|\mathcal O(x)^\dagger\mathcal O(y)|\Omega\rangle\,dx\,dy.
\]
The field \(\mathcal O\) may be composite and its dynamics nonlinear. Wick factorization need not hold. A generic source-dependent vacuum energy or partition function contains higher source powers, so it is a less direct target for an exactly quadratic arithmetic form.

The substantive question is whether the action, state, and source map *derive* the needed kernel. Arbitrary nonlocal Gaussian kernels and arbitrarily fitted interacting potentials both risk putting the answer into the model.

## 3. Interactions can preserve the spectral restriction

Suppose a response, after its specified contact subtraction, still has the form
\[
\mathcal T(s)=s\int_0^\infty\frac{d\mu(t)}{s+t},\qquad d\mu\ge0.
\]
If the relevant moments exist, its coefficients \(m_j=\int t^j\,d\mu(t)\) necessarily obey
\[
(m_{i+j})_{i,j=0}^n\ge0,\qquad
(m_{i+j+1})_{i,j=0}^n\ge0.
\]
Indeed their polynomial quadratic forms are \(\int|p(t)|^2d\mu\) and \(\int t|p(t)|^2d\mu\).

Replacing discrete masses by an interacting continuum of positive spectral weights does not change this necessity. The finite-block obstruction in the existing investigation therefore survives whenever the new response remains in that class and retains the stipulated moments. An interacting model must escape a specific hypothesis: the observable, arithmetic-frequency dependence, finite-block replacement, or spectral integrability. The general spectral representation in physical time does not imply a Stieltjes representation in an unrelated arithmetic spatial variable.

## 4. Infinite input space and finite charge data

### Finite ground-state rank

If every \(\Gamma_Lf\) lies in an \(r\)-dimensional ground-state space, then its Gram form has rank at most \(r\). The closed Weil form has infinite rank: its associated self-adjoint operator \(W_L\) is the unbounded logarithmic gamma operator plus fixed-\(L\) bounded terms. A densely defined self-adjoint finite-rank operator would be bounded. Closedness is relevant here; unboundedness of an arbitrary test-space functional alone would not exclude a finite-rank form. A finite matrix of vacuum overlaps cannot represent the required closed form for arbitrary inputs.

A field theory, a direct integral, infinitely many operator states, or an unwrapped periodic theory can escape this test. A periodic model may have a rank-one metric in each Bloch fiber and nevertheless an infinite total state space. One must inspect the full construction rather than merely count vacua in a fiber.

### Fixed finite flavor tori

Suppose all dependence on the arithmetic Fourier variable is through a fixed one-parameter subgroup of a flavor torus:
\[
\theta_j(\tau)=\alpha_j\tau\pmod{2\pi},\quad j=1,\ldots,r.
\]
The allowed character frequencies lie in \(\sum_j\mathbb Z\alpha_j\), whose rational span has dimension at most \(r\). Distinct prime logarithms are rationally independent: clearing denominators in \(\sum_p q_p\log p=0\) and exponentiating would give a nontrivial integer prime factorization of one. Thus a fixed finite torus cannot produce every \(\log p\) by this mechanism.

This statement assumes a regular character expansion with a legitimate Fourier pullback and unique frequency coefficients. It does not exclude nonlinear excitation spectra, singular encodings, or a different source map. It says that a proposed all-prime holonomy construction of the stated type needs unbounded charge rank, a multiplicative arithmetic space, or some independently specified replacement for the finite torus.

## 5. The separated-return singularities select the geometry

Away from the diagonal, the target kernel contains
\[
-(\log p)p^{-m/2}\bigl[\delta(x-y-m\log p)+\delta(x-y+m\log p)\bigr].
\]
The gamma and pole kernels are smooth at each nonzero prime return and do not cancel these delta distributions. Consequently any proposed kernel known to be smooth at all separated input points cannot equal the target once a prime return is active.

This applies, for example, when the proposed observable is a conventional local Euclidean two-point function with the relevant separated-point regularity. It is not a no-go theorem for local quantum field theory: extended observables, arithmetic correspondences, defect networks, quotient geometries, and Lorentzian-time observables can have different singular structures. Arithmetic \(x\) should not be identified with physical Euclidean time without checking this issue.

The existence of infinitely many singular return lengths does not itself contradict positivity. Even
\[
\|(I-U_\ell)F\|^2
=2\|F\|^2-\langle F,(U_\ell+U_\ell^*)F\rangle
\]
has negative shifted delta terms in a positive Gram kernel. The challenge is deriving the entire set of returns and their compulsory contact terms.

## 6. An exact bridge from positive arithmetic weights

Let \(\mathcal S\) be a finite set of primes and set
\[
\Lambda_{\mathcal S}(z)
=\pi^{-z/2}\Gamma(z/2)
\prod_{p\in\mathcal S}(1-p^{-z})^{-1},\qquad
w_{\mathcal S,\sigma}(\tau)=|\Lambda_{\mathcal S}(\sigma+i\tau)|^2.
\]
For \(\sigma>0\), this is a strictly positive integrable weight in \(\tau\). The gamma factor gives exponential decay; every finite prime factor has positive upper and lower bounds on a fixed vertical line. Positive critical-line measures of precisely this local-factor type appear in Connes–Consani–Moscovici's semilocal moment problem.[^ccm]

Direct differentiation, with no all-prime Euler product, gives
\[
\begin{split}
\partial_\sigma\log w_{\mathcal S,\sigma}(\tau)
={}&\Re\psi((\sigma+i\tau)/2)-\log\pi\\
&-2\sum_{p\in\mathcal S,m\ge1}(\log p)p^{-m\sigma}
\cos(m\log p\,\tau).
\end{split}
\]
Each repetition series converges absolutely for finite \(\mathcal S\) and \(\sigma>0\). At \(\sigma=1/2\), denote this multiplier by \(m_{\mathcal S}(\tau)\). If \(\mathcal S\) contains every prime with \(\log p<L\), then
\[
W_L=E_L^*m_{\mathcal S}(D)E_L+P_L
\]
as forms, where \(P_L\) is the rank-two pole operator. Extra inactive translations vanish on compression.

Thus the *entire pole-free target* is a logarithmic normal derivative of a natural positive arithmetic weight. It is not that weight's positive norm. This identity makes the missing task precise without solving it.

## 7. Normalization makes a positive generator and exposes the missing contact

Define
\[
\widetilde w_{\mathcal S,\sigma}(\tau)
=\frac{w_{\mathcal S,\sigma}(\tau)}{w_{\mathcal S,\sigma}(0)},\qquad
c_{\mathcal S}=w_0-2\sum_{p\in\mathcal S,m\ge1}(\log p)p^{-m/2}.
\]
Then the preceding identity implies
\[
\left.\partial_\sigma\log\widetilde w_{\mathcal S,\sigma}(\tau)\right|_{1/2}
=B(\tau^2)+2\sum_{p\in\mathcal S,m\ge1}
(\log p)p^{-m/2}[1-\cos(m\log p\,\tau)]\ge0.
\]
Consequently the exact finite-interval identity can also be written
\[
Q_L[f]=K[E_Lf]
+\sum_{p\in\mathcal S,m\ge1}(\log p)p^{-m/2}
\|E_Lf-U_{m\log p}E_Lf\|^2
+c_{\mathcal S}\|f\|^2+P_L[f].
\]
The infinite sum over repetitions is finite as a bounded form at fixed \(\mathcal S\). Inactive returns contribute \(2(\log p)p^{-m/2}\|f\|^2\), canceled by their contribution to \(c_{\mathcal S}\).

The first two terms have an explicit positive energy interpretation. The last two terms are precisely what cannot be removed by normalizing the state and declaring success. In particular \(c_{\mathcal S}<0\). The pole form has a positive even and negative odd component. This recovers the correct signed target rather than a favorable normalization of it.

It also explains why building independent stable prime oscillators is easy but insufficient: their positive jump energies force diagonal companions. Supersymmetry must explain the complete contact and pole accounting if it is to complete this route.

The all-prime limit makes this a structural problem. For nonzero \(F\) supported in an interval of length \(L\), every shift \(h>L\) has \(\|F-U_hF\|^2=2\|F\|^2\). The positive prime-jump energy therefore diverges already through \(\sum_{p>e^L}(\log p)p^{-1/2}\). The full finite-interval Weil expression stays finite because these inactive off-diagonal translations vanish and the matching diagonal terms cancel. A limit of the positive energies alone is not the desired renormalized form.

### Fixed primes cannot support the full pole form at every length

There is a complementary exact exclusion. Keep a finite prime set \(\mathcal S\) fixed, retain the full gamma and signed pole forms, and omit all other primes. The resulting form \(Q_{\mathcal S,L}\) is negative on some sufficiently long intervals, unconditionally.

Choose an even nonnegative \(g\in C_c^\infty((-a,a))\) with \(\|g\|_2=1\), let \(c_g=\int g(y)\cosh(y/2)\,dy>0\), and define
\[
F_R(x)=\frac{g(x-R)-g(x+R)}{\sqrt2},\qquad R>a.
\]
The bumps are disjoint, so \(\|F_R\|_2=1\), \(C(F_R)=0\), and
\[
P[F_R]=-4c_g^2\sinh^2(R/2).
\]
The Fourier identity \(|\widehat F_R|^2=2\sin^2(R\tau)|\widehat g|^2\) implies \(K[F_R]\le2K[g]\). The total fixed-prime translation norm is at most \(2A_{\mathcal S}\), where
\[
A_{\mathcal S}=\sum_{p\in\mathcal S}\frac{\log p}{\sqrt p-1}<\infty.
\]
Thus, whenever \(L>2R+2a\),
\[
Q_{\mathcal S,L}[F_R]\le
2K[g]+w_0+2A_{\mathcal S}-4c_g^2\sinh^2(R/2)\longrightarrow-\infty.
\]
This is not a counterexample to the full Weil form: its growing set of active primes was deleted. It prevents an impossible proposed benchmark. One-prime all-repetition amplitude identities are legitimate, but a full norm identity including poles must be tested only on supports for which the finite set contains every active prime, and the set must grow with support.

## 8. The flat-frame obstruction to a naive tt* identification

For finite \(\mathcal S\), \(\Lambda_{\mathcal S}\) is holomorphic and nonzero on \(\Re z>0\). If one simply declares
\[
g(z,\bar z)=|\Lambda_{\mathcal S}(z)|^2
\]
to be a Hermitian metric on a holomorphic line, then
\[
\bar\partial\partial\log g=0.
\]
It is globally the constant metric in a different holomorphic frame on that half-plane. Under \(e\mapsto h(z)e\),
\[
g\mapsto |h|^2g,\qquad
\partial_\sigma\log g\mapsto
\partial_\sigma\log g+2\Re(h'/h).
\]
Already \(h(z)=e^{cz}\) changes the putative arithmetic contact by the arbitrary constant \(2\Re c\), without producing any curvature.

This does not make the arithmetic weight meaningless: a distinguished arithmetic source or Mellin normalization can fix its frame. It does show why the weight alone is not a nontrivial tt* theory or a frame-invariant positive observable. A proposed metric mechanism must independently fix the physical sources, adjoint, and normalization, and explain why its relevant derivative is meaningful.

An equivalent physical problem occurs for supersymmetric zero states. The equation \(\mathcal Q\Psi_\sigma=0\) permits multiplication by an arbitrary nonzero scalar depending on \(\sigma\). The Hamiltonian determines a ray, not the external source normalization needed for a logarithmic norm derivative.

## 9. The pole term is not supplied by a scalar completion factor

For \(z=1/2+i\tau\),
\[
2\Re\left(\frac1z+\frac1{z-1}\right)=0.
\]
Therefore replacing \(w_{\mathcal S}\) by \(|z(z-1)|^2w_{\mathcal S}\) does not add the required pole term to the ordinary normal derivative on the critical line.

The desired pole kernel is instead
\[
P_L(x,y)=2\cosh((x-y)/2).
\]
It is a finite-interval distributional/contour contribution in the explicit formula. Turning it into a physical sector requires that operation to be derived; multiplying a positive scalar weight by the completion polynomial is insufficient.

The complete xi function emphasizes the issue. Its functional equation and real structure imply
\[
\left.\partial_\sigma\log|\xi(\sigma+i\tau)|^2\right|_{\sigma=1/2}=0
\]
at every point where \(\xi\ne0\). This does not say that the Weil distribution vanishes. It says that a pointwise derivative on that line loses the zero, residue, and boundary-value information carried by the explicit formula. One may not replace the causal contour prescription in the background by analytic continuation of a finite-prime pointwise score.

## 10. Conditional metric equations do not supply physical polarization

The tt* equations relate an actual ground-state metric, connection, and operator multiplication data; they are a mechanism for constraining the metric.[^tt]
Formal equations alone do not guarantee a positive solution for arbitrarily chosen arithmetic data. Even a constant scalar negative metric, with scalar commuting multiplication operators, satisfies the flatness equations and elementary algebraic reality relations. Positive polarization and physically selected boundary conditions are additional information.

A finite moment matrix built from \(w_{\mathcal S,\sigma}\) is genuinely positive:
\[
G_{jk}=\int_{\mathbb R}\tau^{j+k}w_{\mathcal S,\sigma}(\tau)\,d\tau.
\]
Its determinant has the positive Vandermonde representation
\[
\det G_{0\le j,k<n}
=\frac1{n!}\int_{\mathbb R^n}
\prod_{i<j}(\tau_i-\tau_j)^2
\prod_i w_{\mathcal S,\sigma}(\tau_i)\,d\tau_i.
\]
All moments exist at finite \(\mathcal S\). This produces nontrivial positive matrix geometry rather than just a scalar frame, and is a credible object to compare with Toda/tt* constructions. It is not itself a construction of extended supersymmetry, nor an identity with \(Q_L\). In particular, a positive Hessian or covariance obtained from a partition function is usually a *second* derivative; the target here is the displayed first normal derivative plus poles.

## 11. Compatibility of Hilbert spaces across support lengths

An infinite arithmetic state space is necessary in the broad program but does not remove domain requirements. The existing positive-factorizations investigation proves that the full central Weil form cannot be a closable norm factor on ordinary whole-line \(L^2(\mathbb R)\) containing every compactly supported smooth test.

The mechanism is informative. Such a factor would first imply RH; then the explicit formula would identify its norm with discrete zero sampling \(\sum_\gamma m_\gamma|\widehat f(\gamma)|^2\). Choosing increasingly broad, increasingly small \(L^2\) wave packets concentrated at one sampling frequency contradicts closability. Finite-interval forms do not have that sequence within one fixed interval.

A field-theoretic construction can instead use the test-function topology and compatible interval state spaces, as distributional observables naturally do. It must not silently replace these with a bounded source embedding followed by a closed operator on ordinary whole-line \(L^2\). Neither a formal infinite tensor product nor an uncontrolled cutoff limit resolves this point.

## 12. A useful criterion for promoting a candidate

A candidate should be promoted beyond a benchmark only when it supplies at least one new structural bridge, with its assumptions stated:

1. An independently positive boundary pairing whose first nontrivial arithmetic sector has the correct full kernel, normalization, and poles.
2. A polarized metric or supersymmetric identity converting the exact arithmetic logarithmic derivative into a norm, while fixing its frame and boundary terms.
3. An independently passive bulk realization of the shifted completed-zeta transfer, with the required causal analytic domain and support compatibility.

The third possibility is a structural energy route, not a numerical contraction estimate. De Branges/canonical-system theory describes the relevant positive transfer geometry, but assuming the needed inner/Hermite–Biehler property of the zeta input would insert an unresolved RH condition.[^canonical]

A theory that produces a gamma function, an Euler product, a positive Hamiltonian, a finite matrix metric, or a protected index has passed an interesting preliminary test. It has not yet passed one of these promotion tests.

## Sources

[^suzuki]: Masatoshi Suzuki, [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096v2), 2026, especially the definition of the full distribution, finite-interval closed forms, and the explicitly conditional discussion of the infinite Hilbert space.
[^ccm]: Alain Connes, Caterina Consani, Henri Moscovici, [On q-series and the moment problem associated to local factors](https://arxiv.org/abs/2403.01247), 2024. The positive local-factor measure is literature; the normal-derivative, normalization, and flat-frame comparisons above are deductions made for this investigation.
[^tt]: Boris Dubrovin, [Geometry and integrability of topological-antitopological fusion](https://arxiv.org/abs/hep-th/9206037), 1992. The arithmetic compatibility tests above do not assume a tt* realization exists.
[^canonical]: Masatoshi Suzuki, [A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/abs/1204.1827), 2012. The shifted transfer and its causal prescription are also defined in the local background, without invoking its equation numbers.
