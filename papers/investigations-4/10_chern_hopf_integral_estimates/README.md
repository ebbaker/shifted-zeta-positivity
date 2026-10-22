# 10 Chern/Hopf integral estimates

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded **gpt-6.1-sol (Codex), effort
ultra**, verified from this turn's metadata.

**Status: dedicated home and results write-up established; conditional local
identities, trace/remainder bounds and scoped estimator failures inherited
from the existing research; coupled signed tail bounds now proved and
interval-certified at one regular theta critical point. A global canonical
signed improvement remains open.** This home collects the evaluated Chern/Hopf mass, its comparisons
with spatial Gauss area, and the g_2=q² critical-wall amplitude connection.
Integral estimation is useful independently of collision exclusion.

Start with the [results write-up](notes/01_ESTABLISHED_MASS_TRACE_AND_AMPLITUDE_RESULTS_20261022.md),
then the [research program](research-overview/01_CHERN_HOPF_INTEGRAL_ESTIMATION_PROGRAM_20261022.md)
and [sole CHB progress register](research-progress/01_CHERN_HOPF_INTEGRAL_ESTIMATION_PROGRESS_20261022.md).
The existing program and register moved here; their former locations are
routing pages. CHB task IDs and statuses are preserved, with no second ledger.

The reusable results are:

- Complete local physical boundary assembly and a positive regularized mass
  with bounded-weight estimates.
- Direct Gauss-area/regulator-bias bounds and a scoped failure of the
  existing global inverse-Schur certificate for every finite regulator.
- A sharp spatial critical-wall trace and a fully costed bulk-to-curve
  estimate; the specified local-Schur/total-mass certificate is weaker than
  direct critical-value estimation from the same data.
- Explicit signed cancellation C_2-C_0/t=tB', bounded endpoint remainder
  and signed center, with wall/source/regulator errors retained.
- [Coupled signed tail estimates](notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md)
  using both C_0=V and S_1=0. Their exact-data widths improve specified
  same-moment Taylor intervals by factors 4/5 and 3/7; complete finite
  interval arithmetic retains strict gains. An added direct signed tail
  integral is substantially sharper in the actual pilot.

These remain **proved in-note in their stated conditional local scope**,
with internal LLM reviews. The new finite acquisition concerns a regular
critical point, not a conditional theta collision. No new global theta sign,
subunit logarithmic budget, all-height theorem or simplicity proof is
claimed. The [write-up review](reviews/01_HOME_AND_RESULTS_WRITEUP_REVIEW_20261022.md)
checks faithful synthesis and organization; it is not new independent
mathematical validation. The [coupled-tail review](reviews/02_COUPLED_SIGNED_TAIL_REVIEW_20261022.md)
checks the new proofs, actual acquisition, complete errors and comparator scope.

## Sources, ownership and next work

The detailed shared derivations [01–06](../notes/README.md), original
home 03 reviews and hash-bound execution records retain their source paths.
The new write-up presents them together without replacing those sources.
New focused derivations belong in this home's notes/, small computations
in numerics/, and assessments in reviews/. [Home 02](../02_theta_source_constraints/README.md)
continues to own the unchanged canonical source and full reflection ledger.

[Home 03](../03_heat_transport_and_charges/README.md) retains its broader
heat-transport/charge and ICW tasks. [Home 07](../07_weighted_green_integrals/README.md)
owns its separate weighted-Green consumer. This home owns CHB execution;
it links sibling results when applicable rather than duplicating their work.

**Next unpaid task:** acquire additional arithmetic information for the
complete conditional signed quadratic or a localized mass/error consumer,
improving a complete certificate over the equally informed direct method.
The new finite moment refinement does not beat its added signed quadrature
comparator. Retain the signed C_2C_4+S_3² center,
S_1=0, simultaneous event matching, full source tails, wall uncertainty and
the unit logarithmic endpoint term. Repeating either stopped certificate
comparison does not pay this task. CHB-04 stays complete in its conditional
local scope; CHB-05 acquisition is unperformed; CHB-06 and inherited
BW10/BW12 exclusion gates remain unchanged.

Follow [AGENTS.md](../../../AGENTS.md), [LARGE_FILES.md](../../../LARGE_FILES.md),
the [history policy](../../../tools/CHAT_HISTORY.md), [result index](../../../result-summaries/README.md)
and [avoid index](../../../avoid/README.md), particularly
[local heat geometry](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../result-summaries/12_collision_controls_and_screening.md),
[target classification](../../../avoid/01_restating_the_target.md),
[scope](../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[coupled terms](../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The [milestone record](DRAFT_HISTORY.md) distinguishes the initial
organization from the later coupled-estimate acquisition.
The [home-establishment receipt](HOME_ESTABLISHMENT_20261022.json)
records the program/register routing; [chat histories](chat-histories/README.md)
retain the actual conversation identity and provenance.
