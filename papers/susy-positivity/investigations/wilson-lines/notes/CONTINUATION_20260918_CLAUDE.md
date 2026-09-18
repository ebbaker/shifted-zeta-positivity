# Continuation for Claude: endpoint matter and Wilson lines

18 September 2026. Prepared by OpenAI GPT-6 (Codex) for Edward Baker.

## User intent and working location

Edward wants to push the Wilson-line proposal despite earlier closure language. Continue in the existing investigation, not a new folder:

`/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-lines`

The relevant siblings are `../loewner` and `../fractional-dimension`. Edward explicitly authorized preserving the current manuscript in drafts, adding the endpoint-matter continuation, and continuing the research. He is switching to Claude for usage reasons, not changing the direction or requesting another general assessment. Proceed with concrete calculations; do not stop to ask whether to continue.

## Read these first

1. [ENDPOINT_MATTER_CONTINUATION_20260918.md](ENDPOINT_MATTER_CONTINUATION_20260918.md): free endpoint kernels, the gauge-invariant pairwise candidate, renormalization qualification, weight perturbation, and correction to the protected delay claim.
2. [ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md](ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md): semicircle supersymmetry calculation, positive-gluing problem, and full archimedean determinant identity.
3. [The 17 September review](../reviews/review_claude-fable-5-1_2026-09-17.md), then [Loewner Section 4.1](../../loewner/sections/04_realizations.tex): these already correct overly strong readings of abelianity and flatness.
4. The unchanged manuscript's [conventions](../sections/02_conventions.tex) and [generator](../sections/03_generator.tex) fix every target normalization.

Do not start with the older session prompts: their proposed next steps and some exclusion language are superseded.

## What was preserved and changed

The current manuscript is **0.8, 47 pages**, despite stale references elsewhere to 0.3. Its source, PDF, original validation script and original check records are unchanged. A fresh complete snapshot was saved as `drafts/2026-09-18-v08-endpoint-baseline/`; it is still version 0.8, not a new manuscript version. All nine snapshots passed file-identity verification. The snapshot tool has inherited generic title text; the actual saved TeX/PDF title is authoritative.

The two new research notes above, a standard-library check program, its retained record, a legacy replay audit, a separate continuation validator and `ENDPOINT_MATTER_RECORD.json` were added. The main README, notes and numerics indexes, drafts index, and `NEW_SESSION_PROMPT.md` were updated. These changes, including the baseline snapshot, are **uncommitted**. Inspect git status and preserve them. Nothing was pushed. No revised manuscript PDF was built or claimed.

## Results to carry forward

For a free dimension-one-half endpoint scalar, use a coordinate along a line **within the three-dimensional defect**, with endpoints at signed positions `±r`. This is a proposed dictionary, not the original paper's normal ray into the bulk. For `u=log(r1/r2)>0`, the weighted same-ray and opposite-ray kernels obey

\[
\frac12\left[\frac1{2\sinh(u/2)}+\frac1{2\cosh(u/2)}\right]
=\frac{e^{-u/2}}{1-e^{-2u}}=\sum_{n\ge0}e^{-(2n+1/2)u}.
\]

This is exactly the target's archimedean kernel. Its difference energy is
`Re psi(1/4+i tau/2)-psi(1/4)`. The tower was already known in the program; its endpoint interpretation is the proposed opening. This supplies neither the contact/pole pieces nor the prime atoms.

A pairwise gauge-invariant candidate uses the average of the semicircle OWLs joining `(r2,r1)` and `(-r2,r1)`, weighted by `sqrt(r1 r2)/2`. It matches the leading kernel. Individual gauge invariance does not make this a positive Gram kernel.

For planar upper semicircles with center `c`, radius `R`, one fixed scalar coupling and the displayed Euclidean bulk BPS equation, the derivation gives

\[
\epsilon_s=-c\Gamma_1\epsilon_c-iR\Gamma_I\Gamma_3\Gamma_1\epsilon_c.
\]

Writing `J=i Gamma_I Gamma_3`, two circles require `(Delta c+Delta R J)Gamma_1 epsilon_c=0`. Since `J^2=1`, distinct circles can share a bulk solution only if they share an endpoint. The two terms of the candidate share `r1`, and a fixed row passes this necessary bulk test. Varying `r1` across the full kernel leaves no common bulk supercharge in this ansatz. **Defect endpoint conditions were not solved even for the fixed row.** This is not an exclusion of varying scalar couplings, other networks, or positivity without a common supercharge.

The entire archimedean shift has an auxiliary fixed-space realization. With `H|n>=(2n+1/2)|n>` and

\[
D(p)=\det{}_\zeta((H+p)/2)=\sqrt{2\pi}/\Gamma(1/4+p/2),
\quad K^\Gamma_\omega(p)=\pi^\omega D(p+\omega)/D(p-\omega),
\]

the correct shifted Gamma ratio and its `cosh(omega u)` generator follow. The conductor factor is supplied, and no gauge-theory localization has derived this determinant. It removes the need to vary spatial dimension merely to represent this factor; it proves no contraction.

## Claims requiring care

- The new calculations are by one model and have **not received independent scientific review**. Audit the bulk BPS conventions and the physical interpretation before incorporating them into the manuscript. Finite Clifford checks are not a count of physical defect supercharges.
- The original OWL paper's endpoint normalization at one scale is not by itself an all-scale protection theorem. The elementary cutoff self-energy integral retains `log(Lambda/p)`. A local counterterm cannot remove its momentum dependence everywhere. Do not infer an anomalous dimension from that gauge-dependent diagram alone: cancellation in the full observable remains to be tested.
- The old protected zero-delay inference applies a divergent beta integral at half-integer weights. A subtracted dimension-one-half transform is a digamma difference and has nonconstant phase. This qualifies that inference; it does not supply target winding or invalidate the convergent Stieltjes theorem.
- Flatness of a connection reconstructed from a transfer is automatic. Spacetime field strength can still enter its deformation coefficient. Do not use flatness as a general no-go.
- Positivity of `theta^m` fails for the prescribed fractional lattice continuation. That does not exclude every fixed-dimensional defect theory with a continuous spectral parameter.

## Next calculation: construct the positive pairing before adding arithmetic

Choose and write one actual **common-reference or reflected-state transport network**. Specify the endpoint operators, gauge-index contractions, reflection/adjoint, and the pair of paths. Compute its free kernel and check whether the even image average survives. Pairwise semicircles generally do not factor as `T_x^dagger T_y`; for unitary transport such a factorization would force triangular holonomies to be trivial. The supersymmetric scalar connection needs separate adjoint treatment.

If using a protected family, solve the bulk and defect endpoint constraints together. A possible alternative is contour-dependent scalar couplings preserving one fixed supercharge; check that endpoint polarizations retain the required equal even weights. Existing arbitrary-contour supersymmetric *closed-loop* constructions do not automatically provide these endpoints.

Do not insist that common supersymmetry is logically necessary for every positivity mechanism. It is necessary for the proposed common cohomological/localization argument and has failed for this simplest ansatz. A reflected Hilbert-space construction could follow a different route.

After a concrete pairing survives its leading test, calculate the full first interaction correction in one local renormalization scheme. The notes give the exact effect of a shifted endpoint weight. Only then pursue a physical interpretation of omega and the determinant. Inserting a zeta ratio, a prime spectrum, or chosen prime-dependent weights by hand would not solve the arithmetic realization problem.

## Reproduction and provenance

From the investigation folder:

```sh
python3 validation/drafts.py check
python3 validation/endpoint_matter.py check --replay
```

The new **154 finite cases** pass and replay identically. All **1067 legacy cases** pass their programmed tolerances, but the original strict replay differs in five small floating-point diagnostics across two programs on this runtime. See `numerics/records/endpoint-baseline-replay-audit.json`; do not replace historical records to conceal this difference.

The separate `validation/endpoint_matter.py` contains the new registry. It binds the research notes and their checks without changing the unchanged manuscript's build record. When editing those notes, replay the checks and refresh with `python3 validation/endpoint_matter.py record --replay`. On manuscript integration, migrate the check into the manuscript registry and perform the usual build, rendered review, and provenance update. Keep files below 1 MiB, identify the model on new notes, and preserve historical drafts.

Primary sources already consulted: [Baker 1102.4948](https://arxiv.org/pdf/1102.4948), especially Sections 3.1–3.3 and Appendix C; [DLMF 25.11.18](https://dlmf.nist.gov/25.11.E18); [Dymarsky–Pestun 0911.1841](https://arxiv.org/abs/0911.1841); [Drukker et al. 0704.2237](https://arxiv.org/abs/0704.2237). The latter two were consulted for framework/direction, not fully audited as defect constructions.
