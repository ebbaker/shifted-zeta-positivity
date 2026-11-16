# VCD-E21 r1 — Complete quadrature error probability law

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note.** All seven input hashes in the [frozen request][request]
match. The [B06 decision][decision] yields an exact entire quadrature
remainder and explicit second and fourth moments for its error law. A
modeled lower-modulus margin for controlling zeros remains open. See the
[result index][results], [coefficient cluster][cluster], [control catalog][catalog],
[avoid index][avoid] and patterns [01][a01], [02][a02], [07][a07] and [12][a12].

## 1. Physical source and Gaussian rule

At \(\lambda=0\), let \(d\mu(u)=\Phi(u)\,du/Z\), \(Z=\int\Phi\), using the
unchanged complete even theta source. Then \(F(z)=\int e^{izu}\,d\mu=2H_0(z)/Z\).
The source bound in [manuscript §2][ms] gives all absolute exponential
moments, also with any fixed polynomial factor. Write \(P_j\) for its
monic orthogonal polynomials and \(h_j^*=\int P_j^2\,d\mu\). Reflection and
uniqueness give \(P_j(-u)=(-1)^jP_j(u)\). Set \(\beta_0=0\) and
\(\beta_j=h_j^*/h_{j-1}^*>0\) for \(j\ge1\), so \(h_0^*=1\) and
\(h_N^*=\prod_{j=1}^N\beta_j\). In the orthonormal basis \(p_j=P_j/\sqrt{h_j^*}\),
multiplication by \(u\) acts by the zero-diagonal Jacobi matrix \(J\) with
links \(a_j=\sqrt{\beta_j}\) between \(j-1\) and \(j\). The prefix
\(J_N\) retains \(0,\ldots,N-1\), where \(N\ge1\).

The leading block characteristic polynomials satisfy the monic
recurrence \(P_{j+1}(u)=uP_j(u)-\beta_jP_{j-1}(u)\) by determinant
expansion, with the \(P_{-1}\) term omitted at \(j=0\). Thus its real
eigenvalues \(x_1,\ldots,x_N\) are the roots of \(P_N\). The row
recurrence forces a zero vector if an eigenvector has first entry zero,
so each eigenspace has dimension one and the spectral weights \(w_j\)
at \(e_0\) are positive. The statement for \(N=1\) follows from \(J_1=0\).
The weights sum to one, and alternating site signs conjugate \(J_N\) to
\(-J_N\) while fixing \(e_0\). In particular the node multiset and the
weighted rule are even. Define
\[
 Q_N f=\sum_{j=1}^N w_j f(x_j),\qquad
 G_N(z)=Q_N(e^{iz\cdot})=e_0^{\mathsf T}e^{izJ_N}e_0.
\]
The full moment \(\int u^k\,d\mu=(J^k)_{00}\) is a sum of walks from
site \(0\) back to site \(0\), by applying multiplication to \(p_0=1\).
The finite moment \(Q_N(u^k)=(J_N^k)_{00}\) keeps the walks in the
prefix. Reaching site \(N\) and returning takes at least \(2N\) steps,
so \(Q_N\) is exact through degree \(2N-1\), also for polynomials with
complex coefficients. At degree \(2N\), the one omitted walk goes
monotonically to \(N\) and back, with weight \(h_N^*\).
[E04 §§1, 5][e04]

## 2. Simplex moments from beta integrals

Put \(d=2N\), \(M=d+1\). Let \(S=(S_0,\ldots,S_d)\) be uniform on
\(s_i\ge0,\ \sum_{i=0}^d s_i=1\), with Lebesgue coordinates
\(s_1,\ldots,s_d\) and \(s_0=1-\sum_{i=1}^d s_i\). For any nonnegative
integers \(k_0,\ldots,k_d\), let \(k=\sum_i k_i\). The unnormalized
simplex integral of \(\prod_i s_i^{k_i}\) equals
\[
 \frac{\prod_{i=0}^d k_i!}{(d+k)!}.
\]
In dimension zero the integral is \(1\). For the induction step fix
\(s_d=r\) and rescale the remaining coordinates by \(1-r\). The change
of variables multiplies the \((d-1)\)-dimensional integral by
\((1-r)^{d-1+\sum_{i<d}k_i}\), leaving the beta integral with the
other factor \(r^{k_d}\). For nonnegative integers \(a,b\), integration
by parts reduces \(\int_0^1 r^a(1-r)^b\,dr\) to
\(a!b!/(a+b+1)!\), starting from \(a=0\). Substitution gives the
claimed induction. At \(k=0\) the volume is \(1/d!\), so the
probability density in the stated coordinates is \(d!\).

For a fixed ordered knot list \(t=(t_0,\ldots,t_d)\), let
\(c_k(t)=\sum_{\sum k_i=k}\prod_i t_i^{k_i}\), the complete
homogeneous polynomial of degree \(k\) in the knots. Expanding by
the multinomial theorem cancels the \(k_i!\) and gives
\[
 \mathbb E_S\Big(\sum_i S_i t_i\Big)^k
       =\frac{k!\,d!}{(d+k)!}c_k(t),
 \qquad
 \sum_{k\ge0}c_k(t)v^k=\prod_{i=0}^d(1-vt_i)^{-1}.
 \tag{1}
\]
The product identity is for fixed knots and can be used as a formal
power series. Both formulas retain every occurrence of a repeated knot.

## 3. Confluent remainder and integration for complex height

For \(z\in\mathbb C\) put \(f_z(v)=e^{izv}\). Let \(I_z\) be its
polynomial interpolant of degree at most \(d-1\) matching \(f_z\) and
its first derivative in \(v\) at the \(N\) nodes. The homogeneous
interpolation conditions force divisibility by \(P_N^2\), of degree
\(d\), so the linear interpolation map is injective between spaces of
dimension \(d\) and hence bijective. For any fixed real \(u\) augment
the list of doubled nodes by \(u\), making \(t=(u,x_1,x_1,\ldots,x_N,x_N)\).
Let \(I_{z,t}\) interpolate \(f_z\) in degree at most \(d\) on this
list, matching derivatives of orders \(0,\ldots,b-1\) at any knot of
multiplicity \(b\). This also exists uniquely by divisibility by the
degree-\(d+1\) knot polynomial \(\Pi_t(v)=\prod_i(v-t_i)\) in the
homogeneous case. If \(u=x_j\) the augmented conditions include the
second derivative at that node. The difference \(I_{z,t}-I_z\) is
\(P_N^2\) times the coefficient of \(v^d\) in \(I_{z,t}\), since it
satisfies the homogeneous doubled-node conditions. Denote this
coefficient functional by \(D_t f_z\). Evaluating at \(u\) gives
\[
 f_z(u)-I_z(u)=P_N(u)^2 D_t f_z . \tag{2}
\]

To compute \(D_t\) elementarily, the interpolant of a monomial \(v^l\)
is its polynomial remainder modulo \(\Pi_t\), by the same matching
conditions with multiplicity. Its coefficient of \(v^d\) is the
coefficient of \(v^{-1}\) in the Laurent expansion of \(v^l/\Pi_t(v)\)
at infinity, since the quotient polynomial contributes no negative
powers and lower remainder terms start at \(v^{-2}\). By (1) this
coefficient is zero for \(l<d\) and is \(c_{l-d}(t)\) for \(l\ge d\).
For fixed \(t\), \(D_t\) is a linear combination of finitely many
values and derivatives at the knots. The exponential Taylor series
and these derivatives converge absolutely at every knot. Thus (1)
identifies the series for \(D_t f_z\) with
\[
 \sum_{k\ge0}\frac{(iz)^{d+k}}{(d+k)!}c_k(t)
    =\frac{(iz)^d}{d!}\mathbb E_S\exp\Big(iz\sum_i S_i t_i\Big).
 \tag{3}
\]
The exponential series can be averaged over \(S\) since the fixed
knot hull is bounded. This proves the confluent formula including
coincident knots and complex \(z\), without using a real-valued
mean-value remainder. It is the exponential case of the classical
formulas in de Boor, §1 (16), p. 50, and §9 (52), p. 64, whose simplex
integral is unnormalized. Section 7, Definition 37, p. 59, identifies
the divided difference as the leading coefficient of the Hermite
interpolant, with derivative data as in (36), p. 58.
[Passage record][ref] and [de Boor PDF][deboor]

By exactness for \(I_z\) and interpolation at the nodes,
\(F-G_N=\int(f_z-I_z)\,d\mu\). Take \(U\) independent of \(S\) with
law \(d\nu_N(u)=P_N(u)^2\,d\mu(u)/h_N^*\). Label the last \(d\) simplex
coordinates by \((j,1),(j,2)\), one pair per node. The resulting law is
\[
 X_N=S_0 U+\sum_{j=1}^N(S_{j,1}+S_{j,2})x_j,
 \qquad E_N(z)=\mathbb E e^{izX_N}.
\]
The grouped coordinates \((S_0,S_{1,1}+S_{1,2},\ldots,S_{N,1}+S_{N,2})\)
have Dirichlet parameters \((1,2,\ldots,2)\). Indeed, for each pair
write \((s_{j,1},s_{j,2})=(q_j r_j,q_j(1-r_j))\). The absolute
Jacobian for the pair is \(q_j\); integrating each \(r_j\) over
\([0,1]\) yields density \(d!\prod_j q_j\) on \(q_j\ge0,\sum_jq_j\le1\),
with \(q_0=1-\sum_jq_j\). This is the stated Dirichlet density in the
coordinates \(q_1,\ldots,q_N\).

If \(L=\max_j|x_j|\), then \(|X_N|\le |U|+L\). For each \(R>0\),
\(e^{R(|U|+L)}\) has finite mean by the source tail bound and the
fixed polynomial density factor for \(\nu_N\). This majorant justifies
the interchange of the simplex and source integrals in (2)–(3), and
also bounds the absolute sum of the exponential series on \(|z|\le R\).
Thus \(E_N\) is entire, as are \(F\) by the same source bound and
\(G_N\) by its finite sum. Equations (2)–(3) give on all of \(\mathbb C\)
\[
 \boxed{F(z)-G_N(z)=(-1)^N h_N^*\frac{z^{2N}}{(2N)!}E_N(z).} \tag{4}
\]
Here \(E_N(0)=1\), including at the removable point of the ratio of
the error to its first Taylor term. The physical field in (4) remains
the Fourier transform of \(\mu\). The law of \(X_N\) represents the
factor of the remainder.

## 4. Symmetry, second and fourth moments

The law \(\nu_N\) is even by polynomial parity. Simultaneously sending
\(U\) to \(-U\) and permuting the simplex coordinates according to
the reflection of the nodes preserves the joint law and sends
\(X_N\) to \(-X_N\). Here the simplex measure is invariant under
coordinate permutations, as they preserve its affine volume, which
is a constant multiple of the coordinate volume. Thus \(E_N\) is
even and \(\mathbb E X_N=0\), with all moments finite.

Let \(m_2=\mathbb E U^2\), \(m_4=\mathbb E U^4\) and
\(S_p=\operatorname{tr}(J_N^p)=\sum_j x_j^p\) for \(p\ge1\).
Write \(A(v)=\prod_j(1-v x_j)^{-2}\).
The formal logarithm has coefficient \(2S_p/p\) at degree \(p\).
All odd \(S_p\) vanish, so
\[
 A(v)=1+S_2 v^2+\frac{S_2^2+S_4}{2}v^4+O(v^6).
\]
Conditionally on \(U=u\), the generating series for \(c_k(t)\) is
\(A(v)(1-vu)^{-1}\). In degree two its coefficient is \(u^2+S_2\),
and in degree four it is \(u^4+u^2 S_2+(S_2^2+S_4)/2\). Averaging
these finite polynomials and using (1) gives
\[
 \boxed{\begin{aligned}
 \mathbb E X_N^2&=\frac{2(m_2+S_2)}{M(M+1)},\\
 \mathbb E X_N^4&=\frac{24m_4+24m_2 S_2+12 S_2^2+12 S_4}
                         {M(M+1)(M+2)(M+3)}.
 \end{aligned}} \tag{5}
\]
The coefficient extraction is conditional and finite; the reciprocal
series with unbounded \(U\) serves only to name coefficient polynomials.

Since \(d\nu_N=p_N^2\,d\mu\), the two raw moments are the squared norms
of \(J e_N\) and \(J^2 e_N\), respectively. The former has neighboring
coefficients \(a_N,a_{N+1}\). The latter has coefficients
\(a_N a_{N-1},\ \beta_N+\beta_{N+1},\ a_{N+1}a_{N+2}\), at sites
\(N-2,N,N+2\), with the first omitted at \(N=1\). Therefore
\[
 m_2=\beta_N+\beta_{N+1},\qquad
 m_4=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2+
           \beta_{N+1}\beta_{N+2}. \tag{6}
\]
For the complete source, [E01][e01] gives \(m_2\le B_N\) and
\(m_4\le3B_{N+1}^2\), with \(B_j=\operatorname{arcosh}^2(2j+12)/16\).
Also \(S_2=2\sum_{j=1}^{N-1}\beta_j\) and \(S_4\le\|J_N\|^2 S_2\),
where \(\|J_N\|\le2\max_{1\le j<N}a_j\) for \(N\ge2\). The envelope
and (5) give \(\mathbb E X_N^2=O(\log^2(N+1)/N)\) and
\(\mathbb E X_N^4=O(\log^4(N+1)/N^2)\). The quantitative complex
phase comparison is the separate E22 task.

For \(N=1\), \(G_1=1\), \(P_1(u)=u\), \(h_1^*=\beta_1\) and
\(x_1=0\), so \(X_1=S_0U\). The marginal density of \(S_0\) is
\(2(1-s)\) on \([0,1]\), giving \(\mathbb E X_1^2=m_2/6\) and
\(\mathbb E X_1^4=m_4/15\), as in (5). Moreover
\(\cos(zu)-1=-(zu)^2\int_0^1(1-s)\cos(zsu)\,ds\) by integrating its
second derivative in \(s\) twice. Integrating against the even \(\mu\)
gives \(F-1=-\beta_1 z^2 E_1(z)/2\), directly checking the sign and
factor at the endpoint, where \(E_1\) here is the degree-one error factor.

## 5. Physical E15 comparison and controls

For the same prefix put \(e=e_{N-1}\) and use the physical normalized
tail kernel \(k_N(z)=\langle e_N,e^{izJ^{[N]}}e_N\rangle\), entire
on its fixed-vector domain with \(k_N(0)=1\) by [E04 §4][e04]. In
[E15 §§3–4, 6][e15], \(f_{k_N}=F\) and \(f_0=G_N\). Thus, with the
ordered entire convolutions of E15, the right side of (4) equals
\[
 -\beta_N\,(e_0^{\mathsf T}T_{k_N}e)*k_N*
                         (e^{\mathsf T}e^{izJ_N}e_0).
\]
This follows by the common left side \(F-G_N\). E15 has \(q=0\) in its
first discrepancy formula, yielding the same omitted walk and sign.
The probability law represents the combined physical error in that
comparison. The arbitrary-kernel transport identity stays in E15.

The proof of (4)–(6) uses an even probability source of infinite
support with all absolute exponential moments and its own literal
Fourier readout. The moment orders use E01's coefficient envelope,
derived from its weighted cosh bound. The following screen uses
[E01 §5][e01], [E04's control scope][e04] and the [catalog][catalog].

| Control | Checked premise |
| --- | --- |
| Three- and four-square positive weights | Both share the exact-law premises and E01's weighted cosh input and envelope. The positive constants cancel in each summand score and the factor \(u\) cancels the even-extension junction term. They lack full canonical reflection and the complete equal square coefficients, which the error formula does not use. |
| Finite square-mode changes and finite-prime orbit controls | The perturbations change the complete coefficients and fail full canonical reflection. At admissible even full-line sources with all exponential moments, the exact law applies. The inherited B01 screen allows the score bound for appropriate bounded nonnegative weights, without an all-family coefficient claim. |
| Euler-factor translates | Exponential moments, evenness and the literal readout of the translated source suffice for (4). The canonical summand score changes. E01's envelope failure is at \(c=1/2,p=23,\lambda=0\) and index zero. Other translates and indices are outside that check. |
| Reflected super-Gaussian | The exact law applies by evenness and all exponential moments. Its polynomial-growth score fails the exponential confinement premise of the E01 derivation. Its actual envelope is untested. |
| Smooth shape and positive-primitive sources | Double-exponential tails allow the exact-law premises. These controls lack the canonical square summand score. The weaker E01 score inequality and envelope remain untested, with the catalog's small-damping qualification. |
| Three-atom and finite-profile threshold families | Atoms terminate the recurrence, so the all-degree premises fail. The interpolation proof of (4) applies below support size, where \(h_N^*>0\). The inherited three-atom event fails the E01 envelope at index one. Even triangular compact extensions allow (4), while global positive density for the E01 score fails. No general coefficient verdict follows. |
| RH-conditional normalized endpoint controls | Their positive even sources with uniform relative proximity to theta meet the exact-law premises. Ordinary Dirichlet arithmetic and the unchanged theta summand formula fail, with the RH qualification intact. The E01 envelope remains untested. |
| Fixed amplitude with varied observation | The source recurrence and the law for its literal Fourier readout stay the same. The altered observable lacks that readout premise. |
| Actual-profile positive-measure relaxation | Its admissible-height measure supplies no physical full-line source and Fourier readout to use in (4). |

The weighted-square witnesses already pass the generic proof and the
inherited envelope at their recorded events, so these premises acquire
no new theta discriminator. The finite-source nonreal-zero scope in
[E07][e07] remains separate from the smooth freedoms in [E10][e10] and
[E12][e12]. The [B05 synthesis][b05] retains its actual-source exclusions.

[request]: ../research-progress/handoffs/VCD-E21-r1.md
[decision]: ../brainstorm/notes/12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md
[ms]: ../manuscript/main.tex
[ref]: ../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md
[deboor]: https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf
[e01]: 01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e10]: 10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e12]: 12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md
[e15]: 13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
[b05]: 19_VCD_B05_CANONICAL_FOURIER_ESTIMATE_SYNTHESIS_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
