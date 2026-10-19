# UAR-03: uniform coherent edge and cutoff matching

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Separate same-model edge derivation, cutoff matching, source audit and mathematical review; internal LLM work, no specialist human review.

**Outcome: proved in-note, with outward checks of constants.** A bounded double-contour model of the actual RS heat edge has a complete uniform error on the [UAR-01 disks][contract], for either frozen cutoff. Its limits depend only on t, so same-cutoff models agree on chart overlaps. A separate coherent bound makes the corrected cutoff-transition allowance summable across the sector. These results supply UAR-03's analytic input; together with [UAR-02][finite] they make UAR-04 Ready. The retained signed increment has not been evaluated or bounded, and no physical anchor, cost advantage or new exclusion coverage follows.

Classification under [avoid/01][a01]: quantitative uniform approximation and transition theorems, not a nonvanishing criterion. Read the [result summaries][results] and [patterns to avoid][avoid], especially [collision controls][controls], [theta bookkeeping][theta], [scoped claims][a07], [normalization][a08] and [signed recombination][a12]. The exact contour, Gaussian shift and profile jump are inherited. The new estimating outputs are the uniform compact-truncation error and the summed corrected-transition payment.

## 1. Fixed source and a single coherent edge model

Keep UAR-01's M, M0=exp(m0), A, theta, omega, corrected f_N=(G_N-Chat_N^an)/A and residual r_N. For each fixed 0<t<=1/20 use

\[
J_t=[4\pi e^{1/t},4\pi e^{2/t}],\quad
c=4\pi e^L,\quad \kappa=tL\in[1,2],\quad R=1/L,
\quad D_c=\{|z-c|\le R\},\quad W_c=[c-R/2,c+R/2].
\]

Freeze N as either extremal natural cutoff on [c-R,c+R]. Define

\[
q=N+\tfrac12,\quad w_q(r)=q+(1+i)r,\quad
V_t=S_t=2\sqrt{2/t},\quad\tau(z)=z/2+\pi t/8,
\quad h(v,z)=\tfrac12+\sqrt t\,v+i\tau(z).
\]

The exact fixed-contour integral and its finite version are

\[
J_N(s)=(1+i)\int_{+\infty}^{-\infty}
 \frac{w_q(r)^{-s}e^{i\pi w_q(r)^2}}
 {e^{i\pi w_q(r)}-e^{-i\pi w_q(r)}}\,dr,
\quad
J_N^{S_t}(s)=(1+i)\int_{S_t}^{-S_t}(\cdots)\,dr.            \tag{1}
\]

The descending orientation in (1) is essential. The logarithm along w_q uses the principal branch: that line never meets the negative real axis. Its denominator is never zero. No extra parity factor is inserted; the true contour already contains its sign and parity.

Define the retained positive-channel model

\[
B_N^{\Box}(t,z)=\frac{e^{t\pi^2/64}}{\sqrt\pi}
 \int_{-V_t}^{V_t}e^{-v^2-i\pi\sqrt t\,v/4}
 M(h(v,z))J_N^{S_t}(h(v,z))\,dv.                            \tag{2}
\]

For an analytic physical function B, B^sharp(z)=overline{B(overline z)}. The signed normalized edge-discrepancy model is

\[
\widehat e_{edge,N}
 =\{B_N^\Box+(B_N^\Box)^\sharp+\widehat C_N^{an}\}/A.       \tag{3}
\]

This is a concrete finite integral, independent of H values, H quadrature or source-inferred edge data. It retains the true gamma factor and the entire heat phase. The exact edge is the same expression with both integrals infinite, as follows from [Polymath section 4, (39)-(41)][polymath]. That representation is valid for **any fixed N**. By contrast, Proposition 6.2's RS coefficient remainder specifies N=floor(a); it cannot be assigned unchanged to the alternate frozen cutoff.

In (2) all bounds and q are fixed while differentiating z. Since V_t and S_t are the same at every center, same-N models are identical on every overlap. Their t dependence must be included if a later consumer differentiates time. The finite integrands are holomorphic in z; gamma poles remain far from these disks. No printed nonholomorphic correction, RS polynomial truncation, negative-u order selection or profile Taylor conversion is used in this model. The common exact Chat is its removable analytic continuation from UAR-01 and cancels from the exact-minus-model error.

Numerical quadrature and evaluation errors for the **retained** finite model have not been incurred here: (2) is an exact definition. Any numerical UAR-04 consumer must enclose them and charge their acquisition cost. No claim of a fast evaluator or cost gain is made.

## 2. Complete uniform error theorem

Put

\[
Z_c=\exp(-L/4-tL^2/16),\quad
\epsilon_c=1000 Z_c e^{-3.99L}.
\]

Let e_(edge,N)=(\mathscr E_N+\widehat C_N^an)/A be UAR-01's complete exact edge discrepancy, and d_(edge,N)=e_(edge,N)-ehat_(edge,N).

**Theorem 1.** For either frozen cutoff, uniformly on D_c,

\[
|d_{edge,N}|<\epsilon_c.                                  \tag{4}
\]

Throughout W_c,

\[
|(d_{edge,N})_x|<2L\epsilon_c,\qquad
|Z_{d_{edge,N}}|<9\epsilon_c.                             \tag{5}
\]

At the center the derivative factor improves to L. The largest ceilings over the sector satisfy epsilon_c<4.3e-35 and 9epsilon_c<3.9e-34. These are complete **model-error** payments, excluding the retained signed model itself. The value and first derivative are the selected UAR-01 budget; no second-jet consumer is activated.

### Geometry and normalizer, including cutoff overlaps

Write z=X+iy, T=X/2+pi t/8, a=sqrt(T/(2pi)). On D_c and its enclosing rectangle,

\[
T>3\times10^9,\quad q\ge22025,\quad |q-a|<.500001,
\quad\sigma=\tfrac12-y/2\in[.475,.525].                    \tag{6}
\]

Indeed c>=4pi exp(20)>6e9 and the entire a-variation over [c-R,c+R] is <2e-7. Either extremal integer therefore has the q-distance stated in (6), including a disk containing a cutoff. Also V_t,S_t>=2sqrt(L), and |sigma+sqrt(t)v|<.525+2sqrt(2)<4 on the retained v interval.

Let P(t,X)=exp(tpi^2/64)|M0(iT)|. A safe **one-channel** normalization bound is

\[
P(t,X)/|A(t,z)|<2Z_c.                                    \tag{7}
\]

For an explicit source of (7), use the [earlier matching note][matching], equations (20)-(21) and its prefactor estimate. At y=0 it bounds P/A(t,X) by

\[
Z_*=q_-^{-1/4}\exp\left\{-t\log^2q_-/16
 +\frac{3\sqrt{\log^2q_++\pi^2/4}+3.58}{c-R-8.52}\right\},
\quad q_\pm=(c\pm R)/(4\pi).
\]

The ratio Z_*/Z_c is at most exp((3L+10)/(.99c))<1.001. UAR-02's explicit alpha/beta bounds give |(log A)_z|<L/4+.501 on the containing rectangle; a vertical displacement |y|<=R costs at most exp(.25+.501/20)<1.4. Thus (7) has room. The two channels together cost at most 4Z_c, not 2Z_c. This avoids mixing center normalizers with actual complex A(z).

### A global contour majorant

Set F(r)=T arg(w_q(r))-2pi q r-2pi r^2. Since q is half-integral,

\[
|e^{i\pi w_q}-e^{-i\pi w_q}|\ge2.
\]

For r>=-q, arg(w_q)<=r/q: the derivative of arg(w_q)-r/q is -2r(q+r)/(q|w_q|^2), with value zero at r=0. Completing the square gives F(r)<=4-pi r^2, since

\[
\frac{(T/q-2\pi q)^2}{4\pi}<4.
\]

For r<-q, arg(w_q)<=-pi/2 and F(r)+pi r^2<=pi q^2-pi(r+q)^2-pi T/2<0, because q^2<T/2. Furthermore |d_r log|w_q||<=2/q, so with delta_q=|log(q/a)|<.000024,

\[
|J_N(u+iT)|\le\sqrt2\,a^{-u}
 \exp\{4+\delta_q|u|+u^2/(\pi q^2)\},\qquad u\in\mathbb R. \tag{8}
\]

This holds on the entire Gaussian line for either frozen N; no natural-cutoff expansion is invoked.

A direct gamma/reflection bound and a horizontal Taylor estimate for m0 give, for all real u,

\[
\frac{|M(u+iT)a^{-u}|}{|M_0(iT)|}
 \le\exp\left\{\frac1{2T}+\frac{3|u|}{2T}
                      +\frac{u^2}{4(T-3)}\right\}.        \tag{9}
\]

For (9), |alpha(iT)-log(a)-i pi/4|<=3/(2T) and |alpha'|<=1/[2(T-3)] on the whole horizontal segment. To pay the gamma factor on that **unbounded** line, put w=(u+iT)/2. If Re w>=0, the [DLMF logarithmic Stirling remainder][stirling] gives |S_Gamma(w)|<=sec^2(arg w/2)/(12|w|)<=1/(3T). If Re w<0, apply that right-half-plane bound at -w, and use the exact [gamma reflection identity][reflection]. Relative to the two Stirling factors it yields exp(S_Gamma(w)+S_Gamma(-w))=(1-exp(2pi i w))^(-1). Thus

\[
\log|\Gamma(w)/\Gamma_{St}(w)|
 \le1/(3T)-\log(1-e^{-\pi T})<1/(2T),
\]

where Gamma_St is the leading Stirling factor. The reflection payment -log(1-exp(-pi T))<1/(6T) holds for T>=3e9. Only this modulus inequality is needed. This proves (9) without applying a fixed-sector Stirling bound to the infinite left tail or using the smaller shortcut constant discussed in S03 Note 07.

Combining (8)-(9), in M0(iT) units the exact integrand is bounded by sqrt(2) exp(4+epsilon0+lambda|u|+Q u^2), where

\[
\epsilon_0<2\times10^{-10},\quad \lambda<.000025,\quad Q<10^{-9}.
\]

With u=sigma+sqrt(t)v this gives the Gaussian-weighted bound

\[
78\exp\{.000006|v|-(1-10^{-10})v^2\}.                     \tag{10}
\]

### Complement of the retained rectangle

Split the omitted set into |v|>V_t with the **whole** r contour, plus |v|<=V_t and |r|>S_t. These sets cover the complement once; no approximate Gaussian tail is silently dropped.

The two v tails in (10), divided by sqrt(pi), have Mills bound

\[
\frac{156}{\sqrt\pi}
 \frac{e^{-(1-10^{-10})V_t^2+.000006V_t}}
 {2(1-10^{-10})V_t-.000006}
 <100e^{-3.99L}.                                         \tag{11}
\]

Here V_t>=2sqrt(L), L>=20, and 4e-10+12e-6/sqrt(L)<.01 justify the weakened exponent uniformly. The remaining prefactor is already <100 at L=20 and decreases.

For the central v interval, |u|<4 and 2|u|/q<.001. On |r|>=S_t, the logarithmic-radius bound and phase give -pi r^2+.001|r|<=-3r^2. Equations (8)-(9) before the r integration, followed by a Mills bound, therefore pay the two contour tails by

\[
\frac{\sqrt2 e^{4+4(.000024)}
 e^{1/(2T)+6/T+4/(T-3)}}{6S_t}\,e^{-3S_t^2}
 <50e^{-12L}                                             \tag{12}
\]

in the same M0(iT) units. The retained v Gaussian mass is at most one. Bounds (11)-(12), the external heat scalar counted once in P, and (7) for both channels give

\[
|d_{edge,N}|<4Z_c\{100e^{-3.99L}+50e^{-12L}\}
 <1000Z_c e^{-3.99L}.
\]

This proves (4). The exact-minus-finite error is holomorphic, with uniform domination on a neighborhood of the disks. Cauchy on the **combined** normalized error gives the derivative factor 2L on W_c. Real symmetry gives |Z_d|^2=d^2+(d_x/omega)^2, and |omega|>L/4.001 yields sqrt(1+8.002^2)<9, proving (5). No derivative is taken of a printed real-parameter inequality.

## 3. Exact entering-mode compensation

The residue identity underlying the exact fixed-contour representation is

\[
\mathscr E_n-\mathscr E_{n-1}
 =-\{R_n(s)+R_n(1-s)\}=-m_n^{heat}.
\]

Let Bhat_N=B_N^Box+(B_N^Box)^sharp. At a crossing use the same t, same disk and both N=n-1,n. Equation (4) gives the **complete** model-matching statement

\[
\left|\frac{m_n^{heat}+\widehat B_n-\widehat B_{n-1}}A\right|
 <2\epsilon_c.                                          \tag{13}
\]

Its derivative costs at most 4L epsilon_c on W_c, by Cauchy on the common holomorphic difference. Thus the entering exact heat mode and matching edge change cancel before a norm; neither is charged as an independent full-mode disk. Replacing the exact heat mode in (13) by its prescribed g_n(1+chi_n) pair costs precisely the single-mode UAR-02 remainder, with its full weights and derivative payment. This is available from that theorem, without H calibration.

The compensated edge model (3) includes Delta Chat with its positive sign. All leading correction profiles and gamma factors are retained. Their numerical evaluation error, if a consumer evaluates them, remains its explicit extra payment.

## 4. The original corrected transitions have a summable allowance

For the original UAR-01 approximation define h_n=f_n-f_(n-1)=[g_n(s)+g_n(1-s)-Delta Chat_n]/A. At a crossing c=xi_n=4pi(n^2-t/16) in J_t:

**Theorem 2.** On its common disk D_c,

\[
|h_n|<8Z_c/c,\qquad
|Z_{h_n}(c)|<32.008Z_c/c<3Z_c/n^2.                        \tag{14}
\]

For every physical prefix, including both endpoint conventions of UAR-01,

\[
\sum_{a_t<\xi_n\le x}|Z_{h_n}(\xi_n)|
 <3.01e^{-13/(16t)}<2.639\times10^{-7}.                    \tag{15}
\]

This is an upper allowance for the corrected transition sum; no cancellation between different crossings is assumed. It replaces the divergent independent raw-mode rule in its **stated class**, not a lower bound for actual theta errors.

### Proof of the common-disk bound

Use the [earlier Note 22][matching], equations (13)-(15), for the entering leading mode minus the **printed** jump. On x in [c-R,c+R], 0<=y<=R, its parameters satisfy

\[
E<.025001/c,\quad\sigma_*\le.525,\quad\Delta<.526,
\quad D_0<3.000001/c,\quad D_1<1.000001/c,
\quad D_s<3.526002/c.
\]

These follow from a(c)=n and d<=R/(8pi a_-). Substitution in its explicit matching exponent gives Lambda_edge<1.81/c. Its terms involving d^3, E^2 and D_s^2 have their actual additional inverse-c factors, not a constant independent of height. The printed physical mismatch is consequently <3.621 P/c.

Pay the printed-to-analytic jump separately. Its exact single-wave formula is

\[
\Delta\widehat C_n=(-1)^{n+1}e^{-\pi z/8}D_n(z),\quad
D_n=\frac{\sqrt\pi}4e^{-\pi^2t/64}\tau^{3/2}
                  (\cos\psi-\sin\psi/\tau),
\quad\psi=2\pi(a-n)^2-\pi/8.
\]

On the disk |a-n|/|a|<.0251/c, |psi'|<.0126/c and |psi+pi/8|<1e-11. Differentiating the slow factor gives the bracket

\[
\frac3{4\tau}(\cos\psi-\sin\psi/\tau)
 +(-\sin\psi-\cos\psi/\tau)\psi'
 +\frac{\sin\psi}{2\tau^2},
\]

whose modulus is <1.52/c. The amplitude relative to the real slice changes by <1.000001 on a vertical segment; its real value without the trigonometric bracket is at most 2P. Since |y|<=R<=.05, this pays the complete printed-to-analytic difference by <.16P/c. The combined mismatch is <3.8P/c. Divide by the **actual** complex A and use (7); reflection supplies the lower half-disk, proving |h_n|<8Z_c/c.

Only now use holomorphy and real symmetry. Real Schwarz-Pick on D_c gives |Z_h(c)|<= (8Z_c/c) max{1,1/(R|omega(c)|)}<32.008Z_c/c. Finally c/n^2>12 gives the last inequality in (14). Independent value/derivative boxes would not give this sharper coefficient.

For the sum, every included n exceeds u=exp(1/(2t)); Z_c<=exp(-5/(16t)) and sum_(n>u)n^-2<=1/(u-1). Thus the total is bounded by

\[
\frac{3e^{-13/(16t)}}{1-e^{-1/(2t)}}<3.01e^{-13/(16t)}.
\]

All prefixes and their left/right descriptions have this same majorant. It tends to zero as t decreases; at t=1/20 it is already below the last ceiling in (15). This is the specific improvement over S04-T3's raw independent-mode allowance >.99 exp(1/(4t)). It does not bound the signed retained residual endpoints in UAR-01 (16).

## 5. Complete ledger, validation and next obligation

| Term | Status and destination |
| --- | --- |
| Full gamma factor, Gaussian heat weight and phase, descending RS contour | Retained exactly in (2), independently of H. |
| Omitted Gaussian v tails, whole r contour | Paid in (11). |
| Omitted contour r tails, central v | Paid in (12); complement is disjoint from the first term. |
| Both reflected channels and complex normalizer | Paid once by (7); Cauchy applied only to their combined holomorphic normalized error. |
| Printed/asymptotic RS model and profile conversions | Absent from (2); no fixed-B Taylor chart or coefficient remainder is transferred. Common exact Chat cancels from model error. |
| Adjacent exact heat modes | Compensated by the edge change with complete error (13); prescribed finite replacement uses UAR-02. |
| Original leading corrected transition | Full analytic mismatch paid before Schwarz-Pick; every prefix has (15). |
| Retained-model quadrature/rounding, signed endpoint variation | UAR-04 obligations. No quadrature evaluation or cost benefit is claimed by defining the exact finite integral. |
| Physical anchor and return | UAR-05 obligations; normalizer derivatives and forced residual equation remain exactly those of UAR-01. |

The [primary 192/256-bit receipt][record] checks the elementary uniform reserves, tails, normalizer and transition constants, exact sign/compensation fixtures, domain and source-identity guards. The [separate same-model review][review] includes a fresh same-checker scalar replay; this is not implementation-independent validation or a proof by sampled heights. The written arguments supply the uniform domain.

The [fresh source-own control replay][control-record] rejects five existing event boxes and retains the separate Euler negative-Laguerre witness in unchanged consumers. Its historical producer date is preserved separately. Finite-prime/weighted-square controls lack unchanged full normalized theta reflection/coefficient data; reflected/shape/primitive controls lack the specific theta square expansion and matching arithmetic contour; Euler controls change the level and coefficients; polynomial/counter-kernel/wall controls lack this arithmetic representation. Generic rotation identities distinguish none of them. No theta allowance is assigned to altered sources, and analytic-only controls receive no invented event box.

**Decision:** UAR-03 is Complete as a uniform edge-model/error and coherent transition theorem. UAR-04 is Ready to recombine the prescribed finite correction with (3), enclose the retained signed expression, and include (15) or a stronger signed transition treatment. It must compare the **complete** paid allowance in the same norm and domain. The bounded-contour representation has no demonstrated acquisition advantage. No new physical margin, real bridge coverage, complex exterior or Newman bound is established.

[contract]: ../../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[finite]: 08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md
[matching]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[polymath]: https://arxiv.org/html/1904.12438v2#S4
[stirling]: https://dlmf.nist.gov/5.11#ii
[reflection]: https://dlmf.nist.gov/5.5#E3
[record]: ../numerics/UAR03_UNIFORM_COHERENT_EDGE_20261019.json
[review]: ../reviews/09_UAR03_UNIFORM_COHERENT_EDGE_INTERNAL_REVIEW_20261019.md
[control-record]: ../numerics/UAR03_SOURCE_CONTROLS_20261019.json
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
