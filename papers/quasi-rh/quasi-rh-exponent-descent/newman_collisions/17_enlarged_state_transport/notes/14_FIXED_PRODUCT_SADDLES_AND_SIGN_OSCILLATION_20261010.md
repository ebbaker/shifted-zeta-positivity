# Fixed-product saddles and sign oscillation

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. Derivations and separate-agent audits are internal
LLM work, not independent mathematical validation. No priority claim is made.

At time zero, the signed transform of each fixed product channel has an
exact gamma/polygamma expression. Retaining its negative-half-line partner
transfers that expression to the legitimate shifted summands in
[Note 9](9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md).
Every fixed product summand of the signed \(J_1\) transform takes both signs
at arbitrarily large frequencies. Thus a separate nonnegativity theorem for these summands that includes
time zero is false.
This result imposes no condition on the complete physical stationary set
and is not a counterexample to the desired stationary inequality.

The leading saddle reaches the half-line endpoint at \(P=x/(4\pi)\),
with local transition width of order \(\sqrt x\). This identifies the
uniform incomplete-transform problem left by the calculation. It does
not replace Note 9's paid product cutoff of order \(x\log x\).

The exact gamma decomposition below is restricted to time zero and fixed
\(P\). At positive heat its raw negative-half-line partner diverges, as
proved in [Note 10](10_MATCHED_MELLIN_BESSEL_TRANSFORM_AND_RAW_CHANNEL_OBSTRUCTION_20261010.md).
No positive-time uniform sign or stationary-point theorem is established.

## 1. Leading two-variable saddle

Use Note 8's product \(P=nm\), divisor shift \(d_n=\tfrac14\log(P/n^2)\),
and \(z=2\pi P e^{4s}\). Before the polynomial amplitude is included,
the time-zero exponent is

\[
E_0(s,\rho)=2ixs-z\cosh(4\rho).
\]

The saddle approached from the upper source contour is

\[
\rho_P=0,
\qquad s_P=\frac14\log\frac{x}{4\pi P}+\frac{i\pi}{8}. \tag{1}
\]

Indeed \(z=ix/2\) there, and its Hessian is

\[
E_{ss}=E_{\rho\rho}=-8ix,
\qquad E_{s\rho}=0.
\]

Both Gaussian widths are of order \(x^{-1/2}\). The physical difference
coordinate is \(r=\rho+d_n\), so the leading signed \(J_1\) insertion is

\[
d_n^2(d_n^2-s_P^2). \tag{2}
\]

The complex value of \(s_P\) is essential: replacing it by its real part
loses phase information. The entire saddle amplitude is also oscillatory,
so the sign of the real part of (2) alone does not determine the sign of
the response.

For a balanced divisor \(n^2=P\), expression (2) vanishes. Gaussian
fluctuations supply its first nonzero contribution. In particular \(P=1\)
cannot be assessed by merely inserting \(\rho=0\) in the polynomial;
Section 3 computes its nonzero term exactly to leading order.

The real saddle reaches \(s=0\) when \(P=x/(4\pi)\). Since

\[
\frac{d}{dP}\Re s_P=-\frac1{4P},
\]

moving it one Gaussian width near that point changes \(P\) by order
\(\sqrt x\). This is a local saddle-location statement. It does not
permit discarding \(P>x/(4\pi)\), whose incomplete endpoints remain.

## 2. Exact fixed-product gamma readout at time zero

Let \(C_P(\alpha,\lambda)\) be the raw all-line transform of a fixed
product channel at time zero. For this one fixed \(P\), the integral and
its needed derivatives converge near \(\alpha=2ix,\lambda=0\).
The fixed-channel gamma formula from Note 10, (A7), is

\[
\mu=\frac{\alpha+10}{4},\qquad \nu=\frac\lambda4,
\]
\[
C_P(\alpha,\lambda)=\frac{\pi^{2-\mu}}{32}
 [(\mu-3)^2-\nu^2]
 \Gamma\!\left(\frac{\mu+\nu}{2}\right)
 \Gamma\!\left(\frac{\mu-\nu}{2}\right)
 P^{2-\mu}R_P(\lambda), \tag{3}
\]
\[
R_P(\lambda)=\sum_{n\mid P}e^{\lambda d_n}.
\]

This fixed-\(P\) identity does not license summing (3) separately over
all \(P\) on the physical line. Note 10 identifies that failure explicitly.

Put \(\tau=\tau(P)\), and set

\[
m_2=\frac1\tau\sum_{n\mid P}d_n^2,
\qquad m_4=\frac1\tau\sum_{n\mid P}d_n^4,
\qquad F_P(\alpha)=C_P(\alpha,0).
\]

Its logarithmic derivative with respect to \(\alpha\) is

\[
b=\frac14\left[\psi(\mu/2)-\log(\pi P)+\frac2{\mu-3}\right],
\]
\[
b'=\frac{\psi_1(\mu/2)}{32}-\frac1{8(\mu-3)^2},
\qquad
b''=\frac{\psi_2(\mu/2)}{256}+\frac1{16(\mu-3)^3}. \tag{4}
\]

All primes in this note denote \(\alpha\)-derivatives when applied to
\(b\). The second \(\lambda\)-derivative of the logarithm of the
non-divisor factor in (3) equals \(b'\), and its fourth derivative equals
\(b'''\). To see this, factor the quadratic as
\((\mu-3-\nu)(\mu-3+\nu)\). The remaining logarithm is the sum of
one function of \(\mu+\nu\), one of \(\mu-\nu\), and an affine function
of \(\mu\); its even derivatives in \(\nu\) and \(\mu\) agree.

The exact signed readouts are therefore

\[
C_{0,P}=F_P(m_2+b'),
\qquad C_{1,P}=F_P Q_P, \tag{5}
\]
\[
\boxed{Q_P=m_4-m_2b^2+5m_2b'
 +2(b')^2-b^2b'-2bb''.} \tag{6}
\]

Here

\[
C_{0,P}=\left.\partial_\lambda^2 C_P\right|_{\lambda=0},
\qquad
C_{1,P}=\left.(\partial_\lambda^4-
 \partial_\alpha^2\partial_\lambda^2)C_P\right|_{\lambda=0}.
\]

In detail, the two terms in the second expression, after division by
\(F_P\), are

\[
m_4+6m_2b'+3(b')^2+b''',
\]
\[
(b^2+b')(m_2+b')+2bb''+b'''.
\]

Subtracting cancels \(b'''\) exactly and proves (6). Retaining only the
fourth \(\lambda\)-derivative would omit the signed insertion's
\(-s^2r^2\) component.

## 3. Fixed-product asymptotics and both signs

For each fixed \(P\), put

\[
\ell_P=\log\frac{x}{4\pi P},
\qquad \vartheta_P=\frac{x}{2}(\ell_P-1)-\frac\pi4,
\]
\[
\mathcal A_P=\frac{\sqrt\pi}{512}\tau(P)P^{-1/2}
 x^{7/2}e^{-\pi x/4}.
\]

The gamma and digamma expansions on their closed vertical sectors give

\[
F_P(2ix)=\mathcal A_P e^{i\vartheta_P}(1+O(x^{-1})),
\qquad b=s_P+O(x^{-1}),
\]
\[
b'=-\frac{i}{8x}+O(x^{-2}),\qquad b''=O(x^{-2}). \tag{7}
\]

These follow from the sectorial expansions in
[DLMF §5.11](https://dlmf.nist.gov/5.11); differentiation can also be
justified by Cauchy estimates on smaller sectors. The leading quadratic
factor in (3) contributes phase \(\pi\); combined with the two gamma
phases, it produces the displayed \(-\pi/4\). It also supplies the
factor needed for the constant \(512\).

For \(P>1\), the divisor variance \(m_2\) is positive. Equations (6)–(7)
give

\[
C_{1,P}=F_P\left[m_4-m_2s_P^2
 +O_P\!\left(\frac{1+\ell_P^2}{x}\right)\right],
\]
\[
2\Re C_{1,P}=
-\frac{\sqrt\pi\,\tau(P)m_2}{4096\sqrt P}
 x^{7/2}\ell_P^2e^{-\pi x/4}
 \left[\cos\vartheta_P+O_P(\ell_P^{-1})\right]. \tag{8}
\]

For \(P=1\), \(m_2=m_4=0\), but the fluctuation term survives:

\[
C_{1,1}=F_1\left[\frac{i s_1^2}{8x}
 +O\!\left(\frac{1+\ell_1^2}{x^2}\right)\right],
\]
\[
2\Re C_{1,1}=
-\frac{\sqrt\pi}{32768}
 x^{5/2}\ell_1^2e^{-\pi x/4}
 \left[\sin\vartheta_1+O(\ell_1^{-1})\right]. \tag{9}
\]

Since \(\vartheta_P'(x)=\ell_P/2\) is eventually positive and
\(\vartheta_P(x)\to\infty\), one can choose arbitrarily large \(x\)
with the cosine in (8), or the sine in (9), equal to either \(+1\) or
\(-1\). The remainders then tend to zero relative to the displayed
nonzero values. Thus the auxiliary gamma-channel readouts take both signs.
The next section pays their endpoint partner before transferring that
conclusion to the valid shifted representation.

## 4. Uniform fixed-product endpoint payment

Let \(F_{j,P}(w)\) denote the time-zero raw product kernel with its
\(J_j\) insertion, as in Note 9. It is distinct from the gamma factor
\(F_P(\alpha)\) in Section 2. For \(0<a<\pi/8\), define

\[
N_{j,P}(x,a)=e^{-2ax}\int_{-\infty}^0
 e^{2ixs}F_{j,P}(s+ia)\,ds.
\]

Shifting the fixed-\(P\) all-line integral at time zero yields the exact
identity

\[
e^{-2ax}\int_0^\infty e^{2ixs}F_{j,P}(s+ia)\,ds
=C_{j,P}(2ix)-N_{j,P}(x,a). \tag{10}
\]

Consequently its matched contribution in Note 9 is precisely

\[
\mathcal T_{j,P}(x,a)
=2\Re\{C_{j,P}(2ix)-N_{j,P}(x,a)\}. \tag{11}
\]

This negative-half-line partner is part of the exact formula. It differs
from the vertical endpoint of a real-axis raw half-line transform in
Note 10.

**Fixed-product endpoint bound.** For fixed \(P\ge1\) and \(j=0,1\),
there is a finite constant \(K_{j,P}\) such that

\[
\boxed{|N_{j,P}(x,a)|\le K_{j,P}\frac{e^{-2ax}}x,
\quad x\ge1,\quad 0\le a<\pi/8.} \tag{12}
\]

Here the constant is uniform as \(a\uparrow\pi/8\), but no useful
uniformity in \(P\) is asserted.

To prove (12), use the exact Bessel formula (A1) of Note 10 and its
\(\lambda\)-derivatives. Its argument on \(s\le0\) is

\[
z=2\pi P e^{4(s+ia)},
\qquad 0<|z|\le2\pi P,
\qquad 0\le\arg z\le\pi/2.
\]

We give a small-order bound rather than assuming that analyticity alone
controls the origin. The connection formula
[DLMF 10.27.4](https://dlmf.nist.gov/10.27.E4), together with the
convergent \(I_\nu\) series in
[DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2), implies

\[
|(z\partial_z)^hK_\nu(z)|\le C_P |z|^{-1/4},
\quad |\nu|=1/4,\quad h=0,1,2, \tag{13}
\]

uniformly on this quadrant. Indeed the denominator \(\sin(\pi\nu)\)
in the connection formula is bounded away from zero on the order circle.
Each series term in \(I_{\pm\nu}\) carries \(z^{\pm\nu}\); its absolute
value is bounded by a constant times \(|z|^{-1/4}\) when \(|z|\le1\).
Applying \(z\partial_z\) multiplies the terms by fixed powers of
\(2k\pm\nu\), preserving uniform convergence. The rest of the bounded
\(z\)-quadrant is compact and away from the branch cut, giving (13)
there as well.

For each fixed nonzero \(z\), \(K_\nu(z)\) is entire in the order
\(\nu\). Cauchy estimates on \(|\nu|=1/4\) therefore extend (13), with
new constants, to all order derivatives through degree four at \(\nu=0\).
The finite divisor generator has bounded derivatives for this fixed \(P\).
Formula (A1) contains only the first Euler derivative \(z\partial_z\);
one further \(s\)-derivative therefore needs at most the bound \(h=2\)
in (13). If expressed with ordinary derivatives, the modified Bessel
equation
\[
z^2K_\nu''=(z^2+\nu^2)K_\nu-zK_\nu'
\]
gives the same reduction. The factor \(e^{10(s+ia)}\) in (A1) now yields,
for \(j=0,1\),

\[
|F_{j,P}(s+ia)|+|\partial_sF_{j,P}(s+ia)|
\le C_P e^{9s}(1+s^2),\qquad s\le0, \tag{14}
\]

uniformly for \(0\le a\le\pi/8\). The \(s^2\) factor pays the
\(J_1\) insertion, and the exponent \(9\) comes from
\(e^{10s}|z|^{-1/4}=O_P(e^{9s})\). The value at \(a=\pi/8\) in this
bound is the Bessel continuation; no absolute convergence of the original
real-\(\rho\) integral at that boundary is assumed.

One integration by parts gives

\[
|N_{j,P}(x,a)|\le\frac{e^{-2ax}}{2x}
\left(|F_{j,P}(ia)|+
 \int_{-\infty}^0|\partial_sF_{j,P}(s+ia)|\,ds\right).
\]

Equation (14) proves (12). At each strict interior \(a\), the same bound
at negative infinity and the Bessel exponential decay at positive
infinity justify the shift used in (10).

On Note 9's contour \(a_x=\pi/8-4\pi/x\), valid for sufficiently large
\(x\), equation (12) gives

\[
N_{j,P}(x,a_x)=O_P(e^{-\pi x/4}/x), \tag{15}
\]

because \(e^{-2a_xx}=e^{8\pi}e^{-\pi x/4}\). This is negligible
relative to the nonzero subsequence values in (8) and (9). Therefore

\[
\boxed{\text{For every fixed }P\ge1,\quad
\mathcal T_{1,P}(x,a_x)\text{ takes both signs for arbitrarily large }x.}
\tag{16}
\]

Nothing in this proof is uniform when \(P\) grows with \(x\). In
particular the gamma series and its negative partners cannot be summed
separately on the physical line. Their algebraic product tails cancel
inside the valid matched quantities, as explained in Note 10.

## 5. Positive heat and the limit of the calculation

For one divisor shift \(d\), inclusion of heat gives the exponent

\[
E_t(s,\rho)=2ixs-z\cosh(4\rho)+2t[s^2+(\rho+d)^2].
\]

Before the polynomial amplitude is incorporated, its exact saddle
equations are

\[
z\cosh(4\rho)=ix/2+ts,
\qquad z\sinh(4\rho)=t(\rho+d). \tag{17}
\]

Their first displacements from the time-zero saddle are formally

\[
s-s_P=\frac{ts_P}{2ix}+\text{higher terms},
\qquad \rho=\frac{td}{2ix}+\text{higher terms}.
\]

For fixed \(P\) and bounded \(t\log x\), these are of order \(x^{-1}\)
(the second is smaller). The polynomial amplitude causes an additional
displacement of this scale. These are local saddle equations, not a
positive-time integral asymptotic with a proved remainder.

Although the displacement is small, the heat factor at the old saddle

\[
\exp\{2t(s_P^2+d^2)\} \tag{18}
\]

is not close to one. Its modulus contains \(e^{t\ell_P^2/8}\), a power
of \(x\) in the shrinking sector, and its phase contains
\(e^{it\pi\ell_P/8}\). The divisor tilt \(e^{2td^2}\) also remains.
Thus a Taylor expansion in \(t\) with coefficients bounded independently
of \(x\) would lose terms of leading size.

More decisively, for \(t>0\) the raw negative-half-line integral in
Section 4 diverges by Note 10's (A10). One must use the incomplete source
or the completely summed Gaussian lift. Inserting (18) into the
time-zero gamma expression does not prove the corresponding heat result.

## 6. The remaining signed target

At time zero, the product channels have no common favorable sign, even after the
fixed-product endpoint is paid. The balanced first channel changes sign
through a fluctuation term missed by evaluating only at the saddle.

A useful complete asymptotic still needs the physical equation
\(H_{xx}=0\), the saddle and incomplete endpoint uniformly through
\(P\approx x/(4\pi)\), balanced-divisor fluctuations, the full heat
factor, and the sum over all remaining channels. Until a signed tail
estimate is proved, Note 9 provides the available absolute remainder.

The result is a fixed-product obstruction and an explicit description
of the missing transition problem. It proves neither the required
positive-time stationary correlation nor an RH consequence.
