# Research progress and priorities for theta collision control

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session metadata. Three collaborating readers assessed the analytic criterion, arithmetic mechanisms and wider research portfolio. This is an internal research assessment, not external refereeing or formal verification.

The investigation has made substantial progress in identifying the precise obstruction a proof must overcome. The fixed-endpoint chord theorem gives a sharp, multiplicity-independent target; the weighted-square collision eliminates an entire relaxation; and reflection rigidity identifies arithmetic information that survives that test. The central missing result remains an independently proved theta-specific signed inequality. Further work should concentrate on that inequality, with each proposed identity required to demonstrate a useful sign or a remainder that vanishes at the physical scale.

The highest-value next experiment is to preserve the complete starting factor of the chord, approximate only its endpoint expression, and exploit elliptic coefficient translation in the resulting signed core. A new conditional transfer observation removes the need to compare cutoff growth and tail rates when that factor is preserved. A second observation allows positive averages of short chords, giving more freedom in the test kernel. Both are proved in the accompanying [analytic note](../notes/02_signed_turning_control/03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md); neither establishes the missing theta bound.

## Progress and the remaining gap

The full [manuscript](../manuscript/theta_manifold_geometry.tex), [Overview 02](../research-overview/02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md), [continuation note](../notes/00_research_coordination/04_ARITHMETIC_CONTOUR_AND_CHORD_CONTINUATION_20261015.md), and their detailed supporting notes give the following picture.

| Established contribution | Why it matters | What remains |
| --- | --- | --- |
| Every finite collision produces a chord of negative order square-root starting energy | One exponent works for both parity branches and all multiplicities; exact chord positivity is unnecessary | A theta-specific lower bound with smaller error |
| Complete source and primitive formulas retain signed cross terms and endpoint constants | The physical quantity to be estimated is now explicit | A favorable term, rather than another equivalent identity |
| A positive weighted-square source collides while satisfying every support-only localizer and the first source endpoint | Increasing only support constraints cannot solve the stated problem | A constraint that genuinely couples coefficients |
| Full reflection, with the stated normalization and growth assumptions, forces the theta coefficients | The arithmetic discriminator is precisely identified | An inequality extracted from that discriminator |
| Geometric and contour controls expose lost signs, lost physical scale and artificial cancellations | Several attractive but insufficient mechanisms can be set aside | A specific signed benefit from any new geometric construction |

The sharpest conceptual improvement is the fixed endpoint. On the full predecessor of a multiplicity `2r+j` event,

\[
\mathcal L_j/E\sim-r/(T-t),\qquad
\mathcal C_j/\sqrt E\longrightarrow-d_\delta<0.
\]

The second law avoids a multiplicity-dependent power target. It does require a nearby endpoint that remains a positive distance from the limiting event as time approaches it. A test only at one shrinking scale would lose that advantage. Both branches use `E=H^2+H_x^2` at the complete stationary start.

This is progress in reduction, discrimination and error accounting. There is still no new global theta sign theorem in these documents. The geometric constructions and finite assertion counts should not be interpreted as a measure of distance to RH. The most important next milestone is a signed arithmetic estimate surviving the existing controls.

## Priority one Preserve the starting amplitude through every remainder

Write `W=h_j(t,x)` and `D=h_j(t,y)-h_(j+1)(t,y)`. Then `C_j=WD` and `|W|<=sqrt(E)` for both branches. If `D_N` approximates only D, the identity

\[
\mathcal C_j=W D_N+W(D-D_N)
\]

preserves the small complete starting factor. The accompanying note proves a Gaussian bound for the ordinary theta endpoint tail, uniform in all real endpoint coordinates and on every time interval bounded above.

The signed target becomes

\[
W D_N\ge-K_NE,
\qquad |D-D_N|\le\varepsilon_N\longrightarrow0,
\]

which implies

\[
\boxed{\mathcal C_j\ge-K_NE-\varepsilon_N\sqrt E.}
\]

Here `K_N` must be prescribed and locally bounded through a possible event for each fixed N. Its growth with N can be arbitrarily fast. Divide by square-root energy on a fixed-endpoint predecessor, let time approach the event at fixed N, and then choose N large enough that `epsilon_N<d_delta`. This contradicts the collision law. The same spatial endpoint must remain admissible for arbitrarily large N; time thresholds may depend on N if each eventually covers that predecessor.

This refinement is consequential. For the mixed family

\[
\mathcal C_j\ge-AE e^{aN^2}-B\sqrt E e^{-cN^2},
\]

the optimized exponent is

\[
p=\frac{a+2c}{2(a+c)}>\frac12\qquad(a\ge0,\ c>0),
\]

with the usual subpower integer-rounding factor. There is no requirement `a<c`. The original rate-gap theorem remains correct for its different, pure-tail family. Retaining the amplitude gives a more permissive target; it does not magically improve an arbitrary absolute remainder.

**First deliverable:** derive one complete expression for `W D_N` using exact full stationarity and a coefficient-coupling identity, with every boundary term present. Exhibit a favorable term and an independently bounded `K_N`, or identify exactly why that proposed decomposition fails.

**Decision gate:** continue only if the core inequality is obtained without dividing by an observed energy floor, substituting truncated stationarity, or estimating a starting-factor error separately. A finite theta sign table does not establish the required local boundedness through an unknown event. The easy Gaussian tail is already available; the signed core is the research problem.

## Priority two Give elliptic translation a concrete signed task

For

\[
\Theta_a(z,\tau)=\sum_{n\in\mathbb Z}a_n
 e^{\pi in^2\tau+2\pi inz},
\]

direct reindexing gives the exact defect

\[
e^{\pi i\tau+2\pi iz}\Theta_a(z+\tau,\tau)-\Theta_a(z,\tau)
=\sum_{m\in\mathbb Z}(a_{m-1}-a_m)
 e^{\pi im^2\tau+2\pi imz}.
\]

Full elliptic translation sets the left side to zero and forces adjacent coefficients to agree. This is a local coefficient relation that the weighted-square collision fails. For the symmetric cutoff `Theta_N=sum_(|n|<=N) exp(pi i n^2 tau+2 pi i n z)`, the defect reduces to exactly two boundary modes:

\[
e^{\pi i\tau+2\pi iz}\Theta_N(z+\tau,\tau)-\Theta_N(z,\tau)
=e^{\pi i(N+1)^2\tau+2\pi i(N+1)z}
-e^{\pi iN^2\tau-2\pi iNz}.
\]

At `tau=iq`, `q>=1`, `z=0`, these boundary terms decay at Gaussian rate in N; fixed-order derivatives add polynomial factors. The convention is the manuscript's period-one elliptic argument; see also [DLMF periodicity and quasi-periodicity](https://dlmf.nist.gov/20.2#ii).

**Proposed calculation:** insert this defect into the complete physical source operator and the endpoint-only chord core. Compare the direct coefficient-shift formulation with its modular-reflection form. Use stationarity subtraction before taking absolute values. Seek a telescoping or constrained quadratic representation whose remaining boundary contribution still carries W. All multiplier derivatives, physical heat weights and primitive constants must remain.

The finite defect is an identity, not a positivity argument. The calculation is worthwhile because it has an exact arithmetic discriminator and a small explicit boundary. Stop if the proposed identity reduces to the Jacobi heat equation or a scalar tautology without a signed improvement.

The transverse jet recurrence itself is not that discriminator. Its derivation from the Gaussian generating identity and Jacobi heat also applies to arbitrary fixed weighted theta series. The same is true of period two and the tested contour identity. These structures become arithmetically useful only when coupled to a relation such as full elliptic translation or reflection.

## Priority three Allow a positive average of endpoint chords

The all-endpoint hypothesis can be weakened. Choose a fixed nonnegative smooth function `rho` supported in `(0,1)` with integral one and define

\[
\overline{\mathcal C}_{j,\delta}(t,x)
=h_j(t,x)\int_0^1\rho(v)
 [h_j(t,x+\delta v)-h_{j+1}(t,x+\delta v)]\,dv.
\]

At a collision, write `W(T,a+z)=a_0 z^(2r)+O(z^(2r+1))`. The companion note proves

\[
\lim_{s\downarrow0}
\frac{\overline{\mathcal C}_{j,\delta}(T-s,\chi(s))}{\sqrt E}
=-2r|a_0|\delta^{2r-1}
\int_0^1\rho(v)v^{2r-1}\,dv+O(\delta^{2r})<0
\]

for every sufficiently small fixed delta. Therefore bounds with error `o(sqrt(E))` for a prescribed sequence `delta_k->0` suffice; no uniformity across k is required. At the event, first select a suitable fixed k, then approach in time. The one-sided positive averaging and full predecessor preserve the collision sign.

**Why explore it:** instead of proving a bound for every individual endpoint, choose a test profile whose transformed kernel works well with reflection or coefficient translation. The kernel acquires the explicit factor `M_rho(delta u)=int rho(v)exp(i delta u v)dv`. A carefully selected profile might admit a sign decomposition unavailable to a sharp endpoint. Smoothness alone does not establish that sign.

**First deliverable:** compare a small, predeclared family of averaging profiles in the same coefficient-coupled core identity. Retain the exact starting factor and use the mixed-remainder lemma. A failure of the sharp-endpoint ansatz should not automatically end the averaged route.

## Priority four Use endpoint controls to decide whether a finite hierarchy is useful

The existing collision fails `Phi'''(0)=0`. Adding that condition, then one or two more odd endpoint conditions, is a useful inexpensive discriminator. It is not a reason to assume that a finite hierarchy will succeed.

At fixed candidate `(T,x)`, collision conditions `H_a=H_(a,x)=0`, source endpoint conditions and primitive normalization are linear in the nonnegative weights. This makes a feasibility search and its dual a concrete experiment. Search across a declared bounded time-space region and enough square nodes, with suitable coefficient scaling. Certify a candidate collision and its nondegeneracy using interval methods; alternatively, certify a dual obstruction on the declared region with a complete tail bound. Failure of an optimizer to find weights proves neither infeasibility nor collision exclusion.

There are two valuable outcomes. A further collision shows that the added finite hierarchy still loses essential arithmetic information. A certified obstruction identifies a quantitative finite relation worth inserting into the chord identity. Neither result should be extrapolated to all hierarchy levels or all heights. Turning the infinite rigidity theorem into a finite estimate would also require quantitative control of omitted endpoint data or of the reflection defect; uniqueness alone supplies no stability constant.

## A separate route to measurable domain progress

The effective outer-domain program in Investigation 21 deserves a bounded parallel effort, but its attainable height should be assessed before investing heavily in the last arithmetic constant. [Note 58](../../21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) gives the conservative sufficient log-height

\[
L=\log(x/(4\pi))\ge
1+\max\{749376582912,
14000\log(663552G_0C_{\rm EP})\}.
\]

The first entry is the single integer **749,376,582,912**. Its size persists regardless of how favorably the missing exponent-pair constant is evaluated. This is a limitation of the present sufficient error budget, not a lower bound on the true onset of favorable signs. The separate hypotheses `tL>=61/24` and the imported validity threshold also remain.

The best first task here is a budget audit: identify the dominant enlargement, recompute the attainable overlap with the finite certified region, and determine whether a sharper approximation can reduce the gap. An evaluated outer theorem would still be valuable, even if it does not close the research program. Finite computation combined with effective asymptotics has a clear precedent in [Polymath's heat-flow estimates](https://arxiv.org/abs/1904.12438); that precedent does not supply the missing constants or coverage for this manuscript.

## Work to defer and conditions for reopening it

| Direction | Current decision | Evidence that would justify another attempt |
| --- | --- | --- |
| Higher support-only localizers | Stop for this relaxation | A genuinely new coefficient constraint |
| Additional calibrated or special-holonomy realizations | Defer | A specified signed term or physical-energy estimate inaccessible in the existing representation |
| Positive fiber norms | Defer the tested lift | A space and observation map preserving the actual physical decay and a proved energy comparison |
| Independent contour-sector estimates | Stop the tested budget | A bound for the recombined packet using real coefficient coupling and the starting amplitude |
| Compact ASD completion | Defer unchanged data | A precise modified boundary, singularity or connection construction that improves the signed estimate |
| Global Pick or Hermite–Biehler positivity | Defer an unspecified kernel | A concrete kernel with an independent positivity mechanism that does not assume the desired zero statement |

An exponential coefficient in finite spectral height is not itself fatal: the local collision criteria need boundedness near each finite event, not one global constant for all heights. The stronger reason to deprioritize the present contour route is that its arithmetic identities also admit the weighted collision control and no physical-scale signed core has emerged. Keep this logical distinction explicit.

## Recommended next research cycle

1. Use the two companion lemmas to fix the exact sharp or averaged chord target and preserve the complete starting factor.
2. Derive one elliptic-shift or modular-reflection identity for its signed core, including the exact boundary remainder. State the claimed favorable term before extending the geometry.
3. In parallel, search the next finite endpoint hierarchy for an adversarial collision. Test the proposed core on the existing polynomial and weighted-square controls to identify which additional hypothesis matters.
4. Only after fixing that mechanism, certify theta stationary points and intervals using a coefficient rule fixed in advance. Record the complete signed components and tails. Finite success supports an analytic extension; it is not the all-cutoff theorem.
5. Keep a separate domain-budget project, and assess whether it can produce a new verified region at a useful cost.

For a bounded research cycle, I would devote about half the effort to the coefficient-coupled core, one quarter to averaged kernels and adversarial endpoint controls, and one quarter to the outer-domain budget and independent review. The next decisive milestone is a coefficient-coupled signed decomposition with an independently bounded core and a remainder that retains the starting amplitude. An additional representation without that consequence should not become the main workstream.

## Review scope and provenance

The assessment read the entire current LaTeX manuscript and the two requested research documents, together with the relevant chord, source-bridge, reflection, contour, integration-review and outer-budget notes. The new mixed-remainder implication was independently derived by multiple readers and checked against the fixed-endpoint law. The positive-average criterion has a written local analytic proof and an explicit physical kernel. No existing numerical certificate was rerun for this strategic review, and no new numerical theta sign claim is made.

The reviewed manuscript has SHA-256 `114611f06f0928827045399561d2f83ca6ca9abc1d35a9d5cd7d406c845aa417`. The manuscript and its existing overview remain unchanged. The companion note records new conditional deductions separately from the strategic proposals above. This chat is registered under its actual title, **Review research paths**, as formal-replay history **19**, preserving the destination required by the local standing instruction.
