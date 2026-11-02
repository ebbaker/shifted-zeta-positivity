# Research overview: Fermionic correlators and Slater overlaps

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC02-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_FERMIONIC_CORRELATORS_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** Does the actual theta orbital family admit a noncircular operator or overlap comparison that supplies information beyond Wick’s determinant identity?

## Background: a determinant as a correlation function

For \(\mathcal H=L^2((0,\infty),du)\), set
\[
f_i=\Phi^{(2i)}/\sqrt\Phi,\qquad
g_{k,j}=u^{2(k+j)}\sqrt\Phi/(2(k+j))!.
\]
Evenness at the origin and complete-source decay give the existing
integration-by-parts identity
\(\langle f_i,g_{k,j}\rangle=c_{k+j-i}\), including the convention
\(c_n=0\) for \(n<0\). Consequently
\[
D_{r,k}=\langle f_0\wedge\cdots\wedge f_{r-1},
g_{k,0}\wedge\cdots\wedge g_{k,r-1}\rangle.
\]
The same scalar is the vacuum expectation of \(r\) annihilation operators
followed by \(r\) creation operators, with the annihilators reversed in
order. This is an exact smeared equal-time \(2r\)-field correlation, as
specified in [Note04, Section 2](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md). The geometric many-body and
fermionic pictures are this same construction.

For \(b_j=u^{2j}\sqrt\Phi\), use the wedges \(F_r\) and \(B_r\), and the
multiplication operator \(\widehat T=2\sum_j\log u_j\). Then
\[
M_r(s)=\langle F_r,e^{s\widehat T}B_r\rangle.
\]
The vectors differ. A positive Hilbert space does not make their overlap
nonnegative, and the connected response of this matrix element is not an
ordinary positive-state variance. No local interacting action, or dynamical
identification with the circle Hamiltonian, has been supplied.

## Bounded research approach

Compare at most two explicit theta-dependent relations between the
derivative and monomial orbital families. For example, assess a specified
intertwining/operator relation or a deformation of the overlap whose
derivative has a controllable signed remainder. Select one candidate and
write its domain, adjoint convention and claimed inequality before using it.

Determine whether it yields a quantitative comparison for the original
\(M_3\), preferably its complete logarithmic response. A proposed positive
operator must be constructed from independently known theta data and have
its needed property proved. Defining that property to be equivalent to the
unknown determinant sign is a reformulation, not a mechanism. Treat
unbounded operators and differentiation domains explicitly.

Keep the two states and the original amplitude. Cauchy–Schwarz bounds the
absolute overlap from above; it supplies neither its sign nor the desired
curvature comparison. Replacing the amplitude with its squared modulus,
or choosing unrelated adjoint insertions, changes the question.

## What counts as a result

Return a worked operator/overlap relation with a quantified consequence,
or a scoped failure identifying precisely where its positivity,
adjointness or domain premise breaks. An exact identity that isolates a
new source-dependent residual can be a useful reduction if the residual
is fully stated and its sign remains explicitly open.

The known negative region of the order-three insertion already rules out
an everywhere positive integrand for the unchanged wavefunctions. A
different integrated representation is not thereby ruled out. The known
order-four pointwise obstruction likewise has its stated scope; do not
promote it to an impossibility theorem for operator methods.

## Controls and reading

Wick and exterior algebra work for many smooth positive even sources,
including controls satisfying the same integrability hypotheses. They do
not distinguish theta. For a new comparison, name the additional premise
and test whether the relevant [control families](../../../../../../../result-summaries/12_collision_controls_and_screening.md) satisfy it;
do not assume they have theta’s derivative-ratio monotonicity.

Read [Note04, Sections 2–3](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), [the exact initial assessment](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md)
and the [physical bibliography](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md), especially the checked
Alexandrov–Zabrodin passages. Finite CAR algebra here does not import
convergence or positivity of an infinite-current construction. The
[previous physical-channel lessons](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md) help distinguish an
exact realization from new information about its value.

## Ownership, return and evidence standards

Own orbital/operator comparisons. Do not rederive MC01-B01’s spectrum or MC05-B01’s formal Schur algebra as the main return.

Save the bounded return under `notes/01_THETA_ORBITAL_COMPARISON_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_FERMIONIC_CORRELATORS_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.
