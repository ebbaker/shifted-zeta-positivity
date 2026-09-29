# Bounded audit of the infinite-support route

Date: 26 September 2026. Continuation round 5.

Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact variant and reasoning-effort setting are not exposed in this session. This is an analytic audit of two candidate mechanisms, with exact finite algebra controls. The [review](../reviews/INFINITE_L_BOUNDED_AUDIT_REVIEW_20260926.md) is a sequential same-agent review, not independent refereeing.

## 1. Decision and scope

**Decision: change approach. Suspend automatic enlargement of the fixed-support Schur certificate.** The existing estimates cannot become a useful uniform-support argument merely by certifying a more accurate odd gap or increasing the matrix size. Two explicit obstructions are proved below, each restricted to a specified estimate rather than the underlying Weil operator.

The audit assesses exactly two mechanisms:

1. Direct control of the combined mass–stiffness trace, separating small odd energies from their complement. The present scalar version provably loses uniformity. Retaining the exact algebra identifies the full trace with a normalized ground-state second moment; a logarithmic toy family shows that the general structural assumptions cannot bound that moment uniformly.
2. Transfer of concentration from the prolate-based candidate to the actual ground state. A quantitative transfer lemma and a polynomial Fourier-resolution bound are obtained. The required comparison with the actual Weil ground state remains unproved. It needs arithmetic information not supplied by the mechanical realization.

No arithmetic sweep in L was run: finite data would not settle either obstruction or the missing comparison. No new odd-gap, simple-even, Weil-positivity, Xi-identification, or infinite-support convergence claim is made. The useful result is a sharper decision about which estimates deserve further work.

## 2. Normalization and an L-dependence ledger

Set \(X=e^L=\lambda^2\), \(I_L=[-L/2,L/2]\), and \(d_n=2\pi n/L\). N is the finite Fourier cutoff; M below is the split used in a high-frequency lower bound. Write \(\varepsilon_L=\inf\sigma(W_L)\),
\[
K_L=W_{-,L}-\varepsilon_L I,\qquad
B_L=J_L^*(W_{+,L}-\varepsilon_L I)J_L.
\]
The fixed-support statements use the closed Weil form and Fourier core recorded in the [preceding fixed-support note](CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md). A positive odd gap is an additional assumption whenever \(K_L^{-1}\) is used. Finite CCM statements retain the simple-even ground state, nonzero boundary functional, and weighted-adjoint identities.

Let \(\Lambda(q)=\log p\) for a prime power \(q=p^j\), and zero otherwise. Use
\[
P_L=\sum_{q<e^L}\frac{\Lambda(q)}{\sqrt q},\qquad
D_L=4\sinh(L/2)+2\sum_{q\le e^L}\frac{\Lambda(q)}{\sqrt q}.
\]
The endpoint term q=e^L is a zero translation operator; including it in D only enlarges that bound. Since \(\Lambda(q)\le L\) and \(\sum_{n\le X}n^{-1/2}\le2\sqrt X\),
\[
P_L\le2Le^{L/2},\qquad D_L\le(2+4L)e^{L/2}.
\tag{1}
\]
These are elementary bounds, with no prime-number theorem input.

| Quantity | Dependence on L or missing control | Meaning |
|---|---|---|
| Inverse derivative J | \(\lVert J\rVert\le L/\pi\), \(\operatorname{tr}(J^*J)=L^2/8\) | Geometric scaling, not arithmetic cancellation |
| Prime/pole absolute bound D | (1), and \(D_L\ge4\sinh(L/2)\) | The chosen upper-bound expression grows; actual form values may cancel |
| Ground energy | \(\lvert\varepsilon_L\rvert\le D_L+6\) for L>=2, proved below | Retains the energy shift without presuming its sign |
| Integrated mass trace | \(\operatorname{tr}B_L\le U_L=(D_L+\lvert\varepsilon_L\rvert)L^2/8+\sqrt3 L/4\) | Explicit bound; \(U_L=O(L^3e^{L/2})\) for L>=2 |
| Odd gap \(\kappa_L\) | Positivity unknown in general; if positive, \(\kappa_L\le2D_L+8\) for L>=2 | A finite Ritz difference is not a lower bound on this quantity |
| Odd pole tail | \(p_L(M)=4L\sinh^2(L/4)/(\pi^2M)\) | This upper bound is of size \(Le^{L/2}/M\) |
| Continuous-frequency leakage | \(\eta_L(M,T)=(LT+1)/[\pi^3M(1-(T/d_{M+1})^2)^2]\), T<d_(M+1) | High discrete modes still leak into low continuous frequency |
| Prime translation norm sum | \(S_L\le2P_L\), but \(S_L\ge e^{L/2}/4\) for L>=log16 | Lower bound on the **sum of individual norm bounds**, not on the norm of the signed full Weil form |
| Divided-difference coefficient bound | \(\lvert b_{L,n}\rvert\le\beta_L=1/4+L(2\cosh(L/2)-1)/(2\pi^2)+P_L/\pi\) | \(\beta_L=O(Le^{L/2})\); the earlier number 2 applied only at L=log13 |
| Free-tail inverse trace | \(L^2\sum_{n>N}n^{-2}/(4\pi^2)\le L^2/(4\pi^2N)\) | N much larger than L^2 removes this known contribution only |

The general coefficient bound follows from the same exponential sine series as in the [odd-tail note](CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md): its archimedean part is at most \(1/d_n+\pi/4\), its pole part at most \(2(\cosh(L/2)-1)/d_n\), and its prime part at most P. No constant certified at log13 is reused at another support.

Consequently the geometric far-coupling expansion, for retained modes r and far rows n>K, has error
\[
\|E-F_q\|\le
\frac{2\beta_L}{1-(r/(K+1))^2}(r/K)^{2q}(1+r/K).
\tag{2}
\]
If r/K<=theta<1, this is at most \(2\beta_L\theta^{2q}/(1-\theta)\). For fixed theta and target error, a number of expansion terms of order L suffices for this bound. This does not control the intervening block or errors measured relative to a collapsing spectral scale. The much worse obstruction below comes from the high-block lower estimate, not this separable expansion.

## 3. Explicit scalar estimates and why they cannot be uniform

### A global multiplier upper bound

For the archimedean symbol \(a(t)=\Re\psi(1/4+it/2)-\log\pi\),
\[
-6<a(t)\le\tfrac12\log(1+t^2).
\tag{3}
\]
The lower bound was established in the preceding tail certificate. For the upper bound apply one digamma recurrence to z=1/4+it/2. The integral remainder from [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13), rearranged as in the preceding note, gives
\[
|\psi(z+1)-\log(z+1)+1/[2(z+1)]|\le4/75.
\]
The real parts of the two subtracted reciprocal terms are nonnegative. Since
\(|z+1|^2\le(25/16)(1+t^2)\),
\[
a(t)\le\tfrac12\log(1+t^2)+\log(5/4)+4/75-\log\pi
<\tfrac12\log(1+t^2).
\]
Here \(\log(5/4)<1/4\), \(\log\pi>\log2>1/2\), and \(1/4+4/75<1/2\). This is an effective elementary bound, not an asymptotic used without a remainder.

For even \(u\in H^1_0(I_L)\), Jensen and Plancherel therefore give
\[
\langle u,(W_{+,L}-\varepsilon_L)u\rangle
\le\|u\|^2\left[D_L+|\varepsilon_L|+
\tfrac12\log\left(1+\|u'\|^2/\|u\|^2\right)\right].
\]
Using \(\|Je_n\|^2=3/d_n^2\), \(\|(Je_n)'\|^2=1\), gives
\[
\operatorname{tr}B_L\le U_L:=(D_L+|\varepsilon_L|)L^2/8+\sqrt3 L/4.
\tag{4}
\]
For the logarithmic part, the decreasing function \(f(x)=\log(1+c^2x^2)/x^2\) satisfies \(\sum_{n\ge1}f(n)\le\int_0^\infty f(x)dx=\pi c\). Take \(c=2\pi/(\sqrt3 L)\). This proves the last term in (4); trace-class justification is unchanged from the earlier column argument.

The lower form bound gives \(\varepsilon_L\ge-6-D_L\). The even trial function Je_1 gives \(\varepsilon_L\le D_L+\tfrac12\log(1+d_1^2/3)\). For L>=2 this implies \(|\varepsilon_L|\le D_L+6\). The normalized odd first sine gives
\[
\kappa_L\le D_L+\tfrac12\log(1+d_1^2)-\varepsilon_L
\le2D_L+8\le4D_L\quad(L\ge2),
\tag{5}
\]
where \(D_L\ge2L\ge4\).

### Obstruction to the present scalar inverse-gap estimate

If \(\kappa_L>0\), then (4) yields the sufficient upper estimate
\(\operatorname{tr}(K_L^{-1/2}B_LK_L^{-1/2})\le U_L/\kappa_L\). But (4)–(5) also imply
\[
\boxed{U_L/\kappa_L\ge L^2/32\qquad(L\ge2).}
\tag{6}
\]
Indeed \(U_L\ge D_LL^2/8\) and \(\kappa_L\le4D_L\). Any certified lower gap used instead of the exact gap only increases this upper estimate. Thus **even exact knowledge of the odd gap cannot make this particular scalar mass-bound/inverse-gap argument uniform in L**.

Equation (6) is a lower bound on an upper-bound expression. It is not a lower bound on the actual mechanical trace. A sharper arithmetic estimate of the mass or a relative estimate can evade it. Certifying a fixed-support odd gap still has local mathematical value, but does not repair this support-growth problem.

## 4. The separate prime-norm tail certificate requires enormous cutoffs

For the translation-fiber method define
\[
S_L=\sum_{q<e^L}\frac{\Lambda(q)}{\sqrt q}
\,2\cos\frac{\pi}{\lceil L/\log q\rceil+1}.
\]
For q<e^L each path has at least two vertices, so its displayed norm is at least one. We now prove without prime asymptotics that
\[
S_L\ge e^{L/2}/4\quad(L\ge\log16).
\tag{7}
\]

Let X=e^L and n=ceil(X/2)-1, so X-2<=2n<X. Legendre's valuation formula gives
\[
\binom{2n}{n}\mid\operatorname{lcm}(1,\ldots,2n):
\]
at each prime power, \(\lfloor2n/p^j\rfloor-2\lfloor n/p^j\rfloor\) is zero or one. Also \(\binom{2n}{n}\ge4^n/(2n+1)\), since it is the largest of the 2n+1 coefficients summing to 4^n. Hence, writing \(\psi_{\rm Ch}(y)=\sum_{q\le y}\Lambda(q)\),
\[
S_L\ge X^{-1/2}\psi_{\rm Ch}(2n)
\ge\frac{(X-2)\log2-\log(X+1)}{\sqrt X}.
\]
For X>=16, \(\log2>1/2\) and \(\log(X+1)\le X/4-1\). The latter holds at 16 because exp(3)>17 and then follows by differentiation. These inequalities prove (7). Endpoint prime powers have not been included incorrectly.

The generalization of the current high-tail sufficient lower bound is
\[
h_L(M,T)=A-(A-a_*)\eta_L(M,T)-S_L-p_L(M),
\tag{8}
\]
where \(a_*=-6\), \(a_*\le A\le a(T)\), 0<=eta<=1, and T<d_(M+1). To certify a shifted tail strictly positive at threshold s, it needs h>s. Since h<=a(T)-S, (3) gives the necessary condition for **this test to succeed**
\[
\boxed{M+1>\frac L{2\pi}
\sqrt{\exp(\tfrac12e^{L/2}-2C)-1}}
\tag{9}
\]
whenever L>=log16, s>=-C with C independent of L, and the radicand is positive. In particular, for nonnegative thresholds C=0. Asymptotically (9) requires a cutoff at least of size \(L\exp(\tfrac14e^{L/2}-C)\), up to the fixed prefactor and a factor tending to one.

Thus even a Fourier cutoff exponential in L is eventually insufficient for this bound. Optimizing T or certifying constants more accurately does not remove the obstruction: it already follows by dropping two adverse terms from (8). It is a consequence of paying for all prime translations separately against a logarithmic multiplier.

This is not a lower bound on the cutoff actually needed by the Weil operator. Arithmetic cancellation, a different high-block comparison, or a threshold tending sufficiently far negative falls outside the argument. Such a negative threshold would itself need justification and comparison with the even energy. No conclusion about the sign of the Weil form follows from (9).

## 5. Candidate 1: the combined trace and ground-state concentration

For any finite positive mechanical pair, diagonalize K in its ordinary orthonormal basis: Kv_j=k_jv_j. Then
\[
\operatorname{tr}(K^{-1}M)=\sum_j\frac{\langle v_j,Mv_j\rangle}{k_j}.
\tag{10}
\]
A threshold theta separates this into a small-energy contribution and a complement bounded by \(\theta^{-1}\operatorname{tr}(P_{>\theta}M)\). Every summand is nonnegative. The needed cancellation is in the relation between the original forms that makes the low-energy mass small; it is not cancellation between positive summands of (10). The existing results bound neither part uniformly in L.

### Exact removal of the inverse-gap factor

Let the finite even ground function in centered logarithmic coordinates be
\[
g(x)=L^{-1/2}\left(a_0+2\sum_{n=1}^N a_n\cos(d_n(x+L/2))\right),
\qquad s=a_0+2\sum_{n=1}^Na_n\ne0.
\]
In the established boundary gauge the quotient square is
\[
Q=M^{-1}K=\operatorname{diag}(d_n^2)-\frac2s(d_na_n)_{n=1}^N(d_n)_{n=1}^N{}^t.
\]
Its determinant is \(\prod d_n^2\,a_0/s\). Positivity of the mechanical pair implies a_0/s>0, so the mean \(\int g=\sqrt L a_0\) is nonzero. The rank-one inverse formula gives
\[
\operatorname{tr}(K^{-1}M)=\sum_{n=1}^N d_n^{-2}
+\frac2{a_0}\sum_{n=1}^N a_nd_n^{-2}.
\]
After adding the free tail, the exact identity is
\[
\boxed{\tau_{L,N}=\frac{L^2}{24}+
\frac2{a_0}\sum_{n=1}^N\frac{a_n}{d_n^2}
=\frac12\frac{\int_{I_L}x^2g(x)\,dx}{\int_{I_L}g(x)\,dx}.}
\tag{11}
\]
The corresponding entire function is exactly
\[
F_{L,N}(z)=\frac{\int_{I_L}e^{-izx}g(x)\,dx}{\int_{I_L}g(x)\,dx}.
\tag{12}
\]
One can verify (12) by the finite determinant lemma followed by the sinc product; differentiating twice gives (11). This is a consequence of the known [CCM Fourier-determinant formula, Proposition 5.9 and Theorem 5.10](https://arxiv.org/html/2511.22755v1#S5.SS6), not a newly discovered spectral representation. The direct inverse calculation checks the normalization and shows exactly where the scalar gap has disappeared.

No pointwise positivity of g is assumed. Its normalized second moment in (11) is a signed ratio, although the spectral trace is nonnegative under the finite hypotheses. It must not be treated as a probability variance without an additional sign theorem.

### What the identity achieves, and what it does not

A uniform bound \(\int x^2|g|\le C|\int g|\) would suffice for trace control, but is unproved. The weaker signed-moment bound in (11) is also unproved. Removing the inverse gap from the formula has converted the task into ground-state concentration. It has not bounded that concentration.

There is an explicit obstruction to deriving the bound from the generic realization alone. On the periodic Fourier basis consider the nonarithmetic comparison family
\[
\widetilde W_LV_n=\log(1+d_n^2)V_n.
\]
It has a simple even constant ground state, commutes with differentiation and reflection, has logarithmic high-frequency growth and compact resolvent at each fixed L, and obeys the finite weighted-adjoint relation. Its mass–stiffness pair is
\[
\widetilde K_{nn}=\log(1+d_n^2),\qquad
\widetilde M_{nn}=\log(1+d_n^2)/d_n^2.
\]
Every finite pair is positive, its odd gap is positive at each fixed L, and its full normalized determinant is the sinc function. Nevertheless
\[
\widetilde\tau_{L,N}=L^2/24\longrightarrow\infty.
\tag{13}
\]
This family is not the arithmetic Weil form and is not claimed to satisfy its defining prime/pole distribution. It proves only that positivity, simple-even structure, logarithmic growth, and the mechanical transformation do not supply the missing uniform estimate.

**Candidate-1 disposition:** the scalar estimate is ruled out by (6). The exact relative formulation remains mathematically possible but needs a new arithmetic concentration estimate. Neither (10) nor (11) alone is the promised progress toward a uniform bound.

## 6. Candidate 2: a quantitative prolate comparison

This candidate identifies an explicit sufficient accuracy for a ground-state comparison. It does not establish that comparison.

### The known candidate can be concentrated and resolved

Let \(h(u)=(\pi/2)u^2(2\pi u^2-3)e^{-\pi u^2}\), and let \(h_\lambda\), supported on [-lambda,lambda], be the prolate combination in CCM with its stated normalization. The external input used here is their estimate
\[
\sup_{|u|\le\lambda}|h_\lambda(u)-h(u)|\le C\lambda^{-2}.
\tag{P}
\]
This is [CCM Lemma 7.2](https://arxiv.org/html/2511.22755v1#S7). The deductions below take (P) as input; they are not an independent verification of the prolate asymptotic theorem or of its comparison with the Weil ground state.

Put \(k(x)=\mathcal E(h)(e^x)\), where \(\mathcal E(h)(u)=u^{1/2}\sum_{n\ge1}h(nu)\). This is the even, rapidly decreasing Xi kernel with nonzero integral. Define the truncated logarithmic candidate
\[
k_L(x)=\mathbf1_{I_L}(x)e^{x/2}
\sum_{1\le n\le\lambda e^{-x}}h_\lambda(ne^x),
\]
then take its even part q_L and set \(v_L=q_L/\|q_L\|_2\).

The finite-sum error from (P) is at most \(C\lambda^{-1}e^{-x/2}\) on I. Its L1 norm is at most \(2C\lambda^{-1/2}\); weighting by 1+x^2 costs at most \(1+L^2/4\). The omitted Gaussian sum also must be included. With a decreasing envelope \(H(t)=C_0t^4e^{-\pi t^2}\) for t>=1, it is bounded by
\[
e^{x/2}H(\lambda)+e^{-x/2}\int_\lambda^\infty H(t)\,dt.
\]
Its integral is at most \(2\sqrt\lambda[H(\lambda)+\int_\lambda^\infty H]\), and the exterior tails of k are rapidly decreasing on both sides by its evenness. Hence
\[
\|q_L-k\|_{L^1(1+x^2)}=O((1+L^2)e^{-L/4}),\qquad
\|q_L-k\|_2=O(\sqrt L e^{-L/4}).
\tag{14}
\]
Both functions are regarded on the whole line by zero extension where appropriate. Even projection cannot increase these errors. The Gaussian tail terms are smaller than the displayed bounds. This explicitly accounts for the part of the infinite arithmetic sum absent from k_L.

In particular, after normalization, \(|\int v_L|\ge a>0\), \(\|v_L\|_1\) and \(|\int x^2v_L/\int v_L|\) are bounded for all sufficiently large L. Its normalized transform converges to \(\Xi/\Xi(0)\) on the real line. These assertions concern the candidate, not the actual Weil eigenfunction.

There is also a polynomial Fourier-resolution bound. Normalize the restriction of k to I in L2, calling it w_L. Its two endpoint values agree by evenness, so it is in periodic H1; its derivative norms stay bounded. For projection P_N onto modes |n|<=N,
\[
\|(I-P_N)v_L\|_2
\le C_1\sqrt L e^{-L/4}+C_2\frac{L}{N+1}.
\tag{15}
\]
This follows by comparing v_L with w_L using (14), then using Parseval and \(d_{N+1}^{-1}\|w_L'\|_2\). No derivative estimate for the prolate candidate itself has been assumed. Choosing N at least a fixed positive multiple of \(L^{7/2}\) makes (15) O(L^(-5/2)); it also makes the known free-tail trace O(L^(-3/2)). This resolves the Fourier approximation cost for the candidate only.

### The concentration-transfer lemma

Let u and v be real even unit vectors on I, with \(I_v=\int v\ge a>0\), phase chosen so \(\delta=\|u-v\|_2\). Suppose \(\sqrt L\delta\le a/2\). Then \(I_u\ge a/2\). Write \(m_2(v)=\int x^2v/I_v\) and \(\tau(v)=m_2(v)/2\). Cauchy–Schwarz yields
\[
\boxed{|\tau(u)-\tau(v)|\le
\frac{\delta}{a}\left(\frac{L^{5/2}}{\sqrt{80}}+|m_2(v)|\sqrt L\right).}
\tag{16}
\]
Indeed the numerator of the normalized moment difference is
\(\int x^2(u-v)-m_2(v)\int(u-v)\), while \(\|x^2\|_{L^2(I)}=L^{5/2}/\sqrt{80}\). For real z, the analogous transform estimate is
\[
|F_u(z)-F_v(z)|\le\frac{2\sqrt L\delta}{a}(1+|F_v(z)|).
\tag{17}
\]
These are elementary normalized-function estimates, independent of any eigenvalue assumption.

Apply them to \(v=v_L\) and to an L2-normalized finite CCM ground state \(u_{L,N}\). Along a sequence with \(L_j,N_j\to\infty\), the additional estimate
\[
\boxed{\|u_{L,N}-v_L\|_2=O(L^{-5/2})}
\tag{18}
\]
would give bounded full inverse trace by (11), (14), and (16), and arithmetic identification on a real interval by (17). Together with the finite CCM hypotheses, the earlier normal-family criterion would then give locally uniform convergence to Xi/Xi(0). The complete free factor is already included in (11)–(12); it has not been discarded. A choice satisfying (15) can also enforce the earlier explicit free-tail schedule.

Equation (18) is a **sufficient, unproved comparison target**, not a claimed convergence rate. It shows exactly how much a particular L2 comparison would accomplish. A weaker norm tailored to the moment could suffice; no necessity is claimed for the exponent 5/2.

### What a residual proof would require

Let \(A=W_{+,L,N}\) be the finite even Weil block. Normalize \(\widehat v=P_Nv_L/\|P_Nv_L\|_2\), set \(\rho=\langle\widehat v,A\widehat v\rangle\), and \(r=\|(A-\rho)\widehat v\|_2\). Let \(\epsilon^+_1\) be its second even eigenvalue. If the even ground is simple and a certified separation \(\sigma\le\epsilon^+_1-\rho\) is positive, spectral expansion gives
\[
\|u_{L,N}-v_L\|_2\le\sqrt2\left(
\|(I-P_N)v_L\|_2+r/\sigma\right)
\tag{19}
\]
after choosing the sign of the ground vector. The excited-state weight is at most (r/sigma)^2; converting it to distance gives the factor sqrt2. Normalizing a projection costs at most sqrt2 times its discarded L2 norm.

The unresolved quantitative requirement for this implementation is therefore
\[
\boxed{r_{L,N}/\sigma_{L,N}=O(L^{-5/2})}
\tag{20}
\]
on a suitable sequence, with rho below the second even level and with all finite CCM hypotheses established. The odd-sector gap being pursued in round 4 does not supply this even-sector separation. A small residual alone also does not locate the ground state within a cluster of small even eigenvalues.

No estimate of (20), and no alternative proof of (18), has been obtained in this audit. A future proof must retain the actual prime/pole arithmetic at the scale of this separation. Substituting a prolate spectral gap for the Weil gap would assume the missing comparison rather than prove it.

**Candidate-2 disposition:** the candidate concentration, its Fourier-resolution cost, and the transfer inequalities are controlled under the stated prolate input. The arithmetic ground-state comparison remains the decisive missing step. This clarifies that step but does not remove it.

## 7. Verification, claim ledger, and stopping decision

The standard-library [control program](../numerics/check_infinite_l_audit.py) verifies the rank-one inverse trace by exact matrix inversion, the normalized determinant by exact elimination at 20 rational spectral parameters, and the central-binomial divisibility and size inequalities for n=1..128. Its [small record](../numerics/records/infinite_l_audit_controls_20260926.json) binds the output to the program hash. Signed Fourier-coefficient controls check algebra only; they are not represented as actual positive Weil examples. The all-n proofs are the analytic arguments above, not inference from these finite checks.

| Claim | Status |
|---|---|
| Explicit mass bound (4) and failure of its scalar inverse-gap upper bound to stay bounded | Proved from the stated Weil-form facts, conditional on a positive odd gap when an inverse is used |
| Prime-norm certificate requires cutoff growth (9) | Proved for the specified test at thresholds bounded below independently of L |
| Full trace is the normalized ground-state second moment | Exact finite identity under the existing CCM assumptions; a consequence of the known transform formula |
| Generic structural hypotheses imply a uniform trace | False for the explicit nonarithmetic comparison family |
| Candidate estimates (14)–(15) | Deductions from the cited prolate input (P) and the known Xi kernel |
| Moment/transform transfer (16)–(17), residual inequality (19) | Proved elementary inequalities under their explicit normalization and separation assumptions |
| Actual arithmetic comparison (18) or (20) | Not established |
| Full odd gap, general simple-even hypothesis, Xi limit, RH | Not established |

The bounded audit stops here, after the two mechanisms. It recommends **changing approach to the arithmetic ground-state comparison and suspending automatic growth of the existing fixed-L certificate**. Further work is justified if it brings a concrete estimate for (20), or a direct normalized-moment comparison that bypasses that residual method. Merely improving fixed-L precision, another coordinate realization, or a new name for (18) does not meet that condition.

This is a method limitation and a sharper research target. It is not evidence that the actual infinite-L limit fails, and it is not a claim that a proof of that limit is close.

## Sources and preservation

- [CCM, Zeta Spectral Triples, v1](https://arxiv.org/html/2511.22755v1): Proposition 5.9/Theorem 5.10 for the Fourier-determinant relation, Lemma 7.2 for input (P), and Sections 7–8 for the candidate and missing comparison. Primary HTML inspected 26 September 2026.
- [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13): digamma integral underlying the explicit remainder bound already derived in round 4.
- [Program overview](../PROGRAM_OVERVIEW.md) and [audit instruction](../CONTINUATION_PROMPT.md) delimit this round. Earlier research files and numerical records are preserved. No third-party PDFs, large matrices, draft snapshots, commit, or release are added.
