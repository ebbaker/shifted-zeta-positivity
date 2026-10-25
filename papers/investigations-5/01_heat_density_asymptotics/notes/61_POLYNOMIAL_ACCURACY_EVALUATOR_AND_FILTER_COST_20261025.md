# Polynomial accuracy-bit cost for the complete evaluator and filter

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol, actual recorded effort ultra**,
chat0021, turn `01a17566-c7a0-7702-b608-fe983c0c1b44`.

## 1. Quantitative gain and scope

For the **unchanged complete IC23 tuple**, fix its certified descriptor
and a compact rational query/slack box Q. Let p be the requested
additional absolute output-accuracy bits and I the query encoding length.
For exact rational/dyadic independent scalar parameters and the explicit
canonical/elementary provider recipes below, the algorithm has

    bit cost <= C_(descriptor,Q)(1+p+I)^40,
    working storage <= C_(descriptor,Q)(1+p+I)^8.      (PC1)

For more general computable fixed scalar inputs permitted by Note59,
retain their stated provider costs. Let C_ext(P), S_ext(P) bound one
request to all such external scalar providers at P bits. Then the
general bounds are the PC1 work bound multiplied by
1+C_ext(C_(descriptor,Q)(1+p+I)), and the PC1 storage bound plus
S_ext(C_(descriptor,Q)(1+p+I)). A fixed scalar can have arbitrarily
slow computable digits; its accuracy cost cannot be hidden in a constant.
For polynomial-time scalar providers the total remains polynomial, with
their degree added if necessary. No scalar value or tuple is changed.

The constants are computable positive expressions from the descriptor,
local branch/magnitude data and the physical regulator floor; they are
independent of p and I. They can be enormous. The proof gives the
more informative node and precision formulas PC9--PC12 below. The loose
degrees in PC1 cover the stated schoolbook algorithms, not an optimal
complexity claim.

This improves [Note59](59_EVALUATOR_WORKING_PRECISION_AND_CONTINUOUS_FILTER_20261025.md):
its Euler-product gamma and midpoint profile/filter recipes have
exponential sufficient cost in requested accuracy bits even after fixing
the descriptor and query box. They are replaced here by shifted Stirling,
finite rational high-order interpolation and the inherited smoothness
bounds. No field, source, kernel, regulator, covariance, time join or
observable is replaced. All signed defect components and both curvature
time rows remain. [Note60](60_EXACT_PHASE_INDEX_BY_DYADIC_ONSET_SELECTION_20261025.md)
continues to supply the exact phase index with the authorized onset freedom.

PC1 does **not** assert polynomial cost uniformly in height, time or
descriptor size. In particular its constants still depend on inverse
physical floors. Section8 gives a separate inverse-floor-free puncture
estimate for weak primitives and identifies its remaining complete
consumer. That estimate is not silently substituted for the raw circuits
used to prove PC1.

This is quantitative evaluation analysis, not an RH-equivalent criterion,
positivity proof or collision exclusion. Opening inputs are pinned in
[Manifest61](61_COMPLETE_EVALUATOR_COST_INPUTS_20261025.json). Read the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification01](../../../../avoid/01_restating_the_target.md),
[premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[shared review05](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[signed cancellation12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [quantitative gain20](../../../../avoid/20_volume_without_a_gain.md).

## 2. Spatial smoothness with explicit, fixed constants

Use the notation G_3(V,A) for a real or complex function on a real
rectangle whose **pure-axis** derivatives obey, in each coordinate i,

    |partial_i^r f|<=V A^r(r!)^3, r>=0, V,A>=1.       (PC2)

Mixed derivative bounds are unnecessary for the interpolatory rule.
Time rows are separate fixed functions of the spatial coordinates.
All caps hold on the entire support/slack box, including field seams.

The crude inherited flat bump bound in EV12 is already sufficient:

    ||phi^(r)||<=r! 2^r(2r)^(2r)<=64^r(r!)^3,
    ||b_*^(r)||<=2^11 64^r(r!)^3.                    (PC3)

Here r^r<=e^r r! and e^2<8. These are Gevrey-3 bounds; no improved
Gevrey order is assumed. The flat function exp(-1/s), extended by
zero, has the same sufficient bound by the same exponential derivative
argument. Its positive-denominator quotient gives the physical switch
chi. Translate a profile freely and replace A by A/h for scale h<=1.
Fixed spatial or time-profile derivatives are handled by the derivative
rule below; the moving center and its finite time jets are coefficients.

The following one-coordinate rules prove closure, independently for x,y.
Pad every displayed V,A to be at least1.

| Output | Sufficient V | Sufficient A |
| --- | --- | --- |
| f+g | V_f+V_g | max(A_f,A_g) |
| fg | 3V_f V_g | max(A_f,A_g) |
| partial_i f | V_f A_f | 8A_f |
| 1/f, real f>=d>0 | 1/d | 2A_f(1+V_f/d) |
| exp(f) | exp(V_f) | 16A_f(1+V_f) |
| log(f), real f>=d | max(V_f+1/d,3V_f A_f/d) | max(8A_f,2A_f(1+V_f/d)) |

For products, the Leibniz sum after division by (r!)^3 is bounded
by sum_j binom(r,j)^(-2)<=3. For the derivative rule,
(r+1)^3<=8^r for r>=1. The inverse derivative recurrence is bounded
by the geometric sum of (A_f/A_out)^j, j>=1; multiplying that sum by
V_f/d is <=1. For exp(f), use (exp f)'=f'exp f, the same normalized
Leibniz recurrence and A_out>=16A_f,2V_f A_f. For log use f'/f
and then integrate the derivative bound. These arguments include r=0
via the declared magnitude caps. Complex inverses are implemented as
conjugate(f)/|f|^2 with the positive modulus-square floor, as in EV15.
Conjugation and real/imaginary parts preserve bounds.

### 2a. Actual IC23 leaves and guards

The fixed source jets have bounds independent of real height:

    |partial_i^r partial_t^h partial_z^j G|
      <=100 U^(2h+j+1) exp(s_b U^2+Y U) max(1,U)^r,

on their real support/slack box, with the fixed finite h,j of EV59.
This follows directly from 0<=f<100 and u<=U; it needs no absolute
power-coefficient cancellation bound. That separate bound is retained
for evaluation error. These leaves satisfy PC2. Every required fixed
mixed spatial/time jet is supplied as its own leaf. The derivative row
in the table proves a bound along the same active coordinate only;
pure-axis bounds alone do not imply bounds for transverse derivatives.
The analytic component jets and explicit products of one-dimensional
profile jets provide those separate leaves before the algebraic rules
are applied. No missing mixed-derivative premise is assumed.

For N, q and r use their explicit Gaussian/polynomial formulas on the
declared time guards. For P use the paid analytic saddle branch on the
larger transverse buffer in Notes45/54. Small pure complex x or y
disks, of radius1/64, lie inside those buffers wherever P is active.
The compact exterior guards use the inherited strict rectangle margins
and |B_s|>=1/2. At the all-height late branch, Note54 A's full-strip
holomorphy and determinant floor supply these disks, including the
conjugate branches glued at height zero. The real saddle at height zero
need not lie in the strict imaginary interior of its half-rectangle.
On such disks take the explicit EV59 Section3 bound on log Gamma,
the rectangle cap on p, the determinant floor and the finite jet
recurrences. Exponentiating their positive absolute sum bounds P
and its fixed t/spatial jets by a finite M. Cauchy gives
|partial_i^r leaf|<=M 64^r r!, hence PC2. This is a coarse bound,
not a new unknown supremum. The slow old gamma formula may still
serve to define a coarse M at tolerance1/4; it is not used as the
variable-accuracy value provider.

Use the original overlapping guards to omit undefined inactive N or P.
The flat extensions are globally smooth; their derivatives are products
of the stated analytic leaves and PC3 profiles, not derivatives of a
proof-case indicator. Translated cutoffs involving |x| are constant near
zero and flat at their actual joins. Finite one-sided caps therefore
give the same global derivative bounds there. The fixed time rows of
the moving cutoff retain X', widths and every temporal addend.

Propagate the PC2 rules through **every** EV59 raw scalar circuit and
its interior polynomial kernel factor. This gives explicit common
V,A>=1 for all those integrands, independent of requested accuracy.
Positive denominator floors are EV14 or stronger already paid local
floors. For a time box contained in t<=64 one may use the stronger
actual time-only floor min(1,e_base)^2; the unused e_plus in EV14 need
not impose a spurious quadratic-height loss in that regime.

## 3. Efficient normalized log-Gamma and fixed gamma jets

The actual gamma inputs are log Gamma and its fixed derivatives at
Re z>1. For target delta=2^-P, orders0<=j<=J, put

    m=N=P+J+ceil(log_2(J!))+8,
    T_m(w)=(w-1/2)Log w-w+(1/2)log(2pi)
           +sum_(k=1)^(m-1) B_(2k)/[2k(2k-1)w^(2k-1)],
    g(z)=T_m(z+N)-sum_(a=0)^(N-1)Log(z+a).          (PC4)

The [gamma recurrence](https://dlmf.nist.gov/5.5.E1) preserves the
right-half-plane normalized analytic log Gamma exactly. It never
reduces the final gamma value to a principal argument. From
[DLMF's sectorial Stirling remainder](https://dlmf.nist.gov/5.11#ii),
and the [Bernoulli--zeta identity](https://dlmf.nist.gov/25.6.E2),
|B_(2m)|<=4(2m)!/6^(2m). On |zeta-z|<=1/2 we have
Re(zeta+N)>m and sec^2(arg(zeta+N)/2)<=2. Consequently

    |R_m(zeta+N)|<=(2/9)^m/m<2^(-2m),
    |(log Gamma-g)^(j)(z)|<=j!2^j2^(-2m)<2^(-P-4). (PC5)

For example the first inequality follows by replacing (2m-2)! with
(2m)^(2m-2); the second is Cauchy on radius1/2. Differentiating the
**analytic remainder** pays fixed polygamma jets without differentiating
an asymptotic allowance.

Elementary complex logarithms also have polynomial precision cost.
For rational w=x+iy with x>0, use
Log w=(1/2)log(x^2+y^2)+i arg w. Binary-scale the positive modulus
square to 2^h s, 1<=s<2; the log s atanh ratio is <=1/3. For the
argument, invert |y|/x when it exceeds1 and use pi/2 minus arctan.
For 0<=u<=1 the identity

    arctan u=arctan(1/2)+arctan[(u-1/2)/(1+u/2)]

has both Taylor arguments of modulus <=1/2. Machin pi and log 2
are supplied as in Note60. All remaining series are geometrically
convergent at fixed ratios. This avoids a log series whose convergence
rate degenerates with imaginary height.

There is no Bernoulli-coefficient oracle: b_n=(n+1)!B_n are integers
given by b_0=1 and

    b_n=-sum_(j<n) binom(n+1,j) [n!/(j+1)!] b_j.

For rational input length I_z, |z|<=A_z, choose

    L=P+ceil log_2[32(A_z+2m+2)]+4,
    H=I_z+L+m+J+ceil log_2(A_z+m+4)+32.

Compute and round each elementary log with total complex error
<=2^(-L) on the common L-bit grid; assemble the remaining
rational jet expressions exactly and round outputs once to P+4
fractional bits. For nonrational saddle data first round the input
with the EV10/EV15 displacement debit, requesting one extra fixed
gamma derivative if needed for its explicit Lipschitz cap. The sum of
absolute coefficients of these logs is <=A_z+2m+2 in the value row,
<=1 in the first derivative; higher rows use only rational powers.
This pays a separate arithmetic reserve. Explicit factorial/power
common denominators, or polynomial-length rounded arithmetic with
that reserve, give the conservative bounds

    C_gamma<=2^(100(J+1)) H^10,
    S_gamma<=2^(20(J+1)) H^3.                         (PC6)

For fixed J this is polynomial in P,I_z,log A_z, replacing EV9's
1/delta-length product. The claim concerns log Gamma/psi/polygamma.
An absolute-error Gamma value on the positive axis can itself require
O(A_z log A_z) output bits. Subsequent exp(log S), magnitudes and
cancellation retain their independent EV15 payments. No uniform cheap
gamma-value oracle has been inferred from PC6.

## 4. A rational high-order continuous filter rule

For degree n>=1, let t_j=-1+2j/n, j=0,...,n, and let ell_j be the
Lagrange polynomials on these rational nodes. For t in[-1,1],

    sum_j|ell_j(t)|<=sum_j n^n/[j!(n-j)!]
                    =2^n n^n/n!<6^n.               (PC7)

Define exact rational weights w_j=integral_(-1)^1 ell_j(t)dt.
They integrate degree-n polynomials exactly and sum to2. They need
not all be positive: their full absolute amplification is paid below.
Use M equal panels per axis on[-1,1] and the scaled rule on each.

Let r=n+1. Taylor's degree-n polynomial at a panel center has remainder
at most V(A/M)^r(r!)^2 by PC2. Interpolation costs at most the factor
1+6^n. Tensor splitting I_x I_y-Q_x Q_y gives, on the whole square,

    |integral f-Q_x Q_y f|
      <=4(1+6^n)^2 V(A/M)^r(r!)^2.                  (PC8)

Only pure x derivatives for the first error and pure y derivatives
for the second are used. The norm of the composite one-dimensional
rule is <=2*6^n, so the tensor norm is <=4*36^n.

For an elementary raw-filter target e<=1, choose safe integer upper
bounds in

    n=max(1,ceil log_2(64V/e)),
    M=max(1,ceil[2^16 A(n+1)^2]),
    N_nodes=[M(n+1)]^2.                              (PC9)

Using r!<=r^r, PC8 is <=V2^(-10n-12)<e/16. Hence

    N_nodes<=2^34 A^2(n+1)^6.                        (PC10)

For fixed V,A this is polynomial in log(1/e), replacing the old
M_q^2=O(L_*^2/e^2) sufficient count. No height cutoff, changed
kernel or sample-based integration certificate is introduced.

### 4a. Boundary representatives, node error and exact summation

K is still k(u)k(v), k=(315/256)(1-u^2)^4 on[-1,1], zero outside.
For each retained weak K derivative through4, use its **interior
polynomial trace** at endpoint nodes. Endpoint representative values
do not affect the continuous weak integral. PC2 then applies on the
closed offset square. No fifth weak derivative of the zero extension
is assumed. The high interpolation order differentiates the interior
polynomial raw integrand for a remainder bound, not the weak kernel.

Evaluate every full integrand at its rational nodes with absolute error

    eta_node<=e 2^(-6n-10).                          (PC11)

The tensor weight norm makes the total node contribution <e/256.
Run EV15 with this target and retain its magnitude and floor reserves.
Compared with e itself, this asks for only O(n) additional accuracy
bits. It pays signed interpolation weights explicitly.

The canonical weights can share denominator

    W=2^n n!(n+1)!.

To see this, form numerator polynomials
product_(m!=j)[nt-(2m-n)] and denominator
2^n(-1)^(n-j)j!(n-j)!, then integrate monomials. Every monomial
denominator divides (n+1)! and j!(n-j)! divides n!. Their coefficients
and weights have O(n log(n+1)) bits. Form all weights with polynomial
integer work. If node values are rounded to a common 2^-B grid, the
full mapped tensor sum has common denominator

    2^B M^2 W^2.                                    (PC12)

Do not multiply one independent denominator per node. Stream exact
integer numerators, accumulate with the displayed common denominator,
and round the final division with error <=e/16. Its storage is
O(B+log M+n log(n+1)+log(2+V)+log N_nodes+n), apart from the
separate source/provider workspace. Together PC8--PC12 give raw
continuous-filter error <e with slack, uniformly between nodes and
across the smooth field seams.

## 5. Efficient flat functions and the other providers

Apply the one-dimensional version of PC7--PC12 to phi on[0,1],
with V=1,A=64. Requested integral error delta=2^-P uses
O((P+1)^3) nodes. The same rule, affinely restricted to[0,s],
constructs a partial integral; no unknown smoothness constant depends
on the interval endpoint. Keep the normalizer floor N_phi>2^-11.
Value ratios and fixed-order derivative jets are evaluated with their
separate numerator and normalizer error debits, as in EV12.

At rational interior s, v=1/[s(1-s)] is rational. For requested
leaf error tau=2^-B, if v>=B+2, return zero for phi; exp(-v)<tau
since e>2. Otherwise v=O(B), so ordinary exponential Taylor and
dyadic argument rounding have polynomial precision cost. For all
derivatives through the fixed order J, a fully rational safe tail test is

    v>=max(16J^2,2[B+J+ceil log_2(J!)+2]).            (PC13)

It dominates EV12's natural-log tail cutoff. On the complementary
region Bell/rational derivative factors have polynomial size in B;
their logarithmic magnitudes and required working bits are polynomial
as well. Endpoint values are returned exactly. Partial-integral tails
include the normalizer factor; near1 use one minus the reflected tail.
This treats endpoint equality and extremely small encoded distances
without unbounded inverse-distance work. The physical switch made
from exp(-1/s) has the same mechanism and its paid denominator floor.

Apart from separately charged external scalar inputs, the other finite
providers have polynomial accuracy-bit cost at fixed descriptor/Q:

* G retains EV5--EV8: with fixed U,m,beta and a fixed query box,
  D_e,B,K_e are O(P+1). Its sufficient bit cost is polynomial of
  degree11, with the explicit source cancellation debit retained.
* The full complex saddle uses EV10's contraction with factor<=1/2.
  There are O(P+1) inexact iterations, now using PC6. The finite
  implicit jet recurrence still divides by the paid determinant floor.
* The fixed-index moving phase inverse halves its bracket in O(P+1)
  steps. Each step uses the preceding saddle and unwrapped logarithm;
  neither endpoint equality nor a zero residual prevents contraction.
* The physical real source saddle has fixed contraction factor <1 on
  Q; its iteration count is O_Q(P+1). Its scalar formulas and jets use
  the same efficient elementary log/exp arithmetic.
* The fixed source constant Phi(0) has a geometrically bounded complete
  mode tail. Taking P+20 modes is a crude sufficient choice; the
  n^4 exp(-pi n^2) tail decreases faster than 2^-n there. All retained
  exponential arguments have polynomial magnitude in P. Thus this
  constant also needs no exponential-length precision provider. Indeed
  each source summand at0 has modulus <=64n^4 exp(-3n^2). Since
  n^4<=24exp(n), for n>=4 this is <2^(11-2n^2)<=2^(-n-4).
  Summing gives a tail <2^(-N-4) after N>=4 modes, so P+20
  is ample; pi/exponential input errors have separate dyadic debits.

Elementary exp and sin/cos may use the original factorial Taylor
algorithm, after fixed-box magnitude/argument bounds and rounding.
Its length is O_Q(P+1) for bounded arguments. The Phi(0) mode
provider is a polynomial exception: O(P) modes have arguments O(P^2),
so their factorial series may need O(P^2+P) terms. Both cases have
polynomial bit cost; no fast large-argument range reduction is needed
for this fixed-box theorem. Integer output magnitude
and query reading costs remain. Each finite provider hierarchy is
acyclic. Fixed-order jet-ring operations have a fixed finite size.

For clarity, for the explicit scalar encodings of PC1 all point
providers can be bounded by

    C_point(P,I)<=C_Q(1+P+I)^20,
    S_point(P,I)<=C_Q(1+P+I)^8.                      (PC14)

The generous exponent20 covers source11, gamma10, and two nested
linear iteration counts for phase inversion (degree12). An exp leaf
with argument O(P) uses O(P) terms and O((P+I)^2) operand bits,
so the O(P^3) profile integration fits degree8. The O(P) Phi(0)
modes with O(P^2) terms and O((P+I)^3) operand bits fit degree9.
Common-grid rounding and exact common denominators prevent additional
per-node denominator growth. These all fit under degree20. Constants include the
actual fixed jet order, encoded descriptor and every fixed magnitude.
General external scalar costs multiply this bound as specified in
Section1. This is not a claim of a universal polynomial in the
descriptor length.

## 6. Complete tuple, arithmetic and coordinate errors

Use **all** EV59 Section7 circuits, including rho_t evaluated directly,
both total-curvature time rows, current derivatives, each component/
spatial/moving/temporal E and B addend, actual mathcal S, heat-potential
correction, traces, and the signed stress/covariance recombination.
No raw term is deleted to obtain PC1.

Apply the same finite post-filter circuit as EV18--EV19. Its caps and
A_post are fixed before e. For final target zeta choose the original
e=min(1,zeta/(16A_post),zeta/[2^20(1+M_mean)^2]). Thus
log_2(1/e)=log_2(1/zeta)+O_(descriptor,Q)(1).
Compute actual full mean products, not component covariances or a
separately positive squared-gradient integral. Equation sums retain
their component allocations. PC11's node accuracy is passed through
EV15 to every elementary provider; no special function is unit cost.

Let p=ceil log_2(1/zeta). Then n=O_Q(p+1), M=O_Q((p+1)^2),
node count O_Q((p+1)^6), and every required provider accuracy has
O_Q(p+1) bits. Rational node encoding length is
I+O(log M+log(n+1)), and exact weights/summation have polynomial
bit length by PC12. External scalar calls retain Section1's separate
cost; the following degree count concerns the explicit encodings. Substituting PC14 in PC10 gives a degree26
sufficient dominant product; degree40 in PC1 leaves room for all
weight construction, rounding, input reading and post-filter sums.
Streaming nodes gives the displayed polynomial storage bound.

For supplied coordinate balls retain EV59's one-unit slack and its
explicit derivative/error recursion, including the extra time jet.
Its displacement constant is fixed on Q, so requiring coordinate
radius O_Q(zeta) costs p+O_Q(1) bits and does not change PC1.
Those moduli may have very poor inverse-q constants. No better
coordinate-height dependence is inferred from this argument.

The mathematical source approximation remains <=theta_r/2. Choosing
the original zeta(t,x)=theta/[4(1+t^2)(1+x^2)] leaves the total
<=3theta_r/4 for every retained scalar with its own allocation. Both
infinite-time and height-end error limits are retained. The algorithm
works at boxes throughout the entire time/height domain, with constants
depending on the box; one uniform finite cost over the domain is not
asserted. Constructing the source or descriptor, if not already stored,
adds Notes58/60's separate finite costs.

## 7. What still prevents a useful uniform height bound

PC2's inverse gate contains V/d, and EV14 still has a Gaussian positive-
time regulator floor. Consequently A, and therefore M, can be
exponential in height squared. The gain is polynomial dependence on
**additional accuracy bits at a fixed box**, not removal of that
height dependence. The generic local inputs alone do not justify a
polynomial-height pointwise density cap: locally F=a(z-c), with q
approximately constant, gives

    rho(c)=|a|^2/(pi q)=1/(pi delta^2),
    delta=sqrt(q)/|a|.                               (PC15)

The narrow peak is real. This local model explains why replacing a
single Lipschitz constant does not pay the height cost. It is not a
lower bound for every integration algorithm, a theta counterexample
or a universal obstruction to weak/carrier-aware methods.

## 8. A paid weak-primitive puncture estimate and its unpaid consumer

The appropriate cancellation precedes quadrature. Reuse
[Note31 PE22/24--26/34](31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md)
and Note47 GS9/GS12. On holomorphic regions, writing
w=q/(|F|^2+q), chi=w(1-w), define

    V_m=(F_zz/F)(1-w)w^m,
    Z_m=(E/F)(1-w)w^m.

At zeros these mean their smooth fractions
V_m=w^m F_zz conjugate(F)/D and Z_m=w^m E conjugate(F)/D,
D=|F|^2+q, rather than undefined quotients.

The exact time identities include

    S_t=-2Re V_0+r_t w+2Re Z_0,
    w_t=r_t chi+2Re V_1-2Re Z_1,
    chi_t=(1-2w)w_t.                                 (PC16)

Here r=log q, consistently with these inherited formulas. They retain
actual E and its separate addends. Density/current and direct density-
time can be paired weakly with K derivatives; actual covariance uses
the signed GS9 stress and the actual full filtered mean products.
Nonholomorphic bands need their exact B terms and zero-free band
payment; they are not covered by asserting holomorphy there.

Suppose a paid simple-root collar has F=(z-a)b, |b|>=s>0 and

    |F_zz/F|<=V_0*/|z-a|+G_0,
    |E/F|<=E_0*/|z-a|+G_E,
    q>=q_min>0, |F|<=F_max, q<=q_max.

For B_log=max(1,|log q_min|,|log(F_max^2+q_max)|), radius h inside
that collar, and every m>=0, direct polar integration gives

    integral_(|z-a|<h) |S| <=pi h^2 B_log,
    integral |V_m| <=2pi V_0* h+pi G_0 h^2,
    integral |Z_m| <=2pi E_0* h+pi G_E h^2.          (PC17)

Bounded w,chi polynomials cost their bound times pi h^2. These bounds
use (1-w)w^m<=1 and contain **no inverse q_min**. Finite logarithmic
q dependence is explicit. Multiplying by each actual weak test sup
norm pays the omitted-disk error. With N collars and finite coefficient
cap C, choosing h<=e/[C N(1+B_log)] (and the paid collar radius)
makes their total error <=e after enlarging C for displaced disk guards.
This is a proved lemma, not an executed collar calculation.

One must not apply PC17 by deleting disks from the original raw rho,
j or D_E circuits. Density carries finite mass in a shrinking disk;
signed heat terms can contain dipoles. First derive the exact weak
primitive representation, including every joining-test commutator.

The **first remaining complete height-cost payment** is a constructive
full-inventory weak-filter theorem consuming PC17: enumerate and guard
every intersecting actual collar; bound the retained integrands and
their normalized providers away from punctures; replace pointwise
EV19 post-filter caps by primitive L1 caps and the actual mean bounds;
and retain every band/temporal defect and kernel-order allocation.
For optional coordinate balls, add explicit highest-kernel boundary
trace and time moduli. Differentiating a fourth kernel derivative can
produce boundary line measures; the old pointwise L_final would
reintroduce the inverse-floor loss. Those moduli are not paid by PC17.

In particular, neither PC17 alone nor a better gamma algorithm proves
the desired complete polynomial-height theorem. The known simple-root
phase clocks and zero-free bands give a specific route, rather than an
unnamed assertion that weak cancellation should help.

## 9. Status, controls and records

**PC1 is proved in-note at fixed-descriptor/fixed-query-box scope for
its explicit scalar encodings; external scalar-provider costs are retained
in the general bound.** The full evaluator/filter improves from finite
potentially exponential accuracy-bit work to a polynomial bound for
those encodings, or a polynomial overhead on external scalar costs.
Uniform useful height/time/descriptor cost and executed acceptance remain open.
The next precise estimate is Section8's complete weak-filter consumer.

These algorithms and smoothness bounds also apply to smooth colliding
controls with their own data. That is required: they assert no favorable
sign. The full IC23 application uses the complete canonical theta
source/completion. Euler-factor controls alter that identity; weighted-
square/finite-prime controls lack full coefficients/reflection; reflected,
shape and primitive controls lack the canonical source identity; atomic
and heat-polynomial controls lack the smooth complete source. These
premise checks do not claim the numerical algorithms exclude collisions.

**HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled** remain. The
[internal assessment](../reviews/40_COMPLETE_EVALUATOR_COST_ASSESSMENT_20261025.md)
is same-model, not independent full-chain validation. No numerical,
exact-rational or machine-symbolic research runs, coefficients, field/
gamma/phase samples or interval campaigns were performed. All algorithms
and costs were derived on paper. Housekeeping hashes/links/history are
not mathematical certificates. See the [zero-run record](../numerics/COMPLETE_EVALUATOR_COST_ANALYTICAL_WORK_RECORD_20261025.json)
and [whole-chat summary](62_CHAT0021_RESEARCH_SUMMARY_20261025.md).
Manuscript/DRAFT_HISTORY unchanged; no snapshot, commit or new chat.

**Next: Analysis — Sol**, the complete weak-primitive/carrier-aware
height-cost consumer above, retaining actual covariance and all defects.
