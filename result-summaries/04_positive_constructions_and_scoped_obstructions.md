# Positive constructions and scoped obstructions (SUSY-positivity, earlier packages)

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

These packages were moved to `investigations/previous/` on 20 September
2026 as "outside the current research focus", explicitly "not disproved,
completed, or scientifically obsolete". What they established:

- **Small-window full factor.** For \(0<L\le\tfrac14\), \(0\le\omega\le\tfrac12\),
  the full shifted form (prime-free there) is an explicit sum of positive
  energies with potential floor \(c^*>0.099\). A worked full-normalization
  control.
- **Positive gamma kinetic realizations.** The tower
  \(K[f]=\inf\sum_kE_{a_k}[f,u_k]\), \(a_k=2k+\tfrac12\); a relative Hilbert
  complex whose harmonic class reproduces the gamma pairing including the
  contact; the exact prime-loop identity \(Y^*Y=W^*(I-r^2T^*T)W\).
- **Odd gamma factor.** An explicit cubic gives
  \(Q^\gamma_{0,L}\ge\tfrac1{100}\|f\|^2\) on odd \(f\) for \(L\le7/10\)
  (the full Weil form only for \(L\le\log2\)); round 4 extends it to
  \(0\le\omega\le\tfrac12\) with floor \(1/200\) and bounds even mean-zero
  inputs by \(11/100\) with one scalar unevaluated. Exact rational interval
  cover (1980 cells).
- **Certified first-prime witness** at \(L=1\), \(f=\sqrt{12}\,x\): gamma in
  \([-0.137027,-0.128850]\), full form in \([0.268205,0.276382]\),
  independent-edge remainder in \([-0.598903,-0.590726]\).
- **Scoped factor obstructions.** \(Q^\gamma_{0,2/3}\) has no positive
  pairwise factor, hidden-node Schur elimination keeps the restriction, and
  there is no closable whole-line \(L^2\) factor.
- **Gamma boundary representation.** \(T_L=b(H_N)+K_L\) with \(K_L\ge0\)
  bounded, \(\|K_L\|_{\rm ess}=\pi/2\), explicit columns and finite-input
  tails; \(b(H_N)\le T_L\le b(H_D)\).
- **Exact Schur localization.** \(Q_L\ge0\iff S_{L,N}\succeq0\) with
  \(H\ge\delta_0I\) unconditional (at \(L=1\): \(N=4\), \(\delta_0=1/16\)),
  convergent two-sided enclosures, \(\log\log N_{\min}=L/2+O(\log L)\).
- **Smooth-density obstruction.** Replacing primes by \(e^r\,dr\) while
  keeping gamma, contact and poles gives
  \(Q_2^{\rm dens}[\cos(\pi x/2)]<-2979/6125\): a negative control any
  mechanism must fail.
- **Spectral form and rigidity.** \(Q_L=\sum_\rho\hat F(\gamma_\rho)\overline{\hat F(\bar\gamma_\rho)}\);
  an \(L\)-compatible realization is evaluation at the zeros; every source
  carries the reflection involution; a single-\(L\) realization is vacuous.
- **Two-channel interference exclusion.** No \(G,S\) with
  \(\|Gf\|^2=K\), \(\|Sf\|^2=\sum_pB_p\) and \(\|(G\pm S)f\|^2=Q_L\) at
  \(L=1,\,5/4\) or large \(L\).
- **Subtraction form.** \(Q_L=A_L-\sum_p\tilde B_p\) with \(A_L\) free of
  prime translations and \(A_L\ge0\) for \(L\ge\log7\); below \(\log2\) it is
  Yoshida's theorem; the window \(\log2<L<\log7\) is open.
- **Density identity, jump form, necessary condition.**
  \(b(\tau^2)+w_0=2\theta'(\tau)\); the target minus its pole term is one
  Lévy jump form with prime atoms; \(Q_L\ge0\Rightarrow\alpha_L\le2\sinh(L/2)+L\),
  a cheap disproof test.

## Status

Analytic proofs with replayed floating or exact-rational checks; operator
domains "await specialist review"; reviews are internal (the inverse-bulk
review was cross-model). The finite-response conjecture is unproved and
RH-equivalent; its arXiv submission was deferred on 14 September.

## Caveats

Every completion tested left an infinite-rank or signed residual, and
"positivity of the auxiliary source does not remove that error". Several
exclusions were later narrowed (the v0.4 ghost-pair requirement and the
"unreachable" remark were withdrawn in v0.5); the
[exclusion map](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/notes/EXCLUSION_MAP_20260917.md)
is the authoritative scope statement.

## Reusable for

The positive source side and the exact prime-return bookkeeping; the odd
sector as a control (Yoshida's odd criterion); the Schur localization as an
exact finite reformulation; the smooth-density and two-channel results as
negative controls for any new mechanism.

## Where

- [Program README](../papers/weil-positivity/susy-positivity/README.md), [PROGRAM_OVERVIEW](../papers/weil-positivity/susy-positivity/PROGRAM_OVERVIEW.md), [brainstorm assessment](../papers/weil-positivity/susy-positivity/brainstorm/ASSESSMENT.md), [relocation record](../papers/weil-positivity/susy-positivity/archive/REORGANIZATION_20260920.md), [previous packages index](../papers/weil-positivity/susy-positivity/investigations/previous/README.md).
- Positive factorizations: [manuscript](../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/manuscript.tex), [STATUS](../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/STATUS.md), [round-4 review](../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/archive/progress-reports/REVIEW_round4_20260911.md).
- Topological bulk: [manuscript](../papers/weil-positivity/susy-positivity/investigations/previous/topological-susy-bulk/manuscript.tex), [STATUS](../papers/weil-positivity/susy-positivity/investigations/previous/topological-susy-bulk/STATUS.md).
- Ground-state geometry: [STATUS](../papers/weil-positivity/susy-positivity/investigations/previous/arithmetic-ground-state-geometry/STATUS.md), [note 20](../papers/weil-positivity/susy-positivity/investigations/previous/arithmetic-ground-state-geometry/notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md), [outlook with the smooth-density theorem](../papers/weil-positivity/susy-positivity/investigations/previous/arithmetic-ground-state-geometry/sections/15_outlook.tex).
- Finite response: [manuscript](../papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/manuscript.tex), [review](../papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/reviews/review_claude_20260914.md), [assessment with withdrawals](../papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/reviews/assessment_claude_current_draft_20260914.md).
- Inverse bulk: [Weil background](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/sections/02_weil_background.tex), [gluing](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/sections/07_gluing.tex), [review](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/reviews/review_claude_opus_5_20260915.md), [prime-free inequality note](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/notes/PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md).
- Source selection: [density](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/sections/03_density.tex), [jump form](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/sections/04_jump.tex), [necessary condition](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/sections/07_necessary.tex), [open directions](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/notes/OPEN_DIRECTIONS_20260916.md).
