# GNP-RS-B07 return, continuation and model-change guidance

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0006, thread
`01a1d151-91b1-7663-8f10-07d0b4f94163`. Actual backend model and reasoning
effort are unavailable in the recorded configurations. Three analytical
helpers contributed to the proof/check; their inherited settings are not
independently identified. Suggested models below are prospective.

**B07 is complete at inherited-input analytical-proof and contributing
separate-agent internal-check scope.** [Note23](23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md)
holds the proof; [Review12](../reviews/12_GNP_RS_B07_INTERNAL_ASSESSMENT_20261112.md)
holds the assessment. This supersedes Note22's proposed B07 routing and its
current-localization-loss description, while preserving the original B06
proof and scope. The [sole register](../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md)
owns status. No E08, manuscript integration or new numerical campaign is
issued.

Read [result summaries](../../../../../result-summaries/README.md), especially
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
and [avoid](../../../../../avoid/README.md), specifically
[target01](../../../../../avoid/01_restating_the_target.md),
[premise02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[separate-bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Note23 Section 8 applies [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
to named canonical premises. A collision witness need not contradict a
large-height averaged estimate.

## 1. Quantitative return

At c=1, with \(L_U=\log(U/(4\pi))\) and prime cutoff
\(P_U=\lfloor L_U^2\rfloor\) constant on the outer interval, for every
fixed \(0<\rho\le1/4\), all sufficiently large real U and
\(U^{1/4+\rho}\le\ell\le U\),
\[
 \frac1\ell\int_U^{U+\ell}R_{P_U}(X,1)dX
       =\mu_{P_U}+O_\rho(L_U^{-3/2})=O_\rho(L_U^{-1}),
\]
\[
 \frac1\ell\int_U^{U+\ell}J_{1/L_X}(X)dX=O_\rho(L_U^{-1/3}).
\]
For each fixed h>0 the exceptional proportion with Green value at least h
is \(O_{h,\rho}(L_U^{-1})\). The exponent in the shortest useful
interval is improved from B06's 3/8 to 1/4; the logarithmic rates are
preserved. Note23 also gives a uniform formula for every integer
\(2\le P\le\lfloor L_U^2\rfloor\), with error
\[
 C(\sqrt{\mu_P}/L_U+L_U^{-2})
       +O_\rho(U^{-\min(1/128,5\rho/24)}).
\]
These are inherited-input analytical estimates with internal LLM checking,
not specialist-reviewed theorems or evaluated onset certificates.

Two reusable improvements deliver this gain. First, keep the exact
Fubini weight W and use \(d\sigma=2W\,dx/\ell\). Its mass differs
from 1 by at most \((4/\pi)U^{-4}\), and its total variation is bounded.
The old separate convolution-edge envelope is unnecessary. Second,
majorize the nonnegative complete-tail norm by a fixed smooth height
average, pay coefficient/phase freezing and every cutoff crossing, and
use a discrete third-derivative estimate on the actual shifted
logarithmic phases. This yields
\[
 \|A-A_Y\|_{L^2(\sigma)}^2\ll Y^{-1/4}
 +U^{7/24}\ell^{-7/6}+U^{5/24}\ell^{-5/6}
 +U^{3/8}\ell^{-4}+U^{-5/8}
\]
for \(r_*\le\ell\le\sqrt U\). There is no dyadic-block logarithmic
loss. B06 covers \(\sqrt U\le\ell\le U\). The retained reflected
phases already have a paid nonstationary gap; do not reintroduce their
old full-population curvature loss.

## 2. Precise remaining gap

At \(\ell=U^{1/4}\), the two displayed shifted-tail bounds are order
one. This is the limit of the particular estimate that sums absolute
values after bounding each shift separately. It is not a lower bound on
the actual correlation, not optimality of exponent 1/4, and not an
impossibility theorem for other methods. The finite head's same-arm cost
also needs retuning below that range; retuning alone cannot fix the
complete tail.

The arithmetic object before that absolute summation is Note23 (B07.31):
\[
 \sum_h\sum_{m\in I_{N,h}}w_m(U)w_{m+h}(U)
 e^{i\nu_U\log(1+h/m)}
 \widehat\chi\bigl((\ell/2)\log(1+h/m)\bigr),
\]
where \(m\asymp N\le\sqrt U\), \(m+h\le N_U\), and the effective
shift range is \(h\lesssim N/\ell\). The current block bound is
\[
 U^{1/6}N^{1/4}\ell^{-7/6}
             +U^{-1/6}N^{3/4}\ell^{-5/6}.
\]
This is a concrete place to test a stronger arithmetic estimate.

An every-center conclusion still requires additional information. The
available total Green mass is \(O(\ell L_U^{-1/3})\), which grows even
on the new shortest intervals. A localized positive defect can fit inside
it. No pointwise small value, maximal estimate adequate to eliminate
exceptions, or quantitative persistence lower bound on the same moving-time
curve has been proved. A further smaller positive exponent would improve
localization but would not by itself close that logical gap.

Keep all coverage obligations visible: c=1 only; fixed original Green
strip/depth/radius; physical time fixed inside each spatial window;
cutoff fixed across the outer block; unevaluated finite onset and untreated
bounded heights. Full-c, center-varying-cutoff, shrinking-depth, time-zero
and positive-threshold exclusions are not obtained. Parent GNP and sibling
RSCT retain their ownership. Fixed-P obstruction results keep their
fixed-reference scope.

## 3. Suggested next model and one bounded question

**Suggested continuation model: GPT-6 Astra.** The next pass requires
selecting and testing a stronger arithmetic estimate. This remains the
conceptual-work recommendation from Note22, whose
[official model source](https://developers.openai.com/api/docs/models/gpt-6-astra)
was checked on 12 November 2026. No switch is performed here, and no
recommendation identifies the actual model used for this proof. Record
the actual selected effort if available. GPT-6.1 Sol can execute a later
fixed proof or focused audit after its statement is settled.

The recommended next bounded pass, provisionally **GNP-RS-B08**, is:
can one applicable estimate for the exact shifted sum above improve the
quarter-power localization threshold, while keeping the complete tail,
physical clock and exact convolution weight paid?

Start at (B07.31), retaining the m and h dependence until the selected
estimate justifies a loss. Compare the proposed bound quantitatively with
(B07.16) before writing a new theorem. Check all primary-source hypotheses,
partial-interval uniformity, amplitude derivatives, floor crossings,
product growth and the head/reflected gates. An acceptable return is a
proved improvement to the exponent/range or a precisely scoped failed
inequality. State separately whether it supplies any actual route to
pointwise smallness or a useful persistence-versus-total-mass comparison.
Do not label an assumed bound for (B07.31) a new mechanism.

The exact W boundary repair is already complete; carry it forward. Do not
restart the old edge-envelope calculation, the fixed-P substitution, or
an independent-prime phase average. If the selected estimate has no
applicable improvement, record that stop and its class. Do not automatically
open unrelated signed-log or collision-persistence programs without a
concrete new input. B08 is guidance, not an executed task or frozen E request.

## 4. Reusable continuation prompt

Continue from GNP-RS-B07 Note23 and this return. Refresh chat history,
read the result/avoid indexes and sole progress register, then read
Note23 and Review12 completely. Preserve the exact convolution-weight
boundary repair and the complete-tail estimate that gives every-real-U
means on ell≥U^(1/4+rho), 0<rho≤1/4. The result has inherited-input
analytical proof and contributing internal checking; no independent
specialist review or every-center theorem is available.

Investigate one bounded arithmetic improvement to the canonical shifted
sum (B07.31), beginning with its stated m/h ranges and Fourier weight.
Return a quantitative gain or first scoped failure. Retune the finite
head only after the complete-tail estimate is established. Keep c=1,
P≤floor(L_U²) constant on the outer block, the complete theta source and
carrier, fixed physical time inside each spatial window, and all original
Green geometry. Explain explicitly what remains between a shorter average
and an every-center estimate. Do not claim positive-threshold or time-zero
exclusion from density bounds.

Write incremental research in notes/, assessments in reviews/, the actual
status in the sole progress register, and small genuine execution records
in numerics/. Keep this conversation in its registered chat0006 history
when continuing it; use the strict recorder and bounded exact-turn final
capture. Preserve Edward Baker authorship and LLM assistance; never infer
missing actual model/effort. No new manuscript snapshot folders or numerical
campaign. Provide an updated continuation note and distinguish the suggested
next model from recorded provenance.
