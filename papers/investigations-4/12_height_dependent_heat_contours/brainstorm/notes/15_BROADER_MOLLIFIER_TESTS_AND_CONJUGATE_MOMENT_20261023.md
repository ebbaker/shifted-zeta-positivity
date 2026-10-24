# Beyond the two-prime test: fixed-rank orthogonality, a prime-power test, and the conjugate moment

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Source, kernel, analytic and optimization checks were divided among separate same-model agents and reconciled by the parent. This is internal mathematical research, not specialist or formal verification.

**Status: proved in-note for the two completed tests, within their stated scopes; the conjugate arithmetic remains open.**

**Outcome:** the cancellation in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md) extends to every fixed elementary distinct-prime rank in a specified smoothed class. A concrete nonsquarefree inverse-square coefficient test also gives no leading gain, after its different logarithmic normalization is included. Conjugating the baseline produces a different observable and an exact comparison, but its useful arithmetic moment is not supplied by the checked theorems. No simplicity percentage is improved.

This continuation serves SIMP-01 by screening two additional arithmetic classes and identifying the new moment required by a third. Its classification is a scoped arithmetic obstruction plus an unclosed comparison, not an RH-equivalent reformulation. See the repository [result index](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [scope discipline](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [normalization discipline](../../../../../avoid/08_normalization_and_constant_slips.md), and [unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). The [internal review](../reviews/06_BROADER_MOLLIFIER_AND_CONJUGATE_REVIEW_20261023.md) distinguishes proved statements from formal calculations and missing arithmetic.

## 1. Baseline and the two completed tests

Keep fixed 0<theta<1/2, y=T^theta, L=log T, ell=theta L, and u_n=log(y/n)/ell. Let E_T average over all zero labels with 0<gamma<=T, repeated by multiplicity. Under RH set

\[
 D_P(s)=\sum_{n\le y}\mu(n)P(u_n)n^{-s},\qquad
 w_X(\rho)=\zeta'(\rho)X(\rho)/L.
\]

The ordinary optimum is P_0(u)=(1+theta)u-theta u^2 and w_0=w_D_P0. Its established moments are

\[
 a=\frac{\theta^2+3\theta+3}{6},\quad
 b=\frac{(1+\theta)^3(\theta^2+3\theta+3)}{36\theta},\quad
 c=\frac ab=\frac{6\theta}{(1+\theta)^3},\quad
 F_\theta=\frac{a^2}{b}=1-(1+\theta)^{-3}.
\]

Their iterated theta endpoint gives the classical 19/27 benchmark. We do not set theta=1/2 in a moment theorem.

### Every fixed elementary prime rank

Let e_k(n) be the elementary symmetric polynomial of degree k in {log p:p divides n}, with e_0=1, and put

\[
 F_{k,Q}(s)=\sum_{n\le y}\mu(n)\frac{e_k(n)}{\ell^k}Q(u_n)n^{-s}.
\]

For each fixed k take a fixed real polynomial Q divisible by u^(100+2k). Appendix A proves actual first, mixed and finite square limits, including

\[
 a_k(Q):=\lim E_T w_{F_{k,Q}}=
 \begin{cases}
 Q(1)/2+\theta\int_0^1Q,&k=0,\\
 \theta\int_0^1(1-u)Q,&k=1,\\
 \theta^2\int_0^1(1-u)^3Q/12,&k=2,\\
 0,&k\ge3,
 \end{cases}
\]
\[
 \lim E_T[w_0\overline{w_{F_{k,Q}}}]=c^{-1}a_k(Q).
\]

The new algebraic step is a closed generating identity for the baseline Mellin residue:

\[
 R_\theta(z,t)=c^{-1}\left(\frac12+\frac1t+
                    \frac z{t^2}+\frac{z^2}{2t^4}\right). \tag{1}
\]

The rank-k coefficient is extracted from the exponential marker exp(zH), then multiplied by theta^(-k). A degree bound is proved before the finite algebra is performed, so (1) covers all fixed ranks, rather than extrapolating from checked ranks. The other Mellin residue has zero outer integral with all boundary terms controlled.

Thus the baseline residual is orthogonal to every fixed finite collection of these directions and ordinary profiles. The limiting residual norm cannot decrease, and every fixed combination with positive limiting second moment has leading Cauchy quotient at most F_theta. The nullspace qualification of Note 14 remains: this does not cover lower-order rescaling of limiting null directions, growing families, products of marked statistics, general prime weights or arbitrary mollifiers. The lower smoothing order already proved for rank two in Note 14 is unchanged.

### A concrete nonsquarefree test

Let mu_2=mu*mu, the coefficients of zeta(s)^(-2), and choose

\[
 B_2(s)=\sum_{n\le y}\mu_2(n)u_n^{100}n^{-s},\qquad
 v_T(\rho)=\frac{w_{B_2}(\rho)}{\sqrt L}.
\]

Prime-square coefficients are retained: mu_2(p)=-2 and mu_2(p^2)=1. Appendix B proves

\[
 E_Tv_T\longrightarrow0,\qquad
 E_T[w_0\overline{v_T}]\longrightarrow0,\qquad
 E_T|v_T|^2\longrightarrow \frac{D_{100}(\theta)}{\zeta(2)}>0, \tag{2}
\]

where, for integers B>=2, the exact rational integral is

\[
\begin{aligned}
D_B(\theta)={}&\frac{B(B-1)}{48(2B-1)(2B-3)}
 +\frac{B\theta}{3(2B-1)(2B+1)}
 +\frac{\theta^2}{(B+1)(2B+1)}\\
 &+\frac{(5B+3)\theta^3}{(B+1)^2(2B+1)(2B+3)}
 +\frac{\theta^4}{(B+1)^2(B+2)^2}.
\end{aligned} \tag{3}
\]

Every displayed term is positive. The arithmetic theorem here uses B=100; the general-B rational identity alone is not a low-smoothing theorem.

The unscaled squared norm grows like L D_100/zeta(2). Treating it as a bounded norm would misread the candidate. In the normalized basis (w_0,v_T), the mean vector tends to (a,0) and the Gram matrix tends to diag(b,D_100/zeta(2)), which is strictly positive definite. Gram-inverse convergence therefore gives

\[
 \sup_{(A,C)\ne(0,0)}
 \frac{|E_T(Aw_0+Cv_T)|^2}{E_T|Aw_0+Cv_T|^2}
 \longrightarrow F_\theta. \tag{4}
\]

The supremum includes coefficients depending on T. Since the span is unchanged by the factor sqrt(L), (4) also applies to the original two-dimensional span (w_0,w_B2). This particular test has no limiting-null-direction loophole. It is not a theorem about all nonsquarefree coefficients or an arbitrary joint span with the elementary-rank family.

A formal calculation also gives a zero raw residual with P_0. We do **not** claim its actual order-one cross asymptotic: the old H^1 approximation argument would incur the candidate's growing sqrt(L) norm. The normalized argument proving (2) avoids that error. No O(1/L) gain estimate for the raw P_0 comparison is asserted.

## 2. Conjugation exposes a different, unclosed arithmetic moment

For the real-coefficient ordinary B=D_P0, the exact dual function

\[
 B^*(s)=-\chi(s)^{-1}B(1-s),\qquad
 \zeta(s)=\chi(s)\zeta(1-s),
\]

satisfies w_B*(rho)=overline(w_0(rho)) under RH. Indeed zeta'(rho)=-chi(rho)zeta'(1-rho). This holds also at multiple zeros without dividing by zeta'(rho). The inverse chi factor is essential.

The new mixed quantity is

\[
 H_T=E_Tw_0^2=\frac1{N(T)L^2}
      \sum_{0<\gamma\le T}\zeta'(\rho)^2B(\rho)^2. \tag{5}
\]

It is a holomorphic square, whereas Note 14 supplies an absolute square. The two are not interchangeable. The dual is not a short Dirichlet polynomial, so BEN/HLZ cannot be applied by silently replacing their polynomial twist with B*.

There is a useful exact comparison. Write a_T=E_Tw_0, b_T=E_T|w_0|^2, rotate z_T=exp(-i arg a_T)w_0 when a_T is nonzero, and put H'_T=exp(-2i arg a_T)H_T. Cauchy–Schwarz on the support of Re z_T gives

\[
 \frac{N_{\rm simple}(T)}{N(T)}\ge
 \frac{2|a_T|^2}{b_T+\Re H'_T}\ge\frac{|a_T|^2}{b_T}. \tag{6}
\]

This is an exact algebraic comparison, not a new evaluated asymptotic bound. A sufficient new input for strict leading improvement is

\[
 \liminf_{T\to\infty}E_T(\Im w_0)^2>0. \tag{7}
\]

If H_T converges to H, the feasible disk is |H-a^2|<=b-a^2. Real-part symmetrization then gives 2a^2/(b+Re H). For H unequal to b the full span of w_0 and its conjugate has positive-definite Gram matrix and optimized quotient

\[
 F_{\rm dual}=\frac{2a^2(b-\Re H)}{b^2-|H|^2},\qquad
 F_{\rm dual}-F_\theta=
 \frac{a^2|b-H|^2}{b(b^2-|H|^2)}>0. \tag{8}
\]

The feasible disk shows that Re H=b forces H=b. At H=b the baseline is asymptotically real in L^2, and the conjugate difference is a limiting null direction requiring lower-order analysis. The already proved a,b moments allow both cases; they do not establish (7).

The exact contour identity is

\[
 \sum\zeta'(\rho)^2B(\rho)^2=
 \frac1{2\pi i}\int_{\mathcal C}\frac{\zeta'(s)^3}{\zeta(s)}B(s)^2\,ds,
\]

with a contour enclosing the relevant zero labels and excluding the pole of zeta. Transforming the left edge produces chi(s)^2. A term with Dirichlet index m and B^2 index n has leading phase t log(m/n)-2t log(t/(2pi e)), and a stationary point at t=2pi sqrt(m/n). A useful proof must control the resulting square-root exponential sums in aggregate. No such aggregate estimate is established here.

## 3. Literature limits and research decision

[Hughes–Pearce-Crump, arXiv:2509.07792v1](https://arxiv.org/html/2509.07792v1), Conjecture 5 and Section 9.2, presents even the unmollified holomorphic derivative square as conjectural, with leading term T log(T/(2pi))^3/(12pi). Their [companion, 2509.07788v1](https://arxiv.org/html/2509.07788v1), Conjecture 1, treats complex powers; its proved first-moment cases do not supply the k=2 mollified formula. Neither conjecture is imported as an RH-only theorem.

[Durkan–Hughes–Pearce-Crump, arXiv:2601.18025v1](https://arxiv.org/html/2601.18025v1), Theorem 5, error (2.1), Corollary 5.1 and Lemma 6, supplies chi-weighted zero sums with explicit transition errors. It does not directly evaluate (5), and termwise errors cannot be discarded before summing the differentiated polynomial expansion. This is a checked limitation of that import, not proof that every possible phase estimate fails.

A separate strategy lead is [Conrey et al., arXiv:2508.11108v1](https://arxiv.org/html/2508.11108v1), on optimizing derivative combinations in Levinson's method. Only its metadata, abstract and introductory setup were inspected. Its detector differs from the derivative-supported statistic here; no simplicity improvement or transfer theorem is imported.

The completed result changes the search decision: raising the elementary prime rank cannot supply a leading gain in the proved class, and the concrete inverse-square test also fails after normalization. The conjugate route remains outside these exclusions. Its next useful calculation is a quantitative bound on (5), or directly on (7), with the complete aggregate errors. Rewriting the same phase problem as another criterion would not supply that estimate. Longer mollifiers, other coefficient structures, and other observables remain available, with their own proof obligations.

At a multiple zero every observable used in (1)–(8) that contains zeta' vanishes. The [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) therefore remain compatible with the support algebra. The load-bearing inputs in the completed exclusions are the exact zeta arithmetic moment formulas, not generic heat-flow shape properties. Those formulas have not been established for the Euler-factor, weighted-square, reflected, finite-prime-compatible or perturbed-source controls. No individual theta collision is excluded, and sparse doubles remain compatible with a proportion bound.

All newly encountered articles are in the [reference catalog](../../references/README.md), with external PDFs and verified hashes. The manuscripts are unchanged and SIMP-01 remains open. No exhaustive priority or novelty claim is made.

## 4. Reproducible algebra

The [all-rank generating check](../numerics/15_all_rank_residue_check.py) and [record](../numerics/15_all_rank_residue_check_20261023.json) verify the finite residue polynomial at two distinct extraction grids. The independent [direct rank check](../numerics/15_rank_direct_check.py) and [record](../numerics/15_rank_direct_check_20261023.json) use full-kernel numerator division for ranks 3–6. The [inverse-square check](../numerics/15_mu2_normalization_check.py) and [record](../numerics/15_mu2_normalization_check_20261023.json) verify exact prime-power factors, complete kernels and the positive norm formula. They check algebra; the asymptotic errors and scope are supplied by the following proofs.

## Appendix A. Proof for all fixed elementary ranks

### A.1. Generating kernel and two possible s poles

Use F,G,H_u,H_v from [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md). Replace the right mark H_v^2/2 by exp(zH_v), the swapped-left mark by exp(zH_u), and the J mark by exp(zH_v^J). Retain the complete three-branch I expression, its swapped orientation, and the two J branches. Differentiate in a,b,c for I and a,b for J exactly as in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md). Let K(z;s,t) denote this complete generating expression, understood coefficient by coefficient in z.

For each fixed rank k, its coefficient K_k(s,t) has poles in s only at s=0, of order at most one, and s=-t, of order at most k+1. It is bounded as s tends to infinity with t fixed. This follows directly before shift differentiation: every right kernel contains (s+b)/(s+t), while the swapped-left kernel contains (s+a)(s+c)/[s(s+t)]. Every marker is 1/(s+t) plus a function of t and shifts alone. Differentiating shifts does not increase the s pole orders.

Multiplication by the baseline Mellin factor

M0(s)=(1+theta)/(theta s^2)-2/(theta s^3)

and exp(theta s) therefore gives residues only at 0 and -t. The latter has the factor exp(-theta t). We pay its outer-contour disappearance below, rather than simply omitting it.

### A.2. Explicit s=0 residue formulas

Write h=theta, q=1/t, m1=(1+h)/h, m2=-2/h. The right F kernel factors as

F(a,b,c;s,t)=C_R (s+b)/(s+t),
C_R=b(t+a)(t+c)/[(a+b)(b+c)t].

Let

r0=bq, r1=(1-bq)q, r2=-(1-bq)q^2,
H_R0=2q-1/(t+a)-1/(t+c).

Its baseline s=0 residue with the exponential marker is

C_R exp(z H_R0) [ r0+(1-h)/h (r1-zq^2r0)
 +m2(r2-zq^2r1+zq^3r0+z^2q^4r0/2) ].                 (A.2)

For a left marker before swapping a,b, use F(a,b,c;t,s). Set

C_L=b(t+b)/[(a+b)(b+c)],
d=acq, E=a+c-t-acq,
r0=(a+c)q-acq^2, r1=-Eq^2, r2=Eq^3,
H_L0=q-1/(t+b),
c1=h-zq^2,
c2=c1^2/2+zq^3,
c3=c1^3/6+c1 zq^3-zq^4.

The corresponding residue is

C_L exp(z H_L0) [m1(d c2+r0 c1+r1)+m2(d c3+r0 c2+r1 c1+r2)].       (A.3)

For J, use formula (A.2)'s bracket with

C_J=(t+a)/(a+b), H_J0=q-1/(t+a).

Insert these residues into the prescribed branch sums. In the left orientation swap a,b first, including the phases. These formulas follow by Taylor expansion in s through order3; no contour approximation is used.

### A.3. Why the generating calculation is finite

Substitute (a,b,c)=epsilon(A,B,C). Each C_R or C_L has a simple epsilon pole. The residual exponential has H_R0,H_L0=O(epsilon). In (A.2), the z^2 coefficient has an additional factor b=O(epsilon); the z coefficient can begin at epsilon^0. Therefore extracting epsilon^3 produces a polynomial in z of degree at most5. In (A.3), the z^3 coefficient has d=acq=O(epsilon^2), the z^2 coefficient begins at epsilon, and the z coefficient can begin at epsilon^0. Again the epsilon^3 coefficient has z-degree at most5. For J, extraction is at epsilon^2, and the maximum z-degree is4.

The complete branch sums have removable shift poles. Their epsilon^3 coefficient is a homogeneous polynomial of degree3 in A,B,C, and a unit mixed finite difference extracts its ABC coefficient exactly. The analogous degree2 assertion applies to J. This is the same exact algebraic device justified in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md); it is not finite-step differentiation of the analytic function.

Expanding (A.2),(A.3) to these finite orders gives exactly (1). The independent output components I_right,I_left,J are retained in [the generating check record](../numerics/15_all_rank_residue_check_20261023.json); their z^3,z^4,z^5 coefficients cancel in the complete sum. The script [the generating check](../numerics/15_all_rank_residue_check.py) reproduces the identity using rational arithmetic. It was run with both nonsingular starting triples (1,3,5) and (2,7,11), with exact difference zero in both cases. Both runs are included in the same record.

Because degree<=5 was established before calculating coefficients, the identity proves the statement for every k. There is no untested tail in rank.

### A.4. The discarded s=-t residue is bounded at infinity

This also supplies the ordinary-profile continuity needed to use P0.

For fixed rank k, F H^k is homogeneous of degree -k in (a,b,c,s,t). Before adding phases its Laurent expansion in scaled shifts has lowest epsilon order -1. To extract degree3, at most the fourth phase term can occur. Thus the complete I contribution to K_k is a sum of rational homogeneous functions of Mellin degree

-k-3 <= d <= 1-k.

For J the degree range is -k-2<=d<=1-k. Partial fractions in s consequently have the form

K_k(s,t)=A_k(t)+B_k(t)/s+sum_{j=1}^{k+1}C_{k,j}(t)/(s+t)^j,

where A,B,C are Laurent polynomials in t. Every monomial in C_{k,j} has t-degree d+j<=j+1-k<=2. These claims follow from the pole locations, boundedness at s=infinity, and homogeneity; no residual asymptotic is assumed.

At s=-t the j-th partial fraction contributes

exp(-h t) C_{k,j}(t)/(j-1)! *
 sum_{r=0}^{j-1} binomial(j-1,r) h^(j-1-r) M0^(r)(-t).

Since M0^(r)(-t)=O(t^-2-r), the rational factor after exp(-ht) has growth at most

t^(j+1-k-2-r)=t^(j-1-k-r)=O(1),

because j<=k+1. It has poles only at t=0. For a profile vanishing to order B>=1, M_Q(t)=O(t^-B-1). Therefore the outer integrand after exponential cancellation is rational, has all poles at0, and is O(t^-B-1). Its contour can be closed to the right and gives zero. This proves the discarded contribution vanishes for every fixed k.

### A.5. Actual arithmetic extraction and the ordinary baseline

The high-smoothing localization proof in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md) extends to fixed rank k in the finite coefficient ring modulo w^(k+1),z^(k+1). The logarithmic singular factor is

exp(w H_u/theta+z H_v/theta+wz/[theta^2(s+t)^2]).

Its coefficient w^k z^k, for example, is

theta^(-2k) sum_{r=0}^k H_u^(k-r) H_v^(k-r)
                  /[(k-r)!^2 r! (s+t)^(2r)].

All repeated-prime remainder terms involve absolutely convergent prime sums with p^(-2+epsilon_T) decay, where epsilon_T=O(1/L). The local remainder bound has the form

C_k p^(-2+epsilon_T) (1+log p/ell)^(2k),

which is summable uniformly in T for fixed k. Normalized prime sums of the first and mixed second degrees are O(1), exactly as in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md). Thus the same global L^10 bound holds with a constant depending on k. With B_k=100+2k and cutoff L^1/4, the tail is O(L^(10-B_k/4))=O(L^-15-k/2). The local expansion has O(1/L) integrated error: H_u,H_v and 1/(s+t)^2 are bounded on the right Mellin lines, so the rational growth envelope remains C_k(1+|s|)(1+|t|). Shift Cauchy contours are unchanged.

Admissibility is equally straightforward. On squarefree n<=y,

0<=e_k(n)/ell^k<=1/k!.

Consequently fixed sufficiently small complex perturbations of the envelope mu(n)u_n^B remain comparable in modulus to mu(n)^2u_n^B; finite complex polarization extracts all required moments. This proves actual high-smoothing cross and square limits without importing a theorem for the isolated non-submultiplicative coefficients.

To extend the ordinary comparison profile to P0, keep Q fixed and approximate P0 in H^1 by high-smoothing ordinary polynomials, exactly as in [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md). The candidate square moment is finite, so the actual mixed functional extends by Cauchy--Schwarz. Its rational expression also extends: the partial fractions above have only an s=0 simple pole, a constant part, and powers of (s+t)^-1. Inverse s transformation uses P(1), an integral of P, and convolutions of P against exp(-t v)v^(j-1). Every coefficient C_{k,j}(t) has t-degree at most2, and the constant/simple-pole coefficients have degree at most1-k and2-k, respectively. Thus outer inversion requires at most two Q derivatives and finitely many antiderivatives. Q(0)=Q'(0)=0 removes the derivative boundary distributions; the resulting kernels are continuous. The functional is bounded by C_{k,Q}(|P(1)|+||P||_2), hence continuous in H^1.

This identifies the actual cross with the low-degree baseline as the inverse transform of the s=0 residue (1).

### A.6. First moments and final normal equation

For k>=3, the corrected shifted first-moment formula has zero main derivative: the Feng coefficient is supported on squarefree integers with at least k distinct primes, whereas its first shifted derivative is supported on squarefree integers with at most two prime factors. The fixed-rank coefficient satisfies the same admissible affine-envelope argument, so the remainder has the arbitrary logarithmic saving from the source theorem. Thus its normalized first moment tends to zero.

Rank1 is coefficientwise the ordinary profile (1-u)Q, since mu(n)e_1(n)=mu(n)log n. Rank2 is [Note 14](14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md), and rank0 is the classical ordinary first moment. This gives the displayed a_k formulas.

Finally, inverse transformation of 1/t^j gives

(2pi i)^-1 integral exp(theta t) M_Q(t)t^-j dt
 = theta^j/(j-1)! integral_0^1 (1-u)^(j-1)Q(u)du,

for j>=1, while j=0 gives Q(1). Apply this to (1), with theta^-k for rank k. The cross limit is c_theta^-1 a_k(Q) in every rank. This proves the stated zero residual correlations.

No gain follows in the limiting residual functional from any fixed finite collection of these linear marked-prime directions. This does not exclude products of marked statistics, other prime weights, nonsquarefree coefficients, lower-order nullspace effects, varying dimension, or all mollifiers.


## Appendix B. Proof of the normalized inverse-square test

### B.1. Admissible coefficients and first moment

Use the corrected Benli–Elma–Ng Theorem 1.1 for the first moment and the explicitly unconditional Heap–Li–Zhao Theorem 2 for the shifted second moment, as imported and audited in Note 14. RH is needed only for the Hermitian interpretation. No simplicity assumption is imported from HLZ's separate negative-moment application.

The prime-power values of |mu_2| are (1,2,1,0,...), hence |mu_2(mn)|<=|mu_2(m)mu_2(n)|. Together with u_mn<=u_m u_n, this makes |mu_2(n)|u_n^100 a submultiplicative divisor-bounded envelope. To recover mixed formulas with ordinary profiles u^100 R and inverse-square profiles u^100 S, use fixed sufficiently small complex perturbations

\[
 \mu_2(n)u_n^{100}
 \left[1+\epsilon S(u_n)+\delta\frac{\mu(n)}{\mu_2(n)}R(u_n)\right].
\]

On cube-free support the ratio is zero off squarefree integers and equals 2^(-omega(n)) on squarefree integers; elsewhere set the coefficient to zero. The bracket can be kept in modulus between 1/2 and 3/2. Thus every coefficient family used in finite complex polarization meets the imported hypotheses uniformly in T.

For the first moment alone, take any fixed polynomial Q(0)=0. Use the envelope mu_2(n)u_n and the bounded polynomial Q(u)/u in the same small complex affine argument; the u^100 restriction is only needed for the second-moment extraction here. For V_Q(s)=sum mu_2(n)Q(u_n)n^(-s), BEN with Y=1 gives

\[
 \lim E_T w_{V_Q}=Q(1)/2+2\theta\int_0^1Q(u)\,du
                  +\theta^2\int_0^1(1-u)Q(u)\,du. \tag{B.1}
\]

Here the n=1 term contributes Q(1)/2. The prime contribution, including the coefficient -2, has leading prime sum

\[
 \sum_p\frac{2Q(u_p)}{p-1}
       \left(L\log p-\frac{(\log p)^2}{2}\right).
\]

After division by L^2 it gives 2theta integral Q minus theta^2 integral (1-u)Q. The pq term has coefficient 4; its unordered-prime sum gives 2theta^2 integral (1-u)Q. Terms with a repeated prime have a convergent prime factor in place of one divergent factor and are o(L^2). There are finitely many exponent patterns at the only relevant distinct-prime counts, one and two. Three or more distinct primes vanish after the first shift derivative, since Phi(alpha,n) has that many zeros at alpha=0 and zeta(1-alpha) only a simple pole. The separate prime-power term is also lower order. The PNT and partial summation justify these limits. The BEN error retains arbitrary logarithmic saving after differentiation.

For Q=u^100, (B.1) is 1/2+2theta/101+theta^2/10302, so the mean divided by sqrt(L) tends to zero. The unnormalized first-moment statement does not need RH.

### B.2. Euler factors and actual high-smoothing moments

Put mu_1=mu and take r,q in {1,2} on the two coefficient sides. With actual shifts alpha=a/L, beta=b/L, gamma=c/L, the singular zeta quotient is

\[
 W_{r,q}=\frac{\zeta(1+\alpha+\beta)\zeta(1+\beta+\gamma)
 \zeta(1+(s+t)/L)^{rq}\zeta(1+t/L)^q}
 {\zeta(1+\beta)\zeta(1+s/L+\beta)^r
 \zeta(1+t/L+\alpha)^q\zeta(1+t/L+\gamma)^q}.
\]

Its net pole order is (r-1)(q-1). The leading rational kernels, before the complete shift derivatives and branch sums, are

\[
 F_{r,q}=\frac{b(s+b)^r(t+a)^q(t+c)^q}
 {(a+b)(b+c)(s+t)^{rq}t^q},\qquad
 G_{r,q}=\frac{(s+b)^r(t+a)^q}{(a+b)(s+t)^{rq}}. \tag{B.2}
\]

The factor L^((r-1)(q-1)) must be kept. The local prime-power triple sums at zero, writing x=1/p, are E_12=1-x and E_22=1-x^2. For E_22 the common-divisor exponents zero, one and two contribute respectively 1-4x+2x^2, 4x-4x^2, and x^2. After extracting the singular quotient, the arithmetic constants are A_12(0)=1 and A_22(0)=product_p(1-p^(-2))=1/zeta(2). The J term has the same constants.

Here are sufficient error bounds, to make the distinction from formal algebra explicit. Initially both profiles are divisible by u^100. Use the same nested scaled Cauchy circles and Mellin lines Re s=Re t=1 as Note 14. The prime-power triple sums are finite. Dividing out their first-order prime terms leaves a product with local factors 1+O(p^(-2+O(1/L))), uniformly in imaginary Mellin height. Its denominators stay away from zero, and its derivatives converge absolutely near the origin.

Counting powers, W_rq has at most fifteen zeta or inverse-zeta factors. Absolute Dirichlet series to the right of 1 and the separated outer shift circles give a global O(L^15) envelope, preserved by fixed scaled Cauchy derivatives. The profile weights decay as (1+|Im s|)^(-101). Cutting off at R=L^(1/4) costs O(L^15 R^(-100))=O(L^(-10)).

In the retained box, local Laurent expansion gives

\[
 W_{r,q}A_{r,q}=L^{(r-1)(q-1)}A_{r,q}(0)F_{r,q}
 +O\!\left(L^{(r-1)(q-1)-1}
 (1+|s|+|t|)(1+|s|)^2(1+|t|)^4\right),
\]

and similarly for G. The envelope is integrable against both Mellin weights. Elementary time integration introduces the branch exponentials with relative error O(1/L). The gamma derivative or explicit logarithm gives L, and the final two shift derivatives give L^2, canceled by the common N(T)L^2 normalization as in Note 14. All I branches, both orientations, and J are retained.

It follows that every fixed high-smoothing ordinary/inverse-square cross is its finite rational integral plus O(1/L), hence O(1). The inverse-square square is L/zeta(2) times its rational integral plus O(1). The source error is smaller after choosing its arbitrary logarithmic saving. This is a fixed-profile, fixed-theta assertion.

### B.3. Positive square integral

Applying the complete derivative-and-branch operation of Note 14 to (B.2) gives

\[
 K_{22}(s,t)=\frac{N_{22}(s,t)}{12s^2t^2(s+t)^4},
\]
\[
\begin{aligned}
 N_{22}={}&s^4t^4+8s^4t^3+24s^4t^2+24s^4t+12s^4\\
 &+8s^3t^4+48s^3t^3+96s^3t^2+48s^3t\\
 &+24s^2t^4+96s^2t^3+72s^2t^2+24st^4+48st^3+12t^4.
\end{aligned}
\]

With M_B(s)=B!/(theta^B s^(B+1)), the monomial c_ij s^i t^j in N_22 contributes to the double inverse transform

\[
 \frac{c_{ij}(B!)^2}{12}
 \frac{(2B+4-i-j)!\,\theta^{8-i-j}}
 {(B+2-i)!(B+2-j)!(2B+8-i-j)!}.
\]

All factorial arguments are nonnegative for B>=2. Summing by i+j gives (3), with each coefficient positive. Combining the arithmetic factor and the error bounds proves E_T|w_B2|^2=L D_100/zeta(2)+O(1), not merely an upper bound.

### B.4. The normalized mixed limit and uniform optimization

For any fixed ordinary P divisible by u^100, B.2 gives E_T[w_P overline(v_T)]=O(L^(-1/2)), hence zero in the limit. Approximate P_0 in H^1 by fixed polynomials P_j divisible by u^100: cut P_0 off near zero, divide that smooth cutoff by u^100, then approximate the quotient by polynomials in C^1.

The ordinary moment form in Note 14 is continuous in H^1, and the normalized candidate has square limit D=D_100/zeta(2). Consequently

\[
 \limsup_T|E_T[(w_0-w_{P_j})\overline{v_T}]|
 \le\sqrt{D\,b(P_0-P_j,P_0-P_j)}\longrightarrow0.
\]

Take T to infinity first and j to infinity second. This proves the actual mixed limit in (2). Applying the same argument to the unnormalized candidate would cost sqrt(L) and would not prove a raw cross asymptotic.

Finally, for W_T=(w_0,v_T)^T, set m_T=E_TW_T and G_T=E_T(W_T W_T*). Both converge, with G_T tending to the positive diagonal matrix in Section 1. The exact identity sup_z |z* m_T|^2/(z*G_Tz)=m_T*G_T^(-1)m_T, together with inverse-matrix continuity, proves (4). This supplies only an o(1) additional-gain statement for the low-degree P_0, without claiming an O(1/L) rate.
