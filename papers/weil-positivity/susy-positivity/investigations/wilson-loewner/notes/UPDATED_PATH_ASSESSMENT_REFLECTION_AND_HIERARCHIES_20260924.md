# Updated paths after WZW, N4SYM and arithmetic-storage: reflection positivity and observable hierarchies

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided model identity).  
**Reasoning effort:** not exposed; not inferred.  
**Repository baseline:** `488c782b639728a5dfd9685139b81e09cbb1cd40`.  
**Status:** research assessment, targeted replays and elementary deductions. This is not a specialist proof review, a new continuum QFT construction, or an all-window positivity result. The new arithmetic-storage structural propositions remain research-note results awaiting specialist review.

This updates the [23 September lessons](LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md) and the earlier [24 September cross-program priorities](CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md). In particular, the earlier priority of extending finite append certificates is superseded by the second arithmetic-storage session. Historical notes retain their original arguments and dates.

**Later YM follow-up on 24 September.** The [finite-slab reflection construction](../YM/notes/FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md) now realizes a positive spatial-boundary hierarchy and proves that its unitary boundary multiplication descends through OS nulls. The [first interacting 4D SU(2) experiment](../YM/notes/FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md) finds large residuals for the initial small curvature families; positivity is established at the finite boundary, useful compression is not. The immediate physics priority is now a comparison of local plaquette sectors, boundary-only smoothing and forward/backward observable control. This narrows the physics proposal below without changing its arithmetic assessment or repairing the original scalar-coupled N4SYM hierarchy.

## 1. Assessment

**The two ideas remain useful, but their strongest formulation has become more specific: construct a positive space of observables, retain the states and correlations that carry memory, and prove an exact identity with the arithmetic form or storage deficit.** Reflection positivity could supply the space; an observable hierarchy could identify its dynamics and the channels lost by a restricted readout. Neither ingredient alone proves the required arithmetic identity.

The new work changes the assessment in four ways.

1. **Reflection positivity has two viable arithmetic targets.** It may realize the complete central Weil form directly, or the cumulative defect of the causal transfer. The WZW self-adjointness obstruction excludes identifying a reflected compression with the nonlocal causal transfer itself. It excludes neither of these form-level targets. A direct construction of the central form need not first solve the separate physical problem of producing a variable fractional response front.
2. **N4SYM now demonstrates why retaining storage matters.** In the finite-mass, classical-string approximation, keeping the dressed-source state gives a positive finite-time energy balance. The troublesome Schott term is a term in an expansion of positive storage. This supports the method of enlarging the state space before eliminating variables. It does not establish Osterwalder–Schrader positivity for the interacting Wilson hierarchy, and that particular channel has the wrong arithmetic response.
3. **The hierarchy has become concrete without becoming closed.** The flipped-return observable has exact smooth-field first and second evolution equations and meaningful perturbative checks. Its Schwinger–Dyson audit exhibits additional observables that cannot be deleted. Supersymmetry does not close these first two levels. An infinite hierarchy, controlled projection, or positive enlarged state space remains possible; none has yet been constructed for this family.
4. **Arithmetic-storage now constrains the mechanism much more sharply.** The first-prime join is internally certified, but the append hypothesis is itself joined-window positivity. The new analysis rules out maintaining a fixed relative margin along arbitrarily long chains with join lengths bounded below. It also quantifies how sensitively positivity depends on the exact prime weight. Repeated finite joins and approximate arithmetic fitting should therefore lose priority.

My present arithmetic priorities are the **actual semilocal Sonin residual**, followed by a **focused canonical-system comparison that isolates an independent positivity estimate**. My preferred physics continuation is a **regulated positive-norm treatment of the YM/N4SYM insertion hierarchy**, using the finite-mass source as a solvable storage control. These are complementary research questions; progress on the physics question need not constitute progress on RH.

## 2. What changed after the original lessons

| Branch | New evidence | Consequence | What remains missing |
|---|---|---|---|
| WZW review | Independent model replay of the finite pilot; free-fermion/even-tower dictionary; distinction between reflected transfer and reflected form | Retain the pilot and the archimedean dictionary; remove an overly narrow tower comparison | The complete renormalized form, primes, physical preparation and norm |
| N4SYM straight line | Protected quadratic response is local, with an Abraham–Lorentz work account | The specified linear straight-line channel is exhausted as an arithmetic candidate | A different channel, rather than more precision in its two-point function |
| N4SYM growing trace | Flipped return restores exact backtracking at zero driver; first two smooth-field equations; near-BPS and regulator analysis | A viable nontrivial Wilson observable and explicit hierarchy | Continuum control, a positive hierarchy norm, and causal input/output preparation |
| N4SYM finite mass | One exponential memory and an exact positive work/storage identity in the stated approximation | A concrete control for retaining hidden states and deriving passivity | Arithmetic delays, variable front, and identification with the target channel |
| N4SYM quartic input | Validated dimension-one Euclidean input and anomalous-dimension structure; rejected dimension-two transcription | A credible nonlinear-response calculation remains to be done | Full retarded orderings and contacts; a linear stationary arithmetic channel |
| Arithmetic-storage | First-prime closure, block equivalence, fixed-length margin obstruction, prime-weight bounds | Stop treating another successful finite join as an independent continuation mechanism | A new sign or comparison estimate that works as length grows |

The principal sources are the [WZW review](../WZW/reviews/review_claude_wzw_program_assessment_20260924.md), [N4SYM assessment](../N4SYM/reviews/PROGRAM_ASSESSMENT_CODEX_20260924.md), [flipped-return derivation](../N4SYM/notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md), [closure audit](../N4SYM/notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md), [finite-mass/quartic note](../N4SYM/notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md), and [second arithmetic-storage session](../arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md).

The broad exclusions in the WZW review still require the qualifications in the [cross-program assessment, Section 2](CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md). The far-field transport theorem does not classify all field-dependent Wilson observables; the standard Eisenstein offset does not classify every multichannel scattering problem; the quarter-shift survey excludes its tested amplitudes and dictionaries. These qualifications preserve logically open alternatives without supplying positive evidence for them.

## 3. Reflection positivity: what is still viable

### 3.1 Three objects with different jobs

Write, in the parent's conventions,

\[
Q_{\omega,L}[g]=\operatorname{Re}\langle g,G_{\omega,L}g\rangle,
\qquad D_{\omega,L}=I-V_{\omega,L}^{*}V_{\omega,L}.
\]

The [shift-flow identity](SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md), on its stated domain, is

\[
\langle f,D_{\omega,L}f\rangle
=2\int_0^\omega Q_{s,L}[V_{s,L}f],ds,
\qquad
Q_{0,L}[f]=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\]

There are two possible positive-form constructions:

\[
Q_{0,L}[f]=\|\mathcal A_L f\|_{\mathcal H}^{2},
\qquad\text{or}\qquad
\langle f,D_{\omega,L}f\rangle
=\|\mathcal B_{\omega,L}f\|_{\mathcal H}^{2}.
\]

In either case the amplitudes must be defined independently of the assertion being proved. Writing a formal square root of Q or D assumes its positivity. Likewise, building a positive model from the critical-line zero measure and then identifying that measure with the entire explicit formula would assume the unresolved step.

A bounded self-adjoint causal scalar operator on an interval is multiplication. Consequently a reflected compression cannot be the desired nonlocal V. This is compatible with a reflected construction of Q or D, which are self-adjoint objects. Also, at a fixed positive shift, positivity of the instantaneous Q is not equivalent to positivity of D: the latter depends on the integral along the evolution.

**A change in emphasis from the original lessons:** accumulated storage is one valid use of reflection, not the only one. A direct reflected realization of the central form could bypass constructing a physical V. Such a proposal must reproduce the complete local, pole and arithmetic terms on the required test domain, but it should not be rejected merely because it has no causal fractional-front interpretation. Those extra requirements belong to a proposed transfer realization.

### 3.2 What the WZW correction supplies

The reviewed identity is

\[
\frac12\left(\frac1{2\sinh(u/2)}+
\frac1{2\cosh(u/2)}\right)
=\frac{e^{-u/2}}{1-e^{-2u}}=n_\Gamma(u),\qquad u>0.
\]

The SU(2) level-2 fermion sector therefore supplies the separated archimedean tower after the indicated combination. This corrects the earlier single-primary spacing test. It does **not** identify the required contact prescription, rational completion, prime atoms or full positive norm. The two spin-structure expressions still need a specified physical preparation and adjoint before their sum can be used as a Gram construction.

This is a reusable free-field component. Enlarging the WZW level, adding descendants, or revisiting the already-tested regular thermal loads does not currently address the missing joint arithmetic identity. The Bost–Connes calculation similarly gives exact positive coefficient probabilities, not a common causal amplitude or a complete storage norm.

### 3.3 What the finite-mass result adds

In the zero-temperature, planar classical-string approximation, at linear order and for an initially static source, the N4SYM note obtains

\[
F=m\ddot Y,\qquad X=Y+z_m\dot Y,
\qquad
\int_{-\infty}^{T}F\dot X,dt
=\frac m2\dot Y(T)^2+mz_m\int_{-\infty}^{T}\ddot Y^2,dt.
\]

The energy of the dressed state involves Y, not just X. Expanding this state energy in the short memory time produces the indefinite Schott cross term. Removing or truncating the state before assessing positivity can therefore obscure a valid finite-time balance.

An elementary consequence makes the norm issue explicit. Fix a positive reference impedance \(\eta\), set \(v=\dot X\), and define real port amplitudes

\[
a=\frac{F+\eta v}{\sqrt{2\eta}},\qquad
b=\frac{F-\eta v}{\sqrt{2\eta}}.
\]

Then

\[
\|a\|_{(-\infty,T)}^2-\|b\|_{(-\infty,T)}^2
=m\dot Y(T)^2+2mz_m\int_{-\infty}^{T}\ddot Y^2,dt\geq0.
\]

For zero initial state the corresponding Laplace-domain scattering coefficient is

\[
S_\eta(p)=
\frac{(m-\eta z_m)p-\eta}{(m+\eta z_m)p+\eta}.
\]

This follows directly from \(v/F=(1+z_m p)/(mp)\). Its pole is in the left half-plane and its boundary modulus is at most one. Thus the work identity can be converted into an ordinary signal-norm contraction with an explicitly specified preparation and readout. This algebraic deduction is a useful control, not a new interacting-QFT positivity theorem. The coefficient remains rational and has none of the required arithmetic delay structure; choosing an impedance does not identify it with K.

The lesson for the hierarchy is concrete: seek a norm for the full state and derive the observed contraction by a controlled projection. This energy argument and Euclidean reflection positivity are different mechanisms. The finite-mass computation validates the storage strategy without proving the proposed Euclidean reflection inequality.

The dilaton's absence of temporal broadening is also established in prior arbitrary-motion work by [Chernicoff–Güijosa–Pedraza](https://arxiv.org/abs/1106.4059). The N4SYM assessment correctly redirects the earlier novelty claim toward comparison with that paper. A new numerical check of the local formula would not make the general localization claim new.

### 3.4 A useful positive hierarchy must use the actual adjoint

The parent's [reflection section](../sections/08_reflection.tex) gives a conditional construction. For admissible half-space observables \(F_i\),

\[
K_{ij}=\langle\Theta F_i\,F_j\rangle\succeq0
\]

requires a regulator, reflection operation, color sector where needed, and limiting renormalization that preserve the inequality. Gauge invariance by itself does not prove it. In particular, the flipped return used to restore backtracking in the growing-loop calculation is an inverse transport; it must not automatically be identified with the reflected physical adjoint.

The proposed next construction is a Gram family of the transported curvature, scalar-gradient, ordered-pair and endpoint observables already generated by the hierarchy. It should start at fixed regulator with observables genuinely in a positive-half-space algebra. Gradient-flow smearing smooths fields but can extend their support across a reflection plane; it is not automatically an OS-preserving regulator for this purpose.

A positive Gram matrix would control Cauchy–Schwarz inequalities and orthogonal projections among these observables. It would not prove that growth in Loewner capacity is dissipative, or that any selected Wilson expectation is a contractive channel. Connected correlators, truncations of perturbation theory and finite-part subtractions also need not preserve the positivity of the full Gram matrix. These are the specific issues the next calculation should address.

## 4. The observable hierarchy: new evidence and the remaining task

### 4.1 The successful observable is more informative than the original proposal

The constant-scalar trace-plus-chord completion developed a thin-sliver attraction. The tangent-coupled completion was trivial in the protected setting. The flipped-return completion instead has configuration-by-configuration identity at zero driver and nontrivial shape dependence away from it.

For smooth fields, with \(Q_t=R_t^{-1}U_t\), the new calculation gives

\[
\dot Q_t=\mathcal X_tQ_t,
\qquad
\frac{d^2}{dt^2}\langle N^{-1}\operatorname{tr}Q_t\rangle
=\left\langle N^{-1}\operatorname{tr}
\big((\dot{\mathcal X}_t+\mathcal X_t^2)Q_t\big)\right\rangle,
\]

where \(\mathcal X_t\) contains transported gauge curvature, normal scalar gradient and the scalar tip term weighted by the rate of change of the trace/chord length mismatch. The identities have noncommuting-background checks. Passing to quantum expectations and taking continuum limits retains the stated integrability and renormalization obligations.

The leading shape behavior depends on the order of limits: the fixed-flow small-time expansion has an \(a^2t^3\) term, while the continuum near-BPS cusp regime has an \(|a|\sqrt t\) term with regulator logarithms. This is evidence for controlling the limits, not a contradiction between the two calculations. Bare cusped loops still require cusp renormalization.

The near-BPS analysis supplies a useful effective coupling and a classical strong-coupling crossover. Its claimed one-loop exact corner slope is an order-by-order statement under the multi-angle antiparallel bound used in the note; it is not an unconditional nonperturbative theorem. These results strengthen the physical observable without furnishing an arithmetic channel.

### 4.2 The nonclosure is now an explicit calculation

The second equation contains transverse gauge derivatives, scalar and fermion currents, a transverse scalar Laplacian, scalar-potential and Yukawa insertions, transported scalar commutators, tip gradients and ordered pairs. Schwinger–Dyson identities reduce selected field-equation combinations, not this whole inventory.

Two controls are particularly informative. A harmonic four-dimensional scalar background has a nonzero planar Laplacian, so the planar derivative cannot be replaced by the full field equation. At one loop the transverse residual has a nonzero long-range contribution, while the field-equation part is a regulator contact. The omitted terms therefore matter in the actual perturbative observable, not only in an artificial example. Differentiating transport along a scalar-coupled chord also produces a scalar commutator that cannot be discarded.

The original lesson that four-dimensional evolution need not close like a finite KZ system is substantially strengthened. It remains a scoped result: failure at the first two levels does not exclude a larger invariant sector or a useful infinite hierarchy. No such sector or controlled infinite completion has been identified here.

### 4.3 What would make further hierarchy work worthwhile

There are three levels of progress:

1. **Formal identities:** further exact equations with all residual terms retained. Useful for organizing the physical theory, but increasingly costly without estimates.
2. **Controlled hierarchy:** a common domain, positive norm and estimates for the generated observables, or a finite projection with a rigorous remainder. This would be a substantial new result.
3. **Arithmetic realization:** a specified linear source preparation and readout whose pairing equals the complete Q or D. This is additional to level 2.

The best next physics step is level 2. One option is a regulated Gram construction for the first genuinely nonclosed insertion sector, including its transverse and endpoint terms. Another is exact memory elimination within a state space whose generator and energy balance are already controlled. Schematically, for a justified splitting into observed x and retained z,

\[
\dot x=A_{00}x+A_{01}z,
\qquad\dot z=A_{10}x+A_{11}z
\]

gives a memory kernel \(A_{01}e^{tA_{11}}A_{10}\), together with the initial-state term. The useful theorem would establish the relevant domains, propagation, norm and dissipative balance; writing this formula formally does not establish them. A positive state metric alone does not make its generator dissipative.

The quartic defect calculation is a bounded alternative if the aim is nonlinear real-time physics. The complete retarded kernel must include nested commutators with all time orderings and the source-contact terms. A discontinuity of one Euclidean logarithm is not the complete cubic response. The dimension-one input has passed its transcription controls; the failed dimension-two transcription should not be reused as if validated.

A nonlinear power-law response is not a linear L2 transfer. About the native scale-free straight line there is no distinguished sequence of positive delays. Varying a coupling-dependent operator dimension also varies the bulk theory, whereas the original proposal asked for evolution in a fixed theory. A new background or defect dynamics could change the question, but would need to supply stationarity, parameter action, delay geometry and the physical norm explicitly. Finite temperature or a richer pole spectrum alone is not evidence of the required logarithmic arithmetic delays.

## 5. Arithmetic-storage changes the continuation question

### 5.1 The first-prime join is closed, but its hypothesis is the joined form

For coercive local forms, the second session writes

\[
Q_{0,L+h}=
\begin{pmatrix}A&-B^*\\-B&C\end{pmatrix},
\qquad
\kappa_0=\|C^{-1/2}BA^{-1/2}\|.
\]

Its elementary block lemma gives

\[
\kappa_0\leq\kappa
\quad\Longleftrightarrow\quad
Q_{0,L+h}\succeq(1-\kappa)(A\oplus C).
\]

Thus \(\kappa_0\leq1\) is joined-window positivity. A relative estimate contains quantitative information beyond an absolute floor, but it is still an estimate on that window. The energy-transfer lemma supplies a useful Schur-complement margin; the existing method does not carry that margin to the next join without another positivity estimate.

At \((L,h)=(11/20,1/5)\), the committed internal certificate gives

\[
Q_{0,3/4}\succeq\frac{123}{250000}I,
\qquad\kappa_0\leq0.99980037,
\]

and a normalized cumulative coupling below 0.99981859 at shift 0.001. It also gives direct contraction for shifts up to 1/50. The earlier proposed intermediate target 0.999 was stronger than necessary. Existing weil-depth results already cover larger joined windows; this closes the proposed append task without extending the certified horizon.

The note's Proposition 1 says that no fixed positive relative margin survives all fixed-length joins. Under RH, its explanation is especially instructive: the atomic Weil spectral measure makes arbitrarily long past observations dense in the corresponding spectral Hilbert space, so the old and new segment subspaces become arbitrarily correlated. If RH fails, some joined form ceases to be positive. The domain-splitting and almost-periodic density arguments deserve specialist review; the strategic downgrade of repeated joins already follows from the elementary block equivalence, independently of that proposition.

This does **not** exclude vanishing margins, shrinking joins, or a different state realization. Nor does it prove that a shrinking-join scheme exists. The suggested scale \(h_k\sim e^{-L_k}\) rests on a heuristic eigenvalue profile. An infinitesimal Schur evolution may be a useful comparison with canonical systems, but the precise identification has not been proved in these notes.

### 5.2 Exact arithmetic interference is now a measured requirement

With only the first prime present,

\[
Q_R(s)=Q_R^{A}+sM_2,
\qquad
M_2=-\frac{\log2}{\sqrt2}(S_{\log2}+S_{\log2}^{*}),
\]

where s=1 is the arithmetic weight. The latest certificates at \(R=\log3\) imply failure for

\[
s\geq1.00000316
\quad\text{or}\quad s\leq0.9999182,
\]

and guarantee positivity for \(|s-1|\leq1.1\times10^{-7}\). The outer bounds are exclusion thresholds, not a proof that every intermediate weight is admissible. The archimedean-plus-pole form alone loses positivity between lengths 0.74 and 0.745. Consequently the prime term is indispensable by that length, and it repairs particular directions through interference; it is not simply an additional positive summand.

Under RH, Proposition 2 further proves that a bounded continuous translation-invariant perturbation symbol must be nonnegative if positivity is to hold on every window. A nonzero isolated prime-weight change has a sign-changing cosine symbol and therefore fails on some window, with all other terms fixed. The attempted unconditional extension is only sketched and should not be reported as proved. The result also does not classify boundary-dependent errors or correlated changes outside its hypotheses.

For a reflection construction, the implication is **joint Gram geometry rather than separate positivity of the gamma and prime terms**. Signed cross terms can occur inside a squared norm. A successful construction must explain why their coefficients and the remaining completion terms are exactly right. Generic extra dissipation can make a different form positive; it does not prove positivity of the original form. This observation does not forbid approximation with certified finite-window error bounds or with an error that tends to zero in a controlled limiting argument.

For a transfer construction, the equivalent warning is to keep full memory across a boundary. The failed finite gamma-tower proxy discarded endpoint energy needed in the mixed-block cancellation. It is a failure of that lower-bound method, not a counterexample to the complete transfer.

## 6. Viable paths, ranked by the next informative result

### A. Actual semilocal Sonin pairing and residual — first arithmetic priority

This has an independently positive ambient space and exact finite-place arithmetic operations. The remaining problem is the comparison with the complete Weil form. It is closer to the direct-form reflection strategy than to engineering a new physical transfer.

The [published archimedean theorem](https://arxiv.org/html/2006.13771v1) supplies a Sonin trace inequality on its stated short support with prescribed transform zeros; without the extra zero-frequency condition the comparison has a negative rank-one correction. It is not an unrestricted all-input same-window bound. The [semilocal stability theorem, Theorem 4.13](https://arxiv.org/html/2310.18423v1), transports the spaces by a bounded invertible map, with place-dependent inner product. Stability is not an isometric monotonicity theorem.

The earlier local comparison, summarized in the [cross-program note, Section 4](CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md), suggests

\[
M_2=I-2^{-1/2}U_{\log2},\quad G_2=M_2^*M_2,
\quad A_2=\left.\Pi G_2\Pi\right|_{\operatorname{Ran}\Pi},
\quad\Pi_2=M_2\Pi A_2^{-1}\Pi M_2^*.
\]

Here M2 denotes the finite-place map, not the signed prime form in Section 5.2. The inverse compressed metric is essential. Its suggested positive pairing \(\|C_F\Pi_2\|_{\rm HS}^2\) leaves a signed comparison remainder involving the off-diagonal projection block, the archimedean correction, poles and the explicit prime term.

**Next bounded task:** rederive that comparison from the primary sources in repository-local notation, including trace-ideal and domain claims; then evaluate the actual residual on the weak even and odd directions near the first-prime window, with controlled error. The floor near log3 is only about \(5\times10^{-8}\), so a coarse generic estimate is unlikely to decide the sign. The earlier local formula has not yet been independently established or its actual Sonin trace evaluated. Replacing Pi by an arbitrary positive finite matrix would miss the question.

**Success:** a sign-controlled residual, a new domination inequality, or a verified obstruction to this particular comparison. Merely constructing another positive Sonin Gram matrix is not progress on the missing identity. Negativity of one chosen residual would refute that proposed domination, not Weil positivity itself.

### B. Canonical systems and infinitesimal continuation — focused arithmetic audit

This retains the complete arithmetic kernel and can accommodate changing local scales. Its value depends on exposing a local estimate that is not just positivity on the next whole window in another notation.

Keep two existing constructions distinct. [Suzuki's 2012 explicit canonical-system theorem](https://arxiv.org/html/1204.1827), Theorem 2.3, assumes omega greater than 1; Section 5 discusses the difficulty of smaller shifts. The repository's [omega-string working draft](../../../../shifted-zeta/omega-string/STATUS.md) constructs positive inverse-spectral strings unconditionally in its safe range omega at least 1/2, with smaller shifts subject to a zero-free-half-plane condition. That draft explicitly makes the full small-shift family equivalent to RH and awaits specialist review. Neither construction already supplies unconditional continuation to zero shift.

**Next bounded task:** compare the exact kernels, parameter meanings, determinant/invertibility conditions and Hamiltonian positivity assumptions with the append block form. Derive where the first prime enters after the canonical coordinate change; arithmetic delay log(p) must not be assigned to canonical depth by fiat. Identify the first estimate that remains meaningful as the finite-window margins shrink.

**Success:** a local arithmetic reason for positivity or a new estimate uniform in the required limiting regime. If the construction assumes small-shift innerness or an equivalent positive spectral measure, retain it as an organizational equivalence and do not count it as a separate proof mechanism.

### C. Reflection and a controlled YM/N4SYM hierarchy — first physics priority

This is the most direct continuation of the user's two interests. Use the already computed insertion family; construct its reflected pairings at a specified regulator; check the actual adjoint and contact terms; then seek an estimate for the first omitted sector or a projection identity retaining its energy. Compare that procedure with the finite-mass model, where the hidden state and norm are explicit.

**Success:** a nontrivial controlled hierarchy, or a positive memory realization with specified source and output, in the stated physical regime. That would improve the physics program even without an arithmetic match. For arithmetic relevance, a later calculation must identify its full quadratic form with Q or its storage with D on arbitrary inputs. No presently computed N4SYM observable has passed that test.

A literal interacting OS construction may be too difficult as the first task. A finite-regulator or solvable-sector control is acceptable if its restricted scope and continuum obligations remain explicit. Supersymmetric localization or a protected subsector is useful only if the actual nontrivial observable and its adjoint survive in that sector.

### D. Quartic retarded defect response — bounded physics project, low direct arithmetic priority

Complete the Lorentzian continuation of the validated dimension-one input, including contacts. This could establish the proposed nonlinear memory in an actual response function. It should be pursued for that physical result. Reopening the arithmetic question requires an independently motivated background or defect mechanism with a linear stationary channel and native arithmetic structure. A coupling-dependent exponent alone does not meet those requirements.

### E. Global arithmetic scattering or thermal completion — reserve direction

The modular Hodge benchmark realizes the completed half-shift channel, while the KMS calculation supplies exact primitive probabilities. A new construction joining arithmetic places, completion and physical amplitudes remains logically open. The already-tested loop interfaces, fractional cusp load and finite-total-mass thermal load remain poor candidates.

Reopen this direction only with a specified change that resolves the variable-shift and norm problem, preserves the arithmetic delay support, and survives the first-prime weight test. A larger ordinary WZW module or another fitted passive bath does not currently supply such a change.

## 7. What not to infer from these results

- The full physical state may have positive energy while a chosen observable or subtracted effective account fails finite-time passivity.
- A hierarchy's nonclosure does not imply a negative norm; a positive norm does not imply contraction under arbitrary geometric growth.
- Arithmetic positivity does not require each arithmetic summand to be positive.
- The new fixed-join result does not exclude all continuation, and its shrinking-step suggestion is not an existence theorem.
- The prime-weight rigidity theorem has a conditional spectral hypothesis and a specified perturbation class. It does not prohibit all physical continua, numerical approximations or enlarged Hilbert spaces.
- A direct Q realization can avoid the engineering obligations of a physical V realization, but cannot avoid exact completion, domain control and the all-window requirement.

## 8. Evidence and verification for this update

I read the active notes and reviews listed above, the parent reflection and cumulative identities, the committed closure and weight records, and the omega-string status and relevant source statements. I also checked the primary Sonin, semilocal and Suzuki theorem statements and the prior finite-mass dilaton result. This is a synthesis of the available work, not an exhaustive new literature survey.

Targeted fresh replays passed: WZW program review, 40 controls including 24 exact; N4SYM rounding/closure, 20 controls; finite-mass response, 107 controls; quartic input, 93 controls. These 260 controls test their stated algebra and diagnostics. In particular, the quartic replay includes expected rejection of the bad dimension-two transcription; it does not validate that transcription or a full cubic retarded kernel.

The first-prime record checker also passed its source bindings, 15 nested interval pairs, eight floating reduction controls and conditional rational implication. I separately checked the committed join-closure source bindings and rational implications. I did not regenerate the large-precision Arb matrices or independently verify their tail theorem in this update. The first-prime floor and weight bounds are therefore reported as the repository's internal certificates, not new independent certifications. The old record checker's 0.999 hypothesis remains labelled conditional; the second session closes the task by a different sufficient bound.

A small [verification record](../numerics/records/updated-path-assessment-20260924.json) records the replay scope and source hashes. Specialist review is particularly valuable for the log-energy splitting, the fixed-join density argument, the actual Sonin trace comparison and the continuum reflected hierarchy. None of the three investigations currently establishes an exact physical realization of the complete arithmetic positivity mechanism.
