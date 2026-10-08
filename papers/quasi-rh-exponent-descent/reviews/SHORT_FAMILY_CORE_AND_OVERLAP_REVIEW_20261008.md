# Scoped review: source corrections, core involution, overlap and replication limits

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is same-model internal review, not independent specialist validation.

Reviewed the [core involution](../short_families/notes/SHORT_FAMILY_CORE_INVOLUTION_20261008.md),
[overlap estimate](../short_families/notes/SHORT_FAMILY_HIGH_OVERLAP_20261008.md), and
[replication limits](../short_families/notes/SHORT_FAMILY_REPLICATION_LIMITS_20261008.md). The October 5 primary
[TeX source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
was compared with rendered PDF pages 13--17. Its Gauss/reciprocity identities
and primitive Poisson formula remain imported inputs; its deep theta and
moment proofs were not replayed. No new arithmetic moment or zero strip is
certified by this review.

## Required source corrections

The source uses
\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad
W_0(t)=t^{-1/2}\overline{W(t)},\qquad
\overline{\nu(t)}G(t^{-1})=\sum_\xi c_\xi\xi(t).
\]
Its transformed profile is then
\(W_0(N(bfm_1)/D)\overline{W_0(N(bfm_2)/D)}\).
The earlier small-cofactor note omitted the two overbars in the definitions.
The first error changes a nonconstant angular factor; the second matters for
complex profiles. Both have been explicitly corrected in the note and recorded in its
earlier review. There is no additional conjugation of \(c_\xi\) under the
displayed repair. Modulus bounds and profile seminorm estimates survive it.

## Exact core and actual-prime obstruction

For \(b=f=1\), distinct coprime squarefree columns, and
\(\psi=\chi_{m_1}\overline{\chi_{m_2}}\), masked Poisson has no excluded
factor or zero frequency and gives
\[
K=\frac{\sqrt{N(m_1m_2)}}H\gamma(\psi)
\sum_{u\ne0}\overline{\psi(u)}\Phi(Nu/H).
\]
The primitive CRT identity, source (4.4), and source (4.7) give exactly
\[
a_\xi(m_1)\overline{a_\xi(m_2)}\gamma(\psi)
=\mu_1\mu_2\xi(m_1m_2^{-1})G(m_1m_2^{-1}).
\]
The physical normalization is \(1/D\). After the finite \(c_\xi\) sum,
the residual \(\psi(-1)\) factor is removed by \(u\mapsto-u\), using
radiality. This returns the original coprime off-diagonal Moebius form,
with the original \(\overline\nu_1\nu_2\), physical profiles, and zero
extensions. The claimed involution is correct. Unit symmetry removes
cross terms with different characters on the six units; this is only a
fixed finite-class restriction.

For \(\nu=1\) and nonnegative nonzero annular \(W\), restriction to
distinct prime-ideal columns turns this core into a positive prime-only
moment minus its full diagonal. The \(\asymp H^{1/6}\) explicit rows
\(r^6\), \(Nr\le H^{1/6}\), all have weight at least one and character
value one on every supported prime. The masks really are one: supported
prime norms are \(\asymp D\), larger than \(Nr\) for fixed \(h<1\).
The prime ideal theorem and lattice counting therefore give
\[
\mathcal C_{\rm prime}\gg
\frac{D H^{1/6}}{(\log D)^2}-O(H/\log D)
\gg\frac{D^{1+h/6}}{(\log D)^2}.
\]
The diagonal is too small to cancel this for \(0<h<1\). A target-sized
bound for every such selected core would require \(a+5h/6\ge1\),
whereas improving \(7/8\) requires \(a+5h/6<3/4\). This is an
actual-coefficient obstruction to estimating every prime/composite piece
separately. It is not a lower bound for the full signed core or remainder,
where compensating terms remain. No unrestricted moment counterexample
is claimed or implied.

## Uniform completion and overlap counting

The all-scale Schwartz bound
\(\sum_{\ell\ne0}|\widetilde\Phi(tN\ell)|\ll t^{-1}\) is valid for
every \(t>0\). In each divisor term of the masked Poisson formula its
product with \(R_{12}/(Nd\sqrt Q)\) is \(O(\sqrt Q)\). Nonprincipality
removes the zero frequency. Consequently
\[
|K_f|\ll\tau(g)\sqrt Q,
\qquad |K_f|\ll_\varepsilon D^\varepsilon
\min\{R_{12},\sqrt Q\}.
\]
The second inequality also handles row scales below one: a nonempty
compactly supported row sum forces a fixed positive lower bound for its
scale, and otherwise the sum is empty.

With \(X=D/(BF)\), there are \(O(X^2/G)\) column pairs of gcd norm
\(\asymp G\). Multiplication by \(O(BF)\), the exterior factor
\(O(HB/D^2)\), and the kernel bound gives
\[
|S_{\xi;B,F,G}|\ll_\varepsilon D^\varepsilon
\min\{D^2/(B^2FG),\ HD/(BF^2G^2)\}.
\]
The count is valid also for bounded nonempty quotient scales; impossible
blocks are empty. Divisor factors and the logarithmic block count fit
inside the arbitrary epsilon loss.

The new estimate permits any selector of \(b,f,m_1,m_2\) of modulus at
most one that is independent of the row \(k\). It bounds each complete
row kernel before absolute summation. It does not permit a sharp cutoff
inside that kernel. Separately, the imported positive moment must still
be applied to complete large-\(b\) blocks before pair restrictions.

The cutoff \(BF^2G^2\ge D^{1-a}\) is unambiguous for dyadic lower
endpoints. The stated actual-norm sufficient cutoff with factor 32 is
correct, since each term's norm product is strictly less than
\(2\cdot2^2\cdot2^2=32\) times its lower-endpoint product. Boundary
blocks may remain in the residual. These details justify the enlarged
controlled sector, but at \(B=F=G=1\) the generic bound remains \(HD\).

## Replication limits

The composite-mask Euler completion and inverse are exact. The inverse
Euler product is \(O_\eta((Nr)^\eta)\) for any positive target exponent;
restricting the reverse implication to large primes then proves the
claimed equivalence. Treating a composite \(r\) as if it removed only
primes of norm \(\asymp Nr\) would be incorrect, and is explicitly
avoided. All sixth powers improve prime-only replication only by a
logarithmic count factor.

The weighted Cauchy--Schwarz bound \(J_{\rm eff}\le R\) and the
nonnegative-weight comparison are correct within their stated extraction
method. They exclude no new signed correlation input. The map
\(v\mapsto v^k\) has bounded multiplicity at most \(k\), which is
sufficient to restrict the sextic moment. With inherited parameters
\(h_d=dh/6\), \(a_d=a+h-h_d\), both the extracted floor and mask
contraction remain exactly those of the sextic family. Fixed-core near
repetitions twist the target and do not replicate the untwisted sum.

One scope clarification was requested and applied: the standalone order-\(d\)
formula now states \(a_d\ge0\) and \(0<h_d<d\) when invoking its
finite contraction. All actual inherited parameter choices already
satisfy this restriction. No other blocking finding remains within
the scope reviewed here, after the source definitions were corrected.

## Added audit: the newly located sixth-order sieve baseline

Also reviewed the [generic sieve baseline](../short_families/notes/SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md) against
de Faveri, *Optimal large sieve for fixed order characters*,
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1 and
Sections 2.2--2.5. The stated theorem permits sixth-power-free indices on
both sides. Its proof was not replayed. It is a newly imported preprint
theorem, not a result derived from the earlier source.

The family comparison is adequate. In the Eisenstein PID, the fixed
construction gives \(v_0=\epsilon_v x m_Ej_0^6\). The native symbol
\((v_0/n)_6\) agrees with
\(\chi_n(\epsilon_v)\chi_v^{\rm DF}(n)\) away from finitely many
temporary decomposition primes. This identifies the inducing Hecke
characters; both zero extensions on good ideals exclude exactly the
primes of the sixth-power-free ideal \(v\). Hence those temporary primes
do not create extra masks. Partitioning the at most six values of
\(\epsilon_v\) makes its column twist independent of the averaged row.
The source-compatible original orientation already puts the physical
row in the numerator of the residue symbol, so no unsupported matrix
transposition is involved. A common conjugate orientation has the same
operator bound by conjugating coefficients.

The decomposition into sixth powers and a sixth-power-free part is exact
up to the explicitly counted units. Bad-prime exponents in the latter
part are at most five, so only a fixed finite splitting is required.
For every fixed \(r\), the coefficient mask \(\mathbf1_{(n,r)=1}\)
remains in the coefficient vector; its squared norm is \(O(D)\).
Positivity enlarges only a row subclass with that vector fixed. The sums
over \((Nr)^{-6},(Nr)^{-5},(Nr)^{-2}\) converge, and the remaining
constant term counts \(O(H^{1/6})\) ideals. Thus the asserted normalized
upper bound
\[
(DH)^\varepsilon\bigl(H+DH^{1/6}
+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\bigr)
\]
is valid conditional on the imported theorem. Empty row scales below
one need no theorem extrapolation. Schwartz row weights follow by
dyadic shells using the same polynomial bound and sufficient decay.

For \(1\le H\le D\), the expression is
\(O_\varepsilon(D^{1+\varepsilon}H^{1/6})\). Its exponent matches the
sixth-power prime-row lower bound for the broad coefficient class and
gives only the extraction floor one. No conclusion of failure for the
actual unrestricted Moebius moment follows. The draft preserves this
distinction, and no additional correction is requested.

## Finite replay

The coordinating review reran the new standard-library checker. Its 9,356
exact assertions passed and its JSON output matched the retained record
byte-for-byte. These are finite coefficient/Fourier identities and rational
exponent checks. They support the bookkeeping and detect the conjugation
errors; they do not establish the analytic inputs or the missing moment.
