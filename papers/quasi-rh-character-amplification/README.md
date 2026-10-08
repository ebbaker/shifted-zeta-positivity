# Quasi Riemann hypothesis character amplification

Prepared for Edward Baker, 8 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This investigation studies whether the character-family and cubic-theta
methods in OpenAI's October 2026 quasi-RH release can improve the resulting
prime-variance baseline or help bound our complete signed covariance.

The [working manuscript](manuscript.tex), *Conductor localization of a mixed
inverse–plain moment in a sextic character family*, is drafted for Edward
Baker. It presents the conditional reduction and its proofs, keeps the
remaining signed estimate explicit, and includes an LLM acknowledgement.
The [manuscript review](reviews/MANUSCRIPT_REVIEW_20261008.md) records the
scoped checks and successful native compilation. The concise
[manuscript history](DRAFT_HISTOR.md) replaces draft snapshot folders.

The current **conditional extension** supports the candidate boundary
`7/8 - 1/24000 = 20999/24000`, with local variance consequence
`O(X^(11/4 - 1/12000))`. This improves the first candidate's displacement
by a factor of 25. Increasing the total prime-slot length while preserving
the scale identity keeps the principal signal exponent unchanged. An
exact polynomial certificate controls the complete continuous parameter
range for the exceptional-row count.

The applicability of the low estimate, moment estimates, and contour
arguments has received separate source-scoped audits, including a
separate same-model check of the exact certificate. The external
reflection and moment proofs and the source's seven-eighths theorem
remain assumptions. No Lean proof was replayed. These records do not
establish an independently verified new zero-free theorem or priority.

The next-stage reduction now isolates a nearly saturated residual class.
Existing moments improve profiles outside that class after the detector
cutoff is retuned. A NEW restricted mixed-moment saving of `1/5000` in
its exponent would suffice for the next target `7/8 - 1/20000`; that
estimate remains unproved, so it is not adopted as the current candidate.
The common-signal and off-balance scouts also make their missing inputs
and existing costs explicit.

The first mixed-moment calculation now removes low primitive-row conductors,
the entire plain-variable diagonal, and ratio-character conductor blocks
through `U^(4/5)`. Their errors lie below the requested mixed exponent by
explicit margins. The unresolved input is a precisely specified signed
sum over distinct plain ideals on the remaining large-conductor rows;
the existing transformed inverse proof does not cover its coefficient class.

| Record | Contribution |
| --- | --- |
| [Current geometry extension](notes/GEOMETRY_OPTIMIZATION_20261008.md) | Derives the candidate `7/8 - 1/24000`, all range margins, and the exact endpoint certificate. |
| [Mixed-moment reduction](notes/MIXED_MOMENT_REDUCTION_20261008.md) | Combines three controlled contributions into one explicit remaining signed sum. |
| [Column kernel and small conductors](notes/MIXED_KERNEL_CONDUCTOR_REDUCTION_20261008.md) | Derives the exact masks and proves the ideal-pair bound removing conductors through `U^(4/5)`. |
| [Primitive row conductors](notes/SATURATED_MIXED_ARITHMETIC_20261008.md) | Uses the actual conductor in reflection to obtain the required mixed saving on smaller-conductor rows. |
| [Mixed transfer audit](reviews/MARKED_MIXED_TRANSFER_AUDIT_20261008.md) | Identifies the enlarged dual range and forbidden transformed divisor coefficient in a direct source-proof transfer. |
| [Mixed reduction review](reviews/MIXED_REDUCTION_REVIEW_20261008.md) | Checks the new pair count, masks, diagonal, conductor bounds, and noncircular use of the old row count. |
| [Localized next target](notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md) | Synthesizes the new reduction and certifies the conditional payoff of an explicitly unproved residual estimate. |
| [Full amplitude profiles](notes/AMPLITUDE_PROFILE_REDUCTION_20261008.md) | Derives actual whole-slot selection, cutoff retuning, and the remaining nearly saturated class. |
| [Joint inverse/plain witnesses](notes/JOINT_WITNESS_REDUCTION_20261008.md) | Identifies the smaller mixed moment, exact truncated convolution, and the two rebalances needed for its payoff. |
| [Two common-signal probes](notes/COMMON_SIGNAL_PROBE_SCOUT_20261008.md) | Constructs admissible probes and their signed mixed kernel; separates one-mode cancellation from a uniform power gain. |
| [Off-balance geometry](notes/OFF_BALANCE_GEOMETRY_SCOUT_20261008.md) | Derives the dual-length cost and shows positive imbalance worsens the current low envelope. |
| [Localized reduction review](reviews/LOCALIZED_TARGET_PROFILE_REVIEW_20261008.md) | Independently checks the exact endpoint certificate, profile compatibility, and mixed-moment payoff. |
| [Research directions from the repo](notes/RESEARCH_DIRECTIONS_20261008.md) | Ranks joint witness estimates, full amplitude profiles, common-signal probe combinations, and new geometry; separates usable identities from missing bounds. |
| [Low estimate audit](reviews/LOW_STRUCTURAL_AUDIT_20261008.md) | Checks the actual-row, coefficient, and Gram requirements; derives the admissible geometry and required positive-part correction. |
| [Moment and count audit](reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md) | Checks fixed `kappa=3/4`, witness classes, capacities, prime supply, quantifiers, and independently verifies the new certificate. |
| [Contour and normalization audit](reviews/CONTOUR_TRANSFER_AUDIT_20261008.md) | Checks the enlarged Euler domain, full correction, principal residues, outer rows, and order of choices. |
| [Exact arithmetic records](numerics/README.md) | Reproducible rational identities, continuous positivity certificates, and retained margins. |
| [Initial comparison](notes/OPENAI_QUASI_RH_COMPARISON_20261008.md) | Compares the two research programs and translates announced boundaries into variance exponents. |
| [First parameter extension](notes/PARAMETER_EXTENSION_20261008.md) | Retains the initial `7/8 - 1/600000` derivation and Euler-domain repair. |
| [First extension review](reviews/PARAMETER_EXTENSION_REVIEW_20261008.md) | Records the initial scoped checks and domain repair. |
| [Character-family transfer targets](notes/CHARACTER_FAMILY_TRANSFER_20261008.md) | Identifies unproved short-family targets and the coefficient and field obstacles to a direct covariance transfer. |

The current geometry has a specific limit: with `b=1/8` and the same
row-count bound, the high estimate loses its strict saving near boundary
`0.8749572006154`. This is a limit of that parameter family and estimate,
not a mathematical barrier to stronger results. Repeating the present
adjustment does not by itself approach RH.

The next arithmetic task is to bound the signed term in equation (12) of
the mixed-moment reduction, retaining the row selector and the actual
Möbius divisor coefficients. A direct transfer of the existing canonical
moment fails both its width and coefficient hypotheses. The separate
short-family program still seeks a sufficiently uniform sextic Mobius
mean square with row range `H=D^h`, `h<9/10`.
Independent specialist or formal validation of the imported machinery
and the extension remains necessary before treating the candidate as
an established theorem.

Research belongs in `notes/`, checks in `reviews/`, and reproducible
calculations in `numerics/`. Third-party PDFs and large derived files
remain outside the repository under [LARGE_FILES.md](../../LARGE_FILES.md).
The [prime-variance investigation](../prime-variance-exponents/README.md)
supplies the existing response, scalar, and equivalence results.
The current manuscript is a single editable source. No manuscript snapshot
or commit milestone was created; later milestones belong in the history index.
