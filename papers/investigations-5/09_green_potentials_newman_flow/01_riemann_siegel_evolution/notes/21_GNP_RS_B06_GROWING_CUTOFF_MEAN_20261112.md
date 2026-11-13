# GNP-RS-B06 — quantitative growing-cutoff residual means

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0006, thread
`01a1d151-91b1-7663-8f10-07d0b4f94163`. Actual backend model and effort are
absent from the recorded configuration; recommendations are not provenance.
Three separate analytical helpers contributed the diagonal, oscillatory and
clock/edge checks. Their inherited configurations are not independently
identified. This is internal LLM work sharing the inherited source inputs.

**Status: proved in-note from named inherited inputs, with contributing
separate-agent internal checking.** The [assessment][review] records the
check and its limits. This completes the bounded analytical attempt in
[brainstorm Note05][brief]. No manuscript integration or E08 is issued.

The result is a quantitative averaged milestone under [avoid01][a01], not
an RH-equivalent criterion or an every-center estimate. Read the
[result index][results], [heat-flow cluster11][r11], [avoid index][avoid],
[control catalog12][controls], [premise02][a02], [scope07][a07] and
[separate-bounds12][a12]. The numerical gains are the cutoff range
\(P\le L_U^2\), an \(O(L_U^{-3/2})\) mean error at the selected cutoff,
and useful translated intervals of length \(U^{3/8+\rho}\).

## 1. Statement, complete field and domain

Keep the complete theta field, physical equation
\(\partial_\lambda H=-H_{zz}\), carrier \(C_-\), strip \(0<\Im z<8\),
center \(X+4i\), and defect parameters \(d=1/2,r=1\) of [E01][e01]. Set
\[
 L_x=\log(x/(4\pi)),\quad V_\lambda=H_\lambda/C_-,\quad
 R_X^w=(32/\pi)\log X,\quad W_X=[X-R_X^w,X+R_X^w],\quad
 K(t)=\frac1{16\cosh(\pi t/8)}.
\]
The superscript on the window radius distinguishes it from the residual.
For each center use \(\lambda=1/L_X\), held fixed throughout \(W_X\).
For an integer cutoff \(P\ge2\), also held fixed throughout the outer
interval, put
\[
 E_P(\lambda,x)=\prod_{p\le P}(1-p^{-3/4}e^{i\nu_\lambda(x)\log p})^{-1},
 \quad \nu_\lambda(x)=x/2+\pi\lambda/8,\quad
 \phi_\lambda(x)=2\Theta(\lambda,x),
\]
\[
 R_P(X,1)=\int_{W_X}K(x-X)
 \left|\frac{V_\lambda(x)-E_P(\lambda,x)
                -e^{i\phi_\lambda(x)}\overline{E_P(\lambda,x)}}
               {E_P(\lambda,x)}\right|^2dx,
\]
\[
 \mathscr R(U,\ell;P)=\ell^{-1}\int_U^{U+\ell}R_P(X,1)dX,
 \quad \mu_P=\sum_{\substack{k>1\\(k,D_P)=1}}k^{-3/2},
 \quad D_P=\prod_{p\le P}p.
\]
Thus \(\mu_P=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1\), and
\(0\le\mu_P\le2P^{-1/2}\): every integer in this sum exceeds P.

**Theorem.** There are finite constants and onset gates specified below,
independent of \(P,U,\ell\), such that for every sufficiently large real
U, every integer \(2\le P\le\lfloor L_U^2\rfloor\), and
\(1\le\ell\le U\), the explicit ledger (12) bounds
\( |\mathscr R(U,\ell;P)-\mu_P|\). In particular, for every fixed
\(0<\rho\le5/8\), uniformly on
\[
 U^{3/8+\rho}\le\ell\le U,\qquad 2\le P\le\lfloor L_U^2\rfloor,
\]
\[
 |\mathscr R(U,\ell;P)-\mu_P|
 \le C\left(\frac{\sqrt{\mu_P}}{L_U}+L_U^{-2}\right)
       +O_\rho\bigl(U^{-\frac12\min(\rho/2,1/64)}\bigr).       \tag{1}
\]
At \(P_U=\lfloor L_U^2\rfloor\), this gives
\[
 \boxed{\mathscr R(U,\ell;P_U)=\mu_{P_U}+O_\rho(L_U^{-3/2}),
 \qquad \mathscr R(U,\ell;P_U)=O_\rho(L_U^{-1}).}             \tag{2}
\]
The dyadic case is \(\ell=U\). All real starting heights beyond the
onset are covered; there is no selected subsequence or sampled-height
premise. Constants in the field/clock costs depend only on the fixed
inherited HDA/E01 provider. Their numerical values and the resulting
finite onset remain unevaluated. The \(\rho\)-dependent onset is explicit
through the inequalities in Section 7.

## 2. Arithmetic field and weighted truncation

At the auxiliary time \(1/L_u\), [E03][e03] and [E04][e04] give
\[
 A(u)=\sum_{n\le N_u}w_n(u)e^{i\nu(u)\log n},\quad
 N_u=\lfloor\sqrt{u/(4\pi)}\rfloor,\quad
 w_n(u)=n^{-3/4}e^{(\log n)^2/(4L_u)}\le n^{-5/8},
\]
\[
 S(u)=A(u)+e^{i\phi(u)}\overline{A(u)},\quad
 \nu(u)=u/2+\pi/(8L_u),\quad
 \phi(u)=u(L_u-1)/2+\pi/8+7\pi/4,
 \quad |V_{1/L_u}(u)-S(u)|\le C_Hu^{-1/4}.                  \tag{3}
\]
The error contains the full correction and residual. HDA CS6 is used on
fixed charts \(r=1,b=9\), with the buffers/onsets of E01 Section 3.1,
not on a chart whose radius grows like \(\log U\). CS25 covers every
fractional cutoff, including its removable singularities. The Gaussian
exterior is already in that provider. The inherited theorem has internal
review; this note is not a fresh independent audit of it.

Keep A as the complete arithmetic arm. Introduce an integer head cutoff
\(2\le Y\le N_U\) and \(A_Y=\sum_{n\le Y}w_n e^{i\nu\log n}\).
Section 4 pays its omitted tail in the required mean-square norm. Let
\(Q=E_P^{-1}\), \(B_Y=A_YQ-1\), and, for \(M\ge2\), set
\[
 Q_M=\sum_{\substack{d\mid D_P\\d\le M}}\mu(d)d^{-3/4}e^{i\nu\log d},
 \quad E_M=\sum_{\substack{e\le M\\p\mid e\Rightarrow p\le P}}
                  e^{-3/4}e^{i\nu\log e},\quad B_M=A_YQ_M-1.
\]
Here \(\mu(d)\) in a coefficient is the Möbius function.
For \(0<\eta<1/4\), define explicit positive products
\[
 H=\prod_{p\le P}(1-p^{-3/4})^{-1},\quad
 F_s(P)=\prod_{p\le P}(1-p^{-s})^{-1},\quad
 T=M^{-\eta}F_{3/4-\eta}(P).
\]
Absolute coefficient sums of Q, Q_M, E and E_M are at most H; both
omitted tails have supremum at most T. Indeed \(n>M\) gives
\(n^{-3/4}\le M^{-\eta}n^{-(3/4-\eta)}\), and the full squarefree
sum is no larger than the smooth-integer Euler sum. These are pointwise
bounds in the actual phases, not independent-prime averaging.
For \(0<s<1\), elementary integral comparison gives
\[
 F_s(P)\le\exp(C_sP^{1-s}),\qquad
 C_s=\frac1{(1-s)(1-2^{-s})}.                               \tag{4}
\]
This follows from \(-\log(1-p^{-s})\le p^{-s}/(1-2^{-s})\) and
\(\sum_{n\le P}n^{-s}\le P^{1-s}/(1-s)\).

The full reflected multiplier is retained:
\[
 m=\overline Q/Q=\overline Q E,\quad |m|=1,\qquad
 m_M=\overline{Q_M}E_M,\quad
 \|m-m_M\|_\infty\le2HT,\quad
 \|m_M\|_{\text{coefficient }1}\le H^2.                    \tag{5}
\]
Its frequencies are \(e/d\) with \(e,d\le M\); possible coincident
rational frequencies cause no problem for the absolute coefficient sum.

## 3. Uniform diagonal estimate

Write \(b_k\), \(b_k^{(M)}\) for the coefficients of B_Y, B_M, extended
by zero beyond their finite supports, and
\(r_k=k^{-3/4}{\bf1}_{k>1,(k,D_P)=1}\). The coefficient at 1 is zero.
The exact divisor cancellation for the limiting coefficients is
\(\sum_{d\mid(k,D_P)}\mu(d)={\bf1}_{(k,D_P)=1}\).

For active n, \(e^t-1\le te^t\) and \(\log n\le L_u/2\) give
\[
 |w_n-n^{-3/4}|\le\frac{(\log n)^2}{4L_u}n^{-5/8}.
\]
For inactive \(n>Y\), \(n^{-3/4}\le Y^{-1/8}n^{-5/8}\).
Since \(d^{-3/4}(k/d)^{-5/8}=k^{-5/8}d^{-1/8}\), convolution gives
\[
 |b_k-r_k|\le k^{-5/8}\tau(k)
              \left(\frac{(\log k)^2}{4L_u}+Y^{-1/8}\right),
 \quad |b_k-b_k^{(M)}|\le M^{-1/8}k^{-5/8}\tau(k).          \tag{6}
\]
Here \(\tau(k)\) is the divisor count, not a time parameter. These
bounds are uniform for **every finite P**. No product supremum is
multiplied by \(1/L_u\) in this step.

Set
\[
 C_0^2=\sum_{k\ge1}\tau(k)^2k^{-5/4},\quad
 C_2^2=\sum_{k\ge1}\tau(k)^2(\log k)^4k^{-5/4}.
\]
Both are finite, with explicit bounds
\(C_0\le25\), \(C_2\le81(32/e)^2\). To check them,
\((a+1)^2\le\binom{a+3}{3}\) gives \(\tau(k)^2\le d_4(k)\);
expanding four absolutely convergent sums yields
\(\sum d_4(k)k^{-s}=\zeta(s)^4\). Also
\(t^4e^{-t/8}\le(32/e)^4\) and \(\zeta(s)\le1+1/(s-1)\).
This is an elementary coefficient calculation, not an imported mean theorem.

On \([U,U+\ell]\subset[U,2U]\), put
\[
 a_0=\frac{C_2}{4L_U}+C_0Y^{-1/8}+C_0M^{-1/8},\quad
 D_0=2\sqrt{\mu_P}a_0+a_0^2.
\]
The coefficient Hilbert-space triangle inequality proves, pointwise in u,
\[
 \|b^{(M)}-r\|_2\le a_0,\quad
 \left|\sum_k|b_k^{(M)}|^2-\mu_P\right|\le D_0,
 \quad\sum_k|b_k^{(M)}|^2\le(\sqrt{\mu_P}+a_0)^2.            \tag{7}
\]
“Pointwise” here qualifies the coefficient diagonal, not the oscillatory
field or the Green value.

## 4. All same-arm pairs, cutoff jumps and tail products

Let \(N=N_{2U}\), \(K_0=\lfloor M\rfloor Y\), and set
\[
 s_0=75000\frac{K_0(1+\log K_0)}\ell,\quad
 b_0=(\sqrt{\mu_P}+a_0)^2+s_0,\quad
 A_0=1000\left(1+\frac{U^{3/8}(1+\log U)}\ell\right).
\]
For \(k>1\), define
\(g_k=k^{-5/8}\tau(k)\). Every summand of \(b_k^{(M)}\) switches on
once at \(u=4\pi(k/d)^2\), then decreases. Its supremum is bounded
by \(k^{-5/8}d^{-1/8}\). Thus
\(\sup|b_k^{(M)}|\le g_k\), total variation is at most \(2g_k\),
and the product amplitude has supremum plus total variation at most
\(5g_kg_l\). This includes jumps and interval endpoints.

Since \(\nu'\ge1/4\) and \(\nu''>0\), each same-arm phase
\(\nu\log(k/l)\), \(k\ne l\), has unweighted partial-integral bound
\(12/|\log(k/l)|\). Integration against the bounded-variation
amplitude and
\[
 |\log(k/l)|^{-1}\le K_0/|k-l|,\quad
 2g_kg_l\le g_k^2+g_l^2,\quad \sum g_k^2\le625
\]
pay the entire off-diagonal sum by \(\ell s_0\). The constant is
\(12\cdot5\cdot2\cdot625=75000\), with the harmonic sum bounded
by \(1+\log K_0\). Therefore
\[
 \left|\langle|B_M|^2\rangle-\mu_P\right|\le D_0+s_0,
 \qquad\langle|B_M|^2\rangle\le b_0.                       \tag{8}
\]
Angle brackets mean \(\ell^{-1}\int_U^{U+\ell}\), always the actual
one-parameter height trajectory.

For A and A_Y, the sharper elementary pair summation from E03 gives
\(\langle|A|^2\rangle,\langle|A_Y|^2\rangle\le A_0\). In detail, for \(m\le n/2\) use
\(|\log(n/m)|^{-1}\le1/\log2\); for \(n/2<m<n\) use
\(n/(n-m)\). Summing \((mn)^{-5/8}\) then gives at most an absolute
constant times \(N^{3/4}(1+\log N)\), with the weight-variation factor
and both orderings included. The diagonal is at most \(\zeta(5/4)\le5\).
The displayed factor 1000 exceeds these elementary constants, and
\(N\le\sqrt U\). In particular,
\[
 \|B_Y-B_M\|_{L^2(du/\ell)}\le T\sqrt{A_0}.                 \tag{9}
\]
The same pair argument restricted to \(n>Y\), with diagonal tail
\(\sum_{n>Y}n^{-5/4}\le4Y^{-1/4}\), gives
\[
 \langle|A-A_Y|^2\rangle\le
 A_1:=1000\left(Y^{-1/4}+\frac{U^{3/8}(1+\log U)}\ell\right).
\]
This includes every actual cutoff activation in the omitted arm. Define
\[
 Z(A)=AQ-1+e^{i\phi}(Q/\overline Q)\overline{AQ-1}.
\]
Since \(|Q/\overline Q|=1\),
\(\|Z(A)-Z(A_Y)\|_2\le2H\sqrt{A_1}\), while each of
\(\|Z(A)\|_2,\|Z(A_Y)\|_2\) is at most \(4H\sqrt{A_0}\).
Therefore the complete-arm to head-square comparison costs at most
\[
 |\langle|Z(A)|^2-|Z(A_Y)|^2\rangle|
                  \le16H^2\sqrt{A_0A_1}.                 \tag{9a}
\]
This pays both tails **after multiplication by the arithmetic arms**.
A uniform multiplier tail need not remain small after pointwise arm-envelope
multiplication; the translated mean-square estimate pays that product.
Truncating the arm is a paid analytical approximation, not a change to the
physical source. It is the one localized refinement of the initial route:
it avoids charging curvature against the whole \(N_U\asymp\sqrt U\) population.

## 5. The full reflected cross term

The relative arithmetic square is exactly
\[
 F(u):=\left|\frac{S(u)-E(u)-e^{i\phi(u)}\overline E(u)}{E(u)}\right|^2
 =2|B|^2+2\Re(e^{-i\phi}B^2m),\qquad B=AQ-1.
\]
After paying (9a), use \(F_Y=|Z(A_Y)|^2\), and truncate it to
\(F_M^*=2|B_M|^2+2\Re(e^{-i\phi}B_M^2m_M)\).
This auxiliary expression need not be nonnegative. Since \(|m|=1\),
Cauchy–Schwarz and (5), (8), (9) give
\[
 |\langle F_Y-F_M^*\rangle|
 \le 8T\sqrt{A_0b_0}+4T^2A_0+4HTb_0.                    \tag{10}
\]
No assumption that \(\langle|B_Y|^2\rangle\) was already bounded is used.

Each retained reflected phase is
\(\psi=-\phi+\nu\log(kl e/d)\), with \(k,l\le K_0\), \(e,d\le M\).
It includes \(k=l\). At the auxiliary time,
\[
 \phi''=1/(2u),\qquad
 \nu''=\frac\pi{8u^2}(L_u^{-2}+2L_u^{-3}).
\]
Impose the explicit gate
\[
 \frac\pi{8U^2}(L_U^{-2}+2L_U^{-3})
                  (2\log Y+3\log M)\le\frac1{8U}.
\]
Since \(|\log(kl e/d)|\le2\log Y+3\log M\),
\(\psi''\le-1/(8U)\), so the first derivative is monotone. The paid
head truncation now permits the additional gate
\[
 3\log M+2\log Y\le(7/8)L_U.
\]
For nonnegative \(\log(kl e/d)\), use \(\nu'\le1/2\); for negative
logarithm use \(\nu'>0\). In both cases
\(\psi'=-L_u/2+\nu'\log(kl e/d)\le-L_U/16\).
Thus every retained phase has unweighted partial-integral bound
\(48/L_U\). This is a proved lower bound for the actual relative
phase derivative of the **truncated** expression, not an assumption about
the untruncated arm. The stationary population has been paid in (9a).

Apply the bounded-variation estimate. The coefficient envelope before
the divisor majorant has sum at most \((8/3)HY^{3/8}\); the multiplier
coefficient sum is at most \(H^2\). Consequently
\[
 |\langle2\Re(e^{-i\phi}B_M^2m_M)\rangle|
 \le c_0:=4000\frac{H^4Y^{3/4}}{\ell L_U}.                 \tag{11}
\]
Indeed \(2\cdot48\cdot5(8/3)^2<4000\). The full multiplier is
retained through (5) and (10), and the omitted arm through (9a).

## 6. Complete field, physical clock and convolution edges

The following constants \(C_{\rm clk},C_{\rm edge}\) depend only on the
fixed provider, elementary sums and kernel; they have no hidden P,
M, Y or interval-length dependence. Let \(R_*=(32/\pi)\log(2U)\).
On the enlarged interval \([U-R_*,U+\ell+R_*]\subset[U/2,3U]\),
the auxiliary arithmetic relative square F is at most
\(C H^2U^{3/8}\), by (3) and the unit modulus of the reflected ratio.

For the physical-time comparison, fix x in \(W_X\) and interpolate
between \(1/L_X\) and \(1/L_x\), never differentiating the cutoff.
At intermediate times \(1/2\le\lambda L_x\le2\), each arm is
\(O(U^{7/32})\), and its time derivative is
\(O(L_U^2U^{7/32})\), as in E03 Section 3. Define
\[
 T_1(P)=\sum_{p\le P}\frac{p^{-3/4}\log p}{1-p^{-3/4}}
 \le\frac4{1-2^{-3/4}}P^{1/4}\log P.
\]
Then \(|Q|\le H\), \(|\partial_\lambda Q|\le(\pi/8)HT_1\),
and \(|\partial_\lambda(Q/\overline Q)|\le(\pi/4)T_1\).
The last bound uses a unit-modulus ratio and avoids paying inverse
products twice. Impose \(T_1(P)\le L_U^2\). For
\[
 Z_\lambda=S_\lambda Q-1-e^{i\phi_\lambda}Q/\overline Q
\]
we have \(|Z_\lambda|\le CHU^{7/32}\) and
\(|\partial_\lambda Z_\lambda|\le CHL_U^2U^{7/32}\).
With \(|1/L_X-1/L_x|\le C R_* /(UL_U^2)\), the square difference
costs \(CH^2R_*U^{-9/16}\). The exact field error from E04 (E04.1), with its full-band physical-time
validity and the same provider as (3), multiplied by Q and paired with \(Z_\lambda\), costs
\(CH^2U^{-1/32}\). This pays the complete correction and residual;
no derivative of the exact field or of its remainder is assumed.
Thus replacing the original residual by \(\int_{W_X}KF(x)dx\)
costs at most \(C_{\rm clk}H^2(U^{-1/32}+R_*U^{-9/16})\).

Fubini gives the weight
\(W_{U,\ell}(x)=\int_U^{U+\ell}K(x-X){\bf1}_{|x-X|\le R_X^w}dX\).
It lies in \([0,1/2]\). Except in the four boundary strips of total
length at most \(4R_*\), its difference from
\(\tfrac12{\bf1}_{[U,U+\ell]}\) is at most \((2/\pi)U^{-4}\),
using the exact kernel tail. The same estimate holds when the interior
is empty: the whole enlarged interval then has length at most \(4R_*\).
The edge cost is
\(C_{\rm edge}H^2(R_*U^{3/8}/\ell+U^{-29/8})\).
There is no use of an approximant outside the enlarged interval.
The kernel mass is exactly \(1/2\).

Combining (7)–(11) and these payments proves
\[
\boxed{\begin{split}
 |\mathscr R(U,\ell;P)-\mu_P|\le\varepsilon(U,\ell,P;M,Y,\eta):={}&
 D_0+s_0+\tfrac12c_0+8H^2\sqrt{A_0A_1}
 +4T\sqrt{A_0b_0}+2T^2A_0+2HTb_0\\
 &+C_{\rm clk}H^2(U^{-1/32}+R_*U^{-9/16})\\
 &+C_{\rm edge}H^2(R_*U^{3/8}/\ell+U^{-29/8}).
\end{split}}                                                   \tag{12}
\]
Every term is explicit in the growing parameters. Only the declared
fixed inherited constants are unevaluated. Formula (12), under its
gates, is valid for every \(1\le\ell\le U\); it need not be small.

## 7. Parameter choice, onset ledger and localization

Write \(M=U^\theta\), \(Y=\lfloor U^\alpha\rfloor\),
\(\eta\in(0,1/4)\), and \(\ell\ge U^\beta\). Require
\(0<\alpha<1/2\), so Y lies below the original cutoff eventually.
The same-arm cost has power \(U^{\alpha+\theta-\beta}\) up to a
logarithm. The nonstationary reflected term has
\(U^{3\alpha/4-\beta}/L_U\) times a subpower product factor.
Its frequency gate is satisfied eventually if \(3\theta+2\alpha<7/8\).
The paid full-arm tail has powers \(U^{-\alpha/8}\) and
\(U^{3/16-\beta/2}\) up to subpower factors. Euler/reciprocal tails
have \(U^{-\theta\eta+o(1)}\). The sufficient competing constraints are
\[
 \beta>3/8,\quad\alpha+\theta<\beta,\quad
 3\theta+2\alpha<7/8,\quad 0<\alpha<1/2,\quad\theta>0.
\]
They admit every fixed \(\beta>3/8\). Choose, only after these comparisons,
\[
 M=U^{1/8},\quad Y=\lfloor U^{1/8}\rfloor,\quad
 \eta=1/8,\quad\beta=3/8+\rho,\quad0<\rho\le5/8.
\]
The same-arm power is \(-1/8-\rho\), the reflected power is
\(-9/32-\rho\), and the head-tail power is \(-1/64\).
The full-arm off-diagonal tail contributes \(U^{-\rho/2}\sqrt{1+\log U}\).
For \(P\le L_U^2\), (4) gives
\[
 H\le e^{C_{3/4}L_U^{1/2}},\qquad
 T\le U^{-1/64}e^{C_{5/8}L_U^{3/4}}.                      \tag{13}
\]
On the chosen interval range, \(A_0,b_0\) are bounded by absolute
constants after a finite onset depending on \(\rho\). The complete ledger
implies, with \(G(P)=C\exp\{C(P^{1/4}+P^{3/8})\}\),
\[
 \varepsilon\le C\left(\frac{\sqrt{\mu_P}}{L_U}+L_U^{-2}\right)
 +G(P)\left(U^{-1/64}
      +U^{-\rho/2}(1+\log U)^{1/2}\right).                \tag{14}
\]
The smaller clock, edge, same-arm and Euler-tail powers are absorbed by
these explicitly stated bounds. Since \(P\le L_U^2\),
\(G(P)=U^{o(1)}\). For fixed \(\rho>0\), impose the finite gate
\[
 \log G(P)+\tfrac12\log(1+\log U)
       \le\tfrac12\min(\rho/2,1/64)\log U.
\]
Replacing P on the left by \(L_U^2\) gives a sufficient onset for every
admissible P simultaneously. This proves (1)–(2); the power remainder
may equivalently be written \(O_\rho(U^{-\min(\rho/4,1/128)})\).

Other onset requirements are: \(L_{U-R_*}\ge16\),
\(U-R_*\) beyond all E01 Section 3.1 chart/buffer/correction onsets;
\(R_*\le U/2\); the E03 clock gates ensuring
\(\lambda L_x\in[1/2,2]\); \(\nu'\ge1/4\); the curvature gate in
Section 5 and its nonstationary frequency gate; \(T_1(P)\le L_U^2\); and \(P\ge2,M\ge2,2\le Y\le N_U\).
All hold eventually uniformly over \(P\le L_U^2\), with
\(U^\theta\) fixed as above. E06's phase gates are added only for
the Green corollary below. No numerical onset is claimed.

The first remaining localization limitation of **this particular ledger**
is \(U^{3/8}(1+\log U)/\ell\), in both the full-arm tail mean \(A_1\)
and the convolution-edge allowance. Its majorant is not small at
\(\ell\le U^{3/8}\). The discarded-arm contribution uses its square root.
The low-head refinement has already removed the avoidable reflected
\(U^{7/8}\), and then \(U^{1/2}\), curvature costs by proving a
nonstationary derivative gap for the retained frequencies. We do not
claim that any of these upper-bound thresholds is a lower bound on the
actual correlations or an optimal localization theorem.
Further improvement needs a stronger localized full-arm/tail estimate
and compatible convolution-edge accounting, or a different signed route.
No maximal or pointwise bound follows by substituting \(\ell=1\).

## 8. Green consequence and remaining every-center gap

For the outer-block constant cutoff \(P_U\), E06's phase gates hold
uniformly at every \(X\in[U,U+\ell]\): its bounds are monotone in P
and \(P_U\le L_X^2\). The complete transfer [E06 (E06.6)][e06]
therefore gives, for every fixed-on-window \(\delta>0\),
\[
 0\le J_{1/L_X}(X)\le\delta/4+R_{P_U}(X,1)/(2\delta^2)+C/L_U.
\]
The omitted prime series, true logarithmic tail and reference exterior
are paid there; at this cutoff they are absorbed in \(C/L_U\).
Choose \(\delta=L_U^{-1/3}\). Equations (1)–(2) prove
\[
 \boxed{\ell^{-1}\int_U^{U+\ell}J_{1/L_X}(X)dX
              =O_\rho(L_U^{-1/3})}
 \quad(U^{3/8+\rho}\le\ell\le U).                         \tag{15}
\]
For each fixed \(h>0\), one may instead choose a small constant regulator
with \(\delta/4\le h/4\), and increase the onset so the overhead is
at most \(h/4\). Then \(J\ge h\) implies \(R_{P_U}\ge h\delta^2\),
so Markov also gives a translated exceptional proportion
\[
 \ell^{-1}|\{X\in[U,U+\ell]:J_{1/L_X}(X)\ge h\}|
                    =O_{h,\rho}(L_U^{-1}).                \tag{16}
\]
These are moving-time means and Lebesgue proportions, not fixed-time zero
counts or zero exclusion. In particular, **the mean theorem does not
supply an every-center Green estimate.**

Localization of the same proof needs a better **localized complete-arm/tail
mean-square estimate with compatible edge control**, not a larger finite-prime sample. A direct signed
estimate at exceptional centers may need to retain the full logarithm and
residual/phase correlation. Neither is proved here, and the old fixed-P
Jensen/tangent obstructions are not upgraded to adaptive-P obstructions.

A persistence argument would need a proved mass lower bound on the same
moving-time curve. Its derivative, where defined, is
\[
 \frac d{dX}J_{1/L_X}(X)=\partial_XJ_\lambda(X)
 -\frac{\partial_\lambda J_\lambda(X)}{XL_X^2}
 \quad\text{at }\lambda=1/L_X.
\]
Spatial smoothing alone does not estimate the time term near a collision.
At the available interval length the upper bound on the total Green mass
is \(O(\ell L_U^{-1/3})\), which grows with U. A bounded amount of
localized defect mass can fit within it. No persistence width, event-time
regularity or maximal estimate sufficient to remove exceptions is supplied.

| Coverage item | Obtained / remaining |
| --- | --- |
| Starting heights | Every real U beyond the finite analytical gates; no evaluated numerical onset. |
| Cutoff | Uniform mean ledger for integer 2≤P≤floor(L_U²), constant across each outer interval. Pointwise center-varying cutoffs are not substituted into this theorem. |
| Interval lengths | Ledger for 1≤ell≤U; vanishing uniform estimate for ell≥U^(3/8+rho), fixed rho>0. |
| Time | c=1 only, physical time fixed within each spatial window. Full c band and other times remain open for this mean theorem. |
| Green geometry | Original strip, d=1/2,r=1; no every-center margin, shrinking-depth or time-zero conclusion. |
| Finite heights | Remaining; no finite-height certification or numerical campaign. |
| Critical-time sibling | RSCT retains separate ownership; no positive-threshold event is excluded. |

## 9. Collision-control premise screen

This is an analytical application of [controls12][controls] on its recorded
witness domains, not a rerun of its certificates. The generic truncation,
Cauchy–Schwarz and scalar transfer inequalities may hold for controls.
The literal canonical application also needs the following missing premises.

| Control family / witness scope | Premise not supplied for literal reuse |
| --- | --- |
| Euler-factor/translated sources, including the recorded positive-time witnesses | Unchanged Dirichlet coefficients, completion and prime subtraction. |
| Three/four weighted squares (T=1/4 and T=1/100); finite tails/prefixes | Complete unchanged square series plus full source reflection. Their local events need not be all-real thresholds. |
| Finite-prime orbits, with events in arbitrarily high gaps at fixed positive time | Full reflection and every canonical coefficient beyond the matched finite data. |
| Reflected super-Gaussian (T=1/4, x=pi/4), smooth and positive-primitive sources | Complete theta square-series arithmetic despite their shape/endpoint properties. |
| Atomic, exact finite-profile and compact continuous thresholds | Full canonical profile and high-zero behavior, not only selected observations. |
| Conditional normalized endpoint controls | Ordinary Dirichlet arithmetic; their RH premise remains conditional. |
| Heat counter-kernels; fixed amplitude with variable readout | Literal theta source and/or actual cosine readout with its physical generator. |
| Relaxed Green profiles | Exact integer zero measure simultaneously identified with the complete boundary field. |
| RSCT calibrated multiplicative models | Actual height phases beyond the calibrated set and a complete Green-window law. |

The diagonal cancellation in Section 3 specifically uses the canonical
all-one limiting Dirichlet coefficients. The field transfer specifically
uses the complete inherited formula. This screen does **not** prove that
every control violates (2) or (15). Isolated collision witnesses can coexist
with these mean bounds, and no witness has been relocated into our time band.

## 10. Continuation

Use the [return and model-change note][return]. The bounded B06 proof is
complete at the status stated above. A next conceptual pass should isolate
one quantitative improvement to the **complete-arm tail and edge terms** or one
exceptional-center signed/persistence input. It should return a numerical
exponent gain or a scoped failed inequality before any broader program is
opened. No dependent execution task is issued merely to restate the gap.
The [sole progress register][progress] owns the current disposition.

[brief]: ../brainstorm/notes/05_GNP_RS_GROWING_CUTOFF_ANALYTICAL_CONTINUATION_20261112.md
[review]: ../reviews/11_GNP_RS_B06_INTERNAL_ASSESSMENT_20261112.md
[return]: 22_GNP_RS_B06_RETURN_AND_MODEL_CHANGE_20261112.md
[progress]: ../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[e01]: 03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[e03]: 07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md
[e04]: 11_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_20261111.md
[e05]: 14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md
[e06]: 17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
