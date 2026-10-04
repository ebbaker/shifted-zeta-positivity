# Shifted Hermite–Biehler positivity

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Research planning and internal review; no new global exponent is proved.

Status: Exploratory; independent dominance below \(b=1\) is open.

[Project overview](../../PROJECT_OVERVIEW_20261004.md) fixes the common probe, exponent conversion,
evidence inventory and relative priority. This charter opens a program;
its missing estimate is not established.

## Exact target

Fix \(1/2<b<1\), \(E_b(z)=\xi(b-iz)\), and prove \(|E_b^\#(z)|<|E_b(z)|\) for every \(\Im z>0\). Then \(\delta=2b-1<1\).

## First deliverable and proposed mechanism

Derive the shifted theta/Euler representation or positive kernel and identify a strict diagonal positivity mechanism with full global tails/mixed terms. Recompute the archimedean phase rather than changing one Euler exponent.

## Failure criterion

Do not assume quotient analyticity or the desired strip. Semidefiniteness may hide common nonreal factors. Boundary zeros give real zeros, allowed here but forbidden in some HB definitions; use dominance directly. At \(b=1/2\), symmetry prevents strictness.

## Starting evidence

- [FINITE EULER BOUNDARY IDENTITY 20261003](../../../../investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md)
- [CLOSED SOURCE RELATIVE COMPARISON 20261003](../../../../investigations/sonin-critical-boundary/notes/CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md)
- [Lagarias, Lemma 2.1 and Section 6](https://arxiv.org/pdf/math/0601653).

## Continuation

Save dated investigation notes here; put corresponding reviews under
'reviews/07_shifted_hermite_biehler/' and numerical sources/small records under
'numerics/07_shifted_hermite_biehler/' in the prime-variance project when needed. Keep
parent evidence linked in place. Include model/effort and LLM assistance,
and distinguish reductions, conditional inputs, conjectures and diagnostics.
Require an explicit inequality/exponent budget before numerical sweeps.

The [preliminary investigation](PRELIMINARY_INVESTIGATION_20261004.md) records
the first concrete deductions and their limits. See the
[cross-program assessment](../../PROGRAM_PREFLIGHT_ASSESSMENT_20261004.md)
for the updated shortlist and targeted next investigation.
