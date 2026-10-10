# Internal review of the finite multi-cutoff candidate family

10 October 2026. Model GPT-6.1-sol (Codex), configured reasoning effort
ultra, verified from the parent chat recording and inherited by delegated
work. These are internal derivation, interval and agent replay checks,
not independent mathematical review.

Reviewed [Note 5](../notes/5_MULTI_CUTOFF_CORRELATED_CANDIDATE_FAMILY_20261010.md),
[the generic source](../numerics/check_multi_cutoff_candidate_family.py),
the certificates for
[22067](../numerics/MULTI_CUTOFF_M22067_CERTIFICATE_20261010.json),
[22068](../numerics/MULTI_CUTOFF_M22068_CERTIFICATE_20261010.json) and
[22080](../numerics/MULTI_CUTOFF_M22080_CERTIFICATE_20261010.json), and
[the family build record](../numerics/MULTI_CUTOFF_CANDIDATE_FAMILY_BUILD_RECORD_20261010.json).
All earlier sources and certificates remain preserved.

## Result and exact scope

For each \(M\in\{22067,22068,22080\}\), the exact domain is
\[
 [(2\log M)^{-1},1/20]\times[4\pi M^2,4\pi M^2+8].
\]
These are three disconnected local rectangles in distinct natural-cutoff
cells. They do not cover complete cells, cutoff boundaries or the height
gaps between windows. No cutoff-change correction between these windows
is used or needed; each has its own constant natural integer cutoff.

The new atlases have 29, 28 and 32 closed height strips. Their value
screens prune 16, 14 and 15 strips, leaving 13, 14 and 17 strips that
simultaneously pass the first-jet Schur candidate condition in reverse
and the fully paid physical derivative condition in reverse. The
certificates prove exactly 12, 12 and 13 simple genuine heat zeros at
every time in their respective domains. There are no unresolved boxes.
The uniform normalized joint-vector floors exceed 0.03117, 0.02205 and
0.0032919.

The Schur predicate is checked actively. Here its conjunction with a
positive paid derivative gap makes it redundant for joint exclusion:
the derivative term alone already exceeds one. These certificates do
not establish an arithmetic example of additional exclusion from the
curved error body. Only two retained strips per cutoff also pass the
coarse rectangular complete-current test; the remaining enclosures are
inconclusive, not certified negative actual currents.

## Analytic checks

1. The exact sector edge follows from \(t_M(2\log M)=1\), positive
   height offset and monotonicity. The numerical outer hull is explicitly
   distinguished from the exact domain. The upper time endpoint is
   exactly \(1/20\), and \(1\le tL<1.000243<2\) is checked/proved
   on the exact domain.
2. Natural-cutoff squared bounds lie strictly between \(M^2\) and
   \((M+1)^2\) throughout each rectangle. Distinct rectangles are never
   spliced into an alleged contiguous height cover.
3. Every rectangle rebuilds all its genuine summands, carrier parity,
   weights and 64 signed coherent midpoint jets at its own \((t_M,x_M)\).
   The global polynomial remainders use the complete 64th absolute
   frequency moment. No complement or cross interference is omitted.
4. Physical spatial amplitude drift, carrier curvature and normalizer
   coefficients are paid over the full height hull. Fixed-height time
   transport retains the genuine common phase and the mixed multiplier
   \(\gamma_{n,t}+\gamma_n\chi_n\). Both physical transport errors
   and both Taylor remainders are added to each observation enclosure.
5. The full holomorphic \(\eta,L\eta\) interface, including reflection,
   analytic normalization and disk cutoff changes, remains intact. It
   is imported analytic input. An off-axis real-part expression is not
   used as a holomorphic extension.
6. The lower first-jet Schur quantity uses distances of the physical
   real observation intervals from zero and outward upper denominators.
   A lower endpoint exceeding one safely violates the necessary genuine
   candidate condition. Both earlier rectangular candidate tolerances
   are also explicitly retained.
7. Exact closed-cell adjacency, both endpoints and total height width
   eight are verified for each rectangle. Every leaf covers its whole
   exact closed time interval; no sample-only argument establishes
   coverage.
8. Connected unpruned bands independently have opposite all-time paid
   endpoint signs and one nonzero fully paid derivative sign throughout.
   Strict monotonicity gives exactly one zero per band, while the
   value-pruned complement excludes additional zeros.
9. \(H_t=A_tQ_t\), \(A_t>0\), transfers zeros and simplicity, with
   \(H_t'=A_tQ_t'\ne0\) at each zero. The component margin on each
   strip proves the quoted normalized joint-vector floor. The implicit
   function theorem and fixed disjoint bands give simple zero branches
   across each certified time interval.

## Preservation and independent internal replay

The new source checks the unchanged Note 4 source hash before import;
that source checks Note 3, which checks Note 2. Every hash listed in the
retained Note 4 build record still matches. A deliberate substitute Note
4 dependency was rejected for its hash mismatch before its code executed.

The computation inherits the 60-digit directed Decimal arithmetic,
enclosed pi and principal carrier, reduced trigonometric Taylor bounds,
adjacent enclosing logarithm/exponential outputs and directed-multiply
integer-power override. The rational polynomial-shift controls pass.
No ordinary binary float enters a certificate assertion.

All three fresh builds passed. A second internal agent independently
audited the source, exact domains, cutoff bounds, transport, acceptance
predicates, complete coverage and zero bands, then ran full arithmetic
replays for all three cutoffs. Each final JSON was byte identical to its
retained certificate. The agent also read Note 5 and confirmed that the
Schur redundancy and limited current conclusions are stated honestly.
These checks are internal and do not replace independent mathematical
review or formal verification.

Each new certificate is below 101 KB and needs no external archive.
The build record binds the new source, preserved dependencies and three
certificates. Hashes identify the files; arithmetic decides their signs
and complete coverage. The remaining research obligation is a signed
estimate uniform in a specified cutoff or shrinking-time family, or a
complete paid threshold-jet implication. Three finite local successes
do not provide that theorem or an RH conclusion.
