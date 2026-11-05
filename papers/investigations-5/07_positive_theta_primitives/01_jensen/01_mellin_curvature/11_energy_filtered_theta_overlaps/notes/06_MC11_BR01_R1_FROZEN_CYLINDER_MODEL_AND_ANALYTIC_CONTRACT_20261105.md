# MC11-BR01 r1: frozen cylinder model and analytic contract

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), actual recorded effort max**. Thread `01a1aa32-c540-7671-aa14-f080cfbedd5d`, MC11 history0004. **B — brainstorm**, request r1; sole writer, no delegated assessment.

**Decision: select the complete radius-1/2 product cylinder, its free squared Dirac operator, no wall, zero potential, and a heat-damped radial-diagonal Green response at one fixed probe.** Recover the entire original filter family by an explicitly external angular insertion. Keep the source evaluation external. One additional class—bounded nonnegative scalar radial potentials—is frozen solely for AR-E02's rigidity/defect theorem; it does not replace the selected zero potential. The Euclidean spherical readout is deferred, not ruled out.

This completes the model choice. The prospective theorems in §§5–6 are **execution requests, not completed or assessed results**. The accepted free identities remain those of [AR-E01 Note05](05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md) and [Assessment03](../reviews/03_MC11_AR_E01_R1_ANGULAR_RADIAL_IDENTITY_ASSESSMENT_20261105.md), including R1. [Register02](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) alone owns status; the [activation versions](../research-progress/handoffs/06_MC11_BR01_R1_INPUT_VERSIONS_20261105.json) identify this decision's inputs.

| Next task | Type | Recommended model | Dependency | Deliverable |
| --- | --- | --- | --- | --- |
| **MC11-AR-E02 — default next** | E | **Sol**, fixed one-dimensional resolvent comparison | Ready from this frozen contract | Complete-sum response defect and exact-recovery rigidity in the one selected potential class |
| MC11-AR-E03 | E | **Sol**, fixed source differentiation and integration by parts | Successful relevant E02 return | Arbitrary-index source and pairing theorem, including endpoint terms |
| MC11-B01 — retained alternative | B | **Astra**, signed-estimate choice remains open | Independently ready from E04; default angular route consumes E02/E03 | One noncircular E05 lemma or scoped stop |

## 1. What the decision optimizes

The immediate question is a coherent realization of the unchanged source, including the filter path used by MC11. It is not a finite partition function, a bound state construction, or a signed-determinant theorem. The cylinder supplies the inverse multiplicity through an actual radial response; its angular gap makes the response well defined without confinement. This resolves the role of radial propagation and the meaning of the observation. It does not derive the source's external sampling law or prepare its auxiliary vectors physically.

AR-E01 already proves the free Green identity. Repeating that proof would not be a new task. E02 instead asks whether the chosen readout can survive a nonnegative bounded local potential, and freezes a quantitative all-index defect with which to answer that question. No potential is fitted to theta coefficients. E03 then closes the source/domain/endpoint dictionary once. A useful signed estimate remains a separate B01 decision.

Under [avoid/01](../../../../../../../avoid/01_restating_the_target.md), this is a **model-selection and representation contract**, not an RH criterion or an acquired determinant milestone. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern that classification.

## 2. Exactly two compared contracts

Write K=L²(S²,Σ;dΩ), with the complex rank-two spinor bundle, unit-sphere self-adjoint Dirac D, chirality Γ, and projections P_n onto D²=n². Both signs ±n are retained, with dim P_nK=4n. The spectral convention is the one accepted by AR-E01 and rechecked in [Camporesi–Higuchi v1, §3.1 and (3.54)](https://arxiv.org/html/gr-qc/9505009). Put W=(4|D|)⁻¹ and B_s=P_1+s(I-P_1), 0≤s≤1.

| Item | C: complete cylinder — selected | E: Euclidean spherical readout — deferred |
| --- | --- | --- |
| Configuration and bundle | R_v×S², metric dv²+g_S²/4; pullback of Σ | R³ with its usual metric and complex rank-two spin bundle; polar description for r>0 |
| Measure | Metric volume dv dΩ/4, unitarily represented as H_C=L²(R,dv;K) by a constant spinor normalization | d³x=r²dr dΩ; reduced spinors rψ have measure dr dΩ |
| Kinetic operator | L_0=D_C², D_C=-iΓ∂_v+2D; explicit self-adjoint direct sum below | Free Pauli square H_E=(-iσ·∇)²=-Δ I on H²(R³;C²), the usual whole-space realization |
| Radial domain and boundary | Complete line; no wall or extension parameter; probe v=0 is an interior point | r∈(0,∞), regular origin inherited from the whole-space operator, no exterior wall. Reduced channels are Friedrichs realizations of -∂_r²+n(n±1)/r²; the n=1 lower channel uses the regular/Dirichlet reduced condition |
| Potential | Selected V=0; one additional comparison class 0≤V∈L∞(R), added to L_0 only | V=0 only; no Euclidean potential survey |
| Observation | Tr_K[B_s e^{-tD²}K_{L_0^{-1}}(0,0)] | S_s(t,r)=Tr_K[B_s W e^{-t(D/r)²}], a sphere's angular spectral readout, not the radial Green kernel of H_E |
| Independent evolution | τ>0 in e^{-τL_0}; t>0 is separate angular damping | τ>0 in e^{-τH_E}; t>0 is separate angular damping at the selected sphere |
| Source recovery | R_0,s(t)=Q_s(t); use the external map in §3 | S_s(π,r)=Q_s(π/r²). Unmodified Jacobi recovery gives A_1(r), with its harmonic correction, only at s=1 |
| Radial accounting | The complete radial momentum integral is retained in the Green diagonal | No radial trace is taken or claimed. A full H_E thermal trace cannot be substituted for this angular observable |

The Euclidean choice above is sufficiently fixed to compare; its whole-space realization is a proposed standard domain choice here, not an extension of AR-E01's formal-domain acceptance. No Euclidean Green theorem is claimed or assigned. Its frozen angular readout uses **dimensionless W fixed**, not (4|D/r|)⁻¹=rW. The latter would multiply S_s by r. This retains R1 rather than absorbing it into a normalization.

At s=1, [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) gives
\[
A_1(r)=r^{-1}Q_1(\pi/r^2)+(r^{-1}-1)/2,\qquad r>0.
\]
AR-E01 Note05 (21) records the nonzero filtered defect for s≠1. An additional explicit correction could recover that family too, but is not the unmodified modular law. Moreover the Euclidean angular weight is an inserted readout rather than a weight derived from its selected radial operator. These are the reasons for deferral. There is no impossibility claim about Euclidean models, other boundaries, or other observations.

## 3. Frozen selected model C0

All units below are dimensionless; no physical mass or temperature is inferred from the old box energies πn². In the representation H_C=L²(R,dv;K), Fourier transformation in v gives
\[
\widehat{\mathcal D_C\psi}(k)=(k\Gamma+2D)\widehat\psi(k),\qquad
L_0=-\partial_v^2+4D^2,
\]
\[
\operatorname{Dom} L_0=
\left\{\psi:\sum_{n\ge1}\int_{\mathbb R}(k^2+4n^2)^2
\|P_n\widehat\psi(k)\|_K^2\,dk<\infty\right\}.
\tag{1}
\]
Dom D_C uses the first power of k²+4n². These are the accepted full-line domains. The metric-volume spinor corresponding to ψ in this normalized representation is 2ψ. There is no angular multiplicity adjustment. L_0≥4I, so its inverse is bounded; no confining potential is needed for this observable. The spectrum includes continuous radial momentum k, not a second discrete index silently equated with n. P_1 is the lowest **angular shell**, not a normalizable full-cylinder ground state.

Fix the probe v_*=0 once and for all. It is independent of the source variable u. For a potential in the comparison class of §5 let
\[
R_{V,s}(t)=\operatorname{Tr}_K[B_s e^{-tD^2}K_{L_V^{-1}}(0,0)],\qquad t>0.
\tag{2}
\]
At the selected V=0,
\[
K_{L_0^{-1}}(0,0)=W,\qquad
R_{0,s}(t)=\sum_{n\ge1}a_n(s)e^{-tn^2}=Q_s(t),\quad
 a_1=1,\ a_n=s\ (n\ge2).
\tag{3}
\]
The kernel diagonal is operator-valued on K. It is not insertion of an unrestricted L² point-evaluation map into a full-space trace. W is positive and bounded, but has infinite trace and is not a density matrix. The only filter is the stated external B_s; there is no compensating n-dependent normalization after V or a boundary is changed.

The physical heat/evolution parameter is **τ**, independent of **t**. At V=0 the complete radial integral is
\[
G_{n,0}(0,0)=\int_{\mathbb R}\frac{dk}{2\pi(k^2+4n^2)}
=\int_0^\infty\frac{e^{-4\tau n^2}}{\sqrt{4\pi\tau}}\,d\tau
=\frac1{4n}.
\tag{4}
\]
Thus the proper-time form of (2) contains all radial propagation. Its radial diagonal is used before the angular trace; integrating the latter over all v would diverge. It is a static Green response with angular heat damping, not a finite three-dimensional thermal partition function or a first-order Dirac propagator. The latter has the additional D_C numerator.

The unchanged source map is frozen as an **external observation**:
\[
t(u)=\pi e^{4u},\quad u\ge0,\qquad
p_s(u)=e^u R_{0,s}(t(u)),\qquad
\Phi_s(u)=\frac{(\partial_u^2-1)p_s(u)}8.
\tag{5}
\]
Neither τ=t nor v=u is imposed in (2)–(5). The symbol r=e^{2u} remains a source parameter; it is not the physical radius of the cylinder, which stays 1/2. This contract derives no position-dependent temperature law. The e^u factor and the differential observation are external too. Precisely this separation lets a fixed-probe response have constant shell coefficients and prevents hidden derivatives of a moving probe.

No radial half-line boundary is chosen. Restricting the source integrals to u≥0 does not restrict the physical operator to v≥0. AR-E01's Dirichlet/Neumann image terms are therefore not being discarded or canceled by source evenness.

## 4. Scalar-to-spinor encoding

Keep the auxiliary source space h=L²((0,∞),du) with its ordinary measure and conjugate-linear first slot. Fix a unit smooth eigenspinor χ∈K with Dχ=χ, for example the J_z=+1/2 state in that eigenspace, up to a harmless phase. It is a global section, not a parallel or angularly constant spinor. For comparison with physical spinors use the explicit isometry
\[
(Jf)(v,\omega)=\begin{cases} f(v)\chi(\omega),&v>0,\\0,&v<0.\end{cases}
\qquad \langle Jf,Jg\rangle_{H_C}=\langle f,g\rangle_h.
\tag{6}
\]
Here identifying the numerical integration coordinate with v is only the definition of a Hilbert-space embedding; it is not the observation rule (2). The physical metric-volume field has the extra constant factor 2 noted above. Choosing χ fixes a spin frame for this auxiliary pure-state encoding; the trace (2) still retains all angular states and is not replaced by a rank-one expectation.

This zero extension imposes no boundary on L_0, whose full domain stays (1). An embedded function with nonzero trace at v=0 need not belong to Dom D_C or Dom L_0. Only Hilbert membership and pairings are claimed. No Hamiltonian eigenstate or finite-energy preparation claim is made for these vectors; requiring one would reopen BR01. The induced exterior-power maps preserve pairings. A constant parallel spinor on S² is not assumed.

## 5. AR-E02 r1 — intended theorem and fixed route

**E — execution; recommended Sol; ready, unstarted.** Reuse (1)–(4) at V=0. The only added operator class is
\[
\mathcal V_+=\{V\in L^\infty(\mathbb R;\mathbb R):V\ge0\text{ a.e.}\},\quad
M=\|V\|_\infty,\quad L_V=L_0+V(v)I,
\tag{7}
\]
with Dom L_V=Dom L_0. V is independent of n,s,t,u. It is a second-order scalar potential: no assertion identifies L_V with (D_C+V)². The class is bounded and does not cover potentials diverging at infinity, singular walls, angular-dependent or signed potentials. Confinement was not required by C0; the theorem below must not be advertised as excluding every confining realization.

**Requested all-index statement.** Prove existence and positivity of the channel Green kernels for
\[
H_{n,V}=-d^2/dv^2+4n^2+V(v),\quad \operatorname{Dom}H_{n,V}=H^2(\mathbb R),
\quad b_n(V)=4nG_{n,V}(0,0),\quad d_n=1-b_n,
\]
and, for every n≥1,
\[
\frac{2n}{\sqrt{4n^2+M}}\le b_n\le1,\qquad
0\le d_n\le1-\left(1+\frac{M}{4n^2}\right)^{-1/2}
\le\frac{M}{8n^2}.
\tag{8}
\]
If V is not zero a.e., the requested rigidity is d_n>0 for **every** n at this probe. Consequently, for all 0≤s≤1 and t>0,
\[
R_{V,s}(t)=\sum_{n\ge1}a_n(s)b_n(V)e^{-tn^2},\quad
\Delta_{V,s}(t)=Q_s(t)-R_{V,s}(t)
=\sum_{n\ge1}a_n(s)d_ne^{-tn^2},
\tag{9}
\]
with exact recovery at even one such (s,t) only when V=0 a.e. The retained a_1=1 matters, including at s=0. For every fixed m≥0 require
\[
0\le(-1)^m\partial_t^m\Delta_{V,s}(t)
\le\frac M8\sum_{n\ge1}a_n(s)n^{2m-2}e^{-tn^2}.
\tag{10}
\]
The remainder after n≤N obeys the same bound with n>N. It is uniform for t≥ε>0 and s∈[0,1], at each fixed m; no uniformity in m or t↓0 is asserted. Include termwise s differentiation (the series is affine in s) and a complete-sum argument. A pointwise large-n asymptotic is insufficient.

**Route and strictness checkpoint.** Use bounded perturbation on the fixed domains, comparison with constant potentials 0 and M, and the resolvent identity. Justify comparison on the kernel diagonal by a kernel construction or mollified evaluation; positive operator order alone is not an unexplained pointwise-kernel statement. The intended strictness identity is
\[
G_{n,0}(0,0)-G_{n,V}(0,0)
=\int_{\mathbb R}G_{n,0}(0,x)V(x)G_{n,V}(x,0)\,dx.
\tag{11}
\]
Establish strict positivity of both scalar kernels and convergence before using (11). Multiplying it by 4n gives the proposed defect, and comparison with the constant-M kernel gives (8). Gaussian domination yields (9)–(10). Standard one-dimensional ODE/maximum-principle or semigroup arguments inside this same class are routine execution choices. This outline specifies the route; it is not an E02 proof return.

The frozen source uses V=0. If desired for error transport within the same derivation, define p_V,s, Φ_V,s by (5) with R_V,s; their coefficients b_n are independent of u. E02 must show that every finite u derivative of that composition is justified by (9)–(10), or the equivalent polynomial recurrence in §6. These deformed sources are not silently renamed theta, and their moment/determinant comparison is not an E02 objective. In particular, a positive scalar defect does not sign a determinant defect.

**Completion and limits:** one analytic derivation and at most one regrouping; a proved theorem (8)–(11) with domains and complete-sum differentiation, or a precise failed assertion in this class. No spectral scan, potential optimization, new boundary, inverse filter or numerical acquisition. A false local bound may receive an explicitly documented routine constant correction; changing the source, observation, sign/class of V or geometry requires a dated **BR01 revision** before dependent work. Sol records the result in notes and Register02; it does not mark this future theorem accepted merely because the request contains a formula.

## 6. AR-E03 r1 — frozen source and pairing target

**E — execution; recommended Sol; conditional on the relevant E02 return.** Use C0, V=0, all s∈[0,1], fixed h and J, and the [existing normalized wedge convention](../brainstorm/notes/04_MC11_AUXILIARY_INNER_PRODUCT_AND_WEDGE_NORMALIZATION_20261104.md). Do not expand the task to deformed-potential determinants.

For x_n=πn²e^{4u}, the fixed general-index route is
\[
p_s^{(m)}(u)=e^u\sum_{n\ge1}a_n(s)e^{-x_n}P_m(x_n),\quad
P_0=1,\quad P_{m+1}=(1-4x)P_m+4xP_m',
\tag{12}
\]
\[
\Phi_s^{(m)}(u)=e^u\sum_{n\ge1}a_n(s)e^{-x_n}H_m(x_n),\quad
H_0=2x^2-3x,\quad H_{m+1}=(1-4x)H_m+4xH_m'.
\tag{13}
\]
Prove these for every fixed finite m, including complete-sum and half-line integration justifications, rather than generating a table. The n=1 term and x_1≥π>3/2 give a uniform-in-s positive lower bound for Φ_s. The intended proof bounds each derivative by a polynomial in x_1 times e^{u-x_1}, with constants allowed to depend on m, and uses that same ground term in the denominator below. No estimate uniform as m→∞ is requested or implied.

Establish for all finite i,ℓ≥0 and j≥0
\[
f_i=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}}\in h,\quad
g_\ell=\frac{u^{2\ell}\sqrt{\Phi_s}}{(2\ell)!}\in h,\quad
c_j(s)=\int_0^\infty\frac{u^{2j}\Phi_s(u)}{(2j)!}\,du.
\tag{14}
\]
Retain the exact integration-by-parts endpoint rule as the target to verify:
\[
\langle f_i,g_\ell\rangle=
\begin{cases}
c_{\ell-i}(s),&\ell\ge i,\\
-\Phi_s^{(2(i-\ell)-1)}(0),&\ell<i.
\end{cases}
\tag{15}
\]
For every q≥1 and integer k≥q-1 the indices ℓ=k+j satisfy ℓ≥i for 0≤i,j<q. Hence the requested identity is
\[
\left\langle\bigwedge_{i=0}^{q-1}f_i,
\bigwedge_{j=0}^{q-1}g_{k+j}\right\rangle
=\det[c_{k+j-i}(s)]_{i,j=0}^{q-1}.
\tag{16}
\]
In particular k=q-1,q,q+1 are in scope for the whole filter family, without assuming filtered reflection. For k<q-1 and nonnegative column indices, use (15) rather than inventing negative-index c_j. At s=1, odd endpoint derivatives vanish by the accepted theta reflection; for general s, that parity must not be assumed. Check q=1 as part of the symbolic range, not as a numerical test.

Use the normalized coordinate wedge det[f_i(u_j)]/√(q!) and the ordinary du product measure. J and its exterior powers preserve these cross-pairings but do not turn them into squared norms. State the standard Hilbert direct sum F_-(h)=⊕_{q≥0}∧^q h without inventing a Hamiltonian or a preparation protocol. No second-quantized finite-energy claim follows for the zero-extended vectors in §4.

**Completion and limits:** one general-index theorem, one proof pass and at most one local correction, with all finite derivative, moment and pairing indices quantified and every endpoint retained. No low-order acquisition or moment table. A physical preparation/domain requirement beyond Hilbert membership or a changed observation goes back to **BR01**. An order-dependent signed-estimate choice goes to **B01**. This identity alone is not a sign estimate in q.

## 7. Control screen and evidence boundary

Apply the [collision-control cluster](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid/02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) to the actual retained premises. This is an analytic premise screen, not a repeat of the archived collision computations.

| Control | Construction that survives | Premise absent from the canonical s=1 source |
| --- | --- | --- |
| Positive weighted-square controls | The same Green diagonal with a nonnegative shell insertion gives weighted square sums; the auxiliary pairing still exists | Exact unit shell coefficients and full normalized reflection; finite endpoint matches do not replace them |
| Euler-factor controls | Positivity of the source and the generic Hilbert/exterior construction | Unchanged canonical arithmetic source/trace; source positivity is not distinguishing |
| Reflected super-Gaussian | Reflection and positive Hilbert/Fock metrics | Literal complete integer-square theta expansion |
| Smooth shape/positive-primitive controls | Their positive auxiliary channel and the relevant shape/endpoint identities | Exact canonical arithmetic coefficients; primitive positivity does not sign a cross-pairing |

The E02 potential comparison is generic for positive one-dimensional scalar resolvents and does not distinguish theta from weighted-square controls. A control that uses different shell coefficients fails the exact-source requirement, not the resolvent comparison. In particular, no control is claimed to violate (8)–(10); those inequalities concern a response deficit, not collision exclusion. Even the literal unit-weight premise only identifies the target. B01 must still supply and screen a genuinely quantitative signed hypothesis.

The decision was checked against AR-E01's six reusable premises, the R1 weight normalization, the two-candidate limit, all filter settings, full radial accounting and the endpoint ranges. This is author-side contract checking by the same assistant, not independent review or completion of E02/E03. No new certified computation, determinant gain, manuscript, or research closure is claimed. No result-summary promotion is warranted by model selection alone.

**Next: [E] MC11-AR-E02 — Sol.** Prove the frozen bounded-nonnegative-potential response/rigidity theorem, reusing the free result. The [return and model-change continuation](../research-progress/handoffs/06_MC11_BR01_RETURN_AND_AR_E02_MODEL_CONTINUATION_20261105.md) supplies activation instructions and preserves this chat's history identity.
