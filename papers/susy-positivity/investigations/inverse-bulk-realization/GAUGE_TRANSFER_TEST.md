# Gauge transfer and the first-prime boundary test

14 September 2026. Continuation of [inverse bulk realization](ANALYSIS.md).
The paper's direction remains a forward implication from a credible
field-theory construction and an exact pairing identity to RH.

This calculation makes four concrete advances in selecting that model.
A constructible two-dimensional Yang–Mills control rejects literal
Wilson-loop winding as the proposed prime repetition law. A positive
disk boundary operator puts the gamma masses and geometric prime
returns in one transfer system. A specified positive preparation using
its lowest mode then matches the first-prime translation coefficient
but fails the complete pairing by an unavoidable cusp at that delay.
A coherent two-component control cancels that cusp exactly, but its
Hermitian interference with the gamma source vanishes, leaving the
previous independent positive-contact problem.

The last result is an exact exclusion of this preparation, not a bound
on an error to be improved. None of the calculations constructs a
matching four-dimensional Yang–Mills observable or proves Weil positivity.

## 1. A constructible gauge-theory control

Use the heat-kernel formulation of pure two-dimensional \(SU(2)\)
Yang–Mills on the plane. It is a setting with a rigorous continuum
construction and exact Wilson-loop expectations
([Ashtekar–Lewandowski–Marolf–Mourão–Thiemann](https://arxiv.org/abs/hep-th/9605128),
[Nguyen, section 2](https://arxiv.org/html/1508.06305v3#S2)).
It is a control for the arithmetic observable, not a substitute for
four-dimensional Yang–Mills.

Normalize the positive Casimir so that the spin-\(j\) character has
eigenvalue \(j(j+1)\). Absorb the coupling and enclosed area into
\(s>0\). For the holonomy \(U\) around one simple loop,

\[
\mathbb E_s[\chi_j(U)]=(2j+1)e^{-s j(j+1)}.
\tag{1}
\]

The fundamental normalized Wilson loop traversed \(m\) times is
\(w_m(U)=\frac12\operatorname{Tr}_{\mathbb C^2}(U^m)\).
Writing the eigenvalues of \(U\) as \(e^{\pm i\vartheta}\),
\(w_m=\cos(m\vartheta)\), while
\(\chi_{n/2}=\sin((n+1)\vartheta)/\sin\vartheta\).
Therefore

\[
\mathbb E_s[w_1]=e^{-3s/4},
\qquad
\mathbb E_s[w_m]
=\tfrac12\left[
(m+1)e^{-s m(m+2)/4}
-(m-1)e^{-s m(m-2)/4}
\right]\quad(m\ge2).
\tag{2}
\]

Match the first return to \(q=p^{-1/2}\) by setting
\(s=-\frac43\log q\). The second winding is then

\[
\mathbb E_s[w_2]=\frac{3q^{8/3}-1}{2},
\tag{3}
\]

whereas the required second return is \(q^2\). These disagree for every
\(0<q<1\). Indeed, for \(y=q^{2/3}\),

\[
2(\mathbb E_s[w_2]-q^2)
=3y^4-2y^3-1
=(y-1)(3y^3+y^2+y+1)<0.
\tag{4}
\]

At prime 2, (3) is approximately \(0.0952754\), compared with the
required \(1/2\). The exact inequality (4), not that decimal example,
is the exclusion. Choosing an overall primitive-length coefficient
\(\log p\) does not repair the ratio after the first winding is fixed.

This failure extends beyond the heat generator. Suppose a central
probability convolution semigroup on \(SU(2)\) were to have
\(\mathbb E_t[w_1]=q_t=e^{-\lambda t}\) and
\(\mathbb E_t[w_2]=q_t^2\), with \(\lambda>0\).
Since \(\chi_1=1+2w_2\), its normalized spin-1 character coefficient
would have to be \(c_1(t)=(1+2q_t^2)/3\).
Central convolution requires \(c_1(t+u)=c_1(t)c_1(u)\), but

\[
c_1(t+u)-c_1(t)c_1(u)
=\frac{2}{9}(1-q_t^2)(1-q_u^2)>0.
\tag{5}
\]

Thus this whole central-semigroup winding prescription fails. This
does not exclude different gauge observables, different loop
geometries, or nontrivial correlations among several loops.

## 2. Transfer repetition is a different operation

The same positive rotor has a simple way to produce geometric returns.
On the character Hilbert space with Haar inner product, take
\(H=\frac23C_2\) and the unit vector \(\eta=\chi_{1/2}\). Then
\(H\eta=\frac12\eta\), so

\[
\langle\eta,e^{-m(\log p)H}\eta\rangle=p^{-m/2}.
\tag{6}
\]

Equation (6) evolves one representation for a longer transfer interval.
Equation (2) winds the same random holonomy repeatedly, which mixes
representations. They are different observables. A gauge construction
using transfer intervals could pass the repetition test.

Passing that scalar test is not yet a boundary norm. For example, the
literal preparation

\[
\Phi_L(f)=\int_{I_L}f(x)e^{-(b+x)H}\eta\,dx,
\qquad b>L/2,
\]

has pairing kernel
\(\langle\eta,e^{-(2b+x+y)H}\eta\rangle\), depending on \(x+y\).
The localized Weil kernel depends on \(x-y\). For a general spectral
measure of \(\eta\), write \(C(t)=\langle\eta,e^{-tH}\eta\rangle\).
If \(C(2b+x+y)\) were invariant under simultaneous small translations
of \(x,y\), then \(C'\) would vanish on an interval. Since

\[
-C'(t)=\int_{[0,\infty)}\lambda e^{-t\lambda}\,d\nu_\eta(\lambda),
\]

this forces \(\eta\) into the zero-energy subspace, leaving a constant
kernel. This proof also applies whenever the displayed Laplace
integrals are finite and differentiable at positive \(t\).

Consequently the arithmetic coordinate cannot simply be identified
with an affine Euclidean preparation time in this ansatz. Spatial,
nonlinear, normalized or extended preparations are outside this
exclusion and require their own calculation.

## 3. A positive geometric transfer system for the gamma tower

Here is an explicit common system for the gamma masses and the return
factor in (6). It is a positive rotor/boundary model, not an identification
with pure four-dimensional Yang–Mills.

Let \(\Lambda\) be the Dirichlet-to-Neumann operator of the unit disk:
harmonically extend a boundary function and take its outward normal
derivative. Use the normalized boundary measure \(d\vartheta/(2\pi)\)
and restrict to the even subspace of \(L^2(S^1)\). Its orthonormal basis
is

\[
e_0=1,\qquad e_n=\sqrt2\cos(n\vartheta)\quad(n\ge1).
\]

The harmonic extension of \(e_n\) is \(r^n e_n\), so
\(\Lambda e_n=ne_n\). The operator

\[
A=2\Lambda+\tfrac12 I
\tag{7}
\]

is independently positive and has eigenvalues
\(a_n=2n+\frac12\), exactly the gamma tower. Its quadratic form is

\[
\langle h,Ah\rangle
=\frac{2}{2\pi}\int_{\mathbb D}|\nabla u_h|^2\,d^2z
+\frac{1/2}{2\pi}\int_{S^1}|h|^2\,d\vartheta.
\tag{8}
\]

It is closed on the even \(H^{1/2}(S^1)\) trace space; the displayed
formula follows mode by mode and extends by completion. This gives
a local harmonic bulk and a positive boundary term, with no Weil
operator used in their definition. The half-unit shift and the
restriction selecting one mode per integer are specified model data,
not coefficients claimed to be forced by gauge symmetry.

For \(t>0\), the full-circle transfer is the positive Poisson operator
with parameter \(e^{-2t}\), multiplied by \(e^{-t/2}\). It preserves the
even subspace. Equivalently, with \(D=-i\partial_\vartheta\), it is a
positive subordination of the ordinary \(U(1)\) rotor heat evolution:

\[
e^{-tA}
=e^{-t/2}\frac{t}{\sqrt\pi}
 \int_0^\infty s^{-3/2}e^{-t^2/s}e^{-sD^2}\,ds.
\tag{9}
\]

The scalar Laplace identity verifies (9) on every Fourier mode.
Subordination changes the transfer generator; it does not establish
equivalence to the original Yang–Mills dynamics.

The gamma kinetic multiplier now has the exact operator expression

\[
b_{1/4}(\tau^2)
=\operatorname{Tr}_{\mathrm{even}}
 \left[\frac{2}{A}\frac{\tau^2}{A^2+\tau^2}\right].
\tag{10}
\]

For each fixed \(\tau\), the summands are \(O(n^{-3})\); the trace
converges and equals the existing positive gamma construction.
For example its closed source on each fixed-interval logarithmic
domain can be written mode by mode as

\[
(\mathcal A_nF)\widehat{\ }(\tau)
=\sqrt{\frac{2}{a_n}}\frac{i\tau}{a_n+i\tau}\widehat F(\tau),
\qquad
\sum_n\|\mathcal A_nF\|^2=K[F].
\tag{11}
\]

This is a source with the same Gram form as the two-component source
in the ground-state investigation, not an asserted identification of
their complete output spaces under arbitrary added couplings.

Let \(P_0=|e_0\rangle\langle e_0|\) and \(T_p=e^{-(\log p)A}\).
Then

\[
\operatorname{Tr}(P_0T_p^m)=p^{-m/2},
\qquad T_pT_q=T_{pq}.
\tag{12}
\]

The full trace instead gives
\(\operatorname{Tr}(T_p^m)=p^{-m/2}/(1-p^{-2m})\).
Thus the ground projection has a necessary, explicit role in the
proposed prime response. The construction supplies gamma masses and
geometric returns in the same auxiliary bulk. It does not select
primes among integers, generate the coefficient \(\log p\), or remove
mixed histories from a subsequently coupled source.

## 4. Compute a first-prime source before proposing more interactions

Test a simple positive branching of the lowest gamma mode. Put
\(a=1/2\), \(d=\log2\), \(q=e^{-ad}=2^{-1/2}\), and
\(D_q=I-qU_d\), with \(U_dF(x)=F(x-d)\) on the whole line.
For \(0\le\theta\le1\), specify the complete source

\[
\Phi_{\theta,d}F
=\left(
\{\mathcal A_nF\}_{n\ge1},
\sqrt{1-\theta}\,\mathcal A_0F,
\sqrt{\theta}\,\mathcal A_0D_qF
\right).
\tag{13}
\]

Its outputs have the ordinary positive direct-sum metric. It has the
same logarithmic domain as the gamma source: only a bounded lowest
mode is changed. This is an explicitly positive linear preparation.
The two lowest-mode outputs are orthogonal branches, so this test
does not claim a coherent interaction between them or a Yang–Mills
realization.

Since \(D_q\) commutes with the free mode resolvent,

\[
B_{\theta,d}
=K+\theta\,\frac{2}{a}
 \frac{H_x}{a^2+H_x}
 \left[q^2I-q(U_d+U_d^*)\right],
\qquad H_x=-\partial_x^2.
\tag{14}
\]

Matching the first-prime translation coefficient forces
\(\theta=ad/2=d/4\), which lies in \((0,1)\). At this value,

\[
\boxed{
B_{\theta,d}
=K+dq^2I-dq(U_d+U_d^*)+R_{a,d}.
}
\tag{15}
\]

The last operator is exactly

\[
R_{a,d}
=-da^2\bigl(q^2I-q(U_d+U_d^*)\bigr)(a^2+H_x)^{-1}.
\tag{16}
\]

Using the resolvent kernel \(e^{-a|r|}/(2a)\) and \(q=e^{-ad}\),
its convolution kernel is

\[
\boxed{
R_{a,d}(r)=\frac{ad}{2}
\begin{cases}
q^2e^{a|r|},& |r|\le d,\\
e^{-a|r|},& |r|\ge d.
\end{cases}
}
\tag{17}
\]

The expressions agree at \(|r|=d\), but their first derivatives do not:

\[
R_{a,d}'(d+)-R_{a,d}'(d-)=-da^2q\ne0.
\tag{18}
\]

Equations (14)–(18) are full identities. There is no tail expansion
or small-remainder assumption.

## 5. Why this source cannot match the full first-prime form

Compress (15) by zero extension from \(I_L\), with \(d<L<\log3\);
in particular \(L=1\) is allowed. The target in this range is

\[
W_L=K_L+w_0I+P_L-dq(V_d+V_d^*),
\]

where \(w_0=\psi(1/4)-\log\pi\) and
\(P_L(x,y)=2\cosh((x-y)/2)\).
Consequently the exact difference from the specified candidate is

\[
B_{\theta,d,L}-W_L
=(dq^2-w_0)I+E_L^*R_{a,d}E_L-P_L.
\tag{19}
\]

This cannot vanish. Near \(x-y=d\), the diagonal contact has no
support and the pole kernel is smooth, while (18) is a nonzero cusp.
The target's first-prime delta has already been matched in (15).
After removing that common delta, the remaining target kernel is
smooth near this separation. Equality of the polarized forms on
all smooth inputs would imply equality of these distribution kernels,
which is impossible.

Thus even allowing independent adjustment of a diagonal contact and
the prescribed pole terms cannot repair (13). This conclusion is
local near the first-prime delay; it does not require evaluating an
operator norm or deciding the sign of (19).

A finite positive sum of analogous orthogonal mode branches at the
same delay has the same obstruction. For mode \(a_n\), branch weight
\(\theta_n\ge0\), and attenuation \(0<q_n<1\), its resolvent correction
has derivative jump \(-2\theta_n a_nq_n\) at \(d\). Every active branch
has the same sign, so their jumps cannot cancel. This assertion concerns
finite sums with positive weights. General coherent couplings between
outputs, changes of dynamics, and coupled pole preparations are outside
this exclusion.

## 6. A coherent control: exact cancellation without a joint norm

The cusp can be cancelled by coherent readout, so it is useful to
calculate what such a repair actually accomplishes. Return to the
original two-component lowest gamma source at \(a=1/2\):

\[
\Gamma_0F=
\begin{pmatrix}
2H_x(a^2+H_x)^{-1}F\\
\partial_x(a^2+H_x)^{-1}F
\end{pmatrix},
\qquad
\Gamma_0^*\Gamma_0=\frac{4H_x}{a^2+H_x}.
\tag{20}
\]

In those same two outputs, introduce the real-parameter source

\[
Z_{u,v}F=
\begin{pmatrix}
u(U_d-U_d^*)F\\
vF+u(U_d+U_d^*)F
\end{pmatrix}.
\tag{21}
\]

The first component of \(\Gamma_0\) is self-adjoint and the second
is skew-adjoint. The corresponding components of \(Z\) are
skew-adjoint and self-adjoint, respectively. All these operators
commute on the line. Hence the complete Hermitian cross term is
exactly zero:

\[
\Gamma_0^*Z+Z^*\Gamma_0=0.
\tag{22}
\]

Also the shifts by \(2d\) cancel between the two output norms:

\[
Z^*Z=(v^2+4u^2)I+2uv(U_d+U_d^*).
\tag{23}
\]

Adding (21) coherently to the lowest mode, and retaining the other
gamma modes, therefore gives

\[
B_{\mathrm{coh}}=K+C I-dq(U_d+U_d^*),
\quad
2uv=-dq,\quad C=v^2+4u^2.
\tag{24}
\]

There is no displaced continuous response in (24). Its contact satisfies
\(C-2dq=(v+2u)^2\ge0\), with equality for
\(u=\frac12\sqrt{dq}\), \(v=-\sqrt{dq}\).
This is the ordinary positive first-prime jump norm in a coherent
output representation. The minimum stated here belongs to this
whole-line stationary source class; it is not a sharp claim for every
finite-interval realization.

On the first-prime interval, the exact comparison is now simply

\[
B_{\mathrm{coh},L}-W_L=(C-w_0)I-P_L.
\tag{25}
\]

It cannot vanish: \(C-w_0>0\), whereas \(P_L\) has rank at most two
on the infinite-dimensional input space. Thus this coherent repair
passes the cusp test and still fails the full contact-and-pole test.
It does not supply an arithmetic interaction in the Hermitian norm:
equation (22) makes its Gram form exactly the sum of the gamma and
independent jump pairings.

## 7. What the next junction must accomplish

The disk model provides a fully defined positive auxiliary mass operator,
a source for the gamma norm, and transfer operations with the required
geometric returns. It is a constructive comparison model. Relating
these operations to a pure Yang–Mills observable remains open.

The two explicit preparations give successive exact constraints.
The coupling must retain the prime translation atom while cancelling
the displaced continuous response. It must also have a nonzero joint
Hermitian contribution that determines the contact and poles within
the same complete positive pairing. More orthogonal positive branches
of the tested type fail the first requirement. The coherent control
(21) passes that requirement and fails the second.

The next bounded calculation should specify a junction and its physical
adjoint with nonvanishing gamma/return interference, then solve the
cusp, contact and pole identities together. Repetition and mixed-prime
conditions follow only after that full first-prime mechanism is fixed.
No claim of novelty is made for the underlying heat kernels, Poisson
semigroup or disk spectrum. The outputs of this pass are the explicit
comparison calculations and scoped exclusions above.

The [checks](check_gauge_transfer.py) and their
[record](gauge-transfer-checks.json) verify finite algebra underlying
these identities. They are not a constructive field-theory proof
checker or a Weil positivity certificate.
