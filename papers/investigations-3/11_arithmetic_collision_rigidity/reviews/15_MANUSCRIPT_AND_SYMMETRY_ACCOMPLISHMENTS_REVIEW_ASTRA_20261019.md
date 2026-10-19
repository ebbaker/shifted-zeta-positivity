# Manuscript and symmetry research accomplishments and priorities

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewing model: **gpt-6-astra (Codex)**, actual reasoning effort **max**, verified from the current session metadata.

This is an internal LLM assessment of the manuscript, the research program and its completed continuations. It includes cross-model assessment of work authored by gpt-6.1-sol and same-model assessment of Astra work. Fresh calculations use the existing implementations; this is not an independent implementation or specialist human review.

**Assessment.** The investigation has produced substantial analytic, computational and methodological results. Its strongest new research lead is **S03's complete arithmetic residual estimate**, supported by **S04's uniform scaling and signed averaging theorems**. The manuscript's clearest established contributions are the positive-carrier bounds, the distinction between full modular rigidity and finite arithmetic constraints, and the complete finite and eventual real exclusion results. The recent symmetry work has also identified several approaches whose tested estimates should now be stopped. The remaining real bridge and global complex exterior are still open; no improved Newman bound follows from these results.

## Review scope and source version

The assessment covers all twelve TeX files of the [current manuscript][manuscript], the [18 October program guide][guide], the [seven-program assessment][assessment], both [symmetry research overviews][overview] and [geometric alternatives overview][geometry], the [19 October progress summary][summary], and the [current task tracker][tracker]. The principal mathematical continuations are linked beside the findings below. The repository's [collision-control summary][controls], [theta bookkeeping summary][theta-summary] and [patterns to avoid][avoid] supply the scope checks.

The manuscript matches every source hash in its [build record][build]. Its source-set SHA-256 is `2690c3052927702a7f25d7e0519cc8ae10abfd202ac891bb8c06208eaa9a7b0c`; the build record describes the 45-page integration of 18 October. The repository HEAD observed during this review is `a36d80e4d2c50f747fe5b8bad7e6aab708277dca`. The assessment includes the later working-tree research files, so that commit alone does not identify the reviewed material. The [review receipt][receipt] pins the cited local sources and records the selective fresh replays.

Throughout, let

\[
H_t=-H_{xx},\qquad E=H^2+H_x^2,\qquad
\mathcal L_0=H_x^2-HH_{xx}.
\]

The common pilot is \(B=[1/100,1/5]\times[999,1001]\), and the separate cutoff-crossing box is \(C=[1/100,1/5]\times[1017,1019]\). In the symmetry work, \(Q=H/\mathcal A_t\), \(\omega=\theta_x\), and \(J=(Q,-Q_x/\omega)\). The nonvanishing symmetric normalizer \(\mathcal A_t\) differs from the manuscript's positive arithmetic carrier. Bounds in these normalizations cannot be compared with physical errors in fixed \(G_c=1000^{7/4}e^{-125\pi}\) units without the stated conversion.

## What the manuscript has established

**Positive arithmetic carriers have strong, explicit analytic control.** The packet construction retains the lower interval created by a shifted half-line integral, mixed-prime contributions, and the signs of reflected derivatives. For nontrivial bounded nonnegative higher-mode weights and \(0\leq t\leq1/2\), the resulting carriers have a positive real part in an explicit complex strip. For the real carrier containing mode 2, the logarithmic derivative satisfies \(\alpha^2+|\alpha_x|\leq1/64\). With the original theta coefficients, the \(\{2,3\}\) approximation to its positive higher-mode carrier has a relative tail below \(7.3\times10^{-25}\), with derivative and complex-strip versions. These are clean quantitative statements about the carrier. [Packet and positivity sections][packets] [Carrier bounds][positivity]

**The complete signed field requires cancellation that carrier positivity cannot supply.** Full modular reflection cancels the algebraic endpoint tails of the complete source. A fixed positive-tail omission can therefore become decisive after division by the exponentially small physical field, despite extraordinary relative accuracy for the carrier. The normalized Laguerre identity isolates a controlled carrier term but leaves the signed normalized-field term unproved. This is a valuable diagnosis of the actual obstacle. [Modular cancellation and collision analysis][modular]

**Exact modular identity is more restrictive than any fixed package of finite arithmetic tests.** Within the stated polynomial-growth square-comb class, exact normalized reflection forces constant coefficients. Conversely, the finite-prime orbit construction permits positive weights arbitrarily close to one that preserve a fixed finite prime set, a prescribed coefficient prefix and finitely many real linear measurements while creating a nondegenerate positive-time collision. The latter controls do not retain full modular reflection, and their event heights are not effective. Together these results explain why the full theta identity matters and why finite arithmetic compatibility alone is insufficient. This pair is among the manuscript's strongest conceptual accomplishments. [Rigidity argument][modular] [Finite-prime controls][finite-controls]

**The approximation machinery reaches physical certificates.** Reflecting the complete source before contour truncation avoids losing the endpoint cancellation. Nonstationary tail bounds then pay the omitted modes and the first two spectral derivatives. Constant-distance contours give a uniform \(O(x^{-1/4})\) error relative to \(G_0=x^{7/4}e^{-\pi x/8}\). The stated choice \(A_c=33\), \(b=1/8\) gives errors below \(7\times10^{-11}G_0\) for \(x=\operatorname{Re}z\geq1000\), \(0\leq t\leq1/2\), \(|\operatorname{Im}z|\leq1\). These estimates support closed-domain certificates for \(\mathcal L_0>E/100\) on \([.01,.2]\times[25,45]\) and on \(B\), plus a complete vertical wall at \(x=1000\) for \(0\leq t\leq.2\), \(|\operatorname{Im}z|\leq1\). [Shifted approximation][shifted] [Effective tails][tails] [Finite certificates][finite]

The wall and the named published initial-zero and heat-flow inputs imply

\[
E(t,x)>0\quad(0<t\leq1/5,\ |x|\leq1000),
\]

and the additional signed rectangle extends the certificate to \(|x|\leq1001\) on \(1/100\leq t\leq1/5\). The manuscript handles possible initial multiplicities through local heat splitting. Its eventual real theorem gives

\[
E(t,x)>0\quad(\varepsilon\leq t\leq1/2,
\ |x|\geq e^{20/\varepsilon}),
\]

improving the earlier onset used within this investigation from \(e^{64/\varepsilon}\). These are actual exclusion statements with explicit domains. The published inputs remain dependencies; they are not new theorems of this investigation. [Finite propagation][finite] [Exterior theorem][outer] [Polymath's approximation and heat-flow results](https://arxiv.org/html/1904.12438v2) [Platt and Trudgian's initial-zero verification](https://arxiv.org/abs/2004.09765)

The real gap on the common slab remains \(1001<|x|<e^{2000}\). Real first-jet exclusion also does not establish the required complex exterior. The manuscript's possible \(\Lambda\leq.18\) application remains conditional on that further complex-domain theorem and its complete consumer hypotheses. The exact remote polynomial control makes the separation concrete: local walls and eventual exclusion can coexist with a collision in the intervening region. Its failure of the stronger signed pilot test is correctly retained as a limitation of that control. [Global scope and conditional consumer][global]

## What the symmetry program has added

The latest tracker, rather than the initial Ready/Waiting entries in chronological plans, determines task completion. A completed comparison may establish a useful theorem, a scoped obstruction or a failed benefit test.

| Program | Accomplishment through 19 October | Research implication |
| --- | --- | --- |
| S01 Modular self-duality | Paired endpoints reduce complete added errors by about 14.85%, 7.22% and 2.99% at orders 0–2. All 40 signed intervals and 116 calls remain unchanged. | Retain the error theorem; stop tail tuning on this pilot. |
| S02 Cutoff reflection | Coherent analytic correction, matched frozen comparison and complete jet consumers. Coupled analytic residual data certify all 4096 B cells. | Useful infrastructure for S03; no strongest-consumer or coverage advantage yet. |
| S03 Normalized jet rotation | Complete independent arithmetic increment below 0.000854, prescribed finite-mode corrections and a fully paid edge. Calibrated transport is compared with matched direct exclusion. | Highest priority for a new arithmetic estimating mechanism. |
| S04 Time-height scaling | Uniform full-cutoff model; signed intermediate average below \(1.5\times10^{-6}\); complete average within 0.11 of one; uniform local transfer and a transition-payment obstruction. | Best developed route toward uniform height analysis, with pointwise and coherent matching obligations still open. |
| S05 Covariant theta jets | Large source-range improvements and a completed compatible shifted acquisition comparison. Complete added-error gains are roughly 0.008–0.009%. | Small reusable implementation gain; the fixed-pilot consumer has reached its stopping point. |
| S06 Hodge and transverse geometry | Exact completions, an event counterexample to second-current positivity, and a paid four-jet comparison: current 60/64 cells, direct 64/64. | A new source of information or cheaper acquisition is needed before continuing this approach. |
| S07 Geometric duality | Exact five-jet space and residual contract; complete profile-trace comparison and further feasibility screens. Tested norm payments lose substantially to direct tails. | Admissibility is now explicit; a useful geometric observation estimate remains missing. |
| GEO-T1 Physical winding | Degree zero on B, with all boundary and control checks; optimized direct certification uses fewer calls and the cost target fails. | Retain as an alternative certificate, reserve further work for a different acquisition bottleneck. |

### S03 supplies the strongest new arithmetic lead

The exact rotating residual coordinate is

\[
Z_r=e^{-i\theta}(r-i r_x/\omega),\qquad
I_r(t;x,a)=i\{Z_r(t,x)-Z_r(t,a)\},
\]

where \(r=Q-f\) for the specified coherent approximation. This endpoint identity alone supplies no arithmetic improvement. The progress is a smaller complete bound for that quantity from prescribed arithmetic information.

The earlier source-informed work preserved the correlation between the residual and its derivatives, reducing an independent-endpoint allowance of 0.002011747 to a signed increment below 0.000266448. The later [gamma and heat correction][s03-6] identifies the omitted logarithmic Stirling and Gaussian-curvature terms without fitting them to values of \(H\). At the pilot center the finite correction and edge discrepancy have opposite signs, but their particularly small difference is phase dependent. The point diagnostic alone did not prove a uniform estimate.

The [complete edge and increment theorem][s03-7] closes that local gap. It pays the Riemann–Siegel edge, gamma prefactor, Gaussian tails, the correction needed for analytic continuation and the retained polynomial approximation. Cauchy bounds apply to the combined holomorphic error. The finite and edge corrections are then recombined before estimating the rotating increment over the closed pilot.

The resulting complete increment is below **0.000854**, independently of source quadrature, physical \(H\) values or source Taylor coefficients. This is more than a 950-fold reduction in the reported allowance relative to the earlier independent analytic-only value 0.812260. It is an advance in the information used by the estimate, as well as its size. It still exceeds the source-informed 0.000266448 allowance by about a factor of 3.2. Neither comparison measures speed or actual residual size.

Fresh replay gives a retained-model increment allowance of 0.0008409937809119583 and a complete remainder payment of 0.00001229053509560982, totaling 0.0008532843160075681. The remainder contributes approximately **1.44%** of that reported total. Thus sharpening only the already small remainder cannot substantially change the current total; extending or more efficiently enclosing the signed retained correction matters more. This is a diagnosis of the certified budget, not a lower bound for the true increment.

The practical comparison is equally important. With the same source information and matched propagation, the earlier calibrated vector radius exceeds 1.3859351576, while the direct radius exceeds 1.3898732635. Comparing the former only with the older raw direct radius 1.3473946960 would falsely suggest a win. The new arithmetic-only increment has not yet established a stronger or cheaper complete consumer. [Matched calibrated comparison][s03-5]

**Why this is the best lead:** it estimates the complete discrepancy using arithmetic structure that survives removal of expensive source calibration. That creates a plausible route to a uniform or less costly method. The next decisive result must show that the mechanism survives changing height and cutoff, or demonstrate a fair complete cost advantage. The fixed \(N=8\) pilot theorem alone establishes neither.

### S04 has the strongest uniform analytic results

S04 studies the sector

\[
0<t\leq1/20,\qquad 1\leq\kappa\leq2,\qquad
L=\kappa/t,\qquad x=4\pi e^L.
\]

Its [full-cutoff model theorem][s04-1] retains the arithmetic phases, heat weights and spectral derivative terms. The [Gaussian averaging theorem][s04-2] then proves cancellation in the intermediate arithmetic core and pays the complete physical approximation. The phase-matched average lies within 0.11 of one throughout the sector, giving a weighted \((Q/2)^2\) energy lower bound of 0.198025. This is an analytic uniform result supported by outward scalar checks, not an extrapolation from the separately reported sample sums.

The distinction between averaged mass and pointwise exclusion is decisive. A positive average or energy does not prevent an isolated simultaneous zero of \(H\) and \(H_x\). It does not identify a useful anchor with the required nonzero first-jet margin. Moreover, the sector begins near \(x=6.097\times10^9\) and restricts \(t\leq.05\); it neither overlaps B nor covers the whole remaining time-height bridge.

The [local transfer theorem][s04-3] is also real progress, even though the attempted global transfer fails. It establishes complete residual charts of radius \(1/(2L)\) throughout the sector, with increment allowance \(46.679e^{-b_*/t}\), where \(b_*\) is the exponent specified in that note. At the opening parameters the increment is below 0.090111. Adding the approximation-anchor uncertainty yields about 0.12873, compared with the direct endpoint allowance of about 0.051492. These are error budgets, not positive anchor margins.

Across the natural cutoff transitions, the specified independent coefficientwise disk rule incurs an assigned budget exceeding \(.99e^{1/(4t)}\), with the sharper opening calculation exceeding 148.413. This excludes that bookkeeping rule as an effective global transfer mechanism. It is not a lower bound for actual signed jumps. Coherent matching or correlated summation could change the estimate, but must be proved for the complete residual. In particular, S04-T3 does not transfer S03's corrected fixed-pilot constant into this sector.

**Priority:** use S04 as the uniform setting in which to test the S03 arithmetic mechanism. Preserve its completed averaged and local theorems while targeting the missing coherent residual and anchor estimate. Improving the average alone would not resolve the physical collision problem.

### S01, S02 and S05 provide useful numerical methods with bounded gains

[S01's complete consumer comparison][s01-2] shows that a sizable percentage reduction in a tiny error component can leave the physical certificate unchanged. Its main remaining obstacle is the retained signed core and whole-cell variation. Further omitted-tail tuning on B has little support from the measured budget.

[S02's comparison][s02-3] establishes a particularly useful distinction between error envelopes and evaluated consumers. The frozen correction has a slightly smaller disk-error envelope; the coherent full approximation has the larger certified first-jet radius, 0.9702739184 against 0.9686625938. Both remain below the source-informed 1.3473946960 reference. Coupling the value and derivatives as data from one bounded analytic residual signs all 4096 cells, whereas independent derivative boxes sign only 1770. That preservation of analytic correlation is a reusable method, and the full approximation remains the appropriate interface for S03. The separate C box has an error theorem, not a newly evaluated exclusion certificate.

[S05's completed acquisition comparison][s05-3] prevents its dramatic source-coordinate width reductions from being mistaken for equally dramatic physical gains. The selected hybrid uses the grouped order-2 coefficient and factored forms for the other 50 coefficients. Against the stronger prior hybrid it reduces complete added errors by more than 0.0092005%, 0.0077659% and 0.0082207% at orders 0–2. The adaptive minimum remains unchanged; fixed-cover differences change direction with precision. Three acquisitions replace two, and no cost improvement is established. This small complete error improvement deserves credit, while the much stronger earlier real-source accuracy reference remains available.

These methods should be retained where they simplify a new analysis or reduce an actual dominant error. Their completed B comparisons do not justify another round of parameter tuning merely to make a smaller intermediate number.

### The geometric work now identifies precise obstacles

S06 first completes the transverse source exactly. The first completed current reproduces \(\mathcal L_0\), so its sign is inherited. The second centered current can be strictly positive at a nondegenerate collision, where \(E=0\); positivity of that current is therefore insufficient. The reselected event-vanishing residual receives fresh complete four-jet estimates, but certifies only 60 of 64 cells. The four remaining intervals straddle zero; they do not prove negativity. Direct certification using the same input balls succeeds on all 64, and every successful current radius is less than 0.552 of its direct comparator. The associated dominance argument concerns the stated scalar extraction and Cartesian jet information. [Completed-current comparison][s06-5]

S07 supplies a concrete five-dimensional theta-jet space, its Gram structure, and a global residual class that includes the necessary complement. This repairs an admissibility problem: the physical source occupies more than the holomorphic theta line, and the residual cannot simply be assumed to live in a favorable finite-dimensional space. The earlier zero-flux and generic first-order trace obstructions also retain their specified function-class hypotheses. [Admissible space and residual contract][s07-3]

The subsequent physical observation estimate is paid and loses. For its fixed \(N=2\) whole-profile norm, assigned value and derivative payments exceed the direct complete-tail allowances by factors greater than 1618 and 34152 before common acquisition errors. Follow-up screens show that changing the admissible cutoff under the same rule or projecting onto the five-jet space while retaining the old complement payment does not repair the comparison. These are floors for the assigned estimates, not observed errors of the theta field. They do not exclude a different norm, mixed adjoint or additional signed arithmetic information. [Profile-trace comparison][s07-4] [Options assessment][s07-5]

[GEO-T1][geo] separately validates the established physical winding criterion. On B it obtains degree zero using seven accepted boundary segments and ten evaluator calls. Optimized direct certification needs three strips and seven calls. Once common source setup is charged, the reported direct-to-winding cold-cost ratios are about 0.9994, so the factor-two advantage criterion fails. The theorem and controls are useful; this already covered box supplies no new domain or practical advantage.

The geometric program's main accomplishment is now a sharper selection criterion for further work: a new geometric construction must provide additional usable information or a demonstrably cheaper complete observation. Re-expressing the existing residual identity in a new representation would not meet that criterion.

## Recommended research order

1. **Develop the complete arithmetic residual uniformly.** Start from S03 Note 07 and state a bounded extension contract: the precise time-height domain, changing cutoff, gamma/heat remainder, coherent edge, derivative requirements and normalization. The central question is whether the signed finite correction and edge can be bounded together across natural cutoff changes. Use S04's sector as a first analytic setting, while keeping its different residual definition explicit. A useful result would be a complete bound whose constants and transition costs remain controlled as height grows. If it fails, identify the term responsible; do not substitute a sample grid for a uniform theorem.

2. **Pay the anchor and complete physical test.** A residual estimate becomes an exclusion method only after the approximant's nonzero first-jet margin, anchor error and propagation are combined on a closed domain. S04's average may help locate mass, but any conversion into a selected anchor needs a new argument. Only then compare with the strongest direct method, including all source, edge and anchor preparation costs. S03's arithmetic independence makes a cost comparison worthwhile; it does not predetermine its outcome.

3. **Consolidate the strongest completed statements for communication.** The existing manuscript already has a coherent core: exact arithmetic constraints, complete cancellation-preserving evaluation, finite certificates and the explicit exterior theorem. A subsequent integration could add the complete S03 arithmetic estimate and S04 uniform theorems as carefully scoped results, with the failed comparison classes collected compactly. This is a publication-organization judgment, not an assertion of novelty or readiness for specialist acceptance. Keep the detailed exploratory history in linked notes and use a commit or tag for a future manuscript milestone.

4. **Keep geometry conditional and stop completed pilot tuning.** S07-T3 should remain waiting for a useful physical estimate; S07-T4 remains deferred. A bounded audit representing the actual corrected S03 residual in a proposed geometric space could be justified if it identifies an independently stronger observation bound. The existing annihilator's endpoint identity alone is insufficient. S01, S05, S06 and GEO-T1 should resume only when a different consumer or source-acquisition bottleneck makes their tested limitations irrelevant. Finite extension work should retain the existing requirement of a demonstrated advantage.

This order ranks prospects for an additional estimating result. For the most mature results already available, the manuscript's carrier/rigidity/control theorems and finite/exterior certificates remain the stronger foundation. For scalable new analysis, S04 is the most developed companion to S03.

## Review findings and documentation corrections

No blocking discrepancy emerged in the derivations and selected numerical assertions examined here. The main scientific limitation is explicit and unchanged: the signed complete field has not been controlled through the remaining real bridge or the required complex exterior. The positive packet results, fixed-pilot residual estimate, averaged theorem and geometric constructions must retain their different domains and logical roles.

Three small synchronization corrections would make the research entry points more reliable:

- The original guide's advice to begin with S02, and the symmetry overview's opening priority paragraph naming S03-T1/T2, S01-T1, S02-T1/T2, S07-T1 and GEO-T1 as future work, describe an earlier stage. Their current bounded deliverables are complete. Add a dated pointer to the latest tracker and a current-priority paragraph; preserve the chronological task contracts and execution logs.
- The progress summary's compact S05 row still lists only source-range improvements and an outstanding transfer to a named consumer. Its later S05 section and tracker already record the completed T2 shifted comparison. The compact row should state the small complete added-error gain and absence of a physical-margin or cost advantage.
- The compact S04 row should distinguish the completed uniform local residual theorem from the still-open coherent global corrected-residual transfer and positive anchor margin. The detailed text already makes this distinction.

The manuscript is the pinned 18 October integration; the subsequent 19 October achievements live in the symmetry notes. They should not be attributed to that manuscript version until incorporated. These are documentation recommendations in this review; the source plans, summary and manuscript have not been rewritten.

## Fresh verification and its limits

The following replays passed using the existing scripts. Numerical intervals and source hashes are recorded in the [review receipt][receipt].

| Replay | Fresh result |
| --- | --- |
| Manuscript scalar certificate | All nine printed table rows, eight headline upper bounds and inherited original-table checks pass. |
| S03 complete edge | Requested 192/256 bits, with 512 guard bits: complete edge-model error about \(5.357352425\times10^{-8}\), below the \(6\times10^{-8}\) cap; derivative caps retained. |
| S03 complete arithmetic increment | Requested 192 bits with guard precision: 0.0008532843160075681, below 0.000854. |
| S03 dependency and input guards | All seven cases pass using the required two-precision edge record. |
| S04 signed Gaussian theorem | 192-bit scalar audit: moving intermediate radius about \(1.381281112\times10^{-6}\); complete average radius about 0.1051103465. |
| S04 local transfer | 192-bit scalar and structural audit: opening increment about 0.09011038166; invalid-input, source-mutation and cancellation checks pass. |
| Existing source-specific collision controls | All five event fixtures reject strict first-jet and signed acceptance; the finite-Euler negative-Laguerre witness is retained. Each fixture uses its own source contract. |

The source hashes of the manuscript were also checked against the build record. The full finite-wall, 314-strip and 40-cell manuscript certificates, and every historical S01–S07 comparison, were not all re-executed in this review; their existing receipts and later matched comparisons retain their original scope. The S04 scalar replays support the constants in written uniform proofs and do not replace those proofs. The control replay checks its existing interfaces, rather than asserting that every new theta-specific estimating theorem applies to every control.

The resulting disposition is to retain the established claims at their stated scope, prioritize S03 with S04 for new analytic work, and preserve the completed negative comparisons as constraints on further attempts. No task activation, enlarged certificate or Newman-bound improvement is recorded by this review.

[manuscript]: ../manuscript/positive_arithmetic_packets/main.tex
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[guide]: ../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[assessment]: ../symmetries/01_SEVEN_PROGRAM_REVIEW_AND_RESEARCH_PRIORITIES_20261018.md
[overview]: ../symmetries/research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[geometry]: ../symmetries/research-overview/02_S07_MISSING_ESTIMATES_AND_ALTERNATIVE_APPROACHES_20261018.md
[summary]: ../symmetries/summary/01_SYMMETRY_RESEARCH_PROGRESS_SUMMARY_20261019.md
[tracker]: ../symmetries/research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta-summary]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../avoid/README.md
[packets]: ../manuscript/positive_arithmetic_packets/sections/02_packets.tex
[positivity]: ../manuscript/positive_arithmetic_packets/sections/03_positivity.tex
[modular]: ../manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[finite-controls]: ../manuscript/positive_arithmetic_packets/sections/05_controls.tex
[shifted]: ../manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex
[tails]: ../manuscript/positive_arithmetic_packets/sections/08_effective_tails.tex
[finite]: ../manuscript/positive_arithmetic_packets/sections/09_finite_certificates.tex
[outer]: ../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[global]: ../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex
[s01-2]: ../symmetries/01_modular_self_duality/notes/02_COMPLETE_PAIRED_TAIL_CONSUMER_AND_STOPPING_DECISION_20261019.md
[s02-3]: ../symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[s03-5]: ../symmetries/03_normalized_jet_rotation/notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md
[s03-6]: ../symmetries/03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md
[s03-7]: ../symmetries/03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md
[s04-1]: ../symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[s04-2]: ../symmetries/04_time_height_scaling/notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md
[s04-3]: ../symmetries/04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md
[s05-3]: ../symmetries/05_covariant_theta_jets/notes/03_COMPLETE_SHIFTED_ACQUISITION_AND_CONSUMER_COMPARISON_20261019.md
[s06-5]: ../symmetries/06_hodge_and_transverse_geometry/notes/05_BOUNDED_COMPLETED_CURRENT_AND_DIRECT_COMPARISON_20261019.md
[s07-3]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md
[s07-4]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md
[s07-5]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/05_OBSERVATION_OPTIONS_AND_BOUNDED_FEASIBILITY_SCREENS_20261019.md
[geo]: ../symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[receipt]: ../numerics/MANUSCRIPT_SYMMETRY_REVIEW_REPLAY_20261019.json
