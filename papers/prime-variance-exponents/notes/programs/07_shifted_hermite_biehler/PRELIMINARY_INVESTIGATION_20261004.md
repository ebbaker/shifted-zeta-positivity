# Preliminary investigation: the exact theta diagonal and the remaining thin band

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal analytic investigation, not independent specialist refereeing.
No new zero-free strip or global prime-variance exponent is proved.

The fresh reduction is that shifted dominance already holds
unconditionally for
\(\operatorname{Im}z\ge\sqrt{b(1-b)}\). Only the complementary thin
band remains, although its real coordinate is still unbounded. An exact
theta formula below identifies the oscillatory quantity to be controlled.
Positive scalar theta density, even with the usual symmetry, decay, and
entire-function order, does not by itself establish that inequality.

## 1. Source audit and exact conventions

Fix \(1/2<b<1\), put \(q=b-1/2>0\), and write

\[
F(s)=\xi(1/2+s),\qquad E_b(z)=\xi(b-iz),\qquad
E_b^\#(z)=\xi(b+iz).
\]

The primary source
[Lagarias, Lemma 2.1 and its proof](https://arxiv.org/pdf/math/0601653)
was checked at printed pages 5--6. It proves the dominance for
\(b\ge1\), and for \(b>1/2\) under RH, by comparison of zero
factors. Its preceding modified product has zero linear exponential
factor. Nothing in that statement proves the desired case below one
unconditionally.

For the theta normalization use
[Romik, equations (1.6)--(1.11)](https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf),
printed pages 1--2. With the same \(\xi(s)=s(s-1)\pi^{-s/2}
\Gamma(s/2)\zeta(s)/2\) as here, its positive even density is

\[
\Phi(u)=2\sum_{n\ge1}
\big(2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2}\big)
e^{-\pi n^2e^{2u}},
\quad
F(s)=\int_{\mathbb R}\Phi(u)e^{su}\,du.
\tag{1}
\]

Evenness permits the positive-half-line series to handle either tail;
there \(2\pi n^2e^{2u}-3>0\). The tails decrease faster than every
ordinary exponential, so all integrals below converge locally uniformly
in their complex parameters. These representations are inherited
classical facts; the comparisons below are deductions made here.

## 2. Fresh deduction: the complete shifted theta diagonal

Let \(z=t+iy\), \(t\in\mathbb R\), \(y>0\). Conjugation gives

\[
\Delta_b(t,y)=|E_b(z)|^2-|E_b^\#(z)|^2
=|F(q+y+it)|^2-|F(q-y+it)|^2.
\]

Expanding the two modulus squares in (1), then averaging under
\((u,v)\mapsto(-u,-v)\), gives the exact signed formula

\[
\Delta_b(t,y)=2\iint_{\mathbb R^2}
\Phi(u)\Phi(v)\sinh(q(u+v))\sinh(y(u+v))
\cos(t(u-v))\,du\,dv.
\tag{2}
\]

With \(U=(u+v)/2\), \(V=(u-v)/2\), whose Jacobian is two, set

\[
\mathcal A_{q,y}(V)=\int_{\mathbb R}
\Phi(U+V)\Phi(U-V)\sinh(2qU)\sinh(2yU)\,dU.
\]

Then \(\mathcal A_{q,y}\) is nonnegative and even, and

\[
\boxed{\Delta_b(t,y)=4\int_{\mathbb R}
\mathcal A_{q,y}(V)\cos(2tV)\,dV.}
\tag{3}
\]

The diagonal of the charter's kernel is

\[
K_b(z,z)=\frac{\Delta_b(t,y)}{4\pi y}.
\tag{4}
\]

The sign and constant follow from
\(2\pi i(\bar z-z)=4\pi y\). Equation (3) proves strict positivity
at \(t=0\). For general \(t\), it is a Fourier cosine positivity
problem; pointwise positivity of \(\mathcal A_{q,y}\) is insufficient.
In particular the oscillatory factor is not an ignorable mixed term.

The boundary limit is the entire expression

\[
\lim_{y\downarrow0}K_b(t+iy,t+iy)
=\frac1\pi\operatorname{Re}
 [\xi'(b+it)\overline{\xi(b+it)}].
\tag{5}
\]

Away from a boundary zero this equals
\(|\xi(b+it)|^2\operatorname{Re}(\xi'/\xi)(b+it)/\pi\).
The quotient version is not a definition at a zero. Boundary positivity
alone has not been shown here to imply interior positivity, and quotient
analyticity in the open half-plane must not be assumed.

## 3. Fresh deduction: an unconditional exterior region

Here is the zero-product calculation with its grouping and exponential
factor made explicit. The centered function \(F\) is even, entire of
order one, and \(F(0)\ne0\). Write \(\lambda=\rho-1/2\). Its genus-one
Hadamard factors for \(\lambda\) and \(-\lambda\) multiply to
\(1-s^2/\lambda^2\): their exponential factors cancel. Since
\(\sum_\lambda|\lambda|^{-2}<\infty\), the paired product converges
absolutely on compact sets. Evenness removes the remaining linear
exponential factor. Therefore

\[
F(s)=F(0)\prod_{\lambda\ {m modulo}\ \pm}
                    (1-s^2/\lambda^2).
\tag{6}
\]

The known zero count ensures the stated summability. Group nonreal
off-axis pairs further into quadruples
\(\alpha+i\gamma,-\alpha+i\gamma,
\alpha-i\gamma,-\alpha-i\gamma\), with \(0<\alpha<1/2\).
Their normalized polynomial factor is
\((1-s^2/(\alpha+i\gamma)^2)
(1-s^2/(\alpha-i\gamma)^2)\).
Thus the constants in comparing its modulus at two points cancel.
Multiplicities are retained. Critical-line zeros instead form the usual
pair \(i\gamma,-i\gamma\).

For the two zeros at one common ordinate \(\gamma\), the squared
modulus of the unnormalized product at \(s=x+it\) is

\[
P_{\alpha,d}(x)=((x-\alpha)^2+d^2)((x+\alpha)^2+d^2),
\quad d=t-\gamma.
\]

Expanding the quartic and subtracting at \(x=q+y\) and \(x=q-y\)
gives exactly

\[
\boxed{P_{\alpha,d}(q+y)-P_{\alpha,d}(q-y)
=8qy(q^2+y^2+d^2-\alpha^2).}
\tag{7}
\]

For a critical-line zero the corresponding single-factor squared
difference is simply \(4qy>0\). Since unconditionally
\(|\alpha|<1/2\), every factor comparison in (7) is strict when
\(q^2+y^2\ge1/4\). Both ordinate pairs of every quadruple then have
the desired sign. Finite products preserve the comparisons, and their
convergent limit preserves strictness: when the denominator is nonzero,
retain any one strictly larger factor and bound all others below by one.
If the denominator is zero, the numerator is nonzero because
\(q+y>1/2\), which corresponds to \(\operatorname{Re}s_{\xi}>1\).

Consequently, without RH or the desired partial strip,

\[
\boxed{|E_b^\#(t+iy)|<|E_b(t+iy)|\quad
\text{for all real }t\text{ and }y\ge\sqrt{b(1-b)}.}
\tag{8}
\]

For the illustrative target \(\delta=0.99\), \(b=0.995\), the
remaining region is
\(0<y<\sqrt{0.004975}\approx0.070534\), still for **every** real
\(t\). Moreover, a same-ordinate pair can oppose dominance only if

\[
|t-\gamma|<\sqrt{\alpha^2-q^2-y^2};
\tag{9}
\]

such a pair must have \(\alpha>q\), exactly a forbidden zero.
Equations (8)--(9) localize the obstacle; they do not bound those pairs
or prove that the favorable factors dominate them.

As a separate conditional scope check, if every zero obeys
\(|\alpha|\le q\), (7) is strict for all \(y>0\), including boundary
zeros with \(\alpha=q\). Conversely strict dominance prevents an
upper-half-plane zero of \(E_b\), hence prevents \(\beta>b\).
Thus dominance has exactly the closed-strip strength sought here.
Boundary zeros of \(E_b\) on the real line need not be excluded.

## 4. A counterexample to scalar-kernel positivity as a mechanism

Fix \(q<\alpha_0<1/2\), let \(c=\operatorname{sech}\alpha_0\), and
form a positive even density with the same qualitative tail properties:

\[
\widetilde\Phi(u)=\Phi(u)+\frac c2[\Phi(u-1)+\Phi(u+1)].
\]

Its bilateral transform is exactly

\[
\widetilde F(s)=F(s)[1+c\cosh s].
\tag{10}
\]

It is still even, real on the real axis, of order one, and has smooth
strictly positive superexponentially decaying density. Its added zeros
are \(s=\pm\alpha_0+(2k+1)\pi i\), all within the known critical
strip in the uncentered coordinate, but beyond the requested partial
strip. At the corresponding upper-half-plane zero of its shifted
structure function, strict dominance fails, regardless of whether the
other side also vanishes.

This is not a modification of the actual zeta function or a claim about
its primes. It is an exact counterexample to obtaining the new inequality
from only the listed scalar theta properties. Any useful theta proof must
use additional structure of the actual density; establishing its
pointwise positivity again would not meet the missing input.

## 5. Next gate and relative promise

The sharpened sufficient target is a direct proof that the Fourier
transform in (3) is strictly positive for one fixed \(q<1/2\), every
real \(t\), and \(0<y<\sqrt{1/4-q^2}\). An independently proved
positive-definiteness property of \(\mathcal A_{q,y}\) could address
nonnegativity, but strictness or exclusion of common zeros must be
handled separately. Merely assuming the strip in the product comparison
is a converse argument, not an arithmetic mechanism.

**Assessment:** a worthwhile bounded exploratory scout, now with a smaller
geometric region and an exact oscillatory target. It is less ready than
the signed arithmetic and selective-loss programs because no independent
inequality controls that region. Keep it below the top three unless a
specific theta identity, beyond scalar positivity, passes the countermodel
and proves a uniform-in-\(t\) sign. Finite grids cannot address the
remaining all-height obligation.

## Checks and limits

The Fourier normalization, Jacobian, kernel denominator, boundary
derivative, quartic difference, centered-product grouping, and explicit
counterexample were checked algebraically. The cited primary formulas
were read, but neither source's full proof was independently reproved.
No numerical sign certificate, full upper-half-plane strictness claim below one, or
manuscript change is made. Third-party PDFs were not added to the repository.
A separate same-model agent rechecked the theta normalization, kernel
constants, quartic identity, product-limit strictness, and counterexample.
