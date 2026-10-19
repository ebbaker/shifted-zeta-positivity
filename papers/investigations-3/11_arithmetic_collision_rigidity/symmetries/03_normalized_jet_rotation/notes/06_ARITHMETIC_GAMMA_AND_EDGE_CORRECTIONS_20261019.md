# Arithmetic gamma and edge corrections behind residual rotation

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol**, reasoning effort
**ultra**. Separate delegated same-model mathematical review and replay;
no independent specialist review.

## Finding and scope

G3 has a concrete partial arithmetic explanation. The retained Dirichlet
modes omit a prescribed logarithmic Stirling correction and a Gaussian
curvature correction. The finite correction admits an independent uniform
relative remainder, including two spatial derivatives. The Riemann–Siegel
edge has another omitted correction of comparable size and opposite sign
at the pilot center. Its gamma prefactor is essential: the first omitted
RS coefficient alone has the wrong sign to explain that cancellation.

At `t=21/200, x=1000`, the exact finite-mode defect is approximately
`+0.000133439545`; the exact edge discrepancy is approximately
`-0.000136027672`; their sum is the observed defect
`-0.000002588127`. These are enclosed **point decompositions**, with the
edge inferred from the complete source enclosure. The unusually small
center difference is phase dependent, not a uniform cancellation law.
The complete independently bounded edge and signed prefix allowance
remain open. S03-T1/T2/T3 retain their earlier bounded completion status;
this continuation does not replace their complete-source comparator.

Classification under [avoid/01][a01]: a bounded finite-component theorem
and a prescribed arithmetic diagnostic, rather than a new RH-equivalent
criterion. The [result entry points][results] and [avoid entry points][avoid]
apply, particularly [controls][controls], [scoped claims][a07], and
[signed recombination][a12]. The quantitative gain is the finite-mode
remainder theorem below; the point hierarchy explains which omitted terms
matter without fitting them to H.

## Exact arithmetic split

Use the fixed pilot
`B=[1/100,1/5] x [999,1001]`, fixed cutoff `N=8`, and all branches,
normalizer A, phase theta and coherent full correction Chat from
[Note 03](03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md).
Let `s=(1-ix)/2`, `alpha=m0'`, and

```
M(s)=s(s-1) pi^(-s/2) Gamma(s/2)/16,
m0(s)=log s+log(s-1)-s log(pi)/2+log(2pi)/2-log16
      +(s/2-1/2)log(s/2)-s/2,
g_n=exp(m0(s)-s log n+t(alpha(s)-log n)^2/4),
r_n=E_v[M(s+sqrt(t)v) n^(-s-sqrt(t)v)],
E_v f=pi^(-1/2) integral_R exp(-v^2) f(v) dv.
```

The exact Gaussian and fixed-contour Riemann–Siegel decomposition is
available in [Polymath 2019, section 4](https://arxiv.org/html/1904.12438v2#S4).
For the conjugate positive channel `s+=(1+ix)/2`, let E_8(s+) denote
M(s+) times the usual descending RS contour crossing `(8,9)`. Then

```
H=2 Re[sum_(n=1)^8 r_n(conjugate channel)+E_v E_8(s+ +sqrt(t)v)],
f=(G_8-Chat_8)/A,
r=H/A-f=r_AB+r_edge,
r_AB=2 Re sum_(n=1)^8(r_n-g_n)/A,
r_edge=2 Re E_v E_8(s+ +sqrt(t)v)/A+Chat_8/A.                 (1)
```

The plus sign on Chat in the edge discrepancy follows by subtraction.
No cutoff derivative occurs. This representation uses the actual gamma
factor and its matching arithmetic contour, independently of the Taylor
polynomial used to enclose H.

Put `b=(log A)_x`, `mu=omega_x/omega`, `omega=theta_x`, and

```
D=partial_x-b,
L=D^2-mu D+omega^2,
R(q)=q+q_xx/omega^2-omega_x q_x/omega^3,
R(V/A)=L V/(A omega^2).                                  (2)
```

This gives an exact arithmetic filtered functional as well. For the
positive channel, set `aM=M'/M`, `q1=-2b-mu`, and
`q0=omega^2+b^2-b_x+mu b`. Applying L to an exact mode or the RS
integrand multiplies it by

```
B(s,ell)=-[(aM(s)-ell)^2+aM'(s)]/4
                    +i q1(aM(s)-ell)/2+q0.                 (3)
```

Here `ell=log n` for a finite mode and `ell=log w` on the contour.
Thus signed recombination can precede absolute estimates. Formula (3)
is an exact alternative source representation, not an evaluated complete
prefix bound.

## Explicit finite-mode correction and its filtered action

Completing the Gaussian square gives the no-fit first correction

```
kappa_n=1/(6s)+alpha'(s)[t/4+t^2(alpha(s)-log n)^2/8],
r_n=g_n(1+kappa_n+e_n).                                    (4)
```

The first term comes from logarithmic Stirling expansion. The second is
the expected quadratic curvature of m0 under the shifted Gaussian. Both
are fixed by M and the heat convolution; no physical source values enter.
The proof below establishes, uniformly on B for every `1<=n<=8`,

```
|e_n|<6e-7,   |e_n,x|<6e-8,   |e_n,xx|<1.2e-8.              (5)
```

These are relative errors of eight finite gamma/heat modes. They are not
bounds for r or for the complete H remainder.

Write `g_n=A exp(i theta)p_n` and

```
lambda_n=i log n [1+t alpha'(s)/2]/2,
lambda_n,x=t log n alpha''(s)/8,
sigma_n=lambda_n^2+lambda_n,x+(2i omega-mu)lambda_n.
```

The exact product rule yields

```
L(g_n kappa_n)=g_n[sigma_n kappa_n
             +(2i omega+2lambda_n-mu)kappa_n,x+kappa_n,xx]. (6)
```

The same expression holds with e_n. At n=1, lambda and sigma vanish,
so only derivatives of the slowly varying kappa remain. This explains
why the largest value correction can have a much smaller rotation defect.
It does not annihilate the other seven modes. Their logarithmic mode
symbols and signed phases must be retained. A safe finite error payment is

```
|R_error| <= 2/|omega|^2 sum_n |p_n|[
          6e-7 |sigma_n|+6e-8 |2i omega+2lambda_n-mu|+1.2e-8]. (7)
```

The factor 2 pays both reflected channels. Formula (7) is only the
finite-mode remainder after the signed retained correction (6).
The [192/256-bit full-box ledger](../numerics/S03_G3_HEAT_STIRLING_REMAINDER_20261019.json)
uses one outward interval image of B and gives normalized value error
`<5.206260e-6`, first derivative `<3.404651e-6`, second derivative
`<2.961263e-6`, and filtered remainder `<3.874872e-6`.
These bounds pay (5) only; the retained kappa correction and edge remain
signed terms of the complete functional.

## Certified point decomposition

[Exact mode record](../numerics/S03_G3_EXACT_MODES_20261019.json) evaluates
actual gamma–Gaussian integrals and their first two physical-x derivatives
at five declared points, with infinite Gaussian tails paid. Both 192- and
256-bit runs reuse the same historical 192-bit complete-source setup;
this is not a second source quadrature. The center values below are
rounded descriptions; the record holds the outward balls.

| Center quantity | Normalized value | Rotation defect |
| --- | ---: | ---: |
| Complete residual r | -0.000802214368463 | -0.000002588127166 |
| Exact finite correction r_AB | -0.000664858244033 | +0.000133439544937 |
| First correction from (4) | -0.000664954678964 | +0.000133427570832 |
| Exact finite correction minus (4) | +0.000000096434930 | +0.000000011974105 |
| Inferred exact edge discrepancy | -0.000137356124430 | -0.000136027672101 |
| n=1 part of (4) | -0.000679357037247 | -0.000000487150957 |

The complete center defect ball has radius below `7.1e-11`; the finite
Gaussian integrations are much tighter. At the same time and x=999,
the complete defect is about `+0.000292972`, while at x=1001 it is about
`-0.000237490`. There is no evidence here for extending the center's
relative cancellation uniformly over B.

The exact-edge row uses the source enclosure minus the independently
integrated finite part. It diagnoses the location of the missing arithmetic
contribution and cannot be reused as an independent edge allowance.

## Why the omitted edge has the required scale and sign

For the positive channel put

```
tau=x/2+pi t/8, a=sqrt(tau/(2pi)), p=17-2a,
u=1/2+sqrt(t)v, gamma=log a+i pi/4,
F(p)=[exp(i pi(p^2/2+3/8))-i sqrt(2)cos(pi p/2)]/[2cos(pi p)],
eta(u)=log M(i tau+u)-m0(i tau)-u gamma.
```

The full edge bracket is `E_v[exp(eta)(F+C1/a+...+CK/a^K+RS_K)]`.
The retained Chat uses F with `exp(eta)=1`. In particular the gamma
prefactor contributes at the same relevant scale as the first RS terms.
The explicit coefficient

```
C1(p,u)=F'''(p)/(12pi^2)+i(u-1/2)F'(p)/(2pi)                (8)
```

agrees with [Arias de Reyna 2024, section 5](https://arxiv.org/html/2407.06681v1#S5).
Expanding eta to its first relevant terms gives

```
eta_bar=1/(6i tau)+(1/(2i tau)+1/(i tau-1))/2
                       +alpha'(i tau)(1/4+t/2)/2.
```

At the center, the separate explicit normalized defects of `C1/a` and
`eta_bar F` are respectively about `+0.000136116053` and
`-0.000268360449`. Thus C1 alone has the wrong sign; its combination
with the true prefactor explains the sign and scale. The Gaussian mean
of C2 adds about `+0.000000880214` to the defect, with

```
E C2=F^(6)/(288pi^4)+(1-t)F''/(16pi^2)
                                      +i(t/2-1/12)F/(8pi).
```

The prescribed hierarchy with the full exact gamma prefactor gives:

| Truncation K | Finite Gaussian edge defect |
| --- | ---: |
| 0 | -0.000268779287763 |
| 1 | -0.000137074289323 |
| 2 | -0.000136166638310 |
| 3 | -0.000136028672050 |
| 4 | -0.000136027976091 |

These enclosed finite integrals reproduce the inferred edge scale
without fitting. **Gaussian tails and RS_K are unpaid in this hierarchy**;
its rows are diagnostics, not complete edge enclosures. The
[replay](../numerics/S03_G3_RS_EDGE_HIERARCHY_20261019.json) preserves
that distinction.

## A finite identity for the remaining coherent edge payment

The exact RS coefficient recurrence in
[Arias de Reyna 2022, equations 29 and 86–89](https://arxiv.org/html/2201.00342)
gives, at the finite orders checked,

```
partial_u Cj=i[C_(j-1),p/(2pi)+(j-2+u)C_(j-2)/(4pi)].       (9)
```

Only this algebraic recurrence is imported; that preliminary paper's
plot-tested numerical inequalities are not used. There are 126 exact
rational polynomial checks through j=12 in the hierarchy replay.

Let `A_K=U(tau)a^-u sum_(k=0)^K Ck(p,u)a^-k`, where
`U_tau/U=-i log a`. Direct differentiation using (9) telescopes to

```
(partial_tau-i partial_u) A_K = -U a^-u {
 [C_K,p/(2pi)+(K-1+u)C_(K-1)/(4pi)]a^(-K-1)
                         +(K+u)C_K a^(-K-2)/(4pi)}.        (10)
```

For complex physical `z=X+i y`, the printed real-tau approximation
uses `(u-y/2,tau)` and the coherent approximation uses `(u,tau+i y/2)`.
On the connecting path

```
u_lambda=u-y/2+lambda y/2,
tau_lambda=tau+i lambda y/2,
```

the argument `u_lambda+i tau_lambda` of the exact gamma factor stays
constant and `dA_K/dlambda=(iy/2)(partial_tau-i partial_u)A_K`.
The integral of the explicit endpoints in (10) can therefore pay the
coherence mismatch. Combining that payment with the real RS remainder,
negative-u order selection, and Gaussian tails would give a valid
complex-disk remainder, after which Cauchy pays physical derivatives.
Differentiating a printed real value inequality is insufficient.

The next bounded G3 task is to evaluate this **complete edge jet payment
on B**, combine it with (5)–(7), and test the signed prefix against
`0.000266448`. Keep B and N=8 fixed. Stop if the complete allowance
fails to improve the analytic-only or source-informed comparison; do not
start another consumer sweep before the edge estimate is available.
A height-uniform extension needs its own parameterized estimates.

## Controls and reproducibility

The [fresh inherited source control replay](../numerics/S03_G3_SOURCE_CONTROLS_20261019.json)
rejects five event boxes using their own source errors and rejects the
Euler negative-Laguerre witness in the unchanged sign consumer. No new
acceptance consumer is introduced by this note. The premise screen is:

| Control family | Premise absent from this arithmetic application |
| --- | --- |
| Finite-prime and weighted-square | Full normalized theta reflection with unchanged complete coefficients |
| Reflected, shape and positive-primitive | The specific unchanged theta square expansion and matching RS contour |
| Euler-factor deformation | The unchanged level-one completed arithmetic field and coefficients |
| Generic polynomial event | Exact gamma modes and their matching arithmetic edge |

All share the formal rotation/filter identities where defined; those
identities cannot distinguish them. The finite-mode theorem also applies
to those gamma modes wherever they occur and by itself excludes no event.

Replay commands and source pin requirements are in the
[numerics guide](../numerics/README.md). The
[separate same-model review](../reviews/06_ARITHMETIC_GAMMA_AND_EDGE_INTERNAL_REVIEW_20261019.md)
checks the theorem, point integration/tails, signs, normalizer derivatives
and finite telescoping identity. It does not supply the open edge bound.

## Proof of the bounded finite-mode remainder

### Exact shift and the retained correction

Shift the Gaussian contour to `v=w+sqrt(t)*a/2`; no poles are crossed
because the imaginary part of `s+sqrt(t)*v` remains below `-494` on the
intervening strip. Gaussian decay beats the at-most `exp(O(|w| log |w|))`
gamma growth at both ends. With

```
delta=sqrt(t)*w+t*a/2,
S(z)=log(M(z)/M0(z)),
h=S(s+delta)+m0(s+delta)-m0(s)-alpha(s)*delta,
E f=pi^(-1/2) integral_R exp(-w^2) f(w) dw,
```

the exact identity is `r_n/g_n=E exp(h)`. The logarithm of gamma here is
its analytic Stirling branch in the lower half-plane, not necessarily
the principal logarithm of its value.

Since `E delta^2=t/2+t^2*a^2/4`, the expectation of

```
q=1/(6*s)+alpha'(s)*delta^2/2
```

is exactly `kappa_n`. The first term is the first logarithmic Stirling
coefficient of `Gamma(s/2)`; the second is the Gaussian expectation of
the first curvature term in the logarithm of `M0`.

### Uniform central payment

The enlarged domain is the union of closed radius-5 complex s discs
about `(1-ix)/2`, `999<=x<=1001`, for each real `t` in the pilot.
On this domain,

```
494.5 <= |s|, |s-1|,       |s| < 505.6,
|a| < 2.35,               |Im a|<.8,
|t*a/2| < .235,           |Im(t*a/2)|<.08.
```

For example, the rational part of alpha has modulus at most
`1.5/494.5`; its logarithmic real part is between
`.5 log(494.5/(2*pi))` and `.5 log(505.6/(2*pi))`, and its logarithmic
imaginary part has modulus less than `.5*(pi/2+5.5/494.5)`.
Since
`Re alpha >= .5 log(494.5/(2pi))-1.5/494.5 > log 8`, subtracting
`0<=log n<=log 8` reduces its positive real part and gives `|a|<2.35`.

Restrict temporarily to `|w|<=40`; then `|delta|<18.2` and every point
of the segment from `s` to `s+delta` has modulus and distance from 1
greater than `476`. Direct differentiation gives

```
alpha'=-1/(2*s^2)-1/(s-1)^2+1/(2*s),
alpha''=1/s^3+2/(s-1)^3-1/(2*s^2),
|alpha'(s)| < .00102,
sup_segment |alpha''| < 2.25e-6.
```

The logarithmic Stirling remainder after `1/(6*z)` obeys

```
|S(z)-1/(6*z)| <= sec(arg(z)/2)^4/(45*|z|^3).
```

This is the `n=2` logarithmic-gamma error bound in
[DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii), applied at `z/2`.
On this central region, `|Re z|<23.7`, `|Im z|>494.4`, so
`|arg z|<1.619` and `sec(arg(z)/2)^4<4.5`. Thus

```
|S(s+delta)-1/(6*(s+delta))| < 9.3e-10.
```

Taylor's formula and the reciprocal difference now give

```
|h-q| <= c1*|delta|+c3*|delta|^3+c0,
c1=1/(6*494.5*476),  c3=3.75e-7, c0=9.3e-10,
|h| <= A+B*|delta|^2+C*|delta|^3,
A=.000351, B=.00051, C=3.75e-7,
|h| < .172.
```

All expectations below can be extended to the full real Gaussian
because their integrands are positive. With `d=sqrt(.2)*|w|+.235`,
`|delta|<=d`, and Gaussian absolute moments
`E|w|^k=Gamma((k+1)/2)/sqrt(pi)`, the elementary binomial bounds are

```
E d < .488, E d^2 < .275, E d^3 < .177,
E d^4 < .128, E d^5 < .102, E d^6 < .089.
```

They imply

```
E |h-q| < 4.14e-7,
E |h|^2 < 2.56e-7,
exp(.172)<1.188,
E |exp(h)-1-q| < 4.14e-7+1.188*2.56e-7/2
                       =5.66064e-7.
```

The last step uses the exact exponential remainder inequality
`|exp(h)-1-h| <= exp(|h|)*|h|^2/2`.

### Both Gaussian tails

Here is an intentionally coarse independent tail payment, avoiding
application of a fixed-sector asymptotic expansion at infinity on a
horizontal line. Write `u=|w|>=40`, `z=s+delta`, and
`sigma=Re(z/2)`. The enlarged-domain geometry gives

```
|Im(z/2)|>247,     sigma <= 3+.224*u,
|z|, |z-1| <= 507+.45*u.
```

For `sigma<=1`, gamma recurrence shifts to a real part in `[1,2]`;
the gamma integral and log convexity yield `|Gamma(z/2)|<=1`.
For `sigma>=1`, the gamma integral implies
`Gamma(sigma)<= (2*sigma)^sigma`: bound
`exp(-v/2)*v^(sigma-1)` by its maximum and integrate the remaining
`exp(-v/2)`. Thus

```
log |Gamma(z/2)| <= max(0,sigma*log(2*sigma))
                    <= .09*u^2,
```

using `sigma<=.3*u` and `log(2*sigma)<=sigma` when `sigma>=1`.
Also, directly from the formula for `m0`, `Re m0(s)>-450` throughout
the enlarged domain. In fact using `|s|>=494.5`, `|s|<505.6`,
`-4.5<=Re s<=5.5`, `|Im s|<=505.5`, and
`|arg s|<=pi/2+5.5/494.5` already gives a lower bound above `-420`.

The remaining exact shifted-integrand factors obey, for `u>=40`,

```
|z(z-1)|/16 <= exp(.01*u^2),
|pi^(-z/2)*exp(-alpha(s)*delta)| <= exp(.04*u^2).
```

For the second inequality, its logarithm is at most
`(6+.45*u)*log(pi)/2+2.35*(.235+.45*u)`
`<4+1.32*u <= .04*u^2`; the last inequality is true at 40 and its
right-minus-left derivative is positive afterwards. The first is checked
at 40 and by the same derivative comparison. Consequently

```
exp(-w^2)*|M(s+delta)/M0(s)*exp(-alpha(s)*delta)|
  <= exp(450-.86*u^2).
```

Both normalized exact tails combined have integral less than `1e-300`;
the upper bound `2 exp(450-.86*40^2)/(2*.86*40*sqrt(pi))` suffices.
The tails of `1+q` are even smaller, by direct polynomial-Gaussian
integration: on `u>=40`, `|1+q|<=1.001+.000107*u^2`
`<exp(u^2/4)`, giving a tail smaller than the integral of
`exp(-3*w^2/4)`. Hence the full error is below `6e-7`.

### Derivative payment and the existing annihilator

For each real x in B, the holomorphic relative error is bounded on the
closed radius-10 x disc because that disc maps to the radius-5 s disc.
Cauchy's formula yields the stated first and second spatial derivatives;
no derivative of a fitted or tabulated error is taken.

For `g_n=A exp(i theta) p_n` and the physical operator L in S03 Note 03,
the exact correction identity is

```
L(g_n*kappa_n)=g_n*[sigma_n*kappa_n
                   +(2*i*omega+2*lambda_n-mu)*partial_x kappa_n
                   +partial_x^2 kappa_n],
L(g_n*e_n)=g_n*[sigma_n*e_n
               +(2*i*omega+2*lambda_n-mu)*partial_x e_n
               +partial_x^2 e_n].
```

Thus the modewise filtered remainder is paid by

```
|L(g_n*e_n)|/A <= |p_n|*[6e-7*|sigma_n|
       +6e-8*|2*i*omega+2*lambda_n-mu|+1.2e-8].
```

Sum the two reflected channels and the eight modes only after retaining
the signed **correction** expression. The error bound itself may be
summed by the displayed safe triangle bound. The edge residual and all
its value/derivative payments remain separate obligations.

The leading scaling is explicit: `c1,c3=O(|s|^-2)`, the retained
Stirling and curvature terms are `O(|s|^-1)`, and their exponential
remainder is quadratic. This proves the bounded numerical assertion.
An asymptotic theorem over a growing-height family would additionally
need height-dependent tail geometry and the declared growth of n;
no global claim is made here.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
