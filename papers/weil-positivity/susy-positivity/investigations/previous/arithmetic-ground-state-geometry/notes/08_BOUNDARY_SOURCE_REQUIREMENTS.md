# Boundary sources, physical period calibration, and positive resolvent gluing

13 September 2026. Bounded continuation after saving the manuscript draft. The results below are exact conditional identities and necessary source requirements; they do not establish Weil positivity. The finite-dimensional algebra and source-growth test are derived here. The resolvent construction is standard operator theory, reproduced to identify a concrete form of theory-derived positivity. No numerical positivity bound is proposed.

## 1. The next missing object is a physical boundary functional

The interacting prime model supplies a nine-dimensional positive vacuum space. Its symmetry sector and identity-period differential system can have smaller dimension. Neither dimension changes the following distinction: a holomorphic integration period is not automatically a bounded linear functional on the physical vacuum space with the desired normalization.

Let \(V\cong\mathbb C^r\) be a physical vacuum space with positive metric matrix \(G\). Suppose an independently specified boundary construction supplies an actual linear functional

\[
\ell(v)=p\,v,\qquad p\in\mathbb C^{1\times r}.
\]

Identifying a thimble integral with this functional requires a map between the integration data and physical harmonic states. In particular, exponential periods and the Jacobi-ring quotient are not interchangeable by definition. The following statements start only after that map has been supplied.

The Riesz boundary vector and its squared norm are

\[
b=G^{-1}p^\dagger,\qquad
\beta=\|b\|_G^2=pG^{-1}p^\dagger.
\]

For nonzero \(p\), every source \(v\) has the exact orthogonal decomposition

\[
v=\frac{\ell(v)}\beta b+v_\perp,\qquad \ell(v_\perp)=0,
\]

\[
\boxed{\quad
\|v\|_G^2=\frac{|\ell(v)|^2}{\beta}+\|v_\perp\|_G^2.
\quad}
\]

This is a useful physical calibration criterion, rather than merely a numerical Cauchy–Schwarz bound. Equality of a physical norm with a prescribed multiple of a period square means both that the boundary norm \(\beta\) has been fixed and that the source lies on the Riesz boundary line. A single period value supplies neither assertion. An independent gluing law or charge constraint could supply them.

For the identity source of the shape-deformed prime sector, if its period is genuinely this physical functional and is nonzero, the proposed normalization-invariant comparison becomes

\[
\frac{H(c,\bar c)}{|C^{\rm per}(c)|^2}
=\frac1{\beta(c,\bar c)}
+\frac{\|v_\perp(c)\|^2}{|C^{\rm per}(c)|^2}.
\]

The formula does not assert that the current real-cycle period has already been realized as such a boundary functional. It identifies precisely what a future realization would let that ratio measure: boundary normalization plus a source component invisible to that period. Common rescaling of the source cancels from the ratio. Rescaling the boundary functional itself is different physical data and changes \(\beta\).

### Several periods do not remove the need for physical gluing

For an actual boundary map \(P:V\to\mathbb C^m\), set

\[
B=PG^{-1}P^\dagger,\qquad y=Pv.
\]

Here \(B\) is the Gram matrix of the Riesz boundary vectors. With \(B^+\) its Moore–Penrose inverse,

\[
v_{\min}=G^{-1}P^\dagger B^+y,
\qquad
\boxed{\ \|v\|_G^2=y^\dagger B^+y+\|v-v_{\min}\|_G^2\ }.
\]

Indeed \(y\in\operatorname{ran}B\), \(Pv_{\min}=y\), and \(v-v_{\min}\) is orthogonal to the span of the Riesz vectors. Thus even a complete square invertible period matrix determines the physical norm only after its positive boundary Gram matrix is known. In that case

\[
G=P^\dagger B^{-1}P.
\]

A topological intersection form, which can have a different signature and conjugation law, cannot be substituted for \(B\) without a physical identification. Conversely, an independently derived positive gluing matrix would turn period computations into a norm identity without estimating the unknown norm numerically. This is a concrete reason to investigate physical boundary preparation alongside the shape-period system.

## 2. An infinite Hilbert space is insufficient if the source stays regular

The next requirement is stronger than the already established finite-vacuum rank obstruction. It concerns a broad class of boundary source maps even when the receiving physical Hilbert space is infinite dimensional.

Fix an interval \(I=(-L/2,L/2)\) and any nonzero \(\varphi\in C_c^\infty(I)\). Define

\[
f_N(x)=e^{iNx}\varphi(x).
\]

The gamma multiplier satisfies

\[
B(\tau^2)=\log|\tau|-\log2-\psi(1/4)+o(1)
\qquad(|\tau|\to\infty).
\]

Rapid Fourier decay of \(\varphi\), together with this logarithmic growth, gives

\[
K[E_Lf_N]=\|\varphi\|_2^2\log N+O(1).
\]

For a fixed support length all active prime terms are bounded translation forms. The contact is bounded, and the two pole amplitudes of \(f_N\) tend to zero. Consequently the *complete* target satisfies the unconditional high-frequency identity

\[
\boxed{\quad Q_L[f_N]=\|\varphi\|_2^2\log N+O(1).\quad}
\]

No positivity assertion about other inputs is used. In particular, \(Q_L\) is not a bounded quadratic form on \(L^2(I)\).

Now suppose a putative physical boundary preparation has the form

\[
\mathcal A f=\int_I f(x)b_x\,dx,\qquad
\int_I\|b_x\|_{\mathscr H}^2\,dx<\infty,
\]

where \(b_x\) are strongly measurable vectors in an ordinary Hilbert space. The integral defines a Hilbert–Schmidt map \(L^2(I)\to\mathscr H\), and in particular

\[
\|\mathcal A f\|^2\le
\left(\int_I\|b_x\|^2dx\right)\|f\|_2^2.
\]

It therefore cannot satisfy \(\|\mathcal A f\|^2=Q_L[f]\) on all smooth inputs. This includes a normalizable boundary vector transported unitarily, \(b_x=e^{-ixH}b\), and uniformly bounded observable families acting on a normalizable vacuum. Introducing infinitely many excited states does not evade this statement if the resulting point-source vectors retain the displayed square-integrability.

There are ordinary physical ways to change this hypothesis: operator-valued distributions, an unbounded energy or derivative insertion, boundary traces in a rigged Hilbert space, or a singular limit of regularized boundary preparations. Such mechanisms occur already for the positive gamma kinetic term. Their necessity is not evidence against quantum theory or Gaussian theories; it is a source-domain requirement forced by the known logarithmic energy.

The same proof gives a regulator test. If positive preparations \(\mathcal A_\epsilon\) converge in squared norm on every smooth input to \(Q_L\), their operator norms from \(L^2(I)\) cannot stay uniformly bounded as \(\epsilon\downarrow0\). Uniform boundedness would make the limiting form bounded, contradicting the modulation identity. A proposed construction should identify its singular source limit and closed form domain explicitly, rather than hide this limit inside a vacuum overlap.

Finally, time evolution within a vacuum space does not itself provide the missing states: a supersymmetric ground sector has \(H=0\), so its ordinary evolution is constant. An infinite-dimensional boundary source must access excitations, fields, or additional periodic sectors rather than merely attach a time label to the same nine vacua.

## 3. A positive operator gluing identity with finite channels and infinitely many states

There is an exact operator architecture in which a finite channel space can couple to an infinite physical state space and positivity is a consequence of a self-adjoint bulk realization. It is useful as a criterion for future constructions, not an arithmetic realization already obtained here.

Let \(\mathscr K=\mathbb C^r\), let \(H\) be an independently specified self-adjoint operator on \(\mathscr H\), and let \(B:\mathscr K\to\mathscr H\) be bounded. If \(H\) is a physical Hamiltonian one can additionally require \(H\ge0\); the identities use only self-adjointness. They apply equally to interacting Hamiltonians: linearity of this boundary response does not make the bulk theory Gaussian. For \(z\) in the upper half-plane define

\[
R(z)=(H-z)^{-1},\qquad M(z)=B^*R(z)B.
\]

The resolvent identity gives

\[
\boxed{\quad
\frac{M(z)-M(w)^*}{z-\bar w}
=B^*R(z)R(\bar w)B
=\Gamma(z)^*\Gamma(w),
\quad \Gamma(z)=R(\bar z)B.
\quad}
\]

In particular \(\operatorname{Im}M(z)\ge0\), and the entire two-variable kernel is positive as a Gram kernel. For arbitrary finite channel vectors \(u_j\), its quadratic sum is

\[
\sum_{j,k}u_j^*
\frac{M(z_j)-M(z_k)^*}{z_j-\bar z_k}u_k
=\left\|\sum_k\Gamma(z_k)u_k\right\|^2.
\]

The Cayley transform

\[
S(z)=(M(z)-iI)(M(z)+iI)^{-1}
\]

also has the exact positive kernel

\[
\frac{I-S(z)S(w)^*}{-i(z-\bar w)}
=2(M(z)+iI)^{-1}
\frac{M(z)-M(w)^*}{z-\bar w}
(M(w)^*-iI)^{-1}.
\]

Thus a scattering contraction can follow from the bulk resolvent and its Hilbert adjoint. It need not be verified by bounding a desired arithmetic function numerically. Operator-valued Herglotz and conservative-realization theory provides the broader framework; see [Gesztesy–Kalton–Makarov–Tsekanovskii, *Some Applications of Operator-Valued Herglotz Functions*](https://arxiv.org/abs/math/9802103) and [Belyi–Hassi–de Snoo–Tsekanovskii, *A General Realization Theorem for Matrix-Valued Herglotz–Nevanlinna Functions*](https://arxiv.org/abs/math/0510464). Only the elementary bounded-coupling case is asserted by the derivation above.

The distinction between channels and states is essential. Finite \(r\) does not bound the rank of this kernel when \(H\) has infinitely many accessible states. Restricting \(H\) itself to the nine-dimensional vacuum sector makes \(M\) rational and the Gram kernel finite rank; restricting to zero-energy vacua makes its dependence still simpler. The field theory must provide an excited or boundary sector if this architecture is to supply all arithmetic inputs.

For a fixed curve \(z=x+i\epsilon\), finite \(\epsilon>0\), and locally bounded channel preparation, the resulting smeared vectors are regular and fall under the previous bounded-source obstruction. An arithmetic identification would therefore need a controlled boundary-value limit, an unbounded coupling, or a different energy insertion. The resolvent formula is an exact positive starting point for that analysis, not permission to ignore it.

## 4. Where normalization and poles re-enter

A general operator-valued Herglotz representation can involve

\[
M(z)=A+Dz+\int_\mathbb R
\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\Sigma(t),
\qquad A=A^*,\quad D\ge0,
\]

with a positive operator measure and appropriate weighted integrability. Its positive difference kernel is

\[
\frac{M(z)-M(w)^*}{z-\bar w}
=D+\int_\mathbb R\frac{d\Sigma(t)}{(t-z)(t-\bar w)}.
\]

The Hermitian constant \(A\) drops out. Hence positivity of this kernel alone does not fix every normalization of the impedance function. In the bounded-resolvent model the large-imaginary-parameter normalization fixes the missing constant; singular boundary couplings can require a subtraction convention or a specified self-adjoint boundary condition. No identification of \(A\) with the arithmetic contact is asserted before an actual arithmetic-to-boundary transform is given. The warning is structural: a positive operator kernel and a correctly normalized target function are separate pieces of data.

A complete Weil construction based on such gluing must therefore supply, independently of the desired answer:

1. A physical source map from compactly supported arithmetic inputs, with its necessary unbounded or distributional domain.
2. A resolvent, conservative scattering law, or other Ward identity giving the full positive Gram pairing.
3. An exact transform identifying that pairing with the gamma contribution, active prime returns, contact, and both signed pole sectors simultaneously.

The signed pole expression cannot simply be declared the Gram matrix of two positive states. It may arise inside a larger identity with interference, a quotient, or relative boundary data; the positive total pairing must then follow from that same independently derived gluing law. This is distinct from assuming positivity of a Schur block whose minimum is already the unknown Weil form.

## 5. Narrow next test

For the interacting shape family, first determine whether a candidate cycle defines a physical boundary covector and compute or characterize its Riesz vector. The finite-dimensional calibration identity then asks an exact question: does a physical gluing law fix the boundary Gram matrix and the component of the identity source invisible to the chosen period? The ratio investigation can test this question without pretending to represent all arithmetic inputs.

In parallel, any proposed periodic gamma or excited-state extension should state the full source map before a lengthy spectral calculation. If that map consists only of square-integrable point-source vectors, the modulation obstruction rejects the full-Weil identification immediately. If it uses a singular boundary limit, the resolvent Gram identity offers a concrete route by which positivity could survive while the full source space becomes infinite dimensional. The arithmetic matching, source normalization, and pole reconstruction remain open analytical tasks.

## Status

Established here: exact conditional Riesz calibration identities; a bounded-source obstruction stronger than finite-vacuum rank counting; its uniform-regulator consequence; and explicit positive resolvent/Cayley kernel identities with their normalization limits. Proposed, not established: a physical period covector for the current quartic model, a singular arithmetic boundary source, or an exact full-Weil gluing identity. The two external references concern general operator realization theory and do not provide those arithmetic identifications.
