# Height dependent heat contours and time zero cap estimates

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.

**Current priority: analytical control of the pair spectrum and curved heat contours, first for RH implying simple zeros, with almost-all simplicity as an intermediate theorem.** The new [analytical overview](research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md) sets that direction and separates RH-dependent inputs from reusable source and contour tools. HDC-07 now has a paid distant-force bound, and HDC-08/HDC-09 have finite conditional theorems. The retained high-height source estimate and useful correlated backward acquisition remain open; one complete finite canonical wall is now certified. Numerics serve a supporting role. The original physical-cap comparison remains a parallel branch: HDC-01 and HDC-02 are complete in their stated scope, while Notes 13 and 15 now pay finite source bounds and a complete bounded comparison, without a useful positive lower bound or deformation gain.

Start with the [new analytical overview](research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md) and the [research-progress register][progress]. The [first overview][overview] retains the physical-cap contract. The register is the sole detailed owner of **HDC** tasks.

The [23 October progress snapshot](research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md) records the established foundations, missing analytical estimates and next deliverable. The [execution-chat verification receipt](chat-histories/VERIFICATION_EXECUTION_CHAT_20261023.json) records the archive checks.

Execution update, 23 October 2026, **gpt-6-astra (Codex), effort ultra**: read [Note 02](notes/02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md) for the fixed finite-band contract and [Note 03](notes/03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md) for the complete expression, a polynomial sign counterexample, and the scoped direct comparison. The [separate same-model review](reviews/01_FINITE_CONTRACT_AND_COUPLED_ESTIMATOR_REVIEW_20261023.md) and [exact algebra record](numerics/01_BOUNDARY_AND_RELATIVE_ENERGY_CHECKS_20261023.json) support this specification/derivation milestone; no theta interval is certified. HDC-03 source acquisition remains open on the physical-cap branch. The [original continuation note](notes/01_CONTINUATION_HEIGHT_DEPENDENT_HEAT_CONTOURS_20261023.md) retains the historical handoff.

## The proposed geometry and estimating objective

Use the unchanged canonical theta field \(H_\tau=-H_{zz}\) and physical first jet \(G=(H,H_z)\). At each finite height cutoff \(H_{\max}\), the cross-zero contour has a fixed right face \(t=\delta_{H_{\max}}>0\), interpreted through a controlled \(0^+\) limit, and a left face \(t=-\epsilon(h)\), with the backward width allowed to decrease with height. Imaginary time, spatial boundaries and connecting faces are part of the domain.

For the negative-time collar ending at zero, the inherited exact balance on a regular boundary is

\[
I_0=I_{-\epsilon}-S_\epsilon+Q_-,
\qquad Q_-\ge0.
\]

Thus a lower bound for \(I_{-\epsilon}-S_\epsilon\) transfers to \(I_0\) without first excluding interior collisions. Event-freeness gives equality with that complete deformed representative. Boundary events require explicit excisions. The physical three-form cap remains distinct from the real angular integral.

The proposed mechanism combines moving projective tubes, exact cancellation of shared cell faces, and Rodgers–Tao reference-state subtraction before estimation. The material derivative of the complete root-source product contains the inverse-square gap energy plus an analytic-factor term. Both that term and the imaginary-time faces remain in the calculation. A local two-root discriminant radius supplies a direct comparison for any claimed survival improvement.

## Background and reading order

1. Read the [repository result summaries][results] and [patterns to avoid][avoid], especially [local heat geometry][geometry], [collision controls][controls], [target classification][a01] and [coupled estimates][a12].
2. Read the [structural cancellation continuation][continuation]. It explains the original objectives, exact late-tube cancellation, Rodgers–Tao subtraction and the shrinking negative-time proposal.
3. Read the [moving-collar brainstorm][brainstorm] and its [self-review][brainstorm-review]. These contain the refined time-zero estimating objective, material velocity, complete source-product derivative, real-to-complex cap remainder and conditional two-root radius. The [exact algebra record][checks] checks finite identities, not theta exclusion.
4. Read [Note 13 on height-dependent backward contours][collar] and [Review 05 on usefulness][usefulness]. They identify the complete cap-and-connector consumer and the comparison that remains unpaid.
5. For proofs of the inherited local tools, read the [physical boundary derivation][boundary] and the [two-root discriminant equation][two-root]. Use the [quantitative endpoint windows][endpoint] for a geometry that permits a collision rather than assuming an interior gap.
6. Consult the external sources below, then use the new analytical overview and [progress register][progress] for HDC-07 onward.

## External reading

| Reading | Purpose and scope |
| --- | --- |
| [Rodgers–Tao, The De Bruijn–Newman constant is non-negative](https://arxiv.org/html/1801.05914), Sections 4 and 7–8 | Zero dynamics, localized reference subtraction, linear correction and exterior payments. Their all-real negative-time interval is a contradiction hypothesis; it is not an unconditional input here. |
| [Csordas–Odlyzko–Smith–Varga, A new Lehmer pair](https://etna.ricam.oeaw.ac.at/vol.1.1993/pp104-111.dir/pp104-111.pdf), Theorem 1.1 and equation 2.19 | Close-pair dynamics, exterior interactions and the squared-gap heat scale; trace the underlying Csordas–Smith–Varga theorem through its references. |
| [Papanicolaou–Kallitsi–Smyrlis, Entire solutions for the heat equation](https://ejde.math.txstate.edu/Volumes/2021/44/papanicolaou.pdf), Section 4 | Isolated complex multiple zeros and zero trajectories; reverse the forward-heat sign convention when applying it here. |
| [Polymath, Effective approximation of heat flow evolution of the Riemann xi function](https://arxiv.org/html/1904.12438), Proposition 3.1 and Theorem 1.5 | Root motion and the positive-time high-height benchmark. It does not automatically cover the proposed microscopic \(0^+\) face. |

These readings locate the ingredients. The specific coupled theta estimate remains the research task; no novelty claim follows from opening this investigation.

## Work folders and related programs

Save new derivations in [notes](notes/README.md), small computations and execution records in [numerics](numerics/README.md), and assessments in [reviews](reviews/README.md). The [milestone history](DRAFT_HISTORY.md) stays concise. The background brainstorm files remain the cited source records.

[Home 02](../02_theta_source_constraints/README.md) supplies canonical-source constraints; [home 03](../03_heat_transport_and_charges/README.md) owns broader heat transport; [home 10](../10_chern_hopf_integral_estimates/README.md) owns its existing integral estimates; [home 11](../11_late_heat_caps_and_charge_transport/README.md) owns late-time cap asymptotics. Home 12 owns the shrinking backward collar and the complete deformed estimate for the original cap.

The founding conversation **Study height-dependent epsilon** retains its unique [brainstorm archive][chat]. [History guidance](chat-histories/README.md) routes new execution chats and preserves existing identities. Follow the [large-file policy][large] and [chat-history workflow][history-policy].

[overview]: research-overview/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRAM_20261023.md
[progress]: research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[continuation]: ../brainstorm/notes/01_CONTINUATION_STRUCTURAL_CANCELLATION_RODGERS_TAO_AND_BACKWARD_HEAT_20261023.md
[brainstorm]: ../brainstorm/notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md
[brainstorm-review]: ../brainstorm/reviews/01_MOVING_COLLAR_AND_MATERIAL_ENERGY_SELF_REVIEW_20261023.md
[checks]: ../brainstorm/numerics/MATERIAL_JET_ENERGY_CHECKS_20261023.json
[chat]: ../brainstorm/chat-histories/0001_2026-10-23T07-39-02Z_study-height-dependent-epsilon.json
[collar]: ../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md
[usefulness]: ../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md
[boundary]: ../manuscript/topological_zero_transport/boundary.tex
[two-root]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[endpoint]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md
[results]: ../../../result-summaries/README.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../LARGE_FILES.md
[history-policy]: ../../../tools/CHAT_HISTORY.md

## Statistical continuation and conditional simplicity

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The author added RH implying almost-all simplicity as an explicit intermediate objective and recalled the pair-matrix eigenvalue program. [Note 04](notes/04_PAIR_STATISTICS_AS_A_ONE_SIDED_CONTOUR_INPUT_20261023.md) gives the one-sided pair-statistic cap interface. [Note 05](notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md) gives an earlier-time complete projected-pair consumer. [Note 06](notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md) proves a uniform spectral counting implication from the inherited adjacent-gap bound, including a bounded resolvent target. These real-time applications do not depend on completing HDC-04 first. Their missing theta statistical upper bounds remain open; no new simplicity proportion is obtained. [Review](reviews/02_PAIR_STATISTICS_AND_SIMPLICITY_TRANSFER_REVIEW_20261023.md).

Analytical program update, 23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**: the [new overview](research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md) prioritizes complete theta control of L and its bounded spectral filter, distinct curved-contour geometries, error-controlled backward use of late data, and conditional simplicity. [Program review](reviews/03_ANALYTICAL_SPECTRAL_CONTOUR_PROGRAM_REVIEW_20261023.md). This update organizes future analytical work; it proves no new theta upper bound.

Analytical execution, 23 October 2026, **gpt-6-astra, ultra**: [Notes 07–10](notes/README.md) provide the complete distant-force error, finite wall/graph and backward theorems, sharp M_0≤4q and the microscopic gap interface. Current high-height clock data yield q/N→1; scalar separate-error backward transport has the large amplification quantified in Note 09. These are scoped route diagnoses, not universal exclusions. The [updated snapshot](research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md) identifies the remaining local/microscopic source estimate. [Round review](reviews/04_ANALYTICAL_RESEARCH_ROUND_REVIEW_20261023.md); no simplicity theorem.

Coefficient-filter follow-up, 23 October 2026, **gpt-6-astra, ultra**: [Note 11](notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md) gives a complete-coefficient route to the scalar filter through the forest polynomial D=Delta det(I+aL), avoiding internal root isolation when its explicit denominator/residual test passes. It treats double collisions, the complex triple obstruction and heat-scale precision. [Review 09](reviews/09_FOREST_FILTER_AND_COLLISION_CONDITIONING_REVIEW_20261023.md); canonical coefficient acquisition and the microscopic upper estimate remain open.

Complete-source backward follow-up, 23 October 2026, **gpt-6-astra, ultra**: [Note 12](notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md) transports prepared coefficients using a finite polynomial in integrated source wall moments. Its appendix pays the full exterior-force, quotient-floor, derivative-error and reference-defect inputs. [Review 10](reviews/10_COUPLED_COEFFICIENT_TRANSPORT_REVIEW_20261023.md); microscopic theta acquisition and simplicity remain open.

Manuscript checkpoint, 23 October 2026, **gpt-6-astra, ultra**: [working LaTeX manuscript](manuscript/main.tex), [reading-copy build guide](manuscript/README.md), and [critical next-step assessment](notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md). New records: [finite canonical certificate](notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md), [corrected microscopic reference](notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md), and [complete cap comparison](notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md). The manuscript is drafted for Edward Baker with LLM acknowledgement and separate same-model review; no global simplicity theorem or publication-readiness claim.

Analytic open-boundary continuation, 23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), effort max**: the author’s proposed relaxation now has a [research overview](brainstorm/research-overview/01_ANALYTIC_OPEN_BOUNDARY_FLUX_PROGRAM_20261023.md), [OBF progress register](brainstorm/research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md), and [next-chat continuation](brainstorm/notes/05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md) in the requested brainstorm home. The milestones are analytic transport and complete-source flux estimates; numerics support those goals. OBF has its own task identifiers, while this investigation retains the HDC register. No negative-time theta flux estimate or larger useful backward width has yet been acquired.

Brainstorm affiliation correction, 23 October 2026: exploratory work for this investigation belongs in its [own brainstorm folder](brainstorm/README.md), including the open-boundary flux program and statistical-mechanics analogy. Earlier series-wide material belongs in [Investigations 4's brainstorm](../brainstorm/README.md). For Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort max**. [Relocation record](brainstorm/CHAT_HISTORY_RELOCATION_20261023.json).

Selective analytic manuscript, 23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**: [Heat collisions and relative zero flux](manuscript/book.tex) now centers the exact moving nonreal balance, reference-level determinant and complete theta/xi source estimates. The ordered square-source identity strictly sharpens a specified absolute bound and gives quadratic diagonal cancellation. The [first research draft](manuscript/main.tex) is preserved. [Selection note](notes/18_RELATIVE_FLUX_AND_ANALYTIC_MANUSCRIPT_SELECTION_20261023.md), [internal review](reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md), [build guide](manuscript/README.md). Useful height-uniform size, earlier nonreal discrimination and new simplicity conclusions remain open.
