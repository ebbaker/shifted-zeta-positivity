# Arithmetic storage: program, goals, and first-prime benchmarks

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Reasoning effort:** not exposed in this session; not inferred.  
**Repository baseline:** `6a6e2b9e40fd01f142264071c95d41cfeed9d814`, together with the uncommitted 24 September cross-program assessment.  
**Status:** research program and handoff. This note organizes existing results,
corrects the earlier assessment's append status, and specifies new bounded
questions. It supplies no new numerical certificate, sign theorem, or physical
realization. Mathematical formulas below are inherited identities or elementary
bookkeeping; proposed estimates remain open.

## 1. Purpose and place in the broader program

The central question is how the **complete arithmetic response**, including
its local term, gamma memory, signed poles, and delayed arithmetic terms, can
be represented or controlled by a positive state norm. The difficult part is
the interaction between these components. Separate positive spectra or correct
arithmetic coefficients do not establish positivity of their coupled response.

This is a direct continuation of Wilson–Loewner's
[cumulative-storage proposal](../../notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
and [arithmetic-source construction](../../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md).
It therefore belongs inside `wilson-loewner`, even though the immediate methods
are operator theory and arithmetic analysis. An independently defined physical
storage space remains a long-term objective; finding useful arithmetic bounds
does not depend on first finding that space in a particular field theory.

The program has two main directions:

1. Extend the existing cumulative energy method toward the first prime while
   preserving all input directions and the full memory across a spatial join.
2. Audit and control the actual first-prime semilocal Sonin remainder, then
   compare its norm and signed terms with the cumulative defect.

A canonical-system comparison supports these directions only where it supplies
a concrete construction or estimate. WZW and N4SYM serve as sources of physical
mechanisms and constraints, not as prerequisites for the arithmetic work.

## 2. Corrected baseline: do not repeat the completed append

The [24 September comparative assessment](../../notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md)
recommended the normalized append from length 1/2 to 11/20 as the next task.
That recommendation overlooked later notes in the critical-path sequence.
The [operator-coupling certificate](../../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md)
and [current handoff](../../../critical-path/notes/RESEARCH_CONTINUATION_AFTER_OPERATOR_COUPLING_20260920.md)
already record an internal all-input proof at

\[
L=\tfrac12,\qquad h=\tfrac1{20},\qquad \omega=10^{-3},\qquad
V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
\]
\[
E=I-X^*X,\qquad F=I-ZZ^*,\qquad
\|F^{-1/2}YE^{-1/2}\|<0.951.
\]

The proof uses a forward/backward energy identity, a relative generator bound,
endpoint-aware finite blocks, and analytic bounds on every omitted block. The
gamma corner is controlled in operator norm; the previously obstructed
Hilbert–Schmidt estimate is not repaired by increasing resolution. The beta
history and both signed pole states pass through the join.

This is an inherited internal computer-assisted result, with specialist review
outstanding. It is not a new support-length record or an all-depth theorem.
Its positive **local instantaneous forms** are a substantive hypothesis of the
method; a cumulative contraction alone does not automatically supply that
hypothesis for the next join. No replay or specialist validation is claimed in
this opening note.

The next task is consequently an extension and dependency analysis, not another
resolution sweep of the completed example. The historical proof remains in
critical-path; this folder should not create a competing copy.

## 3. The objects and the eventual success criterion

Translate the parent's centered interval to (0,L), using the same ordinary
unweighted L2 norm. With H(p)=xi(1/2+p), the arithmetic transfer has symbol

\[
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},\qquad
\partial_\omega V_{\omega,L}=-G_{\omega,L}V_{\omega,L},\qquad V_{0,L}=I.
\]

Retain three distinct targets:

| Object | What would constitute progress |
|---|---|
| Central form Q(0,L) | An independently positive pairing exactly equal to the full arithmetic form on its stated domain, or a rigorous domination proving its sign. |
| Cumulative defect D(omega,L)=I−V*V | A state norm or estimate for the complete deficit, including cross terms. |
| Causal transfer V(omega,L) | An independently specified response with the exact normalization, arithmetic evolution, and a proved energy balance. |

On the parent's admissible smooth domain,

\[
\langle f,D_{\omega,L}f\rangle
=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,
\qquad
Q_{0,L}[f]=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\]

These relations do not identify positivity of an instantaneous form at a single
shift with contraction at that shift. Nor can a reflected self-adjoint form be
substituted for a nonlocal causal transfer.

The ultimate sufficient target remains a sequence

\[
L_j\longrightarrow\infty,\qquad \omega_j\downarrow0,\qquad
\|V_{\omega_j,L_j}\|\le1
\]

on **all** inputs at every selected pair. By restriction to a fixed window and
the stated smooth-test limit this would give central Weil positivity. A uniform
positive margin is not required, but a rigorous continuation mechanism is.
Neither finitely many successful appends nor a parameter-dependent change of
norm establishes this target. Defining storage as the square root of D after
assuming D is positive supplies no independent construction.

## 4. Direction A: first-prime cumulative continuation

### The bounded experiment

Use omega=10^-3 initially. A concrete first-prime benchmark is

\[
L_{\rm old}=11/20,\qquad h=1/5,\qquad L_*=3/4,
\qquad \log2<L_*<\log3.
\]

This keeps both individual diagonal windows prime-free but introduces the
first prime across their join. The old transfer's contraction has the inherited
append as support; new coercive constants and any local instantaneous metrics
must be proved or extracted explicitly. The old relative bound 0.951 is not a
bound for this new geometry.

In the triangular generator convention with mixed block −2H_s, the prime at
a=log2 adds

\[
H_s^{(2)}=\frac{\log2}{\sqrt2}\cosh(sa)R_a,
\qquad
(R_af)(t)=\mathbf1_{\{0<L_{\rm old}+t-a<L_{\rm old}\}}
f(L_{\rm old}+t-a),\quad 0<t<h.
\]

Thus the new term is an exact partial translation between specified old-input
and new-output segments. It is not a quadrature approximation to a delta
function. Although its active segments shrink as the final window approaches
log2 from above, its unweighted operator norm remains one whenever the segment
has positive length. Small overlap alone cannot make this an all-input small
perturbation. Its **relative energy cost** is what must be estimated.

Start from the inherited energy-transfer lemma

\[
|\langle v,H_sf\rangle|
\le\kappa\sqrt{Q_{s,L_{\rm old}}[f]Q_{s,h}[v]}
\quad\Longrightarrow\quad
\|F^{-1/2}YE^{-1/2}\|\le\kappa.
\]

Keep the gamma corner, pole terms, and prime translation in the combined mixed
operator. First determine whether the necessary local metrics and a useful
relative bound survive. If this sufficient estimate exceeds one, distinguish
failure of a coarse bound from failure of the relative inequality, and both
from noncontractivity of the actual transfer. The program explicitly permits
replacing the instantaneous-energy method by a truly cumulative comparison.

### The shared transfer benchmark

Let T be finite-window convolution by the complete gamma/rational factor,
and S_a the truncated right delay on L2(0,L_*). On the first-prime window,

\[
V=T+c_2S_aT,\qquad c_2=\frac{2^\omega-2^{-\omega}}{\sqrt2},
\]
\[
D=I-T^*T-c_2T^*(S_a+S_a^*)T-c_2^2T^*S_a^*S_aT.
\]

The requested estimate or storage identity concerns this entire expression.
An isolated positive prime mode does not account for the signed interference
or the subtracted delayed-output square. This is a finite-window identity,
not a global passive realization of a finite Euler product.

**Deliverable:** an all-input first-prime bound with stated domains, endpoint
control, complementary-input estimates, and a record of how its constants
change under extension; alternatively, a quantified obstruction pinpointing the
missing estimate. A positive finite matrix is exploratory evidence only.

## 5. Direction B: the actual Sonin remainder

The [comparative assessment, Section 4](../../notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md)
records the earlier local semilocal calculation and its provenance. Begin by
auditing that calculation, including its contact and pole conventions and
trace domains. Its essential comparison must be made reproducible in this
repository before new work depends on the machine-specific original.

Let Pi be the archimedean Sonin projection, U_a whole-line translation,
r=1/sqrt2, and

\[
M_2=I-rU_a,\quad G_2=M_2^*M_2,\quad
A_2=\left.\Pi G_2\Pi\right|_{\operatorname{Ran}\Pi},\quad
\Pi_2=M_2\Pi A_2^{-1}\Pi M_2^*.
\]

Here G_2 is a metric operator, distinct from the shift generator G(omega,L).
The inverse compressed metric in Pi_2 is essential: adjoining a place does not
give the required isometric norm comparison for free. For a smooth preparation
F, let C_F denote convolution and K_F=C_F* C_F. The previous comparison has a
positive pairing B_2[F]=||C_F Pi_2||_HS^2 and an extra coupling

\[
\Delta_2[F]=\operatorname{Tr}_{\operatorname{Ran}\Pi}
\big(A_2^{-1}\Pi G_2(I-\Pi)K_F\Pi\big),
\]
\[
Q_{0,L}[F]=\mathcal B_2[F]+P_L^{\rm pole}[F]
-\mathcal E_\infty[F]-\Delta_2[F]
-\frac{\log2}{\sqrt2}\langle F,(U_a+U_{-a})F\rangle.
\]

There is no sign for Delta_2 supplied merely by positivity of G_2. The task is
to bound the **total correction** relative to B_2, or to identify a preparation
that changes the comparison favorably. Requiring each remainder separately to
have a favorable sign would be unnecessarily strong.

The first computational milestone is an approximation of the actual Pi and
the displayed traces on a declared smooth input family, with controlled
inverse-series and trace tails. A generic finite projection is a diagnostic,
not a substitute for the Sonin projection. The existing one-prime Fourier
operator's failure to be Hilbert–Schmidt prevents a direct unweighted copy of
the archimedean square-trace calculation; retain the justified smoothing and
trace-ideal hypotheses. Likewise, prescribed transform zeros in published
archimedean comparisons must not disappear when comparing to unrestricted
all-input transfer bounds.

**Deliverable:** a checked comparison and a quantitative residual estimate on
a stated domain, followed by an all-input domination argument if feasible.
A well-controlled negative example for this preparation is useful if it
identifies what a different arithmetic state space must supply. This direction
can proceed independently of Direction A.

## 6. Connecting the two directions and auditing canonical systems

The first-prime coefficients already give a normalization check. Since
c_2'(0)=sqrt2 log2, differentiating the defect on admissible tests gives

\[
Q_{0,L}[f]=Q^{A}_{0,L}[f]
-\frac{\log2}{\sqrt2}\langle f,(S_a+S_a^*)f\rangle,
\]

where Q^A includes the complete gamma, local, and rational contribution.
The coefficient agrees with the semilocal comparison. This agreement is
bookkeeping, not a positive-state identification: U_a acts on a whole-line
space, S_a is truncated, and the Sonin metric is a separate object.

A high-value bridge would give an explicit preparation or intertwiner,
its domain and adjoint, and a norm identity or inequality transporting the
semilocal remainder into the cumulative storage problem. It must keep the
pole and contact terms and justify any shift limit. A mere correspondence
between positive operators does not suffice.

The Suzuki comparison should then ask one precise question: does an explicitly
constructed canonical system supply that map, a new bound on that residual,
or continuation beyond the regime of positive local instantaneous metrics?
Record exactly where kernel invertibility, determinant nonvanishing, and
Hamiltonian positivity enter. The inherited assessment identifies a gap between
the available explicit construction and the needed small-shift regime. An
existence statement conditional on the desired positivity is not a solution.

**Deliverable:** a short dependency comparison identifying either a genuinely
new estimate available unconditionally in the relevant range, or the exact
unresolved sign condition shared by both formulations. In the second case,
keep canonical systems as a useful language rather than a third main project.

## 7. Milestones, impact, and decisions

Impact here means progress toward an all-input, arbitrarily large-support
positivity mechanism, not the number of successful tests.

| Milestone | Broader value | Completion or decision criterion |
|---|---|---|
| Audit the completed append's dependencies | High reliability value; limited new mathematical reach | Extract the local-metric and complement hypotheses needed for extension. Preserve the outstanding specialist-review status. |
| Derive and estimate the first-prime mixed block | High immediate value | A complete all-input bound, or a sharp account of where relative energy fails to control the exact translation. |
| Evaluate and dominate the actual Sonin residual | High structural value | Controlled Pi-dependent calculation and an inequality for the full correction, or a specific obstruction to this preparation. |
| Identify the state/norm bridge | Very high conditional value | An explicit map with correct adjoint, normalization, domains, and arithmetic terms; no positivity assumed in its construction. |
| Obtain a continuation invariant | Highest relevance to the ultimate goal | A recurrence or structural estimate that supports unbounded lengths with shifts tending to zero, including any loss of margin. |
| Canonical-system audit | High potential; conditional priority | A new usable estimate or state map, not an equivalent restatement of the missing sign. |

The first substantive session should derive the exact new mixed block and
determine which local metrics are available at (11/20,1/5,10^-3). Only then
choose a numerical representation and certify the omitted spaces. In a separate
session, audit the semilocal residual and establish a controlled evaluation on
a small smooth family. Compare the two at the same first-prime normalization.

After a first-prime success, test increasing supports in their actual order:
the delay at log3, repeated-prime behavior at log4, and mixed-prime behavior at
log6. Every intervening integer delay belongs to the full transfer, including
5; the generator instead contains prime powers. A selected two-prime model
through log6 is not the full arithmetic window.

Finite successes remain calibration until a continuation invariant is proved.
Margins may shrink, but their evolution must be controlled sufficiently for
the stated limiting sequence. If instantaneous local positivity ceases to be
available, record that boundary of the method and prioritize the cumulative
or state-space alternative rather than silently assuming the missing sign.

Every proposed arithmetic mechanism should face the program's negative
smooth-density control. A generic positivity argument that also certifies a
known failing replacement has omitted an essential arithmetic condition.

## 8. Physical interfaces and record keeping

The WZW and N4SYM work supplies useful lessons: matching a spectrum is weaker
than matching a response; a thermal coefficient identity is weaker than a
causal norm identity; and local negative power terms can coexist with positive
energy once the correct internal storage is included. The finite-mass N4SYM
example illustrates the last point, but its work norm and single memory scale
do not provide the arithmetic signal norm or delayed arithmetic response.

Reopen a physical candidate here only with an independently specified
preparation, observable, adjoint, time/shift dictionary, and an explicit role
in one of the missing estimates above. Keep worthwhile YM or N4SYM hierarchy
calculations in their own branches when their goal is physical rather than
arithmetic. The scoped exclusions reviewed in the
[WZW/N4SYM assessment](../../notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md)
do not amount to universal impossibility theorems.

Place new analysis in this folder's notes, numerical sources and small records
in its future numerics folder, and audits in its future reviews folder. Keep
the critical-path certificate and physical source notes at their existing
locations and cross-link them. Follow LARGE_FILES.md for derived data. Record
model, exposed effort setting, assumptions, and evidence level in every note;
distinguish symbolic derivations, floating diagnostics, interval certificates,
and specialist review. Use Git commits or tags for future manuscript milestones
without creating snapshot directories.

The immediate goal is a complete, reproducible first-prime comparison with a
precise account of what pays for its mixed terms. The broader goal is a state
norm or continuation principle that explains why the arithmetic terms remain
compatible with positivity as the support grows.
