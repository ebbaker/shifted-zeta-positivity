# Direct arithmetic first jet: paid exterior calibration and its stopping point

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, HCB chat0003, thread `01a184c3-9ae9-7b53-ad7e-f4f104e0fe5b`.

**Status: proved in-note from the inherited approximation statements;
separate-agent same-model internal review only.** This executes the bounded
comparison in [Note09][n09]. The complete physical first jet has an eventual
constant lower floor on **6 <= tL <= 8**. This is a classical exterior
calibration, with uninstantiated source constants/onsets, not new
zero-exclusion coverage. The absolute-sum comparison fails near tL=4.
**HCB-05's time-zero target remains Open; this bounded variant stops here.**
No source values, numerical experiment, sweep, higher saddle orders or
manuscript snapshot were produced. [Review06][review] records the checks;
[input identities][inputs] identify the inherited statements without
independently validating their complete proof chain.

Read the [result index][results], particularly [heat-flow cluster11][r11]
and [collision controls12][controls], and the [avoid index][avoid],
particularly [target classification][a01], [scoped failures][a07] and
[complete signed estimates][a12]. Under avoid/01 this is an acquired
estimate on a stated exterior subrange, not a new global criterion or an
RH advance.

## 1. Domain and exact paired physical jets

Retain H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, and freeze

\[
 L=\log(X/(4\pi)),\quad N=\lfloor e^{L/2}\rfloor,\quad
 z=X+u/L,\quad |u|\le1,\quad \tau=tL\in[4,8],\quad L\ge16.
\tag{1}
\]

Use Note09's buffered core and the inherited fixed complex buffers. Only
real u is used for the lower estimate. All X,L,N and the normalization
A=E_o(t,X)>0 are constant during spatial differentiation. There is no
time evolution argument here.

Write lambda=log(z/(4pi)) and E=A_o(t,z)=E_o(t,z)>0 on this real core.
The elementary carrier [Ansatz Note03 CB5][an03] is exactly

\[
 E=\frac{\pi^{1/4}}{16}z^{7/4}
 e^{-\pi z/8+t(\lambda^2-\pi^2/4)/16},\quad
 \Theta=\frac z4(\lambda-1)+\frac{\pi t\lambda}{16}+\frac{7\pi}8.
\tag{2}
\]

The two arms in [Note26 RA4][an26] pair to E w_n cos(phi_n), where

\[
 k_n=\log n,\quad w_n=n^{-1/2}e^{t(k_n^2-\lambda k_n)/4},\quad
 \phi_n=\Theta-(z/2+\pi t/8)k_n.
\tag{3}
\]

Set

\[
 q=E/A,\quad \rho=E_z/E=\frac7{4z}-\frac\pi8+\frac{t\lambda}{8z},
 \quad \alpha=\rho/L,\quad
 D=\lambda+\frac{\pi t}{4z},\quad \beta=\frac D{4L}=\Theta_z/L.
\tag{4}
\]

Direct differentiation, including both carrier and weight, gives the
exact paired contribution to (F_N/A,F_{N,z}/(LA)):

\[
 V_n=qw_n\begin{pmatrix}
 \cos\phi_n\\
 (\alpha-tk_n/(4zL))\cos\phi_n
 -(\beta-k_n/(2L))\sin\phi_n
 \end{pmatrix}.
\tag{5}
\]

The n=1 pair thus has complementary value/derivative control. At
cos(Theta)=0 its physical derivative is -q beta sin(Theta). No logarithmic
derivative of the oscillating field is used.

## 2. The ordinary phase-insensitive triangle loses

The leading matrix in (5) is B=[[1,0],[alpha,-beta]], whose minimum
singular value tends to 1/4. A phase-insensitive operator-norm bound for
each remaining pair costs at least q w_n: its first row already has norm
one. Even at tau=8, just n=2,3,4 have limiting sum

\[
 2^{-5/2}+3^{-5/2}+4^{-5/2}
 >\frac16+\frac1{16}+\frac1{32}=\frac{25}{96}>\frac14.
\tag{6}
\]

At smaller tau these fixed-mode weights are larger. Therefore the
comparison of the worst leading ellipse floor against these separate
phase-independent majorants has no asymptotic positive margin anywhere
in the prescribed band. This identifies the loss in that baseline. It
is not a lower bound on the actual remainder and does not disprove
phase-aware Euclidean comparisons or pointwise margins on a chart.

## 3. Preserve the joint vector in an invertible weighted norm

At each evaluation point apply the linear map

\[
 T(v_0,v_1)=\left(v_0,\frac{\alpha v_0-v_1}{\beta}\right).
\tag{7}
\]

This is an algebraic norm comparison of the physical jet; T is not
differentiated or substituted as a new physical field. It divides only
by the nonzero carrier phase slope beta. The leading vector is exactly
q(cos(Theta),sin(Theta)), of radius q. For n>=2,

\[
 TV_n=qw_n(\cos\phi_n,r_n\sin\phi_n+d_n\cos\phi_n),\quad
 r_n=1-\frac{2k_n}{D},\quad d_n=\frac{tk_n}{zD}.
\tag{8}
\]

In fact 0<=r_n<=1 on (1), after the basic positive-height gate. To see
D>=L, use z log(z/X)>=z-X>=-1/L and pi t/4>=pi/L. Also
2k_n<=L and 0<=d_n<=t/(2z)<=4/(Lz). Consequently

\[
 \sum_{n=2}^N\|TV_n\|_2\le q S_X,\qquad
 S_X:=\left(1+\frac4{Lz}\right)\sum_{n=2}^Nw_n.
\tag{9}
\]

The bound follows from the norm of diag(1,r_n) plus the displayed shear.
It retains value/derivative correlation within each pair. It neither
drops mixed terms of a squared expansion nor assumes that the different
arithmetic phases align favorably.

## 4. A full arithmetic payment on 6 <= tau <= 8

For this section restrict tau to [6,8]. With epsilon=|lambda-L|, (3)
and t k_n/4<=1 give

\[
 w_n(t,z)\le e^\epsilon h(n),\quad
 h(x)=x^{-2}\exp\{3(\log x)^2/(2L)\},\quad
 0\le\epsilon\le2/(XL).
\tag{10}
\]

Here h is the weight at t=6/L,z=X; increasing t decreases every weight
since k_n<=L/2. The tiny local-height change is explicitly paid.
Split at K=exp(L/12). For n<=K,

\[
 h(n)\le n^{-15/8},\qquad
 \sum_{n=2}^{\infty}n^{-15/8}
 \le\frac{23}{14}2^{-7/8}<\frac{115}{126}<\frac{11}{12}.
\tag{11}
\]

Integral comparison gives the first constant. The strict elementary
bound uses 2^(7/8)>9/5, since 9^8=43046721<50000000=128*5^8.
No finite arithmetic sum is numerically evaluated.

For K<n<=N, h is decreasing: its logarithmic slope in log x is
-2+3 log(x)/L<=-1/2. Thus the entire upper population is bounded by
h(K)+integral_K^(exp(L/2)) h(x) dx. With k=log x, the integral's
exponent is g(k)=-k+3k^2/(2L). Convexity places its maximum on
[L/12,L/2] at an endpoint, where the values are -7L/96 and -L/8.
Since h(K)<=exp(-7L/96),

\[
 \sum_{K<n\le N}h(n)\le (L/2+1)e^{-7L/96}=:J(L).
\tag{12}
\]

This includes all modes through the frozen cutoff, rather than a
bounded-index approximation. Sufficient elementary gates are

\[
 J(L)\le1/192,\qquad
 e^{2/(XL)}\left(1+\frac4{L(X-1/L)}\right)\le60/59.
\tag{13}
\]

They hold for every sufficiently large X. Combining (9)--(13) gives the
uniform complete arithmetic payment

\[
 S_X\le\frac{60}{59}\left(\frac{11}{12}+\frac1{192}\right)
 =\frac{15}{16}.
\tag{14}
\]

## 5. Completion and the two source errors

Retain the complete term R_c=e^(-kappa_c t) R_N in F_N. Write
R_N=G f_N, f_N=a^(-1/2) C(a-N), kappa_c=pi^2/64. The inherited
CS25/RA20 statements give, on the paid buffers,

\[
 |f_N|\le B_0X^{-1/4},\quad |f_N'|\le B_1X^{-3/4},\quad
 |G'/G|\le B_\gamma,\quad |G|/E(0,z)\le B_G.
\tag{15}
\]

Every B is finite and uninstantiated. Because kappa_c agrees exactly
with the carrier's constant time exponent,

\[
 \frac{e^{-\kappa_ct}|G|}{E(t,z)}
 =\frac{|G|}{E(0,z)}e^{-t\lambda^2/16}.
\tag{16}
\]

The two physical completion components, divided by q, cost respectively

\[
 c_0\le B_G B_0X^{-1/4}e^{-t\lambda^2/16},\quad
 c_1\le\frac{B_G}{L}
 (B_\gamma B_0X^{-1/4}+B_1X^{-3/4})e^{-t\lambda^2/16}.
\tag{17}
\]

Applying T costs sqrt(c_0^2+((|alpha|c_0+c_1)/beta)^2). Thus, on the
carrier gates below, it is at most

\[
 c_R=C_R X^{-1/4}e^{-t\lambda^2/16}.
\tag{18}
\]

The completion and its actual physical derivative remain included even
where R_N vanishes. On [6,8], c_R=O(X^(-5/8)); at tau=8 it is
O(X^(-3/4)). Constants absorb the explicitly bounded local lambda-L
change, not any oscillatory denominator.

For Delta V=((H-F_N)/A,(H-F_N)_z/(LA)), use **[Note04 CS6][an04]**, the
sharper nonnegative-time theorem on this overlap, separately:

\[
 |\Delta V_0|\le q C_0X^{-3/4},\qquad
 |\Delta V_1|\le q C_1\frac{1+L}{L}X^{-3/4}.
\tag{19}
\]

Consequently the transformed source allowance divided by q is

\[
 c_H=X^{-3/4}
 \sqrt{C_0^2+
 \left(\frac{|\alpha|C_0+C_1(1+L)/L}{\beta}\right)^2}.
\tag{20}
\]

The scalar and derivative constants are combined only here. RA5's longer
positive-time band has a different allowance; it is not needed or
silently sharpened. F_N generally has nonzero heat residual. No transport
is used, so no conclusion is inferred from that residual.

## 6. Model floor, net exact floor and onset

Impose the additional elementary carrier gates

\[
 q\ge1/2,\quad |\alpha|\le1/16,\quad1/5\le\beta\le1/3.
\tag{21}
\]

They follow eventually from the exact formulas, uniformly on the whole
core and time interval. The Frobenius bound gives ||T||_2<6 there.
Equations (14),(18),(20) now provide the fully paid estimates

\[
 \|V_{F_N}\|_2\ge\frac q6\left(\frac1{16}-c_R\right),\qquad
 \boxed{\ \|V_H\|_2\ge\frac q6
   \left(\frac1{16}-c_R-c_H\right).\ }
\tag{22}
\]

Here V_H=(H/A,H_z/(LA)) is the original frozen physical jet. In
particular, after the separate gates c_R<=1/64 and c_H<=1/64,

\[
 \|V_{F_N}\|_2\ge\frac{3q}{384},\qquad
 \boxed{\ \|V_H\|_2\ge\frac1{384}
 \quad(|u|\le1,\ 6\le tL\le8).\ }
\tag{23}
\]

Take the maximum of the actual inherited CS6/CS25 onsets, the fixed
buffer/gamma onsets, L>=16, (13), (21) and the two final error gates.
All gates hold uniformly for every larger X, using continuous majorants
and the fixed compact fractional-cutoff range. The height is finite but
uninstantiated: no numerical X_* or practical cost is claimed. The
rational floor 1/384 is a conservative asymptotic floor after these
unevaluated source payments, not a certified finite onset. No RH premise
was used to derive this real-jet exterior calibration.

## 7. Where this comparison stops

At tau=4 every fixed w_n tends to n^(-3/2), while d_n tends to zero.
For sufficiently large X, even the fixed subblock 2<=n<=31 defeats
(9)'s needed payment below one, because

\[
 \sum_{n=2}^{31}n^{-3/2}
 \ge\int_2^{32}x^{-3/2}\,dx
 =\frac{3}{2\sqrt2}>1.
\tag{24}
\]

Therefore the particular weighted triangle cannot reach the lower
endpoint, even with zero completion/source error. By continuity the
same obstacle persists on a nonempty scaled-time interval above four.
It proves neither actual simultaneous cancellation nor failure of other
J methods. The extra arithmetic information needed is control of the
signed sum of the vectors in (8), or a larger explicitly justified paired
block with its entire remainder paid. Smaller approximation errors alone
do not fix (24).

The [Polymath v2 Theorem1.5][pm] comparator was checked directly on
28 October 2026: 0<t<=1/2, a sufficiently large unspecified absolute C,
and the exterior scale exp(C/t), with localization/count statements.
We derive no numerical C from it. Our shrinking-time band has exactly
that exponential time-height scale; this observation alone does not
show our subrange lies above its unspecified C. More decisively,
[cluster11][r11] already records a stronger repository asymptotic
four-jet/sign domain t log(x/(4pi))>=61/24 with unevaluated onset.
[Investigation21 Note58][outer58], §§1--2, retains the imported arithmetic
constant in its effective budget. We have not evaluated that constant or
extended that result. There is no demonstrated improvement in coverage,
onset, exact-field margin against a matched earlier budget, or cost.

This completes Note09's classical-calibration outcome and invokes its
stopping rule. Do not launch a sweep or expand this n=1 absolute-sum
variant. HCB-05 remains open at t=0; HCB-02's finite results and unfinished
uniform acquisition are unchanged. No new P task is opened: returning
to P still requires a specific accessible integrated arithmetic quantity
and a complete error budget below one event, as Note09 requires. Positive
threshold/bounded-height coverage and RH-to-simplicity remain distinct
unproved applications.

## 8. Analytical collision-control screen

The gain above occurs at the canonical paired identity (3) and its
complete quantitative weight bound (10)--(14). The linear transform (7)
alone excludes no control. For the [cluster12 controls][controls]:

| Control | Exact used premise not supplied |
| --- | --- |
| Euler-factor source | Unchanged coefficients and canonical factors in (3); its added shifted arms are absent from our canonical formula and cannot be omitted for that source |
| Weighted-square / finite-source controls | Canonical complete arithmetic approximation (3),(19) and full normalized reflection; no all-real heat time is supplied by those controls, so their local events are not finite global thresholds |
| Reflected super-Gaussian / positive-primitive controls | Canonical integer-square arithmetic, hence the specific weights (3) and paid sum (14) |
| Finite-prime-compatible perturbations | Unchanged infinite coefficient data and full reflection; finite-prime identities do not provide (3),(19) |
| RH-conditional close-source endpoint controls | Ordinary unchanged Dirichlet-series arithmetic; close-source bounds do not supply (3),(14) |
| Free heat double / generic carrier-positive controls | The complete canonical expansion/error payment, not the algebraic transform or positivity of its envelope |

This is an analytical premise screen using existing records, not new
numerical testing. A control may be collision-free on this exterior box;
no claim is made that the local estimate must reject it at an event
outside the proved domain. All failures above retain their precise
information-class and event-domain scope.

[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[an03]: ../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[an04]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[an26]: ../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[inputs]: DIRECT_JET_INPUTS_20261028.json
[n09]: 09_CONTINUATION_FOR_DIRECT_ARITHMETIC_JET_TEST_20261028.md
[outer58]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md
[pm]: https://arxiv.org/html/1904.12438v2#S1
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[results]: ../../../../result-summaries/README.md
[review]: ../reviews/06_DIRECT_ARITHMETIC_JET_INTERNAL_REVIEW_20261028.md
