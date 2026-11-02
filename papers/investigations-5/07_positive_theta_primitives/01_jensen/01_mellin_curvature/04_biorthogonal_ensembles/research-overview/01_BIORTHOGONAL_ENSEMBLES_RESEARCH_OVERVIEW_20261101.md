# Research overview: Biorthogonal ensembles and inserted Ward identities

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC04-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** Does a source-sensitive integration-by-parts identity for the positive ensemble with h3 inserted constrain the full Mellin response beyond carrier positivity?

## Background: a positive ensemble with a signed observable

For \(R=\Phi''/\Phi\), the accepted global inequality \(R'>0\) makes
\[
w_{r,s}(\mathbf u)=\prod_j u_j^{2s}\Phi(u_j)
V(\mathbf u^2)V(R(\mathbf u))
\]
positive on \(0<u_1<\cdots<u_r\). Write its chamber integral as
\(Z_{r,s}\), so the full-orthant probability density is
\(w_{r,s}/(r!Z_{r,s})\). This is a biorthogonal ensemble, a product of two
determinants rather than necessarily a squared single determinant.

For \(\omega_s=u^{2s}\Phi\), one convenient pair is
\(a_i=u^{2i}\sqrt{\omega_s}\), \(b_i=R^i\sqrt{\omega_s}\).
With \(P_{ij}=\int_0^\infty a_i b_j\), determinant composition gives
\(\det P=Z_{r,s}>0\). Its particle correlations use
\[
K(x,y)=\sum_{i,j}a_i(x)(P^{-1})_{j,i}b_j(y).
\]
The inverse transpose follows this pairing convention; \(\int K(x,x)dx=r\).
The kernel need not be Hermitian. These are carrier particle correlations,
not automatically the original coefficient determinants.

The unchanged observable remains
\[
h_r(\mathbf u)=
\frac{\det[\Phi^{(2i)}(u_j)/\Phi(u_j)]_{i,j=0}^{r-1}}
{V(R(\mathbf u))},\qquad M_r(s)=Z_{r,s}E_{r,s}h_r.
\]
At order three \(h_3\) has a negative region. Positivity of \(Z\) says
nothing by itself about the inserted amplitude or its response. Gaussian
source normalization gives \(h_r=1\); this checks the construction but
removes the central theta difficulty.

## Bounded research approach

Compare at most two concrete particle vector fields for integration by
parts, then select one. Start from the inserted total derivative
\[
\sum_{j=1}^3\int_{\Omega_3}
\partial_{u_j}\{v_j(\mathbf u)h_3(\mathbf u)w_{3,s}(\mathbf u)\}
\,d\mathbf u.
\]
Derive all boundary terms before declaring this zero. Expand it into a
relation between the source log derivative, Vandermonde interactions and
derivatives of the insertion. Include \(T\) insertions or differentiate in
\(s\) only with justified domination, if that is the chosen response
consumer. State the exact hypotheses on the vector field.

Ask whether theta’s differential identities close the resulting relation,
or whether they introduce a new signed moment with no estimate. A carrier
loop equation with no \(h_3\) terms is insufficient. A nonclosed hierarchy
may still provide a useful reduction if one specific residual and the
required inequality are isolated. Repeatedly differentiating to a longer
uncontrolled hierarchy is the stopping point, not progress through closure.

## Domain and acceptance

Treat the origin, collision faces and spatial infinity. Vandermonde
vanishing does not excuse ignoring singular expressions introduced after
division; use the smooth undivided product or justified face limits.
If logarithmic insertions occur, check the endpoint behavior at \(s=0\).
Distinguish a formal Ward identity from an integrated identity whose
boundary terms and differentiation have actually been justified.

Return one complete inserted identity and its quantified gain, or the
precise residual that prevents the response estimate. This branch can
complete a useful bounded assessment without signing that residual; the
parent inequality would remain open.

## Controls and reading

Generic biorthogonal determinantal formulas establish no theta sign.
Their application to a control additionally requires increasing \(R\),
which has not been checked for all [control families](../../../../../../../result-summaries/12_collision_controls_and_screening.md). Do not
claim those controls pass or fail this premise without calculation.
Any new Ward estimate must state which additional source relation it uses.

Read [Note04, Section 4](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), [the parent response formula](../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md)
and [the inspected primary-source passages](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md) in Borodin and
Desrosiers–Forrester. Use the normalized-marginal convention recorded
there. Do not import a scaling limit, self-adjoint kernel or positivity
theorem for a different ensemble without checking its hypotheses.

## Ownership, return and evidence standards

Own inserted ensemble/Ward identities. Do not duplicate MC03-B01’s direct saddle analysis or identify the carrier partition function with M.

Save the bounded return under `notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.
