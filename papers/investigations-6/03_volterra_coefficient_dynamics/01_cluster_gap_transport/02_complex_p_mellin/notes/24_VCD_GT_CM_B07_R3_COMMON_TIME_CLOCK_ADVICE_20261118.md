# B07 r3 route B — Common-time clock and a source-jet comparison

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Bounded route-B advisory helper; settings
inherited, actual serving model and effort unavailable. [B07 r3][request]
is the frozen conceptual request. Only this advisory output is owned here.

**Status: detailed proof route and quantitative advice, pending the lead's
E contract and separate assessment.** There is a concrete way to retain
the cancellation lost by the initial-M Riccati envelope: obtain spatial
jets from the complete source approximation, then use the exact heat
equation to estimate the joint gap defect. It works on a fixed positive
slab in the already localized exterior. It neither lowers that exterior's
onset nor supplies a new Lambda bound. The matched direct source enclosure
is stronger for fixed-length time intervals.

Read-first routing: [result index][results], [cluster18][cluster],
[controls12][controls], [avoid index][avoid], and
[classification01][class], [premises02][premises], [scope07][scope],
[joint12][joint]. [Continuation22][continuation], [Note21][e21] and
[E22][e22] delimit the accepted initial-data limitation. The proposed
milestone is a stronger quantitative bound on the canonical joint defect,
not another version of the endpoint target.

## 1. Checked source use and the correct analytic remainder

New selected-passage inspection on this date: Polymath v2, [§9][poly],
Proposition 9.1, Lemma 9.2 and (100)–(103); Theorem 1.5's proof and
Remark 9.4. The latter explicitly anticipates a velocity asymptotic and
says “we leave the details to the interested reader”. Its discussion is
informal; it is not an already supplied proof of the estimate below.
The [canonical catalog][catalog], [source receipt04][receipt] and
[parent bibliography][bib] retain version, DOI and external PDF ownership.
No new PDF download or bibliography copy is needed.

Work with the same complete canonical H_t, H_t=−H_zz, and
I=[t0,t1]⊂(0,1/2]. Let G be the clock from Note21 and q_n(t) its inverse:

    G(q_n(t),t)=n,
    G(x,t)=x/(4π)log(x/(4π))−x/(4π)+11/8+(t/16)log(x/(4π)).

After one uniform enlargement of the onset, the published input provides
one real simple zero ξ_n(t) near each q_n(t), exhausts high zeros and
has constants independent of t∈I. Both the index and height onsets are
paid as in Note21. This is independent of the lower divisor's reality.

For a frozen t and a high clock q=q_n(t), put

    L_q=log(q/(4π)),  λ_q=L_q/4,  κ=π/8,
    A_q=M_t((1+iq)/2),  w=z−q,
    ε_q=q^(−c t0)+L_q/q.

Here M_t is Polymath's nonvanishing carrier, not the exterior interaction
M. The notation A_q avoids identifying the two. Fix a sufficiently small
absolute r>0. All constants below may depend on this chosen r, not on t,q,n.

The proposed local representation is the following **holomorphic** one:

    H_t(q+w)=A_q exp(−κw)[2i sin(λ_q w)+E_(n,t)(w)],
    |w|≤r/L_q,              sup |E_(n,t)|≤C ε_q.           (1)

Derivation of the input for (1): source (102) has carrier exponents

    (−iw)(λ_q−iκ)=−iλ_q w−κw,
    ( iw)(λ_q+iκ)= iλ_q w−κw.

Lemma 9.2/(103) supplies conjugate(A_q)/A_q=−1+O(L_q/q).
The relative source errors and both exponentials are uniformly bounded
on this disk, with exponentials of modulus at most exp(r/4+O(r/L_q)).
Combining the two full terms gives (1). Alternatively (100)–(101) give
the same expansions directly by integrating the carrier's analytic
logarithmic derivative. The t-dependent refinement to the leading
frequency is paid in O(L_q/q); λ_q is deliberately L_q/4, not an asserted
exact phase derivative. The common factor is exp(−πw/8), with complex w.

Crucially define E_(n,t) by the exact left-hand side of (1) minus
2i sin(λ_qw). It is analytic on the disk. No assertion that a displayed
O-term is itself an analytic function is necessary, and no O-term is
differentiated without this definition and its uniform disk bound.
The weaker displayed source formula (104), with its O(|Im w|log q)
allowance, is not the appropriate derivative input; on a radius-r/log q
circle that allowance need not tend to zero. Retaining both analytic
carrier exponents in (102) avoids this loss.

## 2. Spatial Cauchy estimates give physical zero velocities

The source localization places the actual root
w_n=ξ_n(t)−q_n(t) in |w|≤r/(4L_q) for all sufficiently large n,
uniformly on I. Equation (1) then sharpens its size to

    |w_n|≤C ε_q/L_q.                                      (2)

Indeed sin(λ_q w_n)=O(ε_q), and λ_qw_n lies in a fixed small real
interval, where |sin v| is bounded below by a positive constant times |v|.
Reality here comes from the independent source zero count, not from an
assumption that the entire divisor is real.

Cauchy's formula on the radius-r/L_q disk, evaluated in the inner half,
gives the paid jet bounds

    |E'|≤C L_q ε_q,          |E''|≤C L_q² ε_q.             (3)

Set F(w)=2i sin(λ_qw)+E(w). At the actual zero,

    F'(w_n)=2iλ_q(1+O(ε_q)),
    F''(w_n)=O(L_q² ε_q).                                 (4)

The first statement uses cos(λ_qw_n)=1+O(ε_q²) and (3), and in
particular provides the denominator lower bound |F'(w_n)|≥c1 L_q.
The second uses F(w_n)=0 as well as (3). Differentiating the **exact**
representation H=A_q exp(−κw)F spatially and setting F(w_n)=0 gives

    H_zz(t,ξ_n)/H_z(t,ξ_n)=F''(w_n)/F'(w_n)−2κ
                          =−π/4+O(L_q ε_q).               (5)

Implicit differentiation of H(t,ξ_n(t))=0 and the physical heat sign,
H_t=−H_zz, gives the exact identity ξ'_n=H_zz/H_z. Consequently the
proposed quantitative velocity estimate is

    |ξ'_n(t)+π/4|≤C L_q ε_q.                              (6)

No complex-time source estimate is needed. Complex spatial neighborhoods
and the exact heat equation replace differentiation of an unknown time
remainder. The source's informal velocity remark is the attribution for
this method; (1)–(5) spell out the missing disk, normalization and
denominator payments. A smaller exponent can absorb the powers of log q
if desired, but the displayed ledger keeps them visible.

## 3. Common labels, the complete interaction and the stronger defect

The clock labels can be held fixed over I. Explicit differentiation of
G gives

    q'_n(t)=−π/4 [1+πt/(4q_n L_(q_n))]^(−1).              (7)

Their displacement over I is at most π(t1−t0)/4. The source disks move
continuously, remain disjoint and contain exactly one simple occurrence.
The implicit-function theorem therefore patches these local roots into
one C1 branch ξ_n(t) per fixed n, without permutation or a global
ordering assumption on low zeros. Choose n so the full moving disks and
their spatial buffers remain beyond the common source onset. Fixing
labels does not discard a moving physical window boundary.

Let X=q_n(t1), L=log(X/(4π)), ε=X^(−ct0)+L/X. Throughout I, q_n,
q_(n+1), L_q and ε_q are comparable to these fixed parameters. For the
adjacent high pair a=ξ_n, b=ξ_(n+1), let g=b−a and D=g²/4.
The leading velocity −π/4 cancels in (6), giving

    |g_t|≤C L ε,           |D_t|≤C ε,                     (8)

since g=O(1/L). In physical backward time u=t*−t, D_u=−D_t.

For the complete exterior interaction define

    M=Σ_(ρ≠a,b) 1/[(ρ−a)(ρ−b)],
    V=1−2DM.

When the entire divisor is real, M is the positive interaction from
Note17. Even if lower zeros are nonreal, the complete sum exists, is real
by conjugation and has the same pair identity. To justify this extension
explicitly, take the difference of the two canonical root-velocity sums
in complete opposite/conjugate groups before taking the limit:

    g_t=4/g−2g M,          D_t=2−4DM=2V.                  (9)

The surviving exterior terms are inverse-square. The accepted unit-window
count bounds their absolute far sum, including the negative/low divisor;
near denominators are nonzero by source separation. Thus no nonabsolute
single-root sum or uncomputed discarded population remains. Equivalently
the existing finite-product/count-two contour proof passes to this
strictly isolated pair before invoking any positivity. The full source
errors in (1) already retain the complete theta series; (9) is an exact
transfer, not another separately bounded head/tail approximation.

Combining (8)–(9) gives the principal target for a frozen E proof:

    |1−2DM|≤C [X^(−ct0)+log(X/(4π))/X] uniformly on I.    (10)

This is sharper than Note21's O(1/log X) complete-sum allowance. It
estimates the cancellation in the physical gap equation directly.
In a stopped all-real application it uses the same V as the proposed
joint-moment route, but does not need a separately sharp estimate of
every positive forcing term or an unproved finite hierarchy closure.

For s,t∈I, integration yields

    |D(t)−D(s)|≤C ε |t−s|,
    |g(t)−g(s)|≤C L ε |t−s|.                             (11)

A sufficient lower bound is D(t)≥D(t*)−Cε(t*−t).
The inherited source size D(t*) is of order L^(−2), whereas
ε L²→0 at fixed t0>0. Thus (11) pays any **fixed** slab duration for
all sufficiently high pairs. Its allowed duration relative to g² grows
without bound. This overcomes the particular O(g²) allowance in Note21;
it proves no extension below t0 or beyond the source-covered region.

## 4. Matched direct source comparison

The same inputs give a stronger comparison for a fixed-length interval.
Write h_n(t)=q_(n+1)(t)−q_n(t). From (2), uniformly on I,

    |g_n(t)−h_n(t)|≤C ε/L.                               (12)

This is a genuine common-time deterministic enclosure, not a statement
only at the initial slice. In particular it already gives positive gaps
when ε is sufficiently small. Differentiating the **explicit** clock
velocity v(q,t) in (7), not a remainder, gives

    v_q=−[π²t(L_q+1)/(16q²L_q²)]
          [1+πt/(4qL_q)]^(−2),
    |h'_n(t)|≤C/(X² L²).                                (13)

The mean-value theorem uses h_n=O(1/L). Comparing two times via (12)
and (13) therefore yields

    |g_n(t)−g_n(s)|≤C ε/L+C|t−s|/(X²L²),
    |D_n(t)−D_n(s)|≤C ε/L²+C|t−s|/(X²L³).                (14)

The two endpoint source errors are both included in Cε/L. For very short
times, the derivative estimate (11) is better because it vanishes with
|t−s|. For fixed-length intervals, (14) pays roughly L² less source error
than the integrated bound. One may retain the minimum of their two
allowances; neither dominates in every time regime.

This comparison is noncircular: both bounds are derived from the full
source approximation on an independently stated domain. They do not
assume a favorable gap history. Their limitation is equally precise:
the source theorem already counts real simple zeros there, so the new
dynamical estimate does not improve the known collision-free exterior
domain, numerical cutoff or upper bound on Lambda. It is useful as a
sharper source-to-dynamics input and as evidence that the previous scalar
horizon loss was due to discarded cancellation. It does not acquire the
compact exceptional region's dynamics or a time-zero statistical law.

## 5. Bounded proof/assessment scope and control screen

The justified fixed proof is (1)–(14), with target (10) and the matched
consumer (11)/(14). Inputs: the fixed positive slab; the unchanged complete
theta source and heat sign; Polymath Proposition 9.1, Lemma 9.2,
Theorem 1.5 and their uniform constants; the complete pair identity and
count convergence. Method: retain analytic carriers, define one actual
residual, apply Cauchy at separated roots, patch labels, and transfer the
velocity difference. Outputs should include the precise constants'
dependencies, spatial buffers, full pair-tail passage, fixed physical
time comparison and its direct-source benchmark. Numerical constants and
a lower-height extension are not promised by these asymptotic inputs.

This remains an advisory derivation. The lead selects the finite-head
forcing barrier as primary E23; this route is bounded supporting advice
for the same nonauthor assessment, not a separately issued execution
packet. The final assessment should check especially the
complex factor in (1), the denominator in (4), common labels and both
comparators. A separate canonical route is needed for any practical onset
gain or the compact collision region. No numerical campaign is justified
merely by (10).

Analytical control replay uses [controls12][controls] and Note21 §4.
Euler-factor changes for every relevant prime fail unchanged canonical
coefficients; weighted-square/finite-source changes fail full reflection
and, in the stated endpoint-defective class, the all-real start; reflected
and smooth/primitive controls fail exact theta arithmetic; finite-prime,
finite-profile and score matching fails the complete source import;
q/q_(T,a) controls lack that source; RH-conditional mergers change ordinary
Dirichlet arithmetic; modified kernels fail the physical cosine equation;
fractional relaxations lack an integer divisor; static surgery lacks the
common physical evolution. None of their shared shape or moment bounds
imports (1). These failures do not prove a favorable compact canonical
estimate.

The stationary cosine heat field has g_t=D_t=V=0, so it passes the
stronger derivative comparison while exposing the old Riccati loss.
The quadratic collision has M=0 and V=1, so a purported small-defect
estimate must fail near its event. Both fail the canonical source and
population hypotheses. These checks concern the equations and estimating
class, not a claimed theorem about all positive-source dynamics.

[request]: ../research-progress/handoffs/VCD-GT-CM-B07-r3.md
[continuation]: 22_VCD_GT_CM_B07_R2_SYNTHESIS_AND_CONTINUATION_20261118.md
[e21]: 21_VCD_GT_CM_E21_CANONICAL_HEIGHT_HORIZON_20261118.md
[e22]: ../reviews/11_VCD_GT_CM_E22_CANONICAL_HORIZON_ASSESSMENT_20261118.md
[receipt]: ../references/04_VCD_GT_CM_POSITIVE_TIME_SOURCE_AUDIT_20261118.md
[poly]: https://arxiv.org/html/1904.12438v2#S9
[catalog]: ../../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json
[bib]: ../../../references/induction.bib
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
