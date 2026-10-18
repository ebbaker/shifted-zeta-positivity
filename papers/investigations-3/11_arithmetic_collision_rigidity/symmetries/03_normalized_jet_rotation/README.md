# S03 Normalized first jet rotation and its defect

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Exact comparison identity available; the arithmetic estimate is open.

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
same interval. The latter uses a second derivative. A holomorphic residual
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
