# Not reading sibling results and stop lists; closures recommended but never written

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A branch opens without reading the closures, rules and stop lists that
sibling branches produced days earlier, and re-derives them in new
coordinates; a review recommends closing a branch, the recommendation is
"parked", and no closing note is written, so the next branch cannot find
it; a correction is adopted in one review and never propagated to the
reviews that carried the error; a README keeps a superseded candidate as
"current".

## What it looks like here

WZW opened six days after the amplitudes it used had been surveyed and
excluded; 21 and 22 executed the 11 October stop list item by item
without citing it; the heat-lane closure note recommended by two reviews
does not exist; fact (D)'s erratum is absent from the reviews that state
it; the amplification README does not cite the result that superseded it.

## Evidence

- [WZW assessment](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/WZW/reviews/review_claude_wzw_program_assessment_20260924.md) §0: "Four results from sibling investigations are not cited anywhere in WZW/"; the amplitudes were "surveyed and excluded six days before the WZW folder opened". The recommended closure was parked ([cross-program note](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md): "park the tested WZW transfer constructions without declaring a universal closure") and no closing note exists; the same note admits "This assessment overlooked that later result".
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §4: "Investigations 21 and 22 re-derive those rules in new coordinates without citing them."
- [First-prime resonance review](../papers/investigations/sonin-critical-boundary/reviews/FIRST_PRIME_RESONANCE_REVIEW_20261003.md): "the next bounded task was already answerable with existing repository tools".
- The heat-lane closure note recommended in [external review 12](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) ("close with closure note") was never written; the erratum for fact (D) recommended in the [cross-assessment](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md) §3.1 is still absent from reviews 12–13.
- [Amplification README](../papers/quasi-rh/quasi-rh-character-amplification/README.md) still calls 20999/24000 the current candidate; the [priority review](../papers/investigations-2/brainstorm/PRIORITY_REVIEW_AFTER_AUDITS_CLAUDE_20261012.md) §4.7 records that Liu superseded it.
- The positive example: the [Loewner README](../papers/weil-positivity/susy-positivity/investigations/loewner/README.md) closes "with proofs rather than with an expectation", names the durable output, and moves the forward question to a new folder; the [close-and-merge recommendations](../papers/investigations-2/active/CLOSE_AND_MERGE_RECOMMENDATIONS_CLAUDE_20261013.md) and the [portfolio consolidation](../papers/investigations-2/PORTFOLIO_CONSOLIDATION_20261013.md) did the same for nine folders.

## What it cost

Duplicate work across WZW, 21 and 22; rules R1–R5 rediscovered as
theorems; readers of the amplification folder and of reviews 12–13 given
superseded information.

## Instead

At branch opening, read the stop list and the closures of the last two
weeks (this folder and [`result-summaries/`](../result-summaries/README.md) exist to make that cheap); at branch closure, write the closing note on the Loewner template and do the cross-investigation synthesis explicitly, since sibling results can close a branch even when never cited within it; when a correction is adopted, propagate it to every file that states the error, with a pointer header ([`REDACTION_CHECKLIST.md`](../early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md) item 9).
