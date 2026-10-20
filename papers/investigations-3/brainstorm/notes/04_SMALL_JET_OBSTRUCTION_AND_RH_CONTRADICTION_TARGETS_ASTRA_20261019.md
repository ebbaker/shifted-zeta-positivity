# Small jet obstruction and precise contradiction targets for RH

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

**Status:** living brainstorm and explanation of existing reductions, with
proposed research questions. No new arithmetic estimate, exclusion theorem,
or mathematical status upgrade is asserted. Continue updating this note as
the affiliated conversation develops; preserve dated changes and distinguish
existing results from proposed mechanisms.

The immediate objective is to identify an independently estimable arithmetic
statement that conflicts with a necessary consequence of a hypothetical RH
counterexample. Accurate approximation has made that conflict quantitative,
but has not supplied the missing arithmetic estimate. A restricted result
can be worthwhile before a global contradiction is available.

The starting documents are [Project 11 Review 19][review19] and the
[fixed function research program][program]. Read them with the repository
[result summaries][results] and [patterns to avoid][avoid], particularly
[collision controls][controls], [local laws and equivalent criteria][laws],
[target classification][classification], [scoped exclusions][scope], and
[signed recombination][pairing]. The [earlier priority note][priorities]
already identifies a collision-divergence contradiction; this note puts it
beside the retained-sum, threshold, source, and boundary alternatives.

## What the small disk means

Write the complete normalized field as

\[
Q=H/\mathcal A=f_N+r_N,\qquad
f_N=(G_N-\widehat C_N^{\rm an})/\mathcal A,
\qquad J_v=(v,-v_x/\omega),\quad \omega=\theta_x\ne0.
\]

Here the symmetric normalizer \(\mathcal A\) is nonvanishing and is distinct
from the positive arithmetic carrier. The first jet is the value and
rescaled spatial derivative at a point. The disk is in this two-dimensional
value–slope plane, not in the plane of possible zero locations.

The complete endpoint enclosure has the form
\(\|J_{r_N}(t,x)\|\le\varepsilon(t,x)\). At a hypothetical real collision,

\[
H=H_x=0\quad\Longleftrightarrow\quad Q=Q_x=0,
\qquad J_{f_N}=-J_{r_N},
\qquad \|J_{f_N}\|\le\varepsilon.
\]

The last implication is conditional on a collision. It does not say that
the approximant jet is small everywhere. Equivalently, the true jet lies
in \(B(J_{f_N},\varepsilon)\), so

\[
\|J_Q\|\ge\|J_{f_N}\|-\varepsilon.
\]

A proved lower bound \(\|J_{f_N}\|>\varepsilon\) excludes a collision.
Failure of that sufficient inequality is inconclusive. Even a zero retained
jet can be displaced from the origin by its residual. For illustration,
\(f(x)=x^2\), \(r(x)=\delta\), and \(Q=x^2+\delta\) have zero retained
jet at \(x=0\), but a double zero of \(Q\) there only when \(\delta=0\).
This elementary example illustrates the logic, not the theta source.

Thus forbidding every entry into the disk may be stronger than necessary.
The exact forbidden configuration is the joint equality
\(J_{f_N}=-J_{r_N}\). A directional or correlated residual estimate could
in principle exclude it even when a separate norm estimate cannot.

The endpoint error and the ordinary residual prefix-integral error have
different contracts. Their sizes cannot be substituted for one another.
The [uniform-results section][uniform] and [matched comparison][comparison]
retain that distinction. In the comparison box, paid approximant variation
is about 1.0051 while the direct residual allowance is below
\(1.341\times10^{-7}\). These are bounds, not observed actual errors.
Reducing the latter barely changes the dominant variation payment; the box
already has positive separation, while broad coverage remains open.

## Why the remaining problem is arithmetic

On the real axis, the retained reflected scalar has the form

\[
f_N=2\sum_{n\le N}w_n\cos\phi_n-c_N,
\qquad
(f_N)_x=2\sum_{n\le N}
\{(w_n)_x\cos\phi_n-w_n(\phi_n)_x\sin\phi_n\}-(c_N)_x,
\]

where \(c_N=\widehat C_N^{\rm an}/\mathcal A\), and the actual phases are
\(\phi_n=\theta+\tau\log n\), with
\(\tau=(x-t\operatorname{Im}\alpha)/2\) in the source notation.
The common height determines the phases, heat weights, amplitude drift,
normalizer, and cutoff together. Differentiation freezes the cutoff;
crossing corrections have their own accounting.

Positive weights do not prevent cancellation of the signed trigonometric
terms. The value and derivative impose two different cancellation
requirements. A bound on the modulus of an unreflected Dirichlet polynomial
does not automatically control this reflected scalar and its true derivative.

The [predecessor manuscript][predecessor], at `sc:character`, constructs
completely multiplicative unit phase twists whose complete model jet
vanishes. Actual-height realization is not asserted. This defeats a lower
bound valid for all such twists, not a bound for the genuine height-dependent
sum. Approximating finitely many selected phases at another height does not
transfer the construction while holding its weights and cutoff fixed.

Existing mean-square or Gaussian mass estimates also permit isolated
collisions. A quantitative relation between average mass and local variation
would be additional input. An almost-everywhere result may be useful, but
its exceptional set can still contain every candidate collision.

## The contradiction with RH stated explicitly

RH says that every nontrivial zeta zero has real part \(1/2\). Under
\(H_0(z)=\xi(1/2+iz/2)/8\), an off-line zero
\(\beta+i\gamma\) corresponds to the nonreal zero
\(z=2\gamma+i(1-2\beta)\) of \(H_0\).

The standard threshold theorem and the repository's finite-collision
reduction give the chain

\[
\begin{aligned}
\neg\mathrm{RH}
&\Longrightarrow \Lambda>0\\
&\Longrightarrow \exists\,T=\Lambda>0,\ x_*>0:\quad
 H(T,x_*)=H_x(T,x_*)=0,\\
&\hspace{43mm}\text{all zeros of }H_T\text{ are real}.
\end{aligned}
\]

The finite-height step is substantive. Choose nonreal zeros at times
approaching \(\Lambda\) from below. Uniform positive-time confinement
prevents their escape to infinite height, and strip control bounds their
imaginary parts. A limiting zero is real at the threshold. It cannot be
simple, since a simple real zero would continue locally as a real zero,
contradicting the approaching nonreal zeros. Positivity at zero excludes
\(x_*=0\); evenness permits \(x_*>0\). See the predecessor's
`prop:finitecollision`, using [Polymath Theorem 1.5][polymath].

Consequently it suffices to contradict **positive all-real threshold
events**. The broader exclusion of all positive-time real multiple zeros
is also RH-equivalent in this setting, by the local splitting theorem.
Neither route requires simplicity of the zeros at time zero.

There is no known contradiction between an off-line zero and the general
functional equation, conjugation symmetry, or backward heat equation alone.
These structures are compatible with colliding controls. The desired
contradiction must use additional consequences of the genuine theta
arithmetic, or another independently proved property specific enough to
distinguish it.

A particularly strong screen is the predecessor's quartic threshold model.
For \(\delta=t-T\),

\[
P_t(z)=z^4-(2a^2+12\delta)z^2+a^4+4a^2\delta+12\delta^2
\]

solves the backward heat equation and has all zeros real exactly when
\(t\ge T\), with double zeros at \(\pm a\) at \(T\). It saturates the
mirror inequality below. For \(a^2>6T\), it also has
\(P_t(iy)>0\) for all \(t\ge0\). The failed premises are the complete
theta source and its arithmetic approximation contract; it is not claimed
to arise from a positive theta kernel. Thus even threshold real-rootedness,
the heat PDE, and imaginary-axis positivity do not themselves contradict
a positive threshold. See `lj:quartic` in the predecessor.

## Concrete pairs of incompatible statements

Each proposed route needs two assertions about the same object, on the
same domain and with compatible errors. The event side is a known
necessary condition. The arithmetic side below is the missing estimate,
unless a bounded certificate is specifically cited.

### Separation of the retained first jet

**Event side:** \(\|J_{f_N}\|\le\varepsilon\).

**Desired arithmetic side:** \(\|J_{f_N}\|\ge L\) with
\(L>\varepsilon\), or an enclosure for the exact joint sum that excludes
zero. The positive margin is \(L-\varepsilon\).

FFA-01 selects a complete block interaction; FFA-02 estimates it with
genuine common-height data. Expanding the squared jet is not that estimate.
A first milestone could bound one cross-block term or restrict simultaneous
small values on a declared domain. A universal strict lower bound is the
full target in another form, and a uniform positive constant over an
unbounded family must not be assumed.

### The threshold fourth-derivative sign

**Event side:** at an all-real ordinary double event,

\[
2H_3^2-3H_2H_4-9H_2^2/x_*^2\ge0.
\]

For normalized derivatives \(q_j=\partial_x^jQ\), let
\(b=\mathcal A_x/\mathcal A\),
\(\gamma=18b_x+9/x_*^2\), and

\[
\mathscr L(q)=2q_3^2-3q_2q_4-\gamma q_2^2.
\]

At the collision, the same necessary condition is \(\mathscr L(q)\ge0\).
The normalization terms cannot be dropped.

**Desired arithmetic side:** using a specified approximant with derivatives
\(f_j\) and complete errors \(|q_j-f_j|\le\delta_j\), prove

\[
\mathscr L(f)+\Delta(f,\delta)<0,
\]

where a valid product-error allowance is

\[
\begin{aligned}
\Delta={}&4|f_3|\delta_3+2\delta_3^2
+3|f_2|\delta_4+3|f_4|\delta_2+3\delta_2\delta_4\\
&+|\gamma|(2|f_2|\delta_2+\delta_2^2).
\end{aligned}
\]

This implies \(\mathscr L(q)<0\), the explicit contradiction. The
predecessor already derives this algebra and a measured conditional test
at `lj:paidtest`. New work must prove the arithmetic inequality, possibly
conditioned on the necessary small first jet. Substituting the current
corrected approximant requires its own complete higher-derivative errors;
older errors cannot simply be assigned to it.

At the quartic control, \(P_2=8a^2\), \(P_3=24a\), and \(P_4=24\), so
\(2P_3^2-3P_2P_4=576a^2=9P_2^2/a^2\). This analytic screen shows why a
strict opposite sign cannot follow from the generic threshold hypotheses.
At exact multiplicity three the displayed condition is automatically
satisfied; at multiplicity at least four it becomes \(0\ge0\). Higher
multiplicities therefore need their appropriate deflated higher-jet
condition and its own errors, as already discussed in the predecessor.

### Incompatibility with complete source reflection

**Genuine-source side:** the specified normalized theta reflection defect
is zero, together with the complete coefficient and dilation constraints.

**Desired event consequence:** the required physical cancellation forces
a strictly positive defect, violates one of those constraints, or has a
signed observation outside their quantitatively permitted range.

The source class, defect norm, observation, cutoff, and measurement growth
must be fixed first. Exact uniqueness alone does not prove this implication.
An intermediate theorem could quantify the number of constraints or the
conditioning cost required at height \(x\), even before it gives exclusion.
This is the higher-risk FFA-04 alternative. Fixed finite measurement controls
do not rule out every growing hierarchy or every use of complete modular
information.

### Boundary winding incompatible with an interior event

This is an existing alternative that can avoid estimating the smallest
interior jet. For the physical map \(J=(H,H_x)\), orient spacetime by
\(dt\wedge dx\). On a bounded domain \(D\) with nonzero boundary jet,
the [spacetime index result][winding] gives

\[
\operatorname{wind}_{\partial D}(H+iH_x)
=-\sum_{(T,x)\in D:\,H=H_x=0}\left\lfloor m(T,x)/2\right\rfloor.
\]

**Event side:** an interior collision forces winding at most \(-1\).

**Desired arithmetic side:** prove boundary nonvanishing and winding zero;
equivalently, a validated lower bound strictly greater than \(-1\) suffices
once the displayed integer/sign law applies. Boundary approximation errors
must preserve a nonzero homotopy on every segment.

This handles finite multiplicities together and may require no interior
energy floor. It relocates the arithmetic estimate to the boundary; it does
not remove it. The existing GEO-T1 pilot lost its matched cost comparison
on an already covered box, as [summary 13][laws] records. Another attempt
needs a different domain, new boundary information, or an acquisition
advantage. An exhaustive zero-winding assertion is RH-equivalent, not a
new weaker theorem.

### Collision divergence incompatible with arithmetic boundedness

For the stationary predecessor branch appropriate to multiplicity
\(m=2r+j\), \(j\in\{0,1\}\), the existing local law is

\[
\mathcal L_j/E=-r/(T-t)+O(1),\qquad
E=H^2+H_x^2,\quad
\mathcal L_j=(\partial_x^{j+1}H)^2-
(\partial_x^jH)(\partial_x^{j+2}H).
\]

**Event side:** the ratio tends to \(-\infty\) as \(t\uparrow T\).

**Desired arithmetic side:** an independently proved lower bound that
remains finite on that branch near the positive-time event, or a bound
with rigorously slower allowed divergence. See [summary 13][laws] and
the [earlier priority note][priorities] for its precise scope.

An absolute tail bound or carrier-relative estimate does not become a
bound relative to the vanishing physical energy. The required transfer is
the main difficulty. This is an existing contradiction target; repeating
the local pole law is not progress toward the arithmetic bound.

## Proposed additions to the estimating plan

### Analyze what simultaneous cancellation forces

Condition on the first-jet tolerances supplied by the endpoint theorem.
Seek a further quantitative consequence for a particular block correlation,
logarithmic moment, higher jet, or required source constraint. The new
consequence must restrict an additional observable or parameter range;
rewriting the two smallness equations is insufficient.

This approach can target a restricted event class rather than demanding
global separation immediately. Its central question is whether a putative
event forces two independently controlled observations to disagree. It is
a natural connection between FFA-02 and FFA-03.

### Retain the joint direction of the approximation and residual

Replace independent balls, where justified by new information, by an
enclosure for the jointly admissible pairs \((J_{f_N},J_{r_N})\).
Collision requires intersection with
\(\{(u,v):u+v=0\}\). A proved empty intersection can allow the retained
jet to enter its old disk. The enclosing set must come from independent
arithmetic or analytic estimates, not from defining admissibility to exclude
collisions.

The first useful output would be a joint estimate that excludes cancellation
on a specified domain where the separate norm bounds do not. Coordinate
rotations or a different presentation of the same ball do not provide this
gain. The [matched comparison][comparison] leaves stronger correlated
information outside its scoped negative result.

### Use computation to identify the restrictive observation

A bounded diagnostic can locate the most cancellation-prone retained jets
and record their complete block contributions, higher derivatives, signed
residual information, and proximity to cutoff changes. Compare the genuine
data with suitable phase relaxations and source controls. Its purpose is
to select an estimate and to falsify overly broad mechanisms.

Before any campaign, specify the domain, tolerances, observable, and what
outcome would change the choice of mechanism. Favorable samples are not
evidence for a universal RH-equivalent claim. Almost-everywhere mass or
rarity alone cannot eliminate isolated candidate events.

## A precise statement for each proposed contradiction

Before estimating, record the following together:

1. **Hypothetical witness.** Specify the threshold or arbitrary-event class,
   multiplicity, time and height range, and source normalization. Explain
   why failure of RH supplies such a witness, or state that only a restricted
   class is being addressed.
2. **Forced statement.** Write the exact inequality, equality, integer
   index, or rate forced by that witness, with a source or proof.
3. **Competing statement.** Write the independently sought arithmetic bound
   on the same object, including a strict margin where needed.
4. **Available information.** Identify the complete arithmetic input and
   explain why it is stronger than the premises shared by the nearest
   colliding control. Do not assume a lower margin to prove that margin.
5. **Transfer and scope.** Give the total error allowance, dependence on
   time and height, treatment of cutoff changes and higher multiplicities,
   and the remaining domains outside the proposed result.
6. **Useful first outcome.** Name a quantitative intermediate gain or a
   scoped obstruction that would justify the investigation even if the
   contradiction does not close.

The comparison can be summarized as a witness-derived permitted set and an
arithmetically derived permitted set. A contradiction means they are
disjoint after all errors. Drawing the two sets is organizational; proving
their separation is the research.

## Control screen and global coverage

The following is an analytic premise screen for the proposals, not a fresh
numerical validation of a consumer. A future quantitative consumer must run
the relevant source-specific controls at their event boxes or signed
witnesses with their own error contracts. Analytic existence controls must
not be assigned invented effective event locations.

| Control | What survives | What an arithmetic argument must distinguish |
| --- | --- | --- |
| Weighted-square and finite-prime orbit sources | Positive coefficients or carriers and specified finite arithmetic tests | Full normalized reflection or unchanged complete coefficients fails |
| Reflected smooth and positive-primitive sources | Reflection and substantial positivity or endpoint information | The normalized theta square expansion and its arithmetic contract are absent |
| Euler-factor modifications | Many symmetries and explicit arithmetic structure | Coefficients, level, or lattice change; unchanged theta constants cannot be imported |
| Complete multiplicative phase twists | Multiplicativity, retained model weights, and local frequencies in the relaxed construction | Coupling to one genuine height with its simultaneous cutoff and weights is not established |
| Quartic threshold model | Heat equation, evenness, a positive all-real threshold, mirror equality, and optionally imaginary-axis positivity | Complete theta source, infinite zero structure, and arithmetic approximation contract are absent |

An exclusion on one sector or for ordinary double events does not yet
contradict RH failure: the hypothetical witness might lie outside it or
have higher multiplicity. Global closure needs a proved cover of all
possible witnesses, or a theorem localizing every hypothetical witness to
the treated class. An arbitrarily small positive threshold cannot be
discarded; there need be no uniform positive jet margin as \(t\downarrow0\).

The starting UAR sector is
\(0<t\le1/20\), \(1\le t\log(x/(4\pi))\le2\).
It does not contain all possible threshold events. The existing real bridge
and complex barrier obligations in [Review 19][review19] remain separate.
For classification, a universal no-collision or zero-winding formulation is
RH-equivalent under the cited reductions; a restricted estimate is judged
by its domain and quantitative gain. A merely reformulated target is not a
new theorem. Negative outcomes retain their proved source class and
quantifiers.

## Current discussion and next questions

The proposed priority remains a genuine retained-sum estimate, with explicit
conditional cancellation analysis and a possible threshold-sign consumer.
Correlated residual information is a distinct possible addition. Boundary
winding and the collision-rate target are existing alternatives to compare
when a specific arithmetic observation makes one of them more accessible.
This note does not activate a computation campaign or revise the program's
task statuses.

The next useful choices are the weakest event class whose exclusion would
still yield a meaningful result; the observable for which the event forces
the sharpest restriction; and the arithmetic information most likely to
bound that observable independently. Each choice should identify one of
the concrete incompatible pairs above, its nearest control, and its missing
estimate.

### Discussion record

- **19 October 2026:** Catalogued the first discussion of the small-disk
  implication, simultaneous arithmetic cancellation, recommended program
  tasks, and three possible augmentations.
- **19 October 2026:** Added the explicit RH-failure-to-threshold-event
  chain, the quartic threshold screen, five concrete contradiction targets,
  and a common format for stating their missing arithmetic estimates.

- **19 October 2026:** Created [Investigation 13][investigation13] with five
  standard route folders and initial research notes. The routes are
  retained first-jet separation, threshold higher-jet signs, complete
  source reflection, boundary winding, and collision divergence.
  Correlated residual information is included within the first route.
  A consolidated research program and progress file are deferred until
  the individual routes have been explored more deeply. This is research
  setup, not a new theorem or numerical run.

At Edward's request on 19 October 2026, the affiliated conversation moved
to its sole [brainstorm history][chat], preserving number 11, its original
identity, and all public messages. The [relocation receipt][relocation]
records the verified transfer. Future additions to this note should preserve its
explanatory role and distinguish proposals, proved-in-source reductions,
numerical observations, and reviewed results.

[review19]: ../../11_arithmetic_collision_rigidity/reviews/19_FIXED_FUNCTION_PROGRAM_AND_AMBITIOUS_NEXT_STEPS_REVIEW_ASTRA_20261019.md
[program]: ../../research-overview/03_FIXED_FUNCTION_ARITHMETIC_RESEARCH_PROGRAM_20261019.md
[uniform]: ../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/13_uniform_coherent_edge.tex
[comparison]: ../../11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[predecessor]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[laws]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[classification]: ../../../../avoid/01_restating_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[priorities]: 02_FIXED_CHARACTER_GOALS_AND_ARITHMETIC_COLLISION_RESEARCH_CODEX_20261018.md
[winding]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1.Thm5
[chat]: ../chat-histories/0011_2026-10-20T01-37-24Z_explain-arithmetic-rigidity-obstacle.json

[investigation13]: ../../13_contradiction_analysis/README.md

[relocation]: ../CHAT_HISTORY_RELOCATION_20261019.json
