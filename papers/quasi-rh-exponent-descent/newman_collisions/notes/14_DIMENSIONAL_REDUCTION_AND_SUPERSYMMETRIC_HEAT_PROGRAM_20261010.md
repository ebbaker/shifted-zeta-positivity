# Dimensional reduction and supersymmetric lifts of the Riemann heat flow

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from this chat's
recorded configuration. Parallel same-model readings are internal checks,
not independent mathematical validation.

The proposed program seeks a higher dimensional, graded, geometric, or
collective system whose distinguished observable reduces to the genuine
Riemann heat flow, and whose additional structure supplies a usable
constraint on collisions. The immediate target is a signed local theorem
for the value and derivative together, or a contradictory derivative sign
at an all-real threshold. The research directions below are proposals for
separate parallel projects. An exact lift alone is a representation result;
collision exclusion requires an additional theorem that survives reduction.

Instantiation update, 10 October 2026: the sixteen projects now live directly
in `newman_collisions/`, following the previously created first project.
[Heat Note 15](15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md)
records the fifteen new initial scouts and ranks five continuations. The
prospectus below retains its original proposed layout and stopping targets.

This program continues [Heat Note 13](13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md)
and the [stable heat manuscript](../newman_collision_reductions.tex).
It reconnects the heat investigation to the repository's earlier search for
positive bulk systems, supersymmetric boundary pairings, arithmetic
operator realizations, and dimensional interpretations. No new collision
exclusion, RH proof, or literature-priority claim is made here.

## The scalar equation and the collision observable

Use the manuscript's normalization

\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_0(z)=\tfrac18\xi(\tfrac12+iz/2),
\qquad \partial_tH_t=-\partial_z^2H_t.
\]

The positive, even theta kernel \(\Phi\) has super-exponential decay.
The minus sign is essential: increasing Newman time is backward heat in
the real coordinate. Ordinary forward heat, a shift in the zeta argument,
and the Newman deformation are different evolutions.

If RH fails, the positive threshold \(\Lambda\) entails a finite nonzero
multiple real zero at time \(\Lambda\), when all zeros are real. Excluding
all such positive threshold collisions would therefore suffice for RH.
Direct exclusion of every positive-time real collision is another,
stronger local target. The finite-threshold reduction and its imported
localization and splitting inputs are in the manuscript's first two
sections; the standard heat-flow inputs are in
[Polymath](https://arxiv.org/html/1904.12438v2).

Write \(H_t=A_tQ_t\), with the manuscript's nonvanishing symmetric analytic
normalizer. Then \(H_t=H_t'=0\) is equivalent to \(Q_t=Q_t'=0\).
In the present shrinking sector,

\[
1\le\kappa\le2,\qquad 0<t\le1/20,\qquad
L=\kappa/t,\qquad x=4\pi e^L,
\qquad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]

define the genuine observation and its finite arithmetic approximation by

\[
\mathcal W(t,x)=\left(Q_t(x)/2,\;2Q_t'(x)/L\right),
\qquad
\mathcal V_N(t,x)=\left(F_{t,N}(x)/2,\;2F_{t,N}'(x)/L\right).
\]

The exact real-axis arithmetic identity is

\[
\mathcal V_N=\sum_{n\le N}w_n
\bigl(\cos\phi_n,\;r_n\sin\phi_n-c_n\cos\phi_n\bigr),
\qquad r_n=-4\phi_n'/L,\qquad
c_n=-4(\log w_n)'/L.
\]

The phases and weights share the same physical height. The second
coordinate includes amplitude drift. Every spatial derivative fixes time
and the integer cutoff; \(L\) is the scale at the chosen center.
The complete approximation gives

\[
|Q_t-F_{t,N}|\le\eta_N\le5e^{-\mathfrak b/t},\qquad
|Q_t^{(j)}-F_{t,N}^{(j)}|\le j!L^j\eta_N,
\qquad \mathfrak b=\kappa(\kappa+4)/16.
\]

Consequently a genuine collision requires
\(|\mathcal V_N|^2\le17\eta_N^2/4\). A lifted arithmetic inequality
strictly exceeding that margin would exclude it. A theorem concerning the
genuine observation \(\mathcal W\) can instead act before approximation.

The threshold alternative uses the all-real necessary sign

\[
\mathscr L(q)=2q_3^2-3q_2q_4-\gamma q_2^2\ge0,
\qquad q_j=Q_t^{(j)}(x),\qquad
\gamma=18\partial_x^2\log A_t+9/x^2.
\]

Put \(f_j=F_{t,N}^{(j)}(x)\). One sufficient new input is
\(\mathscr L(f)<-\Delta\), with the complete
measured quadratic payment \(\Delta\) from Note 13. The full cutoff and
original value core already have vanishing payments. At exact multiplicity
three this fourth-jet expression is automatically positive; at multiplicity
at least four it is zero. A jet route must therefore cover the higher
deflation hierarchy or independently eliminate those multiplicities.

## Where the heat program stands

Heat Notes 8–12 have paid the full holomorphic approximation and derivative
errors, removed growing terminal sets by actual-phase cancellation, and
proved a positive average for the complete physical derivative. The value
core removes \(\lfloor N^{3/4}\rfloor\) terms; the derivative core removes
\(\lfloor N^{7/8}\rfloor\). These remain almost full sums, and their
different cutoffs must not be treated as a function and its derivative.
The all-real threshold now supplies the explicit signed jet test above.

The missing step is arithmetic: a constraint incompatible with both
candidate equations, or with the necessary threshold sign. A positive
average permits an isolated common zero. With
\(\mathfrak a=\kappa(4-\kappa)/16\), the known sufficient derivative
probe has length \(H_d=Dt^2e^{2\mathfrak a/t}\), whereas the current
absolute curvature estimate transfers a collision only over a scale
comparable to \(Le^{-\mathfrak a/t}\). Their exponential separation
cannot be repaired by adjusting a constant. Collective attraction estimates
provide useful positive-time tools but do not force the threshold to zero.
No actual positive-time collision exclusion or new numerical Newman bound
has been established by these local results.

The proposed enlarged systems are intended to supply this missing input.
They may also produce useful exact representations, scoped obstructions,
or positive-time bounds before a global exclusion theorem becomes available.

## What an exact reduction must specify

Let \(\Psi_t\) denote the enlarged state, \(\mathscr G\) its generator,
and \(\mathcal P\) the operation producing the scalar observable. A
time-independent linear realization would satisfy, on a stated invariant
domain or a stated class of arithmetic states,

\[
\partial_t\Psi_t=\mathscr G\Psi_t,
\qquad \mathcal P\Psi_t=H_t,
\qquad \mathcal P\mathscr G\Psi=-\partial_x^2\mathcal P\Psi.
\]

The reduction may be a fiber integral, matrix element, trace, boundary
value, selected superfield component, or elimination of internal fields.
These are different maps and require different hypotheses. A Berezin
integral or supertrace has no automatic interpretation as a positive
ordinary average.

If \(\mathcal P_t\) changes with time, the required identity becomes

\[
(\partial_t\mathcal P_t)\Psi_t+
\mathcal P_t\mathscr G_t\Psi_t
=-\partial_x^2(\mathcal P_t\Psi_t).
\]

State-dependent reduction, forcing, coordinate transport, boundary flux,
and memory introduce further terms. They must be derived, not suppressed.
If the projection depends on the spatial coordinate, its derivative also contributes: \(\partial_x(\mathcal P\Psi)=(\partial_x\mathcal P)\Psi+\mathcal P\partial_x\Psi\). With \(b=\partial_x\log A_t\), the observation changes by the exact triangular relation \((Q_t,Q_t')=A_t^{-1}(H_t,H_t'-bH_t)\); higher jets retain every product derivative.

The arithmetic initial state and all normalization factors must match
\(H_0\), not only the gamma factor, a toy spectrum, or a freely chosen
function satisfying the same PDE. Matching both value and derivative at
one point requires much less than reproducing the full evolution.

For a positive Hilbert Hamiltonian \(\mathscr K\ge0\), the contractive
evolution is \(\partial_t\Psi=-\mathscr K\Psi\). The desired scalar
generator \(-\partial_x^2\) has positive Fourier eigenvalues, so an exact
bounded intertwining with this contraction cannot hold on arbitrary scalar
Fourier modes in ordinary \(L^2\). Restricted analytic states, unbounded
observations, continuation, or a different time orientation can change the
framework; each requires its own domain and growth estimates.

A fixed orthogonal projection onto a subspace that is exactly invariant
under a selfadjoint generator is reducing when the orthogonal projection
preserves its domain and commutes with it there, or when a compatible
resolvent or spectral intertwining is proved. Formal invariance on an
unspecified core is insufficient. In that architecture the complementary
dimensions decouple.
Useful additional restrictions must then enter through the selected
arithmetic state, its preparation, the observable, or a different coupling
architecture. This observation does not exclude nonorthogonal, moving,
nonlocal, constrained, or nonlinear reductions.

## Established lifts and calibration examples

For \(t>0\), the exact Gaussian formula is

\[
H_t(x)=\frac1{\sqrt{4\pi t}}
\int_{\mathbb R}e^{-y^2/(4t)}H_0(x+iy)\,dy.
\]

The super-exponential theta decay justifies the interchange: Gaussian
averaging of \(\cos((x+iy)u)\) yields \(e^{tu^2}\cos(xu)\).
This is the rescaled identity in
[Polymath Section 4](https://arxiv.org/html/1904.12438v2#S4).
For \(U(t,x,y)=H_t(x+iy)\), holomorphicity gives
\(U_y=iU_x\), hence \(U_t=U_{yy}=-U_{xx}\).
This is forward transverse diffusion on a constrained analytic field.
Restriction to \(y=0\) recovers the desired scalar function. It is not
isotropic two-dimensional diffusion, and its analytic modes need not be
square integrable in the transverse coordinate.

A second calibration is a product lift. On the transverse line put

\[
B=\partial_y+y,\qquad
g(y)=\pi^{-1/4}e^{-y^2/2},\qquad Bg=0,
\qquad \mathscr K=-\partial_x^2+B^\dagger B.
\]

For \(\mathcal P U=\int g(y)U(x,y)\,dy\), integration by parts gives
\(\mathcal P\mathscr K=-\partial_x^2\mathcal P\) on a suitable domain.
The field \(U=H_tg\) satisfies \(U_t=\mathscr K U\), retaining every
scalar collision. The conventional contraction \(U_t=-\mathscr K U\)
would instead reduce to forward heat. This product model isolates why a
positive transverse supersymmetric factor alone supplies no exclusion.

Every project should also compare its proposed implication with three
controls from the heat manuscript: the even quartic with an arbitrary
positive threshold, the genuine adjacent packet whose cross term cancels
almost all diagonal energy, and the complete multiplicative-twist joint
zero. Their scopes differ. The quartic is not the theta heat function;
twisted phases are not a genuine height orbit. A proposed arithmetic
selection rule may distinguish them, but must say how.

## The additional theorem sought in the enlarged system

The joint observation map is

\[
\mathcal C_{t,x}\Psi=
\left(\frac{\mathcal P\Psi}{2A_t},\;
\frac2L\partial_x\left(\frac{\mathcal P\Psi}{A_t}\right)\right).
\]

Positive bulk energy or norm does not imply that this pair is nonzero.
For a probability average, Jensen gives
\(|\mathbb E Z|^2\le\mathbb E|Z|^2\), which is in the wrong direction
for the desired lower bound. A map with two scalar observations also has
a large kernel on an unrestricted infinite-dimensional linear state space.
Any useful visibility theorem must concern a genuinely restricted
arithmetic family, additional observations with a proved transfer, or a
specific dynamical identity.

Three forms of new input would be useful. First, a quantitative
observability estimate could separate the actual arithmetic state from
the joint observation kernel by more than the approximation payment.
Second, a Ward, energy, or geometric identity conditional on both collision
equations could force the opposite threshold-jet sign. Third, a regular
closed first-order equation for the reduced pair could forbid simultaneous
vanishing by uniqueness. Such closure must be derived independently;
defining coefficients by dividing by \(H_t\) at its unknown zeros would
presuppose the desired conclusion. A global index, spectral nonnegativity,
or a formally positive factorization is not itself one of these inputs.

The earlier [superspace continuation](../../../susy-positivity/brainstorm/continuation-notes/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md)
specifies positive component energies, physical adjoints, boundary traces,
and exact arithmetic matching. The
[topological SUSY construction](../../../susy-positivity/investigations/previous/topological-susy-bulk/README.md)
produced a positive Hamiltonian and a protected gamma pairing, while an
arithmetic residual remained. The
[CCM ground-selection investigation](../../../investigations/ccm-operator-realizations/notes/CCM_GROUND_SELECTION_TARGET_20260928.md)
separates an extremely small arithmetic residual from actual bottom-space
overlap. These precedents motivate keeping exact reproduction, independent
structure, and visibility under reduction as separate obligations.

## Parallel research directions

Each direction below has a stable proposed folder name. The suggested
parent is `newman_collisions/dimensional_reduction/`. The names identify
projects to instantiate in the next research chat; no project result is
asserted merely by assigning a folder. Each project should retain its own
`README.md`, numbered `notes/`, `numerics/`, and `reviews/`, while common
notation and the cross-project comparison remain in this note.

### Gaussian analytic lift as the control experiment

Proposed folder: `01_analytic_gaussian`.

**Established architecture.** For \(t>0\), the exact imaginary Gaussian convolution is
\[
H_t(z)=\frac1{\sqrt{4\pi t}}\int_{\mathbb R}
e^{-y^2/(4t)}H_0(z+iy)\,dy.
\]
This is the fundamental-solution representation used in [Polymath, Section 4](https://arxiv.org/html/1904.12438v2#S4). It already provides a higher dimensional analytic representation; its existence is not a new theorem of this proposed project.

There are two interfaces to distinguish. One keeps the field \(H_0(x+iy)\) fixed and uses the moving Gaussian projection \(P_t\). The other evolves \(U(t,x,y)=H_t(x+iy)\) and takes the trace \(U(t,x,0)\). Holomorphicity gives
\[
U_y=iU_x,\qquad U_t=U_{yy}=-U_{xx}.
\]
The trace is not automatically a bounded observation on an ordinary transverse \(L^2\) space.

**Sign and domain issue.** Forward diffusion in \(y\) reproduces backward diffusion in \(x\) because of the analytic constraint. The mode \(e^{ikx-ky}\) illustrates the point: it is not square integrable on the whole \(y\)-axis and is amplified by the transverse heat operator. The positive Gaussian integrates complex, potentially cancelling quantities. Jensen supplies an upper bound for projected energy by bulk energy, not the lower bound needed for collision exclusion.

**Proposed extra property.** Seek an actual-theta, candidate-conditioned identity for the two Gaussian integrals representing \(H_t\) and \(H_t'\). A useful outcome would be a correlation or angle restriction preventing their simultaneous cancellation, or a relation among Gaussian projections of higher jets that contradicts the threshold condition. An arbitrary holomorphic function cannot satisfy such a universal restriction.

**Bounded first task.** On one closed parameter rectangle inside the present shrinking-time sector, derive the joint observation kernel and exact moving-projection identity. Pay the Gaussian tails, any contour movements, the normalizer, and the existing fixed-cutoff analytic errors. Use the manuscript's quartic and positive-kernel models as scope checks, not as genuine arithmetic counterexamples.

**Stopping criterion.** End the initial project with either one new signed conditional inequality for the actual theta state, or a precise proof that the proposed Gaussian norm or positivity argument controls only bulk/averaged energy and cannot bound the point observation from below. Re-deriving the convolution or reducing a constant in its remainder is a baseline result, not the new arithmetic input.

### Bargmann Fock and coherent state observation geometry

Proposed folder: `02_bargmann_fock`.

**Concrete architecture.** Place the entire function \(H_t(z)\) in a Gaussian weighted holomorphic space with a fixed width parameter. Its order-one growth makes this natural after proving the required growth bound and norm convergence. In the conventional Fock space
\[
\|f\|_a^2=(\pi a)^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2/a}\,d^2z,
\]
the reproducing kernel is \(K_a(z,w)=e^{z\bar w/a}\). Value and first derivative are two coherent-state observations. This framework originates in [Bargmann's 1961 paper](https://doi.org/10.1002/cpa.3160140303); applying it to the present arithmetic family and obtaining an exclusion estimate would be new work.

A second architecture applies the unitary Bargmann transform to the real-axis function \(H_t|_{\mathbb R}\). That transformed function is not simply \(H_t(z)\). In standard units,
\[
B\partial_xB^{-1}=(\partial_z-z)/\sqrt2,\qquad
B(-\partial_x^2)B^{-1}=-\tfrac12(\partial_z-z)^2.
\]
The inverse transform and its differentiated observation must recover the original collision vector. These two architectures must not be conflated.

**Sign and domain issue.** For direct holomorphic embedding, \(-\partial_z^2\) is not the positive number operator. For the unitary transform, positivity of the transformed momentum-square operator is preserved but the evolution remains its anti-contraction \(e^{+tK}\). Changing the Gaussian width with time introduces an additional moving-space or moving-projection term.

The positive Gram matrix of the two evaluation kernels proves their independence. It does not prove that a nonzero arithmetic state has nonzero overlap with them. Indeed \((z-x)^2\) belongs to the Fock space and has a zero value/derivative pair; within the even subspace, \((z^2-x^2)^2\) gives the same obstruction.

**Proposed extra property.** Identify a quantitative angle between the genuine theta/Hermite coefficient vector and the codimension-two observation kernel. An arithmetic cone, a rigidity relation among coefficients, or a conditional estimate using both candidate coordinates could be useful. Generic reproducing-kernel bounds have the wrong direction.

**Bounded first task.** Fix one width \(a\), print the exact evaluation/derivative Gram matrix and observation kernel, and express the actual theta state in this representation with a proved truncation payment. Test one specific arithmetic coefficient restriction against the common-height condition. If using the unitary transform, prove the real-axis function and derivative lie in the relevant operator and observation domains before taking norms.

**Stopping criterion.** Success is a paid angle/coercivity estimate on a stated arithmetic class, or a threshold-jet relation derived from it. Stop a proposed universal Fock-positivity route once it admits states orthogonal to both observations. Merely making the Hermite expansion convergent or the Gram determinant positive does not resolve the collision question.

### Supersymmetric quantum mechanics and Dirac boundary data

Proposed folder: `03_susy_dirac_hodge`.

**Concrete architecture.** Start in the spectral variable \(u\), where the genuine positive even theta kernel is explicit. Normalize
\[
\rho_t(u)=\frac{e^{tu^2}\Phi(u)}{\int_{\mathbb R}e^{tv^2}\Phi(v)\,dv},
\qquad W_t=-\log\rho_t,
\]
and set
\[
B_t=\partial_u+\tfrac12W_t',\quad
K_t=B_t^\dagger B_t,\quad
D_t=\begin{pmatrix}0&B_t^\dagger\\ B_t&0\end{pmatrix}.
\]
The ground state is \(\sqrt{\rho_t}\), and the characteristic function
\[
C_t(x)=\langle\sqrt{\rho_t},e^{ixu}\sqrt{\rho_t}\rangle
      =H_t(x)/H_t(0)
\]
has the same spatial collision conditions. This is an explicit ground-state factorization, in the general tradition of [Witten's supersymmetric quantum mechanics](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf). Its existence for a positive density is not evidence of new arithmetic rigidity.

The heat generator in this spectral representation is multiplication by \(u^2\). It is not \(K_t\). Also \(C_t\) obeys
\[
\partial_tC_t=-C_t''-\mu_2(t)C_t,\qquad
\mu_2(t)=\int u^2\rho_t(u)\,du,
\]
because the normalization moves. Any proposed Dirac/Hodge boundary model must account for these differences.

**Sign and domain issue.** A positive supersymmetric Hamiltonian controls a global quadratic form. Its zero-free ground-state density does not make its oscillatory characteristic function zero-free. Fermionic partner relations must be observed through the same genuine projection. A first-order Dirac equation in a larger space does not prohibit a simultaneous zero of only two projected components.

A regular, closed first-order spatial system for the actual projected pair would be much stronger:
\[
\partial_x(H_t,H_t')^\top=M_t(x)(H_t,H_t')^\top.
\]
Uniqueness would exclude a common zero of a nontrivial solution. Obtaining such closure with regular coefficients is a substantive new property; defining a potential by dividing by \(H_t\) merely puts the unknown zeros into singular coefficients.

**Proposed extra property.** Seek an arithmetic partner identity, boundary Wronskian, or finite closure of the Ward hierarchy that yields local observation coercivity. The elementary integration-by-parts identity is
\[
\mathbb E_{\rho_t}[W_t'e^{ixu}]=ixC_t(x).
\]
At a collision, additional inserted identities impose further vanishing weighted moments. For a Gaussian density, the linearity of \(W_t'\) gives a closed first-order equation. For the actual theta density \(W_t'\) is not linear; closing its hierarchy without circular assumptions is the research problem.

**Bounded first task.** Construct the spectral Dirac factorization and its domains on one time interval, derive the first three Ward identities, and express their observed quantities in the manuscript's normalized jets. Determine whether theta modularity supplies a genuine closure or a signed residual estimate. Print the moving normalization and every boundary term.

**Stopping criterion.** Success is a new, paid partner/Ward constraint at actual candidates. Stop if the construction yields only the standard integration-by-parts identities available for every smooth positive kernel, or if the partner observation is independent of the collision derivative and its relation has no lower-bound content.

### Cohomological localization and protected Ward identities

Proposed folder: `04_cohomological_localization`.

**Concrete architecture.** Try first a finite dimensional superspace integral whose bosonic reduction gives the genuine theta integral or a fixed-cutoff actual-phase sum. Specify a nilpotent or equivariant supercharge \(\mathcal Q\), its measure, contour, and a deformation
\[
S_\lambda=S_0+\lambda\mathcal QV.
\]
A localization claim must identify the exact observation and show why its expectation is invariant under this deformation. [Witten's two dimensional gauge-theory paper](https://arxiv.org/abs/hep-th/9204083) provides an example of a rigorously motivated mapping/localization mechanism in a different model; it supplies no zeta reduction.

**Sign and domain issue.** The observation \(\cos(xu)\) is generally not \(\mathcal Q\)-closed when \(\mathcal Q u\) is a fermion:
\[
\mathcal Q\cos(xu)=-x\sin(xu)\,\mathcal Q u.
\]
Thus independence of the partition function under a supersymmetric deformation does not imply independence of the heat observable. A fermionic completion may be possible, but its extra terms must be retained in the reduced scalar quantity. A localized saddle sum may have complex phases, determinant signs, boundary contributions, or noncompact saddle directions.

A BPS ground state or global supersymmetric index does not prevent a signed matrix element from vanishing. The relevant question is whether the actual collision observations belong to a protected class with an additional quantitative relation.

**Proposed extra property.** Find a \(\mathcal Q\)-closed completion of the joint observations or a threshold-jet combination whose Ward identity is both compatible with exact reduction and sign-informative on actual candidates. Localization might organize correlated arithmetic contributions into a useful finite signed formula; it need not make them individually positive.

**Bounded first task.** Work with a finite dimensional model and one finite arithmetic block. Print the full superspace action, the completed observation, the localized terms, and all orientation/Jacobian factors. Differentiate the exact reduced expectation in \(x\) at fixed cutoff and show agreement through fourth order. Check whether the proposed Ward relation genuinely uses theta coefficients/shared phases rather than a generic identity for any input function.

**Stopping criterion.** Success is one protected identity with a paid collision-vector or threshold-jet consequence. Stop if the observation fails to be closed, if localization changes the desired scalar quantity, or if the localized expression retains the original cancellation problem without a new constraint. Calling the same integral a partition function is not progress by itself.

### Interacting supersymmetric and gauge collective fields

Proposed folder: `05_interacting_susy_gauge`.

**Concrete architecture.** Aim beyond a free auxiliary lift: introduce collective variables for prime exponent data, theta modes, or a macroscopic arithmetic block, together with bosonic/fermionic partners. Fixed background holonomies would encode the genuine orbit
\[
U_p(t,x)=e^{i(x-t\alpha_i(t,x))\log p/2},\qquad
U_n(t,x)=\prod_pU_p(t,x)^{a_p(n)}.
\]
The heat weight involves \(\log^2n=(\sum_pa_p(n)\log p)^2\), so its prime data are naturally correlated. A common Gaussian auxiliary variable can represent the quadratic heat weight exactly at finite cutoff. More ambitious interactions would have to encode theta modularity or another actual arithmetic relation.

Independent integration of prime holonomies is not exact reduction: it replaces the common-height orbit by an averaged or twisted family and can erase the correlations that matter. Gauge-invariant composite observables and background-source derivatives must be specified, including amplitude drift and the carrier phase.

Nicolai maps suggest another possible architecture: transform an interacting supersymmetric measure into a Gaussian one while transforming the observations by the inverse map. [Lechtenfeld and Rupprecht's construction](https://arxiv.org/abs/2104.00012) establishes such a mechanism for its specified supersymmetric theories. A map from the genuine theta arithmetic to one of those theories is not supplied by these sources or the present manuscript; constructing one would be an additional task.

**Sign and domain issue.** Even an exact Gaussianization moves the hard information into a transformed oscillatory observable. A one-dimensional cumulative-distribution map already Gaussianizes any smooth positive density; that generic fact cannot distinguish zeta. Fermionic determinants need not be nonnegative, and formal continuum or large-system limits need their own control. Claims of supersymmetric dimensional reduction require symmetry, observable, state, and limit hypotheses; [Parisi–Sourlas](https://doi.org/10.1103/PhysRevLett.43.744) concerns a specific random-field mechanism, not arbitrary heat families, and [subsequent work](https://arxiv.org/abs/1912.01617) separates the reduction implication from the existence of the required supersymmetric fixed point.

One concrete superspace scout is a field theory with three bosonic
coordinates and two Grassmann coordinates, aiming for a one-dimensional
restricted correlation function through Parisi–Sourlas symmetry. This would
require an explicit action, invariant state, and protected correlation whose
reduced value is the genuine \(H_t\), with the Newman parameter realized
in its generator or sources. Establishing reduction for a different
observable would not identify the theta state. This is a proposed dictionary
to construct, not an available application of the cited theorem.

**Proposed extra property.** Seek an interaction or gauge Ward identity linking a macroscopic block to its complement while preserving the actual shared orbit. The desired output could be a conditional signed contribution to the full joint vector, or a constraint relating second-through-fourth jets. A model that admits every completely multiplicative unit-modulus twist cannot supply a universal positive joint bound, in view of the manuscript's relaxation obstruction.

**Bounded first task.** Choose a small composite-complete index set or one fixed relative block. Construct a finite dimensional measure/observable dictionary reproducing its exact weights, phases, and raw spatial derivatives. Show what one nontrivial interaction adds beyond an identity valid for arbitrary phases. If using a Nicolai map, derive the inverse-transformed joint observation before discussing positivity.

**Stopping criterion.** Success is one actual-orbit correlation or Ward identity with a measured remainder when recombined with the full core. Stop if the model simply re-encodes the input coefficients, integrates away the common-height dependence, transfers all cancellation to the inverse observable, or requires an uncontrolled continuum/large-system limit.

### Theta lattices and compact boson reductions

Proposed folder: `06_theta_lattice`.

**Enlarged system.** Begin with the circle rotor on `ell^2(Z)`, with momentum `P e_n = n e_n`, before adding a compact boson, a second lattice direction, or momentum/winding channels. Its heat trace is the exact rank-one theta series

\[
\vartheta(v)=\operatorname{Tr}e^{-\pi vP^2}=\sum_{n\in\mathbb Z}e^{-\pi vn^2}.
\]

For `v = exp(4u)`, direct differentiation gives the genuine theta kernel

\[
\Phi(u)=v^{1/4}\left(v^2\vartheta''(v)+\frac32v\vartheta'(v)\right)
=\operatorname{Tr}\left[v^{1/4}\left(\pi^2v^2P^4-\frac32\pi vP^2\right)e^{-\pi vP^2}\right].
\]

This is a useful exact starting identity derived from the manuscript's kernel, not a new positivity theorem. Integrating this trace against `exp(t u^2) cos(xu)` reproduces `H_t`; inserting `-u sin(xu)` reproduces its derivative.

**Reduction and sign issue.** The enlarged partition function must reduce to this precise inserted trace, including the zero mode, factors of two, scale, and theta reflection. A full compact-boson partition function has more sectors and normalization data than the rank-one trace. A projection, division by an oscillator factor, or restriction of winding sectors needs an explicit map and theorem. The Newman parameter multiplies the squared logarithmic coordinate, not the rotor Hamiltonian itself; it is not ordinary rotor thermal time. Even a positive kernel does not prevent destructive interference in the final cosine readout.

**Potential additional arithmetic constraint.** Test whether lattice duality or a Ward identity relates the signed logarithmic moments appearing in the collision jets, with more content than the already-known theta functional equation. The desired relation would constrain the full common-height observation, not independently chosen phases.

**Bounded first task.** Derive the rotor trace identity and its first four spatial readouts with domains and endpoint terms. Then specify one compact-boson completion and compute its exact reduction: identify every sector or normalization correction. Seek one candidate-conditioned identity that could enter the paid fourth-jet test. The first deliverable can be an exact mismatch rather than a sign theorem.

**Method-specific stopping result.** The completion changes a theta coefficient, leaves an unaccounted oscillator/winding contribution, breaks odd-endpoint-jet cancellation, or yields only an inequality also satisfied by the manuscript's positive-kernel counterexample. Such a result excludes that proposed completion, not all lattice lifts.

**Precedents.** The current manuscript's exact theta interface and fixed-cutoff obstruction are essential controls. The earlier fractional-dimension investigation also shows that analytic continuation of theta coefficients can lose their positive counting interpretation. For a modest external benchmark, compact-boson correlators can produce lattice theta sums; this does not identify them with the Riemann kernel: [Datta–David, sections 2.2–2.4](https://arxiv.org/html/1311.1218).

### Automorphic and hyperbolic scattering

Proposed folder: `07_automorphic_scattering`.

**Enlarged system.** Use scalar and exact one-form channels on the modular surface, its cusp radiation space, and the Hodge/Dirac complex. The repository already has a geometric fixed-half-shift benchmark. A new heat branch should start with its actual Eisenstein waves and a precisely specified coefficient extraction, then investigate a heat deformation of that extraction.

**Reduction and sign issue.** A scattering ratio is not `H_t`. One must show how an incoming/outgoing coefficient, a completed determinant, or a boundary pairing produces `H_0 = xi/8` in the stated spectral coordinate and then intertwines with the genuine heat flow. With `s = 1/2 + iz/2`, the corresponding entire scalar deformation obeys

\[
\partial_t\Xi_t(s)=\frac14\partial_s^2\Xi_t(s),\qquad\Xi_0(s)=\xi(s).
\]

Here \(\Xi_t(s)=8H_t(-2i(s-1/2))\). The completion polynomial, cusp normalization, and all boundary terms have to be retained. Positivity of the Laplacian and real-frequency flux conservation alone do not show that the extracted amplitude and its derivative cannot vanish together.

**Potential additional arithmetic constraint.** A Maass–Selberg or Hodge boundary identity might relate a putative common zero to a positive bulk norm or flux. The useful statement would be a quantitative nonvanishing/observability estimate for the precise extracted state, including any cusp states lost by the extraction.

**Bounded first task.** Choose one completed Eisenstein coefficient and prove the exact `t = 0` extraction and its first heat-time derivative. Compute the commutator between extraction and the proposed bulk evolution. Pay the first and fourth spatial derivatives before attempting a collision consequence. Determine whether one positive boundary identity survives this operation.

**Method-specific stopping result.** The evolution changes cusp height or boundary load rather than implementing the arithmetic heat derivative; polynomial completion leaves unmatched terms; or the positive norm controls only a channel orthogonal to the coefficient being read. The existing real cusp-load model already fails to realize arithmetic shift evolution and should be used as a calibration control.

**Precedents.** [the modular Hodge and cusp coupling test](../../../susy-positivity/investigations/wilson-loewner/WZW/notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) gives the fixed-shift benchmark and its scoped coupling obstruction. The primary [Lagarias–Suzuki paper, equations (10)–(11)](https://arxiv.org/html/math/0412039) gives the completed Eisenstein constant term. Its results concern its specified integrals, not the genuine Riemann heat flow.

### Adelic and prime local models with a common heat coordinate

Proposed folder: `08_adelic_local_models`.

**Enlarged system.** Combine the real Gaussian/theta channel with prime-local valuation spaces, using a common dilation or auxiliary Gaussian coordinate. The purpose of an adelic description would be to enforce global compatibility of local arithmetic data, rather than permit arbitrary unrelated prime phases.

**Reduction and sign issue.** Independent local heat weights already miss an exact correlation. In the finite approximant,

\[
b_n^t=e^{t\log^2n/4},\quad
b_{p^kq^\ell}^t=b_{p^k}^tb_{q^\ell}^t
e^{(t/2)k\ell\log p\log q}.
\]

Thus a product of independently heat-deformed local channels is not the genuine composite coefficient. A shared auxiliary real variable can reproduce this particular weight exactly on a finite sum:

\[
e^{t\log^2n/4}
=\frac1{\sqrt{\pi t}}\int_{\mathbb R}e^{-\lambda^2/t}n^\lambda\,d\lambda
\qquad(t>0).
\]

This elementary identity retains the mixed heat term. It does not justify interchanging this integral with an unrestricted Euler product: the positive heat weight grows too fast for the corresponding infinite Dirichlet series. The finite cutoff and shared amplitude drift still require explicit treatment.

**Potential additional arithmetic constraint.** Investigate a global state or quotient that couples the local characters, enforces the genuine common-height orbit, and retains the reflected carrier and normalizer. Such compatibility would need to rule out the freedom exploited by the manuscript's complete multiplicative-twist zero construction. Mere complete multiplicativity cannot supply the desired joint lower bound.

**Bounded first task.** Work with the complete cutoff `N = 6`, retaining `1, 2, 3, 4, 5, 6`. Derive the shared-variable representation of both reflected sums and their raw first through fourth derivatives. Compare the exact composite `6` coefficient with independent-prime and shared-coordinate controls. State the global compatibility condition that the proposed local system actually enforces; do not add it as an unexplained restriction after a bad sign is found.

**Method-specific stopping result.** The model omits the mixed heat factor, obtains its desired sign only after discarding composites, admits the existing arbitrary multiplicative twists, or needs an unjustified infinite-product/interchange argument. A mismatch at `6` decides the independent-channel ansatz quickly; it says nothing against a genuinely coupled adelic construction.

**Precedents.** The Newman-collision multiplicative-twist obstruction and exact drift-containing vector are the principal local controls. The primary [Tate thesis, local theory sections 2.3–2.5 and global theory chapters 3–4](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf) supplies the local/global harmonic-analysis architecture. That architecture proves functional-equation and factorization statements, not the missing heat-collision sign.

### Prime phase torus and coherent arithmetic channels

Proposed folder: `09_prime_phase_torus`.

**Exact starting point and projection.** For a fixed cutoff, write
\(n=\prod_{p\le N}p^{\nu_p(n)}\),
\(T=(x-t\alpha_i)/2\), and \(Z_p=e^{iT\log p}\). Then the manuscript's
complex sum is exactly

\[
S_N=e^{i\theta_t}\sum_{n\le N}w_n
       \prod_{p\le N}Z_p^{\nu_p(n)}.
\]

This is a finite Bohr lift: a polynomial in prime-indexed torus coordinates.
Define \(z_n=r_n-ic_n\) and
\(S_{N,z}=e^{i\theta_t}\sum_{n\le N}w_nz_n\prod_{p\le N}Z_p^{\nu_p(n)}\).
The second coherent channel has the same monomials with coefficients
\(w_nz_n\). The projected collision vector is exactly
\(\mathcal V_N=(\Re S_N,\Im S_{N,z})\). Prime factorization gives the monomial identity;
it does not make the heat weights multiplicative. The established Bohr
viewpoint and identification of torus points with unit-modulus multiplicative
characters are described by Bailleul and Lefevre in
[Some Banach spaces of Dirichlet series, introduction](https://www.impan.pl/shop/en/publication/transaction/download/product/90280).

**Bulk dynamics and the heat sign.** The genuine height trajectory is
nonautonomous: \(Z_p'=iT'\log p\,Z_p\), while \(w_n\), the carrier,
normalizer, drift, and cutoff also change. On a local neighborhood keep its
integer cutoff fixed and put \(q_n=w_ne^{i\phi_n}\),
\(v_n=(\log w_n)'+i\phi_n'\). The exact raw multipliers satisfy
\(q_n'=v_nq_n\), including amplitude differentiation. The finite approximant
does not itself satisfy an exact homogeneous heat equation; the projection to
the genuine heat function must retain the manuscript's paid approximation.
An exact infinite lift would have to be constructed separately.

**Potential new constraint, still speculative.** Seek restrictions on
simultaneous cancellation of the two channels and their higher jets along the
actual coupled height/time trajectory, using temporal correlations and the
heat coefficient relations. This uses arithmetic information absent from
an unrestricted torus bound, while applying to a narrower family of states. The manuscript already constructs a complete-vector zero for a
completely multiplicative unit twist at the same coefficient data, so
multiplicativity and composite retention alone cannot be the new input.

**Bounded first task.** Choose one closed \(\kappa\)-interval and one genuine
relative block. Print the torus trajectory, coefficient dynamics, and raw jet
maps through order four on a fixed cutoff. Test one candidate-conditioned
correlation identity on that trajectory and measure its contribution after
recombining with the remaining core. Require a strict useful margin after all
analytic and truncation payments.

**Failure criterion.** The proposed inequality depends only on multiplicative
torus coordinates and therefore also holds for the known cancelling twists;
or physical coefficient movement destroys its sign or exceeds its margin.
Density or approximation of finitely many prime phases with frozen
coefficients does not transfer to a genuine collision at another height.

### Kinetic and stochastic transport with hidden variables

Proposed folder: `10_kinetic_stochastic`.

**Exact starting point and projection.** Let \(\Phi_e\) be the even extension
of the manuscript kernel and retain the spectral variable \(u\) as a hidden
state:

\[
\rho_t(u)=e^{tu^2}\Phi_e(u),\qquad
\partial_t\rho_t=u^2\rho_t,\qquad
H_t(z)=\tfrac12\int_{\mathbb R}e^{izu}\rho_t(u)\,du.
\]

This exact positive bulk evolution is a multiplication or growth equation,
not conservative Markov transport. Its projected jet hierarchy satisfies
\(\partial_tH_t^{(j)}=-H_t^{(j+2)}\). There is also an exact Gaussian
identity, directly obtained from \(\mathbb E e^{aG}=e^{a^2/2}\), with
\(G\sim N(0,1)\):

\[
H_t(z)=\mathbb E\,H_0(z-i\sqrt{2t}\,G),\qquad t\ge0.
\]

The shifts are imaginary. Ordinary real Brownian smoothing would produce
the opposite heat sign. Superexponential theta decay justifies the integral
identity on compact sets.

**Memory formulation.** On a bounded spectral cutoff, the generator
\((Lf)(u)=u^2f(u)\) is bounded. A fixed bounded linear projection splits its bulk
state into resolved variables \(a\) and hidden variables \(b\). With blocks
\(A,B,C,D\), eliminating the latter gives the exact identity

\[
a'(t)=Aa(t)+Be^{tD}b(0)
        +\int_0^tBe^{(t-s)D}Ca(s)\,ds.
\]

This is a concrete linear memory equation. General projection methods retain
memory and an unresolved forcing term; see Darve, Solomon and Kia,
[Computing Generalized Langevin Equations and Generalized Fokker-Planck Equations](https://mc.stanford.edu/cgi-bin/images/c/c1/Darve_pnas_2009.pdf).
Their application is not a theorem about the theta kernel. No damping sign,
white-noise replacement, invariant probability measure, or finite closure is
assumed here.

**Potential new constraint, still speculative.** A theta-specific bound on
the hidden forcing and memory might constrain nearby derivative growth when
the value and first derivative vanish. It would need to yield either a paid
mean square below \(1/8\) on the current derivative-probe interval, or a signed
relation among the collision jets. Memory that merely rewrites the unbounded
jet hierarchy adds no such information.

**Bounded first task.** At one fixed candidate height, resolve the cosine and
sine observables giving jets zero through four, derive the exact projected
blocks on \(|u|\le U\), and pay the theta tail. Evaluate whether the hidden
forcing has a sign or conditional cancellation absent for an arbitrary
positive kernel. Benchmark the proposed implication against the manuscript's
positive-kernel counterexample.

**Failure criterion.** The forcing remains uncontrolled; its paid norm is on
the existing absolute scale; or the argument closes the hierarchy by dropping
memory, noise, or analytic-continuation terms. A positive transport measure
alone cannot exclude a zero of its oscillatory transform.

### Boundary extensions and inverse spectral realizations

Proposed folder: `11_boundary_extensions`.

**Enlarged system.** Start with an independently specified positive elliptic bulk, string, quantum graph, or graded boundary complex. Retain at least two readout channels so value and derivative can be observed jointly. The model can use an existing gamma extension as a benchmark, but the full arithmetic response must be derived rather than reconstructed after assuming the desired positivity.

**Reduction and sign issue.** Specify whether `H_t` is a characteristic determinant, a numerator of a response, or a paired boundary amplitude. Those objects have different positivity implications. A boundary resolvent can have a positive spectral measure while a chosen source is orthogonal to some modes. Identifying the output exactly with `H_t,H_t'` would therefore still require a uniqueness or observability statement ensuring that their common vanishing cannot hide a nonzero lifted state. Shifting a Hamiltonian to make it positive must not erase the sign or alter the heat target.

**Potential additional arithmetic constraint.** A Green identity or unique-continuation theorem might convert simultaneous vanishing of precisely identified boundary value/flux data into vanishing of the whole state. A Schur complement could alternatively retain collective arithmetic correlations. The challenge is to establish that these are the genuine two collision observations, not two more convenient boundary coordinates.

**Bounded first task.** Choose one independently defined two-channel model and derive its full transfer matrix, response, domains, and energy identity. Audit the analytic class of the proposed scalar response before inverse realization. On one compact positive-time rectangle, compare its normalized value and first four jets with the actual finite approximant, retaining the complex-neighborhood error. Prove or disprove quantitative visibility of every candidate mode there.

**Method-specific stopping result.** An unmatched pole, contact, delay coefficient, or nonlocal residual survives; the observation kernel contains a candidate mode; or regulator removal makes a previously visible mode dark. A small mismatch in finitely many jets is diagnostic; agreement in finitely many jets is not an exact global identity.

**Precedents.** The supersymmetric relative-boundary model preserved a genuine positive gamma pairing but retained an infinite-rank arithmetic residual. The CCM string controls show that a cyclic port at every finite stage can lose a spectral factor in its limit. The primary [Kwaśnicki–Mucha extension theorem](https://arxiv.org/abs/1707.02475) realizes complete Bernstein functions of a Laplacian as weighted Dirichlet-to-Neumann maps; it does not assert that an arbitrary zeta response belongs to that class.

### Radial Bessel and fractional dimension geometry

Proposed folder: `12_radial_bessel`.

**Enlarged system.** Seek a radial density or a weighted radial differential system whose axis marginal is the genuine even theta kernel. Integer-dimensional examples should come before formal continuation in dimension. At dimension three, an even marginal `m(u)` of radial density `R(r)` has the elementary relation

\[
m(u)=2\pi\int_{|u|}^{\infty}R(r)r\,dr,
\qquad R(r)=-\frac{m'(r)}{2\pi r}.
\]

This gives a concrete sign and endpoint test for choosing `m = Phi`, without inventing a fractional lattice. Bessel kernels describe angular Fourier averaging; the relevant Poisson integral and its parameter range are recorded in [DLMF 10.9.4](https://dlmf.nist.gov/10.9.E4).

**Reduction and sign issue.** Distinguish a fiber marginal in the spectral
variable from an axis trace in observation space. For a sufficiently decaying
spectral density evolving by the ordinary \(d\)-dimensional Laplacian,
transverse flux integrates to zero and its marginal obeys
\(\partial_tm=\partial_u^2m\). Its Fourier observable then evolves by
\(\partial_tH=-x^2H\), rather than \(\partial_tH=-H_{xx}\).
By contrast, an axis trace of a radial observation-space Laplacian retains
the drift \((d-1)r^{-1}\partial_r\). Weighting an enlarged spectral density
by \(e^{tu_1^2}\) reproduces the desired multiplier exactly, but breaks
full rotational symmetry. The useful symmetry and exact heat intertwining
must therefore be checked together.

There is also an exact radial calibration with a nonlocal correction. Put
\(m_t(r)=e^{tr^2}\Phi_e(r)\) and
\(R_t(r)=-m_t'(r)/(2\pi r)\). For \(r>0\), direct differentiation gives

\[
\partial_tR_t(r)=r^2R_t(r)-2\int_r^\infty R_t(s)s\,ds,
\qquad R_t=e^{tr^2}\bigl(R_0-t\Phi_e/\pi\bigr).
\]

Its marginal and Fourier observation reproduce the desired heat flow while
retaining radial symmetry. It need not preserve a positive density; that
and the extension to \(r=0\) require analysis. This is another exact
representation, not a collision theorem.

**Potential additional arithmetic constraint.** A radial integration identity, a total-positivity property, or a differential intertwiner could relate several genuine readouts. Its useful content must survive the observation map and distinguish the theta density from other positive kernels admitting the same radial lift. A positive radial density alone supplies neither collision exclusion nor an RH implication.

**Bounded first task.** Analyze the three-dimensional inverse marginal for the genuine `Phi`, including `r = 0` and the tail. Compute the projected evolution of one proposed rotation-invariant operator and test the exact intertwining relation with `-partial_x^2`. If it fails, identify the entire correction and test one explicit weighted/interacting correction rather than quietly changing the target equation.

**Method-specific stopping result.** The inverse marginal is signed in the proposed positive class; the heat projection retains an unpaid radial drift; or fractional continuation changes the coefficients or loses a positive measure. The repository's negative theta coefficient at noninteger lattice rank is a control for that specific continuation, not a general impossibility theorem for fractional differential operators.

**Precedents.** [the dimension and volume note](../../../susy-positivity/investigations/fractional-dimension/notes/WHICH_DIMENSION_AND_THE_VOLUME_20260918.md) distinguishes distance, Busemann coordinate, and dimension parameter. [the rank and lattice note](../../../susy-positivity/investigations/fractional-dimension/notes/THE_RANK_AND_THE_LATTICE_20260918.md) and [the fractional dimension comparison](../../../susy-positivity/investigations/fractional-dimension/notes/THE_TRADE_IS_NOT_IT_20260918.md) prevent conflating fractional point-count positivity with the Weil criterion.

### Microlocal phase space and coherent state lifts

Proposed folder: `13_microlocal_phase_space`.

**Exact starting point and projection.** Define a real wave amplitude
\(\psi_t(u)=e^{tu^2/2}\sqrt{\Phi_e(u)}\). Then
\(\partial_t\psi_t=(u^2/2)\psi_t\) and

\[
H_t(z)=\tfrac12\int e^{izu}|\psi_t(u)|^2\,du.
\]

For the convention
\(W_t(u,p)=(2\pi)^{-1}\int e^{-ips}
\psi_t(u+s/2)\overline{\psi_t(u-s/2)}\,ds\),
the position marginal is \(\int W_t(u,p)\,dp=|\psi_t(u)|^2\). A direct
calculation gives

\[
\partial_tW_t=u^2W_t-\tfrac14\partial_p^2W_t.
\]

The negative diffusion survives in the lifted dynamics. Wigner distributions
need not be positive; coherent-state Husimi distributions are positive by
construction but have smoothed marginals. These standard distinctions and
limitations of coarse semiclassical descriptions are discussed by
Trushechkin in
[Semiclassical evolution of quantum wave packets on the torus beyond the Ehrenfest time](https://arxiv.org/abs/1607.07572),
Sections 2–3. That paper concerns free quantum evolution, not Newman heat.

**Arithmetic variant.** One can instead retain the finite coherent
coefficient vector \(q_n\) and its conjugate as a doubled state, together with
the full density matrix. Its off-diagonal entries retain interference; the
doubled state also records the reflected phase-sum terms. Discarding those
entries and retaining only \(\sum w_n^2\) recreates the packetwise diagonal
argument already disproved by the genuine adjacent packet.

**Potential new constraint, still speculative.** A phase-selective estimate
on interference or phase-space flux might correlate the value, derivative,
and higher jets at a candidate, or relate a local collision to the translated
average. A positive mass or a generic uncertainty inequality does not by
itself furnish coherent nonvanishing. Weak phase-space limits also need
careful scale control: errors that vanish asymptotically may remain much
larger than the exponentially small collision margin.

**Bounded first task.** Derive the continuous Wigner equation above with
explicit function-space and tail payments, or construct one exact finite
coherent-state resolution for a genuine block. Express both collision
coordinates and the fourth-jet test in that representation. Test one
interference-sensitive inequality and keep its error below the measured
target payment. Use the adjacent-packet cancellation as a required benchmark.

**Failure criterion.** The proposed result controls only total mass,
diagonal energy, or Husimi positivity; smoothing loses the adverse terms; or
the reconstruction error exceeds the needed sign margin.

### Integrable Lax and isomonodromic systems

Proposed folder: `14_integrable_lax`.

**Known finite starting point.** For a polynomial obeying
\(\partial_tP=-P_{zz}\), its simple roots satisfy

\[
x_i'=2\sum_{j\ne i}\frac1{x_i-x_j}.
\]

This follows directly by differentiating \(P(t,x_i(t))=0\). It has the
repulsive sign for real roots in increasing Newman time. Hall and Ho give a
finite matrix representation of heat-evolved polynomial roots and explain
their relation to Calogero–Moser systems in
[The heat flow conjecture for polynomials and random matrices, Sections 3.1–3.2](https://arxiv.org/html/2202.09660v3#S3.SS2).
Their time variable must be rescaled and reversed to match this convention.
Their large-degree transport conjectures are separate from these exact
finite identities.

**Bulk dynamics and projection.** A finite Calogero–Moser matrix system
projects its matrix coordinates to the roots and then to the characteristic
polynomial. For the genuine entire heat function, the exact logarithmic
derivative \(b=H_z/H\), away from its poles, instead obeys
\(b_t=-b_{zz}-2bb_z\). Neither identity establishes an arithmetic Lax pair,
finite-dimensional closure, or isomonodromic representation for the genuine
theta heat flow. Any finite approximation must pay its analytic error and
root-tail interaction before making a genuine collision claim.

**Potential new constraint, still speculative.** A special arithmetic
matrix or Riemann–Hilbert realization might impose additional spectral,
resolvent, or monodromy constraints that forbid a threshold degeneracy or
force the opposite jet sign. The extra constraint would have to come from
the theta/arithmetic data. Integrability alone permits collision solutions.
The invariant eigenvalues of a Lax matrix must not be confused with the
moving particle positions. An isomonodromic tau function can also vanish:
Bertola studies moment determinants as tau functions and their zeros as
obstructions to an associated Riemann–Hilbert problem in
[Moment determinants as isomonodromic tau functions](https://arxiv.org/abs/0805.0446).

**Bounded first task.** Reproduce the exact matrix lift for an even quartic
with a positive threshold and for one analytically controlled finite model
from the heat kernel. One concrete model is an initial Taylor polynomial and
its exact polynomial heat evolution, with a separately proved joint
time/spatial remainder on the chosen region. Identify a proposed arithmetic constraint satisfied by
the latter that excludes the former. Determine whether its characteristic
polynomial, tau function, or distinguished matrix element is the actual
projected observable, and pay jets through the first nonvacuous test.

**Failure criterion.** The candidate invariant is shared by the quartic
counterexample; the zeta lift is only formal; infinite sums are unrenormalized;
or a determinant is nonzero merely because it is a positive moment Gram
determinant unrelated to the oscillatory heat projection.

### Lee Yang and statistical mechanical partition functions

Proposed folder: `15_lee_yang`.

**Exact starting point and projection.** Define the unnormalized one-spin
partition function

\[
Z_t(h)=\int_{\mathbb R}e^{tu^2+hu}\Phi_e(u)\,du,
\qquad H_t(z)=\tfrac12Z_t(iz).
\]

Then \(\partial_tZ_t=\partial_h^2Z_t\): heat in the field variable becomes
backward heat after \(h=iz\). The normalized spin density
\(\mu_t(u)=e^{tu^2}\Phi_e(u)/Z_t(0)\) obeys the exact growth-selection
equation \(\partial_t\mu_t=(u^2-\mathbb E_tU^2)\mu_t\). For \(t\ge0\),
Gaussian decoupling gives
\(Z_t(h)=\mathbb E Z_0(h+\sqrt{2t}G)\). These representations are exact;
their positivity is present before any Lee–Yang property is proved.

**Known external input and its hypothesis.** Ferromagnetic Lee–Yang theorems
give nonvanishing partition functions in the half-plane \(\Re h>0\) when
the coupling and single-spin measures satisfy specific hypotheses. The
single-spin nonvanishing assumption cannot be omitted. These conditions are
stated explicitly in Fröhlich and Rodriguez,
[Some Applications of the Lee-Yang Theorem, Theorems 1–2](https://arxiv.org/pdf/1205.6643).
Simply calling the genuine theta measure a Lee–Yang measure at \(t=0\)
assumes the desired RH conclusion. Positive density and positive moment
Hankel matrices are weaker properties.

**Potential new constraint, still speculative.** Seek a constructive
ferromagnetic spin realization with independently certified elementary
single-spin factors whose magnetization law converges to the genuine theta
measure. Its coupling signs and convergence must be proved, rather than
inferred from a fitted distribution. A valid realization at time zero would
be an RH-strength result. A weaker regional realization or stable multiplier
comparison could instead provide a local threshold obstruction or a positive
Newman bound. That would be a useful separate outcome, not automatic descent
to zero.

**Bounded first task.** Choose one explicit finite-spin family with known
Lee–Yang single-spin measures and test whether its normalized magnetization
law can match the first several genuine theta moments under Gaussian
reweighting. Print the inverse moment or coupling constraints. If a candidate
family survives, derive complex-neighborhood approximation and jet payments
before using its zero geometry. Moment matching is a screening device only.

**Failure criterion.** Matching requires antiferromagnetic or inadmissible
couplings; the single-spin property is assumed for the unknown theta factor;
or convergence holds only for real fields/moments without the control needed
to transfer zeros or the paid collision test. A finite number of passing
moment constraints is not a Lee–Yang certificate.

### Nonlinear collective fields and exact moment closure

Proposed folder: `16_nonlinear_collective_fields`.

An interacting bulk could have a linear distinguished observable even when
its internal equations are nonlinear. One explicit starting point is the
normalized theta density

\[
Z_t=\int_0^\infty e^{tu^2}\Phi(u)\,du=H_t(0),\qquad
\rho_t(u)=e^{tu^2}\Phi(u)/Z_t,
\qquad m_2(t)=\int u^2\rho_t(u)\,du.
\]

It obeys the exact nonlinear normalization equation
\(\partial_t\rho_t=(u^2-m_2)\rho_t\).
Its cosine observable \(\chi_t(x)=\int\rho_t(u)\cos(xu)\,du\)
satisfies \(\partial_t\chi_t=-\chi_t''-m_2\chi_t\);
restoring \(H_t=Z_t\chi_t\) restores the desired heat equation exactly.
This elementary calculation supplies a calibration for collective dynamics,
not a new noncollision condition. Positive densities can have cancelling
Fourier observables.

The proposed extension is an interacting field or constrained moment system
whose genuine theta state lies on a distinguished invariant manifold.
Interactions could enforce relations among the signed second, third, and
fourth derivative moments at a candidate collision, or bind additional
observations to the value and slope. Their contribution to the reduced
equation must vanish or be absorbed by an explicit normalization, while
their constraint on admissible states remains effective.

The first bounded task is to derive the equations for jets through the fourth
spatial derivative, retaining the fifth and sixth derivatives introduced by
their time evolution. Then test a specified closure or symmetry against the
theta initial density and the quartic control. A useful result would be an
independently justified relation with a paid signed consequence. The
failure criterion is an unavoidable unclosed moment, a modified scalar
generator, or a closure whose regularity already assumes the absence of
zeros. The Burgers substitution based on \(\partial_x\log H_t\) can be a
diagnostic, but its poles at unknown zeros cannot be excluded by definition.

## Project map and opportunities for joint work

The catalog separates sources of extra structure, although projects can
share representations. The Gaussian project is a reference calculation;
the other projects seek additional content. None should claim success by
renaming that baseline or decorating a product lift with a grading.

| Proposed folder | Main mechanism to test | Intended exclusion interface |
| --- | --- | --- |
| `01_analytic_gaussian` | Holomorphic transverse diffusion and weighted observations | Quantitative visibility or a sharper short probe |
| `02_bargmann_fock` | Coherent states and holomorphic Hilbert geometry | Simultaneous overlap and derivative control |
| `03_susy_dirac_hodge` | Arithmetic supercharge and coupled boundary components | Regular closure or signed jet identity |
| `04_cohomological_localization` | Ward identities and a controlled localized observable | Threshold jet sign or joint observation inequality |
| `05_interacting_susy_gauge` | Collective interactions and gauge constraints | Arithmetic relation retained after reduction |
| `06_theta_lattice` | Lattice heat kernels, Poisson duality, and theta sectors | Genuine coefficient rigidity and correlated jets |
| `07_automorphic_scattering` | Cusp reduction and geometric spectral observables | Visibility, regularity, or spectral constraints |
| `08_adelic_local_models` | Coupled archimedean and prime-local factors | Exact arithmetic matching and surviving local constraint |
| `09_prime_phase_torus` | Actual height orbit in many phase coordinates | Signed correlations beyond all-torus bounds |
| `10_kinetic_stochastic` | Hidden variables, stochastic dynamics, and projection memory | Candidate-conditioned growth or a shorter average |
| `11_boundary_extensions` | Auxiliary fields, boundary response, and inverse spectra | Coherent observation control and exact response matching |
| `12_radial_bessel` | Radial reduction and continuous dimension parameters | Geometric restrictions tied to genuine coefficients |
| `13_microlocal_phase_space` | Correlated phase-space transforms and dual packets | Recombined signed vector or threshold jets |
| `14_integrable_lax` | Compatibility equations and spectral deformations | Collision restrictions beyond heat evolution |
| `15_lee_yang` | Partition functions, stability, and interacting spin systems | Real-rootedness or local derivative inequalities |
| `16_nonlinear_collective_fields` | Invariant state constraints and exact moment dynamics | Signed jet closure or joint visibility |

The first phase should give each project one bounded scout rather than an
open-ended construction campaign. The analytic Gaussian and theta-lattice
projects can establish common identities and normalization conventions.
The SUSY Dirac and localization projects can test whether a symmetry
actually acts on the joint observation. The prime-phase and microlocal
projects can search for the correlated arithmetic input already requested
in Note 13. Other geometric, stochastic, interacting, and integrable
projects should proceed independently with their own explicit reduction
and first obstruction test.

Useful collaborations include coherent-state formulas with microlocal
transforms; theta lattices with automorphic or adelic constructions; SUSY
boundary pairs with extension operators; and localization with interacting
partition functions. A contribution should cross projects as an explicit
identity or estimate with hypotheses, not as a general analogy.

## How the portfolio serves the five goals in Note 13

The projects are alternative or enabling routes to the existing goals;
they are not a sequence that must wait for the threshold-sign project.

| Goal in Note 13 | What a successful lift could supply | Natural initial contributors |
| --- | --- | --- |
| 1. Candidate-conditioned threshold sign | An arithmetic identity forcing the strict paid opposite of the necessary sign | 03–05, 11, 14–16 |
| 2. Correlated macroscopic transformation | A full-block transformation retaining cross terms, drift, and shared-height correlations | 06, 08, 09, 13 |
| 3. Collision-to-average transfer | A conditional upper bound overlapping a proved lower bound on the same probe | 01, 02, 10, 13, 16 |
| 4. Higher multiplicity | A signed hierarchy with individual payments or a sufficient multiplicity restriction | Shared work package for every jet route |
| 5. Global coverage | Explicit regions, overlaps, margins, and uncovered candidate parameters | Shared ledger across successful routes |

For the third goal, a shorter interval alone does not establish a
contradiction. The lower and collision-conditioned upper bounds must overlap
on that interval. On the current \(H_d\), a pure curvature route would need
\(M_2<\sqrt{3/32}\,L/H_d\), whereas the known absolute budget has size
\(C_2e^{\mathfrak a/t}\). The ratio of probe length to the currently
transferred scale is \((Dt^2/L)e^{3\mathfrak a/t}\).

For the fourth goal, let \(b_x=\partial_x^2\log A_t\). The full-deflation
necessary expressions at exact multiplicities three and four are

\[
E_3=\frac{q_4^2}{16}-\frac{q_3q_5}{10}
       -\left(b_x+\frac{3}{4x^2}\right)q_3^2\ge0,
\]
\[
E_4=\frac{q_5^2}{25}-\frac{q_4q_6}{15}
       -\left(b_x+\frac1{x^2}\right)q_4^2\ge0.
\]

Each needs its own measured quadratic approximation payment, then an
opposite arithmetic sign or a separate multiplicity restriction. Higher
orders retain the full-deflation hierarchy in Note 13. In particular,
time evolution of a fourth spatial jet involves a sixth jet;
\(\partial_tH_t^{(4)}=-H_t^{(6)}\) cannot be silently closed at order four.

## Common research record and stopping rules

Each project README should state its mathematical question and name the
enlarged state, generator, reduction map, arithmetic initial data, domain,
and intended collision implication. Its first numbered note should derive
the reduced equation and its time orientation before estimating signs.
Record the admissible state class explicitly: a proof for every freely
twisted coefficient phase cannot use a property specific to the genuine
height orbit.

Separate four milestones: an exact representation; a new property of the
genuine arithmetic state; a signed exclusion result with all errors paid;
and coverage sufficient for an endpoint conclusion. A project may finish
usefully at any earlier milestone or with a precise obstruction. A small
residual, successful typesetting, positive bulk norm, finite cutoff gap,
or a symbolic Ward identity must not be reported as the next milestone.

Numerical work should test a stated conjectured relation or locate the loss
in a specified mechanism. Retain actual common-height phases, fixed-time
derivatives, normalization, cutoff corrections, and the correct quadratic
payments. Finite models must state what their continuum or infinite-volume
limit would require. The repository's existing paid cell criterion is a
better compact checkpoint than a broad unverified zero grid.

For each scout, a useful failure result identifies the precise uncancelled
term, observation kernel, domain mismatch, coefficient mismatch, memory
term, or remainder that prevents the intended implication. The result
should be restricted to the mechanism actually examined. The existing
twist and quartic controls do not constitute a general no-go theorem for
all arithmetic lifts.

Save derivations in each selected project's `notes/`, numerical programs
and small records in `numerics/`, and scoped checks in `reviews/`. Include
the serving model and recorded reasoning effort, distinguish internal
LLM checks from independent review, and follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
Avoid new manuscript snapshot folders. Keep later milestone history concise
and point to commits or tags when they exist.

## Coverage and the next chat

A successful signed theorem in \(1\le\kappa\le2\), \(t\downarrow0\)
would cover only that sector. The endpoint still needs other relations
between time and height, compact positive-time regions, overlap estimates,
and higher multiplicities. Eventual simplicity at each time bounded away
from zero leaves a finite height range whose available proved cutoff diverges
as that lower time bound tends to zero. A finite set of certificates does not supply the
missing uniformity. The coverage ledger in Note 13 remains part of this
program, whichever lift mechanism succeeds.

The next chat should read this note, Note 13, the stable manuscript's signed
vector and threshold sections, and the
[program review](../../reviews/HEAT_DIMENSIONAL_REDUCTION_PROGRAM_REVIEW_20261010.md).
It can then instantiate the proposed project subfolders and distribute
bounded scouts in parallel. Begin each scout by deriving its reduction and
checking its proposed additional constraint against the relevant controls.
Choose a concrete signed target before expanding numerical work. The most
useful initial output is one explicit new arithmetic relation, or a sharp
obstruction to that relation in the chosen realization.

This conversation is recorded as chat **3**, “Review Newman collision
program”, in [chat histories](../../chat-histories/README.md) and the
[numbering registry](../../chat-histories/index.json). Its original creation
time is 2026-10-10T03:36:56.248Z, corresponding to 9 October 2026 at
23:36:56.248 America/New_York. The note date and archive capture date are
10 October 2026. A later refresh retains number 3; the next new conversation
uses number **4**. The archive preserves completed public text through its
capture, with subsequent delivery messages available for a later refresh.
