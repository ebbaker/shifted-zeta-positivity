# Normalized heat approximation: complete limits and arithmetic costs

20 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model **gpt-6-astra**, effort **ultra**. Separate same-model internal
derivation and review, continuing [Note 16](16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md)
from checkpoint `071cee983f0c094943b5462c577ade35454d4cf5`.
No specialist review, novelty claim, or simplicity claim.

This changes an actual bound: the carrier-normalized moving heat target
has a complete first-order norm, not merely the compact coefficient HD.
It does not restore an Euler product or a Nyman--Beurling lower bound for
the changed target. The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md),
and especially the [complete-payment](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [gain-before-expansion](../../../../../../../avoid/20_volume_without_a_gain.md) rules govern this scope.
The norm theorem in §§1–5 assumes RH. Sections 6–7 give unconditional
limitations of this specific normalization; §8 quantifies transfer at a
hypothetical original double zero under RH. No original zero is excluded.

## 1. Statement

Assume RH. Fix a real normalized compact Gevrey extension W of order
1<sigma<2 as in Note 16, write w=W|[0,1], and put L=log N. Retain exactly
the original polynomial V_N,w. Let

\[
 A(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\tfrac12\Log\frac{s}{2\pi},
\]
\[
 T_\tau(s)=e^{-\tau\alpha(s)^2/4}
       \frac{F_\tau(s-1/2)}{A(s)},\qquad
 F_\tau(z)=8H(\tau,-2iz).
 \tag{CN1}
\]

For the norm estimates in §§1–5, the target is evaluated on the critical
line, where the principal logarithm is unambiguous. Sections 6–7 use its
continuation to the right half-plane away from s=1.
For v>=0 define

\[
 E_{N,w}^{[v]}=\frac1{2\pi}\int_{\mathbb R}
 \frac{|1-T_{v/L^2}(1/2+it)V_{N,w}(1/2+it)|^2}{1/4+t^2}\,dt.
 \tag{CN2}
\]

For every fixed V<infinity and every 0<epsilon<2-sigma,

\[
 \sup_{N\ge2}\sup_{0\le v\le V}L(E_{N,w}^{[v]})^{>|T|}
       \ll_{W,V,\epsilon}T^{\sigma-2+\epsilon}\quad(T\ge2).
 \tag{CN3}
\]

Here the superscript means integration over |t|>T. With

\[
 f_m(u)=\frac{u^{m-1}w(u)}{(m-1)!},\quad
 P_{m,v}(z)=\sum_{k=0}^{\lfloor m/2\rfloor}
 \frac{m!}{k!(m-2k)!}(v/4)^kz^{m-2k},
\]
\[
 p_{m,v,w}(u)=-\sum_{k=0}^{\lfloor m/2\rfloor}
 \frac{m!}{k!(m-2k)!}(v/4)^k f_m^{(m-2k)}(u),
 \quad C_{m,v}(w)=\int_0^1|p_{m,v,w}(u)|^2du,
 \tag{CN4}
\]

the full limit, for each fixed v, is

\[
 \lim_{N\to\infty}L E_{N,w}^{[v]}
   =\sum_{\rho\ {\rm distinct}}\frac{C_{m_\rho,v}(w)}{|\rho|^2}
   <\infty .
 \tag{CN5}
\]

Both signs and every multiplicity are retained. The proof below also
makes the limit locally uniform in v. At v=0 this is ST4. For m=1 the
coefficient is unchanged; for m=2 the density is -(uw)''-(v/2)uw,
exactly HD with a=sqrt(v/2).

## 2. The exact Gaussian formula and a uniform numerator bound

The original complete theta integral, Tonelli on its absolute majorant,
and the elementary Gaussian moment give, for tau>0,

\[
 F_\tau(s-1/2)=\frac1{\sqrt\pi}\int_{\mathbb R}
       e^{-x^2}\xi(s+\sqrt\tau x)\,dx.
 \tag{CN6}
\]

Indeed the theta integrand contains cosh(2(s-1/2)u); Gaussian averaging
multiplies it by exp(tau u^2). The doubly exponential theta decay pays
the whole x and u integral. The same identity follows from the
order-one bound on xi and the heat equation F_tau'=F_tau''/4.

For every fixed tau_0<infinity and epsilon>0,

\[
 \sup_{0\le\tau\le\tau_0}|T_\tau(1/2+it)|
       \ll_{\tau_0,\epsilon}(3+|t|)^\epsilon.
 \tag{CN7}
\]

Here is the complete payment, including the cancellation needed for
uniformity in tau. Write s=1/2+it, U=log t, t large, and
A_0=Re alpha(s), B_0=Im alpha(s). RH gives uniformly for a>=0
|zeta(s+a)|<<_epsilon t^epsilon: use the RH critical-line estimate,
Phragmen--Lindelof on the fixed strip [1/2,2] after removing the pole,
and the Euler bound for Re s>=2. The primary critical-line input is
[Chandee--Soundararajan, Theorem 1.1](https://arxiv.org/pdf/0908.2008),
reopened in this continuation. No inverse derivative moment is used.

The [sectorial Stirling and digamma expansions](https://dlmf.nist.gov/5.11)
give, uniformly 0<=a<=t/2,

\[
 \log|A(s+a)/A(s)|=aA_0+O((a+a^2)/t),\qquad
 A_0=\tfrac12\log(t/(2\pi))+O(1/t),\quad B_0=O(1).
 \tag{CN8}
\]

For example integrate the exact log derivative of A: its difference
from alpha at s is O(1/t), and its derivative on this horizontal segment
is O(1/t). Reflection and conjugation give
|xi(s-a)|=|xi(s+a)|, so this bound treats both signs of x in (CN6).
In the variable a=sqrt(tau)|x| the absolute integral over a<=t/2,
after division by A and multiplication by the carrier, is at most

\[
 C_\epsilon t^\epsilon e^{-\tau(A_0^2-B_0^2)/4}
 \frac2{\sqrt{\pi\tau}}\int_0^\infty
 \exp[-(1/\tau-C/t)a^2+(A_0+C/t)a],da.
 \tag{CN9}
\]

Extend the last integral to the real line and complete the square. For
t>=2C tau_0 the additional exponent after cancellation of tau A_0^2/4
is O_{tau_0}(1+log^2(t)/t), and the variance factor is bounded. Thus
(CN9) is O(t^epsilon) uniformly down to tau=0.

For a>=t/2, order-one growth and sectorial Stirling give
|xi(s+a)/A(s)|<=exp(C(a+t+2)log(a+t+2)+Ct). With tau<=tau_0,
the Gaussian e^{-a^2/tau} makes this tail O_J(t^{-J}), uniformly in tau.
The carrier has modulus <=exp(C tau_0) at these large heights.
Bounded t is handled by the compact theta/Gaussian majorant. This proves
(CN7). The proof, unlike GH2, needs no height condition exp(C/tau).

## 3. The two-integral cluster estimate

Use the exact convolution GC8 for V and its kernel K_H(y). At s=1/2+it,

\[
 e_{N,v}(t):=1-T_{v/L^2}(s)V_{N,w}(s)
 =\int_{\mathbb R}K_H(y)
       \left[1-\frac{T_{v/L^2}(s)}{\zeta(s+(H+iy)/L)}\right]dy.
 \tag{CN10}
\]

Its absolute convergence follows from CN7, GC7 and GC10. Set beta=1/sigma
and choose b<beta close enough to beta, as in GC/ST. In the low range
U=log t<=L^b set ell=log U, r=d/ell, and let M count all zeros in
|lambda-t|<=r with multiplicity. Retain the established sharp bound
M<=(1/2+d/pi+epsilon)U/ell. Put H=M+1. Shrink numerical disk constants
so H/L<=r/8. For the central double integral take

\[
 |y|\le rL/8,\qquad |x|\le rL/(8\sqrt V),
 \quad a=\sqrt v\,x/L,\quad b_y=(H+iy)/L.
 \tag{CN11}
\]

When V=0 use the original ST proof; otherwise (CN11) is uniform v<=V.
Factor F(z)=P_t(z)G_t(z), removing precisely this cluster. The integrand
ratio from CN6 and CN10 is exactly

\[
 e^{-v\alpha(s)^2/(4L^2)}
 \frac{A(s+b_y)}{A(s)}
 \frac{G_t(it+a)}{G_t(it+b_y)}
 \prod_{|\lambda-t|\le r}
 \frac{a+i(t-\lambda)}{b_y+i(t-\lambda)}.
 \tag{CN12}
\]

This convenient cancellation keeps all completion terms: there is no
remaining A(s+a). Denote the first three factors by Z. The anchored
regular-factor calculation GC16 gives B=O_d(U log ell) and hence

\[
 |Z|\le t^{o(1)},\qquad
 |1-Z|\le t^{o(1)}
 \left[(B+U)(H+|y|+\sqrt V|x|)/L+V U^2/L^2\right].
 \tag{CN13}
\]

The o(1) is uniform throughout the central rectangle: |a|,|b_y|<r/2,
and VU^2/L^2=o(1). At a=b_y=0 the only remaining factor differs from
one by O_V(U^2/L^2), which explains that last term. It also fits the
coherent 1/L payment: U<=L^b implies U^2/L<=max(1,U^(2-1/b)),
so VU^2/L^2<=t^{o(1)}/L uniformly in this range. Since D(t)<=1/4,
it is absorbed by the same 1/(L D(t)) bound.

Let R_y=sqrt(1+y^2/H^2), and D(t)=min(1/4,dist(t,{lambda})). Each
cluster factor r_lambda in CN12 obeys

\[
 |r_\lambda|\le R_y(1+\sqrt V|x|/H),\qquad
 |1-r_\lambda|\le
 \frac{R_y(H+|y|+\sqrt V|x|)}{L D(t)}.
 \tag{CN14}
\]

The first uses GC18 for the original numerator and |b_y+i(t-lambda)|
>=H/L for its added real term. The second uses the exact difference
and the same GC18 denominator comparison. At a zero read the eventual
bound using its independent bounded branch, not division by D=0.
Telescoping the product and using M/H<=1 gives

\[
 \left|1-\prod r_\lambda\right|
 \le\frac{M R_y^M e^{\sqrt V|x|}
                   (H+|y|+\sqrt V|x|)}{L D(t)}.
 \tag{CN15}
\]

The Gaussian integral of exp(sqrt V|x|) times any fixed polynomial in x
is a V-dependent constant. The remaining y integral is precisely the
one-extra-moment payment ST12:

\[
 e^H\int C e^{-c|y|^\beta}R_y^M(H+|y|+1)dy
 \le\exp[(\sigma-1)M\log(M+2)+O_W(M+1)].
 \tag{CN16}
\]

The polynomial factors M,B,U are absorbed in t^{o(1)}. Thus the central
coherent difference is <<_{W,V,q} t^q/(L D(t)) for any fixed
q>(sigma-1)/2, after the same choices of d,epsilon,b as ST. Without
subtraction, CN12--CN16 also give the independent bound O(t^q).

## 4. Both omitted tails and the high-height range

First integrate the Gaussian exactly before treating |y|>rL/8. CN7,
GC10 and GC7 bound the full y-tail, just as ST14--ST15, by
O_{J,W,V}(L^{-J}t^{-J}) for every fixed J. In particular no absolute
Gaussian estimate is combined with that unbounded y-tail.

For central y, the omitted |x|>rL/(8sqrt V) is also paid. CN8,
completed reflection and the RH right-half-plane bound give, as long as
|a|<=t/2, the Gaussian integrand bound

\[
 C_\epsilon t^\epsilon
 \exp[-x^2+C_V(U|x|/L+|x|/(Lt)+x^2/(L^2t))].
 \tag{CN17}
\]

On the omitted range the positive x-dependent terms are o(x^2),
uniformly in U<=L^b, because its lower endpoint is >>_V L/log L.
The portion |a|>t/2 is still smaller by the order-one bound in §2.
Consequently the Gaussian tail is O(t^epsilon exp(-c_V r^2L^2)).
Multiplying by the coarse reciprocal payment exp(CU log(2+L)), and
by the kernel mass O(e^H), leaves
O_{J,W,V}(L^{-J}t^{-J}). This also pays the missing Gaussian mass in
the constant term 1 of CN10. These are actual absolute tail estimates.

In the high range U>L^b use CN7 as the numerator estimate in GC21--GC23.
The sharp reciprocal bound and H=kappa U then give the same global
O(t^q) estimate. The entire |y|>tL/2 tail has the same exponential
payment as GC; no Gaussian expansion is needed in this range.
Combining the low estimates, with J fixed large, yields

\[
 |e_{N,v}(t)|\ll_{W,V,q}
 t^q\min\{1,(L D(t))^{-1}\}+L^{-J}t^{-J}
 \quad(U\le L^b),
 \tag{CN18}
\]

and |e_{N,v}(t)|<<t^q in the complementary range. Bounded heights use
the same finite-disk cluster argument with the Gaussian moment. Each
finite exceptional N is handled uniformly v<=V by CN7 and its finite
Dirichlet polynomial.

The nearest-zero cells from ST17 give
L int_R min(1,(L|u|)^(-2))du=4, with no lower spacing assumption.
Use the unit-window count, square CN18, and sum with t^(2q-2). The
low tail is O(T^(2q-1)log T). In the high range L<=log(t)^(1/b), so
the scaled tail is O(T^(2q-1)log(T)^(1/b)). Choose 2q close enough to
sigma-1 and absorb the logarithms. This proves CN3 for large T; the
compact calculation below supplies the uniform compact bound needed
to enlarge the constant to every T>=2.

## 5. Actual compact profiles and the complete limit

At a fixed zero rho of order m let q=s-rho. The complete original
convolution gives, uniformly on the critical-line segment q=iy of a fixed isolated disk,

\[
 V_{N,w}(\rho+q)=\sum_{j=1}^m b_jL^j A_j(Lq)+G(q)+O(1/L),
 \quad A_j(z)=\int_0^1\frac{u^{j-1}w(u)}{(j-1)!}e^{-zu}du,
 \tag{CN19}
\]

where 1/zeta(rho+q)=sum b_j q^(-j)+G(q), and
|A_j(ix)|<<_W,j(1+|x|)^(-j). Every Laurent coefficient and the external
convolution tail are retained, as in CH/HD.

Apply the heat equation to the analytic function A(s)zeta(s). At
tau=v/L^2, the highest Laurent term in CN19 and the leading order-m
zero give P_m,v(Lq) A_m(Lq). Completion derivatives, lower Laurent
terms, and the heat Taylor remainder give O_{rho,W,V}(1/L) uniformly
on the whole fixed critical-line segment. Explicitly the kth heat term contributes
L^(-2k) times a function vanishing to order max(m-2k,0); its next
Taylor coefficient, multiplied by L^m A_m, is O(1/L), using the displayed
A_j bound. A lower pole j<m contributes at most
O(L^(-min(m-j,2k))) for k>=1. Choose the heat Taylor order K with
2K+2>=m+1; its uniform O(L^(-2K-2)) remainder times V=O(L^m)
is O(1/L). The k=0 term is the original CH profile. Finally the carrier
is 1+O_{rho,V}(L^(-2)) on the disk and multiplies a product bounded on the segment.
Therefore

\[
 e_{N,v}(\gamma+y)=1-P_{m,v}(iLy)A_m(iLy)+O_{\rho,W,V}(1/L).
 \tag{CN20}
\]

All endpoint terms in integration by parts are explicit: f_m and its
derivatives vanish at 1; at 0, only f_m^(m-1)(0)=1 enters the mth
derivative, and every lower derivative in CN4 has zero initial data.
Thus

\[
 1-P_{m,v}(z)A_m(z)=\int_0^1p_{m,v,w}(u)e^{-zu}du
       =O_{m,W,V}((1+|\Im z|)^{-1})\quad(\Re z=0).
 \tag{CN21}
\]

Plancherel, CN20 and the fixed-disk weight comparison give its actual
unscaled norm C_m,v(w)/(L|rho|^2)+O_{rho,W,V}(log L/L^2).
Away from the finitely many zeros in a fixed height interval the error
is O(1/L). Consequently the compact first-order limit is the finite
sum in CN5, uniformly v in compact sets. For each fixed v, finite-height limits and CN3 bound every finite
profile sum over |Im rho|>T by the same O(T^(sigma-2+epsilon)),
independently of v in [0,V]. Exhausting the finite set therefore gives
that bound for the full nonnegative profile tail, uniformly in v. Thus
the profile series converges uniformly on [0,V]. The finite-height
convergence is already uniform there; CN3 bounds the actual complementary
norm uniformly as well. These two uniform tail payments prove CN5
locally uniformly in v, rather than only pointwise by positivity.

## 6. The normalization does not retain ordinary Dirichlet arithmetic

Here the symbols \(R_t\) and \(T_t\) denote the same function.

Use the original theta heat flow and its completed zeta coordinate:
\[
 \mathcal X_t(s)=8H_t(-2i(s-\tfrac12)),\qquad
 A(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),
 \qquad \mathcal X_0(s)=\xi(s)=A(s)\zeta(s).
 \tag{RN1}
\]
The carrier in Note 16, (GH2)–(GH3), is
\[
 \alpha(s)=\frac1{2s}+\frac1{s-1}
       +\frac12\Log\frac{s}{2\pi},\qquad
 R_t(s)=\frac{\mathcal X_t(s)}{A(s)e^{t\alpha(s)^2/4}}.
 \tag{RN2}
\]
The logarithm is real on the positive real axis. For **every fixed
\(t>0\)**, unconditionally, as real \(\sigma\to+\infty\), put
\(\ell=\log(\sigma/(2\pi))\). Then
\[
 \boxed{\quad R_t(\sigma)
 =1+\frac{t^2\ell^2/64+t/8}{\sigma}
      +O_t\!\left(\frac{(1+|\ell|)^4}{\sigma^2}\right).\quad}
 \tag{RN3}
\]
Consequently this explicitly normalized function has **no representation
by an ordinary Dirichlet series converging in any right half-plane**.
Convergence need not be absolute in the assumed representation. The claim
concerns this particular carrier, not every possible heat-dependent
completion. The all-positive-time range here follows from the exact
Gaussian representation below; it does not extend the distinct
critical-line asymptotic used in Note 16 §16 beyond its primary-source
range \(0<t\le1/2\).

### 6.1. Complete Gaussian representation and its remote tail

The theta definition and normalization are [Polymath15, equations
(1)–(4)](https://arxiv.org/html/1904.12438v2#S1). Direct Gaussian integration
gives
\[
 \mathcal X_t(s)=\frac1{\sqrt{\pi t}}
       \int_{\mathbb R}e^{-h^2/t}\xi(s+h)\,dh.
 \tag{RN4}
\]
Indeed averaging \(H_0(z-2i\sqrt t\,v)\) with density
\(\pi^{-1/2}e^{-v^2}\) multiplies its cosine-source integrand by
\(e^{tu^2}\). The source's superexponential decay justifies absolute
Fubini, also for complex \(s\) in a compact set. Thus the real displacement
\(h\) in (RN4) has variance \(t/2\), and the exact heat equation is
\(\partial_t\mathcal X_t=\tfrac14\partial_s^2\mathcal X_t\).

For real \(\sigma\) sufficiently large and every real \(h\),
\[
 \frac{|\xi(\sigma+h)|}{A(\sigma)}
 \le C\exp\{C|h|\log(\sigma+|h|+2)\}.
 \tag{RN5}
\]
To verify it, on real arguments at least two use the bounded Euler series
for \(\zeta\) and \(|(\log A)'(x)|\ll\log(x+2)\), with eventual
monotonicity of \(A\). Reflect arguments below zero by
\(\xi(x)=\xi(1-x)\), and use boundedness on the remaining compact interval.
The reflected argument exceeds \(\sigma\) by at most \(|h|+1\), with
\(|h|\gg\sigma\) whenever that extra constant matters. This proves the
stated single bound after increasing \(C\).

Take \(R=(\log\sigma)^2\). Uniformly for \(|h|\ge R\),
\(\log(\sigma+|h|+2)/|h|=o(1)\). Consequently (RN5) gives
\[
 \frac1{A(\sigma)\sqrt{\pi t}}
 \int_{|h|>R}e^{-h^2/t}|\xi(\sigma+h)|\,dh
       =O_t(e^{-c_t(\log\sigma)^4}).
 \tag{RN6}
\]
This includes all negative displacements across the original completion's
poles: the integrand is the complete entire function \(\xi\). No separate
global Gaussian integral of \(A\) or termwise integral of its Euler
expansion is being asserted.

### 6.2. The curvature term survives carrier division

Let \(g=\log A\) on the real interval \((1,\infty)\), and set
\(a=g'(\sigma)\), \(b=g''(\sigma)\). The real gamma expansions
[DLMF 5.11.1–5.11.2](https://dlmf.nist.gov/5.11#E1) and the
[polygamma series 5.15.1](https://dlmf.nist.gov/5.15#E1) give
\[
 \begin{split}
 a&=\alpha(\sigma)-\frac1{6\sigma^2}+O(\sigma^{-4})
      =\ell/2+O(\sigma^{-1}),\\
 b&=\frac1{2\sigma}+O(\sigma^{-2}),\qquad
 \sup_{|x-\sigma|\le R}|g'''(x)|=O(\sigma^{-2}).
 \end{split}
 \tag{RN7}
\]
For example, differentiate the explicit elementary factors of \(A\)
and use the digamma expansion for \(a\); use the convergent polygamma
series for \(b\) and \(g'''\). This avoids differentiating an uncontrolled
Stirling remainder.

On \(|h|\le R\), the Euler series gives
\(\zeta(\sigma+h)=1+O(2^{-\sigma+R})\), and Taylor's theorem gives
\[
 g(\sigma+h)-g(\sigma)
   =ah+\frac b2h^2+O(|h|^3/\sigma^2).
 \tag{RN8}
\]
Tilt the density in (RN4) by \(e^{ah}\). Its normalizing factor is
\(e^{ta^2/4}\); the tilted variable has mean \(ta/2\), variance \(t/2\),
and absolute \(k\)-th moment \(O_t((1+|\ell|)^k)\) for each fixed \(k\).
On the retained interval, both the quadratic exponent and the Taylor
remainder tend uniformly to zero. Expanding that exponential, its
integrated error after the linear curvature term is bounded by
\[
 O_t\!\left(\sigma^{-2}\mathbb E_a|h|^3
                   +b^2\mathbb E_a h^4\right)
      =O_t((1+|\ell|)^4/\sigma^2).
 \tag{RN9}
\]
The tilted Gaussian's discarded tail is also
\(O_t(e^{-c_t(\log\sigma)^4})\), since its mean is \(O_t(\log\sigma)\).
Together with (RN6), the exponentially small central Euler correction,
and \(e^{ta^2/4}\ge1\), this proves
\[
 \frac{\mathcal X_t(\sigma)}{A(\sigma)e^{ta^2/4}}
 =1+\frac b2\left(\frac t2+\frac{t^2a^2}4\right)
       +O_t((1+|\ell|)^4/\sigma^2).
 \tag{RN10}
\]
Finally,
\[
 e^{t(a^2-\alpha(\sigma)^2)/4}
       =1+O_t((1+|\ell|)/\sigma^2),\quad
 \frac{tb}4=\frac t{8\sigma}+O_t(\sigma^{-2}),\quad
 \frac{t^2ba^2}8=\frac{t^2\ell^2}{64\sigma}
                 +O_t((1+|\ell|)^2/\sigma^2).
 \tag{RN11}
\]
Equations (RN10)–(RN11) prove (RN3), including the variance contribution
\(t/(8\sigma)\). In particular
\(R_t(\sigma)-1\sim t^2\ell^2/(64\sigma)>0\).

### 6.3. Why even conditional ordinary Dirichlet convergence is excluded

Suppose \(D(s)=\sum_{n\ge1}c_nn^{-s}\) converges at a real \(\sigma_0\).
Its individual terms are bounded, so \(|c_n|\le C n^{\sigma_0}\), and
it converges absolutely at \(\sigma_1=\sigma_0+2\). Hence for
\(\sigma\ge\sigma_1\),
\[
 |D(\sigma)-c_1|
 \le 2^{-(\sigma-\sigma_1)}
          \sum_{n\ge2}|c_n|n^{-\sigma_1}
 =O(2^{-\sigma}).
 \tag{RN12}
\]
If this represented (RN2) on a right half-plane, (RN3) would force
\(c_1=1\), whereas its positive \(\ell^2/\sigma\) correction contradicts
(RN12). No negative derivative moment, RH, zero simplicity, or interchange
of an infinite heat-evolved Dirichlet expansion enters this argument.

The fixed-time conclusion is also not a uniform assertion for moving
\(t=t_N\to0\). It identifies a concrete arithmetic defect of the
suggested normalization at each positive time. It does not determine a
new weighted approximation infimum, forbid other completions, or exclude
an RH multiple-zero endpoint. In particular an attempted replacement by
the separately Gaussian-heated \(A\) needs its own definition: \(A\) has
uncancelled negative-even poles, so its literal real Gaussian integral
does not have the absolute-convergence justification of (RN4).

## 7. An essential singularity replaces the ordinary pole

In this section and §8, write \(\widetilde Z_t=T_t\),
\(\mathcal F_t=F_t\), and \(\mathcal A=A\), with definitions (CN1).


For every fixed \(t>0\), the source is strictly positive on \(u\ge0\), because each summand has positive coefficient \(2s^2-3s\) with \(s=\pi n^2e^{4u}\ge\pi\). Hence
\[
\mathcal F_t(1/2)=8\int_0^\infty e^{tu^2}\Phi(u)\cosh u\,du>0.
\]
The integral converges by the superexponential source decay. Moreover \(\mathcal A'(1)=1/2\). Writing \(s=1+z\) and
\[
b(s)=\frac1{2s}+\frac12\Log\frac{s}{2\pi},\qquad
b_0=b(1)=\frac{1-\log(2\pi)}2,\qquad b'(1)=0,
\]
gives
\[
\widetilde Z_t(1+z)
=z^{-1}\exp\!\left(-\frac{t}{4z^2}-\frac{tb_0}{2z}\right)U_t(z),
\qquad
U_t(0)=2\mathcal F_t(1/2)e^{-tb_0^2/4}>0,
\tag{NT1}
\]
where \(U_t\) is holomorphic and nonzero in a sufficiently small disk.

Thus \(s=1\) is an essential singularity. It cannot be removed by multiplying by a nonzero finite Dirichlet polynomial, by any finite-order zero, or by subtracting finitely many pole terms. More concretely, if \(D(1+z)=d_kz^k+O(z^{k+1})\), \(d_k\ne0\), then
\[
|\widetilde Z_t(1+iy)D(1+iy)|
\sim 2\mathcal F_t(1/2)|d_k|e^{-tb_0^2/4}
|y|^{k-1}\exp\!\left(\frac{t}{4y^2}\right),
\qquad y\to0.
\tag{NT2}
\]
Every finite pole subtraction is negligible compared with (NT2). In particular the corresponding expression divided by \(s\), as in the usual weighted Hardy-space conversion, still has an essential singularity and an infinite local squared integral on the vertical line \(\Re s=1\).

This proves a precise limitation of the literal normalization (CN1): finiteness of its boundary norm on \(\Re s=1/2\) does **not** restore the ordinary meromorphic target with a removable, finitely paid pole that underlies the standard Nyman–Beurling/Hardy argument. The given expressions fail that analytic hypothesis. This is not a claim that their critical-line norm is infinite; it is finite at fixed \(0<t\le1/2\), as follows from the already verified carrier cancellation. Nor does it rule out a different normalization with the pole of \(\alpha\) modified. Such a modification would require its own approximation theorem.

Essential singularity at \(1\) alone does **not** exclude an ordinary Dirichlet series on a farther right half-plane. That separate conclusion follows from the real-axis asymptotic proved in §6.

## 8. A nonvanishing cost at the proposed moving heat scale

Assume RH and an original exact double zero \(\rho=1/2+i\gamma\). Fix an isolated neighborhood and a normalized real flat Gevrey taper \(w\) as in Note16 §15. Put \(L=\log N\), \(v>0\), \(t=v/L^2\), \(f(u)=uw(u)\), and \(a^2=v/2\). Keep \(v,w,\rho\) fixed before \(N\to\infty\). Then
\[
\boxed{\;
\frac1{2\pi}\int_{-r}^{r}
\frac{|[\widetilde Z_{v/L^2}(\rho+iy)-\zeta(\rho+iy)]
V_{N,w}(\rho+iy)|^2}{1/4+(\gamma+y)^2}\,dy
=\frac{v^2\|uw\|_{L^2(0,1)}^2}{4L|\rho|^2}
+O_{\rho,w,v}(L^{-2}).
\;}
\tag{NT3}
\]

Indeed the completely paid local Laurent expansion (HD4) and compact heat expansion give
\[
[Z_{v/L^2}-\zeta]V_{N,w}
=a^2A_2(iLy)+O_{\rho,w,v}(L^{-1}),\qquad
A_2(z)=\int_0^1uw(u)e^{-zu}\,du,
\tag{NT4}
\]
uniformly on the fixed critical-line segment through the zero. Formula (HD5) also gives \(Z_{v/L^2}V_{N,w}=O_{\rho,w,v}(1)\) there. Since \(\alpha\) is bounded on this neighborhood,
\[
(e^{-t\alpha^2/4}-1)Z_tV_{N,w}=O_{\rho,w,v}(L^{-2}).
\]
This proves (NT4) with \(\widetilde Z\) in place of \(Z\). Integration by parts gives \(A_2(ix)=O_w((1+x^2)^{-1})\), so the uniform error, weighted cross term, weight variation, and omitted Fourier tail contribute \(O(L^{-2})\). Plancherel gives the main term (NT3).

Because \(w(0)=1\), \(\|uw\|_2>0\). Therefore this fixed-taper double-event consumer does not admit an \(o(L^{-1/2})\) norm perturbation from the normalized heat target back to the original target. Any triangle-inequality transfer of a sharp \(1/L\) coefficient must pay the nonzero coefficient in (NT3). The conjugate neighborhood contributes separately. This does not exclude more general approximants or a coherent signed transfer; the existing fixed-taper identity already retains that coherence:
\[
C_a(w)=C_0(w)-2a^2\|f'\|_2^2+a^4\|f\|_2^2.
\]
Dropping the cross term would lose precisely the relevant information.

## 9. Scope, controls and the remaining arithmetic step

This is an actual complete norm theorem for the explicitly changed
critical-line target. It upgrades the local HD coefficient and repairs
the infinite-norm issue GH for this particular carrier normalization.
For a double zero the finite-separation coefficient can indeed fall below
two, exactly as HD shows. That fact supplies no opposing inequality for
the original zeta approximation problem: the multiplier exp(-tau alpha^2/4)
is not an ordinary Euler/Dirichlet normalization, and the heat target has
not been assigned the unchanged Nyman--Beurling lower bound.

The fixed original Gevrey taper, fixed bounded v range, and ordered
height exhaustion are essential stated hypotheses. There is no asserted
uniformity for a moving taper, v tending to infinity with N, or a global
heat derivative obtained by differentiating the asymptotic. RH implies
simplicity remains open.

The source identities and the original Möbius convolution are essential.
The [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
does not turn this estimate into an event exclusion: Euler-factor controls
change the theta source and inverse Dirichlet coefficients; weighted-square
controls change its coefficients; reflected and positive-primitive controls
have different sources. None satisfies the premise that the numerator is
the original theta heat flow and the inverse convolution is the original
1/zeta. The Gaussian and finite-cluster algebra themselves are compatible
with collisions.

BW09 can use the Gaussian identities and the normalization warning, but
CN3–CN5 depend on original-zeta RH arithmetic; importing them into its RH
contradiction would assume its conclusion. The unconditional obstructions
in §§6–7 concern this explicit carrier only. Removing its pole by hand or
choosing another completion requires a new theorem, including a paid link
to the original arithmetic norm. The fixed-double cost (NT3) rules out
an unpriced small-perturbation transfer for the stated taper class.

[Review 17](../reviews/17_NORMALIZED_HEAT_LIMIT_AND_ARITHMETIC_REVIEW_20261020.md)
records the internal checks and the corrected local-segment scope. The
six-page manuscript is left unchanged at its consolidation checkpoint;
this full continuation and its precise scope stay in the notes.
