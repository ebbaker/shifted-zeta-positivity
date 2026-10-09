# A complete small-cofactor pairing that retains the coherent power

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: a selected signed-response obstruction under the already imported
fixed-field prime ideal theorem. No bound for the full retained response
is proved. Same-model audits and finite checks are internal validation,
not independent specialist review or formal proof verification.

This follows the bounded task in
[note 23](23_SHORT_FAMILY_PARITY_CONTINUATION_20261008.md): sum complete
small-cofactor channels before taking absolute values, allowing actual
semiprimes and odd-total-product compensation in one nonzero response.
The complete divisor cofactor sum considered here fails to save a power,
even when its maximum norm grows through a fixed power of the main scale.
This is a rigorous obstruction to that particular pairing, not a lower
bound for the complete squarefree tail.

## 1. An actual signed product block

Use the manuscript's good ideal monoid, physical zero extensions, and
\[
 H=D^{2/5},\qquad z=\sqrt{CD},\qquad
 Y_u=D^{9/20}/L_u.
 \tag{1}
\]
The obstruction specializes to the permitted trivial fixed twist
\(\nu=1\). Let \(W\in C_c^\infty((c,C))\), \(0<c<C\), be fixed,
complex, nonzero, and have zero integral. Let \(M\) be any squarefree
good ideal. It may depend on \(D\), subject to
\[
 NM\le D^\beta,\qquad 0<\beta<1/20
 \tag{2}
\]
for a fixed \(\beta\). In particular a fixed \(M\), including the
unit, is allowed.

Define the row-independent total-product set
\[
 \mathcal P_M(D)=\{bqr:b\mid M,\ q,r\text{ distinct good primes},\
       Nq,Nr\le z,\ (qr,M)=1\}.
 \tag{3}
\]
The unordered pair \(\{q,r\}\) and divisor \(b\) are determined
uniquely by a member of this set. All factors are squarefree and pairwise
coprime. Define its actual projected response by
\[
 \mathcal B_{u,M}(D)=
 \sum_{n\in\mathcal P_M(D)}t_{Y_u}(n)\lambda_u(n)W(Nn/D),
 \quad
 t_Y(n)=\mu_K(n)+\sum_{\substack{d\mid n\\Nd\le Y}}
                                      (-2)^{\omega(d)}.
 \tag{4}
\]
The coefficient identity is valid on the profile for sufficiently large
\(D\), since every actual \(Y_u\le D^{9/20}<z\).

For \(u=v^6\), \(0<Nv\le D^{1/15}\), and \((v,M)=1\), the
radical comparison gives
\[
 Y_{v^6}\gg D^{23/60}>NM\ge Nb.
 \tag{5}
\]
Every contributing prime in (3) also satisfies
\[
 Nq,Nr\ge \frac{cD}{Nb\,z}
       \ge \frac{c}{\sqrt C}D^{1/2-\beta}
       >D^{9/20}\ge Y_{v^6}
 \tag{6}
\]
for sufficiently large \(D\), uniformly in \(M\). Therefore precisely
the divisors of \(b\) occur in the low prefix in (4), and
\[
 t_{Y_{v^6}}(bqr)=2\mu_K(b).
 \tag{7}
\]
All physical phases are one: the condition \((v,M)=1\) treats every
prime of \(b\), and (6) implies \(q,r\nmid v\). Thus the original
zero extensions have been retained, rather than replaced on a row where
they might vanish.

Since ordered distinct prime pairs count each product twice, (7) gives
the exact identity on these coherent rows
\[
 \mathcal B_{v^6,M}(D)=\mathcal P_{M,W}(D),\qquad
 \mathcal P_{M,W}(D)=\sum_{b\mid M}\mu_K(b)
      \sum_{\substack{q\ne r\ \mathrm{good}\text{ primes}\\Nq,Nr\le z}}
                  W(Nb\,Nq\,Nr/D).
 \tag{8}
\]
The condition \((qr,M)=1\) in (3) is automatic in the inner sum on
the profile: (6) gives \(Nq,Nr>NM\). Equation (8) includes the
semiprimes \(b=1\), negatively signed triple products for prime
\(b\mid M\), and every higher divisor cofactor of \(M\) with its
actual sign. It is a nonzero signed combination. In particular this is
not an additional coefficient-zero sector.

## 2. Uniform prime-pair continuum with the complete cutoffs

Write
\[
 B=\log z,\qquad v(t)=\log(C/t),\qquad
 F_B(v)=\frac{2}{2B-v}\log\frac{B}{B-v}.
 \tag{9}
\]
Use only the already imported fixed-field prime ideal theorem
\[
 \pi_K(x)=\operatorname{Li}(x)+O_K(xe^{-c_K\sqrt{\log x}}).
 \tag{10}
\]
All norms in the two prime sums are at least a fixed constant times
\(D^{1/2-\beta}\), so its error is uniform in the present range. No
growing-character prime ideal theorem is being asserted.

For each \(b\mid M\), two partial summations give
\[
 \sum_{\substack{q,r\ \mathrm{good}\text{ primes}\\Nq,Nr\le z}}
 W(Nb\,Nq\,Nr/D)
 =\frac{D}{Nb}\int_c^C W(t)F_B(v(t)+\log Nb)\,dt
  +O_{\beta,W}\left(\frac{D}{Nb}e^{-c_\beta\sqrt{\log D}}\right).
 \tag{11}
\]
Here the prime-square diagonal is included. For clarity about uniformity,
fix \(x=Nq\) and sum over the other prime. One-variable partial
summation gives error
\(O_W(D/(Nb\,x)e^{-c_\beta\sqrt{\log D}})\), because the support
in the other norm has a fixed ratio and all of it exceeds
\(D^{1/2-\beta}\) up to a fixed constant. Summing \(1/Nq\) costs
at most \(O(\log D)\), absorbed by decreasing \(c_\beta\).
For the remaining continuous function
\[
 G_b(x)=\int_2^z W(Nb\,xy/D)\,\frac{dy}{\log y},
\]
the nonzero support has \(y\gg D^{1/2-\beta}\); the artificial
lower endpoint \(2\) removes no supported contribution. Its bounds are
\[
 |G_b(x)|\ll_W\frac{D}{Nb\,x\log D},\qquad
 |G_b'(x)|\ll_W\frac{D}{Nb\,x^2\log D}.
\]
They make the second partial-summation error in (11) uniform as well.
The fixed excluded primes are absent from these supports eventually.

To compute its main term, set \(xy=Dt/Nb\) and then
\(x=ze^{-s}\). The exact inner integral is
\[
 \int_0^{v(t)+\log Nb}
 \frac{ds}{(B-s)(B-v(t)-\log Nb+s)}
       =F_B(v(t)+\log Nb).
 \tag{12}
\]
Both denominators are positive. Under (2), the argument of \(F_B\)
is at most \(\beta\log D+O_W(1)<B\). The lower and upper prime
cutoffs in (11) have therefore not been replaced by an unrestricted
product Dirichlet series.

Removing the diagonal from the sum over all \(b\mid M\) costs at
most
\[
 O_W\left(\sqrt D\sum_{b\mid M}(Nb)^{-1/2}\right)
       =O_{\varepsilon,\beta,W}(D^{1/2+\varepsilon}),
 \tag{13}
\]
by the ideal divisor bound. This is negligible compared with every fixed
logarithmic order of \(D\).

## 3. Why the complete signed cofactor inverse leaves a main term

Let \(k_0\ge1\) be the first nonzero logarithmic profile moment:
\[
 M_j(W)=\int_c^C W(t)v(t)^j\,dt,\qquad
 M_j(W)=0\ (0\le j<k_0),\qquad M_{k_0}(W)\ne0.
 \tag{14}
\]
Such a finite \(k_0\) exists for every nonzero complex \(W\) of
zero integral, by the polynomial-density argument in note 16. This does
not require \(W\) to be real or nonnegative.

The exact kernel has the convergent expansion
\[
 F_B(v)=\sum_{k\ge1}\alpha_k\frac{v^k}{B^{k+1}},\qquad
 \alpha_k=\sum_{j=1}^k\frac{2^{-(k-j)}}j>0.
 \tag{15}
\]
For growing \(M\), a uniform Taylor argument is preferable to treating
\(\log Nb\) as a fixed constant. On
\(0\le l\le\beta\log D\), all relevant arguments are a fixed
fraction below \(B\), so
\[
 F_B^{(k_0+1)}(l+v)=O_{\beta,W,k_0}(B^{-k_0-2}).
\]
Taylor expansion in the bounded variable \(v\), followed by (14),
and then comparison of \(F_B^{(k_0)}(l)\) with its value at zero,
gives uniformly
\[
 \int_c^C W(t)F_B(v(t)+l)\,dt
 =\frac{\alpha_{k_0}M_{k_0}(W)}{B^{k_0+1}}
  +O_{\beta,W}\left(\frac{1+l}{B^{k_0+2}}\right).
 \tag{16}
\]

Define the finite Euler products and logarithmic moment
\[
 P_-(M)=\prod_{p\mid M}(1-(Np)^{-1}),\qquad
 Z_+(M)=\prod_{p\mid M}(1+(Np)^{-1}),
 \qquad S(M)=\sum_{p\mid M}\frac{\log Np}{Np+1}.
 \tag{17}
\]
Exact divisor expansion yields
\[
 \sum_{b\mid M}\frac{\mu_K(b)}{Nb}=P_-(M)>0,
 \quad
 \sum_{b\mid M}\frac1{Nb}=Z_+(M),
 \quad
 \sum_{b\mid M}\frac{\log Nb}{Nb}=Z_+(M)S(M).
 \tag{18}
\]
Combining (11), (13), (16), and (18), before taking an absolute value,
proves
\[
 \mathcal P_{M,W}(D)=
 \frac{D\alpha_{k_0}M_{k_0}(W)P_-(M)}{B^{k_0+1}}
 +O_{\beta,W}\left(
      \frac{D Z_+(M)(1+S(M))}{B^{k_0+2}}
      +D Z_+(M)e^{-c_\beta\sqrt{\log D}}\right)
 +O_{\varepsilon,\beta,W}(D^{1/2+\varepsilon}).
 \tag{19}
\]
The inverse \(\sum_{b\mid M}\mu_K(b)=0\), when \(M\ne1\),
is not the inverse needed by this continuum. Rescaling the total product
by \(Nb\) supplies its essential Jacobian \(1/Nb\). Its complete
signed sum is the positive Euler factor \(P_-(M)\), not zero.

For fixed \(M\), (19) immediately has a nonzero leading coefficient.
The result is uniform for growing \(M\) in (2) as well. To see this,
split its prime divisors at \(T=\log D\). Partial summation from
(10) gives
\[
 \sum_{Np\le T}(Np)^{-1}=\log\log T+O(1),\qquad
 \sum_{Np\le T}\frac{\log Np}{Np}=\log T+O(1).
 \tag{20}
\]
For primes of \(M\) above \(T\), use
\(\sum_{p\mid M}\log Np=\log NM\le\beta\log D\) to get
\[
 \sum_{\substack{p\mid M\\Np>T}}(Np)^{-1}
     \le\frac{\beta\log D}{T\log T},\qquad
 \sum_{\substack{p\mid M\\Np>T}}\frac{\log Np}{Np}
     \le\frac{\beta\log D}{T}.
 \tag{21}
\]
Consequently, uniformly under (2),
\[
 P_-(M)\gg_\beta(\log\log D)^{-1},\qquad
 \frac{Z_+(M)}{P_-(M)}\ll_\beta(\log\log D)^2,
 \qquad S(M)\ll_\beta\log\log D.
 \tag{22}
\]
The first error in (19), relative to its nonzero main term, is
\(O_{\beta,W}((\log\log D)^3/\log D)=o(1)\). The other errors
are smaller, choosing any fixed \(\varepsilon<1/2\) in (13).
Thus
\[
 |\mathcal P_{M,W}(D)|
 \gg_{\beta,W}\frac{D P_-(M)}{(\log D)^{k_0+1}}
 \tag{23}
\]
uniformly for every \(M\) in (2). All prime-counting estimates in
this argument are untwisted and over the fixed field.

## 4. Complete row-weight obstruction and its limitations

Put \(X=H^{1/6}=D^{1/15}\). Elementary Eisenstein lattice counting
and finite divisor inclusion-exclusion give
\[
 \#\{0<Nv\le X:(v,M)=1\}
 =\kappa_K X P_-(M)
  +O_K\left(\tau(M)(\sqrt X+1)\right).
 \tag{24}
\]
Indeed the count in the principal ideal \(d\) is
\(\kappa_K X/Nd+O_K(\sqrt{X/Nd}+1)\), uniformly in \(d\).
The ideal divisor bound gives \(\tau(M)\ll_{\varepsilon,\beta}
D^\varepsilon\). Choose \(\varepsilon<1/30\); (22) makes the
error in (24) smaller than the main term. The sixth-power map has at
most six preimages per nonzero element, and \(\Phi\ge1\) on the
inner norm ball. Equations (8), (23), and (24) therefore prove
\[
 \boxed{
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|\mathcal B_{u,M}(D)|^2
 \gg_{\beta,W,\Phi}
 \frac{D H^{1/6}P_-(M)^3}{(\log D)^{2k_0+2}}
 \gg_{\beta,W,\Phi}
 \frac{D^{16/15}}
      {(\log D)^{2k_0+2}(\log\log D)^3}.}
 \tag{25}
\]
For fixed \(M\), the extra \((\log\log D)^3\) denominator may
be omitted, with constants depending on \(M\). Every fixed nonzero
zero-integral profile leaves the power \(16/15\). Higher derivative
profiles only move \(k_0\), as in note 16.

This is a selected sum of squares of an actual product projection. It
does not discard cross terms from the full squarefree tail. Writing
\(T_{u,\mathrm{sf}}=\mathcal B_{u,M}+\mathcal R_{u,M}\) leaves
an uncontrolled signed cross term. The remaining total products can
therefore compensate (25). In particular, the balanced triples of
note 23, with three prime norms near \(D^{1/3}\), are outside (3):
their smallest cofactor cannot divide an \(M\) of norm at most
\(D^\beta\), \(\beta<1/20\). Their required low-conductor
compensation has not been estimated here.

The conclusion is specific and useful for reassessment: complete divisor
cofactor resummation on a fixed or power-growing small ideal, even with
the genuine Möbius signs and semiprime/triple pairing retained, cannot
be charged separately to the proposed \(D^{4/5+\varepsilon}\)
budget. The source of the failure is quantified by (18)--(22), rather
than inferred from a positive kernel alone. No contraction for the
nonzero full signed combination has been found. The short-family route
now needs a coupling involving broader total-product ranges or an
additional conductor-uniform arithmetic estimate; the parallel
mixed-character route should be reassessed as prescribed by note 23.

## 5. Verification and source status

The [standard-library checker](../../numerics/check_short_family_cofactor_pairing.py)
compares original ordered truncated-convolution tuples with (7), retains
distinct equal-norm prime symbols and exact sixth-root phases/deletion
zeros, and verifies the dilation Euler products, weighted Jacobian,
translated first moments, free/complement coefficients and rational
support margins. Two fresh runs match the
[record](../../numerics/short_family_cofactor_pairing_record_20261008.json)
byte for byte: 3,289 assertions, 27 actual pairing cases and 108
phase/deletion checks. Record SHA-256:
`ea54f5736dce0ab5358ff588b6df1715925f94fb7f74d0aa137951e5a59b083d`.
The [scoped review](../../reviews/SHORT_FAMILY_COFACTOR_PAIRING_REVIEW_20261008.md)
audits the uniform errors and the full-response limitation. The theorem
and proof are incorporated in the existing manuscript.

No finite test proves (10), the asymptotic use of partial summation,
lattice asymptotics, conductor comparison, or an unbounded moment. These
retain their already declared manuscript source status. The new result
uses the fixed-field prime ideal theorem only; it makes no integer-to-
ideal transfer and assumes no new Möbius or Hecke zero-free estimate.
The full \(4/5\) moment and its conditional scalar consequences remain
open.

See [note 16](16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md) for the
prime-pair kernel and all-fixed-profile moment argument,
[note 21](21_SHORT_FAMILY_ROUGH_PARITY_20261008.md) for saturated
coefficients, and [note 23](23_SHORT_FAMILY_PARITY_CONTINUATION_20261008.md)
for the preceding research task, and
[note 26](26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md) for the new
handoff and mixed-family reassessment.
