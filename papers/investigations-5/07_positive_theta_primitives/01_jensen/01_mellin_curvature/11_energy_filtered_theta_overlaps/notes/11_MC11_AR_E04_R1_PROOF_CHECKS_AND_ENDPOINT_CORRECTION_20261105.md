# MC11-AR-E04 r1: proof checks and endpoint correction

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual recorded **gpt-6.1-sol (Codex), effort ultra**. Thread `01a1aa7d-08ce-74a3-b98d-c016f472bc45`, MC11 history0005. **E — execution**, MC11-AR-E04 request r1.

**Result: accepted within scope with one local correction R1 to Note09 (18) at s=0.** The [assessment](../reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md) owns dispositions. This note records supporting derivations and R1 without changing issued inputs. One analytic pass with disjoint read-only same-model checks; root alone writes artifacts. The accepted AR-E01 spectrum/domain/readout and E01 finite anchor are shared premises, not reacquired evidence.

## 1. Measurable potentials and the continuous diagonal

In Note07 let a=2n, λ=√(a²+M), U=M−V, ρ=M/λ²<1 and g=g_λ. The positive path kernel K_j represents (SU)^jS and has supremum at most ρ^j/(2λ). For j≥1, removing the outer g factor gives
\[
\sup_{v,w}|K_j(v+h,w)-K_j(v,w)|
\le\frac{M\rho^{j-1}}{2\lambda}\|\tau_hg-g\|_1.
\]
Consequently
\[
\sup_{v,w}|G(v+h,w)-G(v,w)|
\le\|\tau_hg-g\|_\infty+
\frac{M}{2\lambda(1-\rho)}\|\tau_hg-g\|_1\longrightarrow0.
\]
M=0 is the continuous free kernel; symmetry treats the other endpoint. This makes Note07's valid joint-continuity proof explicit, **not a further correction**. No continuity of V is used.

The convolution majorant has Fourier transform 1/(ξ²+a²), hence is g_a everywhere by continuity. Thus g_λ≤G≤g_a. The continuous resolvent identity
\[
g_a(v-w)-G(v,w)=\int g_a(v-x)V(x)G(x,w)dx
\]
holds at the diagonal as well as distributionally. If {V>0} has positive measure, its integral at (0,0) is strictly positive. Since ∫g_a²=1/(4a³), multiplication by 4n=2a gives M/(8n²). Constant-potential comparison gives Note07's stronger square-root bound. The retained n=1 angular shell proves exact response at even one t>0,s∈[0,1] iff V=0 a.e.

The angular-block tail norm is ≤1/[4(N+1)], so the complete radial kernel is norm continuous. The finite observable is an angular trace of the damped radial diagonal; no full-space finite partition function or angular point diagonal is implied. Scope remains bounded nonnegative scalar radial V and unchanged second-order domains/readout.

For all fixed differentiated sums, maximizing x^p e^{−εx²/2} and using (L+j)²≥L²+(2L+1)j proves the complete T_p tails, including p=−2. For the external source, e^u=π^{−1/4}x_n^{1/4}n^{−1/2} and max x^αe^{−x/2}=(2α/e)^α prove Note07 (22). Each finite derivative is paid; constants depend on order.

## 2. Source denominator, integrability and endpoints

The chain rule is T(F)=(1−4x)F+4xF'. In particular P_2=1−24x+16x² and (P_2−P_0)/8=H_0=2x²−3x. Note08's recurrence is exact. Complete spectral domination gives
\[
|\Phi_s^{(m)}|\le B_m e^{u-x}x^{m+2},\qquad
\Phi_s\ge\kappa e^{u-x}x^2,\quad\kappa=2-3/\pi>0.
\]
The matching ground exponent matters: division gives
\[
|f_i|^2\le(B_{2i}^2/\kappa)e^{u-x}x^{4i+2}.
\]
Together with the g_ℓ bound this proves every finite L²(du) membership. The exact substitution u=log(x/π)/4 yields
\[
\int_0^\infty u^re^ux^de^{-x}du
=\frac{\pi^{-1/4}}{4^{r+1}}\int_\pi^\infty
[\log(x/\pi)]^r x^{d-3/4}e^{-x}dx<\infty.
\]
C_d(N)→0 pays all polynomially weighted complete spectral tails. No constant is asserted uniform as indices grow.

Integration by parts against u^{2ℓ}/(2ℓ)! gives +c_{ℓ−i} for ℓ≥i. For ℓ<i, integrate 2ℓ times, then integrate Φ_s^{(2(i−ℓ))}; the result is **−Φ_s^{(2(i−ℓ)−1)}(0)**. Infinity terms vanish. Only s=1 is guaranteed even; the exact filtered odd endpoint is (1−s)e^{−π}H_{2r+1}(π).

For q≥1,k≥q−1 every column index ℓ=k+j is ≥i, including q=1. Lower nonnegative shifts retain endpoint entries instead of negative-index coefficients. The coordinate wedge det[f_i(u_j)]/√(q!) cancels the two permutation sums' q!, giving the cross-determinant without an extra factor. J, its exterior powers and Fock direct sum are Hilbert isometries only, with no Hamiltonian-domain/preparation or squared-norm sign consequence.

## 3. Ratio proof and accepted anchor

For n≥2,
\[
r_n(x)=n^2\frac{2n^2x-3}{2x-3}e^{-(n^2-1)x},\qquad
(\log r_n)'=-(n^2-1)\left[1+\frac6{(2n^2x-3)(2x-3)}\right]<0.
\]
The complete geometric majorant gives 0<r=Σr_n<4/999<1/200. Comparison at two arguments proves strict decrease of the sum without differentiating it.

Let μ_j have density u^{2j}φ_π/((2j)!b_j). The normalized u² tilt cancels factorials, so
\[
\rho_{j+1}-\rho_j=
\frac{\operatorname{Cov}_{\mu_j}(u^2,r)}{\mathbb E_{\mu_j}u^2}<0.
\]
Twice the covariance is the μ_j×μ_j integral of (u²−v²)(r(u)−r(v)), strictly negative off the diagonal. Bounded r and the proved finite moments justify all integrals.

Accepted E01 Note01 §2/Review01 supply |b_1−c_1^*|≤εc_1^*, h_1≤εc_1^*, c_1^*>0 and ε=1/40000. Therefore
\[
\rho_1\le\epsilon/(1-\epsilon)=1/39999,\qquad
0<\rho_j\le1/39999\ (j\ge1),\qquad0<\rho_0<1/200.
\]
The compact enclosure and its complete energy/spatial payments are inherited accepted premises. No quadrature is repeated and no compact/compensated zero coefficient replaces raw b_0.

## 4. Sole local correction R1

**Note09 (18) is false at s=0 in its strict zero-index upper bound:** it would require 1<1. The corrected closed-interval statement is
\[
\boxed{1\le c_0(s)/b_0\le1+s/200\quad(0\le s\le1),}
\]
with strict upper inequality for 0<s≤1. This follows from c_0(s)/b_0=1+sρ_0 and 0<ρ_0<1/200. The positive-index bound remains valid as printed.

R1 changes no scalar constant, moment, source, domain, determinant identity or complete payment. Note09 (24) already uses a non-strict allowance and gives zero payment at s=0; both certificate-ceiling thresholds remain valid. Issued Note09 remains byte-identical. The current M01 manuscript omits this false strict coefficient line, but its pending-assessment provenance needs the separate recorded M01 follow-through.

## 5. Complete payments and the exact stop scope

Collect P(z)=Σ_αγ_αz^α before taking absolute values. It is homogeneous of degree q; z_k^q has coefficient one. Substitution gives the exact common-path difference
\[
D(s)-D(0)=\sum_\alpha\gamma_\alpha b^\alpha
\left[\prod_j(1+s\rho_j)^{\alpha_j}-1\right].
\]
Its complete upper payment R replaces γ_α with |γ_α|. All mixed powers and excited levels survive, and actual index ratios are retained. **It is still an absolute monomial payment:** cancellation between distinct collected monomials is discarded. This clarifies the existing scope, rather than correcting another formula.

At k=q−1 only the bottom-left entry has index zero; every monomial contains b_0 at most once. Corrected R1 proves the same U_q^− allowance, including q=1 and s=0. A positive reference has μ=D(0)/A(b)∈(0,1]. For N=39999, the quadratic binomial term gives (1+1/N)^N>2. Hence the displayed uniform certificate is impossible for q≥39999,k≥q, and its stated lower-shift ceiling holds for q≥40000. These are sufficient ceilings, not earliest failures or actual-error lower bounds.

For Route A, m=k−q+1≥0 and deleting the bottom-left entry leaves A_0=(−1)^{q−1}D_{q−1,k+1}. Integrate the slope recursion against u^r/r! only for r≥1, then iterate down to J_{2m}; m=0 uses J_1≤J_0/λ and needs no r=0 integration. Positive summation gives the complete 40^{−2ℓ} remainder. A quantitative shifted-cofactor margin, positive initial determinant and paid loss remain missing.

The fixed-uniform-envelope implementation has a proved eventual certificate limitation. Route A's margin and Route B's nonuniform payment/reference comparison have missing estimates, not disproved canonical inequalities. No structural BR01 failure or signed E05 contract arose.

## 6. Reuse and continuation

Classification: supporting representation, unsigned estimate and scoped certificate limitation, not an RH criterion. Read the [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [review provenance](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [endpoint slips](../../../../../../../avoid/08_normalization_and_constant_slips.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

**Next: [E] MC11-M01 follow-through — Sol**, under the [continuation/model-change packet](../research-progress/handoffs/11_MC11_AR_E04_RETURN_AND_M01_MODEL_CONTINUATION_20261105.md). Future B01 reopening is conditional on a specified signed-margin or source-sensitive reference/conditioning route; E05 remains reserved. No numerical acquisition, new determinant sign, curvature domain or RH consequence.
