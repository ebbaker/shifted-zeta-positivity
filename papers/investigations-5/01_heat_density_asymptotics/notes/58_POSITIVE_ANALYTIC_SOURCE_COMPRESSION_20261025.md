# Positive analytic-source compression with a complete construction ledger

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's recorded metadata. Chat **0021**, thread
`01a1751b-9ac5-7192-9f6c-b9f59ec30827`.

**Status: positive compressed-source, four-jet and source-construction cost
bounds proved in-note; same-model internal analytical checks only.** This
returns [HDA-17-AN05 r1](../research-progress/handoffs/HDA-17-AN05.md).
There is no unpaid complex-branch, positive-approximation, coefficient or
source-construction estimate in the construction below. Field evaluation
and continuous filtering remain separate unpaid tasks. No source
coefficients, theta values or research calculations were executed.

The unchanged [Note55](55_FIXED_CENTRAL_CONDITIONING_AND_SOURCE_COST_20261025.md)
IC14/IC23 demand is the consumer. For an already fixed upper time b, put
q_s=log(1/epsilon). The new sufficient bounds are

    polynomial degree n = O_b(q_s log q_s),
    dyadic coefficient fractional bits beta = O_b(q_s),
    compressed source descriptor = O_b(q_s^2 log q_s) bits,
    expanded normalized-power descriptor = O_b(q_s^2 log^2 q_s) bits.
                                                               (AC1)

A finite, deliberately coarse polynomial source-construction bit bound
is given in AC18. With Note55's specified fixed-b accuracy policy,
q_s=pi R/8+O_b,eta,theta(log^2 R), so the compressed descriptor is
O_b,eta,theta(R^2 log R) bits, replacing that note's specified sufficient
exponential descriptor bound. This is a construction upper bound, not a
lower complexity bound, a useful finite crossover, or an evaluator bound.
Huge fixed constants remain. HDA-17 **Partial**, HDA-18 **Gated**, HDA-20
**unfulfilled** are unchanged.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision screen12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification01](../../../../avoid/01_restating_the_target.md),
[control premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[shared review05](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerical scope10](../../../../avoid/10_numerics_ahead_of_the_question.md),
[signed cancellation12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status maintenance19](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is quantitative approximation and construction analysis, not an RH
criterion or collision exclusion. [Manifest58](58_POSITIVE_ANALYTIC_SOURCE_INPUTS_20261025.json)
pins the opening inputs; [Review37](../reviews/37_POSITIVE_ANALYTIC_SOURCE_COMPRESSION_ASSESSMENT_20261025.md)
records the internal assessment. Earlier mathematical sources are preserved.

## 1. Contract, target and order of choices

First fix J=[95,97], b=97. Retain the canonical normalization

    H(t,z)=integral_0^infinity exp(tu^2) Phi(u) cos(zu) du,
    Phi(u)=sum_(r>=1)[2pi^2 r^4 exp(9u)-3pi r^2 exp(5u)]
                                  exp[-pi r^2 exp(4u)].        (AC2)

The source will be f(u)=p(u)^2 on [0,U], and zero above U, where p
has real dyadic coefficients in a specified normalized Chebyshev basis.
Its exact field is G=integral_0^U exp(tu^2) f(u) cos(zu) du. We prove

    |partial_z^j(G-H)| <= 51epsilon/256 < 29epsilon/64,
    j=0,1,2,3, all real x, |Im z|<=4, every real t<=b. (AC3)

Choose epsilon<=1 from the exact IC14 demand for the initial slab, or
from **every clause** of IC23 for Note54's global consumer. The source
is chosen once for that demand. It is independent of the subsequently
queried t,x,y. A dyadic epsilon0<=epsilon, within a factor two when
asymptotics are claimed, may be used; replacing epsilon by epsilon0 in
all formulas changes q_s by O(1).

The physical q=epsilon_g^2, fixed K=k_1 k_1, unnormalized observables,
possible multiple central events, actual covariance and every spatial,
moving and temporal defect remain those of Notes54--55. The new G is
real-type and exactly satisfies G_t=-G_zz. The full transfer uses these
properties and the four errors, not the cubic shape of its predecessor.
In particular G alone is not asserted to be a relative all-height
approximation at positive time. It replaces only the source component
of the already paid joined field and domain table.

For general upper time let s=max(0,b), or a specified finite rational
upper bound for it. Constants called fixed-b below may depend on that
choice. Note54 first selects its finite T_+, then b=T_++1, and only then
the gap and source; that order is unchanged.

## 2. An explicit branch for the complete canonical square root

Let E(w)=exp(4w) and

    D={w: Re w> -1/16, |Im w|<1/16},
    A(w)=pi exp(5w)[2pi E(w)-3] exp[-pi E(w)],
    R(w)=sum_(r>=2) r^2[2pi r^2 E(w)-3]/[2pi E(w)-3]
                                      exp[-pi(r^2-1)E(w)].     (AC4)

Then Phi=A(1+R), with **all** canonical arithmetic modes included.
On D, e^(-1/4)>3/4 and cos(1/4)>=31/32 give

    |E|>3/4, Re E>93/128>2/3,
    |2pi E-3|>2|E|, Re(2pi E-3)>87/64>0.

Here use 3<pi<4, reverse triangle inequality, and 3<4|E|. Consequently
each relative summand in AC4 has modulus at most

    t_r=6r^4 exp[-2(r^2-1)].

For r>=2, t_2=96e^-6 and
t_(r+1)/t_r <= (3/2)^4 e^-10 <1/4. Therefore the complete normally
convergent series obeys

    |R(w)| <=128e^-6 <1/2.                             (AC5)

The last strict inequality follows from e>8/3 and (8/3)^6>256; no
evaluated source or numerical constant is needed. The Weierstrass
majorant also proves holomorphy. The two factors 2pi E-3 and 1+R lie
in the open right half-plane. Thus the following is an explicit branch:

    h(w)=exp{[log pi+5w+Log(2pi E(w)-3)-pi E(w)
                                         +Log(1+R(w))]/2}.    (AC6)

The displayed Log factors use their principal branches. Then h^2=Phi
on D, and h(u)>0 on the entire real half-line. Real positivity was not
used as a substitute for this complex branch proof.

The norm is also uniform in the source cutoff. Put y=exp(4 Re w)>0.
Then

    |A(w)| <= [32y^(9/4)+12y^(5/4)] exp[-(93/32)y] <=44.

For alpha=9/4 or 5/4, the maximum of y^alpha exp[-(93/32)y] is
[alpha/((93/32)e)]^alpha<1. It follows from AC5 that

    |Phi(w)|<66, |h(w)|<9, w in D,
    |h'(u)|<=288<512, real u>=0.                       (AC7)

The derivative uses the Cauchy circle of radius 1/32, fully inside D.
There is a strict left buffer at u=0 as well as a vertical buffer.

## 3. Cutoff, ellipse and a constructive interpolation degree

Use Note55 IC16's shorter complete-tail cutoff and integral cap:

    Q_s=log(32/epsilon),
    U=ceil[4+log(2+s+Q_s)],
    F=U^4 exp(sU^2+4U), delta=epsilon/(160F),
    rho=1+1/(8U).                                      (AC8)

All transcendental ceilings use the predecessors' certified integer
upper-bound convention, allowing bounded extra integer slack. Whenever
U is enlarged, recompute F and the subsequent parameters. In particular
the constructor needs no real-number equality test at a ceiling.
For j<=3, the weighted integral over [0,U] is <=F. IC16/FB7, with
exactly s and Y=4, gives

    integral_U^infinity u^j exp(su^2+4u) Phi(u) du
                                                  <=epsilon/8. (AC9)

To recall its paid scale: U>=4, s,Q_s<=exp(U-4),
lambda_j=4pi exp(4U)-2sU-13-j/U>=pi exp(4U), and
sU^2+13U-pi exp(4U)<=-2exp(4U)<=-Q_s. The complete FB7
prefactor is <=1. This is the entire source tail, not a nodal-mode tail.

Under w=U(1+v)/2, the Bernstein ellipse of parameter rho has

    max |Im w|=U(rho-rho^-1)/4 <1/16,
    endpoint extension=U(rho+rho^-1-2)/4 <1/(256U).

Its closure lies inside D. For g(v)=h(U(1+v)/2), the Laurent expansion
of g((zeta+zeta^-1)/2) on |zeta|=rho yields Chebyshev coefficients
|a_k|<=18rho^-k. The Chebyshev tail beyond degree n is therefore
<=18rho^-n/(rho-1).

Let I_n g be the degree-n interpolant at m=n+1 roots of T_m.
At those nodes, every T_k aliases to plus or minus a T_r, r<m, or to
zero, so ||I_n T_k||<=1 on [-1,1]. Applying this to the absolutely
convergent tail, and using that I_n fixes degrees through n, proves

    ||g-I_n g|| <=36rho^-n/(rho-1)=288U rho^-n.

Since log rho>=1/(8U+1) and 16U>=8U+1, the finite degree

    n=ceil[16U log(1152U/delta)], m=n+1                 (AC10)

pays interpolation error <=delta/4. This proof establishes the rate
for the full canonical source, rather than assuming its analytic input.
The identity T_k(cos theta)=cos(k theta) and the Laurent substitution
are also recorded in [DLMF18.5.1](https://dlmf.nist.gov/18.5.E1).
The approximation and aliasing estimates just used are proved here.

## 4. Construct every coefficient without a nodal oracle

Set

    eta_n=delta/(16m), zeta_n=delta/(160m),
    beta=ceil log2(8m/delta),
    alpha=min(eta_n/(4096U),zeta_n/m^2,1/4),
    B_c=ceil log2(8/alpha), D_cos=B_c+46.               (AC11)

The subscript on eta_n distinguishes this construction accuracy from
the unchanged physical regulator parameter eta. The ideal nodes are
theta_l=(2l+1)pi/(2m), c_l=cos theta_l, u_l=U(1+c_l)/2, 0<=l<m.
Compute pi to absolute error 2^(-B_c-10) by the finite Machin series,
then cosine of its rational theta_l by Taylor degree D_cos. Its
argument has modulus <=4; the ordinary factorial remainder gives
error <=2^(-B_c-10). Round the result to the B_c-bit dyadic grid and
project onto [-1,1]. The resulting c_hat,l has error <=alpha. Define
u_hat,l=U(1+c_hat,l)/2 exactly, so it lies in [0,U]. By AC7,

    |h(u_hat,l)-h(u_l)|<=512U alpha/2<=eta_n/16.

Compute every DCT weight as the exact rational T_r(c_hat,l), by its
three-term recurrence. The elementary bound |T_r'|<=r^2 on [-1,1]
follows from sin(r theta)/sin theta having modulus <=r. It gives
weight error <=r^2 alpha<=zeta_n; each computed weight has modulus
<=1. Thus approximate cosine nodes do not introduce an unpaid DCT
or polynomial-conversion error.

To obtain the source value and square root at u_hat,l, use

    n0=max(3,ceil sqrt[log(2^18/eta_n^2)/2]), N=n0-1,
    B_phi=ceil log2(4096/eta_n^2),
    P=B_phi+20+ceil[9log2(N+1)+26U/log 2],
    T=ceil[10N^2 exp(4U)+13U+1], D_exp=ceil[P+8T+4],
    B_h=ceil log2(128/eta_n).                           (AC12)

Note44 FI19's complete omitted-value envelope is
64n0^6 exp(-3n0^2)<=64exp(-2n0^2)<=eta_n^2/4096.
Here n0^6<=exp(n0^2) for n0>=3. The same note's explicit
Machin/Taylor value algorithm with parameters B_phi,P,T,D_exp computes
Phi_N(u_hat,l) to absolute error <=2^(-B_phi)<=eta_n^2/4096.
In that algorithm pi and positive exponentials are approximated first;
the exact rational argument pi_hat r^2 exp_hat(4u) is then inserted
into the negative exponential. Its argument derivative has modulus
<=1. The paid finite-product error is
2^16 N^9 exp(26U)2^-P, followed by the prescribed B_phi-bit rounding.
The Taylor degree D_exp pays the largest argument T by the factorial
remainder. These are finite algorithm instructions, not executed data.

Project the computed source value v_l onto [0,infinity), and find its
square root by B_h exact dyadic bisections on [0,16]. The source value
is <82, so this interval suffices. Projection cannot enlarge the error
from the nonnegative Phi(u_hat,l). Use the absolute inequality

    |sqrt(a)-sqrt(b)|<=sqrt(|a-b|), a,b>=0.

The combined mode and source-arithmetic error in the square root is
<=eta_n/sqrt(2048); the bisection error is <=eta_n/8. Together with
the node displacement these bounds give dyadic data

    |h_hat,l-h(u_l)|<=eta_n, 0<=h_hat,l<=10.            (AC13)

In particular no inverse lower bound for Phi near U is introduced.
An eta_n-accurate square root is paid with eta_n^2 source accuracy;
ignoring this square would have left an arithmetic debit unpaid.

Form the DCT coefficients by exact rational arithmetic:

    a_hat,0=m^-1 sum_l h_hat,l,
    a_hat,r=(2/m)sum_l h_hat,l T_r(c_hat,l), 1<=r<m.

Round each once to the dyadic grid 2^-beta, giving a_bar,r. Define

    p(u)=sum_(r=0..n) a_bar,r T_r(2u/U-1),
    f(u)=p(u)^2 on [0,U], f(u)=0 for u>U.              (AC14)

These are real coefficients; positivity is exact after storage and
does not require a clipping or root-isolation algorithm.

## 5. Separate approximation debits and the four-jet bound

The exact root-node DCT gives the coefficients of I_n g. Because
|T_r|<=1, data perturbations contribute <=2m eta_n=delta/8 to
the polynomial norm. Since h_hat,l<=10, the weight perturbations
contribute <=20m zeta_n=delta/8. Rounding contributes
<=m2^-beta<=delta/8. Together with AC10,

    ||p-h||_[0,U] <=5delta/8 <delta,
    |p^2-Phi| <=(18+delta)|p-h| <=19|p-h|.             (AC15)

The separate field-error ledger for each j<=3 is therefore:

| Category | Absolute jet allowance |
| --- | ---: |
| Full analytic interpolation | 19epsilon/640 |
| Nodal h data, including the separate AC12--AC13 mode/source/sqrt/node payments | 19epsilon/1280 |
| DCT weights from dyadic nodes | 19epsilon/1280 |
| Stored dyadic coefficients | 19epsilon/1280 |
| Complete source tail | epsilon/8 |
| Exact basis conversion and squaring | 0 |
| Positivity enforcement beyond the preceding errors | 0 |
| Total before field evaluation and continuous filtering | 51epsilon/256 |

The nodal row is not an omitted category: its four constituent errors
are explicitly bounded in AC12--AC13 before the DCT is taken. Squaring
is charged using the final error, so cross terms are included in the
factor 19. For every real t<=b, z=x+iy, |y|<=4,

    |partial_z^j cos(zu)|<=u^j exp(4u),
    integral_0^U u^j exp(tu^2+4u)du<=F.

Integrating AC15 and adding AC9 proves AC3 simultaneously for all
real x. It requires no horizontal mesh or bound on x. Multiplication
by u^2 supplies time differentiation; thus G is entire in t,z and
G_t=-G_zz exactly. A jump of the source at U introduces no field heat
defect because the integration interval and source are fixed in t.

The bound is stronger than the predecessor's 29epsilon/64 constructor
margin, so the same IC14/IC23 reserve and every four-jet consumer remain
valid without changing an observable target. Remaining reserves are not
silently spent on field arithmetic or filter quadrature.

## 6. Descriptor, conversion and complete source-construction costs

The DCT and rounding give |a_bar,r|<=21. Store U,m,beta and the m
signed integer numerators 2^beta a_bar,r. A conservative explicit
descriptor bound, with a fixed header/encoding convention, is

    S_Cheb <=64m[beta+ceil log2(U+m+2)+1] bits.         (AC16)

The formula defining f uses one polynomial and one interval, with
O(m) recurrence nodes. There are no algebraic clipping endpoints.
For an expanded polynomial use v=u/U, and Q_r(v)=T_r(2v-1).
Q_0=1, Q_1=2v-1, Q_(r+1)=2(2v-1)Q_r-Q_(r-1) prove
||Q_r||_(coefficient l1)<=7^r. Therefore the coefficients of the
expanded p have modulus <4*7^m. After squaring, each coefficient has
common denominator 2^(2beta) and a numerator of at most

    L_d=2beta+6m+ceil log2(m+1)+10 bits.               (AC17)

Consequently a specified expanded normalized-power descriptor has
<=64(2m+1)[L_d+ceil log2(U+m+2)+1] bits. Conversion and squaring
use O(m^2) exact integer arithmetic and zero approximation loss.
If literal powers of u rather than u/U are stored, also pay up to
2n log2 U denominator bits per coefficient. The normalized convention
avoids that unnecessary storage. No exponential basis-conversion loss
has been omitted: it is the explicit 6m term in L_d.

A complete conservative source-construction cost can also be given.
Let the certified integer recipe parameters above be supplied, and put

    K_int=2+U+m+N+beta+B_phi+B_c+B_h+P+D_exp+D_cos,
    L_int=2^20 K_int^4,
    arithmetic operations <=2^20 K_int^4,
    schoolbook bit operations <=2^100 K_int^12.        (AC18)

Here arithmetic operations are exact integer/rational additions,
multiplications, comparisons, divisions with remainder and bisections.
The bound includes Machin constants, trigonometric nodes, every finite
source mode, nodal square roots, DCT weights and sums, coefficient
rounding, conversion and squaring; it includes no field evaluations.

For clarity, an explicit implementation establishing the operand bound
is as follows. At a rational argument a=p/q, form a Taylor sum with
common denominator q^D D!, rather than accumulating unrelated
denominators. Form factorials, powers and terms exactly, then round
each elementary output to its specified dyadic grid before products
in the source formula. Machin's rational partial sums have denominator
bit length O(P^2+P log P), and are likewise rounded to dyadics first.
More explicitly, K_int>16. Each rational Taylor argument numerator
and denominator uses <=32K_int bits: its dyadic precision, input-node
denominator, positive-exponential magnitude and mode integer are all
included in K_int. With Taylor degree d<=K_int, the common denominator
q^d d! has <=32K_int*d+d log2(d)+1 bits. Each scaled numerator and
partial sum has <=64K_int^2 bits, including signs and the d+1 terms.
Machin staging has <=128K_int^2 bits, even if all its O(P) rational
denominators are multiplied before its final dyadic rounding. Exact
DCT weights have denominators 2^(r B_c), and coefficient sums can use
the common denominator m*2^(r B_c+B_h); their operands use
<=128K_int^2 bits. The source products/sums after prescribed elementary
rounding and the AC17 conversion/squaring lengths fit the same bound.
Known common denominators can be used without any unbounded rational
reduction routine. In particular all operands fit L_int with the
displayed generous constant; no unspecified O constant is used to
justify that finite L_int.

There are m source evaluations, each with N modes and finite Taylor
degree D_exp; m trigonometric node evaluations; O(m^2) exact DCT and
conversion operations; and O(m B_h) bisections. Even computing every
power naively, a sufficient arithmetic count is

    2^16 {m(N+1)(D_exp+P+1)^2
             +m(D_cos+B_c+1)^2 +m^2+m B_h+1}
                                               <=2^20 K_int^4.

Schoolbook arithmetic
on L_int-bit operands costs at most a constant times L_int^2 per
operation, absorbed by 2^100 K_int^12. Division is included. These
elementary counting and denominator bounds prove AC18 without an
unprovided special-function or square-root oracle.

AC18 is a source-construction bound **from certified recipe parameters**.
It does not include determining or numerically certifying the upstream
all-time contour/transfer constants in IC23. Given a dyadic input
epsilon0 and rational s, all elementary recipe bounds can themselves
be selected by rational interval series and bounded-slack upper integers;
alternatively the certified integers are the constructor input. No real
oracle for an arbitrary exact b or epsilon is being assumed. Earlier
notes' upstream analytical parameter selection is not relabeled as a
cheap evaluated operation.

At fixed s, as q_s->infinity, the finite formulas give

    U=O(log q_s), log F=O_s(log^2 q_s),
    m=O_s(q_s log q_s),
    beta,B_phi,B_c,B_h,P,D_cos=O_s(q_s),
    N=O_s(sqrt q_s), T,D_exp,K_int=O_s(q_s^5).         (AC19)

Thus AC16 gives O_s(q_s^2 log q_s) bits, AC17's expanded descriptor
O_s(q_s^2 log^2 q_s) bits, and AC18 gives the intentionally coarse
O_s(q_s^60) complete source-construction bit upper bound. These are
upper bounds for specified algorithms, not optimality or runtime data.

For varying s or tolerance, use **AC8--AC12 and AC16--AC18**, not
fixed-s big-O notation. In particular U<=5+log(2+s+Q_s) under exact
ceilings, exp(4U)<=e^20(2+s+Q_s)^4, and log F=sU^2+4U+4log U.
The degree explicitly pays sU^2. Bounded extra ceiling slack changes
only the stated finite constant. No result polynomial in the encoding
length log b, or uniform polynomial cost in a simultaneous global
accuracy/upper-time limit, follows from AC19.

## 7. One finite exact-heat Gaussian-moment field

After exact conversion write f(u)=sum_(k=0..2n) d_k(u/U)^k on [0,U].
Define

    M_k(a,c)=integral_0^1 v^k exp(av^2+cv)dv,
    a=tU^2, c_+=izU, c_-=-izU,
    G(t,z)=U/2 sum_k d_k[M_k(a,c_+)+M_k(a,c_-) ].     (AC20)

For jet j, multiply the two moments by (iU)^j and (-iU)^j and replace
k by k+j. The highest needed moment is 2n+3. For a!=0 put
A=sqrt(-a), E=exp(a+c), and use

    M_0=sqrt(pi)/(2A) exp[-c^2/(4a)]
            *[erf(A-c/(2A))-erf(-c/(2A))],
    M_1=(E-1-c M_0)/(2a),
    M_(k+1)=(E-k M_(k-1)-c M_k)/(2a), k>=1.          (AC21)

Changing the square-root branch changes neither M_0 nor the field.
At a=0,c!=0 use M_0=(exp c-1)/c and
M_k=(exp c-k M_(k-1))/c. At a=c=0 use M_k=1/(k+1).
These explicit branches cover t=0 and z=0; removable denominators
have not been left outside the prescription. The integral definition
shows that the combined field is entire even across those branches.
Shared moment recurrences give O(m) arithmetic/special-function formula
nodes after the O(m^2) exact source conversion, with a bounded number
of erf/exponential base calls. Formula-node count does not count the
precision or cost of accurately evaluating those nodes.

In particular near-zero divisions, large opposite moment terms,
high-degree cancellations, erf/exp working accuracy, observable
arithmetic and the continuous K integral need an evaluator theorem.
They have not been paid by source-data bits or by AC18.

## 8. Same consumer, quantitative comparison and disposition

At equal epsilon and upper time, Note55's specified clipped-cubic
descriptor has logarithm q_s/4+(s/4)log^2 q_s+O_s(log q_s).
AC16 is polynomial in q_s. It therefore improves that sufficient
description asymptotically without changing the absolute target.
For Note55 IC23's fixed-b policy substitute

    q_s=pi R/8+O_b,eta,theta(log^2 R),
    n=O_b,eta,theta(R log R),
    S_Cheb=O_b,eta,theta(R^2 log R),
    S_expanded=O_b,eta,theta(R^2 log^2 R).             (AC22)

This compares two explicit construction bounds, not a lower bound
against an upper bound. A high-degree moment evaluator may still be
poorly conditioned; AC22 proves no useful finite crossover. One need
not execute the construction to establish its description/construction
bound, and no such execution occurred here.

IC23's gap and late relative-field clauses, negative and middle-time
clauses and bridge requirement are all retained. AC3 satisfies the
same common minimum with extra margin. The new source changes none
of Note54's field/domain table, time endpoints, gamma exterior,
switches, source traces, actual covariance, signed weak cancellation,
compatibility corrections or heat/nonholomorphic defects. The fixed
central comparison still permits multiple events. The old finite-cutoff
obstruction to a standalone all-height relative approximation remains
valid for its stated class; no contrary conclusion is drawn from an
absolute field approximation.

The collision screen is a premise check, with no new runs. Euler-factor
controls alter the canonical completion. Weighted-square and finite-prime
controls do not retain the unchanged full coefficients/reflection input;
reflected, smooth-shape and positive-primitive controls do not have AC2's
full canonical square expansion and its proved leading-mode remainder.
Atoms and heat-polynomial controls lack this smooth complete source.
Generic approximation estimates can still hold for controls with their
own analytic inputs. Neither their failure of an application premise
nor source positivity is a theorem excluding a collision.

**HDA-17-AN05 r1 CLOSED at bounded analytical source-compression and
source-construction scope.** The first unpaid task beyond that scope is
the evaluator working-precision/error theorem for AC20--AC21, followed
by actual observable arithmetic and continuous-filter integration on
the inherited IC23 consumer. No source/theta/gamma/field sampling,
numerical, exact-rational or machine-symbolic research execution,
mesh/precision search, interval campaign, evaluated coefficient source,
manuscript change, DRAFT_HISTORY milestone, snapshot, commit, new
user-owned chat or model change occurred. Hashes, sizes, links, file
installation and chat capture are housekeeping, not proof certificates.

**Next: Analysis — Sol.** Specify and prove an evaluator working-bit and
continuous-filter error ledger for this source representation and the
unchanged complete tuple, before preparing a separately bounded
numerical diagnostic. A named conditioning problem would justify a
different evaluation representation; source compression alone does not
settle that decision. HDA-20 remains a distinct full-chain audit with
reviewer assignment held by Edward Baker.
