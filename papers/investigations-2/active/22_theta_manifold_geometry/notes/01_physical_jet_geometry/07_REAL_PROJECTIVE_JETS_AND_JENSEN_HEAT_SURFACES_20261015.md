# Real projective jets and the Jensen heat surface hierarchy

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Internal mathematical review is not external refereeing or formal verification. The statements below are proved mathematical syntheses of classical ingredients, not a new theta estimate or a novelty claim.

The two constructions can be simplified and connected precisely. Real projectivization retains the spacetime obstruction. Separately, the number of missing real components of a Jensen surface equals a finite polynomial heat-flow collision count. The resulting family has two monotonicities and a useful degree-versus-heat dichotomy.

## 1. Real projectivization retains the obstruction

Let an analytic real field satisfy \(H_t=-H_{xx}\), with no identically zero slice. On \(E=H^2+H_x^2>0\), define

\[
\ell=[H:H_x]\in\mathbb{RP}^1,
\qquad
q=\frac{(H+iH_x)^2}{E}
=\frac{H^2-H_x^2+2iHH_x}{E}\in S^1.
\tag{1}
\]

The map \([a:b]\mapsto(a+ib)^2/(a^2+b^2)\) identifies \(\mathbb{RP}^1\) with the circle. Equivalently, \(\ell\) is the rank-one orthogonal projection

\[
\Pi=\frac1E\begin{pmatrix}H^2&HH_x\\HH_x&H_x^2\end{pmatrix}.
\]

Thus this carrier forgets the sign of the jet but retains its unoriented physical line. If \(D\) is a bounded Jordan domain with nonzero boundary jet, [Note 04](04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md)'s index theorem gives

\[
\deg(q|_{\partial D})
=2\operatorname{wind}_{\partial D}(H+iH_x)
=-2\sum_{(T,a)\in D}\left\lfloor\frac{m(T,a)}2\right\rfloor.
\tag{2}
\]

In particular, the boundary real-projective map extends over the disk exactly when there is no interior collision. Every degree appearing here is even; the displayed jet provides a lift to the double-covering circle. At an individual collision the actual real-projective map cannot extend continuously, since its local boundary degree is nonzero.

This sharpens the projective discussion in Note 04. There are three different operations:

* On a fixed complex spatial slice, \([f:f']\) extends across an order-\(m\) zero after cancellation. In the affine chart \(f/f'\), its derivative at the zero is \(1/m\). Thus extension alone loses the obstruction, although the marked derivative still retains multiplicity.
* On **real spacetime**, \([H:H_x]\) retains the circle obstruction. For \(H=x^2-2t\), paths \(t=kx\) give \([H:H_x]\to[-k:1]\), so even continuity fails at the collision.
* Allowing a boundary loop to fill freely in \(\mathbb{CP}^1\cong S^2\) removes the fundamental-group obstruction. This does not assert that the actual two-variable meromorphic map extends across its base point.

No new computational advantage is asserted: (1) is an exact sign-free repackaging of the same first jet.

## 2. A surface defect that includes singular models correctly

Let \(Q\in\mathbb R[x]\) have odd degree \(d=2g+1\), and let \(C_Q\) be the smooth projective normalization of \(y^2=Q(x)\). Write \(r_o(Q)\) for the number of distinct real roots having odd multiplicity. Then

\[
b_0(C_Q(\mathbb R))=\frac{r_o(Q)+1}{2},
\qquad
\Delta(Q):=g+1-b_0(C_Q(\mathbb R))
=\frac{d-r_o(Q)}2.
\tag{3}
\]

Indeed, writing \(Q=cA^2B\) with \(B\) squarefree does not change its normalized function field. The real roots of \(B\) are precisely those counted by \(r_o\). Its degree is odd, and the ordinary sign-interval count for the double cover gives (3). In root multiplicities,

\[
\boxed{\quad
\Delta(Q)=\frac{N_{\rm nonreal}(Q)}2
+\sum_{a\in\mathbb R:Q(a)=0}\left\lfloor\frac{\operatorname{mult}_a Q}2\right\rfloor.
\quad}
\tag{4}
\]

Here \(N_{\rm nonreal}\) counts all nonreal roots with multiplicity. Complex square factors cannot disappear unnoticed: the original degree remains in the defect. In particular, \(\Delta=0\) means exactly that all \(d\) roots are real and simple.

## 3. The defect is exactly a polynomial spacetime index

Evolve \(Q\) by the finite polynomial heat operator

\[
Q_s(x)=e^{-sD_x^2}Q(x),\qquad s\in\mathbb R.
\tag{5}
\]

For sufficiently large positive \(s\), \(Q_s\) has \(d\) simple real roots. To see this, if \(a_d\) is the leading coefficient,

\[
s^{-d/2}Q_s(\sqrt{s}\,y)\longrightarrow
 a_d\,p_d(1,y),
\]

coefficientwise, where \(p_d\) is the degree-\(d\) heat polynomial in Note 04. Its roots are simple and real. Small real coefficient perturbations retain one real root in each disjoint root interval, accounting for the entire degree.

The physical multiple-real-root events of (5) are isolated by Note 04. On a bounded time interval all polynomial roots remain bounded; hence there are finitely many such events. Once all roots are real and simple, no later event is possible: the local heat splitting at an event would require nonreal roots immediately before it. These observations also give ordinary preservation of polynomial hyperbolicity and immediate strictness after a multiple-root slice.

At an event of multiplicity \(m\), the local real-root counts are \(m\bmod2\) before, \(m\bmod2\) at the event when only odd multiplicities are counted, and \(m\) immediately after. Consequently

\[
\Delta(Q_T)=\Delta(Q_{T^-}),\qquad
\Delta(Q_{T^+})=\Delta(Q_T)-\lfloor m/2\rfloor,
\tag{6}
\]

with weights added for simultaneous events. A nonreal multiple-root event leaves (3) unchanged. Thus \(\Delta(Q_s)\) is a nonnegative, nonincreasing, left-continuous integer staircase, eventually zero, and

\[
\boxed{\quad
\Delta(Q_s)=\sum_{T\ge s:\,Q_T(a)=\partial_xQ_T(a)=0}
\left\lfloor\frac{m(T,a)}2\right\rfloor.
\quad}
\tag{7}
\]

The time-\(s\) events are deliberately included. If \(s\) is itself an event, the normalization has the **pre-splitting** component count.

Choose a regular \(a<s\) so close that there are no events in \([a,s)\), choose \(b\) after all events, and take spatial walls \(\pm R\) outside every real root for \(a\le t\le b\). Note 04 then yields

\[
\operatorname{wind}_{\partial([a,b]\times[-R,R])}
 (Q_t+i\partial_xQ_t)=-\Delta(Q_s).
\tag{8}
\]

This is an exact bridge between real-component deficit and spacetime winding. It applies to arbitrary odd real polynomials; theta-specific information has not entered.

## 4. A monotone Jensen hierarchy, with an existing classical comparator

Use [Note 05](05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md)'s \(f(z)=\xi(1/2+\sqrt z)\), coefficients \(\gamma_k\), and reciprocal Jensen polynomials

\[
R_d(x)=f(D)x^d=\sum_{k=0}^d\binom dk\gamma_kx^{d-k}.
\]

Define

\[
Q_d(s,x)=e^{-sD^2}R_d(x),\qquad
\Delta_g(s)=\frac{2g+1-r_o(Q_{2g+1}(s,\cdot))}{2}.
\tag{9}
\]

The surface in (9) is the normalization of \(y^2=Q_{2g+1}(s,x)\). At \(s=0\) it has the same real-component count as the original Jensen surface because reciprocation preserves every nonzero root and its multiplicity; \(\gamma_0,\gamma_d>0\) exclude zero roots there.

For every fixed \(s\),

\[
\partial_xQ_d(s,x)=dQ_{d-1}(s,x),
\qquad
\boxed{\Delta_g(s)\le\Delta_{g+1}(s).}
\tag{10}
\]

This remains true with repeated roots. For any real polynomial \(p\), consecutive odd-multiplicity real roots enclose a nonzero interior extremum of \(p\); at such an extremum \(p'\) has an odd-multiplicity root. Hence \(r_o(p')\ge r_o(p)-1\). Applying twice to \(Q_{2g+3}\) proves (10). Together with (6), the defect increases with degree and decreases with auxiliary heat time.

This is **not a new polynomial family**. Commutativity of differential operators gives

\[
Q_d(s,x)=(e^{-sz^2}f(z))(D_x)x^d,
\qquad
Q_d(1,2X)=\sum_{k=0}^d\binom dk\gamma_k H_{d-k}(X).
\tag{11}
\]

The latter is exactly O'Sullivan's Hermite–Jensen polynomial, equation (1.4) in *Zeros of Jensen polynomials and asymptotics for the Riemann xi function*. Its RH equivalence is already Theorem 1.2. The geometric content here is the precise defect/index interpretation and multiplicity-safe monotonicity.

The variable \(s\) is an **auxiliary polynomial heat time**. It is not the physical heat parameter of the complete theta transform in the manuscript: (11) multiplies \(f\) by a zero-free Gaussian and therefore leaves the entire function's zero divisor unchanged.

## 5. A degree-versus-heat dichotomy

Set

\[
\tau_g=\inf\{s\ge0:Q_{2g+1}(s,\cdot)\text{ has only real roots}\}.
\tag{12}
\]

Every \(\tau_g\) is finite, the threshold is attained by continuity of roots, and all slices after it have simple real roots. Rolle's theorem gives \(\tau_g\le\tau_{g+1}\). The following is a transparent consequence of classical Jensen convergence:

\[
\boxed{
\begin{array}{ll}
\mathrm{RH}:&\Delta_g(s)=0\ (g\ge1,s\ge0),\quad \tau_g=0;\\
\neg\mathrm{RH}:&\tau_g\longrightarrow+\infty.
\end{array}}
\tag{13}
\]

Under RH, Note 05 proves strict real-rootedness of every \(R_d\), and (5) preserves it. Conversely, suppose \(\tau_g\le S\) for all \(g\). For the real entire function \(F(z)=e^{-(S+1)z^2}f(z)\), the polynomials \(Q_d(S+1,x)\) are its reciprocal Jensen polynomials. Their reciprocals, scaled by \(1/d\), converge locally uniformly to \(F\), also along odd degrees. All those polynomials have real roots; Hurwitz therefore excludes nonreal zeros of \(F\), hence of \(f\), proving RH. Monotonicity of \(\tau_g\) supplies the divergence in (13).

More quantitatively in a logical sense, if \(f\) has \(K\) nonreal conjugate pairs counted with multiplicity inside specified disjoint disks, Rouché's theorem applied to the same convergence gives \(\Delta_g(s)\ge K\) for all sufficiently large \(g\), for each fixed \(s\). This is not an effective degree estimate. If \(f\) has infinitely many nonreal pairs then \(\Delta_g(s)\to\infty\) at every fixed \(s\).

The dichotomy explains a limitation: eventual maximality of each individual heat-deformed surface is automatic for every polynomial and says nothing about RH. A uniform finite heat time across all degrees already has full RH strength. The hierarchy supplies no new favorable theta inequality by itself.


## Exact examples at singular times

For \(Q=x^3+a x\), \(a>0\), the heat evolution is \(Q_s=x^3+(a-6s)x\). Its defect is one for \(s\le a/6\), including the triple event, and zero afterward. At the event the normalization has genus zero and one real component: the defect retains its left value.

For \(Q=x(x^2+1)^2\),

\[
Q_s=x^5+(2-20s)x^3+(1-12s+60s^2)x.
\]

The discriminant of the remaining quadratic in \(y=x^2\) is \(32s(5s-1)\). For \(0\le s\le1/5\), the defect is two. At \(s=1/5\), \(Q_s=x(x^2-1)^2\) has two simultaneous double real events, each of index minus one; afterward all five roots are simple real and the defect is zero. The complex square factors at \(s=0\) lower the normalized genus but do not escape the original-degree deficit.

## References and scope

The sources were opened and checked on 15 October 2026:

* [O'Sullivan, author's revised paper](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/xi-revised.pdf), Introduction equations (1.2)–(1.4), Theorem 1.2, and Section 3: coefficient normalization, reciprocal Jensen operators, and the already existing Hermite–Jensen RH criterion.
* [Angenent, *Inflection Points, Extatic Points and Curve Shortening*](https://people.math.wisc.edu/~angenent/preprints/extatic.pdf), Section 3: classical parabolic zero-number/degree mechanism underlying Note 04.
* [Gross–Harris, *Real algebraic curves*](https://www.numdam.org/item/10.24033/asens.1401.pdf), Section 6: classical real hyperelliptic topology. Formula (3) was independently derived here by reduction to the squarefree odd-degree model.

No numerical theta domain, new bound on RH, or publication-priority claim follows from these derivations. The strongest concise addition is (7)–(10); (13) usefully prevents mistaking automatic finite-degree regularization for an arithmetic gain.
