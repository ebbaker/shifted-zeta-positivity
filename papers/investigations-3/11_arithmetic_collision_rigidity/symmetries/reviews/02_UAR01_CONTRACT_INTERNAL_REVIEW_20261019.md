# UAR-01 contract: internal mathematical review

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Root assistant plus separate same-model derivation and adversarial readers. This is internal LLM review, not specialist human review or an implementation-independent analytic proof.

**Disposition: pass as a shared contract milestone.** [UAR-01 Note 07][note] defines the corrected finite approximation and complete residual, charts, interval, transition convention, error destinations and comparison norm required by the [program][program]. UAR-02 and UAR-03 may start independently from this contract. No numerical estimate, physical acceptance input, positive anchor, coverage or cost advantage is established. UAR-04 still needs useful outputs from both estimating tasks.

The review consulted S03 Notes 03/06/07, S04 Notes 01/03, S02's analytic correction and the older [cutoff-matching Note 22][old]. The latter already establishes the exact profile jump and a complete printed-correction matching estimate. Its displayed shrinking-sector asymptotic corollary is restricted to kappa<=3/2 and a frozen-center exponential correction. Neither that corollary nor S03's fixed-B polynomial edge/error constants have been promoted to the new kappa<=2 analytic-correction contract.

The checked mathematical points are:

- The full analytic correction includes parity (-1)^(N+1), both profile components and their removable continuations. The two finite channels use s and 1-s; the RS contour's second channel uses the reflected analytic contour, rather than assuming the descending contour has real coefficients.
- The real sector determines centers; its small complex disks extend outside the center interval without borrowing center constants there. Cutoffs stay frozen in derivatives. The half-radius real windows, one-crossing disk geometry, nonvanishing A and real omega bound are consistent with the inherited sources.
- The entering mode and correction jump form h_n=f_n-f_(n-1), so the residual jump is -h_n. The ordinary sum of local residual integrals contains **+i sum Z_h**. The physical approximation return contains the corresponding negative transition sum. Same-N overlaps add no artificial charge. Endpoint ownership includes coincident cutoffs.
- The ledger retains the first gamma/heat correction in the residual model and assigns its higher terms and tails to UAR-02. It assigns the actual RS edge, gamma prefactor, Gaussian tails, coherent continuation and all profile replacements to UAR-03. A printed real-parameter estimate alone is not a holomorphic disk bound.
- The normalized forced heat equation contains 2(A_x/A)r_x and (A_t/A+A_xx/A)r; the contract uses no homogeneous-residual shortcut. Endpoint error payment needs a value and first derivative, while any later second-jet consumer has an additional obligation.

Corrections made during review: the initial edge notation was made explicitly sharp-reflected; the S04 comparator was restricted to the actual natural-center frozen N and center-to-window prefixes; and the direct envelope comparison was strengthened to the available real-symmetric Schwarz-Pick radius. These changes prevent accidental use of the raw residual constant for the corrected or alternate-cutoff scalar and avoid choosing a weaker independent-box comparator. All are incorporated in the reviewed note.

The [exact checker][checker] verifies the profile-shift Laurent reduction, jump phase/parity, multi-chart and partial-prefix transition signs, the normalized heat product rule, and omission mutations. It rejects invalid sector inputs and missing/stale sources. An exact polynomial heat event with f=Q and r=0 checks that zero approximation error is compatible with a zero physical first jet. The [receipt][receipt] pins the installed note, checker and analytic inputs. These bounded fixtures check bookkeeping and guards; they do not numerically verify an unbounded theta estimate.

Source-specific premise screening is explicit for finite-prime, weighted-square, reflected/shape/primitive, Euler, polynomial and moving-wall controls. This contract adds no acceptance consumer, and no theta allowance is assigned to an altered source. The existing Euler negative-Laguerre witness is kept distinct from a collision event. Future UAR-V1 instances must test each changed estimating or acceptance interface using its own source/errors.

**Remaining obligation:** prove complete uniform finite-mode and edge-model errors on the common disks and then bound the recombined signed expression, including every transition and partial prefix. Definitions and exact identities alone do not pass those estimating gates. The physical anchor and matched consumer are later obligations. The real bridge and complex exterior remain open.

[note]: ../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[program]: ../research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md
[old]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[checker]: ../numerics/check_uar01_contract.py
[receipt]: ../numerics/UAR01_CONTRACT_CHECK_20261019.json
