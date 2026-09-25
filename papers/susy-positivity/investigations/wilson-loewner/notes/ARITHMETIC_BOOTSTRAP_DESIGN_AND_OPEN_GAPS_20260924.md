# Arithmetic bootstrap: design, existing inputs, and the missing bridge

Date: 24 September 2026, America/New_York.
Prepared for Edward Baker with LLM assistance.
Model: GPT-6 (Codex). Reasoning-effort setting: not exposed; not inferred.
Baseline: repository commit 520a859b7f73fea9e314debdecabd45439b3fcb1, with the preceding arithmetic-bridge sweep as an uncommitted note.
Status: explanation and proposed investigation, before implementation. No new numerical bootstrap, positivity interval, or RH result is reported.

## 1. What the proposal means

An arithmetic bootstrap would use exact arithmetic and Fourier identities together with positivity of ordinary Hilbert-space Gram matrices to constrain the signed Weil form. Increasing the family of observables would impose more simultaneous consistency conditions. The intended output is a mathematical certificate or new inequality, not merely a positive numerical matrix.

The analogy with the lattice bootstrap concerns the method. The known lattice approach combines positive inner products with loop equations and trace identities. Those equations constrain correlations that positivity alone leaves undetermined. [Kazakov–Zheng, finite-N lattice bootstrap](https://arxiv.org/html/2404.16925v2).

There is no fully specified arithmetic counterpart ready to solve in the earlier proposal. In particular, we have not identified the identity playing the role of a loop equation that controls the joint gamma–prime contribution. Finding that identity, or showing why a selected algebra cannot supply it, is the first research task.

The Weil form's coefficients are already explicit. A bootstrap would not discover their numerical values. It would expose a reason they jointly produce a nonnegative quadratic form.

## 2. The exact objective

Use the pole-neutral smooth class
\[
\mathcal D_L^0=\{f\in C_c^\infty(-L/2,L/2):
\int e^{x/2}f(x)dx=\int e^{-x/2}f(x)dx=0\}.
\]
On this class, with \(F\) the zero extension,
\[
Q_L[f]=K_\Gamma[F]+w_0\|F\|^2
-2\sum_{m\log p<L}(\log p)p^{-m/2}
\operatorname{Re}\langle F,U_{m\log p}F\rangle.
\]
Here \(U_aF(x)=F(x-a)\), \(w_0=\psi(1/4)-\log\pi\), and \(K_\Gamma\) has Fourier multiplier
\[
b(\tau^2)=\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).
\]
Positivity on \(\mathcal D_L^0\) for every \(L\) is RH-equivalent, by the prescribed Mellin-vanishing criterion. [Connes–Consani, Appendix C](https://arxiv.org/html/2006.13771v1).

A useful long-term objective is a family of certificates
\[
Q_L[f]\ge b_{k,L}\|f\|^2,\qquad f\in\mathcal D_L^0,
\]
where \(k\) labels the level of the hierarchy. Every claimed lower bound must be valid on the stated source class. We would need a theorem establishing nonnegative bounds or a nonnegative limit for every finite \(L\). A generic convergence theorem for an optimizer does not establish that its limiting optimum is nonnegative.

This direct-form goal avoids requiring a native causal device or a literal YM realization. It still requires the exact contact, prime repetitions, domains, and all-length implication.

## 3. Two versions should be distinguished

### 3.1 Bootstrap the input state of the actual Weil operator

The Hilbert space is the known \(L^2(\mathbb R)\), the state is
\[
\omega_F(A)=\langle F,AF\rangle,\qquad \|F\|=1,
\]
and the operators include translations, Fourier multipliers, and support projections. The source satisfies the two pole constraints.

The source constraints also have a bounded-operator formulation. Let \(S_L\) be multiplication by the interval indicator and \(R_L\) the orthogonal projection onto the span of \(1_{I_L}e^{x/2}\) and \(1_{I_L}e^{-x/2}\). Then a normalized source obeys
\[
\omega_F(S_L)=1,\qquad \omega_F(R_L)=0.
\]
These encode support and pole neutrality. Smoothness and finiteness of the gamma form are separate domain conditions.

We seek lower bounds on the actual quadratic form using moments of these operators. The unknowns are correlations of the arbitrary input \(F\), rather than unknown coefficients of the target. Constraints come from genuine operator relations, support, Fourier duality, and the source restrictions.

This version is concrete. It is also close to existing operator lower-bound methods; its value would be a stronger joint estimate or a symbolic certificate reusable beyond one finite matrix calculation.

### 3.2 Construct an arithmetic state whose source pairing realizes the form

Here the ambient algebra is independently arithmetic: for example, a Bost–Connes algebra or a semilocal adelic Fourier space. One seeks a linear preparation \(f\mapsto A_f\) and an identity such as
\[
Q_L[f]=\varphi(A_f^*A_f)
\]
or a comparison with an explicitly controlled remainder.

The state and its positivity must be established independently. The preparation cannot be defined as an assumed positive square root of \(Q_L\). Nor can it be separately fitted for each source.

This is the more ambitious physical/algebraic interpretation of the original sketch. The missing gamma–prime identity appears before the optimization stage.

**Recommendation:** use the first version as a precise diagnostic and certificate language while investigating the second. They need not be separate projects. An arithmetic identity from the second version could become a new valid constraint in the first.

## 4. A concrete moment matrix

For normalized \(F\), define
\[
z_q=\langle F,U_{\log q}F\rangle,\qquad q\in\mathbb Q_{>0}.
\]
The three vectors \(F,U_{\log2}F,U_{\log3}F\) have Gram matrix
\[
M=
\begin{pmatrix}
1&z_2&z_3\\
\overline{z_2}&1&z_{3/2}\\
\overline{z_3}&\overline{z_{3/2}}&1
\end{pmatrix}\succeq0.
\]
This is an unconditional identity for ordinary Hilbert vectors. Translation composition gives the ratio entry. Compact support gives
\[
z_q=0\quad\text{if }|\log q|\ge L.
\]

The Weil objective uses selected \(z_{p^m}\), together with the gamma expectation. Higher moments connect them to repeated shifts, mixed shifts, and real-place observables.

Two points matter:

- A ratio correlation such as \(z_{3/2}\) is a legitimate auxiliary variable. Its absence from the final Weil formula does not imply it vanishes.
- Bounding each \(|z_q|\) separately discards the joint information in the matrix. The purpose of the hierarchy is to retain information that separate Cauchy–Schwarz estimates lose.

For a larger word family \(\mathcal W_k\), introduce
\[
M^{(k)}_{u,v}=\omega_F(u^*v).
\]
Each genuine input produces a positive matrix satisfying all independently derived constraints. Optimizing over a larger, relaxed set therefore gives a lower bound, provided the objective and approximation errors are correctly represented. A negative relaxed bound is evidence that the relaxation has not proved enough, not a negative Weil test.

### Keeping the gamma sector in the same problem

Put \(a_j=2j+1/2\). The elementary digamma expansion gives
\[
b(\tau^2)=2\sum_{j\ge0}\frac{\tau^2}{a_j(a_j^2+\tau^2)}.
\]
With \(P=-i\partial_x\), each summand is a nonnegative bounded function of \(P\); the series defines an unbounded logarithmic quadratic form. This offers resolvent observables sharing the same input as the translations.

Dropping a positive tail gives a lower approximation, but does not automatically give a sufficiently sharp one. The contact \(w_0\) remains fixed. Existing gamma-domain and tail estimates should be reused.

The translations and gamma multiplier commute on the full line. The support restriction and its Fourier consequences are essential additional structure. A relaxation that allows an arbitrary spectral measure without the support and source constraints can solve a different problem.

## 5. What arithmetic algebra already gives

In the integer representation,
\[
V_n|m\rangle=|nm\rangle,\qquad H|m\rangle=(\log m)|m\rangle.
\]
On a suitable core,
\[
V_mV_n=V_{mn},\quad V_n^*V_n=I,\quad
[H,V_n]=(\log n)V_n.
\]
Range projections \(e_n=V_nV_n^*\) obey
\[
e_me_n=e_{\operatorname{lcm}(m,n)}.
\]
The bounded-operator dynamics is
\(\sigma_t(V_n)=n^{it}V_n\). This is preferable to presuming that the same unbounded Hamiltonian and trace representation work in every thermal sector.

Positive Bost–Connes equilibrium states exist for \(0<\beta\le1\); they are not obtained by normalizing a divergent Gibbs trace. [Neshveyev](https://arxiv.org/html/0907.1456).

The repository's 23 September Bost–Connes note derives
\[
\varphi_\beta(e_n)=n^{-\beta},\qquad
\varphi_\beta\!\left(\prod_{p\mid n}(1-e_p)\right)
=\prod_{p\mid n}(1-p^{-\beta}).
\]
It already matches the coefficients of the shifted Euler transfer, with an explicitly separate centering factor. For the central coefficient alone, one can also write
\[
(\log p)p^{-m/2}=(\log p)\varphi_{1/2}(e_{p^m}).
\]
This is an exact coefficient dictionary, not a Gram representation of \(Q_L\).

The auxiliary choice \(\beta=1/2\) in the last display must not be confused with the earlier transfer dictionary \(\beta=2\omega\). The central-form limit \(\omega\to0\) is not justified by setting the latter thermal parameter to \(1/2\).

### Additive structure is important

The simple multiplicative skeleton is too generic: analogous isometries and assigned energies can be built for arbitrary prime-labelled oscillators. It does not explain the relation to the real-place gamma factor.

The full arithmetic algebra is richer. For example, on the integer representation,
\[
T_r|m\rangle=e^{2\pi imr}|m\rangle,\qquad r\in\mathbb Q/\mathbb Z,
\]
satisfies
\[
T_rT_s=T_{r+s},\qquad V_n^*T_rV_n=T_{nr},
\]
and
\[
V_nT_rV_n^*=\frac1n\sum_{ns=r}T_s.
\]
These equations follow directly by acting on the integer basis. They encode additive residue structure and its interaction with divisibility. The full Bost–Connes setting already contains such structure; it would be misleading to describe it as only a collection of independent oscillators.

The unresolved step is relating those finite-place identities to the correct real-place source and pairing.

## 6. A specific limitation of the simplest thermal Gram ansatz

**Elementary deduction, not a new literature theorem.** Let \(\varphi\) be any normalized state invariant under \(\sigma_t\). Then
\[
\varphi(V_m^*V_n)
=(n/m)^{it}\varphi(V_m^*V_n).
\]
For \(m\ne n\), invariance for every \(t\) forces this expectation to vanish. For \(m=n\), it equals 1. Therefore
\[
\varphi(V_m^*V_n)=\delta_{mn}.
\]
Consequently, a finite source \(A_f=\sum_n a_n(f)V_n\) has
\[
\varphi(A_f^*A_f)=\sum_n|a_n(f)|^2.
\]
The bare different-frequency isometries do not provide the desired inter-label interference. Artificially fitting the coefficient maps to factor \(Q_L\) would reinstate the original problem.

This does not exclude the full algebra, different preparations, or a coupled real-place state. It identifies an ansatz that is too small.

One possibility is to pair an arithmetic operator with a real-place operator of opposite flow weight, yielding a flow-neutral composite that can have nonzero cross correlations in an invariant state. This is a proposal: neither the suitable joint state nor the Weil identity follows from frequency balancing alone.

Another possibility is the input-state bootstrap of Section 3.1, whose arbitrary compactly supported input is not a thermal invariant state. The matrix in Section 4 is therefore not contradicted by this thermal selection rule.

## 7. What has already been tried, and what a bootstrap must add

| Existing construction | What it accomplished | Remaining obstruction |
|---|---|---|
| YM reflected Gram construction | An independently positive state space with a specified adjoint | No arithmetic operator/source dictionary |
| Bost–Connes primitive projections | Exact positive primitive probabilities and shifted Euler coefficients | Joint archimedean pairing and amplitude interpretation |
| Finite Euler partition functions | Correct primitive repetitions and removal of mixed composites under a logarithmic derivative | A logarithmic derivative is not automatically a positive quadratic form |
| Independent prime delay squares | Desired signed cross term inside a positive square | Extra diagonal cost cannot simply be debited from a separately positive gamma sector |
| Naive coherent multi-prime amplitudes | Shared positive ambient norm | Additional mixed-ratio correlations appear in the resulting quadratic form |
| Scalar coherent derivative deformations | Correct leading singularity in some regimes | Continuous remainder and, at finite coupling, wrong repetition coefficients |
| Semilocal Fourier/Sonin spaces | Canonical positive norms and exact finite-place maps | Signed Weil comparison remainder and changing metric |
| Schur elimination and short-window certificates | Rigorous local positivity and explicit responding inputs | No all-length arithmetic continuation law |

The project failure inventory gives scoped failures, not a no-go theorem for every arithmetic bootstrap.

For example,
\[
Z_{\{2,3\}}(s)=\frac1{(1-2^{-s})(1-3^{-s})}
\]
already satisfies
\[
-\partial_s\log Z_{\{2,3\}}(s)
=\sum_{m\ge1}(\log2)2^{-ms}
+\sum_{m\ge1}(\log3)3^{-ms}
\]
in its convergent half-plane. There is no mixed \(6^{-s}\) term. This is a known Euler-product identity. Reproducing it would not constitute the new bootstrap mechanism.

The elementary Möbius identity
\[
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d)
\]
also produces the repeated-prime weight and composite cancellation. The missing accomplishment is making that cancellation occur in the same independently positive, correctly normalized source pairing as the gamma term.

Likewise,
\[
c\|F-U_dF\|^2=2c\|F\|^2
-2c\operatorname{Re}\langle F,U_dF\rangle
\]
already explains how negative cross terms can occur in a positive norm. The compulsory diagonal term is exactly why the independent-prime solution was incomplete.

A tensor product of independently positive gamma and arithmetic states usually multiplies correlations; a direct sum adds positive forms. Neither operation automatically produces the required signed completed sum.

## 8. The missing identity: plausible places to look

### A. Joint Fourier and scaling identities

The real and finite places admit normalized Fourier transforms and scaling actions with exact intertwining relations. Semilocal adelic spaces implement them on a common space, including maps between different sets of places. Their metrics change under place-adjoining; compatibility is not isometry. [Connes–Consani–Moscovici](https://arxiv.org/html/2310.18423v1).

A promising bootstrap would use words containing both scaling and Fourier/cutoff operations, and derive mixed identities before applying positivity. The target is a relation involving the actual signed comparison remainder.

It is reasonable to borrow this operator algebra while retaining a bootstrap research objective. That does not require committing in advance to the previously proposed Sonin domination inequality.

### B. Divisibility projectors, additive characters, and primitive cancellations

Products \(\prod_{p\mid n}(1-e_p)\) are positive projections whose expansions contain signed Möbius coefficients. Additive characters provide further exact identities. This is a concrete source of signed terms inside a positive construction.

A useful result would show how an energy/scaling insertion and these projectors create the desired prime-power contributions while preserving the full diagonal normalization in a joint real-place form. An unconstrained derivative of a positive metric or thermal state is not enough.

### C. The actual operator residual

One may keep the explicit Weil operator and seek a decomposition into ordinary squares modulo valid arithmetic/Fourier relations, with a controlled remainder. Burnol's conductor operators provide a place-by-place explicit-formula dictionary, but do not themselves establish positivity. [Burnol](https://arxiv.org/abs/math/9902080).

This option has the clearest diagnostic: does adding a specific relation improve a rigorous bound compared with the same moment system without it? It may establish a useful inequality without yielding a complete physical realization.

These are candidate mechanisms, not three established solutions. The common requirement is that a real arithmetic identity controls the signed gamma–prime interaction.

## 9. What a certificate would look like

For a fixed source class, a schematic successful certificate is
\[
Q_L[f]-\lambda\|f\|^2
=\sum_j\|B_jf\|^2+\sum_r\mathcal I_r[f]+\mathcal E[f],
\]
where every \(\mathcal I_r\) is proved to vanish on that class and the remainder satisfies a proved lower bound. If \(\mathcal E\ge-\epsilon\|f\|^2\), the result is \(Q_L\ge(\lambda-\epsilon)\|f\|^2\).

The equations and positive blocks used in finding the certificate must be independently valid. Setting \(Q_L\) itself equal to a required positive moment matrix assumes the desired conclusion unless the equality is independently derived.

Some relations are operator identities and can be inserted inside arbitrary admissible words. Others hold only after taking expectation. They require separate handling. In particular, a KMS state is not generally tracial: unrestricted cyclic permutation of its factors is invalid.

The established theory of noncommutative moment relaxations supplies monotone bounds under boundedness hypotheses and offers dual sum-of-squares certificates. It does not automatically apply to this unbounded arithmetic problem. [Pironio–Navascués–Acín](https://arxiv.org/html/0903.4368).

A floating-point optimum is a candidate certificate. Its sign, residual, and analytic tails would need exact or interval verification.

## 10. Main difficulties and how to recognize them

1. **Insufficient constraints.** Generic Gram positivity may permit many fake moment assignments. A negative relaxed optimum does not identify a genuine negative Weil input.
2. **Overstrong or circular constraints.** Positivity of the Weil distribution, innerness of the small-shift zeta ratio, or the desired norm identity cannot be assumed.
3. **Finite matrices versus finite representations.** A finite moment matrix may describe infinite-dimensional operators. A proper isometry cannot be represented exactly by a finite square matrix: finite-dimensional \(V^*V=I\) forces \(VV^*=I\). Hard occupation cutoffs therefore alter the arithmetic relations unless the boundary defects are retained.
4. **Unbounded operators and domains.** Logarithmic energy, gamma multipliers, derivatives, and point evaluation require a specified common core and form bounds. Bounded unitary flows or resolvents can help, but recovering the generator still requires estimates.
5. **Contacts and normalization.** An extra positive diagonal term proves positivity of a different form. The joint completion must retain the original scalar contact.
6. **Correct variables.** A thermal energy difference \(\log n\) is not automatically a propagation delay. The direct-form project can avoid a causal interpretation, but still needs an exact map to source translations.
7. **Critical sensitivity.** Existing prime-weight tests show that small independent coefficient errors can matter. This supports exact coefficient identities and retained correlations, not an assumption of a uniform gap.
8. **Several limits.** Source dimension, word degree, gamma approximation, and arithmetic representation cutoffs are different. Their errors and order of removal must be stated separately.
9. **All support lengths.** For fixed \(L\), only finitely many prime powers enter the target. This does not make the auxiliary arithmetic space finite, and a finite list of successful \(L\)'s does not imply RH.

## 11. Proposed first investigation

### Step 1: write a complete specification before choosing a solver

Fix the pole-neutral source class and the normalization above. Distinguish the input-state problem from the auxiliary arithmetic-state realization. List every operator, adjoint, state, and source map, and mark each identity as established, derived, or conjectural.

Deliverable: a short specification in which the objective is explicitly expressed in the chosen moments. If that expression is missing, the bootstrap is not yet defined.

### Step 2: build the smallest faithful algebraic examples

For the input version, start with the Gram family \(F,U_{\log2}F,U_{\log3}F\), retaining the ratio moment, support relations, and shared gamma observables. For the arithmetic version, use the established divisibility/additive-character relations and identify the proposed real-place coupling.

Reproduce known coefficient identities as calibration. Do not count them as the new result. Use the thermal orthogonality calculation to reject the bare \(V_n\) Gram ansatz.

Deliverable: a common list of actual relations that survives the adjoint, support, and contact checks.

### Step 3: require one genuinely informative mixed identity

Look for an identity involving both a real-place operator and an arithmetic operator that constrains the troublesome cross term or comparison remainder. Candidate sources are Fourier/scaling intertwining, primitive-projector expansions, and a carefully derived expectation identity.

Deliverable: an exact identity with a demonstrable consequence beyond separate positivity of its components, or an explicit obstruction showing why the chosen algebra is too weak.

### Step 4: only then formulate a small optimization

Use a finite source family \(f_i=(-\partial_x^2+1/4)h_i\), with smooth compactly supported \(h_i\), when a finite diagnostic is useful. Compare constraints added successively: Gram positivity, exact relations, support, and the new mixed identity.

Test \(L=1\), \(1.25\), and \(1.5\) as distinct arithmetic regimes. At \(1.5\), the prime square 4 is active. To test absence of the coefficient at 6, work algebraically before imposing the support cutoff or use \(L>\log6\) with prime 5 included. Below \(\log6\), support alone hides that coefficient and cannot test its cancellation.

Deliverable: a verified improvement or a validated dual certificate, with all remaining analytic errors explicit. A source-family result must not be called full-window positivity.

### Step 5: decide whether to continue

Continue if the new relation supplies a reusable mechanism, a useful rigorous bound, or a certificate pattern with a plausible analytic extension. Reconsider the architecture if all gains come from enlarging a matrix already equivalent to the original spectral problem, or if essential relations only restate the desired sign.

Do not start an all-prime or large-window campaign before this decision. The first success should be a new relation controlling the completed arithmetic form.

## 12. Local references

- [Preceding sweep](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/notes/ARITHMETIC_BRIDGE_SWEEP_AFTER_YM_20260924.md).
- [Bost–Connes coefficient and norm tests](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/WZW/notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md).
- [Scoped failure inventory](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/brainstorm/candidate-bulk-theories/FAILURES.md).
- [Current reflection and hierarchy assessment](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/notes/UPDATED_PATH_ASSESSMENT_REFLECTION_AND_HIERARCHIES_20260924.md).
- [First-prime closure and weight rigidity](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md).

The proposal is worth investigating because it can retain arithmetic correlations that separate norm estimates erase. Its current uncertainty is structural: we have several correct positive arithmetic ingredients, but not yet the joint identity that would turn their positivity into the Weil inequality.
