# First-slab positivity for shifted zeta canonical systems

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

For \(0<\omega\le\tfrac12\) and \(0<L\le\log2\), the shifted Weil form of
Suzuki's canonical system is positive on the first slab, by two routes that
the preprint proves and one certificate.

- **Theorem A.** \(\|V_{\omega,L}\|=\|H_{\omega,L}\|<1\), so
  \(I\pm H_{\omega,L}\succ0\): a positive archimedean base slab that
  complements Suzuki's Lemma 4.4 for \(\omega>\tfrac12\).
- **Theorem B, with Lemma 7.1 (block Schur).**
  \(Q_{\omega,L}[f]\ge c_*\|f\|^2\) on \(D_{\log}\) with
  \(c_*=6.1159\cdot10^{-4}\) (\(5.2613\cdot10^{-2}\) on the odd sector),
  for \(0\le\omega\le\tfrac12\), \(L\le\log2\); the certificate uses 256
  shift boxes per parity and 16 Legendre modes.
- **Proposition 4.2 (bounded shift difference).**
  \(Q_{\omega,L}=Q_{0,L}+C_{\omega,L}\) with an explicit Hilbert–Schmidt
  kernel \((\cosh(\omega|x-y|)-1)R(|x-y|)\), all forms sharing the domain
  \(D_{\log}\); this is the \(C_L\omega^2\) perturbation bound that the
  finite-horizon papers reuse.
- **Theorem C (shift-energy identity).**
  \(I-V^*V=2\int_0^\omega V_s^*Q_sV_s\,ds\), which turns generator
  coercivity into a Gram factor and a contraction.

## Status

Release-stage preprint v1.0, the only manuscript at that stage; no release
tag or DOI exists. In the statement ledger, Theorem A is `fs:S27` (paper),
the certificate is `fs:S18` ("computer (Arb; audited)") and the
shift-energy identity rests on `fs:S21`, whose status is "asserted" and
which the checklist calls the weakest-supported claim in the paper. The
round-2 verdict records all ten referee items resolved. Human checks are
"not yet" throughout; the originality search C2 and the normalization check
C1 against Suzuki are open.

## Caveats

The primary Arb certificate bundle is outside the public tree pending its
release gate, and the central certificate inherits tail majorants that
have not been audited (item D1). The sentence "No error survives in the
main proof chain" in the manuscript was found overstated by the 9 September
repository review; the correction reached the status files but not the
`.tex`. A 5 September clean-room audit found a float-conversion issue in
the audit code, recorded only in a chat log; see
[`avoid/19`](../avoid/19_status_files_that_lag_the_findings.md). The second
slab is not a perturbation of this one (see [02](02_finite_horizon_certificates.md)).

## Reusable for

A positive base slab for any argument that starts at small support; the
block-Schur glue (`fs:S19`, rated an easy formalization target); the
\(\omega^2\) perturbation bound.

## Where

- Manuscript: [`first_slab_positivity.tex`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/first_slab_positivity.tex) (§1.3 Theorem A, §7 Theorem B and Lemma 7.1, Proposition 4.2, §8 Theorem C); [README](../papers/weil-positivity/shifted-zeta/first-slab-positivity/README.md); [verification status](../papers/weil-positivity/shifted-zeta/first-slab-positivity/VERIFICATION_STATUS.md).
- Statement inventory: [`blueprint/first-slab/statements.md`](../blueprint/first-slab/statements.md) and the machine ledger [`statements/ledger.yaml`](../statements/ledger.yaml).
- Verification: [checklist](../verification/first-slab/CHECKLIST.md), [protocol C1/C2](../verification/first-slab/PROTOCOL_C1_C2.md), [certificate rerun](../verification/first-slab/CERTIFICATE_RERUN_20260909.md), [round-2 verdict](../verification/first-slab/reviews/REVIEW_round2_verdict_20260903.md); release gate in [`code/README.md`](../code/README.md).
- First review round (31 August): [`REVIEW_first_slab_positivity_20260831.md`](../early-chat-logs/initial-project-files/rh3/claude/REVIEW_first_slab_positivity_20260831.md).
