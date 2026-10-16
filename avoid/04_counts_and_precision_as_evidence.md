# Assertion counts, replay totals and precision read as evidence

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A checker loops an identity over thousands of polynomial germs, rational
surrogates or mask patterns, and the total ("12,271 exact replay
assertions", "725,761 assertions", "1,177 numerical observables agree at all 45 saved" digits) is
reported in READMEs and reviews as if it measured the strength of a
theorem or the state of the research. The count measures the loop; the
identity it checks is often one line; the hard case is frequently the one
the loop never exercises; and precision agreement between two programs
sharing a formula does not detect a shared error.

## What it looks like here

Headline totals in investigation READMEs; "exact assertions" cited as a
reason for confidence about theta; three Lean acceptances derived from one
proof counted as three; trial spaces enlarged eightfold with no change in
the answer.

## Evidence

- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §9: totals such as "12,271 exact replay assertions" are counts of identity checks on polynomial germs and rational surrogates, "not evidence about theta".
- [Mixed note-25 review](../papers/quasi-rh-exponent-descent/reviews/MIXED_NOTE25_REVIEW_AND_NEXT_STEPS_20261009.md): "725,761 assertions should nevertheless be read through coverage, rather than their total"; about 98.45% were mask identities, the checker never exercised the hard case, and its ledger omitted the sieve deficit. The [exponent-descent README](../papers/quasi-rh-exponent-descent/README.md) still leads with "26,966 finite assertions".
- [External review 12 of project 17](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) §7: "Assertion counts are loop counts".
- [Cross-family review of replays](../papers/investigations-2/formal_replay_crosswalk/reviews/CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013.md): "the three acceptances check three statements derived from one shared proof … The records should not read as three independent proofs."
- [CCM energy-ports note](../papers/investigations/ccm-operator-realizations/notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md): "1,177 numerical observables agree at all 45 saved" significant digits, while the [string realization review](../papers/investigations/ccm-operator-realizations/reviews/STRING_REALIZATION_CRITICAL_REVIEW_20260926.md) warns: "Precision agreement does not detect a shared modeling or formula error"; [arithmetic-storage assessment](../papers/investigations/program-meta-analysis/reviews/ARITHMETIC_STORAGE_PROGRAM_ASSESSMENT_20260929.md): "Higher numerical precision cannot repair this fixed trial space."
- [Short-family continuation](../papers/quasi-rh-exponent-descent/short_families/notes/20_SHORT_FAMILY_SESSION_CONTINUATION_20261008.md): "do not confuse a larger assertion count with a stronger theorem."

## What it cost

Reviews and READMEs that had to be reread with the counts discounted;
crosswalk labels revised; a ledger that hid a deficit behind a total.

## Instead

Report what a checker checks (which identities, on which class of
inputs, whether any genuine theta integral is involved) next to any count;
receipts in the second portfolio now say so, and
[result-summaries 15](../result-summaries/15_verification_infrastructure.md)
lists the convention. Treat agreement of two programs as evidence only when
they share no code and no formula ([19's two-program certificate](../papers/investigations-2/active/19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md) is the model). The [program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md) §4.7: "hundreds of passed identity checks do not establish omitted-input bounds or an asymptotic theorem".
