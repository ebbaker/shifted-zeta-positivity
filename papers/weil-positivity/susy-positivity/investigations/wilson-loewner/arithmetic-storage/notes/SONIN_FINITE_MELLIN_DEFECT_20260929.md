# Direct first-prime arithmetic diagnostic and a finite Mellin-defect gate

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured effort are not
exposed. This is an internal derivation and computer-assisted diagnostic,
not independent specialist refereeing.

## 1. Question and outcome

The exact prescribed pole-neutral sources are

\[
b=9/20,\quad \phi(x)=e^{-1/(1-(x/b)^2)}1_{|x|<b},\quad
P=-\partial_x^2+1/4,\quad
f_0=P\phi/\|P\phi\|_2,\quad f_1=P(x\phi)/\|P(x\phi)\|_2.
\]

They have unit norm and opposite additive parity. At support length 1,
the only active prime-power delay is \(a=\log2\). Put

\[
\kappa_j(a)=\int f_j(x)f_j(x+a)\,dx,\qquad
\mathfrak a_2[f_j]=\sqrt2\log2\,\kappa_j(a),\qquad
Q_1[f_j]=\Gamma[f_j]-\mathfrak a_2[f_j].
\]

The new Arb/Acb calculation gives the following outward rounded intervals:

| Quantity | Even source | Odd source |
|---|---:|---:|
| Prime correlation | [-0.194741440569596, -0.194741440569595] | [0.295846745258268, 0.295846745258269] |
| Prime form \(\mathfrak a_2\) | [-0.190896882989143, -0.190896882989142] | [0.290006181258082, 0.290006181258083] |
| Direct full arithmetic \(Q_1\) | [1.439237951, 1.439237964] | [1.047808580, 1.047808594] |
| Residual after the first compressed moment | [-7.24075680, 0.40279415] | [-5.81945856, 0.25084343] |

The prime contribution helps positivity for the even source and reduces it
for the odd source. Both full forms remain comfortably positive. Since the
full form commutes with additive reflection, its mixed even/odd entry is
zero. Therefore on this particular two-dimensional complex span,
\(Q_1\ge1.047808580 I\). This is a direct finite-family consequence; stronger
all-input finite-window certificates already existed. It is not a new
continuation mechanism.

The complete residual intervals both contain zero. They use the independent
[first compressed-moment bounds](SONIN_COMPACT_FIRST_MOMENT_20260929.md)
and exclude neither \(R\ge0\) nor source-specific residual negativity. The
prime-correlation calculation by itself does not evaluate \(B_2\). In
particular it cannot turn the directly positive arithmetic answer into a
successful Sonin comparison by definition.

## 2. Certified correlation calculation

Write \(d=b-a/2>0\). Parity and a centered change of variable give

\[
\kappa_j(a)=2(-1)^j d\int_0^1
f_j(a/2-du)f_j(a/2+du)\,du.
\]

The source polynomials and normalization intervals are loaded from the
existing hash-bound `source_norm_enclosures.py` and its record. Acb
integration covers the segments with endpoints
\(0,1/2,3/4,\ldots,127/128,255/256\). On these segments the source formulas
are holomorphic; every callback rejects a complex interval whose source
denominator contains zero. Integration occurs at 192 bits with absolute and
relative targets \(2^{-100}\). The logarithm, endpoint transformation,
normalizers, and coefficients all remain enclosed.

For \(u\ge255/256\), the upper source coordinate is greater than
\(b(255/256)\), so the pre-existing analytic source endpoint-tail bound
covers the omitted region. For a real smooth compact unit source,

\[
\|f\|_\infty^2\le\|f\|_2\|f'\|_2=\|f'\|_2.
\]

If \(T_j\) denotes the raw **both-endpoint** L1 bound and \(N_j\) the
normalizer, the conservative added correlation radius is

\[
2\|f_j\|_\infty T_j/N_j.
\]

These radii are below \(3.51\times10^{-51}\) and
\(4.10\times10^{-51}\). The actual correlation interval widths are below
\(1.34\times10^{-31}\) and \(1.78\times10^{-31}\). The inherited gamma
intervals dominate the final arithmetic widths, approximately
\(1.18\times10^{-8}\) and \(1.34\times10^{-8}\).

The script checks source/gamma/summary generator bindings and summary input
hashes. A separate 256-bit replay gives overlapping rigorous intervals.
Agreement is a consistency check; Acb enclosures and the analytic tail
bound provide the error proof. Earlier source/gamma certificates are used
as certified inputs, not regenerated in this bounded calculation.

Files: [generator](../numerics/arithmetic_prime_diagnostic.py),
[principal record](../numerics/records/arithmetic_prime_diagnostic.json), and
[256-bit replay](../numerics/records/arithmetic_prime_diagnostic_256bit.json).
The residual row above comes from the later
[combined record](../numerics/records/sonin_first_moment_bounds.json); the
prime generator preserves its earlier scalar-only comparison as historical
output.

## 3. Finite Mellin-defect hypothesis: a useful sufficient statement

On pole-neutral sources, a prospective theorem is

\[
R_{S,L}[f]\ge-\sum_{z\in E}c_{z,S,L}|M_z(f)|^2,
\quad M_z(f)=\int e^{zx}f(x)\,dx,
\quad c_{z,S,L}\ge0.
\tag{D1}
\]

Here \(E\) must correspond to a fixed finite set of permitted Mellin zeros
under \(M_{g_0}(s)=M_{s-1/2}(f)\), with none of those Mellin points a
nontrivial zeta zero. If (D1) holds on the full source class for unbounded
nested support windows, and each finite place set contains the active
primes, it proves RH by the restricted-test criterion: impose those finitely
many additional zeros and the correction vanishes exactly. The coefficients
need not be uniform as support grows.

An expanding support-dependent set of moment constraints is not automatically
covered by that criterion. It requires a separate sufficiency argument.
The current calculation proves no instance of (D1). The underlying
restricted-test criterion is discussed in
[Connes and Consani, Weil positivity and trace formula, Appendix C, Proposition 1](https://arxiv.org/html/2006.13771v1),
with the source convention fixed in the
[canonical comparison audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).

For the specific mean-only hypothesis, \(M_0(f)=\int f\), the odd source has
\(M_0(f_1)=0\) exactly. Thus a certified \(B_2[f_1]>Q_1[f_1]\) would refute
the mean-only inequality at this support, regardless of the proposed finite
coefficient. Present bounds are too broad to decide this. A positive
residual on this one source would not prove (D1).

## 4. A finite-penalty lemma and its extra obligation

Let \(R\) be a Hermitian form on a vector space \(V\), and let
\(M:V\to\mathbb C^k\) be a moment map onto its finite-dimensional image.
Choose a linear lifting \(T\) of that image and write
\(f=v+Tm\), where \(v\in V_0=\ker M\). The following are equivalent:

1. For some finite \(c\ge0\), \(R[f]+c\|Mf\|^2\ge0\) for all \(f\in V\).
2. \(R[v]\ge0\) on \(V_0\), and for some finite \(K\),
   \[
   |R(v,Tm)|^2\le K\|m\|^2R[v]
   \quad(v\in V_0).
   \tag{D2}
   \]

For necessity, apply Cauchy--Schwarz in the nonnegative form
\(R+cM^*M\), observing that its cross term on \(v,Tm\) is exactly
\(R(v,Tm)\). Its finite-dimensional restriction to the range of \(T\)
is bounded by a constant times \(\|m\|^2\).

For sufficiency, complete the scalar square:

\[
R[v]+2\Re R(v,Tm)\ge -K\|m\|^2.
\]

The remaining form \(R[Tm]\) has a finite lower bound on the
finite-dimensional moment space, so a finite penalty suffices.

This identifies an extra obligation frequently missed in the finite-defect
idea. Nonnegativity on moment-zero sources is necessary but alone need not
yield a finite correction coefficient. Cross terms must be bounded in that
possibly degenerate residual seminorm and must vanish on its nullspace.
For example, \(R(x,y)=2\Re(\bar x y)\), \(M(x,y)=y\), vanishes on
\(\ker M\), yet no \(c|y|^2\) makes it positive for all \(x,y\).

Applied to the Sonin residual, a useful new kernel theorem must prove both
the constrained sign and this cross-term control. A finite number of
numerically negative directions, without identifying the prescribed Mellin
functionals and controlling the full complement, is insufficient.

The source preparation for an additional mean zero can be kept exact and
support preserving: \(f=\partial_x(-\partial_x^2+1/4)h\).
Thus the next mean-defect test should retain this preparation, both parity
sectors and mixed entries, and the full compressed metric.
