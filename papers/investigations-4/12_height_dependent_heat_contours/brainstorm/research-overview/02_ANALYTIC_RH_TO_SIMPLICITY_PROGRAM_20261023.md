# Analytic progress from RH toward simple zeros

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Current continuation after the book theorem:** use [Overview 04](../../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and its [progress register](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) for the next arithmetic work inside the acquired contour. This earlier overview retains its program history; the fixed-offset theorem is now an input, and the multiplicity-sensitive arithmetic estimate remains open. Updated 23 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**.

**Overarching objective: find the strongest new analytic result we can establish in support of RH implying simple zeta zeros, and organize the paper around its proof. The theorem's conclusion, hypotheses, formulation, scale and method remain open to improvement as the research develops.**

The author's governing instruction is: “We are not necessarily looking for a well-characterized theorem, we are looking for the best result we can find to support RH->simple zeros.” This program therefore does not fix density-one simplicity, a particular percentage, a power of a logarithm, a heat statistic, or a moving boundary as the required outcome. RH implying every-zero simplicity remains the ultimate question. Any substantive intermediate result must make its advance toward that question visible.

**Analytic arguments fit for the selective paper are the overarching goals.** Numerics, model examples, approximation machinery, computational certificates, and auxiliary representations serve those arguments. They do not set a competing research agenda. The author expressly permits rewriting or replacing the argument in [book.tex][book] if a superior result emerges. [main.tex][main] and its supporting material are available to that search; the present organization of either manuscript is not a constraint.

This overview and its [progress register][progress] are the current cross-route research brief. They refine [Note 10][targets]: its density-one target, logarithmic rate, microscopic clock and percentage thresholds are useful examples and calibrations, not a binding theorem specification. The [OBF register][obf-progress] continues to own its open-boundary tasks, and the [HDC register][hdc-progress] its existing spectral/contour tasks. Their results remain available without requiring every old work package to be completed. New **SIMP-01–03** goals below concern the analytic advance, its strongest consequence and the eventual paper.

Read the [result index][results] and [avoid index][avoid], particularly [local heat geometry][geometry], [collision controls][controls], [target reformulations][a01], [shared premises][a02], [coupled estimates][a12], [scoped exclusions][a07], and [numerics before the question][a10].

## What can count as the desired theorem

The strongest reachable conclusion should emerge from the successful arithmetic argument. Possible outcomes include every-zero or eventual simplicity under RH; an exceptional-count estimate; density-one simplicity with or without a rate; an improved simple-zero proportion; or a new quantitative restriction on possible multiple zeros with a proved and useful consequence for simplicity. A result outside this list is welcome if its mathematical contribution is stronger or more revealing. These are alternatives, not mandatory stages or an ordered list of tasks.

For orientation, let N(T) count nontrivial zeta zeros with 0<Im rho<=T, with multiplicity, and let N_s(T) count simple zeros. Then M(T)=N(T)-N_s(T) counts labels at nonsimple sites. Bounds M=0, M=o(N), M<<N/(log T)^delta, and M<=(1-p+o(1))N express different strengths. An average bound that still allows a sparse exceptional set does not prove every-zero simplicity. Eventual simplicity also leaves a finite initial region to resolve. No particular delta or p is promised by this program.

RH alone is the preferred unproved hypothesis in a theorem described as progress on RH implying simplicity. If an intermediate theorem needs additional arithmetic assumptions, state them, explain what is known about them, and identify the new implication or estimate it supplies. Assuming the desired nonclustering or full pair-correlation input does not establish a new RH-alone conclusion. Conversely, a new arithmetic lemma with a demonstrable quantitative gain can be valuable interim progress before a global theorem is complete.

The checked numerical benchmark is the RH-only proportion 19/27 from [Bui–Heath-Brown][bhb], also recorded in [Lamzouri's September 2026 introduction][lamzouri]. A new proportion should be compared with that benchmark. A different local, uniform, or structural theorem needs a comparison appropriate to its own conclusion; it should not be rejected solely because it is not a record percentage. Novelty, strength and usefulness require a literature check matched to the theorem actually obtained.

## Established resources and their limits

The canonical normalization is H_t=-H_zz and 8H(0,z)=xi(1/2+iz/2). The H-coordinate is twice the usual zeta ordinate. Preserve the complete theta/xi field, its arithmetic coefficients and its tails in every application.

| Available result | What it supplies | What remains unproved |
| --- | --- | --- |
| [Book's finite moving-window balance][book] | Exact nonreal population loss and relative flux; sharp endpoint multiplicity bounds | Useful canonical bounds for the earlier nonreal population and the full inward flux at growing height |
| Reference determinant and ordered theta residual | Coupled expression H_zz G_z-H_z G_zz, exact current limit, quadratic diagonal cancellation and a strict improvement over a specified absolute comparator | Useful normalized arithmetic size; source ordering alone also holds for weighted-square controls |
| [Positive-time spectral route][spectral] | Under its complete real-root motion hypotheses, M<=4q; bounded spectral filter, coefficient/forest interfaces | A useful microscopic upper estimate for the actual theta statistic, with all source and coverage costs |
| [Corrected microscopic reference][reference] and complete coefficient transport | Arithmetic approximation and finite transport in their stated regimes | Appropriate whole-wall margins, conditioning, reference spectrum and any needed extension of the error theorem |
| [Hybrid multiplicity bound][targets] | A stronger combination of the heat budget with a published RH multiplicity moment | A new small upper bound for the heat budget itself |

These statements have the proof and internal-review status recorded in their sources. They are not specialist refereeing, a new global simplicity proportion, or evidence that a particular target is close to completion. Existing finite certificates support their specified claims and do not extend them to unbounded height.

For the negative-time route, let R(T) sum the complete earlier nonreal population plus one-sided inward flux over windows covering the endpoint population. Let

\[
 C(T)=\sum_{\rho\ \mathrm{distinct}}m_\rho(m_\rho-1).
\]

[Note 10][targets] proves the generic consumer

\[
 M(T)\le\min\left\{N(T),C(T),\frac32R(T),\frac{3R(T)+C(T)}4\right\}.
\]

[Chirre–Gonçalves–de Laat][cgd] give C(T)<=(0.3208+o(1))N(T) under RH. The mixed bound exploits different worst multiplicities: triples for the standalone heat bound and doubles for the moment bound. Thus limsup_{T→∞} R(T)/N(T)<(32/27-0.3208)/3=0.288128395... would improve 19/27, R<=(1/4+o(1))N would give at least 73.23% simple, and R=o(N) would give density one. These thresholds measure a proposed estimate's consequence; none is an acquired estimate or an imposed destination. Use cumulative populations when importing the cumulative moment theorem, unless a corresponding local theorem has separately been justified.

The positive-time q route is an alternative, not a compulsory intermediate step toward R. A proof may instead combine these quantities, sharpen a multiplicity-sensitive bound, use existing arithmetic mean values, or develop another observable with a justified connection to simplicity. A new representation must earn its place through the estimate it enables.

## Three overarching analytic goals

### SIMP-01 — Prove an arithmetic estimate that restricts multiplicity

Find and prove an estimate in which actual theta/xi arithmetic, together with RH where used, constrains a quantity that detects possible multiple endpoint zeros. Seek useful size, a signed cancellation, a nonconcentration estimate, or a local obstruction that survives complete error accounting. The decisive question is what the arithmetic proves that generic heat geometry cannot.

The present candidates are the joint earlier-population/relative-flux resource; the positive-time bounded spectral statistic; and their possible combination with multiplicity moments or other arithmetic mean-value information. These are starting points, not an exhaustive list. Source normalization, reference choice, boundary geometry and averaging should be chosen to make a substantive estimate possible. They may all change.

Retain coupled expressions before applying inequalities. For the resource approach, a small determinant or source tail alone does not pay the earlier nonreal population. For the spectral approach, accurate approximation alone does not make the reference spectrum small. A finite anchor constant is useful only when its dependence is compatible with the theorem being pursued. Claim progress when a proved estimate improves a stated consequence, range, or same-information comparison, with its full scope visible.

### SIMP-02 — Derive the strongest justified simplicity consequence

Translate each useful estimate into the sharpest result it supports, including combinations with known arithmetic theorems. Compare bounds on multiplicity mass, excess multiplicity, numbers of multiple sites, and particular multiplicity classes when these distinguish stronger outcomes. Retain complete populations and quantify exceptional labels. Improve a loss in the conversion when it affects the final theorem; the hybrid consumer is an example.

Choose spatial scales, heat times and covering schemes from information independently available in the proof. No single microscopic clock is prescribed. If a proof uses a two-limit statement such as

\[
 \limsup_{T\to\infty}R_T(\lambda)/N(T)\le A(\lambda),
 \qquad A(\lambda)\to0,
\]

justify the fixed-lambda height limit and then the lambda limit. A rate or a choice lambda=lambda(T) needs additional uniformity. This is one candidate mechanism, not the program's required theorem.

Pay localization, overlap, repeated crossings, exterior forces, carrier terms, heat defects, approximation errors, and omitted labels wherever they actually occur. An estimate on a fixed band, on average, or away from zero time has exactly that scope until an assembly theorem extends it. Separate control of sparse exceptions from density conclusions. If a local estimate reaches the single-event threshold, investigate whether it extends to every height; do not assume that a density argument must be the final outcome.

### SIMP-03 — Build a selective analytic proof around the strongest result

Once a substantive estimate and its consequence are available, organize a coherent mathematical argument for the reader: the theorem, the arithmetic mechanism, the necessary analytic transfer, and the resulting advance. Seek sharp constants and transparent hypotheses when they improve that argument. The moving-boundary formula is a valuable candidate centerpiece; it is not owed that position if a better mechanism emerges.

A result belongs in the main paper when it proves a necessary step, explains the central mechanism, establishes a relevant sharpness or limitation, or supplies an independently significant analytic theorem that fits the argument. Detailed implementations, extensive model checks, and routine approximation bookkeeping normally support the proof from notes, appendices or numerical records. Keep enough explanation in the paper for the claim and its dependencies to be assessable.

The author has authorized reconsidering and rewriting book.tex. Its title, order and selection of results may change with the mathematics. This overview does not itself rewrite a manuscript or create a draft snapshot. The eventual milestone should record the actual theorem and its proof, rather than preserve a preselected outline.

## Supporting work and how to choose it

For substantive supporting work, make clear which SIMP goal it serves, the uncertainty or proof obligation it addresses, and how its outcome bears on the analytic argument. Support can include a proof lemma, a literature import, a sharp model, a symbolic calculation, or a bounded interval computation. Routine proof exploration and literature checks can develop freely; document the connection when a line of work becomes substantial. No numerical work is required merely because tools are available.

A useful computation might challenge a conjectured inequality on a collision model, determine whether a derived allowance has any usable margin on a prescribed example, or verify a finite constant genuinely needed by a proof. Record what failure would refute or force revision of the proposed estimate. Finite observations cannot establish asymptotic uniformity, a density conclusion, or every-zero simplicity; a rigorous finite certificate may establish its expressly finite corollary. Broad height scans, fitted heat-width laws and extra precision need a specific analytic reason to enter this program.

Likewise, an auxiliary representation or a new error lemma should resolve an identified bottleneck in SIMP-01 or SIMP-02. Completion of an OBF/HDC subtask is not automatically completion of an overarching goal. Use a matched analytic comparator where the claimed advance is improved estimation from the same information. A failed implementation should narrow the affected approach, not imply that every arithmetic or geometric alternative is impossible.

## Controls and mathematical standards

Apply the [control register][controls] to the actual hypotheses and conclusion of each proposed estimate. The quadratic and cubic heat models attain the sharp generic bounds and retain their collision costs. Euler-factor controls alter the canonical source; weighted-square and finite-prime controls fail the relevant complete coefficients/reflection requirements; reflected and primitive-compatible sources alter the complete theta data; close normalized endpoint controls fail ordinary Dirichlet-series arithmetic. Naming these failures does not establish a quantitative advantage for theta. Show exactly where the proposed estimate uses distinguishing information, or keep it classified as generic.

Sparse collision controls can be compatible with a density theorem. They must not be rejected merely because they contain an exceptional double; test whether the control contradicts the claimed scale and conclusion. For every-zero claims, retain the stricter single-event accounting. State negative results with the precise class of estimates or constructions they exclude.

Classify outputs as proved analytic results, conditional implications with named extra assumptions, conjectural targets, scoped obstructions, or numerical evidence. A criterion equivalent to the desired conclusion is stated once and is not counted as an arithmetic advance. Keep same-model review distinct from specialist or formal verification.

## Current user-directed continuation: spatial conservation

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), effort ultra**. The continuation in history 0007 prioritizes the spatial contour z=T+i epsilon(T,t), with smoothing left as an open modeling question. [Note 16](../notes/16_NATURAL_CONTOUR_EVOLUTION_20261023.md) selects the native heat conservation law H_t+partial_z H_z=0 as the first model: velocity H_z/H preserves H dz and the primitive image. It derives the positive-density and Noether formulations and compares the original physical topological connection and regularized zero current. [Review 07](../reviews/07_SPATIAL_CONTOUR_EVOLUTION_REVIEW_20261023.md) checks scope and controls.

The infinite adjoint/Fourier hierarchy is exact; its actual theta values may be useful, but generic existence or completeness does not prevent collisions or provide coercivity. The next analytic question is whether those data control inverse-primitive continuation and actual tangent strain on a prescribed compact initial contour. No global graph or simplicity consequence is acquired. [The progress register][progress] also records the completed scoped arithmetic tests of Note 15, so they need not be restarted. The theorem form remains flexible.

## Next analytical session and maintenance

[Continuation 11](../notes/11_CONTINUATION_FLEXIBLE_ANALYTIC_RH_TO_SIMPLICITY_20261023.md) gives the next-chat reading path, exact current status and verified history identity.

Start from the strongest current arithmetic inputs and the comparison in the [progress register][progress]. Identify a promising estimate and the simplicity information it could supply; investigate the estimate analytically while allowing both the method and the eventual conclusion to change. There is no prerequisite to choose a final theorem statement or numerical target before doing research. A provisional quantitative question should be precise enough to test, but should be revised when the mathematics reveals a better result.

Record new derivations in brainstorm `notes/`, assessments in `reviews/`, and necessary computations in `numerics/`. Update the progress register when evidence changes an estimate's status or the best supported consequence. Link to OBF/HDC owners for their technical status instead of maintaining competing copies. Keep milestone history concise and follow [LARGE_FILES.md][large]; create no new manuscript snapshot folders. This overview establishes research priorities, not a new mathematical result.

This conversation remains [brainstorm history 0006][chat]. Preserve its identity and use the repository [chat-history workflow][history] for beginning/end refreshes and bounded final capture until trusted native completion capture is verified.

[progress]: ../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md
[targets]: ../notes/10_SIMPLICITY_THEOREM_TARGETS_AND_HYBRID_CONSUMER_20261023.md
[book]: ../../manuscript/book.tex
[main]: ../../manuscript/main.tex
[spectral]: ../../manuscript/spectral_forest.tex
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[obf-progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[hdc-progress]: ../../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[bhb]: https://arxiv.org/abs/1302.5018
[lamzouri]: https://arxiv.org/html/2609.02882v2
[cgd]: https://arxiv.org/pdf/1810.08843v2
[large]: ../../../../../LARGE_FILES.md
[history]: ../../../../../tools/CHAT_HISTORY.md
[chat]: ../chat-histories/0006_2026-10-23T22-48-39Z_shape-a-theorem-for-rh-and-simple-z.json

## Focused conservation continuation

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The author requested a dedicated analytic program toward the result and proof for the book. The [new overview](../research-overview/03_CONSERVED_SPATIAL_CONTOURS_ANALYTIC_PROGRAM_20261023.md) and [SCF register](../research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md) now own that continuation; the overarching SIMP statuses remain open as recorded above. The provisional conservation section is in main.tex, while book.tex is preserved. Numerics always support identified analytical work. [Continuation 17](../notes/17_CONTINUATION_CONSERVED_SPATIAL_CONTOURS_20261023.md) is the current handoff.
