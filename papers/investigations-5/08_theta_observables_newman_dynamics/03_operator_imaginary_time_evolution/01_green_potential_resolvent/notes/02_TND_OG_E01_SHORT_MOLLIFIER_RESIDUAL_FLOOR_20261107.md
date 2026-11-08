# E01 r1: a uniform short-mollifier quadratic-residual floor

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Exact backend model identifier and effort were **not exposed in verifiable session metadata**. The packet recommends gpt-6.1-sol / ultra; this is a recommendation, not a claim about the actual configuration. Two parallel inherited-configuration analytical helpers checked the primary-moment and Green/tail calculations; these are shared-premise internal checks, not E02 or independent specialist review.

**Status: proved in-note from the named imported theorem and inherited canonical Green/source inputs; separate E02 assessment pending.** This completes [E01 request r1](../research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md). All 25 frozen files and the external PDF matched their recorded sizes and SHA-256 hashes before execution. No frozen request, input, parent source or sibling was changed.

**Delivery limitation:** direct writes to the canonical checkout were denied. This note and the accompanying register updates are staged in the reviewable export; they are not installed in the checkout. The export's application manifest records the original versions. Chat capture also failed because no exact-id session transcript was discoverable; the explicitly partial public-text record is not a registered archive.

## 1. The theorem and exact class

Use the literal complete canonical source, only at Newman time zero:
\[
H_0(z)=\xi(s(z))/8,\qquad s(z)=\tfrac12-\tfrac i2z,\quad
a=\pi/8,\quad K(u)=\frac1{16\cosh(au)},\quad q(s)=\frac{s-1}{s}.
\]
The measure \(\mu_X\) puts density \(K(x-X)\) on each of \(y=0,8\); each boundary has mass \(1/2\). For fixed \(0<\theta<1/2\), put \(S=T/2\), \(N\le S^\theta\), and
\[
A(s)=\sum_{n\le N}a_nn^{-s},\qquad a_1=1,\quad a_n\in\mathbb C,\quad |a_n|\le1.
\tag{1}
\]
For each \(T\), a single such polynomial is used throughout the boundary and all centers. Define
\[
L_T=a^{-1}\log T,\quad I_T=[T-L_T,2T+L_T],\quad
F_A(z)=q(s(z))\zeta(s(z))A(s(z)),\quad c_A(X)=F_A(X+4i),
\]
\[
\epsilon_A(X)^2=\int |F_A/c_A(X)-1|^2d\mu_X.
\tag{2}
\]
Then
\[
\boxed{\quad
\liminf_{T\to\infty}\inf_{A\text{ satisfying }(1)}
\frac1{|I_T|}\int_{I_T}\epsilon_A(X)^2\,dX
\ge
\frac{1/(2\theta)-11/12}{\zeta(5/2)^4}
>
\frac1{12\zeta(5/2)^4}.
\quad}
\tag{3}
\]
In particular the requested finite lower bound \(1/[24\zeta(5/2)^4]\) holds for every sufficiently large \(T\), uniformly in \(A\). Its onset may depend on fixed \(\theta\) and the primary theorem with common coefficient bounds; no numerical onset is supplied.

This is an obstruction to uniformly small **sufficient quadratic certificates**, not a lower bound for the Green potential. It is a quantitative milestone in the sense of [target01](../../../../../../avoid/01_restating_the_target.md), not an RH-equivalent reformulation or an RH conclusion.

## 2. Analytic mean, denominator and actual variance

The fractional-part formula, for \(\Re s=\sigma>0\), gives
\[
q(s)\zeta(s)=1-(s-1)\int_1^\infty\{v\}v^{-s-1}\,dv.
\tag{4}
\]
The integral is holomorphic for \(\sigma>0\). It cancels the zeta pole at \(s=1\), with value one. On \(0\le\Im z\le8\), let
\[
C_A=\sum_{n\le N}|a_n|n^{-1/2}\le2\sqrt N.
\]
Then \(|F_A(x+iy)|\le C_A(8+|x|)\). Thus the strip Poisson formula applies to its real and imaginary parts: the vertical-side contributions vanish by exponential harmonic-measure decay against this polynomial growth. It proves the complete complex identity
\[
\int F_A\,d\mu_X=c_A(X).
\tag{5}
\]
At \(s_c=5/2-iX/2\), absolute convergence and Euler factors give
\[
2-\zeta(5/2)\le|A(s_c)|\le\zeta(5/2),\quad
\frac{\zeta(5)}{\zeta(5/2)}\le|\zeta(s_c)|\le\zeta(5/2),\quad
\frac35\le|q(s_c)|\le1.
\]
Since \(\zeta(5/2)\le1+\int_1^\infty u^{-5/2}du=5/3\), set
\[
c_*=\frac35\frac{\zeta(5)}{\zeta(5/2)}[2-\zeta(5/2)]>0,\qquad
U=\zeta(5/2)^2.
\]
Uniformly in \(X,T,A\),
\[
c_*\le|c_A(X)|\le U.
\tag{6}
\]
Expand the square using (5), retaining its actual center-dependent denominator:
\[
V_A(X):=\int|F_A|^2d\mu_X-|c_A(X)|^2
=|c_A(X)|^2\epsilon_A(X)^2\ge0,\qquad
\epsilon_A(X)^2\ge V_A(X)/U^2.
\tag{7}
\]
All these integrals are finite by the polynomial bound and exponential kernel. No center value has been replaced by one.

## 3. Green comparison including every multiplier zero

Write \(\mathcal J[f](X)=\int\log|f|d\mu_X-\log|f(X+4i)|\). The inherited complete canonical identity in parent [Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) gives \(\mathcal J[H_0]=J_0^{\rm G}\ge0\), absolute boundary-log integrability and the complete multiplicity-weighted Green sum. These are imported at their internally assessed scope.

The exact factorization is
\[
F_A=D_0H_0(A\circ s),\qquad
D_0(z)=\frac{16\pi^{s(z)/2}}{s(z)^2\Gamma(s(z)/2)}.
\tag{8}
\]
Here \(D_0\) is holomorphic and zero-free on the closed strip and a neighborhood. Its log-modulus is harmonic with at most linear plus logarithmic horizontal growth, so its strip mean has zero defect.

The polynomial multiplier may have zeros. For \(0<\delta\le1\),
\[
u_\delta(z)=\tfrac12\log(|A(s(z))|^2+\delta^2)
\]
is bounded subharmonic on the strip, and is bounded above by \(M=\log(C_A+1)\). Strip subharmonic majorization gives \(\int u_\delta d\mu_X\ge u_\delta(X+4i)\). Consequently
\[
0\le\int(M-u_\delta)d\mu_X
\le M-u_\delta(X+4i)\le M-\log|A(s_c)|.
\]
As \(\delta\downarrow0\), monotone convergence of \(M-u_\delta\) proves absolute boundary-log integrability of \(A\circ s\), including its boundary zeros, and
\[
\mathcal J[A\circ s](X)\ge0.
\tag{9}
\]
This uses the nonzero safe center, not any assumption of zero-free continuation of \(A\). Combining the logarithms in (8) and applying concavity of log to \(|F_A/c_A|^2\) yields
\[
\boxed{\quad
0\le J_0^{\rm G}\le\mathcal J[F_A]
=J_0^{\rm G}+\mathcal J[A\circ s]
\le\tfrac12\log(1+\epsilon_A^2).
\quad}
\tag{10}
\]
The multiplier contribution is retained with a nonnegative sign. Neither zeros of \(A\) nor boundary zeros are divided out. The pole of zeta was already canceled in (4); the plus \(G(X,1)\) in the separate prime representation is not added again here.

## 4. The primary moment: version, quantifiers and uniformity

The sole new external moment input is Maksym Radziwiłł, *Limitations to mollifying \(\zeta(s)\)*, **arXiv:1207.6583v3**, Proposition B (Soundararajan), printed p. 2. Its definition (1) permits complex coefficients with \(a(1)=1\) and the stated \(a(n)\ll n^\varepsilon\) bounds. For fixed \(\theta<1/2\), it gives
\[
\frac1S\int_S^{2S}|1-\zeta(\tfrac12+it)A(\tfrac12+it)|^2dt
\ge\frac1\theta+o_\theta(1).
\tag{11}
\]
This imports the theorem, including its underlying moment input; it does not reprove that external mean-value theorem. The conditional Theorems 2–3 are not used.

**Uniformity payment.** Pad shorter polynomials with zeros to \(\lfloor S^\theta\rfloor\). The whole class has coefficient-growth constants at most one for every fixed \(\varepsilon>0\). Proposition B applies to arbitrary such families, including coefficients depending on \(S\). If (11) failed uniformly, a sequence of offending coefficient arrays, extended by \(A=1\) at other heights, would itself be an admissible family with the same constants and contradict (11). Thus its \(o_\theta(1)\) lower error is uniform over (1). This argument concerns the lower bound, not an assertion that the displayed asymptotic formula has additive \(o(1)\) for arbitrarily large quadratic forms.

Inspection of §7, (13)–(16) and Lemmas 9–14, printed pp. 12–16, confirms why the primary lower bound survives arbitrary coefficients. With its \(N=\lfloor S^\theta\rfloor\), write
\[
y(\ell)=\sum_{d\le N/\ell}a_{d\ell}/d,\quad
G_N=\sum_{\ell\le N}\frac{\mu(\ell)^2}{\varphi(\ell)},\quad
z(\ell)=\frac{\mu(\ell)\ell}{G_N\varphi(\ell)},\quad
E_N=\sum_{\ell\le N}\frac{\varphi(\ell)}{\ell^2}|y(\ell)-z(\ell)|^2\ge0.
\]
Lemma 9 is an exact diagonalization with excess \(E_N\). Lemma 12 bounds the quadratic excess term by \((\log N+O(\log\log N))E_N\); Lemma 13 bounds the mixed error by \(O((\log\log N)/\sqrt{\log N})\sqrt{E_N}\); Lemmas 11 and 14 leave scalar vanishing errors and terms \(O((\log\log N)^2)E_N\). Absorbing the mixed term into any fixed positive allowance times \(\log S\,E_N\) leaves a scalar \(o(1)\), independent of the coefficients. Equations (15)–(16) then have a nonnegative excess coefficient \(1-\theta-\varepsilon\). For floors, \(\log N=\theta\log S+o(1)\), which changes only scalar vanishing terms and the absorbable excess coefficient.

The displayed Proposition B form in v3 includes **\(2\log2\)**. No main term has been reconstructed from an earlier conversion. The PDF's byte/hash identity and exact checked passages are in [source-use02](../references/02_TND_OG_E01_SOURCE_USE_20261107.md); the canonical citation remains [source-use01](../references/01_TND_OG_B01_SOURCE_USE_20261107.md).

## 5. Elementary first moment and the square mean

Let \(B(s)=\zeta(s)A(s)\). Shift its finite rectangle from \(\Re s=1/2\) to \(2\) at heights \(S,2S\). The pole at \(s=1\) lies outside this rectangle. For integer \(M=\lceil2S\rceil\),
\[
\zeta(s)=\sum_{n\le M}n^{-s}+\frac{M^{1-s}}{s-1}
-s\int_M^\infty\{v\}v^{-s-1}dv.
\tag{12}
\]
For \(1/2\le\sigma\le2\) on those two horizontal edges,
\[
|\zeta(s)|\le2\sqrt M+M^{1/2}/S+|s|M^{-\sigma}/\sigma
=O(\sqrt S),\qquad |A(s)|\le2\sqrt N.
\]
Both edges therefore cost \(O(\sqrt{SN})\), uniformly in the coefficients.

On \(\Re s=2\),
\[
B(s)=\sum_{n\ge1}b_nn^{-s},\qquad
b_n=\sum_{\substack{d\mid n\\d\le N}}a_d,\quad b_1=1,\quad |b_n|\le\tau(n).
\]
Termwise integration is absolutely justified. The nonconstant mean is at most
\(2S^{-1}\sum_{n\ge2}\tau(n)n^{-2}/\log n=O(S^{-1})\); the sum converges, for example by \(\sum\tau(n)n^{-2}=\zeta(2)^2\). Hence
\[
\frac1S\int_S^{2S}B(\tfrac12+it)dt
=1+O_\theta(S^{(\theta-1)/2}).
\tag{13}
\]
Expansion of the square in (11), followed by (13), gives uniformly
\[
\frac1S\int_S^{2S}|B(\tfrac12+it)|^2dt
\ge1+\frac1\theta-o_\theta(1).
\tag{14}
\]
In particular (11) was not substituted directly for a square mean or for the normalized residual.

## 6. Safe-line square mean and padding

For any interval \([u,u+S]\), absolute convergence at \(\sigma=5/2\) gives
\[
\frac1S\int_u^{u+S}|B(5/2+it)|^2dt
=\sum_{n\ge1}|b_n|^2n^{-5}+O(S^{-1}),
\tag{15}
\]
uniformly in \(u,A\). Indeed its absolute off-diagonal error is bounded by
\[
\frac4S\sum_{m<n}
\frac{\tau(m)\tau(n)}{(mn)^{5/2}\log(n/m)}
\le\frac{16}S\sum_{m\ge1}\frac{H_m}{m^3}<\infty,
\tag{16}
\]
where \(\log(n/m)\ge(n-m)/n\), \(\tau(n)\le2\sqrt n\), and
\(\sum_{k\ge1}1/[k(m+k)]=H_m/m\). This proves an actual common error bound.

Its diagonal satisfies
\[
\sum_{n\ge1}\tau(n)^2n^{-5}
\le1+4\sum_{n\ge2}n^{-4}
\le1+4(1/16+\int_2^\infty v^{-4}dv)=17/12.
\tag{17}
\]
The center has \(|q(5/2-it)|\le1\). Substitution \(X=2t\), and coefficient conjugation if necessary, proves
\[
\frac1T\int_T^{2T}|c_A(X)|^2dX\le17/12+O(T^{-1}).
\]
The two added pieces of \(I_T\) have total length \(2L_T\); by (6) their integral is at most \(2L_TU^2\). In particular, normalized by the **actual** length,
\[
\frac1{|I_T|}\int_{I_T}|c_A(X)|^2dX
\le\frac{T}{|I_T|}(17/12+O(T^{-1}))
+\frac{2L_TU^2}{|I_T|}
=17/12+o(1).
\tag{18}
\]

## 7. Complete convolution and the residual floor

Integrate (7) over \(I_T\). Tonelli applies to the complete nonnegative boundary square, without a truncation or any unproved upper-tail estimate. Discard only the nonnegative upper-boundary square. For \(x\in[T,2T]\), all \(X\in[x-L_T,x+L_T]\) lie in \(I_T\), so
\[
\int_{I_T}K(x-X)dX\ge k_{L_T}:=\int_{-L_T}^{L_T}K(u)du
=\frac1\pi\arctan(\sinh(aL_T))
\ge\frac12-\frac{e^{-aL_T}}{4a}
=\frac12-O(T^{-1}).
\tag{19}
\]
The discarded square pieces remain nonnegative; (19) does not replace the complete convolution by a falsely negligible remote boundary.

On the lower boundary \(|q(1/2-ix/2)|=1\). Define
\(\widetilde A(s)=\sum\overline{a_n}n^{-s}\), still in (1). Complex conjugation of zeta and the exact scaling \(x=2t,\ S=T/2\) give
\[
\int_T^{2T}|F_A(x)|^2dx
=2\int_S^{2S}|\zeta(\tfrac12+it)\widetilde A(\tfrac12+it)|^2dt
\ge T(1+1/\theta-o_\theta(1)).
\tag{20}
\]
It follows from (18)–(20) that
\[
\begin{aligned}
\frac1{|I_T|}\int_{I_T}V_A(X)dX
&\ge\frac{T}{|I_T|}k_{L_T}(1+1/\theta-o_\theta(1))
-\frac1{|I_T|}\int_{I_T}|c_A(X)|^2dX\\
&\ge\frac{1+1/\theta}{2}-\frac{17}{12}-o_\theta(1)
=\frac1{2\theta}-\frac{11}{12}-o_\theta(1).
\end{aligned}
\tag{21}
\]
Every vanishing error here is common to (1). Divide by \(U^2=\zeta(5/2)^4\), then take the infimum and liminf to obtain (3). Since \(0<\theta<1/2\), the limiting allowance is strictly larger than \(1/12\). The finite requested bound follows by the definition of a uniform vanishing error. Neither an unpadded interval nor a center-adaptive polynomial follows from this argument.

## 8. Complete-source acquisition and both remote tails

The proof above uses the exact canonical field and no numerical approximation. To retain the full consumer payment, adapt parent [Note28 §§3–6](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md) as follows. Use \(M_{\rm src}\) for the source index and \(V_{\rm src}\) for the radial cutoff, distinct from the mollifier length \(N\).

With \(\rho(u)=\pi e^{4|u|}\), \(C_2(M)=\sum_{n>M}n^4e^{-\pi(n^2-1)}\), \(B_0=5C_2(0)\), let
\[
\mathcal Q=\int_{\mathbb R}e^{9|u|}\rho(u)^2e^{-\rho(u)}du,\quad
\mathcal Q^{>V}=\int_{|u|>V}e^{9|u|}\rho(u)^2e^{-\rho(u)}du.
\]
The literal reflected theta sum and its positive majorant give, for its undifferentiated finite-source cosine/Fourier integral \(\widehat H\),
\[
\sup_{|\Im z|\le8}|H_0-\widehat H|
\le\delta_H:=\tfrac12[5C_2(M_{\rm src})\mathcal Q+B_0\mathcal Q^{>V_{\rm src}}].
\tag{22}
\]
Both terms tend to zero separately; this does not assume matching odd derivatives for a reflected finite prefix.

On the compact boundary \(|x-X|\le R\), put \(D_A=D_0(A\circ s)\) and \(\widehat F_A=D_A\widehat H\). Note28's reciprocal-gamma product bound, reused as an inherited derived inequality, supplies
\[
\sup |D_A|\le\mathcal B_A(X,R):=
16\pi^{9/4}C_A
\exp\!\left\{\frac94+\frac{\pi^2[81+(|X|+R)^2]}{192}\right\}.
\tag{23}
\]
Consequently the compact probability-norm error is at most
\(\mathcal B_A\delta_H/c_*\). No full-boundary use of this compact bound is allowed.

For the **exact** field, (4) gives
\[
|F_A(x)|\le C_A(2+|x|),\qquad
|F_A(x+8i)|\le\zeta(9/2)^2.
\]
Let \(B_X=2+|X|\). With \(\mu_{X,R}\) the restricted boundary measure,
\[
\begin{split}
\tau_A(X,R):=\frac{e^{-aR}}{2a}\bigg\{&
\frac{C_A^2}{c_*^2}
\left[(B_X+R)^2+\frac{2(B_X+R)}a+\frac2{a^2}\right]\\
&+\frac{\zeta(9/2)^4}{c_*^2}+2\bigg\}
\end{split}
\tag{24}
\]
bounds \(\|F_A/c_A-1\|_{L^2(\mu_X-\mu_{X,R})}^2\). To check constants, apply \(|v-1|^2\le2|v|^2+2\) and \(K(u)\le e^{-a|u|}/8\), then sum two spatial tails on each boundary and integrate the quadratic polynomial. The upper-boundary square requires the **fourth power** of \(\zeta(9/2)\) in (24).

For the center, the absolutely convergent zeta logarithm has tail
\[
\left|\log\zeta(s_c)-\sum_{p^k\le M_c}\frac{p^{-ks_c}}k\right|
\le\beta_{M_c}:=\tfrac23M_c^{-3/2}.
\]
Evaluate the finite \(A(s_c)\) itself, and set
\[
\widetilde c=q(s_c)A(s_c)
\exp\left(\sum_{p^k\le M_c}\frac{p^{-ks_c}}k\right),\qquad
|c_A-\widetilde c|\le U(e^{\beta_{M_c}}-1)=:\eta.
\tag{25}
\]
The factor \(U=\zeta(5/2)^2\) follows from \(|A|\le\zeta(5/2)\), \(|q|\le1\), and the partial-log exponential bound \(\le\zeta(5/2)\). Any eventual finite arithmetic error is added to \(\eta\). No logarithm of \(A\) or division by \(A\) is used.

Write \(\ell=|\widetilde c|-\eta>0\),
\(\mu_R=2\pi^{-1}\arctan(\sinh(aR))\), and
\(A_R=\|\widehat F_A/\widetilde c-1\|_{L^2(\mu_{X,R})}\).
The triangle inequality and exact denominator difference give
\[
\boxed{\quad
\epsilon_A(X)\le A_R+\frac{\eta}{\ell}(A_R+\sqrt{\mu_R})
+\frac{\mathcal B_A\delta_H}{c_*}+\sqrt{\tau_A(X,R)}.
\quad}
\tag{26}
\]
This pays compact source error, both remote boundaries, safe-center acquisition and denominator propagation separately.

For any fixed finite \(X,A,d,r\) and positive error budget \(h\), first choose \(R\) with \(\sqrt{\tau_A}<h/3\). Next fix that \(R\) and choose the two source cutoffs with \(\mathcal B_A\delta_H/c_*<h/3\). Finally acquire the center with \(\eta<c_*/4\) and \(2\eta\|\widehat F_A\|_{L^2(\mu_{X,R})}/c_*^2<h/3\). Then \(\ell\ge c_*/2\), \(|\widetilde c|\ge3c_*/4\). For this precision prescription use the sharper direct denominator payment
\[
\frac{\eta\|\widehat F_A\|}{|c_A||\widetilde c|}
\le\frac{4\eta\|\widehat F_A\|}{3c_*^2}
\le\frac{2\eta\|\widehat F_A\|}{c_*^2}<h/3,
\]
in place of the conservative surrogate in (26). It uses the exact known floor \(|c_A|\ge c_*\), not just \(\ell\); if the norm is zero the actual denominator error is zero. The finite norm may instead be bounded by \(\mathcal B_A B_0\mathcal Q/2\). Equation (25) attains any positive tolerance, including the zero-norm case.

The same ordered choices work for each tuple of a prescribed sequence with unbounded \(|X|,N\) or \(d\downarrow0\), using a fresh budget per tuple. This proves finite acquisition, not a common cutoff, affordable cost, small actual \(A_R\), or an executed finite certificate. No growing derivative order is used.

## 9. Consumer scope and analytical control screen

A canonical upper zero with \(d\le y\le1\) and \(|x-X|\le r\) forces
\[
J_0^{\rm G}(X)\ge m(d,r)=\frac{\sin(a)d}{\cosh(ar)}.
\]
Thus \(\epsilon_A^2<e^{2m(d,r)}-1\), if independently acquired with all of (26)'s errors, is sufficient for exclusion in that box. For fixed \(r\) this threshold tends to zero as \(d\downarrow0\). The positive average floor (3) prevents these residuals from being uniformly small throughout the padded interval using one polynomial from (1), even when the polynomial changes with \(T\). It does not give a quantitative density of bad centers or a lower bound on \(J_0^{\rm G}\). In particular (10) cannot be reversed.

The [result index](../../../../../../result-summaries/README.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md) and [patterns index](../../../../../../avoid/README.md), especially [control02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [same-model05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), govern this classification. The following is an analytical premise check, not numerical replay:

| Control | Shared data | Missing premise for this canonical application |
| --- | --- | --- |
| Euler-factor controls, including Note01's fixed-prime translated-source family | Positive smooth even source; generic harmonic/Green facts; heat evolution and, for the fixed-prime family, common source/count constants | The observed field is not literal \(H_0=\xi/8\). Its extra multiplier changes the arithmetic object; Proposition B is applied here to the unchanged \(\zeta A\) class, not indiscriminately to the control. |
| Weighted-square and finite-prefix controls | Square support and the specified finite endpoints/moments | Complete normalized theta coefficients and the full reflection conjunction; they supply no unchanged zeta identity. |
| Reflected super-Gaussian control | Positivity, evenness, endpoint identities and Fourier–Gram positivity | Exact theta square expansion and xi/zeta identity. |
| Smooth-density and positive-primitive controls | Their recorded decay, shape, primitive positivity and endpoint data | Literal complete arithmetic source and its xi/zeta moment input. |

No argument from positivity alone is claimed to distinguish the canonical field. This note neither assumes a canonical collision nor extends Note01's conditioning obstruction into a theorem about theta-only stability.

The theorem excludes uniform vanishing quadratic certificates **only** for fixed \(\theta<1/2\), bounded complex coefficients with \(a_1=1\), one polynomial per padded interval, the fixed kernel and strip, and Newman time zero. Longer or adaptive polynomials, \(\theta\ge1/2\), unpadded intervals, signed logarithmic cancellation and other Green/resolvent methods are outside its conclusion.

## 10. Disposition

E01 completes with the stronger bound (3), the exact E5–E6 comparison and a complete acquisition ledger. No bounded repair or conceptual escalation was needed. No numerics, manuscript, commit, shared-summary promotion or sibling expansion occurred. The requested canonical signed **upper** Green margin remains unacquired.

Next is **[E] TND-OG-E02 — Sol6.1/ultra**, a separate fixed claim-level assessment of this note, its actual return and Note01 §§1–5. Its request is frozen in [assessment03](../research-progress/handoffs/03_TND_OG_E02_ASSESSMENT_REQUEST_20261107.md); it is ready for a later authorized execution, not performed by the two analytical helpers. See [Continuation03](../continuation-notes/03_TND_OG_E01_RESULTS_AND_MODEL_CHANGE_20261107.md). A model change does not constitute specialist independence.
