# Unit-row amplification at arbitrary column scale

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Author of this research note: GPT-6 (Codex), inherited session configuration.
Exact serving variant and reasoning effort are not exposed and are not inferred.

The arbitrary-`D` mechanism needed for U3 is present in the pinned source.
`eventually_fixed_ray_amplification` is eventual in the **prime-window scale
`x`**, and then quantifies arbitrary positive `D` and arbitrary row cutoff
`U`. Applying this declaration at `U=1`, together with two applications of
`RawMoment.scaleEnergy`, gives the unit-row extraction with the expected
`11/12` exponent after choosing the raw losses. It does not require setting
`U=1` in `no_slot_endpoint`.

This pass establishes a conditional mathematical specialization of exact
source contracts. No new Lean term has been elaborated or compiled. U1's
identification of the prescribed October 5 character/exclusions remains a
condition, and U2's uniform seminorm conversion is not proved by this pass.

## Source identity and scope

The source pin is `openai/math`
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. All 16 supplied
`Hecke/InverseAmplification*.lean` files, plus `Moments/PrimePool.lean` and
`Hecke/Dyadic.lean`, match the preserved source manifest in byte length,
SHA256 and Git blob SHA1: 18 matches, no mismatches. The manifest's expected
commit is the same pin; its stored SHA256 is
`b0bd1f6b77e23bec0a78811a644114eb12dea6e55138620c82ef76a00af77c48`.
The supplied amplification bundle SHA256 is
`06cca70867ac7db95df7c90f0a262231a292cffe6bff88430a2784faca71898c`.

This is an identity check against the earlier preserved inventory, followed
by source reading. It is not an independent validation of the whole import
closure, a successful comparator result, or a kernel/axiom report.

All declarations below have prefix
`OAI.SevenEighths.HeckeInverseAmplification` unless stated otherwise. The
file paths are under `lean/OAI/NumberTheory/DirichletL/` at that pin.

## The declarations that discharge the structural obstacle

| Exact declaration | Source locator | Contract used |
| --- | --- | --- |
| `eventually_fixed_ray_amplification` | [Hecke/InverseAmplificationPrimePool.lean:41](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationPrimePool.lean#L41) | For fixed ray/prime-window data, there is `δ>0` and an eventual set of `x`, on which the estimate holds for all `data,rows,W,wa,wb,D,U,E`; `D>0`, row norm `≤U`, and raw scale energies for `W` and `scaleProfile W` are its inputs. The loss is exactly `4*(1+2*log(x*b))*E*log x/(δ*x)`. |
| `RawMoment.scaleEnergy` | [Hecke/InverseAmplificationRaw.lean:18](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationRaw.lean#L18) | From `RawMoment data W c κ C`, `c,κ,C≥0`, `D≥1`, `U*V^6≥1`, `D^(1+c)≤U*V^6`, obtain `RawScaleEnergy data W U D V (C*(U*V^6)*((U*V^6)*D)^κ)`. |
| `RawMoment` | [Hecke/InverseAmplificationRaw.lean:11](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationRaw.lean#L11) | Uniformly over `H≥1`, positive column scale `d`, and `d^(1+c)≤H`, every finite set of nonzero element rows of norm `≤H` has central inverse-polynomial square sum `≤C*H*(H*max 1 d)^κ`. |
| `RawScaleEnergy` | [Hecke/InverseAmplificationPrimePool.lean:12](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationPrimePool.lean#L12) | Controls every finite nonzero-element row set of norm `≤U*V^6` at every log scale `l∈[log D−log V,log D]`. |
| `averaged_energy` | [Hecke/InverseAmplificationAggregate.lean:35](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationAggregate.lean#L35) | For any finite sixth-free rows and prime ideals of norm `≤V`, the two raw scale energies imply `(prime count)*Σ row energies ≤4*(1+2*log V)*E`, without a relation `D=U^r`. |
| `OAI.SevenEighths.CenteredMomentPrimePool.eventually_primePool_card` | [Moments/PrimePool.lean:40](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Moments/PrimePool.lean#L40) | For fixed ray data and a nonnegative nonzero smooth compactly supported prime test, `#primePool≥δ*x/log x` eventually, with `δ>0`. |

The prime-window inputs are a nonzero ideal `M`, a subgroup
`H≤(O/M)ˣ` containing `RayOrthogonality.globalUnits M`, a fixed finite ideal
set `S`, and a real test `φ` with `ContDiff ℝ ∞ φ`, compact support,
positive topological support, nonnegative values, and `φ≠0`. They also
include `0<a≤b`, `B>0`, `support φ⊆(a,b)`, and `φ≤B`. The density constant
and threshold are chosen before `data,W,D,U,E`; retain their dependence on
this fixed data. Here `a,b` describe the prime window, while `wa,wb`
describe the column test `W`.

The underlying prime pool is exactly
`annularPrimeIdeals (RayQuotient.identityClass M H) a b x \ S`
(`Moments/PrimePool.lean:12–14`). Its ideal norms lie in the annular range
from `a*x` to `b*x`; the lower norm bound is used explicitly in the count
proof at lines 23–28. The typed pool preserves cardinality
(`typedPrimePool_card`, lines 22–31), and its precise upper bound is
`norm P≤x*b` (`typedPrimePool_norm`, lines 33–39). No new moving conductor
or growing excluded-prime set is introduced in this application.

## Direct unit-row specialization with the exact raw cutoff

Fix `data : RowData`, a smooth complex test `W` supported in
`[wa,wb]` with `wa>0`, `wb≥0`, and raw inputs

\[
\operatorname{RawMoment}(data,W,c,\kappa,C),\qquad
\operatorname{RawMoment}(data,\operatorname{scaleProfile}W,c,\kappa,C),
\]

where `c,κ,C≥0`. If the two inputs have constants `C₀,C₁`, take
`C=max(C₀,C₁)`; the raw right side is nonnegative and monotone in `C`.
These are uniform-in-scale assumptions, not bounds established only at
one selected column length.

Let `u₁` be the sixth-free element row represented by `1∈O`, take the
singleton row set `{u₁}`, and put `U=1`. Its ideal is the unit ideal,
whose normalized prime-factor multiset is empty and whose absolute norm
is one. Thus it meets the `FreeRow` and row-norm hypotheses. This routine
subtype construction and its singleton simplification remain unwritten
Lean terms; they are not silently imported from `no_slot_endpoint`.

Write

\[
q=\frac{1+c}{6}>0,\qquad V=D^q,\qquad x=\frac{D^q}{b},\qquad
N=U V^6=D^{1+c}.
\]

Take `D` sufficiently large that `D≥1` and `x` lies beyond the fixed
prime-window threshold. If that threshold is `x₀`, one admissible choice
is `X₀=max(2,x₀,1/b)` and `D≥(bX₀)^(1/q)`. This preserves the exact raw
cutoff `N=D^(1+c)` rather than hiding a multiplier in it. The prime norm
range becomes

\[
\frac a b D^q\le\mathrm N P\le D^q,
\qquad \#\mathcal P_x\ge
\frac{\delta}{b}\frac{D^q}{q\log D-\log b}.
\]

Both applications of `RawMoment.scaleEnergy` now have `D≥1`, `N≥1`,
and `D^(1+c)=N`. They give the common scale-energy bound

\[
E=C N(ND)^\kappa
  =C D^{1+c+\kappa(2+c)}.
\]

The smaller column scale `D/\mathrm N P` may fall below one for some
parameter choices; it remains positive. The lemma explicitly controls
the whole log interval using `max 1 d≤D`, so no unjustified raw-moment
restriction `d≥1` is being inserted at those smaller scales.

Set
`P₁(D)=HeckeDyadic.polynomial (data.character ⟨u₁.val,u₁.property.1⟩) true W D 0 0`.
The direct fixed-ray amplification estimate yields

\[
\boxed{
|P_1(D)|^2\le
\frac{4Cb}{\delta}
 (1+2q\log D)(q\log D-\log b)
 D^{\frac{5(1+c)}6+\kappa(2+c)}.
}
\]

This keeps the prime-window multiplier `b`, the factor `4`, the density
`δ`, and both logarithmic factors. In particular, the power of `D` is
obtained by subtracting `q` from
`1+c+κ(2+c)`; it is not inferred by inserting a unit row into an
eventual-in-`U` endpoint.

The amplification map retains actual element rows, including their unit
factor. `primeRowMap_injective` (`Aggregate:16–24`) reduces to
`rowMap_injective` (`Rows:54–70`), whose argument uses sixth-free ideal
decomposition and then cancellation of the fixed ideal generator's sixth
power. Its norm is bounded by `U*V^6` (`Aggregate:26–33`). Thus the unit
application does not replace a potentially repeated element family with
an unjustified ideal count.

## Why the extra scale profile and logarithm are legitimate

`RowData.prime_column` (`Family:46–55`) gives the exact identity

\[
P_u(D)=P_{u\,g_P^6}(D)
 -\chi_u(P)(\mathrm NP)^{-1/2}
   P_{u\,g_P^6}(D/\mathrm NP).
\]

The deleted-prime equality is proved in `RowData.amplified_prime_mask`
(`Family:35–44`), including unsupported-ideal zero terms in
`amplified_row_prime_mask` (`Mask:32–51`). The coefficient in the second
term has norm at most one (`prime_column_energy`, `Energy:18–29`), which
produces the factor two in `RowData.prime_energy` (`Family:57–65`). This
is an exact rescaled-column identity; it does not discard a residual
`O(D/x)` term.

The row-dependent smaller scale is bounded using
`exists_scale_majorant` (`ScaleSup:53–75`). Its total energy cost is
`1+2*(hi−lo)`, here exactly `1+2*log V`. The differentiating profile is

\[
\operatorname{scaleProfile}W(y)=-\tfrac12W(y)-yW'(y)
\]

(`Scale:12`), and `scaleSum_deriv` (`Scale:39–70`) identifies it as the
log-scale derivative of the centrally normalized finite column. Its
support stays in the same interval (`scaleProfile_support`, `Scale:24–32`).
This explains precisely why both raw-moment inputs are needed.

If U2 supplies a uniform quadratic `C^k` raw-moment bound, this profile
costs **one additional ordinary derivative** on the fixed annulus:

\[
(\operatorname{scaleProfile}W)^{(j)}(y)
=-(j+\tfrac12)W^{(j)}(y)-yW^{(j+1)}(y),
\quad 0\le j\le k.
\]

Hence its `C^k` norm is bounded by
`(k+1/2+wb)*‖W‖_(C^(k+1))`, with the usual maximum derivative norm.
The interval-dependent factor belongs in the constant; the derivative
order increases from `k` to `k+1`, independently of the chosen interval.
The resulting common `C` remains quadratic in `W`, and the extracted
unnormalized amplitude remains linear in its seminorm after taking a
square root. This conclusion is conditional on completing U2's stated
quantifier order, rather than on fixed-test existence of a constant.

## Loss budgeting and the October 5 exponent

For fixed `q,b` and every `η>0`, the retained logarithmic product is
`O(D^η)` as `D→∞`. For example, on large `D` it is at most

\[
(1+2q)(q+|\log b|)(1+\log D)^2.
\]

The same log-versus-positive-power argument used in
`logarithmic_cost_eventually` (`Budget:62–98`) absorbs this. Its existing
`A≥1` parameterized statement need not be misapplied to `A=1/b` when
`b>1`; the displayed direct logarithmic estimate suffices mathematically.
Consequently

\[
|P_1(D)|^2\ll
C D^{5(1+c)/6+\kappa(2+c)+\eta}.
\]

`HeckeDyadic.coefficient` (`Dyadic:22–23`), `summand` (`Dyadic:44–46`)
and `polynomial` (`Dyadic:48–49`) show that at `inverse=true`,
`σ=freq=0`, this is `D^(-1/2)` times the ideal Möbius-character sum.
If `\mathcal A_1^{Lean}(D)` denotes that unnormalized sum, positivity of
`D` gives

\[
|\mathcal A_1^{Lean}(D)|\ll
\sqrt C\,
D^{11/12+5c/12+\kappa(2+c)/2+\eta/2}.
\]

Under U1's still-required equality with the prescribed October 5
`A₁(D)`, this is its unit-row extraction. At fixed `c=θ>0`, choose the
raw loss `κ` and logarithmic loss `η` small enough that
`κ(2+θ)+η≤2ε`; for instance, `κ=ε/(2+θ)`, `η=ε` gives exponent
`(11+5θ)/12+ε`.

To obtain `11/12+ε` for an arbitrary requested `ε>0`, provided raw moments
are available for the chosen positive gaps/losses, one explicit budget is

\[
c=\min(1,4\epsilon/5),\qquad
\kappa=\frac{2\epsilon}{3(2+c)},\qquad
\eta=2\epsilon/3.
\]

Then the three excess contributions `5c/12`, `κ(2+c)/2`, `η/2` are each
at most `ε/3`. Their constants and the large-`D` threshold may depend on
these choices and fixed prime/test data. Bounded column scales require
the usual direct finite-sum estimate; no effective numerical constant or
effective prime threshold is claimed here.

## What this changes in the crosswalk

U3's structural source obstacle is resolved: an exact arbitrary-`D`
fixed-ray amplification declaration has been located, and its unit-row
specialization has been derived with explicit cutoffs, constants and
losses. The prior caution about `no_slot_endpoint` remains correct; it
is eventual in `U` with `D=U^r`, and its substitution at `U=1` is invalid.

Remaining work is concrete:

1. Write and elaborate the singleton `FreeRow` construction, two scale-energy
   applications, the large-`D` pullback `x=D^q/b`, and the rpow/logarithm
   simplifications as a Lean application lemma. None was compiled here.
2. Discharge U1's prescribed fixed-character/exclusion dictionary before
   replacing `\mathcal A_1^{Lean}` with October 5's `A₁`.
3. Discharge U2's uniform seminorm input; then apply its estimate to both
   `W` and `scaleProfile W`, retaining the one-derivative cost.

The concurrent mathematical comparator run is independent evidence with
its own narrower nominated statement. This note does not claim its result,
does not expand its theorem scope, and does not claim the remaining U1/U2
applications have become formal proof terms.
