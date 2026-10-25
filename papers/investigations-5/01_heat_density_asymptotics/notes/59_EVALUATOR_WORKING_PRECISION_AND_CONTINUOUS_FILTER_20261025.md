# Working precision and continuous filtering of the positive-source tuple

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Chat **0021**, thread
`01a1751b-9ac5-7192-9f6c-b9f59ec30827`.

**Status: cancellation-safe source evaluator and finite full-tuple
arithmetic/filter error theorem proved in-note from certified fixed
descriptor data; upstream literal phase-index selection remains unpaid.**
No source coefficients or research computations were executed.

This continues [Note58](58_POSITIVE_ANALYTIC_SOURCE_COMPRESSION_20261025.md)
for the **unchanged** [Note55](55_FIXED_CENTRAL_CONDITIONING_AND_SOURCE_COST_20261025.md)
IC23 tuple. It supplies finite working-bit and continuous-integration
bounds, including the inherited nonsource providers, rather than treating
source storage as evaluation precision. It proves no affordable runtime,
uniform cost over unbounded queries, or polynomial evaluated-filter cost.
The exact phase integer n is part of the fixed input descriptor. Section9
states the first unpaid step in constructing that descriptor from scratch.
HDA-17 **Partial**, HDA-18 **Gated**, HDA-20 **unfulfilled** remain.

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
This is quantitative evaluation/error analysis, not an RH criterion or
collision exclusion. [Manifest59](59_EVALUATOR_FILTER_INPUTS_20261025.json)
pins opening sources; [Review38](../reviews/38_EVALUATOR_FILTER_LEDGER_ASSESSMENT_20261025.md)
is same-model internal assessment, not the distinct full-chain audit.

## 1. Fixed mathematical tuple and evaluation contract

Retain Note54's exact field table, Note55 IC23, Note58's one fixed
nonnegative source f=p^2 on [0,U], physical q=epsilon_g^2, K=k_1 k_1,
unnormalized observables, actual covariance and every joining defect.
The source-to-H theorem remains only the four errors j<=3 on strip4:

    |partial_z^j(G-H)|<=51epsilon/256, t<=b.            (EV1)

Higher jets below evaluate that same G; they do not assert more
source-to-H accuracy. No new field or tolerance policy is substituted.

A fixed certified descriptor contains the exact dyadic source data,
integers U,m,beta, the already selected phase integer n, encoded eta>0
with a certified positive lower bound, thresholds T_-,T_+, b=T_++1,
the width and onset data and branch/guard margins of Notes54--55.
The phase integer uses EV11's normalized unwrapped lift, or includes
its exact integer translation to that lift in the descriptor.
Computable fixed scalar data include approximation routines and costs;
an arbitrary unspecified noncomputable real is not an algorithm input.
As in AC18, constructing upstream discrete recipe choices is separate.

The evaluator acts at rational queries (t,x,y), |y|<=1, or on supplied
coordinate balls with the displacement debits below. Its parameters
are explicit on every local query box. Such boxes can be placed at
**every real height and time**; there is no finite height cutoff or
substitution of samples for a uniform integration remainder. Cost is
allowed to depend on the query and the encoded fixed parameters.

An essential scope point: G is active at every real x during
[-2T_-,-T_-], [-T_-,63], and the initial switch [63,64]. Only its
later moving-core use is spatially bounded. The source-active time
interval is contained in [-2T_-,b], but its spatial domain is unbounded.

Let theta_r>0 denote the preassigned scalar comparison targets, including
trace and equation-sum targets where they are required separately. For
the finite retained list, put theta=min(1,min_r theta_r). A sufficient
additional absolute evaluation allowance, declared before any run, is

    zeta(t,x)=theta/[4(1+t^2)(1+x^2)].                 (EV2)

Using a certified smaller rational allowance is harmless. It is <=theta/4,
vanishes uniformly in x as t tends to either infinite endpoint, and
vanishes in either height direction at fixed t. Thus numerical errors
do not destroy the inherited endpoint limits. This schedule changes
neither the fixed source nor the physical density normalization.

## 2. Entire moment series: no unstable erf recurrence is required

After exact Note58 conversion, write

    f(u)=sum_(k=0..2m-2) d_k(u/U)^k,
    D_f=sum_k |d_k| <=16*49^m <2^(6m+4),
    0<=f(u)<100 on [0,U].                             (EV3)

The coefficient l1 cap follows by squaring ||p||_1<4*7^m; the
pointwise cap follows from AC15. They serve different error consumers.
Define a=tU^2, c_+=izU, c_-=-izU, and

    M_k(a,c)=sum_(r,s>=0) a^r c^s/[r!s!(k+2r+s+1)].

This is the absolutely convergent integral of the exponential series.
For 2h+j<=J,

    partial_t^h partial_z^j G
      =U^(2h+j+1)/2 sum_k d_k
         [i^j M_(k+2h+j)(a,c_+)
                    +(-i)^j M_(k+2h+j)(a,c_-)].       (EV4)

No division by a or c occurs. This evaluates AC20 itself, including
all t=0,z=0 neighborhoods, without assuming stability of AC21's erf
or forward moment recurrence. J=8 suffices for the generous real-jet
inventory below and its coordinate moduli; any fixed larger J is allowed.

Take active times -tau<=t<=b, tau=2T_-, source evaluation tolerance
0<nu<=1, and a queried rectangle |x|<=X, |y|<=Y with Y<=4. Allow
one unit of coordinate slack. Put s_b=max(0,b) and

    A=(tau+s_b+2)U^2+U(X+Y+2), T=ceil A,
    p=ceil log2[4*2^(6m+4)U^(J+1)/nu],
    N_e=8(T+1)+p, D_e=N_e-1.                          (EV5)

Truncate EV4's joint sums at r+s<=D_e. With N=N_e,

    exponential remainder <=exp(A) A^N/N!
          <=2^(2A-N)<=2^-p.

Indeed N!>=(N/e)^N, e<3 and N>=8A give
(eA/N)^N<=2^-N, while exp A<=2^(2A). Multiplication by EV3 and
the largest derivative prefactor pays <=nu/4 for each requested jet.
This explicitly pays high-degree coefficient cancellation.

Coordinate errors have a better bound than D_f. Every next real
t,x,y derivative of a requested jet is bounded, on its displacement
segment, by

    V_J=100 U^(J+3) exp[(s_b+1)U^2+(Y+1)U].

Thus coordinates known within 2^-B each, where

    B>=max(0,ceil log2(12V_J/nu)),                     (EV6)

contribute at most nu/4. Exact dyadic query coordinates need no
coordinate debit. General rational coordinates are first rounded under
EV6, or their exact common denominator replaces 2^B and its bit length
is paid. EV7 uses the dyadic-rounded version.

The series also gives an explicit **working-bit** implementation.
Let rounded coordinates share denominator 2^B and set

    H_e=2m+J+2D_e+2,
    Q_e=2^(2beta+B D_e+1) D_e! H_e!,
    p_out=ceil log2(8/nu).

Every series term can be put on the common denominator Q_e:
D_e!/(r!s!) and H_e!/(k+2h+j+2r+s+1) are integers. Generate powers
of the Gaussian-integer numerators of a,c, assemble terms and sum
exactly, then round the complex output once to p_out fractional bits.
The last rounding costs <=nu/4. All three debits total <=3nu/4<nu.

For a finite explicit operand cap let

    ell_e=ceil log2(U+T+D_e+H_e+m+beta+B+p_out+J+8),
    L_e=64[2beta+B(D_e+1)+(D_e+H_e+J+4)ell_e
                              +6m+2T+p_out+16],
    K_e=2+U+m+beta+B+D_e+J+T+p_out.                   (EV7)

Every denominator, power, scaled numerator, absolute partial sum,
derivative prefactor and rounding division fits L_e bits. For example
log2 Q_e<=2beta+B D_e+1+D_e log2 D_e+H_e log2 H_e;
numerator powers cost at most D_e(B+log2(T+1)+3), and the absolute
series sum contributes at most log2 D_f+2T+(J+1)log2 U+4.
These terms are covered by EV7. Precomputed powers/factorials give
the conservative bounds

    operations <=2^20 K_e^5, operand bits <=2^20 K_e^3,
    schoolbook bit operations <=2^100 K_e^11.          (EV8)

There are O(m D_e^2) terms; even naive powers, factorial scaling and
term assembly fit the displayed operation bound. No floating mantissa
or cancellation assumption is hidden here. These bounds can be very
large and grow with the queried height X. They are not a theorem
about the efficiency of AC21 or an affordable evaluation crossover.
If rational query encoding length is I_in, add its reading/rounding
cost <=2^20(I_in+B+1)^2 bit operations and storage I_in+B before
EV8. A long input denominator is not discarded.

## 3. Finite nonsource providers, without special-function oracles

The following deliberately coarse algorithms pay value/finite-jet
evaluation for a **fixed certified descriptor**. Their error budgets
will be chosen by the finite circuit in Section5. They need not be
efficient. Rounding elementary outputs to specified dyadic grids before
long sums avoids uncontrolled common-denominator growth.

### 3a. Gamma, unwrapped logarithms and the complex saddle

On Re v>0, |v|<=A_v, Euler's product gives

    L_N(v)=-Log v-gamma_N v
              +sum_(k=1..N)[v/k-Log(1+v/k)],
    gamma_N=sum_(k=1..N) 1/k-log N.

For N>=2A_v the explicit errors are

    |log Gamma(v)-L_N(v)| <=(A_v^2+A_v)/N,
    first derivative error <=(A_v+1)/N,
    derivative r>=2 error <=(r-2)! N^(1-r).           (EV9)

Use |gamma-gamma_N|<=1/N, |z-Log(1+z)|<=|z|^2 for
|z|<=1/2 and |k+v|>=k. The derivative tails follow by integrating
k^-r. The branch is analytic in the right half-plane and real at
positive v, normalized by log Gamma(1)=0. It supplies the unwrapped
logarithm, not a principal argument of the final small carrier.
The primary identities are [DLMF5.8.2](https://dlmf.nist.gov/5.8.E2)
and [DLMF5.7.6](https://dlmf.nist.gov/5.7.E6); the finite tail bounds
above are derived here from them.

For any finite derivative order r_0 and requested error delta, a safe
cutoff is

    N_G=ceil[2A_v+4(r_0!+1)(1+A_v)^2/delta].

Compute the finite sum and elementary logarithms to leave a separate
delta/2 arithmetic reserve. One possible elementary log algorithm is
Log z=2sum_(j>=0) w^(2j+1)/(2j+1), w=(z-1)/(z+1).
For Re z>=d>0 and |z|<=H, choose
sigma=min(1/2,2d/(H+1)^2). Then |w|<=1-sigma. Degree
M>=log[8/(delta sigma)]/(2sigma) gives remainder <=delta/4.
The positive-real logarithms are a special case. Exponentials use the
ordinary factorial Taylor remainder as in EV5; square roots use positive
bisection or exp(Log/2) on the right-half-plane branch. All finite
term arithmetic is given separate dyadic errors. In particular N_G
can be exponential in requested precision bits: this is an explicit
finite provider, not an efficient gamma algorithm.

For the exact model use Note30 FS3:

    alpha(p)=1/p+1/(p-1)-(log pi)/2+psi(p/2)/2,
    p=w+t alpha(p)/2, B_s=1-t alpha'(p)/2.

Note45 EF4--EF6 and Note54 A/C1 give the actual active contraction
rectangles, factor <=1/2 and |B_s|>=1/2. Let D_rect be a finite
explicit rectangle diameter. Inexact fixed-point iteration, projected
onto a rational closed rectangle with the same paid contraction bounds
if needed (choose its endpoints using the strict inherited margins), with per-step vector error eta_it,
obeys

    |p_k-p|<=2^-k D_rect+2eta_it.                    (EV10)

Choose k>=ceil log2(4D_rect/delta), eta_it<=delta/8, and pay final
rounding separately. The finite gamma provider supplies alpha. Write
the actual arm logarithm as

    log S=Log p+Log(p-1)-(p/2)log pi+log Gamma(p/2)
          -log16-(p-w)^2/t-Log B_s/2.                (EV11)

Here t>=63 wherever this model is active, and B_s has its branch
near1. Taking Im log S on the real axis gives the same continuous
phase lift as the inherited tuple. No phase reduction of S is used.

All required finite jets are obtained in the truncated real Taylor
ring in t,x,y. In each positive-degree coefficient of
p-w-t alpha(p)/2=0, the unknown highest p coefficient is multiplied
by B_s; solve for it using known lower-degree coefficients. Model
jets then follow by finite series products, reciprocal and exponential
rules. This is an explicit finite recurrence, not a differentiation
of an asymptotic error. Evaluation error is propagated by Section5.

For completeness the input magnitude/derivative caps can also be
generated without unknown suprema. The paid rectangles give a finite
A_p>=|p| and Re p>=2. On Re v>=1, |v|<=A_v,
|psi(v)|<=2+2A_v and |psi^(j)(v)|<=2j!, j>=1, directly from its
series; hence conservative alpha jet caps are 8(1+A_p) and 4j!.
A coarse value cap for log Gamma uses EV9 at delta=1/4 and the finite
right-half-plane log bounds |Log z|<=|z|+1/Re z+4. For that fixed
coarse cutoff N_0, 8(N_0+1)(A_v+1) bounds |log Gamma(v)|.
Substitute this in EV11, bound |p-w| by A_p+|w| and 1/t by1/63,
and exponentiate to bound each arm. Positive versions of the finite
jet recurrences supply every further magnitude cap. These caps may
be extremely wasteful, but are explicit before the requested tolerance
is chosen, so the precision construction is not circular.

### 3b. Moving phase, physical regulator and flat functions

With the **given exact phase integer n**, use the inherited real
bracket for X(t). One safe enlargement is
[U_0-Dmov_b,U_0+64+Dmov_b], since Theta_x>=1/8 and pi<4 imply
X(64)<=U_0+32. Here U_0=2^k is the spatial onset, distinct from the
source cutoff U. The entire bracket is in the paid exterior branch.

A monotone inverse needs no root-equality test. On an interval of width
w with Theta_x>=c, evaluate Theta(mid)-npi with error <=cw/16.
If its sign is certified, retain the appropriate half. Otherwise the
true residual has modulus <=cw/8, so retain the interval of radius
w/8 around mid. The root is contained and each step shrinks width by
at least one half. Thus ceil log2(W_0/delta)+1 steps suffice.
The velocity is exactly X'=-Theta_t/Theta_x; its denominator has the
paid floor, and higher finite t jets needed for coordinate moduli follow
by the same implicit-coefficient recurrence. This does not choose n.

For the physical real source saddle, on [63,B_q] use the contraction

    L_s=(1/4)log[(2tL_s+9)/(4pi)],
    1/4<=L_s<=B_q+1,
    contraction factor <=rho_q=B_q/(B_q+18)<1.

The endpoint signs in Note54 C2 prove the interval is mapped into
itself; project rounded iterates onto [1/4,B_q+1] to keep the domain
invariant. A sufficient iteration count is
ceil[(B_q+18)/18 * log(4(B_q+1)/delta)], with local step error
<=(1-rho_q)delta/4. Compute
kappa=8tL_s-2t+36>=36, its derivatives, log M0 and then the exact
r=a(t)-beta_q(t)x^2 from SC1/FB2. Implicit derivatives divide only
by paid positive factors. For any finite late query choose B_q>=t+1;
no uniform positive-time runtime is inferred.

The canonical constant C=Phi(0)sqrt(pi)/2 in N and epsilon_b is
enclosed by the complete source-mode tail of Note44/AC12, with explicit
pi and positive-square-root arithmetic. It is not an additional oracle.

For b_*(s), let phi(s)=exp[-1/(s(1-s))] on (0,1), zero otherwise,
and N_phi=integral_0^1 phi. Note44 gives N_phi>=e^(-16/3)/2>2^-11.
An explicit global derivative cap is C_0=1 and, r>=1,

    ||phi^(r)||<=C_r=r!2^r(2r)^(2r),
    ||b_*^(r)||<=2^11 C_(r-1), r>=1.                (EV12)

Indeed v=1/s+1/(1-s) has |v^(j)|<=j!v^(j+1);
the finite exponential differentiation partitions give
|phi^(r)|<=r!2^r v^(2r)e^-v. Midpoint integration of phi with
M cells costs <=C_1/(4M)<=2/M for both its normalizer and a partial
integral. Errors <=eta<=2^-13 in each give ratio error <=2^13 eta.
Derivative values are phi^(r-1)/N_phi; input displacement is paid
by the next global derivative cap. This constructs all finite jets.

Tiny flat weights need no unbounded inverse-distance work. For the
finite maximum order r, if

    v>=max(16r^2,2log(r!2^r/delta)),

then all relevant derivative tails are <=delta, so return zero with
that error. On the remaining interior v is explicitly bounded in
terms of the requested accuracy, and its rational/exponential formula
is evaluated with its own debit. Near s=0 the partial integral is
<=exp(-1/s); use the reflected bound near1, returning the b_* value near one
as one minus its tail rather than zero. A clamped dyadic
approximation and EV12 pay inputs at or near endpoints without deciding
whether an unspecified exact real equals an endpoint.
The displayed delta is a phi-leaf tolerance. For requested b_* jet
error delta_profile, first use delta_phi<=2^-11 delta_profile and
pay the normalizer error by the same ratio circuit. Normalized
partial-integral endpoint tails include this factor as well.

The physical switch chi of FB2 is a different function. Put
a(s)=exp(-1/s) for s>0, zero otherwise; its denominator in
chi=a(s)/(a(s)+a(1-s)) is >=e^-2 on [0,1]. The same finite
derivative/tail argument and rational circuit evaluate its jets.
No log0 or undefined endpoint is inserted.

For compact pre-late times, use a rational guard inside the region
where lambda and its needed jets vanish, but above P's paid exterior
onset. The strict onset buffers allow such a guard below
U_0-Dmov_b-2. Skip P on its inner side. On its outer side P is
defined even if its coefficient happens to vanish. After T_+ the
all-height late branch is paid. This evaluates the flat-zero extension
without forming an undefined 0P. The negative Gaussian N is elementary. Rational overlapping time guards
can likewise skip N near t=0 and skip G beyond its bounded active time.
If G is evaluated harmlessly on such a guard overlap, enlarge tau,b in
EV5--EV7 and the s_b used in Section4's G-jet caps by that declared
finite overlap width, and recompute all derived circuit caps. This is
a bound for evaluation of exact G, not an extension of EV1's comparison
domain.

## 4. Input jets and explicit local denominator/magnitude caps

For the complete integrand list below it suffices to supply actual F
spatial jets through4 with one t derivative, and r spatial jets
through3 with one t derivative. One further t jet may be included
when paying coordinate uncertainty of a time row. The Section3 finite
jet recurrences provide these. The source requirement is covered by
J=8; again this is evaluation of fixed f, not a stronger IC23 premise.
Real spatial jets follow from holomorphic component jets and exact
cutoff product rules, retaining their nonholomorphic contributions.

For an actual blend F=(1-h)F0+hF1 of holomorphic components, evaluate
separately

    B=(1-h)B0+hB1+h_x(F1-F0)/2,
    E_component=(1-h)E0+hE1,
    E_temporal=h_t(F1-F0),
    E_spatial=h_x(F1-F0)_z+h_xx(F1-F0)/4.             (EV13)

For holomorphic components B0=B1=0. The E addends sum to
F_t+F_zz. The actual h_t includes the moving-gap
term, and nested blends are expanded by this same identity. Keep the
component, spatial, moving and temporal addends and their needed jets;
evaluating their sum does not authorize discarding any of them.

There is an explicit positive local q floor even when no global one
exists. For a query support plus coordinate slack set
X_q=|x|+3, T_q=|t|+2, B_q=max(97,ceil T_q),
K_q=8B_q(B_q+1)+36, and

    e_base=4eta exp(-4)/(1+T_q^2)^(1/4),
    e_plus=exp(-3)K_q^(-3/2)exp(-X_q^2/72),
    d_q=min(1,e_base,e_plus)^2.                       (EV14)

Note44's C bound pays e_base; Note54 C2's M0 and kappa bounds pay
e_plus wherever the positive regulator arm is used. Geometric
interpolation is at least the smaller arm. Thus q>=d_q on the full
queried support, at every real observation time/height. For t<=64
the unused e_plus only weakens the actual time-only floor. Set
D=|F|^2+q>=d_q. This floor is used for **evaluation error**, not to
replace IC23's improved analytical source comparison. It is never
asserted uniform on the entire height line after64.

Use EV3's cap
100U^(a+b+2c+1)exp(s_b U^2+4U) for G jets, Section3's explicit
jet caps for P, elementary caps for N, global profile derivative caps
scaled by sigma and time widths, and the exact Leibniz sums for F.
Use r=a-beta_q x^2 and its finite derivative recurrences for q,r jets.
All are finite positive expressions in the fixed descriptor and local
box parameters. They are supplied to the following mechanical cap
and error recursion, rather than unnamed compact suprema.

## 5. A compositional arithmetic and working-precision ledger

Split complex operations into real ones. For each input jet u provide
V_u>=|u|, L_u>=max(|u_t|,|u_x|,|u_y|) from Section4 and set A_u=1.
For each gate propagate the following positive expressions:

| Gate | V | L | A |
| --- | --- | --- | --- |
| u+v | V_u+V_v | L_u+L_v | A_u+A_v+1 |
| uv | V_u V_v | V_u L_v+V_v L_u | (V_u+1)A_v+(V_v+1)A_u+1 |
| 1/u, u>=d | 1/d | L_u/d^2 | 2A_u/d^2+1 |
| log u, u>=d | V_u+1/d | L_u/d | 2A_u/d+1 |
| exp u | exp V_u | exp(V_u)L_u | exp(V_u+1)A_u+1 |

Signs, conjugation and real/imaginary parts preserve or add these caps.
Complex inverses are evaluated through the real positive modulus
square, whose floor is supplied explicitly. A product bound includes
the input-error cross term once intermediate errors are <=1. The
inverse/log estimates use input error <=d/2. The +1 pays one absolute
elementary or rounding error per gate. By induction A_u tau bounds
the total gate error when every input and gate debit is <=tau.

For the finite retained integrand circuits, let V_*,L_*,A_* be their
respective maxima over all internal gates, including the polynomial
kernel factors of Section6,
and d_*=min(1,all inverse/log floors). These are maxima of a finite
list of explicit expressions, with no unknown optimization. For desired
elementary filtered-term error e<=1 choose

    tau=min(e/(64A_*),1/(2A_*),d_*/(4A_*)),
    p_arith=ceil log2(1/tau)+2.                        (EV15)

Then every integrand evaluation has error <=e/64 and all denominator
and induction gates hold. Ordinary scalar storage additionally needs
ceil log2(2+V_*) integer bits. Each provider must itself be run at
output tolerance tau, using EV5--EV10 and EV12; p_arith is not a
substitute for its internal working bits or cost. The same recursion
applied to finite jet/provider formulas supplies their required leaf
tolerances and rounding accuracy. This terminates in exact source
integers and the explicitly bounded elementary series above.

## 6. Continuous K integration with a uniform remainder

The unchanged kernel is

    k(v)=(315/256)(1-v^2)^4 1_(|v|<=1), K(u,v)=k(u)k(v).

On the interior [-1,1] a cap for its i-th derivative, i<=5, is

    kappa_i=(315/256)sum_(0<=j<=4,2j>=i)
                         binom(4,j)(2j)!/(2j-i)! .    (EV16)

Use products of these caps for K_alpha and its first interior offset
derivatives. The fifth derivative here is an **interior quadrature
derivative**, not an assertion that the extended kernel has a bounded
fifth weak derivative. The fixed support boundary has area zero;
midpoints avoid it. Every weak derivative in the actual tuple still
uses K only through order4.

Write every convolution over the full offset square [-1,1]^2. For a
raw integrand K_alpha(u,v)Psi(t,x-u,y-v), the positive rule gives
an explicit first-derivative bound from V_Psi,L_Psi and EV16.
Use the common resulting L_* in

    M_q=max(1,ceil(64L_*/e)).                         (EV17)

Tensor composite midpoint with M_q cells per axis has error
<=4L_*/M_q<=e/16: on each cell use its two-coordinate Lipschitz
bound and integrate distance from the midpoint. The estimate holds
between nodes and across all globally smooth field seams. It introduces
no derivative of a proof-case indicator and no discarded joining term.
Node evaluation errors cost <=4(e/64)=e/16. Round node outputs to
a common dyadic grid and sum their numerators exactly; multiply by
the rational weight 4/M_q^2. Round the final division with error
<=e/8. Thus each raw continuous filter has error <e, with slack.

The exact node-sum storage can be bounded by
p_arith+ceil log2[M_q^2(1+V_*)]+3 bits, before its final rational
division. Higher internal source/provider precision remains as stated
in their separate algorithms. All time rows below are direct spatial
integrals; no time quadrature or time-differenced derivative is used.

## 7. Full scalar inventory, signed covariance and component errors

For each indicated multi-index integrate the following exact circuits:

| Raw quantity Psi | Kernel orders |
| --- | --- |
| S=log D, w=q/D | through4 |
| rho, direct rho_t, S_t, w_t | through2 |
| j=q F_zz conjugate(F_z)/(pi D^2) | through3 internally |
| C_reg,T_C,(C_reg)_t,(T_C)_t | through2 |
| b_reg w, actual mathcal S | through2 |
| V_0,c_r w,Xi | through2 |
| T_U=Xi/2+2Re Z | through4 |
| D_E,D_B,T_J and separate defect addends | through2, T_J through3 |

Use the **actual** GS7--GS12 definitions for B,E,F. For explicit time
arithmetic,

    D_t=2Re(F_t conjugate(F))+q_t,
    S_t=D_t/D, w_t=q_t/D-qD_t/D^2,
    rho_t=[q_t|a|^2+2q Re(a_t conjugate(a))]/(pi D^2)
                                           -2rho D_t/D, a=F_z.

Thus R_t is evaluated directly, not defined from its PDE. Because
r_y=0, the regulator curvature and its time derivative can be evaluated
as

    C_reg=(2w_x r_x+w r_xx-chi_reg r_x^2)/(4pi),
    (C_reg)_t=[2w_xt r_x+2w_x r_xt+w_t r_xx+w r_xxt
              -(chi_reg)_t r_x^2-2chi_reg r_x r_xt]/(4pi),
    chi_reg=w(1-w), (chi_reg)_t=(1-2w)w_t,
    w_xt=q_xt/D-(q_xD_t+q_tD_x+qD_xt)/D^2
                                               +2qD_xD_t/D^3.

Differentiate the exact GS8 T_C circuit by the product rule for its
time row. Both total-curvature derivatives remain in the density
equation. Actual mathcal S and D_E,D_B are evaluated by GS7/GS12,
with all component/spatial/moving/temporal pieces of E and E_z kept.
The heat-potential correction T_U, internal current derivatives and
fixed boundary/time traces use the same jet and kernel inventory.

For covariance first use the **signed** GS9 identity. For |alpha|<=2,
form

    P_alpha=4Re <K_alpha,V_0>
       -<(K_(alpha+xx)-K_(alpha+yy)),S>
       +<K_alpha,c_r w>+<K_alpha,Xi>,
    Q_alpha=P_alpha
       -sum_(i=x,y) s_i sum_(beta<=alpha) binom(alpha,beta)
                         U_(beta+i) U_(alpha-beta+i),
    s_x=1, s_y=-1.                                   (EV18)

These U derivatives are the **actual full filtered means**. No
component covariance or separate positive squared-gradient integral
is substituted. If each elementary filter and mean has error <=e<=1,
and actual mean derivatives through3 are <=M_mean>=1, then

    |error Q_alpha| <=(8+24M_mean)e<=32M_mean e.

A valid local mean cap is 1+4 max_(|gamma|<=3)(k_gamma V_S), from
the full support and Section5 caps; sharper already paid mean caps
may be used. The 24 includes the full Leibniz sums and product-error
terms. Delta Q is the sum of its two alpha=2 rows, with its own
component allocation. Signed cancellation is retained before taking
error bounds.

For a completely mechanical final allocation, apply Section5's error
recursion to the finite **post-filter** circuit: the displayed linear
combinations, actual mean products, both curvature rows, direct current
balance, T_U, equation component sums and declared traces. Treat each
raw integral as an input with error <=e, independent cap
V=4V_integrand, derivative cap L=4L_integrand, and A=1. Let
A_post,V_post,L_post be maxima over all internal post-filter gates.
They are computed before e, so this choice is noncircular. The listed
post-filter operations are sums, products and fixed encoded constants;
no data-dependent inverse/log gate is needed. Use

    e=min(1,zeta/(16A_post),
                         zeta/[2^20(1+M_mean)^2]).     (EV19)

Each post-filter gate is itself evaluated with absolute debit <=e,
with fixed constants evaluated to the same accuracy. Then
every final retained scalar has error <=A_post e<=zeta/16<zeta.
This explicit finite circuit rule pays the number and coefficients of
equation sums rather than presuming that a scalar row target also
pays every equation residual. It includes the Delta Q recombination.

For supplied coordinate balls, use the one-unit query/slack box for all
caps. The same post-filter derivative recursion gives an explicit
L_final for every output (raw integral derivative caps are 4L_integrand).
Choose each coordinate radius <=min(1,zeta_0/[64(1+L_final)]), where
zeta_0=theta/[4(1+(|t0|+1)^2)(1+(|x0|+1)^2)] at the rational
box center. Then the outer coordinate contribution is <=3zeta_0/64,
and arithmetic error is <=zeta_0/16; together they remain <zeta_0.
This pays full-tuple coordinate uncertainty as well as EV6's internal
source-coordinate rounding. The extra t jets in Section4 supply the
needed moduli. It is a contract on supplied coordinates, not an oracle
for arbitrary unencoded real numbers.

## 8. Complete finite cost consumer and what it does not prove

Let C_pr(t,X,tau) be the total provider bit-operation cost and
L_pr(t,X,tau) the working storage obtained by traversing the finite
algorithms in Sections2--3, their positive jet/error recurrences and
listed loop bounds. Take the maxima of those input caps on the full
support/slack box, not just its center. C_pr includes every elementary
log/exp/sqrt call in the raw circuits as well as nonsource and G calls;
none is counted as a unit-cost rational gate. Let g be the
number of real gates in the finite retained integrand/post-filter
circuits, a fixed finite count determined by the above inventory.
A direct cost bound for a query is

    number of quadrature nodes =M_q^2,
    bit operations <=M_q^2 [C_pr+2^20 g L_work^2]
                         +2^20 g(M_q^2+1)L_sum^2,    (EV20)

where L_work is the maximum of provider bits, EV15 scalar lengths and
p_post+ceil log2(2+V_post), with p_post=ceil log2(1/e)+2.
L_sum is the Section6 exact common-grid node-sum length enlarged to
that maximum. Add reading/rounding costs for encoded query and fixed
inputs as described after EV8. If the stored source has not yet been
constructed, add AC18's one-time constructor bound; EV20 is its query
consumer rather than a second free source oracle. If a provider
algorithm calls another, count its leaf calls and substitute their
displayed series lengths; these are terminating finite recursions.
For example G contributes EV8 at nu=tau; each gamma-jet request uses
N_G terms of EV9 and the displayed log-series length, and each p or
phase request uses EV10 or its explicit inverse iteration count.
Profile normalization uses its EV12 midpoint count. Thus EV20 has
neither an unspecified mathematical supremum nor a special-function
evaluation oracle. It is an algorithmic, computable finite bound from
the certified descriptor and rational query. It is not a small closed
polynomial bound in source descriptor size.

Provider internal precision, post-filter arithmetic and node-sum bits
are different numbers. The gamma product and the crude flat normalizer
can be exponential in requested accuracy bits. More fundamentally,
EV14's compact physical floor introduces factors d_q^(-k) into raw
derivative and arithmetic caps. At growing height its negative log
contains a quadratic X_q^2 payment. EV17 can therefore require
exponentially many nodes even though Note58's source description is
polynomial. Other deliberately coarse provider caps may inflate this
further. This is a sufficient bound for this evaluation scheme, not a
necessary complexity lower bound or a universal quadrature obstruction.

For fixed t and bounded query/source domains EV5--EV20 give finite
precision and integration error at every prescribed target. No uniform
finite work budget is claimed over R_t x R_x. First fix the full
IC23 descriptor; then choose pointwise zeta, local caps, e, M_q and
provider precisions. Do not insert fixed-b source asymptotics into a
joint large-time/large-height runtime claim.

The analytical comparison remains <=theta_r/2 from Note54/IC23.
The additional evaluation error is <=zeta<=theta_r/4, so the total
is <=3theta_r/4 for each declared scalar. Equation sums retain their
separate component budgets. EV2 makes the numerical error vanish at
both time endpoints and both height ends; the inherited actual field,
domain table and endpoint comparisons are unchanged.

## 9. First upstream unpaid input: literal phase-index construction

The evaluator theorem takes the fixed exact n as descriptor data.
The inherited from-scratch prescription is literally

    n=ceil[Theta(64,U_0)/pi], U_0=2^k.                (EV21)

An arbitrary-precision enclosure of Theta does **not** by itself
give a terminating ceiling algorithm if this number might be an integer.
None of the inspected source/contour bounds supplies a non-equality
bound or an exact equality decision at this selected U_0. This is an
upstream constructive input, not a failure of phase inversion after n
is given and not an error in the mathematical existence of the ceiling.

The exact missing payment is either a terminating equality/separation
rule at the selected (64,U_0), or, in the noninteger case, a proved
positive separation from pi Z sufficient to decide the two neighboring
indices. A sufficient statement is

    dist(Theta(64,2^k)/pi,Z)>=delta_k>0,

with a constructive delta_k for the actual selected k; an exact
integer certificate must be handled separately if equality occurs.
We assert neither that equality occurs nor that this selection is
uncomputable. We record that its finite cost has not been proved by
the existing data. Silently substituting a certified upper integer
would change the literal chosen tuple, so it is not done here.

All ceilings for numerical accuracy/series lengths allow safe upper
integers; that does not automatically amend EV21's exact selection.
Supplying a verified exact n would discharge this discrete input.
Without it, the present result must remain a theorem **from certified
fixed descriptor data**, not an executed or complete from-scratch
IC23 constructor. No improved approximation or positivity statement
is being inferred from this distinction.

## 10. Controls, status and continuation

The new evaluator and circuit lemmas are generic and may also evaluate
smooth colliding controls with their own data; they assert no favorable
sign. Canonical IC23 application additionally uses the full theta source,
completion and inherited branch/collar inputs. Euler-factor controls
change the completion; weighted-square/finite-prime controls do not
retain the complete coefficients/reflection premise; reflected,
shape/primitive controls do not have the canonical source identity;
atomic and heat-polynomial controls lack that smooth complete source.
These are premise checks, not new control runs or collision exclusions.

The source evaluator, provider algorithms from fixed data, arithmetic
propagation and uniform continuous-filter remainder close at their
stated finite scopes. **From-scratch literal phase-index selection
remains unpaid.** Useful working constants, efficient nonsource
algorithms and a filter rule avoiding the generic inverse-q loss are
additional performance tasks. HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain. Same-model checks are not independent validation.

No numerical, exact-rational or machine-symbolic research runs,
source/theta/gamma/field sampling, coefficient evaluation, mesh/precision
search or interval campaign occurred. All algorithms and bounds were
derived on paper. Housekeeping hashes, links and chat capture are not
mathematical certificates. No manuscript/DRAFT_HISTORY change,
snapshot, commit, new user-owned chat or model change.

**Next: Analysis — Sol.** Resolve EV21's exact selection at unchanged
scope, or obtain an explicitly revised bounded selection contract before
constructing a different tuple. For useful evaluation, separately improve
the carrier-aware integration/working-error bound that currently loses
d_q^(-k). No numerical diagnostic is requested by this return. A resistant
non-equality estimate may merit a named analytical escalation after this
focused identification; no general transcendence claim is proposed.


## Scoped continuation — Note60, 25 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**, chat0021. The author subsequently clarified:
**“Use existing onset freedom.”** [Note60](60_EXACT_PHASE_INDEX_BY_DYADIC_ONSET_SELECTION_20261025.md)
and [Review39](../reviews/39_EXACT_PHASE_INDEX_ASSESSMENT_20261025.md)
now construct the literal phase ceiling at one of four admissible binary
onsets, using an explicit full-saddle phase remainder and a terminating
rational interval test with polynomial selector bit cost in the onset
exponent. The winner is selected before X0 and all source-dependent data.
The IC23 formulas and original ceiling are retained. Sections9--10 above
preserve the original finding; their unpaid step is discharged at this
authorized free-onset scope. Equality at an arbitrary previously fixed
exponent remains outside the result. Useful complete evaluator/filter
cost and executed acceptance remain open. HDA-17 Partial, HDA-18 Gated,
HDA-20 unfulfilled remain; no research computation or manuscript change.
