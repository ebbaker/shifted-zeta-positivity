# VCD-GT-E01 r1 — Signed quadrature error at physical heat time

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit task dispatch
**gpt-6.1-sol / ultra**. Separate backend verification of that configuration
and actual lead model and effort are unavailable.

**Proved in-note within the frozen scope.** This is an intermediate
approximation estimate and conditional consumer. The seven source hashes
in the [request][request] matched. For every fixed compact
\(I\subset[0,1/2]\), all the estimates below use constants common to the
whole range \([0,1/2]\). [Plan §3][plan] [Branch overview][overview]
[Result index][results] [Coefficient cluster][cluster] [Avoid index][avoid]
[Classification][a01] [Control screening][a02] [Scope][a07]

## 1. Physical measure and uniform inputs

For real \(\lambda\in I\) use the entire theta sum, its even extension,
and the normalization
\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 Z_\lambda=\int_{\mathbb R}W_\lambda(u)\,du>0,\qquad
 d\mu_\lambda(u)=\frac{W_\lambda(u)}{Z_\lambda}\,du,\qquad
 F_\lambda(z)=\int e^{izu}\,d\mu_\lambda(u)=\frac{2H_\lambda(z)}{Z_\lambda}.
\]
Write \(P_n\) for the monic orthogonal polynomial at this time,
\(h_n^*=\int P_n^2\,d\mu_\lambda\), \(\beta_0=0\) and
\(\beta_j=h_j^*/h_{j-1}^*>0\) for \(j\ge1\). All these objects can depend
on \(\lambda\). The unnormalized norms \(h_n=\int P_n^2 W_\lambda\,du\)
give \(h_n^*=h_n/Z_\lambda\), \(h_0^*=1\) and
\(h_N^*=\prod_{j=1}^N\beta_j\). In particular, the coefficients are
the same ratios for both measures. Parity of \(P_n\) follows by uniqueness
and evenness. The corresponding Jacobi matrix has zero diagonal and
link \(\sqrt{\beta_j}\) between sites \(j-1,j\).

For fixed degree and fixed \(R\), the heat weight costs at most
\(e^{u^2/2}\) in the inherited majorant
\(C e^{|u|}\rho(u)^2 e^{-\rho(u)}\) for \(\Phi(u)\), where
\(\rho(u)=\pi e^{4|u|}\). Even with a fixed polynomial factor and
\(e^{R|u|}\), it is integrable. All finite source moments are continuous
in \(\lambda\) by this domination and \(Z_\lambda\ge Z_0>0\). The
coefficients of \(P_n\) solve the monic orthogonality system whose Gram
matrix is positive definite for each \(\lambda\). At each fixed degree
they and \(h_n^*\), \(1/h_n^*\) are continuous and bounded on \(I\).
The same compact domination is therefore available for the fixed-degree
law below.

The quantitative inputs are precisely the two consequences of the
parent score estimate, on the complete source and throughout
\(0\le\lambda\le1/2\):
\[
 d\nu_{n,\lambda}(u)=P_n(u)^2 d\mu_\lambda(u)/h_n^*,\qquad
 \mathbb E_{\nu_{n,\lambda}}\cosh(4U)\le 2n+12,\qquad
 \beta_n+\beta_{n+1}\le B_n:=\frac{\operatorname{arcosh}^2(2n+12)}{16}.
 \tag{1}
\]
Indeed \(\nu_{n,\lambda}=P_n^2W_\lambda\,du/h_n\). The parent integrates
\((uP_n^2W_\lambda)'\) to obtain
\(\mathbb E_{\nu_{n,\lambda}}[u(-\log W_\lambda)']=2n+1\), with
vanishing end terms by its tail bound. It uses
\(u(-\log W_\lambda)'\ge\cosh(4u)-11\) uniformly on the time range.
Jensen in \(u^2\) and the multiplication recurrence then give the
adjacent envelope. This uses the full heat tilt in both the score and the
probability law. [Parent E01 §§1–3][envelope] [Manuscript §2][source]
[Manuscript §10.4][ms]

## 2. Entire law and moments

Use \(N\ge1\), \(d=2N\), \(M=d+1\), and
\(J_{N,\lambda}=J_\lambda|_{\{0,\ldots,N-1\}}\) as a principal block.
Its characteristic polynomials obey the monic recurrence by determinant
expansion, so its eigenvalues \(x_j\), \(1\le j\le N\), are the
zeros of \(P_N\). The row recurrence with positive links forces every
eigenvector with zero first entry to vanish, so the eigenvalues are
simple and the spectral weights at \(e_0\) are positive. Alternating
site signs conjugate the block to its negative and fix \(e_0\), making
the node multiset and its spectral rule even. Denote that rule by
\(Q_N f=\sum_j w_jf(x_j)\) and set
\(G_{N,\lambda}(z)=e_0^{\mathsf T}e^{izJ_{N,\lambda}}e_0\).
Then \(G_{N,\lambda}=Q_N(e^{iz\cdot})\) and \(Q_N 1=1\).
The moment walks from site zero agree with their prefix versions
through length \(2N-1\). The first walk lost at length \(2N\) travels
monotonically to \(N\) and back, with weight \(\prod_{j=1}^{N}\beta_j\).
The rule is therefore exact through degree \(2N-1\).

Let \(S=(S_0,S_{1,1},S_{1,2},\ldots,S_{N,1},S_{N,2})\) have uniform
probability on the simplex with \(M\) coordinates and let
\(U\sim\nu_{N,\lambda}\) independently. Then
\[
 X_{N,\lambda}=S_0 U+\sum_{j=1}^N(S_{j,1}+S_{j,2})x_j,\qquad
 E_{N,\lambda}(z)=\mathbb E e^{izX_{N,\lambda}}.
\]
The paired simplex weights, together with \(S_0\), have Dirichlet
parameters \((1,2,\ldots,2)\). In each pair, changing variables to its
sum and one fractional coordinate supplies the sum as a Jacobian
factor. Reflection of \(U\) and permutation of the node pairs preserve
the joint law and send \(X_{N,\lambda}\) to its negative. In particular
\(E_{N,\lambda}\) is even and \(E_{N,\lambda}(0)=1\).

For the confluent remainder, the probability simplex integral of
\(\prod_i S_i^{k_i}\) is \(d!\prod_i k_i!/(d+\sum_i k_i)!\):
successive beta integrals give the numerator without \(d!\) for
coordinate volume and the integral of \(1\) is \(1/d!\) in that volume.
For knots \(t=(u,x_1,x_1,\ldots,x_N,x_N)\), the moment of the simplex
average of the knots at order \(k\) is
\(k!d!c_k(t)/(d+k)!\), where
\(\sum_{k\ge0}c_k(t)v^k=\prod_i(1-vt_i)^{-1}\).
This follows by the multinomial theorem.

Let \(I_z\) be the degree-\(\le d-1\) interpolant of \(f_z(v)=e^{izv}\)
at the doubled nodes, using both values and first derivatives. The
homogeneous data force divisibility by \(P_N^2\), so the interpolant
exists uniquely. The degree-\(\le d\) interpolant on the augmented
list \(t\) exists by the same divisibility argument, including second
derivative data if \(u=x_j\). The difference of the interpolants is
\(P_N^2\) times the leading coefficient functional \(D_tf_z\) of
the augmented interpolant. At \(v=u\) this gives
\(f_z(u)-I_z(u)=P_N(u)^2D_tf_z\). For a monomial \(v^l\), the
leading coefficient is the coefficient of \(v^{-1}\) in
\(v^l/\prod_i(v-t_i)\) at infinity, by polynomial division. It is
\(c_{l-d}(t)\) for \(l\ge d\) and zero otherwise. Termwise application
to \(f_z\) is valid for the finitely many knots and derivatives, so
\[
 D_tf_z=\frac{(iz)^d}{d!}\,\mathbb E_S e^{iz\sum_i S_it_i}.
\]
At fixed \(N\) and \(|z|\le R\), \(e^{R(|U|+\max_j|x_j|)}\) is
an integrable majorant by §1 and the node bound below. It justifies
integrating the formula against \(P_N^2 d\mu_\lambda\) and the power
series on any compact spatial disk. Since the quadrature integrates
\(I_z\) and agrees with \(f_z\) at the nodes, the entire identity is
\[
 \boxed{\quad F_\lambda-G_{N,\lambda}=L_{N,\lambda}E_{N,\lambda},
 \qquad L_{N,\lambda}(z)=q_N(z)\alpha_{N,\lambda},\qquad
 q_N(z)=(-1)^N z^{2N},\qquad
 \alpha_{N,\lambda}=\frac{\prod_{j=1}^N\beta_j}{(2N)!}>0.\quad}
 \tag{2}
\]
It has exactly the first omitted walk's coefficient, and the error
has order \(2N\) at zero. [Parent E21 §§1–3][e21] [Assessed source][e23]

Use \((M)_k=M(M+1)\cdots(M+k-1)\), \(T_j=\operatorname{tr}J_{N,\lambda}^j\),
and \(m_k=\mathbb E_{\nu_{N,\lambda}} U^k\). The doubled-node product
has even coefficients and starts as
\(\prod_j(1-v x_j)^{-2}=1+T_2v^2+(T_2^2+T_4)v^4/2+O(v^6)\)
by its formal logarithm. At fixed \(U=u\), multiply by \((1-vu)^{-1}\).
Averaging only the finite coefficient polynomials and applying the
simplex moments gives
\[
 \sigma_{N,\lambda}^2=\frac{2(m_2+T_2)}{(M)_2},\qquad
 \mathbb E X_{N,\lambda}^4
   =\frac{24m_4+24m_2T_2+12T_2^2+12T_4}{(M)_4}.
 \tag{3}
\]
The squared norms of \(uP_N/\sqrt{h_N^*}\) and
\(u^2P_N/\sqrt{h_N^*}\) from one and two steps of the orthonormal
multiplication recurrence give
\[
 m_2=\beta_N+\beta_{N+1},\qquad
 m_4=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2+\beta_{N+1}\beta_{N+2},
 \qquad T_2=2\sum_{j=1}^{N-1}\beta_j.
 \tag{4}
\]
The component at \(N-2\) is absent at \(N=1\), consistent with
\(\beta_0=0\). The unique node is then zero, \(G_{1,\lambda}=1\) and
\(S_0\) has density \(2(1-s)\). Its second and fourth moments give
\(\mathbb E X_{1,\lambda}^2=m_2/6\) and
\(\mathbb E X_{1,\lambda}^4=m_4/15\), consistent with (3).
The prefactor in (2) is \(-\beta_1 z^2/2\) at \(N=1\).
[Parent E21 §4][e21]

## 3. Explicit E22 allowance uniform in physical time

Put \(\bar L_1=\bar T_1=0\) and for \(N\ge2\) set
\[
 \bar L_N=2\sqrt{B_{N-2}}=\tfrac12\operatorname{arcosh}(2N+8),
 \qquad \bar T_N=2(N-1)B_{N-2}.
\]
By (1), \(\beta_j\le B_{j-1}\). The maximum absolute row sum
bounds the eigenvalue moduli by \(\bar L_N\). The trace identities give
\(T_2\le\bar T_N\) and \(T_4\le \bar L_N^2\bar T_N\). For \(N\ge2\),
\(\cosh(2N)\ge1+2N^2+2N^4/3>2N+8\), so \(\bar L_N<N\).
The last inequality follows since the difference
\(2N(N-1)-7+2N^4/3\) is positive at 2 and increasing for \(N\ge2\).
The \(N=1\) bound is immediate. The adjacent estimate also gives
\(m_2\le B_N\), \(m_4\le 3B_{N+1}^2\) using (4).
Define
\[
 \mathcal V_N=\frac{2(B_N+\bar T_N)}{(M)_2},\qquad
 \mathcal Q_N=
 \frac{72 B_{N+1}^2+24B_N\bar T_N+12\bar T_N^2+
                   12\bar L_N^2\bar T_N}{(M)_4}.
 \tag{5}
\]
They bound the variance and fourth moment in (3).

For the exponential allowance, fix \(s=S_0\) and rescale the
remaining simplex coordinates by \(1-s\). The Jacobian
\((1-s)^{d-1}\) gives density \(d(1-s)^{d-1}\) for \(s\) and
independent uniform rescaled coordinates. Grouping them in pairs gives
Dirichlet weights \(W_j\) of parameters \((2,\ldots,2)\).
For \(V=\sum_j W_jx_j\), we have \(X_{N,\lambda}=sU+(1-s)V\)
with \(s,U,V\) independent. For each \(k\), expanding with the
simplex moments gives \(\mathbb E V^k/k!=A_k/(d)_k\), where \(A_k\)
is the coefficient of \(v^k\) in \(\prod_j(1-vx_j)^{-2}\).
This product is \(\prod_{x_j>0}(1-v^2x_j^2)^{-2}\), with nonnegative
even coefficients and vanishing odd ones. For real \(t\) with
\(|t|\bar L_N<d\), using \((d)_k\ge d^k\) and then
\(-\log(1-v)\le v/(1-v)\) for \(0\le v<1\) gives
\[
 \mathbb E e^{tV}
 \le \prod_j(1-tx_j/d)^{-2}
 \le \exp\!\left(\frac{t^2T_2}{d^2(1-t^2\bar L_N^2/d^2)}\right).
\]
The node expansion is on bounded variables. For \(U\) use symmetry,
(1) and concavity of \(v\mapsto v^{t/4}\) to give
\(\mathbb E e^{tU}\le(\mathbb E e^{4U})^{t/4}\le(2N+12)^{t/4}\)
for \(0\le t\le4\). By exponential convexity and \(\mathbb E s=1/M\),
putting \(t=2Y\) yields
\[
 \mathbb E e^{2YX_{N,\lambda}}\le \mathcal A_N(Y)
 :=\frac{(2N+12)^{Y/2}}{M}+
       \frac{2N}{M}\exp\!\left(
          \frac{Y^2\bar T_N}{N^2(1-Y^2\bar L_N^2/N^2)}\right)
 \qquad(0\le Y\le1).
 \tag{6}
\]
The denominator is strictly positive throughout this range. At \(N=1\),
\(\mathcal A_1(Y)=14^{Y/2}/3+2/3\),
\(\mathcal V_1=B_1/6\) and \(\mathcal Q_1=B_2^2/5\).

For \(|\Im z|\le Y\), Taylor's integral remainder bounds
\(|e^{izv}-1-izv|\le |z|^2v^2e^{Y|v|}/2\) for real \(v\).
The linear term averages to zero. By symmetry,
\(\mathbb E e^{2Y|X_{N,\lambda}|}\le2\mathcal A_N(Y)\), so
Cauchy–Schwarz gives the uniform bound
\[
 \boxed{\quad |E_{N,\lambda}(z)-1|\le\epsilon_N(|z|,Y)
    :=\frac{|z|^2}{2}\sqrt{2\mathcal A_N(Y)\mathcal Q_N},
 \qquad \lambda\in I,\ N\ge1,\ |\Im z|\le Y\le1.\quad}
 \tag{7}
\]
Here \(B_{N+1}=O(\log^2(N+1))\),
\(\bar L_N=O(\log(N+1))\), and \(\bar T_N=O(N\log^2(N+1))\).
The source term of (6) is uniformly \(O(N^{-1/2})\), the denominator
factor tends uniformly to one, and the node exponent is uniformly
\(O(\log^2(N+1)/N)\). Hence \(\mathcal A_N(Y)\to1\) uniformly.
By (5), \(\mathcal Q_N=O(\log^4(N+1)/N^2)\) and
\(\mathcal V_N=O(\log^2(N+1)/N)\). The bound in (7) is
\(O(|z|^2\log^2(N+1)/N)\) with unrestricted \(\Re z\) in the
inequality, and gives \(E_{N,\lambda}\to1\) uniformly on
\(|\Im z|\le1,\ |z|\le r_N\) when
\(r_N\log(N+1)/\sqrt N\to0\), jointly in \(\lambda\).
Useful sector control requires the explicit \(\epsilon_N<1\).
The bound gives no height-uniform relative accuracy.

For real \(x\), averaging \(1-y^2/2\le\cos y\le1\) gives
\(1-x^2\sigma_{N,\lambda}^2/2\le E_{N,\lambda}(x)\le1\).
In particular the error sign is strictly \((-1)^N\) for
\(0<|x|<\sqrt{2/\mathcal V_N}\), and the even and odd adjacent
quadratures bracket \(F_\lambda(x)\) on the intersection of their
open sign intervals. Also
\(|E_{N,\lambda}(z)|\le\mathcal A_N(Y/2)\) by (6) and symmetry.
[Parent E22 §§2–5][e22]

## 4. Directed consumer, count, and collar logarithm

At \(z\ne0\), write \(w=G_{N,\lambda}(z)/q_N(z)\), set
\(\varepsilon=\epsilon_N(|z|,Y)\), and use the prefix amplitude bound
\[
 0<\alpha_{N,\lambda}\le A_{N,\lambda}
 =\frac{\prod_{j=1}^{N-1}\beta_j}{(2N)!}
       (B_{N-1}-\beta_{N-1}).
 \tag{8}
\]
At \(N=1\) the product is empty and \(A_{1,\lambda}=B_0/2\).
The actual normalized error belongs to the union of closed disks
\(D(a,a\varepsilon)\) over \(0<a\le A_{N,\lambda}\).
Adjoining \(a=0\) produces
\[
 \mathcal U_{N,\lambda}(z)
 =\bigcup_{0\le a\le A_{N,\lambda}}D(a,a\varepsilon)
 =\operatorname{conv}\bigl(\{0\}\cup
                     D(A_{N,\lambda},A_{N,\lambda}\varepsilon)\bigr).
 \tag{9}
\]
Convexity follows by scaling the largest disk. This compact set
is contained in the capsule of radius \(A_{N,\lambda}\varepsilon\)
around \([0,A_{N,\lambda}]\). For \(v=-w\), the exact closed-set
test is the minimum over \(0\le a\le A_{N,\lambda}\) of
\[
 |v|^2-2a\Re v+(1-\varepsilon^2)a^2.
\]
If this minimum is positive, there is strict separation. For
\(\varepsilon<1\) the minimizer is the vertex
\(\Re v/(1-\varepsilon^2)\) clamped to the interval. For
\(\varepsilon\ge1\) the minimum is attained at an endpoint.

For \(\varepsilon<1\), \(\Re E_{N,\lambda}\ge1-\varepsilon>0\).
Thus \(\Re w\ge0\) excludes a zero of \(F_\lambda\), including at
\(w=0\), and \(F_\lambda-G_{N,\lambda}\) has no nonzero zero
in this paid range. For \(v\in D(a,a\varepsilon)\), \(a>0\), the
distance from \(a\) to the line through \(0,v\) is
\(a|\sin\arg v|\le a\varepsilon\), and \(\Re v>0\). Thus an actual
zero of \(F_\lambda\) requires
\[
 0<|-w|\le A_{N,\lambda}(1+\varepsilon),\qquad
 |\arg(-w)|\le\arcsin\varepsilon .
\]
At \(\varepsilon=1\) the real-part argument loses strictness.
At \(z=0\) we have \(F_\lambda(0)=G_{N,\lambda}(0)=1\).

For the count, use the set in the original value plane
\(\mathcal D_{N,\lambda}(z)=q_N(z)\mathcal U_{N,\lambda}(z)\), with
\(\mathcal D_{N,\lambda}(0)=\{0\}\). Define
\(\delta_{N,\lambda}(z)=\operatorname{dist}(-G_{N,\lambda}(z),
\mathcal D_{N,\lambda}(z))\). Let \(\Gamma\) be a positively
oriented piecewise \(C^1\) simple closed contour in the paid strip.
If \(\delta_{N,\lambda}>0\) on \(\Gamma\), all
\(H_b=G_{N,\lambda}+b(F_\lambda-G_{N,\lambda})\), \(0\le b\le1\),
are boundary-nonzero because \(b(F_\lambda-G_{N,\lambda})\) belongs
to \(\mathcal D_{N,\lambda}\). This uses the zero-amplitude endpoint
and works for every \(\varepsilon\ge0\) allowed by (7). The
argument-principle integral of \(H_b'/H_b\) is continuous in \(b\)
and, after division by \(2\pi i\), integer valued. Thus the counts
agree with multiplicity, at each \(\lambda\) for which separation
holds. Their value still needs model evidence. The pointwise
half-plane test can pass at a model zero, where \(\delta_{N,\lambda}=0\).
[Parent E24 §§3–4][e24]

A quantitative log budget can use the same homotopy **if separation
is paid on a collar**. For a chosen open collar in the paid strip
where \(\delta_{N,\lambda}>0\), both \(G_{N,\lambda}\) and every
\(H_b\) are nonzero. The function
\[
 \mathcal L_{N,\lambda}(z)=
  \int_0^1\frac{F_\lambda(z)-G_{N,\lambda}(z)}{H_b(z)}\,db
\]
is holomorphic there. Indeed the integrand is holomorphic and uniformly
bounded on each compact subset times \(0\le b\le1\). Since
\(\partial_b H_b=F_\lambda-G_{N,\lambda}\), exponentiating this
integral gives \(F_\lambda/G_{N,\lambda}\) by solving the scalar
ordinary differential equation in the auxiliary \(b\) from \(b=0\).
No time derivative occurs here. A directly paid bound is
\[
 |\mathcal L_{N,\lambda}(z)|
 \le\frac{|q_N(z)|A_{N,\lambda}(1+\varepsilon)}{\delta_{N,\lambda}(z)}.
 \tag{10}
\]
In the numerator one can also use
\(|q_N|A_{N,\lambda}\mathcal A_N(Y/2)\) by the independent modulus
bound following (7). A uniform lower clearance and upper numerator
on the chosen collar pay a uniform budget. Alternatively, on a
zero-free model collar, a verified bound
\(|F_\lambda-G_{N,\lambda}|/|G_{N,\lambda}|\le\kappa<1\)
gives the power-series log budget \(-\log(1-\kappa)\).
Qualitative strict separation all along a compact contour in the
interior of the paid strip, for all \(\lambda\in I\), extends by
continuity to some uniform collar, since \(\delta_{N,\lambda}\) is
continuous even at \(z=0\). A quantitative bound on a specified collar
still needs its clearance or a ratio estimate. Contour contact with
the edge of the paid strip gives no collar crossing that edge from
(7). A common interior count by itself gives neither a verified
collar nor a log cost. [Manuscript §10.4][ms] [Branch overview][overview]

## 5. Actual coefficient costs and time-zero check

At each time \(G_{N,\lambda}\), its node traces, and the prefix bound
(8) use links \(\beta_1,\ldots,\beta_{N-1}\). The degree-only
allowances (5)–(7) use no actual links. Exact \(\alpha_{N,\lambda}\)
adds \(\beta_N\). Exact variance in (3)–(4) additionally uses
\(\beta_{N+1}\), and exact fourth moment uses \(\beta_{N+2}\).
The law in (2) depends on the full measure. Its exact transform is
a description of the error, beyond a finite-link evaluation.

With the exact amplitude, \(C_{N,\lambda}=G_{N,\lambda}+L_{N,\lambda}\)
has error allowance \(|L_{N,\lambda}|\varepsilon\); strict domination
by \(|C_{N,\lambda}|\) on a contour transfers its count by Rouché.
The same first \(N\) actual links specify \(G_{N+1,\lambda}\).
The first derivative that can use link \(j\) in either model germ
has order \(2j\), whose only walk to site \(j\) and back contributes
\((-1)^j\prod_{i=1}^j\beta_i\). For the correction model at \(j=N\),
the monomial supplies this term. Thus the two models have the same
actual coefficient input. At \(z\ne0\), (2) gives
\[
 \begin{aligned}
 \frac{L_{N+1,\lambda}}{L_{N,\lambda}}
    &=-\frac{\beta_{N+1}z^2}{(2N+1)(2N+2)},\\
 \frac{|F_\lambda-G_{N+1,\lambda}|}{|L_{N,\lambda}|}
    &\le \frac{(B_N-\beta_N)|z|^2}{(2N+1)(2N+2)}
             (1+\epsilon_{N+1}(|z|,Y)).
 \end{aligned}
\]
In the common bounded-phase range, for example
\(|z|\le c\sqrt{N}/\log(N+1)\) with \(c\) fixed, using \(B_N\) alone
gives an upper allowance of order \(|z|^2\log^2(N+1)/N^2\). The
explicit correction-model allowance \(\varepsilon\) has order
\(|z|^2\log^2(N+1)/N\), including its lower order bound from
\(12\bar T_N^2/(M)_4\) in (5) and \(\mathcal A_N(Y)\ge1\).
For each fixed \(N,\lambda\), the actual error quotient for the
correction over the next physical head has limit at zero
\[
 \frac{\beta_N+\beta_{N+1}+T_2}{\beta_{N+1}}>1,
\]
by \(E_{N,\lambda}-1=-\sigma_{N,\lambda}^2z^2/2+O(z^4)\)
and \(E_{N+1,\lambda}(0)=1\). This gives strict local ordering of
the actual moduli on a punctured disk at that fixed \(N,\lambda\).
The comparison of allowances gives no all-strip ordering of actual
errors. [Parent E24 §§1–2][e24] [Synthesis §3][synthesis]

At \(\lambda=0\), \(Z_\lambda=Z_0\), \(W_0=\Phi\), and the same
orthogonal polynomials, probability norms, and prefix restore the
parent E21 law and E22 constants exactly. The direction \(q_N\)
here equals the phase monomial in parent E24. The error law then
also specializes to the physical, zero modeled-memory E15 difference
through the common left side identified in E21. The present estimates
use fixed-\(\lambda\) quadrature throughout. There is no scalar
bound for a \(\lambda\)-derivative of \(E_{N,\lambda}\) in this
argument and no heat equation for \(G_{N,\lambda}\) is used.

## 6. Analytical control screen

The exact law uses the even probability measure, positive monic norms
at the required degrees, exponential moments, and the literal
Fourier observation. The uniform phase allowance additionally uses
the weighted cosh moment and adjacent envelope. The inherited
family-specific screens extend to the stated physical-time domain
where those premises hold. [Control catalog][catalog] [Parent E01 §5][envelope]
[Parent E22 §6][e22] [Parent E24 §5][e24] [Assessment E23][e23]

| Control | Premise and scope |
| --- | --- |
| Three- and four-square control sources | Positive constants cancel from the half-line summand scores under every \(0\le\lambda\le1/2\). The \(u\) factor removes the reflection junction term in integration by parts. Their own literal transforms pass both quantitative premises even at their certified collision times. They lack the full canonical reflection and complete equal square coefficients, unused by the estimate. |
| E07 finite square-mode changes and bounded positive finite-prime orbit sources | The screened weights retain the half-line score and tail domination, so these sources pass the same law and phase test at their admissible times. Unchanged complete coefficients and full reflection fail. The E07 finite-source nonreal-zero result gives no fixed location. The separate orbit double events vary the source and escape in height. |
| Euler-factor translates | Their literal transforms have the exact law. The translation changes the canonical summand score, and the \(c=1/2,p=23,\lambda=0\) member fails \(B_0\). Other member and degree bounds were untested. |
| Reflected super-Gaussian | It has the literal law and the positive-time event in the catalog. Its polynomial-growth score fails exponential confinement. Its actual degree-wise allowances were untested. |
| Smooth shape and positive-primitive sources | The exact law applies by evenness and their tails. They lack the canonical summand score, and the weaker quantitative premises remain untested in their sufficiently-small-damping families. The distinct E10/E12 compact multipliers retain confinement and the phase allowance at their stated perturbation scopes; those controls' zero locations remain open. |
| Atomic thresholds, triangular compact extensions | The atoms lack a positive density and terminate the chain. The law applies below support size at degrees with positive monic norms. The catalog's inherited three-atom event fails the adjacent bound at index one. Compact triangular extensions lack the globally positive density used in the score argument. There is no blanket coefficient verdict. |
| RH-conditional normalized endpoint controls | They retain their RH qualification and lack ordinary Dirichlet arithmetic and the canonical summand score identity. Their literal laws apply, and the weaker quantitative premises are untested. |
| Fixed amplitude with changed observation | The literal-transform estimate survives for the unchanged amplitude. The altered observable fails the Fourier readout used in (2). |
| Actual-profile positive-measure relaxation | The relaxed data lack a prescribed full-line physical source with its literal observation. |
| Local quadratic heat collision | The polynomial is a local field model. It lacks the normalized full-line positive source and Jacobi probability law used here. Its local geometry provides no test of the phase estimate. |

In the colliding controls that share (1) and (2), a contour enclosing a
nonreal zero cannot give both successful directed separation and zero
model count. That observation places no restriction on their local
separations elsewhere. The canonical geometry, actual collar log
payment, and improvement of the signed gap cost remain application
premises or research questions. The proof used no coefficient acquisition
or numerical control replay.

[request]: ../research-progress/handoffs/VCD-GT-E01-r1.md
[plan]: ../research-plan/01_VCD_GT_RESEARCH_PLAN_20261116.md
[overview]: ../research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md
[envelope]: ../../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[e21]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[e22]: ../../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[e24]: ../../notes/22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md
[synthesis]: ../../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md
[e23]: ../../reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md
[source]: ../../manuscript/main.tex
[ms]: ../../manuscript/sections/cluster_resolution.tex
[results]: ../../../../../result-summaries/README.md
[catalog]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
