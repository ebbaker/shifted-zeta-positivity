# Localized zero marginals: independent research and collision interfaces

8 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual recorded model and effort are unavailable. TND-OC-E11 corrected the destination in OC chat0006; B09 subsequently completed its design pass in redirected thread 01a1bddb-de9d-7221-8f78-7a510e8e4fb9. E10 subsequently returned its in-note proof (runtime GPT-6.1 Sol, effort unavailable).

## Purpose and corrected destination

The author intended this renewal for **02_localized_zero_correlations**.
The earlier request named 02_hamiltonian_auxiliary_dynamics by mistake.
This overview and its [plan02](../research-plan/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PLAN_20261108.md)
replace the current-priority role of OC overview01/plan01. Those documents
remain historical sources. [Progress02](../research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md)
is the sole live OC register. [Correction Note15](../notes/15_TND_OC_PRIORITY_DESTINATION_AND_GREEN_INTERFACES_20261108.md)
records the auxiliary restoration and the Green advisory integration.

The scientific question is: **what new arithmetic information can we
prove about the full localized pair and higher marginals of the canonical
zeros, including their imaginary coordinates and multiplicities?**
Marginals remain an independent, high-risk, potentially high-reward
program. A useful correlation theorem or controlled evolution result
can succeed before a collision exclusion is available.

Across the split, the author's first priority is constraining collisions.
The separate [OA investigation](../../03_collision_constraints/README.md)
starts with a collision event and the estimate needed to constrain it.
The [OG investigation](../../01_green_potential_resolvent/README.md)
develops the Green potential. OC supplies a possible statistical input;
OA and OG need not wait for its entire marginal program. Each branch's
live register owns its tasks. This correction does not rewrite the parent
operator overview or change those branches' current statuses.

## 1. What the objects are

Keep the complete, unmodified theta source and inherited normalization:
\[
 p(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}}
     =\tfrac12e^u[\vartheta(e^{4u})-1],\qquad
 p''-p=8\Phi,\qquad p'(0)=-\tfrac12,
\]
\[
 H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
 \qquad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda .
\]
With \(\mathcal P_\lambda(z)=\int_0^\infty p(u)e^{\lambda u^2}\cos(zu)\,du\),
\[
 8H_\lambda=\tfrac12+(2\lambda-1-z^2)\mathcal P_\lambda
       +4\lambda z\mathcal P_\lambda'-4\lambda^2\mathcal P_\lambda'',
 \qquad 8H_0=\tfrac12-(1+z^2)\mathcal P_0 .
 \tag{1}
\]
These are inherited identities; see [Note14 §2](../notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md)
and its parent source. The source variable \(u\), integer index \(n\),
zero coordinate \(z\), and observation center \(X\) have different roles.
Taking a zero marginal does not mean integrating out \(u\) or \(n\).

At fixed \(\lambda\), count zero labels with multiplicity:
\[
 \nu_\lambda=\sum_j\delta_{z_j}
          =\frac1{2\pi}\Delta\log|H_\lambda|.
 \tag{2}
\]
For a compact window \(W\) and normalized planar Gaussian \(G_\epsilon\),
write in physical coordinates
\[
 q_{X,j}(u)=W(z_j-X)G_\epsilon(u-(z_j-X)),\quad
 r_X(u)=\sum_jq_{X,j}(u),
\]
\[
 R_{2,X}(u,v)=\sum_{j\ne k}q_{X,j}(u)q_{X,k}(v)
             =r_X(u)r_X(v)-d_X(u,v),\qquad
 d_X=\sum_jq_{X,j}(u)q_{X,j}(v).
 \tag{3}
\]
The self term contains \(W^2\). Distinct labels at a multiple zero remain
distinct. Higher factorial intensities sum over mutually distinct labels.
For an unweighted finite configuration, dividing by the appropriate
falling factorial gives normalized marginals. Windowed intensities are
not automatically probability densities. Center averaging is a declared
empirical probability law, not an assumed random-matrix ensemble.

The accepted fixed baseline is [B06 Note11 §1](../notes/11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md):
\(\lambda=0\), fixed finite \(T\ge10\), \(X\) uniform on \([T,2T]\),
physical window width \(h=1\), \(\ell=\min(1,4\pi/\log T)\),
\(\epsilon=\ell/4\), and the specified unfolding and compact observation
square. Each fixed \(T\) has positive smoothing width. This is not a
height-uniform theorem or an unsmoothed limiting law. B09 explicitly
extends the time range to [0,1/2] for its proposed evolution bound,
using the parent's assessed uniform strip/count/exterior inputs;
[E10 Proof17](../notes/17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md) proves the full-pair extension at proof-author scope.

## 2. Where arithmetic enters, and what remains missing

Equations (1)–(2) give, for compact smooth \(\phi\),
\[
 \langle\phi,\nu_0\rangle
 =\frac1{2\pi}\int
  \log\left|\tfrac12-(1+z^2)\mathcal P_0(z)\right|
  \Delta\phi(z)\,dA(z).
 \tag{4}
\]
The primitive therefore enters **inside a logarithm of an oscillatory
expression**, not as a positive marginal density. Positivity of \(p\)
does not control that expression's small values.

For \(\phi_u(\xi)=W(\xi)G_\epsilon(u-\xi)\),
\(L_X(\xi)=\log|H_\lambda(X+\xi)|\), and
\(D_{u,v}=\Delta[W^2G_\epsilon(u-\cdot)G_\epsilon(v-\cdot)]\),
the connected factorial function is exactly
\[
\begin{split}
 C(u,v)&=\mathbb E_XR_{2,X}(u,v)-\mathbb E_Xr_X(u)\mathbb E_Xr_X(v)\\
 &=\frac1{4\pi^2}\iint\Delta\phi_u(\xi)\Delta\phi_v(\omega)
       \operatorname{Cov}_X(L_X(\xi),L_X(\omega))\,dA\xi\,dA\omega\\
 &\quad-\frac1{2\pi}\int D_{u,v}(\xi)\mathbb E_XL_X(\xi)\,dA\xi .
\end{split}
 \tag{5}
\]
This is [Note14 (6)](../notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md),
in physical coordinates; the fixed unfolded version retains its Jacobians.
For the full pair, use the same-center product expectation in the first
integral. Arithmetic must supply useful joint information about these
logarithms, or an alternative estimate of the same marked quantity.
Individual source bounds and a difference-only projection do not supply
a general two-position function.

The existing transfer theorems already pay source truncation,
regularization, Fourier and center-edge errors at their specified scope.
Their missing input is an acquired canonical mixed-source array or
stronger contracted estimate. Repeating the transfer is not progress on
that missing input. Nor does a finite evaluator that first certifies the
zeros independently constrain their unknown configurations; it can still
be a useful benchmark.

## 3. What has actually been established

| Work | Preserved evidence and limitation |
| --- | --- |
| E01/E02 | Compact logarithm-to-zero-statistic transfer, accepted after one bounded support correction; no favorable signed canonical value |
| B02/B03/B04 | Scoped scalar-route obstructions and deterministic marked-pair transfer; author checks only for the unassessed claims; E03/E04 remain pending |
| B05/E06/E07 | Full Gaussian factorial hierarchy, common-center covariance and two-sided pair approximation; E07 accepted after one bounded correction, including a width floor |
| B06/E08 | Fixed center law and joint-source/Fourier interfaces; all eight fixed claims accepted unchanged internally; no canonical moment array or profile |
| B07 | Conditional complete-divisor/Gaussian evaluator with common analytical error \(5249/2^{24}<1/3000\) under its fixed caps at \(T=1000\); author checking only; no execution |
| B08 | Arithmetic/marginal/collision diagnosis and author-directed split; elementary scoped diagnostics, proof-author checking only |
| B09 | Two-candidate design pass; full marked pair/connected evolution contract selected. Design pass only, with the global proof now in E10 |
| E10 | Proved in-note at fixed blur and finite T. Full marked time bounds and integrated exterior errors, accepted unchanged in the internal same-model E12 assessment |

The [historical register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
retains every task, source and assessment. These are internal LLM evidence
levels with shared premises, not independent specialist validation.
The current manuscript remains an existing source; this renewal adds no
manuscript milestone or canonical estimate.

## 4. Collision applications: specify the input being requested

The [Green advisory, §§2–5](../../01_green_potential_resolvent/brainstorm/notes/10_TND_OG_COLLISION_DYNAMICS_AND_PARALLEL_PROBES_20261108.md)
sharpens the exchange between projects. Its elementary interfaces have
proof-author checking only. [Note15](../notes/15_TND_OC_PRIORITY_DESTINATION_AND_GREEN_INTERFACES_20261108.md)
records their qualified adoption here.

**Time and event.** In forward collision time
\(h(t,z)=H_{\lambda_{\rm ref}-t}(z)\), \(h_t=h_{zz}\).
A generic double event creates a nonreal pair on the smaller-\(\lambda\)
side, with height of order \(\sqrt{t-t_*}\).
A \(\lambda=0\) statistic cannot be used at a different event time
without a same-time estimate or quantitative transport. Event-dependent
local expansions do not provide a uniform time/height tube. A finite
isolated-double result does not cover all multiplicities or heights;
a real multiple zero at time zero is compatible with RH.

**Selected-pair dynamics.** For an isolated real pair with
\(h=(z-r_-)(z-r_+)F\), let \(q=(r_+-r_-)^2\). Then
\[
 q'=-8-4qB,\qquad
 B=\int_0^1(\log F)_{zz}(r_-+u(r_+-r_-))\,du .
 \tag{6}
\]
An upper bound \(B\le b\) gives a finite lifetime comparison only with an
earlier gap and a time/isolation budget:
\[
 q(0)>8E_b(\Delta),\qquad
 E_b(\Delta)=
 \begin{cases}(e^{4b\Delta}-1)/(4b),&b\ne0,\\ \Delta,&b=0.\end{cases}
 \tag{7}
\]
Bounded \(B\) at a presumed event alone is compatible with collision.
A finite-cloud pair-conditioned average of \(B\) can require a three-point
factorial statistic, a pair-mass denominator and information about the
other zeros. Integrability, count moments and the canonical exterior
limit must be paid. A valid uniform exterior bound may bypass full
three-point reconstruction; no automatic two-point closure is assumed.

**A two-point Green consumer.** On an admissible slice in the justified
strip, let \(J_\lambda(X)=\langle g_X,\nu_\lambda\rangle\). Then
\[
 J_\lambda(X)^2
 =\langle g_X^2,\nu_\lambda\rangle+
   \langle g_X\otimes g_X,\alpha_{2,\lambda}\rangle .
 \tag{8}
\]
If the event forces an upper zero of depth at least \(d\) within distance
\(r\) of centers in \(A\subset I\), a fully paid arithmetic upper bound
\(U\) contradicts that event only if
\[
 U<\frac{|A|}{|I|}
       \left[\frac{d\sin(\pi/8)}{\cosh(\pi r/8)}\right]^2 .
 \tag{9}
\]
The visibility fraction and its rates are derived from the event.
Connected covariance alone omits parts of (8). Smoothed OC data additionally
pay bias, real-zero background, spatial/observation tails, unfolding and
both intensity errors. A contracted estimate can suffice for this scalar
application without reconstructing the whole pair profile.

At fixed blur, the two-label diagnostic in Note14 has profile difference
\(O_\epsilon(d^2)\) while inverse-square interaction is \(O(d^{-2})\).
This limits an inference with fixed positive error on that finite class;
it does not rule out exact inversion, shrinking blur, stronger arithmetic
input or statistical collision methods in general.

## Gaussian height window for the theta pair marginal

9 November 2026 update prepared for Edward Baker with OpenAI Codex assistance. Runtime GPT-6.1 Sol, reasoning effort unavailable.

The author clarified that the Vandermonde belongs in a model joint
density whose marginals can be compared with empirical zero marginals.
The proposed Gaussian here is a height observation weight on the
canonical zeros. It has a separate width from the planar Gaussian
that smooths the observed locations, and the center law stays uniform
on \([T,2T]\). The pair weights factor exactly into a Gaussian in the
midpoint relative to the center and another in the height difference.
The full blurred profile also has an exact finite center integral per
pair, using the shifted Gaussian centers. Both imaginary marks and
the distinct-label convention are retained.

[Note18](../notes/18_TND_OC_GAUSSIAN_HEIGHT_WINDOW_AND_THETA_SOURCE_20261109.md) gives the kernel identities, explicit omitted
zero-weight bounds and a noncompact log-source transfer justified by
the parent safe-line estimate. The Gaussian convolution identity
for the linear \(H_\lambda\) shifts Newman time. The zero density
still depends on \(\log|H_\lambda|\), and the pair depends on two
such log fields at the same center. The identities and convergence
bounds prepare an estimate but do not give a canonical profile.

**B10 r1 is complete at scoped missing-input/decision scope.**
[Note19](../notes/19_TND_OC_B10_R1_GAUSSIAN_CONTRACTION_AND_MISSING_ESTIMATE_20261109.md) compares the full contraction with one
separation projection retaining both marked test factors. It pays
blur/center integration and spatial/frequency tails, but acquires no
canonical joint estimate or cost advantage. Its local positive-weight
log-remainder lower bound concerns one absolute approximation method.
All new calculations have proof-author checking only. Current thread
settings recorded for this return are gpt-6-astra/max; per-turn backend
configuration is unavailable.

**B10 r2 is complete at analytical design/conditional-contract scope.**
The author's next request activated that source-mechanism search.
[Note20](../notes/20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md)
selects complete contour counts and first complex moments. Exact cluster
centroids cancel the linear Taylor terms in the unchanged Gaussian
projection; an explicit theta/Jensen estimate pays the omitted divisor.
At T=1000, the frozen count, diameter, centroid and arithmetic gates
imply a projected enclosure of radius <1/200. This is **proved in-note,
proof-author checked**, with exact-rational constant checks only.
No canonical count, centroid or value has been acquired.

The finite evaluator inspects the complete source. It does not supply a
general same-center correlation law or constrain unknown configurations
independently of that inspection. It retains complex marks and multiple
labels. No runtime saving or collision exclusion is claimed.

The [plan](../research-plan/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PLAN_20261108.md)
and [Continuation23](../continuation-notes/23_TND_OC_AFTER_B10_R2_CLUSTER_MOMENTS_AND_MODEL_CHANGE_20261109.md)
record the handoff to the fixed **E13 r1 / GPT-6.1 Sol** proof check
and certified pilot. The proof and all work caps are frozen in
request27; a named failed gate can complete that bounded execution.
For this r2 update: Edward Baker, substantial OpenAI Codex assistance,
OC chat0009, recorded thread settings gpt-6-astra/max; per-turn backend
configuration unavailable. E10/E12's time bound applies to the earlier
compact window. E09 remains a separate optional compact-window benchmark.

**E13 r1 is complete at named failed-gate scope.**
[Note21](../notes/21_TND_OC_E13_R1_GAUSSIAN_PROJECTION_EXECUTION_20261109.md) records the certified 388-label census and
91 centroid enclosures. The shared source-call cap stopped the run
during moments. [Continuation24](../continuation-notes/24_TND_OC_AFTER_E13_AND_MODEL_CHANGE_20261109.md)
recommends **B10 r3 / GPT-6 Astra** to decide whether the certified
cell census can pay the projection-width gate through interval evaluation.

## 5. Priorities, controls and next decision

**E12 r1 is complete.** [Review14](../reviews/14_TND_OC_E12_R1_FULL_MARKED_PAIR_CLAIM_ASSESSMENT_20261108.md) accepts the six
E10 claims unchanged at their stated scope. The proof's additive time
allowance transports an independently supplied approximation with a
prescribed height cost. E09 remains optional for a finite canonical
benchmark, and E03/E04 remain separate pending assessments.
[Continuation20](../continuation-notes/20_TND_OC_AFTER_E12_FULL_PAIR_ASSESSMENT_AND_MODEL_CHANGE_20261108.md) gives the objective and
model guidance. The proof assessment does not supply a new signed
estimate or canonical initial data.

Read the [result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), especially
[theta14](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[target01](../../../../../../avoid/01_restating_the_target.md),
[premise02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [volume20](../../../../../../avoid/20_volume_without_a_gain.md).
The inherited screen is [Note14 §6](../notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md);
the B09 evolution-specific screen is [Note16 §6](../notes/16_TND_OC_B09_FULL_PAIR_EVOLUTION_DESIGN_20261108.md).
Generic marginal identities and heat laws admit the controls. A proposed
estimate must identify the actual used premise or quantitative allowance
that separates each relevant witness; merely naming the theta source
does not establish that separation. No new exclusion is proposed here.
