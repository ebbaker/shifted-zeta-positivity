# Degree induction, truncation and zero control

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The current local rollout's
`turn_context` records **gpt-6-astra**, effort **max**; this is recorded
configuration, not separate backend attestation. The paginated chat
registry itself currently records no model configurations.

**Status: exploratory continuation and explanatory derivations.** No
theta zero-preserving induction has been found or claimed. No execution
campaign, manuscript milestone, independent assessment or change to the
completed opening round is implied.

**Author's subsequent direction, 16 November:** focus on the chain and a
controlled omitted-tail closure, informed by hierarchy methods such as
BBGKY. Section 5's Jensen alternative is retained as discussion history
but is **not being pursued**. A shrinking strip for approximant zeros is
allowed; exact reality at every finite stage is not required. The purpose
is to identify a structural induction, not to enlarge numerical bounds.
The second exchange and its exact memory equation are recorded in §7.

Continue [Note 02](02_VCD_OPEN_BRAINSTORM_CONTINUATION_20261115.md) and the
[shared induction discussion](../../../brainstorm/notes/05_VOLTERRA_INDUCTION_AND_DYADIC_REFINEMENT_20261115.md).
Read the [result index](../../../../../result-summaries/README.md), especially
[cluster 18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and the [avoid index](../../../../../avoid/README.md). Relevant distinctions
are [01: target reformulations](../../../../../avoid/01_restating_the_target.md),
[02: control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [07: scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Edward proposes keeping finitely many polynomial modes and approximating
the higher modes, with the useful height range increasing with degree.
He asks whether an inductive finite version of RH could then pass to the
limit. This is a valid proof architecture once both approximation and
zero control have been supplied; the latter is a distinct missing input.

## 1. Polynomial and operator dictionary

At fixed real Newman time let
\[
 d\mu_\lambda=W_\lambda(u)\,du/Z_\lambda,\qquad
 F_\lambda(z)=2H_\lambda(z)/Z_\lambda.
\]
For monic polynomials, \(h_n=\int P_n^2W_\lambda\,du\) is a
**squared norm**. The orthonormal polynomials for the unnormalized weight
are \(p_n=P_n/\sqrt{h_n}\); for \(\mu_\lambda\) they are
\(q_n=\sqrt{Z_\lambda}p_n\), with \(q_0=1\).
\[
 uP_n=P_{n+1}+\beta_nP_{n-1},\quad
 \beta_n=h_n/h_{n-1},\quad a_n=\sqrt{\beta_n},\quad\beta_0=a_0=0.
\]
The link \(a_n\) connects sites \(n-1,n\). In the orthonormal basis,
\[
 J=\begin{pmatrix}0&a_1&0&\cdots\\a_1&0&a_2&\cdots\\
 0&a_2&0&\ddots\\\vdots&\vdots&\ddots&\ddots\end{pmatrix},\qquad
 F_\lambda(x)=\langle e_0,e^{ixJ(\lambda)}e_0\rangle.
\]
Multiplication by \(u\) becomes \(J\), and multiplication by
\(e^{ixu}\) becomes \(e^{ixJ}\). The scalar observation is its first
matrix element. Its zeros are not eigenvalues of \(J\) or roots of
\(P_n\). Those polynomial roots belong to the source variable \(u\).

There is no supplied series \(H=\sum_n P_n\). One may expand
\(e^{izu}=\sum_n c_n(z)q_n(u)\) in the weighted space, but
\(c_0(z)=F_\lambda(z)\). Merely keeping the first terms of that exact
expansion already presupposes the scalar being computed. A finite matrix
evolution or a separately controlled expansion is the constructive step.

The time identities, derived in the [manuscript](../../manuscript/main.tex), are
\[
 \partial_\lambda\log h_n=\beta_n+\beta_{n+1},\qquad
 \partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1}),\qquad
 \partial_\lambda a_n=\tfrac12a_n(\beta_{n+1}-\beta_{n-1}).
\]
Also \(\partial_\lambda H=-\partial_z^2H\). Induction at \(\lambda=0\)
would suffice for RH; a descent in Newman time is an available strategy,
not a logical requirement of a degree argument.

## 2. What the existing suggestion actually supplies

The concrete chain is
\[
 \text{source identity/inequality}\ \longrightarrow\
 \text{coefficient control}\ \longrightarrow\
 \frac{h_N}{h_0}=\prod_{j=1}^N\beta_j\ \longrightarrow\
 \text{scalar approximation error}.
\]
The inherited envelope is
\[
 \beta_n+\beta_{n+1}\le B_n,
 \qquad B_n=\operatorname{arcosh}^2(2n+12)/16,
 \qquad 0\le\lambda\le1/2.
\]
It is proved separately at every degree by integration by parts and
confinement, not by an already discovered nontrivial induction in
\(\beta_n\). The norm-product propagation itself is elementary induction.
A stronger future induction could retain neighboring relations, a norm
product bound, source integrals or derivative information.

The closure problem is visible in
\[
 \beta_{n+1}=\beta_{n-1}+\partial_\lambda\log\beta_n.
\]
A value bound on \(\beta_n\) does not bound its derivative. Nor does a
finite prefix evolve autonomously: its boundary equation needs the next
coefficient. Any proposed invariant must supply these missing quantities.

For \(V_\lambda=-\log W_\lambda\), the source-dependent identity
\[
 \int V_\lambda'P_nP_{n-1}W_\lambda\,du=n h_{n-1}
\]
follows by integrating \((P_nP_{n-1}W_\lambda)'\) and using
orthogonality. A Gaussian gives \(\beta_n=n\sigma^2\). A quartic
weight \(e^{-u^4+tu^2}\) gives
\[
 n=4\beta_n(\beta_{n-1}+\beta_n+\beta_{n+1})-2t\beta_n.
\]
This illustrates finite closure, not a theta identity or an automatic
forward stability theorem. The theta score contains the complete sum;
no corresponding useful finite closure is established here. See the
[checked references](../../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md).

## 3. A precise truncation and its growing height window

Fix \(\lambda\), and let \(J_N\) be the leading \(N\)-site block.
Define
\[
 F_{\lambda,N}(z)=\langle e_0,e^{izJ_N}e_0\rangle
      =\sum_{j=1}^N w_{j,N}e^{iz u_{j,N}},\quad
 w_{j,N}>0,\quad\sum_jw_{j,N}=1.
\]
The nodes \(u_{j,N}\) are the zeros of \(P_N\); this is Gaussian
quadrature for \(\mu_\lambda\). Its moments agree through degree
\(2N-1\). A walk from site zero must take at least \(2N\) steps to
cross the removed link and return. Thus the Taylor expansions in
observation variable \(z\) agree through that degree as well.
The approximation uses \(\beta_1,\ldots,\beta_{N-1}\); its first
remainder factor also uses \(\beta_N\).

The manuscript's cosine Hermite-interpolation argument, at this fixed
weight, gives for real \(x\)
\[
 |F_\lambda(x)-F_{\lambda,N}(x)|
 \le \frac{|x|^{2N}}{(2N)!}\frac{h_N(\lambda)}{h_0(\lambda)}
 \le \left[\frac{e|x|\operatorname{arcosh}(2N+10)}{8N}\right]^{2N}.
\]
The last inequality uses the inherited envelope and
\((2N)!\ge(2N/e)^{2N}\). For any fixed \(0<r<1\), the explicit
choice
\[
 X_N=\frac{8rN}{e\operatorname{arcosh}(2N+10)}
\]
therefore gives normalized absolute error at most \(r^{2N}\) on
\(|x|\le X_N\), uniformly for the stated \(\lambda\)-range.
The scale is \(N/\log N\). This is a direct explanatory consequence
of the existing bound, not a new sharp depth estimate or zero result.
The moving-weight truncation here should not be confused with the fixed
\(J_*\), heat-weighted readout used by branch 02 and manuscript §5.

For completeness, **compact complex convergence** also has an elementary
argument; it need not be assumed from real-axis convergence. Write
\(m_{2k}=\int u^{2k}\,d\mu_\lambda\) and let \(m_{2k,N}\) be the
quadrature moments. For \(k<N\) they agree. For \(k\ge N\), Hermite
interpolation of \(u^{2k}\) at the quadrature nodes has nonnegative
remainder, because its \(2N\)-th derivative is nonnegative everywhere.
Consequently
\[
 0\le m_{2k,N}\le m_{2k},\qquad
 \sup_{|z|\le R}|F_\lambda(z)-F_{\lambda,N}(z)|
 \le\sum_{k=N}^\infty\frac{m_{2k}R^{2k}}{(2k)!}\longrightarrow0.
\]
The series sums to \(\int\cosh(Ru)\,d\mu_\lambda<\infty\), by the
theta tails. Evenness removes odd terms. This argument is at fixed time
and fixed compact radius; the displayed real-height estimate is not
silently asserted on complex growing disks. It is generic approximation
theory and supplies no zero restriction. This explanatory derivation has
not received a separate assessment.

## 4. What must be preserved to pass a zero statement to the limit

If entire real-symmetric approximants \(G_N\) converge locally uniformly
on \(\mathbb C\) to the nonzero function \(F_0\), and all their zeros
inside \(|z|<R_N\) are real with \(R_N\to\infty\), then \(F_0\)
has only real zeros. A small disk about any hypothetical nonreal zero
lies eventually in the permitted region, contradicting Hurwitz (or
Rouché). Global real-rootedness of every \(G_N\) is stronger than needed.
This is a standard limit mechanism, not a newly established property of
the theta approximants.

For a specified arbitrary family \(G_N\), its finite real-zero property
may be stronger than RH; necessity has not been proved. Conversely, an
exhausting sequence of statements that the **actual** \(H_0\) has no
nonreal zero in each region is collectively RH itself. The useful new
work would be a closed induction establishing those statements.

Bare Jacobi truncation is not generically zero-preserving. For a
unit-variance Gaussian, \(F(z)=e^{-z^2/2}\), \(\beta_1=1\),
\(\beta_2=2\), and three-node quadrature gives
\[
 F_3(z)=\frac23+\frac13\cos(\sqrt3z).
\]
It vanishes at
\[
 z=\frac{(2k+1)\pi\ \pm i\operatorname{arcosh}2}{\sqrt3},
 \qquad k\in\mathbb Z.
\]
The exact Gaussian has no zeros. This elementary calculation excludes
only a generic assertion that real source-polynomial roots force real
zeros of the finite Fourier readout. Gaussian coefficients do not obey
the theta logarithmic envelope; the example is not a test of a proposed
additional theta-specific invariant.

## 5. Possible inductive objects

1. **Coefficient or norm inequalities.** Carry a closed family of joint
   coefficient/source inequalities. Quantify the gain in the product or
   remainder. This remains an intermediate estimate, not an RH criterion.

2. **A corrected finite approximation and its omitted-tail response.**
   Cutting the chain sets the unresolved boundary response to zero.
   Instead approximate that response with an error bound and update it
   when a site is added. At the resolvent level the exact recurrence is
   \[
    m_k(\zeta)=\langle e_k,(\zeta-J^{(k)})^{-1}e_k\rangle
      =\frac1{\zeta-\beta_{k+1}m_{k+1}(\zeta)},\quad\Im\zeta\ne0.
   \]
   Here \(J^{(k)}\) is the source Jacobi tail starting at site \(k\),
   with its self-adjoint realization, and \(\zeta\) is a resolvent
   variable, not the Fourier variable. The formula follows by block
   elimination at the first site. The theta coefficient growth permits
   the usual determinate tail realization. A finite \(N\)-site section
   corresponds to \(m_N=0\). The exact response is a function, not an
   unknown constant. Its usual half-plane sign controls the source
   spectral measure; it does not prove real Fourier zeros. This is a
   way to organize Edward's higher-mode approximation, with no current
   zero-preserving closure.

3. **Certificates on growing complex regions.** Carry approximants,
   boundary error bounds, real-root brackets and a complete zero count.
   On a conjugation-symmetric disk containing exactly one approximant
   zero, a strict boundary inequality
   \(|H_0-G_N|<|G_N|\) transfers that count to \(H_0\). The unique
   zero must be real by conjugation. An outer contour count, or exclusion
   in the remaining region, must rule out extra pairs. One outer count
   alone does not prove reality. The induction must extend the region
   while retaining these margins; no such theta estimate is supplied.
   Simple-root disks would prove simplicity as well and are stronger
   than RH; multiplicities need a different treatment. Tiny absolute
   errors alone do not suffice: \(z^2+\epsilon\) illustrates the
   instability near a double real zero. The scalar error must be paid
   against the actual boundary margins, including small large-height
   amplitudes.

4. **Polynomials designed to test Fourier zeros.** Jensen polynomials
   use the Taylor coefficients of the completed function, rather than
   the source-orthogonal \(P_n(u)\). For example define the entire
   function
   \[
    G(w)=F_0(i\sqrt w)=\sum_{k\ge0}\gamma_k\frac{w^k}{k!},
    \qquad\gamma_k=\frac{k!m_{2k}}{(2k)!}>0.
   \]
   Evenness makes this independent of a square-root branch. Its
   unshifted Jensen polynomials are
   \(\mathcal J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k\).
   Their scaled limits satisfy \(\mathcal J_d(w/d)\to G(w)\)
   locally uniformly (coefficient domination by the entire positive
   series suffices). Real roots of every \(\mathcal J_d\) would be
   negative and would force real zeros of \(F_0\). With the completed
   theta function's growth, the all-degree statement is the classical
   RH-equivalent Jensen formulation. This is recorded once as a known
   reformulation, not checked numerically as evidence. The question for
   this program would be whether its coefficient dynamics yield a new
   closed hyperbolicity induction. Fixed degree with shift tending to
   infinity is a different quantifier, as the checked GORZ theorem
   makes explicit; it does not supply all degrees at shift zero.

These are alternatives to explore, not a ranked execution plan. The most
direct continuation of Edward's suggestion is to define what boundary
information a finite chain retains, and whether it can support a
quantitative zero certificate as the chain grows. Coefficient control
can serve either that route or other approximation goals.

## 6. Analytical collision-control screen

The [catalog](../../../../../result-summaries/12_collision_controls_and_screening.md)
was checked against the premises above, using the detailed
[existing VCD screen](../../notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md).
No numerical collision certificates were rerun. No unspecified future
zero invariant is represented as tested.

| Catalog family | Premise comparison for this discussion |
| --- | --- |
| Positive three- and four-square sources | Pass the recurrence, envelope, Gaussian quadrature construction and rapid-tail complex-convergence argument. They lack complete canonical equal coefficients and full reflection; the inherited bound does not use those distinctions to exclude them. Thus approximation alone cannot settle the zero question. |
| Three-atom and finite-profile atomic controls | Fail the positive full-line density and logarithmic-score premises; their finite recurrences terminate. Quadrature/finite Fourier observations still exist. The previously checked three-atom event fails the displayed envelope at the specified index. |
| Compact triangular extensions | Fail global strict positivity for the score proof, while compact support suffices for entire Fourier convergence. |
| Euler-factor translates | Fail the unchanged summand-score premise. Actual envelope failure is established for the existing c=1/2, p=23, lambda=0 example only; generic recurrence and rapid-tail approximation remain. |
| Reflected super-Gaussian | Fails the exponential confinement inequality, but has enough exponential moments for the compact-convergence argument. Its individual coefficient-envelope test remains unperformed. |
| Smooth shape and positive-primitive sources | Lack the exact theta square-summand formula; their coefficient-envelope comparison remains untested. Generic positive-measure approximation offers no discriminator. |
| Finite-prime square perturbations | Lack full canonical reflection, even when score bounds and finite measurement matches persist. No conclusion against controlled infinite assembly is inferred. |
| RH-conditional endpoint controls | Lack ordinary Dirichlet arithmetic and the unchanged theta summand formula; retain their RH hypothesis. No new coefficient-envelope comparison. |
| Varied observation with fixed source | Retains all source coefficients, but fails the literal Fourier/Newman observation required here. |
| Actual-profile positive-measure relaxation | Does not supply the same full-line source and physical Fourier observation. No new coefficient test. |

A successful theta zero argument must establish a premise or quantitative
margin that fails for the applicable colliding controls. At present the
generic approximation premises do not do that. This is not an exclusion
of coefficient induction, corrected tails, Jensen arguments or growing
height certificates.

The new branch-only chat is registered in this investigation's
[history folder](../../chat-histories/README.md). Its actual public final
must be captured after it is recorded; no planned response belongs in
the transcript.

## 7. Tail closure, hierarchy consistency and shrinking zero strips

Second exchange, 16 November 2026. Prepared for Edward Baker with OpenAI
Codex assistance; recorded current turn configuration gpt-6-astra / max.
These are explanatory identities, a standard conditional limiting
argument, and questions for an induction. No new theta exclusion estimate
or independently assessed theorem is claimed. Continue to apply
[avoid 03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
to the exact representation and
[avoid 10](../../../../../avoid/10_numerics_ahead_of_the_question.md)
to any later numerical suggestion.

### Endpoint insertion versus truncating the dynamics

In the polynomial basis, Edward's inserted identity gives
\[
 \sum_\mu\langle e_0,e_\mu\rangle
       \langle e_\mu,e^{ixJ}e_0\rangle
 =\langle e_0,e^{ixJ}e_0\rangle
\]
because the first factor is \(\delta_{0\mu}\). With
\(\Pi_N=\sum_{\mu=0}^{N-1}|e_\mu\rangle\langle e_\mu|\),
inserting \(\Pi_N\) at the endpoints leaves the scalar unchanged.
The different operation is replacing the retained part of the exact
propagator by \(e^{ixJ_N}\); in general
\[
 \Pi_N e^{ixJ}\Pi_N\big|_{\operatorname{ran}\Pi_N}
 \ne e^{ixJ_N}.
\]
The difference consists of excursions through the omitted sites and
back. This also explains why the constant-polynomial coefficient is
\(F\) while all degrees still influence its computation. Edward
acknowledged the collapsing-sum point during this exchange.

An intermediate insertion is nontrivial:
\[
 F(x)=\sum_{\mu\ge0}
  \langle e_0,e^{ixJ/2}e_\mu\rangle
  \langle e_\mu,e^{ixJ/2}e_0\rangle.
\]
These are not modulus squares: both propagators have the same sign.
For the real symmetric Jacobi chain the two entries are equal; odd/even
parity gives alternating signed squares for real \(x\). Truncating
this sum still requires control of the full-chain entries being used.

**Author's midpoint clarification, 16 November 2026.** Edward confirms
that splitting the evolution in half was the intended insertion and asks
about bra/ket conventions. With the standard convention
\(\langle v,w\rangle=v^*w\), put \(U(t)=e^{itJ}\) for real \(t\).
The bra associated with \(U(t)e_0\) is \(e_0^*U(-t)\). Consequently
\[
 \langle U(t)e_0,U(t)e_0\rangle=1,
 \qquad F(x)=\langle U(-x/2)e_0,U(x/2)e_0\rangle.
\]
Inserting the identity between these two states gives the nontrivial
midpoint sum above. If \(c_n(t)=\langle e_n,U(t)e_0\rangle\), reality
and symmetry of the Jacobi matrix give
\[
 F(x)=\sum_{n\ge0}c_n(x/2)^2,
 \qquad \sum_{n\ge0}|c_n(x/2)|^2=1.
\]
The first series is absolutely convergent on the real axis by the second.
Thus the intended pairing can also be written as the bilinear transpose
\((U(x/2)e_0)^T(U(x/2)e_0)\), rather than the Hermitian norm.
This is a convention clarification of the existing representation, not
a new closure or induction estimate. The generic identities also hold
for the regular real Jacobi controls in the §6–7 screen and supply no
source-specific discriminator. Prepared for Edward Baker with OpenAI
Codex assistance; this exchange records gpt-6-astra / max.

### Exact elimination of the omitted tail

Freeze \(\lambda\). Here \(x\) is the evolution variable; it is
observation height, not Newman time. Put
\(\psi(x)=e^{ixJ}e_0\). The amplitude hierarchy is
\[
 \psi_n'=i(a_n\psi_{n-1}+a_{n+1}\psi_{n+1}),\qquad
 \psi_n(0)=\delta_{n0},\qquad F_\lambda(x)=\psi_0(x).
\]
Keep sites \(0,\ldots,N-1\), writing \(\psi=(y,v)\) and
\[
 J=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\quad
 A=J_N,\quad D=J^{[N]},\quad
 B=a_N|e_{N-1}\rangle\langle e_N|.
\]
The tail initially vanishes. Variation of constants gives
\[
 v(x)=i\int_0^x e^{i(x-s)D}B^*y(s)\,ds,
 \qquad
 y'=iAy-\int_0^x B e^{i(x-s)D}B^*y(s)\,ds. \tag{M}
\]
In scalar-boundary form, with
\(k_N(t)=\langle e_N,e^{itJ^{[N]}}e_N\rangle\), this is
\[
 y'(x)=iJ_Ny(x)
 -\beta_N e_{N-1}\int_0^x k_N(x-s)y_{N-1}(s)\,ds. \tag{MB}
\]
The minus sign is from the two factors of \(i\); the boundary coupling
is \(a_N^2=\beta_N\). This is exact for real \(x\), with oriented
integrals for negative \(x\). For the theta coefficients, removing
one edge is a bounded finite-rank perturbation of the self-adjoint
chain; its decoupled tail supplies the self-adjoint \(D\). The basis
vectors lie in the required domains, so the unitary Duhamel argument
justifies (M). No complex operator-norm continuation is asserted.

Setting the whole memory term to zero gives the bare finite chain.
Replacing \(k_N\) by a specified approximate response, with a controlled
residual, is the proposed higher-mode approximation. The initial tail
is zero, so this decomposition has no additional unknown-initial-tail
forcing term. A zero theorem would additionally require holomorphic
approximants and compact complex error control for the chosen closure.

Each tail has the same one-site elimination identity:
\[
 k_n'(x)=-\beta_{n+1}\int_0^x k_{n+1}(x-s)k_n(s)\,ds,
 \qquad k_n(0)=1. \tag{K}
\]
Thus \(k_n''(0)=-\beta_{n+1}\) and
\(k_n^{(4)}(0)=\beta_{n+1}(\beta_{n+1}+\beta_{n+2})\), consistent
with direct Jacobi walks. For real \(s>0\), its Laplace transform obeys
\[
 \widehat k_n(s)=\frac1{s+\beta_{n+1}\widehat k_{n+1}(s)}. \tag{L}
\]
The bound \(|k_n(x)|\le1\) makes these transforms legitimate. Equation
(L) is equivalent to the earlier resolvent continued fraction with the
appropriate change of variable. It is a response recursion, not a
closed finite system: the next tail is still present. A self-consistent
relation between successive responses would be an additional ansatz;
neither short memory nor a small correlation parameter follows merely
from large polynomial degree.

### Relation to BBGKY and the source identity

BBGKY is a useful closure analogy: the retained level depends on a
higher level, and a replacement must remain consistent with the exact
hierarchy. Here the index is polynomial degree, not particle correlation
order. The exact eliminated-tail formulation is also a simple linear
instance of projection with memory, familiar from Mori–Zwanzig. These
analogies supply organizational ideas, not an imported theta estimate.
The newly checked [primary-source passages](../../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
distinguish memory identities from approximate closures and record the
need to preserve compatibility and other structural properties.

The source identity becomes particularly transparent with
\(q_n=\sqrt{Z_\lambda/h_n}\,P_n\):
\[
 \langle q_n,V_\lambda'q_{n-1}\rangle_{\mu_\lambda}
   =\frac{n}{a_n},\qquad
 a_n[V_\lambda'(J)]_{n,n-1}=n. \tag{S-J}
\]
Indeed the unnormalized integral is
\(\sqrt{h_nh_{n-1}}\langle q_n,V' q_{n-1}\rangle\); divide its
value \(n h_{n-1}\) by that factor. Interpret the matrix element
by multiplication by \(V'\) in the source representation; the theta
tails make the stated polynomial-vector integrals finite.

For polynomial \(V'\), the matrix function is banded and (S-J) gives
a finite coefficient relation. For the theta score it generally
depends on the entire chain. In particular
\(\Pi_N V'(J)\Pi_N\) cannot simply be replaced by \(V'(J_N)\).
A potential self-consistent closure must account for the correction in
this source identity as well as the correction to the propagator.
This is a concrete compatibility question linking the source information
and omitted-tail response; no finite theta closure is yet established.

### Shrinking strips suffice, without finite-stage reality

Let a specified closure produce entire \(G_N\) with
\(G_N\to F_0\) locally uniformly on \(\mathbb C\), where
\(F_0(0)=1\). Suppose \(R_N\to\infty\), \(\delta_N\to0\), and
\[
 G_N(z)=0,\quad |z|<R_N
 \quad\Longrightarrow\quad |\Im z|\le\delta_N. \tag{T}
\]
Then every zero of \(F_0\) is real. If a nonreal zero existed, choose
a sufficiently small disk about it with no boundary zero and positive
distance \(\eta\) from the real axis. Rouché and compact convergence
force a zero of \(G_N\) in that disk for all sufficiently large \(N\).
Eventually the disk lies inside radius \(R_N\) and \(\delta_N<\eta\),
contradicting (T). No pairing or labeling of zeros, simplicity assumption,
or quantitative error-to-spacing relation is needed for this limiting
argument. Such estimates may still be needed to *prove* (T) for the
chosen closure. Even compact-dependent widths \(\delta_N(R)\to0\)
for each fixed \(R\) suffice. When no rate is prescribed, diagonalization
also gives a single shrinking strip across some growing window; these
are qualitatively equivalent formulations. A preassigned window growth
or strip-narrowing rate can impose a stronger requirement.

This is a standard conditional transfer argument, not a proof of (T).
**Classification correction, 16 November setup review:** once the stated
local uniform convergence is established, existence of unspecified
\(R_N\) and \(\delta_N\) in (T) is equivalent to RH. Under RH,
\(F_0\) is bounded away from zero on each compact set
\(\{|z|\le j,\ |\Im z|\ge1/j\}\); uniform convergence excludes
zeros of \(G_N\) there eventually, and diagonalization supplies the
sequences. This corrects the earlier assertion that necessity was not
asserted for (T); that caveat applies to prescribed rates or other
stronger premises, not unspecified existential confinement. The new
research ingredient must be a source-sensitive invariant or estimate
that establishes the target without assuming it. (T) is a candidate
consequence, not necessarily the invariant to carry directly.

### What would constitute an induction advance

The proposed working object is a family of tail descriptions with a
controlled residual, together with source constraints and a structural
property from which a narrowing zero strip follows. Three distinct
questions must be answered:

1. Does the true theta tail belong to the described class, using source
   information rather than a zero-location assumption?
2. Does moving the boundary by one site preserve the class and its paid
   residual information, using (K), (L), or an equivalent update?
3. Does the preserved structure constrain zeros of the scalar Fourier
   observation, strongly enough to yield (T)?

The update is now explicit; the required class and the third implication
are not identified. The continued fraction reconstructs an inward
response from a deeper tail. A forward induction or a justified limiting
boundary condition still has to be supplied; its direction cannot be
silently reversed. Increasing numerical depth alone would answer none
of these structural questions. Edward's preference is to understand
them before choosing an induction hypothesis or numerical work.

The [§6 control screen](#6-analytical-collision-control-screen) remains
applicable, with these additional premise checks. Exact projection,
memory and continued fractions hold for the regular Jacobi controls
too (finite atomic chains terminate). The own-source integration-by-parts
identity also holds for the regular positive-density controls; atoms
lack that density/score premise. A control's own-score identity is not
the identity with the unchanged canonical theta score. The controls
lacking that source formula do not establish the canonical constraint,
but no new calculation here proves failure of a particular adjacent
canonical-score matrix element. Generic positive spectral measures and
their resolvent half-plane signs control source spectral data, not
Fourier zeros. The three- and four-square controls continue to pass the
existing envelope; they lack complete equal coefficients and full
reflection. All other family's failed premises and untested envelope
comparisons are as listed in §6. No proposed theta-specific closure has
yet been screened because none has been formulated. These statements
exclude only an inference from the shared generic properties.

**Capture status at this update:** the previous exact-turn worker and
this turn's initial refresh both failed with `unsupported_public_content`
(`Structured assistant content requires a preserving exporter`). The
existing registry remains at its verified five-message capture of
2026-11-16T05:24:10.646Z. It does not contain the preceding final reply.
No source adapter, registered transcript, integrity check or hook trust
was changed. This note preserves the mathematics, not a replacement
conversation transcript; final capture will again be attempted through
the prescribed bounded workflow.
