# The native inverse/plain convolution and its diagonal benchmark

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. This is a same-model internal
native ideal-algebra derivation. It uses the inherited fixed-field prime
ideal theorem for an asymptotic coefficient count. It is not a numerical
realization of selected rows or a proof of the mixed moment.

The proof comparison is with printed pp. 159–178 of the
[30 September companion manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
particularly (18.18), (18.30), (18.31), and (18.50).
The source PDF inspected in phase 1 has SHA-256
8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.

## 1 Complete convolution versus the actual annuli

Work in the monoid of good ideals, outside the original fixed excluded
set. Let \(\mathbf1(v)=1\) on that monoid and let \(\epsilon\) be its
convolution identity. Exact ideal Möbius inversion gives
\[
 \mu_F*\mathbf1=\epsilon,\qquad
 \mu_F*\mathbf1*\mathbf1=\mathbf1. \tag{1}
\]
For a fixed completely multiplicative native presentation \(\psi_u\),
including its zeros, this also gives
\[
 (\mu_F\psi_u)*\psi_u*\psi_u=\psi_u. \tag{2}
\]
These are complete coefficient identities. They do not remove the
original physical profiles.

The actual fixed-profile mixed coefficient without prime slots is
\[
 C(v)=\sum_{d k_1k_2=v}
       \mu_F(d)A_0(\mathrm Nd/D)
           B(\mathrm Nk_1/N)B(\mathrm Nk_2/N),
 \qquad X=DN^2,\quad A=r+2m . \tag{3}
\]
The native polynomial is
\[
 X^{-1/2}\sum_v C(v)\psi_u(v)=M_u S_u^2 . \tag{4}
\]
The inverse variable is squarefree because of \(\mu_F\); the two plain
variables have their unrestricted original good annuli.

For initial independent Mellin lines to the right of one, the arithmetic
Dirichlet series is
\[
 \sum_{d,k_1,k_2}
 \frac{\mu_F(d)\psi_u(dk_1k_2)}
      {(\mathrm Nd)^s(\mathrm Nk_1)^t(\mathrm Nk_2)^w}
 =\frac{L_{\rm orig}(t,\psi_u)L_{\rm orig}(w,\psi_u)}
        {L_{\rm orig}(s,\psi_u)}. \tag{5}
\]
Here \(L_{\rm orig}\) uses exactly the original good Euler factors and
zero-extended presentation. Mellin inversion therefore expresses the
unnormalized actual polynomial as
\[
 \frac1{(2\pi i)^3}
 \int\widehat A_0(s)\widehat B(t)\widehat B(w)
       D^sN^{t+w}
       \frac{L_{\rm orig}(t,\psi_u)L_{\rm orig}(w,\psi_u)}
            {L_{\rm orig}(s,\psi_u)}\,ds\,dt\,dw . \tag{6}
\]
The inverse/plain cancellation occurs on a common Mellin argument;
the actual profiles supply three independent variables. There is no
permitted restriction of (6) to \(s=t=w\), nor an identity making (3)
equal to the constant coefficient in (1). Pure norm twists translate
these arguments but do not eliminate their independent profile variables.
No contour movement or averaged bound is asserted in (6).

## 2 A genuine prime-ideal subset makes the coefficient norm sharp

Take fixed nonzero continuous annular profiles \(A_0,B\). Choose fixed
closed intervals in their original supports on which their moduli are
bounded below. For a varying profile family, this argument requires such
windows uniformly in that family; it is already a valid diagnostic for
one fixed permitted choice.

The working box has the strict scale separations
\[
 r>m,\qquad r<2m .
\]
Choose a good prime ideal \(p\) in the selected window of radius \(D\),
and two distinct good prime ideals \(q_1,q_2\) in the selected window of
radius \(N\). Let \(v=pq_1q_2\). For sufficiently large \(U\), its only
divisor in the original inverse annulus is \(d=p\):
\(q_i\) are too small, \(q_1q_2\) is too large, and every divisor
containing \(p\) and another prime is too large. Its remaining two
plain factors can only be \(q_1,q_2\), in either order. Thus
\[
 C(pq_1q_2)=
 -2 A_0(\mathrm Np/D)
       B(\mathrm Nq_1/N)B(\mathrm Nq_2/N). \tag{7}
\]
The two terms agree even for complex profiles; they do not cancel.
Fixed ray phases multiply the full product and do not change its modulus.

The inherited fixed-field prime ideal theorem gives
\(\asymp D/\log D\) choices for \(p\) and
\(\asymp N^2/(\log N)^2\) unordered distinct pairs \(q_1,q_2\).
Unique ideal factorization distinguishes these products: \(p\) is
identified by its larger norm, while interchanging the two smaller primes
has already been accounted for. Consequently
\[
 \boxed{
 \sum_v |C(v)|^2\frac{\varphi(v)}{\mathrm Nv}
 \gg_{A_0,B}\frac{DN^2}{(\log U)^3}.
 }\tag{8}
\]
Here \(\varphi(v)/\mathrm Nv=\prod_{\mathfrak p\mid v}
(1-(\mathrm N\mathfrak p)^{-1})\) tends uniformly to one on this subset.
The divisor-bound upper estimate is \(XU^\varepsilon\), so the power
of \(X=DN^2\) is sharp for this positive coefficient norm.

This is an asymptotic native ideal count, not a finite phase experiment.
It neither constructs a selected zero bin nor gives a lower bound for
its energy.
The prototype has no prime slots. It obstructs a proposed uniform
coefficient estimate covering that class and zero-slot children; a
specialized argument for one fixed nonempty original slot set would
need its own analysis. No such specialized obstruction is asserted.

The same subset also survives the source's standard two-plain centering.
At physical width \(M=1\), its comparison scales are
\(Y_1=U^{1/4}\), \(Y_2=U^{2m-1/4}\), with \(Y_1Y_2=N^2\).
After the only inverse divisor \(p\) is fixed, the remaining divisors have
norm exponents \(0,m,m,2m\). None lies in the \(Y_1\) annulus. The
comparison rectangle is therefore zero on this subset, while (7) remains.
Hence the analogous coefficient norm for that centered difference also
has the lower bound (8). Equal-product centering alone does not create
a power saving in this marked coefficient norm.

## 3 What the separately positive second diagonal would require

On a zero-common-support, unpunctured Gauss-norm sector, the second
finite transform on source p. 165 gives the exact diagonal
\[
 \mathcal D_2=
 U^{K+g-\ell-A}\widehat\Phi_2(0)
       \sum_v |C(v)|^2\frac{\varphi(v)}{\mathrm Nv}.
 \tag{9}
\]
The fixed ray and norm phases have modulus one on these good columns.
The quantity \(K+g-\ell\) is the effective Gauss-row length after the
specified enlargement and, if present, the pool-density factor.
The [marked source bridge](16_SOURCE_FOURTH_MARKED_BRIDGE_20261009.md) allows
\(U^{A+\Lambda}\), with \(\Lambda=dr-1/540\), for this marked norm.
If the proof bounds the diagonal separately, it would require
\[
 \sum_v |C(v)|^2\frac{\varphi(v)}{\mathrm Nv}
 \ll U^{\,2A+\Lambda-(K+g-\ell)+\varepsilon}. \tag{10}
\]
For the upper-frequency sector, the nominal first frequency length is
\(K_0=2A-1\). The source enlargement leaves effective length \(K_0\)
plus its small positive terminal allowance. Ignoring only those
explicitly small allowances, (10) requests power \(1+\Lambda\).
The benchmark (8) contradicts that coefficient-norm request whenever
\[
 A>1+\Lambda .
\]
In the coarse working box the gap is uniformly positive:
\[
 A-1-\Lambda
 =(1-d)r+2m-1+\frac1{540}
 >\frac{1403}{6750}=0.2078518518\ldots . \tag{11}
\]
The same benchmark survives the standard centered two-plain coefficient.
Therefore the Möbius sign and complete convolution identity cannot repair
the unchanged separate-diagonal estimate by improving this coefficient
norm.

The obstruction applies to this proposed separately positive majorant.
The second diagonal need not be a lower bound for the entire Gauss norm:
its transformed off-diagonal terms can have signs. It is also not a
positive contribution isolated from the original selected signed
correlation. Some artificial common pairs were introduced during the
first coprimality separation, whose full Möbius sum cancels them before
absolute estimates. Retaining that signed combination or using a direct
near-coprime estimate remains a different possibility.

## 4 Bounded conclusion for the next proof choice

The complete inverse/plain convolution is useful as an exact benchmark,
but its cancellation does not persist coefficientwise through the actual
separated annuli. A positive \(\ell^2\) estimate for the marked coefficient
or the standard comparison difference cannot recover the missing power.
The analytic bridge must preserve further signed correlation, improve a
different part of the proof, or bypass this separate Gauss-diagonal bound.
This test establishes no estimate for the surviving selected near-coprime
remainder. The complementary native coprime contour test and a positive
weighted-response alternative are in
[note 17](17_NATIVE_COPRIME_AND_RESPONSE_TEST_20261009.md).
The [small checker](../../numerics/check_mixed_marked_bridge.py) tests the
complete convolution and isolated annular coefficient at finite ideal
norms, the exact rational budget gap, and the layer-integration identity.
Its finite coefficient sample is not a realization of the operational
bin; the asymptotic native count in (8) uses the inherited prime ideal
theorem and the strict exponent separations.
