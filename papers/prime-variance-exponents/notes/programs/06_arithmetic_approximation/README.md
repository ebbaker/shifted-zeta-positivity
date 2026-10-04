# Arithmetic approximation below the RH norm

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Research planning and internal review; no new global exponent is proved.

Status: Exploratory; two sufficient targets, no convergence result.

[Project overview](../../PROJECT_OVERVIEW_20261004.md) fixes the common probe, exponent conversion,
evidence inventory and relative priority. This charter opens a program;
its missing estimate is not established.

## Exact target

Approximate \(1\) by prepared fractional-part functions in one fixed \(L^p(0,1)\), \(1<p<2\), giving \(\delta=2/p-1\). Alternatively prove true \(H^2(\Re s>b)\) convergence of \((1-\zeta P_N)/s\) with \(P_N(1)=0\), \(1/2<b<1\).

## First deliverable and proposed mechanism

Verify Mellin/pole constraints and continuous evaluation; choose a coefficient construction with a full small-\(x\) or Hardy tail budget. Each finite \(P_N(1)=0\) already has Hardy membership for \(b>1/2\); convergence with controlled \(N\)-dependent tails is the new target. Investigate \(p\) just above one. Any proved norm convergence suffices, even logarithmic.

## Failure criterion

Finite optimization is not convergence. Integer-only restrictions at \(p<2\) need justification. A meromorphic boundary integral is not Hardy convergence; retain the pole constraint and prove full norm convergence including all tails. Power Mertens inputs make the program conditional.

## Starting evidence

- [07 weighted energy abscissa 20261003](../../../../investigations/sonin-critical-boundary/notes/selective-loss-program/07_weighted_energy_abscissa_20261003.md)
- [SIGNED MELLIN CONTINUATION 20261004](../../SIGNED_MELLIN_CONTINUATION_20261004.md)
- [Delaunay–Fricain–Mosaki–Robert, introduction pp. 1–2](https://arxiv.org/pdf/1101.1199). The Hardy sufficient criterion is a planning deduction, not a cited convergence theorem.

## Continuation

Save dated investigation notes here; put corresponding reviews under
'reviews/06_arithmetic_approximation/' and numerical sources/small records under
'numerics/06_arithmetic_approximation/' in the prime-variance project when needed. Keep
parent evidence linked in place. Include model/effort and LLM assistance,
and distinguish reductions, conditional inputs, conjectures and diagnostics.
Require an explicit inequality/exponent budget before numerical sweeps.

The [preliminary investigation](PRELIMINARY_INVESTIGATION_20261004.md) records
the first concrete deductions and their limits. See the
[cross-program assessment](../../PROGRAM_PREFLIGHT_ASSESSMENT_20261004.md)
for the updated shortlist and targeted next investigation.
