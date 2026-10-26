# Evolution equations, ansatz residuals, and negative-time arithmetic modes

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0002, thread 01a17600-b15f-7f52-8713-31fa13599341.

**Status:** source-based synthesis, exact algebraic identities and a
proposed continuation. No new accepted asymptotic theorem or independent
review. No numerical, symbolic, sampling or interval research was run.
The [manifest](08_EVOLUTION_INPUTS_20261025.json) pins the inspected state.

The author asks whether applying the evolution equations to the ansatze
and their errors can clarify intermediate negative times. The author
retains the regulator transition near64 and understanding all regimes,
especially large height, as priorities.

## 1. Existing use of the equations

| Use | Evidence | What it supplies |
| --- | --- | --- |
| Construction by heat evolution | Ansatz Note05 FN20--26 | The finite moment sum plus bounded correction integral solves the negative-time heat equation exactly on each frozen chart. |
| Residual cancellation and time error | Note03 CB11--13; Note04 CS26--28 | A corrected outer arm cancels the leading residual; proved spatial errors and residuals give direct time errors. |
| Time joining | Note06 NB20--24 | Both the component residual and the derivative-of-cutoff term are retained. |
| Observable evolution with defects | Parent Note31 PE33--39; Note34 CJ25--26 | Explicit forcing in the potential, density and current equations, with actual covariance and physical regulator. |
| Spatial assembly | Parent Note42 GS7--12; Note50 TJ4 onward | Nonholomorphic compatibility and curvature defects. |

Evolution already constructs and checks the models. A further opportunity
is to organize it into a shorter negative-time asymptotic expansion with
a proved improvement. An exact PDE does not by itself simplify its
arithmetic initial data.

## 2. Exact error evolution and its stability obligation

For a smooth spatially holomorphic ansatz F, define
\[
\mathfrak r_F=F_t+F_{zz},\qquad E=H-F.
\]
Then
\[
(\partial_t+\partial_{zz})E=-\mathfrak r_F. \tag{EV1}
\]
This separates initial mismatch from evolution defect. A zero residual
does not identify the canonical solution without the initial comparison.

For T=-t set h(T,z)=H(-T,z), f(T,z)=F(-T,z), and
d=f_T-f_{zz}=-\mathfrak r_F(-T,z). On the real line, for a function
class admitting heat convolution and differentiation, Duhamel gives
\[
E(T)=\mathsf S_{T-T_0}E(T_0)
 -\int_{T_0}^{T}\mathsf S_{T-s}d(s)\,ds,\qquad T\ge T_0, \tag{EV2}
\]
where
\[
(\mathsf S_v g)(x)=\frac1{\sqrt{4\pi v}}
 \int_{\mathbb R}e^{-(x-u)^2/(4v)}g(u)\,du.
\]
This is forward diffusion toward more negative original time. It does
not justify recovery toward T=0. See [Stanford Math220B Section2.7](https://web.stanford.edu/class/math220b/handouts/heateqn.pdf).
For bounded real-line data the elementary bound is
\[
\|E(T)\|_\infty\le\|E(T_0)\|_\infty+
 \int_{T_0}^T\|d(s)\|_\infty\,ds. \tag{EV3}
\]
This is **not** a bound in the much stronger outer-carrier-relative norm.
The current ansatze are chartwise. A whole-line extension or localization
requires tails and commutators; multiplying an error by a spatial cutoff
adds \(-2\chi'E_x-\chi''E\) to its T-heat equation. Complex targets
require strip control or explicit complex-kernel losses. Normalizing by
a changing carrier adds its coefficients to the error equation.

Subtracting the entire Duhamel defect from f simply recovers the heat
evolution of f(T0). A useful simplification must evaluate or approximate
that correction with a better error or representation; an unevaluated
integral alone supplies neither.

## 3. Evolution equations for amplitude and phase

For a nonzero complex arm f=a exp(i theta) on a real interval, with
real a>0 and real unwrapped theta,
\[
f_T-f_{xx}=e^{i\theta}
\{a_T-a_{xx}+a\theta_x^2+
i(a\theta_T-2a_x\theta_x-a\theta_{xx})\}. \tag{EV4}
\]
An exact heat arm therefore satisfies
\[
a_T=a_{xx}-a\theta_x^2,\qquad
\theta_T=\theta_{xx}+2(a_x/a)\theta_x. \tag{EV5}
\]
For an approximate arm the real and imaginary parts of exp(-i theta)d
are the corresponding forcing terms. Expanding a and theta and cancelling
successive residual orders is a direct construction method. Apply this
to named arms, not a purported globally nonvanishing polar form of H;
the arithmetic sum, its zeros and its correction remain.

For a nonzero reference arm f0, let
p=(f0)_x/f0, r0=((f0)_T-(f0)_xx)/f0 and f=f0(1+c). Exactly,
\[
\frac{f_T-f_{xx}}{f_0}
=c_T-c_{xx}-2pc_x+r_0(1+c). \tag{EV6}
\]
The first correction equation
\(c_T-c_{xx}-2pc_x=-r_0\) leaves \(r_0c\), before further truncation.
Canonical initial data and uniform remainder estimates remain necessary.
Note03 CB12 already realizes this product-residual mechanism with the
original time sign. No new solvability theorem is asserted here.

## 4. The negative-time model as evolving arithmetic modes

On the real right tail put
\[
L=\log(X/(4\pi)),\quad a_X=e^{L/2},\quad N=\lfloor a_X\rfloor,
\quad r_n=\log(a_X/n),\quad k_n=r_n/2,
\]
\[
A_0=A_o(0,X),\qquad
\phi_n(0,X)=\Theta_o(0,X)-(X/2)\log n.
\]
Completing the square in the **existing short model**, exactly,
\[
A_o(-T,X)w_n(-T,X)
=A_0n^{-1/2}e^{\pi^2T/64}e^{-Tr_n^2/4}, \tag{EV7}
\]
\[
\phi_n(-T,X)=\phi_n(0,X)-\pi T r_n/8. \tag{EV8}
\]
Consequently
\[
F_N(-T,X)=e^{\pi^2T/64}\left[
A_0\sum_{n\le N}n^{-1/2}e^{-Tk_n^2}
\cos\{\phi_n(0,X)-\pi T k_n/4\}
+\mathcal R_N(X)\right]. \tag{EV9}
\]
This rewrites Notes03--05; it adds no validity domain or improved error.
For fixed n, \(\partial_X\phi_n(0,X)=k_n\). The locally frozen mode
exp(lambda_n(x-X)), with lambda_n=-pi/8+i k_n, evolves by
exp(T lambda_n^2), giving EV9's damping and phase shift. Slowly varying
amplitude and phase curvature account for the omitted frozen-mode residual.

- For fixed n, k_n has size log X: its absolute damping changes on
  \(T\log^2X=O(1)\).
- Ratios of two fixed mode weights change on \(T\log X=O(1)\).
  These are distinct questions.
- Heat damping by itself retains \(r_n=O(T^{-1/2})\). At fixed T
  this includes a growing population with n comparable to sqrt X.
  Note05 FN9 already controls this population and its logarithmic moments.
- These are component-weight statements, not dominance assertions for
  the signed total. Cancellation with the RS correction remains essential.

The n=1 outer carrier shrinks by exp(-T L^2/16) relative to the natural
gamma scale, up to bounded T-dependent factors. A fixed algebraic error
on the latter scale can therefore be too large for the former. This
explains FN10's failed allowance; it is neither an actual error lower
bound nor an impossibility theorem for a short resummation.

## 5. Observable evolution with the explicit ansatz forcing

The following identities are already in parent Notes14/31/34. Keep
the physical q and fixed K and write
\[
D_F=|F|^2+q,\quad S_F=\log D_F,\quad U_F=K*S_F,\quad
\Xi_F=\frac{2\Re(\overline F\,\mathfrak r_F)}{D_F},
\]
\[
Q_F=K*(S_{F,x}^2-S_{F,y}^2)-(U_{F,x}^2-U_{F,y}^2),\qquad
\mathcal B_F=\frac{q_t+(q_{xx}-q_{yy})/2}{D_F}.
\]
With \(\square=\partial_x^2-\partial_y^2\),
\[
(U_F)_t=-\tfrac12\{\square U_F+(U_F)_x^2-(U_F)_y^2+Q_F\}
+K*\mathcal B_F+K*\Xi_F. \tag{EV10}
\]
For \(\rho_F=q|F_z|^2/(\pi D_F^2)\), \(R_F=K*\rho_F\), define
the actual regulator curvature by \(\Delta S_F=4\pi(\rho_F+C_F)\)
and put \(\overline C_F=K*C_F\). Then
\[
\begin{split}
(R_F)_t={}&-\tfrac12\square R_F
-\frac1{8\pi}\Delta\{(U_F)_x^2-(U_F)_y^2+Q_F\}\\
&+\frac1{4\pi}\Delta K*\mathcal B_F
-\partial_t\overline C_F-\tfrac12\square\overline C_F
+\frac1{4\pi}\Delta K*\Xi_F.
\end{split}\tag{EV11}
\]
The additional current-balance forcing is
\[
\mathcal D_{\mathfrak r_F}
=\frac{2q\Re((\mathfrak r_F)_z\overline{F_z})}{\pi D_F^2}
-4\rho_F\Re(\mathfrak r_F\overline F/D_F). \tag{EV12}
\]
Thus the equations act on the ansatz with explicit forcing. Q is the
actual covariance, not an equation-defined closure. In the negative-time
range q depends only on time: C_F=0, but regulator time forcing remains.
Near the regulator switch the spatial curvature terms must also remain.
Nonholomorphic spatial joins require the additional defects in Note42.

Small field residuals do not automatically give useful observable bounds:
the crude \(|\Xi_F|\le|\mathfrak r_F|/\sqrt q\) can be poor when q
is small. The parent's weak-transfer and collar methods address this,
but the new ansatze need their own uniform estimates. Displaying EV10--12
does not establish a new transfer theorem.

## 6. Scope, controls and next deliverable

This is an approximation direction, not an RH-equivalent criterion.
Consult the [result index](../../../../../result-summaries/README.md),
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
plus the [avoid index](../../../../../avoid/README.md), especially
[quantitative gain01](../../../../../avoid/01_restating_the_target.md),
[shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Heat evolution, Duhamel and the modulation identities also hold for the
collision controls; they exclude none. Euler-factor controls fail the
unchanged ordinary Dirichlet coefficients in EV9. Finite weighted-square
and theta-cutoff controls fail its full canonical completion/RS expansion.
Reflected, smooth-shape, positive-primitive, counter-kernel and fixed-event
controls lack that same gamma/arithmetic identity. Finite-prime matching
does not supply the full coefficients. These are premise distinctions,
not collision-exclusion conclusions.

**Next deliverable: Analysis — Sol**, supplementary
[HDA-A02-AN03 r1](../research-progress/handoffs/HDA-A02-AN03.md): derive
one explicit evolution correction with a genuine error improvement, or
identify its first precise remaining obstruction. Compare both accuracy
scales and retain all modes and corrections. This complements the existing
A03 regulator-center packet. No dispatch, new accepted theorem, manuscript
milestone or parent-status upgrade follows. All-time coverage, physical
transfer, useful cost and independent review remain open.
