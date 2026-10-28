# Continuation toward a natural auxiliary evolution

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Chat0013, Review theta collision strategy.

The next chat should develop a natural evolution in the auxiliary
parameter \(s\), using the exponential transform in the
[Book manuscript](../book/main.tex) as a working example. **The specific
kernel is not finalized and belongs in the next brainstorm.** The intended
purpose is to make a hypothetical collision manifest in spatial geometry
strongly enough to
support a contradiction. What “isolate a collision” should mean remains
an open conceptual question, not a chosen theorem or mechanism.

Continue in **brainstorm/** until the idea is sufficiently precise to
rewrite the research overview and progress register around the new
program. This author-requested continuation replaces the old B02
estimate as the default question for the next chat; it does not discard
the results or change the recorded status of that earlier program.

| Next task | Type | Recommended model | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **Default: kernel, auxiliary evolution and collision-isolation design** | **B — brainstorm** | **Astra:** the kernel, equation, geometric diagnostic and contradiction mechanism remain open | Ready from the Book setup and this note | A coherent proposed mechanism, or a precise remaining design question, sufficient to decide whether a new program can be written |
| Rewrite the research overview and progress register | E — execution, once the conceptual choices are settled | Sol: organize accepted definitions, claims, dependencies and bounded tasks | Depends on the design above; unresolved choices remain B work | A coordinated new program with one live progress register and a crosswalk to earlier work |

These are recommendations under the [model workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md),
not a dispatch or a second live task ledger. Edward Baker chooses the
actual model and effort.

## Read first

Start with [Book Sections 1, 4 and 6](../book/main.tex),
[Brainstorm06](06_BOOK_TRANSFORM_SETUP_20261028.md), and its
[assessment](../reviews/20_BOOK_TRANSFORM_SETUP_ASSESSMENT_20261028.md).
[Brainstorm04](04_CURRENT_STRATEGY_AND_ROADBLOCKS_20261028.md) summarizes
the earlier strategy and unresolved estimates.
[Brainstorm05](05_FIELD_VARIABLES_AND_NONRADIAL_FLOWS_20261028.md)
explains symmetry inheritance, but its old spectral-dependent density
and flux notation have been superseded for this new setup.

Consult the [result index](../../../../result-summaries/README.md) and
[pattern index](../../../../avoid/README.md), especially
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
[restating the target](../../../../avoid/01_restating_the_target.md),
[shared control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Starting principles and the working transform

Keep the density independent of the observation variable \(z\), the
kernel independent of the evolution parameter \(s\), and the complete
function \(H(t,z)\) recoverable at every admitted \(s\). Fixing a kernel
throughout an evolution does not require finalizing its form before the
next design discussion. Compare candidate kernels by their geometric
meaning, information content, inverse on a specified class, and the
evolutions their invariant admits.

For the current working example, \(X=(x,y,w)\), \(r=|X|\), and \(\ell(X)=\tfrac12\log r\),
\[
H(t,z)=\int_{\mathbb R^3}\rho_s(t;X)e^{iz\ell(X)}\,dX
\quad\text{for every }z\text{ and every admitted }s.
\]
The density has no spectral argument. The kernel, coordinates and
volume measure are fixed in \(s\). Edward Baker preferred the exponential
to the cosine formulation, then clarified that the kernel itself should
remain open to further brainstorming. The original cosine formula
follows from the initial source's evenness. Keep \(j_s=\nabla_X\rho_s\) for the gradient, and define
any conservation flux separately.

The initial density is the smooth radial whole-space realization
\[
\rho_0(t;X)=\rho(t;r)
=\frac{q_t(\ell(X))}{16\pi r^3},\qquad
q_t(u)=e^{tu^2}\Phi(u),\quad u\in\mathbb R.
\]
It extends flatly at the origin. This is the symmetric normalization from
the Book, not the earlier exterior-only density with denominator
\(8\pi r^3\). The initial state is radial; later states need not be.

For this specific exponential logarithmic-radius kernel, at each fixed
\(t\), preserving all observations is equivalent to
\[
\overline{\rho_s}(t;r)=\rho(t;r),\qquad
\rho_s(t;r\omega)=\rho(t;r)A_s(t;r,\omega),\qquad
\int_{\mathbb S^2}A_s\,d\sigma=1,\quad A_0=1,
\]
where \(d\sigma\) is normalized spherical measure. For a differentiable
family, the corresponding necessary tangency condition is
\(\overline{\partial_s\rho_s}=0\). This describes the admissible
directions; it does not supply an evolution law.

The next design should state whether positivity is preserved or signed
densities are needed, and justify the regularity and integrability
required by its kernel. Absolute exponential moments of logarithmic
radius suffice for the current example. In that example, changes may
couple different radii while retaining the mean on every sphere. Do not
interpret the marginal constraint as requiring each individual trajectory
to stay on a sphere.

The cosine kernel alone would retain only the even marginal. Comparing
it or other kernels is within the next brainstorm's scope. For any new
choice, derive the compatible initial density and normalization,
information retained, and conservation constraints afresh. The fixed
spherical-average condition above is a consequence of the present
kernel, not a universal requirement on every proposed transform.

## What collision isolation must accomplish

At a real mark \(p=(T,A)\), the event is
\[
H(T,A)=H_z(T,A)=0.
\]
For the working exponential kernel, the spatial pairings with
\(e^{iA\ell(X)}\) and \(i\ell(X)e^{iA\ell(X)}\) both vanish.
For a different kernel, use \(K(A,X)\) and \(\partial_zK(A,X)\),
justifying differentiation under the integral. These pairings remain unchanged throughout an admissible \(s\)-evolution.
Consequently the evolution cannot move or remove the physical zeros.
Its purpose must be to expose their cancellation through some additional
spatial behavior.

The first substantive task is to define that behavior. Possibilities
such as concentration, loss of regularity, degeneration of a geometric
quantity, or an incompatible limiting configuration are questions to
compare, not already selected mechanisms. Specify the observable,
the spatial region or scale if relevant, and whether the effect occurs
at finite \(s\) or only in a limit. Distinguish a double zero from a simple
zero and from a generic nonzero observation.

A contradiction needs two separately justified parts: the assumed
collision forces the specified behavior, while an independently proved
property of the canonical theta evolution prevents it. A new geometric
description or a conditional singularity alone supplies only the first
part. Locate the missing estimate explicitly instead of burying
noncollision in an assumed regularity bound.

Decide whether one evolution is intended to reveal all possible
collisions, or a family is indexed by a fixed mark \(p\). A marked family
may be written \(\rho_s^p(t;X)\), but for each fixed \(p\) it must still
recover the entire \(H(t,z)\) with the same kernel and no observation
argument inside the density. Keep mark dependence separate from
differentiation in \(z\). State the intended time, height and multiplicity
scope; a local double-event model is not automatically a global
threshold argument.

## The first question about a natural equation

Explain why the law follows from the spatial or transform geometry:
what evolves, what drives it, why its invariant is respected, and what
structure makes the equation useful. Prefer a small, intelligible system
whose terms have a geometric meaning. An arbitrary deformation inside
the transform's null space is admissible, but admissibility alone does
not make it informative about collisions.

There is an immediate symmetry issue to resolve. A rotation-equivariant
evolution with unique solutions, radial initial density, and no additional
asymmetric data retains radiality. For the present exponential
logarithmic-radius kernel, radiality then forces the density to remain
equal to its initial value. A different kernel requires checking whether
its observations still determine the radial density. Thus the current
construction needs a source of angular structure for nontrivial scalar
evolution; a different construction must identify which premise changes. Nonlinearity or
an instability does not by itself create a perturbation from exactly
symmetric data.

An auxiliary field, a geometric marking, or a family of equivalent
orientations may be worth considering, but each is a design choice.
Distinguish a coordinate convention from a physical preferred direction,
and identify which conclusions would be independent of that choice.
This observation scopes the stated symmetry class; it does not rule out
other coupled or nonradial constructions.

## Lessons to retain without inheriting the old equation

The earlier flow evolved a different spectral-dependent integrand for
each observation. Its ordinary mass conservation does not establish the
new fixed-kernel invariant for a single spectral-independent density.
Likewise, the shear example in Brainstorm05 is intuition about
nonradial dynamics, not an already admissible flow in the new class.

[Note28](../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md)
provides a finite collision deadline for its own feedback law, but its
regularity assertion restates noncollision and its exact colliding
control also breaks down.
[Note29](../notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md)
does not supply the missing first-jet margin from carrier dissipation.
[Note31](../notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md)
shows why preparation residuals, commutator forcing and boundary
cancellations cannot be dropped in its source-relation calculation.
These are comparisons and cautions, not requirements to retain the old
PDE or its variables.

Once a candidate mechanism is precise, classify its proposed conclusion
and test the relevant colliding controls, starting with Note28 Section 8
and then the registered families appropriate to its premises. Record
which premise or quantitative estimate each applicable control fails.
A geometric mechanism can legitimately reproduce a control's collision;
the eventual contradiction requires a further canonical input. There is
no new candidate or control test asserted by this continuation note.

## The next chat's completion target

Develop one well-motivated candidate, or a small comparison that resolves
a specific design choice. The intended return should contain:

1. A justified working kernel and a precise meaning of collision
   isolation, with a reason the proposed geometry could help produce a
   contradiction.
2. An explicit proposed evolution, state variables and compatible initial
   density, with a derivation of the invariant and an account of the
   symmetry issue.
3. The bridge from a hypothetical collision to its geometric effect, with
   proved identities, conjectural steps and the missing canonical estimate
   distinguished.
4. An initial assessment against the relevant controls and earlier
   failures, plus the next bounded mathematical question.

These are design deliverables, not a demand to prove a collision
exclusion in the next chat. If an essential choice remains unresolved,
save that question and its evidence in brainstorm and continue there.

Once the mechanism and work sequence are coherent, rewrite the
research-overview and research-progress files together. Preserve earlier
results and failed variants, explain the change from the old invariant
and flow, designate one current progress register, and classify future
tasks as B or E before execution. Do not mark an unproved estimate
complete merely because the new program names it. Numerical work should
follow a concrete mathematical question with finite inputs and a clear
decision it can resolve.

## Pasteable continuation prompt

> Continue from brainstorm/07_NATURAL_AUXILIARY_EVOLUTION_CONTINUATION_20261028.md
> in Investigation05. Brainstorm the kernel and a natural auxiliary
> evolution in s together. The exponential logarithmic-radius kernel in
> book/main.tex is a working choice, not a finalized requirement. Retain
> a density independent of z, a kernel independent of s, and recovery of
> every H(t,z) throughout the evolution. Start from the canonical radial
> realization and derive any changed representation carefully.
> Clarify what it would mean to isolate a hypothetical collision through
> spatial geometry and how that could contribute to a contradiction.
> Determine the information and conservation constraints imposed by the
> chosen kernel; the fixed radial marginal belongs to the current kernel,
> not every possible choice. Address the source of nontrivial geometry,
> and distinguish a collision's geometric consequence from
> the independent canonical estimate that would exclude it. Use earlier
> flows and controls as comparisons, without assuming the old feedback
> law must be retained. Keep the work in brainstorm until the idea is
> developed enough to rewrite the research-overview and research-progress
> files around a coherent new program, with B/E tasks and one live ledger.
> Refresh this new chat's own history in the investigation chat-histories
> folder; do not reuse chat0013's identity.

This note is the handoff. It chooses no new auxiliary equation and
changes neither the open Book manuscript nor the formal program files.
