# Continuation of the radial deformation and zero dynamics program

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**, thread `01a18012-c543-7320-ab04-91728654f3ba`.

**Start here.** Edward Baker requested that the deformations be understood well before deciding how to use them against theta forcing. The new [RDZ overview][overview], [research proposal][proposal] and [progress register][progress] supersede both the RTC and RLC programs for current work. Their mathematical results remain valid at their stated scopes. In particular, Note15's flux-first task and Note17's immediate forcing-estimate suggestion no longer govern the next session.

## Read first

1. Repository AGENTS.md, [the chat-history workflow][chatworkflow], [result summaries][results] and [patterns to avoid][avoid]. The specific [collision controls][controls], [local collision geometry][geometry] and [scoped-conclusion rule][scope] are relevant.
2. The new overview, proposal and progress register. These distinguish structural study from a later theta application.
3. The [base-folder manuscript][manuscript], especially Sections 3-8. Its [build instructions][buildinstructions] identify the shared PDF output; [Review11][review] states verification scope.
4. [Note17][n17] for the full deformation construction and [Note18][n18] for physical versus interior zero dynamics. Use [Note01][n01] for normalization and selected tails.
5. Consult earlier flux, Gaussian deformation, multiplier and lattice results only when a specific question needs them. Before a positive-Lambda application, read the existing [threshold reduction][threshold] and its original inputs.

## What is established

With x=log r, lambda=a^2/4>0, g_t=4 exp(t x^2/4) Phi(x/2), and the selected Y satisfying Y_xx+lambda Y=g_t, let

\[
w=\kappa\tanh(\kappa x),\quad c=\lambda+\kappa^2,
\quad U=(\partial_x-w)Y,\quad h=(\partial_x-w)g_t.
\]

The family obeys

\[
U_{xx}+(\lambda+2w_x)U=h,\qquad
U(t,0;\lambda)=B=-8H(t,2\sqrt\lambda),
\]
\[
Y=\frac{g_t-(\partial_x+w)U}{c},\qquad
\partial_\kappa U=-(\partial_\kappa w)Y,
\qquad \partial_t h=\frac{x^2}{4}h+\frac{x}{2}g_t.
\]

All physical positive-frequency multiplicities are preserved at every finite kappa. The invariant integral has complete boundary accounting. The ordinary energy identity is transported with its forcing and two lower boundary terms; its parameter derivatives provide no additional scalar event condition. This does not decide other geometric or analytic uses of the family.

Physical zeros are spectral zeros of B. Interior zeros are spatial zeros of U. At a simple interior zero,

\[
\frac{dx}{d\kappa}
=\frac{(\partial_\kappa w)Y}{g_t-cY},
\]

with nonzero denominator U_x. At kappa=0, use mu=kappa^2 to avoid mistaking the vanishing first kappa derivative for a constant family; partial_mu w at zero is x on compact x sets. Multiple interior nodes, spatial boundary crossings and all-radius limits have not been classified.

The Gaussian-polynomial control retains a double physical boundary zero but has U<0 throughout x>0. Absence of interior nodes is therefore not the missing physical exclusion by itself. The transformed equation is forced, and its source need not be positive or retain the original Kelvin parity.

## First bounded task

Study interior nodal events in this existing family before choosing a theta-forcing estimate.

- Fix symbolic compact parameter and spatial domains and an explicit smooth-source class. Keep the complete selected tails when using a finite spatial interval.
- Derive the local jets needed at U=U_x=0, using the exact inverse and time/deformation laws. Treat mu near zero and kappa away from zero consistently.
- Prove a classification or orientation for a stated nondegenerate event class, or identify exactly why its sign is not determined. A generic double-node model does not cover higher multiplicity automatically.
- Include x=0 and outer spatial boundary crossings in any count law. Keep U_lambda(0)=0 distinct from U_x=0.
- Check the exact colliding control and explain what any auxiliary invariant says about the unchanged physical first jet. A scoped failed correspondence is a valid structural return.
- Save the derivation in notes/, its assessment in reviews/, and only then select any useful supporting computation. Update the RDZ register, not the old RTC/RLC task counts.

The existing simple-node velocity and conserved integral are starting identities. A complete return must answer a new structural question. It need not yet prove a theta-specific separation. No broad numerical scan, large-kappa terminal limit, new lattice, or repeated scalar energy identity is the default continuation.

## Manuscript and records

The single active manuscript source is `radial_deformations_and_zero_dynamics.tex` in this investigation's base folder. Edit it in place when a result is ready for inclusion. Keep generated PDFs under the repository-root output/pdf/radial-theta-collision-geometry/ folder, following [LARGE_FILES.md][largefiles]. Retain the author/drafted-for field and LLM acknowledgment. Save detailed work in notes and reviews; DRAFT_HISTORY.md remains concise and no snapshot folders are created.

This chat has one canonical registration: **chat0006**, thread `01a18012-c543-7320-ab04-91728654f3ba`, in this investigation's [registry][history]. A new chat must use its own actual id and title, not reuse chat0006. Refresh an existing registration at the beginning of a reply. At the end, refresh completed public text and use the documented bounded exact-turn follow-up as the last tool action, then send the actual final reply. The future reply must not be written into the archive in advance. Native completion-hook activation has not been verified here.

[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[proposal]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[buildinstructions]: ../MANUSCRIPT_BUILD.md
[review]: ../reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md
[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n17]: 17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[n18]: 18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[largefiles]: ../../../../LARGE_FILES.md
[chatworkflow]: ../../../../tools/CHAT_HISTORY.md
[history]: ../chat-histories/index.json
