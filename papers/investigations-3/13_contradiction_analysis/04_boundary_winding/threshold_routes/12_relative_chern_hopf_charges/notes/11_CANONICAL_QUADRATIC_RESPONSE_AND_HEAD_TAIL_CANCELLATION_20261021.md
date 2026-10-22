# Canonical quadratic response and head tail cancellation

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. The fixed-time endpoint route is the user's
selected priority. This note supplies a complete signed quadratic
estimator using the actual canonical law, and identifies the leading
head–tail cancellation near a hypothetical double. It supplies no
positive endpoint margin for theta.

The starting point is [Note 10][n10] and the [manuscript's exact
response][source]. The [result index][results], [control register][controls]
and [avoid index][avoid] apply, particularly [target classification][a01],
[matched premises][a02] and [coupled estimates][a12]. The estimator is a
quantitative intermediate result; endpoint positivity remains the target.
The related [large-time analysis][n12] answers whether infinity can provide
the missing endpoint information. [Review 11][review] records internal
same-model checks of this round.

## 1 A signed quadratic response with the complete residual

Work at t=0, with a real-symmetric reference F and H=F+E, holomorphic
near |z−a|≤R for real a. Assume F is nonzero on Γ={|z−a|=R}, with
exactly two roots counted with multiplicity inside, both in |z−a|<r<R.
Let c be their centroid, |F|≥δ>0 on Γ, and sup_Γ|E/F|≤ρ<1. Define
\[
 I[g]=\frac1{2\pi i}\oint_\Gamma g(z)\,dz,
 \qquad L_F(V)=-4I[(z-c)V/F],
\]
\[
 B_F(V,W)=2I[(z-c)VW/F^2]-I[V/F]I[W/F],\qquad Q_F(V)=B_F(V,V).
\]
The complete discriminant response is
\[
 \Delta_H=\Delta_F+L_F(E)+Q_F(E)+R_3,\qquad |R_3|\le C_3(\rho),       \tag{1}
\]
\[
 C_3=4R(R+r)l_3+R^2(2\rho l_2+l_2^2),\quad
 l_2=-\log(1-\rho)-\rho,\quad l_3=l_2-\rho^2/2.
\]
This is Note 10's proved cubic allowance. It follows by retaining the
quadratic term in log(1+E/F) and the centroid square in the exact response.
Set
\[
 C_L=\frac{4R(R+r)}\delta,
 \qquad C_B=\frac{2R(R+r)+R^2}{\delta^2}.
\]
For the contour sup norm,
\[
 |L_F(V)|\le C_L\|V\|_\Gamma,\qquad
 |B_F(V,W)|\le C_B\|V\|_\Gamma\|W\|_\Gamma.              \tag{2}
\]
These estimates contain no inverse internal root separation.

If E(z)=∫ψ(u)cos(zu)du is a complete residual with
∫|ψ(u)|cosh(Ru)du<∞, define
\[
 \alpha(u)=I[\cos(zu)/F],
\]
\[
 K_2(u,v)=2I[(z-c)\cos(zu)\cos(zv)/F^2]-\alpha(u)\alpha(v).
\]
Then
\[
 Q_F(E)=\iint\psi(u)\psi(v)K_2(u,v)\,du\,dv,
 \quad |K_2(u,v)|\le C_B\cosh(Ru)\cosh(Rv).                \tag{3}
\]
The majorant proves Fubini, including the complete source rays. Reality
and symmetry make K_2 real and symmetric. All cross terms in the same
residual are retained.

There is no generic favorable sign. At a reference double
F=U(z)(z−b)², put h=E/U. Residues give
\[
 Q_F(E)=h'(b)^2+2h(b)h''(b).                              \tag{4}
\]
For F=(z−b)² with b>0 and E=cos(uz), this equals
u²(1−3cos²(bu)), which has both signs for positive one-atom residuals.
Multiplying E by a sufficiently small positive constant pays ρ<1.
The reference and residual extend as heat solutions
(z−b)²−2t and e^(tu²)cos(uz). Smooth nonnegative approximations to the
atom preserve the strict signs. This screens positivity of Q from
positive residual mass alone; it asserts no global theta-like root behavior.

## 2 Approximate the actual canonical law with one common residual

Use the unshifted canonical head
\[
 F_M(z)=\int_0^\infty S_M(u)\cos(zu)\,du,\quad
 E(z)=\int_0^\infty R_M(u)\cos(zu)\,du,
 \quad S_M=\sum_{n\le M}\phi_n,
\]
with the complete tail R_M=Σ_(n>M)φ_n. Suppose F_M satisfies the
reference hypotheses above. The canonical-tail theorem gives
\[
 R_M(u)=W(u)\{\mathsf A_M+(\mathsf E_M-\mathsf A_M)z_M(u)\},
\]
where W=φ_M(u)exp[−(λ_(M+1)−λ_M)(e^(4u)−1)],
\(\mathsf E_M=R_M(0)/\phi_M(0)>\mathsf A_M>0\), and
\(z_M(u)=\sigma_M([u,\infty))\) for the explicit canonical probability
measure σ_M. The masses come from the complete Laplace law in the
manuscript, not a freely chosen monotone multiplier.

On the compactified half-line define the probability measure
\[
 \lambda_M=\frac{\mathsf A_M}{\mathsf E_M}\delta_\infty
       +\left(1-\frac{\mathsf A_M}{\mathsf E_M}\right)\sigma_M,
 \quad V_w(z)=\int_0^w W(u)\cos(zu)\,du.
\]
The value w=∞ denotes the complete integral. Fubini gives
\[
 E=\mathsf E_M\int V_w\,d\lambda_M(w),                    \tag{5}
\]
and hence both the linear and quadratic responses use this same law:
\[
 L_F(E)=\mathsf E_M\int L_F(V_w)d\lambda_M,
 \quad Q_F(E)=\mathsf E_M^2\iint B_F(V_v,V_w)d\lambda_M(v)d\lambda_M(w).
                                                               \tag{6}
\]
In particular, the quadratic correction is not an independent adjustment
of the linear-response probability distribution.

Here is an explicit convergent enclosure. Put
\[
 N(w)=\int_0^wW(u)\cosh(Ru)\,du,\qquad N_\infty=N(\infty).
\]
Partition [0,∞] into J ordered intervals I_j, retaining the atom at
infinity in the last one. Set p_j=λ_M(I_j) and
n_j=N(b_j)−N(a_j), with N(∞)=N_∞. Choose w_j at the midpoint in
N-coordinate, so N(w_j)=(N(a_j)+N(b_j))/2, and define
\[
 \widehat E=\mathsf E_M\sum_jp_jV_{w_j}.
\]
Then
\[
 \|E-\widehat E\|_\Gamma\le
 \epsilon_J:=\frac{\mathsf E_M}{2}\sum_jp_jn_j,
 \qquad \|E\|_\Gamma,\|\widehat E\|_\Gamma\le\mathsf E_M N_\infty.
                                                               \tag{7}
\]
Indeed |V_w−V_(w_j)|≤|N(w)−N(w_j)|≤n_j/2 throughout a cell,
including w=∞. Integrating gives (7). Bilinearity and (2) now give
\[
 |L_F(E)+Q_F(E)-L_F(\widehat E)-Q_F(\widehat E)|
 \le\mathcal E_J:=(C_L+2C_B\mathsf E_M N_\infty)\epsilon_J.      \tag{8}
\]
If n_j≤N_∞/J, this is an explicit O(J⁻¹) law-approximation error.
All constants are displayed; they depend on the external wall and the
complete tail. Only one common residual approximation and its contour
response are needed: a separate J² acquisition of every bilinear cell
is not mathematically required. This is not a comparative runtime claim.

With exact actual p_j, another valid enclosure integrates cell infima
and suprema of
\[
 G(v,w)=\frac{\mathsf E_M}{2}\{L_F(V_v)+L_F(V_w)\}
                  +\mathsf E_M^2B_F(V_v,V_w)
\]
against p_jp_k. Such range enclosures are nested under partition
refinement. The midpoint error enclosures (7)–(8) need not themselves
be nested; intersecting valid successive intervals preserves validity.
Certified acquisition and mass errors must be added. For example,
coefficient errors |p_j−p̂_j|≤ε_j contribute at most
\(\mathsf E_M N_\infty\sum_j\epsilon_j\) to the residual error,
with any error in \(\mathsf E_M\) paid separately. Signed responses
must not use invalid lower-mass multiplication on negative terms.
For nonnegative normalized approximate weights the same residual-norm
bound used in (8) remains valid. For an otherwise unrestricted extra
residual error η, add the safe response allowance
\((C_L+2C_B\mathsf E_MN_\infty)\eta+C_B\eta^2\).

Combining (1) and (8) yields the complete analytic lower bound
\[
 \boxed{\Delta_H(0)\ge
 \Delta_F+L_F(\widehat E)+Q_F(\widehat E)
                      -\mathcal E_J-C_3(\rho).}                 \tag{9}
\]
Here ρ is a proved bound for the **actual** E/F; for example
\(\mathsf E_M N_\infty/\delta<1\) suffices. Formula (9) excludes
an endpoint double only when its right side, including any numerical
acquisition errors, is strictly positive. No such theta sign is asserted.

## 3 What a long canonical head does at a hypothetical double

The actual tail has a definite local sign once its cutoff is large.
Write β=π(M+1)² and ε_M=∫R_M(u)du, distinguishing this physical
tail mass from the normalized mass \(\mathsf E_M\) above.
For one mode
\[
 \phi_\lambda(u)=\lambda e^{5u}(2\lambda e^{4u}-3)e^{-\lambda e^{4u}},
 \quad m_j(\lambda)=\int_0^\infty u^j\phi_\lambda(u)du.
\]
For λ≥9 the complete elementary bounds are
\[
 m_2(\lambda)\le\frac{4e^{-\lambda}}{27\lambda},\qquad
 m_0(\lambda)\ge\frac{3\lambda e^{-\lambda}}{32}.          \tag{10}
\]
For the upper bound use e^(4u)≥1+4u and
φ_λ≤2λ²e^(−λ)e^(−3λu), then integrate u². For the lower bound
restrict to 0≤u≤1/(4λ). There λe^(4u)≤λ+9/8, because
e^x≤1/(1−x) for 0≤x<1; also 2λ−3≥3λ/2 and e^(9/8)<4.
Thus φ_λ≥3λ²e^(−λ)/8 on that interval, proving (10).
Their ratio is at most 128/(81λ²)<2/λ². Summing every omitted mode gives
\[
 \int u^2R_M(u)du\le2\beta^{-2}\epsilon_M,
 \quad E(0,a)\ge\epsilon_M(1-a^2/\beta^2)>0
 \quad(\beta\ge9,\ \beta>|a|),                            \tag{11}
\]
using cos(au)≥1−a²u²/2. This is an actual canonical-tail sign, not
the sign of the full discriminant in (9).

On every fixed compact complex spacetime set, the same estimates imply
\[
 E(t,z)=\epsilon_M\{1+O(\beta^{-2})\},\qquad
 E_z(t,z),E_t(t,z)=O(\epsilon_M\beta^{-2}).                 \tag{12}
\]
To justify the uniform errors, bound e^(tu²)cos(zu)−1 by
C u²e^(T u²+Z u) for the chosen compact set. The inequality
e^(4u)≥1+4u+8u² absorbs this factor into the mode envelope for all
sufficiently large λ; integrating again gives O(λ⁻²) relative to
the lower mass in (10). The derivative estimates follow in the same way.
More fixed derivatives are bounded as needed on a slightly larger compact
set. Substituting v=λu in m_0 and dominated convergence gives
m_0(λ)∼λe^(−λ)/2. The bound m_0(λ)≤2λe^(−λ)/3 and the increasing
square-node spacings show that the first omitted mode dominates the
remaining sum. Consequently ε_M∼βe^(−β)/2.

Now suppose conditionally that H has an ordinary double at (0,a).
Put N=H_zz(0,a)≠0 and M_3=H_zzz(0,a). The event Jacobian is
\(\left(\begin{smallmatrix}-N&0\\-M_3&N\end{smallmatrix}\right)\),
with nonzero determinant. The implicit-function theorem, applied to
the small analytic perturbation F_M=H−E, gives a unique nearby real
head event. Taylor expansion of its two event equations and (12) gives
\[
 \tau_M=-\frac{\epsilon_M}{N}
       +O(\epsilon_M\beta^{-2}+\epsilon_M^2),\qquad
 b_M=a-\frac{M_3\epsilon_M}{N^2}
       +O(\epsilon_M\beta^{-2}+\epsilon_M^2).              \tag{13}
\]
The constants depend on the fixed hypothetical event. In particular
the head event is negative for N>0 and positive for N<0, for sufficiently
large M. Adding the tail returns that event to zero under the hypothesis.
A negative head event is therefore not a negative theta event.

The same cancellation appears directly at t=0. On a fixed proper
window about the assumed double, all reference walls are uniformly
nonzero for sufficiently large M. Apply the response first to H−E
using H as reference, then use continuity of the contour expressions:
\[
 \Delta_{F_M}=\frac{8E(0,a)}N+O(\epsilon_M^2),\qquad
 L_{F_M}(E)=-\frac{8E(0,a)}N+O(\epsilon_M^2).              \tag{14}
\]
The quadratic response reduces the remaining discrepancy to
\(\Delta_{F_M}+L_{F_M}(E)+Q_{F_M}(E)=O(\epsilon_M^3)\),
as (1) requires when Δ_H=0. Thus longer cutoff and a positive tail
value do not themselves create a positive endpoint surplus.

## 4 Scope and continuation

The estimator (9) is now explicit with a complete O(J⁻¹) law error
and a cubic response error. Its next substantive use must estimate the
combined signed quantity, retaining the canonical coefficients and all
residual interactions. The canonical tail sign (11) and event shift (13)
identify a real cancellation that any such use must overcome; they do not
prove a universal obstruction to theta-specific inequalities.

The quadratic heat and positive-atom controls test (1)–(4) without
assuming its sign. The broader [collision controls][controls] retain
their separate premises: Euler factors change arithmetic; weighted-square
and finite-prime sources lack the complete normalized reflection conjunction;
reflected and primitive sources lack canonical square data. Close normalized
endpoint sources fail ordinary Dirichlet-series arithmetic. The canonical
head theorem here uses the exact θ tail, whereas the bilinear identities
are generic and should hold for colliding controls. No independent global
real-rootedness is assigned to a truncated head.

ECE-02 remains open for a positive unchanged-theta margin; ECE-03 remains
gated. No new theta numerical region or manuscript revision is claimed.
The [progress register][progress] records this estimator and the separate
infinity-time findings without changing endpoint-exclusion statuses.

[n10]: 10_ANALYTIC_OBSTACLES_AND_ESTIMATION_PRIORITIES_20261021.md
[n12]: 12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[source]: ../manuscript/source.tex
[review]: ../reviews/11_SIGNED_RESPONSE_AND_INFINITY_TRANSFER_REVIEW_20261021.md
[progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
