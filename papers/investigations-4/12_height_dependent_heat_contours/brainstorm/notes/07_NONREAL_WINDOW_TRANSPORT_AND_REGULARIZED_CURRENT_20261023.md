# Finite nonreal window transport and the missing small-value estimate

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **xhigh**. Same-assistant derivation and self-review; no independent specialist review or priority claim.

**Status: proved in-note finite transport, a smooth-window multiplicity consumer, and a regularized complete-field error theorem; scoped obstruction for upper-jet-only information. No useful negative-time theta inflow estimate, larger justified backward width, or new simplicity conclusion is acquired.**

This executes the opening task in [Continuation 05][continuation]: OBF-01 and the representation/error part of OBF-02. The [result index][results] and [avoid index][avoid], especially [classification][a01], [control premises][a02], [numerics before structure][a10], [coupled estimates][a12] and [scoped conclusions][a07], govern the claims. The inherited [finite hard-wall derivation][previous], [earlier-time consumer][earlier], [total-divisor regularization][regularization], [coefficient theorem][coefficient], [physical contours][contours] and [current HDC snapshot][snapshot] are distinct inputs. The [self-review][review] records the proof checks and remaining limitations.

## 1. Finite convention and the hard-wall audit

Put I=[a,0], a<0. Work with H(t,z) jointly holomorphic on a complex neighborhood of I times a spatial neighborhood of the compact sets used below, real type for real t, and H_t=-H_zz. No spatial slice is identically zero. Joint analyticity is an explicit sufficient hypothesis; no assertion about arbitrary nonanalytic heat solutions is needed. The canonical theta integral satisfies it on every compact set.

For the hard-wall statement let Ω be a bounded conjugation-invariant domain with piecewise C² boundary. Include **every** zero in Ω at each slice with its spatial multiplicity. Assume finitely many multiple events near the track, finitely many spatial crossings, no zeros on the spatial wall at a or 0, and that all wall events are simple, transverse crossings away from corners. Interior endpoint multiple zeros are allowed. At a crossing, n is the outward unit normal, v=H_zz/H_z, and entry means n·v<0. A real simple root remains real locally, so cannot silently convert between the real and nonreal counts at a wall crossing.

The local heat law used here follows by parabolic expansion at an order-m zero (t_e,z_e). For s=t-t_e and w=z-z_e its leading polynomial is a nonzero multiple of

\[
 p_m(s,w)=\sum_{k=0}^{\lfloor m/2\rfloor}
       \frac{m!(-s)^k w^{m-2k}}{k!(m-2k)!}.
 \tag{1}
\]

For s>0 its m rescaled roots are distinct and real; for s<0 they are purely imaginary, with a single zero root when m is odd. The simple rescaled roots persist under the higher parabolic terms. Thus local branches are analytic in a one-sided square-root time parameter, their speeds are O(|s|^(-1/2)), and an off-real event stays off the real axis locally. At a real event, exactly w_m=2 floor(m/2) nonreal labels disappear forward in time. A possible central branch for odd m is real, by real type and uniqueness. This also supplies the local integrability used below.

Let N_nr(t) count the complete nonreal divisor in Ω. Count every crossing occurrence, including recrossings, in J_in^nr and J_out^nr; a conjugate pair contributes two. Set

\[
 B_\Omega=\sum_{\substack{a<t_e\le0,\ x_e\in\Omega\cap\mathbb R}}
                    2\lfloor m_e/2\rfloor.
\]

Splitting at crossings and events gives

\[
 N_{\rm nr}(0)=N_{\rm nr}(a)+J_{\rm in}^{\rm nr}
                         -J_{\rm out}^{\rm nr}-B_\Omega. \tag{2}
\]

At an off-real event, multiplicity is conserved. At a real event, the value **at** the event already has all its real multiplicity, so the event at 0 is included and an event at a is excluded. No unique labeling through a collision is required. Spatial endpoint zeros were excluded to avoid an additional corner convention.

Let M_core^real be the sum of multiplicities at real nonsimple endpoint sites in a core contained in Ω. Since m≤(3/2)w_m and m-1≤w_m for m≥2,

\[
 M_{\rm core}^{\rm real}\le\frac32 B_\Omega
 \le\frac32(N_{\rm nr}(a)+J_{\rm in}^{\rm nr}),\qquad
 D_{\rm core}^{\rm real}\le N_{\rm nr}(a)+J_{\rm in}^{\rm nr}. \tag{3}
\]

There is no RH assumption in (2)–(3). RH is used only to identify these real sites with all canonical endpoint sites in the core. A bound on J alone leaves N_nr(a) unpaid.

**Multiple wall events require a correction.** An isolated order-m wall event is outside the transverse theorem. Isolate its local cluster by a small disk and a time block, with a zero-free disk boundary and no other event, and assume its one-sided populations relative to Ω stabilize. Let Δ_e be the number of nonreal labels of this cluster inside Ω just after minus just before the block's central event. Add ΣΔ_e to (2), excluding these wall events from B_Ω and the ordinary crossing sum. The consumer adds C_∂=Σ[Δ_e]_+, with [Δ_e]_+≤m_e. Entries/exits outside these blocks are counted ordinarily. The coarser allowance Σm_e is available if only the complete local multiplicities are known. No universal half-event or ordinary crossing weight is assigned. The stabilization/excision data are extra hypotheses; without them the extended wall statement is not being asserted.

**Exact controls.** On Ω={|z|<1}, a=-1:

| Field | Nonreal branches for t<0 | Entry time | Radial speed at entry | N_nr(a), J_in^nr, B_Ω, M_0^real |
| --- | --- | --- | --- | --- |
| z²-2t | ±i sqrt(-2t) | -1/2 | -1 | 0, 2, 2, 2 |
| z³-6tz | ±i sqrt(-6t), with a real root 0 | -1/6 | -3 | 0, 2, 2, 3 |

The branches have H_z≠0 at entry and negative outward radial velocity. Both events at 0 must be counted. The cubic attains 3/2. The drifting sine in Note 04 can have equal entry and exit with unchanged total count; its signed total count is not a gross-entry estimate.

## 2. The smooth-window theorem, including the nonreal event term

Choose a bounded conjugation-invariant open D, a compact endpoint core K, and ψ∈C_c²(D), with 0≤ψ≤1, ψ=1 near K, and ψ(\bar z)=ψ(z). The support of ∇ψ is the buffer. Its width and derivatives are part of the data: a chosen cutoff profile across distance d pays its actual O(d^(-1)) gradient and O(d^(-2)) Hessian constants. A finite cover of transition charts must retain its multiplicity. No moving time graph or changing degree is used.

Assume the multiple events in a neighborhood of I×supp ψ are finite. Every slice has finitely many zeros on this compact set, uniformly locally in t: isolate the zeros at each time by small disks and apply the argument principle to their zero-free disk boundaries for a short time. Compactness in time gives a finite cover. These auxiliary disks track local clusters only; no zero-free **working spatial wall** across I is assumed. Sum over every zero of H in D, with weight zero outside supp ψ:

\[
 N_{\psi,\rm nr}(t)=\sum_{\Im z_j(t)\ne0}\psi(z_j(t)),\quad
 B_\psi=\sum_{\substack{a<t_e\le0,\ x_e\in\mathbb R}}
                         w_{m_e}\psi(x_e).
\]

The repeated-label notation includes multiplicity. On regular time segments put

\[
 \dot\psi_j=\nabla\psi(z_j)\cdot v_j,\qquad
 F_{\psi,\rm nr}^{\pm}=\int_a^0
       \sum_{\Im z_j(t)\ne0}[\pm\dot\psi_j]_+\,dt. \tag{4}
\]

These integrals are finite. Away from events this is ordinary smooth motion; near each event (1) gives |v_j|≤C|t-t_e|^(-1/2), which is integrable. Entries into or exits from the compact support create no jump, because ψ vanishes there. Off-real collisions preserve the weighted sum continuously. A real event has jump -w_m ψ(x_e). Integrating on regular pieces and taking their endpoint limits proves

\[
 \boxed{N_{\psi,\rm nr}(0)-N_{\psi,\rm nr}(a)
       =F_{\psi,\rm nr}^{+}-F_{\psi,\rm nr}^{-}-B_\psi.} \tag{5}
\]

This is a proof for the **nonreal** divisor. It is not obtained by applying the total-divisor logarithmic identity. As before, the event convention is (a,0]. For real nonsimple endpoint sites in K,

\[
 \boxed{M_K^{\rm real}\le\frac32
       \{N_{\psi,\rm nr}(a)+F_{\psi,\rm nr}^{+}\}.} \tag{6}
\]

The analogous excess bound has factor one. The nonnegative discarded terms in (5) are N_ψ,nr(0) and F^-; the other real events only increase B_ψ. Thus the core endpoint consumer is valid without endpoint reality. RH supplies that additional interpretation for theta. This is the chosen smooth analogue of inflow; it need not equal a sharp Ω crossing count. It is sufficient for the same core consumer, and counts repeated inward motion in the buffer.

## 3. Comparing the wall and volume currents

For a positively oriented arc-length wall parameter γ(s), let F(t,s)=H(t,γ(s)) and T=γ'(s). The Jacobian with columns (t,s) is

\[
 \mathcal J=\Im(\overline{F_t}F_s)
 =\Im(-\overline{H_{zz}}H_zT)
 =|H_z|^2(-n\cdot v). \tag{7}
\]

Hence its positive part has the entry orientation. At finitely many simple transverse wall zeros away from the real axis, integration of an approximate delta of F times [J]_+ tends to the number of such entries, by the local inverse function theorem. A nonreal cutoff first restricts away from the real axis; its later removal is necessary. This exact wall representation is an interface. It does not bound the near-real contribution or provide a uniform finite-cutoff error, and transversality constants can degenerate. We therefore develop the **smooth volume current** below, allowing the conservative inclusion of real trajectories. We do not develop a second hard-wall estimation program.

For field regularization ρ>0, define

\[
 k_\rho(w)=\frac{\rho^2}{\pi(|w|^2+\rho^2)^2},\quad
 \mu_\rho=k_\rho(H)|H_z|^2,\quad
 j_\rho=k_\rho(H)H_{zz}\overline{H_z}. \tag{8}
\]

Identify complex j with its planar vector. The exact smooth continuity equation is

\[
 \partial_t\mu_\rho+\operatorname{div}_z j_\rho=0. \tag{9}
\]

One proof pulls back the closed target-plane two-form k_ρ(w) dRe w∧dIm w by (t,x,y)↦H. Its spatial coefficient is μ_ρ; its time-spatial coefficients give j_ρ with velocity -H_t/H_z=H_zz/H_z wherever H_z≠0. The polynomial expressions (8) then extend the identity through critical points. Equivalently differentiate (8) using H_y=iH_z and H_t=-H_zz. No division by H_z remains. Also μ_ρ=(2π)^(-1)Δ[½log(|H|²+ρ²)], agreeing with LHCT Note 08.

Writing Dψ=ψ_x-iψ_y, define the explicit nonnegative functional

\[
 Q_{\psi,\rho}(H)=\int_I\int_D
    k_\rho(H)[\Re\{D\psi\,H_{zz}\overline{H_z}\}]_+\,dA\,dt.
 \tag{10}
\]

At any regular time, the spatial measures in (10) converge weakly to the sum over simple roots of [dot ψ_j]_+. To check the normalization near a root, substitute w=H(z); dA_w=|H_z|²dA_z, and the remaining numerator divided by |H_z|² is precisely dot ψ_j. The target kernel has total integral one. Away from the finitely many roots, it tends uniformly to zero on the compact buffer. Therefore Fatou's lemma in time gives the safe one-sided estimate

\[
 \boxed{F_{\psi,\rm nr}^{+}\le F_{\psi,\rm all}^{+}
               \le\liminf_{\rho\downarrow0}Q_{\psi,\rho}(H).} \tag{11}
\]

The middle quantity includes real roots. This avoids needing to prove convergence of total positive currents through critical times; Fatou is sufficient and does not assert that no excess concentration survives. Integrability of the root quantity was proved in Section 2. Equations (6) and (11), rather than signed variation of the total count, are the finite consumer.

### The near-real strip and the order of limits

Let 0≤χ_δ(y)≤1 vanish for |y|≤δ, equal one for |y|≥2δ, and increase pointwise to 1_{y≠0} as δ decreases. For each fixed δ, insert χ_δ in both (4) and (10); the same argument bounds F^+_δ by liminf_ρ Q_δ,ρ. Then take δ↓0 using monotone convergence on the root integrals. Do **not** identify δ with ρ. Keeping (10) without χ_δ is a conservative upper bound for every δ and hence for the complete nonreal flux; it has no omitted-strip cost.

If instead a finite δ strip is omitted for sharpness, its missing positive variation is an extra R_δ. Locally, for each incoming nonreal branch at a real event, one can acquire constants c_e,C_e>0 with

\[
 |\Im z_j(t)|\ge c_e\sqrt{t_e-t},\qquad
 |z'_j(t)|\le C_e/\sqrt{t_e-t}.
\]

Once δ is below the clearance of other nonreal branches on the remaining compact tracks, integration gives

\[
 R_\delta\le4\|\nabla\psi\|_\infty\,\delta
                  \sum_{e,\,\text{incoming branches}}C_e/c_e. \tag{12}
\]

This is a fixed-field local estimate; its constants and clearance are **not** uniform theta source inputs. The initial N_ψ,nr(a) likewise requires its own near-real coverage. The quadratic pair with |t|≤O(δ²) shows why taking δ first can discard the entire endpoint witness. No finite δ is assigned zero cost.

## 4. A complete-field approximation theorem with explicit error

For a reference G, no heat equation for G is required in this subsection. Define Q(G) by the spatial-jet expression (10), without interpreting it as G's actual time current. Let e_0≥|H-G| and let η_12≥|H_zz overline(H_z)-G_zz overline(G_z)| on the complete buffer-time region. The elementary bounds

\[
 \|k_\rho\|_\infty=1/(\pi\rho^2),\qquad
 \|\nabla_w k_\rho\|_\infty=C_k/(\pi\rho^3),\qquad
 C_k=125/(54\sqrt5)
 \tag{13}
\]

follow by maximizing 4ρ²r/(r²+ρ²)³ at r=ρ/√5. Since positive part is 1-Lipschitz, subtraction **before** estimates gives

\[
 \boxed{|Q_{\psi,\rho}(H)-Q_{\psi,\rho}(G)|\le E_\rho,}
\]
\[
 E_\rho=\int_I\int_D |\nabla\psi|
 \left\{\frac{\eta_{12}}{\pi\rho^2}
 +\frac{C_k e_0|G_{zz}\overline{G_z}|}{\pi\rho^3}\right\}\,dA\,dt.
 \tag{14}
\]

A fallback from individual errors is η_12≤e_2|H_z|+e_1|G_zz|, where e_j≥|∂_z^j(H-G)|. Directly enclosing the coupled product difference can be better. A uniform version pays |a|‖∇ψ‖_1 times the suprema in braces. If only an absolute field error e_out on an actual spatial collar of width d is available, Cauchy's estimates give e_j≤j! e_out/d^j, j=1,2, provided H-G is holomorphic on each closed collar disk. A bound on a single contour, or on a nonanalytic correction, does not provide this hypothesis.

If one evaluates G's true current using -G_t rather than G_zz, add

\[
 \int_I\int_D\frac{|\nabla\psi|\,|G_t+G_{zz}|\,|G_z|}{\pi\rho^2}\,dA\,dt.
 \tag{15}
\]

The reference heat defect is paid explicitly. There is **no |H| or |H_z| floor** in (13)–(15), but the errors grow as ρ^(-2) and ρ^(-3). A fixed source error does not pass to ρ=0. Uniformly bounded reference jets, e_0=o(ρ³) and η_12=o(ρ²) are sufficient, not necessary, conditions for this particular error bound to vanish along a refined reference sequence.

Consequently (11)–(14) give a source-evaluation interface

\[
 F_{\psi,\rm nr}^{+}\le
       \liminf_{\rho\downarrow0}\{Q_{\psi,\rho}(G_\rho)+E_\rho\}. \tag{16}
\]

Neither the liminf nor the unknown small-field concentration may be replaced by one fixed-ρ value without an independently proved bias allowance. This limitation is substantive, not a reason to refine a mesh.

## 5. What complete theta information already pays on negative time

Use exactly the canonical source and normalization

\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                           e^{-\pi n^2e^{4u}},\quad
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \quad 8H(0,z)=\xi(1/2+iz/2).
 \tag{17}
\]

These definitions and the real-positive-time range of the imported approximation results were checked against [Polymath's primary source][poly]. Each summand of Φ is positive for u≥0. For a declared band with |Im z|≤b, put

\[
 A_j(b)=\int_0^\infty u^j e^{bu}\Phi(u)\,du<\infty.
\]

For -ε≤t≤0, the complete source immediately gives |∂_z^j H|≤A_j(b). More concretely let

\[
 G_K(t,z)=\sum_{k=0}^K\frac{(-t)^k}{k!}H_0^{(2k)}(z).
\]

Taylor's integral remainder for exp(tu²), with t≤0, has absolute value at most (εu²)^(K+1)/(K+1)!. Thus

\[
 \boxed{e_j\le\frac{\epsilon^{K+1}}{(K+1)!}A_{j+2K+2}(b),\quad
                   j=0,1,2,} \tag{18}
\]
\[
 (G_K)_t+(G_K)_{zz}=\frac{(-t)^K}{K!}H_0^{(2K+2)}(z),\quad
 |(G_K)_t+(G_K)_{zz}|\le\frac{\epsilon^K}{K!}A_{2K+2}(b).
 \tag{19}
\]

The complex sine and cosine derivative factors obey |sin(zu)|,|cos(zu)|≤e^{bu}. Positivity and super-exponential decay justify differentiation and the complete tails. Any actual evaluation of A_j or H_0 derivatives must pay both the u-integration tail and the source-index tail; no finite fit is substituted. Equations (18)–(19) are a genuine negative-real-time absolute error budget, derived directly rather than analytically continuing an error bound. Their scale can be extremely poor at high real height: they do not capture the field's oscillatory cancellation or exponential amplitude decay. There is no favorable high-height or larger-ε claim here.

### Normalize a known carrier before attempting a high-height estimate

A specified holomorphic nonvanishing carrier B(t,z) can remove the known amplitude decay, but its transport terms must be retained. Put f=H/B, λ=B_z/B and c_B=B_t/B+B_zz/B. Then

\[
 -f_t=\mathcal T_B f:=f_{zz}+2\lambda f_z+c_B f,\qquad
 \mu_\rho^B=k_\rho(f)|f_z|^2,\quad
 j_\rho^B=k_\rho(f)(\mathcal T_B f)\overline{f_z}. \tag{19a}
\]

The same pullback proof gives exact continuity, and at each simple zero (T_B f)/f_z is the actual root velocity. Therefore (11), the near-real argument, and the error theorem hold with f replacing H and (T_B f) overline(f_z) replacing H_zz overline(H_z). For a normalized reference g and exact known B, its product error is bounded by

\[
 \eta_B\le(e_2+2|\lambda|e_1+|c_B|e_0)|f_z|
                          +|\mathcal T_B g|e_1. \tag{19b}
\]

Use this in (14); if the reference time current is used, its defect is g_t+T_B g. This is the same smooth-current method with its carrier terms, not an assumption that H/B solves the free heat equation. A known carrier floor is computable source data, distinct from a floor for H or H_z. Absolute errors such as (18) must be divided/differentiated with B and may still be poor. Any analytic continuation of B alone does not continue the corrected reference's error.

The small-value theorem in Section 6 applies equally to W^B(r) formed with |∇ψ|1_{|f|≤r}|(T_B f) overline(f_z)|. This normalized version is the more plausible high-height source task; its useful bound is no more acquired than the unnormalized one. All carrier contributions, including c_B f at finite ρ, remain present.

The [corrected microscopic reference][reference] has a useful sharper allowance in its stated real **positive** time regime. Its holomorphic reference formula alone does not extend that allowance to t<0. The [height-boundary analysis][height] bounds signed real net flux away from t=0 at positive times. Neither supplies (16)'s limiting upper bound on this negative-time band.

## 6. The exact missing inequality and a useful conditional bound

Let the complete source define, on the declared band and buffer,

\[
 W_\theta(r)=\int_I\int_D |\nabla\psi|\,
       \mathbf1_{\{|H|\le r\}}|H_{zz}\overline{H_z}|\,dA\,dt.
 \tag{20}
\]

Its total mass is independently bounded by

\[
 W_\theta(\infty)\le |a|\|\nabla\psi\|_1 A_1(b)A_2(b).
 \tag{21}
\]

The missing source-specific estimate is a **small-value** bound, with a useful independently obtained L_h on each prescribed band:

\[
 \boxed{W_\theta(r)\le\pi L_h r^2\quad(0<r\le r_0).}
 \qquad\text{UNPROVED FOR THETA HERE.} \tag{SV}
\]

This is a sufficient aggregate hypothesis, not a claimed equivalence to RH or simplicity. It is stronger than the required directional nonreal positive current because (20) takes an absolute product and includes real trajectories. It can therefore overpay. Identifying θ in (20) does not establish (SV); without an independently derived L_h this is still a small-value interface, not an arithmetic estimate. The first point requiring new theta arithmetic is a useful upper bound in (SV), or a sharper direct bound for the directional functional in (16), beyond the upper moments (21).

**Conditional theorem.** If (SV) holds, then

\[
 Q_{\psi,\rho}(H)\le
 L_h\frac{r_0^2}{r_0^2+\rho^2}
 +\frac{\rho^2W_\theta(\infty)}{\pi(r_0^2+\rho^2)^2},\qquad
 F_{\psi,\rm nr}^{+}\le L_h. \tag{22}
\]

Indeed dominate the positive numerator by |∇ψ||H_zz H_z| and integrate k_ρ(r) against dW_θ(r). On [0,r_0], integration by parts and (SV) give at most πL_h∫_0^{r_0}2r k_ρ(r)dr=L_h r_0²/(r_0²+ρ²). Above r_0 use the decreasing kernel's value at r_0 and total mass (21). The endpoint at r=0 has zero weighted volume mass: each nonzero holomorphic slice has planar zero set of measure zero. Now apply (11). No wall floor or H_z floor has been inserted.

Combining (6) and (22) gives

\[
 M_K^{\rm real}\le\tfrac32\{N_{\psi,\rm nr}(a)+L_h\}. \tag{23}
\]

This does not acquire the earlier resource. Neither small L_h nor (18) completes OBF-04. OBF-05 would also have to pay the complete core coverage, omitted endpoint labels, overlapping buffers, recrossings, and any height-graph joins before an asymptotic conclusion.

One tempting stronger premise should be avoided: an **unweighted** space-time sublevel volume ≤C r² need not survive an ordinary double collision in the buffer. For H=z²-2t near t=0, the two simple-root disks at t<0 have sublevel area comparable to r²/|t| when r≪|t|. Integrating r≲|t|≲c gives a lower bound comparable to r² log(1/r). Replacing |H_zz H_z| by a uniform upper bound would lose the factor comparable to sqrt(|t|) that makes the weighted current integrable. Such an unweighted premise can reintroduce a collision restriction under a new name. The coupled numerator in (20) is deliberate.

## 7. Two scoped obstructions: what upper jets and fixed ρ cannot do

**A fixed field regulator can miss an entire entry.** For H_c=c(z²-2t) in the unit disk on [-1,0], with c>0, J_in^nr=2 independently of c. At a fixed ρ, the regularized hard-wall current from (7) is O(c²/ρ²) and tends to zero as c↓0. The same scaling holds for (10) on any fixed smooth buffer. Thus there is no uniformly vanishing, amplitude-free cutoff bias over this bounded upper-jet class. For any proposed bias tending to zero with ρ, choose c/ρ small enough. This is precisely the nonuniform exchange of field and regulator limits excluded in (16). Theta's normalization is fixed, so this is not an obstruction to an estimate that actually acquires its normalized small-value distribution.

**Even arbitrarily many nonreal entries fit fixed upper derivative budgets.** On I=[-1,0] and Ω=(0,1)+i(-1,1), take k=2πn, κ=k², and

\[
 H_n(t,z)=c_n e^{\kappa z-\kappa^2t}
       \{e^{k^2t}\cos(k(z-2\kappa t)-\pi)-1\},\qquad c_n>0.
 \tag{24}
\]

The bracket before drift is a heat solution and the exponential/drift transformation preserves H_t=-H_zz. For t<0 the complete roots are

\[
 z_m^\pm(t)=2\kappa t+\frac{(2m+1)\pi}{k}
                 \ \pm\frac{i}{k}\operatorname{arcosh}(e^{-k^2t}). \tag{25}
\]

In -1/k²<t<-1/(2k²), the imaginary parts are below arcosh(e)/k<1 and the real velocity is 2k². The left wall is crossed inward by exactly n conjugate pairs: (2m+1)π lies strictly between k and 2k, giving m=n,...,2n-1. Thus J_in^nr≥2n. Equal right-wall exchanges occur because the width is exactly n periods; zero net count does not bound this gross entry. At t=0 the endpoint double roots are the n half-grid points in (0,1), away from the vertical walls.

For any fixed finite list of mixed t,z derivatives on a fixed compact neighborhood, choose c_n sufficiently small that **all** their suprema are at most one (or any prescribed positive upper budgets). This scaling leaves every root and crossing unchanged. Hence no finite bound for J_in^nr can follow from such upper budgets alone on this unnormalized real-type heat class. Small corner modifications, if needed for a wall convention outside the displayed crossing interval, do not affect these entries at |Im z|<arcosh(e)/k.

This is not a positive-source or fixed-theta counterexample, and is not a claim about source data including a normalization or lower information. Its class is explicitly **finite upper field-jet information without a nonzero anchor or normalized low-value control**. In particular (21) by itself cannot be read as (SV); a naive k_ρ≤1/(πρ²) bound diverges, and these controls show why a scale-independent conclusion from upper jets alone is unavailable.

## 8. Registered controls, disposition and the next analytic task

The full [collision register][controls] screens the premises as follows. Every generic theorem above applies to any listed control satisfying its finite analyticity/event hypotheses; none is excluded by (2), (5), (9), or (14).

| Control class | Premise it fails when the unchanged theta source (17) is required | What this note does not infer |
| --- | --- | --- |
| Euler-factor modifications | Unchanged canonical coefficients/source and completion data | No bound on their negative-time inflow from shared positivity |
| Weighted-square and finite-prime substitutes | Recorded full normalized reflection or unchanged complete arithmetic data | No common negative all-real interval or global all-real heat time |
| Reflected super-Gaussian, shape and positive-primitive controls | Unchanged integer-square theta source | No collision exclusion from reflection/shape/primitive positivity |
| Close normalized endpoint controls | Ordinary Dirichlet-series arithmetic of the original zeta source | Fixed source closeness alone does not prove (SV) |
| Polynomial and drifting controls above | Complete source (17), and for the scaling screen also fixed normalization | They audit the finite theorem and information class only |

No control is claimed to violate (SV) with a particular theta-sized L_h: no such estimate has been acquired for either the control or theta. The comparison names the source-identification failures rather than inventing a quantitative rejection.

**OBF-01:** finite hard-wall audit and smooth nonreal extension proved under the declared analytic, finite-event and endpoint conventions; multiple wall events have a stated conditional excision payment. Same-assistant review only.

**OBF-02:** the smooth current route is selected; (11), (14), (18) and (22) give the representation, finite source-error budget, actual negative-time absolute approximation, and a conditional aggregate bound. The useful regulator removal/small-value estimate remains open. This task is **partial**, not complete.

**OBF-03–05:** no useful theta allowance, earlier nonreal bound, width improvement, or all-height assembly has been obtained. On a fixed region, Note 04's monotonicity of the exact conservative resource still applies; the present smooth theorem gives no contrary larger-ε benefit.

The next analytic task is to derive or delimit the carrier-normalized version of (SV) for the unchanged theta field in one prescribed band and buffer, retaining the coupled source jets and their amplitude scale. A possible improvement is to estimate the directional positive functional directly so that real motion and opposite directions are not overpaid. It must come with an actual source inequality; another representation of (20), an assumed nonclustering condition, or a finite regulator scan would not complete it. Independent control of N_ψ,nr(a) remains a separate task. No numerical acquisition was needed for the present opening deliverable.

[continuation]: 05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[previous]: 04_OPEN_BOUNDARIES_ZERO_FLUX_AND_BACKWARD_WIDTH_20261023.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[earlier]: ../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[regularization]: ../../../11_late_heat_caps_and_charge_transport/notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md
[coefficient]: ../../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[contours]: ../../manuscript/contours.tex
[snapshot]: ../../research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[height]: ../../../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md
[poly]: https://arxiv.org/html/1904.12438v2
[review]: ../reviews/02_NONREAL_WINDOW_AND_CURRENT_SELF_REVIEW_20261023.md
