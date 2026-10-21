# Gevrey logarithmic tapers: complete approximation and a quantitative rate

20 October 2026. Prepared for Edward Baker with substantial LLM assistance.
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

**Outcome, proved in-note under RH.** For every fixed normalized compact
Gevrey extension of order \(1<\sigma<2\), the original tapered Möbius
polynomial has the complete first-order squared-error limit
\[
 \lim_{N\to\infty}(\log N)E_{N,w}
   =S_w:=\sum_{\rho\ {\rm distinct}}
                  \frac{C_{m_\rho}(w)}{|\rho|^2}<\infty.
\]
Section 11 pays the actual scaled height tail uniformly in N. It removes
the logarithmic loss of §7 and proves \(E_{N,w}=O_W(1/\log N)\),
without simplicity or inverse-derivative moments.

Section 13 now proves the exact constant for the full Dirichlet-polynomial
infimum under RH:
\[
 \lim_{N\to\infty}(\log N)d_N^2
       =K:=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
\]
Explicit bounded filters built from powers of 2 and 3 let finitely many
zeros use different local tapers while the complete remaining tail stays
controlled. The filters and tapers are fixed before the N limit, and real
coefficients suffice. The previous additional-simplicity constant
\(2+\gamma_E-\log(4\pi)\) is the all-simple special case of this result.

Section 14 replaces attenuation on a finite set by exact bounded
Dirichlet filters, retaining the complete profile tail. For two nearby
ordinates separated by \(\Delta\), it gives the sharp leading
isolation cost \(\log M\sim\pi/|\Delta|\) in the class bounded
by one, and prices the alternative of a larger boundary supremum.
The heat-scale consequence concerns root isolation only; it does not
transfer the fixed-zeta theorem to a heat-deformed function.

Section 15 gives the exact actual local norm at a heat-split double
zero on the scale t=v/(log N)^2. Its sharp fixed-taper infimum is a
nonmonotone finite-separation coefficient, distinct from Note 15's
monotone ratio energy. Section 16 proves unconditionally that the literal
full norm is infinite for every nonzero finite Dirichlet polynomial at
each fixed 0<t<=1/2. Logarithmic Gaussian damping has sharp threshold
t/8 for restoring finiteness; it changes the approximation space.

[Note 17](17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md)
now gives a complete RH-conditional profile sum after explicit carrier
normalization at t=v/(log N)^2, uniformly for bounded v. It also proves
that this carrier destroys ordinary Dirichlet-series structure, creates
an essential singularity at one, and has a nonzero double-event transfer
cost. The unchanged-norm obstruction here and the original ST theorem
are retained; no original multiple zero is excluded.

Section 12 separately tracks a moving almost-linear taper, proving
\(E_{N,\eta}\le C\exp(C\eta^{-a})/\log N\), where
\(a>1/(2-\sigma)\) and \((\log N)^{-\theta_0}\le\eta<1/4\),
for each fixed \(0<\theta_0<1\). The specified slow schedules converge.
This is a uniform-family proof, not an application of fixed-taper constants.
These estimates remain compatible with the costs of multiple zeros.
**RH ⇒ simplicity remains unproved.**

This continues [Note 12 §§10–12](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) at repository HEAD
`663e006d39bfb16fd5393a5eb029f3a8de5c06cd`, following the
[result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md),
[complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md).
The changed quantity is the actual complete upper error. This is a
quantitative estimate, not another equivalent simplicity criterion.
[Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md) records the checks, the original anchor
correction, and the separate same-model audits of §§11–16. Sections 11–12
start from checkpoint `341152badb4340eed052f4e9e1e48ebe52b000aa`.
No analytic part of this note has been formalized in Lean.

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
\(\sigma=1+1/p\) from Note 12 §12. The theorem in §§1–6 alone is not uniform over changing
tapers and does not assert an \(O(1/L)\) rate or a first-order constant.
Section 11 supplies both for fixed tapers; §12 proves a separate bound for
a specified moving family. None of these results proves simplicity.

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
already proved local costs are finite for this Gevrey class. The bound (GC4) alone does not justify multiplying the tail by
\(L\) and exchanging limits. Section 11 subsequently pays that scaled
actual tail and proves the complete first-order norm. An opposing
simplicity estimate remains unproved.


## 7. A quantitative complete-norm rate

Assume RH and the fixed compact Gevrey hypothesis (GC1), with 1<σ<2.
For every fixed exponent B>1+2σ, the actual upper bound is
\[
 \boxed{E_{N,w}\ll_{W,B}
             \frac{(\log\log N)^B}{\log N}\qquad(N\to\infty).}
 \tag{QR1}
\]
This earlier bound has a growing logarithmic allowance. Section 11
supersedes it with the exact fixed-taper first-order limit. Both bounds
remain compatible with the multiplicity costs.

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

This proof gives only the allowance O((log L)^B) for L E. Section 11
removes that loss, but its exact coefficient still retains each true
multiplicity. Thus the old logarithmic loss is no longer the open gap;
the missing opposing multiplicity-free estimate is. RH-to-simplicity
remains unproved.


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
earlier complete upper theorem for 1<σ<2; §11 pays the scaled tail and
uses this compact theorem to obtain the exact complete limit.

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
error outside |t|≤T by this limiting tail. The unscaled tail bound and global domination (GC3)–(GC4) also
do not supply that factor by themselves. Section 11 separately proves
the required uniform scaled actual tail. This profile-mass calculation
makes no conclusion for σ≥2 or a taper varying with N; §12 treats one
moving family by its own uniform proof. RH-to-simplicity remains open.


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

The actual fixed-taper limit in §11 now equals the complete
multiplicity-dependent profile sum from (GF13) of
[Note 12](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md).
The logarithmic allowance in (QR1), and the earlier gap between compact
asymptotics and the full first-order norm, are superseded. The exact
coefficient is still \(S_w=\sum C_{m_\rho}(w)/|\rho|^2\); the proof
does not replace it by a multiplicity-free constant. Section 13 attains
the smaller constant \(K=\sum m_\rho^2/|\rho|^2\) for the full
polynomial infimum by allowing different profiles at different locations.
That removes the common-taper restriction, not the multiplicity cost.
Neither complete estimate supplies an opposing simplicity bound.

Note 12 §13 gives actual lower rates for an almost-linear moving taper.
A triple zero can force divergence on certain faster schedules even while
its extracted coefficient vanishes. Section 12 separately proves a
uniform upper estimate and convergence for specified slower schedules.
Its exponential allowance exceeds every fixed-multiplicity power cost
and therefore supplies no contradiction. The next useful gain must
estimate an actual remaining error or obtain an opposing constant with
its full uniformity. No simplicity proof, sharp moving-family asymptotic,
or literature-priority claim is made here.


## 11. Uniform scaled tail and the exact complete fixed-taper limit

20 October 2026 extension. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort ultra**. Separate same-model
derivations and audits are recorded in Review 16 §7. The gain is a uniform
bound for the actual tail after multiplication by log N, followed by the
exact full limit. No simplicity, separation, inverse-derivative moment,
specialist review or priority claim is supplied.

### 11.1. Statement and retained inputs

Assume RH. Let the fixed real function \(W\in C_c^\infty([-1,1])\) satisfy
\(W(0)=1\) and \(\|W^{(j)}\|_1\le A^{j+1}(j!)^\sigma\), where
\(1<\sigma<2\). Set \(w=W|_{[0,1]}\), \(L=\log N\),

\[
 V_{N,w}(s)=\sum_{n\le N}\mu(n)n^{-s}w(\log n/L),\qquad
 e_N(t)=1-\zeta(\tfrac12+it)V_{N,w}(\tfrac12+it),
\]
\[
 E_{N,w}^{>T}=\frac1{2\pi}\int_{|t|>T}
       \frac{|e_N(t)|^2}{1/4+t^2}\,dt.
 \tag{ST1}
\]

For every \(0<\eta<2-\sigma\),

\[
 \boxed{\quad \sup_{N\ge2} L E_{N,w}^{>T}
       \ll_{W,\eta} T^{\sigma-2+\eta},\qquad T\ge2.\quad}
 \tag{ST2}
\]

In particular the scaled actual norm is tight in height. If \(m_\rho\)
is the order of each distinct nontrivial zero, define

\[
 p_{m,w}(u)=-\frac1{(m-1)!}
                 \frac{d^m}{du^m}\bigl(u^{m-1}w(u)\bigr),\qquad
 C_m(w)=\int_0^1|p_{m,w}(u)|^2\,du.
 \tag{ST3}
\]

Then the complete first-order limit is

\[
 \boxed{\quad
 \lim_{N\to\infty} L E_{N,w}
       =\sum_{\rho\ {\rm distinct}}\frac{C_{m_\rho}(w)}{|\rho|^2}
       <\infty .\quad}
 \tag{ST4}
\]

Both signs of every ordinate occur in this sum. This implies the actual
upper bound \(E_{N,w}=O_W(1/\log N)\) and, for the usual Nyman--Beurling
infimum, \(d_N^2\le E_{N,w}=O_W(1/\log N)\).

We use the inputs already proved and reviewed in this note: the exact
moving-line convolution, its uniform Gevrey kernel, the full cluster
factorization with completion, and the global domination

\[
 |e_N(t)|\ll_{W,q}(3+|t|)^q
 \quad\text{for any fixed }q>(\sigma-1)/2.
 \tag{ST5}
\]

The primary height inputs remain Carneiro--Chandee--Milinovich,
[arXiv:1309.1526](https://arxiv.org/pdf/1309.1526), Theorem 2 and its
Riemann--von Mangoldt convention, and Chandee--Soundararajan,
[arXiv:0908.2008](https://arxiv.org/pdf/0908.2008), Theorem 1.1.
There is no additional unquoted analytic input. The fixed-height exact
norm limit is this note’s compact-height calculation (CH1).

### 11.2. The pointwise improvement keeps the numerator and all cluster zeros

Put \(\beta=1/\sigma\). Choose a fixed \(q\) with
\((\sigma-1)/2<q<1/2\), and then choose \(b<\beta\), sufficiently
close to \(\beta\), as in this note. Consider large positive \(t\), with

\[
 U=\log t,\quad \ell=\log U,\quad U\le L^b,\quad r=d/\ell,
 \tag{ST6}
\]

where \(d>0\) is a sufficiently small fixed constant. Let \(M\) be
the number, with multiplicity, of zeros in \(|\lambda-t|\le r\).
The same one-sided counting estimate as this note gives

\[
 M\le(\tfrac12+d/\pi+\epsilon)U/\ell.
 \tag{ST7}
\]

Take \(H=M+1\), and let \(\omega=(H+iv)/L\). For sufficiently
large \(L,t\), uniformly in (ST6), \(H/L\le r/4\). On
\(|v|\le rL/4\), the displacement lies in the disk \(|\omega|<r/2\).
Write

\[
 F(z)=\xi(\tfrac12+z)=P_t(z)G_t(z),\qquad
 P_t(z)=\prod_{|\lambda-t|\le r}(z-i\lambda)^{m_\lambda}.
\]

The exact completed ratio is

\[
 \frac{\zeta(\frac12+it)}{\zeta(\frac12+it+\omega)}
       =Q_t(\omega)Z_t(\omega),\qquad
 Q_t(\omega)=\prod_{j=1}^M
                    \frac{i(t-\lambda_j)}{i(t-\lambda_j)+\omega},
 \tag{ST8}
\]

where repeated \(\lambda_j\)'s retain their multiplicities, and

\[
 Z_t(\omega)=\frac{G_t(it)}{G_t(it+\omega)}
   \frac{\mathcal A(\frac12+it+\omega)}
        {\mathcal A(\frac12+it)},\qquad
 \mathcal A(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

this note’s paired-product anchoring at \(2+it\), with the complete
gamma and rational factors included, proves on this disk

\[
 |(\log Z_t)'|\le B_t\ll_d U\log\ell.
\]

Consequently, because \(Z_t(0)=1\),

\[
 |Z_t(\omega)|\le e^{B_t|\omega|}=t^{o(1)},\qquad
 |1-Z_t(\omega)|\le B_t|\omega|e^{B_t|\omega|}.
 \tag{ST9}
\]

The \(o(1)\) is uniform in the entire low-height range and central
disk. Its bound is \(O_d(\log\ell/\ell)\).

For \(t\) not a zero ordinate, put
\(D(t)=\min(1/4,\operatorname{dist}(t,\{\lambda\}))>0\) and
\(R_v=(1+v^2/H^2)^{1/2}\ge1\). For every factor \(r_j\) in
(ST8), the already proved geometric bound and the exact difference give

\[
 |r_j|\le R_v,\qquad
 |1-r_j|=\frac{|\omega|}{|i(t-\lambda_j)+\omega|}
     =\frac{|\omega|\,|r_j|}{|t-\lambda_j|}
     \le\frac{|\omega|R_v}{D(t)}.
\]

Telescoping the full product therefore yields

\[
 |1-Q_t|\le\frac{M|\omega|R_v^M}{D(t)},\qquad
 |1-Q_tZ_t|\le
 t^{o(1)}|\omega|
        \left(\frac{M R_v^M}{D(t)}+B_t\right).
 \tag{ST10}
\]

For \(M=0\), the first term is zero. No individual gap is bounded
below: \(D(t)\) remains in the estimate until its actual integral is paid.

### 11.3. Coherent subtraction, the extra kernel moment, and the full tail

The exact kernel and its normalization are

\[
 K_H(v)=\frac1{2\pi}\int_{-1}^1 W(u)e^{(H+iv)u}\,du,
 \quad |K_H(v)|\le C e^H e^{-c|v|^\beta},
 \quad \int_{\mathbb R}K_H(v)\,dv=1.
\]

Thus the complete error, before taking absolute values, is exactly

\[
 e_N(t)=\int_{\mathbb R}K_H(v)
       \left(1-\frac{\zeta(\frac12+it)}
                        {\zeta(\frac12+it+(H+iv)/L)}\right)dv.
 \tag{ST11}
\]

This subtracts the original constant coherently; replacing the quotient
by a standalone upper bound would lose the improvement.

The one additional moment required by (ST10) satisfies

\[
 e^H\int_{\mathbb R} e^{-c|v|^\beta}
       (H+|v|)(1+|v|/H)^M\,dv
 \le \exp\{(\sigma-1)M\log(M+2)+O_W(M+1)\}.
 \tag{ST12}
\]

To verify it, use \((1+x)^M\le2^M(1+x^M)\), and integrate
the moments of degrees \(0,1,M,M+1\). The largest gamma factor is
\(\Gamma((M+2)/\beta)\), divided by \(H^M=(M+1)^M\).
Stirling gives the displayed leading term; the added factor contributes
only \(O_W(M+\log(M+2))\), covered by the stated remainder.

Equations (ST7), (ST9)--(ST12), and the polynomial factors \(M+B_t\)
show that the central portion of (ST11) is

\[
 \ll \frac{t^{(\sigma-1)(1/2+d/\pi+\epsilon)+o(1)}}{L D(t)}
 \ll_{W,q}\frac{t^q}{L D(t)}.
 \tag{ST13}
\]

Here \(d,\epsilon\) were fixed sufficiently small, and the uniform
\(o(1)\), including the logarithm of \(M+B_t\), is absorbed in the
strict margin in \(q>(\sigma-1)/2\).

The entire complementary \(v\)-integral is also paid. Set \(R=rL/4\).
For \(|v|\ge R\), this note’s coarse all-height reciprocal estimate
and critical-line upper bound bound the absolute integrand of (ST11) by

\[
 C\exp\{H+o(U)-c|v|^\beta
       +C\log(2+L)\log(3+t+|v|/L)\}
       +C e^{H-c|v|^\beta}.
 \tag{ST14}
\]

The second term explicitly pays the subtracted constant. Uniformly under
(ST6), \(R\gg_d L/\log L\), \(U\le L^b\), and \(b<\beta\).
The positive exponent is therefore \(o(|v|^\beta)\) on this whole
tail, including \(|v|\) arbitrarily large. Its integral is
\(O(\exp[-c'(L/\log L)^\beta])\). More precisely, for every fixed
\(J>0\), that bound is

\[
                         O_{W,q,J}(L^{-J}t^{-J}),
 \tag{ST15}
\]

since \((L/\log L)^\beta\gg U+\log L\). Thus no tail is lost
after multiplication of the actual norm by \(L\).

Combining (ST13)--(ST15) with the independent full-height bound (ST5)
gives, throughout the low-height range and for all large \(t,L\),

\[
 |e_N(t)|\ll_{W,q}t^q
            \min\left(1,\frac1{L D(t)}\right)
           +O_{W,q,J}(L^{-J}t^{-J}).
 \tag{ST16}
\]

At a zero ordinate, use the first branch of the minimum; those points
also have measure zero. Conjugation gives the negative-height version.

### 11.4. Integrating the real distance, without zero separation

For the part of a nearest-zero cell with \(D(t)<1/4\), let its
nearest zero be \(\lambda\). Then \(|t-\lambda|<1/4\), the weight
\((3+|t|)^{2q}/(1/4+t^2)\) is comparable to
\((3+|\lambda|)^{2q-2}\) for large \(|t|\), and

\[
 L\int_{\mathbb R}
       \min\left(1,\frac1{L^2|t-\lambda|^2}\right)dt=4.
 \tag{ST17}
\]

Each actual cell is only a subset of this integral. Ties have measure
zero; distinct zeros may be arbitrarily close. Repeated zeros do not
create additional cells, although allowing their multiplicities in the
upper sum is harmless. On \(D(t)=1/4\), the scaled contribution is
\(O(L^{-1}\int t^{2q-2}dt)\). The term (ST15), say with \(J=2\),
has a still faster summable tail. Thus the low-height contribution to
the scaled norm over \(|t|>T\) is bounded, uniformly in \(N\), by

\[
 C_{W,q}\left[
  \sum_{|\lambda|>T-1/4}(3+|\lambda|)^{2q-2}
                  +T^{2q-1}+T^{-5}\right]
 \ll_{W,q} T^{2q-1}\log(3+T).
 \tag{ST18}
\]

The last inequality is the usual unit-window zero count, including
multiplicity. Bounded ranges omitted in the preceding large-parameter
proof can be covered by its fixed-height analogue, or absorbed in a fixed
constant; they do not affect the asserted large-height tail.

For the high-height range \(U>L^b\), use (ST5) directly, now retaining
the useful restriction \(L<U^{1/b}\). It gives the uniform scaled bound

\[
 L\int_{\substack{|t|>T\\ \log|t|>L^b}}
      \frac{|e_N(t)|^2}{1/4+t^2}\,dt
 \ll_{W,q}\int_T^\infty t^{2q-2}(\log t)^{1/b}\,dt
 \ll_{W,q}T^{2q-1}(\log T)^{1/b}.
 \tag{ST19}
\]

The finitely many \(N\) below a fixed proof threshold satisfy the
same tail after enlarging the constant, using their fixed Dirichlet
polynomials and the RH critical-line bound. Choose \(q\) sufficiently
close to \((\sigma-1)/2\), and absorb the fixed powers of \(\log T\)
in the remaining exponent margin. Equations (ST18)--(ST19) prove (ST2).
Initially this establishes the bound for all sufficiently large \(T\).
For \(2\le T\le T_0\), fix a sufficiently large \(T_0\) whose
endpoints are not zeros. The fixed-height theorem (ST20) implies
\(\sup_{N\ge2}L E_{N,w}^{\le T_0}<\infty\): it bounds all large
\(N\), and each of the finitely many remaining norms is finite. Add
the already proved scaled tail at \(T_0\). This explicitly supplies
the uniform-in-\(N\) constant needed for every \(T\ge2\).

### 11.5. From fixed-height exact norm to the complete limit

For every fixed \(T\) not itself a zero ordinate, this note’s compact-height
calculation gives

\[
 L E_{N,w}^{\le T}\longrightarrow
          \sum_{|\Im\rho|<T}\frac{C_{m_\rho}(w)}{|\rho|^2}.
 \tag{ST20}
\]

Its proof keeps every Laurent coefficient near each fixed zero and the
entire convolution tail; it does not require any inverse-derivative
estimate uniform in height. Apply (ST2) to the actual complement and then
let \(T\to\infty\). This proves both convergence and finiteness of the
series in (ST4). Equivalently, its finiteness also follows from this note’s
separate Gevrey profile-mass estimate. The scaled tail, rather than that
separate local-mass estimate alone, is what justifies this interchange.

This improves this note’s logarithmically weakened upper bound for fixed
tapers. Multiple zeros remain compatible: their actual costs are the
finite quantities \(C_m(w)\), which are not replaced by the simple-zero
cost. It does not prove RH implies simplicity.

### 11.6. Consequences for the Dirichlet-polynomial infimum

Assume RH. The complete norm theorem just proved gives, for every
fixed taper in the stated class,
\[
 \lim_{N\to\infty}(\log N)E_{N,w}
 =S_w:=\sum_{\rho\ {\rm distinct}}\frac{C_{m_\rho}(w)}{|\rho|^2}<\infty.
 \tag{IC1}
\]
All sums retain both ordinate signs. The admissible-polynomial infimum
of Note 12 (NB1) satisfies \(d_N^2\le E_{N,w}\). Together with Burnol's
lower bound (NB2), this proves
\[
 0<K:=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}
 \le\liminf_N(\log N)d_N^2
 \le\limsup_N(\log N)d_N^2\le S_w<\infty.
 \tag{IC2}
\]
In particular, under RH,
\[
                       d_N^2\asymp\frac1{\log N}.
 \tag{IC3}
\]
This fixed-taper comparison alone need not give the sharp constant
\(K\): its upper constant is supplied by one fixed admissible taper.
Section 13 subsequently attains \(K\) for the full polynomial infimum
using finite Dirichlet multiplier mixtures. Neither result replaces the
multiplicity-squared constant by a multiplicity-free one.

There is a stronger constant statement under the **additional assumption
that all nontrivial zeros are simple**. Let
\[
 Z=\sum_\rho\frac1{|\rho|^2}=2+\gamma_E-\log(4\pi).
\]
For each fixed \(0<\eta<1/4\), use Note 12 §13's almost-linear taper
\(w_\eta\), with a fixed cutoff of Gevrey order between one and two.
Its simple-zero cost is exactly \(C_1(w_\eta)=1+d\eta\), where
\(d=\int_0^1|Q'(r)|^2dr-1>0\) depends only on the cutoff. Equation
(IC1) therefore implies, for **each fixed** \(\eta\),
\[
 \limsup_N(\log N)d_N^2\le(1+d\eta)Z.
\]
Taking the infimum of these bounds over positive fixed \(\eta\), and
then using (NB2), gives
\[
 \boxed{\lim_{N\to\infty}(\log N)d_N^2=Z
          \quad\text{under RH and simplicity}.}
 \tag{IC4}
\]
This order of argument does not choose \(\eta_N\), exchange two limits,
or assert uniform constants in \(\eta\). The limsup on the left is
bounded by every member of a family of fixed real numbers on the right.
It also assumes no moment of inverse zeta derivatives.

The scope differs from the constructive statement of
[Bettin–Conrey–Farmer, Theorem 1](https://arxiv.org/pdf/1211.5191),
which concerns their specified linear Möbius polynomial under RH and an
inverse-derivative moment hypothesis that entails simplicity. Equation
(IC4) concerns the infimum over all length-N Dirichlet polynomials. It
proves neither the corresponding asymptotic for that linear polynomial
nor simplicity from RH. No comparison of priority or best-known bounds
is made here.

If a multiple zero exists, the coefficient in (IC1) contains its actual
\(C_m\), and the lower bound in (IC2) contains \(m^2\). These remain
compatible. In particular, optimizing an upper estimate whose constant
is the exact multiplicity-dependent profile sum cannot erase that same
multiplicity cost. The event-excluding arithmetic estimate remains open.

## 12. A uniform upper bound for slowly moving almost-linear tapers

20 October 2026 extension. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort ultra**. The derivation and separate
same-model checks are recorded in Review 16 §8. This section explicitly
tracks the changing cutoff and estimates the actual norm. It does not
infer uniformity from §11 or claim a necessary convergence threshold.

### 12.1. Quantitative statement

Assume RH. Fix one cutoff chi and its fixed left extension as in Note 12
(JL2), now of Gevrey order 1<sigma<2, and write beta=1/sigma. Set
\[
 w_\eta(u)=(1-u)\chi((1-u)/\eta),\quad
 V_{N,\eta}(s)=\sum_{n\le N}\mu(n)n^{-s}
                w_\eta(\log n/\log N),\qquad L=\log N.
\]
The complete error E_{N,eta} has the same weight
dt/[2pi(1/4+t^2)] as Notes 12 and 16. Fix 0<theta_0<1. Uniformly for
\[
                 L^{-\theta_0}\le\eta<1/4
                 \quad\hbox{and sufficiently large }L,
 \tag{MU1}
\]
the following holds. For every
\[
             a>\frac1{2-\sigma},
\]
there are constants C_1,C_2 depending only on the fixed cutoffs,
sigma,theta_0,a, such that
\[
 \boxed{E_{N,\eta}\le
 C_1\exp(C_2\eta^{-a})/L.}
 \tag{MU2}
\]
The exponential is an allowance in this upper proof, not a lower bound
for the actual error.

In particular, for a fixed
\[
       0<\kappa<2-\sigma,\qquad
       \eta_N=(\log L)^{-\kappa},
 \tag{MU3}
\]
choose a>1/(2-sigma) with kappa a<1. Then
\[
       E_{N,\eta_N}
       \le \exp\{-\log L+O((\log L)^{\kappa a})\}
       =L^{-1+o(1)}\longrightarrow0.
 \tag{MU4}
\]
For every prescribed kappa<1 one may first choose a fixed
1<sigma<2-kappa and a cutoff of that order. This proves (MU4) for that
fixed choice. Neither sigma nor the cutoff is subsequently varied with N.

No sharp leading constant or necessary threshold is asserted. In
particular, the sufficient boundary kappa<2-sigma is a boundary of this
payment, not a nonconvergence theorem for larger kappa.

### 12.2. The moving-H Fourier bound, with its uniform prefactor

Use exactly the compact W_eta of (JL6). Its fixed left transition is
independent of eta; its right transition has amplitude eta, width eta,
and the fixed Gevrey cutoff. For each integer n>=0,
\[
 \|W_\eta^{(n+2)}\|_1
       \le C^{n+1}\eta^{-n}(n!)^\sigma,\qquad
 \|W_\eta\|_1\le C.
\]
Define
\[
 K_{H,\eta}(v)=\frac1{2\pi}\int
                  W_\eta(u)e^{(H+iv)u}\,du,\qquad H\ge0.
\]
Integrating the full complex exponential n+2 times transfers all
derivatives to W_eta. If R=|H+iv|>=1 this gives
\[
 |K_{H,\eta}(v)|
 \le C e^H R^{-2}\frac{C^n(n!)^\sigma}{(\eta R)^n}.
\]
Optimize the integer n; use the zeroth derivative when R<=1. Thus,
with constants independent of H,eta,v,
\[
 \boxed{|K_{H,\eta}(v)|
   \le \frac{Ce^H}{1+H^2+v^2}
          \exp\{-c(\eta\sqrt{H^2+v^2})^\beta\}.}
 \tag{MU5}
\]
In particular
\[
 \int_{\mathbb R}|K_{H,\eta}(v)|\,dv\le Ce^H,\qquad
 \int_{\mathbb R}(1+|v|)|K_{1,\eta}(v)|\,dv
                \le C(1+\log(1/\eta)).
 \tag{MU6}
\]
For the second bound, split at |v|=1 and 1/eta. The intermediate
integrand is O(1/|v|); the final interval is bounded after the
substitution x=eta|v|. The first absolute moment is not uniform, but
its logarithmic growth is explicitly paid.

The exact identity
\[
 V_{N,\eta}(s)=\int_{\mathbb R}
 \frac{K_{H,\eta}(v)}{\zeta(s+(H+iv)/L)}\,dv,
 \qquad \Re s+H/L>1/2,
 \tag{MU7}
\]
holds for each N,eta,H. The proof is the unchanged absolutely
convergent Möbius-series inversion and zero-free contour shift. Formula
(MU5) and the full RH reciprocal bound pay every exterior contour
piece. The negative-u extension changes no integer coefficient.
Also, exactly, integral K_{H,eta}=W_eta(0)=1.

### 12.3. A global majorant with an explicit eta cost

The needed strengthened form of Note 16 (GC3) is the following:
for every a>1/(2-sigma), there is a fixed q<1/2 and constants C,c such
that, throughout (MU1),
\[
 \boxed{|1-\zeta(\tfrac12+it)V_{N,\eta}(\tfrac12+it)|
       \le C\exp(c\eta^{-a})(3+|t|)^q.}
 \tag{MU8}
\]
All full-height tails are included in this bound.

Put X=eta L, lambda=log(1/eta), U=log t, ell=log U for large positive t.
By (MU1),
\[
 X\ge L^{1-\theta_0},\qquad
 \log L\le(1-\theta_0)^{-1}\log X.
\]
Fix b<beta, sufficiently close to beta. The original low/high split is
replaced by U<=X^b and U>=X^b.

In the low range remove the complete zero cluster of radius
r=d/ell, with d>0 fixed and small. The regular-factor argument and
exact completion ratio in (GC16)--(GC18) are independent of eta.
They remain t^{o(1)}. The complete count, including multiplicities, gives
\[
                   M\le c_0 U/\ell,
\]
where c_0 can be chosen arbitrarily close to 1/2 from above by taking
the original fixed small parameters sufficiently small.

Choose H=M+1. The complete cluster quotient is bounded by
(1+|v|/H)^M. Using (MU5), its central integral is at most
\[
 C t^{o(1)}e^H
 \int_{\mathbb R}\frac{(1+|v|/H)^M}{1+H^2+v^2}
                              e^{-c(\eta|v|)^\beta}\,dv
 \le C t^{o(1)}
 \exp\{(\sigma-1)M\log(M+2)+M\lambda+C(M+1)\}.
 \tag{MU9}
\]
Here is a uniform moment payment. For M>=2, the M-th moment with
the quadratic denominator is at most a fixed exponential in M times
\[
       \eta^{1-M}\Gamma((M-1)/\beta).
\]
Division by H^M, Stirling's formula, and e^H give (MU9). For M=1
the remaining integral is O(1+lambda), covered by the displayed
exp(lambda) allowance; M=0 is uniformly bounded. Thus the coefficient
of lambda is M, not an unspecified taper-dependent constant.

The full low-range tail starts at |v|>=R=rL/4. Its exponent is at most
\[
 H+O(U)-c(\eta|v|)^\beta
       +C\log L\log(3+t+|v|/L).
\]
Writing z=eta|v|, its lower endpoint satisfies
z>=cX/log X. The positive terms are bounded by
\[
                  C\log X\{X^b+\log(3+z)\}.
\]
Since b<beta, this is o(z^beta), uniformly on the whole unbounded
tail. The retained quadratic denominator makes its integral bounded
by an exponentially small function of (X/log X)^beta. This includes
every reciprocal-zeta height; it is not an omitted-contour claim.
The horizontal displacement H/L is within r/4 uniformly in this
range, since b<1 and X<=L.

In the high range take H=kU, with k>0 fixed and small. The sharp
reciprocal bound (GC13) remains unchanged. On |v|<=tL/2 it costs
\[
 c_1\frac U\ell\log^+(C_kL/U)+O(1)
 \le c_1(b^{-1}-1)U+c_1\lambda U/\ell+O_k(U/\ell),
 \tag{MU10}
\]
where c_1 can be taken arbitrarily close to 1/2 from above.
Indeed log L=log X+lambda<=ell/b+lambda. The kernel integral
contributes at most Ce^H, uniformly by (MU6). Larger real shifts are
covered by the reciprocal Euler series.

The full high-range tail starts at eta|v|>=tX/2. Also U>=X^b and
X>=L^{1-theta_0} imply log L=O(log U). Therefore its positive
coarse-reciprocal exponent is bounded by a constant times
\[
 U+\log U\{U+\log(3+\eta|v|)\},
\]
which is o((eta|v|)^beta) uniformly there. Formula (MU5) again pays
its integral completely.

Combining the two central estimates, for suitably chosen fixed small
parameters, gives
\[
 \log(1+|\zeta V_{N,\eta}|)
       \le C+q_0U+c_*\,\lambda U/\log U,
 \tag{MU11}
\]
where q_0 may be as close to (sigma-1)/2 from above as desired, and
c_* as close to 1/2 from above as desired.

To prove (MU8), first choose q<1/2 such that
\[
              a>\frac1{\,2q-\sigma+1\,}.
\]
Choose the small parameters so that c_*/(q-q_0)<a, and fix
a_0 strictly between these two numbers. For log U>=a_0 lambda,
the last term of (MU11) is at most (c_*/a_0)U<(q-q_0)U.
For log U<a_0 lambda, it is at most
C(1+lambda)exp(a_0 lambda)<=C_a exp(a lambda).
This proves the explicit exponential allowance.

For bounded t, a finite fixed cluster cover and (MU5) give at most
a fixed power of eta^{-1}; the exterior range |v|>>L is paid because
X>=L^{1-theta_0}. A fixed power is absorbed in exp(c eta^{-a}).
Negative heights follow by conjugation. Enlarging constants handles
the bounded remaining L range. This completes (MU8) with every
multiplicity retained.

The sharp zero-count and critical-line inputs are exactly those
already checked in Note 16:
[Carneiro--Chandee--Milinovich, Theorem 2](https://arxiv.org/pdf/1309.1526)
and [Chandee--Soundararajan, Theorem 1.1](https://arxiv.org/pdf/0908.2008).
No new external hypothesis has entered the moving-family proof.

### 12.4. Coherent subtraction recovers the full factor 1/L

The sharper estimate uses the same cluster and the exact normalization
in (MU7), rather than separately bounding one and the zeta quotient.
In the low-height range U<=X^b, let D(t) be the distance to a nearest
zero ordinate, capped at 1/4. For D>0 and |v|<=rL/4, write
z=(H+iv)/L and the exact completed-product decomposition as
\[
 \frac{\zeta(1/2+it)}{\zeta(1/2+it+z)}
       =B_t(z)\prod_{j=1}^M r_j(z),\qquad
 r_j(z)=\frac{i(t-\lambda_j)}{i(t-\lambda_j)+z}.
\]
All repeated ordinates appear as repeated factors. The regular factor,
including the exact gamma and rational completion, has an analytic
logarithm normalized to zero at z=0, with derivative O_d(U log ell).
Thus |B_t|<=t^{o(1)} and
|1-B_t|<=|z|O_d(U log ell)t^{o(1)}. With
A(v)=sqrt(1+v^2/H^2), the complete local factors satisfy
\[
 |r_j|\le A(v),\qquad
 |1-r_j|\le |z|A(v)/D(t).
\]
Telescoping the product, including the empty product when M=0, yields
\[
 \left|1-\frac{\zeta(1/2+it)}{\zeta(1/2+it+z)}\right|
 \le \frac{Ct^{o(1)}(U\log\ell+M)(H+|v|)}{L D(t)}
                                  (1+|v|/H)^M.
\]
The one-extra-moment payment now is
\[
 \begin{split}
 &e^H\int_{\mathbb R}
 \frac{(H+|v|)(1+|v|/H)^M}{1+H^2+v^2}
                           e^{-c(\eta|v|)^\beta}\,dv\\
 &\quad\le C(1+\lambda)
 \exp\{(\sigma-1)M\log(M+2)+M\lambda+C(M+1)\}.
 \end{split}
 \tag{MU12}
\]
For M>=1 the largest needed moment is bounded by a fixed exponential
in M times eta^{-M} Gamma(M/beta), divided by H^M. The remaining
first moment is O(1+lambda); M=0 is exactly this first-moment case.
Stirling gives the same leading coefficient sigma-1 and the same
M lambda penalty as (MU9). The factor 1+lambda is absorbed into
exp(C eta^{-a}); the factor U log ell+M fits inside an arbitrarily
small t-power already reserved in choosing q_0<q.

Consequently the central integral in the exact identity
\[
 e_{N,\eta}(t)=\int_{\mathbb R}K_{H,\eta}(v)
 \left(1-\frac{\zeta(1/2+it)}
              {\zeta(1/2+it+(H+iv)/L)}\right)dv
 \tag{MU13}
\]
is at most C exp(C eta^{-a})t^q/[LD(t)]. The 1 term is kept in
this identity. Its exterior tail is smaller than the already paid
ratio tail. The low-range calculation in §12.3 strengthens to
O_J(L^{-J}t^{-J}) for every fixed J: its negative exponent is at
least c(X/log X)^beta, and this divided by U+log L tends to infinity
uniformly, because b<beta and X>=L^{1-theta_0}. The constants in this
remainder are independent of eta,N,t throughout the declared range.

Combining this coherent estimate with (MU8), using the latter when
LD<=1, gives
\[
 \boxed{|e_{N,\eta}(t)|
 \le C e^{C\eta^{-a}}(3+|t|)^q
       \min\{1,(L D(t))^{-1}\}
                  +O_J(L^{-J}(3+|t|)^{-J})}
 \tag{MU14}
\]
in the low range. At a zero the minimum is interpreted as one. The
bounded-height proof is the same finite cluster cover used for (MU8),
now with coherent subtraction and one extra moment. It costs only a
fixed power of eta^{-1} times 1+lambda and has the same full tail,
so is absorbed by the displayed exponential. Thus (MU14) covers all
bounded heights too. No inverse derivative or separation hypothesis
is introduced.

Where D=1/4, the squared minimum has integral O(L^{-2}) against the
convergent weighted majorant. On each nearest-zero cell with D<1/4,
the weight is comparable to (3+|gamma|)^{-2+2q}, and
\[
       \int_{\mathbb R}\min\{1,(L|x|)^{-2}\}\,dx=4/L.
\]
The sum of the complete zero weights converges by the unit-window count,
including arbitrary multiplicities. Restricting a cell to U<=X^b only
reduces its integral. Squaring and integrating the remainder in (MU14)
costs O(L^{-2J}), which is harmless after multiplication by L if J>=1.
Therefore the complete low-range contribution satisfies
\[
                      L E_{N,\eta}^{\rm low}
                           \le C\exp(C\eta^{-a}).
\]

For the complementary high range, U>=X^b implies
\[
              L=X/\eta\le\eta^{-1}(\log|t|)^{1/b}.
\]
Using (MU8) alone consequently gives
\[
 L E_{N,\eta}^{\rm high}
 \le C\eta^{-1}e^{C\eta^{-a}}
       \int_{t_0}^{\infty}t^{-2+2q}(\log t)^{1/b}\,dt
 \le C'e^{C'\eta^{-a}},
 \tag{MU15}
\]
since q<1/2. The fixed lower height t_0 can be taken large; the bounded
part is already covered above. Conjugation pays the negative half-axis.
This proves (MU2), including the full factor 1/L. The previous QR
logarithmic allowance is unnecessary for this coherent estimate.

### 12.5. Comparison with the actual multiplicity lower rates

The slow schedules (MU3) satisfy the independent joint hypothesis
(JL8). For any fixed exact multiplicity m>=2, the already paid actual
lower rate becomes
\[
 \liminf_N
 \frac{L E_{N,\eta_N}}{(\log L)^{\kappa(2m-3)}}
       \ge\frac{A_m}{|\rho|^2}>0.
 \tag{MU16}
\]
This is compatible with (MU2)--(MU4). The new upper statement allows
a subpower-in-L cost in LE, whereas (MU16) requires only a fixed
power of log L for a fixed event. These convergence and lower-rate
estimates supply no contradiction to a putative multiple zero.

More generally, dividing the right-hand allowance in (MU2) by the
order-m lower scale 1/(L eta^{2m-3}) gives, up to fixed constants,
\[
            e^{C\eta^{-a}}\eta^{2m-3}.
\]
For eta tending to zero this allowance exceeds every fixed-m
eta-power cost. Consequently this particular fully paid upper proof
cannot oppose JL for any fixed multiplicity. This is a quantitative
limitation of the displayed payment, not a lower bound for the error
and not a barrier to every different signed or coherent estimate.

The construction changes no original Möbius coefficient identity,
completed zeta factor, or RH premise. It permits all noncentral
multiplicities. Generic source or arithmetic controls from earlier
notes do not satisfy those premises in combination. No source-control
exclusion, sharp norm asymptotic for a moving taper, necessary
convergence threshold, or RH-to-simplicity conclusion is claimed.


## 13. Two-prime filters and the sharp polynomial-infimum constant

20 October 2026 extension, from checkpoint 39d6dba. Prepared for Edward
Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
The complete derivation and separate same-model checks are recorded in
Review 16 §9. The gain is the exact infimum coefficient under RH, with its
true multiplicities. This uses the internally established ST and CH
theorems; no specialist validation, analytic formalization, or
literature-priority claim is made.

### 13.1. Statement and exact hypotheses

Assume RH. With the convention of Note 12 (NB1), let

\[
 d_N^2=\inf_{D(s)=\sum_{n\le N}a_n n^{-s}}
       \frac1{2\pi}\int_{\mathbb R}
          \frac{|1-\zeta(\frac12+it)D(\frac12+it)|^2}
               {1/4+t^2}\,dt,
 \qquad
 K=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
 \tag{AD1}
\]

Then this note’s complete fixed-taper theorem, together with the explicit
finite mixtures below and Burnol's lower bound, proves

\[
                  \boxed{\lim_{N\to\infty}(\log N)d_N^2=K.}
 \tag{AD2}
\]

Both conjugate zeros appear separately in the sum, with their actual
orders. Real coefficients suffice in the infimum. No simplicity,
inverse-derivative moment, uniform gap, or bound on multiplicity beyond
the proved RH inputs of this note is assumed. This supplies no effective
threshold in \(N\) and no asymptotic for the original linear Möbius
polynomial. Its finite coefficient choices may depend on the actual
zero locations and multiplicities.

The imported lower bound is
\(\liminf(\log N)d_N^2\ge K\), from
[Burnol, Theorem 1.3](https://arxiv.org/pdf/math/0103058), already checked
in Note 12 (NB2). Its multiplicity convention is the square in (AD1).
Finiteness of \(K\) follows from the unit-window zero count: the sum
of squared multiplicities in a unit interval is at most the square of
the total multiplicity, \(O(\log^2(3+|t|))\), which is summable with
the present weight. The source distinctions from
[Bettin--Conrey--Farmer, Theorem 1](https://arxiv.org/pdf/1211.5191),
concerning a specified polynomial and an extra inverse-derivative moment,
remain as recorded in Notes 12 and 16. No priority comparison is asserted.

### 13.2. A mixed complete-limit lemma

Fix finitely many real normalized tapers \(w_0,\ldots,w_J\), each
admitting a compact Gevrey extension of some fixed order below two.
Taking the largest of those finitely many orders gives a common
\(1<\sigma<2\). Write

\[
 p_{m,j}(u)=-\frac{(u^{m-1}w_j(u))^{(m)}}{(m-1)!},\qquad
 \mathcal E_{m,j}(z)=\int_0^1p_{m,j}(u)e^{-zu}\,du,
 \quad C_m(w_j)=\|p_{m,j}\|_2^2.
 \tag{AD3}
\]

Let \(A_0,\ldots,A_J\) be fixed finite Dirichlet polynomials supported
on integers at most \(M\), satisfying \(\sum_jA_j(s)\equiv1\).
For \(n=\lfloor N/M\rfloor\), put

\[
 D_N(s)=\sum_{j=0}^J A_j(s)V_{n,w_j}(s).
 \tag{AD4}
\]

Every term has index at most \(Mn\le N\). Its complete error is
exactly \(e_N(t)=\sum_j A_j(\frac12+it)e_{n,j}(t)\), by the
identity \(\sum_jA_j=1\). The complete limit is

\[
 \boxed{
 \lim_{N\to\infty}(\log N)E(D_N)
   =\sum_{\rho\ {\rm distinct}}\frac1{|\rho|^2}
      \left\|\sum_{j=0}^J A_j(\rho)p_{m_\rho,j}\right\|_2^2.
 }
 \tag{AD5}
\]

Here complex values \(A_j(\rho)\) are permitted, and the norm is the
complex \(L^2(0,1)\) norm. This identity retains the signed cross
terms; it does not replace them by separately optimized squared norms.

For completeness, fix a zero \(\rho=1/2+i\gamma\) and its isolated
disk. Let \(l=\log n\). This note’s fixed-height calculation (CH9)
gives, uniformly in a fixed real neighborhood of \(y=0\),

\[
 e_{n,j}(\gamma+y)=\mathcal E_{m_\rho,j}(ily)+O(1/l),\qquad
 |\mathcal E_{m_\rho,j}(ily)|\ll(1+l|y|)^{-1}.
\]

Since \(A_j(\rho+iy)-A_j(\rho)=O(|y|)\), replacement of every
multiplier by its value at \(\rho\) introduces only \(O(1/l)\)
throughout that disk. Plancherel and the same complete local integration
as CH1 give the **unscaled** local norm
\(\|\sum_j A_j(\rho)p_{m_\rho,j}\|_2^2/(l|\rho|^2)
+O(\log l/l^2)\). Away from the finitely many zeros on a fixed
height interval, the complete error is \(O(1/l)\).

The actual exterior heights are paid separately. Each finite polynomial
is bounded on the critical line; Cauchy--Schwarz gives

\[
 |e_N(t)|^2\le C_A\sum_{j=0}^J|e_{n,j}(t)|^2.
\]

For fixed \(M\), \(\log N/\log n\to1\), and that ratio is at
most two once \(N\ge(2M)^2\). Thus this note (ST2) gives a uniform
decaying bound for the scaled actual tail in (AD5). Fixed-height limits
followed by height exhaustion prove the full equality. Every derivative
and threshold used here may depend on the fixed multiplier polynomials;
there is no assertion uniform in a multiplier varying with \(N\).

The local moment constraint is preserved even for complex multiplier
values. If \(q=\sum_jA_j(\rho)p_{m,j}\), then
\(\int_0^1u^r q(u)\,du=\delta_{r0}\) for \(0\le r<m\), since
\(\sum_jA_j(\rho)=1\). Let \(K_m\) be the degree-\((m-1)\)
endpoint reproducing kernel on \([0,1]\). Then \(q-K_m\) is
orthogonal to that polynomial space in the complex Hilbert space, so
\(\|q\|_2^2=m^2+\|q-K_m\|_2^2\). Thus the filters cannot cancel
a zero's local cost below \(m^2\).

### 13.3. An explicit bounded two-prime peak

For each target zero \(\rho\) and integer \(k\ge1\), set

\[
 P_{\rho,k}(s)=
       \left(\frac{1+2^{\rho-s}}2\right)^k
       \left(\frac{1+3^{\rho-s}}2\right)^k.
 \tag{AD6}
\]

It is a finite ordinary Dirichlet polynomial supported on
\(2^a3^b\), \(0\le a,b\le k\), hence on integers at most
\(M_k=6^k\). It obeys

\[
 |P_{\rho,k}(s)|\le1\quad(\Re s\ge1/2),\qquad
 P_{\rho,k}(\rho)=1.
 \tag{AD7}
\]

At any distinct zero \(\nu=1/2+i\lambda\),

\[
 P_{\rho,k}(\nu)\longrightarrow0.
 \tag{AD8}
\]

Indeed each factor has modulus at most one. Equality for both would
require \((\gamma-\lambda)\log2\) and
\((\gamma-\lambda)\log3\) both to lie in \(2\pi\mathbb Z\).
For \(\gamma\ne\lambda\), this would make \(\log2/\log3\)
rational, contrary to unique prime factorization. Thus at least one
factor has modulus strictly less than one. This argument applies to
the entire zero set, not merely to a finite preselected list. A one-prime
peak would not provide this guarantee.

Fix a finite set \(F\) of distinct zeros, a baseline \(w_0\), and a
fixed real taper \(w_\rho\) for each \(\rho\in F\). Define

\[
 D_{N,k}(s)=V_{n,w_0}(s)+\sum_{\rho\in F}P_{\rho,k}(s)
                   [V_{n,w_\rho}(s)-V_{n,w_0}(s)],
 \qquad n=\lfloor N/6^k\rfloor.
 \tag{AD9}
\]

This has length at most \(N\), and its multiplier coefficients sum
identically to one. For each fixed \(k\), (AD5) yields the actual
constant

\[
 S_k=\lim_{N\to\infty}(\log N)E(D_{N,k})
 =\sum_{\nu\ {\rm distinct}}\frac{\|q_{\nu,k}\|_2^2}{|\nu|^2},
\]
\[
 q_{\nu,k}=p_{m_\nu,0}+\sum_{\rho\in F}P_{\rho,k}(\nu)
                  (p_{m_\nu,\rho}-p_{m_\nu,0}).
 \tag{AD10}
\]

### 13.4. Paying the complete tail as the peak degree grows

Let \(J=|F|\). For every \(k\) and every zero \(\nu\),

\[
 \|q_{\nu,k}\|_2^2
   \le 2(J+1)^2\left(C_{m_\nu}(w_0)
                    +\sum_{\rho\in F}C_{m_\nu}(w_\rho)\right).
 \tag{AD11}
\]

This follows from (AD7), the triangle inequality, and the coefficient
vector \((J+1,1,\ldots,1)\) in Cauchy--Schwarz. Crucially, this
bound is independent of \(k\), despite \(M_k=6^k\) and arbitrarily
large individual Dirichlet coefficients. Each weighted sum on its right
is finite by this note (ST4), because there are only finitely many fixed
Gevrey tapers.

For \(\nu\in F\), (AD7)--(AD8) give
\(q_{\nu,k}\to p_{m_\nu,\nu}\). For \(\nu\notin F\), they
give \(q_{\nu,k}\to p_{m_\nu,0}\). Dominated convergence in the
**complete** sum therefore proves

\[
 \boxed{
 \lim_{k\to\infty}S_k
 =S_\infty(F,\{w_\rho\})
 :=\sum_{\rho\in F}\frac{C_{m_\rho}(w_\rho)}{|\rho|^2}
       +\sum_{\nu\notin F}\frac{C_{m_\nu}(w_0)}{|\nu|^2}.
 }
 \tag{AD12}
\]

Here is an explicit tail-selection form of that payment. Fix \(H\)
containing all of \(F\), and let \(\theta_H<1\) be the maximum of
the modulus of \(P_{\rho,1}(\nu)\) over the finitely many pairs
\(\rho\in F\), \(|\Im\nu|\le H\), \(\nu\ne\rho\).
Take \(\theta_H=0\) if this set is empty. The same triangle and
norm-difference identities give a finite constant \(B_H\), independent
of \(k\), such that

\[
 |S_k-S_\infty|
 \le B_H\theta_H^k
       +4(J+1)^2\sum_{j\in\{0\}\cup F}
                  \sum_{|\Im\nu|>H}\frac{C_{m_\nu}(w_j)}{|\nu|^2}.
 \tag{AD13}
\]

Explicitly, for \(\rho=1/2+i\gamma\) and \(\nu=1/2+i\lambda\),
\(|P_{\rho,1}(\nu)|=
 |\cos((\gamma-\lambda)\log2/2)
   \cos((\gamma-\lambda)\log3/2)|\).

First choose \(H\) to make the actual complete profile tail small,
uniformly in \(k\); then choose \(k\) for the finite-height term.
There is no appeal to a finite-zero interpolation while leaving its
complexity-dependent tail unpaid. This estimate supplies no uniform
effective rate in \(F\), the taper parameters, or zero separation.

### 13.5. Approaching the individual order-m cost inside the fixed Gevrey class

For every integer \(m\ge1\) and every \(\varepsilon>0\), there is
a fixed admissible real Gevrey taper of any prescribed order
\(1<\sigma<2\) for which

\[
                  m^2\le C_m(w)<m^2+\varepsilon.
 \tag{AD14}
\]

This is the individual-order approximation in Note 12 §11; a direct
construction verifies the required class. Fix a normalized Gevrey cutoff
\(\chi\), zero on \(( -\infty,1/2]\) and one on \([1,\infty)\),
and put

\[
 w_{m,\delta}(u)=(1-u)^m\chi((1-u)/\delta),\quad 0\le u\le1.
 \tag{AD15}
\]

For fixed \(0<\delta<1/2\), this is normalized at zero, flat near one,
and has a compact Gevrey extension using the fixed left cutoff of
Note 12. For the limiting polynomial \(w_m=(1-u)^m\), the function
\(p_{m,w_m}\) is the degree-\((m-1)\) endpoint reproducing kernel
on \([0,1]\); its squared norm is \(m^2\). One can verify this
directly: its degree is \(m-1\), and integration by parts retains the
moments \(\int_0^1u^jp_{m,w_m}(u)\,du=\delta_{j0}\) for
\(0\le j<m\). The shifted Legendre orthonormal basis gives squared
endpoint norm \(\sum_{j=0}^{m-1}(2j+1)=m^2\).

The \(m\)-th derivative of
\(u^{m-1}(w_{m,\delta}-w_m)\) is bounded independently of \(\delta\)
and supported in an interval of length \(\delta\). Leibniz's rule
pays every cutoff derivative by the corresponding factor
\((1-u)^m\). Thus
\(\|p_{m,w_{m,\delta}}-p_{m,w_m}\|_2^2=O_{m,\chi}(\delta)\).
Both functions have the same moment constraints. Orthogonality to the
reproducing kernel therefore gives the stronger exact comparison

\[
 C_m(w_{m,\delta})-m^2
   =\|p_{m,w_{m,\delta}}-p_{m,w_m}\|_2^2
   =O_{m,\chi}(\delta),
 \tag{AD16}
\]

which proves (AD14). No parameter in this approximation is varied with
\(N\) in the argument below.

### 13.6. Ordered choices, real coefficients, and the sharp infimum

Fix \(\varepsilon>0\) and any one admissible baseline \(w_0\).
Its complete profile sum is finite. Choose a finite conjugation-invariant
set \(F\) such that
\(\sum_{\nu\notin F}C_{m_\nu}(w_0)/|\nu|^2<\varepsilon\).
Next choose a fixed taper \(w_\rho\) as in (AD14) at every target,
using the same taper at conjugate targets, so that

\[
 \sum_{\rho\in F}\frac{C_{m_\rho}(w_\rho)-m_\rho^2}{|\rho|^2}
                                    <\varepsilon.
\]

Equation (AD12) then gives \(S_\infty\le K+2\varepsilon\).
With these choices fixed, (AD13) supplies a finite \(k\) such that
\(S_k\le K+3\varepsilon\). For this one fixed polynomial mixture,
take \(N\to\infty\) in (AD10). The infimum comparison gives

\[
       \limsup_{N\to\infty}(\log N)d_N^2
          \le S_k\le K+3\varepsilon.
 \tag{AD17}
\]

Finally let \(\varepsilon\downarrow0\) and combine with Burnol's
lower bound. This proves (AD2). The choice order is
\(F\), tapers, finite height for (AD13), \(k\), then
\(N\to\infty\), then \(\varepsilon\downarrow0\). In particular
there is no unproved uniform interchange of the taper or peak degree
with \(N\), and no shortening of the length budget.

The coefficients can be real without an additional projection. Indeed
\(P_{\bar\rho,k}(s)=\overline{P_{\rho,k}(\bar s)}\); pair conjugate
targets with the same real taper in (AD9). Their coefficient sums are
real, and the baseline is real. Its constant coefficient is one because
each difference \(V_{n,w_\rho}-V_{n,w_0}\) has zero constant coefficient.

### 13.7. What this changes, and what it does not

The common-taper simple/double tradeoff of Note 12 §11 remains valid for
that class. It is not a lower gap for the full Dirichlet-polynomial
infimum: the bounded multipliers select different profiles at different
zeros and pay the entire remaining sum through (AD11)--(AD13).

Under RH the linear zero mass is
\(Z=\sum_{\rho\ {\rm distinct}}m_\rho/|\rho|^2
 =2+\gamma_E-\log(4\pi)\). The constant just obtained satisfies

\[
 K-Z=\sum_{\rho\ {\rm distinct}}
              \frac{m_\rho(m_\rho-1)}{|\rho|^2}.
 \tag{AD18}
\]

An order-m conjugate pair at ordinates \(\pm\gamma\) contributes
exactly \(2m(m-1)/(\gamma^2+1/4)\) to this excess. The complete
upper constant therefore increases by the same multiplicity cost as
the lower constant. This proves neither an RH-only upper \(Z\), nor
simplicity, nor convergence of the prescribed original linear taper.
The missing opposing arithmetic estimate remains missing.

The controls previously constructed do not satisfy all the unchanged
Möbius/zeta convolution and exact completion premises used in this note.
This argument does not combine their different preservation lists or
claim that the present finite mixtures preserve the coefficients of a
single original Möbius taper. They are explicit admissible polynomials
for the full infimum, which is exactly the class stated in (AD1).


## 14. Exact finite filters and the sharp cost of resolving a small gap

20 October 2026 continuation, from checkpoint `5f7d894`. Prepared for Edward
Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
Separate same-model checks are in Review 16 §10. The new quantity is
filter length: exact cancellation at a neighboring ordinate of gap
\(\Delta\) is achievable with
\(\log M\le\pi/|\Delta|+\log2\) for small gaps, and every selector
bounded by one requires \(\log M\ge\pi/|\Delta|\).
This replaces the preceding binomial construction's quadratic inverse-gap
cost. The complete profile tail remains paid. It does not improve the
multiplicity-squared constant or supply a simplicity margin.

### 14.1. A three-term polynomial with an exact prescribed boundary zero

For \(0<\theta<\pi\), put \(k=\lfloor\pi/\theta\rfloor\) and define
\[
 B_\theta(z)=
 \frac{\sin\theta-\sin((k+1)\theta)z^k+\sin(k\theta)z^{k+1}}
      {\sin\theta-\sin((k+1)\theta)+\sin(k\theta)}.
 \tag{FR1}
\]
Its coefficients are nonnegative and sum to one: \(k\theta\le\pi<
(k+1)\theta\le\pi+\theta<2\pi\), and the constant coefficient is
positive. The identity
\[
 -\sin((k+1)\theta)e^{ik\theta}
       +\sin(k\theta)e^{i(k+1)\theta}=-\sin\theta
\]
proves
\[
 B_\theta(1)=1,\quad B_\theta(e^{\pm i\theta})=0,\quad
 |B_\theta(z)|\le1\ (|z|\le1),\quad
 \deg B_\theta\le\pi/\theta+1.
 \tag{FR2}
\]
If \(k\theta=\pi\), this reduces to \((1+z^k)/2\). At
\(\theta=\pi\), use \((1+z)/2\).

Let \(F\subset G\) be finite sets of distinct critical-line points,
with \(F\ne\varnothing\). For \(\rho=1/2+i\gamma\ne\nu=1/2+i\lambda\),
choose \(p_{\rho\nu}\in\{2,3\}\) maximizing
\(|1-p^{i(\gamma-\lambda)}|\), with a fixed tie rule. Let
\(\theta_{\rho\nu}=|\operatorname{Arg}p_{\rho\nu}^{i(\gamma-\lambda)}|\).
At least one phase is nonzero by the irrationality of \(\log2/\log3\);
hence \(0<\theta_{\rho\nu}\le\pi\). Put
\[
 P_{\rho,G}(s)=\prod_{\nu\in G\setminus\{\rho\}}
 B_{\theta_{\rho\nu}}\bigl(p_{\rho\nu}^{\rho-s}\bigr).
 \tag{FR3}
\]
These finite ordinary Dirichlet polynomials are bounded by one for
\(\Re s\ge1/2\), equal one at their target, and vanish at every other
point of \(G\). If \(d_{\rho\nu}=\deg B_{\theta_{\rho\nu}}\), their
common length can be bounded by the integer
\[
 M_G=\max_{\rho\in F}\prod_{\nu\in G\setminus\{\rho\}}
                    p_{\rho\nu}^{d_{\rho\nu}},\qquad
 \log M_G\le\max_{\rho\in F}\sum_{\nu\in G\setminus\{\rho\}}
                     (\pi/\theta_{\rho\nu}+1)\log p_{\rho\nu}.
 \tag{FR4}
\]
Empty products are one. This pays every finite node; simultaneous
near-returns of the two phases at distant ordinates can make the sum
large. No bound in terms of the nearest ordinary zero gap alone is
asserted.

The coefficients are nonnegative in the shifted variable used in
(FR1), not necessarily in the ordinary Dirichlet expansion. For
conjugation-invariant \(F,G\), the stated phase and prime choices give
\(P_{\bar\rho,G}(s)=\overline{P_{\rho,G}(\bar s)}\). Pairing conjugate
targets with the same real taper therefore produces real coefficients
in the final mixture, as in §13.

### 14.2. Exact finite-height profiles with the complete remaining tail

Now assume RH, take \(F,G\) from the actual distinct zeros, and fix
the baseline \(w_0\) and finitely many tapers \(w_\rho\) in §13.
With \(n=\lfloor N/M_G\rfloor\), use
\[
 D_{N,G}=V_{n,w_0}+\sum_{\rho\in F}P_{\rho,G}
                         (V_{n,w_\rho}-V_{n,w_0}).
 \tag{FR5}
\]
Its length is at most \(N\). For each fixed \(G\), the actual mixed
limit (AD5) gives
\[
 S_G=\lim_{N\to\infty}(\log N)E(D_{N,G})
    =\sum_{\nu\ {\rm distinct}}\frac{\|q_{\nu,G}\|_2^2}{|\nu|^2},
 \quad
 q_{\nu,G}=p_{m_\nu,0}+\sum_{\rho\in F}P_{\rho,G}(\nu)
                              (p_{m_\nu,\rho}-p_{m_\nu,0}).
 \tag{FR6}
\]
On \(G\), this is exactly the chosen profile at targets and the baseline
at other nodes. Write \(S_F\) for the comparison sum in (AD12), and
\(J=|F|\). The same global domination as (AD11) proves
\[
 |S_G-S_F|\le4(J+1)^2
       \sum_{j\in\{0\}\cup F}\sum_{\nu\notin G}
                           \frac{C_{m_\nu}(w_j)}{|\nu|^2}.
 \tag{FR7}
\]
There is no finite-height attenuation term. On \(G\) the difference
is zero; outside \(G\), the mixed cost is bounded by
\(2(J+1)^2\sum_j C_{m_\nu}(w_j)\), and adding the baseline cost is
covered by (FR7). Its constant is independent of the number or degrees
of the factors in (FR3). Every series is summable by ST.

For \(G=\{\nu:|\Im\nu|\le H\}\supset F\), (ST2) and the compact
limits bound the right side by
\(O_{F,\{w_j\},\epsilon}(H^{\sigma-2+\epsilon})\), for
\(0<\epsilon<2-\sigma\) and a common fixed \(1<\sigma<2\).
Keep \(F\) and its tapers fixed while exhausting \(G\).
For every chosen finite \(G\), take the \(N\) limit first.
This gives another fully paid construction of the same infimum constant
\(K\). The length estimate does not supply uniformity for \(G_N\),
an effective \(N\) threshold, or a smaller local cost.

### 14.3. A sharp lower bound for all selectors bounded by one

No RH assumption is needed here. Let
\[
 P(s)=\sum_{n\le M}a_n n^{-s},\quad
 \sup_{y\in\mathbb R}|P(1/2+iy)|\le1,\quad
 P(\rho)=1,\quad |P(\rho+i\Delta)|\le\varepsilon,\quad0\le\varepsilon<1.
\]
Then
\[
 \boxed{|\Delta|\log M\ge2\arccos\varepsilon.}
 \tag{FR8}
\]
The coefficients may be arbitrary complex numbers. If the nonzero
indices range from \(n_{\min}\) to \(n_{\max}\), the same bound holds
with \(\log(n_{\max}/n_{\min})\) in place of \(\log M\).

For the proof, assume \(\Delta>0\), put \(B=\log M\), and center the
frequencies:
\[
 g(z)=e^{iBz/2}P(\rho+iz),\qquad
 r(z)=\tfrac12\bigl(g(z)+\overline{g(\bar z)}\bigr).
\]
The function \(r\) is real entire of exponential type at most \(B/2\),
is bounded by one on the real axis, and has \(r(0)=1\) and
\(r(\Delta)\le\varepsilon\). The sharpened Bernstein inequality
\[
 |r'(x)|\le(B/2)\sqrt{1-r(x)^2}
\]
is proved in [Redheffer, §5, Theorem 11, pp. 832–833](https://msp.org/pjm/1953/3-4/pjm-v3-n4-p11-s.pdf).
The primary source's strict growth/boundary formulations are handled by
enlarging the type slightly and dividing \(r\) by \(1+\eta\), then
taking limits. Applying the inequality to \(r/(1+\eta)\) makes
\(\arccos(r/(1+\eta))\) Lipschitz with constant \(B/2\). Integrate
from zero to \(\Delta\), let \(\eta\downarrow0\), and use monotonicity
of arccos. This proves (FR8) without assuming monotonicity of \(r\).

For \(0<|\Delta|<\pi/\log2\), choose \(p=2\) in the single-neighbor
construction. Its principal phase is \(\theta=|\Delta|\log2\).
Equations (FR1)–(FR2) and (FR8) give the matching exact-zero bounds
\[
 \boxed{\frac{\pi}{|\Delta|}\le
       \inf_{\substack{P(\rho)=1,\ P(\rho+i\Delta)=0\\
                         \sup_{\Re s=1/2}|P(s)|\le1}}
                         \log(\operatorname{length}P)
       \le\frac{\pi}{|\Delta|}+\log2.}
 \tag{FR9}
\]
This is a two-point result, not an optimality statement for the full
finite family in (FR4). For comparison, the original binomial peak has
\[
 -\log|P_{\rho,1}(\rho+i\Delta)|
     =\tfrac18\bigl((\log2)^2+(\log3)^2\bigr)\Delta^2
         +O(\Delta^4).
\]
For any fixed \(0<\varepsilon<1\), its log-length is therefore of
order \(|\Delta|^{-2}\) to reach modulus \(\varepsilon\).
The exact construction improves that power and needs no attenuation
tolerance for the specified neighboring node.

### 14.4. The cost of allowing a larger supremum

If instead \(\sup_{\Re s=1/2}|P|\le A\), \(A\ge1\), the same
centered-real-part proof, divided by \(A\), gives
\[
 |\Delta|\log M\ge
 2\left[\arccos(\varepsilon/A)-\arccos(1/A)\right].
 \quad\text{For }\varepsilon=0:\quad
 |\Delta|\log M\ge2\arcsin(1/A).
 \tag{FR10}
\]
In particular, exact cancellation with \(0<|\Delta|\log M\le\pi\)
requires \(A\ge\csc(|\Delta|\log M/2)\). This is sharp even for a
length-\(p\) Dirichlet polynomial. For a prime \(p\), \(B=\log p\),
and \(0<\Delta B\le\pi\), set
\[
 Q(s)=\frac{p^{\rho-s}-e^{-i\Delta B}}{1-e^{-i\Delta B}}.
 \qquad
 e^{iBx/2}Q(\rho+ix)
       =\frac{\sin((\Delta-x)B/2)}{\sin(\Delta B/2)}.
 \tag{FR11}
\]
It has target value one, neighboring value zero, and boundary supremum
\(A=\csc(\Delta B/2)\). Thus a growing supremum can avoid the unit-bound
length threshold, but must be at least asymptotic to
\(2/(|\Delta|\log M)\) when that product tends to zero.
The separate estimate \(|Qe|^2\le A^2|e|^2\) then carries an
\(A^2\) allowance. This is a cost of that supremum-based payment,
not a lower bound on the actual integrated error.

### 14.5. Consequence at a heat collision, with the original coordinates

Note 15 (HR3) uses
\(\mathcal F_t(z)=8H(t,-2iz)\) and
\(\partial_t\mathcal F_t=\tfrac14\partial_z^2\mathcal F_t\).
Under RH, at an order-\(m\) initial zero \(i\gamma\), the actual emerging
ordinates satisfy
\[
 \gamma_j(t)=\gamma+\sqrt{t/2}\,\lambda_j+O(t),\qquad
 \mathrm{He}_m(\lambda_j)=0,\quad
 \lambda_1<\cdots<\lambda_m.
 \tag{FR12}
\]
This follows from the joint analytic expansion there and simplicity
of the Hermite roots. The factor \(1/\sqrt2\) retains the physical
coordinate \(x=2\gamma\).

Suppose a selector bounded by one isolates branches \(j<k\) with
fixed attenuation \(0\le\varepsilon<1\), using length \(M_N\le N^\vartheta\),
where \(\vartheta>0\) is fixed, at times \(t_N\downarrow0\).
Writing \(L=\log N\) and \(\delta_{jk}=\lambda_k-\lambda_j\), (FR8)
implies
\[
 \liminf_N\sqrt{t_N}\,L\ge
       \frac{2\sqrt2\,\arccos\varepsilon}
            {\vartheta\delta_{jk}}.
 \tag{FR13}
\]
In particular \(t_NL^2\to0\) is impossible for this isolation task,
even when the entire length budget \(M_N\le N\) is used.
For a double cluster, \(\delta_{12}=2\). At
\(t_N=v/L^2\), length at most \(N\) consequently requires
\(v\ge2(\arccos\varepsilon)^2\); exact cancellation requires
\(v\ge\pi^2/2\).

These bounds concern filters placed at actual heat-root ordinates.
They do not transfer ST from the original zeta function to a
heat-deformed function, or prove a bound for its polynomial infimum.
Assigning the same taper to both emerging simple roots need not isolate
them. Allowing a growing selector supremum instead invokes (FR10)
and requires a separate complete-norm payment. The boundary phase and
mixed heat-energy identities retain their compatible multiplicity cost;
no original multiple zero has been excluded.

## 15. A split double zero at finite Dirichlet resolution

20 October 2026, from checkpoint `ab3afa0`. Prepared for Edward Baker
with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
Separate same-model internal derivation and review; no specialist
validation or novelty claim.

**Gain and class.** For an original double zero under RH, the actual
Möbius approximant against the heat-deformed completion has an exact
norm limit on a fixed isolated neighborhood at heat time
\(t=v/(\log N)^2\). The sharp local coefficient, optimized over fixed
real normalized flat Gevrey tapers, is an explicit nonmonotone function
of \(a=\sqrt{v/2}\). This is a local approximation result. It does not
transfer ST to a heat-deformed function or estimate the complete
heat-deformed norm. In particular, Note 15's monotone ratio-energy
transition cannot be assigned to this different approximation cost.
The [gain-before-expansion rule](../../../../../../../avoid/20_volume_without_a_gain.md)
and [complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
apply; the changed quantity is the exact finite-separation coefficient.

### 15.1. The actual compact-neighborhood transfer

Assume RH and an exact double zero \(\rho=1/2+i\gamma\) of the
original zeta function. Choose a fixed sufficiently small \(r>0\)
so the disk \(|s-\rho|\le4r\) has no other zero and the completion
factor \(\mathcal A\) is analytic and nonzero there. Use Note 15's
normalization
\[
 \mathcal F_t(z)=8H(t,-2iz),\qquad
 \partial_t\mathcal F_t=\tfrac14\partial_z^2\mathcal F_t,\qquad
 Z_t(s)=\frac{\mathcal F_t(s-1/2)}{\mathcal A(s)},\quad Z_0=\zeta.
 \tag{HD1}
\]
The symbol \(Z_t\) denotes a local analytic quotient here; it is not
assigned a Dirichlet series or Euler product. Fix an admissible real
taper \(w\) from ST, set \(L=\log N\), and keep \(v\ge0\) fixed.
Define
\[
 f_w(u)=u w(u),\quad a=\sqrt{v/2},\quad
 p_{a,w}(u)=-f_w''(u)-a^2f_w(u),\quad
 C_a(w)=\int_0^1 |p_{a,w}(u)|^2\,du.
 \tag{HD2}
\]
Then the actual local norm satisfies
\[
 \boxed{\frac1{2\pi}\int_{-r}^{r}
 \frac{|1-Z_{v/L^2}(\rho+iy)V_{N,w}(\rho+iy)|^2}
      {1/4+(\gamma+y)^2}\,dy
 =\frac{C_a(w)}{L|\rho|^2}
       +O_{\rho,w,v}\!\left(\frac{\log L}{L^2}\right).}
 \tag{HD3}
\]
For \(v>0\), both newly split roots lie inside this fixed neighborhood for large N.
One original ordinate is treated in (HD3); its conjugate neighborhood
has the same coefficient and is counted separately when both are used.

Here is the transfer proof, including the fixed annulus. Write
\(1/\zeta(\rho+q)=b_2q^{-2}+b_1q^{-1}+G(q)\), with
\(b_2=2/\zeta''(\rho)\). The exact original convolution and its
paid remote tail in CH2--CH6 give, uniformly for \(q=iy\), \(|y|\le r\),
\[
 V_{N,w}(\rho+q)=b_2 L^2 A_2(Lq)+b_1 L A_1(Lq)+G(q)+O(L^{-1}),
 \quad A_j(z)=\frac1{(j-1)!}\int_0^1u^{j-1}w(u)e^{-zu}\,du.
 \tag{HD4}
\]
Integration by parts retains the endpoint at zero and gives
\(|A_1(ix)|\ll_w(1+|x|)^{-1}\) and
\(|A_2(ix)|\ll_w(1+x^2)^{-1}\). In particular \(V_{N,w}\ll_{\rho,w}L^2\)
throughout this fixed neighborhood.

Joint analyticity of the unchanged theta source gives the uniform
compact Taylor expansion
\[
 Z_t(\rho+q)-\zeta(\rho+q)=\frac t4 B(q)+O_\rho(t^2),\qquad
 B(q)=\frac{(\mathcal A\zeta)''(\rho+q)}{\mathcal A(\rho+q)}
       =\frac2{b_2}+O_\rho(q).
\]
Substitute \(t=v/L^2\) into this expansion and (HD4). The leading
product is \(a^2 A_2(Lq)\). All remaining products are \(O_{\rho,w,v}(L^{-1})\):
\(|q A_2(iLy)|\ll L^{-1}\), the \(b_1 L A_1\) term pays one
extra power of L, and \(t^2 V_{N,w}=O(L^{-2})\). Together with CH9,
\[
 1-Z_{v/L^2}(\rho+iy)V_{N,w}(\rho+iy)
   =\int_0^1 p_{a,w}(u)e^{-iLyu}\,du+O_{\rho,w,v}(L^{-1}).
 \tag{HD5}
\]
The profile decays as \(O_{w,v}((1+|Ly|)^{-1})\). The cross term,
weight variation and omitted Fourier tail are therefore paid exactly
as in CH11--CH13, giving (HD3). This proves the whole fixed-neighborhood
statement, not just convergence on bounded rescaled intervals.

### 15.2. The sharp coefficient and its flat-taper realization

For \(a>0\), integration by parts using
\(f_w(0)=0\), \(f_w'(0)=1\), and \(f_w(1)=f_w'(1)=0\) yields
\[
 \int_0^1p_{a,w}(u)e^{iau}\,du
 =\int_0^1p_{a,w}(u)e^{-iau}\,du=1.
 \tag{HD6}
\]
Among real \(p\in L^2(0,1)\) satisfying these two conditions, the
minimum norm is obtained in the span of \(\cos(au)\), \(\sin(au)\).
Their Gram matrix has entries
\[
 A=\tfrac12+\frac{\sin(2a)}{4a},\qquad
 B=\frac{\sin^2a}{2a},\qquad
 D=\tfrac12-\frac{\sin(2a)}{4a},\qquad
 AD-B^2=\frac14\left(1-\frac{\sin^2a}{a^2}\right)>0.
\]
Thus the minimizing density is
\(p_*=(D\cos(au)-B\sin(au))/(AD-B^2)\), and
\[
 \boxed{\quad
 \inf_w C_a(w)=Q(a)
 :=\frac{2\left(1-\frac{\sin(2a)}{2a}\right)}
          {1-\left(\frac{\sin a}{a}\right)^2},\qquad a>0.
 \quad}
 \tag{HD7}
\]
The infimum is over the declared real flat Gevrey tapers, with no
positivity or monotonicity requirement on w. To prove sharpness in
that class, solve
\(f_*''+a^2 f_*=-p_*\), \(f_*(0)=0\), \(f_*'(0)=1\).
The two moments imply \(f_*(1)=f_*'(1)=0\), directly from the sine
propagator formula. The solution is analytic, and \(f_*(u)/u\)
has a removable singularity at zero with value one.

Multiply \(f_*\) by a fixed-order Gevrey cutoff equal to one before
\(1-\eta\) and flatly zero near one. Set \(w_\eta=f_\eta/u\).
The resulting density still satisfies (HD6) exactly. Since
\(f_*(u)=O_a((1-u)^2)\) and \(f_*'(u)=O_a(1-u)\),
\(p_{a,w_\eta}-p_*\) is bounded by \(O_a(1)\) and supported
in an interval of length \(\eta\). It is orthogonal to the two
Gram vectors, so
\[
 C_a(w_\eta)=Q(a)+\|p_{a,w_\eta}-p_*\|_2^2
            =Q(a)+O_a(\eta).
\]
An independent negative-side Gevrey cutoff extends \(w_\eta\)
to the compact normalized class in ST, with any fixed order between
one and two. Fix a, the cutoff and \(\eta\) before the N limit;
only then let \(\eta\) tend to zero. No moving-taper uniformity is
being inferred from (HD3).

### 15.3. The exact failure of monotonicity and its scope

For each fixed admissible taper, integration by parts gives the exact
identity
\[
 C_{\sqrt{v/2}}(w)
   =C_0(w)-v\|f_w'\|_2^2+\frac{v^2}{4}\|f_w\|_2^2.
 \tag{HD8}
\]
Both norms are positive. Thus this fixed-taper coefficient decreases
initially, has its unique minimum at
\(v=2\|f_w'\|_2^2/\|f_w\|_2^2\), and then increases. This is
an identity for the coefficient after the fixed-v limit in (HD3),
not a differentiation of its remainder or a joint limit with v growing.

The confluent and separated limits are
\[
 Q(a)=4-\tfrac4{15}a^2+O(a^4)\quad(a\downarrow0),\qquad
 Q(a)=2-\frac{\sin(2a)}a+O(a^{-2})\quad(a\to\infty).
\]
At a=0, the original double-zero problem retains both
\(\int p=1\) and \(\int up=0\), whose minimizer is \(4-6u\)
and cost is four. Literally substituting a=0 into the two identical
conditions in (HD6) would lose the derivative condition and have cost
one; that is not the confluent limit.

Exact values show that Q is not monotone:
\[
 Q(\pi)=2,\qquad
 Q(5\pi/4)=2-\frac{4(5\pi-4)}{25\pi^2-8}<2,\qquad
 Q(3\pi/2)=\frac2{1-4/(9\pi^2)}>2.
 \tag{HD9}
\]
At \(v=25\pi^2/8\), a fixed admissible taper can therefore have
the actual local coefficient in (HD3) strictly below two. The
reduction comes from finite-resolution cross terms, retained in
the Gram matrix. It violates no original-zeta lower bound: the
target function varies with N, only a fixed neighborhood is measured,
and this local statement identifies no complete heat-family infimum.
Section 16 now proves that the literal unchanged full norm is infinite
for every nonzero finite polynomial at each positive time in its range.

This rejects a monotone interpolation claim for this precise optimized
local approximation class. It does not contradict Note 15's distinct
monotone completed-ratio coefficient, exclude a multiple zero, or
supply BW09's strict phase surplus. The elementary Gram calculation
and Hermite separation are reusable in BW09; (HD3) uses the original
Möbius convolution under RH and cannot simply be transplanted to
an unknown positive threshold. The detailed local continuation remains in the notes; the canonical
brief now also records the global obstruction proved in §16.

## 16. Positive heat time leaves the original weighted Dirichlet approximation space

20 October 2026, from checkpoint `79e76cf`. Prepared for Edward Baker with substantial LLM assistance.
Actual model **gpt-6-astra**, reasoning effort **ultra**. Same-model
derivation from an explicitly checked primary asymptotic; no specialist
review or novelty claim. This is a scoped obstruction to an unchanged
global norm, not an event-exclusion criterion.

**Result.** For every fixed \(0<\tau\le1/2\) and every nonzero finite
Dirichlet polynomial \(D\),
\[
 \boxed{\quad \frac1{2\pi}\int_{\mathbb R}
 \frac{|1-Z_\tau(1/2+iu)D(1/2+iu)|^2}{1/4+u^2}\,du=\infty,\quad}
 \qquad Z_\tau(s)=\frac{8H_\tau(-2i(s-1/2))}{\mathcal A(s)}.
 \tag{GH1}
\]
Here \(\mathcal A(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2\) is the
**unchanged** completion factor. This assertion is unconditional. Its
stated heat-time range is exactly the range of the primary proposition
used below; a blanket extension to \(\tau>1/2\) is not asserted.

### 16.1. The checked primary input includes the real axis

[Polymath15, Proposition 9.1(i), equations (6)–(10)](https://arxiv.org/html/1904.12438v2#S9)
was checked in both HTML and the [PDF, p.56](https://arxiv.org/pdf/1904.12438v2).
For \(0<\tau\le1/2\), it implies at real \(x\ge\exp(C/\tau)\)
\[
 H_\tau(x)=2\Re M_\tau((1+ix)/2)
                 +O(x^{-c\tau})|M_\tau((1+ix)/2)|,
 \quad M_\tau(s)=e^{\tau\alpha(s)^2/4}M_0(s),                 \tag{GH2}
\]
where \(M_0\) is the leading Stirling expression for
\(\mathcal A/8\), and
\[
 \alpha(s)=(\log M_0)'(s)
       =\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi}.
                                                               \tag{GH3}
\]
The proposition has no RH hypothesis. It estimates both conjugate
carriers; replacing them by a single nonoscillating lower bound on the
real axis would be invalid.

### 16.2. Carrier and phase in the original zeta coordinate

Put \(s_u=1/2+iu\), so the heat coordinate is \(x=2u\). Choose the
continuous phase \(\theta_\tau(u)=\Im\log M_\tau(s_u)\) for large
positive \(u\), and define
\[
 q_\tau(u)=\frac{8|M_\tau(s_u)|}{|\mathcal A(s_u)|},\qquad
 h_\tau(u)=\frac{H_\tau(2u)}{|M_\tau(s_u)|}.
\]
Then \(|Z_\tau(s_u)|=q_\tau(u)|h_\tau(u)|\) exactly, and (GH2)
gives
\[
 h_\tau(u)=2\cos\theta_\tau(u)+O(u^{-c\tau}).                 \tag{GH4}
\]
From (GH3),
\(\alpha(s_u)=\tfrac12\log(u/(2\pi))+i\pi/4+O(u^{-1})\).
The [sectorial Stirling formula](https://dlmf.nist.gov/5.11#E3)
gives \(8M_0(s_u)/\mathcal A(s_u)=1+O(u^{-1})\), and hence
\[
 \log q_\tau(u)=\frac\tau{16}\log^2\frac{u}{2\pi}
             -\frac{\tau\pi^2}{64}
             +O_\tau\!\left(\frac{\log u}{u}\right).
                                                               \tag{GH5}
\]
In particular, uniformly on \(T\le u\le2T\) for sufficiently large
\(T\),
\[
 \inf q_\tau(u)^2\gg_\tau
                   \exp\left(\frac\tau8\log^2\frac{T}{2\pi}\right).
                                                               \tag{GH6}
\]

Phase derivatives must not be obtained by differentiating an unspecified
error term. Differentiate (GH3) and the exact definition of \(M_\tau\)
instead:
\[
 \theta_\tau'(u)=\Re\{\alpha(s_u)
                      +(\tau/2)\alpha(s_u)\alpha'(s_u)\}
       =\tfrac12\log(u/(2\pi))+O_\tau(u^{-1}),
\]
\[
 \theta_\tau''(u)=\Re\{i\alpha'(s_u)
       +(i\tau/2)[\alpha'(s_u)^2+\alpha(s_u)\alpha''(s_u)]\}
       =O_\tau(u^{-1}).                                      \tag{GH7}
\]
These estimates are uniform on each sufficiently high dyadic interval.

### 16.3. A finite Dirichlet polynomial cannot follow the increasing oscillation

Write \(D(s)=\sum_{n\le M}a_n n^{-s}\), collect equal frequencies,
and put \(d_n=a_n/\sqrt n\),
\(A_D=\sum|d_n|^2>0\). Elementary finite-sum integration gives
\[
 \int_T^{2T}|D(s_u)|^2du=A_DT+O_D(1).                         \tag{GH8}
\]
For each fixed frequency \(\omega=\log(n/m)\), the phase
\(2\theta_\tau(u)+\omega u\) has derivative at least
\(\tfrac12\log T\) in absolute value once \(T\) is sufficiently
large depending on \(M,\tau\). Its second derivative is
\(O_\tau(T^{-1})\). A single integration by parts therefore yields
\[
 \int_T^{2T}e^{i(2\theta_\tau(u)+\omega u)}du
                         =O_{\tau,M}(1/\log T).
\]
Expanding \(|D|^2\) and using \(\cos^2\theta=(1+\cos2\theta)/2\),
\[
 \int_T^{2T}|D(s_u)|^2\cos^2\theta_\tau(u)\,du
                  =\tfrac12 A_DT+O_{D,\tau}(1).              \tag{GH9}
\]
No equidistribution assertion about a moving family of polynomials is
needed: the polynomial is fixed while the height goes to infinity.

Write (GH4) as \(h=2\cos\theta+e\). The elementary inequality
\(|b+e|^2\ge\tfrac12|b|^2-|e|^2\), together with (GH8)–(GH9),
shows
\[
 \int_T^{2T}|D(s_u)|^2|h_\tau(u)|^2du
       \ge A_DT+O_{D,\tau}(1)-O_{D,\tau}(T^{1-2c\tau})
       \ge\tfrac12 A_DT                                   \tag{GH10}
\]
for all sufficiently large \(T\). The oscillatory error is thus paid
without a false pointwise lower estimate for \(H_\tau\).

### 16.4. Divergence and the precise consequence for the local heat experiment

Factor (GH6) out of the **nonnegative actual squared integrand** before
applying (GH10). Since \((1/4+u^2)^{-1}\gg T^{-2}\) on the block,
\[
 \frac1{2\pi}\int_T^{2T}
     \frac{|Z_\tau(s_u)D(s_u)|^2}{1/4+u^2}\,du
 \gg_{D,\tau}\frac1T
       \exp\left(\frac\tau8\log^2\frac{T}{2\pi}\right)
                    \longrightarrow\infty.                 \tag{GH11}
\]
This is a block lower bound, not an asymptotic for the whole integral.
Finally \(|1-z|^2\ge\tfrac12|z|^2-1\) subtracts only \(O(1/T)\)
on the block. It proves (GH1).

The zero polynomial has residual norm one, so for each length bound
N the extended-valued infimum in this unchanged norm is one; every nonzero polynomial has infinite norm. If normalization forces
a nonzero polynomial, no finite competitor exists in this norm. This is
not an ordinary Hilbert-space approximation distance: the nonzero trial
vectors lie outside the weighted space.

In particular fix \(v>0\). For every sufficiently large but finite
\(N\), the time \(\tau_N=v/(\log N)^2\) lies in \((0,1/2]\).
The original normalized Möbius taper has constant coefficient one and
is nonzero. Its **full** heat-deformed residual norm is therefore
infinite at that \(N\), despite the finite compact-neighborhood
asymptotic in Note16 §15. The height threshold in the proof may grow
extremely rapidly with \(N\); an infinite-height integral still sees it.
This proves an actual obstruction to transferring ST to that target and
weight, rather than merely leaving the needed uniform bound unproved.
It does not affect the original time-zero ST theorem, the compact HD
calculation, or completed horizontal-ratio energies with their own
normalization.


### 16.5. Sharp logarithmic Gaussian damping threshold

Fix \(0<\tau\le1/2\), a nonzero finite D, and \(b\ge0\). For
\(|u|\ge U_0>2\pi\), change the weight to
\[
 \omega_b(u)=\frac{\exp[-b\log^2(|u|/(2\pi))]}{1/4+u^2},
\]
with any positive bounded measurable continuation on the compact interval.
Then
\[
 \boxed{\int_{\mathbb R}|1-Z_\tau(1/2+iu)D(1/2+iu)|^2
                  \omega_b(u)\,du<\infty
        \quad\Longleftrightarrow\quad b\ge\tau/8.}
 \tag{GH12}
\]
Indeed the exact carrier estimate (GH5), with
\(\ell(u)=\log(u/(2\pi))\), gives
\[
 q_\tau(u)^2e^{-b\ell(u)^2}
 =\exp\left\{(\tau/8-b)\ell(u)^2-\tau\pi^2/32
                 +O_\tau(\log u/u)\right\}.
 \tag{GH13}
\]
For \(b\ge\tau/8\) this is bounded, including equality. Since h in
(GH4) and every finite D are bounded on the critical line, the weighted
squared signal is \(O_{\tau,D,b}(u^{-2})\). The target term is also
integrable, and \(|1-z|^2\le2+2|z|^2\) pays their sum.

For \(b<\tau/8\), take the minimum of the **combined** factor in
(GH13) on [T,2T] before using (GH10). The signal's weighted block mass
is at least a positive constant times
\(T^{-1}\exp[(\tau/8-b)\log^2(T/(2\pi))]\), which tends to infinity.
Subtracting the target costs only O(1/T). This proves the other direction.
Evenness of H and conjugacy of the completion modulus give the same upper
bound on the negative tail; D need not have real coefficients. On the
compact interval the completion is nonzero on the critical line, so the
bounded weight and continuous numerator give a finite contribution.

This sharp threshold defines a different norm. It provides no uniform
estimate as the heat time, weight or polynomial varies, and does not
transfer the original Burnol lower bound or ST to that norm. The zero
polynomial is excluded from (GH12), since its error is finite for every
b. The earlier infimum value one concerns only the original normalized
weight in (GH1).

### 16.6. Control screen and BW09 scope

The quantified gain is divergence of the full unchanged norm, the exact
extended-real infimum one, and the damping threshold \(\tau/8\). The
[result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
set its scope. The source-identity premise in the imported asymptotic is
the original theta heat flow. Each screened family changes that source:
Euler-factor controls add translates; weighted-square controls change
its square coefficients; reflected and positive-primitive controls use
different sources. None is silently assigned the original Polymath
asymptotic. The elementary finite-frequency argument applies to any
function satisfying the same displayed carrier bounds and is compatible
with collisions; it is not intended to reject those controls.

Because this obstruction is unconditional, BW09 also cannot use this
literal original-completion norm for its positive heat times in the
stated interval. Its contour and completed-ratio methods use different
objects and are unaffected. No threshold event, strict cap surplus,
multiple-zero exclusion or ordering of the two projects' difficulty
follows. [Review 16 §13](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md)
records the primary normalization, finite-frequency and weight checks.
