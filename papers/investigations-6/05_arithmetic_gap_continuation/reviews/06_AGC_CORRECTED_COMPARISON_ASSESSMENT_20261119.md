# AGC-E12 r2: nonauthor corrected-comparison assessment

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Reviewing helper retains the explicit dispatch
**gpt-6.1-sol / ultra**; independent actual serving-backend model/effort
attestation was unavailable.

**Accepted within the frozen fixed-cell numerical implementation scope.**
One full code/source-to-implementation assessment, one final-script scratch
replay and one saved-endpoint/integration correction check completed.
No blocking mathematical or implementation finding remains.

This accepts the [new script](../numerics/agc_corrected_reference_comparison.py),
[Record05](../numerics/05_AGC_CORRECTED_REFERENCE_COMPARISON_20261119.json),
[Note11](../notes/11_AGC_E12_R2_CORRECTED_COMPARISON_20261119.md)
and the corrected numerical subsection/table in
[manuscript Section 9](../manuscript/sections/09_corrected_reference.tex),
under [E12 r2](../research-progress/handoffs/AGC-E12-r2-request.md).

## Ownership and scope

The assessor did not author this numerical program, record, note or
manuscript integration. The assessor did author E10 note04, E13 r1 note08,
the old numerical Review04 and the accepted correction-source Review05.
That overlap is disclosed: this is separate numerical implementation
checking, not independent validation of the assessor's previous work or
the imported source theorem. The author of correction Note10 is a
different contributing agent. All checking remains internal LLM work,
with shared premises and no attested cross-model or specialist review.

The accepted analytical inputs are
[Note10](../notes/10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md) and
[Review05](05_AGC_CORRECTED_REFERENCE_ASSESSMENT_20261119.md),
the complete source Note06 with
[Review03](03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md), and the
previous source/consumer/numerical interfaces. The
[result index](../../../../result-summaries/README.md),
[patterns index](../../../../avoid/README.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [04](../../../../avoid/04_counts_and_precision_as_evidence.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
apply.

The question is a complete allowance comparison on the unchanged
already-covered cell. It does not establish new height/time coverage,
a Newman bound, an actual change in the zeros or a transport advantage.

## Full implementation pass

**Frozen inputs and provenance.** The r1 program and Record03 are checked
against their accepted byte hashes before import. The new program imports
their constants and elementary numerical routines without calling the old
main routine. It uses only the frozen 192-bit, 64-time-cell, 512-arc
geometry and the three radii $4/5,9/10,1$. The natural-cutoff inequalities
are rechecked for $N=33$ on the same rectangle. No adaptive refinement,
new height/time, source change or derivative-constant optimization is used.

**Correction formula and constant scale.** The implementation evaluates
the two analytic formulas for $C_0$ and $C_0^\sharp$ with conjugated
coefficients. It does not conjugate the complex input as a numerical
substitute for the holomorphic sharp function. Every evaluated box
checks the accepted $p$ strip and denominator clearance. Principal
square roots remain in the accepted positive-axis patch.

The scaled correction factor
$(-1)^{34}\sqrt\pi\,\exp[k(X-z)-k^2t]/4$ is exactly
$\mathcal S J_N$, with the same constant
$\mathcal S=\exp(\pi X/8)$ used for the physical $P,H,E,R$.
Subtracting this correction from the old scaled finite reference
therefore gives the intended $Q_{33}$ without a new normalization
equation or an omitted scale derivative.

**Complete corrected source allowance.** The code retains both
33-term replacement-error sums, evaluates the complete retained
$L(\delta_-+\delta_+)$ remainder and adds
$12000|J_{\rm scaled}||y|$. It evaluates that sum directly; it does
not subtract two independently enclosed old bounds and call the result
an error. The leading omitted $1$ has been replaced only after paying
the full accepted vertical mismatch. Negative heights use the physical
conjugation-compatible formulas. The unchanged source domain and cutoff
remain valid on the count circle.

The code acquires the new denominator on the same closed space/time
arc as the source allowance. The local maximum of their ratios is used
on both compared $Q$ readouts. The looser ratio of independent global
supremum/infimum bounds is kept only as context.

**Defect payment and its precise scope.** The old reference defect
is evaluated as its full finite complex sum before taking its modulus.
The additional correction payment uses the accepted
$|A''|<1400$, giving the valid upper bound

\[
|R_{Q,\rm scaled}|
\le |R_{P,\rm scaled}|+350|J_{\rm scaled}|.
\]

The program and record explicitly identify this as a conservative
triangle bound, not an exact signed complex $R_Q$ enclosure or
favorable cancellation. Its acquired contour bound is below
$357.797450$. Note11's separate full-rectangle bound below
$26508.082276$ follows from the pinned old full-rectangle defect
bound plus the accepted $|J_{\rm scaled}|<1$; no additional domain
evaluation is claimed. The final gap calculation is an endpoint value
consumer, so it does not consume a heat integral or omit heat boundary
data from such a claimed integral. No second scalar heat comparison is
asserted.

**Closed covers and direct new count.** The same exact rational time
partition and closed angular arcs used by the accepted r1 primitives
cover every slice and circle point. The interval boxes include their
endpoints. The code directly checks
$\Re(Q_{\rm scaled}/(z-X)^2)>0$ on all three circles; it does not
substitute the older $P$ count transfer for that acquisition.
The middle circle therefore has reference count two and clearance.
Positive real part on both annular boundaries propagates through the
annulus by the harmonic minimum principle and gives one principal
holomorphic logarithm there.

**New moments and aliases.** The sampled logarithm is that of
$Q_{\rm scaled}/(z-X)^2$. The two radius-weighted Laurent trapezoids
have exactly the same positive and negative alias ladders as in
Review04, now with the new logarithm's boundary bounds. Both tails have
the correct exponent $512$, radius power $k=1,2$ and geometric
denominator. The alias disk is safely contained in a coordinate
rectangle. Both coefficient allowances are below
$5.79\cdot10^{-23}$. Arithmetic and the entire time-cell variation
are retained at every node; there is no unpaid interpolation or
time quadrature.

The own-reference formulas
$c_Q-X=-a_{-1}/2$ and
$D_Q=-a_{-2}-a_{-1}^2/4$ retain the complete complex square,
center uncertainty and alias errors. Exact symmetry makes $D_Q$
real; all recorded imaginary inclusions contain zero.

**Matched complete comparisons.** The old E10 and refined E13
allowances use identical newly acquired $Q$ source, denominator,
center, count and discriminant enclosures. The E10 baseline is the
stronger square-root-offset formula. The refined formula is the minimum
of the accepted Cauchy and parabolic bounds, with $\eta<2$ checked
before the latter is used. Both are subtracted from the same full
reference-discriminant enclosure.

The separate comparison with the older $P$ lower envelopes uses the
pinned Record03 rows on the corresponding time cells. It is a comparison
after acquiring correction information, not a comparison between
unequally informed transport and direct representations.

## All-time results and integration check

The saved endpoints support these exact-rational outward statements on
every one of the 64 closed time cells:

| Object | Paid bound |
| --- | ---: |
| Corrected local ratio | $q_Q<0.015234762$ |
| Corrected denominator | $m_{Q,\rm scaled}>941112.53$ |
| Complete corrected source allowance | $V_{Q,\rm scaled}<21410.476$ |
| Own reference discriminant | $D_Q>0.1617006119$ |
| Strong E10 transfer allowance at $Q$ | $B_{\rm E10,Q}<0.012511448$ |
| Refined transfer allowance at $Q$ | $B_{\rm ref,Q}<0.012369746$ |
| E10 complete lower allowance at $Q$ | $D_H>0.1491891639$ |
| Refined complete lower allowance at $Q$ | $D_H>0.1493308659$ |

Every direct count/annulus/q gate passes. Every refined lower envelope is
positive, strictly improves the E10 envelope for the same $Q$ inputs,
and exceeds the corresponding previous refined $P$ lower envelope.
The previous uniform lower allowance is
$>0.005414730535$. Reference moments and all numerical payments have
changed with $Q$; the smaller source budget is not spent at $P$'s
old center.

Rouché and the complete $q_Q<1$ source enclosure give count two for
$H$ on the fixed circle, on every slice. Conjugation and the positive
discriminant make this the real distinct pair there. The manuscript's
gap consequence is correct:

\[
(0.7728)^2/4=0.14930496<0.1493308659,
\]

so the real gap is **greater than $0.7728$ throughout the stated
interval**. This is a stronger sufficient lower bound for the same
unchanged canonical pair within known coverage.

The manuscript's numerical table, complete source/denominator summary,
conservative defect statement, no-new-heat-comparison wording and
known-coverage interpretation agree with the final record. Equally
informed direct $Q$ evaluation receives every correction/source/count
input and the same refined estimator. No representation, runtime or
global coverage advantage is established.

## Sole scratch replay

Pinned final scientific inputs:

| Artifact | SHA-256 |
| --- | --- |
| New script | 3a072c16aa929f6344a779d2bcb487898b27ba3d000a5a8c30b6b845d3e81166 |
| Canonical Record05 | d15913856684a5ebf2d85134585da371b70b84e3113a327c342f17ad2f21dba1 |
| Unchanged r1 script | 9c6b6fd6f19cd716582f1569cea0d38ba0da3c7a3a2a4847bac78242d3160cda |
| Unchanged Record03 | 6f97ba677fd59382dae07ef185e6ab51352a1aae952c761c230a918b3628fb05 |

The sole replay used the final script's output-path option to write
outside the repository. Python 3.10.0, python-flint 0.9.0, 192-bit
precision and all mathematical inputs were unchanged. It completed in
**84.20122508297209 seconds**.

The scientific JSON payload matched canonical Record05 **exactly** after
excluding only elapsed-seconds fields. Interval strings, source hashes,
all 64 rows, complete bounds, comparison flags and uniform summaries
agree. All four pinned canonical byte hashes above were unchanged before
and after replay. The scratch JSON hash is
67d0c78474115d4043233eb1d4e88eee8f13d6d5b39e3eca8e7a778605b946b8.
The different byte hash reflects elapsed runtime only. Scratch JSON,
log and receipt remain outside the repository. No second replay was run.

## Single correction check and limits

The correction check read final Note11 and the appended manuscript
subsection, then checked the existing saved endpoints at 192 bits
against exact rational targets. All table bounds, the conservative
contour/full-rectangle defect statements, gap-square identity, every
new-versus-prior lower-envelope comparison, all imaginary inclusions,
aliases, source hashes and final gates passed. The old/new time-cell
definitions are identical closed rational partitions. No source
evaluation, refinement or new numerical question was added by these
endpoint checks. No mathematical or documentation correction was
required.

The exact quadratic collision still has zero error but zero strict gap
margin at its event. The literal theta source budget is not assigned
unchanged to modified-source or changed-kernel controls; the analytical
screen and its scoped failed premises remain as in accepted Note10 and
Review05. There is no new control-family numerical replay.

The accepted result is this finite complete-margin gain after retaining
the holomorphic correction. It does not independently verify the source
theorem, extend the local branch/cutoff patch, pass to time zero or
infinite height, improve the Newman bound, or establish a transport/direct
cost ordering. Only this review and its assigned return were written by
the assessor; all canonical scientific files remain untouched.
