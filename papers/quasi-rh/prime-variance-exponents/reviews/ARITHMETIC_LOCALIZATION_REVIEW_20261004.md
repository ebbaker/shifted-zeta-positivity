# Arithmetic localization: fresh proof and pilot review

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal same-model review, not independent specialist refereeing.

## Result

**Pass.** I independently checked the proofs in
[Möbius and balanced Vaughan reductions](../notes/MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md)
and audited the
[floating pilot](../numerics/mobius_reduction_20261004/pilot.py).
The stated discarded ranges have \(O(X)\) shell norm, and both retained
arithmetic targets have exactly the original admissible exponents,
including \(\delta=0\). Neither the proof nor the pilot establishes an
actual-prime exponent saving.

One minor wording correction was sent to the drafting agent: the
periodized weight is \(C^4\), not necessarily infinitely differentiable.
Absolute Fourier-series convergence is sufficient for the stated
Poisson argument, so this does not affect the proof.

## Analytic and arithmetic checks

- The zero extension of \(w\) has continuous derivatives through order
  four and bounded, piecewise smooth fifth derivative. Its sixth
  distributional derivative is a bounded interior density plus the two
  jumps of \(w^{(5)}\) as endpoint atoms. The same holds for
  \(v(u)=(\log u)w(u)\), since the support stays away from zero.
  Thus both total-variation constants are finite.

- With Fourier convention \(e^{-2\pi i\xi u}\), the exact constant is
  \(2\zeta(6)/(2\pi)^6=1/30240\). Periodizing
  \(f((k+t)/y)\) gives Fourier coefficients \(y\widehat f(jy)\), whose
  nonzero absolute sum is at most
  \(\|D^6f\|_{\mathrm{TV}}y^{-5}/30240\). This proves the lattice
  estimate for every real \(y>0\); no large-\(y\) qualification is
  needed. Negative and zero samples vanish by the support condition.

- Splitting \(\log k=\log y+\log(k/y)\) leaves the continuum
  \(c_wy\). Substitution \(u=e^{-v}\) gives
  \(c_w=-G'(-1/2)=-H(-1/2)/(2\sqrt\nu)<0\).
  The sign and the nonvanishing are correct. Preparation cancels the
  constant density but does not cancel this logarithmic density.

- The identity
  \(\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d\) has the correct sign and
  includes \(n=1\). Splitting at the real shell-dependent cutoff \(D\)
  while holding it fixed for all \(x\in[X,2X]\) gives an exact
  decomposition. If \(d>D\) and \(w(dk/x)\ne0\), then
  \(k<2BX/D\), so the displayed finite cofactor cap includes every
  term. The terminal hard cutoff \(d>D\) is correctly retained.

- The small-divisor estimate uses only
  \(\sum_{d\le D}d^5\log d\le D^6\log D\).
  At \(D=X^{11/12}(\log X)^{-1/6}\),
  \(D^6=X^{11/2}/\log X\) and
  \(\log D\le(11/12)\log X\), for \(X\ge e\). Multiplication by
  the shell length's square root proves exactly
  \(\|E_{X,D}\|_2\le(11/12)\mathscr C_wX\).
  The logarithmic adjustment is necessary for this stated elementary
  endpoint bound; omitting it leaves \(O(X\log X)\).

- Vaughan's displayed identity follows from
  \(\mu*1=\delta_1\) and \(1*\Lambda=\log\) with the stated plus and
  minus signs. The fourth convolution is exactly the Type II sum with
  \(A_U(m)=\sum_{d\mid m,d>U}\mu(d)\). For \(m>U\ge1\), equivalently
  \(A_U(m)=-\sum_{d\mid m,d\le U}\mu(d)\).
  No integer rounding creates an extra term.

- The first Type I sum is
  \(c_wxM_1(U)+O(U^6X^{-5}(\mathscr C_w\log(2X)+\mathscr C_v))\).
  The second Type I bound keeps the product structure:
  \(\sum_{d\le U}d^5\le U^6\) and
  \(\sum_{r\le V}\Lambda(r)r^5\le(4\log2)V^6\).
  Thus at \(U=V=X^{11/24}\) its amplitude is \(O(X^{1/2})\);
  the first error is \(O(X^{-9/4}\log X)\).
  Both contribute at most \(O(X)\) shell norm. The correct retained
  expression is Type II **plus** \(c_wxM_1(U)\); this linear term
  must not be omitted.

- Once \(V<AX\), the truncated \(\Lambda_{\le V}\) term vanishes by
  support. Both surviving factors exceed \(X^{11/24}\); their product
  is at most \(2BX\), giving the upper bound \(2BX^{13/24}\).
  The strict cofactor restriction \(k<m/U\le2BX^{1/12}\) is correct,
  including integral cutoffs and real shell endpoints.

- The prime-power contribution in the original response is
  \(O(\sqrt x+x^{1/3}\log x)=O(\sqrt x)\), by Chebyshev. This
  establishes its quadratic shell energy. It does not justify
  deleting prime powers from the inner von Mangoldt coefficient of the
  different Type II convolution, a caveat the note correctly retains.

- Each \(O(X)\) norm comparison preserves all \(O(X^{2+\delta})\)
  energy classes for \(\delta\ge0\) in both directions. The estimates
  apply for every sufficiently large real \(X\), with every cutoff
  fixed during integration over its shell. No finite numerical slope,
  density theorem, or generic structural control is substituted for
  the missing signed arithmetic bound.

- The subsequent corollaries leaving room below the limiting cutoffs
  also check. For \(D=X^\theta\), the norm error is
  \(O(X^{6\theta-9/2}\log X)\). At \(\theta=9/10\), this is
  \(O(X^{9/10}\log X)\), with energy
  \(O(X^{9/5}\log^2X)\) and cofactors \(O(X^{1/10})\).
  For \(U=V=X^{9/20}\), the second Type I amplitude is
  \(O(X^{2/5})\), hence norm \(O(X^{9/10})\); its energy is
  \(O(X^{9/5})\). The first Type I error has amplitude
  \(O(X^{-23/10}\log X)\) and is smaller. The surviving factors lie
  in \((X^{9/20},2BX^{11/20}]\). Both discarded sectors are therefore
  strictly below the quadratic energy scale, while the retained signed
  target still needs new arithmetic cancellation.

## Pilot audit and independent checks

The sieve correctly builds \(\mu\) and \(\Lambda\), retaining all prime
powers. I independently expanded the factored polynomial used by the
weight routine using rational arithmetic and matched it exactly to
\(-h'''+h'/4\). The direct-divisor and cofactor arrays have the correct
minus sign and retain every divisor above the integer floor of the real
cutoff. Its practical cap \(N//(D+1)\) omits only empty cofactor sums.
The Type II coefficient array implements the equivalent negative
small-divisor sum above, and the continuum term has the correct sign.

The pilot uses a cutoff factor \(1/4\) by default, recorded in every
row. This is a fixed smaller cutoff than the theorem's unit-factor
choice, which changes constants and retains more cofactors. It is not
an undeclared use of the theorem's exact numerical cutoff.

I replayed scales \(X=1000.25,3000.5\) with 64 and 128 quadrature nodes
into temporary storage. Across those rows, the coefficient identity's
largest absolute discrepancy was \(3.56\cdot10^{-15}\), and the
response identity's was \(8.74\cdot10^{-13}\). The signed-to-diagonal
cofactor energy ratios were approximately \(0.01515\) and \(0.002734\),
respectively. These are finite floating diagnostics, not interval bounds.

As a separate check, I evaluated all four Vaughan convolution terms
directly at \(x=1.37X\) for \(X=1000.25,1300.75\), rather than using
the pilot's preassembled Type II coefficient array. Their sum matched
the original prime response with discrepancies below
\(1.10\cdot10^{-13}\). The fitted linear projection and its shape/scalar
energy split are algebraically correct; floating quadrature is not a
certificate of that split's continuum value.

The original pilot's stated limitations are appropriate: quadrature
agreement is not a rigorous error bound, and observed signed cancellation
does not prove a global exponent. No sieve or large array was retained
by this review.

## Reviewed state

At the initial pass, the arithmetic note SHA-256 was
91d90ebd5a6403f59fd0e7b5eaf6409965084562a79aac0b9b96a926017d6dab.
The pilot SHA-256 was
a31671f8f2b0afc654151b4c642fcbaf673022b34275ffe43263c910a78a0476.
These identify the reviewed versions, not a claim that future editorial
changes retain the same file hashes.

The review did not independently prove the classical identity's
historical attribution or a large-sieve theorem; Vaughan's identity is
proved directly in the note and its use here needs no such external
estimate. The proof of the arithmetic localization itself is
self-contained given the elementary Chebyshev bound and fixed probe
properties already proved in the manuscript.
