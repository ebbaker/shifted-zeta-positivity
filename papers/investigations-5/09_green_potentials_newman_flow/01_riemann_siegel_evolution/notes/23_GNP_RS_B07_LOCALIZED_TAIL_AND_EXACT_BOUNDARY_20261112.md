# GNP-RS-B07 — localized complete-arm tails and exact convolution boundaries

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0006, thread
`01a1d151-91b1-7663-8f10-07d0b4f94163`. Actual backend model and reasoning
effort are unavailable in the recorded configurations. Three analytical
helpers contributed arithmetic, oscillatory and boundary checks; their
inherited settings are not independently identified. Recommendations are
prospective, not provenance.

**Status: proved in-note from named inherited inputs, with contributing
separate-agent internal checking.** See [Review12][review]. This is the
bounded B07 continuation requested in [Note22][return06]. Its quantitative
milestone is a shorter uniform interval range, from
\(\ell\ge U^{3/8+\rho}\) to \(\ell\ge U^{1/4+\rho}\), with the same
logarithmic residual and Green mean bounds. The separate boundary penalty
is removed by retaining the exact convolution weight. No every-center
estimate is proved.

This is an averaged quantitative milestone under [target01][a01]. Read
[result summaries][results], specifically [heat-flow cluster11][r11], and
[avoid][avoid], especially [premise02][a02], [scope07][a07] and
[separate-bounds12][a12]. The [collision controls][controls] are screened
against named premises in Section 8. The source, carrier, physical clock,
strip, depth and radius remain those of B06. No E08 or manuscript
integration is issued.

## 1. Statement and inherited inputs

Use [Note21][b06] Sections 1–3 for the exact definitions of
\(R_P(X,1)\), \(\mathscr R(U,\ell;P)\), \(E_P\), \(Q=E_P^{-1}\),
\(D_P\), \(\mu_P\), and the complete normalized theta field. Explicitly,
\[
 L_x=\log(x/(4\pi)),\qquad
 \mathscr R(U,\ell;P)=\frac1\ell\int_U^{U+\ell}R_P(X,1)dX,
 \qquad
 \mu_P=\sum_{\substack{k>1\\(k,D_P)=1}}k^{-3/2}\le2P^{-1/2}.
\]
The prime cutoff P is constant on the outer interval. At each center X,
physical time \(\lambda=1/L_X\) stays fixed in the spatial window
\(W_X=[X-r_X,X+r_X]\), with
\[
 r_X=(32/\pi)\log X,\qquad K(t)=\frac1{16\cosh(\pi t/8)},
 \qquad\int_{\mathbb R}K=\frac12.
\]
The field still satisfies \(\partial_\lambda H=-H_{zz}\), with carrier
\(C_-\), strip \(0<\Im z<8\), center \(X+4i\), and defect parameters
\(d=1/2,r=1\). All conclusions concern c=1.

**Theorem.** For each fixed \(0<\rho\le1/4\), all sufficiently large
real U, every integer \(2\le P\le\lfloor L_U^2\rfloor\), and
\(U^{1/4+\rho}\le\ell\le U\),
\[
 \boxed{\left|\mathscr R(U,\ell;P)-\mu_P\right|
 \le C\left(\frac{\sqrt{\mu_P}}{L_U}+L_U^{-2}\right)
       +O_\rho\left(U^{-\min(1/128,\,5\rho/24)}\right).}       \tag{B07.1}
\]
Consequently, for \(P_U=\lfloor L_U^2\rfloor\), uniformly on this range,
\[
 \mathscr R(U,\ell;P_U)=\mu_{P_U}+O_\rho(L_U^{-3/2})
                    =O_\rho(L_U^{-1}),                      \tag{B07.2}
\]
\[
 \frac1\ell\int_U^{U+\ell}J_{1/L_X}(X)dX=O_\rho(L_U^{-1/3}),
 \qquad
 \frac{|\{X\in[U,U+\ell]:J_{1/L_X}(X)\ge h\}|}{\ell}
          =O_{h,\rho}(L_U^{-1})\quad(h>0\text{ fixed}).       \tag{B07.3}
\]
The constants in the inherited complete-field comparison and their finite
onsets remain unevaluated; no numerical onset is certified. The proof
below supplies parameter dependence and finite onset inequalities.

At auxiliary time \(1/L_u\), the inherited complete-arm representation is
\[
 A(u)=\sum_{n\le N_u}w_n(u)e^{i\nu(u)\log n},\quad
 N_u=\lfloor\sqrt{u/(4\pi)}\rfloor,\quad
 w_n(u)=n^{-3/4}e^{(\log n)^2/(4L_u)}\le n^{-5/8},
\]
\[
 \nu(u)=u/2+\pi/(8L_u),\quad
 \phi(u)=u(L_u-1)/2+\pi/8+7\pi/4,\quad
 S=A+e^{i\phi}\overline A,\quad
 |V_{1/L_u}(u)-S(u)|\le C_Hu^{-1/4}.                         \tag{B07.4}
\]
This uses the same HDA CS6 fixed charts \(r=1,b=9\), CS25 fractional
cutoff correction and E01/E03/E04 buffers as Note21 Sections 2 and 6.
The full correction and residual are included. The provider has inherited
internal review; it is not independently re-audited here. The only new
external analytical input is a discrete third-derivative test, verified
in the [source-use record][sources] and applied in Section 4.

## 2. Retain the exact boundary weight

Put \(r_*=(32/\pi)\log(2U)\),
\(J=[U-r_*,U+\ell+r_*]\subset[U/2,3U]\), and
\[
 W(x)=\int_U^{U+\ell}K(x-X){\bf1}_{|x-X|\le r_X}\,dX,
 \qquad d\sigma(x)=\frac{2W(x)}\ell\,dx.
\]
Then \(0\le W\le1/2\), \(\operatorname{supp}W\subset J\).
Let \(W_\infty=K*{\bf1}_{[U,U+\ell]}\) and \(D=W_\infty-W\ge0\).
Since \(W_\infty'=K(x-U)-K(x-U-\ell)\),
\(\operatorname{TV}(W_\infty)\le1\). For fixed X the removed
function \(K(x-X){\bf1}_{|x-X|>r_X}\) has total variation
\(4K(r_X)\), counting both jumps. Triangle inequalities for each finite
partition, followed by integration in X, prove
\[
 \operatorname{TV}(D)\le\int_U^{U+\ell}4K(r_X)dX
 \le\frac{\ell}{2U^4},\qquad
 \operatorname{TV}(W)\le1+\frac{\ell}{2U^4}\le\frac32.       \tag{B07.5}
\]
Here \(K(r_U)\le U^{-4}/8\). No derivative of the moving radius is
needed. Also \(\int_{|t|>r_X}K(t)dt\le(2/\pi)X^{-4}\), so
\[
 1-\frac4\pi U^{-4}\le m_\sigma:=\int d\sigma\le1.          \tag{B07.6}
\]
For the auxiliary relative square
\[
 F=|Z(A)|^2,\quad
 Z(A)=AQ-1+e^{i\phi}(Q/\overline Q)\overline{AQ-1},
\]
Fubini is exact:
\[
 \frac1\ell\int_U^{U+\ell}\int_{W_X}K(x-X)F(x)dx\,dX
                  =\frac12\int F\,d\sigma.                 \tag{B07.7}
\]
Thus the arithmetic calculation can use \(\sigma\) directly. There is
no comparison with a sharp height indicator and no pointwise edge-envelope
cost. Restoring the constant diagonal costs only
\(\mu_P(1-m_\sigma)\le(4/\pi)\mu_PU^{-4}\).

## 3. Smooth majorant and paid freezing of the complete tail

For this and the next three sections suppose
\(r_*\le\ell\le\sqrt U\). Fix once and for all a nonnegative smooth
function \(\psi\), supported on \([-1/2,1/2]\), of integral 1; for
example the normalized function \(\exp[-1/(1-4v^2)]\) inside that
interval and zero outside. Set
\(\chi={\bf1}_{[-3/2,5/2]}*\psi\). It is smooth, nonnegative,
supported on \([-2,3]\), equals 1 on \([-1,2]\), and has integral 4.
Since \(J\subset[U-\ell,U+2\ell]\), for every function T,
\[
 \int|T|^2d\sigma\le\frac1\ell\int_{\mathbb R}
           \chi((u-U)/\ell)|T(u)|^2du.                     \tag{B07.8}
\]
This is used only for upper bounds on nonnegative norms. It does not
replace the exact weight in the coefficient diagonal or reflected terms.

Choose an integer \(2\le Y\le N_{U-2\sqrt U}\) and write
\(A_Y=\sum_{n\le Y}w_n(u)e^{i\nu(u)\log n}\). On the full majorant
support \([U-2\ell,U+3\ell]\), freeze the omitted arm to
\[
 T_Y^0(u)=\sum_{Y<n\le N_U}w_n(U)
       e^{i(u/2+\pi/(8L_U))\log n}.                         \tag{B07.9}
\]
On common active indices, differentiating only the weights and the small
\(\pi/(8L_u)\) correction gives total change
\(O(\ell U^{-13/16})\). Indeed their logarithmic derivatives are
\(O(1/U)\) and \(O(1/(UL_U))\), respectively, and
\(\sum_{n\ll\sqrt U}n^{-5/8}=O(U^{3/16})\). If an index is active
at one endpoint but not the other, its size is comparable to \(\sqrt U\).
The number of such indices is \(O(1+\ell/\sqrt U)\), including every
integer cutoff jump, and each has magnitude \(O(U^{-5/16})\).
For these boundary indices the frozen weights satisfy the same bound
up to an absolute constant. Hence, throughout the majorant support,
\[
 |A-A_Y-T_Y^0|\le C\{\ell U^{-13/16}
          +(1+\ell/\sqrt U)U^{-5/16}\}\le C U^{-5/16}.       \tag{B07.10}
\]
No derivative of the floor function or of the exact field remainder is
assumed. The norm-square freezing cost is \(O(U^{-5/8})\), using
\(|a+b|^2\le2|a|^2+2|b|^2\). The head and full arm admit the same
comparison, with the corresponding finite index sets.

## 4. All pairs in the smoothed frozen mean

Use \(\widehat\chi(\xi)=\int\chi(v)e^{iv\xi}dv\). Repeated
integration by parts gives, for each fixed A and j=0,1,
\(|\widehat\chi^{(j)}(\xi)|\le C_{A,j}(1+|\xi|)^{-A}\).
The exact frozen expansion is
\[
 \frac1\ell\int\chi((u-U)/\ell)|T_Y^0(u)|^2du
 =\sum_{Y<m,n\le N_U}w_m(U)w_n(U)
 e^{i\nu_U\log(n/m)}
 \widehat\chi\left(\tfrac\ell2\log(n/m)\right),
 \quad\nu_U=U/2+\pi/(8L_U).                                \tag{B07.11}
\]
The diagonal is at most \(16Y^{-1/4}\). Split every off-diagonal
pair into noncomparable \(n\ge2m\) (and its reverse), or
\(m<n<2m\) (and its reverse). The former contribute at most
\(C_AU^{3/8}\ell^{-A}\), because \(|\log(n/m)|\ge\log2\)
and the absolute arm sum is \(O(U^{3/16})\).

For the latter, write \(n=m+h\), partition m into dyadic blocks
\([N,2N)\), and retain all constraints
\(m>Y,m+h\le N_U,1\le h<m\). For each fixed h these restrict m
to a single interval, possibly empty. Define
\[
 f_h(x)=\frac{\nu_U}{2\pi}\log\frac{x+h}{x}.
\]
On its permitted block, \(f_h'''<0\) and
\[
 \frac{3Uh}{512\pi N^4}\le |f_h'''(x)|
                           \le\frac{3Uh}{\pi N^4}.         \tag{B07.12}
\]
These deliberately loose constants are uniform also on every partial
interval. In particular the derivative has fixed sign and bounded ratio.

The discrete third-derivative estimate used here is
\[
 \left|\sum_{n\in I}e^{2\pi if(n)}\right|
 \le C_c\{N\lambda^{1/6}+N^{1/2}\lambda^{-1/6}\},          \tag{B07.13}
\]
when I has length at most N and
\(\lambda\le|f'''|\le c\lambda\) with fixed sign. This is
inequality III in [Elkies's author-hosted handout][elkies]. Briefly,
differencing and the second-derivative estimate give
\(|S|^2\ll N^2/H+N^2\lambda^{1/2}H^{1/2}
 +N\lambda^{-1/2}H^{-1/2}\).
For \(N^{-3}<\lambda<1\) choose \(H\asymp\lambda^{-1/3}\);
outside that range the trivial bound N suffices. Integer choices and
translated partial intervals alter only the fixed constant. This
establishes the version required for summation by parts, not merely a
continuous oscillatory integral estimate.

With (B07.12), all partial sums over m are bounded by
\[
 C\{U^{1/6}h^{1/6}N^{1/3}
                      +U^{-1/6}h^{-1/6}N^{7/6}\}.          \tag{B07.14}
\]
Let \(\theta(x)=\log(1+h/x)\). On the block,
\(\theta\asymp h/N\), \(|\theta'|\ll h/N^2\).
The logarithmic derivative of \(w_x(U)\), for \(x\le N_U\), lies
between \(-3/(4x)\) and \(-1/(2x)\). Therefore the amplitude
\[
 a_h(x)=w_x(U)w_{x+h}(U)\widehat\chi(\ell\theta(x)/2)
\]
has supremum plus total variation at most
\[
 C_A N^{-5/4}(1+\ell h/N)^{-A}.                            \tag{B07.15}
\]
To check the Fourier derivative contribution, its integrated factor is
\(O(\ell h/N)\); use one additional power of Fourier decay to absorb
it. Cutting down to the permitted interval adds only endpoint bounds.

Summation by parts with (B07.14)–(B07.15), and
\[
 \sum_{h\ge1}h^r(1+qh)^{-A}\le C_{r,A}q^{-r-1}
 \quad(r>-1,\ A>r+1,\ q>0),
\]
gives, on each dyadic m block,
\[
 C\{U^{1/6}N^{1/4}\ell^{-7/6}
                  +U^{-1/6}N^{3/4}\ell^{-5/6}\}.           \tag{B07.16}
\]
The elementary sum bound follows by integral comparison for \(q\le1\),
and by summing \(q^{-A}h^{r-A}\) for \(q\ge1\).
Both powers of N in (B07.16) are positive, so summing the dyadic blocks
geometrically up to \(N_U\ll\sqrt U\) yields
\[
 C\{U^{7/24}\ell^{-7/6}+U^{5/24}\ell^{-5/6}\}.             \tag{B07.17}
\]
There is no blockwise Cauchy–Schwarz loss or omitted cross-block pair:
the partition is by the smaller index m in the full expansion. No
logarithmic factor is required in this step.

Taking A=4 for the noncomparable pairs and including (B07.10), define
\[
 \mathcal E(U,\ell)=U^{7/24}\ell^{-7/6}
                  +U^{5/24}\ell^{-5/6}
                  +U^{3/8}\ell^{-4}+U^{-5/8}.              \tag{B07.18}
\]
For a sufficiently large fixed constant \(C_\chi\), depending only on
our fixed bump and the fixed derivative-test ratio,
\[
 \boxed{\begin{aligned}
 \int|A-A_Y|^2d\sigma&\le A_1:=C_\chi(Y^{-1/4}+\mathcal E),\\
 \int|A|^2d\sigma,\quad\int|A_Y|^2d\sigma
                       &\le A_0:=C_\chi(1+\mathcal E).
 \end{aligned}}                                           \tag{B07.19}
\]
For the last line use the same all-pair proof with the full or head index
set; its diagonal is bounded by \(4\zeta(5/4)\). Choose \(C_\chi\ge1\).
All actual cutoff activations and the small phase correction have been
paid before using the frozen sum. This is a uniform translated-height
estimate on the canonical trajectory, not a prime-phase ensemble average.

## 5. The finite-head ledger against the exact weight

Retain B06's integer-size truncations \(Q_M,E_M,B_M=A_YQ_M-1\),
\(m_M=\overline Q_M E_M\), and products
\[
 H=\prod_{p\le P}(1-p^{-3/4})^{-1},\quad
 T=M^{-\eta}F_{3/4-\eta}(P),\quad
 F_s(P)\le e^{C_sP^{1-s}},\quad
 C_s=[(1-s)(1-2^{-s})]^{-1}.
\]
In particular both multiplier tails are at most T and
\(\|\overline Q/Q-m_M\|_\infty\le2HT\). Set
\[
 L_0=L_{U-r_*},\quad K_0=\lfloor M\rfloor Y,\quad
 a_0=\frac{C_2}{4L_0}+C_0Y^{-1/8}+C_0M^{-1/8},\quad
 D_0=2\sqrt{\mu_P}a_0+a_0^2,
\]
with the same \(C_0\le25\), \(C_2\le81(32/e)^2\) as B06.
The pointwise coefficient-diagonal estimate remains valid on J, with
\(L_0\) in place of \(L_U\). Define
\[
 s_0=150000\frac{K_0(1+\log K_0)}\ell,\quad
 b_0=(\sqrt{\mu_P}+a_0)^2+s_0,\quad
 c_0=8000\frac{H^4Y^{3/4}}{\ell L_0}.                      \tag{B07.20}
\]
Here is the full weight audit, rather than an appeal to an unweighted
estimate. For \(g_k=k^{-5/8}\tau(k)\), the B06 coefficients obey
\(\sup|b_k|\le g_k\), \(\operatorname{TV}(b_k)\le2g_k\), and
\(\sum g_k^2\le625\). A product amplitude a therefore has
\(\sup|a|\le g_kg_l\), \(\operatorname{TV}(a)\le4g_kg_l\).
Equations (B07.5) and \(\|W\|_\infty\le1/2\) give
\[
 \sup|Wa|+\operatorname{TV}(Wa)\le4g_kg_l.                 \tag{B07.21}
\]
The same-arm partial integral bound \(12/|\log(k/l)|\), the harmonic
row sum and the normalization \(2/\ell\) yield the constant
\(12\cdot8\cdot2\cdot625=120000<150000\). Thus
\[
 \left|\int|B_M|^2d\sigma-\mu_P\right|
       \le D_0+s_0+\mu_P(1-m_\sigma),\qquad
 \int|B_M|^2d\sigma\le b_0.                               \tag{B07.22}
\]
For reflected phases \(-\phi+\nu\log(kl e/d)\), keep the gates
\[
 2\log Y+3\log M\le(7/8)L_0,                              \tag{B07.23}
\]
\[
 \frac\pi{8(U-r_*)^2}(L_0^{-2}+2L_0^{-3})
       (2\log Y+3\log M)\le\frac1{12U}.                   \tag{B07.24}
\]
On J, \(\phi''\ge1/(6U)\), so (B07.24) gives
\(\psi''\le-1/(12U)\); (B07.23) gives \(\psi'\le-L_0/16\).
Impose also \(1/4\le\nu'\le1/2\). The partial integral bound is
\(48/L_0\). Applying (B07.21), the absolute coefficient envelope
\((8/3)HY^{3/8}\), and multiplier coefficient sum \(H^2\), gives
\[
 \left|\int2\Re(e^{-i\phi}B_M^2m_M)d\sigma\right|\le c_0,
\]
since \(2\cdot2\cdot48\cdot4(8/3)^2<8000\).
Every retained rational frequency is included; all omitted frequencies
remain paid by the complete-arm and multiplier tails.

Because \(m_\sigma\le1\), the B06 Cauchy–Schwarz comparisons hold
in this weighted norm with the same constants:
\[
 \left|\int(|Z(A)|^2-|Z(A_Y)|^2)d\sigma\right|
                         \le16H^2\sqrt{A_0A_1},
\]
\[
 \left|\int\{ |Z(A_Y)|^2-
 [2|B_M|^2+2\Re(e^{-i\phi}B_M^2m_M)]\}\,d\sigma\right|
 \le8T\sqrt{A_0b_0}+4T^2A_0+4HTb_0.                       \tag{B07.25}
\]
Thus tails are paid after multiplication by the actual arithmetic arms.
No product supremum is multiplied by the coefficient-diagonal \(1/L_0\)
error.

The complete-field and fixed physical-time comparison in Note21 Section 6
is pointwise on J and can be reused before Fubini. Under its stated gates,
including
\(T_1(P)=\sum_{p\le P}p^{-3/4}\log p/(1-p^{-3/4})\le L_U^2\),
it costs
\(C_{\rm clk}H^2(U^{-1/32}+r_*U^{-9/16})\). It differentiates
neither the floor nor the exact field remainder. The relative multiplier
has unit modulus. Combining this with (B07.7), (B07.19)–(B07.25) proves
\[
\boxed{\begin{split}
 |\mathscr R-\mu_P|\le{}&D_0+s_0+\tfrac12c_0
 +8H^2\sqrt{A_0A_1}+4T\sqrt{A_0b_0}+2T^2A_0+2HTb_0\\
 &+C_{\rm clk}H^2(U^{-1/32}+r_*U^{-9/16})
              +\frac4\pi\mu_PU^{-4}.
\end{split}}                                               \tag{B07.26}
\]
There is no separate boundary term proportional to
\(r_*U^{3/8}/\ell\). The new ledger is valid on
\(r_*\le\ell\le\sqrt U\) under its gates, even where it is not small.

## 6. Parameter choice and finite onset

Set \(M=U^{1/8}\), \(Y=\lfloor U^{1/8}\rfloor\), \(\eta=1/8\).
For \(\ell\ge U^{1/4+\rho}\), (B07.18) gives
\[
 \mathcal E\le U^{-7\rho/6}+U^{-5\rho/6}
                       +U^{-5/8-4\rho}+U^{-5/8}.           \tag{B07.27}
\]
The corresponding residual tail powers include \(U^{-1/64}\) from
\(Y^{-1/4}\) after a square root, and \(U^{-5\rho/12}\) from the
slower off-diagonal term. The head same-arm cost is
\(O(U^{-\rho}(1+\log U))\); the reflected cost is
\(O(H^4U^{-5/32-\rho}/L_0)\). The Euler tail is
\(T\le U^{-1/64}\exp(C_{5/8}P^{3/8})\), and
\(H\le\exp(C_{3/4}P^{1/4})\). The field-clock cost is smaller.
Also \(L_0\asymp L_U\). After a finite \(\rho\)-dependent gate
absorbing \((1+\log U)U^{-\rho}\), the ledger yields
\[
 |\mathscr R-\mu_P|\le
 C(\sqrt{\mu_P}/L_U+L_U^{-2})
 +G(P)\{U^{-1/64}+U^{-5\rho/12}\},
 \quad G(P)=C\exp\{C(P^{1/4}+P^{3/8})\}.                  \tag{B07.28}
\]
The constants here depend only on the declared fixed inputs and bump.
For \(P\le L_U^2\), \(G(P)=U^{o(1)}\). Impose
\[
 \log G(L_U^2)\le\tfrac12\min(1/64,5\rho/12)\log U.       \tag{B07.29}
\]
This proves (B07.1) for \(\ell\le\sqrt U\). For
\(\sqrt U\le\ell\le U\), use B06 with its parameter
\(\rho_{\rm old}=1/8\). Its power remainder is \(O(U^{-1/128})\),
which suffices for (B07.1). This overlap uses the same field, cutoff and
physical clock; no partition or center-dependent reference is introduced.
At \(\rho=1/4\) the short-range endpoint is simply \(\ell=\sqrt U\).

Other gates are the inherited chart/buffer/correction and clock onsets on
J, \(L_0\ge16\), \(r_*\le U/2\),
\(r_*\le U^{1/4+\rho}\), \(U-2\sqrt U\ge U/2\),
\(2\le Y\le N_{U-2\sqrt U}\), (B07.23)–(B07.24), the
\(\nu'\) and \(T_1\) gates, and the finite logarithm absorption
just stated. They all hold eventually. For the frequency gate,
\(2\log Y+3\log M\le(5/8)\log U\), leaving a fixed margin
against \((7/8)L_0\). Replacing P by \(L_U^2\) in increasing product
gates gives a common onset for every allowed P.

Finally \(\mu_{P_U}=O(L_U^{-1})\) in (B07.1) proves (B07.2).
The same pointwise residual-to-Green transfer of E06, used in Note21
Section 8, gives (B07.3) by concavity and the fixed-h residual threshold.
Explicitly, the inherited transfer gives
\(J_{1/L_X}(X)\le\delta/4+R_{P_U}(X,1)/(2\delta^2)+C/L_U\)
uniformly on the block. Take \(\delta=L_U^{-1/3}\) for the mean;
for fixed h take a sufficiently small constant \(\delta\), then apply
Markov to the residual. No new Green inequality or collision assumption
is inserted.

## 7. What remains toward every center

The first terms in the new complete-tail majorant that fail to tend to
zero at \(\ell=U^{1/4}\) are precisely
\[
 U^{7/24}\ell^{-7/6},\qquad U^{5/24}\ell^{-5/6}.             \tag{B07.30}
\]
Both are order one there. The head same-arm bound with the displayed
M,Y choice also ceases to be small. Smaller head parameters can reduce
that latter loss, but do not remove (B07.30).

**This is a limitation of the displayed absolute summation over shifts
following a discrete third-derivative estimate, not a lower bound on the
actual correlations and not an obstruction to all localized methods.**
The exact convolution boundary now incurs no growing edge penalty.
The remaining arithmetic sum is visible before its absolute bound:
\[
 \sum_h\sum_{m\in I_{N,h}}w_m(U)w_{m+h}(U)
 e^{i\nu_U\log(1+h/m)}
 \widehat\chi\left(\tfrac\ell2\log(1+h/m)\right).          \tag{B07.31}
\]
Its useful shifts have \(h\lesssim N/\ell\). The current proof bounds
each inner sum and then sums absolute values in h. A further gain needs
an applicable stronger estimate for this canonical sum, or another paid
local estimate; a new symbol for its smallness would only restate the gap.

Even the improved intervals still grow with height. Their allowed total
Green mass is \(O(\ell L_U^{-1/3})\), which diverges. A localized
positive defect can fit inside this allowance. Neither a quantitative
persistence estimate along \(X\mapsto(1/L_X,X)\), nor a direct small
value at each center, has been obtained. Spatial convolution and small
exceptional proportion alone supply neither. The full-c, bounded-height,
shrinking-depth, time-zero and positive-threshold exclusions remain open.

## 8. Collision screening and scope

The complete canonical coefficients and the physical theta cosine/heat
operator are used in (B07.4), the logarithmic shifted phase, and the exact
divisor cancellation. Following [controls12][controls] and [premise02][a02]:

| Control family | Premise not retained by that family |
| --- | --- |
| Euler-factor controls and translated sources | Unchanged canonical theta arithmetic coefficients and the corresponding complete-arm/provider identity. |
| Weighted finite-square and finite theta-tail controls | Complete normalized infinite theta coefficients and full source reflection; finite support is insufficient. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Canonical integer-square arithmetic expansion, even when reflection or endpoint/asymptotic data are retained. |
| Finite-prime orbit controls | Full source reflection and the full unchanged theta coefficient sequence; finitely many preserved prime identities do not supply (B07.4). |
| Fixed-event atomic and exact finite-profile controls, including continuous compact extensions | Full theta profile/coefficients; finitely many exact profiles do not identify the complete arm. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic of the unmodified theta field. |
| Fixed-amplitude variable-kernel controls | The actual cosine oscillator/Newman operator, despite retained source amplitude. |
| Earlier heat counter-kernels | The unchanged complete theta source, completion and canonical coefficient identity. |
| RSCT calibrated multiplicative models | The actual height trajectory beyond calibrated data and a complete physical Green-window law. |
| Actual-profile positive-measure relaxation | An actual integer zero configuration satisfying the complete physical field constraints. |

These are premise screens, not claims that a finite collision must
contradict an asymptotic averaged bound. The four-family comparison and
reflection rigidity retain their catalogued conjunction/scope. No listed
control is declared to fail a property it actually preserves. No numerical
collision test or counterexample to the canonical estimate is asserted.
The only negative conclusion here is the scoped nonvanishing of the
majorant (B07.30). It is not a theorem excluding alternative estimates.

## 9. Records and continuation

[Review12][review] records contributing internal checks and residual
limitations. The small [execution record][record] lists source identities,
exact exponent checks and document validation; it is not numerical evidence
for a sign or onset. [Note24][return07] gives the bounded continuation and
model-change guidance. The [sole progress register][progress] owns status.
The [reference-use record][sources] and its manifest retain the exact
primary-source versions outside the repository. No new manuscript snapshot,
height campaign or source/clock substitution was made.

[b06]: 21_GNP_RS_B06_GROWING_CUTOFF_MEAN_20261112.md
[return06]: 22_GNP_RS_B06_RETURN_AND_MODEL_CHANGE_20261112.md
[return07]: 24_GNP_RS_B07_RETURN_AND_MODEL_CHANGE_20261112.md
[review]: ../reviews/12_GNP_RS_B07_INTERNAL_ASSESSMENT_20261112.md
[record]: ../numerics/14_GNP_RS_B07_INPUTS_AND_CHECKS_20261112.json
[progress]: ../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[sources]: ../references/01_GNP_RS_B07_DISCRETE_DERIVATIVE_SOURCE_USE_20261112.md
[elkies]: https://people.math.harvard.edu/~elkies/M229.09/vdc.pdf
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
