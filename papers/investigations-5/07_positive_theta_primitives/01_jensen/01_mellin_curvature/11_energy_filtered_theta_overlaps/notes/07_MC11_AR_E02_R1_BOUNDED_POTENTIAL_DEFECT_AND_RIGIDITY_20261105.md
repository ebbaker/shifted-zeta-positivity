# MC11-AR-E02 r1: bounded-potential response defect and rigidity

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6.1-sol (Codex), actual recorded effort ultra**. Existing thread `01a1aa23-3513-7681-bad6-d8c15b6914fb`, MC11 history0003. **E — execution**, request r1. Sole artifact writer: this chat. A read-only same-model supporting check verified the summation/derivative bounds below; this is not independent specialist review.

**Status: proved in-note, with proof-author and same-model supporting checks; no separate specialist assessment.** All assertions of [BR01 Note06 §5](06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md#5-ar-e02-r1--intended-theorem-and-fixed-route) hold without a statement, constant, domain or readout correction. The [input/return record](../research-progress/handoffs/07_MC11_AR_E02_R1_INPUTS_AND_RETURN_20261105.json) identifies the six matched frozen inputs. [Register02](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) owns status; the [continuation](../research-progress/handoffs/07_MC11_AR_E02_RETURN_AND_AR_E03_MODEL_CONTINUATION_20261105.md) leaves AR-E03 unstarted under its unchanged frozen r1 contract.

## 1. Fixed operator, readout and theorem

Use the accepted complete-cylinder Hilbert space H_C=L²(R,dv;K), K=L²(S²,Σ;dΩ), with both signs of the unit-sphere Dirac D, and P_n the D²=n² block of dimension 4n. Reuse AR-E01's full-line L_0=-∂_v²+4D² and domain. For a real equivalence class V∈L∞(R), V≥0 almost everywhere, put M=||V||∞ and
\[
 L_V=L_0+VI,\quad \operatorname{Dom}L_V=\operatorname{Dom}L_0,
 \qquad H_{n,V}=-\partial_v^2+4n^2+V,
 \quad \operatorname{Dom}H_{n,V}=H^2(\mathbb R).
\tag{1}
\]
V is independent of n,s,t,u. Fix the interior probe at v=0, the dimensionless angular weight convention and the external filter B_s=P_1+s(I-P_1), 0≤s≤1. There is no compensating multiplier after V is added. Define
\[
 b_n=4nG_{n,V}(0,0),\quad d_n=1-b_n,\quad
 a_1(s)=1,\quad a_n(s)=s\ (n\ge2).
\tag{2}
\]

**Theorem.** The operators (1) are self-adjoint and strictly positive. Each scalar inverse has a continuous, symmetric, strictly positive Green kernel, and for every n≥1,
\[
 \frac{2n}{\sqrt{4n^2+M}}\le b_n\le1,
 \qquad
 0\le d_n\le1-\left(1+\frac{M}{4n^2}\right)^{-1/2}
 \le\frac{M}{8n^2}.
\tag{3}
\]
If V is **not equal to zero a.e.**, equivalently {V>0} has positive measure, then d_n>0 for every n. Here and below “nonzero V” always has this meaning; positivity at a null set alone has no effect.

The angular-operator-valued radial kernel K_V of L_V⁻¹ has a well-defined radial diagonal and, for every t>0 and 0≤s≤1,
\[
 R_{V,s}(t)=\operatorname{Tr}_K[B_se^{-tD^2}K_V(0,0)]
          =\sum_{n\ge1}a_n(s)b_ne^{-tn^2},
\]
\[
 \Delta_{V,s}(t):=Q_s(t)-R_{V,s}(t)
          =\sum_{n\ge1}a_n(s)d_ne^{-tn^2}.
\tag{4}
\]
Exact recovery R_{V,s}(t)=Q_s(t) at even one such pair (s,t) holds **if and only if V=0 a.e.** The complete-sum derivatives, explicit tails and external source-composition estimates are proved in §§5–6. The statement is scoped to (1) and the fixed readout; it covers neither signed/unbounded potentials, walls, other geometries nor compensating observations.

## 2. Self-adjointness and an explicit positive kernel

Real bounded multiplication is self-adjoint and bounded. Thus its addition leaves the self-adjoint operator domains in (1) unchanged; the quadratic forms give L_V≥4I and H_{n,V}≥4n²I. This is also the bounded, relative-bound-zero case of [Teschl, second edition, Theorem 6.4, printed p.159](https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). No kernel positivity is inferred from that abstract perturbation theorem.

Fix arbitrary n and write a=2n, λ=√(a²+M), U=M−V, so 0≤U≤M. For M=0, V=0 a.e. and the accepted free kernel suffices. For M≥0, let
\[
 g_\lambda(z)=\frac{e^{-\lambda|z|}}{2\lambda},\qquad
 A_M=-\partial_v^2+\lambda^2,\qquad S=A_M^{-1}.
\tag{5}
\]
The free-kernel formula applies with this positive mass. It has ||g_λ||_1=λ⁻², ||g_λ||∞=(2λ)⁻¹. Since H_{n,V}=A_M−U and
\[
 \|SU\|\le\rho:=\frac{M}{a^2+M}<1,
 \qquad H_{n,V}^{-1}=(I-SU)^{-1}S
                  =\sum_{j=0}^{\infty}(SU)^jS,
\tag{6}
\]
the inverse has an explicit positive expansion. To justify its pointwise use, set K_0(v,w)=g_λ(v−w) and
\[
 K_j(v,w)=\int_{\mathbb R^j}g_\lambda(v-x_1)U(x_1)
 g_\lambda(x_1-x_2)\cdots U(x_j)g_\lambda(x_j-w)\,d\mathbf x
 \quad(j\ge1).
\tag{7}
\]
All integrands are nonnegative, defined using any representative of U in [0,M]. They obey
\[
 0\le K_j(v,w)\le M^j g_\lambda^{*(j+1)}(v-w),
 \qquad \sup_{v,w}K_j(v,w)\le\frac{\rho^j}{2\lambda}.
\tag{8}
\]
Every K_j is jointly continuous, even for measurable V: translations of the outer exponential kernels are continuous in L¹, the inner integrations are uniformly bounded by (8), and the same argument applies to each endpoint. Their uniformly convergent sum G_{n,V}=Σ_jK_j is therefore continuous. Reversing the path in (7) proves symmetry.

The convolution majorant sums to the free mass-a kernel:
\[
 \sum_{j\ge0}M^jg_\lambda^{*(j+1)}=g_a.
\tag{9}
\]
Indeed the series converges in L¹ (its jth L¹ norm is λ⁻²ρ^j), and its Fourier transform is the geometric series
\[
 \sum_{j\ge0}\frac{M^j}{(k^2+\lambda^2)^{j+1}}
 =\frac1{k^2+a^2}.
\]
Uniform convergence and continuity identify the kernels at every point, not only almost everywhere. Consequently
\[
 0<g_\lambda(v-w)\le G_{n,V}(v,w)\le g_a(v-w)
 \quad\text{for all }v,w\in\mathbb R.
\tag{10}
\]
The series of integral operators in (7) agrees with (6), initially on compactly supported test functions by absolute domination and then on L² by boundedness. This constructs the continuous representative of the inverse kernel and justifies its diagonal. It is an explicit comparison with constant potentials M and 0, rather than an unproved inference from operator order to point values.

For completeness the distributional equation is H_{n,V}G_{n,V}(·,w)=δ_w. Away from w its first derivative is locally absolutely continuous and G''=(a²+V)G almost everywhere. Integrating the equation across w shows the derivative jump is −1. The upper exponential bound in (10) gives decay at both ends. Uniqueness within this decaying Green class follows because the difference is in L², its second derivative is in L², and the positive H² realization has trivial kernel. No regularity of V beyond bounded measurability was used.

## 3. Resolvent defect, diagonal comparison and strictness

The bounded-perturbation resolvent identity gives
\[
 H_{n,0}^{-1}-H_{n,V}^{-1}=H_{n,0}^{-1}V H_{n,V}^{-1}.
\]
Its kernel identity holds at every v,w:
\[
 g_a(v-w)-G_{n,V}(v,w)
 =\int_{\mathbb R}g_a(v-x)V(x)G_{n,V}(x,w)\,dx.
\tag{11}
\]
To pass from operators to kernels, the integral is absolutely bounded by M(g_a*g_a)(v−w), and its endpoint translations are continuous by L¹ translation continuity and (10). The operator identity first identifies these kernels distributionally; continuity then gives equality everywhere. This includes v=w=0, so no L² point evaluation is being presumed bounded.

At that diagonal the integral is finite; explicitly
\[
 0\le\int g_a(-x)V(x)G_{n,V}(x,0)dx
 \le M\int g_a(x)^2dx=\frac{M}{4a^3}.
\tag{12}
\]
If V is nonzero, its positive-measure support meets strictly positive factors g_a(-x) and G_{n,V}(x,0), so the integral is strictly positive for this arbitrary n. Multiplication by 4n proves d_n>0 for every n, including n=1. A nonnegative potential supported far from the probe still has a strict, possibly small, response loss.

At the diagonal (10) yields 1/(2λ)≤G_{n,V}(0,0)≤1/(2a). Since 4n=2a, this proves the first two bounds in (3). For z≥0,
\[
 1-(1+z)^{-1/2}=\frac12\int_0^z(1+y)^{-3/2}dy\le z/2,
\]
which proves its final constant M/(8n²). The direct integral estimate (12), after multiplication by 4n, gives the same last bound. For constant V=M, the lower b_n bound is attained; this is an exact analytic consistency check, not a finite-mode test.

## 4. The complete-cylinder kernel and rigidity of the readout

Angular separation is exact because the scalar V commutes with every P_n. The inverse on H_C is the direct sum of H_{n,V}⁻¹ with multiplicity 4n. It has the angular-operator-valued radial kernel
\[
 K_V(v,w)=\sum_{n\ge1}G_{n,V}(v,w)P_n.
\tag{13}
\]
By (10), the norm of its discarded n>N part is at most 1/[4(N+1)], and ||K_V(v,w)||≤e^{-2|v-w|}/4. Thus (13) is a norm-continuous bounded kernel and represents L_V⁻¹ by the same direct-sum/Schur argument as AR-E01. In particular K_V(0,0) is positive and well defined.

For t>0, B_se^{-tD²}K_V(0,0) is positive trace class because its trace is bounded by Σe^{-tn²}. Its block trace is exactly 4nG_{n,V}(0,0), proving (4) and accounting for every radial contribution. This is an angular trace of a radial diagonal. The full-space trace still diverges: the constant-M lower kernel bound is uniform in the radial diagonal and leaves a positive angular density integrated over all v. No full thermal partition function has replaced the prescribed response.

If V=0 a.e., AR-E01 gives b_n=1 and (4) recovers Q_s for every (s,t). If V is nonzero, (11) gives d_1>0, hence
\[
 \Delta_{V,s}(t)\ge d_1e^{-t}>0,
 \qquad t>0,\quad0\le s\le1.
\tag{14}
\]
This proves exact-recovery rigidity at even one observed pair, including s=0. The ground **angular** shell is always retained by B_s; no normalizable full-cylinder ground state is asserted. Dividing a shell's readout by b_n would change the fixed observation and is outside this theorem.

## 5. Complete-sum derivatives and explicit tails

For each integer m≥0, Gaussian domination and (3) give
\[
 (-1)^m\partial_t^m\Delta_{V,s}(t)
 =\sum_{n\ge1}a_n(s)d_nn^{2m}e^{-tn^2},
\]
\[
 0\le(-1)^m\partial_t^m\Delta_{V,s}(t)
 \le\frac M8\sum_{n\ge1}a_n(s)n^{2m-2}e^{-tn^2}.
\tag{15}
\]
The remainder after n≤N satisfies exactly the same inequality with n>N. Here m=0 legitimately gives exponent −2; n starts at 1. Also
\[
 \partial_s\partial_t^m\Delta_{V,s}(t)
 =(-1)^m\sum_{n\ge2}d_nn^{2m}e^{-tn^2},\qquad
 \partial_s^j\Delta_{V,s}=0\quad(j\ge2).
\tag{16}
\]
At s=0,1 these are the derivatives of the affine extension in s, equivalently the appropriate one-sided derivatives. The response R and Q have analogous differentiated series, with b_n and 1 respectively.

An explicit bound proves all the asserted exchanges and includes the entire infinite tail. For real p, ε>0 and integer L≥1 define
\[
 C_{p,\varepsilon}=\begin{cases}1,&p\le0,\\
 (p/(e\varepsilon))^{p/2},&p>0,\end{cases}\qquad
 T_p(L,\varepsilon)=C_{p,\varepsilon}
 \frac{e^{-\varepsilon L^2/2}}
 {1-e^{-\varepsilon(2L+1)/2}}.
\tag{17}
\]
For t≥ε,
\[
 \sum_{n\ge L}n^pe^{-tn^2}\le T_p(L,\varepsilon).
\tag{18}
\]
For p≤0 use n^p≤1. For p>0, maximizing x^p e^{-εx²/2} over x>0 gives C_{p,ε}. The remaining sum of e^{-εn²/2} is bounded geometrically because (L+j)²≥L²+(2L+1)j for integers j≥0. Thus, for every integer N≥0,
\[
 \left|\partial_t^m\sum_{n>N}a_n(s)d_ne^{-tn^2}\right|
 \le\frac M8 T_{2m-2}(N+1,\varepsilon).
\tag{19}
\]
For its mixed s derivative replace N+1 by max(N+1,2). For R or Q, use T_{2m} without M/8. These bounds are uniform in t≥ε and s∈[0,1], tend to zero as N→∞, and apply at each fixed m. They establish smoothness in t and termwise mixed differentiation. They assert no uniform estimate as m→∞ or t↓0.

## 6. Every finite derivative of the external source composition

Keep t(u)=πe^{4u}, u≥0, distinct from radial probe v=0 and physical heat time τ. To track the fixed map only, put p_{V,s}=e^uR_{V,s}(t(u)) and Φ_{V,s}=(∂_u²−1)p_{V,s}/8. These are deformed comparison functions when V≠0 and are not renamed theta. Set δp=p_s−p_{V,s}, δΦ=Φ_s−Φ_{V,s} and x_n=t(u)n².

With the **same prescribed** polynomials
\[
 P_0=1,\quad P_{m+1}=(1-4x)P_m+4xP_m',
 \qquad H_0=2x^2-3x,\quad H_{m+1}=(1-4x)H_m+4xH_m',
\tag{20}
\]
the chain rule gives, at every fixed finite m,
\[
 \partial_u^m\delta p=e^u\sum_{n\ge1}a_n(s)d_ne^{-x_n}P_m(x_n),
 \qquad
 \partial_u^m\delta\Phi=e^u\sum_{n\ge1}a_n(s)d_ne^{-x_n}H_m(x_n).
\tag{21}
\]
Indeed ∂_u[e^ue^{-x}F(x)]=e^ue^{-x}[(1−4x)F+4xF']; (P_2−P_0)/8=2x²−3x. The same formulas with d_n replaced by b_n hold for p_V,s and Φ_V,s. This verifies the required differentiations of the observation without executing E03's membership, moments or pairings.

Here is an explicit bound valid even on the whole source half-line. For a nonzero polynomial F(x)=Σ_{j=0}^d f_jx^j define A_F=Σ|f_j|, α=d+1/4 and K_α=(2α/e)^α. If |c_n|≤C n^{-κ}, κ≥0, then
\[
 \sup_{u\ge0}\left|e^u\sum_{n\ge L}c_ne^{-x_n}F(x_n)\right|
 \le C A_F\pi^{-1/4}K_\alpha
 \frac{L^{-\kappa-1/2}e^{-\pi L^2/2}}
 {1-e^{-\pi(2L+1)/2}}.
\tag{22}
\]
For F=0 the bound is zero. To prove (22), x_n≥π>1 gives |F(x_n)|≤A_F x_n^d; also e^u=π^{-1/4}x_n^{1/4}n^{-1/2} and x^αe^{-x/2}≤K_α. Leave e^{-x_n/2}≤e^{-πn²/2}, bound n^{-κ-1/2} by its value at L, and sum as in (18).

Apply (22) with C=M/8, κ=2 to every fixed P_m,H_m for defect tails; with C=1, κ=0 to the response/free source. For mixed s differentiation omit n=1 and replace L by max(L,2). All higher s derivatives vanish. The resulting series and all specified finite derivatives converge uniformly on u≥0 and s∈[0,1]. Constants depend on the polynomial/derivative order. No moving-probe derivatives, potential derivatives, uniform-in-index estimate, half-line moment integral or determinant estimate is hidden in this argument.

## 7. Controls, completion and next boundary

This is a **proved scoped response-defect/rigidity theorem**, classified under [avoid/01](../../../../../../../avoid/01_restating_the_target.md); it is not a new RH criterion or a signed determinant bound. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [re-realization caution](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped-exclusion rule](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) delimit reuse.

The [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) is applied to the actual premises: weighted-square controls retain the positive scalar Green comparison and fail canonical unit shell coefficients/full normalized reflection; Euler-factor modifications retain generic positive-source Hilbert constructions and fail the unchanged canonical arithmetic trace; reflected super-Gaussian controls retain reflection and Hilbert/Fock positivity and fail literal integer-square theta expansion; smooth shape/positive-primitive controls retain their positive auxiliary channel and fail the exact canonical arithmetic source. None is claimed to violate (3) or (15). Those are generic scalar response bounds and give no collision exclusion or sign of a cross-determinant. Merely fixing theta identifies the source, not a new separating inequality.

**Completion:** one analytic derivation using the allowed constant-M resolvent expansion, kernel comparison/identity and Gaussian summation; no additional regrouping was needed. No assertion or constant correction, numerical acquisition, spectral scan, potential search, new wall or compensating readout was used. All six frozen input hashes and byte sizes matched at activation and remain unchanged. This result has proof-author checks plus a read-only same-model complete-sum check, not a separate assessment or specialist review; [avoid/05](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) applies. No manuscript milestone or whole-investigation closure is claimed.

**Next: [E] MC11-AR-E03 r1 — Sol**, at V=0 under BR01's unchanged source/pairing contract. This return satisfies its E02 prerequisite and makes it ready for separate activation. The theorem does not activate that task. Physical preparation choices still belong to BR01; a signed all-order estimate remains MC11-B01/E05.
