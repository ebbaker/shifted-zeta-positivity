# Cross model review of the Newman certificate audit

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6.1-sol (`gpt-6.1-sol`), Codex, reasoning effort **ultra**, verified from the current session configuration. Three parallel review agents used the same configuration. This is an internal cross-model review and computational replay, not independent specialist validation or formal verification.

Reviewed: Claude's notes 1–5, the existing review of notes 1–2, the investigation README, and the associated numerical sources and records, as present at repository commit `d3773473f507f2c7e7fa6f1b99c040d92f2e593e`. The latest substantive Claude audit is commit `c50e4d9`. The public certificate is pinned throughout to `judegomila/dbn-lambda-01787854-candidate-audit` at `a74738deb6d5e0f76887cb36901da08b68dca705`. Reviewed file hashes and replay results are retained in the [review check record](../numerics/CODEX_REVIEW_CHECK_RECORD_20261013.json).

## Verdict

The investigation makes substantial, credible progress. The weakest finite row, the complete Dini gate, and the tail and uniform-error checks reproduce. The source arguments for the native binding, window freeze, redundant tail overlap, derivative envelopes, stored sums, closed-prism homotopy, and extension to zero time are coherent within their stated imported inputs. I found no defect that defeats the pinned package's proposed bound.

Claude's audit nevertheless needs corrections before consolidation. Its uniform-budget exposition freezes an exponent too early; several exported or displayed bounds round inward; and the direct-sum comparator tests overlap while reporting containment. The benchmark also turns a reasonable decision about research priorities into stronger claims about impossibility, cost, and maximal parameter gains than its evidence establishes. These findings concern the audit and its auxiliary evidence. They do not establish that the package's mathematical conclusion is false.

The recommendation to stop a corrected-interface record campaign remains reasonable for the present triangle-bound method. The complete certificate remains an open audit: the finite producer and its full corpus have not been independently verified here.

## Findings

### 1 Keep the cutoff dependent exponent in the uniform tail cap

**Priority 2.** [Note 4](../notes/4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md), lines 418–422, writes the U3 cap with `σ1 = σ1(N0,y0)` and then invokes gates that establish decrease as `N` increases. Those gates require the exponent to vary with `N`. The frozen cap in the displayed argument increases even over the finite certificate's range.

Using the note's `t_hi = 0.161250001`, `σ1 = 1.67770988985377282904783187031`, and head cutoff 2000 gives, approximately:

| N | Cap with the exponent frozen at N0 |
| ---: | ---: |
| 690988 | 0.943027908358772120677 |
| 1381976 | 1.425391626007790240637 |

The cap's validity condition holds at both points; its asserted decrease does not. At still larger cutoffs the frozen exponent also ceases to satisfy the cap's validity condition. This is a defect in the written all-cutoff reduction, rather than a discrepancy in the computed value at `N0`.

The repair is to retain

\[
\sigma_N(t)=\frac{1+y_0}{2}+\frac{t}{2}\log N-\delta_1
\]

inside the cap, where `δ1` is the conservative correction already frozen at `N0`. Freeze the finite head at `N0`, and write the reduction as

\[
\sum_{n\le N}b_n n^{-\Re s_*}
\le \operatorname{Head}_{N_0}
 +\operatorname{Cap}(2000,N;\sigma_N(t))
\le \operatorname{Head}_{N_0}
 +\operatorname{Cap}(2000,N_0;\sigma_{N_0}(t)).
\]

Then U3b and U3c apply to the moving cap. This is the intended reduction behind the package's [binding provenance](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/provenance/RECORD_BINDING.upstream.md) and authoritative Arb budget program. No change to the recorded budget is indicated.

### 2 Preserve outward rounding when exporting certified endpoints

**Priority 2.** The helper `s()` in [the tail checker](../numerics/check_tail_and_uniform_error_budget.py), lines 195–197, and [the barrier checker](../numerics/check_barrier_suppliers.py), lines 162–163, creates a fresh Decimal context with nearest rounding. Values labelled `_hi` or `_lo` therefore lose their endpoint meaning when serialized.

For example, the internally computed directed upper endpoint is

```
prop410.Emax_hi = 2.3349490521233784876597101852111302315385982043498E-7
```

but the retained JSON gives

```
prop410.Emax_hi = 2.33494905212337848765971018521E-7
```

which is smaller. The computed lower ratio `3.389224894969161219…` is exported as `3.3892249`, which is larger. Likewise the barrier's serialized lower margin `0.519849894613872543387` exceeds the exact recomputed lower margin by about `1.67·10⁻²⁴`.

The same issue affects prose. [Note 3](../notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md), lines 152–185, labels a table column as the certified lower end. For `N = 718001`, it displays `0.010993582868608`; the certified interval is

```
[0.0109935828686075183228516960437200960498907080,
 0.0109935828686075183919247119471907861011757531].
```

The displayed value lies above the entire interval. This makes it an approximate display, not a certified lower endpoint.

Use explicit floor rounding for lower endpoints and ceiling rounding for upper endpoints, including Fraction-to-decimal conversion and shortened prose displays, as supported by the [Decimal context rounding modes](https://docs.python.org/3.10/library/decimal.html#decimal.Context). Alternatively label shortened values as approximations and keep the full endpoints as the certificate. Rerun and refresh the source hashes of affected records after the change. The decisive comparisons use the original internal values, so the observed serialization errors change no pass/fail result and consume no material margin. The weakest-row replay's full JSON endpoints are sound.

### 3 Test containment and account for printed arithmetic data

**Priority 2.** [The direct-sum comparator](../numerics/compare_direct_and_stored_sum_values.py), line 79, reports `direct_inside_stored_ball` when

\[
|c_d-c_s|\le r_s+r_d.
\]

That tests overlap. Componentwise containment requires

\[
|c_d-c_s|+r_d\le r_s.
\]

A negative control with stored interval `[-1,1]` and direct interval `[0.5,2.5]` returns `True` under the current predicate. Thus the predicate cannot justify [note 5](../notes/5_BARRIER_CERTIFICATE_AUDIT_20261013.md), lines 710–713, as written.

There is also a serialization issue: [the direct evaluator](../numerics/direct_ft_arb.c), lines 120–123, and [the instrumentation patch](../numerics/barrier_dump_instrumentation.patch), lines 33–41, print midpoints and radii independently. A midpoint printed to 30 significant digits can incur rounding near `10⁻²⁹` while the printed direct radius is near `10⁻⁶²`. The resulting decimal midpoint and tiny radius need an additional printing allowance to represent the original Arb ball. Radius rounding and the printed input coordinates also need their stated allowances if claiming rigorous containment at the original mesh point.

The retained evidence survives the corrected predicate. Exact rational checks of all 117 pairs, comprising 234 real components, found no containment failure for the recorded decimals. Allowing one full last printed place for each output midpoint and radius, increasing the direct radius and decreasing the stored radius conservatively, still gives no failure. The largest consumed fraction of the conservative stored radius is approximately `0.00100835`. This output check does not itself pay coordinate displacement between the printed input and the original mesh ball.

Replace the predicate and make the export allowances explicit, or consistently describe this as numerical corroboration. The small observed discrepancies remain persuasive corroboration of the stored-sum implementation. The package's coefficient-provenance and Taylor-tail certificates carry the rigorous barrier argument independently of this auxiliary comparison.

### 4 Narrow the benchmark conclusion to what was measured

**Priority 2.** [Note 1](../notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md), lines 121–138, and [note 2](../notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md), lines 80–110, overstate three conclusions.

First, a smaller approximation allowance can change the barrier's time steps. The [pinned barrier program](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/barrier/src/TloopSinglemat_closed_cert.c), lines 1348–1368, computes a step from

\[
\Delta t\approx\frac{M_i-S_i-\varepsilon}{2D_{t,\mathrm{seam}}}.
\]

The approximation allowance is explicitly in this formula. At prism 882, holding the value and derivative suppliers fixed and lowering `ε` from `0.00125` to `10⁻⁹` increases the candidate step by approximately **0.12023 percent**. That does not establish a different total prism count or a worthwhile speedup: corrected values and derivatives would also change, and subsequent seams would need a fresh replay. It does refute the categorical statement that no time step changes. The mesh count depends on a derivative ceiling, whose effect also was not benchmarked with a corrected evaluator.

Second, the finite-difference sensitivities are local, nonrigorous estimates. Dividing the saved error allowance by those slopes supports a scale of approximately `1.2·10⁻⁸` for a local one-parameter gain near the present row. It does not prove the displayed `≤` inequalities or a maximal gain over the certificate class. That would require derivative bounds on a specified neighborhood and a stated parameter path or optimization problem.

Third, the present coefficientwise triangle bound cannot simply replace `e_{C,0}` by `e_C`: its lower-bound target is `f_t`, whereas the corrected budget belongs to `f_t−C_t/B_t`. A reverse-triangle estimate pays a supremum of the correction. This explains why the smaller residual is not directly usable in the existing lane. It is not an impossibility theorem for every uniform method; a different bound could retain phase correlations. Nor is spacing proportional to `e_C/|∂_x f_t|` a universal requirement for pointwise certification: a mesh spacing is paid from the available modulus slack after all errors.

A supported replacement conclusion is: **The current triangle lane cannot directly consume the retained-C residual. The measured local benefit is very small, and no material improvement in feasibility or cost has been demonstrated. Stop this parameter campaign unless a different lower-bound mechanism supplies a concrete gain.** This preserves the practical decision while keeping its mathematical scope accurate.

### 5 Correct the interpretation of the Dini exploration

**Priority 3.** [Note 3](../notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md), lines 298–307, calls one exploration column “sampled sup, attained L.” [The landscape script](../numerics/explore_dini_gate_landscape.py), lines 99–106, merely filters a continuous logarithmic grid by `L ≥ log(max(2,G0))`. It does not enumerate integer `n`, verify its greatest common divisor with the mollifier modulus, or check compatible integer `N` and sector membership. Relabel that column as a filtered continuous-domain sample. The separate certified negative control at `n = 6910020`, `N = 690988`, is correctly attained and remains valid.

The package's reported gap below 1 is a valid conservative certified gate margin, although the acceptance rule makes it a poor estimate of the actual slack. Replace the phrase “not a margin” with that distinction. When stating ratio suprema, define the ratio where `C0` is nonzero and handle its zeros through the already certified `h ≤ 0` branch. The stronger global gate bounds `3/4, 3/4, 1/4, 0` reproduce and are unaffected by these refinements.

## Reproduced evidence and scope

The review used a fresh temporary checkout of the pinned public package and verified all **443** sealed files. All eight retained checker or script hash fields match their current sources. The Polymath TeX source at `8e8a6ab1115d67aad66f6dbef374eef64922a060` also matches the investigation's recorded hash. Python reruns used CPython **3.10.0**; comparisons exclude software-version and runtime fields.

| Check | Scope replayed in this review | Result |
| --- | --- | --- |
| Error-budget benchmark | All five retained point cases and their benchmark arithmetic | Numerical cases and benchmark fields match exactly |
| Certified finite row | N = 690988, plus four small brute-force enumeration self-tests | Full interval endpoints match exactly; self-tests pass |
| Stored row binding | All 32 retained floors and first-of-run flags, against pinned shards | All match; this is a record-to-shard check, not 32 fresh numerical replays |
| Dini gate | All four legs with thresholds 3/4, 3/4, 1/4, 0 and negative controls | Every non-timing result reproduces; no undecided leaves |
| Tail and uniform finite budget | Complete checker and its self-test | All 54 gates pass; retained result fields match exactly |
| Barrier suppliers | Both 883-prism transcripts, all five direct derivative-majorant sums, Taylor tail, and uniform-error gates | All 44 gates pass; all retained result fields and hashes match exactly |
| Direct-sum comparison | 117 retained pairs with the corrected containment predicate and output-rounding allowances | All 234 components pass; direct evaluator not rebuilt |

The weakest-row interval reproduces as

\[
L_{690988}\in
[7.91366745594125134859763706221890573633320804,
 7.91366745594188364412870631974216863412952246]\,10^{-7}.
\]

Against the package's stated conservative `E_max`, its lower margin exceeds `5.5787184·10⁻⁷`. The tail's overlap-free contraction remains approximately `0.960478`; the reserve near `0.03952` is substantially more informative than the package's padded contraction. These are the principal numerical conclusions relevant to prioritizing further work.

## Mathematical points that check

The analytic review corroborates the finite lane's convolution binding and window freeze, the Dini pattern reduction, the tail partition and cap routing, and the reverse order of the tail's height and cutoff reductions. The barrier review corroborates the derivative-box envelopes, the head-plus-integral monotonicity conditions, the stored-sum identity, the separate Taylor-tail payment, the fixed natural cutoff, the strict prism gate, the polygon-to-boundary homotopy, and continuity at zero time. In particular, note 5 correctly supplies a repair for the derivative-box text's distinction between the true exponent and its replacement majorant.

The [pinned Polymath source](https://github.com/km-git-acc/dbn_upper_bound/blob/8e8a6ab1115d67aad66f6dbef374eef64922a060/Writeup/debruijn.tex) also confirms the discrepancies discussed by Claude: the two versions of the correction in (21), the stated shortcut to `10.44` in (24), and the unjustified time division by `2n` in the historical barrier display. The candidate's barrier uses the undivided time payment. The candidate's error weld uses `10.50`.

Claude's claims that the two displayed Polymath bounds remain true can be stated as uniform inequalities, replacing the asymptotic reasoning in note 4. For (21), the corresponding `Re α` estimate retains a logarithmic gain of at least `1/[4(x²+4)]`, while the discrepancy between its positive-part corrections is at most `1/(3x⁴)`; the former dominates for `x ≥ 200`. Both gains acquire the same `t/2` factor when transferred to `Re s*`. For (24), put

\[
u=\frac{1.24(3^y+3^{-y})}{N-0.125}+\frac{6.92}{x-12},
\qquad v=2.48\sqrt{4\pi/x}.
\]

The natural cutoff gives `N−0.125 ≤ √(x/(4π))`, hence `u ≥ v` and `v < 0.623`. Therefore

\[
u-\log(1+u)\ge\frac{v^2}{2(1+v)}>23/x,
\]

whereas the shortcut's deficit is at most `0.06/(x−12) ≤ 0.064/x` on the stated region. This supplies the missing quantitative comparison without asserting that the original written shortcut was valid.

## Remaining work before consolidation

Correct the five findings and refresh affected records before treating their printed endpoints as reusable certificates. Preserve the distinction between a replay of Claude's checker and an implementation independently derived from the mathematics.

B3 remains the next substantive audit task: inspect the finite producer's amortized updates, frozen sawtooth weights, Taylor and rounding payments, time boxes, and coverage of every shard and seam. Agreement of a pointwise functional with a lower stored floor at `t0` does not by itself validate that producer or its entire time box. Claude independently recomputed 32 of the 3,149,013 stored rows; this review freshly recomputed one of those 32. The remaining 3,148,981 rows are still open in the investigation's replay plan.

The [Polymath criterion and approximation theorem](https://arxiv.org/abs/1904.12438v2), [Platt–Trudgian's verified height](https://arxiv.org/abs/2004.09765), and the arithmetic libraries remain imported dependencies. This review did not rebuild the package's C/Arb programs or the direct evaluator. Claude's reported byte replays remain prior-session evidence, not fresh C replays supplied by this review. Matching the pinned TeX source does not close the investigation's stated identity comparison with arXiv v2.

Proceed with producer correctness and coverage, then B4 consolidation. A new sharp-weight bound would require its full finite and tail suppliers and the height-transfer argument, even though the existing barrier can be restricted to a smaller final time. The positive one-row sharp-weight observation remains an exploratory lead, not a new bound.
