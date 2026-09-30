# Global phase tails and the arithmetic crossing terms

29 September 2026. Prepared for Edward Baker with
substantial LLM assistance. Model: GPT-6 (Codex); exact serving variant and
configured reasoning effort are not exposed and are not inferred. This is
an internal mathematical derivation, not independent specialist refereeing.

## Result and scope

This continues Sections 5--7 of the
[phase boundary trace note](SONIN_PHASE_BOUNDARY_TRACE_20260929.md).
It proves the full, source-weighted limit of the **phase bulk**, including
its frequency tails, and gives its exact difference from the artificial
finite-prime deformation at every real sigma greater than one half.
The difference includes the pole, zeros to the right of the chosen line,
and half contributions from zeros on that line. No RH assumption is used.

For a compact smooth, possibly complex source, write

\[
A_\sigma[F]=\int_{\mathbb R}a(t)\phi_\sigma'(t)\frac{dt}{2\pi},
\qquad a(t)=|\widehat F(t)|^2.
\]

With the definitions below, the exact formula is

\[
\boxed{A_\sigma[F]=\Gamma[F]-W_\sigma[F]
                         +\mathcal P_\sigma[F]-\mathcal Z_\sigma[F].}
\tag{1}
\]

Moreover,

\[
\boxed{\lim_{\sigma\downarrow1/2}A_\sigma[F]
 =\sum_{\rho:\,\Re\rho=1/2}m_\rho|\widehat F(\Im\rho)|^2.}
\tag{2}
\]

The complete arithmetic form contains the additional, generally signed
off-line zero pairing. Thus the boundary correction needed for a direct
arithmetic identification is specified exactly; setting it to zero would
discard that pairing. Projection-measure tails and the boundary limit are
separate operator statements; (2) itself concerns the phase bulk.

## 1 Conventions and entire source weights

Use the Fourier convention and fixed physical cutoff of the preceding
note. For complex sources the entire continuation of the real-line weight
is

\[
a(z)=\widehat F(z)\,\overline{\widehat F(\overline z)}.
\tag{3}
\]

It satisfies \(a(\overline z)=\overline{a(z)}\), but need not be even.
In particular, its value at a nonreal argument is **not** a modulus square.
For every finite \(D\) and every integer \(N\), integration by parts in
the compact source gives

\[
\sup_{|\Im z|\le D}(1+|\Re z|)^N|a(z)|<\infty.
\tag{4}
\]

Let \(\rho=\beta+i\tau\) range over the distinct nontrivial zeros, with
multiplicity \(m_\rho\). Both signs of \(\tau\) are included. Put

\[
\begin{split}
\mathcal P_\sigma[F]&=
\begin{cases}
2\Re a(i(1-\sigma)),&1/2<\sigma<1,\\
a(0),&\sigma=1,\\
0,&\sigma>1,
\end{cases}\\
\mathcal Z_\sigma[F]&=
2\Re\sum_{\beta>\sigma}m_\rho a(\tau+i(\beta-\sigma))
 +\sum_{\beta=\sigma}m_\rho a(\tau).
\end{split}
\tag{5}
\]

All zero sums in this note converge absolutely. Indeed, (4) and
\(N(T)=O(T\log(T+2))\) give convergence, uniformly when the imaginary
source shifts range over a fixed bounded interval. The second term in
\(\mathcal Z_\sigma\) is a half residue relative to a zero strictly to
the right, not an extra multiplicity.

The definitions of the arithmetic terms remain

\[
\Gamma[F]=\int\gamma(t)a(t)\frac{dt}{2\pi},\quad
\gamma(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
W_\sigma[F]=\sum_{p,m\ge1}(\log p)p^{-m\sigma}
 [\kappa_F(m\log p)+\kappa_F(-m\log p)].
\tag{6}
\]

Compact source support makes this prime sum finite. It therefore defines
a continuous function of every real sigma, irrespective of Euler-series
convergence.

## 2 A global weighted bound for the phase

We use the entire completed function

\[
\Xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The needed classical inputs are its Hadamard product, the functional
equation, and the zero count
\(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\).
[Elkies's analytic number theory notes, pp. 2--4](https://people.math.harvard.edu/~elkies/M259.02/zeta2.pdf)
give the product, local logarithmic-derivative estimate, and zero count.
His symbol \(\xi\) omits the polynomial factor; our \(\Xi\) includes it.
The functional-equation convention is also recorded in
[DLMF §25.4](https://dlmf.nist.gov/25.4).

Taking real parts of the logarithmic derivative of the product gives

\[
\Re\frac{\Xi'}{\Xi}(\sigma+it)
=\sum_\rho m_\rho
  \frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\tau)^2}.
\tag{7}
\]

For completeness, the real Hadamard constant disappears as follows.
The product initially gives a constant
\(c=\Re B+\sum_\rho m_\rho\Re(1/\rho)\) in addition to the displayed
sum. That real sum is absolutely convergent. At any ordinate
on the critical line chosen away from zeros, reflection in that line pairs
the displayed terms to zero, whereas the functional equation makes
\(\Re(\Xi'/\Xi)(1/2+it)=0\). Thus \(c=0\).
Here and below one can simply choose any ordinate at which \(\Xi\ne0\).

Set

\[
p_d(u)=\frac{d}{d^2+u^2}\quad(d\ne0),\qquad p_0(u)=0.
\]

The zero-width convention records the removable real-parameter phase at
a zero on the line. It is not a distributional limit as \(d\to0\).
Using the definition of \(\Xi\), the phase identity becomes

\[
\begin{split}
\phi_\sigma'(t)
={}&2\sum_\rho m_\rho p_{\sigma-\beta}(t-\tau)
 +\Re\psi(1/4+it/2)-\Re\psi(\sigma/2+it/2)\\
&-2p_\sigma(t)-2p_{\sigma-1}(t).
\end{split}
\tag{8}
\]

At a zero or at the pole on the chosen line, (8) means the smooth extension
of the derivative of the phase ratio. The singular logarithmic-derivative
term itself is purely imaginary on that line and has zero real part.

For \(d\ne0\), the elementary convolution of two Cauchy kernels gives

\[
\int_{\mathbb R}\frac{|p_d(t-\tau)|}{1+t^2}\,dt
=\pi\frac{1+|d|}{(1+|d|)^2+\tau^2}.
\tag{9}
\]

At \(d=0\) the left side is zero, so the corresponding upper bound still
holds. If \(1/2\le\sigma\le S<\infty\), then
\(|\sigma-\beta|\le\max(S,1)\). Summing (9), using
\(\sum_\rho m_\rho/(1+\tau^2)<\infty\), proves

\[
\boxed{\sup_{1/2\le\sigma\le S}
 \int_{\mathbb R}\frac{|\phi_\sigma'(t)|}{1+t^2}\,dt<\infty.}
\tag{10}
\]

The rational terms are handled by (9). The digamma difference is locally
uniformly bounded and is at most \(O_S(\log(|t|+2))\), which is sufficient
for this weighted integral. No lower bound on the horizontal distance
from the chosen line to a zeta zero is needed.

Consequently, for every Schwartz weight \(a\),

\[
\sup_{1/2\le\sigma\le S}
 \int_{|t|>R}|a(t)\phi_\sigma'(t)|\,dt
\le C_S\sup_{|t|>R}(1+t^2)|a(t)|\longrightarrow0.
\tag{11}
\]

This proves both absolute existence of the bulk integral and the uniform
frequency-tail estimate required to pass from compact frequency windows
to compact smooth position sources.

## 3 Contour comparison, including its convergence

First suppose \(\sigma\ne1\) and no zero has real part sigma. For
\(\sigma<2\), choose the right contour at \(c=2\); for larger sigma the
absolutely convergent Euler calculation already gives (1).
The contour integrand for one of the two logarithmic-derivative terms is

\[
a(-i(s-\sigma))\frac{\zeta'}{\zeta}(s)\frac{ds}{2\pi i}.
\tag{12}
\]

Choose heights \(T_n\in[n,n+1]\) whose distance from every zero ordinate
is at least \(c_1/\log(n+2)\). The unit-interval zero count is
\(O(\log(n+2))\); excluding intervals with a sufficiently small total
length constructs such heights. Conjugation gives the same property at
\(-T_n\). On the horizontal sides the local partial-fraction estimate

\[
\frac{\zeta'}{\zeta}(u+iT_n)
=\sum_{|T_n-\tau|<1}\frac{m_\rho}{u+iT_n-\rho}
  +O(\log(T_n+2))
\]

therefore gives \(O(\log^2(T_n+2))\), uniformly for
\(u\in[\sigma,2]\). This estimate is the one on p. 3 of the cited
Elkies notes; it also follows by subtracting the Hadamard logarithmic
derivatives at \(u+iT_n\) and \(2+iT_n\). Formula (4) makes both
horizontal integrals tend to zero.

Orient the left side upward and the right side downward. This is the
clockwise orientation, so the left vertical integral equals the right
vertical integral **minus** the sum of residues. The pole of zeta has
logarithmic-derivative residue \(-1\), while a zero has residue
\(+m_\rho\). Thus the crossing contributions from (12) are

\[
1_{\sigma<1}a(-i(1-\sigma))
 -\sum_{\beta>\sigma}m_\rho a(\tau-i(\beta-\sigma)).
\tag{13}
\]

On the right line the Euler series converges absolutely. Shifting the
entire weight back to the real frequency axis gives

\[
\int_{\mathbb R} a(t-i(2-\sigma))e^{-it\log n}\frac{dt}{2\pi}
=n^{2-\sigma}\kappa_F(-\log n).
\]

Hence the right-line integral in (12) is
\(-\sum_{n\ge2}\Lambda(n)n^{-\sigma}\kappa_F(-\log n)\).
The interchange is made on the line 2 before this weight shift, where it
is absolute; compact correlation support then makes the resulting sum
finite.

Repeat the same calculation with \(a(-z)\) and add the two finite-height
identities **before** taking their limit. On the left this yields

\[
\int_{-T_n}^{T_n}a(t)
 \left(\frac{\zeta'}{\zeta}(\sigma+it)
      +\frac{\zeta'}{\zeta}(\sigma-it)\right)\frac{dt}{2\pi}.
\]

This sum converges absolutely by (10), together with the integrable
archimedean term. No separate absolutely convergent integral of the
imaginary part of \(\zeta'/\zeta\) is claimed. Adding (13) for the two
weights, using conjugation of the zero set and (3), gives
\(\mathcal P_\sigma-\mathcal Z_\sigma\) with the strict inequalities
in (5). The prime terms give \(-W_\sigma\), proving (1) on these lines.

To include an exceptional line \(\sigma=\sigma_0\), take the average
of the limits from \(\sigma_0-h\) and \(\sigma_0+h\), through
nonexceptional lines. On every bounded frequency window, local analytic
factorization shows that the average is exactly the removable phase
derivative at \(\sigma_0\): the two limits of a zero's Cauchy kernel
are opposite delta masses. The same statement applies with opposite sign
to the pole at sigma 1. Uniform tails (11) extend this average identity
to the whole source. Absolute and uniform convergence of the shifted
zero weights extends the residue identity at the same time. This gives
the on-line zero term in (5) and the pole value
\(\mathcal P_1=a(0)\), proving (1) for every sigma greater than one half.

As a sign check, crossing sigma 1 from right to left changes the bulk by
\(+2a(0)\). Crossing a zero line from right to left changes its local
bulk contribution by \(-2m_\rho a(\tau)\). These agree with (5).

## 4 The complete critical arithmetic expression

The local phase concentration proved in the preceding note is

\[
\phi_\sigma'(t)\frac{dt}{2\pi}
\longrightarrow\sum_{\beta=1/2}m_\rho\delta_\tau
\]

on compact smooth frequency tests. Equations (10)--(11) extend it to every
Schwartz test. The discrete limit has the corresponding weighted finite
mass by the same zero count. This proves (2).

By (4), dominated convergence in the crossing sums yields

\[
\lim_{\sigma\downarrow1/2}\mathcal Z_\sigma[F]
=\mathcal Z_{\rm off}[F]
:=2\Re\sum_{\beta>1/2}m_\rho a(\tau+i(\beta-1/2)).
\tag{14}
\]

The on-line terms at exceptional sigmas cause no difficulty: after any
fixed finite set of zeros has been treated, their remaining total is
uniformly small by (4). Similarly,
\(\mathcal P_\sigma\to2\Re a(i/2)\). Formula (1) therefore gives

\[
\boxed{\Gamma[F]-W_{1/2}[F]
=\sum_{\beta=1/2}m_\rho a(\tau)
 +\mathcal Z_{\rm off}[F]-2\Re a(i/2).}
\tag{15}
\]

Reflection \(\beta+i\tau\mapsto1-\beta+i\tau\) pairs the two
off-line terms as conjugates by (3). Thus the first two terms on the
right are exactly

\[
\sum_\rho m_\rho a(\tau+i(\beta-1/2)),
\]

the complete zero pairing in these conventions. This verification also
handles complex, non-even sources; no assumption that \(a\) is even
was made.

For the prepared sources
\(F=(-\partial_x^2+1/4)h\), \(h\in C_c^\infty\),
one has \(\widehat F(\pm i/2)=0\), so
\(a(\pm i/2)=0\). The final pole term in (15) vanishes. The moving
pole term \(\mathcal P_\sigma\) at intermediate sigmas generally does
not vanish; nor does source preparation imply \(a(0)=0\).

## 5 Consequence for the positive trace program

The companion [frequency-tail theorem](SONIN_PHASE_FREQUENCY_TAILS_20260929.md),
including its bounded-sigma-strip extension, proves the independently
represented full-source decomposition
\(B_\sigma=A_\sigma+K_\sigma\) for every \(\sigma>1/2\).
Combining this identity with (1) gives the exact discrepancy

\[
B_\sigma-(\Gamma-W_\sigma)
=K_\sigma+\mathcal P_\sigma-\mathcal Z_\sigma.
\tag{16}
\]

For prepared sources, identification of the critical positive trace with
the desired arithmetic form therefore requires

\[
\lim_{\sigma\downarrow1/2}K_\sigma[F]
=\mathcal Z_{\rm off}[F].
\tag{17}
\]

The right side is signed in general and involves all off-line zeros,
through nonreal values of the entire source weight. Merely showing
\(K_\sigma\to0\) would identify the bulk critical-line measure and
would not establish the unconditional arithmetic comparison.

This note closes the bulk frequency-tail and arithmetic-crossing
obligations. It neither proves (17) nor identifies the actual projection
measure's local critical limit. Those require the cutoff-operator analysis.
