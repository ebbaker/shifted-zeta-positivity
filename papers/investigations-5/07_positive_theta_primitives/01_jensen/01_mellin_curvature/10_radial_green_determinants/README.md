# Radial Green determinants

4 November 2026, America/New_York. Drafted for **Edward Baker** with
substantial LLM assistance; actual recorded **gpt-6-astra (Codex),
reasoning effort xhigh**.

This investigation develops the radial Green representation of the
canonical theta coefficient determinants. Its mathematical starting point
is the transfer of derivatives from the theta source to explicit
symmetric polynomial probes, with every inner-boundary contribution
retained. The resulting integrals contain the undifferentiated positive
theta primitive.

The author selected this direction after the Green derivation in
[brainstorm Note06](../brainstorm/notes/06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md).
The radial and determinant identities in Sections 1–6 are the inherited
foundation. The later thermodynamic interpretations in that note remain
background discussion; this investigation develops the equations without
requiring an equilibrium ensemble, a particle-number interpretation, or
a chosen Hamiltonian. A physical interpretation can be reconsidered if
the mathematical structure motivates one.

Read the [research overview](research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md)
for the source normalization, scalar Green identity, primitive moments,
complete determinant boundary expansion, low-order example and scope.
The existing derivation has same-assistant analytical and exact rational
algebra checks. It has not supplied a new determinant sign estimate.

The author's 4 November revision centers the
[research plan](research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#research-plan--revision-r2-4-november-2026)
on the induction mechanism and error control with increasing index.
The [sole RGD progress register](research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md)
tracks current evidence and readiness.
The plan classifies conceptual paths as **B — Astra** and fixed execution
as **E — Sol**, following the
[root workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
Numerical work is restricted to testing predeclared hypotheses about the
mechanism; the main deliverable is the overall analytical argument.

The initial conceptual task **RGD-B01** produced the
[boundary-preserving comparison](notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md).
[E04 Review01](reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md)
now accepts all eight analytical obligations without correction, under
different-model internal review with shared premises. The fixed
[E03 return](notes/02_RGD_E03_R1_TWO_CASE_FIRST_MODE_DIAGNOSTIC_RETURN_20261104.md)
is favorable at both k=1,4: q/R about 1375.6 and 2429.8, stable at 80/120
digits. This is floating feasibility, not a certified positive determinant
bound or new coefficient range. Actual assessment/execution **Sol/ultra**,
4 November 2026, chat0003; the original B01 research remains Astra/max.

[E02 Note03](notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md)
now certifies Q3,1>=L1,2>7e-23 and Q3,4>=L4,2>1e-74, including compact
acquisition, source, spatial and rounding errors. A single 384-bit
Arb/FLINT pass and exact rational record propagation succeeded. Actual
**Sol/ultra**, chat0003, 4 November 2026. This quantitative finite payment
has [author checks](reviews/02_RGD_E02_R1_CERTIFICATE_SELF_ASSESSMENT_20261104.md);
no new positivity range or index/order extension is claimed.

[E04 r2 Review03](reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md)
now accepts all eight checks without correction. This is same-assistant/
same-model internal assessment with fresh contributing checks and shared
premises; no integration was repeated or specialist independence claimed.

**B03 preparation and E02 r2:** Astra's
[Note05](notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md)
supplies the first-next-order lemma, and the completed
[Note06 verification](notes/06_RGD_E02_R2_FIRST_NEXT_ORDER_RETURN_20261104.md)
checks its fixed six-input box and full degree-eight norm/margin chain.
Exact rational arithmetic from the accepted acquisition gives
R4,1/q4,1*<1/15 and Q4,1>=L4,1>3e-31. One 0.024-second standard-library
run used zero integrand evaluations. The
[analytical assessment and author checks](reviews/04_RGD_E02_R2_ANALYTICAL_ASSESSMENT_AND_AUTHOR_CHECKS_20261104.md)
retain shared acquisition/library trust; this is not specialist-independent
review or a new positivity range. Actual execution Sol/ultra, chat0003.

**Next: [B] RGD-B03 r2 — Astra**, investigate a quantitative induction
hypothesis, its propagation in order, and complete error control over the
index range. The [current continuation/model-change guide](research-progress/handoffs/10_RGD_B03_R2_INDUCTION_INDEX_ERROR_AND_MODEL_CONTINUATION_20261104.md)
replaces the former default of another finite-application assessment.
E04 r3 remains available as optional evidence maintenance. An all-order
theorem is open; further low-order checks are not prerequisites for
investigating it. Earlier requests, results and accepted inputs are intact.
Plan/navigation revision: 4 November 2026, **gpt-6-astra / max**, chat0002,
prepared for Edward Baker with substantial LLM assistance.

## Mathematical starting point

With \(R=e^{2u}\),
\[
A(R)=\sum_{n\ge1}e^{-\pi n^2R^2},\qquad
p(u)=R^{1/2}A(R),\qquad
\Phi(u)=\tfrac12R^{5/2}\Delta_3A(R).
\]
For \(m_j(u)=u^{2j}/(2j)!\), define \(c_j=\int_0^\infty\Phi m_j\)
and \(d_j=\int_0^\infty p m_j\), with negative indices zero. Then
\[
c_j=\frac{\delta_{j0}}{16}+\frac{d_{j-1}-d_j}{8},\qquad
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}.
\]
The overview gives the symmetric probes that express \(D_{r,k}\)
as a finite sum of volume and boundary integrals. For \(k\ge r\),
only the full-volume term survives. For \(k<r\), endpoint terms
generally remain.

## Evidence and related work

- [Full derivation, Note06](../brainstorm/notes/06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md), Sections 1–6: inherited identities and boundary accounting.
- [Exact algebra checker](../brainstorm/numerics/radial_green_determinant_check.py) and [execution record](../brainstorm/numerics/RADIAL_GREEN_DETERMINANT_CHECK_20261104.json): 25 finite cases checking formal identities and factors, not theta positivity.
- [Radial investigation Note73](../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md): the earlier scalar Green transfer and its control screen.
- [Mellin-curvature program](../README.md) and [Jensen program](../../README.md): the parent determinant and order-comparison questions.
- [Source overlap kernels](../09_source_overlap_kernels/README.md): a separate reconstruction of the same coefficient pairings through source kernels.
- [Open quantum dynamics](../08_open_quantum_dynamics/README.md): earlier physical and dynamical constructions; no such model is a premise here.

Existing notes and computations retain their original locations.
Later derivations belong in notes/, code and small records in
numerics/, and assessments in reviews/ when those materials are added.
The [chat-history guide](chat-histories/README.md) links the originating
conversation at its existing home and this investigation's local planning chat.

The [result index](../../../../../../result-summaries/README.md),
[theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
and [avoid index](../../../../../../avoid/README.md), especially
[reformulations](../../../../../../avoid/01_restating_the_target.md) and
[geometric realizations](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
govern the distinction between an exact representation and a new estimate.
