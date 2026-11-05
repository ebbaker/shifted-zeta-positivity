# MC11-AR-E03 r1: source membership and endpoint-preserving pairings

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6.1-sol (Codex), actual recorded effort ultra**. Existing thread `01a1aa23-3513-7681-bad6-d8c15b6914fb`, MC11 history0003. **E — execution**, frozen request r1. Root is sole artifact writer; a read-only same-model supporting check verified membership, endpoint algebra and index ranges.

**Status: proved in-note without correction, with proof-author and same-model supporting checks; no separate specialist assessment.** The unchanged [BR01 Note06 §6](06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md#6-ar-e03-r1--frozen-source-and-pairing-target) is satisfied for every finite requested index and all s∈[0,1]. [Frozen activation versions](../research-progress/handoffs/08_MC11_AR_E03_R1_FROZEN_INPUTS_20261105.json) include the verified actual E02 return. The [return record](../research-progress/handoffs/08_MC11_AR_E03_R1_RETURN_RECORD_20261105.json), [sole live register](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) and [continuation](../research-progress/handoffs/08_MC11_AR_E03_RETURN_AND_B01_MODEL_CONTINUATION_20261105.md) retain disposition and routing. No numerical acquisition, moment table, finite-order sign campaign or changed source is used.

## 1. Operator-to-source map and theorem

Keep BR01's complete radius-1/2 cylinder, free squared Dirac L_0, full radial line, fixed probe v=0, dimensionless W=(4|D|)⁻¹ and external B_s=P_1+s(I−P_1). Reuse the accepted free identity and E02 return:
\[
 K_{L_0^{-1}}(0,0)=W,\qquad
 \operatorname{Tr}_K[B_se^{-tD^2}W]=Q_s(t)
 =\sum_{n\ge1}a_n(s)e^{-tn^2},
 \quad a_1=1,\quad a_n=s\ (n\ge2).
\tag{1}
\]
The actual model remains **V=0**. No deformed-potential determinant is considered. The radial probe, physical evolution time τ and angular damping t remain distinct from the auxiliary source coordinate u. Apply exactly the external map
\[
 x=\pi e^{4u},\quad x_n=n^2x,\quad
 p_s(u)=e^uQ_s(x),\quad
 \Phi_s(u)=\tfrac18(\partial_u^2-1)p_s(u),\qquad u\ge0.
\tag{2}
\]

**Theorem.** For every s∈[0,1], the following statements hold, uniformly in s at each fixed finite set of indices:

1. The functions p_s and Φ_s are real C∞ on the source half-line, with the complete-sum derivative recurrences in §2. A positive lower bound for Φ_s is supplied by its retained n=1 term.
2. For all integers i,ℓ,j≥0, the functions
\[
 f_i=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}},\qquad
 g_\ell=\frac{u^{2\ell}\sqrt{\Phi_s}}{(2\ell)!}
\]
belong to h=L²((0,∞),du), and
\[
 c_j(s)=\int_0^\infty\frac{u^{2j}\Phi_s(u)}{(2j)!}du
\tag{3}
\]
exists and is finite and positive. Ordinary du is the metric; no extra Φ_s weight is inserted.
3. With the conjugate-linear first slot of h, the exact pairing rule is
\[
 \langle f_i,g_\ell\rangle_h=
 \begin{cases}
 c_{\ell-i}(s),&\ell\ge i,\\
 -\Phi_s^{(2(i-\ell)-1)}(0),&\ell<i.
 \end{cases}
\tag{4}
\]
4. For every integer q≥1 and k≥q−1, with normalized wedges,
\[
 \left\langle\bigwedge_{i=0}^{q-1}f_i,
                  \bigwedge_{j=0}^{q-1}g_{k+j}\right\rangle
 =D_{q,k}(s):=\det[c_{k+j-i}(s)]_{i,j=0}^{q-1}.
\tag{5}
\]
This includes k=q−1,q,q+1 for all filter settings. Lower nonnegative shifts use (4), including its odd endpoint entries. No estimate uniform as any derivative, moment or determinant index tends to infinity, and no determinant sign, is asserted.

## 2. Derivative recurrences and a complete spectral bound

Define the linear polynomial operation T(F)=(1−4x)F+4xF'. The chain rule reads
\[
 \partial_u[e^ue^{-x_n}F(x_n)]
   =e^ue^{-x_n}T(F)(x_n).
\tag{6}
\]
Use the prescribed recurrences
\[
 P_0=1,\quad P_{m+1}=T(P_m),\qquad
 H_0=2x^2-3x,\quad H_{m+1}=T(H_m).
\tag{7}
\]
Then deg P_m=m, deg H_m=m+2, with leading coefficients (−4)^m and 2(−4)^m respectively. The equality H_m=(P_{m+2}−P_m)/8 follows from H_0=(P_2−P_0)/8 and linearity of T. Thus the desired formulas are
\[
 p_s^{(m)}(u)=e^u\sum_{n\ge1}a_n(s)e^{-n^2x}P_m(n^2x),
 \quad
 \Phi_s^{(m)}(u)=e^u\sum_{n\ge1}a_n(s)e^{-n^2x}H_m(n^2x).
\tag{8}
\]
E02 Note07 §6 already justifies every fixed derivative by a uniform full-spectral tail. The following bound also retains source-variable decay, which is needed for half-line integration and the denominator in f_i.

For a polynomial F of degree d≥0 let A_F be the sum of its absolute coefficients (F=0 is handled by the zero bound). For N≥0 define
\[
 C_d(N)=\sum_{n>N}n^{2d}e^{-\pi(n^2-1)},\qquad C_d=C_d(0)<\infty.
\tag{9}
\]
Finiteness is elementary Gaussian summability. More explicitly, the complete-tail function T_p(L,ε) proved in [E02 Note07 (17)–(18)](07_MC11_AR_E02_R1_BOUNDED_POTENTIAL_DEFECT_AND_RIGIDITY_20261105.md#5-complete-sum-derivatives-and-explicit-tails) gives C_d(N)≤e^π T_{2d}(N+1,π), tending to zero as N→∞. Since x≥π>1 and 0≤a_n(s)≤1,
\[
 \left|e^u\sum_{n>N}a_n(s)e^{-n^2x}F(n^2x)\right|
 \le A_F C_d(N)e^u x^d e^{-x}.
\tag{10}
\]
Indeed |F(n²x)|≤A_F n^{2d}x^d and e^{−x(n²−1)}≤e^{−π(n²−1)}. The right side is bounded on u≥0 and its coefficient tends to zero. On every compact source interval it bounds the differentiated series as well; induction using (6) therefore proves (8) at each finite m, including its right endpoint values at u=0.

In particular, writing B_m=A_{H_m}C_{m+2},
\[
 |\Phi_s^{(m)}(u)|\le B_m e^u x^{m+2}e^{-x}.
\tag{11}
\]
The analogous p_s bound uses A_{P_m}C_m x^m. All constants here are allowed to depend on m, and are independent of s. Affine differentiation in s simply omits n=1 in (8); higher s derivatives of p_s, Φ_s and the moments vanish. No such affine claim is made for the nonlinear quotient f_i.

## 3. Positive ground-term bound and all half-line integrals

Every summand in Φ_s itself is nonnegative, because n²x≥π>3/2 and H_0(y)=y²(2−3/y)>0. Its n=1 coefficient is always one, so with κ=2−3/π>0,
\[
 \Phi_s(u)\ge e^{u-x}(2x^2-3x)
             \ge\kappa e^{u-x}x^2>0.
\tag{12}
\]
This is a uniform-in-s positive **function** lower bound, not a positive constant on the unbounded half-line. In particular the square root and division defining f_i are smooth, and the denominator is bounded away from zero on each compact source interval.

For fixed integer r≥0 and real d define the useful scalar integral
\[
 I_{r,d}=\int_0^\infty u^r e^u x^d e^{-x}du
 =\frac{\pi^{-1/4}}{4^{r+1}}\int_\pi^\infty
 [\log(x/\pi)]^r x^{d-3/4}e^{-x}dx<\infty.
\tag{13}
\]
Here u=log(x/π)/4 and du=dx/(4x), so every measure factor is explicit. Finiteness follows from the exponential tail and the positive lower endpoint π. The same reasoning proves u^r Φ_s^{(m)}(u)→0 as u→∞ and absolute integrability of every polynomially weighted finite derivative. On compact intervals all derivatives have finite continuous endpoint values.

Bound (10) gives an actual integrable full-spectral majorant: for every fixed r and polynomial F,
\[
 \int_0^\infty u^r\left|e^u\sum_{n>N}a_n(s)e^{-n^2x}F(n^2x)\right|du
 \le A_F C_d(N)I_{r,d}\longrightarrow0.
\tag{14}
\]
The same bound applies to the sum of the absolute values of its summands. Thus all termwise half-line integrations of the derivative/moment formulas used here are justified, uniformly in s. This strengthens convergence at each fixed index to precisely the weighted integrability needed; it does not supply index-uniform constants.

An optional exact general moment formula, obtained from (8) by Tonelli and y=πn²e^{4u}, is
\[
 c_j(s)=\frac1{4^{2j+1}(2j)!}
 \sum_{n\ge1}a_n(s)(\pi n^2)^{-1/4}
 \int_{\pi n^2}^\infty
 [\log(y/(\pi n^2))]^{2j}y^{-3/4}
 (2y^2-3y)e^{-y}dy.
\tag{15}
\]
All terms are nonnegative, and (11)–(13) show the sum is finite. This is one quantified formula for all j, not a moment table. It also gives the affine identity c_j(s)=(1−s)c_j(0)+sc_j(1). No numerical moment is acquired.

## 4. Hilbert membership at every finite index

Using the **same** source exponent in (11) and (12),
\[
 |f_i(u)|^2=\frac{|\Phi_s^{(2i)}(u)|^2}{\Phi_s(u)}
 \le\frac{B_{2i}^2}{\kappa}e^u x^{4i+2}e^{-x},
\tag{16}
\]
\[
 |g_\ell(u)|^2\le\frac{B_0}{((2\ell)!)^2}
             u^{4\ell}e^u x^2e^{-x}.
\tag{17}
\]
The denominator therefore does not destroy integrable decay. Equations (13), (16)–(17) prove
\[
 \|f_i\|_h^2\le\frac{B_{2i}^2}{\kappa}I_{0,4i+2},\qquad
 \|g_\ell\|_h^2\le\frac{B_0}{((2\ell)!)^2}I_{4\ell,2},\qquad
 0<c_j(s)\le\frac{B_0}{(2j)!}I_{2j,2}.
\tag{18}
\]
These estimates hold for all finite i,ℓ,j≥0, uniformly in s for each index. Positivity of c_j follows from (12) on the positive-measure open half-line. There is no missing origin condition: the functions are bounded on compact intervals, and (12) is nonzero at u=0. No Hamiltonian operator-domain or physical preparation assertion is used to prove membership in h.

## 5. Endpoint-preserving integration by parts

The source functions are real, so their ordinary du pairing is
\[
 \langle f_i,g_\ell\rangle
 =\int_0^\infty\Phi_s^{(2i)}(u)q_\ell(u)du,
 \qquad q_\ell(u)=u^{2\ell}/(2\ell)!.
\tag{19}
\]
Cauchy–Schwarz proves integrability, also directly supplied by §3. Perform integration by parts first on [0,R] and then send R→∞. All terms at R vanish by (11)–(13).

If ℓ≥i, integrate 2i times. Every origin term contains q_ℓ^{(r)}(0) with r≤2i−1<2ℓ, hence is zero. The final derivative is q_ℓ^{(2i)}=u^{2(ℓ−i)}/(2(ℓ−i))!, and the sign (−1)^{2i}=1. This proves the first branch of (4), including ℓ=i and i=0.

If ℓ<i, integrate 2ℓ times. The same origin cancellation holds for derivatives of q_ℓ below its degree, leaving
\[
 \int_0^\infty\Phi_s^{(2(i-\ell))}(u)du
 =\left[\Phi_s^{(2(i-\ell)-1)}(u)\right]_0^\infty
 =-\Phi_s^{(2(i-\ell)-1)}(0).
\tag{20}
\]
This also covers ℓ=0: no preliminary integration by parts is needed. The final odd endpoint is retained, rather than discarded by a parity assumption.

At s=1, the accepted complete-theta Jacobi identity gives p_1(u)−p_1(−u)=−sinh u on the real line. Applying ∂_u²−1 proves Φ_1 is even, so its odd endpoint derivatives vanish. This reuses AR-E01's source/reflection scope and does not extend it to a filtered source. More precisely, write Φ_0 for s=0 (the retained single angular shell). Affinity gives Φ_s=sΦ_1+(1−s)Φ_0 and hence, for every r≥0,
\[
 \Phi_s^{(2r+1)}(0)=(1-s)e^{-\pi}H_{2r+1}(\pi).
\tag{21}
\]
Formula (21) specifies the filtered endpoint correction symbolically; it imposes no vanishing at a general s. No parity of the physical radial kernel or wall condition has been substituted for this source calculation.

## 6. All finite shifted blocks and wedge normalization

For h with its fixed conjugate-linear first slot, use the prescribed coordinate wedge
\[
 (h_1\wedge\cdots\wedge h_q)(u_1,\ldots,u_q)
 =\frac1{\sqrt{q!}}\det[h_i(u_j)]_{i,j=1}^q.
\tag{22}
\]
For any h_i,k_j∈h, expansion of the two determinants gives
\[
 \langle h_1\wedge\cdots\wedge h_q,
         k_1\wedge\cdots\wedge k_q\rangle
 =\det[\langle h_i,k_j\rangle].
\tag{23}
\]
Each product term is absolutely integrable: its one-variable factors satisfy ∫|h_ik_j|≤||h_i||||k_j||, and there are finitely many permutation terms at each q. Thus Fubini is justified. Grouping the two permutation sums leaves q! equal contributions, canceled by the factor 1/q! from (22). No extra factorial remains and no orthonormality assumption is made.

For q≥1, integer k≥q−1, 0≤i,j<q, one has k+j≥q−1≥i. Applying the first branch of (4) to every entry gives (5). The smallest coefficient index is k−q+1≥0. In particular the three neighboring shifts k=q−1,q,q+1 all lie in range for every filter setting. For q=1 this reads simply <f_0,g_k>=c_k for every k≥0; no exceptional small-order hypothesis or computation is needed.

For any lower shift 0≤k<q−1, the same wedge identity remains valid with the matrix
\[
 M_{i,j}=\begin{cases}
 c_{k+j-i}(s),&k+j\ge i,\\
 -\Phi_s^{(2(i-k-j)-1)}(0),&k+j<i.
 \end{cases}
\tag{24}
\]
Its lower-index entries are endpoint data, not coefficients with artificially defined negative indices. At s=1 they vanish by reflection; no such simplification is imposed along the filtered path. Formula (24) is an endpoint dictionary and supplies no determinant sign.

## 7. Fixed spinor embedding and Fock direct sum

Preserve BR01's fixed smooth unit angular eigenspinor χ with Dχ=χ and the isometry
\[
 (Jf)(v,\omega)=\mathbf1_{\{v>0\}}f(v)\chi(\omega),\qquad
 \langle Jf,Jg\rangle_{H_C}=\langle f,g\rangle_h.
\tag{25}
\]
The equality follows by the ordinary product measure and ||χ||_K=1. In the metric-volume convention the spinor field is 2Jf because the angular area is dΩ/4; this constant factor restores the same norm, not an additional spectral multiplicity. J does not replace the angular trace in (1) by a rank-one expectation.

Tensoring an isometry preserves tensor-product inner products and commutes with antisymmetrization, so its induced maps ∧^qJ preserve every pairing (5) and (24). Zero extension chooses a Hilbert embedding, not a radial boundary condition on L_0. It does not show the embedded source functions belong to Dom D_C or Dom L_0, or that they are Hamiltonian eigenstates or prepared finite-energy states.

The standard fermionic Hilbert space is
\[
 \mathcal F_-(h)=\bigoplus_{q=0}^\infty\wedge^qh,
 \qquad\wedge^0h=\mathbb C,
 \quad\|(\Psi_q)_q\|^2=\sum_q\|\Psi_q\|^2<\infty.
\tag{26}
\]
The direct sum of ∧^qJ is an isometry into F_-(H_C). A fixed determinant order is one sector of this Hilbert space. No Hamiltonian, second quantization or interaction is chosen by (26), and no energy-domain claim follows. The Hilbert construction does not identify the two vector families, so it does not make the general determinant in (5) a Gram squared norm.

## 8. Evidence boundary and completed return

This is a general-index **source/domain/representation theorem**, classified under [avoid/01](../../../../../../../avoid/01_restating_the_target.md), not an RH criterion or a sign estimate uniform in q. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [re-realization caution](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [review-provenance rule](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) govern reuse.

The [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) is unchanged: weighted-square controls retain scalar Green/exterior constructions and fail exact unit coefficients/full normalized reflection; Euler-factor controls retain positive-source auxiliary constructions and fail the unchanged arithmetic source; reflected super-Gaussian controls retain reflection/Hilbert positivity and fail the complete integer-square expansion; smooth shape/positive-primitive controls retain their positive auxiliary channel and fail the exact arithmetic source. None is claimed to violate the present Hilbert or integration-by-parts identities. Even fixing theta merely identifies the object; a quantitative signed estimate requires its own premises and control screen. Lower-shift endpoint qualifications remain scoped as in [avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

**Completion:** one proof pass, no correction; every frozen finite-index source, membership, moment, endpoint, shift, embedding and Fock assertion has been proved. All activation input hashes and byte sizes remain unchanged. E02's full-sum estimates and the earlier wedge normalization were reused, not presented as a new numerical acquisition or independent review. Proof-author checks plus a read-only same-model supporting check provide internal evidence; a later AR-E04 assessment remains separate. No manuscript milestone or whole-investigation closure is claimed.

**Next: [B] MC11-B01 — Astra**, the existing at-most-two-route decision for a genuinely quantitative signed estimate, or a scoped stop. E05 remains reserved until B01 freezes its lemma and route. The continuation packet preserves that default sequence and records the separately selectable AR-E04 model/source assessment.
