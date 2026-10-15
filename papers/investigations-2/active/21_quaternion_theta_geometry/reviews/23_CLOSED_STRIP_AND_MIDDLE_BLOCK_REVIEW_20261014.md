# Review of the closed strip extension and middle-block reduction

14 October 2026 (America/New_York). Prepared for Edward Baker with
substantial LLM assistance. Recorded parent model **gpt-6-astra**, reasoning
effort **ultra**, independently verified in the source turn metadata for
`01a13d9a-fea1-7af1-9ca6-51d8429ae89a`. The reviewing agent used inherited
context; its separate runtime model and effort were not independently
verified. This is internal LLM review, not external peer review or formal
verification.

**Assessment: approved within its stated scope. No mathematical correction
is required.**
[Note 32](../notes/32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md)
proves strict full Laguerre signs, the four-jet carrier approximation, and
the two signed cutoff conclusions for sufficiently large height whenever
\(0<t\le1/2\) and \(\theta\ge61/24\). The real boundary \(61/24\) is
included. In particular, the formerly excluded boundary \(8/3\) is now
covered. The result does not prove the interval
\(5/2\le\theta<61/24\). Lemma 3 is a valid implication from its explicitly
unproved middle-block hypothesis, not an unconditional solution of that
remaining interval.

## 1. Source applicability and positive exponent losses

The primary sources were independently inspected:

- Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta
  function*, [arXiv:1408.5794v2](https://arxiv.org/pdf/1408.5794v2),
  Theorem 6 and the discussion of proper subintervals on printed
  pages 20--21.
- Timothy S. Trudgian and Andrew Yang, *Toward optimal exponent pairs*,
  [arXiv:2306.05599v3](https://arxiv.org/html/2306.05599v3), the definition
  in Section 1.1, Lemma 1.1, and the A-process in (1.10).

These supply the five limiting pairs used in the note with arbitrarily
small positive losses. The interval in the exponent-pair definition may
be any subinterval of \((M,2M]\). The exact logarithmic phase has derivative
\((T/(2\pi))y^{-1}\), so it satisfies the derivative hypotheses with zero
approximation error. The required scale condition is satisfied because
\(T\asymp u\) and \(M\le N_{\rm RS}\asymp\sqrt u\).

Bourgain's subinterval discussion permits a completion factor
\(O(\log M)\). This is absorbed by selecting a smaller positive loss
before fixing the final \(\eta\). The exponent-pair theorem is already
stated with arbitrary positive loss; no zero-loss endpoint claim is being
used. Thus (5) is a full maximal bound in the indicated range. No omitted
secondary term or unproved completion rule is needed.

The two A-transform identities in (4) and the increment formulas (6) are
correct. More generally, if final coordinate increments are at most
\(\eta\), their exponent contribution is at most
\(\eta(\log T-\log M)+\eta\log M=\eta\log T\), since
\(1\le M\le T\). Continuity supplies suitable initial losses for the
descendants. Fixed phase normalization constants change only the implied
constant.

## 2. Closed-boundary arithmetic and uniformity

The exponent \(F_{k,l}\) correctly combines the oscillatory block estimate,
the factor \(n^{-1/2-\theta_u/4}\), and the positive heat weight.
Every endpoint value in the five-row table was checked exactly. The
intervals cover \([1/5,1/2]\), and each exponent is a convex quadratic.
Consequently the least endpoint margin

\[
\mu_* = 21807/254720000
\]

controls every point in the corresponding intervals. The perturbation
budget, with \(\eta=\rho=10^{-5}\), is

\[
\rho(1+1/2+1/16+1)=41/1600000.
\]

The remainder \(76399/1273600000\) is greater than \(1/20000\), as
claimed. These are strict inequalities at the actual real boundary
\(\theta=61/24\); setting a previously necessary epsilon equal to zero
is not part of the proof.

The shrinking disc may cross below that real boundary. The paid decrease
\(\theta_u\ge\theta_* -\rho\) covers this. The real-part error costs at
most \(\delta/2\), and the decrease in theta costs at most \(\rho/16\).
The remaining allowance covers the small extension beyond \(\beta=1/2\).
For the final pair, that extension has principal change
\(\theta_u(\beta-1/2)^2/4\); it tends to zero uniformly even when
\(\theta_u\le\ell/2\) grows. The additional real-part error also tends
to zero. Replacing \(T\) by a constant multiple of \(u\) contributes only
bounded factors, since the exponent-pair coordinates are fixed.

The low-index estimate has unperturbed exponent \(121/120\). Its reserve
above \(1+1/240\) survives the disc perturbations. The factor
\((\theta_* -\rho+s)2^{-s/5}\) is bounded uniformly in \(s\ge0\), which
is essential for the theorem's unbounded theta range. The ordinary zeta
tail has the displayed rate from \(\Re w\ge9/8\).

The high-index weight is decreasing for each fixed derivative order at
sufficiently large height. Abel summation uses the arbitrary-interval
bound, including the shortened terminal block. Selecting a pair by the
left endpoint of a block remains valid when its right endpoint crosses
a table boundary: no bound restricted to the right-endpoint coordinate
was assumed. Summing the logarithmically many blocks gives (14).

## 3. Analytic transfer and physical signs

The complete imported Polymath error estimates are still sufficient.
In the positive error sums, the heat factor combined with the shifted
real part is bounded by a constant times \(n^{-1/2}\); the disc error
\(n^{O(1/L)}\) is uniformly bounded. Thus the complete sum is
\(O(u^{1/4})\), giving \(e_A+e_B=O(L^2u^{-3/4})\).
The third error is \(O(u^{-2/5})\), since
\(1/4+(\theta_* -\rho)/16>2/5\). All three errors are paid.

The prior two-branch formula, carrier comparison, and reflection apply
with the new half-plane \(\Re w\ge9/8\). The reciprocal Dirichlet series
gives the lower bound for \(|\zeta(w)|\); fixed-order logarithmic
derivatives remain bounded there. The complete difference in (16) is
analytic, so Cauchy estimates apply even at real points where the
Riemann--Siegel floor changes. The proof never differentiates that floor.
The carrier differentiation from Note 17 consequently yields (2).

The numerical constants in (17) are valid. For normalized component
errors at most \(e=1/8\), the first-pair norm is at least
\(1-4e=1/2\). In each Laguerre expansion, retaining the nonnegative
squared error gives the lower bound
\(1-4e-e^2=31/64\). Multiplication by \(4|Q|^2\) and the appropriate
power of \(\omega\) gives \(31/16\). Since \(\omega\ge1\), this also
gives the stated lower envelope for the physical energy.

The checker uses the weaker normalized Laguerre bound \(15/32\), so its
successful run alone does not verify the sharper constant \(31/64\).
The sharper constant was checked directly from the written expansion.
This distinction does not affect either positivity or the cutoff result.

## 4. Complete cutoff payments

The source moments, the staircase retained domain, and the full pair-tail
identity are unchanged from Notes 19 and 31. Combining the two frequency
squares in the paired identity, including their factor \(1/4\), bounds
the retained form by \(e^{-2ax}\mathsf M_j\mathsf M_{j+2}\).
This retains both pair sectors and all cross terms.

For \(N\ge8\), the omitted region is the complete tail
\(v\ge(\log N)/2\). The source majorant bounds its moments by
\(D_0e^{-cN^2}\). Applying the full omitted-pair identity gives exactly
\(B_j=(\mathsf M_j+\mathsf M_{j+2})D_0+D_0^2\), including the two
mixed sectors and the omitted/omitted sector.

The coefficient \(A_j^*\) divides by the explicit nonzero carrier
\(\Gamma^2\), not by a sampled physical energy. It is independent of
\(N\), locally bounded, and not asserted to be height-uniform. The new
energy envelope proves the relative inequality with a spare factor two.
The independently proved full sign gives the additive Gaussian bound
with zero energy loss. No retained jet is assumed stationary merely
because the full jet is stationary.

## 5. The conditional middle-block lemma

Lemma 3 is a correct conditional transfer, including its lower boundary
\(\theta=5/2\). The low cutoff \(\alpha=19/100\) gives the exact
summability exponent \(161/160\); the stated reserve above
\(1+1/320\) and the half-plane \(\Re w\ge11/10\) survive at sufficiently
large height. The zeta tail rate \(19/1000\) is correct.

The four endpoint margins in (22) are strictly negative and correct.
Convexity covers their complete intervals, with suitably small imported
positive losses. The middle hypothesis has fixed overlaps of \(1/175\)
and \(1/100\), absorbing the logarithmic-coordinate discrepancy
\(\log T=\ell+O(1)\).

More explicitly, write \(b=\log M/\ell\), while the hypothesis uses
\(\gamma=\log M/\log T\). After multiplying by the physical weight,
the logarithm of the middle estimate is at most

\[
-\kappa\ell
-\frac{\theta_u-5/2}{4}b(1-b)\ell+O(1).
\]

The bounded correction includes the real-part disc error because
\(\delta\ell=O(1)\). On the fixed strip, the displacement below its
real lower boundary tends to zero and is absorbed by the fixed positive
\(\kappa\). This proves the claimed power saving and subsequent analytic
transfer conditionally. The conservative third-error estimate
\(O(u^{-2/5})\) also remains valid at theta five halves.

The witness \(F_D(2/5;5/2)=9/3980>0\) is a failure of the selected upper
estimates to supply decay. It is not a lower bound on the actual sum or
a theta counterexample. The source-pair comparison at this point and
the required additional improvement \(9/3980+\kappa\) are correctly
stated. The note does not claim that (MB) is necessary, proved, or
equivalent to the full requested signs.

## 6. Replay and scope limits

The [checker](../numerics/check_remaining_strip_lemma.py) was independently
replayed with its output outside the repository:

```sh
python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_remaining_strip_lemma.py --output /tmp/inv21-remaining-strip-review.json
```

All **97 exact rational checks** passed. The replay was byte-identical to
the [stored receipt](../numerics/REMAINING_STRIP_LEMMA_CHECKS_20261014.json).
The three recorded input hashes matched the checker and Notes 19 and 31.
The receipt does not hash Note 32. Relevant SHA-256 values are:

- Checker: `17cc99d63cfb9b203af82f21fe0af6789e3f730ebdd57072305c830c24e0425a`.
- Receipt: `82d8976630c27c865bb3acb7d11e76f300a7eaf0d5b07888b20dc8053065a141`.

The replay checks finite rational arithmetic, not the external theorems,
the infinite source integral, the uniform analytic estimates, or (MB).
All created research and review files remain small. No broad numerical
sweep, quadrature, zero search, new finite-height certificate, manuscript
revision, commit, tag, or snapshot was made in this review. Only this
review file was created.

The finite cover through 112 remains unchanged. The new starting height
is unevaluated, so the finite bridge is not closed. The remaining lower
interval has width \(1/24\) in theta and includes \(5/2\); neither that
interval nor the still smaller cusp is settled. The result establishes
an asymptotic sign domain and a precise conditional continuation, without
an RH conclusion or an optimality claim. Chat capture remains the
parent's responsibility and is not certified by this review.
