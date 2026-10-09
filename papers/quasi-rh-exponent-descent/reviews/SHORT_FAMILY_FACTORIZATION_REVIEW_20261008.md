# Scoped review of centered factorization and signed gcd recombination

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a separate same-model internal review, not independent specialist
validation or formal proof replay.

Reviewed staged continuations based on repository commit
`480581447dcd3e93c9c2f9c22a050d9c5100ff9d`:
[note 8](../short_families/notes/8_SHORT_FAMILY_CENTERED_FACTORIZATION_20261008.md),
[note 9](../short_families/notes/9_SHORT_FAMILY_SIGNED_GCD_RECOMBINATION_20261008.md),
and [note 10](../short_families/notes/10_SHORT_FAMILY_FACTORIZATION_CONTINUATION_20261008.md).

## Conclusion and dependencies

The displayed reductions and bounds are accepted within their stated
scope, conditional on the imported arithmetic presentation and Poisson
inputs below. They establish a centered sector estimate, exact signed
identities, and quantitative truncation. They do not estimate the
recombined residual moment, establish a useful full short-family moment,
or prove a new zero-free boundary or RH descent.

The imported inputs are the multiplicative zero extension of the sextic
denominator symbol, its finite-order Hecke presentation by reciprocity,
the tame conductor description away from the fixed bad primes, primitive
Gauss sums, and lattice Poisson summation with its principal zero
frequency. The deep source proofs are not replayed here. Dirichlet
convolution algebra, support boundaries, centered-error estimates,
divisor inclusion--exclusion, counting, and exponent comparisons are
deductions from those inputs.

## Note 8: exact identity and centered completion

The truncated inverse identity is valid on the monoid of ideals prime
to the fixed set. The remainder has support strictly beyond \(z^J\),
so the endpoint \(Nn=z^J\) is covered. The profile condition is
\(z^J\ge CD\). With \(J=2\), \(z=(CD)^{1/2}\), and \(cD>z\), the
amplitude factorization holds on the entire annulus. Complete
multiplicativity of \(\lambda_u\), including zeros, justifies twisting
the identity even when its factors overlap. Individual free factors
must not be restricted to squarefree ideals, and no additional
coprimality conditions may be inserted. Their signed recombination
produces the required nonsquarefree zeros.

The combined modulus bound is essential. At a good prime dividing
\(u\), a valuation nonzero modulo six contributes conductor exponent
one; a positive valuation zero modulo six contributes only a deletion
prime. These two supports are disjoint. The conductor times the extra
squarefree mask therefore divides a fixed bad modulus times
\(\operatorname{rad}(u)\), giving

\[
 Q_uNE_u\ll_{\nu,S}Nu.
\]

Separate estimates \(Q_u\ll Nu\) and \(NE_u\ll Nu\) would not suffice
for the asserted rapid-decay scale. The fixed bad conductors remain
bounded through the finite local sixth-power classes and the fixed
character \(\nu\).

For each divisor \(e\mid E_u\), coprimality with the primitive conductor
permits the masked change of scale. Put \(t=L/(NeQ_u)\). Primitive
Poisson has nonzero-frequency prefactor \(\sqrt{Q_u}\,t\). The radial
Schwartz transform has absolute sum \(O(t^{-1})\) for all \(t>0\),
with arbitrary additional decay for \(t\ge1\). Consequently each
divisor contributes \(O_A(\sqrt{Q_u}t^{-A})\). For \(t<1\), this
follows already from the uniform bound because \(t^{-A}\ge1\).
Summation over divisors and the combined modulus yield

\[
 |E_u(L)|\ll_{A,\varepsilon}
 (Nu)^{1/2+\varepsilon}(Nu/L)^A,
 \qquad L>0,
\]

with constants allowed to depend on the fixed profiles and arithmetic
data. The zero frequency is correctly retained precisely on
principal-induced rows. Its coefficient is the residue of the
surviving-prime Dirichlet series times
\(L\int W(t)\,dt\), with no conjugation of \(W\).

Using \( |c_z(d)|\le\tau(d)\) gives

\[
 \mathcal E_I\ll_{A,\varepsilon}
 D^\varepsilon\frac{H^2Y^2}{D}(HY/D)^{2A}.
\]

This retains the original Schwartz row weight: its higher moments
control rows larger than \(H\). For fixed \(0<h<1\) and
\(0<\eta<1-h\), \(Y=D^{1-h-\eta}\) gives arbitrary power decay by
choosing \(A\) in terms of the requested error. The \(A=0\) branch
separately proves the unbuffered budget \(2y+h-1\le a\). When
\(Y>z\), the divisor bound still applies, but the simplification
\(c_z=\mu_K*\mu_K\) is valid only below \(z\).

The two norm inequalities correctly establish the equivalence with the
moment of \(R_u=T_u+P_u\). This equivalence supplies no bound for
\(R_u\). Its principal correction must remain inside the same square
as the complementary convolution sum; separately estimating the two
terms would require additional information.

## Note 9: exact signed recombination and original gcd scale

Inclusion--exclusion proves
\(C=\sum_d\mu_K(d)B_d\) exactly. The full divisor sum removes every
nonunit diagonal, and the unit column is outside the annulus for large
\(D\). For squarefree \(d\), extraction of \(d\mid n\) retains both
the column mask \((m,d)=1\) and row mask \((u,d)=1\). The identity
\(B_d=(Nd)^{-1}\mathfrak M_d(D/Nd,H)\) keeps row scale \(H\), rather
than replacing it by \((D/Nd)^h\).

For distinct squarefree columns, their common ideal cancels in the
ratio character. The remaining coprime nonunit conductor is
nonprincipal and primitive at the good primes. Counting and masked
completion give \(\min\{H,D/G\}\) for the original row kernel and
\(O(D^2/G)\) pairs in a dyadic gcd block. These imply the stated
normalized tail \(D^\varepsilon\min\{HD/T,D^2/T^2\}\).
The truncated divisor sum additionally has a diagonal bounded by
\(HD^\varepsilon\), as the note records.

A pair selector independent of \(u\) with size \(D^\varepsilon\)
is permitted in this absolute tail estimate. No arbitrary pair
restriction is justified inside the exact identities, nor does the
tail estimate bound the remaining signed coprime core. The lossless
original gcd cutoff \(T=D^{1-h/2}\) is correctly distinguished from
the transformed overlap cutoff \(D^{1/2}\) of note 4. Those kernels
have different scales.

The divisor-one summand is the original full moment, so a triangle
bound on the signed positive moments is circular. The local Euler
product is correct in its domain of absolute convergence; the finite
divisor diagnostic demonstrates compensation without providing an
annular asymptotic estimate.

## Verification scope

The coordinating review reran the standard-library
[checker](../numerics/check_short_family_factorization.py) twice.
All 24,245 exact assertions across 33 groups passed, and the two JSON
outputs matched byte-for-byte. The
[retained record](../numerics/short_family_factorization_record_20261008.json)
contains the counts, finite model, witnesses and scope limits.

The checks use a finite free ideal-style monoid with prime norm labels
7, 13, 19 and 25, formal twists in the exact field Q(zeta_6), and finite
complex profile samples. They are not an enumeration of Eisenstein ideals
or evaluations of native sextic residue symbols. Synthetic principal
coefficients test centering algebra, rather than analytic residue values.
The checks cover convolution and endpoint support, deletion masks and
Euler inversion, nonsquarefree cancellation, centering, signed gcd
truncation and its nonzero diagonal, finite divisor compensation, and
rational completion, extraction and core-cutoff budgets.
They do not prove the imported analytic inputs, the Schwartz transform
decay estimates, or the still-unproved recombined moment.

## Note 10: summary and quantitative core cutoffs

The centered-sector and signed-gcd formulas agree with notes 8--9.
The proposed losses \(a<1/12\) at \(h=4/5\) and \(a<1/108\)
at \(h=8/9\) are the correct strict extraction budgets. For those
displayed cutoffs, \(Y\le D^{1/3}\). Grouping the largest of the
three factors is a valid support statement: it is at least a fixed
multiple of \(D^{1/3}\), at most a fixed multiple of \(D/Y\), and
the complementary product has the same \(Y\) to \(D/Y\) range.
This creates no coefficient separation or bilinear estimate.

The Euler inverse in (7) retains every mask, including the zeros at
primes of the core. Its conditional low-core bound is valid for
\(1\le V\le H\), with constants chosen using a smaller preliminary
epsilon. For every \(\beta>0\), the nonnegative divisor convolution
of \(F_\beta^2\) has convergent Euler product in (10). Ideal counting
therefore gives its mean \(O_\beta(R)\) for \(R\ge1\). Taking
\(R=(H/Nv)^{1/6}\) and summing dyadic shells preserves the full
Schwartz row weight and proves (9). Finite bad-prime splittings change
constants only. The factor \(V^{2\kappa+5/6}\) in (11) follows
from ideal counting under the explicitly stated conductor-uniform
hypothesis; fixed-character bounds do not supply it automatically.

The complementary estimate (12) correctly retains the fixed
\(r\)-mask in each application of the imported sixth-power-free
sieve. Only \(Nr\ll(H/V)^{1/6}\) can pay its \(D\) term in a
bounded row shell. The other three inverse-norm sums converge; row
shells and Schwartz decay recover the original smooth moment.

The fixed-core obstruction (13) is correct for the specified broad
coefficient class and nonnegative nonzero annular profile. Use all good
ideals \(r\) up to a fixed multiple of \((H/Nv_0)^{1/6}\), with the
row weight at least one on the inner ball as in note 2. Prime columns
have norms comparable to \(D\), so for large \(D\) they divide neither
these \(r\) nor the fixed core. The aligned coefficient vector makes
their amplitude of order \(D/\log D\); counting all \(r\), rather
than prime \(r\), explains the denominator \((\log D)^2\).
This is not a lower bound for the original Möbius coefficients.
Likewise, the last-term comparison in (12) establishes insufficiency
of that upper bound, not an actual tail lower bound.
