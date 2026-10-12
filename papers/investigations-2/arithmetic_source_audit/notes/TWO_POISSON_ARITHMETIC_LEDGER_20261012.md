# Arithmetic ledger for both Poisson transfers

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. Exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical read-through, not independent specialist
validation or formal verification.

## Source hypotheses and scoped finding

The source is the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), `build/paper2.tex` at openai/math
revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, read from
`/private/tmp/arithmetic-source-audit-20261012/paper2.tex`. Its SHA-256
was reverified as
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Line references use these exact bytes.

The principal scope is physical lines 2217–2568: `lem:first-transfer`,
the universal `lem:arithmetic-poisson`, and the complete signed preimage
sum at the start of `lem:second-transfer`. The displayed summed zero
mode at 2653–2669 is also checked below. The existing single cube-tail
branch note was read for comparison; the calculations here quantify over
all permitted indices, rather than relying on that branch's witness.

The transfer assumes
\(1\le\mathcal H,L,F,\Sigma\le D^{C_0}\),
\(\max(\mathcal H,LF)\le\Sigma\), and a fixed nonnegative radial
Schwartz \(\Phi\), with \(\Phi\ge1\) on \([0,1]\) and
\(\operatorname{supp}\widehat\Phi\subset[0,C_\Phi]\).
All ideal columns are squarefree, primary and prime to fixed \(S\);
\(S\) contains the primes above 2 and 3 and the fixed ray conductors.
Divisor generators are chosen primary; row variables are actual elements
of \(\mathcal O\), including their unit associates. The inherited
arithmetic identities are the earlier scoped audit's classical CRT,
Gauss–Jacobi, inverse-Gauss and reciprocity inputs.

**Finding:** the two conversion identities, every shared-factor and
zero-extension mask, the first enlargement, and the full signed preimage
cancellation close under those inputs. The cancellation is complete for
arbitrary coprime squarefree \(r,f'\) and arbitrary nonzero element
\(k'\), including repeated prime powers in \(k'\), intersections of
\(k'\) with \(r\), and all unit-index cases. No substantive arithmetic
defect or unclosed arithmetic step was identified. The analytic smooth
separation, child energy estimate and recurrence remain distinct inputs;
this finding does not prove the whole theorem.

## Extracting the first common column factor

The input has coefficient \(a_\xi(n)\), row twist \(\chi_n(k)\),
auxiliary twist \(\chi_n(f)^4\), normalization \(1/(LF)\), and row
weight \(\Phi(N(k)/\mathcal H)\). On expanding its square, write
\(n_i=Cu_i\), where \(C=(n_1,n_2)\). Then
\((u_1,u_2)=(u_1u_2,C)=1\), and the coefficient CRT law is

\[
a_\xi(Cu_i)=a_\xi(C)a_\xi(u_i)\chi_{u_i}(C)^4.
\]

The common factor \(|a_\xi(C)|^2\) is 1. The other common factors give
exactly \(\mathbf1_{(k,C)=1}\) and \(\mathbf1_{(f,C)=1}\).
There is no residual \(G(C)\), angular factor, or ray twist at \(C\).
The primitive row character is
\(\chi_{u_1}\overline{\chi_{u_2}}\), of conductor exactly
\(u_1u_2\); it is principal only for \(u_1=u_2=1\).
Poisson with row exclusion \(C\) introduces \(d\mid C\), coefficient
\(\mu(d)\chi_{u_1}(d)\overline{\chi_{u_2}(d)}/N(d)\), and frequency
\(h\). No coprimality between \(h\) and \(C\) or \(d\) is required.

The principal zero mode is, before a harmless upper bound,

\[
\frac{\mathcal H\widehat\Phi(0)}{LF}
\sum_f^*\sum_C^*
\mathbf1_{(C,f)=1}|W(N(C)/L)|^2
\prod_{p\mid C}(1-N(p)^{-1}).
\]

Ideal counting bounds it by
\(O_I(\mathcal H\|W\|_\infty^2)\), as at lines 2280–2285.
The nonzero frequencies with \(u_1=u_2=1\) remain in the next formula.
Neither principal-character case is silently discarded.

## The first paired Gauss identity including the CRT phase

Put \(A(n)=\overline{\alpha(n)}\gamma_2(n)\). For coprime
squarefree \(u_1,u_2\), CRT gives

\[
\begin{aligned}
\gamma(\chi_{u_1}\overline{\chi_{u_2}})
&=\gamma_1(u_1)\gamma_{-1}(u_2)
\chi_{u_1}(u_2)\overline{\chi_{u_2}(u_1)}\\
&=\gamma_1(u_1)\gamma_{-1}(u_2)\mathcal R(u_1,u_2).
\end{aligned}
\]

The conversion identities and unit modulus give

\[
A(u_1)\gamma_1(u_1)=\mu(u_1)G(u_1),\qquad
\overline{A(u_2)}\gamma_{-1}(u_2)
=\mu(u_2)\chi_{u_2}(-1)\overline{G(u_2)}
=\mu(u_2)G(u_2^{-1}).
\]

Here \(u_2^{-1}\) is a ray-group inverse. Since \(\mathcal R\) is a
symmetric sign bicharacter, the product is exactly

\[
a_\xi(u_1)\overline{a_\xi(u_2)}
\gamma(\chi_{u_1}\overline{\chi_{u_2}})
=\mu(u_1)\mu(u_2)(\xi G)(u_1u_2^{-1}),
\]

the identity at lines 2288–2291. Expanding the fixed ray-group function
\((\xi G)(z)\) as \(\sum_{\xi_1}\ell_{\xi_1}\xi_1(z)\) produces
the *same* \(\xi_1\) in the two conjugate columns. Neither its
coefficients nor its finite index set depend on \(C,d,t,f,h\).

## First Möbius insertion and all masks

Once the paired conversion has been made on coprime columns, its new
coefficient expression is defined on all separately squarefree columns.
Apply \(\mathbf1_{(u_1,u_2)=1}=\sum_{t\mid u_1,u_2}\mu(t)\) to this
extension and write \(u_i=tx_i\). This does not invoke a primitive
Gauss-sum identity at noncoprime \(u_1,u_2\). Those terms cancel through
the exact Möbius identity.

Squarefreeness requires \((x_i,t)=1\), and \((C,t)=1\). The common
\(\mu(t)\xi_1(t)\) coefficient cancels against its conjugate. The
common character factor is

\[
|\overline{\chi_t(h)}\chi_t(f)^4\chi_t(C)^4\chi_t(d)|^2
=\mathbf1_{(h,t)=1}\mathbf1_{(f,t)=1},
\]

because \((t,C)=1\) and \(d\mid C\). Hence the surviving restrictions
are \((f,Ct)=1\), \((h,t)=1\), and the separate \((x_i,t)=1\)
masks. There is no remaining condition \((x_1,x_2)=1\), and no
condition \((h,C)=1\).

Combining the column auxiliary and dual row characters gives
\(\overline{\chi_x(h)}\chi_x(f)^4
=\overline{\chi_x(hf^2)}\), including every zero. Thus the exact
profile is

\[
p_y(n)=\mu(n)\xi_1(n)\mathbf1_{(n,t)=1}
\overline{\chi_n(y)}\chi_n(C)^4\chi_n(d),\qquad y=hf^2.
\]

The \(C\)-factor supplies \((n,C)=1\); it is still zero at a shared
prime after the fourth power. The \(d\)-factor is redundant for that
particular mask because \(d\mid C\), but its phase is needed in the
second Poisson output and cannot be omitted.

Put \(\ell=L/(N(C)N(t))\), \(z_i=N(x_i)/\ell\). The original
Poisson normalization is

\[
\frac{\mathcal H}{LF N(d)\sqrt{N(u_1)N(u_2)}}
=\frac{\mathcal H N(C)}{N(d)L^2F}\,(z_1z_2)^{-1/2}.
\]

This is exactly \(w_{C,d}(z_1z_2)^{-1/2}\), with no lost
\(N(t)\). The Fourier argument is
\(\mathcal H N(h)N(C)^2/(L^2N(d)z_1z_2)\), so the support gives

\[
N(h)\le\frac{C_\Phi v^2L^2N(d)}{\mathcal H N(C)^2}.
\]

The displayed outer range \(N(Ct)\le2vL\) includes all possibly
nonzero kernels; terms beyond the original support vanish through \(W\).
The later positive form deliberately has this entire outer domain.

## The first positive enlargement is universal

For fixed \(C,d,t\), if \(y=hf^2\ne0\), then \((f)^2\mid(y)\).
There is at most one actual element \(h=y/f^2\) for each chosen primary
\(f\). Thus the multiplicity is at most an ideal-divisor bound such as
\(\tau_{\rm div}((y))\). The restrictions on \(f,h\) only decrease
it; row unit associates are not identified.

The norm satisfies

\[
N(y)\le
\frac{4C_\Phi v^2L^2F^2N(d)}{\mathcal H N(C)^2}
\le c_I\frac{\Sigma LF N(d)}{\mathcal H N(C)^2}
=Y_{C,d},
\]

using \(\Sigma\ge LF\) and \(c_I\ge4C_\Phi v^2\). These image
norms are polynomial in \(D\), because \(N(d)\le N(C)\),
\(\mathcal H\ge1\), and \(L,F\le D^{C_0}\). The multiplicity cost
is therefore \(D^\varepsilon\), uniformly in the permitted indices.
If \(Y_{C,d}<1\), the nonzero image is empty: a nonzero integral
element has norm at least 1. This creates no exceptional branch.

Since \(\Phi\ge1\) on the image and is nonnegative, the positive sum
of squared *common-test* column sums is majorized by \(\mathcal Q\).
That form includes every \(C,t,d\) in its stated outer range and all
\(y\), including zero; it retains neither the first Fourier support
range nor the original \(f\)-shell as an outer restriction. This
enlargement is made on squared absolute values before the second
Poisson calculation. Retaining those first-stage restrictions would
invalidate the subsequent complete signed preimage count.

The first kernel has bounded derivatives on the fixed support because
\(\mathcal H N(h)N(C)^2/(L^2N(d))\le C_\Phi v^2\).
The smooth mean-square principle then transports that common-test bound
to the row-dependent coupled kernel. Verification of that analytic
principle is a separate audit; it is not replaced by pointwise positivity
of the coupled kernel.

## Second Poisson conversion at positive scales

The identity at lines 2407–2494 starts from the profile above at arbitrary
\(\ell,Y>0\). Its column support is finite, and the \(y\)-sum is
absolutely convergent by the Schwartz row weight. Write the old columns
as \(gz_i\), where \(g\) is their gcd. Their nonzero support gives

\[
(g,Ct)=1,\quad (z_1,z_2)=(z_1z_2,gCt)=1.
\]

The common factors at \(g\) have modulus 1 on this support and leave
exactly the row exclusion \((y,g)=1\). Poisson applies to the primitive
character \(\overline{\chi_{z_1}}\chi_{z_2}\), introducing
\(e\mid g\). Its zero mode is present exactly at \(z_1=z_2=1\):

\[
Z=Y\widehat\Phi(0)\sum_{(g,Ct)=1}^*
|U(N(g)/\ell)|^2\prod_{p\mid g}(1-N(p)^{-1}).
\]

Counting the finite columns gives \(|Z|\ll Y\ell\|U\|_\infty^2\).
If \(b\ell<1\) the columns are empty; otherwise the implied constant
may depend on the fixed upper support endpoint \(b\), so the count
\(O_b(\ell)\) is valid even when \(\ell<1\). No condition \(Y\ge1\)
is used. Principal nonzero frequencies remain.

The paired coefficient conversion is the earlier initial-Poisson
identity with the fixed quotient function
\(\xi_1(z)G(z^{-1})=\sum_{\xi'}c_{\xi'}\xi'(z)\). Hence it yields
\(\sum c_{\xi'}a_{\xi'}(z_1)\overline{a_{\xi'}(z_2)}\), with a
fixed character set independent of all preimage data. The remaining
sextic identity is

\[
\chi_z(dh)\overline{\chi_z(e)}\chi_z(C)^4
=\chi_z(deh)\chi_z(Ce)^4.
\]

At units it is the exponent congruence \(-1\equiv5\pmod6\); at
nonunits of any appearing factor both sides vanish. No inverse of zero
is taken. The support before inversion already has \((z,e)=1\), since
\(e\mid g\). The factor
\(U_0(x)=x^{-1/2}U(x)\) gives the exact normalization
\(N(g)/\ell\), so the nonzero exterior coefficient is
\(Y\mu(e)c_{\xi'}N(g)/(N(e)\ell)\).

## Second common-factor insertion and the exact remaining exclusion

Insert \(\sum_{w\mid z_1,z_2}\mu(w)\) and write \(z_i=wn_i\).
Squarefreeness imposes \((w,n_i)=1\), and the old exclusions give
\((w,gCt)=1\). The common CRT coefficient and characters yield

\[
|a_{\xi'}(w)\chi_w(deh)\chi_w(Ce)^4|^2
=\mathbf1_{(w,h)=1},
\]

because \(d\mid C\), \(e\mid g\), and \(w\) is prime to \(gC\).
This is the only required exclusion on the new frequency \(h\). It
may share factors with \(g,e,C,d,t\). In particular \((e,h)=1\)
and \((d,h)=1\) are not assumptions.

The extra CRT factor is \(\chi_n(w)^4\). The equivalence

\[
\mathbf1_{(n,gCtw)=1}\chi_n(deh)\chi_n(Cew)^4
=\mathbf1_{(n,tg/e)=1}\chi_n(deh)\chi_n(Cew)^4
\]

holds exactly: \(C,e,w\) are excluded by the auxiliary fourth power,
and \(g/e,t\) remain in the explicit mask. The sets are disjoint under
the stipulated squarefreeness and coprimalities. The new profile is

\[
a^\sharp(n)=a_{\xi'}(n)\mathbf1_{(n,tg/e)=1}
\chi_n(deh)\chi_n(Cew)^4.
\]

There is no remaining pairwise coprimality of \(n_1,n_2\). The masks
for their individual squarefreeness, fixed \(S\), and the new exclusion
remain. The coefficient class is precisely the allowed energy class
with an exclusion, not an arbitrary-coefficient enlargement.

The broad finite ranges are \(N(gw)\le b\ell\) and
\(N(h)\le C_\Phi b^2\ell^2N(e)/(YN(g)^2)\). They follow from the
column and Fourier supports and discard only zero kernels. They do not
add a hidden coprimality or frequency restriction.

## The return variables and exact common normalization

Specialize back to \(\ell=L/(N(C)N(t))\) and \(Y=Y_{C,d}\), and set

\[
r=tg/e,\qquad f'=Cew,\qquad k'=deh.
\]

Then \(r,f'\) are coprime squarefree ideals prime to \(S\),
\(k'\ne0\) is an unrestricted element, and the exact individual
column scale is

\[
X'_0=L/(N(r)N(f')).
\]

Direct cancellation gives, uniformly in every preimage,

\[
w_{C,d}\frac{Y_{C,d}N(g)}{N(e)\ell}
=\frac{c_I\Sigma N(r)}{L^2},\qquad
\frac{Y_{C,d}N(h)N(g)^2}{N(e)\ell^2}
=\frac{c_I\Sigma F N(k')N(r)^2}{\mathcal H L}.
\]

No comparable normalization or divisor-dependent weight replaces these
equalities. In particular the factors of \(d\) cancel from the
coefficient, making the later two choices of \(d\) equal in magnitude.

The common kernel's nonzero support implies

\[
N(r)N(f')\le2vL,\qquad
N(k')\le\frac{4C_\Phi v^2}{c_I}
\frac{\mathcal HL}{\Sigma F N(r)^2}
\le\frac{\mathcal HL}{\Sigma F N(r)^2}.
\]

The bound \(c_I\ge4C_\Phi v^2\) is used here in addition to its
earlier role in the first enlargement.

## Completeness of the signed preimages for arbitrary indices

Fix arbitrary coprime squarefree \(r,f'\), both prime to \(S\), and
an arbitrary nonzero element \(k'\). All algebraic preimages, and only
those preimages, are obtained by choosing

\[
t\mid r,\quad f'=Cew\text{ disjoint},\quad e\mid k',\quad
(w,k')=1,\quad d\mid(C,k'),
\]

and setting \(g=e(r/t)\), \(h=k'/(de)\).

To see sufficiency, \(r\) squarefree makes \(t\) and \(r/t\)
coprime. The disjoint squarefree factorization of \(f'\), together
with \((r,f')=1\), implies \((C,t)=1\), \((g,Ct)=1\), and
\((w,gCt)=1\). Since \(d,e\) are coprime divisors of \(k'\), their
product divides the actual element \(k'\), and \(h\) is integral.
As \(w\) is prime to \(de\), \((w,h)=1\) is equivalent to
\((w,k')=1\). Necessity follows by recovering \(t\), the partition of
\(f'\), \(e\) and \(d\) from the original output. This proves the
bijection, retaining row units.

No prime of \(k'\) needs valuation at least 2. A prime of \(f'\) is
in only one of \(C,e,w\), so it cannot divide both \(d\) and \(e\).
Repeated powers in \(k'\) merely occur in \(h\), which is allowed to
intersect \(d,e\). Primes dividing \(r\) and \(k'\) likewise occur in
\(h\) regardless of their placement in \(t\) or \(g/e\); no old
restriction forbids them. Primes of \(S\) in \(k'\) impose no additional
restriction on the ideal indices. All formulas include unit ideals.

For every preimage, \(Ctgw=rf'\). Thus on nonzero common support,
\(N(Ct)\le N(rf')\le2vL\), so *all* algebraic preimages belong to
the enlarged outer domain. Also \(N(gw)\le2v\ell\) is equivalent to
\(N(rf')\le2vL\), and the old frequency bound, after multiplication
by \(N(d)N(e)\), is exactly the common bound on \(N(k')\) above.
Consequently no preimage is lost through a preimage-dependent support
condition. Outside this common support, the kernel is zero for every
preimage and the regrouping still holds.

The \(t\)-choices are independent and contribute \(\tau_{\rm div}(r)\).
For each prime \(p\mid f'\), let \(\delta_p=\mathbf1_{p\mid k'}\).
The signed local counts are

| Placement | Allowed cases and sign | Signed count |
| --- | --- | --- |
| \(p\mid C\) | \(p\nmid d\) always; \(p\mid d\) when \(\delta_p=1\); both positive | \(1+\delta_p\) |
| \(p\mid e\) | Requires \(\delta_p=1\); sign from \(\mu(e)\) | \(-\delta_p\) |
| \(p\mid w\) | Requires \(\delta_p=0\); sign from \(\mu(w)\) | \(-(1-\delta_p)\) |

Their sum is \(\delta_p\). Independence across the disjoint prime
placements gives the universal total

\[
\sum_{\text{all preimages}}\mu(e)\mu(w)
=\tau_{\rm div}(r)\prod_{p\mid f'}\delta_p
=\tau_{\rm div}(r)\mathbf1_{f'\mid k'}.
\]

This establishes the source's full cancellation at lines 2550–2568,
not merely the norm-7 witness. For a unit \(k'\), it leaves only
\(f'=1\). For a prime of \(f'\) appearing to any positive power in
\(k'\), the local total is \(2-1=1\). If that prime does not divide
\(k'\), it is \(1-1=0\). Taking absolute values before this regrouping
would leave forbidden \(f'\nmid k'\) terms and destroy the later child
length lower bound.

## Total zero mode and remaining analytic obligations

The summed second zero modes have nonnegative outer weights. The exact
product is

\[
w_{C,d}Y_{C,d}\ell=\frac{c_I\Sigma}{N(C)^2N(t)}.
\]

Thus their total is bounded by
\(C\Sigma\|U\|_\infty^2
\sum_C\tau_{\rm div}(C)/N(C)^2
\sum_{N(t)\le2vL}N(t)^{-1}\), with coprimality restrictions safely
discarded for this upper bound. The first sum converges and the second is
\(O(\log(2+L))\), giving \(D^\varepsilon\Sigma\|U\|_\infty^2\).
This uses arbitrary \(Y_{C,d}>0\), including scales below 1, and no
unproved bound for a principal Möbius sum.

The arithmetic chain therefore returns to the precise excluded energy
class with the indispensable divisibility \(f'\mid k'\). The final
dyadic child ranges, removal of \(r\)-exclusions, uniform smooth kernel
norms and the induction require their own analytic/range audit. The
arithmetic calculations establish no substitute for those estimates.
Classical Poisson and the stated Gauss/reciprocity identities remain
imports; no theta or sieve cancellation is invoked in this two-Poisson
arithmetic derivation itself.

The [smooth and short-range audit](TWO_POISSON_SMOOTH_AND_SHORT_RANGES_20261012.md) and [return and termination note](TWO_POISSON_RETURN_AND_TERMINATION_20261012.md) check those companion obligations. The [combined review](../reviews/TWO_POISSON_TRANSFER_REVIEW_20261012.md) records the full proposition scope.
