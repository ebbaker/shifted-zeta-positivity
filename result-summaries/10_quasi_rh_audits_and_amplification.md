# Quasi-RH: what the preprints proved versus claimed, the audits, and amplification

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

- **The imported strip and its audit.** The 5 October preprint claims
  \(\operatorname{Re}s>11/12\) for every Hecke \(L\)-function over
  \(\mathbb Q(\sqrt{-3})\), hence for zeta; the saving comes from the
  quadratic large sieve plus a two-Poisson transfer, and the exponent from
  coherent sixth-power rows ("the legitimate extraction mechanism"). Its
  main-theorem chain received "a complete scoped internal source audit"
  that closes "under their identified classical inputs" with "No additional
  unresolved defect". Not covered: the Patterson cubic theta proof, the
  corollaries, and stronger strips.
- **Formal replay.** The Lean comparator accepted zeta, Dirichlet and
  \(\mathbb Q(\sqrt{-3})\) Hecke nonvanishing for \(\operatorname{Re}s>7/8\)
  using only `propext`, `Quot.sound` and `Classical.choice`; the three
  acceptances "check three statements derived from one shared proof" and
  are not three independent proofs.
- **Short-family finite extraction (conditional).** One fixed-character
  bound \(\mathfrak M(D,D^h)\ll D^{h+a+\varepsilon}\) gives
  \(A(D)\ll D^{(1+a)/2+5h/12+\varepsilon}\) with no initial strip; the same
  manuscript proves the generic sieve yields only exponent 1 and that block
  energy \(D^{16/15}\) exceeds the \(D^{4/5}\) budget (small-cofactor
  obstruction).
- **Character amplification (conditional, superseded).** Assuming the
  family baseline \(\beta^*\le7/8\) and four imported September lemmas, no
  Hecke zero has \(\operatorname{Re}s>20999/24000\); the parameter family
  stalls at \(0.8749572006\), which the priority review identifies as the
  real optimum, and the candidate is superseded by Liu
  (arXiv:2610.12234, \(B_{\rm new}\approx0.8749570698\), proved with Lean).
  The conductor-localized mixed moment (margin \(1/6250\)) and "the exact
  open input" (a \(1/5000\) saving) are the manuscript's own statements.
- **Headlines.** The exponent-descent README says the work "does not prove
  quasi-RH implies RH, a new zero-free strip, or the required arithmetic
  contraction"; the honest headline of the short-family step is
  "(H2) ⇒ 33/41", not "11/12 ⇒ 33/41".

## Status

Claimed-and-audited, internal only (same-model and cross-model LLM audits;
no human review). Lean acceptance is of nonvanishing statements derived
from the claimed strip, not of the strip's proof.

## Caveats

A zeta-only strip must not be substituted for a family statement; a lemma
that already assumes \(\beta^*\le7/8\) is not an independent test of it.
The amplification README still calls 20999/24000 the current candidate
and does not cite Liu. Thirty-two mixed-family notes and twenty-nine
short-family notes produced "reductions of this problem to itself".

## Reusable for

The dependency maps and ledgers (which lemma is imported from where); the
Lean comparator setup; the small-cofactor obstruction as a budget check on
any sieve route.

## Where

- Exponent descent: [README](../papers/quasi-rh-exponent-descent/README.md), [research ledger](../papers/quasi-rh-exponent-descent/notes/RESEARCH_LEDGER_20261008.md) ("Logical separation"), [strategic review](../papers/quasi-rh-exponent-descent/reviews/STRATEGIC_REVIEW_20261008.md), [comparative direction review](../papers/quasi-rh-exponent-descent/reviews/COMPARATIVE_RESEARCH_DIRECTION_REVIEW_20261009.md), [short-family reductions](../papers/quasi-rh-exponent-descent/short_families/short_family_reductions.tex), [short-family refinement review](../papers/quasi-rh-exponent-descent/reviews/SHORT_FAMILY_REFINEMENT_REVIEW_20261008.md).
- Audits: [final assembly review](../papers/investigations-2/inactive/arithmetic_source_audit/reviews/FINAL_ASSEMBLY_REVIEW_20261012.md), [dependency map](../papers/investigations-2/inactive/arithmetic_source_audit/notes/DEPENDENCY_MAP_AND_EXTRACTION_20261012.md), [cross-family review of replays](../papers/investigations-2/formal_replay_crosswalk/reviews/CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013.md).
- Amplification: [conditional theorem and ledger](../papers/quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md), [manuscript](../papers/quasi-rh-character-amplification/manuscript.tex), [priority review after audits](../papers/investigations-2/brainstorm/PRIORITY_REVIEW_AFTER_AUDITS_CLAUDE_20261012.md) §4.7; Liu's preprint is in the project files as `2610.12234v1.pdf` (not redistributed in the tree).
- The headline correction: [external review of project 17](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) §6.
