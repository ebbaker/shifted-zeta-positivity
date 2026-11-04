# Radial Green identities for the coefficient determinants and their equilibrium interpretation

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Affiliation: Mellin-curvature brainstorm, chat0004.

**Status: exact analytical reformulation, with same-assistant exact rational
algebra checks.** All formulas concern the complete theta source at physical
heat time zero. They supply no determinant sign theorem or identification
with an ordinary quantum kinetic-energy expectation.

The radial Green identity transfers every source Laplacian to an explicit
symmetric polynomial probe. The result is a finite, fully normalized
boundary expansion of \(D_{r,k}\) involving only the undifferentiated theta
primitive. Its volume term has an exact equilibrium interpretation at one
fixed temperature for classical spatial particles with quantum internal
levels. The original box interpretation instead retains an integral over
inverse temperature. These are two interpretations of the same integrals
with different physical degrees of freedom.

This develops [Note05](05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md)
and the scalar identity in [Radial Note73][radial73]. It retains the user's
conventions: \(u\) is not a quantum particle coordinate; equilibrium weights
are unfiltered; source factors remain observables; quantum many-particle
notation uses creation and annihilation operators.

**Author-selected continuation, 4 November 2026:** The
[radial Green determinant investigation](../../10_radial_green_determinants/README.md)
continues the mathematical development in Sections 1–6 independently of
the thermodynamic interpretations below. Those interpretations remain
historical discussion; the new overview leaves physical meaning open.

## 1. Source, primitive and determinant conventions

Set
\[
E_n=\pi n^2,\qquad Q(\beta)=\sum_{n\ge1}e^{-\beta E_n},
\qquad R=e^{2u},\quad\beta=R^2=e^{4u},
\]
\[
A(R)=Q(R^2),\qquad p(u)=e^uQ(e^{4u})=R^{1/2}A(R).
\tag{1}
\]
The one-particle Dirichlet box realization has eigenfunctions
\(\sqrt2\sin(n\pi x)\), \(0<x<1\), with
\(h=-\pi^{-1}\partial_x^2\). Its fermionic second quantization is
\[
\widehat H_{\rm box}=\sum_{n\ge1}E_n d_n^\dagger d_n,\qquad
\{d_m,d_n^\dagger\}=\delta_{mn}.
\tag{2}
\]
Here \(Q\) is the trace in the **one-particle sector**. It is not the
fixed-\(N\) fermion partition function when \(N>1\).

The complete source and coefficient convention are
\[
\Phi(u)=\sum_{n\ge1}
(2E_n^2e^{9u}-3E_ne^{5u})e^{-E_ne^{4u}},
\]
\[
m_j(u)=\frac{u^{2j}}{(2j)!}\quad(j\ge0),\qquad
m_j=0\quad(j<0),
\]
\[
c_j=\int_0^\infty\Phi(u)m_j(u)\,du\quad(j\ge0),\qquad
c_j=0\quad(j<0),
\qquad
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}.
\tag{3}
\]
Throughout \(r\ge1\) and \(k\ge0\). Every polynomial moment below converges
absolutely. On \(R\ge1\) the complete theta series and all derivatives used
here converge uniformly on compact sets, with Gaussian decay at infinity.
In \(u\), their decay dominates every polynomial and every exponential
needed in these calculations.

## 2. The radial identity and its endpoint constant

For \(a>0\), direct differentiation gives
\[
\partial_R e^{-aR^2}=-2aRe^{-aR^2},\qquad
\Delta_3 e^{-aR^2}
=(4a^2R^2-6a)e^{-aR^2},
\quad
\Delta_3=\partial_R^2+\frac2R\partial_R.
\]
Consequently
\[
\boxed{\Phi(u)=\frac12R^{5/2}\Delta_3A(R).}
\tag{4}
\]
In dimension \(d\), the second coefficient is \(-2da\). Matching the
source's \(-3E_nR^{5/2}\) after the factor \(R^{5/2}/2\) selects \(d=3\).
The mode sum remains the one-dimensional square spectrum; no
three-dimensional lattice sum has been substituted.

For a polynomial probe \(f\), or a smooth probe satisfying the same tail
and endpoint conditions, define
\[
F(R)=R^{-1/2}f(u),\qquad u=\tfrac12\log R.
\]
Its derivatives are
\[
F'(R)=\frac12R^{-3/2}(f'-f),\qquad
\boxed{\Delta_3F(R)=\frac14R^{-5/2}(f''-f).}
\tag{5}
\]
Primes on \(f\) denote \(u\)-derivatives. Since \(du=dR/(2R)\),
\[
\int_0^\infty\Phi f\,du
=\frac14\int_1^\infty F\,\Delta_3A\,R^2\,dR.
\]
Radial Green's identity, including the inward-facing boundary of the
exterior region, gives
\[
\int_1^\infty(F\Delta_3A-A\Delta_3F)R^2\,dR
=[R^2(FA'-AF')]_1^\infty.
\]
The outer boundary vanishes, so
\[
\int_0^\infty\Phi f\,du
=\frac14\int_1^\infty A\,\Delta_3F\,R^2\,dR
+\frac14[-A'(1)F(1)+A(1)F'(1)].
\tag{6}
\]

For completeness, the normalized theta reflection is
\[
\Theta(R)=1+2A(R)=R^{-1}\Theta(1/R).
\]
Differentiating at \(R=1\) yields
\[
\Theta'(1)=-\tfrac12\Theta(1),\qquad
A'(1)=-\tfrac12A(1)-\tfrac14.
\tag{7}
\]
Thus \(p(0)=A(1)\), \(p'(0)=A(1)+2A'(1)=-1/2\).
Substituting (5) and (7) into (6), with
\(F(1)=f(0)\) and \(F'(1)=(f'(0)-f(0))/2\), proves
\[
\boxed{
\mathscr L[f]:=\int_0^\infty\Phi f\,du
=b f(0)+\frac{p(0)}8 f'(0)
+\frac18\int_0^\infty p(u)(f''-f)\,du,\qquad b=\frac1{16}.}
\tag{8}
\]
Equivalently \(p''-p=8\Phi\); integrating this identity twice gives the
same boundary expression. The constant \(1/16\) comes from complete
theta reflection, not from discarding the inner sphere.

## 3. Primitive moments and the determinant matrix

Define
\[
d_j=\int_0^\infty p(u)m_j(u)\,du\quad(j\ge0),\qquad d_j=0\quad(j<0).
\]
For every integer \(j\), \(m_j''=m_{j-1}\),
\(m_j'(0)=0\), and \(m_j(0)=\delta_{j0}\).
Therefore (8) gives
\[
\boxed{c_j=b\delta_{j0}+\frac18(d_{j-1}-d_j).}
\tag{9}
\]
For negative \(j\), both sides are zero under the conventions above.
In particular \(c_0=b-d_0/8\); the endpoint constant must be retained.

Writing \(C_{ij}=c_{k+j-i}\), the decomposition is
\[
C=B+M,\qquad
B_{ij}=b\delta_{i,k+j},\qquad
M_{ij}=\frac18(d_{k+j-i-1}-d_{k+j-i}).
\tag{10}
\]
The endpoint matrix has rank \(\max(r-k,0)\). Hence \(k\ge r\) gives a
pure primitive-moment determinant. For smaller \(k\), multilinearity
produces endpoint minors as well as the full volume determinant.
The following integral formula identifies every one of these terms.

## 4. A symmetric multiparticle probe for the same determinant

Use \(r\) variables \(u_0,\ldots,u_{r-1}\) and define
\[
T_{r,k}(\mathbf u)=
\det[m_{k+j-i}(u_i)]_{i,j=0}^{r-1},
\qquad
\mathcal T_{r,k}(\mathbf u)=
\frac1{r!}\sum_{\sigma\in S_r}
T_{r,k}(u_{\sigma(0)},\ldots,u_{\sigma(r-1)}).
\tag{11}
\]
Expanding the first determinant shows
\[
\begin{aligned}
\int_{[0,\infty)^r}\prod_i\Phi(u_i)T_{r,k}(\mathbf u)\,d\mathbf u
&=\sum_{\tau\in S_r}\operatorname{sgn}(\tau)
\prod_{i=0}^{r-1}
\int_0^\infty\Phi(u_i)m_{k+\tau(i)-i}(u_i)\,du_i\\
&=\det[c_{k+j-i}].
\end{aligned}
\]
The measure and domain are permutation-invariant, so symmetrizing leaves
the integral unchanged:
\[
\boxed{D_{r,k}=\int_{[0,\infty)^r}
\prod_i\Phi(u_i)\mathcal T_{r,k}(\mathbf u)\,d\mathbf u.}
\tag{12}
\]
There is no additional \(r!\) in (12). The factor in (11) is an average.
Every coordinate enters \(\mathcal T\) evenly.

This is an alternative integrand for the desired determinant. It avoids
the determinant of high derivatives of \(\Phi\) in Note05 by moving the
Toeplitz structure into a polynomial observable from the beginning.
The polynomial is prescribed by the coefficient problem; its symmetry
does not identify it with a fermionic density or make it nonnegative.

## 5. Transfer of all radial derivatives and every boundary face

Put \(L_i=\partial_{u_i}^2-1\). For \(0\le q\le r\), define
\[
W_{r,k}^{(q)}(u_0,\ldots,u_{q-1})=
\left[
\left(\prod_{i=0}^{q-1}L_i\right)\mathcal T_{r,k}(u_0,\ldots,u_{r-1})
\right]_{u_q=\cdots=u_{r-1}=0}.
\tag{13}
\]
For \(q=0\), this is the scalar \(\mathcal T_{r,k}(0,\ldots,0)\).
For \(q=r\), no evaluation at zero is performed.
In particular the full-volume probe can be written without derivatives:
\[
W_{r,k}^{(r)}(\mathbf u)=\operatorname{Sym}_{\mathbf u}
\det[m_{k+j-i-1}(u_i)-m_{k+j-i}(u_i)]_{i,j=0}^{r-1},
\]
where \(\operatorname{Sym}\) uses the average in (11).

Apply (8) in each coordinate of (12). Every remaining probe is even in
each unevaluated coordinate, so all \(p(0)f'(0)/8\) contributions vanish.
For any subset \(S\) of coordinates left in the volume, the resulting
term is
\[
b^{r-|S|}8^{-|S|}
\int_{[0,\infty)^{|S|}}
\prod_{i\in S}p(u_i)
\left[
\prod_{i\in S}L_i\,\mathcal T_{r,k}(\mathbf u)
\right]_{u_j=0,\ j\notin S}\,d\mathbf u_S.
\]
Symmetry makes all subsets of the same cardinality equal. Thus
\[
\boxed{
D_{r,k}=
\sum_{q=0}^r\binom rq b^{r-q}8^{-q}
\int_{[0,\infty)^q}
\prod_{i=0}^{q-1}p(u_i)
W_{r,k}^{(q)}(\mathbf u)\,d\mathbf u.}
\tag{14}
\]
The zero-dimensional integral means its scalar integrand.
This is the complete Green expansion. All energy-derivative insertions
have left the theta weight.

The calculation uses the full orthant. Ordering radii first would
introduce collision faces that would need separate accounting.
There are no such artificial faces in (14). A coordinate evaluated at
zero is the genuine inner sphere \(R=1\).

More precisely,
\[
W_{r,k}^{(q)}\equiv0\quad\text{if }q<\min(k,r).
\tag{15}
\]
To see this before symmetrization, an endpoint row of the matrix in
(11) has entries \(\delta_{k+j-i,0}\). Such a row can be nonzero only for
\(i\ge k\). There are at most \(r-k\) available nonzero endpoint rows
when \(k<r\), and none when \(k\ge r\). If more rows are assigned to
the endpoint, every summand vanishes. Differentiating the other
coordinates does not alter this fact. Averaging over their assignments
proves (15).

In particular, for \(k\ge r\),
\[
\boxed{
D_{r,k}=\frac1{8^r}
\int_{[0,\infty)^r}
\prod_i p(u_i)W_{r,k}^{(r)}(\mathbf u)\,d\mathbf u.}
\tag{16}
\]
For \(k<r\), the \(q<r\) terms in (14) are generally nonzero.

A direct three-dimensional normalization check is also useful.
For radial probes,
\[
\Phi(u)f(u)\,du
\longleftrightarrow
\frac1{16\pi}(\Delta_3A)(R)R^{-1/2}f(\tfrac12\log R)\,d^3\mathbf R.
\]
Transferring all \(r\) Laplacians gives the full-volume term
\[
\frac1{(64\pi)^r}
\int_{\Omega^r}
\prod_i\left[A(R_i)R_i^{-5/2}\right]
W_{r,k}^{(r)}(\tfrac12\log\mathbf R)\,d^{3r}\mathbf R,
\quad \Omega=\{\mathbf R:|\mathbf R|\ge1\},
\tag{17}
\]
where the shorthand logarithm means the vector of logarithms of the
radii. Since \(R^{-5/2}d^3\mathbf R=8\pi R^{1/2}du\)
after angular integration, (17) is exactly (16)'s volume expression.
For \(k<r\), (17) must be accompanied by (14)'s boundary terms.

## 6. Explicit low-order checks

For \(r=1\), \(\mathcal T_{1,k}=m_k\),
\(W^{(0)}=\delta_{k0}\), and \(W^{(1)}=m_{k-1}-m_k\).
Equation (14) reduces to (9).

For \(k=0\), the unsymmetrized matrix in (11) is upper triangular with
unit diagonal. Hence
\[
\mathcal T_{r,0}=1,\quad W_{r,0}^{(q)}=(-1)^q,\quad
D_{r,0}=(b-d_0/8)^r=c_0^r.
\tag{18}
\]
This checks all boundary multiplicities at once.

The first example with a nontrivial surviving face is \(r=2,k=1\):
\[
\mathcal T_{2,1}(u,v)=m_1(u)m_1(v)
-\tfrac12[m_2(u)+m_2(v)],
\]
\[
W^{(0)}=0,\qquad
W^{(1)}(u)=-\tfrac12[m_1(u)-m_2(u)],
\]
\[
\begin{aligned}
W^{(2)}(u,v)
={}&[1-m_1(u)][1-m_1(v)]\\
&+\tfrac12[m_1(u)-m_2(u)+m_1(v)-m_2(v)].
\end{aligned}
\tag{19}
\]
Substitution into (14) gives
\[
\begin{aligned}
D_{2,1}
&=-\frac b8(d_1-d_2)
+\frac1{64}\{(d_0-d_1)^2+d_0(d_1-d_2)\}\\
&=\left(\frac{d_0-d_1}{8}\right)^2
-\left(b-\frac{d_0}{8}\right)
 \left(\frac{d_1-d_2}{8}\right)
=c_1^2-c_0c_2.
\end{aligned}
\tag{20}
\]
Omitting the one-coordinate face would lose \(-b(d_1-d_2)/8\).

The [exact algebra checker][checker] constructs (11), applies (13),
and integrates monomials symbolically using
\(\int p(u)u^{2j}du=(2j)!d_j\). It compares the result with an independent
permutation expansion of the determinant in (9), treating \(b,d_0,d_1,\ldots\)
as formal indeterminates. All 25 cases
\(1\le r\le5,\ 0\le k\le r+1\) pass, including (15), (18), and the
explicit probes (19); the [execution record][record] preserves scope and
the script hash. This checks exact algebra and factors, not theta signs.
The general proof is the coordinatewise argument above.

## 7. What remains thermodynamic in the original box

Keeping the physical meaning of (2),
\[
p(u)\,du=\frac14\beta^{-3/4}Q(\beta)\,d\beta,\qquad \beta\ge1.
\tag{21}
\]
For example,
\[
\int p(u)f(u)\,du
=\frac14\int_1^\infty\beta^{-3/4}
\operatorname{Tr}_{N=1}(e^{-\beta\widehat H_{\rm box}})
f(\tfrac14\log\beta)\,d\beta.
\]
Equation (14) eliminates the energy-inserted traces, but does not make
the integration variables \(\beta_i\) equal. It is still an integrated
thermodynamic functional of the box family. Declaring
\(R_i=\sqrt{\beta_i}\) alone does not change this.

The \(N\)-particle box equilibrium state and its TFD obey
\[
\rho_{\beta,N}=
\frac{\Pi_Ne^{-\beta\widehat H_{\rm box}}\Pi_N}{Z_N(\beta)},
\qquad
\langle\widehat O\rangle_{\beta,N}
=\langle\mathrm{TFD}_{\beta,N}|
\widehat O_L|\mathrm{TFD}_{\beta,N}\rangle.
\tag{22}
\]
No change of purification turns (21) into a trace at one fixed
\(\beta\), and \(Q^r\) does not become \(Z_r\) for box fermions.

## 8. An exact fixed-temperature configurational interpretation

There is a different, explicit physical interpretation. Let
\(\mathbf R\in\Omega\) be an actual classical spatial coordinate, let
\(n\ge1\) be an internal energy label, and choose the bath inverse
temperature \(\beta_*=1\) in the units of (1). Give the particle potential
\[
V_n(\mathbf R)=E_n|\mathbf R|^2=\pi n^2R^2.
\tag{23}
\]
Equivalently the local internal Hamiltonian is
\(\widehat V(\mathbf R)=R^2h\), with \(h\) the one-particle box operator.
The spatial dependence changes the local level spacing while the bath
temperature stays fixed.

The ordinary, unfiltered configurational Gibbs distribution is
\[
Z_{\rm conf}=\sum_{n\ge1}\int_\Omega e^{-V_n(\mathbf R)}\,d^3\mathbf R,
\qquad
d\gamma(\mathbf R,n)=Z_{\rm conf}^{-1}e^{-V_n(\mathbf R)}d^3\mathbf R.
\tag{24}
\]
The sum and integral are finite. Classical momenta with an independent
kinetic energy can be included; their common Gaussian factor cancels
from the normalized position observables used here. At other bath
temperatures the potential remains (23), and the local partition sum
becomes \(A(\sqrt{\beta_*}R)\); the displayed canonical theta identities
are evaluated at the reference temperature \(\beta_*=1\).

Summing the internal label at a fixed position gives
\[
\sum_n e^{-V_n(\mathbf R)}=A(R).
\]
The force interpretation is exact:
\[
\Delta_3 e^{-V_n}
=e^{-V_n}(|\nabla V_n|^2-\Delta_3V_n),
\qquad
|\nabla V_n|^2-\Delta_3V_n
=4E_n^2R^2-6E_n.
\tag{25}
\]
The same quantity is force squared plus the divergence of the force.
Thus the old energy insertion has become a spatial force/curvature
observable in a single bath.

Keep the radial measure factor in the observable, as requested:
\[
J(R)=\frac1{8\pi R^{5/2}},\qquad
\boxed{\int_0^\infty p(u)f(u)\,du
=Z_{\rm conf}\left\langle
J(R)f(\tfrac12\log R)\right\rangle_\gamma.}
\tag{26}
\]
Indeed \(4\pi R^2J(R)dR=\frac12R^{-1/2}dR\), which is
exactly \(p(u)du/A(R)\). There is no \(J\)-filtered Gibbs state.

One can first represent the determinant without integrating by parts.
For \(P_0(x)=2x^2-3x\),
\[
P_0(V_n)=\frac{R^2}{2}
(|\nabla V_n|^2-\Delta_3V_n),
\qquad
\int\Phi f\,du
=Z_{\rm conf}\langle J(R)P_0(V_n)f(\tfrac12\log R)\rangle_\gamma.
\tag{27}
\]
Let \(\langle\cdot\rangle_{q,1}\) denote the fixed-temperature canonical
configurational average for \(q\) noninteracting classical particles
with these internal levels. For symmetric observables it is the product
average under \(\gamma^{\otimes q}\). The indistinguishability factor
\(1/q!\) appears in the partition function
\(Z_q^{\rm conf}=Z_{\rm conf}^q/q!\) and cancels from the normalized
average. No quantum exclusion rule is imposed.

Combining (12) and (27), **for every \(r,k\)**,
\[
\boxed{
D_{r,k}=Z_{\rm conf}^r
\left\langle
\mathcal T_{r,k}(\tfrac12\log R_0,\ldots,\tfrac12\log R_{r-1})
\prod_{i=0}^{r-1}J(R_i)P_0(V_{n_i}(R_i))
\right\rangle_{r,1}.}
\tag{28}
\]
This is one common-temperature \(r\)-particle average. The determinant
is in the observable. Its particles are the spatial particles just
defined, not copies of an experiment performed at different temperatures.
They are also not the spinless fermions of (2).

Applying Green's identity yields the equivalent expression
\[
\boxed{
D_{r,k}=
\sum_{q=0}^r\binom rq b^{r-q}
\left(\frac{Z_{\rm conf}}8\right)^q
\left\langle
\prod_{i=0}^{q-1}J(R_i)\,
W_{r,k}^{(q)}(\tfrac12\log R_0,\ldots,\tfrac12\log R_{q-1})
\right\rangle_{q,1}.}
\tag{29}
\]
For \(q=0\), the average is \(W^{(0)}\).
For \(k\ge r\), (29) consists of the single \(q=r\) term.
For smaller \(k\), the lower-\(q\) averages describe the boundary
contributions left when some coordinates are evaluated at the sphere.
They do not imply a chemical potential or a grand-canonical equilibrium
state; (28) already gives the fixed-\(r\) representation.

The internal equilibrium state at a fixed spatial point also has either
the density-matrix or TFD presentation:
\[
\rho_{\rm int}(R)=A(R)^{-1}e^{-R^2h},\qquad
|\mathrm{TFD}(R)\rangle=
A(R)^{-1/2}\sum_{n\ge1}e^{-E_nR^2/2}|n\rangle_L|n\rangle_{\widetilde L}.
\tag{30}
\]
For example its expectation of \(P_0(R^2h)\) produces the insertion
in (27), after multiplication by \(A(R)\). In the spatial model
the \(R\)-dependence is an energy landscape at fixed bath temperature;
in (21) it is inverse temperature for a fixed Hamiltonian.

## 9. What an energy or quantum interpretation would still require

The Hamiltonian (23) is a natural family of harmonic potentials with
stiffnesses fixed by the box spectrum. Equations (28)–(29) are
equilibrium expectations of explicit observables. Those observables
are not the ordinary total energy \(\sum_iV_{n_i}(R_i)\).
Even the one-particle insertion is a quadratic polynomial in \(V\);
after Green transfer the observable contains derivatives of the
coefficient probe and its boundary traces.

Nor does the appearance of \(\Delta_3\) alone give a positive kinetic
energy. Already (6) pairs two different functions \(F\) and \(A\).
Its first integration by parts gives the mixed form
\[
\int\Phi f\,du
=-\frac14A'(1)F(1)
-\frac14\int_1^\infty R^2A'(R)F'(R)\,dR,
\tag{31}
\]
which is not a norm square. At determinant level, the transferred
operator is a product of radial insertions, together with boundary
terms, rather than an additive many-particle kinetic Hamiltonian.
For example \(\mathcal T_{2,1}\) changes sign as the radii separate.

A quantum spatial version can be written using genuine spatial fields:
\[
\widehat H_3=
\sum_{n\ge1}\int_\Omega
\widehat\Psi_n^\dagger(\mathbf R)
[-\kappa\nabla_{\mathbf R}^2+\pi n^2R^2]
\widehat\Psi_n(\mathbf R)\,d^3\mathbf R,\qquad\kappa>0,
\tag{32}
\]
\[
\{\widehat\Psi_n(\mathbf R),
\widehat\Psi_m^\dagger(\mathbf R')\}
=\delta_{nm}\delta^3(\mathbf R-\mathbf R').
\]
Specify a self-adjoint boundary condition, for example Dirichlet on
\(R=1\). The fields here live at spatial \(\mathbf R\), not at temperature
\(u\). For this model, the Gibbs diagonal is the heat kernel of
\(-\kappa\nabla_{\mathbf R}^2+V_n\), not \(e^{-V_n}\). Quantum exchange changes the
fixed-\(N\) position distribution as well. In particular the Dirichlet
kernel vanishes at the wall, whereas the configurational weight
\(e^{-V_n(1)}\) does not. Consequently (28) is not an exact quantum
fermion expectation for (32) as it stands.

This scopes the missing step: matching the actual \(N\)-particle quantum
thermal kernel and observable, or justifying a classical limit with
controlled corrections. It does not exclude other quantum constructions.
Using a TFD for (32) leaves that kernel-matching question unchanged.

## 10. Classification and control screen

This is the user-requested physical dictionary and determinant
bookkeeping, not a proposed sufficient positivity criterion. Read it with
the [result index][results], [theta identities][thetaresults],
[geometric realizations][geometry], and [avoid index][avoid], particularly
[target reformulations][a01], [geometric re-realizations][a03],
[normalizations][a08], and [scoped exclusions][a07].

The [collision controls][controls] supply an immediate analytical screen.
For a positive half-line source \(\xi\) with the required moments,
\[
p_\xi(u)=8\int_u^\infty\sinh(v-u)\xi(v)\,dv>0,\qquad
p_\xi''-p_\xi=8\xi,
\]
\[
b_\xi=-p_\xi'(0)/8=\int_0^\infty\cosh(v)\xi(v)\,dv.
\tag{33}
\]
The same even-probe determinant derivation gives (9)–(16) with
\(p_\xi,b_\xi\). A positive rescaling can set \(b_\xi=1/16\);
it does not remove a zero collision. Radial Note73 applies precisely
this screen to a colliding Gaussian-polynomial source.
Thus positive primitive, Green transfer, and the endpoint constant
together cannot establish the desired signs.

For the principal named families, the failed premise of the literal
model (23)–(24) is specific. Weighted-square controls alter the complete
unit weights, while retaining square energies and the generic radial
calculation; selected endpoint matching does not restore the full
normalized theta source. Euler-factor controls alter that source by
shifts and do not retain the unchanged unit-weight trace \(A(R)\).
Reflected super-Gaussian and smooth shape/positive-primitive controls
retain suitable symmetry or primitive properties but lack this canonical
square-spectrum partition density. Formula (33) still transfers their
derivatives, so the algebra itself does not separate these controls.
No new control numerics or sign range is claimed.

The exact fixed-temperature interpretation is therefore available.
The useful remaining research question is whether this explicit
observable, its boundary decomposition, or a justified quantum
completion supplies an estimate using the complete canonical theta
weights that is stronger than the original determinant formulation.

[radial73]: ../../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md
[checker]: ../numerics/radial_green_determinant_check.py
[record]: ../numerics/RADIAL_GREEN_DETERMINANT_CHECK_20261104.json
[results]: ../../../../../../../result-summaries/README.md
[thetaresults]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
