# Complete current and a paid rectangle of genuine simple heat zeros

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available and are not inferred. The derivations and interval checks are
internal checks, not independent mathematical review.

This continues [Note 2](2_CENTERED_RELATIVE_BLOCK_AND_ADVERSE_COHERENT_CURRENT_20261010.md)
by restoring every term of the genuine cutoff, paying spatial and time
transport, and applying the full holomorphic approximation. The finite
result is a positive-area rectangle in the shrinking sector that contains
exactly one simple genuine heat zero at every time and contains no joint
zero of \(H_t,H_t'\). It is not a uniform sector theorem or a statement
about the sign of the current at all genuine candidate collisions.

Put
\[
 M=N=22066,\quad t_0=(2\log M)^{-1},\quad x_0=4\pi M^2,
\]
\[
 \mathcal R=\{(t,x):t_0\le t\le t_0+8\cdot10^{-6},\quad
                         x_0+0.3\le x\le x_0+0.4\}.
\tag{1}
\]
The interval certificate proves the following three strict inequalities:
\[
 Q_t(x_0+0.3)<0,\qquad Q_t(x_0+0.4)>0,
 \qquad \inf_{(t,x)\in\mathcal R}Q_t'(x)>0.
\tag{2}
\]
Here \(H_t=A_tQ_t\), with the same symmetric analytic nonvanishing
normalizer as the manuscript; \(A_t(x)>0\) on the real axis. Thus (2)
establishes one unique simple zero of \(H_t\) inside the height interval
for each time in (1). At that zero \(H_t'=A_tQ_t'\ne0\). Away from it
\(H_t\ne0\). Hence \((H_t,H_t')\) is jointly nonvanishing everywhere
on (1). The implicit-function theorem gives a smooth local zero branch
through this rectangle; no claim about continuation outside it is made.

## 1. Complete recombination restores the current sign

Use precisely the genuine coefficients of Note 2:
\[
 S=\sum_{n=1}^{M}q_n=S_B+S_C,\quad
 S'=S_B'+S_C',\quad B=\{M/2<n\le M\},\ C=\{1\le n\le M/2\},
\]
\[
 \mathcal J=-\Im(S'\overline S),\qquad
 W=4iS'/L_0,\quad L_0=2\log M.
\tag{3}
\]
The point computation includes all 22066 terms, their physical first
derivatives, and the true principal-branch carrier. Its negative block
current is the preserved result of Note 2. The complement current and
cross current are explicitly enclosed as well:
\[
 \mathcal J=\mathcal J_B+\mathcal J_C+\mathcal J_{BC},\quad
 \mathcal J_{BC}=-\Im(S_B'\overline{S_C}+S_C'\overline{S_B}).
\tag{4}
\]
The following displayed bounds are deliberately wider than the retained
60-digit intervals and are checked as replay assertions.

| Complete-cutoff quantity at \((t_0,x_0)\) | Certified bound |
|---|---|
| \(\mathcal J_B\) | \(-0.000673643<\mathcal J_B<-0.000673642\) |
| \(\mathcal J_C\) | \(12.32324<\mathcal J_C<12.32325\) |
| \(\mathcal J_{BC}\) | \(-0.215813<\mathcal J_{BC}<-0.215811\) |
| \(\mathcal J\) | \(12.10675<\mathcal J<12.10677\) |
| \(|\mathcal V_M|^2\) | \(3.13574<|\mathcal V_M|^2<3.13575\) |

The complement reverses the sign of the block example. This removes any
inference from that adverse block to a negative *complete* current.
It does not establish complete-current positivity at other heights.

Both phase channels of the real collision vector are measured:
\[
 |\mathcal V_M|^2=|\mathcal B|^2+|\mathcal C|^2+E_{BC}^-+E_{BC}^+,
\]
\[
 E_{BC}^-=\Re(S_B\overline{S_C}+W_B\overline{W_C}),\qquad
 E_{BC}^+=\Re(S_BS_C-W_BW_C).
\tag{5}
\]
The current uses coherent phase differences; (5) separately retains the
reflected phase sums and actual signed real observation. The checker
reports both terms rather than hiding them in a positive complex norm.
Intervals obtained from the direct complete expressions overlap the
independently recombined intervals in (4) and (5).
At this point \(E_{BC}^-\) is approximately \(-0.0437599560\), while
\(E_{BC}^+\) is approximately \(0.00922600702\). Their opposite signs
are actual measured interference, not a replacement of the cross term by
an absolute-value estimate. The complete-current collision tolerance in
(6) is less than \(0.061241\), leaving a paid gap greater than \(12.0455\).

At a genuine collision the full complex-disk payment gives
\(u=\Re S\), \(u'=\Re S'\) with
\[
 |u|\le\eta/2,\quad |u'|\le L\eta/2,
 \quad \mathcal J=u'v-uv',\quad v=\Im S,\quad v'=\Im S'.
\]
Consequently a sufficient paid current test for joint nonvanishing is
\[
 |\mathcal J|>\frac\eta2(L|v|+|v'|).
\tag{6}
\]
There is no division by \(S\). The right side is the exact support
bound of the paid rectangle for \((u,u')\); treating \(|S|\) alone as
the genuine real observation would not give (6). The new certificate
proves (6) at \((t_0,x_0)\) and uniformly throughout (1), with the
complete complement interference included. The latter current exclusion
is consistent with the simple zeros in (2): at a simple zero the derivative
is nonzero, so the collision hypothesis used to obtain (6) fails.

## 2. A physical spatial transport with an explicit residual

The coherent transport is applied to every genuine term. Set
\(\delta_n=\log(M/n)\), \(\omega_n=\delta_n/2\),
\(q_n^0=q_n(t_0,x_0)\), and introduce the comparison function
\[
 G(h)=\sum_{n\le M}q_n^0e^{-i\omega_nh}.
\tag{7}
\]
This frozen-frequency function is an auxiliary coherent sum; it is not
substituted for the physical approximant without payment. The exact
physical logarithmic derivative at fixed time and cutoff is
\[
 \gamma_n=\frac{\partial_xq_n}{q_n}
       =-\frac{tV}{4}\log n-i(\Omega-c\log n),
\]
\[
 c=(1+tU/2)/2,\qquad
 \Omega=\{\alpha_r(1+tU/2)-\alpha_i tV/2\}/2,
\tag{8}
\]
where \(\alpha'=U+iV\). In particular \(\alpha_r'=V/2\) and
\(\alpha_i'=-U/2\). The normalizer-induced amplitude and phase motion
are already present in (8).

Define the exact residual
\[
 r_n(t_0,x)=\gamma_n(t_0,x)+i\omega_n
 =-\frac{t_0V\log n}{4}
   -i\{\Omega-c\log M+(c-\tfrac12)\delta_n\}.
\tag{9}
\]
For \(0\le h\le0.4\), integration of this scalar equation gives
\[
 q_n(t_0,x_0+h)=q_n^0e^{-i\omega_nh}e^{E_n(h)},\quad
 E_n(h)=\int_0^h r_n(t_0,x_0+y)\,dy.
\tag{10}
\]
Suppose \(|r_n|\le R_n\) on this whole spatial hull. The checker
uses the safe \(\ell^1\) complex bound on the real and imaginary
components of (9), evaluated by outward intervals. With
\(w_n^0=|q_n^0|\), (10) proves
\[
 |S(t_0,x_0+h)-G(h)|\le
 \epsilon_{x,0}:=\sum_{n\le M}w_n^0(e^{0.4R_n}-1),
\]
\[
 |S'(t_0,x_0+h)-G'(h)|\le
 \epsilon_{x,1}:=\sum_{n\le M}w_n^0
       \{\omega_n(e^{0.4R_n}-1)+R_ne^{0.4R_n}\}.
\tag{11}
\]
Thus the physical derivative is paid explicitly; neither \(\Omega\)
nor \(c\) nor the amplitude drift is held artificially fixed. Keeping
the residual in centered form (9) also avoids a crude large bound on two
nearly equal carrier terms.

## 3. Time transport at fixed physical height and cutoff

The time derivative is not taken along the scaling curve. At fixed real
\(x\), direct differentiation of the genuine weight and phase gives
\[
 \chi_n:=\frac{\partial_tq_n}{q_n}
 =\frac{\log^2n}{4}-\frac{\alpha_r\log n}{2}
       +\frac{i\alpha_i}{2}(\alpha_r-\log n),
\]
\[
 \partial_t\gamma_n
 =-\frac{V\log n}{4}
       -\frac i4\{U(\alpha_r-\log n)-\alpha_iV\}.
\tag{12}
\]
The imaginary part of \(\chi_n\) includes
\(\partial_t\theta_t=\alpha_r\alpha_i/2\); omitting it would
freeze a genuine common phase. In particular
\[
 \partial_t S=\sum q_n\chi_n,\qquad
 \partial_tS'=\sum q_n(\partial_t\gamma_n+\gamma_n\chi_n).
\tag{13}
\]
Let \(W_n,C_n,D_n,A_n\) be outward upper bounds on
\(|q_n|,|\chi_n|,|\gamma_n|,|\partial_t\gamma_n|\), respectively,
on the full rectangle (1). The same componentwise complex bound gives
\[
 B_{t,0}=\sum W_nC_n,\qquad
 B_{t,1}=\sum W_n(A_n+D_nC_n),
\]
\[
 |S(t,x)-S(t_0,x)|\le8\cdot10^{-6}B_{t,0},\qquad
 |S'(t,x)-S'(t_0,x)|\le8\cdot10^{-6}B_{t,1}.
\tag{14}
\]
These are physical fixed-cutoff derivative bounds for the complete sum.
They are intentionally absolute budgets; the coherent cancellation is
preserved in (7), and only the small motion errors are bounded absolutely.

## 4. Coherent midpoint jets and a sixth-moment remainder

Set \(h_*=0.35\), \(d=0.05\). The signed complex midpoint jets are
exact finite sums
\[
 g_j=G^{(j)}(h_*)=\sum_{n\le M}(-i\omega_n)^j q_n^0
                               e^{-i\omega_nh_*},\quad 0\le j\le5.
\tag{15}
\]
All genuine phases survive in (15). With
\(M_6=\sum w_n^0\omega_n^6\), the real-variable Taylor integral
remainder gives, uniformly for \(|z|\le d\),
\[
 \left|G(h_*+z)-\sum_{j=0}^5g_jz^j/j!\right|
       \le M_6d^6/6!,
\]
\[
 \left|G'(h_*+z)-\sum_{j=0}^4g_{j+1}z^j/j!\right|
       \le M_6d^5/5!.
\tag{16}
\]
No exponential loss is required here: along the real height variable
\(|e^{-i\omega_nh}|=1\). The intervals for the signed jets, the
polynomial on \(z\in[-0.05,0.05]\), the endpoint polynomials, and
the positive sixth-moment remainder are all in the certificate.

Combining (11), (14), and (16) gives complex enclosures of the actual
complete \(S,S'\) on (1). The error radii added to each component are
\[
 E_0=M_6d^6/6!+\epsilon_{x,0}+8\cdot10^{-6}B_{t,0},
 \quad E_1=M_6d^5/5!+\epsilon_{x,1}+8\cdot10^{-6}B_{t,1}.
\tag{17}
\]
The endpoint tests use \(z=-d,+d\) in the same signed polynomial.
This is a finite coherent summation transformation with quantitative
remainders, rather than an assumption of a favorable phase alignment.

## 5. The full holomorphic payment and finite conclusion

For every point of (1) define
\[
 L(t,x)=\log(x/(4\pi)),\qquad \kappa=tL(t,x).
\]
The checker proves \(1\le\kappa\le2\), \(0<t\le1/20\), and
\[
 M^2\le\frac{x}{4\pi}+\frac t{16}<(M+1)^2.
\tag{18}
\]
Hence the natural cutoff is the same genuine integer \(M\) everywhere
on the rectangle. The local complex disk may still encounter a cutoff
change; the imported full payment already includes that possibility.

Use [Heat Note 13, equation (1)](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md),
including its symmetric normalizer, reflected analytic terms and full
cutoff-change payment. Its source is the effective approximation in
[Polymath, Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3),
with the repository's explicit shrinking-sector deductions. At each real
point the disk of radius \(1/L(t,x)\) gives
\[
 |Q_t-F_{t,M}|\le\eta(t,x),\quad
 |Q_t'-F_{t,M}'|\le L(t,x)\eta(t,x),
\]
\[
 \eta(t,x)\le5\exp\{-tL(t,x)^2/16-L(t,x)/4\}.
\tag{19}
\]
Spatial derivatives of \(F_{t,M}\) hold \(t,M\) fixed. The derivative
scale in (19) is the point's central Cauchy radius; it is not differentiated
as a factor in a physical coordinate. On the real axis
\(F_{t,M}=2\Re S\), \(F_{t,M}'=2\Re S'\). Off-axis the
holomorphic approximant is \(S(z)+S^\#(z)\), not \(2\Re S(z)\).
No real-part or conjugated-coordinate substitution enters the Cauchy
derivative payment.

Apply (19) to the endpoint and derivative enclosures obtained from (17).
Their strict signs give (2). The same enclosures also prove the uniform
reverse of the collision necessary inequality (6). These are finite
arithmetical interval results about the actual heat approximation and its
fully paid genuine remainder. They give no signed estimate uniform as
\(t\downarrow0\), no sectorwide current positivity, no threshold
fourth-jet inequality and no RH conclusion.

| Uniform quantity on \(\mathcal R\) | Certified coarse bound |
|---|---|
| \(Q_t(x_0+0.3)\) for all allowed times | \(-0.337<Q_t(x_0+0.3)<-0.246\) |
| \(Q_t(x_0+0.4)\) for all allowed times | \(0.851<Q_t(x_0+0.4)<0.941\) |
| \(Q_t'(x)\) on the whole rectangle | \(10.20<Q_t'(x)<13.46\) |
| Complete \(\mathcal J(t,x)\) | \(5.07<\mathcal J(t,x)<11.10\) |
| Paid current gap in (6) | greater than \(4.92\) |
| Full value payment \(\eta\) | less than \(0.009642\) |
| Full spatial derivative payment \(L\eta\) | less than \(0.193\) |

For comparison, the auxiliary motion payments are substantially smaller:
\[
 \epsilon_{x,0}<1.3\cdot10^{-9},\quad
 \epsilon_{x,1}<4.5\cdot10^{-9},\quad
 B_{t,0}<2203,\quad B_{t,1}<2195,
\]
\[
 M_6d^6/6!<9.39\cdot10^{-7},\qquad
 M_6d^5/5!<0.000113.
\tag{20}
\]
The dominant derivative error in the proof is therefore the *full*
holomorphic approximation payment, which is still well below the observed
positive derivative margin.

## 6. Replay, review and the next signed checkpoint

The new standard-library source
[check_complete_current_rectangle.py](../numerics/check_complete_current_rectangle.py)
imports the unchanged [Note 2 interval arithmetic](../numerics/check_block_current.py).
It checks that imported source's retained SHA-256 before importing it and
fails closed if the dependency changes.
It uses 60-digit outward Decimal intervals, explicit Machin arctangent and
sine/cosine Taylor remainders, and adjacent enclosing endpoints for the
correctly rounded monotone logarithm and exponential. The latter contract
is documented by [Python Decimal](https://docs.python.org/3/library/decimal.html).
For this new certificate, a local override evaluates every nonnegative
integer interval power by repeated outward multiplication, with sign and
parity handled exactly. It avoids relying on the C implementation's
less general rounding guarantee for `Context.power`, while preserving the
older source and its source-bound record. Forty-five exact rational checks
cover the override's endpoint, negative-odd and even-zero-crossing cases.
All heights and phase reductions use enclosed pi. No ordinary binary float
enters an assertion.

The small [certificate](../numerics/COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
stores every interval and motion budget above. The
[build record](../numerics/COMPLETE_CURRENT_RECTANGLE_BUILD_RECORD_20261010.json)
binds the new source, its unchanged imported source, and the certificate.
Hashes establish file identity; all signs are established by the outward
arithmetic. [Review 3](../reviews/3_COMPLETE_CURRENT_RECTANGLE_INTERNAL_REVIEW_20261010.md)
records the internal scope checks.

The next signed checkpoint is to turn (6) into a uniform estimate for
*complete genuine candidate states* on a specified shrinking subsector,
or to obtain the complete paid fourth-jet threshold sign from the same
centered moments. A finite simple-zero rectangle can test the machinery
and its payments; it does not supply that missing uniform arithmetic input.
