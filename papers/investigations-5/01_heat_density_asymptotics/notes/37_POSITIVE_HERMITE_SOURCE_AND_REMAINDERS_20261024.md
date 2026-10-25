# Positive cubic-Hermite finite source and explicit remainders

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from session metadata. Thread
`01a170a3-5f6e-7aa2-9e33-bcae4835c782`, chat **0011**.

**Status: routine remainder/positivity bounds proved in-note; bounded
floating comparison with exact selected polynomial controls.** No
continuous full-observable numerical acceptance is asserted.
This answers [HDA-17-AN03 r1/r2](../research-progress/handoffs/HDA-17-AN03.md)
and continues [Note 36](36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md).
The canonical source, physical regulator, unnormalized observables and
fixed kernel/targets remain unchanged. Read the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [rounding/evidence](../../../../avoid/06_status_stronger_than_the_evidence.md).
This is a quantitative approximation milestone, not an RH-equivalent criterion.

## Decision and quantitative result

**Retain the positive 768-cell cubic-Hermite source, explicit fourth-order
remainder and ideal-Gauss evaluator bounds. With r2's directional gradient
caps, every one of the 91 sampled source rows fits its 80% allocation at the
two existing points. This is an informative floating diagnostic, not an
accepted continuous core.** Nodal/source-budget/evaluator rounding and
continuous filter integration are still unpaid. HDA-17 remains Partial;
HDA-18 remains Gated; HDA-20 independent review is unchanged.

The [r1 record](../numerics/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json),
[r2 supplemental record](../numerics/HERMITE_DIRECTIONAL_CAPS_20261024.json),
[source implementation](../numerics/hermite_source.py),
[main diagnostic](../numerics/positive_hermite_diagnostic.py),
[directional-cap comparison](../numerics/hermite_directional_caps.py),
[exact controls](../numerics/check_hermite.py) and
[assessment](../reviews/20_POSITIVE_HERMITE_SOURCE_ASSESSMENT_20261024.md)
retain the evidence. All eleven frozen r1 input hashes match; r2 separately
pins the immutable r1 record. The physical source/regulator/target contract
is unchanged. The r2 request was appended before its execution and adds
only a new valid error-envelope comparison at the same two observations.

### Same-mesh and storage-cost comparisons

Source cutoff 1.5, four modes and the original t=64,x=4,y=0,1/2 centers are
retained. The adaptive 768 node hash exactly matches AN02; adaptive 384 uses
every second one of those nodes, so it is the nested quantile mesh for the
same source-only density. No field values or zero data select source nodes.

| Source | Nodal value/slope scalars | Order0 interpolation allowance | Worst r1 source/(0.8 target) |
| --- | ---: | ---: | ---: |
| uniform 192 Hermite |386|8.48491e-5|1697.07|
| adaptive 384 Hermite |770|7.77535e-6|161.689|
| adaptive 768 Hermite |1538|5.34704e-8|1.10507|
| AN02 adaptive 768 linear |769|1.04980e-4|2056.73|

Hermite at 768 cells lowers the same-mesh interpolation allowance by about
**1963 times**. It stores both values and slopes, so this is not a
cost-neutral comparison. At comparable nodal storage (770 versus 769),
Hermite 384 improves the source allowance substantially but still fails the
full norm. Its positive fallback makes the distinction concrete.

The stored source is **nonnegative**, with zero coefficients/cells allowed.
All finite Bernstein coefficients are checked as nonnegative binary64 data,
which define exact dyadic coefficients in the mathematical source. This
proves positivity of that chosen source on its entire support. Canonical
nodal accuracy remains a separate ledger. There are 65,37,59 fallback cells
for uniform 192,adaptive 384,adaptive 768. Their contiguous ranges are
approximately [.86719,1.375], [.68462,1.38584], [.81503,1.37632], respectively.
The order0 fallback contributions are 1.75e-20,7.33051e-6,8.79e-15. Thus the
storage-matched 384 case is dominated by fallback at its lower edge near
u=.685; the 768 fallback is negligible. The record retains exact cell
indices, ranges and all weighted contributions. Underflowed coefficients
are zero data in the finite model; complete canonical tails remain positive.

### Preserve the r1 failure and the r2 gain

With the original common gradient caps, adaptive 768 gives Delta Q
allowances 0.00884058 and 0.00274925 at y=0,1/2. Its source allocation is
0.008. The y=0 ratio 1.10507 is retained as the r1 failure; unused arithmetic
or integration budgets are not silently reassigned to it.

The r2 common caps keep each physical gradient direction separate. Their
Delta Q allowances become

| Observation | r1 allowance | r2 allowance | r2 source/(0.8 target) |
| --- | ---: | ---: | ---: |
| t=64,x=4,y=0 |0.00884058|0.00550999|0.688748|
| t=64,x=4,y=1/2 |0.00274925|0.00179015|0.223769|

Only covariance rows change. All other r1 rows and observable values are
inherited unchanged. The next-largest source row at y=0 is R_t,x, ratio
0.202177; at y=1/2 the source rows are smaller still. For orientation, the
same-mesh AN02 linear Delta Q allowance at y=0 was 16.4538, about 2986 times
the final Hermite/cap allowance. That is an allowance comparison with
specified methods, not a measured actual-error reduction or universal
cost lower bound.

### Explicit source and evaluator remainders

For the 768 source, interpolation allowances at source orders 0--3 are

    [5.3470386e-8, 3.5776473e-8, 2.4408408e-8, 1.6743577e-8].

The mathematical continuous-cell formulas HE1--HE9 below bound the complete
canonical source, including all omitted modes and the cutoff tail. The
r1 source ledger at order0 separates:

| Category | Allowance |
| --- | ---: |
| Hermite/fallback interpolation |5.3470386e-8|
| Omitted endpoint values |3.45818e-33|
| Omitted endpoint derivatives |7.25093e-34|
| Nodal value arithmetic candidate |1.22598e-12|
| Nodal derivative arithmetic candidate |1.50834e-14|
| Stored coefficient-construction discrepancy |2.43810e-17|
| Complete source tail |log10 allowance=-483.767|

The last term is positive and is preserved logarithmically. Construction
discrepancies use exact rational differences between stored coefficients
and the ideal polynomial of the stored node/value/slope data, converted
upward to binary64. Mapping them through numerically evaluated weights
still retains source-ledger arithmetic uncertainty.

The derivative candidate uses a positive sum of differentiated monomial
magnitudes plus 1e-300, so cancellation near Phi_N'(0) does not suppress
its scale. At 80 digits, the maximum observed value/slope candidate ratios
are [.0708202,.0930915] for uniform 192, [.0469957,.0461973] for adaptive 384,
and [.118339,.116447] for adaptive 768. These finite comparisons leave the
transcendental/node arithmetic candidates unproved.

The explicit ideal-Gauss 12 truncation bounds (HE10) for the 768 source, over
the full standing buffer D+ at t=64 with Y=1,|z|<=sqrt(101), are

    [3.06293e-17, 5.18836e-16, 3.67474e-16, 5.69233e-15].

They are mathematical truncation bounds evaluated in floating arithmetic;
rounded nodes, weights, polynomial evaluation, exponentials, trigonometric
functions and summation have separate unpaid arithmetic. The weaker 8-node
bounds are also retained. Gauss12 is primary for both filter rules; the
8-node comparison is evaluated only on the fine filter geometry and is
recorded for both weak and direct four-jet observables.

The local transfer freezes caps using total source errors plus the 12-node
truncation vector before mapping source/evaluator categories. R2's largest
mapped evaluator truncation allowance is 1.40143e-11 for Delta Q at y=0,
only 1.40143e-8 of the evaluator allocation. This neither pays nor replaces
later evaluator rounding.

### Filter indicators, controls and work

The same composite 8/12 filter geometry is retained. Across the final 91
rows at the two best-source points, the maximum ratios to the 10% allocation
are 0.000823813 for weak observable filter change, 0.140097 for the selected
direct observable filter change, and 0.00444251 for the new positive-envelope
filter change. Weak/direct source-rule 8/12 changes have maximum ratios
2.16716e-10/1.42109e-10. Direct/weak identity disagreement reaches ratio
0.000140429. These are diagnostic indicators. Min/absolute-value switching
curves in the new directional envelopes and the curved |Delta K| zero set
are not continuously enclosed by axis splitting; no filter remainder or
rounding certificate is inferred.

Eight exact-rational polynomial control families pass, including cubic
reproduction, the quartic remainder sign/factor 1/24, endpoint value/slope
perturbations, positive cardinal moments, fallback and dyadic-coefficient
construction. Assertion counts describe scope; they do not validate theta
source accuracy. No new 120-digit or switch-time field case was performed.

R1 main execution 106.444440 seconds and r2 execution 38.597589 seconds,
with a conservative total AN03 numerical debit 160.042 seconds, stay below
the 30-minute cap. Hermite 384 has 770 shared nodal values/slopes and 1536
stored per-cell coefficients, versus 769 shared nodal values and 1536
unshared linear coefficients at 768 cells. Its source Gaussian 12 rule has
4608 nodes, versus 9216 at 768 cells. Composite filters have 16384/36864 field
points. Runtime, exact interaction counts and environment are retained in
the records; no wall-time saving is inferred from a model label. All
artifacts are below 1 MiB and large arrays are regenerated in memory.

## r2 directional common-gradient cap

Let G be the exact ideal-Gauss 12 field of the chosen finite source. Write
bar_delta_j=d_j(source)+d_j(eval12). Freeze LC6 coefficients on the disk
|H_j-G_j|<=bar_delta_j, in particular P1>=|G_z|+bar_delta1. At t=64,
r_x=r_y=0, so both gradient errors have the LC8 envelope

    dbar_i=2a bar_delta1+2P1 b_* bar_delta0,
    |S_H,i|,|S_G,i|<=G_i^univ=2P1 a.

Triangle inequality also bounds both by |S_G,i|+dbar_i. Hence

    G_i^common=min(G_i^univ, |S_G,i|+dbar_i)              (HE11)

is a valid pointwise common cap for each i=x,y. Keep the two actual
finite-field gradient magnitudes distinct. Substitute these caps in
LC9/LC10 and their component derivative versions. At t=64 the two
error-column vectors coincide, so the sums can use G_x+G_y; there is no
extra outer factor 2 for duplicated components. Global mean products are
formed after all support integrals, exactly as before.

For the ledger, HE11 is frozen using total source+evaluator errors;
individual source/evaluator categories then enter only through the linear
gradient-error columns. No source category recomputes a smaller cap.
These are continuous mathematical inequalities given their field/jet
premises; sampled field/gradient inputs retain arithmetic and integration
uncertainty. The supplement uses the common cap HE11, not the stronger
half-sum variant one can derive for covariance alone.

## Disposition and next deliverable

AN03 r1 is closed with its retained overrun; r2 is closed with informative
sampled source allowances and explicit remainders. The positive 768 source
is a useful candidate for certification. Source/nodal/budget/evaluator
arithmetic, continuous filter integration, D/time coverage and endpoint
field/residual errors remain unpaid. CJ27 still has no accepted cutoff
ratio. HDA-17 is not accepted, and no HDA-18 spatial or all-time assembly
follows from these two observation centers.

**Next: Analysis and numerics — Sol.** Enclose the nodal values/slopes,
complete source-cap/chord arithmetic and one fixed-point filter integral
for this frozen 768 source. Use interval arithmetic with explicit source,
evaluator and filter remainder payments before expanding the time/space
box. Preserve the 384 fallback failure as the storage-cost comparator.
This is a bounded certification task within the established methods;
there is no identified extra high difficulty issue requiring Astra.

## Explicit finite-field representation

On each cell expand the stored cubic as sum_(k=0..3) p_(i,k)u^k. Its
field is a finite sum of cosine Gaussian moments, so it retains an explicit
finite definition rather than another complete theta integral. Let
I_k(a,b)=integral_a^b u^k exp(tu^2+izu)du. I_0 is the Note 20 FB4 error-function
primitive difference, and for k>=1,t!=0,

    2t I_k=[u^(k-1) exp(tu^2+izu)]_a^b
                     -(k-1) I_(k-2)-iz I_(k-1),         (HE12)

with the k=1 middle term zero. Average the +z/-z formulas for cosine.
The t=0 limits are removable. The production diagnostic uses the positive
Gaussian rule with HE10 truncation bound, avoiding the known unstable
bare error-function subtraction. No root information enters its coefficients.



## 1. Complete fourth derivative of the canonical source

For A=pi n^2 exp(4u), the canonical source summand is

    Phi_n(u)=pi^(-1/4)n^(-1/2)e^(-A) A^(5/4) P0(A),
    P0(A)=-3+2A.

Since d/du=4A d/dA, define

    P_(k+1)(A)=(5-4A)P_k(A)+4A P_k'(A).

The first four derivative polynomials are

    P1=-15+30A-8A^2,
    P2=-75+330A-224A^2+32A^3,
    P3=-375+3270A-4232A^2+1440A^3-128A^4,
    P4=-1875+30930A-68096A^2+41408A^3-8448A^4+512A^5.

Thus the required complete-source formula is

    Phi^(4)(u)=pi^(-1/4) sum_(n>=1) n^(-1/2)e^(-A_n)
                               A_n^(5/4) P4(A_n).          (HE1)

The signs, degree, powers and constant factors follow from the recurrence,
not from fitting values. Exact integer recurrence controls below check P4.

### Continuous cell cap

On a source cell [a,b], let l_n=pi n^2 exp(4a), r_n=pi n^2 exp(4b).
One elementary continuous upper bound for each retained mode is

    pi^(-1/4)n^(-1/2) sum_(j=0..5) |c_j| m_(5/4+j)(l_n,r_n),

where c=(-1875,30930,-68096,41408,-8448,512), and
m_p(l,r)=v^p exp(-v), v=clamp(p,l,r).

A potentially tighter cap retains P4's signed polynomial. Put d=r-l,
t_j=d^j P4^(j)(l)/j! and take its degree-five Bernstein coefficients

    beta_k=sum_(j=0..k) [binom(k,j)/binom(5,j)] t_j,
    k=0,...,5.

Then |P4(A)|<=max_k |beta_k| throughout [l,r], so one may instead use

    pi^(-1/4)n^(-1/2) m_(5/4)(l,r) max_k|beta_k|.          (HE2)

Take the smaller valid retained-mode cap if useful. Sum retained modes
and append a complete positive tail. For a cap evaluated through n=N_B,
let n0=N_B+1, A0=pi n0^2 exp(4a), and

    r4=(1+1/n0)^12 exp[-pi(2n0+1)exp(4a)].

Provided A0>=25/4 and r4<1, the omitted fourth-derivative modes contribute
at most

    pi^(-1/4)n0^(-1/2)e^(-A0)
       sum_(j=0..5)|c_j| A0^(5/4+j) / (1-r4).            (HE3)

Each monomial decreases with u on this omitted range. Its mode-power
factor is n^(2p-1/2), whose largest exponent is 12. Successive-mode
ratios are bounded by r4; all powers and exponential ratios then decrease
as n grows. The old N_B=8 choice satisfies these gates on u>=0; this
does not change the finite source's separate four-mode count N=4.
HE2/HE3 are continuous inequalities. Floating evaluation of them still
needs arithmetic accounting and does not become an interval enclosure.

## 2. Hermite interpolation with complete-source error

On [a,b] write h=b-a>0, s=(u-a)/h. The cardinal basis is

    H00=2s^3-3s^2+1=(1-s)^2(1+2s),
    H01=-2s^3+3s^2=s^2(3-2s),
    H10=s^3-2s^2+s=s(1-s)^2,
    H11=s^3-s^2=-s^2(1-s).

The exact Hermite interpolant to a C4 function g is

    Hg=g(a)H00+g(b)H01+h g'(a)H10+h g'(b)H11.

The repeated-node Rolle argument gives, at every interior u,

    g(u)-Hg(u)=g^(4)(xi_u)(u-a)^2(u-b)^2/24,
    |g-Hg| <= B4 (u-a)^2(b-u)^2/24,                      (HE4)

where B4 bounds |g^(4)| throughout the cell. Endpoints have zero error.
The sign in HE4 is positive when g^(4)>0; for g(u)=u^4 it is exactly
(u-a)^2(u-b)^2. The pointwise maximum allowance is B4 h^4/384.

Apply HE4 to the **complete** Phi, using HE1--HE3 for B4. Comparing its
complete endpoint data with the chosen finite-mode/numerical endpoint
data is a separate step; a Phi_N fourth-derivative cap alone is not the
complete-source interpolation bound.

## 3. Endpoint omitted modes: values and derivatives are distinct

At a node v, let n0=N+1 and A0=pi n0^2 exp(4v). The existing value tail is

    0<=Phi(v)-Phi_N(v)<=tau0(v),
    tau0(v)=2pi^2 n0^4 exp(9v-A0)/(1-r0(v)),
    r0(v)=(1+1/n0)^4 exp[-pi(2n0+1)exp(4v)].

The derivative tail has signs from P1; it is **not** a positive omitted
source value. A safe absolute endpoint bound is

    |Phi'(v)-Phi_N'(v)|<=tau1(v),
    tau1(v)=pi^(-1/4)n0^(-1/2)e^(-A0)
       [15A0^(5/4)+30A0^(9/4)+8A0^(13/4)]/(1-r1(v)),
    r1(v)=(1+1/n0)^6 exp[-pi(2n0+1)exp(4v)]<1.          (HE5)

The largest mode-power exponent here is 6. This is a direct geometric
sum of positive monomial majorants, with no assertion that Phi'-Phi_N'
is positive. In fact for the current N>=1,u>=0, every omitted A exceeds
the larger root (15+sqrt(105))/8 of P1, so those derivative summands are
negative. Their signed cardinal factors must still be handled correctly.

Let the implemented nodal data satisfy

    |v_i-Phi_N(u_i)|<=sigma0_i,
    |d_i-Phi_N'(u_i)|<=sigma1_i.

Before coefficient-construction error, the pointwise cubic source error
on [a,b] is bounded by the sum of

    interpolation:  B4 (u-a)^2(b-u)^2/24,
    omitted values: tau0(a)H00+tau0(b)H01,
    omitted derivs: h tau1(a)H10+h tau1(b)|H11|,
    value arithmetic: sigma0_a H00+sigma0_b H01,
    deriv arithmetic: h sigma1_a H10+h sigma1_b |H11|.     (HE6)

The derivative basis has H10>=0 and H11<=0. Replacing H11 by a positive
hat without its absolute value/sign would be a transcription error.
Endpoint derivative arithmetic cannot inherit the value arithmetic
allowance. A merely relative |Phi_N'| candidate is ill-conditioned near
derivative cancellation; an absolute differentiated-term scale plus a
floor is a safer diagnostic candidate, still unproved without enclosure.

## 4. Positive Bernstein source and a linear fallback

For given implemented endpoint values v_a,v_b and derivatives d_a,d_b,
the ideal cubic Hermite polynomial has degree-three Bernstein coefficients

    beta0=v_a,
    beta1=v_a+h d_a/3,
    beta2=v_b-h d_b/3,
    beta3=v_b.                                          (HE7)

If the stored finite binary64 coefficients beta_hat are all finite and
nonnegative, the **chosen finite source** sum beta_hat_k B_k^3(s) is
exactly nonnegative on the full cell: B_k^3>=0 and sum B_k^3=1.
No unproved rounding assumption is needed for this positivity statement.
The binary64 numbers are exact dyadic coefficients defining that source.
One may take C_i=max_k beta_hat_(i,k) as its exact real amplitude cap.

The relation to ideal Hermite data is a different issue. If

    |beta_hat_(i,k)-beta_ideal_(i,k)|<=gamma_(i,k),

where beta_ideal uses the actual stored node geometry and the ideal
operations in HE7, add the separate construction term

    E_construct(u)<=sum_(k=0..3)gamma_(i,k)B_k^3(s).        (HE8)

This includes rounded cell-width/coefficient construction. Copies of
endpoint values can have zero construction error, while the nodal value
error in HE6 remains. A high-precision discrepancy is a diagnostic, not
automatically a rounding bound. Nonnegative stored coefficients do not
pay HE8 or any nodal error. Actual stored nodes should define the source;
any reference grid difference must also remain in its arithmetic ledger.

If HE7's stored coefficients cannot establish positivity, use the exact
line through nonnegative stored endpoint values,

    L(u)=(1-s)v_a+s v_b.

This branch is nonnegative. Its complete-source interpolation allowance
is the existing linear B2(u-a)(b-u)/2, not the cubic B4 allowance. It
uses endpoint value tails/arithmetic only; derivative data are unused and
their errors need not be charged to that cell. If the line is instead
stored as rounded degree-elevated cubic coefficients, retain its own
construction term, since it need no longer equal the exact line.
Do not clip a cubic coefficient and continue to call it the ideal Hermite
polynomial without charging that change in HE8.

Piecewise positive polynomials with fixed nodes and coefficients define
the same kind of exact finite heat field as before:

    F(t,z)=integral_0^U exp(tu^2) f(u) cos(zu)du.

Each chosen source satisfies F_t=-F_zz exactly; source derivative jumps,
linear fallbacks and the existing cutoff jump do not change this fact.
Endpoint derivative matching is not needed for the finite integral's
entire field or heat identity.

## 5. Absolute cardinal integrals and source-jet ledger

On the unit interval, the absolute cardinal moments are

| Polynomial | integral | integral s times polynomial |
| --- | ---: | ---: |
| H00 | 1/2 | 3/20 |
| H01 | 1/2 | 7/20 |
| H10 | 1/12 | 1/30 |
| abs(H11) | 1/12 | 1/20 |
| s^2(1-s)^2/24 | 1/720 | 1/1440 |
| B_k^3 | 1/4 | (k+1)/20 |

In physical coordinates, constant positive weight W gives

    int H00 W du=int H01 W du=h W/2,
    int h H10 W du=int h |H11| W du=h^2 W/12,
    int [(u-a)^2(b-u)^2/24]W du=h^5 W/720.

For the same t=64,Y=1 source-jet weights W_j=u^j exp(64u^2+u),
j=0,...,3, convexity permits the same secant upper bounds as Note36.
If one whole-cell chord has endpoint values W_a,W_b, the exact positive
upper integrals are

    J00=h(7W_a+3W_b)/20,
    J01=h(3W_a+7W_b)/20,
    J10=h^2(W_a/20+W_b/30),
    J11=h^2(W_a/30+W_b/20),
    J4=h^5(W_a+W_b)/1440,
    JB_k=h[(4-k)W_a+(k+1)W_b]/20.                        (HE9)

Subdividing a source cell and integrating each local chord times these
global-cell polynomials is tighter. The cardinal integrands have degree
at most four after multiplication by a chord; the Hermite remainder
integrand has degree five. Integrating only through degree three would
reuse the old linear formula incorrectly. These are exact polynomial
integrals of a continuous chord majorant, apart from arithmetic in its
endpoint weights and summation.

For each jet order j, integrate every HE6/HE8 term against W_j, add across
cells, and keep value-mode, derivative-mode, value arithmetic, derivative
arithmetic and construction arithmetic distinct. Append the unchanged
complete-source tail T_j beyond U. Each cell's branch determines whether
its interpolation row is cubic or linear. The field-jet bound then follows
from |partial_z^j cos(zu)|<=u^j exp(Yu), as in LC2. Later field evaluation
and spatial averaging remain separate categories.

## 6. Explicit ideal-Gauss finite-field truncation remainder

The parent-proposed source quadrature remainder is valid. This is a
bound for the mathematical ideal G-point Gauss rule; rounded nodes,
weights and elementary-function/summation arithmetic remain separate.

For a positive cubic cell f with max f<=C_i=max beta_hat, let c=(a+b)/2,
d=(b-a)/2, u=c+v. For either exponential sign, write

    exp(tu^2 +/- izu)
       =exp(tc^2 +/- izc) exp([(2tc +/- iz)v+t v^2]).

Uniformly on the cell, let

    theta_i=(2|t|c+|z|)d+|t|d^2,
    M=floor((2G-1-j-3)/2)>=0.

The exponential series through power M, multiplied by f(u)u^j, has
polynomial degree at most 2M+3+j<=2G-1, so ideal Gauss integrates it
exactly. Its remaining integrand is bounded in absolute value by

    C_i b_i^j exp(tc_i^2+Yc_i+theta_i)
                 theta_i^(M+1)/(M+1)!.

The true integral and the positive Gauss weighted sum of that remainder
are each at most h_i times this bound, because the ideal weights sum to
h_i. The two exponential signs have cosine weights 1/2, so their sum
does not add another factor of two. Consequently

    |jet_j(F)-ideal_Gauss_G(F)|
       <= 2 sum_i h_i C_i b_i^j exp(tc_i^2+Yc_i+theta_i)
                      theta_i^(M+1)/(M+1)!.              (HE10)

For G=8, j=0,1,2,3 the values of M are 6,5,5,4; for G=12 they are
10,9,9,8. A linear fallback can be safely treated as degree three.
The full standing D+ at t=64 allows Y=1 and |z|<=sqrt(101); smaller
honestly declared support caps can also be used. HE10 is an explicit
truncation inequality beyond refinement agreement. A floating evaluation
of HE10 still has its own arithmetic uncertainty. It does not pay source
nodal/construction error or spatial-filter integration.

## 7. Exact controls and limits

[check_hermite.py](../numerics/check_hermite.py) contains eight exact-rational polynomial control
families: the source derivative recurrence; nontrivial cubic reproduction
on [1/3,5/4]; quartic remainder sign and factor 1/24; independent endpoint
value perturbations; endpoint derivative perturbations including H11's
negative sign; all absolute cardinal/Bernstein moments; a negative cubic
with positive endpoints and its positive linear fallback; and exact
nonnegative dyadic stored coefficients with a separate construction ledger.
All identities and selected rational envelope inequalities passed.

The sole retained control execution took **0.007861791 seconds** in
Python3.10.0 on macOS27.0.1 arm64, using the standard library. The script
SHA-256 is `12616a421690eac6dc73bf096bfee4f88fbc408c72f677272e756a6188a16d59`.
[HERMITE_CONTROLS.json](../numerics/HERMITE_CONTROLS.json) records exact inputs, differences/moments,
environment and runtime. The controls check algebra, not theta-source
numerics, continuous field errors, rounding or filter integration. No
repository/history write or additional observation was made by this
subagent.

## Control screen and review provenance

This source construction and the generic regulated transfers allow
colliding controls. Polynomial controls here lack canonical theta data;
Euler-factor controls change the source; weighted-square controls change
its fixed weights/reflection; reflected controls lack the canonical square
expansion; smooth/positive-primitive controls lack unchanged theta
arithmetic; atomic controls lack the C4 source-density interpolation
premise. No collision family is excluded by positivity or Hermite algebra.
Only the complete-source cap constants use the canonical theta expansion.
The recorded approximation gain supports no RH, simplicity, regulator
removal or global compatibility conclusion.

The assessment includes a separate read-only same-model subagent audit.
Prior source premises remain shared; this is not independent specialist
review or HDA-20. The manuscript, old notes/records and other chats'
transcripts remain unchanged. R1 evidence remains immutable after r2.
No commit or manuscript snapshot was created.

## Reproduction

With NumPy/mpmath available, run from numerics, using an external/ignored
output folder for regeneration. The control script writes beside itself,
so run a copy to preserve the frozen original control record:

```sh
cp check_hermite.py /tmp/check_hermite.py
python3 /tmp/check_hermite.py
python3 positive_hermite_diagnostic.py --repo /path/to/shifted-zeta-positivity --output /tmp/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json
python3 hermite_directional_caps.py --repo /path/to/shifted-zeta-positivity --output /tmp/HERMITE_DIRECTIONAL_CAPS_20261024.json
```

The supplemental replay reads the frozen r1 record in the repository and
checks its script/source hashes and the original covariance coefficient
replay before changing caps. All records identify the actual Python/NumPy/
mpmath environment, field/source nodes, coefficients and inputs by hash.
These identify the recorded data and do not replace proof or ensure
bitwise portability across arithmetic libraries.
