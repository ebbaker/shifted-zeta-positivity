# Final assembly review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are unavailable and are not inferred.
Parallel read-throughs are internal checks, not independent mathematical
review or formal verification.

## Finding and scope

The final composition closes in this internal audit under the earlier
audited inputs and the identified classical imports. No additional
unresolved defect was found between the canonical energy estimate,
the original mean square, fixed-character extraction, and the claimed
zero-free half-plane. This completes the bounded end-to-end source audit
of the pinned October 5 main theorem. It does not establish an
independently validated proof of quasi-RH.

For fixed \(0<\vartheta\le1/10\), every \(\epsilon>0\) gives finite
orders \(J,k\) in the first two links below. A requested \(\delta>0\)
then determines a positive \(\vartheta\) and smaller losses for extraction.
The final links give
\[
\mathcal E(\mathcal H,X,F;\xi,U)\ll \|U\|_{C^J}^2D^\epsilon XF
\quad\Longrightarrow\quad
\sum_{0<N(u)\le D^{1+\vartheta}}|A_u(D)|^2
\ll \|W\|_{C^k}^2D^{2+\vartheta+\epsilon}
\quad\Longrightarrow\quad
A_1(D)\ll_{\nu,S,W,\delta}D^{11/12+\delta}
\]
for every fixed \(\delta>0\). The Mellin identity then excludes zeros
of every fixed finite-order Hecke character in \(\Re s>11/12\);
the norm-lift Euler product transfers the conclusion to every
Dirichlet character, including the principal and imprimitive cases.
The exponent boundary is common to all characters. Constants, support
thresholds and the norm of a test depending on an alleged zero need
not be uniform in conductor or height.

The three detailed ledgers are:

- [Canonical energy to original mean square](../notes/FINAL_ORIGINAL_MOMENT_ASSEMBLY_20261012.md).
- [Sixth-power extraction and Dirichlet norm lift](../notes/FINAL_EXTRACTION_AND_BASE_CHANGE_20261012.md).
- [Mellin holomorphy, identity extension and principal pole](../notes/FINAL_MELLIN_AND_ZERO_FREE_ASSEMBLY_20261012.md).

The source is the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
at openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb,
SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
All source-line references are physical lines. The theorem is at
74–77; extraction and continuation are at 665–770; original reduction
at 1000–1248; canonical estimate and final application at 1261–1277
and 1515–1629. The completed-family and full-transfer proof ranges
are indexed in their own reviews.

## What closes the final links

The original and dual row lengths must remain distinct.
With \(H=D^{1+\vartheta}\), the initial reduction supplies
\[
\mathcal H\le CD^{1-\vartheta}/B^2,\qquad
\Sigma=XF=D/B,\qquad
\mathcal H/\Sigma\le CD^{-\vartheta}/B.
\]
For sufficiently large \(D\), the canonical estimate applies with
\(\kappa=\vartheta/2\) and \(C_0=2\). Nonempty support bounds the
otherwise unrestricted \(F\). Exclusion shifts preserve \(XF\) and
the dual row length; shifted columns below length one are counted
directly, and a dual row bound below one gives an empty sum.
Bounded \(D\) also has a finite counting bound with the permitted
constants.

The unnormalized column moment is \(XF\,\mathcal E\), so its bound
contains \((XF)^2\). Counting the \(b\)-shell and using the original
Poisson coefficient gives
\[
(HB/D^2)\cdot B\cdot(D/B)^2=H
\]
per dyadic block. Divisor counts and the finite dyadic sums consume
reserved positive losses. The diagonal contributes \(O(H)\) to the
smoothed quantity. Its defining outside factor is \(1/D\); restoring
that factor gives \(DH=D^{2+\vartheta}\).
The final smooth-kernel lemma composes derivative orders as \(2J+4\),
after the finite canonical recursion has chosen \(J\).

For prime ideals of norm between \(Y/2\) and \(Y\), with
\(Y=D^{(1+\vartheta)/6}\), the sixth-power rows satisfy
\(\chi_n(p^6)=\mathbf1_{p\nmid n}\). They are distinct rows in the
original moment. Their error relative to \(A_1\) is uniformly
\(O_I(\|W\|_\infty D/Y)\), by ideal counting; their number is
\(\asymp Y/\log Y\), by the fixed-field prime ideal theorem.
With separate positive moment and logarithm losses \(\eta,\lambda\),
the exact square-root exponent is
\[
11/12+5\vartheta/12+(\eta+\lambda)/2.
\]
For a requested \(\delta>0\), one explicit choice is
\(\vartheta=\min(1/10,3\delta/5)\) and
\(\eta=\lambda=\delta/2\). The added exponent is at most
\(3\delta/4<\delta\). These choices precede the large-\(D\) limit.
No estimate is applied at \(\vartheta=0\), and no uniformly bounded
derivative order as \(\delta\) tends to zero is needed.

For each compact subset of \(\Re s>11/12\), choose one positive loss
smaller than its distance to the boundary. This makes the Mellin
integral and all its logarithmic derivatives uniformly convergent
at infinity. Support removes the small-\(D\) endpoint. For
\(\Re s>1\), absolute convergence gives
\[
L_K^S(s,\nu)\mathcal M_W(s)=\widehat W(s).
\]
Hecke continuation extends this identity meromorphically. The principal
pole at 1 is removable in the product; it is not an alleged zero.
For a hypothetical zero \(\rho\), the fixed smooth test
\(W(y)=y^{-\rho}\phi(y)\), \(\phi\ge0\), has
\(\widehat W(\rho)>0\), which contradicts the identity there.
Allowing its norms to depend on \(\rho\) is sufficient.

The Dirichlet norm lift has conductor dividing the chosen modulus
\(q\mathcal O_K\), and its actual conductor can be smaller. For
example, the primitive lift of \(\chi_{-3}\) is trivial. Checking
split, inert and ramified primes gives
\[
L_K(s,\chi\circ N)
=E_q(s)L(s,\chi)L(s,\chi\chi_{-3}),
\]
where the finite correction \(E_q\) and its inverse are holomorphic
in positive real part. Induced Dirichlet Euler factors have the
same property. Away from 1, neither Dirichlet factor has a pole.
At 1, a possible pole occurs only in the principal/\(\chi_{-3}\)
pair; \(L(1,\chi_{-3})>0\), also seen directly from its positive
paired series. Thus no zero is hidden by pole cancellation.

## Whole-chain dependency map

| Link | What was audited | Record and boundary |
| --- | --- | --- |
| Original coefficients and first Poisson reduction | Gauss phases, fixed ray expansion, masks, diagonal, shared-column change, smooth norms and exact initial ranges | [Initial review](INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md); classical reciprocity, Gauss identities and lattice Poisson remain inputs |
| Theta transformation and uniformity | All three cusps, active denominator, fixed and moving masks, conjugation, Mellin normalization, finite derivative bounds | [Theta review](THETA_TRANSFORMATION_REVIEW_20261012.md); primary Dunn–Radziwiłł comparison, original Patterson access limitation retained |
| Completed mean square | Exceptional local terms, coefficient norms, primitive quadratic sieve family, infinite recombination and general rows | [Completed review](COMPLETED_MEAN_SQUARE_REVIEW_20261012.md); Goldmakher–Louvel theorem remains imported |
| Full two-Poisson return | Every signed preimage, zero mode, short scale, common kernel, exclusion-shifted child and finite induction | [Transfer review](TWO_POISSON_TRANSFER_REVIEW_20261012.md); relies on the preceding special-family inputs |
| Original mean square | Gap, ranges, normalization, divisor and dyadic losses, finite smooth orders | [Final moment note](../notes/FINAL_ORIGINAL_MOMENT_ASSEMBLY_20261012.md); no new arithmetic cancellation premise |
| Extraction and nonvanishing | Coherent rows, exact exponents, compact-set convergence, pole handling, norm lift and finite factors | [Extraction](../notes/FINAL_EXTRACTION_AND_BASE_CHANGE_20261012.md) and [Mellin](../notes/FINAL_MELLIN_AND_ZERO_FREE_ASSEMBLY_20261012.md); fixed-field prime counting and Hecke continuation remain imports |

The argument never enlarges the completed-family estimate to arbitrary
sextic coefficient sequences. The signed return is performed before
absolute values; it restores the original arithmetic family. The
recursion decreases the row length by the squared gap ratio in a
nonempty cube tail. Its number of stages is finite for each chosen
positive \(\vartheta\). The principal Möbius bound is extracted from
the positive original moment and is not separately assumed.

## Verification and limits

The new [finite final-assembly diagnostic](../numerics/check_final_assembly.py)
and [record](../numerics/final_assembly_record_20261012.json) check the
exact normalization and exponent algebra, boundary scale examples,
coherent-row masks, and Euler polynomial identities. The
[CLI validation](../numerics/final_assembly_cli_validation_20261012.json)
checks source-hash rejection and execution without a third-party source.
The [replay guide](../numerics/README.md#final-assembly-bookkeeping)
states the finite coverage and negative controls. Final run counts
are recorded there and in the JSON; they are arithmetic diagnostics,
not counts of independent theorem validations.

The classical prime ideal asymptotic is stated in
[Burgin's primary paper](https://arxiv.org/html/2406.08565v1);
Hecke continuation is matched to the completed formulation in
[Poonen's MIT Tate notes, Theorem 5.22](https://math.mit.edu/~poonen/786/notes.pdf).
The notes distinguish these imports from the audit's own exponent,
Mellin and Euler-factor derivations. They also record the
[NIST Dirichlet continuation and nonvanishing statements](https://dlmf.nist.gov/25.15).
No external theorem's full proof is certified by citing its statement.

The finite checks prove neither analytic Poisson nor theta automorphy,
the quadratic large sieve, infinite estimates, or holomorphic
continuation. The previous reviews' exact scopes are preserved.
In particular, the original Patterson proof was not independently
read, and internal parallel LLM checks do not substitute for
independent mathematical review.

## Decision

There is no further unassembled source link in the bounded main-theorem
chain identified by this investigation. The appropriate next scrutiny
is an independent review of the full argument and its deep imported
interfaces, particularly the original cubic theta theorem and the
precise cusp coefficients used here. This is a change in review level,
not a newly identified missing cancellation estimate.

The manuscript's quantitative introduction corollaries, effective
constants, and later stronger strips were outside this assembly.
They are not promoted by the qualitative fixed-character argument.
No manuscript or third-party source was changed, and no new zero-free
result is claimed as independently established by this audit.
