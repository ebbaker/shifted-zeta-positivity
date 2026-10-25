# Negative endpoint: all-height evolution and actual covariance errors

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's session metadata.

**Status: estimates proved in-note; same-assistant review only.** This
advances the negative-time part of HDA-16. Under the unchanged global
regulator of Note 20, the Gaussian field approximates density, current,
time derivatives, potential and actual filtered covariance uniformly over
all real heights. The covariance error is `O(T^-3)` and its Laplacian error
is `O(T^-4)`, improving on the `O(T^-2)` obtained by a direct application
of the earlier global gradient comparison. The proof retains covariance
cancellation; it does not define a covariance from an equation residual.

The positive endpoint, a useful transition overlap, and the all-time
assembly are not completed. The separate HDA-19 result is [Note 25][outer].
Read the [result index][results], [heat-flow cluster][geometry],
[collision controls][controls] and [avoid index][avoid], particularly
[target classification][a01], [scope][a07] and [separate bounds][a12].
This is a quantitative approximation milestone. No RH or simplicity
conclusion follows. No numerical or machine-symbolic verification was
performed; [Review 09][review] records the same-assistant analytical audit.

## 1. Contract and the Gaussian field

Write `t=-T`, with `T>=1`, and choose fixed `eta>0`, `0<=A0<A`.
The observation domain is all real `x`, `|y|<=A0 sqrt(T)`. Use the
fixed product kernel `K=k_ell k_h` of Note 19, with `ell,h>0`, and require
\[
 T\ge T_0:=\max\{1,(h/(A-A_0))^2\}.
\tag{NE1}
\]
The entire convolution buffer and every segment between two of its points
then lie in `|y|<=A sqrt(T)`, all real `x`. There is no time averaging
or moving filter; every time derivative below is at fixed physical `x,y`.
The expanding transverse domain specifies a norm, not a derivative of a
rescaled observable or of a moving boundary.

Let `phi_0=Phi(0)`, `C=phi_0 sqrt(pi)/2`, and retain exactly
\[
 e=e_T=\epsilon_g(-T,x)=\eta C(1+T^2)^{-1/4},
 \quad q=e^2,\quad r_t={T\over1+T^2}=:b_T.
\tag{NE2}
\]
The approximating heat field is
\[
 G_T(z)={C\over\sqrt T}e^{-z^2/(4T)}.
\tag{NE3}
\]
It obeys `G_t=-G_zz` with `t=-T`. Assign it the same physical regulator
NE2, not just the asymptotic equivalent `eta C/sqrt(T)`.
Define `rho_G,j_G,S_G,w_G` by replacing `H` with `G` in Note 25 OH1.
In particular
\[
 \rho_G={e^2|z|^2|G|^2\over4\pi T^2(|G|^2+e^2)^2},\qquad
 j_G={e^2|G|^2\over\pi(|G|^2+e^2)^2}
       \left({\overline z\over4T^2}-{z^2\overline z\over8T^3}\right),
\tag{NE4}
\]
\[
 S_G=\log\left(e^2+{C^2\over T}e^{-(x^2-y^2)/(2T)}\right).
\]
Use `R_G=K*rho_G`, `J_G=K*j_G`, `U_G=K*S_G`, and the actual
\[
 Q_G=K*((S_G)_x^2-(S_G)_y^2)
      -((K*(S_G)_x)^2-(K*(S_G)_y)^2).
\tag{NE5}
\]
These fixed convolutions define the Gaussian observable model without
unknown theta roots, covariance fitting or harmonic adjustments.
All stated norms are absolute suprema on NE1's domain. The main physical
scales and their smaller errors are stated explicitly below.

## 2. Extend the source estimate before differentiating observables

Let `B_2` be the explicit complete-source constant in Note 11 (2)--(3),
so `|Phi(u)-phi_0|<=B_2 u^2/2` for `u>=0`. Define, for `0<=j<=4`,
\[
 J_m(A)=\int_0^\infty v^m e^{-v^2+Av}\,dv,\quad
 d_j={B_2 J_{j+2}(A)\over2T^{(j+3)/2}},\quad
 P_j={\phi_0 J_j(A)\over T^{(j+1)/2}}+d_j.
\tag{NE6}
\]
Then on the whole buffer,
\[
 |\partial_z^j(H-G)|\le d_j,\qquad
 |\partial_z^jH|,|\partial_z^jG|\le P_j.
\tag{NE7}
\]
The proof is the source Taylor remainder integrated against
`u^j exp(-T u^2+A sqrt(T)u)`. Thus it is independent of real height.
Differentiating the actual integral, whose differentiated integrands have
integrable majorants, proves NE7 for each order. No derivative of the
static error for `j=0` is asserted. The moments use Note 11's erfc formula
and recurrence, so all constants are specified by positive expressions.

For algebra only, write
\[
 u_j=P_j/e,\quad v_j=d_j/e,\quad c_0={125\over54\sqrt5}.
\tag{NE8}
\]
Here `u_j` and `v_j` denote nonnegative bounds, not field values or source
coordinates. Uniformly for `T>=T0`,
\[
 u_j=O(T^{-j/2}),\qquad v_j=O(T^{-j/2-1}).
\tag{NE9}
\]
These follow from NE2 and NE6; `A,eta` and the canonical source fix the
constants. Dividing by `e` is internal algebra at one time, not a change
to the physical evolution or a claim that `H/e` solves heat.

## 3. Density, current and time derivatives with explicit budgets

The earlier global rational-map comparison becomes
\[
 E_R={2u_1v_1+c_0u_1^2v_0\over\pi},\qquad
 E_J={u_1v_2+u_2v_1+c_0u_1u_2v_0\over\pi},
\tag{NE10}
\]
\[
 E_{13}={u_1v_3+u_3v_1+c_0u_1u_3v_0\over\pi},
 \qquad \rho_*={u_1^2\over\pi},
\]
\[
 E_{R,t}=2E_{13}+b_T(E_R+2\rho_*v_0)
           +2u_2E_R+2\rho_*v_2+4\rho_*u_2v_0.
\tag{NE11}
\]
They give, before and after positive normalized filtering,
\[
 |R-R_G|\le E_R=O(T^{-2}),\quad
 |J-J_G|\le E_J=O(T^{-5/2}),\quad
 |R_t-(R_G)_t|\le E_{R,t}=O(T^{-3}).
\tag{NE12}
\]
For the potential, regulator fraction and their time terms,
\[
 |U-U_G|\le v_0=O(T^{-1}),\quad |K*(w-w_G)|\le v_0,
\]
\[
 |U_t-(U_G)_t|\le v_2+(2u_2+b_T)v_0=O(T^{-2}).
\tag{NE13}
\]
For the actual forcing `B=r_t w` and source `s_r=r_t(1-2w)rho`,
\[
 |K*(B-B_G)|\le b_Tv_0=O(T^{-2}),
\]
\[
 |K*(s_r-(s_r)_G)|\le b_T(E_R+2\rho_*v_0)=O(T^{-3}).
\tag{NE14}
\]
The spatial curvature corrections of both models are exactly zero because
`q` has no spatial dependence at negative time.

**Proof.** For normalized field argument `a in C`, the map
`(1+|a|^2)^-2/pi` has maximum `1/pi` and gradient norm at most `c_0/pi`.
Product differences prove NE10. The exact density derivative OH10 of
Note 25 gives NE11, using the bounded maps
`bar a/(1+|a|^2)` (norm at most `1/2`, Lipschitz constant at most `1`)
and `w(a)=(1+|a|^2)^-1` (Lipschitz constant at most `1`). In particular
the terms involving `b_T` are retained. The same maps in
`S_t=-2 Re(H_zz bar H/(|H|^2+q))+r_t w` prove NE13. Finally apply
product differences to the forcing and current source. These arguments
compare true time derivatives; no static big-O estimate is differentiated.

The leading physical density, current and density derivative are bounded
by `O(T^-1)`, `O(T^-3/2)` and `O(T^-2)`, respectively. Thus NE12 gives
`O(T^-1)` absolute errors after multiplying by `T`, `T^(3/2)` and `T^2`.
At points where a reference observable vanishes this remains an absolute
comparison, not a relative error claim.

## 4. Uniform spatial derivatives of the potential difference

A finite, reusable composition bound supplies the covariance estimates
without hiding higher derivatives. Identify `C` with `R^2` and set
`F(a)=log(1+|a|^2)`. Define, for `m>=1`,
\[
 C_m=\sum_{p=0}^{\lfloor m/2\rfloor}
 {m!\,(m-p-1)!\over(m-2p)!\,p!}.
\tag{NE15}
\]
Only `C_1,...,C_5` are used. The norm of the real multilinear derivative
`D^m F` is at most `C_m`, globally in `a`.

To see this, differentiate `log g` with `g=1+|a|^2`. A term indexed by a
partition into `k` blocks has coefficient `(k-1)!` in absolute value.
Only singleton and pair blocks survive, and their normalized derivative
bounds are `|Dg|/g<=1`, `|D^2g|/g<=2`. A partition with `p` pairs has
`k=m-p` blocks and there are `m!/[(m-2p)!p!2^p]` such partitions.
Their sum is NE15. This is a dimension-independent bound for unit real
directions, not a componentwise norm asserted to be an operator norm.

Let `Pi_m` be the finite set of partitions of `{1,...,m}`. For
`1<=m<=4`, set
\[
 B_m=\sum_{\pi\in\Pi_m}C_{|\pi|}
                   \prod_{B\in\pi}u_{|B|},
\tag{NE16}
\]
\[
 D_m=\sum_{\pi\in\Pi_m}\left[
 C_{|\pi|+1}v_0\prod_{B\in\pi}u_{|B|}
 +C_{|\pi|}\sum_{B\in\pi}v_{|B|}
                         \prod_{B'\in\pi,\ B'\ne B}u_{|B'|}
 \right].
\tag{NE17}
\]
Then the spatial real derivative tensors obey
\[
 \|D^m S\|,\|D^m S_G\|\le B_m=O(T^{-m/2}),\qquad
 \|D^m(S-S_G)\|\le D_m=O(T^{-m/2-1}).
\tag{NE18}
\]
Also `|S-S_G|<=v0` as above. These explicit finite sums are proof bounds,
not a requested symbolic computation.

**Proof.** At fixed time, `S=log(e^2)+F(H/e)`. Holomorphy gives
`|D^j(H/e)[v_1,...,v_j]|<=u_j product |v_i|`, and the corresponding
error is bounded by `v_j product |v_i|`. Apply the real composition
partition formula. For the difference, first change the argument of
`D^k F`, costing `C_(k+1)v0`; then telescope the `k` derivative factors,
one at a time. Bounds `u_j` hold for both fields and their straight
segment. This proves NE16--NE18 with all mixed x/y directions included.
The rates follow because the block sizes sum to `m`. No logarithmic
derivative `H_z/H`, zero exclusion or simple-root assumption is used.

For a sharper spatial forcing budget, the same argument applies to
`W(a)=(1+|a|^2)^-1`. Its derivative constants may be taken as
\[
 C_m^w=\sum_{p=0}^{\lfloor m/2\rfloor}
 {m!\,(m-p)!\over(m-2p)!\,p!},\qquad m\ge1.
\tag{NE18a}
\]
The additional undifferentiated factor `1/g<=1` and the coefficient `k!`
in derivatives of `1/g` prove this formula. Let `D_m^w` be NE17 with
all `C` replaced by `C^w`. For `m=1,2` it bounds
`||D^m(w-w_G)||=O(T^(-m/2-1))`. In particular
\[
 |K*\Delta(B-B_G)|\le 2b_T D_2^w=O(T^{-3}).
\tag{NE18b}
\]
This supplies the differentiated forcing without losing its spatial
scale by moving every derivative onto the kernel.

## 5. Retaining cancellation in the actual covariance

For any fixed positive normalized `K`, write
\[
 \operatorname{Cov}_K(f,g)=K*(fg)-(K*f)(K*g),\qquad
 \sigma_K^2=\int|a-\bar a|^2K(a)\,da,\quad \bar a=\int aK(a)\,da.
\]
For our even compact kernel `bar a=0` and
`0<sigma_K^2<=ell^2+h^2`. On the convex full buffer,
\[
 \operatorname{Cov}_K(f,g)
 ={1\over2}\iint K(a)K(b)
 [f(z-a)-f(z-b)][g(z-a)-g(z-b)]\,da\,db,
\tag{NE19}
\]
so
\[
 |\operatorname{Cov}_K(f,g)|\le\sigma_K^2
              \operatorname{Lip}(f)\operatorname{Lip}(g).
\tag{NE20}
\]
This follows from the line-segment mean-value bound and
`(1/2)int int |a-b|^2 K(a)K(b)=sigma_K^2`.

Apply the identity to the two signed components of `Q`. Product
differences and NE18 give the improved comparison
\[
 \boxed{|Q-Q_G|\le4\sigma_K^2 B_2D_2=O(T^{-3}).}
\tag{NE21}
\]
In this section `B_m,D_m` are NE16--NE17, not Note 11's source constant.
Also `|Q|,|Q_G|<=2 sigma_K^2 B_2^2=O(T^-2)`.

For the Laplacian, differentiating the actual covariance under a fixed
kernel yields, with `s_x=1,s_y=-1`,
\[
 \Delta Q=2\sum_{i=x,y}s_i\sum_{a=x,y}
 \left\{\operatorname{Cov}_K(S_{ia},S_{ia})
       +\operatorname{Cov}_K(S_i,S_{iaa})\right\}.
\tag{NE22}
\]
Use NE20 on each product difference. The Lipschitz bounds for
`S_ia`, `S_i`, `S_iaa` are respectively `B_3,B_2,B_4`; their difference
bounds are `D_3,D_2,D_4`. There are two components and two derivative
directions. Consequently
\[
 \boxed{|\Delta Q-\Delta Q_G|\le
 16\sigma_K^2 B_3D_3+
 8\sigma_K^2(B_4D_2+B_2D_4)=O(T^{-4}).}
\tag{NE23}
\]
And `|Delta Q|,|Delta Q_G|<=8 sigma_K^2(B_3^2+B_2B_4)=O(T^-3)`.

Thus both covariance quantities have an error smaller by one power of
`T` than the corresponding upper physical scale. NE21 and NE23 use
finite-width covariance cancellation; separately bounding squares of
first gradients would lose that power. NE22 is an exact derivative
identity, and NE18 controls the needed fourth spatial derivatives.
No differentiation of NE21's error allowance is performed.

## 6. Evolution, traces, and status

Every quantity of the Gaussian field, including its actual covariance,
obeys Note 14's fixed-filter adaptive equations with the same time-only
regulator. In particular
\[
 \Delta U_G=4\pi R_G,\qquad
 (U_G)_t=-\tfrac12\{\mathcal D U_G+(U_G)_x^2-(U_G)_y^2+Q_G\}
                  +K*B_G,
\]
\[
 (R_G)_t+\operatorname{div}J_G=K*(s_r)_G.
\tag{NE24}
\]
The density potential equation retains `Delta(K*B_G)/(4pi)`; spatial
curvature and both its derivatives vanish identically here. One may
move spatial derivatives onto the fixed kernel in NE12--NE14, or use
NE18 for potential derivatives through fourth order. In particular the
comparison pays all terms of the negative-time version of P3a--P5a.
NE18b pays the differentiated forcing at order `T^-3`; exact current
balance also gives `div(J-J_G)=O(T^-3)` from NE12 and NE14.
The absolute source comparisons supply the potential itself as well as
its derivatives, so no free harmonic datum is being used.

Boundary values of `U`, its normal derivative and normal current on any
observation boundary inside NE1 inherit the same errors from the full
buffer. On a moving transverse boundary the normal-flux comparison is
still pointwise; an evolution of an integral over that moving region
would additionally use its transport formula. Such a moving-domain
identity is not silently included in NE24.

This completes the stated **negative-endpoint direct-comparison budgets**
on all real heights and the declared transverse scale. It does not
complete HDA-16, whose positive potential/covariance and outer comparison
remain open, or HDA-18, which still requires transition and positive
endpoint overlaps. There is no new regulator-to-zero-measure conclusion:
the Gaussian is zero-free and its regulated density is a measurement
background, not a zero-count approximation.

The control screen is the same source-specific one as Note 11. Positive
atoms and heat polynomials fail the smooth canonical source Taylor
premise. Euler-factor, weighted-square/finite-prime, reflected and
positive-primitive sources do not inherit the unchanged canonical
`phi_0,B_2`. Any smooth even colliding source with its own finite second
source-derivative bound can satisfy an analogous Gaussian theorem;
NE10--NE23 are generic zero-safe comparisons. They therefore do not
exclude collision controls or constitute an arithmetic simplicity test.
The Gaussian control is the exact zero-source-error case of every
comparison, including covariance cancellation.

Next retain these budgets while developing Note 25's proposed positive
noncompact outer representation; do not replace the remaining positive
work with a larger transition mesh. A future use of finite-time overlap
must compare both models to theta at the same regulator and account for
any joining terms. No computation is requested until an analytical
question specifies its finite inputs and decision. The maintained
manuscript remains at Note 23's integration; Notes 25--26 are linked
research advances pending its next revision and independent review.

[outer]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/09_OUTER_TAIL_AND_NEGATIVE_ENDPOINT_SELF_REVIEW_20261024.md
