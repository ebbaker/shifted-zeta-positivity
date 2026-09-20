# Quantum ground-state correlations: explicit models and a moment obstruction

Date: 13 September 2026.

This investigation follows the [operator-perspective note](OPERATOR_PERSPECTIVE_20260913.md).
It asks whether the arithmetic energy can be obtained as a ground-state
two-point function, rather than as a classical minimized energy. The results
below are calculations within explicitly specified Gaussian models; they do
not establish positivity of the full Weil form or a new positivity interval.

The investigation produces more than a change of notation:

- A positive quantum Hamiltonian and an observable give the gamma kinetic
  term exactly as a vacuum correlation, on its full logarithmic form domain.
- A new coupled two-field covariance replaces the first two loop channels and
  cancels three leading residual coefficients simultaneously.
- One further auxiliary field cancels a fourth coefficient while retaining a
  positive Hamiltonian. Its entire covariance is calculated explicitly.
- A negative shifted moment determinant prevents *any* positive mass-matrix
  model of the specified class from canceling the first five coefficients while
  replacing only those two original channels, regardless of the number of
  auxiliary fields.

| Response model | Canceled leading inverse powers | First surviving residual order |
| --- | --- | --- |
| Original loop response | None | \(|\tau|^{-2}\) |
| Manuscript's independent low-channel split | \(|\tau|^{-2}\) | \(|\tau|^{-4}\) |
| Coupled two-field vacuum covariance below | \(|\tau|^{-2},|\tau|^{-4},|\tau|^{-6}\) | \(|\tau|^{-8}\) |
| Coupled three-field vacuum covariance below | The preceding three and \(|\tau|^{-8}\) | \(|\tau|^{-10}\) |

The improvement concerns high-frequency structure and kernel regularity.
Neither a smaller operator norm of the error nor a better Weil positivity bound
follows from the table. These Gaussian covariance models also admit classical
positive realizations. Thus the progress comes from allowing coupled fields
and a different observable, not from a demonstrated effect unique to quantum
mechanics.

## 1. The observable and the Gaussian control

The quantum target is an independently specified positive Hilbert space, a
Hamiltonian with a ground state \(|\Omega_L\rangle\), and an operator-valued
field \(\widehat{\mathcal O}_L(x)\) satisfying

\[
Q_{0,L}[f]=\langle\Omega_L|
\widehat{\mathcal O}_L(f)^\dagger
\widehat{\mathcal O}_L(f)|\Omega_L\rangle,
\qquad
\widehat{\mathcal O}_L(f)=\int_{I_L}f(x)
\widehat{\mathcal O}_L(x)\,dx.
\]

The positivity would follow from the ordinary Hilbert norm. The integral is a
smearing of an operator-valued distribution. Equality of the full correlation
kernel would cover every admitted complex input, without first choosing a
profile. The interacting dynamics, if any, need not be quadratic, since this
particular observable is quadratic in the smearing function by definition.

There is an important exact control. For a finite regulator, let a classical
quadratic energy be

\[
\mathcal E[f,u]=Z[f]+\tfrac12(u-u_f)^TA(u-u_f),\qquad A>0.
\]

Adding \(\tfrac12\widehat p^TM^{-1}\widehat p\), with a positive
source-independent mass matrix, gives a displaced oscillator system. Its
frequencies are independent of \(f\), and hence

\[
E_0[f]-E_0[0]=Z[f].
\]

Consequently merely quantizing the manuscript's existing quadratic minimization
models does not change their residuals. The construction below instead chooses
a quantum covariance observable and then changes the coupled field Hamiltonian.
It is a new Gaussian model, not a quantum correction computed for the old one.

The oscillator facts used here are \(E_0=\nu/2\) and
\(\langle\phi^2\rangle_0=1/(2\nu)\), in units \(\hbar=1\).
They follow from the creation and annihilation operators; see
[Tong, “Free Fields”](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S2.html).
Vacuum-energy subtraction must be distinguished from subtraction of a
two-point function. The observable below uses an ordinary positive correlation,
not a normal-ordered correlation with its vacuum expectation removed.

## 2. A quantum Hamiltonian giving the gamma kinetic term exactly

Use \(D=-i\partial_x\), \(A=D^2\) on the whole line, and
\(a_k=2k+1/2\). Write

\[
B(s)=\sum_{k\geq0}\frac2{a_k}\frac{s}{s+a_k^2}.
\]

For each mass choose a real canonical field with frequency operator
\(h_a=A+a^2\). Its Hamiltonian is formally

\[
\widehat H_a=\frac12\int_{\mathbb R}
\left[\widehat\pi_a(x)^2+
\bigl((A+a^2)\widehat\phi_a(x)\bigr)^2\right]dx.
\]

The precise vacuum-subtracted operator is the nonnegative second-quantized
operator \(d\Gamma(h_a)\) on bosonic Fock space. The Hamiltonian has a
positive local spatial energy with fourth-order spatial derivatives. Its
dispersion is \(\nu_a(\tau)=\tau^2+a^2\); this is an auxiliary,
nonrelativistic dynamics, not the ordinary relativistic scalar dispersion.

The ground-state field covariance is \(\tfrac12(A+a^2)^{-1}\). Define

\[
\widehat{\mathcal O}_a(x)=\frac2{\sqrt a}\partial_x\widehat\phi_a(x).
\]

Its covariance multiplier is exactly

\[
\frac4a\frac{\tau^2}{2(\tau^2+a^2)}
=\frac2a\frac{\tau^2}{\tau^2+a^2}.
\]

Independent channels have zero cross covariance, so their sum realizes
\(B(A)\). More precisely, the one-particle creation amplitude for the
smeared derivative observable can be chosen as

\[
\Gamma_aF(\tau)=\sqrt{2/a}\,
\frac{i\tau}{\sqrt{\tau^2+a^2}}\widehat F(\tau),
\]

with one-particle measure \(d\tau/(2\pi)\). For the zero extension
\(F=E_Lf\), the direct sum has finite norm exactly on

\[
\mathcal D_{\log,L}=\left\{f\in L^2(I_L):
\int_{\mathbb R}\log(2+|\tau|)|\widehat{E_Lf}(\tau)|^2d\tau<\infty\right\}.
\]

Thus

\[
\boxed{\|\widehat{\mathcal O}_\gamma(f)\Omega\|^2
=\frac1{2\pi}\int B(\tau^2)|\widehat F(\tau)|^2d\tau
=K[F].}
\]

The Fock vacuum is the ground state of
\(d\Gamma(\bigoplus_k h_{a_k})\). It exists without assigning a value to
an infinite sum of zero-point constants. The smeared observable acting on the
vacuum is defined by the convergent one-particle sum above. This handles the
infinite tower without introducing the divergent unprepared source vector
discussed in the manuscript.

This is an explicit quantum realization of a known positive gamma factor.
It neither supplies the remaining arithmetic terms nor explains why the
specified masses and weights are selected.

## 3. The old loop response as a quantum covariance

For the remainder of the concrete calculation, use the manuscript's one-prime
model with \(p=2\), \(\ell=\log2\), \(r=2^{-1/2}\), and

\[
v(\tau)=w_0-2\ell\sum_{m\geq1}r^m\cos(m\ell\tau),
\qquad w_0=\psi(1/4)-\log\pi,
\qquad q(\tau)=e^{-2v(\tau)}.
\]

This covers the target's first-prime interval regime
\(\log2<L\leq\log3\), retaining the full primitive history series.
Here \(v<0\), so \(q>1\). For example,
\(v\leq w_0+2\ell r/(1+r)<0\). At fixed parameters \(q\) has finite
positive upper and lower bounds and is real analytic in the phase
\(\theta=\ell\tau\). In the matrix calculations first regard \(q\geq1\)
as an independent scalar, and then substitute this function.

Choose frequency operators

\[
h_{a,q}=A+a^2q(D)
\]

with the same derivative observable as above. Their vacuum response is

\[
T_a(s,q)=\frac2a\frac{s}{s+a^2q},\qquad s=\tau^2.
\]

The whole tower therefore gives \(B(s/q)\), exactly the old positive loop
response. This Hamiltonian realizes the modulus-dependent pairing; it does not
identify the causal loop amplitude with unitary physical time evolution.

Let

\[
\rho(\tau)=B(s/q)-B(s)+\tfrac12\log q.
\]

The target identity remains
\(\mathsf W_L=\mathsf Z_L+\mathsf P_L-\mathsf R_L\), with \(\mathsf P_L\)
the pole operator and \(\mathsf R_L\) the interval compression of this
residual. The quantum reinterpretation alone has not altered it.

## 4. A coupled mass matrix and the matching conditions

We now replace precisely the first two channels, with masses \(1/2\) and
\(5/2\), leaving all higher channels unchanged. Their total leading weight is
\(c_0=24/5\). Introduce a positive matrix \(\mathcal M(q)\) and canonical
fields whose frequency operator is

\[
h=A I+\mathcal M(q(D)).
\]

Their positive Hamiltonian is \(\tfrac12(\|\pi\|^2+\|h\phi\|^2)\),
defined after vacuum subtraction by \(d\Gamma(h)\). Use the fixed observable

\[
\widehat{\mathcal O}_{\rm pair}(x)=\sqrt{2c_0}\,
\partial_x\widehat\phi_1(x).
\]

The resulting exact response is

\[
\mathcal T(s,q)=c_0s\,e_1^T(sI+\mathcal M(q))^{-1}e_1.
\]

This formula is the full observable, not an expansion. Define its moments
\(m_j=c_0e_1^T\mathcal M^je_1\). At fixed bounded phase data,

\[
\mathcal T(s,q)=c_0-\frac{m_1}s+\frac{m_2}{s^2}
-\frac{m_3}{s^3}+\frac{m_4}{s^4}-\frac{m_5}{s^5}+\cdots.
\]

The corresponding original moments are \(c_jq^j\), where

\[
c_j=2(1/2)^{2j-1}+2(5/2)^{2j-1},
\qquad
(c_0,c_1,c_2,c_3,c_4,c_5)
=\left(\frac{24}5,6,\frac{63}2,\frac{1563}8,
\frac{39063}{32},\frac{976563}{128}\right).
\]

Write the gamma asymptotic as

\[
B(\tau^2)=\log|\tau|+\text{constant}
+\sum_{j\geq1}b_j\tau^{-2j},
\]

where the first five coefficients are

\[
(b_1,b_2,b_3,b_4,b_5)=
\left(-\frac1{24},-\frac7{960},-\frac{31}{8064},
-\frac{127}{30720},-\frac{511}{67584}\right).
\]

These are asymptotic coefficients, not a convergent series identity. They
follow from the digamma expansion, or exactly from
\(b_j=(-1)^{j+1}2^{2j}B_{2j}(1/4)/(2j)\); see
[NIST DLMF, “Asymptotic Expansions”](https://dlmf.nist.gov/5.11).

Canceling the residual coefficient at order \(s^{-j}\) requires

\[
\boxed{m_j=t_j(q):=c_jq^j+(-1)^{j+1}b_j(q^j-1).}
\]

These are necessary matching conditions inside a specified positive covariance
family. No spectral square root of the unknown Weil operator is used.

## 5. Two fields cancel three coefficients and remain positive

Set

\[
\mu=\frac{t_1}{c_0},\qquad
\beta^2=\frac{t_2}{c_0}-\mu^2,\qquad
N=\frac{t_3}{c_0}-\mu^3-2\mu\beta^2,\qquad
\nu=\frac{N}{\beta^2},
\]

and define

\[
\mathcal M_2(q)=
\begin{pmatrix}\mu&\beta\\\beta&\nu\end{pmatrix},\qquad\beta>0.
\]

To check positivity without assuming any arithmetic sign result, put
\(z=q-1\geq0\). Direct expansion gives

\[
\mu=\frac54+\frac{715}{576}z,
\qquad
\beta^2=5+\frac{7699}{768}z+\frac{1666559}{331776}z^2.
\]

Moreover, with \(\Delta=\mu N-(\beta^2)^2\),

\[
\Delta=
\frac{125}{16}+\frac{27645}{896}z+
\frac{1685029}{36864}z^2+
\frac{11653297}{387072}z^3+
\frac{3316762711}{445906944}z^4>0.
\]

Since \(\det\mathcal M_2=\Delta/\beta^2>0\) and \(\mu>0\), the
mass matrix is positive definite for every \(q\geq1\). The complete response is

\[
\boxed{
\mathcal T_2(s,q)=
\frac{c_0s(s+\nu)}{(s+\mu)(s+\nu)-\beta^2}.}
\]

Matrix multiplication gives

\[
m_1=c_0\mu=t_1,\qquad
m_2=c_0(\mu^2+\beta^2)=t_2,
\qquad
m_3=c_0(\mu^3+2\mu\beta^2+\nu\beta^2)=t_3.
\]

Thus all first three residual coefficients vanish. At \(q=1\),
\((\mu,\beta,\nu)=(5/4,\sqrt5,21/4)\). This matrix has eigenvalues
\(1/4,25/4\), with the correct observable weights, and its response is
exactly the original pair for every \(s\). The uncoupled control is exact.

The new positive total response is

\[
Z_2(\tau)=B(s/q)-T_{1/2}(s,q)-T_{5/2}(s,q)+\mathcal T_2(s,q).
\]

The subtractions remove the two replaced channels. Positivity follows from the
remaining positive fields plus the positive coupled system, not from treating
the displayed difference as an independent positive addition.

## 6. The eighth-power residual is nonzero

The next coupled moment is

\[
m_4^{(2)}=c_0\left[(\mu^2+\beta^2)^2+
\beta^2(\mu+\nu)^2\right].
\]

Define \(d_8=m_4^{(2)}-t_4\). Exact algebra gives

\[
d_8(q)=-\frac{(q-1)P_5(q-1)}{2996494663680\,\beta^2}<0
\qquad(q>1),
\]

where all coefficients of the following polynomial are positive:

\[
\begin{aligned}
P_5(z)={}&25088675512320+117564089389056z
+220378871447424z^2\\
&+206578537972416z^3+96833156436946z^4
+18158086308041z^5.
\end{aligned}
\]

The two-field residual therefore satisfies

\[
\rho_2(\tau)=\frac{d_8(q(\tau))}{\tau^8}+O(\tau^{-10}).
\]

The first three moments fix \(\mu,\beta^2,\nu\) in a two-dimensional
cyclic mass realization, so its fourth moment is already determined. This is
why another two-field matrix in this same class cannot also match the fourth
coefficient. The statement assumes the fixed total observable strength and the
frequency form \(sI+\mathcal M(q)\).

## 7. A third field cancels the fourth coefficient

Let \(d=\det\mathcal M_2>0\), and set

\[
\chi^2=-\frac{d_8}{c_0\beta^2}\geq0,
\qquad \eta=q+\frac{\chi^2\mu}{d}.
\]

Define the three-field mass matrix

\[
\mathcal M_3(q)=
\begin{pmatrix}
\mu&\beta&0\\
\beta&\nu&\chi\\
0&\chi&\eta
\end{pmatrix}.
\]

Its Schur complement over \(\mathcal M_2\) is
\(\eta-\chi^2\mu/d=q>0\). Hence it is positive for all \(q\geq1\).
At \(q=1\), \(\chi=0\); the added oscillator decouples and does not
change the original two-channel response.

The full covariance is

\[
\boxed{
\mathcal T_3(s,q)=
\frac{c_0s[(s+\nu)(s+\eta)-\chi^2]}
{(s+\mu)[(s+\nu)(s+\eta)-\chi^2]-\beta^2(s+\eta)}.}
\]

The first three moments are unchanged, while

\[
m_4^{(3)}=m_4^{(2)}+c_0\beta^2\chi^2=t_4.
\]

Replacing the original pair by this positive system cancels all four leading
inverse powers. This adds one auxiliary field to the coupled pair; the higher
original gamma channels remain untouched.

The next coefficient is still strictly nonzero. Define the shifted moment
matrix

\[
\mathcal H_1(q)=
\begin{pmatrix}
t_1&t_2&t_3\\t_2&t_3&t_4\\t_3&t_4&t_5
\end{pmatrix}.
\]

The sign calculation in the next section gives \(\det\mathcal H_1<0\).
For the chosen \(\eta\), the tenth-power residual coefficient is

\[
\boxed{
d_{10}(q)=\frac{\det\mathcal H_1(q)}{c_0^2\Delta(q)}+q\,d_8(q)<0
\qquad(q>1).}
\]

To derive this formula, increasing the third diagonal entry changes the fifth
moment by \(c_0\beta^2\chi^2\) times that increase, with the first four
moments fixed. For a three-dimensional cyclic realization,
\(\det\mathcal H_1=c_0^3\beta^4\chi^2\det\mathcal M_3\).
Our positive choice has \(\det\mathcal M_3=dq\), while the hypothetical
choice matching \(t_5\) has determinant \(\det\mathcal H_1/
(c_0^3\beta^4\chi^2)\). Subtracting their fifth moments gives the formula
above. The formulas extend continuously to \(q=1\).

Thus

\[
\rho_3(\tau)=\frac{d_{10}(q(\tau))}{\tau^{10}}+O(\tau^{-12}).
\]

## 8. Why more positive masses cannot match all five conditions

For any positive finite-dimensional mass matrix \(\mathcal M\), any
observable vector \(b\), and moments \(m_j=b^*\mathcal M^jb\), the
matrix \((m_{i+j+1})_{i,j=0}^2\) is positive semidefinite. Indeed, for
\(p(t)=u_0+u_1t+u_2t^2\),

\[
\sum_{i,j=0}^2\overline{u_i}m_{i+j+1}u_j
=\|\mathcal M^{1/2}p(\mathcal M)b\|^2\geq0.
\]

The same conclusion holds for a positive spectral measure with the requisite
finite moments. It does not depend on the number of auxiliary fields.

But the required moments satisfy the exact identity

\[
\det\mathcal H_1(q)
=-\frac{(q-1)P_8(q-1)}{2307300891033600}<0\qquad(q>1),
\]

where

\[
\begin{aligned}
P_8(z)={}&487589611674009600
+3448095090231214080z\\
&+10688033459782287360z^2
+18978552455244742656z^3\\
&+21129142239284465664z^4
+15113209891689105408z^5\\
&+6787293707867872896z^6
+1751016271770907632z^7\\
&+198814690954739017z^8.
\end{aligned}
\]

Every coefficient is positive, so the sign holds throughout the required
one-prime regime. This excludes cancellation of the first five whole-phase
coefficients by **any positive mass realization of this class replacing only
the first two original gamma channels**. The class has frequency operator
\(sI+\mathcal M(q)\), a derivative observable with fixed total weight
\(c_0\), and no further dependence on \(s\) beyond the displayed term.

This is not a prohibition on quantum completions. It does not cover changing
more of the original gamma tower, changing the observable's frequency
dependence, another dispersion law, or interacting ground states outside this
resolvent form. Whole-phase moment matching is also stronger than an arbitrary
finite-interval kernel identity. For the explicit candidates above, however,
the surviving diagonal jumps establish failure of the actual interval identity,
as explained next.

## 9. The remaining error is an interval obstruction, not just a formal tail

For the one-prime function \(q(\theta)>1\), the coefficients \(d_8(q(\theta))\)
and \(d_{10}(q(\theta))\) are real analytic periodic functions with strictly
negative means. Their Fourier coefficients decay exponentially. All expansions
above are uniform over that fixed compact phase range.

For an inverse-power term \(h(\ell\tau)/\tau^{2n}\), subtract
\(h(\ell\tau)/(1+\tau^2)^n\). The improved remainder has enough
integrable Fourier moments to make its inverse transform \(C^{2n}\).
The inverse transform of \((1+\tau^2)^{-n}\) is \(C^{2n-2}\), and its
\((2n-1)\)-st derivative has jump \((-1)^n\) at zero. This follows
by applying \((1-\partial_x^2)^n\) to its fundamental solution.

Consequently the two-field residual kernel is \(C^6\) and has a seventh
derivative jump equal to the mean of \(d_8\), which is negative. The three-field
kernel is \(C^8\) and has a ninth derivative jump equal to minus the mean
of \(d_{10}\), hence positive. Translated jumps occur at the return lengths.

These are nonzero diagonal jumps on every nonempty open input interval.
Columns of the difference kernel have their jumps at different positions;
choosing arbitrarily many distinct column positions inside a subinterval
shorter than \(\ell\) proves their linear independence. Thus both
compressed residuals have infinite rank. Smooth pole terms or a net finite-rank
boundary correction cannot complete either fixed model to the full target.

The changes in the total response are bounded and \(O(\tau^{-2})\), so
the original contact and prime delta coefficients are preserved. The improved
remainders are continuous kernels. The original logarithmic form domain also
remains unchanged: only finitely many bounded channel responses were replaced.

## 10. What is quantum about the construction, and what is not

These are actual canonical quantum models with a vacuum and a calculated
correlation observable. They do not require imposing an individual boundary
profile on the ground state. An input enters only when the observable is
smeared. Positive cross correlations between the coupled fields permit a
redistribution of spectral weights that is absent from the manuscript's
independent convex splitting family.

The arithmetic coupling is nevertheless prescribed. The operator
\(\mathcal M(q(D))\) is spatially nonlocal, because \(q\) contains the
prime-return data and the matrix entries involve rational functions and square
roots of those data. We have not derived this coupling from a local transport
law, a Ward identity, or a topological invariant. The square roots here belong
to explicitly proved positive field matrices, not to the unknown Weil form.

There is also an exact classical counterpart. For a positive matrix multiplier
\(\mathcal M\) commuting with \(A\), the energy

\[
\mathcal E[F,u]=c_0\|F e_1-u\|^2+
c_0\|\mathcal M^{-1/2}\partial_xu\|^2
\]

has minimized response
\(c_0s\,e_1^T(sI+\mathcal M)^{-1}e_1\). Positive upper and lower
bounds on the matrix at fixed cutoff give the standard closed form and unique
minimizer on the whole line. Hence the new covariances also solve explicit
coupled classical response problems. The quantum perspective suggested a
productive class of couplings, but these calculations do not demonstrate an
advantage exclusive to quantization.

An optional quantum SUSY completion pairs each bosonic mode of frequency
\(\nu\) with a fermionic mode of the same frequency. On the finite-mode
core, \(\mathcal Q=\sum_j\sqrt{\nu_j}\,c_j^\dagger a_j\) obeys
\(\mathcal Q^2=0\) and
\(\{\mathcal Q,\mathcal Q^\dagger\}=\sum_j\nu_j(a_j^\dagger a_j+
c_j^\dagger c_j)\). The common vacuum has zero energy and the bosonic
correlator is unchanged. This standard pairing supplies no new arithmetic
constraint or protected correlation identity. See
[Tong, “Supersymmetric Quantum Mechanics”](https://www.damtp.cam.ac.uk/user/tong/susy/susyqm.pdf)
for the positive algebra and ground-state interpretation.

For a full quantum proposal, vacuum subtraction or supersymmetry alone still
does not identify a correlation with the Weil kernel. The full pole correction,
regular kernel, and compatibility across unbounded interval lengths remain to
be established. A single realization on ordinary whole-line \(L^2\) also
faces the closability restriction discussed in the preceding operator note;
the finite-interval family should be retained.

## 11. Reproducible checks and their limits

The accompanying [calculation](../../numerics/check_quantum_covariance.py) and
[record](../../numerics/records/quantum-covariance-diagnostics.json) contain:

- Exact rational derivation of the digamma coefficients and moment identities.
- Positive coefficient certificates for the two-field matrix and exact negative
  coefficient certificates for \(d_8\) and the shifted moment determinant.
- The three-field positive Schur complement and the derived sign of \(d_{10}\).
- Normal-mode covariance and uncertainty-product controls for both coupled
  systems, including the large \(q\) values of the arithmetic one-prime model.
- Eighty-digit evaluations of the digamma residual, with two recurrence and
  asymptotic settings, confirming the eighth- and tenth-power asymptotics for
  fixed \(q=2,10,10^6\). These are scalar response controls, not a Weil
  eigenvalue calculation or an interval sign certificate.

The rational sign certificates are exact polynomial calculations. Numerical
covariance agreement and high-precision asymptotic agreement remain diagnostics;
their truncation and rounding errors are not enclosed by interval arithmetic.
The proofs of the quantum response, domain coverage, and kernel jumps are the
analytic arguments given above, not consequences of a finite sample of inputs.

The new calculation is separate from the four historical replay jobs. No
previous numerical program, diagnostic record, manuscript source, or PDF was
modified for this investigation.

## 12. What the next quantum investigation must change

The first quantum pass reaches a positive covariance with four canceled leading
errors and a precise obstruction to continuing within its fixed mass class.
Adding more unobserved positive masses while keeping only the first two
original channels replaced cannot satisfy the fifth matching condition.

The next choices have concrete mathematical differences:

1. Replace a larger part of the original gamma tower and recompute its required
   moment matrices before designing a covariance. The obstruction polynomial
   above depends on the two selected original masses.
2. Change the observable or the frequency operator beyond
   \(sI+\mathcal M(q)\). Calculate the entire ground-state covariance,
   including any new contact terms, before using its high-frequency expansion.
3. Specify an interacting ground-state model whose two-point kernel has an
   independently controlled positivity and symmetry structure. The present
   spatial resolvent moment restriction need not apply, but exact arithmetic
   matching remains a separate obligation.

The tests should continue to distinguish asymptotic matching, exact interval
kernel matching, and an operator inequality establishing positivity. This
investigation improves the first and supplies failures of the second for its
explicit models. It does not establish the third.
