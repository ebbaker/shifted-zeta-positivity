# Critical phase limit and the remaining projection defect

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This synthesis combines three parallel
derivations and a [separate internal review](../reviews/SONIN_CRITICAL_LIMIT_REVIEW_20260929.md).
Same-model checks are not independent specialist refereeing.

## What this continuation settles

The full phase-family smoothed trace is now finite, with uniform
source-weighted frequency tails near the critical endpoint. The arithmetic
pole and zero-crossing terms are also explicit. For the actual orthogonal
Sonin projection, the unresolved issue is how much critical-line mass is
lost through the return operator. An exact comparison model proves that
the local phase data and a prelimit cutoff gap cannot determine that loss.

The detailed proofs are in:

- [Uniform frequency tails](SONIN_PHASE_FREQUENCY_TAILS_20260929.md):
  width-independent rational-factor estimates and full source trace bounds.
- [Critical boundary localization](SONIN_CRITICAL_BOUNDARY_MODEL_20260929.md):
  vanishing small-cutoff and crossing terms, the exact-projection upper
  limit, spectral endpoint concentration, and a solvable countermodel.
- [Arithmetic crossing terms](SONIN_PHASE_ARITHMETIC_CROSSINGS_20260929.md):
  the complete contour comparison, including exceptional lines and the
  full source-weighted phase-bulk limit.

These results supersede the trace-finiteness and frequency-tail gaps in the
[earlier boundary note](SONIN_PHASE_BOUNDARY_TRACE_20260929.md). They do not
prove a positive approximation to the complete arithmetic Weil form or RH.

## Full source control

Keep the earlier notation: \(\Pi_\sigma\) is the actual intersection
projection, \(C_\sigma=\chi\mathcal F_\sigma\chi\),
\(T_\sigma=\chi\mathcal F_\sigma P\), and

\[
L_\sigma=P-T_\sigma^*T_\sigma,
\qquad H_\sigma=L_\sigma-\Pi_\sigma\ge0.
\]

The letter \(H_\sigma\) denotes this return operator, not a source.
For \(1/2<\sigma\le3/4\), the positive frequency measures of
\(\Pi_\sigma,L_\sigma,C_\sigma^2\) satisfy the common bound

\[
\nu([j,j+1])\le C\log^2(2+|j|),\qquad j\in\mathbb Z,
\tag{1}
\]

with \(C\) independent of sigma and j. Local factorization isolates
\(O(\log(2+|j|))\) nearby zeta zeros. Each rational factor has
the same finite half-derivative energy, independently of its width or
orientation. This avoids estimates that deteriorate when a zero approaches
the chosen vertical line. The extension with an explicit pole factor gives
the analogous bound on every bounded sigma strip above one half.

For every \(F\in C_c^\infty\), with arbitrary support size,

\[
B_\sigma[F]=\operatorname{Tr}(C_F\Pi_\sigma C_F^*)<\infty,
\qquad R_\sigma[F]=\operatorname{Tr}(C_F H_\sigma C_F^*)<\infty.
\tag{2}
\]

Schwartz decay of \(\widehat F\) and (1) give uniform tails for
these positive traces. The independent full-source boundary formula is
also valid: its crossing term is the trace-class cutoff product
\(\operatorname{Tr}_\chi(C_\sigma T_\sigma
P|\widehat F|^2(D)\chi)\). No additional assertion that the full
crossing sandwich is trace class is needed.

## The actual projection can only lose critical-line mass

Write

\[
Z_{\rm crit}[F]=\sum_{\rho=1/2+i\gamma}
m_\rho|\widehat F(\gamma)|^2.
\]

Localized analytic factorization, followed by (1), proves

\[
\operatorname{Tr}(C_F C_\sigma^2 C_F^*)\to0,
\qquad \operatorname{Tr}_\chi(C_\sigma T_\sigma
P|\widehat F|^2(D)\chi)\to0,
\]
\[
\operatorname{Tr}(C_F L_\sigma C_F^*)\to Z_{\rm crit}[F].
\tag{3}
\]

Consequently the exact, possibly nonconvergent projection trace satisfies

\[
\boxed{B_\sigma[F]=Z_{\rm crit}[F]-R_\sigma[F]+o_F(1),
\qquad R_\sigma[F]\ge0.}
\tag{4}
\]

Every subsequential limit of its frequency measures is supported on
critical-line zero ordinates, with weights between zero and their
multiplicities. This is stronger than mere existence of an unknown positive
subsequential limit, but it does not determine the weights.

The explicit return measure \(\eta_{\sigma,b}\) from the boundary
note satisfies, for every compact smooth frequency test b,

\[
\eta_{\sigma,b}([0,1-\delta])
\le\delta^{-1}\|C_\sigma T_\sigma b(D)^*\|_{\rm HS}^2\to0,
\qquad \delta>0.
\tag{5}
\]

Thus every remaining return defect moves to cutoff spectral value 1.
The needed uniform control at that endpoint is not a consequence of (5).
The rational model in the localization note has
\(v_\epsilon=-B_\epsilon/B_{1/\epsilon}\), with
\(B_h(t)=(t-ih)/(t+ih)\). It has the same local critical factor and
a positive prelimit gap, yet \(\Pi_\epsilon=0\) exactly and the
entire local trace is lost at spectral value tending to 1. This model
does not determine the actual zeta projection; it rules out the proposed
inference from local information alone.

For each fixed Abel parameter \(0\le r<1\), the positive contractions
\(\Pi_{\sigma,r}\) instead satisfy

\[
\operatorname{Tr}(C_F\Pi_{\sigma,r}C_F^*)\to Z_{\rm crit}[F].
\tag{6}
\]

In particular \(r=0\) gives the source-independent positive family
\(L_\sigma\) with an identified full-source limit. That limit counts
critical-line zeros; it is not unconditionally the complete arithmetic
form. Passing first to the exact projection reverses the order of limits
and may retain the defect in (4).

## Exact remaining arithmetic discrepancy

For a complex source use the entire weight
\(a(z)=\widehat F(z)\overline{\widehat F(\bar z)}\), not a modulus
square at nonreal arguments. Define the absolutely convergent off-line
pairing

\[
Z_{\rm off}[F]
=2\Re\sum_{\rho=\beta+i\gamma:\,\beta>1/2}
m_\rho a(\gamma+i(\beta-1/2)).
\tag{7}
\]

The crossing calculation proves the complete explicit-formula identity

\[
\Gamma[F]-W_{1/2}[F]
=Z_{\rm crit}[F]+Z_{\rm off}[F]-2\Re a(i/2).
\tag{8}
\]

For the prepared sources \(F=(-\partial_x^2+1/4)h\), the pole term
vanishes. Combining (4) with (8) gives the sharpened discrepancy

\[
\boxed{B_\sigma[F]-Q[F]
=-R_\sigma[F]-Z_{\rm off}[F]+o_F(1).}
\tag{9}
\]

Every term is independently represented. This equation neither assigns a
sign to \(Z_{\rm off}\) nor proves cancellation. It shows why vanishing
boundary error by itself would leave the arithmetic question unresolved.
Even if RH were supplied as an additional hypothesis, convergence of the
actual projections would still require the new statement
\(R_\sigma[F]\to0\). No such hypothesis is used in the derivations.

## Next work and decision point

Trace finiteness, weighted frequency tails, and crossing bookkeeping are
no longer the next gates. The next bounded problem is a global property
of the **actual** zeta phase which controls its near-kernel modes as the
cutoff singular value approaches 1. One can seek a lower bound showing
which of the local critical-zero packets survive in the exact kernel,
or a proved nonzero return defect showing that this candidate loses mass.
The local factorization and norm-gap argument cannot supply that step,
as the exact comparison model demonstrates.

Any proposed lower-bound argument must distinguish an approximate kernel
vector from an element of the exact intersection. A small value of
\(\|T_\sigma h\|\) does not bound the distance to its kernel when the
nonzero singular values can approach zero. Source-specific finite tests
cannot settle the all-support statement. An arithmetic argument must also
retain (7), rather than replace the full zero pairing by critical-line
absolute squares.

The raw prime-cutoff candidate remains separate and is not ruled out by
these phase-family results. Revising the family remains legitimate if its
exact kernel loses the required mass. No new numerical campaign, manuscript,
commit, or push accompanies this continuation.
