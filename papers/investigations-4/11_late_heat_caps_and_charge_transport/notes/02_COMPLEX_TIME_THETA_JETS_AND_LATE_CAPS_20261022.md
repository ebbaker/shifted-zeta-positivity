# Canonical complex-time root caps with a complete integrated remainder

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from the parent turn metadata. Status: **proved in-note; separate same-model internal review**. See the [internal review][review]. No specialist review or endpoint exclusion.

**Classification.** A direct canonical-source estimate on a fixed finite collection of late root caps. This is a quantitative milestone, not an RH-equivalent exclusion criterion. It needs no root-pair statistics. Its physical projective radius shrinks with the real heat saddle. It covers both shrinking and fixed bounded imaginary-time widths, with different evaluated cap limits. It does not by itself connect a cap to an endpoint event or estimate the remaining boundary.

The [result index][results] and [avoid index][avoid] apply, especially [collision controls][controls], [heat geometry][heat-geometry], [target classification][a01], [matching controls][a02], [scope][a07] and [coupled errors][a12]. The imported source is the complete canonical theta source of [BW10 Note 20][saddle], §§1,3, with ownership retained by the [canonical-source home][source]. The source proof, rather than the inherited real clock limit alone, supplies the following complex-time estimates. Only its explicit scalar density inequalities are imported. The [finite attachment construction][geometry] and [complete closure accounting][closure] connect the present cap family to its full boundary.

## 1. Parameters, source normalization and complete moments

Write
\[
H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
\qquad A_T=H(T,0)>0,
\]
with exactly the canonical source and the convention \(H_\tau=-H_{zz}\). Its positive density is
\[
e^{Tu^2}\Phi(u)=2\pi^2e^{q_T(u)}b(u),\qquad
q_T(u)=Tu^2+9u-\pi e^{4u},
\]
\[
b(u)=\sum_{n\ge1}\left(n^4-\frac{3n^2e^{-4u}}{2\pi}\right)
 e^{-\pi(n^2-1)e^{4u}},\qquad
b_*:=1-\frac3{2\pi}\le b(u)\le B_*:=\frac1{1-16e^{-3\pi}}.
\tag{1}
\]
Every theta index is retained. Let \(L=L_T\) be the large stationary point and
\[
4\pi e^{4L}=2TL+9,\qquad \kappa=8TL-2T+36.
\]
Set \(\delta=1/4\), \(c=1/(4e)\), and impose the finite checks
\[
L\ge1,\quad \kappa\ge32,\quad T/\kappa\le1/(4e),\quad
q_T(L-\delta)\ge q_T(0).
\tag{2}
\]
These hold for all sufficiently large real \(T\), and \(L\sim(\log T)/4\), \(\kappa\sim8TL\). Let \(U\) have probability density \(e^{Tu^2}\Phi(u)/A_T\), and put \(V=U-L\).

For fixed \(Z\), define
\[
N_T=2b_*\exp\left[-\frac12-\frac{4e}{3\sqrt\kappa}\right],\qquad
J_k(a)=\int_{\mathbb R}|w|^k e^{-cw^2+a|w|}\,dw,
\]
\[
\boxed{W_k(T,Z)=\frac{B_*}{N_T}\left[
\kappa^{-k/2}J_k\left(\frac{Z}{L\sqrt\kappa}\right)
+L^{k+1}\sqrt\kappa\,e^{Z-c\kappa\delta^2}\right],\quad k=1,2,3.}
\tag{3}
\]
These are complete explicit scalar Gaussian integrals, equivalently derivatives of the shifted Gaussian integral. They satisfy
\[
\mathbb E\bigl[|V|^k e^{Z|V|/L}\bigr]\le W_k,
\qquad W_k=O_{k,Z}(\kappa^{-k/2}).
\tag{4}
\]

**Proof.** The imported exact saddle identity is
\[
q_T(L+v)-q_T(L)=Tv^2-\pi e^{4L}(e^{4v}-1-4v).
\]
Under (2), the source proof bounds this by \(-c\kappa v^2\) on \(v\ge-\delta\), and by \(-c\kappa\delta^2\) on \(-L\le v\le-\delta\). On \(|w|\le1\), \(v=w/\sqrt\kappa\) has
\[
q_T(L+w/\sqrt\kappa)-q_T(L)\ge-w^2/2-4e/(3\sqrt\kappa).
\]
The rescaled normalization is therefore at least \(N_T\). The near/right weighted numerator is at most the first term in (3); the entire far-left interval has rescaled length at most \(L\sqrt\kappa\), \(|V|\le L\), and weight at most \(e^Z\), giving its second term. This pays both source tails, all indices, the exponential spatial weight, and normalization. No small relative physical-field floor is assumed.

## 2. Complex-time physical-jet bounds

Fix finite \(K\ge1\), \(S>0\), and set
\[
r_1=1/3,\quad r=1/4,\quad \rho=1/4,\quad
Z=(K-\tfrac12)\pi+\operatorname{arctanh}r_1+\rho.
\]
On \(|\eta|\le S\), \(|w|\le Z\), put
\[
F(\eta,w)=\frac{H(T+i\eta/L^2,w/L)}{A_T},\qquad F_j=\partial_w^jF.
\]
For \(j=0,1,2,3\), let \(c_j(w)=\partial_w^j\cos w\) and
\[
\boxed{B_j=e^Z\left[
\sum_{k=1}^j {j\choose k}\frac{W_k}{L^k}
+\frac{ZW_1}{L}
+S\left(\frac{2W_1}{L}+\frac{W_2}{L^2}\right)\right].}
\tag{5}
\]
The sum is zero for \(j=0\). Then
\[
|F_j-e^{i\eta}c_j(w)|\le B_j,
\qquad B_j=O_{K,S}\left(\frac1{L\sqrt\kappa}\right).
\tag{6}
\]
Indeed \(F_j=\mathbb E[R^je^{i\eta R^2}c_j(Rw)]\), \(R=U/L\). Split its difference from \(e^{i\eta}c_j(w)\) into the factor \(R^j-1\), spatial displacement, and phase displacement. The bounds
\[
|R^j-1|\le\sum_{k=1}^j{j\choose k}|V|^k/L^k,
\quad |c_j(Rw)|\le e^Ze^{Z|V|/L},
\]
\[
|c_j(Rw)-c_j(w)|\le Ze^Z|V|e^{Z|V|/L}/L,
\quad |e^{i\eta(R^2-1)}-1|\le S(2|V|/L+V^2/L^2)
\]
prove (5). Absolute convergence of the complete source permits the derivatives. Exactly,
\[
F_\eta=-iF_2,\qquad (F_1)_\eta=-iF_3.
\tag{7}
\]

The physical jet is
\[
\boxed{G=A_T(F,LF_1).}
\tag{8}
\]
Thus the second component is not replaced by \(F_1\). Its cap-coordinate derivatives are
\[
A_T^{-1}\partial_wG=(F_1,LF_2),\qquad
A_T^{-1}\partial_\eta G=(-iF_2,-iLF_3).
\]
The factors \(L\), \(\partial_s=L^2\partial_\eta\), and \(\partial_z=L\partial_w\) are retained. The positive real source normalization \(A_T\) cancels only as a scalar in the normalized jet; the common phase \(e^{i\eta}\) remains.

## 3. Actual inverse root caps

Write \(s_j=(j-1/2)\pi\), \(\sigma_j=\sin s_j\in\{1,-1\}\), and
\[
w_{0,j}(v)=s_j+\arctan v,\qquad |v|\le r_1.
\]
The principal analytic branch is well-defined on this disk. Put
\[
d_0=\operatorname{arctanh}r_1+\rho,\quad
c_0=2-\cosh d_0>0,\quad
m_0=\sqrt{1-r_1^2}(2\rho-\sinh\rho)>0.
\]
Require
\[
B_0+r_1B_1<m_0,\qquad B_1<c_0.
\tag{9}
\]
For every \(|\eta|\le S\), \(|v|\le r_1\), the equation
\[
F(\eta,w)-vF_1(\eta,w)=0
\tag{10}
\]
has precisely one solution \(w_j(\eta,v)\) in \(|w-w_{0,j}(v)|<\rho\), counted with multiplicity. It is simple, smooth in \(\eta\), holomorphic in \(v\), and \(F_1\ne0\) there. At that solution
\[
\frac{H}{H_z}=\frac vL.
\]

**Proof.** The reference equation is
\[
e^{i\eta}(\cos w+v\sin w)
=-\sigma_j e^{i\eta}\sqrt{1+v^2}\sin(w-w_{0,j}(v)).
\]
On the radius-\(\rho\) circle its modulus is at least \(m_0\), since \(|\sin\xi|\ge2\rho-\sinh\rho\) when \(|\xi|=\rho\). Its perturbation is at most \(B_0+r_1B_1\); Rouché gives one simple solution. Furthermore \(|\sin w|=|\cos(w-s_j)|\ge2-\cosh d_0=c_0\) throughout the disk, so \(|F_1|\ge c_0-B_1>0\). Local implicit inverses patch by uniqueness. This proves an actual regular projective cap, not merely a formal equation containing joint zeros.

For any
\[
0<S_T\le S,\qquad 0<r_T\le r,\qquad
Y_T=S_T/L^2,\quad \epsilon_T=r_T/L,
\]
define the terminal cap
\[
M_{T,j}=\{(\tau,z)=(T+i\eta/L^2,w_j(\eta,v)/L):
|\eta|\le S_T,\ |v|\le r_T\}.
\tag{11}
\]
The map is embedded: \(\tau\) specifies \(\eta\) and \(H/H_z=v/L\) specifies \(v\). It has positive Jacobian for the forward cap orientation:
\[
ds\wedge d\Re z\wedge d\Im z
=L^{-4}|(w_j)_v|^2\,d\eta\wedge d\Re v\wedge d\Im v.
\tag{12}
\]
Here \((w_j)_v=F_1/(F_1-vF_2)\ne0\). The cap's spatial edge is the regular level \(|H/H_z|=\epsilon_T\). A finite connector can use smaller \(S_T,r_T\), with no lower bound required in this theorem. A radius fixed independently of \(T\) is not asserted: the reference inverse has branch points at \(v=\pm i\), or \(q=\pm i/L\).

## 4. Full normalized jet and first tangential derivatives

The following explicit bounds make the normalized-jet contract complete, although the sharper integrated remainder below uses the exact chart formula. Put
\[
a_\rho=2-\frac{\sinh\rho}{\rho}>0,\quad
\varepsilon=B_0+r_1B_1,\quad
d=\frac{\varepsilon}{\sqrt{1-r_1^2}a_\rho},
\]
\[
J=B_1+e^{d_0}d,\quad \delta_1=\sqrt{1+r_1^2}J.
\]
The equation and \(|\sin\xi|\ge a_\rho|\xi|\) yield \(|w_j-w_{0,j}|\le d\). Hence
\[
\left|\frac{F_1(\eta,w_j)}{e^{i\eta}[-\sigma_j/\sqrt{1+v^2}]}-1\right|\le\delta_1.
\tag{13}
\]
Require \(\delta_1<1/2\), and define \(b=-\log(1-\delta_1)\). The ratio has the canonical logarithm \(\ell\) with \(|\ell|\le b\), holomorphic in \(v\). On \(|v|\le r\),
\[
|\ell_v|\le b/(r_1-r).
\]
For its heat derivative put
\[
E_{20}=B_2+B_0,\quad E_{31}=B_3+B_1,\quad f_*=c_0-B_1,
\]
\[
d_*=(1-r_1^2)f_*-r_1E_{20}>0,\quad
N=E_{20}+r_1E_{31},
\]
\[
D_*=\frac{E_{31}}{f_*}
 +\left(r_1+\frac{E_{20}}{f_*}\right)\frac{N}{d_*}.
\tag{14}
\]
Then \(|\ell_\eta|\le D_*\). To check it, differentiate (10):
\[
(w_j)_\eta=i\frac{F_2-vF_3}{F_1-vF_2},\qquad
F_2-vF_3=(F_2+F_0)-v(F_3+F_1).
\]
The numerator is bounded by \(N\); since \(F_0=vF_1\), the denominator is bounded below by \(d_*\). Finally
\[
\partial_\eta\log F_1-i
=-i\frac{F_3+F_1}{F_1}+\frac{F_2}{F_1}(w_j)_\eta.
\]
This proves (14).

Let \(n=G/|G|\) on (11), and take the actual physical reference
\[
n_0(\eta,v)=e^{i\eta}
\frac{-\sigma_j|\sqrt{1+v^2}|}{\sqrt{1+v^2}}
\frac{(v/L,1)}{\sqrt{1+|v|^2/L^2}}.
\tag{15}
\]
Exactly \(n=e^{i\Im\ell}n_0\). If \(v=x+iy\), then
\[
|n-n_0|\le b,\qquad
|\partial_\eta n-\partial_\eta n_0|\le D_*+b,
\]
\[
|\partial_xn-\partial_xn_0|,
|\partial_yn-\partial_yn_0|
\le\frac b{r_1-r}+b\left(\frac1L+\frac r{1-r^2}\right).
\tag{16}
\]
All right sides are \(O_{K,S}(1/(L\sqrt\kappa))\). The reference spatial derivative bound uses the phase derivative \(-v/(1+v^2)\) and the physical vector \((v/L,1)\). These are the three first tangential derivatives needed by \(\mathcal A\wedge d\mathcal A\). Formula (12) records physical measure; (16) is a bound in the stated cap coordinates, not a claim that physical \(s\)-derivatives vanish.

## 5. Exact evaluated reference flux and complete remainder

Use
\[
\mathcal A=\frac{\Im(G^*dG)}{|G|^2},\qquad
\mathcal C=\frac{\mathcal A\wedge d\mathcal A}{4\pi^2}.
\]
On (11), let \(\phi=\arg H_z(\tau,z)\) be its continuous lift; it exists because the parameter prism is contractible and \(H_z\ne0\). With \(q=v/L\),
\[
\mathcal A=d\phi+\frac{\Im(\bar q\,dq)}{1+|q|^2},\qquad
d\mathcal A=\frac{2/L^2}{(1+|v|^2/L^2)^2}\,dx\wedge dy.
\tag{17}
\]
For each fixed \(\eta\), \(\phi_\eta\) is harmonic in \(v\): the scalar \(H_z(\eta,w_j(\eta,v)/L)\) is nonvanishing and holomorphic there. The radial weighted mean-value identity in (17) therefore proves the **exact** cap formula
\[
\boxed{I_{T,j}=\int_{M_{T,j}}\mathcal C
=\frac{\gamma_T}{2\pi}\,[\phi(S_T,0)-\phi(-S_T,0)],
\quad \gamma_T=\frac{\epsilon_T^2}{1+\epsilon_T^2}
=\frac{r_T^2}{L^2+r_T^2}.}
\tag{18}
\]
This accounts for the physical measure, every derivative in the three-form, and the complete disk integration. The reference (15) has \(\partial_\eta\phi_0=1\), so
\[
\boxed{I^{\rm ref}_{T,j}=\gamma_T S_T/\pi.}
\tag{19}
\]
Its flux is positive and is not set to zero.

At \(v=0\), \(F_0=0\). Set
\[
f=2-\cosh\rho-B_1>0,\qquad
\boxed{D=\frac{B_3+B_1}{f}+\frac{(B_2+B_0)^2}{f^2}.}
\tag{20}
\]
The exact scaled heat equation gives
\[
\frac d{d\eta}\log F_1(\eta,w_j(\eta,0))-i
=-i\frac{F_3+F_1}{F_1}+i\left(\frac{F_2}{F_1}\right)^2.
\]
Here \(|F_2|=|F_2+F_0|\le B_2+B_0\), \(|F_3+F_1|\le B_3+B_1\), and \(|F_1|\ge f\). Consequently
\[
|\phi_\eta(\eta,0)-1|\le D,
\]
\[
\boxed{\left|I_{T,j}-\frac{\gamma_T S_T}{\pi}\right|
\le\frac{\gamma_T}{\pi}\min\{S_TD,b\},
\qquad D=O_{K,S}\left(\frac1{L\sqrt\kappa}\right).}
\tag{21}
\]
The derivative estimate proves the first allowance gamma_T S_T D/pi. Independently (13) supplies one continuous near-one logarithm over the full cap, so the phase difference differs from 2S_T by Im ell(S_T,0)-Im ell(-S_T,0), of modulus at most 2b. This proves the second allowance gamma_T b/pi without losing phase windings. Taking their minimum is a coupled endpoint bound. It is a complete integrated allowance, retaining the relative derivative estimate even when \(S_T\) and \(r_T\) become arbitrarily small. It gives an explicit upper and lower endpoint. In particular the cap is positive for \(D<1\), while \(I_{T,j}=O(S_T r_T^2/L^2)\to0\) for bounded \(S_T,r_T\). For finitely many disjoint selected root caps, add (18)–(21); no growing population is covered.

Every finite condition (2), (9), (13), (14), (20) eventually holds, since the \(B_j\) tend to zero and all limiting denominators are strictly positive. A definite finite terminal choice is the least integer T>=1 with the large stationary point defined and satisfying all the displayed explicit conditions for the selected K,S; eventual validity proves that this set is nonempty. Evaluating that integer would require certified finite comparisons, which are not supplied here. This is a definable finite choice, not a certified numerical onset or a uniform-in-height onset. The source normalization lower bound is N_T; the phase remainder in (20) is D=D(T), a different quantity.

## 6. Fixed bounded imaginary-time width: an actual nonzero theta cap

The finite bounds (3), (5), (9), (13), (14), (20), (21) remain valid for each finite S without a bounded-S hypothesis. Fix K and a physical width Y_max>0, and use
\[
S=S(T)=Y_{\max}L^2.
\]
The explicit formula (5), rather than an invocation of its fixed-S big-O statement, gives
\[
B_j=O_{K,Y_{\max}}(L/\sqrt\kappa),\qquad j=0,1,2,3.
\tag{22}
\]
Indeed the growing term is
\[
S(2W_1/L+W_2/L^2)=Y_{\max}(2LW_1+W_2)
=O_{Y_{\max}}(L/\sqrt\kappa).
\]
It tends to zero, so every inverse-cap test eventually holds uniformly for |s|<=Y_max. The normalized C1 bounds (16) remain valid with their displayed finite allowances, now of order L/sqrt(kappa) in eta,v coordinates. The physical s derivative still includes the factor L^2; no derivative rescaling is hidden.

For any 0<Y_T<=Y_max and 0<r_T<=r=1/4, put S_T=L^2Y_T and epsilon_T=r_T/L. Formula (21) now reads
\[
\boxed{\left|I_{T,j}-\frac{r_T^2Y_T}{\pi}
                   \frac{L^2}{L^2+r_T^2}\right|
\le \frac{r_T^2}{\pi(L^2+r_T^2)}\min\{L^2Y_TD(T),b(T)\},
\qquad D(T),b(T)=O_{K,Y_{\max}}(L/\sqrt\kappa).}
\tag{23}
\]
This bound is uniform also when Y_T or r_T shrinks. The second endpoint allowance gives an absolute cap error O_{K,Y_max}(1/(L sqrt(kappa))), retaining the paired common phase. In particular, for fixed 0<Y<=Y_max and 0<r_0<=1/4,
\[
\boxed{I_{T,j}\longrightarrow r_0^2Y/\pi>0,
\quad I_{T,j}-r_0^2Y/\pi
=O_{K,Y_{\max}}(L^{-2}+1/(L\sqrt\kappa)).}
\tag{24}
\]
This is an **actual canonical theta cap**, with its full common phase and physical jet, not merely the nonzero reference cosine control. The phase rate of order L^2 compensates for the spatial projective curvature mass of order L^(-2).

It proves terminal-cap regularity on a fixed bounded imaginary-time strip near each fixed late root rank. By itself it does not continue that strip back to the candidate. The [companion geometry, Section 7][geometry] combines this late estimate with compact-prefix continuation to prove a fixed positive width on growing finite intervals, with the constant-on-each-tube radius r_0/L_T shrinking as T grows. Its full joining and imaginary-time closures remain payable and are evaluated in [the closure note][closure]. Neither a growing Y_max nor a growing root population is covered.

## 7. Scope, controls and the unpaid complete boundary

The cap is on the zero-following projective disk \(|H/H_z|\le\epsilon_T\) where the chart was proved regular, with \(\epsilon_T\le1/(4L)\). The source theorem does not estimate a cap containing a critical point of the reference cosine. It does not cover a fixed spatial domain, a fixed physical projective radius, or a growing number of zeros. Section 6 covers a fixed bounded imaginary-time width at the terminal cap; the companion geometry proves the matching fixed-width continuation by an additional compact-prefix argument.

The nonzero cosine diagnostic remains visible. For the reference physical jet \(e^{i\eta}(\cos w,-L\sin w)\) on a *fixed spatial* disk with boundary avoiding critical points and containing exactly one zero of \(\sin w\), the curvature is
\[
\frac{2L^2}{(|\cos w|^2+L^2|\sin w|^2)^2}\,d\Re w\wedge d\Im w.
\]
Its mass tends to \(2\pi\), and the cap reference tends to \(S/\pi\), unlike (19). Near the critical point put \(w=k\pi+\zeta/L\) to obtain the integrable density \(2(1+|\zeta|^2)^{-2}\); away from critical points the density tends uniformly to zero on fixed compact sets. This is a reference-profile diagnostic, not an unproved uniform canonical theorem on another geometry.

The ordinary quadratic double and projective shell keep charge one and a surviving closure, respectively. They do not satisfy the complete moving theta saddle (1)–(4). The exact cosine has an atomic source and does not satisfy that saddle; more fundamentally, (19) explicitly retains its common-phase flux, so no inference from clock roots to a zero cap was made. Euler-factor controls change (1). Weighted-square/finite-prime controls lack unchanged full theta coefficients and the required full reflection. Reflected/positive-primitive controls lack the canonical square series. Close positive endpoint controls can preserve the leading tail and can satisfy analogous estimates for their own sources; this generic late-cap mechanism is consequently **not an arithmetic discriminator**, and no exclusion of those controls is asserted. Their ordinary Dirichlet arithmetic fails, but that missing premise is not used by (18)–(21).

For an actual candidate event, the connector, initial boundary, imaginary-time faces and joining closure must still be supplied. If those pieces give \(Q=I_T-I_-+S_T^{\rm side}\), (21) bounds only its explicitly named terminal caps. Making them small does not make the complete right-hand side small. The local linking charge and any additional positive event accounting remain unchanged. A finite continuation theorem may choose \(Y_T\le S/L^2\), \(\epsilon_T\le r/L\); its shrinking choices are already allowed in (21), and any choices bounded by a fixed Y_max are allowed in (23), but all its other boundary terms remain payable. No PCC bridge is needed for this bounded direct source result.


[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[heat-geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[source]: ../../02_theta_source_constraints/README.md
[geometry]: 01_FINITE_PROJECTIVE_TUBES_AND_COMPLETE_ATTACHMENTS_20261022.md
[closure]: 04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
[review]: ../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md
