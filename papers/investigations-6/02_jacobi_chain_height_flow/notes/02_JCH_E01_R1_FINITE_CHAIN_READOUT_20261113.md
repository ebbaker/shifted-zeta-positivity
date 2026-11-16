# JCH-E01 r1 — Real-height scalar error for the finite principal chain

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Execution dispatch selected
**gpt-6.1-sol / ultra**. Actual backend model and effort unavailable.
**Status: proved in-note.** [Frozen request](../research-progress/handoffs/JCH-E01-r1.md)
SHA-256 048d40e9ab7990d9f1da7d08dbb74020c59cd38602e7383c9c09afe9ae4740b7.
The [input manifest](../numerics/01_JCH_E01_R1_INPUT_MANIFEST_20261113.json)
has the prescribed SHA-256
6fafa20add1debfbe74378e42e2c044d34a34b9c6bec5d0f1ce4d0c35b40273d.
All nine entries matched their SHA-256 and byte counts before use.

This is an intermediate approximation estimate under [avoid 01][a01].
Its scope is governed by the [result index][results], [avoid index][avoid],
[controls 12][controls], [control-premise rule][a02] and [scope rule][a07].
The estimate specializes classical Gaussian quadrature to the inherited
fixed theta chain. Section 5 accounts for the acquisition cost and scope
of its signed scalar output.

## 1. Fixed source, chain and finite Gaussian rule

Use the complete even positive [theta source][source]. Write \(W_*=e^{u^2/2}\Phi\),
\(Z_*=\int_{\mathbb R}W_*\,du>0\), and \(d\mu_*=W_*\,du/Z_*\).
The source domination for all fixed Gaussian moments gives
\(M_1=\int e^{u^2}\,d\mu_*<\infty\) and all polynomial moments.
The [inherited construction][chain], §§2–3, transports multiplication
\(U f(u)=uf(u)\) with domain \(\{f:uf\in L^2(\mu_*)\}\) to \(J_*\)
in the complete orthonormal polynomial basis \((p_n)\). In particular
\(e_0\) corresponds to \(p_0=1\). Every finite polynomial vector belongs
to the domain of any fixed power of \(J_*\).

Let \(a_n>0\) join \(e_{n-1}\) to \(e_n\), and let \(P_n\) be monic
with \(p_n=P_n/\sqrt{h_n}\), \(h_n=\int P_n^2\,d\mu_*\).
Comparing the leading terms in \(up_{n-1}=a_np_n+a_{n-1}p_{n-2}\)
gives \(a_n=\sqrt{h_n/h_{n-1}}\). Since \(h_0=1\),
\(h_N=\prod_{j=1}^Na_j^2\). For \(N\ge1\), \(J_N\) is the leading
\(N\)-site principal matrix, on \(e_0,\ldots,e_{N-1}\).

For \(x\) real and \(0\le\tau\le1/2\), the spectral calculus gives
\[
\begin{aligned}
 H_{1/2-\tau}(x)
   &=\frac{Z_*}{2}\langle e_0,e^{-\tau J_*^2}e^{ixJ_*}e_0\rangle,\\
 H_N(\tau,x)
   &=\frac{Z_*}{2}\langle e_0,e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle .
\end{aligned}
\tag{R1}
\]
The infinite operators in the readout are bounded for this domain.
The physical clock is \(\lambda=1/2-\tau\), so \(W_*e^{-\tau u^2}=W_\lambda\),
\(\partial_\tau H=\partial_x^2 H\) for \(H=H_{1/2-\tau}\), and
\(\partial_\lambda H_\lambda=-\partial_x^2 H_\lambda\).
The fixed normalization is \(Z_*/2\), and real Newman height \(x\) is
twice zeta height.

The tridiagonal determinant recurrence for \(\det(uI-J_N)\), with
degrees zero and one initialized to \(1,u\), is the monic
orthogonal-polynomial recurrence \(P_{n+1}=uP_n-a_n^2 P_{n-1}\).
Consequently the nodes \(u_i\) are the roots of \(P_N\). They are real
by symmetry of \(J_N\). A zero first component of an eigenvector forces
the whole vector to vanish by the site equation and positivity of the
internal couplings. Thus the first-component map is injective on each
eigenspace, the roots are simple, and the weights
\(w_i=|\langle e_0,v_i\rangle|^2\) of unit eigenvectors are strictly
positive and sum to one. The diagonal parity map \(e_j\mapsto(-1)^j e_j\)
conjugates \(J_N\) to \(-J_N\) and fixes \(e_0\). Its scalar measure is
therefore even, as is \(\mu_*\), so both readouts in (R1) reduce to real
cosine integrals.

For \(0\le r\le 2N-1\), the expansion of \(\langle e_0,J_*^re_0\rangle\)
through the tridiagonal matrix is a finite sum over return walks. Any
walk reaching site \(N\) and returning to site zero needs at least \(2N\)
steps. Thus these moments agree with those of \(J_N\) and one has
\[
 \int q\,d\mu_* = \sum_{i=1}^N w_i q(u_i),\qquad \deg q\le 2N-1 .
 \tag{1}
\]
This proves the positive Gaussian rule here on \(\mathbb R\) using finite
moments, with no finite support interval required. At degree \(2N\) the
only contributing walk lost by the cut reaches \(N\) in \(N\) steps and
returns in \(N\) steps, with weight \(h_N\). The quadrature and spectral
identifications agree with [DLMF §§3.5(v)–(vi)][dlmf], whose passages are
recorded in the [reference note][ref].

## 2. Real Hermite remainder and Gaussian averaging

For real \(s\), let \(I_s\) be the polynomial of degree at most \(2N-1\)
matching \(f_s(u)=\cos(su)\) and its first derivative at each node \(u_i\).
The \(2N\) interpolation conditions determine \(I_s\) since their
homogeneous problem forces divisibility by \(P_N^2\), and the domain and
target of this linear map both have dimension \(2N\).

For each \(u\) distinct from the nodes, put
\(c=(f_s(u)-I_s(u))/P_N(u)^2\). The real function
\(r=f_s-I_s-cP_N^2\) has a double zero at every node and a zero at \(u\).
Apply repeated Rolle on the finite real interval spanned by the nodes
and this \(u\), also when \(u\) lies outside the node interval. At each
differentiation, zeros of order at least two retain one lower order and
every gap between distinct zeros supplies a zero. Thus \(r^{(2N)}\) has
a zero \(\xi\) there. Monicity of \(P_N^2\) gives
\(c=f_s^{(2N)}(\xi)/(2N)!\). At a node the interpolation error is zero.
For every \(u\in\mathbb R\), this proves
\[
 |\cos(su)-I_s(u)|\le P_N(u)^2\frac{|s|^{2N}}{(2N)!}.
 \tag{2}
\]
The right side and the interpolant are integrable. Exactness (1) and
matching the node values yield, with \(Q_N[f]=\sum_i w_i f(u_i)\),
\[
 \left|\int \cos(su)\,d\mu_* - Q_N[\cos(s\,\cdot)]\right|
 \le h_N\,\frac{|s|^{2N}}{(2N)!}.
 \tag{3}
\]

For \(G\sim N(0,1)\), its characteristic function gives
\(e^{-\tau u^2}\cos(xu)=\mathbb E\cos((x+\sqrt{2\tau}G)u)\), including
the deterministic case \(\tau=0\). Cosine is bounded by one and both
measures are probabilities, so Fubini applies to the full integral and
the finite sum. The Gaussian moment on the right of (3) is finite.
Odd centered moments vanish. Integration by parts in the Gaussian
density gives \(\mathbb E G^{2k}=(2k-1)\mathbb E G^{2k-2}\) for \(k\ge1\),
hence \(\mathbb E G^{2k}=(2k)!/(2^k k!)\) including \(k=0\). Expansion gives
\[
 \frac{\mathbb E|x+\sqrt{2\tau}G|^{2N}}{(2N)!}
 = \sum_{k=0}^N\frac{\tau^kx^{2N-2k}}{k!(2N-2k)!}
 = S_N(\tau,x).
\]
Now apply (3) inside the Gaussian average and multiply by \(Z_*/2\).
For every integer \(N\ge1\), \(0\le\tau\le1/2\), \(0\le X<\infty\)
and \(|x|\le X\), the result is
\[
 \boxed{|H_{1/2-\tau}(x)-H_N(\tau,x)|\le
         \frac{Z_*}{2}h_N S_N(\tau,x).}
 \tag{R2}
\]
Zero powers in \(S_N\) are one. At \(\tau=0\) the bound is the pure-height
cosine bound, and at \(x=0\) it is \(Z_* h_N\tau^N/(2 N!)\).
At their intersection both readouts equal \(Z_*/2\).
For \(N=1\), \(J_1=0\) and the formula uses \(h_1=a_1^2\) and
\(S_1=x^2/2+\tau\).

## 3. Complete-source envelope and sufficient integer depth

Orthogonality gives \(\int (P_N+q)^2\,d\mu_*=h_N+\int q^2\,d\mu_*\)
for every real polynomial \(q\) of degree less than \(N\). This minimizes
the norm among monic degree-\(N\) polynomials. The competitor \(u^N\)
then gives
\[
 h_N\le \int u^{2N}\,d\mu_*\le N! M_1,\qquad
 M_1=\frac{1}{Z_*}\int_{\mathbb R}e^{3u^2/2}\Phi(u)\,du ,
\]
using \(u^{2N}/N!\le e^{u^2}\). This moment is from the complete source
domination, and the readout keeps the frozen physical time interval.
All terms in \(S_N\) are nonnegative and nondecreasing in \(\tau\) and
\(|x|\). With \(T_0=1/2\), substituting \(j=N-k\) gives
\[
 \begin{aligned}
 N! S_N(T_0,X)
  &=T_0^N\sum_{j=0}^N\frac{N!}{(N-j)!}
                    \frac{(X^2/T_0)^j}{(2j)!}\\
  &\le T_0^N\sum_{j=0}^\infty
                    \frac{(N X^2/T_0)^j}{(2j)!}
   =2^{-N}\cosh(X\sqrt{2N}) .
 \end{aligned}
\]
Thus
\[
 \boxed{\sup_{0\le\tau\le1/2,\,|x|\le X}|H_{1/2-\tau}(x)-H_N(\tau,x)|
  \le C_* 2^{-N}\cosh(X\sqrt{2N}),\qquad C_*=\frac{Z_*M_1}{2}.}
 \tag{R3}
\]
For \(\epsilon>0\), let \(L=\log 2\), \(b=\sqrt2 X\) and
\(d=\max(0,\log(C_*/\epsilon))\). Since \(\cosh t\le e^t\) for \(t\ge0\),
it suffices that \(LN-b\sqrt N\ge d\).
The nonnegative root of \(Ly^2-by-d=0\) is \((b+\sqrt{b^2+4Ld})/(2L)\),
and the quadratic is nonnegative after this root. A sufficient integer is
\[
 N\ \ge\ \max\left(1,\left\lceil
 \left(\frac{b+\sqrt{b^2+4Ld}}{2L}\right)^2
 \right\rceil\right).
 \tag{R4}
\]
If \(X=0\) the square of the root is \(d/L\). If \(d=0\), the root is
\(b/L\), and if \(X=d=0\) the cutoff is \(1\).
For fixed \(X\), \(-LN+b\sqrt N\to-\infty\), giving uniform convergence
on the stated rectangle. The constants in R2–R4 pass without correction.

## 4. Actual control recheck

The proof uses a positive even probability measure, the stated moments,
a nondegenerate polynomial Gram matrix through degree \(N\), and the
physical cosine observation. For finite support with \(q\) distinct
atoms, (1)–(3) apply for \(N<q\) and the \(q\)-site matrix represents
multiplication exactly. There are only \(q\) orthonormal sites, so
\(a_q=0\) denotes termination. Exactness of the terminating chain handles
this case directly. As listed in the [B01 control screen][screen] and
[control cluster 12][controls], the witnesses apply as follows.

- For \(F_\lambda(x)=2+2e^{\lambda-T}\cos x\), \(0<T\le1/2\), put
  \(E=e^{1/2-T}\). At the fixed base, \(Z_*^{F}/2=2(1+E)\) and the
  probability measure has total mass \(p=E/(1+E)\) split at \(u=\pm1\),
  with mass \(1-p\) at zero. Here \(P_1=u\), \(P_2=u^2-p\),
  \(h_1=p\), \(h_2=p(1-p)\). The \(3\)-site matrix has
  \(a_1^2=p\), \(a_2^2=1-p\), and characteristic polynomial
  \(u(u^2-1)\). The three eigenvector weights reproduce the three atomic
  masses by (1), or by the norms of the three-dimensional multiplication
  representation. Its scalar output is exactly
  \(2(1+E)[1-p+pe^{-\tau}\cos x]\), which equals \(F_{1/2-\tau}(x)\).
  At \((\tau,x)=(1/2-T,\pi)\), \(F=F_x=0\), \(F_{xx}=2\) and the
  scalar approximation error is zero when the height box contains
  \(\pi\). The missing theta premises are infinite support, the complete
  theta profile/arithmetic, and eventual threshold simplicity.
- Euler-factor controls \(\Phi_{1/2,p}\) retain positivity, evenness and
  complete Gaussian moments by their finite translated theta sums.
  The sources of the positive-threshold witnesses satisfy the generic
  estimate with their own constants. They fail unchanged canonical theta arithmetic.
- The certified three- and four-square events at \(T=1/4\) and
  \(T=1/100\) retain the quadrature premises after even extension of the
  positive half-line source. Their stated event heights are about
  \(44.1303\) and \(83.5324\), respectively. Full smooth reflection and
  complete coefficients fail. The event times are distinct from finite
  all-real thresholds.
- The reflected super-Gaussian control at \((\lambda,x)=(1/4,\pi/4)\)
  satisfies the moment constraints by its super-Gaussian tail.
  The smooth shape and positive-primitive controls also retain the
  required complete moments and admit positive-time events. All
  lack the canonical integer-square theta expansion. Primitive endpoint
  information does not enter (R2).
- The finite-prime-orbit controls have the needed tails on each fixed
  positive source. Full reflection and unchanged infinite arithmetic fail,
  and the high-gap event locations may lie outside a chosen height box.
  The estimate uses one source at a time with its own constants.
- Finite-profile threshold families and the atomic fixed-event controls
  terminate exactly on their full atomic supports. Compact continuous
  extensions have the required moments. Full theta profile/arithmetic
  and the atomic examples' eventual threshold simplicity fail.
- The RH-conditional normalized endpoint controls fall under the
  generic estimate in the regimes where their conditional construction
  applies and their tails give \(M_1\). They lack ordinary Dirichlet
  series arithmetic, and the escaping doubles require a box containing
  the particular event.
- The fixed-source polynomial-kernel control can retain \(J_*\).
  It fails the literal cosine observation and physical Newman equation,
  so (R2) for cosine cannot serve as a bound for that alternative output.

For controls satisfying the scalar approximation premises, any valid
error allowance \(E_N\) at a zero in the box satisfies
\(|H_N|\le E_N\) there. The exact three-site control demonstrates this
even at zero actual error. This is a scope test of the approximation
estimate and supplies no theta sign inference. The assessment uses
existing witness records and the exact atomic calculation.

## 5. Baseline, boundary and practical inputs

Direct Gaussian quadrature with the same nodes and weights has output
\((Z_*/2)\sum_i w_i e^{-\tau u_i^2}\cos(xu_i)\), exactly the scalar
output in (R1). This supplies an absolute convergence theorem for that
matched evaluation class, with computational savings unestablished.

The boundary matters twice. The squared finite generator is
\(J_N^2\), with
\[
 \Pi_N J_*^2\Pi_N\big|_{\operatorname{ran}\Pi_N}
 = J_N^2+a_N^2 |e_{N-1}\rangle\langle e_{N-1}| .
\]
The separately evolved finite scalar is compared to the exact scalar.
The \(e_0\) coefficient of the projection of the exact state is already
the exact readout, while the exact-state prefix tail measures the loss
in projecting the entire state. The R2 upper bound concerns the former
finite-operator readout difference only. The omitted coupling \(a_N\)
still enters \(h_N\) and is essential to R2.

A sharper certified R2 enclosure requires enclosures on
\(a_1,\ldots,a_{N-1}\) for \(J_N\), \(a_N\) for \(h_N\) (or a certified
bound on \(h_N\)), and \(Z_*\) for the readout. Acquiring them from the
source requires complete integral/tail enclosures for the normalized
moments through order \(2N\) for the norm, with reliable recurrence or
Gram linear algebra and certified finite evaluation/rounding. R3 can
use a certified upper bound on \(M_1\) and \(Z_*\), or directly on
\(Z_* M_1/2=\frac12\int e^{3u^2/2}\Phi\,du\). It avoids obtaining
\(a_N\) for the allowance but still needs finite-chain coefficients and
readout normalization to evaluate \(H_N\). The analytic formula R4
can use any certified upper bound on \(C_*\). Neither these practical
inputs nor a numerical depth are certified here. No coefficient
asymptotic enters the proof. A relative estimate would require a
separate nonzero lower bound for \(|H_{1/2-\tau}(x)|\), which is absent.
A large allowance supplies an upper bound of limited precision and
gives no lower bound on actual error. The claimed domain and norm are
bounded real rectangles and absolute scalar error.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[screen]: 01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md
[source]: ../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex
[chain]: ../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md
[dlmf]: https://dlmf.nist.gov/3.5
[ref]: ../references/01_DLMF_GAUSS_QUADRATURE_20261113.md
