# TND-D-E01 r1: complete-spectrum conditional quadrature realization

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, verified in the local rollout `turn_context`. Direct-branch chat0002, thread `01a1af5d-1362-74c1-9d74-fdfc7572e761`. **E — execution**, immutable request r1. [Exact activation/input record][inputs]; [return record][return]; [sole live register][progress].

**Result: complete at the contracted proof-author conditional-representation scope.** L1–L3 hold for the supplied preparation, the sole D-X1 instrument and the unchanged clock and readout. No failed premise is found within that ideal-operation contract. For every fixed positive \(\omega,\gamma\), every \(0\le t\le1/\gamma\) and every real \(k\),
\[
\boxed{H_{1/2-\gamma t}(k)=H_{1/2}(0)\,[q_+(t,k)-q_-(t,k)].}
\tag{1}
\]
This is a cosine expectation of a density, calibrated by the joint no-count frequency. The theta source, position loader, complete angular ensemble, initial mass calibration and ideal measurement access are supplied. Their intrinsic physical origin, microscopic implementation, collision restrictions and estimating advantages are not obtained. One proof pass and one local correction pass were used; this is not TND-D-E02 or independent specialist assessment.

## 1. Contract and evidence retained

The [issued request][request] and [Decision01][decision] fix all construction choices. All frozen mathematical inputs and the request matched their hashes at activation. The sole mismatch among the 38 manifest entries was a continuation-navigation addition in the live branch register. The input record identifies its current bytes and this resolution. Neither r1 nor its frozen manifest was edited.

| Consumed ingredient | Evidence retained here |
| --- | --- |
| MC11 complete cylinder, domains, Green weight and angular multiplicities | Accepted within scope through [Note05][mc-free] and its internal assessment; shared spectral premises, no specialist review. |
| Canonical source lower bound, finite-order recurrences and complete tails | [Note08 (6)–(14)][mc-source], accepted without correction in [AR-E04 Review05][mc-review]; internal same-model assessment of that source proof. |
| Parent TND-E01 geometric/spectral comparison, normalizations and compact-parameter derivative bounds | [Note02][parent], proof-author comparison work. Shared **TND-E03 r2 remains ready, unactivated** in the [shared register][shared-progress] at this intake. |
| Investigation05 scalar/heat benchmarks | Their recorded same-assistant scope remains; no additional benchmark theorem is imported here. |
| Supplied loader, \(u=v\), \(R\), \(H_{1/2}(0)\), D-X1 and measurement access | Declared ideal model data from Decision01; their mathematical consistency is checked locally below. |
| MC11-OBS-E01, MC11-E05 and other branches | External statuses unchanged. No pending Note13-only measurement or state claim is an accepted input. L1–L3 discharge only this request's local obligations. |

Primary passage checks on 6 November 2026 rechecked [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), at zero argument and positive imaginary lattice parameter, and [Rodgers–Tao v5, Introduction (1)–(4)](https://arxiv.org/html/1801.05914v5#S1), for reflection and canonical source/calibration. The no-count sign and normalization conventions agree with [Castin–Dalibard–Mølmer v1 §1 (4)–(11)](https://arxiv.org/html/0805.4002v1) and [Jacobs–Steck v1 §III (17)–(19)](https://arxiv.org/html/quant-ph/0611067v1). Those articles do not supply the unbounded cylinder/infinite-count proof: §§3–5 do so directly. No zero theorem, diffusive model, general unbounded Lindblad theorem or microscopic dilation theorem is imported. Canonical records remain linked in the [branch source-use index][refs].

## 2. Complete free spectrum and exact domains — E1–E4

Retain \(\mathcal H=L^2(\mathbb R,dv;K)\), \(K=L^2(S^2,\Sigma;d\Omega)\), \(P=-i\partial_v\), \(X=v\), \(A=D^2\), \(\mathcal D_C=\Gamma P+2D\), \(L_0=P^2+4A\), \(H_{\rm kin}=\varepsilon L_0\) and \(U(t)=e^{-i\omega tL_0}\). The metric is \(dv^2+g_{S^2}/4\); multiplication of a product-measure spinor by 2 is its metric-volume isometry. The fixed curvature term \(2\varepsilon\) is already included. These are the inherited operators, without a wall, potential or boundary at zero.

Use the full unitary radial Fourier transform with factor \((2\pi)^{-1/2}\). On each of the \(2n\) angular pairs at every \(n\ge1\),
\[
M_n(k)=\begin{pmatrix}2n&k\\k&-2n\end{pmatrix},\quad
M_n(k)^2=(k^2+4n^2)I,\quad
\Pi_\pm(n,k)=\tfrac12\left(I\pm\frac{M_n(k)}{\sqrt{k^2+4n^2}}\right).
\tag{2}
\]
Both first-order signs \(\pm\sqrt{k^2+4n^2}\), each with multiplicity \(2n\), and all \(k\in\mathbb R\) are retained. The square has multiplicity \(4n\). Generalized modes are not normalizable states. Evenness reduces the square rather than the first-order Dirac operator. These inherited resolutions are those of parent Note02 §§2–3; the apparatus receives no free-energy spectrum by relabeling these branches.

The constituent maximal domains remain exactly
\[
\begin{aligned}
\operatorname{Dom}L_0^p
 &=\left\{\psi\in\mathcal H:\sum_{n\ge1}\int_{\mathbb R}
 (k^2+4n^2)^{2p}\|P_n\widehat\psi(k)\|^2dk<\infty\right\},\\
\operatorname{Dom}\mathcal D_C
 &=\left\{\psi\in\mathcal H:\sum_{n\ge1}\int_{\mathbb R}
 (k^2+4n^2)\|P_n\widehat\psi(k)\|^2dk<\infty\right\},\\
\operatorname{Dom}X^q&=\{\psi\in\mathcal H:|v|^q\psi\in L^2\},\qquad
\operatorname{Dom}P^q=\{\psi\in\mathcal H:|k|^q\widehat\psi\in L^2\}.
\end{aligned}
\tag{3}
\]
Here \(p,q\) are arbitrary fixed nonnegative integers. In particular
\(\operatorname{Dom}L_0=\operatorname{Dom}P^2\cap\operatorname{Dom}A\), since its positive commuting multipliers give \(\|P^2\psi\|\le\|L_0\psi\|\), \(4\|A\psi\|\le\|L_0\psi\|\), and the converse follows by addition.

Let \(\mathscr C=\mathcal S(\mathbb R)\otimes K_{\rm fin}\), with finite linear sums understood. Free Fourier multiplication preserves this core and maps it onto itself. In Fourier variables, conjugating \(i\partial_k\) by \(e^{-i\omega t(k^2+4n^2)}\) gives
\[
Q_t:=U(t)XU(t)^*=X-2\omega tP\quad\hbox{on }\mathscr C,\qquad
\operatorname{Dom}Q_t^q=U(t)\operatorname{Dom}X^q.
\tag{4}
\]
Since \(\mathscr C\) is a core for \(X^q\) and is invariant under \(U(t)\), it is a core for the conjugated powers; (4) therefore specifies the closure, rather than an unproved domain for a formal differential sum. In particular no equality with \(\operatorname{Dom}X\cap\operatorname{Dom}P\) is asserted. The inherited compactly supported smooth radial/finite-angular core remains a core for the free constituents. Finite angular support is used only in approximation.

Because \(U(t)\) preserves \(\operatorname{Dom}L_0\), the strong-law domain is precisely
\[
\mathcal D_t=\operatorname{Dom}L_0\cap\operatorname{Dom}Q_t^2
=U(t)(\operatorname{Dom}L_0\cap\operatorname{Dom}X^2).
\tag{5}
\]
No assertion enlarges this to a maximal domain of \(H_{\rm eff}\), or makes that non-Hermitian expression self-adjoint.

## 3. L1: square-root source and full-spectrum preparation — E5–E8

Write \(r=|v|\), \(x=\pi e^{4r}\), \(\kappa=2-3/\pi>0\). On \(v\ge0\), keep the complete source
\[
\Phi(v)=e^v\sum_{n\ge1}(2n^4x^2-3n^2x)e^{-n^2x},\qquad
\kappa e^v x^2e^{-x}\le\Phi(v).
\tag{6}
\]
For the full derivative bounds, use Note08 and parent Note02 (27)–(29):
\[
\begin{gathered}
H_0(x)=2x^2-3x,\quad H_{j+1}=(1-4x)H_j+4xH'_j,\quad\deg H_j=j+2,\\
C_d(N)=\sum_{n>N}n^{2d}e^{-\pi(n^2-1)}\longrightarrow0,\quad
B_j=A_{H_j}C_{j+2}(0),\\
\left|e^v\sum_{n>N}e^{-n^2x}H_j(n^2x)\right|
\le A_{H_j}C_{j+2}(N)e^v x^{j+2}e^{-x}.
\end{gathered}
\tag{7}
\]
Here \(A_H\) is the finite sum of absolute polynomial coefficients. The same bound pays the absolute summand sum. Gaussian summability proves finiteness and decay of \(C_d(N)\) at every fixed order.

The source is the complete canonical smooth even extension. Explicitly DLMF 20.7.32 gives, for \(p(v)=e^vQ_1(\pi e^{4v})\),
\(p(v)-p(-v)=-\sinh v\). The full series is smooth on each compact real interval because its damping parameter has a positive lower bound there. Applying \((\partial_v^2-1)/8\) proves smooth evenness of \(\Phi\), including at zero. Reflection transfers (6)–(7) as absolute bounds to \(r=|v|\). This is not differentiation of reflected finite truncations. Strict positivity on both half-lines and at zero makes the positive square root smooth and even, with every odd derivative zero at zero.

The square-root step needs a new estimate. Set \(h=\sqrt\Phi\), \(a_\ell=\Phi^{(\ell)}/\Phi\). The matching lower and upper exponents yield
\[
|a_\ell(v)|\le (B_\ell/\kappa)x^\ell,\qquad
a_\ell'=a_{\ell+1}-a_\ell a_1.
\tag{8}
\]
Define finite polynomials
\[
S_0=1,\qquad
S_{j+1}=\tfrac12 a_1S_j+
\sum_{\ell=1}^{j}\frac{\partial S_j}{\partial a_\ell}
(a_{\ell+1}-a_\ell a_1).
\tag{9}
\]
Induction gives \(h^{(j)}=hS_j\). Each monomial has weighted degree \(j\), assigning weight \(\ell\) to \(a_\ell\). Evaluating the absolute coefficient polynomial at \(B_\ell/\kappa\) gives a finite constant \(c_j\), so
\[
|h^{(j)}(v)|\le\sqrt{B_0}\,c_j
e^{r/2}x^{j+1}e^{-x/2}.
\tag{10}
\]
Thus denominator differentiation retains half the double-exponential decay; source Schwartz membership alone was not used to infer square-root membership.

For \(|\lambda|\le1/2\), put
\[
F_\lambda=e^{\lambda v^2}\Phi,\quad
Z_\lambda=\int_{\mathbb R}F_\lambda=2H_\lambda(0),\quad
z_-:=Z_{-1/2}\le Z_\lambda\le Z_{1/2}=:z_+.
\tag{11}
\]
Here \(z_+<\infty\) follows from (7). A positive lower payment is
\[
z_-\ge2\kappa\int_0^1e^{-v^2/2+v}(\pi e^{4v})^2e^{-\pi e^{4v}}dv>0.
\tag{12}
\]
Consequently \(f_\lambda=Z_\lambda^{-1/2}e^{\lambda v^2/2}h\) is well defined and normalized in the full-line measure.

For spatial derivatives of its exponential factor use
\(T_0=1\), \(T_{j+1}=\partial_vT_j+\lambda vT_j\), so
\(\partial_v^je^{\lambda v^2/2}=e^{\lambda v^2/2}T_j\).
Finite Leibniz summation with (10) gives controlled order-dependent constants \(D_j\):
\[
|\partial_v^jf_\lambda(v)|\le D_j(1+r)^j x^{j+1}
\exp(v^2/4+r/2-x/2).
\tag{13}
\]
Every polynomially weighted supremum and integral of this majorant is finite, uniformly on the slab: substitution \(x=\pi e^{4r}\) leaves a fixed power of \(x\), powers of \(\log(x/\pi)\), a log-squared exponential and \(e^{-x/2}\). The latter dominates them. This proves every fixed Schwartz seminorm, weighted \(L^2\) norm and radial kinetic moment. Constants depend on the orders, never uniformly on all orders.

Parameter derivatives are paid as well. For each finite \(a\),
\(Z_\lambda^{(a)}=\int v^{2a}F_\lambda(v)dv\), by parent Note02's \(J\)-majorants, and \(\partial_\lambda^ae^{\lambda v^2/2}=(v^2/2)^ae^{\lambda v^2/2}\). Derivatives of \(Z^{-1/2}\) are controlled by (12) and a finite recurrence: put \(b_\ell=Z^{(\ell)}/Z\), use \(b_\ell'=b_{\ell+1}-b_\ell b_1\), and replace the first coefficient \(1/2\) in (9) by \(-1/2\). Finite Leibniz summation therefore bounds mixed derivatives by (13) with \((1+r)^{2a+j}\) and a new finite constant. All parameter differentiations below hold in the required Schwartz or weighted \(L^2\) norms, one-sided at slab endpoints.

The supplied angular ensemble has the complete per-state weights
\[
r_n=\frac{e^{-\pi n^2}}{4nQ_1(\pi)}>0,\quad
R=\sum_{n\ge1}r_nP_n,\quad
\operatorname{Tr}R=\sum_{n\ge1}4nr_n=1,
\tag{14}
\]
and for every fixed nonnegative moment order \(b\),
\(\operatorname{Tr}(A^bR)=Q_1(\pi)^{-1}\sum n^{2b}e^{-\pi n^2}<\infty\).
The \(4n\) consists of both signs and \(2n\) states per sign. The count labels introduce no angular degeneracy. This is an angular preparation, not a full-cylinder Gibbs state.

For \(\rho^I_\lambda=|f_\lambda\rangle\langle f_\lambda|\otimes R\), the exact finite binomial payment is
\[
\begin{aligned}
&\sum_{n\ge1}4nr_n\int_{\mathbb R}(k^2+4n^2)^{2p}|\widehat f_\lambda(k)|^2dk\\
&=\frac1{Q_1(\pi)}\sum_{j=0}^{2p}\binom{2p}{j}4^{2p-j}
\|P^jf_\lambda\|_2^2\sum_{n\ge1}n^{4p-2j}e^{-\pi n^2}<\infty.
\end{aligned}
\tag{15}
\]
Tonelli, the finite expansion and Plancherel justify every equality. This defines the positive trace-class quadratic-form sandwich \(L_0^p\rho^I_\lambda L_0^p\), equivalently the convergent sum of the weighted rank-one vectors. It is not a claim that every vector in the closed support of \(\rho^I_\lambda\) belongs to the domain. The ensemble vectors themselves have all specified finite domains.

Angular tails are the actual positive Gaussian sums over \(n>N\) in (14)–(15). For every fixed \(j,M\) and \(K>0\), radial tails satisfy
\[
\int_{|k|>K}|k|^{2j}|\widehat f_\lambda(k)|^2dk
\le K^{-2M}\|P^{j+M}f_\lambda\|_2^2.
\tag{16}
\]
Together these pay the full weighted spectral limits uniformly in \(\lambda\) for each specified finite order, without using a final cutoff. **L1 is established.**

## 4. L2: complete count instrument, composition and strong law — E9–E10

Throughout this section \(0\le s\le t\le T=1/\gamma\). For \(a=\gamma(t-s)>0\) write
\(B_j(a)=e^{-aX^2/2}(\sqrt aX)^j/\sqrt{j!}\) and
\(K_j(t,s)=U(t)B_j(a)U(s)^*\), with the request's \(B_0(0)=I\), \(B_{j>0}(0)=0\). Functional calculus gives
\[
\|B_0(a)\|=1,\qquad
\|B_j(a)\|^2=\frac{j^je^{-j}}{j!}\le1\quad(j\ge1).
\tag{17}
\]
The maximum occurs at \(av^2=j\); the inequality follows since each term of the Poisson sum is at most its sum. Odd \(j\) keeps the sign of \(v^j\). No absolute-value replacement is made to the Kraus amplitude. Dominated convergence proves the stated strong zero-duration limits of every \(B_j\), hence every \(K_j\), with the moving unitaries included. There is no operator-norm continuity or operator-norm Taylor expansion at zero.

For \(y\ge0\), define \(c_N(y)=e^{-y}\sum_{j=0}^Ny^j/j!\). The exponential series converges by the ratio test; its positive terms give \(0\le c_N\uparrow1\). More explicitly, for \(0\le y\le R\) and \(N+2\ge2R\), its remaining terms have successive ratio at most \(1/2\), whence
\[
0\le1-c_N(y)\le\frac{2R^{N+1}}{(N+1)!}.
\tag{18}
\]
The spectral measure of any fixed vector, dominated by 1, now proves
\[
\sum_{j=0}^NK_j(t,s)^*K_j(t,s)
=U(s)c_N(aX^2)U(s)^*\ \xrightarrow{\rm strong}\ I.
\tag{19}
\]
Thus all outcomes are retained. The bounded-spectral estimate (18) plus the remaining vector spectral mass is also an explicit proof of this limit.

For positive trace-class \(\rho\), use its positive spectral decomposition to obtain
\[
\operatorname{Tr}\!\left[\rho\left(I-\sum_{j=0}^NK_j^*K_j\right)\right]\longrightarrow0.
\tag{20}
\]
Scalar dominated convergence applies to each vector term and then to the summable eigenvalue weights. Positive output partial sums have uniformly bounded trace; their differences have trace norm equal to their trace. They therefore converge in trace norm, and the resulting channel \(\mathcal T_{t,s}(\rho)=\sum_jK_j\rho K_j^*\) has the same trace as \(\rho\). Equivalently \(V_{t,s}\psi=(K_j\psi)_{j\ge0}\) is an isometry into \(\bigoplus_j\mathcal H\), by (19); taking its count diagonal gives the same operation. This explicit isometry justifies complete positivity and a bounded extension to trace class, also after every finite matrix amplification. Subsets of counts give countably additive trace-norm instrument operations. It is an abstract outcome-space construction; no physical spinor multiplicity or microscopic apparatus model is inferred from it.

For \(r\le s\le t\), set \(a=\gamma(t-s)\), \(b=\gamma(s-r)\), \(c=a+b\). If \(c>0\), with \(J=j+\ell\), direct bounded multiplication gives
\[
K_j(t,s)K_\ell(s,r)
=\sqrt{\binom Jj}\,(a/c)^{j/2}(b/c)^{\ell/2}K_J(t,r).
\tag{21}
\]
When one duration is zero use the endpoint convention; nonzero terms have the corresponding count zero. For each \(J\), the sum of squared coefficients in (21) is 1 by the binomial theorem. Hence summing sequential operations over \(j+\ell=J\) gives exactly \(K_J(t,r)\rho K_J(t,r)^*\). Summing over \(J\), positivity and trace-norm convergence allow regrouping, proving
\(\mathcal T_{t,s}\mathcal T_{s,r}=\mathcal T_{t,r}\), together with count aggregation. In particular \(K_0(t,s)K_0(s,r)=K_0(t,r)\). The \(c=0\) case is the identity interval directly.

For the strong equation, take exactly \(\psi\in\mathcal D_s\) and put
\(\chi=U(s)^*\psi\in\operatorname{Dom}L_0\cap\operatorname{Dom}X^2\).
For \(m_a(v)=e^{-av^2/2}\),
\[
m'_a=-avm_a,\quad m''_a=(a^2v^2-a)m_a,\qquad
\|m'_a\|_\infty\le\sqrt{a/e},\quad
\|m''_a\|_\infty\le(1+2/e)a.
\tag{22}
\]
The weak product rule, first on the core then in \(H^2(\mathbb R;K)\), gives
\[
L_0(m_a\chi)=m_aL_0\chi-2m'_a\partial_v\chi-m''_a\chi,
\qquad X^2m_a\chi=m_aX^2\chi.
\tag{23}
\]
Angular multiplication commutes with \(m_a\). Since \(\chi\in\operatorname{Dom}P^2\) also has \(\partial_v\chi\in L^2\), these formulas prove preservation of both constituent domains. At \(a\downarrow0\), (22), strong multiplier convergence and (23) prove convergence in their two graph norms. At positive \(a\), bounded multiplier domination on a compact neighborhood gives the same graph continuity. No mixed \(XP\)-domain hypothesis is inserted.

For admissible \(a,a+h\ge0\), the scalar mean-value bound is
\(|(m_{a+h}-m_a)/h|\le v^2/2\). Thus on \(\operatorname{Dom}X^2\), dominated convergence proves
\[
\partial_a(m_a\chi)=-\tfrac12X^2m_a\chi
\quad\hbox{strongly, one-sided at }a=0.
\tag{24}
\]
Independently, full spectral calculus proves
\(\partial_tU(t)\eta=-i\omega L_0U(t)\eta\) on \(\operatorname{Dom}L_0\): the difference quotient is dominated by \(\omega(k^2+4n^2)\), square-integrable with the domain weight in (3). Taking the product difference quotient, with (23)–(24), yields
\[
\begin{gathered}
K_0(t,s)\mathcal D_s\subseteq\mathcal D_t,\\
\partial_tK_0(t,s)\psi
=\left[-i\omega L_0-\frac\gamma2Q_t^2\right]K_0(t,s)\psi.
\end{gathered}
\tag{25}
\]
This is exactly the contracted strong law and effective Hamiltonian
\(H_{\rm kin}-i\hbar\gamma Q_t^2/2\), with \(C_t=\sqrt\gamma Q_t\). The equality of the laboratory attenuation term follows from \(Q_t^2U(t)=U(t)X^2\) on its declared domain. All propagators exist boundedly on all \(\mathcal H\); the strong equation is claimed on (5).

For fixed \(s<T=1/\gamma\), (25) has the right derivative at \(t=s\), the left derivative at \(t=T>s\), and both interior derivatives. The singleton interval \(s=t=T\) prescribes \(K_0(T,T)=I\); it has no nontrivial fixed-\(s\) derivative within the slab. The initial/final domains in (25) make this endpoint qualification precise. The prepared family satisfies the same law by §3: each angular ensemble vector is in the initial domain, the weighted sum of its squared \(L_0\) norms is finite by (15), and its \(X^2\) norm is finite by (13). Conjugation transfers these statements to the \(Q_t^2\) graph domain. **L2 is established.**

## 5. L3: conditioning, half-factor tangent and absolute readout — E11–E15

The preparation is loaded once:
\(\rho_* = |f_{1/2}\rangle\langle f_{1/2}|\otimes R\).
With \(\lambda(t)=1/2-\gamma t\), multiplication in the interaction frame gives exactly
\[
m_{\gamma t}f_{1/2}
=\sqrt{Z_{\lambda(t)}/Z_{1/2}}\,f_{\lambda(t)}.
\tag{26}
\]
Consequently
\[
\widetilde\rho_t=K_0(t,0)\rho_*K_0(t,0)^*
=p_tU(t)\rho^I_{\lambda(t)}U(t)^*,\quad
p_t=\frac{Z_{\lambda(t)}}{Z_{1/2}}
=\frac{H_{\lambda(t)}(0)}{H_{1/2}(0)}\in(0,1].
\tag{27}
\]
Positivity and finiteness follow from (11)–(12); the upper bound follows also from \(0\le m_{\gamma t}^2\le I\). In particular \(p_0=1\), and \(p_{1/\gamma}=Z_{-1/2}/Z_{1/2}>0\). Dividing by \(p_t\) gives the normalized conditional state. Its theta density is the distribution of \(Q_t\), equivalently interaction-frame position. Free dispersion does not generally preserve that density in laboratory position \(X\). The angular ensemble remains complete and is a spectator to this filtering; \(R\) commutes with angular free evolution.

Let \(\mu_2(\lambda)=\int v^2|f_\lambda(v)|^2dv=Z'_\lambda/Z_\lambda\).
The parameter differentiability already proved gives
\[
\partial_tp_t=-\gamma p_t\mu_2(\lambda(t)),\qquad
\partial_tf_{\lambda(t)}
=-\frac\gamma2[X^2-\mu_2(\lambda(t))]f_{\lambda(t)}.
\tag{28}
\]
Both terms and the half factor are necessary: differentiating \(e^{\lambda v^2/2}\) gives \(v^2/2\), while differentiating \(Z_\lambda^{-1/2}\) subtracts \(\mu_2/2\). The same moment bounds justify these strong derivatives and their endpoint versions. There is no linear-source-amplitude evolution hidden in this normalized tangent.

For every real \(k\), real spectral calculus gives
\[
O_t(k)=\cos(kQ_t)=U(t)\cos(kX)U(t)^*,\qquad
E_\pm(t,k)=(I\pm O_t(k))/2,\quad 0\le E_\pm\le I.
\tag{29}
\]
In particular \(\|O_t(k)\|\le1\); its effects sum to \(I\). All products with \(\widetilde\rho_t\) are trace class, and cyclicity uses only bounded unitary/effect factors. Tonelli for \(R\), followed by absolute integrability of \(F_\lambda\), gives
\[
\begin{aligned}
\operatorname{Tr}(\rho_tO_t(k))
&=\operatorname{Tr}(\rho^I_\lambda\cos(kX))
=\int_{\mathbb R}\frac{F_\lambda(v)}{Z_\lambda}\cos(kv)dv\\
&=\frac{2H_\lambda(k)}{Z_\lambda}
=\frac{H_\lambda(k)}{H_\lambda(0)}.
\end{aligned}
\tag{30}
\]
The trace of \(R\) is exactly one, with all channels counted. Conditional successful samples alone therefore determine the normalized ratio.

The joint outcome effects on the initial state are \(K_0(t,0)^*E_\pm(t,k)K_0(t,0)\). Their sum is \(K_0^*K_0\le I\), so they and the remaining effect \(I-K_0^*K_0\) form a three-outcome measurement, equivalently the post-success effects plus all failed count outcomes. Hence
\[
\begin{gathered}
q_\pm(t,k)=\operatorname{Tr}(\widetilde\rho_tE_\pm(t,k))
=\tfrac12\left[p_t\pm\frac{H_\lambda(k)}{H_{1/2}(0)}\right]\ge0,\\
q_++q_-=p_t,\qquad q_{\rm fail}=1-p_t,\qquad
H_\lambda(k)=H_{1/2}(0)(q_+-q_-).
\end{gathered}
\tag{31}
\]
The displayed nonnegativity follows directly from the effects, also from \(|H_\lambda(k)|\le H_\lambda(0)\). Equation (31) proves (1), with the supplied absolute calibration retained. At \(k=0\), \(q_+=p_t\), \(q_-=0\), confirming the full-line factor. At \(t=1/(2\gamma)\), \(\lambda=0\), so the observation is the unchanged \(H_0(k)=\xi((1+ik)/2)/8\), exactly the normalization in Rodgers–Tao v5 Introduction (1)–(4). No assertion about its zeros is used.

To separate the observed object from amplitudes, the even density has
\[
\widehat{|f_\lambda|^2}(k)=\sqrt{2/\pi}\,H_\lambda(k)/Z_\lambda,
\qquad \int|f_\lambda(v)|^2\cos(kv)dv=2H_\lambda(k)/Z_\lambda.
\tag{32}
\]
Neither \(\widehat f_\lambda\) nor \(|\widehat f_\lambda|^2\) is that source readout. This also checks the Fourier versus cosine normalization independently of the probability algebra. **L3 is established.**

## 6. Complete limits, parameter scope and controls

Every spatial/source derivative above uses the finite recurrence (7) or (9), and complete source tails \(C_d(N)\to0\). Positive normalization is bounded below by (12). The square-root majorant (13), the exact moment payment (15) and radial bound (16) pay all angular/radial preparation and domain limits. A reflected partial source need not be smooth at zero; none was differentiated there. Full reflection supplies the origin statements separately.

For the source transform and its finite \(\lambda,z\) derivatives, use parent Note02 (30)–(34) at \(M=1/2\). In the present notation, for every fixed \(r,d\) and \(b\ge0\),
\[
J_{r,d}(1/2,b)=\int_{\mathbb R}|v|^r
e^{v^2/2+(b+1)|v|}x^de^{-x}dv<\infty.
\tag{33}
\]
Substitution \(x=\pi e^{4|v|}\) proves this by domination of every fixed log-squared/polynomial factor by \(e^{-x}\). The same bound multiplied by \(A_{H_j}C_{j+2}(N)\) pays integrated full-source tails at each fixed order. Thus, on compact complex readout sets, source integration and differentiation commute, for example
\[
\partial_\lambda^a\partial_z^bH_\lambda(z)
=\tfrac12\int_{\mathbb R}v^{2a}(iv)^bF_\lambda(v)e^{izv}dv.
\tag{34}
\]
For each fixed order this proves entire continuation in \(z\); it introduces no bounded \(\cos(zQ_t)\) measurement for nonreal \(z\). The raw scalar \(G\) integral retains its inherited initial strip \(|\operatorname{Im}z|<1\), and is not substituted for (34). No infinite Taylor expansion in operator order or parameter is used. The only infinite expansion in the instrument is proved separately by the positive exponential series (18)–(20). No uniform derivative-order, all-height, infinite-time or \(\gamma\downarrow0\) estimate is asserted.

Under [avoid/01][a01] this is a **physical interpretation/representation theorem conditional on supplied preparation and ideal apparatus**. The [result index][results], [theta/source cluster][theta], [control register][controls] and [patterns index][avoid] limit its interpretation, particularly [re-realizations][a03], [normalization][a08] and [scoped exclusions][a07]. The following is the inherited analytical premise screen, without new control computations.

| Control class | Exact premise absent; construction that can survive |
| --- | --- |
| Euler-factor sources | Fail the unchanged canonical arithmetic source. Their smooth positive source preparations can still admit generic count filtering and cosine readout on an admissible slab; recorded positive-time witnesses are not excluded. |
| Weighted-square and finite-prime perturbations | Fail complete unit weights/full canonical reflection. Positive half-line formulas or finitely matched endpoints do not establish the smooth full-line square-root premise at zero. Applicable generic filtering identities survive. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Fail the exact complete theta arithmetic expansion. Applicable positive smooth preparation, reflection/tails and cosine identities survive; this proof supplies no separating signed estimate. |
| Atomic/finite-profile and continuous nonsmooth controls | Their Fourier/moment observations can survive, while this smooth square-root/domain hypothesis fails or needs a separate check. A smooth replacement must meet its own tails and preparation interval; no universal failure or exclusion is inferred. |

No control is required to violate the generic instrument identities: those are not collision-excluding hypotheses. Positivity of the source, \(p_t\), the angular state and the instrument is compatible with zero or colliding signed cosine expectations. Gaussian-tail replacement sources need their own admissible slab; no blanket extension to them is made. Naming theta as the input identifies the target but supplies no quantitative signed gain.

## 7. Claim-by-claim disposition and bounded correction record

Equation labels E1–E15 below refer to immutable request r1, not this note's numbering. “Proved here” means proof-author scope, conditional on the declared supplied data and the inherited inputs at their recorded levels.

| Request claim | Disposition | Proof and precise scope |
| --- | --- | --- |
| E1 | Inherited/reused | §2, (2)–(3); original free cylinder, units and complete signed spectra. No new free-Hamiltonian derivation. |
| E2 | Inherited/reused | §2 (3); maximal weighted direct-integral domains for every fixed \(p\), and first-order weight. |
| E3 | Reused spectral/multiplication domains | §2 (3)–(4); maximal \(X,P\) powers, full line. |
| E4 | Proved here from inherited domains | §2 (4)–(5), §4 (22)–(25); conjugated quadrature domain and propagation \(\mathcal D_s\to\mathcal D_t\). |
| E5 | Supplied source definition; well-definedness proved | §3 (6)–(13); positive normalized square root, full-line \(Z=2H(0)\), compact-slab smoothness. |
| E6 | Supplied ensemble/preparation; well-definedness proved | §3 (14)–(15); positive trace-one \(R\) with both signs and all multiplicities. |
| E7 | Inherited accepted lower bound, reused | §3 (6); ground term with \(\kappa=2-3/\pi\), extended using full smooth reflection. |
| E8 | Proved here | §3 (15)–(16); complete finite-order quadratic-form trace and paid angular/radial tails. No claim about every support vector. |
| E9 | Supplied instrument; consistency proved | §4 (17)–(21); every signed Kraus amplitude bounded, all counts complete, trace-norm CP instrument, count/channel composition. |
| E10 | Proved here | §4 (22)–(25); no-count cocycle and strong law on the declared domains, with genuine one-sided endpoints. |
| E11 | Well-defined | §5 (26)–(27); positive trace-class no-count output, positive success probability and normalized conditional state. |
| E12 | Proved here | §5 (27); exact conditional family and success mass, including both temporal endpoints. |
| E13 | Proved here | §5 (28); half-factor and normalization subtraction, strong finite-moment tangent. |
| E14 | Supplied access; probabilities proved | §5 (29)–(31); all real \(k\), bounded cosine effects and joint success/outcome probabilities. |
| E15 | Proved here | §5 (30)–(32); exact absolute \(H\) calibration, density Fourier normalization and \(H_0=\xi/8\) check. |
| L1 | Complete local proof | §3; square-root ratios and finite recurrences, origin reflection, normalization, full-spectrum moments. |
| L2 | Complete local proof | §4; spectral-calculus limits and trace convergence, composition, graph preservation and strong law. |
| L3 | Complete local proof | §5; normalized tangent, success mass, bounded effects and absolute observation. |

**One proof pass:** root derived the normalized-state/readout calculation and integrated two disjoint read-only Sol supporting derivations, L1 and L2. Root alone writes repository artifacts and captures the chat. The supporting agents share the root model and inherited premises; they are proof-author assistance, not independent assessment.

**One local correction pass:** checked the square-root exponent/ratio payment, \(4n\) angular normalization, signed odd-count amplitude, binomial squared coefficients, graph continuity at zero duration, full-line Fourier/cosine factors, half-factor tangent, and the temporal/readout endpoints. The retained local clarifications spell out the interval and prepared-vector domain payment, and that (25) starts with \(\psi\in\mathcal D_s\) and lands in \(\mathcal D_t\); a fixed-\(s\) derivative is not asserted on the singleton \(s=t=T\). This is a domain/endpoint exposition clarification within r1, not a change of construction or request. No failed mathematical claim required a substitute source, controller, clock or readout. No second proof/assessment pass, numerics, manuscript or successor execution was performed.

## 8. Continuation boundary

The finite contract succeeds conditionally at proof-author level. Intrinsic theta preparation, resource-bounded engineering, a collision restriction and a gain over direct source analysis remain outside it. L1–L3 do not change external MC11 statuses. No result-summary promotion or investigation closure is made before the required assessment.

**Next prerequisite: [E] TND-E03 r2 — Sol**, the existing shared assessment, ready but unactivated. It must dispose of inherited parent E01 claims once. **Then [E] TND-D-E02 — Sol**, still pending and unactivated, assesses this realization with that shared disposition. The [continuation/model-change handoff][continuation] gives the reading order and pasteable prompt. A model change transfers context and does not upgrade evidence. A changed physical construction returns to TND-D-B01; a useful estimating target remains TND-D-B02 after E02.

[inputs]: ../research-progress/handoffs/02_TND_D_E01_R1_INPUT_VERSIONS_20261106.json
[return]: ../research-progress/handoffs/02_TND_D_E01_R1_RETURN_RECORD_20261106.json
[progress]: ../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[request]: ../research-progress/handoffs/02_TND_D_E01_R1_REQUEST_20261106.md
[decision]: ../brainstorm/notes/01_TND_D_B01_CONDITIONAL_QUADRATURE_DECISION_20261106.md
[parent]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[shared-progress]: ../../research-progress/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[mc-free]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md
[mc-source]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[mc-review]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[refs]: ../references/README.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[continuation]: ../research-progress/handoffs/02_TND_D_E01_R1_RETURN_AND_MODEL_CONTINUATION_20261106.md
