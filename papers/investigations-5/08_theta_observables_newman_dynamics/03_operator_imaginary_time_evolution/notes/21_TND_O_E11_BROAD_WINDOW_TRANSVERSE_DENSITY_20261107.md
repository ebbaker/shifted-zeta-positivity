# E11 r2: convex broad-window transport and full-family transverse density

7 November 2026 UTC. Prepared for **Edward Baker** with substantial OpenAI
Codex assistance. Observable executor dispatch selection:
**gpt-6.1-sol, ultra**. This records tool-selected configuration, not
independent verification of the serving backend.

**Proved in-note:** broad-window transport for every even convex test has
an upper cost independent of its derivatives. A cosh test propagates
canonical time-zero density to an exponential off-axis bound throughout
\(0\le\lambda\le1/2\), uniformly down to time zero. The dyadic second
moment and local averaged moments of every integer order follow. These
are density/moment estimates, not realness, simplicity or single-event
exclusion theorems. No novelty claim is made.

[Request25 r2](../research-progress/handoffs/25_TND_O_E11_R2_CONVEX_DENSITY_REQUEST_20261107.md)
and [inputs25 r2](../research-progress/handoffs/25_TND_O_E11_R2_CONVEX_DENSITY_INPUTS_20261107.json)
fix this package, following [Decision12](../brainstorm/notes/12_TND_O_B05_R3_CONVEX_DENSITY_TRANSPORT_DECISION_20261107.md)
and [Decision11](../brainstorm/notes/11_TND_O_B05_R2_BROAD_WINDOW_TRANSPORT_DECISION_20261107.md).
The narrower request25 r1 was never dispatched or executed. All eleven
input sizes and hashes matched at entry. The lead subsequently authorized
and made a status-only register update; its consumed and final hashes are
separately recorded in [return25 r2](../research-progress/handoffs/25_TND_O_E11_R2_CONVEX_DENSITY_RETURN_20261107.json).
All ten other frozen sources remain byte-identical. Only this note and
that return are worker outputs.

## 1. Conventions, imported constants and statements

Use the complete canonical family
\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
 \partial_\lambda H=-H_{zz},\qquad |\Im z_j(\lambda)|\le1,
 \quad 0\le\lambda\le1/2.
 \tag{1}
\]
All zeros are counted with multiplicity. Write \(z_j=x_j+iy_j\) and
\(F_\lambda=H_\lambda'/H_\lambda\). Let \(A\ge1\) be the fixed absolute
constant in frozen [Note18](18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md),
equation (4):
\[
 |F_\lambda(u+4i)|\le A\log(2+|u|),\qquad
 \#\{j:u\le x_j\le u+1\}\le A\log(2+|u|).
 \tag{2}
\]
These hold for all real \(u\) and all declared times, including zero.
Polymath's Theorem 1.5(iv), §9 equation (105) and its following proof,
and Proposition 9.1(ii) are the primary inputs; Note18 explicitly pays
the time-zero limit and closed endpoints. Those primary count/resolvent
passages were freshly checked here. Their upper bounds have no
\(\exp(C/\lambda)\) height restriction.

Fix \(\chi\in C_c^2([-1,1])\), \(0\le\chi\le1\), equal to one on
\([-1/2,1/2]\). For \(T\ge8\), put
\[
 L=\log T,\quad a_T(x)=\chi((x-3T/2)/T),\quad
 \mathcal C_T=\{j:T/4\le x_j\le11T/4\}.
 \tag{3}
\]
The weight is supported in \([T/2,5T/2]\) and equals one on \([T,2T]\).
The cluster is bookkeeping only; no derivative of its indicator is taken.

Let \(g\in C^2([-1,1])\) be even and convex, with \(g(0)=0\), and define
\[
 G=\|g\|_\infty,\qquad
 Q_{T,g}(\lambda)=\sum_j a_T(x_j(\lambda))g(y_j(\lambda)).
 \tag{4}
\]
Then \(g\ge0\), \(g''\ge0\), and \(yg'(y)\ge0\). One explicit transport
constant is
\[
 D_\chi=A^2(36\|\chi''\|_\infty+1200\|\chi'\|_\infty).
 \tag{5}
\]
The general theorem is
\[
 \boxed{Q_{T,g}(\beta)\le Q_{T,g}(\alpha)
      +D_\chi G(\beta-\alpha)L^3
      \quad(0\le\alpha\le\beta\le1/2).}
 \tag{6}
\]
In particular this proves target (C), with no \(g'\) or \(g''\) dependence
in its constant.

For every fixed \(b\in(0,1/2)\), there is a constant \(B_b\) specified
below such that
\[
 \boxed{N_\lambda(T,v):=
 \#\{j:T\le x_j(\lambda)\le2T,\ |y_j(\lambda)|>v\}
 \le B_bTL e^{-bvL}}
 \quad(0<v<1).
 \tag{7}
\]
This holds simultaneously for every \(T\ge8\) and \(0\le\lambda\le1/2\).
It implies
\[
 \sum_{T\le x_j(\lambda)\le2T}y_j(\lambda)^2
 \le\frac{2B_b}{b^2}\frac{T}{L}.
 \tag{8}
\]
All-p local averaged bounds, including their constants and small-height
cover, are proved in §6.

## 2. Complete broad exterior field and its tail

Write \(P=6A\). Covering the cluster's horizontal length \(5T/2\) by
at most \(3T\) closed unit intervals, each with logarithm at most \(2L\),
gives
\[
 n:=\#\mathcal C_T\le PTL,
 \qquad m:=\#\{j:T/2\le x_j\le5T/2\}\le n.
 \tag{9}
\]
Let \(z=x+iy\) be active, so \(x\in[T/2,5T/2]\), \(|y|\le1\), and put
\(w=x+4i\). Every exterior root \(\zeta=u+iv\) satisfies
\[
 |x-u|\ge T/4\ge2,\qquad
 |(z-\zeta)^{-1}-(w-\zeta)^{-1}|\le5|x-u|^{-2}.
 \tag{10}
\]
Define the field by safe-line subtraction,
\[
 E_T(z)=F_\lambda(w)
       -\sum_{k\in\mathcal C_T}(w-z_k)^{-1}
       +\sum_{k\notin\mathcal C_T}
          [(z-z_k)^{-1}-(w-z_k)^{-1}].
 \tag{11}
\]
The first term retains full opposite-zero pairing. The last series is
absolutely convergent; removing the finite, generally non-opposite
cluster does not change that convention.

Here are explicit bounds. A distance shell \(h\le|x-u|<h+1\) contains
at most
\(2A[\log(2+x)+\log(h+2)]\) roots, by (2). Set
\(H=\lfloor T/4\rfloor\ge2\). Since \(H-1\ge T/16\),
\(\log(2+x)\le2L\), and \(\log(H+1)+1\le2L\), integration of the
decreasing shell majorant gives
\[
 \sum_{k\notin\mathcal C_T}|x-x_k|^{-2}
 \le\frac{2A}{H-1}[2L+\log(H+1)+1]
 \le\frac{128AL}{T}.
 \tag{12}
\]
For the finite safe-line cluster sum, shells from zero to
\(\lceil9T/4\rceil\le3T\) each contain at most \(4AL\) roots and
\(|w-z_k|\ge\sqrt{h^2+9}\). Hence
\[
 \sum_{k\in\mathcal C_T}|w-z_k|^{-1}
 \le4AL\left[\tfrac13+1+\log(3T)\right]
 \le12AL^2.
 \tag{13}
\]
Combining (2), (11)–(13), and \(T\ge8,L\ge1\), yields
\[
 |E_T(z)|\le2AL+12AL^2+640AL/T\le100AL^2.
 \tag{14}
\]
No absolute exterior harmonic sum was used.

There is also a full-index remainder: truncating the absolute difference
series in (11) at \(|x-x_k|<M\), integer \(M\ge2\), leaves at most
\[
 \frac{10A}{M-1}[2L+\log(M+1)+1].
 \tag{15}
\]
It tends to zero uniformly in time and in the active strip for fixed
\(T\). Start with full radial opposite-paired Hadamard cutoffs containing
the cluster, use accepted E08's paired tail, and then use (15) for the
difference series. This justifies (11) with the full canonical zero set.

## 3. The convex kernel and the two favorable signs

For \(f(x,y)=a_T(x)g(y)\), the accepted E08 chord derivation applies
without changing scale. For distinct endpoints, let
\(d=x_j-x_k\), \(e=y_j-y_k\), \(D=d^2+e^2\). It gives
\[
 K_f(z_j,z_k)=\int_0^1
  \frac{a_T(x_t)g''(y_t)e^2-a_T''(x_t)g(y_t)d^2}{D}\,dt.
 \tag{16}
\]
The mixed Hessian terms cancel exactly. On intervals with simple relevant
roots, the Newman-time finite-cluster identity is
\[
 Q_{T,g}'=-2\sum_{j<k\in\mathcal C_T}K_f(z_j,z_k)
   +2\sum_{\rm active\ j}
       [a_T'(x_j)g(y_j)\Re E_T(z_j)
        +a_T(x_j)g'(y_j)\Im E_T(z_j)].
 \tag{17}
\]
Inactive rows have zero endpoint gradients; repeated inactive roots need
no velocities and their coincident zero kernel is assigned zero.

First, the \(a_Tg''e^2\) part in (16) is nonnegative. Discarding its
nonpositive contribution to (17), rather than taking its absolute value,
gives
\[
 -2\sum_{j<k\in\mathcal C_T}K_f
 \le \|a_T''\|_\infty G n^2
 \le36A^2\|\chi''\|_\infty G L^2.
 \tag{18}
\]
This bound has no minimum-gap denominator or test-curvature constant.

Second, the imaginary exterior series is absolutely convergent: each
term has modulus at most \(2/|x-u|^2\). The exterior is conjugation
invariant, so pair its ordinates \(v,-v\). Their real vertical sum is
\[
 \frac{y-v}{d^2+(y-v)^2}+\frac{y+v}{d^2+(y+v)^2}
 =\frac{2y(d^2+y^2-v^2)}
        {[d^2+(y-v)^2][d^2+(y+v)^2]}.
 \tag{19}
\]
By (10) and \(|v|\le1\), this has the sign of \(y\). A real exterior
root contributes \(y/(d^2+y^2)\), with the same sign. Since the imaginary
part of \((z-\zeta)^{-1}\) is minus this vertical term, and \(g'(y)\)
has the sign of \(y\),
\[
 a_T(x)g'(y)\Im E_T(z)\le0.
 \tag{20}
\]
Absolute convergence permits this conjugate grouping even though the real
exterior field still requires opposite pairing. The favorable vertical
contribution is discarded, not estimated by \(\|g'\|_\infty\).

The remaining horizontal term in (17), using (9) and (14), is at most
\[
 2T^{-1}\|\chi'\|_\infty G(6ATL)(100AL^2)
   =1200A^2\|\chi'\|_\infty G L^3.
 \tag{21}
\]
Together (18), (20), (21), and \(L^2\le L^3\) prove
\(Q_{T,g}'\le D_\chi G L^3\) on every simple relevant interval.

## 4. Collision assembly for each broad fixed test

We use the qualitative compact-box argument in frozen
[Note19](19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md),
§§2–4, and its exact [return23](../research-progress/handoffs/23_TND_O_E12_RETURN_20261107.json).
Their hashes were verified. Their microscopic Lipschitz estimate is not
invoked with \(R=T\).

For fixed \(T,g\), the sum of the continuous function \(f=a_Tg\) over
root multisets is continuous, by local zero-free-boundary rectangles and
Rouché continuity. A collar around the support includes every possible
contributing root nearby in time. Multiple-root points in the closed
padded box \([T/2-1,5T/2+1]\times[-2,2]\) and time interval are compact.
At each, the canonical heat/Hermite splitting gives distinct simple roots
at every sufficiently close nonzero time; hence the multiple-point set is
locally isolated in space and time. Compactness makes it finite,
including spatial/time endpoints. This argument depends only on a fixed
compact support, not a microscopic width restriction.

For completeness, at fixed \(T,g\) the absolute chord bound is
\(\max(\|a_T\|_\infty\|g''\|_\infty,
\|a_T''\|_\infty G)\), and the active gradient is bounded by
\(\|a_T'\|_\infty G+\|a_T\|_\infty\|g'\|_\infty\).
Together with (9),(14) this supplies some finite two-sided derivative
bound on the complementary intervals. Continuity joins it across the
finite event set, so the fixed-test moment is Lipschitz and absolutely
continuous. This auxiliary regularity bound may depend on test
derivatives; the one-sided bound (18)–(21) does not. Summing the latter
over the finite time partition uses only its total duration and proves
(6), with exactly \(D_\chi\). No event number, separation, multiplicity,
Hermite error, or test-derivative constant enters (6).

The complete interaction passage is likewise legitimate for each fixed
\(T,g\): the E08 paired tail multiplies a finite bound on \(|\nabla f|\),
and (15) pays the exterior difference. Finite event-time values do not
affect the almost-everywhere or integrated formula. There is no collision
atom in the first derivative, no globally simple labeling, and no
differentiated radial or cluster indicator. A fixed \(C^2\) extension of
\(g\) beyond the strip, if desired for local Taylor statements, affects
none of the bounds on the actual strip.

## 5. Cosh consumer and exponential density

Fix \(c\in(0,1)\), \(a=c/2\), and one \(b\in(0,a)\). Let \(D_c\ge1\)
be the uniform time-zero zeta-density constant used in
[Note20](20_TND_O_E10_R2_ALL_ORDER_TRANSVERSE_MOMENTS_20261107.md),
(2), and set \(C_0=8D_c\). The entire broad support has H ordinates
\(x\in[T/2,5T/2]\), thus zeta ordinates \(t=x/2<2T\) and
\(|y|=2|\beta-1/2|\). Critical-line reflection doubles the right-half
count exactly once. The same complete-band estimate as Note20 gives
\[
 \#\{j:T/2\le x_j(0)\le5T/2,\ |y_j(0)|>v\}
 \le C_0TL e^{-avL}\quad(0<v<1).
 \tag{22}
\]
The fixed \(D_c\) is uniform as \(v\downarrow0\).

Set \(g_T(y)=\cosh(bLy)-1\). It is even, convex, nonnegative,
vanishes at zero and satisfies \(\|g_T\|_\infty\le T^b\).
Direct layer cake, with no general positive-test assertion, gives
\[
\begin{aligned}
 Q_{T,g_T}(0)
 &\le C_0TL\int_0^1 bL\sinh(bLv)e^{-avL}\,dv\\
 &\le C_0TL\,b\int_0^\infty\sinh(bw)e^{-aw}\,dw\\
 &=C_0TL\frac{b^2}{a^2-b^2}.
\end{aligned}
 \tag{23}
\]
The denominator is positive by the strict \(b<a\) hypothesis.
The horizontal-flux allowance in (6) is absorbed by
\[
 T^{b-1}L^2\le\frac{4}{e^2(1-b)^2}.
\]
Therefore, using \(\lambda\le1/2\),
\[
 Q_{T,g_T}(\lambda)\le K_bTL,\qquad
 K_b:=C_0\frac{b^2}{a^2-b^2}
          +\frac{2D_\chi}{e^2(1-b)^2}.
 \tag{24}
\]
This bound is uniform on the whole time interval, even when time varies
with height. Large test derivatives were never inserted into the flux
constant.

Put \(\kappa=(1-e^{-1})^2/2>0\). If \(t=bvL\ge1\), then
\(\cosh t-1=(e^t/2)(1-e^{-t})^2\ge\kappa e^t\). Each counted root in
\([T,2T]\) has plateau weight one, so its contribution to (24) gives
\(N_\lambda(T,v)\le(K_b/\kappa)TL e^{-bvL}\).
If \(bvL<1\), the ordinary count (9) gives
\(N_\lambda(T,v)\le PTL\le eP TL e^{-bvL}\).
Thus (7) holds with
\[
 B_b=\max\{K_b/\kappa,eP\}.
 \tag{25}
\]
For any desired fixed \(0<b<1/2\), choose, for example,
\(c=1/2+b\in(2b,1)\). With the fixed spatial profile and imported
absolute \(A\), these constants depend only on \(b\) and its selected
density constant. No uniform claim as \(b\uparrow1/2\) is made.

A final layer cake proves (8):
\[
 \sum_{T\le x_j(\lambda)\le2T}y_j(\lambda)^2
 =2\int_0^1vN_\lambda(T,v)\,dv
 \le\frac{2B_b}{b^2}\frac{T}{L}.
 \tag{26}
\]
This includes Decision11's mean transverse-mass conclusion. Taking
\(g(y)=y^2\) in (6) also gives its direct broad transport bound.

## 6. Local moments of every order, uniformly in time

For \(X\in[T,2T]\), \(0<R\le1\), define the same fixed-profile local
observable
\[
 Q_{X,R}(\lambda)=\sum_j\chi((x_j(\lambda)-X)/R)y_j(\lambda)^2,
 \qquad I_\chi=\int\chi.
 \tag{27}
\]
Its complete center band is \(B_R=[T-R,2T+R]\). For \(T\ge16\), it is
covered by the three dyadic bands at scales \(T/2,T,2T\), all at least
8. Applying (7) with the same \(b\), then expressing their logarithms
in terms of \(L\), gives
\[
 \#\{j:x_j(\lambda)\in B_R,\ |y_j(\lambda)|>v\}
 \le5B_bTL e^{-bvL}.
\]
Indeed the lower scale costs at most \(2^{b-1}<1\), the middle costs
1, and the upper costs at most 3. Closed endpoints may be counted more
than once. For \(8\le T<16\), the enlarged band lies in \(\mathcal C_T\);
(9) and \(e^{bvL}\le16^b\) supply the same kind of estimate. Thus,
for all \(T\ge8\), use the explicit constant
\[
 \widetilde B_b=5B_b+P16^b,
 \quad
 \#\{j:x_j\in B_R,\ |y_j|>v\}
 \le\widetilde B_bTL e^{-bvL}.
 \tag{28}
\]

Two closed H unit intervals cover the local window of length \(2R\).
By (2), its full population is at most \(JL\), where \(J=4A\).
Weighted Hölder, the exact center-width bound \(RI_\chi\), and direct
layer cake now give, for every integer \(p\ge1\),
\[
\begin{aligned}
 \frac1T\int_T^{2T}Q_{X,R}(\lambda)^p\,dX
 &\le\frac{RI_\chi}{T}(JL)^{p-1}
       \sum_{x_j\in B_R}|y_j|^{2p}\\
 &\le\frac{\widetilde B_b I_\chi}{J}
      R\left(\frac{J}{b^2}\right)^p\frac{(2p)!}{L^p}\\
 &\le\boxed{C_b^{\rm mom}R(A_b^{\rm mom})^p
                       \frac{(2p)!}{L^p}},
\end{aligned}
 \tag{29}
\]
where
\[
 A_b^{\rm mom}=J/b^2,\qquad
 C_b^{\rm mom}=\max\{1,\widetilde B_b I_\chi/J\}.
 \tag{30}
\]
These constants have no \(p,\lambda,T,R\) dependence. The factorial comes from the exact integral
\(2p\int_0^\infty v^{2p-1}e^{-bLv}\,dv=(2p)!/(bL)^{2p}\);
no fixed-order literature moment constant is imported. Thus (7), (8), (29) hold along
arbitrary joint sequences \(\lambda(T)\in[0,1/2]\), \(R(T)\in(0,1]\),
\(v(T)\in(0,1)\), and integer \(p(T)\ge1\) in the relevant clauses.

The one-pair comparison of Note20 remains valid with the new moment
constants: for a pair \(x_0\pm id\) whose local center profile is wholly
inside the band, its exact selected signal is
\((R/T)(2d^2)^p\int\chi^p\). The chosen allowance in (29) divided by
that signal is at least
\[
 \frac{C_b^{\rm mom}T}{I_\chi}
   e^{-\sqrt{2L/A_b^{\rm mom}}}\longrightarrow\infty
\]
uniformly over all integer orders. This lower-bounds an allowance,
not an actual moment or exceptional probability. Exponential averaged
rarity does not exclude an isolated pair.

## 7. Scope, sources and bounded verification

The acquired endpoint density and signed broad flux costs close this
mean-statistical consumer for the actual complete canonical family.
Convexity, horizontal separation, the canonical strip/count/resolvent,
and canonical time-zero density are all used. The local kernel/collision
geometry alone, shared by polynomial controls, does not supply the last
arithmetic input. No control is asserted to satisfy an unproved canonical
premise. The [result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[target classification](../../../../../avoid/01_restating_the_target.md)
and [scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
retain their meanings. All-covering-window vanishing remains RH.

The Polymath article is
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 4 August 2019.
Theorem 1.5(iv), Proposition 9.1(ii) and §9 (105) onward were freshly
checked here for the count/resolvent input. Its Proposition 3.1 supplies
the paired selected-simple dynamics and Hermite splitting; their checked
versions are recorded in frozen Notes17–19/return23. The time-zero
Maples–Rodgers input is
[arXiv:1404.3080v2](https://arxiv.org/html/1404.3080v2), 4 June 2016,
Corollary 2.3, Theorem 2.4 and §4 (18), freshly checked by this same worker
in Note20 §1 and identified in [source-use11](../references/11_TND_O_ALL_ORDER_DENSITY_SOURCE_USE_20261107.md).
No new full-paper review, article/PDF acquisition, priority claim or
premise from the separately triaged recent weighted-moment preprint is
made. Polymath's eventual-realness theorem retains its own positive-time
height margins; these density estimates do not improve its threshold.

One fixed theorem/consumer package and one local consistency/repair check
were completed. The check covered the Newman-time signs, derivative-free
constant, separated vertical field, real-field pairing, absolute remainder,
fixed-test collision assembly, exact cosh integral, polynomial flux
absorption, both threshold cases, dyadic cover and all-order constants.
No mathematical repair, numerical/symbolic research run, subdelegation,
redesign, shared-file edit, manuscript change, commit or push was needed.
No worker source transcript exists; none was fabricated. The package
awaits E13 assessment and retains shared-premise limitations; no
independent specialist review is claimed.
