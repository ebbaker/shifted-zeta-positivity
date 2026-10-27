# Gaussian source deformation and complete collision-index transport

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Conversation: **Begin radial theta collision study**, Investigation05 chat0001, thread 01a17e9c-bfd5-7782-a76f-b2a2eaa82417.

**Status: first bounded RTC-05 return; exact source/degree transport and a scoped obstruction proved in-note, with same-assistant checks only.** A positive Gaussian relaxation takes the complete theta source to an explicit source with a strictly positive transform. However, the relaxation is an exact symmetry of the physical heat equation before its limiting endpoint. Every hypothetical collision retains its multiplicity and negative physical index, follows an explicit orbit, and exits a fixed region through a time or frequency boundary. The terminal zero degree therefore does not give the original degree without the crossing terms.

An exact positive-source control demonstrates the failure on a fixed rectangle: the boundary degree changes from \(-1\) to \(0\) through a double zero on the upper time face, while both frequency walls stay strictly positive. The general transport covers arbitrary finite multiplicity; the explicit control has multiplicity two. **No canonical collision is excluded, no new canonical region is certified, and no Newman bound or endpoint simplicity theorem is obtained.**

This continues [Note03][circle] and the [RTC register][progress]. Consult the [result index][results], [local degree and walls][geometry], [theta arithmetic][arithmetic], [collision controls][controls] and [avoid index][avoid], especially [target restatements][a01], [coordinate lifts][a03], [scoped conclusions][a07] and [complete boundary payments][a12]. The inherited local index and wall-flux theorems are used at their original scope. Gaussian heat symmetries themselves are classical; no novelty claim is made.

## 1. Selected deformation and declared region

The proposed mechanism is natural: continuously smooth and contract the positive even complete source to a Gaussian, whose heat transform is positive, then attempt to transport zero boundary degree back to theta. We test that implication analytically on

\[
D=(b,c)\times(0,R),\qquad 0<b<c<\tfrac12,\quad 0<R<\infty,
\tag{1}
\]

with physical orientation \(dt\wedge da\). A boundary degree is asserted only when the physical first jet is nonzero on the entire boundary. The inequalities in (1) give a convenient strict monotonicity range for the deformation's event orbits; they are not a newly covered theta domain. The basic formulas hold on the larger slab \(0<t<1\).

Use the complete even theta source \(\Phi\), with the normalization of [Note01][initial]:

\[
H(t,a)=\int_0^\infty e^{tu^2}\Phi(u)\cos(au)\,du,\qquad
H_t=-H_{aa},\qquad Z=\int_{\mathbb R}\Phi(u)\,du=2H(0,0)>0.
\tag{2}
\]

For \(0<\rho<1\), define

\[
\sigma_\rho=(1-\rho^2)/4,\quad
G_\sigma(u)=\frac{e^{-u^2/(4\sigma)}}{\sqrt{4\pi\sigma}},\quad
\Phi_\rho(u)=\int_{\mathbb R}G_{\sigma_\rho}(u-\rho v)\Phi(v)\,dv.
\tag{3}
\]

Set \(\Phi_1=\Phi\) by continuity and

\[
\Phi_0(u)=Z\pi^{-1/2}e^{-u^2}.
\tag{4}
\]

This preserves strict positivity, evenness and total source mass \(Z\). The complete reflected source is assembled **before** the convolution; no separate full-line theta mode integral is used. The intermediate sources differ from the canonical theta source. Their normalized square expansion and double-exponential tails are not claimed to persist.

The unit-mass Gaussian convention follows from the elementary Gaussian integral; the limited primary checks are recorded in the [reference annotation][refs]. All transformation and degree statements below are derived here, not imported from a Gaussian positivity theorem.

For each fixed \(0\le\rho<1\), the source has Gaussian quadratic tail rate

\[
\lim_{|u|\to\infty}\frac{\log\Phi_\rho(u)}{u^2}
=-\frac1{4\sigma_\rho}=-\frac1{1-\rho^2}.
\tag{5}
\]

For the upper bound, use
\((u-\rho v)^2\ge(1-\varepsilon)u^2-(\varepsilon^{-1}-1)\rho^2v^2\)
and theta's integrability against every Gaussian multiplier. For the lower bound integrate over a fixed interval on which \(\Phi>0\). Let \(\varepsilon\downarrow0\). At \(\rho=0\), (5) is immediate. Derivatives have the same available Gaussian domination after polynomial factors.

Thus the absolutely convergent heat integral

\[
F_\rho(t,a)=\int_0^\infty e^{tu^2}\Phi_\rho(u)\cos(au)\,du
\tag{6}
\]

is available for \(\operatorname{Re}t<1/(1-\rho^2)\), with entire dependence on \(a\); at \(\rho=1\) the original all-finite-time domain returns. The common real slab \(t<1\) suffices below. The final Gaussian has a convergence boundary at \(t=1\). This changed-source family is not silently treated as a canonical all-time Newman family.

## 2. The exact observation map and a paid positive endpoint

Write

\[
d=1-\rho^2,\quad \Delta=1-dt,\quad
T=\frac{\rho^2t}{\Delta},\quad A=\frac{\rho a}{\Delta},\quad
W=\Delta^{-1/2}\exp\!\left(-\frac{d a^2}{4\Delta}\right).
\tag{7}
\]

For \(0<\rho\le1,\ 0<t<1,\ a\in\mathbb R\), Gaussian integration gives

\[
\boxed{F_\rho(t,a)=W(t,a,\rho)H(T,A).}
\tag{8}
\]

Indeed, integrate the full-line kernel against \(e^{tu^2+iau}\):

\[
\int_{\mathbb R}G_{\sigma_\rho}(u-\rho v)e^{tu^2+iau}\,du
=\Delta^{-1/2}
\exp\!\left(-\frac{\sigma_\rho a^2}{\Delta}
+\frac{t\rho^2v^2}{\Delta}+\frac{i\rho av}{\Delta}\right).
\tag{9}
\]

The real full-line transform is twice (6). Absolute convergence, using the complete \(\Phi\) and \(\Delta>0\), justifies Fubini. This pays both infinite source endpoints. On a half-line integration-by-parts derivation, evenness also gives \(\Phi_\rho'(0)=0\), while the cosine derivative and the drift factor \(u\) vanish at zero; there is no omitted lower flux.

Uniform finite moment domination is also available: for \(c<c'<1\),
\(F_\rho(c',0)\le(1-c')^{-1/2}H(c',0)\) for all \(0\le\rho\le1\), since the transformed time is at most \(c'\). The gap \(c'-c\) absorbs any fixed power of \(u\). Together with (8), this pays the compact-parameter differentiations used below, including the endpoint \(\rho=0\).

At \(\rho=0\), the exact endpoint is

\[
F_0(t,a)=H(0,0)(1-t)^{-1/2}
\exp\!\left[-\frac{a^2}{4(1-t)}\right]>0,\qquad t<1.
\tag{10}
\]

The positive anchor can be reached at finite deformation, with an explicit source-only allowance. Let

\[
M_2(c)=\int_0^\infty u^2e^{cu^2}\Phi(u)\,du,\qquad
\rho_*=\min\!\left\{\frac12,\frac{1-c}{R}
\sqrt{\frac{H(0,0)}{M_2(c)}}\right\}>0.
\tag{11}
\]

For \(0<\rho\le\rho_*\) and \((t,a)\in\overline D\), \(0\le T\le c\),
\(|A|\le\rho R/(1-c)\), and \(1-\cos(Au)\le A^2u^2/2\). Hence

\[
H(T,A)\ge H(0,0)-\frac{A^2}2M_2(c)\ge\frac12H(0,0),
\]
\[
\boxed{F_\rho(t,a)\ge
\frac12H(0,0)\exp\!\left[-\frac{R^2}{4(1-c)}\right]>0.}
\tag{12}
\]

The endpoint degree is therefore genuinely zero on this fixed rectangle. This is an analytic bound in complete positive source moments, not a numerical enclosure of those moments or a bound at \(\rho=1\).

## 3. Auxiliary evolution, physical heat, and compatibility

Put \(\rho=e^{-s}\), \(s\ge0\), and write \(F_s=F_{e^{-s}}\). The source kernel directly satisfies

\[
\partial_s\Phi_s=\tfrac12\partial_u^2\Phi_s+\partial_u(u\Phi_s).
\tag{13}
\]

This is a positive contraction-and-diffusion evolution in the auxiliary source parameter. It is distinct from physical heat time \(t\).

For \(f=e^{tu^2+iau}\),

\[
\tfrac12 f_{uu}-uf_u
=\left[t-\frac{a^2}2+2t(t-1)u^2+i(2t-1)au\right]f.
\]

Integrating with both source ends paid gives the exact observation equation

\[
\boxed{\partial_sF_s=XF_s,\quad
X=2t(t-1)\partial_t+(2t-1)a\partial_a+t-a^2/2.}
\tag{14}
\]

Every fixed \(s\) still satisfies \(BF_s=0\), where \(B=\partial_t+\partial_a^2\). Their operator compatibility is

\[
\boxed{[B,X]=(4t-2)B.}
\tag{15}
\]

For example, the first-order \(a\)-terms \(2a\partial_a\) and
\(-2a\partial_a\) cancel; the scalar terms \(1\) and \(-1\) cancel. This is an on-solution compatibility, not a zero commutator on arbitrary functions.

Eliminating physical \(F_t\) gives

\[
\partial_sF_s=2t(1-t)F_{aa}+(2t-1)aF_a+(t-a^2/2)F.
\tag{16}
\]

At fixed \(0<t<1\), this is forward parabolic in \(a\). It permits real zero pairs to disappear as \(s\) increases; it is not a proof that they were absent initially. At an ordinary double zero, its \((s,a)\) jet determinant is \(+2t(1-t)F_{aa}^2\), while the physical \((t,a)\) determinant is \(-F_{aa}^2\). These are different oriented parameter planes.

## 4. Multiplicity and the exact degree transport

From (8),

\[
\binom{F_\rho}{(F_\rho)_a}
=W
\begin{pmatrix}
1&0\\
-da/(2\Delta)&\rho/\Delta
\end{pmatrix}
\binom{H}{H_A}(T,A).
\tag{17}
\]

Both target diagonal entries are positive. Moreover

\[
\det\frac{\partial(T,A)}{\partial(t,a)}=\frac{\rho^3}{\Delta^3}>0.
\tag{18}
\]

Thus physical collision points correspond exactly for \(\rho>0\), spatial multiplicities are preserved, and their inherited index remains
\(-\lfloor m/2\rfloor\). This is not restricted to doubles.

For the fixed rectangle (1), the transformed physical region is

\[
\Omega_\rho=\left\{(T,A):
T_b(\rho)<T<T_c(\rho),\
0<A<\frac R\rho[\rho^2+(1-\rho^2)T]\right\},
\]
\[
T_v(\rho)=\frac{\rho^2v}{1-(1-\rho^2)v},\qquad v=b,c.
\tag{19}
\]

If the boundary jet is nonzero, then

\[
\boxed{\operatorname{wind}_{\partial D}(F_\rho+i(F_\rho)_a)
=\operatorname{wind}_{\partial\Omega_\rho}(H+iH_A).}
\tag{20}
\]

The point-dependent target matrix in (17) introduces no extra winding: its lower-triangular positive-diagonal form contracts to the identity through matrices of that same form on the whole region. The coordinate map is an orientation-preserving diffeomorphism. These two facts prove (20), including the parameter-dependent matrix, rather than assuming that any variable positive-determinant matrix preserves winding.

For \(c<1/2\), \(T\le t\) and \(\rho/\Delta\le1\), so every \(\Omega_\rho\) lies in \((0,c)\times(0,R)\). As \(\rho\downarrow0\), its time coordinates are \(O(\rho^2)\) and its frequency coordinates are \(O(\rho)\). It shrinks toward \((0,0)\), where \(H>0\). Equation (20) is an exact reduction to the existing physical degree on a moving domain. It supplies no new degree constraint.

## 5. Collision orbits and all four physical faces

Take any hypothetical canonical event \((T,A)\), \(0<T<1,\ A>0\), of any finite multiplicity. Its unique event in the deformed family is

\[
q_\rho=T+(1-T)\rho^2,\qquad
\boxed{t_\rho=\frac T{q_\rho},\quad a_\rho=\frac{A\rho}{q_\rho}.}
\tag{21}
\]

With \(s=-\log\rho\), direct differentiation yields

\[
\dot t=2t(1-t),\qquad \dot a=(1-2t)a,\qquad
\boxed{\frac{a_\rho^2}{t_\rho(1-t_\rho)}
=\frac{A^2}{T(1-T)}.}
\tag{22}
\]

Event orbits lie on the displayed elliptical arcs. Before \(t=1/2\), both \(t\) and \(a\) increase. At the time face \(t=v>T\),

\[
\rho_v^2=\frac{T(1-v)}{v(1-T)},\qquad
a_v=A\sqrt{\frac{v(1-v)}{T(1-T)}}.
\tag{23}
\]

For an event initially inside \(D\), it must leave by \(t=c\) or \(a=R\) at a finite \(s\). If \(a_c<R\), the exit is through the upper time face. If \(a_c>R\), it first crosses the right frequency wall. Equality is a corner crossing. A right-wall crossing on the increasing branch occurs at

\[
t_R=\frac{1-\sqrt{1-4R^2T(1-T)/A^2}}2,
\tag{24}
\]

when that value lies between the initial time and \(c\). The condition \(a_c>R\) ensures the relevant real branch exists.

Here is the complete deformation accounting for \(D\):

| Face | Event flux as \(s\) increases |
| --- | --- |
| \(a=0\) | No event: \(F_\rho(t,0)>0\) |
| \(t=b\) | Events from original times below \(b\) can enter; \(\dot t>0\) |
| \(t=c\) | Events can leave; \(\dot t>0\) |
| \(a=R\) | Events can leave in the chosen \(c<1/2\) region; \(\dot a>0\) |

Let \(K_s(D)\) be the sum of \(\lfloor m/2\rfloor\) over interior events, and let \(I_b,O_c,O_R\) be the corresponding weighted entry and exit counts over a finite deformation interval. At regular parameter endpoints and with no corner crossings,

\[
\boxed{K_{s_1}(D)=K_{s_0}(D)+I_b-O_c-O_R.}
\tag{25}
\]

Equivalently, each lower-time entry decreases boundary winding by its weight; each upper-time or right-wall exit increases it by that weight. All interior event indices have the same negative sign. Corners can be avoided by an arbitrarily small generic boundary adjustment, or counted once by the signed change of the interior indicator; they must not be counted independently on both incident faces. The strict domain \(c<1/2\) removes wall tangencies for these orbits. On an enlarged domain crossing \(t=1/2\), the signed indicator rule retains tangential contacts, whose net crossing is zero, and right-wall entries as well as exits.

The sums are finite on any compact deformation interval: (19) stays in a fixed compact analytic region and inherited heat collisions are isolated. The finite positive anchor (12) suffices; no infinite-parameter interchange is needed to obtain a zero final degree. Taking \(s_0=0\) and any \(s_1\ge-\log\rho_*\) gives

\[
K_0(D)=O_c+O_R-I_b.
\tag{26}
\]

This is the paid conservation identity, **not** a new criterion supported by evidence that its right side vanishes. A positive terminal source does not set these boundary fluxes to zero.

For comparison, at each fixed \(s\) the inherited physical root-count formula still reads

\[
\operatorname{wind}_{\partial D}(F_s+i(F_s)_a)
=\frac{N_b-N_c-Q_0+Q_R}{2}.
\tag{27}
\]

Here \(Q_R\) is the signed flux of ordinary simple real roots through the right wall as physical \(t\) varies, and \(Q_0=0\). It is distinct from the deformation's collision flux \(O_R\). Formula (25) does not discard \(Q_R\) in (27); it follows the joint-zero boundary crossings that change the degree.

## 6. The global cap and radial normalization are not free boundaries

On the whole open slab \(0<t<1,\ a>0\), the map (7) is a diffeomorphism for every \(\rho>0\). An original event with fixed \(0<T<1,A>0\) satisfies

\[
(t_\rho,a_\rho)\longrightarrow(1,0)\quad(\rho\downarrow0),
\qquad
1-t_\rho=\frac{(1-T)\rho^2}{q_\rho}.
\tag{28}
\]

The limiting Gaussian has no ordinary heat transform at this point. For each \(\rho>0\), (9) also applies at \(t=1\), since \(\Delta=\rho^2>0\). It gives

\[
F_\rho(1,0)=\rho^{-1}H(1,0)\longrightarrow\infty.
\tag{29}
\]

Consequently the source homotopy does not extend as a uniformly finite, nonzero boundary homotopy over this cap. An exhaustion or moving-wall version must retain the cap contribution. If the frequency walls are chosen along the invariant \(a/\sqrt{t(1-t)}\), event side crossings disappear, but the upper-time exits persist with their full weights. This is a scoped boundary failure of the chosen Gaussian deformation, not a statement about all global continuations.

All positive even intermediate sources have the elementary radial Kelvin realization. Put \(u=\log r/2\) and

\[
Q_{\rho,t}(r)=4r^{-5/2}e^{tu^2}\Phi_\rho(u),\qquad
M_{\rho,t}=\int_0^\infty r^2Q_{\rho,t}(r)\,dr=16F_\rho(t,i).
\tag{30}
\]

On the stated domain, (8) gives the explicit positive mass

\[
M_{\rho,t}=16\Delta^{-1/2}e^{\sigma_\rho/\Delta}
H\!\left(T,\frac{i\rho}{\Delta}\right).
\tag{31}
\]

The same tail-selected potential as Note01 is

\[
\mathcal T_{\rho,t}(r)
=M_{\rho,t}+\int_r^\infty(v^2/r-v)Q_{\rho,t}(v)\,dv,
\]
\[
\mathcal T_{\rho,t}\sim M_{\rho,t}/r\ (r\downarrow0),\quad
\mathcal T_{\rho,t}\to M_{\rho,t}\ (r\to\infty),\quad
\Delta_{\mathbb R^3}\mathcal T_{\rho,t}
=Q_{\rho,t}-4\pi M_{\rho,t}\delta_0.
\tag{32}
\]

Evenness yields weight-five inversion for \(Q_{\rho,t}\). The Gaussian domination for \(t<1\) pays both radial tails. Source mass \(Z\) is conserved by (3), but the radial charge \(M_{\rho,t}\) is not. At the limiting source it equals

\[
M_{0,t}=16H(0,0)(1-t)^{-1/2}e^{1/[4(1-t)]}.
\tag{33}
\]

No unit origin charge, fixed infinity constant, or boundary cancellation is assumed along the deformation.

## 7. Exact positive-source control: a top-face crossing changes the degree

Use Note01's Gaussian-polynomial control with event time \(T_*=1/4\):

\[
\Phi_*(u)=(64u^4+6)e^{-17u^2/4}>0.
\tag{34}
\]

It is even and its heat integral converges for \(t<17/4\). Let \(\gamma=17/4-t>0\). Direct Gaussian moments give

\[
H_*(t,a)=\frac{\sqrt\pi}{2\sqrt\gamma}e^{-a^2/(4\gamma)}
\frac4{\gamma^4}\mathcal P_\gamma(a^2),
\quad
\mathcal P_\gamma(y)=y^2-12\gamma y+\frac32\gamma^4+12\gamma^2.
\tag{35}
\]

At a nonzero common zero, \(\partial_y\mathcal P_\gamma=0\) gives \(y=6\gamma\), and
\(\mathcal P_\gamma(6\gamma)=\tfrac32\gamma^2(\gamma^2-16)\).
Thus the only positive-frequency collision in this real time domain is

\[
(T_*,A_*)=(1/4,2\sqrt6),
\tag{36}
\]

and it is double. Its physical index is \(-1\).

Apply the same source deformation (3) to this control. Formula (8) is valid on the rectangle

\[
D_*=(1/8,3/8)\times(0,6)
\tag{37}
\]

because the transformed \(T\) lies below \(3/8\), inside its own heat domain. The event orbit is

\[
t_\rho=\frac1{1+3\rho^2},\qquad
a_\rho=\frac{8\sqrt6\,\rho}{1+3\rho^2}.
\tag{38}
\]

It exits through the upper time face at

\[
\boxed{\rho^2=5/9,\quad t_\rho=3/8,\quad a_\rho^2=30<36.}
\tag{39}
\]

This crossing is transverse. There is no lower-time entry, since the sole original event is above \(1/8\).

The frequency walls can be paid uniformly for the **entire** deformation. The left wall is positive. A real positive root of \(H_*(T,A)\), for \(T\le3/8\), requires \(T\ge1/4\), hence \(31/8\le\gamma\le4\). In this interval every positive root satisfies \(A^2<28\). To see the upper bound, the quadratic's vertex is \(6\gamma\le24<28\), and

\[
\mathcal P_{31/8}(28)=3203/8192>0,\qquad
\frac d{d\gamma}\mathcal P_\gamma(28)
=6\gamma^3+24\gamma-336\ge27165/256>0.
\tag{40}
\]

The map (7) also gives the exact identity
\(a^2/[t(1-t)]=A^2/[T(1-T)]\) at every point. Therefore, at any real root of the deformed control with \(t\in[1/8,3/8]\),

\[
a^2<28\,\frac{(3/8)(5/8)}{(1/4)(3/4)}=35<36.
\tag{41}
\]

Hence the entire right wall \(a=6\) has no real root; its sign is positive by continuity from \(\rho=0\). The ordinary physical root flux \(Q_R\) in (27) is zero for every \(\rho\).

The lower time face has no real roots because its transformed time is below \(1/4\). On the upper time face there are two positive simple roots if \(\rho^2>5/9\), none if \(\rho^2<5/9\), and a double at equality. Equations (27) and (39) therefore yield the complete exact result

\[
\boxed{
\operatorname{wind}_{\partial D_*}(F_{\rho,*}+i\partial_aF_{\rho,*})
=\begin{cases}-1,&5/9<\rho^2\le1,\\0,&0\le\rho^2<5/9.\end{cases}}
\tag{42}
\]

At equality the boundary jet vanishes and its winding is not defined. In particular, \(\rho=1\) has degree \(-1\), while \(\rho=1/2\) has degree zero; at the latter value \(T_c=3/23<1/4\), so the whole rectangle's field is positive. The missing degree is exactly the upper-time crossing, not a frequency-wall loss or a rounding effect.

This is an analytic control with exact rational checks. It is not a canonical theta event or a global Newman threshold control. Its complete source, rather than theta tails substituted into another function, is used throughout.

## 8. Screening, result classification and continuation

The argument (3)–(28) works for any nonzero positive even source with the required Gaussian moments on the declared domain. The original canonical theta source satisfies the stronger all-Gaussian-moment condition. The exact control (34) requires only its stated finite domain, which covers every use in §7.

| Control family | Relevant screen |
| --- | --- |
| Gaussian-polynomial control | Shares the positive deformation, evenness, radial inversion, physical heat, positive terminal transform and complete boundary accounting; lacks canonical square arithmetic and canonical tails. It realizes the top-face degree change exactly |
| Weighted-square / finite-tail controls | Their certified local events remain local; full reflected source and all-real thresholds are not inferred from finite endpoint conditions. No whole-line Gaussian convolution of an uncompleted finite source is asserted here |
| Reflected smooth / positive-primitive controls | When their actual source moments meet the declared domain, the same Gaussian identity applies; unchanged square arithmetic fails |
| Finite-prime square controls | Selected identities do not supply the full normalized reflection required to identify theta; no global heat-domain extension is imported |
| Euler-factor threshold controls | Positive even source deformation applies on its convergence domain; unchanged conductor/source is absent. Their threshold status is not transferred to the Gaussian-deformed family |
| Finite-profile atomic controls | Formula (9) also applies to a finite positive even measure; the original theta smoothness, arithmetic and eventual-simplicity premises are absent |

The non-Gaussian rows are premise screens, not newly evaluated control certificates. No single missing premise is assigned to all families.

Within the polynomial-growth weighted-square class, [full reflection plus the normalized primitive endpoint][rigidity] already forces the original theta coefficients. That inherited rigidity does not provide a nontrivial interpolation to a Gaussian inside the same class. A changed-source homotopy is legitimate, but its departure from the class and all boundary crossings must be paid.

**Stop the tested inference:** a positive Gaussian endpoint, positivity/evenness along the source flow, and the inherited negative physical indices do not force zero original degree. Here the exact transformation preserves all interior events for positive \(\rho\), and the full boundary crossing terms explain their disappearance from a fixed box. This closes this Gaussian contraction-and-smoothing inference only. It does not rule out a non-Gaussian arithmetic deformation, an independent canonical boundary estimate, or a different global current.

RTC-05 now has a first bounded analytical return, with a complete transport formula, a finite positive anchor, an all-multiplicity orbit law and an exact counterexample to the unpaid homotopy step. Its central canonical degree constraint remains open. The next attempt must specify information beyond this heat symmetry: an actual signed theta estimate on the complete time/frequency boundary, or a concrete non-Gaussian source construction with its full residual. No new equivalent degree target is counted as progress.

The [exact checker][checker] verifies the rational transformation/compatibility identities and the control's complete face accounting. The [record][record] distinguishes those checks from the analytical convergence and degree proofs. The [self-assessment][review] is by the same assistant. No manuscript, snapshot, numerical theta pilot or investigation closeout was created.

[initial]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[circle]: 03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[review]: ../reviews/03_GAUSSIAN_DEFORMATION_AND_INDEX_SELF_ASSESSMENT_20261027.md
[checker]: ../numerics/03_check_gaussian_index_transport_20261027.py
[record]: ../numerics/03_GAUSSIAN_INDEX_TRANSPORT_CHECKS_20261027.json
[refs]: ../references/02_GAUSSIAN_NORMALIZATION_AND_INHERITED_INDEX_INPUTS_20261027.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[rigidity]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md
