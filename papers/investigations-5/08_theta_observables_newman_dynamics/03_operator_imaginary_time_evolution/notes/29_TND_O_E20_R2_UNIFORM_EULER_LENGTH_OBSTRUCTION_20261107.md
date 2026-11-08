# E20 r2: uniform obstruction for finite Euler products of growing length

7 November 2026. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Executor dispatch selected **gpt-6.1-sol, reasoning effort ultra**; conceptual selection: B04 r5, Astra/ultra. These are actual supplied dispatch records, not independent backend verification. Root configuration is unavailable. No numerical experiment, novelty claim or specialist-independence claim is made.

**Status: proved in-note, awaiting E21 assessment.** For every fixed 0<theta<17/33, the actual squared quadratic residual has a center average bounded below by an explicit positive multiple of sqrt(log(T/2)), minus a Q-independent constant, uniformly for the finite Euler products whose primorial length is at most (T/2)^theta. The product may vary between averaging intervals; it is fixed throughout each interval. This strengthens the fixed-Q obstruction in [Note28](28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md) without using its Q-dependent asymptotic constant.

The separately frozen [request37](../research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_REQUEST_20261107.md) executes the route selected in [Decision17 §5.1](../brainstorm/notes/17_TND_O_B04_R5_SIGNED_ACQUISITION_DECISION_20261107.md). All **56 sources** in [inputs37](../research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_INPUTS_20261107.json) matched their frozen byte counts and SHA-256 hashes before derivation. The appended r2 use in source-use15 and the new Register02 version belong to this freeze, not the earlier r1 freeze. Exact input/output fingerprints and final verification are in [return37](../research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_RETURN_20261107.json). Note28 and return36 are preserved byte-identically.

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| TND-O-E21 | E — execution | Sol6.1/ultra | Actual r1/r2 returns and completed Decision17 | Claim-level assessment of both comparison/obstruction packages and the separately derived mechanism2 |

## 1. Exact uniform statement and inherited normalization

Retain only Newman time lambda=0 and the exact definitions

\[
 s(z)=\frac12-\frac{iz}{2},\quad q(s)=\frac{s-1}{s},\quad
 M_Q(s)=\prod_{p\le Q}(1-p^{-s}),\quad
 P_Q=\prod_{p\le Q}p,
\]
\[
 F_Q(z)=q(s(z))\zeta(s(z))M_Q(s(z)),\quad
 c_Q(X)=F_Q(X+4i),\quad
 \epsilon_Q(X)^2=\int\left|\frac{F_Q}{c_Q(X)}-1\right|^2d\mu_X.
 \tag{1}
\]

Here mu_X is the probability measure on y=0 and y=8, with density K(x-X) on each line, where

\[
 a=\frac\pi8,\quad K(u)=\frac1{16\cosh(au)},\quad
 U_0=\zeta(5/2),\quad
 k_1=\int_{-1}^{1}K(u)\,du
      =\frac1\pi\arctan(\sinh(\pi/8))>0.
 \tag{2}
\]

Note28 proves, uniformly in every finite Q and X, the nonzero center bound |c_Q(X)|<=U_0 and the exact variance identity

\[
 1+\epsilon_Q(X)^2
   =\int|F_Q/c_Q(X)|^2d\mu_X.
 \tag{3}
\]

Its positive lower center bound, harmonic-mean proof, pole payment, real-zero logarithmic integrability and full acquisition theorem remain unchanged. No new approximation is needed for the present moment obstruction.

Fix theta and phi once and for all, with

\[
 0<\theta<17/33,\qquad
 0\ne\phi\in C_c^\infty((1,2)),\qquad 0\le\phi\le1,
\qquad A_\phi=\int_1^2\phi(u)\,du>0.
 \tag{4}
\]

Set S=T/2. For each T allow any integer Q>=2 satisfying P_Q<=S^theta, with **the same Q for every center X in [T,2T]**. We prove

\[
 \boxed{\quad
 \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
 \ge c_{\theta,\phi}\sqrt{\log(T/2)}-C_{\theta,\phi},\qquad
 c_{\theta,\phi}=
 \frac{k_1 e^{-2/\log3}A_\phi}{4U_0^2\sqrt\theta}>0.
 \quad}
 \tag{5}
\]

The existence constant C_(theta,phi) and the sufficiently large T threshold are independent of Q. Section6 states their full allowed dependence and distinguishes explicit elementary constants from the unspecified constants imported from the primary theorem.

## 2. Apply the primary moment theorem afresh

The executor re-opened the [primary text of arXiv:1411.7764v1](https://arxiv.org/html/1411.7764v1), Bettin–Chandee–Radziwiłł, *The mean square of the product of ζ(s) with Dirichlet polynomials*, §1, definition(1.1) and Theorem1, on 7 November 2026. The same pinned statement, version metadata and retrieval limitation are recorded in [source-use15](../references/15_TND_O_SIGNED_ACQUISITION_SOURCE_USE_20261107.md). This checks the imported statement, coefficient hypothesis and error, not the paper's full proof; no PDF possession or full reading is claimed.

Use its arbitrary-Dirichlet-polynomial theorem with length N=S^theta and

\[
 a_n=\begin{cases}\mu(n),&n\mid P_Q,\\0,&\text{otherwise},\end{cases}
\qquad
 \sum_{n\le N}a_n n^{-s}=M_Q(s).
 \tag{6}
\]

The actual nonzero polynomial length is **P_Q**, not Q. All its divisors fit inside N, and the remaining coefficients are zero. The theorem assumes a_n<<n^varepsilon. Its uniform coefficient-bound convention allows the O-constant to depend on fixed constants bounding the coefficient class, not separately on the support of each admissible polynomial. Here, for every auxiliary nu>0,

\[
 |a_n|\le1\le n^\nu
\]

with the same bound constant **one for all S,Q,n**. Thus there is no drifting coefficient-bound constant or hidden Q parameter. We use the theorem directly for this normalized bounded coefficient class, rather than substituting Q(T) into any fixed-Q consequence.

Write

\[
 I_Q(S)=\int_{\mathbb R}
    |\zeta(\tfrac12+it)M_Q(\tfrac12+it)|^2\phi(t/S)\,dt.
\]

The checked theorem then gives

\[
 \begin{split}
 I_Q(S)={}&\sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
       \int_{\mathbb R}
       \left[\log\frac{t(d,e)^2}{2\pi de}+2\gamma\right]
                              \phi(t/S)\,dt+E_Q(S),\\
 |E_Q(S)|\le{}&C_{\rm BCR}
       \left(S^{3/20+\varepsilon+33\theta/20}
                                      +S^{1/3+\varepsilon}\right).
 \end{split}
 \tag{7}
\]

The integral is supported in positive t. The constants C_BCR and the starting threshold S_BCR depend only on theta, phi, the chosen varepsilon and the common normalized coefficient bound. Neither depends on Q. The theorem's stated O-constant is not given numerically; we do not extract an effective numerical value or a computable starting threshold here. No sharp-cutoff theorem is imported.

## 3. Exact logarithmic gcd correction and its sign

Put

\[
 \kappa_Q=\sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
          =\prod_{p\le Q}(1-1/p)>0.
 \tag{8}
\]

For a prime p, let alpha,beta in {0,1} indicate its divisibility in d,e. Its local weight is

\[
 w_p(\alpha,\beta)=(-1)^{\alpha+\beta}p^{-\max(\alpha,\beta)}.
\]

The four local values are 1,-1/p,-1/p,1/p, whose sum is 1-1/p. The local logarithm from log((d,e)²/(de)) is

\[
 [2\min(\alpha,\beta)-\alpha-\beta]\log p.
\]

It vanishes in the two equal-divisibility cases and equals -log p in each mixed case. Each mixed product is therefore **(-1/p)(-log p)=+log p/p**. Summing over the other primes gives

\[
 \sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
                 \log\frac{(d,e)^2}{de}
   =2\kappa_Q\sum_{p\le Q}\frac{\log p}{p-1}.
 \tag{9}
\]

Consequently the full main-term summand in (7) factors exactly as

\[
 \boxed{\quad
 \sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
       \left[\log\frac{t(d,e)^2}{2\pi de}+2\gamma\right]
 =\kappa_Q\left[\log\frac t{2\pi}+2\gamma
               +2\sum_{p\le Q}\frac{\log p}{p-1}\right].
 \quad}
 \tag{10}
\]

The added prime sum is nonnegative. Bounding its summands separately in absolute value would lose the useful uniform sign; dropping the exact positive correction is valid.

Let

\[
 b_\phi=\int_1^2\left[\log\frac u{2\pi}+2\gamma\right]\phi(u)\,du,
\qquad B_\phi=\max(0,-b_\phi).
 \tag{11}
\]

Substitute t=Su into (7),(10). Since 0<kappa_Q<=1, the possibly negative constant satisfies kappa_Q b_phi>=-B_phi. Hence

\[
 \frac{I_Q(S)}S\ge
       \kappa_Q A_\phi\log S-B_\phi
        -C_{\rm BCR}\left(
           S^{-17/20+\varepsilon+33\theta/20}
                                      +S^{-2/3+\varepsilon}\right).
 \tag{12}
\]

No Q-dependent constant from the main term has been discarded into an O_Q term.

## 4. Elementary lower bound for the Euler density

We prove a bound for **any finite set of distinct primes**, not just an initial segment. Let its product be L and let kappa be the corresponding product of 1-1/p. Set y=max(3,log L). Separate primes at y.

The product over selected p<=y is at least half the product over all odd integers 3,5,...,2m+1<=y:

\[
 \prod_{\substack{p\mid L\\p\le y}}(1-1/p)
 \ge\frac12\prod_{j=1}^{m}\frac{2j}{2j+1},
\qquad 2m+1\le y<2m+3.
 \tag{13}
\]

Adding factors between zero and one can only decrease a product; the factor 1/2 is conservative whether or not 2 is selected. For m=0 the product is one. Inductively,

\[
 \prod_{j=1}^{m}\frac{2j}{2j+1}\ge\frac1{\sqrt{2m+1}},
 \tag{14}
\]

because the step from m to m+1 reduces to

\[
 (2m+2)^2\ge(2m+1)(2m+3),
\]

whose difference is one. Thus (13) is at least 1/(2sqrt(y)).

For the selected primes p>y, use

\[
 -\log(1-1/p)\le\frac{1/p}{1-1/p}\le\frac2p.
\]

If their number is h, then h log y<=log L, and their reciprocal sum is at most h/y. Therefore

\[
 \sum_{\substack{p\mid L\\p>y}}-\log(1-1/p)
 \le\frac{2\log L}{y\log y}\le\frac2{\log3}.
 \tag{15}
\]

Combining (13)-(15) proves the requested elementary estimate

\[
 \boxed{\quad
 \kappa\ge\frac{e^{-2/\log3}}
                 {2\sqrt{\max(3,\log L)}}.
 \quad}
 \tag{16}
\]

No prime-counting estimate or prime number theorem is used. In the present regime log P_Q<=theta log S. Once log S>=3/theta, both 3 and log P_Q are at most theta log S, and (16) yields uniformly

\[
 \kappa_Q\log S\ge
      \frac{e^{-2/\log3}}{2\sqrt\theta}\sqrt{\log S}.
 \tag{17}
\]

## 5. Uniform remainder and the complete center convolution

Choose explicitly

\[
 A_\theta=\frac{17-33\theta}{20}>0,\qquad
 \varepsilon_\theta=\frac12\min(A_\theta,2/3),
\qquad
 \rho_1=A_\theta-\varepsilon_\theta>0,\quad
 \rho_2=2/3-\varepsilon_\theta>0.
 \tag{18}
\]

Then the remainder divided by S in (12) is at most
C_BCR(S^(-rho_1)+S^(-rho_2)), tends to zero uniformly over admissible Q, and is at most 2C_BCR for S>=1. Equations (12),(17) consequently give

\[
 \frac{I_Q(S)}S\ge
  \frac{e^{-2/\log3}A_\phi}{2\sqrt\theta}\sqrt{\log S}
                  -B_\phi-2C_{\rm BCR}.
 \tag{19}
\]

The passage to the actual complete-boundary residual uses (3), not a sharp moment cutoff. Since |c_Q(X)|<=U_0, dropping only the nonnegative top-boundary term gives

\[
 \epsilon_Q(X)^2\ge
      U_0^{-2}\int_{\mathbb R}K(x-X)|F_Q(x)|^2\,dx-1.
 \tag{20}
\]

At the lower boundary |q(1/2-ix/2)|=1, and conjugation gives

\[
 |F_Q(x)|^2
   =|\zeta(\tfrac12+ix/2)M_Q(\tfrac12+ix/2)|^2.
 \tag{21}
\]

Let

\[
 \delta_\phi=\operatorname{dist}(\operatorname{supp}\phi,\{1,2\})>0,
\qquad w_T(x)=\int_T^{2T}K(x-X)\,dX.
\]

For x in [T+1,2T-1], w_T(x)>=k_1 because the centers [x-1,x+1] lie inside the averaging interval. If T>=1/delta_phi, every x in the support of phi(x/T) lies in this trimmed interval. Thus, for all x,

\[
 w_T(x)\ge k_1\phi(x/T).
 \tag{22}
\]

Integrate (20) in X and use Tonelli on the **full nonnegative convolution**. Since the same polynomial M_Q is used for all centers, (21)-(22) imply

\[
 \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
 \ge\frac{k_1}{TU_0^2}\int_{\mathbb R}|F_Q(x)|^2\phi(x/T)\,dx-1
 =\frac{k_1}{U_0^2}\frac{I_Q(S)}S-1.
 \tag{23}
\]

The last equality pays x=2t exactly: dx=2dt, phi(x/T)=phi(t/S), and T=2S. Omitting this change of scale would alter the coefficient. No remote boundary contribution is approximated or omitted with a negative sign.

## 6. Constants, threshold and conclusion

With varepsilon=varepsilon_theta in C_BCR, define

\[
 C_{\theta,\phi}=1+\frac{k_1}{U_0^2}
                                (B_\phi+2C_{\rm BCR}),
 \tag{24}
\]

and take

\[
 T\ge T_{\theta,\phi}:=
 2\max\left\{1,S_{\rm BCR},e^{3/\theta},\frac1{2\delta_\phi}\right\}.
 \tag{25}
\]

The elementary entries of this threshold are explicit. C_BCR and S_BCR are the unspecified existence constants supplied by the primary mean-square theorem for the uniformly bounded coefficient class; no numerical values or effective implementation are extracted. We do not assert that the source proves them intrinsically ineffective: this note simply does not establish quantitative effectivity for those imported constants. All dependence is on theta, phi and the explicit choice varepsilon_theta; none is on Q.

Combining (19),(23) actually gives

\[
 \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
 \ge \frac{k_1 e^{-2/\log3}A_\phi}{2U_0^2\sqrt\theta}
                  \sqrt{\log(T/2)}-C_{\theta,\phi}.
 \tag{26}
\]

The conservative coefficient c_(theta,phi) in (5) is half this proved coefficient, so (5) follows with the same constant and threshold. This holds simultaneously for all admissible Q at each sufficiently large T, equivalently after taking the infimum of the averaged residual over those Q. It is a uniform family of fresh theorem applications, not a substitution into Note28's O_(Q,phi)(1).

## 7. Scope, controls and consumer assessment

The class excluded is now larger than in r1: no choice Q(T) with P_(Q(T))<=(T/2)^theta, fixed on each averaging interval and fixed theta<17/33, can give a uniformly bounded residual at **all** sufficiently high centers in that interval. Its actual squared residual average diverges. In particular this class cannot deliver the uniform all-center smallness required by Note28's quadratic sufficient Green certificate at a fixed positive defect margin.

This is a lower bound on epsilon², **not on J_0**, and it is compatible with an all-real zero set. It asserts neither failure at each individual center nor an exceptional-set bound. Adaptive per-center choices Q(X), longer products, arbitrary mollifiers, defect-conditioned centers, replacements of the localization width and signed logarithmic cancellation remain outside this failure class. No RH assertion, nonreal-zero existence assertion, collision or nonzero-time Euler arithmetic follows. The Gaussian hierarchy remains available.

The control screen is the one in Note28 §8 and Decision17: the analytic Jensen comparison is shared information; positive-source Euler-factor controls have an extra factor and fail the exact unchanged F_Q=qζM_Q premise; weighted-square controls fail the complete normalized infinite theta coefficients/full reflection; reflected super-Gaussian and smooth/primitive controls fail the exact theta square arithmetic. The uniform BCR specialization here depends specifically on ζ times the polynomial (6) with coefficients bounded by one. It does not turn any shared positivity, reflection or shape estimate into a discriminating small residual. No finite experiment is used to test these controls.

This scope follows the [result index](../../../../../result-summaries/README.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [pattern index](../../../../../avoid/README.md), [target-classification rule](../../../../../avoid/01_restating_the_target.md), [shape/control rule](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped-exclusion rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The retained gain is the uniform growing-length obstruction with its elementary coefficient lower bound and exact positive logarithmic correction. The consumer still needs an independently acquired signed comparison or a separately selected residual method outside this exact class. Simply allowing this finite Euler cutoff to grow within the proved polynomial-length regime does not close the absent small-residual estimate.

No bounded mathematical correction was needed. This executor created only Note29 and return37, preserving the frozen r1 artifacts. Root owns shared files and chat capture. There were no subagents, numerical computations, manuscript edits, commits or pushes in this r2 execution.
