# A stable collective feedback source and its exact compact defect

13 September 2026. This note combines the pole interference of
[note 15](15_COHERENT_DELAY_DEFECT.md) and the conservative prime returns
of [note 16](16_PRIME_RETURN_CHANNELS.md) with one specified stable
boundary response. The resulting source is closed in an ordinary
positive Hilbert space on the full logarithmic domain. Its gluing is

\[
\boxed{\quad
\|\Gamma_L f\|^2=Q_L[f]+\langle f,C_{\kappa,\mu}f\rangle,
\qquad C_{\kappa,\mu}>0\text{ compact}.
\quad}
\]

The contact, both pole signs, the gamma term and every active prime
have their exact arithmetic coefficients in this identity. The
additional compact operator is explicit and cannot be discarded. This
is a positive completion of the complete target, not a factorization
or positivity proof for \(Q_L\). No square root or unknown spectral
data of \(Q_L\) enter the construction.

A second result shows that a Hilbert–Schmidt coherent correction to the
already unbounded gamma source cannot realize the complete form. The
feedback below escapes this restriction through a compact correction
that is not Hilbert–Schmidt. Its slow ultraviolet decay is essential;
the residual error still remains.

## 1. Fix the positive reference source before the feedback

All input inner products are those of \(X_L=L^2(I_L,dx)\), antilinear
in the first entry, with \(I_L=(-L/2,L/2)\). Write \(E_L\) for zero
extension, \(U_dF(x)=F(x-d)\), and \(H=-\partial_x^2\) on the line.
The massive residual source of [note 11](11_CLOSED_ARITHMETIC_SOURCE.md)
is

\[
(\mathcal A_\gamma F)_k=
\begin{pmatrix}
\sqrt{2/a_k}\,H(a_k^2+H)^{-1}F\\
\sqrt{2a_k}\,\partial_x(a_k^2+H)^{-1}F
\end{pmatrix},
\qquad a_k=2k+\tfrac12.
\tag{1}
\]

Its positive output is a countable sum of pairs of ordinary
\(L^2(\mathbb R)\) spaces. Tensor it with the unit physical quartic cap

\[
\chi=\lambda^{-1/2}h_{f_0}(Z^2+W^2),\qquad
f_0=(Z^4+W^4+Z^2W^2)/16,\qquad
\lambda=256\pi^2/3,
\tag{2}
\]

where the raw volume form is implicit as in
[note 10](10_REFLECTED_BOUNDARY_PAIRING.md).
The evaluated norm \(\|\chi\|=1\) supplies an isometric internal label;
no unknown other entry of the quartic metric is used.

Fix \(D\ge L\). In the lowest output pair introduce the raw delay
source

\[
\mathcal B_DF=-\frac{e^{D/2}}2
\begin{pmatrix}(U_D+U_{-D})F\\ (U_D-U_{-D})F\end{pmatrix}
\otimes\chi,
\tag{3}
\]

with all other components zero, and set

\[
\mathcal A_0=(\mathcal A_\gamma\otimes\chi+\mathcal B_D)E_L.
\tag{4}
\]

The same-output interference in note 15 gives the exact identity

\[
\|\mathcal A_0f\|^2=K_L[f]+P_L[f]+e^D\|f\|^2,
\quad
P_L=2|c_L\rangle\langle c_L|-2|s_L\rangle\langle s_L|,
\tag{5}
\]

where \(c_L(x)=\cosh(x/2)\), \(s_L(x)=\sinh(x/2)\), and
\(K_L[f]=\|\mathcal A_\gamma E_Lf\|^2\).
The source is closed, with domain and compact-support core

\[
\mathcal D_{\log,L}
=\left\{f\in X_L:\int_{\mathbb R}\log(2+|\tau|)
 |\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\},
\qquad C_c^\infty(I_L).
\tag{6}
\]

Let \(T_L=(\mathcal A_\gamma E_L)^*(\mathcal A_\gamma E_L)\). Then

\[
T_0:=\mathcal A_0^*\mathcal A_0=T_L+P_L+e^D I,
\qquad \operatorname{Dom}T_0=\operatorname{Dom}T_L.
\tag{7}
\]

The negative pole eigenvalue is \(L-2\sinh(L/2)\). Thus

\[
T_0\ge m_{L,D}I,\qquad
m_{L,D}=e^D+L-2\sinh(L/2)>0.
\tag{8}
\]

The compact form-domain embedding proved in note 11 makes \(T_0\)
have compact resolvent. In particular \(T_0^{-1}\) exists and is
compact. This is an independently positive gamma-and-pole reference;
it contains no prime kernel or unknown arithmetic operator.

## 2. Specify a stable response and a coherent readout

Choose real parameters \(\mu\ge0\), \(\kappa>0\). For each input \(f\),
prepare an auxiliary boundary field \(w\in\mathcal D_{\log,L}\) by
minimizing

\[
\mathcal E_f(w)
=\|\mathcal A_0w\|^2+\mu\|w\|^2
-2\Re\langle f,w\rangle.
\tag{9}
\]

For fixed external \(f\), this functional is coercive and bounded below.
It is not a nonnegative joint energy if \(f,w\) are both dynamical.
Its Hessian is the already specified strictly positive \(T_0+\mu\).
The unique response and the completed square are

\[
R_\mu=(T_0+\mu)^{-1},\qquad w_f=R_\mu f,
\tag{10}
\]
\[
\mathcal E_f(w)
=\|(T_0+\mu)^{1/2}(w-w_f)\|^2-\langle f,R_\mu f\rangle.
\tag{11}
\]

The square root in (11) only denotes the known positive energy in
(9); it does not define the source. The response may equivalently be
defined by the weak Euler equation of (9). Its minimum value can be
negative because of the external drive; stability refers to the
positive Hessian in the field variable.

Specify the observed state by destructive feedback of this response
into the same residual output:

\[
\boxed{\quad
\mathcal A_{\rm fb}f
=\mathcal A_0(f-\kappa w_f)
=\mathcal A_0f-\kappa\mathcal A_0R_\mu f.
\quad}
\tag{12}
\]

This readout is additional coupling data. It is not asserted to be
the minimum of its own squared norm, and the feedback gain is not
derived from the quartic theory alone.

The correction \(\mathcal F_{\kappa,\mu}=-\kappa\mathcal A_0R_\mu\)
is bounded on \(X_L\), since

\[
\|\mathcal A_0R_\mu\|
=\sup_{\lambda\in\sigma(T_0)}
 \frac{\sqrt\lambda}{\lambda+\mu}
\le m_{L,D}^{-1/2}.
\tag{13}
\]

For \(\mu>0\) it also has the bound \(1/(2\sqrt\mu)\).
Its singular values tend to zero, so this correction is compact.
Consequently (12) is a closed source on exactly (6), with the same
graph topology and core.

If \(\mathscr Y\) is the positive output of (4), its maximal Hilbert
adjoint is

\[
\mathcal A_{\rm fb}^*g
=\mathcal A_0^*g-\kappa R_\mu\mathcal A_0^*g,\qquad
\operatorname{Dom}\mathcal A_{\rm fb}^*
=\operatorname{Dom}\mathcal A_0^*.
\tag{14}
\]

Here \(R_\mu\mathcal A_0^*\) on that domain extends boundedly as
\((\mathcal A_0R_\mu)^*\). Bounded perturbation proves the maximal
domain statement; an informal distributional product is not being
used to replace the interval adjoint of note 11.

## 3. The negative contact and the residual are both exact

Expanding (12) and using \(T_0R_\mu=I-\mu R_\mu\) yields, as closed
forms on (6),

\[
\|\mathcal A_{\rm fb}f\|^2
=\|\mathcal A_0f\|^2-2\kappa\|f\|^2
+\langle f,C_{\kappa,\mu}f\rangle,
\tag{15}
\]
\[
\boxed{\quad
C_{\kappa,\mu}
=2\kappa\mu(T_0+\mu)^{-1}
+\kappa^2T_0(T_0+\mu)^{-2}.
\quad}
\tag{16}
\]

Both terms are positive compact operators, with the second strictly
positive on every nonzero input. Positivity here means a positive
quadratic form, not a uniform positive spectral gap for this compact
operator. Its eigenvalue at \(\lambda\in\sigma(T_0)\) is

\[
c_{\kappa,\mu}(\lambda)
=\frac{2\kappa\mu}{\lambda+\mu}
+\frac{\kappa^2\lambda}{(\lambda+\mu)^2}>0.
\tag{17}
\]

This is how a compact coherent source correction produces a negative
scalar contact when paired with an unbounded source. A bound on the
correction alone does not make its cross term compact. Its positive
self-pairing is an unavoidable part of the displayed readout.

Now choose a finite prime set \(\mathcal S\) containing every prime
with \(\log p<L\). Include *all* returns of each selected prime through
the previously specified graph source

\[
\mathcal D_pF=
\sqrt{\frac{d_pq_p(1+q_p)}{1-q_p}}\,
(I-U_{d_p})(I-q_pU_{d_p})^{-1}F\otimes\chi,
\quad d_p=\log p,\quad q_p=p^{-1/2}.
\tag{18}
\]

Set

\[
c_{\mathcal S}=\sum_{p\in\mathcal S}
 \frac{2d_pq_p}{1-q_p},\qquad
\mathcal J_{\mathcal S}f=(\mathcal D_pE_Lf)_{p\in\mathcal S}.
\tag{19}
\]

Each return series converges in operator norm. On supported inputs,
returns with \(m\log p\ge L\) have zero translation overlap, although
their contribution to the loop's scalar contact has already been
included in (19). Thus

\[
\|\mathcal J_{\mathcal S}f\|^2
=c_{\mathcal S}\|f\|^2
-\sum_{m\log p<L}(\log p)p^{-m/2}
 \langle E_Lf,(U_{m\log p}+U_{m\log p}^*)E_Lf\rangle.
\tag{20}
\]

Keep the fixed arithmetic contact

\[
w_0=\psi(1/4)-\log\pi
=-\gamma_E-\pi/2-3\log2-\log\pi<0.
\tag{21}
\]

After the response law and gluing have been derived, prescribe

\[
2\kappa=e^D+c_{\mathcal S}-w_0>0,\qquad
\Gamma_Lf=\mathcal A_{\rm fb}f\oplus\mathcal J_{\mathcal S}f.
\tag{22}
\]

In the notation of notes 00 and 03,
\(\kappa_{\mathcal S}=c_{\mathcal S}-w_0\), so the same matching is
\(2\kappa=e^D+\kappa_{\mathcal S}\); \(w_0\) is subtracted only once.
Equation (22) matches a known coefficient. It is not an independent
physical prediction of that coefficient.

Combining (5), (15), and (20) gives the full identity

\[
\boxed{\quad
\langle\Gamma_Lf,\Gamma_Lg\rangle
=Q_L(f,g)+\langle f,C_{\kappa,\mu}g\rangle,
\qquad f,g\in\mathcal D_{\log,L}.
\quad}
\tag{23}
\]

All target terms occur with their fixed coefficients. The identity
for mixed inputs follows either directly or by complex polarization.

The source \(\Gamma_L\) is closed on (6), because its added prime
ports are bounded. Its ordinary physical adjoint is

\[
\Gamma_L^*(g,(z_p)_p)
=\mathcal A_{\rm fb}^*g+
 \sum_{p\in\mathcal S}E_L^*\mathcal D_p^*z_p,
\quad
\operatorname{Dom}\Gamma_L^*
=\operatorname{Dom}\mathcal A_0^*
 \oplus\bigoplus_{p\in\mathcal S}\mathscr Y_p.
\tag{24}
\]

Cap contraction is included in each \(\mathcal D_p^*\).
The block charge
\(\left(\begin{smallmatrix}0&\Gamma_L^*\\\Gamma_L&0\end{smallmatrix}\right)\)
on \(\operatorname{Dom}\Gamma_L\oplus\operatorname{Dom}\Gamma_L^*\)
is self-adjoint and its square is positive. This is a specified
positive Hilbert realization of the *completed* form in (23), not
an assumed positive block with the unknown target as its Schur
complement. It does not supply a local interacting supersymmetric
Lagrangian coupling the quartic theory to the graph.

If \(W_L\) is the semibounded operator associated with \(Q_L\),
then \(\Gamma_L^*\Gamma_L=W_L+C_{\kappa,\mu}\), with operator
domain \(\operatorname{Dom}T_L\). The logarithmic source/form domain
and this operator domain remain distinct.

## 4. The feedback parameter does not remove the defect

For fixed \(L,D,\mathcal S\), and hence fixed \(T_0,\kappa\), the gap
(8) gives norm convergence

\[
C_{\kappa,\mu}\longrightarrow\kappa^2T_0^{-1}>0
\qquad(\mu\downarrow0).
\tag{25}
\]

Thus removing the auxiliary mass does not give the target norm. At
the other extreme \(C_{\kappa,\mu}\to2\kappa I\) strongly as
\(\mu\to\infty\), not zero. This is not operator-norm convergence;
a norm limit of compact operators would remain compact.

More generally, for every fixed \(\lambda>0\), differentiation of
(17) gives

\[
\frac{\partial c_{\kappa,\mu}(\lambda)}{\partial\mu}
=\frac{2\kappa\lambda(\lambda+\mu-\kappa)}
 {(\lambda+\mu)^3},
\tag{26}
\]
\[
\inf_{\mu\ge0}c_{\kappa,\mu}(\lambda)
=\begin{cases}
\kappa^2/\lambda,&\lambda\ge\kappa,\\
2\kappa-\lambda,&0<\lambda<\kappa.
\end{cases}
\tag{27}
\]

Both alternatives are strictly positive. No sequence of this one
feedback parameter removes the residual even on one fixed nonzero
eigenmode. At high \(\lambda\),

\[
c_{\kappa,\mu}(\lambda)
=\frac{2\kappa\mu+\kappa^2}{\lambda}+O(\lambda^{-2})
\tag{28}
\]

for fixed parameters. Compactness makes the defect small on high
spectral modes; it does not establish positivity of \(Q_L\) on the
remaining modes. Adding independent positive output ports cannot
subtract this positive error.

The construction is explicit for every fixed support, but the
completed norm is not asserted to be compatible with inclusion of
supports. The response \(T_0^{-1}\) is an interval response, and the
choice of \(D,\mathcal S,\kappa\) can change as the support grows.
The signed \(Q_L\) obtained after subtracting (16) is compatible, as
in note 11. Note 16's divergent all-prime contact is not eliminated
by silently taking an infinite set in (22).

## 5. Hilbert–Schmidt coherent corrections cannot supply the contact

There is a useful restriction on more regular attempts to finish the
gluing, independent of the finite raw delay alphabet in note 15.

**Proposition.** Embed the gamma output isometrically into any positive
Hilbert space \(\mathscr Z\), and write \(A=\mathcal A_\gamma E_L\)
for that source. There is no Hilbert–Schmidt map
\(B:X_L\to\mathscr Z\) such that

\[
\|(A+B)f\|^2=Q_L[f]\qquad(f\in C_c^\infty(I_L)).
\tag{29}
\]

The source \(A\) is already unbounded. This proposition is therefore
different from the earlier obstruction to a bounded *total* source.

**Proof.** Hilbert–Schmidt maps are bounded, so the left-hand side is
a closed form on (6), with its same compact-support core. Equality
on that core extends to all of (6), since the arithmetic remainder
is bounded.

Choose an interior interval \(J\) of length
\(0<\ell<\min(L,\log2)\), and let

\[
f_n(x)=\ell^{-1/2}\boldsymbol1_J(x)
 e^{2\pi i n x/\ell},\qquad n=1,2,\ldots.
\tag{30}
\]

These form an orthonormal sequence in \(X_L\).
Their zero extensions have sinc Fourier tails, so each belongs to
(6). Every prime-power translation has distance at least \(\log2\);
therefore all of its correlations on (30) vanish. Integration by
parts on \(J\) gives
\(\langle c_L,f_n\rangle,\langle s_L,f_n\rangle=O(n^{-1})\).
Consequently

\[
Q_L[f_n]-\|Af_n\|^2=w_0+O(n^{-2}).
\tag{31}
\]

The gamma multiplier is bounded above by a constant times
\(\log(2+|\tau|)\). Fourier translation and
\(\log(2+|s+N|)\le\log(2+|s|)+\log(1+|N|)\) give

\[
\|Af_n\|^2\le C_L\log(n+2).
\tag{32}
\]

The finite weighted sinc integral justifies this estimate despite
the endpoint jumps. If (29) held, its expansion and \(w_0<0\) would
give, for all sufficiently large \(n\),

\[
\frac{|w_0|}{2}
\le -2\Re\langle Af_n,Bf_n\rangle-\|Bf_n\|^2
\le 2\|Af_n\|\|Bf_n\|.
\tag{33}
\]

Hence \(\|Bf_n\|^2\ge c_L/\log(n+2)\) with a positive constant
\(c_L\). This contradicts
\(\sum_n\|Bf_n\|^2\le\|B\|_{\rm HS}^2<\infty\). ∎

In particular a defect with a square-integrable Hilbert-valued kernel
\(b(x)\), or any finite-rank bounded coherent correction, fails (29).
Compact corrections in general are not excluded. The argument does
not forbid a different bulk source, a change in the observable, or a
singular coupling outside this Hilbert–Schmidt class. It also does not
say that every normalizable individual state is Hilbert–Schmidt as a
family; the integrated source regularity is the hypothesis.

The same obstruction applies directly to the assembled reference
\(A_{\rm ref}=\mathcal A_0\oplus\mathcal J_{\mathcal S}\), not only to
the gamma source. In that case (5), (20), and (22) give exactly

\[
Q_L[f]-\|A_{\rm ref}f\|^2=-2\kappa\|f\|^2.
\tag{33a}
\]

The sequence (30) still has
\(\|A_{\rm ref}f_n\|^2=O(\log(n+2))\), since all additions to its
gamma form are bounded. Repeating (33) excludes a Hilbert–Schmidt
coherent correction to this reference as well. This qualification
matters because the remote delay correction in (3) is already outside
the Hilbert–Schmidt class.

In fact the same proof excludes every finite Schatten class
\(\mathcal S_p\), \(0<p<\infty\). For \(p\ge2\), convexity applied
in a singular-vector expansion and Bessel's inequality give

\[
\sum_n\|Bf_n\|^p\le\sum_j s_j(B)^p<\infty.
\tag{33b}
\]

The lower bound from (33) contradicts this, since
\(\sum_n(\log(n+2))^{-p/2}\) diverges. For \(p<2\), membership in
\(\mathcal S_p\) already implies Hilbert–Schmidt membership.
This strengthening concerns the decay of singular values; arbitrary
compact corrections remain possible.

## 6. The collective response lies beyond that regularity class

The compact correction in (12) is in fact not Hilbert–Schmidt for
any \(\kappa>0,\mu\ge0\). This can be proved without assuming a Weyl
law for the compressed logarithmic operator.

Let \(H_{\rm D}=-\partial_x^2\) be the ordinary Dirichlet Laplacian on
\(I_L\), and let

\[
b(s)=\sum_{k\ge0}\frac2{a_k}\frac{s}{a_k^2+s}
=\Re\psi\!\left(\tfrac14+\tfrac{i\sqrt s}{2}\right)-\psi(\tfrac14).
\tag{34}
\]

For each massive preparation, restricting its auxiliary field to
\(H_0^1(I_L)\) and extending it by zero gives an admissible whole-line
field. Its minimum energy is at least the whole-line minimum.
The Dirichlet minimum is exactly the corresponding summand of
\(b(H_{\rm D})\). Summing the nonnegative energies therefore proves
the form comparison

\[
T_L\le b(H_{\rm D})
\tag{35}
\]

on the right-hand form domain. This is an upper comparison for
eigenvalues, not a replacement of the actual gamma boundary
condition.

Let \(0<\lambda_1\le\lambda_2\le\cdots\to\infty\) be the eigenvalues
of \(T_0\). The first \(n\) Dirichlet eigenfunctions are admissible
trial vectors. Min–max and (7), (35) give

\[
\lambda_n\le b((n\pi/L)^2)+\|P_L+e^DI\|
=O(\log(n+2)).
\tag{36}
\]

For an orthonormal \(T_0\) eigenbasis \((e_n)\), the vectors
\(\mathcal A_0e_n\) are orthogonal with squared norms \(\lambda_n\).
Thus the nonzero singular values of the compact feedback correction
have exact squares

\[
s_n(\mathcal F_{\kappa,\mu})^2
=\frac{\kappa^2\lambda_n}{(\lambda_n+\mu)^2}
\tag{37}
\]

as a multiset. For all large \(n\), these are bounded below by a
positive constant divided by \(\log(n+2)\). The sum of any positive power of these singular values diverges,
so the correction lies outside every finite Schatten class.
This verifies that the collective response has the slow decay
required to escape the Hilbert–Schmidt obstruction.

The same estimate and (17) show that \(C_{\kappa,\mu}\) is also
outside every finite Schatten class, in particular not trace class. It is an infinite-rank compact defect, not a finite collection
of pole states or a trace-class term that can be removed by an
unexplained trace subtraction.

## 7. What this changes in the research problem

Three concrete operations now have exact physical Hilbert adjoints:
remote coherent injection supplies the signed poles, a conservative
graph supplies all prime returns, and a stable boundary response
supplies a negative contact with an explicit compact remainder. The
last operation changes the finite-translation hypothesis of note 15
and meets the necessary source regularity identified here.

Nevertheless the scalar gains and prime parameters were prescribed
to match arithmetic coefficients, and the final positive norm is
(23), not \(Q_L\). The construction uses a known positive reference
operator and elementary feedback algebra; it does not select
arithmetic positivity. Its universality as a completion should not be
mistaken for an arithmetic mechanism.

The justified next step is to derive a joint gamma-and-prime boundary
interaction or constraint whose *full* output pairing accounts for
the residual (16), with a source law compatible across supports.
Such a law must alter the coherent response, rather than add
independent positive ports, and must be checked against the
Hilbert–Schmidt and stationary-contact restrictions. Positivity of
a new block equivalent to the desired identity is still an
assumption, not the missing derivation.

The identities in this note follow directly from the previously
constructed sources and the explicitly positive response (9).
The [exact feedback program](../numerics/check_collective_feedback.py)
and [retained record](../numerics/records/collective-feedback.json)
verify the rational identities for the contact, residual, derivative
and parameter minimum. They do not verify closedness, compactness,
the Hilbert–Schmidt exclusion, or positivity of the Weil form.
