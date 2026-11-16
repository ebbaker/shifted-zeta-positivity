# Open brainstorming continuation for exact dyadic products

15 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in this chat's recorded configurations and are not
inferred.

**Purpose: continue an open-ended mathematical conversation.** Edward finds
the exact representation appealing and wants to understand its construction
more deeply. He will probably explore Volterra first, while keeping this
program open for further discussion. The immediate aim here is conceptual
understanding and exploration; no particular architecture, theorem target
or computational objective is selected.

The [shared deep dive](../../../brainstorm/notes/05_VOLTERRA_INDUCTION_AND_DYADIC_REFINEMENT_20261115.md)
contains the preceding explanation and a two-level mass-splitting example.
Compression and scale-dependent cancellation were possible future questions.
They remain available alongside other questions that arise from understanding
the construction. This note activates no new execution task and leaves the
completed opening round at its recorded status.

## Starting mathematical picture

The source and its Fourier field are
\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du.
\]
At resolution \(L\), a cell \(I_{L,j}\) has width \(h=2^{-L}\) and
exact source mass
\[
 m_{L,j}=\int_{I_{L,j}}W_\lambda(u)\,du.
\]
Each parent mass equals the sum of its two child masses. Preparing
amplitudes \(\sqrt{m_{L,j}}\) gives the refinement rule
\[
 |j\rangle\longmapsto
 \sqrt{\frac{m_{L+1,2j}}{m_{L,j}}}|j0\rangle+
 \sqrt{\frac{m_{L+1,2j+1}}{m_{L,j}}}|j1\rangle.
\]
The conditional fractions depend on the resolved prefix. Following one
branch multiplies those fractions to obtain the final mass, or their
square roots to obtain its amplitude.

With \(f_L=P_hW_\lambda\), the cell-average density, the source product is
\[
 f_L=f_0\prod_{k=1}^L R_k,\qquad R_k=f_k/f_{k-1}.
\]
The corresponding states converge to \(\sqrt{W_\lambda}\). A countable
integer label selects a unit interval; the binary digits locate a point
within it. The observation has the separate product
\[
 e^{izu}=e^{iza}\prod_{k\ge1}e^{iz2^{-k}b_k}.
\]
Its individual bit factors act on a generally correlated source state.

The [manuscript](../../manuscript/main.tex) develops these statements at
eq:mass-isometry, eq:telescopes, eq:state-limit and eq:phase-product.
Exact integration of the unresolved cell phase gives
\[
 A_L(\lambda,z)=\frac12\operatorname{sinc}(zh/2)
       \sum_jm_{L,j}e^{izc_{L,j}},
\]
at eq:sinc and eq:readout. This is exact for the cell-average source and
converges to the original field. A finite resolution still has infinitely
many cells on the full line until a spatial tail is also truncated.

The [exact-cell transfer](../../notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
is **proved in-note** and
[accepted without correction within scope](../../reviews/01_ITP_E02_EXACT_CELL_PHASE_ASSESSMENT_20261114.md)
in an internal same-worker assessment. Its absolute error statement and
scoped center-phase comparison are starting evidence. Efficient acquisition,
compression and relative or signed-field consequences remain open.

## Questions to keep available

These strands are invitations to explore, not a prescribed agenda.

- **Follow a single split carefully.** What are mass, probability,
  amplitude and density at each level? Why do the square roots preserve
  the norm? Work through a small example, then locate its quantities in
  the complete-source formulas. How does dependence on the earlier bits
  distinguish the state from independent binary choices?

- **Understand the common space and the limit.** Why does appending the
  uniform reference bit leave an old step function unchanged, while the
  source-dependent split updates it? What does the telescoping product
  say before taking a limit? Explore the distinction between convergence
  on a fixed interval and weighted state convergence on the full line.

- **Trace the Fourier observation.** Where do correlations enter the
  expectation of the bit phases? Derive the sinc factor from the phase
  integral over one cell. What information is preserved by uniform
  filling of that cell, and what is restored at the next refinement?
  Follow the effect of increasing observation height through an example.

- **Ask what refinement could reveal.** Could relations between adjacent
  cells, sibling splits or groups of levels carry information useful to
  the Fourier field? What could an induction in resolution keep track of?
  Consider both source quantities and oscillatory observations without
  assuming that positive masses determine the sign of their sum.

- **Explore what is particular to theta.** Which features of the complete
  source become visible in the conditional fractions or refinement
  factors? How might symmetry, reflection, smoothness or arithmetic
  information be expressed across the tree? Which features belong to
  generic positive densities, and which genuinely distinguish the source?

- **Separate the different parameters.** Resolution \(L\), height \(x\)
  and Newman time \(\lambda\) have different roles. At finite resolution,
  the time derivative of a cell mass uses an additional in-cell
  \(u^2\)-moment. What further information would be natural to retain if
  time evolution becomes the focus? The mass-refinement rule alone does
  not answer that question.

- **Consider what exactness makes possible.** It may support structural
  analysis, comparison of representations, or eventually a practical
  finite approximation. Explore these possibilities as understanding
  develops. Compression is one possible direction; another architecture
  or analytical viewpoint can also be worth discussing.

A small tree, a worked cell integral or a comparison with a familiar
positive density may be the most useful next step. The conversation can
stay with the construction for as long as needed before choosing a more
specific research question.

## Context to retain as the ideas develop

Read the [result index](../../../../../result-summaries/README.md) and
[cluster 18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
with the [avoid index](../../../../../avoid/README.md).
[Pattern 03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
distinguishes exact re-representation from a new estimate or mechanism;
[pattern 01](../../../../../avoid/01_restating_the_target.md) supplies the
classification when a concrete proposed criterion or bound emerges.

The [integration screen](../../notes/03_ITP_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
and [collision catalog](../../../../../result-summaries/12_collision_controls_and_screening.md)
retain the relevant premise distinctions. Conditional mass refinement is
available for broad classes of positive densities, including colliding
weighted-square sources; complete canonical coefficients and full
reflection are absent from those controls. Atomic controls lack the
positive differentiable full-line density assumed by this construction's
source estimates. A different conditional-mass construction for a measure
would need its own hypotheses.

The paper's fixed center-phase aliasing obstruction concerns that fixed
uniform-cell sampling rule in an all-height error norm. It does not exclude
exact cell integration, changing resolutions or all dyadic architectures.
Use [pattern 07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
to preserve this scope. If a specific theta mechanism is proposed, apply
[pattern 02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and identify precisely which additional premise the relevant controls fail.

## Opening a later conversation

Resume with Edward's interest in exactness and his wish to understand the
construction. Work through one branch of the mass tree, the square-root
state, the limiting product and its Fourier observation at a comfortable
pace. Let the resulting questions guide the discussion. Keep alternative
structures and uses available, and distinguish an illuminating example
from a statement proved for the complete theta source.

The [Volterra continuation](../../../03_volterra_coefficient_dynamics/brainstorm/notes/02_VCD_OPEN_BRAINSTORM_CONTINUATION_20261115.md)
records the likely first program. Comparing degree refinement with spatial
refinement may eventually be useful, while each conversation can develop
on its own. The shared discussion keeps its single
[parent history home](../../../chat-histories/README.md); this note does
not create or duplicate a chat registration.

