# Conditional improvement from a longer total prime slot length

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.

## Status and candidate

Conditional on the external structural inputs listed in the earlier
[first parameter extension](PARAMETER_EXTENSION_20261008.md), including the
[September 30 paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)'s seven-eighths theorem, the modified geometry below supports

\[
\sigma=\frac{20999}{24000}=\frac78-\frac1{24000}.
\]

This is 25 times the displacement of the initial candidate
\(7/8-1/600000\). The argument is a conditional extension of the stated
analytic machinery, not an independent verification of the external
199-page proof, a formal proof, or a claim of priority. The computation
below proves the continuous exponent inequalities exactly; it does not
prove the imported reflection, detector, or moment estimates.

Keep \(\kappa=3/4\) in Lemma 18.1. The already available boundary
\(\beta_*\le7/8\) supplies its prerequisite. Under a contradiction to the
new boundary, all dynamic bins still satisfy \(\delta\le3/4\). No extension
of the allowed \(\kappa\) range and no capacity penalty proportional to a
positive \(\beta_*-7/8\) is used.

The source PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The [low audit](../reviews/LOW_STRUCTURAL_AUDIT_20261008.md),
[moment audit](../reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md), and
[contour audit](../reviews/CONTOUR_TRANSFER_AUDIT_20261008.md)
check the transfer to this geometry. These are scoped reviews by agents
using the same model. The moment review independently reconstructed
the polynomial certificate and checked the complete written derivation.

## Geometry and the low estimate

Put

\[
e=\frac1{6000},\quad
\ell=\frac16+e=\frac{1001}{6000},\quad b=\frac18,
\]
\[
l_x=\frac{1-\ell-b}{2}=\frac{4249}{12000},\quad
l_y=\frac{1-\ell+b}{2}=\frac{5749}{12000},\quad
h=1-l_x+\ell=\frac{3251}{4000}.
\]

Thus \(M=l_x+l_y=1-\ell\), \(M+\ell=1\), and \(l_y-l_x=b\).
The source's exact physical expression is retained, using the new positive
slot lengths with total \(\ell\); the finite slot system and windows are
chosen before the scale or target. The support primes vary with the scale.

The unspecialized row-energy computation, for a rescaled subset of total
length \(d\in[0,\ell]\), permits an excess

\[
\frac{(5\ell-1+d)_+}{4}
\]

in the squared row norm. After Cauchy--Schwarz and the source's rescaled
count and coefficient factor, its net contribution is

\[
f(d)=-d+\frac{(5\ell-1+d)_+}{8}\le0.
\]

Indeed \(\ell<1/5\); before the kink \(d=1-5\ell\) it equals \(-d\),
and after the kink it decreases with slope \(-7/8\). The endpoints and
kink prove the inequality on the whole interval. The Gram estimate has
strict slack because

\[
l_x-\ell>0,\qquad l_y-\ell>0,\qquad
l_y-\ell-\frac{11b}{6}>0.
\]

Equivalently, the last condition follows from
\(b<3(1-3\ell)/8\). The common low exponent is consequently

\[
L=\frac{l_x}{2}+\frac b{12}
=\frac{4499}{24000}=\frac3{16}-\frac1{24000}.
\]

The residue exponent is

\[
C(s)=s+\frac{l_x}{2}-1+\frac h6=s-\frac{11}{16},
\qquad C(\sigma)=L.
\]

Unlike the first displacement, this change preserves \(M+\ell=1\) and
the constant in the signal exponent. All other support, coefficient,
mask, height-uniformity, and common-normalization requirements still have
to be retained; the identities alone do not supply those requirements.

## Exact adaptive endpoint certificate

Use the source's crossing envelope with fixed \(\kappa=3/4\):

\[
\alpha=5/6,\quad x=q/\delta\in[0,1/2],\quad y=1/2-x,
\]
\[
D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),
\quad J=(\alpha-\delta)D_x+\delta P_x,
\]
\[
T=\frac{(\alpha-\delta)\delta P_x}{J},\qquad
R^*=1-\delta+T/2.
\]

Here \(0<\delta\le3/4<\alpha\) and \(J>0\). At row exponent \(d=h\),
the high exponent relative to the new low scale is

\[
E=h(R^*+1/2+\delta)-1-b(7/12+\delta/2)
  +\ell(q-1-\delta/2).
\]

Equivalently,

\[
E=-\frac14+\frac{5\ell}{4}+\frac b6
 -\delta\left(\frac b2+\ell y\right)
 +\frac{1+3\ell+b}{4}T.
\]

This formula is derived from the general exponent in source (10.15), not
from a specialized seven-eighths identity. Write

\[
p_y=7+18y+8y^2,\qquad
j_y=185+170y+(-138+12y+96y^2)\delta,
\]

so \(P_x=p_y/9\) and \(J=j_y/108\). The polynomial
\(N=10368J(-E)\) has the exact representation

\[
N=A(y)\delta^2+B(y)\delta+C(y),
\]

where the coefficient lists, in increasing powers of \(y\), are

| Polynomial | Exact coefficients |
| --- | --- |
| \(A\) | \(306126/125,\ 786048/125,\ 564168/125,\ 192192/125\) |
| \(B\) | \(-47352/25,\ -75386/25,\ -5204/25\) |
| \(C\) | \(3663/10,\ 1683/5\) |

The coefficients of \(D(y)=4A(y)C(y)-B(y)^2\) are

\[
\left(
\frac{467172}{625},\frac{680072136}{625},
\frac{3248881292}{625},\frac{884272016}{125},
\frac{1266754928}{625}
\right).
\]

They are all positive. More strongly, direct coefficient comparison gives

\[
D(y)\ge \frac{D(0)}{A(0)}A(y)\quad(y\ge0).
\]

The constant coefficient of the difference is zero and every remaining
coefficient is positive, as checked with exact rational arithmetic.
Completing the square proves

\[
N=\frac{(2A\delta+B)^2+D}{4A}
\ge\frac{D(0)}{4A(0)}=\frac{12977}{170070}.
\]

On the physical rectangle, \(0<P_x\le D_x\le3\), hence
\(J\le3\alpha=5/2\). Consequently

\[
-E\ge\frac{12977}{4408214400}
>\frac1{400000}.
\]

This certificate holds for the complete continuous rectangle. No numerical
mesh or floating-point extremum is used in the proof. In particular,
rounding and detector losses can be chosen to consume only a fixed fraction
of this positive margin.

## Other rows and the remaining margins

The floor bin has \(\delta=1/50\), \(R=1\), and \(q\le\delta/2\).
Its saving is

\[
m_{\rm floor}=\frac7{1200}-\frac{32e}{25}>0.
\]

For \(d\le1/2\), use the source's common exponent
\(R=76/75-2\delta/3\). At fixed row exponent the change is
\(e(1/100+a/2+q)\), at most \(329e/400\), because
\(a\le7/8\), \(q\le3/8\). The source's old middle bound, evaluated at
\(\delta\le3/4\), therefore gives

\[
m_{\rm middle}=\frac{241}{9600}-\frac{329e}{400}>0.
\]

For small rows retain \(d_{\min}=1/100\) and the conservative count
\(2d_{\min}\). The saving is

\[
m_{\rm small}=\frac{l_y}{2}
-h\left(\frac{17}{50}-\frac16\right)-\frac1{50}
=\frac{63}{800}-\frac{51e}{100}>0.
\]

The principal error margins remain

\[
m_w=l_y/20>0,\qquad m_z=h/600>0.
\]

Every listed margin exceeds \(1/400000\). The adaptive and floor frequency
slopes are positive, and less than two. Taking

\[
\zeta=\frac1{6400000}
\]

costs at most \(2\zeta\), while retaining
\(\ell/(h+\zeta)>1/5>7/37\). The existing fixed large-row contour can
then be chosen sufficiently far right. The enlarged Euler domain from the
initial extension still contains the new boundary, since
\(20999/24000>87/100\). Its local factors and pole locations do not
depend on these physical exponents. This last observation uses the separate
source audit; the rational certificate alone is not a contour proof.

As in the source and initial extension, choose all real losses, slot mesh,
and capacity decrements before the target, retaining a fixed fraction of
these margins and of \(\beta_*-\sigma\). Choose the permitted target height
only after the finite internal height orders, followed by external-tail
orders. Use the same final excluded set and the same normalization in the
physical sum and principal signal. Proposition 2.1 then supplies the
conditional contradiction.

## Size and limitation of the change

In the local [fixed-probe variance equivalence](../../prime-variance-exponents/manuscript.tex), this candidate corresponds
to

\[
\mathcal V_g(X)=O\!\left(X^{11/4-1/12000}\right),\qquad
\delta_{\rm variance}=\frac34-\frac1{12000}.
\]

There is a concrete obstruction to increasing \(\ell\) much further with
\(b=1/8\) and this same envelope. At \(y=0\), for arbitrary positive
\(e=\ell-1/6\), the discriminant complement is

\[
4A(0)C(0)-B(0)^2
=576\bigl(49-286020e-1162800e^2\bigr).
\]

Its positive root lies strictly between
\(1711975385/10^{13}\) and \(1711975386/10^{13}\), approximately
\(0.0001711975385\). At that root the quadratic vanishes at

\[
\delta_*=
\frac{1896-11520e}{2(2448+6048e)}\approx0.386688531,
\]

inside the active bin interval. Thus strict endpoint negativity genuinely
fails there for this parameter family and chosen moment envelope. The
corresponding limiting boundary is approximately \(0.8749572006154\).
This is not a universal limitation on the mathematics: it does not rule out
better moment counts, a different geometry, or additional arithmetic input.
The present rational candidate deliberately leaves a positive margin.

The companion [exact check script](../numerics/check_geometry_optimization.py) verifies the algebra,
coefficientwise certificate, all stated rational margins, and a rational
interval enclosing this root, using only the Python standard library. Its
[JSON output](../numerics/geometry_optimization_check.json) retains the small exact record. Numerical exploration
helped choose the candidate but is not retained as proof evidence.
