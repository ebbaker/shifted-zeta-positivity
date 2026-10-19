# S05 Covariant theta jets and modular parity

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Exact normalized identities available. The opening execution below records
a bounded source-enclosure improvement; spectral usefulness remains unpaid.

## Question and origin

Can the normalized covariant-jet basis from the manifold work simplify
complete-source differentiation, error estimates, or certified evaluation
enough to improve the symmetry program? This is an additional direction
from the [Hodge and modular discussion][review]. The basis makes modular
reflection diagonal and removes variable coefficients from the source
derivative recurrence. It supports [S01][modular], [S02][cutoff], and the
transverse identities of [S06][geometry]. The [program guide][guide] fixes
the common scope and quantitative gates.

## Exact available basis

Use the period-one theta section and the vertical Chern derivative
\(\mathcal D\) in [Investigation 22's connection note][connection]. For
\(q=e^{4u}\), let
\[
 J_k(q)=(\mathcal D^k\vartheta)(0,iq),\qquad
 T_k(u)=\pi^{-k/2}q^{k/2+1/4}J_k(q).
\]
The [complete signed bridge][bridge] and [Note 07][note] give
\[
 \partial_uT_k=T_{k+2}-k(k-1)T_{k-2},\qquad
 T_{2m}(-u)=(-1)^mT_{2m}(u).
\]
Odd zero-section jets vanish. The complete source combinations are
\[
 16\Phi=T_4-3T_0,\quad
 16\Phi'=T_6-15T_2,\quad
 16\Phi''=T_8-45T_4+30T_0.
\]
These derivatives are in the source variable u. The covariant lower-jet
terms are included. The first equation is an infinite ladder, not a finite
closed system for the physical field.

There are two essential cancellations. First, normalizing J_k cancels the
diagonal coefficient of its recurrence. Second, the growing zero lattice
mode \((2m-1)!!e^u\) of T_(2m) cancels only in the complete source
combinations. The separate positive-time transforms of these pieces do
not converge. Multiplying by physical heat adds the term 2tu T_k in the
source derivative identity; it is not Jacobi heat evolution.

## Read in this order

1. [Note 07][note], its normalized-basis derivation and zero-mode warning.
2. [Connection and fourth-jet source][connection], [metric freedom and
   transverse commutators][metric], and [complete signed bridge][bridge].
3. [Review 14][review] and [its exact/checker record][checks]. These establish
   the current algebraic scope, not a practical advantage.
4. [Current theta source][source] and the [existing evaluator guide][numerics]
   for the baseline representation being compared.

## Bounded first task

Choose one concrete use: a simpler complete-source jet evaluator, a more
stable interval enclosure of source derivatives, or a smaller signed
remainder in an already specified pairing. Identify the old operation or
bound being replaced. Use the identities above directly rather than making
their rediscovery the task.

For an evaluator comparison, implement only the combined source expressions,
or combine their polynomials mode by mode before evaluation. Include the
whole source tail and verify that interval cancellation does not cost more
precision than the original formula. Compare value and all required jets
at the same input domain, rounding convention, and accuracy. Explain any
change in operation count separately from an observed runtime or enclosure
improvement. If estimating an integral, justify convergence before splitting
or exchanging a sum and integral.

For an analytic comparison, apply the basis to a specified complete signed
expression from S01 or S06, and expose the term whose bound becomes easier.
Preserve lower-jet commutators and the physical test covector. A constant
recurrence matrix alone is not that estimate.

## Controls and decision rule

The local ladder also holds for weighted square-series modes; it alone
does not reject the weighted collision controls. The normalized modular
inversion law uses the full theta arithmetic data. Reflected smooth
controls can retain source parity without having this theta jet expansion.
State which part of the argument uses which premise, using the
[program control map][guide].

Pass with a verified simplification useful to another direction and a
declared quantitative comparison: tighter complete errors, fewer required
operations with correctness preserved, measured matched speedup, or an
effective bound. Label a purely algebraic simplification as such. Stop if
separate divergent transforms, a dropped correction term, or an assumed
finite closure create the apparent gain. Do not infer physical positivity
from the parity signs.

## Outputs and handoff

Create `notes/`, `numerics/`, and `reviews/` here when executing. Record the
chosen complete combinations, required derivative orders, tail/rounding
costs, original comparison, source hashes, controls, and actual model/effort.
Supply a checked algebra/evaluation component to S01, S02, or S06. The
existing [checker][checker] is a reusable algebra regression check, not an
RH experiment. Follow the [program guide][guide] for histories and storage.

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[note]: ../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[review]: ../../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[checks]: ../../numerics/HODGE_MODULAR_ROTATION_REVIEW_CHECKS_20261018.json
[checker]: ../../numerics/check_hodge_modular_rotation.py
[connection]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md
[metric]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[bridge]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[source]: ../../manuscript/positive_arithmetic_packets/sections/01_theta.tex
[numerics]: ../../numerics/README.md
[modular]: ../01_modular_self_duality/README.md
[cutoff]: ../02_cutoff_reflection/README.md
[geometry]: ../06_hodge_and_transverse_geometry/README.md


## Opening execution, 18 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol
(Codex), actual reasoning effort ultra**. The [complete-source note](notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md)
and [192/256-bit records](numerics/README.md) implement cancellation-safe
source jets with complete tails and a modular fixed-point Taylor enclosure.
On each of [0,1/64], [0,1/256], [0,1/1024], the source and its first two
source derivatives have strictly narrower enclosures than the existing
expanded evaluator. At the smallest cell the radius factors exceed
894.47, 7.29, 2394.90; the gain persists against fused Horner evaluation.

The normalized basis organizes existing algebra. The principal gain is
complete-source Taylor evaluation with known parity. Fused Horner alone
widens the second derivative on 34 of 64 shifted-line cells. No physical
spectral jet error, runtime gain, new exclusion region, or global bound is
claimed. The [internal review](reviews/01_COMPLETE_SOURCE_ENCLOSURE_INTERNAL_REVIEW_20261018.md)
is by the same model. Next choose a named local-source consumer or pay a
cancellation-preserving spectral transfer; do not expand the source scan.
