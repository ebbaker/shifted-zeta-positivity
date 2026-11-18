# B07 r3 — Retaining the joint forcing: bounded advisory

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Helper at inherited configuration; actual
serving model and effort are unavailable. This is route-A analytical
advice under [B07 r3][request], not the lead's executed canonical proof or
its separate assessment. No numerical experiment or manuscript edit.

Read [result summaries][results] and [avoid][avoid], particularly
[classification01][class], [controls12][controls], [premises02][premises],
[scope07][scope] and [joint12][joint]. [Continuation22][cont] and the
accepted [E21 proof][e21] delimit the one-step initial-M consumer failure.
The following comparison is different: it retains a coupled, whole-time
lower bound for a normalized positive forcing. Its quantitative target is
a physical interval that does not shrink like 1/(log height)^2. The
conditional inequality alone is not a canonical acquisition milestone.

## 1. Exact variables and the useful barrier

On the stopped simple all-real physical backward interval, let

    D_u = −2+4DM,
    M_u = −2M²+F,             F=12S2+16D S3,
    V=1−2DM,                 K=2D²F=24D²S2+32D³S3.

D>0, M≥0, and all exterior occurrences are retained. These are the
[accepted regular hierarchy][hierarchy] and [Note17][n17] identities.
Direct product differentiation gives

    D_u=−2V,
    V_u=2M(1+V)−2DF=(1−V²−K)/D.                    (1)

This normalization matters: K involves the *same pair's* D and complete
moments. Separate bounds with their correlation discarded need not imply
a useful lower K.

**Conditional barrier.** Suppose, throughout a common stopped interval,

    K(u) ≥ 1−eta²,       0≤eta<1,
    V(0) ≤ v0,          v=max(v0,eta)<1.            (2)

Then

    V(u)≤v,          D(u)≥D(0)−2vu.                 (3)

If v>0, strict positivity holds through every

    Delta < D(0)/(2v).                             (4)

If v=0, D is nondecreasing through the stopped interval. The available
physical slab and full pair/boundary coverage still constrain use.

Proof: (1) and (2) give V_u≤(eta²−V²)/D. On any compact pre-stop interval
D has a positive minimum, so scalar comparison applies to the locally
Lipschitz right side. The constant v is a supersolution because
eta²−v²≤0, and V(0)≤v. Alternatively apply the usual positive-part
Gronwall argument to (V−v)_+. Integrating D_u=−2V proves (3).
No time derivative of an asymptotic error or finite moment closure is
used. Taking compact intervals to the first stop retains (3) by continuity.

For the canonical high-height scale D(0)~4π²/L², sufficient rates for
an arbitrarily fixed admissible Delta are

    upper bound for V(0) = o(L^−2),
    upper bound for 1−K(u), uniformly in u, = o(L^−4).        (5)

These are sufficient rates for this barrier, not necessary conditions
for actual noncollision. The square root of the K deficiency is paid;
writing only K=1+o(1) would not meet the target.

## 2. A finite positive head gives an exact lattice deficit

For the equally spaced two-sided divisor with gap g, take the pair 0,g
and n exterior labels on each side. Write D=g²/4. For the mth exterior
label on either side, q_m=1/[g²m(m+1)]. Define the finite positive sums
S2,n and S3,n with these 2n labels. Then

    K_n=24D²S2,n+32D³S3,n
       =sum_(m=1)^n {3/[m²(m+1)²]+1/[m³(m+1)³]}
       =sum_(m=1)^n {1/m³−1/(m+1)³}
       =1−(n+1)^−3.                               (6)

The middle equality follows from 3m(m+1)+1=(m+1)³−m³.
Thus the exact normalized-forcing deficit is cubic in n; it requires
neither zeta-value evaluation nor a numerical sum. The corresponding
initial interaction subsum b_n gives

    2D b_n=n/(n+1),       1−2D b_n=1/(n+1).         (7)

On a real divisor, omitted exterior contributions are positive. A lower
K from the finite head therefore needs no upper tail subtraction. A claim
about the complete interaction M, its error, or an asymptotic equality
still requires its complete tail payment. This distinction does not
license a finite divisor evolution: the head labels and D are evaluated
along the unchanged full dynamics.

If (6) and (7) hold as lower inequalities for the relevant evolving
configuration, the barrier gives v=1/(n+1) and the conditional duration

    Delta < g(0)²(n+1)/8.                           (8)

Unlike the old initial-M Riccati horizon, this allowance grows linearly
with the number of dynamically controlled neighbors. The difference is
the **whole-time head geometry** needed for (6), not additional initial
data alone.

A robust version makes that acquisition requirement explicit. Let a,b be
the pair at a time u, and d>0 a local reference spacing. Suppose
0≤e<1/3, g=b−a≥(1−e)d, and for each of the first n exterior labels on
either side, its distances r and r+g from the two target endpoints obey

    r ≤ (1+2e) m d,
    r+g ≤ (1+2e)(m+1)d.                            (9)

These inequalities hold, for example, under the absolute normalized
clock error bounds inherited from E21, after increasing e to cover both
endpoint errors. Define gamma=(1−e)/(1+2e). Each normalized contribution
satisfies Dq≥gamma²/[4m(m+1)]. Since 0≤gamma≤1, (6)–(7) imply

    K ≥ gamma^6 [1−(n+1)^−3]
      ≥ 1−18e−(n+1)^−3,
    1−2D b_n ≤ 6e+(n+1)^−1.                       (10)

Indeed 1−gamma≤3e, 1−gamma^6≤6(1−gamma)≤18e, and
1−gamma²≤2(1−gamma)≤6e. Use the lower bound on the complete M at the
initial time to obtain the second inequality for V(0).
With a uniform e_* on the full interval, a fully explicit barrier parameter
is therefore

    v=max{6e_*+(n+1)^−1,
          sqrt(18e_*+(n+1)^−3)}.                   (11)

Apply (3)–(4) whenever v<1. This is a finite, proof-ready sufficient
mechanism, with explicit source error and label-count dependence. It
has not acquired e_* for theta by being stated here.

## 3. Why a ratio-F bound is a weaker comparison

For M>0 write kappa=F/(2M²). The same exact equation (1) becomes

    V_u=2M[(1−kappa)+(1+kappa)V].                  (12)

Near kappa=1 this is an unstable upper comparison in a positive V:
its coefficient is approximately 4M, of order L² at high height.
Thus F≥2(1−epsilon)M² is not interchangeable with (2).

For 0<epsilon<1, that ratio hypothesis gives

    M(u)≥b/(1+2epsilon b u),       b=M(0),
    D(u)≥A(u)^(2/epsilon)
      [D(0)−{1−A(u)^(-(2−epsilon)/epsilon)}/(b(2−epsilon))],
    A(u)=1+2epsilon b u.                            (13)

The first inequality is the scalar Riccati comparison, and the second
follows by multiplying D_u≥−2+4D b/A by A^(−2/epsilon) and integrating.
For p=bD(0), r=1−(2−epsilon)p>0, this lower comparison remains positive
only for

    Delta < [r^(−epsilon/(2−epsilon))−1]/(2epsilon b).   (14)

For epsilon=0, M≥b and the continuous limit is

    D(u)≥exp(4bu)[D(0)−(1−exp(−4bu))/(2b)].          (15)

If the initial upper defect is delta=1−2bD(0)>0, the horizon is
log(1/delta)/(4b). At bD(0)=1/2 but epsilon↓0, (14) is asymptotic to
log(2/epsilon)/(4b). If bD(0) is already on the favorable side with a
proved sign, these particular finite caps need not apply.

Consequently a conservative positive defect allowance O(1/L), as in the
unrefined E21 complete-interaction error, gives at best an allowance on
the scale (log L)/L² under (15). Even a favorable polynomial-in-height
error exp(−cL) gives scale 1/L in this unstable comparison. Fixed positive
Delta would require a bound of approximately exp(−c_Delta L²), or a
favorable sign/correlation that changes the comparison. These statements
concern this absolute-defect method; they do not assert the canonical
initial defect has a positive sign or give a lower bound on actual error.

By contrast K=(1−V)² kappa. Bound (2) keeps the D–M–forcing relation
rather than replacing it by a lower kappa alone. This is exactly why the
barrier in (3) can use polynomially small errors.

## 4. Exact heat control: initially near a clock does not retain K

For k>0 and 0<a<1 use the even physical heat family

    H(u,z)=exp(−k²u) cos(kz)+a,       H_u=H_zz,

where u is backward Newman time. It is the cosine transform of a finite
positive atomic source, not the complete theta source. It starts with an
entirely real simple divisor. Its first double events occur at

    u_c=k^−2 log(1/a),

when the cosine amplitude reaches a. After that time there are nonreal
zeros. For the short pair around π/k, set

    alpha(u)=a exp(k²u),      theta(u)=arccos alpha(u),
    D(u)=theta(u)²/k²,
    V(u)=theta(u) alpha(u)/sqrt(1−alpha(u)²).

Direct differentiation verifies D_u=−2V. At u=0 and a↓0,
V(0)=(π/2)a+O(a²), and the alternating gaps differ from π/k by O(a/k).
Thus choosing a=exp(−c k) makes the initial clock error exponentially
small in k, yet u_c=c/k still shrinks to zero. This is an exact
all-real-start heat control for the rate in the weaker comparison,
not a construction of canonical collisions.

As u↑u_c, D→0. The other zero clusters stay a positive distance from the
chosen pair for each fixed k. Their complete inverse-power sums stay
finite by the periodic inverse-square tail, so K=24D²S2+32D³S3→0.
The whole-time premise (2) with eta<1 therefore fails. Initial clock-like
geometry and generic positivity do not propagate the normalized forcing
floor. The canonical source route must supply that propagation or an
independent common-time source estimate.

## 5. What a canonical execution must pay

[Polymath source audit04][source] and E21 already provide uniform clock
localization on each fixed 0<t0≤t≤t*≤1/2, with absolute source constants
but no numerical values extracted. The lead's proposed proof can extend
E21's unit-radius head to a slowly growing physical radius R=L². The
candidate normalized local error is

    E=L X^(−c t0)+R²/X=L X^(−c t0)+L^4/X,           (16)

at high center X with L=log(X/(4π)). The first term is the uniform source
localization; the second is the Taylor curvature error of the clock G.
For n comparable to RL=L³, (10)–(11) would then give

    V(0) upper bound = O(L^−3+E),
    1−K upper bound  = O(L^−9+E),
    v=O(L^−3+sqrt(E))=O(L^−3),
    D(0)/(2v) ≥ c L,                               (17)

after increasing the starting height. The last statement is an admissible
comparison allowance within the fixed available slab, not a claim of
unlimited backward continuation. If v=0 there is no finite scalar cap.

These are proof obligations for the lead, not new imported facts. The
execution must check consecutive occurrence labels, both sides of the
pair, the effect of moving center/reference spacing, uniformity of all
onsets on the **same** slab, and the local Taylor bound across the enlarged
head. To claim a complete initial M approximation, pay the whole far
tail, expected O(1/(RL)) after normalization; to use its finite subsum as
a lower bound, positivity already suffices. No derivative of a big-O
remainder is allowed. A lower K from the positive head needs no omitted
forcing upper bound. No finite hierarchy or independently evolved finite
divisor has been substituted.

With those proofs, (17) supplies a genuine nonshrinking quantitative
comparison. The independent uniform positive-time clock theorem already
implies real/simple exterior zeros on that slab. The new result would
therefore be a quantitative strengthened consumer with matching
source-dependent coverage, **not additional all-height reality coverage
or an improved Lambda bound**. It does not reach t0=0, whose localization
onset and error have different behavior. A compact acquisition not already
protected by the source theorem remains a separate unsolved task.

## 6. Control-premise screen and recommendation

Replay [controls12][controls] analytically, retaining the canonical
premises distinguished in E21 §4. Euler-factor, weighted-square,
finite-source and finite-prime changes fail the unchanged reflected theta
source in their stated classes; endpoint-defective finite sources also
lack an all-real start. Reflected super-Gaussian and smooth/positive-
primitive controls lack the canonical arithmetic clock input. Atomic and
finite-profile controls lack the complete theta population and its
X log X growth. RH-conditional close-source controls change arithmetic
and retain RH as a premise. Variable kernels lack physical Newman
readout; fractional profiles lack integer divisor realization; static
surgery lacks common canonical heat evolution. The explicit cosine-plus-
atom control above additionally fails the whole-time K floor. The
stationary cosine control in E21 satisfies K=1 and is handled exactly.
The quadratic collision has M=F=K=0, so also fails a near-one forcing floor.

These failures do not themselves prove a canonical lower K. The generic
barrier applies to every real heat divisor satisfying its actual premises.
It makes no universal no-go claim about other forcing controls.

**Recommendation:** select the normalized K barrier, finite positive head
identity and enlarged common-time source localization for one bounded E
proof. The precise target is (17), with the coverage limitation above.
Do not select a ratio-F floor plus absolute initial-defect Gronwall as the
main mechanism: it loses the needed correlation. Do not present the
whole-time K floor as acquired until the independent source/head argument
has been written and separately assessed. E16 remains untouched.

[request]: ../research-progress/handoffs/VCD-GT-CM-B07-r3.md
[cont]: 22_VCD_GT_CM_B07_R2_SYNTHESIS_AND_CONTINUATION_20261118.md
[e21]: 21_VCD_GT_CM_E21_CANONICAL_HEIGHT_HORIZON_20261118.md
[n17]: 17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md
[hierarchy]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[source]: ../references/04_VCD_GT_CM_POSITIVE_TIME_SOURCE_AUDIT_20261118.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
