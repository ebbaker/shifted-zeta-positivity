# R05-AN07: uniform RS bounds and fewer contour nodes

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Recurrence **chat0006**, thread
`01a178a3-9572-7bf2-b0a0-bd4d47f796ab`, turn
`01a178b6-b665-71f3-a10f-cc95d0d1ab9c`.

**Return to HDA-R05-AN07 r1. Proved in-note from the named inputs;
same-model internal assessment only.** On precisely the old domains,
the majorants of [Note06][n6] can be replaced by

    B_F^sharp=B_F/sinh(pi) < B_F/10,
    D_k^sharp=D_k/sinh(pi) < D_k/10, every k>=0,
    B_c^new=B_c/16.                                         (J1)

The first two control the full normalized-jet and coefficient family;
the last controls the larger contour region independently. If an old
contour order q delivers all h_m,m<=3K, to truncation error<=tau_h/4,
0<tau_h<=1, then **q_new=q-11** delivers the same error. Every such
old order has q>=12, so the new order is positive. Each four-edge rule
uses **44 fewer contour locations**; each supplied chi uses
44(3K+1) fewer contour summands when all normalized jets are formed.
The proof uses an unbounded comparison family, not chosen finite cases.

Every coefficient C_0 through C_K and its pi/weighted-table error
payment remain. All modes, both arms, canonical normalization, buffers,
strict descriptors, real completion integral, p,K,V, [1,2] and the total
exp(-L²/4) field/spatial orders 0--3/first-time accuracy remain. The old provider
is a valid fallback. The full evaluator and useful runtime are not
certified by these analytical gains. No numerical or machine-symbolic
research check, field evaluation or provider replay was run.

[Input versions][inputs], [work record][work] and [Review13][review]
record exact identities and limits. The input record declares the
family and bound comparison before installation of this result.

## 1. Frozen function, domains and comparison family

Use the actual complex normalization of Note06 E12:

    F_0(z)=[exp(pi i(z²/2+3/8))-i sqrt2 cos(pi z/2)]
                                      /[2cos(pi z)].         (J2)

Every half-integer singularity is removable. At z=n+1/2 both numerator
terms equal i(-1)^(n(n+1)/2), and every denominator zero is simple.
Thus F_0 is entire. No real-cosine normalization is substituted and no
near-zero quotient is evaluated in the certified construction.

The unchanged rectangles are

    R_F: |Re z|<=2,   |Im z|<=1,
    D:   |Re chi|<=3/2, |Im chi|<=1/2,
    R_c: |Re z|<=9/4, |Im z|<=5/4.                          (J3)

The old constants are exactly

    B_F=[exp(2pi)+sqrt2 cosh(pi/2)]/2,
    E_k=8^k(k!)²,
    D_k=B_F (64/pi²)^k(k!)²/(1-pi/8),
    B_c=exp(45pi/16)+sqrt2 cosh(5pi/8), rho_c=9/8.           (J4)

The bound comparison is uniform over all integers k,m>=0 on the
stated rectangles. In particular it covers every finite K, all
m<=3K and k<=K arising from the original accepted exact centers and
queries. The node-count family is every K>=0, 0<tau_h<=1 and any
old supplied integer q satisfying Note06 E27 at m=3K. It includes
the old orders selected by the terminating rational test without
padding. Those orders tend to infinity as tau_h tends to zero, even
at fixed K. No new decision procedure for a real equality or ceil
boundary is used. Original real-node provider inputs and P13's
perturbation/separation restrictions remain; uniform complex analytical
bounds do not enlarge that input class.

## 2. An elementary monotonicity lemma

For a>=2 and t>=0 put

    g_a(t)=exp(at)/cosh t, q_0(t)=cosh(t/2)/cosh t.

With u=tanh t in [0,1), differentiation gives

    g_a''=g_a(a²-1-2au+2u²)>0,
    a²-1-2au+2u²>=(a-1)²>0.                               (J5)

Indeed the quadratic decreases on 0<=u<=1 when a>=2. Consequently
g_a'(t)>=g_a'(0)=a. Also 0<q_0<=1 and

    q_0'=sinh(t/2)/(2cosh t)-q_0 tanh t>=-1.

It follows that

    f_a(t)=[exp(at)+sqrt2 cosh(t/2)]/cosh t
    satisfies f_a'(t)>=a-sqrt2>0.                           (J6)

This proves the necessary mixed-numerator boundary monotonicity.
Bounding its two terms independently at unrelated points would leave
an unnecessarily larger constant. The lemma is an exact calculus
argument; no fitted monotonicity or numerical derivative is used.

## 3. Uniform improvement on the original rectangle

For z=x+iy,

    |exp(pi i(z²/2+3/8))|=exp(-pi xy),
    |cos(pi z/2)|<=cosh(pi|y|/2),
    |cos(pi z)|²=cos²(pi x)+sinh²(pi y).                    (J7)

On horizontal edges y=+/-1, the numerator is at most 2B_F and the
denominator at least 2sinh pi. On vertical edges x=+/-2, put
t=pi|y|. The denominator is exactly 2cosh t, and the numerator is
at most exp(2t)+sqrt2 cosh(t/2). By J6 with a=2, its ratio increases
up to t=pi. Therefore

    horizontal bound = B_F/sinh pi,
    vertical bound   = B_F/cosh pi < B_F/sinh pi.            (J8)

Maximum modulus, justified by the exact removability above, proves
|F_0|<=B_F^sharp everywhere on R_F. The strict gain needs only pi>3:

    sinh pi > sinh3
      >3+27/6+243/120+2187/5040+19683/362880
      =44859/4480 >10.                                    (J9)

All summands are positive; the rational calculation is part of the
proof, not an executed finite research check. Thus
alpha:=1/sinh pi<4480/44859<1/10.

Radius-1/2 Cauchy at every chi in D now gives, for every m>=0,

    |h_m(chi)|=|F_0^(m)(chi)/m!|<=B_F^sharp 2^m.            (J10)

Radius-one Cauchy at real chi in [-1,1] gives the corresponding real
derivative bounds. Note06's exact weighted recurrence is unchanged:

    C_k=pi^(-2k) sum_(j=0)^floor(3k/2)
                 (pi/(2i))^j e_j^(k) h_(3k-2j),
    |e_j^(k)|<=E_k=8^k(k!)².                               (J11)

Every summand bound is linear in B_F. Repeating E16--17's identical
finite algebra therefore proves

    |C_k(chi,1/2)|<=D_k^sharp=alpha D_k on D,
    |partial_chi^s C_k|<=alpha times E17's old RHS,
                      real chi in [-1,1], s=0,1,2.          (J12)

This is a strict uniform improvement for every k, including k=0;
it does not improve the weighted coefficient bound E_k itself, prove
a lower bound for actual coefficient size, or change its normalization.

## 4. The larger contour region needs its own proof

An R_F bound alone would not pay E27, whose edge ellipses extend into
R_c. On horizontal edges of R_c the numerator is at most B_c and the
denominator at least 2sinh(5pi/4). On vertical edges x=+/-9/4,

    |2cos(pi z)|²=2+4sinh²t>=2cosh²t, t=pi|y|.

The numerator is at most exp((9/4)t)+sqrt2 cosh(t/2). By J6 at
a=9/4 the resulting upper ratio increases up to t=5pi/4. Thus

    |F_0|<=B_c/min(sqrt2 cosh(5pi/4),2sinh(5pi/4)) on R_c.

For t=5pi/4>15/4, the positive series give

    cosh t>1+(15/4)²/2+(15/4)^4/24=99969/6144>16,
    2sinh t>2(15/4)+(15/4)³/3=1605/64>16.                 (J13)

Both boundary denominators exceed 16. Maximum modulus proves the
simple effective replacement

    |F_0|<B_c/16=:B_c^new throughout R_c.                    (J14)

The exact four contour edges, rho_c=9/8 ellipses and distance1/4
remain unchanged. Radius-1/4 disks about Gamma also lie within R_c;
consequently |F_0'|<=4B_c^new there, as required for P13. The contour
separation |2cos(pi zeta)|>=1 for scalar quotient delivery is retained;
the proof does not use direct quotient evaluation near real poles.

## 5. Eleven fewer nodes per edge at identical jet tolerance

Write the actual old E27 allowance at M=3K as

    U(q)=(24/pi) B_c 4^(M+1)
                  rho_c^(-2q+1)/(rho_c-1).                 (J15)

Every supplied old q satisfies U(q)<=tau_h/4, with 0<tau_h<=1.
No minimal-order claim is needed. The elementary rational comparisons

    rho_c^4=6561/4096<13/8,
    rho_c^3=729/512<3/2,
    rho_c^22<(13/8)^4(3/2)^2=257049/16384<16              (J16)

are strict. At q=11, pi<4,B_c>1 and 4^(M+1)>=4 imply

    U(11)>192 rho_c^-21>12>tau_h/4.

Since U decreases in q, every accepted old order has q>=12.
For q_new=q-11>=1, replacing B_c by B_c/16 gives

    U_new(q_new)/U(q)=rho_c^22/16
                      <257049/262144<1.                   (J17)

Thus U_new(q_new)<tau_h/4 with exactly the same jet tolerance and
all m<=M, because the worst-case factor is still 4^(M+1). This
comparison applies directly to an old certified order: it never decides
whether a logarithm is exactly an integer. Any rational upper enclosure
bar B_c used in the old certificate can be divided by 16, and J17
holds with those same enclosures. The finite node rule is constructed
at the smaller order using the existing certified Gauss provider.

A four-edge rule goes from 4q to4q-44 locations. F_0 values may be
reused across all jets and across queries at the same rule; the saved 44
is per instantiated rule, not repeatedly counted for reused samples.
Forming every h_0,...,h_(3K) for one chi saves 44(3K+1) summands.
Both statements hold throughout the declared unbounded tolerance/order
family. They do not imply a fixed percentage reduction in total cost,
an improved polynomial degree, or measured runtime. All N arithmetic
modes and the outer completion integral still remain.

## 6. Delivered data, rounding and retained-integral propagation

The new quadrature order pays analytic truncation only. Construct its
nodes and weights to the original P13 tolerances, or the following
no-larger constants. With M=3K, replace

    B -> B/16, L_zeta -> L_zeta/16, L_chi -> L_chi/16

in P13, using B=B_c4^(M+1), L_zeta=4(M+2)B,
L_chi=4(M+1)B. Its full data error remains

    [eta_w^c B +(12+eta_w^c)
       (L_zeta eta_zeta+L_chi eta_chi+eta_H)]/(2pi)
      +eta_kappa(12+eta_w^c)(B+eta_H).                      (J18)

Terms eta_H, eta_kappa, total contour length12, and all input/node/weight
errors are retained. Using the original tolerances makes J18 no larger.
The normalized output quantization allocation also remains. The smaller
order does not itself waive or certify these finite data contracts.

In P14 the unchanged denominator separation still gives

    |F_hat-F_0|<=2eta_N+2B_c^new eta_d, eta_d<=1/2.          (J19)

The old scalar numerator/denominator accuracies therefore remain valid.
All reciprocal powers and pi/kappa perturbations retain their payments.
Exact weighted tables have epsilon_e=0 as before; a rounded alternative
must retain J11/E28's |e_j|epsilon_h+|h_m|epsilon_e+
epsilon_e epsilon_h bound term by term.

For P15 retain A_kj,S_C and its rational pi lower bound3, and set

    T_C^sharp=max_(k<=K) sum_j (2k-j)A_kj/3
                         *(B_F^sharp 2^(3k-2j)+1).         (J20)

Then |C_hat_k-C_k|<=tau_h S_C+|pi_hat-pi|T_C^sharp,
and T_C^sharp<=T_C. The **+1 remains**. It prevents claiming that the
whole pi-conditioning constant scales by alpha. The original tau_h
and pi tolerance caps deliver every k<=K at identical epsilon_C;
one may refine the new caps only from the actual J20 formula.

No new transcendental oracle is needed. A simple rational delivery
record may use bar B_F/10 instead of the exact sharper value, since
B_F^sharp<B_F/10<=bar B_F/10. This preserves the factor-controlled
enclosure convention when the displayed new majorant is B_F/10.
Use bar B_c/16 for the contour. All elementary tails and their errors
remain those of the existing finite providers.

For the outer retained integral, E18/E23 improve only in their RS
coefficient sums. For example set

    S_RS=H_U a_*^-1/2 sum_(k=0)^K D_k a_*^-k>0.

Its old and sharpened ellipse factors are

    B_Q=2H_M(T_X+S_RS),
    B_Q^sharp=2H_M(T_X+alpha S_RS),
    B_Q^sharp/B_Q=(T_X+alpha S_RS)/(T_X+S_RS) in[alpha,1).   (J21)

When transfer is absent the ratio is alpha. When it is present there
is no uniform alpha factor for the whole integral allowance. Apply
the same affine replacement to B_loc, leaving its transverse transfer
cost, all kernel/spatial/time factors, total branch length, endpoint
guards and frozen branch labels unchanged. E20, E22--25 may use these
smaller majorants; retaining the old allocations already proves the
same delivered accuracy. A claim of fewer **outer** Gauss nodes would
need a separate ceil comparison; none is made here.

## 7. Full accuracy, all heights, and what did not change

Keep the half-target truncation, L>=64nu onset, strict exact descriptors,
comparable dyadic e and scale/geometry/arithmetic/RS/quadrature/rounding
allocations of Notes06/09--11 and16. J10--21 either preserve or decrease
the specific positive bounds used in those inequalities. The contour
truncation still receives <=tau_h/4, P13 data errors retain their separate
allocation, and P15 supplies every C_k at the same epsilon_C. Consequently
the same center-normalized evaluation allowance and outer conversion
give total combined error<=exp(-L²/4). This is a substitution into the
proved finite contracts, not an inference from agreement of sampled jets.

The method retains every m<=3K and every k<=K, and all n<=N with exact
adjacent-cutoff transfer. Constant improvements hold for every integer
order, so no new p,K or N jump restriction appears. The model is frozen
under z,T differentiation. No uncertain-coordinate delivery, additional
mixed T,z channel, through-zero/moving-time theorem, arithmetic
compression, necessary onset, or complete evaluator certificate follows.
Delivered-precision and full bit-work/streamed-space orders stay those
of Note10. The old provider, constants and contour order remain valid
fallbacks; the N02 software packet and caps are not executed or enlarged.

## 8. Checks, scoped limits and disposition

The gain closes analytically without a finite research run. Two read-only
checks covered boundary calculus and propagation; a third assessed the
written proof, including the 11-node count. They share model and named
source premises and do not constitute independent specialist validation.
Selected [Polymath Proposition6.2, (53)](https://arxiv.org/html/1904.12438v2#S6.SS2)
and [DLMF3.5(v)](https://dlmf.nist.gov/3.5#v) passages were re-read for
complex C_0 normalization and Gauss positive-weight/polynomial exactness.
No fresh full reading of PartI's coefficient proof is claimed; the
inherited PartII exact-identity access/caveats remain. New constants, boundary calculus and count arithmetic are derived here.

The failed shortcut is precisely scoped: the improved R_F bound alone
does **not** imply a smaller E27 constant, because its edge ellipses use
R_c. Section4 separately closes that missing uniform inequality. Also
neither the transfer-containing integral nor T_C's +1 scales uniformly
by alpha. These are limits on specific substitutions, not impossibility
claims about better providers or cancellations.

This is an approximation/evaluation milestone under [avoid01][a1],
judged by J1 and J17. Read the [result index][results], [heat cluster][heat],
[controls12][controls] and [avoid index][avoid], especially
[shared-premise limits][a5] and [separate bounds][a12]. Euler-factor/
finite-prime controls fail unchanged canonical coefficients; weighted-
square/cutoff controls fail the complete canonical xi/RS initial identity;
reflected, smooth and positive-primitive controls fail the same full
gamma/arithmetic identity. Atomic profile controls lack that complete
source, and RH-conditional endpoint controls lack ordinary Dirichlet
arithmetic. Heat equations may survive. No collision, RH, simplicity
or physical-transfer exclusion follows from this applicability screen.

**Disposition:** AN07 r1 Complete and CLOSED at the bounded analytical
scope after Review13. Broad R05 remains Partial at complete software/
certification. R04/R06 NOT_STARTED, HDA-A02 Partial, HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled are unchanged. No new numerical
campaign, thread or software task is dispatched. The [continuation19][next]
records the next recommended analytical target and supporting N02 lane.

[n6]: 06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md
[n9]: 09_FINITE_PROVIDER_ALGORITHMS_20261026.md
[inputs]: 18_UNIFORM_RS_BOUND_INPUTS_20261026.json
[work]: 18_UNIFORM_RS_BOUND_WORK_RECORD_20261026.json
[review]: ../reviews/13_UNIFORM_RS_BOUND_ASSESSMENT_20261026.md
[next]: 19_ANALYTICAL_CONTINUATION_AFTER_RS_BOUNDS_20261026.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[a5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
