# Positive arithmetic packets and the remaining modular cancellation

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort
**max**, verified from the authoring turn metadata.

**Status: packet positivity and uniform relative bounds proved in-note;
numerical constants certified with Arb; same-assistant review only.** For
\(0\le t\le1/2\), every nonzero source formed with bounded nonnegative
coefficients from modes \(n\ge2\) has a strictly positive real cosine transform. The
complete \(\{2,3\}\) prime block approximates the full positive arithmetic
tail with relative error below \(7.3\times10^{-25}\), uniformly at every
real height. Its logarithmic curvature is bounded in absolute value by 117.
These are auxiliary estimates. The sign needed to exclude a theta collision
remains in the cancellation with the first source mode.

This continues [packet matching][n02] and its [finite-prime control screen][n03].
Classification follows the [result summaries][summaries], [arithmetic
identities][s14], [patterns to avoid][avoid], [target-reformulation rule][a01],
[paired-cancellation rule][a12] and [quantitative-gain rule][a20]. The new
numbers concern the complete arithmetic packets, not a bound for the Newman
constant. The full modular relation is retained in Section 4; its consequences
are not replaced by a finite endpoint test. Assessment: [self-review][review].

## 1. The arithmetic terms have positive cosine transforms

Use the existing normalization
\[
\phi_n(u)=e^{u-a}(2a^2-3a),\qquad a=\pi n^2e^{4u},\qquad
g_{n,t}(u)=e^{tu^2}\phi_n(u),\qquad
H_n(t,x)=\int_0^\infty g_{n,t}(u)\cos(xu)\,du.
\]
Thus \(H=\sum_{n\ge1}H_n\). In this note, a source prime denotes a
u derivative; an x derivative is explicitly marked or acts on a transform.

For \(n\ge2\), \(a>12\), and direct logarithmic differentiation gives
\[
\ell'=2tu+9-4a+\frac{12}{2a-3},\qquad
\ell''=2t-16a-\frac{96a}{(2a-3)^2},\qquad \ell=\log g_{n,t}.
\tag{1}
\]
Since \(2tu\le u\), \(12/(2a-3)<4/7\), and
\(a\ge12(1+4u)>u+9+4/7\), we have \(\ell'\le-3a\).
Also \(\ell''\ge-17a\). Consequently
\[
g_{n,t}'<0,\qquad
\frac{g_{n,t}''}{g_{n,t}}=(\ell')^2+\ell''
\ge9a^2-17a\ge7a^2>0.
\tag{2}
\]
All derivatives and polynomial moments are integrable. Integration by parts
twice, using \(g'(\infty)=0\), now gives the positive representation
\[
\boxed{H_n(t,x)=\frac1{x^2}\int_0^\infty
  g_{n,t}''(u)[1-\cos(xu)]\,du>0\quad(x\ne0).}
\tag{3}
\]
At x=0 the original integral is positive. Strictness in (3) follows from
\(g''>0\) on every interval and the fact that \(1-\cos(xu)\) is not
identically zero. Nonnegative sums inherit this conclusion whenever they
converge; bounded nonnegative coefficients suffice for the applications here.

This is an application of the classical convex-kernel principle, directly
proved above in the present normalization. See [Csordas, Theorem 3.4][polya].
The repository's [positive-primitive note][primitive] used the same principle
for a different source. Here it applies to the physical arithmetic modes
\(n\ge2\), and hence to the complete prime packets themselves. It does not
apply to the full theta source or automatically to the first mode.

For a finite prime set P, write \(Q=\prod_{p\in P}p\). As in Note 02,
\[
G_d=\sum_{d\mid n}H_n,\qquad
A_P=\sum_{(n,Q)>1}H_n,\qquad
R_P=\sum_{\substack{n>1\\(n,Q)=1}}H_n,\qquad C=A_P+R_P.
\tag{4}
\]
In particular \(A_{\{2,3\}}=G_2+G_3-G_6\). All four transforms
\(G_d\ (d\ge2), A_P, R_P, C\) are positive for nonempty P. The subtraction
in the displayed prime block is controlled by its exact coefficient selector.
This statement concerns the complete lower-interval-corrected packets of
Note 02, not isolated shifted F terms or independently heated Euler factors.

## 2. An explicit lower bound and relative remainder

Let P contain 2, and define
\[
\kappa=\frac78\phi_2(0)
=\frac78(32\pi^2-12\pi)e^{-4\pi}.
\]
Then, throughout the stated time interval and for every real x,
\[
\boxed{A_P(t,x)\ge H_2(t,x)\ge\frac{\kappa}{4096+x^2}.}
\tag{5}
\]
To prove the second inequality, take \(L=1/64\). On \([0,L]\),
\(a=4\pi e^{4u}<14\), since \(\pi<22/7\) and
\(e^{1/16}<16/15\). Equation (1) gives \(\ell'>-47\), so
\(g_{2,t}(u)\ge g_{2,t}(0)e^{-47/64}>\phi_2(0)/3\).
Equation (2) implies \(g_{2,t}''\ge336\phi_2(0)\) there. Finally,
\[
1-\frac{\sin v}{v}\ge\frac{v^2}{6(1+v^2)}\quad(v\in\mathbb R).
\tag{6}
\]
For \(|v|\le2\), use \(1-\sin(v)/v\ge v^2/6-v^4/120\);
for \(|v|\ge2\), use \(1-\sin(v)/v\ge1/2\).
Integrating (3) over \([0,L]\) and applying (6) proves (5), including
x=0 by continuity. No lower bound for H or its collision coefficient is used.

For any subset of indices \(n\ge m\ge2\), denote its summed source by
\(g_S\) and its cosine transform by V. Put
\[
r_{m,k}=(1+1/m)^k e^{-\pi(2m+1)},\quad
S_m=\frac{2\pi^2m^4e^{-\pi m^2}}{1-r_{m,4}},\quad
Q_m=\frac{8\pi^3m^6e^{-\pi m^2}}{1-r_{m,6}},
\]
\[
\epsilon_j(m)=\frac{S_m j!}{(4\pi m^2-9)^{j+1}}.
\tag{7}
\]
The ratios are below one. The bounds
\[
g_S(0)\le S_m,\quad -g_S'(0)\le Q_m,\quad
\int_0^\infty u^j g_S(u)\,du\le\epsilon_j(m)
\tag{8}
\]
follow by comparison with all integers n>=m. Indeed
\(g_{n,t}\le2(\pi n^2)^2e^{-\pi n^2-(4\pi n^2-9)u}\), from
\(e^{4u}\ge1+4u+8u^2\) and \(8\pi n^2\ge t\).
Also \(-\phi_n'(0)=e^{-a_0}(8a_0^3-30a_0^2+15a_0)<8a_0^3e^{-a_0}\),
where \(a_0=\pi n^2\). Successive numerator ratios give (7).

Equation (3) and \(\int g_S''=-g_S'(0)\) give
\[
0<V(t,x)\le\min\{\epsilon_0(m),2Q_m/x^2\}.
\tag{9}
\]
The second bound is only needed for x!=0. Thus, if every remainder index
is at least m,
\[
0<r_P:=\frac{R_P}{A_P}\le\rho_m
:=\frac{4096\epsilon_0(m)+2Q_m}{\kappa}.
\tag{10}
\]
The bound is uniform in real height and does not divide by physical energy.
In particular \(0<(C-A_P)/C\le\rho_m/(1+\rho_m)<\rho_m\).
The interval-certified constants are

| Prime set | First remainder index m | Uniform bound for R_P/A_P |
| --- | --- | --- |
| {2} | 3 | < 0.000263 |
| {2,3} | 5 | < 7.3e-25 |

The all-height assertion follows from (1)–(10), not sampling. The [Arb
record][record] certifies the rounded numbers in these analytic bounds.

## 3. The derivative bounds and an energy-scale payment

The same positive measure \(g_S''(u)du\) gives
\(\int u g_S''=g_S(0)\) and \(\int u^2 g_S''=2\int g_S\).
Differentiate (3) before estimating. For x!=0,
\[
|V_x|\le4Q_m/|x|^3+S_m/x^2,
\quad
|V_{xx}|\le12Q_m/x^4+4S_m/|x|^3+2\epsilon_0(m)/x^2.
\tag{11}
\]
For \(|x|\le64\), instead use \(|V^{(j)}|\le\epsilon_j(m)\).
Combining with (5) proves
\[
\frac{|V_x|}{A_P}\le\eta_1(m)
=\frac{\max\{8192\epsilon_1(m),Q_m/8+2S_m\}}{\kappa},
\]
\[
\frac{|V_{xx}|}{A_P}\le\eta_2(m)
=\frac{\max\{8192\epsilon_2(m),3Q_m/512+S_m/8+4\epsilon_0(m)\}}{\kappa}.
\tag{12}
\]
The argument also applies to V=A_P with m=2. Set
\(B_1=\eta_1(2)<10.75\), \(B_2=\eta_2(2)<0.671\). It follows that
\[
|\partial_x\log A_P|\le B_1,\qquad
|\partial_x^2\log A_P|\le B_2+B_1^2<117.
\tag{13}
\]
For the normalized remainder,
\[
|r_{P,x}|\le\eta_1(m)+B_1\rho_m,
\]
\[
|r_{P,xx}|\le\eta_2(m)+2B_1\eta_1(m)+(2B_1^2+B_2)\rho_m.
\tag{14}
\]
For P={2,3}, the three uniform bounds are
\[
\boxed{0<r_P<7.3\times10^{-25},\quad
|r_{P,x}|<7.9\times10^{-24},\quad
|r_{P,xx}|<1.7\times10^{-22}.}
\tag{15}
\]

There is now a legitimate, nonvanishing real-axis normalization
\(q=H/A_P\), with
\[
q=Z_P+r_P,\qquad Z_P=1+H_1/A_P.
\tag{16}
\]
It is real analytic near each real point. No assertion that A_P is nonzero
throughout a complex strip is needed or made. Both H and A_P obey the heat
equation, so
\[
q_t=-q_{xx}-2(\partial_x\log A_P)q_x.
\tag{17}
\]
For \(\mathcal L_0=H_x^2-HH_{xx}\), direct differentiation gives
\[
\boxed{\mathcal L_0
=A_P^2(q_x^2-qq_{xx})-(\partial_x^2\log A_P)H^2.}
\tag{18}
\]
The second term is bounded in absolute value by \(117H^2\le117E\).
Thus the positive arithmetic background contributes a bounded energy-scale
payment. The first term in (18) remains signed and unestimated. Equation
(18) is bookkeeping; (5), (10), (13) and (15) are the quantitative gains.

At a hypothetical double event in \(0<T\le1/2\), with
\(c=H_{xx}/2\ne0\), the necessary matching conditions become
\[
Z_P=-r_P\in[-\rho_m,0),\qquad Z_{P,x}=-r_{P,x},\qquad
Z_{P,xx}+r_{P,xx}=2c/A_P.
\tag{19}
\]
This gives a one-sided value band and a derivative tolerance for a specified
complete finite block. It places no sign restriction on the last expression.
The carrier bounds remain finite at the event; normalization of the local
collision germ still involves c, as in Note 02.

## 4. What the complete modular relation actually supplies

Retain the full identity
\[
\Theta(y)=y^{-1/2}\Theta(1/y),\quad
P(u)=e^u\Theta(e^{4u})=P(-u),\quad
\Phi=(P''-P)/16,
\tag{20}
\]
with \(\Theta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y}\).
This is the usual [theta transformation][dlmf], with the normalization used
in the [reflection-rigidity proof][rigidity]. Consequently the full weighted
source \(w_t=e^{tu^2}\Phi\) is even and rapidly decreasing with all derivatives.
Writing \(w_t=g_{1,t}+g_{A,t}+g_{R,t}\), the *whole* endpoint hierarchy is
\[
g_{1,t}^{(2k-1)}(0)+g_{A,t}^{(2k-1)}(0)+g_{R,t}^{(2k-1)}(0)=0
\quad(k\ge1).
\tag{21}
\]
This hierarchy is a consequence of the complete functional identity, not
an assumption inferred from finitely many checked derivatives.

In particular, with b=phi_1'(0),
\[
b=\sum_{n\ge2}-\phi_n'(0)>0,\quad
q_A=-g_{A,t}'(0)>0,\quad q_R=-g_{R,t}'(0)>0,\quad b=q_A+q_R.
\tag{22}
\]
These constants are independent of t. Repeated integration by parts yields
\[
H_1=-b/x^2+O(x^{-4}),\quad
A_P=q_A/x^2+O(x^{-4}),\quad R_P=q_R/x^2+O(x^{-4}),
\tag{23}
\]
whereas H and its spectral derivatives decay faster than every power. All
algebraic endpoint terms cancel in the complete sum, by (21). At the first
level the exact coupled integral is
\[
H(t,x)=-\frac1{x^2}\int_0^\infty
 (g_{1,t}''+g_{A,t}''+g_{R,t}'')\cos(xu)\,du\quad(x\ne0).
\tag{24}
\]
The first-mode second derivative has not acquired a nonnegative sign.
Equation (24) retains the cancellation; it supplies no pointwise sign for H
or for the first term in (18).

There is a precise limit to the relative approximation:
\[
r_P\longrightarrow q_R/q_A>0,\quad
Z_P\longrightarrow-q_R/q_A,\quad q=Z_P+r_P\longrightarrow0.
\tag{25}
\]
For P={2,3}, the endpoint ratio is approximately \(7.26538\times10^{-27}\).
Thus the narrow band in (19) is approached at large height even without an
event. It is a useful tolerance, not an independently excluding condition.

For each fixed finite P containing 2,
\[
H_1+A_P=H-R_P=-q_R/x^2+O(x^{-4})<0
\quad\text{for all sufficiently large }|x|.
\tag{26}
\]
**An accurate relative approximation to the positive arithmetic tail is not
a relative approximation to the vanishing physical field.** In particular,
discarding R_P destroys the all-order modular cancellation, however small
the number in (10). This is a statement about this fixed finite-prime
truncation, not a prohibition on controlled infinite assembly.

At a double-event stationary predecessor, q is of order s while r_P tends
to a fixed positive value at the event. An error independent of s in (15)
therefore cannot be promoted to an energy-scale estimate for the residual
term in (18). The bounded payment in that equation covers only the carrier.

## 5. Controls, checks and the next mathematical task

| Control | What survives here | Premise absent from the full theta coupling |
| --- | --- | --- |
| Positive weighted-square and finite-prime orbit controls | Positivity of every weighted n>=2 transform; a positive normalization and bounded carrier derivatives, with coefficient-dependent constants | The complete normalized modular reflection and its entire endpoint hierarchy |
| Reflected smooth and positive-primitive controls | Full source reflection and the universal quotient identity (18), wherever a carrier is chosen | The prescribed normalized integer-square expansion and hence this arithmetic packet identification |
| Euler-factor controls | Reflection and their correctly shifted heat identities | The unchanged normalized theta coefficients and lattice entering (4) and (20) |
| Generic heat germs | The local double-collision law | The complete source, coefficients and modular identity |

The [control catalogue][s12] and Note 03 specify these classes. In particular,
the positive-coefficient orbit controls can still collide; the new packet
positivity does not reject them. No source is claimed to satisfy both the
unchanged square expansion and full normalized reflection while differing
from theta. Their conjunction is rigid by the existing theorem, but that
uniqueness alone does not estimate (18).

The [checker][code] certifies the displayed scalar bounds in 384-bit Arb
arithmetic. It checks the first endpoint normalization using an infinite
tail bound. Eight finite-interval integrations verify (3) with the necessary
upper-boundary correction, and reject omitting that correction. The universal
convexity proof is analytic, not a numerical grid. These checks certify no
collision or full theta sign; the [execution record][record] gives their scope.

The next estimate must act on the complete residual q=Z_P+r_P, retaining
(20)–(24) before taking norms. A useful continuation would bound a signed
residual-curvature expression on a declared domain and compare it with the
117 energy payment. Merely proving positivity of another packet, reducing a
fixed absolute tolerance, or asserting a sign for the first term of (18)
would leave the collision question unchanged. No all-event criterion is
offered as a new result here.

[n02]: 02_COMPLETE_PACKET_MATCHING_CODEX_20261018.md
[n03]: 03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[review]: ../reviews/02_POSITIVE_PACKET_AND_MODULAR_CANCELLATION_SELF_REVIEW_CODEX_20261018.md
[code]: ../numerics/check_positive_packets.py
[record]: ../numerics/POSITIVE_PACKET_BOUNDS_20261018.json
[primitive]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
[rigidity]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md
[polya]: https://arxiv.org/html/1309.0055v2
[dlmf]: https://dlmf.nist.gov/20.7.E32
[summaries]: ../../../../result-summaries/README.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
