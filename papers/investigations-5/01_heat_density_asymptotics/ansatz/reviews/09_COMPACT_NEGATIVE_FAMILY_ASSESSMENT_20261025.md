# Assessment: compact-negative-time family and endpoint dependence

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0003, thread `01a17626-abf5-7a90-9ba2-7a2395254aee`.

**Review type: same-model internal analytical assessment.** Parallel
read-only checks addressed weighted kernels/tails and population/residual/
carrier estimates, then read the staged note. They share the model and
classical premises; this is not cross-model or specialist independent
validation. No numerical, machine-symbolic, fitting, sampling,
exact-arithmetic or interval research was executed.

## Disposition and precise theorem

Accept [Note12 CF26--28][note] under [AN05 r1][packet] for every declared
fixed 0<tau<=B<infinity, uniformly on tau<=T<=B and full fixed buffered
charts with an extra analytic unit:

- Field, spatial derivatives j<=3 and direct first time error:
  C(tau,B,r,b)|G|X^-5/4, with no logarithmic loss.
- Actual residual and its first spatial derivative:
  C(tau,B,r,b)|G|X^-7/4, with no logarithmic loss.
- All endpoint factors are displayed in CF7, CF11, CF15, CF16, CF22,
  CF25, with sufficient height gates CF24. Remaining constants depend
  only on fixed buffers and named classical inputs, not tau or B.

The model keeps the evaluated first gamma-curvature correction, all N
modes, K=1 RS initial data, exact adjacent transfers and a bounded
correction integral. The larger fixed window is
V_B=8 sqrt(max(1,B)) log(X/(4pi)). No endpoint-dependent order or
arithmetic mode deletion is hidden in this statement.

Close **AN05** at this fixed compact-family scope. HDA-A02 remains
**Partial**: outer-scale short formulas, integral-free simplification,
growing-time limits, through-zero assembly and physical transfer remain
open. Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.
The [opening manifest][inputs] and [work record][work] identify evidence;
hashes are provenance, not proof certificates.

## Analytical checks

1. **Canonical initial mismatch is independent of residual cancellation.**
   The K=1 real RS import still pays G X^-5/4. The exact adjacent
   transfer stays inside real initial data; no C1 derivative or cutoff
   recurrence is inferred from a size bound. No additional external
   theorem or positive-time evolved estimate is imported.
2. **Kernel constants.** CF7--8 retain exp(Y²/(4tau)), finite-B Gaussian
   moments and both inverse-time factors. The Gaussian normalization
   and binomial/Gamma moment coefficients were checked analytically.
   Direct time needs moments through six. Target-centered polynomial
   spatial derivatives are correctly handled by Cauchy, not by treating
   the kernel as the only z dependence.
3. **Full population.** The slope gate controls the beta-square
   calibration uniformly in all n and T. The shell count, W_d integral
   comparison and exponent exp((Y-1)_+²/(2tau)) pay the full growing
   population. Fixed low modes or an absolute shell bound are not
   substituted for the signed field. The corrected near-cutoff lower
   comparison now has an explicit |c|<=1/2 onset gate.
4. **Actual residual.** CF14 was independently expanded from Note10
   EC24 by hand. Every coefficient in P2/P3 agrees; all transport and
   coefficient-derivative terms remain. Original-time sign is the
   negative of the T-heat defect. The complete degree-four moment pays
   residual order X^-7/4; fixed-margin Cauchy pays residual_z. The
   retained integral has exactly zero residual, since endpoints/data
   are frozen in T and z.
5. **Tails and onsets.** The D_m and J_m normalizations, V>=32B tilt
   absorption, moderate/artificial X powers and remote Gaussian gate
   were checked. The two logarithmic gates put all tails below
   G X^-7/4, for both field and direct time. The remote gates
   X>=32pi B and X>=sqrt(256B log^+A_far) correctly absorb the lost
   gamma height exponential. Global source boundedness is used only
   beyond X/2. No analytic RS/gamma function is extended through its
   remote poles to complete the artificial polynomial.
6. **Solution error and derivatives.** Local gamma Taylor remainder
   has per-mode error X^-2. Transverse cancellation precedes absolute
   estimation, so summing all n costs X^1/4, yielding G X^-7/4.
   The separate initial G X^-5/4 remainder dominates. Fixed-radius
   Cauchy gives j<=3 without logs; direct kernel differentiation and
   the separately proved residual/PDE identity both pay time error.
   No Duhamel contraction or localization commutator is assumed.
7. **Outer conversion and limits.** CF31 re-derives the carrier on the
   full interval using its B(1+L)/X onset gate. The favorable
   exp(-pi²T/64) factor and large exp(TL²/16) loss have the correct
   signs. The resulting finite algebraic allowances still grow at
   each fixed T>0, without implying an actual error lower bound or
   universal obstruction to resummation. The displayed constants
   degenerate at tau=0 and B=infinity; no growing-time substitution
   is accepted.
8. **Overlap and physical consumer.** If [tau,B] intersects [1,2],
   comparison through the same H is made after both onsets. Different
   fixed integration windows are not identified. The old growing-order
   outer theorem keeps its existing domain. Physical PE37--39 forcing
   is named, with the regulator-uniform weak/collar and actual-Q
   transfer still unpaid. No new join is performed.

No blocking mathematical issue was found in this scoped proof. Review
prompted two minor qualifications now incorporated: a signed definition
of E1 before its modulus bound, and explicit near-cutoff/overlap onset
conditions. No prior result or frozen contract was changed.

## Scope and next owner

This is a quantitative approximation result, not an RH-equivalent
criterion. The [result index][results], especially heat-flow11 and
controls12, and the [avoid index][avoid], especially review05, scope07,
separate-bounds12, imports16 and status19, govern its interpretation.
The control-premise screen stays canonical/arithmetic and names each
failed premise; heat identities themselves exclude none.

No independent specialist review, evaluated onset, integral-free formula,
useful runtime, through-zero/growing-time theorem, regulator-layer result
or physical-transfer campaign is supplied. The maintained manuscript
has not been edited in this analytical return.

**Next owner: Analysis — Sol**, [AN06 r1][next], assessed-result manuscript
integration with the endpoint-factor/onset ledger and remaining limits.
Prepared, not dispatched. The completed endpoint/kernel bookkeeping
reveals no resistant mechanism requiring Astra for this follow-through.

[packet]: ../research-progress/handoffs/HDA-A02-AN05.md
[note]: ../notes/12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md
[inputs]: ../notes/12_COMPACT_NEGATIVE_FAMILY_INPUTS_20261025.json
[work]: ../numerics/AN05_ANALYTICAL_WORK_RECORD_20261025.json
[next]: ../research-progress/handoffs/HDA-A02-AN06.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
