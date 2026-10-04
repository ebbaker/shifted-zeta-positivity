# Initial investigation of a smaller variance exponent

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Fresh checks were performed by separate agents using the inherited model.
They are internal checks, not independent specialist refereeing.

## Initial result

The investigation proves an arithmetic localization with a strictly
subquadratic discarded part. It reduces the unresolved actual-prime
problem to a signed sum with small cofactors, using the exact Möbius
divisor identity for von Mangoldt coefficients. A finite pilot confirms
the identities and detects substantial cancellation between the retained
cofactor responses. No fixed global delta below one is proved.

The main new statement has a particularly simple form. Keep the fixed
weight w of the [manuscript](../manuscript.tex), and for each real X set

\[
D=X^{9/10},\qquad K=\lfloor2B X^{1/10}\rfloor,
\]
\[
R_X(x)=-\sum_{k\le K}\sum_{d>D}\mu(d)\log d\,w(dk/x),
\qquad X\le x\le2X.
\]

All terminal support restrictions remain in the weight and in d>D.
Then, unconditionally and for every sufficiently large real X,

\[
\boxed{\quad
\|V_g-R_X\|_{L^2(X,2X)}\ll_g X^{9/10}\log X.
\quad}
\tag{1}
\]

In particular the discarded energy is
O(X^(9/5)(log X)²)=o(X²). Every admissible exponent 2+delta, delta≥0,
is therefore preserved in both directions by R_X. The normalized norms
also differ by o(1):

\[
\left|\frac{\sqrt{\mathcal V_g(X)}}X-
\frac{\|R_X\|_2}X\right|\ll_g X^{-1/10}\log X\longrightarrow0.
\tag{2}
\]

This is a power saving for the discarded arithmetic sector. It places
every possible superquadratic contribution in the retained signed sum;
it does not yet bound that sum.

## Why the elimination is rigorous

The elementary exact identity and the fixed probe's lattice cancellation
are the two ingredients:

\[
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d,\qquad
\left|\sum_{k\ge1}w(k/y)\right|
\le\frac{\|D^6w\|_{\rm TV}}{30240}\,y^{-5}.
\]

The second statement follows from Poisson summation, zero mean, and the
sixth distributional derivative, including its endpoint atoms. Summing
the absolute bound over d≤D gives the discarded amplitude
O(X^(-5)D^6 log D), and hence shell norm
O(X^(-9/2)D^6 log D). This proves (1) at D=X^(9/10) without any
unproved cancellation estimate for μ.

One can reduce the cofactor ceiling further to
O(X^(1/12)(log X)^(1/6)) by taking
D=X^(11/12)/(log X)^(1/6). The remainder then has O(X) norm rather
than o(X). Larger logarithmic denominators recover o(X) while retaining
the power 1/12. These tradeoffs and explicit constants are proved in the
[arithmetic localization note](MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).

The advance over the previous generic countermodel is the use of exact
identities of the actual Möbius and von Mangoldt functions. The proof
identifies and bounds the discarded range, rather than simply giving a
new name to an unestimated residual. No claim that this localization is
new in the literature has been established or is made.

## A second, balanced arithmetic formulation

The same note proves a Vaughan reduction. With U=V=X^(11/24), put

\[
A_U(m)=\sum_{d\mid m,\,d>U}\mu(d),\qquad
B_X(x)=\sum_{m>U,n>V}A_U(m)\Lambda(n)w(mn/x),
\]
\[
c_w=\int w(t)\log t\,dt=-\frac{H(-1/2)}{2\sqrt\nu}\ne0,
\qquad M_1(U)=\sum_{d\le U}\frac{\mu(d)}d.
\]

Then \(\|V_g-[B_X+c_wM_1(U)x]\|_2=O_g(X)\), and both factors
lie between X^(11/24) and 2B X^(13/24). The slightly wider choice
U=V=X^(9/20) gives O(X^(9/10)) norm error and factors between
X^(9/20) and 2B X^(11/20).

The nonzero logarithmic continuum is essential. Dropping it would
incorrectly label every Type I term negligible. An equivalent grouping
has coefficients μ(m) and
b_V(n)=sum_(r|n,r>V)Λ(r), with 0≤b_V(n)≤log n. This makes the
prime-specific Möbius cancellation needed by a bilinear approach explicit.

As a supporting result, a three-length extrapolation of the original
short-interval response,

\[
R_{6,h}=\frac{V_h-20V_{h/2}+64V_{h/4}}{45},
\]

has O(X) norm error at h=X^(11/12). The
[higher-order reconstruction note](HIGHER_ORDER_SHORT_INTERVAL_RECONSTRUCTION_20261004.md)
proves this with a positive Peano kernel, full endpoint accounting, and
a precisely sourced Brun–Titchmarsh cap bound. It enlarges the available
interval length; it is not itself an arithmetic saving.

## What the pilot establishes

The [reproducible numerical package](../numerics/mobius_reduction_20261004/README.md)
uses actual Möbius and von Mangoldt coefficients at six noninteger shell
origins from 1000.25 through 300000.5. It retains 25–44 cofactor channels
with a fixed smaller prefactor in the 11/12 cutoff. The coefficient
identity, direct response identity, and balanced continuum/shape split
were checked independently. The 128/256-node quadrature refinements
agree to the recorded floating tolerances.

Across these six cases the signed cofactor energy is only about
0.27%–1.52% of the sum of the individual cofactor energies. The low-divisor
energy divided by X² lies between about 6.82e-6 and 0.001711. These
observations favor retaining cofactor cross terms in a future estimate.
They are finite floating diagnostics, not interval certificates, evidence
of an asymptotic exponent, or a claim that the ratios keep decreasing.

The balanced pilot also separates
\(\|B_X-\lambda_Xx\|_2^2\) from
\((7/3)X^3|\lambda_X+c_wM_1(U)|^2\), where
\(\lambda_X=\langle B_X,x\rangle/(7X^3/3)\).
This preserves the required scalar cancellation and identifies the
remaining fluctuating part without hiding it in a fitted slope.

## The arithmetic obligation that remains

The selected next target is one fixed κ>0 in

\[
\boxed{\quad
\int_X^{2X}|R_X(x)|^2\,dx\ll X^{3-\kappa}L(X),
\qquad L(X)=X^{o(1)},
\quad}
\tag{3}
\]

for all sufficiently large real X, with the complete d>D and k≤K bands.
For 0<κ≤1, the elementary norm transfer gives delta=1−κ when L is
bounded, and every delta>1−κ for an unbounded subpower L. The subsequent
[continuation](SIGNED_MELLIN_CONTINUATION_20261004.md) proves that the
manuscript’s fixed-probe spectral equivalence then recovers the endpoint
delta=1−κ even for unbounded L. The same target can be posed for the
centered balanced sum. In either form it must retain the actual signs.

The [bounded primary-source search](BILINEAR_INPUT_SOURCE_AUDIT_20261004.md)
identified a precise conditional Type II major-arc lemma in the recent
higher-uniformity literature. Its known applications to μ and Λ supply
logarithmic savings. Obtaining a power by that route would require a
new polynomial Dirichlet-polynomial estimate, including the low Mellin
frequencies, or a signed argument avoiding that stronger uniform
hypothesis. The power-saving divisor-function cases do not provide a
prime estimate. The source audit spells out the input, ranges, exceptional
measure, and missing hypothesis.

Generic bounded coefficients in the same balanced range can have cubic
energy: indicators of a small positive-sign rectangle around m,n≈sqrt X
already give such an example. Thus balanced factor sizes and coefficient
norms alone cannot close (3). The next analytic attempt must use μ's
arithmetic signs or the exact convolution structure. Further numerical
sweeps without a proposed signed inequality would not settle this gap.

## Checks and recorded status

- [Fresh arithmetic proof review](../reviews/ARITHMETIC_LOCALIZATION_REVIEW_20261004.md): passed, including strict subquadratic cutoff variants, support caps and the Type I continuum.
- [Independent code and reconstruction review](../reviews/MOBIUS_PILOT_REVIEW_20261004.md): passed; includes independent sieve, polynomial, divisor and Vaughan checks.
- Higher-order reconstruction was checked by a separate agent; formatting and the definition at subsidiary lengths h/2,h/4 were corrected.
- Primary arithmetic references were checked against the identified author texts; no exhaustive priority claim is made.
- The manuscript remains the existing draft. These results are research notes for a subsequent manuscript revision, so no replacement source or draft snapshot was created.

This first investigation has produced proved arithmetic sector bounds,
two explicit surviving targets, and a checked diagnostic of their signed
cancellation. The first global actual-prime exponent below one and an
exponent-descent rule remain open.


## Continuation: signed Mellin localization and endpoint recovery

The [next investigation note](SIGNED_MELLIN_CONTINUATION_20261004.md)
proves that the retained signed response can be restricted to Mellin
frequencies |t|≤X^(1/12)log X with o(X) shell-norm error. Together with
the existing divisor elimination, this preserves every admissible
variance exponent, including the quadratic endpoint. The note displays
the exact central quadratic kernel with all arithmetic caps and signs.

An exact Mertens-function integral sums the cofactors before applying a
bound and retains the hard-cutoff boundary. Its nonzero lattice moment
is precisely the c_w required by the Vaughan continuum. Available global
Mertens estimates still yield only subpower savings. A further pole-order
check shows that bounding individual cofactor channels at an exact
endpoint would exclude boundary zeros that the signed prime response
permits; preserving cross terms is therefore analytically consequential.

The continuation also proves two conditional implications. A global
X^(3−κ)L(X), L=X^(o(1)), estimate for any quadratically equivalent
response would give the exact endpoint bound X^(3−κ), for 0<κ≤1.
The fully uniform real-block Type II hypothesis proposed in the source
audit already contains a stronger fixed zero-free strip in its t=0
slice. Both observations refine the research target; neither supplies
a positive κ. The remaining selected task is a direct signed bound for
the central form, or for the correctly centered balanced form.

A [fresh internal review](../reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md)
checks the derivations and quantifiers. No additional numerical sweep,
manuscript revision, draft snapshot, commit, or push was made.
