# Progress assessment: investigations 3

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; effort: **ultra**.
Three same-model collaborators reviewed separate parts of the portfolio.
This is an internal synthesis, not independent specialist validation.

## Overall judgment

**The portfolio has made substantive progress, and its strongest positive
lead is now the combined Dirichlet-family and transport program, 01+03.**
It has an arithmetic estimate that is actually consumed by a zero-strip
comparison. The sharp finite-sum program, 02, is the strongest near-term
certificate-completion opportunity. The other investigations have produced
useful estimates and precisely scoped obstructions, but do not presently
supply comparable progress toward an improved global bound.

That is a meaningful change from the [initial portfolio plan][plan]. Its
opening family contract has become a proved comparison in the sources;
the feared confinement gap is bypassed; the effective outer program has
found a useful family application; and the finite-row workload may be much
smaller than originally expected. The negative results are also more
informative: 05 identifies construction classes that fail even on a known
stable source, while 07 explains why finite changes of the theta source can
be arbitrarily close locally yet have radically different global zeros.

This assessment follows the [result summaries][results] and
[patterns to avoid][avoid], especially [01][a01], [02][a02], [07][a07],
[12][a12], [15][a15], [19][a19], and [20][a20]. A positive-time bound is a
quantitative milestone. A global zero-time positivity criterion can still
be RH/GRH-equivalent. An exact identity earns further development when it
enables an estimate, not merely another equivalent formulation.

## Scope and evidence

The baseline was repository commit `bed1dac7307626385c98bf210e326999c07ae9f1`,
with a clean working tree before this chat's history registration. The
review covered the root avoid/result-summary collections, the portfolio
plan, and all seven investigations through their manuscript sources,
substantive reviews and continuation notes. Delegated readings were
read-only. The [manifest](SOURCE_MANIFEST_20261017.json) identifies the
survey's source set; it is not a claim that every numerical program was
rerun or every proof was independently reconstructed.

The user noted ongoing integration in 02. This assessment reads the
activation result directly in its review and distinguishes it from a
completed floor certificate. It also reads the latest 04, 05, and 07
results in their notes, rather than treating their dated manuscripts as
complete accounts of the current state. No heavy certificate campaign was
launched for this assessment.

## Results and decisions by investigation

| Investigation | Strongest current contribution | Evidence boundary | Recommended position |
| --- | --- | --- | --- |
| **01 Dirichlet Newman families** | Sine-tail comparison without original-flow H12; all primitive q>=10^12 have Lambda_chi<=0.27; conductor rate O((log q)^(-4/7)) | In manuscript/notes; another GPT model reviewed the main chain. New appendices have authoring checks. No specialist review or priority conclusion | Develop jointly with 03 |
| **02 Sharp finite-sum bounds** | Sharp pairing, all four strip-transfer legs, one positive row, complete error allowance and infinite tail; review supplies an activation lemma | Cross-model review accepts the round-one mathematics. Approximately 20 anchors is a floating plan; complete finite floors remain open | Finish bounded certificate before parameter expansion |
| **03 Effective outer remainders** | Complete transport budget gives S_chi(x,3,t)>6 for all x and t in [0,1/4], q>=10^12; finite restart gives Lambda_chi<=0.215 | Round-one cross-model review; round-two proof and certificates have same-model audits. Near-threshold tables and derivative circles remain uncertified | Highest analytic priority with 01 |
| **04 Sonin mixed-prime response** | Exact complete mixed response, compact source transfer; sharp metric threshold and endpoint essential norm | Round one cross-model reviewed; round two same-model checked. No improved complete sign or residual margin | Dormant estimate campaign; retain the operator results |
| **05 Constructive stable models** | Scoped independent-spin, quartic, persistent-site and diverging-heat exclusions | Main exclusions also reject stable Bessel. Round two extends scopes but has same-model checks | New construction must pass a stable reverse control first |
| **06 Explicit heat zero counts** | K_t(X)<=0.9 log(X+2)+6 for 0<t<=1/2, X>=100000 | New cutoff/extraction same-model checked; earlier weaker count cross-model reviewed. No demonstrated consumer gain | Supporting tool; freeze optimization until a consumer exists |
| **07 Source-measurement audit** | Finite perturbations have nonreal zeros at every heat time; one direction produces collisions in sufficiently high gaps at each fixed t>0 | Nonnegative finite reflection-breaking class; fixed-time cutoff. Latest one-direction proof same-model checked | Consolidate as approximation/conditioning result; use to design error budgets |

### 01 and 03: an estimate and a transfer finally meet

Project 01's essential advance is the [real sine-tail construction][p01n].
Finite canonical products alone lose the global logarithmic-derivative
floor. Adding a real zero lattice supplies a usable exterior floor while
the central region converges to the intended function. Each approximant
has confined nonreal zeros, so a compact first-contact argument applies;
controlled heat convergence then transfers the conclusion to the original
function. H12 for the original character flow remains open, but it is no
longer a premise of these results. Complex characters need real-entire
normalization, not evenness; that distinction is retained.

The [latest mathematical review][p01r] found no substantive defect in the
main comparison and its two applications. Its scalar replay validates the
finite inequalities consumed by that proof. It does not convert earlier
zero-loss planning tables into theorems. The [review response][p01response]
also correctly identifies 03's 0.215 as the stronger finite benchmark.

Project 03 supplies the missing sustained arithmetic floor. Its
[round-two envelope][p03floor] pays for the complex Gaussian denominator,
ordinary and reflected tails, arbitrarily small positive times, both
parities, and the unbounded height/conductor range. Its [restart lemma][p03restart]
uses that floor at original time slices, rather than assuming that the
non-character approximants inherit the arithmetic for a long interval.
This is why the result is more than a formal transport identity.

The [latest audit][p03r] checks the analytic domination as well as replaying
the two scalar outputs, but is same-model review of the round-two work.
It also flags lagging manuscript passages. The separate zeta value
0.18891 still depends on external analytic estimates and the stated
boundary computation. It is not an unconditional result of the family
certificate. The floating conductor thresholds near 1.1e5 and 4.9e4 do
not inherit the q>=10^12 certificate.

**A further deduction emerges from reading the two projects together.**
The 03 error envelope is uniform for every ell>=25.8. It allows the main
floor to retain its conductor dependence:

\[
 C(q)=\frac{\log(q/\pi)-\gamma}{4}-\frac{77}{200}.
\]

The finite-restart lemma then yields, with k(q)=4C(q)/3-1,

\[
 \Lambda_\chi\le \frac{\log(1+k(q)/2)}{k(q)}
 =O\!\left(\frac{\log\log q}{\log q}\right),\qquad q\ge10^{12}.
\]

The [short proof saved with this assessment][corollary] uses only finite
partitions followed by an endpoint limit. It is a new source-dependent
deduction in this assessment, with same-model checks, not a new independent
audit of the inputs or an upgraded manuscript claim. This rate is also
suggested in an earlier [public discussion][mo]; no novelty is asserted.
The important next task is analytic review and integration, not another
conductor grid. It materially improves the rate furnished by the current
repository arguments.

### 02: a realistic completion task, with a clear limit to further tuning

At t=0.157 the sharp first-row margin is about 0.00177553. The complete
approximation allowance is below 2.829444e-7, and the infinite-tail budget
closes with head 600000. The active-branch gate covers all four finite
legs. These are real gains over a triangle estimate that discards the
pairing. They do not yet establish the target Lambda<=0.1745354.

The decisive recent result is [Claude Review 01, §3][p02r]. Its seminorm
activation lemma propagates one certified anchor to a run of indices;
the divisor majorant cancels in the activation payment. The floating
greedy plan uses 4, 5, 5 and 6 anchor rows on the four legs. This replaces
the expectation of millions of separately evaluated rows by a small
bounded certificate task **if** the lemma, anchors, payments and interval
coverage all check. The twenty-row number is a plan, not a completed
certificate or a theorem about minimal computational cost.

The acceptance condition is explicit: at every index in the remaining
finite bridge, the anchor floor minus an outward activation allowance
must exceed 3e-7. The transfer, approximation, inherited initial
verification and barrier imports, and infinite tail must then be assembled
into one coverage statement. The [current manuscript][p02ms] retains its
conditional conclusion. The criterion being consumed is the full
[Polymath Theorem 1.2][polymath], not just its final-time exterior hypothesis.

The review also finds that t=0.157 is only about 1e-4 above this first
row's own boundary. Reduction past that boundary needs a changed mollifier,
height or estimate, with renewed transfer and coverage work. Finish the
existing target before optimizing that frontier. Separate host resource
guards from mathematical gates: a slower replay is not a counterexample
to a correct inequality. No claim of a globally best public bound should
be made without a separate current comparison of competing claims.

### 04: cancellation clarified, but no useful sign obtained

The [round-one manuscript][p04ms] keeps the compressed inverse metric in
the exact response and identifies the complete mixed response with the
mixed return. Its compact source-transfer theorem gives a useful finite
approximation contract with a controlled complement. The correction to
the literal translate-span claim matters: changing places is not the same
as translating the prepared source, already at first order.

The [round-two note][p04n] sharpens the metric analysis. For
a=|log(p/q)|, boundedness holds exactly for L<=a. After explicit arithmetic
subtraction the remainder is compact for L<a, and at L=a has essential
norm pi beta_p beta_q/8. The full metric remainder can retain noncompact
arithmetic shifts below threshold. Above threshold the separated metric
term has both unbounded signs, even though the complete mixed form is
compact. This is evidence to preserve cancellation before estimating.

The return expansion and cubic error are also useful. Their generic
bound still holds for the tilted projection control and therefore does
not supply a Sonin-specific sign. Reopening requires a named complete
residual budget and an actual-Sonin mixed estimate that improves it.
The current identities alone do not do that. Conversely, they do not
exclude all collective prime estimates; the reconciliation explicitly
preserves that possibility.

### 05: strong family exclusions, not evidence against theta stability

The [reviewed round-one record][p05r] excludes independent cosine products,
specified quartic and Bessel-multiplier classes, independent pure-quartic
arrays with a Gaussian component, and interacting quartic networks with
a persistent diffuse site at readout scale. The stable Bessel source is
the crucial reverse control: several of these tests reject it too. They
measure the expressive limits of the proposed families.

[Round two][p05n] goes further than the retained manuscript. Weak closure
extends the persistent-site result. Fixed rollback excludes independent-spin
preparation at every nonpositive base time, including times tending to
minus infinity. The separate Newman-class argument excludes theta and
Bessel from limits of diverging heat tilts of general symmetric LP seeds.
These extensions have same-model checks and named classical dependencies.

General interacting infinitesimal arrays and fixed non-Gaussian Cardon
multipliers remain outside the established exclusions. That is a statement
of scope, not a reason to launch broad fitting. A nominated construction
must first approximate a known stable Bessel/Pólya target and then identify
a theta-specific estimate. Matching a finite list of moments or the leading
h log h field-growth scale does not meet that requirement.

### 06: a useful bound whose next application must be specified

The [current manuscript][p06ms] incorporates the improved cutoff and
conjugate-pair/Schwarz–Pick extraction. The new result is

\[
 K_t(X)\le\tfrac9{10}\log(X+2)+6,
 \quad 0<t\le\tfrac12,\quad X\ge100000,
\]

with the additive 11/2 improvement for X>=2000000. Its predecessor was
(6/5)log(X+2)+22 from X>=2000000. The new proof has [same-model checks][p06r];
the earlier weaker theorem received cross-model review.

This is a local **upper** count of complex zeros with multiplicity. It
supplies neither a lower population nor exact zero counts, simplicity,
reality, or lower bounds on velocity denominators. It cannot fill a
family-attraction hypothesis by changing log X to log(qX). A sensible next
consumer is an absolutely convergent omitted-zero tail or a finite
off-axis comparison, with a stated tolerance. Continued constant tuning
without such a consumer is unlikely to be the best use of effort.

### 07: a substantial instability result and a guide to valid approximation

The original audit separated a sufficient nonvanishing radius from an
actual feasible collision distance. Its large distance ratios were at
six **prescribed abscissae**. They did not rule out a much nearer event
somewhere inside a surrounding zero gap. The [reconciliation][p07n1]
restores the nonvertical-vector hypothesis of the gap lemma and certifies
one positive alignment near x=44.1060084240846 at t=1/4.

More decisively, every nonzero finite theta-tail change with nonnegative
resulting source, and every nonzero nonnegative finite zero-tail source,
has finitely many real and infinitely many nonreal zeros at every real
heat time. The uncancelled endpoint produces an algebraic real-axis tail.
In particular the weighted-square controls' certified collision times
are not finite thresholds above which all zeros are real.

The [newest note][p07n2] proves that one fixed nonzero finite direction
already produces a unique nondegenerate ratio event in every sufficiently
high theta-zero gap, at **each fixed** t*>0. The cutoff depends on t*;
there is no t*=0 or uniform-small-time assertion. Its 264/269 tail heights
are sufficient envelope thresholds for two fixed error conventions, not
the first heights at which zeros disappear.

These are valuable approximation-class theorems. They do not invalidate
accurate finite-domain approximations, nor exclude reflected, infinite
or height-dependent designs. They do exclude the idea of obtaining a
globally stable seed by a nonzero finite nonnegative theta-mode change.
The productive lesson is to certify the complete error against the
actual margin on the stated domain, not infer global stability from a
finite absolute measurement tolerance.

## Recommended allocation and closure

Keep two substantive developing tracks: **01+03 together**, and **02**.
For the former, review the stronger conductor deduction and the complete
uniform envelope, then choose a lower-conductor or genuinely stronger
comparison target. For the latter, finish the activation certificate and
assemble its dependencies. These are different deliverables and should
not be confused with progress toward zero-time RH.

Use 06 as a supporting estimate when a consumer names its error tolerance.
Consolidate 07's corrected scope and current theorem before adding new
measurement designs. Keep 04 and 05 dormant pending their stated reopening
inputs. Dormancy is a resource judgment, not a universal impossibility
theorem. The [direction memo](02_RESEARCH_DIRECTIONS_CODEX_20261017.md)
states concrete questions for each possible continuation.

The most urgent documentation work is modest: route the portfolio opening
table to this current assessment; integrate 02's review result without
calling its planned mesh a finished certificate; and retain explicit
round-two pointers for 04/05/07. The new conductor corollary should enter
the canonical manuscript only after focused review. Another large
manuscript expansion is unnecessary for the immediate decisions.

[plan]: ../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a15]: ../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
[a19]: ../../../avoid/19_status_files_that_lag_the_findings.md
[a20]: ../../../avoid/20_volume_without_a_gain.md
[p01n]: ../01_dirichlet_newman_families/notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md
[p01r]: ../01_dirichlet_newman_families/reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md
[p01response]: ../01_dirichlet_newman_families/notes/round-4/04_REVIEW_RESPONSE_AND_SIBLING_BENCHMARK_CODEX_20261017.md
[p02r]: ../02_sharp_finite_sum_bounds/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[p02ms]: ../02_sharp_finite_sum_bounds/manuscript/sharp_finite_sum_bounds/main.tex
[p03floor]: ../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md
[p03restart]: ../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md
[p03r]: ../03_effective_outer_remainders/reviews/03_FAMILY_FLOOR_AND_RESTART_AUDIT_CODEX_20261017.md
[p04ms]: ../04_sonin_mixed_prime_response/manuscript/sonin_mixed_prime_response.tex
[p04n]: ../04_sonin_mixed_prime_response/notes/round-2/01_REVIEW_RECONCILIATION_AND_SHARP_METRIC_THRESHOLD_CODEX_20261017.md
[p05r]: ../05_constructive_stable_models/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[p05n]: ../05_constructive_stable_models/notes/round-2/README.md
[p06ms]: ../06_explicit_heat_zero_counts/manuscript/explicit_heat_zero_counts.tex
[p06r]: ../06_explicit_heat_zero_counts/reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md
[p07n1]: ../07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md
[p07n2]: ../07_source_measurement_audit/notes/round-2/02_ONE_DIRECTION_GAP_COLLISIONS_AND_TAIL_BUDGET_CODEX_20261017.md
[corollary]: notes/01_CONDUCTOR_RATE_FROM_UNIFORM_FLOOR_CODEX_20261017.md
[mo]: https://mathoverflow.net/questions/515667/do-de-bruijn-newman-constants-of-dirichlet-l-functions-tend-to-0-as-the-cond
[polymath]: https://arxiv.org/html/1904.12438v2
