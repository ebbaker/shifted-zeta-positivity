# B04 r5: paid quadratic acquisition, Euler obstructions, and the remaining sign

7 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Research lead: explicitly tool-selected **gpt-6-astra / ultra**; this records dispatch selection, not independent backend verification. Root model/effort unavailable. The proof executor is separately selected gpt-6.1-sol / ultra. No specialist-independence or novelty claim is made.

**Parent:** [frozen request16](16_TND_O_B04_R5_REQUEST_20261107.md), with [exact inputs16](16_TND_O_B04_R5_INPUTS_20261107.json). **Type B, revision 5.** This is a conceptual decision and derivation record, not a second status register. Register02 remains the sole live status source. The mathematical input hashes and sizes were checked before the comparison; the user-specified relocated Note27 and the working Note27 agreed byte for byte. Root subsequently changed the live E20 status in Register02; that administrative change is not a mathematical input replacement.

## 1. Decision and classification

The retained gain is a **paid quadratic comparison** for the exact time-zero Green potential. It converts a complete, pole-cancelled, finite-Euler-preconditioned boundary norm into the existing one-defect exclusion margin, with explicit compact-source error, remote-tail error and safe-center denominator payment. The norm can be acquired at arbitrary height by increasing the source cutoffs in a specified order. This is stronger than merely rewriting the unknown logarithmic sign, but it does **not** prove the norm small.

There is also a substantive obstruction: for every fixed finite Euler preconditioner the squared residual has a height average growing at least as a positive constant times log height. Thus this particular Jensen certificate cannot be uniformly small at all large centers, even if all actual zeros were real. A further, narrowly specified extension to growing Euler products of permissible Dirichlet-polynomial length is ready below; it is outside the already frozen E20 r1.

The second mechanism, stable continuation of safe Euler-line information toward the critical boundary, fails on an explicitly quantified enlarged control class. A positive even-source Euler-factor perturbation can approach the canonical safe-line data, together with any fixed number of derivatives and any fixed Dirichlet-coefficient prefix, while its added Green potential tends to infinity uniformly in the observation center. Its conductor, exact source coefficients and other canonical data change. Therefore this is an obstruction to a stability argument using only the stated partial data, not to a theorem using all fixed canonical data.

Exactly two mechanisms were compared. The single focused clarification is the joint limit in height, preconditioning length and source cutoff: preserve the one-defect budget after gamma normalization, and distinguish permissible uniform length asymptotics from a fixed-Q limit. The Gaussian hierarchy and other justified metrics remain available. No numerical campaign, finite zero check, nonzero-time Euler product or RH assumption is activated.

## 2. Inherited normalization and the actual missing estimate

Write

\[
s(z)=\tfrac12-\tfrac{i z}{2},\qquad a=\frac\pi8,\qquad
K(u)=\frac1{16\cosh(au)},\qquad
G(u,y)=\operatorname{atanh}\frac{\sin(ay)}{\cosh(au)}.
\]

The canonical normalization is \(H_0(z)=\xi(s(z))/8\). The sign of the imaginary coordinate is harmless here because the functional equation identifies the two usual arguments of xi. On the strip \(0\leq\operatorname{Im}z\leq8\), each of the two boundary measures with density \(K(x-X)\) has mass one half. Their union is a probability measure \(\mu_X\).

[Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) pays the complete product, boundary logarithms and remote tails and gives

\[
J_0(X)=\int\log|H_0|\,d\mu_X-\log|H_0(X+4i)|
      =\sum_{y_j>0}G(X-x_j,y_j).
\]

All relevant upper zeros satisfy \(0<y_j\leq1\). A zero with \(y_j\geq d>0\), \(|x_j-X|\leq r\), where \(d\leq1\), therefore contributes at least

\[
m(d,r)=\frac{\sin(a)d}{\cosh(ar)}.
\tag{2.1}
\]

The pole-corrected time-zero baseline is exactly

\[
J_0(X)=L(X)-P(X)+G(X,1),
\quad
P(X)=\sum_{n\geq2}\frac{\Lambda(n)}{\log n}
\frac{n^{-5/2}}{1+n^{-4}}
\cos\!\left(\frac X2\log n\right).
\tag{2.2}
\]

Here \(L(X)=\int K(x-X)\log|\zeta(1/2-ix/2)|\,dx\). The plus pole term is retained. The available lower bound \(L\geq P-G(X,1)\) does not exclude a defect. An upper bound below this baseline plus (2.1) is the absent signed information.

## 3. Mechanism 1: an independently acquirable quadratic comparison

For an integer \(Q\geq2\), put

\[
q(s)=\frac{s-1}{s},\quad
M_Q(s)=\prod_{p\leq Q}(1-p^{-s}),\quad
F_Q(z)=q(s(z))\zeta(s(z))M_Q(s(z)),\quad
c_Q(X)=F_Q(X+4i).
\tag{3.1}
\]

The zeta pole is removable in \(q\zeta\); the pole of q is outside the closed strip. Each finite Euler factor is zero-free there. In particular F has the same interior zeros as H. At the center, \(\operatorname{Re}s=5/2\), and the absolutely convergent rough Euler product gives uniform bounds

\[
c_0:=\frac35\frac{\zeta(5)}{\zeta(5/2)}
\leq |c_Q(X)|\leq U_0:=\zeta(5/2).
\tag{3.2}
\]

For the lower bound, \(|q|\geq3/5\) on that line and
\(\prod_{p>Q}(1+p^{-5/2})^{-1}\geq\zeta(5)/\zeta(5/2)\). For the upper bound, \(|q|\leq1\) and the corresponding product is bounded by \(\zeta(5/2)\). The lower margin is independent of X and Q.

The exact quotient is

\[
\frac{F_Q(z)}{H_0(z)}
=\frac{16\pi^{s(z)/2}M_Q(s(z))}{s(z)^2\Gamma(s(z)/2)}.
\tag{3.3}
\]

It is holomorphic and nonzero throughout the strip. Its logarithmic modulus has at most linear-plus-logarithmic horizontal growth. Consequently its harmonic strip mean is its center value and contributes no Green defect. Polynomial growth of F itself also gives the complete complex harmonic mean

\[
\int F_Q\,d\mu_X=c_Q(X).
\tag{3.4}
\]

These statements follow from the strip Poisson formula with vanishing remote vertical-boundary terms; the exponential decay of K dominates the indicated growth. The real-boundary zeros remain logarithmically integrable, as paid in Note25. There is no division by a critical-line zeta value.

Define

\[
\varepsilon_Q(X)^2
=\int\left|\frac{F_Q}{c_Q(X)}-1\right|^2d\mu_X.
\]

Equation (3.4) removes the cross term exactly, and concavity of log yields

\[
1+\varepsilon_Q(X)^2
=\int\left|\frac{F_Q}{c_Q(X)}\right|^2d\mu_X,
\qquad
J_0(X)\leq\frac12\log\bigl(1+\varepsilon_Q(X)^2\bigr).
\tag{3.5}
\]

Thus the independently acquired strict certificate

\[
\varepsilon_Q(X)^2<\exp(2m(d,r))-1
\tag{3.6}
\]

excludes the stated defect class. This is a sufficient comparison, not an equivalent reformulation of RH: absence of nonreal zeros does not force its quadratic Jensen gap to be small. Section 5 exhibits that distinction quantitatively.

## 4. Focused clarification: pay the source conversion before taking limits

Gamma division in (3.3) amplifies an absolute H error exponentially with horizontal height. Inserting a uniform absolute theta-truncation error on the entire normalized boundary can produce a nonintegrable squared majorant. It is therefore essential to split the acquisition into a compact interval and a direct canonical remote tail.

Let \(A_R\) consist of the portions \(|x-X|\leq R\) of both boundaries, and set

\[
B_Q(X,R)=\sup_{A_R}
\left|\frac{16\pi^{s/2}M_Q(s)}{s^2\Gamma(s/2)}\right|<\infty.
\]

The complete source estimates in [manuscript Section 2](../../manuscript/sections/02_source.tex) give, for a reflected arithmetic prefix n≤N integrated only over |u|≤U,

\[
\sup_{|\operatorname{Im}z|\leq8}|H_0(z)-H_{N,U}(z)|
\leq\delta_H(N,U;8)
:=\frac12\left[5C_2(N)J_{0,2}(0,8)
+B_0J_{0,2}^{>U}(0,8)\right].
\tag{4.1}
\]

Here \(C_2(N)=\sum_{n>N}n^4e^{-\pi(n^2-1)}\); the J notation and B0 are the inherited full-line majorants. A usable geometric estimate, for N≥1, is

\[
C_2(N)\leq
\frac{(N+1)^4e^{-\pi((N+1)^2-1)}}{1-16e^{-\pi(2N+3)}}.
\]

This finite reflected prefix is an approximation to an integral, not a replacement canonical source or an assertion of smooth matching at zero. No derivatives of that reflected prefix are used here. If \(\widehat\varepsilon_R\) is the norm on \(A_R\) formed from (3.3) with \(H_{N,U}\) and exact c, its compact error is at most \(B_Q\delta_H/c_0\).

For the remaining boundary, fractional-part continuation gives

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{u\}u^{-s-1}\,du
\quad(\operatorname{Re}s>0),
\]

with the pole understood by continuation. Therefore, with
\(C_Q=\prod_{p\leq Q}(1+p^{-1/2})\),

\[
|F_Q(x)|\leq C_Q(2+|x|),\qquad
|F_Q(x+8i)|\leq\zeta(9/2).
\tag{4.2}
\]

The first follows from \(|q\zeta|\leq1+|s-1|/\operatorname{Re}s\); the second uses the rough Euler product on \(\operatorname{Re}s=9/2\). Put B=2+|X|. The inequalities \(K(u)\leq e^{-a|u|}/8\) and \(|v-1|^2\leq2|v|^2+2\) give the explicit residual-tail bound

\[
\tau_Q(X,R)=\frac{e^{-aR}}{2a}\left\{
\frac{C_Q^2}{c_0^2}
\left[(B+R)^2+\frac{2(B+R)}a+\frac2{a^2}\right]
+\frac{\zeta(9/2)^2}{c_0^2}+2\right\}.
\tag{4.3}
\]

In particular,

\[
\varepsilon_Q(X)\leq
\widehat\varepsilon_R+\frac{B_Q\delta_H}{c_0}+\sqrt{\tau_Q}.
\tag{4.4}
\]

There is also an absolute center prescription. On \(s_c=5/2-iX/2\), use the logarithm of the rough Euler product, with the prime powers n≤V whose base prime exceeds Q. The discarded logarithm is bounded uniformly by
\(\eta_V=(2/3)V^{-3/2}\). If \(\widetilde c=q(s_c)\exp(\ell_V(s_c))\), then

\[
|c-\widetilde c|\leq\delta_c
:=U_0(e^{\eta_V}-1).
\tag{4.5}
\]

Choose \(\delta_c<c_0\). If the compact residual is instead acquired with \(\widetilde c\), call it \(\widetilde\varepsilon_R\). An explicit denominator payment is

\[
\varepsilon_Q(X)\leq
\left(1+\frac{\delta_c}{c_0}\right)\widetilde\varepsilon_R
+\frac{B_Q\delta_H}{c_0}+\frac{\delta_c}{c_0}+\sqrt{\tau_Q}.
\tag{4.6}
\]

Indeed, on the compact set write
\(F/c-1=(\widetilde c/c)(\widetilde F/\widetilde c-1)+(F-\widetilde F)/c+(\widetilde c-c)/c\), and use that its measure is at most one. Any later quadrature or rounding error must be added; no quadrature is performed in this cycle.

The usable order of limits is explicit. For each target X,Q,d,r and chosen error allowance smaller than the threshold in (3.6), first choose R to reduce (4.3), then choose N,U to reduce the compact amplification B times (4.1), then choose V for the denominator error. Each step terminates for every finite X,Q and every positive d. This gives acquisition at arbitrarily large height or source index, including any specified varying-parameter sequence. It asserts neither economical cost nor favorable residual size. For fixed Q and a fixed tolerance, the direct tail only requires logarithmic growth of R in |X|, with a slightly enlarged coefficient or iterated-log payment for the polynomial factor; the compact source accuracy becomes increasingly stringent because of gamma normalization. No uniform derivative-order claim is needed or obtained.

## 5. A genuine obstruction to the fixed finite Euler certificate

Let \(P_Q=\prod_{p\leq Q}p\). The actual polynomial length is this primorial, not Q:

\[
M_Q(s)=\sum_{d\mid P_Q}\mu(d)d^{-s}.
\]

The checked primary input is Bettin–Chandee–Radziwiłł, *The mean square of the product of ζ(s) with Dirichlet polynomials*, arXiv:1411.7764v1, Theorem 1. Its exact version, selected passages and limitations are recorded in [source-use15](../../references/15_TND_O_SIGNED_ACQUISITION_SOURCE_USE_20261107.md). The following specialization and residual consequence are derived here, not quoted as a theorem about Green potentials.

For a fixed nonzero smooth \(0\leq\varphi\leq1\) with support strictly inside (1,2), the theorem gives, for fixed Q,

\[
\int|\zeta(1/2+it)M_Q(1/2+it)|^2\varphi(t/T)\,dt
=\kappa_Q T\log T\int\varphi+O_{Q,\varphi}(T),
\tag{5.1}
\]

where

\[
\kappa_Q=\sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
=\prod_{p\leq Q}(1-p^{-1})>0.
\tag{5.2}
\]

The local gcd/lcm matrix has sum \(1-1/p-1/p+1/p=1-1/p\). A fixed polynomial may be zero-padded within a permissible fixed positive power of T; no growing-Q conclusion is hidden in (5.1).

On the lower boundary \(|q(1/2-it)|=1\). Apply (5.1) with the time variable t=x/2 and scale T/2, and convolve over centers X∈[T,2T]. The support of \(\varphi(x/T)\) lies inside [T+1,2T−1] for all sufficiently large T. Every such x receives at least

\[
k_1:=\int_{-1}^1K(u)\,du
=\frac1\pi\arctan\!\left(\sinh\frac\pi8\right)>0
\]

of center mass. Dropping the other nonnegative boundary contribution in (3.5) and using \(|c|\leq U_0\) gives

\[
\frac1T\int_T^{2T}\varepsilon_Q(X)^2\,dX
\geq\frac{k_1\kappa_Q}{U_0^2}
\left(\int\varphi\right)\log T+O_{Q,\varphi}(1).
\tag{5.3}
\]

This excludes uniform all-center bounded residuals for each fixed finite Q, hence excludes uniform all-center certification by (3.6). It does not exclude useful individual centers, conditioned local certificates, other multipliers, or the truth of RH. It is an obstruction to this particular sufficient certificate; ordinary real-zero fluctuations can already make it large.

### 5.1 Ready successor: a uniform growing-length obstruction

Root identified a useful extension within the same mechanism; its coefficient sign and elementary product bound were checked here. This is **not part of E20 r1** and must be frozen separately before execution or assessment.

Fix \(0<\theta<17/33\), put \(S=T/2\), and allow any integer Q=Q(T) satisfying \(P_Q\leq S^\theta\). Zero-pad to length \(S^\theta\). The BCR coefficient hypothesis is uniform because all coefficients have modulus at most one. Its full logarithmic main term has the exact factorization

\[
\sum_{d,e\mid P_Q}\frac{\mu(d)\mu(e)}{[d,e]}
\left[\log\frac{t(d,e)^2}{2\pi de}+2\gamma\right]
=\kappa_Q\left[\log\frac t{2\pi}+2\gamma
+2\sum_{p\leq Q}\frac{\log p}{p-1}\right].
\tag{5.4}
\]

The added prime sum is nonnegative. Locally its only nonzero logarithmic contributions are the two mixed divisibility cases, each \((-1/p)(-\log p)\); this verifies the sign.

No prime number theorem is needed to keep the main term large. For any finite prime set with product L, set \(y=\max(3,\log L)\). The factors with p≤y have product at least
\(\frac12\prod_{k=1}^{m}\frac{2k}{2k+1}\geq1/(2\sqrt y)\), with \(2m+1\) the largest odd integer ≤y. The displayed product inequality follows by induction from \(\prod_{k=1}^m2k/(2k+1)\geq(2m+1)^{-1/2}\). The remaining factors satisfy
\(\sum_{p>y}-\log(1-1/p)\leq2\log L/(y\log y)\leq2/\log3\). Hence

\[
\prod_{p\mid L}(1-p^{-1})
\geq\frac{e^{-2/\log3}}{2\sqrt{\max(3,\log L)}}.
\tag{5.5}
\]

For fixed θ and sufficiently large T, (5.5) implies
\(\kappa_Q\log S\geq[e^{-2/\log3}/(2\sqrt\theta)]\sqrt{\log S}\), uniformly over the admissible Q. Meanwhile BCR's error divided by S is

\[
O_{\theta,\varphi,\epsilon}
\left(S^{-17/20+\epsilon+33\theta/20}+S^{-2/3+\epsilon}\right)=o(1)
\tag{5.6}
\]

after choosing \(0<\epsilon<\min((17-33\theta)/20,2/3)\). Equations (5.4)–(5.6), with the same convolution as above, therefore support the uniform target

\[
\frac1T\int_T^{2T}\varepsilon_{Q(T)}(X)^2\,dX
\geq c_{\theta,\varphi}\sqrt{\log(T/2)}-O_{\theta,\varphi}(1),
\quad c_{\theta,\varphi}>0.
\tag{5.7}
\]

The polynomial is fixed across each height average; (5.7) is not a statement about selecting a different Q at each center X. An explicit allowed constant is any positive number smaller than
\(k_1e^{-2/\log3}(\int\varphi)/(2U_0^2\sqrt\theta)\). This strengthens the fixed-Q failure to growing finite Euler products throughout the proven polynomial-length regime. It supplies no claim for longer products, arbitrary mollifiers, adaptive per-center choices or conditional local estimates. A further successor must change or condition the residual estimate in a way that escapes this exact failure class; merely allowing Q to grow slowly is not enough.

## 6. Mechanism 2: quantified instability of safe-line continuation

Fix \(0<d<1\), \(\beta=(1+d)/2\), and let p tend to infinity through primes. Consider the existing Euler-factor control shape

\[
D_p(s)=(1+p^{\beta-s})(1+p^{1-\beta-s})
=1+(p^\beta+p^{1-\beta})p^{-s}+p^{1-2s}.
\tag{6.1}
\]

On every fixed safe half-plane \(\operatorname{Re}s\geq\sigma_0>1\), uniformly in imaginary part,

\[
|D_p(s)-1|\leq2p^{\beta-\sigma_0}+p^{1-2\sigma_0}\longrightarrow0,
\tag{6.2}
\]

and for each fixed integer j≥1,

\[
|\partial_s^j(D_p-1)|
\leq(\log p)^j\left[2p^{\beta-\sigma_0}+2^jp^{1-2\sigma_0}\right]
\longrightarrow0.
\tag{6.3}
\]

The bounded safe-half-plane derivatives of zeta imply the same convergence for any fixed jet of \(\zeta D_p-\zeta\). Its Dirichlet coefficients at every n<p equal those of zeta. Thus any prescribed finite coefficient prefix and every local Euler factor except the altered prime can also be retained as p grows.

The completion reveals exactly what is hidden by (6.2):

\[
\frac{p^{s-1/2}D_p(s)}{2\cosh(d\log p/2)}
=1+c_p\cos(a_pz),\qquad
a_p=\frac{\log p}{2},\quad c_p=\operatorname{sech}\frac{d\log p}{2}.
\tag{6.4}
\]

Multiplying H0 by this factor replaces its source by
\(\Phi(u)+\frac{c_p}{2}[\Phi(u+a_p)+\Phi(u-a_p)]\), which is positive, even and has all fixed exponential moments. The factor adds zeros

\[
z=x_k\pm id,\qquad x_k=\frac{2(2k+1)\pi}{\log p},\quad k\in\mathbb Z,
\tag{6.5}
\]

with spacing \(\ell_p=4\pi/\log p\). For each fixed p these already reach arbitrarily large real heights. The added Green potential is

\[
\Delta J_p(X)=\sum_{k\in\mathbb Z}G(X-x_k,d).
\tag{6.6}
\]

The sum is absolutely convergent. The strip formula applies directly to the periodic multiplier, whose boundary logs and center log are bounded; its zeros are the simple lattice (6.5). The scalar and conductor multiplier in (6.4) contribute only harmonic logarithms.

This instability is quantitative. Differentiation under the integral, followed by v=sinh(au), gives

\[
\frac d{dd}\int_{\mathbb R}G(u,d)\,du
=\cos(ad)\int_{\mathbb R}\frac{dv}{v^2+\cos^2(ad)}=\pi,
\quad
\int_{\mathbb R}G(u,d)\,du=\pi d.
\]

Consequently the exact period mean is

\[
\frac1{\ell_p}\int_0^{\ell_p}\Delta J_p(X)\,dX
=\frac{d\log p}{4}.
\tag{6.7}
\]

Moreover G as a function of u is positive, even, decreasing on u>0 and has total variation \(2G(0,d)\). Comparing one lattice sample with the integral on each length-\(\ell_p\) cell yields, uniformly in X,

\[
\left|\Delta J_p(X)-\frac{d\log p}{4}\right|
\leq2\operatorname{atanh}(\sin(ad)).
\tag{6.8}
\]

Thus the entire added potential diverges uniformly while the safe-line errors and every fixed derivative error tend to zero. A weaker direct one-defect count gives
\(\Delta J_p(X)\geq[r\log p/(2\pi)-1]_+m(d,r)\), which independently preserves the same local margin.

The rejected method class is now precise: no continuity modulus tending to zero can control this Green potential from only a fixed safe-half-plane error, any finite jet there and any fixed coefficient prefix across this enlarged family. Exact analytic continuation remains unique; the example concerns stability from the stated incomplete data. Moving the safe line changes (6.2), and suppressing the added factor there requires the explicit separation \((\sigma_0-\beta)\log p\) to remain large. This does not prove that a canonical moving-line theorem is impossible.

These controls do **not** preserve the literal canonical theta coefficients or conductor: \(p^{s-1/2}\) is the completion change associated with conductor p². The zeta pole residue is also changed by \(D_p(1)\); dividing by that value repairs the residue but changes the leading Dirichlet coefficient. The local factor is non-tempered, and zero-count/source constants are not uniform in p. Therefore (6.8) cannot be promoted to a counterexample to a bound that actually uses those fixed canonical restrictions. It shows that citing the complete source or a safe Euler product without a quantitative use of the distinguishing restrictions does not acquire the missing sign.

## 7. Collision-control audit and retained alternatives

The controls were checked analytically against their actual premises, using result-summaries12–13 and the requested avoid entries. No finite control computation was substituted for this audit.

| Control family | Shared information | Premise not supplied to a canonical signed acquisition |
|---|---|---|
| Positive-source Euler factors | Positive even reflected source, moments, heat orbit, explicit nonreal zeros; the generic strip/Jensen comparison with their own bounds | Literal theta coefficients, conductor and canonical residue/normalization; uniform source/count constants; the moment calculation for exactly ζM_Q |
| Weighted-square, finite-tail and finite-prime-orbit controls | Arithmetic-looking pieces or selected finite identities | Complete canonical reflection and all coefficients; finite pieces cannot inherit the global theta/zeta quotient or canonical strip constants merely by resemblance |
| Reflected super-Gaussian, smooth strong-log-concavity and positive-primitive controls | Smooth positive even sources and strong fixed-order decay/moment estimates | The unchanged theta series and ordinary canonical Euler data; polynomial growth after the particular gamma normalization must be proved anew |
| Atomic fixed-event and finite-profile controls | Local collision patterns or selected finite observables | The complete smooth theta source and eventual-profile assumptions; atomic sources are not the prepared canonical L² source |
| Polynomial quadratic/cubic heat controls | Local zero splitting and the sign diagnostics | Canonical source/arithmetic; any strip comparison uses their own analytic field and growth rather than ζM_Q |
| Variable-kernel/counterkernel and smooth-density/two-channel controls | Selected positivity or density identities | The actual cosine transform, scalar canonical field and full Newman heat relation required by the consumer |
| RH-conditional close positive sources | Close source data and certain completed-function constraints | Ordinary unchanged Dirichlet arithmetic; no RH-conditional control is promoted to an unconditional canonical theorem |

The Jensen step is intentionally general: a valid control with a nonreal zero must have a residual large enough to satisfy \(\varepsilon^2\geq e^{2J}-1\). Its generality creates no false exclusion. The new arithmetic obstruction uses the literal finite Euler polynomial for zeta, and the growing-length proposal must use the uniform primary theorem rather than borrow constants from fixed Q.

[Note24](../../notes/24_TND_O_E15_GAUSSIAN_LAGUERRE_HIERARCHY_20261107.md) remains an alternative. It supplies complete finite-order quadratic source expressions and the local order-m event signal at level m−2. The shrinking-variance choice needed to read that negative signal conflicts with the transport cancellation schedule; neither the present Green comparison nor the Euler instability resolves that issue. No high-order uniform estimate is claimed, and the Gaussian hierarchy has not been discarded or treated as obligatory.

## 8. Exact execution contract and consumer boundary

Root has frozen and dispatched [E20 r1 request36](../../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_REQUEST_20261107.md), with its own hashed input receipt. The executor owns only Note28 and return36. Its exact task is: prove (3.2)–(3.6), pay (4.1)–(4.6) with conservative repairs if needed, and establish the fixed-Q consequence (5.3) from the checked BCR theorem. Domain is λ=0, Q finite, arbitrary real X and positive finite cutoffs. One bounded repair may address constants, normalization, denominator propagation or the smooth moment cutoff. A changed multiplier or scientific mechanism returns to B. This decision does not pre-accept the executor's work or replace the separate E21 assessment.

The ready successor, after r1 returns, is precisely Section 5.1: same q, F, residual and kernel; fixed θ<17/33, Q allowed to depend on the averaging scale T with primorial length at most (T/2)^θ; uniform BCR main term and error, elementary product lower bound, then the averaged lower bound (5.7). No new numerical work or source model is needed. The assessment must verify uniform constants, actual polynomial length, the logarithmic correction sign and the x=2t scaling. It may not claim a per-center adaptive obstruction or anything beyond the theorem's length range.

Mechanism 2 has the explicit derivation (6.1)–(6.8) as a scoped B obstruction. It is not a separately accepted E theorem or a new research-note branch. If the eventual assessment includes it, that inclusion must be explicit; otherwise its classification remains a checked conceptual derivation here.

For a localized exclusion consumer, the still-missing input is an independently proved upper bound for the acquired residual at the required centers, with the entire right side of (4.6) strictly below \(\sqrt{e^{2m(d,r)}-1}\). The present all-center moment obstruction specifies where that input cannot come from. A useful replacement could restrict or condition centers, change the preconditioner class, or control the logarithm with canonical cancellation; none of those estimates has been obtained here. Shrinking d, increasing coverage r, λ≠0 and unbounded derivative order remain separate requirements. There is no unconditional nonreal-zero exclusion in this decision.

## 9. Source-use and provenance appendix

The complete current manuscript was read, including all twenty section inputs and the integrated Gaussian/Green sections. The frozen starting set also included [Note27](../../notes/27_TND_O_NEXT_BRAINSTORM_SIGNED_CANONICAL_ESTIMATES_20261107.md), Notes24–25, [Decision15](15_TND_O_B04_R4_SIGNED_METRIC_COMPARISON_20261107.md), Overview02, sole Register02, Reviews09–11 and the build record. The frozen JSON identifies exact bytes; this appendix does not replace that receipt.

The root instructions and controls read were AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, tools/CHAT_HISTORY.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md, result-summaries/README.md, clusters12–13, avoid/README.md and avoid01,02,05,06,07,10,11,17. Their operative mathematical constraints are reflected in the unchanged-source distinctions, bounded two-mechanism scope, explicit failure classes and absence of numerical promotion above. Root owns chat recording; no transcript was reconstructed or fabricated by this lead.

The only new external theorem used is the primary BCR v1 Theorem 1, selected passages checked by lead and root and registered by root in [source-use15](../../references/15_TND_O_SIGNED_ACQUISITION_SOURCE_USE_20261107.md) and the separate signed-acquisition bibliography. Version-pinned metadata: [arXiv:1411.7764v1](https://arxiv.org/abs/1411.7764v1); checked [primary converted text](https://arxiv.org/html/1411.7764v1), §1, equations (1.1)–(1.2), Theorem 1 and its stated error. The metadata dates v1 to 28 November 2014; the converted text's anomalous August 2026 date is recorded in source-use15. No later version, full-paper proof audit or retained PDF is claimed. The PDF fetches failed and no third-party large file was placed in Git.

All additional displayed specializations, elementary continuation/tail estimates, gcd products and control-lattice calculations are derivations in this decision or fixed execution targets. Status at writing: E20 r1 dispatched, not yet assessed; the growing-length successor is ready for its own frozen contract; no manuscript change is authorized by this record alone.
