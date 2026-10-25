# Finite input costs: a positive clipped source and the unpaid outer gate

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from turn metadata. Chat **0015**, thread
`01a1711d-376c-7de3-929c-60ec4065bddc`.

**Status: finite model/regulator reductions and constructive finite-source
size bound proved in-note; no particular finite gap accepted.** This is
the author-authorized next analysis after
[Note 43](43_FULL_SUPPORT_FIXED_GAP_TRANSFER_20261024.md), returned under
[HDA-18-AN02 r1](../research-progress/handoffs/HDA-18-AN02.md).
Its gains are an explicit positive fourth-order source construction,
source-description cost, and finite model/cutoff/regulator coefficients.
Its stop is a precise uninstantiated theta-to-saddle estimate, rather than
a demonstrated false inequality. The earlier fixed-gap comparison and
all its partition, nonholomorphic, heat, curvature and actual-covariance
terms are retained.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[status](../../../../avoid/06_status_stronger_than_the_evidence.md),
[unpaid cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared review](../../../../avoid/05_same_model_reviews_and_shared_premises.md).
This is quantitative approximation analysis, not an RH criterion or a
source-cost lower bound. The [input manifest](44_FINITE_INPUTS_MANIFEST_20261024.json)
identifies the exact starting versions.

## 1. One finite template, with the physical definitions preserved

Take t0=96, J=[95,97], ell=h=Y=1, hence Y_b=4. The physical eta>0,
H, q, source normalization and averaging kernel are unchanged. These
are chosen finite parameters within the previous theorem, not a claim
that 96 or any selected height is a certified outer onset.

A candidate center is an exact solution Theta_*(96,X)=n pi on a
certified branch of the explicit model P. No particular integer n is
accepted in this note. All model caps below are over a full complex
chart containing the two reflected gap neighborhoods, collar buffers,
and a positive analytic enlargement; they are independently computable
from gamma/polygamma and the implicit saddle. A certificate would have
to supply their finite values and branch uniqueness. This note reduces
that obligation to finite formulas, without executing gamma evaluation.

Put L=log(2+X). Choose sigma>0 and tau>0 from Section 2 and the GS2
restriction; I=[96-tau,96+tau] stays in J. The spatial band is fixed.
Write R_c=X+2sigma+3 for the full source rectangle's horizontal radius,
with any further necessary analytic enlargement included by increasing
R_c. All source bounds below hold on |y|<=4 and every real x, so such
an enlargement does not add a source-jet error factor.

## 2. Explicit model-only gap, jet, time and residual coefficients

Use alpha=M'/M and p,B,S_t exactly as in Note 30 FS3. Suppose a validated
finite branch chart, chosen for all t in J before sigma and tau are
selected, supplies b=inf|B|>0 and

    a_j=sup |alpha^(j)(p)|,                 j=0,...,4.    (FI1)

There is no assertion that these finite numbers have been evaluated.
Differentiating the implicit equation gives p_w=1/B and p_t=alpha/(2B).
For D=(log S_t)_w, bounds on D,D_w,D_ww are

    D0=a0+97a2/(4b^2),
    D1=a1/b+97a3/(4b^3)+97^2 a2^2/(4b^4),
    D2=a2/b^2+97a1 a2/(2b^3)+97a4/(4b^4)
                   +7*97^2 a2 a3/(8b^5)+97^3 a2^3/(2b^6). (FI2)

Thus the GS1 bounds |partial_z^j P|<=C_j L^j A are paid by

    C0=1, C1=D0/(2L), C2=(D0^2+D1)/(4L^2),
    C3=(D0^3+3D0D1+D2)/(8L^3).                          (FI3)

Each arm has z derivative ±i/2 times its w derivative. A is the **sum
of carrier moduli**, so these bounds survive cancellation between arms.

At fixed w the exact time logarithmic derivative is

    T=(log S_t)_t=alpha^2/4+alpha'/(4B)
                                        +t alpha alpha''/(8B^2),
    T0=a0^2/4+a1/(4b)+97a0a2/(8b^2).                    (FI4)

For compatible arm logarithms set Theta=(log S_+ -log S_-)/(2i).
On real x, Theta is real, Theta_x=(D_++D_-)/4, and
|Theta_zz|<=D1/4. The linear imaginary displacement has zero real part.
Taylor's integral formula therefore gives, on the full vertical band,

    |Re Theta(t,x+iy)-n pi|<=sigma D0+tau T0+2D1,
                 |x-X|<=2sigma, |y|<=4.                 (FI5)

One finite model-only choice is

    sigma=min(1/2, pi/[16(D0+1)]),
    tau<=min(1, pi/[16(T0+1)]), D1<=pi/32.               (FI6)

Then the phase deviation is <=3pi/16<pi/4. Writing
P=2exp((log S_++log S_-)/2)cos Theta gives exactly

    |P|/A=|cos Theta|/cosh(Im Theta)>=|cos(Re Theta)|.

Consequently c0=1/2 is a conservative field-floor constant. To include
GS2 also require tau<=c_gap/[(V+1)L] using the actual finite collar
margin. On the real root charts

    Omega_min=(1/2)inf Re D>0,
    V=T0/Omega_min                                      (FI7)

bounds the actual model root speed, by c'=-Theta_t/Theta_x. The model
heat residual is not omitted from that velocity. Supply injectivity
and enlarged-collar separation on the chosen full chart; the phase floor
by itself is not a numerical certificate of all collar inputs in FT7.
For fixed J, FI6 has the sigma=O(1/L) scale. At a particular chart it
can be written sigma=c/L with c=sigma L, as required by the fixed-gap
contract; c and the actual derivative caps are recorded, not assumed
uniform without the branch estimates.

Finally PE8's exact nonzero residual gives the finite caps

    R0=97a3/(16b^3)+5*97^2 a2^2/(64b^4),
    R1=97a4/(16b^4)+97^2 a2a3/(4b^5)
                                      +5*97^3 a2^3/(32b^6),
    |E_P|<=R0 A, |(E_P)_z|<=(D0 R0+R1)A/2.             (FI8)

These replace an unspecified residual constant on the model side once
FI1 is supplied. They do not establish |H-P| or propagation accuracy.

## 3. An explicit flat cutoff and the heat test partition

Let phi(s)=exp(-1/[s(1-s)]) for 0<s<1 and zero otherwise. Put
N_phi=integral phi and b_*(s)=N_phi^-1 integral_(-infinity)^s phi.
The function b_* is C-infinity and flat at 0,1. On [1/4,3/4],
phi>=exp(-16/3), so N_phi>=exp(-16/3)/2. With v=1/[s(1-s)]>=4,

    |phi|<=e^-4, |phi'|<=16e^-4, |phi''|<=416e^-4.

For the last two bounds use |v'|<=v^2, |v''|<=2v^3+2v^2 and the
maxima of (v^4+2v^3+2v^2)e^-v on v>=4. It follows that

    ||b_*'||<=2e^(4/3), ||b_*''||<=32e^(4/3),
    ||b_*'''||<=832e^(4/3).                             (FI9)

Choose the even fixed spatial cutoff

    lambda(x)=b_*((|x|-X+sigma/2)/sigma).

It transitions strictly inside the declared bands and is constant on
neighborhoods of their endpoints; the absolute value causes no lack of
smoothness near zero because the function is identically zero there.
A finite explicit choice is

    l1=2e^(4/3)/sigma, l2=32e^(4/3)/sigma^2,
    l3=832e^(4/3)/sigma^3.                              (FI10)

For Note 43's exterior heat test take
eta_O=b_*((|x|-X-sigma)/sigma), c1=l1,c2=l2. Retain FT14's convolution
sign and all FT15 derivative products. These specified profiles do not
remove any GS5/GS8/GS12 term. Their exact normalizing integral is part
of the fixed cutoff definition; the displayed bounds need no quadrature.

## 4. Fully elementary core regulator floors and coefficient caps

Denote the **real source saddle** by L_s, distinct from log(2+X).
On 95<=t<=97 it satisfies

    1/2<L_s<1, 226<kappa=8t L_s-2t+36<618,
    0<kappa'<13, 1<M0<e^110.                            (FI11)

Here 4pi exp(4L_s)=2tL_s+9. Indeed q_t'(1/2)>0 and q_t'(1)<0
using 3<pi<22/7 and 8/3<e with e^2<8; the larger root lies between.
The source exponent q_t(L_s) is at least q_t(1/2)>87/28>0 and at
most 106. Insert these bounds in SC1's M0. Also
kappa'=8L_s+16tL_s/kappa-2 is positive and <13.
These estimates concern the explicit regulator saddle, not the complex
outer saddle or a theta-zero onset.

The fixed C=Phi(0)sqrt(pi)/2 obeys 4e^-4<C<4. The lower bound uses
just the first positive theta-source term at zero. For the upper bound,
Phi(0)<=2pi^2 C_b e^-pi<4, with C_b=(1-16e^-3pi)^-1<2.
Thus the exact physical regulator on the full core has the explicit floor

    e_c=E_eta exp(-R_c^2/452),
    E_eta=min((2/5)eta e^-4,1/618),
    epsilon_g(t,x)>=e_c,              |x|<=R_c, t in J.  (FI12)

Indeed epsilon_b>= (2/5)eta e^-4 and
M0 kappa^-1 exp(-x^2/[2kappa]) >=618^-1 exp(-R_c^2/452).
Their geometric interpolation is at least the smaller lower bound.
A convenient upper bound is q<=16eta^2+e^220. This is a floor on the
finite core only, never a substitute for the gap/exterior field floors.

For the switch chi on J, v=(t-64)/64 lies in [31/64,33/64]. Its logit
has v derivative <=9, hence |chi'|<1/16. With beta=chi/kappa,

    beta<=1/226, |beta'|<=1/(16*226)+13/226^2<1/512.

Write log epsilon_b=l_b and log(M0/kappa)=l_+. Then
|l_b|<=|log eta|+8, |l_+|<=110, |l_b'|<=1/190, |l_+'|<2.
Consequently the regulator coefficient caps required in FT10–FT12 are

    A_t=4+(118+|log eta|)/8+R_c^2/512,
    |r_t|<=A_t,
    R1<=R_c/113, R2<=1/113,
    T1<=R_c/256, T2<=1/256, Th<=R_c^2/14464,
    c_r<=1/113+R_c^2/113^2,
    b_r<=A_t+(1/113+R_c^2/113^2)/2.                     (FI13)

These are caps on finite coefficient functions, not source or solution
errors. They include the derivative of the switch and its logarithmic
amplitude mismatch.

For a source-independent compact transfer table use

    a_C=1/(2e_c), b_C=e_c^-2, k_C=e_c^-1.                (FI14)

Canonical moments supply P_j. For j=0,2 and
U0=1+log(111), an explicit upper bound from Note 11's split is

    B_j=40[U0^(j+1)exp(97U0^2+13U0)/(j+1)
                                      +Gamma((j+1)/2)/2].

Set bar d_0=bar d_2=1 for this coarse source construction and take
P_j=B_j+1; any tighter frozen caps must also enter FI15b's minimum.
For kernel norms through four,
put a=(315/256,315/4,315,4725/4,16065/4); then

    ||partial^alpha K||infinity<=a_(alpha_x)a_(alpha_y),
                                      |alpha|<=4.       (FI15)

These follow by differentiating k's polynomial and summing absolute
coefficients (using k_0's sharper actual maximum). Thus the core FT4/
FT10–FT12 coefficients now consist of explicit elementary expressions
in R_c, eta and the still-declared common covariance cap. If a finite
coarse cap is needed instead of PE30's sharper O(L) cap, use CJ12 with
the actual model amplitude cap on the entire seam support as well as
P_0; do not apply a pure-G cap to a support partly containing P. The
model amplitude cap is gamma-defined, not additional theta data.
This coarse cap is suitable for a finite cost requirement; it must not
replace the sharper cap in Note 43's claimed asymptotic decay.

A single scalar source tolerance can now be stated. For d0,d2<=varepsilon<=1,
put Z=varepsilon/e_c^2. Since e_c<1, the pointwise core ledger obeys

    s_C,w_C<=Z,
    v_m,C<=[(1+m/2)P2+1/2]Z,                 m=0,1,2,
    st_C<=(A_t+2P2+1)Z,
    wt_C<=(A_t+3P2+1)Z,
    ct_C<=(A_t+11P2+3)Z.                                (FI15a)

For a weight a, multiply its supremum by these coefficients and by
area(C_p)<=4. Substitute these explicit replacements in FT11–FT13 and
FT16 (core E,B are zero), including J through three and the already
fixed common M_gamma. Let D_r be the resulting coefficient after
factoring out 4Z in row r; the mean-product term uses e_gamma<=4k_gamma Z.
Thus D_r is a finite arithmetic expression from FI13–FI15 and the
specified mean cap, with no remaining source error. One sufficient
uniform core demand is

    varepsilon_core=e_c^2 min_(D_r>0) theta_c,r/(4D_r),
    varepsilon<=min(1,varepsilon_core).                 (FI15b)

Include the auxiliary common-cap rows, and keep the exterior/gap debits
out of their source reserve. The band demand additionally requires
varepsilon<=min_(j=0..3) mu_s L^j A_min. This explicit common tolerance
may be more conservative than separate FT20 columns, but closes all
source orders with the one source recipe below.

## 5. Positivity without an order loss: clip each rational cubic

Let p_i be the exact cubic Hermite interpolant of chosen rational value/
slope data on a cell of width h. If those data approximate the complete
Phi's endpoint data with errors a,b, HE4 and the cardinal identities give

    |p_i-Phi|<=B4 h^4/384+a+h b/4.

Because Phi>=0, projection onto [0,infinity) is a contraction relative
to Phi. Therefore f_i=max(0,p_i) satisfies

    |f_i-Phi|<=|p_i-Phi|.                               (FI16)

No Bernstein-positivity fallback to second order is necessary for this
constructor. This does not change or reinterpret the earlier Hermite
768 diagnostic or its retained fallback/storage failures.

A cubic has at most three distinct real roots; split at those roots and
use the polynomial on positive subintervals and zero otherwise. Degenerate
zero polynomials and multiple/endpoint roots are handled by deduplication.
Thus f is a nonnegative compact piecewise polynomial with at most four
pieces per original cell. Exact rational coefficients give real algebraic
splitting endpoints. Its field G=integral_0^U exp(tu^2) f(u)cos(zu)du
is an entire exact heat field and has the same finite Gaussian-moment
representation as HE12, now with algebraic endpoints. Corners in f do
not impair differentiating its compact integral in t or z. There is no
zero-count interpretation or all-height potential comparison for G.

A global finite constant for the complete fourth derivative is

    sup_(u>=0)|Phi''''(u)| < B4=2^20.                    (FI17)

Here is an elementary certificate using HE1–HE3. For the absolute
polynomial coefficients c=(1875,30930,68096,41408,8448,512), the first
mode is bounded by

    Q1=(8/5)sum_(j=0..5)c_j (j+1)^(j+1)(3/8)^(j+1)
                                               =75122271/80.

For p=j+5/4, use p^(1/4)<8/5 and
p^(j+1)e^-p<= (j+1)^(j+1)e^-(j+1). For n>=2 the HE3 tail, using
4pi>12 and e>8/3, is bounded by

    r4=(3/2)^12(3/8)^15<1,
    Qtail=2(3/8)^12 sum_(j=0..5)c_j 12^(j+1)/(1-r4)
                  =2055936470669686996992/28821512495674177.

Exact rational arithmetic verifies Q1+Qtail<2^20. This bounds the
complete source on the entire positive half-line; it is not a sample
or finite-mode fourth derivative masquerading as a complete cap.

## 6. An explicit source recipe for any finite jet requirement

Let 0<varepsilon<=1 be an absolute accuracy demand for each of the four
jets j=0,1,2,3 on t in J, |y|<=4 and every real x. Define

    Q=log(32/varepsilon),
    U=ceil(4+log(5+Q)),
    F=U^4 exp(97U^2+4U),
    n0=max(3,ceil sqrt(log(2^14 F/varepsilon)/2)), N=n0-1,
    M=ceil(U max(1,(B4 F/(48varepsilon))^(1/4))), h=U/M,
    b=ceil log2(64F/varepsilon).                         (FI18)

All ceilings involving logarithms or exponentials mean certified integer
upper bounds (an interval upper endpoint's ceiling, with at most two
extra units, suffices). This avoids deciding equality with an integer;
the conservative choices preserve the bounds and cost rates.
Use the rational nodes u_i=iU/M. Obtain dyadic data v_i,d_i for the finite
Phi_N(u_i),Phi_N'(u_i), with errors <=varepsilon/(16F). Form each
normalized Hermite cubic by exact rational arithmetic and clip as in FI16;
extend f by zero above U. Its description is finite, source-defined,
nonnegative, and independent of t,x,y.

The separate continuous jet debits are

| Category | Allowance for each jet j<=3 |
| --- | ---: |
| Complete-source fourth-order interpolation | varepsilon/8 |
| Omitted nodal values plus omitted nodal slopes | varepsilon/8 |
| Nodal value plus nodal slope arithmetic | 5varepsilon/64 |
| Complete source tail | varepsilon/8 |
| Exact rational coefficient construction | 0 |
| Positive clipping, beyond the preceding debits | 0 |
| Total before field evaluation/filtering | 29varepsilon/64 |

To verify the table, integral_0^U u^j exp(97u^2+4u)du<=F for j<=3.
The interpolation choice gives B4 h^4/384<=varepsilon/(8F).
For n0>=3, the HE5 reciprocal geometric factors (1-r_k)^-1 are <2,
and its monomial envelopes imply

    tau0+h tau1/4<=2^11 n0^6 exp(-3n0^2)
                 <=2^11 exp(-2n0^2)<=varepsilon/(8F).   (FI19)

In detail, tau0<=64n0^6e^-3n0^2 and
 tau1<=2^12 n0^6e^-3n0^2; h<=1 and 64+2^10<2^11.
All omitted-mode errors are retained, including the signed derivative
tail through its absolute envelope. The nodal data contribute at most
(1+h/4)varepsilon/(16F)<=5varepsilon/(64F).

For the complete tail use FB7 with s=97,Y=4. U>=4 and
4+Q<=exp(U-4). Elementary exponential inequalities give, for j<=3,

    16pi exp(4U)>=194,
    lambda_j=4pi exp(4U)-194U-13-j/U>=pi exp(4U),
    2pi^2 C_b U^j/lambda_j<=1,
    97U^2+13U-pi exp(4U)<=-2exp(4U)<=log(varepsilon/8).

For example e^U>=2U^2 for U>=4 pays the polynomial terms; the remaining
negative exponential is much larger than Q. Thus T_j<=varepsilon/8.
The table follows with no coefficient rounding because exact rational
operations define the chosen cubic. No error is silently removed by
clipping. Subsequent special-function evaluation, algebraic-endpoint
rounding, observable arithmetic and filtering are additional debits.

This construction can be made effective without an oracle for nodal data.
For completeness, a deliberately coarse finite enclosure procedure is:
use b fractional bits, and set

    P=b+20+ceil(9log2(N+1)+26U/log 2),
    T=ceil(10N^2 exp(4U)+13U+1).

Use positive rational approximants pi_hat and approximants to the
positive exponentials with absolute error <=2^-P. Form A_hat=pi_hat
n^2 (exp(4u))_hat exactly. Enclose exp(-A_hat), at that exact rational
argument, to error <=2^-P, and pay |A-A_hat| separately by the derivative
bound below. Machin's arctangent formula with P+4 terms and exponential
Taylor degree ceil(P+8T+4) suffice. Propagate finite products exactly,
then round to the b-bit grid. The source summands and derivatives are

    [2pi^2 n^4e^(9u)-3pi n^2e^(5u)]e^(-A),
    [30pi^2 n^4e^(9u)-15pi n^2e^(5u)-8pi^3 n^6e^(13u)]e^(-A),
                         A=pi n^2 e^(4u).

A conservative product-error bound is 2^16 N^9 e^(26U)2^-P,
which is <=2^-b/16; the b-bit rounding fits the prescribed nodal debit.
The large negative exponential's derivative is bounded by one on its
positive argument A; it is not bounded by exp(T). The Taylor-degree
claim follows from the ordinary exponential remainder and
m!>=(m/e)^m with m>=8T+P. These are constructive finite bounds;
this nodal enclosure procedure has **not** been executed here.

## 7. Description size and consumption of the transfer gate

Safe nodal magnitude caps are |Phi_N|<=2^8 and |Phi_N'|<=2^14, from
the same global monomial envelopes. The normalized cubic's integer
coefficients after clearing denominator 2^b M have height below
2^(b+17)M. Put

    B=b+20+ceil log2(M+1).

There are 2(M+1) b-bit-fractional nodal data and at most 3M algebraic
splitting endpoints. Each endpoint can be described by its cell cubic,
root index and dyadic isolating interval. An intentionally conservative
source-description upper bound, including those data, is

    storage <=64(M+1)(B+1) bits.                        (FI20)

An elementary isolation bound explains why this is finite. For a
squarefree integer cubic of coefficient height H<=2^B, its nonzero
integer discriminant and |root|<=1+H give root separation
>=1/(16H^4). A dyadic grid of depth 8+4B in [0,1], with exact sign tests,
isolates its simple roots; roots equal to grid points are recorded
exactly. Repeated-root cubics have rational repeated/simple roots and
are handled by exact gcd/fixed-degree algebra, not by a strict sign
change assumption. This is a very inefficient possible construction,
not a statement that FI20 bits can be produced in linear time. Nodal
transcendental enclosure, root isolation, and later field evaluation
retain their separate work costs.

For fixed Y_b=4 and q0=log(1/varepsilon) tending to infinity, FI18 gives

    U=O(log q0), N=O(sqrt(q0+log^2 q0)),
    M=varepsilon^(-1/4) exp(O(log^2 q0)),
    b,B=O(q0+log^2 q0).                                (FI21)

Thus if a core transfer requires varepsilon=exp(-a X^2), a>0 fixed,
this sufficient construction has

    M=exp(a X^2/4+O(log^2 X)),
    nodal precision O(X^2), mode count O(X).             (FI22)

This is an explicit **upper** bound; it is neither a lower bound nor
proof that every possible source is unaffordable. No storage/runtime
acceptance cap was specified or tested. The old finite-source failure
at all heights after 64 remains: this all-real-x **absolute jet** bound
does not give a global relative field/potential comparison where H and
q shrink. The joined field uses G only on its bounded core and gap.

To consume Note 43, choose one varepsilon below 1, every FT20 permitted
d_0,d_2 (or the explicit FI15b common core demand), and all four FT19
values mu_s L^j A_min. The 29/64 margin pays
those demands with one source. FI12–FI15 can be substituted directly into
the core coefficient table. Every cutoff, model, transition, exterior,
source and actual-covariance row of Note 43 still has to fit its own
allocation. Source refinement cannot pay a failed nonsource row.

## 8. The exact finite acceptance gate that remains unpaid

Even granting a finite gamma model chart satisfying FI1–FI8, the first
**theta-dependent** gap-admissibility debit is

    mu_o(X,I)=max_(0<=j<=3) sup_(G_an)
                |partial_z^j(H-P)|/(L^j A)
                         <=1/4-mu_s,       c0=1/2.      (FI23)

G_an includes the full enlarged analytic neighborhoods of both bands,
not selected real points. For example choosing mu_s=1/16 for this initial
floor gate requires mu_o<=3/16. Tighter source/field inputs may be needed
for the final observable targets; passing FI23 alone accepts no tuple.

The attempted payment from FS20 has the form, with its original R=2+t+|x|
and mathcal L=log R,

    |H-P|/A <= C { t^(3/2)/N^2 + R^(-t log2/8)
                              +R^b0 exp(-c t mathcal L^2) },
    N=1+|x|+t mathcal L, R>=R_*.                        (FI24)

FS7 and PE9 then transfer to the needed analytic derivative bounds.
But C,c,b0,R_* and the corresponding circle/derivative constants were
not made finite in Notes 30–31. Their proofs establish eventual bounds;
substituting 1 for these constants, or choosing a large round X without
R_*, would not verify FI23. This uncertainty remains when the finite
source error tends to zero. The signed-pole, collar-count and weighted
exterior constants in FT7/FT9/FT15 are further finite acceptance inputs,
not automatically supplied by the model-only residual FI8.

Therefore this return accepts **no particular finite gap index n** and
no numerical theta construction. FI23 is unpaid from the present
finite evidence, not proved false. There is no discovered failure of
Note 43's uniform comparison and no universal no-go claim for fixed
spatial joining. The model caps FI1 and collar margins themselves also
need finite evaluation before a chosen chart is accepted; this note
provides their formulas without claiming that evaluation occurred.

## 9. Evidence, controls and disposition

The [five-case rational audit](../numerics/FINITE_INPUT_RATIONAL_BOUNDS_20261024.json)
and its [script](../numerics/finite_input_rational_bounds.py) check only
FI17's rational majorant, its mode ratio, FI15 kernel coefficient sums,
the beta' ceiling and the real-regulator-saddle bracket arithmetic.
They do not sample Phi, H, gamma or model gaps. No source nodes were
evaluated, no mesh/precision search was run and no certificate of the
full theorem is claimed. The [assessment](../reviews/25_FINITE_INPUTS_AND_SOURCE_COST_ASSESSMENT_20261024.md)
records same-model proof checks and their limitations.

Collision screening is unchanged: a positive finite source or a generic
heat-transfer identity may collide. The theta-specific coefficient/
completion assumptions and FI23 are the premises absent from the
changed-source controls; the gap floor fails on a transition covering a
zero. Euler-factor, weighted-square, reflected/smooth-positive-primitive,
atomic and heat-polynomial controls are not excluded by source positivity
or by this cost construction. No RH or simplicity inference follows.

**Disposition:** AN02 r1 closes as completed bounded analysis with an
explicit positive-source description bound and retained unpaid FI23.
HDA-17 remains Partial, HDA-18 Gated and HDA-20 unfulfilled. No manuscript,
snapshot or milestone change.

**Next: Analysis — Sol**, [HDA-18-AN03 r1](../research-progress/handoffs/HDA-18-AN03.md):
make the full complex-buffer FS20 field remainder effective on J=[95,97],
including its Cauchy circles, or return the first contour component that
cannot be given an explicit finite bound. This is the named finite input
blocking FI23. Gamma/model evaluation and any eventual theta certificate
remain separately budgeted; no sweep or new chat is dispatched.
