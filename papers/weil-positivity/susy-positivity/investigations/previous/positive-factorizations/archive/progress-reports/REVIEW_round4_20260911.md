# Round 4 review and continuation: shifted odd factor and an even-sector reduction

11 September 2026. Research notes only; no new manuscript version.

Reviewed branch: `susy-positivity`. Baseline: commit
`f92e775b44765a0f2e7fcfa69eb3bfb986ea46bb` ("Work from Codex on gamma contributions").
The working changes seen at the start of the review were committed by the
researcher during this session. The review below refers to that commit.

## Outcome

The round-3 odd factor, first-prime test, and their rational certificates
survived this review. No blocking mathematical error was found in the
arguments examined. All three original checkers were replayed successfully
from temporary copies; the repository's recorded diagnostics were preserved.
This is an AI-assisted proof audit, not independent specialist certification.

The continuation produced three concrete results:

1. **An explicit shifted odd factor.** The existing cubic gives a positive
   factor of the shifted gamma form for every `0 < L <= 7/10` and
   `0 <= omega <= 1/2`, with floor `1/200`. This completes the shift parameter
   for this odd construction. It is a factor of the full shifted Weil form
   only on the prime-free range `L <= log(2)`.
2. **A coercive even subspace.** At central shift, the gamma form is bounded
   below by `11/100` on even functions of mean zero, for `L <= 7/10`. The
   remaining even-sector sign reduces exactly to one scalar Schur complement.
   That scalar is not evaluated or proved positive in this round.
3. **A failed simplification with an exact witness.** Replacing the smooth
   gamma remainder by its value at zero and replacing the even pole amplitude
   by a constant gives a negative value on `1-(2x/L)^2` at `L=log(2)`.
   Thus these small-looking terms cannot be discarded when designing an even
   completion. This is a failure of the simplified model, not of the Weil form.

Read the [shifted odd proof](SHIFTED_ODD_FACTOR_round4_20260911.md),
[even-sector reduction](EVEN_SECTOR_REDUCTION_round4_20260911.md), and
[reproducibility record](REPRODUCIBILITY_round4_20260911.md).

## Review of the existing work

| Claim or component | Review result and qualification |
|---|---|
| Full-output jump formula and normalization | The exterior output, constant `w0`, endpoint logarithms, and pole signs agree between the Fourier, jump, and kernel descriptions. Omitting exterior output would change the form. |
| Small-window factor | The positive conductance and potential estimates have the stated restricted range. The shift correction subtracts the required diagonal contribution. Original identity checks pass. |
| Local auxiliary tower | Single-channel minimization, summation, and the weighted auxiliary Hilbert space are consistent. The componentwise closedness and density arguments work with smooth `H^1` tails. The tower realizes only the kinetic term. |
| Pairwise comparison obstruction | The two-by-two Gram reduction and bounded comparison correction are consistent. The exact sign checker passes. The constant witness can be approximated in the logarithmic form norm. |
| Hidden-node restriction | The off-diagonal triangle inequality gives the comparison Schur inequality with the correct direction. This remains a finite-network statement unless convergence of comparison forms is separately proved. |
| Odd cubic potential | Rechecked the singular polynomial action, `r'` bound, folded pole coefficient, and interval reduction. The complete interval cover passes; the first cell gives the smallest old certified lower bound. |
| Odd factor domain | The cubic is positive on the open half interval. Odd smooth inputs have bounded quotient at zero. Closing the factor is justified after its positive norm identity is established; the graph norm is equivalent to the logarithmic form norm. A subsequence argument identifies the closed components with the displayed weighted functions. |
| Linear-input first-prime signs | The correlation `1-3t/L+2(t/L)^3`, mass sum, prime coefficient, and diagonal debit agree. The rational certificate confirms all three strict signs. |
| Cap-reflection identity | The factor of `sqrt(2)` in folding, parity sign, and projections are consistent. Both signs of the prime contribution occur; the original controls pass. |
| Whole-line closability obstruction | The expanding-support sampling sequence is valid. The argument assumes a factor, obtains RH from Weil positivity, and then contradicts closability. It does not assume RH as an external premise, nor exclude other input topologies. |

The review distinguishes the analytic reductions from the programs that
evaluate their bounds. Passing a program cannot establish a missing
reduction. The new proof likewise includes its derivative estimate and
length-uniform argument before invoking interval arithmetic.

## Literature findings and attribution

The phenomenon that a prime can restore positivity after the archimedean
contribution loses it is already explicitly present in Connes and Consani,
*Spectral triples and zeta-cycles* (2023), Sections 2.2–2.4, especially
Figures 7 and 13–17. Their finite-matrix experiments examine both parities
near prime-power thresholds. The present round-3 contribution should be
described as a certified elementary witness and a design constraint on the
proposed edge remainder, not discovery of the stabilization phenomenon.
Comparing numerical eigenvalue sizes requires a normalization and basis
dictionary. [Published paper, pp. 112–116](https://ems.press/content/serial-article-files/44477).

Suzuki's *Weil's quadratic form via the screw function*, version 2 dated
17 August 2026, provides the relevant closed-form operator setting.
Sections 3–5 discuss logarithmic form domains, endpoint approximation,
compactness, and small-interval behavior. In particular, equation (4.4)
contains the singular difference energy and boundary logarithm used in the
even-sector analysis below. Its small-interval result is not an explicit
certificate of our length cutoff or cubic factor. [Suzuki v2](https://arxiv.org/html/2606.09096v2).

Theorem 1 of Connes and Consani's archimedean trace-formula paper imposes
support and Fourier-vanishing conditions. It should not be imported as an
unconditional factorization on the entire even subspace. Its Sonin-space
construction remains relevant conceptual background, with a separate
matching problem. [Theorem 1 and surrounding discussion](https://arxiv.org/html/2006.13771v1).

This was a targeted primary-source comparison, not a complete priority
search. No novelty claim is made for reflection decompositions,
ground-state transforms, harmonic-number diagonalization, or scalar Schur
complements.

## What the new work changes

The old [status ledger](../../STATUS.md) correctly describes the baseline,
but its statement that a shift-uniform odd factor is open is superseded by
the new background proof. The manuscript and that ledger were left in their
committed state at the researcher's request.

The even problem is now more precise: a known coercive subspace can be
separated from one remaining scalar condition. A practical next step is to
construct an explicit response to the coupling vector on that subspace,
with a residual bound small enough to decide the scalar sign. Repeating a
large finite-depth certification campaign would not, by itself, supply the
arithmetic selection rule sought in this project.

The first-prime joint construction, compatibility across multiple delays,
and global positive mechanism remain open. The new shifted odd factor does
not increase the positivity range already known from the first-slab paper;
it makes one particular factor construction uniform in shift.

## Preservation and verification

All new repository deliverables from this session are Markdown files in
this background folder. No manuscript source, PDF, manifest, historical
diagnostic, or synced project source was changed. The baseline manifest's
12 recorded hashes matched when reviewed. Original checkers and new code
were executed in temporary locations; the new code is retained as fenced
text in the reproducibility note rather than as additional repository
program files.

The existing manuscript remains a working draft. The new results have
written derivations, exact arithmetic checks where stated, and separate
floating-point identity diagnostics; specialist mathematical review and a
full literature audit remain outstanding.
