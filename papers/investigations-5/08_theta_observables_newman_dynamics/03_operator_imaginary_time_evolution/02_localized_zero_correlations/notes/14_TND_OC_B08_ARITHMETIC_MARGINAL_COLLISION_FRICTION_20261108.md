# B08: where the arithmetic, marginals and collision programs separate

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, existing chat0006. Actual recorded
model and effort are unavailable. This is a program-fit review with
elementary diagnostic derivations, **proof-author checking only**.
It acquires no canonical zero values or collision bound.

## 1. Finding and author decision

The intended program is mathematically reasonable, but the notes have
blurred three different achievements: representing a zero statistic in
terms of the arithmetic source; computing that statistic to prescribed
accuracy; and proving a constraint on unknown zeros. The first two do
not supply the third. The previous high-level explanation did not make
this distinction sufficiently concrete.

The author has now chosen a bifurcation: keep generalized marginals in
this investigation as a **high-risk, potentially high-reward** direction,
and create a separate investigation for alternatives that prioritize
constraining collisions. Neither direction is declared impossible.
The new [collision-constraint branch](../../03_collision_constraints/README.md)
owns TND-OA tasks. The existing [Green branch](../../01_green_potential_resolvent/README.md)
continues independently. Its tasks and statuses are not reassigned.

This respects the earlier [author-goal correction](08_TND_OC_RESTORING_GENERALIZED_MARGINAL_OBJECTIVE_20261108.md):
an immediate zero exclusion is not required for a useful marginal result.
It also corrects the later drift toward treating a finite evaluator as
the default way to obtain a collision-relevant arithmetic theorem.

Read the [result index](../../../../../../result-summaries/README.md),
especially [theta identities14](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[local geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../../avoid/README.md), especially
[classification01](../../../../../../avoid/01_restating_the_target.md),
[premise screen02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [volume20](../../../../../../avoid/20_volume_without_a_gain.md).
The gain here is a diagnostic and a change of research organization, not
a smaller canonical error, improved threshold, or RH result.

## 2. The actual theta-to-marginal map

There are two different spaces. The theta source lives in a real
integration variable u and has an arithmetic sum over integers n.
The zero marginals live in the positions z of zeros of its transform.
Marginalizing over zero positions is not marginalizing over u or n.

Use the inherited normalization
\[
\vartheta(v)=\sum_{n\in\mathbb Z}e^{-\pi n^2v},\qquad
p(u)=\tfrac12e^u[\vartheta(e^{4u})-1]
=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\quad u\ge0,
\]
\[
p''-p=8\Phi,\quad p'(0)=-\tfrac12,\qquad
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
\quad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\tag{1}
\]
Define the primitive transform, with notation distinct from the Green
potential,
\[
\mathcal P_\lambda(z)=\int_0^\infty p(u)e^{\lambda u^2}\cos(zu)\,du.
\]
Two integrations by parts give
\[
8H_\lambda=\tfrac12+(2\lambda-1-z^2)\mathcal P_\lambda
 +4\lambda z\mathcal P_\lambda'-4\lambda^2\mathcal P_\lambda'',
\qquad
8H_0=\tfrac12-(1+z^2)\mathcal P_0.
\tag{2}
\]
These are inherited from [parent Note11, §§3–4](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md),
not new identities or an estimating advantage.

For the multiplicity-sensitive zero measure,
\[
\nu_\lambda=\sum_j\delta_{z_j},\qquad
\nu_\lambda=\frac1{2\pi}\Delta\log|H_\lambda|,\qquad
\partial_{\bar z}\frac{H_\lambda'}{H_\lambda}=\pi\nu_\lambda
\tag{3}
\]
in distributions. Thus for a compact smooth test \(\phi\),
\[
\langle\phi,\nu_0\rangle
=\frac1{2\pi}\int_{\mathbb C}
 \log\left|\tfrac12-(1+z^2)\mathcal P_0(z)\right|
 \Delta\phi(z)\,dA(z).
\tag{4}
\]
The constant \(-\log8\) drops out because \(\int\Delta\phi=0\).
Equation (4) explicitly answers where the primitive enters a zero
statistic: **inside the logarithm of a signed, oscillatory expression**.
Positivity of p does not sign this expression, control its small values,
or provide a bound for its logarithm.

Fix lambda and a uniform center law on a finite interval. For clarity
take physical coordinates with no unfolding; the existing
declared rescalings only add the known Jacobians. Let W be a compact
smooth window and
\[
G_\epsilon(w)=\frac{e^{-|w|^2/(2\epsilon^2)}}{2\pi\epsilon^2},\quad
q_{X,j}(u)=W(z_j-X)G_\epsilon(u-(z_j-X)).
\]
The one- and two-point factorial intensities are
\[
r_X(u)=\sum_jq_{X,j}(u),\quad
R_{2,X}(u,v)=\sum_{j\ne k}q_{X,j}(u)q_{X,k}(v)
=r_X(u)r_X(v)-d_X(u,v),
\quad d_X=\sum_jq_{X,j}(u)q_{X,j}(v).
\tag{5}
\]
The diagonal term contains W squared. Distinct labels at a multiple zero
are still distinct: the subtraction removes self labels, not all
coincident positions. For a finite unweighted N-label configuration,
these factorial intensities equal the normalized marginal densities
times N or N(N−1). The windowed convention in (5) is an intensity, not
automatically a probability density.

Set \(\phi_u(\xi)=W(\xi)G_\epsilon(u-\xi)\),
\(K_u=\Delta\phi_u\), \(L_X(\xi)=\log|H_\lambda(X+\xi)|\), and
\(D_{u,v}=\Delta[W^2G_\epsilon(u-\cdot)G_\epsilon(v-\cdot)]\).
Then the center-averaged connected factorial function is exactly
\[
\begin{split}
C(u,v)&=\mathbb E_XR_{2,X}(u,v)
             -\mathbb E_Xr_X(u)\mathbb E_Xr_X(v)\\
&=\frac1{4\pi^2}\iint K_u(\xi)K_v(\omega)
 \operatorname{Cov}_X(L_X(\xi),L_X(\omega))\,dA\xi\,dA\omega\\
&\quad-\frac1{2\pi}\int D_{u,v}(\xi)\mathbb E_XL_X(\xi)\,dA\xi .
\end{split}
\tag{6}
\]
At time zero insert (2) into each logarithm. For the full averaged pair
function replace the covariance in (6) by the same-center product
expectation. Common-center dependence is essential.

Equations (4)–(6) are a genuine arithmetic representation. They also
expose the missing input: a useful **joint logarithmic estimate**, with
small-value behavior and two spatial variables controlled. Bounds on
individual source integrals do not determine it. The full pair retains
separate imaginary marks; a single arithmetic difference projection
does not recover it. [Note11](11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md)
and its [E08 assessment](../reviews/09_TND_OC_E08_CLAIM_LEVEL_ASSESSMENT_20261108.md)
already pay transfer errors but leave those joint inputs unacquired.

A third possible probability space is an auxiliary random-matrix
ensemble. Its joint density is not supplied by theta positivity.
Indeed \(H_\lambda(x)/H_\lambda(0)\) is the cosine transform of a
positive source probability measure. That probability concerns u;
it is not a joint distribution of the zeros. Symmetrizing zero labels
or randomizing the observation center produces valid empirical
marginals without proving a determinantal or Vandermonde law.

## 3. What a collision consumer would need

The Green branch gives the cleanest existing example of a consumer.
Put \(a=\pi/8\) and
\[
G(s,y)=\operatorname{atanh}\frac{\sin(ay)}{\cosh(as)},\quad
\mathcal J_\lambda(X)=\sum_{\Im z_j>0}G(X-\Re z_j,\Im z_j).
\tag{7}
\]
On the canonical strip \(|\Im z_j|\le1\), all terms are nonnegative.
For 0<d<=1, an upper zero at height at least d and horizontal distance at most r
forces
\[
\mathcal J_\lambda(X)\ge
m(d,r):=\frac{d\sin a}{\cosh(ar)}.
\tag{8}
\]
An independent arithmetic upper bound strictly smaller than m excludes
that specified defect. At time zero the existing exact comparison is
\[
\mathcal J_0(X)=\mathcal L(X)-P_{\rm prime}(X)+G(X,1),
\quad
\mathcal L(X)=\int_{\mathbb R}
\frac{\log|\zeta(1/2-ix/2)|}{16\cosh(a(x-X))}\,dx,
\]
\[
P_{\rm prime}(X)=\sum_{n\ge2}
\frac{\Lambda_{\rm vM}(n)}{\log n}
\frac{n^{-5/2}}{1+n^{-4}}\cos\!\left(\frac X2\log n\right).
\tag{9}
\]
The pole correction appears once. [Parent Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md)
and the [Green acquisition note](../../01_green_potential_resolvent/notes/06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md)
supply the representation and paid approximation; they do not supply
the favorable strict upper value. The universal vanishing assertion at
time zero is RH-equivalent and is not counted as progress.

There is also a real pair-marginal connection to this consumer.
With \(g_X(z)=1_{\Im z>0}G(X-\Re z,\Im z)\) and
\(\alpha_2=\nu\otimes\nu-\operatorname{diag}_*\nu\),
\[
\mathcal J(X)^2
=\langle g_X^2,\nu\rangle+\langle g_X\otimes g_X,\alpha_2\rangle .
\tag{10}
\]
Prove this first for finite sums and pass to the convergent positive
Green sum. Thus an appropriate full pair estimate could control a
second moment of the defect field, together with its one-point term.
It must have the required imaginary marks, localization and accuracy.
A connected statistic alone is not the nonnegative total in (10).

Using a Gaussian marginal in (10) replaces g by its Gaussian convolution;
this creates a bias and requires window/tail accounting. Even a real zero
has the exact smoothed positive-height contribution
\[
\int_{\mathbb C}(\Im z)_+G_\epsilon(z-x_0)\,dA(z)
=\epsilon/\sqrt{2\pi}.
\tag{11}
\]
This illustrates the real-zero background; it is not a claim that (11)
is the exact Green bias. Some biases can be subtracted: for a finite
weighted configuration,
\(\int((\Im z)^2-\epsilon^2)r_X(z)dA=\sum_jW_j(\Im z_j)^2\).
That signed, unbounded test still requires complete observation tails
and an arithmetic estimate.

Broad averaging has a separate cost. The new
[Green B04 note, §2](../../01_green_potential_resolvent/notes/09_TND_OG_B04_GREEN_MASS_RESOLUTION_AND_VALUE_DECISION_20261108.md)
proves \(\int_\mathbb R G(s,y)ds=\pi y\). One upper zero of height d
therefore contributes at most \(\pi d/T\) to a uniform [T,2T] average.
An unspecified o(1) error does not resolve that signal. That note also
shows the inherited density allowance fails its chosen one-defect
comparison; it does not prove that all statistical bounds fail.

## 4. One focused calculation: fixed smoothing versus a collision

Consider the exact finite heat-polynomial model
\[
f_s(w)=w^2-2s,\qquad \partial_sf_s=-\partial_w^2f_s.
\tag{12}
\]
Its roots are \(\pm d\) for s>0 and \(\pm id\) for s<0, where
\(d^2=2|s|\). This is a diagnostic for a relaxed class, not a canonical
theta source or a positive-source counterexample.

Take W=1 near the two roots, \(A_\epsilon=(2\pi\epsilon^2)^{-1}\)
and Q=[−1,1]+i[−1,1]. For the two real labels,
\[
R^{\rm real}_{2,\epsilon}(u,v)
=2A_\epsilon^2
 e^{-(|u|^2+|v|^2+2d^2)/(2\epsilon^2)}
 \cosh\!\left(\frac{d(\Re u-\Re v)}{\epsilon^2}\right).
\tag{13}
\]
For the imaginary pair replace Re by Im. Hence for d>0,
\[
\|R^{\rm real}_{2,\epsilon}-R^{\rm imag}_{2,\epsilon}\|_{\infty,Q^2}
\le \frac{4A_\epsilon^2d^2}{\epsilon^4}
          \cosh(2d/\epsilon^2)=O_\epsilon(d^2).
\tag{14}
\]
For proof, write cosh(t) as a function of \(t^2\); its derivative is
\(\sinh|t|/(2|t|)\le\cosh(2d/\epsilon^2)/2\) in this range.
The two squared arguments differ by at most \(4d^2/\epsilon^4\).
At u=v=0 the two values agree exactly.

Meanwhile the ordered inverse-square interaction is
\[
E(s)=\sum_{j\ne k}|z_j-z_k|^{-2}
=\frac1{2d^2}=\frac1{4|s|}.
\tag{15}
\]
Thus the pair signal at fixed blur vanishes quadratically as the
interaction diverges. A fixed positive absolute error for the smooth
pair function cannot uniformly distinguish these two configurations
at arbitrarily small d. This excludes that inference on the stated
two-label class, not a canonical arithmetic method with stronger input.
Exact Gaussian convolution is injective on finite measures; its inverse
amplifies Fourier errors by \(\exp(\epsilon^2|k|^2/2)\). The issue is
finite-error stability, not loss of all exact information.

For the imaginary pair, the Green contribution at its center is
\(G(0,d)=ad+O(d^3)\). It vanishes at the double real zero itself:
a nonreal-defect detector must be coupled to time or event geometry
to constrain the collision. Moreover E decreases as s increases on
the real side but increases on the imaginary side. Real-root
dissipation does not extend unchanged to arbitrary complex pairs.

## 5. Where dynamics can help, and what remains missing

At a simple zero, implicit differentiation gives exactly
\[
z_j'(\lambda)=H_\lambda''(z_j)/H_\lambda'(z_j).
\tag{16}
\]
For a finite polynomial solving this heat equation it equals
\(2\sum_{k\ne j}(z_j-z_k)^{-1}\).
The canonical infinite-zero formulation needs the appropriate product
normalization, paired sums and exterior control; a finite cutoff does
not remove those obligations.

This is why pair information can matter: the force is a pair observable.
But its kernel is singular, and pair evolution brings in further
particles and boundary terms. A definition of a hierarchy is not a
closed evolution law. One needs control near the diagonal or a
separation/regularization argument that pays the singular remainder.

[Rodgers–Tao v5](https://arxiv.org/html/1801.05914v5), §4, (56), and
§§8–9 illustrate a successful connection: under their all-real
contradiction hypothesis, dynamics forces almost all normalized gaps
toward one; the known positive proportion of smaller gaps contradicts
that conclusion. They do not obtain their result by detecting one
arbitrary sparse defect with a coarse average. Their real-root ordering
and energy estimates cannot simply be imported for a complex cloud.
These selected passages were checked; no fresh full-paper audit or
new external theorem is asserted.

For collision constraints, a prospective argument must provide either
a localized arithmetic estimate at the dangerous scale, or a proved
amplification from the proposed event to a statistically detectable
effect. Neither has yet been obtained for the present full nonreal
marginal program. This does not prevent a useful intermediate
correlation theorem without a collision consequence.

## 6. Premise-level control screen and evidence limits

This is a documentary screen against the recorded witnesses in
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
not a numerical replay. No collision exclusion is proposed here.

| Control class | What it permits; premise distinguishing the canonical application |
| --- | --- |
| Euler-factor controls | Positivity, evenness and rapid decay do not preclude collisions. The complete unmodified theta/xi arithmetic in (1)–(2) is changed. Generic zero-measure and marginal identities still apply. |
| Weighted-square controls | Square support and finitely many source/primitive endpoints are insufficient. Full normalized reflection and the complete unit-weight theta expansion fail. |
| Reflected super-Gaussian | Reflection, source positivity and all listed endpoints do not supply a repulsion theorem. The complete integer-square theta expansion fails. |
| Smooth shape / positive primitive | Source shape and even a positive primitive transform do not supply the missing signed or joint-log estimate. Exact theta arithmetic fails. |
| Finite-prime-compatible controls | Any fixed selected-prime list and finite measurements can coexist with the recorded collisions. Full reflection fails; no obstruction to a controlled infinite arithmetic assembly follows. |
| Fixed-event / finite-profile threshold controls | Finite profiles and common moment bounds do not determine the event jet. The unchanged theta source, complete profile growth and eventual-simplicity premises fail as specified in the source. |
| RH-conditional normalized endpoint control | Under RH, close positive sources can preserve the displayed completion and pole residue while adding time-zero double zeros escaping to infinity. Ordinary Dirichlet-series arithmetic fails; the separate polynomial control has a different preservation list. |
| Raw-kernel and finite-observation relaxations | Shared amplitudes or selected actual profiles do not impose the physical cosine/Newman equation or an integer complete divisor, respectively. Their failures concern the relaxed class only. |

The local model (12) likewise fails the canonical-source premise.
Identities (3), (5), (6), (10) and generic heat dynamics are compatible
with collisions and cannot themselves reject these controls. An
arithmetical estimate must do the separating work. Merely saying
“use the exact theta source” identifies a premise, not the estimate.

## 7. Disposition and division of work

[Note13](13_TND_OC_B07_COMPLETE_DIVISOR_AND_GAUSSIAN_EVALUATOR_20261108.md)
does use arithmetic: its proposed evaluator certifies a complete finite
zero inventory by exact-zeta interval evaluations, then computes the
Gaussian marginal. It is not circular as a finite computation and does
not assume RH. It does, however, obtain the positions before calculating
their statistics. That is a benchmark or descriptive acquisition route,
not a new analytic constraint on unknown configurations. Its conditional
<1/3000 error bound has not been executed.

The author-directed division is:

- **OC, generalized marginals:** retain full marked marginals, the
  theta/primitive dictionary, common-center dependence, and paid error
  transfers. Pursue an arithmetic correlation estimate or a useful
  evolution relation as an independent research objective. E09 stays
  available as an optional finite benchmark; it is no longer the
  automatic collision-facing successor.
- **OA, collision constraints:** start with a stated event, domain and
  quantitative consequence. Compare event-conditioned source/primitive
  jets with localized gap/exterior-force barriers; use the Green
  consumer as the existing direct comparator. Do not require OC to
  succeed first, and do not repeat generic representations as new gains.
- **OG, Green:** retain its current ownership, acquisition results,
  resolution limits and separately planned feasibility work. This
  bifurcation neither activates nor changes its tasks.

The [continuation](../continuation-notes/16_TND_OC_AFTER_B08_BIFURCATION_AND_MODEL_CHANGE_20261108.md)
fixes the OC successor and links the new branch's standalone prompt.
A source-specific quantitative improvement, an independently useful
marginal theorem, or a scoped failed candidate can complete the next
bounded cycle. More definitions alone cannot.
