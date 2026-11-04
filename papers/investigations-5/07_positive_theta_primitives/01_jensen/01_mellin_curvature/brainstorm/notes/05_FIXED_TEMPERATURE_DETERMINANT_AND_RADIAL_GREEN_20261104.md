# Fixed-temperature determinant interpretation and radial Green transfer

**Continuation, 4 November 2026:** [Note06](06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md) derives the full determinant boundary expansion and the exact fixed-temperature configurational interpretation, with its quantum scope stated explicitly.

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance: **gpt-6-astra (Codex), recorded effort xhigh**. Chat `01a1a455-6c1d-7aa2-9723-43ab36704924`, turn `01a1a6fb-2e86-7061-bd47-2d0b81403d35`; Mellin-curvature history **0004**.

**Author correction.** In the box interpretation u = log(beta)/4 is a thermodynamic parameter, not a particle coordinate. The source-field operators psi(u) in Notes03–04 are auxiliary algebraic encodings and will not be used as physical creation operators. Work at fixed temperature with spatial box modes, examine the actual determinant integrand, and also consider the three-dimensional primitive integration-by-parts picture from Investigation05. This note corrects the physical interpretation, while preserving earlier algebraic identities in their stated auxiliary spaces.

**Status.** Exact identities and a scoped occupation-count diagnostic, derived and checked by this assistant; no independent review, new positivity estimate, numerical campaign, or selected complete Hamiltonian model. Fixed particle number N is not silently identified with determinant order r.

## 1. The box at fixed beta

Continue with noninteracting spinless fermions, as in the preceding discussion. In units giving the desired square spectrum, the Dirichlet box is 0 < x < 1, with
\[
\varphi_n(x)=\sqrt2\sin(n\pi x),\qquad E_n=\pi n^2,
\quad \{\hat d_n,\hat d_m^\dagger\}=\delta_{nm}.
\]
The physical field and Hamiltonian are
\[
\hat\psi(x)=\sum_n\varphi_n(x)\hat d_n,
\qquad
\hat H_0=\sum_nE_n\hat d_n^\dagger\hat d_n
=\frac1\pi\int_0^1\partial_x\hat\psi^\dagger\partial_x\hat\psi\,dx.
\tag{1}
\]
The latter identity is understood as the usual kinetic-energy form on the Dirichlet domain. Fix the particle sector N and use
\[
\rho_{\beta,N}=Z_N^{-1}\Pi_Ne^{-\beta\hat H_0},\qquad
Z_N=\sum_{n_1<\cdots<n_N}e^{-\beta\sum_aE_{n_a}}.
\tag{2}
\]
TFD is an equivalent purification of (2). The trace in the original primitive is specifically Q(beta) = Z_1(beta), so p(u) = e^u Z_1(e^{4u}). The one-particle heat trace supplies spectral data for the gas, but it is not the canonical N-particle partition function for arbitrary N.

The natural fixed-temperature N-particle kernel is explicit. Put
\[
K_\beta(x,y)=\sum_ne^{-\beta E_n}\varphi_n(x)\overline{\varphi_n(y)}.
\]
Then the physical field correlation containing all N particles is
\[
\boxed{
\left\langle\hat\psi^\dagger(y_1)\cdots\hat\psi^\dagger(y_N)
\hat\psi(x_N)\cdots\hat\psi(x_1)\right\rangle_{\beta,N}
=\frac{\det[K_\beta(x_a,y_b)]_{a,b=1}^N}{Z_N}.}
\tag{3}
\]
This follows by summing occupation eigenstates: annihilating all N particles leaves vacuum, giving two mode determinants, and Cauchy–Binet sums them into (3). Its diagonal divided by N! is the normalized joint position density. The full-coordinate diagonal identity appears in Dean et al., equations (59)–(68); see the [checked references](../references/02_FIXED_N_FERMION_CORRELATIONS.md).

Equation (3) is not a claim that arbitrary lower-order canonical correlations equal determinants of the canonical one-particle density matrix. Fixed-N occupation constraints prevent that general Wick factorization; Schönhammer's introduction and Sections II–III clarify the distinction. No grand-canonical replacement or large-N limit is used here.

## 2. What the actual determinant integrand contains

The established ordered-chamber representation is
\[
D_{r,k}=\frac1{\prod_{j=0}^{r-1}(2k+2j)!}
\int_{0<u_1<\cdots<u_r}
\left(\prod_ju_j^{2k}\right)V(\mathbf u^2)\Delta_r(\mathbf u)\,d\mathbf u,
\tag{4}
\]
\[
\Delta_r(\mathbf u)=\det[\Phi^{(2i)}(u_j)]_{i=0,\ldots,r-1;\ j=1,\ldots,r},
\qquad V(\mathbf u^2)=\prod_{a<b}(u_b^2-u_a^2).
\]
See [Jensen Note03](../../../notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md), Section 2, and [Note14](../../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md), Section 2. All factors outside Delta_r are positive in the ordered interior.

At a fixed tuple of temperatures beta_j = exp(4u_j), define
\[
q_i(u_j)=\operatorname{Tr}\left[\rho_{\beta_j,1}
P_{2i}(\beta_j\hat H_0)\right].
\]
The exact thermal reading of the sign-bearing determinant is
\[
\boxed{\Delta_r(\mathbf u)
=\left(\prod_jp(u_j)\right)\det[q_i(u_j)]_{i,j}.}
\tag{5}
\]
Thus the existing integrand compares derivative insertions of the same one-particle heat trace at r thermodynamic parameter values. Its columns are temperature-response vectors, not spatial coordinates or distinct occupied box modes. “Fixed integrand point” means fixed u_1,...,u_r in this representation; it does not make the temperatures equal. It is not yet identified with (3), an energy expectation, or an N-particle density.

An exact diagnostic shows why simply reading the existing antisymmetry as exclusion of repeated box energies is invalid. Expanding (5) before dividing by positive normalizations gives
\[
\Delta_r(\mathbf u)=e^{\sum_ju_j}
\sum_{n_1,\ldots,n_r\ge1}
e^{-\sum_j\beta_jE_{n_j}}
\det[P_{2i}(\beta_jE_{n_j})]_{i,j}.
\tag{6}
\]
Repeated spectral labels n_j are allowed and need not vanish when beta_j differ. For r = 2, the n_1 = n_2 = n contribution contains
\[
P_0(\beta_1E_n)P_2(\beta_2E_n)
-P_2(\beta_1E_n)P_0(\beta_2E_n),
\]
which is generally nonzero. A two-spinless-fermion trace on a one-mode Hilbert space instead vanishes. This excludes only the direct termwise identification with distinct occupied energy modes; it does not exclude a different observable/preparation representation in the complete box system.

Accordingly, the earlier statement that r is exactly a particle number was true for the auxiliary source-coordinate Fock encoding, not an established identification with N of this physical box. Such an identification is a question to solve, not a premise.

## 3. The local fixed-temperature quantity

At u_1 = ... = u_r, Delta_r vanishes for r > 1 because its columns coincide. The nontrivial local fixed-temperature limit is obtained after extracting its Vandermonde zero:
\[
\boxed{
\lim_{u_j\to u}\frac{\Delta_r(\mathbf u)}{V(\mathbf u)}
=\frac{\det[\Phi^{(2i+j)}(u)]_{i,j=0}^{r-1}}
{\prod_{j=0}^{r-1}j!}
=\frac{p(u)^r}{\prod_jj!}
\det\!\left[\left\langle P_{2i+j}(\beta\hat H_0)\right\rangle_{\beta,1}\right].}
\tag{7}
\]
Taylor expansion of each column proves the first equality. The second uses the complete unnormalized thermal-trace derivative formula, not repeated differentiation of normalized expectations alone. This is a Wronskian of the derivative-inserted partition trace, expressible as a determinant of energy moments at one temperature. It measures the local linear independence of those response functions. No connected-correlation or positive susceptibility interpretation is assumed.

For r = 2 it is Phi Phi''' - Phi' Phi'', or Phi^2 times the derivative of Phi''/Phi. In the one-mode comparison, the recurrence gives at x = beta E = 4:
\[
(P_0,P_1,P_2,P_3)=(20,-92,-1164,17540),\qquad
P_0P_3-P_1P_2=243712.
\]
These integers were checked by the polynomial recurrence with integer arithmetic. This is an algebraic occupation diagnostic, not a theta truncation used to estimate its sign. That comparison lacks the full spectrum and reflection.

The complete integrand in (4) has two Vandermonde zeros at confluence. For u > 0, with m = r(r-1)/2, its ratio to V(u_1,...,u_r)^2 tends to
\[
\frac{u^{2kr}(2u)^m}{\prod_j(2k+2j)!\prod_jj!}
\det[\Phi^{(2i+j)}(u)]_{i,j=0}^{r-1}.
\tag{8}
\]
The endpoint u = 0 has different vanishing powers. Equations (7)–(8) inspect one temperature locally; they do not replace the separated-temperature integral (4).

## 4. The three-dimensional picture and exact boundary terms

The author identified the relevant earlier investigation. [Radial Note01, Section 2](../../../../../05_radial_theta_collision_geometry/notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md) and [Radial Note73](../../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md) give
\[
R=e^{2u},\quad A(R)=\sum_{n\ge1}e^{-\pi n^2R^2}=Q(R^2),
\quad p(u)=R^{1/2}A(R),
\]
\[
\boxed{\Phi(u)=\tfrac12R^{5/2}\Delta_3A(R),\qquad
\Delta_3=\partial_R^2+\frac2R\partial_R.}
\tag{9}
\]
The radial variable has been renamed R to keep it distinct from determinant order r. The energy index n still ranges over one-dimensional square modes. Replacing the sum by a three-dimensional lattice changes the source.

For an admissible smooth probe f, put F(R) = R^(-1/2) f(log(R)/2). Then
\[
\int_0^\infty\Phi f\,du
=\frac14\int_1^\infty A(R)\Delta_3F(R)R^2dR
+\frac14[-A'(1)F(1)+A(1)F'(1)].
\tag{10}
\]
Full theta reflection gives p'(0) = -1/2, hence A'(1) = -A(1)/2 - 1/4. Therefore
\[
\boxed{
\int_0^\infty\Phi f\,du
=\frac{f(0)}{16}+\frac{p(0)f'(0)}8
+\frac18\int_0^\infty p(u)[f''(u)-f(u)]du.}
\tag{11}
\]
The complete tail removes the outer boundary. If applied to determinant formulas, (11) must be applied to complete probes with all remaining derivative and boundary contributions; moving each term separately and discarding faces would change the quantity.

For the even moment probes m_j(u) = u^(2j)/(2j)!, let d_j = integral p m_j. Then
\[
c_0=\frac1{16}-\frac{d_0}{8},\qquad
c_j=\frac{d_{j-1}-d_j}{8}\quad(j\ge1).
\tag{12}
\]
This provides a direct thermodynamic reading of integration by parts: the heat trace Q remains unchanged, while source derivatives are transferred into signed functions of log inverse temperature plus the modular endpoint constant. At determinant level these substitutions generate primitive-moment minors and boundary contributions. Positivity of d_j alone does not sign the differences or resulting minors.

## 5. What statistical mechanics survives in three dimensions?

There are two distinct, explicit interpretations.

**Geometric thermodynamic parameter.** Keep R = sqrt(beta) as a parameter. A(R) is exactly the same box heat trace. The radial Laplacian is a geometric device for transferring derivatives among thermodynamic probes. This needs no claim that R is the particle coordinate and preserves the quantum statistical mechanics of (1)–(2).

**Actual spatial radial coordinate in a new model.** In dimensionless units at a reference bath inverse temperature beta_* = 1, assign internal levels the spatial potentials
\[
V_n(\mathbf R)=\pi n^2|\mathbf R|^2.
\]
Then A(R) is exactly the local internal partition sum. At a fixed spatial point, its normalized internal weights are ordinary Gibbs weights e^(-V_n)/A. Direct differentiation gives
\[
\frac{\Delta_3A}{A}
=\left\langle |\nabla V_n|^2-\Delta_3V_n\right\rangle_R
=\left\langle4\pi^2n^4R^2-6\pi n^2\right\rangle_R.
\tag{13}
\]
Thus Phi is a weighted force-squared-minus-potential-curvature expectation. With force F_n = -grad V_n, the insertion is |F_n|^2 + div F_n. At general bath beta_* the expression is beta_*^2 |grad V_n|^2 - beta_* Delta V_n and the partition sum is A(sqrt(beta_*)R). The potential itself need not depend on bath temperature.

The classical configurational weight is A(R)d^3R after integrating a common classical kinetic momentum factor. Green's identity then has the familiar force/curvature integration-by-parts meaning, with the R = 1 boundary retained if the configuration region is exterior to that sphere. This is an exact classical configurational interpretation of the displayed weight.

For a genuine quantum particle moving in R, adding a kinetic term gives, for example, a multichannel oscillator Hamiltonian with blocks -kappa Delta_3 + pi n^2 R^2. Its quantum thermal diagonal includes propagation and is not simply exp(-pi n^2 R^2). No equality of that quantum Gibbs density with A, and no exact fermionic N-particle interpretation of the original source, follows from (13). Also A is a partition density here, not a wavefunction whose Laplacian can be identified directly with a positive kinetic-energy expectation.

**Preferred next comparison.** At fixed beta use the physical box field (1) and its N-particle heat-kernel correlation (3) as the candidate object to match, carrying the response insertions in (5) or the local diagnostic (7). In parallel, (11)–(12) provide an exact way to transfer those insertions to thermodynamic probes without changing the equilibrium ensemble. The 3D force interpretation is useful if a new classical configurational model is intended; its quantum completion remains a separate choice. No physical identification r = N, source replacement, or sign theorem is asserted.

## 6. Status and controls

Read with the [result index](../../../../../../../result-summaries/README.md), [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [geometric realizations](../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [normalizations](../../../../../../../avoid/08_normalization_and_constant_slips.md), and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The one-mode diagnostic excludes only the termwise occupied-mode reading; it fails full theta spectrum/reflection and cannot challenge (4) for the complete source. Weighted-square controls retain suitable Boltzmann and radial derivative formulas but change the unit weights and reflection. Euler-factor and reflected shape controls may retain generic source/integration-by-parts features but not the literal unchanged heat trace A. Radial Note73 explicitly constructs positive-primitive controls retaining the endpoint constant while lacking the canonical theta primitive. These observations screen generic state positivity or Green transfer as a sign mechanism; they do not exclude a new complete-source quantum or thermodynamic estimate. No numerical control signs or new parameter ranges are claimed.
