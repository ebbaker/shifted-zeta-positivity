# Matched Mellin Bessel transform and the raw channel obstruction

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. Derivations and separate-agent audits are internal
LLM work, not independent mathematical validation.


The [product pairing in Note 8](8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md)
admits an exact incomplete Mellin–Bessel representation with both endpoint
terms retained. Its unrestricted Mellin version recovers the original
completed-zeta product, while the raw divisor series fails on the physical
line. At positive heat even a single raw channel has no absolute full-line
Mellin chamber. These conclusions complement the [paid contour bounds](9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md);
they do not establish a stationary sign theorem.

## 1. Complete exponential generator at time zero

Write
\[
G(s,\lambda)=\int_{\mathbb R}e^{\lambda r}
 \Phi_e(s+r)\Phi_e(s-r)\,dr,
\qquad
M_+(\alpha,\lambda)=\int_0^\infty e^{\alpha s}G(s,\lambda)\,ds.
\]
Here \(s\) is real, \(G(s,\lambda)\) is entire in \(\lambda\), and
\(M_+\) is entire jointly in \((\alpha,\lambda)\). The complete double-exponential
decay supplies local uniform domination of every parameter derivative.
Put
\[
a_P=2\pi P,\quad z=a_Pe^{4s},\quad
\nu=\lambda/4,\quad \mu=(\alpha+10)/4,
\]
and retain the complete divisor generator from Note 8,
\[
R_P(\lambda)=\sum_{n\mid P}e^{\lambda d_n},
\qquad d_n=\tfrac14\log(P/n^2).
\]
The Bessel integral gives
\[
\int_{\mathbb R}e^{\lambda\rho-z\cosh(4\rho)}\,d\rho
=\tfrac12K_\nu(z).
\]
Consequently, for \(s\ge0\), the exact complete product source is
\[
G(s,\lambda)=\frac{\pi^2e^{10s}}2
 \sum_{P\ge1}P^2R_P(\lambda)
 \bigl[z^2+9+6z\partial_z\bigr]K_\nu(z).
\tag{A1}
\]
All divisor channels and the negative polynomial term survive.
The formula uses the standard integral in
[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9); the factor one half
comes from changing \(4\rho\) to the Bessel variable and reflecting it.

## 2. Incomplete Mellin transform with both endpoint terms

Define
\[
I_\mu(a,\nu)=\int_a^\infty z^{\mu-1}K_\nu(z)\,dz,
\qquad D(\mu,\nu)=(\mu-3)^2-\nu^2.
\]
Then
\[
\boxed{
M_+(\alpha,\lambda)=\frac{\pi^2}{8}
\sum_{P\ge1}P^2R_P(\lambda)
\left[
D(\mu,\nu)a_P^{-\mu}I_\mu(a_P,\nu)
+(\mu-6)K_\nu(a_P)-a_PK_\nu'(a_P)
\right].}
\tag{A2}
\]
The prime means derivative in the positive Bessel argument. The series
and all fixed parameter derivatives converge locally uniformly on
\(\mathbb C^2\). In particular, (A2) is valid at the physical
\(\alpha=2ix\) for every real \(x\).

To derive it, substitute \(z=a_Pe^{4s}\) into (A1). Integrating the
\(6zK_\nu'\) term produces \(-6a_P^\mu K_\nu(a_P)\).
The Bessel equation gives
\[
I_{\mu+2}(a,\nu)
=(\mu^2-\nu^2)I_\mu(a,\nu)
 +\mu a^\mu K_\nu(a)-a^{\mu+1}K_\nu'(a).
\]
Combining them proves (A2), including the two displayed endpoint terms.
Their omission would change the complete source. The lower cutoff is
\(a_P\), not zero, and it grows with the arithmetic product index.

Local uniform convergence follows directly from the original absolute
half-line source envelope with bounded exponential insertions. It also
follows from the Bessel integral: on compact \(\nu\)-sets,
\(K_\nu(a)\), its fixed order derivatives, and the incomplete integrals
are bounded by \(e^{-a}\) times a fixed polynomial in \(a\) and
\(\log a\) for \(a\ge2\pi\). Meanwhile
\(|R_P(\lambda)|\le\tau(P)P^{|\operatorname{Re}\lambda|/4}\).

The exact signed readouts at time zero are
\[
\widehat J_{0,0}(2x)
=2\operatorname{Re}\left.
 \partial_\lambda^2 M_+(2ix,\lambda)\right|_{\lambda=0},
\tag{A3}
\]
\[
\widehat J_{1,0}(2x)
=2\operatorname{Re}\left.
 (\partial_\lambda^4-\partial_\alpha^2\partial_\lambda^2)
 M_+(\alpha,\lambda)\right|_{\alpha=2ix,\lambda=0}.
\tag{A4}
\]
Thus (A2) retains the \(-s^2r^2\) insertion. It is not legitimate to
replace it by just the fourth order derivative in \(\lambda\).
Stationarity remains a condition on the full physical \(H\), never on
one \(P\)-channel or on a finite collection of divisors.

## 3. Exact full Mellin collapse and its absolute-convergence chamber

For time zero only, let
\[
M(\alpha,\lambda)=\int_{\mathbb R^2}
e^{\alpha s+\lambda r}\Phi_e(s+r)\Phi_e(s-r)\,dr\,ds.
\]
Changing to \(u=s+r,v=s-r\) gives the entire identity
\[
\boxed{M(\alpha,\lambda)=\frac1{32}\xi(q_+)\xi(q_-),
\qquad q_\pm=\frac{\alpha+2\pm\lambda}{4}.}
\tag{A5}
\]
Here \(\xi(q)=\tfrac12q(q-1)\pi^{-q/2}\Gamma(q/2)\zeta(q)\).
The normalization is fixed by
\[
\int_{\mathbb R}e^{wu}\Phi_e(u)\,du
=\frac14\xi\!\left(\frac{w+1}{2}\right).
\]
That single-factor identity follows by raw theta integration in
\(\operatorname{Re}w>1\), then entire continuation.

The raw double theta expansion over the full \((s,r)\)-plane is
absolutely integrable precisely in the chamber
\[
\boxed{\operatorname{Re}\alpha>2+|\operatorname{Re}\lambda|.}
\tag{A6}
\]
Indeed the change to \((u,v)\) factors the absolute sum. If \(\phi_n\)
is the nth raw theta summand, its actual absolute sum satisfies
\[
\sum_{n\ge1}|\phi_n(u)|\sim c_{\rm abs}e^{-u},\qquad
c_{\rm abs}=\int_0^\infty|2\pi^2y^4-3\pi y^2|e^{-\pi y^2}\,dy>0
\quad(u\to-\infty).
\]
This is a Riemann sum with mesh \(e^{2u}\). It proves both necessity
and sufficiency of \(\operatorname{Re}(\alpha\pm\lambda)/2>1\).
The larger positive/negative-parts envelope from Note 8 also proves
sufficiency, but the actual absolute sum establishes the word precisely.

Within (A6), each fixed \(P\) all-line Mellin integral equals
\[
\frac{\pi^{2-\mu}}{32}
D(\mu,\nu)
\Gamma\!\left(\frac{\mu+\nu}{2}\right)
\Gamma\!\left(\frac{\mu-\nu}{2}\right)
P^{2-\mu}R_P(\lambda).
\tag{A7}
\]
The Bessel Mellin integral is
[DLMF 10.43.19](https://dlmf.nist.gov/10.43.E19), valid initially for
\(\operatorname{Re}\mu>|\operatorname{Re}\nu|\).
The complete arithmetic series is exactly
\[
\sum_{P\ge1}P^{-(\alpha+2)/4}R_P(\lambda)
=\zeta(q_+)\zeta(q_-)
\tag{A8}
\]
in (A6). Combining gamma recurrences and
\(D(\mu,\nu)=(q_+-1)(q_--1)\) reduces (A7) to (A5).
Thus the unrestricted complete Mellin transform merely recovers the
original completed-zeta product. It does not create a new positivity
input or an arithmetic gain.

The physical line \(\alpha=2ix,\lambda=0\) lies outside (A6).
Analytic continuation of the *summed expression* is valid, but termwise
summation there is not licensed by (A7). At \(x=0\) the failure is
especially transparent: every (A7) term is
\[
\frac{\Gamma(5/4)^2}{128\sqrt\pi}\,
\frac{\tau(P)}{\sqrt P}>0,
\tag{A9}
\]
so their sum diverges, although the actual glued (A5) is finite.
For fixed \(P\), the valid positive-half-line channel (A2) is
exponentially small as \(P\to\infty\). Writing it as the full Mellin
channel minus its negative-half-line raw partner therefore requires
cancellation of the entire algebraic term (A9) before summing in \(P\).
One cannot sum the two parts separately on the physical line.

This is an explicit matched-endpoint obstruction, not an error in
Note 8, which correctly restricts its absolute rearrangement to \(s\ge0\).

## 4. Positive heat makes the naive all-line channel transform worse

For every fixed \(P\), every \(t>0\), every finite complex Mellin
parameter \(\alpha\), and \(\rho\) in a fixed bounded interval,
\[
B_P(s,\rho)=9\pi^2P^2e^{10s}(1+O(e^{4s}))
\quad(s\to-\infty),
\]
uniformly on that interval. The heat weight includes
\(e^{2ts^2}\), and its remaining \(\rho+d_n\) factor is bounded
above and below by positive constants on suitable fixed intervals.
Hence even one fixed divisor channel has an infinite absolute integral
over negative \(s\), because
\[
\int_{-\infty}^{-1}
e^{2ts^2+(10+\operatorname{Re}\alpha)s}\,ds=\infty.
\tag{A10}
\]
The same obstruction survives every fixed polynomial insertion whose
absolute value is bounded below on an appropriate bounded \(\rho\)
interval, including \(J_0\) and signed \(J_1\); for \(J_1\),
\(r^2(r^2-s^2)\) has a negative region of growing magnitude there.
The complete Jacobi-glued heat source is nevertheless absolutely
integrable for all finite complex parameters. Thus at positive heat,
there is no finite Mellin convergence half-plane that makes the naive
full-line raw product-channel interchange valid. Modular gluing must
precede that operation, or the transformation must retain the half-line
with all endpoint partners and remainders.

## 5. An optional valid positive-time lift

If \(M_{+,t}\) denotes the actual half-line double transform with the
heat factor \(e^{2t(s^2+r^2)}\), then for \(t>0\)
\[
M_{+,t}(\alpha,\lambda)
=\frac1{8\pi t}\int_{\mathbb R^2}
e^{-(a^2+b^2)/(8t)}M_+(\alpha+a,\lambda+b)\,da\,db.
\tag{A11}
\]
This follows from the ordinary Gaussian exponential moment in each
variable. Fubini is justified at the level of the complete physical
source: integrating absolute values in \(a,b\) reproduces a bounded
complex-frequency majorant with the heat factor, which is integrable by
theta decay. (A3)–(A4) remain valid with \(M_{+,t}\).

It is valid to first sum (A2), then use (A11). Interchanging the Gaussian
integral with a raw all-line Mellin series requires a fresh proof and is
not justified by the time-zero chamber. The Gaussian lift by itself
contains no conditional stationary sign information.

## 6. A certified nonzero boundary term in the first divisor channel

Let \(J_{0,P}(s)\) be the time-zero raw product channel
\[
J_{0,P}(s)=\int_{\mathbb R}B_P(s,\rho)
 \sum_{n\mid P}(\rho+d_n)^2\,d\rho.
\]
The complete sum is the even kernel \(J_{0,0}(s)\), so its derivative
at zero vanishes. The individual channels need not be even. In fact the
[outward endpoint checker](../numerics/check_paired_boundary_derivative.py)
proves
\[
\boxed{0.00474119<J_{0,1}'(0)<0.00500393.}                 \tag{A12}
\]
This is a property of the actual first theta product channel, not of a
generic substitute kernel.

For \(z_1=2\pi\) and \(w=\cosh(4r)\), direct differentiation gives
\[
J_{0,1}'(0)=\pi^2\int_{\mathbb R}r^2 e^{-z_1w}
 [18z_1^2+24z_1^2w^2-4z_1^3w-120z_1w+90],dr.          \tag{A13}
\]
The checker integrates complete interval ranges over 4,096 cells in
\(0\le r\le1\), doubles by evenness, and pays the whole remaining tail.
Indeed put \(C=42z_1^2+4z_1^3+120z_1+90\) and
\(b=4\pi e^4-8\). The absolute tail is at most
\[
2\pi^2 C e^{8-\pi e^4}(b^{-1}+2b^{-2}+2b^{-3})
 <9.7860\cdot10^{-70}.                                \tag{A14}
\]
Use \(e^{4r}/2\le w\le e^{4r}\) and
\(e^{4(1+y)}\ge e^4(1+4y)\) for the last bound. The
[small record](../numerics/PAIRED_BOUNDARY_DERIVATIVE_RECORD_20261010.json)
contains the directed endpoints and the hash-checked interval sources.

Fix \(0<a<\pi/8\), and take real \(x\to+\infty\). For this raw channel,
the endpoint in the half-line contour shift has real contribution
\[
V_1(x,a)=2\Re\left(i\int_0^a e^{-2xy}J_{0,1}(iy)\,dy\right)
 =-\frac{J_{0,1}'(0)}{2x^2}+O_a(x^{-4}).                \tag{A15}
\]
The sign and coefficient follow from Taylor expansion on the vertical
segment. If \(C_3=\sup_{0\le y\le a}|J_{0,1}'''(iy)|\), an explicit
error bound is
\[
\left|V_1(x,a)+\frac{J_{0,1}'(0)}{2x^2}\right|
\le \frac{C_3}{8x^4}
 +|J_{0,1}'(0)|e^{-2ax}\left(\frac a x+\frac1{2x^2}\right).
\tag{A16}
\]
Here \(C_3<\infty\) by the fixed-channel closed-strip domination; no
uniform estimate of this constant as \(a\uparrow\pi/8\) is asserted.

Thus omitting the endpoint of even the first channel creates an
algebraic error. The complete transform has the exponentially decaying
scale paid in Note 9. The cancellation of these algebraic endpoints is
therefore an essential modular correlation, not a negligible correction.
At fixed \(a\), locally uniform absolute convergence licenses their
complete sum, whose real contribution is exactly zero by Jacobi
evenness. Transforming a finite raw source requires its endpoint payment.
There is a different valid operation: first cancel the endpoints for the
complete kernel, then truncate its shifted integral with Note 9's paid
remainder. That approximates the complete Fourier response and is not
the Fourier transform of the finite raw source.

## 7. What the next signed estimate must retain

The safe starting representations are the half-line series (A2), its
complete positive-time lift (A11), and Note 9's full glued contour.
Each keeps the boundary source that the unrestricted raw Mellin series
loses. A future asymptotic must control the incomplete integral and both
Bessel endpoints together, including order derivatives for the signed
\(J_1\) insertion and every omitted product channel. The complete
physical conditions \(H_x=0\) or \(H_{xx}=0\) must be imposed only
after those operations. None of (A2), (A5), or (A12) supplies that sign.
