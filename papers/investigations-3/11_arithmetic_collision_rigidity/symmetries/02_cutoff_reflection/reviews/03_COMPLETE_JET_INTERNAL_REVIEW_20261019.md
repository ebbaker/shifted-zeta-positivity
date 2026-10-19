# S02-T2 complete evaluated jets: separate internal review

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewing model **gpt-6.1-sol (Codex), actual reasoning effort ultra**, inherited from the coordinating research turn. Separate delegated same-model mathematical and numerical review; **no independent specialist human review**.

**Disposition.** The staged complete-jet evaluator passes this mathematical/code audit and a fresh 192-bit replay. Its frozen local jets, corrected diagonal propagation, joint real Schur residual cover and physical signed forms are valid under the imported S02 disk-error theorem. Both frozen and full formulas validate the already covered B pilot. The full coherent formula has the stronger evaluated first-jet lower bound on this fixed cover despite its slightly larger residual allowance. The freshly acquired complete-source reference is stronger than both. This is a completed evaluation and a scoped no-advantage result against the strongest applicable source-informed reference, with a useful local-jet/S03 interface; it is not new coverage, a matched-cost result or a new Newman bound.

## Reviewed inputs and independent replay

The reviewed producer is `numerics/evaluate_complete_frozen_jets.py` in the S02 lane, staged at `/private/tmp/s02-jets-20261019/evaluate_complete_frozen_jets.py`. Its SHA-256 is `461ee502434f519a082ff212a0c2b5a0512c3426ef081f2ee2d82b4f5d4ce1b9`. The reviewer read the repository instructions, [result-summary index](../../../../../../result-summaries/README.md), [avoid index](../../../../../../avoid/README.md), S02 matched Note 02 and comparison contract, the S02-T2 evaluation contract, both S03 notes, and the complete-source evaluator. The relevant standing patterns are [normalization](../../../../../../avoid/08_normalization_and_constant_slips.md), [preserving cancellation](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped conclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The independent process rebuilt the complete-source midpoint setup and reran all 4096 closed cells at 192 bits, using the final staged producer without sharing root's source setup. The resulting small record is `S02_COMPLETE_JET_REVIEW_REPLAY_192_20261019.json`. It agrees exactly with the root 192-bit run in both methods' aggregate results, all 32 slab ledgers, all exact checks and the complete canonical cell-content hash:

`9e73d866c3a25ac79d9d6fd18f17e24c787aa2fa862bd155feffc99685829842`.

The source-reference setup time differs, as expected; all other source-reference summary fields agree. This hash identifies replayed data and is not a mathematical proof by itself. The stored compressed-file hash is allowed to differ because its header includes observed acquisition timing. The archive loader verifies the stored hash, canonical cell-content hash, producer/source pins, precision, count and cell order before exposing data.

The root 256-bit run repeats the positive gates on the unchanged cover. Some conservative scalar lower bounds differ slightly with precision, so the record should not claim that every displayed 192/256-bit enclosure overlaps. The independently rebuilt 192-bit mathematical cell content agrees exactly.

## Frozen derivative semantics and propagation

For fixed real center X write `q=B_t exp(-kX)/A(X)`, `c=q J(X)`, `u=q J'(X)`, `h=k+b`, with `b=(log A)_x` and `k=pi/8`. The local analytic frozen correction holds X fixed during z differentiation. Its normalized jets satisfy

\[
 f_{fr,0}=g_0-c,\qquad
 f_{fr,1}=g_1+hc,\qquad
 f_{fr,2}=g_2-(h^2-b')c.
\]

Their diagonal center-family derivatives are instead

\[
 \partial_Xf_{fr,0}=f_{fr,1}-u,\qquad
 \partial_Xf_{fr,1}=f_{fr,2}+hu.
\]

Consequently, for `Wfr=f0-i f1/omega` and the local algebraic expression `Rloc=f0+f2/omega^2-omega_x f1/omega^3`,

\[
 \partial_XW_{fr}=i\omega(W_{fr}-R_{loc})-u(1+ih/\omega).
\]

The evaluator pays this last term in its whole-cell midpoint propagation. Its sign is correct. Omitting it would incorrectly apply the coherent S03 propagation identity to a varying-center family. The full formula has no such diagonal defect. Closed-cell interval evaluation already includes time variation, and the phase recentering uses the actual omega derivative at fixed time. The exact-series comparisons at 999, 1000 and 1001 check both local jet formulas and both diagonal defects.

## Why the joint Schur cover contains every residual jet

At each real center let `eta>0`, `R=1/2`, and

\[
 H(\zeta)=r(X+R\zeta)/\eta.
\]

The imported disk contract and real symmetry make H an analytic unit-disk map with real Taylor coefficients. Put `a=H(0)`. If `|a|=1`, the maximum-modulus principle forces H to be constant, and the formulas below give zero first and second coefficients. Otherwise Schwarz's lemma applied after the disk automorphism gives the Schur map

\[
 G(\zeta)=\frac{H(\zeta)-a}{\zeta(1-aH(\zeta))},\qquad |G|\le1.
\]

Put `beta=G(0)`, which is real. A second Schwarz step yields `G'(0)=(1-beta^2)gamma`, with real `gamma in [-1,1]`. If `|beta|=1`, G is constant and the same expression gives zero derivative. Inverting the first step,

\[
 H(\zeta)=\frac{a+\zeta G(\zeta)}{1+a\zeta G(\zeta)},
\]

and comparing coefficients gives

\[
 H_0=a,\quad H_1=(1-a^2)\beta,\quad
 H_2=(1-a^2)\{(1-\beta^2)\gamma-a\beta^2\}.
\]

Thus every allowable residual jet is included in

\[
 (r,r_x,r_{xx})=
 \bigl(\eta a,\ 2\eta(1-a^2)\beta,
 8\eta(1-a^2)\{(1-\beta^2)\gamma-a\beta^2\}\bigr),
\]

for `(a,beta,gamma) in [-1,1]^3`. The factor 8 includes the second-derivative factorial. The fixed 8 by 8 closed rational cover of a and beta, with gamma left as the entire interval [-1,1], covers this cube including all boundaries. Outward interval arithmetic may widen the image but cannot exclude an admissible residual jet. The signed physical tests evaluate the complete nonlinear expressions on these images; they do not assert three independent derivative errors. The separate box branch remains a valid, weaker comparison.

The division-free first-jet Schur rejection test is also correct: if a true first-jet zero existed, the approximant would necessarily satisfy `f0^2+R eta |f1|<=eta^2`. A strictly positive lower bound for the opposite difference excludes that event. The four exact analytic-disk event fixtures challenge the actual acceptance functions and are rejected. Source-specific controls are a separate required evidence lane; this review does not replace their replay or import theta error constants into altered sources.

## Physical return and comparator findings

The exact return is

\[
 (H,H_x,H_{xx})/A=(Q,Q_x+bQ,Q_{xx}+2bQ_x+(b^2+b')Q).
\]

The implemented normalized energy and Laguerre forms are therefore

\[
 E/A^2=Q^2+(Q_x+bQ)^2,\qquad
 L/A^2=Q_x^2-QQ_{xx}-b'Q^2.
\]

In particular, the sign of `-b'Q^2` is correct. The fresh source return uses `Qxx=chi*(Vxx-2b Vx+(b^2-b')V)` for `V=H/Gc`, `chi=Gc/A`, also with the correct sign. The source enclosures already include their quadrature, Taylor, omitted-mode and source-tail costs, so their direct radius is not charged those errors a second time. The separately printed source uncertainty is diagnostic, and phase/normalizer interval uncertainty is present in the actual returned enclosures.

At 192 bits the frozen/full paid phase-first-jet lower bounds exceed 0.9686625938 and 0.9702739184, with respective residual allowances below 0.413732966 and 0.413734640. Thus selecting frozen by a smaller disk residual does not make it the stronger evaluated consumer. Both methods' joint Schur Laguerre and `L-E/100` tests pass all 4096 old-pilot cells; the frozen normalized excess lower bound exceeds 0.2747031086 and the full lower bound exceeds 0.2780996132. The box tests alone certify fewer cells, as expected from discarded residual correlation.

The freshly rebuilt complete-source comparison on the same cover gives a phase-first-jet radius above 1.3473946960, phase uncertainty below 2.349e-10, and normalized signed excess above 3.0153583623. It is stronger than both analytic candidates and must remain the primary accuracy limitation. The older analytic-only reference above 0.967290 and source-informed reference above 1.336516 are useful historical references with different information levels; the fresh source comparison is the stronger current result on the frozen domain and geometry. No acquisition or consumer timing advantage was selected or established.

For S03 retain the full coherent analytic expression and its eta_an, signed phase/normalizer derivatives, complete local jets and source pins. Exported frozen jets are valid local-disk data with their diagonal defects; they are not a shared analytic residual and must not be propagated by the unmodified heat equation. C is unactivated. Stop this bounded evaluated-jet comparison without extending the cover or claiming new collision-free cells, global control or a Newman bound.

## Final note and supplementary evidence check

The separate reader subsequently checked the installed [Note 03](../notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md), the [new acceptance-control record](../numerics/S02_COMPLETE_JET_CONTROLS_20261019.json), and the [archive check record](../numerics/S02_JET_ARCHIVE_CHECKS_20261019.json). The note's Schur proof, local derivative semantics, normalized physical formulas, comparison constants and scoped stopping decision agree with this audit. Its displayed shared 192/256-bit lower bounds are valid for both retained runs, including the source normalized excess lower bound above 3.0153583623.

The supplementary control receipt records rejection of five genuine event boxes through the new first-jet and signed helpers using each source's already-paid complete jet balls and eta=0. The Euler p=41 witness is correctly treated as a separate strictly negative-Laguerre/excess witness, not a double event. Its nonzero first jet need not fail a first-jet exclusion test. Twelve exact-rational Schur fixtures cover boundary and interior coefficient normalizations; their mutation challenges detect the factorial-8 error, omitted `-a beta^2` term and collapsed gamma interval. The reported diagonal fixture has nonzero u and contains zero in both corrected identities. These records use no theta residual allowance for altered sources. The reviewer checked the receipts and their mathematical interpretation; the independent full 192-bit replay above is the computation rerun by this reader.

The archive receipt reports successful loading of all 4096 rows at each precision and rejection of wrong stored hash, wrong canonical hash, missing archive and stale producer before the first row. Positivity survives conservative numeric-string parsing. In the implementation, full hashes/count/header pins are checked before any row is exposed, while cell order is checked before yielding each individual row. This distinction should be preserved in descriptions of the loader. The supplementary evidence supplies the previously separate control/archive lanes; no mathematical blocking issue remains.
