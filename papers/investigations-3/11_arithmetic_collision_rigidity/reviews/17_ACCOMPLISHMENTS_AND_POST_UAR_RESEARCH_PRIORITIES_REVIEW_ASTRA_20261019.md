# Arithmetic collision rigidity accomplishments and research priorities

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewing model: **gpt-6-astra (Codex)**; actual reasoning effort: **max**, verified from the reviewing turn metadata.

This is an internal LLM assessment, including cross-model assessment of Sol work and same-model assessment of Astra work. Selective fresh calculations use the existing implementations. It is not specialist human review or an independent numerical implementation.

**The strongest new analytic result is the complete uniform arithmetic residual estimate in UAR-04, made possible by UAR-03's coherent cutoff matching and S04's scaling framework.** The program has also acquired a physical noncollision certificate on one small box near height \(6.1\times10^9\). Its latest complete comparison establishes that direct certification has the better margin with the same dominant computation.

**The research priority should therefore move from obtaining a uniform residual estimate to controlling the retained approximant's first jet over a useful domain, or reducing the cost of acquiring that information.** The manuscript's positive-carrier, modular-rigidity, collision-control and finite/exterior results remain its most mature foundation. The real bridge and required complex exterior remain open; no improved Newman bound follows.

## Scope and current source version

This assessment covers the [manuscript][manuscript], the requested [18 October research guide][guide], the [original symmetry plan][sym-plan], [geometric alternatives overview][sym-geometric], [uniform-residual program][sym-uar], the requested [progress summary][summary1], and the relevant proof notes and comparisons linked below. The later [uniform-residual summary][summary2] and [execution register][uar-progress] are essential: they record UAR-01 through UAR-06 after the earlier summary and manuscript integration.

The current manuscript has thirteen TeX files and a recorded 48-page build. All thirteen source hashes match its [build record][build], with source-set SHA-256

4ad46c6a95ff04c0ab7acd3b4c2433d24ad08e5915dde3dd0c73342c226dfa70.

The checkout HEAD at review was 5f8092d78fbf7c50f1c212b9eaced525481ade5e. The [review receipt][receipt] fixes the reviewed source identities and fresh replay results. [Review 15][previous] assesses the preceding stage; its proposed uniform-residual and bounded-anchor tasks have now been completed. This review updates their disposition.

Write \(E=H^2+H_x^2\) and \(\mathcal L_0=H_x^2-HH_{xx}\). In the symmetry work, \(Q=H/A\), \(\omega=\theta_x<0\), and \(J_Q=(Q,-Q_x/\omega)\). The symmetric normalizer \(A\) is distinct from the manuscript's positive arithmetic carrier. A bound in one normalization requires its stated conversion before it becomes a physical bound.

The [result summaries][results], [collision-control record][controls] and [patterns to avoid][avoid] govern the assessment, particularly [target reformulations][avoid1], [scoped negative results][avoid7] and [signed recombination][avoid12].

## Established manuscript accomplishments

**Positive carriers now have explicit quantitative control.** The exact packet construction retains the shifted lower integration interval, mixed-prime terms and reflected derivative signs. Higher-mode positive carriers have positive real part in an explicit complex strip. For a real carrier beginning at mode 2, the logarithmic derivative obeys \(\alpha^2+|\alpha_x|\leq1/64\). With the original coefficients, the \(\{2,3\}\) carrier approximation has relative tail below \(7.3\times10^{-25}\), together with derivative and strip estimates. These are strong, clean carrier theorems. [Packet construction][packets] [Positivity and constants][positivity]

**The manuscript identifies why these positive estimates do not settle the signed field.** Complete modular reflection cancels all algebraic endpoint tails. A fixed positive-tail omission changes that cancellation, so extraordinarily accurate carrier approximation does not imply a relative margin for \(H\) near a zero. The normalized Laguerre identity pays the carrier contribution by \(E/64\), while its decisive signed term remains uncontrolled globally. This diagnosis prevents an attractive but invalid inference from positive components to collision exclusion. [Modular cancellation][modular]

**Full modular rigidity and finite arithmetic compatibility are sharply distinguished.** In the stated polynomial-growth even integer-comb class, exact normalized theta reflection forces constant coefficients. Conversely, bounded positive coefficient perturbations arbitrarily close to one can preserve a fixed finite prime set, a prescribed prefix and finitely many linear measurements while producing nondegenerate positive-time collisions at sufficiently high height. These controls lose full modular reflection, and their event heights are not effective. The two results together explain which arithmetic information has actually been retained. Their significance is structural; they do not assert that every possible finite observation of the theta field is useless. [Rigidity][modular] [Finite-prime controls][finite-controls]

**Complete approximation leads to actual finite and eventual real certificates.** Reflecting before truncation preserves cancellation. The nonstationary tails pay omitted modes and derivatives; constant-distance contours with \(A_c=33\), \(b=1/8\) give errors below \(7\times10^{-11}G_0\), with \(G_0=x^{7/4}e^{-\pi x/8}\), for \(x\geq1000\), \(0\leq t\leq1/2\), and \(|\operatorname{Im}z|\leq1\). The finite computation proves \(\mathcal L_0>E/100\) on \([.01,.2]\times[25,45]\) and \([.01,.2]\times[999,1001]\), and supplies a complete vertical wall at \(x=1000\). [Approximation][shifted] [Tail estimates][tails] [Finite certificates][finite]

Together with the named published initial-zero and heat-flow inputs, these yield

\[
E(t,x)>0\quad(0<t\leq.2,\ |x|\leq1000),
\]

and extend to \(|x|\leq1001\) on \(.01\leq t\leq.2\). The eventual real theorem gives

\[
E(t,x)>0\quad(\varepsilon\leq t\leq1/2,\quad
|x|\geq e^{20/\varepsilon}),
\]

improving this investigation's earlier onset \(e^{64/\varepsilon}\). The imported inputs remain dependencies, principally [Polymath's heat-flow and approximation results](https://arxiv.org/html/1904.12438v2) and [Platt and Trudgian's initial-zero verification](https://arxiv.org/abs/2004.09765). This review makes no literature-wide novelty claim for the threshold. [Exterior theorem][outer]

These results leave the bridge between \(1001\) and \(e^{2000}\) unclosed on the common slab \([.01,.2]\). The later UAR box is a small certified island inside that range. The required complex exterior is a separate obligation. The manuscript's possible \(\Lambda\leq.18\) application remains conditional on the further complex nonvanishing theorem and its consumer hypotheses. [Global scope][global]

## What the symmetry programs have contributed

The programs have produced reusable estimates, actual physical certificates and useful stopping decisions. Completion of a comparison includes a rigorously recorded failure of its proposed advantage.

| Program | Accomplishment | Current assessment |
| --- | --- | --- |
| S01 Modular self-duality | Complete paired-endpoint errors improve by approximately 14.85%, 7.22% and 2.99% at orders 0–2; the 40 signed intervals and 116 calls are unchanged. | Preserve the theorem; further tail tuning on the same pilot has little support. |
| S02 Cutoff reflection | Coherent analytic correction and coupled value/derivative errors certify all 4096 pilot cells, versus 1770 using independent frozen derivative boxes. | Important infrastructure for complete residual estimates; the best source-informed direct comparator remains stronger. |
| S03 Normalized jet rotation | The fixed-pilot independent arithmetic increment is below 0.000854; the later UAR round supplies uniform residual control and a paid physical box. | Leading analytic direction, with the tested transport consumer now stopped. |
| S04 Time-height scaling | Uniform full-cutoff model, signed Gaussian average within 0.11 of one, and weighted energy above 0.198. | Strongest uniform companion to S03; averaged mass alone does not exclude a common zero. |
| S05 Covariant theta jets | Completed shifted acquisition gives roughly 0.008–0.009% improvements in complete added errors. | Retain the small error improvement; no physical-margin or cost advantage supports more tuning on this pilot. |
| S06 Hodge and transverse geometry | Exact source completions and a paid four-jet comparison: selected current certifies 60/64 cells, direct certifies 64/64. | Existing geometric extraction loses with the same input information. |
| S07 Geometric duality | Explicit five-dimensional theta-jet space, necessary residual complement and complete trace-cost comparison. | Valuable admissibility analysis; a useful new observation estimate is still missing. |
| GEO-T1 Winding | Degree-zero certificate on the pilot with complete boundary payments. | Alternative certificate; ten calls versus seven for optimized direct, with the factor-two cost gate failed. |

The underlying completed comparisons are [S01][s01], [S02][s02], [S05][s05], [S06][s06], [S07][s07-4] and [GEO-T1][geo]; the earlier [S03 arithmetic theorem][s03-local] fixes the local increment's scope.

Three limitations matter when ranking these results. First, S04's phase-matched average gives mass somewhere in a window, but an isolated simultaneous zero of \(H,H_x\) is compatible with that mass. Locating and paying a useful anchor requires more information. Second, S06's second completed current is positive at a nondegenerate collision; that positivity cannot itself be an exclusion criterion. The four unsuccessful intervals in the later current comparison are inconclusive, not proofs of negativity. Third, S07's tested whole-profile rule assigns value and derivative payments over 1618 and 34152 times the direct tail allowances. Those are floors for that rule's payments, not lower bounds on the actual theta error or a general obstruction to geometry. [S04 averaging][s04-average] [S06 completion][s06-completion] [S07 residual class][s07-3] [S07 alternatives][s07-5]

## The uniform residual theorem is the leading new result

The UAR round joins S03's corrected arithmetic approximation to S04's sector:

\[
0<t\leq1/20,\qquad
J_t=[4\pi e^{1/t},4\pi e^{2/t}],\qquad
L=\log(x/(4\pi)).
\]

For each fixed \(t\), this is a finite height interval. The family reaches unbounded height as \(t\downarrow0\); it does not cover all heights at a fixed positive time.

The [UAR-01 contract][uar1] fixes \(f_N=(G_N-\widehat C_N^{\rm an})/A\), \(r_N=Q-f_N\), the analytic reflected channels, frozen cutoffs and switch ownership. The ordinary piecewise residual integral has the endpoint identity

\[
\mathcal I_t(x)=i\left[
Z_{r_{N(x)}}(x)-Z_{r_{N(a_t)}}(a_t)
+\sum_{a_t<\xi_n\leq x}Z_{h_n}(\xi_n)
\right],
\qquad
Z_v=e^{-i\theta}(v-i v_x/\omega),
\]

with \(a_t=4\pi e^{1/t}\) and \(h_n=f_n-f_{n-1}\). The positive switch sum is essential. Omitting it changes the quantity being bounded.

Three substantive estimates follow.

1. **UAR-02 retains the prescribed finite gamma/heat correction and bounds its remainder uniformly.** The rotating remainder is below \(1.9\times10^{-16}\) throughout the sector. The proof retains full weights near the growing cutoff and pays both Gaussian tails; it is not a fixed-mode asymptotic extrapolation. This number concerns the remainder after retaining a correction, not the complete residual. [Finite theorem][uar2]

2. **UAR-03 makes the edge and cutoff matching uniform.** A common bounded contour with the true gamma factor has rotating model error below \(3.9\times10^{-34}\). Its corrected transitions have a summable prefix allowance below \(2.639\times10^{-7}\). Compensation between the entering mode and the adjacent edge removes the earlier divergent payment for raw modes. No favorable cancellation between different crossings is assumed. The very small model error does not bound the retained integral's value. [Coherent edge theorem][uar3]

3. **UAR-04 bounds the complete ordinary integral over every prefix:**

\[
\boxed{\sup_{x\in J_t}|\mathcal I_t(x)|
<3.246e^{-13/(16t)}<2.846\times10^{-7}.}
\]

Its proof cancels the leading saddle profile and retains the signed Gaussian first moment before taking norms. Coupled rotating estimates give edge and finite endpoint coefficients below 0.97 and 0.558 in the scale \(S_x=e^{-3L/4-tL^2/16}\). A decreasing transition envelope then pays every prefix, with all remaining errors included. This analytically encloses the retained expression without calibrating against values of \(H\) or evaluating a retained contour quadrature. [Complete theorem][uar4]

This is more consequential than another small fixed-pilot error improvement: it survives growing cutoff, changing height and every switch in a declared uniform family. Its allowance is below 0.684 of a specified independent published-error-box allowance floor. That comparison is restricted to the stated error accounting, and says neither that the actual error shrank by that factor nor that a complete physical algorithm became faster.

UAR-03's coherent matching is the key reusable mechanism; UAR-04 is the strongest completed quantitative result. They also show why the earlier S04 obstruction was correctly scoped: a losing raw-mode payment did not forbid a better corrected combination. The earlier fixed-pilot bound of 0.000854 and the new sector bound use different domains and contracts, so their numerical ratio is not a matched improvement factor.

## The paid anchor succeeds while transport loses the matched comparison

[UAR-05][uar5] certifies the exact closed box

\[
D=[1/20-10^{-14},1/20]\times[u-.01,u+.01],
\qquad u=4\pi e^{20}+1,\qquad N=22026.
\]

The approximant anchor has rotating norm above 1.5441778256. Its complete signed variation over the box costs less than 1.0051. After all residual payments and the normalizer conversion, \(|J_Q|>.539\) and \(E/A^2>.27\). This is an additional bounded physical certificate. Its very thin time interval and height width 0.02 must remain explicit; it does not provide uniform anchors or separation throughout \(J_t\).

[UAR-06][uar6] compares three complete methods on precisely that box and data:

| Method | Certified rotating norm | Certified physical energy \(E/A^2\) |
| --- | ---: | ---: |
| Global rebased transport | \(>.53908342\) | \(>.27778597\) |
| Refined local transport | \(>.53908372\) | \(>.27778628\) |
| Matched propagated direct | \(>.53908399\) | \(>.27778656\) |

The comparison has a structural explanation. Write \(a\) for the acquired anchor bound, \(v\) for paid approximant variation, \(e_u,e_x\) for complete endpoint errors, and \(B\) for the uniform prefix bound. Direct pays \(a-v-e_x\); global transport pays \(a-v-e_u-2B\); local transport pays \(a-v-e_u-2e_x\). The factor two is required when rebasing a prefix theorem from \(a_t\) to \(u\).

All methods use the same nominal approximant. Direct's uncertainty disk is contained in either independently paid transport disk, and the common physical linear map preserves that inclusion. Keeping exact anchor/increment correlation recovers the endpoint residual; with the presently available estimate, that ties direct rather than surpassing it. This is a result about the current information and bounds, not every possible transport construction.

Each method uses 44,052 finite-mode evaluations and 110,130 moment accumulations per production precision. Direct has fewer error payments. The common acquisition graph supplies no mechanism for the proposed factor-two saving. UAR-06 therefore correctly stops this configuration and adds no coverage beyond the UAR-05 box; it does not retract UAR-02–05. The strongest direct certificate itself uses the new complete endpoint theorem, so the analytic progress remains useful after transport is stopped.

The budget identifies the next obstacle. The direct residual allowance is below \(1.341\times10^{-7}\), while the paid approximant variation is about 1.0051. Even removing the residual allowance entirely, with the same acquired data and propagation, would improve the direct rotating lower bound by less than \(1.341\times10^{-7}\). Further accuracy in the already tiny finite or edge remainders cannot materially change this comparison. The retained sum, its variation, and the cost of enclosing them deserve priority.

## Research priorities after the completed comparison

**First priority: arithmetic control of the retained first jet.** Use the coherent approximation and complete endpoint envelope already established to seek a quantitative separation result for \((f_N,(f_N)_x)\) on a stated useful domain, including cutoff behavior and the physical normalization. The missing input is a new estimating mechanism for the oscillatory retained sum. Merely restating a positive first-jet margin as the desired theorem would repeat the target. S04's average may help only if a new argument quantitatively connects its mass to an acquired anchor and controlled variation.

**Second priority: cheaper complete acquisition.** A proposed reusable sum, correlation estimate or observation method should identify exactly which dominant operation it removes. Give the same improvement to direct certification in the comparison. Residual transport deserves reopening only if it supplies information or savings unavailable from the current endpoint bound. The present UAR-E1 extension and UAR-G1 geometric gates remain conditional; the failed comparison does not justify a larger numerical sweep.

**Consolidate the mature theorems and obtain focused external scrutiny.** The manuscript has a coherent core in carriers, rigidity versus finite controls, complete evaluation, and finite/exterior exclusion. The next mathematical integration should add UAR-02–04 with their definitions and proof dependencies, then the exact UAR-05 domain and UAR-06 disposition. The delicate coherent edge, alternate-cutoff saddle identity, analytic correction and coupled derivative bound are the best targets for an independent specialist or separate implementation review. This is a recommendation for verification and presentation, not a claim of publication novelty.

**Keep the bounded stopping decisions.** S01 and S05 should resume when their errors become dominant in a different application. S06, S07 and GEO-T1 need a new useful observation estimate or acquisition advantage. Their exact identities and admissible spaces remain resources; changing representation alone does not overcome the recorded comparisons.

For results already mature, the manuscript's rigidity/control pair and finite/exterior certificates rank highest. For prospective additional analysis, UAR-03/04 with S04 rank first. Geometric routes remain exploratory until they provide a quantitatively useful estimate.

## Current documentation findings

The main synchronization issue is that current entry points still describe completed work as future work:

- [Manuscript Section 12][sym-section], especially its final subsection, leaves uniform corrected control, coherent matching and a paid anchor as future tasks. The [manuscript README][ms-readme] says new mathematical work has not begun. These accurately describe an earlier integration cutoff, but now need an explicit historical cutoff or a current UAR update.
- The [investigation README][root-readme] calls UAR-06 Ready. The [latest register][uar-progress] and [round summary][summary2] record its completed losing comparison and stopping decision.
- The requested [first progress summary][summary1] remains useful for the completed original symmetry round. Its continuation link should be treated as essential; its earlier recommendations are not the current task queue. Preserve chronological task contracts and earlier review conclusions at their original source versions.

A new manuscript integration should distinguish the existing broad finite certificate, the small additional UAR-05 island, and the still-unclosed bridge. This review records those corrections without changing the manuscript or research plans.

## Fresh checks and review disposition

Selective fresh replays passed:

| Check | Result and scope |
| --- | --- |
| Manuscript source identity | All thirteen TeX files match the recorded build source set. |
| Manuscript scalar certificate | Nine table rows, eight headline checks and inherited original checks pass. |
| UAR-02 | Stored 192/256-bit scalar bounds reproduce with source identities checked; finite component only. |
| UAR-03 | Stored 192/256-bit edge and transition constants reproduce; model error and corrected transitions. |
| UAR-04 | Stored 192/256-bit complete-prefix scalar calculations reproduce. Opening ceiling is \(2.844874972032\times10^{-7}\). |
| UAR-06 and inherited UAR-05 acceptance | All three physical calculations reproduce at 192/256 bits; source-specific controls are rerun. |

The last replay includes the five existing event rejections and the separate Euler negative-Laguerre witness. Each uses its own source errors. Finite-prime and weighted-square controls do not retain the unchanged full theta coefficients/reflection; smooth, reflected and positive-primitive controls lack the required theta expansion; Euler modifications change level or coefficients. Generic rotation and anchor identities alone do not distinguish these sources.

The [receipt][receipt] records exact commands, source hashes and verification scope. The computations check constants and bounded acquisitions; the written analytic arguments carry the uniform claims. This review did not rerun every earlier symmetry experiment or the full 314-strip, 40-cell and wall computations, and did not repeat historical timing benchmarks. Their existing receipts retain their scope. Primary-source checks included [Polymath's Riemann–Siegel estimates](https://arxiv.org/html/1904.12438v2#S6) and the [DLMF complex Stirling remainder guidance](https://dlmf.nist.gov/5.11#ii).

No blocking mathematical discrepancy emerged in the examined derivations and selected replays. Retain the stated auxiliary theorems and bounded physical results, update the current handoff, and direct further estimating work toward retained-sum separation or cheaper acquisition. This review itself establishes no enlarged exclusion domain or Newman-bound improvement.

[manuscript]: ../manuscript/positive_arithmetic_packets/main.tex
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[guide]: ../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[sym-plan]: ../symmetries/research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[sym-geometric]: ../symmetries/research-overview/02_S07_MISSING_ESTIMATES_AND_ALTERNATIVE_APPROACHES_20261018.md
[sym-uar]: ../symmetries/research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md
[summary1]: ../symmetries/summary/01_SYMMETRY_RESEARCH_PROGRESS_SUMMARY_20261019.md
[summary2]: ../symmetries/summary/02_UNIFORM_ARITHMETIC_RESIDUAL_ROUND_SUMMARY_20261019.md
[uar-progress]: ../symmetries/research-progress/02_UNIFORM_ARITHMETIC_RESIDUAL_PROGRESS_20261019.md
[previous]: 15_MANUSCRIPT_AND_SYMMETRY_ACCOMPLISHMENTS_REVIEW_ASTRA_20261019.md
[receipt]: ../numerics/POST_UAR_ACCOMPLISHMENTS_REVIEW_RECEIPT_20261019.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[avoid1]: ../../../../avoid/01_restating_the_target.md
[avoid7]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[packets]: ../manuscript/positive_arithmetic_packets/sections/02_packets.tex
[positivity]: ../manuscript/positive_arithmetic_packets/sections/03_positivity.tex
[modular]: ../manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[finite-controls]: ../manuscript/positive_arithmetic_packets/sections/05_controls.tex
[shifted]: ../manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex
[tails]: ../manuscript/positive_arithmetic_packets/sections/08_effective_tails.tex
[finite]: ../manuscript/positive_arithmetic_packets/sections/09_finite_certificates.tex
[outer]: ../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[global]: ../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex
[s01]: ../symmetries/01_modular_self_duality/notes/02_COMPLETE_PAIRED_TAIL_CONSUMER_AND_STOPPING_DECISION_20261019.md
[s02]: ../symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[s03-local]: ../symmetries/03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md
[s04-average]: ../symmetries/04_time_height_scaling/notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md
[s05]: ../symmetries/05_covariant_theta_jets/notes/03_COMPLETE_SHIFTED_ACQUISITION_AND_CONSUMER_COMPARISON_20261019.md
[s06]: ../symmetries/06_hodge_and_transverse_geometry/notes/05_BOUNDED_COMPLETED_CURRENT_AND_DIRECT_COMPARISON_20261019.md
[s06-completion]: ../symmetries/06_hodge_and_transverse_geometry/notes/03_SECOND_TRANSVERSE_COMPLETION_AND_CURRENT_FEASIBILITY_20261019.md
[s07-3]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md
[s07-4]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md
[s07-5]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/05_OBSERVATION_OPTIONS_AND_BOUNDED_FEASIBILITY_SCREENS_20261019.md
[geo]: ../symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[uar1]: ../symmetries/notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[uar2]: ../symmetries/03_normalized_jet_rotation/notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md
[uar3]: ../symmetries/03_normalized_jet_rotation/notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md
[uar4]: ../symmetries/03_normalized_jet_rotation/notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md
[uar5]: ../symmetries/03_normalized_jet_rotation/notes/11_PAID_ANCHOR_AND_BOUNDED_PHYSICAL_SEPARATION_20261019.md
[uar6]: ../symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[sym-section]: ../manuscript/positive_arithmetic_packets/sections/12_symmetry_findings.tex
[ms-readme]: ../manuscript/README.md
[root-readme]: ../README.md
