# Internal review: octonionic lift and associator sign target

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Independent reviewing agent; the reviewer did not author the note or checker.
Inherited run configuration recorded by the parent from current-turn metadata:
**gpt-6-astra (Codex)**, reasoning effort **ultra**. The reviewer did not
independently query a platform model selector.

**Assessment:** no mathematical correction is required in the reviewed
versions. The explicit extension, signed associator identities, source
kernels, and analytic positive-source collision control check out. The
work gives an exact reformulation and a useful obstruction to generic
positivity arguments. It does not establish the outstanding theta estimate.

## Reviewed versions and independent replay

Files reviewed from the staging directory `/tmp/inv21-octonions/`:

| File | SHA-256 |
|---|---|
| `15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md` | `7f314c43b93db4b94f4df8994781204a6d4c94ab322536c59ce315e07e408e7d` |
| `check_octonion_jet_identities.py` | `800e47adcc28cdc4c4142f325c9f59a656f4601aaee1991594a871ea5dd7fe89` |

Independent command:

```sh
python3 /tmp/inv21-octonions/check_octonion_jet_identities.py \
  --output /tmp/inv21-octonions/OCTONION_JET_IDENTITY_INDEPENDENT_REPLAY_20261014.json
```

Python 3.10.0 returned **PASS: 248 checks, zero failures**. The independent
record has SHA-256
`5f30108461c3f4bb837485bacbec0e526c943464238bcfdc0233b1bfc7a7c9b8`.
This temporary replay is separate from the author's execution record.

Counts by group: arithmetic kernel 6; complex jet packaging 7; differential
extension 32; Hamilton convention 11; heat collision examples 20;
octonion algebra 34; physical jet identities 7; physical subalgebra 80;
rational samples 24; signed associators 24; transverse identity 3.

The reviewer inspected the rational polynomial arithmetic, conjugations,
Hamilton and Cayley--Dickson multiplication, stipulated jet derivations,
split and direct implementations of the eight-dimensional operator, and
the actual assertions. The generic symbolic norm identity is stronger
than the additional 24 rational samples. The differential checks establish
formal identities under the declared holomorphic heat recurrences; they
do not themselves establish analytic convergence or a source inequality.
The test count includes routine basis and arithmetic checks and is not a
count of independent theorems. This is internal computational and analytic
review, not proof-assistant verification or an external referee report.

## Independent algebra and differential checks

The declared convention agrees exactly with the multiplication and
left-unit representation in
[Baez, Section 2.2](https://math.ucr.edu/home/baez/octonions/node5.html).
The associator convention agrees with his
[preliminaries](https://math.ucr.edu/home/baez/octonions/node2.html).
The cited [Kauhanen--Orelma paper](https://arxiv.org/abs/1701.08698)
concerns octonionic Cauchy--Riemann operators; the specific extension here
is checked directly and does not depend on importing a product rule.

For a quaternion pair `(A,B)`, left multiplication by `(e_mu,0)` gives
`(e_mu A, conjugate(e_mu) B)`, while multiplication by `(0,e_mu)` gives
`(-B conjugate(e_mu), A e_mu)`. This verifies the two components in
equation (7). With

\[
A=G_m-\tfrac12G_{m+3}\bar r,\qquad B=G_{m+2},
\]

the first component is zero by quaternion left regularity and
associativity. The second is
`2 G_(m+3) - (1/2) G_(m+3) sum(conjugate(e_mu)e_mu) = 0`.
The spatial and heat recurrences follow by differentiation. Joint
entireness of the original heat family and linear dependence on `r`
give the stated global real analyticity. The correction uses
additional jets, including `h_4` at `m=0`; it is not a closed four-jet
system. The more general extension of any two left regular quaternion
fields also follows from `barD B = 2 B_x0`.

Direct calculation gives `[a,b,ell] = -ell(ab-ba)` for quaternion
arguments. For `a=A+jB`, `b=C+jD`, the two twisted quaternion commutators
are `2j(AD-BC)` and `-2j(AC+BD)`. This confirms all factors and signs in
(11)--(16), including the energy detector `A_E=2u E`, the stationary
forms `A_j=2u L_j`, and `A_t=u E_t`. The ray condition is an oriented
scalar condition, not an order on octonions. Its squared norm cannot
recover the sign.

For the transverse identity, differentiating the commutator gives

\[
[G_1\mathbf i,G_1]+[G_0,G_2\mathbf i]
=2\mathbf i(h_2^2-h_1h_3).
\]

Thus (17) has exactly the claimed negative sign. It uses the actual
spectral normal `x_1` with `tau` fixed. The physical untwisted four-jet
trace remains in its associative quaternion subalgebra; fixed twists
produce nonzero associators that encode already existing dot products
and determinants.

## Analytic checks outside the finite checker

The source formulas (19)--(20) were rederived by symmetrizing the double
integrals and using product-to-sum identities. The factors `1/4` and
`(-1)^j` are correct. For example, the `j=0` kernel is

\[
uv\sin(xu)\sin(xv)
+\tfrac12(u^2+v^2)\cos(xu)\cos(xv),
\]

which gives precisely the two terms in (20). Absolute convergence on
compact parameter sets justifies Fubini and the symmetrization for the
complete theta source. No kernel becomes pointwise nonnegative.

The quadratic and cubic controls give respectively `E=4 delta^2` and
`E=36 delta^2`, with `L_j=-E/delta` on the indicated stationary
predecessors. They exclude a locally bounded loss coefficient through
their collisions while satisfying every generic algebraic identity.

The positive-source example is valid analytically, including the stronger
claim of joint entireness in complex `epsilon`. The normalization is
correct because the integral of `exp(-v^4)` over the real line is
`Gamma(1/4)/2`. The symmetric shifted density has half-line mass 3.
For positive real `epsilon`, its half-line heat cosine transform is
exactly (23). On each compact subset of complex `(t,z,epsilon)` space,
its absolute integrand and any fixed parameter derivative are bounded
by a polynomial times

\[
C\exp(-v^4+C v^2+C|v|),
\]

which is integrable. The integral representation therefore gives a
jointly entire continuation, including `epsilon=0`. This does **not**
assert that the density formula containing `epsilon^(-1)` is entire at
zero; only its transformed representation has that continuation.

At `T_0=log(2)/3`, `x_0=pi`, one has `H=H_x=0` and
`H_xx=-6 exp(T_0)`. The Jacobian of `(H,H_x)` in `(t,x)` has determinant
`-H_xx^2`, which is nonzero. The real analytic implicit-function theorem
therefore produces real double collisions at positive time for all
sufficiently small positive `epsilon`; nonzero second derivative and
positive time persist by continuity. Changing `v` to `-v` proves
evenness in `epsilon`, and local uniqueness gives the stated
`O(epsilon^2)` displacement. The density is strictly positive and even
on the real axis, entire in `u`, and has quartic real-axis decay.
No explicit admissible `epsilon` or numerical collision certificate is
claimed or needed for this existence argument.

## Remaining obligation and recommendation

Equations (24)--(26) are correct. The residual pairing obeys

\[
\Re(\bar F R_\lambda)=\tfrac12E_t-\lambda E.
\]

Consequently the proposed one-sided bound implies
`E_t >= -2 max(0,B-lambda) E` on the genuine stationary union. The
stronger residual-norm bound also suffices by Cauchy--Schwarz. The
normalization/oscillator associator comparison is an exact physical
slice identity with the stipulated real frequency `omega(t,x)`.

Preserve the note's qualification that centering by `lambda` is presently
an algebraic reformulation of the original radial energy inequality.
It provides progress toward exclusion only when an independent estimate
uses the actual theta arithmetic or modular structure to control its
negative radial component with locally bounded loss through every
candidate joint zero. Neither generic regularity, the new associators,
source positivity, nor arbitrarily accurate absolute approximation
supplies that estimate. The required domain still includes the complete
padded small-time collision region, with all source cross terms and
derivative remainders retained. The finite-height certificates are not
extended by this note.

The reviewed research note and small checker record are suitable for
retention as incremental research with these scope statements. No
manuscript revision, new RH conclusion, or certificate claim follows
from this review.
