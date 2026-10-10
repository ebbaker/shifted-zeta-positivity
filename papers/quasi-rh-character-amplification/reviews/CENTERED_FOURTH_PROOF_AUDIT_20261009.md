# Proof-level internal audit of the centered fourth-moment induction

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model internal audit, not independent specialist validation
or formal verification of the source theorem.

**No local cancellation, exponent, or quantifier defect was found in the
reviewed proof of source Lemma 18.1.** In particular, transformed principal
and other \(\Theta\)-rows are included; their complete rectangle difference
is retained until its main terms cancel. The small affine width induction,
single-slot overshoot, and slot-count-independent mesh have an explicit
compatible ledger. This strengthens the previous transfer audit: it checks
the critical local proof steps, rather than only the stated moment theorem.
It does not promote the conditional geometry candidate to an established
zero-free theorem or independently validate all its upstream inputs.

## Source and scope

The complete proof read is September 30 source Section 18, PDF pp. 152--180,
Lemma 18.1 and equations (18.1)--(18.52), including its concluding physical-row
paragraph. The local extracted copy is `/private/tmp/quasi-rh-continuation/paper.txt`,
lines 9838--11578; the PDF hash was directly checked as
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The source is the [September 30 paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Also read were Sections 4.2--4.4, the coefficient conventions in Section 13.1,
and the proofs of finite correlations in Lemmas 13.2--13.4. The existing
[moment transfer audit](MOMENT_STRUCTURAL_AUDIT_20261008.md) and new
[conditional theorem ledger](../notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md)
provide the application context. No source, old note, or manuscript was changed.

The audit discharges the local algebra and exponent obligations below under
their explicitly stated number-field reciprocity, Poisson, reflection, and
global-family analytic inputs. The finite checker verifies exact algebra and
specified finite cases; it does not prove those inputs or the unbounded moment.

## 1. The coefficient class is essential and is preserved locally

The source's row character is \(\psi_k(n)=\tau(n)\chi_n(k)\), with
\(M=m+q\). Its displayed moving support includes canceled and six-divisible
factors before reduction on units. One extra squarefree mask is fixed in a
row sum and is common to both plains and every slot. A varying row's natural
zero cannot be reclassified as an externally chosen puncture. These are real
restrictions, not harmless conventions.

Equations (18.4)--(18.6) erase a fixed extra mask by exact inclusion--exclusion
before natural reflection or moment invocation. Its row scalars are bounded
only after the finite identity is formed. Removing a plain divisor or freezing
a slot decreases the nonnegative affine expression; an exhausted slot list
calls the unrestricted zero-slot theorem. A retained subunit scale has a fixed
lower support bound and can be clipped to one with its stated normalization
and profile cost. The mask divisor masses are charged once, with local shares
that may depend on the fixed number of slots.

The positive-slot coefficient condition is also necessary for the pointwise
input (18.12). Every \(\nu_i\) is a fixed finite combination of members of the
finite group \(\Theta\). If the row's primitive inducing character is outside
\(\Theta\), multiplying it by a component cannot make it principal. Conversely,
if this condition were weakened to arbitrary fixed character coefficients,
choose a fixed nonprincipal \(\psi\notin\Theta\) and \(\nu=\bar\psi\).
The slot then has principal prime phase. For a nonnegative nonzero annular
profile, the same fixed-field prime ideal theorem used by the source gives
\(|Q_\psi|^2\asymp P/(\log P)^2\), violating the proposed \(P^{\kappa+o(1)}\)
bound whenever \(\kappa<1\). This is a countercheck to weakening the hypothesis,
not a counterexample to the actual lemma.

Complete genuine support extraction removes every shared prime with its
entire multiplicity and punctures every remaining variable on its side.
The same allocation acts on both rectangles, including a rectangle whose
profile vanishes. A prime shared with a slot freezes that whole slot. The
remaining \(\nu_i\), underlying disjoint slot windows, and whole-product
character stay unchanged. Local amplification has only valuations one,
six, and seven; its squared extraction factors are respectively
\(P^{-1},(1-P^{-1})^2,P^{-1}\). In the six case the residual nonunit zero
is retained as a common puncture, rather than replaced by one.

The full Möbius indicator in both transforms is inserted before independent
columns are estimated. Its off-coprime extension is explicitly artificial.
For a final divisor prime, the factor-allocation identity selects any nonempty
subset of factors that contain it. Writing a selected plain as \(p\ell\)
does not impose \((p,\ell)=1\); quotients can retain the prime and overlap the
other side. A selected prime slot is frozen. These facts preserve the signed
coefficient and avoid an unlicensed coprime-family enlargement.

## 2. Centering includes the cross terms and survives the two transforms

The original and comparison plain scales satisfy \(X_1X_2=Y_1Y_2\).
Their allocated coefficient is the single difference
\[
D_b(\ell_1,\ell_2)=
 W_1(Nb_1N\ell_1/X_1)W_2(Nb_2N\ell_2/X_2)
 -W_1(Nb_1N\ell_1/Y_1)W_2(Nb_2N\ell_2/Y_2).
\]
Both first- and second-transform norms use the square of this difference.
Thus the two rectangle squares and their signed cross terms are included.
Replacing that square by a sum of separate rectangle squares would lose
the exceptional cancellation; two identical rectangles already give an
exact finite countercheck, with centered energy zero and separate energy
positive. The source does not make this replacement in the exceptional branch.

The first transform separates only the row norm and two **whole-product**
norms, on common boxes chosen before fixing live slot labels. It gives one
norm power within each whole column; the two plain variables inherit the
same power. The second transform has the same property. Its two child sides
may have different powers, which causes no problem: each side cancels its
own two rectangle main terms. It would be a problem to give different powers
to the two plains within one side. Equal scale products alone then do not
cancel, as the checker demonstrates.

Lemma 18.2's mask and power conclusion is supported by the explicit operations
preceding it. Frozen slot values and row scalars, including zeros, remain in
the signed identity. The natural row zeros are retained throughout. The two
child inducing characters differ by a member of \(\Theta\), including the
supplementary factor from \(-1\), so either both children are exceptional or
neither is. This comparison concerns primitive inducing characters on units;
it does not divide two zero symbols.

The equal-product lattice cancellation in Lemma 18.3 can be checked directly.
For one fixed exceptional row, its common mask \(R_*\), finite ray character
\(\vartheta\), and whole-product power \(N\ell^{it}\) give
\[
 L_i(X,t)=c_{\vartheta,R_*}X^{1+it}I_i(t)
             +O(Z^{\epsilon_1}(1+|t|)^J).
\]
Fixed-lattice Poisson gives the unmasked constant and bounded error; fixed-mask
inclusion--exclusion costs a divisor bound. In its main term the extracted
\(Nd^{it}\) cancels the \(Nd^{-it}\) from scaling, so the residue constant
is independent of both \(X\) and \(t\). Therefore the product main terms
cancel exactly at equal products. All cross terms with lattice errors remain
in the bound. This works for a complex profile and for the principal character.

In the exceptional branch formal scales are never clipped. If the reference
lower length is \(r\), the first side's saving is \((r-er_1)_+\). With the
opposite extraction and a lower-endpoint divisor dyad, (18.34) gives
\[
t_- -er_1-er_2-(r-er_1)_+
 =(t_- -er_2)-\max(r,er_1)\le\omega_2-r.
\]
This proves the aggregate saving (18.48), even for artificial divisor terms
whose quotients retain divisor primes. It is not an assertion of cancellation
after an absolute supremum or after independent rectangle clipping.

## 3. Transformed principal rows are paid, including newly admitted rows

The original zero-slot family \(R_0\) excludes principal inducing rows,
which is needed for the entire primitive functional equation in reflection.
After a transform, principal and other \(\Theta\)-rows are explicitly counted
and bounded instead of being passed to a nonprincipal moment.

At the second common support, an equal-multiplicity-one nonunit prime has
valuation two in \(G_cV_{\rm id}\). Old moving supports are disjoint from this
genuine support on every nonzero frozen allocation. Exceptional induction
therefore forces \(v_p(h')\equiv4\pmod6\). The fixed sixth-power-free kernel
has norm at least \(Z^{4v_1}\). The source uses only the weaker count
\(Z^{(m'_{\rm act}-f)/6+\epsilon_1}\), \(f=2v_1\), rather than its stronger
available \(2f\) version.

Bounding the partition scalar by one after positivity may admit exceptional
rows that violated an old unit restriction. These rows are included in (18.41).
For example a fixed valuation-one factor admits exceptional row valuations
five modulo six after the original unit condition is erased. The proof does
not claim an extra forcing saving from the unit-prime set \(t_2\). This avoids
an otherwise plausible missing-principal-row error.

The local table in (18.44) is sufficient. In units of a prime's logarithmic
norm, its equal multiplicity-one nonunit contribution is \(F_2=2/3\),
exactly \(2b_2/3\). The extra \(f/6=1/3\) is necessary there. All other
nonzero common-support cases give at least that ratio. The finite-field
correlation formulas behind this table, including six-divisible powers and
nonunit zeros, were checked in exact \(\mathbb Q(\zeta_6)\) arithmetic.

## 4. Exact exponent and induction closure

Six affine ledgers were independently verified as symbolic identities:
the first-transform allowance (18.23), diagonal excess (18.31), strict width
identity (18.32), child allowance (18.33), positive-slot affine defect (18.38),
and exceptional excess (18.42). In particular,
\[
 M'=M+J-g-g_2+t_2\le M-\sigma,
 \qquad \Delta_{\rm child}=b_2-p_2+w+B_c+\ell\ge w+\ell.
\]
The source's local inequalities are also proved on their full ranges, rather
than inferred from a numerical plot:

- For (18.24), write the shared multiplicities as \(i\ge j\). The difference between six times the right
  side and the positive numerator is \(3i+11j-12-5r\), with
  \(r=\mathbf1_{6\nmid i-j}\). It is nonnegative in every relevant case.
- For (18.44), splitting \(J\ge0\) from \(J<0\) gives the stated
  \(F_1\) bound. The maximum additional loss is
  \(w/3+5\sigma/3\le22\sigma/9<3\sigma\). Its \(F_2\) bound is
  primewise, including the multiplicity-one case discussed above.
- With \(L=M/4\), the centered exceptional deficit
  \(A-5M/6-2v/3-(L-v)_+\) has maximum \(A-M\), attained at \(v=L\).
  It therefore costs no additional power beyond the reserved padding
  for the zero-slot core.
- Equation (18.38) is a **positive-slot** bound. Applying it to the
  unamplified zero-slot branch would produce a false \(\sigma\)-sized
  counterexample; that branch has no slot-affine boundary to repair and
  the source does not apply this bound there.

The greedy deletion is performed once after all actual boundary defects have
been included. One whole slot can overshoot the required deleted length, so
\(\kappa d_z\le F_{\rm act}/6+\eta\). It is not \(N\eta\).
Together with the paired coefficient estimate (18.37) and actual-width
enclosure, this gives exactly the edge allowance in (18.40).

All zero-slot bands are completed before positive-slot bands. Within a band,
the uncentered range is completed first; a centered comparison calls that
earlier same-width stage with its strict margin. Each nonterminal transformed
child drops by at least \(\sigma/2\) after the frequency allowance. Each
Gauss norm is amplified at most once and its error norms go straight to the
second transform. These choices exclude a same-band induction cycle.
Triangle inequalities take the maximum exponent; Cauchy averages child
exponents, so a terminal loss is not added at every ancestor.

## 5. Slot-count, derivative, and height quantifiers

The order in (18.52) addresses the delicate mesh requirement. \(\rho,\sigma,\delta\),
finite depth \(D\), aggregate error constant \(C_*\), \(\xi\), and \(\eta\)
are chosen from bounded real ranges and the requested loss before fixing
the eventual slot count. Afterwards \(H_N\), constants, seminorm orders,
height degrees, and the lower threshold may depend on the fixed slot system.

This distinction works because every subset of frozen/live slot support
ratios is bounded by one aggregate \(H_N/\log Z\), and the displayed ledgers
use a fixed list of aggregate lengths. Increasing \(N\) changes the eventual
threshold needed to make that aggregate small. It does not create one fixed
boundary loss per slot. Likewise divisor/allocation constants use an arbitrarily
small power chosen for the fixed \(N\); their masses are not counted again
inside a separated smooth norm.

The Fourier separation integrates the required polynomial height weight over
the full coefficient measure. Kernel Euler derivatives are uniformly bounded
after whole-product normalization, even when the outer scale ratio varies.
Thus a larger derivative order raises a finite input seminorm and a constant;
it does not introduce a hidden \(Z^{J\xi}\) factor. Internal derivative and
height orders are propagated backwards through the finite depth. The later
external tail order changes only the external seminorm, after those internal
orders have been fixed. This agrees with the consolidated theorem's height
absorption order.

At the proposed geometry, \(\kappa=3/4\) is within the lemma's range and
the assumed family baseline gives \(\beta_*\le(1+\kappa)/2=7/8\).
The proof therefore uses its permitted positive-slot prime estimate directly.
No negative source capacity penalty or zeta-only substitution is needed.
The physical prime coefficients and common masks must continue to satisfy
the original finite-\(\Theta\) class.

## Result and remaining source status

The audit supports the centered induction's local closure under its named
upstream inputs and supports its reuse in the conditional geometry theorem.
It found no new missing transformed principal sector, omitted centered cross
term, fixed-power deficit, or slot-count-dependent mesh obstruction.

The remaining imported analytic obligations are the exact moving-character
Poisson bridges with the stated number-field measure and reciprocity phases;
primitive completion/reflection and uniform conductor growth; the global
family strip and logarithmic derivative theorem used for (18.12); and the
finite-order continuity of the complete analytic operations. Their formulas
and dependency order were reviewed here, but finite local-field and exponent
checks are not independent proofs of all that machinery. The consolidated
theorem also needs the separate reflection/inverse and contour/detector
audits. An expert or formal check of these remaining inputs is still a
priority before calling the candidate an established improvement.

The [new checker](../numerics/check_centered_fourth_proof_audit.py) passes
49,273 exact assertions, including 10,530 finite-field correlation cases,
90 prime-power support cases, six symbolic affine ledgers, 8,800 stage branch
cases, mask/centering counterchecks, and greedy/band allocations. Its
[record](../numerics/centered_fourth_proof_audit_record_20261009.json) labels
the local and synthetic scope explicitly. These tests also show why dropping
the six-divisible zeros, full Möbius sum, centered cross terms, or common
whole-product power would change the argument.
