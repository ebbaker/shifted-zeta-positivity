# A uniform height three floor for large conductor characters

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
**Status: proved in-note with an Arb certificate of the scalar envelope;
internal same-model checks only.** Independent specialist review remains
outstanding.

For every primitive Dirichlet character of conductor \(q\ge10^{12}\), in
Project 01's normalization, this note proves

\[
 S_\chi(x,3,t)=-\Im\frac{H'_{\chi,t}}{H_{\chi,t}}(x+3i)>6
 \quad(x\in\mathbb R,\ 0\le t\le1/4).                         \tag{1}
\]

The [restarted comparison in Note 02](02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md)
then gives \(\Lambda_\chi\le43/200=0.215\). The computation certifies
one useful regime of the transport remainder, including every time and
height and every larger conductor. It does not certify the original
near-threshold zero-loss tables or the vertical derivative on a Cauchy circle.

The analytical inputs are Proposition 4.5 and the saddle/transport lemmas
of [round-one Note 01](../round-1/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md),
with the errata and saddle-domain correction in the
[current manuscript](../../manuscript/height_p_transport.tex) and
[Review 01](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CODEX_20261017.md).
The scalar [program](../../numerics/round-2/family_floor_gate_arb_20261017.py)
and [record](../../numerics/round-2/FAMILY_FLOOR_GATE_ARB_20261017.json)
use python-flint 0.9.0 at 128 bits. No quadrature, floating-point sign
decision or parameter sampling is used. The mathematical domination and
monotonicity proved below are necessary parts of the certificate.

## 1. Parameters and transport budget

Write
\[
 h=\tau^2=t/2,\quad L=129/5,\quad 0<h\le1/8,\quad
 \ell=\ell_*\ge L,\quad \sigma=\sigma_*=2+h\ell/2.
\]
The real part of the height-three evaluation point is \(\sigma_0=2\).
The saddle lemma is applied on \([\sigma_0,\infty)\) for the real saddle;
it does not claim uniqueness on the whole real domain of the digamma.
Choose a cutoff separately at each point:
\[
 a=(\sigma+1)/2,\qquad V=(\sigma-1)/2,
 \qquad \sigma-V=a\ge3/2>1.
\]
Define the positive decreasing functions
\[
 \kappa(s)=-\zeta'(s)/\zeta(s),\quad K_2(s)=-\kappa'(s),\quad
 K_3(s)=\kappa''(s),\quad
 A_1(s)=\psi'(s/2)/4,\quad A_2(s)=-\psi''(s/2)/8,
\]
\[
 k(s)=K_2(s)+A_1(s),\qquad j(s)=K_3(s)+A_2(s).
\]
Their positivity and monotonicity follow from their Dirichlet or
polygamma series. The even Gamma majorants dominate the odd ones, so
one enclosure handles both parities at every imaginary part of the saddle.
The certificate checks
\(\kappa(2)<57/100\), \(\zeta(2)<33/20\), and
\(\zeta(5/4)<5\).

With \(M_\rho,B_V,P_1,D_L,N_L,P_2\) as in Proposition 4.5, put
\[
 d_0=e^{-h\kappa(\sigma)^2/2}-P_1-P_2.
\]
That proposition bounds the logarithmic-derivative remainder by
\[
 E=\frac{hk(\sigma)\kappa(\sigma)}{1-hk(\sigma)}+
 \frac{M_\rho+B_V+hk(\sigma)\kappa(\sigma)D_L+
       (1+hk(\sigma))N_L}{(1-hk(\sigma))d_0}.                 \tag{2}
\]
We give upper bounds for every numerator payment and a positive lower
bound for the denominator. Thus the use of (2) does not assume a
positive real Gaussian weight for the complex completed function.

## 2. Moments on the Euler product region

For \(c,b\ge0\), \(d=1-hb>0\), and \(z=c\sqrt{h/d}\), set
\[
 M_2(h,c,b)=\frac{h}{d^{3/2}}
 \left[(1+z^2)e^{z^2/2}\left(1+\frac45z\right)+\frac45z\right].
\]
If \(X\) is normal with variance \(h\), then
\[
 \mathbb E[X^2 e^{c|X|+bX^2/2}]\le M_2(h,c,b).              \tag{3}
\]
Indeed the exact expression has bracket
\(2(1+z^2)e^{z^2/2}\Phi(z)+\sqrt{2/\pi}\,z\), where \(\Phi\)
is the standard normal distribution function. Use
\(2\Phi(z)\le1+\sqrt{2/\pi}\,z\le1+(4/5)z\).
The displayed positive expression for \(M_2\) increases in \(h,c,b\).

On \(v\ge-V\), all real parts on the Taylor segment are at least \(a\).
The Euler and Gamma majorants give
\[
 r(v)\le j(a)v^2/2,\quad
 g(v)\le e^{\kappa(a)|v|+A_1(a)v^2/2},\quad
 \omega_m(v)\le k(a)v^2/2.
\]
Extend the nonnegative integrals to the whole line, and use
\(e^y-1\le ye^y\) for \(y\ge0\). Then
\[
 M_\rho\le\tfrac12j(a)M_2(h,\kappa(a),A_1(a)),\qquad
 P_1\le\tfrac12k(a)M_2(h,\kappa(\sigma),k(a)).             \tag{4}
\]
Every coefficient decreases with \(\ell\), so at fixed \(h\) it is
bounded by its value at \(\ell=L\). The moving cutoff is harmless:
the nonnegative integral at each parameter point has separately been
extended to the full line.

For the boundary payment,
\[
 B_V\le\frac{\exp(\kappa(a)V+A_1(a)V^2/2-V^2/(2h))}
                 {\sqrt{2\pi h}}.                       \tag{5}
\]
On a cell \([h_-,h_+]\), define
\(\sigma_-=2+Lh_-/2\), \(a_-=(\sigma_-+1)/2\),
\(V_-=(\sigma_--1)/2\). The certificate checks
\[
 (1/h_+-A_1(a_-))V_->\kappa(a_-),\qquad V_-^2>h_+.
\]
After replacing the coefficients by their values at \(a_-\), the first
inequality makes (5) decrease in \(V\ge V_-\); the second makes its
Gaussian density increase in \(h\le h_+\). Hence evaluation at
\((V_-,h_+)\) bounds the entire cell and every \(\ell\ge L\).

## 3. The ordinary left tail above 5/4

Put \(u=\sigma+v\). On \(5/4\le u<a\), the Euler product gives
\[
 |L(u+iT,\chi)/L(s_*,\chi)|\le(33/20)5=33/4=:C.
\]
The polygamma series and integral test give
\[
 A_1(u)\le\frac1{2u}+\frac1{u^2}\le26/25=:b.
\]
Thus the Gamma Taylor remainder satisfies \(\vartheta(v)\le bv^2/2\).
For \(d=1-bh\), extending to the entire half-line \(v<-V\) gives
\[
 D_{\rm mid}\le\frac C{\sqrt d}\Phi(-V\sqrt{d/h}),
\]
\[
 N_{\rm mid}\le C\left[
 \frac{e^{-dV^2/(2h)}}{d\sqrt{2\pi h}}+
 \frac{\kappa(\sigma)}{\sqrt d}\Phi(-V\sqrt{d/h})\right]. \tag{6}
\]
These expressions decrease in \(V\) and increase in \(\kappa(\sigma)\),
so the same lower \(\sigma\) endpoint applies. They increase in \(h\)
on each cell: for the first moment use \(V_-^2>h_+\), and the other
factors have the required monotonicity directly.

The pure-tilt contribution to \(P_2\) is
\[
 J=e^{h\kappa(\sigma)^2/2}
   \Phi((h\kappa(\sigma)-V)/\sqrt h),\qquad P_2\le D_L+J. \tag{7}
\]
It increases in \(h\) and \(\kappa(\sigma)\) and decreases in \(V\).

## 4. Both critical intervals

The ordinary and reflected critical tails have reflected or ordinary
real part \(1/2\le u\le5/4\). Proposition 4.5's height proxy is
\(\mathcal Q=2\pi e^{\ell+c_*}\), with
\[
 c_*\le1/\sigma+1/(3\sigma^2)\le7/12.
\]
Choose \(N=\lceil\mathcal Q/2\rceil\). The scalar inequality
\(\pi e^{7/12}+e^{-L}<e^2\), checked by the certificate, proves
\(\log N\le\ell+2\). The partial-summation bound therefore gives
\[
 Z(u)\le(\ell+5)e^{(1-u)_+(\ell+2)}.                     \tag{8}
\]
For \(u<1\), use \(\int_1^N x^{-u}dx\le\log(N)N^{1-u}\) and
tail \(N^{1-u}/u\le2N^{1-u}\); for \(u\ge1\), use the same
bounds with \(N^{1-u}\le1\).

Integrating \(A_1(s)\le1/(2s)+1/s^2\) with the Taylor weight yields
\[
 \vartheta(u-\sigma)\le\frac{\sigma-u}{2}
 +(1-u/2)\log(\sigma/u)+u/\sigma-1
 \le\sigma/2+\log(2\sigma).
\]
The ordinary critical density is consequently at most
\[
 \frac{(33/20)2\sigma(\ell+5)}{\sqrt{2\pi}}h^{-1/2}
 \exp\left(\frac\sigma2-\frac{(\sigma-u)^2}{2h}
                    +(1-u)_+(\ell+2)\right).             \tag{9}
\]
The numerator weight for either critical tail is at most
\((\sigma+1/4)/h+57/100\).

The full envelope, including that weight, decreases with \(\ell\).
Its polynomial prefactor has logarithmic derivative at most \(3/\ell\).
The exponent in (9) has derivative
\[
 -u/2-h(\ell-1)/4\le-1/4\quad(u\le1),
\]
\[
 -(2-u)/2-h(\ell-1)/4\le-3/8\quad(u\ge1).
\]
Since \(3/L<1/4\), replacement by \(\ell=L\) is justified even for
the numerator tail. Now \(\sigma\le S:=2+L/16=289/80\).

Set
\[
 R=\sqrt{L(L-2)},\quad C_*=(33/20)2S(L+5)/\sqrt{2\pi},
 \quad H_r(c)=(r/(ec))^r,
\]
\[
 Z_0=2-L/4-3\sqrt3 R/8,\quad c_0=1/8,\quad d_0^*=1/2,
\]
\[
 Z_1=1-3L/8-3\sqrt3 R/16,\quad c_1=9/128,\quad d_1^*=1/4.
\]
Here \(d_i^*\) are interval lengths, unrelated to the denominator \(d_0\).
For \(u\le1\), let \(y=1-u\in[0,1/2]\). The exponent in (9) is
\[
 1+2y-L(1-y)/2-(1+y)^2/(2h)-hL(L-2)/8.
\]
Reserve one quarter of the inverse-\(h\) payment, at least \(1/(8h)\),
and apply AM–GM to the rest and the \(h\) payment. The resulting
expression increases in \(y\), and at \(y=1/2\) equals \(Z_0\).
For \(u\ge1\), put \(d_u=2-u\in[3/4,1]\). The exponent is
\(1-d_uL/2-d_u^2/(2h)-hL(L-2)/8\). Reserving one quarter gives
\(9/(128h)\); AM–GM and \(d_u\ge3/4\) give \(Z_1\).
Finally \(h^{-r}e^{-c/h}\le H_r(c)\) for every \(h>0\).

At the same \(u\), the ratio of the reflected majorant density to the
ordinary one is exactly
\[
 \exp[-3(2u-1)/(2h)]\le1.                                \tag{10}
\]
The Gamma remainders and \(Z(u)\) agree; subtracting the two Gaussian
exponents and the reflection factor, using \(\sigma=2+h\ell/2\),
gives (10). Hence the combined ordinary and reflected critical costs obey
\[
 D_{\rm crit}\le2C_*\sum_{i=0}^1d_i^*e^{Z_i}H_{1/2}(c_i)<10^{-5},
\]
\[
 N_{\rm crit}\le2C_*\sum_{i=0}^1d_i^*e^{Z_i}
 [(S+1/4)H_{3/2}(c_i)+(57/100)H_{1/2}(c_i)]<1/2000.        \tag{11}
\]
The certificate obtains upper values below \(6.686\cdot10^{-6}\)
and \(0.000349931\). These bounds are uniform in both parameters.

## 5. The far reflected tail

For reflected real part \(u\ge5/4\), put \(w=u-\sigma\), and retain
\(C=33/4\), \(b=26/25\). Both endpoints of the Gamma Taylor segment
are at least \(5/4\). Completing the reflection square gives density
at most
\[
 C e^{-3\ell/2}\frac{\exp(-(w+3)^2/(2h)+bw^2/2)}{\sqrt{2\pi h}}. \tag{12}
\]
The Euler bound is used throughout this far tail, so no height proxy is
extended past its allowed real-part range.

Set \(d=1-bh\ge d_{\min}=87/100\). The whole-line mass of the
Gaussian factor in (12) is
\[
 Z(h)=d^{-1/2}e^{9b/(2d)}\le Z_{\max}:=d_{\min}^{-1/2}e^{9b/(2d_{\min})}.
\]
It follows that
\[
 D_{\rm far}\le CZ_{\max}e^{-3L/2}<2.991\cdot10^{-14}<10^{-10}.
\]
For \(x=w+3\), the normalized tilted normal has mean \(-3bh/d\)
and variance \(h/d\). The actual numerator weight is
\(x/h+\ell+\kappa(\sigma)>0\). Enlarge it to
\(|x|/h+\ell+57/100\), obtaining
\[
 N_{\rm far}\le CZ_{\max}e^{-3\ell/2}
 [\ell+57/100+3b/d_{\min}+1/\sqrt{hd_{\min}}].             \tag{13}
\]
The artificial small-\(h\) divergence in (13) is removed by three cases,
with \(h_0=1/100\).

1. If \(h\ge h_0\), replace \(1/\sqrt h\) by 10 and then \(\ell\)
   by \(L\). The exponentially weighted linear expression decreases
   for \(\ell\ge L\). The result is below \(1.217\cdot10^{-12}\).
2. If \(h<h_0\) and \(\ell\ge1/h\), replace \(1/\sqrt h\) by
   \(\sqrt\ell\). The resulting exponential times the sum of a linear
   term and a square root also decreases for \(\ell\ge L\), by direct
   differentiation. Its value at \(L\) is below \(1.059\cdot10^{-12}\).
3. If \(h<h_0\) and \(\ell<1/h\), the integration domain has
   \(x=u+1-h\ell/2\ge7/4=:A\). Expand the exponent in (12) and
   discard the negative term \(-3bx\). Bound the weight by
   \(x/h+1/h+57/100\). Gaussian integration and
   \(\int_A^\infty e^{-dx^2/(2h)}dx\le h e^{-dA^2/(2h)}/(dA)\)
   give the bound
   \[
   \frac{Ce^{9b/2-3L/2}}{(1-bh_0)\sqrt{2\pi h_0}}
   \left[1+\frac{1+(57/100)h_0}{A}\right]
   e^{-(1-bh_0)A^2/(2h_0)}<1.364\cdot10^{-79}.
   \]
   Taking \(h=h_0\) enlarges this expression because
   \(h^{-1/2}e^{-A^2/(2h)}\) increases for \(h\le h_0<A^2\),
   and its other enlarged factors also increase.

Thus \(N_{\rm far}<10^{-8}\) in every case, without leaving a gap near
\(h=0\) or at arbitrarily large \(\ell\).

## 6. Certificate and floor

Substitute (4)–(7), (11) and the far-tail payments into (2), with
\[
 D_L\le D_{\rm mid}+10^{-5}+10^{-10},\qquad
 N_L\le N_{\rm mid}+1/2000+10^{-8},\qquad P_2\le D_L+J.
\]
The program uses 1,000 rational intervals with endpoints
\(h_i=i/8000\). Every cell uses \(h_+\) and
\(\sigma_-=2+Lh_-/2\), as justified above. The first cell is
\((0,1/8000]\); it needs no evaluation at zero and leaves no omitted
small-time interval. All transcendental evaluations use Arb balls;
uncertain sign comparisons fail the program.

| Quantity | Certified rational bound | Largest or smallest computed enclosure, rounded outward |
| --- | --- | --- |
| \(hk(\sigma)\) | \(<1\) | \(<0.033447\) |
| \(d_0\) | \(>93/100\) | \(>0.931777\) |
| \(E\) | \(<1/5\) | \(<0.192767\) |

The row for \(E\) is assembled on each cell; it is not formed by
combining separately located extrema. The record gives the auxiliary
payments and extremizing cell indices. The analytic bounds reduce the
unbounded height and conductor domain to these finite intervals.

For \(q\ge10^{12}\), the time-zero saddle parameter satisfies
\[
 \ell_0\ge\log(10^{12}/\pi)+\psi(1)>25.8.
\]
The lower value is certified as greater than \(25.909075565\), and the
saddle lemma gives \(\ell_*\ge\ell_0\) at every real height. Therefore
\[
 S_\chi(x,3,t)\ge\ell_*/4-\kappa(\sigma_*)/2-E/2
 >\frac{129}{20}-\frac{57}{200}-\frac1{10}
 =\frac{1213}{200}>6.
\]
At \(t=0\), the exact Euler-product floor omits the remainder payment
and is stronger. This proves (1) on the entire closed time interval.

## 7. Controls and the next decision

This is a quantitative sufficient estimate, in the terminology of
[avoid 01](../../../../../avoid/01_restating_the_target.md), with the
numerical consumer supplied by Note 02. It is not an RH-equivalent
reformulation. The work follows the
[result summaries](../../../../../result-summaries/README.md) and
[patterns to avoid](../../../../../avoid/README.md), specifically the
[heat-flow summary](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[uniformity and status caution](../../../../../avoid/06_status_stronger_than_the_evidence.md)
and [import caution](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

The [documented collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
are screened by their premises. The Euler-factor control with \(c=1/2\)
inserts \(1+4\sqrt{\mathfrak p}\,\mathfrak p^{-s}+\mathfrak p^{1-2s}\);
its logarithmic coefficient at \(\mathfrak p\) violates the zeta
majorant used here. The weighted-square, reflected super-Gaussian,
smooth shape and positive-primitive controls lack the specified
primitive-character Euler product and character partial-sum bounds.
The older Bessel and polynomial counter-kernels likewise do not have
these arithmetic inputs. No claim about their actual floors is inferred
from their positivity, symmetry or endpoint data. This is a premise
screen, not a new collision computation or a universal exclusion of
other methods.

The next review should check the analytic domination and restarted
comparison, not merely rerun the scalar programs. Lowering the conductor
threshold or certifying the derivative-circle consumer is separate work.
The zeta \(0.18891\) table keeps its existing conditional status.
