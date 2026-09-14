# Conservative prime returns and their sharp contact cost

13 September 2026. This note specifies a positive quantum-graph return
channel before calculating its arithmetic response. A finite normalized
quartic cap labels the channel; the graph supplies infinitely many
excited states. A single coherent output reproduces every repetition of
one prime, including the negative translation signs, with an exactly
computed positive contact. A sharp bound then shows that interference
among arbitrary stationary channels cannot lower that contact while
preserving the same complete prime kernel on the line.

This is a physical realization of the known positive prime reference,
not a realization of the full Weil form. The new content is the explicit
conservative coupling, its positive Hamiltonian and source, the
distinction between its output norm and its scattering-phase or Euler
logarithmic derivative, and the contact bound with its finite-support
qualification. The independent-jump divergence in notes 00 and 03 is
not being presented as a new obstruction.

## 1. Fix the finite channel and the positive bulk

Use the homogeneous quartic of [note 10](10_REFLECTED_BOUNDARY_PAIRING.md),

\[
f_0=(Z^4+W^4+Z^2W^2)/16,\qquad
s_0=Z^2+W^2,\qquad \lambda=256\pi^2/3.
\]

Its independently prepared cap

\[
e=\lambda^{-1/2}h_{f_0}(s_0\,dZ\wedge dW)
\tag{1}
\]

has exactly unit physical norm. This uses the evaluated middle-source
norm, not the unknown other entries of the vacuum metric. Every graph
channel below may carry this same internal label. The channel index and
its spatial wavefunction are additional degrees of freedom, so the
prepared range is not confined to the quartic vacuum space.

Fix numbers \(0<q<1\) and \(d>0\). The prime choice will be
\(q=p^{-1/2}\), \(d=\log p\). Take a metric graph with two semi-infinite
leads and one finite stub of length \(d/2\), joined at a degree-three
vertex. At the closed stub endpoint impose Neumann boundary conditions.
Define the real symmetric matrix

\[
O_q=
\begin{pmatrix}
1-q&\sqrt q&\sqrt{q(1-q)}\\
\sqrt q&0&-\sqrt{1-q}\\
\sqrt{q(1-q)}&-\sqrt{1-q}&q
\end{pmatrix},\qquad O_q^2=I.
\tag{2}
\]

Put \(P_-=(I-O_q)/2\), \(P_+=(I+O_q)/2\). These are orthogonal
projections. With coordinates increasing away from the junction, the
positive closed quadratic form is

\[
\mathfrak h_q[\psi]=\sum_{j=1}^3\int_{e_j}|\psi'_j(s)|^2\,ds,
\qquad
\mathcal D(\mathfrak h_q)=
\{\psi\in\bigoplus_jH^1(e_j):P_-\psi(0)=0\}.
\tag{3}
\]

The Neumann stub endpoint is natural in this form. Trace continuity
makes its domain closed in the graph \(H^1\) norm. The associated
self-adjoint Hamiltonian is \(-\partial_s^2\ge0\), with junction
conditions

\[
P_-\psi(0)=0,\qquad P_+\psi'(0)=0.
\tag{4}
\]

There is no unknown target operator in (2)–(4). Tensoring with the
quartic Hamiltonian gives a positive Hamiltonian with the cap (1) as
its internal ground label and the graph continuum as its accessible
excited sector. This construction does not assert an interacting
arithmetic coupling between the two factors or an additional set of
supercharges.

For an incoming and outgoing plane-wave pair
\(a_j e^{-iks}+b_j e^{iks}\), \(k>0\), (4) gives
\(P_-b=-P_-a\), \(P_+b=P_+a\), hence

\[
b=O_q a.
\tag{5}
\]

Thus the vertex scattering matrix is exactly the specified orthogonal
coupler. The self-adjoint quantum-graph scattering framework and the
composition of internal propagation with vertex scattering are
standard; see [Kostrykin–Schrader, *Kirchhoff's Rule for Quantum Wires*](https://arxiv.org/abs/math-ph/9806013).
For this particular graph the positive form and scattering calculation
are given explicitly above, so no general inverse-realization theorem
is being used to manufacture an arithmetic scattering function.

## 2. Eliminate the stub and retain the ordinary physical adjoint

Write (2) in blocks

\[
O_q=\begin{pmatrix}D&B^T\\B&q\end{pmatrix},\qquad
D=\begin{pmatrix}1-q&\sqrt q\\\sqrt q&0\end{pmatrix},
\quad B=\sqrt{1-q}\,(\sqrt q,-1).
\tag{6}
\]

The Neumann endpoint returns a traveling amplitude with round-trip
phase \(z=e^{ikd}\). If \(a,b\in\mathbb C^2\) are the external input
and output, and \(v\) is the amplitude launched into the stub, the
boundary equations are

\[
v=Ba+qzv,\qquad b=Da+B^Tzv.
\tag{7}
\]

Since \(q<1\), they have a unique solution for every real \(k\). The
external scattering matrix is

\[
V_q(z)=D+\frac{z}{1-qz}B^TB
=\frac1{1-qz}
\begin{pmatrix}
1-q&\sqrt q(1-z)\\
\sqrt q(1-z)&(1-q)z
\end{pmatrix}.
\tag{8}
\]

For \(|z|=1\), direct multiplication gives

\[
V_q(z)^\dagger V_q(z)=I,\qquad
\det V_q(z)=\frac{z-q}{1-qz}.
\tag{9}
\]

No absorption has been introduced: \(q\) is the internal return
amplitude of a lossless coupler, with the other amplitudes carrying
the escaping flux. Keeping only the second outgoing lead is an
ordinary orthogonal projection of a unitary scattering output.

For the first external input, its two output multipliers are

\[
K_0(z)=\frac{1-q}{1-qz},\qquad
K_1(z)=\frac{\sqrt q(1-z)}{1-qz},\qquad
|K_0(z)|^2+|K_1(z)|^2=1.
\tag{10}
\]

Now put \(U=U_d\), \((U_dF)(x)=F(x-d)\), in \(L^2(\mathbb R,dx)\),
and specify the scaled observed source

\[
\boxed{\quad
\mathcal D_{q,d}F=
\sqrt{\frac{dq(1+q)}{1-q}}\,
(I-U)(I-qU)^{-1}F\ \otimes e.
\quad}
\tag{11}
\]

Here \((I-qU)^{-1}=\sum_{n\ge0}q^nU^n\) converges in operator norm.
The input scale \(\sqrt{d(1+q)/(1-q)}\) multiplying the passive output
\(K_1\) is explicit. It fixes the desired coefficient \(d\) after
gluing; it is additional source data, not a normalization forced by
the quartic Hamiltonian alone.

The variable \(x\) is the arithmetic coordinate dual to wavenumber;
it is not being identified with the Schrödinger evolution time. For
a literal graph scattering preparation of arbitrary complex \(F\),
use two copies of the graph, feed the first incoming lead with
\(\widehat F(k)/\sqrt{2\pi}\) in one copy and
\(\widehat F(-k)/\sqrt{2\pi}\) in the other, \(k>0\), and retain
their second outgoing leads. Both copies have energy \(k^2\ge0\).
The resulting complex-linear map has the same polarized Gram form as
(11), because \(|K_1(e^{ikd})|^2\) is even in \(k\). This supplies
all Fourier inputs without assigning a two-sided unbounded-below
momentum operator the role of a positive physical Hamiltonian.

The physical adjoint in the output representation (11) contracts the
internal label against \(e\) and applies

\[
\mathcal D_{q,d}^*
=\sqrt{\frac{dq(1+q)}{1-q}}\,
(I-qU^*)^{-1}(I-U^*)
\tag{12}
\]

to that component. Both operators have domain all of \(L^2\). On
an interval the source is \(\mathcal D_{q,d}E_L\), with adjoint
\(E_L^*\mathcal D_{q,d}^*\); the propagation and stub are unchanged
as the support length changes.

## 3. The exact coherent prime Gram form

For \(z=e^{-i\tau d}\), let

\[
\Pi_q(z)=\frac{1-q^2}{|1-qz|^2}
=1+\sum_{m\ge1}q^m(z^m+z^{-m}).
\tag{13}
\]

The elementary identity

\[
q|1-z|^2+(1-q)^2=|1-qz|^2
\tag{14}
\]

gives

\[
\mathcal D_{q,d}^*\mathcal D_{q,d}
=\frac{d(1+q)}{1-q}I-d\Pi_q(U)
=\frac{2dq}{1-q}I
-d\sum_{m\ge1}q^m(U^m+U^{*m}).
\tag{15}
\]

Therefore, for all \(F,G\in L^2(\mathbb R)\),

\[
\boxed{\quad
\langle\mathcal D_{q,d}F,\mathcal D_{q,d}G\rangle
=\frac{2dq}{1-q}\langle F,G\rangle
-d\sum_{m\ge1}q^m
\bigl(\langle F,U^mG\rangle+\langle F,U^{*m}G\rangle\bigr).
\quad}
\tag{16}
\]

The sums converge absolutely in operator norm. For the prime values,

\[
dq^m=(\log p)p^{-m/2},\qquad
c_p:=\frac{2dq}{1-q}=\frac{2\log p}{\sqrt p-1}.
\tag{17}
\]

Thus one coherent infinite-output channel, rather than independent
outputs for every repetition, gives all the required negative prime
translations. Its compulsory diagonal is exactly the positive-jump
contact already present in notes 00 and 03. The construction passes
the finite-vacuum rank test because its continuum output is infinite
dimensional. Each prime source is bounded, as it should be for the
bounded finite-support prime contribution; the gamma source must
still carry the unbounded logarithmic domain.

For reference, the exact whole-line norm is
\(\|\mathcal D_{q,d}\|^2=4dq/(1-q^2)\), attained as a multiplier
supremum at \(\tau d=\pi\) modulo \(2\pi\). No such equality is
asserted for a fixed interval compression.

For a finite prime set \(\mathcal S\), the source

\[
\mathcal A_{\mathcal S,L}f
=\mathcal A_\gamma E_Lf\ \oplus
\bigoplus_{p\in\mathcal S}\mathcal D_pE_Lf
\tag{18}
\]

is closed on exactly \(\mathcal D_{\log,L}\) from
[note 11](11_CLOSED_ARITHMETIC_SOURCE.md), because it adds bounded
components to the closed gamma preparation. Its compactly supported
smooth core is unchanged. Its Gram form is precisely the known
\(J_{\mathcal S,L}\), and the full arithmetic comparison remains

\[
Q_L[f]=\|\mathcal A_{\mathcal S,L}f\|^2
+\left(w_0-\sum_{p\in\mathcal S}c_p\right)\|f\|^2
+2|C(f)|^2-2|S(f)|^2,
\tag{19}
\]

provided every prime active on \(I_L\) belongs to \(\mathcal S\).
Equation (19) does not turn its last three terms into a positive
gluing or derive them from the graph.

## 4. A sharp contact bound that allows coherent channels

Let \(\mathcal S\) be any finite prime set. Suppose an ordinary
positive source, with arbitrarily many interacting or coherent output
channels, has the following whole-line Gram operator:

\[
A^*A=cI-
\sum_{p\in\mathcal S,m\ge1}
(\log p)p^{-m/2}
(U_{m\log p}+U_{m\log p}^*).
\tag{20}
\]

Only the displayed Gram operator is assumed stationary. The source
itself need not be a direct sum of prime channels. The equality is
understood first on a dense smooth core; since the right side is
bounded, the source extends boundedly there if it is to have this
norm.

The Fourier multiplier is continuous. It is smallest at
\(\tau=0\), because every cosine is at most one and all weights are
positive. A Fourier packet concentrated near zero tests that minimum.
Consequently

\[
\boxed{\qquad A^*A\ge0
\quad\Longleftrightarrow\quad
c\ge\sum_{p\in\mathcal S}\frac{2\log p}{\sqrt p-1}.
\qquad}
\tag{21}
\]

The direct sum of (11) attains equality. This proves a stronger
statement than divergence for independent jump squares: coherent
multiport mixing cannot reduce the scalar contact if its final Gram
operator retains exactly the prescribed prime translations and no
additional off-diagonal terms. Any mixed delays or other kernels
produced by a more complicated network have to be kept and matched;
they cannot silently be discarded when applying (21).

The assertion is about this stationary prime sector. It does not
exclude a coupled construction involving the gamma and pole terms,
nonstationary intermediate kernels, or a physical constraint that
changes the complete gluing identity. In particular it is not a
general no-go theorem for positive quantum theories.

### Fixed finite supports have a different sharp constant

The whole-line hypothesis matters. For a single \((q,d)\) on an
interval of length \(L\), split positions into residue classes modulo
\(d\). Almost every fiber is a finite chain. Its longest length on a
set of positive measure is \(n=\lceil L/d\rceil\), and the prime
translation operator on such a fiber is

\[
d(R_n(q)-I),\qquad
R_n(q)_{ij}=q^{|i-j|},\quad 1\le i,j\le n.
\tag{22}
\]

Thus the smallest scalar contact for positivity after this one
compression is

\[
c_{q,d,L}=d\bigl(\lambda_{\max}(R_n(q))-1\bigr).
\tag{23}
\]

Smaller fibers are principal submatrices, so none raises the maximum.
For \(L\le d\), (23) is zero. For \(d<L\le2d\), it is \(dq\),
strictly below the whole-line constant \(2dq/(1-q)\). These are exact
finite-matrix statements, not numerical positivity evidence for
\(Q_L\).

The row-sum bound gives
\(\lambda_{\max}(R_n)\le(1+q)/(1-q)\), while the normalized constant
vector has Rayleigh quotient

\[
1+2\sum_{m=1}^{n-1}(1-m/n)q^m
\longrightarrow\frac{1+q}{1-q}.
\tag{24}
\]

Hence (23) increases to the contact in (21) as supports grow. Choosing
a separate minimal scalar contact for each interval does not give a
support-compatible source pairing: the scalar coefficient on an
already supported input changes when that input is embedded in a
larger interval. Formula (23) explains the scope of the obstruction
without assuming fixed-prime positivity for the complete Weil form on
arbitrarily large supports.

## 5. Output norms and logarithmic derivatives are different observables

The denominator in (8) is the Euler return denominator. That fact
does not identify its logarithmic derivative with a positive source
norm. Let

\[
Z_{q,d}(s)=\frac1{1-e^{-sd}},\qquad
s=\tfrac12+i\tau,\qquad q=e^{-d/2}.
\]

Then

\[
2\Re\,\partial_s\log Z_{q,d}(s)
=-2d\sum_{m\ge1}q^m\cos(m\tau d)
=d-d\Pi_q(e^{i\tau d}).
\tag{25}
\]

This is the signed prime multiplier with zero contact. It is negative
at \(\tau=0\), so it cannot alone be the norm of the graph output.
The actual norm (15) has the additional contact \(2dq/(1-q)\).

The scattering phase supplies a second exact comparison. From (9),

\[
\frac{d}{dk}\arg\det V_q(e^{ikd})
=d\Pi_q(e^{ikd})>0.
\tag{26}
\]

More explicitly, the Wigner–Smith matrix obtained by differentiating
the already specified scattering law is

\[
-iV_q(e^{ikd})^\dagger\frac{d}{dk}V_q(e^{ikd})
=\frac{d}{|1-qe^{ikd}|^2}B^TB\ge0.
\tag{27}
\]

Its trace is (26), since \(BB^T=1-q^2\). These formulas follow
directly from (6)–(8). They describe the derivative with respect to
wavenumber; converting to an energy derivative adds the factor
\(1/(2k)\). No claim about a general time-delay positivity theorem is
needed.

Thus the negative arithmetic prime response is the constant \(d\)
minus the positive trace density (26). It is a relative response,
not the output power or the physical Gram matrix. The coherent source
(11) replaces that insufficient constant \(d\) by the maximum
\(d(1+q)/(1-q)\), exactly as (21) requires. A logarithmic determinant,
a trace or phase derivative, and an ordinary norm must remain
distinguished even when all of them contain the same Euler
denominator.

## 6. All-prime limits and the next missing interaction

For a nonzero input supported in an interval of length \(L\), every
prime with \(\log p\ge L\) has zero translation overlaps at every
repetition. Nevertheless (16) gives

\[
\|\mathcal D_pE_Lf\|^2=c_p\|f\|^2.
\tag{28}
\]

The sum of \(c_p\) over primes diverges. For example
\(c_p=2\log p/(\sqrt p-1)\ge1/p\), and Euler's elementary divergent
prime reciprocal sum suffices; no prime number asymptotic is needed.
Therefore the unrenormalized all-prime direct sum of these coherent
graph outputs has no nonzero compactly supported source in its domain.
The source (18) remains well defined for finite \(\mathcal S\).

This recovers the old divergence under a substantially more coherent
physical realization. More generally, (21) shows that any finite
stationary prime realization with the same exact off-diagonal kernel
must pay at least the same divergent contact. Adding primes when the
support grows changes the positive reference norm on earlier inputs;
the subtraction in (19) is exactly what restores compatibility of
the signed arithmetic form.

The concrete result is therefore a calibrated finite-channel,
infinite-state prime preparation with a physical adjoint and positive
bulk Hamiltonian. Its failure is also concrete: passivity generates
the minimal positive contact, whereas the Weil form requires the fixed
\(w_0\), together with the signed poles. Simply replacing independent
prime jumps by coherent cavities does not resolve this difference.
The next mechanism must derive the contact reduction and pole
interference jointly with the gamma and prime source, through a
specified coupling or constraint. The cap, loop and logarithmic
derivative formulas above do not provide that missing gluing law.

All operator and scattering identities in this note are direct
calculations for the specified model. They do not certify full Weil
positivity, claim a new general realization theorem, or replace the
analytical review needed for the broader investigation.

The standard-library [prime return algebra program](../numerics/check_prime_returns.py)
and its [retained record](../numerics/records/prime-returns.json) replay
seven exact polynomial checks of the coupler, stub elimination,
unitarity, determinant, complementary powers, contact and
Wigner–Smith formulas. They do not test scattering completeness,
source domains or the analytical contact bound.
