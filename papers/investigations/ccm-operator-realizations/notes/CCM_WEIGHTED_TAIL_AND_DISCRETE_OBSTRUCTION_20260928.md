# The full weighted tail and the remaining discrete obstruction

28 September 2026. CCM continuation, round 8. Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed. These are analytic working proofs with parallel same-model checks, not independent human refereeing or formal verification. Sonin residuals remain deferred.

## 1. Result and change of target

The full weighted jump form from [round 7](CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md) controls escape to infinity at its sharp threshold. Its even self-adjoint operator J satisfies, unconditionally,

\[
J\ge0,\qquad \ker J=\operatorname{span}\{1\},\qquad
\inf\sigma_{\rm ess}(J)=\tfrac14.
\tag{1}
\]

The point 1/4 is itself an eigenvalue of infinite multiplicity. All spectrum strictly below it is discrete, of finite multiplicity, and can accumulate only at 1/4. In particular there is an unconditional, unspecified positive spectral gap above the constants. The sharp value of that gap is not proved.

Consequently the remaining RH target is exactly

\[
\boxed{\ \sigma(J)\cap(0,1/4)=\varnothing.\ }
\tag{2}
\]

This is a whole-line theorem, not an extrapolation from finite L. It removes a specific obstruction: normalized functions supported progressively farther out cannot have energy bounded a fixed amount below 1/4. It does not exclude a family of subthreshold eigenvalues approaching 1/4, or prove the CCM determinant limit.

There are two complementary derivations. The [prime-return note](CCM_PRIME_RETURN_AND_EXTERIOR_COERCIVITY_20260928.md) identifies how prime jumps back to the central region recover the threshold, using an unconditional prime number theorem. The [operator note](CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md) obtains the spectral theorem and a stronger exterior error from exact pole cancellation and weighted translations; that proof does not require a prime number theorem. Section 5 below makes the remaining eigenvalue-count problem precise.

## 2. Definitions and normalization

Keep the literal kernel used by the preceding programs:

\[
k(x)=e^{x/2}\sum_{n\ge1}\frac\pi2(ne^x)^2
\bigl(2\pi(ne^x)^2-3\bigr)e^{-\pi(ne^x)^2},
\quad \widehat k=\Xi/4.
\]

It is even, strictly positive, and superexponentially decreasing. Set

\[
m(x)=k(x)\cosh(x/2),\quad d\mu=m(x)dx,
\quad M=\int d\mu=\tfrac18,\quad s=2M=\tfrac14.
\]

The even Hilbert space is \(L^2(\mu)^+\). Close the positive form below from even compact smooth functions:

\[
\begin{split}
\mathcal E_\Gamma(u)&=\tfrac12\iint
\frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}k(x)k(y)
|u(x)-u(y)|^2dxdy,\\
\mathcal E_p(u)&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int k(x)k(x+\log n)|u(x+\log n)-u(x)|^2dx,\\
\mathcal E&=\mathcal E_\Gamma+\mathcal E_p.
\end{split}\tag{3}
\]

J is its associated operator. Constants belong to the closed domain and have zero energy. Round 7 established the exact even identity

\[
Q(ku)=\mathcal E(u)-s\|u-\bar u\|_\mu^2,
\qquad \bar u=M^{-1}\int u\,d\mu.
\tag{4}
\]

Compact even Weil positivity is equivalent to RH. Since multiplication by the smooth positive k is a bijection of the compact smooth even tests, (4), form closure, and removal of the constant mode identify (2) with RH. No RH assumption enters (1).

## 3. The exact operator exposes the controlled tail

Use the unitary map and bounded positive multiplier

\[
(Uu)(x)=\sqrt{m(x)}u(x),\qquad
a(x)=\sqrt{k(x)/\cosh(x/2)}.
\]

Thus \(ku=aUu\). Write

\[
g(t)=\Re\psi(1/4+it/2)-\log\pi,
\qquad g(t)\ge g(0)>-6,
\]

and let \(T_\ell v(x)=v(x+\ell)\). On the compact core, the transformed operator has the form identity

\[
\boxed{\quad H:=UJU^{-1}=sI+A_0-K,\quad
A_0=M_a(g(D)+6)M_a,\quad
K=6M_{a^2}+P_a,\quad}
\tag{5}
\]

\[
P_a=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_a(T_{\log n}+T_{-\log n})M_a.
\tag{6}
\]

A_0 means the positive closed form \(\|(g(D)+6)^{1/2}av\|_2^2\), with the domain and core justified in the operator note. It is not a product identity asserted on arbitrary L2 vectors. K is bounded and self-adjoint; it need not be positive.

The rank-one pole form for even f is \(2|\int f(x)\cosh(x/2)dx|^2\). On putting f=ku this cancels exactly the mean term in (4), leaving (5). The multiplier g and prime shifts are the explicit formula in [CCM, Section 3](https://arxiv.org/html/2511.22755v1#S3); the weighted operator and ensuing conclusions are deductions here.

For any fixed \(0<c<\pi/2\), the theta bound gives a finite constant C such that

\[
a(x)\le C e^{-c e^{2|x|}}.
\tag{7}
\]

Since \(e^{2|x|}+e^{2|x+\log n|}\ge2n\),

\[
\|M_aT_{\log n}M_a\|
=\sup_x a(x)a(x+\log n)\le C^2e^{-2cn}.
\tag{8}
\]

The prime series is therefore absolutely convergent in operator norm using only \(\Lambda(n)\le\log n\). For a v supported on \(|x|\ge R\), both endpoints of every surviving quadratic-form prime term are outside. Splitting the exponent between the bounds \(2e^{2R}\) and \(2n\) gives

\[
\langle v,Hv\rangle\ge(s-\eta_R)\|v\|_2^2,
\qquad
\eta_R=6C^2e^{-2ce^{2R}}
+2C^2e^{-ce^{2R}}\sum_{n\ge2}\frac{\log n}{\sqrt n}e^{-cn}
\longrightarrow0.
\tag{9}
\]

This holds uniformly over the exterior form domain, including oscillatory or extremely narrow tests. It is not restricted to a family of trial profiles. The constants have not been optimized or enclosed numerically.

Local form compactness follows from the logarithmic growth of g and the positive lower bound for a on each compact interval. Multiplication by a bounded function vanishing at infinity is consequently compact from the A_0 form domain to L2. Equation (8) then shows that K is relatively form compact for A_0, by truncating the norm-convergent shift sum. Thus the essential spectrum of H is that of \(sI+A_0\), with lower bound s. The already established independent eigenfunctions

\[
u_j=k^{(2j)}/k-4^{-j},\qquad Ju_j=s u_j,
\quad j\ge1,
\tag{10}
\]

put s in the essential spectrum and prove equality of the lower edge. No description of the rest of the essential spectrum is claimed. Strict positivity of the gamma jump kernel implies that zero energy forces u to be constant almost everywhere, proving the simple zero mode and hence the positive, unspecified gap.

## 4. Why full prime return matters, and what can be truncated

For x>T, keep only prime jumps from x to \(y=x-\log n\in[-T,T]\). Their outgoing rate relative to dmu is

\[
B_T(x)=\frac{1}{\cosh(x/2)}
\sum_{|x-\log n|\le T}\frac{\Lambda(n)}{\sqrt n}k(x-\log n).
\tag{11}
\]

There is no extra factor of two: each undirected prime edge is already counted once in (3). Replacing the prime measure by dt gives the exact continuous comparison

\[
B_T^{\rm cont}(x)=\frac{2e^x}{e^x+1}
\int_{-T}^T e^{-y/2}k(y)dy.
\tag{12}
\]

The unconditional PNT makes (11) converge uniformly for x beyond a growing lower endpoint to \(2\int_{-T}^T e^{-y/2}k(y)dy\). Letting T grow recovers 2M=s. The support-restricted lower estimate uses only jumps to a region where u vanishes, so no cancellation or assumed smoothness of the tested u is needed. The supporting note supplies endpoint conventions and an error bound from \(\psi(t)-t\). An explicit unconditional input is available from [Johnston–Yang](https://arxiv.org/abs/2204.01980v2).

This explains the round-7 finite-prime zero-gap theorem: to return from x to a fixed central interval requires prime powers of size comparable to \(e^x\). A fixed finite family cannot do that as x tends to infinity.

There is nevertheless a useful, distinct approximation in (5): truncate **only the weighted off-diagonal sum** P_a while retaining the exact s and gamma term. It has the rigorous global norm error

\[
\|P_a-P_{a,\le P}\|
\le2C^2\sum_{n>P}\frac{\log n}{\sqrt n}e^{-2cn}.
\tag{13}
\]

This is not the positive jump truncation \(\mathcal E_\Gamma+\mathcal E_{p,\le P}\). The latter also deletes the long-jump diagonal contributions, and has gap zero. Equation (5) has already combined the complete diagonal, gamma, and pole cancellation through the exact kernel k. Retaining that identity is essential. The earlier finite-prime obstruction is unchanged.

A bounded [prime-return diagnostic](../reviews/CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md) checks (11)–(12), normalization, and a finite Stieltjes identity, with no Weil matrices or zeta-zero list. Its finite samples illustrate the mechanism; the uniform theorem comes from the analytic estimates.

## 5. A compact eigenvalue-count target at each fixed distance below threshold

Equation (5) gives a concrete next object. For \(0<\lambda<s\), define

\[
B_\lambda=A_0+(s-\lambda)I,
\qquad
\mathcal T_\lambda=B_\lambda^{-1/2}K B_\lambda^{-1/2}.
\tag{14}
\]

B_lambda is strictly positive and T_lambda is compact self-adjoint, because K is relatively form compact. A form congruence gives

\[
H-\lambda=B_\lambda^{1/2}(I-\mathcal T_\lambda)B_\lambda^{1/2},
\qquad
N(H<\lambda)=n(\mathcal T_\lambda>1).
\tag{15}
\]

The counts include multiplicity and use strict inequalities. This is the Birman–Schwinger inertia principle for signed K; it does not assume that K or T_lambda is positive. A proof follows directly by mapping negative form subspaces through the invertible map B_lambda^(1/2) between its form domain and L2 and applying min–max.

The normalized constant mode of J maps to

\[
v_0=\sqrt m/\sqrt M,\qquad Hv_0=0.
\]

For every lambda in (0,s), this guarantees at least one eigenvalue of T_lambda above 1. It need not be v_0 itself as an eigenvector of T_lambda. The exact remaining statement is

\[
\boxed{\quad \mathrm{RH}\iff
n(\mathcal T_\lambda>1)=1
\quad\text{for every }0<\lambda<1/4.\quad}
\tag{16}
\]

In equivalent language, the even operator H−s must have negative index exactly one. Its known negative eigenvector v_0 has eigenvalue −s. On the orthogonal complement, the absence of any negative direction is the missing assertion.

For a fixed depth delta=s−lambda>0, an operator-norm approximation K_N obeys

\[
\|\mathcal T_\lambda-
B_\lambda^{-1/2}K_NB_\lambda^{-1/2}\|
\le\|K-K_N\|/\delta.
\tag{17}
\]

Thus the arithmetic norm tail (13) is now globally controlled, rather than tied to increasing finite support. Spatial and frequency approximation still require their own verified bounds. If an approximate eigenvalue lies near 1, the norm error alone does not decide its count. This round implements no eigenvalue-count certificate.

The fixed-depth problem is compact and has only finitely many obstructions. Passing delta to zero is the substantive next task: (17) deteriorates, and the infinite threshold eigenspace prevents casually replacing the limit by a finite-dimensional separation assumption. The theorem does not provide a single compact central interval that captures every hypothetical eigenvalue arbitrarily close to s. Local compactness and exterior coercivity are sufficient below each fixed depth, not a uniform threshold estimate. The operator note strengthens this to a quantitative eigenfunction estimate: for a normalized eigenfunction with eigenvalue at most s−delta, its mass outside [−R−1,R+1] is at most e_R/(delta−d_R), whenever d_R<delta. Both explicit errors d_R and e_R tend to zero superexponentially; the denominator retains the threshold dependence.

## 6. Research decision and limits

The next useful analytic direction is a **one-negative-direction theorem for (5)**, or an equivalent bound on the second eigenvalue of (14) uniformly as lambda increases to 1/4. A workable approach must preserve the signed prime translations and account for the full threshold eigenspace. Proving only that each fixed derivative trial space is positive, or inspecting finitely many values of lambda, does not establish (16).

The new leverage is specific: whole-line tail control and compactness below a known essential edge are now available. A proposed central comparison can use (9), (13), and (17) to expose precisely which estimates need to be uniform. The remaining arithmetic inequality still has RH strength. No sign estimate for that central problem has been obtained here, and the original CCM ground-profile and determinant-convergence requirements remain stronger unresolved goals.

Files for this round include the two supporting proofs, the [critical review](../reviews/CCM_WEIGHTED_TAIL_REVIEW_20260928.md), and small [reproduction records](../numerics/weighted-tail-20260928/README.md). No new manuscript snapshot, commit, or finite-L matrix sweep was created.
