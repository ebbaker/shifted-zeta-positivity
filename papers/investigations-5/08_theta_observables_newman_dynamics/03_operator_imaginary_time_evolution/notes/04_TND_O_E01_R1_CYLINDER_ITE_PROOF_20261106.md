# TND-O-E01 r1 cylinder imaginary time realization

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, verified in the current rollout `turn_context`. Branch chat0002, thread `01a1b245-ac68-7e83-afd5-26a26a873c90`. **E — execution, unchanged r1.** [Activation][activation], [actual input versions][inputs] and the [sole register][progress] fix authorization, provenance and status.

**Result: all six r1 obligations are proved in this note, conditional on the declared canonical source and preparation choices, with proof-author checking only.** The full cylinder has a nonnegative self-adjoint relative-energy generator K=L0−4I. Its fixed calibrated amplitude observation is exactly

\[
 R_\chi e^{-\tau K}E_\chi F_{\lambda_0}=H_{\lambda_0-\tau},\qquad \tau\ge0.
\tag{1}
\]

The unshifted generator cannot produce this absolute orbit for every nonnegative time with any fixed bounded linear L² readout and fixed finite-norm initial field. The error identity is exactly the direct-source identity. A colliding smooth control satisfies the same generic operator and moment premises. This is an operator/domain and interpretation result; it provides no collision restriction.

## 1. Fixed inputs and geometric conventions

The [unchanged r1 request][request] selects B01's [Note02][b01] and [Decision01][decision]. [Parent Note02][parent], §§1–3 and 5–7, supplies the full cylinder, Fourier convention, canonical reflection, source normalization and complete bounds. [Shared Review01][shared], §§3–5, accepts those inherited results within their explicit geometric/source comparison scope. Its heat-generator and reflected-prefix qualifications are retained. The [B01 source-use receipt][refs] identifies checked primary passages behind the inherited angular spectrum and H0 normalization. No new external theorem is imported: the proofs below use the stipulated angular resolution, explicit real multipliers, Fourier Plancherel and dominated integrals. This is not a renewed assessment of every indirect reference.

Write

\[
 \mathcal K=L^2(S^2,\Sigma;d\Omega),\qquad
 \mathcal H_C=L^2(\mathbb R_v,dv;\mathcal K),\qquad
 g_C=dv^2+\tfrac14g_{S^2}.
\tag{2}
\]

The metric volume is dv dΩ/4. If metric-volume fields are used, the unitary conversion from (2) is Ψ↦2Ψ, and the corresponding readout must be composed with its inverse. We work throughout in the product-measure convention (2); there is no extra volume factor in (1).

The unit-sphere self-adjoint Dirac operator D has eigenvalues ±n, n≥1, multiplicity 2n for each sign. A=D² has complete orthogonal shell projections P_n of rank 4n. Thus both Dirac signs and all angular shells remain in the ambient space. The inherited cylinder Dirac square is

\[
 L_0=-\partial_v^2+4A=(\nabla^C)^*\nabla^C+2,
 \qquad K=L_0-4I=-\partial_v^2+4(A-I).
\tag{3}
\]

The Fourier convention is

\[
 (\mathscr F\Psi)(p)=\widehat\Psi(p)
 =(2\pi)^{-1/2}\int_{\mathbb R}e^{-ipv}\Psi(v)\,dv,
 \qquad \mathscr F^{-1}\widehat\Psi(v)
 =(2\pi)^{-1/2}\int_{\mathbb R}e^{ipv}\widehat\Psi(p)\,dp.
\tag{4}
\]

Integrals initially defined on integrable data extend unitarily to L². All angular pairings below are conjugate-linear in the first argument. Source coordinate u is calibrated externally to radial momentum p=u. The observed real Newman variable x is radial position v=x. Analytic continuation x↦z is a source-transform statement, not physical complex momentum. No physical source-position identification u=v is made.

The complete normalized source is supplied:

\[
 F_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\tfrac12\int_{\mathbb R}F_\lambda(u)e^{izu}\,du
 =\int_0^\infty F_\lambda(u)\cos(zu)\,du,
\tag{5}
\]
\[
 \Phi(u)=e^u\sum_{n\ge1}[2(n^2s)^2-3n^2s]e^{-n^2s},
 \quad s=\pi e^{4u},\quad u\ge0.
\tag{6}
\]

The complete Jacobi identity extends (6) smoothly and evenly to the real line, with all odd derivatives zero at u=0. Every summand at u≥0 is positive, so Φ(0)>0. The inherited absolute normalization is H0(z)=ξ((1+iz)/2)/8. Complete unit weights, reflection, phase and scale remain input data.

## 2. Full maximal realization and common core

Put m_n(p)=p²+4(n²−1), and use the complete Fourier/shell unitary identification

\[
 \mathcal H_C\simeq\bigoplus_{n\ge1}
 L^2(\mathbb R_p;\operatorname{Ran}P_n).
\]

Define

\[
 \operatorname{Dom}K=\left\{\Psi\in\mathcal H_C:
 \sum_{n\ge1}\int_{\mathbb R}m_n(p)^2
       \|P_n\widehat\Psi(p)\|_{\mathcal K}^2\,dp<\infty\right\},
 \qquad \widehat{K\Psi}_n=m_n\widehat\Psi_n.
\tag{7}
\]

Underlying L² membership in (7) is essential, especially in shell n=1 near p=0. The domain is dense: finite shells with bounded momentum support form a dense subset and lie in it. The operator is symmetric because each m_n is real. If h lies in its adjoint domain, with adjoint value k, test against arbitrary L² fields supported in finitely many complete shells and a bounded momentum interval. On each such set m_n is bounded; the adjoint relation forces k_n=m_n h_n almost everywhere. Exhaust the shells and intervals. Since k∈H_C, their squared integrals have finite sum, so h∈Dom K and K*h=Kh. Conversely the domain elements satisfy that adjoint relation by Cauchy–Schwarz. This proves self-adjointness and closedness on precisely (7).

For L0 the multiplier is ℓ_n=m_n+4. The inequalities

\[
 m_n^2\le\ell_n^2\le2m_n^2+32
\tag{8}
\]

show Dom L0=Dom K as sets, with equivalent graph norms. This proves that (3) is the actual constant shift of the inherited self-adjoint realization.

A common core is

\[
 \mathcal C=\bigcup_{N\ge1}
 C_c^\infty(\mathbb R_v;\bigoplus_{n=1}^N\operatorname{Ran}P_n).
\tag{9}
\]

To prove graph density, let Q_N=Σ_{n≤N}P_n. For Ψ∈Dom K, the tail of Σ∫(1+m_n²)||Ψhat_n||² tends to zero, hence Q_NΨ→Ψ in graph norm. Each retained angular space is finite dimensional, and for each fixed shell the weight 1+(p²+4(n²−1))² is equivalent to 1+p⁴. Thus each coefficient of Q_NΨ lies in H²(R). For a fixed smooth cutoff η equal to one near zero and supported in a compact interval, η(v/R)h→h in H² as R→∞: expand the first two derivatives; the terms with cutoff derivatives have factors R⁻¹ and R⁻² and are bounded by the corresponding L² norms, while the remaining tails vanish. Mollifying each cut-off coefficient then converges in H² with compact support. Finite coefficients permit simultaneous approximation. Combining these two stages proves (9), including all complete shells and both signs. By (8) it is also an L0 core. No reflected finite theta prefix is used in this proof. For higher integer powers the same argument uses H^(2j) in each finite shell and the weight 1+m_n^(2j).

The spectrum of K is [0,∞). Outside that set (m_n−z)⁻¹ is bounded, while shell n=1 supplies approximate spectral vectors near every p²=a≥0, including a=0. No a is an eigenvalue: in each shell {p:m_n(p)=a} has Lebesgue measure zero. On either open momentum half-line, p↦p²+4(n²−1) is a smooth monotone change of variable, so its spectral densities are absolutely continuous; the thresholds contribute no atoms. Countable shell sums preserve absolute continuity. In particular zero is a continuous threshold, not a normalizable ground state. In each inherited signed Dirac pair the cylinder block is [[2n,p],[p,−2n]], with eigenvalues ±√(p²+4n²), each with 2n angular states at fixed p. The complete L0 spectrum remains [4,∞); the unchanged first-order cylinder Dirac spectrum remains (−∞,−2]∪[2,∞). Subtracting 4 from its square neither discards a Dirac sign nor asserts a new first-order square root.

Define, on all of H_C,

\[
 \widehat{S(\tau)\Psi}_n(p)=e^{-\tau m_n(p)}\widehat\Psi_n(p),
 \qquad \tau\ge0.
\tag{10}
\]

These are contractions, S(0)=I and S(τ+σ)=S(τ)S(σ), directly by multiplication. Their operator norm is exactly one, since shell n=1 has positive-measure momentum neighborhoods arbitrarily close to zero. Dominated convergence with |e^(−τm)−1|≤2 proves strong continuity at zero and hence at every nonnegative time. On Dom K, |(e^(−hm)−1)/h|≤m for h>0 proves the strong right derivative −K at zero; multiplication then gives ∂τS(τ)Ψ=−KS(τ)Ψ and domain preservation. Conversely, if the strong difference quotient has an L² limit, Fatou applied to its squared multiplier norm forces Σ∫m_n²||Ψhat_n||²<∞. Thus the generator domain is exactly (7), not just a formal dense subset.

For τ>0 and integer j≥1, sup_{m≥0}m^j e^(−τm)=(j/(eτ))^j, proving finite-power smoothing for general data. The exact domain of K^j has weight m_n^(2j) together with L² membership. Multiplication by e^(δm), δ>0, is unbounded already in shell n=1; (10) supplies no bounded reverse-time evolution on H_C.

## 3. Encoder, fixed readout and absolute calibration

Choose any fixed unit χ∈Ran P1. It may have components in either Dirac sign. On the full source space L²(R_u), define

\[
 \widehat{E_\chi f}(p)=f(p)\chi,
 \qquad
 (J_\chi\Psi)(x)=\langle\chi,\Psi(x)\rangle_{\mathcal K},
 \qquad R_\chi=\sqrt{\pi/2}\,J_\chi.
\tag{11}
\]

Eχ is an isometry by (4) and ||χ||=1. Angular Cauchy–Schwarz gives ||Jχ||≤1, with equality on any nonzero field h(v)χ; hence ||Rχ||=√(π/2). Jχ and Rχ are bounded into L²(R_x), with almost-everywhere representatives. Their definition makes no bounded point-evaluation assertion on arbitrary H_C. The rank-one angular projection onto χ commutes with K and S(τ). This is a declared reducing preparation channel of the full operator, not a cutoff of its ambient angular spectrum or an invariant parity subspace for the first-order Dirac operator.

Let \(\mathsf M\) be multiplication by u² on \(\operatorname{Dom}\mathsf M=\{f\in L^2:u^2f\in L^2\}\), and let B=−∂x² on H²(R). In shell n=1, m_1=p², so

\[
 E_\chi f\in\operatorname{Dom}K\iff f\in\operatorname{Dom}\mathsf M,
 \qquad KE_\chi f=E_\chi\mathsf M f.
\tag{12}
\]

For Ψ∈Dom K, Fourier transformation of Rχ gives √(π/2)〈χ,Ψhat(p)〉. The estimate

\[
 \int p^4|\langle\chi,\widehat\Psi(p)\rangle|^2dp
 \le\int p^4\|P_1\widehat\Psi(p)\|^2dp
 \le\sum_n\int m_n^2\|P_n\widehat\Psi\|^2dp
\tag{13}
\]

shows RχΨ∈H². Since (A−I)χ=0, the exact typed identity is

\[
 R_\chi K\Psi=BR_\chi\Psi\quad(\Psi\in\operatorname{Dom}K).
\tag{14}
\]

Explicit multipliers, with no domain cancellation, yield for all L² inputs

\[
 S(\tau)E_\chi=E_\chi e^{-\tau\mathsf M},\qquad
 R_\chi S(\tau)=e^{-\tau B}R_\chi.
\tag{15}
\]

For f∈L¹∩L², the canonical continuous representative of RχEχf is

\[
 R_\chi E_\chi f(x)
 =\frac{\sqrt{\pi/2}}{\sqrt{2\pi}}\int_{\mathbb R}f(u)e^{ixu}du
 =\tfrac12\int_{\mathbb R}f(u)e^{ixu}du.
\tag{16}
\]

For even f this is exactly ∫₀∞f(u)cos(xu)du; both the full-line 1/2 and half-line constant are fixed. There is no normalization by H(0). Section 4 pays the required L¹, L² and derivative hypotheses for every finite real λ. Consequently

\[
 \Psi_0=E_\chi F_{\lambda_0}
 =\sqrt{2/\pi}\,H_{\lambda_0}(v)\chi,\qquad
 S(\tau)\Psi_0=E_\chi F_{\lambda_0-\tau}
 =\sqrt{2/\pi}\,H_{\lambda_0-\tau}(v)\chi.
\tag{17}
\]

Equations (16)–(17) prove (1), including τ=0 and H0=ξ/8 at λ0−τ=0 when that time lies in the orbit. The time law is λ=λ0−τ: ∂τΨ=−KΨ, and ∂τH_(λ0−τ)=∂x²H_(λ0−τ). The source itself is a momentum amplitude, not sqrt(F), a probability density or a normalized state. The supplied source, Fourier phase/scale, p=u calibration, χ, readout and time identification are physical choices, not deductions from self-adjointness. If energy units are desired, H_rel=εK and τ=εt_E/ℏ use the inherited positive energy unit ε; they do not derive the clock identification.

## 4. Complete sources, derivatives and continuation

Fix M,T≥0, |λ0|≤M and 0≤τ≤T, and put L=M+T. Every finite real λ0 is covered by some M. Let ρ(u)=πe^(4|u|). To avoid confusing source polynomials with Hλ, denote the inherited recurrence polynomials by P_j:

\[
 P_0(s)=2s^2-3s,\quad
 P_{j+1}(s)=(1-4s)P_j(s)+4sP_j'(s),\quad \deg P_j=j+2.
\tag{18}
\]

For a polynomial P let a(P) be its absolute coefficient sum, and define

\[
 C_d(N)=\sum_{n>N}n^{2d}e^{-\pi(n^2-1)},\qquad
 B_j=a(P_j)C_{j+2}(0)<\infty.
\tag{19}
\]

Since ρ≥π>1, differentiating the complete half-line series and summing absolute values gives

\[
 \left|e^u\sum_{n>N}e^{-n^2\rho}P_j(n^2\rho)\right|
 \le a(P_j)C_{j+2}(N)e^u\rho^{j+2}e^{-\rho},\quad u\ge0.
\tag{20}
\]

Indeed |P_j(n²ρ)|≤a(P_j)n^(2j+4)ρ^(j+2), and e^(−n²ρ)≤e^(−ρ)e^(−π(n²−1)). For each fixed j, C_{j+2}(N)→0. Complete smooth reflection, already an inherited canonical-source result, gives

\[
 |\Phi^{(j)}(u)|\le B_j e^{|u|}\rho(u)^{j+2}e^{-\rho(u)}
\tag{21}
\]

on the whole real line. Reflected finite prefixes need not have matching odd derivatives at zero. Equations (20)–(21) do not assert their global smoothness or use them as the core (9).

For nonnegative integers r,d and L,b≥0, set

\[
 J_{r,d}(L,b)=\int_{\mathbb R}|u|^r
 e^{Lu^2+(b+1)|u|}\rho(u)^d e^{-\rho(u)}du.
\tag{22}
\]

This is finite. Substitution s=πe^(4|u|) makes it

\[
 \frac{2}{4^{r+1}}\int_\pi^\infty
 [\log(s/\pi)]^r(s/\pi)^{(b+1)/4}s^{d-1}
 \exp\!\left(\frac L{16}\log^2(s/\pi)-s\right)ds.
\tag{23}
\]

The exponent −s dominates its logarithmic square and every fixed polynomial/logarithmic factor. The same expression restricted to s≥πe^(4U) tends to zero as U→∞, paying full radial tails.

For λ=λ0−τ, (21) gives exponential L¹ moments and polynomial/exponential L² moments:

\[
 \int |u|^r e^{b|u|}|F_\lambda(u)|du
 \le B_0J_{r,2}(L,b),
\quad
 \int |u|^{2r}e^{2b|u|}|F_\lambda(u)|^2du
 \le B_0^2J_{2r,4}(2L,2b+1).
\tag{24}
\]

For the second bound, square (21), multiply by the weights and use e^(−2ρ)≤e^(−ρ). In particular, every prepared K power exists, uniformly on the parameter slab:

\[
 \|K^jE_\chi F_\lambda\|^2
 =\int |u|^{4j}|F_\lambda(u)|^2du
 \le B_0^2J_{4j,4}(2L,1),\qquad j\ge0.
\tag{25}
\]

There is no appeal to source-coordinate differentiability in (25): K acts as u² on momentum preparation.

For a,b,q≥0 integer derivative orders, and |Im z|≤β, explicit differentiation of the full source gives

\[
 \partial_{\lambda_0}^{a}\partial_\tau^{b}\partial_z^q
 H_{\lambda_0-\tau}(z)
 =\frac{(-1)^bi^q}{2}\int_{\mathbb R}
 u^{2a+2b+q}F_{\lambda_0-\tau}(u)e^{izu}du,
\tag{26}
\]
\[
 \left|\partial_{\lambda_0}^{a}\partial_\tau^{b}\partial_z^q
 H_{\lambda_0-\tau}(z)\right|
 \le\tfrac12B_0J_{2a+2b+q,2}(L,\beta).
\tag{27}
\]

The corresponding strong field derivative is (−1)^b Eχ[u^(2a+2b)Fλ]; after K^j its squared norm is bounded by B0²J_{4(j+a+b),4}(2L,1). At τ=0 these are right derivatives. The inequality |(e^(−hu²)−1)/h|≤u² and the next paid moment give dominated convergence in both L¹ exponential weights and L² for the first derivative; repetition gives every fixed finite order. Parameter derivatives can also be justified on a slightly larger compact parameter neighborhood and then evaluated with the displayed bounds. At τ=T the same formulas give the corresponding one-sided slab limits.

For completeness, source-coordinate derivatives have their own payment. Let

\[
 R_0(\lambda,u)=1,\qquad R_{j+1}=\partial_uR_j+2\lambda uR_j,
\quad
 R_j=j!\sum_{h=0}^{\lfloor j/2\rfloor}
 \frac{(2\lambda u)^{j-2h}\lambda^h}{h!(j-2h)!}.
\tag{28}
\]

Leibniz gives ∂u^q(u^rFλ) as the finite sum over α+β+γ=q, α≤r, of

\[
 \frac{q!}{\alpha!\beta!\gamma!}\frac{r!}{(r-\alpha)!}
 u^{r-\alpha}R_\beta(\lambda,u)e^{\lambda u^2}\Phi^{(\gamma)}(u).
\]

If A_β(L) is the sum of the absolute coefficients of Rβ at |λ|≤L, an explicit finite bound is

\[
 |\partial_u^q(u^rF_\lambda)(u)|
 \le D_{r,q,L}(1+|u|)^{r+q}
 e^{Lu^2+|u|}\rho^{q+2}e^{-\rho},
\tag{29}
\]

where D is the same finite multinomial sum of r!/(r−α)!, A_β(L) and B_γ. Here |Rβ|≤A_β(L)(1+|u|)^β and ρ^(γ+2)≤ρ^(q+2). Formula (23) and its squared version pay every polynomial seminorm, weighted L¹/L² moment and radial boundary limit in (29). Taking r=2a+2b pays every fixed source/time mixed derivative. The complete source is Schwartz, uniformly in each fixed seminorm on the slab, with all odd derivatives at zero vanishing by smooth even reflection. Away from zero, differentiated arithmetic tails use (20) in the finite sum; one-sided reflected limits are legitimate. Distributional derivatives of nonsmooth finite reflected prefixes are not substituted for complete-source derivatives. Every derivative order here is fixed and finite: no bound uniform in the order, nor convergence of an infinite derivative expansion, is asserted.

Equations (24), (26) and local complex domination prove that (5) is entire in z, with uniform convergence on every complex compact. They also yield joint entire dependence on the complex source parameter λ and z, if desired: replace L by an upper bound for Re λ on a compact set. This is a statement about the supplied orbit; it does not supply a bounded inverse to (10) on the full Hilbert space. The smooth real representative of (17), including every finite position/time derivative, is therefore fixed by the source integral and has this entire continuation.

For undifferentiated reflected arithmetic truncation Φ_N, all mixed time/z tail errors in (27) are bounded by replacing B0 with a(P0)C2(N); explicitly the bound is a(P0)C2(N)J_{2a+2b+q,2}(L,β)/2. The squared L² moment errors in (24)–(25) have the same replacement squared. These tend to zero, and (23) pays the additional exterior |u|>U tails. This proves complete-source convergence rather than a finite-source surrogate theorem, without using Φ_N as a globally smooth source-coordinate core approximation.

The scalar G is not needed for (1). If its inherited dictionary is used, Gλ=8(1−∂u²)⁻¹Fλ has Gλ(u)~cλe^(−|u|), cλ=8Hλ(i)>0, and

\[
 16H_\lambda(z)=(1+z^2)\int_{\mathbb R}G_\lambda(u)e^{izu}du
 \quad\hbox{initially only for }|\operatorname{Im}z|<1.
\tag{30}
\]

The raw G integral is not absolutely convergent on the boundary or beyond it. Entire continuation through (5) does not enlarge that raw strip or justify multiplying a divergent integral by 1+z² at z=±i. All continuation claims here use F, not a continued raw G integral.

## 5. Absolute energy origin and the precise unshifted obstruction

Since L0=K+4I on the common domain, its explicit heat multiplier gives

\[
 R_\chi e^{-\tau L_0}E_\chi F_{\lambda_0}
 =e^{-4\tau}H_{\lambda_0-\tau}.
\tag{31}
\]

Thus the angular energy offset is visible in absolute imaginary-time amplitude. Leaving L0 unshifted and using e^(4τ)Rχ instead would restore the same amplitude with an explicitly time-dependent amplifying calibration. That alternative is outside the fixed-readout contract, not a hidden step in (1).

More generally, for any fixed bounded linear R:H_C→L²(R), and any fixed Ψ0∈H_C,

\[
 \|Re^{-\tau L_0}\Psi_0\|_2
 \le\|R\|\,\|\Psi_0\|\,e^{-4\tau}.
\tag{32}
\]

For the canonical target and each fixed finite real λ0, Plancherel gives

\[
 \|H_{\lambda_0-\tau}\|_2^2
 =\frac\pi2\int e^{-2\tau u^2}|F_{\lambda_0}(u)|^2du.
\tag{33}
\]

For τ>0 substitute u=y/√τ. Since Fλ0 is continuous, bounded and Fλ0(0)=Φ(0)>0, the integrand e^(−2y²)|Fλ0(y/√τ)|² is dominated by ||Fλ0||∞²e^(−2y²). Therefore

\[
 \lim_{\tau\to\infty}\tau^{1/2}\|H_{\lambda_0-\tau}\|_2^2
 =\frac\pi2\Phi(0)^2\int e^{-2y^2}dy
 =\Phi(0)^2(\pi/2)^{3/2},
\]
\[
 \|H_{\lambda_0-\tau}\|_2
 \sim\Phi(0)(\pi/2)^{3/4}\tau^{-1/4}.
\tag{34}
\]

The positive coefficient contradicts (32) if the two L² functions are equal for every τ≥0. This proves the requested impossibility for the **unshifted L0, fixed finite-norm initial field and fixed bounded linear readout into real-line L², exact absolute target for all τ≥0**. It includes nonlocal bounded readouts and arbitrary angular preparation. It makes no finite-time-only impossibility claim and does not exclude unbounded/distributional observations, time-dependent calibration, other generators or constructions outside that class. In particular it is compatible with (1).

## 6. Identical direct error and collision control screen

For any f,g∈L²(R), not only even inputs, (11), (15) and Plancherel give

\[
 \|R_\chi S(\tau)E_\chi(f-g)\|_2
 =\sqrt{\pi/2}\,\|e^{-\tau u^2}(f-g)\|_2
 \le\sqrt{\pi/2}\,\|f-g\|_2.
\tag{35}
\]

Indeed the output is exactly √(π/2)F⁻¹[e^(−τu²)(f−g)]. This is B01 (12), with the identical source norm and absolute constants. A direct multiplication/Fourier calculation supplies the same equality and every bound derived solely from it. The cylinder contributes no improved estimating or computational bound. Canonical arithmetic was supplied to the initial data, not extracted from K≥0.

The generic preparation theorem requires only L² density. Every finite K power requires the corresponding polynomial L² moment, and entire readout requires exponential L¹ moments. Smoothness in momentum/source coordinate is not a prerequisite for those claims. Smooth source-coordinate derivatives such as (29) are an additional canonical-source statement.

Use the [control cluster][controls] at those actual premises:

| Control family | Generic operator admission and precise failed canonical premise |
| --- | --- |
| Euler-factor sources | Their finite shifted smooth even rapidly decaying sources have the required moments, hence admit the generic encoder/flow/readout. They fail unchanged unit-weight theta arithmetic; K≥0 and (35) do not use that arithmetic to restrict events. |
| Weighted-square and finite-prime sources | Applicable reflected rapidly decaying L² densities and all polynomial/exponential moments suffice. Full unit weights and/or complete canonical reflection fail. Unmatched odd reflection endpoints can invalidate global source-coordinate derivative claims, but do not invalidate these K-power or entire-readout claims. |
| Reflected super-Gaussian, smooth shape and positive-primitive sources | Their applicable even density and tail hypotheses admit the same realization. The exact theta arithmetic expansion fails. Positivity, reflection, primitive properties and self-adjointness do not reject their collisions. The explicit witness below pays its own domains. |
| Atomic controls, including BW-01 and atomic finite-profile versions | Finite measures with atoms are not L² densities: they fail the actual input-space premise. Moment existence or a Fourier transform does not cure this failure. A generalized-state encoder is outside r1. |
| Continuous compact finite-profile extensions | The stated bounded continuous compact densities are L² and have all polynomial/exponential moments, so are admitted even without source smoothness. They fail unchanged theta coefficients/full canonical profile; missing smoothness alone cannot exclude them. |
| RH-conditional normalized endpoint controls, including BW-10 | Applicable relative-density/tail bounds retain L² and exponential moments, within their inherited RH-conditional existence scope. Ordinary Dirichlet-series arithmetic fails. Their endpoint events are not newly computed here and do not change a canonical theta conclusion. |
| Fixed theta amplitude with variable observation kernel | These controls fail the literal full Fourier/cosine observation and Newman equation fixed in (16), rather than the source amplitude. They are not counterexamples to this fixed readout; no restriction follows merely from rejecting their changed readout. |
| Positive-measure profile relaxations of zero data | They are reduced information classes, not an asserted source density with this prescribed Fourier observation. An atomic relaxation fails the L² source premise; no physical theta event or additional operator encoding is inferred. |

Full normalized reflection plus the specified integer-square comb can identify theta in its inherited rigidity class; that source-identification result still supplies no signed collision estimate. Family-specific properties beyond the cited control inventory are not assumed.

An exact admitted witness is enough to disprove an inference from the generic representation to noncollision. Reuse [direct Note04 §7][witness], with

\[
 g(u)=e^{-u^4}+\tfrac12e^{-(u-4)^4}+\tfrac12e^{-(u+4)^4},\qquad
 \Phi_*(u)=c e^{-u^2/4}g(u),\quad c>0.
\tag{36}
\]

Use its same positive normalization c, without fitting an operator. For |u|≥8, g(u)≤2e^(−u⁴/16); every finite derivative is a polynomial times one of its shifted super-Gaussians. Hence for every finite real λ and b,r≥0,

\[
 \int |u|^r e^{b|u|}|e^{\lambda u^2}\Phi_*(u)|du<\infty,
 \qquad
 \int |u|^{2r}|e^{\lambda u^2}\Phi_*(u)|^2du<\infty.
\tag{37}
\]

The same bounds are uniform on compact λ intervals; all polynomial L² moments and exponential L¹ moments needed above are paid. Thus EχF*_(1/2) is a finite-norm initial field in every K-power domain; (1) with this source and the same K,χ,R is valid, with entire readout.

At λ*=1/4 the source factor is cg(u), so translation of the full Fourier transform gives exactly

\[
 H^*_{1/4}(x)=cQ(x)(1+\cos4x),\qquad
 Q(x)=\int_0^\infty e^{-u^4}\cos(xu)du.
\tag{38}
\]

To verify the curvature without a numerical value, put M_j=∫₀∞u^j e^(−u⁴)du. Integrating the derivative of ue^(−u⁴) yields M4=M0/4; Cauchy–Schwarz gives M2≤√(M0M4)=M0/2. The inequality cos y≥1−y²/2 therefore gives Q(x)≥M0(1−x²/4)>0 for |x|<2. At x*=π/4,

\[
 H^*_{1/4}(x_*)=\partial_xH^*_{1/4}(x_*)=0,
 \qquad \partial_x^2H^*_{1/4}(x_*)=16cQ(\pi/4)>0.
\tag{39}
\]

With λ0=1/2 this is τ*=1/4. The same nonnegative self-adjoint cylinder and fixed calibrated readout admit a positive-Newman-parameter collision. The witness fails canonical theta arithmetic; the generic realization has not used that arithmetic in any collision-sign argument. This screens the representation, not source-sensitive mechanisms using the given theta profile.

## 7. Disposition and proof-author checking boundary

| r1 obligation | Proof location and result |
| --- | --- |
| 1. Full realization/domain/core/heat | §2: complete-shell maximal self-adjoint domain, common compact-radial core, continuous threshold, contraction semigroup and exact generator domain |
| 2. Typed intertwiners and calibration | §3: isometric Eχ, ||Rχ||=√(π/2), domain-typed generator and semigroup identities, exact full/half-line constants and λ=λ0−τ |
| 3. Complete payments | §4: complete arithmetic and radial tails, exponential L¹ and polynomial L² moments, source/time/position derivatives including τ=0 right limits, finite K powers and entire source continuation; raw G strip kept separate |
| 4. Energy origin | §5: e^(−4τ) unshifted amplitude and positive coefficient Φ(0)(π/2)^(3/4) in the norm asymptotic; precise all-time bounded-readout exclusion |
| 5. Comparison and controls | §6: exact identical direct error, actual density/moment premises, admitted exact colliding witness and named failures of other controls |
| 6. Precise disposition | This section and the [return][return]: conditional supplied preparation, proved operator theorem, scoped obstruction, no collision or gain upgrade |

Inherited premises are the angular spectrum/geometry, complete theta reflection/normalization and source bounds, at their existing internal assessment level. New execution here pays the full shifted domain/core/evolution, typed prepared channel, complete finite-order limits, energy-gap comparison and identical error, while making their conditional preparation scope explicit. The theta source, Fourier encoding, phase, scale, χ, momentum calibration, fixed amplitude observation and time interpretation remain supplied. An intrinsic physical preparation law is unresolved and separate from the later collision question.

One proof pass and one bounded local correction pass were completed. The local pass verified the adjoint/core exhaustion, squared-source weight J(2L,2b+1), Fourier constants, heat sign, asymptotic coefficient, raw-G scope and actual control moments. It disambiguated the source multiplier from the parameter bound M, displayed the inherited signed Dirac block, and made the fixed-finite-order qualification explicit; these are local notation/scope annotations, with no changed equation or scientific contract. Its exact receipt is in the return. This is not E02 or specialist/formal independence. No conceptual alteration or failed r1 clause was required. No numerical evaluation, manuscript, delegation or successor task was executed.

Classification follows [the result index][results], [theta bookkeeping][theta] and [patterns index][avoid]: a conditional geometric/operator realization and scoped compatibility obstruction, not an RH criterion. Carry especially [re-realizations][a03], [used control premises][a02] and [scoped exclusions][a07]. The investigation remains open; no assessed global result-summary promotion or manuscript milestone is made.

**Next: [E] TND-O-E02 — Sol**, after author selection, for one fixed assessment and local correction check of this exact proof/input/return. The [continuation and model-change note][continuation] gives exact paths and a pasteable prompt. **[B] TND-O-B02 — Astra stays reserved and unactivated** for actual canonical collision-control mechanisms after the assessment. It may use the canonical source as given; intrinsic source generation is a separate question. The operator representation alone is not a collision restriction.

[activation]: ../research-progress/handoffs/06_TND_O_E01_R1_ACTIVATION_20261106.md
[inputs]: ../research-progress/handoffs/06_TND_O_E01_R1_INPUTS_20261106.json
[request]: ../research-progress/handoffs/03_TND_O_E01_R1_PROPOSED_REQUEST_20261106.md
[return]: ../research-progress/handoffs/06_TND_O_E01_R1_RETURN_20261106.json
[progress]: ../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md
[b01]: 02_TND_O_B01_OPERATOR_COMPARISON_AND_ENERGY_OFFSET_20261106.md
[decision]: ../brainstorm/notes/01_TND_O_B01_TWO_REALIZATION_DECISION_20261106.md
[parent]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[shared]: ../../reviews/01_TND_E03_R2_GEOMETRY_SOURCE_AND_TRANSPORT_ASSESSMENT_20261106.md
[refs]: ../references/01_TND_O_B01_SOURCE_USE_20261106.md
[witness]: ../../01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[continuation]: 05_TND_O_E01_RETURN_E02_CONTINUATION_AND_MODEL_CHANGE_20261106.md
