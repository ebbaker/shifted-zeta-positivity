# Effective full-buffer outer field estimate on [95,97]

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from turn metadata. Chat **0015**, thread
`01a1711d-376c-7de3-929c-60ec4065bddc`.

**Status: explicit field/jet bounds proved in-note; same-model internal
review only.** This returns [HDA-18-AN03 r1](../research-progress/handoffs/HDA-18-AN03.md).
There is no failed contour bound. The constants below pay every part of
Note 30's full complex-buffer field comparison on the requested compact
time interval, at a deliberately enormous explicit onset. This pays the
previously uninstantiated theta-field debit FI23. It does not instantiate
all collar, signed-pole, weighted-regulator or observable budgets, choose
an affordable finite source, or complete HDA-18.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared review](../../../../avoid/05_same_model_reviews_and_shared_premises.md).
This is an approximation estimate, not an RH criterion. The
[input manifest](45_EFFECTIVE_OUTER_INPUTS_20261025.json) pins the request
and predecessor notes and records the primary passages inspected.

## 1. Explicit result and unchanged model

Keep H, P=P_*, M, alpha=M'/M, p, B and S_t exactly as in
[Note 30](30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md) FS1–FS4:

    M(w)=w(w-1) pi^(-w/2) Gamma(w/2)/16,
    p=w+(t/2)alpha(p), B=1-(t/2)alpha'(p),
    S_t(w)=M(p)exp(-(p-w)^2/t)/sqrt(B),
    P(t, z)=S_t((1+iz)/2)+S_t((1-iz)/2).

The square root remains the branch near one. For z=xi+iy put x=|xi|,
L=log(2+x), and

    A(t, z)=|S_t((1+iz)/2)|+|S_t((1-iz)/2)|.

All statements below are uniform for 95<=t<=97. On the **full strip**
|y|<=5, the explicit field estimate is

    |H(t, z)-P(t, z)| <=12000 A(t, z)/x^2,
                                      x>=2^2048.        (EF1)

On |y|<=9/2, hence on the required smaller strip |y|<=4, full Cauchy
circles give

    |partial_z^j(H-P)| <= C_j A(t, z)L^j/x^2,
                         j=0,1,2,3, x>=2^2049,         (EF2)

with

| j | C_j |
| --- | ---: |
| 0 | 12000 |
| 1 | 384000 |
| 2 | 3072000 |
| 3 | 36864000 |

These onsets are finite theorem parameters, not practical proposed
numerical cutoffs. No theta, gamma or field values were sampled. The
canonical source, normalization, physical regulator and actual covariance
of Note 43 are unchanged. The field proof is independent of q.

## 2. Explicit gamma input and a finite saddle branch

The first omitted digamma term and the complex-remainder rule in
[DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii), with n=1, give

    psi(v)=Log v-1/(2v)+Rpsi(v),
    |Rpsi(v)|<=sec^3(arg(v)/2)/(12|v|^2).

Use the principal logarithm away from the negative axis. Consequently,
for Re p>=2 and m=|p|>=4096,

    alpha(p)=0.5 Log(p/(2pi))+r(p), |r(p)|<=2/m,
    |alpha^(j)(p)|<=j!/m^j,                    1<=j<=4. (EF3)

Here r(p)=1/(2p)+1/(p-1)+Rpsi(p/2)/2. To justify the derivative
constants, the circle |p'-p|=m/4 lies in |arg p'|<3pi/4,
|p'|>=3m/4. There |r(p')|<=4/|p'|<=6/m. The rational factors and
gamma remainder are analytic there even if that circle crosses the
imaginary axis; the negative axis and 0,1 remain outside. Cauchy gives

    |r^(j)(p)|<=6 j! 4^j/m^(j+1).

Adding the logarithm's derivative proves EF3 because
1/(2j)+6*4^j/4096<1 for j<=4. The original, right-half-plane bound
|r|<=2/m follows directly using sec^3(arg(p)/2)<3.
This is a complex remainder on an analytic circle, not differentiation
of an asymptotic allowance.

It is enough to prove the remaining estimates for x>=exp(1000), which
includes x>=2^2048 since log2>1/2. Write lambda=log x>=1000. Each arm,
using conjugation for its negative imaginary part, has

    w=sigma+iT, -2<=sigma<=3, T=x/2.

The contraction rectangle is

    sigma+t lambda/8<=Re p<=sigma+t lambda/2,
    T<=Im p<=T+t.                                      (EF4)

On it x/2<=|p|<=x. For the upper bound use Re p<=3+49lambda,
Im p<=x/2+97 and exp(lambda)>=lambda^4/24; these elementary bounds
also give T>=Re p and Re p>2. EF3 yields

    (lambda-3)/2-4/x <= Re alpha(p) <= lambda/2+4/x,
    0<Im alpha(p)<1.                                   (EF5)

For the imaginary lower bound use arg p>=pi/4 and |r|<=4/x; the
upper bound is pi/4+4/x<1. The logarithmic lower bound uses
log(4pi)<3. Thus p->w+t alpha(p)/2 maps EF4 strictly into itself and
has Lipschitz constant <=97/x<1/2. Its unique fixed point is holomorphic
in w on a neighborhood of the full strip by its interior margins and
B!=0. Uniqueness makes overlapping local branches agree.

At the fixed point, with v_*=p-w=a+ih,

    t lambda/5<=a<=t lambda/3, 0<h<t/2,
    |B-1|<=97/x, 1/2<|B|<3/2, Re B>1/2.                (EF6)

The stronger a bounds follow by substituting EF5; lambda>=1000 has
ample margin. They also put the fixed point in the original FS9
rectangle with mathcal L=log(2+t+x), where the same finite contraction
bounds apply. This specifies the original large-right-half-plane branch;
P and its determinant have not been changed. Negative imaginary arms
use conjugation and negative heights follow from the original symmetries.

## 3. Exact contour decomposition and its central Gaussian part

Gaussian averaging of the prescribed source proves Note 30 FS11.
Indeed H(0, z-2iv)=xi(s+v)/8, and the real Gaussian average of
cos((z-2iv)u) is exp(tu^2)cos(zu). Fubini is justified by
integral exp(-v^2/t+2|v|u)dv/sqrt(pi t)<=2exp(tu^2)
and the complete source's superexponential tail. Thus

    H(t, z)=(pi t)^(-1/2) integral_R exp(-v^2/t)xi(s+v)/8 dv,
                                            s=(1+iz)/2.

Split at Re(s+v)=2 and -1, reflect the left arm using xi(q)=xi(1-q),
and retain the length-three middle interval. The two arms have exactly

    I_w=(pi t)^(-1/2) integral_(v0)^infinity
                  exp(-v^2/t) M(w+v)zeta(w+v) dv,
    v0=2-sigma in [-1,4].                              (EF7)

Move each arm to v=r+ih with its **oriented vertical connector** at
v0. Re(w+v)>=2 throughout, so no pole is crossed and the complete
Dirichlet series converges absolutely. At a finite right end close the
rectangle first. Its face tends to zero as the endpoint tends to infinity:
integrating EF3 along the horizontal ray bounds log|M| by an explicit
integral of 0.5 log(|w+v|/(2pi))+2/|w+v|, whereas the Gaussian has a
negative quadratic real exponent. This justifies the exact deformation.
No finite right cutoff or discarded face is an input to the estimate.
The uniform right-tail payment is given next.

On the central shifted ray put v=v_*+u. For all u>=-a/2, every point
between p and p+u has real part >2 and modulus >=x/2, even as u tends
to infinity. The Taylor integral remainders therefore satisfy

    Gamma_p(u)=log M(p+u)-log M(p)-alpha(p)u,
    |Gamma_p(u)|<=u^2/x,
    E_p(u)=Gamma_p(u)-alpha'(p)u^2/2,
    |E_p(u)|<=4|u|^3/(3x^2).                            (EF8)

Exact cancellation by the implicit saddle gives

    exp(-(v_*+u)^2/t)M(p+u)/[exp(-v_*^2/t)M(p)]
                                      =exp(-Bu^2/t+E_p(u)).

Both this exact expression and exp(-Bu^2/t) have modulus at most
exp(-u^2/(2t)), by EF3/EF6. Using the segment integral for the difference
of two exponentials avoids any exp(|E_p|) loss. Since
integral_R |u|^3 exp(-u^2/(2t))du=4t^2, the central **unit arithmetic
mode** comparison on [-a/2, a/2], relative to |S_t(w)|, costs at most

    12 t^(3/2)/x^2.                                    (EF9)

The full complex Gaussian integral equals B^(-1/2), with Re B>0.
For any of the missing Gaussian left end u<-a/2, Gaussian right end
u>a/2, and actual unit-mode right end u>a/2, its relative allowance is

    T_G=exp(-t lambda^2/200).                           (EF10)

Indeed the half-Gaussian tail is <=(2t/a)exp(-a^2/(8t)); after the
normalization and |B|^(1/2)<2 its prefactor is
4sqrt(t)/(a sqrt(pi))<1. EF6 supplies the exponent. Thus all three
ends may be paid separately by 3T_G. Alternatively the unit-mode
comparison over [-a/2, infinity) directly costs EF9+T_G. The three-end
version is used below so the actual infinite right tail is visible.
All non-unit arithmetic modes, including their infinite right tail,
are additional in Section 6.

## 4. Remaining left horizontal piece and connectors

Set A_r=Re p=a+sigma and T'=T+h. For 2<=v<=A_r, EF3 gives

    Re alpha(v+iT')-Re alpha(p)
              >=0.5 log(v/A_r)-2/v-2/|p|.

After integration over [A_r-d, A_r] this proves

    integral_(A_r-d)^A_r Re alpha(v+iT')dv
            >=d Re alpha(p)-D(A_r),
    D(A_r)=A_r/2+2log(A_r/2)+2<=2A_r.                   (EF11)

The logarithmic loss uses integral_0^A log(v/A)dv=-A; the two
remainder integrals are bounded by 2log(A/2) and 2A/|p|<=2.
There is no unspecified CA. Hence for v0<=r<=a/2,

    |exp(-(r+ih)^2/t)M(w+r+ih)/[exp(-v_*^2/t)M(p)]|
                               <=exp(-(a-r)^2/t+D(A_r)).

The full zeta factor has magnitude <2 on this ray. The entire left
piece is bounded, relative to |S_t(w)|, by

    E_left=2|B|^(1/2)(a/2+1)/(sqrt(pi t))
                             *exp(-a^2/(4t)+D(A_r)).    (EF12)

For connectors a convenient global fact is

    |Im alpha(2+iT)|<2,                     T real.    (EF13)

Indeed the rational terms contribute at most 1/4+1/2, while
[DLMF 5.7.8](https://dlmf.nist.gov/5.7.E8) and comparison with its
positive integral bound |Im psi(1+iy)|<=pi/2. This leaves less than
2 after the factor 1/2 in alpha. Moving the gamma factor from T+h
back toward T costs at most exp(2|h|). The Gaussian modulus never
increases compared with its top value. The actual connector, including
its full zeta factor and length, is therefore bounded by

    E_conn=2|B|^(1/2)|h|/sqrt(pi t)
                *exp(-(A_r-2)^2/t+D(A_r)+2|h|).         (EF14)

The formula also covers a collapsed connector; its allowance is zero
when h=0. Absolute values are taken only after the exact orientation
has been retained in EF7.

## 5. Explicit bounded-middle comparison

For every real T, the following elementary inequality suffices:

    sup_(-1<=b<=2)|xi(b+iT)/8|
                         <=225(1+|T|)|M(2+iT)|.        (EF15)

Here is a finite proof, so no compactness constant or vertical Stirling
constant is hidden. Reflection reduces to b in [1/2,2]. The N=1
[Euler formula](https://dlmf.nist.gov/25.2.E8) implies, for q=b+iT,

    |(q-1)zeta(q)|<=|q|(1+2|q-1|).

At q=1 this is understood by continuity. The
[beta integral](https://dlmf.nist.gov/5.12.E1) bounds
|Gamma(b/2+iT/2)/Gamma(1+iT/2)| by Gamma(b/2)<5; the endpoint b=2
follows by a limit or directly. The bound on Gamma on [1/4,1] follows
by splitting its defining integral at one. Combine pi^(1-b/2)<3,
|(2+iT)(1+iT)|>=1+T^2, and (2+|T|)^2/(1+T^2)<=5. This yields
75(3+2|T|), which is at most 225(1+|T|). It uses the canceled zeta
pole, not a finite bound on zeta at that pole.

The original middle has length three, |v|<=4 and a real Gaussian
factor <=1. Use EF11 at A_r-d=2 and EF13 to compare M(2+iT) with
its shifted endpoint. Its total relative allowance against **either**
arm's |S_t(w)| is

    E_mid=675|B|^(1/2)(1+T)/sqrt(pi t)
       *exp(16/t-(A_r-2)^2/t+D(A_r)+2|h|).              (EF16)

Thus the middle is not counted twice, and it is never dropped from the
complete field. The extra 16/t bounds v0^2/t when the endpoint Gaussian
is removed; the favorable -h^2/t is discarded only to enlarge the bound.

## 6. Every arithmetic mode and the finite decay checks

On Re q>=2, the complete series gives

    |zeta(q)-1|<=3*2^(-Re q),  |zeta(q)|<2.

The first inequality follows by comparing the sum from n=2 with its
integral; it includes every mode. On the central shifted ray the Gaussian
bound from EF8 therefore pays all non-unit modes by

    E_arith=3sqrt(2)|B|^(1/2)2^(-sigma-a)
                                      exp(t(log2)^2/2). (EF17)

The positive integral is extended to the whole real u line only after
its bound has been established on u>=-a/2. No Dirichlet-series argument
is extended to a point outside its convergence region. On the remaining
left and connector pieces full zeta was already included in EF12/EF14.

Every quantity in the ledger is now a finite elementary expression.
For clarity, the following conservative reductions prove one uniform
constant. For lambda>=1000, EF6 and EF11 imply

    -a^2/(4t)+D(A_r)
        <=-95lambda^2/100+(194/3)lambda+6
        <=-lambda^2/2.                                 (EF18)

For the connector/middle, A_r-2>=a-4>=a/2; their exponent without
2|h|+16/t obeys the same bound. Also

    2|B|^(1/2)(a/2+1)/sqrt(pi t)<=66lambda,
    2|B|^(1/2)|h|/sqrt(pi t)<=194,
    675|B|^(1/2)(1+T)/sqrt(pi t)<=1350x,
    2|h|<=97<194, 16/t<1.

Consequently

    T_G <= x^-3,
    E_left <=66lambda exp(-lambda^2/2)<=x^-3,
    E_conn <=194 exp(-lambda^2/2+194)<=x^-3,
    E_mid <=1350x exp(-lambda^2/2+195)<=x^-3,
    E_arith <=48 exp(97/2-95lambda/10)<=x^-3.            (EF19)

These comparisons require no evaluation at enormous x. For example
66lambda<=exp(lambda/2) follows from the cubic exponential term,
log194<6 and log1350<8 follow from e>8/3, and the remaining quadratic
inequalities are increasing past lambda=1000 with strictly positive
rational margins there. For arithmetic use 1/2<log2<1; for the Gaussian
use 95lambda/200>3. All weakenings enlarge the costs.

For each arm EF9 plus three EF10 ends and EF12/EF14/EF17 is therefore
at most (12t^(3/2)/x^2+6/x^3)|S_t(w)|. Add both arms and the one
middle. Since t^(3/2)<970, the complete error divided by A is at most

    11640/x^2+7/x^3 <12000/x^2.                         (EF20)

This proves EF1. The tiny terms remain in EF9–EF17 as finite
allowances; EF20 explicitly absorbs them, rather than setting them to
zero. It pays the middle, both connectors, actual infinite ends and
all arithmetic modes of the canonical H.

## 7. Full-circle Cauchy transfer and finite FI23 consumption

From EF3 and the exact determinant derivative,

    D=(log S_t)_w=alpha+t alpha''/(4B^2),
    |D|<=0.5log x+1+4/x+776/x^2<=log x.                 (EF21)

Fix t, |Im z|<=9/2 and x>=2^2049. Set rho=1/(4L). Its complete
circle and disk lie in the strip |Im zeta|<=5 and have
|Re zeta|>=x-1>=2^2048. The branch and H-P are holomorphic on an
open neighborhood of that disk. Each arm's z logarithmic derivative
is bounded by L there, so along each radial segment

    A(t, zeta)<=exp(rho L)A(t, z)<2A(t, z).

The derivative version of [Cauchy's formula](https://dlmf.nist.gov/1.9.E31)
now gives, for j<=3,

    |partial_z^j(H-P)|/A(t, z)
       <=2*12000 j!(4L)^j/(x-1)^2
       <=8*12000 j!4^j L^j/x^2.                        (EF22)

This proves the table in EF2, retaining EF1's sharper C0. Neither the
field error nor an asymptotic remainder was differentiated. A fixed
unit-radius circle would not give this carrier control; the actual
radius is rho=O(1/L) and the extra strip provides its full analytic buffer.

For one Note 44 gap chart let X>=2^2050, sigma<=1/2, L_X=log(2+X).
Take the full gap analytic neighborhood inside

    ||Re z|-X|<=2, |Im z|<=9/2.

It contains the declared vertical band and an additional open buffer.
Every point has local height >=X/2>=2^2049 and
log(2+|Re z|)<=2L_X. Thus the FI23 debit is now explicitly paid by

    mu_o <=32*C3/X^2=1179648000/X^2 <=1/16.              (EF23)

The last inequality is immediate, for example, from
16*32*C3<2^4100 and X^2>=2^4100. With mu_s<=1/16 the initial
c0=1/2 gap-floor requirement mu_o+mu_s<=1/4 has strict margin.
For any smaller specified target mu_o^*, it suffices instead to require
X>=2^2050 and X^2>=1179648000/mu_o^*.

This is a uniform theorem for every such **model** gap chart; no particular
phase index or source was evaluated. FI1–FI8's model geometry/velocity,
collar separation and later full observable allocations remain their own
requirements. The bounds hold on all t in [95,97], so shortening to the
fixed I required by the root-motion gate does not spend a new time error.
Note 43's actual partition, nonholomorphic, component heat, curvature,
forcing and actual covariance rows are retained in full. Field accuracy
is obtained from the complete convolution, not propagated from E_P.

## 8. Evidence, control screen and disposition

The primary inputs above were checked in official DLMF HTML on
25 October 2026; the [reference record](../references/README.md) and
manifest specify the equations, hypotheses and use. These are imported
classical formulas plus new conservative estimates derived here, with
no novelty or external theorem-extension claim.

At most six selected exact-rational scalar checks are recorded in the
[small audit](../numerics/EFFECTIVE_OUTER_SCALAR_BOUNDS_20261025.json) and
its [script](../numerics/effective_outer_scalar_bounds.py). They check
constant arithmetic only. There was no theta/source/gamma sampling,
mesh/precision search, numerical field comparison or interval theorem
certificate. [Review 26](../reviews/26_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_ASSESSMENT_20261025.md)
records same-model proof checks and their shared premises.

The generic source/heat identities still permit collision controls.
Canonical arithmetic/completion fixes the H in EF7 and the all-mode
payment; changed-source Euler-factor, weighted-square, reflected,
smooth-positive-primitive, atomic and polynomial controls lack those
exact inputs. They are not excluded by a generic approximation or an
unrelated zero-free gap. This result does not prove RH or simplicity.

**Disposition:** AN03 r1 closes at its requested analytical scope:
explicit complete field/jet constants and onsets, with no unpaid contour
component. The former FI23 uninstantiated comparison input is paid in
this very large finite-height regime. HDA-17 remains Partial, HDA-18
Gated and HDA-20 unfulfilled; no manuscript or draft-history milestone.

**Next: Analysis — Sol**, make the root-collar/unit and signed-pole/
weighted-exterior constants in FT7/FT9/FT15 explicit for this same regime,
then test one complete Note 43 budget before any numerical source/gap
execution. This is the next finite consumer; optimizing the enormous
onset is optional and is not evidence of an accepted global join.
