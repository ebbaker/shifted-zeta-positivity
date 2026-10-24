# First bounded averaging and accuracy contract

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

**Status:** HDA-01 contract fixed for one pilot. This is an approximation
experiment, not an RH/simplicity criterion. Preliminary scouting preceded
this contract; the extended schedule and derivative checks below were
fixed before their full run. No preregistration claim is made.

## Target, domain and averaging

Keep the unnormalized field
\[
R=\mathcal F\rho_\epsilon,\quad U=\mathcal F\log(|H|^2+\epsilon^2),
\quad J=\mathcal F j,\quad Q=\operatorname{Var}_{\mathcal F}(S_x)
-\operatorname{Var}_{\mathcal F}(S_y),
\]
with the unchanged theta source and conventions of [Note 02][identities].
The primary regulator is \(\epsilon=10^{-4}\); use \(5\cdot10^{-5}\) for
sensitivity only, with no claim that either is already a zero-count limit.
The regulator remains fixed through every differentiated calculation.

Use the positive even unit-mass kernel
\[
k(q)=\frac{315}{256}(1-q^2)^4\mathbf1_{|q|\le1},\quad
\int q^2k(q)dq=\frac1{11},\quad\int q^4k(q)dq=\frac3{143}.
\]
Its zero extension is \(C^3\). An active coordinate of halfwidth \(h\)
uses \(h^{-1}k(q/h)\); zero width means no averaging in that coordinate.
The full filter is the product of the three kernels in \((t,x,y)\).
Time averages are centered and use both earlier and later source values.
They are an offline description, not a causal forecast. Widths are fixed
for each run, so there are no moving-width commutators.

Observation centers lie in
\([-1/4,1/4]\times[26,30]\times[-1/2,1/2]\).
The explicit sample centers are
\[
c_1=(0,28,1/2),\quad c_2=(1/4,26,1/4),\quad
c_3=(-1/4,30,1/2).
\]
These are a small finite sample, not coverage of the box or of a large
zero population. Evenness/conjugation give corresponding reflected
observations but do not increase independent evidence.

For every center, use halfwidths \((\tau,\ell_x,\ell_y)\)
\[
(0,1/4,1/4),\quad(0,1,1),\quad(1/4,0,0),\quad(1/4,1/2,1/2).
\]
Add spatial halfwidths \(1/8,1/2\) at \(c_1\). Repeat the small-spatial,
wide-spatial and combined cases at \(c_1\) with half the regulator.
This gives 17 cases, with no fitted coefficient. The first center was
used in scouting; centers 2 and 3 extend the check to unscouted points.
The source evaluation box including filter and finite-difference buffers
is \([-1/2,1/2]\times[24.98,31.02]\times[-1.52,1.52]\).
No artificial values are imposed at that box's edge: the source integral
supplies the full buffer and fixes the harmonic/additive data of \(U\).

## Quantities and accuracy targets

Compare the exact covariance with the moment-based gradient approximation
in [Note 04][closure]. Measure the potential-equation defect
\(|Q-Q_\nabla|/2\), and, separately, the density-equation defect
\[
E_R=\frac1{8\pi}|\Delta(Q-Q_\nabla)|.
\]
The corresponding omission baselines are \(|Q|/2\) and
\(|\Delta Q|/(8\pi)\). Report absolute defects and ratios where the
baseline is nonzero. These are consistency defects evaluated on the
source-derived mean fields, not errors of a separately evolved solution.
A closure fit to its own solutions would be a different test.

Numerical targets, fixed before the extended run: changes under source
and filter quadrature refinement below \(10^{-7}\) in the reported mean
and covariance diagnostics; differentiated consistency uncertainty below
\(\max(10^{-8},0.01 E_R)\). Check a spatial finite-difference step of
0.02 against 0.01 and Richardson extrapolation, and compare the exact
analytic \(\Delta Q\) with its finite-difference evaluation. If a target
fails, report the failure and refine or withhold that case. A useful local
closure should reduce both defects, rather than only one. A factor-of-two
improvement in each is an exploratory usefulness target, not a theorem
or a universal acceptance criterion.

The current supplies a separate differentiated check:
\(R_t+\partial_x\Re J+\partial_y\Im J=0\).
Pointwise algebraic identities alone cannot detect quadrature error;
source/order refinement and finite differences are distinct checks.

The first source quadratures use 160 versus 224 Gauss–Legendre nodes,
8 theta summands, and \(u\le2\). The filter uses 20 versus 28 nodes
per active axis. Record truncation, cancellation and floating arithmetic
as error sources; this is not interval certification or an independent
implementation. Retain only the small reproducibility record.

## Asymptotic and collision controls

For negative time, also test \(T=-t=10^8,4\cdot10^8,1.6\cdot10^9\)
at \(z=2+i/2\), spatial halfwidths \(1/2\), and the primary regulator.
Use \(u\le12/\sqrt T\) to resolve the endpoint. Compare both the
strict \(T^{-3}\) law and the leading Gaussian with its regulator
still in the denominator. These huge times are deliberate: fixed
\(\epsilon=10^{-4}\) can delay the regulator-dominated limit substantially.
They do not bridge the intermediate-time regime.

For positive time, this round extends the exact cosine slice model to
its mean potential and covariance, not to a claimed theta asymptotic.
Actual positive-time boundary data require the complete-source transfer
and complex-domain/uniformity estimates left open by [Note 01][opening].
No final boundary-value solve is authorized by these model formulas alone.

The generic identities and the small-width expansion must also hold for
the colliding heat polynomial \(H=z^2-2t\) at fixed positive regulator.
A successful check is allowed through its double event; it does not
exclude the event. Use the previous exact cosh control for the failure
of density variance alone. The repository's [collision screen][controls]
and [shape-only warning][shape] apply to any eventual global claim.
This round supplies no such claim and does not rerun old certificates.

## Deliverables and next decision

Save a derivation and the observed scale dependence in notes, executable
numerics and a small JSON record in numerics, a scoped same-assistant
assessment in reviews, and update the [sole progress ledger][progress].
The next decision is whether to advance the local expansion, the
whole-period covariance model, or both on separated scales. Boundary
matching still requires paid asymptotic data and stability estimates.

[identities]: 02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[opening]: 01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[closure]: 04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[shape]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
