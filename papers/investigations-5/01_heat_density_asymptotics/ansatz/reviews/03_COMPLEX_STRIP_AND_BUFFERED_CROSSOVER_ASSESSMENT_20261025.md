# Assessment: complex remainder and buffered signed-time crossover

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Review type: same-model internal analytical assessment.** Parallel
same-model source, interpolation and heat-consumer checks participated.
They are not independent specialist, human or cross-model validation.
No numerical, symbolic, exact-arithmetic or interval research was run.

Final note audit incorporated three local clarifications before acceptance:
tail constants are frozen before choosing the window; enlarged-chart
constants only affect the onset/final prefactors; the near-tail source
range is u>=X/3 to include shifted chart centers; and complex weights
are bounded by their moduli. None changes the theorem or exponent.

## Evidence and disposition

Reviewed [AN02 r1](../research-progress/handoffs/HDA-A01-AN02.md),
[Note03](../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md),
its prior assessment, the [opening manifest](../notes/04_COMPLEX_STRIP_INPUTS_20261025.json),
and [Note04](../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md).
Primary DLMF25.2.8, DLMF25.10.3--4, DLMF5.11 and Polymath
equations36--38, Proposition6.2, and the domains of Proposition6.3
and corrected equation69 were rechecked.

Accept **CS3**, the fixed-cutoff complex remainder with exponent -3/4
and **no epsilon loss**, on every declared fixed chart and strip.
Accept **CS6--7**, the signed buffered field, spatial jets j<=3 and
direct first time derivative for |t| log(X/(4pi))<=8. Close AN02 r1
and HDA-A01 at the combined AN01--AN02 **bounded analytical scope**.
The global all-real-time objective remains open. The proof has finite
analytical onset gates; constants and numerical cutoffs are unevaluated.

## What was checked

1. **A real estimate is not analytically extended by assertion.** The
   normalized error `E_N/M(1-s)` is holomorphic on the whole upper
   rectangle because its denominator is nonzero there. Its growing
   real edge is justified anew: with A=log^2 X, the neighboring-cutoff
   mismatch is O(G[(A+1)X^-5/4+A^3X^-9/4]), which is absorbed by the
   original corrected real RS error after the recorded eventual gates.

2. **The upper edge preserves the exponent.** At height D>=4, the
   exact arithmetic identity groups `H/Mdom` and its dominant finite
   sum as the **ordinary Dirichlet tail**. Its bound and that of the
   reflected finite sum are X^((1-D)/4), at most X^-3/4. The correction
   is smaller there. Estimating these terms separately would leave O(1)
   and incur an avoidable power loss.

3. **Vertical edges are paid.** Euler summation with integer cutoff
   ceil X gives zeta=O_D(X^1/2) uniformly for real part>=1/2 in the
   bounded strip. Both finite sums are O_D(X^1/4) after dominant-arm
   normalization. The analytic Gaussian weight gives side factor
   X^5/4 exp(-log^4 X+D^2). Undoing the weight costs a fixed constant
   on a fixed target width. Reflection pays the lower half-strip.
   There is no hidden unbounded-edge assumption or epsilon loss.

4. **Published domains stay distinct.** Polymath Proposition6.2 is
   an all-real-sigma zero-time contour estimate, with K+sigma>=2
   required for its negative-sigma remainder. Proposition6.3's narrower
   evolved domain is not imported as a broad-buffer theorem. The
   main maximum-principle proof already proves the needed zero-time
   estimate from its independently paid boundaries. The source contour
   calculation is a separate same-model consistency check.

5. **The averaging and differentiation buffers are complete.** The
   proof establishes CS3 on arbitrary fixed enlarged charts before
   consuming it. Positive heat uses the strip b+1+2V_b; negative heat
   uses the horizontal radius r+V_b+2. A common fixed window V_b
   is chosen from source/gamma constants and the coarse height power.
   This repairs the limitation of retaining window16 for arbitrary
   strip widths under a coarse absolute tail estimate.

6. **Both signed source identities are exact.** Negative times use
   real spatial Gaussian smoothing; positive times use imaginary
   spatial Gaussian smoothing. Both are derived from the complete
   source and not from continuation of a signed remainder. Near
   tails retain the gamma height exponential, and the distant tails
   are paid separately. The true analytic correction is used only
   on the fixed local windows; only its linearized model is completed
   to a full elementary Gaussian.

7. **Population and amplitude losses are retained.** All N modes
   are counted. Their total nonzero-arm envelope is at most
   C E_o X^1/4 exp(t_- L_X^2/16), including off-axis n-powers and
   the dominant/subdominant arm ratio. This yields
   delta=X^-3/4 exp(t_- L_X^2/16), bounded by C X^-1/4 in the
   declared signed window, and X^-3/4 for nonnegative times.
   No fixed-mode convergence is substituted for this growing sum.

8. **The time derivative does not inherit a 1/T loss.** Cauchy disks
   of radius comparable to 1/log X give the spatial jets. The exact
   per-mode residual CS26 is O(log X/X), including the t c^2 term
   on |t|L_X<=8. The correction residual is O(G X^-3/4). Summing
   these and using the exact heat identity gives CS7 uniformly
   through zero. No big-O or Gaussian error estimate is differentiated.

## Limits that remain

The theorem is on holomorphic fixed-N charts. A global floor-valued
formula remains piecewise and is not silently differentiated; overlap
comparison is through the same H. Physical joins and their defects
remain separate. Constants can grow strongly with fixed strip/filter
widths; no useful runtime or certified numerical onset is supplied.

This theorem is not a uniform fixed-negative-time result. At T bounded
away from zero, exp(T L_X^2/16) exceeds every fixed power of X, so the
fixed-order RS remainder used here cannot pay the outer-carrier target.
That is a limitation of this budget, not a lower bound on the actual
error or an impossibility theorem for a higher-order or contour method.

No physical U,W,R,J,Q transfer, collision exclusion, simplicity or RH
conclusion is accepted. Parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain. Note04's control table names the exact completion
and coefficient premises absent from the repository controls. Consult
[result summaries](../../../../../result-summaries/README.md) and
[avoid](../../../../../avoid/README.md), especially shared-premise02,
review05, scope07, cancellation12 and unchecked-imports16.

**Next owner: Analysis — Sol.** The next regime is HDA-A02, fixed compact
negative time. Its next bounded packet should pay a growing-order RS
remainder or retain a quantitatively controlled complete contour. This
requires a new estimate, not substitution of fixed negative time into
the present shrinking-time theorem. No numerical execution or dispatch
is authorized by this assessment.
