# Möbius ratio cores in the selected inverse weighted fourth moment

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Parallel audits are same-model
internal validation, not independent specialist review or formal verification.

The selected inverse fourth moment has an exact decomposition by squarefree
ratio core. The common gcd contributes its physical zero mask and the
original annular scales; its Möbius sign squares away. The ratio core carries
the remaining Möbius sign. Annular balance removes growing prime cores
automatically, but balanced two-prime cores attain the existing absolute
pair-count exponent. Thus squarefree inverse support does not by itself
improve that exponent. A complete-family sixth-order sieve with a pointwise
fourth-weight bound also misses the direct target by a substantial power.
The outstanding task is a signed correlation with the actual selected
fourth weight.

## 1 The inherited selected moment

Use the physical family, fixed exclusions, native orientation, permitted
profiles and whole slots of the [mixed manuscript](../mixed_character_reductions.tex).
Fix a legal whole-slot subset \(J\), and retain
\[
 D=U^r,\qquad
 M_u=D^{-1/2}\sum_{\mathfrak d}
    \mu_F(\mathfrak d)A_0(\mathrm N\mathfrak d/D)\psi_u(\mathfrak d),
\]
\[
 V_u=\mathbf1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2,\qquad
 \sum_u V_u\ll U^{1+\varepsilon}H^b,\qquad
 F_J=\sum_u V_u|M_u|^2.
 \tag{1}
\]
The fourth mass in (1) is an imported source-compatible input, including
the prescribed derivative and height uniformity. It is not asserted for
arbitrary bounded prime coefficients or arbitrary deleted prime annuli.

Suppose \(\operatorname{supp}A_0\subset[c,C]\subset(0,\infty)\), with
fixed \(0<c<C\). Put
\[
 D_J=2dm+\Gamma_J-g,\qquad
 \chi_J=(2s-\mu-D_J)_+.
 \tag{2}
\]
The direct criterion asks for \(F_J\ll U^{1+dr-\chi_J+\varepsilon}H^b\).
For a fixed cap exponent \(\upsilon\ge0\) with
\(\gamma_J=dr-\chi_J-\upsilon/2>0\), note 7 proves
\[
 F_J=F_{J,>\upsilon}
       +O(U^{1+\upsilon/2+\varepsilon}H^b).
 \tag{3}
\]
Both terms in (3) are real, and a bound for the positive part of the
signed large-ratio term suffices. The derivation below keeps the
normalization \(D^{-1}\) and all the original profiles in that term.

## 2 Exact squarefree ratio core decomposition

Only squarefree inverse ideals contribute. For each ordered contributing
pair, write its unique gcd decomposition
\[
 \mathfrak d=\mathfrak g\mathfrak a,\qquad
 \mathfrak d'=\mathfrak g\mathfrak b,\qquad
 (\mathfrak a,\mathfrak b)=1.
\]
Squarefreeness implies that \(\mathfrak g,\mathfrak a,\mathfrak b\)
are squarefree and pairwise coprime. Conversely those conditions produce
a unique squarefree ordered pair. Define
\(\mathfrak f=\mathfrak a\mathfrak b\). Then
\[
 f_{\rm inv}(\mathfrak d,\mathfrak d')=\mathfrak f,\qquad
 \mu_F(\mathfrak d)\mu_F(\mathfrak d')=\mu_F(\mathfrak f).
 \tag{4}
\]
The first equality concerns the good radical of the sixth-order ratio.
At a prime of \(\mathfrak a\) the ratio exponent is one, at a prime of
\(\mathfrak b\) it is five, and a prime of \(\mathfrak g\) cancels in
phase. The full primitive conductor can still have the inherited fixed
bad-prime factors.

Multiplicativity with the physical zero convention gives
\[
 \psi_u(\mathfrak d)\overline{\psi_u(\mathfrak d')}
 =|\psi_u(\mathfrak g)|^2
       \psi_u(\mathfrak a)\overline{\psi_u(\mathfrak b)}.
 \tag{5}
\]
On good ideals for a unitary finite-order ray factor,
\(|\psi_u(\mathfrak g)|^2=\mathbf1_{(u,\mathfrak g)=1}\);
retaining the squared factor in (5) also retains every prescribed fixed
zero. Replacing it by one changes the weighted correlation.

Let
\[
 \mathcal L_{J;\mathfrak g}(\mathfrak a,\mathfrak b)
 =\sum_u V_u|\psi_u(\mathfrak g)|^2
                 \psi_u(\mathfrak a)\overline{\psi_u(\mathfrak b)},
\]
\[
 \mathcal H_J(\mathfrak f)
 =\sum_{\mathfrak a\mathfrak b=\mathfrak f}
    \ \sum_{\substack{\mathfrak g\ {\rm squarefree}\\
                          (\mathfrak g,\mathfrak f)=1}}
 A_0(\mathrm N(\mathfrak g\mathfrak a)/D)
 \overline{A_0(\mathrm N(\mathfrak g\mathfrak b)/D)}
 \mathcal L_{J;\mathfrak g}(\mathfrak a,\mathfrak b).
 \tag{6}
\]
All ideals are good, \(\mathfrak f\) is squarefree, and each factorization
in (6) is ordered. Its two factors are automatically coprime. Every sum
is finite on the original supports. Expanding (1), then using (4) and
(5), proves the exact identity
\[
 \boxed{
 F_{J,>\upsilon}
 =D^{-1}\sum_{\substack{\mathfrak f\ {\rm squarefree}\\
                       \mathrm N\mathfrak f>U^\upsilon}}
               \mu_F(\mathfrak f)\mathcal H_J(\mathfrak f).
 }
 \tag{7}
\]
Swapping \(\mathfrak a,\mathfrak b\) conjugates each summand in (6).
Thus every \(\mathcal H_J(\mathfrak f)\) is real, even for a complex
inverse profile. No positivity of these core sums is asserted.

The native ratio can also be represented by the sixth-power-free ideal
\(\mathfrak c=\mathfrak a\mathfrak b^5\). This representation is
\[
 \psi_u(\mathfrak a)\overline{\psi_u(\mathfrak b)}
 =\nu(\mathfrak a)\overline{\nu(\mathfrak b)}
                  \chi_{\mathfrak a\mathfrak b^5}(u)^{s_\chi}.
 \tag{8}
\]
The fixed ray phase in (8) must remain separate unless its equality with
another presentation is proved. Its physical index is not
\(\mathfrak f\): on balanced pairs
\(\mathrm N(\mathfrak a\mathfrak b^5)\asymp(\mathrm N\mathfrak f)^3\).
A canonical arbitrary-coefficient sieve cannot be invoked at column
radius \(\mathrm N\mathfrak f\) merely because that is the ratio radical.

## 3 Annular balance and the gcd scale

Write \(A=\mathrm N\mathfrak a\), \(B=\mathrm N\mathfrak b\),
\(G=\mathrm N\mathfrak g\), and \(F=AB=\mathrm N\mathfrak f\).
The supports require
\[
 cD\le GA,GB\le CD.
\]
Consequently
\[
 \frac cC\le\frac AB\le\frac Cc,\qquad
 \frac{cD}{\min(A,B)}\le G\le\frac{CD}{\max(A,B)},
 \qquad
 \frac{cD}{\sqrt F}\le G\le\frac{CD}{\sqrt F}.
 \tag{9}
\]
These are restrictions on the original annuli, not a rescaling of the
inverse polynomial to its conductor.

For any fixed \(\upsilon>0\), the remainder (7) therefore has
\[
 G<CD\,U^{-\upsilon/2}.
 \tag{10}
\]
In a core block \(F\asymp U^\beta\), its gcd scale is
\(G\asymp U^{r-\beta/2}\). The core range ends at \(F\ll D^2\).

If \(\mathfrak f\) is one prime, its only factorizations have
\(A=1,B=F\) or the reverse. Equation (9) forces \(F\le C/c\).
Thus every growing prime core is absent from (7). For sufficiently
large \(U\), the first possible large cores have at least two primes.
A two-prime core can have one prime on each side, at comparable norms,
and has Möbius sign \(+1\). An odd core can be balanced by placing a
larger prime against a product of smaller primes. The profile does not
force those cores to cancel one another.

## 4 The squarefree absolute pair count remains sharp in power

The core decomposition recovers the upper bound in note 7 directly.
For a core of norm \(F\), there are at most \(2^{\omega(\mathfrak f)}\)
ordered factorizations. For each one, the number of gcds allowed by the
upper support bound is \(O(D/\max(A,B))\le O(D/\sqrt F)\).
With \(|\mathcal L_{J;\mathfrak g}|\le\sum V_u\), this gives
\[
 |\mathcal H_J(\mathfrak f)|
 \ll U^{1+\varepsilon}H^b\,D
       F^{-1/2}2^{\omega(\mathfrak f)}.
 \tag{11}
\]
Summing over \(F\le V\) and restoring \(D^{-1}\) gives
\(O(U^{1+\varepsilon}H^b V^{1/2+\varepsilon})\).
This improvement in presentation gives no new exponent.

There is also an arithmetic lower bound for the absolute *column pair
count*. Assume \(A_0\) is nonzero; choose a closed subinterval inside
its support where \(|A_0|\) is bounded below. For
\[
 D=U^r,\qquad V=U^\upsilon,\qquad 0<\upsilon<2r,
\]
choose distinct good prime ideals \(\mathfrak p,\mathfrak q\) in one
sufficiently narrow fixed annulus of radius \(P\asymp\sqrt V\), with
the constants chosen so \(\mathrm N(\mathfrak p\mathfrak q)\le V\).
Choose squarefree good \(\mathfrak g\) in a fixed annulus of radius
\(G_0\asymp D/P\). Narrowing the prime window makes both
\(\mathrm N(\mathfrak g\mathfrak p)/D\) and
\(\mathrm N(\mathfrak g\mathfrak q)/D\) fall in the chosen profile
subinterval. Retain \((\mathfrak g,\mathfrak p\mathfrak q)=1\).

The same fixed-field prime ideal theorem used in mixed note 5 and short
note 24 gives \(\asymp P/\log P\) prime ideals in that window.
Squarefree good ideals have positive density. For completeness,
the Eisenstein lattice count for good ideals is
\(I_S(X)=\kappa_S X+O_S(\sqrt X+1)\); square-divisor inversion gives
\[
 \#\{\mathfrak g:\mathrm N\mathfrak g\le X,\ 
                    \mathfrak g\ {\rm squarefree},\ (\mathfrak g,S)=1\}
 =\frac{\kappa_S}{\zeta_F^S(2)}X+O_S(\sqrt X\log(2X)).
 \tag{12}
\]
To obtain (12), sum
\(\mu_F(\lambda)I_S(X/(\mathrm N\lambda)^2)\) for
\(\mathrm N\lambda\le\sqrt X\). The error is
\(O(\sqrt X\sum_{\mathrm N\lambda\le\sqrt X}1/\mathrm N\lambda)\);
ideal counting bounds that sum logarithmically. The omitted tail of
the convergent Euler series contributes \(O(\sqrt X)\).
Subtracting ideals divisible by either growing prime costs
\(O(G_0/P+1)=o(G_0)\).

Thus the ordered squarefree pairs
\((\mathfrak d,\mathfrak d')=(\mathfrak g\mathfrak p,
                            \mathfrak g\mathfrak q)\) contribute
\[
 \gg G_0(P/\log P)^2
 \asymp \frac{D\sqrt V}{(\log V)^2}
 \tag{13}
\]
to the absolute count, and the actual profile coefficient magnitudes
are bounded below there. All inverse ideals are squarefree; their good
ratio is \(\mathfrak p\mathfrak q\). This shows sharpness in power
for the \(DV^{1/2+\varepsilon}\) pair majorant even on the actual
squarefree support.

Equation (13) supplies no lower bound for \(F_J\), no population of a
selected detector bin, and no sign for its weighted row kernel. It rules
out improving this particular absolute pair-count exponent merely by
using the inverse's squarefree support or the absolute value of its
Möbius coefficient.

## 5 A complete positive inverse sieve also misses the fourth target

Another legitimate sufficient bound retains (1) until positivity, then
uses
\[
 V_u\ll U^{2dm+\Gamma_J+\varepsilon}H^b.
\]
Enlarge the nonnegative inverse square to all good sixth-power-free
physical rows of norm \(O(U)\). Subject to the inherited exact native
transfer, the sixth-order sieve applies to the squarefree inverse
columns of length \(D\), with coefficient squared norm \(O(D)\).
The inverse normalization cancels that factor:
\[
 F_J\ll U^{2dm+\Gamma_J+\varepsilon}H^b\Theta_6(U,D).
 \tag{14}
\]
For \(7/10<r<73/100\), the dominant operator exponent is
\(\theta_{\rm inv}=5/6+r/3\). The deficit relative to the desired
\(1+dr-\chi_J\) is
\[
 \Delta_{\rm pos}
 =-\frac16+r\Bigl(\frac13-d\Bigr)+2dm+\Gamma_J+\chi_J.
 \tag{15}
\]
At the exact favorable point and relaxed fourth capacity of note 7,
\[
 \Delta_{\rm pos}
 =\frac{15459785767}{126862500000}
 =0.1218625343738\ldots.
 \tag{16}
\]
The inherited pointwise inverse bound and the selected fourth mass
already give \(F_J\ll U^{1+dr+\varepsilon}H^b\), missing the favorable
target only by \(\chi_J\). The larger loss in (16) is a limitation
of (14), not a required saving in the original fourth moment.

## 6 The precise next correlation theorem

The target after this decomposition is
\[
 \left(
 \sum_{\substack{\mathfrak f\ {\rm squarefree}\\
                 \mathrm N\mathfrak f>U^\upsilon}}
        \mu_F(\mathfrak f)\mathcal H_J(\mathfrak f)
 \right)_+
 \ll D\,U^{1+dr-\chi_J+\varepsilon}H^b.
 \tag{17}
\]
Its kernels contain the original sharply selected \(V_u\), the
gcd masks, the balanced partitions and the unchanged inverse profile.
A theorem for scalar Möbius partial sums cannot be substituted for
(17): the real coefficient \(\mathcal H_J(\mathfrak f)\) depends on
the moving native characters, every balanced factorization, and the
selected response. Complete-row Poisson is likewise unavailable for
this selected kernel without an additional argument.

A useful first analytic test is a dyadic block in
\((F,G,A,B)\) obeying (9), with a signed combination of even and odd
cores or an actual weighted row correlation. A sector estimate must
have a specified power reserve and leave its cross terms under control.
Separately estimating the positive two-prime absolute packet from
(13) cannot establish compensation in (17).

For a uniformly stronger fourth saving \(c_*>0\), replace \(\chi_J\)
in (17) by \(c_*\), provided the operational budget proves
\(c_*\ge\chi_J\) and \(dr-c_*-\upsilon/2>0\). The [operational
budget note](9_OPERATIONAL_FOURTH_BUDGET_20261009.md) supplies that
comparison under its stated slot and witness hypotheses.

## 7 Exact checks and remaining mathematical scope

[The checker](../../numerics/check_mixed_mobius_ratio_core.py) uses
four formal primes, zero-extended sixth-root phases in the exact ring
\(\mathbb Z[\zeta_6]\), complex inverse profiles, a fixed multiplicative
ray phase, and an assembled nonzero selected fourth weight. It compares
the original inverse-pair expansion with the gcd/core expansion in both
native orientations, including strict cutoff equality, annular balance,
fixed phases and nontrivial canceled zero masks.
Its [small record](../../numerics/mixed_mobius_ratio_core_record_20261009.json)
also checks (15) and (16) with exact rational arithmetic.

The finite checks validate algebra and the displayed rational comparison.
The proof of (13) additionally uses the inherited fixed-field prime ideal
theorem and the squarefree lattice count above. Native reciprocity,
the family sieve, legal selected fourth mass, actual detector population
and (17) are not certified by the formal phases. The full mixed estimate,
a new global boundary, and descent to RH remain open.
