# AGC-B04: three-prime cancellation and its fixed-strip obstruction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Conceptual helper explicitly dispatched
**gpt-6-astra / ultra**; this is dispatch metadata, not independent
serving-backend attestation. Root backend model and effort unavailable.
One conceptual pass and one correction/alternative pass. No numerical
evaluation, scan or certificate is part of this decision.

**Decision: freeze one arithmetic mechanism and a quantitative failure
test, AGC-E16 r1.** Use the three-prime Euler multiplier for primes
2,3,5, retaining its exact coefficient cancellations and the shared
phases of the two principal sums. The final estimator takes a sum of
individual ellipse radii and pays the retained correction separately.
Eight unaffected prime terms already force this estimator's signed
complete lower allowance below **−1/400** on the fixed lower boundary
segment specified below, provided the elementary rational estimate in
the frozen E16 request is proved. E16 owns the full proof and a separate
assessment owns acceptance; the target is not yet an acquired result.

| Next task | Type / recommended model | Readiness | Deliverable |
| --- | --- | --- | --- |
| **AGC-E16 r1, default** | E / Sol6.1 ultra | [Frozen request](../research-progress/handoffs/AGC-E16-r1-request.md) | Exact arithmetic/ellipse proof, rational eight-prime witness, complete errors and scoped failure |
| Separate E16 assessment | E / Sol6.1 ultra | E16 proof complete | Check formulas, constants, control scope and integration |
| AGC-B05, stronger arithmetic acquisition | B / Astra ultra | Accepted E16 outcome; no new mechanism selected here | Select a phase-preserving grouping with a distinct quantitative input and a bounded proof contract before any numerical packet |

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns live status. Required interpretation is routed to the
[result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: an independently checkable quantitative screen of one
lower-bound estimator, not another restatement of the desired positivity.
The quantitative outcome concerns the allowance, never the true value.

Inputs read: Notes10–11 and13–15, Review07, manuscript Section10,
E14's return, the B04 request and the required repository instructions.
The earlier fixed-circle bound D_H>.1493308659 and its scientific pins
remain unchanged. Related RSCT multiplicative-phase exclusions, routed
from pattern07, concern different relaxed signed consumers and do not
establish the present canonical-parameter estimate.

Selected passages of [Polymath v2](https://arxiv.org/html/1904.12438v2)
were reopened: definitions (9)–(22), the retained-correction interface,
§8.5's finite Euler multiplier and Lemma8.5, Proposition9.1 and
Theorem1.2. The present modulus/ellipse inequality is derived directly;
the published numerical constants at t=.2 are not imported at t=.1.
No new source version, reading copy, novelty claim or full-paper audit.

## 1. Actual normalized arithmetic and the selected information

Keep t=1/10 and the exact final strip

    x>=x0:=14000+sqrt(24/25),   1/5<=y<=sqrt(4/5).

Write s0=(1+y−ix)/2, s=s0+(t/2)alpha(s0)=sigma+i*tau,
where alpha(s0)=1/(2s0)+1/(s0−1)+(1/2)Log(s0/(2pi)).
Use the accepted nonzero carrier B=M_t(s0), the exact gamma and kappa
of source(16),(18), and

    b_n=exp(log(n)^2/40),   N=floor(sqrt(x/(4pi)+1/160)),
    S=sum_(n<=N) b_n n^(−s),
    T=sum_(n<=N) b_n n^(y−s),
    f=P_N/B=S+gamma sum_(n<=N) b_n n^(y−conjugate(s)−kappa),
    c=Cval_N/B=J_N A_N(x/2+pi/80)/B,
    q=Qval_N/B=f−c,   v=Vval_N/|B|.

Here Vval_N is exactly Note14's two complete term-error sums plus
L(delta_-+delta_+). Neither c nor any part of that remainder is omitted.
No heat derivative is taken of this natural-cutoff value formula.

Select the single multiplier

    E=product_(p in {2,3,5}) (1−b_p p^(−s))
      =sum_(d|30) lambda_d d^(−s),
    lambda_d=product_(p|d)(−b_p).

Define real coefficients for 1<=m<=30N by the exact finite convolution

    beta_m=sum_(d|gcd(m,30), m/d<=N) lambda_d b_(m/d),
    a_m=sum_(d|gcd(m,30), m/d<=N) lambda_d (m/d)^y b_(m/d).

The truncation indicator is mandatory, including terms m>N. Thus
U=ES=sum beta_m m^(−s), V=ET=sum a_m m^(−s), and beta_1=a_1=1.
This uses the actual multiplicative phase relation
(dn)^(−i*tau)=d^(−i*tau)n^(−i*tau), so equal frequencies cancel
before any absolute value. It is more information than independent
magnitudes of the original terms. Heat weights are not treated as
completely multiplicative: generally b_(mn) differs from b_m b_n.

The correction pass strengthens the initial separate-branch triangle
bound by retaining the phase coupling between U and conjugate(V).
Put g=|gamma|. Wherever E!=0 and 0<=g<1,

    E(S+gamma conjugate(T))=U+rho conjugate(V),
    rho=gamma E/conjugate(E),   |rho|=g.

For rho=g exp(i theta), rotate by exp(−i theta/2). Each m-th pair
then lies on the ellipse with semiaxes |beta_m+g a_m| and
|beta_m−g a_m|, times m^(−sigma). The constant pair lies on the
ellipse with axes 1+g and1−g. This retains the within-index coupling;
the eventual triangle sum discards dependencies between different m.
The actual phases tau log(m) are not replaced by a claimed actual
counterexample. Their remaining correlations are simply unused by this
specified estimator.

## 2. Fixed lower-bound formula and completion target

For a complex number w set

    ||w||_g=sqrt((Re w/(1+g))^2+(Im w/(1−g))^2).

The constant pair has this norm1, and |w|>=(1−g)||w||_g.
The triangle inequality therefore supplies the signed lower bound

    K=(1−g)−sum_(m=2)^(30N) h_m m^(−sigma),
    h_m=max(|beta_m−g a_m|, ((1−g)/(1+g))|beta_m+g a_m|).

All retained terms and cutoff-edge convolution terms are present.
The exact kappa replacement is paid by

    D_kappa=g sum_(n=1)^N b_n n^(y−sigma)
                       [exp(|kappa| log n)−1],

using |n^(−kappa)−1|<=exp(|kappa|log n)−1. The selected lower function
and complete signed allowance are

    ell_E=K/|E|−D_kappa−|c| <= |q|,
    m_E=ell_E−v.

This formula uses the actual retained reference q=f−c; paying |c|
separately is a declared limitation of this estimating class, not a
change back to the old omitted-reference error budget. The entire
retained source budget v is still paid. If a nonnegative lower function
is desired, max(0,ell_E) is valid, but cannot supply a strict floor
where ell_E<0 and v>0. The definition uses the exact |E|. An upper
bound for |E| must not be substituted into this signed lower-bound
formula when K<0; it is used below only to bound the already defined
allowance from above and demonstrate its failure.

E16's fixed failure domain is the included lower boundary segment

    F0={t=1/10, y=1/5, x0<=x<=30000}.

This is an analytic interval question, not a parameter scan. The target
is m_E<−1/400 everywhere on F0. In particular it includes the exact
lower endpoint of the required closed final strip, so global success
of this estimator is already impossible if the target is proved.

The proof reduces to elementary constants:

    N>=33,   3/5<sigma<4/5,   0<g<3/5,   0<|E|<8,
    sum_(p in P*) exp(log(p)^2/40) p^(−4/5)>21/20,
    P*={7,11,13,17,19,23,29,31}.

Every p in P* is present and coprime to30, hence beta_p=b_p and
a_p=p^(1/5)b_p. Consequently h_p>=(1−g)b_p. The eight terms alone
give K<−(1−g)/20<−1/50, and division by |E|<8 gives
K/|E|<−1/400. D_kappa, |c| and v are nonnegative and cannot rescue
the allowance. This rejects even the strengthened paired-ellipse
version, rather than just the initial separate-branch triangle bound.

For the sigma bound, put T0=x/2. Directly from alpha at3/5−iT0,

    Re alpha−(1/2)log(T0/(2pi))
      = (3/10)/(T0^2+9/25)−(2/5)/(T0^2+4/25)
        +(1/4)log(1+9/(25T0^2))
      <= (39/100)/T0^2−(2/5)/(T0^2+4/25)<0.

Thus sigma<3/5+(1/40)log(x/(4pi))<4/5 on F0:
x/(4pi)<2500<e^8 follows from pi>3 and e>8/3.
A crude positive lower bound for Re alpha gives sigma>3/5.
The source bound g<=exp(y/50)(x/(4pi))^(−y/2) gives g<3/5.
Since log p<2 for p=2,3,5, each b_p p^(−sigma)<1, proving E!=0
and |E|<8. E16 must give a short exact-rational proof of the finite
eight-prime sum, not a floating decimal evaluation. Conservative
rational lower logarithms and exponential series, or fifth powers,
are routine permitted choices. The root's separately dispatched
Sol6.1/ultra preflight supplied a concrete quartic-series witness,
now included as fixed proof data in E16; its [preflight return](../research-progress/handoffs/AGC-E16-r0-preflight-return.md)
is preliminary supporting work, not the accepted E16 proof.

## 3. Direct comparison and every coverage interface

Give direct retained-value evaluation exactly the same b_n, gamma,
kappa, phases, multiplier coefficients, c and complete v. Its exact
allowance is

    m_dir=|f−c|−v >= m_E.

The inequality is a comparison of these exact information reductions,
not a runtime or interval-implementation theorem. Direct evaluation
can itself use the multiplier and ellipse construction. Nothing here
shows m_dir<=0, exhibits a physical zero or excludes an estimator
retaining cross-index phases or c's exact orientation.

The full desired strip would require a split at an effective height
X_tail: finite region x0<=x<=X_tail and tail x>=X_tail, with an
overlap or common included endpoint. The finite region must cover
every y in the full strip, not only F0. The known classical two-carrier
asymptotic supplies eventual tail behavior; it is not new coverage.
An explicit usable X_tail and a complete error comparison there have
not been acquired in this packet. They are an independent dependency
of any future successful global proof, not hidden assumed constants.
No tail acquisition is needed to decide this failure: moving the join
cannot remove the included failing lower endpoint. No separate tail
calculation or finite-region scan is authorized by E16.

At x_j=4pi*j^2−pi/40 the old and new indices are j−1 and j.
Apply the finite convolution independently to each natural chart;
the indicator m/d<=N includes all changed terms. The old endpoint
bound is obtained by its one-sided limit, and the new index owns the
endpoint. Both have N>=33 on F0. Thus the same eight-prime witness
works on both sides of every seam in the failure segment. If a future
argument transfers a fixed reference, it must retain Note14's signed
jump d_j−2J_j A_j(W) and E_new=E_old−Delta Q, or its full paid
bound. No differentiation of a floor or unpaid holomorphic gluing.

The initial zeta verification and intermediate barrier for0<=t<=.1
remain separate unacquired criterion inputs; F0 is a final-time
boundary only. The earlier finite-circle pair theorem remains intact.

## 4. Collision screening and exact scope of the decision

The premises are (a) the literal normalized theta arithmetic and its
complete retained source enclosure, (b) the finite convolution and
stated phase relations, and (c) a strict complete lower allowance.
They must not be collapsed into a generic shape premise.

| Controls12 class | Precise premise not supplied; quantitative control |
| --- | --- |
| Euler-factor translates | Changed ordinary coefficients and source error do not inherit(a); a genuine included zero defeats(c) with its own honest budget. |
| Weighted-square, finite-source, finite-prime and finite-score controls | Preserved finite prime identities or finite coefficient rows do not supply the complete theta coefficients/reflection and remainder in(a). Some may satisfy selected identities in(b); those alone do not prove(c). Retain each construction's own event/location scope and the finite-source lack of an all-real anchor. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Reflection, Gram or primitive positivity does not provide the two finite arithmetic sums and their complete source remainder. With their own valid reference, any included zero defeats(c). |
| Atomic fixed-event and exact finite-profile controls | Finite profile data fail the full theta arithmetic/profile and eventual-simplicity hypotheses; their own threshold events force failure of(c), not a claimed failure on every unrelated box. |
| RH-conditional normalized endpoint controls | Changed ordinary Dirichlet arithmetic fails(a); keep RH and escaping-height qualifiers. A time-zero real double is not a final-strip event. |
| Fixed theta amplitude with changed observation kernel | The literal cosine/Newman readout and complete forcing in(a) fail if the additional prepared forcing is dropped. They are not physical theta collision examples. |
| Fractional profile relaxations and static divisor surgery | Integer physical multiplicity and a common physical heat path, respectively, are missing; neither is a physical zero forced by this allowance failure. |
| Reflection rigidity | Its full normalized conjunction identifies theta in its stated class, but adds no quantitative lower allowance. |

Independently of all source identities, if |H−Q|<=V and H(z*)=0,
then every valid ell<=|Q/B| satisfies ell−V/|B|<=0 at z*.
The exact quadratic H=Q=(z−x_c)^2−2(t−1/4), B=1,V=0 has a
zero at t=.1,z=x_c+i sqrt(3/10), inside the actual final strip for
x_c>=x0. Perfect approximation cannot give(c) there. It does not
claim to satisfy theta's arithmetic or the multiplier premises.

The prospective negative result is restricted to this fixed
{2,3,5} multiplier, anchor coefficient1, sum of individual paired
ellipse radii and separate |c|/kappa/source payments. It excludes
neither larger or adaptive multipliers nor signed groups, height-phase
constraints, correlated correction/remainder estimates, contour
arguments or all arithmetic methods. No numerical campaign follows
from a failed allowance. B04 stops at the frozen E16 contract.

After E16's assessed milestone, the next conceptual choice is
**B05 / Astra ultra**: select one phase-preserving grouping on this
same retained-value consumer and specify a distinct independent input
that controls the grouped sum. Its acceptance test must be a paid
quantitative bound or an equally precise failure, with the same direct
comparator and all coverage interfaces. Merely increasing the prime
set, repeating a positivity criterion or tuning correction constants
does not resolve this named missing information. No grouping or
numerical packet is selected or activated by this guidance.
