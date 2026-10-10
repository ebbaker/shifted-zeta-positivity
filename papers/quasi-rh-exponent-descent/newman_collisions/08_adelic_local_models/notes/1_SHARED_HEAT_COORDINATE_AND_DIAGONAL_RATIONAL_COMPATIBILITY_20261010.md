# Shared heat coordinate and diagonal rational compatibility

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. The review is an internal LLM check,
not independent mathematical validation.

This implements direction 08 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The scout proves the complete six-term shared-coordinate representation
through four raw spatial derivatives. Its additional result separates two
admissible state classes precisely: local valuation coordinates plus heat
coupling still admit every multiplicative twist, whereas triviality on
diagonal positive rationals, with an unramified archimedean character,
forces one common height parameter. That latter compatibility is useful
information, but is not a signed nonvanishing theorem.

## 1. Finite valuation model and mixed heat factor

For primes `2,3,5`, retain the valuation vectors of all six integers:

| `n` | `nu_2,nu_3,nu_5` |
| --- | --- |
| 1 | `(0,0,0)` |
| 2 | `(1,0,0)` |
| 3 | `(0,1,0)` |
| 4 | `(2,0,0)` |
| 5 | `(0,0,1)` |
| 6 | `(1,1,0)` |

Let `J_p` multiply a basis vector by `nu_p log p`, and `J=sum J_p`.
The finite enlarged Hilbert space is the span of these six vectors, with
its ordinary positive norm. Its heat-weight generator is `J^2/4`, so
`exp(tJ^2/4)` gives `b_n^t=exp(t log^2 n/4)`. This sign is positive;
the corresponding torus generator is backward heat. The state includes
the manuscript's nonmultiplicative heat coefficient, complex exponent,
and reflected carrier, not an Euler product with new coefficients.

An independent-prime generator `sum J_p^2/4` misses
`sum_{p<q} J_p J_q/2`. At the retained integer 6 it gives

\[
\frac{b_6^t}{b_2^tb_3^t}
=\exp\{\tfrac t2\log2\log3\}>1\quad(t>0).
\tag{1}
\]

The support `n<=6` is itself a joint constraint; it is not a tensor product
of independently truncated local valuation spaces. Products that would
create 8, 10, 12, and other excluded integers cannot be silently retained
or removed in a purported Euler-product equality.

For `t>0`, one shared real coordinate restores every mixed coefficient:

\[
b_n^t=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
 e^{-\lambda^2/t+\lambda\log n}\,d\lambda.
\tag{2}
\]

Completing the square proves (2); its variance is `t/2`. The same
`lambda` occurs in every prime factor of each integer. It is not a
collection of independent prime Gaussian variables.

## 2. The reflected arithmetic sum and all four raw jets

Keep the manuscript's holomorphic data

\[
s_-=(1-ix)/2,\quad s_+=1-s_-,\quad
\eta_\pm=s_\pm+\tfrac t2\alpha(s_\pm),\quad
\theta=\theta_t(x),\quad \ell_n=\log n.
\]

Put `epsilon_- =+1`, `epsilon_+=-1`. The exact six-term finite
approximation has the shared-coordinate realization

\[
F_{t,6}(x)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}e^{-\lambda^2/t}
 \sum_{\sigma\in\{-,+\}}\sum_{n=1}^6
 e^{i\epsilon_\sigma\theta+(\lambda-\eta_\sigma)\ell_n}\,d\lambda.
\tag{3}
\]

This is an exact representation of the specified finite approximant,
not an assertion that `F_{t,6}=Q_t`. The normalizer and both carriers are
already retained in (3). On the real axis the two branches are conjugate.
All terms use one actual `x`, with weights and derivatives evaluated there.

At fixed `t` and fixed integer cutoff define

\[
a_\sigma=i\epsilon_\sigma\theta'-\eta_\sigma'\ell_n,
\qquad
a_\sigma^{(k)}=i\epsilon_\sigma\theta^{(k+1)}
 -\eta_\sigma^{(k+1)}\ell_n.
\]

The raw derivative multipliers of the integrand are

\[
\begin{aligned}
B_0&=1,& B_1&=a,\\
B_2&=a^2+a',&B_3&=a^3+3aa'+a'',\\
B_4&=a^4+6a^2a'+3(a')^2+4aa''+a'''.
\end{aligned}
\tag{4}
\]

Multiply each term of (3) by `B_j` to obtain `F_{t,6}^{(j)}` through
order four. For `k>=1`,
`eta_sigma^{(k)}=s_sigma' 1_{k=1}+(t/2)(s_sigma')^k alpha^{(k)}(s_sigma)`;
`s_-'=-i/2` and `s_+'=i/2`. In particular the minus branch has

\[
a_-=-i\Omega+(-tV/4+ic)\ell_n,
\quad c=\tfrac12(1+tU/2),\quad
\Omega=\tfrac12\Re\{\alpha(1+t\alpha'/2)\}.
\tag{5}
\]

The real term `-tV ell_n/4` is the amplitude drift. It cannot be dropped
when taking the derivative readout. The integral in (3) and its four
derivatives converge uniformly on closed holomorphic neighborhoods where
the manuscript's logarithms are defined: a finite sum times a polynomial
in `ell_n` is dominated by `exp(-lambda^2/t+C|lambda|)`. Differentiation
is therefore justified without an infinite-product interchange.

At fixed `x`, increasing `t` changes not only `b_n^t` but also
`eta_sigma`, `theta`, and the normalizer underlying them. The finite
approximation is not an exact homogeneous heat solution. The genuine full
theta observation has `partial_t H=-H''`; the approximation/reduction
interface is paid separately in section 5.

## 3. Why the shared Gaussian does not remove twisting freedom

A local unit twist acts diagonally as
`U_chi e_n=chi(n)e_n`, with `chi(n)=product chi(p)^{nu_p(n)}`.
It commutes with `J`, `J^2`, every local generator, and the finite cutoff
projection. Therefore the shared-coordinate identity (2) and the
derivative identities (3)–(4) hold unchanged after every such twist.
Gaussian coupling repairs the mixed heat coefficient but enforces no
phase restriction beyond complete multiplicativity.

This observation matters at the growing complete cutoff: the manuscript's
complete multiplicative-twist construction already cancels both real
collision coordinates at the same coefficient data. A joint lower bound
for all states of the local-plus-Gaussian model cannot supply the missing
actual-orbit inequality. No zero is asserted for the six-term control,
and no twist is identified with a genuine theta collision.

## 4. A concrete global compatibility that does restrict phases

For this bounded test impose an actual global condition, rather than an
unexplained phase restriction. Consider a product quasicharacter on the
rational ideles, trivial on diagonal positive rationals. Assume its finite
local factors are trivial on `Z_p^*`, and its real factor on positive
numbers is `chi_infinity(r)=r^a`, with one complex `a`. Evaluating it on
the diagonal rational prime `p` gives, using the product's triviality,

\[
1=\chi_\infty(p)\chi_p(p)=p^a\chi_p(p),
\qquad \chi_p(p)=p^{-a}.
\tag{6}
\]

All other finite factors see units and contribute one. Conversely these
assignments are compatible on every positive rational by unique prime
factorization. In the unitary case `a=iT`, the local valuation phases are
all controlled by the single real `T`; taking the inverse character gives
the genuine monomials `p^{iT nu_p(n)}`. Triviality also on diagonal `-1`
removes an odd real sign character under the stated trivial finite-unit
condition. These are elementary consequences of the declared global
condition. The local/quasicharacter and global framework is the imported
architecture from [Tate's thesis, sections 2.3 and 4.3](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf).

In (3), each Gaussian slice has `a=eta_sigma-lambda`; its finite
characters then supply `n^{lambda-eta_sigma}`. A superposition of these
globally compatible slices reproduces the nonmultiplicative heat weight.
The Gaussian superposition itself is not one character, and no unrestricted
Euler product is needed. This is a genuine restriction missing from
independent local phase channels. It selects a common spectral exponent;
it does not yet force that exponent, carrier, and heat-time derivatives
to move according to the physical height unless the explicit functions
`eta_sigma(t,x)` and `theta_t(x)` in (3) are supplied.

Crucially, common-character compatibility has no displayed inequality
on the projected value and derivative. It replaces the all-torus problem
by the actual one-parameter orbit problem of program 09. One may not
conclude nonvanishing merely from the absence of arbitrary local twists.

## 5. Finite and genuine scopes, and continuation

The `N=6` calculation is a coefficient-level exact control at arbitrary
admissible `t,x`; it is not a shrinking-sector theorem with six terms.
For the genuine sector `L=kappa/t`, `x=4 pi exp(L)`, choose the complete
natural cutoff and then freeze its integer value for spatial derivatives.
The manuscript pays `|Q^{(j)}-F_N^{(j)}|<=j! L^j eta_N`. A collision
requires `|(F_N/2,2F_N'/L)|^2<=17 eta_N^2/4`; a threshold jet sign needs
the complete measured quadratic payment, not small single-jet errors alone.

The infinite series `sum b_n^t n^{-s}` diverges at positive time for
every fixed `s`, since its terms fail to tend to zero. The Gaussian identity
does not authorize moving its integral through that series or an Euler
product. A genuine infinite adelic realization would need a different
summability architecture, such as the full theta channel and a proved
Poisson reduction, with its domains printed explicitly.

The strongest continuation is to use (6) as the admissible state condition
in a coupled theta/prime model and seek a candidate-conditioned signed
identity along the actual orbit. Program 06 offers an exact theta Ward
relation; program 09 identifies the orbit jet algebra. This scout reaches
exact finite matching, a concrete global compatibility, and a scoped
twisting obstruction. It establishes no paid signed exclusion or RH result.

The [checker](../numerics/check_adelic_scout.py) verifies finite valuation
support, the mixed coefficient polynomial, Gaussian moment identities,
the four raw-jet polynomials, and diagonal-rational compatibility for
formal rational prime data. It does not verify a global adelic continuum
construction or an actual collision inequality.
