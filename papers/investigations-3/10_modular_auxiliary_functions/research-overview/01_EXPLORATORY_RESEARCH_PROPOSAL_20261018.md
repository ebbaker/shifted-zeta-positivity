# 10: Modular auxiliary functions for signed collision forms — exploratory research proposal

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

**Status: outlined; research round not yet begun.**

## Research question and intended advance

Can an explicitly constructed auxiliary function turn the exact modular and
coefficient constraints of the theta source into a lower bound for the
existing signed collision form? This is a construction project: the unknown
is a usable test kernel with a proved physical interpretation, not another
criterion equivalent to the desired zero statement.

The first result sought is one admissible nontrivial functional on a declared
domain, with its sign and infinite tails proved. A precise impossibility
result for a selected auxiliary family could also redirect the project.
Both are more informative than a finite optimization with an unexplained
positive objective or an interpolation formula for the original unknown.

## Established tools and compatibility limits

The [signed correlation bridge][signedbridge] provides the physical bilinear
form. The [nonlocal audit][nonlocal] identifies complete-source Fourier
representations and their boundary obligations. These are the starting
objects, with the original source insertion and physical heat multiplier
retained.

Two external construction tools motivate the proposal. [Radchenko–Viazovska][rv]
give Fourier interpolation for even Schwartz functions using values of a
function and its Fourier transform at \(\sqrt n\).
[Cohn–Kumar–Miller–Radchenko–Viazovska][ckmrv] give radial interpolation in
dimensions 8 and 24 using values and radial derivatives at \(\sqrt{2n}\).
The original [candidate note][candidates] records these primary references.
Neither theorem supplies a theta collision inequality without an additional
construction and transfer argument.

The physical integer-index samples do not automatically provide every
\(\sqrt n\) datum required in the one-dimensional formula. The
[E8 character bridge][e8] contains anisotropy, differential insertions and
signed sectors, so a radial E8 extremal theorem cannot be applied to that
bridge by identifying the ambient dimension. Any reduction to a theorem's
function class must be proved with its normalization and sign intact.

Finite-source-cutoff test functions can be Schwartz while the separately
integrated dual modes diverge in the positive-time limit. This project must
prove admissibility for the complete paired expression and justify the
cutoff limit used. Schwartz membership at each finite cutoff is not a
uniform convergence theorem.

## Opening research round

1. **Fix the functional to be bounded.** Write the exact double-source
   formula for one \(\mathcal L_j\), or one previously established signed
   observation with a proved transfer to it. Specify its domain in time and
   frequency, the source cutoff if any, and its normalization.
2. **Choose one small auxiliary family.** Declare its basis, permitted
   coefficients, modular transformation law, growth conditions, and the
   identities that make any added term vanish on the complete theta source.
   Do not assume such a family exists with useful sign. Constructing a
   nonzero admissible example is the first technical problem.
3. **Separate construction from sign.** Prove the identity relating the
   auxiliary functional to the physical form, including boundary terms.
   Then seek a sign or lower bound for the complete kernel. Pointwise kernel
   positivity is one possible sufficient condition, not a requirement to
   discard a useful integrated signed inequality.
4. **Close the complement.** State and prove what happens off the sampled
   domain, beyond all cutoffs, and at any modular cusp or singular point.
   If finite optimization suggests coefficients, replace its sign check by
   analytic inequalities or a rigorously certified bounded calculation plus
   analytic tails.

The proposed output is a reusable auxiliary-function specification and its
complete proof obligations, together with one construction or a scoped
obstruction. This setup has not selected coefficients, solved an optimization
problem, or proved that an admissible family exists.

## Two possible construction routes

The direct route works in the original one-dimensional source variables.
Use exact modular or dilation identities to add complete expressions that
vanish for theta, then seek a better lower bound for their sum with the
original bilinear form. The identity and any lower interval must hold for
the actual positive-time transform. The coefficients of the added terms
must be chosen independently of the sign one is trying to prove.

The interpolation route attempts to express the complete physical functional
through an admissible interpolation basis. It first has to account for all
required samples, differential data and signed sectors. If it only
reconstructs \(\mathcal L_j\) from equally uncontrolled quantities, it has
not yet supplied a new estimate. A useful reduction would leave a smaller,
independently controllable signed quantity and price the remainder.

Begin with whichever route admits an exact low-complexity candidate. There
is no requirement to launch both, or to use dimensions 8 or 24. The modular
origin of an auxiliary function matters through the identities it satisfies
and the bound they make possible.

## Control screen and circularity checks

The [control summary][s12] and [Reply 18][reply18] distinguish the premises:

| Information used by the functional | Test and missing arithmetic information |
| --- | --- |
| A Fourier–Gram positive form or interpolation identity | Generic colliding sources can share these structures; neither gives the required signed collision bound |
| Square support and positive weights | Weighted-square controls fail complete theta coefficients and full reflection |
| Reflection and rapid decay | Reflected smooth controls lack the normalized integer-square expansion |
| Finitely many prime relations without a full source or level restriction | Euler-factor modifications at other primes can escape detection |
| A transfer to a Weil-form positive factorization | Retain the smooth-density and two-channel tests in [summary 04][s04] for the particular claimed transfer |

The auxiliary form must identify which of these distinctions it actually
uses. A null identity true for every source cannot by itself distinguish
theta. An identity unique to theta may be informative, but uniqueness does
not establish its proposed sign consequence. Do not hide the target in a
coefficient defined from \(\mathcal L_j/E\), a prescribed zero set, or the
unknown sign of a reconstructed sample.

## Success, useful failure and dependencies

A positive result should state the family, admissibility, parameter range,
inequality and all error terms. A bound valid away from degeneracy remains
a restricted result until its constants are controlled near a collision.
An estimate that excludes one explicitly defined event class is valuable
with that scope; the shared overview classifies the all-event target.

A negative result must prove infeasibility for the actual analytic family
and constraints stated. Failure of a sampled numerical search, an arbitrary
degree cutoff, or a radial surrogate is not an obstruction to every modular
auxiliary function. Preserve a failed candidate when it pinpoints a real
sign or tail obstruction and state exactly what would have to change.

[08][p08] may supply a weighted space in which the candidate is admissible.
[09][p09] supplies complete arithmetic blocks that might generate null terms.
[11][p11] can identify the exterior data a useful auxiliary function must
control. [12][p12] is a separate fixed-character setting with an explicit
product, requiring its own admissibility argument. None of these transfers
is assumed at setup.

The specialist brief should specify the exact physical form, one proposed
auxiliary family, its modular constraints, the desired sign and the nearest
colliding control. Fourier interpolation, modular forms and extremal
function theory are the likely areas. Assess a coherent construction round
before expanding the search; a failed finite trial alone should neither
close the project nor trigger an unbounded computation.

## Shared scope and research practice

This is an exploratory proposal, not a new theorem, completed experiment or
reviewed research result. The [shared overview][overview] states the common
collision target and classifies its all-event strength. Begin with the
[result summaries][summaries] and [patterns to avoid][avoid]; in particular,
use [criterion classification][a01], [premise-based control screening][a02],
[scoped negative results][a07] and [preservation of paired cancellations][a12].

Save incremental derivations in notes, computations and small records in
numerics, and separate assessments in reviews. Review a coherent research
round, which may contain several notes. Record the actual model, effort,
sources and status in subsequent work. Source links below point to canonical
records; existing results retain the review scope stated in those records.

[Project home](../README.md) · [Proposal index](README.md) · [Source guide](../source-documents/README.md).

[signedbridge]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[nonlocal]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md
[rv]: https://arxiv.org/html/1701.00265v2
[ckmrv]: https://annals.math.princeton.edu/2022/196-3/p03
[candidates]: ../../brainstorm/notes/03_NEW_FIXED_FUNCTION_PROJECTS_CODEX_20261018.md
[e8]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[reply18]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md
[s04]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[p08]: ../../08_modular_oscillator_estimates/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p09]: ../../09_coupled_arithmetic_dilations/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p11]: ../../11_arithmetic_collision_rigidity/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p12]: ../../12_fixed_beta_eta_kernel/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[overview]: ../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
