# Gevrey logarithmic tapers: complete approximation and a quantitative rate

20 October 2026. Prepared for Edward Baker with substantial LLM assistance.
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

**Outcome, proved in-note under RH.** For each fixed normalized compact
Gevrey extension of order \(1<\sigma<2\), the original tapered Möbius
polynomial has complete squared error
\[
 E_{N,w}\ll_{W,B}\frac{(\log\log N)^B}{\log N},
 \qquad B>1+2\sigma.
\]
The proof bounds the actual norm at all heights. It assumes neither
simplicity nor inverse derivative moments. The extra logarithmic factor
leaves room for multiple zeros. RH ⇒ simplicity remains unproved.

The separate fixed-height asymptotic and summability of its limiting
profile masses are proved in §§8–9. Neither supplies a sharp global
first-order constant by itself. All tapers in the upper theorem are fixed
before N tends to infinity; the changing-taper lower bound in Note 12 §13
has different uniformity and is not contradicted by this theorem.

This continues [Note 12 §§10–12](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) at repository HEAD
`663e006d39bfb16fd5393a5eb029f3a8de5c06cd`, following the
[result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md),
[complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md).
The changed quantity is the actual complete upper error. This is a
quantitative estimate, not another equivalent simplicity criterion.
[Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) records the checks and the sole anchor
correction. No analytic part of this note has been formalized in Lean.

## 1. Statement

Assume RH. Fix a real compactly supported Gevrey function
\(W\in C_c^\infty([-1,1])\), with \(W(0)=1\), for which

\[
 \|W^{(j)}\|_1\le A^{j+1}(j!)^\sigma,
 \qquad 1<\sigma<2.
 \tag{GC1}
\]

Write \(w=W|_{[0,1]}\), \(L=\log N\), and

\[
 V_{N,w}(s)=\sum_{n\le N}\frac{\mu(n)}{n^s}
                  w\!\left(\frac{\log n}{L}\right),
 \qquad
 E_{N,w}=\frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\zeta(\frac12+it)V_{N,w}(\frac12+it)|^2}
      {\frac14+t^2}\,dt.
 \tag{GC2}
\]

For every \(\eta>0\), there is a constant depending only on \(W,\eta\)
such that, simultaneously for all integers \(N\ge2\) and all real \(t\),

\[
 \left|\zeta(\tfrac12+it)V_{N,w}(\tfrac12+it)\right|
 \ll_{W,\eta}(3+|t|)^{(\sigma-1)/2+\eta}.
 \tag{GC3}
\]

Consequently, for \(0<2\eta<2-\sigma\), the actual error has the uniform
height-tail estimate

\[
 \sup_{N\ge2}\frac1{2\pi}\int_{|t|>T}
 \frac{|1-\zeta(\frac12+it)V_{N,w}(\frac12+it)|^2}
      {\frac14+t^2}\,dt
 \ll_{W,\eta}T^{\sigma-2+2\eta},
 \qquad T\ge2,
 \tag{GC4}
\]

and

\[
                       E_{N,w}\longrightarrow0.
 \tag{GC5}
\]

In particular this applies to each fixed
\(w_p(u)=\exp(1-(1-u)^{-p})\), \(0\le u<1\), \(w_p(1)=0\),
with \(p>1\), using its compact Gevrey extension of order
\(\sigma=1+1/p\) from Note 12 §12. This theorem is not uniform over changing
tapers. It does not assert an \(O(1/L)\) rate, a sharp asymptotic constant,
or simplicity.

## 2. Inputs and the exact moving-line convolution

The primary analytic input is the RH estimate

\[
 |S(t)|\le(\tfrac14+o(1))\frac{\log t}{\log\log t}
 \tag{GC6}
\]

from Carneiro–Chandee–Milinovich, *Bounding \(S(t)\) and \(S_1(t)\) on
the Riemann hypothesis*, [arXiv:1309.1526](https://arxiv.org/pdf/1309.1526),
Theorem 2, together with their introductory Riemann–von Mangoldt formula.
One-sided limits of that formula handle interval endpoints that are zeros;
all counts below include multiplicities. We also use only the consequence
\(|\zeta(\frac12+it)|=t^{o(1)}\) of Chandee–Soundararajan,
*Bounding \(|\zeta(1/2+it)|\) on the Riemann hypothesis*,
[arXiv:0908.2008](https://arxiv.org/pdf/0908.2008), Theorem 1.1.
Both primary statements were reopened. The completed product and its exact
gamma and rational factors are retained below.

Put \(\beta=1/\sigma\), and for **any** \(H>0\) set

\[
 K_H(v)=\frac1{2\pi}\int_{-1}^1 W(u)e^{(H+iv)u}\,du.
\]

Integrating the full complex exponential by parts gives

\[
 |K_H(v)|\le \frac{e^H}{2\pi}
       \frac{\|W^{(j)}\|_1}{|H+iv|^j}.
\]

Optimizing the integer \(j\) using (GC1) therefore gives constants
\(C,c>0\), independent of **both** \(H\) and \(v\), such that

\[
                  |K_H(v)|\le C e^H e^{-c|v|^\beta}.
 \tag{GC7}
\]

This step does not differentiate \(e^{Hu}W(u)\) and thereby introduce an
uncontrolled \(H\)-dependent decay constant. The extension to negative
\(u\) is retained and causes no change: \(e^{Hu}\le e^H\) throughout
the support.

Note 12 §12's exact convolution is valid at every positive \(H\):

\[
 V_{N,w}(s)=\int_{\mathbb R}
       \frac{K_H(v)}{\zeta(s+(H+iv)/L)}\,dv,
 \qquad \Re s+H/L>\tfrac12.
 \tag{GC8}
\]

It follows first from the absolutely convergent Möbius series, then by
shifting the integration line within the zero-free right half-plane.
The coarse RH reciprocal bound proved there is

\[
 |\zeta(\tfrac12+a+iy)|^{-1}
       \le C(3+|y|)^{C\log(2/a)},\qquad 0<a\le\tfrac14.
 \tag{GC9}
\]

The same completed-product proof, or integration of its real logarithmic
derivative, extends this with a fixed polynomial bound for
\(1/4\le a\le3/2\); for \(a\ge3/2\), the Euler series gives
\(|1/\zeta|\le\zeta(2)\). Thus for \(a\ge1/L\), all the ranges needed
below satisfy the weaker uniform estimate

\[
 |\zeta(\tfrac12+a+iy)|^{-1}
          \le C(3+|y|)^{C\log(2+L)}.
 \tag{GC10}
\]

Together with (GC7), this pays the horizontal contour pieces and justifies
(GC8) for the varying choices of \(H\) below. No zero is crossed and no
residue is deleted.

## 3. A sharp-coefficient reciprocal bound directly from (GC6)

For \(t\) large, write \(U=\log t\), \(\ell=\log U\). For each fixed
\(\epsilon>0\), define
\(A_t=(\frac12+\epsilon)U/\ell\).
Let \(n_t(v)\) count all zero ordinates in \([t-v,t+v]\), with
multiplicity. Uniformly for \(0\le v\le t/2\),

\[
 n_t(v)\le \frac v\pi\log(t/(2\pi))+A_t
 \tag{GC11}
\]

for sufficiently large \(t\). Indeed, the difference of the two \(S\)
terms is at most \((1/2+o(1))U/\ell\), uniformly since both endpoints
are at height comparable to \(t\). The smooth counting-function increment
is at most \(v\log(t/(2\pi))/\pi\), by concavity of \(\log\).
The \(O(1/t)\) Riemann–von Mangoldt errors are absorbed into \(\epsilon\).
One-sided endpoint limits give exactly the same upper bound for the closed
interval. In particular any atom at \(v=0\) is included.

For \(0<a\le3/2\), Stieltjes integration gives the exact positive identity

\[
 \sum_\lambda\frac{m_\lambda a}{a^2+(t-\lambda)^2}
       =\int_0^\infty n_t(v)\frac{2av}{(a^2+v^2)^2}\,dv.
\]

Apply (GC11) up to \(t/2\) and extend its two nonnegative elementary
integrals to infinity. The remaining tail is
\(O(aU/t)\), from \(n_t(v)\ll(t+v)\log(t+v+3)\) for \(v\ge t/2\).
Since
\(\int_0^\infty2av^2/(a^2+v^2)^2\,dv=\pi/2\) and
\(\int_0^\infty2av/(a^2+v^2)^2\,dv=1/a\),

\[
 \sum_\lambda\frac{m_\lambda a}{a^2+(t-\lambda)^2}
 \le\frac12\log(t/(2\pi))+\frac{A_t}{a}+O(aU/t).
 \tag{GC12}
\]

The exact completed-product formula is

\[
 \Re\frac{\zeta'}\zeta(s)
 =\sum_\lambda\frac{m_\lambda a}{a^2+(t-\lambda)^2}
 -\frac12\Re\psi(s/2)+\frac12\log\pi
 -\Re\left(\frac1s+\frac1{s-1}\right),
 \quad s=\tfrac12+a+it.
\]

Uniform Stirling estimates for \(0<a\le3/2\) cancel the first term of
(GC12), leaving
\(\Re\zeta'/\zeta(s)\le A_t/a+O(U/t)\).
Integrate from \(a\) to \(3/2\) and use \(|1/\zeta(2+it)|\le\zeta(2)\):

\[
 \log|\zeta(\tfrac12+a+it)|^{-1}
       \le A_t\log\frac{3/2}{a}+O(1),
 \qquad 0<a\le3/2.
 \tag{GC13}
\]

The constant is uniform in \(a\). This proof needs no typicality,
inverse-jet estimate, or zero separation.

## 4. Low heights: preserve the entire nearby zero cluster

Fix \(b<\beta\), to be chosen sufficiently close to \(\beta\). First
consider the range

\[
                    U=\log t\le L^b.
 \tag{GC14}
\]

Fix a small \(d>0\), put \(r=d/\ell\), and let \(M\) be the number of
zeros, with multiplicity, in \(|\lambda-t|\le r\). By (GC11),

\[
       M\le\left(\tfrac12+d/\pi+\epsilon\right)U/\ell.
 \tag{GC15}
\]

Set \(F(z)=\xi(\frac12+z)\). Remove exactly that cluster:
\(F(z)=P_t(z)G_t(z)\),
\(P_t(z)=\prod_{|\lambda-t|\le r}(z-i\lambda)^{m_\lambda}\).
The function \(G_t\) is nonzero in \(|z-it|<r\).

We need a uniform estimate for its regular logarithmic derivative, rather
than an inverse bound that discards the numerator's zeros. Anchor the
paired product at \(z_*=3/2+it\). Its logarithmic-derivative difference is
absolutely convergent:

\[
 \frac{G_t'}{G_t}(z)=\frac{F'}F(z_*)
  -\sum_{|\lambda-t|\le r}\frac{m_\lambda}{z_*-i\lambda}
  +\sum_{|\lambda-t|>r}m_\lambda
       \left(\frac1{z-i\lambda}-\frac1{z_*-i\lambda}\right).
 \tag{GC16}
\]

Here \(F'/F(z_*)=O(U)\) by the exact completion and the absolutely
convergent logarithmic derivative of \(\zeta\) on \(\Re s=2\).
For \(|z-it|\le r/2\), the terms with \(|\lambda-t|>1\) contribute
\(O(U)\), by the unit-window zero count and the summable squared
denominators. For \(r<|\lambda-t|\le1\), (GC11) and partial summation give

\[
 \sum_{r<|\lambda-t|\le1}\frac{m_\lambda}{|\lambda-t|}
 \ll U\log(1/r)+\frac{U}{r\ell}
 \ll_d U\log\ell.
\]

Thus (GC16) is \(O_d(U\log\ell)\). Integrating on the disk of radius
\(r/2\) proves

\[
 \left|\frac{G_t(it)}{G_t(it+z)}\right|
       \le\exp\{O_d(U\log\ell/\ell)\}=t^{o(1)}.
 \tag{GC17}
\]

The exact completion ratio
\(\mathcal A(\frac12+it+z)/\mathcal A(\frac12+it)\), where
\(\mathcal A(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\), is likewise
\(\exp\{O(rU)\}=t^{o(1)}\) on this disk. It has not been suppressed.

Choose \(H=M+1\). In (GC14), for large \(L\), \(H/L\le r/4\)
uniformly. For \(|v|\le rL/4\), the displacement
\(z=(H+iv)/L\) lies in the preceding disk. Each individual cluster
factor obeys the exact inequality

\[
 \frac{|t-\lambda|}
 {\sqrt{(H/L)^2+(t+v/L-\lambda)^2}}
                   \le\sqrt{1+v^2/H^2}.
 \tag{GC18}
\]

Therefore the contribution of this entire part of (GC8), after multiplying
by \(\zeta(\frac12+it)\), is at most

\[
 t^{o(1)} e^H
 \int_{\mathbb R}C e^{-c|v|^\beta}(1+|v|/H)^M\,dv
 \le t^{o(1)}
       \exp\{(\sigma-1)M\log(M+2)+O_W(M+1)\}.
 \tag{GC19}
\]

For completeness, \((1+x)^M\le2^M(1+x^M)\), and the \(M\)-th
moment of \(e^{-c|v|^\beta}\) is
\(2\beta^{-1}c^{-(M+1)/\beta}\Gamma((M+1)/\beta)\).
Division by \(H^M=(M+1)^M\), followed by Stirling, proves the last
inequality. Thus (GC15) makes (GC19) at most

\[
            t^{(\sigma-1)(1/2+d/\pi+\epsilon)+o(1)}.
 \tag{GC20}
\]

The omitted \(v\)-tail is genuinely paid. Use (GC10), (GC7), and the
critical-line upper bound. With \(R=rL/4\), its integrand is bounded by

\[
 C\exp\{H+o(U)-c|v|^\beta
           +C\log(2+L)\log(3+t+|v|/L)\}.
\]

Uniformly for \(|v|\ge R\) in (GC14), the positive terms are
\(o(|v|^\beta)\): indeed
\(R\gg_d L/\log L\), \(U\le L^b\), and \(b<\beta\).
The remaining logarithmic growth in \(|v|\) is also dominated uniformly
on this tail. Its integral is
\(O(\exp(-c'R^\beta))\), in particular bounded by 1. This closes the
low-height estimate for every sufficiently large \(L,t\).

## 5. High heights: a different moving line removes the remaining range

Now assume

\[
                          U\ge L^b.
 \tag{GC21}
\]

Choose a small fixed \(\kappa>0\), set \(H=\kappa U\),
\(a=H/L\), and first restrict to \(|v|\le tL/2\). The imaginary part
\(y=t+v/L\) then satisfies \(t/2\le y\le3t/2\), so
\(\log y=U+O(1)\) uniformly. If \(0<a\le3/2\), (GC13) gives

\[
 \log|\zeta(\tfrac12+a+iy)|^{-1}
 \le(\tfrac12+\epsilon+o(1))\frac U\ell
               \log^+(C_\kappa L/U)+O(1).
\]

The range (GC21) implies \(\log L\le\ell/b\), and therefore

\[
 \log^+(C_\kappa L/U)
              \le(b^{-1}-1)\ell+O_\kappa(1).
\]

If \(a\ge3/2\), the Euler-series bound is stronger. Thus throughout
this central part of the integral,

\[
 |\zeta(\tfrac12+a+iy)|^{-1}
       \le t^{(1/2+\epsilon)(b^{-1}-1)+o(1)}.
 \tag{GC22}
\]

Multiplying by the numerator's \(t^{o(1)}\) bound and integrating
(GC7), with \(e^H=t^\kappa\), gives

\[
 t^{\kappa+(1/2+\epsilon)(b^{-1}-1)+o(1)}.
 \tag{GC23}
\]

For \(|v|>tL/2\), use (GC10) instead. The exponent is at most

\[
 \kappa U+o(U)-c|v|^\beta
         +C\log(2+L)\log(3+t+|v|/L).
\]

Its positive terms are \(o(|v|^\beta)\) uniformly for these \(v\),
\(t\) and \(L\); here \(|v|\ge tL/2\), and in (GC21)
\(L\le U^{1/b}\). This full tail is
\(O(\exp(-c'(tL)^\beta))\). It is not discarded as a formal contour
error. Equations (GC23) and this estimate close every high-height range,
including \(t\) much larger than \(N\).

## 6. Uniform domination and complete convergence

Given \(\eta>0\), first choose \(b<\beta\) sufficiently close to
\(\beta\); then choose \(d,\epsilon,\kappa>0\) sufficiently small.
The exponents in both (GC20) and (GC23) are then less than
\((\sigma-1)/2+\eta\). Enlarging the constant handles their uniform
\(o(1)\)'s for all large \(t\).

The bounded \(t\)-range also has a uniform bound in \(N\). One can
cover it by finitely many small disks each containing either no zero or
one fixed zero location with its full multiplicity. On each disk, the
same regular-factor argument gives a bounded quotient times a fixed
polynomial in \(v\); a fixed \(H>0\) and (GC7) integrate that
polynomial. The exterior \(|v|\gg L\) is paid by (GC10) and Gevrey
decay. No inverse leading Laurent coefficient is used. Finally, the
finitely many integers \(N\) with \(\log N\) below the proof's threshold
are bounded by the finite polynomial and the critical-line
\(t^{o(1)}\) estimate. Conjugation handles negative \(t\).
This proves (GC3) and hence (GC4).

For each fixed \(t\) with \(\zeta(\frac12+it)\ne0\), (GC8) on a fixed
line, its local analytic Taylor expansion, and its paid exterior tail
give \(V_{N,w}(\frac12+it)\to1/\zeta(\frac12+it)\). Equivalently,
the constant term is \(\int K_H(v)\,dv=W(0)=1\) and the first error is
\(O_t(1/L)\); the full exterior contribution is exponentially small.
At zero ordinates the product is 0, but this countable set has measure 0.
Choose \(2\eta<2-\sigma\). The square of (GC3), divided by
\(\frac14+t^2\), is integrable independently of \(N\), so dominated
convergence proves (GC5).

This is a full-height upper result for fixed original Möbius coefficients
with the declared taper. It is compatible with multiple zeros: their
already proved local costs are finite for this Gevrey class. The uniform
tail bound is not \(O(1/L)\), and it does not justify multiplying it by
\(L\) and exchanging limits. A sharp first-order global norm and an
opposing simplicity estimate remain unproved.


## 7. A quantitative complete-norm rate

Assume RH and the fixed compact Gevrey hypothesis (GC1), with 1<σ<2.
For every fixed exponent B>1+2σ, the actual upper bound is
\[
 \boxed{E_{N,w}\ll_{W,B}
             \frac{(\log\log N)^B}{\log N}\qquad(N\to\infty).}
 \tag{QR1}
\]
It has a growing logarithmic allowance and is not a sharp O(1/log N)
constant. In particular it does not contradict the multiplicity costs.

Put L=log N, β=1/σ, and choose once and for all q with
(σ−1)/2<q<1/2. By (GC3),
\[
 |e_N(1/2+it)|\ll_{W,q}(3+|t|)^q,
 \qquad e_N=1-\zeta V_{N,w}.
 \tag{QR2}
\]
Choose a fixed A>1/(1−2q) and set
\[
 T=L^A,\qquad d=(\log L)^B/L,\qquad
 D(t)=\min\{1/4,\operatorname{dist}(t,\{\gamma:\zeta(1/2+i\gamma)=0\})\}.
 \tag{QR3}
\]
For large N, d<1/4. Zeros are counted once in this distance; any zero
sums used to bound it may include their full multiplicities. Split the
critical-line integral into |t|>T, the set |t|≤T with D(t)<d, and its
complement. All three portions of the squared norm will be bounded.

### 7.1 Increasing heights and the near-zero portion

By (QR2), the first portion is
\[
 E_{N,w}^{>T}\ll_{W,q}T^{-1+2q}
       =L^{-A(1-2q)}=o(L^{-1}).
 \tag{QR4}
\]
The near-zero portion is covered by intervals |t−γ|<d. On each such
interval, (3+|t|)^(2q)/(1/4+t²) is at most a constant times
(3+|γ|)^(−2+2q). Thus
\[
 E_{N,w}^{\{|t|\le T,D(t)<d\}}
 \ll_{W,q}d\sum_{\gamma\ {\rm distinct}}
                           (3+|\gamma|)^{-2+2q}
 \ll_{W,q}d.
 \tag{QR5}
\]
The complete sum converges by the unit-window O(log(3+|γ|)) zero count
and 2q<1. Overlapping intervals only increase this upper allowance;
there is no zero-separation assumption.

### 7.2 A zero-free local estimate uniform in the base height

On a point s=1/2+it with D=D(t)>0, the complete paired xi product,
anchored at 2+it, gives
\[
 \sup_{|z|\le D/2}
 \left|\frac{\zeta'}\zeta(s+z)\right|
       \ll \frac{\log(3+|t|)}{D}.
 \tag{QR6}
\]
Here is its full payment. The difference of the logarithmic derivatives
of ξ at s+z and 2+it is the absolutely convergent sum of
1/(s+z−ρ)−1/(2+it−ρ). Zeros with |γ−t|≤1 have denominators at least
D/2 in the first term and at least 3/2 in the anchor. Their number is
O(log(3+|t|)), with multiplicity, so their cost is O(log(3+|t|)/D).
The remaining differences have summable squared denominators and cost
O(log(3+|t|)). The anchor is O(log(3+|t|)) by the absolutely convergent
Euler logarithmic derivative and the exact completion. Subtracting the
completion at s+z has the same bound. At bounded t, that completion is
uniformly regular because Re(s+z) lies in [3/8,5/8]. The cap D≤1/4
also keeps the ζ pole at 1 out of every disk. Thus (QR6) retains the
complete product and is uniform without an inverse-derivative bound.

On the complementary portion of (QR3), D≥d and |t|≤T. Use the exact
convolution with H=1 and its coherent subtraction:
\[
 e_N(s)=\int_{\mathbb R}K_1(v)
       \left(1-\frac{\zeta(s)}{\zeta(s+(1+iv)/L)}\right)dv,
 \qquad \int K_1(v)dv=W(0)=1.
 \tag{QR7}
\]
Choose a sufficiently small absolute c_0>0 and put
V_t=c_0 L D/\log(3+|t|). Since Ld=(log L)^B and log(3+T)=O_A(log L),
V_t→∞ uniformly on this entire portion. For |v|≤V_t, the line segment
from s to s+(1+iv)/L lies in the disk of (QR6), and integrating the
logarithmic derivative along it gives an exponent bounded by a fixed
constant. Hence
\[
 \left|1-\frac{\zeta(s)}{\zeta(s+(1+iv)/L)}\right|
 \ll\frac{(1+|v|)\log(3+|t|)}{L D},
 \qquad |v|\le V_t.
 \tag{QR8}
\]
The finite absolute first moment of K_1 pays this central contribution
to (QR7). No signed cross term is removed from the exact identity.

For the full complementary v-integral, the coarse RH reciprocal bound
(GC9) at a=1/L and any polynomial bound for ζ on the critical line give
\[
 |K_1(v)|\left(1+
       \left|\frac{\zeta(s)}{\zeta(s+(1+iv)/L)}\right|\right)
 \ll\exp\{-c|v|^\beta+
          C_A(\log L)^2+C\log L\log(3+|v|)\}.
 \tag{QR9}
\]
This holds uniformly for |t|≤L^A. The omitted range has
\[
 |v|>V_t\ge c_A(\log L)^{B-1}.
\]
Since β(B−1)>2, both positive terms in the exponent of (QR9) are
o(|v|^β) uniformly on that whole unbounded range. Its integral is
O_{W,A,B,J}(L^(−J)) for every fixed J>0. Thus the full pointwise error
on the complementary critical-line set satisfies
\[
 |e_N(1/2+it)|
 \ll\frac{\log(3+|t|)}{L D(t)}+O_{W,A,B,J}(L^{-J}).
 \tag{QR10}
\]
This pays all nonlocal heights in the convolution before any squared
norm estimate is made.

### 7.3 Integrate the distance singularity and assemble the norm

The following integral bound is independent of T:
\[
 \int_{\{D(t)\ge d\}}
 \frac{\log^2(3+|t|)}{(1/4+t^2)D(t)^2}\,dt\ll d^{-1}.
 \tag{QR11}
\]
Where D=1/4 the integral is bounded by a fixed convergent integral.
On the remaining set, assign each t to a nearest zero ordinate γ
(ties have measure zero). Then |t−γ|<1/4, so the weight times log² is
comparable to log²(3+|γ|)/(1/4+γ²). Each assigned cell is a subset of
{d≤|t−γ|<1/4}, whose integral of |t−γ|^(−2) is at most 2/d.
Summing the resulting upper bounds proves (QR11), because
Σ_γ log²(3+|γ|)/(1/4+γ²)<∞ by the complete unit-window count.
No lower gap or simplicity has been imposed.

Equations (QR10)–(QR11), with J chosen larger than one, give
\[
 E_{N,w}^{\{|t|\le T,D(t)\ge d\}}
          \ll_{W,A,B}\frac1{L^2d}+O(L^{-2J}).
 \tag{QR12}
\]
Combining (QR4), (QR5) and (QR12) proves (QR1), since d dominates
both 1/(L²d) and o(1/L).

For the explicit family w_p, one may take any B>3+2/p. In particular,
for each B>3 a sufficiently large fixed p>1 gives the rate (QR1).
This does not permit p or the cutoff to vary with N. No priority or
best-known-bound claim is made; comparison with the wider literature
requires separate specialist review. The current mathematical claim is
only the displayed conditional upper bound with its written proof.

The remaining logarithmic allowance is decisive for the investigation:
L E is bounded above here by O((log L)^B), not by the simple-zero constant.
The fixed local lower constants, including those of multiple zeros,
are compatible with (QR1). RH-to-simplicity remains unproved.


As a direct consequence, the Nyman–Beurling infimum \(d_N^2\) defined
in Note 12 (NB1) obeys the same upper bound, since its admissible
polynomials include this particular \(V_{N,w}\). Together with the
fixed-p choice just described, this yields, for every fixed B>3, an
RH-conditional bound \(d_N^2\ll_B(\log\log N)^B/\log N\).
This corollary makes no comparison of priority or optimality.


## 8. Exact asymptotics on a fixed bounded height interval

**Gain.** Under RH, the fixed Gevrey class of Note 12 §12 has an exact
norm asymptotic on every fixed bounded height interval whose endpoints
are not zero ordinates. This includes the whole interval, not only
shrinking neighborhoods selected for a lower bound. Its error is
\(O_{T,w}((\log\log N)/(\log N)^2)\). This compact proof alone is not a global upper estimate: its constants
may depend on the fixed height. Sections 1–7 separately supply the
complete upper theorem for the narrower order range 1<σ<2.

Put \(L=\log N\), \(e_N(s)=1-\zeta(s)V_{N,w}(s)\), and
\[
 E_{N,w}^{\le T}
 =\frac1{2\pi}\int_{-T}^{T}
      \frac{|e_N(1/2+it)|^2}{1/4+t^2}\,dt .
\]
Assume \(T>0\) and neither endpoint is a zero ordinate. With the exact
orders \(m_\rho\), both signs counted, the result is
\[
 \boxed{\displaystyle
 E_{N,w}^{\le T}
 =\frac1L\sum_{\substack{\rho=1/2+i\gamma\\|\gamma|<T}}
           \frac{C_{m_\rho}(w)}{|\rho|^2}
   +O_{T,w}\!\left(\frac{\log L}{L^2}\right).}
 \tag{CH1}
\]
The sum is over distinct zeros. No simplicity, negative derivative
moment, or height-uniform zero separation is assumed.

### 8.1 The original convolution and its complete remote tail

Use exactly the compact Gevrey extension and fixed \(H>0\) from
Note 12 (GF3)–(GF5):
\[
 V_{N,w}(s)=\int_{\mathbb R}
       K_H(v)\,\frac1{\zeta(s+(H+iv)/L)}\,dv .
 \tag{CH2}
\]
Fourier inversion at zero and Gevrey decay give
\[
 \int_{\mathbb R}K_H(v)\,dv=1,\qquad
 \int_{\mathbb R}(H+|v|)|K_H(v)|\,dv<\infty .
 \tag{CH3}
\]
These are identities and an absolute integrability statement for the
same signed kernel. In particular the first identity is used before
bounding the analytic remainder.

For any fixed height bound \(T_0\) and fixed \(r>0\), the complete
reciprocal bound (GF6) gives uniformly for \(|t|\le T_0\)
\[
 \int_{|v|\ge rL}
  \left|\frac{K_H(v)}
   {\zeta(1/2+it+(H+iv)/L)}\right|\,dv
 \ll_{T_0,r,w,H}\exp(-c_rL^\beta),\quad \beta>0 .
 \tag{CH4}
\]
Indeed its competing logarithm is at most
\(C\log L\,\log(C_{T_0}+|v|/L)\), uniformly on this range. On writing
\(v=Lx\), \(|x|\ge r\), its ratio to \(|v|^\beta\) is
\(O_{T_0,r}(\log L/L^\beta)\). The stretched exponential Fourier
decay therefore absorbs every external height, including all other
reciprocal-zero poles at horizontal distance \(H/L\). This is the
same paid bound as (GF8), now explicitly uniform in a bounded set of
base heights.

### 8.2 Subtract the analytic Laurent remainder before estimating it

Fix one zero \(\rho\) of order \(m\). Choose \(r>0\) sufficiently small
that the disk \(|q|\le4r\) contains no other zero, and that
\[
 \frac1{\zeta(\rho+q)}
 =\sum_{j=1}^m b_j q^{-j}+G(q),\qquad
 b_m=\frac{m!}{\zeta^{(m)}(\rho)},
 \tag{CH5}
\]
has \(G,G'\) bounded on that disk. Such a choice uses only this fixed
isolated zero. Shrinking \(r\) if needed, take \(r\le1\).

For \(q=iy\), \(|y|\le r\), truncate (CH2) at \(|v|\le rL\).
For large \(L\), every shifted point there remains in \(|q|\le3r\).
By (CH3), subtracting \(G(q)\) inside the integral gives
\[
 \begin{split}
 &\int_{|v|\le rL}K_H(v)
       G\!\left(q+\frac{H+iv}{L}\right)dv-G(q)\\
 &\hspace{2cm}=O_{\rho,w}(L^{-1}).
 \end{split}
 \tag{CH6}
\]
The derivative bound and the first absolute moment in (CH3) pay the
integrand difference; the omitted kernel mass is exponentially small.
The actual reciprocal tail is paid by (CH4). Extending each principal
term to all \(v\) also costs an exponentially small amount: on
\(|v|\ge rL\),
\[
 |q+(H+iv)/L|^{-j}\le (L/H)^j ,
\]
so a polynomial factor is absorbed by the same kernel tail. This bound
also covers \(v\) close to \(-Ly\); no denominator lower bound of order
one is silently assumed at the edge.

Using the exact principal-term transform (GF10) now yields uniformly
for \(|y|\le r\)
\[
 e_N(\rho+q)
 =\sum_{j=1}^m
      a_j(q)\,\mathcal E_{j,w}(Lq)
   +O_{\rho,w}(|q|^m/L),
 \qquad
 a_j(q)=b_j\frac{\zeta(\rho+q)}{q^j}.
 \tag{CH7}
\]
Each \(a_j\) is analytic at zero; \(a_m(0)=1\) and
\(a_j(q)=O(q^{m-j})\) for \(j<m\). Formula (CH7) follows by using
the exact identity
\(\sum_j a_j(q)+\zeta(\rho+q)G(q)=1\) before estimating (CH6).
All expressions extend continuously to \(q=0\), where \(e_N=1\).

### 8.3 The full annulus between the zero scale and fixed height is paid

The model \(\mathcal E_{j,w}\) is the Fourier transform of the smooth
function \(p_{j,w}\) on \([0,1]\), which vanishes at one. A single
integration by parts, retaining the term at zero, gives
\[
 |\mathcal E_{j,w}(ix)|\le \frac{A_{j,w}}{1+|x|}
 \qquad (x\in\mathbb R).
 \tag{CH8}
\]
Only the finite orders \(j\le m\) occur here. Because
\(a_m(q)-1=O(q)\) and \(a_j(q)=O(q)\) for \(j<m\), (CH7) gives the
stronger, fixed-neighborhood approximation
\[
 \boxed{\displaystyle
 e_N(\rho+iy)=\mathcal E_{m,w}(iLy)+O_{\rho,w}(L^{-1}),
 \quad |y|\le r.}
 \tag{CH9}
\]
In particular
\[
 |e_N(\rho+iy)|
 \ll_{\rho,w}(1+L|y|)^{-1}+L^{-1}.
 \tag{CH10}
\]
This controls the whole annulus \(Y/L<|y|\le r\), not just each
fixed rescaled compact set.

Let \(W_\gamma(y)=(1/4+(\gamma+y)^2)^{-1}\). It is bounded and
Lipschitz on the fixed interval. From (CH8)–(CH9),
\[
 L\int_{-r}^r
  \left||e_N(\rho+iy)|^2
       -|\mathcal E_{m,w}(iLy)|^2\right|dy
 =O_{\rho,w}(\log L/L).
 \tag{CH11}
\]
The cross term uses
\(\int_{-r}^r(1+L|y|)^{-1}dy=O((\log L)/L)\);
the squared remainder costs \(O(1/L)\) after multiplication by \(L\).
Similarly the replacement of \(W_\gamma(y)\) by \(W_\gamma(0)\)
costs \(O(\log L/L)\), because
\[
 L\int_{-r}^r\frac{|y|}{(1+L|y|)^2}\,dy
 =O(\log L/L).
 \tag{CH12}
\]
Finally the omitted model tail \(|x|>rL\) has squared integral
\(O(1/L)\). Plancherel, with its normalization in (GF12), proves
\[
 \frac{L}{2\pi}\int_{-r}^r
   \frac{|e_N(\rho+iy)|^2}{1/4+(\gamma+y)^2}\,dy
 =\frac{C_m(w)}{|\rho|^2}
     +O_{\rho,w}(\log L/L).
 \tag{CH13}
\]

### 8.4 Cover the remaining compact set and retain the global boundary

There are finitely many zeros in \([-T,T]\). Choose disjoint
neighborhoods as above lying inside that interval. The complementary
closed set is a positive distance from every zero. On finitely many
zero-free disks covering it, use (CH2)–(CH4) with the analytic function
\(1/\zeta\) itself. The same coherent subtraction as in (CH6) gives
\[
 V_{N,w}(s)=1/\zeta(s)+O_{T,w}(L^{-1}),\qquad
 e_N(s)=O_{T,w}(L^{-1})
 \tag{CH14}
\]
uniformly on the complementary critical-line set. Its contribution to
\(L E_{N,w}^{\le T}\) is \(O_{T,w}(L^{-1})\). Summing (CH13) and
(CH14) proves (CH1).

The constants include radii of isolated zero disks, bounds for their
regular Laurent parts and the finitely many coefficients \(b_j\).
They are finite at each fixed height under RH, but no estimate uniform
in increasing \(T\) has been proved here. Thus (CH1) does not bound
the actual complementary norm on \(|t|>T\) uniformly in \(N\).
Even convergence of the sum of limiting profile masses would not
alone pay that complementary norm.

This proof uses the unchanged Möbius/zeta convolution (GF5) and its
complete RH reciprocal estimate. The collision controls described in
Notes 03/05 do not satisfy this original coefficient identity with the
same completed zeta factor. The result is a compact-height asymptotic,
compatible with multiple zeros; it does not produce an opposing
global upper estimate or an RH-to-simplicity conclusion.


## 9. Summability of the limiting local profile masses

Assume RH. Let w be a fixed normalized taper, flat at 1, with
\[
 \|w^{(j)}\|_\infty\le A B^j(j!)^\sigma,
 \qquad 1<\sigma<2.
 \tag{PM1}
\]
The class in Note 12 §12 with compact extension of this order satisfies
this condition. In particular w_p has σ=1+1/p<2 when p>1.

For the density defining C_m(w), the full Leibniz formula is
\[
 p_{m,w}(u)=-\sum_{j=1}^m\binom mj
              \frac{u^{j-1}}{(j-1)!}w^{(j)}(u).
 \tag{PM2}
\]
Since j!^σ/(j−1)!=j(j!)^(σ−1), (PM1) gives for a fixed D≥max(1,B)
\[
 \|p_{m,w}\|_\infty
 \le A m(2D)^m(m!)^{\sigma-1},\qquad
 C_m(w)\le A^2m^2(2D)^{2m}(m!)^{2(\sigma-1)}.
 \tag{PM3}
\]
Thus log C_m(w)≤2(σ−1)m log m+O_w(m+log(m+1)). This is a bound
for all orders m, rather than an implicit constant at each fixed order.

The RH estimate in
[Carneiro–Chandee–Milinovich, Theorem 1](https://home.olemiss.edu/~mbmilino/new_S%28t%29.pdf)
is |S(t)|≤(1/4+o(1))log t/loglog t. Its one-sided limits at a zero
of ordinate γ differ by that zero's full multiplicity: the exact counting
identity in their Lemma 3 has a continuous gamma term. Consequently
\[
 m_\rho\le(1/2+o(1))\frac{\log|\gamma|}{\log\log|\gamma|}.
 \tag{PM4}
\]
This imported classical RH consequence does not assume simple zeros.
For each ε>0, (PM3)–(PM4) imply, uniformly over zeros at large height,
\[
 C_{m_\rho}(w)\ll_{w,\varepsilon}
                  (3+|\gamma|)^{\sigma-1+\varepsilon}.
 \tag{PM5}
\]
Indeed m log m≤(1/2+o(1))log|γ| and m=o(log|γ|); bounded orders
are harmless. The implied constants may depend on the fixed taper.

The unit-height zero count is O(log(3+|t|)), with multiplicity. Summing
(PM5)/|ρ|² over unit intervals and absorbing their logarithm in ε gives,
for every 0<ε<2−σ and T≥2,
\[
 \boxed{\sum_{|\gamma|>T}\frac{C_{m_\rho}(w)}{|\rho|^2}
          \ll_{w,\varepsilon}T^{\sigma-2+\varepsilon}.}
 \tag{PM6}
\]
The sum is over distinct zeros and includes both ordinate signs. In
particular the full limiting profile mass is finite for σ<2. For w_p,
the displayed decay exponent is −1+1/p+ε.

This improves the extended-sum scope of (GF13) for the stated subclass.
It bounds the tail of the limiting zero-profile masses. Neither (PM6)
nor a fixed-height asymptotic justifies replacing the actual approximation
error outside |t|≤T by this limiting tail. The actual uniform tail bound and global domination are supplied
separately by (GC3)–(GC4); neither contains the factor 1/log N required
for a global first-order exchange of limits. No conclusion is
made for σ≥2, for a taper varying with N, or for RH-to-simplicity.


## 10. Scope and the remaining simplicity gap

The upper proof preserves the unchanged Möbius/zeta convolution, the
complete RH product, and the exact gamma and rational completion. The
[collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
does not supply a counterexample with those premises: Note 05's positive
source control fails the original ordinary Dirichlet identity, while
Note 09's arithmetic control fails the exact completed entire reflection
and original zeta tail. Their structural preservation lists cannot be
combined into one control. No exclusion of those generic controls is
asserted by this theorem.

The actual bounds now have a concrete separation: (GF13) of
[Note 12](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) supplies a positive first-order lower constant depending
on the true multiplicities, whereas (QR1) permits a growing power of
loglog N in the corresponding upper allowance. This does not oppose even
one fixed multiple zero. The fixed-height identity (CH1) and finite
profile sum (PM6) do not remove that allowance without a further uniform
first-order estimate. Choosing a different fixed taper can change the
constants but does not authorize a taper that varies with N.

Note 12 §13 makes the latter restriction quantitative: an almost-linear
moving taper has actual multiplicity-dependent lower rates, and a triple
zero can force divergence even while its extracted coefficient vanishes.
The next useful gain must estimate an actual remaining error or obtain
an opposing constant with its full uniformity. No all-zero simplicity
claim, sharp global asymptotic, or literature-priority claim is made here.
