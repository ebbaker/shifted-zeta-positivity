# S05-T1: consumer fit and a bounded shifted-acquisition candidate

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Separate same-model consumer audits and replay
review; internal LLM assessment, no independent specialist human review.

**Decision:** S05-T1 is Complete as a consumer-fit selection. The existing
real parity-Taylor enclosure is not a direct fit for the inspected S01 or
S06 calls. A different existing part of S05, polynomial factoring before
source evaluation, is compatible with **S01's shifted midpoint-coefficient
acquisition**. A bounded one-coefficient experiment supports selecting that
caller for a complete comparison. It does not establish a complete
consumer improvement or a speedup.

The [overview][overview] and [tracker][tracker] explicitly update S05-T2's
route: its original parity-Taylor transfer is parked; its next selected
branch tests factoring within the unchanged shifted acquisition. The
complete-error/cost gate remains. This does not count an incompatible
parity handoff as a success or silently change its required domain.

## Contract and evidence class

Read the [result summaries][results] and [patterns to avoid][avoid],
especially [theta bookkeeping][theta], [collision controls][controls],
[normalizations][a08], [preserving cancellation][a12] and [scoped
exclusions][a07]. This is a bounded implementation-fit assessment, not an
RH-equivalent criterion or a new arithmetic identity. The polynomial
`P0(w)=w(2w-3)` and source-coordinate recurrence already appear in the
[S05 opening note][opening]. Their mathematical rediscovery is not the
claimed progress. The new evidence is their measured effect in an actual
existing acquisition call and a scoped decision about the next test.

The fit question is whether an existing source component could improve a
named complete-budget term. Whole-source parity, finite retained-mode
algebra, source derivatives and physical derivatives are kept distinct.
The [probe][probe] runs only the original coefficient j=0 at two
precisions, with the same contour, modes and tolerances. It also evaluates
128 fixed closed source cells for diagnostics. No full 51-coefficient
setup, physical signed consumer or new coverage run is executed.

## The direct real-parity handoffs do not fit

### S01: its real physical domain uses complex source data

The named caller is `WholeCellEvaluator` in the [height-1000
consumer][consumer], as used by [S01's paired-tail integration][s01].
Its physical output is `(H,Hx,Hxx)/Gc` on
`B=[1/100,1/5] x [999,1001]`, with fixed
`Gc=1000^(7/4) exp(-125*pi)`. Its source coordinate is
\[
 v=u+id,\quad 0\le u\le2,\quad
 d=\pi/8-4\log(1000)/1000\simeq0.36506806.
\]
This is neither the real near-zero cell nor the opening S05 scan at
`Im v=pi/16`. Physical derivatives multiply the integrand by `(iv)^j`;
they do not request `Phi_u` or `Phi_uu`.

The complete source parity used in S05's fixed-point Taylor estimate
cannot be imposed separately on the retained modes 1..11 or on their
omitted tail. The paired omitted-mode calculation already combines its
signed endpoints at v=id. No real `[0,h]` source-range allowance occurs
in the existing consumer's error ledger. Its directly replaceable share
for **that real parity component** is exactly zero.

### S06: point endpoints and all-half-line majorants

The secondary inspected caller is `endpoint_and_moments` in
[check_signed_transverse.py][s06-code]. It uses
\[
 g^{(r)}=\pi e^u\sum_{n\ge1}n^2P_r(\pi n^2e^{4u})
                           e^{-\pi n^2e^{4u}}
\]
through source order six. These are weighted raw-source jets. In
particular, `g'(0)=-0.372268390680...`, rather than a vanishing odd
endpoint. The caller evaluates endpoint **points** and pays its remaining
integral by analytic Gaussian/linear monomial majorants on the whole
half-line. It has no local real source-cell range budget to replace.

Fresh 192/256-bit calls reproduce its scaled sixth-order allowance
`epsilon6=0.00218954730579...`:

| Contribution | Allowance in x^2 K units | Share |
| --- | ---: | ---: |
| abs(f'''(0))/999^2 | 3.98566104e-4 | 18.2031% |
| abs(f^(5)(0))/999^4 | 1.00061974e-7 | 0.00457% |
| norm(f^(6),1)/999^4 | 1.79088114e-3 | 81.7923% |

Endpoint rounding contributes less than `1e-50` of this allowance; the
sixth-order mode tail contributes about `7.16e-98` of its L1 majorant.
These are not meaningful bottlenecks. Improving the dominant term would
require a new weighted higher-derivative integral estimate. The raw
observation also retains its already documented physical-scale mismatch.
For the completed source `C=(9-D)Phi/4`, the current implementation uses
the physical H/Hx observation, rather than direct real local-source
quadrature. That call likewise has no such range-bound component.

These are scoped fit decisions for the inspected calls, not exclusions of
future complete-source consumers. The original S05 component remains
reusable.

## Compatible candidate: factor the finite polynomial on S01's actual contour

Set `q=exp(4v)`, `lambda_n=pi n^2`, `w_n=lambda_n q`. The jth acquired
coefficient is the real part of
\[
 C_j=1000^{9/4}\int_0^2 e^{t_c v^2+v+i1000u}
 \sum_{n=1}^{11}(2\lambda_n^2q^2-3\lambda_nq)e^{-\lambda_nq}
 (iv)^j\,du,\qquad t_c=21/200.                            \tag{1}
\]
The selected candidate replaces only the finite mode polynomial by
`w_n*(2*w_n-3)`, caching w_n. It preserves the **common exponential
factor** in (1). This exact finite identity needs no parity or new tail
theorem. S01's original physical mode/source tails, normalizer,
moment/Taylor constants and whole-cell propagation remain required.

For comparison, the probe also moves exp(v) inside each summand,
giving `exp(v-w_n)*w_n*(2*w_n-3)`, as in the generic S05 source evaluator.
All three formulas are algebraically equal. Their interval enclosures
and adaptive quadrature errors need not be equal.

The Acb integrals use exactly `abs_tol=1e-13`, `rel_tol=1e-30`,
`eval_limit=200000`, `depth_limit=30` and the original `(iv)^0` factor.
The returned real coefficient radii are:

| Formula | 192 bits | 256 bits |
| --- | ---: | ---: |
| Original expanded polynomial | 2.51442361432e-13 | 2.51442358891e-13 |
| Factored polynomial, common exponential retained | **2.51257275416e-13** | **2.51257275839e-13** |
| Exponential moved inside the mode sum | 2.55265945659e-13 | 2.55265945236e-13 |

All returned balls overlap as required. Factoring alone decreases the
assigned radius by about `1.8508e-16`, approximately **0.07361% of r0**.
All three methods use 3289 callbacks at 192 bits and 3291 at 256 bits.
One-run elapsed times are diagnostics, not a matched performance result.

Both alternative formulas give narrower finite-source enclosures on all
128 actual-contour cells `[k/64,(k+1)/64]+id`, k=0..127. Exponential
grouping gives the larger width decrease, yet **worsens the actual j=0
quadrature radius**. Thus source-cell width ratios alone would select the
wrong candidate here. These line-cell images are diagnostics; the Acb
quadrature independently pays its complex-neighborhood evaluations.

## Complete-budget relevance and its limit

The existing S01 complete added error is
\[
 \epsilon_j=Q_j+T+M_j+S_j,\qquad
 Q_j=\sum_{\ell=0}^{24}\sum_{k=0}^{12}
 {R^\ell\Delta^k\over\ell!k!}r_{j+\ell+2k}.                \tag{2}
\]
Here R and Delta are distances from the physical midpoint, not source
Taylor coordinates. The S01 record's producer and **all** source pins
match before its existing ledger is used.

On the whole B box at 192 bits, `epsilon0=3.93453437e-12 Gc` and
`Q0=6.73270377e-13 Gc`, about **17.11%** of that allowance. Its common
Taylor term is `2.16483700e-12`; the paired omitted-mode term is
`1.09642699e-12`. Their unchanged floor is already `>3.26126e-12`, so
quadrature tuning alone cannot beat the stronger retained real-source
complete-error reference `<2.165e-12 Gc` using its different polynomial.
No strongest-consumer superiority is claimed.

The coefficient r0 has weight one in Q0, and is absent from Q1,Q2. If
the other 50 coefficients/radii and the remaining error terms were held
common, a reduction delta_r0 would reduce the complete value allowance
by that amount. The new C0 midpoint may change with its radius; retaining
an old midpoint with a new radius would require a separate payment.
Dividing the **fresh matched-integral** decrease by the historical complete
allowance gives the feasibility scale **about 0.004704%**. This is not a
fresh complete consumer bound or an assertion that all other coefficients
improve. It just identifies a real budget term and a compatible candidate.

The ledger's item called “source tail” covers the retained modes beyond
u=2. It is at most `1.17e-435 Gc` through order two. Even deleting that
entire unrelated term would save less than `4e-424` relatively; it must
not be confused with local source-range overestimation.

## Decision gate, review and next task

S05-T1's selection gate passes for the **finite polynomial-factoring
acquisition branch**. Park the real parity-Taylor handoffs for these S01
and S06 calls. The [budget audit][audit] and [bounded acquisition
probe][probe] retain exact inputs, outward constants and source identities.
[Separate same-model review][review] replays both precisions, source/metadata
guards and the fresh S06 budget. [Fresh inherited controls][control]
reject the five event boxes and Euler witness in the unchanged signed
consumer; this fit probe introduces no acceptance interface.

For interpretation, finite-prime and weighted-square controls do not
provide the unchanged complete theta reflection/coefficient contract;
reflected/shape/primitive controls do not supply the specific theta square
expansion; Euler controls alter level/coefficient data. Polynomial and
counter-kernel controls share generic transport but lack the theta source.
The selected factoring identity itself works for each finite mode and is
**not a collision discriminator**. No theta error allowance is assigned
to a control, and no effective event box is invented for analytic-only
families.

S05-T2 is Ready **under the explicitly recorded acquisition-route update**.
Its primary metric is complete physical added error on the same B domain,
orders 0..2, with the strongest applicable same-caller comparator. Acquire
or rigorously reuse all coefficients required by (2), retain every mode,
source, Taylor, rounding and whole-cell cost, and compare the old and
factored methods at the same settings. Retain an alternative wherever it
is tighter. If a hybrid coefficient selection is used, include all its
acquisition work and new midpoints. Cost claims still require matched
accuracy/coverage and the established factor-two threshold. No full T2
execution is implied by this selection. No new physical coverage,
noncollision region, Newman bound or manuscript snapshot is produced.

[overview]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[tracker]: ../../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[opening]: 01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[consumer]: ../../../numerics/high_height_consumer/high_height_consumer.py
[s01]: ../../01_modular_self_duality/numerics/integrate_paired_tail_consumer.py
[s06-code]: ../../06_hodge_and_transverse_geometry/numerics/check_signed_transverse.py
[probe]: ../numerics/probe_shifted_source_consumer_fit.py
[audit]: ../numerics/audit_source_consumer_budgets.py
[review]: ../reviews/02_SOURCE_CONSUMER_FIT_INTERNAL_REVIEW_20261019.md
[control]: ../numerics/S05_T1_CONTROLS_20261019.json
