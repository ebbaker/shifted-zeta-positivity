# Analytical program for a signed cap-phase surplus

20 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**, verified by the parent from turn metadata. Separate same-model calculations inform this program; no specialist or cross-model review is claimed.

**Status: analytical continuation program prepared; its new estimates are unexecuted.** The objective is to determine whether the complete theta source can contradict the ordinary half-turn of a cap between two continued roots born at a hypothetical positive threshold. The precise possible success is a strictly positive, fully accounted signed phase surplus. No such theta surplus is presently proved. Numerical work is restricted to checks of derived arguments and predeclared validation of a specified inequality; it is not the discovery method for this program.

This program follows [Brainstorm 01][brainstorm] and the [manuscript](../manuscript/main.tex), *Root-Following Heat Contours, Phase Concentration, and the Cap at Infinity*. The [matching register][progress] governs PSC-00–06. The [original BW09 register][bw09] remains authoritative for the ordinary-event class, global coverage, later-collision target and multiplicity extensions. The [HFCE register][hfce] retains its bounded Gaussian and localized-comparison outcomes; those tasks are not restarted or relabeled as phase-surplus work.

Read the [result index][results], [collision controls][controls], and [avoid index][avoid], particularly [reformulations][a01], [control premises][a02], [scope][a07], [question before numerics][a10], [signed recombination][a12], and [gain before expansion][a20]. New analytical discussion and derivations belong in this route's `brainstorm/`, with explicit links to their proof status; numerical checks go in `numerics/`, assessments in `reviews/`. Preserve route chat 0002's established `chat-histories/` identity.

## 1. Established starting point and the missing sign

Use the unchanged complete theta source and physical jet
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad H_t=-H_{xx},\qquad J=H+iH_x.
\]
The inherited ordinary-event hypothesis is conditional:
\[
 0<T=\Lambda\le1/5,\quad a\in[1001,1002],\quad
 H(T,a)=H_x(T,a)=0,\quad h_2=H_{xx}(T,a)\ne0.
\]
Known excluded boxes stay excluded. No event is observed, no nonempty event set is asserted, and no uniform lower bound on \(|h_2|\) is available.

The following are inherited results, not new PSC execution:

* Simple zero walls contribute zero phase. A regular cap between the continued born roots, with \(N\) simple interior zeros, has signed phase decrease \(M=(N+1)\pi\), where \(N\) is even. After paying the initial ordinary event, extra collision requires \(N\ge2\). The physical contour degree is \(-1-N/2\), and the corresponding truncated/regularized degree is \(-N/2\).
* Opposite wall slopes force at least the ordinary \(\pi\). An interior point with \(h_2H(T+R,b)>0\) is equivalent, under the full cap contract, to extra cap roots. It is a scalar restatement of the missing cap information, not an estimate.
* The quadratic has total cap decrease exactly \(\pi\), even when nearly all of it lies in endpoint windows. Its positive middle phase equals the endpoint deficit exactly. The positive atomic actual-threshold control also keeps the ordinary \(\pi\) and has no later collision.
* The complete theta source has a proved-in-brainstorm fixed-index large-time cosine profile. For the large saddle \(L_t\), \(F_t(z)=H(t,z/L_t)/H(t,0)\to\cos z\), and \(L_tx_k(t)\to(k-\tfrac12)\pi\) for each fixed positive index. Globally identifying the selected walls is an additional premise. When they are adjacent fixed labels, the profile gives the ordinary half-turn, with physical phase concentrated near the interior extremum. It gives no excess phase.
* The bounded HFCE round recorded direct exclusion of one small initial box, failure of its frozen Gaussian interval estimator, and positivity of one fixed localized Laguerre comparator. Neither energy computation established a winding sign.

For disjoint endpoint windows and their complementary middle, retain the **signed** decreases
\[
 M=M_{\rm ends}+M_{\rm mid}.
\]
The conditional success gate is
\[
 M_{\rm ends}\ge\pi-\eta_R,\qquad M_{\rm mid}>\eta_R,
 \quad\text{hence }M>\pi.
\]
Quantization then forces \(M\ge3\pi\) and \(N\ge2\). Every endpoint deficit, parameter error, source remainder and continuation obligation must appear in this comparison. Concentration alone is not a contradiction.

## 2. Analytical priorities and bounded tasks

| ID | Deliverable | Dependencies and bounded completion test |
| --- | --- | --- |
| PSC-00 | Program, register and inherited-status reconciliation | Record this analytical scope and links. Documentation only; no new theta estimate. |
| PSC-01 | Explicit source-moment constants and a regime map | First analytical task. Derive a complete finite-onset bound for \(m_1=\mathbb E|U-L|\) and \(m_2=\mathbb E(U-L)^2\), with explicit constants and saddle admissibility conditions. Translate it into phase/root errors for fixed and declared growing spatial-index ranges. Mark every range already controlled by a one-lobe model as ordinary-phase behavior, not a contradiction candidate. |
| PSC-02 | One finite-wall and endpoint-window feasibility contract | Use PSC-01 and the inherited local event law. Select **one** event-conditioned intermediate regime, or one explicitly declared growing-index regime. Establish or identify the precise missing finite-wall continuation, wall-label, cap regularity and window-separation bounds. Test whether relative-curvature bounds and disjoint windows can coexist at the chosen jet scale. A proved infeasibility of this selected window mechanism is a valid scoped result. |
| PSC-03 | One complete signed source estimate preserving event cancellations | Requires an admissible PSC-02 contract or a clearly stated conditional version of it. Compare the phase-current representation with the exact opposite-lobe source target; select one before further estimates. Derive a complete signed bound from theta's unchanged source, keeping the event constraints and correlated signs. Run own-data controls before treating the bound as useful. A target identity or an estimate with an unpaid sign is not completion. |
| PSC-04 | Matched endpoint/middle deficit comparison | Requires the full continuation and estimator premises from PSC-02–03. Assemble one proved lower bound \(\sigma\le M_{\rm ends}+M_{\rm mid}-\pi\), with all payments. Success means \(\sigma>0\). Otherwise record the exact remaining deficit or a scoped obstruction for the declared estimating class; do not change windows or discard endpoint losses silently. |
| PSC-05 | Proof checks and, only if justified, bounded numerical validation | Check the algebra, inequalities and own-data controls of PSC-01–04. Numerical evaluation is allowed only after a specific analytically derived inequality, parameter domain, precision/error contract, comparator and stopping rule are frozen. A failed validation does not authorize a scan or adaptive parameter search. No numerical run is required if the analytical conclusion is already decisive. |
| PSC-06 | Internal review and continuation decision | Review the actual analytical results and any permitted checks. Update this register and the governing BW09/HFCE registers without marking unexecuted or gated work complete. Retain, narrow, or stop the selected mechanism according to its proved margin, actual deficit, or failed hypothesis. |

### PSC-01: make the existing asymptotic quantitatively usable

Start from the complete-source law
\[
 e^{tu^2}\Phi(u)=2\pi^2e^{q_t(u)}b(u),\quad
 q_t(u)=tu^2+9u-\pi e^{4u},\quad 0<c\le b\le C,
\]
and the inherited exact saddle identity
\[
 q_t(L+v)-q_t(L)=tv^2-A(e^{4v}-1-4v),\quad
 A=\pi e^{4L},\quad \kappa=16A-2t.
\]
For the first bound, freeze the proof split \(\delta=1/8\). Derive an explicit denominator lower bound for the complete mass, numerator bounds for \(m_1,m_2\), and the far-left and right-tail payments. State the sufficient conditions on \(t,L,\kappa\); an unspecified “large enough” is not this task's endpoint. Changing the split is a recorded alternative proof, not an unreported numerical adjustment.

Use the existing finite error interface
\[
 \varepsilon_0=Zm_1/L,\quad
 \varepsilon_1=(1+Z)m_1/L,\quad
 \varepsilon_2=(2+Z)m_1/L+m_2/L^2.
\]
Distinguish the physical jet \(F+iLF'\) from the rescaled derivative-channel jet \(F+iF'\). Determine the actually justified range of \(Z=Z(t)\), hence of root indices, for each bound. A uniform homotopy to a single cosine lobe, with correctly transferred endpoints and labels, gives its ordinary half-turn. It **cannot force an extra half-turn or later event**. The analytic regime map must make this limitation visible before any contradiction estimate is attempted.

The only proposed contradiction regimes beyond that compatible conclusion are an event-conditioned intermediate-time regime, or a growing-index regime with genuinely additional uniform arithmetic information and proved wall identification. Neither is presently activated by the fixed-index limit.

### PSC-02: continuation and geometric feasibility before a phase budget

Work first with complete **finite** contours. For each selected cap, prove that the born walls remain finite and simple up to it, give the intended endpoint identification, and exclude a boundary collision by information independent of the desired surplus. If a continuation proof is unavailable, record it as an unresolved premise; do not assume the absence of the very extra roots being sought. A zero on the chosen cap requires another justified regular truncation or paid excision, not an undefined winding.

At a simple endpoint with slope \(s\), the inherited estimate uses
\[
 |f''|\le K|s|\quad\text{on a window of width }V,
 \qquad KV<1.
\]
Record how \(K\), \(V\), the root gap and the jet scale \(\beta\) are controlled simultaneously. Capturing almost \(\pi/2\) requires \(V/\beta\) large while the relative-curvature error is small and the two windows remain disjoint. No lower bound on a wall slope or \(|h_2|\) is free. A stipulated floor restricts coverage and leaves its complement unresolved.

The positive scaling \(J_\beta=H+i\beta H_x\) preserves winding but changes localization. Freeze \(\beta>0\), constant on each cap, and keep it throughout the comparison. An \(x\)-dependent choice adds a phase-current term. The shrinking fixed-index theta gap and its interior phase layer must not be assigned the quadratic's endpoint budget.

### PSC-03–04: the arithmetic obligation

The generic heat equation, source positivity and finite local jets pass controls with no later event. A useful estimate must therefore identify quantitative theta input beyond those shared premises and show where the controls fail that input. Preserve the exact event cancellations inside the complete source expression; do not estimate separately two large terms whose signed difference is the target.

The alternatives are estimates of the complete phase current, or a signed bound for
\(H_{xx}(T,a)H(T+R,b)\) with \(b\) independently proved inside the intended cap. Dividing by an unknown small \(h_2\), locating \(b\) by the desired sign, or defining a nonvanishing region by the conclusion is not an admissible shortcut. The local expansion at the center starts with
\(h_2H(T+R,a)=-h_2^2R+O(R^2)\); local quadratic domination points toward the compatible sign.

For a phase split, compare the middle contribution against the **actual endpoint deficit at the same parameter and scale**. A positive middle integral without that comparison is not progress. If the proposed source estimate only proves closeness to an ordinary one-lobe model, record that compatible result and stop the attempted surplus deduction from it.

## 3. Controls, checks and stopping decisions

Use the applicable own-data calculations, not assigned theta errors:

* Quadratic and arbitrary-jet cubic actual-threshold controls: no later event; ordinary cap accounting must survive.
* Positive atomic actual-threshold control: a complete nonzero limiting cap with phase \(-\pi\). Its missing premise is theta's unchanged complete source, not positivity or the heat equation.
* Two-event quartic: detect the additional cap pair with complete initial-event accounting; its first event is not its all-real threshold.
* Multiplicity-four control: refuse the ordinary \(h_2\ne0\) normalization and retain its own initial index.
* The cap-only family \(-\sin(nx)/n\), odd \(n\), has identical endpoint slopes and \(Q\equiv1\) with different cap counts. It screens removal of the phase denominator, but is not an ordinary-born-event family.
* For Euler-factor, weighted-square, finite-prime, reflected and positive-primitive sources, retain the catalogue's supplied source/event/threshold distinctions. Do not invent a finite threshold or global wall system from a local collision witness.

Stop a selected estimate if its premises are passed by a contradictory own-data control, if its claimed gain is only an equivalent target, if the wall/nonvanishing contract is circular, if the required windows cannot fit, or if a proved ordinary-lobe comparison already fixes its phase at \(\pi\). Record the exact information class and unresolved hypotheses; none is a universal impossibility statement about theta estimates.

No generic numerical scan, precision escalation, large-time grid, or growing-index survey is part of this program. A symbolic identity check, exact control replay, or bounded interval verification of a previously derived inequality is legitimate support. It cannot replace its analytical sign, continuation, or uniformity proof.

[progress]: ../research-progress/03_ANALYTICAL_PHASE_SURPLUS_PROGRESS_20261020.md
[brainstorm]: ../brainstorm/01_CAP_AT_INFINITY_20261020.md
[bw09]: ../research-progress/01_EXPANDING_CONTOUR_PROGRESS_20261020.md
[hfce]: ../research-progress/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRESS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
