# Height-localized spikes and the trajectories of nonreal zeros

6 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, actual **gpt-6-astra / max**, branch chat 0004.
**TND-O-B03 r2 — B/Astra**, author-directed brainstorming. One focused
analytical/source pass and local consistency check; no independent
assessment, numerical campaign or manuscript revision.

**Disposition: localization is a substantive continuation, and a nonreal
pair does produce a local signal. The missing implication is a sufficiently
strong arithmetic bound for that signal, with its window, background and
trajectory costs included.** The earlier fixed-sum finite-exception result
does not exclude this approach.

The author asks whether height-varying local statistics, together with
transport from a collision at positive Newman time to time zero, could
produce a spike that is impossible for zeta zeros. This note makes that
proposal quantitative. The [scope/input packet14](../../research-progress/handoffs/14_TND_O_B03_R2_LOCALIZED_STATISTICS_20261106_SCOPE.md)
records the task; the [primary-source ledger08](../../references/08_TND_O_B03_LOCALIZED_STATISTICS_SOURCE_USE_20261106.md)
records inspected versions and passages. The existing
[manuscript](../../manuscript/README.md), especially Sections 5 and12, is
unchanged. Its preliminary formulas are used at their proof-author scope.

## 1. Two independent notions of locality

Use lambda for Newman time, so H_lambda satisfies
partial_lambda H=-partial_z^2 H. A collision at lambda=lambda_*>0
is followed toward time zero by increasing

\[
s=\lambda_*-\lambda,\qquad 0\le s\le\lambda_*.
\tag{1}
\]

Zeta height is a different variable. At lambda=0, a conjugate H_0 pair
x±iy, y>0, corresponds to

\[
\rho_\pm=\frac12\pm\frac y2+i\theta,\qquad \theta=x/2.
\tag{2}
\]

Thus the pair has **exactly equal ordinates**, whatever its transverse
distance y. We call these zeros nonreal H zeros, not purely imaginary
zeros; H_lambda(iy)>0.

For statistics, fix a large height scale T, a movable center v in [T,2T],
and a width h=h(T)>0. Set

\[
L=\frac{\log T}{2\pi},\qquad
w_j(v)=w\!\left(\frac{t_j-v}{h}\right),\qquad
M=hL\int_{\mathbb R}w(r)^2\,dr,
\tag{3}
\]

where 0<=w<=1 is smooth, supported in [-1,1], and equals 1 on
[-1/2,1/2]. Sum over all zeta zeros rho_j=sigma_j+it_j with
multiplicity. The window makes each sum finite. M is a declared
density normalization, not an assertion that every window contains M zeros.

There are two scales: the height width h and the resolution of differences
t_j-t_k within that window. Making h smaller does not automatically improve
the second resolution, the arithmetic error, or uniformity in v.

The previous manuscript considered finite marked windows, but did not
develop these moving-center, shrinking-width statistics or a transport
estimate to the final window. Its Proposition 12.4 concerned two specified
cumulative normalized sums. It is not a theorem against the present family.

## 2. An exact positive spike from a single pair

Let phi be an even nonnegative Schwartz function with phi(0)=1. For
epsilon>0 define the unnormalized ordered-pair statistic

\[
S_{v,h,\epsilon}
=\sum_{j\ne k}w_j(v)w_k(v)
  \phi\!\left(\frac{L(t_j-t_k)}{\epsilon}\right).
\tag{4}
\]

The exclusion j!=k removes a zero's self-pair, not distinct copies at the
same ordinate. Positivity makes (4) useful as a lower-bound witness.

**Finite-window identity and bound.** If m_t is total multiplicity on a
horizontal line, then

\[
D_{v,h}:=\lim_{\epsilon\downarrow0}S_{v,h,\epsilon}
=\sum_t w\!\left(\frac{t-v}{h}\right)^2 m_t(m_t-1),
\qquad S_{v,h,\epsilon}\ge D_{v,h}.
\tag{5}
\]

Indeed, finitely many terms occur; phi tends to 0 at each nonzero scaled
difference and equals 1 at a zero difference. The inequality follows
because every other summand is nonnegative.

A conjugate H_0 pair as in (2) therefore contributes exactly

\[
2w\!\left(\frac{\theta-v}{h}\right)^2
\tag{6}
\]

to the coincident-ordinate part, for every epsilon. It gives at least 2
throughout |v-theta|<=h/2. The factor2 counts the two orders. It cannot
be canceled by the other terms in (4).

This is a spike at **zero separation**, with a height profile localized
near theta. Its contribution after dividing by M is 2w^2/M:
it remains order one when h is comparable to 1/L, but is diluted when
hL tends to infinity. This is the precise reason microscopic localization
can evade the previous bulk dilution.

For fixed T and h, the pair's profile integrates over all centers to
2h integral w^2. A center average over a length-T region sees only
O(h/T) raw weight from it, when the profile is contained in that region.
Similarly its fixed p-th moment costs O_p(h/T). A theorem holding for
almost every center can therefore miss the spike. Choosing the window
center after finding the zero requires either a bound uniform in the
relevant centers or a separate argument comparing spike size and width
with an averaged bound.

The atom does not uniquely identify an off-line pair: repeated
critical-line zeros also contribute. Vanishing of (5) for a covering
family of windows means every zero is simple and on the critical line,
which is stronger than RH alone. It is a reformulation to classify once,
not a new proven criterion.

## 3. What a sine-kernel comparison would need to pay

A near-zero sine-kernel main term has scale

\[
\begin{aligned}
I_\epsilon
&=\int_{\mathbb R}\phi(r/\epsilon)
  \left[1-\left(\frac{\sin\pi r}{\pi r}\right)^2\right]dr\\
&=C_\phi\epsilon^3+O_\phi(\epsilon^5),\qquad
C_\phi=\frac{\pi^2}{3}\int_{\mathbb R}r^2\phi(r)\,dr>0.
\end{aligned}
\tag{7}
\]

This follows by Taylor expansion, change of variable r=epsilon u, and
the finite fourth moment of phi. It is an elementary calculation of a
candidate main term, **not an asserted local zeta asymptotic**.

The finite height window can be retained exactly in this comparison.
For the unit-density sine process, put q=hL and
C_w(b)=integral w(r)w(r-b) dr. Its expected version of (4) is

\[
q\int_{\mathbb R}C_w(r/q)\phi(r/\epsilon)
 \left[1-\left(\frac{\sin\pi r}{\pi r}\right)^2\right]dr
\le M I_\epsilon.
\tag{7a}
\]

This follows by changing to the difference coordinate and using
C_w(b)<=C_w(0), a consequence of Cauchy--Schwarz. Moreover,
C_w(0)-C_w(b)=one half of the squared L2 distance between w and
its translate, at most b^2 integral |w'|^2/2. Thus the difference
between the right and left sides of (7a) is O_w,phi(epsilon^5/q).
This justifies the proposed upper main term even when a finite-window
correction matters; it remains a reference-process calculation.

Suppose one could independently prove, in a relevant range,

\[
S_{v,h,\epsilon}\le M I_\epsilon+E(T,h,\epsilon)
\tag{8}
\]

uniformly at the centers supplied by the trajectory. A plateau pair
contradicts (8) only if its entire right-hand side is less than 2.
For M tending to infinity, this calls for epsilon at most a sufficiently
small multiple of M^(-1/3), together with an **absolute** error below
the remaining margin. An error o(M), obtained from an ordinary normalized
o(1), is insufficient. An o(1) absolute error would suffice.

Narrowing the test also expands its Fourier scale:
the transform of phi(r/epsilon) is epsilon times hat(phi)(epsilon xi).
Even if hat(phi) initially has fixed compact support, this support grows
like 1/epsilon. The known bounded-frequency theorem does not automatically
supply that range. Nor does replacing the cumulative cutoff by a
microscopic height window follow from its leading asymptotic.

This is one possible route, with a demanding remainder and uniformity
requirement. Unmarked near-pair tests also respond to close real pairs.
A theorem ruling out all sufficiently close pairs would demand more than
exclusion of nonreal zeros; retaining a transverse mark may be better.

## 4. What published localized statistics actually establish

Maples–Rodgers, [arXiv1404.3080v2](https://arxiv.org/abs/1404.3080v2),
Theorem 1.2, gives an unconditional mesoscopic CLT with random center
in [T,2T], n(T) tending to infinity but o(log T), and compact
bounded-variation tests of diverging variance. It is not a uniform
microscopic assertion.

Their Proposition 2.5 also gives, with N(sigma,u) counting zeros to the
right of sigma, for fixed integer k>=1, 1<=H<=T^(1/4) and 0<c<1/2,

\[
\frac1T\int_0^T
 |N(\sigma,v+H/\log T)-N(\sigma,v)|^k\,dv
 \ll_{c,k}H^kT^{-c(\sigma-1/2)}.
\tag{9}
\]

Use this for 1/2<sigma<1. Here H is their dimensionless width, so the
physical window width is H/log T, distinct from our h.

**Own comparison with a single spike.** One off-line zero in the interior
contributes at least H/(T log T) to the left side of (9), for every fixed
k. For fixed H and sigma this is much smaller than the allowance on the
right. Thus this inspected estimate permits a single narrow spike.
Letting k grow requires control of the k-dependent constants, not just
the fixed-k statement.

Rodgers' [arXiv1502.05658v3](https://arxiv.org/abs/1502.05658v3),
Theorem 1.1/Corollary 1.2, bounds microscopic clump frequencies by
exp(-c A log A) under RH. The theorem averages over centers; it does
not supply an unconditional pointwise exclusion at one exceptional height.
The remark after Corollary 1.2 mentions a weaker unconditional exponential
tail. It is not used here as a fully specified new input.

These are relevant tools and possible starting points. The inspected
sources do not pay (8), or the amplitude comparison in Section 8 below.
This is not an exhaustive assertion that no other local theorem exists.

## 5. From the collision to a quantitative pair trajectory

Suppose that on a specified interval 0<=s<=S there is a conjugation-symmetric
isolating neighborhood containing exactly the two zeros in question.
Factor, with a monic quadratic,

\[
H_{\lambda_*-s}(z)=
 [(z-x(s))^2+y(s)^2]\,U(s,z),\qquad
g(s,z)=\partial_z\log U(s,z).
\tag{10}
\]

The unit U is nonzero in this neighborhood and real on its real segment.
For s>0 suppose the roots are simple and y(s)>0.
Implicit differentiation of the forward heat equation in s gives

\[
x_s=-2\Re g(s,x+iy),\qquad
(y^2)_s=2-4y\,\Im g(s,x+iy).
\tag{11}
\]

The pair's mutual interaction is imaginary, hence cancels from its
midpoint velocity. These are manuscript(12.13)–(12.16) with the time
direction reversed.

Put u=y^2 and

\[
k(s)=\frac{\Im g(s,x+iy)}{y}
=\int_0^1\Re g_z(s,x+iry)\,dr.
\]

The second equality follows by integration along the vertical segment,
since g(s,x) is real. Then u_s=2-4k(s)u, u(0)=0, and the exact
integrating-factor identity is

\[
u(s)=2\int_0^s
  \exp\!\left(-4\int_r^s k(q)\,dq\right)\,dr.
\tag{12}
\]

**Conditional tube bounds.** If |g_z|<=K on those vertical segments and
|Re g(s,x+iy)|<=V throughout the interval, then

\[
\frac{1-e^{-4Ks}}{2K}\le y(s)^2
\le\frac{e^{4Ks}-1}{2K},\qquad
|x(s)-x_*|\le2Vs.
\tag{13}
\]

For K=0 both transverse bounds mean 2s. These follow directly from (12)
and integration of the first equation in (11). At s=lambda_* they give
a lower transverse distance and a final zeta-height enclosure
|theta-x_*/2|<=V lambda_*, **if the paid tube reaches that time**.

There is no presumption that an arbitrarily small event neighborhood
extends all the way to lambda=0. A source-based proof needs the contour
zero count, nonzero boundary, two-root isolation, complete-source error
and bounds for g,g_z over the entire proposed tube. Bounds that keep the
predicted enclosure strictly within that tube provide a continuation
scheme, but their availability is the unresolved canonical input.

Near the event, the existing coefficients ell and kappa give

\[
x(s)=x_*-2\ell s+O(s^2),\qquad
y(s)^2=2s-4\kappa s^2+O(s^3).
\tag{14}
\]

The midpoint coefficient is -2ell=-2b/(3a), not the critical-curve
velocity -b/a. Equation(14) follows from manuscript(5.6),(5.12),(5.17),
or by expanding(11). The constants and neighborhood are event-dependent.

A transverse statistic at lambda=0 can retain this information:

\[
A_{v,h}=\sum_jw_j(v)^2 L^2(\sigma_j-\tfrac12)^2.
\tag{15}
\]

Write y_f=y(s=lambda_*) for the value at **Newman** time zero.
The isolated pair contributes L^2 y_f^2 w((theta-v)/h)^2/2. Unlike the coincidence atom, this signal grows as the
pair moves off the axis. Near collision its natural dimensionless time
is sL^2, because its scaled transverse coordinate is Ly/2.
The assertion A=0 for every window would simply restate RH.

## 6. Global and environmental benchmarks for the motion

The local formulation (10) does not need an infinite sum.
For the canonical family, Polymath
[arXiv1904.12438v2](https://arxiv.org/html/1904.12438v2#S3),
Proposition 3.1, also supplies the paired, convergent full zero-dynamics
formula, including the complex regime. Theorem 3.2 records de Bruijn's
strip contraction:

\[
Y(\lambda_2)^2
\le\max\{Y(\lambda_1)^2-2(\lambda_2-\lambda_1),0\},
\tag{16}
\]

where Y is the supremal transverse width and lambda_2>lambda_1;
one obtains the supremum formulation by decreasing an allowed strip bound.

**Consequence, not a new upper-bound theorem.** A positive collision at
lambda_* has nonreal zeros immediately below it, hence Lambda>=lambda_*.
The same strip theorem gives Lambda<=Y(0)^2/2. Therefore
Y(0)>=sqrt(2lambda_*). If the supremum is not attained, this means that
zeros exist beyond every smaller transverse threshold. It identifies
some transverse defect but does not locate it near x_*/2 or trace one
unchanged pair there. It is already implicit in the classical strip bound.

There is a useful conditional amplification calculation. Follow a simple
upper zero x+iy which remains of **maximal imaginary part** while s
increases. All other imaginary-part forces then have the same outward
sign in this time direction. If at every time there are at least m>=1
real zeros within horizontal distance R of x, and u(0)=0 at the
collision, the full dynamics implies

\[
u_s\ge2+\frac{4mu}{R^2+u}.
\tag{17}
\]

The 2 is the conjugate partner; each of the m real zeros contributes
4u/((x-r)^2+u), and all omitted terms are nonnegative.
While u<=R^2 this yields

\[
u(s)\ge \frac{R^2}{m}
 \left(e^{\,2ms/R^2}-1\right).
\tag{18}
\]

Thus, if the assumptions persist, u reaches R^2 no later than
R^2 log(1+m)/(2m). After reaching it, (17) gives u_s>=2+2m.
Equation(18) is a conditional environmental estimate, not an available
uniform neighbor count. Maximality can switch between roots, a complex
collision can interrupt simple labeling, and the nearby real population
must remain present. Those are substantive proof obligations.
Maximality starting at y=0 also requires all the other zeros to be real
at the event; a generic collision inside the nonreal regime need not
satisfy it.

If 0<R<=1 and the assumptions persist to s=lambda_*, the canonical
time-zero strip y_f^2<1 gives the additional necessary bound

\[
\lambda_*\le
 \frac{R^2\log(1+m)}{2m}
 +\frac{1-R^2}{2+2m}.
\tag{18a}
\]

Indeed, the first term bounds the time to reach R^2, and the second
bounds the further time to reach 1. This is a conditional comparison with
a known strip, not a new numerical Newman bound: persistent real-neighbor
counts, maximality and continuation remain unpaid.

The final Polymath paper's Proposition 3.3 uses spatial zero-free barriers
to control transport. Its initial, far-field and intervening-wall
hypotheses cannot be discarded. This is an existing rigorous comparator
for any new height-localized trajectory method. The earlier Tao research
post discusses the difficulty of controlling longitudinal drift; the later
paper is the theorem source.

## 7. Localizing a transverse balance introduces extra terms

For a fixed isolated finite cluster with simple roots on an interval,
let z_j=x_j+iy_j, let g denote its exterior logarithmic derivative, and
let a_j(s) be differentiable real window weights. In backward Newman
time s the exact weighted identity is

\[
\frac d{ds}\sum_j a_j y_j^2
=
4\sum_{j<k}\frac{(a_jy_j-a_ky_k)(y_j-y_k)}
 {|z_j-z_k|^2}
-4\sum_j a_jy_j\Im g(z_j)
+\sum_j a'_j y_j^2.
\tag{19}
\]

Multiply the imaginary component of the finite root equation by 2a_jy_j
and pair the j,k terms. For a_j=w((x_j-X(s))/R(s)),

\[
a'_j=w'\!\left(\frac{x_j-X}{R}\right)
 \left[\frac{x'_j-X'}R-\frac{(x_j-X)R'}{R^2}\right].
\tag{20}
\]

Even the internal term is not automatically positive after localization:

\[
(a_jy_j-a_ky_k)(y_j-y_k)
=\frac{a_j+a_k}{2}(y_j-y_k)^2
 +\frac{a_j-a_k}{2}(y_j^2-y_k^2).
\]

The second summand, window-motion term and exterior force must be
estimated. A cutoff cannot simply be inserted into the unweighted
monotonicity formula. Moving the center with the selected pair preserves
its plateau weight, but does not remove these terms for its neighbors.

A path traversing many heights over different times does not itself
create many zeros at those heights at the final time. To turn a
space-time path into a large final spatial statistic requires a separate
amplification or width argument. The two-zero model below demonstrates
this distinction.

## 8. A transverse-sensitive analytic statistic and its background cost

The second candidate is a height-weighted version of the analytic
complex-difference sum. For a>=0 set

\[
E_{v,h}(a)=\sum_{j,k}w_jw_k
 e^{a(\rho_j-\rho_k)}W(\rho_j-\rho_k),\qquad
W(q)=\frac4{4-q^2}.
\tag{21}
\]

Because the real weights are equal on reflected partners
rho -> 1-conjugate(rho), the finite identity

\[
E_{v,h}(a)=
\int_{\mathbb R}e^{-2|r|}
 \left|\sum_j w_j e^{(\rho_j-1/2)(a+r)}\right|^2dr\ge0
\tag{22}
\]

follows by the same integral/relabeling proof as manuscript Proposition 12.2.
This is a finite algebraic extension of the already attributed positivity;
no height-localized arithmetic asymptotic is imported with it.

For a pair(2), write d=y_f at Newman time zero, so 0<d<1. Its isolated
contribution, including its two self terms, is exactly

\[
P=2w_0^2[1+W(d)\cosh(ad)].
\tag{23}
\]

When a=alpha log T and d is fixed, this can grow like T^(alpha d).
For d=O(1/log T), this particular amplification remains bounded.

Other terms in (21) can interfere. Let B be the squared norm in (22)
of the exterior/background sum. The reverse triangle inequality gives

\[
E_{v,h}(a)\ge(\sqrt P-\sqrt B)_+^2.
\tag{24}
\]

It does **not** give E>=P. If independent bounds give E<=U and B<=V,
the necessary condition is P<=(sqrt U+sqrt V)^2. These two error budgets,
plus a lower bound for d, make a concrete possible contradiction target.

For illustration only, if every background zero in the window lies on
the critical line, then sqrt B<=sum_background w_j: each exponential
has unit modulus in the norm(22), whose weight integrates to 1.
An off-line background needs its own bound. Assuming all other zeros
are real is not part of the proposed unconditional route.

Averaged estimates could also suffice if the spike is large enough.
If E>=A throughout an interval J of centers of length ell contained
in [T,2T], then for p>0

\[
\frac1T\int_T^{2T}E_{v,h}(a)^p\,dv\ge\frac{\ell}{T}A^p.
\tag{25}
\]

Thus one need not insist on a pointwise upper theorem: a proved averaged
moment smaller than this lower bound would contradict the spike.
For a plateau ell comparable to h and a surviving signal comparable to
T^(alpha d), the lower scale is (h/T)T^(p alpha d). This explains
how transverse growth might defeat dilution in principle. It requires
a lower bound **after** interference and an applicable unconditional
moment estimate at that frequency/window scale. Neither is supplied here.

A fixed-height exception also does not generate a sequence of exceptions
at heights tending to infinity. An asymptotic theorem needs an effective
finite-height complement or a proved mechanism supplying such a sequence.

## 9. Controls, classification and a bounded next brainstorm

The elementary heat model H_lambda(z)=(z-x_*)^2+2(lambda_*-lambda)
has g=0, x fixed and y^2=2s. It satisfies (11)–(14), makes the exact
coincidence atom(6), and produces the transverse growth in(15)/(23).
A moving zero pair alone therefore creates no contradiction. This
polynomial is a local dynamical control, not a positive theta source.

The manuscript's exact smooth positive even colliding source supplies
the same local behavior while retaining the analytic heat/source/operator
hypotheses. It fails the **literal canonical theta arithmetic formula**.
The existing Euler-factor controls alter that arithmetic; weighted-square
controls lack the complete normalized reflection; fully reflected smooth
and positive-primitive controls lack the complete canonical square
coefficients. None is asserted to satisfy the proposed unproved localized
zeta comparison. This is the analytical control screen from
[result12](../../../../../../result-summaries/12_collision_controls_and_screening.md);
no fresh numerical control campaign was run.

Equations(5),(11)–(14),(19)–(24) are finite identities or explicitly
conditional bounds. Equations(8) and the arithmetic side of(24)/(25) are
**unproved estimate targets**. They are not established merely by
defining a statistic. The all-window statements D=0 and A=0 have the
reformulation status identified above. Follow
[pattern01](../../../../../../avoid/01_restating_the_target.md) and
[pattern02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).

Two candidates are now concrete enough for a further bounded discussion:

| Candidate | Signal | Missing payment |
| --- | --- | --- |
| Positive local coincidence statistic(4) | At least2 from one pair on a plateau, with no cancellation | Effective local small-gap bound with absolute error below one-pair scale; window and Fourier uniformity |
| Transverse-sensitive analytic statistic(21) | cosh(ad) amplification from the trajectory | Reachable height/transverse bounds, background norm, and an unconditional pointwise or sufficiently strong averaged moment bound |

The next brainstorm should compare these two targets, not launch a broad
statistics search. A useful first question is whether one can pay a finite
canonical tube or a spatial barrier and then obtain an amplitude/width
lower bound that lies outside an **actually stated** arithmetic estimate.
The coupled coefficient/source information from B02 is relevant to that
payment. No control route or execution contract is selected in this note.

## 10. Check and continuation

Local checking verified the time reversal, factors 2 in the ordered atom
and trajectory, factor 1/2 in the zeta transverse moment, midpoint versus
critical-point drift, integrating-factor bounds, epsilon^3 scaling,
weighted-force/window terms, and the Gram/background inequality. The
polynomial control attains the K=0 trajectory bounds. The real-neighbor
bound was checked by retaining only nonnegative forces under its stated
maximality hypothesis. No machine numerics or separate review was used.

[Continuation 05](05_TND_O_B03_LOCALIZED_STATISTICS_CONTINUATION_AND_MODEL_CHANGE_20261106.md)
supersedes the earlier default E05 routing for the author's requested
further brainstorming. E05 stays available but unactivated. The
[sole register](../../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md)
owns status. Use [result summaries](../../../../../../result-summaries/README.md),
[local geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[patterns](../../../../../../avoid/README.md) and
[scoped exclusions07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The reviewed literature leaves this proposed mechanism unresolved;
it does not exclude every localized statistical approach.

