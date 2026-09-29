# Meta-analysis of the shifted-zeta-positivity research program

26 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed to the lead reviewer and are not inferred. Three parallel agent readings supported this synthesis. They are additional machine reviews, not independent human refereeing.

**Scope:** the current local working tree at baseline commit `122e0f7f681bd3cbec52d1f3aa79252365b24001`, including the uncommitted CCM/operator and fractal investigations. This is a strategic mathematical review of manuscripts, indexes, selected proofs, notes and review exchanges. It is not a complete proof audit, a certificate replay, or a claim of novelty. The [coverage record](../notes/COVERAGE_AND_SOURCE_LEDGER_20260926.md) identifies the reading groups and external sources. Existing research files were not revised.

## 1. Assessment

There is a coherent research program here, and further mathematical progress is possible. There is not presently an established mechanism that is plausibly close to proving RH. Most branches either characterize the same missing positivity, realize an already positive finite object in new coordinates, or prove why a proposed mechanism cannot work. The strongest positive assets are the precise arithmetic normalization, finite-window analytic and certification tools, exact transfer decompositions, and the increasingly explicit connection to prolate/Sonin constructions. The strongest negative assets are scoped obstruction theorems that identify which estimates discard the information needed at large support.

The main missing ingredient is **an arithmetic relation that controls the joint prime, archimedean, pole and boundary contributions as support grows**. Generic positivity of an auxiliary system does not supply that relation. Neither does fitting a spectrum, matching a gamma factor, or recasting a Schur complement as storage.

My recommendation is to concentrate the RH-directed work on two connected questions:

1. **Why should the actual Weil ground state follow the prolate candidate?** The newest CCM audit states a sufficient comparison estimate and shows why several substitute estimates fail.
2. **Can the semilocal trace formula produce a positive form with a residual controlled on fixed compact tests?** This seeks the same missing arithmetic relation at the level of quadratic forms, without requiring the particular CCM eigenvector comparison.

A shrinking-step canonical-system continuation is a third, conditional priority. It needs an independently derived evolution law preserving positivity; the current coupling inequality is not such a law. Further bulk-field and geometric constructions should have a specific new mechanism to test before receiving substantial effort.

This is a resource judgment, not a theorem that the alternatives fail. The evidence supports tractable questions about operators, asymptotics, and obstructions. It does not support a numerical probability of proving RH, or an expectation that another finite computation will reveal the missing structure.

## 2. What actually has to be proved

Use the program's total support length convention:

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
Q_{0,L}[f]\ge0\quad\text{for every }L>0,
\quad f\in C_c^\infty((-L/2,L/2)).
\]

Here the zero denotes the central shift, not an eigenvalue. This is the full arithmetic Weil form. The gamma-only form equals it only in the appropriate prime-free range. Factors of two in support length differ between papers; comparisons must first reconcile test support, autocorrelation support, and logarithmic coordinates. The [program overview](../../../susy-positivity/PROGRAM_OVERVIEW.md) and [Weil-depth manuscript](../../../shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex) give the local conventions. Suzuki's [screw-function paper](https://arxiv.org/html/2606.09096v2) provides a primary-source comparison for the localized form and its operator realization.

There are several sufficient ways forward; they should not be conflated.

- **All-support positivity:** a proof on an unbounded sequence of nested support windows suffices. Every fixed compact test eventually fits. A uniform strictly positive lower bound is unnecessary.
- **Diagonal transfer contraction:** the repository proves that \(L_j\to\infty\), shifts \(0<\omega_j\downarrow0\), and all-input inequalities \(\|V_{\omega_j,L_j}\|\le1\) suffice. The allowable shifts and coercive margins may shrink. Causality restricts the inequality to each fixed shorter interval before the central derivative is taken.
- **Positive form approximation:** if independently positive forms \(P_j\) are eventually defined on every compact smooth test and \(P_j[f]\to Q[f]\) for each such test, then \(Q[f]\ge0\). This elementary route does not require convergence in operator norm on the whole line. A one-sided estimate \(Q[f]\ge P_j[f]-\epsilon_j(f)\), with \(\epsilon_j(f)\to0\), also suffices.
- **Spectral approximation:** real-zero entire approximants can prove RH if they converge in a suitable holomorphic topology to the correctly normalized Xi function. Real finite spectra alone are insufficient. Local uniform convergence, a nonzero limit, and arithmetic identification are the bridge.

The third formulation is a useful discipline for future research: seek the weakest topology that proves the desired sign. It is an implication, not a newly constructed family of positive approximants.

Some apparent roadblocks come from asking for more than RH requires. A single closable norm factor on ordinary whole-line \(L^2\), a support-independent coercive gap, a fixed nonvanishing shift interval, or norm convergence of every boundary expansion may be false or unavailable while one of these sufficient routes remains possible. Conversely, weakening the target does not construct the required family.

## 3. Map of the approaches

“Established” below means established in the cited repository arguments or internal certificates, with their stated hypotheses. It does not mean externally human-verified.

| Approach | Durable contribution | Missing ingredient or obstruction | Assessment |
|---|---|---|---|
| Early higher-dimensional, quaternionic, twistor, Yang–Mills motivations | Historical motivation for seeking additional symmetry and bulk/boundary structure | The root README describes this prehistory; this checkout does not provide enough of those earlier papers for a substantive audit. Additional coordinates alone impose no new constraint on zeta. | Background, not an independently assessed active proof route. |
| **Psi-omega margin, omega-string, defect-depth** | Quantitative zero-free/positivity criteria, shifted inverse spectral family, endpoint and defect-length analysis | Positivity or innerness at small shifts and arbitrary support is not supplied by reconstructing its consequences. Endpoint statements remain conditional on the required positive family. | Retain as the program's dictionary and possible continuation framework. |
| **First-slab, Weil-depth, storage-depth** | All-input finite-window certificates, central-to-shift estimates, Schur and residual continuation tools, precise omitted-input accounting | Each new join still needs a new arithmetic sign estimate. Separate prime-norm estimates encounter a structural dimension barrier. | A useful completed methodological base; stop routine depth extension as an RH strategy. |
| **Positive factorizations and SUSY organization** | Small-window factors, auxiliary-field gamma kinetic energy, restricted odd factors, exclusions of pairwise-square and whole-line \(L^2\) constructions | No all-support rule fixes the full arithmetic factor. Writing a graded square after finding a factor does not explain the factor's existence. | Retain the obstructions and domain lessons; require a new arithmetic identity. |
| **Topological SUSY bulk, ground-state geometry, inverse bulk** | Boundary/response identities, gamma comparison, explicit collective couplings, tests of contact and pole matching | A topological cap or chosen Schur completion has not forced the arithmetic sign. Exact realization of selected terms is not realization of the full positive form. | Operator tools survive; the tested physical explanations do not close the problem. |
| **Finite-response technical note** | Noncompact boundary correction, finite-input tail control, alternative image expansion, exact Schur reduction | The finite response still contains an infinite inverse and the remaining sign. Its effective cutoff estimate grows too rapidly. | Potential analysis contribution; no demonstrated new all-support mechanism or certification advantage. |
| **Source-selection rules** | Useful checks of normalization, short-distance growth and prime-delay structure | Several historical statements promote a chosen representation or numerical observation into a universal requirement. | Use as candidate tests only after restoring hypotheses. |
| **Wilson lines and Loewner** | Exact all-pass/phase description, positive-measure plus exponential-moving-average decomposition, direct arithmetic transfer assembly | Boundary unimodularity and a positive component do not give half-plane analyticity or contraction of the completed transfer. | Strong calculational dictionary; the original bare-Loewner proposals have scoped exclusions. |
| **Fractional dimension** | Unified gamma/comb/pole parameter dictionary, explicit failure of a fractional theta point-count interpolation | Continuing a formula through noninteger dimension does not continue a positive space or establish passivity. | The dictionary is informative; “dimension” is not an added positivity principle. |
| **Critical path and arithmetic storage** | All-input finite anchor, normalized cumulative append bound, first-prime closure, arithmetic-weight rigidity tests | The central append condition is joined-window positivity in relative form. Fixed-length joins cannot retain a fixed relative margin under the note's hypotheses. | Shift to a genuine continuation law or a new semilocal identity. |
| **Wilson–Loewner physical sources, WZW, N4SYM** | Specified observables, local response and storage calculations, normalization and front-exponent tests, closure residuals | No independently derived channel produces the full shift dependence, prime delays, arithmetic coefficients and required norm together. | Useful physical work, currently low direct RH priority. |
| **Interacting YM and one-probe response** | Signed prime/archimedean limits, domain and occurrence obstructions, reduction to one detecting correlation | A signed mixed identity is not a positive source norm. The required actual correlation is itself sufficient for RH and has not been obtained from YM. | Preserve as an obstruction record; resume only with a specified source outside excluded classes. |
| **CCM operators, strings, graph Dirac systems** | Exact finite realizations, fixed-support trace-class results, conditional determinant convergence, infinite Fourier-tail certificate | Simple-even ground hypotheses, arithmetic ground-state comparison, and support-growing convergence remain missing. Shifted mechanics loses the absolute ground-energy sign. | Most precise current spectral target, conditional on a new arithmetic estimate. |
| **CCM fractal/resistance geometry** | A changing-scale tree defeats a broad spectral-growth objection; explicit tests exclude the prescribed arithmetic-coordinate map | Matching \(T\log T\) counting or realizing a finite pencil does not identify Xi. The tested odd-coordinate form fails scalar Markov positivity. | Do not build another geometry without a new arithmetic estimate it would yield. |
| **RH detector / de Bruijn–Newman diagnostics** | Finite residual, multipole and polynomial-pencil diagnostics | No uniform hidden-defect detection theorem. A tail formula needs a separate audit for hypothetical off-axis zeros. | Diagnostic branch, not a current global proof mechanism. |

The [coverage record](../notes/COVERAGE_AND_SOURCE_LEDGER_20260926.md) links each cluster to its controlling documents. Latest notes sometimes supersede their own README summaries; in particular the first-prime join is already closed internally, and the latest CCM audit has already recommended suspending automatic fixed-support enlargement.

### Three distinct questions in the original shifted-zeta papers

The original sequence deserves a distinction that the larger operator program can obscure.

**The margin paper asks how a zero-free boundary appears in time.** It decomposes the shifted screw function into an explicit linear term, a constant, and a zero-dependent remainder. A violating nonreal quartet produces exponentially amplified oscillation below the critical shift. This yields one-sided formulations, including the stated criterion that integrability of the unshifted negative part implies RH. The missing ingredient is a prime-side one-sided estimate. It is not supplied by showing how hypothetical zeros would violate the estimate. These scalar time-domain questions remain legitimate analytic search directions; they have no presently demonstrated advantage over the main positivity problem. The Dirichlet extension also needs care: a possible exceptional real zero does not have the same oscillatory signature.

**The string paper asks what positive inverse spectral object corresponds to that boundary.** Its Weyl function is

\[
q_\omega(z)=\frac{(\xi'/\xi)(1/2+\omega+\sqrt{-z})}{\sqrt{-z}}.
\]

Membership in the Stieltjes class, in the stated regime, is the crucial condition. Positive boundary density does not suffice when poles have crossed away from the cut. Continuity from the unconditional region does not exclude such a crossing. The endpoint geometry is singular: the paper describes a change from continuous to atomic spectral measure and from infinite strings to a finite endpoint in a local limit. This makes a naive compactness argument especially hazardous.

**Defect-depth asks how much finite information detects a violation.** Its Christoffel and moment calculations quantify a controlled defect added to a positive reference. The zeta application with a single scaled quartet is a model, not a theorem about every possible zero configuration if RH fails. The fixed-defect asymptotics do not automatically remain uniform when the defect moves toward the compactified support or the shift tends to zero. Uniform moving-point estimates would be worthwhile mathematics, but would improve detection rather than independently prohibit defects.

These distinctions suggest useful secondary projects—one-sided arithmetic screw estimates, quantitative inverse-spectral endpoint analysis, and uniform defect-detection bounds—without mistaking them for a completed route to RH. Their controlling texts are the [margin manuscript](../../../shifted-zeta/psi-omega-margin/psi_omega_concise.tex), [string manuscript](../../../shifted-zeta/omega-string/omega_string.tex), and [defect-depth manuscript](../../../shifted-zeta/defect-depth/defect_depth.tex).

## 4. The traps that recur across branches

### 4.1 Moving the sign problem into the definition

The following constructions can be useful reductions, but they do not prove the premise they use:

- define the energy as the desired contraction defect;
- take the positive square root of a form whose sign is unknown;
- invoke a de Branges/canonical-system realization after assuming the needed innerness;
- define a covariance by zeta-zero ordinates and then appeal to Hilbert-space positivity;
- postulate a physical correlation equal to the arithmetic detecting correlation;
- eliminate high modes and call the remaining unknown positive matrix a completion theorem.

RH-equivalent reformulations are not automatically sterile. A reformulation advances a proof when some additional, independently established structure makes its difficult hypothesis accessible. The review question is: **what theorem has become easier to prove, and why?**

The arithmetic-storage [join note](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md), Section 1, makes this especially transparent. With coercive local forms,

\[
Q_{L+h}=\begin{pmatrix}A&-B^*\\-B&C\end{pmatrix},\qquad
\kappa=\|C^{-1/2}BA^{-1/2}\|,
\]

\[
\kappa\le1\quad\Longleftrightarrow\quad Q_{L+h}\ge0.
\]

A bound \(\kappa<1\) gives useful quantitative information. But deriving it by the Cauchy–Schwarz inequality of the *joined positive form* assumes the result. An inductive proof needs a different source for the bound.

### 4.2 Confusing positivity of a component with positivity of the target

Gamma-only positivity, a positive Euler comb, positive radiation, an OS norm, and a positive mechanical pencil refer to different objects. At the first prime the arithmetic contribution can repair a negative gamma/pole direction; hence a design demanding that the gamma component remain positive by itself at every length can exclude the intended mechanism.

The same issue appears in the shift variable. Instantaneous shifted-generator positivity is a sufficient condition for cumulative contraction in the range where the energy identity applies. It is stronger than the central Weil criterion. A negative shifted-generator direction is not an RH counterexample. Nor is positive accumulated defect on one selected vector an all-input contraction proof.

An elementary control illustrates the Loewner/Markov trap. Choose \(0<a<b\), and write

\[
K(p)=\frac{p+a}{p-a},\quad B_b(p)=\frac{p-b}{p+b},\quad
\widehat K(p)=\left(1+\frac{2a}{p-a}\right)
\left(1+\frac{2b}{p-b}\right).
\]

Then \(K=B_b\widehat K\); \(\widehat K\) is the Laplace transform of a positive measure in its convergence half-plane \(p>b\); and \(|K(i\tau)|=1\). Yet \(K\) has a right-half-plane pole at \(a\). Thus that package of structural properties does not imply stable all-horizon contraction. This is an elementary counterexample, not a zeta model. It identifies the extra analytic obligation rather than dismissing the useful decomposition.

### 4.3 Forgetting the energy offset

In the finite CCM mechanics, subtracting the smallest eigenvalue gives

\[
T=W-\varepsilon I\ge0.
\]

Replacing \(W\) by \(W+cI\) replaces \(\varepsilon\) by \(\varepsilon+c\), so \(T\) does not change. Any construction depending only on \(T\)—the positive pencil, a string, a chiral square—cannot recover the sign of the original \(\varepsilon\).

This does **not** invalidate the CCM approach. Its alternative route is to construct real-zero approximants and then prove their arithmetic limit is Xi. It does invalidate an inference from positive shifted mechanics to unshifted Weil positivity. See the [founding CCM note](../../ccm-operator-realizations/notes/CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md).

### 4.4 Taking the wrong infinite limit

The program has at least three independent parameters: support \(L\), resolution \(N\), and shift \(\omega\). Geometry and physical regulators introduce further limits.

- Resolving infinitely many Fourier modes at one fixed \(L\) does not enlarge support.
- Increasing \(L\) in a fixed finite trial space does not control all inputs.
- Small-shift convergence on each fixed test does not justify an unproved exchange of \(L\), \(N\), and \(\omega\) limits.
- Stable boundary response, total string mass, or the first few spectral points need not prevent loss of spectral information.

For the CCM free tail, \(L^2/N\to0\) makes that factor disappear; \(L^2/N\to c>0\) instead leaves a Gaussian factor \(\exp(-cz^2/(4\pi^2))\). These facts concern the known free factor alone. A schedule that handles it need not control the arithmetic block. Conversely, when the complete determinant is retained and identified by the exact ground-transform formula, there is no license to discard a tail factor separately.

### 4.5 Estimating away the required cancellation

The repeated architecture is “positive gamma lower bound minus an absolute prime bound.” It pays for large terms independently even where the actual form is extremely small.

The storage-depth barrier argument shows why merely removing a larger finite-dimensional head cannot make the full arithmetic translation norm small on the complement. The newer [CCM bounded audit](../../ccm-operator-realizations/notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md) proves two sharper limitations:

\[
\frac{U_L}{\kappa_L}\ge\frac{L^2}{32}\quad(L\ge2)
\]

for the particular scalar mass upper bound divided by the exact positive odd gap; and cutoff growth at least of order

\[
L\exp(c e^{L/2})
\]

for the specified separate-prime-norm tail test at thresholds bounded below independently of support.

The first is a lower bound on an *upper-bound expression*. It is not a lower bound on the actual trace. Neither statement proves Weil negativity or failure of the true limit. They do show why more precision, a better gap certificate, or optimization inside the same estimate cannot supply the desired support control.

Future estimates should retain the combined arithmetic form, or use a relative comparison adapted to its weak directions. Merely announcing that cancellation must occur is not such an estimate.

### 4.6 Losing boundary terms or choosing an impossible topology

The [finite-response evaluation](../../../susy-positivity/manuscripts/finite-response-weil-positivity/EVALUATION.md) records a boundary correction with essential norm \(\pi/2\). Truncating its mass expansion does not give operator-norm convergence, although fixed finite-input columns can converge and a different image grouping can have an operator-norm remainder.

This essential-norm obstruction does not preclude convergence on fixed smooth tests or the positive-form approximation route in Section 2.

The [positive-factorizations manuscript](../../../susy-positivity/investigations/previous/positive-factorizations/manuscript.tex), Section 9, rules out the specified closable all-support norm factor on ordinary whole-line \(L^2\). That is a warning about the ambient space. It does not rule out finite-interval factors, test-function-topology maps, or appropriate completions. Boundary/contact normalization and the choice of topology are mathematical parts of the problem.

### 4.7 Mistaking numerical fidelity for an explanatory identity

Near-null directions make coefficient accuracy consequential. The first-prime tests show a narrow admissible interval around the arithmetic coefficient. A small fixed perturbation can therefore fail at longer support even if the initial matrices look excellent.

But “the arithmetic must be exact at every approximation stage” is too strong. Independently positive approximants with a proved error tending to zero on every fixed test would suffice. What is excluded by the rigidity arguments is the specified *persistent* perturbation class, not every controlled approximation scheme.

Positive finite Gram matrices, two-precision agreement, or hundreds of passed identity checks do not establish omitted-input bounds or an asymptotic theorem. Conversely, numerical work is valuable when it tests a stated mechanism, exposes a missing term, or distinguishes a relative residual estimate from an absolute one.

## 5. Corrections to overly broad conclusions in the research record

The program has improved through adversarial review, but the reviews also need scope checks.

1. **Tiny margins do not themselves block RH.** A degenerating sequence of positive floors is compatible with positivity on every finite support. It makes absolute-error methods difficult; it does not require a uniform gap that the criterion never asked for.
2. **An empirical ladder is not an asymptotic theorem.** The observed profile \(-\log\lambda_{\min}(L)\) is informative. Two-sided order bounds alone do not establish a pointwise limit for \(\lambda(L+h)/\lambda(L)\), a specified loss at each join, or growth of a chosen coupling norm. Superlinear growth of \(-\log\lambda\), if proved, would exclude a fixed positive ratio lower bound holding at *all* large steps of fixed size; that is a weaker conclusion.
3. **The recorded height scale is not a universal blindness theorem.** Storage-depth's estimate of a scale near \(e^{2L}\) comes from a particular low-mode sensitivity diagnostic. Compactly supported tests can be modulated to high frequencies. A theorem about what the full form can detect would also need assumptions on horizontal displacement, errors and the test family.
4. **The physical no-go results have hypotheses.** The [YM review exchange](../../../susy-positivity/investigations/wilson-loewner/YM/response/CLAUDE_REPLY_TO_RESPONSE_20260925.md) corrects overclaims about derivative sources, smooth pure-point flows, winding intertwiners and positive completions. An arithmetic source translation need not be a preselected native spacetime flow. The [26 September audit](../../../susy-positivity/investigations/wilson-loewner/YM/reviews/FULL_ELECTRIC_AND_BUFFERED_SOURCE_AUDIT_20260926.md) excludes specific fixed-power point sources and strictly buffered finite-order preparations; it does not exclude every distributional source or every continuum model.
5. **A fractional point-count obstruction is not a theorem against all generalized geometry.** The negative coefficients in the tested theta-power interpolation reject that construction. They do not prove that every possible fractional-dimensional interpretation is impossible.
6. **A representation dictionary is not a universal source law.** A jump-kernel presentation of one part of the form does not require every Hilbert-space realization to be literally a Lévy process. A gamma mass tower is a physical energy spectrum only after the relevant coordinate has actually been identified with time.
7. **The detector has a specific unresolved audit issue.** In [rh_detector.tex](../../../misc/rh-detector/rh_detector.tex), the tail is written using \(4\gamma/(\gamma^2-u^2)\,dN(u)\). This is the real-zero-pair contribution. A hypothetical off-axis pair has additional horizontal-displacement dependence. Before calling the resulting tail band unconditional for that diagnostic, bound the omitted displacement correction or state the applicable hypothesis. Likewise, the boundary value of the counting function must come from a certified complete count, not the list whose completeness is being tested. This is a newly identified review concern, not a complete adjudication of the detector paper.

These corrections change the strength of the conclusions, not the practical recommendation to stop repeating already stalled constructions.

## 6. Priority one: the arithmetic ground-state comparison

The newest CCM work has identified the most concrete missing theorem in the current tree. This deserves focused analysis precisely because the elementary realization stage is already understood.

Write \(g_{L,N}\) for the actual finite even Weil ground function, under the finite CCM assumptions. The [bounded audit](../../ccm-operator-realizations/notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md), Sections 5–6, gives

\[
F_{L,N}(z)=
\frac{\int_{-L/2}^{L/2}e^{-izx}g_{L,N}(x)\,dx}
{\int_{-L/2}^{L/2}g_{L,N}(x)\,dx},
\]

\[
\tau_{L,N}=
\operatorname{tr}(K_{L,N}^{-1}M_{L,N})+
\frac{L^2}{4\pi^2}\sum_{n>N}\frac1{n^2}
=\frac12\frac{\int x^2g_{L,N}(x)\,dx}{\int g_{L,N}(x)\,dx}.
\]

The full free tail is included. The second expression is a signed normalized moment, not an established probability variance. The finite positivity assumptions make the spectral trace nonnegative; they do not prove pointwise positivity of \(g\).

This is useful because it replaces an inverse-gap estimate by a concentration question. It is insufficient because generic positive/simple-even systems need not concentrate: the audit's logarithmic toy family has \(\tau=L^2/24\).

The local work derives the following sufficient target. Let \(v_L\) be the normalized prolate-based candidate and \(u_{L,N}\) the normalized actual ground state. Along a suitable sequence,

\[
\|u_{L,N}-v_L\|_2=O(L^{-5/2})
\]

would bound \(\tau\) and identify the real-axis limit, subject to the stated candidate theorem and finite CCM hypotheses. The corresponding residual implementation needs

\[
\frac{r_{L,N}}{\sigma_{L,N}}=O(L^{-5/2}),
\]

where \(r\) is the residual of the projected candidate for the **actual even Weil block**, and \(0<\sigma\le\lambda_2^+-\rho\), with \(\rho\) its Rayleigh quotient and \(\lambda_2^+\) the **second even** eigenvalue. Thus the quotient must lie below that second level. The odd gap is not this separation. A prolate spectral gap cannot be substituted for a Weil gap without proving the comparison.

The power \(5/2\) is sufficient, not necessary. It comes from controlling the second moment by an \(L^2\) error on a growing interval. The candidate itself has a polynomial Fourier-resolution estimate; that does not estimate the true eigenvector error.

The primary [CCM paper, Section 8](https://arxiv.org/html/2511.22755v1#S8), explicitly leaves simplicity/evenness and the true-ground-state/prolate comparison open. Its candidate-transform convergence is not convergence of the actual Weil ground state. Thus the local work has sharpened an existing substantial open step rather than bypassed it.

### A bounded next project

Choose one comparison mechanism and write the residual as an arithmetic identity before running a new support sweep. In the finite even block, set \(W=W_{+,L,N}\), \(v=P_Nv_L/\|P_Nv_L\|\), \(\rho=\langle v,Wv\rangle\), and \(P=|v\rangle\langle v|\). Then

\[
W-\rho I=
\begin{pmatrix}0&b^*\\b&C\end{pmatrix},
\qquad b=(I-P)Wv.
\]

The work is to control \(b\) and the complementary operator \(C\) with their actual prime, gamma, pole and endpoint terms. Possible sources of a useful identity are the semilocal trace formula, Poisson summation in the arithmetic transform, or an approximate intertwining with the prolate operator. These are search locations, not established estimates. In particular, a short norm estimate of the separate terms will reproduce the existing barrier.

**Continue** if this yields a support-dependent relative residual/separation estimate, a useful estimate on the low spectral projection, or a direct normalized-moment bound not already equivalent by definition to the desired conclusion. **Stop or redirect** if it only restates the desired eigenvector closeness or replaces the arithmetic gap by an assumed one.

There is also a less prescriptive sufficient target: normalize \(\widetilde g=g/\int g\) and the Xi kernel \(\widetilde k=k/\int k\), and prove

\[
\|\widetilde g_{L_j,N_j}-\widetilde k\|_{L^1(1+x^2)}\longrightarrow0.
\]

This controls real transforms and second moments directly. Under the finite real-zero determinant hypotheses, the trace bound supplies normal-family compactness and the real-axis identification fixes the limit. Alternatively, exponential weighted \(L^1\) convergence on each weight \(e^{a|x|}\), \(a<1/2\), would supply convergence inside the critical strip directly. These are elementary sufficient conditions; neither has been proved for the actual ground state.

## 7. Priority two: the Sonin residual as an arithmetic bridge

The [archimedean trace-formula paper](https://arxiv.org/abs/2006.13771) relates a positive Sonin compression to the Weil distribution with a correction. The [semilocal prolate paper](https://arxiv.org/abs/2310.18423) proves structural results including stability of semilocal Sonin spaces when places are added. These are concrete mathematical structures to investigate. Stability of a space is not positivity of the full required trace-formula residual.

The repository's [first-prime handoff](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md) correctly identifies a missing comparison rather than requesting another finite append. The old derivation it references is outside this checkout, so it must be recovered or rederived before its formulas are used.

The proposed deliverable is an exact decomposition, in reconciled normalization,

\[
Q_L[f]=P_{S,L}[f]+R_{S,L}[f],\qquad P_{S,L}[f]\ge0,
\]

including contact, pole, endpoint and all active prime-power terms. Here \(S\) is a finite set of places; this formula is a target, not an identity established by this review.

The first-prime window is useful as a *mechanism test*: find where the residual lies on the already known weak directions, and whether it has a relative or one-sided estimate derived from the structure. Do not treat a numerically positive \(R_{S,L}\), or a new certificate for \(Q_L\), as the mechanism.

For a global result there are several possible acceptable outputs:

- a nonnegative residual on every compact test, valid for arbitrary relevant \(S,L\);
- a relative bound \(R_{S,L}\ge-\eta_{S,L}P_{S,L}\) with \(\eta_{S,L}\le1\), derived uniformly in the required family;
- a family of independently positive approximants whose discrepancy tends to zero on each fixed compact test, as in Section 2.

A support-independent strict relative margin is not required. What is required is a quantified passage to the desired form. Adding a prime should be treated as an exact arithmetic operation on the positive structure and its residual. Replacing prime information by a smooth leading density loses precisely the delicate information the existing counterexamples expose; this does not exclude all uses of rigorous prime-counting estimates.

**Continue** if the first-prime derivation reveals a rule that applies when an arbitrary place is added, or identifies a residual estimate with explicit support and place-set dependence. **Stop or redirect** if the proposed “residual theorem” is just the remaining Weil positivity written under a new name, with no additional structure to estimate it.

This and the CCM comparison should be treated as two attempts to extract information from a common arithmetic/prolate structure, not two unrelated projects that repeatedly rebuild the same background.

## 8. Priority three: shrinking joins and canonical systems

The arithmetic-storage fixed-join obstruction is meaningful but leaves shrinking joins open. Its heuristic scale \(h_k\asymp e^{-L_k}\) is compatible with \(L_k\asymp\log k\to\infty\); there is no finite accumulation of support in that model schedule. The scale is motivated by the observed eigenvalue decay, not proved as a necessary or sufficient arithmetic continuation rate.

A viable project would derive a continuous or discrete boundary/Riccati evolution from the exact arithmetic data and prove that it preserves the required cone or form inequality across every prime-power event. It must provide:

1. a positive starting state;
2. an independently justified preservation estimate, including endpoint and jump terms;
3. existence of the evolution for unbounded total support, with no finite-support singularity or stalled step selection;
4. the link back to the full central form or the diagonal transfer criterion.

If \(h_k\) is adaptive, the proof must establish \(\sum h_k=\infty\). Saying that a sufficiently small next step exists is not enough. If a relative margin deteriorates, its cumulative loss must be quantified only to the extent the chosen sufficient route requires.

The inverse-spectral dictionary is available, but it cannot be invoked circularly. Suzuki's [explicit canonical-system construction](https://arxiv.org/abs/1204.1827) is unconditional in its stated \(\omega>1\) construction range; its extension to all positive shifts is a substantive open obligation. This must be distinguished from other innerness/support arguments and their different parameter ranges.

**Continue** if an arithmetic evolution law supplies positivity before the desired innerness or joined-window sign is assumed. **Stop or redirect** if Hamiltonian positivity is simply reconstructed from a positive kernel that has not been proved positive. This route is conceptually attractive but currently less sharply developed than the CCM comparison target.

## 9. How to handle the physics and geometry branches

The physics investigations have genuine outputs: source-domain constraints, exact response calculations, positive storage examples, and failures of particular identifications. Their RH value depends on finding an arithmetic identity that follows from the physics rather than being assigned to an observable.

The latest YM work makes the central distinction explicit. Its signed mixed limits do not give a positive physical norm. Some matching limits are universal over the allowed boundary marginals, which weakens the claim that the match explains anything through Yang–Mills dynamics; other pairings retain state dependence. The one-probe theorem reduces the amount of data to match, but its actual stationary correlation hypothesis already implies RH. An arbitrary Hilbert embedding constructed using the target covariance does not establish physical occurrence.

N4SYM supplies an instructive example of retaining internal storage before elimination. In the tested regime it does not supply the variable arithmetic front and prime-delay law. WZW/Bost–Connes work gives structural and coefficient comparisons, but a positive thermal weight or finite block norm is not the completed arithmetic norm. A Euclidean self-adjoint Gram pairing should be judged against the Weil form; it is not automatically a causal transfer. A retarded response should be judged against the transfer together with its input/output norm, not merely its frequency shape.

For a new physical candidate, require one short feasibility document fixing the observable, parameter action, source domain, positive pairing, arithmetic variable, and matching obligation through an exact identity or a controlled fixed-test limiting identity. For a new geometric candidate, require a prescribed map identifying **both** energy and mass, controlled comparisons across cutoffs (exact compatible refinements are one option), and retained spectral factors. Passing necessary tests is permission to investigate, not evidence of the target identity.

The fractal work is particularly useful as a control: a changing-scale tree can have the right counting order and a finite inverse-square trace while having a different determinant. Conversely, the analytic odd-coordinate Markov obstruction excludes the tested scalar resistance map, not arbitrary two-sheet, nonlocal or transformed geometries. Another geometry is worthwhile only if it gives a specific bound unavailable in the original coordinates.

The existing Ihara/function-field comparisons should also be used as adversarial controls. A proposed mechanism should identify the feature distinguishing a true RH analogue from a false one. If it grants the same claimed conclusion to both, the implication is missing something. There is no requirement that every successful zeta-specific proof also prove every analogue; the value of these controls is to reveal which arithmetic hypotheses are actually used.

## 10. A research plan that would count as progress

I would pause automatic growth of support windows, Fourier cutoffs, physical hierarchies and isospectral realizations. Keep numerical work tied to an explicitly written mathematical question.

| Next work package | Concrete output | Evidence to continue | Evidence to stop or change method |
|---|---|---|---|
| **Arithmetic/prolate comparison** | Exact candidate residual and a candidate-adapted complement estimate, or direct normalized-profile bounds | A new bound with useful support dependence that retains joint arithmetic terms | Separate absolute prime/gamma bounds, assumed Weil gap, or restatement of eigenvector closeness |
| **Semilocal Sonin comparison** | Reconciled full form identity and explicit residual, starting with the first prime | A place-addition rule or fixed-test convergence estimate that survives beyond one window | Another certificate of the same joined form, with no residual mechanism |
| **Shrinking-step continuation** | Arithmetic evolution with a proved invariant and unbounded support schedule | Preservation follows from independent data and total support diverges | Cauchy–Schwarz in an unproved positive enlarged space; steps may accumulate |
| **Reliability work** | Human specialist assessment of selected central lemmas, and clear claims/status ledger | Corrections clarify or strengthen the actual bridge | Large repeated diagnostic campaigns that test only transcribed identities |
| **Optional physics/geometric candidate** | One prescribed source/form map and the estimate it would deliver | A new exact identity or controlled fixed-test limiting identity outside the existing obstructions | Renaming a known positive finite system or fitting arithmetic coefficients |

Before a numerical campaign, record four things: the proposition being investigated, the specific hypothesis being tested, the required error scale/topology, and the result that would stop the campaign. An experiment testing an asymptotic residual ratio can be useful; it should be reported as evidence about that ratio, not as a finite fragment of an unproved infinite theorem.

The most promising consolidation is to bring the near-null-vector observations, semilocal trace formula and CCM ground-state comparison into one arithmetic question. The repeated success of prolate ideas identifies a meaningful place to search. The repeated failure of absolute estimates identifies what that search must preserve. The next substantial advance would be a new arithmetic comparison or preservation theorem—even a limited one that demonstrably changes the support dependence—not a longer list of positive finite matrices.

## 11. Verification and limits of this review

The review reconciled current indexes against later dated notes, inspected the decisive identities and obstruction scopes, and used three parallel readings of the foundations, earlier SUSY branches, and current CCM/geometric work. It checked primary-source scope for Suzuki, CCM and the Sonin/prolate literature. It did not rerun the large certificate pipeline, certify new eigenvalue bounds, audit every historical draft, or establish a new RH implication beyond the elementary sufficient-condition explanations stated here.

The repository contains substantial internally checked material but still needs human mathematical review of the claims selected for further development. That limitation is relevant to confidence in the present premises; it is not the reason the all-support problem remains open. Even accepting the strongest current local claims, the missing arithmetic bridge identified above remains.
