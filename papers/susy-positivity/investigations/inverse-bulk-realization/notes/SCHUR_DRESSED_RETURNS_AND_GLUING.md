# Dressed Schur returns: an exact local norm and its gluing requirements

14 September 2026. **Focused continuation** of
[sphere and Schur pairings](SPHERE_AND_SCHUR_PAIRINGS.md). The broad
candidate comparison remains in the [survey](DEFECT_OBSERVABLE_SURVEY.md).

There is a concrete improvement over the first tests. In the elementary
Schur representation, an explicit electric dressing followed by one
magnetic insertion gives a positive norm with the exact negative
prime-power coefficients. All primes can use one fixed quantization
parameter. The full norm also fixes a positive contact term; it realizes
the known positive prime reference, not the complete Weil form.

Two further calculations narrow the continuation. The dressed states
have only a specified magnetic domain, and a simple coherent sum of two
return filters generates forbidden mixed returns. The next fit must
therefore use an actual joint gauge/interface construction. Neither
result calls for estimating increasingly complicated residual terms.

## 1. Fix the theory data and distinguish the two parameters

Throughout, \(0<q<1\) is one fixed Schur quantization parameter. For an
arithmetic prime \(p\), use the separate boundary data

\[
r_p=p^{-1/2},\qquad d_p=\log p.
\tag{1}
\]

The calculation takes place in the elementary \(q\)-Weyl representation
associated with SQED with one hypermultiplet. It is a protected-sector
control, not an identification with the full conformal \(SU(2),N_f=4\)
theory. The latter remains the nonabelian benchmark.

Use \(\mathcal H=\ell^2(\mathbb Z)\otimes L^2(S^1,d\theta/(2\pi))\),
write \(\zeta=e^{i\theta}\), and denote magnetic charge by \(m\).
The model data needed here are

\[
\begin{split}
(v\psi)_m(\zeta)&=q^{-m}\zeta\psi_m(\zeta),\\
(u_-\psi)_m(\zeta)&=(1+q^{-m-1}\zeta)
\psi_{m+1}(q^{-1}\zeta),\\
(u_+\psi)_m(\zeta)&=\psi_{m-1}(q\zeta),\\
(\Omega_q)_m(\zeta)&=C_q\delta_{m0}\chi_q(\zeta),\\
\chi_q(\zeta)&=(-q\zeta;q^2)_\infty^{-1},\qquad
C_q=(q^2;q^2)_\infty.
\end{split}
\tag{2}
\]

Here \((b;Q)_\infty=\prod_{j\geq0}(1-bQ^j)\). The normalization and
actions in (2) are those of
[Gaiotto–Teschner, Schur RG flow, §3.1.1](https://arxiv.org/html/2503.16685#S3.SS1.SSS1).
The physical adjoints are inherited from the doubled representation;
no assertion that \(u_-\) is the ordinary adjoint of \(u_+\) is used.

Complex shifts in (2) must be interpreted on an operator domain. A
meromorphic expression which happens to have finite boundary values
after crossing a pole is not automatically the action of that operator.
The source below is checked before applying its magnetic insertion.

## 2. An admissible electric dressing removes the descendant factors

For \(0<a<1\), define on the zero-charge sector

\[
D_{q,a}(\zeta)=\frac{\sqrt{1-a^2}}{C_q}
\frac{(-q\zeta;q^2)_\infty}{1+a\zeta}.
\tag{3}
\]

This is an analytic function on a neighbourhood of the closed unit disk,
with a uniformly convergent electric-line expansion there. It is bounded
on that sector. It need not be a bounded operator on all magnetic sectors.
Acting on the given state, it yields

\[
\eta_a=D_{q,a}(v)\Omega_q,
\qquad (\eta_a)_m(\zeta)=
\delta_{m0}\frac{\sqrt{1-a^2}}{1+a\zeta},
\qquad \|\eta_a\|=1.
\tag{4}
\]

Thus, in Fourier coefficients, \(\eta_a=\sqrt{1-a^2}
\sum_{n\geq0}(-a)^n|0,n\rangle\). Multiplication by \(-v\) on this
sector has the exact normalized returns

\[
\langle\eta_a,(-v)^k\eta_a\rangle=a^{|k|},\qquad k\in\mathbb Z.
\tag{5}
\]

This changes the source, not the Hilbert metric. It resolves the
descendant mismatch of the undressed state computed in the preceding
note. Since \(a\) is a source parameter, (5) does not require varying
\(q\) between primes.

The preparation (3) is an infinite electric-line observable in a Hilbert
completion, rather than a single polynomial line operator. This extra
observable choice is explicit. It has not been derived as the unique
boundary condition of a new UV theory or from a rule selecting primes.

## 3. One magnetic insertion gives the signed prime coefficients

### 3.1 Check the magnetic action on the state

Take \(a=qr\), where \(0<r<1\). The state (4) is in the domain needed
for one negative magnetic insertion: its coefficients after the
\(q^{-1}\) shift decay geometrically with ratio \(r\). Equation (2)
therefore gives

\[
(u_-\eta_{qr})_m(\zeta)=\delta_{m,-1}\sqrt{1-q^2r^2},
\frac{1+\zeta}{1+r\zeta}.
\tag{6}
\]

The Fourier coefficients, without the common square root, are
\(b_0=1\) and \(b_n=(1-r)(-r)^{n-1}\) for \(n\geq1\). Consequently

\[
\|u_-\eta_{qr}\|^2=\frac{2(1-q^2r^2)}{1+r}.
\tag{7}
\]

There is also a graph-domain argument using actual line states.
Since \(a<q\), the Taylor polynomials \(D_N\) of (3) converge uniformly
on a disk of radius greater than \(q^{-1}\). Both \(D_N(v)\Omega_q\)
and \(u_-D_N(v)\Omega_q\) converge in norm to (4) and (6), respectively;
for the second convergence use
\((1+\zeta)\chi_q(q^{-1}\zeta)=\chi_q(q\zeta)\).
Thus the source is in the graph closure of this algebraic action, and
every closed physical extension of that action has the displayed value.

The factor \(1+\zeta\) comes from the actual magnetic operator. Its
interference with the geometric tail changes the sign of the return
coefficients after setting \(z=-\zeta\).

For finite Laurent polynomials \(h\), define the linear preparation

\[
\Phi_{q;r,d}[h]=
\beta_{q;r,d}\,h(-q^{-1}v)u_-D_{q,qr}(v)\Omega_q,
\quad
\beta_{q;r,d}^2=
\frac{dr(1+r)}{(1-r)(1-q^2r^2)}.
\tag{8}
\]

On the final sector \(m=-1\), \(v=q\zeta\), so the argument
\(-q^{-1}v\) is exactly \(z=-\zeta\). This factor of \(q\) is required
by the representation; using \(h(-v)\) would give a different source.
The positive overall source normalization in (8) uses the stated
boundary data \((r,d)\). It does not alter a contact term separately.

### 3.2 Compute the entire norm

The full polarized pairing is

\[
\langle\Phi[h],\Phi[k]\rangle=
\int_{S^1}\overline{h(z)}k(z)\,w_{r,d}(z)\frac{d\theta}{2\pi},
\qquad
w_{r,d}(z)=\frac{dr(1+r)}{1-r}
\frac{|1-z|^2}{|1-rz|^2}.
\tag{9}
\]

In particular it is positive. Direct Fourier expansion gives

\[
w_{r,d}(z)=\kappa_{r,d}
-d\sum_{n\geq1}r^n(z^n+z^{-n}),
\qquad \kappa_{r,d}=\frac{2dr}{1-r}.
\tag{10}
\]

Equivalently, on the Laurent basis,

\[
\langle\Phi[z^j],\Phi[z^k]\rangle=
\begin{cases}
\kappa_{r,d},&j=k,\\
-dr^{|j-k|},&j\ne k.
\end{cases}
\tag{11}
\]

This is a positive norm identity, not a logarithmic derivative of a
partition function. For \(r=p^{-1/2}\), \(d=\log p\), every nonzero
coefficient in (10) is precisely the required prime coefficient. The
same \(q\) works for all primes because \(a_p=q/\sqrt p<q\).

The diagonal is equally part of the result. It is positive and fixed by
the preparation. It cannot be discarded while retaining positivity.
Indeed, a translation-invariant scalar form with these off-diagonal
coefficients and a constant diagonal \(C\) is nonnegative on the full
line only if \(C\geq2dr/(1-r)\), by evaluating its continuous multiplier
at zero. The form (9) attains equality. This is the already known sharp
contact of the positive prime reference; the advance here is its explicit
Schur realization and checked source domain.

### 3.3 Lift the circle calculation to the logarithmic arithmetic input

The circle identity must not be mistaken for a real translation without
a source map. One explicit Hilbert-space lift is the unitary decomposition

\[
(\mathcal B_dF)_j(\theta)=d^{-1/2}
\widehat F\bigl((\theta+2\pi j)/d\bigr),\qquad j\in\mathbb Z,
\tag{12}
\]

from \(L^2(\mathbb R,dx)\) to
\(L^2(S^1,d\theta/(2\pi);\ell^2(\mathbb Z))\). Here
\(\widehat F(\tau)=\int e^{-i\tau x}F(x)\,dx\). Apply (9) to each
component of (12). Its sum is exactly

\[
\begin{split}
B_{r,d}[F]
&=\frac1{2\pi}\int_{\mathbb R}w_{r,d}(e^{id\tau})
|\widehat F(\tau)|^2\,d\tau\\
&=\kappa_{r,d}\|F\|^2
-2d\sum_{n\geq1}r^n\operatorname{Re}\langle F,U_{nd}F\rangle,
\qquad U_sF(x)=F(x-s).
\end{split}
\tag{13}
\]

The conjugation of the Fourier multiplier for \(U_d\) has no effect
because (10) contains both orientations. For zero-extended inputs
supported in \(I_L\), only terms with \(nd<L\) remain.

Equation (12) explicitly adds a multiplicity space and a boundary
preparation. It does not identify that multiplicity with magnetic flux,
or prove that a particular 4D interface implements the lift. The result
is a precise positive Hilbert-space realization of the local reference
with a Schur operator factor. Its promotion to one field-theoretic
boundary construction remains part of the matching problem.

## 4. The magnetic domain places a useful restriction on further gluing

The finite-norm condition for one insertion does not license every
negative magnetic power. Iterating the coefficient action in (2) gives

\[
(u_-^k\eta_a)_{-k}(\zeta)=\sqrt{1-a^2}
\frac{\prod_{j=0}^{k-1}(1+q^{k-1-2j}\zeta)}
{1+aq^{-k}\zeta}.
\tag{14}
\]

This is first an identity of formal Fourier series. Beyond the numerator
degree, its coefficients are a nonzero constant times
\((-aq^{-k})^n\), unless the numerator cancels the pole. The cancelling
factor is characterized exactly by

\[
\prod_{j=0}^{k-1}(1-q^{2j+1}/a)=0.
\tag{15}
\]

Therefore the coefficient sequence belongs to \(\ell^2\) exactly when

\[
a<q^k\quad\text{or}\quad
a\in\{q,q^3,\ldots,q^{2k-1}\}.
\tag{16}
\]

For a fixed \(a>0\), compatibility with **all** negative magnetic powers
requires \(a=q^{2j+1}\) for some \(j\geq0\). At these exceptional values
the formal outputs are square summable for every power; this alone is
not a proof about a chosen unbounded operator extension. Away from them,
the divergent output coefficients are a necessary domain obstruction in
any realization with the stated action.

For the prime preparations \(a_p=qr_p\), requiring all powers would
force \(r_p=q^{2j_p}\). This cannot hold for both 2 and 3 at one fixed
\(q\). It does **not** invalidate (8): that observable needs only one
magnetic insertion, which was checked directly. Any specified finite
number \(K\) of powers is simultaneously allowed for all primes by
choosing \(q\) sufficiently close to one, for example
\(q^{K-1}>2^{-1/2}\) when \(K>1\).

The practical lesson is to specify the actual word of line operators
used by a proposed junction. Do not apply an unrestricted hierarchy of
Ward identities to these source states. Conversely, construction of a
QFT does not require every state to lie in the domain of every power of
every unbounded observable, so (16) is not an exclusion of the theory.

## 5. The first two-prime test excludes constant-vector coherent gluing

The scalar return filter appearing in (9) is

\[
A_p(z)=\frac{1-z}{1-r_pz}
=1-(1-r_p)\sum_{n\geq1}r_p^{n-1}z^n.
\tag{17}
\]

Consider the following specific attempt to share outputs between two
primes: use the amplitudes
\(\sqrt{c_p}A_p(e^{id_p\tau})v_p\), where
\(c_p=d_pr_p(1+r_p)/(1-r_p)\), and \(v_p\) are fixed unit vectors in
one output Hilbert space. Square the norm of their sum against
\(\widehat F(\tau)\).

The cross term for \(p=2\), \(p=3\) has a nonzero Fourier coefficient
at the mixed length \(\log3-\log2\) whenever
\(\langle v_2,v_3\rangle\ne0\). In the Fourier convention used here, that
coefficient is

\[
\sqrt{c_2c_3}\,(1-r_2)(1-r_3)\langle v_2,v_3\rangle.
\tag{18}
\]

No other pair of positive repetition indices gives this length, by
unique factorization. More generally the cross terms contain
\(n\log2-m\log3\), \(m,n\geq1\), rather than just prime powers.
The coefficient series is absolutely summable, so these are genuine
atoms, even though other mixed lengths can accumulate near them.
Neither the smooth gamma kernel away from zero nor the smooth pole
kernel can cancel an atom at \(\log(3/2)\).

This mixed return lies inside the two-prime interval \(L=5/4\), but is
absent from the Weil target. A purely imaginary overlap does not solve
the problem: it gives an imaginary antisymmetric kernel detected by
complex inputs. For this fixed-vector ansatz, eliminating the mixed
atoms requires \(v_2\perp v_3\), returning to the orthogonal sum of
the separate contacts.

This excludes that simple coherent gluing prescription. It does not
exclude an operator-valued junction whose additional terms cancel
mixed returns as an identity. Such a junction is a new model/source
choice, not a reason to bound the unwanted terms in (18).

## 6. Compare with the full target and decide what to pursue

Let \(K_L\) be the positive gamma form, \(w_0=\psi(1/4)-\log\pi<0\),
and let \(P_L\) be the two signed pole contributions, with conventions
as in [the preceding note](SPHERE_AND_SCHUR_PAIRINGS.md). For a finite
set \(\mathcal P\) containing all primes below \(e^L\), (13) gives
the exact identity

\[
Q_L[f]=K_L[f]+\sum_{p\in\mathcal P}B_{r_p,d_p}[E_Lf]
+\left(w_0-\sum_{p\in\mathcal P}\kappa_{r_p,d_p}\right)\|f\|^2
+P_L[f].
\tag{19}
\]

This has the same unresolved contact and pole problem as the
[conservative graph realization](../../arithmetic-ground-state-geometry/notes/16_PRIME_RETURN_CHANNELS.md).
It would be circular to declare the last line positive or to subtract
it from a norm by definition. The present result does not improve a
positivity interval or replace that problem with a smaller error bound.

The comparison is nevertheless useful. We now have a genuine Schur
source calculation supplying the full local positive reference, with
its real adjoint inherited from a known representation and with a
single \(q\). The older failures of bare windings, undressed Schur
states, or changing \(q\) per prime are not obstructions to this source.
The remaining work can focus on the joint arithmetic preparation.

The sphere Gaussian/oscillator module continues to supply the
archimedean normalization control. Taking its positive source in an
orthogonal sum with (8), after the lift (12), gives the reference in
(19); changing
the description of those independent pieces cannot change the contact.

For the interacting Schur benchmark, the next useful object is a
gauge-invariant, charge-neutral RG/interface preparation in the
\(SU(2),N_f=4\) theory. Its magnetic generator contains two shifted
terms and a neutral coefficient \(C_0(v)\), and its Hilbert space has a
Weyl constraint. Those terms are potential sources of the required
joint interference, but none may be dropped or identified with the
elementary abelian calculation without a derivation.
[Gaiotto–Teschner, §§5.1.2–5.1.3](https://arxiv.org/html/2406.09171#S5.SS1.SSS2)

Specifically, compute a proposed neutral line/interface word and its
whole pairing, including the neutral term and Weyl projection, before
assigning it the arithmetic source. Test its compatibility with the
gamma/pole normalization and the absence of the mixed atom in (18).
The alternative sphere direction is a boundary/vortex module with an
actual correspondence on the Gaussian control, rather than a further
independent positive summand.

No system-specific paper is warranted yet. The new result is an exact
local source realization and two scoped selection tests. The known
positive prime reference is not being claimed as new mathematics, and
the arithmetic prime labels and continuous-input lift are still supplied
as boundary data rather than derived from a full QFT construction.

## 7. Checks

[check_dressed_schur.py](../numerics/check_dressed_schur.py) and its
[record](../numerics/records/dressed-schur-checks.json) verify the finite
coefficient algebra, the magnetic action with its truncation boundary,
the norm and Fourier coefficients, the higher-power cancellation
polynomial, and the uniqueness of the first mixed return in a finite
integer sample. The latter supports, rather than replaces, the written
unique-factorization argument. The infinite series here are geometric
or convergent products, with their analytic qualifications given above.
The checks do not certify operator extensions, a UV construction, or
positivity of the full Weil form.
