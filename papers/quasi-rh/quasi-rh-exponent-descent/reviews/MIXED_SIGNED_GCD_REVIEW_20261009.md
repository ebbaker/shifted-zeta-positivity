# Cross-review of the signed high gcd reduction

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. This is same-model internal
validation, not independent specialist review or formal verification.

Reviewed the staged note 14_SIGNED_HIGH_GCD_REDUCTION_20261009.md and
check_mixed_signed_gcd.py, with their phase dependency. Replayed the
checker, including the final buffer and completion budget additions:
all 2,161 assertions passed. No mathematical blocker found.

The exact fixed-gcd identity is correct. Coprimality inversion acts on
the initially unrestricted squarefree cofactor pair, with \(v,w\) allowed
to share primes after extracting \(h\). The signs \(\mu_F(h)^2\) from the
original coefficients disappear, leaving the inversion sign \(\mu_F(h)\).
The character phases leave \(|\psi_u(h)|^2\), and the exterior
\(|\psi_u(g)|^2\) remains. Consequently reindexing \(q=gh\) gives precisely
the partial divisor coefficient in (22), including its strict gcd
inequality and both signs. There is no unlicensed positive enlargement.

The additional deletion estimate uses a valid exact Dirichlet
convolution. Its auxiliary \(q\)-smooth coefficient can depend on the
row because only its modulus is used; it does not require an arbitrary
coefficient version of the imported inverse bound. The original profile
is evaluated at a shorter real scale, with the same pure twist and
cumulative frequency allowance. The convergent Euler product at
\(a\ge17/25\) costs only an arbitrary small power of the polynomial norm
of \(q\). This extends the actual buffered all-length input, not a
pointwise estimate assumed solely at the original length. The source's
height admissibility, preliminary buffer choice and derivative scope
remain essential conditions, correctly retained by the note.

The explicit fixed-buffer caveat is necessary and correct. Retaining
\(\kappa=d+\rho\) gives high-gcd exponent
\(1+dr-d/125+\rho(r-1/125)\), rather than treating a fixed positive
buffer as an arbitrarily small loss. The stated \(\rho\le1/100000\)
still leaves reserve greater than \(1/1000\), using the enclosing
\(r<73/100\). A separate allocation for remaining losses is required.

The high-gcd sum has the correct original \(D^{-1}\) normalization:
the convergent \(h\)-sum gives \((D/G)^{1+d}\), and summing gcds beyond
\(G_0\) leaves \(UD^dG_0^{-d}\). The constant \(c\) in
\(G_0=cU^{1/125}\) is necessary: original lower annular supports then
force the strict residual inequality
\(\mathrm N(ab)>U^{2r-2/125}\). The discarded gcd boundary uses \(G\ge G_0\);
no equality is lost. The strict old large-ratio condition is restored
legally by subtracting its absolute small-core portion, instead of
applying a short-inverse estimate to a filtered square.

The reserve calculation is exact:
\[
 \frac{9}{3125}-\frac1{540}
 =\frac{347}{337500}>\frac1{1000}.
\]
Together with the separately cited operational small-core reserve, it
supports the stated error budget after allocating the source and height
losses in their original order. The coarse remaining core exponent
\(173/125\) is also correct.

The compatible finite-prime completion has no subset-filter trap.
Writing \(g=g_0j\), with \(g_0\) prime-to-\(P\) and \(j\mid P\),
the completed condition \(g_0<K=G_0/\mathrm NP\) ensures every prime
state has full gcd \(g<G_0\). Its complementary near-gcd portion is
exactly a union of whole fixed-\(g\) sectors: the predicate
\(\mathrm N(g_{P\text{-free}})\ge K\) depends only on \(g\), and implies
\(\mathrm Ng\ge K\). Thus the same bound for the full \(T_g\) applies
before any absolute summation. With \(\mathrm NP\le U^{1/25000}\), its
reserve is at least \(17107/16875000\). Including the stated fixed
buffer gives
\[
 \frac{17107}{16875000}
 -\frac1{100000}\left(\frac{73}{100}-\frac1{125}
                                  +\frac1{25000}\right)
 =\frac{67940623}{67500000000}>\frac1{1000}.
\]
This boundary estimate relies on the complete gcd sectors and the
retained local inverse input; it is stronger than transferring the
elementary old small-core crossing count to the new ratio edge.

The formal checker includes actual nonzero masks, complex annular
coefficients, both orientations, \(q\)-smooth convolution, strict
cutoff restoration, and the low-gcd regrouping. Its scope warning is
appropriate: these finite weighted identities do not certify native
characters, source analytic estimates, slot witnesses or the surviving
asymptotic correlation. The \(q=1\) term of the signed-square aggregate
is exactly the original selected fourth moment, so taking absolute
values again cannot produce the final \(1/540\) gain. The note identifies
that limitation correctly.
