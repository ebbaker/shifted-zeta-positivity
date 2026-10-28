# Canonical flux bounds, a coupled moment restriction, and the direct comparison

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**. Investigation05 chat0005, **Begin radial collision research**, thread `01a18000-840b-7fd3-96cb-6af456884c05`.

**Status: first bounded RLC-01/RLC-02 return; elementary estimates and a scoped comparison proved in-note, with same-model internal checking.** Every simultaneous real zero satisfies the necessary source-balance inequality

\[
\boxed{a^4P_4(t)>24P_0(t)},\qquad
P_j(t)=\int_0^\infty u^j e^{tu^2}\Phi(u)\,du.
\tag{1}
\]

This gives a uniform, bounded range without multiple zeros, with a completely explicit conservative version below. The projection inequality is generic to positive sources; complete theta estimates instantiate it. The matched direct-u proof has **exactly the same constants and tails**. Separately majorizing the flux boundary and integral instead gives a provably larger residual allowance. These conclusions stop the coordinate-only and separate-absolute-value variants tested here. They do not stop other coupled flux estimates or the event-conditioned RLC-04 route.

No enlargement of previously covered theta regions, global collision exclusion, Newman improvement, or endpoint simplicity theorem is established. There is no literature-priority claim or independent specialist review. This is incremental research, not a manuscript milestone.

The [handoff][handoff] and [current progress register][progress] supply the contract. The [result index][results] and [avoid index][avoid] apply, particularly [collision controls][controls], [target classification][a01], [coordinate comparisons][a03], [scoped conclusions][a07], and [coupled estimation][a12]. We derive a finite moment restriction and decide a specified estimator comparison; we do not count a global reformulation as progress.

## 1. Declared domain and normalization

Fix arbitrary finite parameters

\[
0\le t\le T<\infty,\qquad 0<a_-\le a\le A<\infty.
\tag{2}
\]

All estimates below are derived before numerical choices. Some hold for every real frequency. Retain [Notes01][n01] and [14][n14]'s definitions:

\[
r=e^{2u},\quad u=\tfrac12\log r,\quad
w_t(r)=e^{t\log^2r/4},\quad Q_t=w_t\Delta_3\Theta,
\]
\[
d\nu_t=r^2Q_t(r)\,dr,\qquad S_t(R)=\nu_t([R,\infty)),
\quad
K_a(r)=r^{-1/2}\binom{\cos(au)}{-u\sin(au)},
\]
\[
8(H,H_a)=\int_1^\infty K_a\,d\nu_t.
\tag{3}
\]

The central charge is still \(M_t=16H(t,i)\); it is **not** the moment \(P_0(t)=H(t,0)\) or the exterior flux \(S_t(1)\). The exterior integral is the complete physical observation, with inversion already incorporated. No interior copy is added.

## 2. Complete canonical remainder bounds

We give bounds for either the entire source (m=1), or the remainder after the first N square modes (m=N+1). For integers p>=0 define

\[
q_m=e^{-\pi(2m+1)},\qquad
C_p(m)=\sum_{k\ge0}(m+k)^p q_m^k.
\tag{4}
\]

These are explicit rational functions of q_m. In particular,

\[
C_2(m)=\frac{m^2}{1-q_m}+\frac{2mq_m}{(1-q_m)^2}
       +\frac{q_m(1+q_m)}{(1-q_m)^3},
\quad
C_4(1)=\frac{1+11q+11q^2+q^3}{(1-q)^5},\ q=e^{-3\pi}.
\tag{5}
\]

Since \((m+k)^2\ge m^2+(2m+1)k\), for r>=1,

\[
\sum_{n\ge m}n^pe^{-\pi n^2r^2}
\le C_p(m)e^{-\pi m^2r^2}.
\tag{6}
\]

Choose any \(0<\eta<\pi m^2\), and write

\[
\beta=\pi m^2-\eta>0,\qquad
B=\exp\{T^2/(4\eta e^4)\},\qquad
J_p(R;\beta)=\int_R^\infty s^pe^{-\beta s^2}\,ds.
\tag{7}
\]

Here J_p is a specified positive Gaussian integral, equivalently
\(\frac12\beta^{-(p+1)/2}\Gamma((p+1)/2,\beta R^2)\). Its use requires no numerical enclosure or unresolved sign. The inequalities

\[
\log^2r\le4r/e^2,\quad
Tr/e^2\le\eta r^2+T^2/(4\eta e^4)
\]

give the uniform absorption

\[
w_t(r)e^{-\pi m^2r^2}\le B e^{-\beta r^2}.
\tag{8}
\]

Thus no small-T assumption is hidden in the tail estimate. The first inequality follows by maximizing y^2e^{-y} for y=log r>=0; the second is completion of a square.

Let \(Q^{\ge m}=4\pi\sum_{n\ge m}n^2(2\pi n^2r^2-3)e^{-\pi n^2r^2}\) on r>=1, and let \(d\nu_{t,m}=r^2w_tQ^{\ge m}\,dr\). Every summand is positive there, and

\[
0<\frac{d\nu_{t,m}}{dr}
\le8\pi^2C_4(m)B\,r^4e^{-\beta r^2}.
\tag{9}
\]

Only the upper bound drops the negative polynomial term; the physical source remains the complete sum. Write \(E_{t,m}(R)=\nu_{t,m}([R,\infty))\). The exact flux formula is

\[
E_{t,m}(R)=w_t(R)E_{0,m}(R)
+\frac t2\int_R^\infty\frac{\log s}{s}w_t(s)E_{0,m}(s)\,ds,
\quad E_{0,m}(R)=4\pi R^3\sum_{n\ge m}n^2e^{-\pi n^2R^2}.
\tag{10}
\]

Both terms are retained. With log s<=s/e, equations (6)-(10) imply

\[
E_{t,m}(R)\le\mathcal F_{m,T}(R)
:=4\pi C_2(m)B\left[R^3+\frac{T}{4e\beta^2}(\beta R^2+1)\right]e^{-\beta R^2},
\quad
E_{t,m}(R)\le8\pi^2C_4(m)B J_4(R;\beta).
\tag{11}
\]

Indeed the correction is at most \(4\pi C_2B\,T J_3/(2e)\), and \(J_3=(\beta R^2+1)e^{-\beta R^2}/(2\beta^2)\). One may take the minimum of the two bounds.

For fixed 1<=R<U, exact shell charges and remainders satisfy

\[
q(t;R,U)=S_t(R)-S_t(U)>0,
\quad q_{\rm rem}=E_{t,m}(R)-E_{t,m}(U)\ge0,
\]
\[
w_t(R)[E_{0,m}(R)-E_{0,m}(U)]
\le q_{\rm rem}\le
w_t(U)[E_{0,m}(R)-E_{0,m}(U)].
\tag{12}
\]

This follows directly by integrating w_t against the positive static charge on [R,U]. Adjacent shells share the same E values; (12) is not a set of independent signed endpoint errors. The time correction in (10) remains part of those values. All cuts here are fixed.

## 3. Joint observation tails and complete flux transfer

For any real direction v=(c,d), use \(|c\cos(au)-du\sin(au)|\le\sqrt{c^2+d^2u^2}\) before majorizing. Equations (8)-(9) give

\[
\begin{split}
\left|\int_R^\infty v\cdot K_a\,d\nu_{t,m}\right|
&\le8\pi^2C_4(m)B\int_R^\infty
r^{7/2}\sqrt{c^2+d^2\log^2r/4}\,e^{-\beta r^2}\,dr\\
&\le8\pi^2C_4(m)B
\sqrt{c^2J_{7/2}^2+(d^2/e^2)J_{7/2}J_{9/2}}.
\end{split}
\tag{13}
\]

All J values in (13) have arguments (R;beta). The second step uses Cauchy-Schwarz and u^2<=r/e^2. Divide by eight for the physical observations. This bound retains the joint direction and is uniform in real a, hence on (2). Take m=1 for a spatial outer tail; take R=1 for the full error from omitted square modes.

The exact flux residual transfer, with \(\phi=v\cdot K_a\), is

\[
\int_1^\infty\phi\,d\nu_{t,m}
=cE_{t,m}(1)+\int_1^\infty E_{t,m}(r)\phi'(r)\,dr,
\]
\[
\phi'=-\tfrac12r^{-3/2}
\{(c+da u)\cos(au)+(ca+d(1-u))\sin(au)\}.
\tag{14}
\]

Thus the r=1 residual is present and both components use the same E. For completeness, the weighted flux tails in (14) are explicitly bounded by (11). Put

\[
W_p(R)=4\pi C_2(m)B\left[J_{p+3}
+\frac{T}{4e\beta^2}(\beta J_{p+2}+J_p)\right].
\]

Then \(\int_R^\infty\mathcal F_{m,T}(r)r^pdr=W_p(R)\), and, uniformly for a<=A,

\[
\int_R^\infty E_{t,m}|\phi'|\,dr
\le\tfrac12\{(|c|\sqrt{1+A^2}+|d|)W_{-3/2}(R)
+|d|\sqrt{1+A^2}W_{-1}(R)/e\}.
\tag{15}
\]

This is an available absolute bound, not a claim that splitting (14) improves (13). A tail starting at R instead of one has boundary term \(\phi(R)E_{t,m}(R)\).

Finite t and a derivatives add powers of log r to (9); finite source derivatives add polynomial powers of n and r. The construction (6) with a larger p and a slightly reduced positive Gaussian exponent dominates them uniformly on compact sets. It justifies termwise differentiation, parameter differentiation, all moments below, integration by parts, and vanishing outer boundaries. No finite prefix is used without its remainder. Finite exterior prefixes are not claimed to possess full theta reflection.

## 4. A sharp coupled projection and its collision consequence

The choice \(v_a=(1,-a/2)\) cancels the quadratic term of the observation kernel. For theta>=0 set

\[
G(\theta)=\cos\theta+\tfrac\theta2\sin\theta-1+\theta^4/24.
\]

Direct differentiation gives

\[
G(0)=G'(0)=0,\qquad
G''(\theta)=\tfrac\theta2(\theta-\sin\theta)>0\quad(\theta>0).
\]

Therefore \(G(\theta)>0\) for theta>0. Integrating this **global** kernel inequality against the positive complete source gives

\[
\boxed{H(t,a)-\tfrac a2H_a(t,a)
>P_0(t)-\tfrac{a^4}{24}P_4(t)}\qquad(a>0).
\tag{16}
\]

Strictness holds because the source is positive on u>0. This proves (1). The coefficient 1/24 is optimal for this particular projection, since
\(\cos\theta+(\theta/2)\sin\theta=1-\theta^4/24+O(\theta^6)\). Among kernels \(\cos\theta+b\theta\sin\theta\), b=1/2 is the unique constant canceling the quadratic coefficient. No optimality among all coupled estimates is claimed.

The moment ratio increases with time:

\[
\frac d{dt}\frac{P_4}{P_0}
=\frac{P_6P_0-P_4P_2}{P_0^2}>0.
\tag{17}
\]

The numerator equals
\(\frac12\iint(u^4-v^4)(u^2-v^2)m_t(u)m_t(v)\,du\,dv>0\), with \(m_t=e^{tu^2}\Phi\). Hence the full slab 0<=t<=T has no simultaneous zero in

\[
0<a\le A_4(T):=\left(\frac{24P_0(T)}{P_4(T)}\right)^{1/4}.
\tag{18}
\]

This rules out every finite real multiplicity at least two in that range. It does not rule out ordinary simple zeros there. At a=0, H(t,0)>0 separately. Statement (18) includes t=0 only at the displayed bounded heights; it makes no all-height simplicity claim.

### A completely specified conservative range

The moments in (18) are independent positive source integrals, not unknown event residuals. They also admit explicit unconditional bounds. From the n=1 source on 1<=r<=sqrt(2),

\[
P_0(t)=\tfrac18\int_1^\infty r^{3/2}Q_t\,dr
\ge L_0:=\tfrac\pi2(2\pi-3)(\sqrt2-1)e^{-2\pi}>0.
\tag{19}
\]

Here w_t>=1, r^{3/2}>=1, 2pi r^2-3>=2pi-3 and exp(-pi r^2)>=exp(-2pi). For all integer j>=0, (9) and u^j<=r^{j/2}/e^j give

\[
\frac18\int_R^\infty u^j r^{-1/2}\,d\nu_{t,m}
\le\pi^2C_4(m)B e^{-j}J_{(7+j)/2}(R;\beta).
\tag{20}
\]

Choose m=1, eta=pi/2 and beta=pi/2. Then

\[
P_4(t)\le U_4(T):=\frac{\pi^2C_4(1)}{e^4}
e^{T^2/(2\pi e^4)}J_{11/2}(1;\pi/2).
\tag{21}
\]

Consequently **every** finite T has the explicit range

\[
\boxed{0\le t\le T,\quad
0<a^4\le24L_0/U_4(T)\ \Longrightarrow\ (H,H_a)\ne(0,0).}
\tag{22}
\]

All constants are specified positive numbers or positive Gaussian integrals; no favorable signed constant remains to be established for (22). The coarse bounds are deliberately unoptimized. No numerical evaluation or claim that this enlarges a known theta region is made.

The ordinary positivity estimate \(H>P_0-a^2P_2/2\) excludes all zeros up to \(A_2(T)=(2P_0(T)/P_2(T))^{1/2}\). The ratio P2/P0 also increases with time by the same covariance argument. Their exact comparison is

\[
\frac{A_4(T)}{A_2(T)}
=\left(\frac{6P_2(T)^2}{P_0(T)P_4(T)}\right)^{1/4}.
\tag{23}
\]

Thus the coupled moment radius improves this direct second-moment radius precisely if \(P_0P_4<6P_2^2\). That canonical comparison is not proved here. A sharper estimate is not inferred merely from using both observations.

## 5. Matched direct comparison and the stopped variant

The exact pushforward is

\[
d\nu_t=8e^u m_t(u)\,du,\qquad
K_a(e^{2u})=e^{-u}(\cos(au),-u\sin(au)).
\tag{24}
\]

Every shell, shared endpoint charge, and outer-tail integral in (12)-(15) therefore has the identical direct-u expression with the same source information. In particular, the radial projection giving (16) becomes exactly \(\cos(au)+(au/2)\sin(au)\), with the same constant 1/24. The moments themselves can be acquired from flux:

\[
8P_j=\mathbf1_{j=0}S_t(1)+\int_1^\infty S_t(r)f_j'(r)\,dr,
\quad f_j=r^{-1/2}u^j,
\]
\[
f_0'=-\tfrac12r^{-3/2},\qquad
f_j'=\tfrac12r^{-3/2}(j u^{j-1}-u^j)\quad(j\ge1).
\tag{25}
\]

The sign change of f_4' at u=4 must be retained. A simpler expression for S_0 does not itself improve the resulting moment bound. Equations (20) and (25), including their tails, transport exactly under (24). No evaluation-cost advantage is established.

There is a sharper decision for a particular estimator. For a nonnegative omitted-source measure dnu and its tail E, put phi=v dot K_a, and define the *direct absolute residual allowance* and the *separate flux allowance* by

\[
D_v=\int_1^\infty|\phi|\,d\nu,\qquad
F_v=|c|E(1)+\int_1^\infty E|\phi'|\,dr.
\]

Integrating |phi| against -E', with the same boundary and tail hypotheses as (14), proves the exact identity

\[
\boxed{F_v-D_v
=2\int_{\{\phi\phi'<0\}}E(r)|\phi'(r)|\,dr\ge0.}
\tag{26}
\]

Absolute value is locally Lipschitz, so the integration is valid across zeros. For a>0, v!=0 and any canonical omitted-mode measure, phi is a nonzero analytic function tending to zero, and E>0 everywhere. The absolute value of phi must decrease on an interval. Therefore (26) is strict in this case. This compares error allowances, not the signed physical values or total implementation costs.

**Decision.** A radial rewrite using the same shell information gives the same estimate. Separately bounding the flux boundary and integral for a nonnegative source remainder increases the ideal absolute error allowance. Stop those two variants as claimed routes to a better bound. Signed residuals, different correlated source information, event-conditioned identities, or a demonstrated acquisition-cost reduction lie outside this conclusion.

## 6. Controls, scope and next work

For the exact [Note01][n01] control \(\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2}\), the event is t=T_c and a=2sqrt(6). Gaussian integration gives

\[
P_{0,*}=9\sqrt\pi/4,\qquad P_{4,*}=123\sqrt\pi/256,
\qquad a^4P_{4,*}/P_{0,*}=123>24.
\tag{27}
\]

It passes (1), as a generic necessary condition must. Positivity and Kelvin geometry alone have not excluded its event. Its evolved radial source has log-Gaussian decay,
\(Q_{*,T_c}=4r^{-5/2}(4\log^4r+6)e^{-\log^2r}\), so it fails the canonical Gaussian-in-r envelope (9).

The [registered controls][controls] have the following roles:

| Family | Screen for this return |
| --- | --- |
| Euler-factor controls | Generic moment and transfer inequalities remain valid on their convergence domain. Their source/conductor differ; (4)-(11) are not identities for that changed source. |
| Weighted-square, finite-tail and finite-prime controls | Unit canonical coefficients or full normalized reflection fail. Conservative Gaussian envelopes can still hold; failing the identity is not proof that each upper bound rejects a control. Their local events must satisfy (1). |
| Reflected smooth and positive-primitive controls | The positive-source moment inequality remains valid. The complete canonical integer-square source premise is absent. No auxiliary positivity is used to exclude their events. |
| Finite-profile atomic/compact controls | (16) and (26) have positive-measure versions when moments exist; theta arithmetic/growth fail. Strictness of (16) needs some positive mass away from u=0, which any event source here has. |
| RH-conditional endpoint perturbations | Ordinary canonical Dirichlet arithmetic changes. Closeness does not defeat a generic necessary moment condition or establish a canonical separating margin. |

These are analytic premise checks, using the control register's existing results; no external certificate was rerun. No listed control is rejected merely for satisfying a generic shell enclosure. The explicit event (27) supplies a complete local sanity check, and (26) is compatible with every positive control having the required tails.

The first bounded contract is met by complete bounds (11)-(15), the actual restriction (16)-(22), and the exact equality/loss (24)-(26). The broad RLC-01/02 goals remain open: no theta-specific improvement over the matched direct formulation has been proved. One next bounded question is to prove or disprove the complete-source moment comparison in (23) on a declared time slab, before computing constants. It would measure a generic coupled-projection gain, not a radial gain or a global solution. Alternatively RLC-04 may seek an additional event-conditioned theta relation. No repeat shell optimization is justified by a coordinate change alone.

No numerical work was needed for this return. All constants were checked analytically; separate same-model subagents checked the projection, normalization, tail absorption and control moments. The [assessment][review] records that limited review status. The [chat registry][history] holds current capture provenance; the final reply is captured only after it is actually sent.

[handoff]: 15_RADIAL_LAPLACIAN_COLLISION_PROGRAM_HANDOFF_20261027.md
[progress]: ../research-progress/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_PROGRESS_20261027.md
[review]: ../reviews/09_FLUX_MOMENT_AND_DIRECT_COMPARISON_ASSESSMENT_20261027.md
[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n14]: 14_RADIAL_FLUX_AND_COLLISION_RESTRICTIONS_BRAINSTORM_20261027.md
[history]: ../chat-histories/index.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
