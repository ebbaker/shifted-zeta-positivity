# VCD-E22 r1 — Quantitative phase of the complete quadrature error

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Proved in-note for the defined error law.** For the full theta source
at time zero, a degree-only bound gives
\(\left|\mathbb E e^{izX_N}-1\right|=O(|z|^2\log^2(N+1)/N)\) uniformly
on \(|\Im z|\le1\). The corrected-model consumers in §5 use the
quadrature-error identification stated there. The quantitative allowance
is an intermediate estimate. A contour margin and model zero count
remain unproved. The [frozen request][request] implements [decision12][decision]
after [synthesis19][e19]. See the [result index][results], [cluster18][cluster],
[control catalog12][catalog], [avoid index][avoid] and patterns
[01][a01], [02][a02], [07][a07] and [12][a12].

## 1. Distribution and elementary moments

Set \(d\mu=\Phi\,du/Z\) and \(Z=\int_{\mathbb R}\Phi(u)\,du\).
Let \(P_n\) be monic orthogonal for \(\mu\),
\(h_n^*=\int P_n^2\,d\mu\), and \(\beta_n=h_n^*/h_{n-1}^*\) for
\(n\ge1\), with \(\beta_0=0\). Use
\[
 d\nu_N=P_N^2\,d\mu/h_N^*,\qquad
 B_n=\frac{\operatorname{arcosh}^2(2n+12)}{16}.
\]
[E01 §§1–3][e01] supplies all exponential moments at fixed degree,
\(\mathbb E_{\nu_N}\cosh(4U)\le 2N+12\), and
\(\beta_n+\beta_{n+1}\le B_n\). The law \(\nu_N\) is symmetric by
evenness of \(\mu\) and the parity of \(P_N\). Write \(q=2N,\ M=q+1\).
Let \(x_1,\ldots,x_N\) be the eigenvalues of the zero-diagonal Jacobi
prefix \(J_N\) on sites \(0,\ldots,N-1\). Its edge at sites \(j-1,j\)
is \(\sqrt{\beta_j}\). Conjugation by the alternating site signs
gives the node symmetry \(x_j\mapsto-x_j\) as a multiset. These are
the simple Gaussian nodes by [E04 §5][e04].

Let \(U\sim\nu_N\) be independent of uniform probability barycentric
coordinates \((S_0,S_{1,1},S_{1,2},\ldots,S_{N,1},S_{N,2})\)
on the simplex with \(M\) coordinates. Define
\[
 X_N=S_0 U+\sum_{j=1}^N(S_{j,1}+S_{j,2})x_j .
 \tag{1}
\]
Write \(s=S_0\) and \(S_{j,b}=(1-s)R_{j,b}\). The change of
variables in the \(q-1\) independent remaining coordinates has
Jacobian \((1-s)^{q-1}\), so the joint law factors into
\(q(1-s)^{q-1}\,ds\) and uniform probability on the remaining
simplex. In particular \(S_0\) has the
\(\mathrm{Beta}(1,q)\) law and is independent of the rescaled
coordinates \(R_{j,b}=S_{j,b}/(1-S_0)\). The zero-probability
endpoint \(S_0=1\) may be discarded in forming \(R\).
Putting \(W_j=R_{j,1}+R_{j,2}\) and \(V_N=\sum_j W_j x_j\) gives
\(X_N=S_0 U+(1-S_0)V_N\) with \(U,S_0,V_N\) jointly independent.
The distribution of \(V_N\) is symmetric by a permutation of the
node pairs. Hence \(X_N\) is symmetric, centered, and
\(|X_N|\le |U|+\max_j|x_j|\). In particular \(E_N(z)=\mathbb E e^{izX_N}\)
is entire by dominated power series on each compact disk.

For integer powers \(r_i\ge0\) of uniform probability barycentric
coordinates \(R_i\) on the \(q\)-coordinate simplex, successive
integration with
\(\int_0^1 t^a(1-t)^b\,dt=a!b!/(a+b+1)!\) gives
\(\mathbb E\prod_i R_i^{r_i}=\prod_i r_i!/(q)_{\sum_i r_i}\).
Here \((b)_k=b(b+1)\cdots(b+k-1)\), with \((b)_0=1\).
The integral identity follows by repeated integration by parts,
and the factor \((q-1)!\) normalizes the uniform simplex volume.
For powers \(k_j\) of \(W_j\), the binomial expansion of each pair
sums \(k_j+1\) identical factors \(k_j!\) after the simplex integral.
Thus, with \(k=\sum_j k_j\), the grouped \(\mathrm{Dirichlet}(2,\ldots,2)\)
moment formula is
\[
 \mathbb E\prod_j W_j^{k_j}=\frac{\prod_j(2)_{k_j}}{(q)_k},\qquad
 \mathbb E[S_0^a(1-S_0)^b]=\frac{(1)_a(q)_b}{(M)_{a+b}}
 \quad (a,b\in\mathbb Z_{\ge0}).
 \tag{2}
\]
The second formula integrates the beta density.

Write \(S_2=\operatorname{tr}J_N^2=\sum_j x_j^2\) and
\(S_4=\operatorname{tr}J_N^4=\sum_j x_j^4\).
By (2), \(\mathbb E[V_N^k]/k!=A_k/(q)_k\), where \(A_k\) is the
coefficient of \(w^k\) in \(\prod_j(1-x_jw)^{-2}\) about zero.
Its logarithm has coefficients \(S_2\) at order two and \(S_4/2\)
at order four, and no odd powers by symmetry. Hence \(A_2=S_2\)
and \(A_4=(S_2^2+S_4)/2\).

To compute \(\mathbb E_{\nu_N}U^2=m_2\) and
\(\mathbb E_{\nu_N}U^4=m_4\), use
\(p_n=P_n/\sqrt{h_n^*}\) and the orthonormal multiplication
recurrence for \(u p_n\). The squared norm of \(u p_N\) is
\(m_2=\beta_N+\beta_{N+1}\). Applying the recurrence twice, the
coefficients in \(u^2p_N\) at degrees \(N-2,N,N+2\) are
\(\sqrt{\beta_N\beta_{N-1}},\ \beta_N+\beta_{N+1},\
\sqrt{\beta_{N+1}\beta_{N+2}}\), respectively. The \(N-2\) term
is omitted for \(N=1\). Therefore
\[
 m_4=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2
       +\beta_{N+1}\beta_{N+2}.
\]
Expanding the second and fourth powers of \(S_0 U+(1-S_0)V_N\)
leaves just the even powers of \(U,V_N\). The mixed fourth-moment
term is \(6\cdot 2m_2\cdot 2S_2/(M)_4\) using (2). The two pure
moments at each degree then give
\[
 \sigma_N^2=\mathbb E X_N^2=\frac{2(m_2+S_2)}{(M)_2},\qquad
 \mathbb E X_N^4=\frac{24m_4+24m_2S_2+12S_2^2+12S_4}{(M)_4}.
 \tag{3}
\]
These calculations require only finite moments of \(U\).

## 2. Payment of the full exponential weight

Let \(L\ge \max_j|x_j|\). All odd coefficients \(A_k\) vanish
and all even \(A_k\) are nonnegative, since
\(\prod_j(1-x_jw)^{-2}=\prod_{x_j>0}(1-x_j^2w^2)^{-2}\).
For real \(t\), boundedness of \(V_N\) justifies expanding its
exponential in expectation. If \(|t|L/q<1\), then \((q)_k\ge q^k\)
and the coefficient comparison yields
\[
 \mathbb E e^{tV_N}
 =\sum_{k\ge0}\frac{A_k t^k}{(q)_k}
 \le\prod_j(1-t x_j/q)^{-2}
 \le \exp\left\{\frac{t^2 S_2}{q^2(1-t^2L^2/q^2)}\right\}.
 \tag{4}
\]
For the last step, each positive node contributes
\(-2\log(1-t^2 x_j^2/q^2)\) to the logarithm of the product.
Use \(-\log(1-v)\le v/(1-v)\) for \(0\le v<1\) and
\(2\sum_{x_j>0}x_j^2=S_2\). All reciprocal series in (4) concern
the bounded nodes. The unbounded variable \(U\) is treated directly
by the source's exponential moment.

For \(0\le t\le4\), the inequality
\(\mathbb E_{\nu_N} e^{t U}\le(\mathbb E_{\nu_N} e^{4 U})^{t/4}\)
follows from concavity of the power \(t/4\). Symmetry and E01
then give the bound \((2N+12)^{t/4}\). Convexity of the real
exponential gives
\(e^{t X_N}\le S_0 e^{t U}+(1-S_0)e^{t V_N}\).
Take expectations with \(t=2Y\), \(0\le Y\le1\), and use
\(\mathbb E S_0=1/M\) and \(q=2N\). When \(Y L<N\) this gives
\[
 \mathbb E e^{2Y X_N}\le
 \frac{(2N+12)^{Y/2}}{2N+1}
 +\frac{2N}{2N+1}\exp\left\{
       \frac{Y^2 S_2}{N^2(1-Y^2L^2/N^2)}\right\}.
 \tag{5}
\]
This estimate uses a convex combination of the full exponential
moments after the beta split.

## 3. Degree-only allowances and domain

For \(N\ge2\) define
\[
 \overline L_N=2\sqrt{B_{N-2}}=\tfrac12\operatorname{arcosh}(2N+8),
 \qquad
 \overline S_{2,N}=2(N-1)B_{N-2}.
\]
The Jacobi row sums bound \(\max_j|x_j|\) by \(\overline L_N\),
since \(\beta_j\le B_{j-1}\le B_{N-2}\) for \(1\le j<N\).
Indeed, for an eigenvector, a row at a largest coordinate bounds
the modulus of its eigenvalue by the largest row sum.
Also \(S_2=2\sum_{j=1}^{N-1}\beta_j\le\overline S_{2,N}\) and
\(S_4\le\overline L_N^2\overline S_{2,N}\).
To check the denominator for all \(N\ge2\),
\[
 \cosh(2N)\ge 1+2N^2+\tfrac23N^4>2N+8.
\]
The difference from \(2N+8\) in this lower bound is
\(2N(N-1)-7+\tfrac23N^4\), positive at \(N=2\) and increasing
for \(N\ge2\). Inverting proves \(\overline L_N<N\).

At \(N=1\), \(J_1=0,\ V_1=0,\ X_1=S_0 U\) with
\(S_0\sim\mathrm{Beta}(1,2)\). Equation (3) gives
\(\mathbb E X_1^2=m_2/6,\ \mathbb E X_1^4=m_4/15\).
Set \(\overline L_1=\overline S_{2,1}=0\). The node exponential
is exactly one, so (5) gives \(\mathbb E e^{2Y X_1}
\le14^{Y/2}/3+2/3\), with equality at \(Y=0\).

For all \(N\ge1\), define the exponential allowance
\[
 \mathcal A_N(Y)=\frac{(2N+12)^{Y/2}}{2N+1}
 +\frac{2N}{2N+1}
  \exp\left\{\frac{Y^2\overline S_{2,N}}
             {N^2(1-Y^2\overline L_N^2/N^2)}\right\}.
 \tag{6}
\]
The estimates \(m_2\le B_N\) and \(m_4\le 3B_{N+1}^2\) follow
from the adjacent envelope, \(\beta_j\le B_{j-1}\) for \(j\ge1\),
and monotonicity of \(B_j\). The three terms of \(m_4\) are each
at most \(B_{N+1}^2\), using \(\beta_0=0\) at \(N=1\).
Equation (3) gives the degree-only variance and fourth-moment
allowances
\[
 \mathcal V_N=\frac{2(B_N+\overline S_{2,N})}{(M)_2},\qquad
 \mathcal Q_N=\frac{72 B_{N+1}^{2}
      +24 B_N\overline S_{2,N}+12\overline S_{2,N}^{2}
      +12\overline L_N^2\overline S_{2,N}}{(M)_4}.
 \tag{7}
\]
These also apply at \(N=1\), with \(\mathcal V_1=B_1/6\) and
\(\mathcal Q_1=B_2^2/5\).

## 4. Phase bound and convergence

Taylor's integral remainder gives
\[
 |e^{izv}-1-izv|\le \tfrac12 |z|^2 v^2 e^{Y|v|}
 \qquad(v\in\mathbb R,\ |\Im z|\le Y).
\]
The linear term vanishes in expectation. Symmetry gives
\(\mathbb E e^{2Y|X_N|}\le 2\mathbb E\cosh(2Y X_N)
=2\mathbb E e^{2Y X_N}\). Cauchy–Schwarz, (6) and (7) give
\[
 \boxed{\displaystyle
 |E_N(z)-1|\le
 \epsilon_N(|z|,Y):=\frac{|z|^2}{2}\sqrt{2\mathcal A_N(Y)\mathcal Q_N}
 \quad (N\ge1,\ |\Im z|\le Y\le1).}
 \tag{8}
\]
At \(Y=0\), the simpler bound \(|E_N(x)-1|\le x^2\mathcal V_N/2\)
follows directly from \(\mathbb E X_N^2\le\mathcal V_N\).

Since \(\operatorname{arcosh}v\le\log(2v)\) for \(v\ge1\),
\(B_{N+1}=O(\log^2(N+1))\),
\(\overline L_N=O(\log(N+1))\) and
\(\overline S_{2,N}=O(N\log^2(N+1))\).
Then \(\mathcal Q_N=O(\log^4(N+1)/N^2)\), and
\(\mathcal V_N=O(\log^2(N+1)/N)\).
In (6) the denominator factor \(1-Y^2\overline L_N^2/N^2\)
tends uniformly to one on \(0\le Y\le1\). Its exponential term
tends uniformly to one since the exponent is
\(O(\log^2(N+1)/N)\) there, and the source term tends uniformly
to zero by the \(Y=1\) bound \(O(N^{-1/2})\).
Thus \(\mathcal A_N(Y)\) is bounded uniformly and tends to one
uniformly on \(0\le Y\le1\). In particular (8) is
\(O(|z|^2\log^2(N+1)/N)\) with a common constant on the full stated
strip and unrestricted \(\Re z\). For any \(r_N\log(N+1)/\sqrt N\to0\),
\(E_N\to1\) uniformly on \(|z|\le r_N,\ |\Im z|\le1\).

## 5. Corrected-model consumer under the remainder identification

Use the identity
\[
 F-G_N=L_N E_N,\qquad
 F(z)=\int e^{izu}\,d\mu(u),\qquad
 G_N(z)=e_0^{\mathsf T}e^{izJ_N}e_0,\qquad
 L_N(z)=(-1)^N\left(\prod_{j=1}^N\beta_j\right)
                 \frac{z^{2N}}{(2N)!}.
 \tag{9}
\]
Equation (9) is the identification assigned to E21, with its completed
proof pinned in the [return addendum][return]. The estimates (1)–(8)
were derived from the law alone. The sign and coefficient in \(L_N\)
also agree with the first excluded walk of [E04 §1][e04] and the
physical \(k_N,\ell=0\) discrepancy of [E15 §§4, 6][e15].

Define the corrected finite model \(C_N=G_N+L_N\). Equations (8)–(9)
give the disk and lower modulus
\[
 |F-C_N|\le |L_N|\epsilon_N(|z|,Y),\qquad
 |F|\ge |C_N|-|L_N|\epsilon_N(|z|,Y)
 \quad (|\Im z|\le Y\le1).
 \tag{10}
\]
Thus a strictly positive right-hand side excludes an \(F\)-zero
pointwise. Since \(\beta_j>0\), an \(F\)-zero at \(z\ne0\) necessarily
satisfies \(|G_N/L_N+1|\le\epsilon_N(|z|,Y)\). At \(z=0\) both
\(F\) and \(C_N\) equal one. If a positively oriented, piecewise
\(C^1\) simple closed curve lies in the strip and
\(|C_N|>|L_N|\epsilon_N\) everywhere on the curve, then \(F,C_N\)
are both nonzero on it and have equal interior zero counts with
multiplicity. Apply Rouché to \(G=C_N,\ g=F-C_N\), both entire.
The checked passage states strict boundary domination on such
a curve. [Reference02][ref02] and [Topping, §9.9, Theorem 9.21][topping].

Evaluating \(G_N\) requires \(\beta_1,\ldots,\beta_{N-1}\).
The norm factor in \(L_N\) adds \(\beta_N\) because the probability
norm satisfies \(h_0^*=1\). Equation (10) uses these \(N\) actual
links to specify the center. The degree-only \(\epsilon_N\) and
\(\mathcal V_N\) require no deeper links. The envelope also gives
an upper allowance for \(|L_N|\) by \(\beta_j\le B_{j-1}\).
That allowance leaves the modeled modulus to be evaluated from
actual coefficients. The exact variance in (3), if used, adds
\(\beta_{N+1}\). Local uniform convergence \(C_N\to F\) follows
from that of \(G_N\) in E04 and, on \(|z|\le R\), the bound
\(|L_N(z)|\le(B_{N-1}R^2/N)^N\) using \((2N)!\ge N^N\).
Zero confinement still requires an actual contour margin and
a controlled model zero count in the chosen regions. In particular
there is no established sequence of successful shrinking-strip
contours or assertion of real-rootedness for these models.

For comparison, the loose bare disk from (8)–(9) is centered at
\(G_N\) with radius \(|L_N|(1+\epsilon_N)\) and contains the
corrected disk by the triangle inequality. An independent bare
payment gives \(|F-G_N|\le |L_N|\mathcal A_N(Y/2)\):
\(|E_N(z)|\le\mathbb E e^{-\Im(z)X_N}\), which by symmetry and
(6) is bounded by \(\mathcal A_N(|\Im z|/2)\le\mathcal A_N(Y/2)\).
On the real axis this bare radius is \(|L_N|\). At \(x\ne0\) and
\(0<\epsilon_N(|x|,0)<1\), that disk and the corrected disk have
center separation \(|L_N|\) and neither contains the other.
The center \(G_N+L_N\) retains the leading phase, which can matter
for the exclusion test. For instance, at any nonzero point with
\(G_N=0\) and \(\epsilon_N<1\) the corrected test excludes an
\(F\)-zero while a bare test based on \(|G_N|\) gives no exclusion.
This implication does not require finding such a point.

For real \(x\), symmetry gives \(E_N(x)=\mathbb E\cos(xX_N)\),
so \(1-x^2\sigma_N^2/2\le E_N(x)\le1\). In particular (9) implies
\[
 |L_N(x)|(1-x^2\mathcal V_N/2)
 \le (-1)^N(F(x)-G_N(x))\le |L_N(x)|.
 \tag{11}
\]
For \(0<|x|<R_N=\sqrt{(M)_2/(B_N+\overline S_{2,N})}\) the error
has strict sign \((-1)^N\). The exact variance gives the possibly
larger open range \(0<|x|<\sqrt{2/\sigma_N^2}\).
On \(0<|x|<\min(R_N,R_{N+1})\) the consecutive even-degree
quadrature is strictly below \(F\) and the odd-degree one strictly
above it. They coincide at zero. This supplies signed brackets on
an explicit real interval.

## 6. Collision control screen and remaining premise

The phase allowance uses the node and source symmetries,
Gaussian quadrature and the two quantitative E01 bounds.
The [catalog][catalog] and [E01 §5][e01] give the following scope.

| Source or observation | Premise tested |
| --- | --- |
| Certified three- and four-square controls | Same half-line positive summand scores and tail type give \(uV'\ge\cosh(4u)-11\). The \(u\)-factor kills the junction term in the half-line integrations by parts, so both the \(\nu_N\) cosh bound and the coefficient envelope hold. They pass (8) on their own exact laws and literal readouts. They fail full canonical reflection and equal canonical square coefficients. Those failures do not enter (8). |
| Finite positive square changes and bounded positive finite-prime orbits | The same score and dominated mode bounds apply as in E01 and E07. They pass the phase estimate on their own sources with these premises. The complete arithmetic coefficients and full reflection fail. The orbit witness remains at fixed positive heat time with varying source and escaping heights. |
| Euler-factor translates | The canonical summand score changes. The \(c=1/2,p=23,\lambda=0\) member fails \(B_0\) in E01. Other prime/member bounds remain untested here. |
| Reflected super-Gaussian | The polynomially bounded \(uV'\) fails the exponential confinement used to get the cosh bound. The corresponding moment/envelope bounds themselves were untested in E01. |
| Smooth shape and positive-primitive controls | The small-damping constructions lack the canonical summand score. E01 did not test the weaker confinement or actual coefficient envelope on those families. |
| Atomic collision/threshold and finite-profile controls | They lack the positive full-line density premise of E01's proof, including the compact triangular profiles. The generic law only makes sense through degrees with positive norm and a nondegenerate Jacobi prefix. No blanket coefficient or phase failure is asserted. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic and the canonical summand score derivation fail. The weaker confinement and coefficient envelope remain untested here. Their zero conclusions retain the RH hypothesis. |
| Fixed theta amplitude with modified observation | The source bounds and law remain intact. The modified observation fails the literal Fourier/Newman readout in (9). |
| Actual-profile positive-measure relaxation | The relaxed data do not give the prescribed full-line physical source and its literal Fourier observation. |

The [E07 finite score controls][e07] have nonreal zeros by the
finite-source theorem in their stated class, with no fixed zero
location. The separate [E10][e10] and [E12][e12] smooth compact
multiplier controls retain the same pointwise confinement and tails,
so the E01 integrations give (8) for their laws too. Their Fourier
zero locations remain open. None of these distinctions gives a
canonical model modulus bound. A zero claim needs a further estimate
on the chosen contour and the zeros of \(C_N\) there, or an
independent count matching argument within the enclosed domain.
The result and screen concern the stated law, allowance and consumer.

[request]: ../research-progress/handoffs/VCD-E22-r1.md
[return]: ../research-progress/handoffs/VCD-E22-r1-return.md
[decision]: ../brainstorm/notes/12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md
[e01]: 01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e10]: 10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e12]: 12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md
[e15]: 13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
[e19]: 19_VCD_B05_CANONICAL_FOURIER_ESTIMATE_SYNTHESIS_20261116.md
[ref02]: ../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md
[topping]: https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf#page=104
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
