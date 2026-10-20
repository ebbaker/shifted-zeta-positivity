# Review of the first analytical round

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from the parent session metadata. Two separate same-model agents
reviewed the consolidated analysis, each checking substantial material
outside its original derivation. This is internal LLM review, not
independent specialist or cross-model review.

**Verdict: no substantive mathematical error found after two wording
corrections. The result is a conditional structural advance and scoped
estimating failures; no theta multiple zero is excluded.**

Reviewed [Note 01][n1] and [Note 02][n2] against the [program][program],
[BW09 manuscript][bw09], [result index][results], [control catalogue][controls]
and [avoid index][avoid]. The latter's reformulation, control-premise,
scoped-exclusion and checked-import rules remain operative.

1. **Finite walls.** The compact-time entire-growth bound, even product,
   real-axis decay, and infinitely many zeros justify enumeration. Local
   persistence of each finite rank gives analytic continuation for all
   positive times and boundedness on every compact time interval. The
   proof does not assume time-zero simplicity or uniform root separation.
   This discharges the finite-wall subtask under RH.

2. **Phase accounting.** The logarithmic derivative has strictly negative
   derivative between zeros. Exact endpoint arctangents give middle phase
   equal to endpoint deficit and outer baseline `(m-1)pi`. The weak
   boundary atom `(m-1)pi delta_a` is retained; filling in a removable
   density does not make the jet nonzero. No surplus follows.

3. **Poisson arithmetic.** Pairing removes the possible real constant;
   the heat/zeta ordinate factor two is correct. The control contribution
   is `delta log(p) coth(delta log(p)/2)>2`. The conductor and changed
   Euler coefficients are both paid. The elementary digamma remainder
   and uniform absolute-envelope lower bound check. The exact fixed-width
   obstruction is correctly confined to an un-deflated one-point test.

4. **Finite-prime continuation.** The squared-sinc test meets
   [Goldston–Gonek Lemma 1](https://arxiv.org/pdf/math/0511092)'s
   analytic-strip and quadratic-decay hypotheses. The Fourier convention,
   both pole terms, gamma integral, and `1/(pi Delta)` prime coefficient
   check. The gamma error is uniform even for arbitrarily growing
   bandwidth. The decreasing-weight PNT calculation gives the claimed
   prime payment, including its vanishing endpoint weight. Splitting the
   bandwidth range proves the optimized envelope
   `(1/2+o(1)) log(gamma)/log log(gamma)`. This is a statement about the
   declared absolute-value envelope, not a lower bound on the exact signed
   test at simple zeros. The finite control sum agrees with the added
   double-zero lattice, including `0<N<1` and equality at integer `N`.

5. **Gaussian comparison.** Independent expansion verifies both source
   kernel signs and the Hermite coefficients `2s^3/3`, `2s^4/3`. The mirror
   double root supplies `S>=1/(2a^2)`; minimizing the first two terms gives
   `D_s>=6s^4 h2^2/a^4` for `s<=a^2/4`. The Euler control contributes
   `b_p^2/6` to its deflated curvature and obeys the same positive-sign
   conclusion. The matched direct comparison is confined to separate
   remainder payment and asserts no wider computational dominance.

Two review edits were incorporated: the finite-prime controls are said to
have **no supplied all-real endpoint**, rather than an asserted absence;
and the elementary definition of `A(sigma,gamma)` is explicitly extended
before its use inside the critical strip. Its Euler-series identity is
still restricted to `sigma>1`.

Primary imports were checked directly: Goldston–Gonek equation (4),
Lemma 1 and Corollary 1; [Polymath's normalization and splitting](https://arxiv.org/html/1904.12438v2);
and [the classical PNT in Chebyshev form](https://dlmf.nist.gov/25.16.E3).
No claim of novelty or current-best multiplicity constant is made.

The frozen [exact algebra contract][contract] passed all **265 rational
fixtures**: 11 heat monomials, nine double-event fixtures, and 245 finite
control sums (88 integer equality cases). The [record][replay] includes
script and contract hashes. This is a finite algebra check, not interval
certification of theta data or validation of the infinite asymptotics.

**Disposition:** record RHS-02 as attempted with exact discriminators and
scoped failures, while its opposing-estimate gate remains open. Record
RHS-03's finite-wall subtask as proved under RH, not its surplus. RHS-04
has no new event exclusion coverage. This review completes assessment of
the bounded round only; the complete RH-to-simplicity argument remains
unproved and cannot be marked reviewed as a theorem.

[n1]: ../notes/01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md
[n2]: ../notes/02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[contract]: ../numerics/EXACT_ALGEBRA_CONTRACT_20261020.md
[replay]: ../numerics/EXACT_ALGEBRA_REPLAY_20261020.json
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
