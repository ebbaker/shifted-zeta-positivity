# Internal audit of the finite Euler continuation

3 October 2026. Prepared for Edward Baker with substantial GPT-6 (Codex)
assistance in a separate same-model subagent reading. Exact serving variant
and configured reasoning effort were not exposed. This is an internal
analytic audit, not independent specialist refereeing or a priority review.

Reviewed the [residual certificate](../notes/FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md)
and [first-prime analysis](../notes/FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md),
against the [finite Euler identity](../notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md).
The earlier [finite Mellin-defect lemma](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md)
and [prolate certificate](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md)
were read as inherited inputs; their numerical generators were not rerun.

Manuscript integration check by the parent agent: the finite-product
proposition, active-prime comparison, and fixed-place obstruction are now
in [manuscript.tex](../manuscript.tex), with the detailed identity note
cited in its bibliography. The built-in desktop compiler reported success
for source SHA-256
`f48309c50261d01b46023c6255c10ad8e784f8f92329c1357b91e11f9e293fc8`.
The first-prime exploratory calculations remain in research notes and are
not asserted as manuscript theorems.

## Verdict

The two new analytic error estimates pass this audit. They give a route to
certifying the actual boundary correction, including its full spatial
residual and nuclear source tail. They do not certify a correction sign,
prove the proposed mean-functional bound, or establish the support-adapted
Weil comparison. The general primal-dual identity and finite-penalty lemma
are correctly treated as reused tools.

## 1. Resolvent identity, adjoints, and source tail

For a factorization \(X_N=VW^*\), the exact scalar is
\(K_N=2\Re\langle CW,A^{-1}TV\rangle_{\rm HS}\), with
\(A=I-C^2=TT^*\ge gI\). Thus the dual source is \(CW\), without
an additional adjoint or conjugation. With inner products antilinear in
the first argument, direct subtraction gives
\[
K_N-2\Re\{\langle d,Y\rangle+\langle Z,b-AY\rangle\}
=2\Re\langle d-AZ,A^{-1}(b-AY)\rangle.
\]
All maps in these inner products have finitely many Hilbert-space columns;
there is no cancellation of divergent operator traces. Cauchy--Schwarz
and the gap give exactly the stated product of full residual norms.

The improved source-tail coefficient also checks:
\[
(CA^{-1}T)(CA^{-1}T)^*=C^2A^{-1},\qquad
|K-K_N|\le 2c g^{-1/2}\|X-X_N\|_1.
\]
Here \(c\) may be replaced by any justified upper bound for \(\|C\|\).
No Hilbert--Schmidt assumption on \(C\) is used.

The reflected source kernel is \(\Re\kappa_F(x+z)\) on \((0,L)^2\).
Compact smooth support makes it smooth through \(x+z=L\). The scaled
Legendre operator has eigenvalues \(n(n+1)\); its factors \(x(L-x)\)
remove boundary terms at each integration by parts on these smooth
kernels. Parseval therefore gives the stated weighted square sum.
The sum of the inverse weights outside the retained square is
\(2s_rt_{r,N}-t_{r,N}^2\). Cauchy--Schwarz controls the sum of
absolute rank-one coefficients, hence the **trace norm**, not merely the
Hilbert--Schmidt norm. For \(N\ge1\), both integral bounds and the
resulting constants check: \(\sqrt{14}/3\) with \(N^{-3/2}\) for
\(r=1\), and \(\sqrt{30}/7\) with \(N^{-7/2}\) for \(r=2\).
The quantity \(H_r\), coefficient errors, and factorization errors must
still be enclosed in any computation.

## 2. Physical kernel and the missing spatial component

The scaled cosine expansion has the correct transport orientation and
tail \((1+p^{-1/2})p^{-N/2}\). Integrating each cosine against a
normalized interval indicator gives the sine difference in equation (4).
The identity
\(J(z)=z\operatorname{Si}(z)+\cos z-1\) follows by integration by
parts; product-to-sum then verifies the whole-output Gram formula (7),
including its factor \(1/(\pi^2p^{m+n}\sqrt{h_i h_j})\).
The compressed entry (8) has the matching factor \(2/k\).

For an isometric trial map \(E\), selfadjointness of \(C\) gives
\[
E^*C^2E=(E^*CE)^2+((I-EE^*)CE)^*((I-EE^*)CE).
\]
Thus the actual Galerkin matrix is \(I-H\), and replacing it with
\(I-D^2\) omits a positive leakage Gram. The note retains this term.

Writing the off-diagonal block of \(C_N\) as \(R_N\) gives
\((I-Q)C_N^2E=R_ND_N+C_{N,\perp}R_N\). This verifies both
spatial-complement bounds in (16), including the dual combination
\(R_N(V+D_Nz)\). Orthogonality of the trial space and its complement
justifies the square roots in (17). The remaining Euler errors are
\(\tau_N\|U\|_F+\delta_N\|y\|_F\) and their dual analogues,
with \(\delta_N=\tau_N(2c+\tau_N)\), exactly as stated.
The finite center (19), its error (20), and the combined bound (21)
preserve complex adjoints. Their validity does not require the candidate
coefficient solves to be exact or their finite matrix to be positive.

The source projection estimate (23) is a valid nuclear bound, obtained by
splitting each rank-one difference in its two factors. For implementation,
the logarithmic source modes must first be carried unitarily into the
physical coordinates used by the step spaces: a positive mode becomes
\(u^{-1/2}v(\log u)\), while a reflected negative mode becomes
\(u^{-1/2}w(-\log u)\). Equivalently the physical crossing kernel is
\((uv)^{-1/2}\Re\kappa_F(\log(u/v))\), for \(u>1>v\).
This preserves normalization and the nuclear norm. Partition endpoints
must retain the supports of the zero-extended modes, as the note states.

## 3. What remains uncertified

The reported floating-point formula checks are exploratory consistency
checks. This audit did not independently replay them and assigns no
rigorous enclosure or sign to their output. A stable sign in a compressed
calculation would still require the full leakage terms, Euler tails,
source nuclear tail, outward arithmetic errors, and an independently
certified gap in one bound. The cited archimedean certificate supplies a
possible gap input; it does not supply the other errors automatically.

A positive certified correction on one exactly mean-zero prepared source
would refute the rank-one proposal at that support. Negative results on
a finite set of sources would establish only those tests. Even an
all-source sign on the mean-zero subspace would still leave the mixed-term
condition of the inherited finite-penalty lemma. Neither continuation note
claims these unresolved conclusions.
