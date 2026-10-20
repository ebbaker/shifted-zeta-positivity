# BW-07: differentiation preserves the threshold and the necessary bound

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; recorded reasoning
effort **ultra**, as supplied by the parent research session.

**Status: conditional reduction and scoped closure audit, proved in-note;
separate same-model root review, not independent specialist review.** If the unchanged theta flow has an exact
m-fold zero at a>0 at its positive threshold T, then its (m-2)nd spatial
derivative has a double zero at the same point and has **the same all-real
threshold T**. Both parity classes retain the positive-source argument
behind BW-08's imaginary-axis floor. Consequently the existing necessary
double-jet bound and its critical-value transfer extend to the differentiated
flow, with complete moments through order m+4.

This is **not a reduction of a proved exclusion theorem**: no such BW-01
theorem is available. The complete theta source changes, and the degree of
the derivative jet is not the degree of the original physical jet.
These are the exact outstanding closure obligations. No theta event,
numerical theta jet, later witness or RH conclusion is obtained.
The [review][review] assesses the proof and exact controls.

Read the [result summaries][results], especially [local laws][laws] and
[collision controls][controls], and the [patterns to avoid][avoid],
especially [target classification][a01], [premise screening][a02] and
[scoped conclusions][a07]. The [opening note][initial] specifies this
bounded task. Its actual consumers are [BW-08 Note 03][bw08] and
[BW-01's paired-face contract][bw01contract], not a hypothetical theorem
with unspecified premises.

## 1. Exact transformation and its source

Use the complete source and normalization of the BW-01 contract:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \Phi(u)>0\quad(u\ge0).
\]

All moments below exist, and differentiation in t or z is dominated on
compact parameter sets. Write k=m-2, epsilon=k mod 2 and choose the fixed
real sign

\[
G_k(t,z)=
\begin{cases}
(-1)^{k/2}\partial_z^kH(t,z),&k\text{ even},\\
(-1)^{(k+1)/2}\partial_z^kH(t,z),&k\text{ odd}.
\end{cases}                                                     \tag{1}
\]

Then G_k is the cosine transform of u^k Phi when k is even and the
**positive sine transform** of u^k Phi when k is odd. In both cases
G_t=-G_zz. At an exact m-fold event its value and first derivative vanish,
and G_zz(T,a)=c_k h_m is nonzero, where c_k is the sign in (1) and
h_j=partial_z^j H(T,a).

For k even G_k(t,0)>0. For k odd G_k(t,0)=0 and
G_k,z(t,0)=M_(k+1)(t)>0, so the origin is a simple zero at every time.
The parity change is real but manageable. The weight u^k Phi is positive
on u>0; it is not the original spectral source when k>0. Its extension
to the full real u axis is even for even k and odd for odd k.

At t=0 the exact arithmetic identity is now

\[
A_k(0,b):=i^{-\epsilon}G_k(0,ib)
=\frac{\xi^{(k)}((b+1)/2)}{8\,2^k},\qquad b>0,                 \tag{2}
\]

obtained by k differentiations in b of H(0,ib)=xi((b+1)/2)/8.
Thus the original xi identity is not literally preserved. The floor
below will compare with the unchanged k=0 source instead of assuming
an unproved lower bound for the logarithmic derivative of xi^(k).

## 2. The transformed all-real threshold really is T

At every t>=T the original H(t,.) is an even order-one real entire
function with only real zeros and H(t,0)>0. Its paired canonical product
has real-rooted polynomial truncations converging locally uniformly.
Their kth derivatives converge locally uniformly to partial_z^k H;
Rolle's theorem and Hurwitz's theorem therefore put G_k(t,.) in the
Laguerre-Pólya class. This is the usual differentiation closure; see
[Bergweiler–Eremenko–Langley, introduction][lp] for the classical class
and closure statement. Here the paired product supplies the required
approximating polynomials directly.

We also need forward preservation starting from a possibly earlier
all-real slice of G_k. The following argument includes both parities and
does not assume that the canonical theta threshold theorem applies to a
changed source.

Suppose G_k(t0,.) is all-real. Its parity, order at most one and nonzero
value (even case) or simple origin (odd case) give a product

\[
G_k(t_0,z)=Cz^\epsilon\prod_{\rho>0}
 (1-z^2/\rho^2)^{n_\rho},                                  \tag{3}
\]

with no nonconstant exponential factor. Indeed the possible linear
Hadamard exponential is ruled out by parity. The paired product converges
because the original order bound is at most one. It again gives
real-rooted polynomial approximations.

For a real-rooted polynomial p and real c, (1+c partial_z)p is real-rooted:
away from p's real zeros, p'/p=sum_r 1/(z-r), whose imaginary part is
nonzero whenever Im z is nonzero, and hence cannot equal the real number
-1/c. Shared repeated roots stay real. The claim passes to nonzero
locally uniform limits by derivative convergence and Hurwitz. Therefore

\[
E_n=(1-(s/n)\partial_z^2)^n
=\{(1-\sqrt{s/n}\partial_z)(1+\sqrt{s/n}\partial_z)\}^n
\]

preserves this class for every s>0. On the exact sine or cosine source,
E_n multiplies its integrand by (1+s u^2/n)^n. This increases pointwise
to e^(s u^2) and is bounded above by it. On any compact z-set the
integrand is dominated by a constant times
u^k Phi(u)e^((t0+s)u^2+R u), which is integrable. Thus

\[
E_nG_k(t_0,\cdot)\longrightarrow G_k(t_0+s,\cdot)
\quad\hbox{locally uniformly}.                              \tag{4}
\]

The limit is nonzero by its positive imaginary-axis integral. Its zeros
are real. Hence an all-real slice of G_k remains all-real forward.

Finally G_k has an ordinary double zero at (T,a). The local backward-heat
expansion, divided by g2=G_k,zz(T,a), is

\[
G_k(T+s,a+y)/g_2=y^2/2-s+O(|y|^3+|sy|+s^2).
\]

After y=sqrt(|s|)w, the leading polynomial for s<0 is w^2/2+1.
Rouché on two disjoint small discs around +/-i sqrt(2) gives nonreal
zeros for all sufficiently small negative s. If any t0<T were all-real,
(4) would make one of these later slices all-real, a contradiction.
Consequently

\[
\boxed{G_k(t,\cdot)\text{ has only real zeros exactly when }t\ge T.}
                                                                    \tag{5}
\]

This proves equality of thresholds **conditional on the assumed exact
m-fold theta event**. Differentiation can lower thresholds in other
families or when no multiple zero survives; no unconditional equality
for arbitrary derivatives is claimed. All zeros of G_k for t>T are
simple: a multiple zero there would have nonreal immediate predecessors
still above T by the same local heat splitting law.

## 3. The imaginary-axis floor survives both parities

For b>0, put

\[
A_k(t,b)=\int_0^\infty u^k e^{tu^2}\Phi(u)
 \begin{cases}\cosh(bu),&k\text{ even},\\\sinh(bu),&k\text{ odd}
 \end{cases}\,du>0,\quad D_k=\partial_b\log A_k.
\]

Under the probability measure proportional to this positive integrand,

\[
D_k(t,b)=\mathbb E[f_\epsilon(u)],\quad
\partial_tD_k=\operatorname{Cov}(u^2,f_\epsilon(u))\ge0,
\quad f_0=u\tanh(bu),\quad f_1=u\coth(bu).                 \tag{6}
\]

Both functions increase on u>0. For f1 this follows from
sinh(v)cosh(v)-v>0 for v>0; the removable limit is f1(0)=1/b.
The covariance is half the double integral of the product of increments.
The odd case uses coth, **not tanh**.

Compare with the k=0 cosh probability measure at the same (t,b).
For even k, its tilt u^k is increasing, so the same covariance argument
gives D_k>=D_0. For odd k, the tilt is u^k tanh(bu), also increasing.
First replace f1 by the smaller f0, then apply the covariance argument
to this tilt. This gives D_k>D_0 for odd k. For positive even k it is
also strict, because the continuous source has nontrivial support.
In particular, for every k>=0,

\[
D_k(T,b)\ge D_0(T,b)\ge D_0(0,b)
>\tfrac14\log((b+1)/(4\pi)),\qquad T\ge0,\ b\ge5.            \tag{7}
\]

The last inequality, including the complete Euler-series tail, is
already proved in [BW-08 Note 03, section 2][bw08]. No new special-function
estimate or truncated xi derivative has been substituted for it.

At the double zero of G_k put g_j=partial_z^jG_k(T,a). Deflation of its
two factors at +a gives

\[
S_k:=\frac{g_3^2}{9g_2^2}-\frac{g_4}{6g_2}
=\frac{1}{2a^2}+\frac{\epsilon}{a^2}
 +\sum_{\rho>0,\rho\ne a}n_\rho
 \left\{\frac1{(a-\rho)^2}+\frac1{(a+\rho)^2}\right\}.
\]

The optional origin contributes epsilon/a^2 to both this expression and
D_k(T,a)/a. It therefore cancels in the BW-08 comparison, and

\[
\boxed{S_k\ge D_k(T,a)/a-3/(2a^2)
>\ell(a):=\frac1{4a}\log\frac{a+1}{4\pi}-\frac{3}{2a^2}}
\qquad(a\ge5).                                             \tag{8}
\]

For a>=20, ell(a)>1/(2a^2)>0 as in BW-08. In terms of the original
physical jets the left side is
h_(m+1)^2/(9h_m^2)-h_(m+2)/(6h_m). It is the deflated invariant of
the **differentiated function**, not the m-fold deflation invariant of H.

The proof also supports any BW-08 comparison using b>=a. In that case
the origin leaves the nonnegative surplus epsilon(1/a^2-1/b^2), and

\[
S_k\ge\frac1{2a^2}+\frac{D_k(T,b)}b-\frac4{a^2+b^2}.
                                                               \tag{9}
\]

For example b=max(a,40) and (7) give the entirely explicit all-height
consequence S_k>1/(2a^2)+1/(40b). Indeed b>=40 implies
log((b+1)/(4pi))>1/2, while 4b/(a^2+b^2)<=4/b<=1/10.
This is a necessary inequality and permits collisions.
The parallel [BW-08 all-height note][bw08all] applies the same flexible-b
comparison directly to the m-fold deflation of H, a different invariant.

## 4. What transfers to BW-01, and what does not

The [BW-08 finite critical-value proof][bw08] applies to G_k because it
uses only the heat equation, a nonzero second jet, (8), and complete
derivative bounds. Let a>=20 and L=ell(a); alternatively use any positive
lower coefficient delivered by (9), at every a>0. Let
B_j>=sup_R|partial_z^jG_k| for j=3,...,6 on
R={|t-T|<=delta, |x-a|<=rho}, with delta<T, rho<a. Set
b2=|g2|/2 and require

\[
B_3\rho+B_4\delta\le|g_2|/2,\qquad B_3\delta<b_2\rho.
\]

There is a unique local critical curve c(t) of G_k and, with the signed
constant normalization v(t)=G_k(t,c(t))/g2,

\[
v''(T)=-\tfrac13(g_3/g_2)^2-6S_k<-C,
\quad C=\tfrac13(g_3/g_2)^2+6L>0.
\]

The complete third-derivative allowance is

\[
K=\frac1{|g_2|}\left(B_6+\frac{3B_3B_5}{b_2}
 +\frac{3B_3^2B_4}{b_2^2}+\frac{B_3^4}{b_2^3}\right).
\]

It yields v(T+s)+v(T-s)<=-Cs^2/2 for
0<s<=min(delta,3C/(2K)), omitting the second cap if K=0. The weaker
C=6L is sufficient. The required original derivative orders are
k+3 through k+6, hence m+1 through **m+4**. Complete moments
M_(k+j)(T+delta) are valid B_j. This transfer preserves the original
event time and location but observes a different critical curve.

The pair (G_k,G_k,x) has local degree -1 with the same dt wedge dx
orientation. The original pair (H,Hx) has degree -floor(m/2).
They differ already when m=4. Even when m=3 gives the same integer,
there is no automatic boundary homotopy between the two jets.
Multiplying both components by c_k has positive determinant; taking
derivatives is not a pointwise invertible target-coordinate change.

The centered quadratic remainder obstruction of BW-01 transfers too:
retaining only the differentiated quadratic collision model and symmetric
absolute remainder bounds cannot force degree zero. Better derivative
accuracy does not repair that information loss.

## 5. Complete shifted-moment and product-error interface

The analytic results use exact full-source integrals. For numerical
realization, every spatial derivative of G through order six needs the
corresponding original moment M_(k+j). The old common order-six tail is
**not** an allowance for arbitrary m. Here is a complete replacement.

Put J=m+4, beta=T+delta>0 and choose U>=1 so large that

\[
d_J=4\pi e^{4U}-9-J/U-2\beta U>0,\qquad
16\pi e^{4U}>2\beta.
\]

Keep N=4 theta modes on [0,U]. With B_N as defined in
[BW-01 Note 03, section 3][bw01], a common bound for all omitted modes
there, for every 0<=j<=J, is

\[
E_{\rm head}=e^{\beta U^2}U^J\mathcal B_4/8.
\]

For the all-mode exterior u>=U, use
u^j<=U^j exp(j(u-U)/U) and Phi_n<=2pi^2 n^4 exp(9u-pi n^2 e^(4u)).
The exponent has negative second derivative and negative tangent slope
at U. Integration under that tangent and summation of the mode ratio
give

\[
E_{\rm ext}=\frac{2\pi^2U^J
 e^{\beta U^2+9U-\pi e^{4U}}}
 {d_J(1-16e^{-3\pi e^{4U}})}.                                \tag{10}
\]

The negative theta correction was dropped only for this upper bound;
retained signed values still use the full two-term mode. Add outward
retained quadrature/rounding error to E_head+E_ext for each required
moment or derivative. These are disjoint, exhaustive source regions.
For low J, U=1 may suffice; for unbounded m it cannot be fixed at one.
There is no claim that this conservative error is numerically efficient.

For j=m,m+1,m+2, event intervals contribute
M_(j+2)(beta) DeltaT+M_(j+1)(beta) Deltaa to d_j, with beta covering
the complete paths. This still needs no order beyond m+4. For a certified
lower coefficient L>0 and approximate jets hhat_j with full errors d_j,
the necessary raw restriction is

\[
Q_L=2h_{m+1}^2-3h_mh_{m+2}-18Lh_m^2>0.
\]

Its complete product error is

\[
\begin{aligned}
|Q_L-\widehat Q_L|\le{}&2(2|\widehat h_{m+1}|d_{m+1}+d_{m+1}^2)\\
&+3(|\widehat h_m|d_{m+2}+|\widehat h_{m+2}|d_m+d_md_{m+2})\\
&+18|L|(2|\widehat h_m|d_m+d_m^2).
\end{aligned}                                               \tag{11}
\]

Require q=|hhat_m|-d_m>0 before normalizing, use q/2 for b2 and 1/q
in K, and use C=6L if ratios have not been enclosed. Parameter uncertainty
in a also enters L; an exact hypothetical a in this analytic theorem is
not a measured midpoint. No opposing upper bound on Q_L is supplied.

## 6. Premise audit, controls and the next actual task

| Premise or output | Differentiation audit |
| --- | --- |
| Heat equation, same (t,x), fixed sign normalizer | Preserved exactly. |
| Exact double zero | Preserved when k=m-2 and h_m is nonzero. |
| All-real threshold and future simplicity | Reproved in section 2, including odd k. |
| Positive half-line source | Preserved as u^k Phi; sine replaces cosine for odd k. |
| Evenness and nonzero origin | Fail for odd k; the simple origin is paid explicitly. |
| Original complete theta source and time-zero xi identity | Fail literally for k>0; (2) gives the changed identity. |
| BW-08 imaginary-axis floor | Reproved by positive tilts; does not require importing the unchanged identity for G. |
| Derivative errors through order six | Become original errors through order m+4; (10) replaces the fixed order-six tail. |
| BW-01 physical winding of H+iHx | Not transported by differentiation; only the derivative jet is controlled. |
| An arithmetic exclusion theorem | No base exclusion exists, and no closure of its unknown signed estimate has been proved. |

The [exact checker][checker] was specified to test polynomial controls
P_m=(1-x^2/a^2)^m for m=2,...,8 and a=1,20, with their own finite heat
sources and derivatives. It checks parity, exact event multiplicity,
the origin, the imaginary-axis/deflation comparison, heat commutation
and the critical-value curvature identity. It separately checks both
parities of the positive-tilt inequalities on a two-atom source at
b=log 2 and t=0,log 2, where every value reduces to a rational number.
These finite checks test normalization and algebra, not the universal
theorems, theta jets or a winding exclusion. A comparison falsely
rejecting one of these colliding polynomial controls would fail the test.

| Control family | Shared premises and missing discriminator |
| --- | --- |
| Hermite and even polynomial threshold controls | Heat equation, differentiation closure and all-real evolution pass. They have no theta source. The scalar bound alone can pass when enough real roots are added; it is not an exclusion. |
| Positive-kernel threshold controls q and q_(T,a) | Positive tilts and parity versions of (6) pass for their own sources; their unchanged xi identity fails. Threshold arguments require their own order and all-real hypotheses, not borrowed theta event data. |
| Weighted-square and finite-prime controls | Differentiation is defined, but unchanged normalized coefficients/xi identity fail. Their local events do not supply a global all-real slice; no threshold is invented. |
| Reflected smooth and positive-primitive controls | Reflection or auxiliary positivity does not supply the exact physical source or all-real threshold premises. Their own source/errors remain necessary. |
| Euler-factor controls | As BW-08 documents, their positive source and imaginary-axis floor both pass. Positive tilts preserve the same floor for their derivative family. They therefore remain a specific surviving screen for any exclusion based only on (7)–(9). |

BW-07's first task is completed as a **restricted closure theorem plus
precise remaining obstruction**. Differentiation does preserve more than
the elementary double-zero algebra: it preserves the actual threshold
and this particular quantitative necessary estimate. It does not close
the entire research program. The next useful step requires a proved
signed arithmetic double-event exclusion on the derivative-weighted
class, or a separate theorem transferring a derivative-jet contradiction
to the unchanged source. Repeating (8) at successively higher orders is
not an induction: there is no proved exclusion base case.

Source parent: b39c6cc9b4756bc14c2e500e327169db88571d1f, with uncommitted
research additions. The [execution record][record] binds this note, its
checker and inherited source notes by SHA-256. Hashes identify files;
the written arguments establish the conditional claims.

[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[bw08]: ../../08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[bw08all]: ../../08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[bw01contract]: ../../01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[bw01]: ../../01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md
[checker]: ../numerics/check_differentiation_closure.py
[record]: ../numerics/DIFFERENTIATION_CLOSURE_CONTROLS_20261020.json
[review]: ../reviews/01_DIFFERENTIATED_THRESHOLD_REVIEW_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[lp]: https://www.math.purdue.edu/~eremenko/dvi/bergweil.pdf
