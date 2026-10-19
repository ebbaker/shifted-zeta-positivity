# S05-T2: complete shifted acquisition and consumer comparison

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Separate same-model implementation and internal
review/replay; no independent specialist human review.

**Status:** interval-checked bounded consumer comparison under the
established complete reflected-source contract. **S05-T2 is Complete for
its selected complete added-error metric.** Acquiring all 51 coefficients
shows that the selected hybrid uses exponential grouping at coefficient
order 2 and polynomial factoring with the original common exponential at
the other 50 orders. Against the stronger hybrid of the two previously
available formulas, its complete physical error allowances decrease by
more than **0.0092005%, 0.0077659%, 0.0082207%** at physical orders 0–2,
respectively, in both precision runs.

This is a small interval-evaluation improvement, not a new arithmetic
cancellation estimate. The reported adaptive paid margin is unchanged.
The raw fixed-cover lower margin moves slightly in opposite directions at
the two precisions. No margin superiority, cost advantage, new coverage,
effective exterior improvement or Newman bound is obtained.

## Frozen scope and primary metric

This executes the explicit route update in the [overview][overview] and
[S05-T1 fit decision][fit]. The original real parity-Taylor handoff remains
parked for these callers. Read the [result summaries][results] and
[patterns to avoid][avoid], especially [collision controls][controls],
[theta bookkeeping][theta], [status and evidence][a06], [normalization][a08]
and [preserving cancellation][a12]. No RH-equivalent target is introduced.

The [comparison contract][contract] was fixed before the full acquisitions,
including a stronger old-alternatives hybrid to isolate factoring's
marginal contribution. The domain and acquisition parameters are unchanged:

\[
 B=[1/100,1/5]\times[999,1001],\quad t_c=21/200,\ x_c=1000,
 \quad G_c=1000^{7/4}e^{-125\pi},
\]
\[
 v=u+id,\quad d=\pi/8-4\log(1000)/1000,\quad0\le u\le2.
\]
Retain source modes 1..11, time/spatial degrees 12/24, midpoint coefficient
orders 0..50 and the order-52 common majorant. Physical outputs are
`(H,Hx,Hxx)/Gc`; Gc is fixed and is not differentiated. The original
moment bound, high-order tails and retained-source tails are inherited
unchanged. Install the same [S01 paired omitted-mode payment][paired] in
all five evaluated representations.

The primary comparison is the **complete added approximation-error
allowance** for each physical coordinate, uniformly on all B. Physical
signed-cell tests on the same existing closed cover are secondary. They
do not turn an old-domain validation into new coverage.

## Algebra, acquisition and the stronger comparator

For `q=exp(4v)`, `lambda_n=pi n^2`, `w_n=lambda_n q`, all acquired
coefficients are real parts of the same finite integrals
\[
 C_j=1000^{9/4}\int_0^2 e^{t_c v^2+v+i1000u}
 \sum_{n=1}^{11}(2\lambda_n^2q^2-3\lambda_nq)e^{-\lambda_nq}
 (iv)^j\,du,\quad0\le j\le50.                            \tag{1}
\]
Compare the original expanded polynomial, `w_n(2w_n-3)` with the same
common exponential, and the mode-by-mode `exp(v-w_n)w_n(2w_n-3)` grouping.
These are exact finite algebraic identities, valid in the complex
neighborhoods inspected by Acb integration. No source parity, vanishing
odd endpoint or new infinite-tail estimate is assumed for this finite sum.

Each pure acquisition uses the original absolute/relative tolerances
`1e-13`/`1e-30`, integral evaluation cap 200000, depth cap 30, and complete
setup bounds of 60 seconds/2 million callbacks. The expanded baseline
runs the original constructor; the alternatives inherit its moment,
tail, Taylor and physical-consumer operations. The actual new acquisition
producer and formula are separately recorded. All 51 returned coefficient
balls are finite and agree across equivalent formulas and precisions.

Two declared selectors choose the whole `(midpoint,radius,method)` tuple
at each coefficient. The **old-alternatives hybrid** minimizes the exact
upper radius over expanded and exponential-grouped acquisitions. The
**selected hybrid** minimizes over all three. Exact ties use the declared
formula order. Both selections must retain the corresponding midpoint;
an old midpoint cannot receive an unrelated smaller radius.

At both 192 and 256 bits:

- Polynomial factoring gives a smaller radius than expansion at all 51
  orders.
- Exponential grouping is wider than expansion at 50 orders, but is much
  tighter at order 2. At 192 bits, its order-2 radius is about
  `1.923253e-13`, versus `2.596254e-13` expanded and `2.594540e-13` factored.
- The old hybrid therefore uses expanded data at 50 orders and grouped
  data at order 2. The selected hybrid uses factored data at those 50
  orders and grouped data at order 2.

The T1 order-0 probe alone did not reveal this ranking. The grouped pure
method is the strongest pure consumer after full propagation, despite
its worse order-0 acquisition. Comparing only with expansion would give
factoring credit for a larger benefit already available by using grouped
order-2 data. The two-hybrid comparison removes that attribution error.

## Complete-error proof and outward evaluation

Let exact dyadic acquired midpoints define the finite mathematical
polynomial
\[
 p_j(t,x)=\sum_{\ell=0}^{24}\sum_{k=0}^{12}
 {(-1)^k\widehat C_{j+\ell+2k}\over\ell!k!}
 (x-1000)^\ell(t-t_c)^k.
\]
With `R=max|x-1000|`, `Delta=max|t-t_c|`, the inherited complete contract
gives
\[
 |H^{(j)}/G_c-p_j|\le\epsilon_j=Q_j+T+M_j+S_j,\qquad
 Q_j=\sum_{\ell=0}^{24}\sum_{k=0}^{12}
 {R^\ell\Delta^k\over\ell!k!}r_{j+\ell+2k}.                \tag{2}
\]
The value, derivative and time coefficients come from the same signed
finite source. T pays the original finite-integral Taylor remainder, M
the omitted arithmetic modes, and S the retained source beyond u=2.
The infinite-source reflection and analytic tail contract precede finite
truncation. There is no extra physical source cutoff or floor derivative.

All weights in Q are nonnegative. Selecting smaller valid coefficient
radii can only decrease this allowance, with a strict decrease whenever
a strictly improved coefficient has a positive weight. Exact dyadic
midpoints and upper radii, the full common data and the selected tuples
are retained. Outward arithmetic pays the sums in (2).

The numerical image of p is separately evaluated by outward interval
arithmetic, including factorial reciprocals, coefficients and time/space
variation. The actual consumer adds the interval error `[-epsilon_j,
epsilon_j]` to that image. A reduction of epsilon is a reduction of the
mathematical approximation-error allowance. It is not necessarily a
reduction of the final interval radius, which also encloses variation of
p over its physical cell.

## Complete quantitative result

The following upper ceilings hold in both precision runs. Units are
`1e-12 Gc` for the error in the indicated physical derivative. These are
uniform whole-B allowances, not point samples or actual errors.

| Acquisition or selector | Value | First derivative | Second derivative |
| --- | ---: | ---: | ---: |
| Expanded | <3.934534374 | <3.218758246 | <2.964412231 |
| Polynomial factored | <3.934074108 | <3.218342162 | <2.964002723 |
| Exponential grouped | <3.902346952 | <3.157130992 | <2.902534759 |
| Stronger old-alternatives hybrid | <3.894490817 | <3.151458150 | <2.897112135 |
| Selected three-alternative hybrid | **<3.894132500** | **<3.151213409** | **<2.896873971** |

The interval ratios themselves, not differences of rounded table entries,
give the complete marginal factoring gains quoted above. At 192 bits the
absolute decreases against the old hybrid are approximately
`(3.583178,2.447405,2.381639)e-16 Gc`. Against the strongest pure grouped
formula, the selected hybrid decreases the allowances by more than
`0.2104%,0.1874%,0.1950%`. Only the smaller two-hybrid gains are attributed
to adding factoring to the prior alternatives.

The unchanged nonquadrature floor for the value is `>3.26126e-12 Gc`.
The stronger retained real-source reference `<2.165e-12 Gc`, using a
different polynomial and higher-precision setup, remains unbeaten.
This comparison does not establish a new strongest physical error.

## Physical consumer and cost

All five representations pass the same **40 closed cells** covering B,
with the time/slab boundaries and spatial cover checked. The original
adaptive algorithm retains its geometry and **116 calls** in every case.
The minimum reported adaptive excess `(L0-E/100)/Gc^2` is identical
between the two hybrids at each precision, and remains `>8.2608772e-5`.

The directly extracted fixed-cover lower margin changes at a much smaller
scale: at 192 bits it is about `8.91296564757e-5` for the old hybrid and
`8.91296528377e-5` for the selected hybrid; at 256 bits the direction is
reversed. The smaller approximation-error allowance therefore gives no
consistent paid-margin increase. These direct lower endpoints also use
a different serialization convention from the historical adaptive
summary, which reparses printed interval balls. Their larger printed
number must not be presented as an acquisition gain.

For the executed selection comparison, the old hybrid charges both prior
full acquisitions and the selected hybrid charges **all three**, including
their original common setup and paired-tail work:

| Precision | Expanded callbacks | Factored callbacks | Grouped callbacks | Old-hybrid charged callbacks | Selected-hybrid charged callbacks |
| --- | ---: | ---: | ---: | ---: | ---: |
| 192 bits | 173696 | 173696 | 173724 | 347420 | 521116 |
| 256 bits | 173798 | 173798 | 173826 | 347624 | 521422 |

Host timings, per-coefficient acquisition work, common setup, paired-tail
setup and physical-consumer times are in the records. They are descriptive
single-run costs. The selector pays extra acquisition work and earns no
factor-two matched-cost claim. A future fixed production policy could
choose the observed 50+1 recipes in advance; that future cost is not
measured here and is not substituted for the executed selector's cost.

## Validation, controls and stopping decision

The [192/256 records and implementation][numerics] retain all 51
coefficient tuples for each pure acquisition, both selectors, common-data
fingerprints, complete ledgers, fixed physical images and adaptive
summaries. Historical source/producer pins, current code pins, contract
identity, metadata and coverage guards fail closed. The [separate
same-model review][review] supplies fresh full replays and mechanism
checks. This validates an implementation comparison under the imported
analytic source theorem; it does not independently prove that theorem.

Fresh source-specific controls reject five event boxes and the Euler
negative-Laguerre witness through the unchanged actual signed consumer.
The paired-tail invalid-parameter and non-even vertical-boundary fixtures
also pass. Altered sources receive their own errors. Finite-prime and
finite weighted-square controls lack unchanged complete theta reflection
and coefficient data; reflected/shape/primitive controls lack the specific
theta square expansion; Euler controls change the level/coefficient data.
Polynomial and counter-kernel controls share generic identities without
the complete theta source. Factoring the finite polynomial itself is
available to weighted modes and is not a collision discriminator. No
event box is invented for an analytic-only control.

**Decision:** complete S05-T2 at the declared complete added-error gate.
Retain the bounded evaluator/selector and its stronger comparators. Stop
this fixed B acquisition comparison: it gives a small paid-error decrease,
while the physical-margin, matched-cost and coverage objectives are
unachieved. The real parity-Taylor component stays reusable and parked for
the inspected callers. A further S05 continuation needs a named new
consumer or a material error/cost objective. EXT-01 remains Conditional;
no expansion is activated by this implementation result. The real bridge,
complex exterior and global physical sign remain open. No manuscript
snapshot is created.

[overview]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[fit]: 02_SOURCE_CONSUMER_FIT_AND_SHIFTED_ACQUISITION_SELECTION_20261019.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a06]: ../../../../../../avoid/06_status_stronger_than_the_evidence.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[contract]: 04_S05_T2_COMPARISON_CONTRACT_20261019.md
[paired]: ../../01_modular_self_duality/notes/02_COMPLETE_PAIRED_TAIL_CONSUMER_AND_STOPPING_DECISION_20261019.md
[numerics]: ../numerics/README.md
[review]: ../reviews/03_COMPLETE_SHIFTED_CONSUMER_INTERNAL_REVIEW_20261019.md
