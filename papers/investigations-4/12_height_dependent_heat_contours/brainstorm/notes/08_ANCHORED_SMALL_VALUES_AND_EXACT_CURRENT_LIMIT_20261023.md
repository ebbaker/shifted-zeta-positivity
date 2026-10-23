# Anchored small-value bounds and the exact smooth-current limit

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Derivation with collaborating same-model agents; [separate-agent internal review][review], not specialist review or formal verification.

**Status: proved in-note, using the cited polynomial-root regularity theorem.** On the finite analytic scope of [Note 07][previous], the smooth current converges to the actual positive variation of the complete zero divisor. A quantitative anchor and complete-source upper bounds give a finite small-value bound, including a coarse application to theta on negative time. No useful growing-height constant, improved backward width, or simplicity conclusion is established. Universal constants from the imported theorem are not numerically evaluated here.

This continues [Continuation 05][continuation] at the point reached by Note 07 and the [OBF register][progress]. It does not repeat the completed transport audit. The [result index][results], [collision controls][controls], and [avoid index][avoid] govern the interpretation, especially [target classification][a01], [scope][a07], and [coupled estimates][a12]. The result is a finite quantitative estimate and a convergence theorem, not an RH-equivalent criterion. Finiteness is distinguished throughout from a small allowance useful to the endpoint consumer.

## 1. The field and the quantity being estimated

Keep I=[−ε,0], a compactly supported C² window ψ, and the finite analytic/event hypotheses of Note 07. Write S=supp ∇ψ. Let B be a specified holomorphic nonvanishing carrier on a neighborhood of the sets used, and put f=H/B. The choice B=1 is allowed. Define

\[
q=-f_t=\mathcal T_Bf,
\qquad
\mathcal T_Bf=f_{zz}+2(B_z/B)f_z+(B_t/B+B_{zz}/B)f.
\tag{1}
\]

Thus every carrier term is retained. The root velocity at a simple zero of f is q/f_z. Introduce

\[
W(r)=\int_I\int_S\mathbf1_{|f|\le r}|\nabla\psi|\,|q\overline{f_z}|\,dA\,dt,
\quad
Q_\rho=\int_I\int_S k_\rho(f)
 [\operatorname{Re}\{D\psi\,q\overline{f_z}\}]_+\,dA\,dt,
\tag{2}
\]
\[
k_\rho(w)=\frac{\rho^2}{\pi(|w|^2+\rho^2)^2},
\qquad D\psi=\psi_x-i\psi_y.
\]

The unknown smooth nonreal inflow is F⁺_{ψ,nr} from Note 07. It is bounded by F⁺_{ψ,all}, which also pays real-root motion. Neither is identified with the number of entries through a sharp spatial wall. Recrossings and repeated inward motion are included by positive variation.

For almost every complex target w, define the level-track variations

\[
V_{\rm abs}(w)=\int_I\sum_{f(t,z)=w}
 |\nabla\psi(z)|\left|\frac{-f_t}{f_z}(t,z)\right|dt,
\quad
V_+(w)=\int_I\sum_{f(t,z)=w}
 \left[\operatorname{Re}\left\{D\psi(z)\frac{-f_t}{f_z}(t,z)\right\}\right]_+dt.
\tag{3}
\]

Only roots meeting the weighted support contribute. Quotients are used at regular preimages, with the almost-everywhere interpretation justified below. The holomorphic area formula on each spatial slice, followed by Tonelli, gives

\[
\boxed{W(r)=\int_{|w|\le r}V_{\rm abs}(w)\,dA_w,
\qquad Q_\rho=\int_{\mathbb C}k_\rho(w)V_+(w)\,dA_w.}
\tag{4}
\]

Indeed the spatial Jacobian is |f_z|²; division by it leaves precisely the velocity in (3). Critical preimages contribute zero to the original density and their critical values form a planar null set at each time. Fubini permits exceptional pairs (t,w) to be discarded. A spatially constant nonzero slice contributes zero to (2) and does not affect this argument. Persistent multiple roots of some shifted level do not authorize division there; the area formula ignores those exceptional fibers.

Equation (4) alone is an interface. The next two sections bound its right side from data other than the unknown level-track variation.

## 2. Uniform variation on an auxiliary polynomial chart

An auxiliary chart consists of a real interval J of length l>0, a disk |z−c|<R, and a complex-time neighborhood of J. Assume f is holomorphic there and

\[
|f(\tau,z)|>r_0 \quad (|z-c|=R)
\tag{5}
\]

throughout that neighborhood. For |w|≤r₀, with a strict margin in (5), the number n of roots of f(τ,z)−w in the disk is fixed, counted with multiplicity. There is no separation assumption on these roots. Degree zero charts can be omitted.

Normalize t=t_J+lu, z=c+Rζ, u∈[0,1]. The monic polynomial of the n enclosed roots is

\[
P(u,w;\zeta)=\zeta^n+\sum_{j=1}^n b_j(u,w)\zeta^{n-j}.
\tag{6}
\]

Its coefficients are holomorphic in (u,w). For example the power sums are contour integrals of (z−c)^k f_z/(f−w), and Newton identities recover the coefficients. This is a local fixed population: no varying degree is inserted into a propagator. The n roots all lie in |ζ|<1, hence |b_j|≤binom(n,j).

**Imported input.** Parusiński–Rainer, *Optimal Sobolev regularity of roots of polynomials*, Theorem 1, proves that continuous roots of a monic degree-n polynomial with C^{n−1,1} coefficients on [0,1] satisfy

\[
\|\lambda'\|_{L^p(0,1)}
 \le C(n,p)\max_{1\le j\le n}\|b_j\|_{C^{n-1,1}}^{1/j},
\qquad 1\le p<n/(n-1).
\tag{7}
\]

The constant depends only on n,p. We checked the published statement, including its interval-length factor, at the [authors' primary source][pr], Theorem 1, formula (1.2). The unit interval removes that factor. Degree one is elementary; use C(1,p)=1 with the norm below. This is an imported theorem, not a new regularity claim.

Use the norm given by the sum of derivative suprema through n−1 and the Lipschitz seminorm of derivative n−1. Enlarging the universal constant accommodates an equivalent convention. If the normalized complex-time collar contains every closed disk of radius σ centered on [0,1], Cauchy's estimate gives

\[
\|b_j(\cdot,w)\|_{C^{n-1,1}}
 \le {n\choose j} A_n(\sigma),
\qquad A_n(\sigma)=\sum_{k=0}^n k!\sigma^{-k}.
\tag{8}
\]

Put K_n(σ)=max_j[binom(n,j)A_n(σ)]^{1/j}. Continuous enumeration over a real interval is available even through multiple roots. Applying (7) to all n roots proves

\[
\sum_{j=1}^n\int_J|z'_j(t,w)|dt
 \le nR C(n,p)K_n(\sigma).
\tag{9}
\]

There is **no l factor in this L¹ path-length bound**. By contrast, its physical-time Lᵖ version pays l^{1/p−1}. This distinction is essential when using many short charts.

For a finite chart cover of the low-value portion of I×S, choose one p>1 admissible for every chart and set

\[
L_{\rm geo}=\sum_\nu
 G_\nu n_\nu R_\nu C(n_\nu,p)K_{n_\nu}(\sigma_\nu),
\quad
G_\nu=\sup_{|z-c_\nu|<R_\nu}|\nabla\psi(z)|.
\tag{10}
\]

All overlaps are paid by this sum. Equations (3), (9) imply V_abs(w)≤L_geo for almost every |w|≤r₀, so

\[
\boxed{W(r)\le\pi L_{\rm geo}r^2\quad(0<r\le r_0).}
\tag{11}
\]

For a fixed analytic field with no identically zero spatial slice, such a finite chart cover exists: isolate the finitely many spatial zeros at each time by disks, continue their boundary clearance to a short complex-time neighborhood, and cover the compact zero set over S by finitely many chart interiors. The uncovered compact remainder has positive |f| minimum; reduce r₀ below it and all chart clearances. This argument proves existence, not a source-effective value of L_geo. Section 3 supplies an independent acquisition of every chart parameter from a nonzero anchor.

The circles in (5) are **auxiliary local isolating circles**, allowed to change from one short time interval to the next. They are not the boundary of the window's core or buffer. Zeros may cross the physical working region. Nevertheless the local circle margins are genuine lower information and must be obtained or paid for; they are not a consequence of upper jets alone.

## 3. A quantitative anchor supplies the circles and the bound

Translate the anchor to z=0. Fix radii

\[
S\subset\{|z|<r_1\},\qquad 0<r_1<r_2<R_1<R.
\]

Suppose independently acquired data m,M,T,d satisfy 0<m≤M, d>0,

\[
|f(t,0)|\ge m\ (t\in I),\qquad
|f(\tau,z)|\le M,\quad |f_t(\tau,z)|\le T
\tag{12}
\]

on the complex-time tube dist(τ,I)≤d and |z|≤R, with holomorphy on a neighborhood. The anchor is uniform in real time; a single spacetime value is insufficient for (12).

Define the following quantities entirely from this data:

\[
N=\max\left(1,\left\lceil\frac{\log(M/m)}{\log(R/R_1)}\right\rceil\right),
\quad \delta=\frac{r_2-r_1}{4N},\quad
\kappa=\frac{R_1+r_2}{R_1-r_2},
\]
\[
\eta=M(m/M)^\kappa
       \left(\frac{\delta}{R_1+r_2}\right)^N,
\quad r_0=\eta/4,\quad
\ell=\min(d/4,\eta/(8T)),\quad P=\lceil\epsilon/\ell\rceil.
\tag{13}
\]

Interpret η/(8T)=∞ when T=0. We assume ε>0.

**Circle lemma.** At every fixed real t there is s∈[r₁,r₂] such that |f(t,z)|≥η on |z|=s.

*Proof.* Jensen's formula bounds the number of zeros a in the open R₁ disk, with multiplicity, by N. Remove them with the disk Blaschke product

\[
\mathcal B(z)=\prod_a\frac{R_1(z-a)}{R_1^2-\overline a z},
\qquad h(z)=f(t,z)/\mathcal B(z).
\]

The function h has no zeros inside that disk, |h|≤M by the maximum principle, and |h(0)|≥m. Harnack applied to the nonnegative harmonic function log(M/|h|) yields |h(z)|≥M(m/M)^κ on |z|≤r₂. Zeros exactly on |z|=R₁ remain boundary zeros and do not affect this interior argument. Excluding radial intervals of radius δ about at most N zero moduli removes at most half of [r₁,r₂]. Choose an s outside them. On |z|=s each factor has modulus at least δ/(R₁+r₂); multiplying and using the bound N proves the assertion. This proves the existence and size of a permissible circle without knowing its zero labels. Finding a particular circle in a numerical implementation is a separate bounded acquisition, not carried out here.

Partition I into P intervals of positive lengths at most ℓ. For each midpoint select the circle from the lemma. On the complex-time neighborhood dist(τ,J)≤ℓ/2, the distance to that midpoint is at most ℓ, so (12) gives a field change at most Tℓ≤η/8. Consequently |f(τ,z)−w|≥5η/8 on its circle for |w|≤η/4. The root count is fixed and at most N by continuation from the unshifted midpoint. Every circle encloses S, so no low-value portion of the weighted support is missed.

After rescaling any such interval to [0,1], its complex-time collar is at least 1/2. Use the smaller Cauchy radius σ=1/4. Set

\[
p_N=1+\frac1{2N},\qquad
D_N=\max_{1\le n\le N}
 n C(n,p_N)K_n(1/4),
\quad G=\|\nabla\psi\|_\infty.
\]

The exponent p_N is strictly below n/(n−1) for every n≥2 here. The degree-one convention after (7) covers n=1. Equations (10)–(11) now prove the **anchored small-value estimate**

\[
\boxed{L_{\rm anc}=PGr_2D_N,
\qquad W(r)\le\pi L_{\rm anc}r^2\quad(0<r\le\eta/4).}
\tag{14}
\]

This is an acquired analytical bound in the data (12), not another name for a crossing count. It uses no H_z floor and no fixed zero-free physical wall. It does use an actual nonzero anchor, spatial analyticity on a larger disk, and complex-time control. The constants C(n,p_N) are finite universal constants from (7), not tabulated numbers or interval-certified constants in this note.

## 4. The current actually converges; collision mass does not remain hidden

Retain the finite multiple-time hypothesis for the zeros f=0 on a neighborhood of the weighted support. From the charts and (7), the integrands v_abs(t,w) and v_+(t,w) in (3) are uniformly bounded in physical-time Lᵖ for some p>1, for almost every small w. The bound is a finite sum of terms

\[
G_\nu n_\nu R_\nu |J_\nu|^{1/p-1}
C(n_\nu,p)K_{n_\nu}(\sigma_\nu).
\tag{15}
\]

Thus on every measurable time set E their integrals are bounded by a constant times |E|^{1−1/p}, uniformly in w. The shifted families f=w need not have finitely many multiple events; the root theorem already covers their coefficients.

At every regular time for f=0, the implicit function theorem gives convergence of roots and velocities as w→0. Compactness excludes additional small-value roots away from the finitely many zero neighborhoods. Roots crossing the boundary of S cause no discontinuity in the weighted expression, since ∇ψ extends continuously by zero. Therefore v_abs(t,w)→v_abs(t,0) and v_+(t,w)→v_+(t,0) for almost every t. Uniform integrability from (15), or excision of small neighborhoods of the finite event times, proves the essential limits

\[
V_{\rm abs}(w)\longrightarrow V_{\rm abs}(0),
\qquad V_+(w)\longrightarrow F^+_{\psi,\rm all}.
\tag{16}
\]

The statement is an essential limit in the target plane, which is sufficient for (4). No assertion about exceptional critical levels is necessary. The total weighted product mass W(∞) is finite by compactness. For the portion |w|≥r₀,

\[
\int_{|w|\ge r_0}k_\rho(w)V_+(w)dA_w
\le\frac{\rho^2 W(\infty)}{\pi(r_0^2+\rho^2)^2}\to0.
\]

Using (16) on the small target disk in (4) proves

\[
\boxed{\lim_{\rho\downarrow0}Q_\rho=F^+_{\psi,\rm all},
\qquad
\lim_{r\downarrow0}\frac{W(r)}{\pi r^2}=V_{\rm abs}(0).}
\tag{17}
\]

This strengthens Note 07's safe Fatou inequality at its fixed-field finite analytic scope. It supplies no uniform rate as a field, height, chart degree or chart margin degenerates. A fixed-ρ calculation still needs an independently acquired bias allowance; the ρ^{−2} and ρ^{−3} approximation costs of Note 07 remain in force.

Combining (14), Note 07's integration-by-parts bound, and its nonreal consumer gives

\[
Q_\rho\le L_{\rm anc}\frac{r_0^2}{r_0^2+\rho^2}
 +\frac{\rho^2W(\infty)}{\pi(r_0^2+\rho^2)^2},
\quad F^+_{\psi,\rm nr}\le L_{\rm anc},
\]
\[
\boxed{M_K^{\rm real}\le\tfrac32\{N_{\psi,\rm nr}(-\epsilon)+L_{\rm anc}\}.}
\tag{18}
\]

No RH assumption is needed for real endpoint sites. The earlier nonreal population is still a separate resource; (18) does not acquire OBF-04.

## 5. Complete theta inputs really meet the anchor contract

Take B=1 and the unchanged positive source Φ and normalization of Note 07 (17): H(t,z)=∫₀∞e^{tu²}Φ(u)cos(zu)du. Its super-exponential tail makes the following complete integrals finite for every fixed ε,d,R:

\[
m=\int_0^\infty e^{-\epsilon u^2}\Phi(u)du>0,
\quad M=\int_0^\infty e^{d u^2+Ru}\Phi(u)du,
\quad T=\int_0^\infty u^2 e^{d u^2+Ru}\Phi(u)du.
\tag{19}
\]

They supply (12): for real t∈I, H(t,0)≥m; in the complex-time tube Re τ≤d and |Im z|≤R, the absolute cosine bound gives M and differentiation gives T. Even an elementary explicit anchor lower bound is available by keeping the n=1 source term on 0≤u≤1/10:

\[
m\ge\frac{\pi(2\pi-3)}{10}
\exp\{-\epsilon/100-\pi e^{2/5}\}>0.
\tag{20}
\]

For (20), the prefactor of that term is πe^{5u}(2πe^{4u}−3)≥π(2π−3); every omitted summand is positive. Source and integration tails must still be paid in any numerical upper evaluation of M,T. No finite source fit is used in the theorem.

For any fixed finite buffer, choose r₁ large enough to enclose it about zero, then r₂,R₁,R and d. Equations (13), (14), and (19) now give a **coarse finite negative-time theta bound for the smooth inflow functional** from complete-source information. It is not a bound on sharp-wall gross entry. Its universal root constants remain unevaluated.

This improves the former state of the argument: a finite (SV) constant and regulator removal are no longer merely assumed. But the anchor at zero is far from a high-height buffer. Increasing the containing disk can make M/m, N, η^{−1}, P and D_N enormous. No estimate here makes L_anc sublinear in a target zero count, small on a chosen height band, or favorable when ε is enlarged.

The same theorem applies to f=H/B if its own anchor and complex-tube bounds are obtained. A convenient high-height carrier need not be holomorphic and nonvanishing on the large disk back to zero; one cannot silently transplant (19) to such a carrier. A local normalized anchor or a sharper directional inequality would be additional information. The [corrected reference][reference] retains its stated positive-time error regime and does not provide that information at negative time.

For future local acquisitions, one can derive an actual complex-time error instead of continuing a real-time bound. For a real center t*, |τ−t*|≤d*, and |Im z|≤b, the heat Taylor polynomial through K has spatial derivative remainder

\[
e_j\le\frac{(d_*)^{K+1}}{(K+1)!}
\int_0^\infty u^{j+2K+2}
 e^{(t_*+d_*)u^2+bu}\Phi(u)du.
\tag{21}
\]

This follows directly from the complex exponential remainder under the complete integral. Normalizing by B also pays its lower bound and derivative terms. Equation (21) gives a valid acquisition budget, with no claim of high-height efficiency or an already acquired local circle margin.

## 6. Collision checks and the near-real strip

For H=z²−2t, the roots of H=w are ±√(2t+w). Their summed speed is 2/|2t+w|^{1/2}. Since |2t+w|≥|2t+Re w|,

\[
\int_{-\epsilon}^0\frac{2\,dt}{|2t+w|^{1/2}}
\le\int_{\operatorname{Re}w-2\epsilon}^{\operatorname{Re}w}|u|^{-1/2}du
\le4\sqrt\epsilon.
\tag{22}
\]

The last maximum occurs for an interval centered on zero. Hence W(r)≤4πG√ε r² for this control, with no H_z floor, even though the pair collides and enters the unit disk at t=−1/2. At w=0 the exact total root length is 2√(2ε). The cubic z³−6tz likewise lies within the polynomial theorem and still saturates the inherited factor 3/2. Neither control is excluded by the new estimate; its constant is not assumed subunit.

A useful local refinement applies to the conjugation-symmetric window already used in Note 07. At a real heat event, incoming nonreal branches can be parametrized by q=√(t_e−t). Uniqueness of each simple rescaled branch and real type give z_j(−q)=overline{z_j(q)}, so x(q) is even analytic and y(q) odd analytic. Consequently x'=O(1), y=O(q), y'=O(q^{−1}), where primes here denote t derivatives, while ψ_y(x,y)=O(y). Thus dψ/dt remains bounded near the event. If on each branch |y|≥c_e√(t_e−t) and |dψ/dt|≤A_e, then its contribution omitted by a cutoff supported in |y|≤2δ is at most 4A_eδ²/c_e². Summing finitely many incoming branches yields

\[
R_\delta\le4\delta^2\sum_e A_e/c_e^2
\tag{23}
\]

once δ is below the clearance of all other nonreal tracks. This sharpens Note 07's O(δ) local bound to O(δ²) for the symmetric window. Its constants remain field-dependent. It does not permit the strip to be discarded at a fixed δ, and the safe order remains first ρ→0, then δ→0. Keeping the complete current avoids omitting the strip altogether.

## 7. Scope, controls and the next inequality

The quantitative premise added to upper jets is the uniform nonzero anchor (12), together with larger-disk and complex-time analyticity bounds. The scaling controls in Note 07 fail a fixed positive anchor as their amplitude tends to zero. Under a pure scaling f↦cf, the data m,M,T and η scale by |c|; L_anc stays unchanged while r₀ shrinks by |c|. It is therefore the regulator threshold that degenerates in this homogeneous example. Other varying families can also deteriorate the geometric allowance. There is no contradiction with the scoped upper-jet obstruction.

The full [registered controls][controls] have the following disposition:

| Family | Relation to this theorem and the intended arithmetic application |
| --- | --- |
| Euler-factor controls | On finite analytic domains with positive source anchor they also satisfy the generic estimate. They fail the unchanged theta source/completion premise, not the anchored theorem. No theta-sized flux separation is asserted. |
| Weighted-square and finite-prime controls | They may share the finite anchor/moment inputs while failing full normalized reflection or unchanged arithmetic coefficients. No common negative all-real interval is assumed. |
| Reflected, smooth-shape and positive-primitive controls | Their finite analytic heat fields are not excluded by the generic theorem. They fail unchanged integer-square theta arithmetic. |
| Close normalized endpoint controls | Broad positivity, normalization and closeness do not distinguish them; their ordinary Dirichlet-series arithmetic fails. The bound does not exclude their endpoint collisions. |
| Polynomial/drifting controls | They check collision integrability, scaling and recrossings. They are not the unchanged theta source. |

Finiteness of (SV) is therefore a generic local analytic fact with an anchored quantitative version; **smallness useful for the chosen consumer is the missing arithmetic problem**. A sufficient next target on prescribed normalized bands is to acquire charts or another directional bound with

\[
\sum_\nu G_\nu n_\nu R_\nu C(n_\nu,p)K_{n_\nu}(\sigma_\nu)
\le L_h^{\rm useful},
\tag{24}
\]

where the required size of L_h^{useful} is set in advance by the endpoint/aggregate consumer. Equation (24) is **not proved here** and is not claimed necessary: the chart sum can overpay degree, real motion and overlaps. Merely naming L_h^{useful} does not advance the arithmetic. The anchored bound (14), in contrast, is already derived from declared source data, although too coarse to show the required size.

**Register disposition.** OBF-01 is unchanged. OBF-02 now has a proved fixed-field regulator limit and anchored quantitative (SV), in addition to Note 07's finite source-error theorem; useful normalized parameter dependence remains open. OBF-03 gains a coarse finite complete-theta-source allowance via (19), with no useful band or growing-height size demonstrated. OBF-04 and OBF-05 remain open; OBF-06 is untouched. Larger ε still cannot lower the exact conservative resource of a fixed region. No numerical campaign, manuscript snapshot, or new global conclusion was required for this continuation.

[previous]: 07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md
[continuation]: 05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[review]: ../reviews/03_ANCHORED_SMALL_VALUES_AND_CURRENT_LIMIT_REVIEW_20261023.md
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[pr]: https://math.univ-cotedazur.fr/~parus/publis/ens.pdf
