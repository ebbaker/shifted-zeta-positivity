# Nonlocal arithmetic multipliers and boundary obstructions

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. Three independent collaborator calculations were reconciled with the complete scalar target in [coordination 11](../00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md).

This note audits three concrete alternatives to the finite polynomial currents already excluded in [note 09](09_JOINT_SOURCE_CURRENT_AND_POLYNOMIAL_OBSTRUCTION_20261015.md). Each retains the complete starting factor. None currently gives the missing bound `W B_partial <= C W^2 + epsilon |W|`. These are bounded rejections of specified estimates, not a theorem that arithmetic methods cannot work. The separate [multiplicative-dilation note](11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md) gives the surviving exact prime identities and their indispensable lower intervals.

## 1. Infinite-range massive recurrence current

Use the same residual weights `w_n` as note 09, so

\[
 r_n=\phi_n w_n=\partial_uK_n+g_n,\quad
 K_n=(p_n'w_n-p_nw_n')/8,\quad
 g_n=p_n(w_n''-w_n)/8.
\]

For `kappa>0`, write `r=exp(-kappa)`, `lambda=r+r^(-1)-2`, and define the half-line Green kernel

\[
 \mathcal G_\kappa(n,m)
 =\frac{r^{|n-m|}-r^{n+m}}{r^{-1}-r},\qquad n,m\ge1.
\]

It is positive and solves `(lambda-Delta)G=I` with zero boundary at index zero. Set

\[
 J_n=-\sum_m\mathcal G_\kappa(n,m)g_m,\qquad J_0=0,
 \qquad R_n=\lambda\sum_m\mathcal G_\kappa(n,m)g_m.
\]

Then `r_n=Delta J_n+partial_u K_n+R_n` exactly. On every finite rectangle,

\[
 \sum_{n=1}^M\int_0^U r_n
 =\int_0^U(-J_1+J_{M+1}-J_M)
  +\sum_{n=1}^M[K_n(U)-K_n(0)]
  +\sum_{n=1}^M\int_0^U R_n.                        \tag{1}
\]

The endpoint-only cutoff occurs in `w_n`; starting terms are complete. The source bounds of note 09 justify removal of the upper boundaries for each fixed positive `kappa`. The identities

\[
 \mathcal G_\kappa(1,m)=r^m,\qquad
 \lambda\sum_{n\ge1}\mathcal G_\kappa(n,m)=1-r^m
\]

give, on writing `G_m=int_0^infinity g_m`,

\[
 B_\kappa=\sum_m r^mG_m,\qquad
 \mathcal R_\kappa=\sum_m(1-r^m)G_m,
\]
\[
 |\mathcal R_\kappa|
 \le\kappa\mathcal M(g),\qquad
 \mathcal M(g)=\sum_m m\int_0^\infty |g_m(u)|\,du<\infty. \tag{2}
\]

Thus the complete reconstruction is

\[
 V_N=AH+BH_x+CS+B_{\rm src}+B_\kappa+\mathcal R_\kappa,
\qquad
 B_{\rm src}=\frac{\mathbf1_{j=0}\sum_{n\le N}\beta_n-A/2}{8}. \tag{3}
\]

In particular the error after multiplication by full `W` is at most `kappa M(g)|W|`. The constant is locally uniform under the prescribed bounded coefficient rules of note 09. The same source-prescribed `A` cancels `B_src`; no new cancellation of `B_kappa` follows.

There is a concrete complete-theta interpretation. For a common physical weight `w`,

\[
 B_\kappa=\tfrac18\int_0^\infty\psi_\kappa(w''-w),\quad
 \psi_\kappa(u)=e^u\sum_{n\ge1}r^ne^{-\pi n^2e^{4u}}.
\]

With `Theta_y(v)=sum_(n in Z) exp(-pi n^2 y) exp(inv)` and the circle Poisson kernel `P_r(v)=(1-r^2)/(1-2r cos v+r^2)`,

\[
 \psi_\kappa(u)=\frac{e^u}{2}
 \left[\frac1{2\pi}\int_{-\pi}^{\pi}
 P_r(v)\Theta_{e^{4u}}(v)\,dv-1\right].              \tag{4}
\]

Only an endpoint occurrence is truncated when its weight differs from the complete starting weights. Equation (4) is outside a finite-range current ansatz, but its positive kernel acts on the signed test `w''-w` in (3).

For polynomial-growth coefficients `a_n` and `a_0=1`, summation by parts instead gives

\[
 \sum_n a_ng_n=-J_1+\sum_nJ_n\Delta a_n+\sum_n a_nR_n. \tag{5}
\]

Theta removes the explicit interior defect `sum J_n Delta a_n`. Weighted-square collision controls generally do not. This is a real arithmetic discriminator; it is not a sign estimate. As `kappa` tends to zero, `B_kappa` tends exactly to `V_N-AH-BH_x-CS-B_src`. The new current therefore regularizes the same unresolved trace. Do not optimize its parameters until a separate signed inequality is proposed.

For precision, the canonical source reduction has zero residual only when `w''=w`, giving the two exponential anchors. This does not prohibit arbitrary nonpolynomial inverses: if coefficients are allowed arbitrary nonpolynomial dependence on `exp(4u)`, a polynomial degree-separation argument no longer applies. The earlier obstruction is confined to its stated polynomial and finite-range class.

## 2. Euler summation and the arithmetic counting multiplier

Let `a=pi exp(4u)` and

\[
 f_u(v)=e^u(2a^2v^4-3av^2)e^{-av^2},\qquad f_u(n)=\phi_n(u).
\]

Since

\[
 f_u(0)=0,\qquad
 f_u(v)=-ae^u\frac{d}{dv}(v^3e^{-av^2}),\qquad
 \int_0^\infty f_u(v)\,dv=0,
\]

Euler summation with `B_1({v})={v}-1/2` gives the exact arithmetic identity

\[
 \Phi(u)=\int_0^\infty B_1(\{v\})\partial_vf_u(v)\,dv. \tag{6}
\]

The cancellation in (6) cannot be replaced by an absolute source estimate. With `F(z)=(2z^4-3z^2)exp(-z^2)` and `z=sqrt(a)v`, dominated convergence as `u` tends to positive infinity proves

\[
 e^{-u}\int_0^\infty|B_1(\{v\})\partial_vf_u(v)|\,dv
 \longrightarrow\frac12\int_0^\infty |F'(z)|\,dz>0. \tag{7}
\]

The putative absolute source majorant grows like `exp(u)`. Its integral after multiplication by `exp(tu^2)` diverges for every `t>=0`, already at frequency zero. Thus an absolute-value interchange of the continuous index and physical source integrals is invalid.

There is an exact convergent repair. Integration by parts gives `int_0^infinity(v-1/2)partial_v f_u=0`. Subtracting this null multiplier from (6) yields

\[
 \boxed{\Phi(u)=-\int_1^\infty\lfloor v\rfloor\partial_vf_u(v)\,dv.} \tag{8}
\]

For `u>=0,v>=1`,

\[
 \partial_v f_u(v)
 =-2av(2av^2-1)(av^2-3)e^{u-av^2}<0.                 \tag{9}
\]

Hence (8) is a convergent positive-mixture representation with the exact integer counting multiplier. The analogous primitive identity is

\[
 \psi(u)=-\int_1^\infty\lfloor v\rfloor\partial_vp_v(u)\,dv,
 \quad p_v(u)=e^ue^{-\pi v^2e^{4u}}.
\]

For `beta(v)=(4 pi v^2-1)exp(-pi v^2)`, the full lower trace is

\[
 -\int_1^\infty\lfloor v\rfloor\beta'(v)\,dv
 =\sum_{n\ge1}\beta_n=\tfrac12.
\]

Every even physical weight therefore satisfies exactly

\[
 \int_0^\infty\Phi w
 =\frac{w(0)}{16}+\frac18\int_0^\infty\psi(w''-w).  \tag{10}
\]

For an endpoint-only cutoff, replace the endpoint counting function by `min(floor(v),N)`. Its lower coefficient is `sum_(n<=N) beta_n`; the starting counting function remains complete.

For example, put `c_j(x,u)=u^j cos(xu+j pi/2)` and

\[
 w=e^{tu^2}[c_j(x+\delta,u)-c_j(x,u)-\delta c_{j+1}(x,u)].
\]

This even weight has `w(0)=w'(0)=0`, so its source lower edge vanishes. The bulk integral in (10) is nevertheless exactly `V-W-delta S`, hence `V-W` at complete stationarity. It supplies no improved vanishing order of the cross term.

For nonnegative square coefficients of polynomial growth, (8) holds with the cumulative sum `A(v)=sum_(n<=v) a_n` in place of `floor(v)`. Bounds using only positivity, monotonicity or a positive envelope for `A` therefore admit the weighted-square collision controls. The arithmetic distinction resides in **exactly** `A(v)=floor(v)`, not in positivity of (8). This rejects the proposed envelope argument without rejecting a future signed discrepancy estimate that retains that exact multiplier.

## 3. Poisson duality before and after source integration

For continuous real index `a`, use `p_a,phi_a` from section 2 with `a` now the index, and the Fourier convention `hat f(xi)=int_R f(a)exp(-2 pi i a xi) da`. Gaussian transformation gives

\[
 \widehat{p_\cdot(u)}(\xi)=p_\xi(-u),\qquad
 \widehat{\phi_\cdot(u)}(\xi)=\phi_\xi(-u).           \tag{11}
\]

At each finite source coordinate, Poisson summation and `phi_0=0` imply

\[
 \Phi(u)=\sum_{k\ge1}\phi_k(-u).                   \tag{12}
\]

This is the actual theta reflection identity, not a property of arbitrary positive square weights. The classical transformation law is recorded in [DLMF 20.7(viii)](https://dlmf.nist.gov/20.7.viii); [DLMF 1.8(iv)](https://dlmf.nist.gov/1.8.iv) gives Poisson summation.

For finite `U`, the function

\[
 F_{j,U}(a)=\int_0^U e^{tu^2}u^j\cos(yu+j\pi/2)\phi_a(u)\,du
\]

is Schwartz in its index. Its Fourier transform at `k` is the same integral with `phi_k(-u)`, so

\[
 h_{j,U}(t,y)=\sum_{k\ge1}D_{j,k,U},\quad
 D_{j,k,U}=\int_0^U e^{tu^2}u^j\cos(yu+j\pi/2)\phi_k(-u)\,du. \tag{13}
\]

All exchanges in (13) are valid at fixed `U`. For fixed nonzero `k`, however,

\[
 \phi_k(-u)=-3\pi k^2e^{-5u}+5\pi^2k^4e^{-9u}+O_k(e^{-13u}). \tag{14}
\]

At every fixed `t>0`, the associated complex integral has endpoint asymptotic

\[
 \int_0^Uu^je^{tu^2+iyu}\phi_k(-u)\,du
 =-\frac{3\pi k^2 U^j e^{tU^2-5U+iyU}}{2tU-5+iy}
 [1+O(U^{-2})+O_k(e^{-4U})].                        \tag{15}
\]

This follows by one endpoint integration by parts, then (14). Consequently each ordinary `j=0` real dual mode has no improper limit for real `y`; oscillation does not tame its growing amplitude. The `j=1,y=0` test is identically zero and is an explicit exception. One cannot write the full physical transform as a sum of separately integrated positive-time dual modes.

The scale of the required collective cancellation is visible without quadrature:

\[
 \phi_k(-u)<0\quad\Longleftrightarrow\quad
 0<k<\sqrt{3/(2\pi)}e^{2u}.                         \tag{16}
\]

Any dual source cutoff `M(u)=o(exp(2u))` eventually retains only negative terms, whereas the complete sum is positive. Put `mathcal F(v)=(2 pi^2 v^4-3 pi v^2)exp(-pi v^2)`. A Riemann-sum calculation gives

\[
 \sum_{k\ge1}|\phi_k(-u)|=e^u(C_{\rm abs}+o(1)),\quad
 C_{\rm abs}=\int_0^\infty|\mathcal F(v)|\,dv>0,      \tag{17}
\]

while the signed sum is `Phi(u)~2 pi^2 exp(9u-pi exp(4u))`. Thus absolute bounds erase precisely the lattice cancellation needed for source integrability, already at `t=0`.

For every finite `M,U` the full error is still exactly

\[
 h_j-\sum_{k\le M}D_{j,k,U}
 =(h_j-h_{j,U})+
 \int_0^U e^{tu^2}u^j\cos(yu+j\pi/2)
                    \sum_{k>M}\phi_k(-u)\,du.      \tag{18}
\]

The first term has the ordinary rapidly decaying source-tail bound. For fixed `M` at positive time, the second cancels the divergent dual head; it is not a negligible tail.

An additional local diagnostic is

\[
 \phi_a(u)=\sum_{m\ge1}
 \frac{(-1)^m(2m+1)\pi^m}{(m-1)!}
 a^{2m}e^{(4m+1)u}.                                \tag{19}
\]

The `2m`th index derivative of `F_(j,U)` at zero is therefore its displayed coefficient times `(2m)!` and the integral with the growing factor `exp((4m+1)u)`. Odd index derivatives vanish. Dual derivatives replace that factor by `exp(-(4m+1)u)`, which still loses integrability for positive heat time. This prevents an unproved Schwartz-limit argument from rescuing a termwise full-source passage.

## 4. Controls and research decision

The massive current uses exact coefficient recurrence, the floor identity uses the exact lattice counting function, and the Poisson identity uses the complete unweighted comb. Weighted-square collisions fail those complete arithmetic premises. They nevertheless pass generic positive-kernel or positive-envelope versions of the proposed estimates. The reflected quartic control has no polynomial-growth square-source expansion; its positive primitive and reflection do not provide the missing lattice information. The [positive-primitive collision in Investigation 21](../../../21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) reinforces the distinction between a positive source construction and a signed physical consequence.

The bounded decision is:

1. Retain the massive current as an explicit convergent regularization with all boundaries, but do not count its small remainder as control of the main trace.
2. Reject absolute Bernoulli-sector estimates and coarse positive envelopes of the repaired floor multiplier.
3. Reject separately integrated Poisson dual modes at positive time. Sum the collective arithmetic cancellation first, or retain its entire finite-cutoff error.
4. Retain the exact finite prime packets from note 11 as another concrete formulation. Their shifted frequencies and lower intervals must remain coupled.

No new theta signed domain, noncollision theorem, or RH conclusion follows. The calculations narrow the proposed methods and identify their lost cancellations. They leave open an estimate genuinely using the exact arithmetic coupling inside the complete signed stationary pairing. No broad numerical search was performed.
