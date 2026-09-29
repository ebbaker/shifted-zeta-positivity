# Threshold deflation and the failure of the bare energy norm

28 September 2026 (America/New_York). CCM continuation, round 9. Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed in this session. The derivation and subsequent adversarial review use agents of the same model family; they are not independent human refereeing or formal verification. No numerical sweep, manuscript snapshot, commit, or push was made.

## 1. Result and selected mechanism

This round executes the [threshold-index handoff](CCM_THRESHOLD_INDEX_CONTINUATION_20260928.md). It tests one concrete mechanism: remove the known zero mode on the H side, use the positive archimedean form as the endpoint energy norm, and try to control signed prime truncation and threshold deflation in that norm.

The mechanism has a rigorous obstruction, even after exact removal of the zero mode:

* The known threshold profiles are dense in the **bare archimedean energy completion**, although they do not exhaust the physical even mean-zero Hilbert space.
* The reduced Birman–Schwinger family has spectral infimum tending to minus infinity as the depth tends to zero. It has no bounded endpoint operator in this normalization.
* Every fixed finite prime cutoff has an unbounded absolute relative-form remainder at the endpoint. This remains true on the exact mean-zero subspace.
* Removing the full closed known threshold span is legitimate in the physical Hilbert space, but that projection is unbounded in the bare energy norm. The quotient seminorm obtained by minimizing this energy over threshold profiles is identically zero.

The divergence is on the **negative** side of the signed Birman–Schwinger operator. It does not contradict the desired upper bound by one, exclude a one-sided factorization, or prove an obstruction to RH itself. Schedules with increasing prime cutoff can still control errors at positive depth. The sharp inequality and the CCM determinant limit remain open.

## 2. Exact reduction and the proposed endpoint estimate

Retain the literal theta kernel k, transform Xi/4, mass M=1/8, and threshold s=1/4 from round 8. Put c(x)=cosh(x/2), a=sqrt(k/c), and v0=sqrt(kc)/sqrt(M). On the even physical Hilbert space L2(dx), the inherited closed-form identity is

\[
H=sI+A_0-K,\qquad
\mathfrak a[v]=\|(g(D)+6)^{1/2}(av)\|_2^2,
\quad K=6M_{a^2}+P_a,
\tag{1}
\]
\[
\mathcal V=\{v\in L^2(dx)^+:av\in H_{\log}\},\qquad
g(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
P_a=\sum_{n\ge2}q_nM_a(T_{\log n}+T_{-\log n})M_a,
\qquad q_n=\Lambda(n)/\sqrt n.
\]

All Fourier integrals below use Plancherel measure dt/(2pi) when the transform is hat f(t)=integral f(x)exp(-itx)dx. Define p(t)=g(t)+6. The inherited bounds p>=p*>0 and p(t) comparable to 1+log(2+|t|) make

\[
\|f\|_{\mathscr E}^2=\int p(t)|\widehat f(t)|^2\frac{dt}{2\pi}
\tag{2}
\]

an equivalent H_log norm. This is the **bare** energy norm: it does not include ||v||2 when f=av.

Let P0=|v0><v0|, X=v0-perp, V_X=V intersect X, and let A_X be the positive self-adjoint operator represented by the restriction of a to V_X. This is a closed densely defined form on X. Density follows by compact-core approximation followed by subtraction of the v0 component; v0 belongs to V. Set C_X=P_X K restricted to X. Exact ground removal gives

\[
B_X:=(H-s)|_X=A_X-C_X,
\qquad \mathfrak b[v]=\mathfrak a[v]-\langle v,C_Xv\rangle.
\tag{3}
\]

The target is b[v]>=0 for every v in V_X. No lower bound of that kind is assumed here.

For 0<delta<s define the correctly reduced compact signed operator

\[
S_\delta=(A_X+\delta I)^{-1/2}C_X(A_X+\delta I)^{-1/2}.
\tag{4}
\]

Relative form compactness passes to the restricted form: the inclusion of V_X into V is bounded in their form-plus-L2 norms, and the compact map furnished by K can be composed with it and with P_X. Thus (4) is compact. The form congruence, with no positivity assumption on C_X, gives

\[
N(H<s-\delta)=1+n(S_\delta>1),\qquad
\mathrm{RH}\iff S_\delta\le I\quad\hbox{for every }0<\delta<s.
\tag{5}
\]

The initial one is exactly the removed zero mode. A_X is a form restriction; (4) is not an orthogonal compression of the old T_E by v0.

The sufficient approximation mechanism being tested would need finite constants in estimates such as

\[
|\langle v,C_Xv\rangle|\le L\mathfrak a[v],\qquad
|\langle v,R_Pv\rangle|\le\epsilon_P\mathfrak a[v]
\quad(v\in\mathcal V_X),
\tag{6}
\]

where R_P is the compression of P_a-P_(a,<=P) and, for a useful truncation, epsilon_P tends to zero. A threshold projection would also have to be bounded in a^(1/2) to descend to this energy completion. Sections 3–6 disprove these requirements, rather than merely observing that the round-8 bound loses a factor 1/delta.

The arithmetic identities and domain facts used here were checked against the [weighted operator proof](CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md), its [review](../reviews/CCM_WEIGHTED_TAIL_REVIEW_20260928.md), and the [annihilator note](CCM_XI_ANNIHILATOR_AND_BOUNDARY_RESIDUAL_20260928.md). The prime, archimedean, and pole signs agree with [CCM, Section 3, equations (3.7)–(3.11) and (3.19)](https://arxiv.org/html/2511.22755v1#S3), checked this session. The new arguments below are proved here; no additional external spectral estimate is invoked.

## 3. Threshold profiles are dense in the energy completion

For j>=1 put

\[
d_j=k^{(2j)}-4^{-j}k,\qquad z_j=d_j/a.
\tag{7}
\]

The inherited threshold eigenfunctions give z_j in Dom H, z_j perpendicular to v0, and B_X z_j=0. Indeed a Uu_j=d_j. Integration by parts gives integral c d_j=0. The superexponential tails put every z_j in the physical form domain. These are exact operator eigenvectors, so

\[
\mathfrak b[z_j,v]=0\quad(v\in\mathcal V_X).
\tag{8}
\]

**Proposition 1.** The linear span of the d_j, j>=1, is dense in the even space E defined by (2).

**Proof.** Let ell be a continuous linear functional on E annihilating all d_j. For a complex parameter z define

\[
k_z^{\rm ev}(x)=\tfrac12(k(x-z)+k(x+z)),\qquad
F(z)=\ell(k_z^{\rm ev}).
\]

This is holomorphic for |Im z|<pi/4. To justify the vector-valued assertion rather than assume it, use the theta series on the positive real tail. On each compact subset of the strip, with bounded Re z and |Im z|<=beta<pi/4, the real part of the exponential's decay parameter is bounded below by a positive constant times exp(2|x|). All fixed x and z derivatives consequently have uniform superexponential bounds for large positive x. The analytic evenness of k supplies the negative tail. These bounds give local holomorphy into H1, and hence into E, by dominated differentiation. Analytic evenness in the strip follows from the real theta identity by analytic continuation; the theta series is locally normally convergent throughout that strip.

The even Taylor coefficients satisfy

\[
F^{(2j)}(0)=\ell(k^{(2j)})=4^{-j}\ell(k),
\qquad F^{(2j+1)}(0)=0.
\]

Therefore F(z)=ell(k)cosh(z/2), first near zero and then throughout the connected strip. But real translations are isometries in E, so |F(t)|<=||ell|| ||k||_E for every real t. This forces ell(k)=0 and F(t)=0 for all real t.

Represent ell by an even h in E. Then F is the Fourier transform, up to the sign convention, of the even L1 function

\[
p(\xi)\overline{\widehat h(\xi)}\widehat k(\xi)/(2\pi).
\]

Integrability follows by Cauchy–Schwarz in (2). Fourier uniqueness forces this product to vanish almost everywhere. One can use Gaussian convolution and an approximate identity for this elementary uniqueness step. Since hat k=Xi/4 is nonzero and entire, its real zeros are isolated; p>0 then gives h=0. Thus ell=0, proving density. No information about the location of nonreal zeros was used. QED.

The topology is essential. This proves density of d_j in E, not density of z_j in X or V_X with its form-plus-L2 norm. In fact Section 4 supplies a vector outside their closed physical span. The map v to av identifies the completion of V_X in a^(1/2) with all of E, because its image already contains the dense d_j span.

## 4. A positive witness and an unbounded negative endpoint

First construct one compact even f with

\[
\int c(x)f(x)dx=0,\qquad Q(f)>0.
\tag{9}
\]

Choose 0<b<log(2)/2 and a nonzero even real phi in C_c^infinity((-b,b)). Choose an even psi of the same support with integral c psi=1. Set

\[
f_T(x)=\phi(x)\cos(Tx)-\beta_T\psi(x),\qquad
\beta_T=\int c(x)\phi(x)\cos(Tx)dx.
\]

Repeated integration by parts gives beta_T=O_N(T^(-N)) for every N. All prime autocorrelations vanish exactly, because their shifts are at least log 2>2b. The even pole contribution vanishes by the imposed moment. The archimedean form satisfies

\[
Q(f_T)=\langle f_T,g(D)f_T\rangle
=\tfrac12\|\phi\|_2^2\log T+O(1)>0
\tag{10}
\]

for large T. For completeness, the Fourier transform of phi cos(Tx) is the sum of two translated Schwartz functions divided by two. On either packet g(T+t)=log T+O(1) on bounded t, the complement is controlled by Schwartz decay and |g(t)|<=C(1+log(2+|t|)), and the packet cross term tends to zero. The beta_T correction has vanishing contribution. Fix such a T and call the resulting function f; put q=Q(f)>0 and v=f/a in V_X.

By Proposition 1 choose h_n in span{d_j:j>=1} with ||f-h_n||_E tending to zero. Define

\[
r_n=f-h_n,\qquad v_n=r_n/a\in\mathcal V_X.
\]

Every v_n is a legitimate physical form vector: f/a is compact smooth, and each h_n/a is a finite threshold combination. Equation (8) and the zero moment give

\[
\mathfrak a[v_n]=\|r_n\|_{\mathscr E}^2\longrightarrow0,
\qquad \mathfrak b[v_n]=\mathfrak b[v]=Q(f)=q>0.
\tag{11}
\]

Consequently

\[
\langle v_n,C_Xv_n\rangle=\mathfrak a[v_n]-q
\longrightarrow-q,
\qquad
\inf_{0\ne v\in\mathcal V_X}
\frac{\langle v,C_Xv\rangle}{\mathfrak a[v]}=-\infty.
\tag{12}
\]

This proves that even a finite lower relative bound for C_X is impossible. In particular the first absolute estimate in (6) is false.

**Corollary 2.** For the exact reduced family (4),

\[
\inf\sigma(S_\delta)\longrightarrow-\infty
\quad\hbox{as }\delta\downarrow0.
\tag{13}
\]

For any prescribed L>0 choose a fixed n for which the quotient in (12) is below -2L. Test S_delta on (A_X+delta)^(1/2)v_n; its Rayleigh quotient is

\[
\frac{\mathfrak a[v_n]-q}
{\mathfrak a[v_n]+\delta\|v_n\|_2^2}.
\tag{14}
\]

It is below -L for all sufficiently small positive delta. Since L is arbitrary this proves the full limit assertion, without assuming operator monotonicity for signed S_delta. There is no bounded operator representing the endpoint C_X sandwich on the completed energy space, and no convergence to one in operator norm. No quantitative rate in delta is claimed.

The positive q in (11) is crucial: the diverging negative spectral side in (13) is compatible with S_delta<=I. This argument constructs neither a negative Weil vector nor a subthreshold eigenvalue of H.

## 5. Every fixed prime tail fails absolute relative control

Write R_P=P_X(P_a-P_(a,<=P)) restricted to X for any finite P. In the f=av coordinates let

\[
\mathfrak p_{\le P}[f]=\sum_{2\le n\le P}q_n
\langle f,(T_{\log n}+T_{-\log n})f\rangle.
\]

This finite sum is bounded on L2, with norm at most 2 sum_(2<=n<=P) q_n. From p>=p*>0 and (11), ||r_n||2 tends to zero; hence p_(<=P)[r_n] tends to zero for each fixed P. The exact form identity (3) gives

\[
\langle v_n,R_Pv_n\rangle
=\mathfrak a[v_n]-6\|r_n\|_2^2
-\mathfrak p_{\le P}[r_n]-q\longrightarrow-q.
\tag{15}
\]

Thus, for **every finite P**,

\[
\inf_{0\ne v\in\mathcal V_X}
\frac{\langle v,R_Pv\rangle}{\mathfrak a[v]}=-\infty,
\qquad
\inf\sigma\bigl((A_X+\delta)^{-1/2}R_P
(A_X+\delta)^{-1/2}\bigr)\longrightarrow-\infty.
\tag{16}
\]

The second conclusion follows by the same fixed-vector argument as (14). This is stronger than failure of a remainder tending to zero: no finite absolute relative bound exists for any fixed cutoff.

There is no conflict with the inherited ordinary operator-norm estimate

\[
\|R_P\|\le\tau(P):=
2C^2\sum_{n>P}\frac{\log n}{\sqrt n}e^{-2cn},
\qquad
\|(A_X+\delta)^{-1/2}R_P(A_X+\delta)^{-1/2}\|
\le\tau(P)/\delta.
\tag{17}
\]

The v_n have uncontrolled physical L2 size. The limit in (16) keeps P fixed, whereas P(delta) growing at a suitable multiple of log(1/delta) can make (17) tend to zero. Such a schedule approximates operators at positive depths; it still needs an upper spectral margin to certify their strict inertia counts. Again, the obstruction is to absolute endpoint energy control, not to every one-sided use of the signed tail.

## 6. What exact threshold removal does and does not fix

Let Z be the closed physical L2 span of z_j in X. Since B_X is self-adjoint and all z_j are zero eigenvectors, Z is contained in its complete kernel and is reducing. Z need not be the complete kernel. The orthogonal projections onto Z and Y=X intersect Z-perp preserve V_X; this follows from the spectral form domain of the semibounded B_X and the bounded perturbation C_X. Equivalently, a and b have equivalent form-plus-L2 norms. Thus physical threshold removal is exact and legitimate:

\[
B_X=0_Z\oplus B_Y.
\tag{18}
\]

**Proposition 3.** The projection Pi_Y is unbounded in the bare norm a^(1/2), and

\[
\inf_{z\in\operatorname{span}\{z_j\}}\mathfrak a[v-z]=0
\quad\hbox{for every }v\in\mathcal V_X.
\tag{19}
\]

The second assertion is Proposition 1 applied to av. For the first use (11): Pi_Y v_n=Pi_Y v, while a[v_n] tends to zero. The fixed vector Pi_Y v is nonzero, because b[v]=q>0 and b vanishes on Z; it has strictly positive a-energy by injectivity of multiplication by a and p>0. No finite energy bound for Pi_Y can hold. The same reasoning shows that Z does not exhaust X.

The quotient of V_X by the known threshold span therefore has an identically zero seminorm if its norm is defined by minimizing a over the span. This completion cannot carry the nonzero form b. A physical compression to Y remains a valid possible alternative, but a new estimate on that compressed space is required; (19) says nothing against its possible one-sided positivity.

There is also a separate finite-deflation limitation. For every finite-dimensional physical threshold space F subset Z, let

\[
\alpha_F=\min_{z\in F,\ \|z\|_2=1}\mathfrak a[z]>0.
\]

On (A_X+delta)^(1/2)F the Rayleigh quotient of S_delta is

\[
\frac{\mathfrak a[z]}{\mathfrak a[z]+\delta\|z\|_2^2}
\ge\frac{\alpha_F}{\alpha_F+\delta}.
\tag{20}
\]

The min–max principle puts at least dim F eigenvalues at or above the right side. Hence, for every fixed N and epsilon>0, there are at least N eigenvalues greater than 1-epsilon for all sufficiently small delta. Any rank-at-most-r approximation L_delta obeys

\[
\liminf_{\delta\downarrow0}\|S_\delta-L_\delta\|\ge1:
\tag{21}
\]

use an (r+1)-dimensional trial space from (20) and a unit vector in its intersection with ker L_delta. This argument allows the approximant to vary with delta. It does not assert that the eigenvalues in question exceed one.

Deleting any fixed finite number of exact threshold directions on the physical side leaves an infinite threshold space, so the same crowding argument applies to the newly restricted A-form and its own Birman–Schwinger family. Infinite removal avoids that particular argument, but encounters the energy-projection obstruction above. These are different statements and neither licenses assuming a positive gap on Y.

## 7. Endpoint error ledger

The ledger concerns operator or all-vector estimates, rather than convergence on a selected test.

| Component | Proven control and delta dependence | Cancellation and inertia limit |
|---|---|---|
| Prime cutoff | ||remainder|| <= tau(P)/delta after the reduced sandwich. For any kappa>0, P(delta)=ceil((1+kappa)log(1/delta)/(2c)) gives tau(P)/delta ->0, up to the harmless polynomial factor. Every fixed P instead has (16). | Retains the exact full diagonal s. Finite cutoff breaks exact threshold annihilation; a small norm error must be compared to a proved upper spectral margin. |
| Spatial restriction | Inherited eigenfunction mass bound e_R/(delta-d_R), d_R<delta; d_R and e_R are superexponentially small. Choosing exp(2R)=L log(1/delta) with cL>1 makes e_R/delta ->0 and d_R/delta ->0. | This controls shallow eigenfunction tails as R grows, not an all-vector operator error or an inertia count by itself. Localization creates gamma and prime coupling terms already represented by e_R. |
| Frequency resolution | For Q_F the Fourier cutoff in f=av, ||(1-Q_F)f||2^2 <= ||f||_E^2 / inf_(|t|>F)p(t), of order 1/log F. Also a[(A_X+delta)^(-1/2)y] <= ||y||2^2. | This is a bound for f, not for v or the signed prime form. Spatial recovery of v introduces lower bounds for a on the retained region; frequency cutoff also breaks the exact mean and threshold constraints. No complete frequency operator-norm error or count certificate is supplied. |
| Ground-mode removal | H-side restriction to X is exact for every delta; no coupling error. A_X is the restricted form operator. | Preserves the true reducing zero mode. Ordinary v0-deflation of the old T_E would not be this construction. |
| Threshold projection and remaining coupling | Physical projection onto Y is exact and form-domain preserving; (19) proves it has no delta-independent bound in the bare energy norm. Finite removal leaves (20). | Exact B_X mixed blocks vanish, but A_X and C_X mixed blocks need not vanish separately. Approximate threshold projections need a bound on their actual residual and cross terms at the relevant depth; none is inferred from density. |
| Arithmetic precision | No numerical approximation was used. | No floating-point or Ritz conclusion enters any theorem. |

These schedules control two inherited error bounds, not the sign of the remaining operator. Even operator-norm errors tending to zero do not certify n(S_delta>1)=0 unless they fit a verified margin or a sign-preserving comparison. Equations (20)–(21) explain why a fixed margin and fixed rank are unavailable before full threshold removal. No monotonicity of the signed S_delta is invoked anywhere.

## 8. Decision and next useful input

**Suspend the bounded endpoint-operator/absolute-relative-tail route in this normalization.** It fails for a structural reason: the known exact null directions are dense in the proposed energy completion, and the signed prime contribution becomes unbounded below there. More precision or another fixed-depth matrix does not repair that defect.

A genuinely different next step would need a **one-sided signed form argument** or a physically compressed comparison that retains the cancellation. On Y, with A_Y the restriction of a and C_Y=P_Y K restricted to Y, the exact missing estimate is

\[
\langle y,C_Yy\rangle\le\mathfrak a[y]
\quad\text{for every }y\in\mathcal V\cap Y.
\tag{22}
\]

To justify further work, specify a factorization or arithmetic estimate producing (22), or an upper-bound approximation valid for all 0<delta<s with a proved remainder after the physical compression. It must tolerate an unbounded negative side and cannot rely on a bounded extension of Pi_Y to the bare energy completion. Equation (22) is recorded as the remaining obligation, not as a new reduction claimed to solve it. Completeness of the known threshold span is not assumed.

This round supplies a scoped obstruction and a decision, as permitted by the handoff. It establishes no RH proof, no subthreshold counterexample, no universal impossibility result for operator approaches, and no ground-profile or determinant convergence. Sonin residuals remain deferred. See the [sequential adversarial review](../reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md) for checks and limitations.
