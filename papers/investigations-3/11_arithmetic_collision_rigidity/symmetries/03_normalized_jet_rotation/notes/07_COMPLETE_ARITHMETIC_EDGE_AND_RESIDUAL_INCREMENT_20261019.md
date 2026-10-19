# Complete arithmetic edge remainder and residual increment

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Separate delegated same-model derivation, proof review and
fresh replay; no independent specialist human review.

## Result and comparison

The previously unpaid Riemann–Siegel edge remainder in G3 now has a
complete independent bound on the fixed pilot
`B=[1/100,1/5] x [999,1001]`, with fixed cutoff `N=8`.
An explicit eighth-order RS approximation, exact gamma prefactor, finite
Gaussian moment model, complex-extension payment and both infinite
Gaussian tails give normalized edge error

```
|e_edge|<6e-8,  |e_edge,x|<6e-8,  |e_edge,xx|<1.2e-7.        (1)
```

The value bound is uniform on physical complex-x disks of radius 1 about
B, with real heat time; its spatial derivatives follow by Cauchy. Combine
it with the finite heat–Stirling correction from [Note 06][note06], then
evaluate the **recombined signed** endpoint primitive. The complete result is

```
sup_B |I_r(t,x)| < 0.000854.                               (2)
```

No complete-source quadrature, Taylor coefficients for H, inferred edge
values, or fitted coefficients enter (1)–(2). The comparison is:

| Complete increment allowance on B | Upper bound | Information used |
| --- | ---: | --- |
| Prior analytic-only phase-aware payment | 0.812260 | Complete generic disk envelope and known phase |
| New arithmetic payment | 0.000854 | Explicit finite gamma/heat modes, RS8 edge and complete errors |
| Retained strongest source-informed payment | 0.000266448 | Complete-source polynomial and correlated residual integration |

The new independent arithmetic allowance is more than 950 times smaller
than the prior analytic-only allowance. It does not beat the retained
source-informed payment or establish a cost advantage. No further consumer
sweep or coverage extension is activated. This completes the bounded G3
edge and independent-prefix task; it supplies neither a height-uniform
cancellation law nor the remaining global real bridge or complex exterior.

Classification: a **proved bounded arithmetic estimate with outward
constants**, not a new global nonvanishing criterion. Read the repository
[result summaries][results] and [patterns to avoid][avoid], especially
[controls][controls], [scoped exclusions][a07] and
[signed recombination][a12]. The exact transport identities are inherited;
the new quantitative input is the paid edge model and (2).

## The retained signed arithmetic model

Use the normalizer A, phase theta and coherent full approximation
`f=(G8-Chat8)/A` from [Note 03][note03]. Put

```
Q=H/A, r=Q-f, omega=theta_x,
R_r=r+r_xx/omega^2-omega_x*r_x/omega^3,
Z_r=exp(-i theta)*(r-i*r_x/omega),
I_r=integral_999^x exp(-i theta)*omega*R_r dy
   =i*(Z_r(t,x)-Z_r(t,999)).                               (3)
```

The exact arithmetic decomposition is `r=r_AB+r_edge`, with
`r_edge=2 Re(exact heat RS contour)/A+Chat8/A`. In particular, the sign of
Chat is positive in the edge discrepancy. Both reflected channels and
normalizer derivatives are retained; no floor-defined cutoff is differentiated.

For `s=(1-ix)/2`, `alpha=m0'`, let

```
kappa_n=1/(6s)+alpha'(s)[t/4+t^2(alpha(s)-log n)^2/8],
rhat_AB=2 Re sum_(n=1)^8 g_n*kappa_n/A.                     (4)
```

Note 06 proves the relative finite-mode remainder and its first two
spatial derivatives. Its whole-B normalized finite-sum payments are

```
e_AB,0 <5.206260e-6,
e_AB,1 <3.404651e-6,
e_AB,2 <2.961263e-6.                                       (5)
```

For the edge, put

```
tau=x/2+pi*t/8, a=sqrt(tau/(2pi)), p=17-2a,
u=1/2+w, w=sqrt(t)*v, E_v=pi^(-1/2) integral_R exp(-v^2),
gamma=log a+i*pi/4,
eta(u,tau)=log M(i*tau+u)-m0(i*tau)-u*gamma,
S8(p,u)=sum_(k=0)^8 Ck(p,u)/a^k.
```

The coefficients Ck come from the exact finite recurrence used in
[Note 06][note06], with F=C0 and the 126 previously checked rational
coefficient identities. The true gamma function is
`M(s)=s(s-1) pi^(-s/2) Gamma(s/2)/16`.

Define a specific polynomial model, so that its error can be bounded
independently of numerical quadrature. Write b=i*tau and

```
S3(z)=1/(6z)-1/(45z^3)+8/(315z^5),
eta_tilde(u,b)=(u+u^2)/(2b)
 +sum_(k=2)^24 (-1)^(k+1) u^k [b^(1-k)+(1+u)b^(-k)]/(2k)
 +sum_(k=1)^24 (-1)^(k+1) u^k (b-1)^(-k)/k +S3(b+u).       (6)
```

This is the Taylor expansion of the exact logarithmic identity displayed
in Appendix D, with the first three Stirling terms. Let P12(w,tau) be the
degree-12 Taylor polynomial of `exp(eta_tilde(1/2+w,i*tau))` in w.
Replace F by its degree-120 Taylor polynomial about `p0=-21/25`, and use
its actual derivatives in the finite Ck recurrence; call the resulting
profile `S8_hat`. All retained Taylor coefficients are outward balls.
Then the retained edge bracket is

```
P_hat(tau,t)=E_v[P12(sqrt(t)v,tau)*S8_hat(p,1/2+sqrt(t)v)]
                                                      -F_hat(p). (7)
```

The integrand in (7) has degree at most 20 in w. Every Gaussian moment
is evaluated exactly in form:
`E w^(2j)=(t/2)^j (2j-1)!!`, with odd moments zero.
The subtracted F_hat corresponds to the retained Chat; its tiny profile
approximation error is included in the payment below.

On the real axis the coherent normalized edge model is

```
rhat_edge=W_real(x,t)*sqrt(tau)*[tau*Re P_hat-Im P_hat],
W_real=sqrt(pi)/4*exp(-pi*x/8-pi^2*t/64)/A(x,t).             (8)
```

The implementation differentiates the same analytic expression, including
tau, a, p, W_real, normalizer and gamma-profile terms. Its two-channel
holomorphic extension uses F and its reflected conjugate profile; taking
real and imaginary series coefficients in (8) is only the real-axis
implementation of that extension. Set `rhat=rhat_AB+rhat_edge`.

## Complete complex edge payment

Use radius-1 physical-x disks about the pilot and their containing tube
`Re z in[998,1002]`, `|Im z|<=1`. The printed real parameters have
`tau_real in[499,502]`, `sigma in[0,1]` and fixed natural cutoff 8.
The central Gaussian interval is `|v|<=10`. At order K=8,
`K+sigma+sqrt(t)v>3.5278>2`, so the negative-argument RS remainder
hypothesis holds throughout that interval.

Four separately proved payments bound the **complete holomorphic
exact-minus-polynomial edge**, in the actual complex A(z,t) units:

| Component | Safe normalized value ceiling |
| --- | ---: |
| Central real-parameter RS8 remainder, true gamma prefactor included | 4.805e-8 |
| Finite coherent-extension mismatch | 5.529e-9 |
| Exact Gaussian tails outside 10 | 1.4e-41 |
| Retained gamma/Gaussian/profile polynomial conversion | 1e-11 |
| Sum | <6e-8 |

The unrounded complete sum in the 192/256 nominal replays is below
`5.357353e-8`. The gamma/heat prefactor is charged once, not once per
lemma. The complete sum is holomorphic; its separate real-parameter RS
and CR estimates need not themselves be holomorphic. Cauchy with radius 1
therefore gives the derivative factors 1 and 2 in (1).

Appendix A proves the real central payment from the published RS remainder.
Appendix B proves the coherent-extension and normalizer costs. Appendix C
pays the exact tails directly on the fixed RS contour, without applying
a central asymptotic expansion at infinite Gaussian arguments. Appendix D
pays every model replacement and polynomial tail. The checker evaluates
all constants rather than importing the source-informed edge diagnosis.

One source-normalization caution matters: the intermediate Stirling
shortcut in the proof of Polymath Proposition 6.3 does not directly give
the smaller constant suggested there. We use the independently derived
safe gamma prefactor `exp((u^2+1)/(tau-3))`. The published Proposition 6.2
RS remainder inequalities themselves are used unchanged. No claim about
failure of that paper's final theorem follows from this local bookkeeping
correction.

## Complete signed increment payment

Let d=r-rhat. Combining (1) and (5) gives

```
|d| <5.266260e-6, |d_x| <3.464651e-6,
|d_xx| <3.081263e-6.                                      (9)
```

The script uses the narrower outward finite-mode ledger, rather than just
these rounded ceilings. Let `w0=inf_B |omega|`. The original explicit phase
has negative omega bounded away from zero. Since d and d_x are real,

```
|Z_d| <= sqrt(e0^2+(e1/w0)^2),
|I_r| <= |Z_rhat(t,x)-Z_rhat(t,999)|
                          +2 sqrt(e0^2+(e1/w0)^2).         (10)
```

The error appears once at each endpoint. No second derivative is needed
for this endpoint payment, though it has independently been supplied.
The formula (3) accounts for every partial spatial prefix.

For interval efficiency, retain the leading phase cancellation algebraically.
If `rhat_AB=2 Re(exp(i theta) Hhat)` with
`Hhat=sum p_n*kappa_n`, `p_n=g_n/(A exp(i theta))`, then exactly

```
Z_rhat_AB=2Hhat-i/omega*[Hhat_x+exp(-2i theta)*conj(Hhat_x)]. (11)
```

Add the edge contribution to Z before subtracting the anchor and bounding
its modulus. This avoids the separate source/approximation-prefix triangle
payment excluded in Note 03. It also prevents the leading mode's large
oscillatory phase from being lost to interval dependency.

A declared closed cover of 8 equal time slabs and 32 equal spatial cells
covers all B. Each time slab has its own interval-enclosed anchor at 999.
The 256 complete interval images give

```
sup |Z_rhat(t,x)-Z_rhat(t,999)| <0.000840994,
two-endpoint model-error payment <0.000012291,
complete |I_r| <0.000853284317 <0.000854.                   (12)
```

Both nominal 192- and 256-bit replays give the same displayed complete
ceiling. High-order profile coefficient calculations use 512 explicit
guard bits, so their actual working precisions are 704 and 768 bits.
The cover is a proof by interval images of closed cells, not point sampling.
The coarse complete payment is not an optimal bound for this model. No
mesh campaign was used to compete with the stronger source-informed result.

## Review controls and interpretation

The [edge ledger][edge-record] and [increment ledger][increment-record]
pin their arithmetic producers and retained polynomial model. The
[separate same-model review][review] independently replays the edge and
prefix at nominal 192 bits. Input guards reject mismatched producers,
model/source pins, missing precision and altered error/radius contracts.
The [fresh inherited source-control replay][control-record] rejects five
event boxes and the Euler negative-Laguerre witness using each source's
own errors. No new event-acceptance consumer is introduced.

The unchanged complete theta coefficients, level-one gamma normalization
and matching RS contour are specific premises. Finite-prime/weighted-square
controls do not supply full normalized theta reflection with unchanged
complete coefficients; reflected/shape/positive-primitive controls do not
supply the specific theta square expansion; Euler deformations change
the completed arithmetic data and level. The rotation, Gaussian and filter
identities alone distinguish none of them. The finite gamma-mode theorem
can apply wherever those modes occur and is insufficient by itself to
exclude a collision.

The fixed-pilot arithmetic obligation left by Note 06 is now supplied.
The unusually strong center cancellation remains a local diagnostic,
not a uniform phase law; (2) is the uniform result actually proved.
The calibrated/direct consumer ordering in Note 05 is unchanged, and the
source-informed `0.000266448` allowance remains stronger.

**Decision:** complete this bounded edge/prefix task and retain the
independent arithmetic evaluator. Further fixed-box refinement needs a
specific error or matched-cost objective. The next structural G3/S04 task
is to parameterize the complete remainder and retained signed functional
for a growing-height regime; this requires new uniform constants and is
not obtained by relabeling the present fixed-box certificate. Existing
S04 first-jet scaling can support that task; second derivatives are needed
only for a consumer that chooses them. No new coverage is claimed.

## Detailed proof of the edge components

## Appendix A Central real RS remainder

### Imported inputs and fixed geometry

The only RS error inputs are [Polymath 2019, Proposition 6.2,
equations (56)–(57)](https://arxiv.org/html/1904.12438v2#S6.SS2).
The uniform gamma/Stirling estimate is its Lemma 5.1(v); the logarithmic
normalizer derivative follows by direct differentiation of the displayed
M0 formula. No value, polynomial, or error enclosure for the complete
source H is consumed.

Keep `B=[.01,.2] x [999,1001]`, fixed `N=8`, and use closed physical
complex-x disks of radius 1 about the real pilot. Write `z=X+i y` and
use the positive channel

```
sigma=(1-y)/2,       T=X/2,
tau=T+pi*t/8,        u=sigma+sqrt(t)*v,
a=sqrt(tau/(2*pi)),  p=17-2*a.
```

Then `sigma in [0,1]`, `499<tau<502`, and
`8.9116954954<a<8.9384440163`. Thus the RS cutoff is exactly 8 on every
disk. On the central Gaussian interval `|v|<=10`,

```
-4.472135955 < u < 5.472135955,
K=8 gives K+u>3.527864045>2.
```

Consequently the negative-u remainder hypothesis is satisfied throughout
the central Gaussian interval. This check is essential: at this cutoff,
uniform K=4 or K=6 does not satisfy that hypothesis on `|v|<=10`.

Let `J_N(s)` denote the RS contour without the gamma prefactor and set

```
J_N(u+i*tau)=(-1)^(N-1)*U(tau)*a^(-u)
                 *[sum_(k=0)^8 Ck(p,u)/a^k + RS_8(u+i*tau)].
```

Define `Q=Gamma(9/2)*(1.1/a)^9` and `c=(3/2)*log 2`. The imported
remainder estimates give

```
|RS_8(u+i*tau)| <= Q * exp(c*u)/7,     u>=0,
|RS_8(u+i*tau)| <= Q/2,               u<0, 8+u>=2.
```

The factor `(9/10)^ceil(-u)` in the second input has safely been dropped.

### Exact gamma prefactor payment

Let `M(s)=s*(s-1)*pi^(-s/2)*Gamma(s/2)/16`. The exact identity

```
alpha(i*tau)=log a+i*pi/4+1/(2*i*tau)+1/(i*tau-1)
```

and the direct bound `|alpha'(s)|<=1/[2*(tau-3)]` on the horizontal
segment from `i*tau` to `u+i*tau` give

```
|M(u+i*tau)*a^(-u)| / |M0(i*tau)|
 <= exp{ 1/[6*(tau-.66)] + 3*|u|/(2*tau)
                              + u^2/[4*(tau-3)] }
 <= exp[(u^2+1)/(tau-3)].                                      (A)
```

For the first step, Lemma 5.1(v) is applied at `(u+i*tau)/2`, so the
logarithmic gamma error is `1/[6*(tau-.66)]`. For the second step, put
`d=tau-3` and use

```
1/[6*(tau-.66)] <= (2/3)/(4*d),
3*|u|/(2*tau) <= 6*|u|/(4*d),
6*|u| <= 3*u^2+3,
u^2+6*|u|+2/3 <= 4*u^2+11/3 <= 4*(u^2+1).
```

This derivation avoids a small factor-of-two issue in a shortcut of the
printed Proposition 6.3 proof: its displayed gamma error
`1/[12*(tau/2-.33)]` is `1/[6*(tau-.66)]`, so it cannot be bounded by
`(1/3)/[4*(T-3)]` as that intermediate line suggests. Our safe constant
1 in (A) is established above, without importing that shortcut or its
`5/6` replacement. This correction affects only a deliberately coarse
scalar payment here; no statement about the paper's final theorem is
needed.

The heat contour shift is exactly

```
R_t,N(sigma+i*T) = exp(t*pi^2/64) E_v[
   exp(-i*sqrt(t)*v*pi/4)*M(u+i*tau)*J_N(u+i*tau)].
```

The v-dependent phase has modulus one. The external
`exp(t*pi^2/64)` occurs once.

### Closed scalar Gaussian bound

Write `d0=496`, `t0=1/5`, `a0=sqrt(499/(2*pi))`, and

```
G(c)=exp[2/d0+c+t0*(c+2/d0)^2/(4*(1-t0/d0))]
                                      /sqrt(1-t0/d0).
```

For `sigma in [0,1]`, `0<t<=t0`, exact Gaussian integration gives

```
E exp[(u^2+1)/d0+c*u]
 = exp[(sigma^2+1)/d0+c*sigma
        +t*(c+2*sigma/d0)^2/(4*(1-t/d0))] /sqrt(1-t/d0)
 <= G(c),                       c>=0.                       (B)
```

All terms in the exponent are nonnegative and increase with sigma and t,
so the final inequality follows directly. Extend the two nonnegative
central Gaussian error integrals to the full line. Use the positive-u
bound on the full line and the constant negative-u bound on the full line;
this deliberate overcount costs little at order 8. Combining (A)–(B), the
central exact-gamma remainder before the external heat factor is at most

```
|M0(i*tau)| * Gamma(9/2)*(1.1/a0)^9
                 *[G((3/2)*log 2)/7+G(0)/2]
 < 7.21e-8 * |M0(i*tau)|.                                    (C)
```

After the external heat factor it is below
`7.44e-8 * |M0(i*tau)|`, since `exp(t*pi^2/64)<=exp(pi^2/320)`.
The script's narrower outward bounds are respectively
`7.199610982425e-8` and `7.425124914857e-8`. The numbers are one-channel,
in units of `|M0(i*tau)|`, prior to normalizing by A.

Multiply (C) by the declared normalizer ratio from the disk calculation;
include the two conjugate channels only once. Add the paid exact Gaussian
tail and finite CR coherence mismatch before applying Cauchy. The
central payment cannot be differentiated as a printed pointwise bound.


## Appendix B Coherent extension and physical normalization

Let t in[.01,.2], real center x in[999,1001], and |z-x|<=1. Write z=X+iy.
Use the containing tube X in[998,1002], |y|<=1. Put

    T=X/2+pi*t/8, tau_c=T+i*y/2,
    u=1/2+sqrt(t)*v, |v|<=10,
    u_lambda=u-(1-lambda)*y/2,
    tau_lambda=T+i*lambda*y/2.

Then u_lambda+i*tau_lambda is constant, equal to u+i*tau_c. Thus the exact
M argument and the heat shift phase exp(-i*pi*sqrt(t)*v/4) do not change on
this path. The derivative of A8=U(tau)*a^-u sum_(k=0)^8 Ck(p,u)a^-k is
(i*y/2)(partial_tau-i*partial_u)A8. Use S03 Note 06 equation(10):

    (partial_tau-i*partial_u)A8=-U*a^-u*B8,
    B8=[C8,p/(2pi)+(7+u)C7/(4pi)]a^-9
                                      +(8+u)C8*a^-10/(4pi).

All coefficient identities needed through8 are among the exact Fraction
identities in check_rs_edge_hierarchy.py. No general unproved recurrence
identity or asymptotic error is inferred from finite checks. The natural
cutoff is8 everywhere on this T tube; thus the fixed contour stays the
same while the two finite approximants are connected.

### Uniform endpoint bracket

Along the path Re tau=T in[499.003926...,501.078539...], |Imtau|<=1/2,
u_lambda in[-4.472135955...,5.472135955...]. Principal sqrt has positive
real part. Its real and imaginary parts are stably enclosed using

    aRe >=sqrt(Tlo/(2pi)),
    aRe <=sqrt((sqrt(Thi^2+1/4)+Thi)/(4pi)),
    |aIm| <=1/(8pi*sqrt(Tlo/(2pi))).

The p image lies in the complex disk |p+21/25|<.022338. Direct interval
high derivatives of the rational profile overestimate badly because of
removable-pole cancellations. They are instead enclosed by a point Taylor
series about p0=-21/25, with a separately paid Cauchy tail.

On |p-p0|<=1/4, Re p in[-1.09,-.59], |Im p|<=1/4, whence

    |2cos(pi*p)|>=2sin(.09*pi),
    |numerator|<=exp(1.09*pi/4)+sqrt2*cosh(pi/8),
    |F(p)|<6.952<10.

No denominator zero occurs on this disk. Let f_j be its exact Taylor
coefficients, outward enclosed at 704/768 working bits. For each
0<=k<=25 retain j=0,...,95 in

    F^(k)(p)=sum_j (j+k)!/j! f_(j+k)*(p-p0)^j.

Put q=|p-p0|/(1/4)<.09. The omitted derivative tail is bounded by

    10*k!*(1/4)^(-k)*binom(96+k,k)*q^96
                                /[1-q*(1+k/97)].

The successive positive terms in this Cauchy estimate have ratio at most
q*(1+k/97), so the geometric bound is valid. The largest tail through
k=25 is below2.094e-34. The coefficient polynomials `d[n,k](u)` are generated
with exact Fractions; Horner interval evaluation retains those finite
polynomials. Substitution into C8,C7,C8,p and B8 gives

    |B8|<1.606e-8.

The slightly different outward last digits in the 192+512 and256+512 bit
runs are acceptable: each run separately proves the round ceiling. The
claimed threshold does not depend on a matching hash or overlapping last
digits of upper bounds. Every positive component ceiling is recomputed by
outward arithmetic in each run.

### Exact gamma prefactor

Let s0=i*tau_lambda and gamma=log(a)+i*pi/4. Then

    M(u_lambda+s0)=M0(s0)*exp(u_lambda*gamma+eta),
    eta=S(s0+u_lambda)+m0(s0+u_lambda)-m0(s0)-u_lambda*gamma,
    S=log(M/M0).

The relevant segment has imaginary part >=Tlo and real part of modulus
<=5.973. Using DLMF5.11(ii), after retaining1/(6s),

    |S|<=1/(6Tlo)+4.2/(45Tlo^3),
    |alpha(s0)-gamma|<=3/(2Tlo),
    |alpha'(segment)|<=1/(2Tlo)+3/(2Tlo^2).

The sector cost sec(arg(s)/2)^4<4.2 is checked. Taylor's theorem therefore
bounds

    |eta|<=1/(6Tlo)+4.2/(45Tlo^3)
       +3*5.472136/(2Tlo)
       +(1/(2Tlo)+3/(2Tlo^2))*5.472136^2/2
       <.031876,    exp|eta|<1.032389.

Because u_lambda is real, |exp(i*pi*u_lambda/4)|=1. This leaves only
M0(i*tau_lambda)*U(tau_lambda) outside exp eta. The exact S02 identity is

    M0(i*tau)*U(tau)*exp(i*pi/8)
       =-sqrt(pi)/8*sqrt(tau)*(tau+i)*exp(-pi*tau/4).

For the normalizer use b=(log A)_z, which equals

    -i/4 [alpha(s)(1+t*alpha'(s)/2)
                  -alpha(1-s)(1+t*alpha'(1-s)/2)],
    s=(1-i*z)/2.

Interval evaluation on the tube gives exp(sup|Im b|)<1.000522. Since
log|A(X+iy)|-log A(X) is the vertical integral of -Im b, this pays the
normalizer variation. W_real is exactly

    sqrt(pi)/4*exp(-pi*X/8-pi^2*t/64)/A(X,t),

as algebraically simplified in S02. Thus, including exp(t*pi^2/64) and both
reflected channels, the physical prefactor is at most

    W_real(X,t)*sqrt(|tau|)*|tau+i|*exp(sup|Im b|)<.667289.

This already includes the heat shift; do not add it again. It does not
include exp eta, which is paid separately above. The complete central CR
mismatch, divided by the actual complex normalizer, is therefore

    <=(1/2)*.667289*1.032389*1.606e-8 <5.53e-9.        (CR)

The factor1/2 pays |y|/2, integrating the path length lambda in[0,1]. The
Gaussian central weight integrates to less than1. No fitted source data,
Taylor enclosure for H, or residual table is used.

### Auxiliary approximate-tail polynomial bound

For arbitrary real u on the same complex tau tube, each exact d[n,k]
has degree<=n. If Q=1+|u|, its absolute value is at most its rational
coefficient l1 sum times Q^n. The same profile derivative enclosures give

    |sum_(k=0)^8 Ck(p,u)a^-k|<.472115*(1+|u|)^8.

This is only a polynomial bound for a separate tail proof. The gamma and
Gaussian tails must still be paid; the central |eta| bound above is not
valid uniformly for unbounded u.

Cauchy derivative costs1,1,2 on radius 1 apply to the sum of the real RS,
CR and tail value constants only after establishing that their combined
exact-minus-coherent error is holomorphic. The CR mismatch alone depends
on Re z and Im z and must not be differentiated as a holomorphic error.

## Appendix C Exact infinite Gaussian tails

### Exact fixed-contour Gaussian-tail theorem

For every real pilot center `x0 in [999,1001]`, `t in [.01,.2]`, and every
`|z-x0|<=1`, the two reflected exact shifted edge integrals restricted to
`|v|>10`, divided by the actual complex `A(z,t)`, have sum of absolute values `<1.4e-41`.
No source/H values, fitted coefficients, or adaptive RS order enter.

Write `c=17/2`, `w=c+(1+i)r`, `r real`, and

```
J8(s)=integral_(8 southwest 9) w^(-s) exp(i*pi*w^2)
                           /(exp(i*pi*w)-exp(-i*pi*w)) dw.
s=sigma+i*T,  T in [499,502],  a=sqrt(T/(2*pi)).
```

Orientation does not affect the absolute estimate. Since
`|sin(pi*w)|^2=cos(pi*r)^2+sinh(pi*r)^2>=1`, its denominator has
modulus at least 2 everywhere. The phase exponent is

```
F(r)=T*arg(w)-2*pi*c*r-2*pi*r^2.
```

For `r>=-c`, `arg(w)<=r/c`: differentiate `arg(w)-r/c`, whose derivative
is `-2*r*(c+r)/(c*|w|^2)`, and use its value zero at r=0.
Thus `F<=L*r-2*pi*r^2<=L^2/(4*pi)-pi*r^2`, where
`L=T/c-2*pi*c`. For `r<-c`, use `arg(w)<=-pi/2`; then

```
F(r)+pi*r^2 <= pi*c^2-pi*(r+c)^2-pi*T/2 < 0.
```

Here `T/2>c^2`. Uniformly `L>0` and `L^2/(4*pi)<3`.
The logarithmic magnitude satisfies

```
|log(|w|/a)| <= |log(c/a)|+2*|r|/c < .051+2*|r|/c,
```

because `|w|>=c/sqrt(2)` and the logarithmic derivative along r is at
most `2/c`. Combining denominator and phase, and completing the square
on both half-lines, gives

```
|J8(s)| <= sqrt(2)*a^(-sigma)
              *exp(3+.051*|sigma|+sigma^2/(pi*c^2)).       (A)
```

The true gamma factor is `M(s)=s(s-1) pi^(-s/2) Gamma(s/2)/16`.
The primary source logarithmic Stirling estimate and the direct bound
`|alpha'|<=1/[2*(T-3)]` on the entire horizontal line imply

```
|M(s)*a^(-sigma)/M0(i*T)| <=
 exp(1/[6*(T-.66)]+3*|sigma|/(2*T)+sigma^2/[4*(T-3)]).     (B)
```

For (B), expand `m0` horizontally at `i*T` and use
`|alpha(i*T)-log(a)-i*pi/4|<=3/(2*T)`; there is no restricted sector at
large positive or negative sigma. (A)--(B), with outward constants checked
at 192 bits, give

```
|M(s)*J8(s)/M0(i*T)| < 30*exp(.055*|sigma|+.005*sigma^2).
```

On the disk, `|sigma|<=1+sqrt(.2)*|v|`. Therefore the normalized Gaussian
integrand is bounded by

```
30/sqrt(pi)*exp(.065+.025*|v|-.997*v^2).
```

The slightly weakened quadratic coefficient avoids endpoint rounding.
The two tails at v=10 have total integral at most

```
60*exp(.065)/sqrt(pi)
 * exp(-.997*100+.025*10)/(2*.997*10-.025) < 8e-43.          (C)
```

This is an elementary exponential Mills bound, obtained by replacing the
logarithmic derivative beyond 10 by its boundary upper bound.
The heat scalar is `<1.04`.

Finally use `A(X,t)=|M_t(1/2+i*X/2)|`, where `X=Re z` is in the
expanded real interval [998,1002]. On the connecting segment from `i*T`
to `1/2+i*X/2`, `|alpha|<2.4` and `|X/2-T|<=pi*.2/8`, so

```
|M0(i*T)|/A(X,t)
 <= exp(2.4*sqrt(1/4+(pi*.2/8)^2)) <4.
```

The heat deformation only enlarges the denominator because
`Re(alpha(1/2+i*X/2)^2)>0`: its real part exceeds 2.18 and its imaginary
part has modulus below .79. The already separately checked complex
normalizer vertical cost is `A(X,t)/|A(z,t)|<1.000522` on this tube.
Two reflected channels multiply (C), 1.04, 4 and 1.000522 by two;
`<1.4e-41` remains a safe round payment, now explicitly in actual complex
normalizer units. The actual scalar product in the checker is much smaller.
Cauchy is applied to the entire exact-minus-coherent normalized error;
its radius-one derivative costs are factors `1,1,2` for orders 0,1,2.
This tail majorant is one summand in that complete holomorphic-error bound.

The retained approximate Gaussian tail is a separate payment unless the
retained approximation is integrated only on [-10,10].


## Appendix D Gaussian polynomial model and its derivatives

### Implementation audit

Reviewed the [retained arithmetic estimator](../numerics/estimate_arithmetic_residual_increment.py),
including the finite phase-cancellation formula. Its eta formula, b derivatives,
coherent profile derivatives, coefficient recurrence, and entire Gaussian
moments are consistent. Specifically, writing `b=i*tau`, `u=.5+w`,

```
eta(u)=((b+u+1)/2)log(1+u/b)+log(1+u/(b-1))-u/2+S(b+u),
S(z)=log(M(z)/M0(z)).
```

The first logarithm's k=1 term cancels `-u/2` and leaves
`(u+u^2)/(2b)`. The code's terms k=2..24, plus the other logarithm's
terms k=1..24, are exactly the two prescribed log series. The retained
Stirling terms `1/(6z)-1/(45z^3)+8/(315z^5)` are the first three
logarithmic-gamma coefficients for Gamma(z/2).

In `g_series`, `eb,ebb` are partial-b derivatives of this explicit eta
approximant. Since physical `b_x=i/2`, its value/derivatives are
`g`, `(i/2)*g*eb`, and `-g*(eb^2+ebb)/4`. Truncation at w-degree12
commutes with these parameter derivatives. For the profile coefficients,
`gamma_x=(log a)_x=1/(4tau)`, `gamma_xx=-1/(8tau^2)`,
`p_x=-1/(4pi*a)`, `p_xx=-p_x*gamma_x`; the code's product-rule rows
include all these terms. The product has degree<=12+8=20 in w, and
`E w^(2j)=(t/2)^j*(2j-1)!!`; the code integrates every retained even
coefficient, and every odd term has mean zero.

The rotating finite expression is also exact. If
`q=2Re(exp(i*theta)H)`, then

```
exp(-i*theta)*(q-i*q_x/omega)
 =2H-i/omega*[H_x+exp(-2i*theta)*conj(H_x)].
```

The conjugate derivative is valid on real x. This form cancels the
leading phase algebraically before interval evaluation.

### Complete model approximation payment

The mathematical error estimate is on the radius-one physical-x tube,
not just real sample points. Write `tau=T+i*y/2`, where
`T in[499,502]`, `|y|<=1`, and use complex `|w|<=16`. Then
`|u|<=16.5`, `|b|,|b-1|>=499`, and `|b+u|,|b+u-1|>=482.5`.
The gamma argument remains strictly in the upper half-plane, so all
logarithms and the true exponential prefactor are holomorphic on the
domain. Direct horizontal/complex Taylor bounds yield

```
|eta| <=1/[6*(482.5-.66)]+3*16.5/(2*499)
        +[1/(2*482.5)+3/(2*482.5^2)]*16.5^2/2 <.192.
```

The logarithm approximation error is bounded by the elementary log tail
`q^25/[25(1-q)]`, `q=16.5/499`, with multipliers at most
`(503+16.5+1)/2` and1. Its total is `<1.05e-36`.
For the logarithmic Stirling expansion after the retained three terms,
DLMF5.11(ii) gives

```
|S(z)-[1/(6z)-1/(45z^3)+8/(315z^5)]|
 <=8*sec(arg(z)/2)^8/[105*|z|^7] <2.312e-19.
```

Here `|arg z|<=pi/2+atan(17/482.5)` and the secant cost is below20.
Thus both true and approximate eta have modulus below .2 and their
exponentials have modulus below1.3 on the w-circle of radius 16. The
true exponent versus approximant exponent error is at most
`exp(.2)*2.312e-19`.

Let P12 be the degree12 Taylor polynomial of the explicit approximant
exponential about w=0. On the central Gaussian interval, `|w|<=sqrt(.2)*10`,
Cauchy's coefficient estimate gives

```
|gtilde-P12| <=1.3*(|w|/16)^13/[1-|w|/16].
E |w|^13 <=.2^(13/2)*Gamma(7)/sqrt(pi).
```

Hence its Gaussian mean is below `4.659e-18`. The independently verified
coherent coefficient majorant is
`|S8(u,tau)|<.473*(1+|u|)^8`; on the central interval this is below
765418. Including the retained log/Stirling approximation error, the
weighted central mean error is `<3.782e-12` before the physical prefactor.

The root profile uses the degree120 Taylor polynomial about `p0=-21/25`.
The coefficient bound `|f_j|<=10*(1/4)^(-j)` is proved on the disk
`|p-p0|<=1/4`, and the complete physical tube has `|p-p0|/(1/4)<.09`.
For every derivative order `0<=n<=26`, the omitted k>=121 tail is at most

```
10*n!*(1/4)^(-n)*binom(121,n)*.09^(121-n)
                         /[1-.09*122/(122-n)].
```

The maximum is `<1.793e-30`. The exact recurrence's coefficient l1 sum,
including powers of pi and a but replacing each profile derivative by1,
is `<1.029`. Whole-Gaussian polynomial moments of the P12 coefficient
majorant times `(1+|u|)^8` pay the resulting profile discrepancy by
`<3.187e-28` before the physical prefactor; the separately subtracted F versus F_hat
tail is added as well and is below 2e-125. The floating balls used to
compute retained Taylor coefficients already propagate outward; this
payment covers the omitted analytic tail.

Finally the model integrates P12*S8 over the entire Gaussian line, so
its polynomial tail outside v=10 is paid. From Cauchy,
`|P12|<=13*1.3*(1+sqrt(.2)*|v|/16)^12`; combine this with the S8
polynomial majorant. At v>=10 the logarithmic derivative of the
polynomial times exp(-v^2) is below -19. Evaluating its boundary value
and dividing by19 gives the two-tail allowance `<5.503e-37` before the
physical prefactor. This also accounts for all unbounded negative-u
model values without applying a central eta estimate at infinity.

The already audited both-channel physical prefactor is `<.667289`,
including the heat scalar and division by the actual complex A(z,t).
Consequently the complete model replacement payment is `<2.524e-12`;
**`1e-11` is a safe uniform normalized value ceiling**.

This is one payment in the complete arithmetic edge bound. Add central
real RS8, finite CR mismatch and exact edge Gaussian tails. Only after
that sum bounds the complete holomorphic exact-minus-model normalized
error may radius-one Cauchy give derivative ceilings `epsilon,2epsilon`.



[note03]: 03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md
[note06]: 06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[edge-record]: ../numerics/S03_G3_COMPLETE_EDGE_BOUND_20261019.json
[increment-record]: ../numerics/S03_G3_ARITHMETIC_INCREMENT_20261019.json
[control-record]: ../numerics/S03_G3_EDGE_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/07_COMPLETE_ARITHMETIC_EDGE_AND_INCREMENT_INTERNAL_REVIEW_20261019.md
