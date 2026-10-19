# S02-T1 matched correction: separate internal review

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, as recorded for this delegated reviewer. Separate same-model mathematical/code audit and 192-bit replay; no independent specialist review.

**Disposition: pass for the stated matched error-envelope comparison.** Select the frozen exponential for per-disk physical jets under this ledger. The full analytic correction does not beat the strengthened applicable frozen comparator on either declared box. This decision is scoped to the shared published residual, printed-jump matching and first-derivative continuation estimates; it is not a universal comparison of the approximants or of possible sharper methods.

## Objects, normalization and complete ledger

I read the repository [result summaries](../../../../../../result-summaries/README.md), [avoid index](../../../../../../avoid/README.md), relevant control/normalization/cancellation guidance, S02 opening note and checker, and transport Notes 20–22 before auditing the new [comparison contract](../../notes/02_S02_MATCHED_CORRECTION_COMPARISON_CONTRACT_20261019.md) and implementation. Notes 20 and 22 already supply the frozen holomorphic exponential, correlated physical derivatives and cutoff matching. Note 21 supplies an exact complete-source Hermite comparator, without the additional signed estimate needed for collision exclusion.

For natural cutoff m and frozen N=8, the exact identity

H-G8+Can8 = (H-Gm+Cpubm) + (Gm-G8)-(Cpubm-Cpub8) + (Can8-Cpub8)

justifies using the same printed-correction jump estimate for both methods. The frozen candidate substitutes only its own final continuation difference. The new ledger does not incorrectly identify the printed and analytically continued correction jumps. The algebra challenges distinguish them explicitly.

The chosen edge payment is 2 P_* (exp(Lambda_edge)-1), with the exact opening P_* bound for P/|A(z)|, both reflected channels paid, and Note 22's endpoint logarithm refinement. All spatial/time extrema are retained. Replacing the historical KZ prefactor by this smaller valid bound is a common sharpening available to both methods. The source residual likewise uses the smaller direct Corollary 6.4 payment for both. The direct Q-normalized ledger pays K once. The historical constant-A(X) theorem is shown separately and receives its additional conversion payment before being reported as a Q allowance.

Both continuation bounds use fixed N=8. The full formula pays KWR times the complex-rectangle slope bound; the frozen formula pays KWR times its real-slice bound, holding center X fixed during differentiation. The exact supremum on the real slice is bounded by that on the complex rectangle. The computed outward bounds certify strict ordering here. Real-center correction values agree exactly, while their derivatives differ; a smaller disk allowance is not a measurement of a smaller actual value error.

The closed rational covers and precision choices remain those of the opening contract. The updated code explicitly verifies the historical real formal-phase condition |p8|<21/20, checks nonzero denominators on all complex profile cells, and retains the earlier removable-point algebra checks. No uncovered removable-point cell is accepted.

## Physical derivatives and signed correlations

With b=A'/A, c=C8(t,X)/A(t,X), k=pi/8 and Q residual r, the physical leading correction vector is -c(1,-k,k^2). The normalized correction vector includes b and b'. The checked chain rule gives physical residuals (r, r'+br, r''+2br'+(b^2+b')r).

The demodulated residuals retain the signed terms r'+(b+k)r and r''+2(b+k)r'+((b+k)^2+b')r. Thus the frozen exponential is annihilated before the remaining errors are bounded. The code does not replace b+k by the larger triangle bound |b|+k. These correlations are available source information, not independent derivative-error boxes or a proof of a signed stationary margin.

## Replay and quantitative decision

I ran the final checker independently at 192 bits with python-flint 0.9.0 and compared all decisive ledger, slope, physical-return and demodulation fields against the retained 192-bit execution. They agree exactly as serialized; source and script pins also agree. The primary record additionally contains the retained 256-bit execution and its precision-comparison checks.

| Box | Frozen eta | Full analytic with same edge | Original full analytic eta |
| --- | ---: | ---: | ---: |
| B | 0.226298330166466848 | 0.226299245883866349 | 0.226299245883866349 |
| C | 0.229588316575271923 | 0.229588634567030324 | 0.431777198737756708 |

The decimals describe outward quantities stored in the records. The C improvement restores already available analytic cutoff matching and other common prior estimates. It is not evidence that full analytic continuation improves on the frozen exponential. Additional point challenges of the actual ninth-mode versus printed-jump defect passed at 27 boundary/interior combinations; those checks are only branch/sign sanity checks, not a replacement for Note 22's analytic rectangle proof.

No evaluated whole-cell physical jet enclosure, positive physical margin, new collision-exclusion region, speed gain, Newman bound or global theta/RH claim is supplied. The frozen expression is a family of analytic disk approximants; its diagonal center-value function must not be differentiated as though the center parameter were frozen, and the family must not be propagated as a heat solution. Keeping the full analytic expression for a consumer that explicitly requires one analytic residual across the whole box remains appropriate.

## Reviewed identities and record pins

The source hash map in both records pins the S02 opening note/checker, comparison contract, exterior section, transport Notes 20–22 and historical cutoff-matching checker. I verified that the independent replay and retained record use identical maps. The hashes below identify the exact reviewed bytes; they do not themselves validate mathematical claims.

| Artifact | SHA-256 |
| --- | --- |
| [compare_correction_representations.py](../numerics/compare_correction_representations.py) | `dd92df737bd7023fb6f7c6bb40d69e7a85b46b8fccb96962db4a532227b9c63b` |
| [S02_MATCHED_CORRECTION_20261019.json](../numerics/S02_MATCHED_CORRECTION_20261019.json) | `7646611c3dae320e18364f9548b036ed08b1729d53a2fdafa837a1e5f838b688` |
| [S02_MATCHED_REVIEW_REPLAY_192_20261019.json](../numerics/S02_MATCHED_REVIEW_REPLAY_192_20261019.json) | `355b1a17345ba8bd8ec8dd9bb133a58951148764bb993d9733511e0dc89774cf` |

Key source pins, with the remaining exact paths and hashes in the records:

- `02_S02_MATCHED_CORRECTION_COMPARISON_CONTRACT_20261019.md`: `791099c469158e4be80b678b05c3b6cc3fdf9be62065a0e41614f3398c3a2a6e`.
- `20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md`: `b541c85fbfa58223c42a052ea6f8e1134a894042dc008f8a42cb810214a30ac6`.
- `22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md`: `f3518e4e6469df48713c6fa5db7618806cf5ad273183c6d518cb5b67c19fb410`.
- `check_theta_cutoff_matching.py`: `b7707547a4997e1ebf224cbbfc669f6deb2cb5f598cec0d00827f02a6f34e954`.

No unresolved blocking finding remains. The initially requested explicit historical formal-phase guard was added and included in this final replay.
