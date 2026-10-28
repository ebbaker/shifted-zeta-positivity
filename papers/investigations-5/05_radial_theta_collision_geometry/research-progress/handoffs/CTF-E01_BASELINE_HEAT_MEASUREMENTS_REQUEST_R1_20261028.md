# CTF E01 request R1 for finite time heat measurements

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0008, **Continue radial theta investigation**.

**Type: E — execution. Recommended model: Sol. Request revision: R1.**
The [live register][progress] owns status. This is a fixed-method calculation, not an assignment to invent a new flow. The author has not selected an actual execution model or effort through this file.

## Question and outcome

On the finite cases below, how large are the moment allowances in Note25, at what listed auxiliary times are they informative, and what does acquiring the heat diagnostic cost relative to the matched direct observation? The known extra-decay powers are not the research question. A measured poor allowance or inconclusive case is an acceptable bounded return, with its cause recorded.

Use [Note25][n25], especially equations(10)–(13), and [Review14][review14]. Note25 SHA-256 at request creation: 321d557080ef06abb3e8a70f85872f1e10980881a91fc47806d54ab9b050e11b. Read the current source before work; if it changes, reconcile the changed mathematics and issue a new request revision if needed. Do not silently reuse results from a different normalization.

## Fixed formulas

Set ε=1, r=e^(2u), ρ_t(u)=e^(tu²)Φ(u), and
\[
c_0(a,u)=\cos(au),\qquad c_1(a,u)=-u\sin(au).
\]
Evaluate k=0,1 using the one-dimensional central formulas:
\[
H_k=\int_0^\infty \rho_t c_k\,du,\quad
F_{s,k}=\int_0^\infty \rho_t e^{-e^{4u}/(4s)}c_k\,du,
\quad M_{2,k}=\int_0^\infty e^{4u}\rho_t c_k\,du.
\]
The physical density value is (4πs)^(-3/2)F_(s,k). Avoid computing a tiny density and rescaling if the displayed normalized integral is more stable.

For a simple positive majorant, compute
\[
C_{m,k}=\int_0^\infty e^{2mu}\rho_t u^k\,du,\qquad m=0,2,4.
\]
It bounds the corresponding absolute spatial moment A_(m,k); it need not equal that moment. The inherited allowances are
\[
|F_{s,k}-H_k|\le C_{2,k}/(4s),\qquad
|F_{s,k}-H_k+M_{2,k}/(4s)|\le C_{4,k}/(32s^2).
\]
Routine verification of the coordinate factors and standard positive tail bounds is part of E01. A new inequality or a new interpretation is not required to implement these formulas.

## Frozen cases

| Source | Physical time t | Frequency a | Auxiliary times s |
| --- | --- | --- | --- |
| Complete canonical theta | 0 and 1/4 | 0, 2√6, 28, 30 | 1, 4, 16, 64, 256 |
| Φ_*(u)=(64u⁴+6)exp(−(4+1/4)u²) | T_c=1/4 | 2√6−1/4, 2√6, 2√6+1/4 | The same five values |

Use both k values. There are 55 source/time/frequency/auxiliary-time cases and 110 scalar F values before precision repeats. Reuse H, M and C values across s. These theta points are illustrative measurements, with no assumed theta collision or newly certified zero-free region.

For the control at T_c,
\[
H_*(T_c,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16}.
\]
Use its exact derivative as the reference and preserve H_*=H_{*,a}=0 at a=2√6 exactly in the comparison. Do not replace that exact event by a quadrature residual. At a=0 the first derivative of an even transform also vanishes; one vanishing component is not a collision.

## Permitted numerical choices and limits

Use a locally available high-precision one-dimensional quadrature implementation; the quadrature library, caching and subdivision details are routine choices. Start with 30 decimal digits and repeat at 50 digits. Allow at most one additional subdivision refinement for a problematic case, at the same precision. Do not add further precision levels, frequencies, times or flow parameters in R1.

Separate theta-index truncation, u-tail truncation, quadrature error estimates and roundoff/precision comparison. Select cutoffs with the existing positive source majorants and standard one-dimensional tail estimates; routine derivation of those explicit estimates is allowed. Cap the retained theta index at N=12 and the u cutoff at U=8. These are work limits, not assertions that they always suffice. Record a case as unresolved if its required allowance cannot be met within them.

Aim for agreement between precision levels within 10^(-12) times the appropriate positive C majorant; for small or zero signed values, report an absolute allowance, not relative accuracy. Floating quadrature and precision agreement are diagnostics, not interval certification. An analytic tail bound evaluated without directed rounding is not automatically a certified numerical enclosure.

Cap the total numerical work at 250,000 integrand evaluations or 15 minutes of calculation time, whichever is reached first, with time checks between bounded integrations. Count actual evaluations where the library exposes them or through the integrand wrapper. Cache reusable quantities. If a single integration reaches its remaining budget, preserve the partial return and stop it. This budget concerns the numerical run, not a fabricated model-token allowance.

No three-dimensional PDE mesh, optimization, zero search, parameter fitting or enlarged height scan is included. The spatially radial convolution is already available; a large PDE solver would obscure this question.

## Required return

Save reproducible code and a small machine-readable record in numerics, plus a short note or assessment with:

- H_k, M_(2,k), C_(0,k), C_(2,k), C_(4,k), F_(s,k), and both residuals/allowances for the declared cases;
- the ratio of the allowance to a resolved nonzero signal, and which listed times make that comparison informative; leave the ratio undefined when its denominator is zero or unresolved;
- absolute central signals and remainders at the exact control collision, with no claim of a lower decay bound when the next moment may also cancel;
- source and cutoff choices, precision repeats, each error category, unresolved cases and retained failures;
- measured integrand counts and runtime for direct H/H_a versus acquiring the heat observations and their additional moments, with shared source setup/caching identified;
- a disposition of whether the baseline is practically informative on these samples, what dominates its cost, and what it suggests B01 should address.

A ratio below one is only a finite sampled diagnostic unless its full error enclosure is rigorous. Do not claim a speed advantage from unequal accuracy or omitted setup costs. Conservation and the already proved decay estimate are implementation checks; the substantive return is the measured allowance and cost.

Completion means the fixed question has a documented answer or a precise budget-limited answer, not that the result favors heat flow. Stop the packet then. Recommend the already declared **[B] CTF-B01 — Astra** if its conceptual question remains; routine recording and integration stay with Sol.

## Escalation and files

A defect in code or a routine normalization correction remains E01 work within its limits. If a source change, new flow, new observable, nonstandard tail theorem or different research question is needed, record the precise issue for B01 and do not execute the changed mathematics under R1. Continue unaffected declared cases only if useful.

Permitted writes: new numerics code/records; a return note or assessment; this packet's appended return link; the live progress entry and necessary navigation. Do not edit the manuscript as part of the calculation; accepted integration is E04. Preserve the request text and any failures. Record actual execution model, effort, date, source hashes and software versions.

Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md). No task is currently reported as executed, and no numerical constants have been invented.

[progress]: ../04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[n25]: ../../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[review14]: ../../reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md

## Execution return — 28 October 2026

**CTF-E01 R1 complete, floating evidence.** Prepared for Edward Baker with substantial LLM assistance, actual recorded **gpt-6.1-sol, effort ultra**, chat0009 **Continue conservative theta flow**. See [Note27](../../notes/27_CONSERVATIVE_HEAT_BASELINE_E01_RETURN_20261028.md), [record16](../../numerics/16_CONSERVATIVE_HEAT_BASELINE_MEASUREMENTS_20261028.json) and [assessment15](../../reviews/15_CONSERVATIVE_HEAT_BASELINE_E01_ASSESSMENT_20261028.md). All 110 scalar F values were acquired at both precisions, using 93,552 calls and 1.78331 seconds, without refinement or unresolved quantities. The moment correction improves finite-time allowances; heat and extra moments cost more than direct in this fixed comparison. All failed allowances remain recorded. No collision exclusion or certificate. The request above is unchanged; the live register owns status. **Next: [B] CTF-B01 — Astra**, to select a useful conservative flow/observable contract or return a scoped failure.
