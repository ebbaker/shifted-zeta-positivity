# E20 r1: a paid quadratic Green comparison and its fixed-Euler obstruction

7 November 2026. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Executor dispatch selected **gpt-6.1-sol, reasoning effort ultra**, under the author's authorization; this records the actual selection supplied by root, not independent backend verification. Conceptual selection: B04 r5, Astra/ultra. Root configuration is unavailable. This is an analytical execution note, with no numerical experiments, novelty claim or specialist-independence claim.

**Status: proved in-note within the stated scope; awaiting E21 assessment.** The quadratic comparison, complete-boundary residual tail and compact theta-source acquisition are paid. For each fixed finite Euler preconditioner, the center-averaged quadratic residual is unbounded at least logarithmically. No small signed Green residual or zero exclusion is established. The obstruction concerns this particular sufficient quadratic comparison, not the Green statistic itself, exceptional centers, growing Euler cutoffs or all localized metrics.

The frozen contract is [request36](../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_REQUEST_20261107.md), with [inputs36](../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_INPUTS_20261107.json). All **51** listed sources matched their byte counts and SHA-256 hashes before derivation, including the continuation-note copy outside this working tree. The exact versions and final verification are in [return36](../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_RETURN_20261107.json). The then-uncompleted Decision17 was not used as an input. Root owns all shared registers, indexes, manuscript files and chat capture.

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| TND-O-E21 r1 | E — execution | Sol6.1/ultra | Actual Note28 and return36 | Claim-level assessment of comparison, source/tail payments and fixed-Q obstruction |
| Further canonical acquisition | B — brainstorm | Astra | E21 disposition and an explicitly selected new route | A source-sensitive signed estimate or another bounded contract; no growing-Q theorem is supplied here |

## 1. Domain, inherited Green functional and exact claims

Only Newman time **lambda = 0** is used. Let Q be an integer at least two, and put

\[
 s(z)=\frac12-\frac{iz}{2},\quad a=\frac\pi8,\quad
 K(u)=\frac1{16\cosh(au)},\quad q(s)=\frac{s-1}{s},
\]
\[
 M_Q(s)=\prod_{p\le Q}(1-p^{-s}),\qquad
 F_Q(z)=q(s(z))\zeta(s(z))M_Q(s(z)),\qquad c_Q(X)=F_Q(X+4i).
 \tag{1}
\]

The probability measure mu_X has density K(x-X) dx on **each** line y=0,8. Each line has mass 1/2. The inherited complete Green identity from [Note25](25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) is

\[
 J_0(X)=\sum_{j:y_j>0}\operatorname{atanh}
       \frac{\sin(ay_j)}{\cosh(a(X-x_j))},\qquad 0<y_j\le1.
 \tag{2}
\]

Multiplicities and the complete zero sum are retained. Its logarithmic boundary integrals are absolutely integrable, including multiple real zeros. The pole-corrected prime representation, assessed in E17 and recorded in [Decision15](../brainstorm/notes/15_TND_O_B04_R4_SIGNED_METRIC_COMPARISON_20261107.md) and manuscript §18 (source file17_green_strip.tex), remains exactly

\[
 J_0(X)=\mathcal L(X)-P(X)+G(X,1),\quad
 G(X,1)=\operatorname{atanh}\frac{\sin(\pi/8)}{\cosh(\pi X/8)},
 \tag{3}
\]
\[
 \mathcal L(X)=\int K(x-X)\log|\zeta(\tfrac12-ix/2)|\,dx,
\quad P(X)=\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
       \frac{n^{-5/2}}{1+n^{-4}}\cos\left(\frac X2\log n\right).
\]

For integer L>=2, its separate prime tail is at most (2/3)L^(-3/2). The **plus** pole correction in (3) is unchanged; no Euler product is assigned to nonzero Newman time.

Define

\[
 c_0=\frac35\frac{\zeta(5)}{\zeta(5/2)},\qquad U_0=\zeta(5/2),
\qquad
 \epsilon_Q(X)^2=\int\left|\frac{F_Q}{c_Q(X)}-1\right|^2d\mu_X.
 \tag{4}
\]

We prove

\[
 c_0\le |c_Q(X)|\le U_0,\qquad
 \int F_Q\,d\mu_X=c_Q(X),\qquad
 \epsilon_Q(X)^2=\int\left|\frac{F_Q}{c_Q(X)}\right|^2d\mu_X-1,
 \tag{5}
\]
\[
 \boxed{\quad 0\le J_0(X)\le\frac12\log(1+\epsilon_Q(X)^2).\quad}
 \tag{6}
\]

An upper zero with y>=d>0 and |x-X|<=r forces J_0(X)>=m, where

\[
 m=\frac{\sin(a)d}{\cosh(ar)}.\qquad
 \epsilon_Q(X)^2<e^{2m}-1
 \quad\Longrightarrow\quad\text{no zero in that declared class}.
 \tag{7}
\]

Here 0<d<=1 and r>=0; d>1 gives an empty canonical class. This is a sufficient **comparison**, not an assertion that (7)'s hypothesis holds. Section7 proves that uniform bounded smallness over all high centers fails for every fixed Q.

## 2. Analyticity, harmonic mean and zero-free renormalization

For Re s=σ>0, fractional-part continuation gives the directly usable identity

\[
 \zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{v\}v^{-s-1}\,dv,
\qquad
 q(s)\zeta(s)=1-(s-1)\int_1^\infty\{v\}v^{-s-1}\,dv.
 \tag{8}
\]

For σ>1, the first formula follows by Stieltjes integration of the counting function floor(v)=v-{v}; the integral is holomorphic for σ>0, so continuation gives the stated region. Thus qζ extends holomorphically through s=1 with value one. Consequently F_Q(i)=M_Q(1), not zero or a surviving pole. The pole of q at s=0 is outside the closed strip. Every factor 1-p^(-s) is zero-free for Re s>=1/2.

On 1/2<=σ<=9/2, the integral in (8) has modulus at most 1/σ. With s=σ-ix/2, it gives the convenient uniform closed-strip bound

\[
 |q(s)\zeta(s)|\le1+|s-1|/\sigma\le8+|x|,\qquad
 |M_Q(s)|\le C_Q:=\prod_{p\le Q}(1+p^{-1/2}).
 \tag{9}
\]

Therefore F_Q has at most linear horizontal growth on the entire closed strip. Apply the strip Poisson formula separately to its real and imaginary parts. On truncating rectangles, the harmonic measure of the vertical sides decays exponentially, and the linear bound makes their contributions tend to zero. The horizontal integrals converge absolutely against K. At X+4i this proves the full **complex** identity in (5), not merely an identity of real parts or moduli.

At s_c=5/2-iX/2 the absolutely convergent Euler product gives

\[
 \zeta(s_c)M_Q(s_c)=\prod_{p>Q}(1-p^{-s_c})^{-1}.
\]

Its modulus lies between product_(p>Q)(1+p^(-5/2))^(-1) and product_(p>Q)(1-p^(-5/2))^(-1). Including all primes only weakens the lower and upper bounds, giving respectively ζ(5)/ζ(5/2) and ζ(5/2). Also

\[
 \frac35\le\left|\frac{s_c-1}{s_c}\right|\le1.
\]

This proves the two uniform center bounds in (5).

Xi reflection permits H_0(z)=ξ(s(z))/8, and hence exactly

\[
 F_Q(z)=D_Q(z)H_0(z),\qquad
 D_Q(z)=\frac{16\pi^{s(z)/2}M_Q(s(z))}{s(z)^2\Gamma(s(z)/2)}.
 \tag{10}
\]

D_Q is holomorphic and zero-free on a neighborhood of the closed strip: s=0 and the gamma poles are outside, and all the finite Euler factors are nonzero there. Thus log|D_Q| is harmonic. Stirling growth on the fixed real-part interval bounds its modulus by O_Q(1+|x|+log(2+|x|)); compact x is harmless. The same vertical-side and exponential-kernel argument proves

\[
 \int\log|D_Q|\,d\mu_X=\log|D_Q(X+4i)|.
 \tag{11}
\]

Together with Note25's complete logarithmic integrability, (10)-(11) prove

\[
 J_0(X)=\int\log|F_Q|\,d\mu_X-\log|c_Q(X)|
        =\int\log|F_Q/c_Q(X)|\,d\mu_X.
 \tag{12}
\]

Real-boundary logarithmic singularities remain locally integrable with their true multiplicities; no logarithm of an approximate field is inserted there. The removable zeta pole has already been paid in (8),(10), so (12) creates no extra interior atom. In particular one must not add or subtract G(X,1) again when using F_Q; (3) and (12) are two representations of the same J_0.

Since mu_X has total mass one and its complex mean is c_Q, expanding the square proves the variance identity in (5). All square integrals are finite by (9). Jensen's inequality applied to |F_Q/c_Q|² proves (6). Its logarithm is integrable by (12) and the inherited absolute logarithmic bounds; isolated boundary zeros have measure zero. Finally atanh(v)>=v and sin(ay)>=y sin(a) for 0<=y<=1 prove the margin (7) from (2).

## 3. Compact complete-source approximation

This step uses the literal complete theta source and its majorant from frozen manuscript section02. Set

\[
 \rho(u)=\pi e^{4|u|},\quad P_0(v)=2v^2-3v,\quad
 C_2(N)=\sum_{n>N}n^4e^{-\pi(n^2-1)},\quad B_0=5C_2(0),
\]
\[
 J_{0,2}(0,8)=\int_{\mathbb R}e^{9|u|}\rho(u)^2e^{-\rho(u)}\,du,
\quad
 J_{0,2}^{>U}(0,8)=\int_{|u|>U}e^{9|u|}\rho(u)^2e^{-\rho(u)}\,du.
 \tag{13}
\]

The complete reflected source satisfies |Φ(u)|<=B_0 e^|u| ρ²e^(-ρ). The reflected arithmetic tail has the same bound with B_0 replaced by 5C_2(N), because the absolute coefficient sum of P_0 is five. Define the exact finite-source field

\[
 \Phi_N^{\rm ref}(u)=e^{|u|}\sum_{1\le n\le N}P_0(n^2\rho(u))e^{-n^2\rho(u)},
\qquad
 \widehat H_{N,U}(z)=\frac12\int_{-U}^{U}\Phi_N^{\rm ref}(u)e^{izu}\,du.
 \tag{14}
\]

This undifferentiated integral does not require a reflected finite prefix to have matching odd derivatives at u=0. Split H_0-Hhat into the omitted arithmetic terms on |u|<=U and the **complete** source on |u|>U. Using |exp(izu)|<=exp(8|u|) on |Im z|<=8 gives

\[
 \sup_{|\Im z|\le8}|H_0(z)-\widehat H_{N,U}(z)|
 \le \delta_H(N,U;8)
 :=\frac{5C_2(N)J_{0,2}(0,8)+B_0J_{0,2}^{>U}(0,8)}2.
 \tag{15}
\]

Both terms tend to zero with their respective cutoffs. This derives exactly the requested notation from the inherited majorant rather than assigning an unproved full-line error to the gamma-renormalized field.

For R>=0, let mu_(X,R) be the restriction of mu_X to |x-X|<=R, and let

\[
 B_Q(X,R)=16\max_{\substack{|x-X|\le R\\ b\in\{0,8\}}}
 \left|\frac{\pi^{(1/2+b/2-ix/2)/2}
                  M_Q(1/2+b/2-ix/2)}
 {(1/2+b/2-ix/2)^2\Gamma((1/2+b/2-ix/2)/2)}\right|.
 \tag{16}
\]

This is an explicit finite compact supremum of the displayed known factor. For example, the conservative replacement

\[
 B_Q(X,R)\le64\pi^{9/4}C_Q
 \max_{\substack{|x-X|\le R\\b\in\{0,8\}}}
       |\Gamma((1+b)/4-ix/4)|^{-1}
 \tag{17}
\]

is available. There is also a closed conservative bound requiring no gamma supremum. The executor directly checked [DLMF 5.8.2](https://dlmf.nist.gov/5.8#E2), the reciprocal-gamma product, after root supplied the separately hashed [supplemental input receipt](../research-progress/handoffs/36_TND_O_E20_ADDITIONAL_INPUTS_20261107.json) and [source-use16](../references/16_TND_O_GAMMA_PRODUCT_SOURCE_USE_20261107.md). This is later source use, **not part of the initial 51-source freeze**. For Re w>0 its product and the elementary inequality log|1+v|<=Re v+|v|²/2 give

\[
 |\Gamma(w)^{-1}|\le |w|\exp\left(\gamma\Re w+
                      \frac{|w|^2}{2}\sum_{n\ge1}n^{-2}\right)
 =|w|e^{\gamma\Re w+\pi^2|w|^2/12}.
\]

Indeed log|1+v|=(1/2)log(1+2Re v+|v|²) is at most Re v+|v|²/2 by log t<=t-1; apply this to each canonical product factor and pass to its convergent limit. Use gamma<=1, w=s/2 and 1/(2|s|)<=1. With W=|X|+R one obtains

\[
 \boxed{\quad B_Q(X,R)\le\mathcal B_Q(X,R):=
 16\pi^{9/4}C_Q
 \exp\left(\frac94+\frac{\pi^2(81+W^2)}{192}\right).\quad}
 \tag{17a}
\]

Here |s|²<= (81+W²)/4 on the compact boundary. Euler's constant gamma<=1 follows directly from its harmonic-sum limit. The bound is deliberately expensive in height, but fully explicit. Every subsequent B_Q may be replaced by this known upper bound; no gamma-maximization computation is required.

Define Fhat=D_Q Hhat only on the compact acquisition domain and

\[
 \widehat\epsilon_R
 =\left\|\frac{\widehat F_Q}{c_Q(X)}-1\right\|_{L^2(\mu_{X,R})}.
\]

The restricted measure has mass

\[
 \mu_R=\mu_{X,R}(1)=\frac2\pi\arctan(\sinh(aR))\le1.
\]

Consequently (15)-(16) give the probability-norm payment

\[
 \left\|\frac{F_Q-\widehat F_Q}{c_Q(X)}\right\|_{L^2(\mu_{X,R})}
 \le\frac{B_Q(X,R)\delta_H(N,U;8)}{c_0}.
 \tag{18}
\]

No claim is made that (18) extends over all x with the same B_Q. The reciprocal gamma factor grows exponentially in |x|; a uniform absolute H error cannot be inserted on that full boundary. Fhat need not have the original complete field's remote behavior.

## 4. Full remote-tail theorem

At σ=1/2, (8) gives

\[
 |q(s)\zeta(s)|\le1+2|s-1|=1+\sqrt{1+x^2}\le2+|x|,
\qquad |F_Q(x)|\le C_Q(2+|x|).
 \tag{19}
\]

At σ=9/2, |q(s)|<=1, and the rough-prime Euler product gives

\[
 |F_Q(x+8i)|\le\prod_{p>Q}(1-p^{-9/2})^{-1}\le\zeta(9/2).
 \tag{20}
\]

Set B=2+|X| and

\[
 \boxed{\begin{split}
 \tau_Q(X,R)=\frac{e^{-aR}}{2a}\bigg\{
 &\frac{C_Q^2}{c_0^2}\left[(B+R)^2+\frac{2(B+R)}a+\frac2{a^2}\right]\\
 &+\frac{\zeta(9/2)^2}{c_0^2}+2\bigg\}.
 \end{split}}
 \tag{21}
\]

The numerical factors in the frozen target require **no correction**. Indeed |v-1|²<=2|v|²+2 and K(u)<=e^(-a|u|)/8 show that the squared residual on the two remote boundary pieces is at most

\[
 \frac12\int_R^\infty e^{-au}
 \left\{\frac{C_Q^2}{c_0^2}(B+u)^2+
             \frac{\zeta(9/2)^2}{c_0^2}+2\right\}\,du.
\]

There are two horizontal tails, two boundary fields, and the factor two from the square inequality; these account for the prefactor. Integrating the quadratic polynomial gives (21). Thus

\[
 \left\|F_Q/c_Q(X)-1\right\|_{L^2(\mu_X-\mu_{X,R})}^2
       \le\tau_Q(X,R),
\]
\[
 \boxed{\quad\epsilon_Q(X)\le\widehat\epsilon_R+
        \frac{B_Q(X,R)\delta_H(N,U;8)}{c_0}
        +\sqrt{\tau_Q(X,R)}.\quad}
 \tag{22}
\]

For the last inequality, split the exact residual into compact and remote pieces, use sqrt(A²+B²)<=A+B, and apply the compact triangle inequality (18). Only the **exact** F_Q is used in the remote-tail estimate. This pays the complete boundary, without an unproved full-boundary source approximation.

## 5. Safe center acquisition and denominator error

The nonvanishing safe Euler logarithm is

\[
 L_Q(s_c)=\sum_{p>Q}\sum_{k\ge1}\frac{p^{-ks_c}}k,
 \qquad c_Q(X)=q(s_c)e^{L_Q(s_c)}.
 \tag{23}
\]

For an integer L>=max(Q,2), retain precisely the finitely many p>Q, p^k<=L, and call the sum L_(Q,L). With

\[
 \beta_L=\frac23L^{-3/2},\qquad
 \widetilde c=q(s_c)e^{L_{Q,L}(s_c)},
\]

the absolute prime-power coefficients 1/k<=1 give

\[
 |L_Q-L_{Q,L}|\le\sum_{n>L}n^{-5/2}\le\beta_L,
\qquad
 |c_Q-\widetilde c|\le U_0(e^{\beta_L}-1)=:\eta_L.
 \tag{24}
\]

The last inequality uses |q(s_c)|<=1 and exp(Re L_(Q,L))<=ζ(5/2), so it has no phase assumption. Finite Q is handled exactly by deleting its primes, rather than approximating a separate finite-Euler cancellation. If a tolerance η_*>0 is prescribed, an explicit sufficient cutoff is any integer

\[
 L\ge\max\left\{Q,2,
 \left(\frac{2}{3\log(1+\eta_*/U_0)}\right)^{2/3}\right\}.
 \tag{25}
\]

For an actual finite-arithmetic evaluation, add its certified absolute error to η_L. No such numerical evaluation is performed here.

More generally suppose |c_Q-c_tilde|<=η and the **positive denominator margin** ell=|c_tilde|-η is >0. Define the compact norm

\[
 A_R=\|\widehat F_Q/\widetilde c-1\|_{L^2(\mu_{X,R})}.
\]

The denominator payment is

\[
 \left\|\frac{\widehat F_Q}{c_Q}-
                 \frac{\widehat F_Q}{\widetilde c}\right\|_{L^2(\mu_{X,R})}
 \le\frac{\eta}{\ell|\widetilde c|}\|\widehat F_Q\|_{L^2(\mu_{X,R})}
 \le\frac\eta\ell(A_R+\sqrt{\mu_R}).
 \tag{26}
\]

Thus the fully paid version of (22) is

\[
 \epsilon_Q(X)\le A_R+\frac\eta\ell(A_R+\sqrt{\mu_R})
    +\frac{B_Q\delta_H}{c_0}+\sqrt{\tau_Q}.
 \tag{27}
\]

Any positive lower bound for |c_Q|, including c_0, may replace ell in the first denominator of (26). The displayed ell makes explicit the margin that an approximate denominator must retain.

## 6. Order of limits, arbitrary height and consumer requirement

For any finite X,Q and positive total acquisition budget h, proceed in this order:

1. Choose an integer R with tau_Q(X,R)<(h/3)². Such an R exists by the exponential decay in (21); retain its explicit X and Q factors.
2. With that R fixed, B_Q(X,R) is finite. Choose N and U so each term of delta_H in (15) is less than c_0 h/(6B_Q). Then the source contribution in (22) is less than h/3. The arithmetic and radial choices are independent after R is fixed.
3. Finally acquire c_Q to sufficiently small absolute error. For a nonadaptive prescription let Dhat be the finite norm ||Fhat||_(L²(mu_(X,R))). Choose η<c_0/4 and 2η Dhat/c_0²<h/3. Indeed |c_tilde|>=c_0-η, ell>=c_0-2η>c_0/2, and the actual denominator difference is at most 2η Dhat/c_0². Equations (24)-(25) achieve any such η. When Dhat=0 the denominator term vanishes. One may bound Dhat by B_Q B_0 J_(0,2)(0,8)/2 without evaluating it, since the positive truncated source is at most the complete source.

This proves a full-boundary residual acquisition error less than h. The same order works along **any prescribed sequence** of finite (X_j,Q_j,d_j,r_j), even with |X_j|,Q_j unbounded and d_j tending to zero: choose a positive budget h_j first and redo the displayed choices for each j. This is a pointwise finite acquisition theorem with an explicit joint prescription, not a uniform computational-cost estimate or a growing-Q moment theorem. No limit is interchanged through the unbounded gamma-renormalization factor.

To use the Green consumer, its independently acquired compact residual A_R plus all terms in (27) must be strictly below sqrt(exp(2m)-1). Small h supplies accurate acquisition, **not small A_R**. Coverage of all centers, all heights or arbitrarily small d would require the corresponding new uniform residual estimates and a covering argument. No finite-height or finite-index zero checks are performed or claimed. Finite-source integrals/norms in this note are exact mathematical objects; if evaluated later, quadrature or arithmetic errors must also be included.

## 7. Fixed-Q logarithmic obstruction

**External input checked directly by this executor.** Bettin, Chandee and Radziwiłł, *The mean square of the product of ζ(s) with Dirichlet polynomials*, [arXiv:1411.7764v1](https://arxiv.org/abs/1411.7764v1), §1, definition (1.1) and Theorem1 in the [primary converted text](https://arxiv.org/html/1411.7764v1), were opened and checked on 7 November 2026. The version metadata says submitted 28 November 2014; the HTML's anomalous 2026 displayed date does not change the pinned version. The existing [source-use15](../references/15_TND_O_SIGNED_ACQUISITION_SOURCE_USE_20261107.md) records the same input and unsuccessful PDF acquisition. This is inspection of the imported statement and hypotheses, not a full proof audit or a claim to possess a PDF.

The theorem gives, for A(s)=sum_(n<=N) a_n n^(-s), N=S^theta, theta<17/33, a_n<<n^varepsilon and smooth φ supported in [1,2],

\[
 \begin{split}
 I_A(S)&:=\int_{\mathbb R}|\zeta(\tfrac12+it)A(\tfrac12+it)|^2
                         \phi(t/S)\,dt\\
 &=\sum_{d,e\le N}\frac{a_d\overline{a_e}}{[d,e]}
     \int_{\mathbb R}\left[\log\frac{t(d,e)^2}{2\pi de}+2\gamma\right]
                         \phi(t/S)\,dt
 +O(S^{3/20+\varepsilon}N^{33/20}+S^{1/3+\varepsilon}).
 \end{split}
 \tag{28}
\]

No sharp-cutoff formula or theorem about moving Q is imported.

For clarity, in this section **φ is fixed, nonzero and belongs to C_c^infinity((1,2)), with 0<=φ<=1**. Making smoothness explicit is the sole bounded smooth-cutoff clarification of request36; the conclusion is not asserted for an arbitrary nonsmooth bounded function. In particular integral φ>0.

Fix Q once and for all, and let

\[
 P_Q=\prod_{p\le Q}p,\qquad
 M_Q(s)=\sum_{d\mid P_Q}\mu(d)d^{-s}.
 \tag{29}
\]

The **actual polynomial length is P_Q**, not Q or the number of primes. For S>=P_Q^4, zero-pad the coefficients to N=S^(1/4); |a_n|<=1 satisfies (28). Its remainder is O(S^(9/16+varepsilon)+S^(1/3+varepsilon))=o(S), for any fixed sufficiently small varepsilon>0. This threshold and the constants are not uniform in Q.

The leading coefficient factors prime by prime:

\[
 \kappa_Q=\sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
 =\prod_{p\le Q}\left(1-\frac1p-\frac1p+\frac1p\right)
 =\prod_{p\le Q}(1-1/p)>0.
 \tag{30}
\]

Substitute t=Su in (28). All d,e in (29) are fixed, so their constant logarithms have a finite total. Therefore

\[
 I_{M_Q}(S)=\kappa_Q S\log S\int_1^2\phi(u)\,du
                  +O_{Q,\phi}(S).
 \tag{31}
\]

On the lower boundary |q(1/2-ix/2)|=1 exactly; conjugation gives

\[
 |F_Q(x)|^2=|\zeta(\tfrac12+ix/2)M_Q(\tfrac12+ix/2)|^2.
 \tag{32}
\]

By (5), the upper bound U_0 for the center and nonnegativity of the omitted upper-boundary square,

\[
 \epsilon_Q(X)^2\ge U_0^{-2}\int_{\mathbb R}K(x-X)|F_Q(x)|^2\,dx-1.
 \tag{33}
\]

Integrate over T<=X<=2T and apply Tonelli to the complete nonnegative convolution. Let

\[
 w_T(x)=\int_T^{2T}K(x-X)\,dX,\qquad
 k_1=\int_{-1}^{1}K(u)\,du
       =\frac1\pi\arctan(\sinh(\pi/8))>0.
 \tag{34}
\]

For T+1<=x<=2T-1, the interval [x-1,x+1] lies in [T,2T], so w_T(x)>=k_1. The compact support of φ is separated from 1 and 2 by some delta>0. Once delta T>=1, w_T(x)>=k_1 φ(x/T) for every x; outside its support this just uses positivity. Hence

\[
 \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
 \ge\frac{k_1}{TU_0^2}\int_{\mathbb R}|F_Q(x)|^2\phi(x/T)\,dx-1.
 \tag{35}
\]

The normalization x=2t is essential. With S=T/2, (32) gives the integral in (35) as **2 I_(M_Q)(T/2)**. Since 2S=T, (31) proves the exact requested coefficient:

\[
 \boxed{\quad
 \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
 \ge\frac{k_1\kappa_Q}{U_0^2}
              \left(\int_1^2\phi(u)\,du\right)\log T
              +O_{Q,\phi}(1).
 \quad}
 \tag{36}
\]

Equivalently, the right side is at least its displayed logarithmic term minus a fixed constant C_(Q,φ) for all sufficiently large T. This makes the sign of the O-term unambiguous. The required lower threshold for T includes T/2>=P_Q^4 and the endpoint trimming threshold.

For every fixed finite Q, the positive coefficient in (36) rules out any uniform bounded upper bound on epsilon_Q(X)² over all sufficiently large centers. In particular it rules out a uniform all-center smallness claim at any fixed d,r margin in (7). It does **not** say epsilon is large at every center, give an exceptional-set estimate, or imply an upper zero exists. An all-real slice could have J_0=0 while this quadratic upper allowance is large. No Q=Q(T) substitution is permitted in (31) or (36): the actual primorial length, thresholds and Q-dependent constants have all been frozen before T tends to infinity. Growing-Q analysis is outside r1.

## 8. Controls, retained gain and remaining dependency

This note follows the [result index](../../../../../result-summaries/README.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [pattern index](../../../../../avoid/README.md), [target-classification rule](../../../../../avoid/01_restating_the_target.md), [shape/control rule](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped-exclusion rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The universal statement J_0=0 is already the inherited RH-type reformulation. Equation (6) is general analytic information; literal theta-source naming alone supplies none of the smallness needed in (7).

| Control family | Shared analytic information | Precise canonical premise absent here; consequence |
| --- | --- | --- |
| Positive-source Euler-factor controls | Positive even source, theta factor and generic strip/Jensen reasoning wherever the required analytic strip and nonzero center apply | Their transform has the additional factor 1+c cos(alpha z), so it is not the exact unchanged F_Q=qζM_Q. The canonical rough-prime product and its center bounds cannot simply be assigned to it. The additional factor or its zeros must be included. No generic Jensen inequality distinguishes it. |
| Weighted-square controls | Positive square-supported sources and the matched finite endpoint/moment constraints | The complete normalized infinite theta coefficients and full reflection are absent; the exact ξ/ζ identity used in (10),(23),(28) does not follow. Matching finite endpoint information does not supply it. |
| Reflected super-Gaussian control | Strict positivity, full even reflection and generic Fourier/Gram positivity | It lacks the integer-square theta arithmetic, hence the unchanged canonical ζ identity and the particular twisted-moment input. Reflection and positivity alone do not yield residual smallness. |
| Smooth shape and positive-primitive controls | Smooth positive even sources, strong decay and, for the strengthened construction, the listed primitive normalization/asymptotics | They lack the exact theta square expansion and canonical ζ identity; their shared shape and primitive data do not imply (7). The algebraic spectral asymptotics are not an exact source identity. |

These are failures of named exact premises, not claims that each control fails every coarse inequality derived from those premises. The universal Jensen step would remain valid for a control satisfying its analytic assumptions, and a genuine strip zero prevents that control's residual from meeting the relevant strict exclusion threshold. A finite box not containing its collision need not reject the control. The present canonical moment obstruction uses the actual ζ times the finite polynomial (29); it is not a negative theorem for all positive-source or arithmetic constructions.

The retained gain is an unconditional **paid acquisition theorem** for a normalized quadratic upper comparison: complex harmonic mean, uniform safe center, compact complete theta error, full remote tail, explicit denominator propagation and arbitrary-height limiting order. The decisive negative result is **fixed finite Q, uniform all-center quadratic smallness**. The consumer still needs an independently small compact residual plus the displayed error payments, or a different directly signed comparison. Exceptional centers, shrinking d, finite-height coverage, growing Q and nonzero Newman time remain outside the proved exclusion. The Gaussian hierarchy and other justified metrics remain available. No change of multiplier, mechanism or growing-Q target has been made, and no manuscript, shared-register, chat-history, numerical, commit or push action belongs to this executor return.
