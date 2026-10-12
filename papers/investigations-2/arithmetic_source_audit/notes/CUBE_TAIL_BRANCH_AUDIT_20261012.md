# A nonempty cube-tail branch through both Poisson transforms

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. The exact serving
variant and configured reasoning effort are not exposed and are not
inferred. This is an internal mathematical audit, not independent
specialist validation or formal verification.

## Source and scoped result

All source lines refer to the manuscript dated 5 October 2026,
[`paper2.tex` at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
See the [provenance record](source_provenance_20261012.json).

**Scoped result:** an explicit squarefree-column input has a genuinely
nonzero cube-tail term, and explicit individual Fourier kernels survive
both transforms. The displayed two-Poisson calculation returns to the
declared energy class, with the masks, normalization and derivative costs
below. The row parameter strictly decreases. No gap was found in this
branch's algebra or recurrence bookkeeping in this read-through.

This is conditional analytic closure: the short-cube estimate uses the
source's completed theta estimate `prop:R`. Its proof, the arithmetic
identities and their external inputs are not independently proved by this
note. Nor does a populated individual Fourier kernel imply that a full
signed off-diagonal sum is nonzero. This note makes neither inference.
The source audit must separately establish the imported theta and sieve
interfaces and their uniformity before treating the claimed saving as
validated.

## 1. An actual coefficient profile and nonzero tail

Use `K=Q(sqrt(-3))`, `O=Z[omega]`, the principal original twist, and `S`
consisting of the primes above 2 and 3. This is an allowed choice under
source lines 665–667. Use the principal ray character `xi=1` as one member
of the energy family, retaining all ray characters generated later.

Choose the primary prime

\[
b=1+3\omega,\quad N(b)=7,\qquad
D=X=7^6=117649,\quad \mathcal H=7^5=16807,
\quad F=1,\quad \Sigma=XF=X.
\]

Thus `H/Sigma=1/7=D^(-1/6)`; `C0=1` and `kappa=1/6` are admissible for
the canonical estimate. The squarefree auxiliary interval `1<=N(f)<2`
contains only `f=1`.

Let `eta` be a nonnegative smooth bump supported in `(-1/4,1/4)`, with
`eta(0)=1` and `||eta||_infinity<=1`. Set

\[
 I=[9/10,11/10],\qquad
 W(y)=\eta(343y-361)+\tfrac1{10}\eta(343y-331).
\]

This is a fixed smooth compactly supported test in `I`. At the tail scale
`L=343`, only columns of integral norms 361 and 331 survive. The only
squarefree ideal of norm `361=19^2` is `(19)`: 19 splits and the other
ideals of that norm are squares of its prime factors. There are exactly
two ideals of norm 331, both prime; primary generators are
`10+21*omega` and `-11-21*omega`. All are prime to `S`.

The actual arithmetic profile, from source lines 800–812 and `eq:energy`
(945–952), is

\[
 a_1(n)=\overline{\alpha(n)}\gamma_2(n),\qquad
 c_{k,f}(n)=\mathbf1_{n\ {m squarefree},(n,S)=1}
 a_1(n)\chi_n(k)\chi_n(f)^4W(N(n)/343).
\]

The normalized primitive cubic Gauss sums have modulus one on these
columns. At the allowed row `k=1`, all sextic factors equal one, hence

\[
 \left|\sum_n^*a_1(n)W(N(n)/343)\right|
 =\left|a_1(19)+\tfrac1{10}
       \{a_1(10+21\omega)+a_1(-11-21\omega)\}\right|
 \ge 1-\tfrac2{10}=\tfrac45.
\]

In particular the tail energy is strictly positive. No conjecture about
Gauss-sum cancellation was used to select the input.

The cube cutoff and selected tail length are

\[
 H_c^3=X^2/\mathcal H^2=49,\qquad H_c=7^{2/3}<7,
 \qquad L_b=X/N(b)^3=343>1.
\]

In the source's grouped cube inversion, lines 1408–1434,

\[
 \beta_0(b,f)=\overline{\alpha(b)}^3\xi(b)^3
 \mathbf1_{(b,f)=1}
 \sum_{\substack{h\mid b\\N(h)>H_c}}\mu(h).
\]

Here `f=1`, the only qualifying divisor is `h=b`, and therefore
`beta_0(b,1)=-conj(alpha(b))^3`, of modulus one. The selected normalized
tail summand at `k=1` has magnitude at least `4/(5*7*sqrt(343))`.
This proves more than a nonempty supremum: the input to that supremum
has a nonzero coefficient sum and nonzero exterior coefficient.

The coefficient norms are explicit. For fixed `k,f`, the column support
has at most three elements, and at `k=f=1` its squared unweighted
coefficient norm after including `W` is `1+2/100=51/50`. For every `j`,

\[
 \|W\|_{C^j(I)}\le\tfrac{11}{10}
 \max_{0\le r\le j}343^r\|\eta^{(r)}\|_\infty.
\]

These are finite constants for this fixed profile. This finite witness
is not itself an asymptotic numerical test of a `D^epsilon` estimate.

## 2. A cutoff with surviving Fourier kernels

It is important to distinguish a nonzero cube-tail input from an
automatically empty Fourier range. The source leaves `Phi` selectable
before `eq:smoothed-energy` (1469–1481); the following allowed choice
makes the distinction concrete.

Take a real radial smooth Fourier bump `rho(w)` that is strictly positive
on `|w|<1/5` and vanishes outside that disk. Let `g` be its inverse Fourier
transform for the source's pairing
`e(z)=exp(4*pi*i*Im(z)/sqrt(3))`, and put `Phi(|z|^2)=A*g(z)^2`.
For `|z|<=1`, each phase has absolute value at most `4*pi/(5*sqrt(3))`,
which is less than `pi/2`. Symmetry therefore gives `g(z)>0` there.
Choose the positive constant `A` so `Phi>=1` on that disk.

Then `Phi` is nonnegative radial Schwartz, its Fourier transform is the
positive convolution of the two bumps, and

\[
 \operatorname{supp}\widehat\Phi\subset[0,4/25],\qquad
 \widehat\Phi(t)>0\quad(0\le t<4/25).
\]

Thus take `C_Phi=4/25` and `c_I=1`, since
`4*C_Phi*(11/10)^2=484/625<1`.

Use the coprime column pair `n1=19`, `n2=10+21*omega`, of norms 361
and 331. In the first transform select `C=t=d=1`, `f=1`, `h=1`.
Its Fourier argument is

\[
 \frac{\mathcal H}{361\cdot331}
 =\frac{16807}{119491}=0.14065494\ldots<\frac4{25}.
\]

Both weight factors are nonzero and this kernel survives. Its primitive
row character is `chi_19*conj(chi_(10+21*omega))`, with conductor the
product of these coprime squarefree ideals; zero extension retains all
its local nonunit restrictions.

For `C=t=d=1`, the positive intermediate family has

\[
 \ell=343,\quad w_{1,1}=1/7,\quad Y_{1,1}=2401.
\]

In the second transform take `g=e=w=1`, `h=1`, so
`r=f'=k'=1`. For the same two column norms the Fourier argument is

\[
 \frac{Y_{1,1}}{361\cdot331}
 =\frac{2401}{119491}=0.02009356\ldots<\frac4{25}.
\]

For example `U=W` is an allowed test in the intermediate family, and
this second kernel also survives. At `y=1`, each intermediate ray twist
has `|P(1;W)|>=4/5`, by the same one-large-term bound as above (with
Möbius and ray factors of modulus one). At least one coefficient in each
finite ray expansion is nonzero. This establishes populated intermediate
forms and individual transformed kernels, without claiming that their
entire signed off-diagonal sums escape cancellation.

The first witness uses the actual input `W`. The second witness uses
`U=W` as one member of the common intermediate test class, for which the
bound must hold for **every** `U`. It is not asserted to be a particular
Mellin mode produced by separation of the original first kernel. The
inequality transporting that original kernel is the uniform
`lem:smooth-mean-square` estimate, with its explicit derivative and
integration costs below; the scalar witness is not used to reconstruct
the original kernel.

## 3. Cube removal and first Poisson ledger

The complete multiplicative twist is

\[
 \Psi_k(n)=\xi(n)\chi_n(k)\chi_n(f)^4
 \quad((n,S)=1),\qquad \Psi_k(n)=0\quad((n,S)>1).
\]

Its zeros are part of the definition (`eq:completed-twist`, 1303–1310).
In `eq:cube-inverse` (1360–1374), expanding the completed sum and grouping
by total cube index produces `sum_(h|b) mu(h)`. No coprimality between
the cube index and the squarefree column is imposed. In the tail,

\[
 \Psi_k(b)^3=\xi(b)^3\chi_b(k)^3\mathbf1_{(b,f)=1}.
\]

The exterior row factor has modulus at most one, rather than identically
one; discarding it in an upper bound is legitimate. The column zeros
`(n,kfS)>1` remain. The divisor norm `|beta_0|<=tau_div(b)` and
`sum tau_div(b)/N(b) << log^2(2+X)` are the only cube recombination
losses (1430–1455). Terms `L_b<=1` are handled separately by counting,
not returned to the recursion (1456–1467).

For a general retained tail scale `L`, the first transform is
`lem:first-transfer`, lines 2230–2349. Expanding the square extracts
`C=(n1,n2)`, leaving coprime squarefree columns `u1,u2`, both prime to
`C`. Consequently `chi_u1*conj(chi_u2)` is primitive modulo `u1*u2`.
The common factor creates the row restriction `(k,C)=1`, and primitive
Poisson introduces `d|C`. The principal primitive case is exactly
`u1=u2=1`; its zero mode is retained as `Z << H*||W||_infinity^2`.

The arithmetic conversion `eq:paired-first-gauss` (2284–2290), followed
by finite ray decomposition and the identity
`1_((u1,u2)=1)=sum_(t|u1,t|u2) mu(t)`, yields `u_i=t*x_i`. The
restriction `(x_i,t)=1` remains; pairwise coprimality of `x1,x2` does
not. The actual resulting profile (`eq:P`, 2246–2251) is

\[
 p_y(n)=\mu(n)\xi_1(n)\mathbf1_{(n,t)=1}
 \overline{\chi_n(y)}\chi_n(C)^4\chi_n(d),
 \qquad \ell=\frac L{N(C)N(t)}.
\]

All columns are still separately squarefree, primary and prime to `S`.
The zero-extended `chi_n(C)^4` retains `(n,C)=1`, and
`overline(chi_n(h*f^2))` retains the original frequency and auxiliary
zeros. This is a Möbius coefficient family at this intermediate stage;
it is not prematurely identified with `eq:energy`.

The exact first kernel and outer coefficient are

\[
 \mathscr K_h(z_1,z_2)=(z_1z_2)^{-1/2}W(z_1)\overline{W(z_2)}
 \widehat\Phi\left(\frac{\mathcal H N(h)N(C)^2}
 {L^2N(d)z_1z_2}\right),\qquad
 w_{C,d}=\frac{\mathcal H N(C)}{N(d)L^2F}.
\]

The first frequency bound is
`N(h)<=C_Phi*v^2*L^2*N(d)/(H*N(C)^2)`. The map `y=h*f^2` has
divisor-bounded multiplicity; `Sigma>=LF` allows enlargement to

\[
 Y_{C,d}=c_I\frac{\Sigma LF N(d)}{\mathcal H N(C)^2}.
\]

The positive form `Q_xi1(U)` then contains **all** permitted squarefree
`C,t`, all `d|C`, and all rows `y`, with weight `Phi(N(y)/Y_Cd)`.
No original Fourier-support restriction is retained on the outer
`C,t,d` domain (source 2259–2261). This enlargement is essential for
the later exact preimage cancellation. It is performed after conversion
to a nonnegative form, not on a signed summand by termwise comparison.

## 4. Second Poisson, masks, and class return

`lem:arithmetic-poisson`, source lines 2353–2493, applies for arbitrary
positive `ell,Y`; in particular it does not require `Y>=1`. Extract
`g=(n1,n2)`, and apply primitive Poisson to
`conj(chi_z1)*chi_z2` with the exclusion `(y,g)=1`. The zero frequency
is retained and bounded by `Y*ell*||U||_infinity^2` (2400–2420).
For nonzero frequencies `e|g` comes from that exclusion. The identity

\[
 \chi_z(dh)\overline{\chi_z(e)}\chi_z(C)^4
 =\chi_z(deh)\chi_z(Ce)^4
\]

preserves the zero extension: `d|C`, `e|g`, and the original support
already forces the relevant coprimalities. A second Möbius insertion
`z_i=w*n_i` removes `(z1,z2)=1`. Squarefreeness leaves the mask
`(n,gCtw)=1`. The CRT coefficient law adds `chi_n(w)^4`, so the exact
remaining profile is

\[
 a^\sharp(n)=a_{\xi'}(n)\mathbf1_{(n,tg/e)=1}
                  \chi_n(deh)\chi_n(Cew)^4.
\]

The indices satisfy `(g,Ct)=(w,gCth)=1`, `e|g`; hence

\[
 r=tg/e,\qquad f'=Cew,\qquad k'=deh
\]

give coprime squarefree `r,f'`, with `f'` prime to `S`, and an arbitrary
nonzero element row `k'`. The exact length, coefficient and Fourier
parameter become (2523–2555)

\[
 X'_0=\frac L{N(r)N(f')},\qquad
 w_{C,d}\frac{Y_{C,d}N(g)}{N(e)\ell}
   =\frac{c_I\Sigma N(r)}{L^2},\qquad
 \frac{Y_{C,d}N(h)N(g)^2}{N(e)\ell^2}
   =\frac{c_I\Sigma F N(k')N(r)^2}{\mathcal H L}.
\]

Thus neither coefficient amplitudes nor normalization are replaced by
an unspecified comparable expression. All intermediate arithmetic
factors have modulus at most one; the surviving divisor multiplicities
are allocated to `D^epsilon`.

For fixed `r,f',k'`, the kernel is identical for every preimage. At a
prime `p|f'`, the choices of placing `p` in `C,e,w`, including the two
possible placements in `d` when `p|k'`, have signed total

\[
 (1+\mathbf1_{p\mid k'})-\mathbf1_{p\mid k'}
       -\mathbf1_{p\nmid k'}=\mathbf1_{p\mid k'}.
\]

This is `lem:second-transfer`, lines 2556–2581. Taking absolute values
only after regrouping leaves the condition `f'|k'` and the factor
`tau_div(r)`. Dropping those signs earlier would not justify the
subsequent lower bound for child column length. The separate
[exact regrouping check](../numerics/check_transfer_regrouping.py) tests
this finite combinatorial identity; it does not prove the analytic
estimate.

On a dyadic block `R<=N(r)<2R`, `F'<=N(f')<2F'`, put

\[
 X'=\frac L{RF'},\quad \Sigma'=X'F'=\frac LR,
 \quad \mathcal H'=\frac{\mathcal H L}{\Sigma F R^2}.
\]

The surviving support implies `N(f')<=N(k')<=H*L/(Sigma*F*N(r)^2)`.
For every divisor `j|r`, this gives the needed nontrivial lower bound

\[
 \frac{X'}{N(j)}\ge
 \frac{\Sigma F N(r)^2}{\mathcal H R N(j)}
 \ge\frac{\Sigma F}{\mathcal H}\ge1.
\]

Therefore `lem:remove-exclusions` (963–991) is applicable with children
`(H',X'/N(j),F'*N(j))`. It retains the precise `a_xi'` profile, makes
the auxiliary index squarefree using its own zero-extended mask, and
preserves `X'*F'=Sigma'`. No forbidden column scale below one is passed
to the induction. The returned energies obey exactly

\[
 \mathcal H'\le\frac{\mathcal H L}{\Sigma F},\qquad
 \frac{\mathcal H'}{\Sigma'}=\frac{\mathcal H}{\Sigma FR}
       \le\frac{\mathcal H}{\Sigma},\qquad \Sigma'\le L.
\]

Since `X',F'>=1` and `X'*F'<=L<=D^C0`, each individual child scale
is also polynomially bounded by the same ambient `D^C0`.

The summed second zero mode is explicitly
`O(D^epsilon*Sigma*||U||_infinity^2)` (2658–2677), using
`sum_C tau(C)/N(C)^2<infinity` and the logarithmic reciprocal sum in
`t`. It is not discarded as a principal exception or fed back as an
unproved target estimate.

## 5. Smooth norms, contraction, and base case

The first kernel is supported in `I^2`; its derivatives of order `q`
are bounded by a constant times `||W||_(C^q(I))^2`. The intermediate
test class uses `I_*=[u/2,2v]`. In the second transform
`U_0(x)=x^(-1/2)U(x)` is harmless on this fixed interval. Rescaling
`1<=X'/X'_0<4` places the returned kernels in
`[u/8,2v]^2`, strictly inside `I'^2` for `I'=[u/16,4v]`
(2598–2617). No long Schwartz tail is relabelled as a compactly
supported column test.

`lem:smooth-mean-square`, source lines 3560–3619, uses a common
pointwise bound for Mellin coefficients before row Cauchy–Schwarz.
The integrable majorant is

\[
 \frac{(1+|s|)^m(1+|t|)^m}
 {(1+|s|+|t|)^{2m+4}}.
\]

Thus the second transform costs `2m+4` derivatives, and the first
costs `2*(2m+4)+4=4m+12`. After homogeneity, the returned scalar tests
have `C^m(I')` norm at most one, as required by the supremum in
`prop:transfer`. The coefficient norm here is an operator bound on the
specified smooth test class, not a claim that every separated Mellin
test has norm one without its compensating integration weight.

For a general nonempty cube branch, `Sigma=XF` and
`N(b)>Hc` give

\[
 \mathcal H'\le\frac{\mathcal H L_b}{\Sigma F}
  =\frac{\mathcal H}{N(b)^3F^2}
  <\mathcal H\left(\frac{\mathcal H}{\Sigma}\right)^2.
\]

If `H/Sigma<=D^(-kappa)` with fixed positive `kappa`, the row scale
contracts by `D^(-2*kappa)` while the same gap remains valid for
children. This is the actual decreasing parameter; it is not merely
a decrease in a normalized bound whose underlying scale could grow.
The base `H<=1` is the elementary count `E<<H*X*||W||_infinity^2`,
hence `E/Sigma<<||W||_infinity^2` since `F>=1` (1531–1547).

For the concrete branch in this note, every returned child satisfies

\[
 \mathcal H'\le49,\quad \Sigma'\le343,
 \quad \mathcal H'/\Sigma'\le1/7.
\]

If such a child has its own nonempty cube tail, its next transfer obeys
`H''<H'*(H'/Sigma')^2<=1`. Its returned supremum, which requires
`H''>=1`, is therefore empty. Consequently at most two applications
of the transfer reach an empty supremum in this selected branch.
Each short-cube contribution still requires `prop:R`; contraction
does not substitute for that theorem.

The general source induction has finite depth at fixed `kappa,C0`,
with derivative recurrence `J_new>=4*J_old+12` and the derivative
requirement of cube removal. Its order and constants may depend on
that depth and the fixed support intervals. Constants may also depend
on the fixed original character, `S` and the finite ray class group.
The positive exponent margin must remain uniform across the generated
energies. Allowing an unstated character-dependent loss to consume
`kappa` would invalidate the recurrence; the source statements retain
the margin explicitly.

## 6. Decision and remaining obligation

The selected branch does not return to the same target without a
decreasing parameter, does not drop the principal zero modes, and does
not visibly leave the declared smooth or arithmetic coefficient class.
The local signed preimage cancellation is indispensable and, with the
source's enlarged outer domain, consistent with the child lower bound.

The next decisive obligation is the completed bound `prop:R`, including
the theta transformation for these zero-extended twists and the
uniform reduction to the quadratic large sieve. A correct recurrence
plus that bound would explain how the completed-family saving reaches
the squarefree energy. The branch bookkeeping alone does not establish
the bound, the full imported baseline, or a stronger zero-free strip.
