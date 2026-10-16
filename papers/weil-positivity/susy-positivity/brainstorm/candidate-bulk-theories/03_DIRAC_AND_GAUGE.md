# Two alternatives tested: Dirac saturation and gauge edge modes

12 September 2026. These are sufficiently specified models to compute and reject their simplest arithmetic identifications. They remain useful controls for the two leading channel constructions. The negative conclusions apply to the stated models, not to all supersymmetric or gauge theories.

## 1. A local supersymmetric half-space with a saturation equation

### Fields, energy, and symmetry

Use $x\in\mathbb R$, $y>0$, a positive mass $a$, and a complex two-component even field $u(x,y)$. Let

\[
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
M_a=-i\sigma_1\partial_x+a\sigma_3.
\]

This last notation means $M_a(u_1,u_2)=(a u_1-i\partial_xu_2,-i\partial_xu_1-a u_2)$. It is self-adjoint on $H^1(\mathbb R;\mathbb C^2)$, and $M_a^2=(-\partial_x^2+a^2)I_2$. The positive bulk energy is

\[
\mathcal E[u]=\int_{y>0}\left(|\partial_yu|^2+|\partial_xu|^2+a^2|u|^2\right)dxdy. \tag{1}
\]

The finite-energy domain is $H^1(\mathbb R\times\mathbb R_+;\mathbb C^2)$. Its trace belongs to $H^{1/2}(\mathbb R;\mathbb C^2)$, which contains all required smooth test traces but is smaller than the eventual logarithmic form domain.

On zero-trace fluctuations, the closed differential $A_0u=\partial_yu+M_a u$ has domain $H^1$ with lower trace zero. Its actual adjoint is the maximal weak operator $-\partial_y+M_a$; its domain is the set of $L^2$ spinors with that weak expression in $L^2$, without imposing an additional zero boundary trace. Do not replace this maximal domain by the same Dirichlet domain. Introduce an odd two-component partner $w$, and set

\[
\mathsf q(u,w)=(0,A_0u),\quad \mathsf q^*(u,w)=(A_0^*w,0).
\]

Then $\mathsf q^2=0$, $H=\{\mathsf q,\mathsf q^*\}=\operatorname{diag}(A_0^*A_0,A_0A_0^*)\ge0$. The physical component Hilbert space is the ordinary positive $L^2\oplus L^2$ space. There is no gauge or null quotient in the energy problem. These are explicitly defined linear SUSY partners, following the standard algebra in [Witten's equations (9)–(10)](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf); the matrix $M_a$ and boundary test are chosen here.

This algebra is an algebra of homogeneous fluctuations. A nonzero prescribed trace is an affine boundary condition, not automatically a supersymmetry-invariant state in that Hilbert domain. That distinction must survive any interpretation of a forced solution as BPS.

### Exact boundary calculation

For a prescribed spinor trace $F(x)=u(x,0)$, integration by parts gives

\[
\mathcal E[u]=\int_0^\infty\|\partial_yu+M_au\|^2dy+\langle F,M_aF\rangle. \tag{2}
\]

At Fourier frequency $\tau$, set $\rho(\tau)=\sqrt{a^2+\tau^2}$. The symbol $M_a(\tau)=\tau\sigma_1+a\sigma_3$ has eigenvalues $\pm\rho$ and orthogonal projections $P_\pm(\tau)=(I\pm M_a(\tau)/\rho)/2$. The saturating field is

\[
\widehat u(y,\tau)=e^{-y\rho}P_+\widehat F+e^{y\rho}P_-\widehat F. \tag{3}
\]

It has finite energy exactly when $P_-\widehat F=0$ almost everywhere and the remaining trace has finite $H^{1/2}$ energy. The *actual* unrestricted minimum for arbitrary $F$ is instead

\[
\widehat u_{\min}(y,\tau)=e^{-y\rho}\widehat F(\tau),\quad
\inf\mathcal E={1\over2\pi}\int\rho(\tau)|\widehat F(\tau)|^2d\tau. \tag{4}
\]

This uses the square root of the independently positive local massive Laplacian, not the unknown Weil operator. The distinction between (2) and (4) is the matrix half-line diagnostic from the brainstorm, here tested for a local tangential Dirac operator.

If one prescribes $F=(\widetilde f,0)$, then

\[
\|P_-(\tau)(\widehat f,0)\|^2
={1\over2}(1-a/\rho)|\widehat f(\tau)|^2. \tag{5}
\]

For a nonzero compactly supported smooth $f$, this is nonzero on a set of positive measure. Hence **no such nonzero input saturates** (2), even though its proposed boundary term is $a\|f\|^2>0$. Positivity of this particular boundary term is insufficient to supply the required solution. This is a stronger coverage failure than merely discovering a negative trial trace.

### A justified modification, and its limit

Allow the second spinor component to respond. Given any $f$, choose

\[
\widehat F(\tau)=\left(\widehat f(\tau),{\tau\over\rho+a}\widehat f(\tau)\right). \tag{6}
\]

This belongs to the positive spectral subspace and has finite energy for every smooth $f$. Its saturated pairing has multiplier

\[
\rho\left(1+{\tau^2\over(\rho+a)^2}\right)
={2\rho^2\over\rho+a}\sim2|\tau|. \tag{7}
\]

Thus the modification restores all-input coverage but gives order-one frequency growth, whereas the Weil form grows as $\log|\tau|$. Also (6) is a nonlocal boundary condition. If the second trace is merely left *free* in the minimization of (1), its minimizer is zero, not (6). The right boundary term in (2) depends on both components and is then not determined by $f$ alone. One must impose (6), or derive it from a different boundary action, before claiming a reduced-energy identity.

No finite number of constant positive weighted copies of (4) or (7), plus bounded normalization, pole, and finite-delay terms, changes their nonzero leading $|\tau|$ growth to a logarithm. This is a finite-family/order statement. Singular infinite-channel extensions can change the order: the explicit positive string in [01_RELATIVE_COMPLEX.md, §6](01_RELATIVE_COMPLEX.md#6-a-literal-extra-coordinate-and-a-gluing-calculation) is the viable modification used in this pass. It has a variational boundary equation rather than the failed unrestricted first-order saturation condition.

### Symmetry, smearing, and invariance actually available

Translation in $x$ and common phase rotation preserve (1). The fluctuation SUSY algebra is exact with the adjoints just stated. No invariance of the forced Hermitian pairing under changes of $a$, thickness, or boundary projection has been shown. If a different supersymmetry closes an insertion only up to $\partial_x R(x)$, smearing gives $-\int f'(x)R(x)dx$; compact support removes endpoint terms but not $f'$. Equations (5)–(7) are a concrete warning against claiming arbitrary-input symmetry from a homogeneous boundary calculation.

Gluing the positive energy (1) is legitimate when the full spinor trace and flux are retained at the interface and that trace is varied. Projecting independently onto the two half-spaces' decaying subspaces is a different problem. There is no proposed independent rule choosing the gamma spectrum, pole data, or arithmetic delays in this model.

## 2. Abelian Chern–Simons theory with surviving edge modes

### Geometry and boundary dynamics

Take $M=\mathbb R_t\times\mathbb R_x\times\mathbb R_{y\ge0}$, with an abelian gauge one-form $A$, integer level $k>0$, and

\[
S_{\rm CS}={k\over4\pi}\int_M A\wedge dA.
\]

Choose the boundary polarization $A_t-vA_x=0$, with $v>0$, and compatible boundary action/variational principle. Quotient gauge transformations $A\mapsto A+d\lambda$ that vanish at the boundary. In the topologically trivial sector, bulk flatness gives $A_i=\partial_i\phi$; its boundary value survives this relative gauge quotient. The edge action and Hamiltonian are

\[
S_\partial={k\over4\pi}\int dt dx\,[\partial_t\phi\,\partial_x\phi-v(\partial_x\phi)^2],
\quad H_\partial={kv\over4\pi}\int(\partial_x\phi)^2dx. \tag{8}
\]

These equations, including the role of the boundary velocity, are printed in [Tong, equations (6.7)–(6.11)](https://www.damtp.cam.ac.uk/user/tong/qhe/six.pdf). [Geiller–Jai-akson, equation (4.14) and its discussion](https://arxiv.org/pdf/1912.06025) explicitly separate the choice of boundary Hamiltonian from the extended symplectic structure. This separation is material: the bulk does not force the positive coefficient $v$, much less an arithmetic operator in its place.

The gauge transformations commute in this abelian model. If BRST notation is used, $\mathsf sA=dc$, $\mathsf sc=0$, $\mathsf s\bar c=b$, $\mathsf sb=0$; take the gauge ghost $c$ to vanish at the physical boundary. Then the surviving edge field is fixed by this relative gauge symmetry. Ghosts implement the quotient and are not the positive physical space. There is no additional physical SUSY supermultiplet in this candidate.

### Two choices for the role of $f$

As a prescribed classical edge profile, set $\phi(x,0)=f(x)$ for real $f$, then use two copies for the Hermitian complexification. The result is $H_\partial[f]=(kv/4\pi)\|f'\|^2$, with a $\tau^2$ multiplier. It cannot match the logarithmic target. If instead $f=\partial_x\phi$, the energy becomes a constant times $\|f\|^2$, again the wrong multiplier. On a circle in a fixed winding sector, this second interpretation also fixes $\int f$; a periodic single-valued scalar gives zero mean. On the line, allowing different limits of $\phi$ at the two ends repairs classical trace coverage, but changes the charge-sector question in quantization. Adding quantized winding sectors does not make arbitrary complex means a linear boundary profile in one fixed sector.

For a **linear insertion** interpretation, quantize the edge in its positive chiral boson Fock space. Normalize the current so its one-particle preparation is explicitly

\[
f\longmapsto j(f)\Omega:\quad
\tau\mapsto\sqrt{\tau}\,\widehat f(\tau),\qquad \tau>0,
\]

in $L^2(\mathbb R_+,d\tau/(2\pi))$. The current normalization is a fixed field rescaling; a different level convention supplies a positive overall constant. Its ordinary Hilbert adjoint gives

\[
\langle j(g)\Omega,j(f)\Omega\rangle
={1\over2\pi}\int_0^\infty\tau\,\overline{\widehat g(\tau)}\widehat f(\tau)d\tau. \tag{9}
\]

Every required smooth $f$ can be smeared this way, so *chirality of this insertion is not itself a failure to define the input map*. However, modulating a test far in one frequency direction makes (9) grow linearly, while modulating it far in the other direction makes it rapidly small. The target grows logarithmically in both directions. Two opposite chiralities give $|\tau|$, still not the target. The known chiral scalar logarithmic **position-space propagator** should not be confused with a logarithmic **Fourier multiplier**: differentiating it gives the current pairing (9), not the digamma kinetic term.

For (9), choose the neutral vacuum charge sector and its oscillator Fock space; the constant scalar mode is absent from the current observable. This does not require $\int f=0$, since $f$ smears a current insertion and is not being declared the derivative of a periodic classical scalar. Null bulk gauge directions have already been quotiented, and the resulting one-particle norm is the ordinary positive one displayed in (9).

### What is invariant and what could extend it

The full physical adjoint pairing in a fixed positive edge Fock representation is gauge invariant; changing a bulk flat representative with the same boundary mode does not change it. Bulk metric deformations fixing the edge data do not alter the classical reduction (8). But replacing the boundary Hamiltonian, changing the charge sector, or changing the polarization is not one of those operations. No claim about a regulated quantum metric Ward identity is needed for the obstruction in (9).

Gluing requires matching the edge phase space, including the boundary current and global charge. Keeping only bulk gauge equivalence classes that are trivial at the cut would discard the mode producing (8). A topological bulk can therefore retain exactly the kind of infinite boundary space needed by the program; it does not determine its desired norm. One may couple its edge to the positive string/relative complex of the first candidate. That would provide a gauge interpretation of the already computed gamma energy, with all its arithmetic choices and missing terms still to be supplied. Choosing a nonlocal boundary Hamiltonian equal to the Weil kernel is excluded as circular.

## 3. Ranking after these tests

The Dirac candidate has a calculable positive bulk and exact SUSY algebra, but its simplest saturation proposal has almost no allowed traces; the repaired model has the wrong frequency order. The Chern–Simons candidate supplies robust surviving edge modes and a positive quantization, but its concrete energy and insertion norms have the wrong frequency order and its boundary Hamiltonian is not selected by the bulk. Neither is developed further in this pass. The relative channel complex is stronger for a complete nonlocal toy boundary pairing; the loop model is stronger for explicit arithmetic coefficients and finite-interval composition.
