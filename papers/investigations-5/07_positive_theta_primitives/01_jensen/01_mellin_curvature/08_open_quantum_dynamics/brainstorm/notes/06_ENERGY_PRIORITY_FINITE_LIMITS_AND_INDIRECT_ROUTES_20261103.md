# Energy-first continuation: finite limits and indirect routes

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a19ff8-8565-7b92-9b9a-b18b628f4785`, brainstorm history **0002**.

**Status:** author-priority clarification and explanatory algebra after E06, not execution of B04's conceptual model selection. The author strongly favors investigating energy meaning. B04 should therefore lead with that question, retaining its existing work limit and treating infinite-domain and signed-target questions as named dependencies. No new architecture, theorem for the MC08 infinite generator, numerical task or E07 contract is issued here.

| Next task | Type / recommended model | Priority and expected output |
| --- | --- | --- |
| MC08-B04 | B / Astra: energy meaning, correspondence and observable remain conceptual | Energy-first: specify what the accepted finite joint Hamiltonian's energies/energy responses mean, and what correspondence to the source spectrum or target observable would be useful. Then select finite/infinite requirements and a bounded E07 route if ready. |
| MC08-E07 | E / Sol | Reserved until that conceptual specification is fixed. |

## Finite-first analysis can be sufficient, with a specified limit

The author's intuition is conditionally correct: finite Hamiltonians, states, dynamics and relevant observables can determine an infinite model when a suitable convergence theorem and its hypotheses are established. The assumption that the required limits exist in the required sense contains substantive mathematical work. There is no need to demand a uniform upper bound on all energies of an unbounded limiting Hamiltonian; the needed controls depend on the chosen claim.

Energy eigenvalues alone leave out the eigenstates, couplings and observable matrix elements. Even in two dimensions, set
\[
H_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
H_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Both have spectrum {−1,1}, but for the fixed basis e_0,e_1,
\[
\langle e_1,e^{-itH_z}e_0\rangle=0,\qquad
\langle e_1,e^{-itH_x}e_0\rangle=-i\sin t.
\]
This is direct elementary algebra and shows why a spectrum list does not determine our transition observable. For driven Hamiltonians the relation among eigenspaces at different times also matters.

For comparison, in the autonomous self-adjoint setting, strong resolvent convergence implies strong convergence of the unitary evolution at each fixed time. This is the precise scope of Teschl, second edition, Theorem 6.31 and Corollary 6.33, inspected in [the author's authorized online book](https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), printed pp.179–180. The discussion immediately preceding Theorem 6.31 permits approximating subspaces with projections tending strongly to identity. This is an example of the kind of theorem that makes finite-first reasoning rigorous; it is **not applied here** to MC08's driven Hamiltonian. Time-dependent propagation needs its own time/domain control. Unbounded energy expectations and high responses also need tail/domain control beyond convergence of bounded observables. No infinite-generator result is inferred from this source.

Two distinctions specific to MC08 are already established:

1. N truncates coefficient sites, not the theta energy spectrum. The denominator F(v) and source coefficients remain complete at every finite N. Increasing N does not simply append omitted source energies pi n².
2. For each fixed finite determinant, once N contains all its occupation indices, its amplitude is already represented exactly by the finite transfer. This follows from backward-shift invariant restriction and the unchanged full F; no limiting approximation is needed for that one amplitude. A theorem for arbitrary indices/particle numbers remains a family-wide claim, and joint Hamiltonian compatibility is separate.

Energy eigenvalues converging, propagators converging, and energy expectations converging are distinct claims. If a finite inequality is proved for all cutoffs and its actual scalar quantities converge, its non-strict sign passes to the limit. Strict positivity can be lost. Observing a finite list of examples supplies neither the all-cutoff theorem nor the convergence premise.

## What an indirect route would need to contribute

The signed determinant is an expression of the hard target within this representation. It is reasonable to seek a structural energy principle that makes it a consequence, rather than to attack every determinant separately. Calling that an indirect strategy describes a research preference; it is not a theorem that direct signed analysis cannot work or that one equivalent formulation has a demonstrably greatest difficulty.

An indirect route still needs an exact bridge to the original determinant or zero statement. Ordinary self-adjointness gives real energy eigenvalues, not a sign for a chosen transition amplitude. Ordinary positive thermal weights likewise do not sign a mixed antisymmetric observable; the reviewed MC01 residual and MC08 controls retain that point. A new source-specific inequality, spectral correspondence, or other structural identity could in principle supply the missing information. It must use more than the generic completion admitted by the negative polynomial control. No claim that these are the only possible classes of approach is made.

## Energy-first question to put before B04

The source already has the square energies E_n=pi n². E06's h_tot,N(t) instead generates an explicit driven coefficient-system/environment model; its overall scale also depends on the chosen clock. B04 should determine which finite energy observable and response have a useful mathematical meaning, and whether they can be related to the complete square-spectrum source and the fixed signed observable. An observable or integral correspondence may be appropriate; literal equality of spectra or a unitary identification is not an assumed requirement.

Use the existing [energy primer](01_FOCK_ENERGIES_AND_THETA_TRANSFER_20261102.md), [Hamiltonian motivation](02_HAMILTONIAN_MOTIVATION_AND_DESIGN_CHOICES_20261102.md), and [reviewed source-energy dictionary](../../notes/06_THETA_ENERGY_LEVELS_AND_FERMIONIC_LABELS_20261102.md). B04 first compares the existing stream and accepted fixed bath under its r0 contract. A genuinely different source-energy representation requires an explicit B03 conceptual revision, not a silent change of E06. Infinite-limit work should follow the observable being selected and retain the distinction between source-mode and coefficient-site cutoffs.

Read with [result summaries](../../../../../../../../result-summaries/README.md), particularly [theta/bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid](../../../../../../../../avoid/README.md), particularly [reformulations](../../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [unchecked imports](../../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). This note records a priority and explains necessary distinctions; it adds no signed bound or infinite-model theorem.

**Next: [B] MC08-B04 — Astra**, energy-first under the existing bounded contract. On a model change, read this note with [Handoff08](../../research-progress/handoffs/08_MC08_E06_RETURN_AND_B04_MODEL_CONTINUATION_20261103.md) and [E06 inheritance](../reviews/01_MC08_E06_QUADRATIC_CLOCK_ASSESSMENT_20261103.md). Preserve this chat's unique history 0002 and record actual model/effort; do not infer them from the recommendation. Current readiness belongs only to the [sole MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md).
