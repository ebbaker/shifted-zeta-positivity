# GNP-RS-E03 r1 — exact coherent moment and quadratic-Jensen obstruction

11 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance. Child chat0002 has no recorded
model configuration or reasoning effort. The execution recommendation
was GPT-6.1 Sol.

**Status:** proved in-note from named inherited inputs, with
[same-assistant checking][review]. The [frozen request][request] fixes
the complete theta field \(H_\lambda\), heat equation
\(\partial_\lambda H=-H_{zz}\), exact carrier \(C_-\) of E01 (E2),
and strip \(0<y<8\) with center \(X+4i\) and defect parameters
\(d=1/2,r=1\). Write \(V_\lambda=H_\lambda/C_-\),
\(L_x=\log(x/(4\pi))\), \(R_X=(32/\pi)\log X\) and
\(K(t)=1/[16\cosh(\pi t/8)]\). On the \(c=1\) subfamily of the
original \(\lambda=c/L_X\), \(1/2\le c\le1\), put
\[
 M(X,1)=\int_{|x-X|\le R_X}K(x-X)|V_{1/L_X}(x)|^2\,dx,
 \qquad q_X=\int_{-R_X}^{R_X} K(t)\,dt.
\]
Then
\[
 \lim_{T\to\infty}T^{-1}\int_T^{2T} M(X,1)\,dX=\zeta(3/2).
 \tag{E03a}
\]
The exact quadratic-Jensen allowance of [B02 (B7)][b02] satisfies
\[
 \text{For every sufficiently large } A\text{ there exists }X\ge A
 \text{ with }\mathcal B_J(X,1)\ge m_* .
 \tag{E03b}
\]
This is an obstruction to the exact localized quadratic-Jensen upper
allowance for the frozen every-center margin.

## 1. Complete real field and its diagonal

Apply [HDA Note04 CS3/CS6][hda] at the center of each fixed real chart
\(r=1,b=9\), with \(N_x=\lfloor\sqrt{x/(4\pi)}\rfloor\).
Take the \(V_9\) of [E01 §3.1][e01], satisfying
\(V_9\ge\max\{16,17,16c_9,8\sqrt{P_9+6}\}\).
The enlarged initial charts have radius \(V_9+3\), height 10 for
negative smoothing and radius 2, height \(10+2V_9\) for positive
smoothing. Keep their separate CS3 onsets and the provider's Gaussian
exterior and Taylor gates. The field estimate consumes CS6 at
\(j=0, 0\le\lambda L_x\le8\), with the original
[provider assessment][hda-review]. For real \(x\), the two carriers
have equal modulus. Dividing (E10) by \(C_-\) gives
\[
 V_\lambda(x)=S_\lambda(x)+E_\lambda(x),\qquad
 S_\lambda(x)=\sum_{n\le N_x}w_n(\lambda,x)e^{i\nu(\lambda,x)\log n}
 +e^{2i\Theta(\lambda,x)}
 \sum_{n\le N_x}w_n(\lambda,x)e^{-i\nu(\lambda,x)\log n},
\]
\[
 w_n(\lambda,x)=n^{-1/2}e^{\lambda[(\log n)^2-L_x\log n]/4},
 \quad \nu(\lambda,x)=x/2+\pi\lambda/8,
 \quad \Theta(\lambda,x)=x(L_x-1)/4+\pi\lambda L_x/16+7\pi/8.
\]
The normalized residual is at most \(2h_9 x^{-3/4}\) by CS6.
For the correction in (E11), \(e^{-\kappa\lambda}\le1\) and
\[
 |C_-(\lambda,x)/C_-(0,x)|
  =e^{\lambda(L_x^2-\pi^2/4)/16}\ge1
\]
once \(L_x\ge16\), and
\(|G|\le g_9|C_-(0,x)|\),
\(|a^{-1/2}\mathcal C(a-N_x)|\le f_9 x^{-1/4}\).
The removable singularities of \(\mathcal C\) are covered by
CS25/E11. Together these estimates bound the normalized correction
by \(g_9f_9 x^{-1/4}\) uniformly through all fractional cutoffs.

Set \(v(u)=V_{1/L_u}(u)\) as an auxiliary function. At this time
\(w_n(u)=n^{-3/4}e^{(\log n)^2/(4L_u)}\le n^{-5/8}\), since
\(\log n\le L_u/2\). Each arm is \(O(u^{3/16})\) by summing the
power bound. The pointwise squared-modulus difference between \(v\)
and \(S_{1/L_u}\) is bounded by \(2|S_{1/L_u}||E_{1/L_u}|+|E_{1/L_u}|^2\),
giving \(O(u^{-1/16}+u^{-1/2})\). The diagonal of the two individual
arm squares is \(2\sum_{n\le N_u}w_n(u)^2\).
Extend the weights by zero above the cutoff. They are dominated in
square by \(n^{-5/4}\). For each finite prefix, all terms are present
once \(u\ge4\pi n^2\), and \(w_n(u)^2\to n^{-3/2}\) uniformly for
\(u\in[T,2T]\). The summable tail then gives uniform diagonal convergence
to \(2\zeta(3/2)\).

## 2. All oscillatory terms

Every pair is integrated on its actual interval
\(I_{mn}=[T,2T]\cap[4\pi\max(m,n)^2,\infty)\)). Empty or singleton
intervals contribute zero. On the interval,
\(a_{mn}=w_m w_n\) decreases because
\[
 (\log w_n)'=-\frac{(\log n)^2}{4uL_u^2},\qquad
 \sup a_{mn}+\int_{I_{mn}} |a_{mn}'|\le 2(mn)^{-5/8}.
\]
For a real smooth phase \(\psi\) with monotone derivative and
\(|\psi'|\ge\eta>0\), integration by parts on any subinterval
bounds the unweighted integral by \(3/\eta\). The two endpoint
terms cost \(2/\eta\), and variation of the fixed-sign reciprocal
costs \(1/\eta\). If \(B\) bounds every unweighted partial integral
on \(I_{mn}\), integration by parts against its primitive bounds the
weighted integral by \(B(\sup a_{mn}+\int |a_{mn}'|)\).
This proves the needed amplitude estimate with the cutoff endpoints
included. See also [Shapiro, §2, Theorems 2.5–2.6][shapiro].

For a same-arm pair \(m\ne n\), the phase is
\(\pm\nu(u)\log(n/m)\), where \(\nu(u)=u/2+\pi/(8L_u)\).
Here \(\nu'=1/2-\pi/(8uL_u^2)\ge1/4\) eventually and
\(\nu''=(\pi/(8u^2))(L_u^{-2}+2L_u^{-3})>0\).
Thus the integral is \(O((mn)^{-5/8}/|\log(n/m)|)\).
For \(m\le n/2\), sum using \(\log(n/m)\ge\log 2\) to get
\(O(n^{-1/4})\) for each \(n\). For \(n/2<m<n\), use
\(\log(n/m)\ge(n-m)/n\) and sum the reciprocals of \(n-m\)
to get \(O(n^{-1/4}(1+\log n))\).
Summing in \(n\le N_{2T}\ll\sqrt T\), including both arms and
orderings, gives an averaged cost \(O(T^{-5/8}(1+\log T))\).

The interference between arms is twice the real part of the sum
with phases \(\phi_{mn}=2\Theta(u)-\nu(u)\log(mn)\), where
\(\Theta(u)=u(L_u-1)/4+\pi/16+7\pi/8\). This includes \(m=n\).
On \(I_{mn}\), \(\log(mn)\le L_u\), so
\[
 \phi_{mn}''=\frac1{2u}-\nu''\log(mn),\qquad
 \frac1{8T}\le \phi_{mn}''\le \frac1{2T}.
\]
The lower bound holds once
\((\pi/(8u))(L_u^{-1}+2L_u^{-2})\le1/4\) for \(u\ge T\).
On any subinterval, the portion where
\(|\phi_{mn}'|\le T^{-1/2}\) has length at most \(16\sqrt T\).
The complement has at most two intervals on which the first
derivative bound gives \(3\sqrt T\) each. Thus \(22\sqrt T\) is a
uniform partial-integral bound, including intervals meeting the
stationary region or a cutoff endpoint. The amplitude estimate
gives an averaged cost
\[
 O\left(T^{-1/2}\left(\sum_{n\le N_{2T}} n^{-5/8}\right)^2\right)
 =O(T^{-1/8}).
\]
The diagonal limit, both oscillatory bounds and the squared-error
bound give \(T^{-1}\int_T^{2T}|v(u)|^2\,du\to2\zeta(3/2)\).

## 3. Fixed time in the original moment and convolution

For \(X\) large enough that \(R_X\le X/2\), the entire window has
\(x\asymp X\), and \(|L_x-L_X|\le 2R_X/X\). Consequently
\(L_x/L_X\in[1/2,2]\) eventually and
\[
 |1/L_X-1/L_x|\le 4R_X/(XL_X^2).
\]
At fixed \(x\) and any time \(\lambda\) between these two values,
\(1/2\le\lambda L_x\le2\), inside the provider domain. Since
\((\log n)^2-L_x\log n\le-(L_x/2)\log n\),
the common bound is \(w_n\le n^{-9/16}\). Each arm is \(O(x^{7/32})\).
The cutoff stays fixed in this comparison. The time derivatives
of the weight, \(\nu\), and \(2\Theta\) are
\(w_n[(\log n)^2-L_x\log n]/4\), \(\pi/8\), and \(\pi L_x/8\).
Thus \(\partial_\lambda S_\lambda(x)=O(L_x^2 x^{7/32})\).
The arm difference is \(O(x^{7/32}R_X/X)\) and the difference of
their squared moduli is \(O(R_X X^{-9/16})\).
At each endpoint time the squared-modulus cost of the complete
correction/residual is \(O(X^{-1/32}+X^{-1/2})\) by the same
\(2|S||E|+|E|^2\) bound. Hence replacing the original integrand by
\(|v(x)|^2\) costs \(O(R_X X^{-9/16}+X^{-1/32})\) after integrating
against \(K\), uniformly as \(X\to\infty\). This comparison keeps
\(1/L_X\) fixed in the defining \(x\)-integral of \(M\).

To compute the kernel mass, first set \(s=\pi t/8\). The
substitution \(u=e^s\) gives \(\int_{\mathbb R}\operatorname{sech}s\,ds=\pi\). This gives mass \(1/2\) for \(K\). The two tails beyond \(R_T\) are bounded together by
\((2/\pi)e^{-\pi R_T/8}=(2/\pi)T^{-4}\), so
\(0\le1/2-q_T\le(2/\pi)T^{-4}\).
By Fubini on the enlarged interval
\(J_T=[T-R_{2T},2T+R_{2T}]\), the averaged auxiliary moments are
\(T^{-1}\int_{J_T}|v(x)|^2 W_T(x)\,dx\), where
\[
 W_T(x)=\int_T^{2T}K(x-X)\mathbf1_{|x-X|\le R_X}\,dX.
\]
This weight lies in \([0,1/2]\). On
\([T+R_{2T},2T-R_{2T}]\), every \(|X-x|\le R_T\) is included,
so \(W_T\ge q_T\). The rest of \(J_T\) has total length
\(4R_{2T}\). The real field bound in §1 gives
\(|v(x)|^2=O(T^{3/8})\) on all of \(J_T\) once
\(T-R_{2T}\) exceeds the common chart onset.
Replacing \(W_T\) by \(\tfrac12\mathbf1_{[T,2T]}\) thus costs
\(O(T^{-29/8}+T^{-5/8}\log T)\) in the average, including both
interior edges and both exterior edges. The local-time comparison
and the centered mean now give (E03a) with the factor \(1/2\).
No approximant is used outside the enlarged interval.

All implicit constants above are finite. The field constants and
onset are those of E01 §3.1 and HDA's fixed buffers, with
\(L_x\ge16\). The additional gates are the displayed real phase
derivative inequalities, \(R_X\le X/2\), \(2R_X/X\le L_X/2\),
and \(2R_{2T}<T\) with \(T-R_{2T}\) past the common onset.
The elementary summation, integration and kernel constants are
absolute. These dependencies suffice for finite onsets without
evaluating the inherited provider constants.

## 4. Defect margin and scope

Use the [B02 (B7)/(B13)][b02] recipe
\[
 \mathcal B_J(X,1)=\frac{q_X}{2}\log\frac{M(X,1)}{q_X}
      -P_{1,1/L_X}(X)+D_VX^{-3}\log^2X+C_*/L_X,quad
 m_*=\frac{\sin(\pi/8)}{2\cosh(\pi/8)}.
\]
Here \(D_V,C_*\ge0\) are E01's allowances. The log has positive
argument because the exact \(H_\lambda\) is an entire nonzero
function (its positive-source integral is positive at zero), \(C_-\)
is nonzero on the window, and \(K>0\).

The four rational bounds in (B13) follow as below.

- \(\sqrt2>141/100\) gives \(\sqrt{2-\sqrt2}<77/100\).
  The quadratic term of \(\cosh(\pi/8)\) gives
  \(\cosh(\pi/8)>137/128\) since \(\pi>3\).
  Hence \(m_*<9856/54800<9/50\).
- E01's cosine series has coefficient
  \(n^{-11/4}/[k(1+n^{-4})]\) at the unique representation
  \(n=p^k\), zero elsewhere. For \(n\le16\), the complete list is
  \(2,3,4,5,7,8,9,11,13,16\), with \(k=1,1,2,1,1,3,2,1,1,4\).
  Keeping the denominator at \(2,3\) gives bounds
  \(2(119/100)/17\) and \(4/82\), using the fourth-root bounds
  in B02. Dropping the denominator at the remaining entries gives
  respectively \(3/256,3/250,5/1029,1/768,1/810,1/726,1/1014,1/8192\)
  by the listed B02 root inequalities, each verified by powers.
  These fit B02's ten rational budgets, which sum to \(0.22323\).
  The integer tail past 16 is at most
  \(\int_{16}^\infty u^{-11/4}du=1/224<0.0045\).
  Therefore \(|P_{1,\lambda}(X)|<0.22773<23/100\).
- The convex trapezoid bound on every \([n,n+1]\), \(n\ge3\),
  yields \(\sum_{n\ge3}n^{-3/2}\ge
  \int_3^\infty u^{-3/2}du+3^{-3/2}/2=13/(6\sqrt3)\).
  Adding the first two terms and using
  \(\sqrt2<17/12,\ \sqrt3<26/15\) gives
  \(\zeta(3/2)>177/68>13/5\).
- From \(k!\ge2\cdot3^{k-2}\) for \(k\ge2\),
  \(e^a\le1+a+a^2/[2(1-a/3)]\) for \(0\le a<3\).
  At \(a=41/100\) this is \(<151/100\). Its fourth power is
  \(519885601/10^8<26/5\).

If \(\mathcal B_J(X,1)<m_*\) for every \(X\ge A\), then
nonnegativity of the two allowances and the bounds above give
\[
 M(X,1)<q_X\exp\{2(m_*+P_{1,1/L_X}(X))/q_X\}
       \le q_X\exp\{(41/50)/q_X\}.
\]
The last expression tends to \(\tfrac12 e^{41/25}<13/5\).
It bounds the moment by a constant strictly below \(13/5\) throughout
every sufficiently large dyadic window, contradicting (E03a).
This proves (E03b). By monotonicity of the logarithm the same
centers fail for any valid upper replacement \(M^\#\ge M\).
The \(c=1\) subfamily suffices to defeat eventual every-center
success on the original band.

This is an analytical moment milestone and a scoped certificate
obstruction under [avoid01][a01] and [avoid07][a07]. The actual
critical-boundary log and Green value remain open at the failing
centers. Direct logarithmic methods, bounds with a separately proved
Jensen-gap subtraction, and other coupled estimates remain open.
The moment law covers only the stated shrinking-time subfamily.

## 5. Collision-control premise check

Apply [controls12][controls], [cluster11][r11] and the detailed
[B02 §5 screen][b02] to the literal inputs above. The generic Jensen
and kernel steps are shared. The source-dependent steps require the
complete canonical CS6 real formula, all its specified weights and
the E01 prime coefficients.

| Control family | Premise unavailable for this proof |
| --- | --- |
| Euler-factor and translated sources | Unchanged completed theta field and its all-one arithmetic arms; the prime coefficients also change. |
| Weighted-square and finite-tail changes | The full unmodified square coefficients and canonical reflection needed for the inherited provider. |
| Finite-prime orbits | Full reflection and all source coefficients, even with selected-prime identities and finite measurements preserved. |
| Reflected super-Gaussian and smooth/primitive controls | Ordinary theta/zeta Dirichlet arithmetic in the real HDA formula. |
| Atomic and finite-profile controls, including continuous extensions, and heat counter-kernels | The canonical completed theta field with its full Riemann–Siegel expansion. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic despite matching the displayed completion and residue. |
| Fixed-amplitude, variable-readout control | The actual cosine readout and corresponding Newman equation. |
| Relaxed positive Green profiles | Identification with the exact integer zero measure. The finite profile constraints do not supply the exact real field moment. |

The collision evidence retains its original domains. The screen tests
premises analytically, with no new numerical runs. The obstruction
concerns the stated Jensen allowance for the actual source.

[request]: ../research-progress/handoffs/02_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_R1_20261111.md
[review]: ../reviews/05_GNP_RS_E03_COHERENT_JENSEN_SELF_CHECK_20261111.md
[e01]: 03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[b02]: 05_GNP_RS_B02_JENSEN_AND_SHIFTED_ZETA_COMPARISON_20261111.md
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hda-review]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[shapiro]: https://www.joelshapiro.org/Pubvit/Downloads/OscNotes/oscint.pdf
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
