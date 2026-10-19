# S02 Reflection within the Riemann Siegel cutoff interval

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Published leading profile and proposed signed comparison; no new jet bound.

## Opening execution: complete-error comparison

18 October 2026. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. The [opening note](notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md)
implements a holomorphic signed correction with paid continuation and
cutoff costs. The complete disk-error budget falls from approximately
0.887748 to 0.226299 on the height-1000 box, and from 2.897965 to 0.431777
on the separate `[1017,1019]` crossing test, with Cauchy bounds through
order two. [192/256-bit evidence and reproduction](numerics/README.md),
[internal review](reviews/01_CUTOFF_REFLECTION_INTERNAL_REVIEW_20261018.md).

The earlier transport Notes 20 and 22 already derive the multiplier,
nonholomorphy repair, exact jump and analytic matching. This round credits
those results and tests the full analytic continuation on the new bounded
domains. It has not compared against their best correlated-error method.
No signed lower bound, new exclusion region or speed gain is claimed.
The next bounded task is that comparison or a paid S03 consumer.

## Matched continuation comparison, 19 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual reasoning effort ultra**. [Matched Note 02](notes/02_MATCHED_FROZEN_AND_ANALYTIC_CORRECTIONS_20261019.md)
completes S02-T1 against the strongest applicable frozen exponential using
the same published residual and earlier analytic ninth-mode matching.
The frozen allowances are <0.226298331 on B and <0.229588317 on C;
full analytic allowances with the same edge payment are <0.226299246 and
<0.229588635. The C improvement over the opening 0.431777199 restores old
matching work and is shared by both methods. Full analytic continuation
does not beat frozen under this first-derivative continuation ledger.

[Separate internal review](reviews/02_MATCHED_CORRECTION_INTERNAL_REVIEW_20261019.md),
192/256-bit comparisons and fresh source-specific controls pass. Select
frozen per-disk physical jets for S02-T2, holding the center fixed during
spatial differentiation. Keep the full analytic expression for a named
consumer requiring a single analytic residual across the box. No evaluated
whole-cell field, margin, cost gain or new coverage is claimed. Stop this
bounded comparison; [tracker](../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md).
This continuation preserves the chat's [existing registration](../01_modular_self_duality/chat-histories/0002_2026-10-19T04-00-03Z_begin-first-research-track.json).

## Complete evaluated jets, 19 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual reasoning effort ultra**. [Note 03](notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md)
completes S02-T2 on B at 192/256 bits. Both formulas pass the firstjet and
Schur-coupled L0>E/100 tests on all 4096 closed cells; independent frozen
Cauchy boxes pass only 1770 signed cells. The evaluated full formula gives
the stronger paid firstjet radius (>0.9702739184 versus frozen
>0.9686625938), despite frozen's smaller eta. Fresh complete-source data
remain stronger (>1.3473946960). No new coverage or cost advantage.

Keep the coherent full formula for S03. Frozen local jets export and pay
their diagonal derivative defects; they are not a global analytic jet.
[Small records and reproduction](numerics/README.md), [external tables](ARCHIVES.md),
[separate internal review](reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md).
S02-T2 is complete as a known-box certificate and evaluated interface;
C is unactivated and the next analytic task is S03-T1.

## Question and priority

Can the even normalized cutoff correction be combined with nearby retained
arithmetic terms to reduce the complete error? This is the first quantitative
priority in the [program guide][guide] and [original continuation][context].
The baseline currently pays for the correction in absolute value. The
proposed change must improve the full value/derivative calculation after
all costs are included.

## Transformation and known formula

For real spectral height x, use
\[
 a=\sqrt{x/(4\pi)+t/16},\quad N=\lfloor a\rfloor,
 \quad p=1-2(a-N).
\]
On the open interval \(N<a<N+1\), the map
\(a\mapsto2N+1-a\) sends p to minus p. The leading profile is
\[
 C_0(p)=\frac{\exp\{\pi i(p^2/2+3/8)\}
                 -i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)},
 \qquad C_0(-p)=C_0(p),
\]
with removable singularities at \(p=\pm1/2\).

[Polymath, Section 6.2, equation (53) and Proposition 6.3][polymath]
give the explicit nonzero multiplier and normalized value error for
\(0\le\sigma\le1\), \(T\ge100\), \(0<t\le1/2\), with real-axis
\(T=x/2\). Use its full multiplier, including the cutoff sign, amplitude,
phase, and heat factors. The source uses sigma+iT; the local symmetric
representation uses s=(1-iz)/2, so the reflected/conjugate translation must
be written explicitly. Evenness of C0 does not make the complete H even
under this change of height.

## Read in this order

1. [Brainstorm formula and derivative warning][brainstorm].
2. [Current exterior section][outer], especially `eq:rs-normalization`,
   `eq:rs-eta`, and the fixed-cutoff disk proposition.
3. [Published remainder estimate and signed assembly][polymath], including
   Corollary 6.4. Do not transfer a value-only error into a derivative claim.
4. [Earlier collision manuscript][earlier], especially `sc:vector`,
   `sc:packet`, and its fixed-cutoff derivative and edge-cancellation work.
5. [Transport Note 20][transport20] and [Note 22][transport22], which already
   construct a paid holomorphic correction and match its cutoff jump.
6. [S03 rotation defect][rotation] for an optional consumer and
   [S04 scaling][scaling] for the growing-cutoff regime.

## Bounded first task

Start with the guide's comparison box
\([1/100,1/5]\times[999,1001]\). Construct a fixed-cutoff analytic
approximation that retains the signed leading correction and a specified
number of neighboring arithmetic terms. Record the complete symmetric
normalization before numerical evaluation.

Derive a holomorphic residual estimate on the disks used to pay for the
jets. Include approximation errors from both reflected sums, the corrected
remainder, retained-mode evaluation, source or contour tails where used,
and arithmetic rounding. Use that bound or directly proved derivative
bounds to pay for orders zero and one; order two is needed for Laguerre
or rotation-defect use. State explicitly whether the published value
estimate supplies the required complex neighborhood or needs extension.

Add a small bounded neighborhood of a=9 as the transition test. Freeze an
integer cutoff there and express its difference from the natural cutoff
by exact added/removed terms. Do not differentiate N. Treat the removable
points p=plus/minus one half with analytic continuation or a validated
local expansion if encountered, rather than subtracting nearly zero
floating numerator and denominator without an error bound.

Compare baseline and candidate using the same complete normalized jet
error or physical error. Report which part of the total budget changes.
Measure the additional cost of retaining and evaluating the signed term.
The reference box has known coverage; reproducing it is validation, not
a new exclusion region.

## Controls and decision rule

The complete approximation is specific to the unchanged theta data. The
[control replay][controls-record] does not authorize using its tail constants
for altered sources. The proposed acceptance interface must reject a
source-specific enclosure at each applicable control event; a control box
without an event may pass a valid local test.

The adjacent-packet result defeats a positive lower bound by separate
diagonal energies for its specified two-term packets. It leaves combined
signed sums open. Preserve those cross terms when combining the correction
with the arithmetic block.

Pass with a strict certified reduction of the complete paid error, matched
cost savings meeting the chosen gate, or new certified coverage. Stop if
the saving is confined to C0, disappears after derivative/transition costs,
or requires dropping the published multiplier. Record the particular failed
combination; do not infer an obstruction to all cutoff treatments.

## Outputs and handoff

Create `notes/`, `numerics/`, and `reviews/` here for the derivation, bounded
comparison, and assessment. The record must include exact domains, cutoffs,
disk radii, retained neighbors, normalizer, derivative errors, whole-cell
coverage, source/code hashes, actual model/effort, costs, and controls.
Hand the complete signed approximation and paid derivatives to S03.
Follow the [program guide][guide] for history and storage.

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[context]: ../../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[brainstorm]: ../../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[outer]: ../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[polymath]: https://arxiv.org/html/1904.12438v2#S6.SS2
[earlier]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[rotation]: ../03_normalized_jet_rotation/README.md
[scaling]: ../04_time_height_scaling/README.md
[controls-record]: ../../numerics/SYMMETRY_BRAINSTORM_CONTROL_REPLAY_20261018.json

[transport20]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md
[transport22]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
