# A closed gamma source and the domain of the complete arithmetic pairing

13 September 2026. This note completes the source-domain construction for
the already-positive gamma **kinetic** term. It specifies a massive local
preparation, its reduced source and physical Hilbert adjoint, a compactly
supported core, and two controlled singular limits. It does not identify
the complete Weil form with a positive norm. The fixed contact, signed
poles and every active prime remain explicit bounded additions at each
fixed support length.

The local auxiliary energy was established in the shared background and
the positive-factorizations investigation. The additional results here
are the closed reduced preparation on the actual arithmetic source
space, its maximal adjoint after zero extension, exact regulator norm
growth, and the finite-rank closability consequence. These are direct
operator calculations. They do not assert a new realization theorem or
identify the auxiliary fields with the quartic theory's physical vacua.

## 1. Fix the preparation before taking a singular limit

Let \(H=-\partial_x^2\) be the nonnegative whole-line Laplacian, with
domain \(H^2(\mathbb R)\) in \(L^2(\mathbb R,dx)\). Put

\[
a_k=2k+\tfrac12,\qquad R_k=(a_k^2+H)^{-1},\qquad k\geq0.
\]

For a boundary input \(F\in L^2(\mathbb R)\), the independently specified
positive energy for a field \(u_k\in H^1(\mathbb R)\) is

\[
\mathcal E_k(F,u_k)=\frac2{a_k}
\left(\|F-u_k\|_2^2+a_k^{-2}\|u_k'\|_2^2\right).
\tag{1}
\]

Its unique minimizer is

\[
u_k[F]=a_k^2R_kF
=\frac{a_k}{2}\int_{\mathbb R}e^{-a_k|x-y|}F(y)\,dy.
\tag{2}
\]

Thus all bulk fields extend over the whole line even when the input is
zero outside a finite interval. Replacing them by Dirichlet fields on
that interval changes the preparation and its induced form.

Take the ordinary positive output space

\[
\mathscr H_\gamma=\bigoplus_{k\geq0}
\bigl(L^2(\mathbb R)\oplus L^2(\mathbb R)\bigr).
\]

The prepared source is the collection of energy residuals

\[
(\mathcal A F)_k=
\begin{pmatrix}
\sqrt{2/a_k}\,H R_kF\\
\sqrt{2a_k}\,\partial_xR_kF
\end{pmatrix}
=\begin{pmatrix}
\sqrt{2/a_k}(F-u_k[F])\\
\sqrt{2/a_k^3}\,u_k[F]'
\end{pmatrix}.
\tag{3}
\]

Every individual component is a bounded operator on \(L^2\). No
square root of the full arithmetic operator has been used. The
resolvents, couplings and adjoints in (1)–(3) are fixed explicitly.

With the Fourier convention
\(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\), the two-component column is

\[
v_k(\tau)=
\begin{pmatrix}
\sqrt{2/a_k}\,\tau^2/(a_k^2+\tau^2)\\
\sqrt{2a_k}\,i\tau/(a_k^2+\tau^2)
\end{pmatrix},
\qquad
v_k(\tau)^\dagger v_k(\tau)
=\frac2{a_k}\frac{\tau^2}{a_k^2+\tau^2}.
\tag{4}
\]

Completion of the square in (1), or (4) and Plancherel, gives the
positive gluing identity

\[
\langle\mathcal AF,\mathcal AG\rangle_{\mathscr H_\gamma}
=\frac1{2\pi}\int_{\mathbb R}B(\tau^2)
\overline{\widehat F(\tau)}\widehat G(\tau)\,d\tau,
\qquad
B(s)=\sum_{k\geq0}\frac2{a_k}\frac{s}{a_k^2+s}.
\tag{5}
\]

The [digamma partial-fraction identity](https://dlmf.nist.gov/5.7.E6)
identifies this **known positive** multiplier as

\[
B(\tau^2)=\Re\psi(\tfrac14+i\tau/2)-\psi(\tfrac14).
\tag{6}
\]

The same construction is a discrete direct integral of massive
resolvents, with positive measure
\(\nu=\sum_{k\geq0}(2/a_k)\delta_{a_k^2}\) in
\(B(s)=\int s/(s+r)\,d\nu(r)\). It satisfies
\(\int(1+r)^{-1}d\nu(r)<\infty\). Consequently it also falls under the
general complete-Bernstein extension framework of
[Kwaśnicki–Mucha](https://arxiv.org/abs/1707.02475). No uncomputed string
coefficient is needed for the explicit local tower above.

## 2. The maximal domain and a genuine compact-support core

Define

\[
\mathcal D_\gamma(\mathbb R)=
\left\{F\in L^2(\mathbb R):
\int B(\tau^2)|\widehat F(\tau)|^2\,d\tau<\infty\right\}.
\tag{7}
\]

This is exactly the maximal domain of (3). Its squared graph norm is
\(\|F\|_2^2+\|\mathcal AF\|^2\). The
[digamma asymptotic expansion](https://dlmf.nist.gov/5.11.E2) gives

\[
B(\tau^2)=\log|\tau|-\log2-\psi(\tfrac14)+O(|\tau|^{-2}).
\tag{8}
\]

In particular \(1+B(\tau^2)\) is comparable to
\(\log(2+|\tau|)\) on the whole real axis.

**Closedness.** Suppose \(F_n\to F\) in \(L^2\) and
\(\mathcal AF_n\to U\) in \(\mathscr H_\gamma\). Each bounded component
of (3) converges to the corresponding component applied to \(F\), so
every component of \(U\) equals that of \(\mathcal AF\). Their square
sum is finite because \(U\in\mathscr H_\gamma\). Hence \(F\) belongs to
(7) and \(U=\mathcal AF\). This proves closedness without interchanging
an unbounded infinite sum with an adjoint.

For \(I_L=(-L/2,L/2)\), let \(E_L\) be zero extension and set

\[
\mathcal A_L=\mathcal A E_L,\qquad
\mathcal D_{\log,L}=\{f\in L^2(I_L):E_Lf\in\mathcal D_\gamma(\mathbb R)\}.
\tag{9}
\]

Zero extension is an isometry, so the preceding closedness argument
also proves that \(\mathcal A_L\) is closed. This definition includes
the endpoint contribution of the exterior field. It is not an
unspecified intrinsic logarithmic space on the open interval.

Here is a full core argument. Write
\(w(\tau)=\log(2+|\tau|)\) and let \(F=E_Lf\). For \(0<r<1\), the
unitary dilation

\[
(D_rF)(x)=r^{-1/2}F(x/r),\qquad
\widehat{D_rF}(\tau)=r^{1/2}\widehat F(r\tau)
\]

has support in \([-rL/2,rL/2]\). For \(r\in[1/2,1]\),

\[
\int w(\tau)|\widehat{D_rF}(\tau)|^2\,d\tau
=\int w(\xi/r)|\widehat F(\xi)|^2\,d\xi
\leq2\int w(\xi)|\widehat F(\xi)|^2\,d\xi.
\]

Dilations are strongly continuous in this weighted Fourier norm:
first check it for smooth compactly supported Fourier functions, then
use their density and the uniform displayed bound. Thus
\(D_rF\to F\) in the graph norm as \(r\uparrow1\).

For fixed \(r<1\), convolve \(D_rF\) with a smooth approximate identity
\(\rho_\delta\) supported in \([-\delta,\delta]\), with
\(\delta<(1-r)L/2\). The convolution lies in \(C_c^\infty(I_L)\).
Its Fourier multiplier \(\widehat\rho(\delta\tau)\) tends to one and
is uniformly bounded. Dominated convergence in the weighted norm
proves convergence to \(D_rF\). A diagonal choice proves

\[
\boxed{\ C_c^\infty(I_L)\text{ is an operator core for }\mathcal A_L
\text{ and a form core for }\|\mathcal A_L f\|^2.\ }
\tag{10}
\]

In particular, the closure of the explicit smooth source is its maximal
domain (9). No trace-zero Sobolev condition is being silently imposed:
the constant function on \(I_L\), whose zero extension has jumps,
already belongs to this logarithmic domain. Endpoint mollification
must follow support contraction; unrestricted convolution of a
zero-extended input would leave the interval.

## 3. The physical adjoint and the compressed operator

For \(\Psi=(g_k,h_k)_k\in\mathscr H_\gamma\), define the whole-line
distribution \(t_\Psi\) by its Fourier transform

\[
\widehat t_\Psi(\tau)
=\sum_{k\geq0}v_k(\tau)^\dagger
\begin{pmatrix}\widehat g_k(\tau)\\\widehat h_k(\tau)\end{pmatrix}.
\tag{11}
\]

For almost every \(\tau\), this is a convergent Hilbert-space inner
product because \(\sum_k\|v_k(\tau)\|^2=B(\tau^2)<\infty\). Moreover,

\[
\frac{|\widehat t_\Psi(\tau)|^2}{1+B(\tau^2)}
\leq\sum_k\bigl(|\widehat g_k(\tau)|^2+|\widehat h_k(\tau)|^2\bigr).
\tag{12}
\]

Thus \(t_\Psi\) belongs to the continuous dual of the graph-norm
Fourier space. The finite-component adjoint terms are

\[
\sqrt{2/a_k}\,H R_k g_k-\sqrt{2a_k}\,R_k\partial_xh_k.
\]

The derivative in the second expression is harmless when composed
with \(R_k\); the multiplier is bounded. Their infinite sum is first
understood in the dual topology (12), not assumed to converge in
whole-line \(L^2\).

The maximal adjoints are exactly

\[
\begin{aligned}
\operatorname{Dom}\mathcal A^*
&=\{\Psi:t_\Psi\in L^2(\mathbb R)\},
&\mathcal A^*\Psi&=t_\Psi,\\
\operatorname{Dom}\mathcal A_L^*
&=\{\Psi:t_\Psi|_{I_L}\text{ is represented by an }L^2(I_L)\text{ function}\},
&\mathcal A_L^*\Psi&=t_\Psi|_{I_L}.
\end{aligned}
\tag{13}
\]

The second formula follows first on \(C_c^\infty(I_L)\) by the
definition of distributional restriction, then on all of (9) by the
core property (10). Conversely an adjoint vector supplies precisely
that \(L^2\) representative on tests. One must not replace (13) by a
formal identity with domain \(\operatorname{Dom}\mathcal A^*\):
requiring the distribution to be \(L^2\) on the whole line can impose
an unnecessary condition outside the input interval.

The induced nonnegative self-adjoint operator is

\[
T_L=\mathcal A_L^*\mathcal A_L,
\quad
\operatorname{Dom}T_L=
\left\{f\in\mathcal D_{\log,L}:
\bigl(B(H)E_Lf\bigr)|_{I_L}\in L^2(I_L)\right\},
\tag{14}
\]

where \(B(H)E_Lf\) is initially a distribution in the dual space.
This is the operator domain; (9) is its form domain. They must not be
identified. The closed densely defined source also gives an ordinary
positive graded Hilbert system

\[
\mathbb S_L=
\begin{pmatrix}0&\mathcal A_L^*\\\mathcal A_L&0\end{pmatrix},
\quad
\operatorname{Dom}\mathbb S_L=
\operatorname{Dom}\mathcal A_L\oplus\operatorname{Dom}\mathcal A_L^*,
\quad
\mathbb S_L^2=\operatorname{diag}(T_L,\mathcal A_L\mathcal A_L^*)\geq0.
\tag{15}
\]

This graded organization concerns the specified kinetic model. It does
not calibrate the four-supercharge quartic boundary theory or add the
missing arithmetic terms.

## 4. Two regulator limits and their topology

### A finite massive tower

Let \(\Pi_N\) retain \(0\leq k<N\), and put
\(\mathcal A_{L,N}=\Pi_N\mathcal A E_L\). It extends to a bounded map
on all of \(L^2(I_L)\), with the **exact** norm

\[
\boxed{\quad
\|\mathcal A_{L,N}\|^2
=b_N:=\sum_{k=0}^{N-1}\frac2{a_k}
=\psi(N+\tfrac14)-\psi(\tfrac14)
=\log N-\psi(\tfrac14)+O(N^{-1}).\quad}
\tag{16}
\]

Indeed its multiplier
\(B_N(\tau^2)=\sum_{k<N}(2/a_k)\tau^2/(a_k^2+\tau^2)\)
is bounded above by \(b_N\) and tends to \(b_N\) at high frequency.
For any fixed nonzero \(\phi\in C_c^\infty(I_L)\), modulation of
\(\phi\) approaches that upper bound by dominated convergence.
This proves equality even after zero-extension compression.

For \(f\in\mathcal D_{\log,L}\),

\[
\mathcal A_{L,N}f\longrightarrow\mathcal A_Lf
\quad\text{in }\mathscr H_\gamma,
\qquad
\|\mathcal A_{L,N}f\|^2\uparrow\|\mathcal A_Lf\|^2.
\tag{17}
\]

For \(f\notin\mathcal D_{\log,L}\), these squared norms tend to
infinity. The source therefore has a finite vector limit **exactly**
on the dense domain already specified, rather than on all of \(L^2\).
For the stronger hypothesis \(E_Lf\in H^1(\mathbb R)\), a useful
explicit tail estimate is

\[
\|(\mathcal A_L-\mathcal A_{L,N})f\|^2
\leq\left(\frac2{a_N^3}+\frac1{2a_N^2}\right)
\|(E_Lf)'\|_2^2.
\tag{18}
\]

This follows from \(B-B_N\leq\tau^2\sum_{k\geq N}2/a_k^3\) and
an integral estimate of the decreasing tail. It is not claimed for a
general interval \(H^1\) function with nonzero endpoint traces.

The nonnegative operators
\(T_{L,N}=\mathcal A_{L,N}^*\mathcal A_{L,N}\) converge to \(T_L\)
in the strong-resolvent sense. One way to see this is increasing-form
convergence, as in [Simon's monotone-form theorem](https://doi.org/10.1016/0022-1236(78)90094-0):
the pointwise supremum form has domain (9), is dense and closed by
section 2, and is exactly the form of (14). This is convergence of
resolvents on \(L^2\), not a claim that the unbounded source is a
bounded strong-operator limit there.

### Normalizable point sources followed by a singular boundary limit

A heat regulator directly connects the construction to note 08's
regular source families. For \(\epsilon>0\), define

\[
\mathcal A_L^{(\epsilon)}
=\mathcal A e^{-\epsilon H/2}E_L.
\tag{19}
\]

The point-source vector \(b_{\epsilon,x}\in\mathscr H_\gamma\) is
specified by

\[
\widehat b_{\epsilon,x,k}(\tau)
=e^{-i\tau x}e^{-\epsilon\tau^2/2}v_k(\tau).
\]

It is normalizable, depends continuously on \(x\), and gives the
Bochner preparation

\[
\mathcal A_L^{(\epsilon)}f
=\int_{I_L} f(x)b_{\epsilon,x}\,dx,
\quad
\langle b_{\epsilon,x},b_{\epsilon,y}\rangle
=\frac1{2\pi}\int B(\tau^2)e^{-\epsilon\tau^2}
e^{i\tau(x-y)}\,d\tau.
\tag{20}
\]

Thus (20) is an actual positive Gram gluing of regular Hilbert vectors
in the specified auxiliary model before the limit. Its
Hilbert–Schmidt norm is exactly

\[
\|\mathcal A_L^{(\epsilon)}\|_{\rm HS}^2
=\frac L{2\pi}\int_{\mathbb R}B(\tau^2)e^{-\epsilon\tau^2}\,d\tau.
\tag{21}
\]

The source converges in \(\mathscr H_\gamma\) as
\(\epsilon\downarrow0\) exactly for \(f\in\mathcal D_{\log,L}\),
with limit \(\mathcal A_L f\); outside that domain its squared norm
diverges. This is immediate from monotone convergence of the norm
integrals and dominated convergence for their differences on the
domain. The associated forms again converge monotonically and their
operators converge in strong resolvent topology.

For completeness, (8) makes the divergence of the regular point-source
norm completely explicit:

\[
\|\mathcal A_L^{(\epsilon)}\|_{\rm HS}^2
=\frac{L}{2\sqrt\pi\sqrt\epsilon}
\left(\frac12\log\frac1\epsilon
+\frac{\gamma_E}{2}+\frac\pi2+\log2\right)+O_L(1).
\tag{22}
\]

To verify the constant, rescale the Gaussian integral in (21), use
\(\int e^{-t^2}\log|t|\,dt=(\sqrt\pi/2)\psi(1/2)\),
\(\psi(1/2)=-\gamma_E-2\log2\), and
\(\psi(1/4)=-\gamma_E-\pi/2-3\log2\); the last two values follow
from the [special-value identities](https://dlmf.nist.gov/5.4).
The error is \(O(1)\) because the difference between \(B(\tau^2)\)
and \(\log|\tau|-\log2-\psi(1/4)\) is integrable on the whole line.
The Hilbert–Schmidt divergence alone would not prove divergence of
the operator norms; the high-frequency test and the domain limit do.
The exact operator-norm statement for the massive cutoff is (16).

## 5. Every remaining arithmetic term on this domain

For fixed \(L\), let the active delays and weights be

\[
\mathcal P_L=\{(p,m):p\text{ prime},\ m\geq1,\ m\log p<L\},
\quad d_{p,m}=m\log p,\quad c_{p,m}=(\log p)p^{-m/2}.
\]

This is a finite set. Set \(T_df=(E_Lf)(\,\cdot-d)|_{I_L}\), and
write \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). The full bounded
remainder is the explicitly self-adjoint operator

\[
\mathcal R_L=w_0I+2|c\rangle\langle c|-2|s\rangle\langle s|
-\sum_{(p,m)\in\mathcal P_L}c_{p,m}(T_{d_{p,m}}+T_{d_{p,m}}^*),
\qquad
w_0=-\gamma_E-\frac\pi2-3\log2-\log\pi.
\tag{23}
\]

Its constants and signs are fixed arithmetic data. Since \(c\perp s\),

\[
\|c\|^2=L/2+\sinh(L/2),\qquad
\|s\|^2=\sinh(L/2)-L/2,
\]

the two nonzero pole eigenvalues are
\(L+2\sinh(L/2)\) and \(L-2\sinh(L/2)\). In particular,

\[
\|\mathcal R_L\|
\leq M_L:=|w_0|+L+2\sinh(L/2)
+2\sum_{(p,m)\in\mathcal P_L}c_{p,m}<\infty.
\tag{24}
\]

It follows unconditionally that the complete arithmetic form is

\[
q_L(f,g)=\langle\mathcal A_L f,\mathcal A_L g\rangle
+\langle f,\mathcal R_L g\rangle,
\quad\operatorname{Dom}q_L=\mathcal D_{\log,L},
\quad W_L=T_L+\mathcal R_L,
\quad\operatorname{Dom}W_L=\operatorname{Dom}T_L.
\tag{25}
\]

The form is closed and semibounded: adding
\((M_L+1)\|f\|^2\) makes its form norm equivalent to the graph norm
in section 2. The same core applies. No positivity assumption on
\(q_L\) is needed for this statement.

Both regulator families retain (23) without changing it. The forms
\(\|\mathcal A_{L,N}f\|^2+\langle f,\mathcal R_Lf\rangle\)
converge monotonically after the same fixed lower-bound shift;
their operators converge in strong resolvent topology to \(W_L\).
The heat-regulated version has the same conclusion. The regulated
**full** forms are semibounded; the kinetic gluing does not make their
signed arithmetic remainder positive.

This construction is support compatible. If an input already lies in
a smaller interval, zero extension to a larger interval leaves the
kinetic and pole forms unchanged. Newly active delays with length at
least the old interval length have zero overlap with that input.
All primes active at each new \(L\) must nevertheless be included for
new inputs. The bound (24) is local in support and supplies no
uniform all-prime positive limit.

As an additional domain consequence, the embedding
\(\mathcal D_{\log,L}\hookrightarrow L^2(I_L)\) is compact. Its
bounded sets have uniformly small Fourier tails by (7)–(8), while
the map from \(L^2(I_L)\) to any bounded Fourier interval is
Hilbert–Schmidt. Frequency truncation therefore approximates the
embedding in operator norm by compact maps. Thus \(T_L\), and then
the bounded perturbation \(W_L\), have compact resolvent. Any
negative spectral subspace of \(W_L\) is finite dimensional for
fixed \(L\). This does not identify or remove that subspace, and is
not an independent positivity mechanism.

The high-frequency identity can now retain the finite arithmetic
oscillations and the exact contact constant. If
\(f_N(x)=e^{iNx}\phi(x)\), \(0\ne\phi\in C_c^\infty(I_L)\), then

\[
\begin{aligned}
Q_L[f_N]={}&\|\phi\|_2^2\bigl(\log N-\log(2\pi)\bigr)\\
&-2\sum_{(p,m)\in\mathcal P_L}c_{p,m}
\Re\!\left(e^{-iNd_{p,m}}
\langle E_L\phi,U_{d_{p,m}}E_L\phi\rangle\right)+o(1).
\end{aligned}
\tag{26}
\]

The pole amplitudes decay faster than any inverse power of \(N\).
For the multiplier term, Fourier translation, (8), and rapid decay
of \(\widehat\phi\) give the displayed limit. The constant follows
from \(-\log2-\psi(1/4)+w_0=-\log(2\pi)\), so moving the contact
changes this subleading term. The prime oscillations generally do
not converge; they stay bounded at fixed support. In particular
\(Q_L[f_N]=\|\phi\|^2\log N+O(1)\) as required.

## 6. A finite vacuum space cannot hide the unbounded source

**Finite-rank closability lemma.** Let \(A:\mathcal D\subset\mathscr H
\to\mathscr K\) be densely defined and linear, with finite-dimensional range.
If \(A\) is closable in these Hilbert norms, it is bounded on
\(\mathcal D\) and extends to a bounded finite-rank map on all of
\(\mathscr H\). If it is closed, its domain is already all of
\(\mathscr H\).

**Proof.** If no bound exists, choose \(f_n\in\mathcal D\) with
\(\|f_n\|\to0\) and \(\|Af_n\|=1\). Compactness of the unit sphere
in the finite-dimensional range gives a subsequence with
\(Af_n\to v\), \(\|v\|=1\). This contradicts closability. The
bounded extension has domain all of the source Hilbert space and is
the graph closure because \(\mathcal D\) is dense. ∎

Consequently a densely defined, closable \(L^2(I_L)\) preparation
whose image stays inside the three-state symmetry sector, all nine
quartic vacua, or any fixed finite-dimensional physical space is
excluded by (26). Describing its input as a distribution or restricting
the initial formula to smooth test functions does not evade this
lemma if its closure is still required in the \(L^2\) source topology.
Using a stronger source norm changes the assertion and must be made
explicit; it does not provide an unbounded closable finite-vacuum map
from \(L^2\).

There is also no loophole in deliberately omitting a closure check
for a purported norm identity. If a linear map on \(C_c^\infty(I_L)\) had
\(\|Af\|^2=Q_L[f]\), then the known closed form and its core imply
that it is closable: a sequence tending to zero in \(L^2\) whose
images converge is Cauchy in the form norm; closedness forces its
image norm to tend to zero. Equality would first imply nonnegativity
on the core and hence on the form domain. The finite-rank lemma then
applies. Finite channel spaces coupled to infinitely many excited
states remain possible, since their total prepared range need not
be finite dimensional.

## 7. What has and has not been constructed

The explicit gamma model now has the required unbounded source,
positive pairing, physical adjoint, maximal dense domain, core and
singular regulator topology. It supplies an exact reference for an
excited-state or defect extension of a physical theory. The mass
cutoff explains how an infinite tower accumulates logarithmic energy;
the heat cutoff gives ordinary normalizable boundary vectors whose
limit becomes distributional in the required manner.

The complete norm identity remains open. A direct sum of the gamma
source with independent positive finite-vacuum outputs would add
nonnegative forms. It does not reproduce the fixed negative contact,
the negative pole direction, or the signed prime translations in
(23). A coherent source, physical constraint or other gluing law
must derive those terms jointly, on the domain (9), with the
normalization and support compatibility shown above. Assuming that
the operator in (25) is positive and then taking its square root, or
assuming the positivity of an equivalent Schur block, would still
assume the desired conclusion.

The most direct next connection to the quartic boundary investigation
is therefore an independently specified coupling from its boundary
channels to an infinite excited sector. Its physical gluing should
retain the gamma source's singular topology while producing (23).
The three-state pairing can calibrate boundary amplitudes and their
normalization, but the finite-rank lemma proves that this calibration
cannot be the whole arithmetic preparation.

All closure, core, adjoint, compactness and asymptotic claims above
are analytical deductions, not conclusions of the package's exact
algebra programs. No new numerical dataset or sampled positivity
claim is involved. The cited primary analytical literature supplies
the general extension and monotone-form frameworks; the explicit
source and domain calculations are given here and await independent
specialist review.
