# Prioritized routes to a theta specific signed bound

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session. Three collaborating tasks compared analytic, geometric and numerical proposals; the coordinator checked the formulas below. This is a strategy note with elementary derived diagnostics, not a new theta sign certificate or manuscript revision.

## Continuation update

The [completed pilot](04_ARITHMETIC_CONTOUR_AND_CHORD_CONTINUATION_20261015.md) supersedes two scope judgments below. Support-only localizers admit a certified collision even with the first source endpoint. The chord warning in Section 3 applies to one fixed inner scaled window; uniform short-interval coverage also permits fixed nearby endpoints, for which errors o(sqrt(E(start))) suffice. Consequently some Gaussian cutoff costs are admissible when their growth rate stays strictly below the tail rate. The original proposals below are retained as the record of the experiment design.

The strongest next program is a small signed inequality that uses identifiable theta arithmetic and survives physical cancellation. The [latest continuation](../00_research_coordination/02_CONNECTION_BRIDGE_AND_INNER_TURNING_CONTINUATION_20261015.md) makes two candidates concrete: a finite angular-gap inequality with no energy denominator, and a stationary signed bound allowing much larger cutoff costs than a polynomial. Square-lattice constraints and a transverse period-two identity are possible inputs. Neither is yet a successful mechanism.

## Priority and expected deliverable

| Priority | Route | First bounded deliverable | Reason to continue |
| --- | --- | --- | --- |
| Primary target | A fixed angular gap written as a two-point product | Exact full-source kernel, primitive endpoints and a candidate signed certificate | A simpler observation of the universal collision core, valid for both branches without a physical-to-angular energy conversion |
| Primary arithmetic input | Square-lattice moment constraints in a stationary certificate | A small explicit hierarchy and its dual identity, with a paid remainder | Uses the actual support `pi*n²`, beyond positivity or source concavity |
| Alternative target | A signed cutoff bound with sub-Gaussian cost | One complete cutoff family satisfying an energy-relative estimate | The existing analytic-collision argument tolerates costs as large as `exp(a*N^beta)`, `beta<2` |
| Bounded geometric pilot | Jacobi heat plus period-two transverse transport | One complete bilocal identity with the bottom edge and shifted weights retained | Tests a genuine theta symmetry while preserving the physical point observation |
| Parallel coverage work | Evaluate the unresolved outer constants in Investigation 21 | An explicit starting height that can be joined to a finite certificate | Offers measurable domain improvement, though it does not alone settle the small-time cusp |

These are judgments about useful next deliverables, not estimates of the probability of proving RH.

## 1. Replace angle division by a finite two point inequality

Fix a branch `j=0,1`, write `W=h_j`, and let `y=x+ell>x`. Assume the **full** stationary condition `W_x(t,x)=0` and `W(t,z) != 0` throughout `[x,y]`. The interval therefore has one sign of W and a unique continuously lifted increment from its stationary start. For `0<theta_*<pi/2`,

\[
 \Delta\alpha_j\le\theta_*
 \quad\Longleftrightarrow\quad
 W(t,x)\{\tan(\theta_*)W(t,y)-W_x(t,y)\}\ge0.
\]

Indeed `Delta alpha=arctan(W_x(t,y)/W(t,y))`, and `W(t,x)W(t,y)>0`. A prescribed uniform short-interval bound with any fixed `theta_*<pi/2` excludes collisions, because the known collision intervals have W of fixed sign and approach a quarter-turn. Restricting this proposed bound to W-zero-free intervals is sufficient; it is not necessary to control every jet-regular interval across a zero of W.

The especially simple choice `theta_*=pi/4` gives

\[
 \boxed{\mathcal C_j(t;x,y)
 =h_j(t,x)\{h_j(t,y)-h_{j+1}(t,y)\}\ge0.}
\]

The required statement is: in a fixed neighborhood of each covered candidate event, the inequality holds for every full stationary start and every `0<ell<=ell_0` whose interval is W-zero-free. The length `ell_0>0` must be prescribed uniformly through the event. Choosing it from an observed energy floor would assume the missing conclusion.

At a collision of multiplicity `2r+j`, put `s=T-t` and use its full predecessor `x=chi(s)`. The new inner-profile theorem gives

\[
 \frac{\mathcal C_j(T-s;\chi(s),\chi(s)+s\xi)}{k^2s^{2r}}
 \longrightarrow1-r\xi.
\]

Taking the fixed value `xi=2` makes this negative for every `r>=1`. This is a clean adversarial test. For a fixed regular stationary start, the separate Taylor expansion is

\[
 \mathcal C_j(t;x,x+\ell)=W(t,x)^2+\ell\mathcal L_j(t,x)+O(\ell^2).
\]

The remainder here is a local Taylor statement, not a uniform collision estimate.

Let `w_t=e^{tu²}Phi` and `c_j(x,u)=u^j cos(xu+j*pi/2)`. The exact kernel is simply

\[
 \mathcal C_j=\iint w_t(u)w_t(v)c_j(x,u)
 [c_j(y,v)-c_{j+1}(y,v)]\,du\,dv.
\]

Its symmetrization in u,v has the same integral. The existing primitive bridge, with `I_j(t,z)=int psi(u)(partial_u²-1)[e^{tu²}c_j(z,u)]du`, gives

\[
 64\mathcal C_0=(\tfrac12+I_0(t,x))
 [\tfrac12+I_0(t,y)-I_1(t,y)],
 \qquad
 64\mathcal C_1=I_1(t,x)[I_1(t,y)-I_2(t,y)].
\]

Preserve the affine combination `I_0+1/2` before estimation. This target avoids dividing by E and avoids identifying the second branch's angular energy with E. It still asks for a difficult theta-specific sign; the reformulation itself is not progress on that sign.

## 2. Use arithmetic support rather than generic moment positivity

For `q>0`, define

\[
 \Psi(q)=\sum_{n\ge1}e^{-\pi n^2q},\qquad
 M_k(q)=\sum_{n\ge1}(\pi n^2)^k e^{-\pi n^2q}.
\]

The source is

\[
 \Phi(u)=q^{1/4}[2q^2M_2(q)-3qM_1(q)],\qquad q=e^{4u}.
\]

In addition to ordinary moment positivity, the gaps in the square lattice give

\[
 \boxed{M_2-5\pi M_1+4\pi^2M_0
 =\sum_{n\ge1}(\pi n^2-\pi)(\pi n^2-4\pi)e^{-\pi n^2q}\ge0.}
\]

More generally, for adjacent nodes `lambda_m=pi*m²` and `lambda_(m+1)`, the matrices

\[
 \big[M_{a+b+2}-(\lambda_m+\lambda_{m+1})M_{a+b+1}
       +\lambda_m\lambda_{m+1}M_{a+b}\big]_{a,b=0}^d
 \succeq0
\]

are positive semidefinite: testing a vector integrates the square of its polynomial against `(lambda-lambda_m)(lambda-lambda_(m+1))`, nonnegative at every lattice node. This proof uses the discrete support, not log-concavity. It does not fix the lattice weights; a finite list of these constraints does not characterize theta.

The proposed experiment is to use a few such localizing matrices in a dual identity for the complete chord or stationary kernel. Multiples of the full stationary observation may be added because their integral vanishes on the tested set. The resulting identity must account for both source variables, phases, the affine primitive endpoint and all tails.

A useful outcome is a concrete nonnegative arithmetic term plus a remainder with the required physical scaling. If the relaxation admits a colliding control, its constraints are insufficient. A failed small ansatz rejects that ansatz, not every hierarchy. Simply bounding `M_k` or replacing the oscillatory observation by a positive source norm does not address the target. The existing [primitive-compatible control](../../../21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) already rules out a large collection of generic positivity assumptions.

## 3. Accept a substantially larger cutoff cost where the transfer permits it

For the **stationary Laguerre target**, a useful sufficient family is

\[
 \mathcal L_j\ge-A E\exp(aN^\beta)-B\exp(-cN^2),
 \qquad 0<\beta<2,
\]

for every sufficiently large integer N, on the full stationary sets in a declared domain containing the full predecessor neighborhoods of every collision claimed excluded. Without that coverage the exclusion is only local. Assume A,a,B are nonnegative and locally bounded, c is locally bounded below by a positive constant, beta is fixed, and the cutoff threshold is locally bounded through candidate events. The coefficients must be prescribed from the complete source.

On one such neighborhood choose fixed constants `M>=max(1,sup B)` and `c_0>0` with `c>=c_0`, and a fixed upper bound `N_0` for the cutoff threshold. Set `N=ceil(max(N_0,sqrt(log_+(M/E)/c_0)))` for `E>0`, where `log_+(z)=max(0,log z)`. The Gaussian remainder is then at most E. The resulting relative loss is

\[
 \exp\{C[\log(M/E)]^{\beta/2}\}=E^{-o(1)}
 \quad(E\downarrow0).
\]

Along a finite-multiplicity predecessor, `E` is asymptotic to a positive constant times `s^(2r)` and `-L_j/E~r/s`. The subpower loss cannot accommodate that pole. Thus an `exp(aN)` cost is acceptable; requiring a polynomial cost would reject some potentially useful mechanisms unnecessarily. This uses the existing [subpower collision-transfer reasoning](../../../21_quaternion_theta_geometry/notes/02_signed_cusp_control/44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md).

The indispensable condition is still the factor E. An absolute source allowance does not become useful merely because its cutoff growth is moderate. Finite successful cutoff tests do not prove the all-N family. The Gaussian cutoff tail must be proved for the chosen complete decomposition, not imported from a different cutoff convention.

This loss criterion must not be transferred unchanged to the chord target: the chord divided by central energy has a finite negative collision limit, whereas `L_j/E` has a pole. A generic subpower E-loss could swallow the chord violation. Keep the two acceptance criteria distinct.

## 4. Give transverse geometry one specific arithmetic task

The Chern connection and the Jacobi heat connection should be compared using the globally defined smooth horizontal lift

\[
 Y=\partial_\tau+s\partial_z,\qquad s=\operatorname{Im}z/q.
\]

Fiber translation sends `s` to `s+n` and pushes Y to the same expression. For `h_b=e^b h`, direct expansion gives

\[
 \boxed{\nabla_Y^b-\frac{D^2}{4\pi i}
 =\left(\partial_\tau-\frac{\partial_z^2}{4\pi i}\right)
   +b_\tau+\frac{i}{4q}.}
\]

The last terms equal the Chern coefficient of the fiber L² metric `e^b(2q)^(-1/2)`. Consequently projection onto the one-dimensional theta section space may leave only a scalar identity. The standard theta heat-connection framework is described in [Andersen and Blaavand, Section 6](https://arxiv.org/html/1106.1564v1).

There is an exact arithmetic discriminator: fiber multipliers force a holomorphic section to be `a(tau)theta`, and Jacobi heat forces `a'=0`. This follows directly by comparing its periodic Fourier coefficients, then applying the heat operator. It identifies information missing from generic collision controls, but uniqueness of theta is not an inequality for its physical transform.

A concrete transverse calculation uses **period two**, not curvature positivity alone. Set

\[
 A(\tau)=(-i\tau)^{1/4}
  [\tau^2\partial_\tau^2+\tfrac32\tau\partial_\tau]\vartheta(0,\tau),
\]
\[
 \eta_{t,x}(\tau)=\tfrac14
 e^{t\operatorname{Log}(-i\tau)^2/16}A(\tau)
 \cos[x\operatorname{Log}(-i\tau)/4]\,\frac{d\tau}{\tau}.
\]

Use the branch of Log on `Re(-i*tau)>0`. This form is holomorphic in the upper half-plane and its integral on `i -> i infinity` is H. Cauchy's theorem on `0<=Re(tau)<=2`, `Im(tau)>=1`, followed by the uniformly decaying top edge, gives

\[
 H(t,x)=\int_i^{2+i}\eta_{t,x}
       +\int_{2+i}^{2+i\infty}\eta_{t,x}.
\]

The theta derivatives are period two. The shifted polynomial, logarithmic, heat and cosine factors are **not** periodic and must remain. The bottom edge is explicit. Apply this identity to the complete two-source product before any absolute estimates.

The first deliverable should identify a term from this period relation that improves the selected chord or stationary observation. Stop if everything reduces to an existing scalar identity, or if the only available bound pays separate contour norms with no suitable physical scaling. The external spectral variable x is not the elliptic coordinate p; the formula above specifies their actual relation.

## 5. Run a discriminating pilot rather than repeat favorable signs

A pilot should test the proposed decomposition and its coefficients, not just evaluate a quantity already known positive in a finite theta region.

- Start with exact heat polynomials of multiplicities 2, 3, 4 and 5, including asymmetric and negative-amplitude germs. At `ell=C*s/r`, recover the angle `arctan C`; the pi/4 chord must fail for `C>1`.
- Include the proven smooth positive-primitive collision controls. A numerical use of a fixed positive damping requires its own certified collision bracket; an existential small-damping argument is not a numerical parameter value.
- Use complete theta stationary roots from the [existing certified baseline](../../../21_quaternion_theta_geometry/notes/03_effective_bridge/40_FIXED_THETA_STATIONARY_BASELINE_20261015.md), then fresh predeclared observations once the mechanism is fixed. Keep both branches and full interval regularity.
- Record every signed component, endpoint and remainder. Freeze the coefficient rule before validation; never define it by dividing by observed E.
- Treat a certified negative slack as rejection of the stated proposal, an enclosure containing zero as undecided, and finite success as a reason to seek an all-cutoff or unbounded-domain proof.

The conventional finite-plus-asymptotic route has a successful precedent in [Polymath's effective heat-flow estimates](https://arxiv.org/abs/1904.12438). In this repository, evaluating the unresolved outer constants is a distinct useful project. It cannot substitute for a small-time cusp argument.

## 6. Directions to defer and the reasons

**Canonical fiber norms.** There is a precise obstacle for the natural normalized lift. In the common unitary fiber realization,

\[
 \Psi_u(r,s)=(2q)^{1/4}\sum_{n\in\mathbb Z}
 e^{-\pi q(n+s)^2+2\pi inr},\qquad q=e^{4u},
\]

one has `||Psi_u||=1` in the unit square, and

\[
 \langle\Psi_u,\Psi_v\rangle=\operatorname{sech}(2(u-v))^{1/2}.
\]

Integrating r first removes unequal Fourier modes, and summing the s intervals gives the elementary Gaussian integral. For the natural source lift `S_u=(partial_u²-1)Psi_u/16`, differentiation gives

\[
 \langle S_u,S_v\rangle
 =\frac{105\operatorname{sech}(2d)^{9/2}
       -72\operatorname{sech}(2d)^{5/2}}{256},\quad d=u-v,
 \qquad \|S_u\|^2=\frac{33}{256}.
\]

Yet `S_u(0,0)=2^(1/4)Phi(u)` decays rapidly. Thus this norm loses the physical point observation's decay. The ordinary Bochner integral with weight `e^(tu²)cos(xu)` does not exist for `t>=0`. Even the norm-improper integral fails: choose arbitrarily late short intervals with cosine positive and nearby overlaps bounded below, and test their increments against the initial state on each interval. The increment norms stay bounded away from zero. This does not rule out scalar evaluation first, a different space or a justified regularization. Point evaluation is unbounded on the stated L² space. The formulas were independently derived and checked analytically in this brainstorming turn; no new numerical verification record is claimed.

**An unchanged compact K3 extension.** On a compact Kähler surface with its complex orientation, an ASD Chern curvature has `i Lambda F=0`. The compact Bochner identity then forces every holomorphic section to be parallel; a nonzero section trivializes a line bundle, contradicting degree one on elliptic fibers. Equivalently, a nonempty effective zero divisor has positive Kähler area, whereas ASD gives zero degree against the Kähler form. Thus a compactification cannot preserve a smooth ASD Chern connection, the degree-one theta line bundle, and its nonzero holomorphic section unchanged. The vanishing principle is recorded in [Kim, Sections 1.9–1.10](https://archive.mpim-bonn.mpg.de/3830/1/preprint_1990_3.pdf). Singular or meromorphic data, boundary terms, or a changed connection require a new specified mechanism.

**Global Pick or Hermite–Biehler positivity.** These can be useful factorization destinations, but may already demand the real-rootedness one is trying to establish. Small quotient-free kernel matrices are reasonable rejection tests only after a precise kernel is proposed. Particular historical de Branges positivity conditions fail for the associated zeta spaces; this does not invalidate the whole theory, but makes exact formulation essential. See [Conrey and Li](https://aimath.org/~kaur/publications/41.pdf).

**Separate Poisson sectors, extra lifts and generic source positivity.** Investigation 21 already records positive-heat integrability failures for isolated modes and sectors, and collisions compatible with positive primitives, strong concavity and fast decay. Revisit these only with a new cancellation-preserving identity and a declared physical payment.

## Recommended sequence

First, select the pi/4 chord or the stationary cutoff target and keep its quantifiers fixed. Derive its full kernel in the primitive/arithmetic variables. In parallel, test a small square-gap localizing hierarchy and perform the period-two contour calculation. Use the known collision controls to reject generic mechanisms immediately. Continue only when one route exposes an explicit arithmetic term or remainder estimate with the required scaling; then certify that fixed proposal and address domain coverage.

No proposed route currently supplies the missing theta-specific bound. The useful change in emphasis is to demand a measurable signed benefit from each arithmetic or geometric construction before increasing its complexity.
