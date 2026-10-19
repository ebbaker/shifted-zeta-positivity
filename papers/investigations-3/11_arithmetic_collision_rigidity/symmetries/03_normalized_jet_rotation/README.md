# S03 Normalized first jet rotation and its defect

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Exact comparison identity and a bounded correlated residual estimate are
available; the uniform arithmetic estimate remains open.

**Opening execution, 18 October 2026:** the [signed transport comparison](notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md)
evaluates the complete defect integral by a first-jet endpoint primitive.
A proved comparison shows that scalar transport with independent endpoint
residual envelopes cannot improve on the ideal direct radius test. On the
prescribed height-1000 pilot, direct exclusion passes; the standard Cauchy
payment fails a certified point witness, while sharper joint-disk transport
remains inconclusive on the fixed cover. [192/256-bit checks](numerics/README.md),
[internal review](reviews/01_SIGNED_TRANSPORT_INTERNAL_REVIEW_20261018.md).
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual reasoning effort ultra**. No new region or arithmetic correlation
estimate is claimed; further work needs such a bound or a measured cost gain.

**Correlated continuation, 18 October 2026:** [Note 02](notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md)
certifies the complete residual increment below `0.000266448`, versus
`0.002011747` for independent endpoints from the same source data. Paid
transport now has radius greater than `1.124460`; the matched independent
transport gives `1.122848`, while direct exclusion remains stronger at
`1.336516`. A nominal oscillator calibration has complete normalized
first-jet error below `0.000266449`, with exact anchor coefficients exported
in the [192/256-bit records](numerics/README.md). This supersedes the opening
round's finite transport uncertainty using additional source information;
its independent-endpoint comparison theorem remains unchanged.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**; [internal review](reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md).
No new height range, uniform arithmetic theorem or performance gain.


**S03-T1, 19 October 2026:** [Note 03](notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md) derives a single complete
source-filtered residual with explicit logarithmic mode symbols, full
correction derivatives, tail accounting and normalized heat forcing.
A certified witness excludes separate source/approximation prefix triangle
payments: they must exceed `1.912087` on B. This is a scoped obstruction,
not a new recombined residual allowance. [Separate same-model review](reviews/03_FILTERED_RESIDUAL_INTERNAL_REVIEW_20261019.md)
and [192/256-bit checks](numerics/S03_FILTERED_MECHANISM_20261019.json).
S03-T1 Complete; S03-T2 Ready to estimate the signed combined functional.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**; no new coverage or specialist review.

## Question and connection to the manifold work

Can the actual arithmetic amplitudes and phases be controlled so that the
normalized first jet approximately rotates without reaching the origin?
This extends the existing [rotation proposal][brainstorm] with the exact
defect derived in [Note 07][note]. It is the spectral counterpart of
Investigation 22's oriented real Gauss-map picture. The plane's algebraic
quarter turn is not automatically a symmetry of a scalar derivative jet.
Use the [program guide][guide] for scope and the [cutoff direction][cutoff]
for the first proposed source of an improved signed approximation.

## Exact equations

Fix t and a real interval where the [existing normalizer][outer] has
\(\mathcal A_t>0\) and \(\omega=\partial_x\vartheta_t\ne0\). Put
\[
 Q=H/\mathcal A_t,\quad \theta=\vartheta_t(x),\quad
 D_\theta=\omega^{-1}\partial_x,\quad W=Q-iD_\theta Q.
\]
The complete defect and its transport are
\[
 \mathscr R=(D_\theta^2+1)Q
 =Q+Q_{xx}/\omega^2-\omega_xQ_x/\omega^3,
\]
\[
 D_\theta(e^{-i\theta}W)=-ie^{-i\theta}\mathscr R,
\]
\[
 e^{-i\theta}W(\theta)=e^{-i\theta_0}W(\theta_0)
       -i\int_{\theta_0}^{\theta}e^{-is}\mathscr R(s)\,ds.
\]
The leading pair Q=2cos(theta) has zero defect. A separately proved bound
on the modulus of the complete complex integral, uniformly smaller than a
certified nonzero initial radius, would preserve nonvanishing on that
interval. This is an elementary comparison identity; its arithmetic bound
has not been supplied. No division by W is used at a candidate collision.

With \(J=(Q,-D_\theta Q)\) and
\(a=\partial_x\log\mathcal A_t\),
\[
 E=\mathcal A_t^2\{J_1^2+(aJ_1-\omega J_2)^2\}.
\]
The change of coordinates preserves the collision set, but a uniform
comparison of energies needs bounds on this matrix. The phase is the
specified explicit theta phase, not the argument of an unknown nonvanishing
physical jet.

## Read in this order

1. [Note 07][note], equations (7)–(12), and [Review 14][review].
2. [Exterior contract][outer] for the actual normalizer, phase, and errors.
3. [Earlier collision manuscript][earlier]: `sc:vector` retains amplitude
   drift; `lem:phase` is the existing conditional amplitude–phase test;
   `sc:packet` gives the adjacent-packet obstruction.
4. [Investigation 22 manuscript][manifold], the marked real Gauss-map
   section. Its signed angular formula is prior work, not a new bound.

## Bounded first task

Take a complete fixed-cutoff approximation, initially from S02 or the
existing contract, on one finite interval with a certified initial jet
and lower bound for absolute omega. Derive its complete complex defect
integral, retaining the signed correction and correlations between modes.
Do not replace it immediately by the sum of absolute mode defects.

Compare direct first-jet exclusion with this transport calculation on the
same interval. Directly bounding the pointwise defect uses a second derivative;
the [opening endpoint primitive](notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md)
avoids that residual derivative payment and exposes the independent-endpoint
comparison limitation. A holomorphic residual
r bounded by eta on a radius-d disk obeys
\[
 |(D_\theta^2+1)r|
 \le\eta\{1+2/(d^2|\omega|^2)+|\omega_x|/(d|\omega|^3)\}.
\]
Pay that error, integration error, phase uncertainty, and interval-wide
propagation. Any claim about the entire phase interval needs uniform
coverage, not just endpoint agreement.

The known mode frequencies satisfy the leading relation
\(D_\theta\phi_n\sim1-2\log n/\log(x/(4\pi))\) in the cited
high-height regime. Near the cutoff this ratio is close to zero. Thus the
complete sum has no established common rotation speed; a useful estimate
must handle these modes through their signed correlations.

## Controls and decision rule

The transport identity holds for every twice differentiable real function
with the prescribed nonzero phase derivative. Every relevant collision
control therefore shares it. On a domain containing an event, the complex
integral cancels the initial rotating jet at that event, so the proposed
strict smaller-than-initial-radius bound must fail. The distinguishing
premise must be a new quantitative arithmetic bound, not the identity.

Pass only with a certified finite propagation advantage, a smaller paid
error/cost, or a precise obstruction to the selected defect estimate. Stop
if the criterion merely renames nonvanishing, assumes the unknown jet
angle, loses to the direct first-jet test after second-derivative costs,
or relies on an unproved uniform rotation of all modes.

## Outputs and handoff

Create `notes/`, `numerics/`, and `reviews/` here as work is executed.
Record the anchor, phase range and orientation, omega bound, complete signed
integral, residual payment, physical conversion, control failures, comparison
gate, and actual model/effort. Use [S04][scaling] to identify the regimes
where the defect is small or large. Follow the [guide][guide] for provenance
and chat registration.

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[brainstorm]: ../../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[note]: ../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[review]: ../../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[outer]: ../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[manifold]: ../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[cutoff]: ../02_cutoff_reflection/README.md
[scaling]: ../04_time_height_scaling/README.md

**S03-T2, 19 October 2026:** [Note 04](notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md) proves a complete analytic-only increment allowance **<0.812260**, versus <0.827470 for same-input independent endpoints (>1.8381% decrease). Known phase and real-Schur jet geometry suffice; no source polynomial is reused. The retained source-informed <0.000266448 allowance remains stronger. A separately defined absolute shifted-channel kernel-variation rule pays >4037.45136 in one old cell; this is a method-payment obstruction, not a residual lower bound. [192/256-bit checks](numerics/S03_PHASE_ANALYTIC_ALLOWANCE_20261019.json), [kernel check](numerics/S03_KERNEL_VARIATION_OBSTRUCTION_20261019.json), [separate same-model review](reviews/04_PHASE_ALLOWANCE_AND_KERNEL_OBSTRUCTION_INTERNAL_REVIEW_20261019.md). T2 Complete in its bounded analytic-only branch; T3 Ready. Arithmetic cancellation and growing-height control remain open; no new coverage. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

**S03-T3, 19 October 2026:** [Note 05](notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md) implements the exact anchor calibration and compares complete real first jets on the same B cover/data. Paid radius calibrated pointwise **>1.3859351576**, calibrated scalar **>1.1288659652**, strongest source direct **>1.3898732635**. Giving the source test the same propagation is essential; raw source >1.3473946960 is a weaker implementation. [Anchor export](numerics/S03_T3_ANCHOR_EXPORT_20261019.json), [192/256-bit ledger](numerics/S03_CALIBRATED_CONSUMERS_20261019.json), [controls](numerics/S03_T3_CONTROLS_20261019.json), [separate same-model review](reviews/05_CALIBRATED_CONSUMER_COMPARISON_INTERNAL_REVIEW_20261019.md). T3 Complete; stop this fixed-box comparison and retain reusable calibration/direct interfaces. No new residual theorem, coverage, second-jet error or matched-cost advantage. For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

**G3 arithmetic continuation, 19 October 2026:** [Note 06](notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md)
derives the prescribed first gamma/heat correction, with uniform relative
mode errors <6e-7, <6e-8 and <1.2e-8 through spatial order 2. Its complete
finite eight-mode filtered error on B is <3.874872e-6. Certified center
finite/edge defects +0.000133439545 and -0.000136027672 explain the small
-0.000002588127 difference locally; a no-fit RS hierarchy retains the
essential gamma prefactor. A finite Cauchy–Riemann telescope identifies two
endpoint terms for the remaining coherent edge payment. [192/256 records](numerics/README.md),
[separate same-model review](reviews/06_ARITHMETIC_GAMMA_AND_EDGE_INTERNAL_REVIEW_20261019.md). **G3 remains partially explained**:
the independent complete edge jet and uniform signed prefix bounds are open.
No new consumer allowance, height range or coverage. Next bounded work is
that edge payment on the same B,N=8, before further consumer comparisons.
For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

**G3 complete arithmetic edge and increment, 19 October 2026:**
[Note 07](notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md) closes the fixed-pilot edge/prefix obligation left by
Note 06. RS8, finite CR coherence, true gamma prefactor, exact Gaussian
tails and a paid moment/profile polynomial give complete normalized edge
errors <6e-8,<6e-8,<1.2e-7 through spatial order 2. Combining the retained
signed finite and edge corrections before endpoint payment proves
**|I_r|<0.000854 on all B**, without source quadrature or H Taylor data.
The independent analytic-only <0.812260 allowance is improved by >950-fold;
source-informed <0.000266448 remains stronger. [Nominal 192/256 records](numerics/README.md)
use 512 guardbits for high profile derivatives; [fresh same-model review](reviews/07_COMPLETE_ARITHMETIC_EDGE_AND_INCREMENT_INTERNAL_REVIEW_20261019.md)
and192 replay pass. No new consumer, cost or coverage claim. The fixed-pilot
arithmetic task is complete; height-uniform input remains open. Stop this
comparison unless a new concrete objective earns refinement. For Edward
Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.
