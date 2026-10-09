# Scoped review of the zero integral adaptive continuation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Coordinating derivation, two parallel scoped audits and finite replay are
same-model internal checks. They are not independent specialist validation
or formal proof replay.

Reviewed working-tree notes based on repository commit
480581447dcd3e93c9c2f9c22a050d9c5100ff9d:

- [11: Profile and adaptive reduction](../short_families/notes/11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md).
- [12: Factor selection barrier](../short_families/notes/12_SHORT_FAMILY_FACTOR_SELECTION_BARRIER_20261008.md).
- [13: Latest continuation](../short_families/notes/13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md).

## Outcome

No substantive error was found in the reviewed reductions after the
row-count clarification below. The derivative profile removes the
principal correction without losing the relevant Mellin detectors.
The radical-dependent cutoff removes the actual small-product sector
under the complete Schwartz weight. A selected prime-by-prime tail
piece still violates every useful separate-piece budget.

The adaptive signed tail estimate is not proved. Neither the finite
checks, the selected-piece obstruction nor the generic sieve comparison
supplies a stronger zero-free strip or descent to RH.

## Mathematical checks and limits

| Claim | Check | Limit |
| --- | --- | --- |
| \(W=(1+t\partial_t)V\), \(\int W=0\) | Integration by parts gives \(\widehat W(s)=(1-s)\widehat V(s)\); \(V=t^{-\rho}\phi\) supplies a detector for every \(\rho\ne1\) | The point \(s=1\) retains its classical separate treatment |
| Conditional scalar extraction | Note 1's finite mask recurrence keeps the same signed or complex profile; the common Mellin zero removes no relevant detector | No new short-family moment is supplied |
| Sharp all-profile recovery | Differentiate the finite smooth sum, integrate \(A_{u,V}/t\), then use finite-row Minkowski with \(h+a<1\) | Uses explicitly retained fixed-character \(o(t)\), without conductor uniformity; does not recover arbitrary Schwartz all-row norms |
| Combined modulus \(L_u=Q_uNE_u\) | Good valuations nonzero modulo six enter the conductor; positive multiples of six enter only the extra deletion mask | Uses imported native character presentation and tame conductor structure; the fixed bad part is bounded |
| Weighted radical mass | The good-prime Euler factors \(1+4q^{-1-\delta}/(1-q^{-\delta})\) converge for every \(\delta>0\); bad-prime factors are finite in number | Infinite convergence is an analytic argument, not a finite numerical certificate |
| Adaptive completion | Full nonzero-frequency Poisson bound costs \(\tau(E_u)\sqrt{Q_u}(L_u/X)^A\); insert \(X=D/Nd\), sum \(|c_z|\), then use the weighted mass | Depends on the inherited primitive Poisson formula and Schwartz decay |
| Empty cutoff | If \(Y_u<1\), the small sector and its correction are exactly empty | The entire convolution remains in the tail on those rows |
| General-profile recombination | Summing all \(c_z(d)\lambda_u(d)/Nd\) gives the ordinary square \(M_z(u)^2\) | It is not \(|M_z(u)|^2\); neither recombined term is estimated |
| Coherent support | Exact \(abm\) support and \(Na,Nb\le\sqrt{CD}\) give the displayed free and Möbius-factor lengths | Substituting \(Nu\le H\) is confined to an inner ball or row shell |
| Prime-by-prime tail obstruction | Two quantitative prime-ideal integrations give \(4D/\log^2D\) times \(\int W(t)\log(C/t)\,dt=\int V>0\); coherent masks equal one | Specializes to \(\nu=1\), actual selected factor coefficients; not a lower bound for full \(m=1\), full tail or Möbius energy |
| Grouped generic sieve | Cube-free \(c_z\) columns are sixth-power-free; Cauchy pays \(Z\), \(m\)-summing pays \(Z\), coefficient norm pays \(X\), division by \(D\asymp XZ\) leaves \(Z\mathcal L(H,X)\) | Its supplied \(DH^{1/6}\) term is an upper-bound diagnostic, not a Möbius lower bound |
| Row-dependent threshold in grouped \(d\) | Fixed binary intervals and the sieve on each interval give a logarithmic maximal partial-sum loss | Does not permit arbitrary selectors inside previously completed kernels |

The first parallel scoped audit checked note 11, including the
fixed-row boundary, norm recovery, adaptive mass, ordinary square and
support table. The second checked note 12, including both prime
integrations, masks, cutoff, bilinear normalization and maximal threshold.
The coordinating review also checked the extraction exponents
\(5/6+a/2\) and \(47/54+a/2\).

One clarification was incorporated: the count
\(\#\{Nu\le H:L_u\le R\}\ll RH^\delta\) follows directly from the
radical Euler product and \(\sum_{Nu\le H}1/N\operatorname{rad}_S(u)
\ll H^\delta\). The smaller mass with weight \(Q_u/L_u^2\) alone
would not establish this count on principal rows.

## Imported inputs

The exact truncated-inverse factorization, native symbol reciprocity,
primitive character presentation and Poisson formula retain the source
status in [the preceding review](SHORT_FAMILY_FACTORIZATION_REVIEW_20261008.md).
The physical sextic sieve retains the status in
[the core and overlap review](SHORT_FAMILY_CORE_AND_OVERLAP_REVIEW_20261008.md).

For the new logarithmically precise obstruction, the statement of
[Das--Kadiri--Ng, Corollary 1.4](https://arxiv.org/html/2508.09480v1)
was inspected. In the fixed trivial extension of
\(K=\mathbb Q(\sqrt{-3})\), it bounds the weighted prime count by an
exponential error plus a possible exceptional-zero term. Subtracting
prime powers, partial summation and absorption of a fixed real zero
give note 12's prime ideal theorem. Its proof was not replayed.
This input is not used for the adaptive small-sector estimate.

The fixed-character Möbius boundary used only for sharp-profile
recovery is expressly an analytic input. Direct Mellin detection
does not depend on that recovery.

## Reproducible finite evidence

The new standard-library
[checker](../numerics/check_short_family_mean_zero.py) passes
**4,812 exact assertions in 28 groups**. Two fresh coordinating
subprocess runs reproduced the
[retained JSON](../numerics/short_family_mean_zero_record_20261008.json)
byte-for-byte, agreeing with the implementation audit's replay.

The 3,144-byte record has SHA-256
a92bd4c77831873245828d8974f325151ec64ae69aa3822a2bc826982cdbd8e3.
The checker has SHA-256
e88b2bc2ca477977a9d9abe7fbbb659671d6be8f78fb66d6203c2905d3997ab1.

Checks cover:

- Rational polynomial integration, zero integral, Mellin factor,
  logarithmic moment and product Jacobian.
- Finite scalar derivative identity and exact adaptive convolution
  in a 36-element ideal-style monoid with complex sixth-root twists
  and deletion zeros.
- Distinct row cutoffs, an explicitly empty small sector and
  vanishing principal correction.
- Valuations from zero through twelve, conductor/mask disjointness,
  radical weights and finite geometric factors including
  \(\tau(E)^2\).
- Rational adaptive error powers, coherent support exponents and
  the generic bilinear quarter-power gap.

The polynomial diagnostic is not a compactly supported \(C^\infty\)
profile; its endpoint vanishing is enough for the checked finite
calculus identities only. Formal monoid twists are not actual residue
symbols. No tolerance or floating approximation is used.

These tests do not certify an infinite Euler product, conductor theorem,
Poisson decay, prime ideal asymptotic, large sieve, unbounded moment or
zero-free region. No large derived data or third-party PDF is saved.

## Remaining obligation

Prove note 13's adaptive tail moment at \(h=4/5\), \(a<1/12\),
for every derivative profile and one fixed positive cutoff buffer.
The proof must preserve the cancellation between the selected
prime-by-prime tuples and their compensating factor classes.
The original transformed low-overlap residual remains another route.
Neither required estimate has been closed by this continuation.
