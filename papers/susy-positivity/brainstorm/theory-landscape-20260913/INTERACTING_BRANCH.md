# Interacting positive theories: what actually escapes the current obstruction

This note distinguishes literature facts, elementary deductions made here, and proposals. It does not claim a realization of the full Weil form or a proof of RH. The companion [extension tests](EXTENDED_SUSY_TEST.md) derive further restrictions on promoting the arithmetic benchmark to four supercharges.

## Assessment

The best reason to move beyond the Gaussian models is not that nonlinear systems are inherently capable of complicated functions while Gaussian systems are not. It is that the current ansatz fixes the response to a positive resolvent class and its Ward identity fixes the wrong ground-state pairing. An interaction is useful only if it changes those restrictions while leaving an independently specified positive Hilbert theory.

Among the mechanisms examined in this branch, the most promising is an interacting theory with **four-supercharge control of the ground-state geometry plus an explicit arithmetic defect algebra**. Chiral couplings lead to tt* equations; real mass/vector couplings lead instead to Bogomolny-type equations. These are different possibilities, not interchangeable names for the same protection. Ordinary interacting SUSY quantum mechanics with an arbitrary fitted potential ranks lower: it supplies positivity easily but offers no structural reason for the desired arithmetic pairing. Integrable boundary models are valuable construction laboratories, but their scattering amplitudes and thermodynamic free energies are not already the required norms.

Any candidate still needs an infinite-dimensional observable space, the prime-delay singularities, the gamma contact and regular kernel, and the two pole amplitudes. Neither a finite set of vacua nor the appearance of a gamma function is an adequate match.

## 1. Two general deductions that constrain the survey

### 1.1 Interactions do not automatically evade a positive spectral-moment obstruction

Let H be a nonnegative self-adjoint Hamiltonian, let Omega be a vacuum, and let v=O Omega be a vector orthogonal to the vacuum. Its Euclidean autocorrelation is

\[
C(t)=\langle v,e^{-tH}v\rangle=\int_{[0,\infty)}e^{-tE}\,d\nu_v(E),\qquad t>0,
\]

where dnu is a positive measure. No Gaussian assumption is used. When the two-sided time correlation and Fourier transform are defined, its nonzero-energy part gives

\[
\widehat C(\omega)=\int_{(0,\infty)}\frac{2E}{\omega^2+E^2}\,d\nu_v(E).
\]

Thus a derivative or subtracted response that remains of the form

\[
T(s)=s\int_{[0,\infty)}\frac{d\mu(t)}{s+t}
\]

still has positive Stieltjes moment matrices, whether the underlying fields are free, interacting, elementary, or composite. If the relevant finite moments exist, then

\[
\sum_{i,j}\overline c_i c_j m_{i+j+1}
=\int t\left|\sum_i c_it^i\right|^2d\mu(t)\ge0.
\]

Consequently an interacting replacement that retains the exact moment assumptions of the finite-block audit meets the same obstruction. Allowing a continuum of masses does not help: the audit already admits positive spectral measures.

The literature analogue is the positive spectral representation derived from reflection positivity and translation invariance. Usui establishes a precise lattice version under Hermiticity, translation invariance, reflection positivity, and polynomial bounds: [A Note on Reflection Positivity and the Umezawa–Kamefuchi–Källén–Lehmann Representation](https://arxiv.org/abs/1201.3415). The elementary Hilbert-space calculation above is our reason for applying that principle here; the lattice paper is not being invoked as a theorem about the present continuum model.

**Scope.** The relevant Euclidean frequency in this argument is the frequency conjugate to the physical evolution parameter. The arithmetic variable x and its Fourier variable tau need not be physical time and energy. Equal-physical-time covariance as a function of spatial tau squared need not have this Stieltjes form. In the existing Gaussian construction the dispersion is already nonrelativistic, h=tau squared+a squared. Keeping reflection positivity in physical time while changing the arithmetic-space observable or kinematics is a legitimate escape. Higher spectral moments may also fail to exist in a field theory; this removes a particular moment proof, not the obligation to match the entire response.

### 1.2 The prime atoms rule out the most naive local Euclidean interpretation

On an interval whose length exceeds log 2, the Weil kernel has a nonzero delta contribution at a nonzero separation, and more appear at prime-power logarithms:

\[
-\sum_{p,m}(\log p)p^{-m/2}
\bigl[\delta(x-y-m\log p)+\delta(x-y+m\log p)\bigr].
\]

The gamma kernel is smooth away from coincident points and the pole kernel is smooth, so they cannot cancel these isolated off-diagonal delta distributions.

For a fixed vector v and H bounded below, C(t)=<v,e^{-tH}v> is analytic for Re t>0. The same conclusion holds for a distributional observable after positive-time preparation, whenever its spectral measure has the usual polynomial growth. Indeed each derivative inserts E to a finite power, which is controlled on Re t at least epsilon by exponential damping. Such a local Euclidean time correlator cannot have a delta singularity at t=log p. A conventional homogeneous local Euclidean field theory whose two-point function is regular away from coincidence likewise cannot match these prime atoms by changing its local interaction potential alone.

**This is a selection rule, not a general quantum-field-theory impossibility theorem.** It does not apply unchanged to Minkowski time, null propagation, spatially nonlocal observables, quotient images, networks with identified endpoints, or a field theory with explicit defect return paths. Nor does it say that the arithmetic x must be Euclidean time. It instead says that the model must specify what produces discrete returns. A topology/defect construction or multiplicative geometry is substantive data, not decoration appended after choosing an arbitrary interacting local model.

## 2. What positivity should measure

For an operator-valued distribution O(x), a linear smearing O(f)=integral f(x)O(x)dx gives

\[
Q_{\rm model}[f]=\|O(f)\Omega\|^2
=\iint\overline{f(x)}f(y)\langle O(x)^\dagger O(y)\rangle\,dx\,dy.
\]

The form is exactly quadratic in f even when O is nonlinear in the fields and the Hamiltonian is interacting. Centering O produces a connected two-point function and preserves covariance positivity. Taking a logarithm of an amplitude, taking an arbitrary parameter derivative, or extracting a coefficient of a signed generating function does not automatically preserve positivity.

This is preferable to expecting a nonlinear source Hamiltonian to have an exactly quadratic ground energy. At a finite regulator, if H(j)=H0-jO has a nondegenerate gapped ground state, perturbation theory gives

\[
E_0''(0)=-2\sum_{n>0}\frac{|\langle n|O|0\rangle|^2}{E_n-E_0}\le0.
\]

More generally E0(j), as an infimum of affine functions of j, is concave. A compensating source-square contact can alter that sign, but must itself be derived. If an entire source-dependent Hamiltonian is a supercharge square with unbroken SUSY, its ground energy remains zero; the useful information is then in state overlaps or observables, not in a nonzero family of vacuum energies.

A further distinction matters. If every prepared O(f)Omega is projected to a fixed r-dimensional ground space, its Gram form has rank at most r. It cannot reproduce the unbounded logarithmic kinetic operator on an infinite-dimensional interval space. A finite-dimensional tt* metric must therefore be combined with a genuine field/continuum of boundary data, an infinite periodic cover, or an operator algebra generating an infinite state space. Merely allowing a continuum of parameter values in a finite vacuum bundle does not solve this: comparing states in different fibers requires a specified common Hilbert embedding. Unitary parallel transport into one finite fiber still gives finite rank.

## 3. Nonlinear sigma and gauged quantum mechanics with four supercharges

**Literature fact.** Sonner and Tong derive supersymmetric constraints on non-Abelian Berry connections. With chiral-multiplet parameters, the connection and projected superpotential operators satisfy tt* equations. With vector-multiplet parameters, the Berry connection A and the projected moment-map operator Phi satisfy

\[
F_{ij}=\epsilon_{ijk}D_k\Phi.
\]

Their nonlinear sigma-model example has a Kähler target, a holomorphic Killing vector, and a mass-induced potential. Phi is the matrix of ground-state expectation values of the moment map. The CP1 example has a smooth BPS-monopole Berry connection, demonstrating nonperturbative ground-state geometry in an explicitly non-Gaussian theory. Sources: [Berry Phase and Supersymmetry](https://arxiv.org/abs/0810.1280), [Non-Abelian Berry Phases and BPS Monopoles](https://arxiv.org/abs/0809.3783).

**Proposal.** Use an N=4 quantum-mechanical defect with these constraints at the boundary of a bulk carrying the arithmetic coordinate. Couple primitive return operators to background chiral parameters if a tt* mechanism is wanted, or to vector multiplets if log p is interpreted as a real mass. The choice must be made from the physical meaning of the arithmetic coupling. Then derive which projected operators and which Hermitian metric enter the norm before choosing parameters to fit the target.

**Why it may help.** These equations constrain changes of ground-state geometry rather than freezing a fixed differential and source map. A nonlinear sigma metric, gauge constraint, or superpotential can alter the embedding and interference among channels. It is therefore outside the already excluded fixed-complex Ward deformation.

**Why this is not yet a leading standalone RH model.** CP1 has only two vacua; compact targets generally give finite ground-state spaces. There is no prime-delay mechanism in the ordinary model. Choosing a complicated target metric solely so that its vacuum metric equals the Weil form would hide the question in the target geometry. Noncompact targets may offer continuum labels, but normalizability, continuous spectrum, and boundary conditions become essential and can invalidate index-based counting arguments.

For gauged QM, exact localization formulas most readily compute refined indices, such as Cordova and Shao's residue formula for four-supercharge gauged QM: [An Index Formula for Supersymmetric Quantum Mechanics](https://arxiv.org/abs/1406.7853). That result concerns signed BPS counting, not the ordinary Hermitian overlap matrix required here. An index or wall-crossing formula should not be substituted for the target norm.

**Useful first investigation.** Classify the proposed arithmetic parameters as chiral/vector/geometric data; derive the resulting ground-state equations and ascertain whether the boundary field retains an infinite observable space. CP1 is an excellent exact control for conventions and what these equations actually protect, not a candidate to fit RH by itself.

## 4. A concrete nonlinear SUSY control: the Morse ground state

Here is an elementary calculation, included to prevent gamma-function appearances from being overvalued. On y in R, let a>0 and

\[
A_a=\partial_y+\frac{e^y-a}{2},\qquad
H_-=A_a^\dagger A_a
=-\partial_y^2+\frac{(e^y-a)^2}{4}-\frac{e^y}{2}.
\]

Together with H+=Aa Aa dagger this is positive SUSY quantum mechanics. The dynamics are nonlinear. Its normalized ground state is

\[
\psi_a(y)=\Gamma(a)^{-1/2}
\exp\!\left[\frac{ay-e^y}{2}\right],
\]

because the substitution u=e^y gives integral exp(ay-e^y)dy=Gamma(a). A unitary multiplication observable therefore has exact expectation

\[
C_a(\tau)=\langle\psi_a,e^{i\tau y/2}\psi_a\rangle
=\frac{\Gamma(a+i\tau/2)}{\Gamma(a)}.
\]

The kinetic function in the present program obeys

\[
B(\tau^2)
=\left.\partial_a\log|C_a(\tau)|\right|_{a=1/4}.
\]

This is not the assertion that B is the Morse two-point covariance. It is a logarithmic derivative of a known amplitude. Its positivity still needs the gamma partial-fraction identity or an additional physical interpretation. The unitary expectation is bounded, whereas B grows logarithmically. For varying real a, the Fubini–Study/Bures metric is one quarter of the trigamma function; the standard pure-state quantum Fisher information is the trigamma function itself. Neither is B at arbitrary tau.

The standard nonlinear supercharge mechanism is rooted in [Witten's supersymmetry and Morse theory](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf). A directly related primary-source exploration, [McGuigan's modified Morse potentials](https://arxiv.org/abs/2002.12825), constructs ground-state Fourier amplitudes involving gamma, eta, and xi functions. Its stated RH reformulation concerns zeros of those Fourier amplitudes; positivity of its Hamiltonian does not prove the required zero locations. This is a useful warning against mistaking an explicit positive Hamiltonian containing zeta for a positive realization of the Weil form.

**Selection implication.** A periodic Landau–Ginzburg amplitude involving gamma deserves serious attention, but the initial test is whether it is the physical Hermitian metric, an amplitude, a logarithmic derivative, or a limit of one of these. The Morse calculation separates those possibilities explicitly.

## 5. Interacting boundary/defect theories

**Literature fact.** Adding boundary degrees of freedom can enlarge the admissible supersymmetric interactions. Nepomechie's boundary supersymmetric sine-Gordon theory includes a Hermitian boundary fermion a and terms schematically of the form

\[
L_b=\bar\psi\psi+ia\partial_ta
-2f(\phi)a(\psi-\bar\psi)+B(\phi),
\]

with the functions tied by supersymmetry and integrability. It has a two-parameter family of permitted boundary interactions: [The boundary supersymmetric sine-Gordon model revisited](https://arxiv.org/abs/hep-th/0103029). The detailed reality conventions and preserved supercharges matter; this is a construction precedent, not an action already matched to the present problem.

**Proposal.** Keep an explicitly positive bulk and add interacting SUSY defects that connect arithmetic positions differing by log p. Measure a single combined boundary observable. If its state map changes from Gamma to Gamma+Lambda, then

\[
(\Gamma+\Lambda)^\dagger(\Gamma+\Lambda)
=\Gamma^\dagger\Gamma+
\Gamma^\dagger\Lambda+\Lambda^\dagger\Gamma+
\Lambda^\dagger\Lambda.
\]

The cross term can carry either sign while the whole norm stays positive. This is a physical way to obtain signed relative corrections, unlike adding independent orthogonal positive channels. Nonlinear composite observables on a Gaussian bulk can already exploit this; actual interactions alter the state and its correlations further. Thus “non-Gaussian action” and “nonlinear observable” should be separate axes of the survey.

**Requirements specific to primes.** Primitive sectors must generate repetitions with weights (log p)p^(-m/2). Generic interacting defects also generate mixed-prime connected histories. The desired logarithmic-derivative arithmetic has primitive powers rather than arbitrary composite return words, so a charge-selection, factorization, or connected-sector identity must explain which histories survive. Simply making the action more complicated can worsen this mismatch.

A single periodic field does not accept arbitrary frequencies log p: single-valued exponentials on an imaginary period require integral charges. Ratios log p/log q are irrational for distinct primes. A proposed periodic superpotential containing exp((log p)Y) therefore needs separate fields, a noncompact covering variable, or a different global definition. This elementary global check should precede perturbation theory.

**Poles.** The pole form decomposes as a positive and a negative rank-one contribution. It cannot be represented by appending an independent state with negative squared norm. A coupled constraint or interference term may produce a negative relative piece while retaining a positive total norm. A finite-rank pole mechanism would be useful, but cannot repair the already proved infinite-rank residual of a fixed old ansatz.

## 6. A fully explicit positive interacting framework, with a limitation

At a finite spatial regulator, choose a real confining function U(phi) of all bosonic coordinates and define

\[
Q=\sum_j\psi_j^\dagger\left(\partial_{\phi_j}
+\partial_{\phi_j}U\right),\qquad H=\{Q,Q^\dagger\}\ge0.
\]

Since U is a scalar function, the derivative operators commute and Q squared is zero. The bosonic zero state is proportional to exp(-U). Nonlinear U yields an interacting positive theory, and every observable has ordinary positive Gram covariance in that state. A field-theory proposal could take U to contain local gradient and quartic terms together with explicitly specified nonlinear interactions joining x and x+log p.

This construction gives a safe arena for testing new arithmetic observables. It escapes the finite constant-mass resolvent ansatz, and can retain positivity in physical evolution time even when the arithmetic-space interactions are nonlocal. Its equal-time bosonic measure is precisely an interacting classical Gibbs measure exp(-2U), so it is not a quantum-exclusive positivity mechanism. The difficulty is still to derive its correlation kernel from the prescribed arithmetic data, and ordinary two-supercharge SUSY supplies no sufficiently strong equation for that kernel.

For comparison, a weighted graph incidence supercharge gives negative off-diagonal terms -w_p(T_p+T_p dagger) inside a positive Laplacian, together with forced positive diagonal weights. This can explain signed prime-like terms structurally, but the required large diagonal compensation, gamma contact, and pole sector remain unsolved. Removing or fitting the forced diagonal by hand is not a completion. Nonlinear Witten Laplacians similarly contain negative Hessian terms inside a positive supercharge square; they offer a mechanism, not an arithmetic identity.

## 7. Integrability: useful control, not an automatic positivity bridge

Interacting supersymmetric sinh-Gordon and related theories admit exact scattering and form-factor analyses; see [Ahn, Thermodynamics and Form Factors of Supersymmetric Integrable Field Theories](https://arxiv.org/abs/hep-th/9306146). Boundary finite-size models have also been derived from spin-chain regularizations: [Ahn, Nepomechie, and Suzuki](https://arxiv.org/abs/hep-th/0611136).

A two-point function of a Hermitian observable has a spectral expansion with squared form factors, hence positive weights, schematically

\[
C(r)=\sum_{n\ge0}\frac1{n!}
\int\prod_{j=1}^n\frac{d\theta_j}{2\pi}
|F_n(\theta_1,\ldots,\theta_n)|^2
e^{-r\sum_jm_j\cosh\theta_j}.
\]

This positivity is useful. However, a homogeneous local Euclidean correlator of this form again cannot produce prime atoms at nonzero Euclidean separation. A boundary scattering matrix, phase shift, TBA free energy, or log determinant is not this positive norm. Interpreting a prime logarithmic derivative as a scattering phase does not establish the desired covariance positivity. An integrable defect network with arithmetic return geometry may deserve attention; a generic integrable bulk chosen because its S matrix contains gamma functions is too weak a criterion.

## 8. Ranking and the next analytic tests

| Architecture | Concrete advantage | Present missing step | Priority |
|---|---|---|---|
| Four-supercharge interacting ground-state geometry with arithmetic defects | Equations govern the Hermitian geometry; defects can supply discrete returns | Specify infinite observable space, arithmetic coupling type, and full norm identity | Highest among this branch; naturally combines with periodic tt* survey |
| Interacting/nonlinear boundary observable on controlled positive bulk | Signed corrections arise through interference; observable can be infinite rank | Derive observable and selection rules from an action, including contact and poles | High as a construction experiment |
| Nonlinear sigma/gauged QM with vector parameters | Bogomolny constraints and exact CP1 control | No arithmetic return geometry; finite vacuum rank | Medium, especially if log p is a mass parameter |
| Detailed-balance SUSY field with nonlinear arithmetic-space interactions | Positive regulated Hamiltonian is explicit; non-Gaussian covariance | No protected arithmetic kernel; continuum and all-prime limits | Medium-low until a governing identity is identified |
| Integrable SUSY boundary field theory | Exact interactions, scattering, form factors, finite-size checks | Norm versus phase/free-energy mismatch and missing prime geometry | Supporting laboratory |
| Arbitrary fitted Morse/quiver potential or spectral measure | Can contain gamma or zeta explicitly | Positivity carries no identified implication for the Weil target | Low as a proof strategy |

Before narrowing to a particular potential, demand answers to five structural questions:

1. Which ordinary positive Hilbert norm is proposed, and why is its f dependence exactly the required sesquilinear one?
2. Where do nonzero-separation prime atoms originate, and how are mixed histories controlled?
3. What changes the physical Hermitian pairing beyond the old fixed-complex Ward family? Which supersymmetric equation constrains that change?
4. How does the candidate avoid finite-rank input loss, the scoped positive-moment obstruction, and undefined infinite-tower source vectors?
5. What identity would determine the complete gamma/contact/pole/prime kernel without inserting the unknown target metric or assuming RH?

The most valuable next deliverable is an explicit map of those five items for one periodic/chiral theory and one vector-multiplet or nonlinear-defect alternative. A simple inconsistency in their global charge structure or observable type is already informative. Numerical exploration is best deferred until an independently specified complete pairing exists to test.

## 9. Exact finite-prime positive SUSY control combining Morse and geometric states

This construction was proposed in coordination with the main survey and independently checked here. It is an original control calculation for this report, not a literature claim or an RH result.

Fix a finite prime set S and a real sigma>0. Write

\[
a=\frac\sigma2,\qquad r_p=p^{-\sigma/2},\qquad
\Lambda_S(s)=\pi^{-s/2}\Gamma(s/2)
\prod_{p\in S}(1-p^{-s})^{-1}.
\]

Use the bosonic Hilbert space

\[
\mathscr H_S=L^2(\mathbb R,dy)\otimes
\bigotimes_{p\in S}\ell^2(\mathbb N_0).
\]

The continuous factor uses the closed Morse operator Aa from Section 4. More precisely, take the closure of its natural first-order operator, or its maximal distributional domain consisting of L2 functions with Aa psi in L2. Its nonnegative Hamiltonian is defined by the closed form ||Aa psi|| squared. The explicit ground state lies in this domain: its first-order expression vanishes and it is square integrable for every a>0. The adjoint zero solution grows like exp(e^y/2), so it is not square integrable.

On each discrete factor let T be the backward unilateral shift,

\[
(T\xi)_n=\xi_{n+1},\qquad D_p=T-r_pI.
\]

Dp is bounded, Dp dagger Dp is positive, and its kernel is the one-dimensional space spanned by (r_p to the n). Its norm squared is (1-r_p squared) inverse. The adjoint has no nonzero kernel: its n=0 component forces xi0=0 and the remaining recurrence forces every component to vanish. Each factor has its standard two-term SUSY doubling. The finite graded tensor product has

\[
Q=\sum_j(-1)^{F_{<j}}Q_j,\qquad Q^2=0,
\qquad H=\{Q,Q^\dagger\}=\sum_jH_j\ge0.
\]

The signs in the graded tensor product are essential for nilpotence; an ungraded sum of supercharges would not be the same construction. The bosonic product ground vector can be taken as

\[
\Psi_\sigma(y,\mathbf n)
=\pi^{-\sigma/4}
\exp\!\left[\frac{ay-e^y}{2}\right]
\prod_{p\in S}p^{-\sigma n_p/2}.
\]

All factors are normalizable since S is finite and sigma>0. Its raw squared norm is

\[
\|\Psi_\sigma\|^2=\Lambda_S(\sigma).
\]

Define the real multiplication operator

\[
X=\frac y2-\sum_{p\in S}n_p\log p-\frac{\log\pi}{2}.
\]

This is self-adjoint on its natural domain, and exp(i tau X) is unitary for real tau. Direct integration and absolutely convergent geometric sums give

\[
\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle
=\Lambda_S(\sigma+i\tau).
\]

No zeros of zeta, target-square-root operation, or numerical fitting enters this finite-prime identity. The dynamics include a nonlinear Morse sector; the prime sectors are positive discrete difference complexes. They are independent sectors, not a new interacting arithmetic theory.

With normalized ground vector Omega=Psi/sqrt(Lambda_S(sigma)), the characteristic function is

\[
\chi_{\sigma,S}(\tau)
=\frac{\Lambda_S(\sigma+i\tau)}{\Lambda_S(\sigma)}.
\]

On two copies of the normalized ground state, the observable exp(i tau(X tensor I-I tensor X)) has expectation

\[
\Phi_{\sigma,S}(\tau)=|\chi_{\sigma,S}(\tau)|^2.
\]

This is positive definite as a function of tau: it is the characteristic function of a real random variable, or equivalently a unitary matrix coefficient. It is not yet the Weil quadratic form. In particular, a logarithmic derivative of a positive-definite kernel is not in general a positive-definite kernel or a protected Hilbert norm.

For the raw scalar metric w=|Lambda_S(sigma+i tau)| squared, differentiation yields

\[
\partial_\sigma\log w_{\sigma,S}(\tau)
=-\log\pi+\operatorname{Re}\psi\!\left(
\frac{\sigma+i\tau}{2}\right)
-2\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}
\cos(m\tau\log p).
\]

At sigma=1/2 this is exactly the pole-free whole-line arithmetic multiplier with finite prime set S. This identity is an important benchmark: a manifestly positive SUSY theory can generate the relevant local factors and their logarithmic derivative, without that derivative being a positive covariance.

**Framing obstruction.** The equation Q Psi=0 only fixes the ground vector up to an overall scalar depending on sigma. If Psi is replaced by c(sigma)Psi, the raw w changes by |c| to the fourth power and its logarithmic derivative shifts by 4 Re(c prime/c), a scalar identity term. In particular the inserted pi prefactor is a chosen normalization of the raw state; it is not selected by the positive Hamiltonian. The Hamiltonian and its normalized vacuum therefore do not fix the very contact term that becomes problematic in the arithmetic form. A future theory needs physically specified boundary states/framing or another principle determining this normalization, as well as the poles.

**Infinite-prime limitation.** In the finite-occupation representation, the all-prime product vector has squared norm proportional to zeta(sigma), which is finite only for sigma>1. At sigma=1/2 it is not a vector. An abstract infinite product of normalized local states can still be defined on a suitable local observable algebra, but that does not automatically define the unbounded sum X or its global unitary exponential. Indeed independent geometric occupations have sum of probabilities P(n_p>0)=sum p to the minus sigma; it diverges at sigma=1/2, and almost surely infinitely many primes are occupied. The displayed finite-sum X then diverges. An alternative representation or renormalization is new work, and analytic continuation is not a substitute for the existence of these positive Hilbert objects.

## 10. Normalization gives an exact positive jump energy, and exposes the contact gap

The normalized metric from the preceding section satisfies

\[
\partial_\sigma\log\Phi_{\sigma,S}(\tau)
=B_\sigma(\tau^2)
+2\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}
\bigl[1-\cos(m\tau\log p)\bigr],
\]

where

\[
B_\sigma(\tau^2)
=\operatorname{Re}\psi\!\left(\frac{\sigma+i\tau}{2}\right)
-\psi(\sigma/2).
\]

Every term is a positive Dirichlet symbol. For the gamma piece, the partial fractions give a direct jump representation:

\[
B_\sigma(\tau^2)
=\int_{\mathbb R}\bigl[1-\cos(\tau x)\bigr]
\frac{e^{-\sigma|x|}}{1-e^{-2|x|}}\,dx.
\]

At sigma=1/2 this is the gamma kinetic B of the program. Near zero the density is asymptotic to 1/(2|x|); its product with min(1,x squared) is integrable, and it decays exponentially at infinity. Thus it is a valid symmetric Levy measure. The prime part adds the positive atomic measure

\[
\nu_{\sigma,S}^{\rm prime}
=\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}
\bigl[\delta_{m\log p}+\delta_{-m\log p}\bigr].
\]

For finite S its total mass is finite. Consequently the entire normalized derivative is the Fourier symbol of a symmetric positive jump energy. Explicitly, for F on the real line,

\[
\mathcal E_{\sigma,S}[F]
=\frac12\int_{\mathbb R}\nu_{\sigma,S}(dh)
\int_{\mathbb R}|F(x+h)-F(x)|^2\,dx\ge0.
\]

This also has a literal positive incidence factorization and hence a SUSY doubling. It is an exact structural positivity result, not a numerical bound. In probabilistic terms its negative is a Markov generator and exp(-t times the symbol) is positive definite. This interpretation follows directly from the displayed positive jump measure; no stochastic assumption about primes is introduced.

**What is missing.** Restoring the raw metric replaces the normalized symbol by

\[
\partial_\sigma\log w_{\sigma,S}
=\partial_\sigma\log\Phi_{\sigma,S}+c_{\sigma,S},
\]

\[
c_{\sigma,S}=\psi(\sigma/2)-\log\pi
-2\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}.
\]

The positive graph/jump structure forces the diagonal companion weights; the raw normalization subtracts them again and introduces the negative arithmetic contact. The finite-rank pole kernel is still absent. This pinpoints why an elementary positive jump or probabilistic interpretation of the normalized expression does not complete the program.

There is a second exact limitation at the all-prime boundary. The prime measure has infinite mass outside every fixed compact set at sigma=1/2, so it is not a Levy measure on the real line. More directly, if F is supported in an interval of length L, then a jump h>L gives

\[
\int|F(x+h)-F(x)|^2dx=2\|F\|^2.
\]

The independent positive prime-jump energy therefore diverges for every nonzero such F as S grows through all primes: the contribution of p>exp L already contains the divergent sum of (log p)p to the minus one half. The complete finite-interval Weil expression remains finite because its off-diagonal prime translations vanish beyond the support and the matching diagonal subtraction is already present. Passing from the positive jump energy to that renormalized form is exactly the difficult step; positivity is not preserved merely because both are related by a formally explicit subtraction.

This finite-prime control is worth keeping alongside the periodic tt* candidates. It demonstrates how much gamma and Euler structure is already obtainable from elementary positive dynamics, and isolates what the more powerful theory must additionally explain: the physical boundary normalization, poles, and a positive treatment of the infinite-prime limit.
