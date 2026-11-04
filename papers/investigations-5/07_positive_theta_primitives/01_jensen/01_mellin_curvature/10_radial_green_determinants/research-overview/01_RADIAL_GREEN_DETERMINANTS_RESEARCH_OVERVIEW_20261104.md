# Radial Green determinant research overview

4 November 2026, America/New_York. Drafted for **Edward Baker** with
substantial LLM assistance; actual recorded **gpt-6-astra (Codex),
reasoning effort xhigh**. Originating chat
01a1a455-6c1d-7aa2-9723-43ab36704924, setup turn
01a1a741-0198-7d80-99a4-e15eaa63f818.

**Current plan: [revision r2](#research-plan--revision-r2-4-november-2026),
focused on the induction mechanism and error control as the index grows.**
The inherited mathematical foundation is the exact radial Green and
determinant derivation in [brainstorm Note06, Sections 1–6][n06], with
same-assistant analytical and exact rational algebra checks. Subsequent
finite comparison results and their review levels are recorded in the
[sole progress register][progress]. The author-requested r2 revision
changes research priorities, not the status of a mathematical claim.
The original r1 plan and all frozen requests remain below or at their
existing paths as historical evidence.

## Purpose and scope

The subject is the canonical theta coefficient determinant
\(D_{r,k}\) expressed through the undifferentiated theta primitive,
symmetric polynomial probes and explicit boundary terms.
The radial Green identity gives a concrete relation between these
objects without assigning them a thermodynamic meaning.

The earlier discussion obtained a fixed-temperature configurational
model by giving spatial particles an additional internal spectrum and
position-dependent potentials. Those choices are not required for the
Green derivation and do not become assumptions of this investigation.
The author has selected the mathematical development through equation 9
of the preceding chat response, corresponding to Sections 1–6 of Note06,
as the starting point. Physical interpretations remain open rather than
being prescribed by the folder.

The geometric variables are \(R\), a radial variable, and
\(u=\tfrac12\log R\). The index \(r\) denotes determinant order.
No physical particle number is identified with \(r\), and no quantum
field is defined on the temperature parameter.

The central mathematical issue is whether the complete canonical
primitive imposes useful relations on the signed polynomial probes
and their boundary contributions. The identities below expose those
quantities exactly; their positivity and comparison estimates remain
separate questions.

## Canonical source and coefficient normalization

At physical heat time zero, retain the complete source
\[
\Phi(u)=\sum_{n\ge1}
\left(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\right)
e^{-\pi n^2e^{4u}},\qquad u\ge0.
\tag{1}
\]
Put
\[
R=e^{2u},\qquad
A(R)=\sum_{n\ge1}e^{-\pi n^2R^2},\qquad
p(u)=R^{1/2}A(R).
\tag{2}
\]
There is no finite spectral truncation in these definitions.
The complete tail justifies all polynomial moments and fixed-order
derivative transfers used below.

For \(j\ge0\), define
\[
m_j(u)=\frac{u^{2j}}{(2j)!},\qquad
c_j=\int_0^\infty\Phi(u)m_j(u)\,du,\qquad
d_j=\int_0^\infty p(u)m_j(u)\,du.
\tag{3}
\]
Set \(m_j=c_j=d_j=0\) for \(j<0\). The determinant convention is
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},
\qquad r\ge1,\quad k\ge0.
\tag{4}
\]
These are the ordinary coefficients \(c_j\), not raw moments or the
exponential coefficients \(\gamma_j=j!c_j\).
The [Jensen program][jensen] supplies the surrounding total-positivity
and real-rootedness questions with their full quantifiers.

## Radial Green transfer and the inner boundary

For a radial Gaussian,
\[
\Delta_3e^{-aR^2}=(4a^2R^2-6a)e^{-aR^2},
\qquad \Delta_3=\partial_R^2+\frac2R\partial_R.
\]
Consequently
\[
\boxed{\Phi(u)=\tfrac12R^{5/2}\Delta_3A(R).}
\tag{5}
\]
Dimension three matches the two coefficients in the canonical source;
the sum itself still runs over one-dimensional square modes.

For a polynomial probe \(f\), define
\[
F(R)=R^{-1/2}f(\tfrac12\log R).
\]
Direct differentiation gives
\[
\Delta_3F=\tfrac14R^{-5/2}(f''-f).
\]
Using \(du=dR/(2R)\) and radial Green's identity,
\[
\begin{aligned}
\int_0^\infty\Phi f\,du
&=\frac14\int_1^\infty F\,\Delta_3A\,R^2\,dR\\
&=\frac14\int_1^\infty A\,\Delta_3F\,R^2\,dR
+\frac14[-A'(1)F(1)+A(1)F'(1)].
\end{aligned}
\tag{6}
\]
The outer boundary vanishes by the complete theta tail.
The inner boundary follows from the normalized reflection
\[
\Theta(R)=1+2A(R)=R^{-1}\Theta(1/R),\qquad
A'(1)=-\tfrac12A(1)-\tfrac14.
\]
Thus
\[
p''-p=8\Phi,\qquad p(0)=A(1),\qquad p'(0)=-\tfrac12,
\]
and (6) becomes
\[
\boxed{
\int_0^\infty\Phi f\,du
=b f(0)+\frac{p(0)}8f'(0)
+\frac18\int_0^\infty p(u)[f''(u)-f(u)]\,du,
\quad b=\frac1{16}.}
\tag{7}
\]
This is the scalar identity inherited from
[Radial Note73][radial73]. The constant \(b\) and the derivative trace
are part of the identity.

For the even moment probes, \(m_j''=m_{j-1}\),
\(m_j'(0)=0\), and \(m_j(0)=\delta_{j0}\). Therefore
\[
\boxed{c_j=b\delta_{j0}+\frac18(d_{j-1}-d_j).}
\tag{8}
\]
In matrix form,
\[
[c_{k+j-i}]=B+M,\qquad
B_{ij}=b\delta_{i,k+j},\quad
M_{ij}=\tfrac18(d_{k+j-i-1}-d_{k+j-i}).
\tag{9}
\]
The endpoint matrix has rank \(\max(r-k,0)\).
This already distinguishes the pure-volume case \(k\ge r\)
from the cases with possible endpoint contributions.

## Symmetric determinant probes and the complete boundary expansion

Define
\[
T_{r,k}(\mathbf u)=
\det[m_{k+j-i}(u_i)]_{i,j=0}^{r-1},
\qquad
\mathcal T_{r,k}(\mathbf u)=
\frac1{r!}\sum_{\sigma\in S_r}
T_{r,k}(u_{\sigma(0)},\ldots,u_{\sigma(r-1)}).
\tag{10}
\]
Expanding the determinant and integrating each row replaces \(m_j\)
by \(c_j\). The product measure is permutation-invariant, so the
symmetrization leaves the integral unchanged:
\[
\boxed{
D_{r,k}=\int_{[0,\infty)^r}
\prod_{i=0}^{r-1}\Phi(u_i)\,
\mathcal T_{r,k}(\mathbf u)\,d\mathbf u.}
\tag{11}
\]
The \(1/r!\) in (10) is an average, and no additional factorial
belongs in (11). Each coordinate enters \(\mathcal T\) evenly.

Write \(L_i=\partial_{u_i}^2-1\). For \(0\le q\le r\), put
\[
W_{r,k}^{(q)}(u_0,\ldots,u_{q-1})
=
\left[
\left(\prod_{i=0}^{q-1}L_i\right)\mathcal T_{r,k}(\mathbf u)
\right]_{u_q=\cdots=u_{r-1}=0}.
\tag{12}
\]
For \(q=0\), this means the scalar \(\mathcal T_{r,k}(0,\ldots,0)\);
for \(q=r\), there is no endpoint evaluation.
Applying (7) in each coordinate of (11) gives
\[
\boxed{
D_{r,k}=
\sum_{q=0}^r\binom rq b^{r-q}8^{-q}
\int_{[0,\infty)^q}
\prod_{i=0}^{q-1}p(u_i)\,
W_{r,k}^{(q)}(\mathbf u)\,d\mathbf u.}
\tag{13}
\]
Every odd first-derivative trace vanishes by coordinatewise evenness.
There are \(\binom rq\) equal terms with \(q\) coordinates remaining
in the volume. The other \(r-q\) coordinates are evaluated at
the inner sphere \(R=1\).

The derivation uses the full orthant, so it introduces no artificial
collision faces by ordering the coordinates.
Endpoint rows have entries \(\delta_{k+j-i,0}\); only rows
with \(i\ge k\) can be nonzero. It follows that
\[
W_{r,k}^{(q)}\equiv0\quad\text{when }q<\min(k,r).
\tag{14}
\]
In particular,
\[
\boxed{
D_{r,k}=8^{-r}\int_{[0,\infty)^r}
\prod_i p(u_i)\,
W_{r,k}^{(r)}(\mathbf u)\,d\mathbf u,\qquad k\ge r.}
\tag{15}
\]
The full-volume probe can also be written explicitly as
\[
W_{r,k}^{(r)}(\mathbf u)
=\operatorname{Sym}_{\mathbf u}
\det[m_{k+j-i-1}(u_i)-m_{k+j-i}(u_i)]_{i,j=0}^{r-1},
\tag{16}
\]
with the same averaging convention as in (10).
For \(k<r\), the lower-dimensional terms in (13) generally remain.

Equations (8) and (13) are two forms of the same identity.
The first displays primitive-moment differences and endpoint matrix
entries; the second displays their complete integral and boundary
structure. Positivity of \(p\) alone signs neither the differences
nor the symmetric probes.

## Low-order example and available checks

For \(r=2,k=1\),
\[
\mathcal T_{2,1}(u,v)
=m_1(u)m_1(v)-\tfrac12[m_2(u)+m_2(v)],
\]
\[
W^{(0)}=0,\qquad
W^{(1)}(u)=-\tfrac12[m_1(u)-m_2(u)],
\]
\[
W^{(2)}(u,v)
=[1-m_1(u)][1-m_1(v)]
+\tfrac12[m_1(u)-m_2(u)+m_1(v)-m_2(v)].
\]
The full expansion is
\[
\begin{aligned}
D_{2,1}
&=-\frac b8(d_1-d_2)
+\frac1{64}\{(d_0-d_1)^2+d_0(d_1-d_2)\}\\
&=c_1^2-c_0c_2.
\end{aligned}
\tag{17}
\]
The first term is the surviving boundary contribution.
For the triangular anchor \(k=0\), \(\mathcal T_{r,0}=1\),
\(W_{r,0}^{(q)}=(-1)^q\), and
\[
D_{r,0}=(b-d_0/8)^r=c_0^r.
\tag{18}
\]

The existing [exact algebra checker][checker] verifies (13) against
an independent permutation expansion of (9), treating \(b,d_0,d_1,\ldots\)
as formal indeterminates. The [execution record][record] reports 25 cases,
\(1\le r\le5\) and \(0\le k\le r+1\), including endpoint vanishing,
the triangular anchor and the explicit example above.
These are same-assistant checks of identities and factors. They are not
numerical evidence for theta determinant signs. The general proof is
the multilinearity and coordinatewise Green argument in Note06.

## Relation to the parent questions

This investigation retains the determinants and coefficient normalization
of the [Mellin-curvature program][parent]. Its new emphasis is the
primitive-weighted integral together with all endpoint contributions.
It has not established a neighboring-index estimate, a new
Mellin-curvature range, or an order-raising theorem.

The [source overlap kernel investigation][kernels] organizes the
coefficient pairings through separate source variables and integral
kernels. The present formulation instead transfers radial derivatives
and studies the resulting symmetric probes and boundary terms.
These descriptions share a determinant target but do not require
the same analytical or physical interpretation.

The earlier [open quantum dynamics investigation][dynamics] remains
a separate body of work. This folder selects no dynamics, Hamiltonian
or equilibrium ensemble. The Laplacian in (5)–(7) supplies a Green
pairing of different functions; it does not by itself turn the
determinant into a nonnegative kinetic-energy expectation.
This observation leaves other energy interpretations open.

## Classification and inherited control screen

The inherited result is an exact reformulation. It exposes the
canonical primitive and the boundary terms but supplies no new
quantitative sign mechanism. The [result index][results], especially
[theta identities][thetaresults] and [collision controls][controls],
and the [avoid index][avoid], especially [target reformulations][a01],
[geometric realizations][a03], [normalizations][a08] and
[joint signed estimates][a12], specify the relevant scope.

The scalar Green structure is not unique to theta.
For a positive half-line source \(\xi\) with the required moments,
[Radial Note73][radial73] gives
\[
p_\xi(u)=8\int_u^\infty\sinh(v-u)\xi(v)\,dv>0,\qquad
p_\xi''-p_\xi=8\xi.
\]
Its endpoint constant is
\[
b_\xi=-p_\xi'(0)/8
=\int_0^\infty\cosh(v)\xi(v)\,dv.
\]
The same even-probe calculation produces (8)–(13) with
\(p_\xi,b_\xi\). A positive normalization can match \(b=1/16\)
without removing a zero collision in the source transform.
This screens positivity of the primitive and Green transfer as a
sufficient sign argument.

The failed canonical premise differs across the inherited controls.
Weighted-square controls alter the complete unit coefficients,
while retaining square support and suitable radial identities.
Euler-factor controls change the canonical source by shifts.
Reflected super-Gaussian and smooth positive-primitive controls can
retain symmetry or primitive data without the literal canonical
square expansion \(A(R)\).
The generic Green calculation does not separate these families.
The source-specific information in the full canonical \(A\) remains
available; no new bound using it is asserted in this overview.

## Research plan — revision r2, 4 November 2026

Prepared for **Edward Baker** with substantial LLM assistance; actual
**gpt-6-astra (Codex), effort max**, chat0002, turn
`01a1a7b4-0874-7401-9d01-11bf9930cad0`. **RGD-E01 r2: planning revision.**
The author requested an emphasis on the induction mechanism, control of
error with increasing index, and the structure of the overall argument.
This revision changes priorities and future task contracts; it proves no
new mathematical result. The [r1 plan](#research-plan--revision-r1-4-november-2026)
and all issued packets remain historical records of their original scope.

**Default next task: [B] RGD-B03 r2 — Astra: investigate the induction
mechanism and its index-dependent error control.** This conceptual work
is ready now. It does not wait for more low-order cases or another pilot
assessment. The former workflow gate on investigating full B03 is
superseded by the author's direction; an induction theorem remains open.
The [sole register][progress] owns current evidence and readiness, and
[Packet10][inductionhandoff] gives the current continuation/model guidance.

### Overall argument to investigate

The intended chain is: canonical theta structure supplies quantitative
data; those data propagate an induction hypothesis from order r to r+1;
the propagated margin dominates the complete error for every required k;
the resulting determinant signs reach the parent conclusion through its
explicitly justified implications. Establishing this chain is the main
research objective. A sequence of additional finite certificates does
not establish any of its missing general links.

Retain the complete time-zero source, ordinary coefficients, negative-index
zeros, exact b=1/16, and all Green boundary terms. The existing identity
\[
Q_{r,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}
=D_{r+1,k}D_{r-1,k},\qquad r\ge2,\quad k\ge1,
\]
specifies the consumer. Lower-order positivity alone does not sign Q.
The research must identify the additional quantitative property that
propagates; assuming Q>0 or D_(r+1)>0 as that property is circular.

| Link in the argument | Required analytical output | Current gap |
| --- | --- | --- |
| Starting hypothesis | State an explicit H_r: lower-order signs plus the quantitative margin, source and error information actually needed at the next step; give its domain and a valid initialization | Existing pilots do not initialize an all-index quantitative invariant |
| Order step | Derive H_(r+1) from H_r and independently justified canonical input, retaining enough quantitative information to apply the step again | Desnanot–Jacobi is an identity, not this propagation theorem |
| Increasing index | Prove complete-error control against the determinant margin over the entire k-domain, with dependence on r displayed | The current entry-relative majorant is nonuniform in the moment index |
| Closure of domains | Cover small k, k near r, and unbounded k with compatible estimates and no unproved gaps as r increases | Neither a fixed-k proof nor a fixed-r tail alone covers the full induction |
| Final implication | Identify exactly which all-order determinant statement is obtained and check the parent's hypotheses for the passage to all required Toeplitz minors/Jensen conclusions | No all-order conclusion is supplied by this plan |

For a comparison route, the operational objective is to derive an
independently justified reference lower margin M_(r,k)>0 and a complete
error allowance E_(r,k) with
\[
Q_{r,k}\ge M_{r,k}-E_{r,k}>0.
\]
This is a **proof obligation**, not a proposed new theorem or evidence for
RH. If q* is used as the margin, its reference determinant signs and size
must be proved without assuming the desired canonical next-order sign.
The induction must also propagate the quantitative information needed at
the following step; dividing by a positive D_(r-1),k alone does not do so.

### RGD-B03 — induction and index growth r2

**Primary attempt:** investigate whether a normalized determinant margin
and the complete signed remainder admit a closed order-propagation law
using the canonical primitive. Begin with the combined Q polynomial and
the general comparison estimates in [Note05][prepnote], rather than a new
list of cases. The first-mode comparison is an available candidate, not
an assumption that it can support induction. Keep its exact joint
cancellations before taking error bounds; track every nonlinear remainder.

The attempt must resolve, or expose a precise obstruction to, these
coupled questions:

1. **What propagates?** Specify H_r and a proposed implication H_r =>
   H_(r+1), including the quantitative output for reuse. Separate source
   identities, established inputs and unproved estimates. If a stronger
   invariant is necessary, identify how it could be initialized and
   propagated rather than hiding the conclusion in its definition.
2. **What pays the growing error?** Compare the complete signed error
   with a justified margin as k increases, and track how that comparison
   changes with r. Small coefficient errors are insufficient when
   determinant cancellation amplifies them. Bound the relevant condition
   factors or replace that auxiliary bound by a justified joint estimate.
   Reference positivity and margin decay are part of this question.
3. **Which quantifiers close?** Aim for every integer k>=1 at each
   induction step. If a split at K(r) is used, give an analytical rule for
   K(r), all constants and the joining argument. The portion k<K(r)
   requires a mechanism valid as r grows, not an ever-growing table of
   separately certified cases. A large-k asymptotic with uncontrolled
   r-dependence is not enough. Include fixed small k as r grows and the
   transition k near r; the three order-r boundary ranks are
   max(r-k+1,0), max(r-k,0), max(r-k-1,0).
4. **What closes the induction?** State the starting order and justified
   initialization, the recurrence/inequality for the quantitative data,
   and why it remains sufficient at every finite step. Explicit positive
   slack may depend on r,k and tend to zero; a globally fixed slack is
   not required unless the proposed proof needs it. Any real-parameter
   extension is a separate obligation, not supplied by integer identities.

Note05 proves that the fixed compact reference and its current tail vector
cannot maintain a uniformly small entry-relative error at all moment
indices. This is a central input to the mechanism investigation. It
excludes that particular shortcut; it does not exclude the exact joint
payment or all first-mode comparisons. Any change of reference, scaling,
cutoff or tail estimate must explain analytically how it affects both the
margin and the complete error. An index-dependent cutoff must pay every
source/spatial remainder and any new boundary term it introduces.

**Bound and completion:** one principal induction attempt, with at most
one alternative if a named obstruction forces a choice. Return one note
containing the overall implication chain, explicit H_r and propagation
claim, complete r/k dependence, and a worked analytical attempt at its
decisive estimate. Acceptable outcomes are a proved induction lemma, a
partial derivation with the exact unresolved estimate and its domain, or
a scoped obstruction to the attempted mechanism. Merely renaming the
target, listing hoped-for lemmas, or adding low-order positive examples
does not complete B03. Freeze a routine E02 proof task as soon as its
route is fixed; issue a numerical E03 task only under the rule below.
A material redesign beyond the bounded attempt returns to B02.

### Numerical checks test hypotheses only

All future numerical research, including numerical work inside E02 or
E04, must serve a stated hypothesis about the induction mechanism or
index-dependent error control. No further order/index certificate campaign
is the default or a prerequisite. Existing exact data may be reused only
for a discriminating question; their availability is not a reason to
extend the list of low-order cases.

Before implementation, a packet must name the hypothesis and its role in
the overall proof, its predicted inequality or behavior, the finite cases
chosen to distinguish outcomes, the arithmetic/error standard and work
cap, and the analytical decision after a favorable, adverse or inconclusive
result. For example, test whether a proposed remainder bound or condition
factor scaling fails at a boundary transition; do not merely retest a
determinant sign already covered by the known finite-order baseline.

A favorable finite test supports further analysis of that hypothesis;
it does not prove its unbounded range. A rigorously verified violation
refutes the stated inequality on its domain; an inconclusive enclosure
does not. Stop at the fixed test. Additional cases require a revised
question, not automatic precision or range escalation. Exact symbolic
identity checks remain verification of algebra, not positivity evidence.
No numerical hypothesis test is issued by this planning revision.

### Current task routing under r2

The stable task IDs are retained. These rules supersede r1's future
routing while preserving every completed result and frozen request.

| Task | Type and recommended model | Readiness and purpose |
| --- | --- | --- |
| RGD-E01 r2 | E — Sol; documentation (actual revision Astra/max) | This author-requested plan/register revision only |
| **RGD-B03 r2** | **B — Astra; induction invariant, margin propagation and index-error control are unresolved** | **Default next; ready for the bounded conceptual attempt above** |
| RGD-E02, next revision | E — Sol; prescribed analytical derivation | Conditional on a B03/B02 packet specifying a general lemma, route, domain and closure test; no new packet issued here |
| RGD-E03, next revision | E — Sol; bounded hypothesis testing | Conditional on the numerical rule above; no test or scan issued |
| RGD-E04 r3 | E — Sol; assess the already completed finite application | Existing [Packet09][priorassessment] remains available as optional evidence maintenance; it is not the default or a gate on B03 |
| RGD-B02 | B — Astra; repair a specific failed mechanism | Conditional on a named obstruction from the induction attempt or assessment; one bounded repair decision |
| RGD-B01 and earlier E returns | Completed evidence | Preserve their results, limits and actual review relationships |

Use [result summaries][results], especially [theta structure][thetaresults]
and [collision controls][controls], with [avoid][avoid], particularly
[target reformulations][a01], [joint estimates][a12], [numerics before a
question][a10], [known-baseline tests][a11] and [scoped exclusions][a07].
For each candidate, identify the quantitative premise actually obtained
from canonical theta. Weighted-square controls change unit weights;
Euler-factor controls change the source; reflected/smooth primitive
controls lack its literal square expansion. Those differences do not
establish failure of an untested margin inequality. Retain the time-zero
scope: a positive-time collision alone is not a counterexample to it.

**Next: [B] RGD-B03 r2 — Astra**, return the proposed induction mechanism,
its index-error analysis, and the precise proof step that succeeds or
fails. Model changes and execution follow the [root workflow][workflow];
no model switch, dispatch or new numerical run is authorized by routing.

## Research plan — revision r1, 4 November 2026

**Historical plan r1.** Its issued questions and results are preserved.
[Revision r2](#research-plan--revision-r2-4-november-2026) supersedes its
future priorities and numerical policy; use the live register for status.

Prepared for **Edward Baker** with substantial LLM assistance; actual
planning model **gpt-6-astra (Codex), effort xhigh**, chat
01a1a749-3920-78b1-a660-223790a78876, turn
01a1a753-26b4-79e3-93d5-b03b12432bc5. Documentation task **RGD-E01**.
This author-requested plan supersedes the initial deferral of planning.
It issues the conceptual question below; it executes no new mathematical
investigation, computation or assessment.

The [root model workflow][workflow] governs the division: **B — brainstorm,
recommended Astra**, when a mechanism or proof strategy must be selected;
**E — execution, recommended Sol**, once the objective, route, inputs and
completion test are fixed. Routine analytical proofs belong to E. Edward
Baker selects the actual model, effort and chat. The recommendation does
not change settings or authorize dispatch. Record actual session metadata
separately from recommendations.

The [progress file][progress] is the **sole live register for RGD tasks**.
This section holds the versioned mathematical plan and task specifications;
the register holds current readiness, results and links to issued packets.
Existing J and MC task identities and their registers remain unchanged.

### Objective and quantitative consumer

The vision is to use the complete theta primitive in (13), including its
boundary terms, to obtain a comparison that remains useful as determinant
order increases. The immediate conceptual question is whether this
representation supplies a theta-specific estimate for the order-three to
order-four comparison. This is a method-development pilot within known
low-order positivity, not a claim of new coefficient coverage.

Write \(\mathcal G_{r,k}\) for the complete right side of (13). The existing
identity says \(\mathcal G_{r,k}=D_{r,k}\). The parent Desnanot–Jacobi identity
gives the consuming expression
\[
Q_{r,k}:=\mathcal G_{r,k}^{\,2}
-\mathcal G_{r,k-1}\mathcal G_{r,k+1}
=D_{r+1,k}D_{r-1,k},\qquad r\ge2,\ k\ge1.
\tag{19}
\]
At \(r=3\), a bound of the form
\[
\frac{D_{3,k-1}D_{3,k+1}}{D_{3,k}^{\,2}}
\le 1-\eta_k
\quad\Longrightarrow\quad
D_{4,k}\ge\eta_k\frac{D_{3,k}^{\,2}}{D_{2,k}},
\tag{20}
\]
uses positive \(D_{2,k}\) and \(D_{3,k}\), with their exact source and
internal review status recorded before application. A nonnegative
\(\eta_k\) gives nonnegativity; strict positivity requires \(\eta_k>0\).
Equations (19)–(20) specify the consumer, not a new sign mechanism. The
case \(\eta_k=0\) restates the next-order sign under these premises.
A useful return must identify an additional independently justified
estimate and its domain, or an explicit obstruction to a proposed estimate.

Use two structural cases to keep the first decision concrete:

- **\(k=1\):** the comparison uses \(D_{3,0},D_{3,1},D_{3,2}\), so endpoint
  contributions remain; \(D_{3,0}=c_0^3\) is the exact anchor.
- **\(k=4\):** all three order-three indices \(3,4,5\) satisfy \(k'\ge3\),
  so the neighboring determinants have pure-volume representations.
  The intervening \(k=2,3\) and unbounded index range remain separate
  obligations until a return explicitly covers them.

These cases diagnose the proposed mechanism, not the truth of already
known low-order determinant signs. A finite pilot is useful only if its
return explains what can extend, what deteriorates with order, and which
part is confined to the pilot. An eventual RH argument must still supply
all required orders and indices and justify the passage to all Toeplitz
minors with the appropriate hypotheses from the [Jensen program][jensen].

### Initial task routing

| Task | Type and recommended model; reason | Eligibility and dependency | Deliverable |
| --- | --- | --- | --- |
| RGD-E01: plan and register | **E — Sol**; ordinary documentation and consistency checks | Author's current request; actual preparation Astra/xhigh | This plan, sole register and repaired navigation |
| RGD-B01: select a theta-specific joint comparison | **B — Astra**; the input that controls signed cancellation is unknown | Inherited (1)–(18), Note06 and control screen; initial default next task | One worked mechanism decision and frozen E contract, or a scoped obstruction |
| RGD-E02: derive the selected comparison | **E — Sol**; execute an explicit analytical route | Requires a tractable, versioned packet from B01, B02 or B03 | Complete derivation on the issued domain, with all boundary and tail terms |
| RGD-E03: finite diagnostic or certificate, if needed | **E — Sol**; implementation and bounded evaluation of a fixed expression | Optional; requires a separately frozen question and finite limits | Exact/floating/certified return at the declared evidence level |
| RGD-E04: assess and integrate one return | **E — Sol**; check a stated argument against its packet | A conceptual or execution return with identifiable inputs | Scoped assessment and accurate local status/navigation |
| RGD-B02: resolve a failed or incomplete mechanism | **B — Astra**; a named mathematical choice must change | Only a documented obstruction or unresolved premise from B01/E02/E03/E04 | One repair decision, alternate contract, or scoped stop |
| RGD-B03: decide whether the mechanism extends in order | **B — Astra**; higher-order premises and losses are unresolved | An assessed useful pilot and explicit order dependence | An induction contract or a precise limit of the pilot |

E02 and E03 are conditional follow-through slots, **not issued execution
requests**. Their detailed inputs and numerical limits cannot be inferred
from this table. E04 may assess a conceptual obstruction without requiring
a numerical task. Read the live register before starting any task.

### RGD-B01

**Question:** Which additional property of the full canonical \(A(R)\)
can control the combined expression (19), including every contributing
boundary term, beyond generic positivity and the Green identity?

The default candidate is a **direct joint estimate** for \(Q_{3,k}\) after
substituting (13), retaining mixed terms between volume and endpoint
contributions. Compare it with at most **one** of these alternatives:

1. A theta-specific inequality among the primitive moments \(d_j\), with
   an explicit transfer through (8)–(9) to the same consumer. Generic
   positive-moment Hankel inequalities are insufficient by themselves.
2. A transfer to the parent's complete signed Mellin comparison. Use its
   established \(M(s)\), normalization and positivity premises. Any new
   derivative transfer for nonpolynomial probes must justify convergence
   and endpoint traces; integer-index formulas (8)–(13) do not supply a
   noninteger Toeplitz identity automatically.

For the second alternative, distinguish the parent's pointwise Gaussian
curvature bound from its weaker integrated comparison and the exact
next-order sign condition. Changing the comparator changes the target;
it must be recorded, not counted as success on the original bound.

**Bound:** one primary candidate and one optional alternative; one worked
analytical attempt, with structural checks at \(k=1,4\). No new numerical
implementation or broad parameter search belongs to B01. Reuse the
inherited 25-case exact checker as normalization evidence; repeating it
alone is not an investigation result.

**Return and acceptance:** save one decision note in `notes/`, recording
the exact canonical input, proposed inequality, domain, mechanism for
handling signs jointly, consumer, baseline and claim-specific controls.
An actual partial proof must name its uncovered range. A scoped failure
must name the failed estimate or class. A surviving obligation must be
an explicit residual or premise exposed by the attempt, not just (19)
written in new notation. These are acceptable completed assessments;
an unsupported conjecture alone is not.

If a route becomes routine, freeze E02 immediately and recommend Sol.
If a finite diagnostic is needed to decide feasibility, freeze E03 with
the exact discriminating question before any code is written. Otherwise
state the specific B02 choice or recommend a scoped stop. Do not introduce
a Hamiltonian or physical ensemble as an assumed source of positivity.

### RGD-E02

**Scope:** one selected estimate, one issued request revision and its
explicit domain. The packet must fix the theta identity, proof route,
normalization, all lower-order inputs, expression to be estimated and
quantitative acceptance test. If the domain is infinite, it must identify
the finite or compact part, analytical tail argument and transition.
An arbitrary-order claim must specify the dependence of every constant
and the induction hypotheses; a pilot does not supply these automatically.

**Output:** one derivation in `notes/` with complete boundary, convergence
and tail accounting, and exact support in `numerics/` only where requested.
Standard algebra, a normalization correction and routine estimates inside
the fixed route are permitted. Complete the task with a proof on its
actual domain, or a precise failed step and retained evidence. An
unproved sign is not an accepted lemma. A changed mechanism, observable,
source, comparator or domain beyond the issued limits returns to B02;
unaffected execution may continue. The evidence bound is the one packet,
not an open-ended sequence of increasingly strong lemmas.

### RGD-E03

**Optional numerical gate:** issue this task only when B01/B02 or the
fixed E02 route supplies a question that a finite computation can answer.
Its packet must name the expression and threshold, exact finite cases,
source-mode and spatial cutoffs, complete-source tail payments, arithmetic
type, initial and maximum precision, refinement/evaluation or runtime cap,
permitted adaptations and the action taken for each possible outcome.
Absent any of these, the task stays unissued.

**Output:** fixed code and a small execution record in `numerics/`, with
input versions, actual errors and capped or failed cases. Floating
diagnostics measure feasibility; certified signs require outward bounds
for every error. Numerical truncation is allowed only as an approximation
to the unchanged complete source with the appropriate error accounting.
Finite samples do not establish an infinite-domain theorem. Completion
at the cap may be an inconclusive or adverse result; it does not authorize
a wider scan. Routine debugging stays inside the packet; an unresolved
mathematical premise goes to B02. Large derived data follow
[LARGE_FILES.md][largefiles].

### RGD-E04

**Scope:** assess one named return/revision against its issued contract.
Check hypotheses and normalization, boundary completeness, signed mixed
terms, actual domain, all error payments, consumer implication and the
control screen. Reuse existing exact checks; run additional checks only
for changed formulas or unresolved issues. Record actual reviewer model
and effort, same-assistant/same-model or cross-model relationship, and
shared premises. Model changes do not create specialist independence.

**Output and completion:** one assessment in `reviews/` with an accepted
scoped result, required corrections or unresolved premise; update the
sole register and local navigation accordingly. One correction cycle
within the same contract is permitted; retain prior evidence. A changed
mathematical target is B02. A useful assessed pilot may make B03 ready;
a finite positive check alone does not. Update result-summary/avoid
indexes only when a qualifying result or closure warrants it under the
root policy, with one coordinated writer. This planning task claims no
such research milestone and creates no manuscript snapshot.

### RGD-B02

**Conditional repair path:** name the exact failed premise or residual
from the preceding return. Compare one repair with at most one alternate
mechanism, preserving the failed evidence and canonical source. Return
one revised E02/E03 packet with an explicit changed target and scope,
or a reasoned stop for that route. A failure of a pointwise probe sign
does not exclude its integrated estimate; a failed Gaussian comparator
does not exclude all order induction. Stop after this bounded comparison.
Further redesign requires a dated revision before dependent work.

### RGD-B03

**Conditional extension path:** given an assessed pilot, decide whether
its canonical input can control (19) for general \(r\). Track the growing
polynomial degree, boundary rank \(\max(r-k,0)\), small-index sector
\(1\le k<r\), neighboring-index transition and unbounded tail. Identify
lower-order and real-parameter positivity premises instead of importing
them from the order-three case.

**Bound and output:** assess one proposed induction mechanism and the
first next-order step. Return a quantified induction lemma and frozen
E02 follow-through, or the exact obstruction and domain where the pilot
still applies. Routine verification is assigned to Sol before it begins.
No arbitrary-order numerical campaign is authorized by a promising pilot.

### Controls, ownership and continuation

Every new claim must be classified as an identity, target reformulation,
sufficient conjecture, bounded diagnostic, proved estimate or scoped
obstruction, using [avoid/01][a01]. Explain the precise extra premise
tested by the [collision controls][controls]: weighted-square controls
change unit coefficients; Euler-factor controls change the source;
reflected and smooth positive-primitive controls lack the literal complete
canonical expansion. A control's failure of canonical reconstruction
does not tell us whether it satisfies an untested quantitative estimate.
A collision at positive heat time does not itself refute a time-zero
finite-order comparison. Claims about such a comparison need a matching
calculation or argument on the control.

Keep the [theta results][thetaresults] and [joint signed-estimate lesson][a12]
visible. No boundary deletion, separate positive-sector argument, generic
Gram positivity or use of the desired next-order sign may supply the
missing comparison. The [numerical-scope][a10], [known-baseline][a11],
[review][a05] and [status][a06] rules govern the evidence wording.

New derivations go in this investigation's `notes/`, code and small records
in `numerics/`, and assessments in `reviews/`. Versioned packets, when
useful, go in `research-progress/handoffs/`; create these folders when
there is content. Each packet records ID, parent, revision, input paths
and versions, actual author/model/effort, B/E classification, permitted
files, limits and stopping rule. Append a return rather than rewriting
an issued request or failed evidence.

One writer owns the local register at a time; reread it before updating.
Leave parent J/MC registers and sibling research artifacts unchanged
unless a separate coordinated integration is requested. The originating
chat retains its existing home; this planning chat is local history0001.
Use the [history tool][history] at turn boundaries. This plan schedules
no chats, agents or automatic research. No separate research-plan file
duplicates this section.

Initial continuation prompt:

> Read GPT_RESEARCH_MODEL_WORKFLOW.md, this overview's research plan r1,
> and the live RGD progress entry. Complete [B] RGD-B01: assess one
> theta-specific joint comparison for Q_{3,k}, keeping the k=1 boundary
> case and k=4 pure-volume case visible. Compare at most one alternative.
> Return a worked argument, scoped obstruction or explicit surviving
> obligation, and freeze any resulting E task for Sol before implementation.

## Sources and provenance

The starting scalar derivation is
[Radial Note73][radial73], following the geometry introduced in
[Radial Note01][radial01]. The complete determinant expansion,
its convergence conditions and the exact algebra record are in
[brainstorm Note06][n06] and its linked computations.
The [preceding brainstorm Note05][n05] records the distinction between
fixed-temperature box correlations and the earlier determinant integrand.

All of those materials retain their existing paths and review status.
The [originating chat][chat] remains registered in the Mellin-curvature
archive, as explained in the [local history guide](../chat-histories/README.md).
This overview is the author-requested separation of the radial Green
mathematical investigation from the earlier thermal interpretation.

[n06]: ../../brainstorm/notes/06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md
[n05]: ../../brainstorm/notes/05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md
[checker]: ../../brainstorm/numerics/radial_green_determinant_check.py
[record]: ../../brainstorm/numerics/RADIAL_GREEN_DETERMINANT_CHECK_20261104.json
[radial73]: ../../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md
[radial01]: ../../../../../05_radial_theta_collision_geometry/notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[parent]: ../../README.md
[jensen]: ../../../README.md
[kernels]: ../../09_source_overlap_kernels/README.md
[dynamics]: ../../08_open_quantum_dynamics/README.md
[chat]: ../../chat-histories/0004_2026-11-04T02-13-44Z_explore-hamiltonian-expectation-formulation.json
[results]: ../../../../../../../result-summaries/README.md
[thetaresults]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

[workflow]: ../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[largefiles]: ../../../../../../../LARGE_FILES.md
[history]: ../../../../../../../tools/CHAT_HISTORY.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a06]: ../../../../../../../avoid/06_status_stronger_than_the_evidence.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md

[prepnote]: ../notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md
[inductionhandoff]: ../research-progress/handoffs/10_RGD_B03_R2_INDUCTION_INDEX_ERROR_AND_MODEL_CONTINUATION_20261104.md
[priorassessment]: ../research-progress/handoffs/09_RGD_E04_R3_NEXT_ORDER_ASSESSMENT_AND_MODEL_CHANGE_20261104.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
