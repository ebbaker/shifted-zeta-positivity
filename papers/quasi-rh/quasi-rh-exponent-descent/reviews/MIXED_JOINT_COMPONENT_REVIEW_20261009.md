# Review of the coupled middle and component-conductor refinement

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate derivations by same-model agents are internal validation, not
independent specialist review or formal proof verification.

The reviewed [mixed note 8](../mixed_character_families/notes/8_JOINT_MIDDLE_COMPONENT_CONDUCTORS_20261009.md)
controls an additional expanded column-pair piece of the actual mixed
chain, with conditional uniform reserve \(927/500000\). It preserves
the eight row restrictions and introduces a coupled exterior-radical/
projected-conductor predicate. The full joint \(pq^2\) bound is open.

## 1 Exact kernels and projected good conductors

The two complete kernels have normalization \(N^{-2}\). Their original
smooth profile and fixed phase factors give the bounded coefficients
\(c_kc_l\); endpoint characters remain outside the full zero-extended
middle quotient. The actual selected weight \(w_v\), physical norm
conditions and all masks remain in the middle sum.

The good projected conductors use valuation differences modulo two and
three. They are the growing quadratic and cubic parts, with bounded
bad-prime/unit/ray factors still retained in the quotient. No full-order
classification is silently inferred from good valuations alone. Taking
primitive projections can cancel phases but cannot delete their inherited
zeros; the estimate uses the modulus of the complete original quotient.

## 2 Pair counting and the coupled tuple count

The elementary projected-conductor pair estimate follows the original
gcd/sixth-power allocation proof with powers two or three. Counting the
common gcd gives \(CN/\sqrt{\mathrm Nf_j}(\mathrm N(ab))^{j/2}\).
For power three the two ideal sums converge; for power two the actual
physical column norm bounds give truncated harmonic sums and logarithms.
All allocations are bounded by a divisor factor, and ideal counting and
partial summation give \(O(N^{1+\varepsilon}V^{1/2+\varepsilon})\).
The pair count is a deduction from the existing ideal-counting input,
rather than a newly imported cubic or quadratic analytic operator.

For fixed endpoints, each exterior radical has at most
\(5^{\omega(\operatorname{rad}\xi)}\) exterior valuation assignments;
endpoint-supported valuations add \(6^{\omega(\operatorname{rad}(uh))}\).
Both costs are \(U^\varepsilon\). Thus the middle count on a radical
norm interval \([H,2H)\) is \(O(HU^\varepsilon)\).

The actual coupled cut implies a column cap
\(V_H=U^{142/125}/H^2\). If \(V_H<1\), its interval contributes
no eligible tuple. Otherwise the radical count times the column-pair
count is \(O(NU^{71/125+\varepsilon})\), independent of \(H\).
The union of the two projected-conductor choices, logarithmic intervals
and final partial interval cost only constants and \(U^\varepsilon\).
Positive tuple counting is the only enlargement; no signed or selected
weighted kernel is fed to a complete-row formula.

## 3 Exponents and exact remainder

The resulting chain estimate is
\(A^2WN^{d-1}U^{71/125+\varepsilon}\mathcal H^b\). Its reserve
is \(1-71/125-g-(1-2d)m-3s+2\mu\). The continuous envelope uses
the same coarse parameter box as note 7. It decreases in \(d,r,m,s\),
with the derivative in \(d\) equal to \(2m-(1+r)/2<0\).
The corner value is exactly \(927/500000\); the exact displayed
point gives \(108685273/9950000000\).

The new reserve exceeds the old minimum \(19/12500\), so the total
removed error remains below \(T\) by that old minimum. The complement
keeps all eight strict row conditions and requires both
\(Z^2\mathrm Nf_2\) and \(Z^2\mathrm Nf_3\) to exceed the product
cutoff. Reversal of endpoints and columns makes the retained expression
real. It is an expanded-tuple remainder, not a whole physical row sector
with two untouched kernels, and is not asserted positive.

The high-pair filter can have a zero diagonal and a nonzero off-diagonal
entry, which gives an indefinite two-by-two block. Therefore a positive
Gram/Cauchy argument cannot be applied to it merely because the original
uncut Gram form is positive. The six-prime row geometry and two coprime
prime columns survive the cut in raw norm bookkeeping; no selected-bin
population or weight lower bound follows.

## 4 Scope of joint cubic operators and the weight

The primary source has a genuine arbitrary-coefficient joint operator,
[de Faveri Proposition 8.1](https://arxiv.org/html/2610.04045v1#S8),
equation (8.1), for cubic \(ab^2\) rows and squarefree columns. Its proof
uses cubic conjugation. Remark 8.2 leaves additional work for a cube-free
column version. Theorem 1.2 is a fixed-twist central \(L\)-value moment.
Neither source statement supplies the sextic phase remaining here.

The quadratic part of a sextic \(pq^2\) phase depends on \(p\)
and the column; it cannot be absorbed into a single fixed column vector
for the joint cubic proposition. Within a fixed parity core it can be
removed from a positive square, but cross-core correlations remain.
On an unweighted positive rectangle, the joint covariance is an entrywise
product. Separate covariance norms and diagonal bounds recover the old
one-factor estimate; aligned positive blocks can saturate that matrix
bound. This is a limitation of those abstract data, not a native arithmetic
or post-cut lower bound.

The actual selected inverse polynomial keeps its original length \(U^r\).
Its marked moment does not become a shorter-family moment by changing
the auxiliary row scale. The global selected mass also supplies no local
weight/intensity decorrelation. Any such improvement needs a separate
estimate with its original coefficients, selectors, capacity and height
uniformity.

## 5 Finite verification and remaining dependencies

The [checker](../numerics/check_mixed_joint_component.py) prints the
deterministic [record](../numerics/mixed_joint_component_record_20261009.json).
Two fresh replays match byte for byte: **312,257 exact assertions**.
They include nontrivial canceled-phase zeros, nonzero removed and retained
off-diagonal terms, an exact negative restricted-chain witness and abstract
entrywise-product norm saturation. The record SHA-256 is
`fa96f75c34ee3c0f674b5e054d19ee8f17c814674a8d3e1e0fc7f46b27f68812`.

The formal checks retain zero extensions, actual finite Möbius weights,
norm-coupled selected subsets and signed pair reversals. Rational checks
use exact fractions. They do not certify asymptotic ideal counts, native
reciprocity or presentation transfer, the imported analytic inputs or
continuous cutoff certificate, selected-bin population, or the remaining
unbounded joint correlation. The new result is a conditional column-sector
refinement; the full mixed moment and any zero-free implication remain open.
