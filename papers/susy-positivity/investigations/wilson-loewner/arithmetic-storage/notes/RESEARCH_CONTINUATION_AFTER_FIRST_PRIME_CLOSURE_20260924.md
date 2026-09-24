# Continuation after the first-prime closure (second arithmetic-storage session)

24 September 2026. Prepared for Edward Baker by Claude (Anthropic): session configured as
`claude-fable-5-1`, runtime-reported serving model Claude Opus 5.5 (`claude-opus-5-5`); the
serving model may differ. Reasoning effort not exposed. This supersedes the
[first handoff](RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_INPUTS_20260924.md), which is preserved.

```
Continue the arithmetic-storage investigation in the shifted-zeta-positivity repo:
papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage.
Two sessions have run (GPT-6 Codex, then Claude). The second session's files are
NOT committed. Ask me before any git operation.

READ FIRST:
  arithmetic-storage/README.md                                         - status
  notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md - sections 0, 1, 3, 5
  reviews/review_claude_first_prime_session_20260924.md                - verdict, sections 5-6

WHERE THINGS STAND.
  - Lemma A: for coercive local forms, kappa_0 <= kappa <=> Q_{0,R} >= (1-kappa)(Q_L + Q_h).
    Every append hypothesis is a joined-window central inequality (relative form);
    contraction of the joined transfer follows directly (weil-depth Prop. "central
    coercivity implies contraction"). The energy-transfer lemma adds only a
    Schur-complement margin.
  - First-prime append CLOSED (internal, weil-depth builder unchanged, both
    implementations): Q_{0,3/4} >= (123/250000) I; kappa_0 <= 0.99980037; normalized
    coupling <= 0.99981859 at omega = 1/1000; ||V_{w,3/4}|| <= exp(-w/5000), w <= 1/50.
    The 0.999 intermediate target is NOT reached (it would need a relative certificate);
    it is not needed.
  - Proposition 1 (unconditional): for fixed join length h, sup_L kappa_0(L,h) >= 1;
    under RH kappa_0 increases to 1 (deterministic process). Chains with SHRINKING joins
    (h_k ~ e^{-L_k}) are not excluded: that is the canonical-system regime.
  - Prime-weight rigidity (certified outer/inner bounds, N=128 heads): on (0, log 3)
    positivity fails for s >= 1 + 3.16e-6 or s <= 1 - 8.18e-5 (s = prime-2 weight /
    arithmetic value) and holds for |s-1| <= 1.1e-7; table from R = 3/4 in the note.
    Proposition 2 (under RH; an unconditional version is sketched): any
    translation-invariant perturbation with bounded continuous sign-changing symbol
    destroys positivity at a finite window (atomic spectral measure).
  - Archimedean threshold: 0.74 < R_A <= 0.745 (certified); Galerkin R_A ~ 0.743203.

OPTIONS FOR THIS SESSION (ask me which; do not start a new finite-append certificate):
  B1. Semilocal Sonin residual. Re-derive the first-prime identity from Connes-Consani
      (arXiv:2006.13771) and the semilocal Sonin paper (arXiv:2310.18423) - the
      14 September derivation is outside the repository - then evaluate the residual
      Delta_2 on the weak directions behind Table 2 (even ground state near t = 0,
      odd state near t = pi/log 2). The residual must be controlled at the lambda_min
      scale (~5e-8 absolute near log 3).
  C1. Canonical systems. Compare the omega-string Hamiltonian at small omega with the
      prime impulses at log 2 and log 3; ask whether an infinitesimal-append chain with
      a FIXED relative margin exists (the regime Proposition 1 leaves open) and whether
      Hamiltonian positivity has a local arithmetic explanation.
  D.  Close this folder; fold B1 into the Sonin work and C1 into the shifted-zeta
      canonical-system papers.
  Small items in any case: annotate the two earlier framings (critical-path certificate
  note, cross-program assessment) with a pointer to Lemma A; write out the unconditional
  version of Proposition 2 if wanted.

DO NOT: run further finite-append certificates (log 3, log 4, log 6 joins are covered
by weil-depth directly); treat Table 2 or any finite certificate as progress toward an
all-depth statement; state Proposition 2 without "translation-invariant, bounded
continuous symbol"; call the same-assistant referee pass a specialist review.

TRAPS.
  - The 40-digit first-session record hash embeds the Python version: the committed
    record is 3caf68b7..., a replay differs; compare the 'checks' sections instead.
  - Trial weights for outer bounds must lie beyond the floating edge by more than the
    ball radius; --auto uses 2% of the margin, which certified at every R tried.
  - Round certified inner half-widths DOWN and outer c-intervals OUTWARD when quoting.
  - kappa_0 is nondecreasing in both L and h: statements about "no uniform margin"
    need "join lengths bounded below".
  - weil-depth's --horizon accepts a rational string; independent_arb.py wants a
    decimal string such as 0.75.

STANDARDS as before: classify every statement (proof / internal computer-assisted /
floating / heuristic); python-flint or standard library for certificates; small records
under numerics/records; model line at the top of every file; READMEs and CHANGELOG in
the same pass; end with a continuation note.
```

## State at handoff

Added this session, not committed:

- the research note [FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md](FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md);
- the review [../reviews/review_claude_first_prime_session_20260924.md](../reviews/review_claude_first_prime_session_20260924.md), with a new `reviews/README.md`;
- four programs under `../numerics/`: three Arb certificates importing the weil-depth builder, and one floating cross-check;
- eleven small records under `../numerics/records/`;
- this continuation;
- updates to the arithmetic-storage READMEs, the Wilson–Loewner README, and the root CHANGELOG.

No first-session file was changed except the README index entries. No weil-depth file was
changed.
