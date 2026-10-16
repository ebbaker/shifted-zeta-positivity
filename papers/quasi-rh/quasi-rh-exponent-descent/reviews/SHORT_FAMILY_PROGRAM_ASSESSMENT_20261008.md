# Short family program assessment and next arithmetic targets

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Three parallel same-model readings supported this assessment. This is an
internal research review, not independent specialist validation.

Reviewed working-tree manuscript:
[Short sextic character families](../short_families/short_family_reductions.tex),
based on repository HEAD `480581447dcd3e93c9c2f9c22a050d9c5100ff9d`.
Manuscript SHA-256:
`4872eb5e46a763750c63f5edf2dd7b904293dfa186b249759b3404545afb85ca`.
The manuscript and its latest supporting notes are uncommitted at this snapshot.

The short-family investigation remains the best developed main arithmetic
direction within quasi-rh-exponent-descent. Its reductions are substantially
stronger than the earlier small-cofactor formulation, but no new exponent
descent has been proved. The next investment should seek cancellation in
the complete signed tail, with mixed-character energy retained as a parallel
direction. Further improvements to already negligible sectors have low
priority unless they expose new arithmetic structure.

## Progress that changes the research problem

The finite extraction theorem needs one moment at one fixed positive row
exponent, for a fixed character and profile. Finite reuse removes the
prime-deletion error without an initial zero-free strip or an additional
supremum over smaller scales. Its output is

\[
\beta(h,a)=\frac{1+a}{2}+\frac{5h}{12},
\qquad a+\frac{5h}{6}<\frac34
\]

for an improvement over the comparison boundary \(7/8\). At \(h=4/5\),
the permitted loss is \(a<1/12\), and the output is \(5/6+a/2\).
See the manuscript's finite extraction theorem and prime-row equivalence.

The exact truncated inverse preserves overlapping factors, nonsquarefree
zeros, and every deletion mask. It supplies an arithmetic coefficient
structure that an arbitrary bounded-coefficient sieve cannot see. The
profile class \(W=(1+t\partial_t)V\) removes the principal density while
retaining Mellin detection of every possible zero except \(s=1\), which
has its separate classical treatment. The optional recovery of all sharp
profile moments has its stated fixed-row boundary and \(h+a<1\)
conditions; it does not recover every Schwartz-weighted all-row moment.

The radical-dependent cutoff

\[
L_u=Q_uNE_u\asymp N\operatorname{rad}_S(u),\qquad
Y_u=D^{1-\theta}/L_u
\]

makes the actual omitted small-product sector arbitrarily small in the
complete weighted mean square. This is a useful estimate under the
recorded primitive character and Poisson inputs. It applies to principal
rows too: their zero frequency vanishes because of the profile, rather
than because those rows have been omitted.

The signed gcd truncation and complete transformed kernels also do real
work. They control high gcd or overlap sectors and prevent invalid
extensions of the source's positive theorem. The exact second-Poisson
involution, selected-component obstructions, and explicit conductor costs
eliminate several approaches that previously looked plausible.
These conclusions are organized in [notes 11–13](../short_families/notes/13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md)
and the [manuscript review](SHORT_FAMILY_MANUSCRIPT_REVIEW_20261008.md).

## The remaining estimate is a substantial arithmetic theorem

For derivative profiles the adaptive tail moment is equivalent to the
original full moment, up to an arbitrarily small weighted error. A smaller
support region therefore does not yet constitute a weaker cancellation
theorem. Likewise, the averaged prime sixth-power rows are equivalent to
their scalar Möbius target. These equivalences are valuable reductions,
but they prevent treating extraction itself as new cancellation.

The supplied generic physical sieve has the coherent term
\(DH^{1/6}\). Its exponent exceeds the useful target by

\[
(1+h/6)-(h+a)=1-5h/6-a>1/4.
\]

At \(h=4/5\), this is \(1/3-a>1/4\). The actual ordered prime-pair
\(m=1\) component of the adaptive tail has energy at least
\(DH^{1/6}/\log^4D\). This is a lower bound for that selected component,
not for the full tail. A successful argument must retain its cancellation
with other factor classes. Zero integral does not make those classes
separately affordable.

Deleting the coherent rows alone does not close the problem. In the
generic grouped \(m=1\) diagnostic at \(h=4/5\), the four supplied
exponents are \(4/5,17/15,1,11/10\), while the useful budget is below
\(53/60\). Even removal of the \(17/15\) contribution would leave two
oversized terms. The complementary-core bound similarly retains
\(H^{1/3}D^{5/6}\) independently of the core cutoff. Fixed-character
estimates do not supply the conductor uniformity required for a growing
core collection.

The endpoint also has a logical qualification. Moments with
\(h_j\to0\), \(a_j\to0\) would approach RH strength through the
\(u=1\) row alone. Zeta-only quasi-RH supplies no such Hecke-family
moments automatically. A first fixed pair would be a significant new
boundary; it would not by itself establish an iterable descent to RH.
See the [dependency ledger](../notes/RESEARCH_LEDGER_20261008.md).

## Relative priority within exponent descent

| Direction | Recommended role | Reason |
| --- | --- | --- |
| Short families | Main arithmetic investigation | Strongest developed extraction, exact factorization, controlled sectors, and an explicit cancellation target with potential endpoint flexibility |
| Selected mixed-character energy | Parallel investigation for a localized gain | Selector-preserving transposition and repeated-character sectors are controlled; the actual fixed vector may require less than a full operator theorem |
| Fixed-scale feedback | Parallel diagnostic and the most direct zeta-only formulation | An actual fixed multiplicative contraction would improve powers; the signed functional remains unbounded |
| Newman collisions | Bounded certification project | Positive-time large-height control does not address the shrinking-time endpoint |
| Integer quadratic lift | Lower priority until a new signed correlation estimate appears | The target carries stronger family consequences, and individual bounds plus the generic quadratic sieve do not descend |

This broadly preserves the earlier [strategic ranking](STRATEGIC_REVIEW_20261008.md),
while updating the main short-family target to the actual adaptive tail.
The ranking expresses research judgment, not evidence that a proof is close.
If the sole objective is an implication from zeta-only quasi-RH, fixed-scale
feedback deserves greater weight because it does not silently add family
information. No alternative branch currently supplies a proved missing
estimate that displaces short families as the arithmetic lead.

## Techniques worth transferring from the repository

The strongest transfer is the complete signed covariance method from
[prime variance](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/SIGNED_COVARIANCE_CONTINUATION_20261004.md).
There too a semiprime component is too large, including after projection,
and compensation with a smooth-cofactor component is compulsory. The
known anticorrelation is already explained at logarithmic resolution;
its existence alone supplies no fixed power saving.

For the current tail, write \(T=U+R\), with \(U\) its actual prime-pair
\(m=1\) amplitude, and use the normalized weighted inner product from
the moment. Retain

\[
\mathcal E(T)=\mathcal E(U)+2\Re\langle U,R\rangle+\mathcal E(R).
\]

The selected-component lower bound shows that a useful target requires

\[
\frac{\mathcal E(T)}{\mathcal E(U)}
\ll D^{-(1-5h/6-a)+\varepsilon}\log^4D.
\]

At \(h=4/5\), the required relative squared-norm saving exceeds a
quarter power. This is a precise diagnostic for a cross-term calculation:
\(R\) must approximate \(-U\) in the weighted norm with a power rate.
Study the exact combined expression on radical and core shells, retaining
the compensating \(m>1\) and composite-factor terms. A fixed negative
correlation coefficient or a logarithmic residual does not meet the target.

The [product-coordinate arithmetic closure](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
offers a concrete algebraic starting point. On the ideal monoid,

\[
(\mu_K\lambda_u)*(\Lambda_K\lambda_u)
=-(\mu_K\lambda_u)\log N
\]

holds exactly, including deletion zeros, because \(\lambda_u\) is
completely multiplicative. An Eisenstein analogue of the complete mixed
discrepancy form could expose a useful joint cancellation before taking
absolute values. Both cutoff edges and any principal density must remain.
The integer project's analytic remainder, one-sided detector theorem,
and uniformity do not transfer automatically: lattice density, conductor
costs, masks, and the row-dependent selector need their own proofs.

The [mixed-family fixed-vector strategy](../mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md)
is a second useful transfer. Seek a bound for the actual Möbius
coefficient vector and its coupled factors before demanding an arbitrary
coefficient operator estimate or a higher trace. Its bounded primitive
fibers apply only to sixth-power-free rows. Full short-family rows
\(u=\eta vr^6\) have coherent multiplicity and different \(r\)-masks;
those cannot be discarded. Conductor bins or maximal norm thresholds can
organize the adaptive selector, but inserting it into a previously
completed row kernel requires a new argument.

The source already used for the sieve contains a more exploratory idea:
[de Faveri's root-number coupling](https://arxiv.org/html/2610.04045v1#S3.SS2)
retains cross phases for nonsquarefree indices. For cube-free \(d=rs^2\),
with \(r,s\) squarefree and coprime, direct convolution gives

\[
c_z(rs^2)=\mu_K(r)
\#\{r=r_1r_2:(r_1,r_2)=1,\ N(sr_i)\le z\}.
\]

This exact structure is worth retaining before replacing coefficients
by their squared norm. Root coupling becomes trivial when \(s=1\),
including the squarefree semiprime obstruction, so it cannot solve that
sector by itself. The same source's positive central-value moments give
no ready reciprocal-L or Möbius-tail estimate; its general higher-order
moment application also has a field hypothesis absent here at order six.

Finally, the [fixed-scale resonance audit](../fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
should be applied to proposed recurrences. Its complete moving-cutoff
functional preserves forbidden-zero residues. Constant contraction at
\(D\mapsto D^\vartheta\) can give only logarithmic savings, whereas a
strict contraction at \(D\mapsto D/b\) can improve a power. These tests
can reject an attractive but ineffective identity before a long continuation.

## A different support regime worth a bounded scout

The choice \(h=4/5\) is a useful benchmark, not a proved optimum. The
adaptive support in the manuscript gives, for every inner row
\(Nu\le D^h\),

\[
Nm\ll D^{h+\theta},\qquad
Na,Nb\gg D^{1/2-h-\theta}.
\]

Thus \(h<1/2\) can make both Möbius factors long across the entire
inner family, rather than only on coherent or small-radical rows. A
concrete arithmetic check is

\[
h=a=2/5,\quad\theta=1/40,\qquad
\mathfrak M(D,D^{2/5})\ll D^{4/5+\varepsilon}.
\]

It would give \(\beta=13/15=7/8-1/120\), and its inner-row tail has
\(Nm\ll D^{17/40}\), \(Na,Nb\gg D^{3/40}\).
For the full Schwartz moment these exact inner exponents cannot be used
globally: a cutoff \(Nu\le D^{h+\delta}\) changes them to
\(17/40+\delta\) and \(3/40-\delta\); the farther rows can be bounded
using rapid decay and the trivial polynomial tail bound.

This does not make the theorem easier automatically. It shortens the row
family, and its generic-to-target gap is still \(4/15\). Its value is a
different bilinear support geometry. Before further optimization, match
an actual signed estimate to this range and its coefficients. No existing
repo theorem has been identified that closes this target.

## Recommended next deliverable

Derive one complete ideal mixed-discrepancy or cross-Gram expression for
the actual adaptive tail, then seek a new power estimate in a specified
unresolved range. Keep \(h=4/5,a<1/12\) as the main benchmark and test
the shorter-family geometry only against a concrete candidate input.
An initial result on a restricted range must account for its boundary and
cross terms; it does not prove the full moment by itself.

A useful continuation should either establish signed cancellation beyond
the generic bound or identify a new obstruction to the proposed mechanism.
Another Poisson involution, positive gcd triangle bound, finite profile
centering, or parameter certificate alone would not justify claiming
closer proximity to exponent descent. The present assessment validates
the strategic distinction and the displayed rational calculations; it
does not replay the imported deep proofs or establish the open moment.
