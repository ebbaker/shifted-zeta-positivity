# Arithmetic collision rigidity in the fixed function research program

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewing model: **gpt-6-astra (Codex)**; actual reasoning effort: **xhigh**, read from this turn's recorded metadata.

**Assessment:** Project 11 has established useful structural distinctions, quantitative arithmetic approximation theorems and bounded physical consequences. Its original ambition remains partly open: the complete arithmetic relations have not yet yielded a new collision-incompatible restriction for the genuine theta field over the difficult intermediate regime. The next primary task should estimate the retained signed arithmetic sum using its actual height dependence. Faster acquisition is a supporting objective when attached to a specific mathematical application.

This is an internal, source-based mathematical and strategic assessment, including same-model assessment of Astra work and cross-model assessment of Sol work. It examines theorem statements, central cancellation and control arguments, the newer UAR integration, and relevant predecessor obstructions. It does not independently verify every manuscript proof or rerun the numerical certificates. The accompanying [source receipt](../numerics/FIXED_FUNCTION_PROGRAM_REVIEW_RECEIPT_20261019.json) identifies the reviewed files and verifies the current manuscript against its build record. No new exclusion theorem is asserted.

## The objective and the current manuscript

The [broader plan](../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md) prioritizes a potentially notable structural result about zeta or a fixed character. It explicitly permits research risk and meaningful intermediate theorems without a new numerical Newman bound. Its original Project 11 question had two parts: match a hypothetical local event to complete exterior arithmetic data, then constrain those data independently. The first part has been completed. The second has useful auxiliary estimates and scoped obstructions, but its decisive signed implication remains open.

The current [manuscript](../manuscript/positive_arithmetic_packets/main.tex) is the fourteen-file source set associated with the 52-page build and source-set hash `90dbe4dc121246529958bc20d1ee7ccc789285f269e1fad398453e4f6fb37cb2`. Review 17 assessed the preceding thirteen-file version. [Review 18](18_UAR_ANALYTIC_MANUSCRIPT_AND_GENERALIZATION_REVIEW_20261019.md) and current Section 13 already incorporate the UAR results, an arbitrary-endpoint residual estimate, and a qualitative compact-band extension. Review 17's manuscript-integration recommendation has therefore been acted on; its substantive bottleneck assessment remains applicable.

The repository [result summaries](../../../../result-summaries/README.md) and [patterns to avoid](../../../../avoid/README.md) set the assessment standard. Especially relevant are [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [local laws and equivalent criteria](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [target reformulations](../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [paired estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## What Project 11 has accomplished

| Accomplishment | Contribution to the broader objective | Remaining limitation |
| --- | --- | --- |
| Complete dilation packets and collision matching | Correctly connects local jets to shifted observations, lower intervals and reflected terms | The matching equations alone do not contradict a collision |
| Positive carriers and sharp logarithmic bounds | Supplies a globally regular arithmetic normalization and an energy-scale payment of at most E/64 | The signed normalized Laguerre term remains uncontrolled |
| Full reflection rigidity and finite-prime controls | Separates exact source identification from finite arithmetic compatibility | Source uniqueness is not an estimate for the sign of its transform |
| Reflection before truncation and effective tails | Preserves cancellations essential to approximating the physical field | An absolute approximation needs a physical lower margin |
| Coherent cutoff matching and complete uniform residual | Provides an actual quantitative estimate through a growing, changing arithmetic cutoff | The retained first jet can still be small |
| Finite and eventual real certificates | Demonstrates that complete estimates can produce physical conclusions | Coverage is disconnected and does not imply a new Newman bound |

The carrier result is mathematically substantive. Higher modes have positive real part in a specified strip; their logarithmic curvature is bounded; the selected positive tail is approximated extremely accurately. The manuscript also proves why these facts stop short of the target. All algebraic endpoint terms cancel only in the complete theta source. Omitting even a tiny fixed positive tail changes the asymptotic behavior. Near a collision, a fixed absolute or carrier-relative error is not an error proportional to the vanishing physical energy. [Sections 3–4](../manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex) make this distinction precise.

The rigidity/control pair is the clearest structural lesson. In the polynomial-growth even integer-comb class, exact normalized reflection fixes the coefficients. Yet a fixed finite prime set, coefficient prefix and finite list of linear measurements can be preserved by positive coefficient perturbations arbitrarily close to theta that collide at remote heights. The latter extends earlier source-measurement work; reflection rigidity itself also has a predecessor in Investigation 22. These results should be presented with that provenance, without a literature-wide novelty claim. The controls fail full source reflection and do not prescribe a bounded event height. They do not exclude a height-dependent hierarchy of measurements or a finite formula that genuinely consumes complete modular information. [Section 5](../manuscript/positive_arithmetic_packets/sections/05_controls.tex).

The strongest recent analytic result is the coherent UAR construction. Entering modes are cancelled against the matching Riemann–Siegel edge before estimation. The complete ordinary residual integral, including its switch sum, satisfies

\[
\sup_{x\in J_t}|\mathcal I_t(x)|<3.246e^{-13/(16t)},\qquad
J_t=[4\pi e^{1/t},4\pi e^{2/t}],\quad0<t\le1/20.
\]

This is a proved-in-note upper estimate with checked constants, not another nonvanishing criterion. The current arbitrary-endpoint corollary improves rebasing within that sector. The compact-band extension concerns edge errors and corrected transitions with band-dependent constants and onset; it does not extend the complete residual theorem or physical coverage automatically. [Section 13](../manuscript/positive_arithmetic_packets/sections/13_uniform_coherent_edge.tex).

Physical consequences include noncollision for `0<t<=.2, |x|<=1000`, the extension to `|x|<=1001` on `.01<=t<=.2`, and the eventual real region `epsilon<=t<=1/2, |x|>=exp(20/epsilon)`. The small UAR box near `4*pi*exp(20)+1` has spatial width `.02` and time width `1e-14`; it is an additional island. The common-slab bridge remains `1001<|x|<exp(2000)`. Eventual reality at heights of exponential order in `1/t` is already a published phenomenon; the explicit onset is a repository improvement, not by itself a new structural phenomenon. See [Polymath, Theorem 1.5](https://arxiv.org/html/1904.12438v2#S1.Thm5).

## The estimating problem that remains

With the symmetric normalizer, write `Q=H/A`, `f_N=(G_N-C_N)/A` using the prescribed analytic correction, and `r_N=Q-f_N`. At a real common zero,

\[
(f_N,-(f_N)_x/\omega)=-(r_N,-(r_N)_x/\omega).
\]

The complete endpoint estimate therefore forces the approximant first jet into an explicitly small disk. The missing arithmetic question is what prevents that simultaneous cancellation, or what additional nontrivial restriction it forces. The prefix-integral theorem and the endpoint enclosure have distinct contracts and must not be substituted for one another.

The completed comparison quantifies the priorities. In the UAR box, paid approximant variation is about `1.0051`; the direct residual allowance is below `1.341e-7`. Improving the latter cannot materially repair the former. Direct certification already uses the new analytic estimate and beats the tested transport variants with the same dominant acquisition. The general rebasing corollary does not reverse that result. [UAR-06](../symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md).

Two predecessor results make the next task more precise. The earlier [collision-reductions manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), at labels `sc:character` and `sc:remaining`, constructs complete multiplicative phase twists whose model first jet vanishes. Actual-height realization is explicitly absent. Thus multiplicativity alone cannot support the desired universal vector bound: a new estimate must retain the common height, its logarithmic phases, heat weights, normalizer and cutoff together. Its fixed-order derivative bounds also have a stated macroscopic-block deficit; subdividing and adding those same upper bounds does not remove it.

The same manuscript's derivative mean square and Taylor-deficit analysis already shows why average mass does not exclude an isolated event. S04's newer Gaussian functional is a worthwhile signed estimate in a different norm, but it still only forces mass somewhere in its window. A new average-to-point argument must prove a quantitatively compatible concentration or variation estimate; another average alone repeats the unresolved step.

## Recommended next round

**Make a restricted estimate for the genuine retained arithmetic sum the primary project.** Start within the existing explicit sector so that approximation errors are already paid. Keep the exact reflected scalar and its actual derivative, including amplitude drift and analytic correction. Use the existing low, intermediate and terminal decomposition to locate the signed interaction that dominates the bound. Select one cross-block correlation or complete packet pairing and derive a bound that improves its present absolute estimate on a stated subdomain. A bound for the squared jet obtained merely by rewriting its expansion is a reformulation; the new work must estimate a term using arithmetic information not present in that identity.

The first acceptable output need not exclude all events. It could be a new quantitative restriction on simultaneous small values, a restricted separation theorem whose proof does not assume separation, or a signed correlation estimate with an explicit transfer loss. Report the domain and numerical or asymptotic gain. An estimate valid for almost all heights remains an intermediate result: a measure-zero exceptional set can still contain collisions. A useful lower margin may depend on time and height; a positive constant uniform over an unbounded family should not be assumed without justification.

**Use threshold information as a possible narrower consumer.** If the aim is to rule out a positive Newman threshold, all zeros are real at that threshold. The predecessor manuscript already derives the deflated mirror constraint, for an ordinary double zero,

\[
2H_3^2-3H_2H_4\ge9H_2^2/x_*^2.
\]

This supplies extra global information absent from an arbitrary heat germ. A focused continuation could ask whether the genuine arithmetic sums, conditioned on the two necessary small first-jet coordinates, restrict this fourth-jet expression more strongly on a declared regime. The mirror inequality and its paid conditional test already exist; deriving them again would not be progress. New arithmetic input is required. The complete second-through-fourth-jet errors must be paid, and the fourth-jet condition is uninformative at multiplicity at least four. Such a restricted result could still justify extension, with higher multiplicity remaining explicit.

**Retain quantitative modular rigidity as a higher-risk alternative.** Seek an effective relation between a specified reflection defect, a growing set of coefficient/dilation constraints and the particular signed observation that collision matching exposes. Fix the source class, weights, cutoff and physical norm before attempting inversion. Exact uniqueness does not imply a stable inverse, and the existing controls forbid a uniform all-height conclusion based on a fixed finite measurement set and ordinary absolute closeness. A meaningful first result would quantify the growth or conditioning required as height increases, or establish a useful trace estimate with that cost included. This direction is closer to the original exterior-rigidity question, but currently has less developed estimating machinery than the retained-sum route.

I would pursue the retained-sum route first and activate this alternative when a concrete observation operator and norm can be specified. Neither proposal is a newly proved theorem or an assurance of feasibility.

## Roles for the neighboring projects

| Project | Focused contribution now |
| --- | --- |
| 08 Modular oscillator estimates | A weighted trace or bilinear estimate for the exact observation selected by 11, including physical heat weights and boundary costs |
| 09 Coupled arithmetic dilations | A signed estimate for complete blocks with lower intervals and reflected terms retained, plus a summable assembly cost |
| 10 Modular auxiliary functions | An admissible auxiliary functional estimating that same signed quantity, with a demonstrated physical implication and complete tails |
| 12 Fixed beta eta kernel | A second fixed-function test after proving its own source, normalization and transfer identities |

Projects 08–10 should receive one precise estimate request from 11. Launching broad independent programs before selecting that request would weaken the connection between their outputs and the collision question. Beta is useful if its eta structure makes the selected estimate more accessible; theta constants cannot be transferred by analogy.

Cheaper acquisition should be compared against optimized direct evaluation on the same data and domain, giving every reusable sum improvement to both methods. Existing [Polymath fast evaluation](https://arxiv.org/html/1904.12438v2#S7) is a relevant baseline. More boxes or a better runtime are valuable when they enable a specified theorem or identify a mechanism; neither alone supplies the structural advance sought in the broader plan.

## Controls and a criterion for continuation

The proposed estimating work must distinguish the actual premises at control events. Positive weighted-square and finite-prime orbit controls fail full normalized reflection or unchanged complete coefficients. Reflected smooth and positive-primitive controls fail the theta square expansion. Euler modifications alter coefficients, arithmetic level or lattice. Generic polynomial heat germs lack the full theta source and Riemann–Siegel contract. The multiplicative-phase relaxation additionally tests whether an argument has discarded actual-height coupling. These are separate controls; none should be credited with all the others' premises.

This review screens proposed mechanisms by their premises; it makes no new numerical acceptance claim. A future quantitative consumer must run with each control's own source errors on a domain containing its event or relevant negative witness, as required by the [control summary](../../../../result-summaries/12_collision_controls_and_screening.md).

Continue after one coherent round if it supplies an applicable arithmetic estimate, a new event restriction, meaningful domain extension, or a precisely scoped obstruction that changes the choice of mechanism. Stop iterations that only reduce already negligible tails, enlarge known pilots, or repackage the same uncertain first jet. Obtain focused external scrutiny of the coherent edge and saddle matching before relying on them for a substantially stronger theorem.

A more ambitious regional noncollision theorem, or a new arithmetic restriction on threshold collisions, would fit the broader goal even before a Newman improvement. A Newman-bound application separately needs its complete real bridge or the specified complex exterior and barrier hypotheses. The current microscopic complex disks do not supply a fixed-width exterior strip. [Section 11](../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex) and [Polymath's barrier theorem](https://arxiv.org/html/1904.12438v2#S1.Thm2) retain that distinction.
