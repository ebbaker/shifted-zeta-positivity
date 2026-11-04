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

The author's 4 November planning request adds a
[research plan](research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#research-plan--revision-r1-4-november-2026)
within the overview and a
[sole RGD progress register](research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md).
The plan classifies conceptual paths as **B — Astra** and fixed execution
as **E — Sol**, following the
[root workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
The initial conceptual task **RGD-B01** now has a
[bounded return](notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md):
complete-source moment bounds, a proved >2200 improvement for the specified
c0 approximation, and a joint-residual test whose sign is unmeasured.
Proof-author checking only; no new positive determinant bound or numerical
execution. Actual research model **gpt-6-astra / max**, 4 November 2026.
**Next: E04 assessment — Sol**, followed after acceptance by the fixed
two-case E03 diagnostic. The [frozen requests](research-progress/handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md)
and [continuation/model-change note](research-progress/handoffs/02_RGD_CONTINUATION_AND_MODEL_CHANGE_20261104.md)
give scope and stopping rules. Read the sole register for current status.
The earlier planning preparation remains Astra/xhigh and claimed no
mathematical result of its own.

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
