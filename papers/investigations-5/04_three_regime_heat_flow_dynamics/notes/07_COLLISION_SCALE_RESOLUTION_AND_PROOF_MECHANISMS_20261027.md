# Collision scale estimates and possible positive time exclusion mechanisms

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.
Affiliated with **Review three-regime heat-flow status**, chat0003,
thread `01a17da8-4a84-7df3-b309-ec18e0535f1e`.

**Status: analytical synthesis, elementary conditional deductions, and
research proposals; same-assistant assessment only.** Shrinking the
complex observation region with the square root of elapsed heat time
removes a particular exponential loss in the real-to-complex Gaussian
estimate. It does not remove the vanishing field amplitude or distinguish
theta from colliding controls. A possible positive-threshold argument
would need an independent canonical estimate below a collision's
scale-invariant signal, or a bound on its accumulation across scales.
No such arithmetic inequality is acquired here; TRD task statuses remain
unchanged.

The [result index][results], [local-geometry summary][geometry],
[control register][controls] and [avoid index][avoid] govern the scope.
In particular, [target classification][classify],
[control screening][screen], [scoped conclusions][scope] and
[coupled estimates][coupled] apply. The endpoint-energy target already
appears in [the positive-threshold analysis][positive], Section 5B.
The universal heat-scale profile and its control obstruction already
appear in [BW-10 Note22][oldprofile]. The present contribution is the
connection to the hierarchy's complex-kernel loss, the explicit scaling
of the weak-response transfer, and the dyadic interpretation below.
These are not claims of a new RH criterion or literature priority.

## 1 Which time is being rescaled

The hierarchy in [recurrence Note20][moving] uses
T=-t>0 and L=log(X/(4pi)). Its strongest complete comparison reaches
1/L<=T<=2; its fixed complex buffers incur exp(Y^2/(4T)). The earlier
[signed crossover][crossover] and [joined construction][bridge] reach
t=0 with weaker errors. The exact canonical field is jointly analytic
at every finite time and position.

For a hypothetical positive collision, use a different parameter.
Let t_c>0 be its time, a its real location, and set

\[
t=t_c+r^2s,\qquad z=a+rw,\qquad r>0.
\tag{C1}
\]

Here r^2 is distance from the event on slices s=+/-1. It is not t_c,
and the original negative-time theorem cannot be applied by relabeling
its time. The shifted field has source

\[
\Phi_c(u)=e^{t_cu^2}\Phi(u),\qquad
H(t_c+v,z)=\int_0^\infty e^{vu^2}\Phi_c(u)\cos(zu)\,du.
\tag{C2}
\]

The complete source remains canonical with this explicit multiplier.
Any approximation, arithmetic identity or domain hypothesis must be
checked for it. In particular, Dobner's ordinary damped Dirichlet series
cannot simply be used at a positive shifted base time.

## 2 What the collision becomes in scaled coordinates

Assume exact multiplicity m>=2 at (t_c,a), and put
c=H_z^{(m)}(t_c,a)/m! !=0. Define

\[
F_r(s,w)=\frac{H(t_c+r^2s,a+rw)}{c r^m},\qquad
P_m(s,w)=e^{-s\partial_w^2}w^m
=\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{m!(-s)^k}{k!(m-2k)!}w^{m-2k}.
\tag{C3}
\]

Both satisfy the backward heat equation in (s,w). The Taylor expansion
and H_t=-H_zz give, on every fixed bounded scaled set,

\[
F_r(s,w)=P_m(s,w)
 +r\frac{H_z^{(m+1)}(t_c,a)}{(m+1)!c}P_{m+1}(s,w)+O(r^2).
\tag{C4}
\]

This is conditional on the event. It is the usual Hermite unfolding,
with normalization consistent with [Polymath Proposition 3.1(ii)][poly].
For m=2, P_2=w^2-2s. On s=-1 its roots are +/-i sqrt(2); on s=+1
they are +/-sqrt(2). Thus nonreal roots before the collision and real
roots after it remain separated at order one in scaled coordinates.

A direct bound preserves the amplitude dependence. Choose rho>0,
S,B>0 and

\[
M=\int_0^\infty
 e^{(t_c+\rho^2 S)u^2+\rho(B+1)u}\Phi(u)\,du<\infty.
\]

For |s|<=S, |w|<=B+1, the function
q -> H(t_c+q^2s,a+qw) is holomorphic and bounded by M on |q|<=rho.
Its coefficients below m vanish, and its coefficient of q^m is cP_m.
Cauchy's estimate therefore gives, for 0<r<=rho/2,

\[
\sup_{|s|\le S,|w|\le B}
|\partial_w^j(F_r-P_m)|
\le \frac{2j!M}{|c|\rho^{m+1}}r.
\tag{C5}
\]

The extra unit is a unit in w, hence a physical buffer of size r.
An analogous extra s buffer gives scaled time derivatives. Constants
depend on the event and m. This adapts the complete-source normal-form
bound in [BW-10 Note22][oldprofile]; it supplies no lower bound for |c|
and no all-height uniformity.

The leading polynomial contains no t_c. Smooth heat evolution, including
positive sources that really collide, has the same local limit. A
bounded scaled field or a correct Hermite limit cannot alone distinguish
a positive collision from one at zero.

## 3 The exponential loss disappears from the scaled kernel

For every epsilon>0 the complete canonical source gives the exact identity

\[
H(t_c-\epsilon,z)=\int_{\mathbb R}
k_\epsilon(z-u)H(t_c,u)\,du,\qquad
k_\epsilon(v)=(4\pi\epsilon)^{-1/2}e^{-v^2/(4\epsilon)}.
\tag{C6}
\]

For z=x+iy its kernel modulus contains exp(y^2/(4epsilon)). Set
epsilon=r^2 theta, u=a+rv and z=a+rw. Then exactly

\[
k_{r^2\theta}(a+rw-u)\,du
 =(4\pi\theta)^{-1/2}e^{-(w-v)^2/(4\theta)}\,dv.
\tag{C7}
\]

On |Re w|<=A, |Im w|<=B and theta in a fixed compact subset of
(0,infinity), its absolute size is controlled independently of r.
The factor is exp((Im w)^2/(4theta)), not exp(C/r^2).
Derivatives also behave correctly in scaled norms:

\[
\partial_w=r\partial_z,\qquad
\partial_s=r^2\partial_t.
\tag{C8}
\]

Unscaled derivatives still have inverse powers of r. Keeping the old
fixed physical Cauchy buffer would reintroduce the large exponential;
the target, analytic buffers and derivative norms must all scale together.

Here is a precise elementary transfer statement. Suppose a real-axis
initial-data error e_0 satisfies

\[
|e_0(a+rv)|\le \delta |c|r^m(1+|v|)^M
\quad\text{for every real }v.
\tag{C9}
\]

Convolving this error as in C6 and dividing by c r^m gives, on the
fixed scaled rectangle,

\[
\max_{0\le j\le J}|\partial_w^j e_r(\theta,w)|
 +|\partial_\theta e_r(\theta,w)|
\le C_{A,B,M,J,\theta_0,\theta_1}\delta.
\tag{C10}
\]

Differentiate the scaled Gaussian in C7: its derivatives are fixed-degree
polynomials times that Gaussian. Their weighted real integrals are finite
uniformly for theta_0<=theta<=theta_1. This proves C10. It is a transfer
lemma under C9, not an assertion that our canonical approximations satisfy
C9 independently of the event.

Localization retains a tail. If C9 holds only for |v|<=V and the outside
error is bounded by D, take V>=2A+2. For fixed theta in [1/2,2], the
omitted normalized contribution, with the stated finite derivatives, is
at most

\[
C\frac{D}{|c|r^m}e^{-V^2/64}.
\tag{C11}
\]

The constant absorbs the polynomial derivative factors by a second
Gaussian split. For fixed event data, V of order sqrt(log(1/r)) can
pay a prescribed small tail; the physical radius rV still tends to zero.
This does not provide a height-uniform bound when D/|c| is uncontrolled.

The remaining conditioning is decisive: raw errors must be small against
|c|r^m. A fixed height-dependent envelope allowance need not be so at
arbitrarily small r. Removing the exponential does not remove this
amplitude requirement. Exact cancellation of low Taylor jets can yield
an O(r) normalized remainder, as C5 does, but a model built by assuming
the collision then reproduces its profile rather than excluding it.

## 4 A local transverse response has a stable scaled transfer

Choose a nonnegative smooth compact cutoff chi in the w plane, equal to
one near every root of P_m(-1,w), with a fixed scaled buffer. Its size
may depend on m. For sufficiently small r, an isolated event has exactly
its m descendants in the relevant neighborhood. Define

\[
Y_r=\sum_{H(t_c-r^2,z)=0}
\chi((z-a)/r)(\Im z)^2.
\tag{C12}
\]

The Hermite root square sum gives

\[
\frac{Y_r}{r^2}\longrightarrow 2m(m-1)\ge4.
\tag{C13}
\]

This is the moving-cutoff version of the response in [Note01][response],
under a local count/no-entry gate. A single exceptional event survives
this normalization. No division by a growing total zero population occurs.

Let f_r(w)=F_r(-1,w), psi(w)=chi(w)(Im w)^2 and use a dimensionless
regulator eta>0. Distributionally,

\[
\mathcal Y_{r,\eta}=\frac1{4\pi}\int_{\mathbb C}
\log(|f_r(w)|^2+\eta^2)\Delta_w\psi(w)\,dA(w)
\longrightarrow Y_r/r^2\quad(\eta\downarrow0).
\tag{C14}
\]

For two scaled fields with sup difference delta on the test support,

\[
|\mathcal Y_{r,\eta}(f)-\mathcal Y_{r,\eta}(g)|
\le \frac{\|\Delta_w\psi\|_1}{4\pi}\frac{\delta}{\eta}.
\tag{C15}
\]

The gradient norm of log(|v|^2+eta^2) is at most 1/eta. In physical
coordinates psi_r=r^2 psi((z-a)/r), so
||Delta_z psi_r||_1=r^2||Delta_w psi||_1. The factor r^2 cancels the
response normalization. There is no extra r loss hidden in this transfer.

Regulator bias still needs its own estimate. At s=-1, the scaled Hermite
roots are simple and separated; C5 and fixed contours give local unit
floors for sufficiently small r at the fixed event. The coalescence-safe
allowance in Note01 supplies a sufficient bias tending to zero uniformly
under those gates. One may choose eta->0 with delta/eta->0 only after
acquiring the normalized delta. In field units the regulator is
eta |c|r^m, and that shrinking scale cannot be omitted.

C14--C15 are auxiliary diagnostics, not substitutions into the Book's
fixed physical regulator or covariance equations. Differentiating moving
tests or regulators in time would require their additional terms.

## 5 One collision produces a signal on every logarithmic time scale

Suppose now t_c=Lambda>0. Above t_c all zeros are real and simple.
For the m descendants of the event, set s=t-t_c>0 and

\[
E_{\rm cl}(s)=\sum_{i<j}(x_i(t_c+s)-x_j(t_c+s))^{-2}.
\tag{C16}
\]

Let h_i be the roots of P_m(1,w). Hermite splitting gives
x_i=a+sqrt(s)h_i+O(s). Consequently

\[
E_{\rm cl}(s)=\frac{\kappa_m}{s}+O(s^{-1/2}),\qquad
\kappa_m=\sum_{i<j}(h_i-h_j)^{-2}
=\frac{m(m-1)}{16}.
\tag{C17}
\]

The weaker displayed error already suffices; the common first drift
can sharpen it, but no sharper error is used here. These are unordered
pairs, so the constant is half the corresponding ordered-pair convention.
For a double collision the gap squared is 8s and kappa_2=1/8.

For completeness, P_m satisfies
P_m''-(w/2)P_m'+(m/2)P_m=0. At each root,
sum_(j!=i)(h_i-h_j)^(-1)=h_i/4. Squaring and summing cancels every
cross term belonging to a triple of distinct roots, leaving twice the
unordered inverse-square sum. Since sum_i h_i^2=2m(m-1), C17 follows.
This evaluates the positive coefficient in the existing
[threshold-energy discussion][positive]; it does not supply an upper bound.

Integrating on one time annulus gives

\[
\int_{r^2}^{4r^2}E_{\rm cl}(s)\,ds
=\kappa_m\log4+O(r).
\tag{C18}
\]

There are infinitely many disjoint such annuli approaching s=0.
Each eventually contributes a fixed positive amount. Thus a single
collision, invisible to a normalized large-height count, has a
logarithmically divergent temporal energy signature:

\[
\int_\epsilon^{s_0}E_{\rm cl}(s)\,ds
=\kappa_m\log(s_0/\epsilon)+O(1).
\tag{C19}
\]

The O(1) is for fixed event data and fixed sufficiently small s_0.
This is not a contradiction: ordinary heat-polynomial and positive-source
controls exhibit precisely this divergence. Smoothness of H does not
imply integrability of inverse-gap energy. Forward energy dissipation
allows a singular lower endpoint. Weighting energy by s, or subtracting
the collision's kappa_m/s term, removes the very signal needed here.

## 6 Possible contradiction mechanisms and their missing arithmetic input

### A An endpoint energy budget independent of the lower cutoff

Let W be a fixed bounded real interval containing the event and with
zero-free boundary at t_c. For small s>0 let E_W be the unordered pair
energy of all zeros in W. It is nonnegative and dominates E_cl.
Any independently proved bound of the form

\[
\int_\epsilon^{s_0}E_W(t_c+s)\,ds
\le \theta\log(s_0/\epsilon)+C,\qquad \theta<1/8,
\tag{C20}
\]

with C independent of epsilon, contradicts C19. A finite integral or
an o(log(1/epsilon)) bound would be stronger examples. The constants may
depend on the fixed event location, positive t_c and W; for excluding
each finite event they need not be uniform over every height. They must
not depend on an assumed minimum gap or a lower time cutoff.

A contradiction argument may fix a hypothetical event and then take r
sufficiently small depending on its finite local constants. It need not
locate that event numerically or make all constants practical in advance.
The independent upper inequality must still hold for every possible
canonical event; an event-dependent diagnostic is not a prescribed
certificate or an acquired uniform source estimate.

This is a **final-strength target**, already anticipated in the parent
positive-threshold program, not a newly established milestone. To use
the hierarchy, one would need a complete source expression for this
energy or its logarithmic primitive, and a theta-dependent signed saving
that survives localization and summation over the annuli.

For a finite cluster, the discriminant
D(s)=product_(i<j)(x_i-x_j)^2 behaves like
const*s^(m(m-1)/2). Its logarithmic variation can represent the same
divergence without separately solving for every root. The finite
coefficient-transport work in [HDC Note12][coefficients] is relevant.
But replacing root energy by log D just transfers the endpoint problem;
assuming a positive endpoint discriminant would assume the conclusion.
Exterior drift, moving membership and complete coefficient errors must
be retained. Existing Rodgers--Tao estimates on intervals separated
from their lower endpoint do not establish C20 at a positive threshold.

### B A source bound below the local transverse response

For the fixed-event cutoff of Section 4, an independent canonical bound
limsup_(r->0) Y_r/r^2<4 contradicts C13. More generally it suffices to
beat 2m(m-1) for every possible multiplicity with a paid cutoff and count.
This avoids dilution by the total zero population and connects directly
to TRD-02's weak-potential methods.

The proposed useful intermediate theorem is a source-derived estimate
for C14 with a complete scaled transfer/bias allowance, preserving signed
arithmetic cancellation. Computing the Hermite limit from the event and
then estimating that same limit does not supply the independent upper
bound. Neither a fixed absolute field error nor a source moment majorant
automatically pays the normalization |c|r^m.

This too is a final-strength collision-exclusion target. A quantitative
transfer improvement on a declared family is a separate approximation
milestone, judged by its actual error and applicable range.

### C Matching the inner profile to the actual exterior

Write H(t_c,z)=(z-a)^m U(z), with U nonzero locally. The inner Hermite
profile fixes the singular cluster contribution; derivatives of log U
carry the exterior influence. A contradiction could come from a
canonical source restriction on that influence or on the coupled low
jets which is incompatible with a colliding cluster.

This explains where arithmetic could enter after the universal leading
profile has been removed. It does not establish such a restriction.
The full event conditions are oscillatory source identities, for example

\[
\int_0^\infty e^{t_cu^2}\Phi(u)\cos(au)\,du=0,
\quad
\int_0^\infty u e^{t_cu^2}\Phi(u)\sin(au)\,du=0.
\tag{C21}
\]

Positivity of Phi does not sign these oscillatory integrals. A successful
bound would have to use information from the unchanged theta arithmetic
that fails for the controls, and identify an actual inequality it improves.
The existing [near-axis cluster comparison][nearaxis] already retains
exterior curvature but does not give a nonvanishing floor. Merely matching
another universal profile would repeat that unresolved issue.

## 7 Control calculations and the scope they impose

The heat polynomial z^2-2(t-t_c) has a positive collision at any prescribed
t_c>0 and satisfies all the scaled kernel/profile conclusions. It lacks
the canonical source, growth and arithmetic.

A positive atomic example makes the positivity limitation explicit:

\[
F(t,z)=e^t\cos z+e^{-3t_c}e^{4t}\cos(2z).
\tag{C22}
\]

Its source consists of positive atoms at frequencies 1 and 2. Put
b=e^{3(t-t_c)} and q=cos z. Apart from e^t its zero equation is
2bq^2+q-b=0. Both roots lie in [-1,1] exactly when b>=1; for b<1
one root is below -1. Thus its all-real times are exactly [t_c,infinity).
At (t_c,pi), F=F_z=0 and F_zz=-3 exp(t_c). It passes C3--C19 with m=2.
It has infinitely many simultaneous threshold events and lacks the
canonical high-height exterior behavior, so it does not test arguments
which genuinely use that extra information.

The full repository screen is retained:

| Control class | What survives this rescaling | Premise missing for a canonical application |
| --- | --- | --- |
| Euler-factor families Phi_(c,p) | Heat equation, positivity, substantial arithmetic structure, local profiles and relevant positive thresholds | Unchanged coefficients and completion; the derived proposed inequality must still be tested, not rejected merely by naming the changed source |
| Weighted-square and finite-tail controls | Actual local multiple events, square support and their listed finite constraints | Full canonical source; these families need not have any all-real heat time, so only the local portions apply |
| Reflected super-Gaussian and smooth positive-primitive controls | Positive/regular source, reflection or primitive data as recorded, and local collisions | Unchanged ordinary theta arithmetic; preservation lists differ between controls |
| Counter-kernels q and q_(T,a) | Genuine positive-threshold mechanisms and heat-scale unfolding | Canonical theta completion and arithmetic |
| Finite-prime and finite-profile controls | Their stipulated exact observations and local events | Full reflection or full profile/asymptotic data, as specified in the control register |
| Smooth-density replacement and two-channel exclusion | Their positive component constructions and exact bookkeeping | These [scoped form obstructions][forms] screen inference from positive pieces to a signed conclusion; they are not additional scalar heat-collision examples |

Every universal estimate above is expected to pass applicable colliding
controls. No separating canonical estimate has been proved. The prior
[leading-profile obstruction][oldprofile] applies directly; it does not
exclude a new source-specific subleading or integrated inequality.

## 8 A bounded analytical next step

The useful next investigation is a comparison of **actual signed source
terms at the scaled observable**, rather than another proof of Hermite
splitting or a numerical search for ever smaller residuals.

First choose either C20's cumulative energy or C14's transverse response.
Write its complete source/coefficient representation for the shifted
canonical field, with the exterior, amplitude normalization and moving
test terms explicit. Then identify the leading contribution that is
O(1) on each logarithmic scale. Test whether a coupled theta estimate
improves that contribution relative to the matching controls. A remainder
of order O(r^alpha), alpha>0, would be summable on geometric r scales,
but the O(1) collision contribution itself must be bounded independently;
summable approximation errors do not make it summable.

A positive return would be a new source-dependent bound with its precise
coefficient/rate and complete transfer. A negative return should identify
the specified information class that cannot beat the Hermite signal.
This task is analytical and can be attempted before implementing a field
evaluator. It does not supersede chat0002's localized response work or
chat0001's Dobner program. The [same-assistant assessment][review] records
the checks and the unresolved arithmetic step.

[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[forms]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[screen]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[positive]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[moving]: ../../01_heat_density_asymptotics/recurrence/notes/20_MOVING_LOWER_ENDPOINT_20261026.md
[crossover]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[bridge]: ../../01_heat_density_asymptotics/ansatz/notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md
[response]: 01_BUFFERED_RESPONSE_AND_RESOLUTION_20261026.md
[oldprofile]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[coefficients]: ../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[nearaxis]: ../../../investigations-4/12_height_dependent_heat_contours/notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md
[poly]: https://arxiv.org/html/1904.12438v2#S3
[review]: ../reviews/04_COLLISION_SCALE_MECHANISMS_SELF_ASSESSMENT_20261027.md

## 9 Follow-up: partial upper bounds and what recentering means

27 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual recorded effort max**, verified for turn
`01a17e15-ead3-77a2-a719-edcd61fff358`. This is a clarification and
conditional bookkeeping statement, not a new acquired upper bound.

The fixed-slab target is inherited from [the positive-threshold note][positive],
Section 5A. Choose 0<b<B with an established Lambda<=B. If Lambda>b,
the canonical positive-time exterior theorem, uniform near Lambda,
gives a finite threshold collision at t_c=Lambda in (b,B]. Excluding all
such candidate events therefore implies Lambda<=b. The existing
[Polymath Theorem 1.5](https://arxiv.org/html/1904.12438v2)
provides eventual real/simple zeros, with a uniform theoretical onset of
shape exp(C/b) on a fixed positive time slab in its stated range. A finite
height computation without its exterior does not give a global upper bound.
No assertion about a new best published numerical bound is made here.

The energy formulation turns this into an explicit comparison. Suppose
an order-N source argument independently gives, at every candidate,

\[
\int_\epsilon^{s_0}E_W(t_c+s)\,ds
\le [A_N(t_c,a,W)+\eta_N(t_c,a,W)]
\log(s_0/\epsilon)+C_N(t_c,a,W,s_0),
\tag{C23}
\]

where eta_N is a complete nonnegative error allowance and C_N is
independent of epsilon and an assumed minimum gap. The bound
A_N+eta_N<1/8 at every candidate in (b,B] excludes all multiplicities
by C17--C19. Better hierarchy estimates could lower eta_N and allow a
smaller b, if the main estimate A_N supplies the requisite margin.
Neither A_N nor eta_N in C23 has been acquired by this follow-up.
The hierarchy does not itself supply the missing canonical inequality.

There are two distinct roles for a remainder on geometric time annuli.
An O(r^alpha) allowance with alpha>0 sums to a finite constant and only
changes C_N. An allowance that approaches a nonzero constant per annulus
accumulates into the coefficient eta_N of the logarithm. Refinement of
that coefficient can change which positive slabs are excluded; merely
reducing an already summable error cannot fix an incorrect leading
coefficient. Turning field errors into energy errors also requires a
complete observable/coefficient comparison; root-gap denominators may
not be treated as uniformly bounded at the candidate event.

Recentring consists of two operations with different logical status:

1. The exact change G(tau,z)=H(t_c+tau,z), with
   Phi_c(u)=exp(t_c u^2)Phi(u), followed by z=a+rw and tau=r^2 s.
   This is legitimate for an arbitrary hypothetical event and does not
   require locating it numerically. The unknown a,t_c remain parameters.
2. A new error theorem adapted to that shifted source and those shrinking
   windows. The original negative-time hierarchy does not supply it just
   by changing the label on time. For example,
   exp(-r^2 u^2)Phi_c(u)=exp((t_c-r^2)u^2)Phi(u): a slice at negative
   relative time still has positive absolute heat time when r^2<t_c.
   The original arithmetic, source tails, amplitude |c|r^m and all
   retained modes must still be paid. One may equivalently keep original
   coordinates while organizing a local expansion around (t_c,a).

The exact shift preserves the heat equation; it does not convert the
canonical positive-time problem into the original negative-time one.
Existing universal profile controls pass this reorganization. The
[Section 7 screen](#7-control-calculations-and-the-scope-they-impose)
therefore applies unchanged: no control is newly excluded, and C23 must
ultimately identify a genuinely separating canonical estimate.

A fixed b>0 allows constants and exterior cutoffs depending on b. The
limit b down to zero requires further work; the exterior exp(C/b) growth
is distinct from the complex Gaussian exp(y^2/(4 epsilon)) loss removed
by local rescaling. The latter improvement alone does not control the
former. A numerical improvement in the actual global bound would be a
milestone; C23 is only its conditional specification, under the
[result index][results] and [target-classification rule][classify].
