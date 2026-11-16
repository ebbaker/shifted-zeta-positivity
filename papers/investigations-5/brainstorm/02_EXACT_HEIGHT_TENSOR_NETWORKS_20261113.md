# Exact height transport and infinite tensor networks

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in this chat's recorded configurations.

**Status:** open conceptual brainstorm, with exact representation identities
derived below and a same-assistant analytical check. No numerical campaign,
new sub-investigation, QTT task activation or theta zero-exclusion result.
The original instruction places this conversation's research notes here;
the [Investigations 6 brainstorm](../../investigations-6/brainstorm/README.md)
links to this record.

## 1. What would make this a distinct investigation

The existing QTT branch asks for useful rank/error bounds. This additional
idea asks for an **exact recursive structure**: how one description generates
all heights, how scale refinement assembles the complete state, and whether
the resulting transfers expose an otherwise inaccessible invariant or
estimate. Those are different questions, even if later results connect them.

Three indices must stay separate:

| Parameter | Meaning | Natural operation |
| --- | --- | --- |
| \(x\) | Real Newman height, twice zeta height | Continuous unitary translation in the source representation |
| \(\tau=1/2-\lambda\) | Contractive imaginary time | Multiplication by \(e^{-\tau u^2}\) |
| \(k\) or \(n\) | Binary resolution or orthogonal-polynomial chain site | Refinement or movement through a basis; not height itself |

An infinite representation can be exact although every finite evaluation
has a remainder. Exactness removes an ansatz mismatch in the limiting
object; it does not automatically make its contraction, convergence or
height-uniform analysis simple.

Classification under [avoid 01](../../../avoid/01_restating_the_target.md):
the identities below are representations, not zero criteria. Proposed
coefficient and transfer estimates are potential intermediate milestones;
none is attained here. Use the [result index](../../../result-summaries/README.md),
[avoid index](../../../avoid/README.md),
[controls 12](../../../result-summaries/12_collision_controls_and_screening.md),
[control-premise rule](../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate-change caution](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped-exclusion rule](../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 2. Fixed source and the exact two-parameter orbit

Keep the complete [GNP source](../09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \qquad H_0(z)=\xi(1/2-iz/2)/8.
 \tag{1}
\]

Here \(\Phi\) is the complete positive, even theta source, with its
double-exponential tails. Initially take \(0\le\lambda\le1/2\).
Set \(W_*=W_{1/2}\), \(Z_*=\int W_*\), and
\(d\mu_*=W_*\,du/Z_*\). In \(L^2(\mu_*)\), let \(X\) multiply by \(u\)
and let \(\Omega=1\). Then

\[
 q_{\tau,z}=e^{-\tau X^2}e^{izX}\Omega,\qquad
 H_{1/2-\tau}(z)=\frac{Z_*}{2}\langle\Omega,q_{\tau,z}\rangle.
 \tag{2}
\]

This is an alternative wavefunction representation with a fixed weighted
Hilbert space. Its Lebesgue-space wavefunction is
\(\sqrt{W_*/Z_*}\,e^{-\tau u^2+izu}\); it is not silently identified
with the earlier source-amplitude state \(W_*e^{-\tau u^2}\).
The readout in (2) preserves the complete original field.

For real \(x\), height evolution is unitary and imaginary-time evolution
is contractive. On the prepared vectors,

\[
 \partial_xq=iXq,\qquad \partial_\tau q=-X^2q,
 \qquad q_{\tau,x+\delta}=e^{i\delta X}q_{\tau,x}.
 \tag{3}
\]

Both operations commute. All differentiated integrals are legitimate on
compact parameter sets because the source has every exponential and
Gaussian moment. This also permits complex \(z\), with the prepared-vector
domains retained; \(e^{izX}\) is not a bounded operator for general nonreal
\(z\). Formula (3) gives \(\partial_\tau H=H_{zz}\), hence the correct
\(\partial_\lambda H=-H_{zz}\).

## 3. An exact semi-infinite chain

Apply Gram–Schmidt to \(1,u,u^2,\ldots\) in \(L^2(\mu_*)\), choosing
orthonormal polynomials \(p_n\) with positive leading coefficients.
They form a complete basis here: if \(g\in L^2(\mu_*)\) is orthogonal
to every polynomial, \(\int g(u)e^{izu}d\mu_*\) is entire by
Cauchy–Schwarz and the source tails. All derivatives at zero vanish, so
Fourier uniqueness gives \(g=0\).

Evenness and degree orthogonality give

\[
 up_n=a_{n+1}p_{n+1}+a_np_{n-1},\quad a_n>0\ (n\ge1),
 \quad a_0=0,
\]
\[
 J=\begin{pmatrix}
 0&a_1&0&\cdots\\
 a_1&0&a_2&\cdots\\
 0&a_2&0&\ddots\\
 \vdots&\vdots&\ddots&\ddots
 \end{pmatrix}.
 \tag{4}
\]

Define the self-adjoint realization by transporting the multiplication
operator \(X\), including its domain, through this complete basis.
Thus no boundary condition at infinity is guessed from a formal matrix.
With \(e_0=(1,0,\ldots)\), (2) becomes

\[
 \boxed{H_{1/2-\tau}(z)=\frac{Z_*}{2}
 \langle e_0,e^{-\tau J^2}e^{izJ}e_0\rangle.}
 \tag{5}
\]

This is the single-particle version of the orthogonal-polynomial chain
mapping familiar in open quantum systems; see
[Chin et al., §3, Theorem 3.1](https://arxiv.org/abs/1006.4507v2).
The full-line theta domain and normalization in (5) were derived above,
rather than imported from their reservoir assumptions.

Writing \(v_n(\tau,x)=\langle e_n,e^{-\tau J^2}e^{ixJ}e_0\rangle\),

\[
 \partial_xv_n=i(a_nv_{n-1}+a_{n+1}v_{n+1}),
\]
\[
 \partial_\tau v_n=-a_na_{n-1}v_{n-2}
 -(a_n^2+a_{n+1}^2)v_n-a_{n+1}a_{n+2}v_{n+2},
 \tag{6}
\]

with missing negative-index terms omitted. Height has a nearest-neighbor
generator, and imaginary time has a range-two generator. Finite height
steps use \(e^{i\delta J}\), which is generally not nearest-neighbor.
The recurrence is in the chain index; it does not close on finitely many
scalar height values of \(H\).

This construction uses only source moments, not unknown zeros. For monic
polynomials with norms \(h_n\), \(a_n^2=h_n/h_{n-1}\). Equivalently,
if \(D_n=\det(m_{j+k})_{j,k=0}^{n-1}\), \(D_0=1\), and
\(m_j=\int u^j d\mu_*\), then
\(a_n^2=D_{n+1}D_{n-1}/D_n^2\). Exact definitions are available;
simple formulas or useful theta-specific bounds for these coefficients
remain a substantive question.

There is a concrete reason an increasing-height hierarchy is natural in
this encoding. At fixed \(\tau\), every fixed \(v_n(\tau,x)\) tends to
zero as \(|x|\to\infty\), by the Riemann–Lebesgue lemma applied to its
integrable polynomial-weighted source. But
\(\sum_n|v_n(\tau,x)|^2=\int e^{-2\tau u^2}d\mu_*>0\) is independent
of real height. Thus mass leaves every fixed finite prefix of the chain.
Truncating to a fixed number of these sites cannot approximate the state
uniformly at all heights. A useful transport estimate could describe how
far down this chain a given height reaches; no rate is established here.
This statement is specific to prefix truncation in this basis.

### An exact MPS, with its information cost visible

Encode \(v\in\ell^2(\mathbb N_0)\) as a single excitation on a chain:
\(|V\rangle=\sum_n v_n|0\cdots1_n\cdots0\rangle\).
For sites \(n=0,1,\ldots\), the cores

\[
 A_n^0=I_2,\quad A_n^1=v_n E_{12},\quad
 \ell=(1,0),\quad r=(0,1)^{\mathsf T}
 \tag{7}
\]

give exactly this state in the norm limit of finite prefixes. Zero
occupations give \(\ell r=0\); one gives \(v_n\); two give zero since
\(E_{12}^2=0\). Prefix errors have squared norm \(\sum_{n>N}|v_n|^2\).
This is an exact bond-two MPS on infinitely many sites, continuously
dependent on height and imaginary time through (6).

Small bond dimension here comes from the single-excitation encoding of
any vector. The infinitely many coefficients still contain the difficulty.
It is a different tensorization from binary-coordinate QTT and supplies
no compression theorem for that ordering. The norm-limit statement does
not claim an operator-norm-convergent infinite product on the entire spin
Hilbert space.

## 4. Newman deformation gives an exact nonlinear coefficient lattice

There is a second useful description. Build the monic polynomials anew
for the unnormalized weight \(W_\lambda(u)du\), and write
\(\beta_n(\lambda)=h_n(\lambda)/h_{n-1}(\lambda)\), \(\beta_0=0\).
Then

\[
 \boxed{\partial_\lambda\beta_n
   =\beta_n(\beta_{n+1}-\beta_{n-1}),\qquad n\ge1.}
 \tag{8}
\]

To check the specialization directly, differentiate
\(h_n=\int P_n^2W_\lambda\). The term containing
\(\partial_\lambda P_n\) vanishes by degree orthogonality. The monic
three-term recurrence gives
\(h_n'/h_n=\beta_{n+1}+\beta_n\); subtract the adjacent identity for
\(\log(h_n/h_{n-1})\) to obtain (8). Reversing to \(\tau\) reverses
the sign.

This is the classical Volterra/Langmuir or Kac–van Moerbeke lattice,
not a new general identity; see [Van Assche, §2.3, Theorem 2.4 and its
symmetric specialization](https://arxiv.org/abs/2202.11017v1).
Its interest here is the exact theta initial data. A finite Painlevé
closure or special coefficient asymptotic is not assumed.

The moving Jacobi matrix \(J(\lambda)\) gives instead
\(H_\lambda(z)=Z_\lambda\langle e_0,e^{izJ(\lambda)}e_0\rangle/2\).
It is distinct from the fixed \(J=J(1/2)\) in (5). Differentiating
vectors in a moving polynomial basis requires its basis-connection terms;
one must not reuse (6) unchanged with \(a_n(\lambda)\).

## 5. A literal infinite product approaching the identity

On a compact interval \([a,a+\ell]\), write
\(u=a+\ell\sum_{k\ge1}2^{-k}b_k\), ignoring the null set of ambiguous
binary expansions. Let \(n_k\) be the bit occupation projector. The
height factor is the exact product

\[
 e^{ixu}=e^{ixa}\prod_{k\ge1}e^{ix\ell2^{-k}n_k},\qquad
 \|e^{ix\ell2^{-k}n_k}-I\|\le |x|\ell2^{-k}.
 \tag{9}
\]

Hence the product converges in operator norm on this compact-coordinate
space, uniformly for bounded heights. For complex height in a compact
set the same conclusion follows from
\(|e^w-1|\le |w|e^{|w|}\). The sum of real-height tail bounds after
level \(L\) is \(|x|\ell2^{-L}\). Increasing height exposes more
nontrivial scales; it does not destroy the exact infinite formula.

The source also has an exact near-identity refinement construction.
For any strictly positive \(C^1\) amplitude \(f\) on this interval,
let \(f_k\) be its average on the dyadic cell of level \(k\), with
\(f_0\) the full-interval average. Define multiplication gates
\(R_k=f_k/f_{k-1}\). If \(m=\min f>0\) and \(M=\|f'\|_\infty\),

\[
 f=f_0\prod_{k\ge1}R_k,\qquad
 \|R_k-I\|\le\frac{M\ell}{m}\,2^{1-k}.
 \tag{10}
\]

Indeed, the finite product telescopes to \(f_L/f_0\), dyadic averages
converge uniformly to \(f\), and the parent-cell oscillation bounds the
displayed ratio. Each gate is a diagonal operator on the first \(k\)
bits and therefore a finite tensor network. Its support grows with \(k\);
no uniform bound on exact bond dimension follows. Applying this to
\(W_{1/2-\tau}\) retains the imaginary-time orbit exactly.

For the complete real line, use a countable partition into compact
intervals and sum their exact readouts. The theta tails make that sum
absolutely convergent, locally uniformly in \((\lambda,z)\). This
retains all tails. The compact-interval constants in (10) need not be
uniform over the intervals, so a global operator-norm product is not
claimed.

These are constructive answers to existence of an exact infinite network.
They work for broad smooth positive-source classes. Their potential
research content is a simpler, theta-specific rule for the cores or a
useful uniform transfer estimate, not existence alone.

## 6. Which asymptotic limit matters

“Factors approach identity” needs a topology and an index. By itself it
does not ensure convergence: \(\prod_k(1+1/k)\) diverges. A summable
bound on deviations suffices for the bounded-operator products above.

In (9), the factors approach identity as resolution \(k\to\infty\)
at a fixed height. They do not do so uniformly over all real heights.
Nor does a fixed height increment become simpler merely because its
starting height increases: (3) always uses the same \(e^{i\delta J}\).
Since the complete source is positive on all of \(\mathbb R\),
\(\sigma(J)=\mathbb R\), and

\[
 \|e^{i\delta J}-I\|=2\quad(\delta\ne0).
 \tag{11}
\]

It is strongly continuous, and its action on the prepared vectors is
analytic, but it is not operator-norm continuous. An asymptotically
near-identity rule in height may require a weighted state norm, a change
of height variable, or removal of a specified leading oscillation. Those
are possibilities to investigate, not properties established here.

On the prepared real-height orbit there is already the elementary bound
\(\|v(\tau,x+\delta)-v(\tau,x)\|\le
|\delta|\,\|Je^{-\tau J^2}e_0\|\), uniform in \(x\). Small state
increments therefore coexist with (11); neither controls relative error
in a small, strongly cancelled scalar readout by itself.

There is also a narrow finite-dimensional obstruction. For any fixed
\(\lambda\), an identity \(H_\lambda(x)=c^{\mathsf T}e^{xA}b\) with
a finite constant matrix \(A\) would, by Cayley–Hamilton, give a nonzero
constant-coefficient differential equation \(P(\partial_x)H_\lambda=0\).
Fourier injectivity then gives \(P(iu)W_\lambda(u)=0\), impossible because
the source is strictly positive everywhere. This excludes only that
autonomous finite-dimensional linear realization. It excludes neither
(7), infinitely many sites, nor nonautonomous or scale-dependent tensors.

## 7. Other possible structures and proof questions

A discrete-height variant starts with a spacing \(\delta>0\) and the
pushforward \(\nu_{\lambda,\delta}\) of \(W_\lambda du/Z_\lambda\)
under \(u\mapsto e^{i\delta u}\). Its moments are exactly
\(H_\lambda(n\delta)/H_\lambda(0)\). Unit-circle orthogonal polynomials
then provide a two-component transfer recursion; see
[Van Assche §1.2, equation (1.7)](https://arxiv.org/abs/2202.11017v1).
A near-background transfer product would require appropriate coefficient
estimates, left open here. Its recursion index is polynomial degree,
not automatically a recurrence between neighboring scalar samples.
Moreover one spacing folds the source modulo \(2\pi/\delta\): the
single sampled family does not recover the continuous-height field without
additional information or compatible spacings.

Continuous MPS in the specific field-theoretic sense use a path-ordered
exponential along a continuous *physical coordinate*. That differs from
letting the external parameter \(x\) vary continuously in (7). See
[Verstraete–Cirac, definition on PDF page 1](https://arxiv.org/abs/1002.1824v1).
A continuum-field model could be another route, but it should explain
what its local degrees of freedom add. Substituting the already unknown
answer as a tensor coefficient would supply no new recursive rule.

The most useful open questions seem to be:

1. **Theta chain structure:** can the full arithmetic source and reflection
   give an explicit relation or quantitative inequality for its recurrence
   coefficients beyond those shared by arbitrary positive even sources?
2. **Exact scale structure:** can the growing-support gates in (10) be
   replaced by a manageable recursive tensor rule, with a proved limiting
   contraction and a useful complex-height domain?
3. **A consequence for the readout:** can either structure control a signed
   boundary amplitude, cancellation or logarithmic observation using an
   invariant that generic source positivity does not give?

Self-adjointness of \(J\) concerns its source-coordinate spectrum, not the
zeros of the return amplitude (5). Orthogonal polynomials' real zeros are
also not the zeros of \(H\). Finite chain truncations need not preserve
the desired zero geometry. An all-real polynomial approximation hierarchy
converging locally uniformly to this \(H_0\) would be the familiar
Laguerre–Pólya/RH-equivalent target, not evidence obtained merely by
tensorizing it. No such hierarchy is proposed as acquired here.

## 8. Collision controls applied to the new mechanisms

The exact atomic control from the
[opening note §9](01_MPS_NEWMAN_FLOW_20261113.md) is
\(F_\lambda(x)=2+2e^{\lambda-T}\cos x\), \(0<T\le1/2\).
Its normalized source has total mass
\(p=e^{\lambda-T}/(1+e^{\lambda-T})\) at \(u=\pm1\), split equally,
and mass \(1-p\) at zero. Its Jacobi coefficients are

\[
 \beta_1=p,\qquad \beta_2=1-p,\qquad \beta_3=0.
 \tag{12}
\]

These satisfy (8): \(p'=p(1-p)\) and
\((1-p)'=-(1-p)p\). At the positive-time double event
\((\lambda,x)=(T,\pi)\), both nonzero coefficients equal \(1/2\).
The finite chain, its height evolution and its coefficient flow are
regular there, while \(F=F_x=0\), \(F_{xx}=2\) and \(F_\lambda=-2\).
Thus exact chain evolution and the Volterra rule do not themselves prevent
a collision. This control fails the full theta source/profile, infinite
support and eventual threshold simplicity.

The remaining catalog screen is analytical, using its existing witnesses;
no numerical certificate was rerun:

| Catalog family | Mechanism it can share | Missing premise of the literal theta problem |
| --- | --- | --- |
| Euler-factor translated sources | Positive even chain, height transport, coefficient deformation | Unchanged complete xi/theta source and its canonical arithmetic |
| Weighted-square and finite-prefix sources | Source-coordinate transport; positivity where the source construction supplies it | Complete coefficients and full smooth reflection; event times are not finite all-real thresholds |
| Reflected super-Gaussian sources | Full smooth positive chain and local dyadic products | Canonical integer-square theta expansion |
| Smooth shape and positive-primitive sources | Both exact constructions and regular coefficient flow | Complete arithmetic source, despite shared decay/shape/primitive data |
| Finite-prime-orbit sources | The general positive-source structures within their stated regularity domains | Full reflection and unchanged infinite arithmetic data |
| Atomic/finite-profile families | Finite chains and exact height motion; smooth extensions where recorded | Complete theta profile/arithmetic; atomic thresholds also fail eventual simplicity |
| RH-conditional endpoint controls | General source-based representations | Ordinary Dirichlet-series arithmetic; their construction remains conditional |
| Fixed source with altered readout | The unchanged source chain | The literal Fourier observation and its Newman equation |

No identical rank or coefficient-decay estimate is assigned to every
control. A future theta-specific inequality must be checked against the
actual witnesses and identify its distinguishing premise. This screen
limits generic arguments, not the possibility of a useful exact network.

## 9. Provisional direction without opening a branch

A possible later umbrella is **exact recursive representations of height
and Newman time**, with the Jacobi/Volterra construction and exact scale
products compared before choosing a physical tensorization. The chain
route currently gives the most concrete continuous family; dyadic products
most directly realize the proposed factors approaching identity. It is
reasonable to leave both in play during conceptual exploration.

No branch number or new live task family is assigned. QTT-B01 remains
unactivated. The next discussion can select which recursion would make
an interesting theorem easier and what information its coefficients must
retain. The [reference record](references/EXACT_HEIGHT_REFERENCES_20261113.md)
and [same-assistant check](reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md)
state the evidence scope.
