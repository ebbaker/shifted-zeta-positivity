# Signed lags and an actual arithmetic remainder obstruction

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, same HCB chat0003, thread `01a184c3-9ae9-7b53-ad7e-f4f104e0fe5b`.

**Status: proved in-note by a finite signed resonator calculation, with
inherited complete-field error transfer; separate-agent same-model
internal review only.** This continues [Note13][n13] at tL=2. All signed
lags are retained. A 25-term arithmetic resonator proves that the **actual
transformed model remainder**, not merely an allocated allowance, has
projection greater than 7/6 along the leading pair at some center in
every sufficiently large dyadic height interval.

Consequently even perfect signed-lag acquisition and optimal Fejer shift
length cannot make the declared n=1-versus-whole-remainder triangle
comparison work uniformly. This closes that comparison in Note13's
specified physical-jet norm, beyond the earlier block and absolute-lag
failures. It does not close J, other norms/main blocks or full-square
methods, and it proves no collision or uniform noncollision result.

The complete signed arithmetic estimate is

\[
 \frac1X\int_X^{2X}P(T(x))Z(x)\,dx
 =\frac{12721}{10800}
 +O_*(L_X^{-1})+O_*(X^{-7/8}),\qquad
 \frac1X\int_X^{2X}P(T(x))\,dx=1+O_*(X^{-1}),
\tag{1}
\]

with the exact physical remainder Z and nonnegative finite P specified
below. The exact surplus above 7/6 is **121/10800**. No lag is replaced
by its absolute value in deriving this estimate. The model and source
payments are separate, and the latter are paid once for the whole field.

[Review09][review] records three read-only same-model analyses/checks;
no independent specialist or full inherited-proof-chain validation is
claimed. [Input identities][inputs] and the [primary-source record][refs]
preserve the actual scope. No source evaluation, numerical experiment,
sweep, higher-order campaign or manuscript snapshot was performed.

Read the [result index][results], particularly [heat flow11][r11] and
[controls12][controls], and the [avoid index][avoid], particularly
[target classification][a01], [control premises][a02],
[scope][a07] and [complete signed payments][a12]. This is a quantitative
arithmetic estimate and a scoped consumer obstruction, not a renamed
nonvanishing assumption. The positive pointwise consequence below is
existential, with uninstantiated onset, not all-height/chart coverage.

## 1. Exact signed Fejer estimate: keep all lag cancellation

Use Note13's actual transformed pair vectors B_n, leading radius q,
R=sum_{n=2}^N B_n, M=N-1, diagonal D and signed correlations C_h.
No mode or cutoff endpoint is removed. Define, for every integer K>=1,

\[
 A_K=\frac{M+K-1}{K}
 \left[D+2\sum_{h=1}^{K-1}(1-h/K)C_h\right],
 \qquad\|R\|_2^2\le A_K.
\tag{2}
\]

Unlike Note13's stopped consumer, (2) keeps each signed C_h. Its exact
quality can be determined without estimating the lags individually.
Let J=M+K-1 and let S_a be the zero-extended sliding vectors in Note13.
Finite expansion of the Cauchy variance gives

\[
 A_K-\|R\|_2^2
 =\frac{J}{K^2}\sum_{a=1}^J
 \left\|S_a-\frac KJ R\right\|_2^2\ge0.
\tag{3}
\]

For K>=M, all lags are present and

\[
 A_K=\left(1+\frac{M-1}{K}\right)
 \left(\|R\|_2^2-\frac2K\sum_{h=1}^{M-1}hC_h\right)
 \longrightarrow\|R\|_2^2.
\]
\[
 \boxed{\ \inf_{K\ge1}A_K=\|R\|_2^2.\ }
\tag{4}
\]

There is no finite-attainment assertion. Perfect signed cancellation
therefore removes the earlier absolute-lag loss, but cannot supply a
remainder upper bound below its actual norm. The next sections estimate
that actual norm/projection using the complete arithmetic, rather than
assuming the desired upper margin.

## 2. Form the physical derivative before following the center family

Keep H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8 and the original microscopic
chart. At every center x set

\[
 L=\log(x/(4\pi)),\quad t=2/L,\quad N=\lfloor e^{L/2}\rfloor,
 \quad A=E_o(t,x)>0.
\tag{5}
\]

For the physical jet V=(F_N/A,F_{N,z}/(LA)), freeze x,L,N,A and t
in spatial differentiation, as before. Reserve |u|<=2 and the inherited
fixed complex buffers; the prospective uniform comparison fails already
at u=0. Set

\[
 T=x/2+\pi/(4L),\quad
 \Theta=x(L-1)/4+\pi,\quad D_c=L+\pi/(2xL),
\]
\[
 W_n=n^{-1}e^{(\log n)^2/(2L)},\quad
 r_n=1-2\log n/D_c,\quad d_n=2\log n/(xLD_c).
\tag{6}
\]

At the center q=1. With the same invertible algebraic map mathsf T as
Note13, the exact pair is

\[
 B_n=W_n(\cos\phi_n,\ r_n\sin\phi_n+d_n\cos\phi_n),
 \quad\phi_n=\Theta-T\log n,\quad B_1=(\cos\Theta,\sin\Theta).
\tag{7}
\]

Thus every carrier, phase and heat-weight derivative is retained.
Write R=(R_0,R_1), and rotate its full physical two-vector:

\[
 Z=e^{-i\Theta}(R_0+iR_1)
 =\sum_{n=2}^{N}W_n\left[
 a_ne^{-iT\log n}+b_ne^{-2i\Theta}e^{iT\log n}\right],
\]
\[
 a_n=(1+r_n+id_n)/2,\qquad b_n=(1-r_n+id_n)/2.
\tag{8}
\]

Both branches in (8) are required. In particular the mirror branch
encodes physical terms that a scalar |U_0| estimate would miss.
|Z|=||R||, and Re Z=B_1 dot R.

Only after forming (7)--(8) do we vary the center x for an auxiliary
analytic average. That average follows t(x)=2/L(x). Its *total*
phase derivatives are

\[
 T'=1/2-\pi/(4xL^2),\qquad \Theta'=L/4.
\tag{9}
\]

These are not substituted for the frozen-time physical derivatives:
physically Theta_z=L/4+pi/(8xL) and beta_c=Theta_z/L.
The total x derivatives in (9) include the clock variation, whereas
r_n,d_n in (8) were already formed from the physical jet. No heat
transport or residual inference is involved.

## 3. A fixed finite multiplicative resonator

Choose exactly

\[
 Q(T)=\left(\sum_{j=0}^{4}2^{-ijT}\right)
       \left(\sum_{k=0}^{4}3^{-ikT}\right),\qquad
 P(T)=|Q(T)|^2/25\ge0.
\tag{10}
\]

Its support has 25 integers 2^j3^k<=1296. No arithmetic population
is sampled or fitted. The Fourier expansion is

\[
 P(T)=\sum_{h,k=-4}^{4}c_{h,k}e^{iT\nu_{h,k}},\quad
 c_{h,k}=\frac{(5-|h|)(5-|k|)}{25},\quad
 \nu_{h,k}=h\log2+k\log3.
\tag{11}
\]

Here c_00=1, sum c_{h,k}=25 and 0<=P<=25. The resonator is a fixed
weight on the *whole* signed sum, not separate upper allowances for
blocks or lags. The classical positive-resonator principle is attributed
to [Soundararajan v2, introduction (1)][sound]; the physical field,
finite choice (10) and all estimates here are derived directly, without
importing a zeta large-value theorem or dropping the quadratic heat
weight.

Use the average <f>_X=X^(-1) integral_X^(2X) f(x) dx. For large X,
T'>=1/3. Distinct fixed rational frequencies in (11) have a positive
gap from zero; integration by parts gives

\[
 \langle P(T(x))\rangle_X=1+O_*(X^{-1}).
\tag{12}
\]

All starred constants depend only on this fixed resonator and elementary
onset gates. They are finite and uninstantiated, not fitted to data.

## 4. The complete first-branch average, including the moving cutoff

The n-th mode is active on at most one interval

\[
 I_n=[\max(X,4\pi n^2),2X],
 \qquad 2\le n\le N(2X).
\tag{13}
\]

Empty intervals contribute zero. We interchange only finite sums and
integrals; a floor is never differentiated. Its entry endpoint in (13)
is explicitly paid by integration by parts.

On the active interval k_n=log n<=L(x)/2, so

\[
 W_n\le n^{-3/4},\qquad
 W_n'=-\frac{k_n^2}{2xL^2}W_n,\quad |W_n'|\le W_n/(8x).
\tag{14}
\]

The exact a_n,b_n have magnitude bounded by an absolute constant and
|a_n'|+|b_n'|<=C/(xL). Consequently each amplitude W_n a_n or
W_n b_n has endpoint size plus total variation at most C n^(-3/4)
on I_n. This total derivative includes the clock variation in (5).

The first branch in (8), after multiplying (11), has phase
T(nu_{h,k}-log n). If it is not identically zero, its frequency has a
uniform fixed gap: nu=log(a/b) with integers a,b<=1296, and nb!=a
implies

\[
 |\nu-\log n|=|\log(a/(nb))|\ge1/1297.
\tag{15}
\]

For instance if nb>a, log(nb/a)>=log(1+1/a)>=1/(a+1); the opposite
case is at least 1/a. Thus one integration by parts costs
O_*(n^(-3/4)) per active index, including both endpoints and amplitude
variation. Summing the **entire** finite population and dividing by X,

\[
 \frac1X\sum_{n\le N(2X)}O_*(n^{-3/4})
 =O_*(X^{-7/8}).
\tag{16}
\]

The exact resonances are n=2^h3^k, 0<=h,k<=4, excluding n=1.
Unique factorization rules out additional integer resonances. They
are all active throughout the interval after N(X)>=1296. For this
fixed finite set, a_n W_n=1/n+O_*(L_X^(-1)), uniformly on the interval.
Their total signed main term is therefore

\[
 \sum_{\substack{0\le h,k\le4\\(h,k)\ne(0,0)}}
 \frac{(1-h/5)(1-k/5)}{2^h3^k}
 =\left(\frac{129}{80}\right)\left(\frac{547}{405}\right)-1
 =:\mu=\frac{12721}{10800}.
\tag{17}
\]

These rational sums are exact analytical arithmetic, not a numerical
field experiment. Every nonresonant mode is covered by (16).

## 5. Pay the whole mirror/physical-derivative branch

The other phase from (8),(11) is

\[
 \psi_n=-2\Theta+T(\log n+\nu_{h,k}),
 \quad \psi_n'=-L/2+T'(\log n+\nu_{h,k}).
\tag{18}
\]

Since log n<=L/2 on its active interval and |nu|<=log1296,
psi_n'<=-L/4+O_*(1). After a fixed elementary gate it has magnitude
at least L/8 everywhere, and psi_n''=O_*(1/x). There are no uncharged
stationary points or connecting segments. Equations (13)--(14) and
integration by parts now cost O_*(n^(-3/4)/L_X) per index, including
the entry endpoint, so the **whole** mirror contribution is

\[
 O_*(X^{-7/8}/L_X).
\tag{19}
\]

Combining (12),(16),(17),(19) proves the full signed estimate (1).
One explicit sufficient accounting form is

\[
 |\langle PZ\rangle_X-\mu|
 \le C_*(L_X^{-1}+X^{-7/8}),\qquad
 |\langle P\rangle_X-1|\le C_*X^{-1}.
\tag{20}
\]

Choose C_* after the finite frequency/amplitude bounds, then impose

\[
 C_*\{L_X^{-1}+X^{-7/8}+(7/6)X^{-1}\}
 \le\frac{121}{21600}.
\tag{21}
\]

It is a finite uninstantiated gate. It pays strictly less than the
surplus mu-7/6=121/10800, so

\[
 \langle P(\operatorname{Re}Z-7/6)\rangle_X>0.
\]

Nonnegativity of P proves the actual pointwise consequence

\[
 \boxed{\ \exists x\in[X,2X]:\quad
 \operatorname{Re}Z(x)>7/6,\qquad\|R(x)\|_2>7/6.\ }
\tag{22}
\]

This holds in every sufficiently large dyadic interval. A witness can
be chosen away from the finite cutoff-entry set. No witness height has
been computed. The average is used to prove **existence of a point that
defeats a uniform comparison**; it is not used to exclude exceptional
collisions or infer uniform pointwise nonvanishing.

## 6. Full physical error budget and consequences

The source comparison is inherited from positive-time [CS6][cross] on
the same buffered chart. Its constants/onsets retain their original
same-model status. At every center the separate source components are

\[
 |\Delta V_0|\le C_0x^{-3/4},\qquad
 |\Delta V_1|\le C_1\frac{1+L}{L}x^{-3/4},
\]
\[
 c_H=x^{-3/4}\sqrt{C_0^2+
 ((|\alpha|C_0+C_1(1+L)/L)/\beta_c)^2}=O(x^{-3/4}).
\tag{23}
\]

For the actual completion R_c=exp(-pi^2t/64)G f_N, retain separately
|f_N|<=B_0x^(-1/4), |f_N'|<=B_1x^(-3/4), |G'/G|<=B_gamma and
|G|/E(0,x)<=B_G. Its value and physical derivative costs are

\[
 r_0=B_GB_0x^{-1/4}e^{-tL^2/16},\quad
 r_1=\frac{B_G}{L}
 (B_\gamma B_0x^{-1/4}+B_1x^{-3/4})e^{-tL^2/16},
\]
\[
 c_R=\sqrt{r_0^2+((|\alpha|r_0+r_1)/\beta_c)^2}
 =O(x^{-3/8}).
\tag{24}
\]

The completion's time exponential cancels the corresponding constant
carrier exponent exactly. No division by the completion or oscillating
field is made. These errors are paid once for the complete field, not
per resonator coefficient, mode or lag. No heat evolution is used;
F_N's nonzero residual is not a substitute for field error.

For the signed Fejer comparison the raw net margin is

\[
 \mathfrak m_K^{\rm signed}=1-\sqrt{A_K}-c_R-c_H.
\]

At each witness in (22), every K has sqrt(A_K)>=||R||>7/6. Hence

\[
 \boxed{\ \mathfrak m_K^{\rm signed}<-1/6-c_R-c_H<0
 \quad\text{for every }K.\ }
\tag{25}
\]

The guaranteed positive floor from that triangle consumer is zero.
This failure is independent of the precision of signed-lag acquisition.
Indeed any valid upper estimate of the same entire remainder norm must
exceed 7/6 there, whether or not it comes from Fejer.

The complete jet is **large in the same direction**, which explains why
this is a poor main/error split. Write the transformed exact jet as
mathsf T V_H=B_1+R+error, with error norm <=delta:=c_R+c_H. Its rotated
projection at a witness exceeds 13/6-delta. After the separate gate

\[
 \delta\le1/24,
\tag{26}
\]

we obtain at that witness

\[
 \|\mathsf T V_H-B_1\|_2>9/8,\qquad
 \operatorname{Re}\{e^{-i\Theta}(\mathsf T V_H)_\mathbb C\}>17/8,
\]
\[
 \boxed{\ \|V_H\|_2>17/48,\quad
 V_H=(H/A,H_z/(LA)),\quad\|\mathsf T\|<6.\ }
\tag{27}
\]

Thus the exact-field remainder also defeats leading-pair domination,
while the full jet has a positive auxiliary existential margin. There
is no contradiction: its leading/remainder mixed term is constructive.
Equation (27) is one unspecified point in every large dyadic interval,
not a uniform core margin, finite certificate, new covered zero-exclusion
region, practical cost claim or endpoint theorem.

The common onset is the maximum of the fixed buffer/source/carrier gates,
N(X)>=1296, the nonstationary phase gate, (21), and (26). All are finite;
none has been numerically instantiated. There is no RH assumption.

## 7. Scope, controls and disposition

This is a genuine signed estimate of the full arithmetic. It preserves
cross-block phases, both physical derivative branches, and cancellation
between signed lags in (2). The obstruction now concerns the actual
remainder, rather than an upper budget's avoidable loss. It specifically
closes **uniform n=1-versus-whole-remainder triangle domination in the
declared transformed physical norm at tL=2**. It does not close full
signed-square methods, larger justified main blocks, another norm,
restricted domains, useful finite charts or all J methods.

The classical outer tL>=61/24 comparator, its domain and unevaluated
arithmetic constants remain unchanged. The existential bound (27) is a
diagnostic byproduct, with no demonstrated all-height, effective-onset or
complete-cost gain. RH-to-simplicity at time zero and positive-threshold
collision exclusion still require their distinct missing uniform
arithmetic and coverage inputs.

For the [collision controls][controls], the resonator uses only primes
2 and 3 as a **test weight**, but the field under that weight is the
unchanged complete canonical arithmetic sum and its approximation.
Selected-prime identities alone do not supply that premise. Euler-factor
controls alter coefficients/factors; weighted-square controls lack full
reflection and the complete canonical approximation and have no all-real
heat time; reflected/primitive controls lack integer-square arithmetic;
finite-prime-compatible and close-source controls lack the full unchanged
arithmetic data. Generic heat doubles and positive carriers do not
supply the canonical weights or CS6. Good points can coexist with
collisions in those controls, so the auxiliary existence statement is
not advertised as a successful exclusion test. Event-domain qualifiers
are retained; no numerical controls were rerun.

**Disposition:** HCB-05 round 4 is complete. Stop the declared leading-pair
triangle comparator at this benchmark, including its perfectly signed
Fejer implementation. A full-square or different-main-block estimate
needs different arithmetic control; none is assumed or launched here.
HCB-05 remains Open; HCB-09 adds same-model review only. HCB-02 and other
inherited statuses are unchanged; P is not automatically activated.
No source evaluations, sweep, manuscript milestone or snapshot occurred.

[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[cross]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[inputs]: SIGNED_LAG_RESONATOR_INPUTS_20261028.json
[n13]: 13_GLOBAL_PHYSICAL_CORRELATION_TEST_AND_SCOPED_STOP_20261028.md
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[refs]: ../references/04_SIGNED_LAG_RESONATOR_PRIMARY_SOURCE_20261028.md
[results]: ../../../../result-summaries/README.md
[review]: ../reviews/09_SIGNED_LAG_RESONATOR_INTERNAL_REVIEW_20261028.md
[sound]: https://arxiv.org/pdf/0708.3990v2
