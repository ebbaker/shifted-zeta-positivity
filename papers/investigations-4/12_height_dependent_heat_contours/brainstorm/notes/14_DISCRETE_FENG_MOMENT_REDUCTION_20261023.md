# Discrete Feng moments: first moment and a scoped orthogonality result

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model agents checked the source imports, admissible coefficient families, Euler factors, analytic localization, residue calculation and optimization scope. This is internal mathematical research and review, not specialist or formal verification.

**Status: proved in-note within the stated smoothing and fixed-parameter scope.** The proposed two-prime Feng direction has an explicit first moment. For profiles divisible by u^100, its full mixed second moment with the optimized ordinary mollifier has zero residual correlation. Consequently these directions supply no gain in the limiting residual functional, or in the leading Cauchy quotient for fixed combinations with positive limiting second moment. The calculation does not improve 19/27, prove a universal mollifier ceiling, or exclude a multiple zeta zero.

For the less smoothed example P(u)=u, the first moment is proved and the same cancellation holds for the formal leading kernel. The analytic mixed-moment passage for that particular low-order profile is not proved here. The exponent 100 is a convenient sufficient smoothing order, not an optimal threshold.

This resolves the first arithmetic test proposed in [Review 04, Section 5](../reviews/04_ANALYTIC_SIMPLICITY_OPENING_ROUND_REVIEW_20261023.md#5-strategic-reassessment-a-direct-arithmetic-comparison) for a substantial specified class. It serves SIMP-01 by testing a candidate arithmetic improvement; SIMP-01 itself remains open. Follow the [result index](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [checked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. Quantities and conclusions

Fix 0<theta<1/2, put y=T^theta, ell=log y, L=log T, and let N(T) count zeta zeros with 0<gamma<=T with multiplicity. Replacing L by log(T/(2 pi)) does not change any limit below. Under RH set

\[
 u_n=\frac{\log(y/n)}{\ell},\quad
 D_P(s)=\sum_{n\le y}\mu(n)P(u_n)n^{-s},
\]
\[
 e_2(n)=\sum_{\substack{p<q\\pq\mid n}}\log p\log q,
 \qquad F_Q(s)=\sum_{n\le y}\mu(n)\frac{e_2(n)}{\ell^2}Q(u_n)n^{-s}.
\]

Profiles in this note are fixed real polynomials with P(0)=Q(0)=0. Write w_X(rho)=X(rho)zeta'(rho)/L and E_T for averaging over those zero labels. The ordinary optimum is

\[
 P_0(u)=(1+\theta)u-\theta u^2,\quad w_0=w_{D_{P_0}},
\]
\[
 a_0=\lim E_Tw_0=\frac{\theta^2+3\theta+3}{6},\qquad
 b_{00}=\lim E_T|w_0|^2
 =\frac{(1+\theta)^3(\theta^2+3\theta+3)}{36\theta},
\]
\[
 c_\theta=\frac{a_0}{b_{00}}=\frac{6\theta}{(1+\theta)^3},\qquad
 F_\theta=\frac{a_0^2}{b_{00}}=1-(1+\theta)^{-3}.
\]

These are the classical Bui–Heath-Brown baseline, not new results. Their fixed-theta limits give 19/27 on subsequently letting theta increase to 1/2.

**First-moment proposition.** For every such Q, the first moment is

\[
 a_Q:=\lim E_Tw_{F_Q}
 =\frac{\theta^2}{12}\int_0^1(1-u)^3Q(u)\,du. \tag{1}
\]

In particular Q(u)=u gives a_Q=theta^2/240. The unnormalized first-moment calculation is unconditional.

**Mixed-moment proposition.** If Q(u)=u^100 R(u) for a fixed polynomial R, then

\[
 b_{0Q}:=\lim E_T[w_0\overline{w_{F_Q}}]
 =\frac{\theta(1+\theta)^3}{72}
       \int_0^1(1-u)^3Q(u)\,du, \tag{2}
\]

and the normalized square moment of w_FQ has a finite limit. All fixed finite families of these directions have a finite Hermitian Gram limit. Thus

\[
 \lim E_T[(1-c_\theta w_0)\overline{w_{F_Q}}]
 =a_Q-c_\theta b_{0Q}=0. \tag{3}
\]

The full complex cross moment is meant in (2), not only its real part. Complex coefficient polarization is retained in the import.

## 2. Source audit and an admissible perturbation family

[Benli–Elma–Ng, arXiv:2311.13554v1](https://arxiv.org/html/2311.13554v1), Theorem 1.1, equations (9)–(11), supplies the corrected shifted first moment. Its remark after (11) identifies errors in the older Ng formula and its large-sieve argument. [Ng, arXiv:0706.1763v1](https://arxiv.org/abs/0706.1763v1), is retained as correction provenance, not imported unchanged.

[Heap–Li–Zhao, arXiv:2003.09368v1](https://arxiv.org/html/2003.09368v1), Theorem 2, equations (5)–(9), supplies the shifted second moment. The explicit remark states this theorem is unconditional. The paper's separate negative-moment theorem assumes simplicity; it is not used. The contour residue in the second-moment theorem counts repeated zero labels. Its shift-uniform error has arbitrary logarithmic saving; two shift derivatives cost only L^2 by Cauchy's formula. RH supplies the Hermitian interpretation.

Both imports require submultiplicative, divisor-bounded coefficients. The isolated Feng coefficient fails the first condition: it is zero at primes but generally nonzero at pq. One must not apply either theorem to it directly.

There is an exact repair. Since

\[
 0\le e_2(n)/\ell^2\le\tfrac12(\log n/\ell)^2\le\tfrac12,
\]

write Q=uR and use the coefficients of D_P0+eta F_Q, with fixed sufficiently small complex eta. Their absolute values are bounded above and below by positive constants times mu(n)^2 u_n. For mn<=y,

\[
 u_{mn}=u_m+u_n-1\le u_m u_n.
\]

This proves submultiplicativity uniformly in T; when mn is outside the support or nonsquarefree the left side is zero. Exact finite differences in eta recover the finite-T shifted first-moment formula, and finite polarization at eta,-eta,i eta,-i eta recovers the finite-T cross and square formulas. Establishing their normalized limits still requires the analysis below. No shrinking-eta limit or new theorem for arbitrary coefficients is needed.

For several strongly smoothed profiles use the envelope mu(n)u_n^100 and brackets 1+epsilon R(u_n)+delta e_2(n)S(u_n)/ell^2 of modulus between 1/2 and 3/2. This proves the same admissibility and finite polarization for the class used in the analytic extraction.

The Feng coefficient itself has prior art in [Pratt–Robles–Zaharescu–Zeindler, Section 3.2](https://doi.org/10.1007/s40687-019-0199-8). Squarefree support is retained exactly; it is not replaced by an unrestricted Dirichlet convolution. There is no novelty claim for the coefficient family or the general projection method.

## 3. Proof of the first moment

Apply the Benli–Elma–Ng shifted formula with Y=1, using the preceding finite difference to isolate F_Q. Its b(1) and prime-power terms vanish. The remaining factor for k is

\[
 -\frac{k}{\varphi(k)}\Phi(\alpha,k)\zeta(1-\alpha)
 \frac{(T/(2\pi k))^{-\alpha}}{1-\alpha},\qquad
 \Phi(\alpha,k)=\prod_{p\mid k}(1-p^{-\alpha}).
\]

For k=pq, p<q,
Phi(alpha,pq)=alpha^2 log p log q+O(alpha^3), while zeta(1-alpha)=-1/alpha+O(1). Its first derivative is therefore +(pq/phi(pq))log p log q. For squarefree k with at least three prime factors it is zero. For every fixed A>0, after absorbing the shift derivative into the arbitrary saving, this gives

\[
 \sum_{0<\gamma\le T}F_Q(\rho)\zeta'(\rho)
 =\frac{T}{2\pi\ell^2}
 \sum_{\substack{p<q\\pq\le y}}
 \frac{(\log p\log q)^2}{(p-1)(q-1)}Q(u_{pq})
 +O_A(TL^{-A}). \tag{4}
\]

The prime number theorem and partial summation give weak convergence on [0,1]

\[
 \ell^{-2}\sum_{p\le y}\frac{(\log p)^2}{p-1}
        \delta_{\log p/\ell}\ \longrightarrow\ v\,dv.
\]

The diagonal p=q has total weight O(ell^-4), since the corresponding prime sum with denominator (p-1)^2 converges. The unordered double sum in (4), divided by ell^4, therefore tends to

\[
 \frac12\int_{v,w\ge0,\ v+w\le1}vwQ(1-v-w)\,dv\,dw
 =\frac1{12}\int_0^1(1-u)^3Q(u)\,du.
\]

The boundary has zero limiting measure. Normalizing (4) by N(T)L proves (1).

## 4. The complete marked second-moment kernel

The variables a,b,c,s,t below are scaled by 1/L in the actual shifts and Mellin arguments. Define

\[
 \mathcal M_P(s)=\sum_{j\ge1}\frac{p_jj!}{\theta^j s^{j+1}},
 \qquad P(u)=\sum p_j u^j.
\]

The local squarefree choices for a prime are: absent, in the common divisor g, in h alone, or in k alone. From the exact local factors in HLZ one obtains the rational kernels

\[
 F(a,b,c;s,t)=\frac{b(s+b)(t+a)(t+c)}{(a+b)(b+c)(s+t)t},
 \qquad G(a,b;s,t)=\frac{(s+b)(t+a)}{(a+b)(s+t)}. \tag{5}
\]

The ordinary arithmetic Euler factor at the origin is exactly one. Marking each prime on the second coefficient by 1+z log p/ell produces the unordered pair as the z^2 coefficient. Its leading insertion is H_v^2/(2theta^2), where

\[
 H_v=\frac1{s+t}-\frac1{t+a}-\frac1{t+c}+\frac1t,
 \qquad H_u=\frac1{s+t}-\frac1{s+b}. \tag{6}
\]

For G use H_v^J=1/(s+t)-1/(t+a), and the same H_u. Repeated-prime terms from a single marker's logarithm are lower order. A prime marked once on each side is different: it contributes C=1/(s+t)^2, so the square-moment insertion is

\[
 \theta^{-4}\left(\frac{H_u^2H_v^2}{4}+H_uH_vC+\frac{C^2}{2}\right). \tag{7}
\]

This gives a finite square limit in the smoothed class; it is not permissible to drop the last two terms.

For the mixed moment retain all three F branches
F(a,b,c)+e^(-a-b)F(-b,-a,c)+e^(-b-c)F(a,-c,-b), differentiate in c, add the conjugate orientation with s,t and a,b swapped, and retain both G branches G(a,b)+e^(-a-b)G(-b,-a). In the swapped orientation the marker is H_u, not H_v. Finally differentiate in a,b. The apparent shift poles cancel before taking derivatives: at a+b=0 the first two F branches have opposite residues; at b+c=0 the first and third do. At a=c the second and third have equal exponentials and opposite residues, using symmetry of F and the right marker in the first and third shift arguments (the left marker does not depend on them). The two J branches similarly cancel at a+b=0. These are all the shift-only polar hyperplanes, so the sums are holomorphic near zero.

After removing the common factor theta^-2, the resulting cross kernel has the compact partial fractions

\[
\begin{aligned}
 K(s,t)={}&-\frac{t^2}{24(s+t)^3}
 +\frac{3t^3-4t^2+12}{24t^2(s+t)^2}
 -\frac{3t^3-8t^2-6t+36}{24t^3(s+t)}\\
 &+\frac{t^4-4t^3-6t^2+24t+12}{24t^5}
 +\frac1{2st^4}. \tag{8}
\end{aligned}
\]

Thus the high-smoothing cross moment is the double inverse transform of
exp(theta(s+t)) M_P(s) M_Q(t) K(s,t)/theta^2. Appendix A proves that these kernels are the actual moment limits in the specified class, including the arithmetic and Mellin errors.

The exact symbolic verification also recovers the unmarked baseline kernel and its b_00 above. It is supporting algebra, not a numerical estimate of zeta zeros or a substitute for Appendix A. See [the reproducible check](../numerics/14_discrete_feng_kernel_check.py) and [its result](../numerics/14_discrete_feng_kernel_check_20261023.json).

## 5. Extending the ordinary baseline and evaluating the cross

Keep Q divisible by u^100. The smoothed square limit bounds its norm. Approximate P_0 in H^1[0,1] by polynomials divisible by u^100: smoothly cut off P_0 near zero, then divide the cut-off function by u^100 and approximate that quotient by polynomials in C^1. The ordinary moment quadratic form from [Bui–Heath-Brown](https://arxiv.org/abs/1302.5018v1), consistent with the historical [Conrey–Ghosh–Gonek optimization, p. 500](https://aimath.org/~kaur/publications/34.pdf), is

\[
 b(P,P)=\tfrac13|P(1)|^2+
 \theta\Re\left(P(1)\overline{\int P}\right)
 +\theta^2|\int P|^2+\frac1{12\theta}\int|P'|^2, \tag{9}
\]

which is continuous in H^1 for P(0)=0. Its sesquilinear extension here is obtained from the full complex shifted import and complex polarization, not inferred from real diagonal values alone. RH and Cauchy–Schwarz show that the actual cross moment converges to the same H^1 extension.

Formula (8) verifies continuity of the rational expression as well. Its s-inversion uses only P(1), an integral of P, and convolutions of P with (theta-v)^(j-1)e^(-t(theta-v)), j=1,2,3. The subsequent t-inversion acts on a fixed highly smoothed Q and involves at most two derivatives of Q and fixed antiderivatives. The resulting kernels are continuous on the compact interval. The functional is therefore bounded by C_Q(|P(1)|+||P||_2), and extends continuously to H^1. This justifies using the low-degree optimized ordinary P_0, without extending the marked profile Q to low smoothing.

For M_0(s)=(1+theta)/(theta s^2)-2/(theta s^3), direct s residues at 0 and -t give

\[
 \frac1{2\pi i}\int e^{\theta s}\mathcal M_0(s)K(s,t)\,ds
 =\frac{(1+\theta)^3}{12\theta t^4}+e^{-\theta t}R_\theta(t), \tag{10}
\]
\[
 R_\theta(t)=-\frac{\theta(1+\theta)}{48}+\frac1{24t}
 -\frac{1+\theta}{6t^2}-\frac1{3t^3}
 +\frac{6\theta^2+9\theta-1}{12\theta t^4}+\frac1{2t^5}.
\]

After the outer exponential cancels, M_Q(t)R_theta(t) has all poles at zero and decays at least as t^-2. Its vertical integral closes to the right and is zero. The remaining transform is

\[
 \frac1{2\pi i}\int e^{\theta t}\frac{\mathcal M_Q(t)}{t^4}\,dt
 =\frac{\theta^4}{6}\int_0^1(1-u)^3Q(u)\,du.
\]

This proves (2), hence (3). It also proves the same algebraic identity for every polynomial Q(0)=0 at the level of formal rational transforms. That last observation does not remove the smoothing condition from the arithmetic theorem.

## 6. What the cancellation rules out

Let r_0=1-c_theta w_0. The normal equations for ordinary profiles follow directly from (9): for every ordinary polynomial P(0)=0,

\[
 \lim E_T[w_0\overline{w_{D_P}}]
 =\frac{(1+\theta)^3}{6\theta}\overline{\lim E_Tw_{D_P}}.
\]

Equation (3) adds every smoothed Feng direction to this orthogonal family. For any fixed finite span of these directions, its limiting Gram form is positive semidefinite. Therefore, for every fixed h in that span,

\[
 \lim E_T|r_0-h|^2=1-F_\theta+\lim E_T|h|^2\ge1-F_\theta. \tag{11}
\]

Equivalently, each fixed combination with positive limiting second moment has leading Cauchy quotient at most F_theta. This includes simultaneous reoptimization of finitely many ordinary profiles and smoothed Feng directions; it is stronger than observing a zero derivative for one numerical coefficient.

**Nullspace qualification.** If both limiting moments of a combination vanish, the leading quotient is 0/0. Neither (11) nor Gram positivity rules out a lower-order gain after a height-dependent rescaling. Positive definiteness modulo exact zero directions, or a separate lower-order analysis, would be needed. No uniform optimization over growing dimension, varying profiles, or theta depending on T is asserted.

The abstract projection criterion is established methodology. [Čech–Matomäki, arXiv:2501.12526v3](https://arxiv.org/html/2501.12526v3), Theorem 2.4 and Corollary 2.6, give general optimality criteria; Remark 2.11 addresses the danger of near-singular cancellation. Their specific arithmetic applications concern different families. They do not supply equation (2) or a universal 19/27 ceiling here.

## 7. Controls, outcome and next question

This is a scoped arithmetic moment calculation and obstruction, not an RH-equivalent reformulation. At every multiple zero both derivative-weighted directions vanish, so its repeated labels contribute exactly one to |r_0|^2. All the repository's collision controls remain compatible with that algebra. The exact zeta/Dirichlet-series moment identities are the source-specific premise; those identities have not been proved for the Euler-factor, weighted-square, reflected, finite-prime-compatible or perturbed-source controls. None is falsely excluded from geometric assumptions. Sparse doubles remain compatible with an average proportion bound.

The proposed prime-pair enrichment does not produce a leading gain in the proved class. Further coefficient searches within that class are not justified by this calculation. The next useful arithmetic question is whether the same normal equation extends to a substantially larger one-piece coefficient class, or whether a particular different direction breaks it. A new direction should first pass this first/cross-moment test with its complete errors. Longer mollifiers, other coefficient structures, lower-order nullspace analysis and different local observables are outside the present exclusion.

No new simplicity proportion, density-one statement, individual-zero exclusion, manuscript revision, commit or publication follows from this note. References and external PDF receipts are in the [investigation catalog](../../references/README.md). The [internal review](../reviews/05_DISCRETE_FENG_MOMENT_REVIEW_20261023.md) records what was checked.

## Appendix A. Analytic extraction for high-smoothing profiles

This appendix supplies the convergence argument for Section 4; Section 5 separately extends the ordinary comparison profile. The large smoothing order is used only to give a simple integrable global envelope.

### A.1. Statement

Fix 0<theta<1/2, y=T^theta, L=log T, ell=log y=theta L, and B=100. Put u_n=log(y/n)/ell for n<=y and

D_P(s)=sum_{n<=y} mu(n) P(u_n)n^(-s),

F_Q(s)=sum_{n<=y} mu(n) [e_2(n)/ell^2] Q(u_n)n^(-s),

e_2(n)=sum_{p<q|n} log p log q.

Let P and Q be fixed real polynomials divisible by u^B. Assume RH when identifying the differentiated discrete moment with a Hermitian inner product. Then all ordinary/ordinary, ordinary/Feng, and Feng/Feng normalized moments

(1/N(T)) sum_{0<gamma<=T} [zeta'(rho) X(rho)/L] conjugate([zeta'(rho) Y(rho)/L])

have finite limits given by the complete differentiated rational kernels in Section 4, with the appropriate zero-, one-, or two-sided marker coefficient. The asymptotic error in the arithmetic extraction is O(1/L); the imported HLZ error is smaller after choosing its arbitrary logarithmic saving sufficiently large. In particular, every fixed such Feng direction has bounded normalized square moment.

The essential import is Heap--Li--Zhao, arXiv:2003.09368v1, Theorem 2, equations (5)--(9), explicitly unconditional. RH is used only for the Hermitian interpretation and Cauchy--Schwarz extension. All three Z branches and both orientations of I are retained, as is J.

### A.2. Admissibility by a fixed affine envelope

The isolated Feng coefficient is not submultiplicative. Instead use the reference mu(n)u_n^B and fixed perturbations

mu(n)u_n^B [1+epsilon R(u_n)+delta e_2(n)S(u_n)/ell^2],

where P=u^B R and Q=u^B S. Since e_2(n)/ell^2<=1/2, choose the finitely many complex epsilon,delta small enough that the modulus of the bracket lies between 1/2 and 3/2. These coefficients have absolute values comparable to mu(n)^2 u_n^B. For mn<=y,

u_{mn}=u_m+u_n-1<=u_m u_n,

so the required submultiplicative inequality follows, with a constant independent of T. If a factor is not squarefree, the product coefficient is zero. If mn>y the truncated coefficient is zero. Divisor boundedness is immediate. Exact finite differences and complex polarization, including the fixed imaginary perturbations ±i epsilon and ±i delta, of the finite-T quadratic moment formula extract every desired cross and square term. The same argument handles any fixed finite family of profiles. No theorem is applied to the isolated inadmissible direction.

### A.3. Shift and Mellin contours

Use actual shifts alpha=a/L, beta=b/L, gamma=c/L. Take separated scaled Cauchy circles |a|=4d, |b|=2d, |c|=d, where d>0 is sufficiently small for the uniform-shift range in HLZ and 4d<1/10. The shift derivative in c is taken first; a,b derivatives follow. Every polar linear form occurring in an individual branch has modulus at least d on the relevant nested circles: a+b, b+c, a-c and their negatives. The apparent poles cancel in the complete branch sum, which is holomorphic at the origin. Thus the nested Cauchy integral evaluates its derivatives without assigning a value to an isolated singular branch.

Take scaled Mellin contours Re s=Re t=1, corresponding to actual Mellin variables s/L,t/L. Every Mellin-dependent zeta or prime-sum argument in all three branches has real part at least 1+c_0/L for a fixed c_0>0. In particular s+t, s+b, t+a, t+c, and t have positive real parts bounded away from zero in scaled variables, including after the branch substitutions.

For a profile P=sum_{j>=B}p_j u^j, Mellin inversion gives the weight

M_P(s)=sum_{j>=B}p_j j!/(theta^j s^(j+1)).

On the contour it is bounded by C_P(1+|Im s|)^(-B-1). Mellin inversion and the initial sum/integral interchanges are absolutely convergent because all Dirichlet exponents lie strictly to the right of 1 and B is fixed and large.

### A.4. A uniform bound for the marked Euler product

Work in the finite coefficient ring in w,z, retaining degrees at most 2 in each variable. Equip it with the sum of absolute values of its coefficients, a submultiplicative norm. This avoids taking logarithms of small-prime factors that could vanish at some imaginary Mellin height.

Write actual Mellin variables as sigma=s/L, tau=t/L. Set

X=p^(-1-sigma-tau), Y=p^(-1-sigma-beta),
U=p^(-1-tau-alpha), V=p^(-1-tau-gamma), W=p^(-1-tau),

and q_p=log p/ell. The exact local Z factor is

E_p(w,z)=1+(1+w q_p)(1+z q_p)X-(1+w q_p)Y
          -(1+z q_p)p^(-1-tau)R_p,

R_p=[p^(-alpha)+p^(-gamma)-1-p^(-1-beta-alpha-gamma)]/[1-p^(-1-beta)].

Uniformly in imaginary s,t and on the fixed shift circles,

p^(-1-tau)R_p=U+V-W+O(p^(-2+epsilon_T)),

with epsilon_T=O(1/L). The denominator in R_p is uniformly bounded away from zero. Define

D_p=(1-Y)(1-U)(1-V)/[(1-X)(1-W)],

lambda_p=q_p(X-Y), nu_p=q_p(X-U-V+W), kappa_p=q_p^2 X.

The unmarked D_p is precisely the local factor of the Mellin-dependent zeta quotient. Factoring in the finite coefficient ring,

E_p(w,z)=D_p exp(w lambda_p+z nu_p+wz kappa_p) A_p(w,z).

The first-order prime terms cancel coefficient by coefficient. Direct expansion, using |1-X|,|1-Y|,|1-U|,|1-V|,|1-W| bounded below, gives

||A_p-1|| <= C p^(-2+epsilon_T) (1+q_p)^4.

Consequently A=product_p A_p converges absolutely in this ring and ||A||<=C uniformly in all imaginary Mellin heights, T large, and the chosen shifts. The same argument for J omits V,W and uses nu_p=q_p(X-U). Its full quotient is W_J=zeta(1+alpha+beta)zeta(1+sigma+tau)/[zeta(1+sigma+beta)zeta(1+tau+alpha)]. Both W_Z and W_J have equal numbers of numerator and denominator poles; their local limits are F and G without an additional power of L.

The remaining prime sums are

Lambda_u=sum_p lambda_p, Lambda_v=sum_p nu_p, Kappa=sum_p kappa_p.

They are uniformly O(1). Indeed their absolute values are bounded using

sum_p log p/p^(1+c_0/L)=O(L),
sum_p (log p)^2/p^(1+c_0/L)=O(L^2),

and ell=theta L. These bounds follow directly by partial summation from the Chebyshev bound sum_{p<=x}log p=O(x), or from the positive real logarithmic derivative of zeta. Therefore every marked coefficient through w^2z^2 is bounded by C times the unmarked zeta quotient.

For Z the quotient is

W_Z= zeta(1+alpha+beta) zeta(1+beta+gamma)
      zeta(1+sigma+tau) zeta(1+tau)
    /[zeta(1+beta) zeta(1+sigma+beta)
      zeta(1+tau+alpha) zeta(1+tau+gamma)].

The outer three factors have size O(L), O(L), O(1/L), respectively, on the separated circles. All other zeta and inverse-zeta factors are individually O(L), uniformly at every imaginary height, by their absolutely convergent Dirichlet series at real part 1+c_0/L. Thus |W_Z|=O(L^6). The intentionally looser O(L^10) bound covers every Z/J marked coefficient and all the fixed scaled Cauchy derivatives. J needs fewer factors. The bound is for the dimensionless arithmetic kernel, after the I time derivative and J log have been divided by L.

### A.5. Mellin tails

Let R=L^(1/4). If |Im s|>R or |Im t|>R, the global bound and the profile weights give

integral over the omitted region <= C L^10 R^(-B)
                                  = C L^(10-B/4)=O(L^-15).

This bounds every branch, every needed marker coefficient and every scaled Cauchy derivative. Constants depend on theta and the fixed profiles, which is harmless. The same tail statement applies before or after the elementary time integrations.

### A.6. Local expansion and dominated convergence

Inside |Im s|,|Im t|<=R, the actual Mellin and shift variables are O(L^-3/4). The ordinary arithmetic factor at all variables zero is exactly 1: E_p(0,0)=D_p=1-1/p there. Its unmarked derivative series converges absolutely near zero. Marker coefficients in A beyond its constant term are O(1/ell), with higher marked degrees gaining corresponding powers except for harmless products. Hence, in the finite coefficient norm,

A=1+O((1+|s|+|t|)/L).

For S_1(v)=sum_p log p/p^(1+v) and S_2(v)=sum_p (log p)^2/p^(1+v), prime powers are analytic near zero, so

S_1(v)=1/v+O(1), S_2(v)=1/v^2+O(1).

Uniformly in this box, therefore,

Lambda_u=H_u/theta+O(1/L),
Lambda_v=H_v/theta+O(1/L),
Kappa=1/[theta^2(s+t)^2]+O(1/L^2),

with H_u,H_v as in the kernel derivation. Every H and 1/(s+t)^2 is uniformly bounded on the Mellin lines and shift circles.

Laurent expansion of each zeta and inverse zeta factor gives

W_Z=F(a,b,c;s,t)[1+O((1+|s|+|t|)/L)],
W_J=G(a,b;s,t)[1+O((1+|s|+|t|)/L)].

On these contours both F and G are bounded by C(1+|s|)(1+|t|). Thus the full marked error, including each fixed scaled derivative, is bounded by

C/L * (1+|s|+|t|)(1+|s|)(1+|t|).

Multiplied by the two Mellin weights this is integrable uniformly in the expanding box, and its integral is O(1/L). The rational-kernel integrals outside the box also tend to zero by the same polynomial envelope and the high profile decay.

The coefficient of z^2 is F H_v^2/(2theta^2). The coefficient of w^2z^2 is

F/theta^4 * [H_u^2H_v^2/4 + H_u H_v/(s+t)^2 + 1/(2(s+t)^4)],

and similarly for G. This records explicitly the nonnegligible same-prime mixed marker term.

Finally the time integrals create no additional difficulty. For fixed scaled d,

integral_0^T (x/(2pi))^(-d/L) dx
 = T (T/(2pi))^(-d/L)/(1-d/L)
 = T e^(-d)[1+O(1/L)].

The corresponding log-weighted integral is obtained by differentiation and equals TL e^(-d)[1+O(1/L)]. These estimates hold with every fixed scaled derivative used above. The I term contributes TL from the gamma derivative and the J term contributes TL from its explicit logarithm; the subsequent alpha,beta derivatives each contribute L. Normalizing by N(T)L^2=(TL^3/(2pi))[1+O(1/L)] completes the claimed moment asymptotic.
