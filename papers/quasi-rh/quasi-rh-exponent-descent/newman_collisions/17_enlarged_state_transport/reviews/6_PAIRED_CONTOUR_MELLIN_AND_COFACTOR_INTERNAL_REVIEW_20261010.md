# Internal review of paired contours Mellin endpoints and cofactor transfer

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. Root derivations, separate-agent audits and replays
are internal LLM work, not independent mathematical validation.

## Verdict and scope

The continuation supplies the complex-contour and remainder checkpoint
requested in [Note 8](../notes/8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md).
[Note 9](../notes/9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md)
establishes a complete matched representation with explicit remainder
uniform on the stated shrinking sector and its complex physical disks.
[Note 10](../notes/10_MATCHED_MELLIN_BESSEL_TRANSFORM_AND_RAW_CHANNEL_OBSTRUCTION_20261010.md)
derives the incomplete Mellin–Bessel transform and identifies the
otherwise missing endpoint cancellation.
[Note 11](../notes/11_QUASI_RH_PRIME_COUNTING_AND_GROWING_COFACTOR_FILTERS_20261010.md)
strengthens the existing cofactor-filter obstruction conditionally on
the assumed paper's fixed-modulus prime-counting consequence.

The analytic formulas and constants pass root and separate-agent
read-throughs. Two minor Mellin clarifications were incorporated:
\(G(s,\lambda)\) is entire in \(\lambda\) for real \(s\), not asserted
entire in \(s\); the actual sum of absolute theta summands, rather than
only the larger polynomial-parts envelope, proves necessity of the raw
Mellin convergence chamber. There is no new stationary sign, shorter-family
moment estimate, collision exclusion, zero-free region, or RH conclusion.

## Contour and remainder checks

The complex theta series converges locally uniformly in
\(|\Im u|<\pi/8\). Jacobi evenness extends throughout this connected strip.
That licenses the complete full-line contour shift and the cancellation
of the two half-line endpoints. For real frequency the vertical segment
is purely imaginary; for complex frequency both matched contours remain.

The low-source constant is
\((3/4+8/e^2)+(3/4+3/e)=C_{\rm low}\).
The conditions \(tU\le3/8\) and \(t\le1/20\) give the printed
\(\beta=5/8\), tail slope and positive denominator \(b-\beta\).
The real change of variables in the pair has Jacobian \(1/2\), and
the vanished mixed moment of the even absolute density supplies the
factor \(1/4\) in the paired norm. This checks the physical normalization
\(\mathscr L_j(H)=\widehat J_j(2x)\), including \(j=1\).

The separate raw half-plane estimate pays negative raw arguments directly.
In its mixed quadrant the inner factor \(e^{(1-B)h}\) cancels the
outer \(B\)-weight. The low and high contributions are bounded by
\(c^{-5}e^{4U/5}\) times the printed polynomial terms, absorbed by
\(c^{-11/2}\). Both denominators in \(Q_{p,B}\) are positive.

For an omitted product \(nm>M\), splitting the raw exponential into
two halves gives exactly \(e^{-\pi cM}\) times the source with \(c/2\).
The sector condition pays \(tU(c/2)\le3/8+\log(2)/80<2/5\).
Two matched half-lines produce \(2^{13/2}\), and substitution of the
displayed cutoff gives the error \(\varepsilon e^{-2a\Re z}c^A\).
The same \(a\) and cutoff work on the whole disk \(|z-x|\le1/L\).

This construction first establishes complete modular cancellation and
then truncates the shifted integral. It never gives individual raw
channels an evenness they do not possess. Its finite approximation is
not identified with the Fourier transform of a finite raw real-axis
source. The bounds are absolute and do not settle its conditional sign.

## Mellin and endpoint checks

Two independent derivations check the Bessel factor \(1/2\), the overall
Mellin coefficient \(\pi^2/8\), and both endpoint terms
\((\mu-6)K_\nu(a)-aK_\nu'(a)\). The differential readout
\(\partial_\lambda^4-\partial_\alpha^2\partial_\lambda^2\)
retains the signed insertion for \(J_1\).

Changing to the two original source coordinates gives the complete
product \(\xi(q_+)\xi(q_-)/32\). The raw absolute series has chamber
\(\Re\alpha>2+|\Re\lambda|\); the physical line lies outside it.
At zero frequency its individual full-line Mellin terms are positive
multiples of \(\tau(P)/\sqrt P\), so their sum diverges. At \(t>0\),
the \(e^{2ts^2+10s}\) negative-\(s\) tail already destroys absolute
full-line integration of each fixed raw channel. The complete glued
source and the retained half-line construction have no such failure.

The [boundary checker](../numerics/check_paired_boundary_derivative.py)
uses hash-checked 60-digit outward interval sources and complete ranges
on 4,096 cells, with an analytic absolute tail. The root and a separate
agent each replayed it successfully:
\[
0.00474119<J'_{0,P=1}(0)<0.00500393,\qquad
E_{\rm tail}<9.7860\cdot10^{-70}.
\]
The differentiated polynomial and its tail majorant were also checked
algebraically. Its unmatched boundary has leading term
\(-J'_{0,P=1}(0)/(2x^2)\) at fixed contour height, verifying that this
boundary cannot simply be dropped from the raw partial transform.
This calculation proves no complete-theta Fourier sign.

## Arithmetic checks

The October 5 primary source was inspected at its
[prime-counting corollary](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).
Only modulus three is used. The source theorem and this corollary remain
assumed, as in Note 8; their proofs are not audited by this continuation.

The split/inert formula for \(\pi_K\), both partial-summation errors,
the norm compensation and the removed diagonal all check. The improved
PNT error is \(D^{(1+\theta)/2+\eta}\prod(1+q_i^{1-\theta})\).
It extends Note 28's actual-response transfer to every growing \(J\)
allowed by its original norm budget. The extension of its continuum
proof to fixed \(\beta<1/2\) keeps its uniform Taylor error.

The direct Möbius projection uses good primes outside the fixed
exclusion set, retains the unordered-pair factor \(1/2\), and requires
\(\beta<1/4\) for unique cofactors and all physical phases. The coherent
row count gives energy exponent \(87/41\); paying the full coefficient
cost loses \(2\beta\), leaving a strict comparison with \(71/41\) only
when \(\beta<8/41\). The selected filter has not been substituted for the
full actual response.

The [arithmetic checker](../numerics/check_quasi_rh_cofactor_transfer.py)
passes 43 exact rational and coefficient assertions, including distinct
prime ideals with equal norms. Repeated runs reproduce the small record.
Those tests verify bookkeeping; the asymptotic transfer is an analytic
argument under the declared PNT premise.

## Remaining analytic target

The matched truncated response now has an explicit uniform error budget.
A sufficient next step is to prove its signed margin exceeds that
budget on the complete physical stationary set, particularly \(H_{xx}=0\)
for the second sign, and then establish the required predecessor coverage.
The present absolute estimates permit that question to be asked on
justified contours. They do not answer it. No manuscript was revised
and no manuscript snapshot was created.
