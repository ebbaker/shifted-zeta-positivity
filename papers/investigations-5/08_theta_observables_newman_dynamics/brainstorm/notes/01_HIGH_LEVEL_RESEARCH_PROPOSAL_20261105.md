# High level proposal for theta observables and Newman dynamics

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in this chat's turn metadata. Investigation08 chat0001, thread `01a1ae2a-64b9-7882-8942-9c56f3d136e6`.

**Later author clarification, 5 November 2026:** [Note02](02_DIRAC_CYLINDER_HAMILTONIAN_PRIORITY_20261105.md) selects the full Dirac-cylinder model and its natural Hamiltonian interpretation as the starting priority. It supersedes this proposal's preparation-first ordering and classical-ensemble organizing suggestion. Direct radial spectral representation of Newman flow and a natural auxiliary flow remain open alternatives. The original proposal below is retained as discussion history.

**TND-B00 — conceptual proposal for discussion.** The author requested a high-level research proposal and asked that relevant notes be kept in the brainstorm folder. The recommended emphasis is a physical model that explains the source, its preparation and its Newman deformation, with a focused mathematical question developed alongside it. This is a proposed direction within the existing brainstorm; the formal research plan and progress register remain deferred.

| Next discussion | Type | Recommended model | Readiness | Useful outcome |
| --- | --- | --- | --- | --- |
| TND-B00 — choose the model's first explanatory goal | B — brainstorm | Astra; the physical interpretation and desired mathematical benefit remain open | Ready for author discussion | Agreement on what the first model should explain, with its supplied theta information explicit |

## Starting assessment

The [draft overview][overview] and [continuation][continuation] identify complementary contributions. MC11 explains the angular spectrum, Green response and energy measurements reconstructing the source. Investigation05 explains radial potential geometry and source-defined Newman evolution. Their common scalar source does not yet establish a common physical system: a scan over angular damping is not automatically a radial preparation, and their fields and measures need an explicit comparison.

The accepted MC11 cylinder/source results retain their internal-assessment scope. Its [observable extension][observables], now in [manuscript Sections 3 and 8][manuscript], has proof-author checks with OBS-E01 pending. The [radial companion assessment][radial-review] records same-assistant checking. Discussion can use this dictionary provisionally; a later analytical result must retain those dependencies. MC11's reserved determinant task E05 stays in MC11.

## Proposed research direction

**1. Establish the physical relationship between the two models.** Make a short comparison of the angular response, radial potential, prepared source distribution and measured transform. Identify which maps are already exact and which require a new preparation or coupling. The aim is to locate the missing physical operation, rather than expand the dictionary. A single Hamiltonian need not be assumed at the outset.

**2. Explain how the canonical source is produced.** Use the cylinder's integer-square spectrum and specified energy filter as the concrete starting point. Account for where unit coefficients, complete reflection and the source observation enter. Distinguish a protocol that loads a known theta profile from one that derives that profile from stated geometry and dynamics. Both can be useful, but they answer different questions. The first worthwhile physical result would be an explicit chain from specified inputs to a source distribution and signed readout, with preparation assumptions and absolute normalization visible.

**3. Give Newman deformation an operational meaning.** Compare a controlled family of preparations with an actual evolution of one prepared system. I recommend the former as the initial benchmark: decide what would prepare and measure the family over a specified finite parameter interval, then ask whether an intrinsic or enlarged dynamics supplies additional understanding. Physical time, angular damping and the Newman parameter remain distinct. The inherited [Newman definition][rt] reweights the source by a Gaussian and induces backward heat evolution of its transform; it does not identify the laboratory generator.

The [observable note][observables] already distinguishes the two filter directions: negative Newman increments permit a bounded conditioning filter, while the corresponding positive-increment multiplication is unbounded on the full Hilbert space. This limits that particular filter implementation. It leaves state-specific preparation and other controlled or enlarged models open. Preparation of the starting state remains an obligation in either direction.

**4. Seek one useful mathematical consequence of the observations.** Keep the signed value and derivative of H central. The most concrete lead is the existing expression of the source's logarithmic slope through angular energy moments. Ask whether the complete canonical response makes one of the previously uncontrolled oscillatory correlations accessible. The [moving-state][moving] and [score-jet][scores] notes are the starting point, not work to rediscover. A useful first gain could be a quantitative relation on a declared domain, a demonstrably better diagnostic, or a precise limitation of a proposed mechanism. A new representation alone would count as physical interpretation, not collision exclusion.

These priorities need not form a rigid sequence. The signed-correlation question can develop before a complete physical dynamics is available. Conversely, a successful physical model remains valuable even if it yields no new zero estimate. The [auxiliary-flow summary][auxiliary] gives the essential lesson for a later mathematical claim: explain how the new information constrains the original H, including its signed cancellations.

## A useful choice for the first model

The current collision readouts are

\[
H_\lambda(a)/Z_\lambda=\mathbb E_\lambda[\cos(aX)],
\qquad
\partial_aH_\lambda(a)/Z_\lambda=-\mathbb E_\lambda[X\sin(aX)],
\quad Z_\lambda=H_\lambda(0).
\]

An immediate interpretation of the existing dictionary is that these two expectations depend only on the position distribution. A classical ensemble can represent their signed averages; coherent wavefunction preparation is an additional physical requirement, not a prerequisite for writing or sampling those particular averages. Averaging a signed function retains information that measuring only the squared return amplitude would discard. This observation supplies neither a preparation protocol nor a sampling advantage near cancellations.

I suggest using such an ensemble as a baseline while asking what coherent dynamics would add. It could add a preparation mechanism, an interference experiment or a useful operator relation. The discussion should decide whether the first goal is a complete operational model or a stronger physical explanation of why the canonical source arises. Laboratory engineering can follow once that goal is clear.

## Standards for the mathematical part

This proposal is model development and question selection, not a new RH criterion. Follow the [result index][results] and [patterns index][avoid], especially [Newman reductions][newman], [target classification][a01], [coordinate realizations][a03] and [scoped exclusions][a07]. A later bounded estimate must state its actual domain and gain; a global reformulation must be identified as such.

The existing [control register][controls] already screens the generic preparation and observation premises:

| Control | What remains possible and what differs from the canonical model |
| --- | --- |
| Weighted-square and finite-tail sources | Applicable positive energy/source observations survive; unit coefficients and complete canonical reflection are changed. Their events are not finite all-real Newman thresholds. |
| Euler-factor sources | Positive even states, Gaussian reweighting and signed observations survive; the canonical arithmetic source is changed. |
| Reflected super-Gaussian, smooth-shape and positive-primitive sources; the counter-kernels in the Newman summary | Relevant positive-source Fourier observations still permit collisions; the complete canonical integer-square source is absent. Each family's stated decay and convergence domain must be retained. |
| Atomic and finite-profile controls | Signed characteristic-function observations survive; the smooth wavefunction/domain argument does not apply literally to atoms, and full theta arithmetic is absent. |
| Fixed theta amplitude with varied observation kernels | Even the source can remain exact while the full cosine oscillator and physical Newman equation fail. Preserve the literal observation kernel in any proposed transfer. |

This is a premise comparison using the registered results, not a new numerical control run. No excluding inequality is proposed here. A correct model may also represent colliding controls. A future exclusion estimate must use and quantitatively exploit its distinguishing premise on a domain containing the relevant control event; naming the canonical source alone does not do that. The old residual-sign, linear-flow and pair-damping failures retain only their proved classes.

## Suggested starting point for discussion

I would begin with **what should count as explaining the source**: an operational preparation with declared theta input, or a derivation that reduces the theta information supplied externally. My recommendation is to make the operational chain precise first, while tracking which ingredients deserve a deeper explanation. That gives the dynamics and signed-correlation questions a concrete common object without committing to a new Hamiltonian or numerical campaign.

The current overview remains provisional. This note records a proposal for the author to discuss; it does not settle its open choices or activate execution work.

[overview]: ../../research-overview/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_DRAFT_OVERVIEW_20261105.md
[continuation]: ../../notes/01_BRAINSTORM_CONTINUATION_20261105.md
[observables]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md
[manuscript]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/manuscript/main.tex
[radial-review]: ../../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[moving]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md
[scores]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/2_CONDITIONAL_SCORE_JETS_AND_CERTIFIED_SIGN_CHANGE_20261010.md
[auxiliary]: ../../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md
[rt]: https://arxiv.org/html/1801.05914v5#S1
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[newman]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
