# Research overview: Connected Mellin response

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC03-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** Can the exact one-dimensional moment determinant support a controlled complete-response estimate, beginning with its large-s behavior and an explicit remaining compact problem?

## Background: the response that would raise determinant order

On the ordered three-particle chamber let
\(q=\prod_j u_j^2\), \(T=\log q\), \(w_s=q^sw_0\),
\(d\mu_s=w_s/Z(s)\), and \(A(s)=E_s h_3\). The complete signed integral is
\(M(s)=Z(s)A(s)\). Accepted order-three signed averaging gives
\(A(s)>0\) for real \(s\ge0\), hence legitimizes \(\log M\).
It does not turn \(h_3d\mu_s/A(s)\) into a positive measure.

The exact connected response is
\[
\mathcal C_3(s)=\operatorname{Var}_s(T)
+\frac{\operatorname{Cov}_s(h_3,(T-E_sT)^2)}{A(s)}
-\left(\frac{\operatorname{Cov}_s(h_3,T)}{A(s)}\right)^2.
\]
The candidate sufficient estimate is
\[
\mathcal C_3(s)\le\kappa_3(s)
=\sum_{j=0}^2\sum_{\nu\ge0}(s+j+\tfrac12+\nu)^{-2},\quad s\ge0.
\]
Its conditional order-four consequence and the weaker comparator hierarchy
are in [the parent overview](../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md). The proposed upper bound is open.
Known order-four positivity makes this a method pilot, not a new positivity
range. Association and increasing \(A\) leave the centered-square term
uncontrolled.

## The direct analytical starting point

Use the exact matrices
\[
H^{[p]}_{ij}(s)=\int_0^\infty u^{2s+2j}(2\log u)^p
\Phi^{(2i)}(u)\,du,\qquad i,j,p\in\{0,1,2\}.
\]
Determinant composition gives \(M(s)=\det H^{[0]}(s)\); column
differentiation gives \(M'\) and \(M''\) from these 27 scalar integrals.
This identity does not integrate by parts to invent noninteger
Toeplitz coefficients. It needs no source derivative beyond order four.
The endpoint and differentiated-tail obligations remain.

[Note03](../../notes/03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md) proposes a saddle/compact strategy and an unproved
large-\(s\) curvature scale smaller than the Gaussian budget. Leading-mode
or entrywise asymptotics do not establish that scale for a determinant:
leading terms can cancel, and a bound for \(M\) alone does not bound two
derivatives of its logarithm.

## Bounded research approach

Compare at most two ways to control the complete determinant and its first
two derivatives; select one. A natural first attempt is a relative
large-\(s\) expansion with an explicit nonzero leading determinant and
remainder bounds strong enough for \(MM''-(M')^2\). Keep the full theta
remainder and coalescing-node effects in any equivalent many-body analysis.

State an actual threshold \(S\) if proving a tail result. Then identify
exactly what remains on \([0,S]\), including \([0,2]\), needed for the
first substantive coefficient index. A tail theorem is worthwhile with
this explicit complement; it is not the global curvature theorem. If the
argument only supplies a formal expansion, label it accordingly and return
the exact relative-error obligation.

Alternatively, if a worked calculation defeats the pointwise envelope,
retain the integrated Gaussian and exact factorial-budget comparisons as
separate targets. Do not silently count a weaker target as success on the
stronger one.

## Controls, stopping and interfaces

Check Gaussian equality and the two-point association-only relaxation
from [the initial assessment](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md). The latter is not a theta or
Toeplitz counterexample. The [general collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) screen
any enlarged class according to its actual premises and domain; no
positive-time event by itself contradicts this time-zero claim.

Stop with a proof on its stated domain, a scoped failure, or the exact
uncontrolled signed remainder. Bounding only \(\operatorname{Var}T\),
assuming \(D_{4,k}>0\) to obtain the desired budget, or fitting a finite
grid to the proposed asymptotic scale does not complete the task. A fixed
compact certificate requires a separately specified E request after the
analytical selection; no open-ended quadrature campaign is issued here.

## Ownership, return and evidence standards

Own direct Mellin/moment-determinant analysis. MC04-B01 owns particle-coordinate Ward identities; this branch must not wait for them.

Save the bounded return under `notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.
