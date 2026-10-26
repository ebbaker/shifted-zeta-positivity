# Assessment: fixed negative times and the two error scales

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Review type: same-model internal analytical assessment.** Parallel
same-model checks of the source remainder, cutoff transfer, gamma
curvature and heat consumers contributed to this assessment. They share
the model and classical inputs with the derivation; they are not human,
cross-model or independent specialist validation. No numerical,
machine-symbolic, exact-arithmetic or interval research was executed.

## Evidence and disposition

Reviewed [HDA-A02-AN01 r1][packet], [Note03][n03], [Note04][n04], the
[preceding assessment][r03], and the complete staged [Note05][n05].
The [opening manifest][inputs] records the continuation's input versions.
The exact zero-time contours and arbitrary-order remainder in
[Polymath v2, equations36--38 and Proposition6.2][polymath] were rechecked.
Their use here is separated from the paper's positive-time evolved
estimates. The underlying Arias de Reyna coefficient construction is an
import through that proposition, not an independently reconstructed or
newly verified coefficient-provider implementation.

Accept **FN5**, for `t=-T`, `1<=T<=2`, on every declared fixed buffered
chart: the existing short finite arithmetic formula has field, spatial
derivatives j<=3 and a direct first time error bounded by
`C |G(z)| X^-3/4`. This is its **natural gamma-scale** comparison. It
does not supply an error tending to zero relative to the smaller outer
carrier.

Accept **FN19** for the finite real-initial-data heat transform, and
**FN25--26** for the finite Gaussian-moment arithmetic sum plus the
retained bounded RS correction integral. Their field, spatial derivatives
j<=3 and direct first time errors are at most
`C E_o(-T,z) exp(-L_X^2/4)`. Both growing RS order and common gamma
curvature are paid before this outer-scale conclusion is drawn.

Close **HDA-A02-AN01 r1** at its requested `1<=T<=2` analytical scope.
The broader compact-negative-time/short-formula program remains
**Partial**. Constants and onset gates are finite analytical quantities,
without an evaluated or certified numerical cutoff.

## What was checked

1. **The two comparison scales remain distinct.** FN3 gives a positive
   lower bound for the outer envelope in terms of
   `G(X) exp(-T L_X^2/16)` on each fixed chart. FN5 divided by that
   envelope still permits `X^-3/4 exp(T L_X^2/16)`, which grows at fixed
   T. The note preserves this failed budget as a limitation of that
   bound. It is neither a lower bound on the actual short-model error
   nor an impossibility theorem.

2. **The negative-time source identity is exact for complex targets.**
   FN4 integrates real initial values against the complex spatial heat
   kernel. Absolute Fubini follows from the integrable complete source
   and the real Gaussian; the resulting Fourier Gaussian is the stated
   negative-time evolution. On `1<=T<=2`, the transverse kernel cost
   `exp((Im z)^2/(4T))` is bounded for each fixed buffer. This avoids
   an unproved off-axis extension of high-order real RS data.

3. **The natural-scale proof counts the entire arithmetic population.**
   FN6--7 retain the transverse cancellation when comparing complex
   target modes to real initial values. The log-gamma curvature is
   `O(X^-1)` independently of n, and summing its absolute error through
   N costs `G X^1/4/X`. FN9 bounds the required logarithmic moments
   over the growing mode population, rather than relying on convergence
   of finitely many low modes. It pays the gamma-to-elementary defect
   and the exact elementary-model residual at fixed T. The slowly
   varying correction factor contributes the same `G X^-3/4` allowance.

4. **The source's growing-order constants are retained.** FN13 is the
   sigma=1/2 specialization of Proposition6.2, including the actual
   factor `Gamma((K+1)/2)(1.1/a)^(K+1)`. Exact gamma M is retained.
   With `K=ceil L_X`, outer normalization gives FN18,
   `-(3/8)L_X^2+(1/2)L_X log L_X+O(L_X)`. The odd/even coefficient
   ratio `k/(8a^2)` supplies a K-uniform bound for the whole retained
   correction when `K<=a_min^2`. No unspecified growing-order constant
   is treated as fixed. The negative-sigma condition of the source was
   checked, but only sigma=1/2 is actually invoked by this construction.

5. **Every cutoff crossing is accounted for exactly.** FN15 transfers
   `S_m-S_N` without an asymptotic replacement. After the stated
   cutoff-span gate, it contains at most one adjacent mode. The source
   order, center cutoff and integration endpoints stay fixed when z or
   time is differentiated. Internal real-u partitions at RS thresholds
   also stay fixed. Possible one-sided discrepancies of the truncated
   initial data at isolated thresholds do not invalidate its integral
   or its holomorphic target dependence.

6. **Real parts are taken in the permitted place.** FN12 constructs
   real initial data before its multiplication by the complex heat
   kernel. The note never replaces this with the real part of a
   target-dependent complex integral. Thus FN16 and the correction
   integral in FN25 are entire in z. The same observation allows
   kernel differentiation despite the piecewise initial coefficients.

7. **Arithmetic heat curvature receives a separate high-order payment.**
   FN20 factors each exact mode into its exponential tangent and a
   curvature function independent of n. On `R=X^1/3`, its logarithm is
   bounded by `C R^2/X`, eventually at most log2. Cauchy's formula
   therefore bounds every exact Taylor coefficient uniformly in its
   order and gives the remainder in FN21. For `J=ceil(3L_X)`, the
   complete mode population and outer-carrier loss yield FN24,
   `-(7/8)L_X^2+3L_X log L_X+O(L_X)`. This is a direct analytic
   high-order construction; a formal growing-order Stirling series is
   not presumed valid.

8. **Both true and artificial tails are paid at the requested scale.**
   The window is `V=8L_X`. The true intermediate tail retains the
   gamma height exponential and an explicit fixed polynomial height
   loss; FN27 has worst leading exponent `-(7/8)L_X^2`. A global
   source bound is used only in the distant `|u-X|>X/2` tail, where
   Gaussian decay dominates the lost height exponential. For artificial
   gamma-moment tails, the common polynomial is bounded on
   `V<|q|<=R/2`; on the remaining ray its degree `O(log X)` and the
   bounded linear tilt are dominated uniformly by a quadratic Gaussian
   exponent. The retained population and kernel derivative factors
   are included before absorption into the stated onset.

9. **Spatial and time estimates follow from proved field comparisons.**
   FN5 uses fixed analytic margins, gamma-envelope comparability and
   the summed exact model residual. For the high-order model, spatial
   derivatives hit the Gaussian kernel and give bounded local moments;
   its completed exponential-polynomial transforms obey the same heat
   identity exactly. Both terms in FN25 satisfy `partial_T F=F_zz`
   with frozen data and endpoints. The direct first time error is
   therefore the negative of the second spatial error. No asymptotic
   allowance is differentiated, and a small residual is not used as a
   substitute for the field comparison.

## Limits and continuation

FN26 concerns a finite representation with logarithmically growing
source/curvature orders and one bounded correction integral. It does
not turn the existing short formula into an outer-scale asymptotic,
identify a single leading elementary amplitude or phase, or establish
that an isolated retained correction dominates H. No denominator is
the true field or a potentially vanishing cosine.

The number of arithmetic modes still grows like sqrt X. Named exact
coefficient functions and derivatives are mathematical data; their
conditioning, evaluated working precision, quadrature cost and useful
runtime are unproved. There is no numerical onset, empirical validation,
interval certificate or provider-complexity theorem in this assessment.

No physical U,W,R,J,Q transfer, joining-defect cancellation, collision
exclusion, simplicity statement or RH conclusion is accepted. The
physical source, normalization, q and unnormalized observables remain
unchanged. Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
remain. The control screen uses the canonical completion and complete
ordinary coefficient sequence, not a positivity or no-collision
assumption. Consult [result summaries][results] and [avoid][avoid],
especially shared-premise review05, scope07, cancellation12,
unchecked-imports16 and status19.

**Next owner: Analysis — Sol.** The next concrete deliverable is the
bounded bridge `4/L_X<=T<=2`, paying the complex-kernel and derivative
losses as its lower endpoint shrinks, then joining to Note04 on
`4<=T L_X<=8`. The actual time-only joining residual and derivative
must be paid before accepting the full negative interval `[-2,0]`.
The [next packet](../research-progress/handoffs/HDA-A02-AN02.md) is
prepared, not dispatched. Arbitrary compact families, unbounded T,
physical transfer and all-time assembly stay outside that task. No
specific resistant mechanism remains to justify Astra escalation; no
numerical execution or automatic dispatch is authorized here.

[packet]: ../research-progress/handoffs/HDA-A02-AN01.md
[inputs]: ../notes/05_FIXED_NEGATIVE_TIME_INPUTS_20261025.json
[n03]: ../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[n04]: ../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[n05]: ../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[r03]: 03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[polymath]: https://arxiv.org/html/1904.12438v2
