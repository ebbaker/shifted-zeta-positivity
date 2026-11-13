# B10 manuscript readiness assessment

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Child chat0008. Actual model
and effort are unavailable. This is a separate internal audit from
the original B10 proof chat, with three contributing agents using
shared inputs. It supplies no specialist review or verified cross-model
comparison.

**Disposition.** All four requested proof groups pass from the named
published and inherited inputs. [Note31][audit] provides the derivations
and the scoped reading of the Green transfer. [Note29][proof] and
[Review15][prior] remain the original proof and same-assistant assessment.

| Claim | Assessment |
| --- | --- |
| (B10.5)–(B10.10), Mellin identity and kernel | Exact on the integer grid. Both transition widths, the positive pole residue and the \(|v|>U\) tail have uniform bounds. Spell out the floor and logarithmic derivative estimates. |
| (B10.4), (B10.11)–(B10.12), signed high modes | Theorem 4 is cumulative. Translated means keep the \(R^\theta\) error, including translates that cross zero. The real correlation bound follows by subtracting the diagonal from the nonnegative norm square. |
| (B10.13)–(B10.19), lower modes and norm split | Both convex endpoints, the \(N^2/(Uh)\) term, the Fourier complement, the cross terms, and all cutoff jumps are accounted for. State the head norm on the admissible short-window range. Cite the checked [Montgomery–Vaughan phase class][mv] to resolve the Robert author copy's inconsistent parameter list. |
| (B10.20)–(B10.22), residual mean | Uniform in block-constant \(2\le P\le\lfloor L_U^2\rfloor\). The \(17/81\) range, \(47/162\) upper margin and \(\min(7/6480,9\rho/28)\) remainder survive the full ledger and overlap. |
| Green mean and fixed-threshold proportion | Use \(R_{P_U}\) in the final Green transfer, with \(P_U=\lfloor L_U^2\rfloor\) fixed on the outer interval. The omitted-prime bound is \(O(P_U^{-3/2})=O(L_U^{-3})\) there. The displayed theorem and corollaries already state the required scope. |
| (B10.23), ancillary setup exclusion | Use the left inequality in (7.3) with \(R\ge2\) and then both caps in (7.5). This rules out retaining the original internal caps for the specified scale. |

The audited scope supports integration of the averaged theorem with its
named inputs and the clarifications above. The complete-field provider,
the Bourgain–Watt proof itself, and the inherited E06 log transfer
retain their original review scopes. Constants and onsets remain
unevaluated. The all-centers bound, full \(c\)-band, varying cutoff,
shrinking depth, time-zero and positive-threshold extensions remain
open. The [model-change return][return] gives the integration scope
and a separate future research question.

[audit]: ../notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[proof]: ../notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[prior]: 15_GNP_RS_B10_SAME_ASSISTANT_ASSESSMENT_20261112.md
[mv]: ../references/03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md
[return]: ../notes/32_GNP_RS_B10_AUDIT_RETURN_AND_MODEL_CHANGE_20261112.md
