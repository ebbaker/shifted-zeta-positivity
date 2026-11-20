# AGC-B05: shared dyadic phase and the full-circle envelope

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Conceptual helper explicitly dispatched
**gpt-6-astra / ultra**; dispatch is not independent serving-backend
attestation. Root backend and effort unavailable. **Type B**, under the
[frozen B05 r1 request](../research-progress/handoffs/AGC-B05-r1-request.md).
One conceptual pass and one correction pass; no numerical scan,
transcendental evaluation or new certificate.

**Decision: freeze E17's analytical obstruction for a stronger grouped
class.** Group all frequencies with the same odd core, preserving their
common dyadic phase, and retain that same phase across groups before
taking one full-circle supremum. The remaining independently relaxed
odd-core phases impose a Fourier-mean floor: the eight surviving prime
cores already force this envelope above **21/20 of the anchor**. The
resulting complete lower allowance is consequently **below −1/400**
throughout the boundary challenge. The derivation below makes the route
tractable; E17 owns its completed proof and a separate assessment owns
acceptance. No actual-height phase maximizer, zero, failure of the direct
margin or universal phase obstruction is asserted.

| Next task | Type / recommended model | Readiness and output |
| --- | --- | --- |
| **AGC-E17 r1, default** | E / Sol6.1 ultra | [Frozen contract](../research-progress/handoffs/AGC-E17-r1-request.md): finite-polynomial norm proof, quantitative obstruction, source and cutoff scope |
| Separate E17 assessment | E / Sol6.1 ultra | After E17: nonauthor check of the mean argument, allowance and information class |
| Actual-height phase acquisition | B / Astra ultra | Conditional continuation after assessment; no new task or numerical packet activated here |

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns status. Read the [result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: a quantitative screen of a specified information reduction,
not an RH-equivalent criterion or a lower bound defined by desired positivity.
Inputs read: Notes14–18, Review08, manuscript Section11 and the frozen
request. Selected passages of [Polymath v2](https://arxiv.org/html/1904.12438v2),
retained Corollary6.4 and Section8.5, were reopened. No new external theorem,
source version, published numerical constant or full-paper audit is imported.

## 1. Unchanged arithmetic and complete payment

Keep the literal theta field, t=1/10, and Note17's exact normalization:

    s0=(1+y−ix)/2, s1=(1−y+ix)/2,
    alpha(w)=1/(2w)+1/(w−1)+(1/2)Log(w/(2pi)),
    s=s0+alpha(s0)/20=sigma+i tau,
    B=M_t(s0), gamma=M_t(s1)/M_t(s0), g=|gamma|,
    kappa=(alpha(s1)−conjugate(alpha(s0)))/20,
    b_n=exp(log(n)^2/40),
    N=floor(sqrt(x/(4pi)+1/160)),
    S=sum_(n<=N)b_n n^(−s), T=sum_(n<=N)b_n n^(y−s),
    f=S+gamma sum_(n<=N)b_n n^(y−conjugate(s)−kappa),
    q=f−c, c=J_N A_N(W)/B, W=x/2+pi/80.

Here J_N and A_N are the unchanged value correction in Note14; the
complete retained error is exactly

    v=Vval_N/|B|,
    Vval_N=sum_(n=1)^N sum_(nu=±)|p_n(t,w_nu)|epsilon_n(t,w_nu)
           +L_N(delta_(sigma_minus)+delta_(sigma_plus)),
    L_N=|J_N|sqrt(W)sqrt(W^2+1)/2,
    w_nu=(1+nu*y)/2+i*x/2.

The full epsilon and delta formulas are Note17(5)–(6), inherited without
deletion or changed constants. Thus |H/B−q|<=v. The arithmetic kappa
replacement remains separately paid by

    D_kappa=g sum_(n<=N)b_n n^(y−sigma)(exp(|kappa|log n)−1).

Retain exactly E=product_(p=2,3,5)(1−b_p p^(−s)) and

    lambda_d=product_(p|d)(−b_p), d|30,
    beta_m=sum_(d|gcd(m,30),m/d<=N)lambda_d b_(m/d),
    a_m=sum_(d|gcd(m,30),m/d<=N)lambda_d(m/d)^y b_(m/d),
    1<=m<=30N.

All cutoff-edge terms are included. ES=sum beta_m m^(−s),
ET=sum a_m m^(−s), and beta_1=a_1=1. With rho=gamma E/conjugate(E)
and rho=g exp(i theta), rotate E(S+gamma conjugate(T)) by
exp(−i theta/2). No multiplicativity of b_n is assumed.

## 2. One explicit grouping and its stronger correction pass

Let R_N be all odd r<=30N. The dyadic index set is

    I_1={j>=1:2^j<=30N},
    I_r={j>=0:r*2^j<=30N} for odd r>=3.

The missing r=1,j=0 term is the unchanged anchor. For real u define
the finite polynomials

    B_r(u)=sum_(j in I_r)beta_(r*2^j)2^(−j*sigma)exp(i*j*u),
    A_r(u)=sum_(j in I_r)a_(r*2^j)2^(−j*sigma)exp(i*j*u).

Use a different symbol from the carrier B only through its subscript.
The actual phase is u=−tau log2 and the actual core phase is
eta_r=−tau log r−theta/2. The entire r-th contribution is exactly

    G_r(eta,u)=r^(−sigma)
                 [exp(i eta) B_r(u)+g exp(−i eta)conjugate(A_r(u))].

Thus every frequency r*2^j retains its true relation to every other
frequency in its core. The same u occurs across all cores. Define

    ||w||_g=sqrt((Re w/(1+g))^2+(Im w/(1−g))^2),
    R_r(u)=(1−g) sup_(eta in [0,2pi]) ||G_r(eta,u)||_g,
    C_sep=sum_(r in R_N) sup_(u in [0,2pi]) R_r(u),
    C_dyad=sup_(u in [0,2pi]) sum_(r in R_N) R_r(u).

The first conceptual pass used C_sep. The allowed correction pass
selects **C_dyad**, retaining the common u until after summation. All
coefficients, sigma, g and N are held at the actual observation point
while these auxiliary phase suprema are taken. No coefficient is
recomputed at a hypothetical height. The only phase relaxations are
independent eta_r and the full-circle enlargement of the actual u.

This input is explicit finite harmonic analysis. In particular, set

    M_r(u)=[ (Re B_r+g Re A_r)/(1+g), −(Im B_r+g Im A_r)/(1+g);
             (Im B_r−g Im A_r)/(1−g),  (Re B_r−g Re A_r)/(1−g) ].

Then R_r(u)=(1−g)r^(−sigma)||M_r(u)||_2, where ||.||_2 is the
real matrix operator norm. This follows by applying the ellipse's
diagonal scaling to the cosine and sine columns of G_r. No optimization
or numerical approximation is necessary for the obstruction below.

The constant pair has ellipse norm one. Reverse triangle therefore gives
the valid signed lower allowance

    K_dyad=1−g−C_dyad,
    ell_dyad=K_dyad/|E|−D_kappa−|c| <= |q|,
    m_dyad=ell_dyad−v.

The correction c is retained in q and its exact magnitude is paid
separately; no phase cancellation with c is claimed. The entire physical
v and kappa cost are additional. As in E16, the divisor in this definition
is exact |E| even when K_dyad is negative.

Writing C_ind=sum_(m=2)^(30N)h_m m^(−sigma) for E16's cost, the
triangle inequality for each matrix coefficient proves

    C_dyad<=C_sep<=C_ind, hence m_E<=m_dyad<=m_dir:=|f−c|−v.

The grouped estimator is a real strengthening of that reduction, though
no strict improvement is asserted. Direct evaluation receives every
polynomial, phase and payment and can use this same bound. There is no
runtime or universal implementation advantage.

## 3. Independent input, quantitative threshold and obstruction

For a positive complete allowance, an independently acquired upper
bound for C_dyad would have to cross the concrete threshold

    C_dyad < 1−g−|E|(D_kappa+|c|+v) <= 1−g.                 (1)

We do not assume this inequality or define a new floor by it. The
independent input actually acquired here is the finite Fourier mean
and convexity inequality, which makes (1) impossible for this envelope.
For any odd r>=3, averaging each matrix entry over the circle gives

    mean_u M_r(u)=diag((beta_r+g a_r)/(1+g),
                      (beta_r−g a_r)/(1−g)).

The matrix norm is convex, so

    mean_u R_r(u)>=(1−g)r^(−sigma)||mean_u M_r(u)||_2
                   =h_r r^(−sigma).                       (2)

For r=1 the mean matrix is zero and its cost remains nonnegative.
Consequently, because a supremum dominates its mean,

    C_dyad >= sum_(r odd,r>=3)h_r r^(−sigma).              (3)

These are elementary identities and norm inequalities, independent of
any nonvanishing or positivity assertion about the physical field.
They distinguish this input from a restatement of the desired floor.

On F0={t=.1,y=.2,x0<=x<=30000}, x0=14000+sqrt(24/25), the accepted
Note17/Review08 supplies N>=33, .6<sigma<.8, 0<g<.6, 0<|E|<8
and the exact eight-prime witness

    P*={7,11,13,17,19,23,29,31},
    sum_(p in P*)b_p p^(−.8)>21/20.

Each p is its own odd core and satisfies beta_p=b_p,
a_p=p^.2 b_p, hence h_p>=(1−g)b_p. Equations(2)–(3) therefore give

    C_dyad>(21/20)(1−g),
    K_dyad<−(1−g)/20<−1/50,
    ell_dyad<−1/400, m_dyad<−1/400 on F0.                 (4)

The 5% anchor excess precedes all three remaining payments. The use
of |E|<8 upper-bounds the already defined negative allowance; it does
not replace the denominator in a signed lower-bound definition.
Clipping ell_dyad at zero cannot give a strict margin over v>=0.

This proves a floor on a **full-circle envelope**, not a lower bound
on sum_r R_r(u(x)) at the actual phase. Indeed the separately valid
actual-phase allowance replaces C_dyad by that latter sum and can be
larger. This argument does not determine its sign. Neither (2) nor (3)
asserts that the worst u and independent eta_r arise at one physical x;
all actual-height arcs, their coefficient variation and the relations
among different odd-core phases remain outside the obstruction.

## 4. Exact domain and cutoff interfaces

The target remains t=.1, x>=x0 and .2<=y<=sqrt(.8); only F0 is tested.
At t=.1 the natural seams are

    x_j=4pi*j^2−pi/40,
    old index j−1, new index j.

There are exactly the indices N=33,...,48 and seams j=34,...,48 in
F0. For an elementary endpoint check use 25/8<pi<22/7:
x_33<14000<x0<x_34 and x_48<30000<x_49 (x0<14001).
Intersect each half-open [x_N,x_(N+1)) with [x0,30000]. The last
endpoint 30000 is included with N=48. At every internal seam both
one-sided references contain all eight primes, and the convolution and
dyadic grouping are reconstructed with their respective N. Terms with
zero coefficients remain harmless; none beyond N but below30N is dropped.

If a fixed reference is transferred, retain Note14's exact signed
jump Delta Qval=d_j−2J_j A_j(W) and E_new=E_old−Delta Q, or pay
its complete magnitude. The old endpoint bound follows by continuity;
the new index owns the seam. No floor derivative or unpaid gluing.

Since (4) holds at the included x0, no repositioned finite/tail join
can rescue this chosen envelope on the whole strip. The rest of the
two-dimensional finite strip and an effective infinite-tail onset with
paid overlap remain unacquired. A hybrid using a distinct successful
estimate would require that new input. The separate initial zeta
verification up to height7000 and full intermediate barrier for
0<=t<=.1 remain obligations of the source criterion. No new Newman
bound, coverage or tail calculation follows here; the earlier finite
pair certificate and retained-value gain remain intact.

## 5. Controls and exact scope

Apply Controls12 to three different premises: **S**, the literal theta
source and complete normalized enclosure; **P**, the retained finite
arithmetic and dyadic phase identities; **M**, a strict complete margin.
The Fourier-mean obstruction needs no physical M assumption. Generic
dyadic identities may hold for other sources; they do not identify theta.

| Control class | Named failed or unprovided premise |
| --- | --- |
| Euler-factor translates | Their changed coefficients/shifted field require a changed S enclosure; selected multiplicative P identities can survive. An included zero defeats M with any honest enclosure. |
| Weighted-square, finite-source, finite-prime-orbit and finite-score controls | Finite arithmetic/support measurements do not supply the complete S coefficients, reflection and remainder. Some P relations survive; that is no M input. Preserve each event/location scope and the finite-source lack of an all-real heat anchor. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Reflection, shape, Gram and primitive information do not supply S or the actual polynomial coefficients in P. Their own included zeros defeat M; no failure on this unrelated fixed strip is claimed. |
| Atomic fixed-event and finite-profile controls, including continuous extensions | The full theta arithmetic/profile and eventual-simplicity premises are absent despite selected profile floors. Their included threshold events defeat M. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic in S changes. Keep the RH condition and escaping-height qualifier; their time-zero real doubles are not events on F0. |
| Fixed theta amplitude with variable observation kernel | The changed readout has additional prepared forcing, so S fails if that payment is omitted. Raw compatibility or finite cosine data do not supply M; these are not physical theta collisions. |
| Actual-theta finite-profile fractional relaxation, static divisor surgery | The integer physical divisor or common physical heat path is absent; neither is a counterexample to an actual theta phase estimate. |
| Reflection rigidity | Its complete normalized conjunction identifies theta in its stated class, but supplies no quantitative M. |

At any included zero, |H/B−q|<=v forces every valid ell<=|q|
to satisfy ell−v<=0. The exact generic check H=Q=(z−x_c)^2−2(t−1/4),
B=1,v=0 has a zero at t=.1,z=x_c+i sqrt(.3) in the full strip for
x_c>=x0. It fails M despite perfect approximation and does not have S.

The exclusion is confined to the fixed {2,3,5} convolution, anchor1,
odd-core dyadic groups, independent core rotations, one common
full-circle dyadic-phase envelope, and separate kappa/correction/source
payments. It does **not** exclude the actual u(x), short height arcs,
correlation among different odd cores or with the anchor, correction
orientation, larger products, other grouping geometries, contour or
heat methods. A future **B06 / Astra ultra** decision must choose one
specific escape and acquire its quantitative input. For actual-height
restrictions, it must enclose the joint curve

    (u(x),eta_r(x))=(−tau(x)log2,−tau(x)log r−theta(x)/2)

together with the changing sigma,g,beta,a and every cutoff. Its bound
must cross the full paid threshold, with direct evaluation given those
same enclosures. For anchor coupling, it must retain a signed aggregate
of the anchor and chosen cores (and c if claimed), specify a separately
proved lower estimate for that aggregate, and pay all unretained terms.
The current circle-mean argument does not decide either option. Merely
naming these exact phases or a favorable correlation acquires neither
input. No choice between them, new packet or numerical campaign is
activated here; root's continuation will own that B06 decision.

The correction pass specifically strengthened separate group suprema
to a common-phase supremum, checked the matrix signs and missing
core-one constant, distinguished actual-phase and envelope claims,
and made every natural endpoint explicit. E17 now has a finite
analytical route and no unresolved design choice. Its proof and
assessment, not this conceptual dispatch, determine accepted status.
