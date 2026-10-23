# Signed Laguerre transfer and a paid zero-count bound

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), reasoning effort ultra**, verified by the parent from this research turn's metadata. **Status: proved in-note; separate same-model internal proof audit completed.** No theta sign, event exclusion, or later collision is established.

[Note 08][n08] proves complete bounds for
\(W(F;U)=2\int_U |F'|^2/|F|\,dA\), including multiple zeros. This note gives a concrete transfer to the signed Laguerre consumer already defined in [BW09 Note 05][bw05], plus a zero-count upper bound with its necessary boundary-amplitude payment. The transfer is a useful error estimate, rather than a completed signed theta estimate. All observations and bounds are available to the matched direct comparator.

Read the [result index][results], [collision controls][controls], and [avoid index][avoid], especially patterns 01, 02, 07, 08 and 12. The existing [root-wall count][bw03], [Gaussian and level-cap payments][bw06], and [signed phase-surplus program][bwprogram] retain their prior scopes and unresolved gates.

## 1. A root-free finite-segment trace transfer

Let \(I=[a,b]\) have length \(\ell\), and let \(U_\delta=\{z:\operatorname{dist}(z,I)<\delta\}\), \(\delta>0\). Let \(F\) be holomorphic on a neighborhood of its closure, and put \(M_F=\sup_{U_\delta}|F|\), \(W_F=W(F;U_\delta)\). An identically zero field has \(W_F=0\). Then

\[
\boxed{\quad
\int_I |F'(x)|^2dx\le \frac{M_F W_F}{\pi\delta}.
\quad} \tag{1}
\]

**Proof.** Apply the submean inequality to the holomorphic function \(F'\):
\(|F'(x)|^2\le(\pi\delta^2)^{-1}\int_{D(x,\delta)}|F'(z)|^2dA_z\).
A limiting smaller radius handles tangency to the collar boundary. Integrate in \(x\); for any fixed \(z\), the set of centers \(x\in I\) whose disk contains \(z\) has length at most \(2\delta\). Therefore

\[
\int_I|F'|^2\le\frac2{\pi\delta}\int_{U_\delta}|F'|^2dA
\le\frac{M_F}{\pi\delta}W_F.
\]

No lower bound for \(F\), \(F'\), a root separation, or a jet is used. In particular we apply submean to \(|F'|^2\), not to the singular quotient \(|F'|^2/|F|\). \(\square\)

The same pointwise-in-time result applies to prescribed moving intervals and collars, with their own constants. Integrating a bound in time adds no moving-boundary derivative because no transport derivative is being asserted.

## 2. A complete signed-functional error bound

Let \(H,P\) be holomorphic near \(\overline U_\delta\), real on \(I\), and let \(\psi\in C_c^2((a,b);\mathbb R)\). Define the existing BW09 functional

\[
A_\psi(F)=\int_I\psi(F'^2-FF'')dx
=2\int_I\psi F'^2dx-\tfrac12\int_I\psi''F^2dx.
\tag{2}
\]

Compact support pays every integration-by-parts endpoint term. Put \(D=H-P\), \(S=H+P\), and define their \(M\) and \(W\) constants as in Section 1. Then

\[
\boxed{\begin{aligned}
|A_\psi(H)-A_\psi(P)|\le \mathcal R_W:={}&
\frac{2\|\psi\|_\infty}{\pi\delta}
 \sqrt{M_D M_S W_D W_S}\\
&+\frac12\|\psi''\|_{L^1(I)}M_D M_S.
\end{aligned}} \tag{3}
\]

**Proof.** The exact difference is
\(2\int\psi D'S'-(1/2)\int\psi''DS\). Apply Cauchy--Schwarz to the first integral, use (1) separately for \(D,S\), and use \(|DS|\le M_DM_S\) in the second. Both signs and the full signed potential term in (2) are retained. \(\square\)

Thus any established enclosure \(A_\psi(P)\in[L_P,U_P]\) gives

\[
A_\psi(H)\in[L_P-\mathcal R_W,U_P+\mathcal R_W]. \tag{4}
\]

This is root-free even when either field has a multiple zero. If a fixed nonnegative \(\psi\) and prescribed time/window eventually give \(U_P+\mathcal R_W<0\), then \(Q_H<0\) somewhere on the support. That is the existing BW09/BW05 direct Laguerre-violation consumer; the **new established content is the complete error transfer (3)**. No such negative value is acquired here, and the estimate does not itself force the extra real cap pair required by BW09's later-collision contour.

For \(\psi\ge0\), the same trace bound also gives a direct finite enclosure: if \(B=-\tfrac12\int\psi''H^2\in[B_-,B_+]\), then

\[
 B_-\le A_\psi(H)\le B_++
 \frac{2\|\psi\|_\infty M_H W_H}{\pi\delta}.
\tag{5}
\]

The upper bound needs the **signed** value of \(B\); replacing it by a positive norm cannot produce a negative witness.

### Matched direct comparison

Cauchy's derivative estimate at the real centers gives
\(|D'|\le M_D/\delta\), \(|S'|\le M_S/\delta\). Hence the same data also permit

\[
\mathcal R_C=
\frac{2\|\psi\|_{L^1(I)}M_DM_S}{\delta^2}
+\frac12\|\psi''\|_{L^1(I)}M_DM_S. \tag{6}
\]

A matched consumer uses the smaller proved derivative allowance, and may mix the two routes separately for \(D\) and \(S\). More generally define

\[
 T_F=\min\left\{
 \frac{M_FW_F}{\pi\delta},\frac{\ell M_F^2}{\delta^2},
 \text{any other paid upper for }\int_I|F'|^2
 \right\}.
\]

Then a shared Cauchy--Schwarz allowance is
\(2\|\psi\|_\infty\sqrt{T_DT_S}+(1/2)\|\psi''\|_1M_DM_S\).
If pointwise derivative budgets or directly weighted derivative norms are available, use those too. Neither (3) nor (6) is claimed optimal. In particular paying \(W_D\) only by a further coarse derivative estimate may make (3) weaker than (6). There is no established intrinsic Hodge advantage or measured cost gain.

When \(M_D\le\varepsilon\), the source-to-functional error is linear in \(\varepsilon\) if \(W_D\) is paid linearly in \(\varepsilon\), as happens with a separately paid larger analytic collar. Such a collar and its derivative/payment constants must be included; the observation \(M_D\le\varepsilon\) alone is not declared a numerical acquisition of \(W_D\).

## 3. A zero-count upper bound with an explicit boundary payment

Let \(\Omega\) be a bounded piecewise smooth domain, \(F\) holomorphic near \(\overline\Omega\), and assume

\[
 m=\inf_{\partial\Omega}|F|>0.
\]

Let \(N_\Omega\) count its interior zeros with multiplicity. Then

\[
\boxed{\quad W(F;\Omega)\ge4\pi m N_\Omega,
\qquad N_\Omega\le\frac{W(F;\Omega)}{4\pi m}.\quad} \tag{7}
\]

**Proof.** For every \(|w|<m\), Rouch\'e's theorem shows that \(F-w\) has exactly \(N_\Omega\) zeros inside \(\Omega\). For regular target values, the real change-of-variables Jacobian of the holomorphic map is \(|F'|^2\). Sum its inverse branches, and then ignore critical target values, which have planar measure zero. The area formula gives

\[
W(F;\Omega)=2\int_{\mathbb C}\frac{n_\Omega(w)}{|w|}dA_w
\ge2N_\Omega\int_{|w|<m}\frac{dA_w}{|w|}
=4\pi mN_\Omega.
\]

Zeros and critical points are finite on the compact closure unless the function is constant; the nonzero constant case has \(N_\Omega=W=0\). This also justifies the improper target weight at zero. \(\square\)

Every boundary component and all multiplicities are retained. In applications, an acquired lower margin \(m_0\le m\) and upper \(W\le B\) give \(N_\Omega\le\lfloor B/(4\pi m_0)\rfloor\). With a field approximant, a valid margin can be obtained from \(\inf_{\partial\Omega}|P|-\varepsilon>0\); neither that margin nor a complete quadrature for \(W\) is free.

Under an independently paid all-real regime and complete cap/complex-domain coverage, (7) gives a cap-count upper bound. It supplies no lower cap count or signed phase surplus. The exact event model \(F=A z^2\) on a radius-\(R\) disk has \(W=8\pi|A|R^2\), \(m=|A|R^2\), and ratio two, exactly admitting its double. The collision compatibility is quantitative.

## 4. What direct amplitude-weighted phase and hard traces lose

On a real cap put \(f=H(t,\cdot)\), \(E=f^2+f'^2\), \(Q=f'^2-ff''\). The physical angular current is \(Q/E\), with total \((N+1)\pi\) under [BW09 Note 03's complete cap contract][bw03].

The tempting replacement \(Q/|f|\) has a definite singular payment. At a simple real root \(r\) with slope \(s\ne0\),

\[
\frac{Q(x)}{|f(x)|}=\frac{|s|}{|x-r|}+O(1). \tag{8}
\]

Thus its one-sided integral truncated at distance \(\varepsilon\) diverges as \(|s|\log(1/\varepsilon)+O(1)\); an interior root contributes twice this coefficient. The real trace \(f'^2/|f|\) has the same divergence, although the planar \(W\) is finite. The logarithm is not canceled by the remaining term \(-\operatorname{sgn}(f)f''\), which is locally bounded. Consequently (1) cannot be replaced by a trace theorem for the singular density itself. A subtraction of (8) would require its own paid root, slope and residual information.

For the physical jet \(J(z)=F(z)+iF'(z)\), an actual cap floor \(j_0=\inf_I|J|>0\) does permit

\[
\int_I\frac{|Q|}{E}dx
\le\frac1{j_0}\int_I|J'|dx
\le\frac1{j_0}
\sqrt{\frac{\ell M_JW(J;U_\delta)}{\pi\delta}}.
\tag{9}
\]

This is a magnitude upper bound, not a signed lower phase surplus. For the ordinary quadratic near its event, \(j_0\le|J(0)|=2|A|\tau\), so this floor collapses. Note 08's upper bounds do not supply a lower replacement.

A smooth transverse average has a fully paid alternative. For nonnegative \(\psi\in C_c^2(I)\), nonnegative \(\rho\in C_c^2(-1,1)\) with \(\int\rho=1\), and \(\rho_\eta(y)=\eta^{-1}\rho(y/\eta)\), define

\[
B_{\psi,\eta}(F)=2\int\psi(x)\rho_\eta(y)
                  \frac{|F'(x+iy)|^2}{|F(x+iy)|}dxdy.
\]

The distribution identity of Note 08 gives exactly
\(B_{\psi,\eta}=2\int |F|(\psi''\rho_\eta+\psi\rho_\eta'')dA\).
A field error \(\sup|H-P|\le\varepsilon\) on this support therefore pays

\[
|B_{\psi,\eta}(H)-B_{\psi,\eta}(P)|
\le2\varepsilon\left(\|\psi''\|_1+
 \eta^{-2}\|\psi\|_1\|\rho''\|_1\right). \tag{10}
\]

This controls a fixed positive-thickness smoothed trace. Its \(\eta^{-2}\) model-error payment and the simple-root logarithm in (8) preclude silently taking a hard trace limit. It does not substitute for the physical phase denominator.

## 5. A scoped full-strip control for unweighted phase inference

There is no bound for physical cap phase depending only on common **upper** \(W\), field, and finite-jet budgets in the following smooth positive-source class. For odd \(n\), let

\[
F_n(z)=\frac{\epsilon_n}{n}e^{-z^2}\cos(nz),
\qquad \epsilon_n=e^{-n^4},
\qquad I=[-\pi/2,\pi/2].
\]

The endpoints and all interior real zeros are simple, and their physical phase decrease is exactly \(n\pi\). Yet for each fixed strip height \(Y>0\), the two physical strip boundaries give

\[
\begin{aligned}
W(F_n;S_Y)&\le4\int_{\mathbb R}|F_n'(x+iY)|dx\\
&\le4\epsilon_n e^{Y^2+nY}
 \left[\sqrt\pi+\frac{2(1+Y\sqrt\pi)}n\right]
 \longrightarrow0.
\end{aligned} \tag{11}
\]

Here \(|\cos(n(x+iY))|,|\sin(n(x+iY))|\le e^{nY}\),
\(\int e^{-x^2}dx=\sqrt\pi\), and \(\int |x|e^{-x^2}dx=1\). Every prescribed finite derivative upper bound on a fixed spatial collar also tends to zero.

These fields have the complete positive even smooth cosine source

\[
g_n(u)=\frac{\epsilon_n}{2n\sqrt\pi}
 \left[e^{-(u-n)^2/4}+e^{-(u+n)^2/4}\right],
\qquad
F_n(z)=\int_0^\infty g_n(u)\cos(zu)du.
\]

Thus they satisfy Note 08's strip integrability hypotheses, rather than exploiting an atomic source outside that theorem. Their heat continuations have the exact form, with \(a_t=1-4t>0\),

\[
F_{n,t}(z)=\frac{\epsilon_n}{n\sqrt{a_t}}
 \exp\left(\frac{tn^2-z^2}{a_t}\right)
 \cos\left(\frac{nz}{a_t}\right).
\]

They remain all-real with simple zeros for \(t<1/4\), and their source/jet upper budgets on each fixed \(|t|\le S<1/4\) are suppressed by \(\epsilon_n\). They have **no birth event**, and are cap-only controls: no threshold or born-root continuation is assigned. They fail the unchanged normalized theta source, its canonical tail and arithmetic. In particular their amplitudes and endpoint slopes tend to zero. They do not refute estimates using a paid lower amplitude/jet datum or unchanged theta arithmetic.

The result narrowly rules out recovering phase magnitude or forcing extra phase from the listed common upper budgets alone, even for a smooth positive source with full-strip finite energy. It does not rule out (3), (7), or a separately proved theta-specific signed estimate.

## 6. Result and remaining work

There is a **positive transfer**: derivative-weighted energy bounds a nonsingular derivative trace and gives the complete root-free signed-functional error allowance (3). A paid boundary amplitude additionally converts \(W\) into the multiplicity-sensitive count upper (7). The hard singular trace and physical angular phase require the extra payments quantified in (8)--(11).

No negative theta functional has been calculated. No cap count, signed endpoint/middle deficit, physical winding, all-height event exclusion, or BW09 later-collision gate changes status. The effective next use of (3) is a fixed \(\psi\), time/window, approximant and complete estimator comparison with a stopping margin; a numerical scan is not authorized by these formulas. Generic quadratic/atomic controls remain compatible with the transfers. Euler-factor, weighted-square, finite-prime, reflected and primitive controls keep the distinct failed canonical premises listed in [cluster 12][controls].

[n08]: 08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
[bw03]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md
[bw05]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[bw06]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[bwprogram]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
