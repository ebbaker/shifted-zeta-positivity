# Complete arithmetic packets at a double collision

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model **gpt-6-astra (Codex)**, reasoning effort **max**,
verified from this turn's metadata.

**Status: exact setup and explicit local remainder proved in-note.** The
arithmetic packet and source-tail estimates are imports. This note supplies
their reflected derivative bookkeeping and collision matching; it does not
claim an independent theta sign bound. The substantive control result of
this opening round is [Note 03][n03]. Assessment: [round-one self-review][review].

The [proposal][proposal] and [Euler-factor discussion][n01] motivate this
calculation. Classification follows the [result summaries][summaries],
[arithmetic identities][s14], [collision laws][s13], [patterns to avoid][avoid],
[restatement rule][a01] and [paired-cancellation rule][a12]. The matched
identity is preparation. A proved obstruction below concerns a specified
relaxation, not theta or every finite arithmetic formula.

## Reflected derivatives of the complete packet

Use the complete theta source and the normalization
\[
F(t,z)=\int_0^\infty e^{tu^2+izu}\Phi(u)\,du,
\qquad H(t,z)=\frac{F(t,z)+F(t,-z)}2.
\]
For \(d\ge1\), set \(a_d=\frac12\log d\),
\[
q_d(t,z)=d^{-1/2}e^{ta_d^2-iza_d},\qquad
\ell_d(t,w)=\int_0^{a_d}e^{tv^2+iwv}\Phi(v)\,dv.
\]
The [packet identity][packets] is
\[
\mathcal P_d(t,z)=q_d(t,z)
 [F(t,w)-\ell_d(t,w)]_{w=z+2ita_d}.
                                                               \tag{1}
\]
It is the half-line transform of \(D_d\Phi=d^{-1/2}\Phi(\cdot+a_d)
=\sum_{d\mid n}\phi_n\). For every integer \(j\ge0\),
\[
\partial_z^j\mathcal P_d
=q_d(t,z)(\partial_w-ia_d)^j
 [F(t,w)-\ell_d(t,w)]_{w=z+2ita_d}.                       \tag{2}
\]
Define the physical cosine packet
\[
G_d(t,z)=\frac{\mathcal P_d(t,z)+\mathcal P_d(t,-z)}2,
\]
so
\[
\partial_z^jG_d(t,z)
=\frac{\mathcal P_d^{(j)}(t,z)+(-1)^j\mathcal P_d^{(j)}(t,-z)}2.
                                                               \tag{3}
\]
In particular the reflected first derivative has a minus sign. Each G_d
satisfies \(\partial_tG_d=-\partial_z^2G_d\), is entire in z, and is real
on the real axis. At complex z, taking a real part is not a substitute for
(3). The source D_d Phi need not be even on the whole source line.

Equations (1)–(3) follow directly by the substitution v=u+a_d and
differentiation under the absolutely convergent source integral. The shifted
derivative in (2) represents the factor \([i(v-a_d)]^j\); it retains the
prefactor and lower interval automatically.

## One prime and two primes

For the baseline p=2, set \(B_2=H-G_2\) and \(A_2=G_2\). For P={2,3},
set
\[
B_P=H-G_2-G_3+G_6,\qquad A_P=G_2+G_3-G_6.
                                                               \tag{4}
\]
Here B_P is the cosine transform of the source with indices coprime to 6,
and A_P is the transform of the complementary indices. Both sources are
nonnegative on u>=0, despite the subtraction in A_P. Their cosine
transforms have no automatic sign. The mixed packet G_6 is retained.

Write \(f_1(t,z)=\int_0^\infty e^{tu^2}\phi_1(u)\cos(zu)\,du\). Then
\[
H=f_1+A_P+R_P,\qquad
R_P=\sum_{\substack{n>1\\(n,6)=1}}H_n.                 \tag{5}
\]
For p=2 alone the same identity has a remainder over odd n>=3.
For P={2,3}, the remainder starts at n=5.

On \(0\le t\le T_+\), \(|\operatorname{Im}z|\le Y\), the imported
complete-source bound is
\[
|\partial_z^jR_P|\le\epsilon_j(m;T_+,Y)
=\frac{2\pi^2m^4j!e^{-\pi m^2}}
 {(4\pi m^2-9-Y)^{j+1}(1-r_m)},\quad
r_m=(1+1/m)^4e^{-\pi(2m+1)},                            \tag{6}
\]
where m=5 (or 3 for the single prime), provided
\(\pi m^2\ge T_+/8\) and \(4\pi m^2-9-Y>0\).
This estimates the complete remainder, not the two separated large terms
in (1). Derivative bounds on each G_d also follow from (6), with m=d>=2,
by including all indices n>=d in its positive absolute majorant.

## Collision matching with a stated remainder

Assume an exact double event \((T,x_*)\), with T>0,
\[
H(T,x_*)=H_x(T,x_*)=0,\qquad c=H_{xx}(T,x_*)/2\ne0.
\]
Take \(s=T-t\), \(|y|\le R\), and \(x=x_*+\sqrt{s}\,y\).
For any real analytic heat field g in a neighborhood containing the
corresponding time and spatial segments, put
\(M_k(g)=\sup|\partial_x^kg|\) on that neighborhood. Taylor's theorem
in time and then in space gives
\[
g(T-s,x_*+\sqrt{s}y)
=g_*+\sqrt{s}y g'_*+s(1+y^2/2)g''_*+\mathcal R_g,
                                                               \tag{7}
\]
\[
|\mathcal R_g|
\le s^{3/2}(R+R^3/6)M_3(g)+\frac{s^2}{2}M_4(g).
                                                               \tag{8}
\]
Indeed the time expansion is g(T-s,x)=g(T,x)+s g_xx(T,x)
with remainder at most s^2 M_4/2. The two spatial remainders have sizes
s^(3/2) R^3 M_3/6 and s^(3/2) R M_3. Applying the same proof to g_x
gives (7) with every derivative index increased by one and the remainder
bounded by s^(3/2)(R+R^3/6)M_4+s^2M_5/2.

Apply this to the *complete* identity (5). Its event equations are
\[
(A_P)_*=-f_{1,*}-R_{P,*},\quad
(A_P)'_*=-f'_{1,*}-R'_{P,*},\quad
(A_P)''_*=2c-f''_{1,*}-R''_{P,*}.                        \tag{9}
\]
Combining (7) for all terms reproduces
\[
\left|\frac{H(T-s,x_*+\sqrt{s}y)}{cs}-(y^2+2)\right|
\le \frac{\sqrt{s}(R+R^3/6)M_3(H)+sM_4(H)/2}{|c|}.
                                                               \tag{10}
\]
Thus the normalization cost 1/|c| is explicit. Uniformity over an event
class requires a bound on the normalized derivatives; compactness of
T and x_* alone is insufficient.

The complex arguments inside A_P remain exactly those in (1). At T>0,
their imaginary displacements tend to T log d, while the rescaled
displacements diverge like T log d/sqrt(s). Equation (7) is a local
expansion of the *whole packet as a function of its physical base point*;
its coefficients still contain the fixed displaced observations. It does
not evaluate those observations by the local Taylor polynomial of H.

## A necessary exterior condition and the failed estimate

The unnormalized exterior pair \((A_P,A'_P)\) is defined independently
of the event and uses no division by H, H_x, or c. One consequence of (9) is
\[
W_P=f_1A'_P-f'_1A_P=f'_1R_P-f_1R'_P
\quad\text{at an event},
\]
\[
|W_P|\le |f'_1|\epsilon_0+|f_1|\epsilon_1.              \tag{11}
\]
At any stationary point H_x=0, the exact relation is instead
\[
W_P=-f'_1H+f'_1R_P-f_1R'_P.                             \tag{12}
\]
This is a quantitative necessary condition on specified exterior data.
Its small remainder follows from the existing source-tail estimate; it
does not give an independent sign for W_P or for the curvature.

For example, replacing H_xx in the stationary expression
\(\mathcal L_0=-HH_{xx}\) using (5) leaves
\[
\mathcal L_0=-H(f''_1+A''_P)-HR''_P,\qquad
|HR''_P|\le\epsilon_2|H|.                              \tag{13}
\]
The first factor H remains complete. At the double-event predecessor,
|H| is of order s and E=H^2+H_x^2 is of order s^2. Hence (13) supplies
an epsilon_2 sqrt(E) error, not an energy-scale bound. Nothing in (11)
or (12) bounds the main signed curvature term at scale E. Enlarging a
fixed prime set decreases an absolute tail but does not repair this
normalization by itself.

The control construction in [Note 03][n03] satisfies the same selected
prime identities, correct primitive constant, and any prescribed finite
endpoint list. Its frozen collisions obey (7)–(13), with the remainder
bound multiplied by at most the coefficient bound. Therefore those
ingredients alone cannot imply a locally bounded stationary inequality
\(\mathcal L_0\ge-C E\) for that relaxed class.

This establishes the opening round's limitation precisely. It does not
rule out estimating the same finite expression using full modular
reflection or the complete constant-coefficient data.

## Bounded computational checks

The [checker][code] and [record][record] evaluate d=2,3,6, derivative orders
0,1,2, at t=1/4 and z=30+i/3, using 384-bit Arb/Acb arithmetic. Direct
source integration agrees with (2), and direct cosine integration agrees
with (3), within the recorded enclosures and analytic tails. Reversing
the reflected first-derivative sign is rejected in all three cases.
These are bounded regression checks of analytically proved identities;
interval overlap is not an independent proof of an identity.

For d=6 and j=0, the two integrals before subtraction have magnitudes
approximately 0.01664, while their difference has magnitude about
6.38e-48. This illustrates the cancellation at one fixed observation;
it is not a general conditioning estimate or evidence for theta positivity.
The same checker certifies the endpoint construction in Note 03.

[proposal]: ../research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[n01]: 01_FINITE_EULER_FACTORS_AND_HEAT_FLOW_CODEX_20261018.md
[n03]: 03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[review]: ../reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md
[code]: ../numerics/check_packets_and_orbits.py
[record]: ../numerics/PACKET_AND_ORBIT_CHECKS_20261018.json
[packets]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md
[summaries]: ../../../../result-summaries/README.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[s13]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
