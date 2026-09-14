# Two compatibility tests for extending the finite-prime SUSY benchmark

These are exact, scoped deductions for the proposed theory comparison. They do not exclude all four-supercharge theories, interacting arithmetic completions, or periodic tt* systems. They exclude two particularly direct attempts to add extended supersymmetry while retaining specified data of the elementary benchmark. No numerical positivity bounds are used.

## 1. The positive benchmark and three different objects

For a finite prime set S and Re z>0, define

\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)
\prod_{p\in S}(1-p^{-z})^{-1}.
\]

On the bosonic Hilbert space

\[
\mathscr H_S=L^2(\mathbb R,dy)\otimes
\bigotimes_{p\in S}\ell^2(\mathbb N_0),
\]

put

\[
X=\frac y2-\sum_{p\in S}n_p\log p-\frac{\log\pi}{2},
\qquad
\Psi_z(y,\mathbf n)=e^{zX/2}e^{-e^y/2}.
\]

This is a holomorphic Hilbert-space-valued function on Re z>0. Local square-integrable domination follows by restricting Re z to a compact subinterval of (0,infinity); derivatives insert powers of X, which remain integrable there.

For real sigma>0 it is the product zero state of the Morse operator

\[
A_a=\partial_y+\frac{e^y-a}{2},\qquad a=\sigma/2,
\]

and discrete operators

\[
D_p=T-p^{-\sigma/2}I,\qquad (T\xi)_n=\xi_{n+1}.
\]

Their standard two-term SUSY complexes, combined with a graded tensor product, have Q squared zero and H={Q,Q dagger} nonnegative. The continuous Hamiltonians use the closed forms of Aa and its adjoint; Dp is bounded. Every factor has a unique bosonic zero state and no fermionic zero state. At finite S their tensor product therefore has one zero state.

The Hamiltonians just specified have a real parameter sigma. To make the chosen holomorphic extension an explicit physical family, set z=sigma+i eta and define on the full graded Hilbert space

\[
H_{\sigma,\eta}=e^{i\eta X/2}H_\sigma e^{-i\eta X/2},
\]

with the same unitary conjugation for its supercharges and domains, acting trivially on fermion labels. Its ground state is the displayed Psi_z. This is one definite partner-parameter prescription. The curvature test below does not assert that every extension retaining the real-sigma ground states must choose this prescription.

Three objects must be kept distinct:

\[
\begin{array}{ll}
\text{Physical norm of the holomorphic ground section:}
&g(z,\bar z)=\langle\Psi_z,\Psi_z\rangle
=\Lambda_S(\Re z),\\[2mm]
\text{Transition amplitude at fixed real sigma:}
&\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle
=\Lambda_S(\sigma+i\tau),\\[2mm]
\text{Squared transition amplitude:}
&w(\sigma,\tau)=|\Lambda_S(\sigma+i\tau)|^2.
\end{array}
\]

The distinction is also visible from the complete overlap kernel:

\[
\langle\Psi_z,\Psi_w\rangle
=\Lambda_S\!\left(\frac{\bar z+w}{2}\right).
\]

In particular, w is not the physical metric of this holomorphic vacuum line. If w is declared to be a different holomorphic-line metric, it is flat because LambdaS is holomorphic and nonzero on this half-plane. That separate declaration does not describe the Berry geometry of the displayed ground states.

## 2. The physical ground line has strictly nonzero curvature

With normalized vacuum Omega_sigma=Psi_sigma/sqrt(LambdaS(sigma)), the probability density is proportional to exp(sigma X)exp(-exp y). Differentiating its normalization gives

\[
\partial_\sigma\log\Lambda_S(\sigma)=\langle X\rangle_\sigma,
\qquad
\partial_\sigma^2\log\Lambda_S(\sigma)
=\operatorname{Var}_\sigma(X).
\]

The explicit variance is

\[
V_S(\sigma)
=\frac14\psi_1(\sigma/2)
+\sum_{p\in S}
\frac{(\log p)^2p^{-\sigma}}{(1-p^{-\sigma})^2}>0.
\]

Here psi1 is the trigamma function. Positivity is exact: its positive-argument partial fractions are a sum of positive reciprocal squares, and each prime term is nonnegative. All terms are finite for fixed S and sigma>0.

Writing z=sigma+i eta, the Chern curvature coefficient of the physical metric is consequently

\[
\partial_z\partial_{\bar z}\log g
=\frac14V_S(\sigma)>0.
\]

The overall sign of the curvature two-form depends on the connection convention; its nonvanishing does not. For example, the normalized state is

\[
\Omega_{\sigma,\eta}=e^{i\eta X/2}\Omega_\sigma.
\]

With the convention A=i<Omega,dOmega>, one obtains

\[
A_\sigma=0,\qquad A_\eta=-\frac12\langle X\rangle_\sigma,
\qquad F_{\sigma\eta}=-\frac12V_S(\sigma).
\]

This directly checks that the curvature is a property of the physical projector, not an artifact of the normalization of the holomorphic section. A nonzero holomorphic rescaling changes log g by a harmonic function and cannot remove it.

In ordinary massive four-supercharge quantum mechanics, chiral-multiplet parameter variations satisfy a tt* curvature equation of the form

\[
F_{i\bar j}\ \propto\ [C_i,C_j^\dagger],
\]

with the adjoint determined by the physical ground-state metric. For one vacuum all C matrices are scalars, so the right-hand side vanishes. This is the chiral-parameter constraint derived by [Sonner and Tong, Berry Phase and Supersymmetry](https://arxiv.org/abs/0810.1280); the same paper explains why vector-multiplet parameters satisfy different, Bogomolny-type equations.

**Scoped obstruction.** The entire displayed holomorphic one-vacuum family cannot be retained unchanged as the ordinary rank-one chiral-parameter tt* vacuum bundle of a four-supercharge extension satisfying that equation. Its physical Berry curvature is strictly nonzero.

This does not say that the benchmark's real-sigma state or its transition amplitude cannot appear in an extended theory. Arithmetic tau initially labels the unitary observable exp(i tau X), not an imaginary chiral coupling. Retaining the real-sigma data leaves freedom to define the physical partner-parameter dependence differently. Additional vacua can also give nonzero matrix commutators; vector-multiplet parameters and periodic systems with coupled Bloch fibers obey different equations. A proposed completion must state which of these changes it makes. Periodic rank-one fiber metrics must not be substituted into an ordinary finite-rank chiral tt* equation without their extra structure.

## 3. The existing Hamiltonian cannot acquire the usual four charges unchanged

There is an independent spectral obstruction at sigma=1/2. It concerns the same Hilbert space and Hamiltonian, rather than the geometry of a chosen parameter family.

### Morse spectrum

The bosonic Morse Hamiltonian is

\[
H_-=-\partial_y^2+\frac{e^{2y}}4
-\frac{a+1}{2}e^y+\frac{a^2}{4}.
\]

Its potential tends to a squared/4 as y tends to minus infinity and grows to infinity at the other end. Its continuum therefore has one open scattering channel with threshold a squared/4. The discrete states can be determined exactly. Put t=exp y and psi=t to the minus one half times u(t). For E below the threshold, the equation becomes Whittaker's equation with

\[
\kappa=(a+1)/2,\qquad
\mu=\sqrt{a^2/4-E}>0.
\]

The solution decaying at t=infinity is proportional to W(kappa,mu)(t). Its non-square-integrable t to the minus mu contribution at t=0 has coefficient proportional to

\[
\frac{\Gamma(2\mu)}{\Gamma(\mu-a/2)}.
\]

It vanishes precisely when mu=a/2-n>0 for a nonnegative integer n. Thus

\[
E_n=an-n^2,\qquad 0\le n<a/2.
\]

This follows from the standard Whittaker connection and endpoint formulas in the [NIST DLMF](https://dlmf.nist.gov/13.14). At a=1/4, corresponding to sigma=1/2, only n=0 is allowed: the bosonic zero state is the sole bound state. The continuum starts at 1/64. The partner Hplus=Aa Aa dagger has no zero state and the same positive spectrum and multiplicity by the polar decomposition of Aa. The doubled Morse system therefore has continuum spectral multiplicity two above 1/64.

### Prime gaps

For r=p to the minus one fourth, T T dagger=I gives

\[
D_pD_p^\dagger=(1+r^2)I-r(T+T^\dagger).
\]

The unilateral adjacency operator T+T dagger has spectrum [-2,2], for example by its sine-transform diagonalization. Hence the positive spectrum is the interval

\[
[(1-r)^2,(1+r)^2].
\]

Dp dagger Dp has the same positive spectrum and one additional zero state. Every prime excitation therefore costs at least (1-p to the minus one fourth) squared. This exceeds 1/49: indeed p at least 2 and

\[
2^{-1/4}<6/7,
\]

because (6/7) to the fourth power exceeds 1/2, equivalently 2592>2401. No decimal approximation or numerical bound is used.

Consequently on the exact interval

\[
J=(1/64,1/49),
\]

every prime factor in the finite tensor product remains in its unique ground state. Only the Morse continuum contributes. The full Hamiltonian restricted to J has spectral multiplicity two.

### Clifford obstruction

Suppose four self-adjoint supercharges R1,...,R4 existed on this same system with the standard algebra and no central charges,

\[
\{R_i,R_j\}=2\delta_{ij}H.
\]

The charges strongly commute with H since each squares to H. On J, which is separated from zero, the bounded normalized charges Ri H to the minus one half are four pairwise anticommuting Hermitian involutions. On each energy fiber they would define a representation of the complex Clifford algebra on four generators.

Such a representation cannot act on a two-dimensional complex fiber. Two anticommuting Hermitian involutions can be put in Pauli-matrix form; a third anticommuting with both is proportional to the remaining Pauli matrix; no fourth Hermitian involution anticommutes with all three. Equivalently the smallest complex module for this four-generator algebra has dimension four. This contradicts the multiplicity-two interval J.

**Scoped obstruction.** The fixed benchmark Hamiltonian and Hilbert space cannot simply be endowed with four standard self-adjoint supercharges of this algebra. Additional fields, changed positive-energy dynamics, or a different supersymmetry algebra are necessary. Central extensions and their shortened multiplets are outside this particular argument. A formal spectator doubling can remove the representation-size obstacle, but it supplies no physical arithmetic identity and no reason for the desired tt* parameter dependence.

## 4. The next analytical question

The benchmark remains valuable: it supplies exact gamma/Euler amplitudes and a positive starting Hilbert theory. A substantive extension must now identify what it changes rather than merely rename the existing supersymmetry.

The strongest initial test is:

> Construct a four-supercharge extension for the Morse factor and one prime, specifying the physical parameter multiplets, adjoint, boundary source, and arithmetic observable. Determine whether its physical ground-state bundle and complete transition pairing retain the benchmark amplitude while evading the rank-one curvature and fixed-spectrum restrictions. Then identify the supersymmetric equation that constrains the first normal derivative and its contact normalization.

Possible changes include nontrivial vacuum mixing, a field-valued or periodic ground space, vector-multiplet geometry, or a new physical boundary insertion. Their usefulness must be assessed by the complete pairing, not only by the number of supercharges. The normalization and pole problem remains even if an extended model reproduces LambdaS exactly; neither obstruction above purports to solve that problem.
