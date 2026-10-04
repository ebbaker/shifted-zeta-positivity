# Preliminary investigation: projected prime increments and a complete head budget

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal analytic investigation, not independent specialist refereeing.
No global prime-variance exponent is proved.

The useful next target is a signed prime-block estimate **after** the
prepared projection and the inverse reference metric. Its diagonal cost
remains polynomial. A Galerkin head can remove the head/residual mixed
term exactly, but the full residual still needs an exponential saving
against the elementary baseline. These statements make the finite-head
proposal testable without assigning an unproved sign to its complement.

## 1. Inherited inputs and the fixed-rate conversion

Use the notation and operator domains of the
[centered dual-energy note](../../../../investigations/sonin-critical-boundary/notes/selective-loss-program/03_centered_dual_energy_20261003.md):
on the prepared source space over
\(I_r=(-r/2-a,r/2+a)\), \(a=1/4\),

\[
A=\Gamma+cI\ge I,\quad Q=\Gamma-W_r,\quad
f_r=QF_r,\quad \mathscr X(r)=\langle f_r,A^{-1}f_r\rangle.
\]

Restriction to \(I_r\) precedes the projection \(P_r\) onto the prepared
source subspace, the orthogonal complement of the three moment
representers \(1,e^{x/2},e^{-x/2}\). All prime powers with
\(\log n<r+2a\) are retained.
The inherited bounds are \(A[F_r]=O(1)\) and a uniform bound for
\(\|P_r\Gamma_\infty F_r\|_2\). The positive-square construction gives
an adverse allowance at most \(\sqrt{A[F_r]\mathscr X(r)}\).

Thus, with one fixed \(0<\delta=1-\kappa<1\),

\[
\mathscr X(r)\ll (1+r)^m e^{\delta r}
\tag{1}
\]

suffices for the one-sided growth theorem and hence the closed strip
\(\beta\le(1+\delta)/2\). Polynomial factors are permitted: apply the
one-sided theorem at every slightly larger rate and intersect the closed
strips. The same observation covers all sufficiently large real \(r\),
not only a sampled sequence. The
[project overview](../../PROJECT_OVERVIEW_20261004.md) supplies the final
closed-endpoint variance transfer.

The inherited complete explicit formula also checks that (1) is not
stronger in exponent than the strip target. If that strip is assumed
solely for this converse, the absolutely summable smoothed zero expansion
gives \(p(y)=O(e^{\delta y/2})\). Since \(\delta>0\),
\(J(Y)=\int_0^Yp(y)^2dy=O(e^{\delta Y})\); the established complete
response comparisons then imply \(\mathscr X(r)=O(e^{\delta r})\).
This is a conditional scope check, not an estimate of actual primes.

## 2. Fresh deduction: the diagonal stays small in the actual dual metric

Fix \(r>2a\), put \(Y=r+a\), and define the complete local packet of a
single prime on \([-a,Y]\) by

\[
b_p(y)=\sum_{k\log p<r+2a}\frac{\log p}{p^{k/2}}
                         g(y-k\log p).
\]

Let \(u_p=P_r[(b_p(y)-b_p(r-y))/\sqrt2]\), where
\(y=x+r/2\), and set

\[
q_p=A^{-1/2}u_p,\qquad z_r=A^{-1/2}P_r\Gamma_\infty F_r.
\]

These vectors all use the same window and the same metric; changing the
prime set does not change \(A\). We have exactly

\[
\mathscr X(r)=\Big\|z_r-\sum_pq_p\Big\|_2^2,
\qquad \|z_r\|_2\le C_\Gamma.
\tag{2}
\]

The powers of a fixed prime have disjoint packet interiors because
\(\log p\ge\log2>2a\). Reflection is an isometry on \([-a,Y]\),
and both \(P_r\) and \(A^{-1/2}\) are contractions. Consequently

\[
\sum_p\|q_p\|_2^2
\le2\sum_p\|b_p\|_{L^2[-a,Y]}^2
=2D(Y)=O((1+r)^2).
\tag{3}
\]

Here \(D(Y)\) is the complete truncated packet diagonal, including
partial top packets, in the
[complete-response note](../../../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md).
The last estimate uses its ordinary PNT calculation; its elementary
\(O((1+r)^3)\) bound would suffice equally for every fixed \(\delta>0\).
No disjointness between different primes is assumed.

Define the actual metric cross sum

\[
\Pi_A(r)=2\sum_{p<q}\operatorname{Re}\langle q_p,q_q\rangle,
\qquad D_A(r)=\sum_p\|q_p\|^2.
\]

Then, exactly,

\[
\mathcal Y_A(r):=\Big\|\sum_pq_p\Big\|^2=D_A(r)+\Pi_A(r),
\quad \Pi_A(r)\ge-D_A(r),
\quad
\big|\sqrt{\mathscr X(r)}-\sqrt{\mathcal Y_A(r)}\big|\le C_\Gamma.
\tag{4}
\]

Therefore the remaining sufficient arithmetic input is just

\[
[\Pi_A(r)]_+\ll (1+r)^m e^{\delta r}
\quad\text{for every sufficiently large real }r.
\tag{5}
\]

The positive part is taken after the full signed sum. This is a weaker
metric target than bounding every unprojected pair separately. Neither
the prepared projection nor \(A^{-1/2}\) preserves support locality:
the compact overlap rule for the unprojected packet Gram must not be
reused as a zero-entry rule for \(\langle q_p,q_q\rangle\).

For any ordering or partition into complete prime blocks, writing
\(S_{j-1}\) for the preceding sum gives the exact update

\[
\|S_{j-1}+q_j\|^2-\|S_{j-1}\|^2
=\|q_j\|^2+2\operatorname{Re}\langle S_{j-1},q_j\rangle.
\tag{6}
\]

This identifies the missing signed drift. A bound on the self terms
alone cannot close (5), and block grouping can increase their cost by
internal coherence. The individual-prime bound (3) must not be asserted
unchanged for arbitrary large blocks.

## 3. Fresh deduction: a head removes its mixed term, not its residual

Choose a finite-dimensional head \(H_N\subset D(A)\) with an
\(L^2\)-orthonormal basis \(e_1,\ldots,e_N\), possibly depending on
\(r\). Define the positive matrix and the complete arithmetic data

\[
G_{ij}=\langle e_i,Ae_j\rangle,\quad
b_i=\langle e_i,f_r\rangle,\quad
y_N=\sum_j(G^{-1}b)_j e_j,
\quad R_N=f_r-Ay_N.
\]

Since \(G\ge I\), the head solve has an independently known gap.
The Galerkin equations give \(\langle e_i,R_N\rangle=0\), and
expanding the inherited full-residual identity now yields the exact
orthogonal decomposition

\[
\boxed{\mathscr X(r)=b^*G^{-1}b+
                   \langle R_N,A^{-1}R_N\rangle.}
\tag{7}
\]

The mixed term vanishes because the head was solved against the actual
\(A\)-Gram matrix. It does not vanish for a generic coefficient
truncation or a fit using a different inverse metric. In particular,

\[
\mathscr X(r)\le b^*G^{-1}b+\|R_N\|_2^2.
\tag{8}
\]

The global Fourier inverse from the parent note may replace the second
term by its smaller certified bound, but is not equal to the compressed
source inverse. If \(y_N\notin D(A)\), the displayed \(L^2\) residual
requires a separate form-dual treatment.

For a budget \(B_\delta(r)=(1+r)^m e^{\delta r}\), the complete
sufficient allocation is

| Cost | Required upper bound | Status |
| --- | --- | --- |
| Solved head \(b^*G^{-1}b\) | \(O(B_\delta)\) | Open arithmetic estimate |
| Exact head/residual mixed term | \(0\) | Identity (7) |
| Full dual residual \(\langle R_N,A^{-1}R_N\rangle\) | \(O(B_\delta)\) | Open arithmetic estimate |
| Stronger computable residual \(\|R_N\|_2\) | \(O(B_\delta^{1/2})\) | Optional sufficient replacement |

The residual includes every unrepresented spatial direction, complete
prime-power and terminal bands, all three moments, and arithmetic and
quadrature errors. A residual on the selected coordinates is identically
zero by construction and proves nothing about the table's third row.

Against the elementary response-norm scale \(\operatorname{poly}(r)
e^{r/2}\), a raw residual allowance \(\operatorname{poly}(r)e^{\delta r/2}\)
requires a factor \(e^{-\kappa r/2}\), or \(X^{-\kappa/2}\) with
\(X=e^r\). This compares two budget scales; it is not a claim about the
unknown ratio of the true residual to the true response. Logarithmic
conditioning gains alone cannot deliver this factor.

## 4. Concrete next investigation and assessment

The next bounded experiment should choose one explicit growing head,
derive \(Ae_i\) and all moment projections, and evaluate the full
residual in (7), together with the signed block increments (6). It should
report the head, residual, and signed cross costs separately. A failed
residual budget can reject that head. A favorable finite trend can only
motivate an arithmetic estimate; it cannot establish an asymptotic rate.

The analytic target should be an actual-prime identity controlling the
sum in (5), or the complete residual in (7), at one fixed \(\delta<1\).
Rephrasing (5) as an assumed contraction is not a new ingredient. Fixed
rank repair and independently positive ambient absorption remain ruled
out in their previously audited classes.

**Assessment:** strong parallel program because it has a positive
reference with a known gap and a precise remaining signed quantity.
It deserves a top-three place, but the present work supplies no reason
to expect a finite head or the logarithmic metric alone to produce the
required arithmetic cancellation. Prefer program 01 for the next main
investigation and use this program to test whether its signed arithmetic
relations become sharper after projection and the inverse metric.

## Checks and limits

The contraction constants in (3), the signs in (2)/(6), the Galerkin
orthogonality in (7), and the exponential square-root conversion were
checked directly. The complete packet diagonal, explicit formula,
one-sided theorem, and operator-domain assertions are inherited results
linked above; they were not independently reproved here. No numerical
certificate, asymptotic prime estimate, or new external theorem is claimed.
A separate same-model agent checked the contraction constants and
Galerkin identity; parent review also checked the projection convention.
