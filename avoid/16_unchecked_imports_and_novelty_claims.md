# Facts imported from the literature or from PDFs without checking the source

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A statement about what a published paper proves is taken from memory, from
a summary, or from an automated reading of a long PDF, and then built on.
Automated readings have fabricated content in this project; plain text
extraction has dropped overbars; and a misremembered theorem has travelled
through two reviews and a rule before anyone read the original. The
positive version of the same failure is a novelty claim made before the
search that would show the result is known.

## What it looks like here

"Fact (D)" about Polymath 15; fabricated §10.2 content from three fetches;
a wrong normalization from a dropped overbar; a "universal threshold"
theorem; "X is new" before the search.

## Evidence

- [Cross-assessment](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md) §3.1: "Fact (D) is not what Polymath 15 proves" (the barrier only excludes zeros above \(y_0=0.2\)); the fact had been used in reviews 12, 13 and rule R5.
- [ROUND11](../early-chat-logs/initial-project-files/rh3/claude/ROUND11_freeboson_and_positivity.md) §1.1: "Three separate fetches fabricated §10.2 content, two of them mutually contradictory."; [`CONTRIBUTING.md`](../CONTRIBUTING.md) rule 3: "Automated readings of long PDFs have fabricated content in this project."
- [Short-family small-cofactor review](../papers/quasi-rh/quasi-rh-exponent-descent/reviews/SHORT_FAMILY_SMALL_COFACTOR_REVIEW_20261008.md): "the plain PDF extraction dropped overbars".
- [ROUND12](../early-chat-logs/initial-project-files/rh3/claude/ROUND12_execution_and_a_retraction.md) §4.5: "I published with the caveat attached rather than resolving it first, which cost a same-day retraction."
- The Suzuki normalization (item C1 of the [first-slab protocol](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/PROTOCOL_C1_C2.md)) is still "the single highest-risk unverified item", and [`references/README.md`](../references/README.md) flags the Suzuki quotations for human confirmation.
- Done right: Paper 2's imports from Kasahara were "source-verified against the original paper" ([omega-string STATUS](../papers/weil-positivity/shifted-zeta/omega-string/STATUS.md)); the Newman certificate audit read every analytic link of Gomila's hypotheses (ii) and (iii) ([audit README](../papers/investigations-2/newman_certificate_audit/README.md)).
- In this round: Review 16's Corollary 2 cited two 2026 \(\Lambda\) claims it "could not verify" and said so; [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md) §1 quotes the published \(\Lambda\) bounds "as I read the literature" for the same reason.

## What it cost

A full agent run; a wrong normalization; a same-day retraction; a rule
(R5) stated for a region the cited theorem does not cover.

## Instead

Ask for the file and read the printed PDF ([`CONTRIBUTING.md`](../CONTRIBUTING.md) rule 3, the standing rule of ROUND11); quote the theorem number and its hypotheses next to any imported fact; mark unverified imports as such in the text, not only in a footnote; and run the originality search before the word "new" (house rule 2; protocol item C2).
