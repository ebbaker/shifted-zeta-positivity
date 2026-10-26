# Assessment: first negative-time correction and remaining outer loss

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0003, thread `01a17626-abf5-7a90-9ba2-7a2395254aee`.

**Review type: same-model internal analytical assessment.** Two parallel
analytical checks contributed the correction/residual algebra and the
initial-data, population and stability audit. They share the model and
classical inputs; this is not cross-model or specialist independent
review. No sampling, numerical, fitting, machine-symbolic, exact-arithmetic
or interval research was executed.

Reviewed [AN03 r1][packet], [Note10][note], its [opening input manifest][inputs],
Notes03--06/08 and the relevant parent observable equations. Primary
Polymath v2 equations36--38 and Proposition6.2 were rechecked online,
including the K=1, sigma=1/2 normalization and remainder. The underlying
Arias coefficient construction remains an import through that primary
restatement. No C1 derivative/parity or coefficient-provider theorem is
assumed.

## Accepted bounded result and representation class

Accept **EC17--18** on the full frozen complex charts, with one extra
analytic unit, for `1<=T=-t<=2`: field, spatial derivatives j<=3 and
direct first time error are bounded by **`C |G(z)|X^-5/4`**, without
logarithmic loss. This improves FN5 by X^-1/2 and is the requested named
o(|G|X^-3/4). Accept actual residual and first spatial derivative
**`C |G(z)|X^-7/4`**, EC25.

Acceptance is specifically in the **fixed-order Gaussian-moment plus
bounded RS-correction-integral class**. One explicit arithmetic correction
is evaluated, all N modes remain, and the integral retains two named
initial RS coefficients and exact adjacent transfers. This is not the
excluded full unevaluated Duhamel construction. It does not complete an
integral-free correction to every part of F_N. The elementary arm formula
EC12 is an equivalent version at the theorem's stated accuracy; the
exact-gamma convention EC11 matches initial modes exactly.

Close AN03 at its bounded gain and two-scale-comparison stop rule.
HDA-A02 remains **Partial**. No manuscript integration is included in this
return; a narrow follow-up packet is prepared for that routine task.

## Mathematical checks and corrections retained

1. **Evolution and signs.** EC9's leading T-heat defect is
   `-gamma(1+4T beta^2)`. The explicit correction
   `gamma(T+2T^2 beta^2)` cancels it. EC24 retains transport, second
   derivatives, coefficient derivatives and the product r0*c. Original
   time residual is the negative of the T-heat defect. The summed bound
   uses all modes before taking the final allowance.
2. **Initial comparison is separately improved.** Keeping only leading
   RS data leaves the old X^-3/4 initial allowance; a smaller arithmetic
   residual alone cannot improve it. K=1 pays the X^-5/4 source error.
   Exact gamma modes also retain the 1/(24z) phase and slope calibration;
   their omission would leave an unpaid first-order population term.
3. **No unsupported C1 regularity.** Proposition6.2 supplies the needed
   coefficient size and remainder. It does not itself display the C1
   derivative or endpoint identities needed for an analytic frozen-C1
   short formula. The retained real-data integral avoids importing those
   properties. The exact transfer S_m-S_N is kept; no lower-order
   recurrence is substituted at the new accuracy.
4. **True solution error.** The exact real initial heat convolution is
   split at the fixed window. Cubic gamma-log and quadratic-square
   remainders cost X^-2 per mode. The cancellation of transverse
   n/height powers in EC21 is retained before the absolute Gaussian
   estimate. Summing n^-1/2 through N gives arithmetic error X^-7/4.
   The separate RS source comparison X^-5/4 dominates this bound.
5. **Full population.** EC16 bounds every fixed logarithmic moment of
   the evolved arms. The near-cutoff band still has order sqrt X modes
   and absolute weight comparable to G X^1/4. The first correction has
   absolute total O(G X^-3/4). Neither quantity is asserted to describe
   the signed field's leading term.
6. **Complex buffers and derivatives.** On T in[1,2], the complex-kernel
   factor exp(y^2/(4T)) and weighted real moments are bounded. The
   target-centered tangent polynomial depends on z: spatial derivatives
   cannot be claimed to hit only the kernel. Note10 correctly proves
   field error on the enlarged chart and uses fixed-radius Cauchy on
   the holomorphic error. Direct T differentiation hits only the kernel
   at fixed z and has bounded polynomial moments. EC27 supplies a
   separate first-time check from the proved j=2 error and residual.
7. **Tails and function class.** Intermediate true tails retain the gamma
   height exponential and polynomial height loss. Only the distant tail
   beyond X/2 uses the complete-source global bound. Artificial tangent
   polynomial tails retain the full G X^1/4 population and are Gaussian
   dominated. No exact gamma mode is extended through remote poles.
   Initial intervals/partitions are fixed, so no unrecorded cutoff
   commutator or endpoint derivative appears. No whole-line supremum
   contraction is used as chartwise relative stability.
8. **Outer conversion.** The remaining solution allowance is precisely
   `X^-5/4 exp(TL^2/16)`, whose logarithm is
   `TL^2/16-5L/4+O(1)`; residual conversion has `-7L/4`. Both allowances
   grow for every fixed T>0. This is a failure of these finite algebraic
   allowances, not an actual error lower bound or a universal no-go.
   The older logarithmically growing-order representation retains its
   stronger outer-scale accuracy and zero residual.
9. **Physical consumer.** EC30 inserts the actual residual into parent
   PE37--39 without redefining Q. The first unpaid step is a physical
   regulator-uniform weak/collar comparison for this model and H.
   Numerator bounds alone do not establish it; no simple-root collar or
   physical transfer is silently borrowed from the positive-time case.

These are analytical checks, not an execution certificate. The final
work record binds output bytes for provenance only.

## Scope and follow-through

The result is an approximation milestone, not an RH-equivalent criterion.
The [result index][results], especially heat-flow11 and controls12, and
the [avoid index][avoid], especially review05, scope07, constants08,
separate-bounds12 and imports16, govern its interpretation. Note10's
control screen names the missing canonical arithmetic/completion premise
for each family; heat evolution identities by themselves exclude none.

No extension to T>2, through-zero join, unbounded time, regulator layer,
observable campaign, numerical onset, useful runtime or independent
specialist validation is supplied. Parent **HDA-17 Partial, HDA-18 Gated
and HDA-20 unfulfilled** remain. No model change or automatic dispatch.

**Next owner: Analysis — Sol**, [AN04 r1][next]. Integrate the assessed
bounded theorem and limitations into the maintained manuscript. A short
pasteable request is in that packet. No resistant analytical bottleneck
requires Astra for this routine follow-through.

[packet]: ../research-progress/handoffs/HDA-A02-AN03.md
[note]: ../notes/10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md
[inputs]: ../notes/10_FIRST_NEGATIVE_CORRECTION_INPUTS_20261025.json
[next]: ../research-progress/handoffs/HDA-A02-AN04.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
