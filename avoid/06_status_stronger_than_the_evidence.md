# Status words, headlines and novelty claims stronger than the evidence

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A result is described one notch above what was done: "rigorous" for
high-precision floating point, "no error survives" for an internally
reviewed chain, "publishable on its own merits" before a literature
search, a headline that credits the starting hypothesis when an added
hypothesis does the work, a tracked quantity labelled as the bound it
tracks. The mathematics is usually fine; the sentence is not, and the
sentence is what readers and later notes inherit.

## What it looks like here

Manuscript status lines and README headlines; "conditional 11/12-to-33/41"
when the honest form is "(H2) ⇒ 33/41"; a table of \(T_0\)
values labelled \(\Lambda_{c,p}\).

## Evidence

- [Repository review of 9 September](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/repository-review-20260909/REPOSITORY_REVIEW_AND_CHANGE_HANDOFF_20260909.md): "“No error survives” overstated what internal reviews establish"; the fix reached the status files, and the `.tex` still says it.
- [RH-detector STATUS](../papers/misc/rh-detector/STATUS.md): "Certificates are rigorous modulo floating point — high-precision arithmetic (mpmath, 25–30 digits), not interval arithmetic."
- [Finite-response assessment](../papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/reviews/assessment_claude_current_draft_20260914.md): "Four are correct and I withdraw the corresponding claims", with §7 titled "The obstruction claim: I overstated it, and withdraw it"; "publishable on its own merits" and a spectral mechanism "off by about 140×" were withdrawn and the arXiv submission deferred.
- [External review 12 of project 17](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) §6: "The honest headline is "(H2) ⇒ 33/41", not "11/12 ⇒ 33/41""; [addendum 13](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md) §5: "The hypothesis consumed is the conclusion". The [README](../papers/quasi-rh/quasi-rh-exponent-descent/README.md) still leads with the stronger form.
- [Portfolio closure review](../papers/investigations-2/brainstorm/reviews/PORTFOLIO_CLOSURE_REVIEW_CODEX_20261013.md): "The claim that the certification margin grows near a collision confuses the normalized ratio with the quantity being certified"; 19's table "originally labelled \(\Lambda_{c,p}\)" holds tracked \(T_0\) values and now carries a disclaimer that \(\Lambda\le T_0\) is not proved.
- Novelty before search: [ROUND12](../early-chat-logs/initial-project-files/rh3/claude/ROUND12_execution_and_a_retraction.md) §4.5, "for every claim of the form "X is new", run the search that would show X is old — before publishing, not after", which "cost a same-day retraction"; [PROGRAM_CLOSED](../early-chat-logs/initial-project-files/riemann-hypothesis/claude/PROGRAM_CLOSED.md): "One of four was checked and came back known; that should lower confidence in the rest."
- In this round: Review 16's "a successful mechanism must use the Euler factor at every prime simultaneously" and that "contour shaping can only change constants" (Response 17's words for message 16) were withdrawn in [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md) §§3, 6.

- [Reply 03 §5](../papers/brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md) called the translate-span picture “a definite formula” before deriving it. The [Sonin round-one cross-model review §3](../papers/investigations-3/04_sonin_mixed_prime_response/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md) says “I withdraw the reply’s identification”; the inverse metric cancels an unbounded shifted gamma part. [Codex reconciliation](../papers/investigations-3/04_sonin_mixed_prime_response/reviews/02_CODEX_RECONCILIATION_OF_ROUND_ONE_REVIEW_20261017.md) accepts this scoped correction. Evidence added 17 October 2026 for Edward Baker with LLM assistance, **gpt-6.1-sol**, effort **ultra**.

## What it cost

A same-day retraction; a deferred arXiv submission; correction blocks and
a legacy-key guide in 19; headlines that still outrun their reviews.


- **Positive correction, 17 October 2026:** [Project 03 Review 02](../papers/investigations-3/03_effective_outer_remainders/reviews/02_UNIFORM_FLOOR_AND_RESTARTED_COMPARISON_REVIEW_CODEX_20261017.md) distinguishes a new complete-domain certificate from the old samples: “The original lower-conductor zero-loss thresholds, derivative-circle bounds, and zeta value \(0.18891\) do not acquire stronger status.” The new family bound is explicitly “proved in-note” with internal same-model checks; scalar replay is not an audit of every analytic import. Added for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), ultra**.

## Instead

Use the status vocabulary of [`result-summaries/README.md`](../result-summaries/README.md) and the source's own words; state the hypothesis that does the work in the headline; run the originality search before "new" (house rule 2 of [`CONTRIBUTING.md`](../CONTRIBUTING.md); item C2 of the [first-slab protocol](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/PROTOCOL_C1_C2.md)); when a claim is withdrawn, write the withdrawal into the file that made it, not only into a review ([`REDACTION_CHECKLIST.md`](../early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md) item 9: corrections get a pointer, never a silent fix).
