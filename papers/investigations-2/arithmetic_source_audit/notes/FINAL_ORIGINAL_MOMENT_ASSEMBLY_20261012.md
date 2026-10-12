# Final assembly of the original mean square

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are unavailable and are not inferred.
This is an internal source audit, not independent specialist validation
or formal verification.

## Source, inputs, and conclusion

Pinned [October 5 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex):
openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb,
SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
All line references are physical source lines.

The [completed-family review](../reviews/COMPLETED_MEAN_SQUARE_REVIEW_20261012.md)
and [full-transfer review](../reviews/TWO_POISSON_TRANSFER_REVIEW_20261012.md)
supply the two inputs to the finite canonical induction. The
[initial reduction](INITIAL_POISSON_REDUCTION_AUDIT_20261012.md)
supplies the original family's precise dual ranges, diagonal, and smooth
kernel. This note checks their final composition at lines 1000–1022,
1204–1248, and 1613–1629, without replacing the special arithmetic
coefficient sequence by arbitrary sextic coefficients.

Under those audited inputs and their stated classical imports, the
original mean square has the claimed form
\[
\sum_{0<N(u)\le D^{1+\vartheta}}|A_u(D)|^2
\ll_{\nu,S,I,\vartheta,\epsilon}
\|W\|_{C^k(I)}^2D^{2+\vartheta+\epsilon},
\qquad 0<\vartheta\le1/10.
\]
The integer \(k=k(\vartheta,\epsilon)\) is finite and independent of the
support interval \(I\). Constants may depend on \(I\), the fixed character
\(\nu\), its fixed ray data and excluded set \(S\), and the displayed losses.
This is a conditional assembly deduction from the earlier ledgers, not
an independent proof of their deep inputs.

## Initial ranges meet the canonical estimate

Distinguish the original row length \(H=D^{1+\vartheta}\) from the dual
row length \(\mathcal H\). The initial reduction gives, for fixed \(C\),
\[
B,F\ge1,\qquad X=\frac D{BF},\qquad
\Sigma=XF=\frac DB,\qquad
0<\mathcal H\le\frac{CD^{1-\vartheta}}{B^2}.
\]
Consequently
\[
\frac{\mathcal H}{\Sigma}
\le\frac C B D^{-\vartheta}\le CD^{-\vartheta}.
\]
Once \(D^{\vartheta/2}\ge C\), this is at most
\(D^{-\kappa}\) with \(\kappa=\vartheta/2>0\).
The constant affects the starting threshold; it does not consume the
eventual exponent gap.

For a nonempty dual energy with \(\mathcal H\ge1\), at least one column
has \(N(n)/X\in I=[a,b]\), so \(X\ge1/b\). Thus
\(F=\Sigma/X\le bD/B\). If also \(X\ge1\), then \(F\ge1\) and
\(\Sigma\le D\), so all the canonical hypotheses hold for large \(D\).
The source uses the harmless common polynomial bound \(C_0=2\).
In this application one could use the tighter product bound; using two
also absorbs fixed support constants in intermediate individual lengths.
No arbitrary \(B,F\) with empty column or row support requires induction.

Exclusion removal sends
\[
(X,F)\longmapsto\left(\frac X{N(d)},FN(d)\right).
\]
It preserves \(\Sigma\), \(\mathcal H\), \(B\), and the initial gap
exactly. A nonempty shifted column again has \(X/N(d)\ge1/b\).
If this new length is at least one, the canonical estimate applies;
if it is below one, use the next direct-count case. The proof does
not assume that every divisor shift keeps the column length above one.

In the common-test step of the original reduction the support is the
fixed enlarged interval \(I_*=[a_0/8,2b_0]\), rather than the original
\(I=[a_0,b_0]\). Apply the preceding support and counting arguments
with \(I_*\); in particular the shifted lower bound there is
\(X/N(d)\ge1/(2b_0)\). This only changes the permitted constants.

## Short, empty, and bounded ranges

If \(\mathcal H<1\), there are no nonzero Eisenstein rows of norm at most
\(\mathcal H\). If \(X<1/b\), the column support is empty. For
\(1/b\le X<1\), the column set has bounded cardinality depending only
on \(I\). The coefficients and zero-extended character factors have
modulus at most one, and the squarefree \(f\)-shell contains \(O(F)\)
ideals. Therefore
\[
\mathcal E(\mathcal H,X,F;\xi,W)
\ll_I\mathcal H\|W\|_\infty^2.
\]
For large \(D\), the initial gap makes this
\(\ll\Sigma\|W\|_\infty^2\). This remains valid for every exclusion shift
because its product and row length are unchanged.

For \(2\le D\le D_0(C,I,\vartheta)\), nonempty row support bounds
\(B^2\le CD^{1-\vartheta}\), and nonempty column support bounds
\(F\le bD/B\). Hence \(\Sigma\) is bounded away from zero and all
remaining ranges are bounded, with constants allowed to depend on
\(C,I,\vartheta\). Direct counting covers this compact range. The
same conclusion for the original family follows by counting its
finitely many supported columns and rows. No additional derivative
order or limiting argument is needed here.

## Recovering the unnormalized original moment

The auxiliary energy is normalized by \(1/(XF)\). Thus the initial
column sum satisfies
\[
\sum_{f,k}|S_U(b,f,k)|^2=XF\,\mathcal E_{(b)}.
\]
Apply the auxiliary target with loss \(\epsilon/4\); exclusion removal
introduces at most the square of the divisor count of \(b\), with
\(N(b)\ll_I D\). Reserve another \(\epsilon/4\) for that factor.
The result is
\[
\sum_{f,k}|S_U(b,f,k)|^2
\ll D^{\epsilon/2}(XF)^2\|U\|_{C^J}^2.
\]
The second \(XF\) is essential: it comes from undoing the energy's
normalization.

The coupled two-column kernel has uniform \(C^q\) norm
\(\ll_{I,\Phi,q}\|W\|_{C^q(I)}^2\). The smooth mean-square lemma uses
\(q=2J+4\); it applies after obtaining a bound for every common test
function \(U\). Positivity may enlarge the Fourier row range because
the original row-dependent kernel is zero outside its support.
The fixed ray-character sum has finitely many terms.

For one dyadic \(B,F\) block the remaining normalization is
\[
\frac{HB}{D^2}\cdot O(B)\cdot(XF)^2
\ll\frac{HB^2}{D^2}\left(\frac DB\right)^2=H.
\]
The factors are respectively the original Poisson coefficient,
the count of \(b\)'s, and the column energy just bounded. There are
\(O_I((1+\log D)^2)\) nonempty blocks; their logarithms use the
remaining \(\epsilon/2\). The zero Fourier mode contributes
\(Z\ll_{I,\Phi}H\|W\|_\infty^2\). Nonzero diagonal frequencies were
already retained in the initial reduction.

Finally the smoothed quantity at lines 1031–1034 is
\[
\mathcal M_D=\frac1D\sum_u\Phi(N(u)/H)|A_u(D)|^2.
\]
Since \(\Phi\ge1\) on \([0,1]\), restoring this outside factor gives
\[
\sum_{0<N(u)\le H}|A_u(D)|^2
\le D\mathcal M_D
\ll \|W\|_{C^q(I)}^2DH D^\epsilon
=\|W\|_{C^q(I)}^2D^{2+\vartheta+\epsilon}.
\]
The lattice point \(u=0\) in the majorized quantity causes no difficulty:
with the source's zero extension its column sum only receives the unit
ideal, which lies outside the fixed support for large \(D\). It is
also handled by counting for bounded \(D\).

## Quantifiers and remaining scope

The canonical induction has finitely many stages depending on
\(\kappa,C_0\); each stage chooses a smaller positive loss and a finite
derivative order before any row or dyadic summation. The transfer order
is \(4m+12\); the final smooth-kernel step is \(2J+4\).
The fixed support boxes can expand finitely many times, which changes
constants, not the declared independence of the derivative order from
\(I\). Taking \(\vartheta\) small later may enlarge the number of stages
and the derivative order; it is always fixed and positive in this proof.

This assembles the original mean square from the already audited
special family. The further extraction and zero-free deductions are
recorded in [the extraction/base-change note](FINAL_EXTRACTION_AND_BASE_CHANGE_20261012.md)
and [the Mellin note](FINAL_MELLIN_AND_ZERO_FREE_ASSEMBLY_20261012.md).
The ultimate [review](../reviews/FINAL_ASSEMBLY_REVIEW_20261012.md)
states what this completes and which external proof inputs remain imports.
