# Positive continuous threshold controls inside the theta Gram norm ball

20 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual reasoning effort **ultra**, inherited from parent turn `01a157aa-be5d-72e0-90dc-ed57a8823b52` and verified there.

**Status: scoped analytic obstruction, proved in-note; [separate same-model internal review][review], not specialist review.** This strengthens [Note 02][gram]: its enlarged multiplier class still contains controls with `Q_L>0` after requiring a nonnegative continuous multiplier and an actual positive all-real threshold. The controls have bounded compact source support, uniform complete moment budgets, exact event cancellation at the fixed height `a=20`, and exactly the same norm budget in the *reference theta Hilbert space*. Their normalized deflated jet `S_2` tends to infinity.

These are changed sources represented relative to theta. Their coefficients, mass and imaginary-axis profile are not theta's. Their own source moments are computed below, separately from the reference theta Gram entries. No positive theta threshold, arithmetic sign, physical exclusion, later witness, or new covered region is established. The result closes an additional repair of one estimator class; BW2-04/05 remain inactive on this evidence.

The [active program][program], [result summaries][results], [collision controls][controls] and [patterns to avoid][avoid] apply, particularly [classification][a01], [scope][a07] and [signed recombination][a12]. This is an explicit counterexample family for a restricted inference, not an RH-equivalent reformulation. Unlike the earlier atomic control, these controls are genuine bounded nonnegative multipliers in `L²` of the unchanged theta reference measure. No claim that they preserve theta's arithmetic expansion is made.

## 1. Domain and explicit positive event density

Fix `0<T<=1/2`, `a=20`, and

\[
 \kappa=\frac1{2a},\qquad \frac12\le q<1,\qquad
 \theta_q=\arccos(-q),\quad \lambda_q=\theta_q/a,
 \quad A_q=(1+q)^{-2}.
\]

The normalized atomic slice from [BW-01 Note 04][atomic] is

\[
 B_q(z)=A_q(\cos(\lambda_qz)+q)^2.
\tag{1}
\]

It is the Fourier transform of the probability measure on the whole real line

\[
 \beta_q=A_q\left[(q^2+\tfrac12)\delta_0
    +q(\delta_{\lambda_q}+\delta_{-\lambda_q})
    +\tfrac14(\delta_{2\lambda_q}+\delta_{-2\lambda_q})\right].
\tag{2}
\]

All masses are positive and sum to one. Define the triangular probability density

\[
 \tau_\kappa(v)=\frac{(2\kappa-|v|)_+}{4\kappa^2},
 \qquad \int_{\mathbb R}\tau_\kappa(v)e^{izv}\,dv
 =J_\kappa(z):=\left(\frac{\sin\kappa z}{\kappa z}\right)^2.
\tag{3}
\]

The equality follows by convolving two uniform probability densities on `[-kappa,kappa]`; the removable value at `z=0` is one. Let

\[
 p_q=\tau_\kappa*\beta_q,\qquad f_q(u)=2p_q(u)\quad(u\ge0),
 \qquad F_q(z)=J_\kappa(z)B_q(z).
\tag{4}
\]

Then `f_q` is a nonnegative continuous, piecewise linear half-line density, with

\[
 \int_0^\infty f_q(u)\,du=1,\qquad
 F_q(z)=\int_0^\infty f_q(u)\cos(zu)\,du,
 \qquad 0\le f_q(u)\le\frac1\kappa.
\tag{5}
\]

There is no atom at zero after convolution; the factor two in (4) is essential. The density is positive near zero, may vanish between the shifted triangles, and is not claimed to be smooth at their knots. All supports lie in the fixed compact interval

\[
 [0,U],\qquad U=2\kappa+2\pi/a=(1+2\pi)/a.
\tag{6}
\]

The exact event is retained because `kappa a=1/2`, so `J_kappa(a)>0`, while `B_q` has an exact double zero at `a` for every `q<1`.

## 2. Exact membership in the reference theta norm ball

Let the unchanged theta event measure be

\[
 d\nu_\theta(u)=\rho_T(u)\,du=e^{Tu^2}\Phi(u)\,du,
 \quad M_0=\nu_\theta([0,\infty)),\quad
 N_U=\nu_\theta([0,U]).
\tag{7}
\]

The source `Phi` is exactly [BW-01 Contract 02][source], with every square coefficient retained. Its density is strictly positive. In particular, using just its positive `n=1` summand gives the explicit common lower bound

\[
 \rho_T(u)\ge m_\theta:=
 \pi(2\pi-3)\exp[-\pi\exp(4U)]>0\qquad(0\le u\le U).
\tag{8}
\]

Indeed `e^{Tu²}>=1`, `e^{5u}>=1`, `2pi e^{4u}-3>=2pi-3`, and `exp(-pi e^{4u})>=exp(-pi e^{4U})`. Also `0<N_U<M_0` because the complete theta density has positive mass beyond `U`.

Define the actual density ratio and its squared norm

\[
 v_q=f_q/\rho_T,\qquad
 I_q=\int_0^\infty v_q^2\,d\nu_\theta
     =\int_0^U\frac{f_q(u)^2}{\rho_T(u)}\,du.
\tag{9}
\]

From (5), (8), and Cauchy--Schwarz on `[0,U]`,

\[
 \frac1{N_U}\le I_q\le\frac1{\kappa m_\theta}.
\tag{10}
\]

The upper bound uses `f_q²<=f_q/kappa` before integration, rather than paying support length again. Set

\[
 c_q=\sqrt{M_0/I_q},\qquad w_q=c_qv_q.
\tag{11}
\]

These are bounded, compactly supported, nonnegative continuous multipliers. They satisfy

\[
 \boxed{\|w_q\|_{L^2(\nu_\theta)}^2=M_0,\qquad
 \sqrt{M_0\kappa m_\theta}\le c_q
 \le\sqrt{M_0N_U}<M_0.}
\tag{12}
\]

For example `w_q<=sqrt(M_0N_U)/(kappa m_theta)` uniformly. The associated physical heat fields are

\[
 \widetilde H_q(t,z)=c_q\int_0^U
 e^{(t-T)u^2}f_q(u)\cos(zu)\,du.
\tag{13}
\]

Their nonnegative time-zero source is exactly `c_q e^{-Tu²} f_q(u)du`. Equivalently it is `w_q(u)Phi(u)du`; the multiplier is held fixed as `t` varies. At the event,
`Htilde_q(T,z)=c_q F_q(z)`. Thus the two event cancellations are exact and (12) is the precise norm budget used in Note 02.

The fifteen Gram entries of the five functions and the Schur complement in Note 02 remain those of the **reference measure** `nu_theta`. Their use for these controls is justified by the exact change of measure (9)--(13) and Cauchy--Schwarz. They are not falsely assigned as the Gram matrix or moments computed under the control's own measure. For that own measure, the complete moment budget is separately

\[
 \widetilde M_j(T+\Delta)
 =c_q\int_0^Ue^{\Delta u^2}u^jf_q(u)\,du
 \le\sqrt{M_0N_U}\,e^{\Delta U^2}U^j
 \quad(\Delta\ge0,\ j\ge0).
\tag{14}
\]

There is no tail or omitted source component in these inequalities.

## 3. The all-real threshold is actually T

Every zero of `B_q` is real: if `cos(lambda z)=-q` with `0<q<1` and `z=x+iy`, a nonzero `y` would force `sin(lambda x)=0`, making the real part have absolute value at least one. Every zero of `J_kappa` is also real. Therefore `F_q` is even real entire, of exponential type, with only real zeros, and is in the Laguerre--Pólya class: its paired canonical product is a locally uniform limit of finite real-rooted polynomials. The paired product has convergent reciprocal-square zero sum; here this also follows directly from the explicit arithmetic sequences of the zeros of the two factors. Equivalently one can use their standard sine products. The positive normalization at zero fixes the constant.

For completeness the needed heat-preservation argument applies to the **compact continuous** source, not only finite trigonometric sums. For real-rooted polynomials, `p+v p'` is real-rooted for real `v`, by interlacing and the monotonicity of `p'/p` between consecutive roots. Hence

\[
 1-d\partial_z^2=(1-\sqrt d\,\partial_z)(1+\sqrt d\,\partial_z)
\]

preserves real-rootedness for `d>=0`. Local uniform convergence of entire functions implies local uniform convergence of their derivatives, so the operator also preserves the Laguerre--Pólya class. For each `s>=0`,

\[
 \left(1-\frac{s}{n}\partial_z^2\right)^n F_q(z)
 =\int_0^U(1+su^2/n)^n f_q(u)\cos(zu)\,du
 \longrightarrow\int_0^Ue^{su^2}f_q(u)\cos(zu)\,du.
\tag{15}
\]

The convergence is uniform on compact sets of `z`, since `u` stays in `[0,U]`. The nonzero limit is in the same class. Thus every zero of (13) is real for every `t>=T`.

At `(T,a)` the exact double jet is

\[
 \widetilde h_2=c_qJ_\kappa(a)\,2A_q\lambda_q^2(1-q^2)>0.
\tag{16}
\]

The backward heat equation gives the local form
`(htilde_2/2)(z-a)^2-htilde_2(t-T)` to leading parabolic order. For times immediately below `T`, quadratic rescaling and Rouché's theorem give a nonreal conjugate pair near `a`. If any earlier slice had only real zeros, that even real entire function of exponential type would itself belong to the Laguerre--Pólya class by its paired product. Applying (15) to its compactly supported, heat-weighted source would propagate real-rootedness to those near-threshold slices, a contradiction. Consequently (13) has **exact all-real threshold T**.

The functions have infinitely many simultaneous real multiple zeros at `T`; their eventual simplicity at that time fails. The construction does not import theta's corresponding premise. This limitation is unchanged by the compact smoothing.

## 4. Divergent normalized jet and positive raw quadratic

For any exact double event define

\[
 S_2=\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}
 =-\left.\frac{d^2}{dz^2}\log\left|\frac{H(T,z)}{(z-a)^2}\right|\right|_{z=a}.
\tag{17}
\]

The identity follows by dividing the Taylor series at `a`; no root sum is needed for the calculation here. Since `J_kappa(a)>0`, the product (4) and the exact atomic formula yield

\[
 \widetilde S_2
 =\lambda_q^2\frac{4-q^2}{6(1-q^2)}
 +2\kappa^2\csc^2(\kappa a)-\frac2{a^2}
 >\frac{2\pi^2}{9a^2(1-q^2)}.
\tag{18}
\]

The added term is strictly positive because `kappa a=1/2` and `sin(1/2)<1/2`; the lower estimate uses `lambda_q>=2pi/(3a)` and `4-q²>3`. Thus `Stilde_2` diverges while `T`, `a`, the reference norm, support bound, and complete moment budgets stay fixed. The nonzero curvature in (16) tends to zero; no uniform curvature floor is claimed.

For each fixed finite `L>0`, choose `q` close enough to one that
`1-q²<2pi²/(9a²L)`. Then

\[
 \boxed{\widetilde Q_L
 =2\widetilde h_3^2-3\widetilde h_2\widetilde h_4
       -18L\widetilde h_2^2
 =18\widetilde h_2^2(\widetilde S_2-L)>0.}
\tag{19}
\]

This includes each fixed admissible inherited coefficient `0<L<=L_2(20)`. It follows that adding **nonnegative multipliers and a genuine all-real threshold** to Note 02's reference norm and exact event information does not make a universal upper bound `Q_L<=0` valid. There is also no finite uniform upper bound on `S_2` for this stronger class. Equation (19) concerns the controls' actual complete fields, not the unchanged theta field.

We do not claim the positive-constrained optimum equals Note 02's signed spectral maximum, or that (19) has a uniform positive raw margin as `q->1`. The normalized quantity diverges while the raw jets degenerate. A separately prescribed lower bound on `|h_2|` remains outside the result.

## 5. The failed mass premise is explicit and uniform

The physical theta multiplier `w=1` has exact event mass `M_0`. For these controls,

\[
 \langle w_q,1\rangle_{\nu_\theta}=c_q
 \le\sqrt{M_0N_U}=M_0-\delta_U,
 \qquad \delta_U:=M_0-\sqrt{M_0N_U}>0.
\tag{20}
\]

Thus every control fails the exact mass anchor, by a fixed positive amount. They also fail an approximate anchor `mass>=M_0-eta` whenever `eta<delta_U`. No conclusion is made for larger `eta`. Keeping exact mass and the norm budget would force `w=1` by equality in Cauchy--Schwarz, as Note 02 proved; the present construction does not evade that fact.

Their imaginary-axis profile has the own-source bound
`0<=partial_b log Htilde_q(T,ib)<=U` for `b>=0`, by (13), so they fail theta's unbounded large-height lower profile. They also fail the unchanged square coefficients, full-support density, and eventual simplicity at the threshold. These failures identify the limits of the inference; they do not mean every derived theta inequality is false on the controls.

## 6. Corollary: exact finite-profile controls can also have continuous densities

The same fixed smoothing applies to the normalized positive finite-atom pencil in [BW-08 Note 05, Section 5A][profile]. That note owns the interpolation construction: for every prescribed finite set of distinct positive heights `b_i`, it supplies a family `F_epsilon` with `F_epsilon(0)=1`, a fixed vector of exact `D_epsilon(b_i)`, fixed `T,a`, genuine threshold `T`, common support `[0,N lambda]`, and `S_2(F_epsilon)` diverging. The vector is constructed; it is not an arbitrary prescribed or measured theta vector.

Before any theta-norm scaling, replace that slice by

\[
 \widehat F_\varepsilon(z)=J_\kappa(z)F_\varepsilon(z),
 \qquad \kappa=1/(2a).
\tag{21}
\]

Convolution with (3) gives a nonnegative continuous compact event density of mass one, with support in `[0,V]`, `V=N lambda+2kappa`. Its own complete heat moments obey `M_j(T+Delta)<=exp(Delta V²)V^j`. The normalization and profile samples are exactly

\[
 \widehat F_\varepsilon(0)=1,\qquad
 \widehat D_\varepsilon(b_i)=D_\varepsilon(b_i)
       +2\kappa\coth(\kappa b_i)-2/b_i.
\tag{22}
\]

The added quantities are independent of `epsilon`, so every selected sample remains fixed. At the exact double event,

\[
 S_2(\widehat F_\varepsilon)=S_2(F_\varepsilon)
       +2\kappa^2\csc^2(\kappa a)-2/a^2
       >S_2(F_\varepsilon)\longrightarrow\infty.
\tag{23}
\]

The curvature is multiplied by the nonzero `J_kappa(a)`, and Section 3's compact-source argument proves that the threshold remains exactly `T`. Thus the finite exact-profile obstruction also holds for **nonnegative continuous compact densities**, with the same normalization and common moments. Atomicity is not needed for that restricted theorem. The densities need not be smooth at the triangle knots; they still fail theta's full source, unbounded large-height profile and eventual simplicity at the threshold. This corollary does not simultaneously impose the physical theta mass and theta norm anchor. It transfers the canonical finite-profile counterexample rather than deriving or acquiring new theta observations.

If simultaneous membership in the reference theta norm ball is wanted, use a **common** scale for this entire pencil. With `m_theta(V)=pi(2pi-3)exp[-pi exp(4V)]` and `N_V=nu_theta([0,V])`, set `c_*=sqrt(M_0 kappa m_theta(V))`. The same proof as (10) gives `||c_* fhat_epsilon/rho_T||²<=M_0` for every member. The resulting mass is the fixed positive `c_*`, all samples (22) are unchanged, and (23) still diverges. Here `c_*<=sqrt(M_0N_V)<M_0`; the mass is not theta's, and norm **equality** is not asserted. This supplies fixed control mass, fixed finite profiles and one common norm budget without concealing which anchor is absent.

## 7. Complete ledger, controls and stopping conclusion

All integrations, convolutions, norm scaling, event jets and time propagation above are exact analytic operations. The source support is finite, but is not a truncation of theta: it is the complete control source. No quadrature, theta cutoff, parameter uncertainty, derivative-acquisition error or numerical event location is used. The reference theta moments and compact mass are exact quantities; only the symbolic lower bound (8) is used to prove finite uniform conditioning. No numerical value for `m_theta`, `N_U` or `c_q` is asserted.

The control comparison is therefore explicit:

- The earlier BW-01 atomic family supplies (1) and its exact jet formula, but its atomic source ratio is not an `L²(nu_theta)` function. The triangle convolution and norm scaling repair precisely that missing premise.
- The new controls have their own nonnegative continuous densities, actual threshold, cancellations and moments (5), (13)--(19). Their admission to the reference Gram norm ball is proved by (9)--(12). No theta moment budget is substituted for their own source without this change-of-measure argument.
- Euler-factor, weighted-square, finite-prime, reflected, primitive and auxiliary-channel controls retain only their documented premises in [cluster 12][controls]. No new threshold, multiplicity, source ratio, or quantitative rejection is asserted for those families. The explicit present family alone falsifies the stronger proposed inference.
- Hermite/quartic models do not automatically supply a positive source ratio. Independent multiplicative phases are absent: every field above is evaluated at its one fixed physical height and time.

**Stop the positivity-plus-actual-threshold repair of this reference-theta norm relaxation.** A continuation must quantitatively retain some additional information excluding these changed sources, such as a sufficiently tight mass anchor together with signed physical data, a proved curvature restriction, or complete coefficient-level arithmetic beyond membership in the reference ball. A more elaborate realization of the same ball does not supply the missing theta sign. This is a stronger scoped obstruction than Note 02's signed witness, not a global impossibility theorem for source-specific estimates.

The [input receipt][receipt] binds the source versions and this note to the parent Git revision. It records file identity only. A [separate same-model review][review] records the internal assessment; there is no specialist review or numerical certificate.

[gram]: 02_EVENT_CONDITIONED_THETA_GRAM_OBSTRUCTION_20261020.md
[program]: ../../04_boundary_winding/research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[source]: ../../04_boundary_winding/threshold_routes/01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[atomic]: ../../04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/02_POSITIVE_MULTIPLIER_GRAM_REVIEW_20261020.md
[receipt]: ../numerics/POSITIVE_MULTIPLIER_INPUTS_20261020.json

[profile]: ../../04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md
