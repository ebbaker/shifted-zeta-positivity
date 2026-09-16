# Continuation note, 16 September 2026

**Author: Claude Opus 5 (Anthropic).** Handoff for the next session on this
investigation.

## 1. What this investigation is

A spin-off from [inverse bulk realization](../../inverse-bulk-realization/README.md).
Its object is not a construction but the **necessary conditions** a source must
satisfy, and the presentation of the target that makes them visible. It exists
because the sibling investigation's exclusions are each of the form "this
particular preparation fails", and what is wanted is conditions that kill whole
families cheaply.

It began from two brainstorm notes,
[the bottleneck note](../../../brainstorm/inverse-bulk-brainstorm/BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md)
and
[the non-constructive note](../../../brainstorm/inverse-bulk-brainstorm/NONCONSTRUCTIVE_EXISTENCE_AND_THETA_SYMBOL_20260916.md).
Their results are restated here with proofs and checks; where they conflict, this
folder is current. One conjecture of the second note is **retracted**
(see the q-Weyl note, §4).

## 2. What is established

1. **`b(tau^2) + w0 = 2 theta'(tau)`**, so the gamma energy together with the
   contact is integration against the smooth zero-counting measure
   `Nbar = theta/pi + 1`. The contact has no independent existence. Proved;
   77 checks.
2. **The symbol split**: splitting the archimedean form by the sign of its
   symbol rather than by the constant keeps the identity exact and both sides
   positive, moves strictly less to the subtracted side, and raises the one-sided
   saturation quotient by a factor of 3.9 at `L = 0.8` falling to 1 at
   `L = log 13`, above which no split is needed at all. Proved; 32295 checks.
   **It does not change the criticality.**
3. **The elementary Schur representation of Section 6.1 is the generalized
   `q`-Weyl algebra with `P(y) = 1 + y`**, so by Klyuev its twisted-trace space
   is one dimensional and the algebra carries no arithmetic parameter. All the
   arithmetic in Section 6 lives in the chosen state. Proved in exact rational
   arithmetic; 292 checks.
4. **Eight selection rules**, four of them new, collected in
   [SELECTION_RULES.md](SELECTION_RULES.md).

## 3. Next, in order

0. **Read Suzuki, arXiv:2606.09096 and arXiv:2607.24830, in full.** Manuscript
   0.5 already cites the first, but only for the normalization of the Weil
   functional in Section 2.1. It reportedly also proves, unconditionally, that
   the localized form is `<A_a v, v>` for a self-adjoint `A_a` built from a screw
   function, that the least Rayleigh quotient is continuous in `a`, and that the
   lowest eigenvalue is positive and simple — all of which bear directly on
   Section 7.6 and on selection rule 7. Cheapest item here and the most likely to
   change what we do. See [the sweep](EXISTENCE_MECHANISM_SWEEP_20260916.md), §8.

0b. **Test the Birkhoff prediction.** Compute the projective diameter `Delta_L`
   of `Pi_L`'s image in the natural cone and check whether `tanh(Delta_L/4)`
   tracks `1 - lambda_min(L)`. Doable with what is already built, and it decides
   whether the cone reading of `||Pi_L|| <= 1` is more than vocabulary. See the
   sweep, §2.

0c. **Port the spectral saturation computation into a check programme**, and
   while doing it adopt Zhu's sine-basis trial functions: our polynomial basis is
   off by hundreds of orders of magnitude (sweep, §7). It is in
   [the fixed-point note](FIXED_POINTS_AND_THE_MARGIN_20260916.md), §5, and it is
   the most consequential thing here: it measures how far the domination is from
   failing (`1e-9` at `L = 1` falling to `1e-24` at `L = 3`) and it shows that
   Section 7.6 of the sibling manuscript quotes figures its own registered check
   does not produce. It currently uses `mpmath`, which this repository's
   conventions do not allow. The port needs: arbitrary precision from `decimal`;
   spherical Bessel functions, which are elementary at half-integer order; and
   zero ordinates, either self-computed or hard-coded as labelled published input
   in the manner of `check_explicit_formula.py` in the sibling investigation.

1. **Rule 7's band-edge half also needs a check programme.** The near-null band-edge measurement is
   currently only in a brainstorm note, computed with `numpy`. Reimplement it
   under this folder's conventions (standard library only, JSON to stdout,
   preserved record, registered in `validation/drafts.py`). While doing it,
   (The `lambda_min` discrepancy is now **resolved**: the manuscript's `1.9e-7`
   is reproducible in an eight-dimensional smooth basis, its own registered
   programme gives `5.5e-4` from 40 cells, and the true value is below `1e-9`.
   See the fixed-point note, §5.)
2. **Offer the density identity and the symbol split to manuscript 0.6**, and at
   the same time **fix Section 7.6's saturation figures and their attribution**:
   they are quoted as coming from "a Fourier-Galerkin space of 41 modes" while
   the registered programme uses 40 indicator cells and produces numbers three
   orders of magnitude larger. The correction strengthens the argument. The
   density identity also retires a stated open debt (the contact "must arise by
   projection"). Keep Proposition 7.14 as the special case.
3. **Rule 4 deserves a proper statement.** The channel-spectrum reading needs the
   identification of the arithmetic coordinate that Section 3.1 declines to make.
   Either make it under an explicit hypothesis, or restate the rule purely
   spectrally so it needs no such identification.
4. **More rigidity (the highest-yield non-constructive work).** Corollary 2.2,
   Proposition 2.4 and Proposition 3.4 have done most of the work in the sibling
   investigation. Candidates for a fourth: a constraint on `q` from requiring one
   fixed `q` to serve every prime (see the q-Weyl note, §5, for a conditional
   version); a statement that any realization's compression has band edge at
   `gamma_1`, which would turn rule 7 from a measurement into a theorem.
5. **Rule 6, the infinite-prime limit.** The family exclusion is proved for
   finite sums. The infinite case is not, because `union_p (log p) Z` is dense,
   so atomic kernels can converge weakly to continuous ones — that is
   Guinand-Weil duality and it is the only route left inside that family.
   Settling it either way would be a real result.

## 4. Do not redo

- Do not look for a better additive split of `Q_L` into positive channels
  (Theorem 7.5).
- Do not use Knaster-Tarski on operator intervals (Kadison's antilattice
  theorem) and do not look for the source at a scale-invariant RG fixed point
  (the primes fix an absolute scale). Both are settled in the fixed-point note,
  §3. Fixed point theorems in general are **not** ruled out; the earlier blanket
  claim to that effect is corrected there.
- Do not revive the budget claim relating roots of `P` to primes. It is false;
  the algebra of Section 6.1 has one root, at `-1`, independent of every prime.
- Do not test candidates by matching the terms of (2.9) one at a time.

## 5. Conventions

- Notes here, with the author model named at the top of anything written by a
  language model. Reviews in [`reviews/`](../reviews/README.md).
- Check programmes are standard library only, print JSON to stdout, keep a
  preserved record under `numerics/records/`, and are registered in the `CHECKS`
  dictionary of `validation/drafts.py`. There are three.
- Everything stays under 1 MiB per file; see the repository's
  [large-file policy](../../../../../LARGE_FILES.md).
- There is no manuscript in this investigation yet. If one is started it goes in
  `manuscript.tex` with `sections/`, `drafts/` and `BUILD.md` as in the sibling
  folder, and `validation/drafts.py` grows the `record` and `save` commands.
