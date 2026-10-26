# Manuscript placement and consolidation review

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), actual effort max**,
verified from the current session's metadata. Parent chat0023,
thread `01a17957-144d-71f3-9efc-069a2698f4ec`.

**Recommendation: update the base manuscript as the main synthesis of
the investigation, with clearly scoped technical companions.** The new
positive-time hierarchy belongs technically in the ansatz manuscript;
the recurrence manuscript should retain its focused negative-time
approximation/evaluation argument. The base paper should explain what
both branches contribute to the physical program and what remains to
be transferred. Combining folders is not a mathematical joining theorem.

This is an internal editorial and theorem-contract review, including
selected source-level checks. It is not a line-by-line audit of all three
papers, independent specialist validation, or HDA-20. The new positive
notes retain **proved in-note from named inputs; same-model internal
assessment only** as their source status. This different-model reading
does not replace their inherited contour/classical premises with an
independent proof. No mathematical research status is upgraded.

## 1. The manuscripts serve different purposes

| Manuscript | Present content | Recommended continuing role |
| --- | --- | --- |
| [Base](../manuscript/main.tex), prior build 112 pages | Global regulated potential/density/current/covariance construction, exact joining defects, both infinite-time endpoints; integrated through parent Notes54–55 | Main synthesis and primary reader entry. Own the global physical construction, its source/evaluator improvements, and a current map of all regional field theorems. |
| [Ansatz](../ansatz/manuscript/main.tex), prior build 33 pages | Evolution/error identities, older negative-time corrections, through-zero comparisons, positive carrier and physical-layer framework; integrated through Ansatz Note12 | Technical home for the positive-time hierarchy and regional asymptotic bridges. Replace obsolete current-status claims and cite the stronger negative-time companion. |
| [Recurrence](../recurrence/manuscript/main.tex), prior build 46 pages | Fixed/growing-order negative-time hierarchy, retained Riemann–Siegel integral, finite algorithms, calibration, onset and evaluation cost; includes Notes16/18 | Focused technical paper. Retain the full negative-time proofs and effective evaluation machinery; cross-reference the positive work without implying identical hypotheses or residuals. |

The build identities were checked: all 25 base TeX files, the single
ansatz TeX file, and all 16 recurrence TeX files match their respective
current build records; all three PDF hashes match too. Page counts and
prior layout checks come from those records. No rebuild or new PDF
visual inspection was performed. Thus the manuscript lag described below
is present in both the maintained sources and their current reading copies.
[Input record](41_MANUSCRIPT_PLACEMENT_REVIEW_INPUTS_20261026.json) pins
the dirty working-tree sources at HEAD `6ac38b83c6602a671cf7e91684895706b425e893`;
it does not describe a new clean commit.

## 2. Findings that should drive the revision

### A. The base manuscript understates its own later results

The [remaining-work section](../manuscript/14_scope_and_remaining_work.tex),
lines 65–78, still recommends proving a canonical complex square-root
neighborhood and positive polynomial source and says that a
polynomial-cost result is not established. [Parent Note58](../notes/58_POSITIVE_ANALYTIC_SOURCE_COMPRESSION_20261025.md)
already records that branch/construction proof and a fixed-upper-time
compressed source descriptor of `O(R^2 log R)` bits for the same
four-jet consumer. The old clipped-cubic exponential descriptor remains
a valid sufficient construction, but is no longer the strongest available
source-description result. Its hypotheses must remain visible when the
new comparison is introduced.

The end of [the all-time theorem](../manuscript/23_all_time_assembly.tex)
also says a working-precision theorem is absent. Parent Notes59–61 now
record a finite evaluator/filter error ledger, a literal phase-index
constructor using existing onset freedom, and polynomial cost in
additional accuracy bits at a fixed descriptor/query box. See
[Summary62](../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md) and
[Note61 PC1](../notes/61_POLYNOMIAL_ACCURACY_EVALUATOR_AND_FILTER_COST_20261025.md).
These advances should replace the corresponding open-task statements.
Useful uniform height/time cost, a complete executed certificate, and
the full-chain review remain open. “Polynomial accuracy-bit cost” must
not become “efficient uniformly over all heights and times.”

Consequently a base revision is warranted even before importing either
branch. Merely appending the newest positive theorem would leave the
paper's abstract, cost discussion and conclusion out of date.

### B. The ansatz paper no longer gives a current account of either branch

Its [coverage table and conclusion](../ansatz/manuscript/main.tex),
lines 1693–1840, still organize negative-time progress around the
`|G| X^(-5/4)` first correction, with its growing outer allowance, and
positive-time progress around the inherited leading saddle. The older
claims remain valid for their specified models. They should be identified
as earlier comparisons, not left as the current ceiling of the program.

The recurrence manuscript now supplies, for fixed `p >= 1`, a
`X^(-(p+3/4))` natural-gamma-scale bound on every declared fixed compact
negative-time family. On `1 <= T=-t <= 2`, controlled growing order
`p=floor(L/2)` gives `exp(-L^2/4)` outer-envelope accuracy, with explicit
calibration, a sufficient `L >= 64 nu`, and an analytical evaluator.
The full arithmetic population and bounded completion integral remain.
See its [comparison theorem](../recurrence/manuscript/sections/04_comparison.tex),
[growing-order theorem](../recurrence/manuscript/sections/05_growing_order.tex)
and [effective evaluation](../recurrence/manuscript/sections/12_effective_evaluation.tex).

The requested [Ansatz Summary21](../ansatz/notes/21_CHAT0005_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md)
correctly points to positive-time results absent from the manuscript:

- [Note19 FO4–FO6](../ansatz/notes/19_ARBITRARY_FIXED_POSITIVE_TIME_ORDER_20261026.md):
  for every fixed `J`, a complete two-arm model `P_(2J)` with eventual
  all-real-height envelope field error `O_J(t^(-J-1) log^(-2J-3)t)`,
  buffered spatial derivatives, direct time error and an actual residual.
  Even `J=0` sharpens the leading field allowance by using parity.
- [Note20 RB4–RB5](../ansatz/notes/20_COMPACT_POSITIVE_FIELD_BRIDGE_20261026.md):
  on each fixed `I=[a,T]` contained in `[32,infinity)`, the complete
  normalized field budget is `X^(-(2J+3)) + X^(-t log(2)/4)`.
  In particular `P4` has field error `O(A X^-7)` on `[63,65]`, with
  the stated derivative/time losses and residual payment.
- Note20 also rechecks the elementary corrected carrier on every fixed
  `[32,T]`, proves buffered envelope comparability and a genuine overlap
  with the late theorem, and retains the exact cutoff term in an optional
  time splice.

The coverage table should report these gains and their remaining gaps.
Its “next” recommendation also predates the current Summary21/
Progress03 route to the existing named-center packet A03-AN01.

### C. The recurrence manuscript is the most cohesive specialist paper,
but its present title and theorem chain are specifically negative-time

The two hierarchies share finite exponential-coefficient recurrences and
Gaussian moments. That makes a shared explanation valuable. Their
analytic contracts nevertheless differ:

| Feature | Negative-time recurrence | Positive-time hierarchy |
| --- | --- | --- |
| Construction | Frozen chart data and forward Gaussian heat evolution | Moving implicit gamma saddle with quadratic part absorbed |
| Arithmetic | All retained `n <= N`, both arms, matched RS completion through `C_(2p)` | Two gamma arms; complete omitted ordinary arithmetic paid in the error |
| Heat residual | Exactly zero for the frozen finite analytic model | Explicit generally nonzero residual `-sum_w S_t(w) Q C_(2J)` |
| Order growth | Controlled `p` proportional to log-height on `[1,2]` | Every fixed `J`; growing order is not established |
| Scale | Natural gamma norm; separately converted outer envelope | Positive sum of saddle-arm moduli |

Adding the whole positive program to the recurrence paper would require
changing its title, organizing theorem and scope. It would also mix a
detailed certified-data/evaluation argument with a positive-time theory
whose comparable evaluator and physical consumers have not been proved.
That is possible as a later new editorial decision, but is not the best
first revision. Keep the existing coherent negative-time paper.

## 3. Distinctions the main synthesis must preserve

**Global physical existence and a sharp regional asymptotic cover are
different achievements.** The base all-time theorem uses one finite
source per target, Gaussian/saddle endpoints and paid joins to approximate
the physical tuple. The newer short hierarchy formulas do not yet form
an all-time/all-height cover. Their compact bounded-height positive core,
the intervening small-positive range, strong negative moving-endpoint
comparison and stronger through-zero joins remain open. This does not
contradict the inherited global finite-source construction.

**A smaller field error does not automatically improve the physical
tuple.** Keep the base's existing positive physical rates until corrected
models have their own zero collars, analytic-unit/pole comparisons,
unchanged-regulator payments, actual filtered means and covariance, and
joining allowances. Summary21 explicitly leaves these consumers open.
Do not substitute `b_J` into an old physical theorem and declare the
transfer proved. The historical `A_lin` center and the rounding scale
`128/(pi X log X)` also remain those of the existing regulator problem.

**Quantifiers and arithmetic determine the claimed accuracy.** The
positive theorem fixes `J` before choosing its constants/onset; the compact
theorem fixes its upper time before height tends to infinity. Keep
`X^(-t log(2)/4)` at higher compact orders. It is a paid upper allowance,
not a lower bound on the true signed error. The `[63,65]` result comes
from its own compact proof, not substitution of `t=64` into an unspecified
eventual-time threshold. An optional splice with the coarser elementary
carrier has its coarser rate; it does not retain the pure `P4` rate
everywhere merely because one component has it.

**Notation needs deliberate reconciliation.** `p` denotes negative
truncation order and a positive saddle; `B` denotes a time endpoint and
a saddle determinant; `N` denotes a mode cutoff and a joint scale;
`C_(2j)` denotes RS coefficients and positive saddle corrections; `Q`
denotes a differential operator and physical covariance. A short notation
dictionary with branch-specific symbols is preferable to literal copying.

These are source-specific quantitative approximation results, not a new
RH criterion. The generic heat/recurrence algebra alone also applies to
controls; the canonical arithmetic, complete xi identity and source
payments supply the distinguishing premises. See the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control screen](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[shared-premise review](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[status lag](../../../../avoid/19_status_files_that_lag_the_findings.md)
and [volume without a gain](../../../../avoid/20_volume_without_a_gain.md).
No new mechanism requiring a new control computation is proposed here.

## 4. A concrete editorial plan

Make the base paper the document a new reader opens first. Give it a short
common normalization/norm dictionary and a table separating four columns:
field accuracy, physical-observable accuracy, domain/quantifiers, and
evaluation status. Organize its argument around:

1. Canonical field, regulator, filter and the main global physical theorem.
2. Regional field approximations: negative hierarchy, inherited zero-time
   window, positive hierarchy, and the exact gaps between them.
3. Physical transfer and the existing all-time construction, with its
   original valid rates and defects.
4. Positive source compression and finite evaluation, integrating parent
   Notes58–61 with their fixed-parameter cost limitations.

Use concise attributed theorem statements and proof references for the
specialist branch results. Keep the negative proof/evaluator sequence in
recurrence. Develop the positive proof sequence in ansatz when that
companion is next revised, replacing its outdated broad status narrative
and shortening duplicated negative-time development. Preserve the older
sources and their model-specific comparisons. Do not concatenate three
papers or recreate their detailed research chronology in the main text.

The existing base title can remain for this first revision: its principal
theorem is still about averaged densities and all-time approximation.
If a later paper puts the two hierarchies themselves at center stage, a
field-asymptotics title would be appropriate, but that would be a separate
scope decision. The present recommendation does not rename or retire a
manuscript or move any research/chat history.

**Next deliverable: Analysis — Sol**, proposed
[HDA-10-MI3 r1](../research-progress/handoffs/HDA-10-MI3.md): update the
base paper's own source/evaluation results and add a faithful two-branch
theorem/domain map, with synchronized companion navigation. This is
routine analytical exposition and production; no resistant mechanism
requiring Astra has been identified. Execution is unstarted. The existing
scientific packets A03-AN01, A08-AN01 and recurrence AN08 keep their
owners and scopes.

The present reply saves this review, its input record and that bounded
integration request, with index/ledger links. It does not change any TeX
proof, rebuild a manuscript, create a manuscript milestone/snapshot, or
commit the preexisting working-tree changes. HDA-17 remains Partial,
HDA-18 Gated and HDA-20 unfulfilled; no branch acceptance is changed.
