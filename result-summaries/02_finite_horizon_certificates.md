# Finite-horizon Weil certificates and continuation algebra

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

**Weil-depth (to \(\log7\)).** Two-sided enclosures
\(m_j\le\lambda_{\min}(Q_{0,L_j})\le\mu_j\) at the horizons
\(\log2,\dots,\log6\), \(9/5\) and \(\log7\). At \(\log7\),
\(1.37\cdot10^{-28}\le\lambda_{\min}\le6.81\cdot10^{-28}\), hence
\(Q_{0,L}\succeq1.37\cdot10^{-28}I\) for every \(L\le\log7\);
\(\|V_{\omega,L}\|\le\exp(-6\cdot10^{-29}\omega)\) for
\(\omega\le4\cdot10^{-15}\); the bottom of the spectrum sits in the even
sector at every horizon. The analytic tools around the certificate are
reusable on their own: the fractional tail lemma
\(\|I_\nu(I-P_N)\|\le(L/2)^\nu\sqrt{\Gamma(N+1-\nu)/\Gamma(N+1+\nu)}\) with
the infinite-tail floor, exact parity leakage, the Schur test, and the
diagonal formulation (a sequence \(L_j\to\infty\), \(\omega_j\downarrow0\)
with \(\|V\|\le1\) would imply RH).

**Storage-depth (past \(\log7\)).** At \(L_q=\tfrac34\log14\approx1.979\):
\(2.99\cdot10^{-29}\le\lambda_{\min}\le3.29\cdot10^{-29}\), residual factor
\(\theta=0.78\), contraction for \(\omega\le9\cdot10^{-16}\). At
\(L_2=\tfrac12\log56\approx2.013\):
\(1.69\cdot10^{-30}\le\lambda_{\min}\le1.89\cdot10^{-30}\), \(\theta=0.8\),
contraction for \(\omega\le2\cdot10^{-16}\). The continuation algebra: the
residual identity \(A-B^*F^{-1}B=H_J-R^*F^{-1}R\), the direct-floor lemma
(\(M_\theta\succeq m\) implies \(Q\succeq m/\tau^2\)), and a conditional
continuation theorem whose hypotheses are verified for the first two steps.

**Certified anchors (critical path, arithmetic storage).**
\(Q(0,\tfrac12)\ge I/40\); append coupling \(<0.951\);
\(Q_{0,3/4}\ge(123/250000)I\); the joined-window equivalence (Lemma A).

## Status

Weil-depth: "Full builds PASS; independent implementation PASS at all seven;
replay PASS"; working draft v0.4, not externally reviewed by a human; the
v0.2 cross-model review found no error. Storage-depth: "Certified
(R14)…(R18)", meaning guarded Arb sign tests in the "working normalization",
with the normalization audit and an independent matrix reconstruction still
open; the R18 matrices are not present locally. Anchors: "computer-assisted
fixed-window proof".

## Caveats

The floors in both papers were restated after review: round targets had
been reported as measurements, and certified floors were understated by
four orders of magnitude (see [`avoid/09`](../avoid/09_round_floors_and_fitted_laws.md)).
Finite data do not establish an asymptotic law in \(L\). The horizons carry
no information about zeros above height about 70 (record R17). Storage
induction from scalar margins fails on a \(2\times2\) example, appending
fixed 32-mode slabs fails after about five slabs, and the barrier theorem
gives \(N>\pi L\,e^{\lambda_{\max}(T_L)}\), so sharper arithmetic norm bounds
on separated complements cannot help. The second slab is not a small
correction to the first (crossings at \(L^*_{\rm odd}\approx0.743\),
\(L^*_{\rm even}\approx0.820\)).

## Reusable for

An all-input positive baseline on \([0,\log7]\) and slightly beyond; tail
closure for any Legendre-head certificate; the residual and direct-floor
lemmas for any cumulative append; the anchors as all-input baselines for
new finite tests.

## Where

- Weil-depth: [manuscript](../papers/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex) (thm:main, thm:computation, prop:upper, prop:tail, lem:parity, prop:schur, prop:diagonal); [STATUS](../papers/shifted-zeta/weil-depth/STATUS.md); [CONTINUATION](../papers/shifted-zeta/weil-depth/CONTINUATION.md); [enclosure summary](../papers/shifted-zeta/weil-depth/numerics/output/enclosure_summary.json); [v0.2 review](../papers/shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.2_claude/REVIEW_CLAUDE_20260909.md); [second-slab strategy note](../papers/shifted-zeta/weil-depth/archive/background/ARITHMETIC_DEPTH_STRATEGY_20260906.md).
- Storage-depth: [manuscript](../papers/shifted-zeta/storage-depth/manuscript/storage_depth.tex) (thm:main, thm:second, lem:residual, lem:directfloor, thm:conditional); [STATUS](../papers/shifted-zeta/storage-depth/STATUS.md); [CLAIMS.json](../papers/shifted-zeta/storage-depth/CLAIMS.json); [CLOSEOUT](../papers/shifted-zeta/storage-depth/CLOSEOUT.md); [v0.2 review](../papers/shifted-zeta/storage-depth/archive/reviews/REVIEW_storage-depth_v0.2_claude_20260910.md); [barrier theorem note](../papers/shifted-zeta/storage-depth/archive/reviews/NOTE_barrier_theorem_and_ladder_conjecture_20260911.md).
- Anchors: [EMA tower anchor](../papers/susy-positivity/investigations/critical-path/notes/EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md); [coupling certificate](../papers/susy-positivity/investigations/critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md); [first-prime join equivalence](../papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md).
- Large derived data policy: [`LARGE_FILES.md`](../LARGE_FILES.md).
