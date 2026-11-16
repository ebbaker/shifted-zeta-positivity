# Midpoint closure: exact comparison, finite freedom and quantitative calibration

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead actual model and effort unavailable in the current archive configurations. Fixed proof and assessment dispatches **gpt-6.1-sol / ultra** are recorded separately from backend attestation. Research chat0003.

**Research synthesis; four proofs accepted within scope in the separate internal [E14 assessment](../reviews/06_VCD_E14_MIDPOINT_SESSION_ASSESSMENT_20261116.md).** The one response pass clarified synthesis wording and quantifiers; no proof correction was required. The assessment shares the proof workers’ model and source premises and is not independent specialist review. This session continues the first [connected synthesis09](09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md), executes the author's midpoint option, and keeps the complete theta source and literal Fourier readout. No zero-confinement induction is established. Source statuses, final assessment and next task belong to the [live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md).

Read the [result index](../../../../result-summaries/README.md), especially [cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md) and [control catalog12](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), especially [classification01](../../../../avoid/01_restating_the_target.md), [controls02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [representations03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [correlations12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The unspecified shrinking-strip conclusion retains E04's existing classification; it is not tested numerically here.

## 1. One memory supplies both midpoint terms

[E13, Note11](11_VCD_E13_MIDPOINT_AUDIT_20261116.md) proves the bilinear identity, fixed-orbit complex domains, local uniform convergence, and the two-error ledger. Write A=J_N, e=e_(N-1), beta=beta_N and c(z)=Pi_N exp(izJ/2)e_0. Then
\[
 c'(z)=\frac{i}{2}Ac(z)-\frac{\beta}{4}e\int_0^z
 k_N((z-s)/2)c_{N-1}(s)\,ds,
\]
\[
 R_N(z)=-\frac{\beta}{4}\int_0^z\!\int_0^z
 k_N\bigl(z-(s+t)/2\bigr)c_{N-1}(s)c_{N-1}(t)\,dt\,ds.
\]
The retained evolution uses the memory through half height; the omitted term uses it through full height. The latter is a bilinear square, without a positivity interpretation. Exact retained c_0(z)=F(z/2) already contains full-chain Fourier data.

[E15, Note13](13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md) extends the baseline comparison. For **any entire scalar k**, used consistently in those two formulas, their sum equals the same model's direct full-height Volterra response f_k(z). This is stronger than the zero-memory bare-quadrature identity. It rules out an improvement solely from splitting the same kernel model at the midpoint; it does not rule out better kernels, different joint models or better error analysis.

For two kernels k and ell on the same prefix, E15 gives the exact signed error
\[
 f_k-f_\ell=-\beta_N\,(e_0^{\mathsf T}T_k e)
       *(k-\ell)*(e^{\mathsf T}T_\ell e_0),
\]
where T solves the corresponding finite Volterra matrix equation. The two midpoint errors sum to this expression. If the first different kernel derivative is order q, the first scalar difference is
\[
 (-1)^N\Bigl(\prod_{j=1}^N\beta_j\Bigr)
 (k-\ell)^{(q)}(0)\frac{z^{2N+q}}{(2N+q)!}.
\]
A fixed-disk absolute stability bound is also proved. These are generic transport results; the exact canonical bounded score remainder b is not used to bound k_N-ell, and no signed theta margin is supplied.

## 2. Finite canonical score and midpoint data leave local freedom

[E12, Note12](12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md) strengthens the smooth E10 construction in a specific direction. For finite L>=N>=1, r>=0 and z*=x+iy with x nonzero and 0<|y|<4, a two-parameter smooth compact multiplier family preserves all of:

- time-zero moments through 2L, polynomials through q_L and links through a_L;
- every canonical V' AND exact canonical b matrix entry with indices at most L;
- retained full-chain midpoint derivatives c_n^(j)(z*) for n<N and j<=r;
- disconnected-tail Taylor coefficients through order 2(L-N)+1;
- the full reflection jet, exact real source tails, the same envelope, and any positive own-to-canonical score tolerance.

Its literal F(z*) and omitted R_N(z*) nevertheless move together through an open complex disk about their canonical values. The radius depends on the fixed data and can be very small. The proof uses finite test-function duality and separation of full-frequency, half-frequency and score growth; it gives neither a zero-location conclusion nor both signs for R_N itself.

The controls fail **pointwise own-score equality** and representation by the same square modes with constant coefficients and absolute convergence at one positive point, despite retaining finite matrix elements of the exact b function. E07's nonreal-zero conclusion remains confined to its different finite square-change class, which loses smooth reflection. It cannot be attached to these smooth controls.

## 3. Finite freedom can shrink geometrically

[E16, Note14](14_VCD_E16_CALIBRATION_UPPER_BOUND_20261116.md) quantifies the opposite side of the same question. Let delta F be the Fourier transform of h dmu, with real even h and ||h||_infinity<=eta. Matching moments through 2L makes delta F vanish at 0 to order at least 2L+2. Matching c_0 midpoint derivatives through order r makes it vanish to order at least r+1 at the quartet
\[
 \mathcal A=\{z_*/2,-z_*/2,\overline{z_*}/2,-\overline{z_*}/2\}.
\]
For rho>|z*| and B_(rho,a)(w)=rho(w-a)/(rho²-conjugate(a)w), the classical disk-factor estimate gives
\[
 |\delta F(w)|\le\eta F(i\rho)
 \left(\frac{|w|}{\rho}\right)^{2L+2}
 \prod_{a\in\mathcal A}|B_{\rho,a}(w)|^{r+1},\qquad |w|<\rho.
\]
At w=z*, the quartet product theta_rho(z*) lies strictly between zero and one. Each extra midpoint derivative multiplies this **same moment-only disk allowance** by theta_rho(z*). One may also use the ordinary moment-series tail and take the smaller bound; no uniform superiority to that alternative is claimed.

This is a conditional absolute error estimate using full-source calibration and a relative source-error allowance. It does not construct such an approximating source or acquire those derivatives from a finite head. At fixed height the freedom left by E12 can therefore shrink geometrically as the calibration grows. At growing height, the factor F(i rho), the geometry and all data/tolerance costs must be paid. A positive local freedom radius is not a uniform obstruction to compact confinement.

## 4. Scientific disposition

B04 completed three documented passes within its two candidate formulations: [finite joint information](../brainstorm/notes/07_VCD_B04_JOINT_MIDPOINT_INFORMATION_DECISION_20261116.md), [shared-memory comparison](../brainstorm/notes/08_VCD_B04_SHARED_MEMORY_COMPARISON_DECISION_20261116.md), and [quantitative remaining freedom](../brainstorm/notes/09_VCD_B04_CALIBRATION_RADIUS_DECISION_20261116.md). E13 is foundation work. E12 is a scoped exact-determination obstruction. E15 gives an exact same-model comparison, error order and stability ledger. E16 gives a conditional geometric calibration bound by a classical method. None is a new source-sensitive signed Fourier inequality.

The family-by-family control screens are in the proof notes and decision07. Generic midpoint and Volterra identities survive for the applicable controls. Keeping the exact canonical b in finite tests does not make a perturbation canonical. Conversely, E12 does not invalidate a growing-data scheme with new quantitative information. Full all-degree source identification from E08 remains available without becoming a zero theorem.

The next conceptual work must supply a quantitative canonical restriction on the correlated memory defect (or construct a genuinely richer joint model with paid calibration errors), a valid degree step or terminal argument, and a signed/model-modulus consumer. A new finite equality or a second derivation of the same-kernel split does not supply these. No new coefficient acquisition, height scan, manuscript snapshot or publication was performed. Detailed evidence and actual dispatches are in the frozen handoffs and the session record; chat0003 is registered under this investigation.
