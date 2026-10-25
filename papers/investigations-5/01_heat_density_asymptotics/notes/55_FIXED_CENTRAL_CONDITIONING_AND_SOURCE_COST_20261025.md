# Fixed central conditioning, direct source collars and improved source cost

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Chat **0019**, thread
`01a17463-238b-7352-982f-f0d3c155e1c8`.

**Status: improved sufficient source-transfer and description-cost bounds
proved in-note; same-model internal checks only.** This returns
[HDA-23 / HDA-17-AN04 r1](../research-progress/handoffs/HDA-17-AN04.md),
using [Note54](54_EFFECTIVE_POSITIVE_ATTACHMENT_AND_ALL_TIME_EXISTENCE_20261025.md)
and [Review34](../reviews/34_EFFECTIVE_POSITIVE_ATTACHMENT_ASSESSMENT_20261025.md).
The regulator floor is now used only on a fixed central rectangle, where
multiple events remain allowed. Direct H/G collars pay the remaining
growing core. For the same complete tuple and fixed time slab, the
sufficient source description improves from a quadratic exponential in
joining radius to

    log(source cells), log(explicit descriptor upper bound)
        = pi R/32 + O_(fixed slab,eta,tolerance)(log^2 R).       (IC1)

These are sufficient construction-size bounds, not necessary complexity,
measured costs, affordable implementation or field-evaluator precision.
The fixed central constant can remain extraordinarily large. HDA-17
remains Partial, HDA-18 Gated and HDA-20 unfulfilled. No research
computation, source evaluation or manuscript production was performed.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision screen12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[shared review premises](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scoped claims](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerical scope](../../../../avoid/10_numerics_ahead_of_the_question.md),
[signed cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status maintenance](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is a quantitative approximation/cost improvement, not an RH
criterion or a central collision exclusion. [Manifest55](55_SOURCE_CONDITIONING_INPUTS_20261025.json)
pins the pre-execution sources; [Review35](../reviews/35_SOURCE_CONDITIONING_AND_COST_ASSESSMENT_20261025.md)
states the internal assessment and remaining limitations.

## 1. Unchanged objects, domain and comparison target

Retain canonical H, H_t=-H_zz, physical q=epsilon_g^2, fixed K=k_1 k_1,
unnormalized S=log(|F|^2+q), and actual covariance
Q=K*(S_x^2-S_y^2)-(U_x^2-U_y^2). The actual source approximation G is
the entire exact-heat field of one nonnegative clipped-cubic source.
Assume its independently paid absolute errors satisfy

    |partial_z^j(G-H)|<=epsilon, j=0,1,2,3,
       all real x, |y|<=4, t<=b.                              (IC2)

The source constructor below gives this with29epsilon/64 before field
evaluation/filtering. IC2 is a field error, not an observable agreement.

First take J=[95,97], b=97, exactly the conditioning domain requested
by r1. Use the same P branch, gap, profiles, scalar targets and tuple as
Notes43/47. The result also applies to Note48's paid moving gap on J.
Observation |y|<=1 retains its full support and collar/source buffer4.
Let R_c be the paid union core radius, including its gap and source
enlargements; use R=R_c+8 for all further collar enlargements. The
additional absolute source accuracy costs no horizontal restriction,
since IC2 already holds at every real height.

The tuple includes U,W through order4; R, total calC, J, actual Q and
Delta Q, calB, Ut,Wt,Rt,calCt and actual calS through order2; internal
third current derivatives; heat-potential correction through order4;
and fixed traces at their paid orders. Both curvature derivatives,
component/spatial/moving heat, signed source and actual mean products
remain. No simple-root premise is imposed in the fixed central region.

Section7 supplies the explicit fixed-b extension needed by Note54's
all-time source minimum. Its constants may depend on that already
selected b=T_++1. No claim uniform in simultaneously varying b and R
is made by IC1.

## 2. Separate the fixed central floor from the expanding radius

Use the explicit R_*, C_H and source moments B0,B2 in Note47 EB16.
For definiteness choose

    R0=2R_*+2^2060+64,
    e0=min(1,E_eta exp[-(R0+16)^2/452]),
    M0=C_H[1+log(2+R0+16)]+2.                         (IC3)

Require R_c>=2R0+64. These choices depend on J and eta, not on R_c,
the source or its tolerance. The accepted exterior onset and all
complete disks at the fixed split have strict margins. The only
regulator inverse introduced by the new core argument is e0^(-1).

For raw nonnegative primitive integrals, pay the portion |Re z|<=R0+8
by the existing positive-regulator rational estimates, with coefficient
caps at R0+16 and canonical moments at97. At observations meeting this
fixed region, the extra kernel/collar buffers still fit that fixed
rectangle and remain far from the spatial seam. Actual means there
have the fixed cap M0, after their auxiliary source rows are paid.

Let D_r^0 be the FI15a/b or EB19 coefficients obtained by substituting
this fixed floor, fixed physical coefficients and M0 in the displayed
FT10--FT13/FT16 maps, including the auxiliary mean rows. Define

    K0=1+(4/e0^2) max_r D_r^0.                         (IC4)

This is a maximum of a finite list of stated positive expressions,
not an unknown compact supremum. The fixed-central source allowance
is <=K0 epsilon in every scalar row. Its proof is regular at any
multiple zero because |F|^2+q>=e0^2. No root positions or multiplicities
are used there. The previous expanding e_c(R_c) is not substituted
into IC4.

On the rest of the core use every complete canonical-H collar and
its larger disk supplied by Note47. Collars touching either boundary
of the proof split are included in full; the fixed rectangle pays the
small overlap at R0. No analytic or observable test is multiplied by
the indicator of the split. Only positive raw integrals are enlarged,
then recombined before weak differentiation. This creates neither a
new actual field interface nor a sharp-interface derivative.

## 3. A carrier-aware source parameter and direct H/G collars

Note47 EB7 pays, arm by arm on the full field strip,

    log|S_t(w)|>=-pi x/8-12log^2 x-200log x-202.

Consequently the following monotone exponent is a valid common lower
carrier payment throughout the consumed outer core and bands:

    Psi97(R)=pi R/8+12log^2(2+R)+200log(2+R)+202,
    zeta=epsilon exp[Psi97(R)+32].                     (IC5)

The32 pays fixed collar/carrier comparisons. The weaker exp(-x)
floor would also work, giving q_source=R+O(log R); IC5 retains the
already paid leading gamma exponent. No new contour is required.

Suppose 0<zeta<=exp(-1) and zeta log(2+R)<=2^(-512). On each outer
canonical-H collar, write u=l_c(z-a_H), l_c=log(2+|a_H|), and normalize
the physical units by A_c l_c. Compare

    G_s=H+s(G-H), 0<=s<=1,                            (IC6)

directly with H. Every G_s is real-type and exact heat. Rouché first
on the paid larger disk and then on a small circle gives one real
simple G_s root per H collar and no additional zero on the zero-free
portion of the consumed support. Finite constants can be taken as

| Input | Source-dependent allowance |
| --- | --- |
| root displacement | <=2^64 zeta/l_c |
| slopes/units after normalization | between2^-64 and2^64 |
| logarithmic unit ratio and its derivative | <=2^96 zeta, <=2^112 zeta l_c |
| residue difference, v_F=F_zz/F_z at its root | <=2^160 zeta l_c |
| individual residues | <=32 |
| difference of analytic regular parts of F_zz/F | <=2^192 zeta l_c^2 |
| carrier-sum floor off collars | >=2^-64 |

These are conservative enlargements of the already finite H table.
For the displacement, divide the IC2 field error by H's linear collar
floor. On the larger boundary compare the quotients
(G_s/H)(z-a_H)/(z-a_s); their removable analytic units differ by
O(zeta). The maximum principle and Cauchy on the paid disks give the
unit derivative. For residues compare first and second jets at paired
roots, using the third jet along the displacement segment. Subtract
the two simple poles on a larger boundary and apply the maximum
principle to the analytic remainder. The operations just described
have at most four inverse slope/unit factors, each from the fixed H
table; the displayed powers leave strict room. The zeta*l_c gate
pays the residue correction and all root/unit smallness margins.

H's geometry was proved using P, but P's approximation error is not
included in the source difference in IC6. Replacing zeta by
e_model+zeta in that difference would leave a nonvanishing source
column as epsilon->0 and would not prove the present improvement.
Only H's acquired geometry is inherited from P.

For the complete primitive integrals on any restricted annular part,
enlarge intersecting collars and add the zero-free complement. The
arbitrary-positive-q unit and regularized-pole proofs then give

    s[1], w[1] <=C1 zeta,
    v_m[1] <=C1 zeta[1+log(1/zeta)+l_R^2], m=0,1,2,
    z_m[1]=0 in the pure G_s core,
    l_R=log(2+R), C1=2^1024.                           (IC7)

The genuine pole-translation modulus zeta*log(1/zeta) is retained.
For example remove scaled disks of radius C zeta about the two roots;
their pole integral is O(zeta). On the complement interpolate roots
and logarithmic units at fixed pointwise q/A_c^2. The derivative of
w^m(1-w)/(u-a) is bounded by fixed constants times
zeta(|u-a|^-2+|u-a|^-1). Radial integration gives the stated logarithm.
Residue and regular-part differences supply the l_R and l_R^2 terms.
No inverse regulator is introduced in this operation.

Local source parameters are <=zeta. Their logarithms alone need not
be <=log(1/zeta). Use the increasing combined function
f(u)=u[1+log(1/u)] on(0,1], so f(u_local)<=f(zeta), and enlarge the
remaining u_local*l_c^2 term separately. All kernel derivatives are
transferred only after the raw integrals have been recombined.

## 4. Source variation on the actual bands and the complete tuple

To isolate the source column, use the proof-only family

    F_s=G_s+lambda(P-G_s), 0<=s<=1.                   (IC8)

F_1 is the actual prescribed field; F_0=H+lambda(P-H) is used only
in the error proof and is not inserted in the evaluation formula.
On bands the whole family has the already paid gap floor. With
Delta=G-H, the source directions are exactly

    delta F=(1-lambda)Delta,
    delta B=-lambda_x Delta/2,
    delta E=-lambda_x Delta_z-lambda_xx Delta/4-lambda_t Delta,
    delta E_z=-lambda_x Delta_zz-3lambda_xx Delta_z/4
                 -lambda_xxx Delta/8-lambda_t Delta_z
                 -lambda_xt Delta/2.                 (IC9)

The corresponding B_t and (B_z)_t directions use
Delta_t=-Delta_zz and Delta_zt=-Delta_zzz. Thus jets through3 suffice,
including moving gaps. The component lambda E_P is independent of s.
Its regularized Z_m is not independent of s: changes of the actual
field and weight in Z_m supply a C*zeta*d component term. It is kept
below. Only the pure exterior has identically zero source variation.
On the pure exterior F_s=P, so its source variation, including the
signed outer heat partition and both spatial commutators, is exactly
zero before taking magnitudes. On the pure core E_s=B_s=0.

For a zero-free band, normalize every field jet by its carrier before
differentiating the rational expressions GS8--GS14 in s. Its field
denominator has a fixed positive normalized floor. Keep w and
theta_reg in each expression; their derivatives in a field direction
are bounded uniformly for arbitrary positive q. Hence the source
directions have finite bounds of the form

    delta(TC),delta(Xi): C zeta l_R^2,
    delta(TJ),delta(TU): C zeta(l_R^3+l_R^2),
    delta(TC_t): C zeta[l_R^4+|r_t|l_R^2].            (IC10)

Here and below C is paid explicitly by IC13, not a new asymptotic
input. The full band area is <=C/l_R. The DE,DB source directions
obtained from GS12/GS13 cost at most C zeta l_R^4 pointwise times
their actual regulator weights. The new compatibility-time and signed
source pieces are included. Retaining a fixed nonsource e_model in
IC10 is unnecessary: this is a directional difference along IC8.

For an explicit mechanical band payment at fixed q, write
u=conjugate(F)/D. Product differentiation gives

    delta u=conjugate(delta F)/D
                   -u*2Re(delta F*conjugate(F))/D,
    |delta u|<=3|delta F|/|F|^2,
    |delta w|<=2w(1-w)|delta F/F|,
    |delta[w(1-w)]|<=|delta w|.                        (IC10a)

Apply these rules to the exact GS8/GS12 expressions and their one
physical-time derivative, retaining the actual q,q_t terms. Together
with IC9 and the normalized gap floor they give IC10, including the
component-residual Z variation. No unspecified Lipschitz constant is
being invoked and no inverse physical regulator is used.

The field and its derivatives are the same spatial/moving prescription
as before. The raw integral split at R0 introduces no new real test.
Use the exact global FT10--FT18 maps, including the signed stress
identity before taking absolute values. On a compact J, the physical
coefficient caps at a local center u obey

    R1,T1 <=C_J(1+u), R2,T2<=C_J,
    |r_t|,Th,c_r,b_r <=C_J(1+u)^2.                    (IC11)

Use FI13 on[95,97], or Note54 C2 on[63,b], to specify C_J. The largest
composed weight is |r_t|R1^2, of degree4. It multiplies the local raw
w error in ct[R1^2]. It is never used as an unbounded coefficient on
an all-height integral. All source-active supports satisfy u<=R, so
the finite local-height supremum is explicit. Pure exterior source
variation vanishes. Time-varying q is unchanged.

Actual means are bounded before covariance. Note47 EB16 bounds the
canonical means independently of R_c. Pay the auxiliary source and
nonsource k_gamma*s rows first, so total primitive mean error<=1.
Then use EB17 for the actual F_s means at the observation's local
height. On a fixed-central support the mean cap is the fixed M0;
on annular and seam supports it is C_H(1+l_R)+1. In FT13 use the
actual global mean-product subtraction, not component covariances or
separate positive pole squares. These caps add only explicit logarithms
and no expanding-floor exponential.

The following table names every consumer of the new source primitives:

| Complete row | Source payment |
| --- | --- |
| U,W through4; auxiliary mean rows | k_alpha*s, k_alpha*w; fixed-central plus IC7/IC10 |
| total calC,R through2 | FT11/FT12 with w[R1],w[R2],w[R1^2], band deltaTC |
| J through2, order3 internally | n_alpha*v0+k_alpha*v1[R1], band deltaTJ |
| Ut,Wt,Rt,calCt through2 | FT10/FT11 with all rt,T1,T2,Th weights; band IC9/IC10 |
| actual Q,Delta Q | signed V0 and squareS first; then FT13 actual mean products and deltaXi |
| calB through2 | actual b_r*w difference |
| actual calS through2 | direct Rt and current derivatives plus signed band DE,DB; outer source variation0 |
| heat-potential correction through4 | deltaXi/2+2Re deltaZ0; separate component and joining heat |
| fixed boundary/time traces and equation sums | paid row orders and their actual component sums |

## 5. One finite improved source map and tolerance

All constants in the next display are finite before choosing R_c or
epsilon. A generous explicit coefficient is sufficient. Let C_H and
B_j be the paid canonical mean/moment constants on the fixed slab;
let W_J>=1 dominate each coefficient in IC11 after its displayed
power of1+u has been removed. Let Lprof>=1 dominate the fixed FI9/FI10
profile constants after factoring out l_R^j, including speed8 for a
moving gap. Let Dmod be the finite residual coefficient from EB4 or
Note54 C1, and K_* be Note54 EA3's fixed kernel bound. Set

    A_J=1+K0+C_H+sum_(j=0..3)(B_j+1)+W_J+Lprof
               +e0^(-1)+R0+K_*+Dmod,
    C_J^src=2^8192 A_J^128,
    P(R)=(1+R)^8.                                    (IC12)

For fixed[95,97], use B1=(B0+B2)/2 and the analogous complete B3
moment formula from the same source split, or the larger Note54 C3
formula at b=97. W_J is explicitly obtained from FI13 by collecting
the constant,linear and quadratic coefficients. For general b use its
displayed A_b,Bprime_b,1/18,1/324 coefficients. For a completely explicit enlargement one may take
W97=2^16(1+|log eta|), W_b=2^16(1+A_b+Bprime_b),
Lprof=2^64(1+exp(4/3)), and Dmod=2^32(1+b)^4. These
dominate the stated coefficient/profile/residual lists, including speed8;
no supremum of an unspecified profile or model field is needed.

To verify the generous exponent, the core coefficients are the finite
FI15/EB19 maps. Their inverse-floor powers and moment/weight/mean
products have degree<16 in A_J. The annular constants IC7 have at
most four slope/unit inverses and the declared finite geometric caps.
The band rational source variation has denominator powers at most4
after normalization, profile derivatives at most3, and at most one
direct time derivative. FT10--FT18 are positive linear maps except
the bilinear actual mean-product row. Even allowing32 input factors
and2^16 terms, their coefficient fits IC12. The largest physical
weight degree is4; retaining all profile/pole/mean logarithms and
using log(2+R)<=1+R gives the conservative degree8 in P(R).

Thus every source-active scalar row, including the auxiliary rows, has
the complete source allowance

    E_source,r <= K0 epsilon
       + (C_J^src/2) P(R) zeta[1+log(1/zeta)]
       <= C_J^src P(R) zeta[1+log(1/zeta)].            (IC13)

The last inequality absorbs K0 epsilon using epsilon<=zeta and
C_J^src>=2K0. This is the source column only. The paid nonsource
gap/exterior/residual columns remain additional and unchanged.

For positive row reserve 0<theta_s<=1 set

    d=theta_s/[C_J^src P(R)],
    Htol=1+log(4/d), zeta_tol=d/(4Htol),
    epsilon_loc=exp[-Psi97(R)-32] zeta_tol.            (IC14)

All root/unit gates hold because C_J^src>=2^8192 and P dominates l_R.
Since 1+log(1/zeta_tol)=Htol+log Htol<=2Htol, IC13 is <=theta_s/2.
No inversion of an unknown modulus or source fit is required. The
continuous source-constructor margin29/64 is retained separately.

For the cost policy choose theta_s as the minimum of a fixed positive
remaining row reserve and the named nonsource envelope: B_mov(X0) or
B_sw(X0), respectively; for Note54 choose
theta_s=min(delta/4,B_b^+(X0)). For the fixed-gap template one may
instead choose theta_s=min(fixed row reserve,(1+R)^(-4)), which is
below its paid decreasing envelope at the accepted onset. These
explicit policies have -log(theta_s)=O(log R) at fixed slab and targets.
Further over-refinement is allowed but is not claimed to retain the
cost asymptotics. A fixed quarter-target alone would not establish
vanishing error as X0 grows.

One can always take the larger of the old and new proved core tolerance
caps before intersecting the other source requirements. This avoids any
claim that the new sufficient rule is larger at every finite radius.
For fixed J,eta and row targets, however,

    log(1/epsilon_loc)=Psi97(R)+O(log R)
      =pi R/8+12log^2 R+O(log R).                     (IC15)

The fixed-center inverse floor affects the constant in O(log R), not
an R^2 term. This is an improved sufficient loss; neither the old
Gaussian loss nor the remaining linear loss is asserted necessary.

## 6. Finite source-description and construction costs

Put q_s=log(1/epsilon), Q_s=log(32/epsilon), and let s>=0 be the
fixed upper time of the source constructor. s=97 serves r1; s=b serves
Note54. The following shorter replacement for Note54 C5 is sufficient:

    U=ceil[4+log(2+s+Q_s)], F=U^4 exp(sU^2+4U),
    n0=max(3,ceil sqrt(log(2^14 F/epsilon)/2)), N=n0-1,
    M=ceil[U max(1,(2^20 F/(48epsilon))^(1/4))], h=U/M,
    beta_bits=ceil log2(64F/epsilon),
    Bbits=beta_bits+20+ceil log2(M+1).                 (IC16)

Ceilings use the predecessor's certified integer-upper-bound convention.
The same clipped rational Hermite cubics have <=4M positive pieces,
2(M+1) value/slope data and <=3M algebraic clipping endpoints. The
explicit descriptor bound remains

    storage<=64(M+1)(Bbits+1) bits.                   (IC17)

Write S_bound=64(M+1)(Bbits+1) for this explicit sufficient descriptor
bound. The asymptotic equalities below concern S_bound, not a minimum
possible encoding or a lower bound on actual storage.

For the shorter cutoff, U>=4 and s,Q_s<=exp(U-4). From exp U>=2U^2,
sU^2<=exp(2U-4)/2<=exp(4U)/4 and13U<=exp(4U)/4. Thus
sU^2+13U-pi exp(4U)<=-2exp(4U), while
lambda_j=4pi exp(4U)-2sU-13-j/U>=pi exp(4U), j<=3.
The complete tail prefactor is <=1, and2exp(4U)>=Q_s, so FB7 gives
tail<=epsilon/8. The interpolation, omitted values/slopes and nodal
arithmetic arguments are unchanged; the four separate debits total
29epsilon/64. Positive clipping introduces no extra error. This source
is one fixed source for every t<=s and every real x on strip4.

Since2^20 F/(48epsilon)>1,

    M=ceil[kappa_src U^2 exp(q_s/4+sU^2/4+U)],
    kappa_src=(2^20/48)^(1/4).                        (IC18)

This finite formula and IC16/IC17 should be used when b varies with
tolerance. With Ubar=5+log(2+s+Q_s), replace U by Ubar for immediate
upper bounds on M and beta_bits; no O_b term conceals that dependence.
For fixed s and q_s->infinity,

    log M=q_s/4+(s/4)log^2 q_s+O_s(log q_s),
    log S_bound=q_s/4+(s/4)log^2 q_s+O_s(log q_s),
    beta_bits,Bbits=O_s(q_s), N=Theta_s(sqrt(q_s)).    (IC19)

At fixed J,eta,tolerance substitute IC15. The sufficient comparison is

| Source policy | Leading log cell/descriptor bound | Nodal fractional bits | Mode count |
| --- | --- | --- | --- |
| FI12/FI15b expanding floor, J=[95,97] | R_c^2/904+O(log^2 R_c) | O(R_c^2) | O(R_c) |
| Note54 coarse expanding floor, fixed[63,b] | R_c^2/144+O_b(log^2 R_c) | O_b(R_c^2) | O_b(R_c) |
| Direct collars with the weaker exp(-x) carrier | R_c/4+O_b(log^2 R_c) | O_b(R_c) | O_b(sqrt R_c) |
| IC5/IC14 sharper paid carrier, J=[95,97] | pi R/32+(109/4)log^2 R+O(log R) | O(R) | O(sqrt R) |

The old two rows describe the specified sufficient tolerance policies,
not an impossibility or a lower bound on all methods. At equal large
radius the new leading exponent is linear. The cell/descriptor count
still grows exponentially, and huge fixed constants can delay any useful
gain. Neither nodal bits nor descriptor size is field working precision.

The finite nodal-enclosure construction from FI18 also gives

    P_work=beta_bits+20+ceil[9log2(N+1)+26U/log2],
    T_work=ceil[10N^2 exp(4U)+13U+1],
    D_Taylor=ceil[P_work+8T_work+4].                  (IC20)

For fixed s, P_work=O_s(q_s), T_work,D_Taylor=O_s(q_s^5). The
displayed Machin/Taylor node algorithm therefore has a rational
arithmetic-term bound O_s(M q_s^(11/2)), before clipping isolation.
This counts arithmetic operations, not their bit complexity or runtime.
No such operation was executed in this analytical packet.

For completeness the inefficient FI20 isolation grid can be replaced
analytically by a pruned sign-variation tree. First remove and record
roots at0,1 and compute the fixed-degree gcd with P'. For a repeated
cubic, its repeated root and remaining root are rational (a repeated
irreducible quadratic would require degree>=4); compute them directly
from this gcd and the quotient. Rational-root denominators are <=H
for original integer coefficient height H, so distinct such roots
are separated by >=H^(-2). This handles the repeated case without
assuming a height bound for a newly formed squarefree polynomial.

For the original squarefree degree<=3 cell polynomial of height
H<=2^Bbits, form P0=P,P1=P' and
P_(i+1)=-rem(P_(i-1),P_i). At a zero of an intermediate P_i, its
neighbors have opposite signs, so the variation count is unchanged.
At a simple P0 root it drops by one. Thus the endpoint variation
difference counts the real roots of any root-free-endpoint interval.
This is the usual Sturm argument, stated here to specify its consumer.

Bisect only intervals with positive root count. At most3 intervals
at any depth contain roots. Exact midpoint roots are recorded and
factored; repeated roots are handled by the fixed-degree gcd first.
All separation bounds use the original cell polynomial before removing
endpoint or midpoint factors; deflation removes roots and cannot reduce
the separation of those remaining. The FI20 separation bound for an
original height<=2^Bbits squarefree cubic is
1/(16*2^(4Bbits)). Depth8+4Bbits therefore suffices for isolation.
There are at most6(8+4Bbits)+O(1) tested nodes per cell, and each
fixed-degree variation evaluation uses a fixed number of exact rational
operations. The additional clipping isolation has a conservative
2^20 M(Bbits+1) operation bound. This avoids a claim that the full
2^(8+4Bbits) grid is scanned in descriptor-linear time. It changes no
source coefficients or error category. No bit-optimality is asserted.

Each positive cubic piece contributes Gaussian integrals of powers
u^k, k<=6, for G through G_zzz. The symbolic evaluation prescription
has O(M) fixed-order erf/exp/elementary primitive calls per point and
<=4M pieces. Complex-erf accuracy, endpoint rounding, cancellation,
observable arithmetic and continuous averaging require their own
error/cost analysis. IC20 and the source-bit bounds do not pay those.

## 7. Consume the improvement in Note54's entire source minimum

Fix Note54's already selected T_+, b=T_++1, eta and scalar allocations
before choosing its moving spatial gap. Use its effective [63,b]
table. Let R0(b) be twice the maximum of its explicit Rstar_b and
2exp(Lambda_b)+32, plus64. This is fixed independently of the new seam.
Use e0(b)=min(1,E_b exp[-(R0(b)+16)^2/72]) only in that fixed region.
Use Note54's B_j(b), C_Hb and compact coefficient caps in IC4/IC12.
The same proof gives IC13/IC14 on [63,b], now with

    Psi_b(R)=pi R/8+Aamp_b[1+log(2+R)]^2,
    Aamp_b=2^16(1+b)^2.                              (IC21)

Its armwise full-buffer lower bound follows from Note54 C1's explicit
log-gamma payment. The actual field and moving-gap identities are
unchanged. The nonsource compact/seam columns remain B_b^+(X0).
Select theta_s<=min(delta/4,B_b^+(X0)) to preserve their decreasing
family, and use the new source cap instead of the old expanding
epsilon_core in every core consumer, including auxiliary mean rows.

The late relative-field clause must also be paid, separately from
the full-tuple core map. On the fixed late central rectangle, Note54
EA6 gives the positive floor

    A_*=exp[-4b log^2(b+2)-2(R0(b)+5)],
    c_*=min(1,A_*).

On the outer part use the proved armwise exp(-Psi_b(R)) floor.
Therefore the following full complex late-core carrier bound is valid:

    A_min_late,new=c_* exp[-Psi_b(R)].                (IC22)

Indeed it is <=A_* on the central part and <=exp(-Psi_b(R)) on the
outer part. It is not an extrapolation of an outer bound through the
unproved central regime. c_* is a possibly terrible fixed-b constant,
but it is independent of R_c. This replaces the old exp(-2R_c)
factor in EA6. At the spatial band use A_min_gap,new=exp(-Psi_b(R)).

Set a_X=X0-Dmov_b, R_c=X0+Dmov_b, L=log(2+R_c) and retain
e_min=T_+^(3/2)/[1+R_c+b log(2+b+R_c)]^2. One new common sufficient
source tolerance is the positive minimum

    epsilon_new = min{1, epsilon_loc(b,R,theta_s),
       a_X^(-2)exp[-Psi_b(R)],
       T_-^(-5/2), delta/[4(1+K_mid(T_-))],
       delta/[2^69 K_bridge L^3],
       e_min c_* exp[-Psi_b(R)]/16}.                 (IC23)

All three earlier conservative clauses are replaced: the expanding
epsilon_core, the exp(-R_c-16) band floor, and the exp(-2R_c) late
carrier floor. Keeping one of those clauses in the minimum would
retain its old quadratic or larger linear source-size exponent.
The original Note54 prescription remains valid; IC23 specifies a new
allowed source choice for the same field formula and row allocations.

Earlier negative/middle demands are constants in spatial R; the
pre-switch bridge adds only3log L in negative logarithm. The new gap
and late demands each have negative logarithm Psi_b(R)+O(log R),
and IC14 has the same dependence when theta_s is the stated decreasing
polynomial/logarithmic reserve. Hence, at fixed b and prescribed
scalar accuracy,

    log(1/epsilon_new)=pi R/8+O_b,eta,theta(log^2 R),
    log M,log S_bound=pi R/32+O_b,eta,theta(log^2 R),
    beta_bits,Bbits=O_b,eta,theta(R), N=O_b,eta,theta(sqrt R). (IC24)

For IC21 specifically the log-square coefficient of log M is
(Aamp_b+b)/4 when the other reserve logarithms are O(log R). Finite
IC16--IC18, rather than fixed-b asymptotics, apply when b varies.

The late relative clause in IC23 pays Note54's mixed-field collar
premise throughout the actual positive core; it is not inferred from
the new observable bounds. The positive bands retain the full lambda_+
derivatives and TJ5 compatibility variation. On supports meeting core
and band, use Note54's uniform actual late mean cap for the entire
blend before FT13. The new core source map does not insert compact
C_Hb into C_+ or alter the order C_+ -> T_+ -> b -> gap/source.

Both endpoint formulas and the all-real-time/all-height domain table
of Note54 are consequently retained with the newly constructed single
source. The only possible multiple-event premise in the ordinary
central comparison remains the positive fixed-region regulator floor.

## 8. Dominant estimates, controls, disposition and next consumer

The previous dominant sufficient loss was the expanding core
epsilon_g^(-2) and its covariance/weight coefficients. IC3--IC14
confine that loss to a fixed rectangle and prove an error map tending
to zero with epsilon in every required row. Outside, direct source
pole translation retains its logarithm and the paid carrier sets the
leading remaining source precision. IC23 checks every all-time source
consumer, rather than improving one clause while leaving the old
quadratic core minimum active.

The remaining leading R-dependence of this construction is the
carrier-relative demand at the growing seam/annulus and late core.
It is a sufficient exponential loss, not a lower bound or a universal
obstruction. The still enormous fixed central coefficient and the
positive-endpoint/compact onset choices may dominate every usable
finite instance. No affordable source, evaluated coefficients, field
working-bit bound, continuous filter certificate or stability theorem
has been supplied.

The collision screen is unchanged. Euler-factor controls change the
canonical completion; weighted-square/finite-prime controls lack the
full unchanged coefficients/reflection input; reflected, smooth and
positive-primitive controls lack the canonical gamma/source identity;
atomic and heat-polynomial controls lack the smooth complete theta
source. The fixed-positive-regulator comparison permits multiple
events and is generic. The collar comparison applies only where its
simple-root/field-floor premises have been proved; it makes no claim
about an event elsewhere. No new control sampling was performed.

Standard analytic tools were checked against the primary
[DLMF Cauchy formula](https://dlmf.nist.gov/1.9.E31),
[sectorial gamma remainders](https://dlmf.nist.gov/5.11#ii) and
[polynomial division/Horner formulas](https://dlmf.nist.gov/1.11).
The last page supplies division/evaluation tools, not the sign-variation
proof, which is given explicitly above. The sharp carrier estimate is
the paid internal EB7/C1 estimate, not a new theorem imported from DLMF.

**HDA-17-AN04 r1 CLOSED — analytical source-conditioning/cost improvement
complete; HDA-23 Complete at this bounded improvement scope.** This
does not establish useful cost or complete HDA-17/18. Their statuses
remain Partial/Gated, and HDA-20 remains unfulfilled. The manuscript,
earlier notes and original packet request are preserved. No numerical,
exact-rational or machine-symbolic research execution, theta/source/
gamma/field sampling, mesh/precision/interval campaign, evaluated source,
snapshot, DRAFT_HISTORY milestone, commit, new user-owned chat or model
change occurred. Formula/algorithm derivations are analytical; hashes,
sizes, links and history capture are housekeeping.

**Next: Analysis — Sol**, prepared/unexecuted
[HDA-17-AN05 r1](../research-progress/handoffs/HDA-17-AN05.md): test a
positive analytic-source compression against this exact four-jet
tolerance and complete-tuple consumer. Prove the canonical complex
branch/approximation inputs and coefficient-error ledger before any
smaller cost claim. This is a candidate direction, not an established
polynomial-cost theorem. The current source-data-bit bound must not
be relabeled a field-evaluator bit bound. HDA-20's distinct full-chain
review should include this conditioning replacement as well as Note54.

Pasteable continuation: Continue HDA-17-AN05 r1 using Note55/Review35.
Prove one nonnegative compressed-source construction and complete
four-jet/cost ledger, or return the first exact unpaid analytic input;
keep the packet analytical-only and preserve the global consumer.
