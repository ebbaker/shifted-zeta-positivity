# Internal audit of the standalone WZW manuscript

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review status:** same-assistant editorial, mathematical-scope, source and rendered-page audit. This is not independent specialist review and does not replace the detailed audits of the original calculations.

Reviewed artifact: [Boundary WZW evolution and the arithmetic Loewner source](../manuscript.pdf), with [editable source](../manuscript.tex). The [build record](../BUILD_RECORD.json) binds the delivered PDF and local sources to this review.

## Integration assessment

The manuscript is a self-contained synthesis of the two 22 September calculations. It builds entirely from local TeX files in `WZW`, without importing parent manuscript sections. Historical notes and numerical programs are linked rather than copied or moved. The parent manuscript pair, research notes, programs and recorded runs are preserved.

The main scope checks were:

1. **Boundary preparation and normalization.** The Cardy boundary sequence and vacuum OPE selection precede the positivity calculation. The tip uses the common prime-end normalization; the spectator Jacobians and moving-tip term are retained. The spin generators use the same factor-of-two convention as the pilot.
2. **The actual metric of each result.** The constant-driver identity is in the fixed invariant-tensor metric. The CS channel pairing is `diag(1,4/3)` in the raw Frobenius basis and becomes a transported metric on evaluated tensors. Neither is asserted to be the arithmetic `L2` pairing. The selected moving-driver counterexample is retained.
3. **The compactness obstruction is scoped correctly.** The raw kernel has an explicit Hilbert--Schmidt limit at initial time. The argument does not assert that every sequence of compact operators is unable to converge strongly to identity, or rule out a new sewing construction with descendants.
4. **Source-domain and time distinctions.** The arithmetic source recovery is stated where both Cayley arguments lie in the disk. Safe source translation, arithmetic shift, generalized Loewner time, physical boundary capacity and canonical depth remain distinct. The zero-shift positive-real condition is explicitly RH-equivalent.
5. **Cumulative versus instantaneous positivity.** The generator poles and exact polynomial counterexample remain visible. The Cayley Riccati equation is an identity, not an independent positivity proof. The parent causal defect equation is included with its form-domain and strong-limit qualifications.
6. **The weighted estimate retains its cost.** The safe transfer translation is at least `Omega + 1/2`. Removing the weight gives only `exp(b L)` as an upper bound, without a claim of actual exponential growth or an unweighted contraction uniform in length.
7. **Literature and novelty.** Classical Cardy/KZ, positive-real and generalized Loewner input is cited. The Lagarias correction is included. Suzuki's explicit construction at shift greater than one is kept distinct from unconditional innerness at shifts at least one-half. The existing modular-surface endpoint is not presented as new. No novel RH criterion or physical realization is claimed.

The priority change is presented as the current research assessment after both calculations: pursue a cumulative arithmetic response with a specified operator norm, keeping the WZW pilot as a physical benchmark. The earlier recommendation to extend sewing is retained as a conditional branch, not presented as the latest arithmetic priority.

## Numerical provenance

The appendix reproduces the existing 72 WZW and 60 arithmetic-source controls, totaling 11 exact rational and 121 floating cases. The record case counts, passing flags and program hashes were checked. The records and programs were not rewritten or rerun for this editorial integration. No new experiment or stronger numerical certificate is claimed.

The five-driver table, selected initial growth, prime-tail comparison and xi-linearization sample are carried over with the original qualifications. Numerical agreement does not establish the BCFT axioms, physical sewing, uniform norm control or RH.

## Build and visual review

The final PDF has **15 pages**. It compiled with no undefined references or citations, no overfull or underfull boxes, and no remaining LaTeX warnings. All pages were rendered at 110 dpi and visually inspected. The contents-page spill and a hyphenated section-heading wrap were corrected, and the changed pages were re-rendered and inspected. Unchanged page images were checked by hash after the final title adjustment.

The final inspection covered the title and author line, abstract and complete contents, boundary labels, matrix and block formulas, boxed generator and norm identities, both tables, the source and weighted-operator formulas, appendix, acknowledgements and references. No clipping, overlap, missing glyphs or broken equation labels was observed. PDF text and page-boundary checks supplement the visual inspection; they are not substitutes for it.

The author field says “Drafted for Edward Baker,” and Appendix A.3 acknowledges the substantial LLM assistance and unexposed effort setting. The package follows the no-new-snapshot policy; the live milestone is indexed in [DRAFT_HISTOR.md](../DRAFT_HISTOR.md).
