# Exact infinite tensor products and scale recursion

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations. **Broad scientific overview;
no research execution.** The subsequent 13 November branch-planning request
is implemented in the [research plan](../research-plan/01_INFINITE_PRODUCTS_RESEARCH_PLAN_20261113.md)
and [sole ITP register](../research-progress/01_INFINITE_PRODUCTS_RESEARCH_PROGRESS_20261113.md).
The architecture and first quantitative question remain for ITP-B01;
creating the plan does not resolve or activate that task.

## Scientific question

Can the complete Newman wavefunction be assembled by an exact infinite
network whose factors approach identity, with a useful rule connecting
successive scales or heights? The branch explores both the convergence
of such a construction and the structure of its factors. Exactness of a
limiting object is compatible with finite truncation errors; a useful
recursive law must describe more than an arbitrary list of exact cores.

Within the [broader program](../../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md),
this branch owns exact scale products, their topology of convergence and
full-source assembly. Finite QTT approximation bounds belong to branch
01. Exact products could later inform those bounds without making the
two questions identical.

## Complete source and inherited products

Use the [unchanged GNP source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):
\(W_\lambda=e^{\lambda u^2}\Phi\),
\(H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}du\),
\(H_0(z)=\xi(1/2-iz/2)/8\). Initially
\(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\), and \(z=x+iy\).
The height parameter and the refinement index are separate.

On \([a,a+\ell]\), let
\(u=a+\ell\sum_{k\ge1}2^{-k}b_k\), with bit projectors \(n_k\).
[Brainstorm 02 §5](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
gives the exact height-phase product

\[
 e^{ixu}=e^{ixa}\prod_{k\ge1}e^{ix\ell2^{-k}n_k},\qquad
 \|e^{ix\ell2^{-k}n_k}-I\|\le |x|\ell2^{-k}.
\]

For a strictly positive \(C^1\) amplitude \(f\) on that interval, let
\(f_k\) be its level-\(k\) dyadic cell average and \(f_0\) its overall
average. The source refinement product is

\[
 f=f_0\prod_{k\ge1}R_k,\qquad R_k=f_k/f_{k-1},\qquad
 \|R_k-I\|\le\frac{\ell\|f'\|_\infty}{\min f}\,2^{1-k}.
\]

The finite products telescope and converge uniformly on the compact
interval. Every gate is a finite tensor network acting on a growing
prefix of bits. Applying this construction to \(W_{1/2-\tau}\) retains
the exact imaginary-time orbit. It does not establish uniform exact bond
dimension or a simple local recursion for the gates.

The complete real line is recovered through a countable partition into
compact intervals and an absolutely convergent sum of their readouts.
The full theta tails are retained. The compact lower floor \(\min f\)
need not be uniform over intervals, so the construction does not assert
one global operator-norm product with uniform constants.

## What remains open

The main structural question is whether these growing-support gates can
be replaced or organized by a manageable recursive rule. Alternative
scale decompositions, transformations that remove a specified leading
oscillation, and different transfer topologies remain possible. The
architecture is deliberately not frozen by this overview.

The factors above approach identity as scale becomes finer at fixed
height. Their tail bound \(|x|\ell2^{-L}\) shows why growing height
requires separate analysis. Uniformity on bounded complex-height sets
does not provide uniformity on the entire height axis. A proposed
height-recursion product must state its indexing, convergence norm,
domain and treatment of the full-line tail.

Possible useful outcomes include an exact core recursion, a controlled
limiting contraction, or a transfer estimate that preserves a signed
observation. A product whose factors merely tend to identity need not
converge, and an invertible operator product can still have a vanishing
boundary matrix element. Positivity or invertibility of internal factors
therefore does not settle the sign or zeros of the Fourier readout.

The first brainstorm's QTT formulas and the previously inspected quantics
references provide related finite-scale context, recorded in the
[branch reference guide](../references/README.md). The exact dyadic
ratio construction above is inherited from the local note; no published
height-uniform theta rank theorem is claimed for it.

## Evidence, controls and limits

The inherited source is an open conceptual brainstorm with exact
representation identities and a
[same-assistant analytical check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md).
No uniform all-height estimate, computational advantage or signed Green
bound has been obtained. Setup does not add a new derivation or experiment.

The smooth reflected and positive-primitive colliding controls also admit
local positive-source refinement products. They fail the canonical
integer-square theta arithmetic or unchanged complete source, not the
existence of a convergent local product. Atomic controls separately show
that exact tensor representations and regular evolution need not exclude
collisions; their lack of a positive \(C^1\) density is kept explicit.
The source note §8 supplies the full analytical premise screen.

Read the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[control premises 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Any stronger transfer inequality needs its own control comparison. The
limitations of these compact dyadic bounds are not a general exclusion
of other exact networks.

## Neighboring questions and later planning

[Branch 02](../../02_jacobi_chain_height_flow/README.md) organizes the
wavefunction by polynomial degree and continuous height; branch 04
organizes it by source resolution. [Branch 03](../../03_volterra_coefficient_dynamics/README.md)
studies the arithmetic information in moving polynomial coefficients.
[Branch 01](../../01_qtt_newman_flow/README.md) may later compare finite
approximations suggested by this exact construction.

The [shared continuation note](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
provides the ITP-B01 prompt for the conceptual choice of the first question.
The branch plan and sole register now own ITP-B01/E01/E02. E01 and E02
remain reserved; no execution packet, numerical run or theorem is supplied
by planning setup.
