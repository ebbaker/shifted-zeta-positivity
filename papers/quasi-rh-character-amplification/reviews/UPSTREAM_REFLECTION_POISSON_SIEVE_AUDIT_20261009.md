# Upstream reflection primitive Poisson and sieve interfaces

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. This is
same-model internal proof read-through and exact finite checking, not
independent specialist validation or formal verification.

**No substantive defect was found in the inspected upstream interfaces.**
The full proof of source Proposition 5.1 has now received a further internal
read-through, including its cusp construction, all local Fourier branches,
Mellin normalization, contour argument, and prime-uniform kernel estimates.
The primitive Poisson formula and the quadratic-sieve family identification
also pass this scoped check. The deep theta, reciprocity, and sieve theorems
remain imports; the complete global family baseline has not been audited or
proved here. The conditional candidate `20999/24000` therefore retains its
previous conditional status.

The important distinction is between two different arithmetic scales:

\[
\text{completed theta reflection: }V^\sharp(q_\mu X/q_c^2),
\qquad
\text{primitive lattice Poisson: }\widehat\Phi(Kq_h/(q_dq_{\mathfrak m})).
\]

Here `c` is an **active cusp denominator**, whereas `m` is a primitive
character conductor and `d` is a divisor of the separately retained zero
mask. Replacing both scales by the same primitive conductor, or erasing
zero-exponent primes when reducing a character on units, would change the
actual identities. The source does neither in the inspected proofs.

## Source, comparison, and scope

The source is the [September 30 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Its local PDF hash was checked again:
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The actual proof read here is pp. 24-35, Proposition 5.1 and Lemma 5.2;
the quadratic family paragraph on p. 36; the cubic interface (14.6) on
p. 94; and Lemma 17.5 on pp. 120-121. Sections 4.1-4.2 provide the
measure, character and reciprocity conventions. Equations (5.15)-(5.19)
and the continuation paragraph were also visually checked on PDF
pp. 31-33 to preserve conjugation bars.

This follows [the reflection/inverse audit](REFLECTION_INVERSE_PROOF_AUDIT_20261009.md)
and [the centered-fourth audit](CENTERED_FOURTH_PROOF_AUDIT_20261009.md).
It does not repeat their child-width, annulus, mask, or affine-loss ledgers.
Those earlier files remain unchanged.

The external comparisons were to primary papers on 9 October 2026:

- [Dunn-Radziwill, arXiv:2109.07463v3, Section 5 and Appendix A](https://arxiv.org/html/2109.07463):
  the conjugate coefficient is explicitly `overline(d_j(-mu))`, and the
  three cusp representatives match source `F_1,F_19,F_10`. Their coefficient
  formulas impose squarefreeness in the Eisenstein ring, with no displayed
  coprimality between the squarefree and cube factors. Their Lemma 5.2
  requires unit Fourier support; source Proposition 5.1 instead derives
  its finite transform from the untwisted theta expansions, retaining
  nonunit and zero frequencies. These coefficient and automorphy inputs
  remain imported, not new proofs here.
- [Goldmakher-Louvel, arXiv:1112.1642v2, Definition 1 and Theorem 1.1](https://arxiv.org/pdf/1112.1642):
  the theorem is for primitive quadratic Hecke families of trivial infinite
  type, with a finite-class reciprocity law and primitive product conductor
  exactly `ab` for coprime same-class indices. The norm-ball sum, arbitrary
  complex coefficient class, and squarefree ideal restriction match the
  interface being used. The proof of that large sieve was not reread.

The original Heath-Brown Theorem 2 PDF was not accessible in this session:
the Oxford repository returned HTTP 403; the DOI and alternate paper
fetches failed. Its statement was compared with the unconditional reprint
in [Dunn-Radziwill, equation (1.11) and Theorem 9.1](https://arxiv.org/html/2109.07463#S9).
That reprint agrees with source (14.6), including arbitrary complex
coefficients and squarefreeness in `Z[omega]`, rather than squarefree
rational norm or exclusion of rational prime factors. This is a statement
comparison through another primary paper, not a read-through of the
original Heath-Brown proof.

## 1. Moving primes do not enter the fixed cusp modulus

The construction fixes the complete finite ray family, its zero extensions,
and `E,L` before selecting the good local prime set. Fixed numerators at the
excluded primes vary through one finite family after their valuations are
reduced modulo six. A moving good prime is retained in the local set even
when its exponent is zero modulo six. Lemma 5.2 says this explicitly.

For fixed `h_0 mod L`, reduce `lambda^2 h_0/L=a_F/c_F`; normalize the
numerator when `lambda|c_F` and the denominator otherwise. If `r` is the
active radical, then

\[
c=c_Fr,\qquad
a=a_Fr+\lambda^2c_F\sum_{p\mid r}(r/p)h_p.
\]

Every active `h_p` is a unit modulo `p`. At fixed primes of `c_F`, the
numerator is congruent to the unit `a_Fr`; at `p|r` it is
`lambda^2(c/p)h_p`. Thus this really is a reduced fraction, including
nonunit `h_0` and the empty active radical.

With `M=lambda^12 L^4`, the local lifts can satisfy `h_p=0 mod M^2`.
The source then fixes `r mod M^2` and the residues of `a,b,c,delta'`
at the required fixed prime powers. Its three cusp reductions all put
`gH^{-1}` in `Gamma_1(3)`. The residual cubic multiplier and cusp
coefficient family depend only on this finite sector. The local active
frequencies are summed only after these common cusp data have been fixed.

The new checker verifies these congruences in the actual ring `Z[omega]`
for **all 324 fixed frequencies modulo L=18**, including 162 nonunits,
five active-prime sets including the empty set, and three choices of every
active frequency. Its 4,860 cusp cases cover all three ramified branches.
It constructs `delta'` by exact CRT and checks the determinant and
`Gamma_1(3)` congruences; it does not assume a matrix already satisfying
them. It also verifies that the fixed cusp residues are independent of
the active frequencies in each tested sector. This checks one permitted
fixed presentation, not every possible ray family or every moving prime.

Treating a frozen good prime as a new member of the fixed excluded set
would not be justified by this argument: the theorem's constants could
then depend on a growing arithmetic datum. Such primes must continue as
explicit local factors, fixed coefficient restrictions, or puncture masks.
The inspected construction retains them in those forms.

## 2. Fourier orientation and every local branch are explicit

Put `x=lambda^4 mu`, `D_F=lambda^3 c_F`, and

\[
\sigma_p=\lambda^2c/p,\qquad
\epsilon_p=-\big((\lambda^3c/p)\sigma_p\big)^{-1}\pmod p.
\]

The reflected additive character is exactly

\[
\check e(-\delta'\mu/c)
= e(-\delta'x/(D_Fr))
=\vartheta(x)\prod_{p\mid r}e(\epsilon_ph_p^{-1}x/p).
\]

The conjugated cubic multiplier contributes `chi_p(h_p)^(-2)`, and
the original Fourier coefficient contributes `chi_p(h_p)^(-j)`.
Inverting `h_p` therefore produces exponent **j+2**, and hence dual
column exponent **-j-2**. The exceptional `j=4` case is a Ramanujan
sum, not a nontrivial Gauss sum:

\[
\sum_{y\ne0}e(\epsilon_pxy/p)=-1+q_p\mathbf1_{p\mid x}.
\]

For `j=0`, its active branch instead has a `q_p^{-1/2}` cubic local
factor; the inactive branch contributes `1-q_p^{-1}` and leaves the
active denominator and every other local factor unchanged. For `j=4`,
the column factor can have size about `q_p^{1/2}` at a collision; it
cannot be absorbed into the bounded scalar. Its explicit local factor
and the previous energy payment must be retained.

These statements are checked in exact cyclotomic arithmetic for actual
split residue fields of orders 7,13,19,31,37,43 and inert residue fields
of orders 25 and 121. Every local exponent, every additive frequency,
every column including zero, and three nonzero epsilon values are read.
The additive characters come from the source's `e` pairing and the
displayed primary Eisenstein prime, not from a floating-point surrogate.
The prime `-2` of norm four is separately checked using its **cubic**
character, as appropriate for cusp coefficients; no order-six character
at that prime is asserted. The checker also validates the additive CRT
signs and lambda powers in (5.16) on 24,300 actual cusp/column cases.

The general local identities still have the direct change-of-variable
proof in the source. The finite check supplies additional diagnostics
of orientation, zero extension, and split/inert conventions; it does
not prove global cubic reciprocity or the theta coefficient theorem.

## 3. Continuation constants and uniform kernel constants have different roles

The source's intermediate polynomial strip bound for `T(s,Psi)` permits
its constants to depend on the current prime set. That does not supply
a uniform moving-family estimate by itself. In the inspected use it
justifies an **exact identity for each finite arithmetic choice**; the
quantitative estimate is then taken on the explicitly transformed side.

The derivative of the theta function eliminates every cusp constant
term. After inversion at the rational cusp, the vertical scale is
`v -> 1/(q_c v)`, and the Bessel Mellin normalization gives the
displayed `q_c^2` in the kernel. The dual series converges absolutely on
the initial reflected line by the three separate squarefree, cube, and
ramified majorants. The fixed dual support has a positive lower bound.
Exponential Bessel decay at both vertical ends makes the Mellin integral
entire. The gamma comparison, bounded vertical edges, and
`exp(epsilon s^2)` rectangle argument then justify the contour shift
for each fixed arithmetic choice. No moving-prime contour constant
is subsequently quoted as a uniform power-saving estimate.

The resulting transformed kernel has a gamma quotient depending only
on the fixed archimedean data. Its first numerator pole is at `-5/6`;
the shifts between `-1/4,0,A` stay clear of that pole. Stirling gives
the fixed-order growth `(1+|u|)^(4 Re t)`. Differentiating the kernel
only inserts powers of `t`, so (5.4)-(5.6) bound every required fixed
Euler/Fourier order by a finite Mellin seminorm of the original test,
independently of the moving good primes. A norm twist shifts Mellin
frequency and costs the stated polynomial in the twist height.

Thus freezing a large good base prime does not create a derivative
constant depending on its norm. Its norm remains in the displayed
scale and local arithmetic factors. The fixed cusp sectors have bounded
number; `4^omega(P)=d(rad P)^2` is divisor-bounded and can be absorbed
in any allocated small power when the radical lies in the declared norm
range. None of this erases the large `j=4` local factor.

This discharges the specific concern that the nonuniform continuation
constant was being used as a uniform kernel estimate. It is a proof
read-through under the theta input, not an independent construction
or theorem for the theta function.

## 4. Primitive Poisson keeps the conductor and deletion zeros separate

The source's measure makes `O` self-dual for `e(zy)` and gives it
covolume one. A radial test at norm scale `K` therefore contributes
`K`; residue-class Poisson at primitive modulus `m` contributes
`K/q_m`. The finite character transform is

\[
\sum_{x\bmod m}\psi(x)e(hx/m)
=\sqrt{q_m}\,\gamma(\psi;m)\overline{\psi(h)}.
\]

Expanding the complete mask, putting `k=dk'`, and retaining `psi(d)`
gives exactly the source prefactor `K gamma/(q_d sqrt(q_m))` and
argument `K q_h/(q_d q_m)`. The plus sign in this finite transform
requires the conjugate dual character. The exact prime-field checks
confirm that orientation.

For a nonunit frequency the finite transform vanishes by primitivity.
One direct general justification is to take a prime dividing both the
frequency and conductor: the additive factor is invariant under the
kernel of reduction by that prime, while the primitive multiplicative
character is nontrivial on that kernel, forcing the sum to vanish.
This argument is not valid for an imprimitive zero-extended character.
The checker records the countercheck: the principal unit mask modulo
a prime has a nonzero zero-frequency transform. The source first
replaces a character by its primitive inducer and puts the removed
local zeros into `R`, so it does not apply that false primitivity claim.

Primes shared by `d` and the true conductor contribute `psi(d)=0`.
For the primitive principal character the conductor is one, with its
explicit zero-frequency convention; the nonzero-frequency restoration
is bounded by lattice counting and Schwartz decay. In particular a
cancelled or six-divisible factor can remove a primitive conductor
prime without removing its natural zero from the mask. These are the
precise conventions required by the downstream induction.

The general self-dual lattice Poisson theorem and primitive finite
character theorem remain analytic/arithmetic inputs; the normalization
and their local interface have been checked, not formally verified for
all prime-power conductors or every fixed ray presentation.

## 5. The quadratic family identification meets the cited hypotheses

For a squarefree good primary ideal `a`, evaluate the quadratic residue
symbol at the primary generator of a column ideal. On an arbitrary
generator `x` prime to `lambda`, its unit adjustment contributes
`epsilon_lambda(x)^(e(a))`, where `e(a)=(q_a-1)/2 mod 2`.
The powers of `omega` are squares and contribute nothing. Hence the
primitive character has conductor exactly `a lambda^(e(a))`:
every prime of `a` has a nontrivial quadratic local component, and
the lambda component is nontrivial precisely when `e(a)=1`.
It has trivial infinite type.

A fixed primary square class modulo four fixes `e(a)`. For coprime
indices in that class, the two lambda components cancel, and the
remaining product is primitive at each prime of `ab`, with conductor
exactly `ab`. Primary generators multiply, so the class map is a
homomorphism; the fixed reciprocity factor supplies the required finite
class law. This is the concrete verification of Goldmakher-Louvel's
three family requirements, including its exact product-conductor clause.

The opposite matrix orientation follows from Hilbert-space transpose
duality; the finite reciprocity classes may also be split. Fixed moving
frozen-prime restrictions are allowed as row subsets or coefficient
zeros with the same theorem constant. They do not require changing
the fixed modulus defining the Hecke family. The previous mask audit
is still needed before a simultaneously row/column-dependent mask
can be replaced by such separated restrictions.

The cubic theorem uses primary Eisenstein squarefree indices as well.
Its opposite orientation follows from cubic reciprocity, with whole
complex coefficients conjugated where necessary. Its statement agrees
with the accessible primary reprint described above. Its original proof
and the full norm-recursion/global-family machinery are not validated
by these observations.

## Verification, remaining obligations, and next validation step

The new [checker](../numerics/check_upstream_reflection_interfaces.py) and
[record](../numerics/upstream_reflection_interfaces_record_20261009.json)
pass **69,881 exact assertions**. They include 5,328 local reflection
cases, 1,776 finite Fourier cases, 1,480 primitive orientation cases,
24,300 additive CRT cases, the actual cusp constructions above, and
the norm-four cubic boundary test. The arithmetic is exact integers,
rationals, and explicit cyclotomic quotient rings. The record labels
the finite scope and binds the checker and source PDF hashes.

From a repository root, run:

```sh
python3 papers/quasi-rh-character-amplification/numerics/check_upstream_reflection_interfaces.py
```

By default it writes its small record beside the checker; `--output PATH`
allows a separate replay record. No large derived data or third-party
PDF is part of the deliverables.

The outstanding obligations can now be stated more narrowly:

1. Independent specialist or formal validation of the imported cubic
   theta automorphy/coefficient formulas and their reciprocity laws.
   This audit checks the completed transformation derived from them,
   not their deep proofs.
2. Independent validation of the external quadratic and cubic sieve
   theorems. The quadratic hypotheses have been matched; the original
   cubic proof has an explicit source-accessibility gap in this session.
3. Validation of the complete sextic norm-recursion/global family baseline
   used by the candidate. It is a separate theorem for moving Hecke
   families and is not replaced by zeta-only quasi-RH or by these local
   reflection checks.
4. Full analytic validation of the entire combined induction beyond the
   specific common-profile and finite-order interfaces reviewed here.

The most useful next internal validation is therefore the global family
baseline and its sextic large-sieve recursion, with a specialist review
of the deep reflection/sieve inputs in parallel. Repeating the now
checked local affine ledgers, or treating 69,881 finite assertions as
a proof of an unbounded family theorem, would not address that task.
