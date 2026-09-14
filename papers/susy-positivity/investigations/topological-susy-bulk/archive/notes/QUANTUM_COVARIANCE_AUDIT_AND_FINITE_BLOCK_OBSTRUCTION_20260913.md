# Quantum covariance audit and an obstruction for every finite replaced block

Date: 13 September 2026.

This is an independent audit and continuation of
[Quantum ground-state correlations](QUANTUM_GROUND_STATE_CORRELATIONS_20260913.md)
and the [operator discussion](OPERATOR_PERSPECTIVE_20260913.md).
It uses the current checkout, including those uncommitted notes. The manuscript,
background, prior programs, and historical records are preserved.

The previous two- and three-field response formulas, positivity certificates,
moment obstruction, and residual jump signs check out. Two qualifications matter:
positive covariance means a positive quadratic form, not positive off-diagonal
correlations; and a finite-regulator displacement identity is not a theorem that
the infinitely displaced vacuum belongs to the original Fock space.

The new result is a finite-block obstruction, with two different scopes.

- At every fixed \(q>1\), replacing any \(N\) original channels by a positive
  resolvent covariance cannot match the first \(2N+1\) residual coefficients.
  An explicit polynomial gives a negative shifted moment quadratic form,
  regardless of the number of replacement masses.
- For the one-prime \(q(\theta)>1\), every finite-dimensional positive mass
  matrix analytic in the phase, with the stipulated dispersion and observable,
  leaves an infinite-rank interval residual. This second assertion does not
  assume full phase matching; a separate diagonal argument proves it.

For the first three and four channels, exact moment matrices also show that six
and eight matches, respectively, are attainable by positive Gaussian models.
Their next errors have strictly negative coefficients and nonzero diagonal
jumps. Thus larger finite blocks postpone the failure within this class. They
provide neither an exact Weil covariance nor a bound proving Weil positivity.

The new [program](../../numerics/check_quantum_block_obstruction.py) and
[record](../../numerics/records/quantum-block-obstruction-diagnostics-20260913.json)
contain independent exact calculations and separate floating-point controls.
The proofs below supply the all-parameter and all-input conclusions.

## 1. The complete target and the domain

Use \(I_L=(-L/2,L/2)\), \(\mathcal H_L=L^2(I_L)\), zero extension
\(E_L:\mathcal H_L\to L^2(\mathbb R)\), and
\(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\). Inner products are
conjugate-linear in their first argument. On the whole line,

\[
D=-i\partial_x,\quad A=D^2,\quad
\operatorname{Dom}D=H^1(\mathbb R),\quad
\operatorname{Dom}A=H^2(\mathbb R).
\]

Write

\[
a_k=2k+\tfrac12,\qquad
B(s)=\sum_{k\ge0}\frac2{a_k}\frac{s}{s+a_k^2}
=\operatorname{Re}\psi(\tfrac14+i\sqrt{s}/2)-\psi(\tfrac14),
\]

\[
w_0=\psi(\tfrac14)-\log\pi
=-\gamma_E-\pi/2-3\log2-\log\pi.
\]

For \(F=E_Lf\), put

\[
K[F]=\frac1{2\pi}\int B(\tau^2)|\widehat F(\tau)|^2\,d\tau,\qquad
C(f)=\int_{I_L}f(x)\cosh(x/2)\,dx,\quad
S(f)=\int_{I_L}f(x)\sinh(x/2)\,dx.
\]

With \(T_af=(E_Lf)(\,\cdot-a)|_{I_L}\), the entire target is

\[
\boxed{
Q_{0,L}[f]=K[F]+w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2
-\sum_{\substack{p\ {\rm prime},\,m\ge1\\m\log p<L}}
\frac{\log p}{p^{m/2}}\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle .
}
\]

In particular, a cosine has coefficient \(-2(\log p)p^{-m/2}\);
each of its two translations has coefficient \(-(\log p)p^{-m/2}\).
The pole kernel is \(2\cosh((x-y)/2)\), of rank two on a nonempty interval,
with one positive and one negative direction.

The closed form domain is

\[
\mathcal D_{\log,L}
=\{f\in L^2(I_L):\int\log(2+|\tau|)|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\}.
\]

Indeed \(B(\tau^2)-\log(2+|\tau|)\) is bounded, and all other displayed
terms are bounded forms at fixed \(L\). Closedness and semiboundedness do not
assert nonnegativity. The operator denoted \(E_L^*B(A)E_L\) is the operator
associated with its compressed form, namely
\((B(A)^{1/2}E_L)^*(B(A)^{1/2}E_L)\). It is not \(B\) of an arbitrarily
chosen interval Laplacian. Zero extension of the input does not confine the
auxiliary fields or discard their exterior tails.

These definitions agree with “The arithmetic form and its input space” in the
[background](../../../../background_section.tex). The digamma partial fractions
used for the tower are given in [NIST DLMF, Series Expansions](https://dlmf.nist.gov/5.7#E6).

## 2. Audit: source-dependent energies under quantization

At a finite regulator, complete the classical square:

\[
\mathcal E[f,u]=Z[f]+\tfrac12(u-u_f)^TA(u-u_f),\qquad A>0.
\]

Add a source-independent kinetic energy \(\tfrac12p^TM^{-1}p\), \(M>0\).
Translation in configuration space is unitary and shifts the oscillator center
without changing the eigenfrequencies, the square roots of the eigenvalues of
\(M^{-1/2}AM^{-1/2}\). Therefore

\[
E_0[f]=Z[f]+\tfrac12\operatorname{tr}
(M^{-1/2}AM^{-1/2})^{1/2},\qquad
E_0[f]-E_0[0]=Z[f]-Z[0].
\]

Here \(Z[0]=0\). For complex sources one may apply the real oscillator
calculation to real and imaginary parts. The source difference is exactly the
classical minimum. Zero-point cancellation does not correct its residual.
The basic oscillator formulas follow directly from
\(a=(\sqrt{\nu}\phi+i\pi/\sqrt{\nu})/\sqrt2\); the standard canonical
conventions are reviewed in [Tong, Free Fields](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S2.html).

There is an additional infinite-tower issue that should not be hidden by that
finite-regulator statement. For unit kinetic mass in the unmodified gamma
channel, the classical energy is

\[
\frac2a(\|F-u\|^2+a^{-2}\|u'\|^2),\qquad
\widehat u_f=(1+\tau^2/a^2)^{-1}\widehat F.
\]

The fluctuation frequency is
\(\nu_a(\tau)=2a^{-1/2}(1+\tau^2/a^2)^{1/2}\). The coherent displacement
amplitude has squared norm

\[
\|\alpha_a\|^2=\frac1{2\pi}\int
a^{-1/2}(1+\tau^2/a^2)^{-3/2}|\widehat F(\tau)|^2\,d\tau.
\]

For every nonzero \(F\in L^2\), a bounded frequency interval carries positive
Fourier mass. Its contribution to the sum over large \(a=a_k\) is bounded below
by a positive multiple of \(\sum_k a_k^{-1/2}=\infty\).
Thus the displaced vacuum is not a vector in the original tower Fock space for
this kinetic choice. To see the issue directly, the overlap between two cutoff
coherent vacua is the exponential of minus half the squared displacement in the
added modes. The normalized cutoff vacua are not Cauchy when that sum diverges.

The finite-cutoff energy differences still converge to the classical tower
response on \(\mathcal D_{\log,L}\); this follows from the nonnegative channel
sum. That numerical limit does not construct an infinitely displaced
ground-state vector or an unrenormalized source Hamiltonian. Other kinetic
weights or representations require their own construction. The preceding
note explicitly began with a finite regulator; its energy calculation is
correct at that scope. An unqualified same-Fock-space continuum reading is not.

## 3. Audit: a genuine vacuum covariance for the kinetic gamma term

The covariance formulation avoids source displacement. There is a real
canonical field \((\phi_a,\pi_a)\) for each channel, and a new real evolution
variable \(t_{\rm phys}\). This time is different from the spatial variable
\(x\), its Fourier dual \(\tau\), the zeta shift, and the old loop coupling.

Take the one-particle frequency operator
\(h_a=A+a^2\) and the vacuum-subtracted Hamiltonian \(d\Gamma(h_a)\).
Its formal classical Hamiltonian is

\[
H_a=\tfrac12(\|\pi_a\|^2+\|h_a\phi_a\|^2).
\]

The coordinate form domain is \(H^2\); its squared-frequency operator is
\(h_a^2\). The dispersion is \(\nu_a(\tau)=\tau^2+a^2\), not the
relativistic square root. Canonical quantization gives covariance
\((2h_a)^{-1}\). Consequently

\[
\mathcal O_a(x)=\frac2{\sqrt a}\partial_x\phi_a(x),\qquad
\langle\mathcal O_a(f)^\dagger\mathcal O_a(f)\rangle
=\frac1{2\pi}\int\frac2a\frac{\tau^2}{\tau^2+a^2}|\widehat F|^2\,d\tau.
\]

For a real smearing this is a Segal field; complex smearing means its complex
linear extension. Acting on the vacuum gives a one-particle amplitude with
modulus \(\sqrt{2/a}\,|\tau|(\tau^2+a^2)^{-1/2}|\widehat F|\);
the sign of its imaginary phase does not affect the pairing.

The direct sum of these amplitudes is square summable exactly on
\(\mathcal D_{\log,L}\). This follows from the positive tower identity and
the logarithmic growth of \(B\). The corresponding field is defined on the
finite-particle core for each such smearing and in particular acts on the
vacuum. Its squared vacuum norm is \(K[F]\), and polarization gives every
sesquilinear pairing. The source \(f\) labels an observable, not a different
vacuum. No divergent sum of zero-point energies or raw source vectors is used.

This verifies the gamma covariance claim on the full stated form domain.
It realizes \(K\), not the complete gamma form \(K+w_0\|f\|^2+P[f]\),
and still less the complete arithmetic target.

## 4. The loop covariance and the exact discrepancy

For the concrete continuation fix \(\ell=\log2\), \(r=2^{-1/2}\), and

\[
v(\theta)=w_0-2\ell\sum_{m\ge1}r^m\cos(m\theta),\qquad
q(\theta)=e^{-2v(\theta)}.
\]

Insert \(\theta=\ell\tau\). Both functions are real analytic, even and periodic.
They have fixed finite bounds. Also

\[
v(\theta)\le w_0+\frac{2\ell r}{1+r}<-2,
\]

using \(w_0<-3\), \(2r/(1+r)<1\), and \(\log2<1\).
Thus \(q_{\min}>e^4>2\). No sampled phase values are needed for this bound.

The frequency \(h_{a,q}=A+a^2q(\ell D)\), with the same observable,
gives \(T_a(s,q)=(2/a)s/(s+a^2q)\). The total positive response is
\(B(s/q)\). All primitive histories stay in \(q\), including histories whose
direct interval translation vanishes. For \(\log2<L\le\log3\), this covers
all active prime terms. The exact residual is

\[
\rho(\tau)=B(\tau^2/q(\ell\tau))-B(\tau^2)+\tfrac12\log q(\ell\tau).
\]

Let \(Z_L\) be its positive covariance response and
\(\mathsf R_L=E_L^*\rho(D)E_L\). Then, as forms,

\[
\boxed{\mathsf W_L=\mathsf Z_L+\mathsf P_L-\mathsf R_L.}
\]

Since \(-\tfrac12\log q=v\), this identity retains the constant, all active
prime coefficients, both pole amplitudes, and the full regular residual with
the stated signs. A new finite block below changes \(\rho\) to the exactly
defined \(\rho_N\); the same identity continues to hold.

## 5. Audit of the two- and three-field algebra

A block of positive masses \(\mathcal M(q)\), with frequency
\(h=AI+\mathcal M(q(\ell D))\), and observable
\(\sqrt{2c_0}\partial_x\phi_1\) gives

\[
\mathcal T(s,q)=c_0s\,e_1^T(sI+\mathcal M(q))^{-1}e_1.
\]

For fixed \(q\), define \(m_j=c_0e_1^T\mathcal M^je_1\).
The high-frequency expansion is
\(\mathcal T=c_0+\sum_{j\ge1}(-1)^jm_js^{-j}\) in the asymptotic sense.
Replacing masses \(a_0,a_1\) gives original moments

\[
(c_0,\ldots,c_5)=
(24/5,6,63/2,1563/8,39063/32,976563/128).
\]

If \(b_j\) is the coefficient of \(\tau^{-2j}\) in \(B(\tau^2)\), cancellation
requires

\[
t_j=c_jq^j+(-1)^{j+1}b_j(q^j-1),\qquad
\text{residual coefficient }d_j=(-1)^j(m_j-t_j).
\]

This sign convention is useful: at an odd order \(d_j=t_j-m_j\).
Independent expansion of
\(j(x)=e^{-x/2}/(1-e^{-2x})\), using
\(B(\tau^2)=2\int_0^\infty j(x)(1-\cos(\tau x))\,dx\), gives

\[
(b_1,\ldots,b_5)=(-1/24,-7/960,-31/8064,-127/30720,-511/67584).
\]

The program divides the Taylor series of
\(xj(x)=e^{-x/2}/((1-e^{-2x})/x)\) using rational arithmetic.
If its coefficient of \(x^{2j}\) is \(g_{2j}\), then
\(b_j=2(-1)^{j+1}(2j-1)!g_{2j}\). This is an independent coefficient
calculation, rather than importing the previous Bernoulli-polynomial routine.
For example the odd Taylor term of \(j\) is the inverse transform singularity
of \(b_j\tau^{-2j}\), which gives precisely this factorial and sign.

Set

\[
\mu=t_1/c_0,\quad \beta^2=t_2/c_0-\mu^2,\quad
N_3=t_3/c_0-\mu^3-2\mu\beta^2,\quad \nu=N_3/\beta^2,\quad
\Delta=\mu N_3-\beta^4 .
\]

The matrix and its complete response are

\[
\mathcal M_2=\begin{pmatrix}\mu&\beta\\\beta&\nu\end{pmatrix},\qquad
\mathcal T_2=\frac{c_0s(s+\nu)}{(s+\mu)(s+\nu)-\beta^2}.
\]

Expansion or multiplication gives the first three moments \(t_1,t_2,t_3\).
The coefficients of \(\mu,\beta^2,\Delta\) in \(q-1\) are positive;
\(\det\mathcal M_2=\Delta/\beta^2>0\).
The audit recomputes and exactly agrees with the old rational certificates.
An independent route is through Gram determinants:

\[
\det\begin{pmatrix}t_0&t_1\\t_1&t_2\end{pmatrix}=c_0^2\beta^2,\quad
\det\begin{pmatrix}t_1&t_2\\t_2&t_3\end{pmatrix}=c_0^2\Delta,\quad
\det(t_{i+j})_{i,j=0}^2=-c_0^2\beta^2 d_8 .
\]

Here \(d_8=m_4^{(2)}-t_4\), named by its inverse power as in the old note.
The third determinant is positive for \(q>1\), so \(d_8<0\).
The new determinant calculation reproduces every coefficient of the old
polynomial \(P_5\) and its denominator.

Let \(d=\det\mathcal M_2\), \(\chi^2=-d_8/(c_0\beta^2)\), and
\(\eta=q+\chi^2\mu/d\). Then

\[
\mathcal M_3=
\begin{pmatrix}\mu&\beta&0\\\beta&\nu&\chi\\0&\chi&\eta\end{pmatrix}
\]

has Schur complement \(q>0\). Its first four moments match, because
\(m_4^{(3)}=m_4^{(2)}+c_0\beta^2\chi^2=t_4\). Cofactor inversion gives

\[
\mathcal T_3=
\frac{c_0s[(s+\nu)(s+\eta)-\chi^2]}
{(s+\mu)[(s+\nu)(s+\eta)-\chi^2]-\beta^2(s+\eta)}.
\]

For \(\mathcal H_1=(t_{i+j+1})_{i,j=0}^2\), the required fifth moment
has \(\det\mathcal H_1<0\). The audit independently reproduces the complete
old \(P_8\) certificate and obtains

\[
d_{10}=t_5-m_5^{(3)}
=\frac{\det\mathcal H_1}{c_0^2\Delta}+q\,d_8<0.
\]

One way to verify this identity is to vary the last Jacobi diagonal entry.
Only the fifth and higher moments change; the fifth changes at rate
\(c_0\beta^2\chi^2\). At the zero Schur complement its shifted Gram
determinant vanishes. Increasing that complement to \(q\) adds
\(-q\,d_8\) to the fifth moment. This proves the formula with its minus sign
for the odd residual order. At \(q=1\), both added corrections vanish and
the pair response is exactly the original two channels for every \(s\).

**Correction to the previous physical prose.** For the displayed \(\beta>0\),

\[
\langle\phi_1\phi_2\rangle_s
=-\frac{\beta}{2[(s+\mu)(s+\nu)-\beta^2]}<0 .
\]

Thus the statement about “positive cross correlations” in the earlier note is
not literally correct for its own field convention. The covariance matrix is
positive as a quadratic form; individual off-diagonal entries need not be
positive, and reversing one field changes their signs. The mechanism is coupled
spectral-weight redistribution. No formula or positivity certificate needs
changing. This correction is recorded here while preserving the earlier note.

## 6. The gamma coefficients at every order

For each fixed truncation order, the digamma expansion yields

\[
B(\tau^2)=\log|\tau|-\log2-\psi(1/4)
+\sum_{j=1}^J b_j\tau^{-2j}+O(|\tau|^{-2J-2}),
\]

\[
b_j=\frac{(-1)^{j+1}2^{2j}}{2j}\,\mathrm B_{2j}(1/4),
\]

where \(\mathrm B_n(x)\) denotes a Bernoulli polynomial. This follows by
expanding the shifted argument in the
[DLMF digamma asymptotic](https://dlmf.nist.gov/5.11#E2); the imaginary axis
remains inside a sector separated from the negative real axis.

The Bernoulli Fourier series at \(1/4\) gives the useful exact sign formula

\[
\boxed{
b_j=-A_j,\qquad
A_j=\frac{2(2j-1)!}{(2\pi)^{2j}}\,
\eta_{\rm D}(2j)>0,\qquad
\eta_{\rm D}(z)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n^z}.
}
\]

Indeed \(\cos(n\pi/2)\) is zero for odd \(n\); summing even \(n\) gives
\(-2^{-2j}\eta_{\rm D}(2j)\). Substitution in the
[DLMF Bernoulli Fourier formula](https://dlmf.nist.gov/24.8#E1)
gives the displayed constants. In particular all \(b_j\), not just the first
five, are negative.

An equivalent integral is

\[
A_j=2\int_0^\infty\frac{x^{2j-1}}{e^{2\pi x}+1}\,dx .
\]

It follows by expanding the denominator into exponentials; the integrated
absolute series converges for \(2j\ge2\). See also the standard
[DLMF integral representation](https://dlmf.nist.gov/25.5#E3).
Neither formula uses zero ordinates. These coefficients grow factorially;
the asymptotic expansion is not a convergent moment series for the gamma tower.
The divergent raw gamma moments must never be obtained by termwise expansion
of the entire infinite channel sum.

## 7. Required moment matrices for a larger replaced block

Replace \(a_0,\ldots,a_{N-1}\) and retain every higher loop channel. Define

\[
c_j^{(N)}=\sum_{k<N}\frac2{a_k}(a_k^2)^j,\qquad
t_0=c_0^{(N)},\qquad
t_j=c_j^{(N)}q^j+(-1)^j A_j(q^j-1)\quad(j\ge1).
\]

The exact total response and discrepancy, for any proposed replacement
\(\mathcal T_N\), are

\[
Z_N(s,q)=B(s/q)-\sum_{k<N}\frac2{a_k}\frac{s}{s+a_k^2q}
+\mathcal T_N(s,q),\qquad
\rho_N=Z_N-B(s)+\tfrac12\log q .
\]

For a positive mass matrix and a fixed observable vector of squared norm
\(c_0^{(N)}\), its moments obey both Hankel positivity conditions:

\[
H_0^{(n)}=(m_{i+j})_{i,j=0}^n\ge0,\qquad
H_1^{(n)}=(m_{i+j+1})_{i,j=0}^n\ge0 .
\]

For a polynomial \(p\), these are respectively
\(\|p(\mathcal M)b\|^2\) and
\(\|\mathcal M^{1/2}p(\mathcal M)b\|^2\).
This necessity also applies to an infinite positive spectral measure when the
displayed moments exist. It requires neither a discretized Weil operator nor
any claim about the sign of \(Q_{0,L}\).

Exact rational calculations for \(N=1,2,3,4\) give the following table.
“Matches” means the number of consecutive coefficients that can be canceled
at every \(q>1\) within this class.

| Replaced original channels \(N\) | \(c_0^{(N)}\) | Attainable matches | First impossible match | Fields in one positive construction |
| --- | --- | --- | --- | --- |
| 1 | \(4\) | 2 | 3 | 2 |
| 2 | \(24/5\) | 4 | 5 | 3 |
| 3 | \(236/45\) | 6 | 7 | 4 |
| 4 | \(3248/585\) | 8 | 9 | 5 |

For each of these blocks all leading minors of \(H_0^{(N)}\) are positive
for \(q>1\). All leading minors of \(H_1^{(N-1)}\) are positive as well,
while \(\det H_1^{(N)}<0\).
The certificate is elementary: write each determinant in \(z=q-1\).
Every coefficient of each smaller minor is positive.
For the final unshifted minor the constant coefficient is zero and all remaining
coefficients are positive. For the final shifted minor the constant coefficient
is zero and all remaining coefficients are negative. The record lists the
entire rational polynomials, rather than sampled determinants.

For the new blocks \(N=3,4\), the final unshifted determinants have degrees
12 and 20; the final shifted determinants have degrees 16 and 25.
Their respective coefficients of \(q-1\) are

\[
\begin{array}{c|cc}
N & \det H_0^{(N)} & \det H_1^{(N)}\\ \hline
3 & 422387910378/143 & -10026896947200/143\\
4 & 5343948424214031642595200/2873
  & -626139463613291566202880000/323 .
\end{array}
\]

These coefficients alone would not prove global signs; the all-coefficient
certificates do. The next section explains why a negative direction exists
for every finite \(N\), without extrapolating this table.

## 8. A negative shifted moment direction for every finite block

**Proposition.** Fix \(q>1\) and any \(N\) distinct positive original masses,
with their positive channel weights. The required moments above cannot be the
first \(2N+1\) moments of any positive mass spectral measure.

**Proof.** Let

\[
p_1(t)=\prod_{k<N}(t-a_k^2)=\sum_{i=0}^Nv_it^i,\qquad
p_q(t)=q^Np_1(t/q)=\sum_{i=0}^Nv_iq^{N-i}t^i .
\]

The original positive atoms at \(qa_k^2\) contribute zero to the shifted
quadratic form of \(p_q\). Also
\(v_i=(-1)^{N-i}|v_i|\), since every root is positive. Therefore its required
value is exactly

\[
\begin{aligned}
\mathcal L_q(t\,p_q(t)^2)
&=\sum_{i,j=0}^N v_iv_jq^{2N-i-j}\,t_{i+j+1}\\
&=-\sum_{i,j=0}^N|v_iv_j|A_{i+j+1}
\left(q^{2N+1}-q^{2N-i-j}\right)<0 .
\end{aligned}
\]

Every summand after the minus sign is strictly positive. But a positive mass
measure would give \(\int t\,p_q(t)^2\,d\mu(t)\ge0\).
This proves the obstruction, independent of the number of replacement fields.
The program checks this polynomial identity separately from the determinant
calculation for \(N=1,2,3,4\). The proof covers every finite \(N\). \(\square\)

There is a useful interpretation of the same calculation. Set

\[
d\sigma_q(\lambda)=
\frac{(e^{2\pi\sqrt{\lambda/q}}+1)^{-1}
-(e^{2\pi\sqrt\lambda}+1)^{-1}}{\lambda}\,d\lambda,\qquad \lambda>0 .
\]

This is a positive finite measure for \(q>1\), with
\(\int\lambda^j\,d\sigma_q=A_j(q^j-1)\) for \(j\ge1\).
Its total mass is \(\frac12\log q\), as follows by substituting
\(\lambda=x^2\) and differentiating the scale in the integral.
For positive moments, the target correction is thus the moment sequence of
this measure placed at **negative** mass squared \(t=-\lambda\).
For \(t_0\) as well, its formal signed representation includes
\(-\frac12\log q\,\delta_0\). The atom at zero drops out of the shifted test.

More explicitly,

\[
\mathcal L_q(t\,p(t)^2)
=\sum_{k<N}\frac2{a_k}\,qa_k^2\,p(qa_k^2)^2
-\int_0^\infty\lambda\,p(-\lambda)^2\,d\sigma_q(\lambda).
\]

This representation describes necessary asymptotic moments. It is not a
proposed stable Hamiltonian or a convergent spectral representation of the
whole target. Introducing negative masses into the frequency \(sI+\mathcal M\)
would leave the stipulated positive class; squaring that frequency in the
classical Hamiltonian would make the actual quantum frequency its absolute
value, changing the covariance.

## 9. Positive larger-block models and what their improvements accomplish

The table's attainability statement follows constructively, without assuming a
general moment-extension theorem. Fix \(N=3\) or \(4\) and \(q>1\).
Apply Gram–Schmidt to \(1,t,\ldots,t^N\) with inner product
\(\mathcal L_q(\overline p r)\), using the required moments through \(t_{2N}\).
The positive \(H_0^{(N)}\) makes all polynomial norms positive.

In the orthonormal basis \(p_0,\ldots,p_N\), multiplication by \(t\) determines
the first \(N\) diagonal entries \(\alpha_0,\ldots,\alpha_{N-1}\) and all
positive adjacent entries \(\beta_1,\ldots,\beta_N\) of a Jacobi matrix.
Tridiagonality follows from polynomial degree and orthogonality.
The upper \(N\)-dimensional matrix \(J_N\) is positive definite, since its
quadratic form is \(\mathcal L_q(t|p|^2)\) for \(\deg p<N\), represented
by the positive \(H_1^{(N-1)}\).

Choose the remaining diagonal entry by

\[
\alpha_N=q+\beta_N^2(J_N^{-1})_{N,N},\qquad
\mathcal M_{N+1}=
\begin{pmatrix}J_N&\beta_N e_N\\\beta_Ne_N^T&\alpha_N\end{pmatrix}>0 .
\]

Its Schur complement is \(q\). The observable is the first coordinate of
strength \(\sqrt{2c_0^{(N)}}\). This specifies the complete frequency and
observable before evaluating their response:

\[
\boxed{
\mathcal T_N(s,q)=c_0^{(N)}s\,
\frac{\det(sI+\mathcal M_{N+1})_{\widehat0,\widehat0}}
{\det(sI+\mathcal M_{N+1})}.
}
\]

Here the numerator determinant deletes row and column zero. Equivalently,
this is the explicit finite continued fraction

\[
\mathcal T_N(s,q)=
\frac{c_0^{(N)}s}{s+\alpha_0-
\dfrac{\beta_1^2}{s+\alpha_1-
\dfrac{\beta_2^2}{\ddots-
\dfrac{\beta_N^2}{s+\alpha_N}}}} .
\]

The coefficients are fixed by the finite Gram procedure just given, not by an
unknown square root of the target. The reproducible code uses mass divided by
\(q\) and normalized moments \(t_j/q^j\), then multiplies back by \(q\);
its last scaled Schur complement is one.

To verify matching through \(2N\), powers of the Jacobi matrix acting on its
first basis vector reproduce multiplication by \(t\) on degrees up to \(N\).
For \(j\le2N\), write \(j=u+v\) with \(u,v\le N\) and use
\(\langle\mathcal M^ue_0,\mathcal M^ve_0\rangle\).
The free last diagonal cannot be visited and returned from before length
\(2N+1\). Thus \(c_0^{(N)}e_0^T\mathcal M^je_0=t_j\) for \(j\le2N\).

The next residual coefficient is strictly negative. Partition \(H_1^{(N)}\)
into its positive upper block \(H_1^{(N-1)}\), a last column \(b\), and
last entry \(t_{2N+1}\). Its negative determinant says

\[
t_{2N+1}<b^T(H_1^{(N-1)})^{-1}b .
\]

Every positive realizing matrix with the preceding moments has
\(m_{2N+1}\ge b^T(H_1^{(N-1)})^{-1}b\). Consequently

\[
\rho_N(\tau)=
\frac{d_{2N+1}(q(\ell\tau))}{\tau^{4N+2}}
+O(|\tau|^{-4N-4}),\qquad
d_{2N+1}=t_{2N+1}-m_{2N+1}<0 .
\]

The new four-field replacement of three channels leaves an inverse-fourteenth
tail; the five-field replacement of four leaves an inverse-eighteenth tail.
At \(q=1\), the last off-diagonal entry tends to zero, the extra mode decouples,
and the remaining block has exactly the original discrete measure.
The unlooped response is therefore the original block for every \(s\).

These constructions improve a regularity property, not a positivity bound.
Their mean coefficients are negative, so their thirteenth and seventeenth
kernel derivatives, respectively, have positive diagonal jumps by the argument
below. Their residuals remain infinite rank. No norm comparison with the old
residual, or favorable sign of the entire correction, follows.

## 10. Compression and the infinite-rank argument

First audit the earlier explicit models. If a residual starts with
\(h(\ell\tau)\tau^{-2n}\), with analytic periodic \(h\), subtract
\(h(\ell\tau)(1+\tau^2)^{-n}\) from the full residual. The remaining
multiplier is bounded near zero and \(O(|\tau|^{-2n-2})\); multiplying by
\(\tau^{2n}\) leaves an integrable function. Its inverse transform is \(C^{2n}\).
This subtraction is made with the regularized multiplier, not the singular
expression \(\tau^{-2n}\) at zero.

Let \(G_n=\mathcal F^{-1}(1+\tau^2)^{-n}\), with inverse measure
\(d\tau/(2\pi)\). The distributional identity
\((1-\partial_x^2)^nG_n=\delta_0\) shows that \(G_n\) is \(C^{2n-2}\)
and its derivative of order \(2n-1\) jumps by \((-1)^n\).
One can also obtain this from the exponentially decaying polynomial formula
for the repeated resolvent. If
\(h(\theta)=\sum h_me^{-im\theta}\), the singular part is
\(\sum h_mG_n(x-m\ell)\); exponential coefficient decay justifies local
termwise differentiation away from the jump locations.

Only \(m=0\) contributes a jump at zero. Therefore the jump equals
\((-1)^n\overline h\), where the overline here means the phase mean.
For the earlier two-field model \(n=4\), it is \(\overline{d_8}<0\).
For the earlier three-field model \(n=5\), it is
\(-\overline{d_{10}}>0\). Their global \(C^6\) and \(C^8\) regularity
claims are correct. The new models have \(n=7,9\) and the positive jumps
stated above.

Here is the missing functional-analytic step behind the column argument.
Choose a smaller open interval \(J\) of length less than \(\ell/2\).
All differences of points of \(J\) avoid nonzero return lengths.
For arbitrarily many distinct \(y_1,\ldots,y_m\in J\), the columns
\(R(\,\cdot-y_i)\) have the nonzero derivative jump at their own point and
are sufficiently smooth at the other selected points. Taking jumps in a
linear relation forces every coefficient to vanish.
If the compressed integral operator had finite rank, normalized approximate
delta inputs at \(y_i\) would have images converging in \(L^2(J)\) to these
columns. Kernel continuity gives the convergence; closedness of a
finite-dimensional range would put every column in that range, a contradiction.
The larger interval compression must therefore have infinite rank as well.
Subtracting the finite-rank pole operator cannot change this conclusion.

## 11. Every finite analytic block leaves an interval obstruction

The phase-wise proposition in Section 8 alone does not prove an interval
obstruction: coefficients supported only at inactive return lengths may fail
phase matching without affecting an interval kernel. The following separate
argument closes that gap in a specified class.

**Theorem.** Keep the one-prime \(q(\theta)\) above. Replace a finite set of
original channels by

\[
\mathcal T(s,\theta)=s\,b^*(sI+\mathcal M(\theta))^{-1}b,\qquad
\|b\|^2=c_0,
\]

where \(\mathcal M(\theta)\) is a finite-dimensional real symmetric, positive
definite, even periodic matrix analytic in a neighborhood of the real phase
circle, and \(b\) is fixed and real. Then the exact residual \(\rho_{\rm new}\)
has an infinite-rank compression on every nonempty open interval.
In the first-prime target range it cannot be completed to \(\mathsf W_L\)
by the poles or any net finite-rank correction.

**Proof.** Positivity and compactness of the phase circle give uniform positive
lower and finite upper mass bounds. Neumann expansion of the block and the
fixed-order digamma asymptotic give, for every fixed \(J\),

\[
\rho_{\rm new}(\tau)=\sum_{j=1}^J
d_j(\ell\tau)\tau^{-2j}+O(|\tau|^{-2J-2}),\qquad
d_j=(-1)^j(m_j-t_j),\quad m_j=b^*\mathcal M^jb .
\]

All coefficients are analytic periodic functions; the remainder is uniform.
The asymptotic order \(J\) is always finite. No convergent infinite expansion
is assumed.

Let \(a_*\) be the largest replaced mass. Then
\(c_j\le c_0a_*^{2j}\). The exact formula of Section 6 gives

\[
A_j\ge\frac{3(2j-1)!}{2(2\pi)^{2j}},
\]

because the alternating series satisfies
\(\eta_{\rm D}(2j)\ge1-2^{-2j}\ge3/4\).
Factorial growth dominates \(c_0a_*^{2j}\). Since \(q_{\min}>1\), some
finite odd \(J\) therefore satisfies

\[
A_J(1-q_{\min}^{-J})>c_J .
\]

At every phase,

\[
t_J/q^J=c_J-A_J(1-q^{-J})<0,\qquad m_J\ge0,\qquad d_J=t_J-m_J<0.
\]

Thus at least one of the finitely many means
\(\overline d_1,\ldots,\overline d_J\) is nonzero. Let \(k\) be the first.
To translate this fact into a local singularity, rewrite the truncated
asymptotic expansion triangularly as

\[
\rho_{\rm new}(\tau)=\sum_{j=1}^J
\frac{h_j(\ell\tau)}{(1+\tau^2)^j}+r_J(\tau),\qquad
r_J=O(|\tau|^{-2J-2}).
\]

Expanding \((1+s)^{-j}\) shows that \(h_j=d_j\) plus fixed linear
combinations of preceding \(d_i\). Hence
\(\overline h_j=0\) for \(j<k\), and
\(\overline h_k=\overline d_k\ne0\).
Near \(x=0\), all nonzero Fourier modes of every \(h_j\) give smooth
translated resolvent kernels. The lower \(j<k\) terms have no zero mode.
The \(j>k\) terms and \(\mathcal F^{-1}r_J\) are at least \(C^{2k}\).
The only jump of derivative \(2k-1\) is therefore
\((-1)^k\overline d_k\ne0\). The column argument in Section 10 proves
infinite rank. \(\square\)

The same proof permits a bounded positive operator on an auxiliary Hilbert
space if its moment functions are analytic with the required uniform bounds.
The theorem as stated does not cover arbitrary unbounded auxiliary spectra,
nonanalytic or additional spatial-frequency dependence, variable leading
observable strength, a different dispersion, or infinitely many replaced
original channels. The pointwise \(2N+1\)-moment obstruction in Section 8
does allow unbounded positive spectra when those finite moments exist.
These two scopes should not be merged.

For reproducible conservative diagonal certificates, it suffices to use
\(q_{\min}\ge2\). Exact rational arithmetic gives

| First \(N\) original channels replaced | Odd \(J\) with \(A_J(1-2^{-J})>c_J^{(N)}\) |
| --- | --- |
| 1 | 5 |
| 2 | 23 |
| 3 | 39 |
| 4 | 57 |

These are the first such odd indices in the exact search, not optimal
obstruction orders. The much earlier \(2N+1\) failures require phase-wise
moment matching. The later bounds prove that some diagonal jump survives
even when earlier coefficients are allowed to differ at inactive translations.
Neither assertion is a numerical eigenvalue inference.

## 12. Physical and classical counterparts

For every explicit new block, \(\mathcal M(q(\ell D))\) is a bounded,
uniformly positive Fourier multiplier at this fixed prime cutoff.
The frequency \(h=AI+\mathcal M\) is self-adjoint on \(H^2\).
The Fock Hamiltonian \(d\Gamma(h)\) is nonnegative with a vacuum.
At real time \(t_{\rm phys}\), the block's vacuum correlation multiplier is

\[
c_0s\,e_0^Th^{-1}e^{-it_{\rm phys}h}e_0 .
\]

Its equal-time value is the covariance used above. The time evolution measures
oscillations of the auxiliary fields; the arithmetic input is prescribed in
their spatial couplings. The input \(f\) smears a derivative observable over
the finite interval. Positive vacuum norms then supply a candidate energy for
all admissible smearings. They do not supply the equality to the arithmetic
operator.

The spatial mass multiplier is nonlocal because of the return dependence.
There is a classical positive realization of the very same response:

\[
\mathcal E[F,u]=c_0\|Fe_0-u\|^2+
c_0\|\mathcal M^{-1/2}\partial_xu\|^2,\qquad u\in H^1(\mathbb R;\mathbb C^{N+1}).
\]

For fixed \(F\in L^2\) this is a closed strictly convex problem with unique
minimizer

\[
\widehat u=(I+s\mathcal M^{-1})^{-1}\widehat F e_0 .
\]

Uniform upper and lower mass bounds imply \(u\in H^2\). Completing the
square gives

\[
\inf_u\mathcal E[F,u]
=\frac1{2\pi}\int c_0s\,e_0^T(sI+\mathcal M)^{-1}e_0
|\widehat F|^2\,d\tau .
\]

Adding the unchanged positive higher channels defines a closed positive
logarithmic form. Only finitely many bounded responses were replaced, so its
form domain is exactly \(\mathcal D_{\log,L}\). All auxiliary fields remain
on the whole line. This proves the classical counterpart, not just a
similarity of finite matrices.

The negative-mass moment contribution explains physically why this dispersion
and derivative observable cannot absorb the entire regular arithmetic error
by reallocating finitely many stable mass channels. It does not diagnose
instability of the target Weil operator or rule out quantum correlations in
other models. No genuinely quantum advantage, interacting Hamiltonian, or
supersymmetric arithmetic identity has been established here.

## 13. Verification record and the remaining operator problem

The new program uses only Python's standard library and NumPy. It:

- Replays the previous covariance program in a temporary directory and compares
  its output with the historical record without overwriting it. In the present
  environment the entire JSON agrees exactly, including all 1,320 covariance
  cases and the 80-digit residual rows.
- Independently derives 60 gamma coefficients from the short-distance kernel,
  recomputes the old Gram-determinant certificates, and checks the three-field
  moment and residual identities with exact rational matrix multiplication.
- Lists the complete target moment polynomials and leading-minor certificates
  for blocks of one through four original channels, and verifies the independent
  annihilator polynomial identity.
- Constructs the new Jacobi data at \(q=2,10,10^6\) with rational arithmetic,
  checks all claimed matched moments and the next residual sign, and compares
  the complete continued-fraction response with both normal-mode quantum
  covariance and classical minimization.
- Records exact positive margins for the conservative diagonal-obstruction
  indices in Section 11.

To reproduce from the investigation directory:

    python3 numerics/check_quantum_block_obstruction.py --output /tmp/quantum-block-check.json
    python3 validation/check_package.py

Polynomial identities and all-positive/all-negative coefficient lists are exact
finite certificates, not interval numerics. The analytic sign formula, general
annihilator proof, domain arguments, and diagonal-jump theorem are mathematical
derivations above. Floating-point normal-mode comparisons and the historical
high-precision asymptotic checks remain diagnostics without interval enclosures.
The package validator checks integrity and packaging, not the correctness of a
mathematical proof. A separate
[audit validation record](../../numerics/records/quantum-block-audit-validation-20260913.json)
records preservation and validation for this pass.

The operator gap remains the exact identity
\(\mathsf W_L=\mathsf Z_L+\mathsf P_L-\mathsf R_L\), with neither a positive
completion nor a bound on the complete signed discrepancy. The new models
leave infinite-rank \(\mathsf R_L-\mathsf P_L\); no number of additional
finite scalar boundary amplitudes repairs them. This does not exclude a useful
operator inequality or a controlled approximation to that infinite-rank error.

Further finite-block moment cancellation in this same dispersion class now has
a proved stopping reason. A productive continuation would have to control the
entire discrepancy by an operator bound, change the observable or dispersion
with an independently computed covariance, or change infinitely many original
channels with a justified domain and convergence construction. No one of those
is supplied by this pass. Coverage of all admissible inputs and unbounded
support lengths, the contact and both pole terms, and the arithmetic selection
of the model remain part of the full positivity program.
