# GNP-RS-E06 r1 — adaptive Euler phase and fixed-reference signed tangent

11 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol, effort ultra**
by explicit execution dispatch. The separate Sol/ultra internal
assessor contributed the fixed-reference tangent proof route.

**Status: proved in-note from named inherited inputs**, with a
[contributing separate-agent internal assessment][review]. This is the
return to the [frozen E06 r1 request][request]. The adaptive reference
phase estimate is an acquisition result under [avoid01][a01].
The signed tangent calculation is a scoped obstruction under
[avoid07][a07] and [avoid12][a12]. Use the [result index][results],
[heat-flow cluster][r11], [avoidance index][avoid] and
[collision controls][controls]. The actual every-center signed
Green value remains open.

## 1. Regulator-uniform joint phase

Keep the [E01][e01], [E04][e04] and [E05][e05] normalization and
complete field \(V_\lambda=H_\lambda/C_-\) with physical evolution
\(\partial_\lambda H_\lambda=-\partial_{zz}H_\lambda\).
Write \(L=L_X=\log(X/(4\pi))\), \(\lambda=c/L\),
\(1/2\le c\le1\), \(W_X=[X-R_X,X+R_X]\),
\(R_X=(32/\pi)\log X\), \(d\mu_X=K(x-X)\,dx\) on \(W_X\),
\(K(t)=1/(16\cosh(\pi t/8))\), and \(q_X=\mu_X(W_X)\).
The observation remains at \(X+4i\) in the strip \(0<y<8\),
with the original defect parameters \(d=1/2,r=1\).
Both \(c,\lambda\) and the prime cutoff \(P\) are fixed across
each spatial integral. Set
\[
 \begin{aligned}
 &\sigma_c=\tfrac12+\tfrac c4,\qquad
 \nu_\lambda(x)=x/2+\pi\lambda/8,\qquad \phi_\lambda(x)=2\Theta(\lambda,x),
 \qquad r_p=p^{-\sigma_c},\\
 &E_P(x)=\prod_{p\le P}(1-r_p e^{i\nu_\lambda(x)\log p})^{-1},
 \qquad S_P^{\rm ref}=E_P+e^{i\phi_\lambda}\overline{E_P}.
 \end{aligned}
\]
Use the canonical Euler logarithm
\(\ell_P(x)=\sum_{p\le P}\sum_{k\ge1}r_p^k
e^{ik\nu_\lambda(x)\log p}/k\), so \(E_P=\exp\ell_P\).
Define \(\psi=\phi_\lambda-2\Im\ell_P\). Then
\(a=S_P^{\rm ref}/E_P=1+e^{i\psi}\).

Let \(\kappa=1-2^{-5/8}>0\). Since \(r_p\le p^{-5/8}\),
the series for \(\ell_P\) can be differentiated twice on the real line.
The geometric sums of \(r_p^k\) and \(kr_p^k\) give
\[
 \begin{aligned}
 2|(\Im\ell_P)'|
 &\le\sum_{p\le P}\frac{r_p\log p}{1-r_p}
 \le D_1(P):=\frac{8}{3\kappa}P^{3/8}\log P,\\
 2|(\Im\ell_P)''|
 &\le\tfrac12\sum_{p\le P}\frac{r_p(\log p)^2}{(1-r_p)^2}
 \le D_2(P):=\frac{4}{3\kappa^2}P^{3/8}(\log P)^2 .
 \end{aligned}
 \tag{E06.1}
\]
Here \(\sum_{n\le P}n^{-5/8}\le(8/3)P^{3/8}\) by the
decreasing integral comparison. With \(R_X\le X/2\), the
window has \(L_x\ge L-2R_X/X\). The carrier derivatives
are \(\phi_\lambda'=L_x/2+\pi\lambda/(8x)\) and
\(\phi_\lambda''=1/(2x)-\pi\lambda/(8x^2)\). Impose the two
additional gates \(D_1(P)\le L/8\) and \(R_X/X\le L/8\).
Then on \(W_X\),
\[
 \psi'\ge L/4,\qquad
 D:=\|\psi''\|_{\infty,W_X}\le
       D_2(P)+X^{-1}+\pi\lambda/(2X^2).
 \tag{E06.2}
\]

For \(\delta>0\), set \(b_\delta=(\delta+\sqrt{\delta^2+4})/2\)
and \(\rho=b_\delta^{-2}<1\). The [E04][e04] unit-arm factorization
is
\[
 f_\delta(a):=\tfrac12\log(|a|^2+\delta^2)
     =\log b_\delta+\Re\sum_{k\ge1}
                  \frac{(-1)^{k+1}\rho^k e^{ik\psi}}{k}.
\]
The coefficient modulus is constant throughout the window.
For \(m=\min_{W_X}\psi'\) and \(k\ge1\), integration by parts
with the derivative of \(e^{ik\psi}\) gives
\[
 \left|\int_{W_X} e^{ik\psi}\,d\mu_X\right|
 \le \frac{2\|K\|_\infty+\|K'\|_1}{km}
       +\frac{q_X D}{km^2}.
\]
The two endpoint terms together cost \(2\|K\|_\infty/(km)\);
the other terms differentiate the kernel and \(1/\psi'\).
The kernel is even and decreases for \(t>0\), so
\(\|K\|_\infty=1/16\), \(\|K'\|_1=1/8\) and \(q_X\le1/2\).
Since \(\sum_{k\ge1}\rho^k/k^2\le2\), (E06.2) gives
\[
 \boxed{
 \left|\int_{W_X} f_\delta(a)\,d\mu_X-q_X\log b_\delta\right|
 \le 2/L+16D/L^2.}
 \tag{E06.3}
\]
This is uniform for all \(\delta>0\). A regulator chosen at the
center stays fixed in the integral and has the same bound.

Under the same gates the unregularized integral also exists
and satisfies
\[
 \left|\int_{W_X}\log|a|\,d\mu_X\right|\le 2/L+16D/L^2 .
 \tag{E06.4}
\]
Indeed \(f_\delta(a)\) decreases to \(\log|a|\) as
\(\delta\downarrow0\) and is bounded above by
\(\tfrac12\log5\) for \(0<\delta\le1\), since \(|a|\le2\).
Apply monotone convergence after subtracting from that constant.
The two-sided bound in (E06.3), with \(\log b_\delta\to0\),
ensures a finite limit.

## 2. Full-band overhead for \(P(X)=\lfloor L^2\rfloor\)

Choose \(P(X)=\lfloor L^2\rfloor\) and keep that value fixed at
each center throughout its integral. Eventually \(P\ge2\).
The upper bounds in (E06.1) give
\[
 D_1(P)\le\frac{16}{3\kappa}L^{3/4}\log L,\qquad
 D_2(P)\le\frac{16}{3\kappa^2}L^{3/4}(\log L)^2 .
\]
They are both \(o(L)\), so the gates of (E06.2) hold eventually
and \(D\le L\) eventually. The phase error in (E06.3) is then
at most \(18/L\), uniformly in \(c,\delta\). The same phase
conclusion holds for \(2\le P\le L^\gamma\) for any fixed
\(0<\gamma<8/3\), with an onset that may depend on \(\gamma\).

E05 (E05.1) applies exactly at the chosen finite \(P\), with
\(\lambda,c\) held fixed across the full-line reference integral.
Its omitted prime subseries has size at most
\((2/3)P^{-3/2}=O(L^{-3})\) for the chosen cutoff. For all
real \(x\),
\[
 |\log|E_P(x)||\le|\ell_P(x)|
 \le\sum_{p\le P}\frac{r_p}{1-r_p}
 \le\frac{8}{3\kappa}P^{3/8}.
\]
The exterior reference log integral therefore has absolute value
at most \((16/(3\pi\kappa))P^{3/8}X^{-4}\) by the E03 kernel
tail. This is \(O(L^{3/4}X^{-4})\). The actual field's exact
critical-log tail still has the E01 allowance
\(T_X=D_V X^{-3}\log^2X\).

Let \(S_\lambda\) be the two complete Riemann–Siegel arms in
E04 (E04.1), whose field error includes the full correction
and provider residual. With the reference normalization,
\[
 \left|\frac{V_\lambda-S_\lambda}{E_P}\right|
 \le C X^{-1/4}\exp\big((8/3)P^{3/8}\big)
 \le C X^{-1/4}\exp\big((8/3)L^{3/4}\big).
 \tag{E06.5}
\]
Indeed \(|E_P|^{-1}\le\prod_{p\le P}(1+r_p)\le
\exp(\sum_{p\le P}r_p)\). The bound is \(X^{-1/4+o(1)}\).
It pays the field approximation error after division by \(E_P\).
The difference between the two-arm arithmetic field and
the reflected Euler reference remains in the complete residual.

Set \(R_P(X,c)=\int_{W_X}|V_\lambda-S_P^{\rm ref}|^2/|E_P|^2\,d\mu_X\),
using the exact \(V_\lambda\). Write
\(P_{c,\lambda}^{(\le P)}\) for E05's prime subseries and
\(P_{c,\lambda}\) for E01's full prime baseline. Applying E04's
upper log transfer to \(V_\lambda/E_P\) and \(S_P^{\rm ref}/E_P\),
and retaining the E05 Jensen payment of the relative residual,
gives at the chosen cutoff
\[
 \boxed{\begin{aligned}
 J_\lambda(X)\le{}&
 P_{c,\lambda}^{(\le P)}(X)-P_{c,\lambda}(X)
 +q_X\log b_\delta+
 \frac{q_X}{2}\log\!\left(1+\frac{R_P(X,c)}{q_X\delta^2}\right)\\
 &+T_X+\frac{C_*+18}{L}
     +\frac{16}{3\pi\kappa}P^{3/8}X^{-4}.
 \end{aligned}}
 \tag{E06.6}
\]
All onsets are finite. They consist of the inherited E01/E04
chart and tail onsets, \(P\ge2\), the window and derivative
gates in (E06.2), and \(D\le L\) by the displayed bounds.
The regulator term obeys \(q_X\log b_\delta\le\delta/4\)
since \(\log b_\delta=\operatorname{arsinh}(\delta/2)\).
Thus the overhead in (E06.6) can vanish while retaining an exact
residual payment. The first unpaid input for this schedule is
an every-center bound for \(R_{\lfloor L^2\rfloor}(X,c)\)
small enough for the chosen \(\delta\) and defect margin,
including exceptional centers. E05's mean law takes \(X\)
to infinity with \(P\) fixed. It supplies no growing-cutoff
mean or every-center estimate here.

## 3. Fixed-reference signed tangent obstruction

Freeze any finite \(P\) and now use \(c=1\). For each center,
allow \(\delta>0\) fixed within its spatial integral. Put
\(w=V_\lambda/E_P\), \(a=S_P^{\rm ref}/E_P\),
\(h=|a|^2+\delta^2\), and
\[
 G_\delta=\tfrac12\log h-\tfrac12+\frac{|w|^2}{2h}.
\]
The inequality \(\log t\le t-1\) with \(t=|w|^2/h\) gives
\(\log|w|\le G_\delta\), including the extended-value inequality
at \(w=0\). Its numerator retains
\[
 |w|^2=|a|^2+2\Re(\bar a(w-a))+|w-a|^2.
\]
It is a signed test of this tangent denominator and keeps the
exact cross term inside the integral.

Let \(H=4+\delta^2\) and \(Z=\int_{W_X}|w|^2\,d\mu_X\).
The bounds \(|a|\le2\), \(h\le H\) and \(h/H\ge|a|^2/4\)
give
\[
 \begin{aligned}
 \int_{W_X}G_\delta\,d\mu_X
 &\ge \frac{q_X}{2}\log H-\frac{q_X}{2}
       +\frac{Z}{2H}
       +\int_{W_X}\log|a|\,d\mu_X-q_X\log 2\\
 &\ge \frac{q_X}{2}\log(Z/q_X)
       +\int_{W_X}\log|a|\,d\mu_X-q_X\log 2 .
 \end{aligned}
 \tag{E06.7}
\]
The second line follows by \(\log t\le t-1\) at
\(t=Z/(q_X H)>0\). A positive \(Z\) holds in particular at
every center used below. At fixed \(P\), (E06.4) bounds the
reference log by \(O(1/L)\) past its finite onset.

E05 §3 proves that the exact complete moment
\(M(X,1)=\int_{W_X}|V_{1/L_X}|^2\,d\mu_X\) is unbounded at
arbitrarily high centers. The reference satisfies
\(B_P:=\sup|E_P|<\infty\) for fixed \(P\). Thus
\(Z\ge M(X,1)/B_P^2\), and (E06.7) tends to infinity along
centers with \(M(X,1)\to\infty\) because \(q_X\to1/2\).
The lower bound is independent of \(\delta\). To obtain a
Green allowance from the tangent, restore
\(\int_{W_X}\log|E_P|\,d\mu_X-P_{1,\lambda}(X)\) and the
nonnegative exact-tail and outer-error allowances. The restored
reference and prime term is bounded by E05 (E05.1) and its
exterior estimate. Hence this particular upper allowance is
unbounded at arbitrarily high centers for every fixed \(P\),
including when \(\delta\) is chosen at the center.

## 4. Scope and control screen

The adaptive phase estimate retains the canonical theta field
and pays its reference phase, prime tail, logarithmic exterior,
and correction scale. The signed margin needs the unpaid
adaptive local residual or a genuinely nonlinear signed estimate
that keeps the relevant residual and phase information together.
The obstruction in §3 concerns the tangent with
\(h=|a|^2+\delta^2\) at fixed \(P\). A varying-\(P\) tangent or
a different nonlinear logarithmic estimate needs its own analysis.
The tangent lower bound is a statement about the allowance, and
does not give a lower bound on the actual Green value.

Apply [controls12][controls], [premises02][a02] and the
[E05 §4][e05] screen at their recorded witness domains.
The scalar log and phase estimates use generic algebra and
calculus. The theta-specific transfer and tangent obstruction
consume the literal complete field estimate, prime calibration,
and exact coherent moment unboundedness from E05.

| Control family | Premise absent from the literal theta application |
| --- | --- |
| Euler-factor and translated sources | The unchanged canonical Dirichlet weights and prime baseline used in E01 and E05. |
| Weighted squares and finite-prefix or finite-tail changes | The full unmodified square coefficients together with canonical source reflection. |
| Finite-prime orbits | Full source reflection and all canonical coefficients, beyond selected prime data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Ordinary theta/zeta Dirichlet arithmetic in the inherited complete field formula. |
| Atomic and exact finite-profile controls, continuous extensions and heat counter-kernels | The complete canonical field with its two arms, correction and coherent moment law. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic despite matching displayed completion data. |
| Fixed theta amplitude with variable readout | The actual cosine readout and physical Newman equation in the field provider. |
| Relaxed positive Green profiles | Identification with the exact integer zero measure and complete critical-boundary field. |

All estimates are analytic.

[request]: ../research-progress/handoffs/05_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_R1_20261111.md
[e01]: 03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[e04]: 11_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_20261111.md
[e05]: 14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

[review]: ../reviews/09_GNP_RS_B05_INTERNAL_REVIEW_20261111.md
