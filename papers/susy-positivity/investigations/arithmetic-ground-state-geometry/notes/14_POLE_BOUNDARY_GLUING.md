# Exact pole absorption by an attractive Robin defect

13 September 2026. This note derives a local boundary modification of the
lowest auxiliary field in [note 11](11_CLOSED_ARITHMETIC_SOURCE.md). Its
Green operator absorbs **both signs** of the arithmetic pole pairing
with the exact coefficient. The modified auxiliary action has one
negative mode, so its stationary value is not a positive minimum. A
specified projection gives a positive reference source and isolates a
single remaining negative direction for support length greater than
four. The fixed contact and every active prime are retained throughout.

This is an exact construction and a scoped failure of the unconstrained
Robin gluing. It is not a positive realization of the complete Weil
form, nor an identification with the quartic theory's caps. The spectral
projections below concern an explicitly solved second-order boundary
operator, not the unknown negative spectrum or square root of the
arithmetic operator.

## 1. The exact boundary condition selected by the pole kernel

Write \(I_L=(-h,h)\), \(h=L/2\), and fix \(a=1/2\). All inner products
are the ordinary \(L^2(I_L,dx)\) inner products, antilinear in the first
entry. Let \(R_{\mathrm f}\) denote the restriction to this interval of
the whole-line inverse \((-\partial_x^2+a^2)^{-1}\). Its kernel is

\[
R_{\mathrm f}(x,y)=\frac1{2a}e^{-a|x-y|}=e^{-|x-y|/2}.
\tag{1}
\]

The lowest gamma contribution and the pole operator are

\[
K_{0,L}=4I-R_{\mathrm f},\qquad
P_L(x,y)=2\cosh((x-y)/2).
\tag{2}
\]

In particular, the coefficient of the inverse in the lowest gamma
term is exactly one. Define

\[
\begin{aligned}
S_{\mathrm R}u&=-u'',\qquad A_{\mathrm R}=S_{\mathrm R}+a^2,\\
\operatorname{Dom}S_{\mathrm R}
&=\{u\in H^2(I_L):u'(h)=a u(h),\ u'(-h)=-a u(-h)\}.
\end{aligned}
\tag{3}
\]

Thus the outward normal condition at **both** endpoints is
\(\partial_\nu u=a u\). These are attractive Robin conditions. The
closed semibounded form is

\[
\mathfrak a_{\mathrm R}[u]
=\int_{-h}^h(|u'|^2+a^2|u|^2)\,dx
-a\bigl(|u(h)|^2+|u(-h)|^2\bigr),
\qquad \operatorname{Dom}\mathfrak a_{\mathrm R}=H^1(I_L).
\tag{4}
\]

The endpoint trace inequality makes the negative boundary term
arbitrarily small relative to \(\|u'\|^2\), at the cost of a multiple
of \(\|u\|^2\). This proves lower semiboundedness and closedness after
a shift. Integration by parts identifies its self-adjoint operator
with (3). More explicitly,

\[
\langle v,A_{\mathrm R}u\rangle-
\langle A_{\mathrm R}v,u\rangle
=[\overline{v'}u-\overline v u']_{-h}^{h}=0.
\tag{5}
\]

If \(v\) is in the adjoint domain, interior tests first give
\(v\in H^2(I_L)\); independent endpoint values in (5) then enforce
the same two Robin conditions. This also proves the equality of
operator and adjoint domains directly. This sign convention for the
attractive form is the one used by
[Pankrashkin–Popoff, *Mean curvature bounds and eigenvalues of Robin
Laplacians*](https://arxiv.org/abs/1407.3087). The interval formulas needed
here are derived below and do not use that paper's asymptotic theorem.

The exact inverse is

\[
\boxed{\quad
A_{\mathrm R}^{-1}(x,y)
=-\frac1{2a}e^{a|x-y|}
=-e^{|x-y|/2}
=R_{\mathrm f}(x,y)-P_L(x,y).
\quad}
\tag{6}
\]

Indeed this kernel is continuous, its first \(x\)-derivative has
jump \(-1\) at \(x=y\), and it satisfies (3) at each endpoint.
Consequently \((-\partial_x^2+a^2)A_{\mathrm R}^{-1}(x,y)=\delta_y\).
There is no homogeneous zero solution: for
\(u=Ae^{ax}+Be^{-ax}\), the left boundary condition forces \(A=0\)
and the right condition forces \(B=0\). The integral operator in (6)
therefore is the inverse on all of \(L^2(I_L)\), with range (3).
Its boundedness at fixed \(L\) is also immediate from the continuous
kernel on a compact square.

It follows that

\[
\boxed{\quad C_L:=K_{0,L}+P_L=4I-A_{\mathrm R}^{-1}.\quad}
\tag{7}
\]

The identity absorbs \(2|\cosh(x/2)\rangle\langle\cosh(x/2)|\)
and \(-2|\sinh(x/2)\rangle\langle\sinh(x/2)|\) together. It does not
replace the negative pole by a positive state norm.

## 2. The local action and its failed minimum

The whole-line positive lowest-field energy of note 11 can first be
reduced to the interval without changing it. For a fixed endpoint
value, the minimizing exterior extension is proportional to
\(e^{-a|x\mp h|}\); each exterior half-line contributes
\(a|u(\pm h)|^2\) to \(\int(|u'|^2+a^2|u|^2)\). Hence the exact
interval energy before the defect is

\[
\mathcal E_{\mathrm f}(f,u)
=4\|f-u\|^2+16\|u'\|^2
+8\bigl(|u(h)|^2+|u(-h)|^2\bigr).
\tag{8}
\]

Its natural boundary condition is \(\partial_\nu u=-a u\), and its
minimum is \(K_{0,L}[f]\). The pole-absorbing defect reverses the
endpoint coefficient:

\[
\begin{aligned}
\mathcal E_{\mathrm R}(f,u)
&=4\|f-u\|^2+16\|u'\|^2
-8\bigl(|u(h)|^2+|u(-h)|^2\bigr)\\
&=4\|f\|^2-8\Re\langle f,u\rangle
+16\mathfrak a_{\mathrm R}[u].
\end{aligned}
\tag{9}
\]

Thus the added local boundary action is precisely
\(-16(|u(h)|^2+|u(-h)|^2)\). Variation gives (3) and

\[
u_f=\tfrac14A_{\mathrm R}^{-1}f,\qquad
\mathcal E_{\mathrm R}(f,u_f)=C_L[f].
\tag{10}
\]

More strongly, for every \(u\in H^1(I_L)\),

\[
\mathcal E_{\mathrm R}(f,u)
=C_L[f]+16\mathfrak a_{\mathrm R}[u-u_f].
\tag{11}
\]

There is exactly one negative eigenvalue of \(A_{\mathrm R}\) for
every \(L>0\). To see this, the unique positive solution of

\[
\kappa_{\mathrm e}\tanh(\kappa_{\mathrm e}h)=a
\tag{12}
\]

satisfies \(\kappa_{\mathrm e}>a\). The normalized even eigenfunction
and its eigenvalue are

\[
\phi_{\mathrm e}(x)=
\frac{\cosh(\kappa_{\mathrm e}x)}
{\sqrt{h+\sinh(2\kappa_{\mathrm e}h)/(2\kappa_{\mathrm e})}},
\qquad
A_{\mathrm R}\phi_{\mathrm e}=-\delta_{\mathrm e}\phi_{\mathrm e},
\quad \delta_{\mathrm e}=\kappa_{\mathrm e}^2-a^2>0.
\tag{13}
\]

The left side of (12) increases from zero to infinity. An odd
negative eigenfunction of \(A_{\mathrm R}\) would require both
\(\kappa>a\) and \(\kappa\coth(\kappa h)=a\), which is impossible.
These exhaust the hyperbolic solutions for negative eigenvalues.
The regular Robin problem has compact resolvent, so there are no
other negative spectral components.

Taking \(u=u_f+t\phi_{\mathrm e}\) in (11) proves

\[
\inf_{u\in H^1(I_L)}\mathcal E_{\mathrm R}(f,u)=-\infty
\quad\text{for every }f.
\tag{14}
\]

Consequently (10) is a saddle value. It is not a stable Euclidean
Gaussian integral, a ground-state minimization, or the norm of its
displayed residuals in a positive Hilbert space. This fails already
with zero arithmetic input and cannot be repaired by a finite contact
term depending only on \(f\).

## 3. The exact sign of the reduced lowest pairing

The negative auxiliary mode in (13) contributes a **positive** reduced
coefficient \(4+1/\delta_{\mathrm e}\). There is a different possible
instability in the reduced source form. If \(\nu\) is an eigenvalue
of \(S_{\mathrm R}\), its coefficient in (7) is

\[
b(\nu)=4-\frac1{a^2+\nu}
=\frac{4\nu}{a^2+\nu}.
\tag{15}
\]

The even negative eigenvalue of \(S_{\mathrm R}\) is
\(-\kappa_{\mathrm e}^2<-a^2\). An additional odd negative eigenvalue
exists exactly when \(ah>1\), or \(L>4\). It is determined by

\[
\kappa_{\mathrm o}\coth(\kappa_{\mathrm o}h)=a,
\quad 0<\kappa_{\mathrm o}<a,
\quad
\phi_{\mathrm o}(x)=
\frac{\sinh(\kappa_{\mathrm o}x)}
{\sqrt{\sinh(2\kappa_{\mathrm o}h)/(2\kappa_{\mathrm o})-h}}.
\tag{16}
\]

The function \(\kappa\coth(\kappa h)\) strictly increases from
\(1/h\) to infinity. At \(L=4\), the corresponding zero eigenfunction
of \(S_{\mathrm R}\) is proportional to \(x\). For \(L<4\) the
lowest odd eigenvalue of \(S_{\mathrm R}\) is positive. All remaining
eigenvalues are positive; this follows by exhausting the even and odd
hyperbolic and linear solutions as above.

It follows without a numerical spectral estimate that

\[
\begin{array}{c|c}
0<L<4&C_L\text{ is bounded and strictly positive}\\
L=4&C_L\geq0,\quad\ker C_L=\operatorname{span}\{x\}\\
L>4&C_L\text{ has exactly one negative direction, }\phi_{\mathrm o}.
\end{array}
\tag{17}
\]

Two elementary inputs give useful exact normalization and threshold
checks without solving the spectral equation. Direct integration of
(6), with \(a=1/2\), gives

\[
C_L1=4e^{L/4}\cosh(x/2),\qquad
C_Lx=8e^{L/4}(1-L/4)\sinh(x/2).
\tag{17a}
\]

Thus the odd affine input itself has negative \(C_L\)-energy when
\(L>4\), since \(x\sinh(x/2)>0\) away from zero. Both inputs belong
to the logarithmic domain, and the same core approximation applies.

For \(L>4\), set

\[
\lambda_{\mathrm o}=a^2-\kappa_{\mathrm o}^2>0,
\qquad
r_L=\frac1{\lambda_{\mathrm o}}-4
=\frac{4\kappa_{\mathrm o}^2}{a^2-\kappa_{\mathrm o}^2}>0.
\tag{18}
\]

Then \(C_L\phi_{\mathrm o}=-r_L\phi_{\mathrm o}\).
The function \(\phi_{\mathrm o}\) belongs to the logarithmic source
domain of note 11 despite its nonzero endpoint traces. Approximation
by that note's compact-support core also gives negative test vectors
for this **lowest-field** form. No negativity of the complete Weil
form, or of the complete gamma-plus-pole form, follows from (17).

## 4. What projection of the unstable auxiliary mode accomplishes

Let \(\Pi_{\mathrm e}=|\phi_{\mathrm e}\rangle\langle\phi_{\mathrm e}|\)
and \(R_+=A_{\mathrm R}^{-1}(I-\Pi_{\mathrm e})\). Then
\(R_+\geq0\) and

\[
A_{\mathrm R}^{-1}=R_+-\delta_{\mathrm e}^{-1}\Pi_{\mathrm e}.
\tag{19}
\]

Restricting the field in (9) to \(u\perp\phi_{\mathrm e}\) gives a
strictly convex, coercive quadratic problem for each fixed \(f\).
Its minimum and the exact removed contribution are

\[
\begin{aligned}
\inf_{u\in H^1,\ u\perp\phi_{\mathrm e}}
\mathcal E_{\mathrm R}(f,u)
&=4\|f\|^2-\langle f,R_+f\rangle,\\
C_L[f]
&=\inf_{u\perp\phi_{\mathrm e}}\mathcal E_{\mathrm R}(f,u)
+\delta_{\mathrm e}^{-1}|\langle\phi_{\mathrm e},f\rangle|^2.
\end{aligned}
\tag{20}
\]

Projection thus fixes the divergent field integral, but a stable
Hessian in \(u\) does not imply a nonnegative energy in the joint
variables \((f,u)\). For \(L>4\), the odd vector (16) is orthogonal to
\(\phi_{\mathrm e}\), and the minimum in (20) still equals
\(-r_L\) on this normalized input. Neither removing the even
auxiliary mode nor adding its positive scalar cap supplies the missing
odd contribution.

There is nevertheless an explicit positive repair with this one
residual left visible. Let

\[
P_{\geq0}=\boldsymbol1_{[0,\infty)}(S_{\mathrm R}),\qquad
\mathscr H_{\geq0}=P_{\geq0}L^2(I_L),\qquad
S_+=S_{\mathrm R}|_{\mathscr H_{\geq0}}\geq0.
\tag{21}
\]

This constraint removes precisely the known even vector (13) and,
only when \(L>4\), the known odd vector (16). At \(L=4\) it retains
the zero mode. The form domain of \(S_+\) is
\(H^1(I_L)\cap\mathscr H_{\geq0}\); there its energy is exactly
\(\|u'\|^2-a(|u(h)|^2+|u(-h)|^2)\), now nonnegative.

Specify the positive preparation energy and its minimum by

\[
\begin{aligned}
\mathcal E_+(f,u)
&=4\|P_{\geq0}f-u\|^2+16\|S_+^{1/2}u\|^2\geq0,\\
u_+[f]&=\tfrac14(S_++\tfrac14)^{-1}P_{\geq0}f.
\end{aligned}
\tag{22}
\]

Here \(S_+^{1/2}\) is the energy insertion of the independently
specified positive Robin operator (21), not a square root of the
desired arithmetic form. On
\(\mathscr H_{\geq0}\oplus\mathscr H_{\geq0}\oplus\mathbb C\),
with its ordinary positive direct-sum inner product, set

\[
\mathcal B_L f=
\begin{pmatrix}
2S_+(S_++\tfrac14)^{-1}P_{\geq0}f\\
S_+^{1/2}(S_++\tfrac14)^{-1}P_{\geq0}f\\
\sqrt{4+\delta_{\mathrm e}^{-1}}\,
\langle\phi_{\mathrm e},f\rangle
\end{pmatrix}.
\tag{23}
\]

The first two entries are the minimum energy residuals of (22); the
last is the positive reduced even sector derived in (15). Every
coefficient is fixed by the mass and Robin condition. For
\(\xi,\zeta\in\mathscr H_{\geq0}\) and \(z\in\mathbb C\), the physical
Hilbert adjoint is the bounded, everywhere-defined map

\[
\mathcal B_L^*(\xi,\zeta,z)
=2S_+(S_++\tfrac14)^{-1}\xi
+S_+^{1/2}(S_++\tfrac14)^{-1}\zeta
+\sqrt{4+\delta_{\mathrm e}^{-1}}\,z\phi_{\mathrm e}.
\tag{24}
\]

Diagonalizing only the explicit Robin operator, or completing the
square in (22), proves

\[
\boxed{\quad
\mathcal B_L^*\mathcal B_L
=C_L+r_L\Pi_{\mathrm o},\qquad
\Pi_{\mathrm o}=|\phi_{\mathrm o}\rangle\langle\phi_{\mathrm o}|.
\quad}
\tag{25}
\]

For \(L\leq4\), the notation \(r_L\Pi_{\mathrm o}=0\) is used and
no odd vector need be selected. Thus the entire lowest gamma-plus-pole
pairing has an explicit positive gluing on these lengths. For greater
lengths (25) is a positive reference pairing with a known rank-one
negative residual. The global orthogonality constraints are part of
this changed preparation; they have not been derived as local gauge
constraints or as a cohomological condition on the quartic caps.

## 5. Supersymmetric factorization keeps track of the necessary shift

The usual ground-state factorization is especially explicit here.
Put

\[
w(x)=\kappa_{\mathrm e}\tanh(\kappa_{\mathrm e}x),\qquad
D=\partial_x-w,\quad\operatorname{Dom}D=H^1(I_L).
\tag{26}
\]

Integration by parts gives
\(D^*=-\partial_x-w\) with \(\operatorname{Dom}D^*=H_0^1(I_L)\).
Because \(w(\pm h)=\pm a\),

\[
\begin{aligned}
D^*D&=S_{\mathrm R}+\kappa_{\mathrm e}^2
=A_{\mathrm R}+\delta_{\mathrm e}\geq0,
&\operatorname{Dom}D^*D&=\operatorname{Dom}A_{\mathrm R},\\
DD^*&=-\partial_x^2+\kappa_{\mathrm e}^2
-2\kappa_{\mathrm e}^2\operatorname{sech}^2(\kappa_{\mathrm e}x),
&\operatorname{Dom}DD^*&=H^2(I_L)\cap H_0^1(I_L).
\end{aligned}
\tag{27}
\]

The block charge \(\left(\begin{smallmatrix}0&D^*\\D&0\end{smallmatrix}\right)\)
on \(H^1\oplus H_0^1\) is self-adjoint and its square has these two
nonnegative partner Hamiltonians. The Robin ground state is
\(\phi_{\mathrm e}\in\ker D\). These domain-sensitive Robin/Dirichlet
supersymmetric partners are consistent with the primary analysis of
[Al-Hashimi–Salman–Shalaby–Wiese, *Supersymmetric descendants of
self-adjointly extended quantum mechanical Hamiltonians*](https://arxiv.org/abs/1303.2343).
The factor and its domains in (26)–(27) have been checked directly here.

This is a positive supersymmetric system, but its first Hamiltonian
is \(A_{\mathrm R}+\delta_{\mathrm e}\), not \(A_{\mathrm R}\).
There can be no unshifted positive-Hilbert-space factorization
\(A_{\mathrm R}=D_0^*D_0\), because of (13).

For example, using the nonnegative \(D^*D\) as the kinetic operator
in the original positive residual model changes the reduced lowest
operator to

\[
C_L^{\mathrm{shift}}
=4I-(A_{\mathrm R}+\kappa_{\mathrm e}^2)^{-1}\geq0.
\tag{28}
\]

The exact difference from the required pole gluing is

\[
C_L-C_L^{\mathrm{shift}}
=-\kappa_{\mathrm e}^2 A_{\mathrm R}^{-1}
(A_{\mathrm R}+\kappa_{\mathrm e}^2)^{-1}.
\tag{29}
\]

This difference is nonzero on infinitely many Robin eigenfunctions.
A supersymmetric energy shift therefore changes the bulk response;
it cannot be described as merely deleting the one unstable pole.
Shifting only the Hessian to \(A_{\mathrm R}+\delta_{\mathrm e}\)
instead leaves a zero mode with a generally nonzero linear source
coupling, so elimination additionally requires a projection or a
further mass. Neither operation preserves (6) automatically.

## 6. The full arithmetic form and its source domain are retained

Let \(\mathcal A_{\geq1,L}\) be the source of note 11 with its
\(k=0\) output pair removed, retaining all \(a_k=2k+1/2\), \(k\geq1\),
and the original whole-line fields. Removing one bounded output pair
does not alter its maximal domain or closedness. Define

\[
\widetilde{\mathcal A}_L f
=\mathcal A_{\geq1,L}f\oplus\mathcal B_Lf,
\qquad
\operatorname{Dom}\widetilde{\mathcal A}_L=\mathcal D_{\log,L},
\tag{30}
\]

where explicitly

\[
\mathcal D_{\log,L}
=\left\{f\in L^2(I_L):
\int_{\mathbb R}\log(2+|\tau|)
|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\}.
\tag{31}
\]

This source is closed into an ordinary positive Hilbert space.
Its graph norm is equivalent to the one in note 11, and
\(C_c^\infty(I_L)\) remains an operator core. The adjoint is

\[
\widetilde{\mathcal A}_L^*(\Psi,b)
=\mathcal A_{\geq1,L}^*\Psi+\mathcal B_L^*b,
\quad
\operatorname{Dom}\widetilde{\mathcal A}_L^*
=\operatorname{Dom}\mathcal A_{\geq1,L}^*
\oplus\operatorname{codom}\mathcal B_L.
\tag{32}
\]

The first adjoint domain is the distributional-restriction domain of
note 11 with the \(k=0\) terms omitted. It is not the stronger
whole-line \(L^2\) adjoint domain. The bounded second summand cannot
change this domain. Equations (25) and (30) give the exact identity

\[
\|\widetilde{\mathcal A}_Lf\|^2
=K_L[f]+P_L[f]+r_L|\langle\phi_{\mathrm o},f\rangle|^2.
\tag{33}
\]

Its induced operator is \(T_L+P_L+r_L\Pi_{\mathrm o}\), with the
same operator domain as \(T_L=\mathcal A_L^*\mathcal A_L\).
The operator domain is distinct from the logarithmic form domain (31).

For every active prime power, put
\(d_{p,m}=m\log p<L\),
\(c_{p,m}=(\log p)p^{-m/2}\), and
\(T_df=(E_Lf)(\,\cdot-d)|_{I_L}\). The complete target is therefore

\[
\boxed{\begin{aligned}
Q_L[f]={}&\|\widetilde{\mathcal A}_Lf\|^2
+w_0\|f\|^2\\
&-\sum_{m\log p<L}c_{p,m}
\langle f,(T_{d_{p,m}}+T_{d_{p,m}}^*)f\rangle
-r_L|\langle\phi_{\mathrm o},f\rangle|^2,\\
w_0={}&\psi(\tfrac14)-\log\pi
=-\gamma_E-\tfrac\pi2-3\log2-\log\pi.
\end{aligned}}
\tag{34}
\]

No contact counterterm, prime omission, shifted arithmetic source, or
assumption about \(Q_L\)'s sign has been used. All remaining terms
are bounded at fixed \(L\), so (34) extends from compactly supported
smooth inputs to exactly (31) and remains a closed semibounded form.
Cutting off the unchanged massive tail and then taking its monotone
limit gives the same source and strong-resolvent convergence after a
fixed lower-bound shift, by the argument in note 11.

The kernel identity (7) is compatible with embedding smaller-support
inputs in larger intervals. The spectral repair
\(r_L\Pi_{\mathrm o}\), however, depends on \(L\). For \(L>4\), the
positive norm (33) and the final negative term in (34) are generally
not separately support compatible; their sum is. This is a material
limitation of treating the projection as the eventual global physical
preparation.

## 7. What this coupling establishes and what remains necessary

Both pole signs now have a concrete origin in a local self-adjoint
boundary condition of an auxiliary field. Their coefficient is fixed
by the lowest gamma mass and the Green derivative jump. The simplest
action realizing that kernel is excluded as a positive gluing because
its field integral has the explicit negative even mode (13).

Projection and supersymmetric factorization are explicit changes with
different costs. Projecting only the negative Hessian mode makes
elimination finite but leaves a negative odd source direction for
\(L>4\). The positive source (23) removes that additional direction
and records its exact rank-one deficit in (34). The supersymmetric
shift (28) instead changes infinitely many response coefficients.
None of these conclusions excludes more general constrained or
interacting boundary theories.

The resulting positive infinite-state reference pairing is a useful
intermediate object: it includes the complete gamma contribution and
both poles for \(L\leq4\), and has only the displayed additional odd
deficit for larger supports. The complete Weil norm identity still
requires a joint mechanism for the fixed contact, every prime return,
and that deficit. In particular, a proposed stabilization must change
the field or source coupling, not simply add an input-only contact to
the divergent action (9). Showing positivity of the remaining full
block by assuming its Schur complement nonnegative would again assume
the desired result.

All sign, domain, normalization and mode-count claims here are direct
analytical calculations. They require independent specialist review;
an algebra replay can check kernel identities and coefficients, but
cannot certify self-adjointness or the logarithmic-domain arguments.
