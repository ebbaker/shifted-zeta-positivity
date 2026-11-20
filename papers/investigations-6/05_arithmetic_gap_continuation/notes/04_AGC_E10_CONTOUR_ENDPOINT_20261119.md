# AGC-E10 module A: endpoint and complete time-integrated contour readouts

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Helper dispatch: **gpt-6.1-sol / ultra**; this records
the requested dispatch, not independent serving-backend attestation. No
additional actual backend or effort record was exposed to this helper.

Status: **proved in-note**, with one author correction pass; no numerical
verification, canonical acquisition, independent review or strict gain claim.
This is the module-A return for [AGC-E10 r1](../research-progress/handoffs/AGC-E10-r1-request.md)
under the [frozen B01 contract](../brainstorm/notes/02_AGC_B01_FIXED_CELL_COMPARISON_20261119.md).

## 1. Scope, inherited formula and frozen inputs

The [result index](../../../../result-summaries/README.md) and
[patterns index](../../../../avoid/README.md) govern the interpretation.
In particular, [Cluster 12](../../../../result-summaries/12_collision_controls_and_screening.md)
supplies the controls, and patterns
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
limit what the identities and allowances establish. Classification under
pattern 01: a finite conditional transfer identity and estimate, **not an
RH-equivalent criterion**. The endpoint identity below is inherited from
[manuscript Section 7](../manuscript/sections/07_program.tex),
`prog:log-moments` and `prog:centered-error`, and is rederived for this
packet. Its appearance here is not a new result or a gain.

Use exactly the physical holomorphic reference $P=P_N$ of
[Section 5](../manuscript/sections/05_arithmetic_source.tex), with unchanged
theta field $H$, and the exact defect of
[Section 6](../manuscript/sections/06_residual_transport.tex):

\[
R=P_t+P_{zz},\qquad E=H-P,\qquad
u=t_*-t,\quad E_u=E_{zz}+R.
\]

The B01 rectangle has $X-A\ge200$, $0<U<t_*\le1/2$, $0<h\le1$,
and one fixed natural cutoff throughout:

\[
N^2\le\frac{X-A}{4\pi}+\frac{t_*-U}{16},\qquad
\frac{X+A}{4\pi}+\frac{t_*}{16}<(N+1)^2.
\]

Let $\Gamma:|z-X|=r$, positively oriented, with $r<\min(A,h)$.
For every time where the readout is used, acquire the count two for
$P$, a nonzero contour denominator, and a complete residual enclosure.
No such acquisition at a specified height is asserted. We use no extension
across $\Re z=0$, new correction center or replacement reference.

Assume the fields are holomorphic near the closed disk and $C^1$ in
time on its contour collar, with the spatial regularity needed for their
displayed heat equations. Suppose on that collar, or on the contour with
a strict bound extended by continuity,

\[
|E/P|\le q(u)<1. \tag{1}
\]

Then $H$ is also nonzero on the contour and has count two by Rouché.
The principal power-series branch

\[
\ell(u,z)=\log(1+E/P)
=\sum_{k\ge1}\frac{(-1)^{k+1}}k(E/P)^k \tag{2}
\]

is single-valued on the collar and continuous in time. It need not extend
through the interior zeros. More generally, the exact formulas only need
such a contour logarithm and the two counts; (1) is a convenient paid gate.

## 2. Exact endpoint discriminant error

Write $\langle f\rangle=(2\pi i)^{-1}\oint_\Gamma f(z)\,dz$, and set

\[
A_j^F=\left\langle z^j F_z/F\right\rangle,\quad
c_F=A_1^F/2,\quad D_F=A_2^F/2-c_F^2,
\quad I_0=\langle\ell\rangle,\quad
I_1=\langle(z-c_P)\ell\rangle.
\]

For a count-two field these are the center and squared half-gap, including
at a double zero. Since $H_z/H-P_z/P=\ell_z$, integration by parts on
the closed contour gives, for $j=1,2$,

\[
A_j^H-A_j^P=-j\langle z^{j-1}\ell\rangle.
\]

Consequently

\[
\boxed{c_H-c_P=-I_0/2,\qquad
\delta:=D_H-D_P=-I_1-I_0^2/4.} \tag{3}
\]

Indeed $A_2^H-A_2^P=-2(I_1+c_PI_0)$, while
$c_H^2-c_P^2=-c_PI_0+I_0^2/4$. The center terms cancel, leaving
the full complex square in (3). It cannot be replaced by $|I_0|^2$
inside this exact identity. Conjugation symmetry of the physical fields
and circle makes $c_F,D_F,I_0,I_1$ real; a real positive $D_H$ is
equivalent to two distinct real zeros within this counted pair.

## 3. Value-only circle allowance

Put $L(u)=-\log(1-q(u))\ge0$ and $d(u)=|X-c_P(u)|$. From (2),
$|\ell|\le L$. Circle parametrization and Cauchy–Schwarz give

\[
|I_0|\le rL,\qquad
|I_1|\le \frac{rL}{2\pi}\int_0^{2\pi}
 |X-c_P+re^{i\theta}|\,d\theta
\le r\sqrt{r^2+d^2}\,L.
\]

Thus a fully explicit value-only allowance is

\[
\boxed{|D_H-D_P|\le B_{\rm end}(u)
:=r\sqrt{r^2+d(u)^2}\,L(u)+\frac{r^2L(u)^2}{4}.} \tag{4}
\]

Also $|c_H-c_P|\le rL/2$. The weaker elementary replacement
$r(r+d)L+r^2L^2/4$ is valid. Since both zeros of $P$ lie in the
disk, convexity gives $d<r$, so the still weaker bound
$\sqrt2\,r^2L+r^2L^2/4$ is available without locating their center.
Use an enclosure for $d$ in (4) if the center is uncertain.

A physical value envelope $|E|\le\varepsilon$ and denominator floor
$|P|\ge m>\varepsilon$ give $q=\varepsilon/m$. All errors in these
inputs, the count, the reference discriminant and contour quadrature
remain payable; (4) does not supply them. This allowance uses no derivative
error bound. It is an outer bound from separately bounded moments, not
claimed sharp for a common logarithm. Direct joint evaluation of (3),
including its square, can be narrower.

## 4. Complete signed time identity

All fields in this paragraph are evaluated at $t_*-u$. Define

\[
Q=\frac{PE_{zz}-P_{zz}E}{P(P+E)}
=\frac{H_{zz}}H-\frac{P_{zz}}P
\]

and the **complete** signed contour readout

\[
K(u)=\left\langle
(z-c_H)Q+(c_P-c_H)\frac{P_{zz}}P
+(z-c_P)\frac RP
\right\rangle. \tag{5}
\]

The sign in backward time is

\[
\delta_u=-K(u),\qquad
\boxed{\delta(u)=\delta(0)-\int_0^uK(v)\,dv.} \tag{6}
\]

This is Section 6 `rt:full-gap-error` integrated **before** taking
absolute values. In particular it includes both the moving-center error
and the reference heat defect.

For a direct proof and sign check, the equations of the frozen reference
give $P_u=P_{zz}-R$, $H_u=H_{zz}$, hence

\[
\ell_u=Q+R/P,\qquad
(c_P)_u=\tfrac12\langle R/P-P_{zz}/P\rangle. \tag{7}
\]

Let $\Psi=I_1+I_0^2/4=-\delta$. Differentiating the moving center in
$I_1$, retaining the square and using $c_H=c_P-I_0/2$, yields

\[
\begin{aligned}
\Psi_u
&=\langle(z-c_P)(Q+R/P)\rangle-(c_P)_u I_0
   +\tfrac12I_0\langle Q+R/P\rangle\\
&=\langle(z-c_H)Q+(z-c_P)R/P\rangle
   +\tfrac12I_0\langle R/P\rangle-(c_P)_u I_0\\
&=\langle(z-c_H)Q+(z-c_P)R/P
                +\tfrac12I_0 P_{zz}/P\rangle=K.
\end{aligned}
\]

Thus the exact endpoint reduction is

\[
\boxed{
-I_1(u)-I_0(u)^2/4
=-I_1(0)-I_0(0)^2/4-\int_0^uK(v)\,dv.} \tag{8}
\]

Formula (8) identifies the complete signed integral with the endpoint
moment functional; it is not an independently smaller error. If only
$|K|\le a$ and $|\delta(0)|\le b_0$ are retained, then

\[
|\delta(u)|\le B_{\rm int}(u):=b_0+\int_0^u a(v)\,dv. \tag{9}
\]

The separate positive terms in Section 6 `rt:gap-error-bound` are one
possible $a$, with all their denominator and center payments. A bound
on the joint quotient alone is not an admissible replacement for (5).

## 5. Holomorphic multiplicative errors are invisible to the endpoint

Let $G$ be holomorphic and nonvanishing on a neighborhood of the closed
disk. A holomorphic logarithm $g=\log G$ exists there because the disk
is simply connected. Replacing $H$ by $GH$ changes any compatible
collar logarithm by $g+2\pi i k$, for an integer constant $k$. Cauchy's
theorem gives

\[
\langle g+2\pi i k\rangle=
\langle(z-c_P)(g+2\pi i k)\rangle=0. \tag{10}
\]

Thus both $I_0,I_1$, and the complete endpoint error in (3), are
unchanged. In particular $H=GP$ gives $I_0=I_1=\delta=0$, even for
spatially nonconstant $G$. Equivalently, the endpoint only sees the
$(z-X)^{-1}$ and $(z-X)^{-2}$ Laurent coefficients of the collar
logarithm: if these are $a_{-1},a_{-2}$, then

\[
I_0=a_{-1},\quad I_1=a_{-2}+(X-c_P)a_{-1},\quad
\delta=-a_{-2}-(X-c_P)a_{-1}-a_{-1}^2/4.
\]

This characterizes the invisible linear subspace for the two moments;
moment invisibility does not require full holomorphic extendibility.
Vanishing discriminant error alone is weaker still, since a nonzero
center error may cancel the centered second moment in (3). A factor
with interior zeros, poles or a nontrivial winding logarithm is outside
the stated gauge cancellation.

This endpoint invariance is stronger than cancellation in $Q$. If
$H=GP$, then

\[
Q=2\frac{G_z}{G}\frac{P_z}P+\frac{G_{zz}}G,
\]

which need not vanish. For the time identity $H=GP$ must also satisfy
the unchanged heat law. This imposes

\[
\frac{G_t}{G}+2\frac{G_z}{G}\frac{P_z}P
+\frac{G_{zz}}G+\frac RP=0. \tag{11}
\]

Now $c_H=c_P$ and the integrand in (5) becomes
$-(z-c_P)G_t/G$, holomorphic in the disk, so $K=0$. Cancellation
is between the full quotient and reference defect. An arbitrary chosen
$G(u,z)$ is not a new admissible physical heat path. Gauge invariance
does not permit removing the defect, changing $P_N$, or propagating
a normalized error with the plain heat equation.

## 6. Matched comparison and what it does not exclude

For the **same exact admissible path**, reference and anchor, (8) proves
equality of the endpoint and complete integrated readouts on each slice.
For the same full feasible set of uncertain paths, their exact extrema
also agree. There is no strict gain from changing between these exact
representations. This assertion does not identify a slice-only log box
with a feasible set retaining initial anchors, boundary data and time
correlations.

In particular, no universal inequality between (4) and (9) follows.
An informative anchor and a correlated bound on the complete signed
integral can improve a raw endpoint value envelope. Conversely (9) can
be larger after signs and correlations are discarded. A direct comparator
must receive every such anchor, time constraint and residual propagated
by module B, and may impose (8), evaluate (3), or intersect the resulting
valid bounds. A sufficient, explicitly checkable improvement over the
**raw value allowance** is

\[
b_0+\int_0^u a(v)\,dv<B_{\rm end,raw}(u), \tag{12}
\]

provided the integrated bound is complete. A smaller propagated endpoint
error $q_{\rm prop}<q_{\rm raw}<1$ also strictly decreases (4) at fixed
reference and geometry, because its right side is strictly increasing
in $L=-\log(1-q)$. This is improved residual acquisition shared by the
direct comparator; it is not recursive superiority or new coverage.
No instance of either sufficient inequality has been acquired here.

For actual continuation one needs, at **every** $u\in[0,U]$, the counts,
conjugation symmetry, cleared contour and a complete lower bound

\[
D_P(u)-B(u)>0, \tag{13}
\]

where $B$ is a valid complete discriminant allowance, with reference
uncertainty included. An exact endpoint lower bound at $U$ does not
protect the intervening path. Multiple valid slice allowances may be
intersected; phase-sensitive one-sided use of (3) may improve the symmetric
absolute bound, but is not supplied by an unsigned $q$ alone.

## 7. Analytical collision-control screen

These checks test premises; they are not numerical replays. For the
zero-error control, choose $0<U<r^2/2$ and the local exact backward-heat
field

\[
H(u,z)=P(u,z)=(z-X)^2+2(u-U).
\]

This auxiliary control does not replace the frozen arithmetic reference.
It has $E=R=0$, $q=0$, count two and contour clearance throughout
$[0,U]$, but $D_H=D_P=2(U-u)$. Both readouts give zero transfer error
and leave the merger at $U$ intact. The failed premise is exactly the
strict reference margin (13), since $D_P(U)=0$. Perfect approximation
is not a gap floor.

The Cluster 12 screen for the remaining relevant classes is as follows.
For any physical colliding field admitting a cleared count-two contour
near its double event, taking the exact field as an auxiliary reference
again makes every approximation payment zero. At the event (13) fails.
More generally, if a valid symmetric transfer allowance applies at that
event, $D_H=0$ implies $D_P\le|D_P|=|\delta|\le B$, so strict (13)
is impossible. No purported numerical margin for the frozen $P_N$ is
being asserted or refuted by this argument.

| Cluster 12 class | Premise that is missing or must fail at its witness |
| --- | --- |
| Euler-factor controls | Source positivity and preserved real zeros at time zero do not acquire the complete whole-time discriminant margin (13); a valid local count-two application cannot make it positive at a merger. |
| Weighted-square and finite-square-source controls | Support, endpoint and moment inequalities do not pay (13). In addition, their documented absence of any all-real heat time blocks importing a global all-real anchor. Their event time is not such an anchor. |
| Reflected super-Gaussian controls | Reflection, endpoint and Gram positivity do not pay (13), which fails at the exact double event. No order-one product assumption is used in (3)–(8), so failure of that separate global input is not a rejection by this local identity. |
| Smooth-shape and positive-primitive controls | Positivity of a primitive and matching asymptotic coefficients do not supply the strict local discriminant margin; it fails at their event. |
| Finite-source measurement and finite-prime orbit controls | Matching the retained finite measurements does not acquire the time-uniform height-dependent margin. At an isolated double event (13) fails; neither escaping event heights nor finite data imply a fixed-compact obstruction. |
| Atomic, fixed-event and exact finite-profile threshold controls | Selected profile values and uniform complete upper moments do not supply (13); it fails at the event. A contour containing more than two zero occurrences fails the count-two gate and is not silently treated as a two-zero divisor. |
| RH-conditional normalized endpoint controls | A fixed positive source-distance tolerance does not acquire a height-dependent discriminant margin at their escaping time-zero doubles. Their RH assumption and the frozen positive-time cell prevent treating them as an unconditional fixed-cell counterexample. |
| Fixed theta amplitude with changed observation kernel | The physical cosine/Newman heat equation is not retained. Its nonzero prepared residual must be paid before (7)–(8) applies; zero raw source mismatch is not zero complete forcing. |

Reflection rigidity is a classification statement, not a further collision
witness. Fractional divisor profiles fail the integer count-two premise;
static divisor surgery has no common source heat path for (7); neither is
silently included in the physical-path comparison. Polynomial and strong
collar controls still test (3) and its full square. The failure statements
here concern these local information and estimating classes only. They
do not exclude arithmetic phase estimates using the unchanged complete
theta source.

## 8. E11 handoff and correction record

E11 must attach the actual published physical source value budget and
finite defect for this same $P_N$; count/denominator/center/reference-gap
enclosures; initial and lateral residual data required by module B; and
all quadrature, source, time and parameter errors. It should compare the
complete all-time lower bounds from (3), (4), (6) and any retained signed
correlations, giving the direct comparator identical propagated information.
Gauge directions may be projected out before bounding only when that
projection is itself paid. No replacement equation or correction center
is authorized by this note.

One derivation and one correction pass were used. The correction pass
checked: the factor $1/4$ and complex square in (3); the moving-center
term and backward sign in (7)–(8); the circle factor in (4); the defect
compatibility in (11); and comparison scopes with retained anchors/time
correlations. No computational experiment or source certificate is claimed.
