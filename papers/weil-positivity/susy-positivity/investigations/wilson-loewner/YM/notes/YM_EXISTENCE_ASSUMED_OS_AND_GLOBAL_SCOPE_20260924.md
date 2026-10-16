# YM existence under assumed OS positivity: a global research target

Date: 24 September 2026, America/New_York.
Prepared for Edward Baker with LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: not exposed; not inferred.
Status: scope correction and proposed theorem strategy; no existence result is claimed.

## 1. Scope correction

The user retains a Yang–Mills realization as an objective, is interested in proving its existence without constructing it explicitly, and is willing to assume OS positivity. Those preferences govern the next research proposal.

The previous bootstrap note's statement that the direct-form approach “avoids requiring a native causal device or a literal YM realization” described a weaker sufficient route to RH. It should not have been used to remove YM from the intended project. The corrected task is to investigate a global YM realization, allowing nonconstructive arguments and taking OS positivity as a stated hypothesis.

The previous recommendation to progress through several small values of \(L\) is also downgraded. Such cases may falsify an ansatz or check normalization. They should not be the main milestones until an all-support existence mechanism has been identified.

## 2. Two physical objectives remain distinct

**Reflected YM realization of the Weil form.** Find an admissible linear source family in a YM theory such that its OS pairing equals the Weil form. This directly gives positivity under the assumed OS hypothesis.

**Native causal YM realization of the shifted transfer.** Additionally identify physical preparation, evolution, readout, and ordinary energy balance with the prescribed shifted-zeta transfer. This asks for more than the reflected pairing. OS positivity does not by itself identify that particular transfer function, a Loewner-capacity evolution, or a passive source/readout system.

The first objective can remain genuinely YM while leaving the causal objective as an additional question. If the specific causal realization is itself the desired endpoint, it stays in scope and its extra identities must be retained.

## 3. A precise global conditional target

Let \(\omega_{\rm YM}\) be the expectation functional of a specified YM model and let \(\mathcal A_+\) be its chosen admissible half-space observable algebra, with physical reflection \(\Theta\). Assume
\[
\omega_{\rm YM}((\Theta A)A)\ge0,\qquad A\in\mathcal A_+,
\]
including the sector and source-domain interpretation needed for the proposed observables. This is an assumption, not a request to redo the lattice OS proof.

Let \(\mathcal D=C_c^\infty(\mathbb R)\), or use the global pole-neutral subspace \(\mathcal D^0\) if an RH-sufficient restricted realization is the immediate target.

The desired theorem is:

> There exists one continuous linear source map \(J\) into the admissible YM source space or its specified OS completion, compatible with the prescribed arithmetic/source operations, such that
> \[
> Q(f,g)=\omega_{\rm YM}((\Theta Jf)Jg)
> \]
> for every pair \(f,g\) in the chosen global test class.

For a map into the completion, the right side means the induced OS inner product. Proving membership in the allowed completion is part of the realization statement.

Then \(Q[f]\ge0\) immediately follows. On the full or globally RH-sufficient test class, this implies RH conditional on the stated physical hypotheses.

Here \(L\) only bounds the support of a test. The model and source law do not get refitted when \(L\) changes. Localized maps would be restrictions of the same \(J\), not independent constructions for individual intervals.

Continuity should use the smooth-test or appropriate logarithmic-form topology. A bounded map from ordinary \(L^2\) on every input is unnecessarily strong and conflicts with the unbounded logarithmic high-frequency growth. Local support-dependent seminorm bounds are legitimate.

A continuum limit need not be part of the positivity implication if one regulated YM model already admits the global source map. A continuum physical interpretation is a further assertion. Conversely, if a continuum Schwinger functional is used, its existence, domain, and the assumed positivity must be identified as the physical hypotheses.

## 4. What assuming OS does and does not settle

It supplies positivity of every admissible reflected source combination and the corresponding Hilbert quotient/completion. It allows attention to shift from proving positivity of the measure to proving existence and identification of the arithmetic source family.

It does not select the arithmetic kernel. Many different pairings can be positive. It does not produce prime weights, the gamma contact, or a source map. Nor does it automatically make an arbitrary multiplier preserve the OS null space.

The existing finite-slab result is useful because it explicitly identifies a boundary algebra whose multiplication preserves that null space. For a different source family, admissibility must be proved or clearly included in the source-domain hypothesis.

Full reconstruction of a relativistic theory uses further OS conditions, not reflection positivity alone. This is distinct from the elementary positive-pairing implication needed here. [Osterwalder–Schrader, corrected reconstruction framework](https://link.springer.com/article/10.1007/BF01608978).

## 5. Existence without an explicit construction is a legitimate objective

The fact that an existence theorem would imply RH locates the difficult step; it does not invalidate the strategy.

The circular argument to avoid is specific: assume the Weil form positive, form its Hilbert completion, and embed that abstract space into another Hilbert space. This proves no independent arithmetic fact. GNS or a dilation theorem applied to the desired kernel likewise needs the relevant positivity as input.

A YM existence theorem must obtain its extra information from YM dynamics, observable relations, a representation theorem, or a global compatibility argument. It need not calculate the source or all its correlators explicitly.

One should also state what “YM realization” requires. An arbitrary Hilbert-space embedding into a sufficiently large YM Hilbert space does not use the physical observable structure. Requiring the source to lie in a specified loop/defect algebra and to intertwine specified arithmetic operations gives the existence question physical and mathematical content. The intended class may be broad; it simply must be stated.

Existence of an abstract positive Hilbert realization is an RH-equivalent positivity formulation under the usual domain assumptions. Existence in a prescribed genuine YM observable class may be stronger. These should not be called equivalent without an additional theorem.

The categorical “do not spend time” on existence in the older 16 September note is not an appropriate restriction on the user's current objective. Its warning about circular use of abstract representation theorems remains relevant.

## 6. Preferred strategy: characterize the pairing globally

The strongest conceptual route is a representation-and-uniqueness argument:

1. Specify an arithmetic source module and relations, covering all primes and all compact supports.
2. Prove that this module occurs in an admissible YM sector, or that a compatible nonzero source map exists. This step could be nonconstructive.
3. Derive global Ward, loop, Fourier, or intertwining identities for its reflected pairing.
4. Prove those identities and stated normalizations determine a unique continuous Hermitian pairing.
5. Verify, without assuming its sign, that the explicit Weil form satisfies the same identities.

The YM pairing and \(Q\) must then coincide. OS supplies the sign.

The uniqueness class must include Hermitian forms of unknown sign. Uniqueness only among positive forms would not identify \(Q\) unless its positivity were already known.

This does not require a finite-dimensional space of observables. Infinite-dimensional representations can have rigid invariant pairings, but the relevant rigidity and domain assumptions must be proved here. The zeta functional equation alone is not a sufficient characterization for this purpose.

This strategy addresses the user's concern about \(L\): the identity is global before localization. The hard question becomes occurrence and rigidity of an arithmetic module inside YM, rather than persistence of a numerically observed gap.

## 7. Alternative: a moment-extension and compactness theorem

An existence bootstrap could formulate all admissible YM/arithmetic correlations as one infinite moment problem.

At a finite level, retain enough moments to state reflection positivity, holonomy identities, the actual YM dynamical constraints, source compatibility, and selected arithmetic matching conditions. A compactness argument could produce a global solution if:

- the moment variables have bounds giving a suitable compact set;
- the relevant constraints are closed in that topology;
- every finite collection of constraints is simultaneously feasible;
- the limiting functional is shown to belong to the intended YM class;
- the source-domain and continuity requirements survive the limit.

This is a theorem schema, not an existence proof currently in hand. Feasibility for a handful of finite systems is insufficient. The central new result would need to establish feasibility for arbitrary finite collections or supply a global extension property.

Holonomy-algebra representation theory gives a real framework for reconstructing measures on generalized connections from appropriate positive loop data. [Ashtekar–Lewandowski](https://arxiv.org/abs/gr-qc/9311010). Such a measure is not automatically the YM measure; the dynamics and regularity still select the intended theory. Algebraic Wilson-loop reconstruction results are relevant background, with the same distinction between kinematics and dynamics. [Giles](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.24.2160).

Two cautions are material:

1. Moment limits can produce a new positive representation. They do not automatically realize observables inside a prescribed existing YM representation.
2. Weak limits of source vectors can lose norm. For example, an orthonormal sequence converges weakly to zero while its norms remain one. Bounded weak compactness alone does not preserve a desired Gram identity; stronger control or an appropriate moment reconstruction is needed.

If a convex separation argument is used, convexity and closure of the admissible class must be established. Mixing states or adjoining auxiliary sectors can enlarge the class beyond the intended fixed YM realization.

## 8. How the bootstrap's role changes

It becomes an existence/rigidity bootstrap for a YM source sector, rather than merely a machine for lower bounds on \(Q_L\).

Finite calculations can:

- test whether proposed identities are mutually consistent;
- identify a missing Ward or holonomy relation;
- reveal a finite obstruction to a chosen source class;
- help conjecture a global recurrence or extension theorem.

They should not be promoted as evidence that an unrestricted sequence of interval certificates will eventually generalize.

An all-support theorem does not require a uniform strictly positive spectral gap. Exact identities, nonnegative limiting forms, and compatible source maps can remain valid as coercivity margins shrink. Conversely, weakening a gap requirement alone does not supply the missing existence theorem.

The logarithmic source coordinate also needs an interpretation. Physical Euclidean-time evolution, spatial translation, radial scaling, and Loewner capacity obey different laws. The nonconstructive theorem must specify the action it intertwines, even if no explicit source formula is produced.

## 9. Revised next steps

1. **Choose the realization class.** State whether the candidate is pure YM or an allowed gauge theory with matter/defects; fix the observable sector, reflection, and arithmetic source action. Treat OS as assumed.
2. **State the global theorem first.** Use one source map on all compact supports. List any allowed physical assumptions separately from the arithmetic existence conclusion.
3. **Audit existing YM identities for global determination.** Determine whether the insertion/loop hierarchy can characterize a pairing on that source module. Identify exactly what additional intertwining or Ward statement would be needed.
4. **Choose one existence mechanism.** Prefer module occurrence plus uniqueness if the algebra is sufficiently rigid. Use compactness only with a stated route to arbitrary finite feasibility and to identifying the limit as YM.
5. **Use finite models to test that mechanism.** A short-window result is worthwhile only if it checks a hypothesis of the global theorem or supplies a genuine obstruction.

No known result reviewed here establishes the required arithmetic module occurrence, uniqueness, or global moment feasibility. The revised direction is nonetheless a legitimate existence program under assumed OS positivity, and is better aligned with the user's aim than extending isolated \(L\)-certificates.

## 10. Relation to earlier notes

This note clarifies the scope and supersedes the finite-window-first recommendation in:

- [Arithmetic bootstrap design](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/notes/ARITHMETIC_BOOTSTRAP_DESIGN_AND_OPEN_GAPS_20260924.md).
- [Arithmetic bridge sweep](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/notes/ARITHMETIC_BRIDGE_SWEEP_AFTER_YM_20260924.md).

It retains their coefficient checks, scoped failures, and warnings about circularity. It does not remove YM or nonconstructive existence from the project.
