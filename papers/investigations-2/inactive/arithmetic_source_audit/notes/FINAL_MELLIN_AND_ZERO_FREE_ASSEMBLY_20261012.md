# Mellin holomorphy and the fixed-zero contradiction

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. The exact serving
variant and configured reasoning effort are unavailable and are not inferred.
This is an internal mathematical audit, not independent specialist validation
or formal verification.

## Source, scope, and finding

The source is the [October 5 manuscript at openai/math revision
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
read from `/private/tmp/arithmetic-source-audit-20261012/paper2.tex`.
Its SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Physical-line references below use those bytes. The theorem is at 74–77;
the relevant saving and Mellin argument occupy 715–757; the Dirichlet
conclusion occupies 759–770.

**Finding:** conditional on the saving at 723–724 for every fixed complex
smooth compactly supported test, the Mellin step is valid throughout
\(\Omega=\{\Re s>11/12\}\). No substantive gap was found in the small-scale
cutoff, local uniform convergence, choice of a test depending on an alleged
zero, or meromorphic identity theorem. The principal pole at 1 requires
interpreting the displayed product identity meromorphically; this is legitimate
and forces its pole to be removable. Finite Euler factors are nonzero in the
larger region \(\Re s>0\).

The saving is an input here. This audit does not independently validate the
new family mean square, nor establish the source's quantitative corollaries.

## 1. Exact input and its quantifiers

Put \(\alpha=11/12\). Fix a finite-order Hecke character \(\nu\), a finite
set \(S\) containing its conductor primes and the primes above 2 and 3, and
\(W\in C_c^\infty((0,\infty);\mathbb C)\). The needed conclusion is

\[
 |A_1(D)|\le C_{\nu,S,W,\epsilon}D^{\alpha+\epsilon}
 \quad(D\ge2),\qquad\text{for every }\epsilon>0.
\]

The source obtains it by selecting a strictly positive \(\vartheta\) and
then the moment loss, depending on the requested final loss (715–724).
No estimate at \(\vartheta=0\) or derivative order uniform as
\(\epsilon\downarrow0\) is needed in the Mellin argument. Constants may
depend on the fixed character, test and loss.

## 2. Small \(D\) and the bounded middle interval

Take \(0<a<b<\infty\) with \(\operatorname{supp}W\subset[a,b]\).
Every nonzero integral ideal has norm at least 1. A summand can be nonzero
only if \(N(n)\le bD\). Hence

\[
 A_1(D)=0\quad\text{for }0<D<1/b.
\]

For the particular test supported in \((1,2)\), the simpler cutoff
\(D<1/2\) suffices. There is no hidden integral down to a nonzero power
singularity at 0.

On any bounded positive \(D\)-interval, only finitely many ideals can
occur. Thus \(A_1(D)\) is bounded and smooth there. The integral between
the support cutoff and 2, if nonempty, is an entire function of \(s\):
the parameter \(D\) ranges over a fixed compact subset of
\((0,\infty)\), and every derivative introduces only a bounded factor
\((\log D)^r\). If \(1/b>2\), the integral from 0 to 2 vanishes and the
same conclusion applies. The saving is only required for the tail.

## 3. Local uniform convergence on the entire half-plane

Let \(T\subset\Omega\) be compact and set
\(\delta=\min_{s\in T}\Re s-\alpha>0\). Use the input saving once with
the fixed choice \(\epsilon=\delta/2\). For \(D\ge2\),

\[
 |A_1(D)D^{-s}|\le C_{\nu,S,W,\delta/2}D^{-\delta/2}
 \qquad(s\in T).
\]

This is integrable with respect to \(dD/D\). For each integer
\(r\ge0\), the parameter derivative has the additional absolute factor
\((\log D)^r\), and

\[
 \int_2^\infty D^{-\delta/2}(\log D)^r\,\frac{dD}{D}<\infty.
\]

The tail integrals, and their derivatives, therefore converge locally
uniformly. Together with the bounded middle interval this proves
\(\mathcal M_W\) holomorphic on all of \(\Omega\), as asserted at
735–741. A separate loss for each compact subset is sufficient; no
uniform majorant at the boundary \(\Re s=\alpha\) is asserted or used.

## 4. Legitimate hypothetical-zero-dependent test

Assume a zero \(\rho\in\Omega\) of the fixed \(L_K(s,\nu)\).
Choose a nonzero nonnegative \(\phi\in C_c^\infty((1,2))\) and set
\(W_\rho(y)=\exp(-\rho\log y)\phi(y)\), using the real logarithm for
positive \(y\). This is an admissible complex smooth test. Its derivative
norms can depend on \(\rho\), which the input permits: once an alleged
zero is fixed, the test is fixed before \(D\) tends to infinity.

Compact positive support makes \(\widehat W_\rho\) entire. With the
source's Mellin convention,

\[
 \widehat W_\rho(\rho)=\int_0^\infty\phi(y)\,\frac{dy}{y}>0.
\]

This selection does not presuppose nonvanishing, require uniformity over
all zero heights, or exchange a limit with a moving test. It merely
ensures the numerator cannot vanish at the single alleged zero.

## 5. Absolute interchange and the Euler identity

For \(\sigma=\Re s>1\), the absolute sum of termwise integrals is at most

\[
 \left(\int_0^\infty|W(y)|y^\sigma\frac{dy}{y}\right)
 \sum_nN(n)^{-\sigma}<\infty.
\]

Here \(|\mu(n)\nu(n)|\le1\), and the ideal zeta series converges
absolutely for \(\sigma>1\). In this fixed field that convergence also
follows directly from the lattice bound
\(\#\{n:N(n)\le R\}=O(1+R)\). Fubini is thus justified. The
substitution \(y=N(n)/D\), including the reversal of endpoints, gives

\[
 \mathcal M_W(s)=\widehat W(s)
 \sum_{(n,S)=1}\mu(n)\nu(n)N(n)^{-s}
 =\frac{\widehat W(s)}{L_K^S(s,\nu)}\quad(\Re s>1).
\]

The reciprocal Euler product is absolutely convergent there, so this
uses no continued reciprocal at an unknown zero.

For each finite omitted factor and \(\Re s>0\),

\[
 |\nu(\mathfrak p)N(\mathfrak p)^{-s}|
 \le N(\mathfrak p)^{-\Re s}<1.
\]

At conductor primes the zero-extension convention gives
\(\nu(\mathfrak p)=0\), so the factor is 1. The finite product and its
inverse are holomorphic and nonvanishing throughout \(\Re s>0\).

## 6. Meromorphic identity and the principal pole

The source invokes classical Hecke continuation at 751–754. Since
\(\mathcal M_W\) is holomorphic and \(L_K^S\) is meromorphic on the
connected domain \(\Omega\),

\[
 G(s)=L_K^S(s,\nu)\mathcal M_W(s)-\widehat W(s)
\]

is meromorphic there. It vanishes on the open subset \(\Re s>1\).
The meromorphic identity theorem gives \(G=0\) throughout \(\Omega\).
This multiplication formulation is valid even at the alleged zeros;
it does not assume the continued reciprocal is holomorphic.

For \(\nu=1\), \(L_K^S\) has a simple pole at 1 with nonzero residue.
The equality to the entire numerator makes the product's singularity
removable. Writing \(L_K^S(s)=a/(s-1)+O(1)\), \(a\ne0\), and
\(\mathcal M_W(s)=m_0+O(s-1)\), shows \(am_0=0\), hence
\(\mathcal M_W(1)=0\). This is a consequence of the identity, not an
extra principal cancellation assumption. The pole at 1 is not a zero.

At any alleged zero \(\rho\) the continued \(L_K^S\) is regular and
vanishes, while \(\mathcal M_W(\rho)\) is finite. Evaluation gives
\(0=\widehat W_\rho(\rho)>0\). For a nonprincipal character this also
handles \(\rho=1\). The pole qualification is a worthwhile explicit
clarification of the source's compressed identity-theorem sentence,
not a missing theorem or obstruction.

## 7. Classical imports and the Dirichlet endpoint

The continuation fact was checked directly against Bjorn Poonen's
[MIT *Tate's thesis* notes](https://math.mit.edu/~poonen/786/notes.pdf),
Theorem 5.22 and Section 5.11 (printed pages 38–39): the completed Hecke
function continues meromorphically, with exceptional norm characters.
For finite-order characters the complex-place restriction is trivial,
because \(\mathbb C^\times\) is connected. Only the principal character
can supply the positive-half-plane pole at 1. Removing the complex
gamma factor, which is holomorphic and nonzero in \(\Re s>0\), gives
the finite Euler-product continuation needed here. This uses a
classical theorem; neither its full proof nor Hecke's original paper
was independently validated by this audit.

Paul Garrett's official [number theory notes, Section 30, Theorem
30.1](https://www-users.cse.umn.edu/~garrett/m/number_theory/Notes_2011-12.pdf)
provide a second formulation through global zeta integrals: the
continuation has only the trivial-character pole terms at 0 and 1.

For the final Dirichlet implication, [NIST DLMF Section
25.15](https://dlmf.nist.gov/25.15) supplies the imported continuation
and nonvanishing-at-1 statements. Nonprincipal Dirichlet functions are
entire; principal ones have a simple pole at 1; induced-modulus Euler
corrections are finite. Away from 1 there is no pole that can cancel a
zero of either factor in the norm-lift identity. At 1, if one factor is
principal, the other primitive factor is \(\chi_{-3}\), whose value is
nonzero. Its positivity is also seen directly from the convergent
positive paired series
\(\sum_{j\ge0}((3j+1)^{-1}-(3j+2)^{-1})\).

The full norm-lift Euler calculation, conductor distinction, and
fixed-character extraction are recorded in
[the extraction and base-change ledger](FINAL_EXTRACTION_AND_BASE_CHANGE_20261012.md); they are not silently substituted
for an independent proof audit here. The theorem's qualitative common
half-plane follows from the saving and these classical imports. It
requires no uniform constant in the conductor or zero height; any
quantitative corollary would require a separate uniformity argument.
