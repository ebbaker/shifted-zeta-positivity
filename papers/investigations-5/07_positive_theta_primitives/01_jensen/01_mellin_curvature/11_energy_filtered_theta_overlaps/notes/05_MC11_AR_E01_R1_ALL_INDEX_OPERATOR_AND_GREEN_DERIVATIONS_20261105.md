# MC11-AR-E01 r1: all-index operator and Green derivations

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6.1-sol (Codex), actual recorded effort ultra**. Thread `01a1aa23-3513-7681-bad6-d8c15b6914fb`, MC11 history0003. Type **E — execution**, request r1. This supporting note is in `notes/` at the author's current request. The issued [Brainstorm Note06](../brainstorm/notes/06_MC11_ANGULAR_WEIGHT_DIRAC_SQUARE_AND_RADIAL_GREEN_20261104.md) is unchanged.

**Result:** the specified cylinder square, full-line Green response, half-line second-order kernels and Euclidean differential expression are accepted within the domains below. One local exposition clarification, **R1**, fixes which angular weight is held fixed when a sphere's radius changes. No displayed identity in Note06 needs an algebraic correction. The [claim assessment](../reviews/03_MC11_AR_E01_R1_ANGULAR_RADIAL_IDENTITY_ASSESSMENT_20261105.md), [input record](../research-progress/handoffs/05_MC11_AR_E01_R1_INPUT_VERSIONS_20261105.json) and [continuation](../research-progress/handoffs/05_MC11_AR_E01_RETURN_AND_BR01_MODEL_CONTINUATION_20261105.md) specify the reusable scope.

## 1. Angular convention and weight

Let K be the Hilbert space of complex rank-two spinors on the unit round S², with its spin metric and round area measure. Fix its self-adjoint geometric Dirac operator D, with domain H¹(S²;Σ), and Hermitian chirality Γ satisfying Γ²=I and ΓD=-DΓ. Both Dirac signs are retained. The spectrum is ±n, n≥1, with 2n states per sign. These are the N=2 specialization, with the paper's index shifted by one, of Camporesi–Higuchi (3.54) and the spectrum discussion at the end of section 3.1. Their slash operator is anti-Hermitian; D=-i slash-nabla. Their (5.35)–(5.36) give D²=∇*∇+1/2. [Primary source, version 1](https://arxiv.org/html/gr-qc/9505009).

Write P_n for the spectral projection of D² at n². Then dim P_nK=4n, Γ preserves P_nK, and
\[
 |D|=\sum_{n\ge1}nP_n,\qquad
 W=(4|D|)^{-1}=\sum_{n\ge1}\frac{P_n}{4n}.
\tag{1}
\]
Thus 0<W≤I/4, but Tr W=Σ1=∞. A positive bounded effect need not be a density operator. For t>0,
\[
 \operatorname{Tr}_K(We^{-tD^2})=\sum_{n\ge1}e^{-tn^2}=Q(t).
\tag{2}
\]
The scalar-weight uniqueness statement has precisely Note06's scope: if a bounded W'=w(|D|) has this trace for every t>0, then 4nw(n)=1 for each integer n. To see this, subtract (2), multiply by e^t and take t→∞ to isolate the first coefficient; repeat after removing every preceding coefficient. Boundedness of w bounds the remaining coefficients by O(n), and Gaussian domination justifies each limit. Only its values on the spectrum are fixed. An arbitrary operator's heat trace fixes block traces, not its matrix entries. Rotations alone do not choose (1).

## 2. Complete-cylinder realization

Use H_C=L²(R,dv;K). The metric dv²+g_S²/4 has angular area dΩ/4; multiplication of all spinors by a constant identifies this Hilbert space with the metric-volume version. There is no angular multiplicity factor from this constant measure change. The Dirac operator on the radius-1/2 sphere is 2D.

On compactly supported smooth radial functions with finite angular spectral support set
\[
 \mathcal D_C=-i\Gamma\partial_v+2D.
\tag{3}
\]
Fourier transformation in v makes (3), on P_nK, the finite-dimensional Hermitian matrix
\[
 M_n(k)=k\Gamma+2D|_{P_nK},\qquad M_n(k)^2=(k^2+4n^2)I.
\tag{4}
\]
The self-adjoint multiplication/direct-sum realization therefore has domain
\[
 \operatorname{Dom}\mathcal D_C=
 \left\{\psi:\sum_{n\ge1}\int_{\mathbb R}
 (k^2+4n^2)\|P_n\widehat\psi(k)\|^2dk<\infty\right\}.
\tag{5}
\]
Finite angular truncation followed by smooth radial approximation proves that the stated initial domain is a core. This explicitly supplies the complete-cylinder realization without a boundary assumption. The anticommutation cancels the cross terms, and its self-adjoint square is
\[
 \mathcal L=\mathcal D_C^2=-\partial_v^2+4D^2,
\quad
 \operatorname{Dom}\mathcal L=
 \left\{\psi:\sum_n\int(k^2+4n^2)^2
 \|P_n\widehat\psi(k)\|^2dk<\infty\right\}.
\tag{6}
\]
In particular L≥4I and L⁻¹ is bounded with norm 1/4. This square is a positive second-order kinetic operator. Interpreting it as a Hamiltonian remains a model choice.

## 3. Green kernel and the complete sum

For every symbolic integer n≥1, let a=2n. The decaying fundamental solution of -∂²+a² is
\[
 G_n(v,w)=\frac{e^{-a|v-w|}}{2a}
          =\frac{e^{-2n|v-w|}}{4n}.
\tag{7}
\]
It solves the homogeneous equation off v=w. Its first v derivative is -e^{-a(v-w)}/2 on v>w and +e^{-a(w-v)}/2 on v<w. The right-minus-left jump is -1, so -∂²G supplies +δ and (-∂²+4n²)G_n=δ. Decay at both ends gives uniqueness. The equivalent Fourier formula is ∫e^{ik(v-w)}(k²+4n²)⁻¹ dk/(2π).

The angular-operator-valued radial kernel of L⁻¹ is
\[
 K(v,w)=\sum_{n\ge1}G_n(v,w)P_n
 =\frac{e^{-2|D||v-w|}}{4|D|}.
\tag{8}
\]
This converges in operator norm, including at v=w: the discarded operator norm is at most 1/[4(N+1)]. It is norm-continuous in v,w and bounded by e^{-2|v-w|}/4. Integrating this bound in w gives 1/4, so convolution defines a bounded operator on H_C. Its Fourier multipliers agree with (6), identifying it with L⁻¹. The derivative jump of K is -I in the strong operator sense. Its diagonal is the bounded angular operator
\[
 K(v,v)=W.
\tag{9}
\]
Equation (9) is a radial kernel diagonal whose values are operators on K. It is not the pointwise spinor kernel at equal angular points; that further diagonal would require angular regularization. Evaluation at v is also not a bounded map on unrestricted L²(R;K), and is not being inserted as such in an operator trace.

For t>0 the positive angular operator e^{-tD²}K(v,v) is trace class, and
\[
 R(t,v):=\operatorname{Tr}_K[e^{-tD^2}K(v,v)]
 =\sum_{n\ge1}4n\frac{e^{-tn^2}}{4n}=Q(t).
\tag{10}
\]
The series is finite since n²≥n. For each fixed integer m≥0 and ε>0, Σn^{2m}e^{-εn²}<∞, so termwise t differentiation is justified uniformly on t≥ε. There is no assertion uniform as t↓0 or as m→∞. No mode cutoff or numerical tail payment is involved.

The full-space positive operator e^{-tD²}L⁻¹ has infinite trace: its angular trace density on the radial diagonal is the positive constant Q(t), integrated over all v∈R. Likewise the actual full heat kernel has radial trace density
\[
 (4\pi\tau)^{-1/2}\sum_{n\ge1}4n e^{-4\tau n^2},\qquad \tau>0,
\tag{11}
\]
and infinite total trace on the cylinder. The response (10) is finite precisely in its stated angular trace sense. Since D_C is invertible, D_C⁻¹=D_C L⁻¹; its differentiated/matrix numerator distinguishes it from (8).

## 4. Half-line second-order benchmarks

On L²((0,∞),dv), the operators -∂²+4n² with domains H²∩H¹_0 (Dirichlet) and {f∈H²:f'(0)=0} (Neumann) are self-adjoint and at least 4n². Their direct sums over P_nK, with the usual summability of graph norms, supply the corresponding second-order spinor realizations. Reflection gives
\[
 G_n^{D/N}(v,w)=\frac{e^{-2n|v-w|}\mp e^{-2n(v+w)}}{4n}.
\tag{12}
\]
The image term is homogeneous in the open half-line. It enforces G^D(0,w)=0 or ∂_vG^N(0,w)=0 for w>0, while preserving the jump from (7). Thus
\[
 \operatorname{Tr}_K[e^{-tD^2}K_{D/N}(v,v)]
 =Q(t)\mp B(t,v),\qquad
 B(t,v)=\sum_{n\ge1}e^{-tn^2-4nv}.
\tag{13}
\]
The trace is well defined for t>0, v≥0, with boundary values understood by continuity. At v=0 it is 0 for D and 2Q(t) for N. At any finite v>0, B(t,v)>0. For fixed derivative orders, t≥ε and v≥0 give Gaussian domination of every differentiated series. As v→∞ the image sum tends to zero; it is not identically absent.

This assesses the second-order problems only. The first-order boundary form is proportional to ψ(0)†Γφ(0). A self-adjoint first-order realization requires maximal appropriate boundary data; imposing zero on every spinor component is not such a maximal condition. Given a self-adjoint first-order A, Dom A² requires both ψ∈Dom A and Aψ∈Dom A. One cannot infer either second-order domain above by naming a first-order wall. No first-order half-line extension is selected here. A parity restriction also changes the normalized half-line kernel; evenness of a scalar source does not remove (13).

A scalar potential V(v) in a specified second-order cylinder problem preserves angular separation, subject to its form/domain hypotheses. Its channel Green coefficient is then 4nG_{n,V}(v,v). This is the observable to calculate, rather than a proof that the coefficient stays one. No potential or comparison theorem is selected in this assessment; those are BR01/AR-E02 dependencies.

## 5. Euclidean spin connection and measure

For r=e^{2u},
\[
 g_E=dr^2+r^2g_{S^2}
     =4e^{4u}(du^2+g_{S^2}/4).
\tag{14}
\]
Thus the cylinder is a conformal geometry, not Euclidean space with its metric unchanged. The scalar companion's normalized cylinder volume du dΩ/(4π), metric volume du dΩ/4, and Euclidean volume r²dr dΩ must be distinguished. Its constant metric-volume normalization does not affect the spectral multiplicities in (10).

Here is an explicit spinor convention establishing Note06 (13). In the Pauli description put Γ=σ·ω, L_orb=-i x×∇ and D_0=σ·L_orb+I. Then {Γ,D_0}=0 and the ordinary Euclidean Pauli operator obeys
\[
 -i\sigma\cdot\nabla=-i\Gamma(\partial_r+1/r)
                         +i\Gamma D_0/r.
\tag{15}
\]
Identify the intrinsic angular D with iΓD_0. It is Hermitian and unitarily equivalent to D_0: e^{iπΓ/4}D_0e^{-iπΓ/4}=iΓD_0. This states explicitly the tangential spinor identification used in the cylinder/cone formulas. Reversing a chirality convention only interchanges the two channels below.

Multiplication Uψ=rψ is a unitary map from L²(r²dr dΩ) to L²(dr dΩ), unlike the scalar du-to-Euclidean isometry in Note05. On smooth spinors supported away from r=0,
\[
 \widetilde{\mathcal D}_E=U\mathcal D_EU^{-1}
                  =-i\Gamma\partial_r+D/r,
\quad
 \widetilde{\mathcal D}_E^2=-\partial_r^2+
                  \frac{D^2+i\Gamma D}{r^2}.
\tag{16}
\]
The radial 1/r spin-connection term in (15) is removed by U. To square the reduced expression, its mixed terms are iΓD/r²-i(ΓD+DΓ)∂_r/r, leaving exactly (16). Hence the connection has not been discarded.

On P_nK, J=iΓD is Hermitian, J²=n²I and DJ=-JD. The invertible D maps the +n and -n eigenspaces of J bijectively, so each has dimension 2n. Therefore the reduced square has scalar expressions
\[
 -\partial_r^2+\frac{n(n+1)}{r^2},\qquad
 -\partial_r^2+\frac{n(n-1)}{r^2},\qquad n\ge1.
\tag{17}
\]
This proves the complete family at the differential-expression level. It chooses neither an origin realization nor an exterior boundary at r=1. Behavior at r=0, conditions at r=1 in the original exterior coordinate, and any resolvent or Green normalization require that later domain decision. The cylinder kernel (7) cannot be used as their Euclidean Green kernel.

## 6. Jacobi inversion and the observation map

Let A(r)=Q(πr²) for r>0. The theta transformation at z=0, τ=ir², yields
\[
 1+2A(r)=r^{-1}[1+2A(1/r)],\qquad
 A(r)=r^{-1}A(1/r)+\tfrac12(r^{-1}-1).
\tag{18}
\]
Here the square root is positive. This is the real-radius specialization of [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32). The complete unit-weight series and r>0 are essential.

**R1 — sole local exposition clarification.** Note06's frozen-sphere response Q(π/r²) holds with the dimensionless unit-sphere weight fixed:
\[
 \operatorname{Tr}_K[W e^{-\pi(D/r)^2}]=Q(\pi/r^2).
\tag{19}
\]
Reapplying the literal inverse-Dirac prescription at radius r instead gives W_r=(4|D/r|)⁻¹=rW, and its trace is rQ(π/r²). Equation (19) is accepted with its readout convention explicitly fixed. The two insertions are distinct BR01 choices; no new radial observable has been adopted here.

Direct differentiation with ∂_u=2r∂_r gives
\[
 \frac18(\partial_u^2-1)[e^u A(e^{2u})]
 =\tfrac12r^{5/2}\Delta_3A(r),\qquad
 \Delta_3=\partial_r^2+2r^{-1}\partial_r.
\tag{20}
\]
The correction 1/(2r)-1/2 is harmonic for r>0; after multiplication by e^u it becomes -sinh u, annihilated by ∂_u²-1. This is a local differential identity. At the Euclidean origin 1/r has a distributional point source, so this statement must not be promoted to a whole-space harmonic assertion without qualification.

For the specified filter family A_s=sA+(1-s)e^{-πr²}, the exact defect from using the same normalized inversion law is
\[
 A_s(r)-r^{-1}A_s(1/r)-\tfrac12(r^{-1}-1)
 =(1-s)\left[e^{-\pi r^2}-r^{-1}e^{-\pi/r^2}
                 -\tfrac12(r^{-1}-1)\right].
\tag{21}
\]
The bracket tends to 1/2 as r→∞, so the canonical law fails identically for s≠1. This scopes the Jacobi argument; it does not exclude externally inserting the original filter. Indeed B_s=P_1+s(I-P_1) gives Tr[B_s e^{-tD²}K(v,v)]=Q_s(t), but the insertion is an additional stated observation, rather than a dynamical consequence of the free cylinder.

In all cases (10) leaves t independent of v. The replacement t=πe^{4u}, the e^u source factor and the observation/derivatives in (20) are still an externally specified source map. They do not follow from a heat evolution whose time is a spatial coordinate. A physical preparation of the auxiliary derivative/moment functions, and their scalar-to-spinor encoding, remains unspecified. There is no parallel constant spinor on the round sphere: D²=∇*∇+1/2 excludes one. No particular spinor state is selected by (10).

Finally, D, |D| and D² define different dynamics. D has two signs and is unbounded below, so e^{-βD} is not an ordinary finite-temperature trace-class Boltzmann operator for β>0. Positive-energy |D| has levels n; D² has levels n². Restricting a branch changes the multiplicity and the first-order product construction. Neither fermionic statistics nor squaring alone selects the physical Hamiltonian.

## 7. Evidence boundary and return

This is one analytic assessment pass over the complete symbolic spectral family, with R1 as the only local exposition correction. A read-only Sol/ultra supporting agent checked the Euclidean and Jacobi calculations and identified the weight qualification; the root chat wrote all artifacts. That is internal same-model support for this assessment of Astra-authored Note06, with shared spectral premises and no independent specialist review. There was no quadrature, finite-mode scan, numerical acquisition, potential search or new signed estimate.

Classification under [avoid/01](../../../../../../../avoid/01_restating_the_target.md): a **representation/domain result**, not a proposed RH criterion or quantitative determinant milestone. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [re-realization caution](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) govern reuse. The review records each control's failed canonical-source premise; no new sign inequality is proposed to test against them. Positive Green response and a positive Hilbert metric leave a cross-determinant's sign open.

**Next: [B] MC11-BR01 — Astra.** Select at most two existing model contracts and freeze one geometry, domain, boundary, potential class, readout and independent thermal/evolution parameter. In particular decide whether the exact full-line cylinder response is an acceptable observation, or whether a Euclidean/exterior response is required and must be derived. AR-E02 remains conditional on that contract; AR-E03 and the distinct B01/E05 signed-estimate route retain their existing dependencies.
