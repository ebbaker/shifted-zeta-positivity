# Research plan: a controlled positive hierarchy for growing Wilson loops in pure YM

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Reasoning effort:** not exposed; not inferred.  
**Status:** proposed continuation informed by the companion [preliminary analysis](YM_POSITIVE_HIERARCHY_PRELIMINARY_ANALYSIS_20260924.md), including new regulated projection identities and 64 finite diagnostic controls. This plan does not assume a continuum YM construction, finite hierarchy closure or an arithmetic match.

**Completion update, later on 24 September.** The [finite-slab boundary construction](FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md) and [first interacting test](FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md) now carry out the first two tasks below. Boundary multiplication has an explicit reflected realization, but the tested small families give large residuals in a genuine coarse 4D Wilson ensemble. The discrete projection is contractive, unlike the continuous approximation here. The latest test note supersedes the immediate next-session plan with local plaquette sectors, slice-only smoothing and forward/backward residual control. Vacuum and continuum questions remain open.

## 1. Objective and the change of strategy

The physical objective remains the one fixed in the parent investigation: hold the theory and state fixed, let a specified Loewner driver generate an actual curve, choose the return completion explicitly, and describe the evolution of the resulting Wilson observable.

The new objective within that problem is **an approximation with a positive norm and a measurable error**, rather than an exact scalar equation obtained by suppressing higher insertions. The N4SYM closure audit identified genuine extra terms. It did not show that all their projections are large, that a memory representation is impossible, or that a suitable observable family cannot approximate the result.

Pure YM is the initial theory because ordinary gauge holonomies are unitary on each configuration and Wilson lattice YM at theta zero has a positive measure. These are concrete advantages for this observable. This is not a claim that YM is generally easier than N4SYM, or that removing supersymmetry resolves continuum confinement physics.

The preliminary calculation supplies a useful starting pair, e and the transported curvature moment J. Its two-state approximation is norm preserving; its residual measures the derivative component orthogonal to J and the curvature-product component orthogonal to e and J. All quantities required to assess the approximation are specified before computing W. The exact formulas are in Sections 3–5 of the companion note.

## 2. Two separate clocks and two initial constructions

Use t for Loewner capacity and tau for physical Euclidean time. Place the contour in a spatial plane at tau zero. Choose a finite lattice spacing and finite spatial volume; the YM coupling and temporal state are fixed throughout each experiment.

There are two complementary initial constructions:

1. **Exact lattice boundary states.** Approximate the actual trace and straight return by a specified sequence of based spatial lattice polygons. The actual unitary link products define the shape steps. A positive transfer-matrix state supplies their inner product. This is the initial interacting problem.
2. **Smooth positive-measure controls.** Use a stated smooth regulator or prescribed finite ensemble to analyze the continuous curvature generator, the moving-basis connection and the residual formulas. The first examples are already computed. These verify geometry and algebra, not the YM measure.

The next work must join these constructions deliberately. A lattice polygon has discrete changes; a clover curvature operator does not automatically generate its exact loop evolution. Conversely, a smooth four-dimensional flowed observable need not be a boundary operator in the reflection construction. Neither discrepancy should be hidden by notation.

## 3. Work package A: establish the finite-lattice boundary dictionary

**Question:** which Hilbert space and reflection pairing realize the actual based loop state?

Write the spatial-link Hilbert space, its gauge action, positive transfer operator and vacuum preparation. Specify the nondynamical basepoint color fiber End(C^N), its normalized trace pairing, and the gauge constraint. The state is Omega times Q, with Omega times the identity as the reference. The scalar Wilson expectation is their overlap.

The companion note supplies the isometry from the positive slice measure and the elementary positivity of the transfer operator compressed to the gauge-covariant reference sector. Complete the dictionary by drawing or writing the reflected Wilson network and demonstrating that its temporal-gluing contraction equals that norm. Establish how the color reference is propagated and where its singlet and nonsinglet components reside. Any static-source normalization must be stated explicitly; a subtraction that changes positivity cannot be treated as harmless.

**Deliverables:** an exact finite-lattice statement of the boundary pairing; the corresponding loop expectation; the unitary discrete shape steps; and the finite-window storage identity with all channels named.

**Required controls:** identity/backtracking at zero driver; gauge covariance at the basepoint; an orientation/adjoint check; and a multi-contour Gram matrix computed directly from the same definition.

**Failure criterion:** if the chosen pairing instead computes a different endpoint network or requires resetting the retained color state at every shape step, it does not realize this proposal. Correct the dictionary before interpreting a positive matrix.

This package addresses the new OS null-space counterexample: it constructs an operator on boundary states explicitly rather than assuming every half-space multiplier descends to the OS quotient.

## 4. Work package B: measure the first omitted sector

**Question:** is the positive residual small enough to predict the Wilson shape effect in the interacting measure?

First fix a modest finite-volume SU(2) Wilson lattice experiment at theta zero. A strong-coupling or otherwise controlled finite-regulator regime is an acceptable first case; it must be labelled as that regime. No lattice Monte Carlo has been performed in the present package.

Choose the trace approximation, return chord, driver slopes and observed capacity interval before comparing approximations. Measure the full Wilson observable and a common collection of insertion observables on the same ensemble. For a smooth comparison use

\[
g=\langle\operatorname{tr}J^2/N\rangle,\quad
\dot g,\quad d=\langle\operatorname{tr}\dot J^2/N\rangle,
\quad\mu_4=\langle\operatorname{tr}J^4/N\rangle.
\]

The SU(2) cubic moment vanishes algebraically. For SU(3), retain the cubic moment. On the exact lattice, start with the discrete shape-increment observables and their block Gram matrices; establish the smooth correspondence before substituting continuum J formulas into a discrete evolution.

Construct the reduced prediction from the moments, and compare it to the separately measured Wilson expectation. Evaluate both the whole-state residual bound and the sharper observable bound. Report sampling error, autocorrelation, numerical derivative error and Gram conditioning. An empirical Gram matrix formed from a common sample set is nonnegative up to roundoff, but that fact alone is not a confidence bound for the exact ensemble matrix. Use correlated estimates consistently, and do not silently clip negative eigenvalues arising from independently estimated entries.

**Success criterion:** the error bound is smaller than the Wilson departure from its backtracking value over a nontrivial interval, with uncertainties controlled. A bound below one is too weak if the physical effect is of order 10^-4. The finite-background pilot shows why this criterion is attainable in principle, not that the interacting measure will satisfy it.

**Useful negative outcome:** if the derivative contribution dominates, quantify that contribution. If the fourth-moment contribution dominates, quantify its fluctuations. This decides which observable to retain next; it avoids another generic appeal to closure.

## 5. Work package C: enlarge the family according to the residual

The first candidate new observables are the two explicitly orthogonal components

\[
R_D=\dot J-\frac{\dot g}{2g}J,
\qquad
R_C=J^2-ge-\frac{\mu_3}{g}J.
\]

Keep whichever has the larger contribution in the relevant regime, or both. Include its derivative in the next residual. Use the full moving Gram matrix and connection; orthonormalizing at each shape does not remove the connection, it changes its expression.

This produces a finite sequence of physically specified approximations. The omitted observables are measured in the same positive norm. It is legitimate for the family to remain infinite in principle.

**Deliverables:** reduced equations for the first enlarged family; a Schur-complement residual; and comparisons of the error bound and computational cost against the two-observable family. Show the actual decrease if there is one. Adding time-dependent basis vectors does not by itself prove that the global error bound decreases monotonically.

The Schwinger–Dyson equations should be used here to relate measured insertion networks or bound selected combinations. They should not replace the transverse derivative by a full field equation. At positive flow time their use must differentiate the flow map as well. Scalar or fermion terms would have to be restored if the theory were later changed to SYM.

**Decision point:** continue enlargement only if it improves control on the observable or reveals a stable physical decomposition. If the Gram matrices become badly conditioned or every new level has order-one leakage, reconsider the basis or use the exact memory representation instead of calling the procedure a successful closure.

## 6. Work package D: study memory without assuming dissipation

The exact complement generates a two-time memory kernel. Determine which retained states carry its dominant correlations and whether the nonstationarity caused by shape growth is essential.

The finite example already shows that positive storage can return to the observed amplitude. Therefore an exponential-decay ansatz or a local damping coefficient needs its own approximation estimate. A Markov reduction should follow a demonstrated separation of correlation scales, not be assumed because the full Hilbert norm is positive.

**Deliverables:** a memory kernel or controlled reduced representation over the selected shape interval; a comparison with the explicit residual family; and a clear account of any discarded history or initial-state term.

If useful, the finite-mass N4SYM source can serve as a separate control with exactly known retained storage and one exponential memory. Its physical force/work norm and its Lorentzian time must not be identified with this YM shape construction.

## 7. Work package E: regulator refinement and continuum obligations

Only after the fixed-regulator construction is informative should the analysis vary lattice spacing, volume, contour approximation and any spatial smoothing radius.

Keep the physical contour shape and the chosen smoothing convention fixed during a lattice-spacing comparison. Test convergence of the observable, Gram entries and residual bound separately. At nonzero smoothing, make explicit which gauge-covariant spatial construction is used and whether it admits the desired smooth identity. Do not infer its renormalization properties from results for four-dimensional gradient flow without checking the different setup.

For unsmeared loops, keep perimeter, cusp, endpoint and insertion counterterms visible. Renormalized Wilson loops need not retain the elementary bound enjoyed by bare unitary link products. A positive bare Gram matrix does not prove that finite parts obtained by subtraction remain positive. A congruence change of an operator basis preserves a positive pairing when the same adjoint is used on both sides; arbitrary additive subtractions need a separate argument.

**Success criterion:** a nontrivial interval where the physical observable and error estimate remain controlled under the specified refinement. If only a smeared finite-resolution result survives, state that as the result. A theorem for continuum 4D YM is not a prerequisite for a useful finite-lattice investigation.

## 8. Relation to N=4 SYM and to an eventual physical channel

The part that may transfer back to N4SYM is the methodology: retain extra insertions as states, use a physically justified metric, and estimate projection error. The pure-YM skew multiplication generator does not transfer automatically. The scalar-arclength coupling in the N4SYM loop makes the configuration transport nonunitary; even a single Hermitian scalar exponential can increase its matrix norm. Extra channels cannot turn an arbitrary noncontractive readout into a passive one without changing preparation, supplying work, or choosing a different norm with physical justification.

A return to N4SYM therefore requires either a separately justified state-space realization for the same scalar-coupled observable or a clearly different unitary observable. The original BPS protection and localization claims must then be checked again. Setting all the troublesome N4 insertions to zero is not the proposed route.

Likewise, Loewner shape evolution is not physical time evolution. An eventual Lorentzian experiment would first specify a Hermitian boundary observable, a physical source coupled to it, the fixed quantum state, and the output and work account. Its Kubo response is a new calculation. The present initial-state overlap is not already a linear filter for arbitrary input waveforms.

Arithmetic comparison remains later work. Neither positivity of this state space nor finite hierarchy control creates prime delays or identifies its Gram form with the complete Weil form. A direct form-level identification could be pursued if a concrete equality emerges; a transfer proposal additionally requires the parameter, causal norm and delay structure. No such equality is suggested by the present finite diagnostics.

## 9. Recommended next bounded session

Complete package A and the exact discrete projection formulas for one lattice trace/chord family. Then design the smallest interacting measurement of package B, including its uncertainty analysis, before launching an extensive ensemble calculation.

The session should end with one of three concrete outcomes:

1. an exact reflected boundary dictionary and an informative first residual estimate;
2. a correct dictionary with a quantified large residual pointing to a specific additional observable;
3. an identified mismatch between the intended Wilson observable and the proposed positive state, requiring a revised construction.

The important advance would be an auditable relation between the original growing loop and a controlled family of observables. The present preliminary work supplies that relation in a regulated Hilbert setting and demonstrates it in finite noncommuting examples. The next experiment must determine whether it is useful in the actual interacting theory.
