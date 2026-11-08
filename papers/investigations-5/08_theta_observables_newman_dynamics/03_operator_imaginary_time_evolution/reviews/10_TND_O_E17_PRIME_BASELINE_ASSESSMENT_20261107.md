# E17 r1: assessment of the time-zero prime baseline

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Assessor explicitly
selected **gpt-6.1-sol, ultra**, continuing under the new E17 contract.
This records dispatch, not independent backend verification.

**Disposition: accepted within scope after one explicit integer-index
clarification. No identity, coefficient or sign changed.**
The new arithmetic reduction in
[Decision15](../brainstorm/notes/15_TND_O_B04_R4_SIGNED_METRIC_COMPARISON_20261107.md),
equations (5)–(8), has the stated normalization, pole correction, prime
coefficients and uniform tail. Its positivity consequence is a lower
comparison. The upper comparison needed to exclude a declared defect
remains unproved. This is a distinct internal shared-premise assessment;
[E16 Review09](09_TND_O_E16_LOCALIZED_METRICS_ASSESSMENT_20261107.md) remains
complete and unchanged. Neither root/lead checking nor this continuation
is specialist-independent review.

## Fixed scope and identity check

[Request31](../research-progress/handoffs/31_TND_O_E17_PRIME_BASELINE_ASSESSMENT_REQUEST_20261107.md)
and [inputs31](../research-progress/handoffs/31_TND_O_E17_PRIME_BASELINE_ASSESSMENT_INPUTS_20261107.json)
freeze nine sources. All nine byte counts and SHA-256 hashes matched before
assessment. Eight remain byte-identical at return; the lead then made the
natural integer domain in Decision15(7) explicit for the bounded recheck.
Its original consumed version is 10,947 bytes, SHA-256
`b3b428113430481b5d44741a1d3e502cb954992c55a340cd91a31bc52f07aded`;
the amended version is 10,963 bytes, SHA-256
`1c0cd8672cd8b42010b3760332af2c455c73e10bec9f504ae9a47ba57892ac0b`.
The [clarification receipt](../research-progress/handoffs/31_TND_O_E17_INTEGER_INDEX_CLARIFICATION_20261107.json)
records this authorized lead edit. Reversing that single insertion
reproduces the original frozen byte count and hash; no other source
change is included. Inputs31 is unchanged: 2,959 bytes, SHA-256
`974e432bd40511d1d6a22295a01976fa077bc7a02c3497985155f75e24b5b583`.
Exact input and output records are in
[return31](../research-progress/handoffs/31_TND_O_E17_PRIME_BASELINE_ASSESSMENT_RETURN_20261107.json).
Root policies and the E16 evidence boundary remain in force; the
[result index](../../../../../result-summaries/README.md),
[control screen](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[target rule](../../../../../avoid/01_restating_the_target.md) and
[scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
retain their meanings.

1. **Coordinates and pole.** Xi reflection changes the supplied coordinate
   \(s=1/2+iz/2\) to \(s=1/2-iz/2\), without changing
   \(H_0=\xi(s)/8\). Thus strip heights \(0,4,8\) correspond to real
   parts \(1/2,5/2,9/2\). In the exact xi factorization, constants cancel
   because the two boundary masses sum to one. The zero of \(s\) is at
   \(z=-i\), outside the strip; \(\pi^{-s/2}\) has an affine harmonic
   log modulus; and \(\Gamma(s/2)\) is holomorphic and zero-free on a
   neighborhood of the closed strip. Their log moduli have zero
   boundary-minus-interior functional. Stirling's bound on
   \(1/4\le\Re(s/2)\le9/4\) gives at most linear-plus-logarithmic
   horizontal growth, so exponential Poisson kernels pay their integrals
   and the vertical-side limit. The elementary factors have smaller
   growth. These are the selected classical identities recorded in
   [receipt14](../references/14_TND_O_GREEN_PRIME_BASELINE_SOURCE_USE_20261107.md),
   used with the already accepted Note25 strip argument.

   The factor \(s-1\) has its zero at \(z=i\). By the finite-factor
   identity its contribution is **\(+G(X,1)\)**. This factor cancels the
   zeta pole in xi; it cannot be discarded as harmonic. Logarithms are
   evaluated only on the two boundaries and the zero-free observation
   line, so their separated integrals are legitimate. In particular,
   absolute weighted integrability of the critical-line zeta logarithm
   follows by subtracting the paid elementary/gamma logarithms from
   Note25's lower-boundary \(\log|H_0|\), including at real multiple zeros.

2. **Fourier factor and safe-line coefficients.** For
   \(a=\pi/8\), \(K(x)=(16\cosh(ax))^{-1}\), the substitution
   \(u=e^{2ax}\) gives
   \[
    \widehat K(\omega)
    =\frac1{16a}\int_0^\infty
       \frac{u^{-1/2-i\omega/(2a)}}{1+u}\,du
    =\frac\pi{16a}\operatorname{sech}\frac{\pi\omega}{2a}
    =\tfrac12\operatorname{sech}(4\omega).
   \]
   In particular its mass is \(1/2\), and at
   \(\omega=(\log n)/2\) the factor is \((n^2+n^{-2})^{-1}\).
   The complete safe-boundary minus interior coefficient is therefore
   \[
    \frac{n^{-9/2}}{n^2+n^{-2}}-n^{-5/2}
    =-\frac{n^{-5/2}}{1+n^{-4}}.
   \]
   Evenness of \(K\) retains exactly
   \(\cos((X/2)\log n)\), without an extra phase or factor of two.

3. **Euler logarithms and complete index.** On both safe lines,
   \(\Re s=5/2,9/2>1\), the absolute Euler logarithm expands into prime
   powers. Reindexing gives coefficient
   \(\Lambda_{\rm vM}(n)/\log n\), equal to \(1/k\) at \(n=p^k\)
   and zero otherwise. It lies in \([0,1]\). Hence each series is
   absolutely and uniformly convergent in its imaginary coordinate;
   its product with the integrable Poisson weight is absolutely summable.
   This justifies every series/integral interchange and proves
   \[
    J_0(X)=\mathcal L(X)-P(X)+G(X,1).
   \]
   For the now explicit integer truncation index \(N\ge2\),
   \[
    |P-P_N|\le\sum_{n>N}n^{-5/2}
      \le\int_N^\infty u^{-5/2}\,du
      =\tfrac23N^{-3/2},
   \]
   uniformly in every real center. A real cutoff can equivalently use
   its integer part. No derivative-order or practical-cost assertion is
   contained in this absolute tail. The von Mangoldt symbol is explicitly
   distinct from the Newman threshold, and this Euler reduction is only
   asserted at \(\lambda=0\).

## Consumer boundary and bounded check

Since \(J_0\ge0\), equation (8) has the correct direction:
\(\mathcal L(X)\ge P(X)-G(X,1)\). To exclude a zero in the declared
\((d,r)\) class instead requires the strict upper comparison in
Decision15(9), with margin \(\sin(a)d/\cosh(ar)\). Neither the prime
baseline nor positivity supplies that estimate. Any truncation errors
must fit inside the same defect margin; the uniform prime tail and
Note25's boundary tail pay different errors. Absolute field approximation
near real zeros is not a relative logarithmic estimate.

The Gaussian comparison remains inherited from accepted Note24: its
signal is measured against \(|a_m|^2t\), its variance is \(\kappa t\),
and its resolving schedule conflicts with \(v'=2\). Nothing in this
prime reduction removes those amplitude, width or continuation costs.
The comparison therefore preserves two exact unpaid inequalities rather
than claiming either signed estimate or a new criterion.

One short substantive audit and one bounded check covered the reflected
coordinate, complete harmonic-factor cancellation, the zeta-pole sign,
kernel mass and Fourier scale, coefficient subtraction, prime-power
reindexing, integer-index tail, and both inequality directions. The audit
identified that the integral-test constant is stated for integer truncation
indices. The lead made that hypothesis explicit, and the bounded recheck
accepted it: for an arbitrary real cutoff the bound instead uses its
integer part. **This is the sole clarification; no identity, coefficient,
sign or proof route changed.** Receipt14 is a selected-passage
source-use record, not a full-paper or specialist audit. No new external
source, numerical/symbolic research run, proof-source edit, transcript,
manuscript revision, original-checkout edit, commit or push was made.
Only this review and return31 were written.

The lead can finalize the actual disposition and the two missing signed
inequalities. This identity alone does not make a further exclusion proof
ready. The 46-page E14 manuscript and the completed E16 outputs are unchanged.
