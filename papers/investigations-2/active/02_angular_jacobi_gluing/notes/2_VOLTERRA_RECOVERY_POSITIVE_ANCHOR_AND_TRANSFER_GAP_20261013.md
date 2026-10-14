# Volterra recovery, a positive correction anchor, and the transfer gap

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort **ultra**, inherited
from the parent session. This is an incremental analytic continuation, not
a manuscript or independent mathematical validation.

This develops the [complete short-period identity](ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md)
after the [09 two-coset reduction](../../../inactive/09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md)
and the [06 factorization obstruction](../../06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md).
All identities below are derived from those exact sources. No external
positivity theorem is assumed.

**New result.** The correction removed from the short-period channel has a
strictly positive real Fourier transform throughout \(0\le t\le1\).
An elementary bound is
\[
 \boxed{P_t(x)>\frac{1}{3000(1+x^2)},\qquad
              0\le t\le1,\quad x\in\mathbb R.}
 \tag{1}
\]
The proof includes the infinite source and requires no sampled sign.
The actual physical recovery is still \(H_t=A_t+P_t\). The positive anchor
does not prohibit cancellation with \(A_t\). In fact that cancellation is
forced to all algebraic orders at large real frequency. This note gives
the exact Volterra recovery and boundary ledger, a stable source-norm
estimate, and the precise remaining observation inequality.

## 1. Exact source recovery

On \(u\ge0\), write
\[
 \Phi(u)=\sum_{n\ge1}
   (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \qquad
 R(u)=2\pi^2e^u\sum_{n\ge1}n^2e^{-\pi n^2e^{4u}}.
 \tag{2}
\]
The preceding calculation identifies the short-period source as
\(a(u)=\Phi(u)-R(u)\), even-reflected after this definition. Every term
in \(R\) is positive. Direct differentiation gives
\[
 \boxed{R'(u)+5R(u)=-4\pi e^{-4u}\Phi(u),\qquad
 \Phi(u)=-\frac{e^{4u}}{4\pi}(R'+5R).}
 \tag{3}
\]
The upper boundary \(e^{5u}R(u)\) tends to zero by the theta tail, so
\[
 \boxed{R(u)=4\pi e^{-5u}\int_u^\infty e^v\Phi(v)\,dv.}
 \tag{4}
\]
The factor \(4\pi\), the weight \(e^v\), and the endpoint at infinity
are all required.

There is also a closed inverse recovering \(\Phi\) from the full signed
short-period source \(a\). Substitute \(\Phi=a+R\) in (3) and use the
integrating factor \(\exp(5u-\pi e^{-4u})\):
\[
 \boxed{
 R(u)=4\pi e^{-5u+\pi e^{-4u}}
       \int_u^\infty e^{v-\pi e^{-4v}}a(v)\,dv,\qquad
 \Phi(u)=a(u)+R(u).}
 \tag{5}
\]
The signed integral in (5) is positive for the genuine prepared \(a\),
but positivity of arbitrary \(a\) is not asserted; the earlier note proves
\(a(0)<-1/10\).

For a finite cutoff \(L\ge u\), the boundary payments are respectively
\[
 R(u)=e^{5(L-u)}R(L)
       +4\pi e^{-5u}\int_u^L e^v\Phi(v)\,dv,
 \tag{6}
\]
\[
 R(u)=e^{5(L-u)+\pi(e^{-4u}-e^{-4L})}R(L)
       +4\pi e^{-5u+\pi e^{-4u}}
           \int_u^L e^{v-\pi e^{-4v}}a(v)\,dv.
 \tag{7}
\]
Deleting these terms before taking the paid infinite-source limit would
change the recovered source.

## 2. Entire heat and spectral transport

Use distinct notation for the half-line transforms:
\[
 G_t(x)=\int_0^\infty e^{tu^2+ixu}\Phi(u)\,du,\qquad
 Q_t(x)=\int_0^\infty e^{tu^2+ixu}R(u)\,du.
 \tag{8}
\]
For real \(t,x\), the physical and correction cosine transforms are
\[
 H_t(x)=\operatorname{Re}G_t(x),\quad
 P_t(x)=\operatorname{Re}Q_t(x),\quad
 A_t(x)=H_t(x)-P_t(x).
 \tag{9}
\]
Their entire extensions use the cosine integrals themselves; the
real-part notation in (9) is restricted to real parameters.
All source terms decay faster than every fixed Gaussian, so these
transforms are entire in \((t,x)\), including all fixed derivatives.
Each obeys \(\partial_t=-\partial_x^2\).

Substitution of (4) and an absolutely justified order exchange gives
\[
 \boxed{
 Q_t(x)=4\pi\int_0^\infty e^v\Phi(v)
              \left(\int_0^v e^{tu^2+(ix-5)u}\,du\right)dv.}
 \tag{10}
\]
On any compact complex parameter set the inner integral is bounded by
\(v\exp(Tv^2+(X+5)v)\), and the complete theta tail absorbs that
factor. Thus (10) does not use a divergent raw negative-half-line
theta integral.

Integration of (3), with its boundary at zero, yields the exact spectral
differential relation
\[
 \boxed{(5-ix+2it\partial_x)Q_t(x)
           =R(0)-4\pi G_t(x+4i).}
 \tag{11}
\]
Equivalently,
\[
 4\pi G_t(x)=R(0)-(1-ix)Q_t(x-4i)
                         -2it\,\partial_xQ_t(x-4i).
 \tag{12}
\]
Every shifted channel in (11)--(12) is the defining entire half-line
transform, with a paid theta tail. No small unshifted approximation disk
is used to justify a fixed shift by \(4i\).

For the cutoff transforms in (8) restricted to \([0,L]\), (11) becomes
\[
 (5-ix+2it\partial_x)Q_t^{[L]}(x)
   =R(0)-e^{tL^2+ixL}R(L)-4\pi G_t^{[L]}(x+4i).
 \tag{13}
\]
The sign of the upper boundary is negative. The limit of that term is
zero, uniformly on compact parameter sets. The lower boundary \(R(0)\)
does not vanish. For example, at \(t=0\),
\[
 Q_0(x)=\frac{R(0)-4\pi G_0(x+4i)}{5-ix}.
 \tag{14}
\]
The apparent pole at \(x=-5i\) is removable: (4) at \(u=0\) gives
\(R(0)=4\pi G_0(-i)\), exactly the numerator value there.

Equations (10)--(14) show explicitly that the correction is a scalar
Volterra observation of the complete physical source. Its elliptic origin
does not make it independently selectable after that source is fixed.

## 3. A bounded and stable full-source inverse

This section records a genuine source-norm estimate and its scope.
For real \(t\ge0\), let
\[
 f_t(u)=e^{tu^2}\Phi(u),\quad r_t(u)=e^{tu^2}R(u),\quad
 a_t(u)=e^{tu^2}a(u).
\]
The heated Volterra kernel from (4) is
\[
 (V_tf)(u)=4\pi\int_u^\infty
   e^{t(u^2-v^2)-5u+v}f(v)\,dv.
 \tag{15}
\]
Thus \(r_t=V_tf_t\) and \(a_t=(I-V_t)f_t\). Its inverse is
\((I-V_t)^{-1}=I+W_t\), where the kernel of \(W_t\) is the kernel in
(15) multiplied by
\(\exp\{\pi(e^{-4u}-e^{-4v})\}\), as (5) proves directly.

For \(U\ge0\), put
\[
 \|f\|_{1,U}=\int_U^\infty e^u|f(u)|\,du.
\]
On \(u\le v\), the heat factor in (15) is at most one. Fubini applied to
absolute values gives
\[
 \|V_t\|_{1,U\to1,U}\le\pi e^{-4U},\qquad
 \|W_t\|_{1,U\to1,U}\le e^{\pi e^{-4U}}-1.
 \tag{16}
\]
For the second estimate the exact inner integral is
\[
 4\pi\int_U^v e^{-4u}
       e^{\pi(e^{-4u}-e^{-4v})}\,du
   =e^{\pi(e^{-4U}-e^{-4v})}-1.
\]
Consequently,
\[
 \boxed{
 e^{-\pi e^{-4U}}\|f_t\|_{1,U}
 \le\|a_t\|_{1,U}
 \le(1+\pi e^{-4U})\|f_t\|_{1,U}.}
 \tag{17}
\]
The inverse bound is valid even when the elementary norm of \(V_t\)
exceeds one: (5) supplies the convergent Volterra resolvent directly.
This establishes stable recovery of the full source in the stated weighted
norm. It is not a lower bound for a Fourier value, a slope, or a stationary
product; absolute source norms do not prevent Fourier cancellation.

## 4. The correction has a strictly positive Fourier observation

For \(0\le t\le1\) and \(n\ge1\), put
\[
 r_{n,t}(u)=2\pi^2n^2e^{tu^2+u-\pi n^2e^{4u}},
 \quad E=e^{4u},\quad q=\pi n^2E,\quad
 \ell'_{n,t}=1+2tu-4q.
\]
On \(u\ge0\), \(1+2tu\le E\), so
\[
 \ell'_{n,t}\le-(4\pi n^2-1)E<0.
\]
Furthermore
\[
 \frac{r_{n,t}''}{r_{n,t}}
   =(\ell'_{n,t})^2+2t-16q
   \ge E\{(4\pi n^2-1)^2-16\pi n^2\}>0.
 \tag{18}
\]
For the last inequality, \(b=\pi n^2>3\) and
\((4b-1)^2-16b=16b^2-24b+1>73\). Hence the complete
\(r_t=\sum_n r_{n,t}\) is strictly decreasing and strictly convex on the
whole half-line. Its differentiated sum and all integrals below converge
absolutely by the theta tail.

Twice integrating by parts gives, for real \(x\ne0\),
\[
 \boxed{
 P_t(x)=\frac1{x^2}\int_0^\infty
                   r_t''(u)(1-\cos(xu))\,du>0.}
 \tag{19}
\]
Indeed \(\int_0^\infty r_t''=-r_t'(0)\); the endpoint term is exactly
what converts the first integration-by-parts expression into (19).
For \(x=0\), the positive defining integral supplies strict positivity.
The sign in (19) is about the complete cosine observation, not just a
positive source.

There is a simple fully explicit lower bound. Set \(\delta=1/10\).
For \(0\le u\le\delta\), the \(n=1\) term alone in (18) yields
\[
 r_t''(u)\ge
 2\pi^2\{(4\pi-1)^2-16\pi\}
                       e^{-\pi e^{2/5}}>5.
 \tag{20}
\]
The elementary constants suffice: \(\pi>3\) makes the prefactor greater
than \(18\cdot73=1314\). Also
\[
 e^{2/5}<1+\frac25+
        \frac{(2/5)^2/2}{1-(2/5)/3}
       =\frac{97}{65}<\frac32,\qquad
 \pi e^{2/5}<\frac{33}{7}<5,\qquad e^5<3^5=243.
\]
Thus the last quantity in (20) exceeds
\(1314/243=146/27>5\).

Equations (19)--(20) imply
\[
 P_t(x)>\frac5{x^2}
           \left(\frac1{10}-\frac{\sin(x/10)}x\right).
 \tag{21}
\]
For \(|x|\le20\), use
\(1-\cos y\ge2y^2/\pi^2\) on \(|y|\le\pi\), which follows from the
concavity of sine on \([0,\pi/2]\). Since \(\pi^2<10\),
\[
 P_t(x)>\frac{2\cdot5\delta^3}{3\pi^2}>
              \frac1{3000}.
 \tag{22}
\]
This also holds at zero by continuity or by the limiting integral.
For \(|x|\ge20\), (21) instead gives
\[
 P_t(x)\ge\frac{5\delta}{2x^2}=\frac1{4x^2}.
 \tag{23}
\]
Together these establish (1). The bound is intentionally conservative;
it is an all-frequency analytic anchor, not a numerical optimization.

At \(t=0\), combining this new sign with (14) also gives a concrete
inequality for a shifted physical half-line channel:
\[
 5R(0)-20\pi\operatorname{Re}G_0(x+4i)
       +4\pi x\operatorname{Im}G_0(x+4i)
  >\frac{25+x^2}{3000(1+x^2)}.
 \tag{24}
\]
This is an actual signed nonlocal relation. Its spectral shift and its
boundary term are essential. It is not the unshifted stationary product.

## 5. Why this anchor still does not transfer to the physical pair

The slope in (3) fixes the positive constant
\[
 d=-R'(0)=5R(0)+4\pi\Phi(0)>0.
 \tag{25}
\]
Repeated half-line integration by parts, including the endpoint, gives
\[
 P_t^{(k)}(x)=
 \frac{(-1)^k(k+1)!d}{x^{k+2}}+O_{T,k}(x^{-k-4})
 \quad(x\to+\infty).
 \tag{26}
\]
Here \(t\) ranges over a compact real interval, and each derivative
asymptotic follows from its own differentiated integral. The full
physical \(H_t\) and every fixed spatial derivative are Schwartz on the
real frequency line. Therefore
\[
 A_t^{(k)}(x)=
 -\frac{(-1)^k(k+1)!d}{x^{k+2}}+O_{T,k}(x^{-k-4}),
 \qquad H_t=A_t+P_t.
 \tag{27}
\]
All algebraic endpoint contributions cancel in the physical sum.
This is the same obstruction exposed by the folded parity channels in 06,
now with a genuinely positive correction transform.

In particular, for every fixed \(t\in[0,1]\), \(\sigma>0\), and \(N\ge0\),
\[
 x^N\frac{H_t(x)^2+\sigma^2H_{t,x}(x)^2}{P_t(x)^2}\longrightarrow0.
 \tag{28}
\]
Thus no strictly positive constant, or polynomially decaying lower
factor in height, can transfer the anchor (1) uniformly to the complete
physical pair. Such a proposed transfer would be false even if every
physical zero were simple.

There is a related distinction from the paired factorization target.
For \(L_j(f)=(f^{(j+1)})^2-f^{(j)}f^{(j+2)}\), (26) yields
\[
 L_j(P_t)=
 -\frac{(j+1)!(j+2)!d^2}{x^{2j+6}}
       +O_{T,j}(x^{-2j-8}),\qquad j=0,1.
 \tag{29}
\]
So even this everywhere positive correction transform has negative
Laguerre responses at large real frequency. It cannot serve as an
independently positive paired block. Equation (29) says nothing adverse
about the signs of the complete physical \(L_j(H_t)\).

Because \(P_t>0\), one can state the remaining collision-observation gap
without a singular denominator. Put
\[
 b_t=\frac{P_{t,x}}{P_t},\qquad
 \alpha_t=\frac{A_t}{P_t},\qquad H_t=P_t(1+\alpha_t).
\]
Then the exact complete pair is
\[
 \left(\frac{H_t}{P_t},\frac{H_{t,x}}{P_t}\right)
 =\big(1+\alpha_t,\,
       \partial_x\alpha_t+b_t(1+\alpha_t)\big).
 \tag{30}
\]
A physical joint zero is exactly
\(\alpha_t=-1,\ \partial_x\alpha_t=0\). On a specified compact rectangle
\(\mathcal R\), a usable transfer would prove
\[
 \boxed{
 |1+\alpha_t(x)|^2+
 \sigma^2|\partial_x\alpha_t(x)+b_t(x)(1+\alpha_t(x))|^2
       \ge\varepsilon_{\mathcal R}>0.}
 \tag{31}
\]
Then (1) would give a paid physical lower bound on that rectangle.
Nothing in (3), (5), the source-norm estimate (17), or convexity (18)
proves (31). Simply minimizing its true left side is still the original
physical residual calculation in a different normalization.

The evolution likewise preserves this limitation:
\[
 \partial_t\alpha_t
 =-\partial_x^2\alpha_t-2b_t\,\partial_x\alpha_t.
 \tag{32}
\]
This follows because both \(A_t\) and \(P_t\) obey backward heat.
A positive gauge supplies a regular drift equation; it does not supply
a forward-time maximum principle excluding the stationary level
\(\alpha=-1\). By (28), this level and its derivative are approached
faster than any inverse polynomial at high frequency, regardless of
whether an exact joint zero exists.

## 6. Reproduction and a failed direct-dominance inequality

The [continuation checker](../numerics/check_complete_angular_channels.py)
and [small record](../numerics/COMPLETE_ANGULAR_CHANNELS_RECORD_20261013.json)
replay the exact constants used in (18)--(23), diagnostic Volterra and
spectral identities, and a separate outward-arithmetic Fourier witness.
The latter retains terms \(n=1,2,3\), uses 512 Simpson panels on \([0,1]\),
encloses the fourth-derivative quadrature remainders, and pays all omitted
theta and source tails. At \(t=0,x=32\), its complete intervals imply
the following outward-rounded bounds:
\[
 -9.60881\cdot10^{-5}<H_0(32)<-9.60862\cdot10^{-5},
 \qquad
 0.0096466403<P_0(32)<0.0096466430,
\]
\[
 1.0099603<\frac{|A_0(32)|}{P_0(32)}<1.0099611.
 \tag{33}
\]
This disproves a proposed global transfer by \(|A_t|\le P_t\), and hence
also by strict relative dominance \(|A_t|\le(1-\delta)P_t\) with
\(\delta>0\). Continuity makes the strict signs persist for some
positive-time interval; this observation does not certify its radius.
No stationarity is asserted at this witness, so it does not refute the
physical stationary signs or the collision-observation condition (31).
The numerical witness and the all-frequency analytic positivity proof
have different jobs and neither is substituted for the other.

## 7. Decision gate

The correction now passes a genuine global sign test: (1), (19), and
(24) are established inequalities with their source and boundary terms
retained. This improves the earlier state of 02, which had only an exact
identity and an obstruction to positivity of the inserted shifted source.
Equations (4)--(17) also give exact and stable recovery of that complete
source.

The next missing input is a source-specific cancellation estimate such as
(31) on a declared domain, with a normalization that can pay the
superalgebraic cancellation in (28), or a new identity controlling the
physical stationary products after recombination. The positive correction
alone does not meet that requirement. A uniform polynomial-scale transfer
from this particular anchor is disproved by (28), so that version should
not be proposed for another numerical search.

The analytic inequalities here do not depend on a finite theta truncation,
a sampled Fourier sign, or a presumed stationary point. The separate
bounded witness (33) includes explicit truncation and quadrature payments.
No uniform stationary sign, joint-zero exclusion on a new
rectangle, or RH conclusion is claimed.
