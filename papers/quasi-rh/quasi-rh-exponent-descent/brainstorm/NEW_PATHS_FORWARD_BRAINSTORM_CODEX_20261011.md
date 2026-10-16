# Assessment of proposed paths from quasi RH to RH

11 October 2026. Prepared for Edward Baker. Model: GPT-6 (Codex). Reasoning effort: the active setting is not exposed in this session and is not inferred. Written with substantial LLM assistance, including parallel internal checks; these are not independent mathematical validation. This is a research brainstorm, with elementary calculations distinguished from proposed investigations. It establishes no new zero-free strip or bound for the de Bruijn–Newman constant.

Companion to [Claude’s brainstorm](NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md), read against repository commit `a01f8f2a21657170ec5bf6138f7b884eecea53ac`. The recommendations below preserve the decision to stop open-ended work on the present heat and moment reductions. They identify a few bounded tasks whose outputs would remain useful even if they produce no descent.

My preferred order is: **audit one complete branch of an imported argument; write the exact moment ledger for the actual families; benchmark the corrected heat approximation on difficult certificate cells.** A matched function-field experiment comes after the ledger. Three further tests concern the density of the counterkernel, quantitative persistence of a collision, and a correction to the Weil wildcard. None presently supplies an RH mechanism.

## 1 Corrections that affect the choice of direction

Claude’s central recommendation is sound: another reformulation is not progress unless it supplies an estimate that was previously missing. The latest project 17 work has produced reusable approximation and certification machinery, while its global coverage problem remains open. Several stronger statements in the brainstorm should nevertheless be narrowed.

**Equivalence is not the same as circular proof.** An independently proved sufficient moment estimate can legitimately control an individual coherent row. Its coherent-row restriction implying the desired conclusion reveals how strong the estimate is; that observation alone does not invalidate it. The failure is claiming that a reduction has proved the estimate, assuming the conclusion in its proof, or asking for an estimate contradicted by an exact lower bound. The same distinction applies to sign criteria equivalent to zero exclusion. They may be useful formulations, but their source estimates must do the work.

**The counterkernel only rules out arguments using the properties it satisfies.** It cannot satisfy the two sufficient stationary signs on a neighborhood containing its positive-time collision and the required predecessor branches. R1 should separate generic properties such as positivity and decay, algebraic identities valid for many kernels, and inequalities that actually exclude collisions. Also, logarithmically growing zero density is not automatically an escape from this counterexample; see Section 6.

**A weaker direct consequence does not exhaust a hypothesis.** The strip-to-heat estimates in Claude’s table give upper bounds worse than the published `0.2` bound. That makes this particular use of quasi-RH unproductive. It does not prove that all arithmetic information carried by quasi-RH is useless to every heat argument. Likewise, zero density equal to zero differs qualitatively from a small positive power of height when the issue is one exceptional zero. This observation supplies no new bridge, but it prevents discarding one by an invalid comparison.

**R5 needs a separate theorem and precise quantifiers.** The cited finite RH verification and a barrier excluding zeros above a positive imaginary height do not, by themselves, establish that every zero in the whole stated `(t,x)` box is real and simple. In particular, a barrier above `y=0.2` does not exclude a complex pair below it. The available certificate theorems should be used in their actual domains. This does not rescue the already unsuccessful local probes: their separation margins and the absence of a global coverage estimate are sufficient reasons to stop those probes.

**D7 cannot be a theorem that every heat method fails.** The local ambiguity result concerns the specified approximation tube and heat information. A no-go theorem must name those inputs. Quantitative regularity can convert a point event into a small-value region of positive measure, so the measure-zero argument alone is insufficient. Section 7 makes both the opportunity and its severe missing estimate explicit.

The relevant local references are [the heat ambiguity note](../newman_collisions/17_enlarged_state_transport/notes/18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md), [the bounded-loss analysis](../newman_collisions/17_enlarged_state_transport/notes/17_MULTIPLICITY_BUDGETS_AND_HOLDER_LOSS_CRITERION_20261010.md), and [the corrected cutoff and physical-jet interface](../newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md).

## 2 D1 and D6 Audit the source of the arithmetic saving

These are the highest-value diagnostic proposals, with a more specific target than searching for an absent family-to-individual step.

The October 5 source fixes a target character before applying its mean square. Section 3 uses prime sixth-power replication, deletion estimates, and Mellin detection to obtain individual control from Proposition 3.1. The place to investigate is therefore the proof of the saving, especially the cube-removal and two-Poisson recurrence. See the [October 5 source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).

The September 30 source organizes its conclusion through Proposition 2.1 and common-signal continuation; the principal row carries the reciprocal of the target L-function. D6 also needs a hypothesis check: the positive-prime-slot version of Lemma 18.1 at `κ=3/4` already assumes `β*≤(1+κ)/2=7/8`. It is not an independent test of that same boundary. The zero-slot and `κ=1` cases have different hypothesis status. See the [September 30 source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).

The repository has already examined more than local algebra. Its [upstream audit](../../quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md) and [dependency ledger](../../quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md) address reflection, primitive Poisson transforms, sieve inputs, and continuation. Start there to identify the global assertions still imported.

**First bounded task.** Make the one-page dependency map, then audit one complete nonempty cube-tail branch of the October 5 argument. Fix one admissible profile and follow it through both Poisson transforms and back into the asserted energy class. Record:

- Support, coprimality masks, primitive-character restrictions, and fixed-character dependence.
- Every normalization and coefficient norm, including diagonal and coherent contributions.
- The derivative orders and weight classes consumed by each transfer.
- The parameter that strictly decreases and the base case that terminates the recurrence.
- Which constants may depend on the fixed target and which positive exponent margins must remain uniform.

The deliverable is a closed chain for that branch, or a located gap with a minimal configuration showing why it matters. One successful branch does not validate the entire external theorem. One failed proof step is not automatically a counterexample to its conclusion.

**D6 should test admissible consequences.** For each imported lemma, print its assumptions beside the proposed corollary. A finite polynomial moment does not automatically become a full central L-function fourth moment. Nor can a conductor-aspect Hecke-family density bound be compared directly with a height-aspect zeta bound. Ordinary Markov bounds give an exceptional-set size determined by the moment and the chosen threshold; there is no universal “all but `T^ε`” output.

An unexpectedly strong consequence is a reason to examine the proof, not a disproof. A weak consequence does not show that the same inputs cannot have a stronger consequence elsewhere. Replace D6’s strength-based kill criterion with a failed hypothesis, normalization, or inference.

**Continue if** the branch closes and exposes a saving with a clearly identified origin. **Stop expanding the downstream program if** it relies on an unproved transfer or returns to the desired estimate without a decreasing parameter. This is a source audit, not a new conditional descent paper.

## 3 D2 and D5 Replace the universal target with an exact moment ledger

D5’s proposed common bound is not merely difficult in a standard interpretation. It is false below the exact diagonal.

Let `q` be prime, `N<q`, and `a_n=μ(n)w(n)`. Character orthogonality gives

\[
\sum_{\chi\bmod q}\left|\sum_{n\le N}a_n\chi(n)\right|^2
 = (q-1)\sum_{n\le N}|a_n|^2.
\]

There are no distinct congruent integers in this range. Removing the principal character gives

\[
\sum_{\chi\ne\chi_0}\left|\sum_{n\le N}a_n\chi(n)\right|^2
 = (q-1)\sum|a_n|^2-\left|\sum a_n\right|^2
 \ge (q-1-N)\sum|a_n|^2.
\]

For `w=1`, squarefree density makes this of order `qN`. Thus, with `N` of order `q^h`, fixed `0<h<1`, the asserted saving `q^{1+h-c}`, `c>0`, is impossible for this family, including its primitive nonprincipal characters. By contrast, `w(n)=n^{-1/2}` changes the coefficient energy to order `log N`. A family over many moduli changes its cardinality again. Neither can be hidden inside the same exponent formula.

This calculation does not rule out a saving for an arbitrary sparse family: its character kernel need not have the full-family orthogonality above. It does rule out treating the displayed normal form as the common open problem before specifying the family and weights.

**The useful replacement is a family-specific ledger.** For every actual lane, record

\[
\mathcal M=\sum_r\omega_r|A_r|^2,
\qquad
K(m,n)=\sum_r\omega_r\chi_r(n)\overline{\chi_r(m)},
\qquad \omega_r\ge0.
\]

Then expand the moment using its actual coefficients and masks. List the exact diagonal, exceptional congruences, coherent mass, and remaining signed covariance. State whether the target concerns the whole moment, a centered moment, or an off-diagonal remainder. A subtraction that is convenient algebraically cannot be ignored when returning to an upper bound on a positive moment.

On coherent rows `r∈C`, suppose a proved mask estimate gives `A_r=A_0-E_r`, `|E_r|≤B_r`. Then

\[
\mathcal M\ge
\sum_{r\in C}\omega_r\bigl(|A_0|-B_r\bigr)_+^2.
\]

For uniform `B_r≤B` and `W_C=Σ_Cω_r>0`, this implies

\[
|A_0|\le B+\sqrt{\mathcal M/W_C}.
\]

That is the correct diagnostic output. Classify a proposed estimate as impossible, equivalent on the restricted rows, stronger than the restricted estimate, or supplied by an independent theorem. Do not have the checker label every sufficient estimate a tautology. The [short-family refinement](../short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md) already makes a coherent-row equivalence explicit; the full-family hypothesis can still be strictly stronger.

D2’s random models are useful stress tests with declared limits. Randomizing Möbius signs destroys `μ*1=δ`, so failure for a random model does not refute a theorem using the exact inverse identity. Conversely, random square-root cancellation does not prove cancellation for Möbius. A counterkernel is decisive only when it satisfies every hypothesis of the proposed implication.

**First bounded task.** Fill the ledger for one short sextic family and one quadratic lift, using their existing definitions. A small checker may verify declared exponent and mask arithmetic after the ledger is correct. It should not purport to decide equivalence of arbitrary hypotheses.

**Continue if** the ledger leaves a feasible signed covariance estimate with a plausible independent source. **Stop that target if** it is below an exact lower bound, or if its only proposed proof assumes its coherent-row conclusion. A literature search should use the corrected family and normalization; a broad claim that no saving exists for any Möbius-weighted family is unwarranted.

## 4 D3 Use function fields to test exact structure

This is worthwhile after the family ledger, but the asserted availability of the required moments is too broad. Keating–Rudnick’s variance results use specified families and large `q` with degrees fixed; they do not supply arbitrary sparse sextic families or uniformity in growing degree. See [their paper, Sections 6–8](https://arxiv.org/html/1504.03444v2). Function-field Möbius moment asymptotics also have positive diagonal-size main terms; see [Gorodetsky, Section 5](https://doi.org/10.1007/s00605-024-01957-z).

There is an exact preliminary test that needs no equidistribution theorem. Let `P∈F_q[T]` be irreducible of degree `d`, and let `2≤n<d`. All polynomial sums below are over monic polynomials. Orthogonality and the squarefree count give

\[
\sum_{\chi\bmod P}
\left|\sum_{\deg f=n}\mu(f)\chi(f)\right|^2
 = (q^d-1)(q^n-q^{n-1}).
\]

Moreover,

\[
\sum_{\deg f=n}\mu(f)=0\quad(n\ge2),
\qquad
1/\zeta_{\mathbb F_q[T]}(u)=1-qu.
\]

The principal row therefore contributes zero here. With `Q=q^d`, `N=q^n`, the full moment has the same diagonal obstruction to D5’s power saving, in a setting where the relevant RH statements are proved. An untwisted coherent-row experiment is also degenerate: its target signal already vanishes. Use a fixed nonprincipal base twist or another nontrivial base L-function.

Normalized degree errors generally involve sums of `e^{inθ_j}` and are quasiperiodic; there is no general period `log q`. Vertical periodicity in the complex variable `s`, arising from `q^{-s}`, is a different statement. A test of an edge-mode recurrence should use the actual Frobenius eigenvalues and its exact degree shifts.

**First bounded task.** Match one integer-family ledger with a fully specified polynomial family: field, base twist, modulus degree, row degree, masks, and limiting regime. Compute its coherent mass and covariance kernel exactly for small instances, then identify the theorem that would control the same objects asymptotically.

**Continue if** this reveals a cancellation mechanism beyond the known diagonal and coherent contributions, with a credible integer analogue. **Stop the analogy if** the relevant theorem controls a different family or limit. A counterexample transfers back only when the claimed argument and its hypotheses transfer; failure of an arbitrary analogue is not a general impossibility theorem over the integers.

## 5 D4 Benchmark the corrected approximation before a bound campaign

This remains the clearest candidate for a concrete analytical or computational deliverable. Its target and comparison set should be updated.

The published baseline `Λ≤0.2` follows from [Platt–Trudgian](https://arxiv.org/html/2004.09765). Primary materials available on 11 October 2026 also contain newer claims: [Gomila’s package](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit) states `Λ≤0.1787854` and says it is not yet peer reviewed; [Gordon’s version 1.0.0](https://github.com/stefangordon/dbn-upper-bound/blob/v1.0.0/README.md) states a bound below `0.158`, also without external peer review and with analytic assumptions retained in its partial Lean theorem; [Planat’s version 2](https://arxiv.org/abs/2609.37164v2) proposes `0.1779532546…` with an audit-relative dependence on its base package. These are comparison and audit targets, not independently validated bounds in this note. Their existence makes “improve 0.2” an incomplete description of the competitive task.

The [Polymath criterion](https://arxiv.org/html/1904.12438v2#S1) has objective

\[
\Lambda\le t_0+\frac{y_0^2}{2},
\]

with hypotheses covering a verified initial region, an intermediate-time barrier, and final-time nonvanishing above `y_0`. Proving that every high zero is already real at `t_0` is a stronger demand than this criterion requires. Optimize the actual objective and every hypothesis needed to certify it. The estimate `t≈5/log X` is a heuristic, not a proved ceiling for all methods at that verification height.

The latest project 17 interface gives a specific tool to compare. Write its corrected approximant as

\[
G_N(t,z)-C_N(t,X)e^{-\pi(z-X)/8},
\]

with the complete normalized disk residual from Notes 20–22. The smaller residual belongs to this corrected center; it cannot be used as a smaller error around the old `G_N`. Physical derivative corrections and normalization must move with it. At isolated complex points, the printed correction can be evaluated directly; a holomorphic surrogate is needed when the argument actually uses a common analytic disk and Cauchy estimates.

[Note 20](../newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md) and [Note 22](../newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md) also impose domain and cutoff contracts. Adjacent natural cutoffs are covered by the matching result; an arbitrary frozen cutoff still requires its add/remove payment. A foreign certificate using larger imaginary heights is not automatically inside the existing source domain. The notes state `0<t≤1/2`; barrier cells at `t=0` require their own certificate or a justified uniform limiting extension.

**First bounded task.** Select 20–50 difficult cells from a pinned existing barrier or final-time certificate. On the same cells and precision, compare the original approximation, the pointwise corrected value, and the corrected holomorphic interface where applicable. Report separately:

- The actual finite-sum margin and the displacement caused by the correction.
- The source error, interval overestimation, derivative allowance, and cutoff payment.
- Runtime and precision needed to obtain the final positive margin.
- The admissible `(x,y,t)` domain and the remaining analytic tail obligation.

Begin with a reproducible replay of the selected original cells. Existing real-axis timing probes are not a cost model for the full complex barrier, and no bounded scan proves the unbounded tail.

**Continue if** the correction resolves a real bottleneck: previously undecidable cells, a justified parameter gain, or a material reduction in certification cost. **Stop a record-bound campaign if** finite-sum cancellation or the tail dominates so that the smaller error changes neither feasibility nor cost. An absolute gain of `0.01` is an arbitrary threshold; a smaller verified improvement or a reusable faster evaluator can be worthwhile.

A publishable outcome could therefore be a carefully scoped corrected evaluator and benchmark, even without a new bound. Its novelty would need comparison with existing correction formulas and certificate software. Merely rediscovering the correction term is not sufficient.

## 6 Additional test Identify what the counterkernel actually lacks

The suggestion that logarithmic zero density distinguishes the theta kernel from the countermodel deserves an immediate check.

At its collision time the [existing countermodel](../newman_collisions/01_analytic_gaussian/notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md) has

\[
J_T(z)=2K_{iz}(1)\cos^2(bz),\qquad b>0.
\]

The positive order-zeros of `K_{iν}(1)` satisfy `ν_n∼πn/log n`; see [Krynytskyi–Rovenchak, Section 3](https://arxiv.org/pdf/2103.01732). Consequently their counting function is asymptotic to `R log R/π`. The cosine factor adds only `O(R)` zeros, counting multiplicity. Rescaling the argument to `z/4` makes the leading positive-zero count `R log R/(4π)`, the leading coefficient in the project’s theta normalization.

This is a leading-density comparison at the displayed collision time. It does not establish the full Riemann–von Mangoldt formula, a matching remainder, simplicity, or uniformity over heat times. It does show that merely demanding a mean density growing like `log x` is too weak to eliminate the model.

**Bounded task.** Make a feature table for the counterkernel: leading and linear counting terms, available remainder, multiplicities, scaling, and time dependence. Compare only features that a proposed proof actually uses. The useful question is which explicitly stated arithmetic or quantitative spectral condition excludes this countermodel.

**Continue if** a condition both excludes the model and has an independent source for the theta kernel. **Stop adding generic conditions if** the model already has them. An Euler product or an exact convolution identity offers a different kind of information; calling a growth condition “arithmetic” does not make it so.

## 7 Additional test Quantify the persistence required of small value estimates

D7’s point-event objection can be made into a precise missing-estimate test. This is low priority unless an arithmetic source for the required estimate can be identified.

On a compact real `(t,x)` patch, choose fixed coordinate scales and a positive normalization `A`, and consider the physical joint jet

\[
J(t,x)=\bigl(H_t(x)/A(t,x),\ \partial_xH_t(x)/A(t,x)\bigr).
\]

Suppose `J` is `K`-Lipschitz in those scaled coordinates. If an interior point `p_0` is a collision, then `J(p_0)=0`, so the sublevel set `||J||≤ε` contains the disk of radius `ε/K` about `p_0`, provided that disk lies in the patch. Its area is at least

\[
\pi\varepsilon^2/K^2.
\]

Thus an actual-source upper bound smaller than this forced area would exclude the collision. A boundary point requires a one-sided version with the corresponding geometric constant. This elementary argument explains why measure estimates plus quantitative regularity can sometimes exclude isolated events.

It also exposes the difficulty. At a nondegenerate double zero, the heat equation `∂_tH=-∂_x^2H` gives, in unscaled coordinates,

\[
\det D(H,\partial_xH)=-(\partial_x^2H)^2\ne0.
\]

Such a zero has a natural sublevel area of order `ε²`. A generic estimate of that same order need not contradict it. One would need a sufficiently strong constant, or an arithmetic improvement in order, with uniform control of `K`. Existing large-value or average cancellation estimates do not automatically supply such a two-variable small-value theorem.

**Bounded task.** On one specified family of patches, compute the Lipschitz budget and forced area at the residual scale relevant to the corrected interface. Compare them with one genuinely applicable source estimate, if available. Account for approximation error in both jet components before passing between the polynomial and the physical jet.

**Stop if** no source estimate is available, only an `ε²` estimate with a noncontradictory constant is obtained, or the uniform constants destroy the comparison. Do not generate another hierarchy of conditional criteria. The possible advance would be the source estimate itself; this continuity observation is only a way to measure what it must accomplish.

## 8 Additional test Cost a finite support Weil detector

The Weil wildcard has a correct caution but an incorrect cancellation argument. A single translated packet has cancelling exponential factors; two packets can make different ends dominate the two transforms.

Use the centered transform

\[
G(s)=\int_{\mathbb R}g(u)e^{(s-1/2)u}\,du.
\]

Let a hypothetical off-line zero be `ρ=1/2+a+iγ`, `a>0`. Choose a nonzero, even, nonnegative real `φ∈C_c^∞(R)`, write `Φ(a)=∫φ(v)e^{av}dv`, and set

\[
g(u)=e^{-i\gamma u}\bigl(\varphi(u-L/2)-\varphi(u+L/2)\bigr).
\]

Direct substitution, using `Φ(-a)=Φ(a)`, gives

\[
G(\rho)=2\Phi(a)\sinh(aL/2),\qquad
G(1-\overline\rho)=-2\Phi(a)\sinh(aL/2),
\]

and therefore

\[
G(\rho)\overline{G(1-\overline\rho)}
=-4\Phi(a)^2\sinh^2(aL/2).
\]

The individual zero contribution can indeed grow exponentially and negatively with separation. For disjoint packets, `||g||₂²=2||φ||₂²` is independent of `L`, so this is not an artifact of scaling the test norm. It does not prove negativity of the full Weil functional: contributions from other zeros, the pole and archimedean terms, and the prime side all remain. If `φ` is supported in `[-w,w]`, the test spans `L+2w`; the associated finite prime sum consequently reaches a scale of order `exp(L+2w)`. An absolute estimate on the outer prime terms can cost order `exp(L/2)` for fixed packet width. The explicit main and pole terms must therefore be included before claiming a useful gain.

**Bounded task.** Use the existing [finite-horizon Weil manuscript](../../../weil-positivity/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex), which already allows complex tests, to cost this two-packet family for a declared detection target `a≥a_min>0`, `|γ|≤T`. Compare its quadratic form and numerical conditioning with the existing finite-horizon basis. Translation invariance permits shifting its support into the prescribed interval.

**Continue if** the test improves a certified finite detection or exclusion problem at a useful cost. **Stop as a global descent proposal if** its horizon depends uncontrollably on `a_min` or `T`. Quasi-RH gives an upper bound on `a`, not the positive lower bound needed for a uniform detector; arbitrarily small displacements and unbounded heights remain. The calculation repairs the stated obstruction without removing the real one.

I would leave the Li and Nyman–Beurling wildcards parked unless a comparable, independently controlled detection cost is supplied. Rewriting the unknown distance from the critical line as an unknown positivity index or approximation rate does not improve the quantifiers. A reversal of the Rodgers–Tao strategy would likewise need a new rigidity statement forced by a positive collision time; the persistence test alone does not provide one.

## 9 Recommended deliverables and decision points

| Order | Deliverable | What would justify further work |
| --- | --- | --- |
| 1 | Dependency map and one complete imported recurrence branch | A verified saving with explicit assumptions and a terminating transfer |
| 2 | Exact moment ledgers for the actual sextic and quadratic families | A feasible covariance target beyond the known diagonal and coherent signal |
| 3 | Corrected-interface benchmark on pinned difficult certificate cells | Improved margins, parameters, or cost under the complete certificate contracts |
| 4 | One matched function-field experiment | A structural mechanism with the same hypotheses and a credible integer analogue |
| 5 | Short density and Weil calculations, with the persistence test only if a source is found | A concrete feature or estimate that the existing no-go examples do not already absorb |

The most promising research principle is to require an identifiable source of new information at the next step. For the arithmetic route, that means the estimate inside the imported proof or a genuinely new covariance bound. For the computational heat route, it means a measured gain in a complete certificate. For an RH route, none of the present proposals yet meets that standard. They can still produce useful mathematics by locating the exact obstruction, repairing an overbroad claim, or improving a tool whose success can be independently checked.
