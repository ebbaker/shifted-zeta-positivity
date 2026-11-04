# Research overview: source overlap kernels

3 November 2026, America/New_York. Drafted for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a1a435-f885-7571-8e16-15894c91e54d`.

3 November 2026 planning revision, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual recorded **gpt-6-astra (Codex), reasoning effort max**, chat `01a1a43c-e3ab-7f73-9373-d130d40c1068`, turn `01a1a43d-98b2-7190-be5a-850c7950ff1e`. The earlier Sol/ultra line records the original synthesis; this revision adds the requested plan and progress register without a new mathematical assessment.

**Evidence and plan status.** This overview records the source-state and compact-kernel results developed in the originating discussion. The compact identities are proved in the linked derivation with same-execution algebraic checks, including two read-only same-model support agents; they have not received a separate specialist assessment. This document remains a synthesis, not a new mathematical review. The author-requested [research plan, revision 1](#research-plan--revision-1-3-november-2026) is now included below. The [local progress register](../research-progress/01_SOURCE_OVERLAP_KERNELS_RESEARCH_PROGRESS_20261103.md) owns readiness and later dispositions; the dated return below supersedes the initial unstarted status.

## Current continuation — MC09-B01 return, 3 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual
**gpt-6-astra / max**, turn `01a1a447-c6e4-7d40-9b2c-8b5eb421cd46`.
The [B01 note](../notes/01_KERNEL_MECHANISM_SELECTION_20261103.md) constructs
a positive Hermitian kernel preserving the original source-state metrics
and proves a matched-Gram preparation obstruction. Its controls keep the
complete source, moment states, ground state and actual separate Gram
matrix but relax the derivative-preparation rule; their neighboring ratio
can be arbitrarily large. This does not refute the original theta
comparison. The common-contour index shift reproduces the known signed
residual, and the specified bare inverse-source kernel has no finite
pointwise halfline limit.

Evidence is **proved in-note with proof-author checks only**. No new signed
bound or comparison range is claimed. **Next: [E] MC09-E01 — Sol**, using
[request r1 and model-change guidance](../research-progress/handoffs/01_MC09_E01_REVIEW_AND_MODEL_CONTINUATION_20261103.md).
The [live register](../research-progress/01_SOURCE_OVERLAP_KERNELS_RESEARCH_PROGRESS_20261103.md)
owns readiness. The research plan below remains as issued; its initial
B01-first routing is historical after this return. B02 has no new signed
premise from this bounded attempt.

## Scope and relation to the Hamiltonian investigation

The question is whether the original theta-derived mixed overlaps can be understood through separate source variables coupled by an analytic or geometric kernel, and whether that representation exposes additional information about the signed pairing. The compact representation below makes the separation exact. No new inequality controlling the pairing has been established.

The [open quantum dynamics investigation](../../08_open_quantum_dynamics/README.md) separately studies Hamiltonians, clocks, environments and their energy meaning. Its established finite realizations remain intact. The present investigation concerns the source wavefunctions and their mixed pairing; it requires no choice of a total Hamiltonian or interpretation of the activity parameter as physical time.

The original discussion and detailed derivations remain in [source-state Note08](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) and [kernel Note09](../../08_open_quantum_dynamics/brainstorm/notes/09_SEPARATED_CONTOUR_KERNEL_FOR_SOURCE_OVERLAPS_20261103.md). No earlier source or archived conversation is moved or duplicated.

## Canonical source and the actual states

Retain the complete theta source at source heat time zero:
\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad u\ge0,
\]
\[
c_j=\frac1{(2j)!}\int_0^\infty u^{2j}\Phi(u)\,du,
\qquad c_j=0\quad(j<0).
\tag{1}
\]
The coefficients are ordinary coefficients, not raw moments or the exponential coefficients j!c_j. The complete source is positive on the real halfline and has the established even extension and double-exponential decay needed for the source-pairing identities.

The two source-derived orbital families in L²((0,infinity),du) are
\[
f_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{\Phi(u)}},\qquad
g_j(u)=\frac{u^{2j}\sqrt{\Phi(u)}}{(2j)!}.
\tag{2}
\]
Their finite-index Hilbert membership and integration-by-parts boundary payments are inherited from the [MC02 return](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) and its [separate internal review](../../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md). The exact pairing is
\[
\boxed{\langle f_i,g_j\rangle=c_{j-i}.}
\tag{3}
\]
Both families arise from the same source: derivative preparation on one side and moment preparation on the other. They are generally different, nonorthonormal families; their labels are not identified with theta energy eigenmode labels.

For increasing finite lists I=(i_1,...,i_r), J=(j_1,...,j_r), with the convention that orthonormal wedges have unit norm,
\[
\boxed{
\left\langle f_{i_1}\wedge\cdots\wedge f_{i_r},
g_{j_1}\wedge\cdots\wedge g_{j_r}\right\rangle
=C_{I,J}:=\det[c_{j_b-i_a}].}
\tag{4}
\]
If the two wedges are nonzero, their normalized overlap is
\[
\langle\widehat F_I,\widehat G_J\rangle
=\frac{C_{I,J}}{\sqrt{\det M_I^f\det M_J^g}},
\quad (M_I^f)_{ab}=\langle f_{i_a},f_{i_b}\rangle,
\quad (M_J^g)_{ab}=\langle g_{j_a},g_{j_b}\rangle.
\tag{5}
\]
The two positive Gram determinants are part of the actual state normalization. Replacing this mixed overlap by the squared norm of a single wedge changes the observable.

The inherited all-minor sign destination is an RH-equivalent reformulation, as recorded by MC02; the present representation is not a new criterion or proof of that destination. The existing quantitative order-three pilot uses
\[
D_{r,k}=\det[c_{k+b-a}]_{a,b=0}^{r-1},\qquad
\frac{D_{3,k-1}D_{3,k+1}}{D_{3,k}^2}\le\frac{k}{k+3},\quad k\ge1.
\tag{6}
\]
This stronger neighboring-index comparison remains unproved. It is included to identify the existing signed consumer, not asserted as a consequence of the kernel formula.

## Reconstruction idea from the unpublished quaternion-forms draft

Edward B. Baker III's *Integral formulas for quaternion valued forms, and their applications to Yang-Mills theory*, dated 14 February 2014, is an **unpublished draft**, as explicitly confirmed by the author. Equation 2.3 on page 3 has the structure
\[
\int_\Omega\omega\wedge\nu
=C_n\int_{\partial\Omega}\int_{\partial\Omega}
\omega(z)\wedge K_n(z,w)\wedge\nu(w).
\tag{7}
\]
It motivates reconstructing each factor from separate boundary data, then integrating the shared original variable into a coupling kernel. Separate variables here remain coupled; no probabilistic independence or product factorization is inferred.

The draft's setting is a complex-volume pairing of holomorphic and antiholomorphic top forms. The present overlaps integrate along a real halfline. Consequently its printed Bochner–Martinelli-related kernel and constants are not substituted unchanged. The compact analogue below is derived directly using Cauchy's formula for the actual real integration measure.

The [author-supplied PDF](../../../../../../investigations-2/active/21_quaternion_theta_geometry/source-documents/QuaternionForms-Final.pdf) remains unchanged. Its checked hash, unpublished status, inspected pages and selected Cauchy source passage are recorded in [source record05](../../08_open_quantum_dynamics/references/05_SOURCE_KERNEL_DRAFT_AND_CAUCHY_20261103.md). This overview does not certify the draft as a whole.

## Exact compact-interval kernel

In the real pairing the square roots cancel:
\[
\overline{f_i(u)}g_j(u)
=\Phi^{(2i)}(u)\frac{u^{2j}}{(2j)!}.
\]
Here the canonical functions are real on the real axis. Define holomorphic factors
\[
a_i(z)=\Phi^{(2i)}(z),\qquad b_j(z)=\frac{z^{2j}}{(2j)!},
\qquad M_{ij}^R=\int_0^R a_i(u)b_j(u)\,du,
\quad R>0.
\tag{8}
\]
The canonical theta series and each fixed finite derivative converge normally on compact subsets of |Im z|<pi/8, where Re(e^(4z))>0. Thus a_i is holomorphic in this strip; b_j is entire. This reconstruction needs no global complex square-root branch or zero-free assertion for Phi.

Let Gamma_z and Gamma_w be positively oriented simple closed contours enclosing [0,R], with filled closures in the strip and positive distance from the segment. Applying [Cauchy's formula, DLMF 1.9.30](https://dlmf.nist.gov/1.9.E30), to each factor and using compact-contour Fubini gives
\[
\boxed{
M_{ij}^R=\oint_{\Gamma_z}\oint_{\Gamma_w}
a_i(z)\mathcal H_R(z,w)b_j(w)
\frac{dw}{2\pi i}\frac{dz}{2\pi i}.}
\tag{9}
\]
The source-independent coupling kernel is
\[
\boxed{
\mathcal H_R(z,w)=\int_0^R\frac{du}{(z-u)(w-u)}
=\frac{\ell_R(z)-\ell_R(w)}{w-z},\quad
\ell_R(z)=\int_0^R\frac{du}{z-u}=\log\frac{z}{z-R}.}
\tag{10}
\]
The integral fixes the logarithm branch, with ell_R tending to zero at infinity. The divided-difference sign follows by partial fractions. Its apparent diagonal singularity is removable:
\[
\mathcal H_R(z,z)=-\ell_R'(z)=\frac{R}{z(z-R)}.
\tag{11}
\]
The contours may therefore coincide without introducing a new diagonal singularity. If d_z,d_w are their distances from [0,R], then |H_R|<=R/(d_z d_w); bounded source factors and finite contour lengths justify the finite interchange.

## Exterior-product kernel

For lists I,J of length r, set
\[
\mathcal A_I(\mathbf z)=\det[a_{i_a}(z_c)]_{a,c=1}^r,
\qquad
\mathcal B_J(\mathbf w)=\det[b_{j_b}(w_d)]_{d,b=1}^r.
\]
Two finite Andréief expansions yield
\[
\boxed{
\det[M^R_{i_a j_b}]
=\frac1{(r!)^2}
\oint_{\Gamma_z^r}\oint_{\Gamma_w^r}
\mathcal A_I(\mathbf z)
\det[\mathcal H_R(z_c,w_d)]_{c,d=1}^r
\mathcal B_J(\mathbf w)
\prod_{c=1}^r\frac{dz_c}{2\pi i}
\prod_{d=1}^r\frac{dw_d}{2\pi i}.}
\tag{12}
\]
Both r! factors are retained. The final determinant has rows indexed by w_d and columns by j_b, fixing the ordering and sign. The two source families now have separate variables, coupled by the determinant of a one-particle kernel. The formula is an exact compact representation of the mixed overlap, without a quantum-mechanical interpretation being required.

## Endpoint terms and the halfline limit

At finite R, M_ij^R is generally neither c_{j-i} nor just its truncated moment. For i>0,
\[
M_{ij}^R=
\sum_{k=0}^{2i-1}(-1)^k
[\Phi^{(2i-1-k)}b_j^{(k)}]_0^R
+\int_0^R\Phi(u)b_j^{(2i)}(u)\,du.
\tag{13}
\]
Complete-source evenness and polynomial parity eliminate the origin terms. The upper endpoint terms remain at finite R. At fixed finite indices, double-exponential source decay makes those terms and the omitted real tail vanish, giving
\[
M_{ij}^R\longrightarrow c_{j-i},\qquad
\det[M^R_{i_a j_b}]\longrightarrow C_{I,J}
\quad(R\to\infty).
\tag{14}
\]
This is convergence of the compact formulas through equality with the original real integrals. It supplies no single fixed unbounded-contour formula or justification for dropping growing-contour sides. The polynomial factors b_j particularly require endpoint control. No uniformity in index, derivative order or particle number is asserted.

## Role of the coefficient encoding

The optional activity parameter gives
\[
F(v)=\sum_{n\ge0}c_nv^n,\qquad
K_v=F(vS)/F(v),\qquad
A_{I,J}(v)=\frac{v^{\sum J-\sum I}}{F(v)^r}C_{I,J}.
\tag{15}
\]
For v>0 this is a positive rescaling of each fixed determinant. It preserves signs, and its scalar factors cancel from the neighboring rectangular ratio in (6). Positive rescalings of the original orbitals likewise leave their individually normalized wavefunctions and nonzero normalized wedges unchanged.

The v construction remains useful for normalized coefficient transfer and the earlier dynamical realization. It has supplied no additional bound for the missing signed source comparison. This is a statement about the evidence acquired so far, not an exclusion of every possible estimate involving v. The present kernel identities can be stated directly for the source pairing without assigning v the meaning of physical time. Further Hamiltonian and energy-interpretation work remains in the separate open-quantum-dynamics folder.

## Evidence and mathematical limits

The compact double-contour and determinant-kernel identities are proved in [kernel Note09](../../08_open_quantum_dynamics/brainstorm/notes/09_SEPARATED_CONTOUR_KERNEL_FOR_SOURCE_OVERLAPS_20261103.md), with same-execution analytical checks. The original source/exterior overlap retains MC02's distinct internal review status. This overview adds no new mathematical validation.

The kernel representation has not supplied a sign for the complex-contour integral, a new neighboring-index bound, a Mellin-curvature range, or RH progress. Positivity of a kernel at real exterior points does not establish a sign on the enclosing complex contours. A generic representation alone supplies no discriminator between the canonical source and another analytic source satisfying the same reconstruction hypotheses. No uncomputed sign or analytic premise is assigned here to another control family.

Read with the [result index](../../../../../../../result-summaries/README.md), especially [theta identities/bookkeeping](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../../avoid/README.md), particularly [target reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [unchecked imports](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). The research plan below preserves these limits and uses the same evidence standards.

## Research plan — revision 1, 3 November 2026

**Objective.** Determine whether the separated source representation exposes a
theta-dependent relation that controls the original mixed overlap or its
neighboring-index comparison. The first result may be a usable estimate, an
exact source-dependent residual with its unpaid bound stated, or a scoped
failure of the selected mechanism. Reproducing (9)–(12) is baseline work;
it is not a new signed estimate.

The [research-progress register](../research-progress/01_SOURCE_OVERLAP_KERNELS_RESEARCH_PROGRESS_20261103.md)
owns live status for the new **`MC09-`** tasks. This section owns the research
plan. It supersedes the earlier setup's deliberate absence of a plan and
local task namespace, following the author's present request. Earlier MC08
notes and task identities remain at their original homes. Hamiltonian,
clock, environment and energy-model work remains with MC08.

**Default next task: [B] MC09-B01 — Astra.** The conceptual choice is which
additional source relation could make the generic kernel informative about
the signed pairing. Follow the repository's [B/E workflow](../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md):
B identifies a mechanism or resolves a structural question; E executes or
checks a specified argument. Edward Baker chooses the actual model and
effort. These recommendations do not dispatch work or change settings.

### Fixed observable and measurable destination

Keep the complete canonical source at heat time zero, the ordinary
coefficients (1), both preparations (2), the actual Gram normalization (5),
and the signed exterior pairing (12). The initial estimating pilot is
\(r=3\), \(I=(0,1,2)\), \(J=(k,k+1,k+2)\). Its target is exactly (6).
With the inherited positive order-three denominator, an equivalent test is
\[
\mathfrak Q_k:=kD_{3,k}^{\,2}-(k+3)D_{3,k-1}D_{3,k+1}\ge0,
\qquad k\ge1.
\]
This names the consumer; it acquires no bound. Report a proved range of k,
an explicit remainder allowance or margin, or a precisely failed premise.
The triangular k=0 anchor and the k=1 comparison must be retained. An
asymptotic estimate leaves its finite complement open.

The [parent Mellin overview](../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md)
records the conditional order-four consequence and the stronger continuous
Gaussian-curvature target. Order-four positivity is already known; this is
a pilot of an estimating mechanism. A kernel proof of the discrete ratio
does not establish the pointwise Mellin bound. If continuous tilts are
chosen, first supply the exact bridge to the parent's M(s), normalization
and real-tilt positivity; include s in [0,2] and the unbounded tail. Do not
insert noninteger powers into (12) without their branch and endpoint work.
No fixed-order result establishes the all-minor destination.

### MC09-B01 — choose one source-dependent mechanism

**B; recommended Astra:** selecting the useful relation and its signed
consumer remains a structural decision. Read Note08, Note09, the MC02
return and review, and the parent comparison before selecting it. The
inherited claims retain their present evidence status during exploration;
MC09-E01 will separately check the kernel/interface used by the attempt.

Compare **at most two concrete candidates**, then work one far enough to
state its exact obligation. Two starting options are:

1. **Conjugate-contour comparison.** Test whether reflection of the contour
   variables yields a useful Hermitian reference pairing together with an
   exact correction for the different source preparations. Keep contour
   orientations, conjugations, measures and both Gram metrics explicit.
   Relating the contours is not permission to identify their independent
   integration variables. Positivity of the reference kernel alone cannot
   sign the original mixed pairing.
2. **Joint neighboring-index comparison.** Use (12) with common contour
   geometry for k-1, k and k+1, seeking one complete theta identity or
   differential relation that constrains their joint signed contribution.
   Isolate how the derivative-source determinant and the moment determinant
   interact with the kernel. Separate absolute bounds on each factor must
   be shown to pay the full consumer, not simply listed as estimates.

For either candidate, identify the extra premise independently of the
desired determinant sign, its source/domain, and the precise place where
it enters the argument. Check the applicable controls below before
presenting it as a sign mechanism. A different geometric reconstruction
may replace one of these two options if its measure, normalization and
reason for improving the same consumer are stated; importing the 2014
draft's printed kernel unchanged is not such a derivation.

**Return:** a bounded note in `notes/` with the candidate comparison, one
selected mechanism, an explicit lemma or residual identity, control
disposition, and the exact missing inequality. If viable, freeze the
analytical obligations and input versions for E01 and B02. If neither
candidate supplies an additional usable premise, return the scoped failure
and park this attempt. A general literature survey, a renamed all-minor
condition or a list of speculative kernels does not complete B01. No
coefficient scan or new Hamiltonian model is part of it.

### MC09-E01 — audit the compact representation and selected interface

**E; recommended Sol:** check fixed derivations after B01 freezes its return.
The output is a separate assessment under `reviews/`, with accept, correct
or unresolved dispositions at the stated scope. It must cover:

- complete-source strip analyticity and cancellation before complex
  continuation, without assuming a zero-free square root;
- the divided-difference sign, logarithm branch, removable diagonal,
  contour orientations, compact Fubini, determinant ordering and both r!
  factors in (9)–(12);
- the actual mixed-state normalization, all finite-R boundary terms in
  (13), the j<i case and the fixed-index meaning of (14);
- the selected new relation, every positivity/adjoint premise, and the
  exact connection of its residual to the original consumer.

Use direct r=1 and r=2 algebra as normalization checks and the r=3 pilot as
the consumer check. These checks do not prove an inequality. Permit routine
algebraic corrections and standard fixed-index domination arguments; do
not replace the source or choose a new mechanism. A substantive failed
premise returns to B01 as a dated conceptual revision. A verified scoped
failure can close this attempt without starting B02.

### MC09-B02 — work the selected signed comparison

**B; recommended Astra:** the joint inequality remains the difficult
research step. Start only after B01 supplies a viable source-dependent
obligation and E01 clears the inputs it actually uses. Work **one selected
mechanism at order three** to a bound, a conditional reduction with its
remaining term fully specified, or a proved failure in a named class.

Start with the compact identities. Any passage to the halfline must bound
the complete-source mode remainder, the real u-tail, upper integration-by-
parts terms and determinant error. For a ratio, also justify its denominator
and propagate error through the whole comparison. Fixed-index decay is not
uniformity in k. A result for all k requires a stated large-k argument and
payment of the finite complement. A global contour deformation is optional,
and must pay every side and limit if used; it is not required merely to use
the compact formula.

If a positive reference or positive region is introduced, retain its signed
complement. Preserve correlations between the three neighboring overlaps
where the proposed bound needs them. The existing negative spatial
insertion forbids assuming pointwise positivity for the unchanged
wavefunctions; it does not exclude every integrated kernel estimate.

**Return:** a proof/obstruction note with exact domain, constants or explicit
unpaid terms, controls, and comparison with (6). If routine derivation or
finite computation becomes the sole remaining work, hand that specified
work to E02 immediately. Stop if the argument assumes the target sign,
replaces the mixed overlap by a norm square, discards a boundary/signed
term, or requires an uncontrolled derivative/order hierarchy. Failure of
one sufficient comparison does not close every kernel approach. No automatic
arbitrary-order extension follows this pilot.

### MC09-E02 — conditional finite verification

**E; recommended Sol:** reserved for a fixed residual or allowance returned
by B02. It is **optional and gated**, not an issued numerical campaign.
Before it becomes ready, put one bounded request in
`research-progress/handoffs/` specifying the formula and input hashes, finite
indices or compact domain, contour/cutoff choices, all analytic complements,
precision and refinement ceilings, runtime/work cap, output, and exact
acceptance condition. B02 must supply the actual values of those limits;
leaving them open is not an execution contract.

For a finite-contour diagnostic, compare with the same truncated real
integral, including its endpoint terms. Label floating feasibility results
as numerical. A claimed certificate must include outward-rounded error
enclosures for source evaluation, quadrature, real/complex tails,
determinant arithmetic and normalization as applicable. A finite grid does
not cover a continuum or all k. Keep code and small records in `numerics/`
and follow [LARGE_FILES.md](../../../../../../../LARGE_FILES.md) for derived
data. Stop at the declared limits; an inadequate mathematical allowance
returns to B02, not to an enlarged precision or parameter campaign.

### MC09-E03 — assess the result and integrate its scope

**E; recommended Sol:** separately check the frozen final mathematical
return and any E02 evidence, then record the disposition in the local
register and README. Distinguish proof-author checks, separate internal
reviews and specialist review. For an early stop already assessed by E01,
reuse that assessment and perform only the needed integration.

Record exactly which domain or obligation changed. A partial estimate keeps
its complement unpaid; an exact reduction keeps its residual open; a
negative result keeps its source, contour and comparison class attached.
Update the concise local `DRAFT_HISTORY.md`. Propose a repository summary
update only for a result meeting the repository's evidence rules, through
the shared-file writer. A successful order-three attempt still needs a new
explicit conceptual decision before extending to growing particle order.
No manuscript or snapshot is required by this plan.

### Controls and decision gates

The [collision-control summary](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
supplies the source families and evidence. For each proposed premise,
record **satisfied / failed / unestablished / outside the stated class**,
with a source or calculation. This planning revision performs no new
control experiment and assigns no uncomputed sign to a control.

| Control | Required comparison with the proposed argument |
| --- | --- |
| Euler-factor perturbations | Check the actual analytic domain, reconstruction and extra theta premise; generic positive/even source data alone are insufficient for a global conclusion. |
| Weighted-square endpoint controls | Check every endpoint order used in integration by parts. Matching finitely many reflection conditions does not supply full-source evenness. |
| Reflected super-Gaussian control | Test the specific source-dependent relation beyond evenness, analyticity and Gram positivity. Do not assume that its quantitative ratio agrees with theta's. |
| Smooth shape and positive-primitive controls | Check whether the claimed contour analyticity is available before applying the representation; otherwise mark that analytic application outside scope and still screen any shape-only claim on its own premises. |

Use the Gaussian case only as a normalization/comparator check where its
hypotheses apply. For a broad collision-exclusion conclusion, a control
sharing every premise is decisive. A positive-time collision alone is not
a counterexample to the time-zero order-three comparison on a specified
domain. Conversely, failure of literal theta reconstruction does not show
that a weaker quantitative estimate discriminates that control. Record the
premise actually used, following [avoid/02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).

**Continue** when the selected relation yields new quantitative information
or a concrete source-dependent obligation whose estimation is specified.
**Return for conceptual revision** when the source, observable, mechanism
or intended domain must change. **Park the selected attempt** when it only
reproduces the old sign condition or reaches a scoped obstruction. Keep
these decisions distinct from proving or disproving the wider destination,
as in [avoid/01](../../../../../../../avoid/01_restating_the_target.md) and
[avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

### Records and ownership

Each return records the actual model/effort, date, request revision, exact
inputs, argument or failed cases, domain and unpaid complement, controls,
review status, and one next declared B/E task. Use `notes/` for incremental
research, `numerics/` for code and small records, and `reviews/` for
assessments. Freeze issued requests and add dated returns rather than
rewriting their historical claims. The local register is the sole owner of
MC09 readiness; the overview is not a second live ledger.

Only this branch's files belong to its writer. Read MC02, MC08, parent
results, the unpublished source draft and shared references as inputs;
shared-index changes require the parent's coordinated update procedure.
Preserve each existing chat's registration. New kernel chats register under
this folder's `chat-histories/` using the [history workflow](../../../../../../../tools/CHAT_HISTORY.md).
