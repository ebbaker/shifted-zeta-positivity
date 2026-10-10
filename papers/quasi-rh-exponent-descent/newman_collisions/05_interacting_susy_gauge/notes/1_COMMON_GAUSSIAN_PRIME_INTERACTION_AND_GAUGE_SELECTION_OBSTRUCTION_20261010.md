# Common Gaussian prime interaction and a gauge selection obstruction

10 October 2026. GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. Derivations and replay checks are internal,
not independent mathematical validation.

This bounded scout develops [Program 05](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
It does not claim a Parisi--Sourlas field theory or a Nicolai map for zeta.
It tests one explicit finite interacting dictionary and its Ward/phase
selection content before any continuum construction.

## 1. A genuine two-variable reduction and its sign

Use the even full theta kernel from the stable manuscript,
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\quad(u\ge0).
\]
For \(t>0\), put \(p_t(\lambda)=(\pi t)^{-1/2}e^{-\lambda^2/t}\).
The exact enlarged state and reduction are
\[
\Psi_t(\lambda,u)=p_t(\lambda)\Phi_e(u),\quad
\partial_t\Psi_t=\tfrac14\partial_\lambda^2\Psi_t,\quad
\mathcal P_x\Psi=\tfrac12\int_{\mathbb R^2}
e^{2\lambda u+ixu}\Psi(\lambda,u)\,d\lambda\,du.
\tag{1}
\]
Completing the square gives
\[
\int p_t(\lambda)e^{2\lambda u}d\lambda=e^{tu^2},
\qquad \mathcal P_x\Psi_t=H_t(x).
\tag{2}
\]
Hence the initial trace is exactly
\(H_0=\xi(1/2+ix/2)/8\); \(p_0\) is interpreted as a delta
distribution and (2) supplies its continuous marginal limit.
On compact positive time intervals, completing the Gaussian and theta's
super-exponential decay justify Fubini and all fixed finite derivatives.
Integration by parts in \(\lambda\), with its endpoint terms vanishing,
yields
\[
\mathcal P_x(\tfrac14\partial_\lambda^2\Psi_t)
=\tfrac12\int u^2e^{2\lambda u+ixu}\Psi_t
=-\partial_x^2\mathcal P_x\Psi_t.
\tag{3}
\]
The auxiliary dynamics is forward heat, but its observation is unbounded
and exponentially weighted. A contraction observability theorem on
unweighted \(L^2(d\lambda\,du)\) cannot be substituted for (3).
Each spatial derivative simply inserts \((iu)^j\), so the full
collision jets are retained without a cutoff approximation.

## 2. A composite-complete finite interaction

For the fixed-cutoff approximation of Heat Note 8, write
\[
\ell_n=\log n,\quad
\sigma=\tfrac12+t\alpha_r/2,\quad
\chi=(x-t\alpha_i)/2,\quad
U_p=e^{i\chi\log p},\quad
q_n=e^{t\ell_n^2/4-\sigma\ell_n+i\chi\ell_n}.
\]
The full genuine finite sum is
\[
F_{t,N}=2\operatorname{Re}\left[e^{i\theta_t}
\sum_{n\le N}q_n\right].
\tag{4}
\]
The exact common-Gaussian identity is
\[
q_n=n^{-\sigma}U_n\int p_t(\lambda)n^\lambda\,d\lambda,
\qquad U_n=\prod_p U_p^{a_p(n)}.
\tag{5}
\]
This is a finite-cutoff identity. The positive \(e^{t\log^2n/4}\)
weight prohibits extending the sum to an unrestricted Dirichlet series.

Choose the closed exponent box
\[
I=\{2^a3^b:0\le a,b\le2\}
=\{1,2,3,4,6,9,12,18,36\}.
\]
Set \(X=2^{\lambda-\sigma}U_2\), \(Y=3^{\lambda-\sigma}U_3\).
Then
\[
\sum_{n\in I}q_n
=\int p_t(\lambda)(1+X+X^2)(1+Y+Y^2)\,d\lambda.
\tag{6}
\]
This is an explicit measure/observable dictionary retaining every
composite and every actual common-height phase. One common \(\lambda\)
couples the two prime exponent channels.
The effective positive coefficient \(w_{ab}\) has
\[
\log w_{ab}=\tfrac t4(a\log2+b\log3)^2
-\sigma(a\log2+b\log3).
\]
Its interaction matrix is rank one,
\[
\nabla_{a,b}^2\log w=
\tfrac t2
\begin{pmatrix}(\log2)^2&\log2\log3\\
\log2\log3&(\log3)^2\end{pmatrix},
\quad \det\nabla^2\log w=0.
\tag{7}
\]
The nontrivial discrete cross ratio is
\[
\boxed{\frac{q_{a+1,b+1}q_{a,b}}
{q_{a+1,b}q_{a,b+1}}
=e^{(t/2)\log2\log3}>1.}
\tag{8}
\]
All phases cancel in this ratio. Independent prime Gaussian variables
would remove precisely the mixed \(tab\log2\log3/2\) term and fail (8).
Thus the interaction has exact content beyond a product of independently
deformed prime channels, but (8) remains true under every multiplicative
unit-modulus twist. It does not select the actual orbit.

For an elementary SUSY realization, take the quartet/action of Program
04 with \(F(u)=u\), whose partition is one, and insert \(e^{cu}\).
After the prescribed fermion and auxiliary Gaussian integrations its
value is \(e^{c^2/(2\lambda_{\rm loc})}\).
Choose \(\lambda_{\rm loc}=1\) and
\(c=\sqrt{t/2}(a\log2+b\log3)\). This gives the heat factor in (7).
The source is not a protected \(Q\)-closed observation. Adding the
quartet therefore does not upgrade (8) to a new signed Ward inequality.

## 3. Exact physical derivatives and moving sources

Let \(A_n=\log w_n+i\phi_n\), with
\(\phi_n=\theta_t+\chi\ell_n\). At fixed time and fixed \(I\),
\[
F_{t,I}^{(j)}=2\operatorname{Re}\sum_{n\in I}
e^{A_n}\mathcal B_j(A_n',\ldots,A_n^{(j)}),\quad0\le j\le4,
\tag{9}
\]
where \(\mathcal B_0=1\), \(\mathcal B_1=A'\),
\(\mathcal B_2=A''+(A')^2\),
\(\mathcal B_3=A'''+3A'A''+(A')^3\), and
\[
\mathcal B_4=A''''+4A'A'''+3(A'')^2
+6(A')^2A''+(A')^4.
\]
In particular
\[
A_n'=-\sigma'\ell_n+i\theta_t'+i\chi'\ell_n,\quad
r_n=-4\phi_n'/L,\quad c_n=-4(\log w_n)'/L,
\]
\[
2F_{t,I}'/L=\sum_{n\in I}w_n(r_n\sin\phi_n-c_n\cos\phi_n).
\tag{10}
\]
The amplitude drift is present. With \(\alpha'(s)=u+iv\) and
\(s=(1-ix)/2\), \(\sigma'=tv/4\), hence \(c_n=tv\ell_n/L\),
agreeing with Note 8.

The finite approximation has moving background sources.
Differentiating (5) in time produces both \(\ell_n^2/4\) and
\(-\sigma_t\ell_n+i\chi_t\ell_n\); the carrier contributes
\(i\partial_t\theta_t\). It is not itself the bare unnormalized
scalar heat equation. The genuine equation is (3). The imported complete
interface for the full \(N\) is
\[
|Q_t^{(j)}-F_{t,N}^{(j)}|\le j!L^j\eta_N,\quad
\eta_N\le5e^{-\kappa(\kappa+4)/(16t)}.
\tag{11}
\]
A small exponent box alone has no such error theorem. Recombining it
with the complement is essential before applying any joint-vector
or threshold test, including the measured quadratic payment of Note 13.

## 4. What gauge averaging and coefficient uniqueness permit

If \(U_2,U_3\) in (6) are independently Haar integrated, every
nonconstant monomial disappears:
\[
\int_{\mathbb T^2}\sum_{n\in I}q_n\,dU_2\,dU_3=1.
\tag{12}
\]
The real readout becomes \(2\cos\theta_t\), losing the arithmetic terms.
Gauge invariance must therefore keep the physical holonomies as
background sources or specify compensated charged observations. Calling
Haar averaging an exact reduction would fail (4).

There is a related uniqueness obstruction. Suppose a new interacting
measure produces a finite generating polynomial
\(\sum_{a,b}\widetilde w_{ab}U_2^aU_3^b\) equal to (6) for every pair
of background holonomies. Fourier coefficient uniqueness forces
\(\widetilde w_{ab}=w_{ab}\) for each sector. Such an exact interaction
can rearrange the representation, but its effective weights are already
fixed. Any extra constraint must concern actual source correlations or
observations, rather than a different freely fitted weight table.

A stronger fixed-coefficient algebraic selection test is available.
Let \(R(U_2,U_3)\) be a finite Laurent polynomial with coefficients
independent of \(\chi\). If
\[
R(e^{i\chi\log2},e^{i\chi\log3})=0
\quad\text{for all \(\chi\) in any open interval},
\tag{13}
\]
then \(R\) is the zero polynomial. Distinct exponent pairs give distinct
frequencies \(a\log2+b\log3\), since \(2^a3^b=1\) only for
\(a=b=0\). Differentiating the finite exponential sum through degree
one less than its number of frequencies gives an invertible Vandermonde
system. Thus a nonzero finite polynomial identity of this particular
kind cannot select the entire actual orbit from arbitrary twists.

Equation (13) has fixed coefficients. It does not exclude identities
with actual \(x\)-dependent amplitudes, source derivatives, nonlocal
constraints, or signed inequalities on a parameter region. These are
precisely the forms in which a useful arithmetic relation could remain.

## 5. Result and continuation

The genuine enlarged heat representation is exact. The finite
prime-exponent dictionary displays a true coupled heat interaction
and its cross-ratio rigidity. Independent prime diffusion and Haar
averaging fail exact matching. The tested coefficient/gauge identities
are shared by twists or reduce to coefficient uniqueness, and therefore
do not supply the required collision exclusion.

The strongest next task is a phase-sensitive estimate connecting this
block to its complement on the actual moving source curve, retaining
(9)--(11). The fixed-coefficient polynomial identity approach in (13)
is exhausted. No uncontrolled field-theory limit or general SUSY
dimensional-reduction claim is needed to reach this stopping result.

For external context only,
[Lechtenfeld--Rupprecht, Universal form of the Nicolai map](https://arxiv.org/abs/2104.00012)
constructs maps for specified globally supersymmetric theories; its
arXiv abstract was checked during this scout. It supplies no map from
theta or from (6) to such a theory. All identities here are direct
derivations. Storage follows [LARGE_FILES.md](../../../../../LARGE_FILES.md).
