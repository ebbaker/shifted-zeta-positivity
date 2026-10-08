# Scoped review: the diagonal-subtracted small-cofactor reduction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed to this agent and are not inferred.
This is same-model internal review, not independent specialist validation.

Reviewed: [SHORT_FAMILY_SMALL_COFACTOR_20261008.md](../notes/SHORT_FAMILY_SMALL_COFACTOR_20261008.md).
The transformed formula, masks, conductor, second-Poisson scale, total-cost
bound, and valid-range reuse of the source moment pass this scoped check.
No new bound for the residual signed quadratic form is proved by the review.

The [October 5 primary source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf)
was inspected through its local PDF text, Sections 4.1–4.4 and Proposition 5.1.
The PDF hash was checked as
`f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`.
This verifies which source and formulas were read, not their deep proofs.
The finite Gauss/reciprocity identities and the stated dual moment are imported
inputs; their full analytic proofs and any formalization were not replayed.

## 1. Original diagonal and transformed weights

The original full column diagonal contributes \(O(H)\) to the normalized
moment. Its character factor is the indicator of coprimality between the row
and the column, bounded by one. Annular ideal counting gives \(O(D)\)
columns, the normalized Schwartz lattice sum is \(O(H)\), and the original
factor \(D^{-1}\) gives the claimed result. No cancellation is needed.

The transformations preserve the exclusion precisely:
\(n_j=gz_j\), \(z_j=vm_j\) imply
\(n_1=n_2\iff z_1=z_2\iff m_1=m_2\). This includes the pairs introduced
when the coprimality condition is expanded by Möbius inversion. There is no
justification for removing only the first zero frequency and then calling
the entire transformed diagonal absent; the note correctly removes it at
the start instead.

The source's equation (4.16) has exactly the outside factor \(H/D^2\),
coefficient \(\mu(f)Nb\), physical profiles at \(N(bfm_j)/D\), and Fourier
argument \(HNk/((Nf)^2Nm_1Nm_2)\) used in the note. The factors
\(\chi_{m_j}(f)^4\) retain the \(f\)-coprimality zeros; the \(b\)-mask
is also retained. The source bijection and its inverse preserve squarefree
variables and impose no extra coprimality between the resulting two columns.
The exact finite transformations do not require the source's later
long-family relation \(H>D\).

## 2. Second Poisson, including the conductor and every mask

For squarefree columns, write
\(g=(m_1,m_2)\), \(c=m_1m_2/g^2\). The local exponents of the ratio
character are \(+1\) and \(-1\) on the disjoint prime supports outside
\(g\). At every allowed prime the local sextic character has exact order
six, so neither exponent becomes principal. Thus, for distinct columns,
the primitive conductor is exactly \(c\), and its zero frequency vanishes.

At a shared prime the phases cancel but both original factors still vanish
on nonunits. Consequently the ratio is
\(\psi_c(k)\mathbf1_{(k,g)=1}\), not merely \(\psi_c(k)\).
The note's use of the masked Poisson lemma is necessary and correct.

With \(G=Ng\), \(Q=Nc=Nm_1Nm_2/G^2\), and
\(R_{12}=(Nf)^2Nm_1Nm_2/H\), the source's Lemma 4.2 gives, for each
\(d\mid g\), Fourier scale and absolute prefactor

\[
 t_d=\frac{R_{12}}{Nd\,Q}
     =\frac{(Nf)^2G^2}{HNd}\ge\frac{(Nf)^2G}{H}=Z,
 \qquad \frac{R_{12}}{Nd\sqrt Q}.
\]

The normalized primitive Gauss factor has modulus one. The transform of the
fixed smooth compactly supported \(\widehat\Phi\) is Schwartz, with fixed
seminorms. Two-dimensional lattice counting in the norm variable gives
\(\sum_{\ell\ne0}|\widetilde\Phi(tN\ell)|\ll_A t^{-A}\) for
\(A>1,t\ge1\). Summing over divisors yields exactly the stated bound
\(\tau(g)R_{12}Q^{-1/2}Z^{-A}\).

This argument would fail if an arbitrary sharp cutoff in \(k\) had been
inserted before the second Poisson sum. The note uses the complete original
smooth row kernel; the residual selector depends on column/cofactor data
and is independent of \(k\). Thus it does not introduce that failure.

## 3. Total cost and valid large-cofactor blocks

In a dyadic block, ideal counts and the physical support give
\(O(BFX^2)\) choices, with \(X=D/(BF)\), outside weight \(O(HB/D^2)\),
and \(R_{12}\asymp D^2/(HB^2)\). Multiplying these quantities and using
\(Q^{-1/2}\le1\) produces the factor \(D^2/(B^2F)\) in the note.
The sector \((Nf)^2G\ge HD^{2\eta}\) then contributes
\(O(D^{2+\epsilon-2\eta A})\) per block. The divisor and dyadic factors
can be absorbed for fixed \(\eta>0\); choosing \(A\) sufficiently large
gives the stated arbitrary power saving. The constants depend on the chosen
Schwartz seminorms, buffer, and target saving, as they must.

For the complete blocks \(B\gtrsim D^{1-h+\eta}\), the source parameters
satisfy \(R/(XF)\ll D^{-\eta}\). After fixed support constants are absorbed,
Proposition 5.1 applies with the stated strict buffer and polynomial length
bounds. The mask comparison preserves \(XF\). The smooth two-variable
kernel is exactly the source's kernel, and its derivative bounds are uniform
because its normalized frequency parameter remains bounded. No pair-dependent
sharp selector is inserted into that positive moment application.

The source theorem requires column scale at least one. If a mask shift makes
that scale smaller than one, a nonempty profile still bounds it below by a
fixed positive constant. Only finitely many ideals can then occur in the
column sum; direct row and ideal counting gives \(\mathcal E\ll R\), which
is sufficient under the same \(R\ll(XF)D^{-\kappa}\) bound. If the row
range is below one it is empty. These boundary cases justify the note's
brief direct-counting provision; they do not require extrapolating the
imported theorem outside its hypotheses.

The transformed diagonal reintroduced by the positive enlargement has block
cost \(FX=D/B\), which is \(\ll HD^{-\eta}\) in this range. Removing it
again therefore preserves the \(O(HD^\epsilon)\) estimate. Treating the
whole large-\(b\) blocks first and the second-Poisson sector afterwards is
essential to this conclusion and is correctly specified in the note.

## 4. The positive-theorem obstruction and remaining scope

The unit-column test in the source's positive dual moment is admissible. A
fixed smooth profile isolating norm one makes its inner sum identically one,
with the actual source coefficient \(a_\xi(1)=1\). The result is
\(\mathcal E(R,1,F)\asymp R\). At \(b=1,F=D,H=D^h\), this is
\(D^{2-h}\), contradicting a uniform bound \(D^{1+\epsilon}\) for
\(\epsilon<1-h\). It does not contradict the original Möbius moment,
whose entire original diagonal is affordable and whose transformed residual
is signed. The distinction is explicitly preserved.

The remaining restrictions

\[
 Nb<D^{1-h+\eta},\qquad (Nf)^2N(m_1,m_2)<HD^{2\eta},
 \qquad m_1\ne m_2
\]

follow from the two controlled sectors. The residual still contains its
actual Gauss coefficients, original masks, complete smooth row kernel,
coupled physical profiles, and the sign \(\mu_K(f)\). The note does not
replace that form by independent row/column estimates or claim its required
bound. The further deduction \(Nm_j\gg D^{h/2-2\eta}\) uses the original
annular support and both residual cofactor upper bounds and is correct up
to its fixed support constant.

Ran the accompanying finite check: 51,040 local mask comparisons, 56
complete-period sums, and the rational exponent identities passed. These
test local coefficients and bookkeeping only; they are not a numerical or
formal proof of the analytic Poisson input or of the missing signed estimate.
No outstanding correction was identified within the reviewed scope.
