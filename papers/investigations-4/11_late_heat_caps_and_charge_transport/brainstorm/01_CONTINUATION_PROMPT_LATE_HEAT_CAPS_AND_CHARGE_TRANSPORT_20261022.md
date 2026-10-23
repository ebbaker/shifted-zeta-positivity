# Continuation for late heat caps and charge transport

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from this turn's metadata.

Use this note as the starting instruction for the next research session.
Saving it does not create a chat or start future work. The [overview][overview]
and sole [progress register][progress] remain authoritative. The current
state is setup complete, with new analytical work unstarted or gated;
writing this handoff does not complete LHCT-01.

## Research instruction

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity` on
`papers/investigations-4/11_late_heat_caps_and_charge_transport`.
Begin LHCT-01 unless the current register has advanced. Carry one bounded
analytical stage through to a proved construction, a new usable estimate,
or a precisely scoped failure, with a research note, internal review and
updated progress. Do not stop after another overview or a restatement of
the conditional charge criterion.

The idea is to estimate a distant cap at large **real heat time**, possibly
using late-time root statistics, and combine it with vanishing or controlled
zero-following sides to constrain a multiple endpoint under RH. Standard
Montgomery PCC uses a different asymptotic parameter. A PCC-like theorem
is optional: direct canonical field/jet asymptotics may estimate the cap.
The primary objective is the complete signed flux bound.

## Read before deriving the first result

1. Repository AGENTS.md, LARGE_FILES.md and tools/CHAT_HISTORY.md, then
   the [result index][results] and [avoid index][avoid]. Apply the specific
   [heat-geometry summary][geometry], [collision controls][controls],
   [target classification][a01], [matching controls][a02], [scope][a07]
   and [coupled-error discipline][a12].
2. This home's [README][home], [overview][overview] and [progress][progress].
3. The [founding assessment][assessment], especially its explicit cap
   bounds and moving-zero-side follow-up. Keep it at its source path.
4. [Projective sides and local sectors][sides], [physical-time face
   reduction][physical] and [complete physical boundary assembly][full].
   Retain their exact hypotheses and the distinction between punctured
   sectors and full event-enclosing windows.
5. [BW12 heat/charge transport][transport] and [large-time reconstruction][large-time],
   then the actual [fixed-rank differentiated-saddle theorem][saddle].
   Follow the [canonical-source home][source] when a source estimate is used.

Source proofs prevail over summaries. Do not promote the existing
fixed-finite-rank clock limit to a growing-population theorem, all-height
bound or uniform complex-time estimate.

## First bounded analytical package

Fix a hypothetical ordinary double at (tau,z)=(0,a), with a real,
H=H_z=0 and H_zz!=0. These are conditional event data, not a claim that
a theta double has been found. Use H_tau=-H_zz and the fixed physical jet
G=(H,H_z). A small linking three-sphere has charge one. General event
weights are binom(m,2); the ordinary-double pilot does not settle them all.

Choose one explicit finite terminal time T and a parameterized family
that could later grow. First specify either a complete admissible window
containing the candidate or a regular connector from its linking sphere
to a distant boundary. State the domain in complex tau=t+is and z, the
spatial motion, imaginary-time width, chart cover and all orientations.
Write every early/linking cap, spatial side, imaginary-time face, joining
piece and corner. A candidate event cannot lie on the normalized boundary.
For a full-window bound, other isolated positive-charge interior events
may be retained. A linking deformation instead needs an event-free swept
connector or explicit accounting for every additional event.

Use one concrete side family. On H_z!=0, a regular side
|H/H_z|=epsilon has a fixed projective-circle image, so its curvature and
Chern–Hopf side flux vanish. Prove the actual regular level set, attachment
and continuation required by the selected geometry. An arbitrary moving
circle around a zero is not enough. The raw equation
|H|^2-epsilon^2|H_z|^2=0 also contains joint zeros; it is not by itself a
regular boundary contract. Neither affine projective chart resolves
H=H_z=0. Keep the event inside a full regular boundary, or retain its
excision/linking closure. Distinguish the inherited local chart lemma
from a new continuation theorem over a finite interval or to infinity.

Reduce the complete boundary to explicit signed observations before
choosing an asymptotic estimate. With forward-oriented caps the inherited
identity is

\[
 Q_{W_T}=I_T-I_-+S_T\in\mathbb Z_{\ge0}.
\]

An upper I_T<=U_T, lower I_->=L_- and |S_T|<=e_T give
Q<=U_T-L_-+e_T. A strict upper below one excludes enclosed events.
For an event-free linking connector, retain 1=I_far+I_connectors;
explicitly retained additional events add their positive charge. These are
conditional consumers, not new analytical progress. Identify the
source-derived estimate that will actually pay their terms.

On the same domain, formulate the first LHCT-03 lemma for the full
normalized jet and its tangential derivatives on the complex-time cap.
Specify an evaluated reference flux and a complete integrated remainder.
Retain common phase, source normalization, imaginary-time width, spatial
scaling, cap measure and every derivative required by the three-form.
A nonzero reference is allowed. Do not assume a zero cap from simple
zeros, clock statistics or pointwise density decay. The first new result
may be a finite-to-late continuation estimate, a reference-cap formula
with a controlled remainder, or a scoped obstruction to that specific
construction. Merely re-proving an inherited local chart is insufficient.

If pair statistics become necessary, specify their actual weighted cap
consumer, population and physical gap scale. The finite-cluster
Delta'/Delta identity has inverse-square interactions and an exterior-unit
term. Pay small-gap uniform integrability, outer tails, the unit and
complex-time phase. Do not launch a broad PCC proof or sampling campaign
before identifying that bridge. A direct source/jet estimate can bypass it.

## Controls and the role of computations

Check the proposed analytical mechanism against the inherited quadratic
double, the nonzero cosine cap and the projective shell with its surviving
inner cap. The quadratic retains charge one; the cosine model has simple
clock roots and zero connecting-side flux but a nonzero cap; the shell
shows why shrinking closure size does not imply shrinking flux. None has
the unchanged canonical theta arithmetic. Apply the other [collision
controls][controls] with their separate preservation lists; name a failed
premise before claiming that an estimate separates theta from a control.
Do not assign any control an unproved late-time statistical property.

Numerics may check exact form identities and orientations, diagnose a
candidate's parameter dependence, or rigorously enclose finite constants
after the analytical inequality and full source budget exist. They must
not replace the asymptotic proof, provide an assumed jet floor, or infer
all-height coverage from a finite sweep. No numerical campaign is needed
for the opening analytical stage.

## Deliverables status and history

Save the first new analytical derivation as the next unused numbered note
in this home's notes/, with a corresponding assessment in reviews/.
Keep small supporting scripts and receipts in numerics/ only when needed.
Include Edward Baker, LLM assistance and the new session's **actual** model
and effort; do not copy this handoff's configuration as its own provenance.
Update the existing LHCT register in place and retain the parent's summary
routing. New continuation notes belong to this home; CHB, source and
transport siblings keep their own task ownership.

A finite partial result must name its actual range and class. Leave
endpoint exclusion, arbitrary-height coverage and untreated multiplicities
gated without their own proofs. A theorem valid at every arbitrary
candidate height may use height-dependent constants; a fixed finite list
of heights is different. Do not create a manuscript, snapshot folders,
duplicate task ledger or new chat unless the user asks for one.

At the start and end of the research reply, follow the [history workflow][history-policy].
A genuinely new focused conversation registers its own actual identity
and title in this home's chat-histories/ through refresh_chat_history.py.
This handoff originates from **Review Chern–Hopf zero sensitivity**, thread
01a16517-7550-7a90-9bd0-96983f7b365b, uniquely archived as home 10 number
0009. That is a historical pointer, not an identity for a new session.
If continuing that same conversation, refresh its existing home 10
registration. Do not duplicate, renumber or relocate it. Read the
[history guide][histories] and [dated verification receipt][verification];
receipt counts/hashes are snapshot values, while the canonical registry
holds current values. Arrange the exact-turn final capture unless a
trusted completion hook is verified active.

Finish the research round with the concrete analytical result and scope,
control/review outcome, file links, precise LHCT status changes and the
next unpaid estimate. A target restatement alone is not a completed round.

[home]: ../README.md
[overview]: ../research-overview/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRAM_20261022.md
[progress]: ../research-progress/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRESS_20261022.md
[assessment]: ../../10_chern_hopf_integral_estimates/notes/03_LATE_HEAT_PAIR_STATISTICS_AND_CAP_FLUX_20261022.md
[sides]: ../../notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[physical]: ../../notes/02_CHERN_HOPF_PHYSICAL_TIME_SECTOR_REDUCTION_20261022.md
[full]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[transport]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[large-time]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[source]: ../../02_theta_source_constraints/README.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[history-policy]: ../../../../tools/CHAT_HISTORY.md
[histories]: ../chat-histories/README.md
[verification]: ../chat-histories/CHAT_HISTORY_VERIFICATION_20261022.json

## Execution pointer — 22 October 2026

This prompt was executed by the distinct chat **Continue late heat caps research** (gpt-6-astra, ultra). [Notes 01–04](../notes/README.md) and [Review 03](../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md) record the new finite/growing-interval geometry, canonical cap estimates and complete closure allocation. The initial unstarted state above is historical. Follow the current [sole ledger][progress]; endpoint exclusion and its opposing signed estimate remain open. This pointer does not change the founding chat's identity or registration.
