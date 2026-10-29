# Signed arithmetic at tL=2: the inherited five-pair payment fails

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, HCB chat0003, thread `01a184c3-9ae9-7b53-ad7e-f4f104e0fe5b`.

**Status: proved scoped budget failure, using the inherited exponent-pair
package; separate-agent same-model internal review only.** This completes
[Note11][n11]'s bounded HCB-05 round-2 test at tL=2. The selected estimate
is the five-pair maximal-interval bound plus exact Abel summation from
[outer Notes32,39,43][o43]. It retains signed cancellation within each
block and applies to the actual quadratic heat weights and their physical
derivative. Its resulting complete lower-certificate budget is eventually
negative, even with an exact retained low block and zero source error.
This is an application and quantitative payment of the inherited
obstruction, not a new exclusion theorem or a no-go for other signed
methods. **Stop this tested consumer; HCB-05 remains Open.**

The central number is

\[
 \min_{p\in\{A^2P,AP,D,R,P\}}F_p(2/5;2)
 =\frac{321}{9950}>\frac1{50}.
\tag{1}
\]

The allocated high-block error grows faster than even the absolute upper
bound for the entire retained low jet. The actual signed high sum is
not proved to grow. No arithmetic source values, numerical research,
pair search, sweep, higher-order campaign or manuscript milestone was
produced. [Review07][review] records three same-model read-only checks.
[Input identities][inputs] and the [primary-source record][refs] preserve
scope and provenance; neither validates the full inherited proof chain.

Read the [result index][results], particularly [heat flow11][r11] and
[controls12][controls], and the [avoid index][avoid], particularly
[target classification][a01], [scoped failures][a07] and
[complete signed payments][a12]. Under avoid/01 the result is a failed
payment for a specified implementation, not another sufficient criterion.

## 1. Freeze the full signed model and physical derivative

Keep H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, and exactly Note11's benchmark

\[
 L=\log(X/(4\pi)),\quad N=\lfloor e^{L/2}\rfloor,\quad
 t=2/L,\quad z=X+u/L,\quad |u|\le1.
\tag{2}
\]

Reserve |u|<=2 and the upstream fixed complex buffers. Freeze X,L,N,
A=E_o(t,X)>0, Y=exp(L/5) and all block endpoints before spatial
differentiation. The lower comparison is on the real core. No time
transport or differentiation of a cutoff is used.

Use [Note10][n10]'s exact real E,Theta,rho=E_z/E and set

\[
 \lambda=\log(z/(4\pi)),\quad T_0=z/2+\pi t/8,\quad q=E/A,
 \quad\alpha=\rho/L,\quad\beta_c=\Theta_z/L
 =\frac{\lambda+\pi t/(4z)}{4L}.
\]
\[
 W(y)=y^{-1/2}e^{t((\log y)^2-\lambda\log y)/4},\quad
 U_r(I)=\sum_{n\in I}(\log n)^rW(n)n^{-iT_0}.
\tag{3}
\]

Here beta_c denotes the carrier slope; beta below denotes log M/L.
For a frozen set I the exact arithmetic jet is

\[
 V_I=q\begin{pmatrix}
 \operatorname{Re}(e^{i\Theta}U_0(I))\\
 \operatorname{Re}\left[e^{i\Theta}
 \{(\alpha+i\beta_c)U_0(I)
 -(t/(4zL)+i/(2L))U_1(I)\}\right]
 \end{pmatrix}.
\tag{4}
\]

Indeed partial_z U_0=-(t/(4z)+i/2)U_1, including the derivative of
the heat weight. Formula (4) retains the full physical derivative.
The complete V_F is the sum over all integers 1<=n<=N plus the
Riemann--Siegel completion jet.

For comparison use only the already calibrated invertible algebraic map

\[
 \mathsf T(v_0,v_1)=(v_0,(\alpha v_0-v_1)/\beta_c).
\tag{5}
\]

At tL=2 its gates must be rechecked: for large X, q>=1/2,
|alpha|<=1/16, 1/5<=beta_c<=1/3 and ||mathsf T||<6. In fact
z(lambda-L)+pi t/4 >=(-1+pi/2)/L>0, so
lambda+pi t/(4z)>=L. Thus Note10's paired contraction 0<=r_n<=1
still holds, with d_n<=t/(2z)=1/(Lz). These are direct elementary
checks on the new domain, not an extension of Note10's lower theorem.

## 2. Select and check the named signed estimate

Fix eta=10^(-5) and the five limiting pairs, retaining positive loss:

\[
 A^2P=(13/414,359/414),\quad AP=(13/194,76/97),\quad
 D=(18/199,593/796),
\]
\[
 R=(4742/38463,35731/51284),\qquad P=(13/84,55/84).
\tag{6}
\]

The selected inherited input is

\[
 \sup_{J\subset(M,2M]}
 \left|\sum_{n\in J}n^{-iT_0}\right|
 \le C_p T_0^{k_p+\eta}M^{l_p-k_p},
 \quad T_0\ge2\pi M.
\tag{EP}
\]

Constants C_p>0 and any validity thresholds are finite and unevaluated.
They are not set equal to one. Primary checks: [Bourgain v2, Theorem6][bou],
Section5, printed pp.20--21, and [Trudgian--Yang v3][ty], Section1.1,
(1.1)--(1.2), Lemma1.1 and the A-process; the repository's specialization
and positive-loss bookkeeping are in [outer Note32 §2][o32]. These were
selected-statement checks, not full proof audits. The logarithmic phase
has derivative (T_0/(2pi))/y exactly, so its monomial approximation error
is zero. Conjugation supplies the negative sign. Since M<=N and
T_0/(2pi) is comparable to exp(L), the required range holds eventually.
The maximal interval premise covers incomplete final blocks.

Choose I_low={1<=n<=Y} and the exact frozen grid

\[
 M_j=Y2^j<N,\qquad I_j=(M_j,\min(2M_j,N)]\cap\mathbb Z.
\tag{7}
\]

Together they cover every integer through N, with no omitted endpoints.
This is signed information between different modes within each I_j,
not Note10's sum of individual paired norms. It retains no cancellation
between different blocks.

For y in a high block, log y<=L/2 and log y>=L/5. Both W(y) and
(log y)W(y) decrease, because

\[
 \frac{d\log W}{d\log y}
 =-\frac12+\frac t2\log y-\frac{t\lambda}4
 =-1+\frac{\log y}{L}+o(1),
\]
\[
 \frac{d\log((\log y)W)}{d\log y}
 \le5/L-1/2+o(1)<0
\tag{8}
\]

after a finite onset. Define the best available unweighted allowance

\[
 a_j=\min_p C_pT_0^{k_p+\eta}M_j^{l_p-k_p}.
\]

Exact Abel summation, including the terminal endpoint, gives

\[
 |U_0(I_j)|\le W(M_j)a_j=:b_j,\qquad
 |U_1(I_j)|/L\le\frac{\log M_j}{L}\,b_j\le b_j/2.
\tag{9}
\]

The same a_j is valid for both components. No heat weight is dropped,
and the logarithm in the physical derivative is divided by L only after
the weighted sum has been estimated.

Put Z_r=e^(iTheta)U_r. The transformed second component divided by q
is exactly

\[
 \operatorname{Im}Z_0+
 \frac{t}{4zL\beta_c}\operatorname{Re}Z_1
 -\frac{1}{2L\beta_c}\operatorname{Im}Z_1.
\tag{10}
\]

Using (9), beta_c>=1/5 and t/(4z)<=1/4, its full two-component norm divided by q
is less than 4 b_j. Hence a legitimate complete high error allocation is

\[
 \mathcal B_{\rm EP}=4q\sum_j b_j,
 \qquad
 \left\|\mathsf T\sum_jV_{I_j}\right\|_2\le\mathcal B_{\rm EP}.
\tag{11}
\]

This keeps every high block and the physical derivative. It is the
specific budget tested below, not a claim of sharpness.

## 3. The exact positive power and an actual block attaining it

For beta=log M/L, local lambda-L=O(1/(XL)) and T_0/(exp L)=2pi+o(1)
give each term in (9) the limiting power

\[
 W(M)C_pT_0^{k_p+\eta}M^{l_p-k_p}
 =\widetilde C_p\exp\{L[F_p(\beta;2)+\eta]+o(1)\},
\]
\[
 F_{k,l}(\beta;2)=k+(l-k-1)\beta+\beta^2/2.
\tag{12}
\]

The constants tilde C_p are positive fixed multiples of the actual C_p.
At beta=2/5 exact substitution yields

| Pair | F(2/5;2) |
| --- | ---: |
| A^2P | 473/10350 |
| AP | 163/4850 |
| D | **321/9950** |
| R | 20939/641050 |
| P | 73/2100 |

This is also obtained from [outer Note39 §3][o39]'s inherited minimum
9/3980 at tL=5/2 by adding (1/8)(2/5)(3/5)=3/100 to every pair.
The positive-power obstruction already existed above this benchmark;
no discovery of a new universal obstruction is claimed.

It is not an isolated unattainable beta. Set

\[
 j_*=\lfloor L/(5\log2)\rfloor,\quad
 \beta_{j_*}\in[2/5-(\log2)/L,2/5].
\tag{13}
\]

For large X this is a genuine full block below N and inside D's
inherited assigned interval. Continuity of the five explicit polynomials
and the O(1/L) grid displacement show that, for some fixed c>0,

\[
 \mathcal B_{\rm EP}\ge4q b_{j_*}
 \ge c q\exp\{(321/9950+\eta)L\}.
\tag{14}
\]

This is a lower bound on the **allocated upper-error expression** (11).
It is not a lower bound on the actual oscillatory block or high jet.
The bounded grid displacement is absorbed into c, rather than into an
unpaid power. Optimizing among these five pairs and their fixed positive
constants does not change this conclusion.

## 4. Complete main/error comparison: even exact low data cannot pay it

Retain the entire signed low block exactly as the main jet V_low; assume
no favorable lower bound for it. For k=log n<=L/5, at the central height

\[
 W(n)=n^{-1}e^{k^2/(2L)}\le n^{-9/10}.
\]

The local-height correction costs at most exp(epsilon),
epsilon=|lambda-L|<=2/(XL). Therefore

\[
 \|\mathsf T V_{\rm low}\|_2
 \le q(1+1/(Lz))e^\epsilon\sum_{n\le Y}n^{-9/10}
 \le11q e^{L/50}
\tag{15}
\]

after the explicit eventual gate
(1+1/(L(X-1/L)))exp(2/(XL))<=11/10. Integral comparison gives
sum_{n<=Y}n^(-9/10)<=10Y^(1/10). This use of an absolute upper bound
serves only to bound how large any exact low main jet can be; the
selected high estimate remains signed EP information.

A lower certificate from this split would use

\[
 \|\mathsf T V_H\|_2\ge
 \underbrace{\|\mathsf T V_{\rm low}\|_2
 -\mathcal B_{\rm EP}-q c_R-q c_H}_{\mathcal L_{\rm cert}}.
\tag{16}
\]

But (14)--(15) imply

\[
 \mathcal L_{\rm cert}
 \le q\{11e^{L/50}-c e^{(321/9950+\eta)L}\}<0
\tag{17}
\]

for every sufficiently large X, even setting c_R=c_H=0. The exact
power gap is 321/9950-1/50=61/4975>0. This proves failure of the
complete declared certificate, not just failure to prove an o(1) error.
It does not imply that the actual model or exact field jet is small.

## 5. The favorable completion and source payments on this new benchmark

Recheck [CS25][cross] and Note10's exact carrier, rather than importing
the previous lower theorem. With R_c=exp(-pi^2 t/64)G f_N,
|f_N|<=B_0 X^(-1/4), |f_N'|<=B_1 X^(-3/4), |G'/G|<=B_gamma and
|G|/E(0,z)<=B_G, the value and physical derivative payments divided by q
are separately

\[
 r_0\le B_G B_0X^{-1/4}e^{-t\lambda^2/16},\quad
 r_1\le\frac{B_G}{L}
 (B_\gamma B_0X^{-1/4}+B_1X^{-3/4})e^{-t\lambda^2/16}.
\tag{18}
\]

The completion exponent cancels the carrier's constant time exponent
exactly. Its transformed payment is at most
c_R=sqrt(r_0^2+((|alpha|r_0+r_1)/beta_c)^2)=O(X^(-3/8)) here.
It is never divided by, including at its zeros.

The positive-time [CS6][cross] remains in domain. Keep its two constants:

\[
 |\Delta V_0|\le q C_0X^{-3/4},\quad
 |\Delta V_1|\le q C_1\frac{1+L}{L}X^{-3/4},
\]
\[
 c_H=X^{-3/4}\sqrt{C_0^2+
 ((|\alpha|C_0+C_1(1+L)/L)/\beta_c)^2}=O(X^{-3/4}).
\tag{19}
\]

Every inherited constant/onset is finite and uninstantiated. Both
payments vanish, while (14) grows. A smaller source error, more source
orders or a bounded norm condition cannot fix (17). No heat-transport
argument is used, so F_N's nonzero residual is not silently discarded.
No positive model or exact net floor is acquired; the returned net
certificate is precisely (16)--(17).

## 6. Why the inherited unweighted-zeta shortcut also cannot be reused

The exact elementary Dirichlet argument is

\[
 w_0=\tfrac12+\tfrac{t\lambda}4+iT_0,
 \quad\operatorname{Re}w_0=1\text{ at }z=X,
 \quad\operatorname{Re}w_0=1+O(1/(XL^2))\text{ on the core}.
\tag{20}
\]

The low weight-to-zeta discrepancy cannot be bounded by outer Note43's
summable infinite majorant: its exponent becomes 1/2+2/5=9/10<1.
Keeping the actual finite Y exposes an unsigned debit

\[
 B_{\rm low}=\sum_{2\le n\le Y}n^{-1}
 (e^{(\log n)^2/(2L)}-1)=\Theta(e^{L/50}).
\tag{21}
\]

For an elementary proof, the upper bound follows from (15). On the last
half-block Y/2<n<=Y, the harmonic sum is bounded below by a positive
constant, and the exponential is at least
exp((L/5-log2)^2/(2L))-1, a positive constant times exp(L/50)
eventually. Inserting log n/L on this same half-block retains the same
power, so the normalized derivative replacement debit is not cured by
its 1/L. These are growth statements about unsigned payments, not
about the signed replacement errors.

Nor can the ordinary zeta tail be completed absolutely at real part
one. The original analytic branch w=s+(t/2)alpha_Gamma(s) does not
restore the hypothesis: with outer58's explicit Stirling logarithmic
derivative, at s=(1+iX)/2,

\[
 \operatorname{Re}\alpha_\Gamma(s)-L/2
 =-\frac1{1+X^2}+\frac14\log(1+X^{-2})<0
\tag{22}
\]

for large X, so Re w<1 at the center. Analytic continuation of zeta is
not an ordinary absolutely convergent tail. Even a separately proved
replacement would still require new control of the zeta derivative in
(4): outer58's fixed Re w>=9/8 Euler-product/logarithmic-derivative
bounds do not apply. No nonvanishing, modulus floor or phase-slope
estimate for this replacement is assumed here.

Thus the direct block test above already retained the exact low sum;
it did not hide these invalid zeta substitutions inside its main term.

## 7. Required saving, comparator, controls and disposition

At beta=2/5 the heat amplitude is exp(-8L/25). Pair D supplies an
unweighted exponent 701/1990, whose excess is exactly

\[
 \frac{701}{1990}-\frac8{25}=\frac{321}{9950}.
\tag{23}
\]

Within this specific Abel-transfer framework, a replacement block bound
with unweighted exponent at most 8/25-kappa would give a decaying
weighted allowance exp(-kappa L). It needs an additional power saving
321/9950+kappa beyond D's limiting majorant, plus the imported positive
loss eta when comparing to the actual package. Removing the demonstrated positive power gap requires a saving of at
least 61/4975+eta. At equality constants decide dominance; a strictly
larger saving makes that high allowance lower order than the crude low
upper bound. Neither saving, nor a favorable physical jet floor, has
been proved. Other block groupings or direct cancellation
of the full vector may have a different demand.

The comparator remains [outer58][o58]'s tL>=61/24, 0<t<=1/2, with
its imported package, unevaluated onset and complete error
1728B_C(L)+409/L. That result is unchanged. This tested tL=2 consumer
supplies no smaller exterior constant, effective onset, finite
certificate, matched-margin or complete-cost improvement. Note39 had
already proved a five-pair obstruction at tL=5/2; (1),(17) identify its
complete physical-consumer payment at the proposed diagnostic benchmark.

The [collision-control screen][controls] is analytical. EP itself is a
generic bound for the logarithmic phase and need not reject controls.
The canonical expansion (3), its coefficients and CS6 comparison are the
used premises: Euler-factor controls alter those factors/coefficients;
weighted-square controls lack complete reflection and the canonical
approximation (and have no all-real heat time); reflected/primitive
controls lack the integer-square arithmetic; finite-prime-compatible
perturbations and close-source endpoint controls lack the unchanged
infinite arithmetic data. Free heat doubles and carrier positivity do
not supply (3) or (19). Since the selected consumer fails on the canonical
benchmark itself, no new successful quantitative control screen or
collision exclusion is claimed. Events outside this local domain are
not being tested. No numerical controls were rerun.

**Disposition:** HCB-05 round 2 is complete with a scoped negative return;
stop this five-pair blockwise-Abel, whole-high-as-error consumer at tL=2.
HCB-05's time-zero target remains Open; HCB-09 includes only same-model
internal review at this scope. HCB-02 and all inherited results retain
their statuses. No new P task is activated: its specific complete
integrated arithmetic quantity and below-one-event budget remain unpaid.
A new attempt must change the arithmetic information, not repeat this
consumer with smaller constants or additional height samples.

[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[avoid]: ../../../../avoid/README.md
[bou]: https://arxiv.org/pdf/1408.5794v2
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[cross]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[inputs]: SIGNED_ARITHMETIC_INPUTS_20261028.json
[n10]: 10_DIRECT_ARITHMETIC_JET_CALIBRATION_AND_STOP_20261028.md
[n11]: 11_CONTINUATION_FOR_SIGNED_ARITHMETIC_TEST_20261028.md
[o32]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md
[o39]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/39_CONVEX_DYADIC_WEIGHTED_REMAINDER_AUDIT_20261015.md
[o43]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md
[o58]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[refs]: ../references/02_SIGNED_EXPONENT_PAIR_PRIMARY_SOURCES_20261028.md
[results]: ../../../../result-summaries/README.md
[review]: ../reviews/07_SIGNED_ARITHMETIC_TEST_INTERNAL_REVIEW_20261028.md
[ty]: https://arxiv.org/pdf/2306.05599v3
