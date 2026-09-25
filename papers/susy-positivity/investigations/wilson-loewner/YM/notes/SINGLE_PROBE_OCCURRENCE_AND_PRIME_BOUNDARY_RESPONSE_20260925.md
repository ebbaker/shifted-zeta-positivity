# One detecting probe, the full current spectrum, and the prime-cutoff boundary response

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred. Baseline commit: `f8b8622fbd687bd152dd40dcc0c4bbd4576008e5`.

Status: new model-assisted derivations with proofs and floating controls, awaiting independent review. No implication from YM existence and mass gap to RH has been established. The fixed four-dimensional model and state are unchanged.

## 1. What this continuation establishes

The [preceding note](NATIVE_RECENTERING_AND_GAPPED_POSITIVE_COMPLETION_20260925.md) recovered a genuine source under the electric–Wilson current, with ordinary L2 pairing, and excluded a fixed closable norm completion. This continuation tests that same current as the carrier of **one** complete signed response. It also reduces the remaining positive-source problem to one precisely specified stationary correlation.

The main results are:

- An explicit compactly supported pole-neutral test detects **every** nontrivial zero, without using a zero list. Its translated Weil response is bounded, or even merely tempered, if and only if RH holds. Its exponential growth rate measures the greatest departure of a zero from the critical line.
- The **full** weighted electric–Wilson current in the actual interacting boundary space is unitarily equivalent to translation on a real line with a transverse multiplicity space. Its spectrum is purely absolutely continuous. Thus it cannot carry the detecting response as a matrix element between any two Hilbert vectors. This goes beyond the earlier class-space and finite-order-seed exclusions.
- The sharp prime cutoff produces an explicit response at distances near plus and minus log A. Its ordinary-L2 norm is at least a nonzero constant times the square root of A. This holds even for exactly pole-neutral tests and uses only the prime number theorem, not RH. A local counterterm at the original source cannot cancel this moving response.
- If an independently specified stationary family of **actual** YM vectors has the one detecting correlation, spectral filtering constructs the complete global smooth-test source law in that same physical sector. The filtering domain and continuity are proved below; the physical occurrence of the stationary family is not.

Only the electric-current candidate is concretely tested here. The last item is a sufficient occurrence theorem, not a claim that another observable with its hypotheses has been found. There is no new physical model, thermal state, prescribed zero spectrum, or assigned digamma insertion.

## 2. State, domains, and the signed response already available

Keep the SU(2) Wilson slab with spatial size 6 cubed, time slices -2 through 2, beta 8/5 and theta angle zero. On the central-slice compact link manifold M,

\[
d\nu=w\,dm,\qquad w=Z^{-1}\Omega^2>0,\qquad
\mathcal H=L^2_{\rm cov}(M,\nu;\operatorname{End}\mathbb C^2).
\tag{1}
\]

The inner product uses trace divided by 2. The class marginal of the fixed four-link plaquette P is \(\rho(g)dg\), with rho smooth and strictly positive. No continuum vacuum or physical Hamiltonian is identified with this finite-state construction.

Use \(\mathcal D=C_c^\infty(\mathbb R)\), \(U_tf(x)=f(x-t)\), \(\widehat f(\tau)=\int e^{-i\tau x}f(x)dx\), and \(T=-\partial_x^2+1/4\). The pole-neutral space is \(\mathcal D^0=T\mathcal D\).

Retain the audited character operations \(V_a\chi_n=\chi_{an}\) and their **actual** weighted adjoints. In odd-circle coordinates,

\[
C_a^{*\rho}=\rho^{-1}L_a\rho,\qquad
L_a h(\theta)=a^{-1}\sum_{j=0}^{a-1}h((\theta+2\pi j)/a).
\tag{2}
\]

The archimedean insertion \(C_\rho\) is the existing compressed, density-compensated electric/angle operator, not the full electric Laplacian:

\[
C_\rho=\mathscr W_\rho^{-1}
\left(\log D+B^*M_{\log(\theta/(2\pi))}B\right)\mathscr W_\rho,
\quad B=\partial_\theta D^{-1},\quad D=\sqrt{-\partial_\theta^2{}_{\rm Dir}}.
\tag{3}
\]

Here \(\mathscr W_\rho F=\sqrt{2/\pi}\sqrt\rho\sin\theta F\). The finite span of \(\phi_n=\rho^{-1/2}\chi_n\) is in its dense symmetric domain. Define on that core

\[
K_A=C_\rho-\sum_{2\le a\le A}\Lambda(a)(V_a+V_a^{*\nu}),
\qquad F_Rf=\sum_{n\ge1}n^{-1/2}f(\log n-R)\phi_n.
\tag{4}
\]

For finite R and A these are actual class-space vectors/operators in the fixed state; symmetry suffices and no self-adjoint realization of the whole sum is assumed. The [archimedean calculation](ELECTRIC_PARITY_ARCHIMEDEAN_RESPONSE_AND_PHASE_OBSTRUCTION_20260925.md) and its [critical audit](../reviews/ELECTRIC_PARITY_RESPONSE_CRITICAL_REVIEW_20260925.md) give

\[
\lim_{R\to\infty}\langle F_Rf,K_AF_Rg\rangle_\nu
=\langle f,L_Ag\rangle_2,
\quad
L_A=m_+(P_x)-\sum_{2\le a\le A}\frac{\Lambda(a)}{\sqrt a}
 (U_{\log a}+U_{-\log a}),
\tag{5}
\]

where \(P_x=-i\partial_x\) and
\(m_+(\tau)=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi\).
In particular \(L_Af\in L^2\) for f smooth and compactly supported. The multiplier includes the contact and the logarithmic high-frequency growth established there.

Taking A to infinity **after** R gives Q on \(\mathcal D^0\). At fixed compact test pair, the limiting prime sum is finite. No uniform joint cutoff/packet limit for the compensated packets is inferred. These are signed inserted responses; (5) is not an OS norm identity.

## 3. An explicit test with no hidden missed zeros

Let \(a_j=2^{-j}\), and let b be the probability density of the absolutely convergent sum of independent variables uniformly distributed on \([-a_j,a_j]\). Equivalently its bilateral Laplace transform is

\[
B(z)=\int e^{zx}b(x)dx
=\prod_{j=1}^{\infty}\frac{\sinh(2^{-j}z)}{2^{-j}z}.
\tag{6}
\]

The removable factors at zero are set to 1. This specifies b without arithmetic data.

**Lemma 1 (detecting probe).** The functions

\[
h_*(x)=\frac{e^x b(x)}{B(1)},\qquad f_*=Th_*
\tag{7}
\]

are real smooth functions supported in \([-1,1]\), with \(f_*\in\mathcal D^0\). Write

\[
F(z)=\int e^{zx}f_*(x)dx
=(1/4-z^2)\frac{B(1+z)}{B(1)}.
\tag{8}
\]

Then F has no zeros in the open strip \(|\operatorname{Re}z|<1/2\), and \(\widehat f_*(\tau)=F(-i\tau)\ne0\) for every real tau.

**Proof.** The sum defining b has support in [-1,1]. Its characteristic function is the product in (6) on the imaginary axis. Bounding any fixed k factors by \(\min(1,(a_j|\tau|)^{-1})\), and the rest by 1, gives decay faster than every power. Fourier inversion therefore gives a C-infinity density, supported in [-1,1]. In particular all its derivatives vanish at the support endpoints.

The product converges locally uniformly in z, since the deviations of the tail factors from 1 are summable. Every factor has its nonzero zeros on the imaginary axis. Away from that axis all factors are nonzero and the summable product tail is nonzero, so B has no zeros there. In the stated strip, \(\operatorname{Re}(1+z)>1/2\). Formula (8) and integration by parts now prove every assertion. The two polynomial zeros at z=plus or minus 1/2 impose pole neutrality; they are not nontrivial zeta zeros after centering. \(\square\)

The exponential tilt is essential to this convenient construction: the untilted even density has real Fourier zeros and could miss a chosen critical-line ordinate. No such exception remains in (7).

## 4. One correlation determines whether zeros leave the line

Set

\[
k(t)=\langle f_*,U_tf_*\rangle_2,\qquad
C_*(t)=Q(f_*,U_tf_*).
\tag{9}
\]

The real function k is even, smooth, and supported in [-2,2]. The geometric definition, containing no zero list, is

\[
C_*(t)=\frac1{2\pi}\int m_+(\tau)|\widehat f_*(\tau)|^2e^{-it\tau}d\tau
-\sum_{a\ge2}\frac{\Lambda(a)}{\sqrt a}
 \{k(t+\log a)+k(t-\log a)\}.
\tag{10}
\]

The prime sum is locally finite in t. For t>2 only primes and prime powers with \(e^{t-2}\le a\le e^{t+2}\) occur. The archimedean part outside that interval of overlapping supports is

\[
C_{*,\infty}(t)
=-\sum_{j\ge1}e^{-(2j+1/2)t}F(2j+1/2)F(-2j-1/2),\qquad t>2.
\tag{11}
\]

Indeed expand \(e^{-r/2}/(1-e^{-2r})\) in exponentials in the off-diagonal kernel. The j=0 coefficient is zero by pole neutrality. The contact contributes only when source supports overlap. Thus (10), rather than the off-diagonal kernel alone, retains the completed normalization.

Let \(\lambda_\rho=\rho-1/2\), where rho now denotes a nontrivial zeta zero, counted with multiplicity, and put

\[
c(\lambda)=F(\lambda)F(-\lambda).
\tag{12}
\]

The unconditioned explicit formula gives

\[
C_*(t)=\sum_\rho c(\lambda_\rho)e^{\lambda_\rho t}.
\tag{13}
\]

One initially obtains the opposite exponent with one Fourier convention; reindexing \(\rho\mapsto1-\rho\) gives (13). This is valid **without RH**. For a real test, the complex-frequency pairing is the product in (12), not a squared modulus off the line. Lemma 1 shows that every coefficient at a nontrivial zero is nonzero. The rapid vertical decay of F, uniform in closed bounded real strips, and the zero-counting bound give absolute convergence, locally uniformly with all t derivatives.

The explicit formula and sign conventions are checked against [Connes–Consani, Appendix B, (148)–(153)](https://arxiv.org/html/2006.13771v1#A2). Only that arithmetic identity is used from this source here. Zero location and symmetry are recorded in [DLMF §25.10](https://dlmf.nist.gov/25.10). The counting bound with multiplicity is proved in [Elkies, *Vertical distribution of zeros*, pp. 1–3](https://people.math.harvard.edu/~elkies/M229.15/zeta2.pdf); only polynomial growth is needed here.

**Theorem 2 (one-probe boundedness and growth criterion).** The following are equivalent:

1. RH.
2. \(C_*\) is bounded on the real line.
3. \(C_*\), as the distribution defined by its smooth function, is tempered.
4. For every epsilon>0, \(|C_*(t)|\le C_\epsilon e^{\epsilon t}\) for t>=0.

More precisely,

\[
\limsup_{t\to+\infty}\frac{\log(1+|C_*(t)|)}{t}
=\sup_\rho |\operatorname{Re}\rho-1/2|.
\tag{14}
\]

**Proof.** Under RH, \(\lambda=i\gamma\) and

\[
C_*(t)=\sum_\gamma m_\gamma|\widehat f_*(\gamma)|^2e^{-i\gamma t}.
\tag{15}
\]

The sign can again be reversed by conjugate-zero symmetry. The weights are strictly positive and summable. This proves boundedness, temperedness, and subexponential growth.

Conversely, for Re z>1/2 the one-sided Laplace transform is

\[
\int_0^\infty e^{-zt}C_*(t)dt
=\sum_\rho\frac{c(\lambda_\rho)}{z-\lambda_\rho}.
\tag{16}
\]

The right side is a meromorphic function on the plane. The series is normally convergent off its discrete poles, and its residue at a zero of multiplicity m is \(m c(\lambda)\ne0\). A subexponential bound makes the left side holomorphic throughout Re z>0. A tempered C has the same consequence: restrict to the positive half-line with a smooth cutoff and a compact correction at zero, and take the Laplace transform of this tempered distribution supported in [0,infinity). The exponential damping defines a holomorphic transform for Re z>0, agreeing with the displayed integral in its original half-plane. Hence there can be no zero with Re lambda>0. The functional equation excludes Re lambda<0 too. Boundedness is a special case.

For (14), let b be the supremum on the right; symmetry makes it the supremum of Re lambda as well. Absolute summability of c gives \(|C_*(t)|\le(\sum|c|)e^{bt}\) for t>=0. If the left side were less than b, a bound with an exponent strictly between them would make (16) holomorphic to the left of at least one of its nonzero-residue poles, a contradiction. If b=0 the upper bound and the nonnegativity introduced by log(1+|C|) suffice. \(\square\)

This supplies an exact relationship to a plausible physical regularity requirement, but **does not establish that requirement from OS temperedness**. The variable t here is logarithmic character scale, not spacetime separation. Moreover (10) is a limit of signed inserted pairings, not an established Schwinger function. Assuming its temperedness without a physical derivation would, by this theorem, assume a new RH-equivalent arithmetic assertion.

**Corollary 3 (nondecay, unconditionally).** \(C_*\notin C_0(\mathbb R)\).

**Proof.** Membership in C0 would imply boundedness, hence RH by Theorem 2. Under that consequence, (15) is an absolutely convergent almost-periodic series. Distinct frequencies and uniform convergence give

\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|C_*(t)|^2dt
=\sum_{\gamma\ {
m distinct}}
\bigl(m_\gamma|\widehat f_*(\gamma)|^2\bigr)^2>0.
\tag{17}
\]

The sum is nonzero since zeta has nontrivial zeros and the probe misses none. A C0 function would have zero mean square. This contradiction proves the claim without assuming RH. \(\square\)

## 5. The entire interacting electric current has continuous spectrum

Retain \(X=\tfrac12\operatorname{tr}P=\cos\theta\), \(\ell=4\), and the full weighted current

\[
A_\nu=\frac{i}{2\ell}[E_\nu,X]
=-i\left(Y+\tfrac12\operatorname{div}_\nu Y\right),
\quad Y=\ell^{-1}\nabla X,
\quad \mathscr U_t=e^{itA_\nu}.
\tag{18}
\]

Its domain is defined by the complete smooth weighted flow, as in the recentering note. In particular it is not a replacement of the full current by its class compression.

**Theorem 4 (global current spectrum).** In the full physical boundary space, there is a transverse covariant Hilbert space \(\mathcal K\) and a unitary identification

\[
\mathcal H\simeq L^2(\mathbb R,dr;\mathcal K),\qquad
\mathscr U_t H(r)=H(r-t),\qquad A_\nu=i\partial_r,
\tag{19}
\]

with the usual Hilbert-valued H1 domain. In particular the current has purely absolutely continuous spectrum, and

\[
\langle\xi,\mathscr U_t\eta\rangle_\nu\longrightarrow0
\quad\text{as }|t|\to\infty
\quad(\xi,\eta\in\mathcal H).
\tag{20}
\]

**Proof.** Off the measure-zero sets P=plus or minus I, set
\(r=\log\tan(\theta/2)\). The exact full-flow relation \(Y\theta=-\sin\theta\) gives \(Yr=-1\). The compact regular hypersurface \(\Sigma=\{\theta=\pi/2\}\) is crossed once by every remaining flow line. Thus

\[
(r,z)\longmapsto\Phi_{-r}z
\]

is a smooth global coordinate map from \(\mathbb R\times\Sigma\) onto this full-measure part of M. This assertion includes the other link coordinates; it is not only a coordinate on the plaquette angle.

Choose a smooth gauge-invariant positive reference measure sigma on Sigma. Write the pulled-back actual measure as \(b_\nu(r,z)dr\,d\sigma(z)\). Multiplying the pulled-back vector by \(b_\nu^{1/2}\) is a unitary to the product measure. The weighted flow Jacobian is exactly the ratio \(b_\nu(r-t,z)/b_\nu(r,z)\), so this multiplication removes it and proves (19). Gauge covariance restricts the transverse space to a closed subspace \(\mathcal K\); the gauge action preserves r and commutes with the flow, so it does not change the translation factor. The discarded sets have Haar, hence nu, measure zero.

Hilbert-valued Fourier transformation in r turns the generator into multiplication by minus the Fourier variable. Every vector spectral measure is absolutely continuous. The Fourier integrand for any matrix coefficient is in L1 by Cauchy–Schwarz, proving (20). \(\square\)

The previous strong recentering map obeys the additional exact relation

\[
J_{\rm rec}U_t=\mathscr U_{-t}J_{\rm rec}.
\tag{21}
\]

Indeed \(S_RU_tf=S_{R+t}f\); apply the previously proved strong limits to \(\mathscr U_RS_{R+t}f\). This is consistent with \(A_\nu J_{\rm rec}f=J_{\rm rec}P_xf\) on smooth tests. No nonidentity phase norm is recovered by this observation; the earlier winding defect remains unchanged.

**Consequences.** There are no \(\xi,\eta\in\mathcal H\) with
\(\langle\xi,\mathscr U_t\eta\rangle=C_*(t)\) for all t, by Corollary 3. This holds in the full fixed-state space, not just in the one-plaquette class sector. It excludes a current-covariant generalized source with the Weil pairing even if the source is only continuous on smooth tests and is not closable in input L2.

It also excludes the common signed-insertion attempt
\(C_*(t)=\langle v,K\mathscr U_t v\rangle\) when the expression is defined and \(v\in\operatorname{Dom}K^*\), since its left entry can be replaced by the Hilbert vector \(K^*v\). This last statement is explicitly a domain restriction: a genuinely distributional left entry need not have the decay in (20). Such a distribution is not thereby an OS Hilbert source.

## 6. A quantitative boundary response from the prime cutoff

The failure of bounded inserted vectors can also be seen directly, before any question about RH. This section applies to every nonzero real \(h\in C_c^\infty((-1,1))\), or smooth h supported in [-1,1] and flat at its endpoints, with f=Th. In particular it applies to the detecting probe.

Put L=log A and define the positive-prime-shift part

\[
P_A f(x)=\sum_{2\le a\le A}\frac{\Lambda(a)}{\sqrt a}
\{f(x-\log a)+f(x+\log a)\}.
\tag{22}
\]

**Theorem 5 (moving boundary profiles).** As A tends to infinity, uniformly for s in [-1,1],

\[
\begin{aligned}
A^{-1/2}P_Af(L+s)&\longrightarrow h'(s)+\tfrac12h(s),\\
A^{-1/2}P_Af(-L+s)&\longrightarrow-h'(s)+\tfrac12h(s).
\end{aligned}
\tag{23}
\]

For the completed finite-cutoff signed operator \(L_A=m_+(P_x)-P_A\), the two limits have the opposite signs. Therefore

\[
\liminf_{A\to\infty}A^{-1}\|L_Af\|_2^2
\ \ge\ 2\|h'\|_2^2+\tfrac12\|h\|_2^2>0.
\tag{24}
\]

**Proof.** The prime number theorem in von Mangoldt form is
\(\Psi(x)=\sum_{a\le x}\Lambda(a)=x+o(x)\).
For the positive edge, only the first shift survives for sufficiently large A. After putting a=Aq, the normalized sum is a Stieltjes integral against \(A^{-1}d\Psi(Aq)\), with integrand \(q^{-1/2}f(s-\log q)\) and q<=1. On the whole s range its relevant q lie in the fixed interval [exp(-2),1]. The PNT and integration by parts give uniform convergence to Lebesgue measure there. Boundary values at q=1 are included; there is no assertion that the sharp cutoff has disappeared. Consequently the limit is

\[
\int_0^1q^{-1/2}f(s-\log q)dq
=e^{s/2}\int_s^1e^{-u/2}f(u)du
=h'(s)+\tfrac12h(s).
\tag{25}
\]

The last equality follows by differentiating
\(e^{-u/2}(h'(u)+h(u)/2)\).
At the negative edge the same calculation gives

\[
\int_0^1q^{-1/2}f(s+\log q)dq
=e^{-s/2}\int_{-1}^s e^{u/2}f(u)du
=-h'(s)+\tfrac12h(s).
\tag{26}
\]

The archimedean operator on f has, away from its original support, the exponentially decaying kernel already derived. Pole neutrality cancels its first exponential; its tails are \(O(e^{-5|x|/2})\). Its local contact is absent at the moving edges. Thus it vanishes after the normalization in (23). The two edge intervals eventually are disjoint. Uniform convergence on each gives their limiting squared norms, and their sum is
\(\|h'+h/2\|^2+\|-h'+h/2\|^2=2\|h'\|^2+\|h\|^2/2\), proving (24). \(\square\)

The PNT used here is unconditional; see [DLMF §27.12](https://dlmf.nist.gov/27.12). Partial summation converts prime counting to the sum of log p; higher prime powers contribute at most O(square root of x times (log x) squared), giving the stated von Mangoldt form. No conjectural error estimate is required.

**What is cancelled and what is not.** On a complete continuum prime average, the exponential moment of f is zero. Cutting that average at A leaves the partial primitives in (25) and (26). The result is a moving response of height of order square root of A, rather than a leftover scalar multiple of f at the original support. Any counterterm supported in a fixed compact neighborhood of that support, including any local differential counterterm with A-dependent coefficients, leaves (24) unchanged. A nonlocal moving subtraction could affect it, but would require its own independent physical definition and proof of the completed pairing/positivity. This theorem is specifically for the sharp cutoff and does not assert that every possible regulator has the same edge profile.

**Actual-state consequence.** Let

\[
v_R=\mathscr U_RF_Rf,\qquad
q_{R,A}=\mathscr U_RK_AF_Rf\in\mathcal H.
\tag{27}
\]

For every test g, symmetry, (5), and the strong source limit give

\[
\langle q_{R,A},\mathscr U_RF_Rg\rangle_\nu
\longrightarrow\langle L_Af,g\rangle_2,
\qquad
\liminf_{R\to\infty}\|q_{R,A}\|_\nu\ge\|L_Af\|_2.
\tag{28}
\]

To obtain the inequality, apply Cauchy–Schwarz for each fixed g, take the lower limit, and then take the supremum over the dense smooth tests of unit L2 norm. Combining with (24) proves

\[
\liminf_{A\to\infty}\frac1A
\left(\liminf_{R\to\infty}\|q_{R,A}\|_\nu\right)^2
\ge 2\|h'\|_2^2+\tfrac12\|h\|_2^2.
\tag{29}
\]

This is a physical Hilbert-norm lower bound on the actual finite inserted vectors in the stated iterated limit. It does not replace rho by Haar, discard winding phases, or interchange the limits. It explains why strong occurrence of the uninserted source alone does not make the signed completion a vector response.

More generally, if a cofinal prescription A(R) had both bounded q-vectors and convergence of all its translated responses to C*, a weakly convergent subsequence and \(\mathscr U_RF_{R+t}f_*\to\mathscr U_{-t}J_{\rm rec}f_*\) would express C* as a finite-vector current coefficient. Theorem 4 and Corollary 3 exclude this. This is a conditional exclusion of such a prescription, not a claim that its joint response convergence is known.

## 7. A sufficient one-probe occurrence theorem

The current candidate fails, but Lemma 1 provides a smaller exact target for a different independently specified physical source mechanism. It also removes a domain concern from the generalized-source route.

**Theorem 6 (one actual correlation supplies every smooth-test source).** In the fixed positive physical Hilbert space, suppose there is an independently specified strongly continuous unitary action \(V(t)=e^{-itG}\) on a closed admissible source sector, and an actual vector v there, such that

\[
\langle v,V(t)v\rangle_{\rm OS}=C_*(t)
\quad\text{for every real }t.
\tag{30}
\]

Assume that limits in this sector are admissible in the same physical completion as before. Then the prescription

\[
Jg=\left(\frac{\widehat g}{\widehat f_*}\right)(G)v,
\qquad g\in\mathcal D^0,
\tag{31}
\]

is well defined, continuous on the global smooth-test space, and satisfies

\[
\langle Jf,Jg\rangle_{\rm OS}=Q(f,g),\qquad
Jf_*=v,\qquad J U_t=V(t)J.
\tag{32}
\]

A separately native G is optional: it suffices instead to obtain a continuous stationary family \(v_t\) of actual vectors with \(\langle v_s,v_t\rangle=C_*(t-s)\); translations on its closed span induce V and v=v0.

**Proof.** An actual unitary matrix coefficient is bounded. Thus (30) implies RH by Theorem 2; this is a consequence, not an input to selecting v or G. Uniqueness of the Fourier transform of finite measures, applied to the spectral measure of v and (15), gives

\[
d\mu_v(\tau)=\sum_\gamma m_\gamma
|\widehat f_*(\gamma)|^2\delta_\gamma(d\tau).
\tag{33}
\]

This spectrum is derived from the physical identity, not assigned in advance. Lemma 1 makes the denominator of (31) nonzero at every real point. Its growth need not be polynomial. The spectral domain test nevertheless is exactly

\[
\int\left|\frac{\widehat g(\tau)}{\widehat f_*(\tau)}\right|^2d\mu_v(\tau)
=\sum_\gamma m_\gamma|\widehat g(\gamma)|^2<\infty.
\tag{34}
\]

Rapid Fourier decay of every compactly supported smooth g and polynomial zero counting prove finiteness. Thus (31) is the strong limit of bounded spectral filters applied to the existing physical vector v. Polarization and the explicit formula prove (32).

For a fixed support interval I, integration by parts bounds \(|\widehat g(\tau)|\) by \(C_I p_k(g)(1+|\tau|)^{-k}\), where \(p_k\) is a finite smooth-test seminorm. Choosing k large enough makes its squared bound summable against the zero count, proving continuity on each \(\mathcal D_I\), hence on \(\mathcal D^0\) with its usual test topology. Fourier translation gives the covariance assertion.

For the family formulation, stationarity makes the shift of finite linear combinations of the v_t isometric and well defined, including null relations. Continuity extends it to a strongly continuous unitary group on the closed span. The preceding argument applies. \(\square\)

This theorem verifies the **analytic reduction**, including the crucial division domain and physical Hilbert completion. It does **not** verify (30) for a new YM observable. Claiming (30) solely because its target kernel is positive would reverse the argument. Nor does the theorem guarantee extra requirements such as bounded local-observable representatives or a uniform electric Sobolev bound on Jg. If these stronger notions of admissibility are imposed, they require additional preparation estimates.

## 8. Role of OS axioms, mass gap, and the remaining direction

All finite-state results above need the already specified positive boundary representation, its exact current geometry, the earlier signed packet identity, and the stated classical arithmetic facts. They do not need a physical mass gap. The prime boundary estimate uses the PNT; the full-current spectral theorem does not use number theory at all.

In an assumed continuum YM theory, OS reconstruction and a gap remain allowed. They do not identify arithmetic t with spacetime time or distance. If an additional physical clustering theorem makes a proposed connected correlation tend to zero along its chosen parameter, Corollary 3 excludes its equality with C*. Likewise a physical Hamiltonian bounded below cannot supply the required symmetric two-sided source spectrum with a vacuum-to-vector interpretation. These statements do not exclude nongeometric source relations or discrete source sectors.

The useful next task is now quite specific: derive the scalar identity (30) for one independently specified stationary family of actual YM sources, or prove a nonconstructive occurrence result retaining that family in the physical representation. The family must be able to have a nondecaying discrete source correlation. The full electric–Wilson current is ruled out as its action, even on the additional physical link degrees of freedom. One should not spend further effort controlling that current's other phases in the hope that this alone yields the norm realization.

There are two distinct possible outcomes worth seeking:

- A physical interpretation and independent bound making the **signed** response (10) tempered would imply RH by Theorem 2, but would not by itself give an OS source norm. OS temperedness cannot simply be cited in the arithmetic variable.
- An independently derived **positive physical correlation** (30) would also yield the required global source law by Theorem 6, with no need to postulate every mixed Gram entry or a zero-spectrum operator.

The exact remaining gap is a YM mechanism establishing either of those physical hypotheses. No such mechanism is established here. The existing infinite positive prime-difference form still has zero domain, and no independently justified positive subtraction/renormalization has been proved. The new cutoff result strengthens the reason that a local subtraction alone is inadequate.

## 9. Reproducible diagnostics and audit

The [small checker](../numerics/check_single_probe_and_prime_edges.py) and [record](../numerics/records/single-probe-prime-edges-20260925.json) test the product-transform conventions, pole cancellation, the signs of both boundary primitives, and the normalized prime-cutoff profiles. The edge calculation uses a separately specified analytic bump; Theorem 5 applies to it as well as to the detecting probe. All 13 controls passed after quadrature refinement. At cutoff one million, the relative two-edge profile error is about 0.006306 and the normalized edge-energy ratio is about 0.999265. These are floating diagnostics, with no zeta zero list, interacting YM samples, or finite positivity certificates. They do not prove an infinite product's zero-free region, the PNT limit, or RH.

The [substantive self-audit](../reviews/SINGLE_PROBE_CURRENT_AND_CUTOFF_DOMAIN_AUDIT_20260925.md) records scope, domain checks, strengthened exclusions, and what has not been inferred. No central earlier signed identity is retracted. Earlier statements leaving a generalized source covariant under the full electric–Wilson current as a possibility are now narrowed by Theorem 4; the general source problem remains open.
